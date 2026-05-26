---
id: slash-review
title: "/review · /code-review · /security-review · /ultrareview"
tier: slash-commands
order: 17
tags: [slash, review, quality]
version_added: "0.1"
updated: "2026-05-26"
---

# Reviewing code

A family of commands for checking work before it ships:

- **`/code-review [target]`** — review the current diff for correctness bugs;
  `--comment` can post findings as PR comments.
- **`/security-review`** — scan pending git changes for security issues
  (injection, auth gaps, data exposure).
- **`/review [PR]`** — pull a GitHub PR into the session and review it locally.
- **`/ultrareview [PR]`** — a deep, multi-agent review run in the cloud
  (a few free runs, then credit-based; you trigger it — Claude can't).

Habit: `/code-review` before you commit, `/security-review` on anything touching
auth, input handling, or secrets.
