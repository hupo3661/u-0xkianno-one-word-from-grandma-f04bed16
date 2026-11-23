#!/usr/bin/env python3
"""Write one word -- the word a grandma would text about AI -- to entry.txt.

The word is "knowitall": the gentle, slightly baffled label a grandma gives
the machine that seems to know everything. One word, nine characters,
lowercase the way she would type it. Standard library only, no network,
no input files.
"""

import os

WORD = "knowitall"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
