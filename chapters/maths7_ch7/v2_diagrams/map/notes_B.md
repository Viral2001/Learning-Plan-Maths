# Notes for chunk B (Class 7 Ch 7, plan cbse_eng_maths7_ch7_v61)

Result: 30 items (16 units) -> required 10 / optional 2 / none 18. Validator: `errors 0`, 3 warnings (all expected, see 1.9).

Required (10): worked C51 (IMG2), solution C55, solution C57, solution C63, solution C65, worked C66 (IMG2), question C69, solution C70, solution C81, solution C83.
Optional, not added (2): solution C59, question C82.

## 1. Judgement calls

1.1 **Construction questions: question none, solution required (5 pairs).** 5-4-45 (C54/C55), Figure it Out SAS Q1 (C56/C57), ASA 45-5-80 (C62/C63), Figure it Out ASA Q1 (C64/C65), 60/70 on bases 5 and 7 cm (C80/C81). The book gives only measurements (no printed figure), so no question figure ("don't invent a question figure"); the built triangle is the answer, so the solution figure is required (B2, ANSWER_IS_FIGURE) and stands alone (`derived_from` null). The five are decided alike (sibling consistency).

1.2 **Three-triangle cards (C57, C65).** The LP keeps parts (a), (b), (c) in one concept, so each pair gets ONE solution diagram: three triangles in a row, left to right in the order of (a), (b), (c). The part letters (a)/(b)/(c) are not drawn (prompt section 4: no figure letters); each triangle is identified by its own given numbers. Each triangle is drawn to its own scale (stated in `scale_note`, `to_scale: false`) because three triangles on one common scale cannot keep 48 px labels legible on a 16:9 card (the 75-5-75 triangle is 9.3 cm tall, the 25-3-60 triangle is only 1.1 cm tall). Coordinates, arc radii and label centres were placed by a script and checked on a preview render (no label touches a line or another label).

1.3 **C65: the side lengths are not drawn.** The LP steps also give the other two sides (a: 9.7 and 9.7, b: 2.6 and 1.3, c: 10.4 and 6, I recomputed all of them: correct), but the LP's own figure note lists only the third angles (30, 95, 30), and six more length labels would crowd the card. If the user wants them, the spec has room only if the card is split into three. The sibling C57 does draw the third side because the LP's final answer is that side.

1.4 **Vertex letters A, B, C are drawn in every construction figure** (C55, C57, C63, C65, C81) even where the LP text of that item has no letters (C65, C81): they follow the book's construction convention (triangle ABC, base AB). In C81 the sides AC and BC carry no length (neither the question nor the LP solution gives them).

1.5 **Worked example C51 (included angle) required.** Question text is complete in words, so a strict reading could say TEXT_SUFFICIENT. I chose required because the whole example is about WHERE the 30 degree wedge sits (between the 6 cm and 5 cm sides, or at the far end of the 6 cm side) and the book itself draws this (p.15). Two-panel figure, both panels at 1.1 canvas-cm per cm; panel 1 is the book's middle triangle, panel 2 is the question's own "what if". The teaching image C51.IMG1 (4 cm, 60 degrees, 3 cm) is not linked. If the user prefers text only, flip it to `optional` (no other change needed).

