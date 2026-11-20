# -*- coding: utf-8 -*-
"""Image ids in the order the LP2 upload endpoint expects them: within each concept the images are numbered IMG1, IMG2 ...
down the media list.

core/solutions/placeholders.py gives an answer concept's solution cards the numbers 2 and 3, because the reserved file name
of a card is <coverage stem>.IMGn.png by question (question card 1, solution card 2, continued card 3) and the sibling
question concept holds IMG1. The server counts per concept and rejects that: "expected media id='...C9.IMG1', got
'...C9.IMG2'" (74 times on Class 5 Ch 1, 5 Nov 2026). Same remedy as placeholders._renumber_existing_images: only the
ids change, every reference to them is rewritten, and the urls (strings starting with http) are frozen, so the file
name an artist saves a card under does not move.

renumber(plan) -> {old id: new id}."""
from __future__ import annotations

import re

_TOKEN = re.compile(r"\bM\d+\.S\d+\.T\d+\.C\d+\.[A-Za-z0-9]+")
_IMG = re.compile(r"\.IMG(\d+)$")


def _topics(plan):
    return [t for m in plan.get("modules") or [] for s in m.get("segments") or [] for t in s.get("topics") or []]


def renumber(plan):
    rename = {}
    for topic in _topics(plan):
        by_concept = {}
        for node in topic.get("media") or []:
            if node.get("type") == "image" and _IMG.search(node.get("id", "")):
                by_concept.setdefault(node.get("concept_id"), []).append(node)
        for cid, nodes in by_concept.items():
            nodes.sort(key=lambda n: int(_IMG.search(n["id"]).group(1)))
            for want, node in enumerate(nodes, 1):
                new_id = "%s.IMG%d" % (cid, want)
                if node["id"] != new_id:
                    rename[node["id"]] = new_id
    if not rename:
        return {}

    def fix(o):
        if isinstance(o, dict):
            return {k: fix(v) for k, v in o.items()}
        if isinstance(o, list):
            return [fix(v) for v in o]
        if isinstance(o, str) and not o.startswith("http"):
            return _TOKEN.sub(lambda mo: rename.get(mo.group(0), mo.group(0)), o)
        return o

    for k in list(plan.keys()):
        plan[k] = fix(plan[k])
    return rename
