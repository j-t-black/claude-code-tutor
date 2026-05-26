"""Headless smoke test for the content engine (M1).

Textual's `run_test()` mounts the app with a headless driver — no TTY needed —
so we can prove the engine end to end: manifest loads, content files are
discoverable (even from the installed package), the app boots, a lesson renders,
and progress round-trips. Uses a throwaway state file so your real progress is
untouched. Run with:

    uv run python scripts/smoke.py
"""

from __future__ import annotations

import asyncio
import tempfile
from pathlib import Path

from claude_code_tutor import content_model
from claude_code_tutor.app import TutorApp
from claude_code_tutor.content_model import load_manifest
from claude_code_tutor.playground import export_example
from claude_code_tutor.progress import Progress


async def _smoke() -> None:
    # 1. Content is discoverable (proves content/*.md ships with the package).
    manifest = load_manifest()
    assert manifest, f"no lessons found under {content_model.CONTENT_DIR}"
    print(f"manifest: {len(manifest)} lessons from {content_model.CONTENT_DIR}")

    # 2. App boots with an isolated progress file.
    with tempfile.TemporaryDirectory() as tmp:
        state = Path(tmp) / "progress.json"
        app = TutorApp(progress=Progress(state))
        async with app.run_test() as pilot:
            await pilot.pause()
            assert app.query_one("#nav"), "nav tree missing"
            assert app.query_one("#lesson-md"), "lesson pane missing"
            assert app.theme == "calm-mono", f"unexpected theme: {app.theme}"

            first = manifest[0].id
            # 3. Opening a lesson marks it started.
            app._show_lesson(first)
            assert app.progress.status(first) == "started", "open did not mark started"
            # 4. Marking done persists.
            app.action_mark_done()
            assert app.progress.status(first) == "done", "mark_done failed"

        # 5. State actually hit disk and reloads.
        reloaded = Progress(state)
        assert reloaded.status(first) == "done", "progress did not persist"

        # 6. A lesson's worked example exports to a real file.
        with_example = next((lesson for lesson in manifest if lesson.example), None)
        assert with_example is not None, "no lesson carries an example"
        out = export_example(with_example.example, base=Path(tmp) / "playground")
        assert out.exists() and out.read_text().strip(), "example not written"
        print(f"example export: {with_example.id} -> {out.name}")
    print("SMOKE OK")


if __name__ == "__main__":
    asyncio.run(_smoke())
