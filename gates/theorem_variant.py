# -*- coding: utf-8 -*-
"""Theorem-chapter gate: the eight rules learned from building maths9_ch5 (Circles) and maths9_ch6
(Perimeter and Area), the two live Class 9 "new design" chapters that actually carry theorems.

Wiring (done elsewhere, not here): gate_runner.py decides whether to call check() at all, off
config.get("grade_band") == "9_10" and/or config.get("theorem_chapter"). This file runs its checks
unconditionally on whatever plan it is given.

Concrete markers found in the live plans (maths9_ch5/maths9_ch6 phase2 and _new.json), one per rule:

  1. A theorem statement concept has concept_kind == "try" and a theorem_id; its tool sits in that
     concept's media (type == "2d_tool") and is referenced by concept.tool_media_id /
     source_tool_ref. Inside the concept's content blocks, a "try_it" block must come after the
     "theorem_statement" block (the live build.py enforces exactly this ordering with
     kinds.index("try_it") < kinds.index("theorem_statement") -> error). The proof itself is a
     separate concept, concept_kind == "prove", same theorem_id, living at a later concept_id (the
     "C<n>" suffix is globally contiguous document order). A theorem and its converse are not
     distinguished by any extra field in either live chapter - both just carry a theorem_id key into
     content.THEOREMS - so two theorem_ids that resolve to the same tool_media_id are accepted as a
     shared tool (not double-flagged); only a theorem_id with *no* try concept, or a try concept
     naming more than one 2d_tool, is a violation.
  2. Exercise questions are content blocks with block_kind == "exercise_question", carrying
     video_media_id and image_media_id. The image's distinguishing field is image_role: "question"
     marks an exercise-question image, "diagram" marks a worked-example/definition diagram
     (media_specs.py literally keys on this: "image_role": "question" if question else "diagram").
     No separate field marks "hint content" on an image; media_specs.py's own authoring check
     (HINT_WORDS regex: hint|answer|solution|therefore|since|because|hence|proof|so that|thus, plus
     a check that the book's own hint text is not a substring of the image's visible fields) is
     reused here against the same image fields (title, description, labels, accuracy_constraints).
  3. The end-of-chapter topic is named "Chapter Exercises" (both live chapters hardcode this name
     and the build.py gate requires topics[-2]["topic_name"] == "Chapter Exercises", with the
     summary topic last). Both chapters split it into two concepts, concept_kind == "eoc": the
     first holds EOC_CORE questions, the second EOC_STARRED, and every question also carries a
     "starred" bool on its exercise_question block plus starred_question_ids on the concept. No
     chapter in either reference actually mixes starred and non-starred questions in one concept,
     so this sub-check is exercised only defensively: it fires only if a concept mixes starred and
     non-starred flags, or if a "core" concept (starred_question_ids empty) is placed after a
     concept that does carry starred questions.
  4. Enrichment concepts carry is_enrichment == True (also true of the framing/intro topic) and
     concept_kind == "enrich" and must have no objective_id / objective_ids (the live build.py
     checks precisely this: "if c["is_enrichment"] and (c["objective_id"] or c["objective_ids"])").
  5. Theorem-statement ("try") and proof ("prove") concepts have objectives, but the live
     concept_plan.py objectives for these concepts spell out the actual relationship being proved
     ("Derive the arc length 2*pi*r x theta/360 from the reflection and quarter-turn symmetries...",
     "State that circumference divided by diameter is the same for every circle...") rather than a
     bare "Prove Theorem 7." This gate flags an objective that is both short and has no content-word
     overlap with the theorem's name/statement (held in plan.source_metadata.theorems[thid]).
  6. No "Fig. 5.x" / "section 5.2" / "Theorem 7" / "Example 2" / "Exercise 3.1" style book-specific
     numbering anywhere in student-facing text. The live build.py already runs a softer version of
     this (r"Fig\\.? ?\\d", scoped to the authored (non-carried) plan blob); this gate's regex is
     stricter per the brief (also bans bare "Theorem N"/"Example N"/"Exercise N.M") and is scanned
     over the same student-facing surface media_content.py and gate_runner.py already draw the line
     at: concept content block text/question/answer/steps, topic_objective text, objectives'
     objective_text, and a media node's video_script - never description/context/teaching_notes.
  7. No scaffolding/category label leaks into rendered text. The live build.py's own authored-plan
     regex list (r"Textbook text", r"On the board", r"Pull it together", r"\\bDo it\\b", plus several
     chapter-specific internal names such as "Predict first", "Book hint", "Diagram decision",
     "End-of-chapter Q") is the direct precedent; this gate keeps the four generic entries and adds a
     short, generic Bloom's-level list. Neither live chapter actually renders a Bloom tag as visible
     text, so that half of the list is unverified against current references and kept defensive.
  8. Reuses rule 6's Exercise-N.M pattern against topic_name specifically: neither live chapter ever
     names a topic "Exercise 5.1" (both use "Chapter Exercises" or a descriptive concept-topic name),
     so this is confirmed clean on both references, not merely defensive.

    python -B theorem_variant.py <plan.json> [<plan.json> ...]      print the problems found, if any
"""
from __future__ import annotations

