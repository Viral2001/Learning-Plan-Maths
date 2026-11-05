# -*- coding: utf-8 -*-
"""Rewrite a LIVE Phase 2 plan into the question layout, from a per-chapter layout spec.

    python -I -X utf8 core/question_layout_live.py brief <live.json> [--book <book text>] -o brief.md
    python -I -X utf8 core/question_layout_live.py check <live.json> <spec.json>
    python -I -X utf8 core/question_layout_live.py apply <live.json> <spec.json> -o <out.json> [--report r.json]

For a chapter that is already live and whose authoring sources are not (or no longer) the thing to rebuild from. A
chapter that is built from sources uses chapter_template/build.py instead (docs/00_overview.md "Question layout").

The layout (docs/00_overview.md): every concept topic is followed by "Questions: <topic>", and every book question
(solved example, Figure it Out / exercise, answerable in-text prompt) is one concept of it, in the book's order, with its
own question image and solution image(s) as placeholders (core/solutions/placeholders.py).

What the engine changes, and nothing else: where a book question lives and in what order. Teaching text, plan-authored
examples, objectives, tools and rendered videos are carried over; ids are renumbered the way core/qt.py does, every
reference is rewritten by exact id match, media urls are frozen. A question that is a whole concept today (a Figure it
Out concept, a thin worked-example concept) moves with its node and its video; a question that is a block inside a
teaching or practice concept is cut out of it into a new concept (which has no video yet).

THE SPEC (one JSON per chapter; the author of it reads the book text and the `brief`):

    {"chapter_id": "cbse_eng_maths6_ch9", "source_version": 30,
     "canon":        {"old ref id": "ref id it is folded into"},      # optional: one book question = one ref id
     "rename_teach": {"<concept id>": "new name"},                     # optional: a teaching concept named after the
                                                                         example that moved out
     "topics": [ {"teach_topic": "<live topic id of a concept topic>",
                  "questions": [                                       # the Questions topic after it, in this order
                      {"keep": "<live id of a question concept already in its Questions topic>"},
                      {"name": "Example 1", "tier": "example" | "prompt" | "exercise",
                       "refs": ["<one coverage id>"],
                       "from": [ {"concept": "<id>", "block": 2},       # a block cut out of a concept, or
                                 {"concept": "<id>", "whole": true} ],  # a concept (one question block) moved whole
                       "keep_video_of": "<a whole-moved concept id>" | null,
                       "q_figure": "one sentence: the diagram the question card needs" | null,
                       "s_figure": "one sentence: the diagram the solution card needs" | null} ] } ] }

A Questions topic that exists today but is not in the spec keeps all its concepts. Existing question concepts the spec
does not list for a topic are appended after the listed ones, in their order (the engine never drops one).
"""
from __future__ import annotations

import argparse
import copy
import io
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from core.solutions import layout, placeholders          # noqa: E402
from core import question_naming as QN                   # noqa: E402

QT_TYPES = ("exercise", "question_topic")
TIERS = ("example", "exercise", "prompt")
MOVABLE = ("worked_example", "exercise", "exercise_question")
TOKEN = re.compile(r"\bM\d+\.S\d+\.T\d+(?:\.C\d+(?:\.[A-Za-z0-9]+)?)?")
BUCKET = "https://media.singularity-learn.com/learning_plan_assets/"


# ---------------------------------------------------------------------------------------------------- helpers
def load_json(path):
    with io.open(path, encoding="utf-8") as f:
        return json.load(f)


def write_json(path, obj):
    with io.open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)


def topics_of(plan):
    return [t for m in plan["modules"] for s in m["segments"] for t in s["topics"]]


def is_qt(t):
    """A Questions topic: typed so (exercise / question_topic) or, in the chapters typed otherwise, named so."""
    return t.get("source_type") in QT_TYPES or (t.get("topic_name") or "").startswith("Questions:")


def qt_topic_name(t, base_name):
    """"Questions: <base>" (every chapter's shape until now), or, when every question block inside
    carries a book label and they all agree on one category, the category-based name
    (core/question_naming.py) a topic_prefix="Questions" build now produces, e.g. "Questions:
    Exercise Set 5.1". This engine does not split a Questions topic by category (core/qt.py does, for
    a fresh build): a topic whose questions span more than one category keeps the plain "Questions:
    <base>" name, since there is nothing single to name it by."""
    labels = []
    for c in t.get("concepts") or []:
        block = next((b for b in c.get("content") or [] if b.get("block_kind") in MOVABLE), None)
        if block is None:
            continue
        cov = block.get("coverage_id") or next(iter(block.get("ncert_refs") or []), None)
        labels.append(QN.classify(block.get("book_number") or "", cov))
    if labels and len({(cat, suf) for cat, suf, _ in labels}) == 1:
        return QN.topic_title(labels[0][1])
    return "Questions: " + base_name


def video_of(c):
    vids = c.get("video_media_ids") or [i for i in c.get("media_ids", []) if ".VID" in i]
    return vids[0] if vids else None


def canon_list(lst, canon):
    out = []
    for r in lst or []:
        r = canon.get(r, r)
        if r not in out:
            out.append(r)
    return out


def canonize(plan, canon):
    """Fold sub-ids into one ref id per book question (the skeleton gate wants one item per question concept)."""
    if not canon:
        return
    for t in topics_of(plan):
        for c in t["concepts"]:
            c["ncert_refs"] = canon_list(c.get("ncert_refs"), canon)
            for b in c.get("content", []):
                if b.get("ncert_refs") is not None:
                    b["ncert_refs"] = canon_list(b["ncert_refs"], canon)
                for f in ("exercise_id", "coverage_id"):
                    if b.get(f) in canon:
                        b[f] = canon[b[f]]
        for x in t.get("media", []):
            if x.get("serves_items"):
                x["serves_items"] = canon_list(x["serves_items"], canon)
    for e in plan.get("video_coverage", []):
        e["item_id"] = canon.get(e["item_id"], e["item_id"])
    cov = {}
    for k, v in (plan.get("source_metadata", {}).get("ncert_coverage") or {}).items():
        lst = cov.setdefault(canon.get(k, k), [])
        lst.extend(x for x in v if x not in lst)
    if cov:
        plan["source_metadata"]["ncert_coverage"] = cov


