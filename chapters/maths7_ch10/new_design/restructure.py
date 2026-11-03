# -*- coding: utf-8 -*-
"""Topic-wise restructure of Class 7 Ch 10 (Operations with Integers), Phase 2.

    python -I -X utf8 restructure.py            (run from anywhere; paths are relative to this file)

Input : ../live_v67/cbse_eng_maths7_ch10_v67.json   (the active live plan, fetched read-only)
Output: cbse_eng_maths7_ch10.json                   (restructured plan, same Phase 2 shape)
        restructure_report.json / restructure_report.md

The only thing this script changes is the ORDER and HOME of book questions:

    concept topic -> "Questions: <that topic>" (one concept per book question) -> next concept topic ...

* every solved example, every Figure it Out item and every answerable in-text prompt becomes its own
  question concept inside the Questions topic that follows its concept topic;
* a question that already was a whole concept (a "Figure it Out" concept or a thin "Ex" concept) moves
  with its node, its block and its rendered video;
* a question that sat as a worked-example block inside a teaching concept is cut out of that concept
  into a new question concept (the teaching concept keeps its text, plan, recap, tool and video);
* nothing is written or rewritten in the teaching content, no video is rendered, no image is made.

Ids are renumbered the way core/qt.py does (global S/T/C counters inside each module); every reference
(media, objectives, video_coverage, ncert_coverage, depends_on, segments) is rewritten by exact id match.
Media URLs are frozen, as qt.py freezes them.
"""
import copy
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LIVE = os.path.join(HERE, "..", "live_v67", "cbse_eng_maths7_ch10_v67.json")
OUT = os.path.join(HERE, "cbse_eng_maths7_ch10.json")

# --------------------------------------------------------------------------------------------------
# The layout.  teach topic (live id) -> (live id of its existing Questions topic or None, [question specs])
#   whole : live concept ids that move as concepts (first one is the base node of the question concept)
#   blocks: [(live concept id, block index)] worked-example blocks cut out of a teaching concept
#   video : live concept id whose rendered video the question concept keeps (None -> new video needed)
# Order of "sources" in the finished concept: blocks first when they come from a teaching concept.
# --------------------------------------------------------------------------------------------------
def Q(name, refs, whole=(), blocks=(), video=None, tier="core"):
    return dict(name=name, refs=list(refs), whole=list(whole), blocks=list(blocks), video=video, tier=tier)


