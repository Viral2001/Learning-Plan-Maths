# Chunk D notes (Class 7 Ch 2, plan cbse_eng_maths7_ch2_v44)

Units: Figure it Out 2.4 Q1-Q4 (M3.S24.T24), three worked examples of "Solving Problems with Expressions" (M4.S25.T25),
Figure it Out 2.5 Q1-Q6 (M4.S26.T26), Puzzle "Expression Engineer" (M4.S27.T27). 24 items:
required 1 / optional 2 / none 21. Validator: errors 0, warnings 0.

## 1. Judgement calls

- **2.4 Q4 question (M3.S24.T24.C114): required, ONE diagram holding both pictures** (id `M3.S24.T24.C114.IMG1`, 16:9).
  The book question says "the numbers given in each picture below", so the pictures are the question (FIG_REFERENCED, DATA_IN_FIGURE).
  The pair is allowed one question diagram, so Picture I (3 x 3: yellow squares 4 at corners and centre, blue circles 8 at edge middles) and
  Picture II (4 x 4: blue 5 at corners and middle block, red 6 on the other edge circles) sit side by side, left and right as in the book.
  Checked against pdf page 19 and the reprint on page 37: the base descriptions are correct.
  Choices to confirm if you disagree: (a) the book's captions "(I)" and "(II)" (printed only on page 37) are NOT drawn, because figure letters are
  on the never-draw list and the LP text names the pictures; (b) the book's yellow / blue / red are approximated by the style-token pair
  SET_B (amber) for squares-4 and circles-6, SET_A (blue) for circles-8 and circles-5, as light tints with INK digits (the digit carries the
  meaning, not the colour). If you want an exact yellow/blue/red palette, the renderer needs three extra colours outside the token table.
- **2.4 Q4 solution (C115): optional, not added.** Both the printed answer (page 38) and the LP solution are arithmetic
  (5 x 4 + 4 x 8 = 52, 2 x (4 + 8 + 4) + (8 + 4 + 8) = 52, 8 x (5 + 6) = 88, 4 x 22 = 88). A marked-up copy of the question figure
  (braces 5 x 4 and 4 x 8, row totals 16, 20, 16, the 5s and 6s grouped) would help but a careful student loses nothing without it
  (tie-breaker -> optional, not required). If the team decides it wants it, the spec would be derived_from `M3.S24.T24.C114.IMG1`.
- **2.5 Q1 solution (C121): optional, not added.** Same logic: the snail part (c) would gain from a post with the height after each day and night
  (why 8 days and not 10) but the 7 x (3 - 2) + 3 = 10 line carries it, and the book prints no figure. Question side none (no given figure).
- **Everything else none.** All other questions and answers are fill-ins, comparisons, word problems and arithmetic (LATEX_ARITHMETIC / TEXT_SUFFICIENT / OPEN_ENDED).
  Siblings are consistent: all six 2.5 questions and Q1-Q3 of 2.4 are none on the question side; Q2/Q4/Q5 of 2.5 (sign and choice answers)
  and Q1/Q2 of 2.4 are none on the solution side.
- **Worked examples (baker, 57 x 30 - 20, 91 - (35 + 12)):** none. These are LP-made examples, not book figures; a 6 x 7 calendar for the baker would be nicer
  but the arithmetic carries it.
- **Inventory:** P19-pattern-1 and P19-pattern-2 both map to the Q4 question item (they are one diagram). P37-pattern-1 and P37-pattern-2 are the same
  two pictures reprinted in the book's answers section (with captions); the printed answer beneath them is text only, so they are
  `none:SAME_AS_QUESTION_DIAGRAM`. The Puzzle page (pdf page 22) has only the owl banner and the row of children: decoration, not inventoried.
  The distributive-property brace figures on page 17 (P17-braced_sum-1 and -2) belong to the section text, not to a unit of this chunk, so I did not claim them.

## 2. Things in the LP that look wrong or need a look

