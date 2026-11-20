# -*- coding: utf-8 -*-
"""Class 5 Chapter 4 v3 structure (9 Nov 2026 change request): 17 learning topics, one video per topic.

This layer rebuilds the topic list from the v2 topic files (topics_1.py to topics_4.py, left as they were) so the book
questions, the worked examples and the teaching lines stay word for word. What changes:

  * Rows the content team wants SEPARATE become their own topic with their own video: Near-Round-Number Addition,
    Pair-the-Ends Shortcut, Sums of Even and Odd Numbers, and the two Let Us Think puzzles (Coins, A Torch).
  * Rows the content team wants as ONE video become one concept with labelled sections and one worked example in two
    parts: Subtraction and its link with addition, Adding and Subtracting Large Numbers, Journey Problems,
    Quick Sums and Differences, Reading Tables.
  * A tool lives in one concept only, so a tool shared by two topics sits in the second one (two activities), and the
    first topic's practice has no tool. Three tools are new (Near-Round Number Adder, Pair-the-Ends Lab, Table
    Explorer, in tools_4.py) and six are re-aimed (also tools_4.py).

All 57 book questions keep their coverage id, text, answer and card images; only the concept that homes them moves.
"""
from __future__ import annotations

import copy

from topics_common import A, DOER, TOPIC, WE  # noqa: F401
import topics_1, topics_2, topics_3, topics_4  # noqa: E402

_OLD = topics_1.TOPICS + topics_2.TOPICS + topics_3.TOPICS + topics_4.TOPICS
_TOPIC = {t["key"]: t for t in _OLD}
_CONCEPT = {c["key"]: c for t in _OLD for c in t["concepts"]}


def old(key):
    """A private copy of a v2 concept (so the v2 module objects stay untouched)."""
    return copy.deepcopy(_CONCEPT[key])


def old_topic(key):
    return _TOPIC[key]


def renamed(old_key, new_key, name=None):
    """A v2 teaching concept moved to a new topic: same lines, new key (and name)."""
    c = old(old_key)
    c["key"] = new_key
    if name:
        c["name"] = name
    return c


def doer(old_key, new_key, name, tool, *, objective=None, recap=None, items=None, misconceptions=None):
    """A v2 DOER moved or re-aimed: same dict, with the fields given replaced."""
    c = old(old_key)
    c["key"] = new_key
    c["name"] = name
    c["tool"] = tool
    if objective is not None:
        c["objective"] = objective
    if recap is not None:
        c["recap"] = list(recap)
    if items is not None:
        by = {it["cov"]: it for it in c["items"]}
        c["items"] = [by[i] for i in items]
    if misconceptions is not None:
        c["misconceptions"] = list(misconceptions)
    return c


def new_doer(key, name, tool, bloom, objective, recap, *, items=(), misconceptions=()):
    return DOER(key, name, tool, bloom, objective, recap, items=items, misconceptions=misconceptions)


def _dedupe(seq):
    out = []
    for x in seq:
        if x not in out:
            out.append(x)
    return out


def _heading(letter, title):
    """'Section A: Title.' (no second stop after a title that already ends in a question mark)."""
    return "Section %s: %s%s" % (letter, title, "" if title.endswith("?") else ".")


def merged(key, name, objective, sec_a, sec_b, we, *, parts, key_terms=(), minutes=8, bloom="Apply",
           a_lead=()):
    """ONE teaching concept from two v2 concepts: the video has two labelled sections and one worked example in two
    parts (Part A, Part B).

    sec_a, sec_b   (title, old concept key): the teaching lines of that concept become the section (its first line is
                   the section's prediction)
    a_lead         lines placed in section A right after the heading, before its body (used once, for T5's alignment)
    we             (question, answer) of the combined worked example
    parts          ((label, old concept key, indexes of its WE steps to leave out), ...)
    """
    ca, cb = old(sec_a[1]), old(sec_b[1])
    ta, tb = ca["teach"], cb["teach"]
    teach = [ta[0], _heading("A", sec_a[0])] + list(a_lead) + ta[1:]
    teach += [_heading("B", sec_b[0])] + tb
    steps = []
    for label, src, skip in parts:
        ex = _CONCEPT[src]["examples"][0]
        keep = [s for i, s in enumerate(ex["steps"]) if i not in set(skip)]
        keep[0] = "Part %s. %s" % (label, keep[0])
        steps += keep
    srcs = [ca, cb]
    textbook = _dedupe(sum((c["textbook"] for c in srcs), []))
    ncert = _dedupe(sum((c["ncert"] for c in srcs), []))
    terms = _dedupe(list(key_terms) or sum((c["key_terms"] for c in srcs), []))
    misc = _dedupe(sum((c["misconceptions"] for c in srcs), []))
    return A(key, name, bloom, objective, textbook=textbook, teach=teach,
             examples=[WE(we[0], steps, we[1])], ncert=ncert, key_terms=terms, misconceptions=misc, minutes=minutes)


