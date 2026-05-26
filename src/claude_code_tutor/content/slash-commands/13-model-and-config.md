---
id: slash-model-config
title: "/model · /effort · /config · /theme"
tier: slash-commands
order: 13
tags: [slash, config]
version_added: "0.1"
updated: "2026-05-26"
---

# Session config & appearance

Tune *how* Claude runs and looks:

- **`/model [name]`** — switch the model for this session (e.g. a faster or more
  capable one for the task at hand).
- **`/effort [level]`** — set reasoning effort (low / medium / high / xhigh).
  More effort = deeper thinking, slower turns.
- **`/config`** — open the Settings UI (theme, model, output style, editor mode).
- **`/theme`** — change the colour theme (light, dark, colourblind, custom).
- **`/statusline`** · **`/tui [default|fullscreen]`** — customise the status line
  and switch to the flicker-free fullscreen renderer.

Most of these have an equivalent in `settings.json`; the commands are the quick,
interactive way in.
