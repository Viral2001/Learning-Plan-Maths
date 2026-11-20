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
    "T1.C1": "Create curiosity with Tamanna's two chocolates: can 1/3 of one chocolate be more than 1/2 of the other? "
             "A short story, no explanation, ending on an open question that leads to the Chocolate Compare tool.",
    "T1B.C1": "Explain that a fraction names a part of its own whole, and that two fractions can be compared only when "
              "the wholes are the same.",
    "T2.C1": "Show how to find a fraction of a grid by splitting the squares into equal groups.",
    "T2.C2": "Show that several small equal parts can cover the same area as a bigger fraction, as a bridge to "
             "equivalent fractions.",
    "T3.C1": "Show that n pieces of 1/n make a whole.",
    "T3.C2": "Show that pieces of different sizes make a whole and that two names for one part are equivalent "
             "fractions.",
    "T3.C3": "Show how to count how many small pieces fit in a bigger piece.",
    "T4.C1": "Show that cutting every part into more equal parts changes the names of a fraction and not the shaded "
             "area.",
    "T4.C2": "Show the pattern in equivalent fractions: the top and bottom numbers grow by the same number of times.",
    "T5.C1": "Explain how to compare fractions with the same denominator by counting equal pieces.",
    "T6.C1": "Explain how to compare fractions with the same numerator by the size of one piece.",
    "T7.C1": "Show how pieces of 1/2 join into whole parathas and how 5/2 is read as 2 1/2, with a number line.",
    "T7.C2": "Show the same with fourths and with thirds of a pizza, past one whole.",
    "T7.C3": "Explain that a fraction is greater than 1 when its top number is more than its bottom number.",
    "T8.C1": "Explain how to compare two fractions using 1 as a reference.",
    "T8.C2": "Explain how to tell which fractions are equal to 1/2.",
    "T8.C3": "Explain how to compare two fractions using 1/2 as a reference, when one is less than half and the other "
             "is more.",
    "T9.C1": "Show how to read a family relation one link at a time, as a warm-up for the relations puzzle.",
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
