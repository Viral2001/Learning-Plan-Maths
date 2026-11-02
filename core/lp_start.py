# -*- coding: utf-8 -*-
"""Start a new chapter: the deterministic first step of the /lp skill (.claude/skills/lp/SKILL.md).

    python -I -X utf8 core/lp_start.py "<chapter>" "<book pdf>" ["<teacher instruction>"] [--pages A-B] [--out DIR] [--force]
    python -I -X utf8 core/lp_start.py --raw "<chapter>, <book pdf>, <teacher instruction>"      (the text after /lp)

<chapter>  "class 7 ch 3", "7.3", "maths7_ch3", "std 8 part 2 ch 1", "grade 10 chapter 4" ...
           Class 7 / Class 8 "Part II" chapters are filed after Part I (upload/chapter_master_ids.md): Class 7 Part II
           Ch N is maths7_ch(8+N), Class 8 Part II Ch N is maths8_ch(7+N). This script applies that offset.
<book pdf> the textbook, either one chapter or the whole book. For a whole book the chapter pages are found by
           the "<N>.1" section heading; if that fails the script stops and asks for --pages.

It does the parts that need no judgement, then stops. It never uploads and never touches the database.
    1. parse the chapter, resolve the repo folder name and the last-known chapter_master_id
    2. copy chapter_template/ into <out>/ (default chapters/maths<G>_ch<N>/new_design/) and fill chapter.config.json
    3. cut the chapter out of the book: book/chapter.pdf, book/pages.json, book/chapter_text.md, book/outline.json,
       and one PNG per page (book/page_NNN.png) so figures can be looked at
    4. write lp_brief.md (the inputs, the teacher instruction verbatim, what is still to do) and lp_state.json

Exit code 0 = scaffold ready, 2 = needs input from the user (message on stderr says what), 1 = error.
"""
from __future__ import annotations

import argparse
import glob
import io
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TEMPLATE = os.path.join(ROOT, "chapter_template")
MASTER_IDS = os.path.join(ROOT, "upload", "chapter_master_ids.md")
PART2_OFFSET = {7: 8, 8: 7}          # Part II chapter N is filed as ch(offset+N)
GRADES = (6, 7, 8, 9, 10)
ASSET_BASE = ("https://media.singularity-learn.com/learning_plan_assets/V2/cbse/cbse/english/"
              "class_{grade}/mathematics/ch_{chapter_no}")

# template file -> scaffolded name (the template keeps .template / .sample so it is never imported by accident)
COPY = {
    "build.py": "build.py",
    "chapter.config.README.md": "chapter.config.README.md",
    "content.py.template": "content.py",
    "concept_plan.py.template": "concept_plan.py",
    "media_specs.py.template": "media_specs.py",
    "book_rules.json.sample": "book_rules.json",
    "name_slots.json.sample": "name_slots.json",
    "MEDIA_BRIEF.md.template": "MEDIA_BRIEF.md",
}


class NeedInput(Exception):
    """Something only the user can answer; main() exits 2 with this message."""


# ---------------------------------------------------------------------------
# 1. chapter reference
# ---------------------------------------------------------------------------
def parse_chapter(text):
    """-> dict(grade, named_no, part2, folder_no). Raises NeedInput when it cannot tell."""
    s = text.strip().lower().replace("_", " ")
    m = re.search(r"maths?\s*(\d+)\s*ch\s*(\d+)", s)
    if m:                                         # a repo folder name: already the filed number
        return _finish(int(m.group(1)), int(m.group(2)), False, folder_no=int(m.group(2)))
    part2 = bool(re.search(r"\bpart\s*(?:ii|2)\b|\bp\s*2\b", s))
    s = re.sub(r"\bpart\s*(?:i{1,2}|[12])\b|\bp\s*[12]\b", " ", s)
    mg = re.search(r"\b(?:class|std|standard|grade|c)\s*(\d+)", s)
    mc = re.search(r"\b(?:chapter|chap|ch)\.?\s*(\d+)", s)
    if mg and mc:
        return _finish(int(mg.group(1)), int(mc.group(1)), part2)
    if mc:                                        # "9 ch 3", "chapter 5 of 9"
        lead = re.match(r"\s*(\d+)\b", s)
        return _finish(int(lead.group(1)) if lead else None, int(mc.group(1)), part2)
    m = re.match(r"\s*(\d+)\s*[.:/\- ]\s*(\d+)\s*$", s)       # "7.3", "7 3"
    if m:
        return _finish(int(m.group(1)), int(m.group(2)), part2)
    if mg:
        rest = s[:mg.start()] + " " + s[mg.end():]
        nums = re.findall(r"\d+", rest)
        if len(nums) == 1:                        # "class 9, 5"
            return _finish(int(mg.group(1)), int(nums[0]), part2)
    raise NeedInput("could not read a class and chapter number from %r. Write it like 'class 7 ch 3', '7.3' "
                    "or 'maths7_ch3'." % text)


