# Candidate A

## Theory
The first #digits token is easy to extract, but its label may refer to an account,
invoice, or phone reference instead of a policy.

## Prediction
Fewer than 10/10 matches. Expect account-only and invoice-before-policy notes to
fail. Multiple policies will produce an unjustified single answer.
Check: `.venv\Scripts\python.exe -m examples.compare_policies`.

## Log
Prediction recorded before the first run; execution entry will be appended.

2026-10-21: Ran `.venv\Scripts\python.exe -m examples.compare_policies`.
Observed 5/10 matches. Mismatches: N02, N04, N07, N08, N09.
Evidence: artifacts/02_comparison.json. Diagnosis: no policy context check and
no ambiguity check; invoice/account/phone references can be returned as policies.

## Verdict
REJECT for this lab's declared rule. Keep the implementation as a teaching
baseline. Lesson: a recognizable number pattern does not establish its meaning.
This verdict does not reject the original PrepBench rule, whose requirements differ.
