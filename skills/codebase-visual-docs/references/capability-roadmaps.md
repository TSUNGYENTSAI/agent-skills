# Capability and roadmap views

Read this reference only when the user explicitly requests a capability roadmap, capability evolution, or investment explanation. As-built architecture is the primary skill use; a Current/Target comparison, a planned integration contract, or a local diagram revision does not by itself request this mode. Do not expand those tasks into investment analysis.

## 1. Keep the questions separate

| View | Main question | Appropriate content |
| --- | --- | --- |
| System architecture | How are responsibilities and representations connected? | Ownership, interfaces, data, process boundaries |
| User workflow | How does a person accomplish a task? | Actors, actions, confirmation, feedback |
| Capability roadmap | What becomes useful next, and why? | Current coverage, intended change, investment rationale, success signal |
| Evidence | What has actually been established, within what scope? | Source, revision/date when relevant, method, result, limitation |
| Dependency | What must exist before something else can operate? | Explicit prerequisites and bounded enabling conditions |

A reader should not need one giant diagram to answer all five. Multiple views can use a shared canonical content model, with a distinct reader question in each.

## 2. Model independently evolving capabilities

Identify the actual capability owners before drawing a timeline. Separate independently useful product or subsystem tracks from shared contracts, cross-cutting assistance, and optional composition.

A useful generic arrangement is:

- Shared contracts/reference primitives that multiple consumers can use.
- Independently useful application or domain capabilities.
- Optional compositions that join them for a particular problem.
- Cross-cutting assistance, diagnostics, or operational concerns.

This arrangement is an example, not a required architecture. Do not invent a shared platform, assistant, or domain hierarchy if the sources do not support one.

A shared identity or data contract does not imply a universal execution representation or one central owner for every task context. Method-specific models can differ while preserving common references. A capability used in one reading profile does not acquire a different owner just because that profile displays it.

## 3. Do not manufacture a universal stage sequence

A page's reading order is not an execution DAG, dependency order, or synchronized release plan. Preserve parallel work and independently evolving maturity where supported.

Examples of distinctions worth showing:

- A minimum shared interface can be a prerequisite for a new integration while existing engine work continues independently.
- A representative use case can test a capability without becoming a mandatory product stage.
- Cross-system feedback may be conditional on demonstrated need, not necessary for each system's standalone value.
- Research can proceed in parallel while production orchestration depends on reliable actions and evidence.

Represent a real dependency as such. Represent a useful contribution as support. If ordering is investment rationale rather than a hard technical prerequisite, say so.

## 4. Give relationships a stable meaning

Use the source's actual relationship semantics and an explicit legend. A compact model may distinguish:

| Relationship | Meaning |
| --- | --- |
| depends_on | Necessary prerequisite within the stated scope |
| derived_from | Data/result lineage |
| supports/enables | Useful contribution; may be conditional or nonessential |
| consumes | Uses an existing contract or capability |
| validates/tests | Produces evidence about a bounded claim |
| applies_to | Cross-cutting role or assistance relevance |

Do not automatically treat every enabling/support edge as required. Do not infer a dependency from proximity, color, or narrative order. Qualify edges when the requirement applies only to one source, deployment, or use case.

When a graph is large, show the main product boundaries and meaningful loops first. Keep the full relation graph in a focus/exploration view; preserve canonical IDs and search/deep-link compatibility when restructuring an existing artifact.

## 5. Separate investment status from evidence status

Investment labels such as current focus, next, deferred, or conditional describe choices. Evidence labels such as tested in a bounded scenario, partial coverage, or unvalidated describe what is known. Neither should silently update the other.

For each material capability, distinguish:

- What exists today, and the exact coverage/limit.
- What changes if the proposed work succeeds.
- Why that change matters to the intended user or system.
- The observable success signal or evidence still needed.
- The actual prerequisite or condition for proceeding.

Use source-grounded dates and promises only. A capability progression does not need invented months, maturity scores, numeric gates, or delivery commitments. Proposed acceptance criteria may be useful when requested; label them as proposed rather than observed.

Do not promote evidence because the wording becomes clearer, the UI is complete, a prototype runs, or a shared concept is renamed. Documentation verification, mock demos, engineering evidence, and real user validation are different receipts.

## 6. Place assistance according to responsibility

An assistant may help interpret input, suggest a mapping, diagnose a failure, or propose an action. It may belong across existing capabilities rather than form a new peer product track.

Show the responsible authority or existing policy gate where a candidate becomes executable or accepted. Do not let a suggestion imply correctness, permission, or automatic execution. Also do not add a mandatory human gate where the implemented workflow does not have one.

If the system supports a concept demonstration, label it as illustrative. A simulated change of input revision can explain staleness; it does not perform real invalidation or improve the evidence level.

## 7. Keep variation and extension boundaries concrete

When the request covers reuse or adaptation, distinguish source mapping, configuration, and existing rule/policy changes from missing semantics, new algorithms, or unsupported actions. This explains what can vary without engineering extension.

Use one representative variation to expose the boundary. Avoid promising universal adaptability from one successful case, or declaring a shared capability complete because a small number of consumer examples passed.

## 8. Refine an accepted model without restarting it

When ownership and conceptual topology are accepted, preserve them unless new evidence or explicit direction changes them. Local improvements can clarify scope, move details, explain a relation, or remove duplication. A new layout does not require a new capability model.

Preserve the distinctions between historical presentations and the current source model. Keep old URLs/aliases when users rely on them; route them to meaningful current content instead of restoring obsolete concepts.
