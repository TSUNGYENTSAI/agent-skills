# Agent Skills

Personal agent skills by Tsung-Yen Tsai: reusable, judgment-oriented workflows for implementing, planning, reviewing, and explaining engineering work.

## Available skills

| Skill | Use it for |
| --- | --- |
| [Codebase Visual Docs](skills/codebase-visual-docs/SKILL.md) | Explain an existing system through technical documents, architecture diagrams, and focused flow visualizations. |
| [Readable Implementation](skills/readable-implementation/SKILL.md) | Implement complete features and refactors with direct flow, clear names, and justified complexity. |
| [Engineering Discipline](skills/engineering-discipline/SKILL.md) | Follow a cross-project development loop: sparse purposeful comments, executable verification, proof-oriented review, and preventing recurring architectural mistakes. |
| [Engineering Scope Review](skills/engineering-scope-review/SKILL.md) | Review proposed work for outcome fit, avoiding both overengineering and artificial under-scoping. |
| [Engineering Evidence Review](skills/engineering-evidence-review/SKILL.md) | Judge what tests, benchmarks, and demonstrations actually establish, and which evidence is needed next. |
| [Semantic Boundary Review](skills/semantic-boundary-review/SKILL.md) | Clarify facts, assumptions, decision authority, interfaces, and representation fidelity before abstracting. |
| [Decision-Driven PoC](skills/decision-driven-poc/SKILL.md) | Frame research spikes and feasibility experiments around a decision, uncertainty, and stop rules. |

## Install in Codex

Ask Codex to install the skill from this repository:

```text
$skill-installer Install codebase-visual-docs from https://github.com/TSUNGYENTSAI/agent-skills/tree/main/skills/codebase-visual-docs
```

For another skill, replace the name and repository path in that command with any skill from the table. Installation is a separate, explicit action; committing a skill here does not install or activate it. When a skill is updated, refresh or reinstall the existing local copy. All skills are self-contained. Each installs with its own optional `references/` materials, including decision cases and the codebase-visual-docs worked fixture.

This installs the selected skill for local use. If it does not appear, restart Codex. See the [official skills documentation](https://learn.chatgpt.com/docs/build-skills) for local discovery and installation details.

## Use Codebase Visual Docs

Open the repository you want to explain, then ask:

```text
Use $codebase-visual-docs to explain this system to an engineer unfamiliar
with the repository. Ground the explanation in the current implementation,
show the main input-to-outcome flow and important failure boundaries, and
check the finished document against the reader questions chosen at the start.
Write the result in docs/system-overview.md.
```

Focused requests also work:

```text
Use $codebase-visual-docs to draw a Mermaid diagram of the request validation
path. Inspect only that path and the immediate context needed to explain it.
```

```text
Use $codebase-visual-docs to revise docs/system-overview.md so the failure
path is easier to understand. Preserve the existing conceptual model unless
the current implementation contradicts it.
```

The skill starts from what the system actually does. It separates implemented behavior, intended changes, and unknowns; chooses visuals around reader questions; and keeps exact interfaces and code details discoverable. Capability-roadmap guidance applies only when explicitly requested. It does not implement product-runtime changes.

## Use Readable Implementation

```text
Use $readable-implementation to implement this feature. Keep the complete
requested behavior, make the main flow easy to follow, and introduce only
abstractions with a concrete responsibility or consumer.
```

It also applies to authorized cleanup of over-layered code. It optimizes the
reader's understanding rather than line counts or the shortest diff. It does
not require the review skills as prerequisites or authorize a wider refactor.

## Use Engineering Discipline

Use this for substantial agent-assisted implementation or repeated architecture/verification problems. It is a **working habit**, not another mandatory review gate:

```text
Use $engineering-discipline to extend the existing implementation, avoid
unnecessary wrappers and comments, verify the real behavior with reproducible
evidence, and improve the repo's development environment when a mistake repeats.
```

The skill keeps the project-specific architecture and verification contracts in the project. For a specialized question, invoke the relevant focused skill (for example, `readable-implementation` for code structure or `engineering-evidence-review` for auditing claims). Do not automatically chain all the skills. The [pilot protocol](skills/engineering-discipline/references/pilot-protocol.md) is an evaluation recipe, not evidence of proven benefit.

## Use the judgment skills

Invoke only the skill relevant to the current decision. They are **independent tools**, not a mandatory four-stage review pipeline.

```text
Use $engineering-scope-review to assess this work item before implementation.
Use $engineering-evidence-review to evaluate whether these results justify the claim.
Use $semantic-boundary-review to challenge this proposed domain/API boundary.
Use $decision-driven-poc to define what our next feasibility experiment must learn.
```

## Examples

The [self-contained example](skills/codebase-visual-docs/references/worked-example/request.md) includes a small Python fixture, an authoring request, and a worked explanation with a Mermaid flowchart. It demonstrates the intended output; it is not evidence of production use or measured skill effectiveness.

Each of the four judgment skills bundles **synthetic, contrasting decision cases** under its own `references/` directory. Standard skill installation therefore includes the cases without extra repository-wide downloads. They demonstrate intended judgments and exceptions, not independent agent evaluations:

- [Engineering Scope Review cases](skills/engineering-scope-review/references/decision-cases.md)
- [Engineering Evidence Review cases](skills/engineering-evidence-review/references/decision-cases.md)
- [Semantic Boundary Review cases](skills/semantic-boundary-review/references/decision-cases.md)
- [Decision-Driven PoC cases](skills/decision-driven-poc/references/decision-cases.md)

Readable Implementation includes [before/after implementation examples](skills/readable-implementation/references/implementation-examples.md), with exceptions that preserve necessary complexity. They illustrate intended behavior, not measured effectiveness.

## Repository layout

```text
skills/<skill-name>/
  SKILL.md             Instructions and trigger description
  agents/openai.yaml   Codex display metadata
  references/          Optional cases, guidance, and worked fixtures; bundled with the installed skill
```

Maintain skills here, then refresh local installations deliberately. Keep each skill focused; add scripts or references when a real workflow needs them. Before publishing changes, validate the skill structure, resolve relative links, and run any affected examples. Structural checks do not establish whether a skill makes good decisions; use real tasks to improve it.

## 中文說明

這個 repository 收錄可持續修正的個人工程判斷 Skills。新增的 `engineering-discipline` 是跨專案的日常開發習慣，強調沿用正式架構、少寫無意義註解、實際執行驗證，以及用可重現證據 Review；它不取代其他專項 Skills，也不是必經審核流程。除 `codebase-visual-docs` 用於建立 code-grounded 的架構解釋外，另有四項工程判斷 skills：`engineering-scope-review`（工程範圍）、`engineering-evidence-review`（證據與宣稱）、`semantic-boundary-review`（語意與權責）、`decision-driven-poc`（探索性 PoC）。它們各有明確使用情境，不需同時啟動；使用後可依實際回饋調整、合併或刪除。`readable-implementation` 用於日常實作與重構：保留完整功能，以清楚名稱、直接流程及有理由的抽象降低理解負擔，不以最少行數或縮減功能為目標。Skill 指令與可重用 prompt 維持英文，交付內容可使用中文。

## License

[MIT](LICENSE).
