# -*- coding: utf-8 -*-
"""Check a diagram map (or one chunk of it) against the chapter's spec/diagram_map.schema_v3.json and the rules of this run.

    python -I -X utf8 validate_map.py <map json> --chunk A|B|...|all --here <chapter v2_diagrams dir>

--chunk X  : the map must hold exactly the units of <here>/map/in_X.json (a chunk file written by an agent)
--chunk all: the merged map must hold all units (<here>/map/inventory.json) and claim every figure of the base inventory
             (<here>/map/inv_base_*.json)

Units (map/inventory.json, built by rollout.py prepare) and the items they give:
  pair    question concept + answer concept            -> (q cid, question, 0) + (a cid, solution, 0)
  single  ONE concept block that links cards           -> (cid, question, block_index) + (cid, solution, block_index)
  worked  a worked-example block without card links    -> (cid, worked_example, block_index)
v3 rules (diagram_identification_prompt v3): figure_inventory + coverage_report required and consistent; a solution diagram is
steps_tex / before_first_step, a question or worked-example diagram question_tex / after_question_text; no reuse of a teaching
image; media ids <cid>.IMG<n> that never collide with a kept (non-card) image of the concept and are unique (the build renumbers
them in media-list order, as the upload server demands).
Exit code 0 only when there are no errors.
"""
import glob
import json
import os
import re
import sys

import jsonschema

VAGUE = re.compile(r"\b(some|several|etc\.?|similar|a few|various)\b", re.I)
BAD_VISIBLE = re.compile(r"(figure it out|^q\d|\bfind\b|\bhence\b|\banswer\b|table \d|ncert|page \d)", re.I)
MAPPED = re.compile(r"^(item:([^ #]+)(?:#(\d+))? \((question|solution)\)|concept_image:(.+)|none:([A-Z_]+))$")


def ikey(it):
    return (it.get("lp_concept_id"), it.get("role"), it.get("block_index", 0))


