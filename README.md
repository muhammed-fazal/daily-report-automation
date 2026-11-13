# Daily Report Automation (Power Automate + Excel)

Automates a recurring reporting task: pick up daily Excel files from a folder, consolidate them,
generate a summary workbook, and email it, with error alerts.

## Problem
Daily reports built by hand from several Excel extracts are slow and error-prone.

## What it does
1. Reads every `PO_Daily_*.xlsx` file in an input folder
2. Consolidates them into one workbook (adds a `Source_File` column)
3. Produces summary metrics (PO count, total spend, delayed POs)
4. Emails the report; sends a failure alert if anything breaks
5. Moves processed files to a `Processed` folder to avoid double counting

## Repo contents
| Path | Purpose |
|---|---|
| `generate_sample_data.py` | Creates synthetic purchase-order files (no real data) |
| `sample_input/` | Example daily files |
| `consolidate.py` | Python reference version, used to validate flow output |
| `docs/flow_build_guide.md` | Step-by-step flow build |
| `docs/screenshots/` | Add your flow screenshots here |

## Tools
Power Automate Desktop, Excel, Outlook/SMTP, Python (pandas) for validation

## Results
_Fill in from your own test run: files processed, run time vs. manual effort._

## How to run
1. `python generate_sample_data.py`
2. Build the flow using `docs/flow_build_guide.md`
3. Compare output with `python consolidate.py`
