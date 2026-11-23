# Brief (v3 rules): diagram decisions for one chunk of Class 8 Ch 9 "The Baudhāyana-Pythagoras Theorem"

You decide, for every question, solution and worked example in ONE chunk of the live plan (cbse_eng_maths8_ch9_v54), whether it needs a
diagram image, you write the full diagram spec for each one that does, and you account for every NCERT figure that
belongs to your chunk. You change nothing else. (This plan is edited IN PLACE as a new V2 version: only the question/solution
image placeholders change; videos, tools and concept images stay.)

All paths are under `/root/maths-learning-plan/Learning-Plan-Maths/chapters/maths8_ch9/v2_diagrams/` (call it HERE). Tools: `/root/maths-learning-plan/Learning-Plan-Maths/chapters/_diagram_rollout/validate_map.py`.

## Read first (in this order)
1. `HERE/spec/diagram_identification_prompt_v3.md` - the rules (v3). EVERY section is binding: Step 0 inventory, Step B2
   (printed answer is a picture, lettered figures, the 'refer picture' rule, sibling consistency), Step C codes, the "Not a
   diagram" list, sections 4 to 7 (7 = diagram types; use `other` with a COMPLETE description when nothing fits) and section 9
   (self-check). Its section 8B (writing into the LP) is done by a builder script, not by you: you only produce the map of
   section 8. v3 in short: a solution diagram token is ALWAYS `steps_tex` / `before_first_step`; a question or worked-example
   token is `question_tex` / `after_question_text`; a teaching (concept) image is NEVER linked (no `reuse_concept_image`, no
   `reuse_media_id`); a lettered or referred figure is drawn even when a teaching image shows it; `decision: none` ->
   `drop_image` (pairs and singles) or `no_image` (worked examples).
2. `HERE/spec/companion_note.md` - the figure-content rule: a question's figure shows ONLY what the question gives; a
   solution's figure shows the COMPLETE final state; no question figure when the question gives none; labels consistent.
3. `HERE/spec/diagram_map.schema_v3.json` - the output schema (figure_inventory and coverage_report are required).
4. Your chunk file `HERE/map/in_<CHUNK>.json` (units in LP order).
5. The book (Ganita Prakash, Grade 8, 22 pdf pages): `HERE/book/chapter_text.md` (text of each pdf page) and the page pictures
   `HERE/book/page_NN.png` (NN = pdf page, two digits). Chapter pages 1-22. This pdf has NO printed-solutions section: the LP solution text is the answer to follow. LOOK at the picture of
   every page your items use, solutions pages included: figures are often only in the pictures.
6. The base figure inventory (Step 0, built by other agents from the page pictures): `HERE/map/inv_base_chapter_01_16.json`, `HERE/map/inv_base_chapter_17_22.json`. Each entry has fig_id, page,
   section, belongs_to, kind, shown_as, description.
7. `HERE/map/concept_images.json` - the 17 teaching (concept) images that already exist in the plan.

## What a unit is (the chunk file)
- `kind: "pair"`: a question concept (`question_concept`) and its answer concept (`answer_concept`). They become TWO items: role
  `question` (lp_concept_id = the question concept id) and role `solution` (lp_concept_id = the answer concept id). Decide the two
  sides separately (Step E). A concept can hold several blocks that share ONE card: `item` is the first block and `extra_items`
  the others; the pair still gets at most ONE question diagram and ONE solution diagram. `kept_image_ids` lists the concept's images
  that stay (teaching images): never reuse those ids.
- `kind: "single"`: ONE block of a concept (`concept_id`, `block_index`) that holds the question AND its solution and links the
  old question/solution card(s) (`question_cards` / `solution_cards`, with their descriptions: hints only). It becomes TWO items with the
  SAME lp_concept_id and the SAME `block_index`: role `question` and role `solution`. The block's `item` carries the question/steps/
  answer; if the block is empty ("read the question in the book"), the real text sits in `lp_text` (a 'Practice' block of a teaching
  concept; that block is NOT a unit of its own: do not make an item for it) and the hints `item.q_figure` / `item.s_figure` and `video`
  (`maths_rules`, `final_answer`) describe it. Judge from the text, the BOOK question and the video's final answer.
- `kind: "worked"`: a worked-example block inside a teaching concept (question + steps + answer in one block, no card). ONE item,
  role `worked_example`, lp_concept_id = the concept id, `block_index` = the unit's `block_index`. Its single diagram is the picture
  the example needs.
- `item` fields: `question`/`question_tex`, `steps`/`steps_tex`, `answer`/`answer_tex` (what the LP says), `text`, `q_figure` /
  `s_figure` (a sentence an earlier author wrote about the figure: a HINT only, often wrong or thin), `book_number`, `ncert_refs`.
  The LP's own numbering can differ from the book's: find the item in the book by its text.
