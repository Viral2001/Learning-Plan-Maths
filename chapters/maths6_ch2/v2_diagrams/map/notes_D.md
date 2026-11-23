# Notes, chunk D (Class 6 Ch 2, section 2.9 part 2: protractor questions, make your own protractor, Mind the Mistake)

Units: T21 (Q4, Q6, Q7), T22 (two worked blocks), T23 (Q8 to Q12), T24 (Mind the Mistake). 11 units, 19 items:
required 11 / optional 2 / none 6. Validator: errors 0, warnings 0.

| Item | Decision |
|---|---|
| T21.C101 Q (name the angles) | required (six rays + scales only in the picture) |
| T21.C102 S | required (readings from P written on the rays), derived_from C101 |
| T21.C103 Q (20 and 55 outer scale) | optional (both readings are in the text) |
| T21.C104 S | required (OT and OS only, 20 and 55 circled, 35 marked), stands alone |
| T21.C105 Q (angle AOB) | required |
| T21.C106 S | required (inner 0 and 80 circled, 80 marked), derived_from C105 |
| T22.C107 worked (craft) | required, one merged picture (Fig. 2.19 letters + Fig. 2.20 degrees), media IMG2 (IMG1 is the kept teaching image) |
| T22.C109 worked (angle bisector) | optional (open-ended; not added) |
| T23.C111/C112 Q8 | none / none |
| T23.C113/C114 Q9 | none / none |
| T23.C115 Q10 / C116 S | required / required (derived_from) |
| T23.C117 Q11 / C118 S | required / none |
| T23.C119 Q12 / C120 S | required / none |
| T24.C121 worked (Mind the Mistake) | required, one 6-panel picture, media IMG2 |

## 1. Judgement calls (item, choice, why)

