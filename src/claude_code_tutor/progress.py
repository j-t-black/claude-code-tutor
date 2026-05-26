"""Per-user progress + freshness state.

A tiny JSON store in the platform data dir records, per lesson, a status and the
content version the user last saw. Status drives the nav-tree glyphs. The
``new`` / ``updated`` glyphs become meaningful in M3 when the auto-refresh job
bumps lesson versions; the machinery (storing the seen version) is here now.
"""

from __future__ import annotations

import json
from pathlib import Path

from platformdirs import user_data_dir

STATE_VERSION = 1

# Status → glyph. Reading order of precedence is handled by the caller.
GLYPHS: dict[str, str] = {
    "unread": "○",
    "started": "◐",
    "done": "✓",
    "new": "●",
    "updated": "◆",
}


def default_state_path() -> Path:
    base = Path(user_data_dir("claude-code-tutor", appauthor=False))
    return base / "progress.json"


class Progress:
    """Load/save lesson progress; compute the glyph for a lesson."""

    def __init__(self, path: Path | None = None) -> None:
        self.path = path or default_state_path()
        self._data = self._load()

    def _load(self) -> dict:
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError):
            return {"version": STATE_VERSION, "lessons": {}}
        data.setdefault("lessons", {})
        return data

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self._data, indent=2), encoding="utf-8")

    def status(self, lesson_id: str) -> str:
        return self._data["lessons"].get(lesson_id, {}).get("status", "unread")

    def seen_version(self, lesson_id: str) -> str:
        return self._data["lessons"].get(lesson_id, {}).get("version", "")

    def mark(self, lesson_id: str, status: str, version: str = "") -> None:
        self._data["lessons"][lesson_id] = {"status": status, "version": version}
        self.save()

    def glyph(self, lesson_id: str, current_version: str = "") -> str:
        """Glyph for a lesson, factoring in freshness vs. the version on disk."""
        status = self.status(lesson_id)
        if status == "unread":
            return GLYPHS["unread"]
        # Seen before, but the content moved on since? Flag it as updated.
        if current_version and current_version != self.seen_version(lesson_id):
            return GLYPHS["updated"]
        return GLYPHS[status]

    def counts(self) -> dict[str, int]:
        done = sum(1 for v in self._data["lessons"].values() if v.get("status") == "done")
        started = sum(1 for v in self._data["lessons"].values() if v.get("status") == "started")
        return {"done": done, "started": started}
