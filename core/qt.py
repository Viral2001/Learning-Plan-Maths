# -*- coding: utf-8 -*-
"""Insert QT (question-topic) sibling topics after instructional topics that carry exercise video slots.

Generalized from the maths6_ch3 new-design `qt.py`. Called from a chapter's build.py after assemble().
Modifies the plan dict in-place and the vslots_all list in-place. Returns the cid_map (old_cid -> new_cid)
so that the caller can rekey pin files.

One QT concept per exercise slot. The worked-example blocks whose video_media_id matches the exercise
video are moved from the teaching concept into the QT concept; video media nodes stay on the teaching
topic's media list (reachable via the QT content block's video_media_id after rename).

Excluded from QT: framing (intro) and summary topics.

This pipeline builds straight into Phase 2 shape (no `_V3` chapter, no `to_phase2.py` mirror), so the
inserted topic is written directly as `topic_type: "instructional"` -- the Phase 2 API has never accepted
`question_topic`, and there is no later patch step that demotes it. `source_type` and `topic_category`
stay `"question_topic"` / `"practice"` so gates and tooling can still tell a QT topic apart from a taught
topic without relying on `topic_type`.

Parameters: (plan, vslots_all, media_tag, strand_map) -> returns cid_map.
"""
from __future__ import annotations

import re

from core import question_naming as QN

_MID_PAT = re.compile(r'^(M\d+\.S\d+\.T\d+\.C\d+)(\..+)$')


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def _vid_to_cid(vid: str) -> str:
    """'M1.S3.T3.C8.VID2' -> 'M1.S3.T3.C8'."""
    return re.sub(r'\.(VID|IMG|2D|3D|SIM)\d+$', '', vid)


def _build_replacer(cid_map: dict, tid_map: dict):
    """Single-pass regex replacer: all old IDs replaced atomically."""
    merged = {}
    merged.update(tid_map)
    merged.update(cid_map)
    if not merged:
        return lambda s: s
    sorted_keys = sorted(merged.keys(), key=len, reverse=True)
    pattern = re.compile("|".join(re.escape(k) for k in sorted_keys))
    return lambda s: pattern.sub(lambda m: merged[m.group(0)], s)


def _fix_list(lst: list, fix) -> list:
    return [fix(x) if isinstance(x, str) else x for x in lst]


def _item_kind(item_ids: list) -> str:
    """Classify an exercise: figure_it_out if any item_id contains 'FiO', else unsolved."""
    for iid in item_ids:
        if "FiO" in iid:
            return "figure_it_out"
    return "unsolved"


def _concept_name(slot: dict) -> str:
    """Derive a concept name from the slot: use question text (capped), or source label."""
    items = slot.get("items", [])
    if items and items[0].get("question"):
        q = items[0]["question"]
        return q[:70].rstrip() + ("..." if len(q) > 70 else "")
    src = slot.get("source", [])
    return src[0] if src else slot["key"]


_BLOCK_COMMON_FIELDS = ("block_kind", "item_kind", "book_kind", "coverage_id", "exercise_id",
                        "ncert_refs", "book_number", "example_id")


