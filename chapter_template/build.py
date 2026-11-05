# -*- coding: utf-8 -*-
"""TEMPLATE - the thin per-chapter build script. Copy this whole chapter_template/ folder to a new
chapter's own new_design/ folder, fill in every TODO in the sibling files, then run this unchanged
(it is not itself a template with TODOs - everything chapter-specific lives in chapter.config.json,
content.py, concept_plan.py, media_specs.py and book_rules.json next to it).

    python -B build.py                  build <chapter_id>.json, then run every gate and print pass/fail
    python -B build.py --check          run the gates only, against the <chapter_id>.json already on disk
    python -B build.py --worklist       (re)write media_worklist.json (image specs still to author), then stop
    python -B build.py --video-worklist (re)write video_worklist.json (video scripts still to author), then stop
    python -B build.py --solution-worklist  (re)write solution_worklist.json (exercise items with no entry in
                                        solutions.json yet), then stop
    python -B build.py --placeholders   build the plan with its question layout and the image PLACEHOLDERS of every
                                        question (question card, solution card, a second solution card for a long
                                        working), without requiring solutions.json yet. Questions that already have
                                        a solutions.json entry get their real cards; the rest keep placeholders.

Question layout (chapter.config.json "question_layout": true): every concept topic is followed by one
"Questions: <category>" topic per book category found there (core/question_naming.py), each with a question
concept and a sibling answer concept per book question of that category - each solved example, Figure it Out
/ exercise item and answerable in-text prompt, written as an `items` entry (concept_plan.FIO, kind="example" |
"exercise" | "prompt") - and core/qt.py does the moving, categorising, splitting and naming. See
docs/00_overview.md "Question layout".

Solutions (chapter.config.json "solutions": true): solutions.json (core/solutions/schema.py) holds each
question's board-format solution. build.py writes its working and answer into the plan, and into the video
worklist's items; core/solutions/gen_scenes.py + render.py make the question and solution images
(solution_images/), which build.py attaches as media_ids = [question image, video, solution image (, solution
image continued)]. Before any solution exists, core/solutions/placeholders.py has already put the same image
nodes on every question as placeholders, so the structure can be reviewed first.

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
from core.solutions import attach as SA     # noqa: E402
from core.solutions import placeholders as SP  # noqa: E402
from core.solutions import bind as SB       # noqa: E402
from core.solutions import check as SC      # noqa: E402
from core.solutions import schema as SS     # noqa: E402

import content as K          # noqa: E402  (chapter author's content.py, same folder)
import concept_plan as CP    # noqa: E402  (chapter author's concept_plan.py, same folder)
import media_specs as MS     # noqa: E402  (chapter author's media_specs.py, same folder)
from tools_spec.tool_node_builder import build_tool_node  # noqa: E402

CONFIG_PATH = os.path.join(HERE, "chapter.config.json")
WORKLIST_PATH = os.path.join(HERE, "media_worklist.json")
VIDEO_WORKLIST_PATH = os.path.join(HERE, "video_worklist.json")
VIDEO_SCRIPT_DIR = os.path.join(HERE, "video_scripts")
SOLUTION_WORKLIST_PATH = os.path.join(HERE, "solution_worklist.json")
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
    # Every question carries its step-by-step solution in the concept AND a question image + a solution image.
    # That is the default for a new chapter, so the key must be decided: true, or an explicit false to opt out.
    if "solutions" not in cfg:
        raise SystemExit('chapter.config.json has no "solutions" key. Add "solutions": true (every question gets '
                         'working + answer in the concept, a question image and a solution image), or an '
                         'explicit false only if the teacher asked for a chapter without them.')
    if cfg["solutions"] not in (True, False):
        raise SystemExit('chapter.config.json "solutions" must be true or false (the text-only mode is not '
                         'allowed for new chapters: both the written solution and the two images are required)')
    return cfg


def out_path(cfg):
    return os.path.join(HERE, "%s.json" % cfg["chapter_id"])


def book_item_kinds():
    """{book id: kind} from content.NCERT_ITEMS. An entry is "id" (kind unknown, not checked), ("id", "kind") or
    {"id": ..., "kind": ...}; kind is example | exercise | prompt | talk | text. gates/question_layout.py checks
    that every item whose kind is in the chapter's question_scope sits in a concept of a Questions topic."""
    kinds = {}
    for entry in getattr(K, "NCERT_ITEMS", []) or []:
        if isinstance(entry, dict):
            kinds[entry["id"]] = entry.get("kind")
        elif isinstance(entry, (list, tuple)) and len(entry) == 2:
            kinds[entry[0]] = entry[1]
    return {k: v for k, v in kinds.items() if v}


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
    for ex in concept.get("examples") or []:
        text = "\n".join(["Worked example: %s" % ex["q"]]
                         + ["%d. %s" % (i, s) for i, s in enumerate(ex["steps"], 1)]
                         + ["Answer: %s" % ex["answer"]])
        blocks.append(_content_block("worked_example", text, question=ex["q"], steps=ex["steps"],
                                     answer=ex["answer"], ncert_refs=ex.get("ncert") or []))
    if concept.get("recap"):
        blocks.append(_content_block("recap", "\n".join(concept["recap"])))
    for it in concept.get("items") or []:
        # question_tex/steps_tex/answer_tex (core/solutions/bind.py, once solutions.json has this item) are
        # the same working, kept as the inline-LaTeX ($...$) text it was authored with; the displayed text
        # uses them when present, so the student reads the maths as LaTeX, not the plain/eqcheck form.
        q_disp = it.get("question_tex") or it["question"]
        steps_disp = it.get("steps_tex") or it["steps"]
        answer_disp = it.get("answer_tex") or it["answer"]
        # Step index wrapped as "$N$." per LATEX_REFERENCE.md's step-identification rule, but only
        # when steps_tex is actually authored - a plain-text fallback must stay bare.
        _idx_fmt = "$%d$. %s" if it.get("steps_tex") else "%d. %s"
        text = "\n".join(["%s: %s" % (it["book"], q_disp)]
                         + [_idx_fmt % (i, s) for i, s in enumerate(steps_disp, 1)]
                         + ["Answer: %s" % answer_disp])
        # worked_example + item_kind "exercise", the question-block shape every built chapter uses; core.qt
        # moves only worked_example blocks into the practice topic.
        # book_kind: "example" (a solved example of the book), "exercise" (Figure it Out / exercise question) or
        # "prompt" (an answerable in-text question); q_figure / s_figure: one plain sentence for the diagram the
        # question card / solution card needs (core/solutions/placeholders.py), left out when the card is text only.
        extra = {k: it[k] for k in ("q_figure", "s_figure", "question_tex", "steps_tex", "answer_tex") if it.get(k)}
        blocks.append(_content_block("worked_example", text, item_kind="exercise", coverage_id=it["cov"],
                                     exercise_id=it["cov"], book_number=it["book"], question=it["question"],
                                     steps=it["steps"], answer=it["answer"], ncert_refs=[it["cov"]],
                                     book_kind=it.get("kind", "exercise"), **extra))
    return blocks