def torch_words(c):
    """The v2 lines talk about 'a lamp'; the topic, the book question and the tool talk about Raghu's torch."""
    def fix(t):
        return t.replace("lamp", "torch")
    c["teach"] = [fix(t) for t in c["teach"]]
    for e in c["examples"]:
        e["q"] = fix(e["q"])
        e["steps"] = [fix(x) for x in e["steps"]]
        e["answer"] = fix(e["answer"])
    return c


def extra_from(concept, old_key):
    """Add the book-text coverage ids and the book lines of a v2 concept that no longer exists (T5.C3: the digits
    lined up) to the concept that took its place."""
    src = _CONCEPT[old_key]
    concept["ncert"] = _dedupe(list(concept["ncert"]) + list(src["ncert"]))
    concept["textbook"] = _dedupe(list(concept["textbook"]) + list(src["textbook"]))
    return concept


# ---------------------------------------------------------------------------------------------------------------
TOPICS = []

# T1 and T1B: unchanged (the hook and its free-try tool, then the first concept and the opener's questions).
TOPICS.append(old_topic("T1"))
TOPICS.append(old_topic("T1B"))

# T2 Fuel Arithmetic: Addition  (place value only; the near-round part is its own topic now)
TOPICS.append(TOPIC(
    "T2", "M1", "Fuel Arithmetic: Addition", ["Fuel Arithmetic", "Let Us Solve"], "Apply",
    "Students add two numbers with place value, regrouping when a place makes 10 or more, and find the total quantity "
    "of fuel in a tank.",
    "To add with place value, add the ones, then the tens, then the hundreds, and regroup 10 of one place as 1 of the "
    "next place on the left.",
    [old("T2.C1"),
     doer("T2.C3", "T2.C3", "Practice: Fuel Tank Adder", "fuel_tank_adder",
          objective="Students add pairs of numbers with place value, regrouping when a place makes 10 or more, and "
                    "find the total quantity of fuel in a tank.",
          recap=["Add the ones first, then the tens, then the hundreds.",
                 "When a place makes 10 or more, regroup: 10 ones are 1 ten and 10 tens are 1 hundred.",
                 "Check the sum: the ones, then the tens, then the hundreds must all be added once."],
          items=["fuel.lorry", "fuel.49_89"], misconceptions=["M_NO_CARRY"])],
    key_terms=["place value", "regroup", "sum"]))

# T2B Near-Round-Number Addition  (its own beat: the round number, then the adjustment)
TOPICS.append(TOPIC(
    "T2B", "M1", "Near-Round-Number Addition", ["Fuel Arithmetic", "Let Us Solve"], "Apply",
    "Students add a number that is just below a ten or a hundred by adding the round number and taking the extra back, "
    "and add whole tens together.",
    "A number just below a round number can be added the easier way: add the round number, then take the extra back.",
    [renamed("T2.C2", "T2B.C1", "Near-Round Numbers: Add, Then Take Back"),
     new_doer("T2B.C2", "Practice: Near-Round Number Adder", "near_round_adder", "Apply",
              "Students add pairs of numbers by adding the nearest round number and then taking the extra back, "
              "wherever that is easier.",
              ["If a number is just below a round number, add the round number and take the extra back.",
               "A whole number of tens is added by adding the tens.",
               "Look at the numbers first: if neither is close to a round number, use place value."],
              items=[it for it in old("T2.C3")["items"] if it["cov"] == "LUS43.add"],
              misconceptions=["M_FORGET_ONE"])],
    key_terms=["easier way", "round number", "take back"]))

