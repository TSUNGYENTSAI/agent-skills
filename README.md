# Agent Skills

Personal agent skills by Tsung-Yen Tsai: reusable workflows for understanding systems and producing code-grounded technical explanations.

## Available skills

| Skill | Use it for |
| --- | --- |
| [Codebase Visual Docs](skills/codebase-visual-docs/SKILL.md) | Explain an existing system through technical documents, architecture diagrams, and focused flow visualizations. |

## Install in Codex

Ask Codex to install the skill from this repository:

```text
$skill-installer Install codebase-visual-docs from https://github.com/TSUNGYENTSAI/agent-skills/tree/main/skills/codebase-visual-docs
```

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

## Example

The [self-contained example](examples/codebase-visual-docs/request.md) includes a small Python fixture, an authoring request, and a worked explanation with a Mermaid flowchart. It demonstrates the intended output; it is not evidence of production use or measured skill effectiveness.

## Repository layout

```text
skills/<skill-name>/
  SKILL.md             Instructions and trigger description
  agents/openai.yaml   Codex display metadata
  references/          Guidance loaded only when relevant
examples/<skill-name>/ Demonstrations outside the installed skill
```

Maintain skills here, then refresh local installations deliberately. Keep each skill focused; add scripts or references when a real workflow needs them. Before publishing changes, validate the skill structure, resolve relative links, and run any affected examples. Structural checks do not establish whether a skill makes good decisions; use real tasks to improve it.

## 中文說明

這個 repository 收錄我持續使用與調整的 agent skills。第一個 skill 是 `codebase-visual-docs`：從實際程式碼出發，整理系統說明、架構圖與流程圖，並檢查文件是否回答了讀者需要理解的問題。可請 agent 用中文產出文件；skill 指令與可重用 prompt 維持英文。

## License

[MIT](LICENSE).
