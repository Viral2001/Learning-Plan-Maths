> **v3 update, 21 Nov 2026.** The rules in `spec/` are now v3 (the user's files, edited in place in docs/karan-MD; originals in
> `spec/originals_21nov/`). Where this brief says otherwise, v3 wins: a solution diagram is ALWAYS `steps_tex` / `before_first_step`
> (no `after_step_<n>`, no `answer_tex`); a teaching image is NEVER linked (no `reuse_concept_image`, no `reuse_media_id`; `decision: none`
> -> `drop_image` for a pair, `no_image` for a worked example); a lettered figure is drawn even when a same-topic teaching image shows it;
> a 'refer picture' question whose picture is a teaching image of an earlier topic is `optional` with `text_alternative` + `needs_lp_text_sync`
> (Step B2). The chunk outputs `map/out_A..D.json` are the v2 run; `apply_supplied_map.py` converts them to v3 at merge time.

# Brief (v2 rules): diagram decisions for one chunk of Class 6 Ch 3 "Number Play"

You decide, for every question, solution and worked example in ONE chunk of the live plan, whether it needs a
diagram image, you write the full diagram spec for each one that does, and you account for every NCERT figure that
belongs to your chunk. You change nothing else.

All paths are under `/root/maths-learning-plan/Learning-Plan-Maths/chapters/maths6_ch3/v3_diagrams/` (call it HERE).

## Read first (in this order)
1. `HERE/spec/diagram_identification_prompt_v3.md` - the rules (v2). EVERY section is binding: Step 0 inventory, Step B2
   (printed answer is a picture, lettered figures, sibling consistency), Step C (incl. the new codes `HEADER_BOXES_ONLY` and
   `NUMBER_LIST_IN_BOXES`), the "Not a diagram" list, sections 4 to 7 and section 9 (self-check). Its section 8B
   (writing into the LP) is done by a builder script, not by you: you only produce the map of section 8. The header of
   the file says what the audit of the first run found: 7 needed diagrams were missed (the three picture answers of the
   3.1 line-ups, and the lettered pattern figures b, c, e, f of 3.9) and 4 unneeded ones were made (place-value header
   boxes, boxes of mental-math numbers). Do not repeat either kind of mistake.
2. `HERE/spec/companion_note.md` - the figure-content rule: a question's figure shows ONLY what the question gives; a
   solution's figure shows the COMPLETE final state; no question figure when the question gives none; labels consistent.
3. `HERE/spec/diagram_map.schema_v3.json` - the output schema (figure_inventory and coverage_report are required).
4. Your chunk file `HERE/map/in_<CHUNK>.json` (units in LP order).
5. The book: `HERE/book/chapter_text.md` (text of each pdf page) and the page pictures `HERE/book/page_NN.png` (NN = pdf page
   01..32). Chapter pages 1-19, printed solutions 20-32. LOOK at the picture of every page your items use, solutions
   pages included: figures are often only in the pictures.
6. The base figure inventory (Step 0, built by two other agents from the page pictures): `HERE/map/inv_base_chapter.json`
   and `HERE/map/inv_base_solutions.json`. Each entry has fig_id, page, section, belongs_to, kind, description.
7. `HERE/map/concept_images.json` - the 30 teaching (concept) images that already exist in the plan.
8. DO NOT read `HERE/map/run1/` (the first run's decisions): decide afresh from the v2 rules.

## What a unit is (the chunk file)
- `kind: "pair"`: a question concept (`question_concept`) and its answer concept (`answer_concept`). They become TWO items
  in your output: role `question` (lp_concept_id = the question concept id) and role `solution` (lp_concept_id = the
  answer concept id). Decide the two sides separately (Step E).
- `kind: "worked"`: a worked example inside a teaching concept (question + steps + answer in one block). ONE item, role
  `worked_example`, lp_concept_id = the concept id. Its single diagram is the picture the example needs.
- `item` fields: `question`/`question_tex` (what the student sees), `steps`/`steps_tex` and `answer`/`answer_tex`
  (the LP solution), `q_figure` / `s_figure` (a sentence an earlier author wrote about the figure: a HINT only, often
  wrong or thin), `book_number`, `ncert_refs`. The LP's own numbering in `book_number`/`ncert_refs` can differ from the
  book's: find the item in the book by its text.
- There are NO old image ids to go by: the old question/solution cards are being deleted, and a missing id never means
  "no diagram". Judge every item with the rules, exactly as v2 says.
- The solution text is in the LP; if the LP and the book's printed answer disagree, FOLLOW THE LP (note it).

## Step 0 for your chunk (mandatory, and checked by a script)
For every base-inventory figure that belongs to your chunk, write one `figure_inventory` entry with the SAME `fig_id`
and exactly one `mapped_to`:
- `item:<concept_id> (question)` or `item:<concept_id> (solution)` - it becomes that item's diagram (a worked-example
  item is written `(question)`); the item you name must be `required` in your `items`;
- `concept_image:<media_id>` - a teaching figure already in `concept_images.json` (same topic as the item that would
  otherwise need it);
- `none:<REASON_CODE>` - with a code from Step C (e.g. LATEX_TABLE, DECORATIVE_ONLY, SAME_AS_QUESTION_DIAGRAM,
  HEADER_BOXES_ONLY, NUMBER_LIST_IN_BOXES, REUSES_CONCEPT_IMAGE).
