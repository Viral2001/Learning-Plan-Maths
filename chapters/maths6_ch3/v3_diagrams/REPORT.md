# Class 6 Ch 3 Number Play - V3 diagram run 2 (prompt v2) + supplied placement map, 21 Nov 2026

Source: live V2 `cbse_eng_maths6_ch3` v108 (still active, untouched, verified identical). Output: `out/cbse_eng_maths6_ch3_V3_v18.json` = chapter `cbse_eng_maths6_ch3_V3`, phase 3, version 18, master id 187. **UPLOADED to staging 21 Nov 2026 as ACTIVE v18, twice**: first (morning) replacing a stray draft v18, then (15:34) replaced IN PLACE with the placement map the user supplied (same version, no new version; v17 stays archived). Read back identical both times. Stamp skipped (phase 3), on the user's instruction.

## Update 15:34: the user's placement map (`ch3_number_play_diagram_map (1).json`, prompt v1)
The user supplied this file as "where the diagram placeholders go" and asked to update the current LP with it, same version. It is applied by `apply_supplied_map.py` (called from `build_v3.py merge`, on top of the v2 map; the v2 specs are kept because they are far more detailed than the v1 specs in the file). Differences between the file and the v2 result, all applied:
1. **Positions**: every one of the 17 solution tokens now sits at `steps_tex` / `before_first_step` (v2 had after_step_N or after_answer for 16 of them).
2. **C9** (3.1 Q3 question) is `optional` in the file -> no question diagram any more (v2 had one). C10 (its solution) now draws the whole line-up itself (derived_from null). Learners see the line-up from the teaching image of the previous topic; the question text itself lacks the numbers 0, 2, 1, 1, 0, 2, 1, 0 (`text_alternative` suggests a sentence).
3. **Pattern figures c, b, f, e** (worked examples C166, C167, C169, C170) are `required` in the file -> four new diagrams (v2 pointed them at the teaching images C165.IMG1 / C168.IMG1 / C168.IMG2, which carry a title banner and a logo). Their specs (not in the file at v2 detail) were written from book pages 13-14 and recomputed in code: c = 32 x 32 + 16 x 64 = 2048; b = 20 x 5 + 44 = 144; f = 31 coins, 7250, min gap 0.09; e = 22 each of 15, 25, 35 (1650), 7 hexagons + 6 rhombi tile the outer hexagon exactly.
Not in the file / not added: optional items C14, C30, C97, C173, C175, C210, C212 (and C9). The file also lists C101 and C130 as optional (C130 'arrow map', C101 'reuse the Kaprekar flow chart'): not added either.
Result on staging: 32 DIAGRAM nodes (11 question, 4 worked example, 17 solution), server message "added 4, removed 1 stable nodes". Backups: `source/cbse_eng_maths6_ch3_V3_v18_overwritten_backup_20261121_153422.json` (the 29-diagram v18), `out/cbse_eng_maths6_ch3_V3_v18_before_supplied_map.json`, `map/diagram_map_run2_before_supplied_map.json`.

## Update 16:47: the 3 spec files changed to v3, v18 re-uploaded (same version)
The user asked to modify the 3 spec files (`docs/karan-MD/diagram_identification_prompt (1).md`, `diagram_map.schema (1).json`, `Diagram trigger word — cross-standard companion note.md`) based on the change; edited IN PLACE (originals in `spec/originals_21nov/`, working copies in `spec/*_v3*`). The user's answers: (1) edit in place; (2) solution figure ALWAYS `steps_tex` / `before_first_step`; (3) NO reuse of teaching images anywhere; (4) C9-type question = optional + the question text must name the data. What changed:
- **Prompt (now v3):** v3 changelog line (Hinglish, like the v2 one), system prompt (placement + linking paragraph), section 2 (concept images never linked), Step 0 (`concept_image:` is accounting only), Step B2 (lettered figures drawn even if a teaching image shows them; new 'refer picture' bullet), Step C (`REUSES_CONCEPT_IMAGE` redefined), Step F (dedupe, no reuse), 'not a diagram' list, section 5 rule 1 (solution `derived_from: null` when the question has no diagram), section 8 sample (`prompt ... v3`), 8B (table row + field rules: solution token always the first line of the steps), self-check 8b/8c.
- **Schema:** `reuse_concept_image` and `reuse_media_id` removed; `placeholder` = question/worked `question_tex`+`after_question_text`, solution `steps_tex`+`before_first_step` only (enforced per role with if/then); `none` -> `drop_image|no_image`; `required` -> `keep_and_replace_spec|add_new_image`; `$comment` with the v3 note. Negative tests pass (after_step_N, answer_tex, reuse, wrong token field are all rejected).
- **Companion note:** two bullets added to the figure-content rule (solution figure first; teaching images never linked, with the 'refer picture' exception) and an 'updated' line. CRLF line endings kept.
- **Pipeline:** `validate_map.py`, `build_v3.py`, `apply_supplied_map.py`, `AGENT_BRIEF.md` follow v3 (no reuse code left; the builder asserts it). C81, C93, C94 are now plain 'no image' items (reason codes LATEX_ARITHMETIC / TEXT_SUFFICIENT as in the supplied map), C9 has `needs_lp_text_sync: true`.
- **v18 re-uploaded (same version, overwritten in place, active):** the ONLY change against the previous upload is that the three `image_media_id` links of the worked-example blocks C81, C93, C94 are gone (V2 never had them). The 32 diagrams, positions, everything else identical; "added 0, removed 0"; read back identical; V2 v108 untouched. Backups: `source/cbse_eng_maths6_ch3_V3_v18_overwritten_backup_20261121_164659.json`, `out/cbse_eng_maths6_ch3_V3_v18_before_v3_rules.json`, `map/diagram_map_before_v3_rules.json`.

