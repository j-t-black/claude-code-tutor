# Roadmap & notes

The planned build (M0–M3) is complete and the Reference corpus is full — **86
lessons** (Basics 5 · Slash commands 10 · Advanced 7 · Workflows 5 · Reference 59).
This file tracks the "go deeper" work and open design questions.

## Done
- **M0** shell · **M1** engine + 27-lesson skeleton + `calm-mono` theme
- **M2** flagships (hooks/subagents/context) + `e` playground export + `:` command bar
- **M3** freshness glyphs (`●`/`◆`) + `/refresh-content` self-refresh
- **Reference** tier: a per-command entry for all 59 slash commands, cross-linked

## Refine-later
- [x] Enrich the original 13 Reference entries' cross-links into the wider graph
- [ ] Deepen high-value entries (gotchas, examples) beyond one paragraph
- [ ] Teach `/refresh-content` to maintain the Reference tier too
- [ ] UI/UX pass (the `theme.tcss` + custom-theme workflow is ready)
- [ ] `textual serve` to share as a web link; package for uvx/pipx

## Notes
- The 46 bulk Reference entries were scaffolded from a one-off data-table generator
  written to `/tmp` (not committed). The emitted `.md` files are canonical — edit
  them directly or via `/refresh-content`; there is no generator in the repo to re-run.

## Open question — the `/refresh-content` workflow
How refreshed content comes back and gets merged (to settle before relying on it):
- **Diffs:** every refresh change is a git change, so you always review a diff.
- **Merge workflow (TBD):** direct-commit vs. propose-then-you-commit vs. branch + PR.
- **Version guidance:** record the Claude Code version each refresh verified against
  and surface it in the app — content tracks the latest while a reader may be on an
  older version. Possibly flag a minimum version on very new features.
