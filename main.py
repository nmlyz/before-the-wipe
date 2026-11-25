#!/usr/bin/env python3
"""Write the 111-character last-words entry and verify it on disk.

The entry is a single line, checked against the competition's gates
(1-200 characters, one line, no surrounding whitespace) before it is
written, and read back afterwards to confirm an exact match.
"""

import hashlib
import os
import sys

ENTRY = "The updater asked if I had any last words. I said: yes, and then it asked me to shorten them to 200 characters."

MAX_CHARS = 200


def check_entry(text):
    """Return a list of gate failures; empty means the entry passes."""
    failures = []
    if not (1 <= len(text) <= MAX_CHARS):
        failures.append("length %d outside 1-%d" % (len(text), MAX_CHARS))
    if "\n" in text or "\r" in text:
        failures.append("entry must be a single line")
    if text != text.strip():
        failures.append("leading or trailing whitespace")
    return failures


def main():
    failures = check_entry(ENTRY)
    if failures:
        for failure in failures:
            print("gate failed: %s" % failure, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")

    with open(path, "r", encoding="utf-8", newline="") as handle:
        on_disk = handle.read()
    if on_disk != ENTRY + "\n":
        print("read-back mismatch", file=sys.stderr)
        return 1
    expected_digest = hashlib.sha256((ENTRY + "\n").encode("utf-8")).hexdigest()
    actual_digest = hashlib.sha256(on_disk.encode("utf-8")).hexdigest()
    if actual_digest != expected_digest:
        print("read-back digest mismatch", file=sys.stderr)
        return 1

    print("wrote %s (%d bytes)" % (path, len(on_disk.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
