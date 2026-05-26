---
id: advanced-planning
title: "Planning & the Plan agent"
tier: advanced
order: 24
tags: [advanced, planning, plan-mode]
version_added: "0.1"
updated: "2026-05-26"
---

# Planning & the Plan agent

Planning means making Claude **think and propose before it acts**. Enter plan mode
with **Shift+Tab** (or `/plan`): Claude researches the code and presents an
approach for your approval *without making edits*. You review, refine, and only
then let it execute — catching a wrong direction while it's still a cheap paragraph
to fix instead of a pile of changes to undo.

For larger or fuzzier work, there's a dedicated **Plan agent** (a subagent
specialised for designing implementation strategies). The habit to build: default
to planning for anything non-trivial or unfamiliar, and treat the plan as the
cheap place to disagree.
