---
id: advanced-memory
title: "Memory & CLAUDE.md"
tier: advanced
order: 23
tags: [advanced, memory, claude-md]
version_added: "0.1"
updated: "2026-05-26"
---

# Memory & CLAUDE.md

Claude Code loads instructions from a **layered set of `CLAUDE.md` files**, most
to least broad:

- **Managed/policy** — org-wide, set by an administrator (can't be overridden).
- **User** — `~/.claude/CLAUDE.md`, your preferences across every project.
- **Project** — `./CLAUDE.md` or `./.claude/CLAUDE.md`, shared with the team in git.
- **Local** — `./CLAUDE.local.md`, personal and gitignored.

You can `@import` other files, and scope rules to paths with `.claude/rules/`.
Separately, **auto-memory** lets Claude persist its own learnings between sessions
(under `~/.claude/projects/<project>/memory/`), and you can jot a memory inline by
starting a line with **`#`**. Run **`/memory`** to view and edit all of it.

> **Pairs with the flagship lessons** — good memory hygiene is half of good context.
