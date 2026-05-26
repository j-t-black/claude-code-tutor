---
id: advanced-context
title: "Context management"
tier: advanced
order: 22
tags: [advanced, context]
version_added: "0.1"
updated: "2026-05-26"
example:
  label: "Context budget checklist"
  dest: "context-budget-checklist.md"
  source: "examples/context-checklist.md"
---

# Context management — your biggest quality lever

The context window is Claude's working memory for the session. Everything competes
for the same finite space, and as it fills, turns slow and quality can drift
("context rot"). Managing it well is one of the highest-leverage habits you can build.

## What's eating it (roughly in order)

1. **Conversation history** — every message, tool result, and reasoning step.
2. **MCP tool definitions** — all loaded tool manifests (kept lean by deferred
   loading / tool search).
3. **Large file contents** — anything read into context.
4. **CLAUDE.md** — loaded at startup; verbose memory costs you every turn.
5. **Preloaded skills** — skills load on demand, but a subagent's `skills:` inject
   their full content up front.

## Seeing and shaping it

Run **`/context`** to visualise the breakdown. Claude **auto-compacts** as the
window approaches ~95% full (clearing old tool outputs first, then summarising);
set `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` to trigger earlier. Steer a manual compaction
with **`/compact focus: <what to keep>`**, use `/clear` when the past is
irrelevant, and **delegate bulky work to subagents** so it never clutters your thread.

> **Try it — press `e`** for a copy-keepable context budget checklist in
> `./playground/`. Builds on the `/context` basics from the Slash commands tier.