def _finish(grade, named, part2, folder_no=None):
    if grade not in GRADES:
        raise NeedInput("could not read a class (6 to 10) from the chapter reference; write it like "
                        "'class 7 ch 3'.")
    if folder_no is None:
        folder_no = named
        if part2:
            if grade not in PART2_OFFSET:
                raise NeedInput("'Part II' only applies to Class 7 and Class 8 (got Class %d)." % grade)
            folder_no = PART2_OFFSET[grade] + named
    return {"grade": grade, "named_no": named, "part2": part2, "folder_no": folder_no}


def last_known_master_id(grade, folder_no):
    """The id in upload/chapter_master_ids.md, or None. 'Last known' only: core/check_master_id.py is the check."""
    if not os.path.exists(MASTER_IDS):
        return None
    section = None
    with io.open(MASTER_IDS, encoding="utf-8") as f:
        for line in f:
            h = re.match(r"##\s+Grade\s+(\d+)", line)
            if h:
                section = int(h.group(1))
                continue
            if section == grade:
                r = re.match(r"\|\s*ch(\d+)\s*\|\s*(\d+)\s*\|", line)
                if r and int(r.group(1)) == folder_no:
                    return int(r.group(2))
    return None


def sibling_defaults(grade):
    """subject_ref_id / medium_id from a built chapter of the same class, and every media_tag already taken."""
    subject = medium = None
    tags = set()
    for p in sorted(glob.glob(os.path.join(ROOT, "chapters", "maths*_ch*", "new_design", "chapter.config.json"))):
        try:
            with io.open(p, encoding="utf-8") as f:
                c = json.load(f)
        except Exception:
            continue
        if c.get("media_tag"):
            tags.add(c["media_tag"])
        if c.get("grade") == grade and c.get("subject_ref_id") and subject is None:
            subject, medium = c["subject_ref_id"], c.get("medium_id", 1)
    return subject, medium or 1, tags


def pick_media_tag(grade, taken):
    for ch in "xyzwvutsrqpnmkjhgfedcba":
        t = "c%d%s" % (grade, ch)
        if t not in taken:
            return t
    raise SystemExit("no free media_tag left for class %d" % grade)


# ---------------------------------------------------------------------------
# 3. the book
# ---------------------------------------------------------------------------
SECTION = re.compile(r"^\s*(\d{1,2})\.(\d{1,2})(?:\.\d{1,2})?\s+\S")


def _lines(text):
    return [ln for ln in text.splitlines() if ln.strip()]


def find_chapter_pages(doc, chapter_no, forced=None):
    """0-based inclusive (first, last) page range of the chapter in `doc`.  Raises NeedInput when unsure."""
    n = len(doc)
    if forced:
        a, b = forced
        if not (1 <= a <= b <= n):
            raise NeedInput("--pages %d-%d is outside the book (it has %d pages)." % (a, b, n))
        return a - 1, b - 1
    if n <= 45:                                   # a one-chapter file
        return 0, n - 1
    texts = [doc[i].get_text() for i in range(n)]

    def heads(i):                                 # chapter numbers of the section headings on page i
        return {int(SECTION.match(ln).group(1)) for ln in _lines(texts[i]) if SECTION.match(ln)}

    starts = [i for i in range(n)
              if any((m := SECTION.match(ln)) and int(m.group(1)) == chapter_no and int(m.group(2)) == 1
                     for ln in _lines(texts[i]))]
    # a contents page lists several chapters' headings; a real chapter opening does not
    starts = [i for i in starts if len(heads(i)) <= 2 and (chapter_no + 1) not in heads(i)]
    if not starts:
        present = sorted(set().union(*(heads(i) for i in range(n))))
        raise NeedInput("could not find where chapter %d starts in this %d-page book (no '%d.1' section heading "
                        "in the text layer). Chapter numbers whose section headings ARE in this file: %s. "
                        "If %d is not among them this is the wrong book or part; otherwise re-run with "
                        "--pages A-B (1-based page numbers of the PDF)."
                        % (chapter_no, n, chapter_no, present or "none", chapter_no))
    first = starts[0]
    last = n - 1
    for i in range(first + 1, n):
        hs = heads(i)
        if (chapter_no + 1) in hs and chapter_no not in hs:
            last = i - 1
            break
    return first, last


