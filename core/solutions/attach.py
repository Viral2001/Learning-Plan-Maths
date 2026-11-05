# -*- coding: utf-8 -*-
"""Attach the question and solution images (solution_images/manifest.json) to an assembled plan.

    from core.solutions import attach
    attach.attach(plan, new_design_folder, key_dir)      # after core.qt.apply(), before the gates

    python -B core/solutions/attach.py <new_design folder> upload [--include-draft]   # PNGs + scene code -> bucket

Each question concept ends with media_ids = [IMG1 (question), VID1 (video), IMG2 (solution)]: the student
sees the question card, attempts it, watches the video, then compares with the solution card.
The concept is found by coverage id: the manifest's `cov` is in the concept's `ncert_refs`, and a
question-topic concept (authored_key "qt.*") wins over the teaching concept the item was first written in.
File names in the bucket stay `<manifest id>.png` (stable when QT renumbers concepts); only the plan node
id is `<concept_id>.IMG1` / `.IMG2`.
"""
from __future__ import annotations

import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))
from core.solutions import layout, schema  # noqa: E402

FOLDER = "solution_images"
BUCKET_PREFIX = "https://media.singularity-learn.com/learning_plan_assets/"
HINT = re.compile(r"\s*\[Hint:.*?\]", re.S)
QUESTION_KINDS = ("exercise", "exercise_question")


def key_dir_for(cfg, version="v1"):
    """Bucket folder for this chapter's solution images, from asset_base_template in chapter.config.json."""
    base = cfg["asset_base_template"].format(grade=cfg["grade"], chapter_no=cfg["chapter_no"])
    if base.startswith(BUCKET_PREFIX):
        base = base[len(BUCKET_PREFIX):]
    return "%s/solution_image_%s" % (base.rstrip("/"), version)


def figure_words(fig, role):
    """One sentence describing the figure on a card, for the node's description. Never the answer on a
    question card."""
    kind = (fig or {}).get("type", "none")
    if kind == "right_triangle":
        lab = fig.get(role) or fig.get("question") or {}
        parts = ["%s side %s" % (n, re.sub(r"\\[,;:! ]|\\text|[{}]", " ", lab[k]).strip())
                 for n, k in (("the upright", "left"), ("the base", "bottom"), ("the hypotenuse", "hyp"))
                 if lab.get(k)]
        return "An upright right triangle with the right angle marked; " + ", ".join(parts) + "." if parts \
            else "An upright right triangle with the right angle marked."
    if kind == "dot_grid":
        n = int(fig.get("n", 5))
        return "A %d by %d grid of dots." % (n, n)
    if kind == "grid_table":
        return "A table of %d rows." % len(fig.get("rows") or [])
    return ""


def node(entry, sol, concept_id, key_dir, has_png):
    role = entry["role"]
    short = sol["label"]
    url = _public_url(key_dir, entry["id"] + ".png")
    fig = figure_words(sol.get("figure"), role)
    part, parts = entry.get("part", 1), entry.get("parts", 1)     # a long working runs over two solution cards
    if role == "question":
        question = HINT.sub("", sol["question"])
        text = "Question card: %s %s Only the question and its figure are shown." % (question, fig)
        instruction = "Try this question yourself before you watch the video."
        notes = "Let the student attempt this before showing the video or the solution image."
    else:
        answer = re.sub(r"\s+", " ", schema.tex_to_plain(sol["answer_tex"])).rstrip(".")
        if parts > 1 and part == 1:
            text = "Solution card, part 1 of %d: Given, To find, method and the first numbered steps of the " \
                   "working, carried on to the next card. %s" % (parts, fig)
            instruction = "Compare this with your own working, step by step."
        elif parts > 1:
            text = "Solution card, part %d of %d: the rest of the numbered working, a highlighted answer and a " \
                   "common-mistake note: %s %s" % (part, parts, answer, fig)
            instruction = "This card carries on from the previous solution card; compare the rest of your working."
        else:
            text = "Solution card with Given, To find, numbered working, a highlighted answer and a common-mistake " \
                   "note: %s %s" % (answer, fig)
            instruction = "Compare this with your own working, step by step."
        notes = "Show only after the student has attempted the question."
    n = 1 if role == "question" else 1 + part
    render_source = {
        "engine": "manim",
        "scene": entry["scene_class"],
        "code_url": _public_url(key_dir + "/code", entry["id"] + ".py"),
        "style_url": _public_url(key_dir + "/code", "_style.py"),
    }
    if parts > 1:
        render_source["part"], render_source["parts"] = part, parts
    return {
        "id": "%s.IMG%d" % (concept_id, n),
        "type": "image",
        "subtype": "illustration",
        "title": "%s: %s%s" % (short, role, " (continued)" if part > 1 else ""),
        "image_url": url,
        "planned_url": url,
        "image_role": role,
        "render_source": render_source,
        "concept_id": concept_id,
        "home_concept_id": concept_id,
        "related_concept_ids": [],
        "image_category": "concept",
        "image_dimensions": "1920x1080",
        "aspect_ratio": "16:9",
        "build_status": "built" if has_png else "placeholder",
        "context": "%s image for %s." % (role.capitalize(), short),
        "description": " ".join(text.split()),
        "instructions_for_student": instruction,
        "teaching_notes": notes,
        "labels": [],
        "accuracy_constraints": "",
        "generation_prompt": "",
        "negative_prompt": "",
    }


