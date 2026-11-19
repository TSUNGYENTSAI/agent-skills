# Sources and adaptation boundaries

## Primary sources reviewed (2026-11-19)

1. Lauren Tan, "All Code Is Slop (Except Mine)," AI Engineer CODE 2026, original event page and video transcript: https://ai.engineer/code/2026/talks/lauren-tan
2. Public pstack source: https://github.com/cursor/plugins/tree/main/pstack
3. Official pstack skills: `correct`, `no-comments`, `create-verification-skill`, `maintain-verification-skill`, `statechart`, `reflect`, `principle-prove-it-works` under `pstack/skills/`.
4. Official pstack README and guide, including workflow routing and references to `cursor-team-kit` for some UI/CLI control and deslop functionality.

## Directly supported by sources

- The agent's environment and codebase patterns strongly affect output quality.
- Prefer architectural constraints, lint/type/verification over prose as enforceable controls.
- Correct recurrent mistakes by modifying the environment, not merely adding comments/instructions.
- In the reported team context most comments were banned; some methods (like `statechart`) are problem-specific.
- Runtime verification and user-facing feature maps/scripts make evidence easy to generate; review can rely increasingly on videos/screenshots/diagrams/formal proof where meaningful.
- Formal verification is an additional, experimental tool, not a silver bullet.
- One cited practitioner used 70% of tokens for verification; this is not a prescribed universal quota.

## Deliberate personal adaptations — not direct quotations or mandates from Lauren

- Sparse comments with documented exceptions rather than universally banning 99% of comments.
- Risk-weighted verification effort, rather than mandatory budget ratios.
- An evidence ladder across UIs, APIs, simulation, algorithms, concurrency and performance.
- PR architecture delta and cumulative drift checks where the repo has real evolution risks.
- Explicit distinction between behavior verified and architectural decision approved.
- Default to a single personal discipline skill and repo-owned contracts; adapt individual official pstack skills selectively rather than installing an entire opinionated stack by default.

## Implementation and attribution limits

Do not present this adaptation as pstack itself or as endorsed by its author. Do not lift third-party skill source verbatim. If installing pstack code, obey the upstream license and its tool-specific requirements. Official pstack is Cursor-oriented; a Markdown excerpt alone does not provide its agents, run tools, scripts, or formal verification dependencies. Avoid claiming that a self-written skill can enforce CI or prove correctness without runnable checks.
