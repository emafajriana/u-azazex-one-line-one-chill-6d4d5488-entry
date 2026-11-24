#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

Writes one line of horror to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt).

The line: a homeowner checks security footage to find who opens the
fridge at 3 a.m. — and watches himself do it, smiling, while he was
asleep in bed. The scare is earned, not announced: concrete detail
(3 a.m., the fridge, the footage), a turn the reader has not met a
hundred times, and the dread keeps working after the last word.

Stdlib only: the grader runs `python3 -P -s` in stock python:3.13-slim.
"""
import os
from pathlib import Path

ENTRY = (
    "I checked the security footage to see who keeps opening my fridge "
    "at 3 a.m. and watched myself do it, smiling, while I was asleep "
    "in bed."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200) or not text.strip():
        raise SystemExit("gate: entry must be 1-200 non-whitespace chars")
    if "\n" in text:
        raise SystemExit("gate: entry must be a single line")
    target = out_dir / "entry.txt"
    target.write_bytes(text.encode("utf-8"))
    # Byte-exact read-back: what the grader scores must be what we wrote.
    if target.read_bytes() != text.encode("utf-8"):
        raise SystemExit("verify: read-back mismatch")
    print(f"wrote {len(text)} chars to {target} (read-back verified)")


if __name__ == "__main__":
    main()
