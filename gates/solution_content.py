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
     last an image with image_role "solution", at least one video between (images mode);
  3. both images carry `render_source` (Manim code the editor can open), and the question image's own
     fields hold no hint, answer or solution words (the question text itself is exempt, as in
     theorem_variant rule 2).
The scene files, the manifest and the numbers in the answer are checked locally by core/solutions/check.py,
which build.py runs: a plan alone does not carry them.

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
    and last of the concept's media_ids. '' when fine."""
    ids = concept.get("media_ids") or []
    if not ids:
        return ""
    if block.get("image_media_id") != ids[0]:
        return "image_media_id must be the question image (first media_id)"
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
            for b in blocks:
                ref = b.get("coverage_id") or b.get("exercise_id") or b.get("example_id") or "?"
                steps = [s for s in b.get("steps") or [] if isinstance(s, str) and s.strip()]
                if not steps:
                    problems.append("%s/%s: no solution steps" % (cid, ref))
                if not (b.get("answer") or "").strip():
                    problems.append("%s/%s: no answer" % (cid, ref))
                if b.get("solution_status") == "to_author":
                    problems.append("%s/%s: solution_status is still 'to_author'" % (cid, ref))
                text = b.get("text") or ""
                if steps and (b.get("answer") or "").strip() and \
                        not (steps[0] in text and steps[-1] in text and b["answer"].strip() in text):
                    problems.append("%s/%s: the concept text must show the question with its numbered steps and "
                                    "'Answer:' (the working is only in the steps field)" % (cid, ref))
                if PLACEHOLDER_RE.search(" ".join(steps) + " " + (b.get("answer") or "") + " " + (b.get("text") or "")):
                    problems.append("%s/%s: the working is a placeholder, not an authored solution" % (cid, ref))
                if with_images and ids_missing(b, concept):
                    problems.append("%s/%s: %s" % (cid, ref, ids_missing(b, concept)))
            if not with_images:
                continue
            ids = concept.get("media_ids") or []
            nodes = [media.get(i) for i in ids]
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
            for n in (first, last):
                if n and n.get("image_role") in ("question", "solution") and not (n.get("render_source") or {}).get("code_url"):
                    problems.append("%s: image %s has no render_source.code_url (Manim code)" % (cid, n.get("id")))
            if first and first.get("image_role") == "question":
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
    return problems


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
