# Class 5 Ch 13 Animal Jumps - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths5_ch13` v4 (taken from staging). Result: new V2 version v5 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (52 items from 31 units)
{"worked_example": {"none": 7, "required": 3}, "question": {"required": 10, "none": 10, "optional": 1}, "solution": {"required": 10, "none": 8, "optional": 3}}

Optional, NOT added: [('C16', 'solution'), ('C18', 'solution'), ('C25', 'solution'), ('C56', 'question')]

needs_lp_text_sync: []

## The 23 diagrams
| id | side | type |
|---|---|---|
| M1.S3.T3.C5.IMG1 | question | arrow_map |
| M1.S3.T3.C6.IMG1 | solution | arrow_map |
| M1.S4.T4.C7.IMG2 | worked example | cell_grid |
| M1.S4.T4.C9.IMG2 | worked example | cell_grid |
| M1.S5.T5.C11.IMG1 | question | cell_grid |
| M1.S5.T5.C12.IMG1 | solution | cell_grid |
| M2.S8.T8.C22.IMG1 | question | number_line |
| M2.S8.T8.C23.IMG1 | solution | number_line |
| M2.S9.T9.C28.IMG1 | question | grid_map |
| M2.S9.T9.C29.IMG1 | solution | grid_map |
| M2.S11.T11.C33.IMG1 | question | other |
| M2.S11.T11.C34.IMG1 | solution | other |
| M2.S11.T11.C39.IMG1 | question | number_line |
| M2.S11.T11.C40.IMG1 | solution | number_line |
| M2.S12.T12.C43.IMG1 | question | other |
| M2.S12.T12.C44.IMG1 | solution | other |
| M2.S12.T12.C45.IMG1 | question | other |
| M2.S12.T12.C46.IMG1 | solution | other |
| M2.S12.T12.C47.IMG1 | question | other |
| M2.S12.T12.C48.IMG1 | solution | other |
| M3.S13.T13.C50.IMG2 | worked example | other |
| M3.S14.T14.C58.IMG1 | question | other |
| M3.S14.T14.C59.IMG1 | solution | other |

### Chunk A notes (from the decision agent)
# Chunk A notes: Class 5 Ch 13 "Animal Jumps" (cbse_eng_maths5_ch13_v4)

Result: 26 items (8 worked examples, 9 pairs). required 10, optional 3, none 13. Validator: errors 0 (2 warnings: the worked examples C7 and C9 draw arrays of 18 / 19 / 21 tiles that the book does not print, so no base figure maps to them).

| Concept | Role | Decision | Diagram |
|---|---|---|---|
| M1.S2.T2.C3 | worked | none | text suffices |
| M1.S3.T3.C5 / C6 | question / solution | required / required | function box (x ?) / box with x 4 and 7, 9, 12, 18 going in |
| M1.S4.T4.C7 | worked | required (IMG2) | arrays 1x18, 2x9, 3x6 |
| M1.S4.T4.C8 | worked | none | arithmetic |
| M1.S4.T4.C9 | worked | required (IMG2) | arrays 1x19; 1x21, 3x7 |
| M1.S5.T5.C11 / C12 | question / solution | required / required | array 3x5 with Factors / Multiple; plus the 1x15 row |
| M1.S5.T5.C13 / C14 | question / solution | none / none | blanks, arithmetic |
| M1.S5.T5.C15 / C16 | question / solution | none / optional | why 13 and 37 are prime |
| M1.S6.T6.C17 / C18 | question / solution | none / optional | arrays of nine numbers |
| M2.S7.T7.C19, C20 | worked | none, none | lists of multiples |
| M2.S8.T8.C22 / C23 | question / solution | required / required | number line 0-13 with jumps of 3 and 4 / continued to 48 |
| M2.S8.T8.C24 / C25 | question / solution | none / optional | two lists with common multiples circled |
| M2.S9.T9.C26 / C27 | question / solution | none / none | arithmetic |
| M2.S9.T9.C28 / C29 | question / solution | required / required | cobbled road 0-64 / road with Robby's and Deeku's landings |
| M2.S10.T10.C30, C31 | worked | none, none | text suffices |

## (1) Judgement calls

