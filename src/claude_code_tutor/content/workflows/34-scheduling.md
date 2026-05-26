---
id: workflows-scheduling
title: "Scheduling: /loop vs /schedule"
tier: workflows
order: 34
tags: [workflows, scheduling, automation]
version_added: "0.1"
updated: "2026-05-26"
---

# Scheduling recurring work

Two complementary ways to make Claude repeat itself:

- **`/loop [interval] [prompt]`** — runs a prompt over and over *while this
  session stays open* (e.g. `/loop 5m check the deploy`). Session-scoped; you can
  let Claude self-pace the interval. Good for watching something for a while.
- **`/schedule`** (alias `/routines`) — creates a **cloud routine** on Anthropic
  infrastructure that runs on a cron schedule, independent of any terminal. Good
  for persistent, unattended jobs (overnight monitoring, a daily digest).

Rule of thumb: **`/loop` while you wait, `/schedule` when you've walked away.**
This is exactly what the tutor's own M3 auto-refresh job will use.