def _question_answer_blocks(blocks: list) -> tuple:
    """Split each combined question+solution block into a question-only block (just the question, no
    working) and an answer-only block (the numbered working and the answer, no video on the question
    side - core/question_naming.py's two concepts attach to these). Both keep the book-item fields
    (coverage_id, item_kind, ...) so per-block gates still find them. question_tex/steps_tex/answer_tex
    (core/solutions/bind.py's inline-LaTeX text, once solutions.json has this item) carry over too, and
    the displayed text is built from them when present - core/solutions/placeholders.py and attach.py
    tag it with "[Image: <title>]" markers if the working ends up on more than one solution card.

    This split is not pure field-copying. Before trusting the source block's own `question`/`steps`/
    `answer` separation, read it: the question side must be the problem exactly as asked, with no part
    of the method or the result folded into it; the answer side must be every step of the working, in
    order, ending in the result. When the source has no worked method or printed answer at all (`steps`
    and `answer` both empty - an open "make your own"/"do you agree"/reader-estimate item, or a genuinely
    unsolved exploration), author an accurate one from the question and the chapter's own content before
    splitting - never hand the answer concept an empty block. Same policy, same wording, as
    math_solutions/skill/references/format-rules.md rule 9 ("solve it yourself... never skip the item or
    submit an unverified guess"), which this mirrors for the learning plan's own Q/A concepts rather than
    a standalone solutions.json document."""
    q_blocks, a_blocks = [], []
    for b in blocks:
        common = {k: b[k] for k in _BLOCK_COMMON_FIELDS if k in b}
        question, steps, answer = b.get("question") or "", list(b.get("steps") or []), b.get("answer") or ""
        q_disp = b.get("question_tex") or question
        steps_disp = b.get("steps_tex") or steps
        answer_disp = b.get("answer_tex") or answer
        qb = dict(common, type="paragraph", question=question, steps=[], answer="",
                  text=q_disp, publication_text=q_disp)
        if b.get("question_tex"):
            qb["question_tex"] = b["question_tex"]
        if b.get("q_figure"):
            qb["q_figure"] = b["q_figure"]
        q_blocks.append(qb)
        # The step index itself is wrapped as "$N$." per LATEX_REFERENCE.md's step-identification rule
        # only when steps_tex is actually present - a plain-text fallback (no solutions.json entry yet)
        # must stay bare, since nothing else in that fallback text is LaTeX either.
        _idx_fmt = "$%d$. %s" if b.get("steps_tex") else "%d. %s"
        a_text = "\n".join([_idx_fmt % (i, st) for i, st in enumerate(steps_disp, 1)]
                            + (["Answer: %s" % answer_disp] if answer_disp else []))
        ab = dict(common, type="paragraph", question=question, steps=steps, answer=answer,
                  text=a_text, publication_text=a_text)
        if b.get("steps_tex"):
            ab["steps_tex"] = b["steps_tex"]
        if b.get("answer_tex"):
            ab["answer_tex"] = b["answer_tex"]
        if b.get("s_figure"):
            ab["s_figure"] = b["s_figure"]
        if b.get("video_media_id"):
            ab["video_media_id"] = b["video_media_id"]
        a_blocks.append(ab)
    return q_blocks, a_blocks


# ---------------------------------------------------------------------------
# main entry point
# ---------------------------------------------------------------------------

