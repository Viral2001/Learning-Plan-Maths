# -*- coding: utf-8 -*-
"""Standalone companion to gates/solution_content.py's "every question block has non-empty steps
and answer" rule: audit a plan for question concepts with no worked solution, and (--write) apply
hand-authored fixes for the gaps found. Detection mirrors solution_content.py's own question_blocks()
and qt_part("question" vs "answer"/legacy) logic exactly, so a concept this reports clean never fails
that gate, and vice versa.

Generating the fix is not something this script does on its own - solving a book question correctly
is not a deterministic transform, so it is an explicit duty of whoever runs this, per core/qt.py's
_question_answer_blocks docstring and math_solutions/skill/references/format-rules.md rule 9: read
the question and the chapter's own content, and write an accurate, step-by-step solution in the same
style as every already-answered neighbour in the same chapter - never leave a gap unauthored, and
never hand back a placeholder or an unverified guess.

    python -B answer_checker.py <plan.json>
        List every question concept with no steps, no answer, or both - concept id, topic, ncert_refs
        and the question text, so the fix can be written straight from this output.

    python -B answer_checker.py <plan.json> --write <fills.json>
        Apply hand-authored fixes and save. fills.json: {"<concept_id>": {"steps": ["...", ...],
        "answer": "..."}, ...} - plain text, the same shape as every other concept's steps/answer
        fields. Every gap this script finds must have an entry (and fills.json may not contain any
        extra ids) or it refuses to write. Rebuilds that block's text/publication_text via
        latex_convert.latex_wrap(), exactly the same numbered-step-then-"Answer:" assembly core/qt.py
        itself uses, so the result matches every other answer concept in the plan.
"""
from __future__ import annotations

import io
import json
import sys
from dataclasses import dataclass, field

try:
    from .latex_convert import latex_wrap
except ImportError:                      # run as a script, package-relative import unavailable
    from latex_convert import latex_wrap

# Mirrors gates/solution_content.py's QUESTION_KINDS/question_blocks exactly (duplicated, not
# imported, the same way every gates/*.py module duplicates its own walk_topics() rather than
# reaching across the gates/core package boundary for four lines).
QUESTION_KINDS = ("exercise", "exercise_question")


def question_blocks(concept):
    for b in concept.get("content") or []:
        kind = b.get("block_kind")
        if kind in QUESTION_KINDS or (kind == "worked_example" and b.get("item_kind")):
            yield b


def walk_topics(plan):
    for module in plan.get("modules") or []:
        for segment in module.get("segments") or []:
            for topic in segment.get("topics") or []:
                yield topic


@dataclass
class Gap:
    concept_id: str
    topic_name: str
    ncert_refs: list = field(default_factory=list)
    question: str = ""
    missing: str = ""  # "steps", "answer", or "steps and answer"


def find_gaps(plan):
    gaps = []
    for topic in walk_topics(plan):
        for concept in topic.get("concepts") or []:
            if concept.get("qt_part") == "question":
                continue  # the question half never carries steps/answer by design
            for b in question_blocks(concept):
                steps = [s for s in b.get("steps") or [] if isinstance(s, str) and s.strip()]
                answer = (b.get("answer") or "").strip()
                missing_steps, missing_answer = not steps, not answer
                if not (missing_steps or missing_answer):
                    continue
                missing = ("steps and answer" if missing_steps and missing_answer
                           else "steps" if missing_steps else "answer")
                gaps.append(Gap(concept["concept_id"], topic["topic_name"],
                                 list(concept.get("ncert_refs") or []), b.get("question") or "", missing))
    return gaps


def apply_fills(plan, fills):
    """fills: {concept_id: {"steps": [...], "answer": "..."}}. Returns the list of concept ids
    patched."""
    applied = []
    for topic in walk_topics(plan):
        for concept in topic.get("concepts") or []:
            cid = concept["concept_id"]
            if cid not in fills:
                continue
            steps = list(fills[cid]["steps"])
            answer = fills[cid]["answer"]
            for b in question_blocks(concept):
                b["steps"] = steps
                b["answer"] = answer
                lines = ["%d. %s" % (i, s) for i, s in enumerate(steps, 1)]
                if answer:
                    lines.append("Answer: %s" % answer)
                text = latex_wrap("\n".join(lines))
                b["text"] = text
                b["publication_text"] = text
                applied.append(cid)
    return applied


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    plan_path = sys.argv[1]
    plan = json.load(io.open(plan_path, encoding="utf-8"))
    gaps = find_gaps(plan)

    if "--write" in sys.argv:
        fills_path = sys.argv[sys.argv.index("--write") + 1]
        fills = json.load(io.open(fills_path, encoding="utf-8"))
        gap_ids = {g.concept_id for g in gaps}
        missing_fill = gap_ids - set(fills.keys())
        if missing_fill:
            print("refusing to write: fills.json is missing these gaps: %s" % sorted(missing_fill))
            return 1
        extra = set(fills.keys()) - gap_ids
        if extra:
            print("refusing to write: fills.json has entries for concepts that aren't gaps: %s" % sorted(extra))
            return 1
        applied = apply_fills(plan, fills)
        with io.open(plan_path, "w", encoding="utf-8") as f:
            json.dump(plan, f, ensure_ascii=False, indent=1)
        print("Applied %d fix(es), wrote %s" % (len(applied), plan_path))
        return 0

    print("%d question(s) missing a worked solution:" % len(gaps))
    for g in gaps:
        print("- %s | %s | refs=%s | missing: %s" % (g.concept_id, g.topic_name, g.ncert_refs, g.missing))
        print("    Q: %s" % g.question)
    return 1 if gaps else 0


if __name__ == "__main__":
    sys.exit(main())
