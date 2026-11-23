# Chunk D notes (Class 6 Ch 7 Fractions, units 51-66, topics T16 to T20)

Result: 31 items, required 14 / optional 1 / none 16, validator errors 0 (5 warnings: the 5 wall/roti-answer solution
diagrams that highlight or fill a book picture and are not themselves a printed book figure; expected).

## 1. Judgement calls

1. **Units 51-54 (fraction wall questions, 7.6.q3 to q6): question required, solution required (all four alike).**
   The LP question text itself says "Look at a fraction wall where 1 unit is split into halves ... sixths", so the 6-row wall
   (book p.14) is referenced and carries the data (FIG_REFERENCED, DATA_IN_FIGURE). Four identical question figures (one per item,
   `render_note` says "same as ...C87.IMG1"). Solutions: the LP solution rests on what is seen on the wall ("the piece 1/2 ends exactly
   where 3/6 ends"), so the figure adds the outlined lengths (ANSWER outlines, MARK_FILL cells, a dashed FOCUS end line). For q5/q6 the
   1/6 pieces are outlined one by one so the count 3 / 2 can be seen; for q3/q4 each length is one block. Alternative if the team wants
   fewer images: make the four solutions `none` (SAME_AS_QUESTION_DIAGRAM); I judged the highlight is the whole argument.
2. **Unit 56 (rotis shared in 3 situations, 7.6.q10): question required, solution required.** Judgement call. All numbers are also
   in the LP text, so a strict reading gives `none` (TEXT_SUFFICIENT / DECORATIVE_ONLY). I chose required because the book question
   is built on the picture ("situations shown below"): repeated groups of 2 rotis and 3 children make the "Why are the shares the same"
   visible, and LP steps 2 and 3 use exactly that grouping ("two groups of ...", "three groups of ..."). The LP's own `q_figure` /
   `s_figure` hints also expect a picture. If the team prefers text-first, switch both sides to `none` and drop the two media ids
   `M2.S16.T16.C97.IMG1`, `M2.S16.T16.C98.IMG1`.
   - The book prints 2/3 under each child of the FIRST situation as an example. The LP question also asks for (a), so the question
     figure leaves ALL boxes empty (no answer leak); the solution figure fills every box (3 x 2/3, 6 x 4/6, 9 x 6/9, one per child).
   - Layout: the book's picture is one long strip; I kept it as one strip (3 situations, solid separators between situations, dashed
     between sub-groups) in the 16:9 card. It is wide (12.7 of 14.22 units) and 3.5 units high, so the card has white space above and
     below; text height 0.26 units (about 26 px on the 1456 px card), the same as the minimum 34 px on a 1920 px canvas.
   - No text in the question figure: the three callouts of the book ("2 rotis divided equally among 3 children", ...) are already in the
     LP question text.
