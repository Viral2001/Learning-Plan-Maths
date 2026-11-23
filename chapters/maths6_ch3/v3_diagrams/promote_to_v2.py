# -*- coding: utf-8 -*-
"""Promote the V3 plan of Class 6 Ch 3 Number Play (cbse_eng_maths6_ch3_V3, v18: 32 built DIAGRAM images) to the V2 flow as a NEW
version of cbse_eng_maths6_ch3 (phase 2, v109), carrying every media forward. STAGING only.

    python -I -X utf8 promote_to_v2.py          build + check + write out/cbse_eng_maths6_ch3_v109.json, send nothing
    python -I -X utf8 promote_to_v2.py --go     also upload it ACTIVE (stamp skipped: the phase-2 gate 'every question has a
                                                question card and a solution card' fails by design), read back and compare

User decisions (23 Nov 2026): tokens {{DIAGRAM:<id>}} stay in the text; upload ACTIVE v109 with the stamp skipped.

What it does: takes the LIVE V3 v18 plan and relabels it (chapter_id cbse_eng_maths6_ch3, phase 2, version 109, plan_id
cbse_eng_maths6_ch3_v109, master id 187 unchanged). Nothing else is edited. It refuses to continue unless:
  * V2's newest version is still 108 and the live v108 equals source/cbse_eng_maths6_ch3_v108.json (nobody changed V2),
  * V3's newest version is 18 (active),
  * the result differs from V2 v108 only in expected places: the old card nodes (all unbuilt placeholders) replaced by the 32
    built DIAGRAM nodes, the links/tokens that go with them, media_ids of the concepts, summary_stats, source_metadata;
  * every V2 video, tool and concept (teaching) image is byte-identical in v109 (same node, same content, same topic);
  * every DIAGRAM node equals the live V3 v18 node (built, url, size fields, description fixes included).
"""
import copy
import importlib.util
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
BASE = "https://staging.singularity-learn.com"
API = BASE + "/agentapi/api/lp2/learning-plans/chapter/"
V2_ID, V3_ID, MASTER = "cbse_eng_maths6_ch3", "cbse_eng_maths6_ch3_V3", 187
V2_BASE_VERSION, V3_VERSION, NEW_VERSION = 108, 18, 109
OUT = os.path.join(HERE, "out", "cbse_eng_maths6_ch3_v109.json")
DIAGRAM = "DIAGRAM · "


def get(path):
    with urllib.request.urlopen(API + path, timeout=180) as r:
        return json.load(r)["data"]


def plan_of(cid, ver):
    p = get("%s?version=%d" % (cid, ver))["plan"]
    pj = p["planJson"]
    return (json.loads(pj) if isinstance(pj, str) else pj), p


def topics_of(plan):
    return [t for m in plan["modules"] for s in m["segments"] for t in s["topics"]]


def media_of(plan):
    return {md["id"]: (t["topic_id"], md) for t in topics_of(plan) for md in t["media"]}


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


OK_PATHS = re.compile(
    r"^(/chapter_id|/phase|/version|/plan_id|/_activate"
    r"|/source_metadata/(summary_stats/images|summary_stats/diagram_placeholders|diagram_v3|promoted_from_v3)"
    r"|/modules\[\d+\]/segments\[\d+\]/topics\[\d+\](/media(\[.*)?"
    r"|/concepts\[\d+\](/media_ids(\[.*)?|/content\[\d+\]/(image_media_id|solution_image_media_ids?|question_tex|steps_tex(\[\d+\])?|text|publication_text|answer_tex))))$")


def build():
    versions = get(V2_ID + "/versions")
    v2_max = max(v["version"] for v in versions)
    if v2_max != V2_BASE_VERSION:
        raise SystemExit("V2 newest version is %d, not %d: someone added a version, stop and re-plan" % (v2_max, V2_BASE_VERSION))
    v2, v2meta = plan_of(V2_ID, V2_BASE_VERSION)
    saved = json.load(open(os.path.join(HERE, "source", "cbse_eng_maths6_ch3_v108.json"), encoding="utf-8"))
    if v2 != saved:
        raise SystemExit("live V2 v108 differs from source/cbse_eng_maths6_ch3_v108.json: V2 was edited, stop")
    if not v2meta["isActive"]:
        raise SystemExit("V2 v108 is not the active version any more, stop")
    v3versions = get(V3_ID + "/versions")
    if max(v["version"] for v in v3versions) != V3_VERSION:
        raise SystemExit("V3 newest version is not %d, stop" % V3_VERSION)
    v3, v3meta = plan_of(V3_ID, V3_VERSION)

    plan = copy.deepcopy(v3)
    plan["chapter_id"], plan["phase"], plan["version"] = V2_ID, 2, NEW_VERSION
    plan["plan_id"] = "%s_v%d" % (V2_ID, NEW_VERSION)
    plan["_activate"] = True
    assert plan["chapter_master_id"] == MASTER
    plan["source_metadata"]["promoted_from_v3"] = {
        "from": "%s_v%d (built DIAGRAM images)" % (V3_ID, V3_VERSION),
        "on": "2026-11-23",
        "note": "V3 promoted to the V2 flow as a new version. The 149 unbuilt question/solution card placeholders of v108 are replaced by the "
                "32 built DIAGRAM images of V3 v18 (tokens {{DIAGRAM:<id>}} kept in the text). Videos, tools and concept images "
                "are identical to v108.",
    }
    check(plan, v2, v3)
    return plan, v2, v3