LAYOUT = [
    ("M1.S2.T2", "M1.S3.T3", [
        Q("Rakesh's Puzzle", ["2.1.rakesh"], whole=["M1.S2.T2.C3"], blocks=[("M1.S2.T2.C2", 2)],
          video="M1.S2.T2.C3", tier="intext"),
        Q("Figure it Out (section 2.1)", ["2.1.FiO"], whole=["M1.S3.T3.C5"], video="M1.S3.T3.C5"),
    ]),
    ("M1.S4.T4", None, [
        Q("Carrom Coin Integers, Q1", ["2.1.carrom_Q1"], whole=["M1.S4.T4.C9"], video="M1.S4.T4.C9", tier="intext"),
        Q("Carrom Coin Integers, Q2", ["2.1.carrom_Q2"], whole=["M1.S4.T4.C10"], video="M1.S4.T4.C10", tier="intext"),
        Q("Carrom Coin Integers, Try This", ["2.1.TryThis"], blocks=[("M1.S4.T4.C12", 1)], tier="intext"),
    ]),
    ("M1.S5.T5", "M1.S6.T6", [
        Q("End of chapter Figure it Out, Q4", ["end.Q4"], whole=["M1.S6.T6.C18"], video="M1.S6.T6.C18"),
    ]),
    ("M2.S7.T7", "M2.S8.T8", [
        Q("Token Bag: 4 × (−6) and 9 × (−7)", ["2.2.similar"], whole=["M2.S7.T7.C21"], video="M2.S7.T7.C21", tier="intext"),
        Q("Figure it Out (multiplication), Q1", ["2.2.FiO_A.Q1"], whole=["M2.S8.T8.C28"], video="M2.S8.T8.C28"),
        Q("Figure it Out (multiplication), Q2", ["2.2.FiO_A.Q2"], whole=["M2.S8.T8.C29"], video="M2.S8.T8.C29"),
        Q("Figure it Out (multiplication), Q3", ["2.2.FiO_A.Q3"], whole=["M2.S8.T8.C30"], video="M2.S8.T8.C30"),
    ]),
    ("M2.S9.T9", "M2.S10.T10", [
        Q("Figure it Out (products)", ["2.2.FiO_B"], whole=["M2.S10.T10.C38"], video="M2.S10.T10.C38"),
        Q("End of chapter Figure it Out, Q3", ["end.Q3"], whole=["M2.S10.T10.C39"], video="M2.S10.T10.C39"),
        Q("End of chapter Figure it Out, Q12", ["end.Q12"], whole=["M2.S10.T10.C40"], video="M2.S10.T10.C40"),
    ]),
    ("M3.S11.T11", "M3.S12.T12", [
        Q("Example 1: Mala's exam marks", ["2.2.Ex1"], whole=["M3.S11.T11.C42"],
          blocks=[("M3.S11.T11.C41", 2)], video="M3.S11.T11.C42"),
        Q("Example 2: the mine elevator", ["2.2.Ex2"],
          whole=["M3.S11.T11.C44", "M3.S11.T11.C45", "M3.S11.T11.C46"], blocks=[("M3.S11.T11.C43", 2)],
          video="M3.S11.T11.C44"),
        Q("Figure it Out (division), Q2", ["2.2.FiO_C.Q2"], whole=["M3.S12.T12.C48"], video="M3.S12.T12.C48"),
        Q("Figure it Out (division), Q3", ["2.2.FiO_C.Q3"], whole=["M3.S12.T12.C49"], video="M3.S12.T12.C49"),
        Q("End of chapter Figure it Out, Q6", ["end.Q6"], whole=["M3.S12.T12.C50"], video="M3.S12.T12.C50"),
        Q("End of chapter Figure it Out, Q8", ["end.Q8"], whole=["M3.S12.T12.C51"], video="M3.S12.T12.C51"),
    ]),
    ("M3.S13.T13", None, [
        Q("A Magic Grid of Integers: try again", ["2.2.magic_grid_try_again"], whole=["M3.S13.T13.C53"],
          video="M3.S13.T13.C53", tier="intext"),
    ]),
    ("M4.S14.T14", "M4.S15.T15", [
        Q("Figure it Out (division), Q1", ["2.2.FiO_C.Q1"], whole=["M4.S15.T15.C61"], video="M4.S15.T15.C61"),
        Q("Figure it Out (division), Q4", ["2.2.FiO_C.Q4"], whole=["M4.S15.T15.C62"], video="M4.S15.T15.C62"),
        Q("End of chapter Figure it Out, Q2", ["end.Q2"], whole=["M4.S15.T15.C63"], video="M4.S15.T15.C63"),
        Q("End of chapter Figure it Out, Q11", ["end.Q11"], whole=["M4.S15.T15.C64"], video="M4.S15.T15.C64"),
    ]),
    ("M5.S16.T16", "M5.S17.T17", [
        Q("Many Factors: 25 × (−6) × 12 in every order", ["2.2.assoc_25m612"], whole=["M5.S16.T16.C67"],
          video="M5.S16.T16.C67", tier="intext"),
        Q("End of chapter Figure it Out, Q1 (b) and (c)", ["end.Q1bc"], whole=["M5.S17.T17.C71"], video="M5.S17.T17.C71"),
        Q("End of chapter Figure it Out, Q9", ["end.Q9"], whole=["M5.S17.T17.C72"], video="M5.S17.T17.C72"),
    ]),
    ("M5.S18.T18", "M5.S19.T19", [
        Q("Distributive Property: (−2) × (4 + (−3))", ["2.2.dist_m2"],
          whole=["M5.S18.T18.C74", "M5.S18.T18.C75"], video="M5.S18.T18.C74", tier="intext"),
        Q("Distributive Property, Try This: −4 × (2 + (−3))", ["2.2.TryThis.dist_m4"], whole=["M5.S18.T18.C77"],
          video="M5.S18.T18.C77", tier="intext"),
        Q("End of chapter Figure it Out, Q1 (a)", ["end.Q1a"], whole=["M5.S19.T19.C79"], video="M5.S19.T19.C79"),
        Q("End of chapter Figure it Out, Q13", ["end.Q13"], whole=["M5.S19.T19.C80"], video="M5.S19.T19.C80"),
        Q("End of chapter Figure it Out, Q14", ["end.Q14"], whole=["M5.S19.T19.C81"], video="M5.S19.T19.C81"),
    ]),
    ("M5.S20.T20", "M5.S21.T21", [
        Q("Pick the Pattern: Machine 1", ["2.2.machine1_last"], whole=["M5.S20.T20.C83"], video="M5.S20.T20.C83", tier="intext"),
        Q("Pick the Pattern: Machine 2", ["2.2.machine2"],
          whole=["M5.S20.T20.C85", "M5.S20.T20.C86"], video="M5.S20.T20.C85", tier="intext"),
        Q("End of chapter Figure it Out, Q7", ["end.Q7"], whole=["M5.S21.T21.C88"], video="M5.S21.T21.C88"),
        Q("End of chapter Figure it Out, Q5", ["end.Q5"], whole=["M5.S21.T21.C89"], video="M5.S21.T21.C89"),
        Q("End of chapter Figure it Out, Q15", ["end.Q15"], whole=["M5.S21.T21.C90"], video="M5.S21.T21.C90"),
        Q("End of chapter Figure it Out, Q16", ["end.Q16"], whole=["M5.S21.T21.C91"], video="M5.S21.T21.C91"),
    ]),
    ("M5.S22.T22", "M5.S23.T23", [
        Q("Pibs: paying +85 with +13 and −9 coins", ["end.Q10.85"], blocks=[("M5.S22.T22.C92", 2)], tier="intext"),
        Q("End of chapter Figure it Out, Q10", ["end.Q10"],
          whole=["M5.S23.T23.C95", "M5.S22.T22.C93"], video="M5.S23.T23.C95"),
    ]),
]

