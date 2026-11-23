# Notes, chunk C (Class 6 Ch 7 Fractions: M2.S13.T13, M2.S14.T14, M2.S15.T15)

Result: 26 items = 1 required / 2 optional / 23 none. Validator `--chunk C`: errors 0, warnings 0.
Items: 14 worked blocks (8 in T13, 6 in T15) + 6 pairs of Figure it Out 7.5 (12 items).
Figures claimed: 7 base figures (1 to an item, 1 to a concept image, 5 none).

## 1. Judgement calls

**C79 (three strips 1/2, 2/4, 4/8): REQUIRED, media_id M2.S15.T15.C79.IMG2.**
- The book question is "What do you observe? Are the lengths 1/2 and 2/4 equal?" and it is about the picture on p.164: that the
  shaded parts end at the same place on strips of the same length is seen only in the drawing. The LP had to describe the picture
  in words ("three paper strips ... 2 equal parts with 1 part shaded ...") which is the sign the figure carries the data.
  Tie-breaker: the picture changes how easily the learner answers. Triggers FIG_REFERENCED, DATA_IN_FIGURE, HIGHLIGHT_MEANING.
- The plan already has a teaching image C79.IMG1 with the same three strips; v3 says it is never linked and an item that needs a
  figure draws its own. The new figure shows only what the question gives (no "=" chain, no equivalent-fraction words, no guide line
  through the strips); the teaching image states the equality, so the two do not duplicate each other.
- Book picture vs my figure (see `render_note`): the book prints a plain top strip labelled 1 and only SOME fold creases (strip 2: one
  at 3/4; strip 3: at 1/4 and 3/4; strip 4: at 1/8, 1/4, 3/8, 3/4; read from the page picture, matches the base inventory). I followed the
  LP text (folded into 2, 4, 8 equal parts): every crease is drawn, as a solid line so the parts can be counted, and the top "1" strip is
  left out because the question speaks of three strips. If the user wants the book's top strip, add a plain 1200 px strip labelled 1.
- Colour: shaded parts use MARK_FILL (the style token) instead of the book's blue.

**C80 (paper strips 1/3 vs 2/6): none, TEXT_SUFFICIENT.** The book gives no picture for it (hands-on instruction, then the fraction wall).
A question with no given figure gets none; the folding is fully described in the steps. A two-strip picture would help but would be
invented, not the book's.

**C81 (one roti, four children): none.** Question names every number; the book's roti picture (p.165) only illustrates; the plan's teaching
image C81.IMG1 already shows the division and the three facts. Figure P15-arrangement-1 is accounted as `concept_image:...C81.IMG1`.

**C82 (Anil's 2 cakes, 5 children; 10 children) and C83 (1/2 = 2/4 = 3/6 by sharing rotis): OPTIONAL.** The book's own pictures
(Group 1 / Group 2 on p.167; "Let us draw and share" on p.167) would clearly help, and the plan has no teaching image of them, but the
questions state every number and the LP answers are plain text/fractions, so they are not needed to attempt or follow the example.
Both pictures are accounted `none:TEXT_SUFFICIENT`. If a budget for optional figures appears, these two are the best candidates:
C82 = two rows, Group 1 (2 cakes over 5 children) and Group 2 (two such blocks, 4 cakes over 10 children); C83 = three situations of
rotis cut in halves with their share boxes. Not added (v3 run adds only required figures).

**C58 (classify the fractions in two groups): none, LATEX_TABLE.** The book's table (p.161) is blank headings only; the fractions are in the
question and the answer is two lists. I did not draw a number line of 21 fractions (the blue/black lines are 7.4 pictures of another chunk).

**C60, C61, C62, C63, C64, C65: none.** The book prints only equation chains / labelled equations here:
- C63: the under-brace "3 x 1/3 = 1" is an `\underbrace` in LaTeX (text_alternative written).
- C64: the "Fraction" / "Mixed number" labels are `\underset` labels (text_alternative written).
Fraction-bar models of 3/2, 5/2, 4/3, 8/3 would help weaker learners but the book has none and nothing needs one, so I did not add them.

**T14 Figure it Out 7.5 Q1 to Q6: all 12 items none.** No figure is given in any question; the printed answers (pdf pp.40-42) are text
(sentences, whole parts, mixed numbers, bare fractions, one expansion chain), so the solution side adds nothing visual. Same decision for
all six (sibling consistency).

## 2. Things in the LP that look wrong or thin

- **C83 question text repeats its parts**: "(a) 1 roti divided equally between 2 children, (b) ..., (c) ... Is the share of every child the same? a) 1 roti ... b) ... c) ...".
  The three situations are written twice. Needs cleaning in the LP text.
- **C58 steps** say "The blue lines all ended before 1 / The black lines (...)", which only makes sense with the 7.4 number-line pictures. A learner
  reading this block alone cannot see blue or black lines. Also the question says "the fractions you marked on the number line earlier" and lists
  them in brackets; the list is the LP's own assembly from several 7.4 exercises (it includes 1/10, 3/10 and 4/5 from the 7.4 draw-on-a-number-line
  exercise), the book itself prints no list. Answer lists are consistent (16 + 5 fractions, all checked).
- **T14 numbering**: the LP numbers the questions Q1 to Q6 in one run, the book has three Figure it Out blocks (p.162: Q1, Q2; p.162: Q1, Q2, Q3; p.163: Q1)
  and the printed solutions use the book's numbering. `book_number` "Figure it Out 7.5, Q3/Q4/Q5/Q6" are therefore not the book's numbers
  (they are FiO2 Q1/Q2/Q3 and FiO3 Q1). The ncert_refs are right.
- **T14 Q4 (C74)**: the LP answer adds "All other fractions greater than 1 can be written as mixed numbers", which the printed answer does not say (true, fine).
- **T14 Q3 (C72)**: the question asks only for the number of whole units; the LP steps also give the mixed number (2 + 2/3, 2 + 1/5, 2 + 1/4). Extra, correct.
- All other sums and counts re-checked against the book and printed answers: 7/2 = 3 + 1/2; 4/3 = 1 + 1/3; 7/3 = 2 + 1/3; 8/3, 11/5, 9/4 = 2 + 2/3, 2 + 1/5, 2 + 1/4;
  Q5: 4 1/2, 1 4/5, 1 2/19, 5 2/9, 1 1/11, 3 1/6; Q6: 13/4, 23/3, 85/9, 19/6, 25/11, 39/10; C65: 3 + 3/4 = 15/4. No contradiction with the printed answers.

## 3. Places where the book itself is unclear

- p.164 strip picture: only some fold creases are printed (listed above), a plain top strip labelled 1 is drawn but not mentioned in the text.
- p.161 table: blank (the learner fills it), so the book has no printed answer to compare with the LP lists.
- p.162 "Fraction / Mixed number" labels: the arrow of "Mixed number" points at the whole part 2 of "2 + 2/3" while the text says the whole sum is the mixed number.

## 4. Figures not claimed (they belong to the next chunk's questions, so I left them to it)

P14-fraction_wall-1 (wall questions q3 to q6), P15-fraction_wall-1, P15-equation_boxes-1 (Figure it Out 7.6), P16-arrangement-1 and SOL43-arrangement-1/2
(three-roti and two-roti questions), P18-answer_boxes-1, P18-arrangement-1 (rotis shared among 3, 6, 9 children). P17-arrangement-1 is the picture of Anil's group
and also fits the next topic's "Anil's cake" question; I claimed it for C82 (optional); if that chunk maps it differently the merge keeps both uses.
