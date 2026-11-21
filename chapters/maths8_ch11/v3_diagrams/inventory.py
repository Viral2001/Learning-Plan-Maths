# -*- coding: utf-8 -*-
"""Inventory of every question / solution / worked-example item of the live Class 8 Ch 11 plan (V2 v31).

    python -I -X utf8 inventory.py <live plan.json> <out dir>

Writes <out dir>/inventory.json (all units, LP order), <out dir>/in_<chunk>.json (one file per chunk A-D, the chunks the
diagram-identification agents work on) and <out dir>/concept_images.json (the teaching images that already exist).
Read-only on the plan.

A "unit" is one book question as the plan holds it:
  pair     a Questions-topic question concept (qt_part=question) and its answer concept (qt_part=answer)
  single   ONE concept that holds both the question card (image_media_id) and the solution card (solution_image_media_id)
           and whose own question / steps / answer text is EMPTY (the 'Figure it Out' topics of this chapter). The question,
           steps and answer text of such a question sit in a 'Practice: ...' block of a TEACHING concept (the block's
           video_media_id is the single's video): that block is attached to the single as `lp_text` and is NOT a unit of its own.
  worked   a worked-example block that lives inside a teaching concept (question + steps + answer in one block);
           a concept with several blocks gives one unit per block (block_index)
"""
import json
import os
import sys


def short(s, n=None):
    return s if n is None or len(s) <= n else s[:n] + "..."


def item_view(it):
    keep = ("question", "question_tex", "steps_tex", "answer_tex", "steps", "answer", "text", "q_figure",
            "s_figure", "book_number", "item_kind", "ncert_refs", "image_media_id", "solution_image_media_id",
            "solution_image_media_ids", "video_media_id", "example_id")
    return {k: it[k] for k in keep if k in it and it[k] not in (None, "", [])}


# chunk -> topic id prefixes (module.segment). Balanced by number of items; set after looking at the counts.
CHUNKS = {
    "A": ["M1"],
    "B": ["M2.S10", "M2.S11", "M2.S12", "M2.S13", "M2.S14", "M2.S15", "M2.S16"],
    "C": ["M2.S17", "M2.S18", "M2.S19", "M2.S20", "M3.S21", "M3.S22", "M3.S23", "M3.S24"],
    "D": ["M3.S25", "M3.S26", "M3.S27", "M3.S28", "M3.S29", "M3.S30", "M3.S31"],
}


def chunk_of(topic_id):
    mod, seg = topic_id.split(".")[0], ".".join(topic_id.split(".")[:2])
    for k, prefixes in CHUNKS.items():
        for pre in prefixes:
            if pre == mod or pre == seg:
                return k
    raise KeyError(topic_id)


def media_by_id(t):
    return {md["id"]: md for md in t.get("media", [])}


def video_view(md):
    if not md:
        return None
    vs = md.get("video_script") or {}
    return {"id": md["id"], "title": md.get("title"), "description": short(md.get("description") or "", 700),
            "serves_items": md.get("serves_items"), "anchor": vs.get("anchor"), "maths_rules": vs.get("maths_rules"),
            "final_answer": vs.get("final_answer"), "source": vs.get("source"), "open_questions": vs.get("open_questions"),
            "hold_back": vs.get("hold_back")}


def card_view(md):
    if not md:
        return None
    return {"id": md["id"], "title": md.get("title"), "description": short(md.get("description") or "", 900),
            "aspect_ratio": md.get("aspect_ratio")}


