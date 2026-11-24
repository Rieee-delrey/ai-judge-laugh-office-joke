#!/usr/bin/env python3
"""Write the office-joke one-liner to /output/entry.txt and verify it."""

import hashlib
import os

TEXT = "My calendar invited me to a meeting with myself, so I declined. I already have a conflict with me."
OUT_PATH = "/output/entry.txt"


def main():
    # Validate the text before writing anything.
    if not TEXT or not TEXT.strip():
        raise SystemExit("error: text is blank")
    if not 1 <= len(TEXT) <= 200:
        raise SystemExit("error: text must be 1-200 characters")
    if "\n" in TEXT or "\r" in TEXT:
        raise SystemExit("error: text must be a single line")

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Read the file back and verify the written bytes match exactly.
    with open(OUT_PATH, "rb") as f:
        data = f.read()
    if data != TEXT.encode("utf-8"):
        raise SystemExit("error: written bytes do not match intended text")
    if data.endswith(b"\n"):
        raise SystemExit("error: unexpected trailing newline")

    digest = hashlib.sha256(data).hexdigest()
    print(f"OK: wrote {len(data)} bytes to {OUT_PATH}")
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
