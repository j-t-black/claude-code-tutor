"""Write a lesson's worked example into ./playground/ for hands-on tries.

This is the "learn by doing, safely" half of M2: a lesson can carry a real,
working artifact (a settings.json hook, a subagent definition, …). Pressing `e`
copies it into a scratch ``playground/`` directory under the current working
directory — which is gitignored — so you can read, run, and adapt it without the
tutor ever touching your live config.
"""

from __future__ import annotations

from pathlib import Path

from claude_code_tutor.content_model import CONTENT_DIR, Example

DEFAULT_BASE = Path("playground")


def export_example(example: Example, base: Path = DEFAULT_BASE) -> Path:
    """Copy ``example``'s source content to ``base/<dest>``; return the path written."""
    src = CONTENT_DIR / example.source
    dest = base / example.dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    return dest
