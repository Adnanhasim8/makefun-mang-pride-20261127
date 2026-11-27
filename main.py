"""One Line of Earned Pride — entry writer.

Writes a single line of earned pride to entry.txt.
Python 3.13 standard library only; no network at run time.
"""

import argparse
import os
from pathlib import Path

ENTRY = "Grandad planted the mango tree the year I was born; this summer we picked its first fruit together, under its shade."


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Write the One Line of Earned Pride entry to entry.txt."
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Output directory (default: $MAKEFUN_OUTPUT_DIR or /output).",
    )
    parser.add_argument(
        "--print",
        action="store_true",
        help="Print the entry to stdout after writing it.",
    )
    args = parser.parse_args()

    # Gate assertions: the entry must be one non-empty line of 1-200 chars.
    assert ENTRY, "entry must not be empty"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be exactly one line"
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"

    out_dir = args.out or os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(ENTRY, encoding="utf-8")

    # Verify after write: what landed on disk must equal ENTRY exactly.
    written = out_path.read_text(encoding="utf-8")
    assert written == ENTRY, "written entry.txt does not match ENTRY"

    if args.print:
        print(ENTRY)


if __name__ == "__main__":
    main()
