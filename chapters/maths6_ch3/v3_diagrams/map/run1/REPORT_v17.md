# Class 6 Ch 3 Number Play - V3 diagram run (20 Nov 2026)

Source: live V2 `cbse_eng_maths6_ch3` v108 (active, untouched, verified identical to the saved copy). Output: `out/cbse_eng_maths6_ch3_V3_v17.json` (chapter `cbse_eng_maths6_ch3_V3`, phase 3, version 17, chapter_master_id 187). UPLOADED to staging 20 Nov 2026 as ACTIVE v17 (v16 archived), read back identical.

## What changed vs v108 (and nothing else)
- 149 old card placeholders removed (72 question + 77 solution; titles ended ': question' / ': solution'), with their ids in media_ids and the image_media_id / solution_image_media_id(s) fields.
- 30 diagram placeholders added: 14 question, 16 solution, 0 worked example. Each is titled `DIAGRAM · <label> given figure / solution figure`, keeps image_role, has the full spec in `diagram_spec` and `generation_prompt`, and a `{{DIAGRAM:<id>}}` token in question_tex / steps_tex / answer_tex and in text / publication_text.
- 30 teaching concept images, videos, tools, objectives, text: unchanged. `summary_stats.images` 179 -> 60, `diagram_placeholders` 30.
- New URLs reserved under `.../ch_3/diagram_v1/<id>.png`; nothing rendered yet (build_status placeholder).

## Decisions (173 items)
| role | required | optional | none |
|---|---|---|---|
| question | 14 | 1 | 57 |
| solution | 16 | 7 | 49 |
| worked_example | 0 | 0 | 29 |

## The 30 diagrams
| id | side | type | where the token goes |
|---|---|---|---|
| M1.S3.T3.C18.IMG1 | solution | people_lineup | steps_tex / after_step_3 |
| M1.S5.T5.C23.IMG1 | question | cell_row | question_tex / after_question_text |
| M1.S5.T5.C24.IMG1 | solution | cell_row | steps_tex / before_first_step |
| M1.S5.T5.C25.IMG1 | question | cell_row | question_tex / after_question_text |
| M1.S5.T5.C26.IMG1 | solution | cell_row | steps_tex / before_first_step |
| M1.S5.T5.C28.IMG1 | solution | cell_row | steps_tex / after_step_2 |
| M1.S5.T5.C36.IMG1 | solution | cell_row | steps_tex / after_step_2 |
| M1.S5.T5.C38.IMG1 | solution | cell_row | steps_tex / after_step_3 |
| M1.S5.T5.C41.IMG1 | question | cell_grid | question_tex / after_question_text |
| M1.S5.T5.C42.IMG1 | solution | cell_grid | steps_tex / after_step_3 |
| M1.S6.T6.C43.IMG1 | question | cell_grid | question_tex / after_question_text |
| M1.S6.T6.C44.IMG1 | solution | cell_grid | steps_tex / before_first_step |
| M1.S8.T8.C48.IMG1 | question | number_line | question_tex / after_question_text |
| M1.S8.T8.C49.IMG1 | solution | number_line | steps_tex / before_first_step |
| M1.S9.T9.C50.IMG1 | question | number_line | question_tex / after_question_text |
| M1.S9.T9.C51.IMG1 | solution | number_line | steps_tex / after_step_4 |
| M1.S9.T9.C52.IMG1 | question | number_line | question_tex / after_question_text |
| M1.S9.T9.C53.IMG1 | solution | number_line | steps_tex / after_step_3 |
| M1.S9.T9.C54.IMG1 | question | number_line | question_tex / after_question_text |
| M1.S9.T9.C55.IMG1 | solution | number_line | steps_tex / after_step_2 |
| M1.S9.T9.C56.IMG1 | question | number_line | question_tex / after_question_text |
| M1.S9.T9.C57.IMG1 | solution | number_line | steps_tex / after_step_2 |
| M2.S15.T15.C88.IMG1 | question | cell_row | question_tex / after_question_text |
| M2.S15.T15.C89.IMG1 | solution | cell_row | steps_tex / after_step_4 |
| M3.S23.T23.C129.IMG1 | question | arrow_map | question_tex / after_question_text |
| M3.S23.T23.C130.IMG1 | solution | arrow_map | steps_tex / before_first_step |
| M3.S23.T23.C131.IMG1 | question | cell_grid | question_tex / after_question_text |
| M3.S28.T28.C172.IMG1 | question | number_pattern | question_tex / after_question_text |
| M3.S28.T28.C174.IMG1 | question | dice_grid | question_tex / after_question_text |
| M3.S29.T29.C177.IMG1 | solution | number_pattern | steps_tex / after_step_3 |

## Optional (NOT added; say if you want any)

