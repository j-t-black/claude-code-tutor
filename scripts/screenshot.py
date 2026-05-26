"""Render the M0 shell to an SVG so it can be eyeballed without a live TTY.

    uv run python scripts/screenshot.py

Writes docs/screenshots/m0-shell.svg — open it in any browser.
"""

from __future__ import annotations

import asyncio

from claude_code_tutor.app import TutorApp


async def _shot() -> None:
    app = TutorApp()
    async with app.run_test(size=(110, 32)) as pilot:
        await pilot.pause()
        path = app.save_screenshot("shell.svg", "docs/screenshots")
        print(f"saved {path}")


if __name__ == "__main__":
    asyncio.run(_shot())
