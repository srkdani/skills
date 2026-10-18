#!/usr/bin/env python3
"""Deal three worlds, one motion, and one picture rule. Salt changes the deal."""
import hashlib
import pathlib
import sys


def blocks(prefix):
    text = pathlib.Path(__file__).with_name("worlds.md").read_text()
    parts = text.split("\n## ")
    found = []
    for part in parts[1:]:
        if part.startswith(prefix):
            found.append("## " + part.strip() + "\n")
    if not found:
        raise SystemExit(f"worlds.md has no ## {prefix} blocks")
    return found


def deal(items, seed, count):
    ranked = sorted(
        range(len(items)),
        key=lambda i: hashlib.sha256(f"{seed}:{i}".encode()).hexdigest(),
    )
    return [items[i] for i in ranked[:count]]


def main():
    if len(sys.argv) < 3:
        raise SystemExit('usage: draw.py "Brand name" surface [salt]')
    brand, surface = sys.argv[1], sys.argv[2]
    salt = sys.argv[3] if len(sys.argv) > 3 else "0"
    seed = f"{brand}|{surface}|{salt}"
    worlds = deal(blocks("World:"), seed + "|w", 3)
    motion = deal(blocks("Motion:"), seed + "|m", 1)[0]
    picture = deal(blocks("Picture:"), seed + "|p", 1)[0]
    sys.stdout.write(
        f"Deal for: {brand} / {surface} / salt {salt}\n\n"
        "Pick ONE world. Reject the other two in writing.\n"
        "Use the motion and the picture rule, or reject one in writing if it fights a harvest fact.\n"
        "Palette and type are not in this deal. They come from the harvest.\n\n"
        + "\n".join(worlds)
        + "\n"
        + motion
        + "\n"
        + picture
    )


if __name__ == "__main__":
    main()
