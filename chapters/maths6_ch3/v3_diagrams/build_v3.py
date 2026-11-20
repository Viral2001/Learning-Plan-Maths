# -*- coding: utf-8 -*-
"""Build the V3 plan of Class 6 Ch 3 Number Play from the live V2 plan (v108) and the diagram map.

    python -I -X utf8 build_v3.py merge            merge map/out_A..D.json into map/diagram_map.json (and validate)
    python -I -X utf8 build_v3.py build [--version N]
                                                   build out/cbse_eng_maths6_ch3_V3_v<N>.json (N = next free V3 version)

What it does to a COPY of source/cbse_eng_maths6_ch3_v108.json (the live V2 plan; nothing is written to staging):
  1. chapter_id -> cbse_eng_maths6_ch3_V3, phase 3, version N, plan_id <chapter_id>_v<N>.
  2. deletes every image node with image_role "question" or "solution" (the old card placeholders, 149 of them), the
     ids in the concepts' media_ids and the image_media_id / solution_image_media_id(s) fields of the blocks.
  3. for every diagram the map marks `required`, adds one image node (title "DIAGRAM · <label> given figure" / "solution
     figure" / "figure"), puts its id in the concept's media_ids and in the block's image field, and writes the
     {{DIAGRAM:<id>}} token into the block's text fields.
  4. integrity checks, and a diff against v108 that must show nothing else changed.
Concept (teaching) images, videos, tools, text and objectives are untouched.
"""
import copy
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "source", "cbse_eng_maths6_ch3_v108.json")
MAP = os.path.join(HERE, "map", "diagram_map.json")
OUT = os.path.join(HERE, "out")
V3_ID = "cbse_eng_maths6_ch3_V3"
API = "https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/chapter/"
DIAGRAM = "DIAGRAM · "      # "DIAGRAM · "  (companion note: first token of the name, then space-middle dot-space)


def load(p):
    return json.load(open(p, encoding="utf-8"))


def ratio_dims(r, width=1920):
    a, b = [int(x) for x in r.split(":")]
    return "%dx%d" % (width, round(width * b / a))


