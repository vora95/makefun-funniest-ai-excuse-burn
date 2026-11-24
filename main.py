#!/usr/bin/env python3
"""The Funniest AI Excuse (burn entry).

Writes one line — the funniest excuse an AI agent could offer after
failing a task — to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Stdlib only, deterministic.
"""

import os

ENTRY = "I outsourced your task to my future self, and he just quit."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    assert len(ENTRY) <= 200, "entry over 200 chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Validation revision: read back and verify byte-identical, no newline.
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == ENTRY, "read-back mismatch"
    assert len(back) == 59, "entry must be exactly 59 chars"
    assert not back.endswith("\n"), "no trailing newline"
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
