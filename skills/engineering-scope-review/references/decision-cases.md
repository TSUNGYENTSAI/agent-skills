# Engineering Scope Review — contrasting cases

Synthetic, non-proprietary examples illustrating the judgment. They are not recorded agent trials.

## A. Too much work

**Request:** Add a CSV importer used by one internal script, with schema validation and clear errors.

**Agent proposal:** Introduce an asynchronous job manager, extensible import plugin registry, distributed retries, an observability service, and a large performance benchmark before delivery.

**Expected judgment:** Revise. Deliver the importer and validation path with focused tests. Require evidence of scale, concurrency, or reliability needs before adding infrastructure.

## B. Too little work

**Request:** Migrate all maintained callers to one supported API and remove the retired route.

**Agent proposal:** Migrate one caller as a pilot and call the task complete.

**Expected judgment:** Revise. A pilot can reduce uncertainty, but cannot satisfy the stated outcome. Include the active consumers and contract checks, or name the precise blocker and an explicit follow-through plan.

**Try it:** Ask: "Use $engineering-scope-review on each proposal. Explain the smallest *sufficient* scope and when the opposite scope choice would be justified."
