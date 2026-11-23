# Chunk A notes (Class 7 Ch 8, units 1-19: M1.S3.T3 to M1.S10.T10)

Result: 32 items. required 6 / optional 2 / none 24. Validator: errors 0, one warning (C42 has no inventory figure because the book prints none, see 1.5).

| role | required | optional | none |
|---|---|---|---|
| question | 0 | 0 | 13 |
| solution | 4 (C31, C33, C35, C42) | 2 (C8, C10) | 7 |
| worked_example | 2 (C26, C28) | 0 | 4 (C36-C39) |

## 1. Judgement calls

1.1 **Four-panel pictures for Figure it Out (C35 = book p.180 Q1, C42 = book p.181 Q2).** Each answer has four sub-answers (a)-(d), and the book prints four separate pictures for Q1 (pp.32-33). The brief says a pair gets at most ONE solution diagram, so each is one 16:9 picture with four unit squares side by side, captioned with the product (no panel letters, no "parts" labels). If the user would rather have four pictures per answer, the pair would need extra media ids (IMG2..IMG4) and the brief changed.
   - The fifth part of Q1, 1/12 x 1/18 = 1/216, is NOT drawn: a 216-cell square is unreadable, the book prints no picture for it and itself calls drawing it "cumbersome" (p.9).
   - Q2 (C42): the book prints no picture ("Draw the figure in the same manner as shown in question 1", p.34). I made the solution `required` for sibling consistency with Q1 (same instruction, same kind of answer). It follows the book's own convention (p.9): rows = denominator of the multiplicand, columns = denominator of the multiplier, band = top rows, product = left columns of the band. All four products were recomputed: 8/15, 2/12 = 1/6, 3/10, 12/30 = 2/5.
   - The question sides of Q1 and Q2 are `none`: they give no figure, the learner is asked to draw.

1.2 **T7 solutions C31 (1/2 x 1/4) and C33 (3/4 x 2/5) are `required`, although the answer is a number.** The LP solution steps themselves shade 1/4 of the unit square, cut it, and count "8 equal parts and 1 shaded" / "5 rows, 4 columns, 20 parts, 2 then 6 shaded". A learner cannot follow those steps without the picture and the book prints it (pp.6-7). The tie-breaker (would the picture change how easily they follow it) says yes. They repeat the two teaching examples (teaching images C25 and C27 show the same figures); v3 forbids linking a teaching image, so each gets its own copy (same layout, solution marks in ANSWER green). Question sides are `none` (no figure is given).

1.3 **Worked example C28 (5/4 x 3/2, Fig. 8.2) is `required` and duplicates the kept teaching image M1.S6.T6.C28.IMG1 in the same card.** v3 says a referenced numbered/lettered figure is drawn even when a teaching image shows it, and a teaching image is never linked. The new image gets id C28.IMG2 (IMG1 is kept). It shows the complete figure the steps read off (12 cells = 3/2, first column of 3 cells highlighted = 3/8). If the user prefers no duplicate inside one card, this is the item to change to `none`.

1.4 **Worked example C26 (area link, Fig. 8.3) is `required`.** The book question names Fig. 8.3 ("what is the length and breadth of the shaded rectangle"); the LP rewrites it as "in the unit square, a shaded rectangle ... 8 such rectangles fill the square" with no figure. Only the one shaded rectangle is drawn, with its sides 1/2 and 1/4 marked (the question gives them); the book's 1/8 arrow (the answer) and its yellow top row are left out. No teaching image shows this figure (C26 has no kept image).

1.5 **Figures mapped to two uses.** P06-fraction_grid-1, P07-fraction_grid-1 and P07-fraction_grid-4 are each claimed twice: the base id maps to the teaching image (accounting) and a `NEW-<id>-sol / -we` entry maps to the item that redraws it (rule: a figure used twice is two entries). Required item C42 has no printed figure at all, hence the validator warning (acceptable, see 1.1).

