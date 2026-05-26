---
id: advanced-subagents
title: "Subagents"
tier: advanced
order: 21
tags: [advanced, subagents, delegation]
version_added: "0.1"
updated: "2026-05-26"
---

# Subagents

A subagent is a separate Claude instance you delegate a task to. It runs with its
**own** context window and returns just a result — so heavy exploration (reading
many files, broad searches) happens *over there* and only the conclusion lands in
your main conversation. That keeps your primary context clean.

Subagents also run **in parallel**, which is how you fan out independent work
(e.g. research three areas at once) instead of doing it serially. You can use
general-purpose agents or define specialised ones with their own tools and prompt.

> **Flagship lesson — coming in M2**, with a hands-on, write-it-for-real example.