3. **Unit 57 (Figure it Out Q1: are 3/6, 4/8, 5/10 equivalent?): question `optional` (not added), solution required.**
   The printed answer ("In the fraction wall their lengths can be seen to be equal") and the LP answer ("On the fraction wall all three
   lengths are equal") both point at a wall that the LP never shows, so the solution figure is the full 10-row wall to 1/10 with the
   lengths 1/2, 3/6, 4/8, 5/10 outlined on one common end line. The LP question text names no figure and halving settles it, so the
   question side is `optional` (the wall would help; not needed), not required. This is the 'refer picture' idea of Step B2, but the
   wall is NOT a concept image of the plan (the 22 concept images do not include it), so the formal rule (REUSES_CONCEPT_IMAGE) does
   not apply; I drew the wall with `derived_from: null`. FiO Q2 and Q3 (same wall nearby) stay `none`: their printed answers are
   text and do not depend on the wall (sibling reason given in the items).
   - Label style: the 10th row is too narrow for stacked fractions at a readable size, so both walls use inline "k/n" labels.
   - Row 7 of the book's wall prints its last label as 1/7 (printing slip for 7/7, see section 3); the spec draws 7/7.
4. **Unit 60 (FiO 2 Q1, 3 rotis for 4 children): question required (book gives the picture), solution required** (printed answer is a
   picture, solutions p.43). The printed picture shows only 3/4 under each child; I added, under each child, a "three quarters of a
   roti" share picture (3 filled quarters + 1 dashed empty quarter) so the sharing is visible, matching the LP step "3 quarters each".
   Brief says solution = question + answer, so the rotis and children keep their positions.
5. **Unit 61 (FiO 2 Q2, 2 rotis for 4 children): question `none`, solution required.** The learner has to draw the picture and the book
   gives no figure ("a question with no given figure gets no question diagram"); the printed answer is a picture (solutions p.43), so the
   solution draws the whole thing (`derived_from: null`), with a half-roti share picture and 1/2 under each child. Same decision type
   as Q4's solution (sibling consistency). Unit 62 (Anil, 2 cakes) is `none` on both sides: the printed answer is text only, no
   sibling clash.
6. **Unit 55 (four more fractions equal to 1/2):** the book's four empty boxes carry no data, the answer is a list of fractions:
   `none` both sides (TEXT_SUFFICIENT/OPEN_ENDED; NUMBER_LIST_IN_BOXES/LATEX_ARITHMETIC). Mapped `P18-answer_boxes-1` to
   `none:NUMBER_LIST_IN_BOXES`.
7. **Units 64-66 (lowest terms, worked 36/60, example 16/20, FiO 4 Q1):** no figure in the book pages 22-23 or in the printed answers
   (pages 45-46 checked): all `none` (LATEX_ARITHMETIC). The concept image M2.S18.T18.C113 (saplings, 16/20) is not linked.
8. Question figures keep to what the book prints: no shading, outlines or labels beyond the wall labels (units 51-54) and the empty
   boxes (unit 56). Whole-figure colours: house CELL_FILL for the wall (the book's light blue), INK strokes, no faces on the
   children, no head colours.

## 2. Figure inventory claimed by chunk D (11 entries; check at merge)

P14-fraction_wall-1 (+ 3 NEW- entries for the 2nd to 4th use) -> the four wall questions; P15-fraction_wall-1 -> solution of FiO Q1
(unit 57); P15-equation_boxes-1 -> none:LATEX_ARITHMETIC; P16-arrangement-1 -> unit 60 question; SOL43-arrangement-1 / -2 -> unit 60 /
61 solutions; P18-arrangement-1 -> unit 56 question; P18-answer_boxes-1 -> none:NUMBER_LIST_IN_BOXES.

Possible merge overlap: chunk C holds the T15 teaching topic of section 7.6 (pages 14-18 strips, roti/quarters, Group 1/2, "draw and
share"). I did NOT claim P14-strip-1, P15-arrangement-1, P17-arrangement-1, P17-arrangement-2 (they belong to C's worked examples and
concept images C79 / C81). I claimed P15-fraction_wall-1 because FiO Q1 (my unit 57) uses it; if chunk C also claims it as `none:...`
the merge will show a conflict: my meaning is "drawn on the solution side of M2.S17.T17.C100".

## 3. Things in the LP that look wrong or thin

- **Unit 56 question text duplicates the callouts.** `question_tex` reads "...Why? (a): 2 rotis among 3 children; (b): 4 rotis among 6
  children; (c): 6 rotis among 9 children" after the same three items were already listed: the sentence appears twice (the second copy
  is the figure's callout text). Worth cleaning when the LP text is synced. Also the old `q_figure` hint says "an empty box under every
  child"; the book has ONE box per group of 3 children (and the first one pre-filled).
- **Unit 56 `s_figure` hint** says "every box showing the share: 2/3 in the first, 4/6 in the second and 6/9 in the third"; in the book's
  own style (the p.167 'draw and share' picture) the share is written once per child, so the spec writes it under each child.
- **Unit 57 answer text points to "the fraction wall"** (steps: "All three show the same length"), but the question text and the LP never
  show a wall. The solution figure now supplies it. Unit 57 also reuses the sentence "fraction wall" for the 6-row wall in units 51-54:
  the two walls differ (6 rows vs 10 rows).
- **Unit 60 question text says "Show the division"** but the learner cannot draw on the LP picture; fine for a paper book, odd on screen.
  The solution picture shows the answer.
- **Unit 66 labels:** the NCERT page prints the parts as "a. b. e. d." (the third is an `e` typo for `c`; the printed solutions page
  46 prints "c."). The LP uses (a), (b), (c), (d): fine. Recomputed: 51 = 3 x 17 -> 1/3; 64/144 = 4/9 (/16); 126/147 = 6/7 (/21);
  525/112 = 75/16 (/7, 75 = 3x5x5 and 16 = 2^4 share nothing): all agree with the book.
- **Unit 52 step 2** "Each 1/3 is made of 2 pieces of 1/6": correct. **Unit 51 step 2** is a long chain "3 pieces of 1/6 make 3/6, and 2 halves
  make 1 whole, 6 sixths make 1 whole, so half of 6 sixths is 3 sixths": correct but clumsy.
- Recomputed counts: unit 53 6 / 2 = 3; unit 54 6 / 3 = 2; unit 60 3 x 4 = 12 quarters, 12 / 4 = 3; unit 61 2 x 2 = 4 halves; unit 62
  2 x 5 = 10 pieces, 10 / 5 = 2 pieces = 2/5; unit 63 5/4 = 10/8, 4/3 = 12/9, 7/5 = 14/10.
- Book numbers: the LP's concept names ("Figure it out: Q4 ... Q7") are renumbered continuously (Q4 is the book's FiO 2 Q1) while
  `ncert_refs` use the book's own FiO groups (7.6.FiO1, FiO2, FiO3, FiO4). Not a problem for the figures; flagging for the report.

## 4. Where the book is unclear

- The last label of the sevenths row of the 10-row wall (book p.15) is printed "1/7"; the spec draws 7/7 (cell and position unchanged).
- Printed answer picture of FiO 2 Q1 (solutions p.43): rotis are drawn above-left and not connected to particular children; the
  alignment is approximate. The spec uses a clean centred layout instead of copying the offsets.
- Printed answer picture of FiO 2 Q2: the two rotis are drawn far apart, roti 1 above the gap between children 1 and 2 and roti 2 above
  the gap between children 3 and 4; the spec keeps exactly that pairing (centres x = -1.7 and 1.7).
- The solutions pages (42-46) print no answer for p.167 "find more fractions equivalent to 1/2" nor for the roti sharing question
  (7.6.q10, p.168); the LP solution texts are used as written.