import json
import re
import sys

from . import media_content as MC

walk_topics = MC.walk_topics
walk_media = MC.walk_media

# ---------------------------------------------------------------- shared regex / word lists
BOOK_NUMBER_RE = re.compile(
    r"\bFig\.?\s*\d+(?:\.\d+)?\b"
    r"|\bsection\s+\d+(?:\.\d+)?\b"
    r"|\bTheorem\s+\d+\b"
    r"|\bExample\s+\d+\b"
    r"|\bExercise\s+\d+(?:\.\d+)?\b",
    re.IGNORECASE,
)
# the sub-pattern rule 8 reuses on its own (topic_name only)
EXERCISE_SET_NAME_RE = re.compile(r"\bExercise\s+\d+\.\d+\b", re.IGNORECASE)

SCAFFOLD_LABELS = [
    "Textbook text", "On the board", "Pull it together", "Do it",
    # Bloom's-level / verdict tags - no live reference renders these as visible text; kept defensive
    "Remember level", "Understand level", "Apply level", "Analyze level", "Evaluate level",
    "Create level", "[correct]", "[incorrect]",
]
SCAFFOLD_RE = re.compile("|".join(re.escape(s) for s in SCAFFOLD_LABELS), re.IGNORECASE)

HINT_WORDS_RE = re.compile(
    r"\b(hint|answer|solution|therefore|since|because|hence|proof|so that|thus)\b|=\s*\?",
    re.IGNORECASE,
)

GENERIC_VERBS_RE = re.compile(
    r"\b(prove|proves|proving|show|shows|showing|state|states|stating|derive|derives|deriving|"
    r"establish|establishes|establishing|demonstrate|demonstrates|demonstrating)\b",
    re.IGNORECASE,
)
STOPWORDS = {
    "a", "an", "the", "that", "this", "to", "of", "for", "and", "is", "are", "its", "it", "on",
    "in", "with", "from", "by", "as", "at", "be", "so", "its", "statement",
}


def _words(text):
    return {w for w in re.findall(r"[a-zA-Z]+", (text or "").lower()) if w not in STOPWORDS and len(w) >= 4}


# ---------------------------------------------------------------- student-facing text surface
# Same line media_content.py / gate_runner.py already draw: content block text fields, topic and
# chapter objectives, and a video's script - never description/context/teaching_notes, which are
# internal build notes the student never sees.
def student_facing_texts(plan):
    """Yield (location_label, text) for every string surface a student can actually read."""
    for topic in walk_topics(plan):
        if topic.get("topic_name"):
            yield (f"{topic.get('topic_id')} topic_name", topic["topic_name"])
        to = topic.get("topic_objective")
        if to and to.get("objective_text"):
            yield (f"{topic.get('topic_id')} topic_objective", to["objective_text"])
        for concept in topic.get("concepts") or []:
            cid = concept.get("concept_id")
            for block in concept.get("content") or []:
                for field in ("text", "question", "answer"):
                    v = block.get(field)
                    if isinstance(v, str) and v:
                        yield (f"{cid} content.{block.get('block_kind')}.{field}", v)
                for step in block.get("steps") or []:
                    if isinstance(step, str) and step:
                        yield (f"{cid} content.{block.get('block_kind')}.steps", step)
    for obj in plan.get("objectives") or []:
        if obj.get("objective_text"):
            yield (f"{obj.get('objective_id')} objective_text", obj["objective_text"])
    for node in walk_media(plan):
        vs = node.get("video_script")
        if not vs:
            continue
        # Only the beats actually spoken/shown to the student (narration, on_screen text) count
        # as rendered surface - core/video_script/contract.py's SCRIPT_KEYS also carries internal
        # production metadata on the same dict (source, placement, chapter, why, callback_to,
        # anchor, misconception_id, ...) that cites which book theorem/example a video illustrates
        # or why a wrong-move distractor was chosen; scanning the whole dict via json.dumps (as an
        # earlier version of this function did) flagged those citations as if they were spoken
        # text, which is why maths9_ch5/maths9_ch6's "source": ["Theorem 7"] production tags
        # dominated this gate's book-numbering findings even though no student ever sees them.
        for beat in vs.get("beats") or []:
            nid = f"{node.get('id')} video_script.beats[{beat.get('key', '?')}]"
            narration = beat.get("narration")
            if isinstance(narration, str) and narration:
                yield (f"{nid}.narration", narration)
            on_screen = beat.get("on_screen")
            if isinstance(on_screen, str) and on_screen:
                yield (f"{nid}.on_screen", on_screen)


