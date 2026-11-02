# -*- coding: utf-8 -*-
"""solutions.json -> Manim scene files, manifest.json and plan_text.json for the editor and renderer.

    python -B core/solutions/gen_scenes.py <chapter new_design folder> [--force]

Writes into <chapter>/solution_images/:
    scenes/<stem>_q.py, scenes/<stem>_sol.py   one question card and one solution card per question
    _style.py                                  copy of core/solutions/style/_style.py
    render.py                                  thin shim over core/solutions/render.py (the editor loads it)
    manifest.json, plan_text.json              what core/image_editor/server.py reads
A scene file that already exists is kept (a teacher may have edited it in the editor) unless --force.
Question cards show the question and a figure only; solution cards are the board-format working
(Given, To find, method, numbered steps, check, highlighted answer, common-mistake note).
"""
from __future__ import annotations

import hashlib
import io
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))
from core.solutions import schema  # noqa: E402

FOLDER = "solution_images"
SHIM = '''"""Editor shim: the renderer lives in core/solutions/render.py."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
_d = HERE
while not (os.path.isdir(os.path.join(_d, "core")) and os.path.isdir(os.path.join(_d, "gates"))):
    if os.path.dirname(_d) == _d:
        raise SystemExit("pipeline root not found above %s" % HERE)
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from core.solutions import render as _render  # noqa: E402


def render_one(entry, code_path=None, out_path=None, timeout=180):
    return _render.render_one(HERE, entry, code_path, out_path, timeout)


if __name__ == "__main__":
    sys.exit(_render.main(HERE, sys.argv[1:]))
'''


def stem_of(cov):
    stem = re.sub(r"[^0-9A-Za-z]+", "_", cov).strip("_")
    return "c" + stem if stem[:1].isdigit() else stem      # it becomes a Python class name


def rs(text):
    """A Python string literal for LaTeX text, raw when it can be (so a teacher can edit it in the editor)."""
    if '"' not in text and not text.endswith("\\") and "\n" not in text:
        return 'r"%s"' % text
    if "'" not in text and not text.endswith("\\") and "\n" not in text:
        return "r'%s'" % text
    return repr(text)


def question_figure(sol):
    """The figure spec with the solution-role labels dropped, so the question card's code never holds the answer."""
    fig = sol.get("figure")
    if not fig or fig.get("type", "none") == "none":
        return None
    return {k: v for k, v in fig.items() if k not in ("solution", "solved")}


