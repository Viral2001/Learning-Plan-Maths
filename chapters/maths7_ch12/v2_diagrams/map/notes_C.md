# Notes, chunk C (Class 7 Ch 12, topics T23, T25, T26, T28, T29)

Result: 32 items, required 0 / optional 1 / none 31. Validator: errors 0, warnings 0.
Reason for zero required: every question and worked example in this chunk is decimal arithmetic (conversion of fractions, long division,
moving the point). I looked at book pages 17 to 21: none of these items has a printed figure, and no printed answer is a picture.

## 1. Judgement calls

- M2.S28.T28.C116 (Q3, 1 / 7, solution) = OPTIONAL. The old card hint (`s_figure`) says "a chain of arrows through the remainders 1, 3, 2, 6, 4, 5
  that returns to 1". That is the book's remainder chain (P19-flow-1) and it already exists as the teaching image C108.IMG1 (never linked in v3).
  The question asks to list the remainders and the LP steps list them all, so the tie-breaker gives "nicer, not needed". v3 section 3 ("a flow-chart
  of a procedure already drawn as a concept image -> none, or optional on the solution side") fits. If you want the picture, this is the only item
  to flip to required. The solution would then be a new diagram C116.IMG1 with the loop 1 -> 3 -> 2 -> 6 -> 4 -> 5 -> back to 1 (derived_from null,
  question has none). Text alternative given in the map: write the chain as LaTeX.
- M2.S28.T28.C118 (Q4, 142857 times 1 to 7, solution) = none, LATEX_TABLE. A column of seven products shows the cycling digits as well as a ring
  would; the ring is the teaching image C109.IMG1. This differs from Q3 on purpose: Q3's answer is a loop that closes (a chain), Q4's is a list.
- Long divisions (T23 Q1 and Q4, T25 both examples, T26 all four, T28 Q1, Q3, Q5): none, LATEX_ARITHMETIC. The v3 list says long division is
  LaTeX/text. The LP steps already say every regrouping in words. If the team later wants stair-case long-division pictures, the items to revisit are
  C85, C91, C96, C98, C100, C112, C116, C120 (solutions) only; no question gives a figure.
- M2.S29.T29.C121 (worked: 128 / 4 and 128 / 0.4): none, TEXT_SUFFICIENT. The number line with the two arcs is already the kept concept image
  C121.IMG1; a worked example never links it and does not need a second copy: three one-line comparisons are complete in text.
- M2.S29.T29.C122 (worked: 12.5 / 2.5, / 1, / 0.5 "and make a table"): none, LATEX_TABLE. The table is a plain 3-row table of numbers
  (divisor, quotient, bigger/equal/smaller than 12.5). Suggested LaTeX array is in the item's text_alternative. The book itself prints no such table
  (Math Talk on p.20 only asks the student to make one), so there is no figure to draw.
- M2.S25.T25.C95 (Example 12, Ravi 126 km in 2.5 h): none. The bar picture is the concept image C92.IMG1 (T24); the book prints no figure for the example.
- M2.S26.T26.C103 (book FiO Q4, blanks in equations): none. The blanks are underlines in `question_tex` (`\underline{\hspace{1.2em}}`), which is
  LaTeX, not a figure. The "box_equation" figures of page 28 are another chunk's.
- Base figures (all three on page 19, section "Does This Ever End?", which only my chunk's questions use):
  - P19-long_division-1 (10 / 3 stair-case) -> concept_image C107.IMG1 (same picture: long division of 10 by 3 with the remainder 1 circled).
  - P19-flow-1 (remainder chain) -> concept_image C108.IMG1 (title "The remainder chain of 1 / 7").
  - P19-long_division-2 (1 / 7 stair-case with three red circles) -> none:LATEX_ARITHMETIC. I did not map it to C108.IMG1 because that image is the
    remainder ring, not the long-division layout; the layout is LaTeX material. I checked all three descriptions against page_19.png: they are right
    (the `unclear` doubt on P19-long_division-2 is only about indentation, which does not matter as nothing is drawn). No "CORRECTED" needed.
  - No other base figure belongs to my units: pages 17 (FiO Q1-4), 18 (Examples 12, 13), 20 and 21 (FiO Q2-5, Dividend/Divisor/Quotient) have none.
    P17-long_division-1 is Example 11 (T22, chunk B) and P21-pattern-1 is the Math Talk box under FiO Q10 (later chunk).

## 2. Things in the LP that look wrong or odd

- Book numbers repeat. The LP labels the second "Figure it Out" set of section 4.3 as Q1 in T20 (book Q1, fractions to decimals), Q1 to Q4 in T26
  (book Q2 to Q5, ncert_refs FiOB2 to FiOB5 are right) and Q1 to Q5 in T30 (book Q6 to Q10). So "Figure it Out 4.3, Q1" appears three times in the
  plan (T20 C69, T23 C84 which is the first set and correct, T26 C99), and T26's labels are off by one against the book. Worth fixing in the
  `book_number` / concept names; not a diagram matter.
- T23 Q2 (C86): the book prints options (i) and (iv) of part (b) both as 4458.75 (book error). The LP question reproduces it and the solution
  explains it; fine, but a reader may think it is a typo of ours.
- T28 Q1 solution (C112) starts at "10 Ones / 3" and skips the book's first step (regroup 1 Ten into 10 Ones); harmless.
- T28 Q2 question text asks "Find 10 / 9 and 100 / 11" but the book's phrase is the closing line of the 10 / 3 box ("Can you find the quotients
  of 10 / 9, and 100 / 11?"); the LP is right.
- T23 and T26 solutions: I recomputed every value (3.6, 103.75, 608.5, 603.375; 381.5 and 445.875; 33, 3.3, 0.33, 0.033; 15.75 down to 0.001575;
  50.4; 3.6 and 36; 20.7166..., 3.768421...; 18.72, 156, 1.2, 0.01872; 1000, 0.1, 10, 0.1, 10, 100; 1.64, 16.4, 164; 1.111..., 9.0909...;
  the 1 / 7 remainders 1, 3, 2, 6, 4, 5; 142857 times 1 to 7; 0.0588235294117647 and its double; 32, 320; 5, 12.5, 25). All agree with the book.

## 3. Where the book itself is unclear

- Only the Q2 (b) options above (duplicate 4458.75).
- Page 21 prints Q5's last sentence as "24.6 / 1.5" with a stray space; the LP reads it as 24.6 divided by 1.5 (quotient 16.4, same as 2.46 / 0.15). Right.
