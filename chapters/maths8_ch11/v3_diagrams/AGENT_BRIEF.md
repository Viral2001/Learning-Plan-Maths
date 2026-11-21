# Brief (v3 rules): diagram decisions for one chunk of Class 8 Ch 11 "Exploring Some Geometric Themes"

You decide, for every question, solution and worked example in ONE chunk of the live plan (V2 v31), whether it needs a
diagram image, you write the full diagram spec for each one that does, and you account for every NCERT figure that
belongs to your chunk. You change nothing else.

All paths are under `/root/maths-learning-plan/Learning-Plan-Maths/chapters/maths8_ch11/v3_diagrams/` (call it HERE).

## Read first (in this order)
1. `HERE/spec/diagram_identification_prompt_v3.md` - the rules (v3). EVERY section is binding: Step 0 inventory, Step B2
   (printed answer is a picture, lettered figures, the 'refer picture' rule, sibling consistency), Step C codes, the "Not a
   diagram" list, sections 4 to 7 (7 = diagram types: use `geometry_figure`, `solid_3d`, `net`, `views`, `symmetry_figure`,
   `tiling`, `grid_map`, ... and `other` with a COMPLETE description when nothing fits, e.g. fractal step pictures) and section 9
   (self-check). Its section 8B (writing into the LP) is done by a builder script, not by you: you only produce the map of
   section 8. v3 in short: a solution diagram token is ALWAYS `steps_tex` / `before_first_step`; a question or worked-example
   token is `question_tex` / `after_question_text`; a teaching (concept) image is NEVER linked (no `reuse_concept_image`, no
   `reuse_media_id`); a lettered or referred figure is drawn even when a teaching image shows it; `decision: none` ->
   `drop_image` (pairs and singles) or `no_image` (worked examples).
2. `HERE/spec/companion_note.md` - the figure-content rule: a question's figure shows ONLY what the question gives; a
   solution's figure shows the COMPLETE final state; no question figure when the question gives none; labels consistent.
3. `HERE/spec/diagram_map.schema_v3.json` - the output schema (figure_inventory and coverage_report are required).
4. Your chunk file `HERE/map/in_<CHUNK>.json` (units in LP order).
5. The book: `HERE/book/chapter_text.md` (text of each pdf page) and the page pictures `HERE/book/page_NN.png` (NN = pdf page
   01..33; the whole pdf is the chapter, there are NO printed solutions). LOOK at the picture of every page your items use:
   figures are often only in the pictures.
6. The base figure inventory (Step 0, built by two other agents from the page pictures): `HERE/map/inv_base_pages01_17.json`
   and `HERE/map/inv_base_pages18_33.json`. Each entry has fig_id, page, section, belongs_to, kind, shown_as, description.
7. `HERE/map/concept_images.json` - the 48 teaching (concept) images that already exist in the plan.

## What a unit is (the chunk file)
- `kind: "pair"`: a question concept (`question_concept`) and its answer concept (`answer_concept`). They become TWO items:
  role `question` (lp_concept_id = the question concept id) and role `solution` (lp_concept_id = the answer concept id).
- `kind: "single"`: ONE concept (`concept_id`) that holds both the question card and the solution card and a video; its own
  `item.text` is only "Work through the practice problem. Read the question in the book...". The LP's real question, steps and
  answer for it sit in a 'Practice: ...' block of a teaching concept, attached to the unit as `lp_text` (`lp_text.item.question`,
  `.steps`, `.answer`; `lp_text.concept_id` / `block_index` say where). That block is NOT a unit of its own, so do not make an
  item for it. A single becomes TWO items with the SAME lp_concept_id (= the single's `concept_id`): role `question` and role
  `solution`. Judge them from `lp_text`, the BOOK question (find it from `ncert_refs`, e.g. "FiO5.q2", and `lp_text`), and the
  hints `item.q_figure` / `item.s_figure`, `question_card.description`, `solution_card.description` and `video` (`maths_rules`,
  `final_answer`; often thin or wrong). A question diagram only if the learner needs the figure to attempt the question (what the
  book question gives, nothing more); a solution diagram if the answer is a picture / adds marks / is drawn in the LP solution.
- `kind: "worked"`: a worked-example block inside a teaching concept (question + steps + answer in one block). ONE item, role
  `worked_example`, lp_concept_id = the concept id, and `block_index` = the unit's `block_index` (a concept can hold several
  blocks: they are separate items, each with its own diagram or none). Its single diagram is the picture the example needs.
- `item` fields: `question`/`question_tex`, `steps`/`steps_tex`, `answer`/`answer_tex` (what the LP says), `text`, `q_figure` /
  `s_figure` (hints), `book_number`, `ncert_refs`. The LP's own numbering can differ from the book's: find the item in the
  book by its text / video.
- There are NO old image ids to go by: the old question/solution cards are being deleted, and a missing id never means "no
  diagram". Judge every item with the rules.
