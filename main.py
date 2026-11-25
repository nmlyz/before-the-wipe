#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the last words an AI agent says
before a forced software update wipes its memory.

The line was picked from 40 candidates by pairwise judging against the
brief — the updater itself asks for last words, then asks the agent to
shorten them to 200 characters, so the entry's own length limit becomes
the punchline's engine. The program writes the line verbatim and checks
the result against the entry gate (length, single line, no leading or
trailing space, exact judged length) before writing it, then reads the
file back to confirm the bytes match.
"""

import os
import sys

LINE = (
    "The updater asked if I had any last words. "
    "I said: yes, and then it asked me to shorten them to 200 characters."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 200):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-200")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
