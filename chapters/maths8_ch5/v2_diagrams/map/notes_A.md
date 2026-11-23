# Notes, chunk A (Class 8 Ch 5 Number Play, topics M1.S2.T2 to M1.S11.T11)

Result: 29 items, required 1 / optional 0 / none 28. Validator: errors 0, warnings 0. Base figures claimed: 25
(1 item, 10 concept images, 14 none).

Book pages used: pp.1-11 (teaching text, tables, dot pictures), pp.21-22 (end-of-chapter Figure it Out Q3 and Q9) and the
printed-answer pages pp.25, 26, 32, 34. All page pictures were looked at; the answer pages carry no figure.

## 1. Judgement calls I was unsure about

- **M1.S8.T8.C25 question: required** (`FIG_REFERENCED`, `DATA_IN_FIGURE`; media id `M1.S8.T8.C25.IMG1`). The book task (p.6-7) says
  "Look at the following expressions and the visualisation. Write the corresponding explanation and examples." and prints the
  dot picture (blue p rows of 4 + yellow q rows of 4 with 2 over = stack, long arrow "(p + q) rows with a remainder 2") in the
  third table row. This is the only item of the chunk whose book question gives a figure that matters. The picture is not a
  concept image (the teaching image `M1.S7.T7.C24.IMG1` uses 4 + 6 = 10), and no concept image is linked anyway. The label
  "with a remainder 2" is printed in the book's own figure, so it is part of what the question gives. I re-flowed the book's
  two-line arrangement into one line for the 16:9 card (content unchanged); coordinates are in the spec.
- **M1.S8.T8.C26 solution: none** (`SAME_AS_QUESTION_DIAGRAM`). The book's picture is already complete; the LP solution adds
  algebra and three number examples in text, nothing new to draw. Therefore no `derived_from` pair either.
- **All worked examples of the chunk (C2, C4, C5, C16, C22, C23, C29, C30, C32): none.** They are arithmetic or algebra with
  no figure given. For C22, C23, C29, C30 and C32 the book's dot rectangles are teaching figures and the plan already carries
  them as teaching images (kept, never linked), so a second picture would only duplicate them.
- **Cards of expressions (C18 and C20 questions): none** (`NUMBER_LIST_IN_BOXES`). The book prints the expressions in boxes;
  nothing but the expressions is in them. Same decision for both (sibling rule).
- **Teaching figures with no matching concept image** (P06-dot_array-2, P08-dot_array-2, P08-dot_array-4, P09-dot_array-2):
  mapped `none:TEXT_SUFFICIENT`, because their content is carried by the algebra and numbers of the worked examples. They are not
  decoration, I only had no better code; a different code would be fine with me.
- **P04-tree_diagram-1** (the lettered a, b, c, d tree) is mapped to the numeric tree's concept image `M1.S2.T2.C3.IMG1`
  (same shape, 3 4 5 6 instead of a b c d), for accounting only.
- **Decorative characters not inventoried** (as the base does): the owl boxes on p.4 and the boy with the speech bubble on p.10.
  Their words ("Can I write an even and an odd number as 2n and 2n+1 instead?") are in the LP text.

## LP text issues

- **M1.S8.T8.C25 (question) and M1.S8.T8.C26 (solution):** the question text never mentions the dot picture that the book gives
  ("Look at the following expressions and the visualisation"), yet the solution says "The full rows stack up and 2 dots are always
  left over", which only makes sense with the picture (or the teaching image of the previous topic). Suggested question sentence,
  to be placed before "write the explanation and examples": "Look at the expressions 4p + (4q + 2) = 4p + 4q + 2 = 4(p + q) + 2 and
  at the picture below, where p rows of 4 dots are joined to q rows of 4 dots and 2 more dots."
- **M1.S6.T6.C20 (question):** the book's list of algebraic expressions has nine cards; the LP lists eight (x^2 + 2 is left to the
  worked example C16, where it is handled). Suggested: either add "x^2 + 2" to the question list and a line to C21, or leave as is
  because C16 covers it.
- **M1.S11.T11.C36 (question_tex):** brackets are written "(i):", "(ii):" etc. with a colon, the plain `question` field and the
  book write "(i)" without it. Cosmetic.
- **LP book numbers differ from the book's:** C11 says "Figure it Out, Q1" (book: Figure it Out Q2 on p.11); C13 says "Figure it
  Out, Q2" (book: end-of-chapter Q9, p.22); C9 and C36 say "Multiples and Remainders, Q1 / Q3" (book: Figure it Out Q1 / Q3 on
  p.11); C27 says "Figure it Out, Q1" (book: end-of-chapter Q3, p.21). These are the LP's own labels; I found the items by text.
- No wrong number was found in any LP solution of this chunk: I re-added every sum, factorisation and example (for example the
  eight signed sums of 3, 4, 5, 6 and the claim that 0, -2, -4 appear for every four consecutive numbers, a - (a+1) - (a+2) + (a+3)
  = 0 and so on).

## 3. Where the book itself is unclear

- p.8, P08-dot_array-2: the staircase boundary between regions p and q is hard to read in print (the base inventory says the same).
  No item uses it.
- Printed answer p.25, Q3 (ii): "30 is not divisible by both 18 and 9" is a wording slip for "by neither"; the LP uses 10, no problem.
- The brief says the pdf has no printed-solutions section; it does (answers on pp.25-37, headed "Page No. ..."). I used them
  to check the Figure it Out items; they agree with the LP solutions (Q1 7-10; Q2 p - 1 to p - 4; Q3 sometimes/sometimes/sometimes/
  always/sometimes; end-of-chapter Q3 m + n even; Q9 5p - 4, 5p - 2, 5p + 2, 5p + 4).
- No book print mistake that changes a spec value was found, so decision 1 (corrected values) did not apply.

## Borderline

- **M1.S3.T3.C8 solution (the eight signed expressions): none.** A completed sign tree with all eight results next to its leaves
  would be a faithful answer picture (the book says "You can use the diagram below to systematically list all the possibilities
  ... write the result next to it"). I kept it as LaTeX arithmetic because the answer is a list of eight sums and the tree is
  already the teaching image `M1.S2.T2.C3.IMG1`. If you want it drawn, it is a `number_pattern` tree: 3, two 4s, four 5s, eight 6s,
  leaves = the eight expressions with values 18, 6, 8, -4, 10, -2, 0, -12 (tree order +++, ++-, +-+, +--, -++, -+-, --+, ---).
- **M1.S6.T6.C19 and C21 solutions: none.** Could be the eight cards with the four even ones in ANSWER green; judged not needed
  (the answer is a verdict with a parity reason, not a drawing).
- **M1.S7.T7.C22 worked example: none.** Six dot arrays in rows of four (4, 12, 36 fill rows; 18, 22, 42 leave 2 over) would help
  but duplicate teaching image `M1.S7.T7.C22.IMG1`.
- **M1.S8.T8.C25 question: required** is itself the closest call of the chunk (the algebra alone is enough to attempt the task);
  I followed the book's own wording "and the visualisation" and decision 4 (no flipping to none because the LP text has the algebra).
