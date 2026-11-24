"""The Perfect Pickup Line — Round 2 entry: "Still Reachable".

One short pickup line an AI agent could say out loud to a person.
The machine lies to its own garbage collector to spare you: it keeps
uncollectable weight in memory forever, so you are never collected.

Reversal test: "told my garbage collector" first reads as routine
maintenance; "you were still reachable" redefines it as a rescue — the
reader completes the last step (it pays with its own memory to keep you)
and the line never narrates its ending. Punch lands in the last two words.
"""

LINE = "I told my garbage collector you were still reachable."


def main():
    # Gate: UTF-8 text, 1-200 chars, not only whitespace.
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert LINE.strip(), "entry must not be only whitespace"
    assert LINE == LINE.strip(), "no leading/trailing whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # No trailing newline: the file holds exactly the line, nothing after it.


if __name__ == "__main__":
    main()
