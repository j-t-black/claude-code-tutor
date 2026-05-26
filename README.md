# claude-code-tutor

An interactive, tutorial-style guide to **Claude Code** that runs *inside your
terminal*. Built with [Textual](https://textual.textualize.io/).

It walks you from the basics (every slash command, core usage) up through the
advanced pillars — **hooks, subagents, context, memory, planning** — and the
power-user workflows, and lets you *try things for real* by writing working
examples into a scratch `./playground/` so you can adopt them in your own work.

## run it

```bash
uv run cc-tutor                      # launch the TUI
uv run python scripts/smoke.py       # headless self-test (no TTY needed)
uv run python scripts/content_report.py   # list lessons + content hashes
python3 scripts/sync_vault.py        # mirror the repo into the Obsidian vault
```

Inside the app:

- **↑/↓ / click** move through the curriculum tree; **Enter** opens a lesson.
- **d** marks a lesson done · **e** writes its worked example into `./playground/`.
- **`:`** opens a command bar that *simulates* slash commands (safe, no side effects).
- **ctrl+p** the command palette (incl. theme switching) · **q** quits.

Progress glyphs: `○` unread · `◐` started · `✓` done · `●` new · `◆` updated.

## keeping it current

Claude Code changes often, so the curriculum can refresh itself. The
`/refresh-content` command (in `.claude/commands/`) runs the `claude-code-guide`
agent to get a verified, current feature inventory, diffs it against the existing
lessons, and writes/updates files. New lessons then show `●` and changed ones show
`◆` automatically (the app derives freshness from the content). Schedule it:

```
/schedule run /refresh-content every Monday at 9am
```

## status

All milestones complete: **M0** shell · **M1** content engine + 27-lesson skeleton
· **M2** flagships + playground export + simulated command bar · **M3** freshness
glyphs + self-refresh.

## stack

Python · [uv](https://docs.astral.sh/uv/) · [Textual](https://textual.textualize.io/)
· custom near-mono **calm-mono** theme (switchable via the command palette).
