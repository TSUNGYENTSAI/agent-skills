# Pilot protocol — test the habit, not the length of the prompt

This is an evaluation recipe, not a claim of measured improvement. Do not commit throwaway implementations to production.

## Select two very different repositories

- One production workflow with documented user-facing behavior and existing CI.
- One research/prototype workflow with lighter architecture but reproducible experiments.

## Controlled trials

For each repo, use one bounded task with clear acceptance criteria. Compare an unmodified baseline working session with a separate session that has the engineering-discipline skill. Keep task instructions, model, source SHA, permissions, execution environment and acceptance tests constant where practical. Use a fresh worktree and a fresh session for both arms. Do not let the second session read first-arm diffs, review comments or failures. For stronger evidence, use multiple runs/seeds and rotate order.

## Representative tasks

1. Add a new variant to an existing policy family or plugin interface; measure whether the agent extends the canonical path.
2. Add a new API/CLI scenario; measure whether the agent reuses its runner and produces reproducible evidence.
3. Change a user-facing flow; measure whether it drives the real UI and captures action-to-result proof rather than only a screenshot.

## Judge the result, independently

First require equivalent feature correctness. Only then compare:

- Duplicated domain decisions, alternative execution paths, dead wrappers or retained obsolete code.
- Unsupported new comments, unnecessary explanation comments, and any legitimately preserved constraints.
- Verification evidence quality: can an independent reviewer reproduce it, and does it demonstrate behavior rather than merely compilation?
- Review burden: number of consequential reviewer corrections, not raw tokens or report length.
- Extra cost: time/tool use and maintenance surface. A stronger check that doubles cost without uncovering new risk might be inappropriate for low-risk work.

Record known confounders, missing runs and failed attempts. Treat one comparison as a pilot, not an impact claim.

## Decision at pilot end

Keep or tighten a principle only if it changed a real engineering decision or improved verifiability without unacceptable cost. Remove ritualistic parts that do not. If the agent failed the same way twice, improve the *repo's* API/structure/lint/verification tool rather than writing an ever-longer skill.