def merge_q_topics(plan):
    """One Questions topic per concept topic: a second (third ...) Questions topic straight after the first is merged
    into it (its concepts and media appended, its segment dropped, references to it pointed at the first). Returns
    [(kept topic id, merged topic id)]."""
    merged, ren = [], {}
    for m in plan["modules"]:
        keep_segs = []
        prev_q = None
        for s in m["segments"]:
            t = s["topics"][0]
            if is_qt(t):
                if prev_q is not None:
                    prev_q["concepts"] = prev_q["concepts"] + t["concepts"]
                    prev_q["media"] = list(prev_q.get("media", [])) + list(t.get("media", []))
                    ren[t["topic_id"]] = prev_q["topic_id"]
                    merged.append((prev_q["topic_id"], t["topic_id"]))
                    continue
                prev_q = t
            else:
                prev_q = None
            keep_segs.append(s)
        m["segments"] = keep_segs
    if ren:
        def fix(o):
            if isinstance(o, dict):
                return {k: fix(v) for k, v in o.items()}
            if isinstance(o, list):
                return [fix(v) for v in o]
            if isinstance(o, str) and not o.startswith("http"):
                return TOKEN.sub(lambda mo: ren.get(mo.group(0), mo.group(0)), o)
            return o
        for k in list(plan.keys()):
            if k != "modules":
                plan[k] = fix(plan[k])
        for t in topics_of(plan):
            t["depends_on"] = list(dict.fromkeys(fix(t.get("depends_on") or [])))
        # ids of concepts under the merged topic keep their old topic prefix until the renumbering below
    return merged


class Index:
    def __init__(self, plan):
        self.order, self.topics, self.mod_of, self.cons, self.con_topic, self.media_home = [], {}, {}, {}, {}, {}
        self.seg_of = {}
        for m in plan["modules"]:
            for s in m["segments"]:
                for t in s["topics"]:
                    tid = t["topic_id"]
                    self.order.append(tid)
                    self.topics[tid] = t
                    self.mod_of[tid] = m["module_id"]
                    self.seg_of[tid] = s
                    for c in t["concepts"]:
                        self.cons[c["concept_id"]] = c
                        self.con_topic[c["concept_id"]] = tid
                    for x in t.get("media", []):
                        self.media_home[x["id"]] = tid
        # Questions topic <-> the concept topic it follows
        self.parent_of, self.qt_of = {}, {}
        prev = None
        for tid in self.order:
            t = self.topics[tid]
            if is_qt(t):
                if prev is not None:
                    self.parent_of[tid] = prev
                    self.qt_of.setdefault(prev, tid)
            else:
                prev = tid

    def media_node(self, mid):
        return next(x for x in self.topics[self.media_home[mid]]["media"] if x["id"] == mid)


