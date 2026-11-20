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
    "T1.C1": "Create curiosity with Samaira and Kabir, two child reporters who ask 35 friends how many hours a day they "
             "watch TV and fill a notebook with answers. A short story, no explanation, ending on an open question that "
             "leads to the Reporter's Notebook tool.",
    "T1B.C1": "Show how to record many answers in a table with one row for each kind of answer, count each row, check "
              "that the counts add up, and use the rows for more than and less than.",
    "T2.C1": "Explain why Joseph Uncle's many items need a scale: one icon stands for 5 items, so a large number is "
             "shown with few icons, and a number is read as icons times the scale.",
    "T2.C2": "Show that the same data can use another scale, that the scale must fit every number, and that a bigger "
             "scale needs fewer icons.",
    "T3.C1": "Show how to read a pictograph with a scale and compare its rows: the most, the total, how many more and "
             "how many fewer.",
    "T4.C1": "Show how a row of squares stands up into a bar, name the vertical line, the horizontal base and the bars "
             "of a bar graph, and say how Sheela's recording differs from Raman's.",
    "T4.C2": "Show how to read the height of a bar and compare two children's bars: who has more, how many more and "
             "which activity is the same.",
    "T5.C1": "Show how to make a bar graph from a table: names on the base, a vertical line that reaches the biggest "
             "number, and each bar drawn up to its number.",
    "T5.C2": "Show a bar graph of real lengths in cm: the bar is the length, the longest is the tallest, and the "
             "difference of two heights is how much longer.",
    "T6.C1": "Show how to use a bar graph: the highest and the lowest bar, the total, a result from a given rule, and "
             "a careful prediction.",
    "T7.C1": "Show how to judge a statement about a picture by counting the children it talks about and comparing "
             "the counts, including more than half, some and no child.",
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
