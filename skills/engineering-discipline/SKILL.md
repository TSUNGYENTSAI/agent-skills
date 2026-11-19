---
name: engineering-discipline
description: Apply cross-project engineering discipline to substantial agent-assisted implementation and iterative development. Use when starting or changing a codebase, preparing verifiable implementation evidence, or converting recurring agent mistakes into better architecture and tooling. Focus on a repeatable inner loop, sparse purposeful comments, proof-oriented review, and preventing accumulated complexity without adding ceremony.
---

# Engineering Discipline

## Purpose

Produce the **smallest maintainable, demonstrably correct change**. Improve the repository so the next agent can repeat the good behavior without having read this conversation. Prioritize **working evidence over claims**, **architecture and interfaces over prose**, and **subtraction over accumulation**.

This skill describes **personal engineering habits** and how to apply them. It does **not** set universal module boundaries, ban all comments, mandate TLA+, or replace the architecture/verification contract of the current repository.

## Five durable habits

1. **Design from the domain and data.** Establish the intended behavior, inputs, invariants, owners and canonical extension point before inventing code. Challenge the premise and read the closest real implementation.
2. **Write less, clearer code.** Reuse and consolidate first; prefer simple direct control flow over one-caller wrappers, parallel pipelines, compatibility shims and speculative generality. Name the data shape and ownership. Make illegal states difficult to represent.
3. **Comments are an exception, not a solution.** Favor readable code, types, tests and executable checks over comments defending a workaround. Review existing/new comments for stale claims or encoded rules. Retain a concise comment when it carries information not recoverable from code (external specification, subtle mathematical or concurrency invariant, necessary safety constraint, intentional non-obvious trade-off, legal/license notice). Do not delete necessary API docstrings or project-mandated documentation. Never treat “few comments” as a numeric quality metric. See `references/comment-policy.md`.
4. **Spend serious effort proving behavior.** Do not declare success because code compiles, unit tests are green, or an agent says “done.” Use the narrowest **real execution surface** that can prove the claimed behavior, then increase coverage with risk. Verification often deserves the largest share of a nontrivial task's effort, but do not enforce an arbitrary 70% time/token quota. See `references/verification-evidence.md`.
5. **Review proof and prevent recurrence.** Inspect executable results, screenshots/video, traces, replay, contract/property checks or formal models when relevant; always retain enough code/architecture review to assess responsibility and long-term maintenance. For each repeated mistake, improve API/design first, then type/lint/test/CI, with prose last. A Skill can guide this; only tools and code enforce it.

## Relationship to focused skills

This is the cross-cutting **working habit**, not a mandatory pipeline of reviews. Use the repository's own contract as authority, and invoke focused skills only when their distinct question is consequential:

- `readable-implementation` for a concrete code-structure or readability decision.
- `engineering-evidence-review` for auditing whether a stated claim is supported by supplied tests, metrics, or demonstrations.
- `engineering-scope-review` when deciding whether a proposed delivery scope is sufficient.
- `semantic-boundary-review` for ambiguous data meaning or decision ownership.
- `decision-driven-poc` for a bounded experiment before committing to a capability.
- `codebase-visual-docs` when producing a reader-oriented system explanation.

Do not automatically chain these skills or require another document for ordinary changes. The goal is one engineering loop, not six reports.

## Choose the lightest workflow

- **Small, local edit:** inspect affected code, make focused change, run relevant fast check; no report template.
- **Feature / refactor:** follow the full inner loop below.
- **Bug:** reproduce first; prove root cause; fix at the owning boundary; rerun the failing case and a nearby valid case.
- **PR/MR review:** review behavior evidence, then architecture delta and meaningful code risks; reject unsupported claims.
- **Repo bootstrap / major refactor:** establish project-specific architecture contract, executable verification entrypoint, and a small number of fitness functions. Reuse tooling already there.
- **Repeated issue / architectural drift:** perform the correction loop and examine several related changes, not just the latest diff.

## Inner loop for a nontrivial change

### 1. Understand

- Read repo instructions, canonical entrypoints, interfaces/schemas, consumers, and current verification tooling. Trace only the needed user-facing or domain path.
- State the behavior to preserve or add, what evidence would convince a skeptical reviewer, and what remains unknown.
- Identify the authoritative decision owner. Distinguish genuinely independent validation from duplicate implementation of one domain decision.

### 2. Shape the implementation

- Prefer **reuse → extend → consolidate**, not new runner/registry/adapter by default.
- Before a new abstraction, ask what exact responsibility cannot live at the existing owner, who calls it, and what previous path can be removed.
- Use direct names, explicit data models, bounded side effects and simple interfaces. Don't patch an architectural conflict with timers, global mutable state or workarounds merely because they make a test pass.
- Choose verification *before* coding: a runnable user path, a behavior test, a persisted result, or a targeted proof obligation.

