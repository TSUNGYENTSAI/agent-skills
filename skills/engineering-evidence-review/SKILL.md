---
name: engineering-evidence-review
description: Evaluate engineering benchmarks, tests, PoC reports, demos, and completion claims by matching each claim or decision to supporting evidence. Use when deciding what is proven, what is still unknown, or which validation is worth running. Do not turn every small code change into a qualification campaign.
---

# Engineering Evidence Review

The strength of an engineering claim must not exceed the evidence supporting it. More tests, charts, or documentation are not inherently better evidence.

## Identify the claim and decision

Before recommending validation, establish what is being claimed, who must act on that claim, what conditions it applies to, and what failure would matter. Keep a proposed acceptance criterion distinct from an observed result.

When auditing existing evidence, identify the actual versions, inputs, environments, measurement method, oracle, tolerances, and known exclusions **when relevant to the claim**. Do not present historical runs as fresh results or synthetic examples as representative field evidence.

## Match the evidence to its purpose

Distinguish the questions rather than merging them into one pass/fail status:

- **Execution / feasibility:** Did it run and produce an output under the tested conditions?
- **Correctness / verification:** Does the output satisfy explicit constraints and invariants?
- **Regression / reproducibility:** Did supported semantic behavior remain consistent across changes?
- **Domain validity:** Do the assumptions and result satisfy the real engineering context?
- **Operational / product readiness:** Does the evidence support deployment, use, or value under representative conditions?
- **Human understanding:** Can a reviewer see what changed, why, and which capabilities and limits exist?

These are lenses, not mandatory maturity stages. A local deterministic bug fix may need one focused regression test; a production qualification claim may need several independent forms of evidence.

## Choose the lightest defensible form

Use machine-readable fixtures, comparisons, and receipts for repeatable behavioral checks. Use a concise human-readable explanation for mechanisms, impacts, limitations, and decisions. Neither format replaces the other when both are needed.

Prefer existing oracles and targeted tests. Introduce a new benchmark only when it protects a real invariant or resolves a consequential uncertainty. Investigate changes in meaningful outputs rather than normalizing them away to obtain a green result.

## Report an evidence-calibrated conclusion

State **supported**, **conditional**, or **not established** for each consequential claim; name the tested scope and the main gap. Recommend the smallest additional observation or test that could change the decision, or explicitly say that no additional evidence is presently justified.

Do not turn a result review into a new research program, claim domain acceptance from solver success, or equate CI green with production-ready.

See [contrasting decision cases](../../examples/engineering-evidence-review/decision-cases.md) for synthetic illustrations.
