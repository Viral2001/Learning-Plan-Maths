# -*- coding: utf-8 -*-
"""Question and solution image PLACEHOLDERS for every question concept, before any solution is authored.

    from core.solutions import placeholders
    report = placeholders.add(plan, cfg)        # after core.qt.apply(), before solutions.attach()

For each concept of a "Questions: <topic>" topic this adds, in the concept's media_ids order:

    IMG1  the question card      the question, and a diagram only when the question needs one
    VID1  the question video     (already there when the concept has one)
    IMG2  the solution card      numbered working and a highlighted answer
    IMG3  the solution, continued    only when the working is too long for one card (core/solutions/layout.py)

Nothing is drawn or rendered: every node has build_status "placeholder" and a reserved url. The nodes have
the fields core/solutions/attach.node writes, so the real pass (gen_scenes.py -> render.py -> attach.attach)
replaces them in place once solutions.json exists; attach.attach removes whatever placeholder it does not
reuse. Each block of the concept names its cards (image_media_id, solution_image_media_id, and
solution_image_media_ids when there are two solution cards), the shape gates/solution_content.py checks.

What a chapter author supplies (concept_plan.py FIO items): `q_figure` and `s_figure`, one plain sentence each
describing the diagram the question card / the solution card needs, or nothing when the card is text only.
The question-card sentence may hold only what the question itself gives: no working, no answer, no hint.

Node ids are <concept id>.IMGn (n is 1, 2, 3 unless the concept already has other images with those numbers, in
which case the cards take the next free numbers); bucket file names are <coverage stem>.IMGn.png, the pipeline's stable names
(core/solutions/attach.py), so the reserved url is the one the real card will have and an image rendered by
any route and dropped there needs no plan change. Config keys read (all optional): image_engine (default
"manim"; the node's render_source.engine), solution_continuation (a second solution card, default off here and
set on in the template's config sample), question_image_max_lines (default layout.MAX_LINES).
"""
from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))
from core.solutions import layout                                       # noqa: E402
from core.solutions.attach import BUCKET_PREFIX, key_dir_for           # noqa: E402
from core.solutions.gen_scenes import stem_of                          # noqa: E402

QT_SOURCE_TYPES = ("exercise", "question_topic")
QUESTION_KINDS = ("exercise", "exercise_question")
HINT = re.compile(r"\s*\[Hint:.*?\]", re.S)
NO_DIAGRAM = "No diagram is needed; the question text only."


def _clean(text):
    return re.sub(r"\s+", " ", HINT.sub("", text or "")).strip()


def _public_url(folder, filename):
    return "%s%s/%s" % (BUCKET_PREFIX, folder, filename)


def question_blocks(concept):
    for b in concept.get("content") or []:
        kind = b.get("block_kind")
        if kind in QUESTION_KINDS or (kind == "worked_example" and b.get("item_kind")):
            yield b


def node(concept_id, n, role, name, description, stem, key_dir, *, part=1, parts=1, engine="manim"):
    """One placeholder image node, field for field what core/solutions/attach.node writes. The node id is
    <concept id>.IMGn; the bucket file is <stem>.IMGn.png (stable when QT renumbers concepts), exactly the url
    attach.attach will write once the card is real."""
    iid = "%s.IMG%d" % (concept_id, n)
    file_id = "%s.IMG%d" % (stem, n)
    scene = stem + ("_q" if role == "question" else "_sol" if part == 1 else "_sol2")
    url = _public_url(key_dir, file_id + ".png")
    render_source = {"engine": engine, "scene": scene, "code_url": _public_url(key_dir + "/code", file_id + ".py"),
                     "style_url": _public_url(key_dir + "/code", "_style.py")}
    if parts > 1:
        render_source["part"], render_source["parts"] = part, parts
    if role == "question":
        instruction = "Try this question yourself before you watch the video."
        notes = "Let the student attempt this before showing the video or the solution image."
        title = "%s: question" % name
    else:
        instruction = ("Compare this with your own working, step by step." if part == 1 else
                       "This card carries on from the previous solution card; compare the rest of your working.")
        notes = "Show only after the student has attempted the question."
        title = "%s: solution%s" % (name, " (continued)" if part > 1 else "")
    return {
        "id": iid, "type": "image", "subtype": "illustration", "title": title,
        "image_url": url, "planned_url": url, "image_role": role, "render_source": render_source,
        "concept_id": concept_id, "home_concept_id": concept_id, "related_concept_ids": [],
        "image_category": "concept", "image_dimensions": "1920x1080", "aspect_ratio": "16:9",
        "build_status": "placeholder",
        "context": "%s image for %s. PLACEHOLDER: specified, not generated yet." % (role.capitalize(), name),
        "description": " ".join(description.split()), "instructions_for_student": instruction,
        "teaching_notes": notes, "labels": [],
        "accuracy_constraints": "", "generation_prompt": "", "negative_prompt": "",
    }


