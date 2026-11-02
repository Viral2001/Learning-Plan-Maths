# 02. Video script schema

Each planned video is one JSON file that a render pipeline turns into a
finished video without anyone reviewing it by hand first - so it must be
complete, true and clear before it is written. The full writing contract
(what to read, what to write, which rules matter most) is
`core/video_script/AUTHOR_BRIEF.md`; this page restates the schema itself,
read directly off `core/video_script/contract.py`, which is the machine
source of truth `core/video_script/check.py` actually enforces.

## File shape

```json
{"key": "<worklist key>",
 "title": "<a question, at most 70 characters, that does not give the answer>",
 "description": "<one or two sentences: what the video shows>",
 "teaching_notes": "<one to three sentences for the tutor: the one idea, the slip to watch for>",
 "video_script": { ...the fields below... }}
```

## The five kinds (`contract.KINDS`)

`hook`, `worked`, `exercise`, `theorem`, `story`. There is no `recap` kind, recap part or break part (Keeko
design, 28 Oct 2026). `worked` and `theorem` are the **concept videos**, `exercise` the **question video**, `hook`
the chapter opener. Each has its own
word/beat/second budget and required parts (`contract.LIMITS`,
`contract.REQUIRED_PARTS`):

| kind | words | beats | seconds | required parts |
|---|---|---|---|---|
| hook | 55-130 | 3-5 | 20-45 | hook |
| worked | 110-430 | 6-12 | 45-150 | hook, ground, idea, keeko |
| exercise | 110-520 | 6-12 | 45-180 | hook, ground, idea |
| theorem | 350-860 | 8-16 | 120-300 | hook, ground, idea, keeko |
| story | 1000-1100 | 17-20 | 330-420 | hook, ground, idea, keeko |

Speaking rate is fixed at 173 words/minute (`contract.WPM`); seconds follow
from words / (WPM/60) plus pauses.

There is exactly **one** `hook` per chapter (the opener; no topic hooks -
see the one-hook-per-chapter rule). It teaches nothing, shows no answer, no
formula, no symbol, and ends on an open question followed by the `Think and tell.` beat.

## `video_script` top-level keys (`contract.SCRIPT_KEYS`)

```
kind, chapter, source, placement, unlock, callback_to, why, substitution,
shape, promise, anchor, misconception_id, wrong_answer, wrong_move,
payoff_line, final_answer, answer_verified, terms, fraction_reading, names,
hold_back, never_show, maths_rules, design, open_questions, keeko_end, beats
```

- `kind` - one of the six above.
- `chapter` - `chapter.chapter_id` from the worklist.
- `placement` - `before` or `after`; `unlock` - `always` or `after_attempt`.
- `shape` - one of `concept`, `procedure`, `proof`, `application`.
- `final_answer.value` - written with digits and symbols; its numbers must
  be among the numbers of the worklist entry's own `answer`.
- `answer_verified` - `true` only if you recomputed the answer yourself and
  it agrees; otherwise `false`, with the doubt recorded in `open_questions`.
- `maths_rules` - every number, how it is computed, and what equals what.
  Digits and symbols are fine here, and in `on_screen` and `marks`.
- `keeko_end` - `misconception` or `real_life` in a concept video (`worked`, `theorem`, `story`); `""` otherwise.
- `names` - every `{{NAME_n}}` placeholder the video uses (n 1 to 10) with the character's role in the book, e.g.
  `{"{{NAME_1}}": "the child who walks round the park"}`; `{}` when none. See "Names" below.

## Beats (`contract.BEAT_KEYS`)

```
key, part, role, meaning, region, on_screen, marks, carries_over, colours,
removed, moves_through, pause_after, block, keeko, narration
```

- `part` - one of `hook`, `ground`, `idea`, `keeko` (`contract.PARTS`), in that order.
- `keeko` - `""`, `think` (the one `Think and tell.` beat, in the hook part: Keeko is only placed on screen) or
  `raise_hand` (opens the keeko part of a concept video).