# ---------------------------------------------------------------- rule checks
def check_tool_at_every_theorem(plan):
    """Rule 1: wherever a theorem's statement is actually shown to the student as its own
    content.theorem_statement block (the field both reference chapters use for this: a concept
    kind == 'try' presenting the theorem, or an 'exercise' concept that establishes a theorem and
    states it inline), that concept must carry exactly one tool, with the try_it block (if any)
    ordered after theorem_statement; the tool must sit before any proof block for the same
    theorem_id elsewhere in the plan. A theorem and its converse may share one tool (same
    tool_media_id), so tools are not required to be distinct across theorem_ids.

    Both maths9_ch5 and maths9_ch6 contain theorems reached only through a 'prove' concept with
    no separate theorem_statement block at all (the statement text sits only inside the proof
    block's own 'statement' field) - e.g. maths9_ch5's Th3 and Th12. Rule 1 cannot be checked for
    those theorems (there is no standalone statement moment to attach a tool to), so this is
    reported as a distinct, softer finding for a human to confirm is an intentional pedagogy
    choice (a quick corollary with no separate explore step) rather than a missed tool."""
    problems = []
    cnum_re = re.compile(r"\.C(\d+)$")
    statement_concepts = {}   # thid -> [(order, concept, tool_or_None)]
    proof_orders = {}         # thid -> [order, ...]
    any_mention = set()

    for topic in walk_topics(plan):
        tools_by_cid = {}
        for x in topic.get("media") or []:
            if x.get("type") == "2d_tool" and x.get("concept_id"):
                tools_by_cid.setdefault(x["concept_id"], []).append(x)
        for concept in topic.get("concepts") or []:
            thid = concept.get("theorem_id")
            if not thid:
                continue
            any_mention.add(thid)
            cid = concept["concept_id"]
            m = cnum_re.search(cid)
            order = int(m.group(1)) if m else -1
            kinds = [b.get("block_kind") for b in concept.get("content") or []]
            if "theorem_statement" in kinds:
                ctools = tools_by_cid.get(cid) or []
                if len(ctools) > 1:
                    problems.append(f"{cid}: more than one tool attached to a single theorem statement")
                statement_concepts.setdefault(thid, []).append((order, concept, ctools[0] if ctools else None))
            if concept.get("concept_kind") == "prove":
                proof_orders.setdefault(thid, []).append(order)

    for thid, entries in statement_concepts.items():
        for order, concept, tool in entries:
            cid = concept["concept_id"]
            if tool is None:
                problems.append(f"{cid}: theorem {thid}'s statement carries no tool")
            kinds = [b.get("block_kind") for b in concept.get("content") or []]
            if "try_it" in kinds and kinds.index("try_it") < kinds.index("theorem_statement"):
                problems.append(f"{cid}: the tool (try_it) opens before the theorem statement")
        stmt_order = min(o for o, _, _ in entries)
        for p_order in proof_orders.get(thid, []):
            if p_order <= stmt_order:
                problems.append(f"theorem {thid}: a proof concept (C{p_order}) sits before or at "
                                f"the concept that states it and carries its tool (C{stmt_order})")

    for thid in any_mention - set(statement_concepts):
        problems.append(f"theorem {thid}: no standalone theorem_statement block anywhere (its "
                        "statement sits only inside a proof block); rule 1 (tool before proof) "
                        "cannot be verified for it - confirm this is an intentional no-explore theorem")
    return problems


