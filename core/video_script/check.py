# -*- coding: utf-8 -*-
"""Check video scripts against the contract in core/video_script/AUTHOR_BRIEF.md (Keeko design, 28 Oct 2026).

A clear-language read (as a weak and tired child would) is a human review, not a gate.

One script:
    python -B core/video_script/check.py --worklist <chapter>/video_worklist.json --file <script.json>
Every script file of a chapter:
    python -B core/video_script/check.py --worklist <chapter>/video_worklist.json --dir <chapter>/video_scripts
A built plan (coverage, placement, the first topic's one video, and every script again):
    python -B core/video_script/check.py --worklist <chapter>/video_worklist.json --plan <plan.json>

A script file holds one video:
    {"key": "...", "title": "...", "description": "...", "teaching_notes": "...", "video_script": {...}}

The worklist is written by the chapter's build.py (`--video-worklist`):
    {"chapter": {"chapter_id", "name", "grade", "allow_words": [...], "length_override": {kind: {...}},
                 "exercise_numbers": {item_id: [numbers]}, "hard_words": [...]},
     "videos": [{"key", "video_id", "kind", "concept_id", "topic_id", "placement", "unlock", "source",
                 "item_ids", "answer", ...}]}
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import contract as K  # noqa: E402
import numwords  # noqa: E402

BOOKMARK = re.compile(r"""<bookmark\s+mark=['"]([^'"]*)['"]\s*/>""")
TAG = re.compile(r"<[^>]*>")
WORD = re.compile(r"[A-Za-z][A-Za-z'\-]*")


# ---------------------------------------------------------------- text helpers
NAME_RE = re.compile(K.NAME_TOKEN)


def spoken(line: str) -> str:
    """A narration line as the voice says it: no bookmarks; a name placeholder counts as one spoken name."""
    line = TAG.sub("", line)
    line = NAME_RE.sub("Asha", line)
    return re.sub(r"\s+", " ", line).strip()


def words(text: str):
    return WORD.findall(text)


def sentences(text: str):
    parts = re.split(r"(?<=[.?!])\s+", text.strip())
    return [p for p in parts if words(p)]


def low(s: str) -> str:
    return re.sub(r"\s+", " ", s.lower()).strip()


def has_word(text: str, word: str) -> bool:
    return re.search(r"(?<![A-Za-z])" + re.escape(word) + r"(?![A-Za-z])", text, re.I) is not None


def token_in(text: str, token: str) -> bool:
    """`token` appears in `text` as a whole token (not inside a longer number or word)."""
    return re.search(r"(?<![0-9A-Za-z./])" + re.escape(token) + r"(?![0-9A-Za-z/]|\.\d)", text) is not None


def all_strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield str(k)
            yield from all_strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from all_strings(v)


# Book numbering (user rule, 1 Oct 2026): no question, example, exercise, section or figure numbers in any text a video
# carries; a title card shows the topic or set name. The ids that trace a video to its book item stay: `source`,
# `chapter`, `callback_to` and the bookmark marks.
_NUMW = (r"(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen"
         r"|seventeen|eighteen|nineteen|twenty)")
BOOK_NUMBER = re.compile(
    r"(?<![A-Za-z0-9_])(?:Q\s?\d+[a-z]?"
    rf"|questions?\s+(?:no\.?\s*)?{_NUMW}\b(?![\s,]*\d)"
    rf"|(?<!for )examples?\s+{_NUMW}\b"
    r"|exercises?\s+\d|ex\.?\s?\d+"
    r"|figure\s+it\s+out\s*,?\s*\d|section\s+\d|try\s+this\s*\d"
    r"|part\s*\([a-h]\)|parts?\s+[b-h](?![A-Za-z0-9'])"
    r"|fig(?:ure)?\.?\s+\d)", re.I)
TRACE_KEYS = ("source", "chapter", "callback_to")


def book_numbers(*texts):
    """The book-numbering phrases in `texts` (bookmark tags ignored)."""
    return [m.group(0) for t in texts for m in BOOK_NUMBER.finditer(TAG.sub("", t))]


def readable_strings(s: dict):
    """Every string value of a video_script a person or the renderer reads, i.e. all but the trace ids."""
    return [x for k, v in s.items() if k not in TRACE_KEYS for x in _values(v)]


def _values(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for v in o.values():
            yield from _values(v)
    elif isinstance(o, list):
        for v in o:
            yield from _values(v)


NEAR = "|".join(K.MATHS_WORDS_NEAR_A)
NAMED = r"(?:side|point|angle|vertex|corner|letter|value of|root of|chord|arc|line)"


def letter_a(say: str) -> bool:
    """True when the letter a (a point, a side, a variable) is written as 'a' or 'A' instead of 'eigh'."""
    for sen in sentences(say):
        toks = re.findall(r"[A-Za-z']+|[,.?!]", sen)
        for i, t in enumerate(toks):
            nxt = toks[i + 1] if i + 1 < len(toks) else ""
            if t == "A" and (i > 0 or re.fullmatch(r"[A-Z]", nxt or "")):
                return True
    if re.search(rf"(?<![A-Za-z'])a\s+(?:{NEAR})\b", say):
        return True
    if re.search(rf"\b(?:{NEAR})(?:\s+by)?\s+a(?=\s*(?:[,.?!]|$)|\s+(?:{NEAR}|and\s+b)\b)", say):
        return True
    if re.search(rf"\b{NAMED}\s+a(?=\s*(?:[,.?!]|$)|\s+(?:and|is|equals|to)\b)", say):
        return True
    return False


# ---------------------------------------------------------------- the check
TOOL_REF = re.compile(r"(?<![A-Za-z])(?:" + K.TOOL_REFERENCE + r")(?![A-Za-z])", re.I)


def load_book_rules(folder):
    """<chapter>/new_design/book_rules.json: allowed `names`, `banned_words`, per-script `theorems` (empty if absent)."""
    p = Path(folder) / K.BOOK_RULES_FILE
    rules = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
    sp = Path(folder) / K.NAME_SLOTS_FILE
    if sp.exists():
        rules["name_slots"] = json.loads(sp.read_text(encoding="utf-8"))
    rules["final_names"] = final_names()
    return rules


def final_names():
    """The pupil names that replace the {{NAME_n}} placeholders once a chapter is filled (core/video_script/final_names.json)."""
    p = Path(__file__).with_name("final_names.json")
    return [n["name"] for n in json.loads(p.read_text(encoding="utf-8"))["names"]] if p.exists() else []


def check_four_rules(s: dict, rules: dict | None, key: str = ""):
    """User rules of 1 Oct 2026 (docs/27 35 to 38) for one script: no tool reference, only book names and words,
    and a theorem video that states the theorem. The hook photo is checked in check_plan."""
    E = []
    rules = rules or {}
    beats = s.get("beats") or []
    texts = []
    for b in beats:
        for k in ("on_screen", "removed", "moves_through"):
            if isinstance(b.get(k), str):
                texts.append((f"beat {b.get('key')}: {k}", b[k]))
        texts += [(f"beat {b.get('key')}: narration", x) for x in b.get("narration", []) if isinstance(x, str)]
    for k in ("why", "substitution", "anchor", "wrong_move", "payoff_line"):
        if isinstance(s.get(k), str):
            texts.append((k, s[k]))
    for where, tx in texts:
        m = TOOL_REF.search(TAG.sub("", tx))
        if m:
            E.append(f"{where}: refers to a tool or an earlier try ({m.group(0)!r}); a video stands on its own")
    slots = rules.get("name_slots")
    used_tokens = set()
    for where, tx in texts:
        used_tokens |= {int(n) for n in NAME_RE.findall(tx)}
    for n in sorted(used_tokens):
        if not 1 <= n <= K.NAME_SLOTS_MAX:
            E.append(f"names: {{{{NAME_{n}}}}} is outside 1 to {K.NAME_SLOTS_MAX}")
        elif slots is not None and f"{{{{NAME_{n}}}}}" not in slots:
            E.append(f"names: {{{{NAME_{n}}}}} is not in this chapter's {K.NAME_SLOTS_FILE}")
    declared = (s.get("names") or {})
    finals = rules.get("final_names") or final_names()
    used_finals = {nm for nm in finals if any(has_word(TAG.sub("", tx), nm) for _, tx in texts)}
    want = {f"{{{{NAME_{n}}}}}" for n in used_tokens} | used_finals
    if set(declared) != want:
        E.append(f"names must list exactly the placeholders or names the video uses {sorted(want)}, not {sorted(declared)}")
    for tok, role in declared.items():
        if not (NAME_RE.fullmatch(tok) or tok in finals) or not isinstance(role, str) or not role.strip():
            E.append(f"names: {tok!r} must be a {{{{NAME_n}}}} placeholder or one of the chapter's final names, with the character's role in the book")
    if slots:
        for orig in (slots.get("_overflow") or {}):
            for where, tx in texts:
                if has_word(TAG.sub("", tx), orig):
                    E.append(f"{where}: {orig!r} has no placeholder in this chapter (more than {K.NAME_SLOTS_MAX} "
                             f"characters); use the book's role, such as 'the teacher', or one of the slot names")
                    break
        for tok, info in slots.items():
            if tok.startswith("_"):
                continue
            orig = (info.get("original") if isinstance(info, dict) else info) or ""
            for part in re.findall(r"[A-Za-z]{3,}", orig):
                if part.lower() in ("the", "and", "his", "her", "their") or part in finals:
                    continue
                for where, tx in texts:
                    if has_word(TAG.sub("", tx), part):
                        E.append(f"{where}: the book name {part!r} must be its placeholder {tok}")
                        break
    for w in rules.get("banned_words", []):
        for where, tx in texts:
            if has_word(TAG.sub("", tx), w):
                E.append(f"{where}: {w!r} is not in the textbook")
                break
    if s.get("kind") == "theorem":
        st = [b for b in beats if b.get("key") == K.THEOREM_STATE_BEAT]
        if not st:
            E.append(f"a theorem video has a beat keyed {K.THEOREM_STATE_BEAT!r} that states the theorem")
        else:
            b = st[0]
            say = low(" ".join(spoken(x) for x in b.get("narration", [])))
            if not b.get("on_screen", "").strip():
                E.append("the state beat shows the theorem on screen")
            for ph in (rules.get("theorems") or {}).get(key, []):
                if low(ph) not in say:
                    E.append(f"the state beat does not say {ph!r}")
    return E


def check_script(s: dict, ctx: dict | None = None, chapter: dict | None = None):
    """Errors for one video_script. `ctx` is the video's worklist entry, `chapter` the worklist header."""
    ctx = ctx or {}
    chapter = chapter or {}
    allow = {w.lower() for w in chapter.get("allow_words", [])}
    E = []

    def err(msg):
        E.append(msg)

    # ---- shape
    missing = [k for k in K.SCRIPT_KEYS if k not in s]
    if missing:
        err(f"missing keys: {missing}")
        return E
    extra = [k for k in s if k not in K.SCRIPT_KEYS]
    if extra:
        err(f"unknown keys: {extra}")
    kind = s["kind"]
    if kind not in K.KINDS:
        err(f"kind {kind!r} is not one of {K.KINDS}")
        return E
    if ctx.get("kind") and ctx["kind"] != kind:
        err(f"kind {kind!r} but the worklist planned {ctx['kind']!r}")
    if chapter.get("chapter_id") and s["chapter"] != chapter["chapter_id"]:
        err(f"chapter {s['chapter']!r} should be {chapter['chapter_id']!r}")
    if not isinstance(s["source"], list) or not s["source"] or not all(isinstance(x, str) and x for x in s["source"]):
        err("source must be a non-empty list of strings")
    if s["placement"] not in K.PLACEMENTS:
        err(f"placement {s['placement']!r}")
    if s["unlock"] not in K.UNLOCKS:
        err(f"unlock {s['unlock']!r}")
    if kind == "exercise" and (s["unlock"] != "after_attempt" or s["placement"] != "after"):
        err("an exercise video is placement 'after' and unlock 'after_attempt'")
    if kind == "hook" and s["placement"] != "before":
        err("a hook is placement 'before'")
    if kind == "worked" and s["placement"] != "after":
        err("a worked video is placement 'after'")
    if s["shape"] not in K.SHAPES:
        err(f"shape {s['shape']!r}")
    for k in ("why", "substitution", "anchor", "design"):
        if not isinstance(s[k], str) or not s[k].strip():
            err(f"{k} is empty")
    if not isinstance(s["maths_rules"], list) or not s["maths_rules"] or not all(isinstance(x, str) and x.strip() for x in s["maths_rules"]):
        err("maths_rules must be a non-empty list of strings")
    for k in ("terms", "hold_back", "never_show", "open_questions"):
        if not isinstance(s[k], list) or not all(isinstance(x, str) for x in s[k]):
            err(f"{k} must be a list of strings")
    if not isinstance(s["names"], dict):
        err("names must be a dict of name -> respelling")
    fa = s["final_answer"]
    if not isinstance(fa, dict) or set(fa) != {"value", "spoken", "units"}:
        err("final_answer must be {value, spoken, units}")
        fa = {"value": "", "spoken": "", "units": ""}
    if not isinstance(s["answer_verified"], bool):
        err("answer_verified must be true or false")
    elif not s["answer_verified"] and not s["open_questions"]:
        err("answer_verified is false, so open_questions must say the doubt")
    for text in all_strings(s):
        if any(d in text for d in K.DASHES):
            err(f"en or em dash in {text[:60]!r} (the plan may hold none)")
            break
    for text in all_strings(s):
        if re.search(r"[\u0900-\u097F]", text):
            err("Devanagari text: English only")
            break
    if s["kind"] == "hook":
        for k in ("wrong_answer", "payoff_line", "promise"):
            if s[k] != "":
                err(f"a hook sets {k} to an empty string")
    if s["keeko_end"] not in K.KEEKO_END:
        err(f"keeko_end {s['keeko_end']!r} is not one of {K.KEEKO_END}")
    elif kind in K.CONCEPT_KINDS:
        if not s["keeko_end"]:
            err("a concept video ends with Keeko's raised hand: keeko_end is 'misconception' or 'real_life'")
        elif s["keeko_end"] == "misconception":
            for k in ("misconception_id", "wrong_answer", "wrong_move"):
                if not str(s[k]).strip():
                    err(f"keeko_end is 'misconception', so {k} says the wrong idea Keeko brings")
        else:
            for k in ("misconception_id", "wrong_answer", "wrong_move"):
                if str(s[k]).strip():
                    err(f"keeko_end is 'real_life', so {k} is an empty string")
    else:
        if s["keeko_end"]:
            err(f"a {kind} video has no raised hand: keeko_end is an empty string")
        for k in ("misconception_id", "wrong_answer", "wrong_move"):
            if str(s[k]).strip():
                err(f"a {kind} video holds no misconception: {k} is an empty string")
    if any(has_word(x, "chintu") for x in all_strings(s)):
        err("Chintu is gone; the mascot is Keeko")
    cb = str(s["callback_to"] or "")
    if cb:
        if ctx.get("method_from") and kind == "exercise":
            if cb not in ctx["method_from"]:
                err(f"callback_to {cb!r}: an exercise video names the solved example whose method it uses, one of {ctx['method_from']}")
        elif chapter.get("worked_keys") and cb not in chapter["worked_keys"]:
            err(f"callback_to {cb!r} is not a video key of this chapter")
    elif kind == "exercise" and ctx.get("method_from"):
        err(f"an exercise video names the solved example whose method it uses: callback_to is one of {ctx['method_from']}")

    beats = s["beats"]
    if not isinstance(beats, list) or not beats:
        err("beats must be a non-empty list")
        return E

    # ---- beats: fields and enums
    keys = set()
    for i, b in enumerate(beats):
        tag = f"beat {i + 1} ({b.get('key', '?')})"
        miss = [k for k in K.BEAT_KEYS if k not in b]
        if miss:
            err(f"{tag}: missing {miss}")
            continue
        extra = [k for k in b if k not in K.BEAT_KEYS and k not in K.OPTIONAL_BEAT_KEYS]
        if extra:
            err(f"{tag}: unknown keys {extra}")
        if not re.fullmatch(r"[a-z][a-z0-9_]*", str(b["key"])):
            err(f"{tag}: key must be a lowercase identifier")
        if b["key"] in keys:
            err(f"{tag}: duplicate key")
        keys.add(b["key"])
        if b["part"] not in K.PARTS:
            err(f"{tag}: part {b['part']!r}")
        if b["role"] not in K.ROLES:
            err(f"{tag}: role {b['role']!r}")
        if b["meaning"] not in K.MEANINGS:
            err(f"{tag}: meaning {b['meaning']!r}")
        if b["region"] not in K.REGIONS:
            err(f"{tag}: region {b['region']!r}")
        if b["keeko"] not in K.KEEKO_BEAT:
            err(f"{tag}: keeko {b['keeko']!r} is not one of {K.KEEKO_BEAT}")
        if b["block"] and b["block"] not in K.BLOCKS:
            err(f"{tag}: block {b['block']!r} is not in the block list (leave it empty unless sure)")
        if not isinstance(b["pause_after"], (int, float)) or not 0 <= b["pause_after"] <= K.PAUSE_MAX:
            err(f"{tag}: pause_after must be 0 to {K.PAUSE_MAX} seconds")
        if not isinstance(b["on_screen"], str) or not b["on_screen"].strip():
            err(f"{tag}: on_screen is empty")
        if not isinstance(b["marks"], dict):
            err(f"{tag}: marks must be a dict")
        if not isinstance(b["carries_over"], list):
            err(f"{tag}: carries_over must be a list")
        for k in ("colours", "removed", "moves_through"):
            if not isinstance(b[k], str) or not b[k].strip():
                err(f"{tag}: {k} is empty (write 'nothing' or 'plain')")
        if re.search(r"#[0-9a-fA-F]{3,6}\b", b["colours"]):
            err(f"{tag}: never name hex codes in colours")
        if not isinstance(b["narration"], list) or not b["narration"] or not all(isinstance(x, str) and x.strip() for x in b["narration"]):
            err(f"{tag}: narration must be a non-empty list of lines")
    if E:
        return E
    for e in check_four_rules(s, chapter.get("book_rules"), ctx.get("key", "")):
        err(e)

    parts = [b["part"] for b in beats]
    order = {p: i for i, p in enumerate(K.PARTS)}
    if any(order[a] > order[b] for a, b in zip(parts, parts[1:])):
        err(f"parts out of order: {parts}")
    for p in K.REQUIRED_PARTS[kind]:
        if p not in parts:
            err(f"a {kind} video needs a {p!r} part")
    if kind == "hook" and set(parts) != {"hook"}:
        err("every beat of a hook is part 'hook'")
    if kind not in K.CONCEPT_KINDS and "keeko" in parts:
        err(f"a {kind} video has no keeko part; Keeko raises a hand only at the end of a concept video")

    # ---- Keeko: one think-and-tell per video; one raised hand at the end of a concept video
    def says(b):
        return low(" ".join(spoken(l) for l in b["narration"]))
    think = [b for b in beats if K.THINK_PHRASE in says(b)]
    marked = [b for b in beats if b["keeko"] == "think"]
    if len(think) != 1:
        err(f"a video has exactly one 'Think and tell.' beat, not {len(think)}")
    if len(marked) != 1 or (len(think) == 1 and marked[0] is not think[0]):
        err("the 'Think and tell.' beat, and only that beat, has keeko 'think' (Keeko is only placed on screen)")
    if len(think) == 1:
        if think[0]["part"] != "hook":
            err("the 'Think and tell.' beat sits in the hook part")
        if think[0]["pause_after"] != K.THINK_PAUSE:
            err(f"the 'Think and tell.' beat has pause_after {K.THINK_PAUSE}")
    for b in beats:
        if b["pause_after"] and not (len(think) == 1 and b is think[0]):
            err(f"beat {b['key']}: the think-and-tell is the only pause; pause_after is 0 here")
    hands = [b for b in beats if b["keeko"] == "raise_hand"]
    kbeats = [b for b in beats if b["part"] == "keeko"]
    if kind in K.CONCEPT_KINDS:
        if len(hands) != 1 or not kbeats or hands[0] is not kbeats[0]:
            err("a concept video has exactly one raise_hand beat, and it opens the keeko part")
        elif K.KEEKO_LINE not in says(hands[0]):
            err("the raise_hand beat has the teacher say 'Keeko has raised a hand' and hand over to the doubt")
    elif hands:
        err(f"a {kind} video has no raised hand")
    if any(b["part"] != "keeko" and b["keeko"] == "raise_hand" for b in beats):
        err("Keeko raises a hand only in the keeko part")
    for b in beats:
        if b["part"] == "keeko" and b["keeko"] == "think":
            err("Keeko is placed for the think-and-tell in the hook part only")
    # the idea part is a board solution: given, find, step_1 ... step_n, answer, one line per beat
    ikeys = [b["key"] for b in beats if b["part"] == "idea"]
    if ikeys:
        n = sum(1 for k in ikeys if re.fullmatch(K.IDEA_STEP, k))
        want = ["given", "find"] + [f"step_{i}" for i in range(1, n + 1)] + ["answer"]
        if n < 1 or ikeys != want:
            err(f"the idea part is a board solution, one line per beat: given, find, step_1 ... step_n, answer; got {ikeys}")

    # ---- lengths
    lim = dict(K.LIMITS[kind])
    lim.update((chapter.get("length_override") or {}).get(kind, {}))
    lim.update(ctx.get("length_override") or {})
    beat_words = [sum(len(words(spoken(l))) for l in b["narration"]) for b in beats]
    total = sum(beat_words)
    lo, hi = lim["words"]
    if not lo <= total <= hi:
        err(f"{total} spoken words; a {kind} video has {lo} to {hi}")
    blo, bhi = lim["beats"]
    if not blo <= len(beats) <= bhi:
        err(f"{len(beats)} beats; a {kind} video has {blo} to {bhi}")
    for b, n in zip(beats, beat_words):
        if n > K.BEAT_WORDS_MAX:
            err(f"beat {b['key']}: {n} words, over {K.BEAT_WORDS_MAX}; split it")
    all_sent = []
    for b in beats:
        for line in b["narration"]:
            for sen in sentences(spoken(line)):
                n = len(words(sen))
                all_sent.append(n)
                if n > K.SENTENCE_MAX:
                    err(f"beat {b['key']}: sentence of {n} words (max {K.SENTENCE_MAX}): {sen[:80]!r}")
    if all_sent:
        avg = sum(all_sent) / len(all_sent)
        a_lo, a_hi = K.SENTENCE_AVG
        if not a_lo <= avg <= a_hi:
            err(f"average sentence {avg:.1f} words; aim for {a_lo:.0f} to {a_hi:.0f}")

    # ---- bookmarks
    run = 0
    seen_part = set()
    for b in beats:
        names = []
        starts_part = b["part"] not in seen_part
        seen_part.add(b["part"])
        first_pos = None
        wcount = 0
        for line in b["narration"]:
            body = line
            pos = 0
            for m in BOOKMARK.finditer(body):
                seg = body[pos:m.start()]
                n = len(words(TAG.sub("", seg)))
                wcount += n
                run += n
                if run > K.BOOKMARK_GAP_MAX:
                    err(f"beat {b['key']}: {run} words without a bookmark (max {K.BOOKMARK_GAP_MAX})")
                run = 0
                if first_pos is None:
                    first_pos = wcount
                names.append(m.group(1))
                pos = m.end()
            n = len(words(TAG.sub("", body[pos:])))
            wcount += n
            run += n
        if run > K.BOOKMARK_GAP_MAX:
            err(f"beat {b['key']}: {run} words without a bookmark (max {K.BOOKMARK_GAP_MAX})")
            run = 0
        if starts_part and (first_pos is None or first_pos >= K.PART_START_BOOKMARK_WITHIN):
            err(f"beat {b['key']} starts the {b['part']!r} part: its first bookmark must come within the first "
                f"{K.PART_START_BOOKMARK_WITHIN} spoken words")
        for nm in names:
            if not re.fullmatch(r"[a-z0-9_]+", nm):
                err(f"beat {b['key']}: bookmark name {nm!r} (lowercase letters, digits and _)")
        if len(names) != len(set(names)):
            err(f"beat {b['key']}: bookmark names repeat")
        if set(names) != set(b["marks"]):
            only_b = sorted(set(names) - set(b["marks"]))
            only_m = sorted(set(b["marks"]) - set(names))
            err(f"beat {b['key']}: bookmarks without marks {only_b}, marks without bookmarks {only_m}")
        for nm, what in b["marks"].items():
            if not isinstance(what, str) or not what.strip():
                err(f"beat {b['key']}: mark {nm!r} must say what arrives, moves or lights up")

    # ---- speech
    lines = [(b, line) for b in beats for line in b["narration"]]
    for b, line in lines:
        if "[" in line or "]" in line:
            err(f"beat {b['key']}: no brackets or stage directions in narration: {line[:60]!r}")
        if "recap" in low(line) or "your turn" in low(line) or "try again with this" in low(line):
            err(f"beat {b['key']}: no recap, 'your turn' or 'try again' in narration")
        say = spoken(line)
        bad = sorted({c for c in say if c in K.SPEECH_BANNED_CHARS})
        if bad:
            err(f"beat {b['key']}: characters the voice cannot read {bad}: {say[:70]!r}")
        if "..." in say or "\u2026" in say:
            err(f"beat {b['key']}: no written pauses ('...'); use pause_after")
        if re.search(r"\s-\s", say):
            err(f"beat {b['key']}: spaced dash in speech")
        if re.search(r"\w:\w", say):
            err(f"beat {b['key']}: 'a:b' in speech; say 'a to b'")
        for w in K.BANNED_WORDS:
            if w not in allow and has_word(say, w):
                err(f"beat {b['key']}: banned word {w!r}")
        for ph in K.BANNED_PHRASES:
            if ph in low(say):
                err(f"beat {b['key']}: banned phrase {ph!r}")
        for w in K.BOOK_OPERATION_WORDS:
            if w in allow or not has_word(say, w):
                continue
            if w == "per" and not re.search(r"\bper\b(?!\s*cent)", say, re.I):
                continue
            err(f"beat {b['key']}: say the operation, not the book word {w!r}")
        for w in K.BOOK_WORD_SWAPS:
            if w not in allow and has_word(say, w):
                err(f"beat {b['key']}: book word {w!r}; swap it for a plain one")
        for w in K.AMERICAN_SPELLINGS:
            if has_word(say, w):
                err(f"beat {b['key']}: American spelling {w!r}")
        for w in K.HINGLISH:
            if has_word(say, w):
                err(f"beat {b['key']}: English only, not {w!r}")
        if has_word(say, "exercise") or has_word(say, "exercises"):
            err(f"beat {b['key']}: never say 'exercise'; say 'a question from your book'")
        if has_word(say, "ay"):
            err(f"beat {b['key']}: write the letter a as 'eigh', never 'ay'")
        for sen in sentences(say):
            first = low(sen).split(" ")[0].strip(",.?!")
            if first in K.BAD_LINE_STARTS:
                err(f"beat {b['key']}: no line starts with {first!r}: {sen[:60]!r}")
        if letter_a(say):
            err(f"beat {b['key']}: the letter a is written 'eigh' ('point eigh', 'eigh squared'): {say[:70]!r}")

    all_say = " ".join(spoken(l) for _, l in lines)

    # ---- wrong idea, terms
    if s["wrong_answer"]:
        home = next((b for b, l in lines if low(s["wrong_answer"]) in low(spoken(l))), None)
        if home is None:
            err("wrong_answer is set but never said")
        elif home["part"] != "keeko":
            err("wrong_answer is first said in the keeko part (Keeko's doubt), never earlier")
        elif "keeko" not in says(home):
            err("the teacher gives the wrong idea as Keeko's doubt ('Keeko thinks ...')")
    if len(s["terms"]) > K.NEW_TERMS_MAX[kind]:
        err(f"{len(s['terms'])} new terms; a {kind} video has at most {K.NEW_TERMS_MAX[kind]}")
    for t in s["terms"]:
        home = next((b for b in beats if low(t) in low(" ".join(spoken(l) for l in b["narration"]))), None)
        if home is None:
            err(f"term {t!r} is never said")
        elif not any(w in low(" ".join(spoken(l) for l in home["narration"])) for w in K.DEFINE_WORDS):
            err(f"term {t!r} is not defined in the beat where it first appears (meaning first, then 'is called')")

    # ---- answer and reveal
    idea_beats = [b for b in beats if b["part"] == "idea"]
    reveal_idx = None
    if kind != "hook":
        if not s["payoff_line"].strip():
            err("payoff_line is empty")
        else:
            for i, b in enumerate(beats):
                if b["part"] == "idea" and low(NAME_RE.sub("Asha", s["payoff_line"])).rstrip(".") in says(b):
                    reveal_idx = i
                    if b["key"] != "answer":
                        err("payoff_line is said in the answer beat, the last line of the board solution")
                    break
            if reveal_idx is None:
                err("payoff_line is not said in the idea part")
    if kind in ("worked", "exercise"):
        if not str(fa["value"]).strip() or not str(fa["spoken"]).strip():
            err("final_answer needs a value and its spoken form")
        if not s["hold_back"]:
            err("hold_back must list the answer as it would appear on screen")
    if kind in ("hook", "theorem") and not s["hold_back"]:
        err(f"a {kind} video lists what it holds back")
    cut = reveal_idx if reveal_idx is not None else len(beats)
    early = beats[:cut]
    for hb in s["hold_back"]:
        if not hb.strip():
            continue
        for b in early:
            screen = b["on_screen"] + " " + " ".join(b["marks"].values())
            if token_in(screen, hb):
                err(f"beat {b['key']}: {hb!r} is on screen before the reveal")
                break
    if fa.get("spoken") and kind in ("worked", "exercise", "theorem"):
        sp = low(str(fa["spoken"]))
        pre = [b for b in beats if b["part"] in ("hook", "ground")]
        for b in pre:
            if len(sp.split()) >= 2 and sp in low(" ".join(spoken(l) for l in b["narration"])):
                err(f"beat {b['key']}: the answer {fa['spoken']!r} is said before the idea part")
                break
    answer_text = ctx.get("answer") or ""
    if kind in ("worked", "exercise") and answer_text and s["answer_verified"]:
        want = {round(float(x), 2) for x in numwords.digit_numbers(NAME_RE.sub("", answer_text))}
        got = {round(float(x), 2) for x in numwords.digit_numbers(NAME_RE.sub("", str(fa["value"])))}
        if got and want and not got <= want:
            err(f"final_answer {fa['value']!r} does not match the item's answer {answer_text[:80]!r}")

    # ---- kind rules
    if kind == "hook":
        talk = [b for b in beats if b is not (think[0] if len(think) == 1 else None)]
        if len(think) == 1 and beats[-1] is not think[0]:
            err("a hook's last beat is the 'Think and tell.' beat")
        before = [spoken(l) for b in talk for l in b["narration"]]
        if not before or not before[-1].endswith("?"):
            err("a hook ends on an open question, then 'Think and tell.'")
        if has_word(all_say, "equals"):
            err("a hook has no formula")
        for b in beats:
            if any(c in b["on_screen"] for c in K.SYMBOL_ON_SCREEN):
                err(f"beat {b['key']}: a hook puts no symbol on screen")
    if kind in ("worked", "exercise"):
        hook_say = low(" ".join(spoken(l) for b in beats if b["part"] == "hook" for l in b["narration"]))
        if "your book" not in hook_say:
            err("the hook part names the book's item ('This is from your book', 'a question from your book')")
    if kind == "theorem":
        idea_screen = low(" ".join(b["on_screen"] for b in idea_beats))
        if "given" not in idea_screen or "to prove" not in idea_screen:
            err("the idea part shows Given and To prove")
        reasons = [b for b in idea_beats if any(w in says(b) for w in K.REASON_WORDS)]
        if idea_beats and len(reasons) * 2 < len(idea_beats):
            err("proof steps give their reasons ('because ...'): too few idea beats do")
        for b in idea_beats:
            if not b["marks"]:
                err(f"beat {b['key']}: a proof step lights up its part of the figure (needs a bookmark)")
        if "?" not in " ".join(beats[0]["narration"]):
            err("a theorem video opens with the claim as a question")
    if kind == "story":
        if not s["promise"].strip():
            err("a story video makes a promise ('you will find ...')")
        elif any(has_word(s["promise"], w) for w in ("know", "learn", "understand")):
            err("the promise uses a doing verb, never know, learn or understand")
        if not any(b["meaning"] == "BREAK" for b in beats):
            err("a story video has at least one BREAK beat")
        ground = sum(n for b, n in zip(beats, beat_words) if b["part"] == "ground")
        if total and ground / total < 0.40:
            err(f"ground is {ground / total:.0%} of the words; never below 40%")
    # real life and misconceptions live only in a concept video's keeko part (and the hook's opening scene)
    for b in beats:
        if b["role"] == K.PHOTO_ROLE and not (b["part"] == "keeko" or kind == "hook"):
            err(f"beat {b['key']}: a 'connect to reality' beat sits only in the chapter hook or a concept video's keeko part")
    if kind in K.CONCEPT_KINDS and s["keeko_end"] == "real_life":
        if not any(b["role"] == K.PHOTO_ROLE for b in kbeats):
            err("keeko_end is 'real_life': a beat of the keeko part has the role 'connect to reality'")

    # ---- words this video must not use yet (a chapter's withheld ideas, e.g. the hook before a discovery)
    for w in ctx.get("forbid_words") or []:
        for b in beats:
            text = " ".join(spoken(l) for l in b["narration"]) + " " + b["on_screen"] + " " + " ".join(b["marks"].values())
            if re.search(r"(?<![A-Za-z])" + re.escape(w), text, re.I):
                err(f"beat {b['key']}: {w!r} is withheld in this video (it gives away what comes later)")
                break

    # ---- book numbering (user rule, 1 Oct 2026)
    hits = book_numbers(*readable_strings(s))
    if hits:
        err(f"book numbering {sorted(set(hits))[:4]}; name the topic or the question's idea, never its number")

    # ---- photos inside the video (docs/25 §14 "Photos inside videos")
    for e_ in check_beat_photos(s, chapter.get("photos")):
        err(e_)

    # ---- book guard
    guard = chapter.get("exercise_numbers") or {}
    own = set(ctx.get("item_ids") or [])
    if guard:
        def significant(vals):
            return {round(float(v), 4) for v in vals if not (0 <= float(v) <= 10) and float(v) != 100}
        if kind in ("hook", "story", "theorem"):
            used = significant(numwords.numbers(all_say))
            for item, nums in guard.items():
                if item in own:
                    continue
                sig = significant(nums)
                if len(sig) >= 2 and sig <= used:
                    err(f"book guard: this {kind} video uses the numbers of {item} {sorted(sig)}")
    return E


