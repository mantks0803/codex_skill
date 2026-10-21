"""Example 3: propose formatting repairs while preserving source bytes."""

from .lab_io import ROOT, file_hash, read_csv_rows, write_report

KNOWN_STATUSES = ("Thành công", "Thất bại", "Chờ kích hoạt")


def build_plan(path):
    before = file_hash(path)
    _, rows = read_csv_rows(path)
    canonical = {name.casefold(): name for name in KNOWN_STATUSES}
    proposed, review = [], []
    for index, row in enumerate(rows, start=1):
        location = {"data_row": index, "customer_id": row["customer_id"]}
        status = row["status"]
        normalized = " ".join(status.split()).casefold()
        if normalized in canonical:
            target = canonical[normalized]
            if target != status:
                proposed.append({**location, "column": "status", "before": status,
                                 "proposed": target, "reason": "Known demo label differs only in case/whitespace"})
        else:
            review.append({**location, "column": "status", "raw": status,
                           "reason": "Empty status" if not status else "Unknown status; meaning not inferred"})
        if row["amount"] in ("", "-"):
            review.append({**location, "column": "amount", "raw": row["amount"],
                           "reason": "Missing amount or marker; no rule authorizes converting to zero"})
    after = file_hash(path)
    return {"scope": "SYNTHETIC_LAB_ONLY", "mode": "PROPOSAL_ONLY",
            "assumption": "The three known labels are an explicit teaching rule, not a confirmed business policy.",
            "source_sha256_before": before, "source_sha256_after": after,
            "source_unchanged": before == after, "applied_changes": 0,
            "proposed_changes": proposed, "review_items": review}


def main():
    report = build_plan(ROOT / "data/raw/customers.csv")
    destination = write_report("03_repair_plan.json", report)
    print(f"Proposed formatting changes: {len(report['proposed_changes'])}")
    print(f"Items needing interpretation: {len(report['review_items'])}")
    print(f"Applied changes: {report['applied_changes']}")
    print(f"Source unchanged: {report['source_unchanged']}")
    print(f"Report: {destination}")


if __name__ == "__main__":
    main()
