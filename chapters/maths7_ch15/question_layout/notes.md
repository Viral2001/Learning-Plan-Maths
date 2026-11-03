# Class 7 Ch 15 "Finding the Unknown" (cbse_eng_maths7_ch15, live v25): question layout notes

Spec: `layout_spec.json` (checked with `core/question_layout_live.py`). Media links of the live plan are intact (every media id a concept lists has a node and is named after that concept), so the layout could be authored.

Result of `check`: 93 question concepts in 10 Questions topics (15 live Questions topics merged by the engine into 10), made of 35 kept as they are plus 58 new. Tiers of the 58 new: 14 example, 40 exercise, 4 prompt. Of the 58, 24 are blocks cut out of teaching concepts and 34 are parts of 10 split concepts. New videos needed: 48 (the 10 first parts of split concepts keep the old video, which now covers only part of the old concept: "refresh"). `SPEC PROBLEMS`: none. `INTEGRITY: clean`. No "GATES WORSE THAN LIVE" line: structure 1 to 1, coverage 16 to 0, video_script_rules 76 to 76, skeleton 32 to 29, objectives 47 to 45.

## Things the caller should know

1. **Six teaching concepts are left with no content blocks.** C19 (Ex 4), C20 (Ex 3), C21 (Ex 2), C29 (Ex 5), C45 (Ex 8), C47 (Ex 12) each held exactly one `example` block and carry an objective, so the engine refuses to move them whole; their block is cut out and the concept stays as an empty shell with its objective (O11 x3, O17, O31, O32) and its rendered video. After renumbering the shells are M2.S6.T6.C22 to C24, M2.S8.T8.C39, M3.S12.T12.C71 and C73. The new Example 2, 3, 4, 5, 8, 12 questions have no video; the shell videos cover exactly those examples and could be re-attached by hand. Gates do not flag the shells.
2. **Videos that now describe a moved question** stay on the teaching concept they came from: C2 (mobiles 1 to 3), C3 (mobiles 6 to 8), C8 (Jasmine), C17 (2n + 1 = 99 by trial and error), C18 (Ex 1), C30 (Ex 6), C44 (Ex 7), C46 (Ex 9), C56 (Ex 10), C57 (Ex 11), C66 (Ex 13), C79 (Ex 16). Those concepts keep their text, predict and teaching blocks.
3. **No rename_teach.** No kept or new name contains "page N" (the structure gate pattern; all 93 names checked), no NCERT, textbook, Fig., en or em dash. The existing style "Chapter Exercises, Q3" carries a question number but not a page, so it stays; new names follow it ("Chapter Exercises, Q1 (a)", "Mend the Mistake, box 1"). No teaching concept is named "Example N: ...", so nothing is named twice. The one structure problem (live and after) is the video script of the C78 video using the word "textbook"; it is not a name.
4. Existing Questions topics typed instructional/exploration or practice are left as typed (the skeleton gate already flags that); the engine only merged and renamed them.

## How a book question was recognised here

The book prints a round "?" icon next to narration too (Example 1 to 6 working, "Why can we do this?", "What happens in cases like u/15 = 6?"), so the icon decides nothing. What counted:

* every printed **Example n** (1 to 13 and 16; the book has no 14 or 15) and every **Figure it Out** item (7.1 Q1, Q2; 7.2 Q1 to Q6; the 20 chapter-end items);
* an in-text task put to the reader whose plan block carries a plan question id (`Q_...`): the plan marks exactly the tasks it treats as questions (`Q_weights_a/b/c`, `Q_sacks_a/b`, `Q_jasmine`, `Q_ways_n`, `Q_other_solution`, `Q_200`, `Q_frame_rest`, `Q_frame5`, `Q_trial_5x`, `Q_check_ex5`, `Q_trick_rule`, `Q_chain_reverse`, `Q_formula_two/2x`). The in-text blocks tagged with descriptive ids (`frame_mobiles`, `solve_5x`, `u15`, `shortcut_*`, `generating`, `formula_650m`, `notation`) retell the book's own working and stay in teaching (see Borderline).
* The 9 "Mind the Mistake, Mend the Mistake" boxes (7.3) each have their own block, steps and answer, so each is a question (tier exercise: the whole section is the printed exercise).

Book order inside each Questions topic: in-text tasks and examples first, then the Figure it Out items, the way the book prints them; existing question concepts are all listed (`keep` or `split`), none dropped.

