# -*- coding: utf-8 -*-
"""Video-script gate: wraps core/video_script/check.py's Keeko-design contract checks as a plan+config gate.

core/video_script/check.py already implements almost everything the approved plan asks this gate to cover
(exactly one hook per chapter, the four script rules, the photo rule, lengths/bookmarks/Keeko+think-and-tell/book-numbering/
book-guard checks) - but it expects two inputs this gate's caller never supplies: a `video_worklist.json`
(the chapter's own authored plan for every video - kind, concept, answer, forbid_words, length_override,
book_items, exercise_numbers, book_rules, photos) and a `by_key` lookup built from it. `gate_runner.py` only
ever hands a gate `(plan, config)`, so this module's job is to build an equivalent, synthetic worklist out of
the plan's own media nodes (every `type: "video"` node already carries its full `video_script` dict, whose
keys were verified against `core/video_script/contract.py`'s `SCRIPT_KEYS` on the three reference phase2
plans - they match exactly), then hand that to `check.check_plan()` so every one of its checks still runs.

What this gate CAN verify from `plan` alone (every video's `video_script` is checked in full against the
Keeko-design contract - shape, lengths, beats, bookmarks, banned words/phrases, one think-and-tell, Keeko's raised hand and wrong idea,
book-numbering, the four script rules' tool-reference ban, theorem-states-the-theorem, plus the plan-level
checks: exactly one hook video and it sits in the first topic and shows a photo, the first topic has exactly
one video, and `video_coverage` is shaped correctly):
  - everything `check.check_script()` / `check.check_plan()` check that depends only on each video's own
    `video_script` dict and the plan's own structure (modules/segments/topics/concepts, `video_coverage`).

What this gate CANNOT fully verify from `plan` + `config` alone, because the data lives in sibling files a
gate never receives (explicit limitations - pass the optional `config` keys below to lift them when the
caller has that data to hand):
  - **book_rules.json** (rule 3, "nothing outside the textbook"): the chapter's allowed character `names`
    and `banned_words`, plus each theorem video's required stated phrases, live beside `video_worklist.json`,
    not in the plan. Pass `config["book_rules"]` ({"names": [...], "banned_words": [...], "theorems": {...}})
    to enforce it; without it, this check is skipped (never a false positive, since an empty rule set simply
    allows everything).
  - **the chapter's photos/ library**: each photo's full entry (subject, prompt, alt text) lives in its own
    file there. Without `config["photos"]` ({photo_id: entry}), this gate still checks every beat's own
    `{id, placement}` shape, that the right beat `role`/`block`/`on_screen` phrasing is used, and the "no
    held-back answer appears in the photo" check (which degrades gracefully to a no-op without the library
    text) - but it suppresses the one check guaranteed to false-positive without the library ("photo X is
    not in the chapter's photos library"), since every real chapter's hook photo would otherwise always fail
    this gate. Pass `config["photos"]` to get that check for real, plus the "every library photo is shown
    somewhere" audit (`check.check_photo_library`).
  - **the book guard** (a hook/theorem video never reusing another book question's
    numbers): needs `chapter.exercise_numbers`, each book item's own printed numbers, authored in
    `video_worklist.json` and not reproduced in the plan. Pass `config["exercise_numbers"]`; otherwise this
    check is skipped entirely (its code only runs `if guard:`, so absence is a silent no-op, not a false
    negative disguised as a pass - it is simply not run).
  - **per-video forbid_words / length_override / item_concept / answer**: these are per-video authoring
    choices from `video_worklist.json` that leave no trace in the built plan (the plan does not record "this
    chapter withheld the word X until this video" or "this item's printed answer is Y"). Pass
    `config["video_forbid_words"]`, `config["video_length_override"]`, `config["video_item_concept"]`,
    `config["video_answers"]` (each `{video_id: value}`) to restore them per video; without them those few
    checks are skipped for that video (the "answer agrees with final_answer" check, the "exercise video sits
    on the concept that asked it" check, and any chapter-specific word budget override).
  - **`book_items`** (used only to flag an item with zero videos): this gate derives it from the plan's own
    `video_coverage` keys, so that one check is self-referential, not an independent audit of a book item
    that was never scripted at all - the same structural limitation `coverage.py` documents for
    `ncert_coverage`. Pass `config["book_items"]` (an independently authored master list) to make it real.
  - **the interactive-video/minimal-tool rule** (pause at every example/question until answered, free-try
    tool before the explanation resumes): `core/video_script/check.py` has no field for this at all - a
    video's `video_script` carries no "a tool preceded this" marker, so there is nothing in the contract to
    wrap. Per the approved plan this is a chapter-level OPT-IN (`config.get("interactive_video_variant")`),
    not a universal gate. When turned on, `check_interactive_variant()` below checks the two things the plan
    JSON *does* expose - that worked/exercise/theorem videos are flagged `interactive` with at least one
    `interaction_points` entry (the pause), and that a topic's free-try tool sits before its explanatory
    video in document order - but it cannot inspect actual render/runtime pause-until-answered behaviour,
    only the authored metadata that asks for it.

    python -B video_script_rules.py <plan.json>      print the problems found, if any
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_VS_DIR = _HERE.parent / "core" / "video_script"
if str(_VS_DIR) not in sys.path:
    sys.path.insert(0, str(_VS_DIR))
import check as _vscheck  # noqa: E402  (core/video_script/check.py; it self-inserts its own dir for `contract`)

PHOTO_LIBRARY_MSG = "is not in the chapter's photos/ library"


def walk_topics(plan):
    for module in plan.get("modules") or []:
        for segment in module.get("segments") or []:
            for topic in segment.get("topics") or []:
                yield topic


def _video_nodes(plan):
    out = []
    for topic in walk_topics(plan):
        for node in topic.get("media") or []:
            if node.get("type") == "video" and node.get("video_script"):
                out.append(node)
    return out


def _synthetic_worklist(plan, config):
    """An equivalent of the authored video_worklist.json, built only from what `plan` + `config` carry.
    See the module docstring's "CANNOT fully verify" section for exactly what each entry is missing."""
    videos = []
    for node in _video_nodes(plan):
        vs = node["video_script"]
        vid = node.get("id")
        entry = {
            "key": vid,
            "video_id": vid,
            "kind": vs.get("kind"),
            "concept_id": node.get("concept_id"),
            "source_key": node.get("source_video_key"),
        }
        fw = (config.get("video_forbid_words") or {}).get(vid)
        if fw:
            entry["forbid_words"] = fw
        lo = (config.get("video_length_override") or {}).get(vid)
        if lo:
            entry["length_override"] = lo
        ic = (config.get("video_item_concept") or {}).get(vid)
        if ic:
            entry["item_concept"] = ic
        ans = (config.get("video_answers") or {}).get(vid)
        if ans:
            entry["answer"] = ans
        videos.append(entry)

    book_items = config.get("book_items")
    if not book_items:
        # derived from the plan's own video_coverage: self-referential, see docstring limitation
        book_items = sorted({r.get("item_id") for r in (plan.get("video_coverage") or []) if r.get("item_id")})

    header = {
        "chapter_id": plan.get("chapter_id"),
        "name": plan.get("chapter_name"),
        "grade": plan.get("grade"),
        "allow_words": config.get("allow_words", []),
        "length_override": config.get("length_override", {}),
        "exercise_numbers": config.get("exercise_numbers", {}),
        "hard_words": config.get("hard_words", []),
        "book_items": book_items,
        "book_rules": config.get("book_rules", {}),
        "photos": config.get("photos", {}),
        # any video of the chapter may be called back: by plan id, or by the script key the node was built from
        "worked_keys": [k for v in videos for k in (v["key"], v.get("source_key")) if k],
    }
    return {"chapter": header, "videos": videos}


