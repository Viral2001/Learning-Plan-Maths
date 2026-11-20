# -*- coding: utf-8 -*-
"""Inventory of every question / solution / worked-example item of the live Class 6 Ch 3 plan.

    python -I -X utf8 inventory.py <live plan.json> <out dir>

Writes <out dir>/inventory.json (all units, LP order) and <out dir>/in_<module>.json (one file per chunk A-D,
the chunks the diagram-identification agents work on). Read-only on the plan.

A "unit" is one book question as the plan holds it:
  pair     a Questions-topic question concept (qt_part=question) and its answer concept (qt_part=answer)
  worked   a worked-example item that lives inside a teaching concept (question + steps + answer in one block)
"""
import json
import os
import sys


def short(s, n=None):
    return s if n is None or len(s) <= n else s[:n] + "..."


def item_view(c, it):
    keep = ("question", "question_tex", "steps_tex", "answer_tex", "steps", "answer", "text", "q_figure",
            "s_figure", "book_number", "item_kind", "ncert_refs", "image_media_id", "solution_image_media_id",
            "solution_image_media_ids", "video_media_id", "example_id")
    d = {k: it[k] for k in keep if k in it and it[k] not in (None, "", [])}
    return d


CHUNKS = {
    "A": ["M1"],
    "B": ["M2", "M4"],
    "C": ["M3.S19", "M3.S20", "M3.S21", "M3.S22", "M3.S23", "M3.S24", "M3.S25"],
    "D": ["M3.S26", "M3.S27", "M3.S28", "M3.S29", "M3.S30", "M3.S31"],
}


def concept_images(t):
    out = []
    for md in t.get("media", []):
        if md.get("type") == "image" and not md.get("image_role"):
            out.append({"id": md["id"], "concept_id": md.get("concept_id"), "title": md.get("title"),
                        "description": short(md.get("description") or "", 600)})
    return out


def chunk_of(topic_id):
    for k, prefixes in CHUNKS.items():
        for pre in prefixes:
            if topic_id == pre or topic_id.startswith(pre + ".") or topic_id.split(".")[0] == pre:
                return k
    raise KeyError(topic_id)


def main(plan_path, out_dir):
    plan = json.load(open(plan_path, encoding="utf-8"))
    os.makedirs(out_dir, exist_ok=True)
    units = []
    for m in plan["modules"]:
        for s in m["segments"]:
            for t in s["topics"]:
                cons = t["concepts"]
                i = 0
                while i < len(cons):
                    c = cons[i]
                    qitems = [it for it in c.get("content", []) if "question" in it]
                    if not qitems:
                        i += 1
                        continue
                    part = c.get("qt_part")
                    base = {"module_id": m["module_id"], "topic_id": t["topic_id"], "topic_name": t["topic_name"],
                            "concept_id": c["concept_id"], "concept_name": c.get("concept_name"),
                            "ncert_refs": c.get("ncert_refs")}
                    if part == "question":
                        a = cons[i + 1] if i + 1 < len(cons) else None
                        assert a is not None and a.get("qt_part") == "answer", c["concept_id"]
                        ai = [it for it in a["content"] if "question" in it]
                        assert len(qitems) == 1 and len(ai) == 1, c["concept_id"]
                        units.append({"unit": len(units) + 1, "kind": "pair", "module_id": m["module_id"],
                                      "topic_id": t["topic_id"], "topic_name": t["topic_name"],
                                      "question_concept": {"concept_id": c["concept_id"], "name": c.get("concept_name"),
                                                           "item": item_view(c, qitems[0])},
                                      "answer_concept": {"concept_id": a["concept_id"], "name": a.get("concept_name"),
                                                         "media_ids": a.get("media_ids"),
                                                         "item": item_view(a, ai[0])},
                                      "ncert_refs": c.get("ncert_refs")})
                        i += 2
                        continue
                    assert part != "answer", "orphan answer %s" % c["concept_id"]
                    for k, it in enumerate(qitems):
                        units.append({"unit": len(units) + 1, "kind": "worked", "module_id": m["module_id"],
                                      "topic_id": t["topic_id"], "topic_name": t["topic_name"],
                                      "concept_id": c["concept_id"], "concept_name": c.get("concept_name"),
                                      "block_index": k, "ncert_refs": c.get("ncert_refs"),
                                      "item": item_view(c, it),
                                      "existing_concept_media_ids": c.get("media_ids")})
                    i += 1
    json.dump(units, open(os.path.join(out_dir, "inventory.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    by = {}
    for u in units:
        by.setdefault(chunk_of(u["topic_id"]), []).append(u)
    for mid, us in sorted(by.items()):
        json.dump(us, open(os.path.join(out_dir, "in_%s.json" % mid), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("units", len(units), {k: len(v) for k, v in sorted(by.items())},
          "pairs", sum(u["kind"] == "pair" for u in units), "worked", sum(u["kind"] == "worked" for u in units))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
