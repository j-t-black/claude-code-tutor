---
id: slash-diagnostics
title: "/status · /usage · /doctor · /debug"
tier: slash-commands
order: 16
tags: [slash, diagnostics]
version_added: "0.1"
updated: "2026-05-26"
---

# Diagnostics & meta

When you want to know what's going on:

- **`/status`** — version, model, account, and connectivity (works even while
  Claude is mid-response).
- **`/usage`** (aliases `/cost`, `/stats`) — session cost, plan limits, and a
  breakdown of activity by skill / subagent / MCP server.
- **`/doctor`** — health-check your install and settings; press `f` to auto-fix.
- **`/debug`** — turn on debug logging to troubleshoot a misbehaving session.
- **`/feedback`** (aliases `/bug`, `/share`) — file a bug or request with session
  context attached. **`/release-notes`** — browse the changelog.
- **`/btw <question>`** — ask a quick side question *without* adding it to the
  conversation history (cheap, no context cost).
