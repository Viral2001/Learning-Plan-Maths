# Chunk C notes (Class 5 Ch 4, plan cbse_eng_maths5_ch4_v5)

Result: 32 items (15 pairs + 2 worked examples). Required 3, optional 0, none 29. Validator: errors 0, warnings 0.

Required (all three belong to the "Quick Sums and Differences" method picture of the book, p.11):
- M3.S26.T26.C86 solution (Sukanta, 32 + ___ = 100): the book's only worked answer is the picture 32 + 67 = 99, +1, 32 + 68 = 100. The question has no figure in the book, so no question diagram and `derived_from` is null.
- M3.S27.T27.C87 question (59 + ___ = 100): the book gives the same figure with two empty ovals to fill ("Try this method for the number 59").
- M3.S27.T27.C88 solution: the same figure with 40 and 41 in the ovals (ANSWER green), `derived_from` C87.IMG1.

All three use one layout: two column additions side by side, a joining arrow, and a +1 curved arrow from the left oval to the right oval (diagram_type `other`, spec complete, 16:9).

Inventory (base figures of this chunk): P10-route_diagram-1 -> none:TEXT_SUFFICIENT; P11-method_pair-1 -> C86 solution; P11-method_pair-2 -> C87 question. I added one NEW entry, `NEW-P11-method_pair-2-sol`, for the second use of the 59 figure (C88 solution). I checked all three base descriptions against the page pictures (p.10, p.11): accurate, no correction needed. The grids on p.12 and the table on p.15 are in the book sections near my units but belong to other chunks' units (grids = M3.S30/S31, table = M4.S42), so I did not claim them.

## Judgement calls

