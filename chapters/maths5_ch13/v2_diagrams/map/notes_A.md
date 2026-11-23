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
