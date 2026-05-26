---
description: Refresh the tutorial's lessons against the current Claude Code feature set
---

You are refreshing the **Claude Code Tutor** curriculum so it stays current as
Claude Code evolves. Work in `~/dev/claude-code-tutor`. Be accurate above all —
this content teaches people, and wrong instructions are worse than missing ones.

## Steps

1. **See what exists.** Run `uv run python scripts/content_report.py` to list the
   current lessons (ids, `version_added`, `updated`, content hash, title).

2. **Get a verified inventory.** Use the **claude-code-guide** agent to produce a
   current inventory of Claude Code: every slash command, core-usage basics, the
   advanced pillars, and power-user workflows. Tell it to verify against
   `claude --help` and the official docs and to report the Claude Code version.

3. **Diff and write.** Compare the inventory to `src/claude_code_tutor/content/`:
   - **New topic** (no matching lesson): create a markdown file in the right tier
     folder (`basics/`, `slash-commands/`, `advanced/`, `workflows/`), following the
     existing frontmatter (`id`, `title`, `tier`, `order`, `tags`, `version_added`,
     `updated`) and the one-paragraph house style. Set both `version_added` and
     `updated` to **today's date**.
   - **Changed topic** (lesson exists but facts moved): update the body and bump
     **`updated`** to today. Leave `version_added` alone.
   - **Removed feature**: only delete if it's truly gone — `git rm` the file and
     note it in the changelog.
   - For exportable examples, keep the artifact under `content/examples/` and the
     `example:` frontmatter pointing at it.

4. **Verify.** Run `uv run python scripts/smoke.py` — it must print `SMOKE OK`
   (manifest parses, engine works, examples export, freshness logic holds).

5. **Sync the vault.** Run `python3 scripts/sync_vault.py`.

6. **Commit.** Stage and commit with a one-line summary plus a short changelog of
   what was added/updated/removed (and the Claude Code version checked against).

## Why this lights up the glyphs automatically

The app derives freshness from the content itself: a **new** lesson file shows
`●` to anyone whose stored catalog predates it, and an **edited body** (its hash
changes) shows `◆` to anyone who had already read it. So you don't set glyph state
by hand — writing correct content is enough.

## Running it on a schedule

To keep this automatic, set up a routine that runs this command, e.g. weekly:

```
/schedule run /refresh-content every Monday at 9am
```
