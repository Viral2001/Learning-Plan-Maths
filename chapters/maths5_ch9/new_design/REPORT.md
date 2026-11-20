# Class 5 Chapter 9, Coconut Farm: build report (local, placeholder route)

## 12 Nov 2026: tool phases removed

The tool write-ups no longer have Phase 1, Phase 2 and Phase 3. In `tools_*.py` the three "what the student does" entries are plain steps without a phase label, and the practice cards are named "Card N" or "Challenge" instead of "Phase N, card N". The same text is in the plan's tool_config, and Section C of `priority_doc.md` has one "What the student does" line per tool. Cards, book questions, feedback, hints and everything else are unchanged (the book's questions are still on the tool's cards). DESIGN.md and MEDIA_BRIEF.md still describe the older three-phase format; this note replaces it.


(Text written by the chapter helper and saved here by the lead session, because the helper could not write the file itself. The lead session re-checks every chapter's built plan afterwards.)

## Ids and source
- Coconut Farm (Maths Mela, Grade 5, Ch 9), `textbooks/class-5/eemm109.pdf`, 17 PDF pages = printed pages 119 to 135. The opener has no printed number: page 119 by sequence (the next page prints 120).
- chapter_id `cbse_eng_maths5_ch9`, master 156, subject_ref_id 80, medium 1, publication 1, phase 2, media_tag c5q (the scaffold's). `core/check_master_id.py`: MASTER IDS clean. Plan `cbse_eng_maths5_ch9.json`, version 2 (plan_id `cbse_eng_maths5_ch9_v2`; live max 1). Never uploaded, no git.
- No helper agents: all three starts were refused (session concurrent-subagent limit), so the chapter helper wrote every file and checked it with scripts. `division_steps.py` is a helper module it wrote that builds the take-away and place value working and asserts every number.
- The lead session's kit-sheet correction does not apply: this chapter refers to no kit, cut-out, token, grid or sheet.

## Counts
- 4 modules; 12 authored topics (T1 framing, T1B, T2 to T10 idea topics, T11 summary) + 26 Questions topics = 38 topics; 173 concepts.
- Teaching: 1 hook + 20 concept videos (one WE each) = 21; plus the summary concept (no video).
- Book questions 70 (question + answer concept each): 13 solved examples, 35 exercises, 22 prompts. 91 coverage ids (70 questions, 11 text, 10 talk); coverage clean.
- Videos: 91 placeholders (1 hook, 20 concept, 70 question). Tools 8: Coconut Array, Place Value Shifter, Smart Splitter, Take Away Groups, Regroup and Share, Quotient Change, Equal Balance, Always Sometimes Never; each 7 challenges (5 Phase 2 + 2 Phase 3), 4 hints.
- Image placeholders 184: 7 concept images (T1.C1 opener array, T1B.C1 one array two ways, T2.C2 place value chart, T3.C1 split bar, T4.C1 take-away bar, T6.C1 and T6.C2 base ten blocks) + 70 question cards (24 with a diagram) + 107 solution cards (37 questions have a second card). `media_specs.check_all()` prints `[]`.

## Gate state
- `build.py --placeholders` ends "structure stage OK". Equations checked 2,147, failed 0; coverage, skeleton, objectives, question layout, solution_content, latex_content clean.
- `validate_local.py`: 182 failures, one family only: video_script_rules x182 (91 slots x 2 messages; placeholder videos have no beats). Nothing else; no stamp (expected).
- Own checks (scratchpad c5ch9/: verify_facts.py, selfcheck.py, numcheck.py, brute.py): every number recomputed; 1,132 chains, 45 quotient/remainder statements, 23 comparisons, 23 halves etc. agree. The checker still lists only the book's own wording on question cards (blanks such as `___ ÷ 18 = 100`, the true/false statements, "Is 726 = 4 × 181?"), which the gate does not scan, and one false positive ("83 is 8 tens and 3 ones").

## Judgement calls and clashes
1. No recap video (pipeline): T11 is a text summary with short checks.
2. Framing topic: hook + free-try tool only; concept videos and the opener's questions are in T1B.
3. Tool 1 follows the hook (open exploration); its Phase 3 asks the opener's question.
4. 8 tools, not 9 to 11 (the count follows the concepts). No tool for: dividend/divisor/quotient, bigger numbers, word problems, puzzle and riddle, Vegetable Market activity, revision.
5. The hexagon puzzle (p. 122) and the riddle (p. 131) are book questions with their own solution video; no separate teaching concept.
6. The equation gate scans tool text and WE text. Quoting the book's deliberately false statements ("Is 726 = 4 × 181?", 20 − 6 = 7 × 3, `___ ÷ 9 = 16 ÷ 2`) inside a tool failed the build, so tool specs give the sides in words; question cards keep the book's wording. Quoting them with = in a tool needs a gate exemption (not touched).
7. Remainders are written "quotient 181, remainder 2" and "726 = 4 × 181 + 2" (the gate calls "726 ÷ 4 = 181" false).
8. Grouping: one coverage id per numbered question. Splits: LUD p.122 Q3 into two cards; p.134 twelve divisions into two cards of six; Statements Q3 (a)(b)(c); p.132 Q5 parts A, B, C; Try It! into two cards (splitting, halving); Let Us Play into products and quotients; Let Us Divide (a) to (d) four cards.
9. Placement: word problems of pp. 126, 132 to 134 after place value (T7); six-division remainder sets with the remainder rule (T4); the twelve divisions of p.134 with place value (T6); p.132 Q5 in its own topic (T8). Book order kept inside each group.
10. The hook attributes the opener's array to Susie and Sunitha's farm (book's characters); the opener names no one.
11. Ten name tokens in name_slots.json; Rahul (one question) in `_overflow`, written by name.
12. Notes for Teachers (pp. 120, 122, 125, 129) are not coverage items; no teaching role for a teacher.
13. Book number formats kept; "1l" written litres; Th H T O written as words ((T) and (F) kept in the statements items).

## Points the book leaves unclear, reading adopted (to confirm)
1. Let Us Play: no answers, many fit; one sample pair each; divisor 1 allowed.
2. LUD Q1 30 × 30: one division statement only (900 ÷ 30 = 30).
3. Hexagon puzzle: read as A ÷ B = C, A − D = F, C × E = H, F + G = H, numbers 1 to 8 once. Exactly two solutions: 6 ÷ 3 = 2, 6 − 5 = 1, 2 × 4 = 8, 1 + 7 = 8; and 8 ÷ 4 = 2, 8 − 7 = 1, 2 × 3 = 6, 1 + 5 = 6.
4. LUD Q3 holds three questions, split in two cards; 10 employees get ₹550 each (less); ₹11000 gives each ₹1100.
5. Try It!: the student chooses the split (samples 64 = 40 + 24, 265 = 250 + 15, 1560 = 1600 − 40, 4824 = 4800 + 24); Q5 halves 3 times (21), Q6 twice (36).
6. "Give 5 examples" and "when does repeated halving work": sample answers (divisors 2, 4, 8, 16).
7. "Each person will get 4 bags" (p.124): kept as each customer's 97 coconuts need 4 bags.
8. Rani's samosas (no price): read as the pack leaving fewer extra: packs of 6 (42 packs, 2 extra) vs 8 (32 packs, 6 extra). Please confirm.
9. Sofia's notes: six combinations (0/26, 2/21, 4/16, 6/11, 8/6, 10/1 of ₹50/₹20 notes); the book does not say if both kinds are needed; the first is flagged.
10. Rally (b): 232 km read from the map (344 + 232 = 576); 232 ÷ 4 = 58 km a day.
11. LUS Q7: (a) price of one mango, (b) total desks, (d) price of one idli missing; (c) complete (₹700). Practice values labelled. Confirm (c).
12. LUD p.131 ten boxes: each divisor box read as one digit: 120; 302; 20; 1000 ÷ 50 = 20; 848 ÷ 4 = 212 or 868 ÷ 4 = 217; 936 ÷ 3 = 312; 88 by 1, 2, 4 or 8; 9_0 many (sample 950 ÷ 5 = 190); 180 ÷ 1 = 180; 6,480 by 8 (810) or 9 (720).
13. Place value layouts print a leading zero in quotient boxes; shown in the layout, not in the quotient.
14. Digits of the quotient (one-digit divisor): as many as the dividend if its first digit is at least the divisor, else one fewer.
15. Statements Q4 (whole numbers): add 10 gives a multiple of ten: sometimes; subtraction order: sometimes (only equal numbers); double one and halve the other: always; odd multiplier gives even: sometimes; times 5 ends in 0: sometimes. The second row is least certain ("never" for different numbers is possible).
16. Vegetable Market total ₹9,185; the Activity (bills, role-play) has no answer and stays as a discussion item.
17. The QR code is unreadable, nothing taken; the book's cartoon children are unnamed.

## Printed-book errors and oddities
- p.126 Q2 "of of 41" and a space before "?"; p.132 "accomodate"; p.132 Q3 ends with a full stop; all written correctly.
- p.132 Q5 B: (c) and (e) are both 384 ÷ 8 (kept, 48); B(f) 86 ÷ 2 does not follow from 192 ÷ 4 (may mean 96 ÷ 2); answered 43 by plain division with a note.
- p.124 "each person" for customer; "1l"/"547 l" written litres.

## Answers the book does not print (worked out and checked)
The book prints solutions only for its 13 solved examples. Worked out: Let Us Play, every Let Us Do and Let Us Solve question, patterns and charts, Try It!, Let Us Learn to Divide, tender coconuts and extra money (₹3810), earnings ₹95,725, Let Us Divide (a) to (d), the ten boxes, the riddle (210), all word problems (bookshelves 30), the Vegetable Market table, relations A, B, C, and all statements. All facts are in DESIGN.md section 4.

## Decisions needed
1. Confirm Rani's samosas, Sofia's notes, LUS Q7 (c), and Statements Q4 row 2.
2. Tool Phase 3 quoting false statements with = needs a gate exemption, otherwise it stays in words.
3. 8 tools acceptable (below 9 to 11)? A tool for the hexagon puzzle or riddle, or solution video only?
4. Revision video exception (otherwise text summary).

## Files (chapters/maths5_ch9/new_design/)
priority_doc.md, DESIGN.md, content.py, concept_plan.py, topics_1..4.py, tools_1..4.py, division_steps.py, media_specs/*.json (33), name_slots.json, book_rules.json, chapter.config.json, build.py, cleanup_fields.py, server_ids.py, media_placeholders.py, media_specs.py, topics_common.py, ch_latex_house.py, cbse_eng_maths5_ch9.json (version set), media_worklist.json, video_worklist.json, question_images_report.json, book/. Scratch scripts: `/tmp/claude-1506/-root-maths-learning-plan/9dfc46bf-2f90-406d-86af-005a3698a5e2/scratchpad/c5ch9/`.
