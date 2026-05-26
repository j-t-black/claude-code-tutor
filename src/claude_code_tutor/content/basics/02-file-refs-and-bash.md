---
id: basics-files-bash
title: "File refs (@) and bash (!)"
tier: basics
order: 2
tags: [basics, files, bash]
version_added: "0.1"
updated: "2026-05-26"
---

# File references (`@`) and inline bash (`!`)

Two characters change how you feed context to Claude:

## `@` — reference a file or directory

Typing `@` opens a fuzzy file picker. Selecting `@src/app.py` tells Claude
exactly which file you mean, and pulls it into context. This is far more precise
than describing a file in prose — and it works for directories too.

## `!` — run a shell command yourself

Prefixing a line with `!` runs that command in your shell and drops the output
straight into the conversation. Great for things Claude can't do for you
(interactive logins) or when you want to hand it the result of a command you ran.

Together these are the fastest ways to ground a turn in *real* context instead of
making Claude guess.
