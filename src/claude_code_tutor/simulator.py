"""Scripted, side-effect-free simulations of slash commands.

The command bar (the `:` key in the app) feeds raw input here and renders the
returned markdown into the lesson pane. Nothing real happens — it's a safe place
to *see* what a command does before running it for real.
"""

from __future__ import annotations

BANNER = "> **simulated** — nothing real happened; this is a safe practice sandbox.\n\n"

_SIM: dict[str, str] = {
    "/help": (
        "### Available commands (excerpt)\n\n"
        "```\n"
        "/help      show commands\n"
        "/context   visualise context-window usage\n"
        "/compact   summarise to free space\n"
        "/clear     start fresh (keeps CLAUDE.md)\n"
        "/model     switch model\n"
        "/agents    manage subagents\n"
        "/mcp       manage MCP servers\n"
        "/hooks     view configured hooks\n"
        "```\n\n"
        "Type any of these into the bar to simulate it."
    ),
    "/context": (
        "### /context — context window (simulated)\n\n"
        "```\n"
        "System prompt     ~4.0k  ██\n"
        "Tools / MCP        2.1k  █\n"
        "CLAUDE.md          1.3k  ▌\n"
        "Files in context  18.4k  █████████\n"
        "Conversation      31.2k  ███████████████\n"
        "Free             ~143k\n"
        "```\n\n"
        "≈ 57k / 200k used. See the **Context management** lesson to act on this."
    ),
    "/compact": (
        "### /compact (simulated)\n\n"
        "Summarised 18 older turns into a compact summary — freed ≈28k tokens, "
        "continuity preserved. Tip: `/compact focus: keep the auth refactor` steers it."
    ),
    "/clear": (
        "### /clear (simulated)\n\n"
        "Conversation history cleared; project memory (CLAUDE.md) kept. "
        "The next turn starts fresh."
    ),
    "/model": (
        "### /model (simulated)\n\n"
        "Current: **opus**. Available: opus · sonnet · haiku. "
        "Pick one to switch for this session."
    ),
    "/usage": (
        "### /usage — this session (simulated)\n\n"
        "Cost **$0.42** · model opus · 18 turns.\n\n"
        "By tool: Bash 6 · Edit 9 · Read 21."
    ),
    "/status": (
        "### /status (simulated)\n\n"
        "Claude Code v2.1.142 · model opus · signed in · MCP: 2 connected."
    ),
    "/agents": (
        "### /agents (simulated)\n\n"
        "- **test-runner** (haiku) — run tests, report failures\n"
        "- *define your own in* `.claude/agents/<name>.md`\n\n"
        "See the **Subagents** lesson — press `e` there to export this one."
    ),
    "/mcp": (
        "### /mcp (simulated)\n\n"
        "Connected servers:\n- github (http) ✓\n- supabase (http) ✓\n\n"
        "Authenticate and manage them here."
    ),
    "/hooks": (
        "### /hooks (simulated)\n\n"
        "Active hooks:\n- PostToolUse · `Write|Edit` → prettier --write\n\n"
        "See the **Hooks** lesson — press `e` there to export a working example."
    ),
}

# Common aliases → canonical command.
_ALIASES = {"/cost": "/usage", "/stats": "/usage", "/reset": "/clear", "/new": "/clear"}


def simulate(raw: str) -> str:
    """Return simulated markdown output for a typed command (always prefixed)."""
    text = raw.strip()
    cmd = text.split()[0] if text else ""
    if cmd and not cmd.startswith("/"):
        cmd = "/" + cmd
    cmd = _ALIASES.get(cmd, cmd)
    body = _SIM.get(cmd)
    if body is None:
        shown = cmd or text or "(nothing)"
        return (
            BANNER
            + f"`{shown}` isn't in the simulator yet.\n\n"
            + "Try `/help` to see what is — or open its lesson in the tree."
        )
    return BANNER + body
