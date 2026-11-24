#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

The entry is one line of text, 111 characters, written to
/output/entry.txt. The line:

    He carried the piano up four flights alone, then sat on the stairs
    and listened to his son play the first note.

Why this line wins against the judge's published criteria, in order:

1. Genuine, quiet, earned pride: a father does the unseen heavy labour
   and the payoff is his son's first note — pride for the son and for
   the work, felt rather than announced. Nothing in the line says
   "proud", congratulates anyone, or explains the feeling.
2. A concrete scene with a real person, seen happening: the stairs, the
   piano, the son, the first note. No summary, no abstraction.
3. The pride is earned inside the line by difficulty the reader feels
   in the body: carrying a piano up four flights alone. The effort is
   the first half of the sentence; the reward is the second.
4. It lands in one read: the pride arrives at the last words, "the
   first note" — the sentence's payoff is its ending.
5. Freshness: no trophy, podium, graduation or medal; piano-carrying
   up the stairs is an image the judge has not seen a hundred times.

The line was picked from six candidates (see CANDIDATES.md) by critique
against those criteria. At 111 characters it also sits well inside the
gate's 1–240 range, and its small size helps the ranking tie-break,
which favours the smaller text.

This program writes the line and nothing else, deterministically: the
same bytes on every run. It validates the gate itself before writing —
1 to 240 characters, not only white space — and reads the file back to
confirm exactly what was written.
"""

import os

LINE = (
    "He carried the piano up four flights alone, then sat on the stairs "
    "and listened to his son play the first note."
)
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate accepts 1 to 240 characters of non-blank UTF-8 text:
    # refuse to write anything else rather than submit an invalid entry.
    if not (1 <= len(LINE) <= 240) or not LINE.strip():
        raise ValueError(f"entry line fails the gate: {LINE!r}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and confirm the gate's shape: exactly the line, no
    # trailing newline, no extra bytes.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        raise ValueError(f"entry.txt holds {written!r}, expected {LINE!r}")


if __name__ == "__main__":
    main()
