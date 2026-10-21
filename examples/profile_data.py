"""Example 1: measure source data before proposing repairs."""

from collections import Counter
from .lab_io import ROOT, file_hash, read_csv_rows, write_report


def build_profile(path):
    before = file_hash(path)
    header, rows = read_csv_rows(path)
    columns = {}
    for name in header:
        values = [row[name] for row in rows]
        columns[name] = {
            "empty_string_count": values.count(""),
            "whitespace_only_count": sum(value != "" and value.strip() == "" for value in values),
            "dash_count": values.count("-"),
            "literal_zero_count": values.count("0"),
            "zero_with_currency_marker_count": values.count("0đ"),
            "distinct_raw_count": len(set(values)),
            "raw_value_counts": dict(Counter(values)),
        }
    after = file_hash(path)
    return {
        "scope": "SYNTHETIC_LAB_ONLY",
        "source_sha256_before": before,
        "source_sha256_after": after,
        "source_unchanged": before == after,
        "row_count": len(rows),
        "column_count": len(header),
        "null_policy": "No typed null inferred from CSV; empty fields are empty strings.",
        "columns": columns,
    }


def main():
    report = build_profile(ROOT / "data/raw/customers.csv")
    destination = write_report("01_profile.json", report)
    amount = report["columns"]["amount"]
    print(f"Rows: {report['row_count']} | Columns: {report['column_count']}")
    print("IDs: " + ", ".join(report["columns"]["customer_id"]["raw_value_counts"]))
    print(f"Amount: empty={amount['empty_string_count']}, dash={amount['dash_count']}, "
          f"text 0={amount['literal_zero_count']}, text 0d={amount['zero_with_currency_marker_count']}")
    print(f"Source unchanged: {report['source_unchanged']}")
    print(f"Report: {destination}")


if __name__ == "__main__":
    main()
