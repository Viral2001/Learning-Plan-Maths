# -*- coding: utf-8 -*-
"""How much working one solution card holds, and where a longer working is cut for a second card.

One estimator for every caller, so the placeholder pass (core/solutions/placeholders.py, run before any
solution is authored) and the scene generator (core/solutions/gen_scenes.py, run once solutions.json exists)
agree on which questions get a continuation card:

    cards_needed(steps)      1, or 2 when the working is longer than max_lines wrapped lines
    split_point(steps)       how many steps stay on card 1 (the rest, and the answer, go on card 2)

`steps` are plain-text strings (use schema.tex_to_plain on LaTeX steps). Two cards is the ceiling: a working
that would need a third is shrunk by the card's own fit_column(), as before.

Numbers are for a 1920x1080 card with the working set at 24pt in core/solutions/style/_style.py: the working
column is 12.4 Manim units wide, or 7.6 when a diagram shares the frame, and holds about 8 wrapped lines of
steps once Given / To find / Method, the answer box and the common-mistake note have taken their share.
They are an estimate from the text; the rendered card is the final word, and the config can move the cut
(`question_image_max_lines`).
"""
from __future__ import annotations

import io
import json
import math
import os

MAX_LINES = 8
CHARS_PLAIN = 90            # characters per wrapped line on a full-width card
CHARS_WITH_FIGURE = 58      # ... on a card that shares the frame with a diagram


def step_lines(step, with_figure=False):
    per = CHARS_WITH_FIGURE if with_figure else CHARS_PLAIN
    return max(1, math.ceil(len(step or "") / per))


def total_lines(steps, with_figure=False):
    return sum(step_lines(s, with_figure) for s in steps or [])


def cards_needed(steps, *, with_figure=False, max_lines=MAX_LINES):
    return 2 if len(steps or []) > 1 and total_lines(steps, with_figure) > max_lines else 1


def split_point(steps, *, with_figure=False, max_lines=MAX_LINES):
    """Number of steps that stay on card 1 (1 <= k <= len(steps) - 1). Only meaningful when cards_needed() is 2."""
    steps = list(steps or [])
    if len(steps) < 2:
        return len(steps)
    run, k = 0, None
    for i, s in enumerate(steps):
        ln = step_lines(s, with_figure)
        if run + ln > max_lines and i > 0:
            k = i
            break
        run += ln
    if k is None:
        k = max(1, len(steps) // 2)
    return min(max(k, 1), len(steps) - 1)


def chapter_config(folder):
    """chapter.config.json beside solutions.json ({} when there is none: the old, single-card behaviour)."""
    path = os.path.join(folder, "chapter.config.json")
    if not os.path.exists(path):
        return {}
    with io.open(path, encoding="utf-8") as f:
        return json.load(f)


def continuation_enabled(cfg):
    """A second solution card is opt-in per chapter (config "solution_continuation": true), so a chapter built
    before this existed, and the Class 9/10 builder that reads the same solutions.json, are untouched."""
    return bool((cfg or {}).get("solution_continuation"))
