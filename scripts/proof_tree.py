#!/usr/bin/env python3
"""Inspect the structured proof tree without third-party dependencies.

This tool checks repository organization and Markdown links. It deliberately
does not claim that any mathematical statement has been proved.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROOF_ROOT = ROOT / "docs" / "proofs" / "exact-lift"

REQUIRED_FILES = (
    ROOT / "AGENTS.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "README.md",
    ROOT / "pyproject.toml",
    ROOT / "uv.lock",
    ROOT / "scripts" / "exact-lift" / "a2-only" / "check_a2_151.py",
    ROOT / "scripts" / "exact-lift" / "a2-only" / "check_a2_decimal_ellipse_phase.py",
    ROOT / "scripts" / "exact-lift" / "a2-only" / "check_a2_endpoint_lattice.py",
    ROOT / "scripts" / "exact-lift" / "a1-only" / "check_a1_top_diag_k1.py",
    ROOT / "scripts" / "exact-lift" / "a1-only" / "check_a1_top_diag_k2.py",
    *(ROOT / "scripts" / "exact-lift" / "double-deficit" / f"check_dd_{n}.py" for n in range(2710, 2729)),
    ROOT / "scripts" / "exact-lift" / "double-deficit" / "check_dd_2729.py",
    ROOT / "scripts" / "exact-lift" / "double-deficit" / "check_dd_2729.cpp",
    ROOT / "scripts" / "exact-lift" / "double-deficit" / "check_dd_2730.cpp",
    ROOT / "scripts" / "exact-lift" / "double-deficit" / "check_dd_2731.cpp",
    ROOT / "scripts" / "exact-lift" / "double-deficit" / "check_dd_2732.cpp",
    ROOT / "scripts" / "exact-lift" / "double-deficit" / "check_dd_2733.cpp",
    PROOF_ROOT / "README.md",
    PROOF_ROOT / "problem-and-carrier.md",
    PROOF_ROOT / "global-framework.md",
    PROOF_ROOT / "branches" / "a2-only" / "README.md",
    PROOF_ROOT / "branches" / "a2-only" / "core.md",
    PROOF_ROOT / "branches" / "a2-only" / "phase-and-defect.md",
    PROOF_ROOT / "branches" / "a2-only" / "hensel.md",
    PROOF_ROOT / "branches" / "a2-only" / "endpoint-lattice.md",
    PROOF_ROOT / "branches" / "double-deficit" / "README.md",
    PROOF_ROOT / "branches" / "double-deficit" / "core.md",
    PROOF_ROOT / "branches" / "double-deficit" / "frontier.md",
    PROOF_ROOT / "branches" / "a1-only" / "README.md",
    PROOF_ROOT / "branches" / "a1-only" / "core.md",
    PROOF_ROOT / "branches" / "a1-only" / "rational-contact.md",
    PROOF_ROOT / "branches" / "a1-only" / "top-layer.md",
    PROOF_ROOT / "branches" / "a1-only" / "diagonal.md",
    PROOF_ROOT / "status.md",
    PROOF_ROOT / "notation.md",
    PROOF_ROOT / "dependency-map.md",
    PROOF_ROOT / "conclusion.md",
    PROOF_ROOT / "claim-template.md",
    PROOF_ROOT / "archive" / "exact_lift_research_synthesis_2026-08-10.md",
)

SECTION_MARKERS = {
    PROOF_ROOT / "problem-and-carrier.md": ("# 1. ", "# 2. "),
    PROOF_ROOT / "global-framework.md": tuple(f"# {n}. " for n in range(3, 12)),
    PROOF_ROOT / "branches" / "a2-only" / "core.md": tuple(f"# {n}. " for n in range(12, 17)),
    PROOF_ROOT / "branches" / "double-deficit" / "core.md": tuple(
        f"# {n}. " for n in range(17, 28)
    ),
    PROOF_ROOT / "branches" / "a1-only" / "core.md": tuple(f"# {n}. " for n in range(28, 32)),
    PROOF_ROOT / "status.md": tuple(f"# {n}. " for n in range(32, 40)),
    PROOF_ROOT / "notation.md": ("# 40. ", "# 41. "),
    PROOF_ROOT / "dependency-map.md": ("# 42. ",),
    PROOF_ROOT / "conclusion.md": ("# 43. ",),
}

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_files() -> list[str]:
    return [f"missing required file: {path.relative_to(ROOT)}" for path in REQUIRED_FILES if not path.is_file()]


def check_sections() -> list[str]:
    errors: list[str] = []
    for path, markers in SECTION_MARKERS.items():
        if not path.is_file():
            continue
        content = read(path)
        missing = [marker.rstrip() for marker in markers if marker not in content]
        if missing:
            errors.append(f"{path.relative_to(ROOT)} missing section(s): {', '.join(missing)}")
    return errors


def check_links() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or ".venv" in path.parts:
            continue
        for target in MARKDOWN_LINK.findall(read(path)):
            target = target.strip().split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)} links outside repository: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)} has broken link: {target}")
    return errors


def check_status() -> list[str]:
    path = PROOF_ROOT / "status.md"
    if not path.is_file():
        return []
    content = read(path)
    required_phrases = (
        "主不存在性命题尚未完成证明",
        "A_2",
        "DD",
        "A_1",
        "有限",
    )
    return [f"status.md missing status phrase: {phrase}" for phrase in required_phrases if phrase not in content]


def proof_files() -> list[Path]:
    return sorted(PROOF_ROOT.rglob("*.md"))


def list_tree() -> int:
    print(f"Proof tree: {PROOF_ROOT.relative_to(ROOT)}/")
    for path in proof_files():
        print(f"- {path.relative_to(ROOT)} ({len(read(path).splitlines())} lines)")
    return 0


def check_tree() -> int:
    errors = check_files() + check_sections() + check_links() + check_status()
    if errors:
        print("Proof tree check: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Proof tree check: OK")
    print(f"- structured Markdown files: {len(proof_files())}")
    print("- mathematical status: main nonexistence theorem remains open")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("list", "check"), nargs="?", default="check")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == "list":
        return list_tree()
    return check_tree()


if __name__ == "__main__":
    sys.exit(main())
