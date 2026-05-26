---
description: Refresh the tutorial's lessons against the current Claude Code feature set (branch + PR + review)
---

You are refreshing the **Claude Code Tutor** curriculum so it stays current as
Claude Code evolves. Work in `~/dev/claude-code-tutor`. Be accurate above all —
this content teaches people, and wrong instructions are worse than missing ones.
Nothing lands on the main branch without review.

## Workflow: branch → write → verify → PR → auto-review

1. **Branch.** `git switch -c refresh/$(date +%Y-%m-%d)`.
2. **See what exists.** `uv run python scripts/content_report.py` (ids, versions, hashes).
3. **Verified inventory.** Use the **claude-code-guide** agent for the CURRENT Claude
   Code feature set — every slash command, core usage, advanced pillars, workflows.
   Have it verify against `claude --help` and the official docs and **report the
   Claude Code version**.
4. **Diff and write** into `src/claude_code_tutor/content/`:
   - **New topic** → create a lesson in the right tier folder, following the existing
     frontmatter (`id`, `title`, `tier`, `order`, `tags`, `version_added`, `updated`)
     and one-paragraph house style. Set `version_added` and `updated` to today.
     For Reference entries, add a `**Related:**` line linking related commands as
     `lesson:<id>` (every link must resolve — smoke enforces this).
   - **Changed topic** → update the body and bump `updated` to today.
   - **Removed feature** → `git rm` the file; note it in the changelog.
5. **Record currency.** Update `src/claude_code_tutor/content/meta.json`:
   `verified_against` = the Claude Code version you checked, `refreshed` = today.
6. **Verify.** `uv run python scripts/smoke.py` must print `SMOKE OK` (parses, engine,
   examples, freshness, and **all cross-links resolve**).
7. **Sync the vault.** `python3 scripts/sync_vault.py`.
8. **Commit + push + PR.** Commit with a one-line summary, `git push -u origin HEAD`,
   then `gh pr create --fill` (title = adds/updates/removes + the version checked).
9. **Auto-review the PR.** Review the diff for accuracy against the docs, house style,
   and obvious errors; post the findings as a PR comment with `gh pr comment`. If
   anything is wrong, fix it on the branch and push again.
10. **Report + hand off.** Output a short changelog and the PR link. **Leave the merge
    to the human** — review the PR and the auto-review comment, then merge. (Only
    auto-merge if explicitly told to.)

Once merged, the freshness glyphs light up automatically: a **new** lesson shows `●`
and an **edited** body shows `◆` to anyone who had already read it. The app also shows
the `verified_against` version from `meta.json` so readers know how current it is.

## Running it on a schedule

```
/schedule run /refresh-content every Monday at 9am
```