# ---------------------------------------------------------------------------------------------------- spec check
def validate(plan, spec):
    """Problems with the spec against this plan; empty means it can be applied."""
    plan = copy.deepcopy(plan)
    merge_q_topics(plan)
    ix = Index(plan)
    canon = spec.get("canon") or {}
    problems = []
    used_blocks, used_whole, used_names, used_refs, seen_topics = set(), set(), {}, {}, set()
    for tp in spec.get("topics") or []:
        tid = tp.get("teach_topic")
        t = ix.topics.get(tid)
        if t is None:
            problems.append("teach_topic %r is not a topic of the live plan" % tid)
            continue
        if is_qt(t) or t.get("topic_type") in ("framing", "summary"):
            problems.append("%s: not a concept topic (%s)" % (tid, t.get("source_type")))
            continue
        if tid in seen_topics:
            problems.append("%s: listed twice" % tid)
        seen_topics.add(tid)
        qold = ix.qt_of.get(tid)
        qold_concepts = {c["concept_id"] for c in ix.topics[qold]["concepts"]} if qold else set()
        for i, q in enumerate(tp.get("questions") or []):
            where = "%s question %d" % (tid, i + 1)
            if "split" in q:
                c = ix.cons.get(q["split"])
                if c is None or q["split"] not in qold_concepts:
                    problems.append("%s: split %r is not a question concept of the Questions topic after %s"
                                    % (where, q["split"], tid))
                    continue
                if q["split"] in used_whole:
                    problems.append("%s: %s used twice" % (where, q["split"]))
                used_whole.add(q["split"])
                parts = q.get("into") or []
                if len(parts) < 2:
                    problems.append("%s: split %s needs at least two parts" % (where, q["split"]))
                seen_idx = []
                for j, pt in enumerate(parts):
                    pname = (pt.get("name") or "").strip()
                    if not pname:
                        problems.append("%s part %d: no name" % (where, j + 1))
                    if pname in used_names.setdefault(tid, set()):
                        problems.append("%s part %d: name %r used twice in this topic" % (where, j + 1, pname))
                    used_names[tid].add(pname)
                    if pt.get("tier") not in TIERS:
                        problems.append("%s part %d (%s): tier must be one of %s" % (where, j + 1, pname, TIERS))
                    if len(pt.get("refs") or []) != 1:
                        problems.append("%s part %d (%s): refs must hold exactly one coverage id" % (where, j + 1, pname))
                    for r in pt.get("refs") or []:
                        r = canon.get(r, r)
                        if r in used_refs:
                            problems.append("%s part %d (%s): ref %r already belongs to %s"
                                            % (where, j + 1, pname, r, used_refs[r]))
                        used_refs[r] = pname
                    if not pt.get("blocks"):
                        problems.append("%s part %d (%s): blocks is empty" % (where, j + 1, pname))
                    seen_idx += list(pt.get("blocks") or [])
                if sorted(seen_idx) != list(range(len(c.get("content") or []))):
                    problems.append("%s: the parts must use every block of %s exactly once (it has %d; parts use %s)"
                                    % (where, q["split"], len(c.get("content") or []), sorted(seen_idx)))
                if not (isinstance(q.get("keep_video_part", 0), int) and 0 <= q.get("keep_video_part", 0) < len(parts)):
                    problems.append("%s: keep_video_part is not a part index" % where)
                continue
            if "keep" in q:
                if q["keep"] not in qold_concepts:
                    problems.append("%s: keep %r is not a question concept of the Questions topic after %s"
                                    % (where, q["keep"], tid))
                if q["keep"] in used_whole:
                    problems.append("%s: %s used twice" % (where, q["keep"]))
                used_whole.add(q["keep"])
                continue
            name = (q.get("name") or "").strip()
            if not name:
                problems.append("%s: no name" % where)
            if name in used_names.setdefault(tid, set()):
                problems.append("%s: name %r used twice in this topic" % (where, name))
            used_names[tid].add(name)
            if q.get("tier") not in TIERS:
                problems.append("%s (%s): tier must be one of %s" % (where, name, TIERS))
            refs = q.get("refs") or []
            if len(refs) != 1:
                problems.append("%s (%s): refs must hold exactly one coverage id (fold sub-ids with canon)" % (where, name))
            for r in refs:
                r = canon.get(r, r)
                if r in used_refs:
                    problems.append("%s (%s): ref %r already belongs to %s" % (where, name, r, used_refs[r]))
                used_refs[r] = name
            frm = q.get("from") or []
            if not frm:
                problems.append("%s (%s): from is empty" % (where, name))
            wholes = []
            for ent in frm:
                c = ix.cons.get(ent.get("concept"))
                if c is None:
                    problems.append("%s (%s): concept %r not in the plan" % (where, name, ent.get("concept")))
                    continue
                if ix.con_topic[c["concept_id"]] in ix.parent_of and ix.con_topic[c["concept_id"]] != qold:
                    problems.append("%s (%s): %s is in a Questions topic of another concept topic"
                                    % (where, name, c["concept_id"]))
                if ent.get("whole"):
                    wholes.append(c["concept_id"])
                    blocks = c.get("content") or []
                    if len(blocks) != 1 or blocks[0].get("block_kind") not in MOVABLE:
                        problems.append("%s (%s): %s cannot move whole: it must hold exactly one worked-example or "
                                        "exercise block (cut that block out with \"block\" instead)"
                                        % (where, name, c["concept_id"]))
                    extra = [m for m in c.get("media_ids", []) if ".VID" not in m]
                    if extra:
                        problems.append("%s (%s): %s has media other than a video (%s); cut its block out instead"
                                        % (where, name, c["concept_id"], extra[:2]))
                    if c.get("objective_id"):
                        problems.append("%s (%s): %s carries objective %s; cut its block out instead"
                                        % (where, name, c["concept_id"], c["objective_id"]))
                    if c["concept_id"] in used_whole:
                        problems.append("%s (%s): %s used twice" % (where, name, c["concept_id"]))
                    used_whole.add(c["concept_id"])
                else:
                    idx = ent.get("block")
                    blocks = c.get("content") or []
                    if not isinstance(idx, int) or not (0 <= idx < len(blocks)):
                        problems.append("%s (%s): %s has no block %r" % (where, name, c["concept_id"], idx))
                        continue
                    if blocks[idx].get("block_kind") not in MOVABLE:
                        problems.append("%s (%s): %s block %d is %r, not a worked example or exercise"
                                        % (where, name, c["concept_id"], idx, blocks[idx].get("block_kind")))
                    if (c["concept_id"], idx) in used_blocks:
                        problems.append("%s (%s): %s block %d used twice" % (where, name, c["concept_id"], idx))
                    used_blocks.add((c["concept_id"], idx))
            kv = q.get("keep_video_of")
            if kv and (kv not in wholes or video_of(ix.cons[kv]) is None):
                problems.append("%s (%s): keep_video_of %r must be a whole-moved concept of this question with a video"
                                % (where, name, kv))
    for cid, idx in used_blocks:
        if cid in used_whole:
            problems.append("%s: cut a block out of it and also moved it whole" % cid)
    for cid in (spec.get("rename_teach") or {}):
        if cid not in ix.cons:
            problems.append("rename_teach: %r is not a concept of the plan" % cid)
    return problems


# ---------------------------------------------------------------------------------------------------- the rewrite
def new_concept(name):
    """A question concept the way core/qt.py writes one for the enrichment shape (no objective, no tool)."""
    return {"concept_id": "NEW", "concept_name": name, "content": [], "key_terms": [], "objective_id": None,
            "objective_ids": [], "source_segment_role": "practice", "source_media": None, "media_ids": [],
            "ncert_refs": [], "authored_key": None, "misconceptions": [], "estimated_minutes": 4, "media_key": None,
            "enrichment_type": "enrichment", "is_enrichment": True, "mixed_objective_ids": [],
            "recap_objective_ids": [], "_is_thin_extra": False, "image_decision": {}}


def new_q_topic(template, parent, ix):
    """A Questions topic: this chapter's own first one as the template (same field set and vocabulary), else the
    enrichment shape of core/qt.py."""
    if template is not None:
        qt = copy.deepcopy(template)
    else:
        qt = {"topic_type": "instructional", "source_type": "exercise", "topic_category": "enrichment",
              "is_enrichment": True, "key_terms": [], "difficulty": "", "important_points": [], "recall_questions": [],
              "primary_content_type": "video", "secondary_content_type": None, "tertiary_content_type": None,
              "available_content_types": ["paragraph", "video"], "estimated_exchanges": 0, "ncert_sections": [],
              "source_content_flow": "Practice problems with video solutions."}
    qt["concepts"], qt["media"] = [], []
    qt["topic_objective"], qt["objective_ids"], qt["learning_objectives"] = None, [], []
    qt["depends_on"] = []
    qt["ncert_sections"] = list(parent.get("ncert_sections") or [])
    qt["topic_id"] = "NEW:" + parent["topic_id"]
    qt["_new"] = True
    return qt


def estimate_asset_base(plan, chapter_no):
    for t in topics_of(plan):
        for x in t.get("media", []):
            for f in ("planned_url", "image_url", "video_url", "2d_tool_url"):
                m = re.match(r"^(%s.*?/class_\d+/mathematics/ch_\d+)/" % re.escape(BUCKET), x.get(f) or "")
                if m:
                    return m.group(1)
    return "%sV2/cbse/cbse/english/class_%s/mathematics/ch_%s" % (BUCKET, plan.get("grade"), chapter_no)


