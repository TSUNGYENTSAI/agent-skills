# Minimal repo-owned engineering contract

Use existing README/architecture guide/AGENTS.md plus source and CI. Avoid a duplicate registry.

## Architecture (only what is not mechanically discoverable)
- Core domain capabilities and decision owners: actual symbols/paths.
- Canonical extension paths and a small working example for each important capability.
- Allowed dependencies and meaningful forbidden imports (enforced if deterministic).
- Externally consumed interfaces, persisted formats and cross-repo limits.

## Verification entrypoint
- How to build/run/doctor the actual app/service/model/simulator.
- Fast local check; CI gates; meaningful end-to-end or domain proof.
- Feature map or benchmark scenarios only when needed; evidence retention location.

## Evolution and lifecycle
- How to move consumers off deprecated APIs and retire old entrypoints.
- Where disposable experiments/raw output belong.
- Which changes require explicit architecture review rather than automatic approval.

## Policy exceptions
- Required comments/docstrings and external protocol/safety constraints.
- Cases where a separate observer, harness or independent evaluator is essential and not a duplicated decision.

## One example of a good MR
- New behavior and expected failure/success evidence.
- Updated canonical path (not a parallel path).
- Tests/evidence artifact pointers.
- Architecture delta or none; remaining unverified areas.
