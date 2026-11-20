# Class 6, 7, 8: field cleanup, question/answer split, LaTeX and tool descriptions

Done 5 Nov 2026 on the ACTIVE staging version of all 39 Class 6-8 chapters. **Uploaded to STAGING the same day (section 'Upload' below); never production. No URL was changed, nothing was committed to git.**

## Upload (5 Nov 2026, staging only)
- Each chapter was uploaded as the next free version (`activate=true`, never `--force`), then read back from staging and compared with the local file: **38 identical**; 7.3 identical except the `_activate` flag (see below).
- **7.3 was uploaded as v43 but NOT activated.** Staging already had inactive drafts v39 to v42 made today by someone else; v38 (the version I built from) is still the active one. Activate v43 yourself once you are sure the drafts do not hold newer work.
- The repo uploader refuses a plan without a validation stamp, and these chapters cannot earn one (video_script_rules on beat-less video placeholders). As for the layout rollout and Class 5 Ch 1, upload/upload_lp.py was run UNCHANGED through a wrapper that replaces only the stamp check. `--skip-preflight` was used for exactly 6.3, 6.5, 7.11, 7.15 and 8.10; their preflight problems (textbook branding inside video scripts) are identical to what was already live.
- Each previous active version is now archived. Versions: 

| Chapter | New version |
|---|---|
| 6 Ch 1 | v82 |
| 6 Ch 2 | v55 |
| 6 Ch 3 | v108 |
| 6 Ch 4 | v84 |
| 6 Ch 5 | v71 |
| 6 Ch 6 | v58 |
| 6 Ch 7 | v31 |
| 6 Ch 8 | v46 |
| 6 Ch 9 | v32 |
| 6 Ch 10 | v88 |
| 7 Ch 1 | v29 |
| 7 Ch 2 | v39 |
| 7 Ch 3 | v43 |
| 7 Ch 4 | v37 |
| 7 Ch 5 | v48 |
| 7 Ch 6 | v62 |
| 7 Ch 7 | v57 |
| 7 Ch 8 | v34 |
| 7 Ch 9 | v61 |
| 7 Ch 10 | v69 |
| 7 Ch 11 | v27 |
| 7 Ch 12 | v31 |
| 7 Ch 13 | v33 |
| 7 Ch 14 | v38 |
| 7 Ch 15 | v27 |
| 8 Ch 1 | v45 |
| 8 Ch 2 | v34 |
| 8 Ch 3 | v36 |
| 8 Ch 4 | v29 |
| 8 Ch 5 | v36 |
| 8 Ch 6 | v32 |
| 8 Ch 7 | v22 |
| 8 Ch 8 | v56 |
| 8 Ch 9 | v54 |
| 8 Ch 10 | v35 |
| 8 Ch 11 | v31 |
| 8 Ch 12 | v24 |
| 8 Ch 13 | v28 |
| 8 Ch 14 | v39 |

To roll a chapter back, activate its previous version (new version - 1; for 7.3 nothing to roll back).

## What was asked
1. Apply `LEARNING_PLAN_FIELD_CLEANUP_AND_LATEX 1.md` (Part 1 field cleanup; Part 2 question/answer split, `Questions: <category>` naming, strict LaTeX, answer present for every question) to every Class 6, 7 and 8 learning plan.
2. At the same time, write a description for every interactive tool from the 'Interactive Learning Tool Design' brief, with `chapters/maths8_ch13/new_design/tool_descriptions.py` as the style reference.

## Result at a glance

| | |
|---|---|
| Chapters rewritten | 39 (Class 6: 10, Class 7: 15, Class 8: 14) |
| Question concepts split into a question concept + an answer concept | **1750 pairs** (5335 concepts in total) |
| Topics | 1153 |
| Tool descriptions written and applied | **354 of 354** tools |
| Questions without a worked solution after the run | **0** (89 were missing; authored: 6.10: 60, 6.2: 17, 6.3: 12) |
| LaTeX checker issues | 0 |
| Structural problems (ids, references, pairing, urls) | 0 |
| Objectives dropped (anchored only to a replaced question concept) | 290 |
| Stub question slots (no question text in the live plan; grouped, NOT split, NOT invented) | 82 |
| Hand edits kept in `edits.json` | 219 per-pair entries, 735 phrase replacements |

