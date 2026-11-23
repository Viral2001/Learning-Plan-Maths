# Chunk B notes (Class 5 Ch 2 Fractions, topics M1.S10.T10 to M2.S18.T18)

Result: 23 items (9 pairs, 5 worked examples). Required 6, optional 5, none 12. Validator errors 0 (2 warnings, explained in 1.7).

Required diagrams (all 16:9, `fraction_model`):

| media_id | item | what it draws |
|---|---|---|
| M1.S10.T10.C39.IMG1 | question | the three printed squares (middle third shaded) with an empty box under each |
| M1.S10.T10.C40.IMG1 | solution | same squares cut into 5, 6, 7 rows, boxes filled 5/15, 6/18, 7/21 (derived_from C39.IMG1) |
| M1.S10.T10.C41.IMG1 | question | four rectangles, rows 2 and 4 of 5 shaded, labels 2/5 and 4/10, two empty fraction slots |
| M1.S10.T10.C42.IMG1 | solution | rectangles 3 and 4 cut into 3 and 4 columns, slots filled 6/15 and 8/20 (derived_from C41.IMG1) |
| M2.S13.T13.C52.IMG1 | solution | chikki slab in 3 strips, Sevi 1/3 and Shami 2/3 ringed (no question diagram, derived_from null) |
| M2.S16.T16.C58.IMG1 | solution | paratha 4/6 and paratha 4/5, loose 1/6 and 1/5 piece, comparison (no question diagram, derived_from null) |

## 1. Judgement calls

1.1 **Worked examples C49, C55, C61, C62, C63 are all `optional` (no image added).** They are LP-written teaching examples (none is a book item), every number is in the text, and no v3 Step B trigger fires. I applied the tie-breaker as written (a careful student can follow each from the text) and did not use the existing teaching images as a reason. Each reason names the figure that would help (C49 two bars of 10 pieces with 3 and 7 shaded; C55 two same-size parathas cut into 4 and 10 pieces; C61 number line 0 to 5 in halves with 9 jumps; C62 11 quarters grouped by 4 and 8 slices grouped by 3; C63 bars of fifths and tenths against the whole). If the user wants them drawn, flipping them to `required` only needs a spec each; C55 and C61 would be the strongest candidates.

1.2 **Example pairs C51/C52 (chikki) and C57/C58 (paratha): question none, solution required.** The LP questions do not point at a figure and give all numbers in words, so a question figure would be a blank slab or a pair of parathas that already shows the comparison (rule: no question figure when the question gives none). The book prints the picture next to the worked answer ("2 pieces of 1/3 are more than 1 piece of 1/3"; "1/6 piece is smaller than 1/5 piece"), so the solution side is required (B2, printed answer rests on a picture). Both solutions draw the whole figure themselves (`derived_from` null).

1.3 **C39/C41 question figures include the empty answer boxes/slots.** The book prints them ("Write them in the boxes below the images"; empty fraction slots under rectangles 3 and 4) and the solution figure fills them in ANSWER green, which keeps the same layout between question and solution. They contain no digit, so nothing leaks.

1.4 **C39 question figure shows only the three given wholes, not Sameer's row of four squares (1/3, 2/6, 3/9, 4/12) from pdf page 4.** The old hint `q_figure` mentioned that row too, but the book question says "the wholes given below", the first four fractions are already in the equation line, and the four squares are the teaching figure of M1.S9.T9 (chunk A: C36 'mk.sameer'). So P04-fraction_model-1 is NOT claimed by chunk B. If the user wants Sameer's row above the three wholes (and in the solution), the figure becomes a two-row picture; say so.

1.5 **Solution of C40 draws only the three pictured wholes (5/15, 6/18, 7/21).** The LP sample answer also gives 8/24 and 12/36, but the book has no picture for those two boxes, so they are not drawn. Likewise C42 does not draw 20/50 and 40/100.

1.6 **Colours.** The book's yellow/lilac shading is replaced by the house tokens: MARK_FILL for shaded cells, ANSWER green for everything the solution adds (new cut lines, new numerals), SET_A / SET_B for the two groups being compared (Sevi / Shami strips; the 4/6 and 4/5 parathas and the loose 1/6 and 1/5 pieces), FOCUS for the ring around Shami's two strips.

1.7 **Warnings (2).** C40 and C42 solutions are required but have no book figure mapped to them: the pdf has no printed-solutions section and the figures are the question figure completed (the base figures P05-1 / P05-2 are mapped to the question items).