# teaching concepts that lose their worked example and were named after it
RENAME_TEACH = {
    "M3.S11.T11.C41": "Exam marks: positive and negative marks",
    "M3.S11.T11.C43": "The mine elevator: signed speed and position",
}

TOKEN = re.compile(r"\bM\d+\.S\d+\.T\d+(?:\.C\d+(?:\.[A-Za-z0-9]+)?)?")


# One book question = one coverage id.  The live plan split some questions into sub-ids (parts, methods, a hint);
# they are folded into the question's own id so the skeleton rule "a question concept maps to exactly one item" holds.
CANON = {
    "2.1.rakesh1": "2.1.rakesh", "2.1.rakesh2": "2.1.rakesh",
    "2.2.Ex1.max_min": "2.2.Ex1",
    "2.2.Ex2a": "2.2.Ex2", "2.2.Ex2b_method1": "2.2.Ex2", "2.2.Ex2b_method2": "2.2.Ex2",
    "2.2.dist_own": "2.2.dist_m2",
    "2.2.make_machine": "2.2.machine2",
    "end.Q10.hint": "end.Q10",
}


def canon_list(lst):
    out = []
    for r in lst or []:
        r = CANON.get(r, r)
        if r not in out:
            out.append(r)
    return out


def canonize(plan):
    for m in plan["modules"]:
        for s in m["segments"]:
            for t in s["topics"]:
                for c in t["concepts"]:
                    c["ncert_refs"] = canon_list(c.get("ncert_refs"))
                    for b in c["content"]:
                        if b.get("ncert_refs") is not None:
                            b["ncert_refs"] = canon_list(b["ncert_refs"])
                        if b.get("exercise_id") in CANON:
                            b["exercise_id"] = CANON[b["exercise_id"]]
                for x in t.get("media", []):
                    if x.get("serves_items"):
                        x["serves_items"] = canon_list(x["serves_items"])
    for e in plan["video_coverage"]:
        e["item_id"] = CANON.get(e["item_id"], e["item_id"])
    cov = {}
    for k, v in plan["source_metadata"]["ncert_coverage"].items():
        lst = cov.setdefault(CANON.get(k, k), [])
        lst.extend(x for x in v if x not in lst)
    plan["source_metadata"]["ncert_coverage"] = cov


