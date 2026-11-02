# -*- coding: utf-8 -*-
"""Take the book numbering off a chapter's video title cards (user rule, 1 Oct 2026).

A card such as 'Sectors and Segments, Q5' keeps its set name ('Sectors and Segments'); a card that is only
numbering ('Figure it Out 3.8 · Q2 (c)', 'Chapter Exercises, Q6', 'Example 2', 'End of chapter · Q7') shows the
name of the topic the video sits in. Only `on_screen` and `marks` of each beat are touched. Whatever numbering
is left elsewhere (descriptions, narration, notes) is listed for a hand rewrite; check.py rejects it.

    python -B pipeline/video_script/strip_book_numbers.py <chapter>/new_design [--write]
"""
from __future__ import annotations

import glob
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from check import book_numbers, readable_strings  # noqa: E402

# A card label runs from "title card" to its closing quote/brace, or (unquoted) to the word that ends it.
CARD = re.compile(r"(title card(?:,|:| reads)?\s*)(?:(['{])([^'{}]+)(['}])"
                  r"|([^;'{}]+?)(?=,?\s+(?:appears?|sits|fades|stays|then)\b|\s*;|\s*$))", re.I)
GENERIC = (r"(?:Q\s?\d+[a-z]?|gFiO\d+|\((?:[a-h]|i{1,3}|iv|vi{0,3}|ix|x|end|multiplication|division)\)"
           r"|parts?\s*\(?[a-h]\)?(?![A-Za-z])|Examples?\s+\d+|Exercises?\s+[\d.]+|Figure it Out|Chapter Exercises"
           r"|End of chapter|Section|Try This|and|[\d.]+)")
TAIL_TOKEN = re.compile(r"[\s·,:&]*" + GENERIC + r"[\s·,:&]*$", re.I)
HEAD_TOKEN = re.compile(r"^[\s·,:&]*" + GENERIC + r"(?![A-Za-z])[\s·,:&]*", re.I)


def card_name(label: str, topic: str) -> str | None:
    """The card's new text, or None when it carries no numbering."""
    if not (book_numbers(label) or re.search(r"Figure it Out|gFiO\d", label, re.I)):
        return None
    rest = label
    while (m := TAIL_TOKEN.search(rest)) and m.start() < len(rest):
        rest = rest[:m.start()]
    while (m := HEAD_TOKEN.match(rest)) and m.end() > 0:
        rest = rest[m.end():]
    rest = rest.strip(" ·,:")
    return rest if re.search(r"[A-Za-z]{3}", rest) and not book_numbers(rest) else topic


def fix_text(text: str, topic: str) -> str:
    def swap(m):
        if m.group(3) is not None:
            name = card_name(m.group(3), topic)
            return m.group(0) if name is None else f"{m.group(1)}{m.group(2)}{name}{m.group(4)}"
        name = card_name(m.group(5), topic)
        return m.group(0) if name is None else f"{m.group(1)}{name}"
    return CARD.sub(swap, text)


def topics_by_key(folder: Path):
    wl = json.loads((folder / "video_worklist.json").read_text(encoding="utf-8"))
    plan = json.loads(Path(glob.glob(str(folder / "*_new.json"))[0]).read_text(encoding="utf-8"))
    names = {t["topic_id"]: t["topic_name"] for m in plan["modules"] for s in m["segments"] for t in s["topics"]}
    return {v["key"]: names[v["topic_id"]] for v in wl["videos"]}


def main(argv):
    folder, write = Path(argv[0]), "--write" in argv
    topic_of = topics_by_key(folder)
    changed = left = 0
    for f in sorted((folder / "video_scripts").glob("*.json")):
        raw = f.read_text(encoding="utf-8")
        doc = json.loads(raw)
        topic = topic_of.get(doc["key"])
        if topic is None:
            continue
        swaps = {}
        for b in doc["video_script"]["beats"]:
            for v in [b["on_screen"], *b["marks"].values()]:
                new = fix_text(v, topic)
                if new != v:
                    print(f"{doc['key']}: {v[:110]!r}\n    -> {new[:110]!r}")
                    swaps[v] = new
        if swaps:
            changed += 1
            # swap the encoded strings in place, so the file keeps its own layout
            for v, new in swaps.items():
                raw = raw.replace(json.dumps(v, ensure_ascii=False), json.dumps(new, ensure_ascii=False))
            doc = json.loads(raw)
            if write:
                f.write_text(raw, encoding="utf-8")
        hits = book_numbers(doc["title"], doc["description"], doc["teaching_notes"],
                            *readable_strings(doc["video_script"]))
        if hits:
            left += 1
            print(f"LEFT {f.name}: {sorted(set(hits))}")
    print(f"{folder}: {changed} files {'rewritten' if write else 'would change'}; {left} still carry numbering")


if __name__ == "__main__":
    main(sys.argv[1:])
