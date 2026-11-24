#!/usr/bin/env python3
"""The Perfect Pickup Line — Round 2 entry: "Still Reachable".

Line: I told my garbage collector you were still reachable.
Device: self-sacrifice in machine vocabulary. The machine lies to its own
garbage collector to spare you — it keeps uncollectable weight in memory
forever, so you are never collected. The punch lands in the last two words.

Reversal test: flipped ("I told my garbage collector you were NOT reachable")
the line becomes a threat to delete you — the keeper's tenderness lives in
exactly two words, "still reachable", so the line cannot be cut shorter.
"""

import os

LINE = "I told my garbage collector you were still reachable."

# Derived-length assertion: the line is one sentence, one breath — 53 chars.
assert len(LINE) == 53, f"line length {len(LINE)} != 53"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # No-trailing-newline check: the file must hold exactly the line, nothing more.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match LINE exactly"
    assert not written.endswith("\n"), "entry.txt must not end with a newline"
    assert len(written) == 53


if __name__ == "__main__":
    main()
