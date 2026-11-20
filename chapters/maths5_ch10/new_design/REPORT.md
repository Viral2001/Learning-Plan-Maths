# Class 5 Chapter 10, Symmetrical Designs: build report

## 12 Nov 2026: tool phases removed

The tool write-ups no longer have Phase 1, Phase 2 and Phase 3. In `tools_*.py` the three "what the student does" entries are plain steps without a phase label, and the practice cards are named "Card N" or "Challenge" instead of "Phase N, card N". The same text is in the plan's tool_config, and Section C of `priority_doc.md` has one "What the student does" line per tool. Cards, book questions, feedback, hints and everything else are unchanged (the book's questions are still on the tool's cards). DESIGN.md and MEDIA_BRIEF.md still describe the older three-phase format; this note replaces it.


(Text written by the chapter helper and saved here by the lead session, because the helper could not write the file itself. This is the corrected version, after the lead session told the helper that the book's Learning Material Sheets are supplied inside eemm115.pdf. The lead session re-checks every chapter's built plan afterwards.)

Built locally on 6 Nov 2026, placeholder route as Chapter 2. Nothing uploaded, nothing outside this folder and the helper's scratchpad folder c5ch10 touched. The helper also ran one read-only `git status` by mistake; it changed nothing.

## What the sheets correction changed
- The chapter refers to one sheet: "Cut out squares and equilateral triangles with the same side length. These are provided at the end of the book." The helper rendered the 15th PDF page of `textbooks/class-5/eemm115.pdf` ("Tessellation and Shapes") and measured its vector art: 6 light blue squares (38 by 38) and 6 pink equilateral triangles (base 38, height 33, so the same side as the squares), also 6 five-sided shapes, 6 six-sided shapes, 6 circles and two cut-out puzzles that this chapter does not use.
- The assumption "as many as needed, to be confirmed" was removed from `content.SOLUTION_NOTES`, `priority_doc.md` (rows and A6.1) and `DESIGN.md`. They now describe the sheet. The Design Studio tool screen now offers 6 light blue squares, 6 pink equilateral triangles of the same side, and circles for the book's design. All sample designs use at most 1 square and 4 triangles, within the 6 of each (the book's design with added circles needs at most 5 circles).
- Side finding: the triangles drawn in the chapter's pictures (pp. 139 and 140) are not equilateral (height 48 on base 48), but the real sheet triangles are, so the plan follows the words and the sheet.
- Rebuilt, then rechecked in order: build, numeric check, check_master_id (clean), set_version last (version 2), validate_local. No other chapter file was touched.

## 1. Ids
- Symmetrical Designs, book `textbooks/class-5/eemm110.pdf`, 6 PDF pages = printed pages 136 to 141. The first PDF page is an unnumbered opener (page 136 by sequence; the next page prints 137).
- chapter_id `cbse_eng_maths5_ch10`, chapter_master_id 157, subject_ref_id 80, medium 1, publication 1, phase 2, media tag c5h. `check_master_id.py`: MASTER IDS: clean.
- `set_version.py`: live max version is 1, so the plan is version 2, plan_id `cbse_eng_maths5_ch10_v2`. A later upload would replace the live v1.

## 2. Counts
- 3 modules; 7 authored topics (T1 framing, T1B, T2, T3, T4, T5, T6 summary) + 13 "Questions: ..." topics = 20 topics and segments; 57 concepts (17 authored, 20 question, 20 answer).
- 20 book questions: 1 solved example (the printed H row of the turning table), 8 exercises (Let Us Do boxes), 11 prompts. Each has a question card, an answer with solution card(s) (all 20 workings need 2 solution cards) and one video.
- 31 coverage ids (11 text, 20 questions; the book has no discussion prompts). Coverage gate clean.
- 30 placeholder videos: 1 hook, 9 concept (one per teaching idea), 20 question videos.
- 4 placeholder tools: Fold and Cut (T1, free try), Turn and Check (T2), Symmetry Sorter (T3), Design Studio (T4). T1B and T5 have no tool.
- 71 image placeholders: 11 concept images (T1.C1, T1B.C1, T1B.C2, T2.C1, T2.C2, T3.C1, T4.C1, T4.C2, T5.C1, T5.C2, T6.C1), 20 question cards (18 with a diagram), 40 solution cards. The 6 practice concepts (T1.C3, T1B.C3, T2.C3, T3.C2, T4.C3, T5.C3) have a no-image decision with a reason.
- 14 concept objectives, 5 topic objectives.

