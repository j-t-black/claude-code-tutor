"""The Claude Code Tutor TUI — M0 shell.

Layout is a classic three-part TUI: a Header, a Horizontal body split into a
navigation Tree (left) and a scrolling lesson pane (right), and a Footer. The
command palette (ctrl+p) is Textual's built-in. Content arrives in M1; for now
the tree holds placeholder chapters and the lesson pane shows a welcome note.
"""

from __future__ import annotations

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Footer, Header, Markdown, Tree

# Glyph vocabulary the freshness/progress system will drive in M1.
#   ○ unread   ◐ started   ✓ done   ● new   ◆ updated
UNREAD = "○"

WELCOME = """\
```
 ██████╗ ██████╗    ████████╗██╗   ██╗████████╗ ██████╗ ██████╗
██╔════╝██╔════╝    ╚══██╔══╝██║   ██║╚══██╔══╝██╔═══██╗██╔══██╗
██║     ██║            ██║   ██║   ██║   ██║   ██║   ██║██████╔╝
██║     ██║            ██║   ██║   ██║   ██║   ██║   ██║██╔══██╗
╚██████╗╚██████╗       ██║   ╚██████╔╝   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚═════╝       ╚═╝    ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝
```

# Learn Claude Code, inside the terminal

This is the **M0 shell** — navigation, the lesson pane, and the command palette
are wired up. The curriculum itself lands in **M1**.

- Move through the tree on the left (arrow keys, or click).
- Press **ctrl+p** for the command palette.
- Press **q** to quit.

Tree glyphs you'll meet in M1:
`○` unread · `◐` started · `✓` done · `●` new · `◆` updated
"""


class TutorApp(App[None]):
    """Interactive, tutorial-style guide to Claude Code."""

    CSS = """
    #body {
        height: 1fr;
    }

    #nav {
        width: 36;
        border-right: vkey $accent 50%;
        padding: 0 1;
    }

    #lesson {
        padding: 1 2;
    }
    """

    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("ctrl+p", "command_palette", "Commands", show=True),
    ]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Horizontal(id="body"):
            yield self._build_nav()
            with VerticalScroll(id="lesson"):
                yield Markdown(WELCOME, id="lesson-md")
        yield Footer()

    def _build_nav(self) -> Tree[str]:
        """Placeholder curriculum tree — M1 replaces this from the content manifest."""
        tree: Tree[str] = Tree(f"{UNREAD} Curriculum", id="nav")
        tree.root.expand()

        basics = tree.root.add(f"{UNREAD} Basics")
        basics.add_leaf(f"{UNREAD} The prompt & input")
        basics.add_leaf(f"{UNREAD} File refs (@) and bash (!)")

        slash = tree.root.add(f"{UNREAD} Slash commands")
        slash.add_leaf(f"{UNREAD} /help")
        slash.add_leaf(f"{UNREAD} /clear & /compact")
        slash.add_leaf(f"{UNREAD} /context")

        advanced = tree.root.add(f"{UNREAD} Advanced")
        advanced.add_leaf(f"{UNREAD} Hooks")
        advanced.add_leaf(f"{UNREAD} Subagents")
        advanced.add_leaf(f"{UNREAD} Context management")

        workflows = tree.root.add(f"{UNREAD} Workflows")
        workflows.add_leaf(f"{UNREAD} Plan mode")
        return tree

    def on_mount(self) -> None:
        self.theme = "catppuccin-mocha"
        self.title = "Claude Code Tutor"
        self.sub_title = "M0 · shell"