def main(plan_path, out_dir):
    plan = json.load(open(plan_path, encoding="utf-8"))
    os.makedirs(out_dir, exist_ok=True)
    units, cimgs = [], []
    # pre-pass: singles' videos -> the 'Practice' block of a teaching concept that carries their text
    single_videos = set()
    for m in plan["modules"]:
        for s in m["segments"]:
            for t in s["topics"]:
                for c in t["concepts"]:
                    for it in c.get("content", []):
                        if "question" in it and it.get("image_media_id") and it.get("solution_image_media_id") and it.get("video_media_id"):
                            single_videos.add(it["video_media_id"])
    practice = {}
    for m in plan["modules"]:
        for s in m["segments"]:
            for t in s["topics"]:
                tm = media_by_id(t)
                for md in t.get("media", []):
                    if md.get("type") == "image" and not md.get("image_role"):
                        cimgs.append({"id": md["id"], "topic_id": t["topic_id"], "topic_name": t["topic_name"],
                                      "concept_id": md.get("concept_id"), "title": md.get("title"), "labels": md.get("labels"),
                                      "description": short(md.get("description") or "", 700)})
                cons = t["concepts"]
                i = 0
                while i < len(cons):
                    c = cons[i]
                    qitems = [it for it in c.get("content", []) if "question" in it]
                    if not qitems:
                        i += 1
                        continue
                    part = c.get("qt_part")
                    base = {"module_id": m["module_id"], "topic_id": t["topic_id"], "topic_name": t["topic_name"]}
                    if part == "question":
                        a = cons[i + 1] if i + 1 < len(cons) else None
                        assert a is not None and a.get("qt_part") == "answer", c["concept_id"]
                        ai = [it for it in a["content"] if "question" in it]
                        assert len(qitems) == 1 and len(ai) == 1, c["concept_id"]
                        units.append(dict(base, unit=len(units) + 1, kind="pair",
                                          question_concept={"concept_id": c["concept_id"], "name": c.get("concept_name"),
                                                            "item": item_view(qitems[0])},
                                          answer_concept={"concept_id": a["concept_id"], "name": a.get("concept_name"),
                                                          "media_ids": a.get("media_ids"), "item": item_view(ai[0])},
                                          ncert_refs=c.get("ncert_refs")))
                        i += 2
                        continue
                    assert part != "answer", "orphan answer %s" % c["concept_id"]
                    for k, it in enumerate(qitems):
                        if it.get("video_media_id") in single_videos and not it.get("image_media_id"):
                            practice[it["video_media_id"]] = {"concept_id": c["concept_id"], "concept_name": c.get("concept_name"),
                                                              "block_index": k, "item": item_view(it)}
                            continue          # text side of a single: not a unit of its own
                        if it.get("image_media_id") and it.get("solution_image_media_id"):
                            # single: question + solution card on one concept, no text
                            assert len(qitems) == 1, c["concept_id"]
                            vid = tm.get(it.get("video_media_id"))
                            units.append(dict(base, unit=len(units) + 1, kind="single", concept_id=c["concept_id"],
                                              concept_name=c.get("concept_name"), ncert_refs=c.get("ncert_refs"),
                                              item=item_view(it), question_card=card_view(tm.get(it["image_media_id"])),
                                              solution_card=card_view(tm.get(it["solution_image_media_id"])),
                                              video=video_view(vid), existing_concept_media_ids=c.get("media_ids")))
                        else:
                            units.append(dict(base, unit=len(units) + 1, kind="worked", concept_id=c["concept_id"],
                                              concept_name=c.get("concept_name"), block_index=k, blocks_in_concept=len(qitems),
                                              ncert_refs=c.get("ncert_refs"), item=item_view(it),
                                              existing_concept_media_ids=c.get("media_ids")))
                    i += 1
    for u in units:
        if u["kind"] == "single":
            u["lp_text"] = practice[u["video"]["id"]]         # KeyError = a single without its practice block: stop
    assert len(practice) == len(single_videos), (len(practice), len(single_videos))
    json.dump(units, open(os.path.join(out_dir, "inventory.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(cimgs, open(os.path.join(out_dir, "concept_images.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    by = {}
    for u in units:
        by.setdefault(chunk_of(u["topic_id"]), []).append(u)
    for cid, us in sorted(by.items()):
        json.dump(us, open(os.path.join(out_dir, "in_%s.json" % cid), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    def items_of(u):
        return 2 if u["kind"] in ("pair", "single") else 1
    print("units", len(units), "| pairs", sum(u["kind"] == "pair" for u in units), "singles", sum(u["kind"] == "single" for u in units),
          "worked", sum(u["kind"] == "worked" for u in units), "| items", sum(items_of(u) for u in units),
          "| concept images", len(cimgs))
    for k, us in sorted(by.items()):
        print("  chunk", k, "units", len(us), "items", sum(items_of(u) for u in us))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
