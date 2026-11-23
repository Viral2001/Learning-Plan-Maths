# Chunk A notes: Class 8 Ch 13 "Algebra Play" (cbse_eng_maths8_ch13_v28)

Units: M1.S2.T2 (1 worked example), M1.S3.T3 (5 pairs, Think of a Number Q1-Q5), M2.S5.T5 (6 pairs, Number Pyramids Q1-Q5 and Figure it Out Q1).
Result: 23 items, required 9, optional 0, none 14, validator errors 0 (2 warnings, explained under "Validator warnings").
Pictures checked: pdf pages 1 to 6 (page_01 to page_06.png). Page 1 has no figure (QR code and chapter art only). All base descriptions of my figures matched the pictures; no CORRECTED entry was needed.

## Decisions at a glance

| Unit / concept | Question | Solution |
|---|---|---|
| M1.S2.T2.C6 worked (change the steps) | none (TEXT_SUFFICIENT) | - |
| T3 Q1 C8/C9, Q2 C10/C11 | none | none (LATEX_ARITHMETIC) |
| T3 Q3 C12/C13, Q4 C14/C15, Q5 C16/C17 (date trick) | none | none (LATEX_ARITHMETIC) |
| T5 Q1 C25/C26 (three pyramids 6 2 / 3 4 3 / 5 4 5 0) | required, C25.IMG1 | required, C26.IMG1 (from C25.IMG1) |
| T5 Q2 C27/C28 (10 / 4 ? / 1 ? ?) | required, C27.IMG1 | required, C28.IMG1 (from C27.IMG1) |
| T5 Q3 C29/C30 (60 / ? ? / 12 ? 8) | required, C29.IMG1 | required, C30.IMG1 (from C29.IMG1) |
| T5 Q4 C31/C32 (three 4-row pyramids) | required, C31.IMG1 | required, C32.IMG1 (from C31.IMG1) |
| T5 Q5 C33/C34 (top from a, b, c) | none | required, C34.IMG1 (stands alone, derived_from null) |
| T5 Q6 C35/C36 (Figure it Out Q1, box rows) | none | none |

Diagram type for all nine: `other` with `layout: number_pyramid` (the catalogue has no pyramid type); every box has its centre coordinates in `content`, so the renderer has nothing to guess. Canvas 16 x 9 units (1 unit = 120 px).

## Borderline

1. **T5 Q1, Q2, Q3, Q4 question diagrams (required).** The LP text carries the bottom rows and where the blanks are, so a careful student could attempt from text. I kept them `required` (ACTION_ON_FIGURE + DATA_IN_FIGURE) because the book question IS the picture (it prints only pyramids with ? or empty boxes, and the student completes them), and because the filled pyramid is the answer (ANSWER_IS_FIGURE) and the four pairs are siblings. Per decision 4 not flipped to none. Q2 (10 / 4 ? / 1 ? ?) is also the book's teaching example and concept image M2.S4.T4.C19.IMG1 covers its steps; the item still draws its own given-state picture (v3: a concept image is never linked).
2. **T5 Q5 (C33 / C34).** Question `none`: the book prints no empty pyramid for this; the figure it prints on page 6 is the finished a + 2b + c pyramid, which is the answer. The question names the bottom row a, b, c in words, and the companion note says not to invent a question figure. Solution `required` (printed answer is a pyramid, B2): ONE diagram holding two pyramids side by side, the letter pyramid (a + 2b + c / a + b, b + c / a, b, c) and the numeric one the LP answer uses (23 / 10 13 / 1 9 4). Given bottom rows in INK, everything the solution adds in ANSWER green. Sibling note: Q1 to Q4 have a question figure, Q5 does not, because the book gives none.
3. **T5 Q6 / Figure it Out Q1 (C35 / C36), both none.** The book draws each case as a plain row of three boxes (4 13 8, 7 11 3, 10 14 25). The answer is one number per case and no pyramid is built, so the boxes carry nothing the text lacks (NUMBER_LIST_IN_BOXES, TEXT_SUFFICIENT; solution LATEX_ARITHMETIC). If the user wants the boxes drawn it is a one-picture addition; I did not add it.
4. **Date trick (C12/C13, C14/C15, C16/C17) and worked C6, all none.** The book shows the date trick only as the Shubham and Mukta comic strip (P02-dialogue_strip-1). I treated it as a procedure plus a number chain (26/01, 1 x 5 = 5, 5 + 6 = 11, 11 x 4 = 44, 44 + 9 = 53, 53 x 5 = 265, 265 + 26 = 291) with characters as decoration, i.e. number chains go to LaTeX (LATEX_ARITHMETIC), not a printed answer picture. If the user reads the strip as a "printed answer is a picture" case, the three solutions (C13, C15, C17) and possibly C12 would turn required with a `flow` style chain; they are the only place where this call could go the other way. C14, C16 follow C12 for sibling consistency. No concept image shows the strip, so no REUSES_CONCEPT_IMAGE.
5. **P05-number_pyramid-6** (the two-row lead-in a + b / a b): mapped `none:TEXT_SUFFICIENT`. No item uses it and no concept image shows exactly it (C23 shows the three-row version).
6. **Question marks versus empty boxes.** The book prints "?" in the unknown boxes of the page-4 pyramids (Q1, Q2, Q3 figures) and leaves them empty on page 5 (Q4 figures). I followed the book per figure.
7. **Letters in the Q3 solution.** The LP steps name the unknown boxes a, b, c, but the figure is not a lettered figure; the solution diagram shows the final numbers (32, 28, 20) only, as the book's filled pyramid does. Decision 3 (figure letters) does not apply to box names.
8. **One picture per side for Q1 and Q4** (brief: at most one question and one solution diagram per pair). Q1 holds the three pyramids in one picture, Q4 the three four-row pyramids (both LP blocks E0 and E1 of C31/C32).
9. **Figure accounting.** Teaching figures keep the base id with `concept_image:` (P03 -> C18, P04 steps -> C19, P05-1 -> C20, P06-1 -> C23). Where an item draws the same figure itself I added a `NEW-` entry for the second use (NEW-P03-number_pyramid-1-q5sol, NEW-P04-number_pyramid_steps-5-final, NEW-P06-number_pyramid-1-q5sol). P04-number_pyramid-4 and P04-number_pyramid-6 are labelled "teaching"/"given in question" in the base; both are the given state of Q2 / Q3, so they map to those question items. The page-4 pyramids 1 to 3 all map to C25 (question), the page-5 pyramids 3 to 5 to C31 (question). I did not claim P06-box_row-5, -6, -7 (Figure it Out Q3): that question is a unit of chunk B.

