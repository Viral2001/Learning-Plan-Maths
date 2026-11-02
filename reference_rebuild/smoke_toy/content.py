# -*- coding: utf-8 -*-
"""Smoke-test content module - not a real chapter, just enough to exercise build.py's assemble()
fix (source_type/is_enrichment/source_segment_role/objective_id/anchor) and core.qt end to end."""
from __future__ import annotations

CHAPTER = {"grade": 6, "label": "Class 6", "chapter_no": 99, "name": "Smoke Toy Chapter",
           "book_part": "Smoke Test", "source_pdf": "textbooks/class6/smoke.pdf"}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [("M1", "Smoke Module", "A tiny module that only exists to exercise the build pipeline.")]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "Smoke test only: one framing topic, one instructional topic, one summary topic.",
    "points": [{"title": "Smoke test", "text": "Exists only to prove assemble() writes every field "
                "gates/skeleton.py and gates/objectives.py require."}],
}

NCERT_ITEMS = ["opening", "2.1.example1", "2.1.FiO1"]
MISCONCEPTIONS = [("M_SMOKE_1", "A student thinks doubling a side doubles the area.")]
SOLUTION_NOTES = []
ERRATA = []
DESIGN_REFERENCES = [{"text": "smoke test, not a real design reference.", "url": ""}]
FIGURES = {}