A figure belongs to your chunk if it is in the book section of one of your units, OR one of your units' question/answer
uses it. Another chunk may claim the same figure for its own item; duplicates are compared at merge, so keep your reason
sound. Check each base description against the page picture; if it is wrong, say so in your entry's `description` (start
with "CORRECTED:") and use the right facts. A figure you find that is missing from the base gets a fig_id starting `NEW-`.
`coverage_report.unmapped` must be 0, and the counts in it must equal the entries you wrote.
Two figures that are the same picture used by two items are two entries (one per use) with different mapped_to.

## Decision rules specific to this run
- Only `required` diagrams are added to the plan. `optional` = a figure that would clearly help but is not needed: it is
  NOT added (action `drop_image` / `no_image`), the reason says what figure would help. Prefer `none` unless a v2 rule
  or the tie-breaker says the picture matters. Text and LaTeX are the default.
- Reuse of a teaching image (`reuse_concept_image`, decision `none`) is allowed ONLY when that concept image is in the SAME
  topic as the item (a block can only point at media of its own topic; the check script enforces it) and it really shows
  the figure. If the figure exists only as a concept image of ANOTHER topic, the item needs its own diagram (required,
  and say "duplicates concept image <id>" in `reason`), exactly as v2 Step B2 demands for lettered figures and picture answers.
- Question side `required` only if the student needs the figure to ATTEMPT it. Solution side `required` only if the
  solution adds something visual or the printed/LP answer IS a picture/arrangement (B2); if it would only repeat the question
  figure, `none` with `SAME_AS_QUESTION_DIAGRAM`. A required solution diagram whose question has a diagram has
  `derived_from` = the question diagram's media_id (same layout, same positions, new content in ANSWER green).
- A question with no given figure gets NO question diagram, even when the solution has one.
- Sibling consistency (B2): the same kind of answer in the same NCERT question set gets the same decision, or `reason` says why.
- Every number, label and position in `content` must come from the item, the LP solution, or the book page. Recompute every
  sum, count and rule you state in `accuracy_checks`.

## Ids and placeholders (mechanical; the validator checks them)
- Question diagram: `media_id` = `<question concept id>.IMG1`, `lp_placeholder_action` = `keep_and_replace_spec`,
  `placeholder` = `{"token": "{{DIAGRAM:<media_id>}}", "insert_into": "question_tex", "position": "after_question_text"}`.
- Solution diagram: `media_id` = `<answer concept id>.IMG1` (ONE solution diagram per answer concept, always `.IMG1`),
  action `keep_and_replace_spec`, `insert_into` = `steps_tex` with position `before_first_step` | `after_step_<n>` (n = 1-based
  number of an existing step of that solution) or `answer_tex` with position `after_answer`. Pick where the picture is first needed.
- Worked-example diagram: `media_id` = `<concept id>.IMG<n>`, n = the lowest number NOT in `existing_concept_media_ids` of
  that unit, action `add_new_image`, `insert_into` `question_tex`, position `after_question_text`.
- `decision: none` -> pairs: action `drop_image` (or `reuse_concept_image` + `reuse_media_id`); worked examples: `no_image`
  (or `reuse_concept_image`). `media_id` null; no `diagram`, no `placeholder`. Always `reason_codes` and a one-line `reason`;
  `text_alternative` where it helps.
- `decision: optional` -> action `drop_image` / `no_image`, no `diagram`, `reason` says which figure would help.
- `manim_description`: imperative, complete, exact values, left-to-right / top-to-bottom, colour tokens by name (BG INK
  MARK_FILL ANSWER FOCUS GUIDE SET_A SET_B CELL_FILL), and NONE of the words some / several / etc. / similar / a few /
  various. `visible_text`: every string drawn and nothing else (no "Q1", "Figure it Out", "Find", "Answer", "Table 2",
  headings). `must_not_show`: copy the list from the prompt's example, add specifics. `alt_text`: one sentence.
  Number style: the LP's own (it matches the LP solution text).
- `diagram.content` needs `"type": "<diagram_type>"` (same value as `diagram_type`) plus every value needed to draw it.
- Each required item also gets `"manim_scene"` (`c3_<section>_<item>_q` / `_sol`, any unique string).

## Output
Write ONE JSON file `HERE/map/out_<CHUNK>.json` in the shape of the v2 schema: `meta` (chapter "Number Play", class 6,
textbook "Ganita Prakash Grade 6, Chapter 3", lp_plan_id "cbse_eng_maths6_ch3_v108", prompt
"diagram_identification_prompt.md v2", placeholder_token_format "{{DIAGRAM:<media_id>}}", counts_by_role_and_decision
matching your items, notes), `style_tokens` (the table in prompt section 6), `figure_inventory`, `coverage_report`
(`inventory_figures`, `mapped_to_items`, `mapped_to_concept_images`, `mapped_none`, `unmapped: 0`, `new_media_ids_created`
= the media_ids of your required items, `lp_ids_dropped` = []), `items` (LP order, `none` ones included; a pair gives its
question item then its solution item). Write the JSON with a Python script kept OUTSIDE HERE (scratchpad or /tmp).

Then run, and fix until it prints `errors 0`:
`python3 -I -X utf8 HERE/validate_map.py HERE/map/out_<CHUNK>.json --chunk <CHUNK>`

Do not edit any other file, do not touch staging, do not upload anything. Your final message (short): counts
(required / optional / none per role), the required media ids with a few words each, inventory numbers, every judgement call
you were unsure about (item, what you chose, why), and anything in the LP that looks wrong (a solution that contradicts the
book, a question text that lacks what only the figure carries, a figure the LP text does not match).
