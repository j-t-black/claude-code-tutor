---
id: advanced-hooks
title: "Hooks"
tier: advanced
order: 20
tags: [advanced, hooks, automation]
version_added: "0.1"
updated: "2026-05-26"
example:
  label: "PostToolUse auto-format hook"
  dest: ".claude/settings.json"
  source: "examples/hooks-postformat.json"
---

# Hooks — make things happen automatically

A **hook** runs a command of *yours* at a specific point in Claude Code's
lifecycle. It's the difference between *asking* Claude to "remember to run the
formatter" (which it may forget) and the formatter **always** running — because
the harness fires it, not the model. Anything you want to happen *automatically in
response to an event* is a hook, not a preference.

## When hooks fire (events)

Hooks are keyed to lifecycle **events**. The ones you'll reach for first:

- **PreToolUse** — before a tool runs; it can *block* the call or rewrite its input.
- **PostToolUse** — after a tool succeeds (e.g. format the file that was just edited).
- **UserPromptSubmit** — when you send a message (inject context, log the prompt).
- **SessionStart** — set up environment or state when a session begins.
- **Stop** — when Claude finishes a turn.

(There are more — Notification, PreCompact, SubagentStop, PermissionRequest…)

## Where they live

Hooks are JSON under `"hooks"` in your settings: `~/.claude/settings.json` (all
projects), `.claude/settings.json` (committed, team-wide), or
`.claude/settings.local.json` (personal, gitignored). Each entry has a **matcher**
— which tool to match, e.g. `Write|Edit` — and a list of handlers.

## What a hook receives

A `command` hook is just a shell command, and Claude pipes it **JSON on stdin**:
`tool_name`, `tool_input`, and (for PostToolUse) `tool_response`. You pull out
what you need with `jq`. Handlers can also be `prompt`, `agent`, `http`, or
`mcp_tool` types — but a shell command covers most needs.

## A real one you can keep

This hook auto-runs Prettier on every file Claude writes or edits:

```json
{
  "hooks": {
    "PostToolUse": [
      { "matcher": "Write|Edit",
        "hooks": [{ "type": "command",
          "command": "jq -r '.tool_input.file_path // .tool_response.filePath' | { read -r f; [ -n \"$f\" ] && npx --yes prettier --write \"$f\"; } 2>/dev/null || true" }] }
    ]
  }
}
```

> **Try it for real — press `e`.** That writes this working hook into
> `./playground/.claude/settings.json`, where you can read it, tweak it, and lift
> it into a real project. We never touch your live config.

Once configured, **`/hooks`** shows what's active in a session.
