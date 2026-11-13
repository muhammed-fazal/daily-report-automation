# Building the flow in Power Automate Desktop (free, Windows)

Action names can differ slightly between versions; use the search box in the actions pane.

**Prep:** create `C:\DailyReport\Input`, `C:\DailyReport\Output` and `C:\DailyReport\Processed`. Copy the files from `sample_input/` into Input.

1. **New flow** → name it `Daily_PO_Summary`.
2. **Get files in folder** → folder `C:\DailyReport\Input`, file filter `PO_Daily_*.xlsx` → output `Files`.
3. **Launch Excel** → "with a blank document" → output `ExcelReport` (the consolidated workbook).
4. **Set variable** `NextRow` = 2. Write headers in row 1 using **Write to Excel worksheet** (PO_ID, Vendor, Category, Plant, Order_Date, Amount_INR, Status, Source_File).
5. **For each** `CurrentFile` in `Files`:
   1. **Launch Excel** → "and open the following document" → `CurrentFile.FullName` → output `SourceExcel`.
   2. **Read from Excel worksheet** → "all available values from worksheet" → output `DataTable`.
   3. **Close Excel** (`SourceExcel`, do not save).
   4. **For each** `Row` in `DataTable` → **Write to Excel worksheet** (`ExcelReport`) at row `NextRow`; then increment `NextRow` by 1.
   5. **Move file(s)** `CurrentFile` → `C:\DailyReport\Processed` (prevents double-counting tomorrow).
6. **Summary cells:** on the report, write formulas such as `=COUNTA(A2:A9999)` and `=SUM(F2:F9999)`.
7. **Save Excel** → `C:\DailyReport\Output\Daily_Summary_Report.xlsx` → **Close Excel**.
8. **Send email** (Outlook action, or the SMTP "Send email" action) → attach the saved report; body = totals (record count, total spend, delayed POs).
9. **Error handling:** wrap steps 5–7 in **On block error** → email "Daily report failed" with `%LastError%`.
10. **Schedule:** use Windows Task Scheduler to launch the flow daily (or a cloud flow with a recurrence trigger if you have a work/school license).

**Validation:** run `python consolidate.py` and confirm record count and total spend match the flow's output.

## Cloud-flow alternative (needs a work/school Microsoft 365 account)
Recurrence (daily, 8:00 AM IST) → List files in folder (OneDrive/SharePoint) → Apply to each → List rows present in a table (data must be formatted as a table) → Append to array variable → Create HTML table → Send an email (V2).
