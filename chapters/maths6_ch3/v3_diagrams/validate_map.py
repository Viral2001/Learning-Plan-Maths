# -*- coding: utf-8 -*-
"""Check a diagram map (or one chunk of it) against diagram_map.schema.json and the rules of this plan.

    python -I -X utf8 validate_map.py <map json> [--chunk A|B|C|D|all]

--chunk A..D : the map must hold exactly the units of map/in_<chunk>.json (a chunk file written by an agent)
--chunk all  : the merged map must hold all 101 units (map/inventory.json)

Exit code 0 only when there are no errors. Warnings are printed but do not fail.
"""
import json
import os
import re
import sys

import jsonschema

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA = os.path.join(HERE, "..", "..", "..", "docs", "karan-MD", "diagram_map.schema.json")
VAGUE = re.compile(r"\b(some|several|etc\.?|similar|a few|various)\b", re.I)
BAD_VISIBLE = re.compile(r"(figure it out|^q\d|\bfind\b|\bhence\b|\banswer\b|table \d|ncert|page \d)", re.I)


def main(path, chunk):
    errors, warnings = [], []
    schema = json.load(open(SCHEMA, encoding="utf-8"))
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
    # LP order
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
            if role in ("question", "worked_example") and ins != "question_tex":
                errors.append("%s: %s diagram must insert into question_tex" % (cid, role))
            if role == "solution" and ins not in ("steps_tex", "answer_tex"):
                errors.append("%s: solution diagram must insert into steps_tex or answer_tex" % cid)
            if role == "solution" and ins == "answer_tex" and it["placeholder"]["position"] != "after_answer":
                errors.append("%s: answer_tex goes with position after_answer" % cid)
            if role == "solution" and ins == "steps_tex" and it["placeholder"]["position"] in ("after_question_text",):
                errors.append("%s: bad position for steps_tex" % cid)
            if role == "solution" and ins == "steps_tex":
                mm = re.match(r"after_step_(\d+)$", it["placeholder"]["position"])
                nsteps = len(u["answer_concept"]["item"].get("steps_tex") or u["answer_concept"]["item"].get("steps") or [])
                if mm and not (1 <= int(mm.group(1)) <= nsteps):
                    errors.append("%s: after_step_%s but the solution has %d steps" % (cid, mm.group(1), nsteps))
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
            if dec == "none" and role in ("question", "solution") and act not in ("drop_image", "reuse_concept_image", "no_image"):
                errors.append("%s: bad action %s for decision none" % (cid, act))
            if dec == "none" and role == "worked_example" and act not in ("no_image", "reuse_concept_image"):
                errors.append("%s: bad action %s for a worked example with no diagram" % (cid, act))
            if dec == "optional":
                if act not in ("drop_image", "no_image"):
                    errors.append("%s: an optional item is not added in this run: action must be drop_image / no_image" % cid)
                if it.get("media_id") is not None and role == "worked_example":
                    pass
        if act == "reuse_concept_image":
            rid = it.get("reuse_media_id")
            if rid not in concept_imgs:
                errors.append("%s: reuse_media_id %r is not a concept image of this plan" % (cid, rid))
            else:
                # the concept image must be in the same topic
                if rid.split(".C")[0] != cid.split(".C")[0]:
                    errors.append("%s: reuse_media_id %s is in another topic" % (cid, rid))
    # solution derived_from
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
        if it["role"] == "question" and df:
            errors.append("%s: a question diagram has nothing to derive from" % it["lp_concept_id"])
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
    print("items %d | units expected %d | required %d | optional %d | none %d | errors %d | warnings %d" % (
        len(items), len(expected),
        sum(i["decision"] == "required" for i in items), sum(i["decision"] == "optional" for i in items),
        sum(i["decision"] == "none" for i in items), len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    a = sys.argv[1:]
    ch = "all"
    if "--chunk" in a:
        ch = a[a.index("--chunk") + 1]
    sys.exit(main(a[0], ch))