# topic_type -> gates/skeleton.py's `source_type` vocabulary (DEFAULTS in that file).
SOURCE_TYPE = {"framing": "framing", "instructional": "instructional/exploration", "summary": "summary"}

# primary_/secondary_/tertiary_content_type: priority image > video > 2d_tool > 3d_tool, except the
# chapter's very first topic (its Introduction video), where video is primary.
CONTENT_TYPE_PRIORITY = ("image", "video", "2d_tool", "3d_tool")


def _content_type_triad(available_content_types, is_first_topic):
    order = list(CONTENT_TYPE_PRIORITY)
    if is_first_topic and "video" in available_content_types:
        order.remove("video")
        order.insert(0, "video")
    present = [t for t in order if t in available_content_types]
    primary = present[0] if present else None
    secondary = present[1] if len(present) > 1 else None
    tertiary = present[2] if len(present) > 2 else None
    return primary, secondary, tertiary


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
                # NOTE: "text" is deliberately NOT added to available_types here - that field is
                # "distinct media types present" (image/video/2d_tool/3d_tool only); a topic's own
                # paragraph/worked-example content is not a media type and must never leak into it
                # (every concept always has content[], so seeding this would make the field
                # permanently non-empty and useless as a signal of what media actually exists).
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
                concepts_out.append({
                    "concept_id": full_cid,
                    "concept_name": c.get("name") or c.get("objective", "")[:60],
                    "content": blocks,
                    "bloom_level": c.get("bloom"),
                    "key_terms": c.get("key_terms") or [],
                    "misconceptions": c.get("misconceptions") or [],
                    "ncert_refs": ncert_refs,
                    "is_enrichment": is_enrichment_c,
                    "source_segment_role": _concept_role(c),
                    "objective_id": objective_id,
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
            # word_count is a simple, honest metric derived from the topic's own concept text - not
            # authored, so it can never drift from the content it's measuring.
            topic_words = " ".join(b.get("text", "") for c in concepts_out for b in c["content"]
                                   if isinstance(b.get("text"), str)).split()
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
                "source_topic_ids": t.get("ncert_sections") or [],
                "key_terms": t.get("key_terms") or [],
                "concepts": concepts_out,
                "media": media_out,
                "available_content_types": sorted(available_types),
                "depends_on": [],
                "objective_ids": topic_objective_ids,
                "recall_questions": [],
                "word_count": {"original": len(topic_words)},
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


def write_video_worklist(concept_lookup, cfg):
    """One slot per concept that needs a video, in the Keeko design (28 Oct 2026): a hook (once, for the
    chapter's first video_focus HOOK), a worked slot per worked example (the concept video; it ends with
    Keeko's raised hand), an exercise slot per FIO/exercise item (the question video; `method_from` names
    the solved examples of the same concept whose method it uses), a theorem slot for video_focus
    "THEOREM". "RECAP" is ignored: there is no recap video. Authors fill `{{NAME_n}}` name tokens; see
    name_slots.json.sample. A real chapter's build.py may add story slots by hand."""
    slots = []
    hook_done = False
    for key, info in concept_lookup.items():
        c, cid = info["concept"], info["concept_id"]
        cslots = []
        if c.get("kind") == "teach" and c.get("video_focus"):
            for focus in c["video_focus"]:
                if focus == "RECAP":
                    continue    # Keeko design: no recap video
                if focus == "HOOK":
                    if hook_done:
                        continue    # one hook per chapter
                    hook_done = True
                kind = {"HOOK": "hook", "THEOREM": "theorem"}.get(focus, "worked")
                cslots.append(VH.slot("%s.%s.%s" % (cfg["media_tag"], key, focus.lower()),
                                      kind, source=[c.get("name", key)],
                                      misconceptions=c.get("misconceptions") or []))
        for i, ex in enumerate(c.get("examples") or []):
            cslots.append(VH.slot("%s.%s.E%d" % (cfg["media_tag"], key, i),
                                  "worked", source=[ex["q"][:60]], item_ids=ex.get("ncert") or [],
                                  items=[{"id": "E%d" % i, "question": ex["q"],
                                          "steps": ex["steps"], "answer": ex["answer"]}],
                                  answer=ex["answer"], misconceptions=c.get("misconceptions") or []))
        for it in c.get("items") or []:
            cslots.append(VH.slot("%s.%s.%s" % (cfg["media_tag"], key, it["cov"]),
                                  "exercise", source=[it["book"]], item_ids=[it["cov"]],
                                  items=[{"id": it["cov"], "question": it["question"],
                                          "steps": it["steps"], "answer": it["answer"]}],
                                  answer=it["answer"]))
        slots += VH.number_slots(cid, cslots)
    # exercise videos name the solved examples of the same concept whose method they use
    worked = [s for s in slots if s["kind"] in ("worked", "theorem")]
    for s in slots:
        if s["kind"] == "exercise":
            stem = s["key"].rsplit(".", 1)[0]
            s["method_from"] = [w["key"] for w in worked if w["key"].rsplit(".", 1)[0] == stem]
    header = {"chapter_id": cfg["chapter_id"], "grade": cfg["grade"], "name": cfg["chapter_name"],
              "chapter_no": cfg["chapter_no"], "allow_words": sorted(set(cfg.get("allow_words") or [])),
              "hard_words": [], "length_override": {},
              "names_note": "Vary names across regions, religions and genders; use {{NAME_n}} tokens "
                            "(n up to 10, one character = one token) and list them in name_slots.json; "
                            "Keeko raises the wrong idea or a real-life link at the end of a concept video.",
              "exercise_numbers": VH.exercise_numbers([i for s in slots for i in s.get("items") or []])}
    return VH.write_worklist(VIDEO_WORKLIST_PATH, header, slots)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    cfg = load_config()
    sols = SS.load(HERE)
    if "--solution-worklist" in sys.argv:
        n = SB.write_worklist(SOLUTION_WORKLIST_PATH, {"chapter_id": cfg["chapter_id"], "grade": cfg["grade"],
                                                       "chapter_no": cfg["chapter_no"],
                                                       "schema": "core/solutions/schema.py",
                                                       "rules": "math_solutions/skill/references/format-rules.md"},
                              CP.TOPICS, sols)
        print("wrote %s (%d exercise items without a solution) - add each to solutions.json, then run "
              "core/solutions/gen_scenes.py" % (SOLUTION_WORKLIST_PATH, n))
        return 0
    if sols:
        print("solutions.json: %d solution(s) written into the items" % SB.fill(CP.TOPICS, sols))
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
                        figures = getattr(K, "FIGURES", {})
                        for im in images.get(key, []):
                            topic["media"].append({
                                "id": im["key"], "type": "image", "subtype": "illustration",
                                "title": im["title"], "concept_id": concept["concept_id"],
                                "related_concept_ids": [],
                                "home_concept_id": concept["concept_id"], "image_url": "",
                                "planned_url": "%s/image_v3/%s.png" % (asset_base, im["key"]),
                                "generation_prompt": im["exact_structure"], "labels": im["labels"],
                                "negative_prompt": MS.FLAT_NEGATIVE,
                                "accuracy_constraints": im["rejection"],
                                "grounding_quote": "",
                                "description": im["description"], "context": im["context"],
                                "teaching_notes": im["teaching_notes"],
                                "heading": "", "heading_style": "standard", "label_style": "standard",
                                "aspect_ratio": "16:9", "image_dimensions": "1456x816",
                                "objects": [], "scientific_facts": [],
                                "composition": im.get("composition", ""),
                                "predict_then_reveal": False,
                                "enrichment": bool(concept.get("is_enrichment")),
                                "source_figure": "; ".join(figures.get(key, []) or []),
                                "source_topic_no": (topic.get("source_topic_ids") or [""])[0],
                                "source_page": None,
                                "build_status": "placeholder",
                            })
                            topic["available_content_types"] = sorted(
                                set(topic["available_content_types"]) | {"image"})

        # fold in any authored video scripts (video_scripts/*.json) via core.video_script. --placeholders runs
        # before any script exists, so an absent video_scripts/ folder is fine there (the Questions topics and
        # their image placeholders still need this pass).
        if os.path.isdir(VIDEO_SCRIPT_DIR) or "--placeholders" in sys.argv:
            scripts = VH.load_scripts(VIDEO_SCRIPT_DIR) if os.path.isdir(VIDEO_SCRIPT_DIR) else {}
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
                                    for b in concept["content"]:
                                        if b.get("block_kind") in ("worked_example", "exercise") \
                                                and set(s.get("item_ids", [])) & (
                                                    {b.get("coverage_id")} | set(b.get("ncert_refs") or [])):
                                            b["video_media_id"] = s["video_id"]

                # QT (question-topic) pass: insert a sibling practice topic after every
                # instructional topic whose exercise slots were just tagged above.
                # every concept lists its own media, as the built chapters do: images, videos, then its tool
                for module in plan["modules"]:
                    for segment in module["segments"]:
                        for topic in segment["topics"]:
                            for concept in topic["concepts"]:
                                own = [x for x in topic["media"] if x.get("concept_id") == concept["concept_id"]]
                                vids = [x["id"] for x in own if x.get("type") == "video"]
                                has_tool = any(x.get("type") == "2d_tool" for x in own)
                                concept["media_ids"] = ([x["id"] for x in own if x.get("type") == "image"] + vids
                                                        + [x["id"] for x in own if x.get("type") == "2d_tool"])
                                concept["video_media_ids"] = vids
                                concept["source_media"] = ("video" if vids else "2d_tool" if has_tool
                                                           else "image" if concept["media_ids"] else None)

                labels = {}
                for v in wl["videos"]:
                    text = (v.get("items") or [{}])[0].get("question") or (v.get("source") or [""])[0]
                    for i in v.get("item_ids") or []:
                        labels.setdefault(i, "Book item: %s" % text)
                plan["video_coverage"] = VH.coverage(wl["videos"], labels)

                # enrichment_qt: the shape every Class 6-7 chapter ships - a "Figure it Out" topic with one
                # concept per question, each holding its own question video (<concept>.VID1). Without it the
                # question concepts get no video and solution_content fails them.
                QT.apply(plan, wl["videos"], cfg["media_tag"], getattr(K, "MODULE_STRANDS", {}),
                         enrichment_qt=True, topic_prefix="Questions" if cfg.get("question_layout") else None)

                # QT moves each exercise ref off its teaching concept; rebuild ncert_coverage from the final
                # concept ncert_refs so the forward and reverse maps agree.
                cov = {}
                for module in plan["modules"]:
                    for segment in module["segments"]:
                        for topic in segment["topics"]:
                            for concept in topic["concepts"]:
                                for r in concept.get("ncert_refs") or []:
                                    if concept["concept_id"] not in cov.setdefault(r, []):
                                        cov[r].append(concept["concept_id"])
                plan["source_metadata"]["ncert_coverage"] = cov

                # question and solution image PLACEHOLDERS on every question concept (nothing is drawn): the
                # structure is reviewable before any solution is authored, and attach() below swaps in the real
                # cards for the questions that have a solutions.json entry.
                if cfg.get("solutions"):
                    img_report = SP.add(plan, cfg)
                    with io.open(os.path.join(HERE, "question_images_report.json"), "w", encoding="utf-8") as f:
                        json.dump(img_report, f, ensure_ascii=False, indent=1)
                    # a split question/answer concept (core/qt.py) gives one report row per concept: a
                    # question-role row has no solution_images/has_video, an answer-role row has no
                    # question_diagram - .get() keeps this summary accurate either shape.
                    print("question images: %d concept(s), %d solution card(s) in all, %d with a diagram on "
                          "the question card, %d without a video yet (question_images_report.json)"
                          % (len(img_report), sum(r.get("solution_images", 0) for r in img_report),
                             sum(1 for r in img_report if r.get("question_diagram")),
                             sum(1 for r in img_report if r.get("has_video") is False)))

        # solutions: check solutions.json + its scene files, then hang the question and solution images on
        # each question concept as media_ids = [question image, video(s), solution image].
        mode = cfg.get("solutions")
        if mode:
            todo = SB.missing(CP.TOPICS, sols)
            if todo and "--placeholders" in sys.argv:
                print("placeholders: %d question(s) have no solutions.json entry yet and keep their image "
                      "placeholders (build.py --solution-worklist lists them)" % len(todo))
            elif todo:
                print("%d QUESTION(S) HAVE NO SOLUTION in solutions.json (run build.py --solution-worklist):"
                      % len(todo))
                for t in todo[:25]:
                    print("  -", t["cov"], t["book"] or "", t.get("note") or "")
                return 1
        if mode and sols:
            errs, warns = SC.check(HERE)
            for w in warns:
                print("  ~ solutions:", w)
            if errs:
                print("%d SOLUTION PROBLEM(S):" % len(errs))
                for e in errs:
                    print("  -", e)
                return 1
            problems = SA.attach(plan, HERE, SA.key_dir_for(cfg))
            if problems:
                print("%d SOLUTION ATTACH PROBLEM(S):" % len(problems))
                for p in problems:
                    print("  -", p)
                return 1

        all_topics_in_order = [topic for module in plan["modules"] for segment in module["segments"]
                               for topic in segment["topics"]]
        for i, topic in enumerate(all_topics_in_order):
            primary, secondary, tertiary = _content_type_triad(topic["available_content_types"], i == 0)
            topic["primary_content_type"] = primary
            topic["secondary_content_type"] = secondary
            topic["tertiary_content_type"] = tertiary

        with io.open(out_path(cfg), "w", encoding="utf-8") as f:
            json.dump(plan, f, ensure_ascii=False, indent=1)
        print("wrote %s" % out_path(cfg))

    gate_cfg = dict(cfg, book_item_kinds=book_item_kinds()) if cfg.get("question_layout") else cfg
    errors, counts = gate_runner.run(plan, gate_cfg)
    warnings = counts.pop("warnings", [])
    expected = []
    if "--placeholders" in sys.argv:
        # structure stage: no video script exists yet, so the video gates (no hook video, video_coverage pointing at
        # videos not made, a question concept with no video between its two cards) cannot pass yet. Show them apart
        # from the failures that need fixing now.
        has_scripts = os.path.isdir(VIDEO_SCRIPT_DIR) and any(
            f.endswith(".json") for f in os.listdir(VIDEO_SCRIPT_DIR))
        if not has_scripts:
            expected = [e for e in errors if e.startswith("video_script_rules:")
                        or ("solution_content:" in e and "needs the question video" in e)]
            errors = [e for e in errors if e not in expected]
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
    if expected:
        print("structure stage OK: the question layout and the image placeholders pass every gate that can pass "
              "now. %d video gate message(s) are expected until video_scripts/ exist, and the solutions are still "
              "to author. This plan is NOT ready to validate or upload." % len(expected))
        return 0
    print("all gates passed (blocking)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
