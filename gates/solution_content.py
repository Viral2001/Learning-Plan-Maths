# -*- coding: utf-8 -*-
"""Every question has its solution: working and answer in the plan, and (by default) a question image,
the video and a solution image in that order.

Runs when chapter.config.json has a truthy `"solutions"`. New chapters must have it (chapter_template/build.py
stops without the key): the concept text shows the question, numbered steps and "Answer:", and media_ids is
question image, video, solution image. `"text"` (working + answer only) is kept for old callers.
`"solutions_video": false` drops the video requirement (Class 10 holds its question videos for now).
A chapter that predates solutions.json and has no such key is untouched.

A "question block" is a content block of block_kind `exercise` or `exercise_question`, or a
`worked_example` carrying an `item_kind` (the shape core/qt.py gives a moved or fallback exercise).

Per question concept:
  1. every question block has non-empty `steps` and `answer`, and `solution_status` (Class 9/10) is not
     "to_author";
  2. media_ids is [question image, video(s), solution image]: first an image with image_role "question",
     last an image with image_role "solution", at least one video between (images mode). A working too long
     for one card may end with a second solution image (the block then lists `solution_image_media_ids`);
  3. both images carry `render_source` (Manim code the editor can open), and the question image's own
     fields hold no hint, answer or solution words (the question text itself is exempt, as in
     theorem_variant rule 2).
The scene files, the manifest and the numbers in the answer are checked locally by core/solutions/check.py,
which build.py runs: a plan alone does not carry them.

core/solutions/answer_checker.py is this gate's "every question has steps and answer" rule (point 1
above), runnable standalone against just a plan - no chapter.config.json needed - for a fast, chapter-
wide list of which question concepts still need a worked solution written, without running every other
check here too. Its docstring carries the authoring policy (core/qt.py's _question_answer_blocks and
math_solutions/skill/references/format-rules.md rule 9): read the question and the chapter's own
content and write an accurate one for every gap found - never leave it, and never hand back a guess.

    python -B solution_content.py <plan.json> <chapter.config.json>
"""
from __future__ import annotations

import json
import re
import sys

try:
    from .theorem_variant import HINT_WORDS_RE
except ImportError:                      # run as a script
    from theorem_variant import HINT_WORDS_RE

QUESTION_KINDS = ("exercise", "exercise_question")
PLACEHOLDER_RE = re.compile(r"read the question in the book|attempt it before watching|\bTODO\b|to be authored"
                            r"|placeholder", re.I)


def ids_missing(block, concept):
    """The question block names both cards (image_media_id / solution_image_media_id) and they are the first
    and last of the concept's media_ids. '' when fine.

    A working too long for one card may carry on to a second solution image. Then the block also lists
    `solution_image_media_ids` (the trailing solution images, in order, the last of them the last media_id)
    and `solution_image_media_id` is the first of them. A block without that list is checked exactly as before."""
    ids = concept.get("media_ids") or []
    if not ids:
        return ""
    if block.get("image_media_id") != ids[0]:
        return "image_media_id must be the question image (first media_id)"
    more = block.get("solution_image_media_ids")
    if more:
        if list(more) != ids[-len(more):] or block.get("solution_image_media_id") != more[0]:
            return ("solution_image_media_ids must be the trailing media_ids, led by solution_image_media_id "
                    "(the solution image and its continuation)")
        return ""
    if block.get("solution_image_media_id") != ids[-1]:
        return "solution_image_media_id must be the solution image (last media_id)"
    return ""


def _question_ids_missing(block, concept):
    """The question concept of a core/qt.py split pair: its block names the question image
    (image_media_id), the concept's own first (and normally only) media_id. '' when fine."""
    ids = concept.get("media_ids") or []
    if not ids:
        return ""
    if block.get("image_media_id") != ids[0]:
        return "image_media_id must be the question image (first media_id)"
    return ""


def _answer_ids_missing(block, concept):
    """The answer concept of a core/qt.py split pair: its block names the solution image(s)
    (solution_image_media_id[_s]), the trailing media_ids (a video, if any, comes before them).
    '' when fine."""
    ids = concept.get("media_ids") or []
    if not ids:
        return ""
    more = block.get("solution_image_media_ids")
    if more:
        if list(more) != ids[-len(more):] or block.get("solution_image_media_id") != more[0]:
            return ("solution_image_media_ids must be the trailing media_ids, led by solution_image_media_id "
                    "(the solution image and its continuation)")
        return ""
    if block.get("solution_image_media_id") != ids[-1]:
        return "solution_image_media_id must be the solution image (last media_id)"
    return ""


def walk_topics(plan):
    for module in plan.get("modules") or []:
        for segment in module.get("segments") or []:
            for topic in segment.get("topics") or []:
                yield topic


def question_blocks(concept):
    for b in concept.get("content") or []:
        kind = b.get("block_kind")
        if kind in QUESTION_KINDS or (kind == "worked_example" and b.get("item_kind")):
            yield b


