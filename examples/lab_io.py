"""Read CSV without guessing types; write named lab reports."""

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_csv_rows(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.reader(stream, strict=True)
        header = next(reader, None)
        if not header or any(not name.strip() for name in header):
            raise ValueError("A nonempty CSV header is required")
        if len(set(header)) != len(header):
            raise ValueError("Duplicate column names are not supported in this lab")
        rows = []
        for values in reader:
            if len(values) != len(header):
                raise ValueError(f"CSV record ending at line {reader.line_num} has wrong column count")
            rows.append(dict(zip(header, values)))
    return header, rows


def write_report(filename, result):
    destination = ROOT / "artifacts" / filename
    destination.parent.mkdir(exist_ok=True)
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return destination
