#!/usr/bin/env python3
"""One Line, Big Laugh — make.fun bounty u-coral-404-one-line-big-laugh-328fb857.

Writes a single funny line (at most 200 characters) to entry.txt.
Fully deterministic: the same fixed line is written on every run,
with no randomness, no clock, no network and no environment input.
"""

import os
import sys

# The entry: one line, 130 characters, no setup or explanation around it.
# Tightened in revision 1: dropped "for the" and swapped the flat
# "paused" for "went silent", so the whisper lands harder.
ENTRY = (
    "I asked my smart speaker the meaning of life. "
    "It went silent, then whispered: 'Have you tried turning "
    "yourself off and on again?'"
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the bounty gate before anything is written.

    The gate requires /output/entry.txt to be UTF-8 text of 1 to 200
    characters, not only white space. A single line means no newline
    may appear inside the text either.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} characters, must be 1-{MAX_CHARS}")
    if text.strip() == "":
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def sha256_hex(data: bytes) -> str:
    import hashlib

    return hashlib.sha256(data).hexdigest()


def main() -> int:
    validate(ENTRY)
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    written = open(path, "rb").read()
    print(f"Wrote {len(ENTRY)} characters to {path}")
    print(f"sha256: {sha256_hex(written)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