- There are NO usable old image ids: the old question/solution cards are being replaced, and a missing id never means "no
  diagram". Judge every item with the rules.
- The LP solution text wins over the book's printed answer if they disagree (note it).

## Step 0 for your chunk (mandatory, and checked by a script)
For every base-inventory figure that belongs to your chunk, write one `figure_inventory` entry with the SAME `fig_id` and exactly
one `mapped_to`:
- `item:<concept_id> (question)` or `item:<concept_id> (solution)` - it becomes that item's diagram; for a worked example write
  `item:<concept_id> (question)` (`item:<concept_id>#<block_index> (question)` when the concept holds several blocks); the
  item you name must be `required` in your `items`;
- `concept_image:<media_id>` - a teaching figure already in `concept_images.json` (accounting only: nothing is linked to it);
- `none:<REASON_CODE>` - with a code from Step C (e.g. LATEX_TABLE, DECORATIVE_ONLY, SAME_AS_QUESTION_DIAGRAM, TEXT_SUFFICIENT).
A figure belongs to your chunk if it is in the book section of one of your units, OR one of your units' question/answer uses it
(printed-answer pictures belong to the chunk of the question they answer). Another chunk may claim the same figure for its own
item; duplicates are compared at merge, so keep your reason sound and, if two chunks could claim the same base figure, give it the
SAME mapped_to meaning (a figure used by two items is two entries: the base id for the first use, `NEW-<base id>-<suffix>` for each
further use). Check each base description against the page picture; if it is wrong, say so in your entry's `description` (start with
"CORRECTED:") and use the right facts. A figure you find that is missing from the base gets a fig_id starting `NEW-`.
`coverage_report.unmapped` must be 0, and the counts in it must equal the entries you wrote.

## Decision rules specific to this run
- Only `required` diagrams are added to the plan. `optional` = a figure that would clearly help but is not needed: it is NOT
  added (action `drop_image` / `no_image`), the reason says what figure would help. Prefer `none` unless a v3 rule or the
  tie-breaker says the picture matters. Text and LaTeX are the default.
- Question side `required` only if the learner needs the figure to ATTEMPT it (what the book question GIVES). Solution side
  `required` only if the solution adds something visual or the printed/LP answer IS a picture/arrangement/drawing (B2); if it would only
  repeat the question figure, `none` with `SAME_AS_QUESTION_DIAGRAM`. A required solution diagram whose question has a diagram
  has `derived_from` = the question diagram's media_id (same layout, same positions, new content in ANSWER green).
- A question with no given figure gets NO question diagram, even when the solution has one.
- Sibling consistency (B2): the same kind of answer in the same NCERT question set gets the same decision, or `reason` says why.
- Plain tables of numbers, arithmetic, sequences, word reasoning stay text/LaTeX (`LATEX_TABLE`, `LATEX_ARITHMETIC`,
  `TEXT_SUFFICIENT`). Judge item by item; neither "none" by habit nor "required" by habit.
- Every number, label, count and position in `content` must come from the item, the LP solution, or the book page. Recompute every
  sum, count, scale and rule you state in `accuracy_checks`. Where the book is unclear or contradicts itself, say so in the spec's
  `render_note` and in your notes file instead of inventing a number.
- A teaching image is never linked. If a figure you need is also a concept image, the item still gets its own diagram when it
  needs one (v3 prompt section 2, Step B2); only the 'refer picture' rule of Step B2 makes a question `optional` instead.
- The same book picture used by several items gets one diagram PER ITEM (identical spec, say in `render_note` "same as <id>").

## Ids and placeholders (mechanical; the validator checks them)
- `media_id` = `<lp_concept_id>.IMG<n>`, n = the lowest number not used by a kept image of that concept (`kept_image_ids`) and not
  used by another item of the same concept (a single with both diagrams: question n, solution n+1; blocks of one concept take
  n, n+1, ...). The build renumbers the ids in media-list order as the upload server demands, so just keep them unique and
  collision-free.
- Question diagram: `lp_placeholder_action` = `keep_and_replace_spec`, `placeholder` =
  `{"token": "{{DIAGRAM:<media_id>}}", "insert_into": "question_tex", "position": "after_question_text"}`.