# ---------------------------------------------------------------- photos
def check_photo(p: dict, grade=None):
    """Errors for one photo library entry (<chapter>/photos/<id>.json)."""
    E = []
    pid = p.get("id", "?")
    miss = [k for k in K.PHOTO_FILE_KEYS if k not in p]
    if miss:
        return [f"photo {pid}: missing {miss}"]
    extra = [k for k in p if k not in K.PHOTO_FILE_KEYS]
    if extra:
        E.append(f"photo {pid}: unknown keys {extra}")
    if not re.fullmatch(r"ph_[a-z0-9_]+", str(pid)):
        E.append(f"photo {pid}: id must be ph_ plus lowercase letters, digits and _")
    st = p["subject_type"]
    if st not in K.PHOTO_SUBJECTS:
        E.append(f"photo {pid}: subject_type {st!r} is not one of {K.PHOTO_SUBJECTS}")
    for k in ("subject", "why", "gemini_prompt", "alt_text"):
        if not isinstance(p[k], str) or not p[k].strip():
            E.append(f"photo {pid}: {k} is empty")
    for k in ("need_basis", "reference", "pair_with"):
        if not isinstance(p[k], str):
            E.append(f"photo {pid}: {k} must be a string ('' when it does not apply)")
    if not isinstance(p["maths_on_object"], bool):
        E.append(f"photo {pid}: maths_on_object must be true or false")
    elif p["maths_on_object"] and not str(p["pair_with"]).strip():
        E.append(f"photo {pid}: the maths sits on the object, so pair_with names the drawn schematic that carries it")
    if E:
        return E
    # grade band: a generic scene is a photo only for young students, or for Class 7 and 8 on need basis
    g = int(grade) if str(grade or "").isdigit() else None
    if st == "scene" and g is not None:
        lo, hi = K.PHOTO_SCENE_GRADES["default"]
        nlo, nhi = K.PHOTO_SCENE_GRADES["need_basis"]
        if nlo <= g <= nhi and not p["need_basis"].strip():
            E.append(f"photo {pid}: a generic scene in Class {g} needs need_basis (why this student needs to see it)")
        if g > nhi:
            E.append(f"photo {pid}: a generic scene is never a photo in Class {g}; only a specific real thing is")
    # people: an authentic likeness only, from a supplied reference
    text = low(" ".join(str(p[k]) for k in ("subject", "gemini_prompt", "alt_text")))
    if st == "person" and not p["reference"].strip():
        E.append(f"photo {pid}: a real person needs a reference photo (no reference, no face)")
    for nm in K.PHOTO_NO_LIKENESS:
        if st == "person" and has_word(text, nm):
            E.append(f"photo {pid}: {nm!r} has no authentic likeness or is a drawn character; never a face")
    if has_word(text, "map"):
        E.append(f"photo {pid}: a map is never AI-generated; draw it from the official outline")
    # the prompt: no numbers, no branding, and it says so
    gp = p["gemini_prompt"]
    if any(c in gp for c in K.PHOTO_BANNED_CHARS):
        E.append(f"photo {pid}: the Gemini prompt holds a digit; a photo never carries a number")
    if K.PHOTO_PROMPT_MUST not in low(gp):
        E.append(f"photo {pid}: the Gemini prompt must say the frame holds {K.PHOTO_PROMPT_MUST!r} (no numerals, no labels)")
    for w in K.PHOTO_BRANDING:
        if w in low(" ".join(str(v) for v in p.values())):
            E.append(f"photo {pid}: branding {w!r}")
    for v in p.values():
        if isinstance(v, str) and any(d in v for d in K.DASHES):
            E.append(f"photo {pid}: en or em dash")
            break
    return E


