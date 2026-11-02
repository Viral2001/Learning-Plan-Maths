# -*- coding: utf-8 -*-
"""The part of a chapter builder that is the same for every chapter: planned video slots, the author worklist,
loading the authored scripts, the plan nodes and the plan-level video_coverage (docs/28).

A chapter builder does three chapter-specific things and calls these for the rest:
  1. for each delivered concept, list its slots in play order with `slot(...)`:
       hook (the chapter opener, before the concept), worked (one per solved book item; the concept video),
       theorem, exercise (one per book question, sub-parts together; the question video);
  2. call `number_slots(concept_id, slots)` to give each slot its media id (VID1..n on that concept);
  3. at the end, `write_worklist(...)` (build.py --video-worklist) or `build_nodes(...)` + `coverage(...)`.

Script files live in <chapter>/video_scripts/<key>.json, one video per file:
    {"key", "title", "description", "teaching_notes", "video_script": {...}}
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import node as N  # noqa: E402
import numwords  # noqa: E402

UNLOCK = {"hook": "always", "worked": "always", "exercise": "after_attempt", "theorem": "always",
          "story": "always"}
PLACEMENT = {"hook": "before", "worked": "after", "exercise": "after", "theorem": "after", "story": "after"}


def slot(key, kind, *, source, item_ids=(), items=(), answer="", **extra):
    """One planned video.

    key       unique, filesystem-safe (e.g. 'c9.T2.D2.E1'); the script file is video_scripts/<key>.json
    source    the book labels the video covers (e.g. ['Isosceles Right Triangles, Q2']); for a hook, the topic id
    item_ids  the coverage ids this video covers (rows in video_coverage)
    items     [{id, label, question, steps, answer}] the book items, for the author
    answer    the item's answer text, which check.py compares with final_answer
    """
    d = {"key": key, "kind": kind, "placement": PLACEMENT[kind], "unlock": UNLOCK[kind],
         "source": list(source), "item_ids": list(item_ids), "items": list(items), "answer": answer}
    d.update(extra)
    return d


def number_slots(concept_id, slots, **common):
    """Give each slot its media id on the concept, in order (hooks first, then the rest as listed)."""
    ordered = [s for s in slots if s["kind"] == "hook"] + [s for s in slots if s["kind"] != "hook"]
    for n, s in enumerate(ordered, 1):
        s["video_id"] = f"{concept_id}.VID{n}"
        s["concept_id"] = concept_id
        if s["kind"] == "exercise":
            s["item_concept"] = concept_id
        for k, v in common.items():
            s.setdefault(k, v)
    return ordered


def exercise_numbers(items):
    """{item_id: numbers in its question}, for the book guard."""
    out = {}
    for it in items:
        vals = numwords.digit_numbers(it.get("question", ""))
        if vals:
            out[it["id"]] = vals
    return out


def write_worklist(path, header, slots):
    """Write video_worklist.json. Keys must be unique; returns the number of videos."""
    keys = [s["key"] for s in slots]
    dup = {k for k in keys if keys.count(k) > 1}
    if dup:
        raise SystemExit(f"duplicate video keys: {sorted(dup)}")
    data = {"chapter": header, "videos": slots}
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    return len(slots)


def load_worklist(path):
    p = Path(path)
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def load_scripts(folder):
    """{key: script file} from <chapter>/video_scripts/. The chapter photo library, <chapter>/photos/, rides along
    in memory as doc["_photo_lib"] (never written back), so build_nodes and script_check_errors can use it."""
    from check import load_photos, load_book_rules
    out = {}
    folder = Path(folder)
    if not folder.exists():
        return out
    lib = load_photos(folder.parent / "photos")
    rules = load_book_rules(folder.parent)
    for f in sorted(folder.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        k = d.get("key")
        if k in out:
            raise SystemExit(f"two script files carry the key {k}")
        d["_photo_lib"] = lib
        d["_book_rules"] = rules
        out[k] = d
    return out


def photo_library(scripts):
    for d in scripts.values():
        return d.get("_photo_lib") or {}
    return {}


def build_nodes(slots, scripts, *, asset_base, chapter_label, related=None):
    """Plan media nodes for these slots (one concept's, or all). Missing scripts are returned, not invented."""
    nodes, missing = [], []
    for s in slots:
        doc = scripts.get(s["key"])
        if doc is None:
            missing.append(s["key"])
            continue
        nd = N.video_node(doc, video_id=s["video_id"], concept_id=s["concept_id"], chapter_label=chapter_label,
                          planned_url=f"{asset_base}/video_v3/{s['video_id']}.mp4",
                          related_concept_ids=(related or {}).get(s["key"], []),
                          photos=doc.get("_photo_lib"), photo_base=f"{asset_base}/photo_v3")
        if s.get("handover") and nd["interaction_points"]:
            nd["interaction_points"][-1]["handover"] = s["handover"]
        nd["serves_items"] = list(s["item_ids"])
        nodes.append(nd)
    return nodes, missing


def coverage(slots, labels):
    """Plan-level video_coverage rows: every covered book item against its video."""
    rows = []
    for s in slots:
        for iid in s["item_ids"]:
            rows.append({"book_item": labels.get(iid, iid), "item_id": iid, "video_id": s["video_id"],
                         "kind": s["kind"]})
    return rows


def script_check_errors(slots, scripts, header):
    """Every authored script checked against its slot (check.py)."""
    from check import book_numbers, check_script, check_photo_library
    errs = []
    lib = photo_library(scripts)
    chapter = dict(header, photos=lib, book_rules=header.get("book_rules") or next(
        (d.get("_book_rules") for d in scripts.values() if d), {}),
        worked_keys=[s["key"] for s in slots])
    for s in slots:
        doc = scripts.get(s["key"])
        if doc is None:
            errs.append(f"{s['key']}: no script file (video_scripts/{s['key']}.json)")
            continue
        for e in check_script(doc["video_script"], s, chapter):
            errs.append(f"{s['key']} ({s['video_id']}): {e}")
        if (hits := book_numbers(*(doc.get(k, "") for k in ("title", "description", "teaching_notes")))):
            errs.append(f"{s['key']} ({s['video_id']}): book numbering in title, description or teaching_notes "
                        f"{sorted(set(hits))[:4]}")
    errs += check_photo_library(lib, {k: d for k, d in scripts.items() if d is not None}, header.get("grade"))
    extra = set(scripts) - {s["key"] for s in slots}
    for k in sorted(extra):
        errs.append(f"{k}: a script file for a video the worklist no longer has")
    return errs