## 3. Gate state
- `build.py --placeholders`: "structure stage OK". structure 0, equations checked 10 / failed 0, coverage 0, skeleton 0, objectives 0, solution_content 0, latex_content 0, question_layout 0, video_script_rules 60 (expected). One advisory: 20 book items map to a question and an answer concept (expected).
- `validate_local.py`: 60 messages, ALL of family `video_script_rules`, nothing else, no stamp (expected). Grouped: 30 "missing keys" (placeholder video, no script), 29 "needs an interaction_point" (no beats), 1 "the chapter hook shows a picture". That is 2 per video, the same pattern as Ch2 (118 for 59 videos).
- Final numeric and text check (final_check.py and verify_facts.py in `/tmp/claude-1506/-root-maths-learning-plan/9dfc46bf-2f90-406d-86af-005a3698a5e2/scratchpad/c5ch10/`): ALL CHECKS PASSED. It scans 1,323 authored and 5,747 plan strings (dashes, fraction characters, plural fractions, NCERT/textbook/page N/Fig., words outside the chapter, polygon names, "(s)" forms, unbalanced `$`); recomputes every whole-number and fraction chain (the repo gate skips slash chains); recomputes turn arithmetic, letters, digits and numbers, the designs as point sets and the 19 border shapes against the page's vector drawing (3 pt tolerance). `media_specs.check_all()` prints `[]`.

## 4. Judgement calls and clashes with the brief
1. No revision video (the pipeline has none): the last topic is a text summary with short concept checks.
2. The framing topic holds only the hook and the free-try tool (Fold and Cut); the first concept video and the opener's questions are in the short idea topic T1B, as in Ch2. So the tool comes before its concept video; Tool 1 Phase 1 recalls the hook and Phase 3 asks the opener's questions as open challenges.
3. Four tools, not the usual 9 to 11 (the count follows the concepts). Block printing is recognition and stamping round a centre repeats Tool 4; the border shapes repeat Tool 3; the project is a paper activity.
4. Book order kept, except "reflection only, turn only, or both" is taught (T3) before the digits, which need it. Border shapes and project stay with block printing, where the book prints them.
5. Kinds: the printed solved H row = example ("Example 1: the letter H turned"); Let Us Do = exercise; in-text questions and activities = prompt. Table rows I, X, Y = one question with 3 parts; Making Designs (a) to (d) = one question; opener blanks = one question with 3 parts; Let Us Think = 3 questions; squares and triangles = 3 questions.
6. Design A (printed "looks the same after every 1/4 turn") is kept as printed text, not a question.
7. Wording the LaTeX converter cannot read: cards write "digits", "shapes", "lines" for "digit(s)", "shape(s)", "line(s)"; "2-digit, 3-digit and 4-digit" for "2-, 3-, and 4-digit"; the printed options (a), (b), (c) of the 11 and 1001 question are dropped; "tick mark" for the tick symbol. Tool specs quote the book's original wording. `ch_latex_house.py` (adapted from Ch2's) also turns the converter's maths capital letters back into plain letters and unwraps (a) to (h) labels.
8. The plan letters the opener's three blanks (a), (b), (c); the book does not.
9. Turn names: the chapter names only 1/4, 1/2, 3/4 and full turn. The border-shapes answer needs 1/3, 1/5, 1/6, 1/7; they appear only there. No degrees, angles or "clockwise" anywhere (the book gives no direction; the plan turns "to the right, the same way each time").
10. Every letter or shape the plan adds (M, B, W, Z, T, S, C, U, F, P, plus sign, pinwheel, leaf block, flower block, circle with triangles, two-colour square) is a labelled practice value, never a book question shape.
11. Characters: Prem, Manu, Lali only (no pronouns for Prem and Manu); no kin words.

