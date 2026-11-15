---
name: readable-implementation
description: Implement features, fixes, and refactors with clear domain names, direct control flow, and only justified complexity. Use when choosing an implementation structure or simplifying code that is hard to follow, over-layered, or built around speculative flexibility. Preserve the requested behavior; this is implementation guidance, not a scope-reduction or mandatory review workflow.
---

# Readable Implementation

Make the complete requested behavior easy to find, follow, and change. Optimize for the reader's understanding, not the fewest lines, files, or changed characters. A larger refactor can leave a simpler system; a one-line expression can hide several decisions.

## Follow the behavior

Start with the relevant entry point and trace inputs, decisions, effects, and failure handling. Read the callers and contracts needed to understand the change. Use domain names that explain what the code does, rather than historical project stages or generic mechanism names.

Keep the authorized outcome intact. Simplifying implementation does not authorize dropping features, changing scientific meaning, discarding data, or breaking consumers. Apply the standard within the requested scope; an ordinary feature does not require a repository-wide cleanup.

## Choose a direct implementation

- Prefer ordinary functions, records, collections, explicit branches, and standard library or existing project facilities. Reuse a helper when it fits the behavior; do not preserve an unnecessary layer merely because it already exists.
- Introduce an abstraction when it names a shared domain rule, protects a real invariant, or separates responsibilities that need to change independently. Avoid wrappers that only forward arguments, generic registries for a few fixed cases, and configurable machinery without a current consumer.
- Keep the main path visible. Use intermediate names where they explain a decision. Expand nested conditional expressions and dense comprehensions when a reader must mentally unpack them. Do not split every few lines into a helper that adds another jump.
- Give each rule a clear owner. A strategy chooses an action; the state owner enforces legality; a persistence boundary validates stored data. Repeated checks at independent trust boundaries can be necessary; repeated implementations of the same rule invite drift.
- Keep data in a straightforward representation. Add copying, immutability, identifiers, hashing, or serialization only for a concrete ownership, integrity, reproducibility, or interoperability requirement. A label and a cryptographic identity solve different problems.

A future integration may justify a small stable interface when it is part of the agreed design. It does not automatically justify loaders, registries, version negotiators, or training infrastructure before there is an actual implementation to integrate.

## Simplify without losing meaning

Preserve constraints, tie-breaking rules, random-stream ownership, units, missing values, interrupted execution, and error handling that affect the result. Do not turn unavailable data into zero or remove a correctness check just because it is lengthy.

When changing a mechanism changes observable behavior, say so and update the affected contract. For example, replacing a custom RNG can change seeded trajectories even when both algorithms are reproducible. Compatibility removal requires evidence from the task or consumers; it is not a default cleanup rule.

Update affected callers, tests, documentation, and names together. Remove tests of intentionally retired mechanisms while retaining coverage of promised behavior. Keep historical research claims only with their source and limitations; remove obsolete generated evidence only within the authorized scope. Moving files or formatting code can help readability, but neither proves that unnecessary mechanisms were removed.

## Check the result

Use the relevant behavioral checks for the change, including important failure paths. Do not create a broad test campaign for a trivial edit or claim measured AI accuracy/token improvements from a cleaner diff.

Before finishing, ask: can a new reader follow the behavior from its entry point, identify who owns each decision, and find the place to change it? Explain the concrete simplification, any intentional behavior change, and what validation establishes. No fixed scorecard or approval gate is required.

For before/after examples and cases where complexity should stay, read [implementation examples](references/implementation-examples.md) when useful. These illustrate judgments, not a template every codebase must copy.
