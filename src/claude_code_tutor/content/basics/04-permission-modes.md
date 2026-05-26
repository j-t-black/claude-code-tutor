---
id: basics-permission-modes
title: "Permission modes (shift+tab)"
tier: basics
order: 4
tags: [basics, permissions, plan-mode]
version_added: "0.1"
updated: "2026-05-26"
---

# Permission modes

How much Claude can do without asking is governed by the **permission mode**,
which you cycle with **Shift+Tab**:

- **default** — asks before each edit or command.
- **acceptEdits** — applies file edits without prompting (still asks for riskier
  actions).
- **plan** — Claude researches and *proposes* changes without touching anything
  until you approve (covered as a pillar in Advanced → Planning).
- **auto** — auto-approves safe, read-only operations.

The mode is a session setting; you can also set a default and fine-tune
per-tool rules via `/permissions` and `settings.json`. The instinct to build:
match the mode to the risk — looser when exploring, tighter when it matters.
