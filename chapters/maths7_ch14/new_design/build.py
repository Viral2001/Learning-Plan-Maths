# -*- coding: utf-8 -*-
"""TEMPLATE - the thin per-chapter build script. Copy this whole chapter_template/ folder to a new
chapter's own new_design/ folder, fill in every TODO in the sibling files, then run this unchanged
(it is not itself a template with TODOs - everything chapter-specific lives in chapter.config.json,
content.py, concept_plan.py, media_specs.py and book_rules.json next to it).

    python -B build.py                  build <chapter_id>.json, then run every gate and print pass/fail
    python -B build.py --check          run the gates only, against the <chapter_id>.json already on disk
    python -B build.py --worklist       (re)write media_worklist.json (image specs still to author), then stop
    python -B build.py --video-worklist (re)write video_worklist.json (video scripts still to author), then stop

This pipeline is Phase-2-only, direct build (user preference): the output plan has "phase": 2 and
"chapter_id" with NO "_V3" suffix, written straight to <chapter_id>.json - there is no separate
_V3 file and no to_phase2.py mirroring step.

Required build order once this script has run (validation/STAMP_FORMAT.md):
    build.py  ->  core/set_version.py  ->  core/published_media.py pin-videos (if rebuilding over
    live assets)  ->  validation/validate_local.py  ->  upload/upload_lp.py --dry-run  ->  upload_lp.py
"""
from __future__ import annotations