- `role` - one of the seven pedagogical roles (`contract.ROLES`): connect
  objects, (co)vary objects, visualise a concept, visualise a process,
  symbol sense, connect to reality, generalise.
- `meaning` - one of `SHOW, BUILD, TRACE, COMPARE, TRANSFORM, VARY, FOCUS,
  BREAK, CONNECT`.
- `region` - `anchor`, `stage` or `working`.
- `block` - one of the fixed visual block types (`contract.BLOCKS`): board
  layouts like `title_card`, `worked_example_board`, `theorem_board`,
  `triangle_figure`, `coordinate_plane`, and so on - the full list is in
  `contract.py`.
- Optional: `photo` (see "Photos inside videos" below).

## Lengths and pacing (unconditional)

- Sentences of 18 words or fewer, averaging 9-12 (`contract.SENTENCE_MAX`,
  `SENTENCE_AVG`).
- A beat is 130 words or fewer (`contract.BEAT_WORDS_MAX`).
- A bookmark within the first 4 spoken words of every part's first beat
  (`PART_START_BOOKMARK_WITHIN`), never more than 28 words between bookmarks
  (`BOOKMARK_GAP_MAX`). Every bookmark has a `marks` entry saying what
  arrives, moves or lights up, and every `marks` entry has a bookmark.
- `pause_after` is 0 on every beat except the one `Think and tell.` beat, which has 3 (`THINK_PAUSE`).

## Language rules

- Plain words, British spelling, English only. `contract.AMERICAN_SPELLINGS`
  and `contract.HINGLISH` are both banned lists the checker scans for.
- No line starts with "So", "Now", "Alright", "Well" or "Okay"
  (`BAD_LINE_STARTS`).
- `contract.BANNED_WORDS` (just, simply, basically, obviously, easy, thus,
  hence, therefore, points, stars, score) and `BANNED_PHRASES` ("believe in
  yourself", "you can do it", "level up") never appear.
- Say the operation ("multiply", "take away"), not the book's own word
  (`BOOK_OPERATION_WORDS`: product, difference, quotient, per - a chapter
  may allow one of these as its own subject word, e.g. "difference" in an
  integers chapter; "per" is always allowed in "per cent").
- `BOOK_WORD_SWAPS` lists specific textbook phrasings to avoid verbatim.
- Narration is words only: no digits, no symbols, no en or em dash anywhere
  (use a comma), the letter "a" written "eigh" (`SPEECH_BANNED_CHARS`,
  `DASHES`).
- A reason beat uses one of `REASON_WORDS` (because, since, as we, so that,
  that means); a definition beat uses one of `DEFINE_WORDS`.

## Keeko and the think-and-tell

Keeko (mascot, no voice) replaces Chintu; the teacher speaks everything.

- **Exactly one** `Think and tell.` beat per video (every kind): hook part, `pause_after: 3`, `keeko: "think"`.
- A **concept video** ends with the keeko part. Its first beat has `keeko: "raise_hand"` and the teacher says
  "Keeko has raised a hand. Let us check the doubt and solve it." Then either `keeko_end: "misconception"`
  (`misconception_id`, `wrong_answer`, `wrong_move` filled; the wrong idea is first said here, as "Keeko thinks ...") or
  `keeko_end: "real_life"` (a `connect to reality` beat from the chapter's own NCERT text; the three misconception
  fields are empty).
- `hook` and `exercise` videos have no keeko part, no raised hand, no misconception and no real-life beat.
- No narration says "recap", "your turn" or "try again with this".

## The idea part is a board solution

Beat keys in order: `given`, `find`, `step_1` ... `step_n`, `answer`. One line per beat; the `payoff_line` is said in
`answer`. An exercise video uses the method of the book's solved example and names it in `callback_to`.

## Names

Every character name, the book's own included, is a `{{NAME_n}}` placeholder (n 1 to 10; one character = one token
across the chapter), mapped in `<chapter>/new_design/name_slots.json`:
`{"{{NAME_1}}": {"original": "Rakesh", "role": "..."}}`. A script never writes an original name; a token not in the
file fails. A token counts as one word. No gendered pronoun for a named character.

