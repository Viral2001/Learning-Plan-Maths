"""Checks for a built Class 10 plan.  Usage: python -I -X utf8 check_std10_lp.py <chapter> [<chapter> ...]"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEAK = re.compile(r"\b(Fig|Figure|Table|Theorem|Example|Exercise|Section|Chapter|Appendix)\.?\s*\d|NCERT|textbook|"
                  r"\[authored\]|please check|renamed at build|Predict first|On the board", re.I)


def student_strings(plan):
    for m in plan["modules"]:
        yield "module", m["module_name"]
        for s in m["segments"]:
            yield "segment", s["segment_name"]
            for t in s["topics"]:
                yield "topic", t["topic_name"]
                for c in t["concepts"]:
                    yield c["concept_id"] + " name", c["concept_name"]
                    for b in c["content"]:
                        yield c["concept_id"] + " " + b["block_kind"], b["text"]
                for x in t["media"]:
                    yield x["id"] + " title", x.get("title", "")
    for o in plan["objectives"]:
        yield o["objective_id"], o["objective_text"]


def check(n):
    fol = os.path.join(ROOT, f"std10_ch{n}")
    old = json.load(open(os.path.join(fol, f"learning_plan_std10_chap{n}_version1.json"), encoding="utf8"))
    new = json.load(open(os.path.join(fol, f"learning_plan_std10_chap{n}_version2.json"), encoding="utf8"))
    bad = []
    # media identity
    old_ids = {x["id"] for m in old["modules"] for s in m["segments"] for t in s["topics"] for x in t.get("media", [])}
    att = {x["old_media_id"] for m in new["modules"] for s in m["segments"] for t in s["topics"] for x in t["media"]
           if x.get("old_media_id")}
    h = new["source_metadata"]["held_assets"]
    held = {x["old_media_id"] for v in h.values() for x in v}
    if old_ids != att | held or att & held:
        bad.append(f"media identity: missing {old_ids - att - held}, overlap {att & held}")
    tools = {x["id"] for m in old["modules"] for s in m["segments"] for t in s["topics"] for x in t.get("media", [])
             if x["type"] not in ("image", "video")}
    if tools - {x["old_media_id"] for x in h["tools"]}:
        bad.append("a tool is not held")
    if any(x["type"] not in ("image", "video") for m in new["modules"] for s in m["segments"] for t in s["topics"]
           for x in t["media"]):
        bad.append("a tool is attached")
    # objectives
    for o in new["objectives"]:
        cs = [c for m in new["modules"] for s in m["segments"] for t in s["topics"] for c in t["concepts"]
              if o["objective_id"] in c["objective_ids"]]
        if not cs or any(c["is_enrichment"] for c in cs):
            bad.append(f"objective {o['objective_id']} not anchored on a non-enrichment concept")
    for m in new["modules"]:
        for s in m["segments"]:
            for t in s["topics"]:
                for c in t["concepts"]:
                    if not c["media_ids"]:
                        bad.append(f"concept {c['concept_id']} has no media")
                    if c["is_enrichment"] and (c["objective_id"] or c["objective_ids"]):
                        bad.append(f"enrichment {c['concept_id']} has an objective")
                    if c["concept_kind"] == "exercise" and c["content"][0]["block_kind"] == "exercise_question":
                        vids = [x for x in t["media"] if x["concept_id"] == c["concept_id"] and x["type"] == "video"]
                        imgs = [x for x in t["media"] if x["concept_id"] == c["concept_id"] and x["type"] == "image"]
                        if vids or len(imgs) != 1:
                            bad.append(f"question {c['concept_id']}: {len(vids)} videos, {len(imgs)} images")
    # leaks, groups
    leaks = [(w, s[:80]) for w, s in student_strings(new) if LEAK.search(s)]
    txt = json.dumps(new)
    if '"group"' in txt or "question_groups" in txt:
        bad.append("group keys remain")
    ncert_media = sum(1 for m in new["modules"] for s in m["segments"] for t in s["topics"] for x in t["media"]
                      if x.get("old_media_id") and re.search(r"ncert|textbook", json.dumps(x), re.I))
    st = new["source_metadata"]["summary_stats"]
    print(f"Ch{n}: {st} | attached {len(att)} held {len(held)} of {len(old_ids)} old media")
    print("  problems:", bad or "none")
    print(f"  leak hits in student-facing strings: {len(leaks)}")
    for w, s in leaks[:25]:
        print("   ", w, "|", s)
    print(f"  re-homed media whose own fields mention NCERT/textbook (rule 10, report only): {ncert_media}")


for a in sys.argv[1:]:
    check(int(a))
