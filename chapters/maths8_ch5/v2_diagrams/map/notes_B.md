# Notes for chunk B (Class 8 Ch 5 "Number Play", plan cbse_eng_maths8_ch5_v36)

Chunk B = topics M1.S12.T12, M1.S13.T13, M1.S14.T14, M1.S15.T15, M2.S16.T16, M2.S17.T17: 14 pairs + 4 worked examples = 32 items.
Result: required 3 / optional 0 / none 29. Validator (`--chunk B`): errors 0, one expected warning (see "Q7 solution" below).

| Item | Decision | Media id |
|---|---|---|
| M1.S12.T12.C44 question (book Q16, four Venn options) | required | M1.S12.T12.C44.IMG1 |
| M1.S12.T12.C45 solution (Venn (iv) alone, with 4, 8, 32 placed) | required, derived_from C44.IMG1 | M1.S12.T12.C45.IMG1 |
| M1.S15.T15.C59 solution (book Q7 "show visually", dot rows) | required, derived_from null | M1.S15.T15.C59.IMG1 |
| every other item | none | - |

The worked-example units (C47, C48, C68, C69) are all `none`. Their kept teaching images (`C47.IMG1`, `C48.IMG1`, `C68.IMG1`, `C69.IMG1`) stay and are never linked.

## Borderline

1. **M1.S12.T12.C45 (Q16 solution) - required.** The book's printed answer is only "Ans. (iv)", and (iv) is already one panel of the question figure, so a plain copy of panel (iv) would be `SAME_AS_QUESTION_DIAGRAM` (none). I chose `required` (`ANSWER_IS_FIGURE`, the answer IS a Venn picture, B2) and made the figure add something: panel (iv) alone at 1.9x with the three example numbers that LP step 3 uses placed in their regions (4 in the outer set only, 8 in the middle ring, 32 in the innermost set), in ANSWER green. If the reviewer reads the rule strictly, the alternative is `none` / `SAME_AS_QUESTION_DIAGRAM` for this one item. The old LP author's hint (`s_figure`) also said "Diagram (iv) alone". `derived_from` = the question figure; note the solution is one panel of it, not the 2 x 2 layout.
2. **M1.S15.T15.C59 (Q7 solution) - required, and the question C58 - none.** The question says "Show the solution both algebraically and visually", the book's printed answer gives only the algebra and "For visual method refer P. 120 of the textbook", and LP step 4 describes the visual in words ("rows of 7 dots with 5 and 3 dots left over; the leftovers join to make a full row and 1 more, or 5 minus 3 leaves 2"). A word description of a dot picture does not replace the picture (B2, `ANSWER_IS_FIGURE`). The question side gives all its data in words and the book prints no figure with it, so no question figure (rule: no question figure when the question gives none). This is not the 'refer picture' case of B2: the question's data is not in a picture, and the picture the answer points to (7-wide dot rows for 7k, pdf page 9 / book p.120, base figures P09-dot_array-4/5) does not show remainders, so the solution draws its own figure (`derived_from` null).
3. **Worked examples C47 and C48 - none** although the book's What Remains? section has dot pictures and each concept already has a teaching image. The worked examples are plain remainder arithmetic and a short list of numbers; nothing asks the student to use a figure, and a teaching image is never linked. Tie-breaker: a careful student solves them exactly as well from the text. Same reasoning for C68 and C69 (place-value sums).
4. **Possible but not added:** C55 (pebbles, a number line of 31, 61, 91 with a divisible-by-7 check), C65 (the 12-periodic triples 2-3-4, 14-15-16), C67 (a table of remainder triples) and C51 (value table of 5k + 3 and 5k - 2) could each be drawn, but all of them are plain tables or number lists that the text carries (`LATEX_TABLE` / `TEXT_SUFFICIENT`). I gave C51 and C67 an optional LaTeX array in `text_alternative`.
5. **Venn colours.** The book tints the options differently (for example (i) blue, yellow, green but (iii) and (iv) in other greens/blues). The spec colours by set (4 = SET_A, 8 = SET_B, 32 = MARK_FILL) in every panel, so a colour always means the same set. Geometry, order of nesting and arrow targets are as printed.
6. **Figure letters.** Roman numerals (i) to (iv) are drawn in the Q16 question figure and (iv) in the solution figure because the LP answer says "Diagram (iv)" (decision 3). In the Q7 figure the panels are marked (i) and (ii) because LP steps 2 and 3 use "(i):" and "(ii):".

## Figure inventory (12 entries)

