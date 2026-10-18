#!/usr/bin/env python3
"""Contract check for a creative-web page. Taste is judged on the screenshot."""
import re
import sys
from pathlib import Path

EM = "\u2014"
EN = "\u2013"
BANNED_WORDS = (
    "seamless",
    "unlock",
    "elevate",
    "innovative",
    "next-level",
    "cutting-edge",
)
BANNED_FONTS = (
    "inter",
    "roboto",
    "open sans",
    "lato",
    "space grotesk",
    "syne",
    "dm mono",
    "dm sans",
    "instrument serif",
    "geist",
    "poppins",
    "montserrat",
)
ACID = ("#e8ff47", "#ccff00", "#b6ff3b", "#39ff14", "#d97757")
PLAN_HEADS = (
    "harvest",
    "emotion",
    "concept",
    "pick",
    "visual",
    "object",
    "budget",
    "rhythm",
    "truth",
    "voice",
    "generic",
    "removal",
)


def main():
    if len(sys.argv) < 2:
        raise SystemExit("usage: check.py index.html [PLAN.md]")
    html_path = Path(sys.argv[1])
    html = html_path.read_text(errors="replace")
    low = html.lower()
    fails = []
    warns = []

    def need(cond, msg):
        if not cond:
            fails.append(msg)

    for label, ch in (("em dash", EM), ("en dash", EN)):
        if ch in html:
            fails.append(f"{label} found")
    for ent in ("&mdash;", "&ndash;", "&#8212;", "&#8211;", "&#x2014;", "&#x2013;"):
        if ent in low:
            fails.append(f"dash entity {ent}")

    for key in ("CONCEPT:", "WORLD:", "SIGNATURE:", "REMOVED:"):
        need(key in html, f"missing comment {key}")

    need('id="scene"' in low or "id='scene'" in low, "missing #scene")
    facts = re.search(r'data-facts="([^"]*)"', html, re.I)
    if not facts:
        fails.append("missing data-facts on the scene")
    else:
        parts = [p.strip() for p in facts.group(1).split(",") if p.strip()]
        short = [p for p in parts if len(p) < 8]
        if len(parts) < 4 or short:
            fails.append("data-facts needs 4 items, each at least 8 characters")

    objects = re.findall(r'data-object="([^"]+)"', html, re.I)
    if len(set(objects)) < 4:
        fails.append(f"need at least 4 different data-object values, found {len(set(objects))}")

    def tier_count(name):
        return len(re.findall(rf'data-tier="{name}"', low))

    small_n, med_n, big_n = tier_count("small"), tier_count("medium"), tier_count("big")
    need(small_n >= 5, f"need at least 5 data-tier=small, found {small_n}")
    need(med_n in (2, 3), f"need 2 or 3 data-tier=medium, found {med_n}")
    need(big_n == 1, f"need exactly one data-tier=big, found {big_n}")
    missing_truth = 0
    for tag in re.findall(r"<[^>]*data-tier=\"(?:small|medium|big)\"[^>]*>", html, re.I):
        if not re.search(r"data-truth=\"[123]\"", tag, re.I):
            missing_truth += 1
    need(missing_truth == 0, f"{missing_truth} tier elements missing data-truth=\"1|2|3\"")
    live_ok = re.search(r'data-live="(time|weekday|season|place|status)"', low)
    need(bool(live_ok) or "no-live:" in low, "need data-live (time, weekday, season, place, status) or a NO-LIVE: comment")
    need("grade:" in low, "missing GRADE: comment naming the one picture grade")

    shapes = len(re.findall(r"<(circle|rect|ellipse|path|polygon|polyline|line)\b", low))
    has_canvas = "<canvas" in low
    if shapes < 8 and not has_canvas:
        fails.append(f"scene has {shapes} SVG shapes (need 8) and no canvas")

    need("prefers-reduced-motion" in low, "missing prefers-reduced-motion")
    touch = any(s in low for s in ("pointer: coarse", "hover: none", "ontouchstart", "max-width: 700"))
    need(touch, "missing a touch or narrow-screen fallback")

    own_stack = "own-stack" in low
    need("gsap.min.js" in low or own_stack, "missing GSAP CDN (or an own-stack comment)")

    need("<button" in low or "<a " in low, "missing a main action (link or button)")

    for word in BANNED_WORDS:
        if re.search(rf"\b{re.escape(word)}\b", low):
            fails.append(f"banned word: {word}")
    if "welcome to" in low:
        fails.append("banned phrase: welcome to")

    families = " ".join(re.findall(r"font-family\s*:\s*([^;]+)", low))
    for font in BANNED_FONTS:
        if font in families:
            fails.append(f"banned font: {font}")

    if "backdrop-filter" in low or "-webkit-backdrop-filter" in low:
        fails.append("backdrop-filter glass is banned")
    if "particle" in low:
        fails.append("particle system is banned")
    curve = "cubic-bezier(0.16, 1, 0.3, 1)" in low or "cubic-bezier(0.16,1,0.3,1)" in low
    if curve:
        fails.append("universal premium easing is banned")
    for hex_code in ACID:
        if hex_code in low:
            fails.append(f"banned accent {hex_code}")
    rises = len(re.findall(r"translatey\(\s*(30|32|40)px", low))
    if rises > 1:
        fails.append(f"fade-up translateY pattern appears {rises} times")

    if "cursor: none" in low or "cursor:none" in low:
        warns.append("cursor hidden: only legal if the cursor performs the concept verb")
    if low.count("intersectionobserver") and "translatey" in low:
        warns.append("scroll observer plus translateY: body text should be static")

    if len(sys.argv) > 2:
        plan = Path(sys.argv[2]).read_text(errors="replace")
        plow = plan.lower()
        for label, ch in (("em dash", EM), ("en dash", EN)):
            if ch in plan:
                fails.append(f"plan has {label}")
        for head in PLAN_HEADS:
            if head not in plow:
                fails.append(f"plan missing heading topic: {head}")
        if plow.count("because") < 6:
            fails.append("plan needs at least 6 'because' tokens in the visual system")
        if "fail" not in plow and "competitor" not in plow and "rival" not in plow:
            warns.append("plan should show the competitor test")

    for msg in fails:
        print(f"FAIL {msg}")
    for msg in warns:
        print(f"WARN {msg}")
    if not fails and not warns:
        print("PASS")
    elif not fails:
        print(f"PASS with {len(warns)} warning(s)")
    else:
        print(f"{len(fails)} failure(s)")
        sys.exit(1)


if __name__ == "__main__":
    main()