def sol_sha(sol):
    return hashlib.sha256(json.dumps(sol, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()[:12]


def question_scene(stem, sol):
    fig = question_figure(sol)
    lines = ["from _style import *", "", "", "class %s_q(Scene):" % stem, "    def construct(self):",
             "        self.add(header(\"Question\", %s))" % rs(sol["label"]), ""]
    if fig:
        lines += ["        question = para(%s, width=6.8, size=36)" % rs(sol["question_tex"]),
                  "        question.move_to([LEFT_EDGE + question.width / 2, 0, 0])",
                  "        self.add(question)", "",
                  "        FIG = %r" % (fig,),
                  "        self.add(figure_from_spec(FIG, \"question\", centre=(3.6, -0.2)))"]
    else:
        lines += ["        question = para(%s, width=12.4, size=40)" % rs(sol["question_tex"]),
                  "        question.move_to([LEFT_EDGE + question.width / 2, 0.3, 0])",
                  "        self.add(question)"]
    return "\n".join(lines) + "\n"


def solution_scene(stem, sol):
    fig = sol.get("figure") if (sol.get("figure") or {}).get("type", "none") != "none" else None
    w = 7.6 if fig else 12.4
    lines = ["from _style import *", "", "", "class %s_sol(Scene):" % stem, "    def construct(self):",
             "        self.add(header(\"Solution\", %s))" % rs(sol["label"]), ""]
    if fig:
        lines += ["        FIG = %r" % (fig,),
                  "        self.add(figure_from_spec(FIG, \"solution\", centre=(-3.4, -0.3)))", ""]
    lines.append("        parts = VGroup()")
    for tag, key in (("Given", "given"), ("To find", "find"), ("Method", "method")):
        if sol.get(key):
            lines.append("        parts.add(para(%s, %s, 24))" % (rs(r"\textbf{%s:} %s" % (tag, sol[key])), w))
    lines.append("        parts.arrange(DOWN, aligned_edge=LEFT, buff=0.1)")
    lines.append("        work = steps([")
    for s in sol["steps"]:
        lines.append("            %s," % rs(s))
    lines.append("        ], width=%s, size=24, gap=0.08)" % w)
    if sol.get("verification"):
        lines.append("        check = note(\"Check\", %s, width=%s, size=22, fill=TEAL_BG, colour=TEAL)"
                     % (rs(sol["verification"]), w))
    lines.append("        ans = answer_box(%s, width=%s, size=26, pad=0.2)" % (rs(sol["answer_tex"]), w))
    lines.append("        slip = note(\"Common mistake\", %s, width=%s, size=22)" % (rs(sol["common_mistake"]), w))
    blocks = ["parts", "work"] + (["check"] if sol.get("verification") else []) + ["ans", "slip"]
    lines += ["        column = VGroup(%s).arrange(DOWN, aligned_edge=LEFT, buff=0.14)" % ", ".join(blocks),
              "        fit_column(column)"]
    if fig:
        lines.append("        column.move_to([RIGHT_EDGE - column.width / 2, -0.3, 0])")
    else:
        lines.append("        column.move_to([LEFT_EDGE + column.width / 2, -0.3, 0])")
    lines.append("        self.add(column)")
    return "\n".join(lines) + "\n"


def plan_text_entry(cov, sol):
    steps, ans = schema.plan_fields(sol)
    return {"name": sol["label"], "q": sol["question"], "steps": steps, "ans": ans,
            "figure": (sol.get("figure") or {}).get("type", "none")}


def generate(nd, force=False):
    sols = schema.load(nd)
    problems = schema.validate(sols)
    if problems:
        raise SystemExit("solutions.json has problems:\n  " + "\n  ".join(problems))
    out = os.path.join(nd, FOLDER)
    os.makedirs(os.path.join(out, "scenes"), exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "style", "_style.py"), os.path.join(out, "_style.py"))
    with io.open(os.path.join(out, "render.py"), "w", encoding="utf-8", newline="\n") as f:
        f.write(SHIM)
    old, key_dir = {}, ""
    mpath = os.path.join(out, "manifest.json")
    if os.path.exists(mpath):
        with io.open(mpath, encoding="utf-8") as f:
            prev_manifest = json.load(f)
        key_dir = prev_manifest.get("key_dir", "")
        old = {(e["cov"], e["role"]): e for e in prev_manifest["images"] if "cov" in e}
    images, plan_text, written = [], {}, 0
    for cov, sol in sols.items():
        if not schema.wants_images(sol):
            continue
        stem = stem_of(cov)
        plan_text[cov] = plan_text_entry(cov, sol)
        for n, role, tag, build in ((1, "question", "q", question_scene), (2, "solution", "sol", solution_scene)):
            scene_file = "%s_%s.py" % (stem, tag)
            path = os.path.join(out, "scenes", scene_file)
            regenerated = force or not os.path.exists(path)
            if regenerated:
                with io.open(path, "w", encoding="utf-8", newline="\n") as f:
                    f.write(build(stem, sol))
                written += 1
            prev = old.get((cov, role), {})
            entry = {"id": prev.get("id") or "%s.IMG%d" % (stem, n), "cov": cov, "concept_id": cov,
                     "concept_short": stem, "role": role, "scene_file": scene_file,
                     "scene_class": "%s_%s" % (stem, tag),
                     "status": "draft" if regenerated else (prev.get("status") or "draft"),
                     # the solution this scene was generated from; check.py warns when solutions.json moved on
                     "sol_sha": sol_sha(sol) if regenerated else (prev.get("sol_sha") or sol_sha(sol))}
            if prev.get("uploaded_sha") and not regenerated:
                entry["uploaded_sha"] = prev["uploaded_sha"]
            images.append(entry)
    with io.open(mpath, "w", encoding="utf-8") as f:
        json.dump({"key_dir": key_dir, "images": images}, f, ensure_ascii=False, indent=1)
    with io.open(os.path.join(out, "plan_text.json"), "w", encoding="utf-8") as f:
        json.dump(plan_text, f, ensure_ascii=False, indent=1)
    return out, len(images), written


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        raise SystemExit(__doc__)
    out, n, written = generate(args[0], force="--force" in argv)
    print("wrote %s: %d images in the manifest, %d scene files written" % (out, n, written))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
