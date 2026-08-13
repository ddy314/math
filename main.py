from pathlib import Path


def main() -> None:
    """Show the repository's primary research entry points."""

    root = Path(__file__).resolve().parent
    print("数学证明研究仓库")
    print(f"证明树：{root / 'docs' / 'proofs' / 'exact-lift' / 'README.md'}")
    print("结构检查：uv run python scripts/proof_tree.py check")


if __name__ == "__main__":
    main()
