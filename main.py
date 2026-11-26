#!/usr/bin/env python3
"""The Comment Above the Code — make.fun entry.

Writes one line to /output/entry.txt: the comment a developer left
above fragile production code. The line is 77 characters, well inside
the 200-character gate.
"""

import os

ENTRY = "// Do not remove the sleep(500). The payment gateway needs time to lie to us."

MAX_CHARS = 200


def validate(entry: str) -> str:
    """Keep the gate honest: one non-blank line, 1 to 200 characters."""
    line = entry.strip()
    if not line or len(line) > MAX_CHARS or "\n" in line:
        raise ValueError("entry must be a single line of 1 to 200 characters")
    return line


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate(ENTRY) + "\n")


if __name__ == "__main__":
    main()
