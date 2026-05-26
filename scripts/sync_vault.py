"""Re-sync the canonical repo into the Obsidian vault mirror.

`~/dev/claude-code-tutor` is the source of truth; the vault holds a browsable
mirror + the human-facing Plan.md. This copies the meaningful files (excluding
`.venv/`, `.git/`, `__pycache__/`) and leaves the vault's `*- Plan.md` untouched.

    uv run python scripts/sync_vault.py     # (or plain: python3 scripts/sync_vault.py)
"""

from __future__ import annotations

import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VAULT = Path(
    "/Users/jtblack/Library/Mobile Documents/com~apple~CloudDocs/"
    "Obsidian Vault/dev/projects/Claude Code Tutor"
)

# What to mirror. Excludes .venv/ and .git/ by omission; the vault Plan.md is not
# listed here, so it is never overwritten or deleted.
INCLUDE = [
    "src",
    "scripts",
    "docs",
    ".claude",
    "README.md",
    "pyproject.toml",
    "uv.lock",
    ".python-version",
    ".gitignore",
]
IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store")


def main() -> None:
    VAULT.mkdir(parents=True, exist_ok=True)
    for name in INCLUDE:
        src = REPO / name
        dst = VAULT / name
        if not src.exists():
            continue
        if src.is_dir():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst, ignore=IGNORE)
        else:
            shutil.copy2(src, dst)
    print(f"synced {len(INCLUDE)} entries -> {VAULT}")


if __name__ == "__main__":
    main()
