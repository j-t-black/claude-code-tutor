# claude-code-tutor

An interactive, tutorial-style guide to **Claude Code** that runs *inside your
terminal*. Built with [Textual](https://textual.textualize.io/).

It walks you from the basics (every slash command, core usage) up through the
advanced pillars — **hooks, subagents, context, memory, planning** — and lets
you *try things for real* by writing working examples into a scratch
`./playground/` so you can adopt them in your own workflow.

## status

**M0 — shell.** The app boots into a panel layout (header, navigation tree,
lesson pane, footer) with the built-in command palette wired up. Curriculum
content arrives in M1.

## run it

```bash
uv run cc-tutor          # launch the TUI
uv run python scripts/smoke.py   # headless smoke test (no TTY needed)
```

## roadmap

- **M1** — content engine + navigation + progress glyphs; full skeleton of every topic.
- **M2** — three deep flagship lessons (hooks, subagents, context), simulated command bar, real `./playground` export.
- **M3** — auto-refresh job: regenerate/extend content from current Claude Code docs (the "what's new" chapters).

## stack

Python · [uv](https://docs.astral.sh/uv/) · [Textual](https://textual.textualize.io/) · Catppuccin Mocha theme.