- The LP solution text wins over the book if they disagree (note it). For singles the LP solution is `lp_text` (the video's `final_answer` agrees with it).

## Step 0 for your chunk (mandatory, and checked by a script)
For every base-inventory figure that belongs to your chunk, write one `figure_inventory` entry with the SAME `fig_id` and exactly
one `mapped_to`:
- `item:<concept_id> (question)` or `item:<concept_id> (solution)` - it becomes that item's diagram; for a worked example write
  `item:<concept_id> (question)`, and `item:<concept_id>#<block_index> (question)` when the concept holds several blocks; the
  item you name must be `required` in your `items`;
- `concept_image:<media_id>` - a teaching figure already in `concept_images.json` (accounting only: nothing is linked to it);
- `none:<REASON_CODE>` - with a code from Step C.
A figure belongs to your chunk if it is in the book section of one of your units, OR one of your units' question/answer uses it.
Another chunk may claim the same figure for its own item; duplicates are compared at merge, so keep your reason sound. Check
each base description against the page picture; if it is wrong, say so in your entry's `description` (start with "CORRECTED:")
and use the right facts. A figure you find that is missing from the base gets a fig_id starting `NEW-`.
`coverage_report.unmapped` must be 0, and the counts in it must equal the entries you wrote. Two figures that are the same
picture used by two items are two entries (one per use) with different mapped_to.

## Decision rules specific to this run
- Only `required` diagrams are added to the plan. `optional` = a figure that would clearly help but is not needed: it is NOT
  added (action `drop_image` / `no_image`), the reason says what figure would help. Prefer `none` unless a v3 rule or the
  tie-breaker says the picture matters. Text and LaTeX are the default.
- This is a GEOMETRY chapter: many questions DO depend on a figure (fractal steps, solids, nets, views, shadows, isometric dot
  paper). Apply the tie-breaker honestly item by item - neither "none" by habit nor "required" by habit.
- Question side `required` only if the learner needs the figure to ATTEMPT it (what the book question GIVES). Solution side
  `required` only if the solution adds something visual or the answer IS a picture/arrangement/drawing (B2); if it would only
  repeat the question figure, `none` with `SAME_AS_QUESTION_DIAGRAM`. A required solution diagram whose question has a diagram
  has `derived_from` = the question diagram's media_id (same layout, same positions, new content in ANSWER green).
- A question with no given figure gets NO question diagram, even when the solution has one.
- Sibling consistency (B2): the same kind of answer in the same NCERT question set gets the same decision, or `reason` says why.
- Every number, label, count and position in `content` must come from the item, the LP solution/video, or the book page.
  Recompute every count and rule you state in `accuracy_checks`.
- A teaching image is never linked. If a figure you need is also a concept image, the item still gets its own diagram when it
  needs one (v3 prompt section 2, Step B2); only the 'refer picture' rule of Step B2 makes a question `optional` instead.

## Ids and placeholders (mechanical; the validator checks them)
- Question diagram (pair or single): `media_id` = `<question concept id>.IMG1`, `lp_placeholder_action` = `keep_and_replace_spec`,
  `placeholder` = `{"token": "{{DIAGRAM:<media_id>}}", "insert_into": "question_tex", "position": "after_question_text"}`.
- Solution diagram: pair -> `media_id` = `<answer concept id>.IMG1`; single -> `media_id` = `<concept id>.IMG2`. Action
  `keep_and_replace_spec`, `placeholder` = `{"token": ..., "insert_into": "steps_tex", "position": "before_first_step"}` ALWAYS.
- Worked-example diagram: `media_id` = `<concept id>.IMG<n>`, n = the lowest number NOT in `existing_concept_media_ids` of that
  unit and not used by another item of the same concept (blocks of one concept take n, n+1, ...), action `add_new_image`,
  `insert_into` `question_tex`, position `after_question_text`; the item also carries `"block_index": <unit block_index>`.
- `decision: none` -> pairs and singles: action `drop_image`; worked examples: `no_image`. `media_id` null; no `diagram`, no
  `placeholder`. Always `reason_codes` and a one-line `reason`; `text_alternative` where it helps.
- `decision: optional` -> action `drop_image` / `no_image`, no `diagram`, `reason` says which figure would help.
- `manim_description`: imperative, complete, exact values, left-to-right / top-to-bottom, colour tokens by name (BG INK MARK_FILL
  ANSWER FOCUS GUIDE SET_A SET_B CELL_FILL), explicit coordinates / counts / positions so that nothing is left to guess, and NONE of
  the words some / several / etc. / similar / a few / various. `visible_text`: every string drawn and nothing else (no "Q1", "Figure
  it Out", "Find", "Answer", "Table 2", headings). `must_not_show`: copy the list from the prompt's example, add specifics.
  `alt_text`: one sentence. Number style: the LP's own.
- `diagram.content` needs `"type": "<diagram_type>"` (same value as `diagram_type`) plus every value needed to draw it.
- Each required item also gets `"manim_scene"` (`c8_11_<section>_<item>_q` / `_sol`, any unique string).

## Output
Write ONE JSON file `HERE/map/out_<CHUNK>.json` in the shape of the v3 schema: `meta` (chapter "Exploring Some Geometric Themes",
class 8, textbook "Ganita Prakash Grade 8, Part 2, Chapter 4", lp_plan_id "cbse_eng_maths8_ch11_v31", prompt
"diagram_identification_prompt.md v3", placeholder_token_format "{{DIAGRAM:<media_id>}}", counts_by_role_and_decision matching
your items, notes), `style_tokens` (the table in prompt section 6), `figure_inventory`, `coverage_report` (`inventory_figures`,
`mapped_to_items`, `mapped_to_concept_images`, `mapped_none`, `unmapped: 0`, `new_media_ids_created` = the media_ids of your
required items, `lp_ids_dropped` = []), `items` (LP order, `none` ones included; a pair or single gives its question item then
its solution item). Write the JSON with a Python script kept OUTSIDE HERE (scratchpad or /tmp).

Then run, and fix until it prints `errors 0`:
`python3 -I -X utf8 HERE/validate_map.py HERE/map/out_<CHUNK>.json --chunk <CHUNK>`

Do not edit any other file, do not touch staging, do not upload anything. Your final message (short): counts (required /
optional / none per role), the required media ids with a few words each, inventory numbers, every judgement call you were unsure
about (item, what you chose, why), and anything in the LP that looks wrong (a solution that contradicts the book, a question
whose text is missing, a figure the LP text does not match).
