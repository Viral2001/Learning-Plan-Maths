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
    "T1.C1": "Create curiosity with Prem and Manu's birthday cutouts: some letters can be cut out the easy way. A short "
             "story, no explanation, ending on an open question that leads to the Fold and Cut tool.",
    "T1B.C1": "Show that a letter with a line of symmetry can be cut from folded paper by drawing half of it (one line) "
              "or a quarter of it (two lines), as in the cutouts of the letters A and H.",
    "T1B.C2": "Show how to tell the horizontal and the vertical lines of symmetry of a letter, and which letters have both.",
    "T2.C1": "Show quarter, half, three-quarter and full turns with a dot on a turning shape, as with the windmill firki.",
    "T2.C2": "Explain that a shape has rotational symmetry when it looks the same after a 1/4, 1/2 or 3/4 turn, and that a "
             "full turn does not count.",
    "T3.C1": "Explain the two tests, a fold for reflection symmetry and a turn for rotational symmetry, and that a shape "
             "can pass one, both or neither.",
    "T4.C1": "Show how to add shapes to a design so that it looks the same after a 1/2 turn and after a 1/4 turn.",
    "T4.C2": "Show how to check shapes and colours for turn symmetry and find the lines of symmetry of a design.",
    "T5.C1": "Show that the straight edge of a half print is the line of symmetry, so a half print and its copy make the "
             "whole print, and how to match a block to its half print.",
    "T5.C2": "Show that a block stamped round a middle point by equal turns makes a print that looks the same after that "
             "turn, as in the print stamped 4 times with a 1/4 turn each time.",
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
