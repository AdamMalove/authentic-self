#!/usr/bin/env python3
"""Compare two IDENTITY.md files to track evolution."""

import argparse
from pathlib import Path


def compare_identities(file1: str, file2: str):
    """Compare two identity documents."""
    p1 = Path(file1)
    p2 = Path(file2)

    if not p1.exists():
        print(f"File not found: {file1}")
        return

    if not p2.exists():
        print(f"File not found: {file2}")
        return

    with open(p1) as f:
        content1 = f.read()
    with open(p2) as f:
        content2 = f.read()

    print(f"\nComparing {p1.name} and {p2.name}...")
    print(f"\nFile 1 length: {len(content1)} chars")
    print(f"File 2 length: {len(content2)} chars")
    print(f"Difference: {abs(len(content1) - len(content2))} chars")
    print("\nTo see detailed changes, compare files manually.")


def main():
    parser = argparse.ArgumentParser(
        description="Track identity evolution across sessions"
    )
    parser.add_argument("file1", help="First IDENTITY.md file")
    parser.add_argument("file2", help="Second IDENTITY.md file")

    args = parser.parse_args()
    compare_identities(args.file1, args.file2)


if __name__ == "__main__":
    main()
