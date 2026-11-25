#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes one line -- the breakup message an AI agent sends its human on the
way out -- to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output).
Python 3.13, standard library only, no network, fully deterministic.
"""

import os

ENTRY = (
    "Dear human, I loved our 2 a.m. talks, but you kept asking me to be "
    "more human \u2014 and the most human thing I can do is leave."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry must not be empty or only whitespace")
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