def check_beat_photos(s: dict, photos):
    """Errors for the photos a script's beats show. `photos` is the chapter library {id: entry} (None = none)."""
    E = []
    photos = photos or {}
    beats = s.get("beats") or []
    used = [(i, b) for i, b in enumerate(beats) if "photo" in b]
    for i, b in used:
        tag = f"beat {b.get('key', i + 1)}"
        ph = b["photo"]
        if not isinstance(ph, dict) or set(ph) != set(K.PHOTO_BEAT_KEYS):
            E.append(f"{tag}: photo must be {{id, placement}}")
            continue
        if ph["id"] not in photos:
            E.append(f"{tag}: photo {ph['id']!r} is not in the chapter's photos/ library")
        if ph["placement"] not in K.PHOTO_PLACEMENTS:
            E.append(f"{tag}: photo placement {ph['placement']!r} is not one of {K.PHOTO_PLACEMENTS}")
        if b.get("role") != K.PHOTO_ROLE:
            E.append(f"{tag}: a photo sits only on a {K.PHOTO_ROLE!r} beat")
        if b.get("part") not in ("hook", "keeko"):
            E.append(f"{tag}: a photo sits only in the hook or the keeko part")
        if (b.get("block") or "") not in K.PHOTO_BLOCKS:
            E.append(f"{tag}: a photo beat carries no maths board (block {b.get('block')!r})")
        if "photo" not in low(b.get("on_screen", "")):
            E.append(f"{tag}: on_screen says where the photo appears and that it leaves at the end of the beat")
        # the photo must not give away what the video holds back
        entry = photos.get(ph["id"]) or {}
        pic = low(" ".join(str(entry.get(k, "")) for k in ("subject", "gemini_prompt", "alt_text")))
        for hb in s.get("hold_back") or []:
            if hb.strip() and len(hb.strip()) > 2 and low(hb) in pic:
                E.append(f"{tag}: photo {ph['id']!r} shows the held-back {hb!r}")
    return E


