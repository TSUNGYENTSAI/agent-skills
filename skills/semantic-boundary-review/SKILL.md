---
name: semantic-boundary-review
description: Review domain models, data contracts, APIs, rule layers, ownership boundaries, and computational representations for semantic confusion or premature abstractions. Use when deciding what facts exist, who has authority to decide them, what can be inferred, and how much representation fidelity downstream work needs.
---

# Semantic Boundary Review

Clarify the meaning and authority of information **before** making its implementation structure permanent. A tidy module diagram does not repair an ambiguous domain model.

## Separate meaning from implementation

Identify the important concepts and the distinctions that change behavior. Do not equate raw input, normalized fact, derived value, hypothesis, user policy, and solver decision. Mark assumptions as assumptions; do not silently promote missing requirements into authoritative domain facts.

Ask which actor or system **authors**, **interprets**, **validates**, and **may revise** each consequential fact or decision. Preserve a single clear authority for domain meaning even when representations are duplicated for computation. Distinguish organizational ownership, logical responsibility, and physical process boundaries.

Where implementation is available, trace only the relevant producer-to-consumer transformations, contracts, and tests. Do not invent a missing owner or API because a diagram would look cleaner.

## Set boundaries at real semantic changes

Choose abstractions when they protect a meaningful contract, decision owner, invariant, or independently evolving responsibility—not simply because a generic interface is possible.

Examine representation fidelity against downstream decisions: what information must survive, which approximations are conservative, what is irreversible to discard, and which resolution or performance costs are justified. Record material loss and uncertainty rather than pretending every representation is equivalent.

A simple model may be sufficient for a time-boxed prototype. Stable external contracts, irreversible information loss, and safety-critical semantics deserve stricter review. Do not require full DDD, a new ontology, or multiple services by default.

## Produce a boundary decision, not a framework

Highlight the few semantic distinctions that matter, their authority and transformations, unsafe inferences, and unresolved choices. Recommend the smallest boundary adjustment that protects the intended behavior.

Separate **confirmed as-built**, **proposed design**, and **unresolved** claims. If a dependency is truly undecided, label it; do not supply speculative implementation as fact. Do not change schemas or code unless requested.

See [contrasting decision cases](references/decision-cases.md) for synthetic examples.
