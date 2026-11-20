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
    "T1.C1": "Create curiosity with Daljeet Kaur's butter milk pouches: 60 pouches packed in groups of 2 and groups of 3, "
             "so what other groups can she make? A short story, no explanation, ending on an open question that leads "
             "to the Pouch Packer tool.",
    "T1B.C1": "Explain that a total is the number of groups times the group size, and that one total can be packed in "
              "equal groups in many ways.",
    "T2.C1": "Show that swapping the number of groups and the group size gives the same product, with arrays turned "
             "around, and that a number times 0 is 0.",
    "T3.C1": "Show that multiplying by 10 moves every digit one place to the left and by 100 two places, in the place "
             "value table.",
    "T3.C2": "Show how to multiply tens, hundreds and thousands: multiply the digits, then write the zeros of both "
             "numbers.",
    "T4.C1": "Show that a number can be split into parts, each part multiplied, and the small products added, as the "
             "children did for 18 × 5.",
    "T5.C1": "Show how an array of packets is cut in the middle and the halves moved, so that halving one number and "
             "doubling the other keeps the product.",
    "T5.C2": "Explain why halving and doubling works well when one number is 5 or 25.",
    "T6.C1": "Show how to round one number to a multiple of 10, multiply, and then take away or add the strip that was "
             "missing or extra.",
    "T7.C1": "Show how to look at the numbers first and choose the strategy that makes the work short: split, halve "
             "and double, or nearest multiple.",
    "T8.C1": "Show how to multiply with a box: split both numbers into tens and ones, fill the box with the small "
             "products and add.",
    "T8.C2": "Show how the same small products are written as Kanti's four lines and as John's two lines.",
    "T9.C1": "Show how to multiply place by place and add: hundreds, tens and ones each multiplied separately.",
    "T9.C2": "Explain Mili's father's method: carries go to the next place and are added after that place is "
             "multiplied.",
    "T10.C1": "Show how to check a worked multiplication by an estimate and by its place values, and how to find a "
              "missing zero or a wrong place value.",
    "T11.C1": "Show how to tell that two products are equal without calculating, by changing the numbers in a way "
              "that keeps the product.",
    "T11.C2": "Show how one more column or one more row of an array adds one more group, to find a neighbouring product "
              "from a known one.",
    "T12.C1": "Show how to estimate a product by rounding both numbers to friendly numbers.",
    "T12.C2": "Show how to solve a digit puzzle by starting from the ones digit and using the colours.",
    "T13.C1": "Follow the amount of gold coins that doubles, triples or is multiplied by 5 every day, one day at a time.",
    "T14.C1": "Show how the product changes when one or both numbers are halved or doubled.",
    "T14.C2": "Show patterns in products: 11 times a two-digit number, numbers ending in 5 multiplied by themselves, and "
              "strings of 1s.",
    "T15.C1": "Show how to read a word problem, decide what to multiply and what to add or take away, estimate and "
              "check.",
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
