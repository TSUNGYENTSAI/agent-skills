# Verification-first: choose evidence that matches the risk and execution surface

## Evidence ladder

| Surface / claim | Minimum direct evidence | Stronger when risk warrants | What is insufficient alone |
| --- | --- | --- | --- |
| UI behavior | Drive real UI; screenshot before/after and concrete state assertion | Short video capturing trigger to outcome; accessibility/state checks | Final screenshot without action or state evidence |
| CLI/API/service | Real command/request, status/result, persisted readback when applicable | Consumer contract, independent client flow, failure/retry path | Unit tests of internal helper only |
| Geometry/simulation | Reproducible input/seed; result saved/read back; quantitative invariant | Replay/video/spatial visualization and independent evaluator | Attractive picture alone |
| Algorithm/model | Deterministic test case and numeric/correctness property | Property-based/metamorphic tests, baseline comparison, repeated seeds | Training/eval summary without dataset/seed or validity checks |
| Concurrency/lifecycle | Reproduction of ordering/race if possible; explicit transition invariants | Targeted model checking (TLA+ etc.), fault injection | One happy-path unit test |
| Performance | Identical hardware/input/workload and method; repeated measurement | Confidence ranges, profiler trace, measured limiting resource | One run or raw speedup claim |

## Proof-oriented review receipt

- Claim: exactly what user-observable or domain behavior is asserted.
- System under test: commit SHA, environment, input fixture/seed and important flags.
- Procedure: executable command, user steps or model-checker invocation.
- Observation: measured result, artifact path, state reached, assertions satisfied.
- Negative/edge check: what would fail on the known bug or invalid state.
- Limits: what the evidence does not prove; mocks/stand-ins, unavailable dependencies.

Only create artifacts that directly help a reviewer or future regression check. Store raw runs according to project retention policy; link to evidence instead of committing disposable logs/screenshots blindly.

## Project-local verify skill (only if absent)

Adapt pstack's `create-verification-skill` model to the actual repository:
- `Launch`: exact start command and readiness condition.
- `Doctor`: read-only version/health check before driving.
- `Drive`: stable CLI/API/UI commands or selectors, not guessed paths.
- `Evidence`: capture action, resulting state, persistent effect and failure path.
- `Cleanup`: shut down only owned instances and remove only owned scratch state.
- `Feature map`: user's meaningful actions, each with a reachable entry and observable done state.

Maintain it as behavior changes; a stale verification skill is worse than no skill when agents trust it. Do not generate a second harness if existing scripts already meet the need.

## Proportional effort

For high-risk, nontrivial changes, allow verification to consume the largest share of time/tokens; invest until evidence addresses the failure modes. Lauren's reported 70% token usage is an observation about a participant's practice, not a universal quota. Small, low-risk edits need proportionate verification, not mandatory videos or formal proofs.