def apply(live, spec, *, add_placeholders=True):
    """(plan, report). `live` is not modified."""
    plan = copy.deepcopy(live)
    problems = validate(live, spec)
    if problems:
        raise ValueError("the spec does not fit the plan:\n  " + "\n  ".join(problems))
    merged_q = merge_q_topics(plan)
    canon = spec.get("canon") or {}
    canonize(plan, canon)
    ix = Index(plan)
    report = {"chapter_id": plan.get("chapter_id"), "source_version": plan.get("version"), "questions": [],
              "merged_questions_topics": merged_q, "splits": [],
              "videos_folded": [], "needs_new_video": [], "teach_concepts_edited": [], "renamed_teach": [],
              "removed_from_teach_topics": [], "appended_existing": []}
    live_minutes = {c["concept_id"]: c.get("estimated_minutes", 0) for c in ix.cons.values()}
    q_template = next((t for t in (ix.topics[i] for i in ix.order) if is_qt(t)), None)
    q_template = copy.deepcopy(q_template) if q_template else None

    spec_by_topic = {tp["teach_topic"]: tp for tp in spec.get("topics") or []}
    # every concept topic that has an existing Questions topic but no spec entry keeps everything
    for tid, qid in ix.qt_of.items():
        spec_by_topic.setdefault(tid, {"teach_topic": tid, "questions": []})

    q_nodes, q_topics = {}, {}
    kept_video, merged_into, whole_moved, cut_blocks = {}, {}, set(), {}
    moved_refs = set()

    for tid, tp in spec_by_topic.items():
        qold = ix.qt_of.get(tid)
        if qold:
            qt = ix.topics[qold]
            old_media = {x["id"]: x for x in qt.get("media", [])}
        else:
            if not tp.get("questions"):
                continue
            qt = new_q_topic(q_template, ix.topics[tid], ix)
            old_media = {}
        nodes, media, listed = [], [], set()
        for q in tp.get("questions") or []:
            if "split" in q:
                c0 = ix.cons[q["split"]]
                listed.add(q["split"])
                vp = q.get("keep_video_part", 0)
                report["splits"].append({"concept": q["split"], "name": c0["concept_name"], "into": len(q["into"])})
                for j, pt in enumerate(q["into"]):
                    name, tier = pt["name"].strip(), pt["tier"]
                    refs = [canon.get(r, r) for r in pt["refs"]]
                    node = copy.deepcopy(c0) if j == vp else new_concept(name)
                    node["content"] = [copy.deepcopy(c0["content"][i]) for i in pt["blocks"]]
                    node["concept_name"] = name
                    node["ncert_refs"] = list(refs)
                    node["source_segment_role"] = "practice"
                    node["estimated_minutes"] = max(4 * len(node["content"]), 4)
                    for k, b in enumerate(node["content"]):
                        b["example_id"] = "E%d" % k
                        b["ncert_refs"] = list(refs)
                        b.setdefault("item_kind", tier)
                        b["book_kind"] = tier
                        b.setdefault("coverage_id", refs[0])
                        b.setdefault("exercise_id", refs[0])
                        b.setdefault("book_number", name)
                    if pt.get("q_figure"):
                        node["content"][0]["q_figure"] = pt["q_figure"]
                    if pt.get("s_figure"):
                        node["content"][0]["s_figure"] = pt["s_figure"]
                    if j == vp:                      # this part keeps the concept's video, images, tool and objective
                        media += [old_media[i] for i in c0.get("media_ids", []) if i in old_media]
                        v = video_of(c0)
                        for b in node["content"]:
                            if v:
                                b["video_media_id"] = v
                    else:
                        node["media_ids"], node["video_media_ids"] = [], []
                        node.pop("walkthrough_video_id", None)
                        node["source_media"] = None
                        for b in node["content"]:
                            b.pop("video_media_id", None)
                        report["needs_new_video"].append(name)
                    nodes.append(node)
                    report["questions"].append({
                        "teach_topic": tid, "question": name, "tier": tier, "refs": refs,
                        "from": ["split %s[%s]" % (q["split"], ",".join(str(i) for i in pt["blocks"]))],
                        "video": video_of(c0) if j == vp else None,
                        "video_status": ("kept, covers only part: refresh" if j == vp and len(q["into"]) > 1
                                         else "kept" if j == vp else "new video needed")})
                continue
            if "keep" in q:
                c = ix.cons[q["keep"]]
                for b in c.get("content", []):             # a question block the images pass must recognise
                    if b.get("block_kind") in MOVABLE and not b.get("item_kind"):
                        b["item_kind"] = "exercise"
                for f in ("q_figure", "s_figure"):
                    if q.get(f) and c.get("content"):
                        c["content"][0][f] = q[f]
                nodes.append(c)
                listed.add(q["keep"])
                media += [old_media[i] for i in c.get("media_ids", []) if i in old_media]
                report["questions"].append({"teach_topic": tid, "question": c["concept_name"], "tier": "existing",
                                            "refs": c.get("ncert_refs") or [], "kept_as_is": True,
                                            "video": video_of(c)})
                continue
            tier, name = q["tier"], q["name"].strip()
            refs = [canon.get(r, r) for r in q["refs"]]
            moved_refs.update(refs)
            srcs, base = [], None
            for ent in q["from"]:
                c = ix.cons[ent["concept"]]
                if ent.get("whole"):
                    srcs.append(c["content"][0])
                    whole_moved.add(c["concept_id"])
                    if base is None:
                        base = c
                else:
                    srcs.append(c["content"][ent["block"]])
                    cut_blocks.setdefault(c["concept_id"], set()).add(ent["block"])
            node = copy.deepcopy(base) if base is not None else new_concept(name)
            node["content"] = [copy.deepcopy(b) for b in srcs]
            node["concept_name"] = name
            node["ncert_refs"] = list(refs)
            node["source_segment_role"] = "practice"
            node["_is_thin_extra"] = False
            node["is_enrichment"], node["enrichment_type"] = True, "enrichment"
            node["objective_id"], node["objective_ids"] = None, []
            node["mixed_objective_ids"], node["recap_objective_ids"] = [], []
            node["estimated_minutes"] = 4 * len(node["content"])
            for k, b in enumerate(node["content"]):
                b["example_id"] = "E%d" % k
                keep = [r for r in canon_list(b.get("ncert_refs"), canon) if r in refs]
                b["ncert_refs"] = keep or list(refs[:1])
                if not b.get("item_kind"):
                    b["item_kind"] = tier
                b["book_kind"] = tier
                b.setdefault("coverage_id", refs[0])
                b.setdefault("exercise_id", refs[0])
                b.setdefault("book_number", name)
            if q.get("q_figure"):
                node["content"][0]["q_figure"] = q["q_figure"]
            if q.get("s_figure"):
                node["content"][0]["s_figure"] = q["s_figure"]
            listed.update(e["concept"] for e in q["from"] if ix.con_topic[e["concept"]] == qold)
            kv = video_of(ix.cons[q["keep_video_of"]]) if q.get("keep_video_of") else None
            if kv:
                media.append(copy.deepcopy(ix.media_node(kv)))
                node["media_ids"], node["video_media_ids"], node["walkthrough_video_id"] = [kv], [kv], kv
                node["source_media"] = "video"
                for b in node["content"]:
                    b["video_media_id"] = kv
            else:
                node["media_ids"], node["video_media_ids"] = [], []
                node.pop("walkthrough_video_id", None)
                node["source_media"] = None
                for b in node["content"]:
                    b.pop("video_media_id", None)
                report["needs_new_video"].append(name)
            for ent in q["from"]:
                if ent.get("whole") and base is not None and ent["concept"] != base["concept_id"]:
                    merged_into[ent["concept"]] = node
                    v = video_of(ix.cons[ent["concept"]])
                    if v:
                        report["videos_folded"].append({"live_video": v, "folded_into": name, "kept": kv})
            kept_video[id(node)] = kv
            nodes.append(node)
            full = len(q["from"]) == 1
            report["questions"].append({
                "teach_topic": tid, "question": name, "tier": tier, "refs": refs,
                "from": ["%s%s" % (e["concept"], "" if e.get("whole") else "[%d]" % e["block"]) for e in q["from"]],
                "video": kv, "video_status": ("kept" if kv and full else "kept, covers only part: refresh" if kv
                                              else "new video needed")})
        if qold:                                   # existing question concepts the spec did not list stay, in order
            for c in qt["concepts"]:
                for b in c.get("content", []):
                    if b.get("block_kind") in MOVABLE and not b.get("item_kind"):
                        b["item_kind"] = "exercise"
                if c["concept_id"] not in listed:
                    nodes.append(c)
                    media += [old_media[i] for i in c.get("media_ids", []) if i in old_media]
                    report["appended_existing"].append(c["concept_id"])
        qt["concepts"], qt["media"] = nodes, media
        q_topics[tid] = qt

    # ---- the teaching side
    for cid, idxs in cut_blocks.items():
        c = ix.cons[cid]
        c["content"] = [b for i, b in enumerate(c["content"]) if i not in idxs]
    removed_minutes = {}
    for cid in whole_moved:
        tid = ix.con_topic[cid]
        if tid in ix.parent_of:
            continue                                  # already in the Questions topic that is being rebuilt
        removed_minutes[tid] = removed_minutes.get(tid, 0) + live_minutes.get(cid, 0)
        report["removed_from_teach_topics"].append({"concept": cid, "from_topic": tid})
        ix.topics[tid]["concepts"] = [c for c in ix.topics[tid]["concepts"] if c["concept_id"] != cid]
    moved_media = {video_of(ix.cons[c]) for c in whole_moved if video_of(ix.cons[c])}
    rebuilt_q = {ix.qt_of[t] for t in q_topics if t in ix.qt_of}
    for tid, t in ix.topics.items():
        if tid not in rebuilt_q:
            t["media"] = [x for x in t.get("media", []) if x["id"] not in moved_media]
    for cid, c in ix.cons.items():
        if cid in whole_moved or ix.con_topic[cid] in ix.parent_of:
            continue
        remain = {r for b in c.get("content", []) for r in (b.get("ncert_refs") or [])}
        new_refs = [r for r in c.get("ncert_refs", []) if r not in moved_refs or r in remain]
        if new_refs != c.get("ncert_refs", []) or cid in cut_blocks:
            report["teach_concepts_edited"].append({"concept": cid, "name": c["concept_name"],
                                                    "refs_moved_out": [r for r in c.get("ncert_refs", []) if r not in new_refs],
                                                    "blocks_cut": sorted(cut_blocks.get(cid, []))})
            c["ncert_refs"] = new_refs
    for cid, newname in (spec.get("rename_teach") or {}).items():
        report["renamed_teach"].append({"concept": cid, "from": ix.cons[cid]["concept_name"], "to": newname})
        ix.cons[cid]["concept_name"] = newname
    for tid, mins in removed_minutes.items():
        if "estimated_minutes" in ix.topics[tid]:
            ix.topics[tid]["estimated_minutes"] -= mins

    # ---- new order: every concept topic, then its Questions topic
    flat = []
    for tid in ix.order:
        t = ix.topics[tid]
        if tid in ix.parent_of:
            continue
        flat.append((ix.mod_of[tid], t))
        if tid in q_topics:
            flat.append((ix.mod_of[tid], q_topics[tid]))
        elif tid in ix.qt_of:
            flat.append((ix.mod_of[tid], ix.topics[ix.qt_of[tid]]))
    old_segment = {}
    for tid in ix.order:
        seg = {k: v for k, v in ix.seg_of[tid].items() if k != "topics"}
        old_segment[tid] = seg
    q_seg_template = next((old_segment[t] for t in ix.order if t in ix.parent_of), None)

    # ---- ids
    id_map, gt, gc = {}, 0, 0
    for mid, t in flat:
        gt += 1
        t["_new_tid"] = "%s.S%d.T%d" % (mid, gt, gt)
        if not t.get("_new"):
            id_map[t["topic_id"]] = t["_new_tid"]
        for c in t["concepts"]:
            gc += 1
            c["_new_cid"] = "%s.C%d" % (t["_new_tid"], gc)
            if c["concept_id"] != "NEW":
                id_map[c["concept_id"]] = c["_new_cid"]
    for cid, node in merged_into.items():
        id_map[cid] = node["_new_cid"]
    for mid, t in flat:
        for c in t["concepts"]:
            kv = kept_video.get(id(c))
            if kv:
                id_map[kv] = c["_new_cid"] + ".VID1"
    for cid, node in merged_into.items():
        v = video_of(ix.cons[cid])
        if v and kept_video.get(id(node)):
            id_map[v] = id_map[kept_video[id(node)]]
    for mid_ in ix.media_home:
        if mid_ in id_map:
            continue
        m = re.match(r"^(M\d+\.S\d+\.T\d+\.C\d+)(\..+)$", mid_)
        if m and m.group(1) in id_map:
            id_map[mid_] = id_map[m.group(1)] + m.group(2)

    def fix_str(s):
        return s if s.startswith("http") else TOKEN.sub(lambda m: id_map.get(m.group(0), m.group(0)), s)

    def walk(o):
        if isinstance(o, dict):
            return {k: walk(v) for k, v in o.items()}
        if isinstance(o, list):
            return [walk(v) for v in o]
        return fix_str(o) if isinstance(o, str) else o

    topic_nodes = []
    for mid, t in flat:
        t2 = walk({k: v for k, v in t.items() if k not in ("_new_tid", "_new")})
        t2["topic_id"] = t["_new_tid"]
        for c_old, c_new in zip(t["concepts"], t2["concepts"]):
            c_new["concept_id"] = c_old["_new_cid"]
            c_new.pop("_new_cid", None)
        for x in t2.get("media", []):
            if x["type"] == "video":
                owner = next((c for c in t2["concepts"] if x["id"] in (c.get("media_ids") or [])), None)
                if owner is not None:
                    x["concept_id"] = x["home_concept_id"] = owner["concept_id"]
        topic_nodes.append((mid, t2, t.get("_new", False), t))
    for key in ("objectives", "strand_to_objective_map", "source_metadata", "video_coverage"):
        if key in plan:
            plan[key] = walk(plan[key])
    seen, vc = set(), []
    for e in plan.get("video_coverage", []):
        k = (e["item_id"], e["video_id"])
        if k not in seen:
            seen.add(k)
            vc.append(e)
    if "video_coverage" in plan:
        plan["video_coverage"] = vc

    # ---- modules, segments, links, names
    linear = True
    prev_id = None
    for tid in ix.order:
        want = [prev_id] if prev_id else []
        if ix.topics[tid].get("depends_on") != want:
            linear = False
        prev_id = tid
    for m in plan["modules"]:
        m["segments"] = []
    modmap = {m["module_id"]: m for m in plan["modules"]}
    nodes_only = [t for _, t, _, _ in topic_nodes]
    prev = None
    for i, (mid, t, is_new, orig) in enumerate(topic_nodes):
        parent = nodes_only[i - 1] if is_qt(t) else None
        if is_qt(t):
            t["topic_name"] = qt_topic_name(t, parent["topic_name"])
            t["summary"] = t["brief_summary"] = t["detailed_summary"] = "Practise: " + parent["topic_name"] + "."
            t["original_chunk"] = t["publication_chunk"] = t["summary"]
            if is_new or True:
                t["ncert_sections"] = list(parent.get("ncert_sections") or t.get("ncert_sections") or [])
            t["estimated_minutes"] = sum(c.get("estimated_minutes", 0) for c in t["concepts"])
            if all(c.get("is_enrichment") for c in t["concepts"]):
                t["topic_objective"] = None
        if linear or is_new:
            t["depends_on"] = [prev] if prev else []
        t["concept_bullets"] = [c["concept_name"] for c in t["concepts"]]
        # objective lists follow the concepts that now sit in the topic
        oids = list(dict.fromkeys(c["objective_id"] for c in t["concepts"] if c.get("objective_id")))
        if oids != list(t.get("objective_ids") or []):
            t["objective_ids"] = oids
            by = {o["objective_id"]: o for o in plan.get("objectives", [])}
            t["learning_objectives"] = [by[o] for o in oids if o in by]
        sn = int(t["topic_id"].split(".S")[1].split(".T")[0])
        base_seg = old_segment.get(orig.get("topic_id")) if not is_new else None
        seg = copy.deepcopy(base_seg or q_seg_template or {"important_points": [], "recall_questions": []})
        seg.update({"segment_id": "%s.S%d" % (mid, sn), "segment_name": t["topic_name"], "summary": t["summary"],
                    "brief_summary": t["brief_summary"], "detailed_summary": t.get("detailed_summary", ""),
                    "segment_objective_ids": list(t.get("objective_ids", [])), "topics": [t]})
        modmap[mid]["segments"].append(seg)
        prev = t["topic_id"]

    # ---- coverage, stats, notes
    cov_old = (plan.get("source_metadata") or {}).get("ncert_coverage")
    if cov_old is not None:
        cov = {k: [] for k in cov_old}
        for t in nodes_only:
            for c in t["concepts"]:
                for r in c.get("ncert_refs") or []:
                    cov.setdefault(r, [])
                    if c["concept_id"] not in cov[r]:
                        cov[r].append(c["concept_id"])
        plan["source_metadata"]["ncert_coverage"] = cov
    media_all = [x for t in nodes_only for x in t.get("media", [])]
    if add_placeholders:
        cfg = {"grade": plan.get("grade"), "chapter_no": int(re.search(r"_ch(\d+)", plan["chapter_id"]).group(1)),
               "solution_continuation": True, "question_image_max_lines": layout.MAX_LINES, "image_engine": "manim"}
        cfg["asset_base_template"] = estimate_asset_base(plan, cfg["chapter_no"])
        report["images"] = placeholders.add(plan, cfg)
        media_all = [x for t in topics_of(plan) for x in t.get("media", [])]
    sm = plan.setdefault("source_metadata", {})
    ss = sm.setdefault("summary_stats", {})
    all_topics = topics_of(plan)
    qts = [t for t in all_topics if is_qt(t)]
    for k, v in (("topics", len(all_topics)), ("concepts", sum(len(t["concepts"]) for t in all_topics)),
                 ("question_topics", len(qts)), ("question_concepts", sum(len(t["concepts"]) for t in qts)),
                 ("videos", sum(1 for x in media_all if x["type"] == "video")),
                 ("images", sum(1 for x in media_all if x["type"] == "image"))):
        ss[k] = v
    if "estimated_time" in live:
        old_minutes = sum(t.get("estimated_minutes", 0) for t in topics_of(live))
        if abs(round(old_minutes / 60, 2) - live["estimated_time"]) < 0.011:
            plan["estimated_time"] = round(sum(t.get("estimated_minutes", 0) for t in all_topics) / 60, 2)
    sm["restructure"] = {
        "from": live.get("plan_id"),
        "layout": "concept topic, then its Questions topic (one concept per book question: solved example, exercise, "
                  "answerable prompt), then the next concept topic",
        "question_concepts": ss["question_concepts"],
        "note": "Order and home of questions only. Teaching text, objectives, tools and rendered videos are carried "
                "over; question and solution images are placeholders until the solutions are authored."}
    report["id_map_concepts"] = {k: v for k, v in id_map.items() if re.match(r"^M\d+\.S\d+\.T\d+\.C\d+$", k) and k != v}
    report["counts"] = {"topics": ss["topics"], "concepts": ss["concepts"], "question_topics": ss["question_topics"],
                        "question_concepts": ss["question_concepts"], "videos": ss["videos"], "images": ss["images"]}
    return plan, report


