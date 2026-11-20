# REPORT: Class 5 Chapter 6, "The Dairy Farm" (local learning plan, placeholder route)

## 12 Nov 2026: tool phases removed

The tool write-ups no longer have Phase 1, Phase 2 and Phase 3. In `tools_*.py` the three "what the student does" entries are plain steps without a phase label, and the practice cards are named "Card N" or "Challenge" instead of "Phase N, card N". The same text is in the plan's tool_config, and Section C of `priority_doc.md` has one "What the student does" line per tool. Cards, book questions, feedback, hints and everything else are unchanged (the book's questions are still on the tool's cards). DESIGN.md and MEDIA_BRIEF.md still describe the older three-phase format; this note replaces it.


(Text written by the chapter helper and saved here by the lead session, because the helper could not write the file itself. The lead session re-checks every chapter's built plan afterwards.)

Built locally by the chapter helper and three sub-helpers. Nothing was uploaded, no git was run, nothing outside the chapter folder and the helper's scratchpad `c5ch6` was touched.

## 1. Chapter and ids
- Book: Maths Mela Grade 5 Ch 6, `textbooks/class-5/eemm106.pdf`, 22 PDF pages = printed 70 to 91. PDF page 1 is the unnumbered opener (70 by sequence; page 2 prints 71, the last prints 91). All numbers read from the page images.
- chapter_id `cbse_eng_maths5_ch6`, chapter_master_id 150, subject_ref_id 80, medium 1, publication 1, phase 2, media tag `c5r`. `core/check_master_id.py`: `MASTER IDS: clean`.
- Plan `cbse_eng_maths5_ch6.json`, version 2 / plan_id `cbse_eng_maths5_ch6_v2` (`set_version` found live max 1).
- Config: eqcheck "plain", doer_tool_optional, media_placeholders, field_cleanup, server_image_ids, publication_id 1, solutions, question_layout.

## 2. Counts
- 4 modules, 37 segments, 37 topics (1 framing, 15 idea, 20 "Questions: ..." topics, 1 summary), 186 concepts (40 authored: hook, free-try, 22 teaching, 15 practice, summary; plus 146 question and answer concepts = 73 pairs).
- Coverage ids 89, all covered (73 questions; 16 text and talk ids: 13 text, 3 talk). Questions: 8 solved examples (numbered Example 1 to 8 by the plan), 40 exercises, 25 prompts.
- Videos (placeholders) 96: 1 hook, 22 concept (2 are puzzles: digit puzzles, King's Reward), 73 question videos.
- Tools 6 (7 challenges, 4 hints each): Pouch Packer (free try), Place Value Shifter, Halve and Double Packets, Nearest Multiple Grid, Box and Lines, Carry Columns.
- Images (placeholders): 13 concept images (T1.C1, T1B.C1, T2.C1, T3.C1, T3.C2, T4.C1, T5.C1, T6.C1, T8.C1, T8.C2, T9.C2, T11.C2, T16.C1), a no-image decision with reason for the other 27 authored concepts (40 media_specs files); 73 question-card images (41 with a diagram) and 129 solution cards (73 first, 56 second).
- The summary is a text topic with short concept checks, no video.

## 3. Gate state
- `build.py --placeholders` ends `structure stage OK`: structure 0, equations checked 2,667 / failed 0, coverage 0, skeleton 0, objectives 0, solution_content 0, latex_content 0, question_layout 0, video_script_rules 192.
- `validate_local.py`: 192 failures, ALL `video_script_rules` (no stamp, expected). Grouped: 96 "missing keys" (placeholder videos have no beats), 95 "interactive_video_variant needs an interaction_point" (73 question, 22 concept videos), 1 "chapter hook shows a picture".
- Advisory only: coverage "mapped to more than one concept" (question and answer concepts, by design).
- Independent numeric check (scripts in scratchpad c5ch6): `verify_facts.py` recomputes and asserts every answer (brute force for the digit puzzles, shape puzzle, make-your-own-numbers, all products, King's Reward tables); `check_numbers.py` checks statements the repo gate cannot read (halves, doubles, "N tens is M", "is/gives" chains, comparisons) on every string and 175 expected numbers against the 73 answers (0 missing; its 20 flags were read by hand, all false positives); helper scripts h1/h2/h3 recompute about 800 facts, 0 wrong; `selfcheck.py` prints 0 problems for all three topic files.
- Scan of the built plan: no `$$`, no unbalanced `$`, no stray variables, no `$10s$`. Cosmetic converter quirk: the label "(i)" stays plain text (ld2.q4); not changed.

## 4. Judgement calls and clashes
1. Revision video: the pipeline has none; the last topic is a 35-line text summary with a check after each idea.
2. Hook before concept video: the framing topic holds one video, so Pouch Packer follows the hook and the concept video "Equal Groups" plus the five opener puzzles (Let Us Think Q1 to Q5) sit in T1B.
3. 6 tools, not 9 to 11 (follows the concepts). No tool, with reasons in priority_doc F2: order of numbers (Turn button of Tool 1), many ways, strategy choice and word problems, Check Check, same product and growing from a known product (same strip action as Tool 4), estimates, digit puzzles, King's Reward, patterns.
4. One book question = one item, except separate stories; Let Us Think Q1 is three items (a to c, d to f, g to i), Patterns Q2 tables two items.
5. Ten name slots (Daljeet Kaur, Priya, Gollappa, Nida, Kanti, John, Mili, Anjali, Mala, Ananya); Asma, Pankaj, Lado, Kira, Asher, the king and ministers stay as printed (`_overflow`).
6. Wording changed for the equation gate (same facts): "2 × 1,000 = 2 thousand = 2,000" reads as the false chain "2 × 1,000 = 2", so it says "is 2 thousand, which is written 2,000"; Let Us Multiply (a) says "___0 + 16 gives 256"; digit-box questions say "gives"; "twenty-four fours and eighteen sixes" (a "4s" converts to a variable); four-digit numbers carry commas in questions.
7. `q_figure` of solved examples shows only what the question gives; worked layouts are in the solution figure. Example 5 has no book picture, so a neutral compost heap with a ₹24 tag is described.
8. 20 of 73 answers are longer than two solution cards (longest ls2.q3b about 36 lines; ld2.q1, lt2.def, lt2.ghi 30 to 33). Two cards is the ceiling, so the renderer shrinks them or the media team shortens them. Ch1 and Ch2 had 10 and 5.
9. Teacher notes are kept as coverage ids only; no teaching role for a teacher.
10. Hook: Daljeet Kaur packs the opener's 60 pouches; no number beyond the book's 60, 2, 3 is added.
11. Kits and sheets: this chapter refers to none. The lead session's note that the Learning Material Sheets are in eemm115.pdf was read; it does not apply here, no sheet used, no kit assumption exists.
12. Built exactly like Ch2: the reference hooks in build.py, cleanup_fields, server_ids, media_placeholders (one purpose line per teaching video), patched media_specs.py, `ch_latex_house.py` instead of `frac_latex_house.py`.

## 5. Points the book leaves unclear (reading adopted; full text in priority_doc.md A6 and content.SOLUTION_NOTES)
1. The opener is unnumbered (70 by sequence).
2. LUT Q1 shapes (p.70): whether different shapes may share a number. Reading: different numbers; exactly 5 full sets (1 to 24), pentagon always 1, sentence (f) follows from (a) and (e). One set is the sample. Without the rule 108 sets fit.
3. Q3 pouches: arrangements unlettered, groups not defined. Reading: number of groups × group size, as 30 × 2 = 60 shows: 20 × 3, 6 × 10, 5 × 12.
4. Q4 "Which number am I?": clues (d) odd and (g) even ones digit contradict; no number fits all eight; without (d) exactly 18. Answer 18 with the reason.
5. Q5 make your own numbers: the same tile twice is not addressed. Reading: two different tiles, whole-number answer. 0 and 19 cannot be made; 15 numbers have more than one way; three numbers make 0 and 19.
6. Order of Numbers (p.72): letters a, b, e, f, g printed, the big-array pair unlettered (kept).
7. Patterns Q1 (h), (i): two blanks each after the given (g). Reading: swapped product and the answer.
8. Patterns Q2: boxes ask 700 × 4, the table row asks 700 × 8; both solved (2,800 and 5,600). 5 × 7,000 appears in both p.74 tables (kept).
9. Doubling/halving and nearest-multiple examples print no question sentence; worded from the working and prompts. Box 35 × 14 has unlabelled arrows: halve 14, double 35 (70 × 7 = 490).
10. LUD Q4 (a) cinema: 3 more full rows of 12, 48 + 36 = 84. (b) cricket: the score includes extras, 96 + 108 + 234 + 23 = 461.
11. LUD p.86 Q1: boxes unlettered (the plan letters (a) to (h)), "and" means plus. p.87 Q4 (e): printed "8 × 9 = 72" with a gap, read as 8 × 9 = 72.
12. LUT Q1 digit boxes (pp.87 to 88): each colour is one digit; in (a) to (c) orange answer boxes one digit, black boxes free. (a) 3, 6 or 9; (b) 3 to 9 (only 111, 222, 333 if black boxes were one digit too); (c) 3, 6 or 9; (d) ten sets; (e) 110 × 5 = 550; (f) 2,222 × 5 and 3,332 × 5; (g) eight sets, green always 0; (h) 857 × 7 = 5,999. (i) has no answer.
13. King's Reward: "for 7 days" = 7 multiplications (640, 6,561, 78,125); with 6 (320, 2,187, 15,625) Minister 3 still wins. "Which reward would you choose" is an opinion (sample, may differ).
14. Number pairs: only pairs joined by a line count (12): smallest 11 × 14 = 154, largest 35 × 75 = 2,625.
15. Let Us Solve (p.91): Ananya's own row counted (30 rows, 41 in her row), total 1,230 assumes equal rows; football expenses ₹1,750 + ₹1,129 = ₹2,879, no profit asked; Mala 6 sets of 3 books at ₹150 plus ₹20 = ₹920.
16. The QR code on the opener is unreadable (nothing taken); no printed summary page.

## 6. Printed-book errors and oddities
- p.71 clues (d) and (g) contradict.
- p.73 700 × 4 (boxes) against 700 × 8 (table).
- p.83 ghee working: "2 Tens × 574 = 2 × 3,740" should be 2 × 5,740 (20 × 574 = 11,480); Example 8 says so.
- p.85 Check, Check!: Pankaj's 135 is not the sum of his lines (92 + 115 = 207); Asher's 5,018 is not the sum of his rows (1,878 + 1,252 + 1,878 = 5,008). Verdicts: Asma correct (2,714), Pankaj not (203 × 54 = 10,962), Lado correct (5,700), Kira not (missing zero; 193 × 272 = 52,496), Asher not (rows not shifted; 626 × 323 = 202,198).
- p.88 digit box (i) has no answer (likely a colour slip).
- p.78 "1200" printed without a comma (shown 1,200).
- The book's solved examples are unnumbered; the plan numbers them Example 1 to 8.

## 7. Answers the book does not print (worked out by the plan)
The book prints only the working of the solved examples (54, 76, 294, 420, 3,600, 1,072, 5,889, 71,750) and the done examples. Every other answer of the 73 questions was worked out from the chapter's own methods and recomputed: shape sets, digits near 100 (53 × 2 = 106), pouch groups, 18, the 0 to 20 table, all products and word problems, every Check, Check! verdict and correction, same-answer boxes, easy ways, digit boxes, estimate matches (25 × 31 with 750, 132 × 19 with 2,600, 101 × 11 with 1,000, 248 × 49 with 12,500, 12 × 25 with 300), King's Reward, patterns, number pairs. See DESIGN.md section 4 (generated and asserted by verify_facts.py).

## 8. Helper choices to confirm or revert
- lm.b: the book's table already shows column sums 2,700 and 405 and total 3,105; the four cells are blank. Commas added to 2700, 3105, 2760.
- ex.dc3: "same coloured digits" answered by the helper's reading of the page image (blue: the 5 hundreds of 2,500 and 3 hundreds of 350, 5 + 3 = 8 hundreds; red: the 5 tens of 350 and 2 tens of 20, 5 + 2 = 7 tens). Please check against the printed colours.
- Check, Check! verdicts are "Correct." and "Not correct." (a capital NOT converts to a variable). ld2.q1's short answer names problems by position, every box worked in the steps.
- WE numbers changed from seeds where a seed repeated a book problem: T5.C2 25 × 28, T7.C1 50 × 34 (changed after review because 25 × 28 was also T5.C2's), T11.C1 14 × 15, T14.C1 20 × 36; T13.C1 uses two chests (3 coins doubled, 1 coin tripled, 4 days) so it does not repeat the book's choices.
- Long multi-part solutions work each part on one line with two or three short operations.
- kr.choose's sample answer says Choice 3 may catch up (mildly previews kr.calc); edit if a neutral version is wanted.

## 9. Decisions needed from the user
1. Colour reading of Let Us Think Q1, and (i) with no answer (a book slip, or meant to show "no answer"?).
2. The King's Reward reading (7 multiplications) and the cricket extras reading.
3. Restore the book's "=" form of the 1,000 and 100 patterns with `eqcheck_errata`, or keep the gate-safe wording.
4. Shorten or split the 20 long solutions before the solution cards are made?
5. Is a revision video wanted after all (needs an explicit pipeline exception)?

## 10. Files in the chapter folder
priority_doc.md, DESIGN.md, content.py, concept_plan.py, topics_1.py to topics_3.py (T1 to T5; T6 to T9; T10 to T16), tools_1.py to tools_3.py (3 tools; 3 tools; none), topics_common.py, ch_latex_house.py, media_placeholders.py, media_specs.py, media_specs/ (40 files), build.py, cleanup_fields.py, server_ids.py, name_slots.json, book_rules.json, chapter.config.json, the built cbse_eng_maths5_ch6.json (version 2), media_worklist.json, video_worklist.json, question_images_report.json, and the scaffold files (book/, lp_brief.md, lp_state.json, MEDIA_BRIEF.md, chapter.config.README.md, empty video_scripts/). Scratch scripts (verify_facts.py, check_numbers.py, selfcheck.py, items_data.py, gen_docs.py, h1/ h2/ h3/) are in `/tmp/claude-1506/-root-maths-learning-plan/9dfc46bf-2f90-406d-86af-005a3698a5e2/scratchpad/c5ch6/`.
