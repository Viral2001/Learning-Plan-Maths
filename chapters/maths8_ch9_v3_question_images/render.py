"""Render question images to png/<image id>.png.

    python render.py                 every image in manifest.json
    python render.py C40 C42         only those concepts
    python render.py C40_q           only that scene file
"""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
MANIM_PYTHON = r"C:\Users\DELL\Desktop\singularity-learn\.venv\Scripts\python.exe"


def render_one(entry, code_path=None, out_path=None, timeout=180):
    """Render one manifest entry. Returns (ok, log). A failed render leaves out_path untouched."""
    code_path = code_path or os.path.join(HERE, "scenes", entry["scene_file"])
    out_path = out_path or os.path.join(HERE, "png", entry["id"] + ".png")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    env = dict(os.environ, PYTHONPATH=HERE, PYTHONUTF8="1")
    with tempfile.TemporaryDirectory() as tmp:
        new_png = os.path.join(tmp, "out.png")
        cmd = [MANIM_PYTHON, "-m", "manim", "-s", "-qh", "--disable_caching",
               "--media_dir", tmp, "-o", new_png, code_path, entry["scene_class"]]
        try:
            run = subprocess.run(cmd, cwd=HERE, env=env, capture_output=True, timeout=timeout,
                                 text=True, encoding="utf-8", errors="replace")
        except subprocess.TimeoutExpired:
            return False, "Render stopped after %d seconds." % timeout
        log = (run.stdout or "") + (run.stderr or "")
        if run.returncode != 0 or not os.path.exists(new_png):
            return False, log
        os.replace(new_png, out_path)
    return True, log


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    with open(os.path.join(HERE, "manifest.json"), encoding="utf-8") as f:
        entries = json.load(f)["images"]
    picks = sys.argv[1:]
    if picks:
        entries = [e for e in entries if e["concept_short"] in picks
                   or e["scene_file"][:-3] in picks]
    bad = 0
    for e in entries:
        ok, log = render_one(e)
        print(("ok    " if ok else "FAIL  ") + e["id"])
        if not ok:
            bad += 1
            print(log[-1500:])
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
