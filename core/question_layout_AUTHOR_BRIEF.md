# Authoring the layout spec of a live chapter

You are deciding, for ONE live chapter, which content of the plan is a **book question** and where it goes. The engine
(`core/question_layout_live.py`) does the moving, renumbering and image placeholders; you write the spec it reads.
Read this whole file first. The spec format is in the docstring of `core/question_layout_live.py`; a finished example
(Class 7 Ch 10, 40 questions) is `chapters/maths7_ch10/new_design/layout_spec.json`.

## The layout you are producing

    concept topic -> "Questions: <that topic>" -> next concept topic -> "Questions: <next topic>" -> ...

and the Questions topic holds **one concept per book question**, in the book's order, each with its own video and its
own question image and solution image (placeholders, made by the engine).

## What is a book question

Count these, and only these:

* **example** - a solved example printed in the book ("Example 3: ..."). The student attempts it, then sees the working.
* **exercise** - a Figure it Out / exercise question printed in the book.
* **prompt** - an answerable in-text question: a "Try This" with an answer, an "answer the following" question, a blank
  to fill, a "find ..." or "how many ...?" put straight to the reader and having a definite answer.

Do NOT count: Math Talk and "what do you notice / why do you think" discussion; open puzzles, games and activities that
have no single answer; history and stories; statements; examples the plan authored itself with its own numbers (they
teach inside the teaching concept and stay there).

## What you work from

* `brief.md` - every topic, concept and **content block** of the live plan: `C` lines are concepts (flags: enrichment,
  thin-extra, obj Ox; media; concept refs); `b<i>` lines are blocks (kind / item_kind, refs, step count, the question).
* the live plan JSON next to it (full text of every block, if the brief line is not enough).
* the book chapter text `textbooks/extracted/<code>.txt` (page markers kept; "Try This" and "Math Talk" appear as
  lines "Try" / "This" and "Math" / "Talk"). The PDF is at `textbooks/class<N>/<code>.pdf` if you need a figure.

The plan can only give you a question that already has its question, steps and answer in a block. **Never invent
content.** A book question the plan does not contain goes in `notes.md` under *Gaps*, not in the spec.

## How to decide

1. Walk the book text in order and list every example, exercise and answerable prompt. Quote its label or first words.
2. Find each one in the plan: a block whose `question` matches it (same numbers and context), or an existing question
   concept. A teaching concept's worked example that simply retells a book example **is** that book question: cut it out
   with `block`. A teaching example with its own new numbers is not.
3. **Existing question concepts** (they sit in a Questions topic already): `keep` them, in book order, and put the new
   ones around them where the book puts them (examples and in-text questions come before the section's Figure it Out
   unless the book orders them otherwise). A `keep` entry may carry `q_figure` / `s_figure`. A new question may also
   be built ON an existing question concept by listing it first in `from` with `"whole": true` (use this to fold a
   follow-up block into the question it belongs to).
4. **Whole or block.**
   * `{"concept": id, "whole": true}` only for a concept that holds exactly one worked-example/exercise block and has no
     image or tool (typically a *thin-extra* worked-example concept, enrichment, no objective). Its video moves with it:
     set `keep_video_of` to the whole-moved concept whose video best covers the question. If a question merges several
     whole concepts, the others' videos are folded away (still in the live version's history).
   * `{"concept": id, "block": i}` for a block inside a teaching concept, or the `exercise` block inside a "Practice:"
     (doer) concept. Never move a teaching or doer concept whole. A question built only from blocks has no video yet
     (`keep_video_of: null`).
5. **One question = one concept = one ref.** `refs` holds exactly one coverage id. If the plan split one book question
   into several ids (parts, "method 2", a hint), fold them with `canon` (`{"old id": "kept id"}`) and list all their
   blocks in `from`, in reading order. A multi-part question stays one concept.
6. **Which Questions topic.** Normally the Questions topic of the concept topic the block sits in. Put it in another
   topic's only when the book clearly places it there.
7. **Names.** Match this chapter's existing question-concept style. For new ones: `Example 3: <3 to 6 word subject>`,
   `Try This (<section>): <subject>`, or `<Topic short>: <subject>`. No "NCERT", "textbook", "page N", "Fig.". No em or
   en dash. A minus sign is U+2212.
8. **Teaching concepts named after a moved example** (their name is "Example 1: ..." or similar): give them a teaching
   name in `rename_teach` so the example is not named twice.
