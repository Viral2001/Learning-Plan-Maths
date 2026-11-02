# -*- coding: utf-8 -*-
"""Authoring helpers shared by the topic files and the tool file: plain dicts that build.py reads directly."""
from __future__ import annotations

def WE(q, steps, answer, *, ncert=(), fact=None, expect=None):
    """A worked example, one step per line.

    fact    the facts.py entry name that independently recomputes this answer (TODO: write facts.py
            once you have real numbers; a template has none to recompute)
    expect  the value the answer text states, checked against fact's result
    """
    return {"q": q, "steps": list(steps), "answer": answer, "ncert": list(ncert), "fact": fact, "expect": expect}


def FIO(cov, book, question, steps, answer, *, expect=None, tool=None):
    """A Figure It Out / Try This item, homed in the DOER concept of the topic whose idea it practises.
    cov is its coverage id (must appear in content.NCERT_ITEMS). tool: optional key of the parent
    topic's own tool when that tool fits this question; it is linked from the Figure it Out concept."""
    return {"cov": cov, "book": book, "question": question, "steps": list(steps), "answer": answer,
            "expect": expect, "tool": tool}


def A(key, name, bloom, objective, *, textbook=(), teach=(), examples=(), ncert=(), key_terms=(),
      misconceptions=(), video_focus=(), enrichment=False, minutes=10, role=None):
    """A teaching concept.

    textbook      the book's own lines, quoted verbatim (dashes normalised to −, commas or "to")
    teach         the plan's own teaching lines; put the prediction step first (predict, then reveal)
    enrichment    True means build.py emits NO objective for this concept (user rule: enrichment
                  carries no objective)
    role          build.py auto-derives gates/skeleton.py's `source_segment_role` ("hook" when
                  "HOOK" is in video_focus, otherwise none) - set this explicitly only to override
                  that, e.g. role="try_it" for the framing topic's second (free-try) concept.
    """
    return {"key": key, "kind": "teach", "name": name, "bloom": bloom, "objective": objective,
            "textbook": list(textbook), "teach": list(teach), "examples": list(examples), "ncert": list(ncert),
            "key_terms": list(key_terms), "misconceptions": list(misconceptions), "video_focus": list(video_focus),
            "enrichment": enrichment, "minutes": minutes, "role": role}


def DOER(key, name, tool, bloom, objective, recap, *, items=(), textbook=(), ncert=(), misconceptions=(),
         enrichment=False, role=None):
    """The LAST concept of an instructional topic: the recap, this idea's exercises, then exactly ONE tool
    (from TOOLS below, by its dict key). Never put more than one tool on a topic (tool-pruning policy:
    keep a tool only where the manipulation IS the concept).

    name    must start with "Pull it together and do it: " or "Practice: " (gates/skeleton.py's
            `doer_name_prefixes`) unless chapter.config.json overrides that list.
    role    build.py auto-derives source_segment_role "doer" for every DOER; override only for the
            framing topic's free-try concept (role="try_it", still built with DOER so it gets a tool).
    """
    return {"key": key, "kind": "doer", "name": name, "tool": tool, "bloom": bloom, "objective": objective,
            "recap": list(recap), "items": list(items), "textbook": list(textbook), "ncert": list(ncert),
            "misconceptions": list(misconceptions), "enrichment": enrichment, "role": role}


def TOPIC(key, module, name, sections, bloom, objective, summary, concepts, *, topic_type="instructional",
          key_terms=()):
    """topic_type: 'framing' (the chapter opener, exactly one), 'instructional' (the normal case,
    ends in a DOER), or 'summary' (the chapter recap, exactly one). core.qt only inserts a QT
    sibling after an 'instructional' topic; framing and summary topics are excluded by design."""
    return {"key": key, "module": module, "name": name, "ncert_sections": list(sections), "bloom": bloom,
            "objective": objective, "summary": summary, "concepts": list(concepts), "topic_type": topic_type,
            "key_terms": list(key_terms)}


# ---------------------------------------------------------------------------
# TOOLS: one "spec + placeholder" tool per DOER concept that has one, keyed by the DOER's
# `tool` field. build() returns the dict tools_spec.tool_node_builder.build_tool_node() expects.
# ---------------------------------------------------------------------------

HINT_LADDER_NOTE = ("Hints climb one rung per request or per unsuccessful try: orienting (what is the question "
                    "asking?), strategic (which move or rule applies?), specific (the next step with these "
                    "numbers), bottom-out after 3 tries (the step is shown, then a similar card follows).")