def die(msg):
    raise SystemExit("RESTRUCTURE STOPPED: " + msg)


def main():
    live = json.load(io.open(LIVE, encoding="utf-8"))
    plan = copy.deepcopy(live)
    canonize(plan)
    report = {"source": live["plan_id"], "questions": [], "videos_folded": [], "needs_new_video": [],
              "teach_concepts_edited": [], "renamed_teach": [], "concepts_removed_from_teach_topics": []}

    # ---- index the live plan -------------------------------------------------------------------
    mod_of, topics, cons, con_topic, media_home = {}, {}, {}, {}, {}
    live_order = []
    for m in plan["modules"]:
        for s in m["segments"]:
            for t in s["topics"]:
                topics[t["topic_id"]] = t
                live_order.append(t["topic_id"])
                mod_of[t["topic_id"]] = m["module_id"]
                for c in t["concepts"]:
                    cons[c["concept_id"]] = c
                    con_topic[c["concept_id"]] = t["topic_id"]
                for x in t.get("media", []):
                    media_home[x["id"]] = t["topic_id"]
    live_minutes = {c["concept_id"]: c["estimated_minutes"] for c in cons.values()}
    template_topic = copy.deepcopy(topics["M3.S12.T12"])
    template_concept = copy.deepcopy(cons["M3.S12.T12.C49"])
    template_segment = next(copy.deepcopy(s) for m in plan["modules"] for s in m["segments"] if s["segment_id"] == "M3.S12")

    def video_of(cid):
        c = cons[cid]
        vids = c.get("video_media_ids") or [i for i in c.get("media_ids", []) if ".VID" in i]
        return vids[0] if vids else None

    def media_node(mid):
        return next(x for x in topics[media_home[mid]]["media"] if x["id"] == mid)

    # ---- sanity: the layout only names things that exist, and each live concept is used once ----------
    seen = {}
    for teach, qold, specs in LAYOUT:
        if teach not in topics or (qold and qold not in topics):
            die("unknown topic in layout: %s / %s" % (teach, qold))
        for sp in specs:
            for cid in sp["whole"]:
                if cid not in cons:
                    die("unknown concept in layout: %s" % cid)
                if cid in seen:
                    die("%s used twice" % cid)
                seen[cid] = sp["name"]
            for cid, idx in sp["blocks"]:
                if cid not in cons:
                    die("unknown concept in layout: %s" % cid)
            if sp["video"] and (sp["video"] not in sp["whole"] or video_of(sp["video"]) is None):
                die("%s: the kept video must come from one of its own whole concepts" % sp["name"])
    for teach, qold, specs in LAYOUT:
        if qold:
            for c in topics[qold]["concepts"]:
                if c["concept_id"] not in seen:
                    die("concept %s of %s is not placed by the layout" % (c["concept_id"], qold))

    # ---- build the question concepts ------------------------------------------------------------
    q_nodes = {}          # teach topic id -> [question concept nodes]
    q_topics = {}         # teach topic id -> Questions topic node
    kept_video = {}       # id(node) -> live video id kept by that question concept
    merged_into = {}      # live concept id (not the base) -> node it was folded into
    base_of = {}          # id(node) -> live base concept id
    for teach, qold, specs in LAYOUT:
        qt = topics[qold] if qold else copy.deepcopy(template_topic)
        if not qold:
            qt["topic_id"] = "NEW:" + teach
            qt["_new"] = True
        nodes, media = [], []
        for sp in specs:
            blocks = [cons[cid]["content"][idx] for cid, idx in sp["blocks"]]
            for cid, idx in sp["blocks"]:
                if cons[cid]["content"][idx].get("block_kind") != "worked_example":
                    die("%s block %d is not a worked example" % (cid, idx))
            base = None
            for cid in sp["whole"]:
                c = cons[cid]
                if len(c["content"]) != 1 or c["content"][0].get("block_kind") != "worked_example":
                    die("%s is not a single worked-example concept" % cid)
                blocks.append(c["content"][0])
                if base is None:
                    base = c
            node = copy.deepcopy(base) if base is not None else copy.deepcopy(template_concept)
            if base is None:
                node["concept_id"] = "NEW"
                node["media_key"] = None
            node["content"] = [copy.deepcopy(b) for b in blocks]
            node["concept_name"] = sp["name"]
            node["ncert_refs"] = list(sp["refs"])
            node["source_segment_role"] = "practice"
            node["_is_thin_extra"] = False
            node["is_enrichment"], node["enrichment_type"] = True, "enrichment"
            node["objective_id"], node["objective_ids"] = None, []
            node["estimated_minutes"] = 4 * len(node["content"])
            for i, b in enumerate(node["content"]):
                b["example_id"] = "E%d" % i
                keep = [r for r in (b.get("ncert_refs") or []) if r in sp["refs"]]
                b["ncert_refs"] = keep or list(sp["refs"][:1])
            kv = video_of(sp["video"]) if sp["video"] else None
            if kv:
                media.append(copy.deepcopy(media_node(kv)))
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
                report["needs_new_video"].append(sp["name"])
            for cid in sp["whole"]:
                if base is not None and cid != base["concept_id"]:
                    merged_into[cid] = node
                    v = video_of(cid)
                    if v:
                        report["videos_folded"].append({"live_video": v, "folded_into": sp["name"], "kept": kv})
            base_of[id(node)] = base["concept_id"] if base is not None else None
            kept_video[id(node)] = kv
            nodes.append(node)
            full = len(sp["whole"]) + len(sp["blocks"]) == 1
            report["questions"].append({
                "teach_topic": teach, "question": sp["name"], "tier": sp["tier"], "refs": sp["refs"],
                "from_whole_concepts": sp["whole"], "from_blocks": ["%s[%d]" % b for b in sp["blocks"]],
                "video": kv, "video_status": ("kept" if kv and full else "kept, covers only part: refresh" if kv
                                              else "new video needed")})
        qt["concepts"], qt["media"] = nodes, media
        q_topics[teach] = qt

    # ---- edit the teaching side ------------------------------------------------------------------
    moved_whole = set(seen)
    moved_refs = {r for _, _, specs in LAYOUT for sp in specs for r in sp["refs"]}
    cut = {}
    for _, _, specs in LAYOUT:
        for sp in specs:
            for cid, idx in sp["blocks"]:
                cut.setdefault(cid, set()).add(idx)
    for cid, idxs in cut.items():
        c = cons[cid]
        c["content"] = [b for i, b in enumerate(c["content"]) if i not in idxs]
    removed_minutes = {}
    for cid in moved_whole:
        tid = con_topic[cid]
        if tid not in {q for _, q, _ in LAYOUT if q}:
            removed_minutes[tid] = removed_minutes.get(tid, 0) + live_minutes[cid]
            report["concepts_removed_from_teach_topics"].append({"concept": cid, "from_topic": tid,
                                                                 "became": seen[cid]})
            topics[tid]["concepts"] = [c for c in topics[tid]["concepts"] if c["concept_id"] != cid]
    moved_media = {video_of(cid) for cid in moved_whole if video_of(cid)}
    rebuilt_q = {q for _, q, _ in LAYOUT if q}      # these already hold exactly the videos they keep
    for tid, t in topics.items():
        if tid not in rebuilt_q:
            t["media"] = [x for x in t.get("media", []) if x["id"] not in moved_media]
    for cid, c in cons.items():
        if cid in moved_whole:
            continue
        remain = {r for b in c["content"] for r in (b.get("ncert_refs") or [])}
        new_refs = [r for r in c.get("ncert_refs", []) if r not in moved_refs or r in remain]
        if new_refs != c.get("ncert_refs", []):
            report["teach_concepts_edited"].append({"concept": cid, "name": c["concept_name"],
                                                    "refs_moved_out": [r for r in c["ncert_refs"] if r not in new_refs],
                                                    "worked_example_blocks_cut": sorted(cut.get(cid, []))})
            c["ncert_refs"] = new_refs
    for cid, newname in RENAME_TEACH.items():
        report["renamed_teach"].append({"concept": cid, "from": cons[cid]["concept_name"], "to": newname})
        cons[cid]["concept_name"] = newname
    for tid, mins in removed_minutes.items():
        topics[tid]["estimated_minutes"] -= mins

    # ---- new order: each concept topic, then its Questions topic ------------------------------------
    qold_ids = {q for _, q, _ in LAYOUT if q}
    teach_to_q = {teach: q_topics[teach] for teach, _, _ in LAYOUT}
    flat = []
    for tid in live_order:
        if tid in qold_ids:
            continue
        flat.append((mod_of[tid], topics[tid]))
        if tid in teach_to_q:
            flat.append((mod_of[tid], teach_to_q[tid]))

    # ---- ids: global S/T/C counters inside each module, as core/qt.py does -----------------------------
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
    for cid, node in merged_into.items():          # folded concepts point at the concept they became part of
        id_map[cid] = node["_new_cid"]
    for mid, t in flat:                             # a kept video is renamed after its question concept
        for c in t["concepts"]:
            kv = kept_video.get(id(c))
            if kv:
                id_map[kv] = c["_new_cid"] + ".VID1"
    for cid, node in merged_into.items():          # folded videos point at the kept one
        v = video_of(cid)
        if v and kept_video[id(node)]:
            id_map[v] = id_map[kept_video[id(node)]]
    for mid_ in media_home:                         # every other media id follows its concept by prefix
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
        topic_nodes.append((mid, t2))
    plan["objectives"] = walk(plan["objectives"])
    plan["strand_to_objective_map"] = walk(plan["strand_to_objective_map"])
    plan["source_metadata"] = walk(plan["source_metadata"])
    seen_vc, vc = set(), []
    for e in walk(plan["video_coverage"]):
        k = (e["item_id"], e["video_id"])
        if k not in seen_vc:
            seen_vc.add(k)
            vc.append(e)
    plan["video_coverage"] = vc

    # ---- modules, segments, links, names ------------------------------------------------------------
    for m in plan["modules"]:
        m["segments"] = []
    modmap = {m["module_id"]: m for m in plan["modules"]}
    prev, nodes_only = None, [t for _, t in topic_nodes]
    for i, (mid, t) in enumerate(topic_nodes):
        if t.get("source_type") == "exercise":
            parent = nodes_only[i - 1]
            t["topic_name"] = "Questions: " + parent["topic_name"]
            t["summary"] = t["brief_summary"] = t["detailed_summary"] = "Practise: " + parent["topic_name"] + "."
            t["original_chunk"] = t["publication_chunk"] = t["summary"]
            t["ncert_sections"] = list(parent.get("ncert_sections", []))
            t["objective_ids"], t["learning_objectives"], t["topic_objective"] = [], [], None
            t["estimated_minutes"] = sum(c["estimated_minutes"] for c in t["concepts"])
        t["depends_on"] = [prev] if prev else []
        t["concept_bullets"] = [c["concept_name"] for c in t["concepts"]]
        seg = copy.deepcopy(template_segment)
        seg.update({"segment_id": "%s.S%d" % (mid, int(t["topic_id"].split(".S")[1].split(".T")[0])),
                    "segment_name": t["topic_name"], "summary": t["summary"], "brief_summary": t["brief_summary"],
                    "detailed_summary": t.get("detailed_summary", ""), "important_points": [], "recall_questions": [],
                    "segment_objective_ids": list(t.get("objective_ids", [])), "topics": [t]})
        modmap[mid]["segments"].append(seg)
        prev = t["topic_id"]

    # ---- coverage, stats, notes -----------------------------------------------------------------------
    old_cov = plan["source_metadata"]["ncert_coverage"]
    cov = {k: [] for k in old_cov}
    for t in nodes_only:
        for c in t["concepts"]:
            for r in c.get("ncert_refs") or []:
                cov.setdefault(r, [])
                if c["concept_id"] not in cov[r]:
                    cov[r].append(c["concept_id"])
    plan["source_metadata"]["ncert_coverage"] = cov
    media_all = [x for t in nodes_only for x in t.get("media", [])]
    qt_nodes = [t for t in nodes_only if t.get("source_type") == "exercise"]
    ss = plan["source_metadata"]["summary_stats"]
    ss.update({"topics": len(nodes_only), "concepts": sum(len(t["concepts"]) for t in nodes_only),
               "objectives": len(plan["objectives"]), "topic_objectives": sum(1 for t in nodes_only if t.get("topic_objective")),
               "question_topics": len(qt_nodes), "question_concepts": sum(len(t["concepts"]) for t in qt_nodes),
               "videos": sum(1 for x in media_all if x["type"] == "video"),
               "images": sum(1 for x in media_all if x["type"] == "image"),
               "tools": sum(1 for x in media_all if x["type"] == "2d_tool")})
    plan["estimated_time"] = round(sum(t.get("estimated_minutes", 0) for t in nodes_only) / 60, 2)
    plan["source_metadata"]["restructure"] = {
        "from": live["plan_id"],
        "layout": "concept topic, then its Questions topic (one concept per book question: solved examples, Figure it Out "
                  "items, answerable in-text prompts), then the next concept topic",
        "question_concepts": ss["question_concepts"],
        "note": "Order and home of questions only. Teaching text, objectives, tools and rendered videos are carried over; "
                "question images, solution images and new videos come in the next stage."}

    with io.open(OUT, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=1)
    report["counts"] = {k: ss[k] for k in ("topics", "concepts", "question_topics", "question_concepts", "objectives",
                                           "videos", "images", "tools")}
    report["id_map_concepts"] = {k: v for k, v in id_map.items()
                                 if re.match(r"^M\d+\.S\d+\.T\d+\.C\d+$", k) and k != v}
    with io.open(os.path.join(HERE, "restructure_report.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    lines = ["# Class 7 Ch 10 restructure: new order\n"]
    for mid, t in topic_nodes:
        lines.append("%s%s  %s  (%d concepts)" % ("    " if t.get("source_type") == "exercise" else "", t["topic_id"],
                                                    t["topic_name"], len(t["concepts"])))
        for c in t["concepts"]:
            lines.append("%s    %s  %s%s" % ("    " if t.get("source_type") == "exercise" else "", c["concept_id"],
                                              c["concept_name"], "" if c.get("media_ids") or t.get("source_type") != "exercise" else "   [new video needed]"))
    io.open(os.path.join(HERE, "restructure_report.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(json.dumps(report["counts"]))
    print("needs new video: %d | videos folded: %d" % (len(report["needs_new_video"]), len(report["videos_folded"])))


if __name__ == "__main__":
    main()