def check_exercise_question_media(plan):
    """Rule 2: every exercise question gets exactly one video and one question-only image, and
    that image carries no hint content (no HINT_WORDS, and never the book's own hint text).

    The image's own fields sometimes legitimately echo the printed question text verbatim (e.g.
    a "description" that restates "since AB = AC, show that..." so the image is self-contained) -
    that is the question being shown, not a hint leaking in, so the block's own `question` text is
    stripped out of `visible` before the HINT_WORDS scan runs, to stop the scan matching a
    "since"/"because" that came from the question itself rather than from an added hint."""
    problems = []
    media = {x["id"]: x for x in walk_media(plan)}
    for topic in walk_topics(plan):
        for concept in topic.get("concepts") or []:
            cid = concept["concept_id"]
            for block in concept.get("content") or []:
                if block.get("block_kind") != "exercise_question":
                    continue
                qid = block.get("exercise_id", "?")
                vid = block.get("video_media_id")
                vnode = media.get(vid)
                if not vid or not vnode or vnode.get("type") != "video":
                    problems.append(f"{cid}/{qid}: no question video")
                img = block.get("image_media_id")
                inode = media.get(img)
                if not img or not inode or inode.get("image_role") != "question":
                    problems.append(f"{cid}/{qid}: no question-only image (image_role == 'question')")
                    continue
                visible = " ".join(str(inode.get(f, "")) for f in
                                   ("title", "description", "accuracy_constraints")) \
                    + " " + " ".join(inode.get("labels") or [])
                question_text = block.get("question") or ""
                if question_text and question_text in visible:
                    visible = visible.replace(question_text, "")
                hit = HINT_WORDS_RE.search(visible)
                if hit:
                    problems.append(f"{cid}/{qid}: question image {img} carries hint-shaped text "
                                    f"'{hit.group(0)}'")
                hint_text = (block.get("hint") or "")[:30]
                if hint_text and hint_text in visible:
                    problems.append(f"{cid}/{qid}: question image {img} repeats the book's own hint")
    return problems


def check_chapter_exercises_topic(plan):
    """Rule 3: end-of-chapter exercises get their own topic, placed just before the summary
    topic, with core and starred questions kept in separate concepts. The starred/core split is
    only checked defensively (see module docstring): it fires only on an actual mix or misorder,
    since neither reference chapter exercises a violation."""
    problems = []
    topics = list(walk_topics(plan))
    if not topics:
        return problems
    eoc_idx = [i for i, t in enumerate(topics) if t.get("topic_name") == "Chapter Exercises"]
    if not eoc_idx:
        # defensive: also accept a topic whose concepts are all concept_kind == "eoc"
        eoc_idx = [i for i, t in enumerate(topics)
                  if t.get("concepts") and all(c.get("concept_kind") == "eoc" for c in t["concepts"])]
    if not eoc_idx:
        problems.append("no end-of-chapter exercises topic found (expected topic_name == "
                        "'Chapter Exercises' or all concept_kind == 'eoc')")
        return problems
    if len(eoc_idx) > 1:
        problems.append("more than one topic looks like the end-of-chapter exercises topic")
    i = eoc_idx[0]
    if i != len(topics) - 2 or topics[-1].get("topic_type") != "summary":
        problems.append("the chapter exercises topic must sit immediately before the summary topic")
    eoc_topic = topics[i]
    seen_starred = False
    for concept in eoc_topic.get("concepts") or []:
        starred_ids = set(concept.get("starred_question_ids") or [])
        qids = set(concept.get("question_ids") or [])
        mixed = bool(starred_ids) and bool(qids - starred_ids)
        if mixed:
            problems.append(f"{concept['concept_id']}: mixes starred and non-starred questions "
                            "in one concept (core and starred must be kept apart)")
        is_starred_concept = bool(qids) and qids == starred_ids
        if is_starred_concept:
            seen_starred = True
        elif seen_starred and qids:
            problems.append(f"{concept['concept_id']}: a core (non-starred) concept sits after a "
                            "starred concept in the chapter exercises topic")
    return problems


def check_enrichment_no_objective(plan):
    """Rule 4: enrichment concepts (is_enrichment, or concept_kind == 'enrich') carry no objective."""
    problems = []
    for topic in walk_topics(plan):
        for concept in topic.get("concepts") or []:
            is_enrich = concept.get("is_enrichment") or concept.get("concept_kind") == "enrich"
            if is_enrich and (concept.get("objective_id") or concept.get("objective_ids")):
                problems.append(f"{concept['concept_id']}: enrichment concept carries an objective")
    return problems


