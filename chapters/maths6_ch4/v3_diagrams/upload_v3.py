# -*- coding: utf-8 -*-
"""Upload the built V3 plan of Class 6 Ch 4 to STAGING, read it back and compare.

    python -I -X utf8 upload_v3.py <plan.json>          dry run: shows what would happen, sends nothing
    python -I -X utf8 upload_v3.py <plan.json> --go     send it
    ... --overwrite-active --expect <file.json>         also allow replacing an ACTIVE version of the same number (the user asked
                                                        for this on 21 Nov 2026: same version, no new version); only if the live
                                                        plan is still identical to <file.json> (what was uploaded before)

Why not upload/upload_lp.py: it only sends phase 2 and needs a validate_local stamp (phase 2 only). This script reuses its
multipart `post` helper and sends the same form fields (chapter_master_id, phase). The user approved the stamp skip for this
plan (Class 6 Ch 4, 21 Nov 2026: "copy V2 latest to V3, modify, make it active"; new V3 chapter, version 1, active). Staging only.

If the plan's version already exists on the server it is OVERWRITTEN in place (force=true, the server's own switch for
"overwrite the single matching version"); the old content is first saved to source/<plan_id>_overwritten_backup.json.
replace_all is never used (it deletes every version of the chapter).
"""
import importlib.util
import json
import os
import sys
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
BASE = "https://staging.singularity-learn.com"
API = BASE + "/agentapi/api/lp2/learning-plans/chapter/"
V3_ID, MASTER, PHASE = "cbse_eng_maths6_ch4_V3", 188, 3


def get(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return json.load(r)


def plan_of(version):
    p = get(API + V3_ID + "?version=%d" % version)["data"]["plan"]
    pj = p["planJson"]
    return (json.loads(pj) if isinstance(pj, str) else pj), p


def main():
    path = sys.argv[1]
    go = "--go" in sys.argv[2:]
    plan = json.load(open(path, encoding="utf-8"))
    assert plan["chapter_id"] == V3_ID and plan["phase"] == PHASE and plan["chapter_master_id"] == MASTER, "wrong chapter/phase/master"
    ver = plan["version"]
    assert plan["plan_id"] == "%s_v%d" % (V3_ID, ver)
    try:
        versions = get(API + V3_ID + "/versions")["data"]
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise
        versions = []
        print("NOTE: the server does not know the chapter %s yet (404): this upload tries to create it" % V3_ID)
    by = {v["version"]: v for v in versions}
    print("V3 versions now:", [(v["version"], v["status"]) for v in versions[:4]])
    exists = ver in by
    active_ok = "--overwrite-active" in sys.argv[2:]
    if exists and by[ver]["status"] != "draft":
        if not active_ok:
            raise SystemExit("version %d exists and is %s, not a draft: refusing to overwrite it (needs --overwrite-active --expect <file>)" % (ver, by[ver]["status"]))
        if "--expect" not in sys.argv[2:]:
            raise SystemExit("--overwrite-active needs --expect <the plan file that was uploaded before>")
        expected = json.load(open(sys.argv[sys.argv.index("--expect") + 1], encoding="utf-8"))
        live_now, _ = plan_of(ver)
        if live_now != expected:
            raise SystemExit("the live v%d differs from the --expect file: someone changed it since; refusing to overwrite" % ver)
        print("live v%d is identical to the --expect file: nobody changed it since" % ver)
    nxt = max(by, default=0) + 1
    if not exists and ver != nxt:
        raise SystemExit("version %d is neither an existing draft nor max+1 (%d)" % (ver, nxt))
    if not by:
        print("NOTE: %s has no version on staging yet: this upload creates the chapter's first version (v%d)" % (V3_ID, ver))
    print("target v%d: %s" % (ver, "OVERWRITE the existing %s version in place (force=true)" % by[ver]["status"] if exists else "new version"))
    others = [v["version"] for v in versions if v["isActive"] and v["version"] != ver]
    print("activate=true: v%d stays/becomes the active one%s" % (ver, "; the active version %s will be archived" % others if others else ""))
    if not go:
        print("dry run, nothing sent")
        return
    if exists:
        old, meta = plan_of(ver)
        bp = os.path.join(HERE, "source", "%s_overwritten_backup.json" % plan["plan_id"])
        if os.path.exists(bp):
            bp = bp.replace(".json", "_%s.json" % time.strftime("%Y%m%d_%H%M%S"))
        json.dump(old, open(bp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("backup of the draft:", bp, meta.get("createdAt"))
    spec = importlib.util.spec_from_file_location("upload_lp", os.path.join(ROOT, "upload", "upload_lp.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    url = BASE + m.PATH + "?activate=true" + ("&force=true" if exists else "")
    print("POST", url)
    status, text, sent = m.post(url, path, {"chapter_master_id": str(MASTER), "phase": str(PHASE)}, 600)
    print("http", status, "sent MB", round(sent / 1048576, 2))
    a = json.loads(text)
    print(json.dumps({k: a[k] for k in a if k != "diff"}, ensure_ascii=False)[:1200])
    if status >= 400 or not a.get("success") or a.get("validation_errors"):
        raise SystemExit("upload failed")
    live, meta = plan_of(ver)
    print("meta:", {k: meta[k] for k in meta if k != "planJson"})
    print("read-back identical to the local file:", live == plan)
    after = get(API + V3_ID + "/versions")["data"]
    print("V3 versions after:", [(v["version"], v["status"], v["isActive"]) for v in after[:4]], "| rows for v%d: %d" % (ver, sum(v["version"] == ver for v in after)))


if __name__ == "__main__":
    main()