- `M1.S3.T3.C10` (solution): Would clearly help but is not needed: the LP solution already writes the first line 0, 2, 1, 1, 0, 2, 1, 0 in text and names the 3rd and 4th children. Helpful figure: that row of eight children (relative heights as on book page 55) with the 3rd and 4th speech bubbles, both 1, circled.
- `M1.S3.T3.C12` (solution): Would help but is not needed: the answer is the order 'shortest to tallest' with 1, 1, 1, 1, 0, fully stated in the LP text; the LP gives no heights. Helpful figure: five children rising in height left to right with bubbles 1, 1, 1, 1, 0 (book solutions page 20 draws it).
- `M1.S3.T3.C16` (solution): Would help but is not needed: the LP solution gives the example heights 150, 140, 120, 135, 145 in text and a student can check each neighbour pair from the numbers. Helpful figure: five children with those heights and bubbles 0, 1, 2, 1, 0 (book solutions page 21 draws it).
- `M1.S5.T5.C30` (solution): Would help but is not needed: the LP steps give the supercell positions for each row length in words (1st, 3rd, 5th, 7th) and the answer 1, 2, 2, 3, 3, 4 in text. Helpful figure: six rows of 2, 3, 4, 5, 6, 7 empty cells with cells 1, 3, 5, 7 shaded (the concept image M1.S4.T4.C20.IMG1 shows this, but it is in another topic, so it cannot be reused here).
- `M1.S5.T5.C40` (solution): Open-ended sample answer, not needed: the LP text states the puzzle and the sample row 120, 450, 130, 380, 210, 560, 300 in words. Helpful figure: that row of seven cells with cells 2, 4, 6 shaded.
- `M3.S20.T20.C101` (question): The book question is plain text (carry out the same steps with a 3-digit number); it has no given figure. A small flow of the routine (largest A, smallest B, C = A - B, repeat with the digits of C) for 3 digits would help only because the LP text does not state the steps; better to put the steps in the question text. Not added (near-copy of concept image M3.S19.T19.C98.IMG1, which is in another topic).
- `M3.S28.T28.C173` (solution): The five LP steps (12 forties, 480; 10 fifties, 500; 980) are complete in text. A figure that would help but is not needed: the question figure with the twelve 40 boxes in SET_A and the ten 50 boxes in SET_B, with counts 12 x 40 and 10 x 50; not added in this run.
- `M3.S28.T28.C175` (solution): The four LP steps (18 per row, 4 x 18 = 72, 5 x 3 = 15, 123) are complete in text. A figure that would help but is not needed: the question grid with each row total written beside its row (18, 18, 18, 18, 18, 15, 18) in ANSWER; not added in this run.

## Things in the LP the diagrams depend on (not changed)
- `M2.S15.T15.C88` Puzzle Time question text has no clues; they are only in an old hint field. Diagram carries the place boxes only. Flagged `needs_lp_text_sync`.
- `M3.S23.T23.C129` / `C131` (Make 28,000 / 45,000): question text does not name the boxes or the rule; the figures carry the boxes only.
- `M3.S19.T19.C101` (Start with 321) states no routine and no question; the LP text needs it.
- `M1.S6.T6.C43` question text does not contain Table 2 or the digits 1, 0, 6, 3, 9; they are only in the figure.
- `M4.S34.T34.C198/C199` (Roshan's custard): the LP says 'do not agree', the book's printed answer says it is possible; LP followed.
- `M4.S33.T33.C193` takes a mug as about 1 litre.
- Lines b, c, d (`M1.S9.T9.C52/C54/C56`) never say 'label the remaining ticks'; book also asks to circle the smallest and box the largest label, the LP does not.
- C18 figure labels heights '150 cm'; LP answer text gives the numbers without cm.

## Judgement calls the agents flagged
- Reuse of a concept image is only allowed inside the same topic, so figures that look like a concept image in an earlier topic (C172/C174 vs C165/C168, C129/C131 vs C115/C124, C18, C28, C44, C49) got new diagrams. Promote to reuse if you prefer.
- Worked examples: all 29 decided none (22 reuse an existing concept image in the same topic, 7 need no picture: text/LaTeX).
- Token position for solutions: inside the step string (after_step_n / before_first_step) so the step count and numbering do not change.

## Upload (done)
Uploaded with the user's OK, stamp skipped, by a direct POST of `upload_lp.post()` to `/agentapi/api/lp2/learning-plans/upload?activate=true` (chapter_master_id 187, phase 3): http 200, no validation errors, 213 concepts, 194 media. Read back from staging: identical to out/cbse_eng_maths6_ch3_V3_v17.json; V2 v108 still active and identical. Before that: `upload/upload_lp.py` refuses phase 3 and any plan without a `validate_local.py` stamp (phase 2 only), so this plan cannot go through it. A direct POST to the same endpoint with phase=3 is needed; that needs your OK. Gates of the phase 2 pipeline (solution_content: every question has a question card and a solution card) would fail on this plan by design.