# T3 Subtraction and Its Link with Addition  (one video, two labelled sections: the link, then place value)
TOPICS.append(TOPIC(
    "T3", "M1", "Subtraction and Its Link with Addition",
    ["Relationship Between Addition and Subtraction", "More Fuel Arithmetic", "Let Us Solve"], "Apply",
    "Students write the addition and subtraction sentences that follow from one sentence, subtract with place value, "
    "and check a subtraction by adding.",
    "Addition and subtraction are linked: from one sentence with three numbers you can write the others. To subtract "
    "with place value, start with the ones, and if there are too few ones, regroup 1 ten as 10 ones. Check a "
    "subtraction by adding the answer to the smaller number.",
    [merged("T3.C1", "Subtraction: the Link with Addition and Place Value",
            "Students write the addition and subtraction sentences that follow from one sentence, then subtract with "
            "place value and check by adding.",
            ("The link between addition and subtraction", "T3.C1"), ("Subtracting with place value", "T3.C2"),
            ("Part A: If 35 + 28 = 63, write the two subtraction sentences. Then, from 74 − 29 = 45, write an "
             "addition sentence and one more subtraction sentence. Part B: Find 72 − 38 and check the answer "
             "(practice values).",
             "Part A: 63 − 28 = 35 and 63 − 35 = 28; 29 + 45 = 74 and 74 − 45 = 29. Part B: "
             "72 − 38 = 34, and 38 + 34 = 72"),
            parts=(("A", "T3.C1", {6}), ("B", "T3.C2", set())),
            key_terms=["whole", "part", "subtract", "regroup", "difference", "check"]),
     old("T3.C3")],
    key_terms=["subtract", "regroup", "difference", "check"]))

# T4 Sums of Consecutive Numbers  (the patterns; pairing the ends is its own topic now)
TOPICS.append(TOPIC(
    "T4", "M2", "Sums of Consecutive Numbers", ["Sums of Consecutive Numbers"], "Understand",
    "Students find the patterns in the sums of consecutive numbers: when the sums are even or odd, and how much "
    "successive sums go up.",
    "Consecutive numbers follow one another with none skipped. The difference between successive sums is the number "
    "of numbers added, and whether the sums are even or odd depends on how many numbers are added.",
    [old("T4.C1"),
     doer("T4.C3", "T4.C3", "Practice: Consecutive Sums Lab", "consecutive_sums_lab",
          objective="Students explain the even and odd sums of consecutive numbers and find the difference between "
                    "successive sums.",
          recap=["The difference between successive sums is the number of numbers added.",
                 "Two consecutive numbers make an odd sum, and four make an even sum.",
                 "Whether the sums are even or odd depends on how many numbers are added."],
          items=["cons.q1", "cons.q2", "cons.q3"], misconceptions=["M_CONSEC_PARITY", "M_SUCC_DIFF_ONE"])],
    key_terms=["consecutive numbers", "successive sums"]))

# T4B Pair-the-Ends Shortcut  (its own beat: a different idea from the sum patterns)
TOPICS.append(TOPIC(
    "T4B", "M2", "Pair-the-Ends Shortcut", ["Sums of Consecutive Numbers"], "Understand",
    "Students find the sum of a run of consecutive numbers by pairing the two ends, without adding one by one.",
    "Pairs from the two ends of a run make the same total, so the sum is the number of pairs times the pair total, "
    "plus the middle number if there is one.",
    [renamed("T4.C2", "T4B.C1", "Pairing the Ends of a Run"),
     new_doer("T4B.C2", "Practice: Pair-the-Ends Lab", "pair_the_ends_lab", "Understand",
              "Students add runs of consecutive numbers by pairing the numbers from the two ends instead of adding "
              "one by one.",
              ["Pair the numbers from the two ends. Every pair makes the same total.",
               "With an odd number of numbers the middle number has no partner, and it is half of every pair total.",
               "The sum is the number of pairs times the pair total, plus the middle number if there is one."],
              items=[it for it in old("T4.C3")["items"] if it["cov"] == "cons.find"],
              misconceptions=["M_FIRST_TIMES"])],
    key_terms=["pairs", "ends", "middle number"]))

