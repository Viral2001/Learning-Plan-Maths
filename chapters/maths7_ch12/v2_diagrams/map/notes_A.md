# Chunk A notes: Class 7 Ch 12 "Another Peek Beyond the Point" (v32 -> diagram map)

Chunk A = topics M1.S2.T2, M1.S3.T3, M1.S5.T5, M1.S6.T6, M1.S7.T7, M1.S8.T8, M1.S9.T9, M1.S10.T10 (16 units, 30 items).
Result: required 1 / optional 0 / none 29. Validator: errors 0, warnings 0.
Book pages used: 1 to 7 (all looked at as pictures). There is no printed-solutions section, so the LP solution text was the answer to follow.

## 1. Judgement calls

1. **Example 4 question (M1.S5.T5.C21) = the only required diagram.** The book question is "Find the area of the given rectangle" and the book draws the rectangle with 13.3 cm under the bottom side and 5.7 cm along the left side. The LP question text repeats both lengths, so a student could attempt it from text; I still marked it required because the book question GIVES a figure and the prompt's own typical pair (Step E) is "figure-based question, numeric answer: Q required, S none". If the reviewer wants the stricter tie-breaker ("could a careful student solve it from text alone?"), flip it to none (TEXT_SUFFICIENT); nothing else depends on it. The diagram is drawn exactly to scale (7.0 x 3.0 units = 13.3 : 5.7); the book draws it about 1.9 : 1, not to scale. It shows no area, no working and no vertex letters. Its solution is `none` (SAME_AS_QUESTION_DIAGRAM + LATEX_ARITHMETIC): area is a number and nothing is marked or split.
2. **M1.S3.T3.C9 / C10 (expansion table, p.2): both sides none (LATEX_TABLE).** The book table (Fraction | Expanding the Numerator | Sum of tenths, hundredths, thousandths | Decimals, one solved row 254/1000) is a plain table with no colour meaning, and the LP text already names the three fractions and the form wanted. The only counter-argument is that a filled table is also listed under ANSWER_IS_FIGURE (Step B); I kept text because the LP solution already writes every row out in four steps and the brief says plain tables of numbers stay text/LaTeX. If the user prefers a filled-table picture, the solution side is the one to flip (the table has 4 columns, 3 filled rows, stacked fractions).
3. **Digit-count table (p.4-5, worked example M1.S8.T8.C35): none (LATEX_TABLE).** Plain table of digit counts, bold numbers only, and the LP steps already state every count. The existing kept image M1.S8.T8.C35.IMG1 (10 by 10 grid, tenths times tenths) is a different teaching figure and is untouched, so no new id was created for this concept.
4. **Decimal-places brace figure (p.5) and Example 5 call-out (p.6): none for M1.S9.T9 and M1.S10.T10 solutions.** The answer in each case is a single number found by counting places; the LP steps say "2 + 1 = 3 decimal places" and "1 + 2 = 3" in words. The brace figure is already the teaching image M1.S8.T8.C36.IMG1 (never linked). Sibling check: unit 15 and unit 16 solutions got the same decision.
5. **Hop-arrow rule picture (p.2-3), worked example M1.S2.T2.C5: none.** Not a lettered/referred figure, the LP steps describe the hops in words, and the picture is the teaching image M1.S2.T2.C4.IMG1.
6. **Figure it Out coin stack (M1.S7.T7.C31, book Q5)**: the book draws nothing for the "cylinder of 36 coins"; a stack picture would only decorate, so none.
7. **Sibling consistency**: all five Figure it Out items (book Q1, Q3, Q4, Q5, Q7) and Examples 1 to 3 have the same decision (question none, solution none, text/LaTeX). Example 4 differs only because the book gives a figure there (see 1).
8. **Figures left to other chunks**: P06-table-1 (Situation 1/2/3 table, LP topic M1.S12.T12) and P08-table-1 (Figure it Out Q10 table, LP topic M1.S11.T11) are in the book pages my units touch but belong to those other units, so I did not claim them. If neither chunk claims them the merge check will flag them.

## 2. Things in the LP that look wrong or thin

1. **Figure it Out numbering does not follow the book.** M1.S7.T7 labels its five items "Figure it Out 4.2, Q1 to Q5" but they are book Q1, Q3, Q4, Q5 and Q7 (ncert_refs FiO1, FiO3, FiO4, FiO5, FiO7 are right, `book_number` is not). M1.S11.T11 restarts at "Q1 to Q4" (book Q2, Q6, Q8, Q10) and M1.S13.T13 has another "Q1" (book Q9). The same label "Figure it Out 4.2, Q1" therefore appears three times.
2. **The Jonali-Pallabi game board (p.1) has no question or answer item.** The seven fractions (3/10, 4/100, 67/1000, 457/100, 71/100, 43/100, 9/100) and the six blanks only appear inside the teaching concept M1.S2.T2.C3 (its step 3 lists the answers). Not a diagram problem, but a practice item is missing; I mapped P01-table-1 to `none:LATEX_TABLE` for that reason.
3. **M1.S3.T3.C9 (expansion table)**: the question text does not mention the table or the solved model row (254/1000 = 200/1000 + 50/1000 + 4/1000 = 2/10 + 5/100 + 4/1000, 0.2 + 0.05 + 0.004 = 0.254). The `q_figure` hint describes it, but the LP question text alone gives no model of the layout. The LP solution text matches the book's pattern and all arithmetic checks.
4. **Example 4 question** (M1.S5.T5.C21) says "a rectangle 5.7 cm by 13.3 cm"; the book says "the given rectangle" with the lengths only in the figure. Fine for the LP (text carries the data), noted for the figure decision above.
5. **Arithmetic check of every LP solution of the chunk**: all products, sums and conversions were recomputed and are correct (e.g. 57 x 133 = 7581, 125 x 75 = 9375, 1.45 x 36 = 52.2 mm = 5.22 cm, 6.4 x 50 = 320, 58 x 124 = 7192, 57 x 1335 = 76095). No LP solution contradicts the book.

## 3. Places where the book itself is unclear

1. **Example 4 rectangle is not to scale**: drawn about 1.9 : 1 although 13.3 : 5.7 = 2.33 : 1. My spec draws it to scale.
2. **Digit-count table is split over two pages** (p.4 rows 1-2, p.5 rows 3-4, header not repeated); treated as one table.
3. **Book wording "one-thousands"** in the table header (p.2) is printed that way (should read one-thousandths); the LP uses "thousandths".