1.8 **Figure ownership.** Claimed (9): P05-fraction_model-1 -> item C39 (question); P05-fraction_model-2 -> item C41 (question); P06-fraction_model-1 -> item C52 (solution); P07-fraction_model-1 and -2 -> item C58 (solution, both paratha pictures are drawn in one diagram); P08-number_line-3, P08-number_line-4 -> concept_image C61.IMG1; P10-number_line-3, P10-number_line-4 -> concept_image C62.IMG1. The four number lines are claimed because the teaching text of my concepts C61 (`gt1.nl_halves`) and C62 (`gt1.nl_fourths`) is the sentence printed with them. They are also the book's number lines for Example 3 (Maa, 5 halves) and Example 5 (Dadaji, 9 fourths), which are chunk C items: chunk C may map the same base figures to its own solution items. Needs a merge decision if both chunks keep them (suggest: chunk C draws them for its solutions, chunk B keeps them as teaching figures, give the second use a NEW- id).

1.9 The six required diagrams use `fraction_model` with a full `content` object (pixel coordinates on a 1920 x 1080 canvas). Squares/rectangles are drawn flat; the book's photographic chikki and paratha textures are not reproduced.

## 2. LP text issues

(Not edited; listed only.)

- **M1.S10.T10.C39** (Q1, equivalents of 1/3): the question text says "Sameer has shaded one-third of the figures. He draws horizontal lines to divide the shapes..." but the figures it talks about (page 4: four squares showing 1/3, 2/6, 3/9, 4/12) are not in the question picture, and the figure now added shows the three blank wholes. Suggested sentence: "Sameer shaded one-third of a square. When he cuts it into 2, 3 and 4 equal rows he gets 2/6, 3/9 and 4/12. Divide each of the three wholes below into more equal rows with horizontal lines and write the equivalent fraction in the box under it."
- **M1.S10.T10.C41** (Q2, equivalents of 2/5): the text says "write your fractions below each image", but only the third and fourth rectangles have an empty slot; the first two are labelled 2/5 and 4/10. Suggested sentence: "Write the fraction of the shaded part in the empty box under the third and the fourth picture, then complete the line below."
- **M2.S13.T13.C51/C52** (Example 1, chikki): neither the question nor the solution says which piece of the chikki is Sevi's. The figure assumes the top strip is Sevi's and the other two strips are Shami's. Suggested sentence for the solution, step 1: "The chikki is cut into 3 equal pieces. Sevi ate the top piece, 1 piece of 1/3."
- **M2.S16.T16.C57** (Example 2, paratha): "One child says: I ate 4/6 ... The other says: I ate 4/5 ... Between Sevi and Shami" never says which child is Sevi. In the book the girl (Sevi) says 4/6 and the boy (Shami) says 4/5. Suggested sentence: "Sevi says: I ate 4/6 paratha yesterday evening. Shami says: I ate 4/5 paratha yesterday evening. Can you tell who ate more? Use your fraction kit to find the answer."
- **M2.S18.T18.C61** (worked example, 9 halves): step 5 says "Check on the number line: 9 jumps of 1/2 from 0 land on 9/2", but the worked-example block shows no number line (only the teaching image of the concept does). Suggested sentence: add "(look at the number line in the picture above)" to that step, or draw the number line (see 1.1).

## 3. Borderline

- Worked examples C49, C55, C61, C62, C63: `optional` (see 1.1). These are the calls most likely to be reversed by the user.
- C52 and C58 solutions: `required` although the LP text carries every number (kept as required on purpose, per the 23 Nov decision 4, because the book's printed answer is a picture).
- C51 and C57 questions: `none` although the book prints a picture beside the question (the picture goes with the printed answer, the LP question text does not refer to it).
- C54 and C60 solutions: `none`. The six parts compare plain fractions; the book prints no figure, and six pictures would only restate the numbers. (Sibling check: the other "compare with < >" items of the chunk are all `none`.)
- C46 solution (ticks on (b) and (c)): `none`, a selection written in the answer line, not a drawing.
- C39 question: boxes drawn empty (1.3); Sameer's row not drawn (1.4).

## 4. Book unclear or contradicting

- Which strip of the chikki is Sevi's: the book shows an unmarked slab; the diagram chooses the top strip.
- Page 7: the book prints the fifths paratha on the left and the sixths paratha on the right, but the question lists 4/6 (girl, left) before 4/5 (boy, right). The diagram follows the question order (sixths left, fifths right); the book's dashed rims and the 1/5, 1/6 sector labels are left out.
- Page 7: the book labels only the eaten sectors (4 of 5 and 4 of 6); the other sector(s) are unlabelled with a dashed rim. The diagram shades the 4 eaten sectors and leaves the others white.
- No book print slips found in my figures. (The base inventory descriptions of P05, P06, P07, P08 and P10 were checked against the page pictures and are correct.)
- Page 5 equation line for Q1: three standalone blanks, then a box over 24 and a box over 36 (same as the LP); the book never says what the boxes over 24 and 36 hold, the LP sample answer gives 8/24 and 12/36.