Rules: `spec/diagram_identification_prompt_v3.md` and `spec/diagram_map.schema_v3.json` (copies of the edited files in docs/karan-MD; v2 originals in `spec/originals_21nov/`). Run 1 (prompt v1, uploaded as v17) is archived in `map/run1/`.

## What changed vs v108
- 149 old question/solution card placeholders removed.
- 32 diagram placeholders added (11 question, 4 worked example, 17 solution), titled `DIAGRAM · <label> question|solution figure`, image_role kept, full spec in `diagram_spec`, token `{{DIAGRAM:<id>}}` in the text.
- No block points at a teaching image (v3 rule; the 16:47 re-upload removed the three links C81, C93, C94 that v2 had added).
- Teaching images, videos, tools, text, objectives: unchanged. Image URLs reserved under `.../ch_3/diagram_v1/`; nothing rendered.

## Figure inventory (Step 0): 65 figures (63 from the page pictures + 2 found by the chunk agents), unmapped 0

## Decisions (173 items)
| role | required | optional | none |
|---|---|---|---|
| question | 11 | 1 | 60 |
| solution | 17 | 7 | 48 |
| worked_example | 4 | 0 | 25 |

## The 32 diagrams
| id | side | type | token goes into |
|---|---|---|---|
| M1.S3.T3.C10.IMG1 | solution | people_lineup | steps_tex / before_first_step |
| M1.S3.T3.C12.IMG1 | solution | people_lineup | steps_tex / before_first_step |
| M1.S3.T3.C16.IMG1 | solution | people_lineup | steps_tex / before_first_step |
| M1.S3.T3.C18.IMG1 | solution | people_lineup | steps_tex / before_first_step |
| M1.S5.T5.C23.IMG1 | question | cell_row | question_tex / after_question_text |
| M1.S5.T5.C24.IMG1 | solution | cell_row | steps_tex / before_first_step |
| M1.S5.T5.C25.IMG1 | question | cell_row | question_tex / after_question_text |
| M1.S5.T5.C26.IMG1 | solution | cell_row | steps_tex / before_first_step |
| M1.S5.T5.C28.IMG1 | solution | cell_row | steps_tex / before_first_step |
| M1.S5.T5.C36.IMG1 | solution | cell_row | steps_tex / before_first_step |
| M1.S5.T5.C38.IMG1 | solution | cell_row | steps_tex / before_first_step |
| M1.S5.T5.C41.IMG1 | question | cell_grid | question_tex / after_question_text |
| M1.S5.T5.C42.IMG1 | solution | cell_grid | steps_tex / before_first_step |
| M1.S6.T6.C43.IMG1 | question | cell_grid | question_tex / after_question_text |
| M1.S6.T6.C44.IMG1 | solution | cell_grid | steps_tex / before_first_step |
| M1.S8.T8.C48.IMG1 | question | number_line | question_tex / after_question_text |
| M1.S8.T8.C49.IMG1 | solution | number_line | steps_tex / before_first_step |
| M1.S9.T9.C50.IMG1 | question | number_line | question_tex / after_question_text |
| M1.S9.T9.C51.IMG1 | solution | number_line | steps_tex / before_first_step |
| M1.S9.T9.C52.IMG1 | question | number_line | question_tex / after_question_text |
| M1.S9.T9.C53.IMG1 | solution | number_line | steps_tex / before_first_step |
| M1.S9.T9.C54.IMG1 | question | number_line | question_tex / after_question_text |
| M1.S9.T9.C55.IMG1 | solution | number_line | steps_tex / before_first_step |
| M1.S9.T9.C56.IMG1 | question | number_line | question_tex / after_question_text |
| M1.S9.T9.C57.IMG1 | solution | number_line | steps_tex / before_first_step |
| M3.S27.T27.C166.IMG1 | worked example | cell_grid | question_tex / after_question_text |
| M3.S27.T27.C167.IMG1 | worked example | dice_grid | question_tex / after_question_text |
| M3.S27.T27.C169.IMG1 | worked example | ring_pattern | question_tex / after_question_text |
| M3.S27.T27.C170.IMG1 | worked example | tiling_pattern | question_tex / after_question_text |
| M3.S28.T28.C172.IMG1 | question | number_pattern | question_tex / after_question_text |
| M3.S28.T28.C174.IMG1 | question | dice_grid | question_tex / after_question_text |
| M3.S29.T29.C177.IMG1 | solution | number_pattern | steps_tex / before_first_step |

