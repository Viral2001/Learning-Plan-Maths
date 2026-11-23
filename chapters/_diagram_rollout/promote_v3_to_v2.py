# -*- coding: utf-8 -*-
"""Promote the V3 plan made from V2 (cbse_eng_maths<c>_ch<n>_V3) back to the V2 flow as a NEW ACTIVE version of cbse_eng_maths<c>_ch<n>
(phase 2), carrying every media forward. STAGING only. Generic version of chapters/maths6_ch3/v3_diagrams/promote_to_v2.py.

    python -I -X utf8 promote_v3_to_v2.py <class> <chapter>          build + check + write out file, send nothing
    python -I -X utf8 promote_v3_to_v2.py <class> <chapter> --go     also upload it ACTIVE (stamp skipped), read back, compare

User decisions (23 Nov 2026): the new LPs made in V3 from V2 must come back to V2 as ACTIVE, no media loss; tokens {{DIAGRAM:<id>}} stay;
stamp skipped (the phase-2 gate 'every question has a card' fails by design). It relabels the LIVE V3 plan (chapter_id, phase 2, version =
V2 newest + 1, plan_id) and edits nothing else. It refuses unless: V2's newest version is still the active one and equals the saved copy of
V2 from the V3 build (nobody changed V2), V3's newest version is its active one, the result differs from V2 only in the expected places (old
card placeholders replaced by the V3 diagram nodes, their links/tokens, media_ids, summary_stats, source_metadata), every V2 video / tool /
concept image is byte-identical in the new version, every DIAGRAM node equals the live V3 node.
"""
import copy
import importlib.util
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
BASE = "https://staging.singularity-learn.com"
API = BASE + "/agentapi/api/lp2/learning-plans/chapter/"
C, N = int(sys.argv[1]), int(sys.argv[2])
V2_ID = "cbse_eng_maths%d_ch%d" % (C, N)
V3_ID = V2_ID + "_V3"
HERE = os.path.join(ROOT, "chapters", "maths%d_ch%d" % (C, N), "v3_diagrams")
MASTER = V2_BASE_VERSION = V3_VERSION = NEW_VERSION = OUT = None


def init():
    """Versions are worked out from staging: V2 base = V2's newest AND active version, V3 = V3's newest AND active version."""
    global V2_BASE_VERSION, V3_VERSION, NEW_VERSION, OUT
    v2v = get(V2_ID + "/versions")
    V2_BASE_VERSION = max(v["version"] for v in v2v)
    if not [v for v in v2v if v["isActive"] and v["version"] == V2_BASE_VERSION]:
        raise SystemExit("V2's newest version is not its active one: stop and ask")
    v3v = get(V3_ID + "/versions")
    V3_VERSION = max(v["version"] for v in v3v)
    if not [v for v in v3v if v["isActive"] and v["version"] == V3_VERSION]:
        raise SystemExit("V3's newest version is not its active one: stop and ask")
    NEW_VERSION = V2_BASE_VERSION + 1
    OUT = os.path.join(HERE, "out", "%s_v%d.json" % (V2_ID, NEW_VERSION))
DIAGRAM = "DIAGRAM · "


def get(path):
    import time
    for attempt in range(5):
        try:
            with urllib.request.urlopen(API + path, timeout=240) as r:
                return json.load(r)["data"]
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if attempt == 4:
                raise
        except Exception:
            if attempt == 4:
                raise
        time.sleep(5 * (attempt + 1))


def plan_of(cid, ver):
    p = get("%s?version=%d" % (cid, ver))["plan"]
    pj = p["planJson"]
    return (json.loads(pj) if isinstance(pj, str) else pj), p


def node_built(md):
    return md.get("build_status") == "built" or bool(md.get("image_url") or md.get("video_url") or md.get("tool_url") or md.get("html_url"))


def is_card_node(md):
    return md.get("type") == "image" and md.get("image_role") in ("question", "solution")


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


def carry_plan(saved, live):
    """Edits made IN PLACE on the live V2 version since the snapshot the V3 plan was built from. Only edits to fields of existing NON-CARD
    media nodes may be carried (they are copied into the promoted plan, so nothing made in V2 is lost); anything else: stop and ask."""
    paths = diff_paths(saved, live)
    ids = {}
    for pth in paths:
        m = re.match(r"^/modules\[(\d+)\]/segments\[(\d+)\]/topics\[(\d+)\]/media\[(\d+)\]/", pth)
        if not m:
            raise SystemExit("live V2 differs from the snapshot outside media-node fields (%s): stop and ask" % pth)
        mi, si, ti, k = [int(x) for x in m.groups()]
        a = saved["modules"][mi]["segments"][si]["topics"][ti]["media"][k]
        b = live["modules"][mi]["segments"][si]["topics"][ti]["media"][k]
        if a["id"] != b["id"] or is_card_node(a):
            raise SystemExit("live V2 changed a card node or reordered media (%s): stop and ask" % pth)
        ids.setdefault(a["id"], []).append(pth.split("/media[")[1].split("]/", 1)[1])
    return ids


