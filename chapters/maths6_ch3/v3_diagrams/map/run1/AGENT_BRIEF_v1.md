# Brief: diagram decisions for one chunk of Class 6 Ch 3 "Number Play"

You decide, for every question, solution and worked example in ONE chunk of the live plan, whether it needs a
diagram image, and you write the full diagram spec for each one that does. You change nothing else.

All paths are under `/root/maths-learning-plan/Learning-Plan-Maths/`.

## Read first (in this order)
1. `docs/karan-MD/diagram_identification_prompt.md` - the rules. Sections 3 (decision procedure), 4 (what may be in
   an image), 5 (question vs solution), 6 (style tokens), 7 (diagram types) and 8 (output format) are binding.
   Ignore its section 1 "system prompt" wording about "Learning Plan items"; the unit shapes are described below.
2. `docs/karan-MD/Diagram trigger word — cross-standard companion note.md` - the figure-content rule: a question's
   figure shows ONLY what the question gives; a solution's figure shows the COMPLETE final state; if the question has no
   given figure do not invent one; labels stay the same between the two.
3. `docs/karan-MD/diagram_map.schema.json` - the output schema.
4. Your chunk file `chapters/maths6_ch3/v3_diagrams/map/in_<CHUNK>.json` (units in LP order).
5. The book: `chapters/maths6_ch3/v3_diagrams/book/chapter_text.md` (text of each pdf page, `<!-- pdf page N -->`
   markers, the printed answers start at "CHAPTER 3 - SOLUTIONS") and the page pictures
   `chapters/maths6_ch3/v3_diagrams/book/page_NN.png` (NN = pdf page, 01..32). LOOK at the page picture of every item
   you judge: the figure is often only in the picture, not in the text. The solutions pages are in the pictures too.
6. `chapters/maths6_ch3/v3_diagrams/map/concept_images.json` - the 30 teaching (concept) images that already exist
   in the plan. If one of them already shows the figure an item needs, do not add a near-copy: decide `none` with
   reason code `REUSES_CONCEPT_IMAGE`, action `reuse_concept_image`, `reuse_media_id` = that id (same topic only).

## What a unit is (the chunk file)
- `kind: "pair"`: a question concept (`question_concept`) and its answer concept (`answer_concept`). They become TWO items
  in your output: role `question` (lp_concept_id = the question concept id) and role `solution` (lp_concept_id = the
  answer concept id). Decide the two sides separately (prompt section 3, step E).
- `kind: "worked"`: a worked example inside a teaching concept (question + steps + answer in one block). ONE item, role
  `worked_example`, lp_concept_id = the concept id. A worked example is shown as one block, so the single diagram is
  the picture the example needs (a given figure, or the picture of its working, whichever the example is about).
  If the existing concept images of that topic (`concept_images.json`) already show it: reuse, do not add.
- `item` fields: `question`/`question_tex` (what the student sees), `steps`/`steps_tex` and `answer`/`answer_tex`
  (the LP solution), `q_figure` / `s_figure` (a sentence a previous author wrote about the figure: a HINT only, it
  is often wrong or too thin; the book page and the prompt's rules decide), `book_number`, `ncert_refs`.
- The solution text is in the LP; if the LP and the book's printed answer disagree, FOLLOW THE LP.
- Old placeholder cards (question card / solution card) are being deleted; they are not your concern. Do not describe
  a card, the question text or the steps in a diagram.

## Decision rules specific to this run
- Only `required` diagrams are added to the plan. Use `optional` ONLY for a figure that would clearly help but is not
  needed; those are NOT added (action `drop_image` / `no_image`), they are just listed for the reviewer. Be strict:
  prefer `none` unless the tie-breaker in section 3 says the picture changes how easily or how correctly the student
  solves it. Text and LaTeX are the default (a table of numbers, column arithmetic, a list, a sequence is `none`).
- This chapter is whole-number play. Real figures in it: rows of boxes/cells with shaded supercells, number lines with
  ticks, dot/dice grids, magic-square-like grids, arrow boards ("Mental Math" middle numbers and side targets), number
  patterns in shapes (the "Figure a-f" patterns), clock faces and calendars, line-ups of children by height.
  Do NOT invent a figure the book does not have; do NOT draw decorative clip-art, children or faces.
- Question side `required` only if the student needs the figure to ATTEMPT it. Solution side `required` only if the
  solution adds something visual (filled cells, marks, a drawn arrow board, a coloured part). If it would only repeat
  the question figure, decide `none` with `SAME_AS_QUESTION_DIAGRAM`. If the question has a diagram, a required
  solution diagram has `derived_from` = the question diagram's media_id (same layout, same positions, new content in
  ANSWER green).