### 3. Implement a verifiable slice

- Make the smallest coherent change and clean up superseded code where consumer migration is safe.
- Keep exploratory scripts and raw artifacts out of product source unless they have a demonstrated durable user, reproducible input contract and owner.
- Avoid comments that narrate obvious statements or justify shortcuts; preserve essential external constraints and non-obvious invariants.
- Run focused checks after each independently verifiable slice; avoid deferring all verification to the end.

### 4. Prove it works

- Run the *actual* CLI/API/app/library/simulation path, not only a mocked or internal proxy. Verify version/commit, inputs, and output location. Reproduce the target failure before claiming a bug fix.
- Use the evidence fit for the surface: UI video or screenshots **plus** state assertions; API request/response and persisted readback; algorithm invariants and reproducible seeds; replay/geometry for spatial outputs; model checking for hard-to-reach concurrency or lifecycle properties.
- Capture the **action and its effect**, not merely a final pretty screenshot. Test meaningful failure/edge behavior when risk warrants it.
- Keep evidence reproducible and proportional. Record what was **not** verified and any stand-in environment. A green CI job does not establish the correct user intent by itself.

### 5. Review, subtract, and ship

- Review diff for redundant wrappers, duplicate domain decisions, extra scripts/flags, stale branches, unsupported assumptions and excessive comments.
- Distinguish: behavior **verified**, architecture **approved** (where needed), and scope **unverified**. Do not conflate them.
- Report concise evidence (command / commit / artifact / observed result / limitations) with links; do not paste raw logs into the MR when a durable artifact exists.
- For architectural changes, include a short delta: new/retired API, execution mode, dependency, persistent data format, long-lived tool or decision owner. An unchanged architecture needs no extra form.

## Review by proof, not just by diff

Before accepting a nontrivial change, ask:

- **Behavior:** What actual run proves the intended outcome? What input and version? What failed case was checked?
- **Verification quality:** Could the evidence pass while the actual user requirement fails? Are mocks, stale outputs or cached screenshots being mistaken for proof?
- **Architecture:** Does it reuse the canonical path? Did the change create a second decision authority or permanent one-off tool?
- **Change lifecycle:** What old callers/paths remain, who owns a necessary compatibility period, and what ends it?
- **Confidence:** Which parts are directly observed, inferred, or unverified?

Visual evidence is highly effective for UI and spatial behavior but **not a substitute** for contracts, tests, traces, or formal reasoning where those are more appropriate. Proof does not eliminate human judgment about product intent or architecture.

## Correction loop: convert lessons into environment

When an agent is corrected, especially for a recurring class of problem:

1. Reproduce a concrete prior failure; identify the root cause rather than the visible symptom.
2. Prefer removing the bad option by **better types, API or architecture**.
3. If it is mechanically decidable, add the **smallest** lint/contract/test/CI check; demonstrate one bad example fails and one legitimate example passes.
4. Improve the repo's canonical example or script so the correct path is natural; migrate known consumers and delete retired alternatives when safe.
5. Only then update brief repo guidance. Keep a trail of `problem → correction → enforcement → evidence` in the existing issue/MR system when material.
6. Occasionally inspect the same capability across successive changes for accumulated parallel paths or change amplification; no universal complexity score.

## Output for substantial work

Keep it to a short engineering receipt, not a long checklist:

- **Decision and ownership:** what was changed, why this existing path, and what was deliberately not added.
- **Evidence:** real command / action; commit and inputs; observable result; reusable artifact.
- **Architecture delta:** new or removed maintenance responsibility, or “none”.
- **Limits and follow-up:** important unverified paths and decisions requiring human approval.

For a simple edit, a one-paragraph result and actual check are enough. If only asked to analyze, do not modify source or CI without authorization. Respect repository authorization and pause at irreversible or external side effects.

## Project-owned companion

If no reliable project-local way exists to prove behavior, propose a `verify-<app>` **project-specific** skill/harness with launch, doctor, drive, evidence, cleanup and a feature map. Keep it close to the app and maintain it as code changes. See `references/verification-evidence.md` and `references/repo-contract-template.md`. Do not force UI/video workflows on backend-only systems.

## Attribution and scope

Principles informed by Lauren Tan's 2026 *All Code Is Slop (Except Mine)* talk and the official Cursor `pstack` skills (especially `correct`, `no-comments`, `create-verification-skill`, `maintain-verification-skill`, `statechart`, `principle-prove-it-works`, `reflect`). This is a selective adaptation, not a copy or a claim that the speaker mandates these defaults. See `references/source-and-adaptation.md`.
