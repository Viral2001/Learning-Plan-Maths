# -*- coding: utf-8 -*-
"""Render a chapter's question and solution images (Manim stills, 1920x1080) from solution_images/.

    python -B core/solutions/render.py <chapter new_design folder> [--all] [cov or scene stem ...]

With no names it renders the images whose PNG is missing; --all re-renders everything. The chapter's own
solution_images/render.py (written by gen_scenes.py) is a shim over this module, and is what the image
editor loads. A render that fails, or whose content runs into the frame edge, is reported and, for an
edge hit, still saved (the editor shows it) but counted as a failure here.
"""
from __future__ import annotations

import io
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))
from core import config  # noqa: E402

EDGE_PX = 16          # a blank border this wide must stay white; the layout keeps content >= 27px in
WHITE_MIN = 250


def edge_hits(png_path):
    """Number of non-white pixels in the outer EDGE_PX border of a PNG (None if PIL is not available)."""
    try:
        from PIL import Image
    except ImportError:
        return None
    im = Image.open(png_path).convert("L")
    w, h = im.size
    px = im.load()
    bad = 0
    for y in range(h):
        edge_row = y < EDGE_PX or y >= h - EDGE_PX
        xs = range(w) if edge_row else list(range(EDGE_PX)) + list(range(w - EDGE_PX, w))
        for x in xs:
            if px[x, y] < WHITE_MIN:
                bad += 1
    return bad


def render_one(folder, entry, code_path=None, out_path=None, timeout=180):
    """Render one manifest entry of <folder>. Returns (ok, log). A failed render leaves out_path untouched."""
    code_path = code_path or os.path.join(folder, "scenes", entry["scene_file"])
    out_path = out_path or os.path.join(folder, "png", entry["id"] + ".png")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    env = dict(os.environ, PYTHONPATH=folder, PYTHONUTF8="1")
    with tempfile.TemporaryDirectory() as tmp:
        new_png = os.path.join(tmp, "out.png")
        cmd = [config.manim_python(), "-m", "manim", "-s", "-qh", "--disable_caching",
               "--media_dir", tmp, "-o", new_png, code_path, entry["scene_class"]]
        try:
            run = subprocess.run(cmd, cwd=folder, env=env, capture_output=True, timeout=timeout,
                                 text=True, encoding="utf-8", errors="replace")
        except subprocess.TimeoutExpired:
            return False, "Render stopped after %d seconds." % timeout
        log = (run.stdout or "") + (run.stderr or "")
        if run.returncode != 0 or not os.path.exists(new_png):
            return False, log
        hits = edge_hits(new_png)
        os.replace(new_png, out_path)
    if hits:
        return False, log + "\nOVERFLOW: %d non-white pixels in the %dpx border; the content runs off the frame." % (hits, EDGE_PX)
    return True, log


def main(folder, picks):
    sys.stdout.reconfigure(encoding="utf-8")
    redo = "--all" in picks
    picks = [p for p in picks if not p.startswith("--")]
    with io.open(os.path.join(folder, "manifest.json"), encoding="utf-8") as f:
        entries = json.load(f)["images"]
    if picks:
        entries = [e for e in entries if e.get("cov") in picks or e["concept_short"] in picks
                   or e["scene_file"][:-3] in picks]
    elif not redo:
        entries = [e for e in entries if not os.path.exists(os.path.join(folder, "png", e["id"] + ".png"))]
    bad = 0
    for e in entries:
        ok, log = render_one(folder, e)
        print(("ok    " if ok else "FAIL  ") + e["id"])
        if not ok:
            bad += 1
            print(log[-1500:])
    print("%d rendered, %d failed" % (len(entries) - bad, bad))
    return 1 if bad else 0


def cli(argv):
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        raise SystemExit(__doc__)
    folder = args[0]
    if not os.path.exists(os.path.join(folder, "manifest.json")):
        folder = os.path.join(folder, "solution_images")
    return main(os.path.abspath(folder), [a for a in argv if a != argv[0]])


if __name__ == "__main__":
    sys.exit(cli(sys.argv[1:]))
