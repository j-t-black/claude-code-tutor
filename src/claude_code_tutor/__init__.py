"""Claude Code Tutor — an interactive terminal tutorial for Claude Code."""

from __future__ import annotations


def main() -> None:
    """Console-script entry point: launch the TUI."""
    from claude_code_tutor.app import TutorApp

    TutorApp().run()
