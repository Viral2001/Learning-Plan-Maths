# Author brief: writing Class 6 to 8 video scripts (Keeko design, 28 Oct 2026)

You write the **videos** of one chapter's learning plan. Each video is **one JSON file**, and a render pipeline
turns it into a finished video without asking anyone. So the script must be complete, true and clear. This brief is
the whole contract; the checker (`core/video_script/check.py`) enforces most of it, and
`core/video_script/test_video_script.py` (function `reference()`) holds one complete, passing script to copy the
format from. Do not copy its maths.

## 1. The four kinds of video
| kind | what it is | words | beats | parts, in order |
|---|---|---|---|---|
| `hook` | the chapter opener, the only one in the chapter; teaches nothing | 55-130 | 3-5 | hook |
| `worked` | **concept video**: one solved example from the book, taught step by step | 110-430 | 6-12 | hook, ground, idea, keeko |
| `theorem` | **concept video** for a proof | 350-860 | 8-16 | hook, ground, idea, keeko |
| `exercise` | **question video**: one unsolved book question, solved step by step | 110-520 | 6-12 | hook, ground, idea |

There is **no recap** (no recap part, no recap video) and **no break part**. Nothing says "your turn", "try again
with this" or "recap".

## 2. Keeko and the one think-and-tell
Keeko is a mascot who has no voice. The teacher speaks everything.
- **Think and tell.** Every video (hook, worked, theorem, exercise) has **exactly one** beat that says
  `Think and tell.` The beat sits in the hook part, has `pause_after: 3` and `keeko: "think"`. Keeko is only
  placed on screen for it, as the child; no hand, no movement. Put the question the child must answer in the beat
  before it (a hook ends on its open question, then comes `Think and tell.`). This is the **only** beat with a
  nonzero `pause_after`.
- **Keeko's raised hand** ends every concept video (`worked`, `theorem`). It is a `keeko` part of one or two
  beats. The first beat has `keeko: "raise_hand"` and the teacher says "Keeko has raised a hand. Let us check the
  doubt and solve it." Then the script has **either**
  - `keeko_end: "misconception"`: the teacher says the wrong idea as Keeko's doubt ("Keeko thinks ..."), then
    breaks it and gives the right idea. Fill `misconception_id`, `wrong_answer` (said first in the keeko part,
    never earlier) and `wrong_move`; or
  - `keeko_end: "real_life"`: the teacher ties the idea to real life, in a beat with role `connect to reality`.
    `misconception_id`, `wrong_answer` and `wrong_move` are empty strings.

  Pick the misconception when the worklist `misconceptions` has one for this video; otherwise real life.
  Real life comes **from the chapter's own NCERT text** (the book's contexts, objects and figures); do not invent a
  new setting.
- `hook` and `exercise` videos have **no** keeko part, no raised hand, no misconception and no real-life beat
  (`keeko_end` is an empty string; the chapter hook still shows its photo beat). `keeko` is `""` on every other
  beat.

## 3. Follow the NCERT book exactly
You are given the book chapter (PDF text) with your task. Match it for every video:
- **Objects, colours, quantities, people and settings are the book's.** A blue ball stays blue; a rectangle that is
  eight by five stays eight by five. If the book does not say, stay general; never invent a detail.
- **An unsolved question (`exercise`) uses the method of the book's solved example on the same idea.** Never bring
  in a new method. Put that solved example's video key in `callback_to` (the worklist entry's `method_from` lists
  the keys; use the first that fits). Say "the same way as the example in your book", never a number.
- For `worked` and `theorem`, solve exactly as the book solves it.

## 4. The board solution (the idea part)
The idea part is a solution written the way a board examination expects, **one line per beat**, with these keys in
this order: `given`, `find`, `step_1`, `step_2`, ..., `answer`.
- `given`: what the question gives. `find`: what is asked (a theorem: `On screen` shows "Given" and "To prove").
- Each `step_n`: one operation, with the formula or rule named, and the values shown **before** they are combined
  (show the numbers before squaring, before adding, and so on). A proof step gives its reason ("because ...").
- `answer`: the last line; it says `payoff_line` and states the result with its unit. The held-back answer is not
  on screen or in speech before this beat.
- An `exercise` ends with its check ("put the answer back in the question") as the last `step_n` before `answer`.
- The `ground` part, before the idea, builds only the objects and words the solution needs; a new word is defined
  in the beat where it first appears (`terms`, at most two, three for a theorem).

