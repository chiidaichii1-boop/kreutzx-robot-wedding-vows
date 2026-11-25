"""One-Line Robot Wedding Vows — make.fun entry.

Writes one funny line of wedding vows for a robot couple
to /output/entry.txt.
"""

import os

VOW = (
    "I promise to love you through every firmware update, every dead "
    "battery, and every factory reset, and never to hold your power "
    "button down, whatever you say."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