9. **Diagrams.** When the question as printed depends on a diagram, table, number line, grid, token picture or shape,
   set `q_figure`: ONE plain sentence saying what the question card must draw, holding only what the question gives. It
   must not contain the result, a step, or the words hint, answer, solution, therefore, since, because, hence, proof,
   thus. `s_figure` is what the solution card needs drawn (it may show the result). A text-only question has neither.
   When unsure, leave them out.
10. Do not touch anything outside the spec. The engine keeps every existing question concept you do not list.

## Lessons from the first chapters (Class 6 Ch 9, Class 7 Ch 8, Class 8 Ch 6 are done: read their `layout_spec.json` and
`notes.md` under `chapters/<chapter>/question_layout/` as finished examples)

* **The book's icons are not decisive.** In these editions the "?" icon, the Math Talk icon and the Figure it Out icon
  all appear next to real questions. Judge by substance: is the reader asked something with a definite answer, and
  does the plan hold a block with that question, its steps and its answer? Then it counts. A pure discussion ("why do
  you think", "share your methods", "what do you notice") does not. A game or puzzle with one definite answer counts.
* **Two plan shapes.**
  * Class 6-7 style: the existing Questions topics ("Figure it Out: <topic>", sometimes "Practise: <topic>") hold
    enrichment concepts with no objective; teaching concepts carry worked-example blocks tagged with plan-chosen ids;
    thin-extra concepts are single-block worked examples with their own video (move those whole when they hold a book
    question).
  * Class 8 style (and Class 6 Ch 3): the Questions topics are "Questions: <topic>" and their concepts carry
    objectives and a tool link, so `keep` them as they are. Every teaching and practice concept carries an objective
    and an image, so nothing there can move whole: cut blocks. The "Practice: ..." (doer) concept at the end of each
    concept topic holds an `exercise` block that is a book question: cut it out; the practice concept keeps its recap,
    tool and video.
* If the plan's answer to a question contradicts the book or its figures, do not move it; say so in the notes.
* Two plan blocks that are one printed question (parts, "method 2", a follow-up) become one question: list both
  blocks in `from`, fold their ids with `canon`.
* `rename_teach` only when a teaching concept is named after a moved example or the name would now be duplicated.
* A book question the plan has no block for is a gap: list it, never invent it.

## Chapters whose Questions topics hold several questions in one concept

A few chapters (Class 6 Ch 6, Class 7 Ch 9 and Ch 15, Class 8 Ch 8 and Ch 10) were built differently: a Questions topic
may be typed "instructional" or "practice" instead of "exercise", and ONE question concept may hold several printed
questions as several blocks ("Figure it Out 1, 2, 3" with three blocks and one video). The layout needs one concept per
question, so split those:

    {"split": "<existing question concept id>",
     "into": [ {"name": "...", "tier": "exercise", "refs": ["<one coverage id>"], "blocks": [0]},
               {"name": "...", "tier": "exercise", "refs": ["<one coverage id>"], "blocks": [1], "q_figure": "..."} ],
     "keep_video_part": 0}

* every block of the concept goes to exactly one part; a part may take several blocks when they are one printed
  question (then give it one ref and fold the others with `canon`);
* the part named by `keep_video_part` (default the first) keeps the concept's video, images, tool link and objective;
  its video covers all the questions, so it is reported as "needs refresh". The other parts are enrichment concepts
  with no video yet;
* parts replace the original concept in place, in the order you list them, which should be the book's order;
* a Questions topic that already holds single-question concepts needs nothing: `keep` them as before.

Two Questions topics straight after one concept topic are merged into the first by the engine (one per topic); you do
not write anything for that. A summary or opening topic with its own Questions topic is left as it is.

If the live plan's concept-to-media links are already broken (a concept listing media that belongs to another concept
or has no node), do not try to repair it: report it at the top of `notes.md` and stop.

## Check loop (run it until it is clean)

    python -I -X utf8 core/question_layout_live.py check <chapter>/question_layout/<live plan>.json <chapter>/question_layout/layout_spec.json

* `SPEC PROBLEMS` must be empty; `INTEGRITY: clean`; and no `GATES WORSE THAN LIVE` line (the live plan already fails
  some gates; yours must not add failures).
* The printed counts are what you report. `check` writes nothing.

## What to write

1. `layout_spec.json` in the chapter's `question_layout/` folder.
2. `notes.md` next to it: a table of every NEW question (book label or quote, plan source, tier, why it counts), then
   *Borderline, not moved* (Math Talk and the like, one line each), then *Gaps* (book questions the plan has no content
   for), then *Judgement calls*.

Final reply (under 200 words): counts per tier, number of new videos needed, gaps, judgement calls, and the last lines
of the check output. Do not edit any other file, do not upload anything, do not call the network.
