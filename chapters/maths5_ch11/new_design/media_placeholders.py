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
    "T1.C1": "Create curiosity with Grandmother's quilt: she wants lace all the way round its border and has three reels. "
             "A short story, no numbers and no explanation, ending on an open question that leads to the Quilt Lace "
             "tool.",
    "T1B.C1": "Explain that the length of the border of a shape is its perimeter, found by adding all the sides, and by "
              "multiplying when all the sides are equal.",
    "T2.C1": "Show that squares, rectangles and triangles tile a surface with no gaps and no overlaps, and that "
             "circles leave gaps.",
    "T2.C2": "Show that the region the tiles cover is the area, counted in the unit of the tile, and that a different "
             "tile gives a different count for the same region.",
    "T3.C1": "Show how to compare two areas: lay one on the other when it fits inside, and count equal squares when "
             "neither fits inside the other.",
    "T3.C2": "Explain the unit square and how to count whole squares and half squares on a grid to find an area.",
    "T4.C1": "Show that shapes with the same area can have different perimeters.",
    "T4.C2": "Show that shapes with the same perimeter can have different areas, so a bigger area does not always "
             "mean a bigger perimeter.",
    "T5.C1": "Show that the area of a rectangle is its length times its breadth, by rows of patches.",
    "T5.C2": "Show that the perimeter of a rectangle is 2 times the length plus 2 times the breadth, because opposite "
             "sides are equal.",
    "T5.C3": "Show that a square is a rectangle with equal sides, so its area is length times length and its "
             "perimeter is 4 times the length.",
    "T6.C1": "Show how to find a missing side by dividing the area by the side that is known.",
    "T6.C2": "Show how to find the area of a rectangle whose side is marked in two parts: add the parts, then "
             "multiply.",
    "T7.C1": "Show how to find the perimeter of a figure of square tiles by counting its outer edges, and what happens "
             "when a tile is added along one edge or in a corner.",
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
