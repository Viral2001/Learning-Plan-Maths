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
    "T1.C1": "Create curiosity with Shikha and Sonu at the weaving centre: one reads a sari in centimetres and the other in "
             "metres. Which unit would you use for a handkerchief, a sari or India Gate? A short story, no explanation, "
             "ending on an open question that leads to the Unit Picker tool.",
    "T1B.C1": "Explain how to choose between centimetres and metres: short things in centimetres, long things in metres, "
              "so that the number sounds sensible.",
    "T1B.C2": "Show that one length has two names, 1 m = 100 cm, with a double number line and the multiplier x100, and "
              "that a length such as 2 m 4 cm is 204 cm.",
    "T2.C1": "Explain how to compare two lengths given in different units by changing both to one unit.",
    "T2.C2": "Explain how to find how much longer one length is than another by subtracting in one unit, and how a "
             "doubled length is the half turned back.",
    "T3.C1": "Show that 1,000 m = 1 km, that kilo stands for thousand, and name the tools that measure long distances.",
    "T3.C2": "Show how to find how many equal ropes or stops fit along a distance, and where they stand.",
    "T4.C1": "Show how to find the distance between two stations by subtracting their distances from the start.",
    "T5.C1": "Show that one centimetre is divided into ten equal parts, each 1 mm, so 1 cm = 10 mm.",
    "T5.C2": "Show how to read and draw a length in cm and mm, and how to write it in mm only.",
    "T6.C1": "Show how to change a length between mm, cm, m and km with the multipliers 10, 100 and 1,000 on a double number "
             "line.",
    "T6.C2": "Show how to split a length into a part in the bigger unit and a leftover part, and how to join them back.",
    "T7.C1": "Show how to add lengths given in two units, by like units or by changing to the smaller unit, and regroup.",
    "T7.C2": "Show how to subtract lengths given in two units, by changing to the smaller unit or by regrouping.",
    "T8.C1": "Show how to multiply a length given in two units by breaking it into metres and centimetres.",
    "T8.C2": "Show how to divide a length given in two units into equal shares.",
    "T8.C3": "Show how to find the price of 1 m from the price of a longer piece, and use a double number line for cost and "
             "length.",
    "T9.C1": "Show how to estimate a length by using a known length as a reference and counting how many times it fits.",
    "T10.C1": "Show that 1 foot = 12 inches = 30 cm and 1 inch = 2 cm 5 mm, and how to read a height in feet and inches.",
    "T11.C1": "Show how to fill a sign grid one clue at a time, so that no sign repeats in a row or a column, on a small "
              "grid first.",
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