def check(plan, v2, v3):
    errs = []
    m2, mn, m3 = media_of(v2), media_of(plan), media_of(v3)
    # 1. nothing made in V2 is lost: videos, tools, concept images identical, same topic
    kept = 0
    for k, (tid, md) in m2.items():
        is_card = md.get("type") == "image" and md.get("image_role") in ("question", "solution")
        if is_card:
            if md.get("build_status") != "placeholder":
                errs.append("V2 card %s is %s, not a placeholder: it would be lost" % (k, md.get("build_status")))
            continue
        if k not in mn:
            errs.append("V2 media %s (%s) missing from v109" % (k, md.get("type")))
        elif mn[k] != (tid, md):
            errs.append("V2 media %s changed or moved" % k)
        else:
            kept += 1
    # 2. everything new is a built V3 diagram, identical to V3 v18
    diagrams = 0
    for k, (tid, md) in mn.items():
        if k in m2 and not (m2[k][1].get("image_role") in ("question", "solution")):
            continue
        if not md["title"].startswith(DIAGRAM) or md.get("build_status") != "built":
            errs.append("node %s is not a built DIAGRAM node" % k)
        if k not in m3 or m3[k] != (tid, md):
            errs.append("diagram %s differs from V3 v18" % k)
        diagrams += 1
    for k, (tid, md) in m3.items():
        if md["title"].startswith(DIAGRAM) and k not in mn:
            errs.append("V3 diagram %s is missing from v109" % k)
    # 3. links and tokens
    s = json.dumps(plan, ensure_ascii=False)
    cons = {c["concept_id"]: c for t in topics_of(plan) for c in t["concepts"]}
    for t in topics_of(plan):
        ids = {md["id"] for md in t["media"]}
        for c in t["concepts"]:
            for x in c.get("media_ids", []):
                if x not in ids:
                    errs.append("%s media_ids %s has no node in its topic" % (c["concept_id"], x))
            for b in c.get("content", []):
                for f in ("image_media_id", "solution_image_media_id", "video_media_id"):
                    x = b.get(f)
                    if x and f != "video_media_id" and (x not in ids or x not in c.get("media_ids", [])):
                        errs.append("%s %s=%s not in the topic / media_ids" % (c["concept_id"], f, x))
    for k, (tid, md) in mn.items():
        if md["title"].startswith(DIAGRAM) and "{{DIAGRAM:%s}}" % k not in s:
            errs.append("token of %s not in the text" % k)
    # 4. nothing else changed against V2 v108
    changed = diff_paths(v2, plan)
    bad = [p for p in changed if not OK_PATHS.match(p)]
    if bad:
        errs.append("unexpected changes against v108: %s" % bad[:10])
    # 5. the only V2 nodes gone are unbuilt cards
    gone = [k for k in m2 if k not in mn]
    if any(m2[k][1].get("image_role") not in ("question", "solution") for k in gone):
        errs.append("a non-card node of V2 is gone")
    if errs:
        print("\n".join("ERROR " + e for e in errs[:40]))
        raise SystemExit("%d integrity errors" % len(errs))
    print("checks ok: %d V2 videos/tools/concept images identical and in place; %d built DIAGRAM nodes identical to V3 v18; "
          "%d unbuilt V2 card placeholders gone (%d of them replaced by a diagram with the same id); %d changed paths, all expected"
          % (kept, diagrams, len(gone), sum(1 for k in m2 if k in mn and m2[k][1].get("image_role") in ("question", "solution")), len(changed)))
    print("   videos %d, tools %d, concept images %d, diagram images %d, tokens in text %d"
          % (sum(1 for _, (t, md) in mn.items() if md["type"] == "video"), sum(1 for _, (t, md) in mn.items() if md["type"] == "2d_tool"),
             sum(1 for _, (t, md) in mn.items() if md["type"] == "image" and not md.get("image_role")), diagrams, s.count("{{DIAGRAM:")))


def main():
    go = "--go" in sys.argv[1:]
    plan, v2, v3 = build()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(plan, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", OUT)
    if not go:
        print("dry run, nothing sent (V2 v%d stays the live plan)" % V2_BASE_VERSION)
        return
    spec = importlib.util.spec_from_file_location("upload_lp", os.path.join(ROOT, "upload", "upload_lp.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    url = BASE + m.PATH + "?activate=true"
    print("POST", url)
    status, text, sent = m.post(url, OUT, {"chapter_master_id": str(MASTER), "phase": "2"}, 600)
    print("http", status, "sent MB", round(sent / 1048576, 2))
    a = json.loads(text)
    print(json.dumps({k: a[k] for k in a if k != "diff"}, ensure_ascii=False)[:1200])
    if status >= 400 or not a.get("success") or a.get("validation_errors"):
        raise SystemExit("upload failed")
    live, meta = plan_of(V2_ID, NEW_VERSION)
    print("meta:", {k: meta[k] for k in meta if k != "planJson"})
    print("read-back identical to the local file:", live == plan)
    after = get(V2_ID + "/versions")
    print("V2 versions after:", [(v["version"], v["status"], v["isActive"]) for v in after[:3]])
    v3_after, _ = plan_of(V3_ID, V3_VERSION)
    print("V3 v18 untouched:", v3_after == v3)
    old, _ = plan_of(V2_ID, V2_BASE_VERSION)
    print("V2 v108 (now archived) still identical to the saved copy:", old == v2)


if __name__ == "__main__":
    main()
