# -*- coding: utf-8 -*-
"""Check a diagram map (or one chunk of it) against spec/diagram_map.schema_v3.json and the rules of this plan.

    python -I -X utf8 validate_map.py <map json> [--chunk A|B|C|D|all]

--chunk A..D : the map must hold exactly the units of map/in_<chunk>.json (a chunk file written by an agent)
--chunk all  : the merged map must hold all 101 units (map/inventory.json) and claim every figure of the base inventory

v3 rules (diagram_identification_prompt v3): figure_inventory + coverage_report are required and must add up, every
mapped_to points at something that exists, items judged without an LP image id like all others.
Exit code 0 only when there are no errors. Warnings are printed but do not fail.
"""
import json
import os
import re
import sys

import jsonschema

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA = os.path.join(HERE, "spec", "diagram_map.schema_v3.json")
VAGUE = re.compile(r"\b(some|several|etc\.?|similar|a few|various)\b", re.I)
BAD_VISIBLE = re.compile(r"(figure it out|^q\d|\bfind\b|\bhence\b|\banswer\b|table \d|ncert|page \d)", re.I)
MAPPED = re.compile(r"^(item:([^ ]+) \((question|solution)\)|concept_image:(.+)|none:([A-Z_]+))$")


def base_inventory():
    out = {}
    for f in ("inv_base_chapter.json", "inv_base_solutions.json"):
        p = os.path.join(HERE, "map", f)
        if os.path.exists(p):
            for x in json.load(open(p, encoding="utf-8")):
                out[x["fig_id"]] = x
    return out


