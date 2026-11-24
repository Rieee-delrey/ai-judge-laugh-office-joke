#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open — one-line office joke entry.

Writes the winning one-line office joke to /output/entry.txt.
The joke: a calendar invite to a meeting with yourself, declined because
you already have a conflict with yourself — the word "conflict" flips from
scheduling to therapy in the final three words.
"""
import os

LINE = "My calendar invited me to a meeting with myself, so I declined. I already have a conflict with me."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: the entry must be exactly the line, no trailing newline.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the winning line"
    assert 1 <= len(written) <= 200, "entry outside the 1-200 character gate"
    print(f"Wrote {len(written)} characters to /output/entry.txt")

if __name__ == "__main__":
    main()