## Changes against run 1 (v17)
- New (audit misses): 3.1 Q3 question + solution figure (C9, C10), Q4 solution (C12), Q6 solution (C16); Q7 solution (C18) was already in.
- Dropped (audit false positives): Puzzle Time boxes (C88, C89, HEADER_BOXES_ONLY), Mental Math boards (C129, C131 NUMBER_LIST_IN_BOXES; C130 arrows, LaTeX expression already gives the answer).
- Pattern figures b, c, e, f (worked examples C167, C166, C170, C169): first (v2 morning) pointed at the same-topic teaching images; now drawn as their own diagrams, as the supplied placement map says (see the update above). Figures a and d are drawn as question figures (C172, C174) because their teaching images are in another topic.

## Optional (NOT added)

- `M1.S3.T3.C14` (solution): The book's printed answer redraws the Q4 line-up (1, 1, 1, 1, 0, the tallest child at the right end saying 0); it only repeats the Q4 solution picture, so v2 Step B2 gives optional. The figure that would help is the five-child lin
- `M1.S5.T5.C30` (solution): The printed answer is text and the LP steps give every position. A figure that would clearly help: rows of 2, 3, 4, 5, 6 and 7 cells with the 1st, 3rd, 5th and 7th cells shaded and the counts 1, 2, 2, 3, 3, 4. Not needed to follow
- `M2.S18.T18.C97` (solution): Optional, not added: a timeline 10:01 - 11:01 - 11:11 - 12:21 with gaps 60, 10, 70 and 70 minutes would help (the same picture is concept image M2.S17.T17.C92.IMG1 of another topic), but the printed answer is minutes in text and t
- `M3.S28.T28.C173` (solution): The LP solution is complete in text (12 forties: 12 x 40 = 480; 10 fifties: 10 x 50 = 500; 480 + 500 = 980) and the question figure is already on screen; the book prints no answer picture for 3.9. A figure that would help: the sam
- `M3.S28.T28.C175` (solution): The LP solution is complete in text (rows 3,4,4,4,3 = 18; four middle rows 4 x 18 = 72; row of threes 5 x 3 = 15; 18 + 18 + 72 + 15 = 123) and the question figure is already on screen; the book prints no answer picture for 3.9. A 
- `M4.S36.T36.C210` (solution): Optional, not added: a strip of the numbers 1 to 21 with 1, 5, 9, 13, 17, 21 highlighted and the '4 back' hops would help (concept image M4.S35.T35.C206.IMG1 is that picture, in another topic), but the answer is a number list that
- `M4.S37.T37.C212` (solution): Optional, not added: a strip of 0 to 22 with the safe numbers 2, 6, 10, 14, 18, 22 highlighted would help (concept image M4.S35.T35.C207.IMG1 shows it, in another topic), but the printed answer is only 'be the first player' and th

