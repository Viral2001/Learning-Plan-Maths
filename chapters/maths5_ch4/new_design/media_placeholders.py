# -*- coding: utf-8 -*-
"""Placeholder video documents for the video slots that have no script file.

User decision (2026-11-05, 'approve and upload'): this chapter's LP carries PLACEHOLDERS for its media; the scripts and the videos are made
in other folders. build.py (chapter.config "media_placeholders": true) calls with_stubs(), which adds one stub script
document per slot of video_worklist.json that has no file in video_scripts/. core.video_script.node.video_node then
builds the usual placeholder video node from it (id, title, description, planned_url, build_status "placeholder"),
with an empty beat list: no script has been written, so nothing here can be rendered until the real script exists.
A real script file for a slot always wins over its stub."""
from __future__ import annotations

# The plan's purpose for each video (priority_doc.md section B), by authored concept key (Class 5 Chapter 4).
DOC_PURPOSE = {
    "T1.C1": "Create curiosity with Nazrana's number cards: two groups add up to 19 and 21, can one swap make the sums "
             "equal? A short story, no explanation, ending on an open question that leads to the Balance the Sums tool.",
    "T1B.C1": "Explain that swapping a smaller and a bigger number between two groups raises one sum and lowers the other "
              "by the same amount, so the gap closes by twice the difference, and that the swap to look for differs by "
              "half of the gap.",
    "T2.C1": "Show how to add with place value, regrouping 10 ones as 1 ten and 10 tens as 1 hundred.",
    "T2B.C1": "Show an easier way to add: add the round number and take the extra back for a number just below it, and add "
              "whole tens together.",
    "T3.C1": "One video with two labelled sections. Section A shows that one addition or subtraction sentence with three "
             "numbers gives the other sentences, with the whole and its two parts, and that this is how to check an "
             "answer. Section B shows how to subtract with place value, regrouping 1 ten as 10 ones, and how to check "
             "by adding.",
    "T4.C1": "Explain what consecutive numbers are, how a sum is built up one number at a time with a running total, why "
             "the difference between successive sums is the number of numbers added, and why the sums are even or odd.",
    "T4B.C1": "Show how pairs from the two ends of a run of consecutive numbers make the same total, and use that to add "
              "without adding one by one.",
    "T5.C1": "One video with two labelled sections. Section A shows how to line up the digits from the right, ones under "
             "ones, and add large numbers with the same regrouping steps as small numbers, with a ten thousands place "
             "for 5 digit numbers. Section B shows how to subtract large numbers with the digits lined up, regrouping "
             "across a zero, and how to check by adding.",
    "T6.C1": "One video with two labelled sections. Section A shows how to read a journey story one step at a time and "
             "decide whether to add, take away or find how many more. Section B shows how to estimate whether an amount "
             "is enough by rounding each price up to the next thousand, then check with the exact numbers.",
    "T7.C1": "One video with two labelled sections. Section A shows how to find what to add to reach 100, 1,000 or 10,000 "
             "by making 9 in every place and adding 1, and that it always works. Section B shows how to take away 9 or "
             "99 quickly by taking away 10 or 100 and adding 1, and how to use it backwards.",
    "T8.C1": "Explain palindrome numbers: they read the same both ways, the first and last digits match, and how to list "
             "the palindromes in a range.",
    "T9.C1": "Show how the inc and dec arrows tell where the smallest and the biggest number go in a grid, and how to fill "
             "and check a grid, as a warm-up for the grid puzzle.",
    "T10.C1": "Show that an even number pairs up with none left over and an odd number has one left over, and that the "
              "units digit tells which.",
    "T10B.C1": "Show what the leftover counters do when two numbers are added: even plus even is even, odd plus odd is "
               "even, odd plus even is odd.",
    "T11.C1": "Show how to list every way to pay an exact amount with a limited number of coins, one kind of coin at a "
              "time, as a warm-up for the coin puzzle.",
    "T11B.C1": "Show that a switch that flips with every press is ON after an odd press and OFF after an even press, as a "
               "warm-up for the torch puzzle.",
    "T12.C1": "One video with two labelled sections. Section A shows how to read a table to find the highest and lowest "
              "values, the difference between two values and a year from an age. Section B shows how to compare the "
              "number printed with the number needed and decide whether it is enough, short or extra, and by how many.",
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
