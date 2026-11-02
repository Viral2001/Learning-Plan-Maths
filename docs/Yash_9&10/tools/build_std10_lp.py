"""Build a Class 10 concept-level learning plan from its representative plan (md) and the phase-1 plan.

Usage (from anywhere):  python -I -X utf8 build_std10_lp.py <chapter number>
Reads  ..\\std10_ch<N>\\maths10_ch<N>_representative_lp.md          structure and concept content
       ..\\std10_ch<N>\\learning_plan_std10_chap<N>_version1.json   old plan: media objects, topic fields, header
Writes ..\\std10_ch<N>\\learning_plan_std10_chap<N>_version2.json   (local only, `_activate` false, never uploaded)

Per-chapter values that cannot be read from the md live in CONFIG below.

Solutions: when ../std10_ch<N>/solutions.json exists (core/solutions/schema.py; keys are the question ids
"<exercise>.Q<n>[.<part>]"), each question it covers gets its working and answer from there (solution_status
"authored" instead of "to_author"), and, if ../std10_ch<N>/solution_images/ was generated
(core/solutions/gen_scenes.py), its question and solution images: media_ids = [question image, video if any,
solution image]. Question videos are held for Class 10 for now, so enforce with chapter.config.json
{"solutions": true, "solutions_video": false}.
"""
import os as _os
PLAN_VERSION = int(_os.environ.get('LP_VERSION', '2'))  # v1 already exists on staging

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def _pipeline_root(start):
    d = os.path.abspath(start)
    while not (os.path.isdir(os.path.join(d, "core")) and os.path.isdir(os.path.join(d, "gates"))):
        if os.path.dirname(d) == d:
            raise SystemExit("pipeline root (a folder holding core/ and gates/) not found above %s" % start)
        d = os.path.dirname(d)
    return d


sys.path.insert(0, _pipeline_root(HERE))
from core.solutions import attach as SA   # noqa: E402
from core.solutions import check as SC    # noqa: E402
from core.solutions import schema as SS   # noqa: E402

CONFIG = {
    1: {
        "name": "Real Numbers",
        "exercises": ["1.1", "1.2"],
        "examples": {},        # concept number -> book example ref (metadata only)
        "notes": {},           # concept number -> ref for a note concept
        "topic_map": None,     # old topic number -> new topic number; None = read Appendix C of the md
    },
    2: {"name": "Polynomials", "exercises": ["2.1", "2.2"], "examples": {}, "notes": {}, "topic_map": None},
    3: {"name": "Pair of Linear Equations in Two Variables", "exercises": ["3.1", "3.2", "3.3"],
        "examples": {}, "notes": {}, "topic_map": None},
    7: {"name": "Coordinate Geometry", "exercises": ["7.1", "7.2"], "examples": {}, "notes": {},
        "topic_map": {1: 2, 2: 1, 3: 3, 4: 4, 5: 4, 6: 5, 7: 6, 8: 7, 9: 6, 10: 7, 11: 7, 12: 8, 13: 9}},
}
try:
    _extra = json.load(open(os.path.join(HERE, "chapter_config.json"), encoding="utf8"))
    for k, v in _extra.items():
        CONFIG.setdefault(int(k), {}).update({kk: ({int(a): b for a, b in vv.items()} if kk in ("examples", "notes", "topic_map") and vv else vv)
                               for kk, vv in v.items()})
except FileNotFoundError:
    pass

ASSET_BASE = "https://media.singularity-learn.com/learning_plan_assets/V2/cbse/cbse/english/class_10/mathematics/ch_{n}"
MINUTES = {"hook": 5, "teach": 8, "try": 6, "prove": 10, "example": 8, "question": 6, "enrich": 3, "summary": 8}
ROLE = {"hook": "hook", "teach": "teaching", "try": "try_it", "prove": "proof", "exercise": "practice",
        "enrich": "enrichment", "summary": "summary"}
REVIEW_ONLY_TAGS = ("figure note",)


def clean(s):
    return s.replace("**", "").strip()


