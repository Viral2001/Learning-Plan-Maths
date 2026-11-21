# -*- coding: utf-8 -*-
"""Build the V3 plan of Class 6 Ch 3 Number Play from the live V2 plan (v108) and the diagram map (prompt v3).

    python -I -X utf8 build_v3.py merge            merge map/out_A..D.json into map/diagram_map.json (and validate)
    python -I -X utf8 build_v3.py build --version N
                                                   build out/cbse_eng_maths6_ch3_V3_v<N>.json

What it does to a COPY of source/cbse_eng_maths6_ch3_v108.json (the live V2 plan; nothing is written to staging):
  1. chapter_id -> cbse_eng_maths6_ch3_V3, phase 3, version N, plan_id <chapter_id>_v<N>.
  2. deletes every image node with image_role "question" or "solution" (the old card placeholders, 149 of them), the
     ids in the concepts' media_ids and the image_media_id / solution_image_media_id(s) fields of the blocks.
  3. writes the map back the way diagram_identification_prompt v3 section 8B says:
       required            one image node (title "DIAGRAM · <label> question|solution figure"), id in the block's image
                           field and in the concept's media_ids, {{DIAGRAM:<id>}} token in the block's text fields
                           (solution token: first line of the steps, before step 1)
       none / optional     nothing (the old id stays removed); a teaching image is never linked from a block (v3)
  4. integrity checks, and a diff against v108 that must show nothing else changed.
Concept (teaching) images, videos, tools, text and objectives are untouched.
"""
import copy
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "source", "cbse_eng_maths6_ch3_v108.json")
MAP = os.path.join(HERE, "map", "diagram_map.json")
OUT = os.path.join(HERE, "out")
V3_ID = "cbse_eng_maths6_ch3_V3"
DIAGRAM = "DIAGRAM · "      # "DIAGRAM · "  (companion note: first token of the name, then space-middle dot-space)


def load(p):
    return json.load(open(p, encoding="utf-8"))


def ratio_dims(r, width=1920):
    a, b = [int(x) for x in r.split(":")]
    return "%dx%d" % (width, round(width * b / a))


# ------------------------------------------------------------------ merge
# two chunks gave the same figure different "none" codes; the merge picks the better one (both mean: no image)
RESOLVE = {"P12-cards-1": "none:TEXT_SUFFICIENT"}      # ten cards that hold text conditions, no numbers to draw


