# -*- coding: utf-8 -*-
"""Placeholder video documents for the video slots that have no script file.

User decision (2026-11-05, 'approve and upload'): this chapter's LP carries PLACEHOLDERS for its media; the scripts and the videos are made
in other folders. build.py (chapter.config "media_placeholders": true) calls with_stubs(), which adds one stub script
document per slot of video_worklist.json that has no file in video_scripts/. core.video_script.node.video_node then
builds the usual placeholder video node from it (id, title, description, planned_url, build_status "placeholder"),
with an empty beat list: no script has been written, so nothing here can be rendered until the real script exists.
A real script file for a slot always wins over its stub."""
from __future__ import annotations

# The plan's purpose for each video (priority_doc.md section B), by authored concept key.
DOC_PURPOSE = {
    "T1.C1": "Create curiosity with woven baskets and a paper mat made of strips: what pattern does the weave make? A short "
             "story, no explanation, ending on an open question that leads to the Mat Weaver tool.",
    "T1B.C1": "Show how to describe a weave row in words with over and under steps and the word repeat, and that the next "
              "row swaps over and under.",
    "T1B.C2": "Show that rows can start one step later each time and that the pattern repeats when a row is the same as "
              "Row 1.",
    "T2.C1": "Explain that shapes with all sides equal are regular shapes, with a square, a pentagon and a rectangle that "
             "is not regular.",
    "T2.C2": "Show that shapes fit round a point when their corners fill the space with no gap and no overlap, and that "
             "such shapes tessellate.",
    "T3.C1": "Show that tiles of two shapes can take turns in a repeating pattern and that the same shapes meet at every "
             "point.",
    "T4.C1": "Explain isosceles triangles: 2 equal sides and 2 equal angles, checked by folding.",
    "T4.C2": "Explain equilateral triangles (3 equal sides and angles) and scalene triangles (no equal sides).",
    "T5.C1": "Explain kites: adjacent sides equal, with a kite and a parallelogram of the same sides to compare.",
    "T5.C2": "Explain parallelograms (opposite sides equal) and rectangles as special parallelograms with right angles.",
    "T6.C1": "Show the seven tangram pieces sorted by number of sides, with their sides and angles.",
    "T7.C1": "Show square, rectangle, rhombus and parallelogram by their sides and angles and that one description can fit "
             "more than one shape.",
    "T8.C1": "Show that joining the ends of two diameters of a circle makes a rectangle, and a square when the diameters "
             "cross at a right angle.",
    "T8.C2": "Show how to join points on a circle one after another until the path comes back to the start, with a "
             "12 point circle.",
    "T9.C1": "Show how three views of a cube tell which faces are opposite and how a net folds.",
    "T9.C2": "Show how to count the small cubes of a big painted cube by corners, edges, faces and inside.",
    "T10.C1": "Show how to solve an arrangement puzzle from clues, placing the surest shape first.",
    "T11.C1": "Show how to count the faces and corners of a solid and what a vertex is, with a box.",
    "T11.C2": "Show how to count the edges of a solid without missing or repeating any: count the sides of all faces and "
              "halve.",
}

NOT_AUTHORED = "placeholder: the script and the video are made in the media folders"


def _concept_key(slot_key):
    parts = slot_key.split(".")          # c5x.T2.C3.r.thousands -> T2.C3
    return "%s.%s" % (parts[1], parts[2])


def _steps_text(steps, answer):
    return " ".join(["%d. %s" % (i, s) for i, s in enumerate(steps, 1)] + ["Answer: %s" % answer])


def stub(slot, info):
    c = info["concept"]
    kind = slot["kind"]
    ckey = _concept_key(slot["key"])
    if kind == "hook":
        title = c["name"]
        description = "Hook video: " + DOC_PURPOSE.get(ckey, c["name"])
        notes = " ".join(c.get("teach") or [])
        why = DOC_PURPOSE.get(ckey, c["name"])
        hold = []
    elif kind == "worked":
        ex = c["examples"][0]
        title = c["name"]
        purpose = DOC_PURPOSE.get(ckey) or c.get("objective") or c["name"]
        description = "Concept video: %s It works this example: %s" % (purpose, ex["q"])
        notes = " ".join(c.get("teach") or []) + " " + _steps_text(ex["steps"], ex["answer"])
        why = purpose
        hold = [ex["answer"]]
    else:                                  # exercise: one book question
        it = (slot.get("items") or [{}])[0]
        title = (slot.get("source") or [slot["key"]])[0]
        description = "Question video: %s" % it.get("question", title)
        notes = _steps_text(it.get("steps") or [], it.get("answer", ""))
        why = "Solve the book question step by step by the method of the idea it practises."
        hold = [it.get("answer", "")]
    script = {"kind": kind, "unlock": slot.get("unlock", "always"), "placement": slot.get("placement", "after"),
              "source": list(slot.get("source") or []), "why": why, "hold_back": hold, "beats": [],
              "status": NOT_AUTHORED}
    return {"key": slot["key"], "title": title, "description": description, "teaching_notes": notes.strip(),
            "video_script": script, "_photo_lib": {}, "_book_rules": {}}


def with_stubs(slots, scripts, concept_lookup):
    """scripts + a stub document for every slot that has no script file."""
    out = dict(scripts)
    for s in slots:
        if s["key"] in out:
            continue
        info = concept_lookup.get(_concept_key(s["key"]))
        if info is None:
            continue
        out[s["key"]] = stub(s, info)
    return out