def main(path, chunk, H, meta, quiet=False):
    errors, warnings = [], []
    schema = json.load(open(os.path.join(H, "spec", "diagram_map.schema_v3.json"), encoding="utf-8"))
    codes = set(schema["properties"]["items"]["items"]["properties"]["reason_codes"]["items"]["enum"])
    m = json.load(open(path, encoding="utf-8"))
    v = jsonschema.Draft202012Validator(schema)
    for e in sorted(v.iter_errors(m), key=lambda e: list(e.path)):
        errors.append("SCHEMA %s: %s" % ("/".join(str(p) for p in e.path), e.message[:200]))
    if m.get("meta", {}).get("class") != meta["class_no"]:
        errors.append("meta.class must be %d" % meta["class_no"])
    units = json.load(open(os.path.join(H, "map", "inventory.json" if chunk == "all" else "in_%s.json" % chunk), encoding="utf-8"))
    concept_imgs = {c["id"] for c in json.load(open(os.path.join(H, "map", "concept_images.json"), encoding="utf-8"))}
    base = {}
    for p in sorted(glob.glob(os.path.join(H, "map", "inv_base_*.json"))):
        for x in json.load(open(p, encoding="utf-8")):
            base[x["fig_id"]] = x

    expected, kept = {}, {}
    for u in units:
        if u["kind"] == "pair":
            qk, ak = (u["question_concept"]["concept_id"], "question", 0), (u["answer_concept"]["concept_id"], "solution", 0)
            expected[qk], expected[ak] = u, u
            kept[qk], kept[ak] = set(u["question_concept"]["kept_image_ids"]), set(u["answer_concept"]["kept_image_ids"])
        elif u["kind"] == "single":
            for r in ("question", "solution"):
                k = (u["concept_id"], r, u["block_index"])
                expected[k] = u
                kept[k] = set(u.get("kept_image_ids") or [])
        else:
            k = (u["concept_id"], "worked_example", u["block_index"])
            expected[k] = u
            kept[k] = set(u.get("kept_image_ids") or [])
    items = m.get("items", [])
    seen = {}
    for it in items:
        k = ikey(it)
        if k in seen:
            errors.append("duplicate item %s" % (k,))
        seen[k] = it
        if k not in expected:
            errors.append("item %s is not a unit of this chunk" % (k,))
            continue
        u = expected[k]
        if u["kind"] in ("single", "worked") and "block_index" not in it:
            errors.append("%s: %s item needs block_index (%d)" % (it.get("lp_concept_id"), it.get("role"), u["block_index"]))
    for k in expected:
        if k not in seen:
            errors.append("missing item %s" % (k,))
    order = [ikey(it) for it in items if ikey(it) in expected]
    if order != [k for k in expected if k in seen]:
        warnings.append("items are not in LP order")

    media_ids = {}
    for it in items:
        k = ikey(it)
        u = expected.get(k)
        if not u:
            continue
        dec, act, role, cid = it.get("decision"), it.get("lp_placeholder_action"), it.get("role"), it["lp_concept_id"]
        if act == "reuse_concept_image" or it.get("reuse_media_id"):
            errors.append("%s: no reuse of a teaching image in v3: a concept image is never linked" % cid)
        if dec == "required":
            mid = it.get("media_id")
            if mid in media_ids:
                errors.append("%s: media_id %s used twice (%s)" % (cid, mid, media_ids[mid]))
            media_ids[mid] = cid
            if not re.match(r"^%s\.IMG\d+$" % re.escape(cid), mid or ""):
                errors.append("%s: media id must look like %s.IMG<n>, got %s" % (cid, cid, mid))
            if mid in kept[k]:
                errors.append("%s: media id %s collides with a kept image of the concept (%s): use the next free number" % (cid, mid, sorted(kept[k])))
            tok = (it.get("placeholder") or {}).get("token")
            if tok != "{{DIAGRAM:%s}}" % mid:
                errors.append("%s: token %r does not match media_id %r" % (cid, tok, mid))
            ins, pos = (it.get("placeholder") or {}).get("insert_into"), (it.get("placeholder") or {}).get("position")
            if role in ("question", "worked_example") and (ins, pos) != ("question_tex", "after_question_text"):
                errors.append("%s: %s diagram must be question_tex / after_question_text, got %s / %s" % (cid, role, ins, pos))
            if role == "solution" and (ins, pos) != ("steps_tex", "before_first_step"):
                errors.append("%s: solution diagram must be steps_tex / before_first_step (v3 rule), got %s / %s" % (cid, ins, pos))
            if role == "worked_example" and act != "add_new_image":
                errors.append("%s: required worked-example diagram must be add_new_image" % cid)
            if role in ("question", "solution") and act not in ("keep_and_replace_spec", "add_new_image"):
                errors.append("%s: bad action %s for a required %s diagram" % (cid, act, role))
            d = it.get("diagram") or {}
            if VAGUE.search(d.get("manim_description", "")):
                errors.append("%s: vague word in manim_description: %s" % (cid, VAGUE.search(d["manim_description"]).group(0)))
            for s in d.get("visible_text", []):
                if BAD_VISIBLE.search(s):
                    errors.append("%s: visible_text %r looks like instruction/heading text" % (cid, s))
                if len(s.split()) > 6 and role != "worked_example":
                    warnings.append("%s: long visible_text %r" % (cid, s[:60]))
            if d.get("diagram_type") != (d.get("content") or {}).get("type"):
                warnings.append("%s: diagram_type != content.type" % cid)
        else:
            if "diagram" in it:
                errors.append("%s: decision %s but has a diagram" % (cid, dec))
            if dec in ("none", "optional") and act not in ("drop_image", "no_image"):
                errors.append("%s: bad action %s for decision %s (drop_image / no_image)" % (cid, act, dec))
    for it in items:
        d = it.get("diagram")
        if not d:
            continue
        df = d.get("derived_from")
        if df and df not in media_ids:
            errors.append("%s: derived_from %s is not a media id of this map" % (it["lp_concept_id"], df))
        if it["role"] != "solution" and df:
            errors.append("%s: only a solution diagram derives from another" % it["lp_concept_id"])
        if it["role"] == "solution":
            u = expected.get(ikey(it))
            qk = (u["question_concept"]["concept_id"], "question", 0) if u["kind"] == "pair" else (u["concept_id"], "question", u["block_index"])
            q = seen.get(qk)
            if q and q.get("decision") == "required" and df != q.get("media_id"):
                errors.append("%s: solution diagram must be derived_from the question diagram %s" % (it["lp_concept_id"], q["media_id"]))

    fi = m.get("figure_inventory", [])
    ids, claimed, item_refs = set(), {"items": 0, "concept": 0, "none": 0}, {}
    for f in fi:
        fid = f.get("fig_id")
        if fid in ids:
            errors.append("figure_inventory: duplicate fig_id %s" % fid)
        ids.add(fid)
        mt = MAPPED.match(f.get("mapped_to", ""))
        if not mt:
            errors.append("figure %s: mapped_to %r does not match item:<cid>[#<block>] (question|solution) / concept_image:<id> / none:<CODE>" % (fid, f.get("mapped_to")))
            continue
        if mt.group(2):
            claimed["items"] += 1
            cid, blk, role = mt.group(2), int(mt.group(3) or 0), mt.group(4)
            cands = [(cid, "worked_example", blk), (cid, role, blk), (cid, role, 0)] if role == "question" else [(cid, role, blk), (cid, role, 0)]
            real = next((c_ for c_ in cands if c_ in seen), None)
            tgt = seen.get(real) if real else None
            if tgt is None:
                errors.append("figure %s maps to item %s (%s) which is not an item of this map" % (fid, cid, role))
            elif tgt["decision"] != "required":
                errors.append("figure %s maps to item %s (%s) whose decision is %s, not required" % (fid, cid, role, tgt["decision"]))
            else:
                item_refs.setdefault(real, []).append(fid)
        elif mt.group(5):
            claimed["concept"] += 1
            if mt.group(5) not in concept_imgs:
                errors.append("figure %s maps to concept image %s which is not in the plan" % (fid, mt.group(5)))
        else:
            claimed["none"] += 1
            if mt.group(6) not in codes:
                errors.append("figure %s: none:%s is not a reason code" % (fid, mt.group(6)))
        if fid not in base and not str(fid).startswith("NEW-"):
            errors.append("figure %s is not in the base inventory (give a figure you found yourself the prefix NEW-)" % fid)
    for it in items:
        if it["decision"] == "required" and ikey(it) not in item_refs:
            warnings.append("%s (%s): required but no inventory figure maps to it (fine only when the figure is not printed in the book)" % (it["lp_concept_id"], it["role"]))
    cr = m.get("coverage_report", {})
    for key, val in (("inventory_figures", len(fi)), ("mapped_to_items", claimed["items"]), ("mapped_to_concept_images", claimed["concept"]), ("mapped_none", claimed["none"])):
        if key in cr and cr[key] != val:
            errors.append("coverage_report.%s is %s, the inventory says %s" % (key, cr[key], val))
    if cr.get("unmapped") != 0:
        errors.append("coverage_report.unmapped must be 0")
    req_ids = {i["media_id"] for i in items if i["decision"] == "required"}
    for x in cr.get("new_media_ids_created", []) or []:
        if x not in req_ids:
            errors.append("coverage_report.new_media_ids_created lists %s which is not a required item's media_id" % x)
    if chunk == "all":
        for fid in base:
            if fid not in ids:
                errors.append("base inventory figure %s is not claimed in the merged map" % fid)
    cnt = {}
    for it in items:
        cnt.setdefault(it["role"], {}).setdefault(it["decision"], 0)
        cnt[it["role"]][it["decision"]] += 1
    mc = m.get("meta", {}).get("counts_by_role_and_decision", {})
    for r, dd in cnt.items():
        for d_, n_ in dd.items():
            if (mc.get(r) or {}).get(d_, 0) != n_:
                errors.append("meta.counts_by_role_and_decision[%s][%s] is %s, items say %d" % (r, d_, (mc.get(r) or {}).get(d_), n_))
    for r, dd in mc.items():
        for d_, n_ in dd.items():
            if n_ and cnt.get(r, {}).get(d_, 0) != n_:
                errors.append("meta count %s/%s=%s has no matching items" % (r, d_, n_))
    if not quiet:
        for e in errors:
            print("ERROR  ", e)
        for w in warnings:
            print("warning", w)
        print("items %d | units expected %d | required %d | optional %d | none %d | figures %d | errors %d | warnings %d" % (
            len(items), len(expected), sum(i["decision"] == "required" for i in items), sum(i["decision"] == "optional" for i in items),
            sum(i["decision"] == "none" for i in items), len(fi), len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    a = sys.argv[1:]
    H = a[a.index("--here") + 1].rstrip("/")
    ch = a[a.index("--chunk") + 1] if "--chunk" in a else "all"
    meta = json.load(open(os.path.join(H, "meta.json"), encoding="utf-8"))
    sys.exit(main(a[0], ch, H, meta))