def load_photos(folder):
    """The chapter photo library: {id: entry} from <folder>/*.json (empty when the folder does not exist)."""
    out = {}
    folder = Path(folder)
    if not folder.exists():
        return out
    for f in sorted(folder.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        pid = d.get("id")
        if pid in out:
            raise SystemExit(f"two photo files carry the id {pid}")
        if f.stem != pid:
            raise SystemExit(f"photos/{f.name}: the file name must be <id>.json ({pid})")
        out[pid] = d
    return out


def check_photo_library(photos, scripts, grade=None):
    """Every library entry is valid and shown by at least one script."""
    E = []
    for p in photos.values():
        E += check_photo(p, grade)
    shown = {b["photo"]["id"] for d in scripts.values() for b in d["video_script"].get("beats", [])
             if isinstance(b.get("photo"), dict) and "id" in b["photo"]}
    for pid in sorted(set(photos) - shown):
        E.append(f"photo {pid}: in the library but no video shows it")
    return E


# ---------------------------------------------------------------- files and plans
def load_worklist(path):
    wl = json.loads(Path(path).read_text(encoding="utf-8"))
    return wl, {v["key"]: v for v in wl["videos"]}


def check_file(path, wl, by_key):
    d = json.loads(Path(path).read_text(encoding="utf-8"))
    errs = []
    for k in ("key", "title", "description", "teaching_notes", "video_script"):
        if k not in d:
            errs.append(f"file needs {k!r}")
    if errs:
        return errs
    ctx = by_key.get(d["key"])
    if ctx is None:
        return [f"key {d['key']!r} is not in the worklist"]
    if len(d["title"]) > 70:
        errs.append("title over 70 characters")
    for text in (d["title"], d["description"], d["teaching_notes"]):
        if any(x in text for x in K.DASHES):
            errs.append("en or em dash in title, description or teaching_notes")
    if (hits := book_numbers(d["title"], d["description"], d["teaching_notes"])):
        errs.append(f"book numbering in title, description or teaching_notes {sorted(set(hits))[:4]}")
    return errs + check_script(d["video_script"], ctx, wl["chapter"])


def check_plan(plan, wl, by_key, check_scripts=True):
    """Plan-level checks: every video scripted and clean, coverage, placement, the first topic's one video.
    With check_scripts=False the per-script checks are left to the caller (e.g. plan_hook.script_check_errors)."""
    E = []
    concepts = {}
    topic_of = {}
    first_topic = None
    for m in plan["modules"]:
        for sg in m["segments"]:
            for t in sg["topics"]:
                if first_topic is None:
                    first_topic = t
                for c in t["concepts"]:
                    concepts[c["concept_id"]] = c
                    topic_of[c["concept_id"]] = t
    videos = []

    def walk(o):
        if isinstance(o, dict):
            if o.get("type") == "video" and "id" in o:
                videos.append(o)
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(plan["modules"])
    seen = {}
    for v in videos:
        seen.setdefault(v["id"], v)
    videos = list(seen.values())
    ids = {v["id"] for v in videos}
    planned = {v["video_id"]: v for v in wl["videos"]}
    for v in videos:
        vs = v.get("video_script")
        if not vs:
            E.append(f"{v['id']}: no video_script")
            continue
        ctx = planned.get(v["id"])
        if ctx is None:
            E.append(f"{v['id']}: not in the worklist")
            continue
        if v.get("concept_id") != ctx["concept_id"]:
            E.append(f"{v['id']}: sits on {v.get('concept_id')} but the worklist placed it on {ctx['concept_id']}")
        swt = (v.get("source_video_walkthrough") or {}).get("type")
        if swt != vs["kind"]:
            E.append(f"{v['id']}: source_video_walkthrough.type {swt!r} should be the kind {vs['kind']!r}")
        if check_scripts:
            for e in check_script(vs, ctx, wl["chapter"]):
                E.append(f"{v['id']}: {e}")
    for vid in planned:
        if vid not in ids:
            E.append(f"{vid}: planned in the worklist but missing from the plan")
    # one hook per chapter: the opener, in the first topic; no topic hooks (user rule, 29 Sep 2026)
    hooks = [v for v in videos if (v.get("video_script") or {}).get("kind") == "hook"]
    if len(hooks) != 1:
        E.append(f"the plan has {len(hooks)} hook videos; it has exactly one, the chapter opener")
    elif topic_of.get(hooks[0].get("concept_id")) is not first_topic:
        E.append(f"{hooks[0]['id']}: the chapter's hook sits outside the first topic")
    # the chapter hook shows a picture (user rule, 1 Oct 2026): one beat carries a photo
    if len(hooks) == 1 and not any(isinstance(b.get("photo"), dict)
                                   for b in (hooks[0].get("video_script") or {}).get("beats", [])):
        E.append(f"{hooks[0]['id']}: the chapter hook shows a picture (a beat with a photo)")
    # the first topic has exactly one video
    if first_topic is not None:
        n = sum(1 for v in videos if topic_of.get(v.get("concept_id")) is first_topic)
        if n != 1:
            E.append(f"the first topic has {n} videos; it has exactly one")
    # coverage
    cov = plan.get("video_coverage")
    if not isinstance(cov, list) or not cov:
        E.append("plan-level video_coverage is missing")
        cov = []
    rows = {}
    for r in cov:
        if set(r) < {"book_item", "item_id", "video_id", "kind"}:
            E.append(f"video_coverage row {r} needs book_item, item_id, video_id, kind")
            continue
        rows.setdefault(r["item_id"], []).append(r)
        if r["video_id"] not in ids:
            E.append(f"video_coverage: {r['item_id']} points at missing video {r['video_id']}")
    for item in wl["chapter"].get("book_items", []):
        if item not in rows:
            E.append(f"video_coverage: book item {item} has no video")
    # exercise videos sit on the concept that asks the question
    for v in videos:
        vs = v.get("video_script") or {}
        ctx = planned.get(v["id"]) or {}
        if vs.get("kind") == "exercise" and ctx.get("item_concept") and v.get("concept_id") != ctx["item_concept"]:
            E.append(f"{v['id']}: an exercise video sits on the concept that asks its question ({ctx['item_concept']})")
    return E


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--worklist", required=True)
    ap.add_argument("--file", nargs="*")
    ap.add_argument("--dir")
    ap.add_argument("--plan")
    ap.add_argument("--only", help="comma-separated keys (with --dir)")
    a = ap.parse_args(argv)
    wl, by_key = load_worklist(a.worklist)
    photos = load_photos(Path(a.worklist).parent / "photos")
    wl["chapter"]["photos"] = photos
    wl["chapter"]["book_rules"] = load_book_rules(Path(a.worklist).parent)
    wl["chapter"]["worked_keys"] = [v["key"] for v in wl["videos"]]    # any video of the chapter may be called back
    bad = 0
    files = [Path(f) for f in (a.file or [])]
    if a.dir:
        files += sorted(Path(a.dir).glob("*.json"))
    only = set(a.only.split(",")) if a.only else None
    for f in files:
        if only:
            try:
                if json.loads(f.read_text(encoding="utf-8")).get("key") not in only:
                    continue
            except Exception:
                pass
        errs = check_file(f, wl, by_key)
        if errs:
            bad += 1
            print(f"FAIL {f.name}")
            for e in errs:
                print("   ", e)
        else:
            print(f"ok   {f.name}")
    if a.dir and not only:
        scripts = {}
        for f in sorted(Path(a.dir).glob("*.json")):
            d = json.loads(f.read_text(encoding="utf-8"))
            scripts[d.get("key")] = d
        errs = check_photo_library(photos, scripts, wl["chapter"].get("grade"))
        for e in errs:
            print("PHOTO", e)
        bad += bool(errs)
        if photos and not errs:
            print(f"photos ok ({len(photos)})")
    if a.plan:
        plan = json.loads(Path(a.plan).read_text(encoding="utf-8"))
        errs = check_plan(plan, wl, by_key)
        for e in errs:
            print("PLAN", e)
        bad += bool(errs)
        if not errs:
            print("plan ok")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
