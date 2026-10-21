# Policy-number comparison: preregistered teaching plan

Written 2026-10-21 before executing the candidates.

Goal: obey the declared synthetic rule: return digits as text only when a note
contains exactly one explicit policy #digits occurrence; otherwise return null
for review. This differs from PrepBench case_005, which asks for any #digits
pattern and converts the result to an integer.

Input: data/notes_cases.json, ten hand-authored teaching examples with expected
answers. Candidate functions receive only the note, never the expected answer.
Verifier: exact-match count including null; display mismatching example IDs.
Candidate A: first #digits, ignoring the label.
Candidate B: one explicit policy label, otherwise abstain.
Predictions: 01-first-number.md and 02-context.md, saved before execution.

Stop after one run of each candidate on this fixture. Diagnose failures and
record the decision; no parameter search or production changes.

Mode: sequential attempts by the same agent using separate pure functions.
This is not a blinded or independent multi-agent study. No baseline commit
exists and the new files are uncommitted: use notebook mode, no experiment branch.
No prior experiment or research index existed. No prior rejected hypothesis.
