# Information design and visual explanation

Use this reference when choosing a reading structure or revising an overloaded artifact. The goal is lower reconstruction effort, not fewer paragraphs at any cost.

## 1. Design a reading contract

Use the Reader Comprehension Contract from SKILL.md: choose the questions before drafting and test those same questions against the finished default view. Keep the questions as a working acceptance checklist unless the user requests a separate brief. For a substantial system explanation, useful candidates are:

- What problem does this system solve, and what is outside its responsibility?
- Who owns the major decisions?
- How does input become something executable?
- What makes a result acceptable, and what happens when work fails?
- What exists now, what is intended, and what is still an open contract?

A focused request may need only one or two questions. Only an explicit capability/roadmap request calls for questions about investment or capability evolution. Do not add all questions or all reading layers to every deliverable.

Design three reading depths where the scope supports them:

1. **Orientation:** purpose, scope, major owners, one primary view.
2. **Understanding:** transformations, feedback, a representative example, key design reasons.
3. **Investigation:** exact requests, types, interfaces, code, provenance, exceptions.

These are information layers, not mandatory tabs or timed acceptance promises. The reader should be able to stop at the relevant depth.

## 2. Choose one primary spine

For system architecture, an outcome-oriented path is often more useful than module order: input → interpretation/normalization → execution → acceptance/reporting. Source preparation can be a supporting branch. Optional preview should be shown as optional.

For a specific bug or algorithm, the primary spine may be a state transition, sequence, iteration, or decision tree. For a roadmap, use capability evolution rather than forcing a universal execution flow.

Group detailed operations into meaningful work phases. Two operations belong together when they serve the same reader-level purpose and the internal distinction can be deferred without hiding a correctness boundary. Do not make every function look like a peer architectural module. Equally, do not compress genuinely independent decision owners into an unexplained box.

## 3. Diagnose density, then choose a presentation home

Before editing individual sentences, determine why the explanation feels dense:

| Structural problem | First correction |
| --- | --- |
| The same concept appears in cards, a table, and prose | Keep one complete account; retain only distinct reasoning elsewhere |
| Responsibility, deployment, data, or planning are mixed | Separate the lenses and state how they connect |
| Readers encounter internal terminology before its purpose | Reorder around their questions and explain the concept before naming the type |
| The answer is scattered across unrelated sections | Consolidate it into one clear main-path view |

Only then shorten wording or change format. More bullets, extra diagrams, and shorter sentences can leave the original structural problem intact.

| Information | Main home | Useful supplementary detail |
| --- | --- | --- |
| What the system does | Short opening prose | Scope exceptions |
| Who owns a decision | Boundary diagram / labeled points | Owning interfaces |
| What happens next | Flowchart / swimlane | Exact sequence |
| What changes in the data | Transformation table | Actual DTO or compiler input |
| How choices differ | Comparison table | Evidence and constraints |
| Why a split exists | Short causal paragraph | Tradeoff and extension seam |
| Why work stops | Failure/feedback view | Error payload and recovery details |
| Where to inspect code | References / disclosure | Pinned lines or definitions |

Do not repeat the complete input/owner/output story in a diagram, a table, and matching paragraphs. Retain a repeated term only when it helps connect different questions. Remove historical delivery notes from the main as-built narrative; retain them as provenance when useful.

Replacing all prose with bullets does not repair the model. Use bullets for parallel responsibilities or conditions; prose for causality; tables for comparisons; arrows for actual relationships.

## 4. Make visual semantics explicit

Choose the smallest visual that fits the relationship:

- Flowchart for ordering, branches, optional operations, and return paths.
- Swimlane for cross-owner interaction.
- State machine for transitions and their conditions.
- Boundary diagram for responsibilities and representation changes.
- Sequence view for exact calls, responses, and callbacks.
- Comparison table for orthogonal differences.
- Focused dependency graph for selected relationships and impact.

Define arrow direction and type. Avoid displaying imports, calls, support relationships, derivation, and prerequisites as equivalent lines. Use grouping and labels alongside color. A cross-cutting assistant, observability function, or security concern may be an overlay rather than a peer service; choose its form from actual ownership.

