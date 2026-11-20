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
    "T1.C1": "Create curiosity with the Statue game: four children keep turning around and freeze when Statue is called, "
             "and they are not all facing the same way. A short story, no explanation, ending on an open question that "
             "leads to the Statue Turn tool.",
    "T1B.C1": "Explain that a child who turns until facing the starting way again has made a full turn, and a child who "
              "turns until facing the opposite way has made a half turn, with the minute hand as another full turn.",
    "T2.C1": "Show that two half turns, or four quarter turns, make a full turn and that two quarter turns make a half "
             "turn, on the giant wheel.",
    "T2B.C1": "Show how to compare the greatest turn of an everyday object with a quarter turn, as less than, equal to or "
             "more than a quarter turn.",
    "T3.C1": "Show that a quarter turn makes a right angle, less than a quarter turn an acute angle and more than a quarter "
             "turn but less than a half turn an obtuse angle, with the straws and the paper fan.",
    "T3.C2": "Show that two quarter turns make a half turn, a straight angle, and that a turn of 3/4 is more than a "
             "straight angle.",
    "T4.C1": "Show how a circle folded into 8 equal parts measures turns in eighths, with 2/8 = 1/4, 4/8 = 1/2, 6/8 = 3/4 "
             "and 8/8 a full turn.",
    "T4.C2": "Show how a circle folded into 6 equal parts measures turns in sixths, and that half of a 1/6 turn is a 1/12 "
             "turn.",
    "T5.C1": "Show how to measure an angle by laying the turn pieces side by side from the first line, adding their "
             "fractions and naming the angle.",
    "T5B.C1": "Show how to draw an angle for a given turn by laying the pieces of the turn from a given line and drawing "
             "along the last edge.",
    "T6.C1": "Show that a full turn of the minute hand is 60 minutes, so 5 minutes is a 1/12 turn, 15 minutes a 1/4 turn "
             "and so on, and how to find where the hand stops from where it starts.",
    "T7.C1": "Explain that the way the hands of a clock move is clockwise and the opposite way is anti-clockwise, and how "
             "to tell the direction of a quarter turn.",
    "T7.C2": "Show how to find the direction faced after turns of right angles, clockwise or anti-clockwise, on a compass "
             "of North, East, South and West.",
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
