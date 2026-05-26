---
id: ref-loop
title: "/loop"
tier: reference
order: 76
tags: [reference, slash, automation]
version_added: "0.1"
updated: "2026-05-26"
---

# /loop

`/loop [interval] [prompt]` runs a prompt repeatedly while *this* session stays open — e.g. polling a deploy. Session-scoped (unlike the cloud [/schedule](lesson:ref-schedule)), and it can self-pace the interval. To run until a condition rather than forever, [/goal](lesson:ref-goal).

**Related:** [/schedule](lesson:ref-schedule) · [/goal](lesson:ref-goal)
