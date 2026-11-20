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
    "T1.C1": "Create curiosity with the Siberian Crane that flies from Siberia to India and the poem of the four little "
             "chicks: how do birds, and people, find their way? A short story, no explanation, ending on an open "
             "question that leads to the Face the Rising Sun tool.",
    "T1B.C1": "Show that facing the rising Sun is facing east, that the left hand then points north, the right hand "
              "south and west is behind, and name the four directions on the compass rose.",
    "T2.C1": "Show how to read directions on a picture with a compass: north at the top, east to the right, and find "
             "what lies north, south, east or west of an object.",
    "T2.C2": "Show that the direction of a thing is said from a person standing at a place, for example the centre of "
             "a room, and that if one thing is east of another then the other is west of it.",
    "T3.C1": "Show how to read a street map: roads and places seen from above, the compass, the stops and a dotted "
             "route.",
    "T3.C2": "Show how a right turn or a left turn changes the direction a vehicle is driving: right turn from north "
             "gives east, left turn from north gives west.",
    "T4.C1": "Show how to read a metro map: coloured lines are routes, circles are stations, a capsule with two "
             "coloured dots is an interchange where one can change lines.",
    "T4.C2": "Show how to ride one line, change at an interchange and count the stations between two stations, not "
             "counting the two ends.",
    "T5.C1": "Show how to make a map with a key: a symbol for each thing, a key that says what each symbol means, and "
             "a red dot for a hidden object.",
    "T6.C1": "Show how a path on a grid of 1 cm squares is a list of distances in cm and directions.",
    "T6.C2": "Show that several routes reach the same point and that the shortest routes never take a step away from "
             "it.",
    "T7.C1": "Show how to read a position on the grid: start from 0, move east to the column, then north to the row, "
             "and write (column,row).",
    "T7.C2": "Show that the order of the two numbers matters: the first is the column and the second is the row, so "
             "two different pairs name two different places.",
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
