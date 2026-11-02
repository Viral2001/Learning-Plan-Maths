# -*- coding: utf-8 -*-
"""Class 7 Chapter 8, Working with Fractions: the modules -> topics -> concepts skeleton and the tool specs.
Topics live in topics_1.py (M1), topics_2.py (M2) and topics_3.py (M3, M4); tools in tools.py."""
from __future__ import annotations

from topics_common import A, DOER, FIO, TOPIC, WE, T  # noqa: F401
from tools import TOOLS  # noqa: F401
import topics_1, topics_2, topics_3  # noqa: E402

TOPICS = topics_1.TOPICS + topics_2.TOPICS + topics_3.TOPICS
QT_TOPICS = set()
FIO_HOME = {}
