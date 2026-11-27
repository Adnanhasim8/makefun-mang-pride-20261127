#!/usr/bin/env python3
"""One Line of Earned Pride — u-mang-one-line-of-earned-pride-a0138557.

Writes a single line (1-200 characters) of earned pride to /output/entry.txt.
Python 3.13 standard library only, no network at run time.

The line: a grandfather's mango tree, planted the year the narrator was born,
bears its first fruit a lifetime later — the harvest is the pride, earned
inside the line and never explained.
"""

import argparse
import os
import sys

ENTRY = (
    "Grandad planted the mango tree the year I was born; "
    "this summer we picked its first fruit together, under its shade."
)

# Gate: the entry must be exactly one line of 1-200 characters, non-empty.
assert ENTRY and not ENTRY.isspace(), "entry must be non-empty"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be exactly one line"
assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write one line of earned pride.")
    parser.add_argument(
        "--out",
        default=None,
        help="Output file (default: $MAKEFUN_OUTPUT_DIR/entry.txt or /output/entry.txt)",
    )
    args = parser.parse_args(argv)

    if args.out:
        out_path = args.out
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        out_path = os.path.join(out_dir, "entry.txt")

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Gate check on what was actually written.
    with open(out_path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written output differs from ENTRY"
    assert 1 <= len(written) <= 200, "written output must be 1-200 chars"
    return 0


if __name__ == "__main__":
    sys.exit(main())
