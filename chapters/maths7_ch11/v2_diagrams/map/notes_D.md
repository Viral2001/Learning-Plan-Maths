# Chunk D notes (Class 7 Ch 11, cbse_eng_maths7_ch11_v30)

Units 52 to 69 = topics T37 (Figure it Out Q1-Q7), T38 (3 worked examples), T39 (Figure it Out Q8-Q13), T40 (2 worked examples of the review).
31 items: required 2, optional 0, none 29. Validator: errors 0, warnings 0.

## 1. Judgement calls

- **T37 Q1 (stars), question: required.** The book prints two rows of 12 stars (checked on page 17: row 1 yellow, green, orange, blue, pink, grey twice; row 2 green, orange, yellow, blue three times; ellipsis after each). The LP question says "the two rows below ... as shown" and only spells the colours out in a bracket, so without the picture "below" points at nothing. Tie-breaker kept it required (FIG_REFERENCED, DATA_IN_FIGURE). The bracket text in the LP stays; it just repeats the picture.
- **T37 Q1, solution: required, derived_from the question diagram.** The question picture stops at 12 stars; the answer is the 16th star. The solution figure is the whole final state: both rows to column 16, columns numbered 1 to 16 (ANSWER), FOCUS boxes round columns 4 and 16 (both rows blue). Columns 1 to 12 keep the same x, y and colours as the question figure, so the question card is left-aligned with empty space on the right. I did not mark the other blue stars (row 1 col 10; row 2 cols 8, 12): the colour already shows them and the boxes would lose their point.
- **Star colours are not style tokens.** The six star colours (yellow, green, orange, blue, pink, grey) are data in the book picture, so the spec gives hex values (yellow #F4D41F, green #7BBF3A, orange #E8801E, blue #3C6DC5, pink #C768AE, grey #8C8C8C) and a 3 px INK outline (the book stars have no outline).
- **Second inventory entry `NEW-P17-pattern-1-sol`.** The solution reuses the same book picture, so by the brief's rule it is a second entry (a figure used by two items). It is not a figure printed in the book; it exists only for accounting.
- **P20-number_grid-1 (Mystery Colours, 10 x 10 ring badges) claimed by D.** It is a teaching figure of M4.S41.T41 (Puzzle Time), and T41/T42 are in none of the chunks A to D (no question items), so the merged base-inventory check would otherwise fail. Mapped `concept_image:M4.S41.T41.C171.IMG1` (Decode and draw a ring). Honest caveat: C170/C171 are small excerpts of the ring scheme, not the full 100-badge grid. If another chunk also claims it, the two entries should be reconciled at merge (either meaning, concept image, is fine).
- **T37 Q6 (box 12 x 18 x 36 and cubes): none on both sides.** The book gives no picture of the box. A cuboid sketch would be a nicety, but the question side may not invent a figure and a student solves it by divisibility. Not marked optional because the book supplies nothing to base it on.
- **T38 worked examples (C151, C152, C153) and T40 (C167, C168): none.** No figure is referred to; steps are arithmetic. C151, C153, C167, C168 already have a teaching image which stays and is never linked (v3). The cat and mouse example (C152) and the dog and rabbit question (T39 Q4, C161/C162) get the same decision (sibling consistency): story + arithmetic, no picture.
- **T39 Q8 solution: none** but with a `text_alternative`: a plain LaTeX array of multiples 420 ... 2100 against remainders 2, 4, 6, 8, 10 (LATEX_TABLE, not an image).
- **Q3, Q4, Q12, Q13 solutions (answers are factorisations, pairs, numbers, a sum): none.** The matched-subpart pictures of section 3.1 are teaching/worked-example figures owned by other chunks; the Figure it Out answers here are not pictures.

## 2. Things in the LP that look wrong

- **Book numbers in T39.** T39's concepts are labelled "Figure it Out 3.3, Q1" to "Q6" (same labels as T37's Q1 to Q6), but the book questions are Q8 to Q13 (ncert_refs end8 to end13 are correct). Two sets of Q1 to Q6 in one topic family may confuse learners and the diagram build; the map uses the LP string in `lp_book_number` and the right book number in `ncert_ref`.
- **T37 Q1 question text.** It contains the colour lists in brackets, which now duplicate the diagram (harmless; the diagram adds the rows, the bracket stays as a text alternative).
- **Worked-example blocks (C151, C152, C153, C167, C168) carry plain text only** (`question`, `steps`, `answer` with "7 - 5", "1/6", "x"), no `*_tex` fields. Not a diagram matter; whoever syncs LP text may want LaTeX there.
- Recomputed and found correct in the LP solutions: Q1 (blue at 4, 10, 16 and 4, 8, 12, 16; LCM(6,4) = 12 so 16), Q3 (HCF 21, LCM 97020; HCF 9, LCM 180), Q4 (66 = 2 x 3 x 11 pairs), Q5 (105 < 200 < 210), Q6 (HCF 6, cubes 6, 3, 2), Q7 (HCF 18), Q8 (2100; remainders 2, 4, 6, 8, 10), Q9 (72 and 36), Q10 (LCM = m x n so only c), Q11 (75 leaps, 675 = 675), Q12 (360), Q13 (LCM 1260; 672 + 63 + 245 + 220 + 60 = 1260), and the five worked examples (60; 24 leaps, 168 = 168; 5/12; 14 and 210, 2940; 1 and 120, 7 and 21, 1 and 156).

## 3. Where the book is unclear

- Figure it Out Q1: the book shows only 12 stars per row with "..."; the next meeting (16th star) lies beyond what is printed, so the solution figure extends the pattern by the stated cycle (6 and 4), as the LP solution does.
- Q9 ("Fire in the Mountain") relies on game rules that this chapter does not explain; the LP solution treats "nobody got out" as "number divisible by the called number". No figure is printed.
- This pdf has no printed-solutions section; every solution follows the LP text.
