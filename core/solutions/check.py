# -*- coding: utf-8 -*-
"""Local checks on a chapter's solutions and their images; build.py runs this and blocks on errors.

    python -B core/solutions/check.py <new_design folder>

The plan gate (gates/solution_content.py) sees only the plan; this sees the files behind it:
  errors    solutions.json fails schema.validate; an exercise has no manifest entry (run gen_scenes.py);
            a scene file is missing, does not parse or lacks its scene class; a solution scene has no
            answer box or no "Common mistake" note; a question scene shows a hint word, or a number that is
            in the answer but not in the question (the answer leaking into the card); a step does not use
            the numbers of the answer.
  warnings  an image is still draft (the editor approves it); its PNG is not rendered; solutions.json changed
            after its scene was generated; an answer number never appears in the working; solutions.json now
            needs a different number of solution cards than the manifest has.
A working over two cards (manifest entries with part 1 and 2) keeps the highlighted answer and the
common-mistake note on the LAST card only.
"""
from __future__ import annotations

import ast
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))
from core.solutions import layout, schema                           # noqa: E402
from core.solutions.gen_scenes import FOLDER, cards_for, sol_sha    # noqa: E402

LEAK_WORDS = re.compile(r"\b(hint|answer|solution|therefore|hence|thus|proof|working)\b", re.I)
NUM = re.compile(r"(?<![\w.])\d+(?:\.\d+)?(?![\w])")


def scene_strings(path):
    """String constants of a scene file, except those inside the header(...) call. (None, error) if it
    does not parse."""
    src = ""
    try:
        with io.open(path, encoding="utf-8") as f:
            src = f.read()
        tree = ast.parse(src)
    except (OSError, SyntaxError) as e:
        return None, src, str(e)
    skip = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and getattr(node.func, "id", "") == "header":
            skip.update(id(n) for n in ast.walk(node))
    strings = [n.value for n in ast.walk(tree)
               if isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in skip]
    classes = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
    return strings, src, classes


def numbers(text):
    return set(NUM.findall(schema.tex_to_plain(text)))


def check(new_design):
    errors, warnings = [], []
    sols = schema.load(new_design)
    if not sols:
        return errors, warnings
    errors += ["solutions.json: " + p for p in schema.validate(sols)]
    out = os.path.join(new_design, FOLDER)
    mpath = os.path.join(out, "manifest.json")
    entries = []
    if os.path.exists(mpath):
        with io.open(mpath, encoding="utf-8") as f:
            entries = json.load(f)["images"]
    by_key = {(e["cov"], e["role"], e.get("part", 1)): e for e in entries}
    cfg = layout.chapter_config(new_design)

    for cov, sol in sols.items():
        steps_text = " ".join([sol.get("given", ""), sol.get("find", "")] + list(sol.get("steps") or [])
                              + [sol.get("verification", "")])
        missing_nums = sorted(numbers(sol.get("answer_tex", "")) - numbers(steps_text) - numbers(sol.get("question_tex", "")))
        if missing_nums:
            warnings.append("%s: the answer has %s, which the working never reaches" % (cov, missing_nums))
        if not schema.wants_images(sol):
            continue
        have = sorted(p for (c, r, p) in by_key if c == cov and r == "solution")
        want = cards_for(sol, cfg)
        if have and len(have) != want:
            warnings.append("%s: solutions.json needs %d solution card(s) but manifest.json has %d; re-run "
                            "gen_scenes.py (--force replaces edits made in the image editor)" % (cov, want, len(have)))
        cards = max(len(have), 1)
        for role, part in [("question", 1)] + [("solution", p) for p in range(1, cards + 1)]:
            e = by_key.get((cov, role, part))
            if not e:
                errors.append("%s: no %s image in %s/manifest.json (run core/solutions/gen_scenes.py)"
                              % (cov, role, FOLDER))
                continue
            path = os.path.join(out, "scenes", e["scene_file"])
            if not os.path.exists(path):
                errors.append("%s: scene file %s is missing" % (cov, e["scene_file"]))
                continue
            strings, src, classes = scene_strings(path)
            if strings is None:
                errors.append("%s: %s does not parse: %s" % (cov, e["scene_file"], classes))
                continue
            if e["scene_class"] not in classes:
                errors.append("%s: %s has no class %s" % (cov, e["scene_file"], e["scene_class"]))
            if role == "solution":
                if part == cards:
                    if "answer_box(" not in src:
                        errors.append("%s: solution scene has no highlighted answer box" % cov)
                    if "Common mistake" not in src:
                        errors.append("%s: solution scene has no Common mistake note" % cov)
                elif "answer_box(" in src:
                    errors.append("%s: solution card %d of %d shows the answer box; it belongs on the last card"
                                  % (cov, part, cards))
            else:
                shown = [s for s in strings if s != sol["question_tex"]]
                for s in shown:
                    hit = LEAK_WORDS.search(s)
                    if hit:
                        errors.append("%s: question scene shows '%s' (%r)" % (cov, hit.group(0), s[:40]))
                seen = set().union(*[numbers(s) for s in strings]) if strings else set()
                leaked = sorted((numbers(sol["answer_tex"]) - numbers(sol["question_tex"])
                                 - numbers(sol.get("given", ""))) & seen)
                if leaked:
                    errors.append("%s: question scene shows %s, which is in the answer but not in the question"
                                  % (cov, leaked))
            if e.get("sol_sha") and e["sol_sha"] != sol_sha(sol):
                warnings.append("%s: solutions.json changed after %s was generated; re-run gen_scenes.py --force "
                                "(replaces edits made in the image editor)" % (cov, e["scene_file"]))
            if not os.path.exists(os.path.join(out, "png", e["id"] + ".png")):
                warnings.append("%s: %s is not rendered yet (core/solutions/render.py)" % (cov, e["id"]))
    drafts = [e["id"] for e in entries if e.get("status") != "approved"]
    if drafts:
        warnings.append("%d of %d question/solution images are still draft; approve them in the image editor "
                        "before the bucket upload" % (len(drafts), len(entries)))
    return errors, warnings


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    if not argv:
        raise SystemExit(__doc__)
    errors, warnings = check(argv[0])
    for w in warnings:
        print("  ~", w)
    for e in errors:
        print("  -", e)
    print("%d error(s), %d warning(s)" % (len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
