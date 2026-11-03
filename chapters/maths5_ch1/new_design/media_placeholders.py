# -*- coding: utf-8 -*-
"""Placeholder video documents for the video slots that have no script file.

User decision (2026-11-03): this chapter's LP carries PLACEHOLDERS for its media; the scripts and the videos are made
in other folders. build.py (chapter.config "media_placeholders": true) calls with_stubs(), which adds one stub script
document per slot of video_worklist.json that has no file in video_scripts/. core.video_script.node.video_node then
builds the usual placeholder video node from it (id, title, description, planned_url, build_status "placeholder"),
with an empty beat list: no script has been written, so nothing here can be rendered until the real script exists.
A real script file for a slot always wins over its stub."""
from __future__ import annotations

# The priority doc's purpose for each video (priority_doc.md section 1), by authored concept key.
DOC_PURPOSE = {
    "T1.C1": "Connect the student's own travel experience with distance, duration and numbers through a short "
             "story-led opening, ending on an open question that leads to the Travel Explorer.",
    "T1B.C1": "Show how travel looked in earlier times and how ways of travelling and travel facilities have changed.",
    "T2.C1": "Introduce counting in thousands up to ten thousand and the new ten thousands place.",
    "T2.C2": "Explain the value of digits in the place value chart with the ten thousands column.",
    "T3.C1": "Explain reading large numbers with the number names of the chapter.",
    "T3.C2": "Explain reading large numbers that have zeros, using the number names of the chapter.",
    "T4.C1": "Explain how to write a number from its number name.",
    "T4.C2": "Explain how to place zeros when a number name skips a place.",
    "T7.C1": "Introduce the digit interchange activity and how swapping digits changes the value of a number.",
    "T7.C2": "Show how one swap makes the biggest or the smallest number.",
    "T9.C1": "Explain the nearest ten with the neighbouring marks on a number line.",
    "T9.C2": "Explain the nearest hundred and the nearest thousand with neighbouring marks on a number line.",
    "T10.C1": "Revisit the travel context of the chapter by adding the animals and modern vehicles of the book; a real "
              "concept in place of the doc's recap slot, because this pipeline has no recap video.",
    "T11.C1": "Show where large numbers appear in everyday life with story-led examples.",
    "T12.C1": "Present the river crossing puzzle, its objects and its rules exactly, and invite the student to think "
              "about a solution without changing the rules.",
    "T12.C2": "Present the pile of pebbles game exactly and show how playing small piles leads to a strategy.",
    "T12.C3": "Explain the number puzzle of Mira step by step with clear working.",
    "T13.C1": "Introduce the King's Horses challenge: the arrangement, the objects and the way the sides are counted.",
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
