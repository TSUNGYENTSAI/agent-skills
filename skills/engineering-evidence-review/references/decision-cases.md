# Engineering Evidence Review — contrasting cases

Synthetic, non-proprietary illustrations, not measured agent evaluations.

## A. A passing test suite overclaims readiness

**Evidence:** All 12 synthetic routing fixtures return a feasible path. No representative operating constraints or domain sign-off were tested.

**Claim:** "This is ready for deployment in any facility."

**Expected judgment:** Not established. Execution feasibility on those fixtures is supported. Deployment readiness under real constraints is not. Identify the missing representative checks and a decision-appropriate next test; do not fabricate a success rate.

## B. A small change does not need a new benchmark

**Evidence:** A local formatting correction changes only a documented error message, and the affected behavior is covered by a focused test.

**Proposal:** Run a full latency benchmark and generate a human review dashboard.

**Expected judgment:** Reject the unnecessary campaign. Check the targeted message contract; state any untested claim plainly.

**Try it:** Ask: "Use $engineering-evidence-review to separate the claims, observed evidence, and remaining uncertainty in both cases."
