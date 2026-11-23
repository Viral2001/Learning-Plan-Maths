# Chunk C notes (Class 7 Ch 3, topics M2.S14.T14, M2.S15.T15, M3.S17.T17, M3.S18.T18)

Result: 29 items = required 14 / optional 0 / none 15. Validator: errors 0, 1 warning (C66 solution has no printed figure, see 1.3).
Required: question C66, C67, C68, C70, C71, C72; solution C66, C67, C68, C69, C70, C71, C72; worked example C76.

## 1. Judgement calls

1. **C66 (divisions between 1 and 1.1), both sides required.**
   1.1 Question figure = the line printed beside the book question (p.70): long ticks 1, 1.1, 1.2, 1.3, nine short ticks in the first gap, the example arrow 1.04 (the book prints it as a given). I drew it because the ten-part cut exists only in the picture. The book's "Locate 1.4" demonstration (line 1 to 2, 1.4 circled) is a teaching figure (concept image C62.IMG1) and is not repeated in the question figure.
   1.2 Solution figure = question figure unchanged plus, in ANSWER green, a fifth long tick 1.4 (ringed) and a magnified strip of 1 to 1.1 with 1.01 to 1.09. The strip is my layout choice: on the line itself the nine labels would collide (32 px between marks).
   1.3 The book's printed answer is text only (p.47), so no base figure maps to the solution (the validator warning). I kept it required because the answer is marks on a number line (B2) and for sibling consistency with C67, C70 to C72.
2. **C67 (letters A to D).** The LP text says there is a large mark at 5.2. The book picture (p.70, also the printed answer p.47) has NO long tick at 5.2, only a continuous run of small ticks between 5.1 and 5.3 (base inventory is right). I followed the LP text (long tick, unlabelled). Arrow positions and the four readings are the same either way; this is also written in the spec's render_note. Please confirm, or drop the long tick at x=980 if the picture should match the book exactly.
3. **C68 (zooming).** The question figure holds both book figures: (a) complete with 4.185 (the book prints it so), and (b) with '?'. The book prints no range labels on rows 2 to 4 of (b); the question figure has none; the solution adds 3-4, 3.0-3.1, 3.05-3.06 and 3.059 (boxed). Figure (a) is also concept image C63.IMG1 (not linked, drawn again; second use recorded as `NEW-P26-number_line-1-q`). No "(a)/(b)" captions are drawn.
4. **C69 (make the zoom lines).** Question `none`: the book gives no figure (it points back to Figures (a) and (b)); inventing a blank would break the companion rule. Solution `required` (ANSWER_IS_FIGURE, derived_from null): two four-row chains drawn from the book's printed answer (p.48). The book chains start with the line 0 to 10, the LP steps list only three zooms; the figure follows the book.
5. **C70, C71, C72 (boxes on number lines).** Question boxes show the letter in the upper half; the solution adds the value in ANSWER below the letter. The book's printed answers (pp.49, 53) put the value alone in the box; I kept the letters so labels stay the same in question and solution (companion note), and because boxes c and b of C72 are only 170 px apart.
6. **C76 (closest decimals, worked example), required.** This is the one I am least sure of. Reasons for: the book's printed answer is a picture of three digit-tile rows (B2 `ANSWER_IS_FIGURE`) and the position of the point is the content. Reason against: the three numbers are in the LP steps as text. The figure shows 25.148 (green MARK_FILL, closest), 8.5421, 124.58, aligned on the point. Drop it (action `no_image`) if you want text only.
7. **C52 rice heaps and C54 money, worked examples `none`.** All numbers are in the question text; the book pictures are real photographs (rice, coins, 1970 cafe bill, stamps). A drawn row of five heaps would be nice-to-have only, so I did not mark it optional.
8. **C56 to C59 (blanks) `none`, both sides:** plain conversion tables (LATEX_TABLE) even though the printed answers are tables. **C60, C61:** word questions, arithmetic answers.
9. **Figure claims.** I claimed every 3.5 figure (no other chunk has 3.5 units) and the 3.6 number-line figures of my units. Not claimed (they belong to chunk D units): P25-table-4 (zero dilemma table), P27-comparison_visual-3, P47-table-2, P35-addition_boxes-1, P55-digit_tiles-1; to chunk B: P44-table-1. If the merge finds P25-table-4 unclaimed, give it to D.

## 2. Things that look wrong in the LP

- C67 and C72 video `final_answer.spoken` contain a typo: "eigh is five point zero nine" (C67) and "the letter eigh is six point four five" (C72); should read "A is" / "the letter a is" (text-to-speech text).
- C67 question/steps: "large marks at 5, 5.1, 5.2, 5.3 and 5.4" and "C is on the large mark 5.2" contradict the book picture (no long tick at 5.2).
- C76: the book's printed answer shows 8.542 in the yellow row (4 tiles, digit 1 missing, so not "each digit once"; the question picture also has only 4 yellow boxes). The LP's 8.5421 is correct and used. The book answer also lists three layouts; the LP picks 25.148 (0.148 away). Checked: 24.851 is 0.149 away, so 25.148 is the closest.
- C56: the book table prints 12 mm = 1.2 cm and 56 mm = 5.6 cm as given examples; the LP question lists them as blanks to fill and the solution repeats them.
- C56 to C59 and C66 to C71: the `text` field of these question blocks starts with "Worked example:" and carries `example_id` "E0" although they are questions (cards are linked). Harmless but misleading.
- C66: the LP merges the book's teaching sentence "Locate 1.4 on the number line" into the question; the book asks only to name the divisions.
- C68: LP question says "Locate 4.185 by zooming"; the book says "Observe the number lines in Figure (a)" and prints 4.185 already located, so the question figure shows the finished (a).
- C54 worked example step 4 ("Prices from your own elders' childhood...") is a discussion prompt, not a working step.
- The brief says the PDF has no printed-solutions section; it does (pdf pages 36 to 55, "Page No. 47" onward). The inventories use it and so did I.

## 3. Book unclear or contradicting itself

- p.70: the A to D line has no long tick at 5.2 (see above); C is at the 10th small-tick position after 5.1 (reads 5.20).
- p.71: Figure (b) rows 2 to 4 have no range labels, so the ranges (3-4, 3.0-3.1, 3.05-3.06) are known only from the zoom boxes and the printed answer (which writes "3" instead of "3.0" on row 3; LP says 3.0, used).
- p.73: yellow row of the Math Talk question has 4 empty boxes although five digits are given.
- p.71 (printed answer p.48): the 9.876 chain's first line is 0 to 10 with the box on the last part; LP lists only 9-10, 9.8-9.9, 9.87-9.88.
