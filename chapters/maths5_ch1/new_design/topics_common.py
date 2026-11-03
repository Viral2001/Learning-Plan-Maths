# -*- coding: utf-8 -*-
"""Authoring helpers shared by the topic files and the tool files: plain dicts that build.py reads directly.
Copied from chapter_template/concept_plan.py.template (the helper block), unchanged in behaviour."""
from __future__ import annotations


def WE(q, steps, answer, *, ncert=(), fact=None, expect=None):
    """A worked example of the PLAN's own, one step per line: it teaches inside the teaching concept, with its
    own numbers. A solved example PRINTED IN THE BOOK is not a WE; it is a question, so it is a FIO(kind="example").

    fact    the facts.py entry name that independently recomputes this answer (unused in this chapter)
    expect  the value the answer text states, checked against fact's result
    """
    return {"q": q, "steps": list(steps), "answer": answer, "ncert": list(ncert), "fact": fact, "expect": expect}


def FIO(cov, book, question, steps, answer, *, kind="exercise", q_figure=None, s_figure=None, expect=None):
    """A BOOK QUESTION, homed in the DOER concept of the topic whose idea it practises. core/qt.py moves it into
    its own concept of the "Questions: <topic>" topic that follows (question layout), with its own video, a
    question image and a solution image.

    cov       its coverage id (must appear in content.NCERT_ITEMS)
    book      its label, as the student sees it: "Example 1", "Figure it Out (division), Q3"
    kind      "exercise" a Figure it Out / exercise question (default)
              "example"  a SOLVED EXAMPLE printed in the book (the student attempts it, then watches the solution)
              "prompt"   an answerable in-text question: a Try This with an answer, "answer the following", a blank
    q_figure  one plain sentence for the diagram the QUESTION card needs: only what the question gives, no working,
              answer or hint. Leave out when the card is text only.
    s_figure  the same for the SOLUTION card (it may show the answer). Leave out when text only.
    """
    d = {"cov": cov, "book": book, "question": question, "steps": list(steps), "answer": answer, "expect": expect,
         "kind": kind}
    if q_figure:
        d["q_figure"] = q_figure
    if s_figure:
        d["s_figure"] = s_figure
    return d


def A(key, name, bloom, objective, *, textbook=(), teach=(), examples=(), ncert=(), key_terms=(),
      misconceptions=(), video_focus=(), enrichment=False, minutes=10, role=None):
    """A teaching concept.

    textbook      the book's own lines, quoted verbatim (dashes normalised to commas, colons or "to")
    teach         the plan's own teaching lines; put the prediction step first (predict, then reveal)
    examples      exactly ONE WE (one concept video); a second worked example is its own thin-extra concept
    enrichment    True means build.py emits NO objective for this concept
    role          build.py auto-derives "hook" when "HOOK" is in video_focus; set explicitly only to override
    """
    return {"key": key, "kind": "teach", "name": name, "bloom": bloom, "objective": objective,
            "textbook": list(textbook), "teach": list(teach), "examples": list(examples), "ncert": list(ncert),
            "key_terms": list(key_terms), "misconceptions": list(misconceptions), "video_focus": list(video_focus),
            "enrichment": enrichment, "minutes": minutes, "role": role}


def DOER(key, name, tool, bloom, objective, recap, *, items=(), textbook=(), ncert=(), misconceptions=(),
         enrichment=False, role=None):
    """The LAST concept of an instructional topic: the recap, this idea's book questions (`items`, FIO above),
    then at most ONE tool (from TOOLS, by its dict key; None = no tool, allowed by doer_tool_optional).

    name    must start with "Pull it together and do it: " or "Practice: " (gates/skeleton.py)
    role    build.py derives "doer"; override only for the framing topic's free-try concept (role="try_it")
    """
    return {"key": key, "kind": "doer", "name": name, "tool": tool, "bloom": bloom, "objective": objective,
            "recap": list(recap), "items": list(items), "textbook": list(textbook), "ncert": list(ncert),
            "misconceptions": list(misconceptions), "enrichment": enrichment, "role": role}


def TOPIC(key, module, name, sections, bloom, objective, summary, concepts, *, topic_type="instructional",
          key_terms=()):
    """topic_type: 'framing' (the chapter opener, exactly one), 'instructional' (ends in a DOER) or 'summary'."""
    return {"key": key, "module": module, "name": name, "ncert_sections": list(sections), "bloom": bloom,
            "objective": objective, "summary": summary, "concepts": list(concepts), "topic_type": topic_type,
            "key_terms": list(key_terms)}


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
