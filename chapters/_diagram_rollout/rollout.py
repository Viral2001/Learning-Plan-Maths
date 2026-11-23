# -*- coding: utf-8 -*-
"""Diagram rollout for ALL Class 5-8 chapters, straight in the V2 flow (user order of 23 Nov 2026, see README.md).

    python -I -X utf8 rollout.py prepare <class> <chapter>      fetch the LIVE plan, book pages, inventory, agent briefs
    python -I -X utf8 rollout.py status  <class> <chapter>      what exists / validates
    python -I -X utf8 rollout.py merge   <class> <chapter>      merge map/out_*.json -> map/diagram_map.json (+ validate)
    python -I -X utf8 rollout.py build   <class> <chapter>      build out/<plan id>.json from the live plan + map, with checks
    python -I -X utf8 rollout.py report  <class> <chapter>      write REPORT.md
    python -I -X utf8 rollout.py upload  <class> <chapter> [--go]   dry run / upload the new V2 version ACTIVE (stamp skipped)

Everything lives in chapters/maths<class>_ch<chapter>/v2_diagrams/ (source/, spec/, book/, map/, agents/, out/, meta.json).
STAGING only. Nothing is ever written to a chapter before `upload --go`; V2 versions are never deleted or edited (a new version
is added; the only overwrite is a DRAFT the user asked to remove, Class 8 Ch1).
"""
import argparse
import copy
import glob
import hashlib
import importlib.util
import json
import os
import re
import shutil
import sys
import urllib.error
import urllib.request

HERE_TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE_TOOLS, "..", ".."))
BASE = "https://staging.singularity-learn.com"
API = BASE + "/agentapi/api/lp2/learning-plans/chapter/"
DOCS = os.path.join(ROOT, "docs", "karan-MD")
SPEC_SRC = {"diagram_identification_prompt_v3.md": "diagram_identification_prompt (1).md",
            "diagram_map.schema_v3.json": "diagram_map.schema (1).json",
            "companion_note.md": "Diagram trigger word — cross-standard companion note.md"}
DIAGRAM = "DIAGRAM · "
PROMPT = "diagram_identification_prompt.md v3"
SKIP = {(6, 3), (6, 4), (8, 11)}            # user: leave them as they are
OVERWRITE_DRAFT = {(8, 1)}                  # user: remove the newer draft v46, make the newly made v46 active
CHUNK_TARGET = 26                           # items per decision agent
PAGES_PER_AGENT = 16

TEXTBOOK = {
    5: ("Maths Mela, Grade 5 (NCERT)", lambda n: "textbooks/class-5/eemm1%02d.pdf" % n),
    6: ("Ganita Prakash, Grade 6", lambda n: "textbooks/class6/fegp1%02d.pdf" % n),
    7: ("Ganita Prakash, Grade 7", lambda n: "textbooks/class7/gegp1%02d.pdf" % n if n <= 8 else "textbooks/class7/gegp2%02d.pdf" % (n - 8)),
    8: ("Ganita Prakash, Grade 8", lambda n: "textbooks/class8/hegp1%02d.pdf" % n if n <= 7 else "textbooks/class8/hegp2%02d.pdf" % (n - 7)),
}


def chapter_id(c, n):
    return "cbse_eng_maths%d_ch%d" % (c, n)


def here(c, n):
    return os.path.join(ROOT, "chapters", "maths%d_ch%d" % (c, n), "v2_diagrams")


def load(p):
    return json.load(open(p, encoding="utf-8"))


