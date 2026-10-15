---
name: engineering-scope-review
description: Review a proposed work item, implementation plan, migration, or refactor for fit to the intended outcome. Use when deciding whether to proceed, revise, split, pilot, defer, or complete the full scope. Avoid both overengineering and artificial under-scoping; this is not a routine gate for every change.
---

# Engineering Scope Review

Judge whether proposed work is sufficient and proportionate to the **actual intended outcome**. A smaller plan is not automatically better; a comprehensive plan is not automatically safer.

## Recover the decision boundary

Identify what the user has already decided, what outcome they expect, and what must be true to call the work done. Respect explicit scope and authorizations; do not quietly substitute a pilot or an expanded platform for the requested delivery.

Distinguish confirmed constraints from assumptions and unknown external dependencies. If repository evidence is available, inspect only the contracts and consumers needed to challenge material scope claims. Do not turn a planning review into an implementation audit without cause.

## Challenge both directions

Look for **under-scoping**: a pilot that never completes an authorized migration, missing consumer changes, omitted acceptance behavior, or work deferred despite foreseeable and costly rework.

Look for **over-scoping**: speculative extensibility, new services or frameworks, duplicate authority, broad compatibility scaffolding, elaborate benchmarks, or approval steps with no demonstrated requirement.

Compare alternatives using current outcome coverage, reversibility, uncertainty, future rework, review risk, and opportunity cost. A bounded experiment is valuable when it resolves a material unknown; it is not a default substitute for completing known work.

Separate necessary work, optional improvements, explicit deferrals, and unresolved decisions. Do not invent extra work items or human review gates merely to make a plan look rigorous.

## Make the recommendation executable

Return a concise recommendation such as **Go**, **Revise**, **Split**, or **Defer**, with only the changes that materially affect the decision. Explain why the rejected scope is too small, too large, or mistimed; show the key tradeoff when alternatives are viable.

When the plan is already adequate, say so and stop. Do not restate an entire proposal, create tickets, modify code, or initiate execution unless requested.

## Counter-judgments

- **Reject premature expansion:** A small internal tool has one known consumer and a clear acceptance test. Adding a queue, plugin framework, and full reliability campaign needs an actual constraint.
- **Reject artificial minimalism:** The agreed outcome is migrating all active consumers to a new contract. A pilot-only change leaves the real migration undone; preserve full delivery unless a genuine blocker requires staging.
- **Prefer staging when warranted:** Irreversible data changes, unknown external consumers, or safety-critical behavior may justify a pilot, migration gate, or stronger validation.

For reusable illustrations, see [contrasting decision cases](references/decision-cases.md). These are synthetic, not measurements of skill effectiveness.