import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _find_pipeline_root(start):
    """Walk up from `start` looking for the directory that holds both gates/ and core/ as real
    sub-packages. This is the "pipeline root" regardless of how many folders deep this copy of
    chapter_template/ has been placed (Std_9/maths9_ch7/new_design/, or anywhere else) - a fixed
    `os.path.dirname(os.path.dirname(...))` would break the moment a chapter folder is nested one
    level differently than chapter_template/ itself is, so this looks for the markers instead of
    counting levels."""
    d = os.path.abspath(start)
    for _ in range(12):
        if os.path.isdir(os.path.join(d, "gates")) and os.path.isdir(os.path.join(d, "core")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent
    raise SystemExit("could not find the pipeline root (a folder containing both gates/ and core/) "
                      "above %r - this script must live somewhere under the pipeline, even if it "
                      "has been copied several folders deep" % start)


ROOT = _find_pipeline_root(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from gates import gate_runner               # noqa: E402
from gates import media_content             # noqa: E402
from core import qt as QT                   # noqa: E402
from core.video_script import check as VC   # noqa: E402
from core.video_script import node as VN    # noqa: E402
from core.video_script import plan_hook as VH  # noqa: E402

import content as K          # noqa: E402  (chapter author's content.py, same folder)
import concept_plan as CP    # noqa: E402  (chapter author's concept_plan.py, same folder)
import media_specs as MS     # noqa: E402  (chapter author's media_specs.py, same folder)
from tools_spec.tool_node_builder import build_tool_node  # noqa: E402

CONFIG_PATH = os.path.join(HERE, "chapter.config.json")
WORKLIST_PATH = os.path.join(HERE, "media_worklist.json")
VIDEO_WORKLIST_PATH = os.path.join(HERE, "video_worklist.json")
VIDEO_SCRIPT_DIR = os.path.join(HERE, "video_scripts")
PHOTO_DIR = os.path.join(HERE, "photos")


def load_config():
    if not os.path.exists(CONFIG_PATH):
        raise SystemExit("no chapter.config.json next to build.py - copy "
                          "chapter.config.json.sample and fill it in first")
    with io.open(CONFIG_PATH, encoding="utf-8") as f:
        cfg = json.load(f)
    missing = [k for k in ("chapter_id", "chapter_master_id", "phase", "grade", "chapter_no",
                           "chapter_name", "media_tag", "asset_base_template") if not cfg.get(k)
               and cfg.get(k) != 0]
    if missing:
        raise SystemExit("chapter.config.json is missing: %s" % missing)
    if cfg["phase"] != 2:
        raise SystemExit("chapter.config.json phase must be 2 - this pipeline is Phase 2 only")
    if "_V3" in cfg["chapter_id"] or "_v3" in cfg["chapter_id"].lower():
        raise SystemExit("chapter_id must not carry a _V3 suffix in this pipeline")
    return cfg


def out_path(cfg):
    return os.path.join(HERE, "%s.json" % cfg["chapter_id"])


# ---------------------------------------------------------------------------
# assembling modules -> segments -> topics -> concepts from concept_plan.TOPICS
# ---------------------------------------------------------------------------
def _content_block(kind, text, **extra):
    d = {"type": "paragraph", "block_kind": kind, "text": text, "publication_text": text}
    d.update(extra)
    return d


def _teach_blocks(concept):
    blocks = []
    if concept.get("textbook"):
        blocks.append(_content_block("textbook_text", "\n".join(concept["textbook"]),
                                     lines=concept["textbook"]))
    if concept.get("teach"):
        blocks.append(_content_block("teaching_plan", "\n".join(
            "%d. %s" % (i, s) for i, s in enumerate(concept["teach"], 1)), steps=concept["teach"]))
    for n, ex in enumerate(concept.get("examples") or []):
        text = "\n".join(["Worked example: %s" % ex["q"]]
                         + ["%d. %s" % (i, s) for i, s in enumerate(ex["steps"], 1)]
                         + ["Answer: %s" % ex["answer"]])
        blocks.append(_content_block("worked_example", text, example_id="E%d" % n, question=ex["q"],
                                     steps=ex["steps"], answer=ex["answer"], ncert_refs=ex.get("ncert") or []))
    if concept.get("recap"):
        blocks.append(_content_block("recap", "\n".join(concept["recap"])))
    for it in concept.get("items") or []:
        text = "\n".join(["%s: %s" % (it["book"], it["question"])]
                         + ["%d. %s" % (i, s) for i, s in enumerate(it["steps"], 1)]
                         + ["Answer: %s" % it["answer"]])
        # worked_example + item_kind "exercise", the Ch10 question-block shape; core.qt moves only
        # worked_example blocks into the Figure it Out topic.
        blocks.append(_content_block("worked_example", text, item_kind="exercise", coverage_id=it["cov"],
                                     exercise_id=it["cov"], book_number=it["book"], question=it["question"],
                                     steps=it["steps"], answer=it["answer"], ncert_refs=[it["cov"]],
                                     **({"related_tool": it["tool"]} if it.get("tool") else {})))
    return blocks


# topic_type -> gates/skeleton.py's `source_type` vocabulary (DEFAULTS in that file).
SOURCE_TYPE = {"framing": "framing", "instructional": "instructional/exploration", "summary": "summary"}


def _concept_role(c):
    """source_segment_role for gates/skeleton.py: an explicit concept_plan role= wins; otherwise a
    DOER concept is "doer" and a teach concept carrying video_focus=["HOOK", ...] is "hook"."""
    if c.get("role"):
        return c["role"]
    if c.get("kind") == "doer":
        return "doer"
    if "HOOK" in (c.get("video_focus") or []):
        return "hook"
    return None


def assemble(cfg):
    """Returns (plan, concept_media_by_authored_key) - the second lets later passes (video building,
    tool nodes) find the concept that owns a given authored key ("T2.C2" etc.)."""
    asset_base = cfg["asset_base_template"].format(grade=cfg["grade"], chapter_no=cfg["chapter_no"])
    media_tag = cfg["media_tag"]

    modules_order = []  # [(module_id, [topics...])]
    by_module = {}
    for t in CP.TOPICS:
        by_module.setdefault(t["module"], []).append(t)
        if t["module"] not in [m for m, _ in modules_order]:
            modules_order.append((t["module"], by_module[t["module"]]))

    modules_out = []
    concept_lookup = {}       # authored key "T2.C2" -> built concept dict (for video/tool passes)
    objectives_out = []
    ncert_coverage = {}       # coverage id -> [concept_id, ...], for plan.source_metadata (core.qt reads this)
    topic_n = 0
    concept_n = 0

    for module_id, topics in modules_order:
        module_name = next((n for mid, n, _ in K.MODULES if mid == module_id), module_id)
        module_summary = next((s for mid, _, s in K.MODULES if mid == module_id), "")
        segments_out = []
        for t in topics:
            # One segment per topic, numbered with the same running counter as the topic itself
            # (the reference chapters' own convention: "M1.S3.T3", never several topics sharing
            # one segment) - core.qt's own renumbering relies on this 1:1 shape.
            topic_n += 1
            full_topic_id = "%s.S%d.T%d" % (module_id, topic_n, topic_n)
            concepts_out = []
            media_out = []
            available_types = set()
            topic_objective_ids = []
            for c in t["concepts"]:
                concept_n += 1
                cid = "C%d" % concept_n
                full_cid = "%s.%s" % (full_topic_id, cid)
                concept_lookup[c["key"]] = {"concept": c, "concept_id": full_cid, "topic": t}
                blocks = _teach_blocks(c)
                available_types.add("text")
                tool_media_id = None
                if c.get("kind") == "doer" and c.get("tool"):
                    spec = CP.TOOLS.get(c["tool"])
                    if spec is None:
                        raise SystemExit("concept %s names tool %r, which is not in CP.TOOLS"
                                         % (c["key"], c["tool"]))
                    tool_media_id = "%s.2D1" % full_cid
                    node = build_tool_node(
                        media_id=tool_media_id, concept_id=full_cid, tool_name=spec["title"],
                        tool_config=spec, tool_questions=spec["challenges"],
                        tool_2d_url="%s/tool_v3/%s/index.html" % (asset_base, spec["tool_id"]),
                        grade=cfg["grade"])
                    media_out.append(node)
                    available_types.add("2d_tool")
                ncert_refs = list(c.get("ncert") or [])
                for ex in c.get("examples") or []:
                    ncert_refs += ex.get("ncert") or []
                for it in c.get("items") or []:
                    ncert_refs.append(it["cov"])
                for cov_id in ncert_refs:
                    ncert_coverage.setdefault(cov_id, []).append(full_cid)
                is_enrichment_c = bool(c.get("enrichment"))
                objective_id = None
                if not is_enrichment_c and c.get("objective"):
                    objective_id = "%s.OBJ1" % full_cid
                    objectives_out.append({
                        "objective_id": objective_id,
                        "anchor": [full_cid],
                        "home_topic_id": full_topic_id,
                        "objective_text": c["objective"],
                        "bloom_level": c.get("bloom"),
                    })
                    topic_objective_ids.append(objective_id)
                # Ch10's thin split: one video per concept, so a teach concept with more than one worked
                # example keeps its first example and each further example becomes its own concept (same
                # name, that one worked_example block, enrichment, no objective, _is_thin_extra).
                thin = []
                if c.get("kind") == "teach" and t["topic_type"] == "instructional" \
                        and len(c.get("examples") or []) > 1:
                    thin = [b for b in blocks if b.get("example_id") not in (None, "E0")]
                    blocks = [b for b in blocks if b not in thin]
                concepts_out.append({
                    "concept_id": full_cid,
                    "concept_name": c.get("name") or c.get("objective", "")[:60],
                    "content": blocks,
                    "bloom_level": c.get("bloom"),
                    "key_terms": c.get("key_terms") or [],
                    "misconceptions": c.get("misconceptions") or [],
                    "tool_media_id": tool_media_id,
                    "ncert_refs": ncert_refs,
                    "is_enrichment": is_enrichment_c,
                    "enrichment_type": "enrichment" if is_enrichment_c else "content",
                    "source_segment_role": _concept_role(c),
                    "objective_id": objective_id,
                    "_is_thin_extra": False,
                })
                concept_lookup[c["key"]]["thin"] = {}
                for b in thin:
                    concept_n += 1
                    thin_cid = "%s.C%d" % (full_topic_id, concept_n)
                    concept_lookup[c["key"]]["thin"][b["example_id"]] = thin_cid
                    concepts_out.append({
                        "concept_id": thin_cid,
                        "concept_name": c.get("name") or c.get("objective", "")[:60],
                        "content": [b],
                        "bloom_level": c.get("bloom"),
                        "key_terms": [],
                        "misconceptions": [],
                        "tool_media_id": None,
                        "ncert_refs": [],
                        "is_enrichment": True,
                        "enrichment_type": "enrichment",
                        "source_segment_role": _concept_role(c),
                        "objective_id": None,
                        "_is_thin_extra": True,
                    })
            is_enrichment_t = t["topic_type"] == "framing"
            topic_objective = None
            if t["topic_type"] == "instructional" and t.get("objective"):
                topic_objective = {
                    "objective_id": "%s.TOBJ1" % full_topic_id,
                    "objective_text": t["objective"],
                    "home_topic_id": full_topic_id,
                }
            summary_text = t.get("summary", "")
            topics_out = [{
                "topic_id": full_topic_id,
                "topic_name": t["name"],
                "topic_type": t["topic_type"],
                "source_type": SOURCE_TYPE[t["topic_type"]],
                "is_enrichment": is_enrichment_t,
                "topic_objective": topic_objective,
                "topic_summary": summary_text,
                "summary": summary_text,
                "brief_summary": summary_text,
                "detailed_summary": summary_text,
                "ncert_sections": t.get("ncert_sections") or [],
                "key_terms": t.get("key_terms") or [],
                "concepts": concepts_out,
                "media": media_out,
                "available_content_types": sorted(available_types),
                "depends_on": [],
                "objective_ids": topic_objective_ids,
            }]
            segments_out.append({
                "segment_id": "%s.S%d" % (module_id, topic_n),
                "topics": topics_out,
            })
        modules_out.append({
            "module_id": module_id,
            "module_name": module_name,
            "module_summary": module_summary,
            "segments": segments_out,
        })

    plan = {
        "chapter_id": cfg["chapter_id"],
        "chapter_master_id": cfg["chapter_master_id"],
        "subject_ref_id": cfg["subject_ref_id"],
        "medium_id": cfg["medium_id"],
        "phase": 2,
        "grade": cfg["grade"],
        "chapter_no": cfg["chapter_no"],
        "chapter_name": cfg["chapter_name"],
        "chapter_approach": K.CHAPTER_APPROACH,
        "design_references": K.DESIGN_REFERENCES,
        "modules": modules_out,
        "objectives": objectives_out,
        "source_metadata": {
            "chapter": K.CHAPTER,
            "ncert_coverage": ncert_coverage,
            "summary_stats": {},
        },
    }
    return plan, concept_lookup, asset_base


# ---------------------------------------------------------------------------
# image worklist / video worklist (author-facing, --worklist / --video-worklist stop here)
# ---------------------------------------------------------------------------
def write_media_worklist(concept_lookup):
    entries = []
    for key, info in concept_lookup.items():
        c = info["concept"]
        entries.append({
            "key": key, "concept_id": info["concept_id"],
            "examples": [{"id": "E%d" % i} for i in range(len(c.get("examples") or []))],
            "exercises": [it["cov"] for it in c.get("items") or []],
            "video_focus": c.get("video_focus") or [],
            "has_image_decision": key in (MS.load_all()[1] if hasattr(MS, "load_all") else {}),
        })
    with io.open(WORKLIST_PATH, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=1)
    return len(entries)


def _exercise_numbers(slots):
    """Numbers of every book question, for the book guard (hook, recap and 'your turn' reuse none of them)."""
    import re as _re
    out = {}
    for sl in slots:
        for it in sl.get("items") or []:
            out[it["id"]] = [int(n) for n in _re.findall(r"\d+", it["question"])]
    return out


def write_video_worklist(concept_lookup, cfg):
    """One slot per concept that needs a video: a hook for the framing topic, a worked slot per
    worked example, an exercise slot per FIO/exercise item, a theorem slot where content.py's
    THEOREMS-equivalent marks one. Kept deliberately simple here - a real chapter's build.py may
    need to add story/recap slots by hand the way the reference chapters' own build.py does."""
    slots = []
    for key, info in concept_lookup.items():
        c, cid = info["concept"], info["concept_id"]
        cslots = []
        if c.get("kind") == "teach" and c.get("video_focus"):
            for focus in c["video_focus"]:
                if focus == "RECAP":
                    continue    # Keeko design (28 Oct 2026): no recap video
                kind = {"HOOK": "hook"}.get(focus, "worked")
                cslots.append(VH.slot("%s.%s.%s" % (cfg["media_tag"], key, focus.lower()),
                                                        kind, source=[c.get("name", key)],
                                                        **({"handover": "Keep the question open: the next topic finds the two centres exactly and names the line through them.",
                                                            "note": "The chapter opener: two eyes drawn with arcs and the question of where the arc centres go, left open."}
                                                           if kind == "hook" else {})))
        thin_slots = {}   # thin concept id -> its one worked slot (Ch10's thin split, see assemble())
        for i, ex in enumerate(c.get("examples") or []):
            thin_cid = (info.get("thin") or {}).get("E%d" % i)
            (thin_slots.setdefault(thin_cid, []) if thin_cid else cslots).append(VH.slot("%s.%s.E%d" % (cfg["media_tag"], key, i),
                                                    "worked", source=[ex["q"][:60]], item_ids=ex.get("ncert") or [],
                                                    items=[{"id": "E%d" % i, "question": ex["q"],
                                                            "steps": ex["steps"], "answer": ex["answer"]}],
                                                    answer=ex["answer"]))
        for it in c.get("items") or []:
            cslots.append(VH.slot("%s.%s.%s" % (cfg["media_tag"], key, it["cov"]),
                                                    "exercise", source=[it["book"]], item_ids=[it["cov"]],
                                                    items=[{"id": it["cov"], "question": it["question"],
                                                            "steps": it["steps"], "answer": it["answer"]}],
                                                    answer=it["answer"]))
        slots += VH.number_slots(cid, cslots)
        for thin_cid, tslots in thin_slots.items():
            slots += VH.number_slots(thin_cid, tslots)
    header = {"chapter_id": cfg["chapter_id"], "grade": cfg["grade"], "name": cfg["chapter_name"],
              "chapter_no": cfg["chapter_no"],
              "allow_words": sorted(set(cfg.get("allow_words") or [])),
              "hard_words": ["perpendicular bisector (define it)", "congruent (define it)", "SSS (say: side side side)",
                             "SAS (say: side angle side)", "bisect (define it)", "transversal (define it)",
                             "equilateral (define it)", "tiling (define it)"],
              "names_note": "Vary names across regions, religions and genders; Keeko raises the wrong ideas at the end of a concept video.",
              "length_override": {},
              "exercise_numbers": _exercise_numbers(slots)}
    return VH.write_worklist(VIDEO_WORKLIST_PATH, header, slots)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    cfg = load_config()
    plan, concept_lookup, asset_base = assemble(cfg)

    if "--worklist" in sys.argv:
        n = write_media_worklist(concept_lookup)
        print("wrote %s (%d entries) - author media_specs/<key>.json for each, then re-run build.py"
              % (WORKLIST_PATH, n))
        return 0

    if "--video-worklist" in sys.argv:
        n = write_video_worklist(concept_lookup, cfg)
        print("wrote %s (%d video slots) - author video_scripts/<key>.json for each, then re-run build.py"
              % (VIDEO_WORKLIST_PATH, n))
        return 0

    if "--check" in sys.argv:
        out = out_path(cfg)
        if not os.path.exists(out):
            raise SystemExit("%s does not exist yet - run build.py once without --check first" % out)
        with io.open(out, encoding="utf-8") as f:
            plan = json.load(f)
    else:
        # fold in any authored images (media_specs/*.json) as image media nodes, keyed by concept.
        images, decisions = MS.load_all() if os.path.isdir(os.path.join(HERE, "media_specs")) else ({}, {})
        for module in plan["modules"]:
            for segment in module["segments"]:
                for topic in segment["topics"]:
                    for concept in topic["concepts"]:
                        key = next((k for k, v in concept_lookup.items()
                                   if v["concept_id"] == concept["concept_id"]), None)
                        # an image spec file is keyed by the authored concept key (media_specs/T3.C1.json);
                        # a thin split concept is reached by its own key "<key>.E<n>".
                        for k, info in concept_lookup.items():
                            for ex_id, thin_cid in (info.get("thin") or {}).items():
                                if thin_cid == concept["concept_id"]:
                                    key = "%s.%s" % (k, ex_id)
                        for n, im in enumerate(images.get(key, [])[:2], 1):
                            topic["media"].append(MS.build_image_node(im, concept["concept_id"], n, asset_base))
                            topic["available_content_types"] = sorted(
                                set(topic["available_content_types"]) | {"image"})

        # fold in any authored video scripts (video_scripts/*.json) via core.video_script.
        if os.path.isdir(VIDEO_SCRIPT_DIR):
            scripts = VH.load_scripts(VIDEO_SCRIPT_DIR)
            wl = VH.load_worklist(VIDEO_WORKLIST_PATH)
            if wl:
                nodes, missing = VH.build_nodes(wl["videos"], scripts, asset_base=asset_base,
                                                chapter_label=cfg["chapter_name"])
                if missing:
                    print("WARNING: %d video slot(s) still have no script file: %s"
                          % (len(missing), missing[:5]))
                by_concept = {}
                for nd in nodes:
                    by_concept.setdefault(nd["concept_id"], []).append(nd)
                for module in plan["modules"]:
                    for segment in module["segments"]:
                        for topic in segment["topics"]:
                            for concept in topic["concepts"]:
                                extra = by_concept.get(concept["concept_id"], [])
                                if extra:
                                    topic["media"].extend(extra)
                                    topic["available_content_types"] = sorted(
                                        set(topic["available_content_types"]) | {"video"})

                # tag the worked_example/exercise blocks each video slot was built from with that
                # slot's video_media_id, so core.qt.apply() (below) knows which content to move
                # into the sibling practice topic it inserts after an exercise slot.
                for s in wl["videos"]:
                    for module in plan["modules"]:
                        for segment in module["segments"]:
                            for topic in segment["topics"]:
                                for concept in topic["concepts"]:
                                    if concept["concept_id"] != s.get("concept_id"):
                                        continue
                                    ex_id = (s.get("items") or [{}])[0].get("id") if s.get("kind") == "worked" else None
                                    for b in concept["content"]:
                                        if b.get("block_kind") != "worked_example":
                                            continue
                                        if (ex_id and b.get("example_id") == ex_id and not b.get("item_kind")) \
                                                or (s.get("kind") == "exercise" and set(s.get("item_ids", [])) & (
                                                    {b.get("coverage_id")} | set(b.get("ncert_refs") or []))):
                                            b["video_media_id"] = s["video_id"]

                # every concept lists its own media, as in the Ch10 plan: images, videos, then its tool
                for module in plan["modules"]:
                    for segment in module["segments"]:
                        for topic in segment["topics"]:
                            for concept in topic["concepts"]:
                                own = [x for x in topic["media"] if x.get("concept_id") == concept["concept_id"]]
                                vids = [x["id"] for x in own if x.get("type") == "video"]
                                concept["media_ids"] = ([x["id"] for x in own if x.get("type") == "image"] + vids
                                                        + [x["id"] for x in own if x.get("type") == "2d_tool"])
                                concept["video_media_ids"] = vids
                                if vids:
                                    concept["walkthrough_video_id"] = vids[0]
                                concept["source_media"] = ("video" if vids else "2d_tool" if concept.get("tool_media_id")
                                                           else "image" if concept["media_ids"] else None)

                # QT (question-topic) pass: insert a sibling practice topic after every
                # instructional topic whose exercise slots were just tagged above. strand_map is
                # left empty here (no cross-chapter strand grouping in this template); a real
                # chapter wires it the way maths6_ch3/new_design's own build.py does if it needs one.
                _lab = {}
                for _v in wl["videos"]:
                    _txt = (_v.get("items") or [{}])[0].get("question") or (_v.get("source") or [""])[0]
                    for _i in _v.get("item_ids") or []:
                        _lab.setdefault(_i, "Book item: %s" % _txt)
                plan["video_coverage"] = VH.coverage(wl["videos"], _lab)
                QT.apply(plan, wl["videos"], cfg["media_tag"], {}, enrichment_qt=True)
                # QT moves each exercise ref off its teaching concept; rebuild ncert_coverage from the final
                # concept ncert_refs so the forward and reverse maps agree.
                _cov = {}
                for _m in plan["modules"]:
                    for _s in _m["segments"]:
                        for _t in _s["topics"]:
                            for _c in _t["concepts"]:
                                for _r in _c.get("ncert_refs") or []:
                                    _cov.setdefault(_r, [])
                                    if _c["concept_id"] not in _cov[_r]:
                                        _cov[_r].append(_c["concept_id"])
                plan["source_metadata"]["ncert_coverage"] = _cov
                # QT renumbers video ids but freezes planned_url and the walkthrough/interaction ids (for
                # already-published assets). Nothing is rendered yet for this chapter, so re-key them to the
                # final id, as in the Ch10 plan.
                for _m in plan["modules"]:
                    for _s in _m["segments"]:
                        for _t in _s["topics"]:
                            for _x in _t.get("media", []):
                                if _x.get("type") == "image":
                                    _x["planned_url"] = "%s/image_v3/%s.png" % (asset_base, _x["id"])
                                    continue
                                _sv = _x.get("source_video_walkthrough") or {}
                                _old = _sv.get("video_id")
                                if not _old or _old == _x["id"]:
                                    continue
                                _sv["video_id"] = _x["id"]
                                if _x.get("planned_url", "").endswith("/%s.mp4" % _old):
                                    _x["planned_url"] = _x["planned_url"][:-len(_old) - 4] + _x["id"] + ".mp4"
                                for _p in _x.get("interaction_points", []):
                                    if str(_p.get("id", "")).startswith(_old + "."):
                                        _p["id"] = _x["id"] + _p["id"][len(_old):]

        # Server-required fields the template does not set (publication 1 as in the Ch10 plan).
        plan.setdefault("publication_id", 1)
        for _m in plan["modules"]:
            for _s in _m["segments"]:
                for _t in _s["topics"]:
                    for _x in _t.get("media") or []:
                        if _x.get("type") == "2d_tool":
                            _x.setdefault("2d_tool_json", "")
        with io.open(out_path(cfg), "w", encoding="utf-8") as f:
            json.dump(plan, f, ensure_ascii=False, indent=1)
        print("wrote %s" % out_path(cfg))

    errors, counts = gate_runner.run(plan, cfg)
    warnings = counts.pop("warnings", [])
    print("counts:", counts)
    if warnings:
        # Advisory only - see gates/gate_runner.py's "Blocking errors vs advisory warnings".
        # Never blocks the build; printed so the author sees it before validate_local.py does.
        print("%d ADVISORY WARNING(S) (non-blocking):" % len(warnings))
        for w in warnings:
            print("  ~", w)
    if errors:
        print("%d GATE FAILURE(S):" % len(errors))
        for e in errors:
            print("  -", e)
        return 1
    print("all gates passed (blocking)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