def dump(o, p):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(o, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def get(path):
    for attempt in range(4):
        try:
            with urllib.request.urlopen(API + path, timeout=240) as r:
                return json.load(r)["data"]
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if attempt == 3:
                raise
        except Exception:
            if attempt == 3:
                raise
    return None


def plan_of(cid, ver):
    p = get("%s?version=%d" % (cid, ver))["plan"]
    pj = p["planJson"]
    return (json.loads(pj) if isinstance(pj, str) else pj), p


def topics_of(plan):
    return [t for m in plan["modules"] for s in m["segments"] for t in s["topics"]]


def is_card(md):
    return md.get("type") == "image" and md.get("image_role") in ("question", "solution")


# ====================================================================== inventory
def cards_by_concept(t):
    """{concept_id: {"question": [nodes], "solution": [nodes]}} from the topic's media list, by the NODE's own concept id
    (always right, even when concept media_ids and block links are stale)."""
    out = {}
    for md in t.get("media", []):
        if is_card(md):
            out.setdefault(md.get("concept_id"), {"question": [], "solution": []})[md["image_role"]].append(md)
    return out


def item_view(it):
    keep = ("question", "question_tex", "steps_tex", "answer_tex", "steps", "answer", "text", "q_figure", "s_figure",
            "book_number", "item_kind", "ncert_refs", "video_media_id", "example_id")
    return {k: it[k] for k in keep if k in it and it[k] not in (None, "", [])}


def short(s, n):
    return s if len(s) <= n else s[:n] + "..."


def video_view(md):
    if not md:
        return None
    vs = md.get("video_script") or {}
    return {"id": md["id"], "title": md.get("title"), "description": short(md.get("description") or "", 600),
            "anchor": vs.get("anchor"), "maths_rules": vs.get("maths_rules"), "final_answer": vs.get("final_answer")}


def build_units(plan):
    """Units in LP order + concept images + warnings. Kinds: pair (qt_part question/answer concepts), single (a non-pair concept that owns
    card nodes; its text may sit in a 'Practice' block that points at its video), worked (no card). Cards are matched by node concept id."""
    cimgs, units, warns = [], [], []
    single_videos = set()
    for t in topics_of(plan):
        cb = cards_by_concept(t)
        for c in t["concepts"]:
            if c.get("qt_part") in ("question", "answer") or c["concept_id"] not in cb:
                continue
            for b in c.get("content", []):
                if "question" in b and b.get("video_media_id"):
                    single_videos.add(b["video_media_id"])
    practice, pending_singles, assigned = {}, [], set()
    for m in plan["modules"]:
        for s in m["segments"]:
            for t in s["topics"]:
                tm = {md["id"]: md for md in t["media"]}
                cb = cards_by_concept(t)
                for md in t["media"]:
                    if md.get("type") == "image" and not is_card(md):
                        cimgs.append({"id": md["id"], "topic_id": t["topic_id"], "topic_name": t["topic_name"], "concept_id": md.get("concept_id"),
                                      "title": md.get("title"), "labels": md.get("labels"), "build_status": md.get("build_status"),
                                      "description": short(md.get("description") or "", 600)})
                cons = t["concepts"]

                def kept_ids(c):
                    return [md["id"] for md in t["media"] if md.get("type") == "image" and not is_card(md) and md.get("concept_id") == c["concept_id"]]

                def ids_of(cid, role):
                    return [x["id"] for x in cb.get(cid, {}).get(role, [])]
                i = 0
                while i < len(cons):
                    c = cons[i]
                    qblocks = [(k, b) for k, b in enumerate(c.get("content", [])) if "question" in b]
                    if not qblocks:
                        i += 1
                        continue
                    part = c.get("qt_part")
                    base = {"module_id": m["module_id"], "topic_id": t["topic_id"], "topic_name": t["topic_name"]}
                    if part == "question":
                        a = cons[i + 1] if i + 1 < len(cons) else None
                        if a is None or a.get("qt_part") != "answer":
                            warns.append("question concept %s has no answer concept after it" % c["concept_id"])
                            i += 1
                            continue
                        ab = [(k, b) for k, b in enumerate(a.get("content", [])) if "question" in b]
                        if not ab:
                            warns.append("answer concept %s has no question block" % a["concept_id"])
                        qid, aid = ids_of(c["concept_id"], "question"), ids_of(a["concept_id"], "solution")
                        assigned.update(qid + aid)
                        for cc_, role_ in ((c, "solution"), (a, "question")):
                            if ids_of(cc_["concept_id"], role_):
                                warns.append("concept %s holds %s cards" % (cc_["concept_id"], role_))
                                assigned.update(ids_of(cc_["concept_id"], role_))
                        units.append(dict(base, kind="pair", ncert_refs=c.get("ncert_refs"),
                                          question_concept={"concept_id": c["concept_id"], "name": c.get("concept_name"), "card_ids": qid,
                                                            "item": item_view(qblocks[0][1]), "extra_items": [item_view(b) for _, b in qblocks[1:]],
                                                            "kept_image_ids": kept_ids(c)},
                                          answer_concept={"concept_id": a["concept_id"], "name": a.get("concept_name"), "card_ids": aid,
                                                          "item": item_view(ab[0][1]) if ab else {}, "extra_items": [item_view(b) for _, b in ab[1:]],
                                                          "kept_image_ids": kept_ids(a)}))
                        i += 2
                        continue
                    if part == "answer":
                        warns.append("orphan answer concept %s" % c["concept_id"])
                        i += 1
                        continue
                    own = cb.get(c["concept_id"])
                    for bi, (_cidx, b) in enumerate(qblocks):       # block_index = position among the concept's QUESTION blocks
                        if own:
                            qs, ss = [x["id"] for x in own["question"]], [x["id"] for x in own["solution"]]
                            if len(qblocks) > 1:
                                qs = qs[bi:bi + 1] if len(qs) >= len(qblocks) else (qs if bi == 0 else [])
                                ss = ss[bi:bi + 1] if len(ss) >= len(qblocks) else (ss if bi == 0 else [])
                                if len(own["question"]) not in (0, len(qblocks)) or len(own["solution"]) not in (0, len(qblocks)):
                                    warns.append("concept %s: %d question blocks but %d question / %d solution cards: check the matching" %
                                                 (c["concept_id"], len(qblocks), len(own["question"]), len(own["solution"])))
                            assigned.update(qs + ss)
                            u = dict(base, kind="single", concept_id=c["concept_id"], concept_name=c.get("concept_name"), block_index=bi,
                                     blocks_in_concept=len(qblocks), ncert_refs=c.get("ncert_refs"), item=item_view(b),
                                     question_card_ids=qs, solution_card_ids=ss,
                                     question_cards=[card_view(tm[x]) for x in qs], solution_cards=[card_view(tm[x]) for x in ss],
                                     video=video_view(tm.get(b.get("video_media_id"))), kept_image_ids=kept_ids(c))
                            units.append(u)
                            pending_singles.append(u)
                        elif b.get("video_media_id") in single_videos:
                            practice[b["video_media_id"]] = {"concept_id": c["concept_id"], "concept_name": c.get("concept_name"),
                                                             "block_index": bi, "item": item_view(b)}
                        else:
                            units.append(dict(base, kind="worked", concept_id=c["concept_id"], concept_name=c.get("concept_name"), block_index=bi,
                                              blocks_in_concept=len(qblocks), ncert_refs=c.get("ncert_refs"), item=item_view(b),
                                              kept_image_ids=kept_ids(c)))
                    i += 1
    for t in topics_of(plan):
        for md in t["media"]:
            if is_card(md) and md["id"] not in assigned:
                warns.append("ORPHAN CARD %s (concept %s has no question block): stop and ask" % (md["id"], md.get("concept_id")))
    for u in pending_singles:
        v = (u.get("item") or {}).get("video_media_id")
        if v in practice:
            u["lp_text"] = practice[v]
    for k, u in enumerate(units, 1):
        u["unit"] = k
    return units, cimgs, warns


def card_ids_for(u, role):
    if u["kind"] == "pair":
        return u["question_concept"]["card_ids"] if role == "question" else u["answer_concept"]["card_ids"]
    if u["kind"] == "single":
        return u["question_card_ids"] if role == "question" else u["solution_card_ids"]
    return []


def card_view(md):
    return {"id": md["id"], "title": md.get("title"), "description": short(md.get("description") or "", 700), "aspect_ratio": md.get("aspect_ratio")}


def items_of(u):
    return 1 if u["kind"] == "worked" else 2


def make_chunks(units):
    """Contiguous chunks of whole topics, about CHUNK_TARGET items each."""
    topics, order = {}, []
    for u in units:
        if u["topic_id"] not in topics:
            topics[u["topic_id"]] = []
            order.append(u["topic_id"])
        topics[u["topic_id"]].append(u)
    chunks, cur, cur_items = [], [], 0
    for tid in order:
        n = sum(items_of(u) for u in topics[tid])
        if cur and cur_items + n > CHUNK_TARGET * 1.25:
            chunks.append(cur)
            cur, cur_items = [], 0
        cur.append(tid)
        cur_items += n
    if cur:
        chunks.append(cur)
    # merge a tiny last chunk into the previous one
    if len(chunks) > 1 and sum(items_of(u) for tid in chunks[-1] for u in topics[tid]) < CHUNK_TARGET * 0.4:
        last = chunks.pop()
        chunks[-1] += last
    letters = "ABCDEFGHIJKLMNOP"
    return {letters[i]: tids for i, tids in enumerate(chunks)}


# ====================================================================== prepare
def detect_solutions_start(pages_text):
    pat = re.compile(r"(chapter\s*\d+\s*[—–-]+\s*solutions|chapter\s*\d+\s*solutions)", re.I)
    for i, t in enumerate(pages_text, 1):
        if pat.search(t[:400]):
            return i
    return None


def prepare(c, n):
    import pypdfium2 as pdfium
    import pdfplumber
    cid = chapter_id(c, n)
    H = here(c, n)
    if (c, n) in SKIP:
        raise SystemExit("%s is skipped by the user's decision" % cid)
    versions = get(cid + "/versions")
    if not versions:
        raise SystemExit("%s: no versions on staging" % cid)
    active = [v for v in versions if v["isActive"]]
    if not active:
        raise SystemExit("%s has no active version: stop and ask" % cid)
    act = active[0]["version"]
    newest = max(versions, key=lambda v: v["version"])
    overwrite = False
    if newest["version"] > act:
        if newest["isDraft"] and (c, n) in OVERWRITE_DRAFT:
            overwrite = True
        else:
            raise SystemExit("%s: version %d (%s) is newer than the active v%d: stop and ask" % (cid, newest["version"], newest["status"], act))
    target = newest["version"] if overwrite else newest["version"] + 1
    plan, pmeta = plan_of(cid, act)
    os.makedirs(H, exist_ok=True)
    for d in ("source", "spec", "book", "map", "agents", "out"):
        os.makedirs(os.path.join(H, d), exist_ok=True)
    src = os.path.join(H, "source", "%s_v%d.json" % (cid, act))
    dump(plan, src)
    sha = hashlib.sha256(open(src, "rb").read()).hexdigest()
    if overwrite:
        draft, _ = plan_of(cid, newest["version"])
        dump(draft, os.path.join(H, "source", "%s_v%d_draft_backup.json" % (cid, newest["version"])))
    for dst, srcname in SPEC_SRC.items():
        shutil.copyfile(os.path.join(DOCS, srcname), os.path.join(H, "spec", dst))
    # book
    tb_name, pdf_fn = TEXTBOOK[c]
    pdf_path = os.path.join(ROOT, pdf_fn(n))
    pdf = pdfium.PdfDocument(pdf_path)
    npages = len(pdf)
    texts = []
    with pdfplumber.open(pdf_path) as p:
        for i, pg in enumerate(p.pages):
            texts.append(pg.extract_text() or "")
    for i in range(npages):
        pdf[i].render(scale=1.65).to_pil().save(os.path.join(H, "book", "page_%02d.png" % (i + 1)))
    open(os.path.join(H, "book", "chapter_text.md"), "w", encoding="utf-8").write(
        "\n".join("<!-- pdf page %d -->\n%s\n" % (i + 1, t) for i, t in enumerate(texts)))
    sol = detect_solutions_start(texts)
    chap_pages = (1, (sol - 1) if sol else npages)
    sol_pages = (sol, npages) if sol else None
    units, cimgs, warns = build_units(plan)
    chunks = make_chunks(units)
    dump(units, os.path.join(H, "map", "inventory.json"))
    dump(cimgs, os.path.join(H, "map", "concept_images.json"))
    for ch, tids in chunks.items():
        dump([u for u in units if u["topic_id"] in tids], os.path.join(H, "map", "in_%s.json" % ch))
    # inventory agent segments
    segs = []

    def split(a, b, kind):
        k = 0
        pg = a
        while pg <= b:
            e = min(b, pg + PAGES_PER_AGENT - 1)
            k += 1
            segs.append({"kind": kind, "from": pg, "to": e})
            pg = e + 1
    split(chap_pages[0], chap_pages[1], "chapter")
    if sol_pages:
        split(sol_pages[0], sol_pages[1], "solutions")
    for k, sg in enumerate(segs, 1):
        sg["file"] = "inv_base_%s_%02d_%02d.json" % (sg["kind"], sg["from"], sg["to"])
        sg["agent"] = "inv_%d" % k
    master = plan.get("chapter_master_id")
    meta = {"class_no": c, "chapter_no": n, "chapter_id": cid, "chapter_name": plan.get("chapter_name"), "master": master,
            "textbook": tb_name, "pdf": pdf_fn(n), "pages": npages, "chapter_pages": list(chap_pages), "solutions_pages": list(sol_pages) if sol_pages else None,
            "base_version": act, "base_sha256": sha, "base_source": os.path.basename(src), "newest_version": newest["version"],
            "target_version": target, "overwrite_draft": overwrite, "overwrite_draft_status": newest["status"] if overwrite else None,
            "segments": segs, "chunks": {k: v for k, v in chunks.items()}, "units": len(units),
            "items": sum(items_of(u) for u in units), "cards_in_plan": sum(1 for t in topics_of(plan) for md in t["media"] if is_card(md)),
            "concept_images": len(cimgs), "warnings": warns}
    dump(meta, os.path.join(H, "meta.json"))
    write_agent_files(c, n, meta)
    print("prepared %s: live v%d (newest v%d) -> new v%d%s | pdf %s %d pages (chapter %s, solutions %s) | units %d items %d cards %d | "
          "inventory agents %d, decision chunks %d %s" % (cid, act, newest["version"], target, " (OVERWRITES draft)" if overwrite else "",
          os.path.basename(pdf_path), npages, chap_pages, sol_pages, len(units), meta["items"], meta["cards_in_plan"], len(segs), len(chunks),
          {k: sum(items_of(u) for u in units if u["topic_id"] in v) for k, v in chunks.items()}))
    for w in warns:
        print("  WARNING:", w)
    return meta


def write_agent_files(c, n, meta):
    H = here(c, n)
    tpl_dir = os.path.join(HERE_TOOLS, "templates")
    subs = {"HERE": H + "/", "CHAPTER": meta["chapter_name"], "CLASS": str(c), "CHNO": str(n), "TEXTBOOK": meta["textbook"],
            "CHAPTER_ID": meta["chapter_id"], "BASE_PLAN": "%s_v%d" % (meta["chapter_id"], meta["base_version"]),
            "NPAGES": str(meta["pages"]), "CH_FROM": str(meta["chapter_pages"][0]), "CH_TO": str(meta["chapter_pages"][1]),
            "N_CIMGS": str(meta["concept_images"]), "TOOLS": HERE_TOOLS}
    sol = meta["solutions_pages"]
    subs["SOL_SENTENCE"] = ("Printed solutions: pdf pages %d-%d (answers section by section; a printed answer can be a picture, Step B2)." % tuple(sol)
                            if sol else "This pdf has NO printed-solutions section: the LP solution text is the answer to follow.")
    subs["BASE_FILES"] = ", ".join("`HERE/map/%s`" % s["file"] for s in meta["segments"])

    def fill(t):
        for k, v in subs.items():
            t = t.replace("{{%s}}" % k, v)
        return t
    open(os.path.join(H, "AGENT_BRIEF.md"), "w", encoding="utf-8", newline="\n").write(fill(open(os.path.join(tpl_dir, "AGENT_BRIEF.md"), encoding="utf-8").read()))
    for sg in meta["segments"]:
        t = fill(open(os.path.join(tpl_dir, "inv_prompt.md"), encoding="utf-8").read())
        t = t.replace("{{SEG_KIND}}", sg["kind"]).replace("{{SEG_FROM}}", str(sg["from"])).replace("{{SEG_TO}}", str(sg["to"])).replace("{{SEG_FILE}}", sg["file"])
        t = t.replace("{{SEG_NOTE}}", "the CHAPTER text (figures a question or example refers to, teaching figures, tables)" if sg["kind"] == "chapter"
                      else "the PRINTED SOLUTIONS (every picture an answer draws, filled/plain tables, graphs, constructions)")
        t = t.replace("{{FIG_PREFIX}}", "P" if sg["kind"] == "chapter" else "SOL").replace("{{SRC_WORD}}", "chapter" if sg["kind"] == "chapter" else "solutions")
        open(os.path.join(H, "agents", sg["agent"] + ".md"), "w", encoding="utf-8", newline="\n").write(t)
    for ch, tids in meta["chunks"].items():
        t = fill(open(os.path.join(tpl_dir, "chunk_prompt.md"), encoding="utf-8").read())
        t = t.replace("{{CHUNK}}", ch).replace("{{TOPICS}}", ", ".join(tids))
        open(os.path.join(H, "agents", "chunk_%s.md" % ch), "w", encoding="utf-8", newline="\n").write(t)


# ====================================================================== validate / merge
def key_of(it):
    return (it.get("lp_concept_id"), it.get("role"), it.get("block_index", 0) if it.get("role") != "question" or False else it.get("block_index", 0))


def unit_keys(u):
    if u["kind"] == "pair":
        return [(u["question_concept"]["concept_id"], "question", 0), (u["answer_concept"]["concept_id"], "solution", 0)]
    if u["kind"] == "single":
        return [(u["concept_id"], "question", u["block_index"]), (u["concept_id"], "solution", u["block_index"])]
    return [(u["concept_id"], "worked_example", u["block_index"])]


def ikey(it):
    return (it.get("lp_concept_id"), it.get("role"), it.get("block_index", 0))


def load_validator(H):
    spec = importlib.util.spec_from_file_location("rollout_validate", os.path.join(HERE_TOOLS, "validate_map.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def merge(c, n):
    H = here(c, n)
    meta = load(os.path.join(H, "meta.json"))
    V = load_validator(H)
    items, notes, figs, conflicts, renamed = [], [], {}, [], []
    first = None
    mmeta = None
    for ch in meta["chunks"]:
        p = os.path.join(H, "map", "out_%s.json" % ch)
        if not os.path.exists(p):
            raise SystemExit("missing %s" % p)
        m = load(p)
        first = first or m
        mmeta = mmeta or m["meta"]
        items += m["items"]
        notes += ["[chunk %s] %s" % (ch, x) for x in m["meta"].get("notes", [])]
        for f in m["figure_inventory"]:
            old = figs.get(f["fig_id"])
            if old and old["mapped_to"] != f["mapped_to"]:
                # the same book picture claimed differently by two chunks = two uses of it: the later use becomes its own NEW- entry
                nf = dict(f)
                nf["fig_id"] = "NEW-%s-%s" % (f["fig_id"], ch)
                nf["description"] = "(another use of %s) %s" % (f["fig_id"], f.get("description", ""))
                renamed.append("%s (chunk %s: %s) kept as %s next to the earlier %s" % (f["fig_id"], ch, f["mapped_to"], nf["fig_id"], old["mapped_to"]))
                figs.setdefault(nf["fig_id"], nf)
                continue
            figs.setdefault(f["fig_id"], f)
    if renamed:
        print("figures claimed by two chunks (kept both as separate uses): " + "; ".join(renamed))
    if conflicts:
        print("\n".join("CONFLICT " + x for x in conflicts))
        raise SystemExit("figure conflicts between chunks: resolve (stop and ask if unclear)")
    inv = load(os.path.join(H, "map", "inventory.json"))
    order = [k for u in inv for k in unit_keys(u)]
    pos = {k: i for i, k in enumerate(order)}
    items.sort(key=lambda it: pos[ikey(it)])
    counts = {}
    for it in items:
        counts.setdefault(it["role"], {}).setdefault(it["decision"], 0)
        counts[it["role"]][it["decision"]] += 1
    md = dict(mmeta)
    md["prompt"] = PROMPT
    md["counts_by_role_and_decision"] = counts
    md["notes"] = notes
    fl = sorted(figs.values(), key=lambda f: f["fig_id"])
    kinds = {"items": 0, "concept": 0, "none": 0}
    for f in fl:
        kinds["items" if f["mapped_to"].startswith("item:") else "concept" if f["mapped_to"].startswith("concept_image:") else "none"] += 1
    cov = {"inventory_figures": len(fl), "mapped_to_items": kinds["items"], "mapped_to_concept_images": kinds["concept"], "mapped_none": kinds["none"],
           "unmapped": 0, "new_media_ids_created": sorted(i["media_id"] for i in items if i["decision"] == "required"),
           "lp_ids_dropped": sorted({i["media_id"] for i in items if i["decision"] != "required" and i.get("media_id")})}
    out = os.path.join(H, "map", "diagram_map.json")
    dump({"meta": md, "style_tokens": first["style_tokens"], "figure_inventory": fl, "coverage_report": cov, "items": items}, out)
    print("merged", len(items), "items,", len(fl), "figures;", json.dumps(counts))
    return V.main(out, "all", H, meta)


# ====================================================================== build
_TOKEN = re.compile(r"\bM\d+\.S\d+\.T\d+\.C\d+\.[A-Za-z0-9]+")
_IMG = re.compile(r"\.IMG(\d+)$")


def renumber_for_server(plan):
    """The upload server wants the images of a concept numbered IMG1, IMG2 ... down the topic's media list. Only ids change,
    every reference is rewritten, urls (strings starting with http) are frozen. Returns {old: new}."""
    rename = {}
    for topic in topics_of(plan):
        by_concept = {}
        for node in topic.get("media") or []:
            if node.get("type") == "image" and _IMG.search(node.get("id", "")):
                by_concept.setdefault(node.get("concept_id"), []).append(node)
        for cid, nodes in by_concept.items():
            for want, node in enumerate(nodes, 1):          # media-list order (the server counts down the list)
                new_id = "%s.IMG%d" % (cid, want)
                if node["id"] != new_id:
                    rename[node["id"]] = new_id
    if not rename:
        return {}
    # two-phase rename through temporary names would be needed if ids swap; detect swaps and stop
    if set(rename) & set(rename.values()):
        pass          # chains (A->B, B->C) are fine for a one-pass regex substitution: each token is replaced exactly once

    def fix(o):
        if isinstance(o, dict):
            return {k: fix(v) for k, v in o.items()}
        if isinstance(o, list):
            return [fix(v) for v in o]
        if isinstance(o, str) and not o.startswith("http"):
            return _TOKEN.sub(lambda mo: rename.get(mo.group(0), mo.group(0)), o)
        return o
    for k in list(plan.keys()):
        plan[k] = fix(plan[k])
    return rename


def ratio_dims(r, width=1920):
    a, b = [int(x) for x in r.split(":")]
    return "%dx%d" % (width, round(width * b / a))


def line_start(text, n):
    m = re.search(r"(?m)^\$?%d\$?\. " % n, text)
    if m:
        return m.start()
    m = re.search(r"(?m)^Answer:", text)
    return m.start() if m else len(text)


def insert_line(text, idx, tok):
    if idx >= len(text):
        return text.rstrip("\n") + "\n" + tok
    return text[:idx] + tok + "\n" + text[idx:]


def put_question_token(block, tok, worked):
    if worked:
        for k in ("text", "publication_text"):
            if isinstance(block.get(k), str):
                block[k] = insert_line(block[k], line_start(block[k], 1), tok)
    else:
        for k in ("question_tex", "text", "publication_text"):
            if isinstance(block.get(k), str):
                block[k] = block[k].rstrip("\n") + "\n" + tok


def put_solution_token(block, tok):
    if block.get("steps_tex"):
        block["steps_tex"][0] = tok + "\n" + block["steps_tex"][0]
    for k in ("text", "publication_text"):
        if isinstance(block.get(k), str):
            block[k] = insert_line(block[k], line_start(block[k], 1), tok)


def label_of(it, u):
    role = it["role"]
    if u["kind"] == "pair":
        cc = u["answer_concept"] if role == "solution" else u["question_concept"]
        return cc["item"].get("book_number") or cc["name"]
    if u["kind"] == "single":
        return u["concept_name"] if (u["item"].get("book_number") or "") in ("", None) or u.get("blocks_in_concept", 1) > 1 or True else u["item"]["book_number"]
    base = u["item"].get("book_number") or u["concept_name"]
    return base + (" (example %d)" % (u["block_index"] + 1) if u.get("blocks_in_concept", 1) > 1 else "")


def make_node(it, u, key_dir, concept):
    d = it["diagram"]
    mid, role = it["media_id"], it["role"]
    label = label_of(it, u)
    if role == "solution":
        side, word = "solution", "solution"
        teach, instr = "Show only after the student has attempted the question.", "Compare this with your own working, step by step."
        ctx = "Solution figure of %s." % label
    else:
        side, word = "question", "question"
        teach, instr = "", "Look carefully at the figure."
        ctx = "Question figure of %s." % label
    spec = dict(d)
    spec["reason"], spec["reason_codes"] = it["reason"], it["reason_codes"]
    if it.get("needs_lp_text_sync"):
        spec["needs_lp_text_sync"] = True
    url = "%s/%s.png" % (key_dir, mid)
    return {
        "id": mid, "type": "image", "title": "%s%s %s figure" % (DIAGRAM, label, word), "concept_id": concept, "home_concept_id": concept,
        "image_role": side, "image_category": "concept", "subtype": "illustration", "build_status": "placeholder",
        "aspect_ratio": d["aspect_ratio"], "image_dimensions": ratio_dims(d["aspect_ratio"]), "image_url": url, "planned_url": url,
        "description": d["alt_text"], "labels": list(d["visible_text"]), "context": ctx + " PLACEHOLDER: specified, not generated yet.",
        "diagram_spec": spec, "generation_prompt": d["manim_description"], "negative_prompt": "; ".join(d["must_not_show"]),
        "accuracy_constraints": "\n".join(d["accuracy_checks"]),
        "render_source": {"engine": "manim", "scene": it.get("manim_scene"), "code_url": "%s/code/%s.py" % (key_dir, mid),
                          "style_url": "%s/code/_style.py" % key_dir},
        "instructions_for_student": instr, "teaching_notes": teach, "related_concept_ids": [], "source_image_key": "",
    }


def build(c, n):
    H = here(c, n)
    meta = load(os.path.join(H, "meta.json"))
    src = load(os.path.join(H, "source", meta["base_source"]))
    plan = copy.deepcopy(src)
    dm = load(os.path.join(H, "map", "diagram_map.json"))
    inv = {}
    for u in load(os.path.join(H, "map", "inventory.json")):
        for k in unit_keys(u):
            inv[k] = u
    items = {ikey(i): i for i in dm["items"]}
    assert not [i for i in items.values() if i["lp_placeholder_action"] == "reuse_concept_image" or i.get("reuse_media_id")], "v3: no reuse"
    req = {k: i for k, i in items.items() if i["decision"] == "required"}
    cid_plan = meta["chapter_id"]
    plan["version"] = meta["target_version"]
    plan["plan_id"] = "%s_v%d" % (cid_plan, meta["target_version"])
    plan["_activate"] = True
    assert plan["chapter_id"] == cid_plan and plan["phase"] == 2 and plan["chapter_master_id"] == meta["master"], "unexpected plan identity"

    topics = {t["topic_id"]: t for t in topics_of(plan)}
    concepts = {cc["concept_id"]: (t, cc) for t in topics.values() for cc in t["concepts"]}
    all_cards = {md["id"] for t in topics.values() for md in t["media"] if is_card(md)}
    removed_ids = set(all_cards)
    old = next(md for t in topics.values() for md in t["media"] if is_card(md))
    key_dir = re.sub(r"/[^/]+/[^/]+$", "", old["planned_url"]) + "/diagram_v1"

    # which old card is replaced by which new node (the unit knows its cards: matched by the node's own concept id)
    replace_by = {}
    for (cid, role, bi), it in req.items():
        for x in card_ids_for(inv[(cid, role, bi)], role):
            replace_by.setdefault(x, it["media_id"])

    added_ids = []
    for tid, t in topics.items():
        new_nodes = {}
        for k, it in req.items():
            if k[0].rsplit(".C", 1)[0] == tid:
                new_nodes.setdefault(k[0], []).append((it["media_id"], make_node(it, inv[k], key_dir, k[0])))
        emitted, out = set(), []
        for md in t["media"]:
            if is_card(md):
                nid = replace_by.get(md["id"])
                if nid and nid not in emitted:
                    node = next(nd for lst in new_nodes.values() for (i_, nd) in lst if i_ == nid)
                    out.append(node)
                    emitted.add(nid)
                continue
            out.append(md)
        for cid, lst in new_nodes.items():
            rest = [nd for (i_, nd) in sorted(lst, key=lambda x: x[0]) if i_ not in emitted]
            if rest:
                last = max([i for i, md in enumerate(out) if md.get("concept_id") == cid] or [len(out) - 1])
                out[last + 1:last + 1] = rest
                emitted.update(nd["id"] for nd in rest)
        t["media"] = out
        added_ids += [nd["id"] for lst in new_nodes.values() for (_, nd) in lst]

    card_concepts = set()
    for u in inv.values():
        if u["kind"] == "pair":
            card_concepts.update((u["question_concept"]["concept_id"], u["answer_concept"]["concept_id"]))
        elif u["kind"] == "single":
            card_concepts.add(u["concept_id"])
    new_by_concept = {}
    for k, it in req.items():
        new_by_concept.setdefault(k[0], []).append(it["media_id"])
    for cid, (t, cc) in concepts.items():
        tids = {md["id"] for md in t["media"]}
        mine = new_by_concept.get(cid, [])
        mids = []
        for x in cc.get("media_ids", []):
            if x in removed_ids:                         # an old card: its diagram takes its place
                nid = replace_by.get(x)
                if nid and nid in mine and nid not in mids:
                    mids.append(nid)
            elif cid in card_concepts and x not in tids and _IMG.search(x):
                continue                                  # a stale card reference of a card-bearing concept: goes with the cards
            else:
                mids.append(x)
        for mid in mine:
            if mid not in mids:
                last_img = max([i for i, x in enumerate(mids) if ".IMG" in x] or [-1])
                mids.insert(last_img + 1, mid)
        cc["media_ids"] = mids

    # block links: only the card links are reset (pair/single blocks), then set per decision; worked blocks and everything else untouched
    def reset(b, fields):
        had = [f for f in fields if f in b]
        for f in fields:
            b.pop(f, None)
        return bool(had)
    tokens = {}
    pair_done = set()
    for u in inv.values():
        if u["kind"] == "pair" and u["question_concept"]["concept_id"] not in pair_done:
            pair_done.add(u["question_concept"]["concept_id"])
    for (cid, role, bi), it in sorted(req.items(), key=lambda x: (x[0][0], x[0][1], x[0][2])):
        pass
    # reset first (all units), then set
    for u in {id(v): v for v in inv.values()}.values():
        if u["kind"] == "pair":
            qb = [b for b in concepts[u["question_concept"]["concept_id"]][1]["content"] if "question" in b]
            ab = [b for b in concepts[u["answer_concept"]["concept_id"]][1]["content"] if "question" in b]
            u["_had_q"] = [reset(b, ("image_media_id",)) for b in qb]
            u["_had_a"] = [reset(b, ("solution_image_media_id", "solution_image_media_ids")) for b in ab]
        elif u["kind"] == "single":
            b = [b for b in concepts[u["concept_id"]][1]["content"] if "question" in b][u["block_index"]]
            reset(b, ("image_media_id", "solution_image_media_id", "solution_image_media_ids"))
    for (cid, role, bi), it in req.items():
        t, cc = concepts[cid]
        u = inv[(cid, role, bi)]
        mid = it["media_id"]
        qblocks = [b for b in cc["content"] if "question" in b]
        tok = "{{DIAGRAM:%s}}" % mid
        tokens[mid] = tok
        if u["kind"] == "pair":
            had = u["_had_q"] if role == "question" else u["_had_a"]
            targets = [k for k, h in enumerate(had) if h] or [0]
            field = "image_media_id" if role == "question" else "solution_image_media_id"
            for k in targets:
                qblocks[k][field] = mid
            block = qblocks[0]
        else:
            block = qblocks[bi]
            block["solution_image_media_id" if role == "solution" else "image_media_id"] = mid
        if role == "solution":
            assert (it["placeholder"]["insert_into"], it["placeholder"]["position"]) == ("steps_tex", "before_first_step")
            put_solution_token(block, tok)
        else:
            put_question_token(block, tok, role == "worked_example")

    kept_nodes = {md["id"]: copy.deepcopy(md) for t in topics_of(plan) for md in t["media"] if not md.get("title", "").startswith(DIAGRAM)}
    rename = renumber_for_server(plan)
    kept_renamed = {o: nw for o, nw in rename.items() if o in kept_nodes}
    n_img = sum(1 for t in topics_of(plan) for md in t["media"] if md.get("type") == "image")
    ss = plan.get("source_metadata", {}).get("summary_stats")
    if isinstance(ss, dict):
        ss["images"] = n_img
        ss["diagram_placeholders"] = len(added_ids)
    plan.setdefault("source_metadata", {})["diagram_v3"] = {
        "from": "%s_v%d (live V2)" % (cid_plan, meta["base_version"]),
        "note": "V2 updated in place (new version): the %d old question and solution card placeholders (none was built) are replaced by %d "
                "DIAGRAM placeholders where a figure is needed, each titled 'DIAGRAM \u00b7 ...', specified in diagram_spec, linked by image_media_id / "
                "solution_image_media_id and by a {{DIAGRAM:<id>}} token in the text (solution token before step 1); no block points at a teaching "
                "image. Videos, tools and concept images are unchanged." % (len(removed_ids), len(added_ids)),
        "rules": ["diagram_identification_prompt v3", "diagram_map.schema v3", "Diagram trigger word companion note (2026-11-18, updated 2026-11-21)"],
    }
    check_build(plan, src, removed_ids, rename, kept_renamed, meta)
    p = os.path.join(H, "out", plan["plan_id"] + ".json")
    dump(plan, p)
    print("wrote", p)
    return plan


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
    r"^(/version|/plan_id|/_activate|/source_metadata/(summary_stats/images|summary_stats/diagram_placeholders|diagram_v3)"
    r"|/modules\[\d+\]/segments\[\d+\]/topics\[\d+\](/media(\[.*)?"
    r"|/concepts\[\d+\](/media_ids(\[.*)?|/content\[\d+\]/(image_media_id|solution_image_media_ids?|question_tex|steps_tex(\[\d+\])?|text|publication_text|answer_tex))))$")


def link_problems(plan):
    """Dangling or cross-topic references of the concepts' media lists and the blocks' image/video links: {(concept_id, kind, value)}."""
    out = set()
    for t in topics_of(plan):
        ids = {md["id"] for md in t["media"]}
        for cc in t["concepts"]:
            for x in cc.get("media_ids", []):
                if x not in ids:
                    out.add((cc["concept_id"], "media_ids", x))
            for b in cc.get("content", []):
                for f in ("image_media_id", "solution_image_media_id", "video_media_id"):
                    x = b.get(f)
                    if x and x not in ids:
                        out.add((cc["concept_id"], f, x))
                    elif x and f != "video_media_id" and x not in cc.get("media_ids", []):
                        out.add((cc["concept_id"], f + "_not_in_media_ids", x))
    return out


def check_build(plan, src, removed_ids, rename, kept_renamed, meta):
    errs = []
    s = json.dumps(plan, ensure_ascii=False)
    nodes = {md["id"]: (t["topic_id"], md) for t in topics_of(plan) for md in t["media"]}
    diagrams = {k for k, (tid, md) in nodes.items() if md.get("title", "").startswith(DIAGRAM)}
    for t in topics_of(plan):
        by = {}
        for md in t["media"]:
            if md.get("type") == "image":
                by.setdefault(md.get("concept_id"), []).append(md["id"])
        for cc, lst in by.items():
            if lst != ["%s.IMG%d" % (cc, i) for i in range(1, len(lst) + 1)] and all(_IMG.search(x) for x in lst):
                errs.append("server numbering broken for concept %s: %s" % (cc, lst))
    # references: whatever was dangling in the live plan may stay (user: 'replace cards only'); NOTHING new may dangle
    pre = {(c_, k_, rename.get(v_, v_)) for (c_, k_, v_) in link_problems(src)}
    new_problems = link_problems(plan) - pre
    for pr in sorted(new_problems)[:20]:
        errs.append("new dangling reference %s" % (pr,))
    for t in topics_of(plan):
        ids = {md["id"] for md in t["media"]}
        for cc in t["concepts"]:
            for b in cc.get("content", []):
                for f in ("image_media_id", "solution_image_media_id"):
                    x = b.get(f)
                    if x and x in ids and x not in diagrams and (cc["concept_id"], f, x) not in pre and nodes[x][1].get("image_role"):
                        errs.append("%s %s=%s points at a non-diagram card" % (cc["concept_id"], f, x))
    for md_id in diagrams:
        if "{{DIAGRAM:%s}}" % md_id not in s:
            errs.append("token of %s not in the plan" % md_id)
    for tok in set(re.findall(r"\{\{DIAGRAM:([^}<>]+)\}\}", s)):
        if tok not in diagrams:
            errs.append("token {{DIAGRAM:%s}} has no diagram node" % tok)
    for x in removed_ids:
        if x not in diagrams and '"%s"' % x in s and x not in {v for (_, _, v) in pre}:
            errs.append("removed card id %s is still referenced" % x)
    sm = {md["id"]: md for t in topics_of(src) for md in t["media"]}
    for k, md in sm.items():
        if is_card(md):
            if md.get("build_status") == "built":
                errs.append("a BUILT card %s would be dropped: stop and ask" % k)
            continue
        nk = rename.get(k, k)
        if nk not in nodes:
            errs.append("live media %s (%s) is missing from the new plan" % (k, md.get("type")))
            continue
        a, b = copy.deepcopy(md), copy.deepcopy(nodes[nk][1])
        if k != nk:
            a = json.loads(json.dumps(a).replace('"%s"' % k, '"%s"' % nk))
        if a != b:
            errs.append("live media %s changed" % k)
    if kept_renamed:
        errs.append("kept (non-card) images would be renumbered: %s" % kept_renamed)
    changed = diff_paths(src, plan)
    bad = [p for p in changed if not OK_PATHS.match(p)]
    if bad:
        errs.append("unexpected changes: %s" % bad[:10])
    if errs:
        print("\n".join("ERROR " + e for e in errs[:40]))
        raise SystemExit("%d integrity errors in the build" % len(errs))
    nvid = sum(1 for _, (t, md) in nodes.items() if md["type"] == "video")
    ntool = sum(1 for _, (t, md) in nodes.items() if md["type"] == "2d_tool")
    print("build ok: %d old cards removed, %d DIAGRAM nodes, %d concept images / %d videos / %d tools identical to the live plan, "
          "%d ids renumbered (all diagram ids), %d pre-existing stale references left as they are, %d changed paths all expected" %
          (len(removed_ids), len(diagrams), sum(1 for k, md in sm.items() if md.get("type") == "image" and not is_card(md)), nvid, ntool,
           len(rename), len(pre & link_problems(plan)), len(changed)))


# ====================================================================== upload
def upload(c, n, go):
    H = here(c, n)
    meta = load(os.path.join(H, "meta.json"))
    cid = meta["chapter_id"]
    target = meta["target_version"]
    out = os.path.join(H, "out", "%s_v%d.json" % (cid, target))
    plan = load(out)
    assert plan["chapter_id"] == cid and plan["phase"] == 2 and plan["chapter_master_id"] == meta["master"] and plan["version"] == target
    versions = get(cid + "/versions")
    by = {v["version"]: v for v in versions}
    act = [v for v in versions if v["isActive"]]
    if not act or act[0]["version"] != meta["base_version"]:
        raise SystemExit("the active version of %s is not v%d any more: stop and ask" % (cid, meta["base_version"]))
    newest = max(by)
    if meta["overwrite_draft"]:
        if newest != target or by[target]["status"] != "draft":
            raise SystemExit("expected the draft v%d to be the newest version of %s: stop and ask" % (target, cid))
    elif newest != meta["newest_version"] or target != newest + 1:
        raise SystemExit("%s has a new version (newest v%d) since prepare: stop and ask" % (cid, newest))
    live, _ = plan_of(cid, meta["base_version"])
    saved = load(os.path.join(H, "source", meta["base_source"]))
    if live != saved:
        # edited IN PLACE by someone since the snapshot: only edits of fields of existing NON-CARD media nodes may be rebased onto
        paths = diff_paths(saved, live)
        for pth in paths:
            m_ = re.match(r"^/modules\[(\d+)\]/segments\[(\d+)\]/topics\[(\d+)\]/media\[(\d+)\]/", pth)
            if not m_:
                raise SystemExit("the live v%d of %s differs from the snapshot outside media-node fields (%s): stop and ask" % (meta["base_version"], cid, pth))
            mi, si, ti, k = [int(x) for x in m_.groups()]
            a_ = saved["modules"][mi]["segments"][si]["topics"][ti]["media"][k]
            b_ = live["modules"][mi]["segments"][si]["topics"][ti]["media"][k]
            if a_["id"] != b_["id"] or is_card(a_) or is_card(b_):
                raise SystemExit("the live plan changed a card node or reordered media (%s): stop and ask" % pth)
        print("REBASE: live v%d was edited in place (%d media-node field edits, e.g. %s); rebuilding on the new live plan" %
              (meta["base_version"], len(paths), paths[0]))
        new_src = os.path.join(H, "source", "%s_v%d_rebased.json" % (cid, meta["base_version"]))
        dump(live, new_src)
        meta["base_source"] = os.path.basename(new_src)
        meta["base_sha256"] = hashlib.sha256(open(new_src, "rb").read()).hexdigest()
        dump(meta, os.path.join(H, "meta.json"))
        build(c, n)
        plan = load(out)
        saved = live
    print("%s: live v%d unchanged; new v%d %s; active v%d will be archived" % (cid, meta["base_version"], target,
          "OVERWRITES the draft (backup saved)" if meta["overwrite_draft"] else "is a new version", meta["base_version"]))
    if not go:
        print("dry run, nothing sent")
        return
    if meta["overwrite_draft"]:
        bp = os.path.join(H, "source", "%s_v%d_draft_backup.json" % (cid, target))
        if not os.path.exists(bp):
            old, _ = plan_of(cid, target)
            dump(old, bp)
    spec = importlib.util.spec_from_file_location("upload_lp", os.path.join(ROOT, "upload", "upload_lp.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    url = BASE + m.PATH + "?activate=true" + ("&force=true" if meta["overwrite_draft"] else "")
    status, text, sent = m.post(url, out, {"chapter_master_id": str(meta["master"]), "phase": "2"}, 900)
    a = json.loads(text)
    print("http", status, "sent MB", round(sent / 1048576, 2), json.dumps({k: a[k] for k in a if k != "diff"}, ensure_ascii=False)[:700])
    if status >= 400 or not a.get("success") or a.get("validation_errors"):
        raise SystemExit("UPLOAD FAILED: %s" % json.dumps(a.get("validation_errors"))[:800])
    back, pm = plan_of(cid, target)
    after = get(cid + "/versions")
    prev, _ = plan_of(cid, meta["base_version"])
    ok = (back == plan, pm.get("isActive"), prev == saved)
    print("read-back identical: %s | v%d active: %s | previous live v%d still identical: %s | rows for v%d: %d" %
          (ok[0], target, ok[1], meta["base_version"], ok[2], target, sum(1 for v in after if v["version"] == target)))
    st = os.path.join(HERE_TOOLS, "STATUS.json")
    S = load(st) if os.path.exists(st) else {}
    S[cid] = {"uploaded_version": target, "active": bool(ok[1]), "read_back_identical": bool(ok[0]), "previous_unchanged": bool(ok[2]),
              "diagrams": sum(1 for t in topics_of(plan) for md in t["media"] if md.get("title", "").startswith(DIAGRAM))}
    dump(S, st)
    if not (ok[0] and ok[1] and ok[2]):
        raise SystemExit("post-upload verification FAILED: stop and ask")


# ====================================================================== status / report
def status(c, n):
    H = here(c, n)
    if not os.path.exists(os.path.join(H, "meta.json")):
        print("not prepared")
        return
    meta = load(os.path.join(H, "meta.json"))
    V = load_validator(H)
    segs = [(s["file"], os.path.exists(os.path.join(H, "map", s["file"]))) for s in meta["segments"]]
    print("inventory files:", segs)
    for ch in meta["chunks"]:
        p = os.path.join(H, "map", "out_%s.json" % ch)
        if os.path.exists(p):
            try:
                rc = V.main(p, ch, H, meta, quiet=True)
            except Exception as e:
                rc = "ERR %s" % e
            print("chunk %s: out exists, validator rc=%s" % (ch, rc))
        else:
            print("chunk %s: no output yet" % ch)


def report(c, n):
    H = here(c, n)
    meta = load(os.path.join(H, "meta.json"))
    dm = load(os.path.join(H, "map", "diagram_map.json"))
    req = [i for i in dm["items"] if i["decision"] == "required"]
    opt = [i for i in dm["items"] if i["decision"] == "optional"]
    sync = [(i["lp_concept_id"].split(".")[-1], i["role"]) for i in req if i.get("needs_lp_text_sync")]
    rows = "\n".join("| %s | %s | %s |" % (i["media_id"], i["role"].replace("worked_example", "worked example"), i["diagram"]["diagram_type"]) for i in req)
    notes = ""
    for ch in meta["chunks"]:
        p = os.path.join(H, "map", "notes_%s.md" % ch)
        if os.path.exists(p):
            notes += "\n### Chunk %s notes (from the decision agent)\n%s\n" % (ch, open(p, encoding="utf-8").read().strip())
    cnt = {}
    for i in dm["items"]:
        cnt.setdefault(i["role"], {}).setdefault(i["decision"], 0)
        cnt[i["role"]][i["decision"]] += 1
    st = load(os.path.join(HERE_TOOLS, "STATUS.json")) if os.path.exists(os.path.join(HERE_TOOLS, "STATUS.json")) else {}
    up = st.get(meta["chapter_id"])
    text = "# Class %d Ch %d %s - V2 diagram update, 23 Nov 2026\n\n" % (meta["class_no"], meta["chapter_no"], meta["chapter_name"])
    text += ("Source: LIVE V2 `%s` v%d (taken from staging). Result: new V2 version v%d%s. Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, "
             "stamp skipped, videos/tools/concept images untouched.\n\n" % (meta["chapter_id"], meta["base_version"], meta["target_version"],
              " (uploaded ACTIVE, read back identical)" if up and up.get("active") else " (not uploaded yet)"))
    text += "## Decisions (%d items from %d units)\n%s\n\n" % (len(dm["items"]), meta["units"], json.dumps(cnt))
    text += "Optional, NOT added: %s\n\nneeds_lp_text_sync: %s\n\n" % ([(i["lp_concept_id"].split(".")[-1], i["role"]) for i in opt], sync)
    text += "## The %d diagrams\n| id | side | type |\n|---|---|---|\n%s\n" % (len(req), rows)
    text += notes
    open(os.path.join(H, "REPORT.md"), "w", encoding="utf-8", newline="\n").write(text)
    print("wrote REPORT.md")


LAUNCHED = os.path.join(HERE_TOOLS, "launched.json")
ORDER = [6, 7, 8, 5]          # class order of the run


def all_jobs():
    """Every agent job of every prepared chapter in run order: (key, prompt file, ready?)."""
    jobs = []
    metas = []
    for mp in glob.glob(os.path.join(ROOT, "chapters", "maths*_ch*", "v2_diagrams", "meta.json")):
        m = load(mp)
        metas.append((ORDER.index(m["class_no"]) if m["class_no"] in ORDER else 9, m["chapter_no"], os.path.dirname(mp), m))
    for _, _, H, m in sorted(metas, key=lambda x: (x[0], x[1])):
        tag = "%d.%d" % (m["class_no"], m["chapter_no"])
        inv_done = all(os.path.exists(os.path.join(H, "map", sg["file"])) for sg in m["segments"])
        for sg in m["segments"]:
            jobs.append(("%s:%s" % (tag, sg["agent"]), os.path.join(H, "agents", sg["agent"] + ".md"), True,
                         os.path.exists(os.path.join(H, "map", sg["file"]))))
        for ch in m["chunks"]:
            done = os.path.exists(os.path.join(H, "map", "out_%s.json" % ch)) and os.path.exists(os.path.join(H, "map", "notes_%s.md" % ch))
            jobs.append(("%s:chunk_%s" % (tag, ch), os.path.join(H, "agents", "chunk_%s.md" % ch), inv_done, done))
    return jobs


def queue(n, mark=None):
    done_l = load(LAUNCHED) if os.path.exists(LAUNCHED) else {}
    if mark:
        for k in mark:
            done_l[k] = "launched"
        dump(done_l, LAUNCHED)
        print("marked", mark)
        return
    out = []
    jobs = [j for j in all_jobs() if not j[3] and j[0] not in done_l and j[2]]
    jobs.sort(key=lambda j: 0 if ":chunk_" in j[0] else 1)        # finish chapters in progress first, then start new inventories
    for key, pf, ready, finished in jobs:
        out.append((key, pf))
        if len(out) >= n:
            break
    for key, pf in out:
        print(key, pf)
    if not out:
        print("nothing ready to launch")


def rechunk(c, n):
    """Recompute the decision chunks from the saved inventory (no network). Chunks whose unit set changed lose their stale outputs."""
    H = here(c, n)
    meta = load(os.path.join(H, "meta.json"))
    units = load(os.path.join(H, "map", "inventory.json"))
    old = {}
    for ch in meta["chunks"]:
        p = os.path.join(H, "map", "in_%s.json" % ch)
        if os.path.exists(p):
            old[ch] = sorted(u["unit"] for u in load(p))
    chunks = make_chunks(units)
    done_l = load(LAUNCHED) if os.path.exists(LAUNCHED) else {}
    tag = "%d.%d" % (c, n)
    for ch in list(old):
        if ch not in chunks:
            for f in ("in_%s.json" % ch, "out_%s.json" % ch, "notes_%s.md" % ch):
                if os.path.exists(os.path.join(H, "map", f)):
                    os.remove(os.path.join(H, "map", f))
            done_l.pop("%s:chunk_%s" % (tag, ch), None)
    for ch, tids in chunks.items():
        us = [u for u in units if u["topic_id"] in tids]
        if old.get(ch) != sorted(u["unit"] for u in us):
            for f in ("out_%s.json" % ch, "notes_%s.md" % ch):
                if os.path.exists(os.path.join(H, "map", f)):
                    os.remove(os.path.join(H, "map", f))
            done_l.pop("%s:chunk_%s" % (tag, ch), None)
        dump(us, os.path.join(H, "map", "in_%s.json" % ch))
    meta["chunks"] = chunks
    dump(meta, os.path.join(H, "meta.json"))
    dump(done_l, LAUNCHED)
    write_agent_files(c, n, meta)
    seen = [u["unit"] for ch in chunks for u in load(os.path.join(H, "map", "in_%s.json" % ch))]
    assert len(seen) == len(set(seen)) == len(units), "rechunk still broken"
    print("rechunked %s: %s" % (tag, {k: sum(items_of(u) for u in units if u["topic_id"] in v) for k, v in chunks.items()}))


def board():
    """One line per prepared chapter: inventory files done/total, decision chunks done(valid)/total, stage."""
    st = load(os.path.join(HERE_TOOLS, "STATUS.json")) if os.path.exists(os.path.join(HERE_TOOLS, "STATUS.json")) else {}
    rows = []
    for mp in sorted(glob.glob(os.path.join(ROOT, "chapters", "maths*_ch*", "v2_diagrams", "meta.json"))):
        H = os.path.dirname(mp)
        meta = load(mp)
        cid = meta["chapter_id"]
        inv_ok = sum(1 for sg in meta["segments"] if os.path.exists(os.path.join(H, "map", sg["file"])))
        V = load_validator(H)
        done = valid = 0
        for ch in meta["chunks"]:
            p = os.path.join(H, "map", "out_%s.json" % ch)
            if os.path.exists(p) and os.path.exists(os.path.join(H, "map", "notes_%s.md" % ch)):
                done += 1
                try:
                    if V.main(p, ch, H, meta, quiet=True) == 0:
                        valid += 1
                except Exception:
                    pass
        if cid in st and st[cid].get("active") and st[cid].get("uploaded_version") == meta["target_version"]:
            stage = "UPLOADED v%d" % meta["target_version"]
        elif os.path.exists(os.path.join(H, "out", "%s_v%d.json" % (cid, meta["target_version"]))):
            stage = "BUILT (not uploaded)"
        elif valid == len(meta["chunks"]):
            stage = "READY TO MERGE"
        elif inv_ok == len(meta["segments"]):
            stage = "READY FOR DECISION AGENTS" if done == 0 else "decision agents running"
        else:
            stage = "inventory running"
        rows.append((meta["class_no"], meta["chapter_no"], "%d/%d" % (inv_ok, len(meta["segments"])), "%d(%d ok)/%d" % (done, valid, len(meta["chunks"])), stage))
    for r in sorted(rows):
        print("Class %d Ch %-2d | inventory %-5s | chunks %-10s | %s" % r)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["prepare", "status", "merge", "build", "report", "upload", "board", "queue", "mark", "rechunk"])
    ap.add_argument("cls", type=int, nargs="?")
    ap.add_argument("chapter", type=int, nargs="?")
    ap.add_argument("--go", action="store_true")
    ap.add_argument("--keys", nargs="*", default=[])
    a = ap.parse_args()
    c, n = a.cls, a.chapter
    if a.cmd == "board":
        board()
        return
    if a.cmd == "queue":
        queue(a.cls or 5)
        return
    if a.cmd == "mark":
        queue(0, mark=a.keys)
        return
    if a.cmd == "rechunk":
        rechunk(c, n)
        return
    if a.cmd == "prepare":
        prepare(c, n)
    elif a.cmd == "status":
        status(c, n)
    elif a.cmd == "merge":
        sys.exit(merge(c, n))
    elif a.cmd == "build":
        build(c, n)
    elif a.cmd == "report":
        report(c, n)
    elif a.cmd == "upload":
        upload(c, n, a.go)


if __name__ == "__main__":
    main()