# ---------------------------------------------------------------------------------------------------- integrity
def integrity(live, plan, report):
    """Everything that must still be true of the result; returns a list of problems."""
    errs = []
    T = topics_of(plan)
    ids = [x["id"] for t in T for x in t.get("media", [])]
    if len(ids) != len(set(ids)):
        errs.append("duplicate media ids")
    cids = [c["concept_id"] for t in T for c in t["concepts"]]
    if len(cids) != len(set(cids)):
        errs.append("duplicate concept ids")
    tids = [t["topic_id"] for t in T]
    if len(tids) != len(set(tids)):
        errs.append("duplicate topic ids")
    have, cset = set(ids), set(cids)
    for t in T:
        for c in t["concepts"]:
            if not c["concept_id"].startswith(t["topic_id"] + ".C"):
                errs.append("concept %s not under topic %s" % (c["concept_id"], t["topic_id"]))
            for i in c.get("media_ids", []):
                if i not in have:
                    errs.append("concept %s lists missing media %s" % (c["concept_id"], i))
                elif not (i.startswith(c["concept_id"] + ".") or "." not in i):
                    errs.append("media %s is not named after %s" % (i, c["concept_id"]))
            for b in c.get("content", []):
                for f in ("video_media_id", "image_media_id", "solution_image_media_id"):
                    if b.get(f) and b[f] not in have:
                        errs.append("block of %s points at missing %s %s" % (c["concept_id"], f, b[f]))
        for x in t.get("media", []):
            if x.get("concept_id") and x["concept_id"] not in cset:
                errs.append("media %s names unknown concept %s" % (x["id"], x["concept_id"]))
    for e in plan.get("video_coverage", []):
        if e["video_id"] not in have:
            errs.append("video_coverage -> missing %s" % e["video_id"])
    for o in plan.get("objectives", []):
        for a in o.get("anchor", []):
            if a not in cset:
                errs.append("objective %s anchor %s missing" % (o["objective_id"], a))
        if o.get("home_topic_id") not in set(tids):
            errs.append("objective %s home topic missing" % o["objective_id"])
    lo = [(o["objective_id"], o["objective_text"]) for o in live.get("objectives", [])]
    no = [(o["objective_id"], o["objective_text"]) for o in plan.get("objectives", [])]
    if lo != no:
        errs.append("objectives changed")
    cov = (plan.get("source_metadata") or {}).get("ncert_coverage") or {}
    for k, v in cov.items():
        if not v:
            errs.append("book item %s maps to no concept" % k)
        for c in v:
            if c not in cset:
                errs.append("coverage %s -> unknown concept %s" % (k, c))
    # every live book item is still covered (ids may have been folded by canon)
    live_cov = (live.get("source_metadata") or {}).get("ncert_coverage") or {}
    folded = set(report.get("folded_ids", []))          # ids the spec folded into another id (canon)
    lost = [k for k in live_cov if live_cov[k] and k not in folded and not (cov.get(k) or [])]
    if lost:
        errs.append("book items no longer covered: %s" % lost[:6])
    # rendered video urls: live minus the folded ones
    lv = {x["id"]: x for t in topics_of(live) for x in t.get("media", []) if x["type"] == "video"}
    nv = [x for t in T for x in t.get("media", []) if x["type"] == "video"]
    folded_ids = {f["live_video"] for f in report.get("videos_folded", [])}
    exp = sorted(x.get("video_url") or "" for k, x in lv.items() if k not in folded_ids)
    got = sorted(x.get("video_url") or "" for x in nv)
    if exp != got:
        errs.append("rendered video urls changed (%d expected, %d found)" % (len(exp), len(got)))
    # Questions topics sit directly after a concept topic and are named after it
    for i, t in enumerate(T):
        if is_qt(t):
            prev = T[i - 1] if i else None
            if prev is None or is_qt(prev) or t["topic_name"] != qt_topic_name(t, prev["topic_name"]):
                errs.append("%s: not directly after its concept topic or misnamed" % t["topic_id"])
    # every question concept: question image first, solution image last
    media = {x["id"]: x for t in T for x in t.get("media", [])}
    for t in T:
        if is_qt(t):
            for c in t["concepts"]:
                ids_ = c.get("media_ids", [])
                if ids_ and (media.get(ids_[0], {}).get("image_role") != "question"
                             or media.get(ids_[-1], {}).get("image_role") != "solution"):
                    errs.append("%s: question image must be first and a solution image last" % c["concept_id"])
    return errs


