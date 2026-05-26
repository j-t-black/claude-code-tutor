---
id: advanced-subagents
title: "Subagents"
tier: advanced
order: 21
tags: [advanced, subagents, delegation]
version_added: "0.1"
updated: "2026-05-26"
example:
  label: "A test-runner subagent"
  dest: ".claude/agents/test-runner.md"
  source: "examples/subagent-test-runner.md"
---

# Subagents — delegate with a clean context

A **subagent** is a separate Claude instance you hand a task to. It runs in its
**own context window** with its **own** system prompt and tool access, and returns
only a result — so heavy work (reading many files, broad searches) happens *over
there*, and just the conclusion lands in your main thread. Subagents also run **in
parallel**, which is how you fan out independent work instead of doing it serially.

## Defining one

A custom subagent is a markdown file in **`.claude/agents/<name>.md`** (project
scope) or **`~/.claude/agents/<name>.md`** (user scope). The YAML frontmatter
configures it; the body *is* its system prompt.

- **`name`** *(required)* — identifier (lowercase + hyphens).
- **`description`** *(required)* — when Claude should delegate to it; "use
  proactively" phrasing encourages automatic delegation.
- **`tools`** *(optional)* — comma-separated allowlist; inherits all if omitted.
- **`model`** *(optional)* — `haiku` / `sonnet` / `opus` / a full id / `inherit`. A
  cheap, fast model is often perfect for a narrow agent.
- Plus `permissionMode`, `maxTurns`, `skills`, `isolation: worktree`, `color`, and more.

## Invoking one

Three ways, not mutually exclusive: Claude **delegates automatically** when your
task matches an agent's description; you **@-mention** it (`@test-runner`) to force
it for a turn; or you run an entire session as one via `--agent <name>`. Manage
them with **`/agents`**.

> **Try it for real — press `e`** to write a working `test-runner` agent into
> `./playground/.claude/agents/test-runner.md`. Read it, adapt the prompt, and drop
> it into a real project's `.claude/agents/`.