def chapter_title(doc, first, chapter_no):
    """The chapter's title: the first non-section, non-numeric line near the top of its first page."""
    for ln in _lines(doc[first].get_text())[:12]:
        t = ln.strip()
        if SECTION.match(t) or re.search(r"\d", t) or re.match(r"(?i)chapter\b", t) or len(t) < 3:
            continue                      # running heads like '0905cH10' and page numbers are not titles
        if len(t.split()) > 8 or len(t) > 60 or re.search(r"[,.;:]", t):
            return None                   # a body sentence, so the title is not in the text layer

        return t
    return None


def extract_book(pdf, chapter_no, forced, out_dir, dpi=100):
    import pymupdf
    doc = pymupdf.open(pdf)
    first, last = find_chapter_pages(doc, chapter_no, forced)
    title = chapter_title(doc, first, chapter_no)
    bdir = os.path.join(out_dir, "book")
    os.makedirs(bdir, exist_ok=True)
    sub = pymupdf.open()
    sub.insert_pdf(doc, from_page=first, to_page=last)
    sub.save(os.path.join(bdir, "chapter.pdf"))
    pages, md, outline = {}, [], []
    for k, i in enumerate(range(first, last + 1), 1):
        txt = doc[i].get_text()
        pages[str(k)] = txt
        md.append("<!-- chapter page %d (pdf page %d) -->\n%s" % (k, i + 1, txt))
        for ln in _lines(txt):
            if SECTION.match(ln) and int(SECTION.match(ln).group(1)) == chapter_no:
                outline.append({"page": k, "heading": ln.strip()})
        pix = doc[i].get_pixmap(dpi=dpi)
        pix.save(os.path.join(bdir, "page_%03d.png" % k))
    with io.open(os.path.join(bdir, "pages.json"), "w", encoding="utf-8") as f:
        json.dump(pages, f, ensure_ascii=False, indent=1)
    with io.open(os.path.join(bdir, "chapter_text.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    with io.open(os.path.join(bdir, "outline.json"), "w", encoding="utf-8") as f:
        json.dump(outline, f, ensure_ascii=False, indent=1)
    chars = sum(len(t) for t in pages.values())
    # OCR-style damage ("TWo", "guantities"): a lower-case letter followed by a capital inside a word
    glitches = len(re.findall(r"\b[a-z]+[A-Z][a-z]+\b", " ".join(pages.values())))
    return {"pdf_pages": [first + 1, last + 1], "n_pages": last - first + 1, "title": title,
            "outline": outline, "chars": chars, "book_total_pages": len(doc),
            "glitches_per_1000": round(1000.0 * glitches / max(chars, 1), 1)}


# ---------------------------------------------------------------------------
# 2. scaffold
# ---------------------------------------------------------------------------
def scaffold(out_dir, cfg, info, force):
    os.makedirs(out_dir, exist_ok=True)
    for sub in ("media_specs", "video_scripts"):
        os.makedirs(os.path.join(out_dir, sub), exist_ok=True)
    written, kept = [], []
    for src, dst in COPY.items():
        d = os.path.join(out_dir, dst)
        if os.path.exists(d) and not force:
            kept.append(dst)
            continue
        with io.open(os.path.join(TEMPLATE, src), encoding="utf-8") as f:
            text = f.read()
        text = text.replace("TODO Chapter Name", info["name"]).replace("TODO_media_tag", cfg["media_tag"])
        with io.open(d, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        written.append(dst)
    d = os.path.join(out_dir, "chapter.config.json")
    if force or not os.path.exists(d):
        with io.open(d, "w", encoding="utf-8", newline="\n") as f:
            json.dump(cfg, f, ensure_ascii=False, indent=2)
        written.append("chapter.config.json")
    else:
        kept.append("chapter.config.json")
    # content.py carries the identity block by hand (see its comment); fill the obvious fields
    cp = os.path.join(out_dir, "content.py")
    if "content.py" in written:
        with io.open(cp, encoding="utf-8") as f:
            t = f.read()
        t = (t.replace('"grade": 0,', '"grade": %d,' % cfg["grade"])
              .replace('"label": "Class N",', '"label": "Class %d",' % cfg["grade"])
              .replace('"chapter_no": 0,', '"chapter_no": %d,' % cfg["chapter_no"]))
        with io.open(cp, "w", encoding="utf-8", newline="\n") as f:
            f.write(t)
    return written, kept


def existing_flows(grade, folder_no, chapters_dir):
    """Other places this chapter already exists, so the skill can ask before building a second copy."""
    found = []
    for p in glob.glob(os.path.join(chapters_dir, "maths%d_ch%d*" % (grade, folder_no))):
        found.append(os.path.relpath(p, ROOT))
    if grade in (9, 10):
        p = os.path.join(ROOT, "docs", "Yash_9&10", "std%d_ch%d" % (grade, folder_no))
        if os.path.isdir(p):
            found.append(os.path.relpath(p, ROOT))
    return found


def write_brief(out_dir, ref, cfg, info, book, instruction, pdf, master_id, flags, others):
    rel = os.path.relpath(out_dir, ROOT).replace("\\", "/") if out_dir.startswith(ROOT) else out_dir
    lines = [
        "# /lp brief: Class %d, %s" % (cfg["grade"], cfg["chapter_name"]),
        "",
        "Generated by `core/lp_start.py`. Everything below is an input or a fact to check; nothing here is approved yet.",
        "",
        "## Inputs",
        "- Asked for: `%s`" % ref["asked"],
        "- Class %d, chapter named %d%s -> repo folder `maths%d_ch%d` (`%s`)"
        % (ref["grade"], ref["named_no"], " (Part II)" if ref["part2"] else "", ref["grade"], ref["folder_no"], rel),
        "- Book: `%s` (%d pages in the file; chapter = pdf pages %d-%d, %d pages, %d characters of text)"
        % (pdf, book["book_total_pages"], book["pdf_pages"][0], book["pdf_pages"][1], book["n_pages"], book["chars"]),
        "- Chapter title read from the first page: %r (check it)" % (book["title"] or "NOT FOUND"),
        "- chapter_master_id: %s" % ("%d (LAST KNOWN, from upload/chapter_master_ids.md; confirm live with "
                                     "core/check_master_id.py before any upload)" % master_id if master_id
                                     else "UNKNOWN: ask the user for the issued id"),
        "",
        "## Teacher instruction (verbatim)",
        "",
        ("> " + instruction.strip().replace("\n", "\n> ")) if instruction and instruction.strip() else "_none given_",
        "",
        "## Flags to settle before building",
    ]
    lines += ["- " + f for f in flags] or ["- none"]
    if others:
        lines += ["", "## This chapter already exists elsewhere", ""] + ["- `%s`" % o for o in others]
    lines += [
        "",
        "## Sections found in the chapter text",
        "",
    ] + ["- p%d  %s" % (o["page"], o["heading"]) for o in book["outline"]] + [
        "",
        "## Scaffold (all unfinished: every TODO must go before build.py will pass)",
        "- `chapter.config.json` filled from the facts above (eqcheck defaults to `signed`; `solutions` is on)",
        "- `content.py`, `concept_plan.py`, `media_specs.py`, `book_rules.json`, `name_slots.json`, `MEDIA_BRIEF.md`: templates",
        "- `book/`: `chapter.pdf`, `pages.json`, `chapter_text.md`, `outline.json`, `page_NNN.png`",
        "",
        "Next: follow `.claude/skills/lp/SKILL.md` from step 2.",
        "",
    ]
    with io.open(os.path.join(out_dir, "lp_brief.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))


def split_raw(raw):
    """The text after '/lp' -> (chapter, book path, instruction).

    '/lp class 7 ch 3, C:\\books\\Part II (new).pdf, use cricket examples': the book is the longest tail of the
    comma-separated head that is an existing file ending in .pdf (paths may hold commas and brackets); everything
    before it is the chapter, everything after it the instruction."""
    m = re.search(r"\.pdf\b", raw, re.I)
    if not m:
        raise NeedInput("no .pdf path found in %r. Use: /lp <chapter>, <path to the book pdf>, <teacher instruction "
                        "(optional)>" % raw)
    head, tail = raw[:m.end()], raw[m.end():]
    parts = head.split(",")
    for k in range(1, len(parts)):
        cand = ",".join(parts[k:]).strip().strip('"\'')
        if os.path.isfile(cand):
            return ",".join(parts[:k]).strip(), cand, tail.lstrip(" ,;\n").strip()
    cand = ",".join(parts[1:]).strip().strip('"\'')
    raise NeedInput("book file not found: %s" % (cand or head))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("chapter", nargs="?", default="")
    ap.add_argument("book", nargs="?", default="")
    ap.add_argument("instruction", nargs="?", default="")
    ap.add_argument("--raw", help="the whole text after /lp: '<chapter>, <book pdf>, <instruction>'")
    ap.add_argument("--pages", help="1-based pdf page range of the chapter, e.g. 41-68")
    ap.add_argument("--out", help="chapter folder to create (default chapters/maths<G>_ch<N>/new_design)")
    ap.add_argument("--force", action="store_true", help="overwrite scaffold files that already exist")
    ap.add_argument("--master-id", type=int, help="chapter_master_id when it is not in upload/chapter_master_ids.md")
    ap.add_argument("--subject-ref-id", type=int, help="subject_ref_id when no chapter of that class is built yet")
    a = ap.parse_args(argv)

    try:
        if a.raw:
            a.chapter, a.book, a.instruction = split_raw(a.raw)
        if not a.chapter or not a.book:
            raise NeedInput("give the chapter and the book: /lp <chapter>, <path to the book pdf>, <teacher "
                            "instruction (optional)>")
        ref = parse_chapter(a.chapter)
        ref["asked"] = a.chapter
        pdf = os.path.abspath(a.book.strip().strip('"'))
        if not os.path.isfile(pdf):
            raise NeedInput("book file not found: %s" % pdf)
        forced = None
        if a.pages:
            m = re.fullmatch(r"\s*(\d+)\s*-\s*(\d+)\s*", a.pages)
            if not m:
                raise NeedInput("--pages must look like 41-68")
            forced = (int(m.group(1)), int(m.group(2)))
        g, fno = ref["grade"], ref["folder_no"]
        out_dir = os.path.abspath(a.out) if a.out else os.path.join(ROOT, "chapters", "maths%d_ch%d" % (g, fno),
                                                                    "new_design")
        others = [o for o in existing_flows(g, fno, os.path.join(ROOT, "chapters"))
                  if os.path.abspath(os.path.join(ROOT, o)) != os.path.dirname(out_dir)]
        if os.path.isdir(out_dir) and os.listdir(out_dir) and not a.force:
            raise NeedInput("%s already has files. Re-run with --force to overwrite the scaffold files "
                            "(your other files are never deleted), or pick another --out." % out_dir)

        # section headings in the book carry the number the book gives the chapter (named_no), not the filed one
        book = extract_book(pdf, ref["named_no"], forced, out_dir)
    except NeedInput as e:
        sys.stderr.write("NEEDS INPUT: %s\n" % e)
        return 2

    subject, medium, taken = sibling_defaults(g)
    subject = a.subject_ref_id or subject
    master_id = a.master_id or last_known_master_id(g, fno)
    name = (book["title"] or "TODO Chapter Name")
    if name.isupper():
        name = name.title()
    media_tag = pick_media_tag(g, taken)
    cfg = {
        "chapter_id": "cbse_eng_maths%d_ch%d" % (g, fno),
        "phase": 2,
        "chapter_master_id": master_id or 0,
        "subject_ref_id": subject or 0,
        "medium_id": medium,
        "grade": g,
        "grade_band": "9_10" if g >= 9 else "6_8",
        "chapter_no": fno,
        "chapter_name": name,
        "media_tag": media_tag,
        "theorem_chapter": g >= 9,
        "eqcheck": "signed",
        "eqcheck_errata": [],
        "idea_topic_concept_range": [2, 4],
        "intro_requires_free_try_tool": True,
        "allow_words": [],
        "interactive_video_variant": True,
        "photo_rule_band": "none" if g >= 9 else "need_basis",
        "solutions": True,
        "asset_base_template": ASSET_BASE,
    }
    if g >= 9:
        cfg["solutions_video"] = False if g == 10 else True
    flags = []
    if not master_id:
        flags.append("chapter_master_id is not known: ask the user for the issued id (a wrong id uploads good "
                     "content to the wrong chapter and still says success).")
    if not subject:
        flags.append("subject_ref_id is not known (no built chapter of Class %d to copy it from): ask the user, "
                     "or read it from the live chapterMaster row with core/check_master_id.py." % g)
    if not book["title"]:
        flags.append("the chapter title could not be read from the text layer (it is probably an image): open "
                     "book/page_001.png and set chapter_name in chapter.config.json and content.py by hand.")
    if not book["outline"]:
        flags.append("no '%d.x' section headings found in the chapter text: the text layer may be damaged; "
                     "look at book/page_NNN.png instead." % ref["named_no"])
    if book["chars"] < 400 * book["n_pages"]:
        flags.append("very little text per page: the PDF may be scanned; read the page PNGs.")
    if book["glitches_per_1000"] >= 1.0:
        flags.append("the text layer is noisy (%.1f OCR-style glitches per 1000 characters, e.g. 'TWo', "
                     "'guantities'): do not trust numbers or signs from chapter_text.md; confirm each one "
                     "against book/page_NNN.png." % book["glitches_per_1000"])
    if forced is None and book["book_total_pages"] > 45:
        flags.append("the page range was found automatically (pdf pages %d-%d): check the first and last page "
                     "in book/ before trusting it." % tuple(book["pdf_pages"]))
    if ref["part2"] or g in PART2_OFFSET and fno != ref["named_no"]:
        flags.append("Part II numbering: the book calls it chapter %d, the folder and master id are ch%d."
                     % (ref["named_no"], fno))
    if g == 10 and os.path.isdir(os.path.join(ROOT, "docs", "Yash_9&10", "std10_ch%d" % fno)):
        flags.append("a Class 10 restructure folder already exists for this chapter (docs/Yash_9&10/std10_ch%d, "
                     "the /restructure-std10-lp flow). Ask the user which flow they want before building." % fno)
    if g >= 9:
        flags.append("Class 9/10: read docs/04_class9_10_variant.md first; it overrides docs/00 and docs/01 where "
                     "they differ.")

    written, kept = scaffold(out_dir, cfg, {"name": name}, a.force)
    write_brief(out_dir, ref, cfg, {"name": name}, book, a.instruction, pdf, master_id, flags, others)
    state = {"ref": ref, "out_dir": out_dir, "pdf": pdf, "pages": book["pdf_pages"], "title": book["title"],
             "master_id": master_id, "subject_ref_id": subject, "media_tag": media_tag, "flags": flags,
             "instruction": a.instruction, "written": written, "kept": kept}
    with io.open(os.path.join(out_dir, "lp_state.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

    print("scaffold ready: %s" % out_dir)
    print("  class %d, folder maths%d_ch%d, media_tag %s, master id %s, subject_ref_id %s"
          % (g, g, fno, media_tag, master_id or "UNKNOWN", subject or "UNKNOWN"))
    print("  chapter: %r  pdf pages %d-%d (%d pages, %d sections found)"
          % (name, book["pdf_pages"][0], book["pdf_pages"][1], book["n_pages"], len(book["outline"])))
    print("  written: %s" % ", ".join(written))
    if kept:
        print("  kept (already existed): %s" % ", ".join(kept))
    for fl in flags:
        print("  FLAG: " + fl)
    if others:
        print("  ALREADY EXISTS ELSEWHERE: " + ", ".join(others))
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
    sys.exit(main())
