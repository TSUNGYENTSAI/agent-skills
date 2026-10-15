# Agent Skills

Personal agent skills by Tsung-Yen Tsai: reusable, judgment-oriented workflows for planning, reviewing, and explaining engineering work.

## Available skills

| Skill | Use it for |
| --- | --- |
| [Codebase Visual Docs](skills/codebase-visual-docs/SKILL.md) | Explain an existing system through technical documents, architecture diagrams, and focused flow visualizations. |
| [Engineering Scope Review](skills/engineering-scope-review/SKILL.md) | Review proposed work for outcome fit, avoiding both overengineering and artificial under-scoping. |
| [Engineering Evidence Review](skills/engineering-evidence-review/SKILL.md) | Judge what tests, benchmarks, and demonstrations actually establish, and which evidence is needed next. |
| [Semantic Boundary Review](skills/semantic-boundary-review/SKILL.md) | Clarify facts, assumptions, decision authority, interfaces, and representation fidelity before abstracting. |
| [Decision-Driven PoC](skills/decision-driven-poc/SKILL.md) | Frame research spikes and feasibility experiments around a decision, uncertainty, and stop rules. |

## Install in Codex

Ask Codex to install the skill from this repository:

```text
$skill-installer Install codebase-visual-docs from https://github.com/TSUNGYENTSAI/agent-skills/tree/main/skills/codebase-visual-docs
```

For another skill, replace the name and repository path in that command with any skill from the table. Installation is a separate, explicit action; committing a skill here does not install or activate it.

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

## Use the judgment skills

Invoke only the skill relevant to the current decision. They are **independent tools**, not a mandatory four-stage review pipeline.

```text
Use $engineering-scope-review to assess this work item before implementation.
Use $engineering-evidence-review to evaluate whether these results justify the claim.
Use $semantic-boundary-review to challenge this proposed domain/API boundary.
Use $decision-driven-poc to define what our next feasibility experiment must learn.
```

## Examples

The [self-contained example](examples/codebase-visual-docs/request.md) includes a small Python fixture, an authoring request, and a worked explanation with a Mermaid flowchart. It demonstrates the intended output; it is not evidence of production use or measured skill effectiveness.

Each new skill has a small pair of **synthetic, contrasting decision cases**. They demonstrate the intended judgment and exceptions; they are not independent agent evaluations:

- [Engineering Scope Review cases](examples/engineering-scope-review/decision-cases.md)
- [Engineering Evidence Review cases](examples/engineering-evidence-review/decision-cases.md)
- [Semantic Boundary Review cases](examples/semantic-boundary-review/decision-cases.md)
- [Decision-Driven PoC cases](examples/decision-driven-poc/decision-cases.md)

## Repository layout

```text
skills/<skill-name>/
  SKILL.md             Instructions and trigger description
  agents/openai.yaml   Codex display metadata
  references/          Optional guidance loaded only when relevant
examples/<skill-name>/ Demonstrations outside the installed skill
```

Maintain skills here, then refresh local installations deliberately. Keep each skill focused; add scripts or references when a real workflow needs them. Before publishing changes, validate the skill structure, resolve relative links, and run any affected examples. Structural checks do not establish whether a skill makes good decisions; use real tasks to improve it.

## 中文說明

這個 repository 收錄可持續修正的個人工程判斷 Skills。除 `codebase-visual-docs` 用於建立 code-grounded 的架構解釋外，新增四項輕量 v0：`engineering-scope-review`（工程範圍）、`engineering-evidence-review`（證據與宣稱）、`semantic-boundary-review`（語意與權責）、`decision-driven-poc`（探索性 PoC）。它們各有明確使用情境，不需同時啟動；使用後可依實際回饋調整、合併或刪除。Skill 指令與可重用 prompt 維持英文，交付內容可使用中文。

## License

[MIT](LICENSE).