# T5 Adding and Subtracting Large Numbers  (one video: separate worked sections, the alignment taught once)
TOPICS.append(TOPIC(
    "T5", "M2", "Adding and Subtracting Large Numbers",
    ["The Longest Land Route", "Subtracting Large Numbers", "Let Us Solve", "Let Us Do"], "Apply",
    "Students add and subtract numbers up to 5 digits with place value and with the digits aligned and no place names.",
    "Large numbers are added and subtracted in the same way as small numbers: one place at a time, starting with the "
    "ones, regrouping 10 of one place as 1 of the next place on the left, or 1 as 10 of the place on the right. When "
    "the digits are aligned, ones under ones and tens under tens, the place names are not needed.",
    [extra_from(merged(
        "T5.C1", "Large Numbers: Adding, Then Subtracting",
        "Students add and subtract numbers of 4 or 5 digits by lining up the digits and working one place at a time, "
        "regrouping when a place has too many or too few.",
        ("Adding large numbers", "T5.C1"), ("Subtracting large numbers", "T5.C2"),
        ("Part A: Add 3,486 and 2,729. Part B: Find 6,402 − 2,758 and check the answer (practice values).",
         "Part A: 3,486 + 2,729 = 6,215. Part B: 6,402 − 2,758 = 3,644, and 2,758 + 3,644 = 6,402"),
        parts=(("A", "T5.C1", {6}), ("B", "T5.C2", set())),
        a_lead=["Line up the digits from the right, ones under ones, tens under tens, hundreds under hundreds and "
                "thousands under thousands. When the digits are lined up you do not need to write the place names. "
                "The same lining up is used for subtracting.",
                ],
        key_terms=["large numbers", "aligned", "place value", "regroup", "sum", "difference"], minutes=9),
        "T5.C3"),
     old("T5.C4")],
    key_terms=["large numbers", "aligned", "regroup", "sum", "difference"]))

# T6 Journey Problems  (one video: add or subtract, then estimate first; practice has no tool)
TOPICS.append(TOPIC(
    "T6", "M2", "Journey Problems", ["Let Us Solve", "Let Us Do"], "Apply",
    "Students solve journey problems that add, take away and compare amounts, and estimate before they calculate.",
    "In a journey problem, read the story one step at a time and decide whether to add, take away or find how many "
    "more. Estimating first, by rounding each amount up to a friendly number, tells you quickly whether an answer "
    "can be right.",
    [merged("T6.C1", "Journey Problems: Add or Subtract, Then Estimate",
            "Students decide whether each step of a journey problem adds or takes away, solve problems with more than "
            "one step, and estimate first by rounding up.",
            ("Add or subtract?", "T6.C1"), ("Estimate first, then check", "T6.C2"),
            ("Part A: A traveller starts a trip with ₹15,000. She spends ₹4,250 on fuel, is paid back "
             "₹2,000 by a friend, then spends ₹3,160 on tickets. How much money is left? Part B: A school "
             "council has ₹50,000 and wants to buy things that cost ₹19,820, ₹14,480 and ₹9,765. "
             "Estimate whether the money is enough, then check (practice values).",
             "Part A: ₹9,590 is left. Part B: enough: the total is ₹44,065 and ₹5,935 is left"),
            parts=(("A", "T6.C1", set()), ("B", "T6.C2", set())),
            key_terms=["journey problem", "add", "take away", "how many more", "estimate", "round up"]),
     old("T6.C3")],
    key_terms=["journey problem", "estimate", "add", "take away"]))

