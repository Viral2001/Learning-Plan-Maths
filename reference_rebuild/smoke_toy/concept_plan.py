# -*- coding: utf-8 -*-
"""Smoke-test concept plan - exercises build.py's assemble() fix end to end (framing + instructional
+ summary topics, one DOER with a tool and one FIO item, so core.qt.apply() actually runs)."""
from __future__ import annotations

import content as K  # noqa: E402


def WE(q, steps, answer, *, ncert=(), fact=None, expect=None):
    return {"q": q, "steps": list(steps), "answer": answer, "ncert": list(ncert), "fact": fact, "expect": expect}


def FIO(cov, book, question, steps, answer, *, expect=None):
    return {"cov": cov, "book": book, "question": question, "steps": list(steps), "answer": answer, "expect": expect}


def A(key, name, bloom, objective, *, textbook=(), teach=(), examples=(), ncert=(), key_terms=(),
      misconceptions=(), video_focus=(), enrichment=False, minutes=10, role=None):
    return {"key": key, "kind": "teach", "name": name, "bloom": bloom, "objective": objective,
            "textbook": list(textbook), "teach": list(teach), "examples": list(examples), "ncert": list(ncert),
            "key_terms": list(key_terms), "misconceptions": list(misconceptions), "video_focus": list(video_focus),
            "enrichment": enrichment, "minutes": minutes, "role": role}


def DOER(key, name, tool, bloom, objective, recap, *, items=(), textbook=(), ncert=(), misconceptions=(),
         enrichment=False, role=None):
    return {"key": key, "kind": "doer", "name": name, "tool": tool, "bloom": bloom, "objective": objective,
            "recap": list(recap), "items": list(items), "textbook": list(textbook), "ncert": list(ncert),
            "misconceptions": list(misconceptions), "enrichment": enrichment, "role": role}


def TOPIC(key, module, name, sections, bloom, objective, summary, concepts, *, topic_type="instructional",
          key_terms=()):
    return {"key": key, "module": module, "name": name, "ncert_sections": list(sections), "bloom": bloom,
            "objective": objective, "summary": summary, "concepts": list(concepts), "topic_type": topic_type,
            "key_terms": list(key_terms)}


def T(tool_id, title, subtype, idea, screen, student_does, challenges, feedback, done_when, shared_state,
      misconceptions, hints):
    assert 5 <= len(challenges) <= 7, title
    assert len(hints) == 4, title
    return {"tool_id": tool_id, "title": title, "subtype": subtype, "idea": idea, "screen": screen,
            "student_does": list(student_does), "challenges": list(challenges), "feedback": list(feedback),
            "done_when": done_when, "shared_state": list(shared_state), "misconceptions": list(misconceptions),
            "hint_ladder": [{"rung": r, "text": t} for r, t in
                            zip(("orienting", "strategic", "specific", "bottom-out"), hints)]}

TOOLS = {
    "smoke_tool": T(
        "tool_smoke_double_square", "Double the Square", "manipulative",
        "Dragging the side of a square shows that doubling the side quadruples the area, not doubles it.",
        "A square with a slider under it that sets the side length; the area is shown as a number "
        "next to the square.",
        ["Predict what happens to the area if the side doubles.", "Drag the slider to double the side.",
         "Read the new area off the square.", "Compare the new area to the old area."],
        ["Set the side to 2 units; what is the area?", "Set the side to 4 units; what is the area?",
         "Set the side to 3 units; what is the area?", "Set the side to 6 units; what is the area?",
         "Double the side from 3 to 6 units; by what factor did the area grow?"],
        ["A wrong guess still lets the slider move; the area number updates live either way.",
         "A solved card shows the side and the area together, side by side with the previous card."],
        "The student has doubled a side at least once and named the area's growth factor out loud.",
        ["side", "area", "cardIndex"],
        ["M_SMOKE_1"],
        ["What does the slider control?", "What happens to area when a side is scaled?",
         "Try doubling the side and read the new area.",
         "Doubling the side gives 4 times the area, because area is side times side."]),
}

TOPICS = []

TOPICS.append(TOPIC(
    "T1", "M1", "Why Doubling a Side Surprises Us", ["Opening"], "Understand", "",
    "The student watches a square's side double and predicts, then sees, what happens to the area.",
    [A("T1.C1", "Opening Hook", "Remember", "",
       textbook=["A farmer doubles the side of a square field."],
       teach=["Ask: if the side doubles, does the area double too?"],
       ncert=["opening"], key_terms=["side", "area"], video_focus=["HOOK"], minutes=5,
       enrichment=True)],
    topic_type="framing"))

TOPICS.append(TOPIC(
    "T2", "M1", "Doubling a Square's Side", ["2.1"], "Apply",
    "Find the area of a square after its side is doubled and compare it to the original area.",
    "The student computes the area before and after doubling the side, then uses the tool to check.",
    [A("T2.C1", "Computing the New Area", "Apply",
       "The student computes a square's area before doubling its side and again after doubling it, "
       "then compares the two areas to see the area grow by four times.",
       textbook=["A square of side 3 units has area 9 square units."],
       teach=["Predict the new area before computing it.", "Double the side to 6 units and compute the area."],
       examples=[WE("A square has side 3 units. What is its area after the side is doubled?",
                     ["New side = 3 × 2 = 6 units.", "New area = 6 × 6 = 36 square units."],
                     "36 square units", ncert=["2.1.example1"])],
       key_terms=["side", "area"], misconceptions=["M_SMOKE_1"], minutes=12),
     DOER("T2.C2", "Practice: Doubling a Square", "smoke_tool", "Apply",
          "The student uses the tool to confirm that doubling a square's side multiplies its area by "
          "four, matching the worked computation done earlier in this topic.",
          ["A square's area is side times side.", "Doubling the side multiplies the area by four."],
          items=[FIO("2.1.FiO1", "Figure it Out (2.1)",
                     "A square has side 5 units. What is its area after the side is doubled?",
                     ["New side = 5 × 2 = 10 units.", "New area = 10 × 10 = 100 square units."],
                     "100 square units")])],
    topic_type="instructional"))

TOPICS.append(TOPIC(
    "T3", "M1", "What We Found", ["Summary"], "Understand", "",
    "A one-line recap that doubling a square's side quadruples its area.",
    [A("T3.C1", "Recap", "Understand", "",
       teach=["Doubling a square's side multiplies its area by four, not two."],
       video_focus=["RECAP"], minutes=4, enrichment=True)],
    topic_type="summary"))