def _category(msg):
    return re.sub(r"M\d+\.S\d+\.T\d+(\.C\d+(\.\w+)?)?|\bO\d+\b|\d+", "#", msg)


def new_integrity_problems(live, plan, report):
    """integrity() minus what the live plan already had: the same check run on the live plan gives a baseline of
    problems per kind (a chapter can carry old oddities, e.g. a concept listing a media id named after another
    concept); only problems beyond that baseline are the rewrite's."""
    import collections
    base = collections.Counter(_category(m) for m in integrity(live, live, {}))
    now = integrity(live, plan, report)
    seen, out = collections.Counter(), []
    for m in now:
        c = _category(m)
        seen[c] += 1
        if seen[c] > base.get(c, 0):
            out.append(m)
    return out


def gate_counts(plan):
    """Per-gate blocking counts under the standard config for a Class 6-8 chapter (for a before/after comparison)."""
    from gates import gate_runner
    cfg = {"eqcheck": "signed", "grade_band": "6_8", "theorem_chapter": False, "idea_topic_concept_range": [2, 4],
           "intro_requires_free_try_tool": False, "intro_requires_handover": False, "allow_words": [],
           "interactive_video_variant": False, "photo_rule_band": "none", "eqcheck_errata": []}
    errors, counts = gate_runner.run(plan, cfg)
    counts.pop("warnings", None)
    return {k: v for k, v in counts.items() if k.endswith("_problems")}, errors


