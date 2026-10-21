---
name: experiment
description: Compare credible implementations or debugging hypotheses using recorded predictions, separate attempts, common verification, and an evidence-based verdict. Use for difficult bugs, repeated failures, optimization, or an explicit comparison request; skip routine edits with one clear solution.
license: AGPL-3.0; see LICENSE
---

# Experiment for Codex

Adapted on 2026-10-21 from hieupth/codeskills at
6f05f460be7f0872503d2f338f071917cbad4e4b. This version removes Claude-only
commands and supports sequential notebook-based attempts in Codex.

## Start with a charter

Read applicable AGENTS.md and relevant entries in .experiments/INDEX.md and
.research/INDEX.md, if present. Before running, create
.experiments/<topic>/CHARTER.md with:

- Observable goal, inputs, material assumptions, and a common verifier.
- Candidate mechanisms and a falsifiable prediction for each.
- Stopping condition: respect the user's budget; otherwise choose a small,
  stated attempt limit suitable for the task.
- Prior failures worth avoiding and a baseline commit if available.
- Whether attempts are sequential or independently delegated.

Do not invent a commit identifier or call same-agent trials independent agent
evaluations. Without Git, with a dirty tree, or when commits are unnecessary,
use notebook records without branches or commits.

## Run separate attempts

Before executing each candidate, start a record under .experiments/<topic>/.
Fill these sections in order:

1. Theory: mechanism that should solve the problem.
2. Prediction: expected outcome and exact check, written before execution.
3. Log: append actual command, observed outcome, artifact paths, and diagnosis.
4. Verdict: KEEP, REJECT, or MERGE, with evidence and the lesson to preserve.

Keep implementations separate. For small pure-function comparisons, separate
functions or files and fresh inputs suffice. For competing repository edits,
use isolated worktrees when available. Inspect Git state first; do not switch
a shared checkout or overwrite user changes. New experiment branches use
codex/exp/<topic>/<candidate>.

Run sequentially unless the user explicitly requests delegation. If delegation
is authorized and available, give executors the problem, their hypothesis,
inputs, and verifier. Keep sibling results private until synthesis.

## Compare and stop

Use the same inputs and scoring rule for all candidates. Keep expected answers
separate from candidate logic. Record raw counts, not just percentages. For
benchmarks, respect permitted access to ground truth. Distinguish classroom
fixtures from held-out tests and production evidence.

When a check fails, diagnose before revising. Do not repeat a hypothesis without
new evidence. If external behavior matters, state the question, consult available
official documentation or source tools, and preserve useful findings under
.research/ when they need to persist.

Stop at the charter's limit or when evidence settles the question. Preserve all
records, including rejected attempts. Add one entry per attempt to
.experiments/INDEX.md and explain the winner, tradeoffs, and uncertainty.
Adopt a winner in application code only within the user's requested scope.

Do not push experiment branches. Cleanup may remove only disposable resources
created for this experiment after useful code and records are preserved.
Never bulk-delete branches or worktrees by name pattern.

## Example

Compare extracting any number after # with extracting an explicitly labeled
policy number. Declare the rule and ambiguous cases before scoring. A result on
synthetic notes establishes only behavior on that fixture; it is not a general
accuracy claim or a PrepBench score.