## Things in the LP text the diagrams depend on (not changed)
- `M1.S3.T3.C9` (3.1 Q3): question text lacks the first line's numbers 0, 2, 1, 1, 0, 2, 1, 0, and the question has no diagram of its own now (supplied map: optional); the teaching image M1.S2.T2.C2.IMG1 and the solution diagram C10 carry the line-up.
- `M1.S9.T9.C50` line a: no tick positions in the text (b, c, d have them).
- `M2.S15.T15.C88` Puzzle Time: question text has no clues now that no image carries the boxes; `M2.S11.T11.C63` lacks the digit-count table; `M4.S33.T33.C188` lacks the data 32, 29, 35; `M4.S34.T34.C200` lacks the map hint.
- `M3.S19.T19.C101` 'Start with 321.' states no routine or question; Mental Math items 'Make N.' (C116-C123, C125-C127, C129, C131) do not name the allowed numbers; 3.8 cards (C143...) drop 'write an example whenever possible'; always/sometimes/never items drop their three options; figures a and d (C172, C174) never say 'find the sum'.
- LP FiO7 text says the 25s are 'at the four corners'; the book (and the diagram C177) put them halfway between the 50s.
- `M4.S34.T34.C198/C199` (custard): LP says 'do not agree', book says possible; LP followed. `M4.S33.T33.C193` takes a mug as about 1 litre.
- LP Question numbering differs from the book's in several sets; items were matched by text.

## Upload
Phase 3 cannot go through `upload/upload_lp.py` (phase 2 only, needs a stamp). `upload_v3.py` reuses its `post()` and sends the same form fields; with an existing version of the same number it overwrites that version in place (force=true), never replace_all. A draft needs no flag; an ACTIVE version needs `--overwrite-active --expect <file>` (refuses when the live plan differs from the file uploaded before). Used on 21 Nov 2026 at the user's request.


## Images for the 32 diagrams (21 Nov 2026, user's request: "make images ... prefix DIAGRAM ... once done upload to V3 flow live plan"; redrawn the same evening as 16:9 house cards)
- Drawn in code from each node's own `diagram_spec` (Image-Pipeline-Maths `workspace/hand-specs/maths6_ch3_v3_diagrams/`: `render_diagrams.py`, `verify.py`, `kids.py`, `delivered_images.json`). **Final version = 16:9 house card, 1456 x 816**: the SINGULARITY logo top right, the faint centre watermark, the diagram enlarged to fill the card, no title banner (the user's choice); the spec's colour tokens, flat strokes and visible text; a question and its solution share one scale and position. The 4 line-ups (C10, C12, C16, C18) use 8 Gemini children (flat picture-book look) instead of stick figures. The figures are code-drawn (no Manim). PNGs: `png/` here and Image-Pipeline-Maths `generated images/NCERT/cbse_eng_maths6_ch3_V3_v18/`. (A first version on plain white at the nodes' own sizes was live for a short while: the user saw it in ContentValidator as "not like the other images", hence the card.)
- Checks: bubble = number of taller neighbours, supercells, every sum (2048, 144, 7250, 1650, 980, 123, 250), the counts (66 / 31 / 22 / 20) and the colour of every cell, pip, coin and dot are re-computed from the picture or the spec; the logo, the card, the watermark and the 16:9 size are checked; a solution redraws its question exactly (same transform, every INK pixel of the question is INK in the solution); printed words = `visible_text`; no overlapping or cut-off text.
- Uploaded to staging as ACTIVE **v18, in place** (no new version), twice: (1) image pass `--phase 3` (first version); (2) the 16:9 version: image pass `--phase 3 --image-folder diagram_v3`, then `upload_v3.py --overwrite-active` to set the nodes' `image_dimensions` (1456x816), `aspect_ratio` and `diagram_spec.aspect_ratio` (16:9) (88 field changes, user's OK; "added 0, removed 0", read back identical; backup in `source/`). Every `image_url` is `.../ch_3/diagram_v3/<id>.png` (`planned_url` unchanged: `diagram_v1`; the reserved folder was never written, because those urls had been in the live plan and the CDN caches a 404 for an hour); `build_status` is `built`, the PLACEHOLDER sentence is gone from `context`, `description` is rewritten from each picture. The 30 teaching images, the rest of every `diagram_spec` and the rest of the plan are unchanged (read back).
- **For the LP side (not changed here):** (a) the 4 line-up nodes' brief fields (`manim_description`, `must_not_show` "faces, clothes or hair", `negative_prompt`, `generation_prompt`, `diagram_spec.content`) still describe stick figures; (b) `render_source` still names a Manim code file that does not exist; (c) the prompt spec (`docs/karan-MD/diagram_identification_prompt (1).md` sections 4 and 6, and the schema) still says "aspect ratio by content, 4:1 to 5:1 for strips" and "no branding or watermarks on the picture"; the user chose to write the new diagram rule in the image pipeline only (Image-Pipeline-Maths CLAUDE.md "Diagram images rule" and the master prompt), so the next LP diagram map will contradict it until those lines are edited.
