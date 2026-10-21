import csv
from pathlib import Path 

root = Path(__file__).resolve().parents[1]
source = root / "data/raw/customers.csv"

with source.open(encoding="utf-8") as stream:
    rows = list (csv.DictReader(stream))

print(f"Rows: {len(rows)} | Columns: {len(rows[0])}")