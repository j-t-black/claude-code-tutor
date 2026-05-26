---
id: ref-batch
title: "/batch"
tier: reference
order: 73
tags: [reference, slash, parallel]
version_added: "0.1"
updated: "2026-05-26"
---

# /batch

`/batch <instruction>` orchestrates a large parallel change across the codebase, spawning isolated subagents in their own worktrees. Reach for it when a mechanical change spans many files. It builds on [/agents](lesson:ref-agents) and runs like [/background](lesson:ref-background) work.

**Related:** [/agents](lesson:ref-agents) · [/background](lesson:ref-background)