def apply(plan: dict, vslots_all: list, media_tag: str, strand_map: dict,  # noqa: C901
          enrichment_qt: bool = False, own_video: bool = False, keep_first: bool = False,
          name_fn=None, topic_prefix: str = None) -> dict:
    """Insert QT topics, renumber the chapter, rebuild objectives.

    enrichment_qt=True (opt-in; the default keeps the old shape) builds the maths7_ch10 "Figure it
    Out" shape instead: topic "Figure it Out: <parent>", source_type "exercise", topic_category
    "enrichment"; each question concept is enrichment (no objective), is named by its book label,
    and OWNS its video - the exercise video node moves from the teaching topic into the QT topic as
    <QT concept id>.VID1. A moved block's `related_tool` (a tool key) links the parent topic's tool
    node to the question concept (related_concept_ids / reused_in_topics).
    own_video=True (the maths8_ch9 shape): topic "Questions: <parent>", each question concept stays a
    taught concept with an objective but OWNS its exercise video (moved as <QT concept id>.VID1), so every
    concept carries one video. keep_first=True leaves each topic's first exercise (with its video) on the
    teaching topic's practice concept. name_fn(slot) -> str names a question concept (e.g. "Unit, Q3").
    topic_prefix="Questions" (the question layout of chapter_template: enrichment_qt=True,
    topic_prefix="Questions"; see docs/00_overview.md) names topics and concepts by book category instead
    (core/question_naming.py), from each item's own book label: a teaching topic's exercise slots are
    grouped by category (exercise set / Figure it Out / example / Let us do / anything else), each group
    becoming its own "Questions: <category>" topic (e.g. "Questions: Exercise Set 5.1", "Questions:
    Example") in book order, with concepts named "Exercise Set 5.1: Q1", "Example 3: Q", etc. A topic whose
    slots span more than one category gets one Questions topic per category, not one mixed topic.
    Returns cid_map (old_cid -> new_cid) for the caller to rekey pin files.
    Modifies plan and vslots_all in-place.
    """

    # ---- 1. exercise slots ------------------------------------------------
    ex_slots = [s for s in vslots_all if s.get("kind") == "exercise"]
    if not ex_slots:
        return {}

    # old concept_id -> [slot]
    ex_by_cid: dict = {}
    for s in ex_slots:
        cid = _vid_to_cid(s["video_id"])
        ex_by_cid.setdefault(cid, []).append(s)

    # ---- 2. flatten plan --------------------------------------------------
    flat = []  # [(module_id, topic_node)]
    for m in plan["modules"]:
        for seg in m["segments"]:
            for t in seg["topics"]:
                flat.append((m["module_id"], t))

    all_cons   = {c["concept_id"]: c for _, t in flat for c in t["concepts"]}
    cid_to_tid = {c["concept_id"]: t["topic_id"] for _, t in flat for c in t["concepts"]}
    tid_to_mid = {t["topic_id"]: mid for mid, t in flat}
    flat_by_tid = {t["topic_id"]: (mid, t) for mid, t in flat}

    # ---- 3. group exercise slots by parent topic --------------------------
    ex_by_topic: dict = {}   # old_topic_id -> [(slot, concept_node)]
    for cid, slots_list in ex_by_cid.items():
        c_node = all_cons.get(cid)
        if not c_node:
            continue
        tid = cid_to_tid[cid]
        topic_type = flat_by_tid[tid][1].get("topic_type", "")
        if topic_type in ("framing", "summary"):
            continue
        for s in slots_list:
            ex_by_topic.setdefault(tid, []).append((s, c_node))
    if keep_first:
        ex_by_topic = {k: v[1:] for k, v in ex_by_topic.items() if len(v) > 1}

    # ---- 4. strip exercise blocks from teaching concepts ------------------
    qt_raw: dict = {}   # old_topic_id -> [(slot, [moved_blocks])]
    for tid, pairs in ex_by_topic.items():
        for s, c_node in pairs:
            ex_vid = s["video_id"]
            moved = [b for b in c_node["content"]
                     if b.get("block_kind") == "worked_example"
                     and b.get("video_media_id") == ex_vid]
            # Set item_kind on moved blocks
            ik = _item_kind(s.get("item_ids", []))
            for b in moved:
                b["item_kind"] = ik
            moved_set = {id(b) for b in moved}
            c_node["content"] = [b for b in c_node["content"] if id(b) not in moved_set]
            c_node["ncert_refs"] = [r for r in c_node["ncert_refs"] if r not in s.get("item_ids", [])]
            vnode = None
            if enrichment_qt or own_video:
                ptopic = flat_by_tid[tid][1]
                vnode = next((x for x in ptopic.get("media", []) if x.get("id") == ex_vid), None)
                if vnode is not None:
                    ptopic["media"] = [x for x in ptopic["media"] if x is not vnode]
                    c_node["media_ids"] = [m for m in c_node.get("media_ids", []) if m != ex_vid]
                    if c_node.get("video_media_ids"):
                        c_node["video_media_ids"] = [m for m in c_node["video_media_ids"] if m != ex_vid]
            qt_raw.setdefault(tid, []).append((s, moved, vnode))

    # ---- 5. build QT topic stubs -----------------------------------------
    # topic_prefix="Questions" (chapter_template's question_layout) groups a topic's exercise slots by
    # book category (core/question_naming.py) instead of lumping them into one bucket, so a topic with
    # both an Example and a Figure it Out question gets two Questions topics, in book order. Every other
    # caller keeps its old single-bucket-per-topic shape untouched (gkey falls back to old_tid itself).
    use_new_naming = bool(topic_prefix)

    qt_stubs: dict = {}  # old_topic_id -> [qt_topic_dict, ...]
    for old_tid, slot_block_pairs in qt_raw.items():
        mid = tid_to_mid[old_tid]
        parent_name = flat_by_tid[old_tid][1]["topic_name"]

        groups: dict = {}    # gkey -> {"category", "topic_suffix", "items": [(s, moved, vnode, concept_prefix)]}
        group_order: list = []
        for s, moved, vnode in slot_block_pairs:
            if use_new_naming:
                label = (moved[0].get("book_number") if moved else None) or (s.get("source") or [None])[0] or ""
                cov = (moved[0].get("coverage_id") if moved else None) or next(iter(s.get("item_ids") or []), None)
                category, topic_suffix, concept_prefix = QN.classify(label, cov)
                gkey = (category, topic_suffix)
            else:
                category, topic_suffix, concept_prefix, gkey = None, None, None, old_tid
            if gkey not in groups:
                groups[gkey] = {"category": category, "topic_suffix": topic_suffix, "items": []}
                group_order.append(gkey)
            groups[gkey]["items"].append((s, moved, vnode, concept_prefix))

        stubs_for_topic = []
        for gkey in group_order:
            grp = groups[gkey]
            subject = grp["topic_suffix"] if use_new_naming else parent_name

            qt_concepts = []
            qt_media = []
            for seq, (s, moved, vnode, concept_prefix) in enumerate(grp["items"], 1):
                ik = _item_kind(s.get("item_ids", []))
                concept_name = _concept_name(s)
                if enrichment_qt and moved and moved[0].get("book_number"):
                    concept_name = moved[0]["book_number"]
                if name_fn:
                    concept_name = name_fn(s) or concept_name
                if moved:
                    blocks = list(moved)
                else:
                    # Fallback for X.{r} slots (no paired worked example in plan text). When the slot carries
                    # its book item with a solution (steps + answer, e.g. from solutions.json) the block holds
                    # that; otherwise it is the placeholder that sends the student to the book.
                    it = next((i for i in s.get("items") or [] if i.get("question") and i.get("steps")
                               and i.get("answer")), None)
                    if it:
                        text = "\n".join(["Practice problem: %s" % it["question"]]
                                         + ["%d. %s" % (n, st) for n, st in enumerate(it["steps"], 1)]
                                         + ["Answer: %s" % it["answer"]])
                    else:
                        text = ("Work through the practice problem. Read the question in the book and attempt "
                                "it before watching the video solution.")
                    blocks = [{
                        "type": "paragraph",
                        "block_kind": "worked_example",
                        "question": it["question"] if it else "",
                        "steps": list(it["steps"]) if it else [],
                        "answer": it["answer"] if it else "",
                        "text": text,
                        "publication_text": text,
                        "video_media_id": s["video_id"],
                        "example_id": f"{s['key']}.qt.1",
                        "item_kind": ik,
                    }]
                    if it:
                        blocks[0]["coverage_id"] = it.get("id") or (s.get("item_ids") or [""])[0]
                authored_key = f"qt.{s['key']}"
                obj_text = ("Attempt each practice question independently, working through "
                            "every step before viewing the video solution and checking the answer.")

                # topic_prefix="Questions" also splits each question into its own concept (titled with
                # "Q"/"Qn") and a paired answer concept (titled with "Ans"/"Ansn", core/question_naming.py):
                # the answer concept carries the video and the solution card(s), the question concept
                # carries only the question card. Every other caller keeps one concept per question.
                if use_new_naming:
                    q_blocks, a_blocks = _question_answer_blocks(blocks)
                    base = {
                        "key_terms": [], "objective_id": None, "objective_ids": [],
                        "source_segment_role": "practice", "media_ids": [],
                        "ncert_refs": list(s.get("item_ids", [])), "authored_key": authored_key,
                        "tier": None, "misconceptions": [], "predict_first": "",
                        "media_key": f"qt.{s['key']}", "enrichment_type": "content", "is_enrichment": False,
                        "mixed_objective_ids": [], "recap_objective_ids": [],
                        "adaptive": {"tier": None, "discovery": False, "hint_ladder": False, "rescue": False,
                                     "say": False, "check_my_thinking": False, "added_for_tier": []},
                        "_qt": True, "_qt_obj_text": obj_text,
                    }
                    q_concept = {**base, "concept_id": "PLACEHOLDER",
                                 "concept_name": QN.concept_title(grp["category"], concept_prefix, seq,
                                                                   role="question"),
                                 "content": q_blocks, "source_media": None,
                                 "estimated_minutes": 2 * max(len(moved), 1), "qt_part": "question",
                                 "_vnode": None, "_slot": None}
                    a_concept = {**base, "concept_id": "PLACEHOLDER",
                                 "concept_name": QN.concept_title(grp["category"], concept_prefix, seq,
                                                                   role="answer"),
                                 "content": a_blocks, "source_media": "video" if vnode is not None else None,
                                 "estimated_minutes": 5 * max(len(moved), 1), "qt_part": "answer",
                                 "_vnode": vnode, "_slot": s}
                    if enrichment_qt:
                        for c in (q_concept, a_concept):
                            c.update({"is_enrichment": True, "enrichment_type": "enrichment", "authored_key": None})
                    if vnode is not None:
                        qt_media.append(vnode)
                    qt_concepts.append(q_concept)
                    qt_concepts.append(a_concept)
                    continue

                qt_concepts.append({
                    "concept_id": "PLACEHOLDER",
                    "concept_name": concept_name,
                    "content": blocks,
                    "key_terms": [],
                    "objective_id": None,
                    "objective_ids": [],
                    "source_segment_role": "practice",
                    "source_media": "video",
                    "media_ids": [],
                    "ncert_refs": list(s.get("item_ids", [])),
                    "authored_key": authored_key,
                    "tier": None,
                    "misconceptions": [],
                    "predict_first": "",
                    "estimated_minutes": 5 * max(len(moved), 1),
                    "media_key": f"qt.{s['key']}",
                    "enrichment_type": "content",
                    "is_enrichment": False,
                    "mixed_objective_ids": [],
                    "recap_objective_ids": [],
                    "adaptive": {
                        "tier": None, "discovery": False, "hint_ladder": False,
                        "rescue": False, "say": False, "check_my_thinking": False,
                        "added_for_tier": [],
                    },
                    "_qt": True,
                    "_qt_obj_text": obj_text,
                    "_vnode": vnode,
                    "_slot": s,
                })
                if enrichment_qt:
                    qt_concepts[-1].update({"is_enrichment": True, "enrichment_type": "enrichment",
                                            "authored_key": None,
                                            "source_media": "video" if vnode is not None else None})
                    if vnode is not None:
                        qt_media.append(vnode)
                elif own_video:
                    if vnode is not None:
                        qt_media.append(vnode)
                    else:
                        qt_concepts[-1]["_vnode"] = None

            stubs_for_topic.append({
                "_qt": True,
                "topic_id": "PLACEHOLDER",
                "topic_name": (QN.topic_title(grp["topic_suffix"]) if use_new_naming
                               else f"{topic_prefix}: {parent_name}" if topic_prefix
                               else f"Figure it Out: {parent_name}" if enrichment_qt
                               else f"Questions: {parent_name}" if own_video else f"Practise: {parent_name}"),
                "topic_type": "instructional",
                "summary": f"Practice problems for {subject}.",
                "brief_summary": f"Practice problems for {subject}.",
                "detailed_summary": f"Practice problems for {subject}.",
                "topic_objective": None,
                "concepts": qt_concepts,
                "media": qt_media,
                "key_terms": [],
                "depends_on": [],
                "difficulty": "",
                "objective_ids": [],
                "learning_objectives": [],
                "important_points": [],
                "recall_questions": [],
                "concept_bullets": [c["concept_name"] for c in qt_concepts],
                "source_type": "exercise" if enrichment_qt else "question_topic",
                "topic_category": "enrichment" if enrichment_qt else "practice",
                "is_enrichment": bool(enrichment_qt),
                "source_topic_ids": [],
                "session_minutes": None,
                "estimated_minutes": sum(c["estimated_minutes"] for c in qt_concepts),
                "original_chunk": f"Practice problems for {subject}.",
                "publication_chunk": f"Practice problems for {subject}.",
                "primary_content_type": "video",
                "secondary_content_type": None,
                "tertiary_content_type": None,
                "available_content_types": ["video"],
                "estimated_exchanges": 0,
                "word_count": {"original": 0},
            })
        qt_stubs[old_tid] = stubs_for_topic

    # ---- 6. build new ordered flat list -----------------------------------
    new_flat = []   # [(mid, topic_node)]
    for mid, t in flat:
        new_flat.append((mid, t))
        for stub in qt_stubs.get(t["topic_id"], []):
            new_flat.append((mid, stub))

    # ---- 7. assign new topic/concept IDs; build rename maps ---------------
    cid_map: dict = {}   # old_cid -> new_cid
    tid_map: dict = {}   # old_tid -> new_tid

    global_c = 0
    global_t = 0

    for mid, t in new_flat:
        global_t += 1
        new_tid = f"{mid}.S{global_t}.T{global_t}"

        if t.get("_qt"):
            t["topic_id"] = new_tid
        else:
            old_tid = t["topic_id"]
            if old_tid != new_tid:
                tid_map[old_tid] = new_tid
            t["topic_id"] = new_tid

        for c in t["concepts"]:
            global_c += 1
            new_cid = f"{new_tid}.C{global_c}"
            if t.get("_qt"):
                c["concept_id"] = new_cid
            else:
                old_cid = c["concept_id"]
                if old_cid != new_cid:
                    cid_map[old_cid] = new_cid
                c["concept_id"] = new_cid

    # enrichment_qt: rename each moved exercise video to <QT concept id>.VID1 and point its concept,
    # block and slot at it. These nodes are already final, so step 8 skips them.
    vid_map: dict = {}
    final_objs: set = set()   # id() of moved video nodes and their concepts: already final
    for mid, t in new_flat:
        for c in t["concepts"]:
            vnode, slot = c.pop("_vnode", None), c.pop("_slot", None)
            if vnode is None:
                continue
            old_vid, new_vid = vnode["id"], f"{c['concept_id']}.VID1"
            vid_map[old_vid] = new_vid
            final_objs.update((id(vnode), id(c)))
            vnode["id"] = new_vid
            vnode["concept_id"] = vnode["home_concept_id"] = c["concept_id"]
            c["media_ids"] = [new_vid]
            c["video_media_ids"] = [new_vid]
            c["walkthrough_video_id"] = new_vid
            for b in c["content"]:
                if b.get("video_media_id") == old_vid:
                    b["video_media_id"] = new_vid
            slot["concept_id"] = c["concept_id"]
            if slot.get("item_concept"):
                slot["item_concept"] = c["concept_id"]

    fix = _build_replacer({**cid_map, **vid_map}, tid_map)

    # ---- 8. fix cross-references in all nodes in new_flat -----------------
    for mid, t in new_flat:
        for x in t.get("media", []):
            if id(x) in final_objs:
                continue
            x["id"] = fix(x["id"])
            if "concept_id" in x:
                x["concept_id"] = fix(x["concept_id"])
            if "home_concept_id" in x:
                x["home_concept_id"] = fix(x["home_concept_id"])
            if x.get("related_concept_ids"):
                x["related_concept_ids"] = _fix_list(x["related_concept_ids"], fix)
            # URLs are FROZEN — they point at CDN assets that keep the old path
            # planned_url is a storage path, not an asset address — freeze it too
            # (the check_plan validates planned_url uniqueness; renaming breaks nothing there)
            if x.get("source_tool_ref"):
                x["source_tool_ref"] = fix(x["source_tool_ref"])

        for c in t["concepts"]:
            if id(c) in final_objs:
                continue
            if hasattr(c, "get"):
                c["media_ids"] = _fix_list(c.get("media_ids", []), fix)
                if c.get("walkthrough_video_id"):
                    c["walkthrough_video_id"] = fix(c["walkthrough_video_id"])
                if c.get("video_media_ids"):
                    c["video_media_ids"] = _fix_list(c["video_media_ids"], fix)
                if c.get("tool_media_id"):
                    c["tool_media_id"] = fix(c["tool_media_id"])
                if c.get("source_tool_ref"):
                    c["source_tool_ref"] = fix(c["source_tool_ref"])
                if c.get("reuses_media_ids"):
                    c["reuses_media_ids"] = _fix_list(c["reuses_media_ids"], fix)
                for b in c.get("content", []):
                    if b.get("video_media_id"):
                        b["video_media_id"] = fix(b["video_media_id"])
                    if b.get("image_media_id"):
                        b["image_media_id"] = fix(b["image_media_id"])
                    if b.get("solution_image_media_id"):
                        b["solution_image_media_id"] = fix(b["solution_image_media_id"])

        if not t.get("_qt"):
            t["depends_on"] = _fix_list(t.get("depends_on", []), fix)
            if t.get("topic_objective"):
                t["topic_objective"]["home_topic_id"] = fix(
                    t["topic_objective"]["home_topic_id"])

    # fix objectives
    for o in plan["objectives"]:
        o["anchor"]        = _fix_list(o["anchor"], fix)
        o["home_topic_id"] = fix(o["home_topic_id"])

    # fix ncert_coverage
    cov = plan["source_metadata"]["ncert_coverage"]
    for item_id in list(cov.keys()):
        cov[item_id] = _fix_list(cov[item_id], fix)

    # fix video_coverage
    for entry in plan.get("video_coverage", []):
        if entry.get("video_id"):
            entry["video_id"] = fix(entry["video_id"])

    # fix vslots_all in-place
    for s in vslots_all:
        moved_slot = s["video_id"] in vid_map
        s["video_id"] = fix(s["video_id"])
        if moved_slot:
            continue
        if s.get("concept_id"):
            s["concept_id"] = fix(s["concept_id"])
        if s.get("item_concept"):
            s["item_concept"] = fix(s["item_concept"])
        if s.get("topic_id"):
            s["topic_id"] = fix(s["topic_id"])

    # ---- 9. rebuild modules / segments from new_flat ----------------------
    for m in plan["modules"]:
        m["segments"] = []
    module_map = {m["module_id"]: m for m in plan["modules"]}

    prev_tid = None
    for mid, t in new_flat:
        t["depends_on"] = [prev_tid] if prev_tid else []
        new_tid = t["topic_id"]
        seg_num = int(new_tid.split(".S")[1].split(".T")[0])
        seg_id = f"{mid}.S{seg_num}"
        module_map[mid]["segments"].append({
            "segment_id": seg_id,
            "segment_name": t["topic_name"],
            "summary": t["summary"],
            "brief_summary": t["brief_summary"],
            "detailed_summary": t.get("detailed_summary", ""),
            "important_points": [],
            "recall_questions": [],
            "segment_objective_ids": list(t.get("objective_ids", [])),
            "topics": [t],
        })
        prev_tid = new_tid

    # ---- 10. rebuild objectives -------------------------------------------
    all_topics_final = [t for m in plan["modules"] for seg in m["segments"] for t in seg["topics"]]
    all_concepts_final = [c for t in all_topics_final for c in t["concepts"]]

    old_objs_by_oid = {o["objective_id"]: o for o in plan["objectives"]}
    mod_names = {m["module_id"]: m["module_name"] for m in plan["modules"]}

    new_objectives = []
    onum = 0
    # legacy_id is a strand-code (e.g. "N2", "A5"): a letter from strand_map (the chapter's own
    # subject-knowledge-strand catalog, see content.py.template's MODULE_STRANDS) plus a running
    # count WITHIN that strand, assigned in final document order - never the raw authored key or
    # module id, which are locators, not a strand taxonomy. A module with no strand_map entry falls
    # back to "G" (general) rather than leaking its module id into a field meant to hold a letter.
    strand_seq = {}

    cid_to_topic_final = {c["concept_id"]: t
                          for t in all_topics_final
                          for c in t["concepts"]}

    for c in all_concepts_final:
        if c["is_enrichment"]:
            c["objective_id"] = None
            c["objective_ids"] = []
            continue

        onum += 1
        new_oid = f"O{onum}"
        t_for_c = cid_to_topic_final[c["concept_id"]]
        mid_for_c = t_for_c["topic_id"].split(".")[0]
        strand = strand_map.get(mid_for_c, "G")

        if c.get("_qt"):
            strand_seq[strand] = strand_seq.get(strand, 0) + 1
            obj_text = c.pop("_qt_obj_text", "")
            new_objectives.append({
                "objective_id": new_oid,
                "objective_text": obj_text,
                "anchor": [c["concept_id"]],
                "status": "taught",
                "strand": strand,
                "strand_name": mod_names.get(mid_for_c, ""),
                "bloom_level": "apply",
                "home_topic_id": t_for_c["topic_id"],
                "legacy_id": "%s%d" % (strand, strand_seq[strand]),
            })
        else:
            old_oid = c.get("objective_id")
            if not old_oid:
                onum -= 1
                continue
            strand_seq[strand] = strand_seq.get(strand, 0) + 1
            o = dict(old_objs_by_oid[old_oid])
            o["objective_id"] = new_oid
            # Fix anchor (it was fixed in step 8, so it now has the new concept id)
            o["anchor"] = [c["concept_id"]]
            o.setdefault("strand", strand)
            o.setdefault("strand_name", mod_names.get(mid_for_c, ""))
            o["legacy_id"] = "%s%d" % (strand, strand_seq[strand])
            new_objectives.append(o)

        c["objective_id"] = new_oid
        c["objective_ids"] = [new_oid]

    plan["objectives"] = new_objectives

    # Sync topic objective_ids and segment_objective_ids
    for m in plan["modules"]:
        for seg in m["segments"]:
            for t in seg["topics"]:
                t["objective_ids"] = [c["objective_id"] for c in t["concepts"]
                                      if c.get("objective_id")]
                t["learning_objectives"] = [o for o in new_objectives
                                            if o["objective_id"] in t["objective_ids"]]
                seg["segment_objective_ids"] = list(t["objective_ids"])
            # Also update topic_objective references
            for t in seg["topics"]:
                if t.get("topic_objective"):
                    pass  # topic_objective doesn't reference an objective_id from plan["objectives"]

    # ---- 11. update ncert_coverage for new QT concept IDs ----------------
    for t in all_topics_final:
        if t.get("source_type") in ("question_topic", "exercise"):
            for c in t["concepts"]:
                for item_id in c["ncert_refs"]:
                    if item_id in cov:
                        if c["concept_id"] not in cov[item_id]:
                            cov[item_id].append(c["concept_id"])

    # ---- 12. update strand_to_objective_map ------------------------------
    # Keyed by each objective's own legacy_id (a strand-code like "N2"), the way the field
    # reference defines it - never by the concept's authored key, which is a build-time locator,
    # not a strand-taxonomy provenance id.
    plan["strand_to_objective_map"] = {
        o["legacy_id"]: o["objective_id"] for o in new_objectives if o.get("legacy_id")
    }

    # ---- 13. update estimated_time and summary_stats ----------------------
    all_media = [x for t in all_topics_final for x in t.get("media", [])]
    plan["estimated_time"] = round(sum(t.get("estimated_minutes", 0) for t in all_topics_final) / 60, 2)
    old_stats = plan["source_metadata"]["summary_stats"]
    qt_count = sum(1 for t in all_topics_final if t.get("source_type") in ("question_topic", "exercise"))
    plan["source_metadata"]["summary_stats"] = {
        **old_stats,
        "topics": len(all_topics_final),
        "concepts": len(all_concepts_final),
        "objectives": len(new_objectives),
        "topic_objectives": sum(1 for t in all_topics_final if t.get("topic_objective")),
        "videos": sum(1 for x in all_media if x["type"] == "video"),
        "images": sum(1 for x in all_media if x["type"] == "image"),
        "interactive_tools": sum(1 for x in all_media if x["type"] == "2d_tool"),
        "question_topics": qt_count,
        "walkthrough_video_placeholders": sum(1 for x in all_media if x["type"] == "video" and x.get("build_status") == "placeholder"),
        "image_placeholders": sum(1 for x in all_media if x["type"] == "image"),
    }

    # ---- 13b. enrichment_qt: link a question to its parent topic's own tool
    if enrichment_qt:
        parent = None
        for t in all_topics_final:
            if t.get("source_type") != "exercise":
                parent = t
                continue
            tools = [x for x in (parent or {}).get("media", []) if x.get("type") == "2d_tool"]
            for c in t["concepts"]:
                keys = {b["related_tool"] for b in c.get("content", []) if b.get("related_tool")}
                for x in tools:
                    tool_id = (x.get("tool_config") or {}).get("tool_id") or x.get("tool_id") or ""
                    if (tool_id[5:] if tool_id.startswith("tool_") else tool_id) not in keys:
                        continue
                    x.setdefault("related_concept_ids", [])
                    if c["concept_id"] not in x["related_concept_ids"]:
                        x["related_concept_ids"].append(c["concept_id"])
                    x.setdefault("reused_in_topics", [])
                    if t["topic_id"] not in x["reused_in_topics"]:
                        x["reused_in_topics"].append(t["topic_id"])

    # ---- 14. clean up internal flags -------------------------------------
    for t in all_topics_final:
        t.pop("_qt", None)
        for c in t["concepts"]:
            c.pop("_qt", None)
            c.pop("_qt_obj_text", None)

    return cid_map


