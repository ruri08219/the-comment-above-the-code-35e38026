#!/usr/bin/env python3
"""The Comment Above the Code — make.fun entry.

Writes one line to /output/entry.txt: the comment a developer left
above fragile production code. The line is 77 characters, well inside
the 200-character gate.
"""

import os

ENTRY = "// Do not remove the sleep(500). The payment gateway needs time to lie to us."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
