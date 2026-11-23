# Chunk B notes (Class 5 Ch 13 "Animal Jumps", cbse_eng_maths5_ch13_v4)

Units: M2.S11.T11 (Let Us Do Q3 to Q7), M2.S12.T12 (Mowgli's trail: jumps of 3, 5, 10), M3.S13.T13 (two worked examples), M3.S14.T14 (Let Us Do Q8 to Q11). 26 items: required 13 / optional 1 / none 12. Validator: errors 0, one warning (C50 worked example has no printed book figure, expected).

Required: questions C33, C39, C43, C45, C47, C58; solutions C34, C40, C44, C46, C48, C59; worked example C50 (media id C50.IMG2, because the kept teaching image is C50.IMG1).
Optional (not added): C56 question. None: C35, C36, C37, C38, C41, C42, C49 (worked), C52, C53, C54, C55, C57.

Specs are drawn on a 16 by 9 unit canvas (120 px per unit) with explicit coordinates; every coordinate was checked in code for overlaps and off-canvas text, and previewed once.

## 1. Judgement calls

- **The Q3 trail picture (book p.4) is used by four question diagrams** (C33 Q3, C43 jumps of 3, C45 jumps of 5, C47 jumps of 10) with identical specs (one diagram per item). The three follow-up questions on p.5 print no picture of their own and never name the trail or Mowgli, and the friends' places exist only in that picture, so each needs its own copy (rule: needed to attempt; decision 5). Their `render_note` says "same as M2.S11.T11.C33.IMG1".
- **Question trail figures leave out the book's red numbers (4, 12, 26, 50) and blue boxes (9, 21, 39, 57).** Those marks are the book's printed answers for jumps of 2 and 3; a question figure must not leak the answer.
- **Trail solutions C34, C44, C46, C48 are all required**: jumps of 2 and 3 because the book prints the answer as marks on the picture (B2), jumps of 5 and 10 by sibling consistency (same kind of answer, same picture). Each shows the landing stones in ANSWER green and rings (FOCUS) the friends reached; derived_from the question diagram.
- **Q10 (C56/C57) differs from the other trail items on purpose.** The question names all four house numbers (Kaa 21, Sher Khan 25, Baloo 30, Akela 35) in its text, so the trail is not needed to attempt it: question `optional` (not added; the trail with those four houses would help). The solution answer is a list of jump sizes (2, 3, 6, 10, 15, 30 and 1, 7), not a picture: `none`.
- **Q6 (C39/C40)**: question required (the six numbers 0, 10, 16, 27, 36, 48 are only on the line). Solution required: 12 hops of 4 from 0 to 48, 16, 36, 48 ringed, 10 and 27 crossed (WRONG colour; the LP says they are skipped). The line is drawn exactly to scale (the book's is only roughly proportional).
- **Q11 (C58/C59)**: question required (15 cards and the empty Venn are given in the book, the learner sorts into them); solution required (filled Venn is the answer, B2). In the solution the cards stay where they are (rule 3, never move given parts) and the numbers are added inside the regions in ANSWER green. Labels use the wording of the question parts ("Divisible by 2 only" ...), written on two lines.
- **Worked example C50 (sort 16, 35, 60, 48, 85, 70)**: required, one diagram, drawn as the completed sort (2 only: 16, 48; 5 only: 35, 85; middle: 60, 70; 10 only empty). This is the sibling of Q11 and the user's decision 5 (own diagram even though teaching image IMG1 shows the same sort). Unlike a normal question figure it shows the worked result and not only the given state, because the example's question gives no figure of its own and its answer is the arrangement. If you would rather have `none` for this example, flip it: no other item depends on it.
- **C49 worked (checking statements)**: none. Lists of multiples and products are text; the book prints no figure for Q8.
- **C36 (Q4 answers)**: none. The earlier author's hint (two factor lists with the six common ones circled) is a layout of numbers that LaTeX handles (boxed or coloured numbers).
- **C55 (Q9 answer)**: none. The LP says "like the start of a number line", but the answer is the list 15, 30, 45, ...; a two-colour number line would be nicer, not needed.
- Figure inventory: `P04-number_line-1` is mapped to its first use (C33 question); each further use (the solution figures, the three follow-up questions) has its own `NEW-P04-number_line-1-<suffix>` entry, and the Q10 use is `none:TEXT_SUFFICIENT`. `P07-number_cards-1` and `P07-venn-1` are each claimed by C58 (question) and a NEW entry for C59 (solution). Nothing else of chunk B's book pages carries a figure. The base descriptions were checked against the page pictures (pp.4, 6, 7) and need no correction.

## Borderline (v3 rules applied as written, text carries the numbers)

- C34, C44, C46, C48 trail solutions: the LP text lists every landing and friend, but the answer is marked on the picture in the book (jumps of 2 and 3) and the siblings follow.
- C40 solution (hops on the Q6 line): the answer is a list of three numbers; kept required because the task is to jump along the given line and the solution adds the hops and skipped numbers.
- C43, C45, C47 questions required although the p.5 book questions print no new picture.
- C58 question required although the LP text lists the 15 numbers.
- C50 worked example required (see above).
- C56 question optional and C57 solution none although the earlier author's hint `s_figure` suggests "jumps of 6 marked, landing on 30 and skipping 25" (one example of the check, not the whole answer).

## 2. LP text issues (not edited, listed only)

- **M2.S12.T12.C43, C45, C47 (questions):** the text says "his friends" and "he" with no antecedent and no trail. Suggested: "Mowgli's friends live along the trail above. Which of his friends will he be able to meet if he jumps by 3 steps? 3 is a common factor of the numbers ___." (same for 5 and 10; for C45/C47 "Which numbers will he touch if he jumps by 5 steps? ___ ").
- **M2.S11.T11.C39 (question):** the numbers to test are missing from the text (only the picture has them). Suggested: "Find which of the following numbers can be reached by jumps of 4 steps: 0, 10, 16, 27, 36, 48. 4 is a common factor of the numbers ___."
- **M3.S14.T14.C58 (question):** the text lists the 15 numbers but never says they are sorted into the three circles. Suggested: add "Write each number in the right part of the three circles."
- **M2.S11.T11.C34 / C44:** the LP answers (ant, frog, bird, Baloo, rabbit for jumps of 2; spider, frog, Kaa, Baloo, deer, monkey for jumps of 3) are correct. The book's own sentences are shorter: p.5 names only 4, 12, 14, 50 for jumps of 2 and only 9, 21, 39, 57 for jumps of 3 (it leaves out Baloo 30, and 12 and 30). The LP is right; no change needed.
- **All pair solutions (cards removed):** the old `text` fields still carry `[Image: ... solution]` and `[Image: ... solution (continued)]` markers inside the steps (for example after step 3 of C34). The v3 token goes before step 1 in steps_tex; the builder should drop the old markers.
- **M3.S14.T14.C56 (question):** "What number of jumps (in steps) he could choose" is the book's own wording; the LP keeps it. Fine, only awkward.
- **M2.S11.T11.C42 (Q7):** the LP numbers the nine pairs (a) to (i); the book prints (f) twice (12 and 15, then 20 and 5), (g) 9 and 21, (h) 6 and 27. The LP's lettering is the correct one.

No arithmetic error was found in the LP solutions of this chunk (all factor lists, multiples and sort lists re-checked).

## 3. Where the book is unclear or wrong (specs show the corrected value; the base inventory keeps what is printed)

- Q3 trail: the last stone is printed **59 twice** (61 dots); the LP says the trail ends at 60, so all trail specs show 60. This is also why the trail has 61 stones, 0 to 60.
- Q3 trail: the red number **26** sits beside the tiger, but the p.5 sentence says the positions for jumps of 2 are 4, 12, **14** and 50 (the bird's nest is at 14, printed black). The solution figure for jumps of 2 rings the bird at 14, and Sher Khan stays on 25 (as Q10 says).
- Q3 trail: the tiger is drawn over stones 25 and 26; Q10 and the LP put Sher Khan's house on 25, so the tag is on 25.
- p.5: the blue boxes and the sentence for jumps of 3 list 9, 21, 39, 57 and leave out 12 (frog) and 30 (Baloo), which are multiples of 3; the LP and the figure include them.
- Q6: the six ticks are only roughly proportional in the book; drawn to scale. The line shows 0, which the LP treats as the starting place, not as a number reached.
- Q9: "start on the same day" is taken as day 0 (LP wording); the first meeting is day 15.
- Q7: duplicate letter (f) in the book (see LP text issues).
- Book picture on p.7 has a faint "NCERT not to be republished" watermark crossing the Venn diagram; it is not part of the figure and the specs leave it out.