def check(plan, config=None):
    mode = (config or {}).get("solutions")
    if not mode:
        return []
    with_images = mode != "text"
    need_video = (config or {}).get("solutions_video", True)
    problems = []
    media = {}
    for topic in walk_topics(plan):
        for m in topic.get("media") or []:
            media[m.get("id")] = m
    for topic in walk_topics(plan):
        for concept in topic.get("concepts") or []:
            cid = concept["concept_id"]
            blocks = list(question_blocks(concept))
            if not blocks:
                continue
            # qt_part (core/qt.py's question/answer split): "question" holds only the question card,
            # no steps/answer/video expected; "answer" holds the working, answer, video and solution
            # card(s). A concept with no qt_part is the older, single-concept shape (both cards).
            role = concept.get("qt_part")
            for b in blocks:
                ref = b.get("coverage_id") or b.get("exercise_id") or b.get("example_id") or "?"
                if role != "question":
                    steps = [s for s in b.get("steps") or [] if isinstance(s, str) and s.strip()]
                    if not steps:
                        problems.append("%s/%s: no solution steps" % (cid, ref))
                    if not (b.get("answer") or "").strip():
                        problems.append("%s/%s: no answer" % (cid, ref))
                    if b.get("solution_status") == "to_author":
                        problems.append("%s/%s: solution_status is still 'to_author'" % (cid, ref))
                    text = b.get("text") or ""
                    # steps_tex/answer_tex (core/solutions/bind.py): the inline-LaTeX text the displayed
                    # text is built from, when present - text contains those, not the plain steps/answer.
                    disp_steps = b.get("steps_tex") or steps
                    disp_answer = b.get("answer_tex") or (b.get("answer") or "").strip()
                    if steps and (b.get("answer") or "").strip() and \
                            not (disp_steps[0] in text and disp_steps[-1] in text and disp_answer in text):
                        problems.append("%s/%s: the concept text must show the question with its numbered steps and "
                                        "'Answer:' (the working is only in the steps field)" % (cid, ref))
                    if PLACEHOLDER_RE.search(" ".join(steps) + " " + (b.get("answer") or "") + " " + (b.get("text") or "")):
                        problems.append("%s/%s: the working is a placeholder, not an authored solution" % (cid, ref))
                if with_images:
                    miss = (_question_ids_missing(b, concept) if role == "question"
                            else _answer_ids_missing(b, concept) if role == "answer"
                            else ids_missing(b, concept))
                    if miss:
                        problems.append("%s/%s: %s" % (cid, ref, miss))
            if not with_images:
                continue
            ids = concept.get("media_ids") or []
            nodes = [media.get(i) for i in ids]

            if role == "question":
                first = nodes[0] if nodes else None
                if not first or first.get("image_role") != "question":
                    problems.append("%s: media_ids must start with the question image (image_role 'question')" % cid)
                if first and not (first.get("render_source") or {}).get("code_url"):
                    problems.append("%s: image %s has no render_source.code_url (Manim code)" % (cid, first.get("id")))
                _check_no_hints(problems, cid, first, blocks)
                continue

            if role == "answer":
                last = nodes[-1] if nodes else None
                if not last or last.get("image_role") != "solution":
                    problems.append("%s: media_ids must end with the solution image (image_role 'solution')" % cid)
                before_last = [n for n in nodes[:-1] if n]
                if need_video and not any(n.get("type") == "video" for n in before_last):
                    problems.append("%s: media_ids needs the question video before the solution image" % cid)
                for b in blocks:
                    for i in b.get("solution_image_media_ids") or []:
                        if (media.get(i) or {}).get("image_role") != "solution":
                            problems.append("%s: %s in solution_image_media_ids is not a solution image "
                                            "(image_role 'solution')" % (cid, i))
                for n in [last] + [x for x in nodes[:-1] if x and x.get("image_role") == "solution"]:
                    if n and not (n.get("render_source") or {}).get("code_url"):
                        problems.append("%s: image %s has no render_source.code_url (Manim code)" % (cid, n.get("id")))
                continue

            # legacy: one concept holds both the question and solution card(s)
            first = nodes[0] if nodes else None
            last = nodes[-1] if nodes else None
            if not first or first.get("image_role") != "question":
                problems.append("%s: media_ids must start with the question image (image_role 'question')" % cid)
            if not last or last.get("image_role") != "solution" or last is first:
                problems.append("%s: media_ids must end with the solution image (image_role 'solution')" % cid)
            middle = [n for n in nodes[1:-1] if n]
            if need_video and not any(n.get("type") == "video" for n in middle):
                problems.append("%s: media_ids needs the question video between the question and solution "
                                "images" % cid)
            for b in blocks:
                for i in b.get("solution_image_media_ids") or []:
                    if (media.get(i) or {}).get("image_role") != "solution":
                        problems.append("%s: %s in solution_image_media_ids is not a solution image "
                                        "(image_role 'solution')" % (cid, i))
            # the question and solution images, and a solution continued on a second card, all carry Manim code
            for n in [first, last] + [x for x in nodes[1:-1] if x and x.get("image_role") == "solution"]:
                if n and n.get("image_role") in ("question", "solution") and not (n.get("render_source") or {}).get("code_url"):
                    problems.append("%s: image %s has no render_source.code_url (Manim code)" % (cid, n.get("id")))
            _check_no_hints(problems, cid, first, blocks)
    return problems


def _check_no_hints(problems, cid, first, blocks):
    """The question image's own visible text (title, description, labels, ...) carries no hint/answer
    words, once the question text itself (exempt) is stripped out."""
    if not first or first.get("image_role") != "question":
        return
    visible = " ".join(str(first.get(f, "")) for f in ("title", "description", "accuracy_constraints")) \
        + " " + " ".join(first.get("labels") or [])
    for b in blocks:
        q = b.get("question") or ""
        if q and q in visible:
            visible = visible.replace(q, "")
    hit = HINT_WORDS_RE.search(visible)
    if hit:
        problems.append("%s: question image %s carries hint-shaped text '%s'"
                        % (cid, first.get("id"), hit.group(0)))


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    plan = json.load(open(sys.argv[1], encoding="utf-8"))
    config = json.load(open(sys.argv[2], encoding="utf-8"))
    problems = check(plan, config)
    for p in problems:
        print("-", p)
    print("%d problem(s)" % len(problems))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