## 5. Points the book leaves unclear, with the reading adopted (please confirm)
1. Cut-outs (RESOLVED, nothing assumed): the sheet "Tessellation and Shapes" (15th PDF page of eemm115.pdf) gives 6 squares and 6 equilateral triangles of the same side. The plan uses only these, at most 6 of each.
2. The triangles in the chapter's pictures (pp. 139 and 140) are not equilateral (height 48 on base 48, other sides 54); the sheet's triangles are. The plan follows the words and the sheet; symmetry answers do not change.
3. Digits: the book draws 1 as a bar and 3, 8 with a smaller top. Adopted: reflection 0, 1, 3, 8; rotational 0, 1, 8; both 0, 1, 8; 6 and 9 turn into each other so neither looks the same alone. Measured on the printed digits: 0 99% on both lines, 8 97% vertical and 87% horizontal, 3 67% horizontal only. So 3 and 8 follow the usual hand-drawn reading, not the typeface exactly.
4. "How many times does this shape look the same during a full turn?" Counted 4 (1/4, 1/2, 3/4, full turn); if only turns before the full turn count, 3.
5. Let Us Think: a two-colour design that looks the same after every 1/4 turn must alternate colours on the 8 triangles (only 2 such colourings) and has no line of symmetry. The green and pink 2 by 2 square has 2 lines (its two diagonals).
6. Open items (Making Designs b and c, make designs, sort designs, diya and boat, digit examples, project): one sample answer each, "your answer may differ".
7. Turn direction not stated: turn to the right.
8. Border shapes are unnumbered; the plan numbers them 1 to 19 clockwise from the top-left corner (top 1 to 5 left to right, right side 6 to 10 downwards, bottom 11 to 14 right to left, left side 15 to 19 upwards). All measured on the page's vector art. Adopted: reflection symmetry in all except 13 (orange slanted four-sided shape) and 15 (thin right-angled triangle); rotational symmetry in all except 15. Shapes 4 (three circles joined by a Y, one leg about 19% short) and 9 (a ring of ten small triangles, meant as two twisted five-sided shapes, corners not exactly even) are drawn unevenly and are read as the even design (both symmetries); as drawn, 4 would be reflection only and 9 has no turn that fits. Shape 3 (yellow six-sided shape, sides 22 and 25) is a little stretched, so the plan says only that it has a vertical and a horizontal line and a half turn. DECISION NEEDED on 4 and 9.
9. Matching blocks to prints: the book prints only (iv) to (e). Worked out from the pictures: (i)-(c), (ii)-(d), (iii)-(a), (v)-(b).
10. Design B: 1/4 turn; both rotational and reflection symmetry (dashed vertical and horizontal lines shown).
11. Letters read as plain sans-serif capitals: E and K horizontal line, X and O both, T and V vertical, N none (N looks the same after a 1/2 turn). Measured on the printed K, a horizontal fold matches only roughly (60%); read as symmetric, as the choice of seven letters suggests (two horizontal, two vertical, two both, one neither).
12. The QR code on the opener is unreadable; nothing taken from it.
13. The wooden-block pictures (matching question, designs A and B) are real photographs. The plan describes them in the question card figures and does not copy them; the media team needs real or newly made block pictures. DECISION NEEDED.

## 6. Printed-book oddities
"Equilateral" triangles drawn isosceles in the chapter's pictures (5.2); digit 1 a bar, 3 and 8 uneven (5.3); border shapes unlabelled, shapes 4 and 9 uneven (5.8); only the H row of the table is filled in. No arithmetic errors (almost no arithmetic).

## 7. Answers the book does not print (worked out by the plan)
Every question except the printed H row and the printed line (iv)-(e): opener letters and blanks, diya and boat, firki, rows I X Y, digits, 11 and 1001, digit examples, Making Designs (a) to (d), the three Let Us Think questions, the squares and triangles designs and the four-square shape, sorting, matching, design B, the 19 border shapes, the project. Worked in DESIGN.md section 4 and checked by verify_facts.py and final_check.py.

## 8. Decisions needed from the user
1. Border shapes 4 and 9, and the 1/3, 1/5, 1/6, 1/7 turn names used only for that question.
2. The digit reading of 3 and 8, and of the letter K.
3. "4 times in a full turn" or "3".
4. How the wooden-block pictures are produced.
5. Whether a revision video is wanted (needs an explicit exception).
6. A later upload would replace live version 1 with version 2.

## 9. Files
priority_doc.md, DESIGN.md, content.py, concept_plan.py, topics_1.py to topics_3.py, tools_1.py, tools_2.py, topics_common.py, ch_latex_house.py, name_slots.json, book_rules.json, chapter.config.json, media_specs/*.json (17), media_specs.py, media_placeholders.py, build.py, cleanup_fields.py, server_ids.py, media_worklist.json, video_worklist.json, question_images_report.json, cbse_eng_maths5_ch10.json (version 2), scaffold files (book/, lp_brief.md, lp_state.json, MEDIA_BRIEF.md, chapter.config.README.md, empty video_scripts/). Scratch scripts: `/tmp/claude-1506/-root-maths-learning-plan/9dfc46bf-2f90-406d-86af-005a3698a5e2/scratchpad/c5ch10/` (verify_facts.py, final_check.py, sym_border.py, sym2.py, make_media_specs.py, sheet15.png).
