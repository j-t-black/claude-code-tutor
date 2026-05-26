```
 ██████╗ ██████╗    ████████╗██╗   ██╗████████╗ ██████╗ ██████╗
██╔════╝██╔════╝    ╚══██╔══╝██║   ██║╚══██╔══╝██╔═══██╗██╔══██╗
██║     ██║            ██║   ██║   ██║   ██║   ██║   ██║██████╔╝
██║     ██║            ██║   ██║   ██║   ██║   ██║   ██║██╔══██╗
╚██████╗╚██████╗       ██║   ╚██████╔╝   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚═════╝       ╚═╝    ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝
```

> **Learn Claude Code without leaving the terminal.** An interactive, self-refreshing tutorial that doesn't *describe* a TUI — it **is** one.

![Python](https://img.shields.io/badge/Python-3.11+-3776ab?logo=python&logoColor=white)
![uv](https://img.shields.io/badge/uv-managed-de5fe9?logo=astral&logoColor=white)
![Textual](https://img.shields.io/badge/Textual-8-5e4bb6)
![theme](https://img.shields.io/badge/theme-calm--mono-c8b88a)
![lessons](https://img.shields.io/badge/lessons-94-8fae8f)

It boots straight into a panel layout, tracks what you've read, lets you **try things
for real**, and **keeps its own content current** as Claude Code evolves.

## ▍ the shell

```
 ┌──────────────────────────────────────────────────────────────────────────
 │ Claude Code Tutor                        3/94 done · Claude Code v2.1.142
 ├──────────────────────────────────────────────────────────────────────────
 │  ○ Basics                  ● Advanced
 │    ◐ The prompt & input      ◐ Hooks               ◀ reading
 │    ✓ File refs (@) and bash  ○ Subagents
 │  ○ Slash commands            ○ Context management
 │    ✓ /help   ◆ /context      ○ Memory · Planning · MCP · Skills
 │  ○ Workflows               ○ Reference
 │    ○ TDD · Worktrees …        · all 59 slash commands, cross-linked ·
 ├──────────────────────────────────────────────────────────────────────────
 │  ↑/↓ move   ⏎ open   d done   e try example   : command bar   q quit
 └──────────────────────────────────────────────────────────────────────────
```

> `○` unread &nbsp; `◐` started &nbsp; `✓` done &nbsp; `●` new &nbsp; `◆` updated
> &nbsp;—&nbsp; a real render lives at [`docs/screenshots/shell.svg`](docs/screenshots/shell.svg).

## ▍ run it

```console
$ cd claude-code-tutor
$ uv run cc-tutor                   # boot the tutor
  ↑/↓ open lessons · d done · e try an example · : command bar · q quit
```

```bash
uv run python scripts/smoke.py        # headless self-test (no TTY)
uv run python scripts/content_report.py   # the curriculum, with content hashes
```

## ▍ what's inside

- **94 lessons, five tiers** — Basics → Slash commands → Advanced → Workflows, then a
  granular **Reference** with a per-command entry for *every* slash command, each
  cross-linked to the ones it's used with (click one to jump).
- **Three flagships you can actually keep** — Hooks, Subagents, Context. Press **`e`**
  and a working example (a `settings.json` hook, a `test-runner` agent, a context
  checklist) is written into `./playground/` for you to lift into a real project.
- **A safe command bar** — press **`:`** and *simulate* a slash command (`/context`,
  `/compact`, …) with scripted output. Zero side effects; a sandbox for the curious.
- **Progress that sticks** — glyphs remember what you've read; `●`/`◆` flag what's new
  or changed since last time.

## ▍ stays current by itself

Claude Code moves fast, so the curriculum refreshes itself. **`/refresh-content`**
re-checks the live feature set via the `claude-code-guide` agent, writes the diff on a
branch, opens a PR, and a **gate agent** auto-merges it — but only if it's clean
(smoke passes **and** the diff touches content *only*, never code). The header shows
the Claude Code version the content was last verified against. Schedule it and walk
away:

```
/schedule run /refresh-content every Monday at 9am
```

## ▍ how it's built

- **Content is data.** Every lesson is markdown + YAML frontmatter; the engine just
  renders a manifest and knows nothing about any specific lesson — so adding or
  refreshing content never touches the app.
- **Design is decoupled.** The look lives in `theme.tcss` + a custom **`calm-mono`**
  theme (near-mono, in the Protey-Temen / Endel calm spirit). Swap palettes from the
  command palette (ctrl+p).
- **Freshness is derived.** Read-state + a content hash drive the `●`/`◆` glyphs — no
  manual bookkeeping.

## ▍ stack

| Layer      | Tool                                                        |
| ---------- | ----------------------------------------------------------- |
| Language   | [Python](https://www.python.org/) 3.11+ via [uv](https://docs.astral.sh/uv/) |
| TUI        | [Textual](https://textual.textualize.io/) 8 (on Rich)       |
| Theme      | custom **calm-mono** (near-monochrome, Temen/Endel-flavoured) |
| Content    | Markdown + YAML frontmatter, rendered from a manifest        |
| Currency   | `claude-code-guide` agent + a deterministic merge gate       |

---

<sub>A terminal-native way to go from "I know the basics" to hooks, subagents, and self-driving workflows. Built in the open with Claude Code.</sub>