## 5. Names are placeholders
Write every character name as `{{NAME_1}}` to `{{NAME_10}}`, including the names the book uses. The chapter's
`name_slots.json` maps each token to the book character (one character = one token, chapter-wide); use the token
the file gives. Never write the original name. Use no gendered pronoun for a named character; repeat the token.
`names` in the script lists exactly the tokens the video uses, each with the character's role in the book:
`{"{{NAME_1}}": "the child who walks round the park"}` (an empty dict when the video uses none). A token counts as
one spoken word.

### Filling the placeholders (29 Oct 2026)
The user fixed five pupil names: Ruhee, Ziva, Laksh, Jia, Leeza (`core/video_script/final_names.json`). Authors still
write `{{NAME_n}}`. Once a chapter is final, `python -B core/video_script/fill_names.py chapters/<ch>/new_design`
(or `--all`) copies `video_scripts/` to `video_scripts_tokens/` (the placeholder source of truth; never overwritten),
colours the chapter's tokens with the five names (two tokens that share a video never get the same name; a
book-stated male character goes to Laksh when possible), writes `name_assign.json` and rewrites `video_scripts/`.
Edit a script in `video_scripts_tokens/` and rerun the fill; `check.py` accepts either tokens or the five names.

## 6. What to read first
1. The chapter's `video_worklist.json`:
   - `chapter` holds the chapter id, the words this chapter may use (`allow_words`), and the numbers of every book
     question (`exercise_numbers`, used by the book guard).
   - `videos` holds one entry per planned video: `kind`, `source`, `item_ids`, `items` (question, steps, answer),
     `answer` (your `final_answer` must agree), `concept_text`, `misconceptions`, `key_terms`, the topic's name and
     objective, `forbid_words` (this video must not use them), `handover`, and `method_from` (exercise only).
2. `new_design/book_rules.json` (words the book never uses) and `new_design/name_slots.json`.
3. The NCERT chapter text you were given, and the chapter's other videos where you need to follow a method.
4. If you need more, the chapter's authored files (`topics_*.py`, `content.py`). Only read them; never edit them.

