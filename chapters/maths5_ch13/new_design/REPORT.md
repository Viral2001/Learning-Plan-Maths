# Class 5 Chapter 13, Animal Jumps: build report

## 12 Nov 2026: tool phases removed

The tool write-ups no longer have Phase 1, Phase 2 and Phase 3. In `tools_*.py` the three "what the student does" entries are plain steps without a phase label, and the practice cards are named "Card N" or "Challenge" instead of "Phase N, card N". The same text is in the plan's tool_config, and Section C of `priority_doc.md` has one "What the student does" line per tool. Cards, book questions, feedback, hints and everything else are unchanged (the book's questions are still on the tool's cards). DESIGN.md and MEDIA_BRIEF.md still describe the older three-phase format; this note replaces it.


(Text written by the chapter helper and saved here by the lead session, because the helper could not write the file itself. The numbers below are the helper's; the lead session re-checks every chapter's built plan afterwards.)

## 1. Ids and files
- Chapter: Class 5, Ch 13 "Animal Jumps", book `textbooks/class-5/eemm113.pdf`, 7 PDF pages = printed pages 164 to 170; the first PDF page is the unnumbered opener (page 164 by sequence).
- chapter_id `cbse_eng_maths5_ch13`, chapter_master_id 211, subject_ref_id 80, medium 1, publication 1, phase 2. `check_master_id`: "MASTER IDS: clean". `set_version` wrote version 2, plan_id `cbse_eng_maths5_ch13_v2` (live max is 1).
- Scratchpad (not in the repo): `/tmp/claude-1506/-root-maths-learning-plan/9dfc46bf-2f90-406d-86af-005a3698a5e2/scratchpad/c5ch13/` has verify_facts.py, check_numbers.py (independent numeric check), gen_media_specs.py (image specs with computed coordinates), validate_out.txt.
- No helper subagents were used (one launch was refused by the concurrency limit); the chapter helper wrote and checked everything.

## 2. Counts
- Built plan: 3 modules, 15 topics (7 authored + 8 "Questions: ..." topics), 60 concepts (18 authored + 42 question and answer concepts).
- Authored topics: T1 Find the Hidden Numbers (framing), T1B Factors and Multiples, T2 Arrays Show Factors, T3 Common Multiples, T4 Common Factors, T5 Factors and Multiples at Work, T6 Chapter Revision (summary). Modules: M1 Factors, Multiples and Arrays; M2 Common Multiples and Common Factors; M3 Using Factors and Multiples.
- Questions: 21 (0 solved examples, 12 exercises, 9 prompts). 38 coverage ids (13 text, 4 talk, 21 questions), 100% covered.
- Videos: 32 placeholders (1 hook, 10 concept, 21 question). No recap video, no puzzle video.
- Tools (5): Hidden Number Box (T1, free try after the hook), Array Maker (T2), Jump Together (T3), Trail Jumper (T4), Number Sorter (T5).
- Images: 68 placeholders = 11 concept images (hook, T1B.C1, T2.C1 to C3, T3.C1, T3.C2, T4.C1, T4.C2, T5.C2, summary) + 21 question cards (8 with a diagram) + 36 solution cards (15 questions have 2 cards, 6 have 1). 7 no-image decisions with reasons. `media_specs.check_all()` prints `[]`.

## 3. Gate state
- `build.py --placeholders` ends "structure stage OK". Structure 0; equations checked 633, failed 0; coverage 0; skeleton 0; objectives 0; solution_content 0; latex_content 0; question_layout 0; one advisory (21 items map to a question and an answer concept, expected).
- `validate_local`: 64 failures, ALL family `video_script_rules` (32 "missing keys", 31 "interactive_video_variant is ...", 1 "chapter hook shows a picture ..."), 2 per video slot as in Ch2. No other family. No stamp (expected).
- check_numbers.py: 1047 strings, 332 chains, 24 multiples lists, 33 factor lists, 35 "is a multiple of", 23 "divisible", 15 jump lists, 12 common factor claims, 76 chapter facts recomputed: 0 problems. Text scan: no dash, NCERT, textbook, page, Fig., plural fraction, or unspaced number list in student text. Longest displayed answer 201 LaTeX characters (limit 220). No `$$`, odd `$`, or stray single-letter span in the built plan.