# ---------------------------------------------------------------------------------------------------- brief
def brief(plan, book_path=None):
    ix = Index(plan)
    out = ["# %s  (%s, live v%s)" % (plan.get("chapter_name"), plan.get("chapter_id"), plan.get("version")), ""]
    if book_path:
        out += ["Book text: `%s`" % book_path, ""]
    out += ["Topics in order. `C` lines are concepts; `b<i>` lines are content blocks (kind, item_kind, refs, "
            "steps, question). A concept topic is followed by its existing Questions topic (if any).", ""]
    for tid in ix.order:
        t = ix.topics[tid]
        kind = "QUESTIONS TOPIC (follows %s)" % ix.parent_of[tid] if tid in ix.parent_of else \
            ("FRAMING" if t.get("topic_type") == "framing" else "SUMMARY" if t.get("topic_type") == "summary"
             else "CONCEPT TOPIC")
        out.append("## %s  %s  [%s]" % (tid, t["topic_name"], kind))
        for c in t["concepts"]:
            flags = []
            if c.get("is_enrichment"):
                flags.append("enrichment")
            if c.get("_is_thin_extra"):
                flags.append("thin-extra")
            if c.get("objective_id"):
                flags.append("obj " + c["objective_id"])
            media = [m.split(".")[-1] for m in c.get("media_ids", [])]
            out.append("C %s  '%s'  [%s]  media=%s  refs=%s" % (c["concept_id"], c["concept_name"], ", ".join(flags),
                                                              media, c.get("ncert_refs") or []))
            for i, b in enumerate(c.get("content", [])):
                q = re.sub(r"\s+", " ", b.get("question") or b.get("text") or "")[:170]
                out.append("   b%d %s/%s refs=%s steps=%d video=%s  %s" % (
                    i, b.get("block_kind"), b.get("item_kind"), b.get("ncert_refs") or [], len(b.get("steps") or []),
                    (b.get("video_media_id") or "-").split(".")[-1], ("Q: " + q) if q else ""))
        out.append("")
    cov = (plan.get("source_metadata") or {}).get("ncert_coverage") or {}
    out += ["## Book items the plan covers (coverage id -> concept)", ""]
    out += ["- %s -> %s" % (k, ", ".join(v)) for k, v in cov.items()]
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------------------------------- CLI
def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.split("THE SPEC")[0], formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("cmd", choices=("brief", "check", "apply"))
    ap.add_argument("live")
    ap.add_argument("spec", nargs="?")
    ap.add_argument("-o", "--out")
    ap.add_argument("--report")
    ap.add_argument("--book")
    a = ap.parse_args(argv)
    live = load_json(a.live)
    if a.cmd == "brief":
        text = brief(live, a.book)
        if a.out:
            with io.open(a.out, "w", encoding="utf-8", newline="\n") as f:
                f.write(text)
        else:
            print(text)
        return 0
    if not a.spec:
        raise SystemExit("spec path needed")
    spec = load_json(a.spec)
    problems = validate(live, spec)
    if problems:
        print("SPEC PROBLEMS (%d):" % len(problems))
        for p in problems:
            print("  -", p)
        return 1
    plan, report = apply(live, spec)
    report["folded_ids"] = list((spec.get("canon") or {}).keys())
    errs = new_integrity_problems(live, plan, report)
    before, _ = gate_counts(live)
    after, after_errs = gate_counts(plan)
    report["gates_before"], report["gates_after"] = before, after
    report["integrity_problems"] = errs
    worse = {k: (before.get(k, 0), v) for k, v in after.items() if v > before.get(k, 0)}
    report["gates_worse"] = worse
    q = [r for r in report["questions"] if r.get("tier") != "existing"]
    print("%s v%s -> topics %d, concepts %d, question topics %d, question concepts %d (%d new from %d tiers: %s)" % (
        report["chapter_id"], report["source_version"], report["counts"]["topics"], report["counts"]["concepts"],
        report["counts"]["question_topics"], report["counts"]["question_concepts"], len(q),
        len({r["tier"] for r in q}), {t: sum(1 for r in q if r["tier"] == t) for t in TIERS}))
    print("needs a new video: %d | videos folded: %d | teaching concepts edited: %d | images: %d question + %d solution cards"
          % (len(report["needs_new_video"]), len(report["videos_folded"]), len(report["teach_concepts_edited"]),
             len(report.get("images", [])), sum(r["solution_images"] for r in report.get("images", []))))
    print("gates before %s" % before)
    print("gates after  %s" % after)
    print("INTEGRITY: %s" % ("clean" if not errs else "%d problem(s)" % len(errs)))
    for e in errs[:20]:
        print("  -", e)
    if worse:
        print("GATES WORSE THAN LIVE: %s" % worse)
    if a.cmd == "apply":
        if errs:
            print("not written: integrity problems")
            return 1
        write_json(a.out, plan)
        print("wrote", a.out)
    if a.report:
        write_json(a.report, report)
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