def fix_pinned_refs(plan: dict, cid_map: dict) -> None:
    """After pin_images/pin_tools replace local nodes with pinned nodes (which carry old concept IDs
    in related_concept_ids), update those fields to the post-QT IDs.
    The KEEP_LOCAL fields (id, concept_id, home_concept_id) are already correct; only
    related_concept_ids needs fixing since it came from the pinned blob."""
    fix = _build_replacer(cid_map, {})
    for m in plan["modules"]:
        for seg in m["segments"]:
            for t in seg["topics"]:
                for x in t.get("media", []):
                    if x.get("related_concept_ids"):
                        x["related_concept_ids"] = _fix_list(x["related_concept_ids"], fix)


def remap_pin_file(pin_file: str, kind: str, cid_map: dict) -> None:
    """Re-key a pin file from pre-QT to post-QT media IDs (run ONCE after QT is first enabled).
    The media id format is <concept_id>.<KIND><n>; the concept_id prefix is remapped via cid_map.
    This writes the file in-place only if anything changed."""
    import json
    with open(pin_file, encoding="utf-8") as f:
        data = json.load(f)
    old_pins = data[kind]
    new_pins = {}
    for old_mid, node in old_pins.items():
        m = _MID_PAT.match(old_mid)
        if m:
            old_cid, suffix = m.groups()
            new_cid = cid_map.get(old_cid, old_cid)
            new_mid = new_cid + suffix
        else:
            new_mid = old_mid
        new_pins[new_mid] = node
    if new_pins != old_pins:
        data[kind] = new_pins
        with open(pin_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
        changed = sum(1 for k in new_pins if k not in old_pins)
        print(f"  rekeyed {kind} pin file: {changed} keys updated")
    else:
        print(f"  {kind} pin file already uses post-QT keys")