1. **Protractor solutions (Q4, Q6, Q7) are `required`, although the printed answers are plain text.** Step E says a figure-based
   question with a numeric answer gets Q required, S none. I broke that for these three because the LP solution is itself a
   description of where on the scale each arm is read ("reading from P as 0: Q=35...", "outer scale 20 and 55", "the scale that starts at 0
   on OB, OA passes 80"). The solution figure marks exactly those readings (an instrument reading is visual evidence, not arithmetic).
   If the user wants the strict Step E reading, Q7's solution (adds only a ring and an 80 mark to the question figure) is the first to drop;
   Q4's (five different readings) and Q6's are the strongest.
2. **Q6 question (C103) is `optional`.** The text gives the two readings (20 and 55), so a careful student loses nothing without the figure.
   The solution (C104) still draws the whole figure alone (`derived_from` null). The book's figure for Q6 is the six-ray figure of Q4 on the
   previous page; the solution draws only OT and OS at the same positions.
3. **Q8 / Q9 none, Q10 required.** Same question set, same answer type (blank + a label written on the paper semicircle). The difference:
   in Q8 ("left bottom corner") and Q9 ("top of the semicircle") the text itself fixes where the label goes and the blanks are plain
   arithmetic; in Q10 the two labels go "at the correct places on the new creases ... as shown", which only the picture tells. Fig. 2.14
   and Fig. 2.15 are teaching pictures that the kept concept image of the fold already covers (accounted as concept images).
4. **Q10 question figure is Fig. 2.17 without 45° and 135°.** The book prints both labels in Fig. 2.17; the question asks the learner to
   write them, so the question figure leaves them out (no leak) and the solution adds them in ANSWER green. The LP's own hint (`q_figure`)
   describes Fig. 2.16 (the folded quarter), but the writing action happens on Fig. 2.17, so I drew that; Fig. 2.16 is not drawn.
5. **Q11 question required, solution none.** The LP text names "Fig. 2.18". The book figure carries no number, so the figure does not
   give the 45 degrees either (see section 2). The solution is a numeric answer on a figure-based question (Step E): none.
6. **Q12 solution none.** One repeated value (22.5 for all eight angles) plus a reason in words. Marking 22.5° eight times would only
   repeat the question figure; the same figure with degrees is already the worked-example picture of the craft.
7. **T22.C107 worked (craft): one picture only.** The text points at Figs. 2.13, 2.15, 2.16, 2.17, 2.18, 2.19 and 2.20 but a worked item
   gets one diagram. I chose the result of the craft (the unfolded semicircle with the creases lettered A to I and marked 0 to 180),
   merging Fig. 2.19 and Fig. 2.20 into one picture (Fig. 2.19 is a lettered figure: v3 B2 says draw it on its first appearance,
   even though a teaching image of the topic exists). The fold pictures 2.13 to 2.18 are not drawn; the fold steps are in the text and the
   kept teaching image shows the first fold. Q12's question figure (Fig. 2.19) is the same drawing without the degree labels.
8. **T22.C109 worked (angle bisector) optional.** Open-ended work on the learner's own protractor, so no figure is needed; the lettered
   semicircle with OE and OC marked would help (see section 2).
9. **T24 Mind the Mistake: one combined picture of six protractors.** A worked item has one diagram, so the six book figures are six
   panels (3 x 2) on one 1456 x 816 card. At that size the real protractor scales cannot stay legible, so the panels use a simplified
   protractor (scale numbers only 0, 90, 180 on both scales, no 10 degree radial lines). The mistakes are about placement (arm off the 0 line,
   vertex off the centre, protractor turned, wrong scale), which the simplified protractor shows. The panel captions "∠U = 35°" etc. are in
   the LP question text, so they are allowed in the picture. The spec shows the student's placement only: no ticks, no corrections, no true angles.
10. **Figure P24-protractor-1 (the plain labelled protractor, pdf p.24) is not claimed.** It is the teaching figure of the topic of chunk C
    ("Reading a Protractor", concept image M3.S19.T19.C95); the merged-map check will show if nobody claimed it.
11. **Concept-image accounting (no link):** Figs. 2.13, 2.14, 2.15 -> M3.S22.T22.C107.IMG1; the two "units" fan pictures on p.26 ->
    M3.S17.T17.C88.IMG1 (same teaching content as the p.21 fan pictures that chunk C accounts for). Fig. 2.16 -> none (TEXT_SUFFICIENT).
12. **Reuse entries:** a figure used by a second item is a `NEW-<base id>-<suffix>` entry: the Q4 figure (solution of Q4, solution of Q6),
    the Q7 figure (solution), Fig. 2.17 (solution of Q10) and Fig. 2.19 (letters inside the craft picture).

## 2. Things in the LP that look wrong or thin

- **C103 (Q6):** "Here, OT and OS pass through the numbers 20 and 55..." points at the six-ray figure of Q4, which is not on this card.
  The card still reads fine because the readings are in the text, but "the numbers marked" is a dangling phrase.
- **C117 (Q11):** the question does not say what is being folded. The 45 degrees comes from the previous question's answer; the book's
  Fig. 2.18 shows no number either. A short phrase such as "the 45° wedge" in the question text would make it answerable on its own.
  I did not set `needs_lp_text_sync`; the question diagram is drawn without a number as in the book.
- **C109 (angle bisector):** the example answer uses the letters OE, OC, A, I of Fig. 2.19 ("OE bisects the straight angle AOI ... OC bisects
  ∠AOE"), but nothing on this card defines them. Either add the lettered semicircle (optional figure, not added) or reword the answer.
- **C111, C115, C117 hints (`q_figure`):** C111's hint (semicircle with 0° only) does not match the book (Fig. 2.14 prints 180° and 0° and a turn arc);
  C115's hint describes Fig. 2.16 not Fig. 2.17. Hints only; not used.
- **Book answer for Think! (printed solutions p.50)** says "In Fig. 2.20 we have ..." while the question (and the LP) say Fig. 2.19. The LP follows the question.
- **Q4:** the LP's fourteen answers leave out the straight angle POU (180°); the book's printed answer also leaves it out. The readings used in the
  solution figure reproduce all fourteen LP values (recomputed: 35, 95, 125, 160, 60, 90, 125, 145, 30, 65, 85, 35, 55, 20).
- **Base inventory error:** P32-protractor-5 (panel Y) says the vertex is at the protractor centre. In the picture the two rays meet on the
  horizontal middle line at the right edge of the cut-out, about a quarter of the radius to the right of the centre. Corrected in the
  inventory entry ("CORRECTED:") and in the spec.
- C121 answer text "Open-ended discussion; no solution printed." The three steps are generic checks. For the user's information only, what the
  six figures show: U second arm below the 0 line, V neither arm on the 0 line, W vertex outside the protractor (centre placed on an arm), X vertex
  off-centre on the straight edge and the wrong scale, Y protractor turned and vertex off-centre with the two readings taken at the rim,
  Z protractor upside down and the wrong scale read. This is not put in the diagram.

## 3. Places where the book itself is unclear

- No true angle is printed for any of the six Mind the Mistake figures. The ray directions in the spec are measured from the page picture
  (about +-2 degrees): U 60, V 70, W 73, X 23, Y 144, Z 105 degrees between the rays. The student readings (35, 80, 70, 150, 120, 85) are the ones printed.
- The ray angles of Q4 and Q7 are not printed either; they are measured (35, 95, 125, 160, 180 and 80) and agree with the printed answers and with the
  book's sentence "OT and OS pass through the numbers 20 and 55 on the outer scale".
- Fig. 2.18 has no values; Fig. 2.17 prints all labels although the text asks the learner to write 45° and 135°.
- Book rays on the protractor figures are about 1.15 R long; Q4's are drawn 1.30 R so that the solution can print the readings on the rays.
