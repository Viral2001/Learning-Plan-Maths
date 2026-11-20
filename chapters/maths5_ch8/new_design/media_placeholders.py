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
    "T1.C1": "Create curiosity with Anu's list of weights: can an iron almirah weigh 40 g? A short story, no explanation, "
             "ending on an open question that leads to the Weight Check tool.",
    "T1B.C1": "Explain that grams are for light things and kilograms for heavy things, that 1 kg is 1,000 g, and that the "
              "number and the unit are read together.",
    "T2.C1": "Show how to read a weighing scale with a needle: start at 0, find the last label the needle has passed and "
             "count the small marks after it.",
    "T2.C2": "Show how to find what one small mark stands for, the weight between two labels divided by the number of "
             "gaps, and why the same needle spot reads differently on different scales.",
    "T3.C1": "Show that the same weight can be written in kilograms and in grams, that 1 kg is 1,000 g, and how a double "
             "number line links the two.",
    "T3.C2": "Show how to change a weight in kg and g to grams, keeping the g part in three places, and how to change "
             "grams to kg and g by taking out whole thousands.",
    "T4.C1": "Explain how to compare weights given in different units by changing both to grams, and how to put weights "
             "in order.",
    "T5.C1": "Show that 1 g is 1,000 mg and that changing g to mg works like changing kg to g.",
    "T5.C2": "Show the quintal and the tonne: 100 kg is 1 quintal, 10 quintals is 1 tonne, and 1 tonne is 1,000 kg.",
    "T5.C3": "Show that a weight n times as heavy is found by multiplying and the smaller weight by dividing.",
    "T6.C1": "Show three ways to add weights in kg and g, and why 1,000 g is exchanged for 1 kg.",
    "T6.C2": "Show three ways to subtract weights in kg and g, and why 1 kg is broken into 1,000 g when the g on top are "
             "fewer.",
    "T7.C1": "Show how to multiply a weight in kg and g by a whole number, kg and g separately or in grams.",
    "T7.C2": "Show how to share a weight in kg and g equally, kg and g separately or in grams, and how to check it.",
    "T8.C1": "Show how to find the cost of a weight in kg and g from the cost of 1 kg, using whole kilograms and a part "
             "of a kilogram.",
    "T8.C2": "Show how a double number line scales two linked quantities by the same number.",
    "T9.C1": "Explain capacity and when to use millilitres and when to use litres, with 1 l = 1,000 ml.",
    "T10.C1": "Show how to change litres to millilitres and back, and how to find how many small containers fill a big one.",
    "T10.C2": "Show how to write a capacity in l and ml in millilitres and back, how to read a container's scale, and how "
              "to add the capacities of containers.",
    "T11.C1": "Explain how to compare capacities given in l and ml by changing both to ml.",
    "T11.C2": "Show how to add and subtract capacities in l and ml, the same ways as for weights.",
    "T12.C1": "Show how to multiply and share capacities in l and ml, and how to find how many small containers fill a big one.",
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
