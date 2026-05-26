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
from textual.widgets import Input

from claude_code_tutor.content_model import load_manifest
from claude_code_tutor.playground import export_example
from claude_code_tutor.progress import Progress
from claude_code_tutor.simulator import simulate


async def _smoke() -> None:
    # 1. Content is discoverable (proves content/*.md ships with the package).
    manifest = load_manifest()
    assert manifest, f"no lessons found under {content_model.CONTENT_DIR}"
    print(f"manifest: {len(manifest)} lessons from {content_model.CONTENT_DIR}")

    # Reference tier exists and every cross-link resolves to a real lesson.
    import re

    ids = {lesson.id for lesson in manifest}
    assert "reference" in {lesson.tier for lesson in manifest}, "reference tier missing"
    for lesson in manifest:
        for target in re.findall(r"lesson:([a-z0-9-]+)", lesson.body):
            assert target in ids, f"broken cross-link 'lesson:{target}' in {lesson.id}"
    print("reference tier + cross-links OK")

    # Content currency metadata is present.
    from claude_code_tutor.content_model import content_meta

    assert content_meta().get("verified_against"), "content meta missing verified_against"

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

            # 5. Command bar simulates a command with no side effects.
            assert "context window" in simulate("/context")
            app.action_command_bar()
            await pilot.pause()
            assert app.query_one("#cmdbar", Input).display is True, "command bar didn't open"
            app.query_one("#cmdbar", Input).value = "/context"
            await pilot.press("enter")
            await pilot.pause()
            assert app.current_lesson_id is None, "sim command did not run"

            # 6. Cross-link navigation jumps to a lesson.
            ref = next((lesson for lesson in manifest if lesson.tier == "reference"), None)
            assert ref is not None, "no reference lesson"
            app._goto_lesson(ref.id)
            assert app.current_lesson_id == ref.id, "cross-link navigation failed"

        # 5. State actually hit disk and reloads.
        reloaded = Progress(state)
        assert reloaded.status(first) == "done", "progress did not persist"

        # 6. A lesson's worked example exports to a real file.
        with_example = next((lesson for lesson in manifest if lesson.example), None)
        assert with_example is not None, "no lesson carries an example"
        out = export_example(with_example.example, base=Path(tmp) / "playground")
        assert out.exists() and out.read_text().strip(), "example not written"
        print(f"example export: {with_example.id} -> {out.name}")

        # 7. Freshness model: new (●) and updated (◆) detection.
        from claude_code_tutor import progress as progress_mod

        fresh = Progress(Path(tmp) / "fresh.json")
        assert fresh.new_ids({"a", "b"}) == set(), "first run should flag nothing new"
        fresh.register_catalog({"a", "b"})
        assert fresh.new_ids({"a", "b", "c"}) == {"c"}, "new lesson not detected"
        assert fresh.glyph("c", is_new=True) == progress_mod.GLYPHS["new"], "● wrong"
        fresh.mark("a", "done", "hash1")
        assert fresh.glyph("a", "hash1") == progress_mod.GLYPHS["done"], "✓ wrong"
        assert fresh.glyph("a", "hash2") == progress_mod.GLYPHS["updated"], "◆ wrong"
        print("freshness: ● new / ◆ updated OK")
    print("SMOKE OK")


if __name__ == "__main__":
    asyncio.run(_smoke())
