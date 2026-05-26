---
id: advanced-skills
title: "Skills"
tier: advanced
order: 26
tags: [advanced, skills, authoring]
version_added: "0.1"
updated: "2026-05-26"
---

# Skills

A **skill** is a packaged, reusable procedure — a `SKILL.md` (in
`.claude/skills/<name>/`) plus any supporting scripts or docs. Skills can be
invoked explicitly as `/skill-name`, or Claude can reach for one automatically
when its description matches what you're doing. Crucially they **load on demand**,
so they cost nothing in context until used — unlike `CLAUDE.md`, which always loads.

Claude Code ships with bundled skills (you've met several), and you can **author
your own** to capture a multi-step workflow, domain guidance, or an integration.
The `write-a-skill` skill walks you through building one — a natural next project
once you spot a routine you repeat.
