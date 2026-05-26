---
id: workflows-worktrees
title: "Git worktrees"
tier: workflows
order: 32
tags: [workflows, git, parallel]
version_added: "0.1"
updated: "2026-05-26"
---

# Git worktrees

`claude --worktree [name]` spins up an **isolated git worktree** on a fresh branch
(under `.claude/worktrees/<name>/`), so you can work on a feature without
disturbing your main checkout — or run several efforts in parallel with no file
collisions. Use a `.worktreeinclude` file (gitignore syntax) to copy across
untracked essentials like `.env`.

Cleanup is automatic when you exit with no changes; if you made commits, Claude
asks whether to keep or discard the worktree. This is the backbone of running
**parallel agents** safely.
