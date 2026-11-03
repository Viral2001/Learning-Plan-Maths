# -*- coding: utf-8 -*-
"""Concept plan for Class 5 Chapter 1, We the Travellers - I: the topic list and the tool specs build.py assembles.

Topics live in topics_1.py (T1 to T5, M1), topics_2.py (T6 to T9, M2), topics_3.py (T10, T11) and topics_4.py
(T12 to T14, M3); tool specs in tools_1.py to tools_4.py. The authoring helpers (WE, FIO, A, DOER, TOPIC, T) are in
topics_common.py."""
from topics_common import A, DOER, FIO, TOPIC, WE, T, HINT_LADDER_NOTE  # noqa: F401
import topics_1, topics_2, topics_3, topics_4  # noqa: E402
import tools_1, tools_2, tools_3, tools_4  # noqa: E402

TOPICS = topics_1.TOPICS + topics_2.TOPICS + topics_3.TOPICS + topics_4.TOPICS
TOOLS = {}
for _t in (tools_1, tools_2, tools_3, tools_4):
    TOOLS.update(_t.TOOLS)

# core.qt finds the question slots on its own; these two only document intent (see chapter_template).
QT_TOPICS = {t["key"] for t in TOPICS if any(c.get("items") for c in t["concepts"])}
FIO_HOME = {it["cov"]: t["key"] for t in TOPICS for c in t["concepts"] for it in c.get("items") or []}
