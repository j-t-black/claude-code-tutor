"""The Claude Code Tutor TUI — M1 content engine.

The shell from M0 now reads a real curriculum: the nav tree is built from the
content manifest, grouped by tier, each lesson prefixed with a progress glyph.
Selecting a lesson renders it in the pane and marks it started; ``d`` marks the
current lesson done. Progress persists to a JSON state file between sessions.

Content lives in ``content/`` (see content_model.py); this module is the engine
and knows nothing about any specific lesson.
"""

from __future__ import annotations

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, VerticalScroll
from textual.theme import Theme
from textual.widgets import Footer, Header, Input, Markdown, Tree
from textual.widgets.tree import TreeNode

from claude_code_tutor.content_model import Lesson, group_by_tier, load_manifest
from claude_code_tutor.playground import export_example
from claude_code_tutor.progress import Progress
from claude_code_tutor.simulator import simulate

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

Pick a lesson from the tree on the left. As you go, the glyphs track you:

`○` unread · `◐` started · `✓` done · `●` new · `◆` updated

- **Enter / click** opens a lesson (and marks it started).
- **d** marks it done · **e** writes a lesson's worked example into `./playground/`.
- **`:`** opens a command bar to *simulate* slash commands safely.
- **ctrl+p** opens the command palette · **q** quits.
"""


# A calm, near-monochrome theme in the Temen/Endel spirit — registered at mount.
CALM_MONO = Theme(
    name="calm-mono",
    primary="#9aa7b1",
    secondary="#6f7b85",
    accent="#c8b88a",
    foreground="#e8e6e1",
    background="#0d0d0d",
    surface="#141414",
    panel="#1c1c1c",
    success="#8fae8f",
    warning="#d2b48c",
    error="#c98a8a",
    dark=True,
    variables={
        "footer-key-foreground": "#c8b88a",
        "block-cursor-text-style": "none",
    },
)


class TutorApp(App[None]):
    """Interactive, tutorial-style guide to Claude Code."""

    CSS_PATH = "theme.tcss"

    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("d", "mark_done", "Mark done"),
        Binding("e", "export_example", "Try example"),
        Binding("colon", "command_bar", "Sim command"),
        Binding("ctrl+p", "command_palette", "Commands", show=True),
        Binding("escape", "close_cmdbar", show=False),
    ]

    def __init__(self, progress: Progress | None = None) -> None:
        super().__init__()
        self.manifest: list[Lesson] = load_manifest()
        self.lessons: dict[str, Lesson] = {lesson.id: lesson for lesson in self.manifest}
        self.progress: Progress = progress or Progress()
        # Freshness: which lessons appeared since the user's last run, then record
        # the current catalog so they won't read as "new" next time.
        current_ids = set(self.lessons)
        self._new_ids: set[str] = self.progress.new_ids(current_ids)
        self.progress.register_catalog(current_ids)
        self._lesson_nodes: dict[str, TreeNode[str | None]] = {}
        self.current_lesson_id: str | None = None

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Horizontal(id="body"):
            yield self._build_nav()
            with VerticalScroll(id="lesson"):
                yield Markdown(WELCOME, id="lesson-md")
        yield Input(
            placeholder="Simulate a slash command — e.g. /context   (Enter to run · Esc to close)",
            id="cmdbar",
        )
        yield Footer()

    def _build_nav(self) -> Tree[str | None]:
        tree: Tree[str | None] = Tree("Curriculum", id="nav", data=None)
        tree.show_root = False
        tree.guide_depth = 3
        for _key, label, lessons in group_by_tier(self.manifest):
            tier_node = tree.root.add(label, data=None, expand=True)
            for lesson in lessons:
                leaf = tier_node.add_leaf(self._leaf_label(lesson), data=lesson.id)
                self._lesson_nodes[lesson.id] = leaf
        return tree

    def _leaf_label(self, lesson: Lesson) -> str:
        glyph = self.progress.glyph(
            lesson.id, lesson.content_hash, is_new=lesson.id in self._new_ids
        )
        return f"{glyph} {lesson.title}"

    def on_mount(self) -> None:
        self.register_theme(CALM_MONO)
        self.theme = "calm-mono"
        self.title = "Claude Code Tutor"
        self._set_subtitle()
        self.query_one("#nav", Tree).focus()

    def _set_subtitle(self) -> None:
        counts = self.progress.counts()
        self.sub_title = f"M1 · {counts['done']}/{len(self.manifest)} done"

    def on_tree_node_selected(self, event: Tree.NodeSelected[str | None]) -> None:
        lesson_id = event.node.data
        if lesson_id is None:  # tier or root node — ignore
            return
        self._show_lesson(lesson_id)

    def _show_lesson(self, lesson_id: str) -> None:
        lesson = self.lessons[lesson_id]
        self.query_one("#lesson-md", Markdown).update(lesson.body)
        self.current_lesson_id = lesson_id
        if self.progress.status(lesson_id) == "unread":
            self.progress.mark(lesson_id, "started", lesson.content_hash)
            self._refresh_glyph(lesson_id)

    def action_mark_done(self) -> None:
        if self.current_lesson_id is None:
            self.notify("Open a lesson first.", severity="warning")
            return
        lesson = self.lessons[self.current_lesson_id]
        self.progress.mark(lesson.id, "done", lesson.content_hash)
        self._refresh_glyph(lesson.id)
        self._set_subtitle()
        self.notify(f"Marked done: {lesson.title}")

    def action_export_example(self) -> None:
        lesson = self.lessons.get(self.current_lesson_id) if self.current_lesson_id else None
        if lesson is None:
            self.notify("Open a lesson first.", severity="warning")
            return
        if lesson.example is None:
            self.notify("This lesson has no example to export.", severity="warning")
            return
        path = export_example(lesson.example)
        self.notify(f"Wrote → {path}", title=lesson.example.label)

    def action_command_bar(self) -> None:
        bar = self.query_one("#cmdbar", Input)
        bar.display = True
        bar.focus()

    def action_close_cmdbar(self) -> None:
        bar = self.query_one("#cmdbar", Input)
        if bar.display:
            bar.value = ""
            bar.display = False
            self.query_one("#nav", Tree).focus()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.input.id != "cmdbar":
            return
        command = event.value.strip()
        event.input.value = ""
        event.input.display = False
        self.query_one("#nav", Tree).focus()
        if command:
            self.query_one("#lesson-md", Markdown).update(simulate(command))
            self.current_lesson_id = None

    def _refresh_glyph(self, lesson_id: str) -> None:
        node = self._lesson_nodes.get(lesson_id)
        if node is not None:
            node.set_label(self._leaf_label(self.lessons[lesson_id]))
