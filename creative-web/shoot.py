#!/usr/bin/env python3
"""First viewport, full page, and a short scroll capture.

Usage: python3 shoot.py path/to/index.html outdir
Writes hero-1440.png, full-1440.png, hero-390.png, full-390.png, scroll.webm
"""
import shutil
import subprocess
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


def launch(p):
    args = ["--no-sandbox", "--disable-dev-shm-usage"]
    try:
        return p.chromium.launch(channel="chrome", args=args)
    except Exception:
        return p.chromium.launch(args=args)


def shoot(html, outdir):
    out = Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    url = Path(html).resolve().as_uri()
    with sync_playwright() as p:
        browser = launch(p)
        for width, height, name in ((1440, 900, "1440"), (390, 844, "390")):
            page = browser.new_page(viewport={"width": width, "height": height})
            page.goto(url, wait_until="load", timeout=20000)
            page.wait_for_timeout(600)
            page.screenshot(path=str(out / f"hero-{name}.png"))
            page.screenshot(path=str(out / f"full-{name}.png"), full_page=True)
            page.close()

        frames = out / "_frames"
        if frames.exists():
            shutil.rmtree(frames)
        frames.mkdir()
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(url, wait_until="load", timeout=20000)
        page.wait_for_timeout(200)
        index = 0

        def grab():
            nonlocal index
            page.screenshot(path=str(frames / f"f{index:03d}.jpg"), type="jpeg", quality=70)
            index += 1

        for step in range(8):
            page.mouse.move(140 + step * 140, 420)
            grab()
        for _ in range(42):
            page.mouse.wheel(0, 200)
            page.wait_for_timeout(160)
            grab()
        page.close()
        browser.close()

    dest = out / "scroll.webm"
    subprocess.run(
        [
            "ffmpeg", "-y",
            "-framerate", "5",
            "-i", str(frames / "f%03d.jpg"),
            "-t", "10",
            "-an",
            "-c:v", "libvpx-vp9",
            "-crf", "36",
            "-b:v", "0",
            "-vf", "scale=1280:-2",
            str(dest),
        ],
        check=True,
        capture_output=True,
    )
    shutil.rmtree(frames, ignore_errors=True)
    print(dest)


def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: shoot.py index.html outdir")
    shoot(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
