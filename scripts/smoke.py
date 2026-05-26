"""Headless smoke test for the M0 shell.

Textual's `run_test()` mounts the app with a headless driver — no TTY needed —
so we can prove the app boots, parses its CSS, builds the widget tree, and
applies the theme without a human at a terminal. Run with:

    uv run python scripts/smoke.py
"""

from __future__ import annotations

import asyncio

from claude_code_tutor.app import TutorApp


async def _smoke() -> None:
    app = TutorApp()
    async with app.run_test() as pilot:
        await pilot.pause()
        # Core widgets mounted?
        assert app.query_one("#nav"), "nav tree missing"
        assert app.query_one("#lesson"), "lesson pane missing"
        assert app.query_one("#lesson-md"), "lesson markdown missing"
        # Theme applied?
        assert app.theme == "catppuccin-mocha", f"unexpected theme: {app.theme}"
        # Command palette available (built-in)?
        assert app.ENABLE_COMMAND_PALETTE, "command palette disabled"
    print("SMOKE OK")


if __name__ == "__main__":
    asyncio.run(_smoke())
