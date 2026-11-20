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
    "T1.C1": "Create curiosity with Raghav's morning yoga: he looks at the wall clock before and after. How much time went by? "
             "A short story, no explanation, ending on an open question that leads to the Yoga Clock tool.",
    "T1B.C1": "Show how to find the time elapsed between two clock times by counting up in easy hops: minutes within an hour, whole "
              "hours, or up to the next whole hour and then the rest.",
    "T1B.C2": "Explain how to compare times taken that are given in hours and minutes: compare the hours first, then the minutes.",
    "T2.C1": "Show the 12-hour format (a.m., p.m.) and the 24-hour format, both ways: a morning time keeps its digits, a p.m. time "
             "adds 12 to the hour, the minutes never change.",
    "T2.C2": "Show how to find the time between two 24-hour times: hop to the next whole hour, then whole hours, then the rest.",
    "T3.C1": "Introduce seconds as a smaller unit through the school race: 1 minute = 60 seconds, a race time such as 01:48 is 1 "
             "minute 48 seconds, and the least time wins.",
    "T3.C2": "Show how to choose seconds or minutes for an activity by asking whether it is over in less than 1 minute.",
    "T4.C1": "Show how to read the seconds hand: each number is 5 seconds, count from the start to the end, past 12 if the hand "
             "goes round, and the minute hand moves on after a full round.",
    "T4.C2": "Show how to draw the seconds hand after a number of seconds: change the seconds into steps of 5 and count on, and "
             "60 seconds is one full round.",
    "T5.C1": "Show how to change hours and minutes to minutes and back, with a double number line: multiply by 60, or find the "
             "whole groups of 60.",
    "T5.C2": "Show how to change minutes and seconds to seconds and back, with a double number line, in the same way.",
    "T6.C1": "Show how to find the time after a start time: add the hours, then hop to the next whole hour and add the minutes left.",
    "T6.C2": "Show how to find the time before a finish time by going back the hours and then the minutes in easy hops.",
    "T6.C3": "Show how to find a time when the time passes 12 noon or midnight, using the 24-hour clock and taking 24 away from a "
             "time above 24:00 hours.",
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
