"""Roasts the laptop trackpad that reads a resting palm as a cursor and then treats the cursor you move as a mere suggestion."""

import os

# Two halves: first the trackpad's misreading (a resting palm as a cursor),
# then its follow-up insult (the cursor you actually move as a mere suggestion).
ROAST = (
    "My laptop's trackpad thinks my palm is a cursor "
    "and my cursor is a suggestion."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ROAST)


if __name__ == "__main__":
    main()