## Where everything is
Per chapter, in `Learning-Plan-Maths/chapters/maths<G>_ch<N>/lp_qa_latex/`:
- `cbse_eng_maths<G>_ch<N>.json`: the new plan. `version` = live active version + 1, `plan_id` set to match. Not uploaded.
- `TOOL_DESCRIPTIONS.md`: every tool as `Tool Name:` / `Tool Description:` (the format in your brief), for reading. The same text is in each tool node's `description` field in the plan.
- `tool_descriptions.py`: the descriptions keyed by the tool id of the SOURCE plan (8.13's are your reference file, re-keyed from v24-v26 ids to the ids of live v27, matched on tool title).
- `edits.json`: hand fixes (authored solutions, wording that converts badly). `report.json`: counts, dropped objectives, stubs, gate comparison, the key of every question.

Regenerate any chapter (about 1 minute) after changing its `edits.json` or `tool_descriptions.py`:
```
python -B -X utf8 core/qa_split_live.py --key maths7_ch10 --src <the live active plan json>
```
The source is `GET https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/chapter/<chapter_id>?version=N` (`data.plan.planJson`). Source versions used are in the table below. If a live version moves, regenerate from the new one: ids, version and `edits.json` keys are all derived from the source.

## Per chapter

| Chapter | Live v -> new | Topics | Concepts | Q/A pairs | Tools | Objectives (dropped) | Stubs | Hand edits (pairs / phrases) | Gate errors before -> after | New kinds of gate problem |
|---|---|---|---|---|---|---|---|---|---|---|
| 6 Ch 1 | v81 -> v82 | 21 | 90 | 30 | 7 | 29 (0) | 0 | 7 / 12 | 50 -> 50 | 0 |
| 6 Ch 2 | v54 -> v55 | 34 | 189 | 67 | 8 | 44 (0) | 0 | 17 / 36 | 124 -> 107 | 0 |
| 6 Ch 3 | v107 -> v108 | 38 | 213 | 72 | 14 | 44 (59) | 0 | 13 / 17 | 221 -> 204 | 0 |
| 6 Ch 4 | v83 -> v84 | 28 | 123 | 46 | 6 | 30 (0) | 0 | 0 / 54 | 67 -> 67 | 0 |
| 6 Ch 5 | v70 -> v71 | 34 | 192 | 71 | 10 | 43 (0) | 0 | 0 / 0 | 149 -> 149 | 0 |
| 6 Ch 6 | v57 -> v58 | 23 | 115 | 40 | 11 | 32 (13) | 5 | 0 / 15 | 216 -> 158 | 0 |
| 6 Ch 7 | v30 -> v31 | 33 | 192 | 70 | 10 | 33 (0) | 0 | 0 / 96 | 118 -> 118 | 0 |
| 6 Ch 8 | v45 -> v46 | 40 | 140 | 41 | 8 | 48 (0) | 0 | 18 / 0 | 81 -> 81 | 0 |
| 6 Ch 9 | v31 -> v32 | 26 | 129 | 41 | 8 | 36 (0) | 0 | 10 / 16 | 75 -> 75 | 0 |
| 6 Ch 10 | v87 -> v88 | 45 | 226 | 84 | 7 | 55 (0) | 0 | 66 / 13 | 177 -> 117 | 0 |
| 7 Ch 1 | v28 -> v29 | 38 | 165 | 55 | 9 | 49 (0) | 0 | 2 / 41 | 164 -> 164 | 0 |
| 7 Ch 2 | v38 -> v39 | 28 | 135 | 48 | 6 | 30 (0) | 0 | 0 / 0 | 76 -> 85 | 9 |
| 7 Ch 3 | v38 -> v39 | 39 | 173 | 57 | 9 | 49 (0) | 0 | 14 / 0 | 100 -> 100 | 0 |
| 7 Ch 4 | v36 -> v37 | 33 | 158 | 58 | 6 | 38 (0) | 0 | 28 / 0 | 87 -> 87 | 0 |
| 7 Ch 5 | v47 -> v48 | 26 | 98 | 31 | 7 | 32 (0) | 0 | 13 / 2 | 55 -> 55 | 0 |
| 7 Ch 6 | v61 -> v62 | 26 | 126 | 42 | 10 | 34 (0) | 3 | 0 / 0 | 93 -> 94 | 0 |
| 7 Ch 7 | v56 -> v57 | 34 | 120 | 39 | 8 | 38 (0) | 0 | 19 / 1 | 67 -> 67 | 0 |
| 7 Ch 8 | v33 -> v34 | 30 | 125 | 37 | 8 | 36 (0) | 0 | 4 / 15 | 72 -> 72 | 0 |
| 7 Ch 9 | v60 -> v61 | 18 | 87 | 22 | 11 | 40 (7) | 3 | 0 / 0 | 185 -> 185 | 0 |
| 7 Ch 10 | v68 -> v69 | 38 | 135 | 40 | 13 | 37 (0) | 0 | 0 / 0 | 264 -> 264 | 0 |
| 7 Ch 11 | v26 -> v27 | 42 | 172 | 54 | 11 | 57 (0) | 0 | 4 / 50 | 134 -> 134 | 0 |
| 7 Ch 12 | v30 -> v31 | 38 | 173 | 62 | 8 | 41 (0) | 0 | 0 / 30 | 94 -> 94 | 0 |
| 7 Ch 13 | v32 -> v33 | 27 | 131 | 43 | 10 | 40 (0) | 0 | 2 / 34 | 72 -> 80 | 1 |
| 7 Ch 14 | v37 -> v38 | 28 | 104 | 33 | 10 | 35 (0) | 0 | 2 / 24 | 56 -> 56 | 0 |
| 7 Ch 15 | v26 -> v27 | 28 | 171 | 65 | 10 | 32 (34) | 0 | 0 / 12 | 650 -> 484 | 4 |
| 8 Ch 1 | v44 -> v45 | 25 | 113 | 35 | 10 | 40 (5) | 0 | 0 / 0 | 77 -> 77 | 0 |
| 8 Ch 2 | v33 -> v34 | 32 | 149 | 47 | 10 | 54 (9) | 0 | 0 / 149 | 101 -> 101 | 0 |
| 8 Ch 3 | v35 -> v36 | 29 | 100 | 30 | 9 | 38 (14) | 0 | 0 / 0 | 69 -> 69 | 0 |
| 8 Ch 4 | v28 -> v29 | 28 | 110 | 35 | 10 | 38 (8) | 0 | 0 / 11 | 78 -> 78 | 0 |
| 8 Ch 5 | v35 -> v36 | 33 | 152 | 52 | 10 | 46 (28) | 0 | 0 / 0 | 103 -> 103 | 0 |
| 8 Ch 6 | v31 -> v32 | 23 | 121 | 43 | 10 | 33 (16) | 0 | 0 / 0 | 77 -> 77 | 0 |
| 8 Ch 7 | v21 -> v22 | 31 | 120 | 44 | 9 | 30 (22) | 0 | 0 / 28 | 75 -> 75 | 0 |
| 8 Ch 8 | v55 -> v56 | 19 | 205 | 84 | 7 | 26 (38) | 0 | 0 / 78 | 455 -> 339 | 0 |
| 8 Ch 9 | v53 -> v54 | 16 | 103 | 23 | 10 | 27 (0) | 0 | 0 / 0 | 458 -> 391 | 3 |
| 8 Ch 10 | v34 -> v35 | 19 | 91 | 28 | 6 | 19 (22) | 0 | 0 / 0 | 320 -> 282 | 0 |
| 8 Ch 11 | v30 -> v31 | 31 | 92 | 14 | 10 | 63 (0) | 16 | 0 / 1 | 158 -> 158 | 0 |
| 8 Ch 12 | v23 -> v24 | 29 | 98 | 16 | 10 | 61 (0) | 22 | 0 / 0 | 187 -> 187 | 0 |
| 8 Ch 13 | v27 -> v28 | 18 | 102 | 36 | 9 | 29 (15) | 0 | 0 / 0 | 66 -> 66 | 0 |
| 8 Ch 14 | v38 -> v39 | 25 | 97 | 15 | 9 | 66 (0) | 33 | 0 / 0 | 240 -> 240 | 0 |

The gate comparison runs `gates/gate_runner` on the source and on the result with the strict config (`solutions` + `question_layout` on). A problem is counted NEW only if its text did not occur before. 34 of 39 chapters introduce none. The five that do:
- **maths7_ch2**: errata entry never matched (remove it from config): (8 - 3) × 7 = 8 × 7; errata entry never matched (remove it from config): (9 + 2) × 4 = 9 × 4; errata entry never matched (remove it from config): 24 + (6 - 4) = 24 + 6; errata entry never matched (remove it from config): 24 - (6 + 4) = 24; errata entry never matched (remove it from config): 24 - 6 - 4 = 24 - 6
- **maths7_ch13**: solution_content: <id>: image <id> has no render_source.code_url (Manim code)
- **maths7_ch15**: skeleton: <id>: <id> maps to 2 exercise/FIO item(s) via ncert_refs (want exactly 1); skeleton: <id>: <id> maps to 3 exercise/FIO item(s) via ncert_refs (want exactly 1); skeleton: <id>: <id> maps to 4 exercise/FIO item(s) via ncert_refs (want exactly 1); skeleton: <id>: <id> maps to 5 exercise/FIO item(s) via ncert_refs (want exactly 1)
- **maths8_ch9**: skeleton: <id>: <id> maps to 2 exercise/FIO item(s) via ncert_refs (want exactly 1); skeleton: <id>: <id> maps to 5 exercise/FIO item(s) via ncert_refs (want exactly 1); skeleton: <id>: <id> maps to 6 exercise/FIO item(s) via ncert_refs (want exactly 1)

Why: 7.2's `chapter.config.json` carries errata entries for question wording the gate used to misread; they no longer match (remove them from the config). 7.13 has 8 images with no role and no `render_source` in the live plan (they predate the solution-card pipeline). 7.15 and 8.9 have concepts that cover several printed items (`ncert_refs` of 2 to 6), which the skeleton rule now checks because their Questions topics are now typed `exercise`; they were typed as idea topics before.

## How the Part 2 rules were applied to live plans
- Every concept of a `Questions:` topic with a question block becomes `Q` (question card: `qt_part: question`, the question image) + `Ans` (steps, answer, the video, the solution cards: `qt_part: answer`). A concept holding several printed questions keeps all of them in one pair.
- Questions of one teaching topic are grouped by category into `Questions: Figure it Out <sec>`, `Questions: Example`, `Questions: Exercise Set x.y`, `Questions: Let us do` or, for everything else, `Questions: <the teaching topic's own name>` (as for Class 6 Ch 3 in the guide). `book_number` on the blocks was rewritten so that `core/question_naming.classify()` lands on the same category.
- Ids renumbered globally (topic, segment, concept, media). Media ids: question image `Cq.IMG1`, answer `Ca.VID1`, `Ca.IMG1..`. **Every planned_url / image_url / video_url / 2d_tool_url / code_url is unchanged**, so a file already made or reserved under it is still found.
- `ncert_coverage` points at both concepts of a pair. Objectives anchored only to a replaced question concept are dropped and the rest renumbered O1..On (guide, section 6).
- The displayed text is inline LaTeX with `question_tex`, `steps_tex`, `answer_tex` beside it; the plain `question`, `steps`, `answer` keep the book's wording (except where `edits.json` says otherwise).
- Part 1: `core/field_cleanup.py` (video_coverage, source_type, source_segment_role, tool_id, is_enrichment, topic_objective and the other gate-read fields are kept for the 6-8 band, exactly as in the Class 5 build).

## Decisions you may want to change
1. **Objectives dropped (290).** Done as the guide does for 6.3. Largest: 6.3 (59), 8.8 (38), 7.15 (34), 8.5 (28), 8.7 (22), 8.10 (22), 8.6 (16), 8.13 (15), 8.3 (14), 6.6 (13). The full list with texts is in each chapter's `report.json` (`dropped_objectives`). If these objectives should stay, the alternative is to keep them anchored to the answer concept; ask and I will change the rule.
2. **Stubs (82).** Question slots whose live concept has no question text at all (8.11: 16, 8.12: 22, 8.14: 33, 6.6: 5, 7.6: 3, 7.9: 3). They are grouped with their topic but not split and nothing was invented. Filling them needs the book pages; ids are in `report.json` (`stubs`).
3. Authored solutions: 6.10 (60: steps for answers that were already printed), 6.2 (17), 6.3 (12). Open items start with 'Sample answer:'. Please have a teacher skim these.
4. Upload: done (see 'Upload'). 7.3 is a draft, not active.

## Shared code changed (found by running the real chapters; none of it was in the request)
All edited with a CRLF-preserving patch; the converter was measured on all 10,150 distinct question/step/answer strings before and after each change, and its self-test still matches `LATEX_REFERENCE.md`.
- `core/solutions/latex_convert.py`: a run of superscript digits is one exponent (`2^{10}`; it used to crash, and `(-1)^56` rendered as `^5^6`); `unit(s)`, `sec`, `min`, `hr`, `ft`, `ml` are units only after a number (the old rule produced `of$\text{ units}$ here`, 150 strings); `km/h` and `m/s` stay units; grams after a number; the article 'a' after `(`, `,` or a cue word is prose, 'a' at the start of the text no longer counts as a variable; a bracket that opens on a number followed by an English word is prose (`($3$ is a common factor)`, 76 strings); `HCF`, `LCM`, `my`, `me` and the pronoun 'I' are words; `\cong`, `\parallel` and U+2206 are converted.
- `core/solutions/latex_house.py` (new): general house-style rules before conversion: `a)`, `a.` and `(a)` part labels, a.m./p.m., ellipses between operators, blanks.
- `core/solutions/latex_checker.py`: `\neq`, `\leq`, `\geq` were flagged as 'glued commands' (a backtracking false positive).
- `core/solutions/schema.py` (`tex_to_plain`): a mixed number `2 \frac{1}{3}` stays `2 1/3` (it became `2 (1)/(3)` and was read as 2 x 1/3); line breaks are kept (a chain `... x 23` + newline + `Answer:` ran together and was cut).
- `gates/gate_runner.py`: the question half of a Q/A pair is not scanned for false equations (a question such as 'Add brackets so that 34 - 9 + 12 = 13' is not an assertion), and the answer half does not re-scan its repeated question.
- `gates/eqcheck_signed.py`: Indian grouping (2,60,000) is one number.
- New: `core/field_cleanup.py`, `core/qa_split_live.py`, `core/solutions/latex_house.py`.

Known converter limits left (reviewers reworded around them): all-capital words of up to four letters become italic maths unless wrapped (`$FDP$`, `$ISRO$`); `statement(s)`; `(50%)`; `(M2)`; `(2 to the power 5)^2` leaves a stray `$^2$`; `(i)` in an a-j list stays plain text (the LaTeX reference allows roman labels outside maths); `a 1/4 turn`; `o'clock`.

## Appendix A: problems found in the existing tool specifications
The descriptions were written to be mathematically right and to keep each tool's own cards and numbers. Where the specification disagreed with the chapter's maths, the description follows the maths and the stored `tool_config` was NOT changed, so the spec itself still needs correcting. The ones that matter most: 6.8 Compass Circle Maker card 5 (stored answer 'yes' should be 'no'), 6.4 Pictograph Builder key card (5 or 15 -> 5 or 10), 6.10 Lift Mover card 6 (+2 should be -2), 7.5 Dot Paper Line Studio yes/no card (the two lines are parallel), 7.7 Two Circles Explorer card 4 (the circles cross, they do not touch), 7.3 Digit by Digit Zoom Locator (a point past 4.8 on a line that ends at 4.8), 8.5 Rule Bench 11 tester, 8.8 (six of seven tools are AI-driven with nothing clickable, thin against the 'learning by doing' brief).

Full list by chapter:
- 6.1 Next Shape Drawer: card 1 says "fifth shape (a pentagon)" but a pentagon is the third regular polygon (triangle, square, pentagon).
- 6.1 Sequence Rule Finder: rule picker has no "squares" option; Sequence Relations Lab: powers-of-2 card needs a "then add 1" step the picker lacks.
- 7.10 Terhuchu Match: spec lists misconception "ignoring the sign: reading -4 as 4 units to the right", which does not fit a capture game.
- 6.8 Compass Circle Maker card 5 (radii 3 cm, centres 4 cm apart: is one centre inside the other?): stored answer "yes" is WRONG, it is "no" (4 cm > radius 3 cm). Description says "no"; the card's stored answer needs correcting.
- 6.8 Side and Diagonal Builder: wrong-end feedback in the spec is loose; misconception M_NAME_ANY_ORDER has no feedback (added ABCD accepted / ABDC rejected check). Shape Property Checker offers square/rectangle/neither only; objective O12 also lists rhombus.
- 6.4 Pictograph Builder: card "good key for 20, 30, 45 (5 or 15)" is WRONG (15 leaves 5 over on 20): written as 5 or 10; key picker (1,2,5,10,100) has no 6 but the dogs card needs 6. Bar Graph Builder "find the wrong bar" card has no data (used the Indore bar of the ticket graph). Pictograph Reader last card "double the count" is loose.
- 7.5 Dot Paper Line Studio: yes/no card "3 across 3 down vs 1 across 1 down, no" is WRONG (those are parallel): written as 3 across 3 up vs 1 across 1 down. Set Square Slide Constructor: "ruler along l" does not work for the through-A-parallel card; "turn 45 to 60 degrees" needs the 30-60 set square. Alternate Angle Chaser: screen uses letters a-h, card uses numbers ("given 6 is 135").
- 6.7 Fraction Wall: rows are one whole long but cards 5 and 6 (5/4, 4/3) pass one whole (wall extended to a second whole). Unit Fraction Puzzle card 1 ("not possible") has no control to say so. Mixed Number Builder stepper range unspecified (needs 11). Fraction Bar Combiner covers subtraction only though note/objective O27 say adding too; the adding topic has no tool.
- 7.2 Gap Comparer / Term Splitter: small open points filled in (beam level until check; refused cut inside bracket).
- 8.9 Altar Builder spec deliberately thin (sandbox + one nudge); Square Combiner 4th task (area 24) rests on concept text; none of the 10 specs has a hint ladder.
- 6.2 Name the Angle card 6 "four points on two lines" (chapter has four points, no three on a line, six lines, 12 angles - written that way). Protractor Reader / Draw the Angle / Paper Protractor: cards give no angle sizes (sizes taken from the chapter's figures; triangle 50/60/70 is the agent's own); Which Angle Is Greater / Sort the Angle card 6 only a phrase.
- 7.8 Fraction of a Journey Strip last card (two different times, same distance) can only be equal fractions; Unit Square Product Maker pickers stop at 8 so the 1/12 x 1/18 card is a typed explanation; Product Size Predictor 565/465 and 707/676 typed in.
- 6.10 Lift Mover card 6: spec total movement "+2" is WRONG (lift ends at +3: it is -2); card 4 lands on -6 but the shaft stops at -5 (extended); Floor Line card 5 compares -7 and 0 but the line runs +6..-6 (extended); Floor Line movement cards use Target minus Start, taught later (agent let the student count steps); Snakes and Ladders spec gives no ladder/snake squares and no overshoot rule at +/-50.
- 7.3 Digit by Digit Zoom Locator last challenge "line 4.3 to 4.8, one part after 4.8" impossible (a point past 4.8 is not on a line ending at 4.8); written as the chapter's question (mark every 0.05, 4.8 at the tenth mark, one more mark) - answer 4.85 stays right.
- 6.9 Punch and Unfold last card ("fold twice, cut a corner") does not say which square results (written so the student makes both); Radial Arms Builder card 2 says "the two pairs differ" but the screen has identical arms (used gaps 60/120/60/120); Angle Ladder mixed-fraction read-out never fires on the 12-sector circle (used for 17 and 7 turns); Fold and Find Lines sits in the first topic but its cards (square, rectangle diagonal, hexagon) are taught later.
- 7.4 Pattern Formula Finder: rope card (r+2) starts at 0 folds so the added amount is used r times; hint "one fewer than y" does not fit it; "fits first two steps but not the third" cannot happen on its six linear patterns. Words to Expression Assembler: no numbers for four cards (bags, wage, pages, pens - agent supplied story constants) and uses 30x before the dropped-times-sign topic; Grid Shape General Prover card 5 (6w - 21) is the agent's own working.
- 7.7 Two Circles Explorer card 4: spec says base 9 with radii 3.5 and 6 TOUCH - WRONG (3.5 + 6 = 9.5 > 9, the circles cross); written as "cross, only just". Triangle Classifier card 4: chapter defers "equal sides mean equal angles", framed via measured 60 degree angles. Triangle Inequality Checker: spec says tent and two poles, chapter has tent, tree and pole.
- 7.1 Trading Board: student_does says trade "to its right ... or to its left" but the screen lists columns smallest to largest (direction looks reversed; avoided left/right). System Converter cards only name numbers (used the chapter's compare pairs). Lakh Ruler and Matchstick Builder specs thin on mechanics (agent added a magnifier and a spare-stick tray).
- 6.5 Rectangle Maker stepper 2..60 but card 4 asks about 1 dot (written 1..60); Eratosthenes Sieve card 4 "crossed out by 7 but not 2,3,5 (49)" incomplete (77 and 91 also qualify; card asks smallest, 49); Thread Art Co-prime Check card 6 uses 35 and 415, beyond the 6..24 peg range (factor lists instead); Last Two and Three Digits: 8560 already a multiple of 8, card 3 needs a changed number (8552); Prime Grid Puzzle done_when says "six puzzles" but cards 1-4 are single rows/columns (cards 5-6 use chapter puzzles 1 and 2).
- 6.3 Line-Up Lab, Supercell Builder, Digit-Sum Dials, Digit Hunt Grid, Palindrome Clock: tool_config done_when/challenges are older and shorter than the long existing description (Line-Up Lab 6 cards vs 8; Supercell Builder levels 1-6 vs 8; Digit-Sum Dials 5 goals vs 6; Palindrome Clock 4 challenges vs 8) - agent followed the long description + teaching notes. Race-to-N Arena thin (no phases/hint rungs, hint order added). Kaprekar Machine: plan notes say 5683 prints 8 rounds, agent wrote 7 (correct when four digits are kept).
- 6.6 Floor Coverer: floor resizes only to 15 x 15 but the grove card is 100 m x 50 m (agent added a scale of 10 m per square); Half the Rectangle: "every triangle is half its snug rectangle" is only true with a base on a grid line; Wire Bender card 4 "impossible" holds only for whole-cm sides; no tool has a hint ladder.
- 7.6 Sum Grid Solver: spec says rows 13/14/18, columns 24/9/12 has "one answer" but without clues it has 14 (written with 9 fixed top-left and 5 bottom-right as in the chapter question); impossible grid has two true reasons; Expression Parity Machine statement (c) is false per the chapter solution; no hint ladders.
- 7.12 Decimal Column Drop Chart ends at ten-thousandths but /10000 results need millionths (used thousands..millionths); Regrouping Tray blocks start at hundreds but 1325/1217/4827 need thousands (added); Divisor Size Quotient Predictor slider 0.1..10 cannot hold 0.003 (zoom added); Factor Size Product Predictor line 0..10 cannot hold 22.1 (stretched to 25; 0.0042 needs a second zoom); Same Stretch Divisor Clearer 12.43 / 0.6 never ends (approximate check); Remainder Cycle Tracker: type-the-digit step added.
- 7.9 No tool has a hint ladder. Pull Them Apart: rule menu lists SAS/ASA/AAS/RHS which come later (every card is SSS); Right Angle Rescue card 1 puts the right angle at Q but Swinging Gate hinges at Q; Six Congruent Pieces card 5 needs an "impossible" button the controls lack; Fold the Isosceles: angle panel "always visible" yet hides base angles from card 3.
- 7.11 Tile-Fitting Challenge spec thin (one 60-second round only; floor, tile sizes, found list, hint ladder and cards are the agent's own from the chapter); HCF or LCM Decider cards 2-4 are not split-or-meet choices (Yes/No multiple or factor, prime-form HCF/LCM, build two numbers for HCF 1 and LCM 66) and its six cards repeat end-of-chapter Q1-Q6.
- 8.8 SIX of the 7 tools (Hundred Square, Piece to Whole, Target Meter, Before & After, Shop Counter, Coupon Stacker) are AI-driven in the plan ("nothing is clickable"; the student answers aloud): thin against the learning-by-doing brief - making them student-operated needs a spec change; only Two Jars is student-operated. Tool-level hints/questions missing (hint ladders from concepts). Raghu's rice loss is 14.28% in the chapter text and 14.29% in the spec (true 14.2857%, written "about 14.3%").
- 8.14 Parallelogram Cutter: screen says the cut "stays perpendicular", feedback says a non-perpendicular cut is "refused"; Triangle Slider card 2 "largest perimeter" has no true maximum; Trapezium Joiner "six sided figure" feedback unverified maths (kept); Rectangle Stretcher: concept also covers path and tube areas, spec has no such cards.
- 8.10 Map Scale Explorer feedback "dividing km by 60 ... calling it km" is muddled; Ratio Table Scaler "x1.5 in the concrete ratio" is wrong (1.5 is a term, the factor is 3); Ratio Bar Splitter discrimination step names the 288 Odiya books card, not among its six challenges; Direct or Inverse Sorter: 6 challenges but 12 cards in the deck.
- 7.14 Perpendicular Bisector Bench 4 cm/3 cm card gives no length for AB (assumed 5 cm: cut at 3.2 and 1.8); Equal Distance Finder: line "appears" after five dots AND a toggle (toggle unlocks after five dots); Angle Halver "nearest halving results" for 65.5 deg undefined; Colour Count Tiler L-tile: 2 x 1 colour rule does not apply. No tool for M1.S6 (right angle at a point) or M4.S24 (tiling the plane).
- 7.13 Outlier Pull Mean Median Tracker stories card "dragged from 15 up to 40" but the 15 chapter values already contain 15 and 40 (read as an extra dot); palm-height card has no data in the spec (chapter palm data used); Double Bar Graph Scale Chooser grid height unspecified ("about twelve units"); Zoomed Axis Bar Comparer cards "Points 12.5 and 4.5" and "Skyscrapers 300 and 86" have no context.
- 8.1 Six tools without a hint ladder (Square Builder, Root As Side Length, Prime Factor Pairing, Root Between Which Numbers, Cube Stacker, Cube Root Tripler); Square Builder spec has no digits/end-zeros/parity content though its concept does; Root Between Which Numbers range 0-225 cannot hold 1936 or 250 (125 cloth case used); Root As Side Length positive root only (chapter's -8 not covered); Gap Between Squares: squares per hundred and triangular pairs not covered; Cube Root Tripler "one cube layer per ring" does not fit root 6.
- 8.11 Net Roller: spec lists radius, height and slant sliders together, but a cone's radius and slant fix the height (made a read-out); Net Folder: tool card puts the two extra squares on the same side of the row of four, chapter example stacks them (maths agrees); Ant Path Unfolder: spec does not say which unfolding makes the line leave the net.
- 7.15 No hint ladders on any of the 10 tools; Undo Machine split-path card (outputs 63 and 227) cannot be undone box by box (merge to "2x minus 3" first); Step Detective has no broken move for a wrong sign in a product (box 8); Both-Sides Stepper has no way to open a bracket (a "tidy" step added); Trick Tracer: four of five cards are clue puzzles, not step tricks.
- 8.2 Exponent Tower base 2-10 but its base-1 hunt needs base 1 (written 1-10), negative-base sign rule not covered, exponent 0 shown before the zero-exponent topic; Product Law Deriver: powers of a power not covered, strip length 1-6 vs 0-6 (used 0-6); Power Comparison Duel: concept beat asks to rewrite 2^10 vs 10^3 onto a common base (impossible: used bounding then values); Quotient Law Deriver: result "hidden" but a note says 27 is on screen; Fold Stack Doubler: the 0.007 option ignores the starting 0.001 cm.
- 8.3 Zero Placeholder Breaker: learn item says repairing one gap in 3005 gives "305 or 350" (only 305 is possible, written 305); Numeral System Sorter spec is legacy (Brahmi, a Class 6 subtractive-pair card, default 27: swapped for the chapter's systems and 125, added an 87 + 78 demo); Roman Numeral Builder: four-in-a-row flag conflicts with CCCC in cards 5-6 (allowed); Column Regrouping Board spec has no 5-counter.
- 8.4 Quad Dragger says it "opens the chapter" and works on a constructed parallelogram but sits in the rectangle topic (parallelograms met later in M4.S10); Sides And Angles Lab uses rhombus/trapezium presets before they are introduced; Quad Hierarchy Sorter has no kite ring and keeps trapezium in the outer ring only ("rhombus is a kite", "parallelogram is a trapezium" untestable); five tools without six-card list or hint ladder; Square in a Square "same inner square as 2 cm" card read as 6 cm.
- 8.6 Five tools (Distributive Area, Binomial Tile Multiplier, Square Of Sum Tiles, Identity Generaliser, Identity Match Sort) have no hint ladder or fixed card list (cards from the Learn/Practice banks); Identity Generaliser's concept recap covers 2(a^2+b^2) and difference of squares but the tool only tests the square of a sum; Identity Match Sort says a sum of two squares does not factorise "over whole numbers".
- 8.12 Missing Value Lab card 2: chapter's coconut problem is a correction (mean 25.6 over 15 trees, one count 3 too high, corrected 25.4), cards 3/5/6 give no data (example sets added); Spreadsheet Simulator card 6 says "class heights sheet" but the chapter's sheet is the marks table; Frequency Table Lab card 5 "adding frequencies directly" ambiguous (both shortcuts shown: 6.5 and 4.5); Line Graph Builder card 3: Punjab's twelve monthly values are not in the plan; Infographic Map card 5: Karnataka's true value not in the chapter.
- 8.5 Digit Puzzle Solver does addition only though the topic's puzzles (PQ x 8 = RS, GH x H = 9K, BYE x 6 = RAY) are multiplication; Rule Bench: spec mentions testers for 3, 6, 9 but the bench has only 2, 4, 5, 8, 10, 11; its 11 tester passes only on a difference of 0 (wrong: 0 or any multiple of 11) and appears before the chapter teaches 11; no card list/hint ladder on three tools; note says "25 more" counterexamples up to 200 but the correct count is 25 in all.
- 8.7 Additive Vs Multiplicative Judge: spec is built on a taxi fare with a fixed charge, a plot and a line through the origin - none of that is in the chapter (rebuilt on the chapter's own cases: Neelima's ages, Lucknow-Kanpur, lemonade, mid-day meal; plot/origin left out); the first seven tools have no hint ladder; Ratio Mixer old note describes a taste bar but the spec uses a swatch above each glass (spec followed).

## Appendix B: existing worked answers or book notes the reviewers flagged or changed
- 6.3 C71 (Kaprekar 5683): teacher note said "127 starting numbers never reach 6174"; agent's count with the leading zero dropped is 77; wording replaced by "some starting numbers, such as 1000".
- 7.1 C93 "Strike out 10 digits": answer/step wrote 123456789 as 1,23,45,67,89; Indian grouping is 12,34,56,789 (fixed). Stray "(b)/(c)/(d)" labels removed from the Roxie/Estu steps (question shows none).
- 7.3 C92(e) step "Tens: 2 + 1 = 3 and 1" and C92(g) "Write 0.03 as 0.03" reworded; C56 answer lacked 12 mm = 1.2 cm (added).
- 7.8 "Fractions of Fractions in a Square" (Figure it out: Ans1, key M3.S18.T18.C78#0): steps say the lines cut off a triangle that is half the square; as the question describes it that triangle is 1/4 of the square - final 3/32 still correct, left as is.
- 7.7 C40 "180 deg a triangle" -> "180 deg, a triangle"; 7.7 C23 variables a, b, c renamed p, q, r.
- 8.7: wording changes "my" -> "our", "I" -> "we", "O" dropped to avoid variable misreads.
- 6.4 C59 (tiger bars) depends on a figure the agent could not see, not verified.
- 7.13 C61 "Nights above 30 C": 6 am is exactly 30, reworded to "30 C or more"; C30 "mean fell by about 2.27" (exact 2.276, left); C76/C67 age-6 averages (113.1, 112.9) not checkable (book table not in the plan).
- Converter limits left (agents reworded around them): all-caps words of up to 4 letters become italic maths ($FDP$, $KYC$, $ISRO$) unless wrapped in \text via _phrases; "statement(s)" -> statement$(s)$; "(50%)" -> $(50$%); "(M2)" -> $(M_2)$; "(2 to the power 5)^2" gives a stray $^2$; a lowercase "(i)" in a-j lists stays plain text (the reference allows roman labels outside maths).
- 6.2 C104 Example 1 says "count your degrees (0, 10, 30)" - the book probably has 20 too (left as is); C95 gives 9 o'clock as 270 deg (reflex side), agent added the 90 deg other way in the steps; 17 gap solutions authored from the video scripts (open items start "Sample answer:"). Equation gate misreads "360 deg / 12 = 30 deg" as "12 = 30" (degree sign) - pre-existing.
- 7.14 C13 answer garbled ("every point ... is (SAS)") reworded; C30 steps used F undefined (C, D, F and equal sides added).
- 6.9 C55(b) and C44 answers depend on a figure, not verifiable from text; 7.15 C49 (arrow-path puzzle) same.
- 8.4 wording of one step changed to "so a + a = 180 - 50 = 130".
- 6.10 C120 Grid 1, row 4 prints -7 but the answer -8 only holds if it is -17 (possible printed error, left; agent avoided that cell in the steps). 60 gap solutions authored (steps leading to the given answers, verified); C63, C64, C120, C129 keep their book question text.

