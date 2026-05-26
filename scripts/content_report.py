"""Print the current lesson catalog with content hashes.

This is the input the refresh job reads to see what already exists before it
diffs against a fresh feature inventory. Also handy for humans.

    uv run python scripts/content_report.py
"""

from __future__ import annotations

from claude_code_tutor.content_model import group_by_tier, load_manifest


def main() -> None:
    manifest = load_manifest()
    print(f"# Content report — {len(manifest)} lessons\n")
    for _key, label, lessons in group_by_tier(manifest):
        print(f"## {label}")
        for lesson in lessons:
            print(
                f"- {lesson.id:24} added:{lesson.version_added or '-':8} "
                f"updated:{lesson.updated or '-':12} #{lesson.content_hash}  {lesson.title}"
            )
        print()


if __name__ == "__main__":
    main()
