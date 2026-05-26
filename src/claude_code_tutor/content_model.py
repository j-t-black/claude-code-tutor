"""Content model: lessons are markdown files with YAML frontmatter.

This is the "content = data" half of the architecture. The engine (app.py) knows
nothing about specific lessons; it just asks this module for a sorted manifest.
Lessons live in ``content/<tier>/NN-slug.md`` and are discovered at runtime.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

CONTENT_DIR = Path(__file__).resolve().parent / "content"

# Ordered tiers: (key, display label). Order here = order in the nav tree.
TIERS: tuple[tuple[str, str], ...] = (
    ("basics", "Basics"),
    ("slash-commands", "Slash commands"),
    ("advanced", "Advanced"),
    ("workflows", "Workflows"),
)
TIER_LABELS: dict[str, str] = dict(TIERS)
_TIER_RANK: dict[str, int] = {key: i for i, (key, _) in enumerate(TIERS)}


@dataclass(frozen=True)
class Lesson:
    """One lesson, parsed from a markdown+frontmatter file."""

    id: str
    title: str
    tier: str
    order: int
    body: str
    tags: tuple[str, ...] = ()
    version_added: str = ""
    updated: str = ""
    prereqs: tuple[str, ...] = ()
    source_path: Path | None = None

    @property
    def tier_label(self) -> str:
        return TIER_LABELS.get(self.tier, self.tier)


def _split_frontmatter(text: str) -> tuple[dict, str]:
    """Return (metadata, body). Tolerates files with no frontmatter."""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            meta = yaml.safe_load(parts[1]) or {}
            return meta, parts[2].lstrip("\n")
    return {}, text


def load_lesson(path: Path) -> Lesson:
    meta, body = _split_frontmatter(path.read_text(encoding="utf-8"))
    return Lesson(
        id=str(meta["id"]),
        title=str(meta["title"]),
        tier=str(meta["tier"]),
        order=int(meta.get("order", 0)),
        body=body,
        tags=tuple(meta.get("tags", []) or ()),
        version_added=str(meta.get("version_added", "")),
        updated=str(meta.get("updated", "")),
        prereqs=tuple(meta.get("prereqs", []) or ()),
        source_path=path,
    )


def load_manifest(content_dir: Path = CONTENT_DIR) -> list[Lesson]:
    """Discover and sort every lesson under ``content_dir``."""
    lessons = [load_lesson(p) for p in sorted(content_dir.rglob("*.md"))]
    lessons.sort(key=lambda lesson: (_TIER_RANK.get(lesson.tier, 99), lesson.order, lesson.title))
    return lessons


def group_by_tier(lessons: list[Lesson]) -> list[tuple[str, str, list[Lesson]]]:
    """Group lessons into ``(tier_key, tier_label, lessons)`` in tier order."""
    grouped: list[tuple[str, str, list[Lesson]]] = []
    for key, label in TIERS:
        in_tier = [lesson for lesson in lessons if lesson.tier == key]
        if in_tier:
            grouped.append((key, label, in_tier))
    return grouped
