# Explain a small summarizer

This is a synthetic, self-contained teaching fixture. The worked output is an illustrative explanation checked against the fixture; it is not a recorded independent agent evaluation or a real-world performance claim.

From the repository root, give an agent this request:

```text
Use $codebase-visual-docs to explain examples/codebase-visual-docs/input/summarize.py
to an engineer unfamiliar with the code. Write a short Markdown document with
one Mermaid flowchart. Explain accepted inputs, how a summary is produced,
and what a caller sees on failure. Ground every behavior claim in the fixture.
```

Read the [worked output](output.md), then try the fixture with Python 3:

```sh
printf '%s\n' '[12, 8, 0]' | python3 examples/codebase-visual-docs/input/summarize.py
printf '%s\n' '[12, -1]' | python3 examples/codebase-visual-docs/input/summarize.py
```

The first command writes `{"count": 3, "total": 20}` to stdout and exits successfully. The second writes an error to stderr and exits with status 1.

For a focused revision, ask the agent to improve only the failure explanation. Check whether it preserves the correct existing model and stays within that scope.
