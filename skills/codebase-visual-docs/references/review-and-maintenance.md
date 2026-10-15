# Review, validation, and maintenance

Use this reference after authoring or when deciding whether a revision is complete. Scale verification to the artifact and uncertainty; do not turn a small diagram into an audit program.

## 1. Check the original comprehension contract and factual correctness

Reuse the reader questions selected before drafting; the lists below are candidates for choosing them, not a new mandatory questionnaire at review time. Do not broaden a local revision into a whole-system review.

For each original question, locate the answer in the finished default view and state it using only that view. An absent answer, an answer hidden behind exploratory clicks, or one reconstructed from unrelated sections fails the comprehension contract. A nearby source link is supporting evidence, not a replacement for an explanation. Revise the information structure and recheck the same question; do not redefine it to excuse a missing answer. Keep this as a working check unless the user requests a review report.

Technical review separately asks whether each answer is supported by implementation and evidence. These are two review concerns, not two required agents or review rounds. A rendering check answers neither by itself.

For a substantial system document, an unfamiliar engineer should be able to answer from the main reading path:

1. What real input reaches the system, and how does it become executable data?
2. Why does validation not guarantee successful execution or an acceptable result?
3. Why are the important responsibility/representation boundaries separate?
4. What establishes that a displayed result satisfies its required conditions?
5. Which client, transport, hosting, or workflow can change without changing domain meaning?

Choose only questions relevant to the actual purpose. Only for an explicitly requested roadmap or capability-evolution task, consider:

1. What is useful today and within what scope?
2. Which owners or capabilities can evolve independently?
3. What is the next concrete change and why is it the current investment?
4. Which relationships are required, supportive, or conditional?
5. What evidence exists, and what evidence would justify proceeding?

A focused request may need only the relevant subset. Do not make readers answer unrelated architecture questions.

## 2. Ground the review in observable problems

Useful technical findings include:

- A client sends different data than the diagram claims.
- A source or cache contributes different facts than the narrative assigns to it.
- A library feature is described as supported end-to-end functionality.
- An optional preview is shown as a persistent execution prerequisite.
- A logical module is presented as a remote service.
- Completion, validity, verification, and UI projection are collapsed.
- Unit conversion or exact JSON fields are incorrect.
- A support/conditional edge is drawn as a hard prerequisite.
- A mock interaction or new prose is presented as new engineering evidence.

Useful comprehension findings include:

- Main questions require reading many source links or opening every stage.
- The graph is technically complete but offers no obvious entry point.
- Cards, table rows, and paragraphs tell the same full sequence repeatedly.
- The example hides the responsibility split it was meant to explain.
- The main view mixes current behavior and target direction without a clear label.

Reviewers should cite the problematic claim or visual and explain its consequence. Do not request broad restructuring because another layout is also reasonable.

## 3. Preserve independent review honesty

When an independent reviewer is available and authorized, provide the reader brief, finished sources/artifact, and permitted implementation access. Do not supply the intended answers or coach away a suspected confusion before the review.

A review can be performed with or without subagents. Label a self-check, independent agent review, and actual human reader study accurately. A model answering comprehension questions is useful feedback, not proof that real readers finish in a particular number of minutes.

If multiple workers are used, assign disjoint editing ownership. Keep shared narrative/model integration with one owner. Do not require a particular model, worker count, or human approval gate through this skill.

## 4. Validate what the artifact actually supports

| Check | When it is relevant |
| --- | --- |
| Referenced paths, symbols, versions | Code-grounded claims |
| Links, anchors, stable IDs | Navigable documents and compatibility |
| Narrative/model/diagram agreement | Structured or generated presentations |
| Regeneration matches checked-in output | Existing generated artifact chain |
| Default view contains primary reasoning | Progressive-disclosure documents |
| Desktop/narrow viewport, no page-wide overflow | HTML or web presentations |
| Keyboard/focus and disclosure behavior | Interactive controls |
| Shareable selection, reload, Back/Forward | URL-managed exploration |
| No-JavaScript and print behavior | Standalone artifacts with these requirements/support |
| Correct units, status predicates, joins | Domain results and evidence |
| Relevant existing tests or a bounded source experiment | A factual claim remains uncertain |

Use available tools and existing validation commands. If a check cannot be run, state the material limitation; do not claim success from inspection alone. Prefer an existing targeted check to a new test that merely mirrors the renderer's strings.

A static document can be technically reviewed without executing the whole product. Browser screenshots confirm presentation, not execution correctness. A source-reference hash confirms provenance, not a new runtime acceptance.

Do not create word/token/performance benchmarks, full acceptance campaigns, or new document frameworks unless requested or actually needed to resolve the task's uncertainty.

## 5. Use a bounded correction loop

Classify feedback before changing the artifact:

| Feedback class | Appropriate response |
| --- | --- |
| Factual contradiction | Fix the claim and every affected view |
| Missing reasoning or failure boundary | Add the smallest clear explanation |
| Misleading visual semantics | Correct arrows, grouping, labels, or status mapping |
| Repetition or information hierarchy | Consolidate presentations; preserve unique depth |
| Local style issue | Refine typography, spacing, wording, or control behavior |
| New requested scope | Incorporate it explicitly; keep unaffected structure stable |

Apply the targeted fix, inspect affected sources and generated output, and rerun only checks affected by it. Existing independent review remains useful for unchanged content; repeat review when new claims, substantive changes, or unresolved concerns justify it.

For an accepted baseline, treat reader feedback as a bounded revision unless it identifies a broken conceptual model. Do not restart architecture discovery or add speculative abstractions after every wording correction.

## 6. Completion criteria

Finish when:

- The original Reader Comprehension Contract passes against the default view, within the requested scope.
- Important claims are grounded; material unknowns have precise labels.
- Main visuals and text agree, including failure/status and dependency meanings.
- Readers can use the default path without assembling it from reference fragments.
- Exact APIs, code, exceptions, and evidence remain discoverable at the appropriate depth.
- Canonical sources and generated deliverables agree.
- Relevant checks pass, or unavailable checks and remaining limits are accurately reported.

Do not continue adding sections, renaming layers, inventing maturity metrics, or polishing the same accepted model without a demonstrated problem. A synthetic forward-test or successful static check does not prove improved first-pass readability or reduced revision burden in real tasks; report that limitation honestly. Maintenance resumes when implementation, agreed direction, evidence, or actual reader feedback changes.

## 7. Deliver and maintain one authority

Provide the requested artifact and concise notes about what changed, why, validation, and important limitations. Preserve exact contracts in their owning documents rather than duplicating them into a new architecture authority.

Keep generated evidence, screenshots, temporary investigations, and review receipts in the project's established output location. Commit or publish them only when requested or required by repository practice. Do not silently create issues, pull requests, deployments, or installed tools.

Keep implementation/source pins explicit when the project uses them. When behavior changes, reconcile the affected narrative, model, diagrams, and code references together. Keep historical records outside the primary as-built reading path.