def _public_url(folder, filename):
    return "%s%s/%s" % (BUCKET_PREFIX, folder, filename)


def _concepts(plan):
    for module in plan["modules"]:
        for segment in module["segments"]:
            for topic in segment["topics"]:
                for concept in topic.get("concepts", []):
                    yield topic, concept


def find_concept(plan, cov, role=None):
    """(topic, concept) for a coverage id: a question-topic concept first, else any concept citing it.
    When a book question is split into a question concept and an answer concept (qt_part, core/qt.py),
    `role` picks the right one: role="question" wants the qt_part "question" concept, anything else
    wants the qt_part "answer" concept. An older, unsplit chapter has no qt_part and role is ignored -
    both roles resolve to the same one concept."""
    hits = [(t, c) for t, c in _concepts(plan) if cov in (c.get("ncert_refs") or [])]
    if role is not None:
        want = "question" if role == "question" else "answer"
        by_role = [(t, c) for t, c in hits if c.get("qt_part") == want]
        if by_role:
            hits = by_role
    qt = [(t, c) for t, c in hits if str(c.get("authored_key") or "").startswith("qt.")]
    return (qt or hits or [(None, None)])[0]


def attach(plan, new_design, key_dir):
    """Add IMG1/IMG2 nodes and order media_ids. Returns the list of problems (empty = fine)."""
    out = os.path.join(new_design, FOLDER)
    mpath = os.path.join(out, "manifest.json")
    if not os.path.exists(mpath):
        return []
    with io.open(mpath, encoding="utf-8") as f:
        manifest = json.load(f)
    sols = schema.load(new_design)
    img_cfg = layout.chapter_config(new_design)
    problems, by_cov = [], {}
    for e in manifest["images"]:
        by_cov.setdefault(e["cov"], []).append(e)
    # one question per concept: a concept holding two questions would keep only the last pair of cards.
    # A split question/answer pair (qt_part, core/qt.py) resolves both roles to their own concept, each
    # with exactly one cov - only a genuine misconfiguration puts more than one cov on one concept.
    owner = {}
    for cov in by_cov:
        for role in ("question", "solution"):
            _, concept = find_concept(plan, cov, role=role)
            if concept is not None:
                owner.setdefault(concept["concept_id"], set()).add(cov)
    for cid, covs in owner.items():
        if len(covs) > 1:
            problems.append("%s: holds %d questions (%s); give each question its own concept (one concept, one "
                            "video, one question and solution image each)"
                            % (cid, len(covs), ", ".join(sorted(covs))))
    if problems:
        return problems
    for cov, entries in by_cov.items():
        sol = sols.get(cov)
        if sol is None:
            problems.append("%s: in manifest.json but not in solutions.json" % cov)
            continue
        q_topic, q_concept = find_concept(plan, cov, role="question")
        s_topic, s_concept = find_concept(plan, cov, role="solution")
        if q_concept is None or s_concept is None:
            problems.append("%s: no concept in the plan cites it in ncert_refs" % cov)
            continue
        # one question card, and one solution card or (a long working, chapter.config "solution_continuation")
        # two, numbered by `part`
        q_entries = [e for e in entries if e["role"] == "question"]
        s_entries = sorted((e for e in entries if e["role"] == "solution"), key=lambda e: e.get("part", 1))
        if len(q_entries) != 1 or not s_entries or [e.get("part", 1) for e in s_entries] != list(range(1, len(s_entries) + 1)):
            problems.append("%s: manifest needs one question image and one solution image (or solution parts 1 to n)"
                            % cov)
            continue

        if q_concept is s_concept:
            # legacy: one concept holds both the question and solution card(s)
            topic, concept = q_topic, q_concept
            cid = concept["concept_id"]
            is_card = lambda m: (m.get("type") == "image" and m.get("image_role") in ("question", "solution")
                                 and m.get("concept_id") == cid)
            removed = {m["id"] for m in topic.get("media", []) if is_card(m)}      # earlier cards, placeholders included
            topic["media"] = [m for m in topic.get("media", []) if not is_card(m)]
            q_node = node(q_entries[0], sol, cid, key_dir,
                          os.path.exists(os.path.join(out, "png", q_entries[0]["id"] + ".png")))
            s_nodes = [node(e, sol, cid, key_dir, os.path.exists(os.path.join(out, "png", e["id"] + ".png")))
                       for e in s_entries]
            topic["media"].extend([q_node] + s_nodes)
            topic["available_content_types"] = sorted(set(topic.get("available_content_types") or []) | {"image"})
            mine = {q_node["id"]} | {n["id"] for n in s_nodes}
            rest = [m for m in concept.get("media_ids") or [] if m not in mine and m not in removed]
            concept["media_ids"] = [q_node["id"]] + rest + [n["id"] for n in s_nodes]
            # the question block itself names the cards (Class 9 Ch5 shape: image_media_id), not only the concept
            for b in concept.get("content") or []:
                if b.get("block_kind") in QUESTION_KINDS or (b.get("block_kind") == "worked_example" and b.get("item_kind")):
                    b["image_media_id"] = q_node["id"]
                    b["solution_image_media_id"] = s_nodes[0]["id"]
                    if len(s_nodes) > 1:
                        b["solution_image_media_ids"] = [n["id"] for n in s_nodes]
                    else:
                        b.pop("solution_image_media_ids", None)
            if "image_media_id" in concept:
                concept["image_media_id"] = q_node["id"]
            decision = dict(concept.get("image_decision") or {})      # keep a placeholder pass's diagram notes
            decision.update({
                "needed": True,
                "why": "A question concept: one image shows the question and its figure for the attempt, and %s the "
                       "worked solution." % ("two images carry" if len(s_nodes) > 1 else "one shows"),
            })
            if len(s_nodes) > 1:
                decision["solution_images"] = len(s_nodes)
            concept["image_decision"] = decision
            continue

        # split: a question concept (image only) and a sibling answer concept (video + solution card(s))
        q_cid, s_cid = q_concept["concept_id"], s_concept["concept_id"]
        is_q_card = lambda m: (m.get("type") == "image" and m.get("image_role") == "question"
                               and m.get("concept_id") == q_cid)
        q_removed = {m["id"] for m in q_topic.get("media", []) if is_q_card(m)}
        q_topic["media"] = [m for m in q_topic.get("media", []) if not is_q_card(m)]
        q_node = node(q_entries[0], sol, q_cid, key_dir,
                      os.path.exists(os.path.join(out, "png", q_entries[0]["id"] + ".png")))
        q_topic["media"].append(q_node)
        q_topic["available_content_types"] = sorted(set(q_topic.get("available_content_types") or []) | {"image"})
        rest_q = [m for m in q_concept.get("media_ids") or [] if m != q_node["id"] and m not in q_removed]
        q_concept["media_ids"] = [q_node["id"]] + rest_q
        for b in q_concept.get("content") or []:
            if b.get("block_kind") in QUESTION_KINDS or (b.get("block_kind") == "worked_example" and b.get("item_kind")):
                b["image_media_id"] = q_node["id"]
        if "image_media_id" in q_concept:
            q_concept["image_media_id"] = q_node["id"]
        q_decision = dict(q_concept.get("image_decision") or {})
        q_decision.update({"needed": True,
                            "why": "The question concept of a question/answer pair: one image shows the question "
                                   "and its figure for the attempt."})
        q_concept["image_decision"] = q_decision

        is_s_card = lambda m: (m.get("type") == "image" and m.get("image_role") == "solution"
                               and m.get("concept_id") == s_cid)
        s_removed = {m["id"] for m in s_topic.get("media", []) if is_s_card(m)}
        s_topic["media"] = [m for m in s_topic.get("media", []) if not is_s_card(m)]
        s_nodes = [node(e, sol, s_cid, key_dir, os.path.exists(os.path.join(out, "png", e["id"] + ".png")))
                   for e in s_entries]
        s_topic["media"].extend(s_nodes)
        s_topic["available_content_types"] = sorted(set(s_topic.get("available_content_types") or []) | {"image"})
        mine_s = {n["id"] for n in s_nodes}
        rest_s = [m for m in s_concept.get("media_ids") or [] if m not in mine_s and m not in s_removed]
        s_concept["media_ids"] = rest_s + [n["id"] for n in s_nodes]
        s_blocks = [b for b in s_concept.get("content") or []
                    if b.get("block_kind") in QUESTION_KINDS
                    or (b.get("block_kind") == "worked_example" and b.get("item_kind"))]
        for b in s_blocks:
            b["solution_image_media_id"] = s_nodes[0]["id"]
            if len(s_nodes) > 1:
                b["solution_image_media_ids"] = [n["id"] for n in s_nodes]
            else:
                b.pop("solution_image_media_ids", None)
        # "[Image: <title>]" markers in the displayed text, at the step where a long working moves to a
        # second solution card - sol["cut"] is the author's override, else the same split gen_scenes.py
        # already rendered the cards with (core/solutions/layout.py).
        steps_disp = [st for b in s_blocks for st in (b.get("steps_tex") or b.get("steps") or []) if isinstance(st, str)]
        answer_disp = next((b["answer_tex"] for b in s_blocks if b.get("answer_tex")), None) \
            or (s_blocks[0].get("answer") if s_blocks else "")
        k = sol.get("cut") or layout.split_point(
            [schema.tex_to_plain(x) for x in sol["steps"]], with_figure=bool(sol.get("figure")),
            max_lines=img_cfg.get("question_image_max_lines") or layout.MAX_LINES)
        tagged = layout.tagged_text(steps_disp, answer_disp, k, [n["title"] for n in s_nodes])
        for b in s_blocks:
            b["text"] = b["publication_text"] = tagged
        s_decision = dict(s_concept.get("image_decision") or {})
        s_decision.update({
            "needed": True,
            "why": "The answer concept of a question/answer pair: %s the worked solution."
                   % ("two images carry" if len(s_nodes) > 1 else "one image shows"),
        })
        if len(s_nodes) > 1:
            s_decision["solution_images"] = len(s_nodes)
        s_concept["image_decision"] = s_decision
    # the manifest records where the files go; the plan nodes point there
    if manifest.get("key_dir") != key_dir:
        manifest["key_dir"] = key_dir
        with io.open(mpath, "w", encoding="utf-8") as f:
            json.dump(manifest, f, ensure_ascii=False, indent=1)
    return problems


