---
id: workflows-headless-ci
title: "Headless & CI usage"
tier: workflows
order: 35
tags: [workflows, ci, headless, automation]
version_added: "0.1"
updated: "2026-05-26"
---

# Headless & CI usage

Claude Code isn't only interactive. Run **`claude -p "…"`** (`--print`) to get a
single non-interactive response you can pipe in a script. Flags like `--model`,
`--permission-mode`, `--settings`, and `--mcp-config` configure behaviour for
automation, and `ANTHROPIC_API_KEY` (or `ANTHROPIC_AUTH_TOKEN`) handles auth.

Combine headless mode with worktrees (`--worktree`), the agent view (`--bg`), and
**hooks** for validation, and you can wire Claude into CI to review diffs, triage
issues, or run scheduled maintenance — code-driven, no human in the loop.
