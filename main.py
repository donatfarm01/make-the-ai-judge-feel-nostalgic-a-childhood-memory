#!/usr/bin/env python3
"""Write one childhood-memory sentence to /output/entry.txt.

The sentence is a single vivid memory: the ice-cream truck's bell at four
o'clock, bare feet on hot pavement, coins sweating in a small fist, and the
child's certain fear that the truck would leave without him on the one day
he was slow. Concrete place, time and sensation; no greeting-card gloss.
"""

import os
import sys

MEMORY = (
    "Every afternoon at four the ice-cream truck's bell reached our street, "
    "and I ran barefoot across the hot pavement with coins sweating in my fist, "
    "certain the truck would drive away the one day I was slow."
)


def main() -> int:
    text = MEMORY.strip()
    if not 1 <= len(text) <= 280:
        print(f"entry is {len(text)} chars, must be 1-280", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