def _first(blocks, field):
    for b in blocks:
        if (b.get(field) or "").strip():
            return b[field].strip()
    return None


_TOKEN = re.compile(r"\bM\d+\.S\d+\.T\d+\.C\d+\.[A-Za-z0-9]+")


def _renumber_existing_images(plan):
    """A question concept that already carries other images (IMG1, IMG2 ...) keeps the order the upload API expects,
    image ids ascending down the list: question card, its existing images, video, solution card(s). So its existing
    images move up to IMG2, IMG3 ... (urls are frozen, only the ids change; every reference is rewritten) and the cards
    then take IMG1 and the numbers after. A concept with no other images is untouched."""
    rename = {}
    for module in plan.get("modules") or []:
        for segment in module.get("segments") or []:
            for topic in segment.get("topics") or []:
                if topic.get("source_type") not in QT_SOURCE_TYPES and \
                        not (topic.get("topic_name") or "").startswith("Questions:"):
                    continue
                by_id = {m.get("id"): m for m in topic.get("media") or []}
                for c in topic.get("concepts") or []:
                    if not list(question_blocks(c)):
                        continue
                    imgs = [by_id[i] for i in c.get("media_ids") or [] if i in by_id
                            and by_id[i].get("type") == "image" and by_id[i].get("image_role") not in ("question", "solution")]
                    num = lambda m: int(re.search(r"\.IMG(\d+)$", m["id"]).group(1)) if re.search(r"\.IMG(\d+)$", m["id"]) else 0
                    imgs.sort(key=num)
                    for want, m in enumerate(imgs, 2):
                        new_id = "%s.IMG%d" % (c["concept_id"], want)
                        if m["id"] != new_id and re.search(r"\.IMG\d+$", m["id"]):
                            rename[m["id"]] = new_id
    if not rename:
        return {}

    def fix(o):
        if isinstance(o, dict):
            return {k: fix(v) for k, v in o.items()}
        if isinstance(o, list):
            return [fix(v) for v in o]
        if isinstance(o, str) and not o.startswith("http"):
            return _TOKEN.sub(lambda mo: rename.get(mo.group(0), mo.group(0)), o)
        return o
    for k in list(plan.keys()):
        plan[k] = fix(plan[k])
    return rename