1.6 **T3 solutions C8 (tortoise, 3 hours) and C10 (Aaron, 2/5 hour) are `optional`.** The book draws a number line for each (p.1, p.3), but the answers are numbers, the LaTeX steps are complete (repeated addition; 3 / 5 then x 2) and the same lines are already teaching images (T1 C1 tortoise path; T2 C4 "3 km cut into fifths", which is exactly C10's picture). Picture only makes it nicer, so not added. Same decision for both (siblings). The earlier author's `s_figure` hints for these two are not followed.

1.7 **T9 worked examples C36 (1/12 x 1/18) and C37 (5/12 x 7/18) are `none`.** C36 literally says "without drawing the unit square"; both have 216-cell grids in the book (pp.9-10), which are only schematic ("18 parts", "12 parts") and are unreadable at card size; teaching images C36.IMG1 (3 x 6) and C37.IMG1 (3 x 5 overlap) already carry the rows-times-columns idea. C38 and C39 (whole number as n/1) are plain arithmetic.

1.8 **T4 (Examples 1, 2) and T5 (Figure it Out Q1-Q5)**: all `none`. No figure in the book, printed answers (pp.31-32) are text. Q4 (Moon, 10 pm + 2 1/2 h) could be a clock or time line but the book gives none and the arithmetic is complete.

1.9 **Figure inventory choices.** P01 is mapped to the nearest teaching image M1.S1.T1.C1.IMG1 (tortoise on a path); that image is the LP's own picture of the situation, not a copy of the book line. P02 and P03 map to M1.S2.T2.C4.IMG1. The pages 1-4 teaching figures belong to topics T1/T2 that have no unit in any chunk, so chunk A claims them (they sit in the book section of the T3 questions, which repeat the same two walks). P10-annotated_expression-2 (12/7 x 5/24, p.10) belongs to T11 (chunk B) and is NOT claimed here.

## 2. Things in the LP or the brief that look wrong

2.1 **Book numbers**: C41/C42 (T10) carry `book_number` "Figure it Out 8.1, Q1" but the question is Q2 of the second Figure it Out set (book p.181). C34/C35 (T8) is Q1 of the second set (p.180). The LP has three topics all labelled "Figure it Out 8.1" with overlapping Q numbers (T5 Q1-Q5 of the first set; T8 Q1; T10 Q2). I put the true book page and number in `ncert_ref`.

2.2 **The brief says the pdf has no printed-solutions section, but pdf pages 31-39 are one** (printed answers, with unit-square pictures on pp.32-33). I used it for the four Q1 pictures and the printed answers.

2.3 **Concept names**: C26 is named "Half of a quarter" but its block is the area-of-a-rectangle link (Fig. 8.3); the half-of-a-quarter teaching image sits in C25. C38 and C39 share the name "Whole numbers as fractions over 1". Unit-level `ncert_refs` are empty for C26 and C39 while their items carry refs (8.1.area_link, 8.1.whole_as_fraction). Cosmetic.

2.4 No LP solution contradicts the book. Every answer was recomputed: 3/4; 6/5 = 1 1/5; 10/3 = 3 1/3; 10; 7/2 and 31/2; 1/8 and 5/8 km; 5/3 and 20/3 l; 5/2 h so 12:30 am; 21/5, 4/3, 54/7, 78/11 with mixed forms 4 1/5, 1 1/3, 7 5/7, 7 1/11; 1/8; 15/8; 3/10; 1/15, 1/12, 1/10, 1/30, 1/216; 8/15, 1/6, 3/10, 2/5; 216; 35/216; 9/4; 12/5.

## 3. Places where the book itself is unclear or wrong

3.1 Figure (b) of the printed answer to Figure it Out Q1 (p.33) says "5 parts" under the grid although it has 4 columns (4 x 3 = 12). Not copied: the new picture has no parts labels.

3.2 p.10 prints "5/12 x 7/8 = (5 x 7)/(12 x 18)": the 7/8 is a misprint for 7/18. The LP has 7/18 (correct).

3.3 p.7 second arrow row says "Divide the multiplicand by 3" for the step that multiplies by 3, and ends in a dangling "=". Book wording, not drawn (accounted as `none:LATEX_ARITHMETIC`).

3.4 Printed answer to Q4 (p.31) reads "10 + 2 + 1/2 = 12 am Or 12:30 am"; the LP's "12:30 am" is the clean form.

3.5 The book's unit squares are drawn as rectangles in some pictures (for example p.33 (c) is 3:2); the new pictures draw every whole as a true square so that rows and columns show the fraction correctly.
