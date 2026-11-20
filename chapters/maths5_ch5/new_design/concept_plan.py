# -*- coding: utf-8 -*-
"""Concept plan for Class 5 Chapter 5, Far and Near: the topic list and the tool specs build.py assembles.

Topics live in topics_1.py (T1, T1B, T2 in M1 and T3 in M2), topics_2.py (T4 to T6 in M2 and T7 in M3) and topics_3.py
(T8 to T12, M3); tool specs in tools_1.py to tools_3.py. The authoring helpers (WE, FIO, A, DOER, TOPIC, T) are in
topics_common.py."""
from topics_common import A, DOER, FIO, TOPIC, WE, T, HINT_LADDER_NOTE  # noqa: F401
import topics_1, topics_2, topics_3  # noqa: E402
import tools_1, tools_2, tools_3  # noqa: E402

TOPICS = topics_1.TOPICS + topics_2.TOPICS + topics_3.TOPICS
TOOLS = {}
for _t in (tools_1, tools_2, tools_3):
    TOOLS.update(_t.TOOLS)

# core.qt finds the question slots on its own; these two only document intent (see chapter_template).
QT_TOPICS = {t["key"] for t in TOPICS if any(c.get("items") for c in t["concepts"])}
FIO_HOME = {it["cov"]: t["key"] for t in TOPICS for c in t["concepts"] for it in c.get("items") or []}


# ---------------------------------------------------------------------------
# LaTeX display text of every book question (core/solutions/LATEX_REFERENCE.md): the question card, the numbered
# working and the answer as strict inline $...$ text. build.py / core/qt.py show question_tex / steps_tex /
# answer_tex when an item has them (the plain question / steps / answer stay for the video worklist and the
# arithmetic gate). A solutions.json entry, once the media team writes one, replaces these with its own.
# ---------------------------------------------------------------------------
import os as _os, sys as _sys  # noqa: E402

_d = _os.path.dirname(_os.path.abspath(__file__))
while not (_os.path.isdir(_os.path.join(_d, "core")) and _os.path.isdir(_os.path.join(_d, "gates"))):
    if _os.path.dirname(_d) == _d:
        raise SystemExit("pipeline root not found above %s" % __file__)
    _d = _os.path.dirname(_d)
if _d not in _sys.path:
    _sys.path.insert(0, _d)
from core.solutions.latex_convert import latex_wrap  # noqa: E402

import ch_latex_house as _LH  # noqa: E402  (house style of the book-question text, see ch_latex_house.py)

for _t in TOPICS:
    for _c in _t["concepts"]:
        for _it in _c.get("items") or []:
            _it["question"] = _LH.house(_it["question"])
            _it["steps"] = [_LH.house(_s) for _s in _it["steps"]]
            _it["answer"] = _LH.house(_it["answer"])
            _it["question_tex"] = _LH.fix_blanks(latex_wrap(_LH.for_tex(_it["question"])))
            _it["steps_tex"] = [_LH.fix_blanks(latex_wrap(_LH.for_tex(_s))) for _s in _it["steps"]]
            _it["answer_tex"] = _LH.fix_blanks(latex_wrap(_LH.for_tex(_it["answer"])))
