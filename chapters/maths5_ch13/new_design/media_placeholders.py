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
    "T1.C1": "Create curiosity with the hidden number box: four numbers, 28, 36, 48 and 72, come out of a box that "
             "multiplied each number that went in. Which number is the box multiplying by, is there only one, and "
             "which numbers went in? A short story with Robby and Deeku, no explanation, ending on an open question "
             "that leads to the Hidden Number Box tool.",
    "T1B.C1": "Explain that a number the box multiplies by is a factor of every number that comes out, that the "
              "numbers that come out are multiples of it, that a factor that fits a whole list is a common factor, "
              "and that the product of two or more factors gives a multiple.",
    "T2.C1": "Show how to make every array of a number with square tiles, write each array as a multiplication and "
             "list the factors of the number.",
    "T2.C2": "Show that a number is a multiple of each of its factors, including 1 and the number itself, and that "
             "1 and the number itself are always factors.",
    "T2.C3": "Show that a number with only one array has only two factors, 1 and itself, and is called a prime "
             "number, as the book names 13 and 37.",
    "T3.C1": "Show how two animals jumping from 0 touch common multiples on a number line, how the first common "
             "multiple is found, and how to find them from two lists of multiples.",
    "T3.C2": "Show the pattern in common multiples: each is the first common multiple more than the one before, "
             "they never end, and when one number is a multiple of the other they are the multiples of the bigger "
             "number.",
    "T4.C1": "Show that a jump of n steps from 0 lands on a number exactly when n is a factor of it, with Mowgli "
             "jumping along the trail and skipping some places.",
    "T4.C2": "Show how to find the common factors of two numbers by listing the factors of each and picking the "
             "ones in both lists, and that 1 is always a common factor.",
    "T5.C1": "Show how to check a statement about factors and multiples: one example that fails shows it is false, "
             "and a true statement needs a reason that it always works.",
    "T5.C2": "Show how to tell whether a number is divisible by 2, by 5 and by 10 by checking which are its "
             "factors, and why a number divisible by 10 is divisible by 2 and 5.",
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