1.6 **Worked example C66 (two big angles never meet) required** for the same reason: 90/90 (right-angle squares) and 100/95 (arms leaning outward) are spatial. The teaching image C66.IMG1 shows only the 90/90 case and is not linked. No vertex letters (the example's text has none).

1.7 **C69 question required, C70 solution required (derived).** The book gives this as a figure (p.17, "angle B marked in the figure"); the LP text does not say which way the arm from A leans, so the figure carries data. The arm is not named l in the question figure (the LP question never names it; the LP solution says "call the line along this arm l"), so l and m appear only in the solution figure. The book's extra fan of rays from B (p.18) is not drawn: only the limiting line m and the 140 degree angle (LP solution).

1.8 **Optional (not added):** C59 solution (SAS Math Talk: no triangle at 180 degrees or more): a picture of the two sides lying on one line would help, but the answer is a statement and the book's printed answer (p.31) has no picture. C82 question (find A from B = 50, C = 70 degrees): both angles are in the text and the learner can sketch the triangle, so the book's triangle is optional there; the solution figure (C83, line XY, alternate angles, 60 degrees) draws the whole triangle itself.

1.9 **The 3 validator warnings** (C57, C65, C81 "required but no inventory figure maps to it") are expected: the book prints no figure for those answers (no printed answer for Figure it Out SAS Q1 and ASA Q1, no figure in the 60/70 exploration), so there is no base figure to claim.

1.10 **Figure inventory mapping.** 12 base figures claimed (7 to items, 1 concept image, 4 none). Teaching figures from which an item diagram is drawn are mapped to that item, not to the concept image: P15-shape-1 (-> C51 worked), P17-shape-1 (-> C66 worked), P15-construction-3 (-> C55 solution), P16-construction-3 (-> C63 solution), P19-shape-2 (-> C83 solution). P16-construction-2 is the same finished triangle as P16-construction-3 and is mapped to the concept image C60.IMG1. P15-construction-2 (intermediate stage) is not drawn (the final state is, TEXT_SUFFICIENT); P16-shape-1 (three teaching examples whose numbers are in the C60 text) and P19-shape-1 (triangle with 50 and 70 degrees, question side optional) are TEXT_SUFFICIENT; P32-table-1 is a plain text table (LATEX_TABLE). If another chunk also claims P19-shape-2 / P19-shape-1 (angle-sum topics S24/S26) the meaning is the same: the figure becomes the solution figure of C83; the plain triangle is optional on the question side.
   Corrected base description: P15-construction-3 (see `figure_inventory`): C is above a point about 56% along AB, and AC is about 0.83 of AB in the picture (base note said 0.7 and "above the left-middle").

1.11 **Rounded values.** The LP writes "about 3.6 cm / 6.9 / 3.5 / 9.8 / 6.0 / 4.3"; the figures draw the geometry exactly and label the rounded value (exact: 3.566, 6.865, 3.518, 9.849, 6.011, 4.316).

1.12 **None items.** C45-C50 (triangle-inequality Figure it Out), C71-C76 (angle pairs) are text, LaTeX arithmetic or a plain table. Figure it Out Q3 (C49/C50) answers are ranges (99 to 101, 0 to 10, 4 to 10); a number line was considered and left as text (tie-breaker).

## 2. Things in the LP that look wrong or thin

2.1 **M2.S17.T17.C59 (Math Talk, two sides and the included angle), step 3** says that for 4 cm, 210 degrees, 6 cm "the angle on the other side is less than 180 degrees and the picture is the same as a smaller angle", yet the answer is "no triangle". Those two statements contradict each other (a reflex 210 degree angle leaves a 150 degree angle on the other side, which does make a triangle). The book's answer only says an included angle of 180 degrees or more gives no triangle. Suggest rewording to the book's statement.

2.2 **Book numbers.** The LP calls the SAS Math Talk (C58/C59) "Figure it Out, Q2"; in the book (p.16) it is a Math Talk after Figure it Out Q1. Same for C75/C76 ("Figure it Out, Q3" is an unnumbered "?" question on p.18 after Figure it Out Q2).

2.3 **C71/C72 (angles 30, 70, 54, 144).** The book's printed answer table (p.32) ends each "possible" cell with "Find the third angle in each case"; the LP question and solution drop that follow-up (and the LP's example angles differ from the book's, all valid; LP kept).

2.4 **C54/C55 and C62/C63 `book_number`** are descriptive strings ("Two Sides and the Angle: construct 5 cm, 45 and 4 cm") rather than book numbers (they are worked examples in the book, p.15 and p.16).

2.5 **Worked units C51 and C66** have no `book_number`; `lp_book_number` is null in the map.

## 3. Where the book itself is unclear

3.1 P17-shape-2 (p.17): the text says "angle B (marked in the figure)" but nothing is marked at B in that figure; the arc at B appears only in the next figure (p.18).

3.2 The book's small ASA picture on p.16 (P16-construction-2) is flatter than the stated angles (the angle at A looks about 34 degrees, not 45); the figure drawn here is to scale.

3.3 The book has no printed solutions for the two construction Figure it Outs (SAS Q1 p.16, ASA Q1 p.17), nor for the 60 and 70 degree exploration; the third sides and angles were recomputed (cosine rule, sine rule) and agree with the LP everywhere.

3.4 Page 31's printed answer to the SAS Math Talk says "greater than or equal to 180 degrees"; the LP adds 0 degrees (arm on top of the base). Both fine.

## 4. Working files (outside HERE)

Generator and preview renders are in the session scratchpad `.../scratchpad/c7ch7_B_v2/` (`build_out.py`, `figs.py`, `geo.py`, `prev/*.png`); nothing else was written under HERE except `map/out_B.json` and this file.