- `P23-venn_diagram-1..4` (the four given options, chapter p.23 = pdf page 23) -> `item:M1.S12.T12.C44 (question)`.
- `P37-venn-4` (the option printed again on the solutions page under "Ans. (iv)") -> `item:M1.S12.T12.C45 (solution)`.
- `P37-venn-1..3` (reprints of the options (i), (ii), (iii) on the solutions page) -> `none:SAME_AS_QUESTION_DIAGRAM` (the solution shows only (iv); these three are the same drawings as the question figure's panels).
- `P10-dot_array-1`, `P10-table-2`, `P11-table-1` (What Remains?: 5k + 3 as rows of 5, the values table, the 5k - 2 table) -> `concept_image:M1.S13.T13.C46.IMG1` (accounting only; plain tables / teaching picture).
- `NEW-P11-pebble-pot` (the pot character with pebbles beside the Q5 riddle on pdf page 11, missing from the base) -> `none:DECORATIVE_ONLY`.
- All base descriptions I used were checked against the page pictures (pdf pages 10, 11, 22, 23, 37); I found no wrong description. The base doubt on `P37-venn-2` (which set the yellow ellipse stands for) is real: the book draws option (ii) with the "Multiples of 8" arrow starting inside the overlap and the "Multiples of 32" arrow at the right ellipse, so the option is deliberately inconsistent (two ellipses for three sets). I drew it as printed.
- The solution M1.S15.T15.C59 has no inventory figure (the book prints no figure for it; it only points to P. 120), hence the one validator warning "required but no inventory figure maps to it". I did not claim P09-dot_array-4/5: they lie in the book section of chunk A.

## LP text issues

(No LP text was changed and no decision depends on these.)

- M1.S12.T12.C38, question_tex: `don'$t$` puts the letter t in math mode. Suggested: "other multiples of $11$ don't remain multiples of $11$ when doubled."
- M1.S12.T12.C40, question_tex: "(i): ... (ii): ..." have a colon after each numeral (the book prints "(i) ..."). M1.S12.T12.C41: step 5 "so (iv): is never true" and answer_tex "(i): always (ii): always (iii): always (iv): never" carry the same stray colon. Suggested: "so (iv) is never true" and "(i) always, (ii) always, (iii) always, (iv) never".
- M1.S12.T12.C44, question_tex: the question does not name the four options although the LP answer says "Diagram (iv)". Suggested sentence: "Which of the four Venn diagrams (i) to (iv) shown below captures the relationship between the multiples of $4$, $8$, and $32$?" (the figure is placed after the question text).
- M1.S14.T14.C51, answer_tex: `$5k + 3 (k$ from $0)$ and $5k - 2 (k$ from $1)$` has math mode opened and closed in the wrong places. Suggested: "$5k + 3$ (with $k$ from $0$) and $5k - 2$ (with $k$ from $1$); the other four do not work".
- M1.S14.T14.C50, question_tex: the six expressions have no numerals (i) to (vi) although the book numbers them (i) to (vi); the answer text does not refer to them by number, so this is cosmetic. The book prints (iii) as the fraction 3k over 5; the LP writes `3k \div 5` (same value).
- M1.S15.T15.C54 and M1.S15.T15.C62: the pronoun is typeset as `$I$` (math italic) and the contractions as `won'$t$` (C54). Suggested: plain "I take", "I hold", "won't".
- M1.S15.T15.C59, steps: the picture is a part of the solution (placed before step 1); step 4 begins "Visually:". Suggested: "Visually (see the picture above):" so the learner knows the figure belongs to this step. The m and n of step 1 are the row counts written on the figure.
- Numbering: the LP's `book_number` labels do not match the book. T12 "Figure it Out, Q1 to Q4" are the end-of-chapter questions Q11, Q12, Q14, Q16; T15 "Figure it Out, Q1 to Q7" are section-5.1 Figure it Out Q5, Q6, Q7, Q8 (FiO1) followed by end-of-chapter Q2, Q7 and Q13 (FiO4); T14 C52 "Multiples and Remainders, Q4" is section-5.1 Figure it Out Q4. Not a diagram matter; suggested only if the numbers are shown to students.
- Missing data: none found. Every number a required figure needs is in the question, the LP solution or the book (Q7: 661 leaves 3, 4779 leaves 5, divisor 7).

## The book itself

- Q16 option (ii) is internally inconsistent by design (see above); drawn as printed.
- Q7 printed answer: "For visual method refer P. 120 of the textbook". Book page 120 (pdf page 9) shows rows of 7 dots labelled "k rows" for 7k, but no remainder picture, so the pointer is vague. I took the visual from LP step 4 and drew it in the book's dot-row style.
- pdf page 11 carries the pebbles picture (pot character) that the base inventory skipped; added as `NEW-P11-pebble-pot`.
- Book mistakes needing a corrected value: none found in my chunk's figures.

## Geometry self-checks done in code (builder kept outside HERE)

- Q16: every arrow start lies in the region its label names; in (iii) and (iv) each shape is wholly inside the previous one (360-point check); in (i) 4 and 32 do not touch, 4-8 and 8-32 overlap; in the solution figure 4, 8, 32 sit in the outer set only, the middle set only and the innermost set respectively.
- Q7: 661 = 7 x 94 + 3, 4779 = 7 x 682 + 5, 4779 + 661 = 5440 = 7 x 777 + 1, 4779 - 661 = 4118 = 7 x 588 + 2; the figure shows 5 + 3 = 8 = 7 + 1 loose dots (5 SET_A + 2 SET_B in the full row, 1 SET_B left) and 5 - 3 = 2.
- A rough picture drawn from each spec was looked at for overlaps (label crowding, arrow ends, ring touching the box); the Q7 ring and the vertical arrows were moved after that look.