- Solution diagram: action `keep_and_replace_spec`, `placeholder` = `{"token": ..., "insert_into": "steps_tex", "position": "before_first_step"}` ALWAYS.
- Worked-example diagram: action `add_new_image`, `insert_into` `question_tex`, position `after_question_text`; `block_index` = the unit's.
- singles and worked items ALWAYS carry `"block_index": <the unit's block_index>`; pair items need none.
- `decision: none` -> pairs and singles: action `drop_image`; worked examples: `no_image`. `media_id` null; no `diagram`, no
  `placeholder`. Always `reason_codes` and a one-line `reason`; `text_alternative` where it helps (e.g. the LaTeX table to write).
- `decision: optional` -> action `drop_image` / `no_image`, no `diagram`, `reason` says which figure would help.
- `manim_description`: imperative, complete, exact values, left-to-right / top-to-bottom, colour tokens by name (BG INK MARK_FILL
  ANSWER FOCUS GUIDE SET_A SET_B CELL_FILL), explicit counts / coordinates / values so that nothing is left to guess, and NONE of
  the words some / several / etc. / similar / a few / various. `visible_text`: every string drawn and nothing else (no "Q1", "Figure
  it Out", "Find", "Answer", "Table 2", headings; axis titles, category labels and values the figure needs ARE allowed). `must_not_show`:
  copy the list from the prompt's example, add specifics. `alt_text`: one sentence. Aspect ratio: 16:9 unless the figure is
  clearly tall (the pipeline draws diagrams as 16:9 cards). Number style: the LP's own / the book's.
- `diagram.content` needs `"type": "<diagram_type>"` (same value as `diagram_type`) plus every value needed to draw it.
- Each required item also gets `"manim_scene"` (`c8_9_<section>_<item>_q` / `_sol`, any unique string).

## Output
Write ONE JSON file `HERE/map/out_<CHUNK>.json` in the shape of the v3 schema: `meta` (chapter "The Baudhāyana-Pythagoras Theorem", class 8, textbook
"Ganita Prakash, Grade 8, Chapter 9", lp_plan_id "cbse_eng_maths8_ch9_v54", prompt "diagram_identification_prompt.md v3", placeholder_token_format
"{{DIAGRAM:<media_id>}}", counts_by_role_and_decision matching your items, notes), `style_tokens` (the table in prompt section 6),
`figure_inventory`, `coverage_report` (`inventory_figures`, `mapped_to_items`, `mapped_to_concept_images`, `mapped_none`, `unmapped: 0`,
`new_media_ids_created` = the media_ids of your required items, `lp_ids_dropped` = []), `items` (LP order, `none` ones included; a pair
or single gives its question item then its solution item). Write the JSON with a Python script kept OUTSIDE HERE (scratchpad or /tmp).

Then run, and fix until it prints `errors 0`:
`python3 -I -X utf8 /root/maths-learning-plan/Learning-Plan-Maths/chapters/_diagram_rollout/validate_map.py HERE/map/out_<CHUNK>.json --chunk <CHUNK> --here /root/maths-learning-plan/Learning-Plan-Maths/chapters/maths8_ch9/v2_diagrams/`

ALSO write `HERE/map/notes_<CHUNK>.md` (plain markdown, as long as needed): (1) judgement calls you were unsure about (item, what
you chose, why); (2) anything in the LP that looks wrong (a solution that contradicts the book, a question text that lacks what
only the figure carries, wrong book numbers, duplicated text); (3) places where the book itself is unclear.

Do not edit any other file, do not touch staging, do not upload anything. Your FINAL MESSAGE must be SHORT (at most 60 words):
"Chunk <X> done: required R / optional O / none N, validator errors 0, notes in map/notes_<X>.md" plus ONE line if something
needs the user's decision. Do not paste the JSON or the notes.


## Decisions from the user (23 Nov 2026) - BINDING, they override anything above that says otherwise
1. **Book mistakes.** When the book's picture or printed answer is wrong (a print slip: a wrong digit, a missing minus sign, a wrong count), the diagram spec shows the CORRECT value, the one the mathematics and the LP solution give. The base inventory keeps recording what the book prints, but `content`, `manim_description` and `visible_text` use the corrected value. Say in the item's `reason` and in your notes which value the book prints and why you corrected it. If the LP text and the book disagree and the LP is mathematically right, follow the LP.
2. **LP text mistakes or missing data.** Do NOT edit LP text and do not change a decision because of it. Only list each case in your notes under a heading `LP text issues` (concept id, what is wrong or missing, suggested sentence).
3. **Figure letters.** When one picture holds several lettered figures, show the letters (a), (b), ... in the picture only if the LP answer text refers to the figures by letter; otherwise draw no letters. Letters you do show may appear in `visible_text`.
4. **Borderline items.** Apply the v3 rules as written. Do not flip a `required` item to `none` only because the LP text carries all the numbers. List borderline calls in your notes under a heading `Borderline`.