def check_interactive_variant(plan, config):
    """Chapter-level opt-in (config["interactive_video_variant"]), per the approved plan - see the module
    docstring's last bullet for exactly what this can and cannot check."""
    E = []
    for node in _video_nodes(plan):
        vs = node["video_script"]
        if vs.get("kind") in ("worked", "exercise", "theorem"):
            if not node.get("interactive"):
                E.append("%s: interactive_video_variant is on; a %s video must be interactive"
                         % (node.get("id"), vs["kind"]))
            elif not node.get("interaction_points"):
                E.append("%s: interactive_video_variant is on; a %s video needs at least one "
                         "interaction_point (the pause at the question)" % (node.get("id"), vs["kind"]))
    for topic in walk_topics(plan):
        media = topic.get("media") or []
        tool_idx = next((i for i, n in enumerate(media) if n.get("type") == "2d_tool"), None)
        if tool_idx is None:
            continue
        for i, n in enumerate(media):
            if n.get("type") != "video":
                continue
            if (n.get("video_script") or {}).get("kind") not in ("worked", "exercise", "theorem"):
                continue
            if i < tool_idx:
                E.append("%s: interactive_video_variant is on; the free-try tool should come before "
                         "the explanation video in %s" % (n.get("id"), topic.get("topic_id")))
    return E


def check(plan, config=None):
    """Return a list of problem strings; empty means clean. See the module docstring for what `config`
    keys lift which limitation."""
    config = config or {}
    if not plan.get("modules"):
        # core/video_script/check.py's check_plan() indexes plan["modules"] directly and would raise;
        # media_content.preflight() already reports "no modules" as its own structural problem, so this
        # gate reports the same thing in its own voice instead of crashing gate_runner.
        return ["no modules; nothing to check"]
    wl = _synthetic_worklist(plan, config)
    by_key = {v["video_id"]: v for v in wl["videos"]}

    errors = _vscheck.check_plan(plan, wl, by_key, check_scripts=True)

    if not config.get("photos"):
        # no sibling photos/ library supplied: this one check would false-positive on every real chapter's
        # hook photo (see docstring), so it is suppressed; every other photo-beat check still runs.
        errors = [e for e in errors if PHOTO_LIBRARY_MSG not in e]

    if config.get("interactive_video_variant"):
        errors += check_interactive_variant(plan, config)

    return errors


def summarise(plan):
    videos = _video_nodes(plan)
    kinds = {}
    for n in videos:
        k = (n.get("video_script") or {}).get("kind")
        kinds[k] = kinds.get(k, 0) + 1
    return {"videos": len(videos), "by_kind": kinds}


if __name__ == "__main__":
    import io
    for path in sys.argv[1:]:
        plan = json.load(io.open(path, encoding="utf-8"))
        problems = check(plan)
        print("%s: %d problem(s)" % (path, len(problems)))
        for p in problems:
            print("  -", p)
        print("  summary:", summarise(plan))
