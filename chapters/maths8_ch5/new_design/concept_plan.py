# -*- coding: utf-8 -*-
"""Class 8 Chapter 5, Number Play: the modules -> topics -> concepts skeleton and the tool specs.
Topics live in topics_1.py (T1 to T4), topics_2.py (T5, T6), topics_3.py (T7 to T11) and topics_4.py (T12, T13);
tools in tools.py."""
from __future__ import annotations

from topics_common import A, DOER, FIO, TOPIC, WE, T  # noqa: F401
from tools import TOOLS  # noqa: F401
import topics_1  # noqa: E402
import topics_2  # noqa: E402
import topics_3  # noqa: E402
import topics_4  # noqa: E402

TOPICS = topics_1.TOPICS + topics_2.TOPICS + topics_3.TOPICS + topics_4.TOPICS
QT_TOPICS = set()
FIO_HOME = {}
