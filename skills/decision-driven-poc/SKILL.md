---
name: decision-driven-poc
description: Frame or review exploratory PoCs, research spikes, feasibility studies, and early technical investment decisions around uncertainty, credible evidence, and stop rules. Use when the goal is to decide whether to pursue a capability, not when implementing an already committed production requirement.
---

# Decision-Driven PoC

A PoC exists to reduce uncertainty that changes a **decision**, not to accumulate demos, features, or platform scaffolding.

## Begin with the investment decision

Define the next decision and the uncertainty blocking it. Keep **technical feasibility**, **engineering suitability**, **workflow or user value**, and **market demand** separate; one does not automatically establish another.

Ask why this uncertainty deserves attention now, what existing alternatives already solve, and what the opportunity cost is. Customer proof is not a universal prerequisite for foundational research; evidence requirements depend on the type of investment.

## Design a bounded learning step

Choose the simplest experiment or representative scenario able to discriminate the key alternatives. State the assumption being tested, the minimum credible observations, material exclusions, and limitations of the setup.

When evaluating a published method or third-party technology, distinguish **claim → mechanism → evidence → limitations → transfer conditions**. A paper benchmark or polished demo is not proof that the method works in the intended workflow. Do not require paper reproduction unless the adoption decision depends on it.

Avoid building generic infrastructure, exhaustive evaluations, or a product-grade interface before the uncertainty warrants that cost. Conversely, do not choose a tiny toy demo that cannot answer the decision.

## Name the stop rule before expanding

Describe what outcomes support **proceed**, **pivot**, **stop**, or **one more bounded test**. Stopping is valid when credible feasibility evidence is sufficient, a decisive constraint is found, or the value case remains too weak to justify investment.

Report what the PoC establishes and does not establish. Do not silently reinterpret a feasibility result as product readiness or claim unknown customer demand is proven.

## Fit the task

Use this skill for exploratory decisions. For sizing an already authorized implementation or migration, use `engineering-scope-review` instead. For rigorous audit of existing results, use `engineering-evidence-review` as needed. Do not automatically chain all three.

Keep outputs concise: the decision, pivotal uncertainty, bounded experiment, sufficiency/stop logic, and next action. Do not create tickets, build prototypes, or initiate external research unless the request authorizes it.

See [contrasting decision cases](../../examples/decision-driven-poc/decision-cases.md) for synthetic examples.
