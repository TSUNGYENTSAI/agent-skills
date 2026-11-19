# Sparse-comments policy: why, not a percentage

## Default

Write code that communicates its intent through structure, naming, types, tests, contracts and examples. Comments are not a license to leave a workaround or duplicated logic in place.

## Review procedure

For each new or affected non-generated comment, ask:
1. Does it merely narrate code or repeat a symbol name? If yes, remove.
2. Does it justify a workaround or claim a constraint? If yes, investigate and fix root cause; encode constraint if enforceable.
3. Is it stale or contradictory to current implementation? Update or remove only with evidence.
4. Is information essential and not inferable from code? Keep a short focused explanation and link to its external source where possible.

## Legitimate exceptions

- Standards/protocol requirements, vendor quirks and external contracts whose reason cannot be derived locally.
- Subtle algorithmic or numerical derivations (with paper/assumption), concurrency orderings and safety invariants.
- Security boundary rationale, non-obvious hazards and required legal/licensing notices.
- Public API/docstrings or generated documentation where they are part of the contract.
- Intentional unusual trade-off with an owner and, where possible, an executable regression test.

Never apply a blanket delete or ban to projects without verifying these exceptions. Keep the policy stricter for internal implementation commentary and more permissive for externally constrained interfaces. Count-free: judge information value, not comment ratio.

## Acceptance evidence

A comment-cleanup pass identifies comments removed/preserved and what enforceable constraints replaced them; targeted tests ensure no behavioral change. Do not claim deleting comments itself improves architecture.
