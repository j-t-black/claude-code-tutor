---
id: workflows-background
title: "Background & parallel agents"
tier: workflows
order: 33
tags: [workflows, background, parallel]
version_added: "0.1"
updated: "2026-05-26"
---

# Background & parallel agents

Not everything needs your attention while it runs. Move a session to the
background with **`/background`** (`/bg`) or `claude --bg`, and watch all detached
work from the **agent view** (`claude agents`) — a dashboard of running sessions,
their state, and which ones need input. Attach with Enter, detach with the arrow
keys.

Inside a session, long shell commands can run in the background too, writing their
output to a file Claude reads back. Combined with subagents and worktrees, this is
how you fan work out instead of waiting on it serially.