## 4. Judgement calls and clashes
1. Revision video: the brief asks for one; the pipeline has none, so T6 is a text summary with a short check after each idea.
2. Concept video before tool: the framing topic holds one video, so Tool 1 follows the hook and the concept video follows it (as Ch2). Tool 1 Phase 3 asks the opener's questions as an open challenge.
3. Tool count 5 (not 9 to 11): a 7-page chapter with five distinct manipulable ideas. Q8, Q9, Q10 have no tool on purpose.
4. Three concepts added for the book's questions: "Numbers With Only Two Factors" (the prime-numbers margin question), "Checking a Statement" (Q8), "Divisible by 2, 5 and 10" (Q11). The book teaches them only through its questions; only the chapter's own words were used. Prime numbers are taught no further than the book's "why" (only the array 1 × the number).
5. No Example-kind questions: the book prints no numbered solved example. The printed trail lines (jump 2, jump 3) are the book's partial answer (trail.answer2, on the Practice concept) and a prompt (trail.three); the 5 and 10 blanks are prompts.
6. Question topics follow the label rule: "Questions: Arrays" (3 prompts), "Questions: Let us do" (arrays), "Questions: Animal Jumps" (2), "Questions: Mowgli's Trail" (3), plus a "Questions: Let us do" after each other practice topic. So "why 13 and 37 are prime" comes before the arrays question, and the trail prompts come after Q3 to Q7 rather than between Q3 and Q4.
7. Q8 to Q11 sit in one closing topic (T5); Q9 and Q10 apply common multiples and common factors.
8. Hook: Robby the rabbit and Deeku the deer (the opener's picture; named only in Q2) watch the box: the plan's reading.
9. Answers go beyond the book's lines (see 5.4). Open items (Q1 "any 5", Q4 (d), Q10, opener (c)) give one reasoned sample and "Your answer may differ".
10. True/false answers are written as words (False, True): the converter turns the letters F and T into maths variables.
11. Possible gate issue (not changed): the equation gate reads a chain that starts right after "(", such as "(2 × 3 = 6)", from its second number as "3 = 6" and fails it, although its docstring says such chains are skipped. 22 sentences were rewritten ("because", colon) to avoid it.
12. Image specs were generated by script from computed positions (tile pitches, number-line scales, circle centres); none rendered. The hook image uses the book's box numbers; all others use the plan's own WE numbers.
13. Names: 8 tokens in name_slots.json (Mowgli, Robby, Deeku, Sher Khan, Bagheera, Baloo, Kaa, Akela); unnamed animals are written by kind; teaching text uses names directly (as Ch2).

## 5. Points the book leaves unclear (reading adopted)
1. Q1 and Q7 print (f) twice (nine pairs each): lettered (a) to (i).
2. The last two trail stones are both printed 59 (61 stones): read as 60, trail 0 to 60. No friend there; only the "numbers he touches" lines for 5 and 10 include 60.
3. Sher Khan: the picture prints a red 26 beside the tiger; Q10 says 25 and the jumps of 5 need 25: placed on 25.
4. Incomplete answer lines: jump 2 prints 4, 12, 14, 50 (the red numbers in the picture are 4, 12, 26, 50); jump 3 prints 9, 21, 39, 57. Baloo (30) is also reached by 2, 3, 5, 10, the frog (12) also by 3. The plan gives full lists: jump 2: 4, 12, 14, 30, 50; jump 3: 9, 12, 21, 30, 39, 57; jump 5: 25, 30, 35, 50; jump 10: 30, 50.
5. Friends' places read from the picture and Q10: ant 4, spider 9, frog 12, bird 14, Kaa 21, Sher Khan 25, Baloo 30, Akela 35, deer 39, rabbit 50, monkey 57.
6. Q2: the food is drawn after stone 64, with no number: read as stone 64. Only Robby lands on it (4 × 16 = 64; Deeku lands on 60 then 66), so Robby is first. A food stone further on changes the answer.
7. Q9: day 0 or day 1 for the start: read as day 0, so days 15, 30, 45 ... (day 1 would give 1, 16, 31 ...).
8. Trail blanks for 5 and 10: first blank = numbers he touches, second = friends' numbers.
9. Q8 (f): answered True (a jump of 0 never leaves 0; 0 times any number is 0); 0 as a factor of 0 itself is not discussed.
10. Q11: none is divisible by 10 only; regions with exactly two circles are empty; 90, 30, 40 in the middle (3); 22, 38, 66, 78, 62, 84, 56 in 2 only (7); 75, 45, 25, 95, 55 in 5 only (5).
11. Box numbers are only in the picture: 28, 36, 48, 72 (picture order 28, 36, 72, 48). The text layer lists the Q11 cards by column; row order read from the image.
12. "Prime numbers" are named but not defined; the plan answers "why" from the arrays.
13. Q10 (b) "what number of jumps" read as jump size; (a) accepts a jump of 30 and excludes 1 and 5 (they land on 25).
14. The unnumbered arrays Let Us Do is labelled "Let Us Do (arrays), Q1" only to place it in a Questions topic.
15. Printing slips quoted corrected: "Multiple of 6" (p. 166), "exactly divides each the numbers" (p. 168).
16. The QR code on the opener cannot be read; nothing is taken from it.

## 6. Kits, sheets, cut-outs
None referred to by the chapter; no assumptions to confirm.

## 7. Printed-book errors
Duplicate (f) in Q1 and Q7; the trail's last stone printed 59 twice; red 26 beside Sher Khan (red 4, 12, 26, 50 against the text 4, 12, 14, 50); incomplete answer lines for jumps of 2 and 3; "Multiple of 6"; "each the numbers". None is quoted into a question or answer; all are in `content.SOLUTION_NOTES`.

## 8. Answers the book does not print (worked out and recomputed with Python; see DESIGN.md section 4)
Opener inputs for multipliers 4, 2, 1; factors of 15 and the four blanks of 12; factors of the nine numbers (counts 4, 4, 2, 6, 3, 6, 2, 4, 8); why 13 and 37 are prime; common multiples of 3 and 4 and of 4 and 6; Q1 (first common multiples 6, 40, 4, 9, 10, 36, 24, 24, 18); Q2; Q3 and jumps 3, 5, 10; Q4 (yes, yes, yes; 1, 6, 12; six common factors; yes); Q5 (only 1); Q6 (16, 36, 48); Q7; Q8 (F, F, T, T, T, T); Q9; Q10 ((a) 2, 3, 6, 10, 15, 30; (b) 1, 7); Q11.

## 9. Decisions needed from the user
1. Q2: is the food on stone 64?
2. Q9: day 0 (the plan's reading) or day 1?
3. Keep the three added concepts, or fold them into the practice sets?
4. Is a jump of 30 wanted in Q10 (a)?
5. Is the equation gate's reading of "(2 × 3 = 6)" as "3 = 6" intended?
6. A revision video needs an explicit exception to the pipeline.
