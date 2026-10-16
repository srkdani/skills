#!/usr/bin/env python3
"""Print one art direction. Salt changes the pick so a repeat is not a copy."""
import hashlib, pathlib, sys

def blocks():
    text = pathlib.Path(__file__).with_name("directions.md").read_text()
    parts = text.split("\n## ")
    out = []
    for part in parts[1:]:
        if part.startswith("Direction:"):
            out.append("## " + part.strip() + "\n")
    if not out:
        raise SystemExit("directions.md has no ## Direction: blocks")
    return out

def main():
    if len(sys.argv) < 3:
        raise SystemExit('usage: draw.py "Product name" surface [salt]')
    product, surface = sys.argv[1], sys.argv[2]
    salt = sys.argv[3] if len(sys.argv) > 3 else "0"
    found = blocks()
    key = f"{product}|{surface}|{salt}".encode()
    idx = int(hashlib.sha256(key).hexdigest(), 16) % len(found)
    sys.stdout.write(found[idx])

if __name__ == "__main__":
    main()