Do not use a dense full graph as the only entry point. Keep the useful overview focused and retain the complete graph for exploration or lookup.

## 5. Show failure as part of the architecture

Place important unsuccessful boundaries near the main flow. A compact table can show:

| Boundary | Owner | Feedback / return point | Result retained |
| --- | --- | --- | --- |
| Cannot identify the requested object | Interpreter and query layer | Clarify; resolve again | No executable candidate |
| Structured candidate fails formal checks | Validation owner | Diagnostics; repair and revalidate | No submitted job, if rejection is pre-submission |
| Execution or acceptance fails | Executor and verifier | Truthful outcome; user/policy decides next action | Failed or partial result according to the implementation |

This is an illustrative pattern. Replace it with the system's actual boundaries; do not invent agents, jobs, retries, or human approvals. Show existing automatic retries separately from user-driven modifications. A candidate that was rejected must not appear as an accepted result in a green path.

## 6. Use one compact worked example

Choose an example that exposes a real boundary, not just a successful API call. Trace a concrete value or identity across stages:

| Stage | Input | Transformation / output |
| --- | --- | --- |
| Request/interpretation | Concrete intent and known context | Structured candidate |
| Validation | Candidate, references, version | Supported policy or diagnostics |
| Semantic conversion | Policy and applicability | Per-operation intent |
| Backend conversion | Intent and runtime representation | Executable primitives |
| Computation | Primitives | Candidate or failure |
| Acceptance/reporting | Complete candidate and original identity | Checks, outcome, associated evidence |

Adapt or merge rows. Below the table, explain only the essential reasons, limits, formulas, or geometry. Keep exact JSON, detailed exception rules, and class inventories in references. Do not add a full set of step cards and matching numbered paragraphs as a second telling of the same example.

When appropriate, contrast one other supported family in a small table. For example, a hard exclusion changes eligibility and needs acceptance proof; a preference changes comparison cost and records application/effect. This avoids implying that every policy creates the same backend primitive.

## 7. Preserve one maintained explanation

Keep the repository's existing source chain. If narrative, structured model, and renderer are separate, assign each a purpose:

- Narrative owns causal explanations and human-readable context.
- Model owns reusable facts, typed relationships, identities, and view data.
- Renderer/template owns presentation and interactions.
- Generated artifact presents the maintained sources.

Multiple views may project the same model without changing ownership or evidence meaning. Avoid creating a separately maintained report with competing facts.

Do not add a generator merely for a short Markdown document. If a directly readable Markdown source uses generated visual widgets, retain enough prose, tables, or appropriate links to answer the important questions outside HTML. Renderer tokens must not be the only place where the meaning exists.

## 8. Add interactivity only for a reader decision

Useful interactions include Current/Target comparison, a selected dependency neighborhood, a bounded scenario showing a changed assumption, search, and deep-linked details. Static flowcharts and tables are often sufficient.

The default main path must remain visible. Exact types and exception paths can be disclosed on demand. Do not hide the whole workflow behind a set of stage buttons or give every small detail its own widget.

For HTML, preserve semantic headings, readable typography, keyboard/focus behavior, and narrow layouts. Let a wide table or complex diagram scroll locally rather than overflowing the document. Use no-JavaScript fallback and print support when the artifact is intended for standalone reading or sharing; preserve existing support during revisions. Check deployed base paths, shareable selection URLs, and Back/Forward when the artifact actually uses them.

Interactive demonstrations must say whether they run real operations or illustrate a concept. A changed mock revision, colored result, or animated sequence does not establish new engineering evidence.

## 9. A reusable authoring request

Use or adapt this English prompt; it is a request template, not a mandatory deliverable structure:

> Create a code-grounded explanation of this system for an engineer unfamiliar with the repository. First choose a few concrete reader questions as acceptance criteria. Inspect only the paths needed to support the requested scope. Use one primary reading spine, distinguish current implementation from target direction, and make the key flow visible by default. Preserve the existing source/generation chain. Keep exact APIs, types, code references, and exceptions discoverable without retelling the main flow. Check the finished default view against the original reader questions, then verify the relevant factual and rendering behavior. Reorganize failed explanations before adding more detail; report actual checks and remaining limits.
