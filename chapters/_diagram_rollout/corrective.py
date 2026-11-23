# -*- coding: utf-8 -*-
"""Corrective new version of a chapter that rollout.py already uploaded, after its decision files were audited
(user decisions of 23 Nov 2026: book slips -> corrected value, figure letters only where the LP answer uses them).

    python -I -X utf8 corrective.py <class> <chapter>          dry run: check, rebuild, diff, send nothing
    python -I -X utf8 corrective.py <class> <chapter> --go     also upload as the next version (ACTIVE), read back, verify

What it does, in order (it stops, and says why, at the first failed check):
 1. live newest version == the version rollout.py uploaded (meta target_version) and it is the active one;
 2. live plan of that version == out/<cid>_v<U>.json, the file rollout.py uploaded (nobody edited it in place);
 3. re-runs merge + build from the ORIGINAL base snapshot with the audited out_*.json files;
 4. the rebuilt plan differs from the live plan ONLY inside DIAGRAM media nodes (spec / description fields) - no text, link,
    token, concept image, video or tool changes;
 5. uploads the rebuilt plan as version U+1 (activate, no force), reads it back (identical), checks v<U> is still identical.
Files: out/<cid>_v<U>.json stays the uploaded plan, out/<cid>_v<U>.rebuilt.json is the rebuild, out/<cid>_v<U+1>.json is what was sent.
"""
import copy
import importlib.util
import json
import os
import re
import sys

