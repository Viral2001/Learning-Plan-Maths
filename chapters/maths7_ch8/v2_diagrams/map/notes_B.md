# Chunk B notes (Class 7 Ch 8, units 20-42)

Result: 32 items = question 0 required / 0 optional / 9 none; solution 1 required / 1 optional / 7 none; worked example 0 / 0 / 14 none. 14 base figures claimed: 0 to items, 2 to the concept image M1.S14.T14.C63.IMG1, 12 `none`. Validator: errors 0, one warning (the required item has no printed book figure, see 1a).

## 1. Judgement calls

a. **M1.S13.T13.C56 (Figure it Out 8.1 Q4, saplings) solution: REQUIRED, the only diagram of the chunk.**
   The book prints no picture; it only hints "Draw a rough diagram with four saplings...". The LP solution's first step is "Draw four saplings in a row: there are 3 gaps between the first and the last". The usual slip is 4 x 3/4, so the picture changes how correctly the student solves it (tie-breaker). Question side `none` (the book gives no figure; no question diagram when none is given). The spec is a row of 4 saplings, three gaps labelled 3/4 m, a bracket 9/4 m in ANSWER green. `derived_from` null. The validator warns that no base figure maps to it; that is true and expected.

b. **M1.S13.T13.C52 (Figure it Out 8.1 Q2, Somu's land) solution: OPTIONAL, not added.** A bar cut into 36 equal parts (road 6, Krishna 15, Bora 10, Somu 5) would show the shares clearly. The subtraction 30/36 - 15/36 - 10/36 = 5/36 in the steps is complete, so it is not needed.

c. **Cancelling and reciprocal "annotated expressions" (P10-ann-2, P11-ann-1, P11-ann-2, P15-ann-1/2, P16-ann-1/2) -> none (LATEX_ARITHMETIC).**
   They are fraction arithmetic with strike-throughs, circles and boxes. The LP steps already say in words which numbers cancel and what they become, and topic T11 has a cancelling tool and videos, T17 has videos and a practice tool. HIGHLIGHT_MEANING was considered (the black pair and the red pair in P11-ann-2), but nothing is lost without the colours because the pairs are named in the text. The LP text uses no `\cancel` anywhere; if the content team wants strike-throughs they can add them in LaTeX.

d. **Dividend / Divisor / Quotient callouts (P14-labelled_expression-3, P16-labelled_expression-3) -> none (TEXT_SUFFICIENT).** They only name the parts of one division. The worked examples C69 and C74 do not need the labels to be solved (C74's steps name "divisor", "dividend" and "reciprocal" in words).

e. **M2.S18.T18 (Figure it Out 8.3 Q1, Evaluate) both sides none, although the printed answer (P37-table-1) is a table.** It is a plain boxed grid: no colour, no meaning in cell position, two empty boxes. B2 "printed answer is a picture" is aimed at arrangements; this is a LATEX_TABLE / NUMBER_LIST_IN_BOXES case. The question text already lists (a) to (j) and the LP solution has all ten results with working.

f. **M1.S14.T14.C63 (order of multiplication, worked) -> none (TEXT_SUFFICIENT + REUSES_CONCEPT_IMAGE).** The picture the example talks about (two unit squares with a 1/8 rectangle, one turned) is already the kept teaching image M1.S14.T14.C63.IMG1 in the same concept (P14-fraction_grid-1/-2 map to it). The example question needs no figure to be solved, and a second copy in the same concept adds nothing. If the reviewer wants an own diagram anyway, the spec would be the same two-square picture: it was not written because the item does not need it.

g. **Three-situations worked examples (C59, C60, C61) -> none.** The book's Situation / Multiplication / Relationship table (P13-table-1, red outline, pink header) is plain text, no colour meaning: LATEX_TABLE. A number line placing the product between or beyond the two numbers would help a little, but the book has none and the text (twentieths for C60) is exact, so nothing is marked optional.

h. **Sibling consistency in Figure it Out 8.1 Q1-Q5:** Q1, Q2, Q3, Q5 solutions are arithmetic, so none (Q2 optional, see b); Q4 differs because its solution step is itself a drawing (see a). The questions are all none (word problems, no given figure).

i. **Practice duplicates:** M1.S12.T12 (12/7 x 5/24) is decided like the worked example C44 (none on both sides).

## 2. Things in the LP that look wrong or odd

- M1.S16.T16.C67/C68 carry `book_number` "Figure it Out 8.3, Q1" but the question is Q9 of the 8.3 Figure it Out (book p.25, answer "(a), (c) and (e)"); the real Q1 is the Evaluate grid in M2.S18.T18.C76/C77, which has the same label. Two different questions are both called "Figure it Out 8.3, Q1".
- M1.S13.T13 labels its five questions "Figure it Out 8.1, Q1" to "Q5"; section 8.1 has three Figure it Out sets (Tenzin, unit squares, and this tank set from book p.11-12), so "Q1" repeats earlier labels. The book prints "Try This" beside part (e) of the tank question; the LP drops it (harmless).
- M1.S13.T13.C55 question text omits the book's hint "[Hint: Draw a rough diagram with four saplings with distance between two saplings as 3/4 m]". The solution step 1 ("Draw four saplings...") assumes it. Consider adding the hint sentence to the question text.
- M1.S12.T12.C47 asks 12/7 x 5/24, the very sum already worked in the teaching concept M1.S11.T11.C43 (book p.10-11). So the "question" repeats the lesson's example.
- M2.S17.T17.C73 ("Find 2/3 / (3/5)") and C74 ("Find 2/3 / (3/5) using the reciprocal") are the same sum with the same answer 10/9, as in the book (p.16 and p.17); two worked examples for one sum.
- No contradiction between LP solutions and the book's printed answers in this chunk (all values rechecked: 7/30, 7/15, 21/40, 49/100, 10/7; 5/6, 5/12, 5/18, 5/36; 36 sq ft; 9/4 m; 600 g against 400 g; the ten quotients; 6 / 22 1/2 for the fill-in-the-blanks). The LP only adds mixed-number forms (1 3/7 hours, 2 1/4 m, 4 1/2, 1 1/9).

## 3. Places where the book is unclear

- The Evaluate grid (book p.24, answers p.37) has two empty boxes (row 2 column 4 and row 3 column 4) and no instruction for them (probably for the student's own sums). The LP lists only the ten given expressions.
- Q4 saplings: the book gives a hint to draw but prints no figure, so the spec follows the LP text (four saplings, three gaps of 3/4 m); no spacing in the book to copy.
- The base description of every figure in this chunk was checked against the page pictures (pages 10, 11, 13, 14, 15, 16, 24, 37): no correction was needed.