# T7 Quick Sums and Differences  (one video, two sections; the tool has two labelled modes)
TOPICS.append(TOPIC(
    "T7", "M3", "Quick Sums and Differences", ["Quick Sums and Differences"], "Apply",
    "Students find the number to add to reach 100, 1,000 or 10,000 by making nines, and take away 9 or 99 quickly by "
    "taking away a round number and giving 1 back.",
    "A round number is a stepping stone. To find what to add to a number to make 100, 1,000 or 10,000, make 9 in "
    "every place and then add 1. To take away 9 or 99, take away 10 or 100 and add 1.",
    [merged("T7.C1", "Quick Sums and Differences with Round Numbers",
            "Students find what to add to a number to reach 100, 1,000 or 10,000 by making nines, and take away 9 or "
            "99 by taking away a round number and giving 1 back.",
            ("Making 100, 1,000 or 10,000", "T7.C1"), ("Taking away 9 or 99", "T7.C2"),
            ("Part A: Find 46 + ___ = 100 and 358 + ___ = 1,000 by making nines. Part B: Find 52 − 9 and "
             "215 − 99 by taking away 10 or 100 and adding 1 (practice values).",
             "Part A: 46 + 54 = 100 and 358 + 642 = 1,000. Part B: 52 − 9 = 43 and 215 − 99 = 116"),
            parts=(("A", "T7.C1", {4}), ("B", "T7.C2", set())),
            key_terms=["round number", "nines", "add 1", "take away", "give back"]),
     old("T7.C3")],
    key_terms=["round number", "nines", "take away"]))

# T8 Palindrome Numbers and T9 Number Grid Puzzles: unchanged.
TOPICS.append(old_topic("T8"))
TOPICS.append(old_topic("T9"))

# T10 Even and Odd Numbers  (pairing; the practice has no tool, the tool is in the next topic)
TOPICS.append(TOPIC(
    "T10", "M4", "Even and Odd Numbers", ["Even and Odd Numbers"], "Understand",
    "Students decide whether a number is even or odd by pairing counters and by looking at the units digit.",
    "A number is even when its counters pair up with none left, and odd when one is left. The units digit tells: 0, "
    "2, 4, 6 and 8 are even.",
    [old("T10.C1"),
     doer("T10.C3", "T10.C3", "Practice: Even and Odd Numbers", None,
          objective="Students circle the even numbers in a list and use pairs to say what changes and what stays the "
                    "same when 2 is added to a number.",
          recap=["Even means pairs with none left over, and odd means one left over.",
                 "The units digit tells: 0, 2, 4, 6 and 8 are even.",
                 "Adding 2 makes one more pair, so a leftover counter stays and an even number stays even."],
          items=["eo.circle", "eo.add18", "eo.add23"], misconceptions=["M_ZERO_NOT_EVEN"])],
    key_terms=["even", "odd", "pairs", "units digit"]))

# T10B Sums of Even and Odd Numbers  (its own beat; the Pairs and Leftovers tool sits here with two activities)
TOPICS.append(TOPIC(
    "T10B", "M4", "Sums of Even and Odd Numbers", ["Even and Odd Numbers"], "Understand",
    "Students explain what happens to the sum of two even numbers, two odd numbers, and an odd and an even number by "
    "using the leftover counters.",
    "Even plus even is even, odd plus odd is even because the two leftovers make a pair, and odd plus even is odd.",
    [renamed("T10.C2", "T10B.C1"),
     doer("T10.C3", "T10B.C2", "Practice: Pairs and Leftovers", "pairs_and_leftovers",
          objective="Students use the leftover counters to explain the sums of two even numbers, two odd numbers, and "
                    "an odd and an even number.",
          recap=["Even plus even is even, odd plus odd is even, and odd plus even is odd.",
                 "The leftover counters decide: two leftovers make a new pair, and one leftover stays alone.",
                 "Even means pairs with none left over, and odd means one left over."],
          items=["eo.q3a", "eo.q3b", "eo.q3c"], misconceptions=["M_ODD_ODD_ODD"])],
    key_terms=["even", "odd", "leftover", "sum"]))

