"""Deterministic pre-merge gate for content-refresh PRs.

Defense-in-depth: even assuming the incoming text is sanitised upstream
(serial-guard), an automated refresh must only ever change CONTENT. This check is
the hard backstop the refresh-gate agent relies on before it auto-merges:

  1. the smoke test passes (parses, engine, examples, freshness, cross-links);
  2. the diff touches ONLY content/docs — never code, settings, scripts, packaging;
  3. it isn't a mass deletion.

Run on the PR branch:  uv run python scripts/gate_check.py [base_ref]   (default origin/main)
Exit 0 = PASS (safe to auto-merge), 1 = FAIL (route to a human).
"""

from __future__ import annotations

import subprocess
import sys

# Only these path prefixes may change in an auto-mergeable refresh.
ALLOWED_PREFIXES = (
    "src/claude_code_tutor/content/",
    "docs/",
    "README.md",
)
MAX_DELETIONS = 5


def _run(cmd: list[str]) -> tuple[int, str]:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, proc.stdout + proc.stderr


def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else "origin/main"
    failures: list[str] = []

    code, out = _run(["uv", "run", "python", "scripts/smoke.py"])
    if code != 0:
        failures.append("smoke.py failed:\n" + out[-800:])
    else:
        print("✓ smoke passed")

    changed = [f for f in _run(["git", "diff", "--name-only", f"{base}...HEAD"])[1].splitlines() if f.strip()]
    offending = [f for f in changed if not f.startswith(ALLOWED_PREFIXES)]
    if offending:
        failures.append("changes outside content/docs (needs human review): " + ", ".join(offending))
    else:
        print(f"✓ {len(changed)} changed file(s), all within content/docs")

    deleted = [f for f in _run(["git", "diff", "--name-only", "--diff-filter=D", f"{base}...HEAD"])[1].splitlines() if f.strip()]
    if len(deleted) > MAX_DELETIONS:
        failures.append(f"{len(deleted)} files deleted — exceeds auto-merge threshold ({MAX_DELETIONS})")
    elif deleted:
        print(f"✓ {len(deleted)} deletion(s), within threshold")

    if failures:
        print("\nGATE: FAIL")
        for f in failures:
            print(" - " + f)
        return 1
    print("\nGATE: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