## New questions cut out of teaching concepts (24)

Plan source is `concept block`. All have `keep_video_of: null` (no video yet). Page numbers are the book's printed pages.

| Topic | New question | Book label or quote | Plan source (ref) | Tier | Why it counts |
|---|---|---|---|---|---|
| Unknown Weights | Unknown Weights: mobiles 1 to 3 | p164 "Find the unknown weights in the following cases", Fig 7.1 to 7.3 | M1.S2.T2.C2 b3 (7.1.Q_weights_a) | prompt | in-text task, definite weights; has q_figure and s_figure. |
| Unknown Weights | Unknown Weights: mobiles 6 to 8 | same task, Fig 7.6 to 7.8 | M1.S2.T2.C3 b3 (7.1.Q_weights_c) | prompt | same task, plan's third group; sits between the kept mobiles 4 and 5 and the kept sacks. |
| From a Pattern to an Equation | Matchstick Pattern: Jasmine's 99 sticks | p167 "Jasmine decides to make a matchstick arrangement ... exactly 99 sticks. What will be the position number ...?" | M1.S4.T4.C8 b3 (7.1.Q_jasmine) | prompt | task put to the reader; the plan's block asks for the equation 2n + 1 = 99 (the value n = 49 is in the trial-and-error question below). Has q_figure. |
| Trial and Error, and a Better Way | Trial and Error: solving 2n + 1 = 99 | p167 "Can you find ways to get the value of n ...?" and p168 "Can this equation have any other solution?" | M2.S7.T7.C17 b3 (7.2.Q_ways_n, folded 7.2.Q_other_solution) | prompt | two book tasks, one plan block; ids folded. Placed before the kept 5x - 4 = 7 trial question. |
| Trial and Error, and a Better Way | Example 1: Removing the term 88 | Example 1 (p169) | M2.S7.T7.C18 b3 (7.2.Ex1) | example | printed example. balance_property and same_op stay on C18. |
| Trial and Error, and a Better Way | Example 2: Removing the factor 7 | Example 2 (p169) | M2.S7.T7.C21 b0 (7.2.Ex2) | example | printed example; C21 left empty (see above). |
| Trial and Error, and a Better Way | Example 3: Removing a negative term | Example 3 (p169) | M2.S7.T7.C20 b0 (7.2.Ex3) | example | printed example; C20 left empty. |
| Trial and Error, and a Better Way | Example 4: Removing a fraction factor | Example 4 (p170) | M2.S7.T7.C19 b0 (7.2.Ex4) | example | printed example; C19 left empty. Placed in book order 1, 2, 3, 4 (the plan's concepts run 1, 4, 3, 2). |
| Solving Step by Step | Example 5: Solving 11y + (−5) = 61 | Example 5 (p171) | M2.S10.T10.C29 b0 (7.2.Ex5, folded 7.2.Q_check_ex5) | example | printed example plus its "Can you check ...?" line; C29 left empty. |
| Solving Step by Step | Example 6: Unknowns on both sides | Example 6 (p171) | M2.S10.T10.C30 b3 (7.2.Ex6) | example | printed example; check_note stays on C30. |
| Everyday Problems as Equations | Example 7: A hundred tiles in a sequence | Example 7 (p174) | M3.S14.T14.C44 b3 (7.2.Ex7) | example | printed example; q_figure for the three tile arrangements; problems_intro stays on C44. |
| Everyday Problems as Equations | Example 8: Friends at the party | Example 8 (p175) | M3.S14.T14.C45 b0 (7.2.Ex8) | example | printed example; C45 left empty. |
| Everyday Problems as Equations | Example 9: Two savings become equal | Example 9 (p176) | M3.S14.T14.C46 b3 (7.2.Ex9) | example | printed example. |
| Everyday Problems as Equations | Example 12: Sixty marbles, two boys | Example 12 (p179) | M3.S14.T14.C47 b0 (7.2.Ex12) | example | printed example; C47 left empty. Kept in this Questions topic (see judgement call 4). |
| Many Roads to One Answer | Example 10: Solving in three ways | Example 10 (p177) | M3.S16.T16.C56 b3 (7.2.Ex10) | example | printed example. |
| Many Roads to One Answer | Example 11: Riyaz's number trick | Example 11 (p178) | M3.S16.T16.C57 b3 (7.2.Ex11) | example | printed example; the kept "A Rule for Riyaz's Trick" follows it. |
| Making Equations from an Answer | Example 13: A story for 100x + 75 = 250 | Example 13 (p180) | M3.S19.T19.C66 b3 (7.2.Ex13) | example | printed example; open (many valid stories) but with the book's solution. Placed after the kept "Chains Going Up". |
| Mind the Mistake, Mend the Mistake | Mend the Mistake, box 1 | 7.3 box 1: 4x + 6 = 10 ... (p181) | M3.S22.T22.C73 b4 (7.3.M1) | exercise | printed box with its own block, steps and answer. |
| Mind the Mistake, Mend the Mistake | Mend the Mistake, box 2 | 7.3 box 2: 7 − 8z = 5 ... | C73 b5 (7.3.M2) | exercise | same. |
| Mind the Mistake, Mend the Mistake | Mend the Mistake, box 3 | 7.3 box 3: 2v − 4 = 6 ... | C73 b6 (7.3.M3) | exercise | same. |
| Mind the Mistake, Mend the Mistake | Mend the Mistake, box 4 | 7.3 box 4: 5z + 2 = 3z − 4 ... | M3.S22.T22.C74 b2 (7.3.M4) | exercise | same. |
| Mind the Mistake, Mend the Mistake | Mend the Mistake, box 5 | 7.3 box 5: 15w − 4w = 26 ... | C74 b3 (7.3.M5) | exercise | same. |
| Mind the Mistake, Mend the Mistake | Mend the Mistake, box 6 | 7.3 box 6: 3x + 1 = −12 ... | C74 b4 (7.3.M6) | exercise | same. Boxes 7 to 9 follow from the split below. |
| A Pinch of History | Example 16: Price of one horse | Example 16 (p183) | M4.S24.T24.C79 b3 (7.4.Ex16) | example | printed example; the teaching concept keeps its debt-as-negative text. |

## New questions made by splitting an existing question concept (34 parts, 10 splits)

Each block of these concepts is a self-contained question (own stem, steps, answer, coverage id), so each becomes a concept of its own; the first part of each split keeps the old video, objective and images ("covers only part: refresh"), the others have no video. Tier exercise throughout.

| Split concept (Questions topic after) | Parts, book label | Why one part per block |
|---|---|---|
| M2.S9.T9.C24 (Trial and Error) | Chapter Exercises, Q1 (a), (b), (c): fill in the blank with an integer (p185) | three separate blanks, three ids |
| M2.S11.T11.C32, C33 (Solving Step by Step) | Solve and Check, Q1 (a) to (e): "Solve these equations and check" (p172) | five equations, five ids; the plan had filed them 3 + 2 under one name |
| M2.S13.T13.C39, C40 (Moving Across) | Unknowns Everywhere, Q2 (a) to (g): "Find the value of each unknown" (p181) | seven equations (4 + 3) |
| M2.S13.T13.C41, C42 (Moving Across) | Chapter Exercises, Q18 (a) to (h): "Solve these equations" (p188) | eight equations (4 + 4) |
| M3.S21.T21.C70 (Building Equations) | Unknowns Everywhere, Q6 (a) to (e): "Given 4k + 1 = 13, find ..." (p181) | five separate values |
| M3.S23.T23.C76 (Mend the Mistake) | Mend the Mistake, box 7, 8, 9 (p182) | three printed boxes |
| M3.S23.T23.C77 (Mend the Mistake) | Chapter Exercises, Q11 (a), (b), (c): "Identify and correct any mistakes" (p187) | three separate solutions |

## Kept as they are (35 existing question concepts, listed in book order)

Unknown Weights: mobiles 4 and 5, Unknown Sacks 1 and 2, 3 and 4; Two Hundred Sticks?, Frame the Mobiles and Scales, Frame Five Equations, Q3, Q16 (two figures); Trial and Error on 5x − 4 = 7, Q4 (a), Q4 (b), Q5; Solve and Check Q2; Chapter Exercises Q19; Q2, Q6, Q7, Q8, Q9, Q12, Q20; A Rule for Riyaz's Trick, Unknowns Everywhere Q3, Q4, Q5, Chapter Exercises Q15, Q17; Chains Going Up, Unknowns Everywhere Q1, Chapter Exercises Q10, Q13; Brahmagupta's Rule on Two Equations, on 2x + 3 = 4x + 5, Chapter Exercises Q14. Kept entries whose printed question depends on a picture carry q_figure (mobiles, sack scales, matchstick sequence, frame task, blobs, both stick patterns, three machines, window grill, two triangles, path puzzle, the two chains), with s_figure for the mobiles, sack scales and the path puzzle.

## Borderline, not moved

* Mobiles 6 and 7 framed with e and y (7.1.frame_mobiles, C9 b3, p168): the book's own working for "frame equations for Fig 7.6 to 7.11"; the printed task itself (mobile 8 and the sacks, then solve and check) is the kept concept C12. Folding the two would need C12 moved whole, which its objective blocks.
* "Solve 5x − 4 = 7 and check" (C28 b3, p170 to 171), "11y + (−5) = 61 long way and short way" (C35 b3), "6y + 7 = 4y + 21 the short way" (C36 b0), "What happens in cases like u/15 = 6?" (C37 b3, p173): narrated working with the answer printed in the next lines, no plan question id; the same equations appear as real Figure it Out items (5x - 4 = 7 trial, Q1 (a) to (e)).
* "Write equations whose solution is y = 5" (C65 b3, p179): open task, the book prints two answers at once and moves to the chains; the real question about the chains is the kept "Chains Going Up".
* Ancient notation table (C78 b3, p183) and the 650m + 4000 = 500m + 5050 calculation (C80 b3, p184): table and worked illustration, not put to the reader. The tasks the book does put there (3, −6, 2, 4 and 2x + 3 = 4x + 5) are the kept concepts.
* Math Talk and discussion with no block: "Discuss the answers with your classmates" (p165), "Why can we do this?", "Is this the same as dividing both sides by 7?" (p169), "will it still preserve equality?" for 15 + 8 = 23 (p169; the plan holds only an authored predict block), "Share the equations you made" (p179), the Note to the Teacher, the history paragraphs.
* "A Magic Trick" (summary page, C85 b7, ref summary.trick): has a block with steps and answer but sits in the Summary topic, which the engine cannot use as a source; left as it is. Likewise the plan-made (authored) blocks stay: the four summary examples in C85, the four ready checks in C1 and the authored "common slip" example in C73 b3.

## Gaps (book questions the plan has no block for)

None. All 20 chapter-end items, 7.1 Q1, Q2, 7.2 Q1 to Q6, Example 1 to 13 and 16, and the nine boxes have a block. (The tangram sheet pages at the end are cut-out material, not questions.)

## Judgement calls

1. **Parts of a Figure it Out question became separate concepts** (the 34 split parts), as the task asked. The brief also says a multi-part question stays one concept; here every part has its own full stem, steps, answer and coverage id, and the plan had already split Q1, Q2, Q18 across two concepts each, which the engine cannot merge back. If one concept per printed number is preferred, drop those `split` entries, keep the concepts and add canon entries folding each concept's part ids into its first (no content change): about 24 fewer new videos.
2. **One printed task spread over several plan concepts stays as the plan grouped it**: "Find the unknown weights in the following cases" (Fig 7.1 to 7.8) is three concepts (1 to 3, 4 and 5, 6 to 8), the sacks two, Q16 two (one per figure). The kept ones carry objectives, so they cannot be folded into one question.
3. **In-text prompts are tier prompt, Mend the Mistake boxes tier exercise**, the Examples tier example.
4. **Example 12 (marbles) stays in the "Everyday Problems" Questions topic** though the book prints it after Example 10 and 11; it is a word problem and the plan puts it with Example 7 to 9. The 7.2 Figure it Out items are filed under the plan's topics (Q2 under Moving Across, Q3 to Q5 under Puzzles and Tricks, Q1 and Q6 under Building Equations) although the book prints them together after Example 13.
5. **Only the question id of each folded group stays on the question**: Q_other_solution folded into Q_ways_n, Q_check_ex5 into Ex5. Descriptive ids on the same block (intro, trial, balance_property, same_op, check_note, problems_intro, matchsticks) stay on their teaching concepts, so no book item loses coverage.
6. **Figure sentences** are written only where the printed question needs a picture. The q_figure for the two chains repeats the printed equations, including the last line of each chain, because the question card must draw the chains as printed.
