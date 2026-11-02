# -*- coding: utf-8 -*-
"""Class 7 Chapter 3, A Peek Beyond the Point: the modules -> topics -> concepts skeleton and the tool specs.
Topics live in topics_1.py (T1 to T5), topics_2.py (T6 to T10) and topics_3.py (T11 to T16); tools in tools.py."""
from __future__ import annotations

from topics_common import A, DOER, FIO, TOPIC, WE, T  # noqa: F401
from tools import TOOLS  # noqa: F401
import topics_1, topics_2, topics_3  # noqa: E402

TOPICS = topics_1.TOPICS + topics_2.TOPICS + topics_3.TOPICS
QT_TOPICS = set()
FIO_HOME = {}
