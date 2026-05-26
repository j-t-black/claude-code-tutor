---
id: advanced-hooks
title: "Hooks"
tier: advanced
order: 20
tags: [advanced, hooks, automation]
version_added: "0.1"
updated: "2026-05-26"
---

# Hooks

Hooks let you run your own commands automatically at specific points in Claude
Code's lifecycle — *before* a tool runs, *after* it succeeds, when Claude stops,
when a session starts, and more. They're configured in `settings.json`, and they
turn "please remember to…" into "this always happens."

Classic uses: auto-format files after every edit, run tests after code changes,
log every shell command, or block an action you never want taken. Because a hook
is just a command receiving JSON on stdin, it can do anything your shell can.

> **Flagship lesson — coming in M2.** This is one of the three topics we'll build
> out deeply, with a simulated configuration and a real, working example you can
> write into `./playground/` and adopt.