# ------------------------------------------------------------------ merge
def merge():
    sys.path.insert(0, HERE)
    import validate_map
    items, notes = [], []
    meta = None
    for c in "ABCD":
        m = load(os.path.join(HERE, "map", "out_%s.json" % c))
        meta = meta or m["meta"]
        items += m["items"]
        notes += ["[chunk %s] %s" % (c, n) for n in m["meta"].get("notes", [])]
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
    meta["counts_by_role_and_decision"] = counts
    meta["notes"] = notes
    json.dump({"meta": meta, "style_tokens": load(os.path.join(HERE, "map", "out_A.json"))["style_tokens"], "items": items},
              open(MAP, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("merged", len(items), "items;", json.dumps(counts))
    return validate_map.main(MAP, "all")


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


def put_solution_token(block, tok, insert_into, position):
    if insert_into == "answer_tex":
        for k in ("answer_tex", "text", "publication_text"):
            if isinstance(block.get(k), str):
                block[k] = block[k].rstrip("\n") + "\n" + tok
        return
    steps = block["steps_tex"]
    if position == "before_first_step":
        n = 0
        steps[0] = tok + "\n" + steps[0]
    else:
        n = int(re.match(r"after_step_(\d+)$", position).group(1))
        steps[n - 1] = steps[n - 1] + "\n" + tok
    for k in ("text", "publication_text"):
        if isinstance(block.get(k), str):
            block[k] = insert_line(block[k], line_start(block[k], n + 1), tok)


def strip_tokens(s):
    return re.sub(r"\n?\{\{DIAGRAM:[^}]+\}\}\n?", "\n", s).replace("\n\n", "\n")


# ------------------------------------------------------------------ nodes
def make_node(it, u, key_dir, concept):
    d = it["diagram"]
    mid, role = it["media_id"], it["role"]
    qb = None
    if role == "question":
        label = u["question_concept"]["item"].get("book_number") or u["question_concept"]["name"]
        title, side = "%s%s given figure" % (DIAGRAM, label), "question"
        teach, instr = ("Let the student attempt this before showing the video or the solution.",
                        "Try this question yourself before you watch the video.")
        ctx = "Given figure of %s." % label
    elif role == "solution":
        label = u["answer_concept"]["item"].get("book_number") or u["answer_concept"]["name"]
        title, side = "%s%s solution figure" % (DIAGRAM, label), "solution"
        teach, instr = ("Show only after the student has attempted the question.",
                        "Compare this with your own working, step by step.")
        ctx = "Complete solution figure of %s." % label
    else:
        label = u["concept_name"]
        title, side = "%s%s figure" % (DIAGRAM, label), None
        teach, instr = ("Show this figure with the worked example.", "Follow the figure while you read the example.")
        ctx = "Figure of the worked example %s." % label
    node = {
        "id": mid, "type": "image", "title": title, "labels": list(d["visible_text"]),
        "context": ctx + " PLACEHOLDER: specified, not generated yet.",
        "subtype": "illustration", "image_url": "%s/%s.png" % (key_dir, mid), "concept_id": concept,
    }
    if side:
        node["image_role"] = side
    node.update({
        "description": d["alt_text"], "planned_url": "%s/%s.png" % (key_dir, mid),
        "aspect_ratio": d["aspect_ratio"], "build_status": "placeholder",
        "render_source": {"scene": it.get("manim_scene"), "engine": "manim",
                          "code_url": "%s/code/%s.py" % (key_dir, mid), "style_url": "%s/code/_style.py" % key_dir},
        "image_category": "concept", "teaching_notes": teach, "home_concept_id": concept,
        "negative_prompt": "; ".join(d["must_not_show"]), "image_dimensions": ratio_dims(d["aspect_ratio"]),
        "source_image_key": "", "generation_prompt": d["manim_description"], "related_concept_ids": [],
        "accuracy_constraints": "\n".join(d["accuracy_checks"]), "instructions_for_student": instr,
        "diagram_spec": {k: d[k] for k in ("diagram_type", "content", "manim_description", "visible_text", "must_not_show",
                                           "accuracy_checks", "alt_text") if k in d}
        | {"derived_from": d.get("derived_from"), "reason_codes": it["reason_codes"], "reason": it["reason"],
           "needs_lp_text_sync": bool(it.get("needs_lp_text_sync"))},
    })
    return node


# ------------------------------------------------------------------ build
def next_version():
    with urllib.request.urlopen(API + V3_ID + "/versions", timeout=60) as r:
        return max(v["version"] for v in json.load(r)["data"]) + 1


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

    plan["chapter_id"], plan["phase"], plan["version"] = V3_ID, 3, version
    plan["plan_id"] = "%s_v%d" % (V3_ID, version)
    plan["_activate"] = True

    removed_ids, added_ids, tokens = set(), [], {}
    topics = {t["topic_id"]: t for m in plan["modules"] for s in m["segments"] for t in s["topics"]}
    concepts = {c["concept_id"]: (t, c) for t in topics.values() for c in t["concepts"]}

    # key dir of the new nodes: same bucket folder as the old cards, folder diagram_v1
    old = next(md for t in topics.values() for md in t["media"] if md.get("image_role"))
    key_dir = re.sub(r"/[^/]+/[^/]+$", "", old["planned_url"]) + "/diagram_v1"

    # 1+2: delete the old cards, 3: add the diagrams
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

    for (cid, role), it in req.items():
        t, c = concepts[cid]
        mid = it["media_id"]
        block = next(b for b in c["content"] if "question" in b)
        tok = "{{DIAGRAM:%s}}" % mid
        tokens[mid] = tok
        mids = c["media_ids"]
        if role == "question":
            mids.append(mid)
            block["image_media_id"] = mid
            put_question_token(block, tok, False)
        elif role == "solution":
            mids.append(mid)                           # after the video, which stays first
            put_solution_token(block, tok, it["placeholder"]["insert_into"], it["placeholder"]["position"])
        else:
            last_img = max([i for i, x in enumerate(mids) if ".IMG" in x] or [-1])
            mids.insert(last_img + 1, mid)
            block["image_media_id"] = mid
            put_question_token(block, tok, True)
    # solution image fields (one or two ids per answer concept), in media_ids order
    for cid, (t, c) in concepts.items():
        sol = [x for x in c["media_ids"] if (cid, "solution") in req and x in
               {r["media_id"] for (k, rl), r in req.items() if k == cid and rl == "solution"}]
        if sol:
            blk = next(b for b in c["content"] if "question" in b)
            blk["solution_image_media_id"] = sol[0]
            if len(sol) > 1:
                blk["solution_image_media_ids"] = sol

    # summary + notes
    n_img = sum(1 for t in topics.values() for md in t["media"] if md.get("type") == "image")
    ss = plan["source_metadata"]["summary_stats"]
    ss["images"] = n_img
    ss["diagram_placeholders"] = len(added_ids)
    plan["source_metadata"]["diagram_v3"] = {
        "from": "cbse_eng_maths6_ch3_v108 (live V2)",
        "note": "Old question and solution card placeholders removed (%d). Diagram placeholders added where a figure is needed "
                "(%d), each titled 'DIAGRAM · ...', specified in diagram_spec, linked by image_media_id / "
                "solution_image_media_id(s) and by a {{DIAGRAM:<id>}} token in the text. Concept images, videos, tools and "
                "teaching text are unchanged." % (len(removed_ids), len(added_ids)),
        "rules": ["docs/karan-MD/diagram_identification_prompt.md v1", "Diagram trigger word companion note (2026-11-18)"],
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
    # every id referenced resolves, inside its own topic
    for t in walk_nodes(plan):
        ids = {md["id"] for md in t["media"]}
        for c in t["concepts"]:
            for x in c.get("media_ids", []):
                if x not in ids:
                    errs.append("%s media_ids %s has no node" % (c["concept_id"], x))
            for b in c.get("content", []):
                refs = [b.get(k) for k in ("image_media_id", "solution_image_media_id", "video_media_id") if b.get(k)]
                refs += b.get("solution_image_media_ids") or []
                for x in refs:
                    if x not in ids:
                        errs.append("%s block ref %s has no node" % (c["concept_id"], x))
                    if x not in c.get("media_ids", []):
                        errs.append("%s block ref %s missing from media_ids" % (c["concept_id"], x))
        for md in t["media"]:
            if md.get("image_role") in ("question", "solution"):
                if not md["title"].startswith(DIAGRAM):
                    errs.append("old card left: %s" % md["id"])
            if md["id"] in set(added_ids) and not md["title"].startswith(DIAGRAM):
                errs.append("title of %s lacks the DIAGRAM word" % md["id"])
    for mid, tok in tokens.items():
        if s.count(tok) < 1:
            errs.append("token %s not in the plan" % tok)
    # old card ids that were not re-added must not be mentioned anywhere
    for x in removed_ids - set(added_ids):
        if '"%s"' % x in s:
            errs.append("removed id %s is still referenced" % x)
    # node counts
    old_imgs = sum(1 for t in walk_nodes(src) for md in t["media"] if md.get("type") == "image")
    new_imgs = sum(1 for t in walk_nodes(plan) for md in t["media"] if md.get("type") == "image")
    if new_imgs != old_imgs - len(removed_ids) + len(added_ids):
        errs.append("image count %d != %d - %d + %d" % (new_imgs, old_imgs, len(removed_ids), len(added_ids)))
    # nothing but the expected changes
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
    print("integrity ok: %d old cards removed, %d diagrams added, %d changed paths all expected" % (len(removed_ids), len(added_ids), len(changed)))


def main():
    a = sys.argv[1:]
    if not a or a[0] not in ("merge", "build"):
        raise SystemExit(__doc__)
    if a[0] == "merge":
        sys.exit(merge())
    version = int(a[a.index("--version") + 1]) if "--version" in a else next_version()
    plan = build(version)
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, plan["plan_id"] + ".json")
    json.dump(plan, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", p, "version", version)


if __name__ == "__main__":
    main()
