# Notes, chunk E (M3.S21.T21, M4.S22.T22 to M4.S26.T26)

Result: required 0 / optional 0 / none 29 (12 question, 12 solution, 5 worked example). Validator: errors 0, warnings 0.

I looked at the page pictures of pdf pages 16 to 20 (book pp. 122 to 126) and solutions pages 30, 31 and 33. They hold no figure that belongs to this chunk: only text, Math Talk icons and the remainders table. The 2 x 2 "special numbers" box on page 20 is section 5.6 (not this chunk).

## 1. Judgement calls

1. **Remainders table (M4.S24.T24.C148, the printed answer of book Figure it Out 5.5 Q4; base figure SOL33-table-1).**
   The printed answer is a plain black-and-white 4 x 8 table with no shading or highlight. I chose `none` with `LATEX_TABLE`, not a required picture. Reasons:
   - the v3 Step C rule names a plain table of numbers as LaTeX;
   - the LP steps already hold all 21 remainders (I recomputed them: they match the printed table);
   - the question side has no figure.
   Against this, Step B2 lists "filled table" under `ANSWER_IS_FIGURE`. If the user wants the book's table drawn as a picture, flip C148 to `required` (question has none, so `derived_from` null, token `steps_tex` / `before_first_step`). A LaTeX array is given in `text_alternative`.
2. **Worked examples C134, C135, C136, C137 (T22) and C149 (T25): `no_image`.** The book prints no figure for any of them and the steps are complete in words or sequences. The teaching images C134.IMG1, C136.IMG1, C137.IMG1 and C149.IMG1 stay as they are and are not linked. Pictures I considered and rejected as "only nicer": a tick-grid for 2 to 10 beside 8560, a number line showing 125 between 120 and 130.
3. **T26 Q1 ("list the multiples of 4 from 1 to 200").** A 1 to 200 grid with multiples shaded would help pattern-spotting, but the book prints none, the question gives no figure and the LP answer only needs six numbers. Left as text.
4. **Sibling consistency.** All five "Figure it Out" and Math Talk style answer sets in this chunk (5.4 Q1 to Q4, 5.5 Q3 and Q4, T23, T26) are word or arithmetic answers, so all take the same decision (`none`).
5. **No new figures.** I added no `NEW-` figure; nothing else on these pages carries mathematical content.

## 2. Things in the LP that look wrong or thin

- **Duplicated sub-parts in the question text.** `question_tex` and `text` of M3.S21.T21.C126, C128 and M4.S24.T24.C145, C147 list the parts (a) to (d) / (a), (b) / (a) to (c) twice (the prose version, then the "a)" version). Same in M4.S26.T26.C157 (the three statements, then a second, truncated copy: "If last two digits divisible by 4 then number is", "...then last two digits are"). Worth cleaning in the text, nothing for a diagram.
- **LP numbering vs the book.** T24 is titled "Figure it Out 5.5" with `book_number` "Q1" and "Q2", but they are the book's Q3 (sum of evens / odds, `ncert_refs` 5.5.FiO.Q3) and Q4 (remainders, 5.5.FiO.Q4). Book Q1, Q2, Q5, Q6, Q7 of that set are in other topics (chunk F).
- **Descriptive `book_number` on T23 and T26 questions** ("Divisibility by 10: numbers that end in 0", "Divisibility by 4: multiples near 330, 1730 and 2030", and so on): these are not book numbers; they are Math Talk / margin questions of 5.5 (pp. 123 to 124).
- **M4.S26.T26.C154 `answer_tex` is cut off:** "A number is a multiple of 4 when the number formed by its last two digits is." The same ending is in `answer`. It should end "...is a multiple of 4" (the printed book answer has no list or rule at all for this question).
- **M4.S26.T26.C153 asks for the list of multiples of 4 from 1 to 200** but the LP answer gives only the three ranges (332 and 336; 1732 and 1736; 2032 and 2036). The book's answer page does not give the 1 to 200 list either. Not a diagram matter.
- **M3.S21.T21.C133 (Guna, "any two primes co-prime?").** The LP is more careful than the book: it adds that a prime with itself (3 and 3) is not co-prime. The book's printed answer is only "Yes, for example 2, 3; 3, 11". The LP wins, as the brief says.
- **Arithmetic checked (all agree with the LP):** every factorisation in 5.4 Q1, Q2 (225 = 3x3x5x5, 27 = 3x3x3, 96 = 2^5 x 3, 24 = 2^3 x 3, 999 = 3x3x3x37, 99 = 3x3x11, 343 = 7^3, 216 = 2^3 x 3^3, 57 = 3x19, 85 = 5x17, 121 = 11^2, 1331 = 11^3); 8560 divisible by 2, 4, 5, 8, 10 and not by 3, 6, 7, 9; 395 as the largest multiple of 5 below 399; multiples of 2 from 400 to 410 (six numbers); 8536 / 4 = 2134; 124, 364, 4028 all multiples of 4; the 21 remainders of the table.

## 3. Places where the book itself is unclear

- Solutions p.30, Figure it Out 5.4 Q1: the printed labels read a, b, c, **c** (the last one, 343 and 216 "Yes", should be d). The LP uses (d).
- Solutions p.30, Q2: the printed answers are a Yes/No followed by a fraction (first number's factorisation over the second's) with no sentence saying "divisible"; the LP spells this out in steps.
- Solutions p.31, Q4: the printed answer "Yes, for example 2, 3; 3, 11 (Try other examples)" is silent on the same-prime case (see above).
- Solutions p.33, Q4: the table header says "Numbers" and "a) / b) / c) Remainder when divided by ..."; the question statement itself says "(a) 10, (b) 5, (c) 2" on p.126 and "i) 10, ii) 5, iii) 2" in the solutions: same content, two labelling styles.
