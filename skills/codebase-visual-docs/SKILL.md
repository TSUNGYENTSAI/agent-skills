---
name: codebase-visual-docs
description: Explain how an existing software system works through code-grounded technical documents, architecture diagrams, and focused flow visualizations. Use for as-built system explanations or bounded revisions that improve reader understanding. Capability-roadmap guidance is available only when explicitly requested; this skill does not implement product-runtime changes.
---

# Codebase Visual Docs

Explain the actual system so the intended reader can understand it. A code inventory, attractive graph, or exhaustive module list is not a substitute for that explanation.

Use the requested format, destination, language, and depth. Write reusable prompts in English; deliver documents in the user's requested or conversational language. No framework, section count, or diagram set is required.

## Match the scope before choosing the method

Default to **as-built system explanation**: responsibilities, transformations, execution, failure, and outcomes. For a focused diagram or local revision, inspect only the affected path and immediate context; do not expand into a whole-system trace, cross-repository investigation, or full review cycle without a concrete need.

Inspect applicable repository instructions and the artifact's maintained sources/build chain. Update generated outputs through that chain. Preserve an accepted conceptual model during a bounded revision unless evidence exposes a material contradiction.

Use capability-roadmap methods only for an explicit roadmap, capability-evolution, or investment request. A Current/Target architecture comparison alone is not such a request. In roadmap mode, read [capability-roadmaps.md](references/capability-roadmaps.md); do not load it for ordinary architecture work.

## Define the Reader Comprehension Contract

Before drafting, identify the primary reader and the questions they must be able to answer. Infer them from the request and existing context; ask only when missing information materially changes the task. For a substantial document, choose approximately 3–5 concrete questions; a focused request may need only one. Use them as acceptance criteria, not as a new report, user approval gate, or mandatory visible section.

After rendering or reading the finished artifact, check those **same questions** against the default reading path. Each answer should be identifiable in visible prose, a diagram, or a table without source-code inspection, exploratory clicks, or reconstruction across unrelated sections. References may substantiate an answer; they must not be the only explanation of it. If a question fails, reorganize the explanation instead of merely adding detail or changing the question to fit the output.

## Establish the behavior before drawing it

Trace enough of a representative entry-to-outcome path to support the requested explanation. Check owning code and relevant contracts/tests; inspect consumers when their input or result projection changes the story. Explain transformations and decision ownership, not just names.

Keep logical responsibility, process deployment, data conversion, user workflow, and planning order distinct. Label implemented behavior, target direction, and actual unknowns precisely. Do not change runtime behavior or invent integration steps to make a diagram true.

When source/representation joins, multiple repositories, exact fields/units, or result-state semantics matter, read only the relevant sections of [investigation-and-modeling.md](references/investigation-and-modeling.md). A narrow task does not require that entire investigation.

## Reorganize before shortening

When an explanation feels dense, diagnose the information structure first: remove duplicated concepts, separate mixed abstraction levels, reorder around reader questions, and replace repeated descriptions with one clear view. Shorter sentences, more bullets, or additional diagrams are not improvements by default.

Use one primary reading spine and give each fact one main presentation home. Keep the key flow and its important failure/feedback boundaries visible; place exact calls, types, payloads, exceptions, and code in references or disclosures. Use prose for design reasons, flows for handoffs, tables for comparisons, and compact points for responsibilities when they fit the content.

For substantial information design or an overloaded artifact, read the relevant sections of [information-design.md](references/information-design.md). Do not add phases, worked examples, interactivity, models, or generators solely to satisfy a template.

## Verify proportionately and stop

Apply the Reader Comprehension Contract, check factual grounding, and run the artifact's relevant link, generation, rendering, and interaction checks. Correct affected sources and views together. A small change needs focused verification, not two full review rounds or an automatic extra agent.

For a substantial artifact or unresolved technical/reader concern, use [review-and-maintenance.md](references/review-and-maintenance.md). Independent review is useful when justified and authorized; label self-checks and actual reader studies accurately. A documentation task does not require a new runtime acceptance campaign or a word/token benchmark.

Finish when the requested scope and original reader questions are covered, material contradictions are resolved or precisely recorded, and relevant checks pass or their limitations are reported. Do not keep redesigning an accepted baseline. Synthetic trials or static checks do not establish that the skill reduces real-world revision burden; use later real tasks to learn that.

Deliver the requested artifact, maintained source locations, important changes/limits, and concise validation evidence. Installation, publication, commits, and external actions follow existing user authorization and repository instructions; this skill grants none.
