# -*- coding: utf-8 -*-
"""Layout toy: a tiny made-up chapter that exercises the question layout end to end (see run_smoke.py).
Not a real chapter and not a book: every number is invented."""
from __future__ import annotations

CHAPTER = {"grade": 7, "label": "Class 7", "chapter_no": 98, "name": "Layout Toy Chapter",
           "book_part": "Toy", "source_pdf": "textbooks/class7/none.pdf"}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [("M1", "Signed Moves", "A coin moves right and left on a line; adding and taking away signed numbers.")]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "Toy chapter: one framing topic, two instructional topics, one summary topic.",
    "points": [{"title": "Toy", "text": "Exists only to prove the question layout and the image placeholders."}],
}

# (id, kind): the kind tells gates/question_layout.py which items must sit in a Questions topic.
NCERT_ITEMS = [
    ("opening", "text"),
    ("2.1.ex1", "example"),
    ("2.1.try1", "prompt"),
    ("2.1.FiO1", "exercise"),
    ("2.2.FiO1", "exercise"),
    ("2.1.MathTalk", "talk"),        # a discussion prompt: not a question, no concept of its own
]
MISCONCEPTIONS = [("M_TOY_1", "A student thinks adding a negative number makes the total bigger.")]
SOLUTION_NOTES = []
ERRATA = []
DESIGN_REFERENCES = [{"text": "toy, not a real design reference.", "url": ""}]
FIGURES = {}
