# Investigation and modeling

Read this reference when an explanation crosses modules, repositories, sources, representations, or status boundaries. For a focused diagram, use only the portions that resolve the actual uncertainty.

## 1. Investigate by question, not by file count

Start from the entry point relevant to the reader: a UI action, API handler, CLI command, event consumer, batch job, or library call. Trace one representative scenario deeply enough to establish the important boundaries. Then inspect a contrasting path only where it changes the explanation.

Select authoritative contracts for the affected area rather than loading every historical document. Use current owning code/tests for as-built claims. Historical records can explain a past decision, but cannot be combined with newer files to invent a current implementation.

Maintain a small claim inventory in working notes if the task is substantial:

| Claim | Supporting implementation | Verification or evidence | Classification / limit |
| --- | --- | --- | --- |
| Request is normalized before dispatch | Handler and normalizer | Owning test or observed trace | Current |
| Preview is optional | Submit path does not consume preview state | Submission contract | Current |
| Future identity propagation | Approved integration direction | No implemented service contract | Target; contract open |

This is an investigation aid, not a required report, new repository authority, or reason to make the user read all the source material.

## 2. Follow the actual input, including omissions

A visual user selection does not prove that the selected identity is sent to the backend. An SDK type does not prove that a field survives serialization. A response label does not prove the UI uses the corresponding domain result.

Check the boundaries that carry the scenario:

- Client request construction, selection/context packaging, and persistence.
- Public transport mapping, request shape, and error behavior.
- Normalization, reference resolution, policy/rule validation, and composition.
- Execution intent and backend-specific representation.
- Algorithm execution, result acceptance, publication, and status projection.

Document missing integration precisely. For example, a valid suggestion might be displayed but require an explicit user action and full-set validation before it becomes saved executable input. Do not silently connect those steps in a happy-path diagram.

## 3. Build a transformation inventory

Use the following row shape internally, adapting names to the actual code:

| Owner | Input | Decision / transformation | Output | Failure / feedback |
| --- | --- | --- | --- | --- |
| Consumer | User action and available context | Construct a request | Actual serialized payload | Missing context or client error |
| Semantic layer | Structured candidate and known references | Resolve meaning, applicability, precedence | Validated policy / intent | Diagnostics or clarification |
| Backend bridge | Intent and runtime facts | Bind representation and executable primitives | Backend request | Binding or preparation error |
| Algorithm | Executable primitives | Search / compute / evaluate | Candidate / status | Infeasibility or exhausted budget |
| Acceptance / reporting | Candidate and required checks | Verify, accept, associate evidence | Domain result / report | Rejection or partial result |

These are illustrative roles, not mandatory layers. Omit roles that do not exist; represent callbacks, shared types, and cyclic composition when the code uses them. A preflight or preview operation may be a side branch rather than a prerequisite.

Use important intermediate types only after explaining what they carry and why the next stage needs them. Distinguish similarly named public responses from internal execution objects. Avoid presenting a vocabulary list as the explanation.

## 4. Keep identities and representations distinct

A semantic model answers what an object means, how it is referenced, and which relationships apply. A computational representation answers how a method operates on it. They may be related without being the same object or forming a simple serial pipeline.

Possible pairs include:

- Logical resource ID and physical storage location.
- Business entity and search index document.
- Source data and normalized query model.
- Semantic entity and collision mesh or discrete grid.
- Domain policy and backend-specific guard, cost, query, or bytecode.

Explain the join: canonical IDs, source/version identity, conversion ownership, cache provenance, or a callback that checks eligibility. An object can be queryable while lacking the representation required for a particular operation. A display representation need not be acceptable for computation.

When sources contribute different facts, draw a branch or join. Label which source supplies identity, relationships, parameters, or geometry. Do not imply that one input supplies all facts, that every source has equal capabilities, or that a query projection produces the physical representation it actually reads.

## 5. Separate the architectural lenses

| Lens | It should explain | It should not imply |
| --- | --- | --- |
| Logical responsibility | Who owns a decision and data meaning | Every box is a deployed service |
| Process/deployment | Processes, workers, libraries, transport | Deployment topology owns domain semantics |
| Execution | Actual data handoffs and side effects | Page order is mandatory execution order |
| User workflow | Actions, confirmation, feedback | Every interaction is an API restriction |
| Capability/investment | Current coverage and intended evolution | A future activity is an implemented feature |

One view may reference another, but arrows need a stated meaning. An import edge, injected callback, network call, data derivation, and hard prerequisite are different relationships.

Ownership can be established while proxy strategy, hosting, authentication, or scheduling contracts remain open. Limit the unknown label to the actual unresolved decision.

## 6. Preserve distinct outcome claims

Where these distinctions exist, trace them separately:

| Claim | Evidence required |
| --- | --- |
| Candidate is well formed | Shape/type checks |
| Candidate is meaningful and applicable | Resolved references, supported semantics, scope/version checks |
| Execution found a candidate | Algorithm result and termination reason |
| Candidate is accepted | Required complete-result checks |
| Execution has terminated | Worker/job lifecycle outcome |
| UI has a displayable result | Consumer projection logic |
| A preference improved quality | Observed comparable effect or metrics |

A terminal display label can represent a readable partial result rather than achievement of every goal. Explain the exact predicate when it matters, then identify the per-item state, failure detail, or matching evidence the consumer must inspect.

A schema-valid candidate can misunderstand user intent. A supported primitive can lack end-to-end product support. An algorithm result can fail downstream verification. A soft policy can be applied without measurable improvement. Keep the appropriate limitation attached to the claim.

## 7. Check units and revisions at handoffs

When relevant, check field names and unit conversion in the producer and consumer. Distinguish requested thresholds from centerline/radius-adjusted thresholds, input units from display units, and algorithm objectives from full-result metrics.

Separate source revision, repository revision, cache identity, request fingerprint, and result identity. Use the repository's traceability method when present; do not invent a hashing system for a simple document.

Examples with exact JSON must use real supported shapes. Mark fictional values as illustrative and identify where real IDs or versions come from. No fixture value, synthetic screenshot, or document build is evidence of production correctness.