### The files you start from
Every key already has a **skeleton** file in `video_scripts/` from the old design: the recap and break parts and the
old pauses are gone, the stop beat is now the `Think and tell.` beat, names are tokens, and `keeko` / `keeko_end`
are empty. The old content is not trusted: rewrite each file (edit it in place) to the rules above. Where an old
script had a Chintu doubt or a recap, `new_design/migration_notes/<key>.json` keeps the removed beats and the old
wrong idea; use it only as raw material (the old recap's "how to check" is a good last `step_n` of an exercise).
`name_slots.json` may list `_overflow` names: characters with no token because the chapter has more than ten. Never
write them; say the role instead ("the teacher", "a farmer"). Slots with `in_book: false` are invented children,
used only when the book gives a question no person; prefer the book's characters.

## 7. What to write
For each key you own, write `<chapter folder>/new_design/video_scripts/<key>.json`:

```json
{"key": "<key>", "title": "<a question, at most 70 characters, that does not give the answer>",
 "description": "<two or three sentences: what the video shows and the idea it teaches>",
 "teaching_notes": "<one to three sentences for the tutor: the one idea, the slip to watch for>",
 "video_script": { ... }}
```

Description and teaching notes follow the Class 7 Chapter 10 style. A description tells what is on the board and what
changes, in plain words with numbers spelt out, then names the slip the video breaks (in a concept video, Keeko's
doubt). Teaching notes start "One idea: ..." and end "Watch for students who ...". Example:
> description: "Negative factors pair up, and each pair multiplies to a positive. In negative two times three times
> negative one times negative four, one negative is left without a pair, which gives the sign."
> teaching_notes: "One idea: count the negative factors; an even count gives a positive answer, an odd count a
> negative one. Watch for children who think negatives always cancel."

`video_script` has exactly these keys (see `core/video_script/contract.py`, `SCRIPT_KEYS`):
`kind, chapter, source, placement, unlock, callback_to, why, substitution, shape, promise, anchor, misconception_id,
wrong_answer, wrong_move, payoff_line, final_answer, answer_verified, terms, fraction_reading, names, hold_back,
never_show, maths_rules, design, open_questions, keeko_end, beats`.
- Copy the entry's `kind`, `source`, `placement` and `unlock`. `chapter` is `chapter.chapter_id`.
- `final_answer` is `{value, spoken, units}`; `value` uses digits and symbols and its numbers must be among the
  numbers of the entry's `answer`. `hold_back` lists the answer as it would appear on screen.
- `answer_verified` is true only if you recomputed the answer and it agrees; otherwise false, with the doubt in
  `open_questions`.
- `maths_rules` holds every number, how it is computed, and what equals what (digits and symbols are fine here and
  in `on_screen` and `marks`).
- `anchor` is the object or scene the video draws, **the book's own**. `promise` is `""` except in a story video.
- Each beat has: `key, part, role, meaning, region, on_screen, marks, carries_over, colours, removed, moves_through,
  pause_after, block, keeko, narration` (and optional `photo`). Roles, meanings, regions and blocks are the lists
  in `contract.py`; leave `block` empty unless sure.
- Narration is words only: no digits, no symbols, no brackets, no en or em dash anywhere in the file (use a
  comma), and the letter a written `eigh`.

## 8. Rules the checker enforces
- **Lengths:** sentences of 18 words or fewer, averaging 9 to 12. Beats of 130 words or fewer.
- **Bookmarks:** a bookmark within the first 4 spoken words of every part's first beat, and never more than 28
  words between bookmarks. Every bookmark has a `marks` entry saying what arrives, moves or lights up, and every
  `marks` entry has a bookmark.
- **Language:** plain words; British spelling; English only; no line starting So, Now, Alright, Well or Okay. Banned:
  just, simply, basically, obviously, easy, thus, hence, therefore, points, stars, score. Say the operation
  ("multiply", "take away"), not "product" or "difference". Never say "exercise"; say "a question from your book".
- **The hook part** of a `worked` or `exercise` video names the book item ("This is a question from your book").
  A `hook` video shows no answer, no formula and no symbol on screen, and ends on an open question, then the
  think-and-tell beat.
- **No book numbers** anywhere: no Q3, Example 2, Exercise 4.2, Figure 1, "part (b)". Name the topic or the idea.
- **No tool talk:** never say the student played or built something with a tool.
- **Book guard:** a hook and a theorem video never reuse the numbers of a book question (`exercise_numbers`).
- **Nothing outside the book:** no word listed in `book_rules.json` `banned_words`.
- **A theorem video** has a beat keyed `state` that says the theorem (the phrases `book_rules.json` lists) and
  shows it on screen.

## 9. What the checker cannot see (reviewers have caught these before)
- **No answer leaks by meaning:** the title is a question without the answer; an explain beat does not state the
  reason the child is about to be asked for; a hint never names the answer.
- **Exact maths:** compute every number yourself, never recall one. Check every equation in `maths_rules`.
- **Pictures:** every drawn number, length or angle follows `maths_rules`. Never fake a picture.
- **NCERT fidelity:** compare each object, colour, number and context with the book text before you finish.

## 10. Photos inside the video
A photo is a Gemini-generated picture of a real thing or place. It sits on one `connect to reality` beat, which is
the chapter hook's opening beat or a `real_life` Keeko beat, fades at the end of the beat, and the drawn schematic
carries the maths. It never holds a number, a count the maths uses, a label or any text.

- Class 3 to 6: a real-world scene the book uses; Class 7 and 8: a specific real thing, a generic scene only with
  `need_basis`; Class 9 and up: a specific real thing only. Never a person with no authentic likeness, a living
  person, Keeko or any named character (they stay drawn), a map, or a book photo.
- Library file, one per photo: `<chapter>/new_design/photos/<id>.json` (name = id) with `id, subject_type, subject,
  why, need_basis, gemini_prompt, alt_text, reference, maths_on_object, pair_with`. The `gemini_prompt` never has a
  digit and always says "No text". No en or em dash.
- The beat: `"photo": {"id": "ph_...", "placement": "backdrop"}` (full, backdrop, left or right), and its
  `on_screen` starts with where the photo sits and that it fades at the end of the beat. Change nothing else.

## 11. Check your work
Run this for every file you write, from the repo root, and fix everything until it prints `ok`:

    python -B core/video_script/check.py --worklist "<chapter folder>/new_design/video_worklist.json" --file "<chapter folder>/new_design/video_scripts/<key>.json"

For a whole chapter, replace `--file ...` with `--dir "<chapter folder>/new_design/video_scripts"` (it also prints
`photos ok`). If you are sure a check is wrong for your case, do not twist the text to pass it. Say so in your
final report, with the key and the message.

## 12. Finish
Reply with the keys you wrote, any `open_questions` you set, and any checker message you think is wrong. Do not
edit any file outside `video_scripts/` (and `photos/` when you add a photo), and do not touch keys you do not own.
