# -*- coding: utf-8 -*-
"""Placeholder video documents for the video slots that have no script file.

User decision (2026-11-05, 'approve and upload'; carried to Class 5 Chapter 9): this chapter's LP carries PLACEHOLDERS for its media; the scripts and the videos are made
in other folders. build.py (chapter.config "media_placeholders": true) calls with_stubs(), which adds one stub script
document per slot of video_worklist.json that has no file in video_scripts/. core.video_script.node.video_node then
builds the usual placeholder video node from it (id, title, description, planned_url, build_status "placeholder"),
with an empty beat list: no script has been written, so nothing here can be rendered until the real script exists.
A real script file for a slot always wins over its stub."""
from __future__ import annotations

# The plan's purpose for each video (priority_doc.md section B), by authored concept key.
DOC_PURPOSE = {
    "T1.C1": "Create curiosity with Susie and Sunitha's array of coconuts, 5 rows of 7: the same 35 coconuts can be split "
             "into equal groups in two ways. A short story, no facts, ending on an open question that leads to the "
             "coconut tray.",
    "T1B.C1": "Show that one multiplication fact gives two division facts: split the total into groups by the columns or "
              "by the rows.",
    "T1B.C2": "Name the dividend, the divisor and the quotient, show that Dividend = Divisor × Quotient, and show that "
              "dividing by 1 gives the same number.",
    "T2.C1": "Show how a table fact gives the division of tens and hundreds: how many 9s are in 270.",
    "T2.C2": "Show the pattern of zeros and place value: one more zero in the dividend gives one more zero in the quotient, "
             "and dividing by 10 moves the digits one place right.",
    "T3.C1": "Show how to divide in the head by splitting the number into convenient parts, dividing each and adding.",
    "T3.C2": "Show how to round up to an easy number, divide, and take the share of the extra away.",
    "T3.C3": "Show how to divide by 4 or 8 by halving two or three times.",
    "T4.C1": "Show Susie's way: take away groups of the divisor again and again and add the groups to find the quotient.",
    "T4.C2": "Show Sunitha's way: estimate first, then take away the biggest groups that fit, in fewer steps.",
    "T4.C3": "Explain the remainder and the rule N = D × Q + R, with the remainder less than the divisor.",
    "T5.C1": "Show how to divide bigger numbers by taking away hundreds, tens and ones groups, always the biggest that fits.",
    "T6.C1": "Show how to divide a two-digit number by place value: share the tens, regroup the tens left into ones, share "
             "the ones.",
    "T6.C2": "Show how to regroup hundreds into tens, why a place that cannot be shared gets a 0, and how many digits the "
             "quotient has.",
    "T6.C3": "Show that taking away groups and place value give the same quotient for thousands and two-digit divisors, "
             "and where the zero goes.",
    "T7.C1": "Explain what the remainder means in a story: one more bag when the leftover needs a container, or a few left "
             "over when it is not shared.",
    "T7.C2": "Explain that total = cost of 1 kg × quantity, and how to find a missing total, quantity or cost.",
    "T7.C3": "Show how to break a word problem into steps: what is asked, what is given, what is missing, then solve in order.",
    "T8.C1": "Show how the quotient changes when the dividend or the divisor is doubled or halved, using a rectangle for "
             "N = D × Q.",
    "T9.C1": "Explain that a statement with an equal sign is true when both sides have the same value, and how to complete "
             "a statement.",
    "T10.C1": "Show how to test a statement with examples and decide if it is always, sometimes or never true.",
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
