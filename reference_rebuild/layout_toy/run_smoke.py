# -*- coding: utf-8 -*-
"""Smoke test of the question layout and the question/solution image placeholders, end to end.

    python -B reference_rebuild/layout_toy/run_smoke.py [--keep]

It builds a scratch chapter (reference_rebuild/layout_toy/_work/, removed afterwards unless --keep) from the
CURRENT chapter_template/build.py and the helpers of chapter_template/concept_plan.py.template plus this folder's
toy content, then checks:

  A. video_worklist: one "exercise" video slot per book question (solved example, prompt, exercise);
  B. build.py --placeholders, no solutions.json yet: each concept topic is followed by "Questions: <topic>" with
     one concept per book question, in the author's order; no book question is left in a concept topic; every
     question concept has a question image first and a solution image last; the long working gets a second
     solution image; a diagram sentence reaches the question card; the layout and solution gates agree;
  C. with solutions.json for two of the questions: gen_scenes.py makes a second solution scene only for the long
     one (answer box and common-mistake note on the last card only), check.py is clean, and build.py --placeholders
     swaps in the real cards for those two while the others keep their placeholders;
  D. the build is deterministic.

Nothing is rendered: Manim is not needed.
"""
from __future__ import annotations

import ast
import io
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
WORK = os.path.join(HERE, "_work")
PY = sys.executable
failures = []


def check(cond, msg):
    print(("  ok    " if cond else "  FAIL  ") + msg)
    if not cond:
        failures.append(msg)


def run(args, cwd=WORK):
    p = subprocess.run([PY, "-B", "-X", "utf8"] + args, cwd=cwd, capture_output=True, text=True, encoding="utf-8")
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def load(path):
    with io.open(path, encoding="utf-8") as f:
        return json.load(f)


def topics_of(plan):
    return [t for m in plan["modules"] for s in m["segments"] for t in s["topics"]]


def setup():
    if os.path.isdir(WORK):
        shutil.rmtree(WORK)
    os.makedirs(WORK)
    tmpl = os.path.join(ROOT, "chapter_template")
    shutil.copy(os.path.join(tmpl, "build.py"), WORK)
    shutil.copy(os.path.join(tmpl, "media_specs.py.template"), os.path.join(WORK, "media_specs.py"))
    for name in ("chapter.config.json", "content.py"):
        shutil.copy(os.path.join(HERE, name), WORK)
    with io.open(os.path.join(tmpl, "concept_plan.py.template"), encoding="utf-8") as f:
        helpers = f.read().split("\nTOOLS = {")[0]
    with io.open(os.path.join(HERE, "toy_topics.py"), encoding="utf-8") as f:
        toy = f.read()
    with io.open(os.path.join(WORK, "concept_plan.py"), "w", encoding="utf-8") as f:
        f.write(helpers + "\n" + toy)


