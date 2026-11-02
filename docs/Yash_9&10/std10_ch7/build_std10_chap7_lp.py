"""Build the Class 10 Ch7 concept-level learning plan from the representative plan (md).

Inputs (same folder):
  maths10_ch7_representative_lp.md          structure + concept content
  learning_plan_std10_chap7_version1.json   old plan: media objects, topic fields, plan header
Output:
  learning_plan_std10_chap7_version2.json
Run: python -I -X utf8 build_std10_chap7_lp.py
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(HERE, "maths10_ch7_representative_lp.md")
OLD = os.path.join(HERE, "learning_plan_std10_chap7_version1.json")
OUT = os.path.join(HERE, "learning_plan_std10_chap7_version2.json")

ASSET_BASE = "https://media.singularity-learn.com/learning_plan_assets/V2/cbse/cbse/english/class_10/mathematics/ch_7"

# group-local question -> book question (Ex 7.1 / Ex 7.2), in the order the md lists them
BOOK_Q = {
    "T5": ["7.1.Q1", "7.1.Q2", "7.1.Q8", "7.1.Q3", "7.1.Q4", "7.1.Q5", "7.1.Q6", "7.1.Q7", "7.1.Q9", "7.1.Q10"],
    "T8": ["7.2.Q1", "7.2.Q8", "7.2.Q4", "7.2.Q5", "7.2.Q2", "7.2.Q9", "7.2.Q3", "7.2.Q7", "7.2.Q6", "7.2.Q10"],
}
EXAMPLE_REF = {7: "7.ex1", 8: "7.ex2", 9: "7.ex3", 10: "7.ex4", 11: "7.ex5",
               26: "7.ex6", 27: "7.ex7", 28: "7.ex8", 29: "7.ex9", 30: "7.ex10"}
FORMULA = {4: "F1", 5: "F1", 22: "F2", 23: "F2"}
OLD_TO_NEW_TOPIC = {1: 2, 2: 1, 3: 3, 4: 4, 5: 4, 6: 5, 7: 6, 8: 7, 9: 6, 10: 7, 11: 7, 12: 8, 13: 9}
MINUTES = {"hook": 5, "teach": 8, "try": 6, "prove": 10, "example": 8, "question": 6, "enrich": 3, "summary": 8}
ROLE = {"hook": "hook", "teach": "teaching", "try": "try_it", "prove": "proof", "exercise": "practice",
        "enrich": "enrichment", "summary": "summary"}


def clean(s):
    return s.replace("**", "").strip()


# ---------------------------------------------------------------- parse md
def parse_md():
    lines = open(MD, encoding="utf8").read().split("\n")
    modules, topic, concept, group = [], None, None, None
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
            name = re.sub(r"\s*\(hook\)\s*$", "", m.group(2)).strip()
            topic = {"n": int(m.group(1)), "name": name, "concepts": [], "groups": {}}
            modules[-1]["topics"].append(topic)
            concept, group = None, None
            i += 1
            continue
        m = re.match(r'\*\*Group "(.+?)"\*\* · objective \*\*(O\d+)\*\* \((\w+)\): (.+)', ln)
        if m:
            group = m.group(1)
            topic["groups"][group] = {"objective": m.group(2), "bloom": m.group(3), "text": m.group(4)}
            i += 1
            continue
        m = re.match(r'\*\*Group "(.+?)"\*\* · objective \*\*(O\d+)\*\*', ln)
        if m:
            group = m.group(1)
            topic["groups"][group] = {"objective": m.group(2), "bloom": None, "text": None}
            i += 1
            continue
        m = re.match(r"### C(\d+) · (.+)", ln)
        if m:
            concept = {"n": int(m.group(1)), "name": m.group(2).strip(), "meta": [], "blocks": [],
                       "quote": [], "media": "", "group": group}
            topic["concepts"].append(concept)
            i += 1
            # meta lines until first blank
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


def objectives_table():
    txt = open(MD, encoding="utf8").read().split("# Appendix A")[1].split("# Appendix B")[0]
    rows = []
    for ln in txt.split("\n"):
        m = re.match(r"\| (O\d+) \| (\w+) \| (.+) \| (.+) \|$", ln)
        if m:
            text = re.sub(r"\s*`\[authored\]`", "", m.group(3)).strip()
            rows.append({"id": m.group(1), "bloom": m.group(2), "text": text, "legacy": m.group(4).strip()})
    return rows


# ---------------------------------------------------------------- build
def main():
    old = json.load(open(OLD, encoding="utf8"))
    modules = parse_md()
    objs = objectives_table()
    obj_by_id = {o["id"]: o for o in objs}

    # old media index
    old_media = {}
    old_tools = []
    old_topics = []
    for m in old["modules"]:
        for sg in m["segments"]:
            for tp in sg["topics"]:
                old_topics.append(tp)
                for x in tp.get("media", []):
                    if x["type"] == "2d_tool":
                        old_tools.append(x)
                    else:
                        old_media[x["id"]] = x
                for x in (tp.get("2d_tool") or []):
                    pass

    def find_old(tn, token):
        c = [k for k in old_media if re.search(r"\.T%d\.(.*)$" % tn, k)
             and (re.search(r"\.T%d\.(.*)$" % tn, k).group(1) == token
                  or re.search(r"\.T%d\.(.*)$" % tn, k).group(1).endswith("." + token))]
        assert len(c) == 1, (tn, token, c)
        return c[0]

    used_old = set()
    all_key_terms = []
    for tp in old_topics:
        for k in tp.get("key_terms", []):
            all_key_terms.append(k if isinstance(k, str) else k.get("term", ""))

    out_modules, concept_loc = [], {}
    new_media_index = {}
    seg_n = 0
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
            qi = 0
            for c in tp["concepts"]:
                cid = f"{tid}.C{c['n']}"
                meta = " ".join(c["meta"])
                kind_m = re.search(r"kind: ([a-z]+)", meta)
                kind = kind_m.group(1) if kind_m else "exercise"
                is_example = "worked example" in meta
                objective_ids = re.findall(r"O\d+", re.search(r"objectives: ([^`]+)`", meta).group(1)) \
                    if re.search(r"objectives: ([^`]+)`", meta) else []
                enrich = "is_enrichment: true" in meta or kind == "enrich"
                if enrich:
                    objective_ids = []
                media_txt = ""
                for ln in c["meta"]:
                    if "Media:" in ln:
                        media_txt = ln[ln.index("Media:"):]
                has_figure = "book's own figure" in media_txt
                # --- media
                refs = re.findall(r"old T(\d+) ([A-Z0-9.]+)", media_txt)
                cmedia, vcount, icount = [], 0, 0
                video_id = image_id = None
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
                    t1 = re.sub(r"\s*\(Example \d+\)", "", t0)
                    t1 = re.sub(r"^Exercise 7\.\d (Reference Card)", r"", t1).replace(" for Exercise 7.2", "")
                    t1 = t1.replace("Chapter 7 ", "")
                    if t1 != t0:
                        obj["old_title"] = t0
                        obj["title"] = t1
                    cmedia.append(obj)
                    new_media_index[nid] = oid
                # --- content blocks
                content = []

                def add(kind_, text, **kw):
                    b = {"text": text, "type": "paragraph", "block_kind": kind_}
                    b.update(kw)
                    b["publication_text"] = text
                    content.append(b)

                qtext = None
                if is_q:
                    qi += 1
                    q = list(c["quote"])
                    hint = ""
                    for j, ql in enumerate(q):
                        if ql.startswith("**Hint"):
                            hint = clean(re.sub(r"^\*\*Hint[^*]*\*\*\s*", "", ql))
                            q = q[:j]
                            break
                    qtext = "\n".join(clean(x) for x in q).strip()
                    label = c["name"]
                    ex_id = BOOK_Q[f"T{tn}"][int(re.search(r"Q(\d+)$", label).group(1)) - 1 + 0] \
                        if False else None
                    k = int(re.search(r"Q(\d+)$", label).group(1))
                    gi = [cc["group"] for cc in tp["concepts"]].index(c["group"])
                    ex_id = BOOK_Q[f"T{tn}"][tp["concepts"].index(c)]
                    figure = has_figure
                    nid = f"{cid}.IMG1"
                    spec = {
                        "id": nid, "type": "image", "title": label,
                        "labels": [],
                        "context": f"Question card for {label}, shown before the student attempts it. PLACEHOLDER: specified, not generated yet.",
                        "subtype": "question_card", "image_url": "",
                        "concept_id": cid, "image_role": "question",
                        "description": ("The figure supplied with the question, and nothing else: no hint, no working, no answer."
                                        if figure else
                                        f"A plain white card holding only the statement of {label}: no hint, no working, no answer."),
                        "planned_url": f"{ASSET_BASE}/image_v3/{nid}.png",
                        "serves_item": ex_id, "aspect_ratio": "16:9", "build_status": "placeholder",
                        "source_image": {"note": "Authored for this plan; no source asset supplied."},
                        "image_category": "question",
                        "teaching_notes": "Shown before the attempt. Let the student try first; hint and solution open afterwards.",
                        "home_concept_id": cid, "image_dimensions": "1456x816",
                        "source_image_key": f"c10.{ex_id}",
                        "generation_prompt": ("MATHEMATICAL IMAGE REQUIREMENT\nTeaching purpose: the question card for "
                                              f"{label}: " + ("only the figure that comes with the question." if figure
                                                              else "the statement only.") +
                                              "\nNo hints, no working, no answer."),
                        "related_concept_ids": [],
                        "accuracy_constraints": ("Only the figure that comes with the question; no extra text"
                                                 if figure else
                                                 "One text block holding the question statement exactly as listed\nno figure; the statement only"),
                        "instructions_for_student": label,
                    }
                    cmedia.append(spec)
                    new_media_index[nid] = "NEW"
                    add("exercise_question", f"{label}: {qtext}", hint=hint, steps=[], answer="",
                        starred=False, question=qtext, item_kind="exercise", has_figure=figure,
                        ncert_refs=[ex_id], exercise_id=ex_id, attempt_first=True,
                        image_media_id=nid, question_label=label, solution_status="to_author")
                    cref = [ex_id]
                else:
                    cref = []
                    for b in c["blocks"]:
                        tag = b["tag"]
                        body = "\n".join(clean(x) for x in b["lines"]).strip()
                        if tag.startswith("textbook_text"):
                            paras = [p for p in body.split("\n") if p.strip()]
                            add("textbook_text", body, lines=paras)
                        elif tag.startswith("theorem_statement"):
                            add("theorem_statement", body, statement=body, theorem_id=FORMULA.get(c["n"]))
                        elif tag.startswith("predict"):
                            add("predict", body, theorem_id=FORMULA.get(c["n"]))
                        elif tag.startswith("enrichment"):
                            add("enrichment", body)
                        elif tag.startswith("question"):
                            add("example_question", body, question=body, attempt_first=True)
                        elif tag.startswith("worked solution"):
                            steps = [p for p in body.split("\n") if p.strip()]
                            add("example_solution", body, steps=steps)
                        elif tag.startswith("remark"):
                            add("remark", body)
                        elif tag.startswith("summary_points"):
                            head = [p for p in body.split("\n") if p and not re.match(r"\d+\. ", p)]
                            pts = [re.sub(r"^\d+\. ", "", p) for p in body.split("\n") if re.match(r"\d+\. ", p)]
                            add("summary_points", body, points=pts, lead=head[0] if head else "")
                        else:
                            raise ValueError(tag)
                    if c["n"] in EXAMPLE_REF:
                        cref = [EXAMPLE_REF[c["n"]]]
                    if cid.endswith(".C42"):
                        cref = ["7.note_external_division"]
                if cmedia:
                    video_id = next((x["id"] for x in cmedia if x["type"] == "video"), None)
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
                ck = ("example" if is_example else "question" if is_q else kind)
                ckind = "exercise" if (is_example or is_q) else kind
                src_media = "video" if any(x["type"] == "video" for x in cmedia) else \
                    "image" if cmedia else "none"
                cobj = {
                    "content": content, "key_terms": kts[:6], "media_ids": [x["id"] for x in cmedia],
                    "media_key": f"c10.{cid}", "concept_id": cid, "ncert_refs": cref,
                    "theorem_id": FORMULA.get(c["n"]), "concept_kind": ckind, "concept_name": c["name"],
                    "objective_id": objective_ids[0] if objective_ids else None,
                    "question_ids": cref if is_q else [], "source_media": src_media,
                    "is_enrichment": enrich, "objective_ids": objective_ids,
                    "enrichment_type": "enrichment" if enrich else "content",
                    "estimated_minutes": MINUTES[ck], "mixed_objective_ids": [], "recap_objective_ids": [],
                    "source_segment_role": ROLE[ckind], "starred_question_ids": [],
                }
                if is_example:
                    cobj["example_ref"] = cref[0]
                if is_q:
                    cobj["group"] = c["group"]
                    cobj["image_media_id"] = f"{cid}.IMG1"
                tconcepts.append(cobj)
                tmedia.extend(cmedia)
                concept_loc[cid] = cobj
            out_tp = {"_n": tn, "_sid": sid, "tid": tid, "name": tp["name"], "concepts": tconcepts,
                      "media": tmedia, "groups": tp["groups"], "mod": mod["id"]}
            om["segments"].append(out_tp)

    # ---- objectives (anchor / home topic)
    obj_out = []
    for o in objs:
        anchors = [c["concept_id"] for c in concept_loc.values() if o["id"] in c["objective_ids"]]
        assert anchors, o["id"]
        home = ".".join(anchors[0].split(".")[:3])
        modid = anchors[0].split(".")[0]
        modname = next(m["module_name"] for m in out_modules if m["module_id"] == modid)
        obj_out.append({"anchor": anchors, "status": "taught", "strand": modid,
                        "legacy_id": o["legacy"], "bloom_level": o["bloom"], "strand_name": modname,
                        "objective_id": o["id"], "home_topic_id": home, "objective_text": o["text"],
                        "objective_level": "concept"})

    # ---- carried old topics
    carried = []
    for tp in old_topics:
        d = {k: v for k, v in tp.items() if k not in ("media", "2d_tool")}
        carried.append(d)
    id_map = {"topics": {}, "media": new_media_index, "concepts_from_old_topic": {}}
    for tp in old_topics:
        n = int(re.search(r"\.T(\d+)$", tp["topic_id"]).group(1))
        id_map["topics"][tp["topic_id"]] = OLD_TO_NEW_TOPIC[n]
    topic_tid = {}
    for m in out_modules:
        for t in m["segments"]:
            topic_tid[t["_n"]] = t["tid"]
    id_map["topics"] = {k: topic_tid[v] for k, v in id_map["topics"].items()}
    # media old -> new
    id_map["media_old_to_new"] = {v: k for k, v in new_media_index.items() if v != "NEW"}

    # ---- assemble final modules/segments/topics
    final_modules = []
    all_video_cov = []
    total_min = 0
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
            kinds = {c["concept_kind"] for c in cs}
            cat = ("introduction" if t["name"].startswith("Finding") else "practice" if t["name"].startswith("Questions:")
                   else "examples" if t["name"].startswith("Examples:") else "summary" if t["name"] == "Chapter Summary"
                   else "instruction")
            bullets = [c["concept_name"] for c in cs]
            words = sum(len(b["text"].split()) for c in cs for b in c["content"])
            has_v = any(x["type"] == "video" for x in t["media"])
            has_i = any(x["type"] == "image" for x in t["media"])
            prev = topic_tid.get(t["_n"] - 1)
            tp_obj = {
                "media": t["media"], "summary": "; ".join(bullets)[:200], "concepts": cs, "topic_id": t["tid"],
                "key_terms": sorted({k for c in cs for k in c["key_terms"]}),
                "depends_on": [prev] if prev else [], "difficulty": "", "topic_name": t["name"],
                "topic_type": "framing" if cat == "introduction" else "instructional",
                "word_count": {"original": words},
                "source_type": "framing" if cat == "introduction" else "instructional",
                "brief_summary": "; ".join(bullets)[:300], "objective_ids": oids,
                "ncert_sections": sorted({r.split(".")[0] + "." + r.split(".")[1] for c in cs for r in c["ncert_refs"]
                                          if r.count(".") >= 1 and r[0].isdigit()}),
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
            if cat == "practice":
                tp_obj["question_groups"] = t["groups"]
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
        k = o["legacy_id"]
        if k in s2o:
            k = f"{k}#{o['objective_id']}"
        s2o[k] = o["objective_id"]

    held = {
        "tools": [{"old_media_id": x["id"], "title": x.get("title"), "reason": "no tools in this chapter",
                   "object": x} for x in old_tools],
        "question_videos": [],
    }
    for oid, x in old_media.items():
        if oid not in used_old:
            held["question_videos"].append({"old_media_id": oid, "title": x.get("title"),
                                            "reason": "no question videos for Class 10 for now", "object": x})

    n_concepts = sum(len(t["concepts"]) for m in final_modules for s in m["segments"] for t in s["topics"])
    plan = {
        "board": "CBSE", "grade": 10, "level": "", "phase": 2, "modules": final_modules,
        "plan_id": "maths10_ch7_concept_v1", "subject": "Mathematics", "version": 1,
        "textbook": old["textbook"], "_activate": False, "medium_id": 1, "chapter_id": old["chapter_id"],
        "objectives": obj_out, "unit_title": old["unit_title"], "unit_number": old["unit_number"],
        "chapter_name": old["chapter_name"], "textbook_url": old["textbook_url"],
        "estimated_time": round(total_min / 60, 1), "publication_id": old["publication_id"],
        "subject_ref_id": old["subject_ref_id"], "video_coverage": all_video_cov,
        "source_metadata": {
            "book": "Ganita Prakash, Class 10, Chapter 7 (Coordinate Geometry)", "class": "Class 10",
            "tools": {}, "hierarchy": "module > segment > topic > concepts (one objective each)",
            "design": "Restructured from maths10_ch7_standard_v1 to the Class 9 concept/block shape "
                      "(docs/04_class9_10_variant.md). Built from maths10_ch7_representative_lp.md.",
            "formulas": {"F1": "distance formula", "F2": "section formula"},
            "media_note": "Existing videos and images re-homed by concept (old_media_id on each). "
                          "Question concepts carry one hint-free image spec each (placeholder) and no video. "
                          "No tools. Held assets are listed under held_assets, nothing deleted.",
            "source_plan": old["plan_id"],
            "values_policy": "Textbook values are allowed everywhere.",
            "held_assets": held,
            "id_mapping": id_map,
            "carried_over_topics": carried,
            "summary_stats": {"modules": len(final_modules), "topics": sum(len(m["segments"]) for m in final_modules),
                              "concepts": n_concepts, "objectives": len(obj_out),
                              "question_concepts": sum(1 for c in concept_loc.values() if c.get("group")),
                              "videos": len(all_video_cov),
                              "images": sum(1 for m in final_modules for s in m["segments"] for t in s["topics"]
                                            for x in t["media"] if x["type"] == "image")},
        },
        "chapter_master_id": old["chapter_master_id"], "strand_to_objective_map": s2o,
    }
    json.dump(plan, open(OUT, "w", encoding="utf8"), ensure_ascii=False, indent=1)
    print("wrote", OUT)
    print(plan["source_metadata"]["summary_stats"], "est hours", plan["estimated_time"])


main()