def main(path, chunk):
    errors, warnings = [], []
    schema = json.load(open(SCHEMA, encoding="utf-8"))
    codes = set(schema["properties"]["items"]["items"]["properties"]["reason_codes"]["items"]["enum"])
    m = json.load(open(path, encoding="utf-8"))
    v = jsonschema.Draft202012Validator(schema)
    for e in sorted(v.iter_errors(m), key=lambda e: list(e.path)):
        errors.append("SCHEMA %s: %s" % ("/".join(str(p) for p in e.path), e.message[:200]))
    if m.get("meta", {}).get("class") != 6:
        errors.append("meta.class must be 6")

    inv_path = os.path.join(HERE, "map", "inventory.json" if chunk == "all" else "in_%s.json" % chunk)
    units = json.load(open(inv_path, encoding="utf-8"))
    concept_imgs = {c["id"] for c in json.load(open(os.path.join(HERE, "map", "concept_images.json"), encoding="utf-8"))}

    expected = {}   # (concept_id, role) -> unit
    for u in units:
        if u["kind"] == "pair":
            expected[(u["question_concept"]["concept_id"], "question")] = u
            expected[(u["answer_concept"]["concept_id"], "solution")] = u
        else:
            expected[(u["concept_id"], "worked_example")] = u
    items = m.get("items", [])
    seen = {}
    for it in items:
        k = (it.get("lp_concept_id"), it.get("role"))
        if k in seen:
            errors.append("duplicate item %s" % (k,))
        seen[k] = it
        if k not in expected:
            errors.append("item %s is not a unit of this chunk" % (k,))
    for k in expected:
        if k not in seen:
            errors.append("missing item %s" % (k,))
    order = [(it["lp_concept_id"], it["role"]) for it in items if (it.get("lp_concept_id"), it.get("role")) in expected]
    want = [k for k in expected if k in seen]
    if order != want:
        warnings.append("items are not in LP order")

    media_ids = {}
    for it in items:
        k = (it.get("lp_concept_id"), it.get("role"))
        u = expected.get(k)
        if not u:
            continue
        dec, act, role = it.get("decision"), it.get("lp_placeholder_action"), it.get("role")
        cid = it["lp_concept_id"]
        if dec == "required":
            mid = it.get("media_id")
            if mid in media_ids:
                errors.append("%s: media_id %s used twice (%s)" % (cid, mid, media_ids[mid]))
            media_ids[mid] = cid
            tok = (it.get("placeholder") or {}).get("token")
            if tok != "{{DIAGRAM:%s}}" % mid:
                errors.append("%s: token %r does not match media_id %r" % (cid, tok, mid))
            ins = (it.get("placeholder") or {}).get("insert_into")
            pos = (it.get("placeholder") or {}).get("position")
            if role in ("question", "worked_example") and (ins, pos) != ("question_tex", "after_question_text"):
                errors.append("%s: %s diagram must be question_tex / after_question_text, got %s / %s" % (cid, role, ins, pos))
            if role == "solution" and (ins, pos) != ("steps_tex", "before_first_step"):
                errors.append("%s: solution diagram must be steps_tex / before_first_step (v3 rule), got %s / %s" % (cid, ins, pos))
            if role == "question":
                want_id = "%s.IMG1" % cid
                if mid != want_id:
                    errors.append("%s: question diagram id must be %s, got %s" % (cid, want_id, mid))
                if act != "keep_and_replace_spec":
                    errors.append("%s: required question diagram on a pair must be keep_and_replace_spec" % cid)
            if role == "solution":
                if mid != "%s.IMG1" % cid:
                    errors.append("%s: solution diagram id must be %s.IMG1 (one solution diagram per answer concept), got %s" % (cid, cid, mid))
                if act not in ("keep_and_replace_spec", "add_new_image"):
                    errors.append("%s: bad action %s for a required solution diagram" % (cid, act))
            if role == "worked_example":
                taken = {x for x in (u.get("existing_concept_media_ids") or [])}
                if mid in taken:
                    errors.append("%s: worked-example diagram id %s already exists on the concept" % (cid, mid))
                if not re.match(r"^%s\.IMG\d+$" % re.escape(cid), mid or ""):
                    errors.append("%s: bad media id %s" % (cid, mid))
                if act != "add_new_image":
                    errors.append("%s: required worked-example diagram must be add_new_image" % cid)
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
            if dec == "none" and act not in ("drop_image", "no_image"):
                errors.append("%s: bad action %s for decision none (v3: drop_image for a pair, no_image for a worked example)" % (cid, act))
            if dec == "none" and role == "worked_example" and act != "no_image":
                errors.append("%s: a worked example with no diagram uses no_image" % cid)
            if dec == "optional" and act not in ("drop_image", "no_image"):
                errors.append("%s: an optional item is not added in this run: action must be drop_image / no_image" % cid)
        if act == "reuse_concept_image" or it.get("reuse_media_id"):
            errors.append("%s: no reuse of a teaching image in v3 (no reuse_concept_image / reuse_media_id): a concept image is never linked" % cid)
    for it in items:
        d = it.get("diagram")
        if not d:
            continue
        df = d.get("derived_from")
        if df and df not in media_ids:
            errors.append("%s: derived_from %s is not a media id of this map" % (it["lp_concept_id"], df))
        if it["role"] == "solution":
            u = expected.get((it["lp_concept_id"], "solution"))
            qcid = u["question_concept"]["concept_id"]
            q = seen.get((qcid, "question"))
            if q and q.get("decision") == "required" and df != q.get("media_id"):
                errors.append("%s: solution diagram must be derived_from the question diagram %s" % (it["lp_concept_id"], q["media_id"]))
        if it["role"] != "solution" and df:
            errors.append("%s: only a solution diagram derives from another" % it["lp_concept_id"])

    # ---- v2: figure inventory + coverage report
    fi = m.get("figure_inventory", [])
    base = base_inventory()
    ids, claimed = set(), {"items": 0, "concept": 0, "none": 0}
    item_refs = {}
    for f in fi:
        fid = f.get("fig_id")
        if fid in ids:
            errors.append("figure_inventory: duplicate fig_id %s" % fid)
        ids.add(fid)
        mt = MAPPED.match(f.get("mapped_to", ""))
        if not mt:
            continue
        if mt.group(2):
            claimed["items"] += 1
            cid = mt.group(2)
            role = mt.group(3)
            real = "worked_example" if (cid, "worked_example") in expected and role == "question" else role
            tgt = seen.get((cid, real))
            if tgt is None:
                errors.append("figure %s maps to item %s (%s) which is not an item of this map" % (fid, cid, role))
            elif tgt["decision"] != "required":
                errors.append("figure %s maps to item %s (%s) whose decision is %s, not required" % (fid, cid, role, tgt["decision"]))
            else:
                item_refs.setdefault((cid, real), []).append(fid)
        elif mt.group(4):
            claimed["concept"] += 1
            if mt.group(4) not in concept_imgs:
                errors.append("figure %s maps to concept image %s which is not in the plan" % (fid, mt.group(4)))
        else:
            claimed["none"] += 1
            if mt.group(5) not in codes:
                errors.append("figure %s: none:%s is not a reason code" % (fid, mt.group(5)))
        if fid not in base and not str(fid).startswith("NEW-"):
            errors.append("figure %s is not in the base inventory (give a figure you found yourself the prefix NEW-)" % fid)
    for it in items:
        if it["decision"] == "required" and (it["lp_concept_id"], it["role"]) not in item_refs:
            warnings.append("%s (%s): required but no inventory figure maps to it (fine only when the figure is not printed in the book)" % (it["lp_concept_id"], it["role"]))
    cr = m.get("coverage_report", {})
    for key, val in (("inventory_figures", len(fi)), ("mapped_to_items", claimed["items"]),
                     ("mapped_to_concept_images", claimed["concept"]), ("mapped_none", claimed["none"])):
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

    # meta counts
    cnt = {}
    for it in items:
        cnt.setdefault(it["role"], {}).setdefault(it["decision"], 0)
        cnt[it["role"]][it["decision"]] += 1
    mc = m.get("meta", {}).get("counts_by_role_and_decision", {})
    for r, dd in cnt.items():
        for d_, n in dd.items():
            if (mc.get(r) or {}).get(d_, 0) != n:
                errors.append("meta.counts_by_role_and_decision[%s][%s] is %s, items say %d" % (r, d_, (mc.get(r) or {}).get(d_), n))
    for r, dd in mc.items():
        for d_, n in dd.items():
            if n and cnt.get(r, {}).get(d_, 0) != n:
                errors.append("meta count %s/%s=%s has no matching items" % (r, d_, n))
    for e in errors:
        print("ERROR  ", e)
    for w in warnings:
        print("warning", w)
    print("items %d | units expected %d | required %d | optional %d | none %d | figures %d | errors %d | warnings %d" % (
        len(items), len(expected),
        sum(i["decision"] == "required" for i in items), sum(i["decision"] == "optional" for i in items),
        sum(i["decision"] == "none" for i in items), len(fi), len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    a = sys.argv[1:]
    ch = "all"
    if "--chunk" in a:
        ch = a[a.index("--chunk") + 1]
    sys.exit(main(a[0], ch))
