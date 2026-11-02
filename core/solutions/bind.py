# -*- coding: utf-8 -*-
"""Bind solutions.json to the chapter's content, and list what still has no solution.

    from core.solutions import bind
    bind.fill(CP.TOPICS, sols)                 # before assemble(): items/examples get plan-text steps + answer
    bind.write_worklist(path, header, CP.TOPICS, sols)   # the --solution-worklist pass of build.py

solutions.json is keyed by coverage id (`cov` of a concept_plan item, or an example's `ncert` id). `fill`
overwrites the item's `steps` and `answer` with the plain text of the board-format solution
(schema.plan_fields), so the plan blocks, the video worklist's items and the question-topic fallback block
all carry the same working, and gates/eqcheck_* read plain text as before.
"""
from __future__ import annotations

import io
import json

from core.solutions import schema


def _items(topics):
    """(kind, owner dict, cov id, concept key) for every exercise item and every worked example that cites a book id."""
    for t in topics:
        for c in t["concepts"]:
            for it in c.get("items") or []:
                yield "exercise", it, it["cov"], c["key"]
            for ex in c.get("examples") or []:
                for ref in (ex.get("ncert") or [])[:1]:
                    yield "example", ex, ref, c["key"]


def fill(topics, sols):
    """Overwrite steps/answer of every item and example that has a solutions.json entry. Returns the count."""
    n = 0
    for kind, owner, cov, _ in _items(topics):
        sol = sols.get(cov)
        if not sol or sol.get("kind") != kind:
            continue
        owner["steps"], owner["answer"] = schema.plan_fields(sol)
        n += 1
    return n


def missing(topics, sols):
    """Exercise items with no entry in solutions.json (examples keep their authored text, so are not listed)."""
    out = []
    for kind, it, cov, key in _items(topics):
        if kind == "exercise" and cov not in sols:
            out.append({"cov": cov, "book": it.get("book", ""), "concept": key, "question": it["question"],
                        "existing_steps": it.get("steps") or [], "existing_answer": it.get("answer") or ""})
    return out


def write_worklist(path, header, topics, sols):
    todo = missing(topics, sols)
    doc = dict(header, todo=todo, count=len(todo))
    with io.open(path, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    return len(todo)