def add(plan, cfg, *, max_lines=None):
    """Add the placeholders to every question concept of the plan; returns one report row per concept.
    Idempotent. A concept whose question or solution image is already built is left alone."""
    key_dir = key_dir_for(cfg)
    _renumber_existing_images(plan)
    engine = cfg.get("image_engine") or "manim"
    max_lines = max_lines or cfg.get("question_image_max_lines") or layout.MAX_LINES
    continuation = bool(cfg.get("solution_continuation"))
    report = []
    for module in plan.get("modules") or []:
        for segment in module.get("segments") or []:
            for topic in segment.get("topics") or []:
                if topic.get("source_type") not in QT_SOURCE_TYPES and \
                        not (topic.get("topic_name") or "").startswith("Questions:"):
                    continue
                old_media = list(topic.get("media") or [])
                by_id = {m.get("id"): m for m in old_media}
                is_card = lambda m: m.get("type") == "image" and m.get("image_role") in ("question", "solution")
                built = {m.get("concept_id") for m in old_media if is_card(m) and m.get("build_status") == "built"}
                media_out, used = [], set()
                for c in topic.get("concepts") or []:
                    cid, name = c["concept_id"], c.get("concept_name", "")
                    blocks = list(question_blocks(c))
                    own = [by_id[i] for i in c.get("media_ids") or [] if i in by_id]
                    if not blocks or cid in built:
                        media_out += own
                        used.update(m["id"] for m in own)
                        continue
                    others = [m for m in own if not is_card(m)]
                    # a concept may already carry other images named IMG1, IMG2 ...: the cards take the next free numbers
                    taken = {int(mo.group(1)) for mo in (re.search(r"\.IMG(\d+)$", m["id"]) for m in others) if mo}
                    cov = (c.get("ncert_refs") or [name])[0]
                    stem = stem_of(cov)
                    # qt_part (core/qt.py's question/answer split): "question" and "answer" are two sibling
                    # concepts of one book question, each getting only its own card; a concept with no
                    # qt_part is the older, single-concept shape and keeps both cards as before. The reserved
                    # url is <stem>.IMGn.png regardless of which concept holds the card (gen_scenes.py always
                    # numbers question=1, solution=1+part, by stem, with no notion of qt_part) - so an answer
                    # concept's numbering must start at 2, leaving IMG1 reserved for its sibling's question card.
                    role = c.get("qt_part")
                    if role == "answer":
                        taken = taken | {1}
                    free = iter(k for k in range(1, 100) if k not in taken)

                    if role != "answer":
                        q_fig = _first(blocks, "q_figure")
                        qs = []
                        for b in blocks:
                            q = b.get("question") or ""
                            q = q if q and "[Hint:" not in q else _clean(q)
                            if q and q not in qs:
                                qs.append(q)
                        q_node = node(cid, next(free), "question", name,
                                      "Question card: %s %s Only the question and its figure are shown."
                                      % (" ".join(qs), q_fig or NO_DIAGRAM), stem, key_dir, engine=engine)

                    if role != "question":
                        s_fig = _first(blocks, "s_figure")
                        steps = [s for b in blocks for s in (b.get("steps") or []) if isinstance(s, str)]
                        steps_disp = [s for b in blocks for s in (b.get("steps_tex") or b.get("steps") or [])
                                      if isinstance(s, str)]
                        cards = layout.cards_needed(steps, with_figure=bool(s_fig), max_lines=max_lines) \
                            if continuation else 1
                        k = layout.split_point(steps, with_figure=bool(s_fig), max_lines=max_lines) if cards == 2 \
                            else len(steps)
                        answers = []
                        for b in blocks:
                            a = _clean(b.get("answer"))
                            if a and a not in answers:
                                answers.append(a)
                        answers = [a for a in answers if not any(a != o and a in o for o in answers)]
                        answer = " / ".join(answers)[:220]
                        answers_disp = []
                        for b in blocks:
                            a = b.get("answer_tex") or _clean(b.get("answer") or "")
                            if a and a not in answers_disp:
                                answers_disp.append(a)
                        answers_disp = [a for a in answers_disp if not any(a != o and a in o for o in answers_disp)]
                        answer_disp = " / ".join(answers_disp)[:220]
                        diagram = (" Diagram: %s" % s_fig) if s_fig else ""
                        if cards == 2:
                            sol_nodes = [
                                node(cid, next(free), "solution", name,
                                     "Solution card, part 1 of 2: numbered working, steps 1 to %d, with the working "
                                     "carried on to the next card.%s" % (k, diagram), stem, key_dir,
                                     part=1, parts=2, engine=engine),
                                node(cid, next(free), "solution", name,
                                     "Solution card, part 2 of 2: numbered working, steps %d to %d, and a highlighted "
                                     "answer: %s" % (k + 1, len(steps), answer), stem, key_dir,
                                     part=2, parts=2, engine=engine)]
                        else:
                            sol_nodes = [node(cid, next(free), "solution", name,
                                              "Solution card with numbered working steps and a highlighted answer: %s%s"
                                              % (answer, diagram), stem, key_dir, engine=engine)]

                    used.update(m["id"] for m in own)
                    if role == "question":
                        media_out += [q_node] + others
                        c["media_ids"] = [q_node["id"]] + [m["id"] for m in others]
                        c["image_decision"] = {
                            "needed": True,
                            "why": "The question concept of a question/answer pair: one image shows the question%s "
                                   "for the attempt." % (" and its figure" if q_fig else ""),
                            "question_diagram": q_fig, "engine": engine}
                        for b in blocks:
                            b["image_media_id"] = q_node["id"]
                        report.append({"concept_id": cid, "question": name, "refs": c.get("ncert_refs") or [],
                                       "question_diagram": bool(q_fig)})
                    elif role == "answer":
                        media_out += others + sol_nodes
                        c["media_ids"] = [m["id"] for m in others] + [n["id"] for n in sol_nodes]
                        c["image_decision"] = {
                            "needed": True,
                            "why": "The answer concept of a question/answer pair: %s the worked solution."
                                   % ("two images carry" if cards == 2 else "one image shows"),
                            "solution_diagram": s_fig, "solution_images": cards, "engine": engine}
                        tagged = layout.tagged_text(steps_disp, answer_disp, k, [n["title"] for n in sol_nodes])
                        for b in blocks:
                            b["solution_image_media_id"] = sol_nodes[0]["id"]
                            if cards == 2:
                                b["solution_image_media_ids"] = [n["id"] for n in sol_nodes]
                            else:
                                b.pop("solution_image_media_ids", None)
                            b["text"] = b["publication_text"] = tagged
                        report.append({"concept_id": cid, "question": name, "refs": c.get("ncert_refs") or [],
                                       "solution_diagram": bool(s_fig), "steps": len(steps),
                                       "est_lines": layout.total_lines(steps, bool(s_fig)), "solution_images": cards,
                                       "has_video": any(m.get("type") == "video" for m in others)})
                    else:
                        media_out += [q_node] + others + sol_nodes
                        c["media_ids"] = [q_node["id"]] + [m["id"] for m in others] + [n["id"] for n in sol_nodes]
                        c["image_decision"] = {
                            "needed": True,
                            "why": "A question concept: one image shows the question%s for the attempt, and %s the "
                                   "worked solution." % (" and its figure" if q_fig else "",
                                                        "two images carry" if cards == 2 else "one shows"),
                            "question_diagram": q_fig, "solution_diagram": s_fig, "solution_images": cards,
                            "engine": engine}
                        for b in blocks:
                            b["image_media_id"] = q_node["id"]
                            b["solution_image_media_id"] = sol_nodes[0]["id"]
                            if cards == 2:
                                b["solution_image_media_ids"] = [n["id"] for n in sol_nodes]
                            else:
                                b.pop("solution_image_media_ids", None)
                        report.append({"concept_id": cid, "question": name, "refs": c.get("ncert_refs") or [],
                                       "question_diagram": bool(q_fig), "solution_diagram": bool(s_fig),
                                       "steps": len(steps), "est_lines": layout.total_lines(steps, bool(s_fig)),
                                       "solution_images": cards, "has_video": any(m.get("type") == "video" for m in others)})
                media_out += [m for m in old_media if m.get("id") not in used and not (
                    is_card(m) and m.get("concept_id") not in built)]
                topic["media"] = media_out
                topic["available_content_types"] = sorted(set(topic.get("available_content_types") or []) | {"image"})
                if not topic.get("secondary_content_type"):
                    topic["secondary_content_type"] = "image"
    return report