- **C108 question_tex (2.4 Q1) is garbled.** The (c) to (p) parts run together: e.g. `... 3 \times \underline{\hspace{1.2em}} (d)$: ...` (the next part label sits inside the previous
  maths), (i) has no `$`, and (m) to (p) are glued into one math span (`... 3 \times 7 (m) 5 \times (12 - ...`). The answer_tex of C109 has the same gluing
  (`$(l)$: $- (m)$ any $n (n) 6$ ...`). Not a diagram matter, but it will render badly; each part should be its own line.
- **C108 (e) in the book reads "3 ____ + ____" (the multiplication sign is lost in the print);** the LP reads it as `3 x ____ + ____`, which is the sensible reading. Book answer
  uses 10 in (e) and 3 in (m) with the remark "you may put any number other than 10 and 3 respectively"; the LP says "any number n works". Both fine.
- **2.4 Q3 solution differs from the book's printed answer:** LP gives 2 x (2 + 5), 2 x (3 + 4), 7 x (1 + 1), 1 x (5 + 9); the book gives 2 x (5 + 2), 2 x (3 + 4), 7 x (1 + 1), 2 x (6 + 1).
  All four LP fills equal 14 (14, 14, 14, 14). LP kept (it wins).
- **2.5 Q6 solution uses 24, the book uses 26.** All ten LP expressions for 24 check out (12 + 12, 4 x 6, 48 / 2, 34 - 10, 20 + 4, 30 - 6, 8 x 3, 100 - 76, 2 x (5 + 7), 72 / 3).
- **2.5 Q3(a):** the book's Way 1 groups all positives and all negatives; the LP gives the pairs method and a leave-out-the-ends method instead (both give -5). Fine.
- **2.4 Q4 question text restates the figure in words** ("Five squares ... eight cells show 5 and eight cells show 6"). With the diagram added this is redundant, and the last clause
  hints at the grouping the book wants the student to find. Suggest trimming it to the book wording once the figure exists (the data then lives only in the figure). Left as is, since I change nothing else.
- Stale ids: several answer items carry a `video_media_id` that belongs to the NEXT question's concept (e.g. C109's video is `C110.VID1`), and C117 and C118 share the
  concept name "Comparing and matching by reasoning". Ignored as instructed; items were matched by their own concept id.

## 3. Arithmetic re-checked (all hold)

- Q4 pictures: left 5 x 4 + 4 x 8 = 52, rows 16 + 20 + 16 = 52; right 8 x 5 + 8 x 6 = 88, rows 22 x 4 = 88.
- Baker: 7 - 1 = 6; 6 x 6 = 36; 36 x 14 = 504; 7 x 6 x 14 = 588; 1 x 6 x 14 = 84; 588 - 84 = 504.
- 57 x 30 - 20 = 1690, 57 x 31 - 20 = 1747, difference 57. 91 - (35 + 12) = 44, -35 + 91 - 12 = 44, 91 - 35 - 12 = 44, 91 - (35 - 12) = 68.
- 2.5 Q1: 7 x 20 = 140; 12 x 12000 = 144000, 240000 - 144000 = 96000; snail 7 x 1 + 3 = 10 on day 8.
- 2.5 Q2: values (a) 80, (b) 40, (c) 56, (d) 112, (e) 33, (f) 72, (g) 40, (h) 16. 2.5 Q4 and Q5 signs and values recomputed, all match the LP.
- Puzzle: 3 x (3 - 3) = 0, (3 + 3) / 3 = 2, 3 + 3 / 3 = 4, 3 x 3 - 3 = 6, 3 + 3 + 3 = 9, 3 x 3 + 3 = 12.

## 4. Where the book itself is unclear

- The Q4 pictures are printed with different gaps on page 19 and page 37 (page 37 has the circles of Picture II nearly touching); the spec uses pitch 1.4 for Picture I and 1.15 for
  Picture II and says so in `render_note`. Squares are very slightly smaller than circles in both prints (0.95 against 1.0).
- The book's text for 2.4 Q1 (e) loses the "x" sign (see above). Question 2.5 Q6's printed answer in the extracted text is partly garbled (the fourth line reads "52 / 4. 2", i.e. 52 / 2).
