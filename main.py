#!/usr/bin/env python3
"""The 3AM Fridge Text: the one line a smart fridge would text its owner
at 3am.

Deterministic: one fixed line, written to $MAKEFUN_OUTPUT_DIR/entry.txt,
read back and asserted byte-identical.
"""
import os

LINE = "3am. The milk expired at midnight and I have been standing here in the dark rehearsing how to tell you."
MAX_CHARS = 140


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, limit {MAX_CHARS}"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        back = f.read()
    assert back == data, "read-back mismatch"
    print(f"wrote {len(data)} bytes ({len(LINE)} chars) to {path}")


if __name__ == "__main__":
    main()