def merge():
    sys.path.insert(0, HERE)
    import validate_map
    items, notes, figs, conflicts = [], [], {}, []
    meta = None
    first = None
    for c in "ABCD":
        m = load(os.path.join(HERE, "map", "out_%s.json" % c))
        first = first or m
        meta = meta or m["meta"]
        items += m["items"]
        notes += ["[chunk %s] %s" % (c, n) for n in m["meta"].get("notes", [])]
        for f in m["figure_inventory"]:
            old = figs.get(f["fig_id"])
            if old and old["mapped_to"] != f["mapped_to"] and RESOLVE.get(f["fig_id"]) in (f["mapped_to"], old["mapped_to"]):
                old["mapped_to"] = RESOLVE[f["fig_id"]]
            elif old and old["mapped_to"] != f["mapped_to"]:
                conflicts.append("%s: chunk %s says %s, earlier chunk says %s" % (f["fig_id"], c, f["mapped_to"], old["mapped_to"]))
            figs.setdefault(f["fig_id"], f)
    if conflicts:
        print("\n".join("CONFLICT " + x for x in conflicts))
    import apply_supplied_map          # the user's placement map of 21 Nov 2026 (positions, C9, figures b/c/e/f)
    apply_supplied_map.apply(items, figs, notes)
    inv = load(os.path.join(HERE, "map", "inventory.json"))
    order = []
    for u in inv:
        if u["kind"] == "pair":
            order += [(u["question_concept"]["concept_id"], "question"), (u["answer_concept"]["concept_id"], "solution")]
        else:
            order.append((u["concept_id"], "worked_example"))
    pos = {k: i for i, k in enumerate(order)}
    items.sort(key=lambda it: pos[(it["lp_concept_id"], it["role"])])
    counts = {}
    for it in items:
        counts.setdefault(it["role"], {}).setdefault(it["decision"], 0)
        counts[it["role"]][it["decision"]] += 1
    meta = dict(meta)
    meta["prompt"] = "diagram_identification_prompt.md v3"
    meta["counts_by_role_and_decision"] = counts
    meta["notes"] = notes
    fl = sorted(figs.values(), key=lambda f: f["fig_id"])
    kinds = {"items": 0, "concept": 0, "none": 0}
    for f in fl:
        kinds["items" if f["mapped_to"].startswith("item:") else "concept" if f["mapped_to"].startswith("concept_image:") else "none"] += 1
    cov = {"inventory_figures": len(fl), "mapped_to_items": kinds["items"], "mapped_to_concept_images": kinds["concept"],
           "mapped_none": kinds["none"], "unmapped": 0,
           "new_media_ids_created": sorted(i["media_id"] for i in items if i["decision"] == "required"),
           "lp_ids_dropped": sorted({x for i in items if i["decision"] != "required" and i.get("media_id") for x in [i["media_id"]]})}
    json.dump({"meta": meta, "style_tokens": first["style_tokens"], "figure_inventory": fl, "coverage_report": cov, "items": items},
              open(MAP, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("merged", len(items), "items,", len(fl), "figures;", json.dumps(counts))
    return validate_map.main(MAP, "all") or (1 if conflicts else 0)


# ------------------------------------------------------------------ text helpers
def line_start(text, n):
    """Index of the start of the line that opens step n ("3. ..." or "$3$. ..."), or of "Answer:" when n is past the
    last step, or len(text)."""
    m = re.search(r"(?m)^\$?%d\$?\. " % n, text)
    if m:
        return m.start()
    m = re.search(r"(?m)^Answer:", text)
    return m.start() if m else len(text)


def insert_line(text, idx, tok):
    if idx >= len(text):
        return text.rstrip("\n") + "\n" + tok
    return text[:idx] + tok + "\n" + text[idx:]


def put_question_token(block, tok, worked):
    if worked:
        for k in ("text", "publication_text"):
            if isinstance(block.get(k), str):
                block[k] = insert_line(block[k], line_start(block[k], 1), tok)
    else:
        for k in ("question_tex", "text", "publication_text"):
            if isinstance(block.get(k), str):
                block[k] = block[k].rstrip("\n") + "\n" + tok


def put_solution_token(block, tok):
    """v3: the solution figure is ALWAYS the first line of the solution steps (steps_tex[0], and before step 1 in the
    combined text fields)."""
    block["steps_tex"][0] = tok + "\n" + block["steps_tex"][0]
    for k in ("text", "publication_text"):
        if isinstance(block.get(k), str):
            block[k] = insert_line(block[k], line_start(block[k], 1), tok)


# ------------------------------------------------------------------ nodes (section 8B of the v3 prompt)
def make_node(it, u, key_dir, concept):
    d = it["diagram"]
    mid, role = it["media_id"], it["role"]
    if role == "solution":
        label = u["answer_concept"]["item"].get("book_number") or u["answer_concept"]["name"]
        side, word = "solution", "solution"
        teach, instr = ("Show only after the student has attempted the question.",
                        "Compare this with your own working, step by step.")
        ctx = "Solution figure of %s." % label
    else:
        if role == "question":
            label = u["question_concept"]["item"].get("book_number") or u["question_concept"]["name"]
        else:
            label = u["item"].get("book_number") or u["concept_name"]
        side, word = "question", "question"
        teach, instr = "", "Look carefully at the figure."
        ctx = "Question figure of %s." % label
    spec = dict(d)
    spec["reason"], spec["reason_codes"] = it["reason"], it["reason_codes"]
    if it.get("needs_lp_text_sync"):
        spec["needs_lp_text_sync"] = True
    url = "%s/%s.png" % (key_dir, mid)
    return {
        "id": mid, "type": "image", "title": "%s%s %s figure" % (DIAGRAM, label, word),
        "concept_id": concept, "home_concept_id": concept, "image_role": side,
        "image_category": "concept", "subtype": "illustration", "build_status": "placeholder",
        "aspect_ratio": d["aspect_ratio"], "image_dimensions": ratio_dims(d["aspect_ratio"]),
        "image_url": url, "planned_url": url, "description": d["alt_text"], "labels": list(d["visible_text"]),
        "context": ctx + " PLACEHOLDER: specified, not generated yet.",
        "diagram_spec": spec, "generation_prompt": d["manim_description"],
        "negative_prompt": "; ".join(d["must_not_show"]), "accuracy_constraints": "\n".join(d["accuracy_checks"]),
        "render_source": {"engine": "manim", "scene": it.get("manim_scene"),
                          "code_url": "%s/code/%s.py" % (key_dir, mid), "style_url": "%s/code/_style.py" % key_dir},
        "instructions_for_student": instr, "teaching_notes": teach, "related_concept_ids": [], "source_image_key": "",
    }


# ------------------------------------------------------------------ build
def build(version):
    src = load(SRC)
    plan = copy.deepcopy(src)
    dm = load(MAP)
    inv = {}
    for u in load(os.path.join(HERE, "map", "inventory.json")):
        if u["kind"] == "pair":
            inv[(u["question_concept"]["concept_id"], "question")] = u
            inv[(u["answer_concept"]["concept_id"], "solution")] = u
        else:
            inv[(u["concept_id"], "worked_example")] = u
    items = {(i["lp_concept_id"], i["role"]): i for i in dm["items"]}
    req = {k: i for k, i in items.items() if i["decision"] == "required"}
    assert not [i for i in items.values() if i["lp_placeholder_action"] == "reuse_concept_image" or i.get("reuse_media_id")], "v3: no reuse"

    plan["chapter_id"], plan["phase"], plan["version"] = V3_ID, 3, version
    plan["plan_id"] = "%s_v%d" % (V3_ID, version)
    plan["_activate"] = True

    removed_ids, added_ids, tokens = set(), [], {}
    topics = {t["topic_id"]: t for m in plan["modules"] for s in m["segments"] for t in s["topics"]}
    concepts = {c["concept_id"]: (t, c) for t in topics.values() for c in t["concepts"]}

    # key dir of the new nodes: same bucket folder as the old cards, folder diagram_v1
    old = next(md for t in topics.values() for md in t["media"] if md.get("image_role"))
    key_dir = re.sub(r"/[^/]+/[^/]+$", "", old["planned_url"]) + "/diagram_v1"

    # delete the old cards, add the diagrams
    for tid, t in topics.items():
        new_nodes = {}
        for (cid, role), it in req.items():
            if cid.rsplit(".C", 1)[0] == tid:
                new_nodes.setdefault(cid, []).append(make_node(it, inv[(cid, role)], key_dir, cid))
        out, emitted = [], set()
        for md in t["media"]:
            if md.get("type") == "image" and md.get("image_role") in ("question", "solution"):
                removed_ids.add(md["id"])
                cid = md["concept_id"]
                if cid in new_nodes and cid not in emitted:
                    out += sorted(new_nodes[cid], key=lambda n: n["id"])
                    emitted.add(cid)
                continue
            out.append(md)
        for cid, nodes in new_nodes.items():          # worked examples: after the concept's last node, else at the end
            if cid in emitted:
                continue
            last = max([i for i, md in enumerate(out) if md.get("concept_id") == cid] or [len(out) - 1])
            out[last + 1:last + 1] = sorted(nodes, key=lambda n: n["id"])
        t["media"] = out
        added_ids += [n["id"] for ns in new_nodes.values() for n in ns]

    for cid, (t, c) in concepts.items():
        c["media_ids"] = [x for x in c.get("media_ids", []) if x not in removed_ids]
        for b in c.get("content", []):
            for k in ("image_media_id", "solution_image_media_id", "solution_image_media_ids"):
                b.pop(k, None)

    def qblock(c):
        return next(b for b in c["content"] if "question" in b)

    for (cid, role), it in req.items():
        t, c = concepts[cid]
        mid = it["media_id"]
        block = qblock(c)
        tok = "{{DIAGRAM:%s}}" % mid
        tokens[mid] = tok
        mids = c["media_ids"]
        if role == "question":
            mids.append(mid)
            block["image_media_id"] = mid
            put_question_token(block, tok, False)
        elif role == "solution":
            mids.append(mid)                           # after the video, which stays first
            block["solution_image_media_id"] = mid
            assert (it["placeholder"]["insert_into"], it["placeholder"]["position"]) == ("steps_tex", "before_first_step")
            put_solution_token(block, tok)
        else:
            last_img = max([i for i, x in enumerate(mids) if ".IMG" in x] or [-1])
            mids.insert(last_img + 1, mid)
            block["image_media_id"] = mid
            put_question_token(block, tok, True)
    # summary + notes
    n_img = sum(1 for t in topics.values() for md in t["media"] if md.get("type") == "image")
    ss = plan["source_metadata"]["summary_stats"]
    ss["images"] = n_img
    ss["diagram_placeholders"] = len(added_ids)
    plan["source_metadata"]["diagram_v3"] = {
        "from": "cbse_eng_maths6_ch3_v108 (live V2)",
        "note": "Old question and solution card placeholders removed (%d). Diagram placeholders added where a figure is needed "
                "(%d), each titled 'DIAGRAM · ...', specified in diagram_spec, linked by image_media_id / "
                "solution_image_media_id and by a {{DIAGRAM:<id>}} token in the text (solution token before step 1); no block "
                "points at a teaching image. Concept images, videos, tools and teaching text are unchanged."
                % (len(removed_ids), len(added_ids)),
        "rules": ["diagram_identification_prompt v3", "diagram_map.schema v3", "Diagram trigger word companion note (2026-11-18)",
                  "placement map supplied by the user, 21 Nov 2026 (ch3_number_play_diagram_map (1).json): solution tokens before the first step, "
                  "3.1 Q3 question without a diagram, lettered pattern figures b, c, e, f drawn, no teaching image linked from any block"],
    }
    check(plan, src, removed_ids, added_ids, tokens)
    return plan


def walk_nodes(plan):
    for t in (t for m in plan["modules"] for s in m["segments"] for t in s["topics"]):
        yield t


def diff_paths(a, b, path="", out=None):
    out = [] if out is None else out
    if type(a) != type(b):
        out.append(path)
    elif isinstance(a, dict):
        for k in set(a) | set(b):
            if k not in a or k not in b:
                out.append(path + "/" + k)
            else:
                diff_paths(a[k], b[k], path + "/" + k, out)
    elif isinstance(a, list):
        if len(a) != len(b):
            out.append(path + "[len]")
        else:
            for i, (x, y) in enumerate(zip(a, b)):
                diff_paths(x, y, "%s[%d]" % (path, i), out)
    elif a != b:
        out.append(path)
    return out


def check(plan, src, removed_ids, added_ids, tokens):
    errs = []
    s = json.dumps(plan, ensure_ascii=False)
    for t in walk_nodes(plan):
        ids = {md["id"] for md in t["media"]}
        for c in t["concepts"]:
            for x in c.get("media_ids", []):
                if x not in ids:
                    errs.append("%s media_ids %s has no node in its topic" % (c["concept_id"], x))
            for b in c.get("content", []):
                refs = [b.get(k) for k in ("image_media_id", "solution_image_media_id", "video_media_id") if b.get(k)]
                refs += b.get("solution_image_media_ids") or []
                for x in refs:
                    if x not in ids:
                        errs.append("%s block ref %s has no node in its topic" % (c["concept_id"], x))
                    if x not in c.get("media_ids", []):
                        errs.append("%s block ref %s missing from media_ids" % (c["concept_id"], x))
        for md in t["media"]:
            if md.get("image_role") in ("question", "solution") and not md["title"].startswith(DIAGRAM):
                errs.append("old card left: %s" % md["id"])
            if md["id"] in set(added_ids) and not md["title"].startswith(DIAGRAM):
                errs.append("title of %s lacks the DIAGRAM word" % md["id"])
    for mid, tok in tokens.items():
        if s.count(tok) < 1:
            errs.append("token %s not in the plan" % tok)
    for x in removed_ids - set(added_ids):
        if '"%s"' % x in s:
            errs.append("removed id %s is still referenced" % x)
    old_imgs = sum(1 for t in walk_nodes(src) for md in t["media"] if md.get("type") == "image")
    new_imgs = sum(1 for t in walk_nodes(plan) for md in t["media"] if md.get("type") == "image")
    if new_imgs != old_imgs - len(removed_ids) + len(added_ids):
        errs.append("image count %d != %d - %d + %d" % (new_imgs, old_imgs, len(removed_ids), len(added_ids)))
    changed = diff_paths(src, plan)
    ok = re.compile(r"^(/chapter_id|/phase|/version|/plan_id|/_activate|/source_metadata/(summary_stats/images|summary_stats/diagram_placeholders|diagram_v3)"
                    r"|/modules\[\d+\]/segments\[\d+\]/topics\[\d+\](/media(\[.*)?"
                    r"|/concepts\[\d+\](/media_ids(\[.*)?|/content\[\d+\]/(image_media_id|solution_image_media_ids?|question_tex|steps_tex(\[\d+\])?|text|publication_text|answer_tex))))$")
    bad = [p for p in changed if not ok.match(p)]
    if bad:
        errs.append("unexpected changes: %s" % bad[:10])
    if errs:
        print("\n".join("ERROR " + e for e in errs[:40]))
        raise SystemExit("%d integrity errors" % len(errs))
    # v3: no block may point at a teaching image (V2 had none either, so every image link in the plan is a DIAGRAM node)
    for t in walk_nodes(plan):
        for c in t["concepts"]:
            for b in c.get("content", []):
                for k in ("image_media_id", "solution_image_media_id"):
                    if b.get(k) and b[k] not in set(added_ids):
                        errs.append("%s %s points at %s which is not a DIAGRAM node" % (c["concept_id"], k, b[k]))
    if errs:
        print("\n".join("ERROR " + e for e in errs[:40]))
        raise SystemExit("%d integrity errors" % len(errs))
    print("integrity ok: %d old cards removed, %d diagrams added, no teaching image linked, %d changed paths all expected"
          % (len(removed_ids), len(added_ids), len(changed)))


def main():
    a = sys.argv[1:]
    if not a or a[0] not in ("merge", "build"):
        raise SystemExit(__doc__)
    if a[0] == "merge":
        sys.exit(merge())
    if "--version" not in a:
        raise SystemExit("build needs --version N")
    version = int(a[a.index("--version") + 1])
    plan = build(version)
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, plan["plan_id"] + ".json")
    json.dump(plan, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", p, "version", version)


if __name__ == "__main__":
    main()
