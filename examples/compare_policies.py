"""Example 2: compare two rules on a declared synthetic contract."""

import json
import re
from .lab_io import ROOT, file_hash, write_report


def first_number(note):
    match = re.search(r"#([0-9]+)", note)
    return match.group(1) if match else None


def explicit_policy(note):
    matches = re.findall(r"\bpolicy\s*#([0-9]+)\b", note, flags=re.IGNORECASE)
    # More than one labeled occurrence is deliberately left for review.
    return matches[0] if len(matches) == 1 else None


def compare(cases):
    results = {}
    for name, candidate in [("first_number", first_number), ("explicit_policy", explicit_policy)]:
        details = []
        for case in cases:
            prediction = candidate(case["note"])
            details.append({"id": case["id"], "expected": case["expected"],
                            "prediction": prediction, "correct": prediction == case["expected"]})
        correct = sum(item["correct"] for item in details)
        results[name] = {"correct": correct, "total": len(cases), "details": details}
    return {"scope": "SYNTHETIC_LAB_ONLY", "results": results}


def main():
    fixture = ROOT / "data/notes_cases.json"
    report = compare(json.loads(fixture.read_text(encoding="utf-8")))
    report["fixture_sha256"] = file_hash(fixture)
    report["rule"] = "Exactly one explicit policy #digits occurrence; otherwise abstain (null). Keep IDs as text."
    report["limitation"] = "10 teaching cases, not a held-out evaluation, business policy, or PrepBench score."
    destination = write_report("02_comparison.json", report)
    for name, result in report["results"].items():
        print(f"{name}: {result['correct']}/{result['total']} correct")
        failed = [row["id"] for row in result["details"] if not row["correct"]]
        print("  Mismatches: " + (", ".join(failed) if failed else "none"))
    print(f"Report: {destination}")


if __name__ == "__main__":
    main()
