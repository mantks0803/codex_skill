"""Focused checks for preservation and known teaching answers."""

import json
from pathlib import Path
import tempfile
import unittest
from examples.lab_io import ROOT, file_hash, read_csv_rows
from examples.profile_data import build_profile
from examples.compare_policies import compare, explicit_policy
from examples.repair_plan import build_plan


class LabChecks(unittest.TestCase):
    def test_profile_preserves_ids_and_distinguishes_markers(self):
        report = build_profile(ROOT / "data/raw/customers.csv")
        self.assertEqual((report["row_count"], report["column_count"]), (6, 4))
        self.assertIn("001", report["columns"]["customer_id"]["raw_value_counts"])
        amount = report["columns"]["amount"]
        for key in ("empty_string_count", "dash_count", "literal_zero_count", "zero_with_currency_marker_count"):
            self.assertEqual(amount[key], 1)

    def test_candidates_match_declared_fixture_scores(self):
        cases = json.loads((ROOT / "data/notes_cases.json").read_text(encoding="utf-8"))
        results = compare(cases)["results"]
        self.assertEqual(results["first_number"]["correct"], 5)
        self.assertEqual(results["explicit_policy"]["correct"], 10)

    def test_context_rule_handles_unseen_ids_and_ambiguity(self):
        self.assertEqual(explicit_policy("Invoice #72; POLICY #0007 updated"), "0007")
        self.assertIsNone(explicit_policy("account #1234"))
        self.assertIsNone(explicit_policy("policy #10; policy #20"))

    def test_plan_does_not_change_source(self):
        source = ROOT / "data/raw/customers.csv"
        before = file_hash(source)
        plan = build_plan(source)
        self.assertEqual(file_hash(source), before)
        self.assertEqual(plan["applied_changes"], 0)
        self.assertEqual(len(plan["proposed_changes"]), 1)
        self.assertEqual(len(plan["review_items"]), 4)
        self.assertEqual(plan["proposed_changes"][0]["proposed"], "Thành công")
        self.assertTrue(any(item["raw"] == "31" for item in plan["review_items"]))

    def test_malformed_csv_is_reported_not_silently_skipped(self):
        temp_root = ROOT / ".tmp"
        temp_root.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temp_root) as folder:
            source = Path(folder) / "bad.csv"
            source.write_text("id,status\n001,ok,unexpected\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                read_csv_rows(source)


if __name__ == "__main__":
    unittest.main()