def check_theorem_objective_names_statement(plan):
    """Rule 5: a theorem's objective must name the theorem's content, not just carry a bare verb
    plus the theorem's own label. Flags an objective that is both short (fewer than 10 content
    words once generic proof verbs are stripped) and shares no content word (len >= 4) with the
    theorem's name/statement in plan.source_metadata.theorems."""
    problems = []
    theorems = ((plan.get("source_metadata") or {}).get("theorems")) or {}
    by_oid = {o.get("objective_id"): o for o in plan.get("objectives") or []}
    for topic in walk_topics(plan):
        for concept in topic.get("concepts") or []:
            thid = concept.get("theorem_id")
            kind = concept.get("concept_kind")
            if not thid or kind not in ("try", "prove"):
                continue
            oid = concept.get("objective_id")
            if not oid:
                continue
            obj = by_oid.get(oid)
            if not obj or not obj.get("objective_text"):
                continue
            text = obj["objective_text"]
            th = theorems.get(thid) or {}
            th_words = _words(th.get("name", "")) | _words(th.get("statement", ""))
            stripped = GENERIC_VERBS_RE.sub("", text)
            content_words = _words(stripped)
            overlap = content_words & th_words
            short = len(stripped.split()) < 10
            if short and not overlap:
                problems.append(f"{concept['concept_id']}: objective '{text}' for theorem {thid} "
                                f"reads as a bare verb, not the theorem's own content")
    return problems


def check_no_book_numbering(plan):
    """Rule 6: no Fig./section/Theorem N/Example N/Exercise N.M style book numbering anywhere in
    student-facing text (stricter than the live build.py's own r'Fig\\.? ?\\d' check: this also
    flags bare 'Theorem 7'/'Example 2'/'Exercise 3.1', in favour of naming the theorem)."""
    problems = []
    for loc, text in student_facing_texts(plan):
        for hit in list(BOOK_NUMBER_RE.finditer(text))[:3]:
            problems.append(f"{loc}: book-specific numbering '{hit.group(0)}' in "
                            f"'...{text[max(0, hit.start() - 30):hit.end() + 20]}...'")
    return problems


_VIDEO_SCRIPT_SAFE_LABELS = {"on the board", "do it"}


def check_no_scaffold_labels(plan):
    """Rule 7: no scaffolding/category/Bloom label ever appears as literal rendered text.

    A video's own `video_script` dict is internal production metadata (camera directions, beat
    labels) scanned here only because student_facing_texts() treats it as one surface among many -
    "on the board"/"do it" shows up there legitimately as a camera/action direction ("the tutor
    writes on the board", "the tutor does it step by step"), never as rendered on-screen text, so
    those two labels are not flagged when the hit is inside a video_script location; every other
    scaffold label (and every other surface) is still checked in full."""
    problems = []
    for loc, text in student_facing_texts(plan):
        hit = SCAFFOLD_RE.search(text)
        if not hit:
            continue
        if "video_script.beats" in loc and hit.group(0).lower() in _VIDEO_SCRIPT_SAFE_LABELS:
            continue
        problems.append(f"{loc}: scaffolding label '{hit.group(0)}' leaked into student text")
    return problems


def check_exercise_topic_names(plan):
    """Rule 8: exercise topics get their own descriptive name, never NCERT's own set name
    (e.g. 'Exercise 5.1'). Reuses rule 6's Exercise-N.M sub-pattern against topic_name only."""
    problems = []
    for topic in walk_topics(plan):
        name = topic.get("topic_name") or ""
        hit = EXERCISE_SET_NAME_RE.search(name)
        if hit:
            problems.append(f"{topic.get('topic_id')}: topic_name '{name}' uses the book's own "
                            f"exercise-set name '{hit.group(0)}'")
    return problems


def check(plan, config):
    """Return a list of problem strings; empty means clean. Runs unconditionally - the caller
    (gate_runner.py) decides, off config, whether to invoke this gate at all."""
    problems = []
    problems += check_tool_at_every_theorem(plan)
    problems += check_exercise_question_media(plan)
    problems += check_chapter_exercises_topic(plan)
    problems += check_enrichment_no_objective(plan)
    problems += check_theorem_objective_names_statement(plan)
    problems += check_no_book_numbering(plan)
    problems += check_no_scaffold_labels(plan)
    problems += check_exercise_topic_names(plan)
    return problems


if __name__ == "__main__":
    import io
    cfg = {"grade_band": "9_10", "theorem_chapter": True}
    for path in sys.argv[1:]:
        plan = json.load(io.open(path, encoding="utf-8"))
        problems = check(plan, cfg)
        print("%s: %d problem(s)" % (path, len(problems)))
        for p in problems:
            print("  -", p)