HERE_TOOLS = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("rollout", os.path.join(HERE_TOOLS, "rollout.py"))
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    go = "--go" in sys.argv[1:]
    c, n = int(args[0]), int(args[1])
    H = R.here(c, n)
    meta = R.load(os.path.join(H, "meta.json"))
    cid = meta["chapter_id"]
    T = meta["target_version"]                           # the version rollout.py uploaded; build() always writes out/<cid>_v<T>.json
    st = R.load(os.path.join(R.HERE_TOOLS, "STATUS.json"))
    if st.get(cid, {}).get("uploaded_version") != T:
        raise SystemExit("STATUS.json does not say v%d of %s was uploaded by rollout.py: stop" % (T, cid))
    U = st[cid].get("corrective_version", T)             # the newest version WE uploaded (an earlier corrective, or the first upload)
    build_path = os.path.join(H, "out", "%s_v%d.json" % (cid, T))
    first_copy = os.path.join(H, "out", "%s_v%d.uploaded.json" % (cid, T))
    if U == T:
        uploaded_path = build_path
        if not os.path.exists(first_copy):
            R.dump(R.load(build_path), first_copy)
    else:
        uploaded_path = os.path.join(H, "out", "%s_v%d.json" % (cid, U))   # what the last corrective sent
        if st[cid].get("corrective_ok") is not True:
            raise SystemExit("%s: the last corrective v%d was not verified: stop" % (cid, U))
    # 1. versions
    versions = R.get(cid + "/versions")
    newest = max(v["version"] for v in versions)
    act = [v["version"] for v in versions if v["isActive"]]
    if newest != U or act != [U]:
        raise SystemExit("%s: newest is v%d, active %s; expected v%d newest and active: someone added a version, stop and ask" % (cid, newest, act, U))
    # 2. live == what we uploaded
    uploaded = R.load(uploaded_path)
    live, _ = R.plan_of(cid, U)
    if live != uploaded:
        paths = R.diff_paths(uploaded, live)
        raise SystemExit("%s: live v%d differs from the file we uploaded (%d paths, e.g. %s): edited in place, stop and ask" % (cid, U, len(paths), paths[:3]))
    # 3. rebuild from the original base with the audited maps (build() writes out/<cid>_v<T>.json)
    R.merge(c, n)
    R.build(c, n)
    rebuilt = R.load(build_path)
    R.dump(rebuilt, os.path.join(H, "out", "%s_v%d.rebuilt.json" % (cid, T)))
    R.dump(R.load(first_copy) if os.path.exists(first_copy) else uploaded, build_path)   # put the first uploaded plan back
    # 4. the rebuild may differ from the live plan ONLY by diagram work: DIAGRAM nodes (changed, added, removed), the links
    #    to them and their {{DIAGRAM:..}} tokens. Strip all of that from both plans: what remains must be identical.
    paths = R.diff_paths(uploaded, rebuilt)

    def dnodes(plan):
        return {md["id"]: md for t in R.topics_of(plan) for md in t["media"] if str(md.get("title", "")).startswith(R.DIAGRAM)}
    du, dr = dnodes(uploaded), dnodes(rebuilt)
    diag = set(du) | set(dr)
    TOK = re.compile(r"\{\{DIAGRAM:[^}]*\}\}")
    DROP_TOP = ("version", "plan_id", "_activate")

    def norm(o, key=None):
        if isinstance(o, dict):
            out = {}
            for k, v in o.items():
                if isinstance(v, str) and v in diag:
                    continue                                     # a link to a DIAGRAM node
                if k == "media" and isinstance(v, list):
                    v = [x for x in v if not str(x.get("title", "")).startswith(R.DIAGRAM)]
                out[k] = norm(v, k)
            return out
        if isinstance(o, list):
            return [norm(x) for x in o if not (isinstance(x, str) and x in diag)]
        if isinstance(o, str):
            return re.sub(r"\s+", "", TOK.sub("", o))
        return o

    def stripped(plan):
        p = copy.deepcopy(plan)
        for k in DROP_TOP:
            p.pop(k, None)
        sm = p.get("source_metadata")
        if isinstance(sm, dict):
            sm.pop("diagram_v3", None)
            ss = sm.get("summary_stats")
            if isinstance(ss, dict):
                ss.pop("images", None)
                ss.pop("diagram_placeholders", None)
        return norm(p)
    nu, nr = stripped(uploaded), stripped(rebuilt)
    if nu != nr:
        rest = R.diff_paths(nu, nr)
        raise SystemExit("%s: the rebuild differs from the live plan beyond diagram work (%d paths, e.g. %s): stop and ask" % (cid, len(rest), rest[:4]))
    added = sorted(set(dr) - set(du))
    removed = sorted(set(du) - set(dr))
    changed = sorted(k for k in set(du) & set(dr) if du[k] != dr[k])
    print("%s: DIAGRAM nodes %d changed, %d added, %d removed (%d paths); after stripping diagram nodes, links and tokens the rebuild equals live v%d"
          % (cid, len(changed), len(added), len(removed), len(paths), U))
    if added:
        print("   added:", ", ".join(added[:20]))
    if removed:
        print("   removed:", ", ".join(removed[:20]))
    if not paths:
        print("nothing to correct: no new version needed")
        return
    new_v = U + 1
    plan = copy.deepcopy(rebuilt)
    plan["version"] = new_v
    plan["plan_id"] = "%s_v%d" % (cid, new_v)
    plan["_activate"] = True
    out_new = os.path.join(H, "out", "%s_v%d.json" % (cid, new_v))
    R.dump(plan, out_new)
    print("wrote", out_new, "| dry run" if not go else "")
    if not go:
        return
    spec2 = importlib.util.spec_from_file_location("upload_lp", os.path.join(R.ROOT, "upload", "upload_lp.py"))
    m = importlib.util.module_from_spec(spec2)
    spec2.loader.exec_module(m)
    url = R.BASE + m.PATH + "?activate=true"
    status, text, sent = m.post(url, out_new, {"chapter_master_id": str(meta["master"]), "phase": "2"}, 900)
    a = json.loads(text)
    print("http", status, "sent MB", round(sent / 1048576, 2), json.dumps({k: a[k] for k in a if k != "diff"}, ensure_ascii=False)[:600])
    if status >= 400 or not a.get("success") or a.get("validation_errors"):
        raise SystemExit("UPLOAD FAILED: %s" % json.dumps(a.get("validation_errors"))[:800])
    back, pm = R.plan_of(cid, new_v)
    prev, _ = R.plan_of(cid, U)
    ok = (back == plan, bool(pm.get("isActive")), prev == uploaded)
    print("read-back identical: %s | v%d active: %s | previous v%d still identical: %s" % (ok[0], new_v, ok[1], U, ok[2]))
    S = R.load(os.path.join(R.HERE_TOOLS, "STATUS.json"))
    S[cid]["corrective_version"] = new_v
    S[cid]["corrective_ok"] = all(ok)
    R.dump(S, os.path.join(R.HERE_TOOLS, "STATUS.json"))
    if not all(ok):
        raise SystemExit("post-upload verification FAILED: stop and ask")


if __name__ == "__main__":
    main()