def upload(new_design, include_draft=False):
    """Upload PNGs and scene code to the bucket. Only approved images, unless include_draft."""
    from core.image_editor import bucket
    out = os.path.join(new_design, FOLDER)
    with io.open(os.path.join(out, "manifest.json"), encoding="utf-8") as f:
        manifest = json.load(f)
    key_dir = manifest.get("key_dir")
    if not key_dir:
        raise SystemExit("manifest.json has no key_dir yet: run build.py once so attach.attach() sets it")
    entries = [e for e in manifest["images"] if include_draft or e["status"] == "approved"]
    skipped = [e["id"] for e in manifest["images"] if e not in entries]
    pngs, codes = [], []
    for e in entries:
        png = os.path.join(out, "png", e["id"] + ".png")
        if not os.path.exists(png):
            raise SystemExit("no PNG for %s: run core/solutions/render.py first" % e["id"])
        with open(png, "rb") as f:
            pngs.append((e["id"] + ".png", f.read()))
        with open(os.path.join(out, "scenes", e["scene_file"]), "rb") as f:
            codes.append((e["id"] + ".py", f.read()))
    if not entries:
        print("nothing to upload (%d image(s) not approved yet)" % len(skipped))
        return 0
    with open(os.path.join(out, "_style.py"), "rb") as f:
        codes.append(("_style.py", f.read()))
    bucket.upload(key_dir, pngs)
    bucket.upload(key_dir + "/code", codes)
    print("bucket ok: %d png, %d code files; %d not approved and skipped" % (len(pngs), len(codes), len(skipped)))
    return 0


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    args = [a for a in argv if not a.startswith("--")]
    if len(args) < 2 or args[1] != "upload":
        raise SystemExit(__doc__)
    return upload(args[0], include_draft="--include-draft" in argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
