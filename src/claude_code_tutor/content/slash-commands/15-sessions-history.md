---
id: slash-sessions-history
title: "/resume · /branch · /rewind · /recap · /export"
tier: slash-commands
order: 15
tags: [slash, sessions, history]
version_added: "0.1"
updated: "2026-05-26"
---

# Navigating & capturing sessions

Your conversation isn't a one-way street:

- **`/resume [id|name]`** — return to a previous conversation, full history intact.
- **`/branch [name]`** — fork the conversation at this point; the original is kept,
  so you can explore an alternative without losing your place.
- **`/rewind`** — roll *code and conversation* back to an earlier checkpoint (or
  summarise from a message). The undo button for a turn that went sideways.
- **`/recap`** — generate a one-line summary of the session so far.
- **`/export`** / **`/copy [N]`** / **`/diff`** — save the conversation to a file,
  copy the last (or Nth) reply to the clipboard, or open an interactive diff of
  uncommitted changes.

Together these let you experiment fearlessly — branch, try, rewind if needed.