def main():
    keep = "--keep" in sys.argv
    setup()
    plan_path = os.path.join(WORK, "layout_toy_ch98.json")

    print("A. video worklist")
    rc, out = run(["build.py", "--video-worklist"])
    check(rc == 0, "build.py --video-worklist runs (%s)" % out.strip().splitlines()[-1][:80])
    wl = load(os.path.join(WORK, "video_worklist.json"))
    ex = {i for v in wl["videos"] if v["kind"] == "exercise" for i in v["item_ids"]}
    check(ex == {"2.1.ex1", "2.1.try1", "2.1.FiO1", "2.2.FiO1"},
          "a solved example, a prompt and two exercises are all exercise (question) video slots: %s" % sorted(ex))

    print("B. structure and placeholders (no solutions.json yet)")
    rc, out = run(["build.py", "--placeholders"])
    check(os.path.exists(plan_path), "plan written")
    check(rc == 0 and "structure stage OK" in out,
          "the structure stage passes every gate that can pass before video scripts exist (rc=%d)" % rc)
    plan = load(plan_path)
    ts = topics_of(plan)
    names = [t["topic_name"] for t in ts]
    check(names == ["A Coin on a Line", "Adding on a Number Line", "Questions: Adding on a Number Line",
                    "Taking Away on a Number Line", "Questions: Taking Away on a Number Line", "What We Found"],
          "each concept topic is followed by its Questions topic: %s" % names)
    qt = {t["topic_name"]: t for t in ts if t["source_type"] == "exercise"}
    q1 = qt["Questions: Adding on a Number Line"]
    check([c["concept_name"] for c in q1["concepts"]] == ["Example 1", "Try This (2.1)", "Figure it Out (2.1), Q1"],
          "one concept per book question, in the author's order: %s" % [c["concept_name"] for c in q1["concepts"]])
    check(all(not (b.get("item_kind") and b.get("block_kind") == "worked_example")
              for t in ts if t["source_type"] != "exercise" for c in t["concepts"] for b in c["content"]),
          "no book question is left in a concept topic")
    media = {x["id"]: x for t in ts for x in t["media"]}
    shapes = {}
    for t in qt.values():
        for c in t["concepts"]:
            ids = c["media_ids"]
            roles = [media[i].get("image_role") for i in ids]
            shapes[c["concept_name"]] = (roles[0], roles[-1], len([r for r in roles if r == "solution"]))
            check(roles[0] == "question" and roles[-1] == "solution",
                  "%s: question image first, solution image last (%s)" % (c["concept_name"], ids[0].split(".")[-1]))
    check(shapes["Figure it Out (2.1), Q1"][2] == 2, "the long working has a second solution image")
    check(shapes["Example 1"][2] == 1 and shapes["Try This (2.1)"][2] == 1, "short workings keep one solution image")
    c_ex = next(c for c in q1["concepts"] if c["concept_name"] == "Example 1")
    c_try = next(c for c in q1["concepts"] if c["concept_name"] == "Try This (2.1)")
    c_long = next(c for c in q1["concepts"] if c["concept_name"].startswith("Figure it Out (2.1)"))
    check("number line from −5 to 5" in media[c_ex["media_ids"][0]]["description"],
          "the diagram sentence reaches the question card of Example 1")
    check("No diagram is needed" in media[c_try["media_ids"][0]]["description"], "a text-only question says so")
    check(all(m["build_status"] == "placeholder" for m in media.values() if m.get("image_role")),
          "every question/solution image is a placeholder")
    check(c_long["content"][0].get("solution_image_media_ids") == c_long["media_ids"][-2:],
          "the block lists both solution cards: %s" % c_long["content"][0].get("solution_image_media_ids"))
    check(c_ex["content"][0]["image_media_id"] == c_ex["media_ids"][0], "the block names its question image")
    url = media[c_long["media_ids"][-1]]["image_url"]
    check(url.endswith("c2_1_FiO1.IMG3.png") and "class_7/" in url, "reserved url uses the stable coverage stem: " + url[-40:])
    from importlib import util
    spec = util.spec_from_file_location("gate_runner_probe", os.path.join(ROOT, "gates", "question_layout.py"))
    gl = util.module_from_spec(spec)
    spec.loader.exec_module(gl)
    cfg = dict(load(os.path.join(WORK, "chapter.config.json")),
               book_item_kinds={"2.1.ex1": "example", "2.1.try1": "prompt", "2.1.FiO1": "exercise",
                                "2.2.FiO1": "exercise", "2.1.MathTalk": "talk"})
    check(gl.check(plan, cfg) == [], "gates/question_layout: no problems %s" % gl.check(plan, cfg)[:2])
    rep = load(os.path.join(WORK, "question_images_report.json"))
    check(len(rep) == 4 and sum(1 for r in rep if r["solution_images"] == 2) == 1,
          "question_images_report.json: 4 question concepts, 1 with a continuation card")

    print("C. real solutions for two of the questions")
    shutil.copy(os.path.join(HERE, "solutions.json"), WORK)
    rc, out = run([os.path.join(ROOT, "core", "solutions", "gen_scenes.py"), WORK])
    check(rc == 0, "gen_scenes.py: " + out.strip().splitlines()[-1])
    man = load(os.path.join(WORK, "solution_images", "manifest.json"))["images"]
    by = {}
    for e in man:
        by.setdefault(e["cov"], []).append(e)
    check(len(by["2.1.FiO1"]) == 3 and len(by["2.2.FiO1"]) == 2,
          "manifest: long working = question + 2 solution entries, short = question + 1")
    parts = sorted((e.get("part"), e["id"].split(".")[-1]) for e in by["2.1.FiO1"] if e["role"] == "solution")
    check(parts == [(1, "IMG2"), (2, "IMG3")], "the continuation card is IMG3, part 2 of 2: %s" % parts)
    scene = lambda f: io.open(os.path.join(WORK, "solution_images", "scenes", f), encoding="utf-8").read()
    s1, s2 = scene("c2_1_FiO1_sol.py"), scene("c2_1_FiO1_sol2.py")
    for src in (s1, s2):
        ast.parse(src)
    check("answer_box(" not in s1 and "answer_box(" in s2 and "Common mistake" in s2 and "Common mistake" not in s1,
          "answer box and common-mistake note only on the last card")
    check("start=" in s2 and "continues on the next card" in s1, "card 2 numbers on; card 1 says it continues")
    s_short = scene("c2_2_FiO1_sol.py")
    check("start=" not in s_short and "continues on" not in s_short and "answer_box(" in s_short,
          "a short working is a single, unchanged card")
    rc, out = run([os.path.join(ROOT, "core", "solutions", "check.py"), WORK])
    check(rc == 0 and "0 error(s)" in out, "check.py: " + out.strip().splitlines()[-1])
    rc, out = run(["build.py", "--placeholders"])
    plan2 = load(plan_path)
    ts2 = topics_of(plan2)
    media2 = {x["id"]: x for t in ts2 for x in t["media"]}
    q12 = [t for t in ts2 if t["topic_name"] == "Questions: Adding on a Number Line"][0]
    cl = next(c for c in q12["concepts"] if c["concept_name"].startswith("Figure it Out (2.1)"))
    sols = [media2[i] for i in cl["media_ids"] if media2[i].get("image_role") == "solution"]
    check(len(sols) == 2 and [s["render_source"].get("part") for s in sols] == [1, 2],
          "real attach: two solution cards, parts 1 and 2")
    check(cl["media_ids"][0].endswith(".IMG1") and cl["media_ids"][-1].endswith(".IMG3"), "real attach: media order")
    check(len([i for i in cl["media_ids"]]) == len(set(cl["media_ids"])), "no duplicate or dangling id after the swap")
    check(all(i in media2 for t in ts2 for c in t["concepts"] for i in c.get("media_ids", [])),
          "every media_id of every concept has a node")
    ce = next(c for c in q12["concepts"] if c["concept_name"] == "Example 1")
    check("PLACEHOLDER" in media2[ce["media_ids"][0]]["context"], "a question with no solution yet keeps its placeholder")
    cs = next(c for t in ts2 if t["topic_name"] == "Questions: Taking Away on a Number Line" for c in t["concepts"])
    check(len([i for i in cs["media_ids"] if media2[i].get("image_role") == "solution"]) == 1,
          "the short working has one solution card")

    print("D. determinism")
    before = io.open(plan_path, "rb").read()
    run(["build.py", "--placeholders"])
    check(io.open(plan_path, "rb").read() == before, "building twice gives the identical plan")

    if not keep:
        shutil.rmtree(WORK)
    print("\n%s" % ("ALL PASSED" if not failures else "%d FAILED" % len(failures)))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
