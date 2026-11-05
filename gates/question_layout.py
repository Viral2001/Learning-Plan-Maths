# -*- coding: utf-8 -*-
"""The question layout: every concept topic is followed by its own "Questions: <topic>" topic, and every book
question lives there, one concept per question.

Runs when chapter.config.json has a truthy `"question_layout"` (the chapter_template sample sets it). A chapter
built before this layout existed keeps its old config and is untouched.

    concept topic -> Questions topic (one concept per solved example, exercise item or answerable prompt)
                  -> next concept topic -> its Questions topic ...

Checks, on the plan:
  1. a Questions topic (source_type "exercise" or "question_topic") comes directly after the concept topic it
     practises and is named "Questions: <that topic's name>";
  2. no question block (a worked_example carrying item_kind, or an exercise block) is left inside a concept
     topic: teaching concepts keep their own LP-authored examples, the book's questions all moved out;
  3. every concept of a Questions topic holds at least one question block;
  4. scope: when the build passes `config["book_item_kinds"]` ({book id: kind}, from content.NCERT_ITEMS), each
     item whose kind is in `config["question_scope"]` (default example / exercise / prompt) is mapped to a
     concept of a Questions topic. Kinds outside the scope (Math Talk discussion, plain text) are not forced.

    python -B question_layout.py <plan.json> <chapter.config.json>
"""
from __future__ import annotations

import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from core import question_naming as QN  # noqa: E402

QT_SOURCE_TYPES = ("exercise", "question_topic")
QUESTION_KINDS = ("exercise", "exercise_question")
DEFAULT_SCOPE = ("example", "exercise", "prompt")


def walk_topics(plan):
    for module in plan.get("modules") or []:
        for segment in module.get("segments") or []:
            for topic in segment.get("topics") or []:
                yield topic


def is_question_block(b):
    kind = b.get("block_kind")
    return kind in QUESTION_KINDS or (kind == "worked_example" and bool(b.get("item_kind")))


def _expected_names(t, base_name):
    """Valid topic_name values for a Questions topic that practises the concept topic named
    `base_name`: the old "Questions: <base>" form (every pre-category-split chapter), or, when every
    question block inside carries a book label and they all agree, the category-based form
    (core/question_naming.py) a topic-prefix="Questions" build now produces, e.g. "Questions: Exercise
    Set 5.1". A topic may legitimately be one of several Questions topics after the same base topic
    (one per category), so this does not require the base's exact name alone."""
    names = {"Questions: %s" % base_name}
    labels = []
    for c in t.get("concepts") or []:
        block = next((b for b in c.get("content") or [] if is_question_block(b)), None)
        if block is None:
            continue
        cov = block.get("coverage_id") or next(iter(block.get("ncert_refs") or []), None)
        labels.append(QN.classify(block.get("book_number") or "", cov))
    if labels and len({(cat, suf) for cat, suf, _ in labels}) == 1:
        names.add(QN.topic_title(labels[0][1]))
    return names


def check(plan, config=None):
    config = config or {}
    if not config.get("question_layout"):
        return []
    problems = []
    topics = list(walk_topics(plan))
    in_qt = {}                                    # concept id -> True for concepts of a Questions topic
    for i, t in enumerate(topics):
        tid = t.get("topic_id")
        is_qt = t.get("source_type") in QT_SOURCE_TYPES
        if is_qt:
            # A run of one or more Questions topics (one per book category) can follow one concept
            # topic, so walk back over any already-seen Questions topics to find the one they practise.
            j = i - 1
            while j >= 0 and topics[j].get("source_type") in QT_SOURCE_TYPES:
                j -= 1
            base = topics[j] if j >= 0 else None
            if base is None or base.get("topic_type") in ("framing", "summary"):
                problems.append("%s: a Questions topic must come directly after the concept topic it practises"
                                % tid)
            else:
                expected = _expected_names(t, base.get("topic_name"))
                if t.get("topic_name") not in expected:
                    problems.append("%s: named %r, want one of %r" % (tid, t.get("topic_name"),
                                                                        sorted(expected)))
            for c in t.get("concepts") or []:
                in_qt[c.get("concept_id")] = True
                if not any(is_question_block(b) for b in c.get("content") or []):
                    problems.append("%s: %s is in a Questions topic but holds no question" % (tid, c.get("concept_id")))
        else:
            for c in t.get("concepts") or []:
                stray = [b.get("book_number") or b.get("exercise_id") or b.get("coverage_id") or "?"
                         for b in c.get("content") or [] if is_question_block(b)]
                if stray:
                    problems.append("%s: %s still holds book question(s) %s; each question belongs in its own concept "
                                    "of the Questions topic after this one" % (tid, c.get("concept_id"), stray[:4]))

    kinds = config.get("book_item_kinds") or {}
    scope = set(config.get("question_scope") or DEFAULT_SCOPE)
    cov = (plan.get("source_metadata") or {}).get("ncert_coverage") or {}
    for item, kind in sorted(kinds.items()):
        if kind not in scope:
            continue
        cids = cov.get(item) or []
        if not cids:
            problems.append("book item %r (%s) is not mapped to any concept" % (item, kind))
        elif not any(in_qt.get(c) for c in cids):
            problems.append("book item %r (%s) is not in a Questions topic (its concept(s): %s)"
                            % (item, kind, cids[:3]))
    return problems


if __name__ == "__main__":
    plan = json.load(open(sys.argv[1], encoding="utf-8"))
    config = json.load(open(sys.argv[2], encoding="utf-8"))
    config.setdefault("question_layout", True)
    out = check(plan, config)
    for p in out:
        print("-", p)
    print("%d problem(s)" % len(out))
    sys.exit(1 if out else 0)