def T(tool_id, title, subtype, idea, screen, student_does, challenges, feedback, done_when, shared_state,
      misconceptions, hints):
    """One tool spec. 5 to 7 challenges; exactly 4 hints (orienting, strategic, specific, bottom-out)."""
    assert 5 <= len(challenges) <= 7, title
    assert len(hints) == 4, title
    return {"tool_id": tool_id, "title": title, "subtype": subtype, "idea": idea, "screen": screen,
            "student_does": list(student_does), "challenges": list(challenges), "feedback": list(feedback),
            "done_when": done_when, "shared_state": list(shared_state), "misconceptions": list(misconceptions),
            "hint_ladder": [{"rung": r, "text": t} for r, t in
                            zip(("orienting", "strategic", "specific", "bottom-out"), hints)]}




# ---------------------------------------------------------------------------
# Book items: book_items.json is the page-image inventory of every book question (ids as in
# content.NCERT_ITEMS), checked against the solution pages. Questions, steps and answers are read from
# it so they are never retyped; we()/fio() wrap one item as a worked example or a Figure it Out item.
# ---------------------------------------------------------------------------
import io as _io
import json as _json
import os as _os

_HERE = _os.path.dirname(_os.path.abspath(__file__))
with _io.open(_os.path.join(_HERE, "book_items.json"), encoding="utf-8") as _f:
    BOOK = {_i["id"]: _i for _i in _json.load(_f)}
with _io.open(_os.path.join(_HERE, "book_text.json"), encoding="utf-8") as _f:
    BOOK_TEXT = _json.load(_f)


def _question(it):
    q = it["question"].strip()
    parts = it.get("parts") or []
    if parts:
        q += " " + " ".join("%s) %s" % (p["label"], p["question"].strip()) for p in parts)
    return q


import re as _re


def _clean(x):
    """Equation-checker hygiene (Ch9 only): write '360 ÷ 3 = 120°' not '360° ÷ 3 = 120°' (a degree sign before ÷
    splits the chain so the checker reads '3 = 120'), and 'is 51 3/7°' not '= 51 3/7°' (a mixed number)."""
    if isinstance(x, list):
        return [_clean(i) for i in x]
    if not isinstance(x, str):
        return x
    x = _re.sub(r"(\d)\s*°(\s*[×÷])", r"\1\2", x)
    x = x.replace("60 × 2 = 120°, × 3 = 180°, × 4 = 240°, × 5 = 300°",
                  "60 × 2 = 120°, 60 × 3 = 180°, 60 × 4 = 240°, 60 × 5 = 300°")
    x = _re.sub(r"÷ (\d+) = (\d+) with remainder", r"÷ \1 gives \2 with remainder", x)
    return _re.sub(r"= (\d+ \d+/\d+)", r"is \1", x)


def _steps(it):
    return it.get("steps") or [it["answer"]]


def we(item_id, *, q=None, steps=None, answer=None):
    """One book item (worked example, in-text question, activity, Math Talk) as a worked example."""
    it = BOOK[item_id]
    return WE(_clean(q or _question(it)), _clean(steps or _steps(it)), _clean(answer or it["answer"]), ncert=[item_id])


def fio(item_id, *, tool=None, book=None, question=None, steps=None, answer=None):
    """One book item as a Figure it Out item in the topic's DOER (core.qt moves it to the practice topic).
    question/steps/answer override the inventory text where content.py records a book-error choice."""
    it = BOOK[item_id]
    return FIO(item_id, book or it["book_label"], _clean(question or _question(it)), _clean(steps or _steps(it)),
               _clean(answer or it["answer"]), tool=tool)


_ALL = object()


def book(section, heading=None, *, start=0, stop=None):
    """The book's own lines for one section's sub-heading, verbatim. heading=None is the untitled opening part
    of the section; heading=_ALL takes every sub-heading."""
    for s in BOOK_TEXT["sections"]:
        if s["number"] != section:
            continue
        lines = []
        for sub in s["subsections"]:
            if heading is _ALL or sub["heading"] == heading:
                lines += sub["textbook_lines"]
        import re as _re
        lines = [_re.sub(r'\s*[–—]\s*', ', ', l) for l in lines]
        return lines[start:stop]
    raise KeyError(section)