## Book guard

A hook and a theorem video never reuse the numbers of any book question (`chapter.exercise_numbers` from the
worklist). A `worked` video's hook part says the item is "from your book".

## No book numbers in text (docs/27 rule, enforced on every chapter)

No Q3, Example 2, Exercise 4.2, Figure it Out 3.1, Section 3.1, "part (b)",
or "Figure 1" anywhere - title, description, teaching notes, on-screen text,
marks, narration or notes. A title card shows the topic or set name instead.
Kept: trace ids (`source`, `video_coverage`, `callback_to`, bookmark marks),
list markers like (a)/(i) inside a multi-part question, and bare theorem
numbers ("Theorem 4") outside the Class 9/10 variant - see `docs/04` for
where the Class 9/10 rule is stricter than this base rule.

## Four script rules (docs/27, enforced by `contract.py`'s own constants)

1. **No tool references.** A video never says it saw what the student
   played - no "tool", "sandbox", "playground", "simulator", "slider",
   "free-try", or "you just built/played/dragged" (`contract.TOOL_REFERENCE`).
2. **The chapter hook carries a photo** - one beat with a `photo` field.
3. **Nothing outside the textbook.** Names are placeholders (see "Names"), and no word from the chapter's
   `book_rules.json` `"banned_words"` list (an analogy or trivia the book never printed)
   appears anywhere.
4. **A theorem video states the theorem.** A beat keyed `state`
   (`contract.THEOREM_STATE_BEAT`) whose narration holds every phrase listed
   for that script in `book_rules.json`'s `"theorems"`.

## Photos inside videos

A photo is a Gemini-generated picture of a real thing, place or scene,
shown for exactly one `connect to reality` beat, then replaced by the drawn
schematic. It is never a concept image and never carries a number, label or
any text the maths depends on.

- **Who gets one**, by grade (from the worklist's `grade`): Class 3-6, every
  distinct real-world anchor scene (reused across videos that share it, one
  photo per scene); Class 7-8, a specific real thing by default, a generic
  scene only on a stated `need_basis`; Class 9 and up, a specific real thing
  only, never a generic scene.
- **Never**: a named historical figure with no authentic likeness
  (`contract.PHOTO_NO_LIKENESS` - Baudhayana, Pythagoras, Fibonacci, Euclid,
  and others), a living person, Keeko or any named character (they stay
  drawn), a map (always drawn), a book photo.
- **Library file**: one per photo, `<chapter>/photos/<id>.json`, keyed by
  `id`, with `subject_type` (thing/place/nature/artwork/document/scene/
  person), `gemini_prompt` (never a digit; always says "no text"; never a
  count the maths depends on), `maths_on_object` (true only when the maths
  itself lives on the real object, paired via `pair_with` with the drawn
  schematic that carries it).
- **The beat**: `"photo": {"id": "ph_...", "placement": "full"|"backdrop"|
  "left"|"right"}` (`contract.PHOTO_PLACEMENTS`). Narration, marks and
  timings are unchanged by adding a photo.

## Checking your work

```bash
python -B core/video_script/check.py --worklist <chapter>/video_worklist.json --file <chapter>/video_scripts/<key>.json
```

or, for a whole chapter's `video_scripts/` directory at once, pass `--dir`
in place of `--file`. Fix everything until it prints `ok` (and `photos ok`
when the chapter uses photos). If a check seems wrong for a specific case,
say so with the key and the exact message rather than reshaping the text to
force a pass.

## Final names (29 Oct 2026)
The `{{NAME_n}}` tokens are replaced by Ruhee, Ziva, Laksh, Jia and Leeza with `core/video_script/fill_names.py` (see AUTHOR_BRIEF.md, "Filling the placeholders"). The token scripts stay in `video_scripts_tokens/`; the mapping is in `name_assign.json`.