def apply_carry(plan, live, v3, saved, carried):
    live_nodes = {md["id"]: md for t in topics_of(live) for md in t["media"]}
    v3_nodes = {md["id"]: md for t in topics_of(v3) for md in t["media"]}
    saved_nodes = {md["id"]: md for t in topics_of(saved) for md in t["media"]}
    n = 0
    for t in topics_of(plan):
        for i, md in enumerate(t["media"]):
            if md["id"] in carried:
                if v3_nodes.get(md["id"]) != saved_nodes[md["id"]]:
                    raise SystemExit("node %s was edited in V2 AND differs in V3: stop and ask" % md["id"])
                t["media"][i] = copy.deepcopy(live_nodes[md["id"]])
                n += 1
    if n != len(carried):
        raise SystemExit("a node edited in V2 is missing from the V3 plan: stop and ask")


def build():
    init()
    v2, v2meta = plan_of(V2_ID, V2_BASE_VERSION)
    saved = json.load(open(os.path.join(HERE, "source", "%s_v%d.json" % (V2_ID, V2_BASE_VERSION)), encoding="utf-8"))
    carried = carry_plan(saved, v2)       # in-place edits of non-card media nodes made on the live V2 since the V3 was built
    if not v2meta["isActive"]:
        raise SystemExit("V2 v%d is not the active version any more, stop" % V2_BASE_VERSION)
    v3, v3meta = plan_of(V3_ID, V3_VERSION)

    plan = copy.deepcopy(v3)
    plan["chapter_id"], plan["phase"], plan["version"] = V2_ID, 2, NEW_VERSION
    plan["plan_id"] = "%s_v%d" % (V2_ID, NEW_VERSION)
    plan["_activate"] = True
    global MASTER
    MASTER = plan["chapter_master_id"]
    assert MASTER == v2["chapter_master_id"]
    apply_carry(plan, v2, v3, saved, carried)
    if carried:
        print("carried the live V2's newer content of %d non-card media node(s): %s" % (len(carried), {k: v for k, v in carried.items()}))
    plan["source_metadata"]["promoted_from_v3"] = {
        "from": "%s_v%d (DIAGRAM nodes)" % (V3_ID, V3_VERSION),
        "on": "2026-11-23",
        "note": "V3 promoted to the V2 flow as a new version. The %d unbuilt question/solution card placeholders of v%d are replaced by the "
                "%d DIAGRAM nodes of V3 v%d (tokens {{DIAGRAM:<id>}} kept in the text). Videos, tools and concept images "
                "are identical to v%d%s." % (sum(1 for t in topics_of(v2) for md in t["media"] if is_card_node(md)), V2_BASE_VERSION,
                                          sum(1 for t in topics_of(v3) for md in t["media"] if md.get("title", "").startswith(DIAGRAM)),
                                          V3_VERSION, V2_BASE_VERSION,
                                          (" (the live V2's in-place edits of %d media node(s) are carried over: %s)" % (len(carried), ", ".join(sorted(carried)))) if carried else ""),
    }
    check(plan, v2, v3)
    return plan, v2, v3


def check(plan, v2, v3):
    errs = []
    m2, mn, m3 = media_of(v2), media_of(plan), media_of(v3)
    # 1. nothing made in V2 is lost: videos, tools, concept images identical, same topic
    kept = 0
    v3_made = []
    for k, (tid, md) in m2.items():
        is_card = md.get("type") == "image" and md.get("image_role") in ("question", "solution")
        if is_card:
            if md.get("build_status") != "placeholder":
                errs.append("V2 card %s is %s, not a placeholder: it would be lost" % (k, md.get("build_status")))
            continue
        if k not in mn:
            errs.append("V2 media %s (%s) missing from the new version" % (k, md.get("type")))
        elif mn[k] == (tid, md):
            kept += 1
        elif mn[k] == m3.get(k) and not node_built(md) and node_built(m3[k][1]):
            v3_made.append(k)         # media MADE in V3 (the V2 node is an unbuilt placeholder): carried
            kept += 1
        else:
            errs.append("V2 media %s changed, moved or would be downgraded (V2 built: %s)" % (k, node_built(md)))
    # 2. everything new is a built V3 diagram, identical to the live V3 plan
    diagrams = 0
    for k, (tid, md) in mn.items():
        if k in m2 and not (m2[k][1].get("image_role") in ("question", "solution")):
            continue
        if not md["title"].startswith(DIAGRAM):
            errs.append("node %s is not a DIAGRAM node" % k)
        if k not in m3 or m3[k] != (tid, md):
            errs.append("diagram %s differs from the live V3 plan" % k)
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
        errs.append("unexpected changes against the V2 base: %s" % bad[:10])
    # 5. the only V2 nodes gone are unbuilt cards
    gone = [k for k in m2 if k not in mn]
    if any(m2[k][1].get("image_role") not in ("question", "solution") for k in gone):
        errs.append("a non-card node of V2 is gone")
    if errs:
        print("\n".join("ERROR " + e for e in errs[:40]))
        raise SystemExit("%d integrity errors" % len(errs))
    if v3_made:
        print("media MADE in V3 and carried into V2 (V2 had an unbuilt placeholder): %d node(s) %s" % (len(v3_made), sorted(v3_made)[:4]))
    print("checks ok: %d V2 videos/tools/concept images identical or carried and in place; %d built DIAGRAM nodes identical to the live V3 plan; "
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
    print("the V3 plan untouched:", v3_after == v3)
    old, _ = plan_of(V2_ID, V2_BASE_VERSION)
    print("V2 v%d (now archived) still identical to the live base it was built on:" % V2_BASE_VERSION, old == v2)


if __name__ == "__main__":
    main()
