"""Python reference version of the flow logic.
Use it to cross-check the Power Automate output (totals should match)."""
from pathlib import Path
import pandas as pd

files = sorted(Path("sample_input").glob("PO_Daily_*.xlsx"))
df = pd.concat((pd.read_excel(f).assign(Source_File=f.name) for f in files), ignore_index=True)

summary = pd.DataFrame({
    "Total_POs": [len(df)],
    "Total_Spend_INR": [round(df["Amount_INR"].sum(), 2)],
    "Delayed_POs": [(df["Status"] == "Delayed").sum()],
})
by_vendor = df.groupby("Vendor", as_index=False)["Amount_INR"].sum().sort_values("Amount_INR", ascending=False)

Path("output").mkdir(exist_ok=True)
with pd.ExcelWriter("output/Daily_Summary_Report.xlsx") as w:
    summary.to_excel(w, sheet_name="Summary", index=False)
    by_vendor.to_excel(w, sheet_name="Spend_by_Vendor", index=False)
    df.to_excel(w, sheet_name="Consolidated_Data", index=False)
print(summary.to_string(index=False))