def no_dashes(s):
    """The upload preflight forbids em and en dashes: spaced em dash -> ' - ', en dash -> hyphen."""
    s = re.sub(r"\s*—\s*", " - ", s)
    return s.replace("–", "-").replace("—", "-")


def clean_title(t):
    """Strip book numbers (Example n, Exercise n.n Qn, Theorem n.n, Table n.n, Fig. n.n, Chapter n) from a media title."""
    t = re.sub(r"\s*\((?:Fig\.?|Figure|Table|Example|Theorem|Exercise)[^)]*\)", "", t)
    t = re.sub(r"\s+(?:and|with|in|for)\s+(?:Table|Fig\.?|Figure)\s*\d+(?:\.\d+)?", "", t)
    t = re.sub(r"\b(?:Worked\s+)?(?:Examples?|Activit(?:y|ies)|Theorem|Exercise|Table|Fig\.?|Figure|Chapter)\s+\d+(?:\.\d+)?"
               r"(?:\s*(?:,\s*and|and|&|,|to)\s*\d+(?:\.\d+)?)*(?:\s*Q\d+)?(?:\s*\([ivx]+\))?(?:\s+for\s+Exercise\s+\d+\.\d+)?\s*[—:–-]*\s*", "", t)
    t = re.sub(r"\b(?:NCERT|textbook)(?:'s)?\b[\s:—–-]*", "", t, flags=re.I)
    t = re.sub(r"\s{2,}", " ", t).strip(" —:–-")
    t = re.sub(r"(?:\s+(?:of|for|from|and|in|with))+$", "", t)
    return t[:1].upper() + t[1:] if t else t


# ---------------------------------------------------------------- parse md
def parse_md(md):
    lines = open(md, encoding="utf8").read().split("\n")
    modules, topic, concept = [], None, None
    i = 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("# Appendix A"):
            break
        m = re.match(r"# (M\d) · (.+)", ln)
        if m:
            modules.append({"id": m.group(1), "name": m.group(2).strip(), "topics": []})
            i += 1
            continue
        m = re.match(r"## T(\d+) · (.+)", ln)
        if m:
            raw = m.group(2).strip()
            name = re.sub(r"\s*\(hook\)\s*$", "", raw).strip()
            topic = {"n": int(m.group(1)), "name": name, "concepts": [], "hook": raw != name}
            modules[-1]["topics"].append(topic)
            concept = None
            i += 1
            continue
        m = re.match(r"### C(\d+) · (.+)", ln)
        if m:
            concept = {"n": int(m.group(1)), "name": m.group(2).strip(), "meta": [], "blocks": [], "quote": []}
            topic["concepts"].append(concept)
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith((">", "[")):
                concept["meta"].append(lines[i])
                i += 1
            continue
        if concept is not None and ln.startswith("["):
            tag = re.match(r"\[([^\]]+)\]", ln).group(1)
            i += 1
            q = []
            while i < len(lines) and lines[i].startswith(">"):
                q.append(lines[i][1:].lstrip(" ") if lines[i] != ">" else "")
                i += 1
            concept["blocks"].append({"tag": tag, "lines": q})
            continue
        if concept is not None and ln.startswith(">"):
            q = []
            while i < len(lines) and lines[i].startswith(">"):
                q.append(lines[i][1:].lstrip(" ") if lines[i] != ">" else "")
                i += 1
            concept["quote"] = q
            continue
        i += 1
    return modules


def appendix(md, start, end):
    txt = open(md, encoding="utf8").read()
    return txt.split(start)[1].split(end)[0] if end else txt.split(start)[1]


def objectives_table(md):
    rows = []
    for ln in appendix(md, "# Appendix A", "# Appendix B").split("\n"):
        m = re.match(r"\| (O\d+) \| (\w+) \| (.+) \| (.+) \|$", ln)
        if m:
            text = re.sub(r"\s*`\[authored\]`", "", m.group(3)).strip()
            rows.append({"id": m.group(1), "bloom": m.group(2), "text": text, "legacy": m.group(4).strip()})
    return rows


