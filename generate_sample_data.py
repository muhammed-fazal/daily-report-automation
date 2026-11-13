"""Generate synthetic daily purchase-order Excel files (no real company data)."""
import random
from datetime import date, timedelta
from pathlib import Path
import pandas as pd

random.seed(42)
VENDORS = ["Alpha Supplies", "Beacon Logistics", "Coral Industrial", "Delta Packaging", "Evergreen Tools"]
CATEGORIES = ["Raw Materials", "Packaging", "MRO", "IT Hardware", "Logistics"]
PLANTS = ["Kochi", "Chennai", "Bengaluru"]
STATUSES = ["Open", "Approved", "Delivered", "Delayed"]

out = Path("sample_input")
out.mkdir(exist_ok=True)
start = date(2026, 11, 9)

for d in range(5):
    day = start + timedelta(days=d)
    rows = [{
        "PO_ID": f"PO{day:%m%d}{i:03d}",
        "Vendor": random.choice(VENDORS),
        "Category": random.choice(CATEGORIES),
        "Plant": random.choice(PLANTS),
        "Order_Date": day,
        "Amount_INR": round(random.uniform(5_000, 250_000), 2),
        "Status": random.choice(STATUSES),
    } for i in range(1, random.randint(25, 40))]
    pd.DataFrame(rows).to_excel(out / f"PO_Daily_{day:%Y-%m-%d}.xlsx", index=False)

print("Sample files written to", out.resolve())