1. Colours of the method figure. The book draws the ovals and the +1 arc in lilac; FOCUS (#CC79A7) is the nearest token, so ovals, +1 arc and "+1" label are FOCUS in all three figures. Digits the solution adds are ANSWER green. In C86 (no question figure) the solution adds 67, 68 and 99; the top number 32 and the target 100 given in the question stay INK. In C87/C88 the book prints 99 and 100 in the question figure, so they stay INK (the question figure therefore shows "99", exactly as printed).
2. C85 (Sukanta question): none. The book prints only the equation on p.10; Piku's picture is on p.11 and answers it. A question with no given figure gets no question diagram.
3. C87 question is `required` (ACTION_ON_FIGURE, FIG_REFERENCED), although a student could do 59 + 41 from the text. The book gives the figure to be completed and says "Try this method", so the figure is the way to attempt it (user decision 4: not flipped to none).
4. C89-C96 (877/666/4,103/5,555; 180/760/400; subtract 9 or 99; get 9 or 99): none. The book prints no figure for them, only equations with blanks, and the answers are numbers. Sibling consistency with C87/C88: the book prints the method picture only for 32 (answer) and 59 (given), so this is a stated difference, not an oversight.
5. Journey/word problems (C71-C82), palindrome lists (C99-C104): none. Column arithmetic and lists stay LaTeX/text.
6. The old two-card solutions (C74, C76, C90, C92, C94, C104 each had IMG1 and IMG2) all become `drop_image`. Their `text` fields still hold two "[Image: ...]" markers each (one after a middle step, one "(continued)" after the answer); the builder must drop those markers.

## Borderline

- M2.S23.T23.C71 (Mary, question): the book gives a route sketch (Delhi top left, Varanasi, Kolkata bottom right, with 1,275 / 2,645 / 3,275). I chose none (TEXT_SUFFICIENT): every amount and the order of the trip are in the question text, no v3 trigger applies (no "in the figure", data not only in the picture). If the user wants the book figure, it would be a route line Kolkata -> Varanasi -> Delhi with the three spending amounts; ask and I will write the spec.
- M2.S23.T23.C72 (Mary, solution): none (LATEX_ARITHMETIC). A running-balance route (12,540 -> 9,265 -> 14,165 -> 11,520 -> 10,245) would be optional at best and only repeats the LaTeX lines.
- M3.S25.T25.C83 (worked example, Quick Sums and Differences with Round Numbers): none. The example is practice values (46 + ___, 358 + ___, 52 - 9, 215 - 99) with no figure in the book; two kept teaching images already show the method and are not linked (not the reason: no v3 trigger applies). It has the same kind of answer as C86, but the example has only one image slot and four parts, so one picture would be overcrowded.
- M3.S28.T28.C97 (worked example, palindromes): none. Reading 2,442 from both ends and listing 303, 313, 323, 333 is plain text.
- M3.S27.T27.C90 (877 + ___ ...): the digit-by-digit "make nine" pairing could be drawn, but the book gives no figure here and the answer is numbers only (see judgement call 4).
- M3.S27.T27.C94 (subtract 9 or 99): a number-line hop would help but is optional at most; the LP carries every step.

## LP text issues

- M3.S27.T27.C87 (question): "Try this method for the number 59." never says what the method is, and the ovals of the figure carry it. Suggested: "Use Piku's method: make 9 in each place, then add 1. Fill the two ovals. 59 + ___ = 100."
- M3.S27.T27.C89 (question): "Now, use this method to solve the following." names no method. Suggested: "Now, use the make-9-then-add-1 method to solve the following."
- M3.S27.T27.C95 (question): "Now, use the above solutions to find answers to the following problems. Do not calculate again." points at the answers of C93 without naming them. Suggested: "Use your answers to the question about taking away 9 or 99. Do not calculate again."
- M3.S27.T27.C96 (steps_tex, first step): broken math delimiters, `$9 ($or $99)$`. Suggested: "...so the blank is the first number minus $9$ (or minus $99$)." The same string should be checked in the `text` field.
- M3.S29.T29.C104 (steps_tex, first step): `$A 5$ digit number` has the letter A inside the math. Suggested: "A $5$ digit number between $25,000$ and $27,000$ ...".
- M3.S27.T27.C92 (steps_tex, step 4): "The last nine is 9, and adding 1 makes it carry." is unclear. Suggested: "The units digit 0 needs 9 to make 9, so the blank ends in 9, and adding 1 makes it carry."
- M3.S25.T25.C83 and M3.S28.T28.C97 (worked example question text): the learner-facing question ends with "(practice values)". Suggested: delete that bracket from the learner text (it is a note for the author).
- LP numbering differs from the book's: C71/C73/C75 are called Q1/Q2/Q3 in the LP but are book Q2/Q3/Q4 (p.10); C77/C79/C81 "Let us do Q1/Q2/Q3" are book Let Us Do Q3/Q4/Q5 (p.15). C85's book note says "blanks" in the book (one blank is printed). Only the labels differ; the questions match the book text.
- All LP answers were recomputed (Mary 10,245; council 68,878 and 1,622 left; truck 6,525 and 1,725; Ambrish 62,873 and 29,502 more; factory 31,300; Virat/Sachin 34,357; 32 + 68; 59 + 41; 123, 334, 5,897, 4,445; 820, 240, 600; 58, 74, 135, 88, 148, 664; 23, 47, 778, 567; palindromes 10 / 12 / 20). No arithmetic error found.

## Book unclear or noteworthy

- p.10 route figure of Mary: no arrowheads or start mark. The amounts at each stop are the spending of the leg that starts there (Kolkata 3,275 on the way to Varanasi; Varanasi 2,645 for the ticket to Delhi; Delhi 1,275 for souvenirs); the start 12,540 and the gift 4,900 are not drawn. A market photograph beside the figure is decoration (not inventoried).
- p.11 Piku figure (32): the book prints the "+1" arc, the ovals and the digits 67 and 68 in lilac and the sums in black; the digits are letter-spaced and "100" has three places, one to the left of the "+" column. The red note "Do you think this method will always work?" is not part of the figure and is excluded.
- The book has no printed-solutions section, so the only printed "answer" picture in this chunk is Piku's figure for 32.
- No print mistake (wrong digit, missing sign) found in this chunk's questions or figures.