## Validator warnings (not errors)

C26 and C32 solution diagrams have no inventory figure mapped: the book prints no solution for these two (Q1 and Q4 fill-ups), the LP solution values are drawn. Fine per the validator message.

## LP text issues

- **M1.S3.T3.C12 (Q3), C14 (Q4), C16 (Q5):** the question text says "follows the steps" / "running the trick forward" / "the date trick" but never lists the six steps; in the book they appear only inside the comic strip. A student working the question alone cannot know them. Suggested sentence to add to each: "The steps are: think of a date, multiply the month by 5, add 6, multiply by 4, add 9, multiply by 5, add the day."
- **M2.S5.T5.C25 question_tex:** "bottom rows $6$, $2$ and $3$, $4$, $3$ and $5$, $4$, $5$, $0$" runs the three rows together. Suggested: "Fill three pyramids with bottom rows (i) $6$, $2$ (ii) $3$, $4$, $3$ (iii) $5$, $4$, $5$, $0$." Same grouping problem in **M2.S5.T5.C35** ("4, 13, 8 and 7, 11, 3 and 10, 14, 25"): suggested "(i) $4$, $13$, $8$ (ii) $7$, $11$, $3$ (iii) $10$, $14$, $25$."
- **M2.S5.T5.C27:** "middle row 4 and a blank, and bottom row 1 and two blanks" does not say the blank is to the right of the 4 / 1. Suggested: "the middle row has $4$ on the left and a blank on the right, the bottom row has $1$ on the left and two blanks".
- **M2.S5.T5.C33 question_tex:** "bottom row a, $b$, $c$" has the first letter outside math mode (reads as the article "a"). Suggested: "bottom row $a$, $b$, $c$".
- **M2.S5.T5.C30 steps_tex[3]:** "so $c$ is $20$, a is $32$ and $b$ is $28$": "a" is outside math mode. Suggested: "$a$ is $32$".
- **M2.S5.T5.C32 (extra block, answer_tex):** "First: bottom 5, 14, 7, 2 and top 70. Second: bottom 3, 5, 5, 2 with rows 8, 10, 7 and 18, 17" labels the book's second and third pyramids "First" and "Second", while its own steps call them "Second pyramid" and "Third pyramid". Suggested: "Second pyramid: bottom $5$, $14$, $7$, $2$ and top $70$. Third pyramid: bottom $3$, $5$, $5$, $2$ with rows $8$, $10$, $7$ and $18$, $17$." The old plan also holds two solution cards for this concept (C32.IMG1, C32.IMG2); the new map gives one solution diagram, M2.S5.T5.C32.IMG1, so the builder must not reuse the old C32.IMG2.
- All other LP answers recomputed and agree with the mathematics (pyramid sums, 1390 - 165 = 1225, 1269 - 165 = 1104, 394 - 165 = 229, 296 - 165 = 131, 4 + 26 + 8 = 38, 7 + 22 + 3 = 32, 10 + 28 + 25 = 63, the Q4 values 9, 1 / 14, 2 / 5, 2). No solution contradicts the book.

## Book unclear or inconsistent

- The pdf has no printed solutions; every solution value comes from the LP and was recomputed.
- Page 4 uses "?" for unknown pyramid boxes, page 5 uses empty boxes (see Borderline 6).
- The step picture on page 4 colours found numbers blue (6, 3) and red (the last 3); the Q2 solution diagram uses ANSWER green for all new numbers, as the v3 style demands.
- The page-6 pyramid has wider bottom boxes than the earlier pyramids (it must hold a + 2b + c); in the Q5 solution figure both pyramids use the same wide boxes (2.4 x 1.3 units) so the letter and number pyramids match.