def topic_map_from_md(md, modules):
    """old topic number -> new topic number, from the first C-number in each Appendix C row."""
    c_to_t = {c["n"]: t["n"] for m in modules for t in m["topics"] for c in t["concepts"]}
    out = {}
    for ln in appendix(md, "# Appendix C", None).split("\n"):
        m = re.match(r"\| T(\d+)\b[^|]*\| (.+) \|$", ln)
        if m:
            c = re.search(r"\bC(\d+)", m.group(2))
            if c:
                out[int(m.group(1))] = c_to_t[int(c.group(1))]
    return out


# ---------------------------------------------------------------- build
def main(n):
    cfg = CONFIG[n]
    folder = os.path.join(ROOT, f"std10_ch{n}")
    MD = os.path.join(folder, f"maths10_ch{n}_representative_lp.md")
    OLD = os.path.join(folder, f"learning_plan_std10_chap{n}_version1.json")
    OUT = os.path.join(folder, f"learning_plan_std10_chap{n}_version2.json")
    asset_base = ASSET_BASE.format(n=n)
    sols = SS.load(folder)
    bad = SS.validate(sols) if sols else []
    if bad:
        raise SystemExit("solutions.json has problems:\n  " + "\n  ".join(bad))
    sols_used = set()

    old = json.load(open(OLD, encoding="utf8"))
    modules = parse_md(MD)
    objs = objectives_table(MD)

    old_media, old_tools, old_topics, media_topic = {}, [], [], {}
    for m in old["modules"]:
        for sg in m["segments"]:
            for tp in sg["topics"]:
                old_topics.append(tp)
                for x in tp.get("media", []):
                    media_topic[x["id"]] = tp
                    if x["type"] in ("image", "video"):
                        old_media[x["id"]] = x
                    else:
                        old_tools.append(x)

    def find_old(tn, token):
        c = []
        for k in old_media:
            mm = re.search(r"\.T%d\.(.*)$" % tn, k)
            if mm and (mm.group(1) == token or mm.group(1).endswith("." + token)):
                c.append(k)
        assert len(c) == 1, (tn, token, c)
        return c[0]

    used_old = set()
    all_key_terms = []
    for tp in old_topics:
        for k in tp.get("key_terms", []):
            all_key_terms.append(k if isinstance(k, str) else k.get("term", ""))

    out_modules, concept_loc, new_media_index = [], {}, {}
    seg_n = 0
    ex_iter = iter(cfg["exercises"])
    theorem_n, last_try = 0, None
    theorems = {}
    for mod in modules:
        om = {"module_id": mod["id"], "module_name": mod["name"], "segments": []}
        out_modules.append(om)
        for tp in mod["topics"]:
            seg_n += 1
            tn = tp["n"]
            sid = f"{mod['id']}.S{seg_n}"
            tid = f"{sid}.T{tn}"
            tconcepts, tmedia = [], []
            is_q = tp["name"].startswith("Questions:")
            is_ex = tp["name"].startswith("Examples:")
            ex_no = next(ex_iter) if is_q else None
            for c in tp["concepts"]:
                cid = f"{tid}.C{c['n']}"
                meta = " ".join(c["meta"])
                kind_m = re.search(r"kind: ([a-z]+)", meta)
                kind = kind_m.group(1) if kind_m else "exercise"
                is_example = "worked example" in meta
                om_ = re.search(r"objectives: ([^`]+)`", meta)
                objective_ids = re.findall(r"O\d+", om_.group(1)) if om_ else []
                enrich = "is_enrichment: true" in meta or kind == "enrich"
                if enrich:
                    objective_ids = []
                media_txt = ""
                for ln in c["meta"]:
                    if "Media:" in ln:
                        media_txt = ln[ln.index("Media:"):]
                has_figure = "book's own" in media_txt and "figure" in media_txt
                # --- media
                refs = re.findall(r"old T(\d+) ([A-Z0-9.]+)", media_txt)
                cmedia, vcount, icount = [], 0, 0
                for tnn, token in refs:
                    oid = find_old(int(tnn), token)
                    assert oid not in used_old, oid
                    used_old.add(oid)
                    obj = json.loads(json.dumps(old_media[oid]))
                    if obj["type"] == "video":
                        vcount += 1
                        nid = f"{cid}.VID{vcount}"
                    else:
                        icount += 1
                        nid = f"{cid}.IMG{icount}"
                    obj["old_media_id"] = oid
                    obj["id"] = nid
                    obj["concept_id"] = cid
                    obj["home_concept_id"] = cid
                    obj["objective_id"] = objective_ids[0] if objective_ids else None
                    t0 = obj.get("title", "")
                    t1 = clean_title(t0)
                    if t1 != t0:
                        obj["old_title"] = t0
                        obj["title"] = t1
                    cmedia.append(obj)
                    new_media_index[nid] = oid
                spec_m = re.search(r'new image spec "([^"]+)"\s*[—-]\s*(.+)$', media_txt)
                if spec_m and not is_q:
                    icount += 1
                    nid = f"{cid}.IMG{icount}"
                    title_, desc_ = spec_m.group(1).strip(), spec_m.group(2).strip()
                    cmedia.append({
                        "id": nid, "type": "image", "title": title_, "labels": [], "subtype": "geometric_diagram",
                        "image_url": "", "description": desc_, "concept_id": cid, "home_concept_id": cid,
                        "objective_id": objective_ids[0] if objective_ids else None,
                        "image_category": "concept_illustration", "build_status": "placeholder",
                        "planned_url": f"{asset_base}/image_v3/{nid}.png", "aspect_ratio": "16:9",
                        "image_dimensions": "1456x816",
                        "context": f"Illustration for {c['name']}. PLACEHOLDER: specified, not generated yet.",
                        "source_image": {"note": "Authored for this plan; no source asset supplied."},
                        "generation_prompt": "MATHEMATICAL IMAGE REQUIREMENT\nTeaching purpose: " + title_ + "\n" + desc_,
                        "teaching_notes": "Show with the concept text. Do not reveal any answer the student is meant to find.",
                        "negative_prompt": "text overlay, watermark, blurry, distorted, incorrect proportions",
                        "accuracy_constraints": desc_,
                    })
                    new_media_index[nid] = "NEW"
                # --- content blocks
                content = []

                def add(kind_, text, **kw):
                    b = {"text": text, "type": "paragraph", "block_kind": kind_}
                    b.update(kw)
                    b["publication_text"] = text
                    content.append(b)

                theorem_id = None
                if kind == "try":
                    theorem_n += 1
                    theorem_id = f"TH{theorem_n}"
                    last_try = theorem_id
                    theorems[theorem_id] = c["name"]
                elif kind == "prove":
                    theorem_id = last_try
                if is_q:
                    q = list(c["quote"])
                    hint = ""
                    for j, ql in enumerate(q):
                        if ql.startswith("**Hint"):
                            hint = clean(re.sub(r"^\*\*Hint[^*]*\*\*\s*", "", ql))
                            q = q[:j]
                            break
                    qtext = "\n".join(clean(x) for x in q).strip()
                    label = c["name"]
                    nm = re.match(r"^(.+), Q(\d+)(?: \(([ivxlc]+)\))?$", label)
                    assert nm, f"question concept name not '<set>, Qn[ (x)]': {label}"
                    ex_id = f"{ex_no}.Q{nm.group(2)}" + (f".{nm.group(3)}" if nm.group(3) else "")
                    nid = f"{cid}.IMG1"
                    spec = {
                        "id": nid, "type": "image", "title": label, "labels": [],
                        "context": f"Question card for {label}, shown before the student attempts it. PLACEHOLDER: specified, not generated yet.",
                        "subtype": "question_card", "image_url": "",
                        "concept_id": cid, "image_role": "question",
                        "description": ("The figure supplied with the question, and nothing else: no hint, no working, no answer."
                                        if has_figure else
                                        f"A plain white card holding only the statement of {label}: no hint, no working, no answer."),
                        "planned_url": f"{asset_base}/image_v3/{nid}.png",
                        "serves_item": ex_id, "aspect_ratio": "16:9", "build_status": "placeholder",
                        "source_image": {"note": "Authored for this plan; no source asset supplied."},
                        "image_category": "question",
                        "teaching_notes": "Shown before the attempt. Let the student try first; hint and solution open afterwards.",
                        "home_concept_id": cid, "image_dimensions": "1456x816",
                        "source_image_key": f"c10.{ex_id}",
                        "generation_prompt": ("MATHEMATICAL IMAGE REQUIREMENT\nTeaching purpose: the question card for "
                                              f"{label}: " + ("only the figure that comes with the question." if has_figure
                                                              else "the statement only.") +
                                              "\nNo hints, no working, no answer."),
                        "related_concept_ids": [],
                        "accuracy_constraints": ("Only the figure that comes with the question; no extra text"
                                                 if has_figure else
                                                 "One text block holding the question statement exactly as listed\nno figure; the statement only"),
                        "instructions_for_student": label,
                    }
                    cmedia.append(spec)
                    new_media_index[nid] = "NEW"
                    sol = sols.get(ex_id)
                    if sol:
                        sols_used.add(ex_id)
                        sol_steps, sol_answer = SS.plan_fields(sol)
                    add("exercise_question", f"{label}: {qtext}", hint=hint,
                        steps=sol_steps if sol else [], answer=sol_answer if sol else "",
                        starred=False, question=qtext, item_kind="exercise", has_figure=has_figure,
                        ncert_refs=[ex_id], exercise_id=ex_id, attempt_first=True,
                        image_media_id=nid, question_label=label,
                        solution_status="authored" if sol else "to_author")
                    cref = [ex_id]
                else:
                    cref = []
                    for b in c["blocks"]:
                        tag = b["tag"]
                        if tag.startswith(REVIEW_ONLY_TAGS):
                            continue
                        body = "\n".join(clean(x) for x in b["lines"]).strip()
                        if tag.startswith("textbook_text"):
                            add("textbook_text", body, lines=[p for p in body.split("\n") if p.strip()])
                        elif tag.startswith("theorem_statement"):
                            add("theorem_statement", body, statement=body, theorem_id=theorem_id)
                        elif tag.startswith("predict"):
                            add("predict", body, theorem_id=theorem_id)
                        elif tag.startswith("enrichment"):
                            add("enrichment", body)
                        elif tag.startswith("method_statement"):
                            add("method_statement", body, lines=[p for p in body.split("\n") if p.strip()])
                        elif tag.startswith("teach"):
                            add("teach", body)
                        elif tag.startswith("question"):
                            add("example_question", body, question=body, attempt_first=True)
                        elif tag.startswith("worked solution"):
                            add("example_solution", body, steps=[p for p in body.split("\n") if p.strip()])
                        elif tag.startswith("remark"):
                            add("remark", body)
                        elif tag.startswith("summary_points"):
                            head = [p for p in body.split("\n") if p and not re.match(r"\d+\. ", p)]
                            pts = [re.sub(r"^\d+\. ", "", p) for p in body.split("\n") if re.match(r"\d+\. ", p)]
                            add("summary_points", body, points=pts, lead=head[0] if head else "")
                        else:
                            raise ValueError(f"{cid}: unknown tag [{tag}]")
                    if c["n"] in cfg.get("examples", {}):
                        cref = [cfg.get("examples", {})[c["n"]]]
                    if c["n"] in cfg.get("notes", {}):
                        cref = [cfg.get("notes", {})[c["n"]]]
                if cmedia:
                    for x in cmedia:
                        if x["type"] == "video":
                            x["video_role"] = ("exercise" if is_q else "hook" if kind == "hook"
                                               else "proof" if kind == "prove" else "example" if is_example
                                               else "summary" if kind == "summary" else "teaching")
                            x["interactive"] = x.get("interactive", False)
                text_all = " ".join(b["text"] for b in content)
                kts = []
                for k in all_key_terms:
                    if k and k.lower() in text_all.lower() and k not in kts:
                        kts.append(k)
                ck = "example" if is_example else "question" if is_q else kind
                ckind = "exercise" if (is_example or is_q) else kind
                src_media = "video" if any(x["type"] == "video" for x in cmedia) else "image" if cmedia else "none"
                cobj = {
                    "content": content, "key_terms": kts[:6], "media_ids": [x["id"] for x in cmedia],
                    "media_key": f"c10.{cid}", "concept_id": cid, "ncert_refs": cref,
                    "theorem_id": theorem_id, "concept_kind": ckind, "concept_name": c["name"],
                    "objective_id": objective_ids[0] if objective_ids else None,
                    "question_ids": cref if is_q else [], "source_media": src_media,
                    "is_enrichment": enrich, "objective_ids": objective_ids,
                    "enrichment_type": "enrichment" if enrich else "content",
                    "estimated_minutes": MINUTES[ck], "mixed_objective_ids": [], "recap_objective_ids": [],
                    "source_segment_role": ROLE[ckind], "starred_question_ids": [],
                }
                if is_example:
                    cobj["example_ref"] = cref[0] if cref else None
                if is_q:
                    cobj["image_media_id"] = f"{cid}.IMG1"
                tconcepts.append(cobj)
                tmedia.extend(cmedia)
                concept_loc[cid] = cobj
            om["segments"].append({"_n": tn, "_sid": sid, "tid": tid, "name": tp["name"], "concepts": tconcepts,
                                   "media": tmedia, "mod": mod["id"], "hook": tp["hook"], "is_q": is_q,
                                   "is_ex": is_ex})

    # ---- objectives (anchor / home topic)
    obj_out = []
    seen_legacy = set()  # the importer keys objectives on legacy_id, so repeats crash it (HTTP 500)
    for o in objs:
        if o["legacy"] in seen_legacy:
            o["legacy"] = f"{o['legacy']} {o['id']}"
        seen_legacy.add(o["legacy"])
        anchors = [c["concept_id"] for c in concept_loc.values() if o["id"] in c["objective_ids"]]
        assert anchors, f"objective {o['id']} has no anchor concept"
        home = ".".join(anchors[0].split(".")[:3])
        modid = anchors[0].split(".")[0]
        modname = next(m["module_name"] for m in out_modules if m["module_id"] == modid)
        obj_out.append({"anchor": anchors, "status": "taught", "strand": modid,
                        "legacy_id": o["legacy"], "bloom_level": o["bloom"], "strand_name": modname,
                        "objective_id": o["id"], "home_topic_id": home, "objective_text": o["text"],
                        "objective_level": "concept"})
    used_objs = {o for c in concept_loc.values() for o in c["objective_ids"]}
    assert used_objs <= {o["id"] for o in objs}, used_objs - {o["id"] for o in objs}

    # ---- carried old topics and id mapping
    carried = [{k: v for k, v in tp.items() if k not in ("media", "2d_tool")} for tp in old_topics]
    topic_tid = {t["_n"]: t["tid"] for m in out_modules for t in m["segments"]}
    tmap = cfg.get("topic_map") or topic_map_from_md(MD, modules)
    id_map = {"topics": {}, "media": new_media_index, "concepts_from_old_topic": {}}
    for tp in old_topics:
        k = int(re.search(r"\.T(\d+)$", tp["topic_id"]).group(1))
        id_map["topics"][tp["topic_id"]] = topic_tid[tmap[k]]
    id_map["media_old_to_new"] = {v: k for k, v in new_media_index.items() if v != "NEW"}

    # ---- assemble final modules/segments/topics
    final_modules, all_video_cov, total_min = [], [], 0
    for m in out_modules:
        fm = {"summary": "", "segments": [], "module_id": m["module_id"], "module_name": m["module_name"],
              "brief_summary": "", "detailed_summary": "", "important_points": []}
        names = []
        for t in m["segments"]:
            cs = t["concepts"]
            oids = []
            for c in cs:
                for o in c["objective_ids"]:
                    if o not in oids:
                        oids.append(o)
            mins = sum(c["estimated_minutes"] for c in cs)
            total_min += mins
            cat = ("introduction" if t["hook"] else "practice" if t["is_q"] else "examples" if t["is_ex"]
                   else "summary" if t["name"] == "Chapter Summary" else "instruction")
            bullets = [c["concept_name"] for c in cs]
            words = sum(len(b["text"].split()) for c in cs for b in c["content"])
            has_v = any(x["type"] == "video" for x in t["media"])
            has_i = any(x["type"] == "image" for x in t["media"])
            prev = topic_tid.get(t["_n"] - 1)
            sections = sorted({".".join(r.split(".")[:2]) for c in cs for r in c["ncert_refs"]
                               if re.match(r"^\d+\.\d+\.Q", r)})
            tp_obj = {
                "media": t["media"], "summary": "; ".join(bullets)[:200], "concepts": cs, "topic_id": t["tid"],
                "key_terms": sorted({k for c in cs for k in c["key_terms"]}),
                "depends_on": [prev] if prev else [], "difficulty": "", "topic_name": t["name"],
                "topic_type": "framing" if cat == "introduction" else "instructional",
                "word_count": {"original": words},
                "source_type": "framing" if cat == "introduction" else "instructional",
                "brief_summary": "; ".join(bullets)[:300], "objective_ids": oids,
                "ncert_sections": sections,
                "original_chunk": "; ".join(bullets), "topic_category": cat, "concept_bullets": bullets,
                "topic_objective": None, "detailed_summary": "; ".join(bullets), "important_points": [],
                "recall_questions": [], "estimated_minutes": mins, "publication_chunk": "; ".join(bullets),
                "estimated_exchanges": 0,
                "learning_objectives": [o for o in obj_out if o["objective_id"] in oids],
                "source_content_flow": ("Exercise questions; attempt first, then the solution"
                                        if cat == "practice" else "Concepts in order, each with its own media"),
                "primary_content_type": "video" if has_v else ("image" if has_i else "paragraph"),
                "tertiary_content_type": None,
                "secondary_content_type": "image" if (has_v and has_i) else None,
                "available_content_types": [x for x in ["video" if has_v else None, "image" if has_i else None,
                                                        "paragraph"] if x],
            }
            seg = {"topics": [tp_obj], "summary": tp_obj["summary"], "segment_id": t["_sid"],
                   "segment_name": t["name"], "brief_summary": tp_obj["brief_summary"], "detailed_summary": "",
                   "important_points": [], "recall_questions": [], "segment_objective_ids": oids}
            fm["segments"].append(seg)
            names.append(t["name"])
            for c in cs:
                for x in t["media"]:
                    if x["type"] == "video" and x["concept_id"] == c["concept_id"]:
                        kind = ("derivation" if c["concept_kind"] == "prove" else
                                "example" if c.get("example_ref") else "concept")
                        all_video_cov.append({"kind": kind, "item_id": c.get("example_ref") or c["concept_id"],
                                              "video_id": x["id"], "book_item": c["concept_name"]})
        fm["summary"] = fm["brief_summary"] = fm["detailed_summary"] = "; ".join(names)
        final_modules.append(fm)

    # ---- plan-level maps
    s2o = {}
    for o in obj_out:
        k = re.sub(r"[^A-Za-z0-9._]+", "_", o["legacy_id"]).strip("_")
        if k in s2o:
            k = f"{k}_{o['objective_id']}"
        s2o[k] = o["objective_id"]

    held = {"tools": [], "question_videos": [], "other_held": []}
    for x in old_tools:
        held["tools"].append({"old_media_id": x["id"], "title": x.get("title"), "reason": "no tools in Class 10",
                              "object": x})
    for oid, x in old_media.items():
        if oid in used_old:
            continue
        tp_name = media_topic[oid].get("topic_name", "")
        if x["type"] == "video" and re.search(r"exercise|question|practic", tp_name + " " + x.get("title", ""), re.I):
            held["question_videos"].append({"old_media_id": oid, "title": x.get("title"),
                                            "reason": "no question videos for Class 10 for now", "object": x})
        else:
            held["other_held"].append({"old_media_id": oid, "title": x.get("title"),
                                       "reason": "held in the representative plan (Appendix B of the md): gives away the answer, "
                                                 "or its concept was dropped",
                                       "object": x})

    q_count = sum(1 for c in concept_loc.values() if c["concept_kind"] == "exercise" and not c.get("example_ref")
                  and c["content"] and c["content"][0]["block_kind"] == "exercise_question")
    n_concepts = len(concept_loc)
    n_images = sum(1 for m in final_modules for s in m["segments"] for t in s["topics"]
                   for x in t["media"] if x["type"] == "image")
    plan = {
        "board": "CBSE", "grade": 10, "level": "", "phase": 2, "modules": final_modules,
        "plan_id": f"cbse_eng_maths10_ch{n}_v{PLAN_VERSION}", "subject": "Mathematics", "version": PLAN_VERSION,
        "textbook": old["textbook"], "_activate": False, "medium_id": 1, "chapter_id": f"cbse_eng_maths10_ch{n}",
        "objectives": obj_out, "unit_title": old["unit_title"], "unit_number": old["unit_number"],
        "chapter_name": old["chapter_name"], "textbook_url": old["textbook_url"],
        "estimated_time": round(total_min / 60, 1), "publication_id": old["publication_id"],
        "subject_ref_id": old["subject_ref_id"], "video_coverage": all_video_cov,
        "source_metadata": {
            "book": f"Mathematics, Class 10, Chapter {n} ({old['chapter_name']})", "class": "Class 10",
            "tools": {}, "hierarchy": "module > segment > topic > concepts (one objective each)",
            "design": f"Restructured from {old['plan_id']} to the Class 9 concept/block shape "
                      f"(docs/04_class9_10_variant.md). Built from maths10_ch{n}_representative_lp.md.",
            "theorems": theorems,
            "media_note": "Existing videos and images re-homed by concept (old_media_id on each). "
                          "Question concepts carry one hint-free image spec each (placeholder) and no video. "
                          "No tools. Held assets are listed under held_assets, nothing deleted.",
            "source_plan": old["plan_id"],
            "values_policy": "Textbook values are allowed everywhere.",
            "held_assets": held,
            "id_mapping": id_map,
            "carried_over_topics": carried,
            "summary_stats": {"modules": len(final_modules), "topics": sum(len(m["segments"]) for m in final_modules),
                              "concepts": n_concepts, "objectives": len(obj_out), "question_concepts": q_count,
                              "videos": len(all_video_cov), "images": n_images},
        },
        "chapter_master_id": old["chapter_master_id"], "strand_to_objective_map": s2o,
    }
    if sols:
        unused = sorted(set(sols) - sols_used)
        if unused:
            print("WARNING: solutions.json entries that match no question concept:", unused[:8])
        errs, warns = SC.check(folder)
        for w in warns:
            print("  ~ solutions:", w)
        if errs:
            raise SystemExit("%d solution problem(s):\n  - %s" % (len(errs), "\n  - ".join(errs)))
        key_dir = SA.key_dir_for({"asset_base_template": ASSET_BASE.replace("{n}", "{chapter_no}"),
                                  "grade": 10, "chapter_no": n})
        problems = SA.attach(plan, folder, key_dir)
        if problems:
            raise SystemExit("%d solution attach problem(s):\n  - %s" % (len(problems), "\n  - ".join(problems)))
        plan["source_metadata"]["media_note"] = plan["source_metadata"]["media_note"].replace(
            "Question concepts carry one hint-free image spec each (placeholder) and no video.",
            "Question concepts with a solution carry a question image and a solution image (Manim, see "
            "render_source); the others carry one hint-free image spec (placeholder). No question videos.")
    plan = json.loads(no_dashes(json.dumps(plan, ensure_ascii=False)))
    json.dump(plan, open(OUT, "w", encoding="utf8"), ensure_ascii=False, indent=1)
    print("wrote", OUT)
    print(plan["source_metadata"]["summary_stats"], "est hours", plan["estimated_time"],
          "| held:", {k: len(v) for k, v in held.items()})


if __name__ == "__main__":
    main(int(sys.argv[1]))
