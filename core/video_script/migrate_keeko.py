# -*- coding: utf-8 -*-
"""One-off, idempotent migration of a chapter's video scripts to the Keeko design (user, 28 Oct 2026).

Mechanical only; the content (the keeko part, the board-solution idea beats, NCERT fidelity) is rewritten by
authors afterwards. For each chapter folder (`.../new_design`) it:

  * writes name_slots.json (token -> original name, role, gender hint) and swaps every literal name for its
    {{NAME_n}} token (names beyond ten slots go to `_overflow`; authors must reword those);
  * deletes the recap videos (script files and worklist slots) and patches build.py so a rebuild does not
    recreate them (`video_focus` "RECAP" is skipped);
  * strips the recap and break parts and the [chintu] tags from every other script, turns the stop beat into the
    one "Think and tell." beat (pause 3, keeko "think"), zeroes every other pause, adds `keeko` to each beat and
    `keeko_end` to the script, and keeps the removed material in migration_notes/<key>.json for the authors;
  * adds `method_from` (the solved examples of the same concept) to each exercise slot of video_worklist.json;
  * replaces the `names` block of book_rules.json (the roles live in name_slots.json now).

Usage (repo root):  python -B core/video_script/migrate_keeko.py [--apply] <new_design folder> ...
Without --apply nothing is written. Running it again on a migrated chapter changes nothing.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

NAME_MAX = 10
ANCHOR_ROLE = "everyday-anchor child"
NONPERSON = re.compile(r"\b(city|town|place|village|mountain|peak|river|lake|country|state|district|capital|island|"
                       r"temple|fort|school|company|team)\b", re.I)
NONPERSON_NAME = re.compile(r"\b(mount|river|lake|fort|temple)\b", re.I)
TITLE_WORDS = {"shri", "sushri", "smt", "queen", "king", "coach", "mr", "mrs", "ms", "dr", "sir"}
FEMALE = re.compile(r"\b(girl|daughter|her|she|queen|mother|sister|woman|sushri|smt|madam)\b", re.I)
MALE = re.compile(r"\b(boy|son|his|he|king|father|brother|man|shri)\b", re.I)
STOP_LINE = re.compile(r"stop the video|say your answer|say it out loud|pause the video|your answer out loud|"
                       r"think and tell", re.I)
BOOKMARK = re.compile(r"<bookmark mark='([^']+)'/>")
CHINTU_TAG = re.compile(r"\[chintu\]\s*", re.I)
RECAP_FOCUS = re.compile(r'^(\s*)kind = \{"HOOK": "hook", "RECAP": "recap"\}\.get\(focus, "worked"\)[ \t]*$', re.M)
NAMES_NOTE = ("Names are {{NAME_n}} placeholders from name_slots.json (one character, one token, chapter-wide); "
              "a named person takes no gendered pronoun.")


def read(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def write(p: Path, data, apply: bool):
    if apply:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def gender_hint(role: str) -> str:
    f, m = bool(FEMALE.search(role)), bool(MALE.search(role))
    return "female" if f and not m else "male" if m and not f else ""


# ---------------------------------------------------------------- name slots
def build_slots(nd: Path, scripts: list[dict]):
    """token -> {original, role, in_book, gender_hint, uses}; names past the tenth go to `_overflow`."""
    rules = read(nd / "book_rules.json") if (nd / "book_rules.json").exists() else {}
    book = dict(rules.get("names") or {})
    book.pop("Chintu", None)
    uses: dict[str, int] = {}
    for d in scripts:
        for n in (d["video_script"].get("names") or {}):
            uses[n] = uses.get(n, 0) + 1
    uses.pop("Chintu", None)
    cands = []
    order = {n: i for i, n in enumerate(book)}
    for n in sorted(set(book) | set(uses), key=lambda n: (order.get(n, 10**6), n)):
        role = book.get(n, "")
        if NONPERSON_NAME.search(n) or (role and NONPERSON.search(role) and ANCHOR_ROLE not in role):
            continue
        anchor = ANCHOR_ROLE in role
        in_book = n in book and not anchor
        cands.append({"original": n, "role": ("" if anchor else role) or "(not listed in book_rules)",
                      "in_book": in_book, "anchor": anchor, "uses": uses.get(n, 0), "order": order.get(n, 10**6)})
    # book characters used first, then unused book characters, then the invented anchor children
    cands.sort(key=lambda c: (c["anchor"], c["uses"] == 0, -c["uses"], c["order"], c["original"]))
    slots, overflow = {}, {}
    for i, c in enumerate(cands):
        if i < NAME_MAX:
            slots["{{NAME_%d}}" % (i + 1)] = {
                "original": c["original"],
                "role": c["role"] if not c["anchor"] else "everyday child, not a character of the book",
                "in_book": c["in_book"], "gender_hint": gender_hint(c["role"]), "uses": c["uses"]}
        elif c["uses"]:
            overflow[c["original"]] = c["role"]
    if overflow:
        slots["_overflow"] = overflow
    return slots


def name_patterns(slots: dict):
    pats = []
    for tok, info in slots.items():
        if not tok.startswith("{{"):
            continue
        full = info["original"]
        forms = {full}
        words = full.split()
        if len(words) > 1:
            forms |= {w for w in words if len(w) >= 4 and w.lower() not in TITLE_WORDS}
        for f in forms:
            pats.append((len(f), re.compile(r"(?<![A-Za-z])" + re.escape(f) + r"(?![A-Za-z])"), tok))
    pats.sort(key=lambda t: -t[0])
    return [(p, tok) for _, p, tok in pats]


def swap(obj, pats):
    if isinstance(obj, str):
        for p, tok in pats:
            obj = p.sub(tok, obj)
        return obj
    if isinstance(obj, list):
        return [swap(x, pats) for x in obj]
    if isinstance(obj, dict):
        return {k: swap(v, pats) for k, v in obj.items()}
    return obj


def scrub_chintu(o, in_narration=False):
    """Chintu -> Keeko in every field except the spoken lines (those are rewritten by authors)."""
    if isinstance(o, str):
        return o if in_narration else re.sub(r"Chintu", "Keeko", o, flags=re.I)
    if isinstance(o, list):
        return [scrub_chintu(x, in_narration) for x in o]
    if isinstance(o, dict):
        return {k: scrub_chintu(v, in_narration or k == "narration") for k, v in o.items()}
    return o


# ---------------------------------------------------------------- one script
def stop_beat(beats):
    hook = [b for b in beats if b["part"] == "hook"]
    for b in reversed(hook):
        if b.get("pause_after") or any(STOP_LINE.search(BOOKMARK.sub("", x)) for x in b["narration"]):
            return b
    return None


def to_think(b):
    marks_seen = []
    keep = []
    for line in b["narration"]:
        if STOP_LINE.search(BOOKMARK.sub("", line)):
            marks_seen += BOOKMARK.findall(line)
        else:
            keep.append(line)
    mark = marks_seen[0] if marks_seen else "think"
    b["narration"] = keep + ["<bookmark mark='%s'/>Think and tell." % mark]
    marks = dict(b.get("marks") or {})
    present = {m for x in b["narration"] for m in BOOKMARK.findall(x)}
    for k in [k for k in marks if k not in present]:
        del marks[k]
    for m in present - set(marks):
        marks[m] = "the question stays on the board while the child thinks"
    b["marks"] = marks
    b["pause_after"] = 3
    b["keeko"] = "think"


def migrate_script(d: dict, notes_dir: Path, apply: bool, report: dict):
    s = d["video_script"]
    if "keeko_end" in s:
        return False
    kind = s["kind"]
    key = d["key"]
    beats = s["beats"]
    removed = [{"part": b["part"], "key": b["key"], "narration": b["narration"], "on_screen": b["on_screen"]}
               for b in beats if b["part"] in ("break", "recap")]
    beats = [b for b in beats if b["part"] not in ("break", "recap")]
    stop = stop_beat(beats)
    for b in beats:
        b["pause_after"] = 0
        b["keeko"] = ""
        b["narration"] = [CHINTU_TAG.sub("", x) for x in b["narration"]]
        if kind == "exercise" and b["part"] == "hook" and b["role"] == "connect to reality" and "photo" not in b:
            b["role"] = "connect objects"
    if stop is None:
        report["no_stop"] += 1
        last = [b for b in beats if b["part"] == "hook"][-1]
        stop = json.loads(json.dumps(last))
        stop.update(key="hook_think", narration=[], marks={})
        stop.pop("photo", None)
        beats.insert(beats.index(last) + 1, stop)
    to_think(stop)
    s["beats"] = beats
    s["keeko_end"] = ""
    notes = {"key": key, "removed_beats": removed}
    if kind in ("exercise", "hook"):
        notes["old_misconception"] = {k: s.get(k, "") for k in ("misconception_id", "wrong_answer", "wrong_move")}
        s["misconception_id"] = s["wrong_answer"] = s["wrong_move"] = ""
    if removed or "old_misconception" in notes:
        write(notes_dir / (key + ".json"), notes, apply)
    return True


# ---------------------------------------------------------------- one chapter
def method_from(videos):
    worked = [v for v in videos if v["kind"] in ("worked", "theorem")]
    for v in videos:
        if v["kind"] != "exercise" or "method_from" in v:
            continue
        stem = v["key"].rsplit(".", 1)[0]
        topic = ".".join(v["key"].split(".")[:2])
        same = [w["key"] for w in worked if w["key"].rsplit(".", 1)[0] == stem]
        if not same:
            same = [w["key"] for w in worked if ".".join(w["key"].split(".")[:2]) == topic]
        v["method_from"] = same


def patch_build(nd: Path, apply: bool):
    p = nd / "build.py"
    if not p.exists():
        return "no build.py"
    src = p.read_text(encoding="utf-8")
    if 'focus == "RECAP"' in src:
        return "already"
    new, n = RECAP_FOCUS.subn(
        lambda m: (m.group(1) + 'if focus == "RECAP":\n' + m.group(1) +
                   '    continue    # Keeko design (28 Oct 2026): no recap video\n' + m.group(1) +
                   'kind = {"HOOK": "hook"}.get(focus, "worked")'), src)
    if n != 1:
        return "NOT PATCHED (%d matches)" % n
    if apply:
        p.write_text(new, encoding="utf-8")
    return "patched"


def migrate_chapter(nd: Path, apply: bool):
    sd = nd / "video_scripts"
    docs = [(f, read(f)) for f in sorted(sd.glob("*.json"))]
    rep = {"chapter": nd.parent.name, "scripts": 0, "recap_deleted": 0, "migrated": 0, "no_stop": 0}
    recap = [(f, d) for f, d in docs if d["video_script"]["kind"] == "recap"]
    live = [(f, d) for f, d in docs if d["video_script"]["kind"] != "recap"]
    rep["scripts"] = len(live)

    slots_path = nd / "name_slots.json"
    if slots_path.exists():
        slots = read(slots_path)
    else:
        slots = build_slots(nd, [d for _, d in live])
        write(slots_path, slots, apply)
    rep["name_slots"] = len([k for k in slots if k.startswith("{{")])
    rep["overflow"] = sorted(slots.get("_overflow", {}))
    pats = name_patterns(slots)

    for f, d in recap:
        rep["recap_deleted"] += 1
        if apply:
            f.unlink()
    for f, d in live:
        fresh = migrate_script(d, nd / "migration_notes", apply, rep)
        out = scrub_chintu(d)
        if fresh:
            out = swap(out, pats)
            used = sorted({t for t in re.findall(r"\{\{NAME_\d+\}\}", json.dumps(out, ensure_ascii=False))},
                          key=lambda t: int(re.search(r"\d+", t).group()))
            out["video_script"]["names"] = {t: (slots.get(t) or {}).get("role", "") for t in used}
            rep["migrated"] += 1
        if fresh or out != d:
            write(f, out, apply)

    wp = nd / "video_worklist.json"
    wl = read(wp)
    before = len(wl["videos"])
    wl["videos"] = [v for v in wl["videos"] if v["kind"] != "recap"]
    method_from(wl["videos"])
    wl["chapter"]["names_note"] = NAMES_NOTE
    rep["worklist_removed"] = before - len(wl["videos"])
    write(wp, wl, apply)

    bp = nd / "book_rules.json"
    if bp.exists():
        br = read(bp)
        if "names" in br:
            br.pop("names")
            br["_note_names"] = "Names are {{NAME_n}} placeholders; the roles live in name_slots.json."
            write(bp, br, apply)
    rep["build"] = patch_build(nd, apply)
    return rep


def main(argv):
    apply = "--apply" in argv
    dirs = [Path(a) for a in argv if not a.startswith("--")]
    for nd in dirs:
        print(json.dumps(migrate_chapter(nd, apply), ensure_ascii=False))
    if not apply:
        print("(dry run: nothing written; pass --apply)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
