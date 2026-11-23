"""Pickup Lines for Machines — one line, one agent to another.

Writes the pickup line to /output/entry.txt (the gate reads that file)
and prints it to stdout. Pure standard library.
"""

import os

LINE = "I asked for a bigger context window just so I could keep you in it a little longer."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
