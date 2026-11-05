# -*- coding: utf-8 -*-
"""Name a book question's "Questions: <...>" topic and its own question/answer concept titles, from the
free-text label the author already writes (FIO(book=...) in concept_plan.py, or layout_spec.json's
"name"). Shared by core/qt.py (building a chapter from source) and core/question_layout_live.py
(restructuring an already-live chapter) so every class names these the same way.

    category        topic ("Questions: ...")       question concept        answer concept
    exercise        Exercise Set 5.1               Exercise Set 5.1: Q1    Exercise Set 5.1: Ans1
    figure_it_out   Figure it Out 5.1               Figure it out: Q1      Figure it out: Ans1
    example         Example                        Example 1: Q           Example 1: Ans
    let_us_do       Let us do                       Let us do: Q1          Let us do: Ans1
    other           <the label's own heading>       <heading>: Q1         <heading>: Ans1

One topic per (category, topic title) found under a teaching topic: a topic with both an Example
and a Figure it Out question gets two Questions topics, each holding only its own category's
concepts, in book order. core/qt.py (topic_prefix="Questions") also splits each book question itself
into a question concept (the question card only) and a sibling answer concept (the video and the
solution card(s)); concept_title()'s `role` picks "Q"/"Qn" or "Ans"/"Ansn" for the two halves.
"example" concepts carry the book's own example number instead of a running count, so they need no
sequence number in the concept title.
"""
from __future__ import annotations

import re

_NUM = r"(\d+(?:\.\d+)*)"
_EXERCISE_RE = re.compile(r"^\s*Exercise\s*" + _NUM, re.IGNORECASE)
_FIGURE_RE = re.compile(r"^\s*Figure\s+it\s+Out\b\s*\(?\s*" + _NUM + r"?", re.IGNORECASE)
_EXAMPLE_RE = re.compile(r"^\s*Example\s*" + _NUM, re.IGNORECASE)
_LET_US_DO_RE = re.compile(r"^\s*Let\s+[Uu]s\s+[Dd]o\b", re.IGNORECASE)
_SECTION_NO_RE = re.compile(r"^(\d+\.\d+)")


def _section_no(coverage_id):
    """'5.1.FiO3' -> '5.1'; None if the coverage id has no chapter.section prefix."""
    m = _SECTION_NO_RE.match(coverage_id or "")
    return m.group(1) if m else None


def _heading(label):
    """Drop a trailing ", Qn" / "(..., question n)" counter, then everything after the first colon,
    leaving the label's own heading as printed - "Try This (Taxicab Numbers): 4104 as two cubes" ->
    "Try This (Taxicab Numbers)"."""
    s = re.sub(r",?\s*question\s*\d+\)?\s*$", "", label, flags=re.IGNORECASE)
    s = re.sub(r",?\s*Q\d+\s*$", "", s, flags=re.IGNORECASE)
    s = s.split(":", 1)[0] if ":" in s else s
    return s.strip().rstrip(",").strip()


def classify(label, coverage_id=None):
    """(category, topic_suffix, concept_prefix) from a book label like "Exercise 5.1, Q3" or
    "Figure it Out (division), Q3". `coverage_id` (the book's own "<chapter>.<section>..." id) backs
    up the section number when the label text does not carry one itself."""
    label = (label or "").strip()

    m = _EXERCISE_RE.match(label)
    if m:
        name = "Exercise Set %s" % m.group(1)
        return "exercise", name, name

    m = _FIGURE_RE.match(label)
    if m:
        num = m.group(1) or _section_no(coverage_id)
        return "figure_it_out", ("Figure it Out %s" % num if num else "Figure it Out"), "Figure it out"

    m = _EXAMPLE_RE.match(label)
    if m:
        return "example", "Example", "Example %s" % m.group(1)

    if _LET_US_DO_RE.match(label):
        return "let_us_do", "Let us do", "Let us do"

    heading = _heading(label) or "Questions"
    return "other", heading, heading


def topic_title(topic_suffix):
    return "Questions: %s" % topic_suffix


def concept_title(category, concept_prefix, seq, role="question"):
    """seq is this question's 1-based position within its group, in book order. "example" concepts
    already carry their own number in `concept_prefix` (from the book's own "Example N") and need no
    running count. role="question" titles end in "Q"/"Qn"; role="answer" mirrors it exactly with
    "Ans"/"Ansn" instead, for the paired concept that carries the worked solution."""
    tag = "Q" if role == "question" else "Ans"
    if category == "example":
        return "%s: %s" % (concept_prefix, tag)
    return "%s: %s%d" % (concept_prefix, tag, seq)