- **C5 / C6 (hidden-numbers box), both required.** The book question is the picture of the box ("this box", "the 4 numbers coming out of the box"). The LP text repeats the four numbers, but under user decision 4 that alone does not turn a figure the book gives into none. Question figure: box marked "x ?", empty IN arrow, four out-tags 28, 36, 48, 72 (the five faint grey numbers of the book's shadow patch are decoration and not drawn). Solution figure: the LP's sample answer, multiplier 4 with 7, 9, 12, 18 going in (7x4 = 28, 9x4 = 36, 12x4 = 48, 18x4 = 72).
- **C7 and C9 (worked arrays), required; C8 (44 is a multiple of its factors), none.** C7 ("make every array of 18") and C9 ("how many arrays with 19 and 21 tiles") have an arrangement of tiles as the answer, which the steps only describe in words (B2, ANSWER_IS_FIGURE), so each gets its own diagram although a teaching image shows the same arrays (user decision 5). C8 asks to show a multiple by multiplication and division; no array has to be made (and 1 x 44 would be a 44-tile row), so it stays arithmetic.
- **C11 / C12 (arrays of 15).** The book gives the 3 x 5 array with the Factors / Multiple labels and asks for other arrays; the LP text does not carry the array (its solution says "the array in your maths book"), so the question figure is required. The solution adds the 1 x 15 row in ANSWER green (5 x 3 is 3 x 5 turned round, not drawn as a second array) and lists the factors 1, 3, 5, 15. Tile size is the same in both arrays (60 px).
- **C13 / C14 (12 is a multiple of its factors).** Four fill-in-the-blank multiplications; no figure in the book; none / none.
- **C15 / C16 (why 13 and 37 are prime).** Question none. Solution optional (not added): the answer is a reason; single-row arrays of 13 and 37 tiles would help but the tie-breaker says the text carries it. Picture that would help: the two single-row arrays 1 x 13 and 1 x 37.
- **C17 / C18 (Let Us Do, arrays for 10, 14, 13, 20, 25, 32, 37, 46, 54).** Question none (no figure given). Solution **optional, not added**, although B2 would make it required ("Answer is an arrangement"). Reason: the answer is 20 arrays for nine numbers (one is 54 tiles in a row); the pair may carry only one solution picture, the LP does not split the question into parts and v3 forbids a combined picture of several parts. A readable single picture is not possible. **User decision needed**: split C17/C18 into per-number items (or at least 54 and 32, 20) if pictures are wanted.
- **C19, C20, C30, C31 (worked examples with a teaching image), none.** Each is lists of multiples or factors in the steps; a careful student loses nothing without a picture (tie-breaker). The teaching images of these concepts (number lines, factor chips) stay and are not linked. I did not drop them because of the teaching image (decision 5); the reason is text sufficiency. Flip to required if you want each worked example to carry its own number line.
- **C22 / C23 (more common multiples of 3 and 4).** Question required: "you can continue the number line" refers to the book's line with the frog's jumps of 3 and the rabbit's jumps of 4 meeting at 12. Solution required: the line continued to 48, with 12, 24, 36, 48 boxed. Layout choices: both jump families are above the line (as in the book); the solution has 35 px tick spacing, so the numbers sit in three tiers (frog only, rabbit only, both) to keep 15 and 16, 27 and 28 and so on apart; arcs keep SET_A / SET_B for both animals and ANSWER green marks the new common multiples 24, 36, 48. The LP answer also says 60, which lies beyond the line (arrowheads show it goes on).
- **C24 / C25 (multiples of 4 and 6).** Question none: the two lists and the sentence "12 and 24 are common multiples" are in the question text. Solution optional (not added): two lists with 12, 24, 36, 48 circled would help, but LaTeX can box the numbers reliably (so HIGHLIGHT_MEANING does not force a picture).
- **C26 / C27 (five common multiples of nine pairs).** No figure in the book, answers are sample lists; none / none.
- **C28 / C29 (cobbled road).** Question required: the 65 stones numbered 0 to 64 and the food after 64 exist only in the picture. The book's irregular four runs are simplified to four equal rows (17, 16, 16, 16 stones, turns 16-17, 32-33, 48-49); stone numbers and their order are exactly the book's (checked 0 to 64 on the page picture). The rabbit, deer and food drawings are replaced by the word "Food". Solution required, derived from the question picture: Robby's landings (16 stones, SET_A dot), Deeku's landings (10 stones, SET_B dot), ANSWER outline on the five stones where both land (12, 24, 36, 48, 60), FOCUS outline on stone 64 (only Robby), and Deeku's jump from 60 over the end to 66 (dashed arc, "66" in WRONG, drawn beyond the road because the LP solution says Deeku "jumps past 64 to 66").
- **Figure inventory choices.** P01-array-2 (arrays of 12, teaching) and P03-number_line-1 (spider / grasshopper, teaching) have no item in this chunk: they are accounted to the LP's teaching counterparts M1.S4.T4.C7.IMG1 and M2.S7.T7.C20.IMG1 (same kind of figure with other numbers; accounting only, nothing linked). P03-number_list-1 (circled lists) is none:TEXT_SUFFICIENT because the LP question text carries both lists. Four solution figures that redraw a printed book figure are second uses and are listed as NEW-<base id>-sol (function box, array of 15, number line, road).
- Aspect ratio 16:9 for all ten diagrams. Diagram types used: arrow_map, cell_grid, number_line, grid_map.

## (2) LP text issues

- **M1.S5.T5.C11** - the question text does not say what the given array is (3 rows of 5, 3 x 5 = 15, with 3 and 5 as factors, 15 as the multiple); the new picture carries it. Suggested sentence: "The picture shows an array of 15 tiles in 3 rows of 5, so 3 × 5 = 15." **M1.S5.T5.C12**, step 1: "The array in your maths book" should read "The array in the picture".
- **M2.S9.T9.C28** - the question text does not say the road ends at stone 64 (only the picture and the solution step 1 say so). Suggested sentence: "The stones of the road are numbered 0 to 64 and the food is at the end of the road, after stone 64."
- **M2.S8.T8.C22** - "You can continue the number line" has no number line in the text. Suggested sentence: "The number line shows a rabbit jumping 4 at a time and a frog jumping 3 at a time from 0; they first land together on 12."
- **M1.S3.T3.C5 / C6** - "this box" refers to the picture only. Suggested sentence: "A box multiplies every number that goes in by the same hidden number." (the four out-numbers are already in the text).
- **M2.S8.T8.C23** - the LP answer lists "24, 36, 48, 60"; the picture stops at 48 (60 is named in step 4). Fine, but the answer line could say "(the line stops at 48)" if the reader looks for 60 on the picture.
- **M1.S6.T6.C18** - the earlier card hint (s_figure) described only the arrays of 54; the answer covers nine numbers (see judgement call on C17 / C18).

## (3) Book unclear or wrong

- p.3, Let Us Do Q1: the book letters the pairs (a), (b), (c), (d), (e), (f) and then (f), (g), (h) again (a print slip: "(f) 9 and 12" and "(f) 8 and 12"); the LP letters them (a) to (i). No diagram depends on it.
- p.3: the book prints "Multiple of 6" (missing s) in the lists; the LP writes "Multiples of 6". No effect.
- p.1 hidden-numbers box: the five faint grey numbers in the shadow patch (read as 12, 4, 7, 18, 6) are low-contrast decoration; checked on a 3x enlargement, they are not part of the question and are not drawn.
- p.4 cobbled road: the turns at the right end (stones 16-19, 51-54) are drawn irregularly in the book; the numbers and their order are consistent 0 to 64 with no gaps. The simplified four-row layout is a redraw, not a measurement.
- This pdf has no printed-solutions section: every solution picture is derived from the LP solution text (sample answers where the LP gives one).

## Borderline

- **C5 (required)**: LP text carries all four numbers; kept because the book question is the picture of the box.
- **C6 (required)**: the sample-answer box with the in-numbers; the answer could be read as only numbers.
- **C3, C8, C19, C20, C30, C31 (none)**: a picture would help a little, text suffices.
- **C16, C18, C25 (optional, not added)**: see judgement calls; C18 breaks the B2 "answer is an arrangement" rule only because nine numbers cannot share one picture.
- **C12 and C23 (required)**: the solution adds one array / the continued line to a figure the question already shows.
- **C29 (required)**: the answer ("only Robby reaches the food") could be argued in text, but the marked landings on the given road are the evidence.

### Chunk B notes (from the decision agent)
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