# T11 Let Us Think: Coins
TOPICS.append(TOPIC(
    "T11", "M4", "Let Us Think: Coins", ["Let Us Think"], "Apply",
    "Students list the ways to pay an exact amount with coins, one kind of coin at a time, so that no way is missed.",
    "To find all the ways to pay an amount, go through the number of coins of the biggest kind one at a time and fill "
    "the rest with smaller coins.",
    [old("T11.C1"),
     doer("T11.C3", "T11.C3", "Practice: Coins", None,
          objective="Students list the coin combinations that pay an exact amount by going through the coins of the "
                    "biggest kind one at a time.",
          recap=["To find every way to pay an amount, go through the number of coins of the biggest kind one at a "
                 "time.",
                 "Fill the rest of the amount with the smaller coins.",
                 "Keep a list so that no way is missed."],
          items=["jincy"], misconceptions=["M_ONE_WAY_COINS"])],
    key_terms=["coins", "exact amount", "ways", "list"]))

# T11B Let Us Think: A Torch
TOPICS.append(TOPIC(
    "T11B", "M4", "Let Us Think: A Torch", ["Let Us Think"], "Apply",
    "Students tell whether a switch is on or off after any press by looking at whether the press number is odd or "
    "even.",
    "A switch that flips with every press is ON after an odd press and OFF after an even press.",
    [torch_words(renamed("T11.C2", "T11B.C1")),
     doer("T11.C3", "T11B.C2", "Practice: The Torch", None,
          objective="Students tell whether a torch is on or off after any press by deciding whether the press number "
                    "is odd or even.",
          recap=["A switch that flips with every press is ON after an odd press and OFF after an even press.",
                 "Decide whether the press number is odd or even.",
                 "You do not have to press the switch again and again."],
          items=["torch23", "torchrule"], misconceptions=["M_TORCH_COUNT"])],
    key_terms=["odd", "even", "ON", "OFF", "press"]))

# T12 Reading Tables  (one video, two sections; the Table Explorer is new and holds the book's two tables)
TOPICS.append(TOPIC(
    "T12", "M4", "Reading Tables", ["Let Us Think", "Math Metric Mela"], "Apply",
    "Students read a table to find the highest and lowest values and the differences between values, and decide "
    "whether an amount is enough, short or extra.",
    "A table gives facts in rows and columns. To compare two numbers in a table, subtract the smaller from the bigger "
    "to find how much more or less. For a printed number and a used number, the difference tells how many are short "
    "or extra.",
    [merged("T12.C1", "Reading a Table: Highest, Difference, Short or Extra",
            "Students read a table to find the highest and lowest values and the difference between two values, and "
            "decide whether a number is enough, short or extra.",
            ("Reading a table", "T12.C1"), ("Enough, short or extra?", "T12.C2"),
            ("Part A: A table shows three buses. Bus A travelled 4,215 km and was bought in 2015, Bus B travelled "
             "6,380 km and was bought in 2018, and Bus C travelled 5,094 km and was bought in 2021. Which bus "
             "travelled the most? What is the difference between the most and the least, and between Bus B and "
             "Bus C? A driver was 25 years old when Bus C was bought. In which year was the driver born? Part B: "
             "12,450 tickets were printed for a fair and 12,615 people came. Were the tickets enough, and how many "
             "were short or extra? On another day 9,830 tickets were printed and 9,415 people came (practice "
             "values).",
             "Part A: Bus B travelled the most; 2,165 km; 1,286 km; the driver was born in 1996. Part B: first day: "
             "not enough, 165 short; second day: enough, 415 extra"),
            parts=(("A", "T12.C1", set()), ("B", "T12.C2", set())),
            key_terms=["table", "row", "column", "highest", "difference", "enough", "short", "extra"]),
     doer("T12.C3", "T12.C3", "Practice: Table Explorer", "table_explorer")],
    key_terms=["table", "difference", "enough", "short", "extra"]))

# T13 chapter revision: its text names every stop of the journey; the picture is one signpost per major idea.
_t13 = copy.deepcopy(old_topic("T13"))
_t13["summary"] = ("The chapter's ideas in one drive along the road trip: swapping to balance sums, adding with place "
                   "value, near-round numbers, subtraction and its link with addition, consecutive sums and the "
                   "pair-the-ends shortcut, large numbers, journey problems, quick sums and differences, "
                   "palindromes, grids, even and odd numbers and their sums, coins, a torch, and tables.")
TOPICS.append(_t13)