- A question with no given figure gets NO question diagram, even when the solution has one.
- "Complete the table / fill the blanks" with a plain table: `none` (`LATEX_TABLE`). Say what to write in `text_alternative`.
- Every number, label and position in `content` must come from the item, the LP solution, or the book page. Recompute
  every sum, count and rule you state in `accuracy_checks`.

## Ids and placeholders (mechanical; the validator checks them)
- Question diagram: `media_id` = `<question concept id>.IMG1`, `lp_placeholder_action` = `keep_and_replace_spec`,
  `placeholder` = `{"token": "{{DIAGRAM:<media_id>}}", "insert_into": "question_tex", "position": "after_question_text"}`.
- Solution diagram: `media_id` = `<answer concept id>.IMG1` (a second, different figure `.IMG2`; avoid two unless one picture
  would be overcrowded), action `keep_and_replace_spec`, `insert_into` = `steps_tex` with position
  `before_first_step` | `after_step_<n>` (n = 1-based number of an existing step of that solution) or `answer_tex` with
  position `after_answer`. Pick the place where the picture is first needed.
- Worked example diagram: `media_id` = `<concept id>.IMG<n>` where n is the lowest number NOT already used by
  `existing_concept_media_ids` of that unit (IMG1 is often taken by a concept image), action `add_new_image`,
  `insert_into` `question_tex`, position `after_question_text`.
- `decision: none` -> pairs: action `drop_image` (or `reuse_concept_image`); worked examples: `no_image` (or
  `reuse_concept_image`). `media_id` may be null; no `diagram`, no `placeholder`. Always give `reason_codes` and a
  one-line `reason`; `text_alternative` where it helps.
- `decision: optional` -> action `drop_image` / `no_image`, no `diagram`, but say in `reason` what figure would help
  (the reviewer may add it later).
- `manim_description` must be imperative, complete, exact values, left-to-right / top-to-bottom, colour tokens by name
  (BG INK MARK_FILL ANSWER FOCUS GUIDE SET_A SET_B CELL_FILL), and must NOT contain the words some / several / etc. /
  similar / a few / various. `visible_text` lists every string drawn and nothing else (no "Q1", "Figure it Out",
  "Find", "Answer", "Table 2", headings). `must_not_show`: copy the list from the prompt's example. `alt_text`: one sentence.
  Keep the book's number style (`15,077`, `1,00,000`; the LP's own style where the item uses another).
- `diagram.content` needs `"type": "<diagram_type>"` (same value as `diagram_type`) plus every value needed to draw it.
  `aspect_ratio` like `16:9`, `4:1`, `4:3`, `1:1`.
- Also give each required item `"manim_scene"`: `c3_<n>_<short>_q` for a question, `..._sol` for a solution (any unique string).
- Do not invent fields outside the schema except `block_index` is not needed.

## Output
Write ONE JSON file: `chapters/maths6_ch3/v3_diagrams/map/out_<CHUNK>.json`, in the shape of the schema:
`meta` (chapter "Number Play", class 6, textbook "Ganita Prakash Grade 6, Chapter 3", lp_plan_id
"cbse_eng_maths6_ch3_v108", prompt "diagram_identification_prompt.md v1", placeholder_token_format
"{{DIAGRAM:<media_id>}}", counts_by_role_and_decision matching your items, notes), `style_tokens` (the table in prompt
section 6), `items` (one per item, LP order, including the `none` ones: a pair gives its question item then its
solution item). Write the JSON with a Python script (not by hand) so quoting is right; keep the script in the scratchpad
or delete it afterwards, do not leave it in the plan folder.

Then run, and fix until it prints `errors 0`:
`python3 -I -X utf8 chapters/maths6_ch3/v3_diagrams/validate_map.py chapters/maths6_ch3/v3_diagrams/map/out_<CHUNK>.json --chunk <CHUNK>`

Do not edit any other file, do not touch staging, do not upload anything. Your final message: counts
(required / optional / none per role), the list of required media ids with a few words each, every judgement call you
were unsure about (item, what you chose, why) and anything in the LP that looks wrong (a solution that contradicts the
book, a figure the LP text does not match). Keep it short.
