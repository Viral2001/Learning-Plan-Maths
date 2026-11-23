# Chunk A notes (Class 8 Ch 8 "Fractions in Disguise", LP cbse_eng_maths8_ch8_v56)

Units: 24 (topics M1.S1.T1, M1.S2.T2, M1.S3.T3, M1.S4.T4, M2.S5.T5) = 32 items.
Result: required 5 (3 question, 2 solution), optional 0, none 27. Validator: errors 0, 2 warnings (the two solution
diagrams C11 and C21 have no printed book picture to map; the pdf has no solutions section, so that is expected).

Diagrams made:
- M1.S3.T3.C8.IMG1 (question, Example 1): the book's page-2 bar model, 4 parts, red for 3, yellow for 1, with the 0 to 4/4 and 0 to 100/100 (25%..100%) scales.
- M1.S3.T3.C10.IMG1 (question) and M1.S3.T3.C11.IMG1 (solution, derived from it): Example 2 Method 3 bar, four empty boxes / the same four boxes filled 20%, 40%, 60%, 80%.
- M1.S4.T4.C20.IMG1 (question) and M1.S4.T4.C21.IMG1 (solution, derived from it): Figure it Out Q4 race line, runners A to D and six option boxes / the four matched boxes outlined and tagged A, B, C, D.

## 1. Judgement calls

- **C8 question = required.** The LP question is only "Yellow paint?". The data (red is 3/4 of the mixture) sits only in the book's bar model, and the book question ("Can you tell what percentage of the colour was made using yellow?") points at that picture. Codes FIG_REFERENCED + DATA_IN_FIGURE. The same picture is the teaching image of M1.S2.T2.C4 (M1.S2.T2.C4.IMG1), but v3 never links a teaching image, so it is drawn again. The 'refer picture' exception does not apply (the book answers the question, it does not just say "refer picture").
- **Colours in the C8 picture.** Red and yellow are paint colours and carry the meaning (no word labels in the book picture), so the spec gives hex values: red #D55E00 (palette vermillion), yellow #F0E442 (palette yellow). They are not style tokens; this is stated in the spec's `render_note`.
- **C10 question = required, C11 solution = required.** ACTION_ON_FIGURE: the student fills four empty boxes; the answer is the filled boxes (ANSWER_IS_FIGURE). The yellow hint speech bubble of the book ("Isn't it the same as finding 2/5 th of 100?") is a hint sentence, so it is not in the diagram. The book's red outline of the whole band is drawn as an INK outline (red carries no meaning there).
- **C20 question = required, C21 solution = required.** The positions of the four runners live only in the picture (DATA_IN_FIGURE). The task is "Match", and the LP answer is a pairing (A 38%, B 55%, C 72%, D 93%), which I treated as a figure answer (B2: answer is an arrangement, even if the steps describe it in words). The solution marks the matched boxes in ANSWER green and tags them with the runner letter; no connector lines (they would cross: A goes to the 3rd box, B to the 1st). The unused options 20% and 84% are left exactly as given (not restyled).
- **Runner positions (C20).** The book gives no numbers. I measured the circle centres on the page picture by pixels: 0.3175, 0.5323, 0.7531, 0.9454 of the Start-to-Finish line; the specs use 0.32, 0.53, 0.75, 0.95 (x = 240 + 1440 x fraction). Nearest-option check: A 32% -> 38% (20% is further), B 53% -> 55%, C 75% -> 72% (84% is further), D 95% -> 93%. This agrees with the LP answer.
- **Plain tables = LaTeX.** The free-hand table (book p.7, P07-table-1) has plain blue cells with no colour meaning, so C25 ("Anything interesting in the table?") and both C26 blocks are none / LATEX_TABLE with a `text_alternative` naming the LaTeX array (header 100, 200, 50, 80, 10, 35, 287; rows 25%, 10%, 20%, 5% (and 40%, 15% for C26)).
- **Figures not claimed.** Section 1.2 pictures P06, P08, P09, P10, P11, P12 and P15, P16 belong to units of the other chunks (Examples 1 to 6 and their Q/A pairs). I claimed only P07-table-1 from 1.2, because my C25/C26 units work on that table. If the merge shows another chunk mapping P07-table-1 differently, it becomes a separate NEW- use; both meanings are the same (a table, LaTeX) so that is harmless.
- **Page 5 cards.** P05-infographic-1 (boy, 60% water) = DECORATIVE_ONLY; P05-infographic-2 (Sun and planets) = TEXT_SUFFICIENT. No unit of this chunk asks anything about them (teaching fact cards, numbers in the caption).
- **Callout boxes not inventoried.** The orange equation boxes (p.1 "3/4 = 6/8 = 30/40 = 75/100", p.4 "9/34 = 26.47 percent ... per mille", p.7 "y/100 x 80") are formulas, not figures, so they are not in the base inventory and I did not add NEW- entries for them.

## 2. Borderline

- **M1.S3.T3.C9 (Example 1 solution) = none (SAME_AS_QUESTION_DIAGRAM + TEXT_SUFFICIENT).** One could argue for a solution figure that brackets the yellow quarter as 25%. The book picture already shows the yellow last quarter against the 25/50/75/100 scale, the answer is a number, and v3 Step E says "figure-based question, numeric answer: Q required, S none". If the reviewer wants it, the spec would be C8.IMG1 plus a bracket under the yellow part labelled 25% in ANSWER, derived_from M1.S3.T3.C8.IMG1.
- **M1.S4.T4.C21 (Q4 solution) = required.** The LP answer text carries every number, so a reviewer could call it none. I kept it required because the answer is a matching drawn on a given picture (ANSWER_IS_FIGURE) and the user's rule is not to flip a required item only because the LP text has the numbers.
- **M1.S1.T1.C1 block 3 (ratio 2 : 3)** is none. A bar of 5 parts would help, but the whole 2 + 3 = 5 is one line of words and the book gives no figure.
- **Diagnostics (C4, C24, C31, "Check my thinking")** are all none (text multiple choice, no book figure).

## 3. LP text issues (not edited, listed only)

- **M1.S3.T3.C8 / C9 (Example 1).** The question text is just "Yellow paint?" and lacks the data. Suggested: "Surya mixes red paint and yellow paint. The red paint makes up 3/4 of the mixture, which is 75%. What percentage of the colour is made with yellow?" (the diagram carries the bar). The solution step "100% - 75%" presupposes the 75%.
- **M1.S3.T3.C10 / C11 (Example 2).** The question text is just "Method 3 boxes" and lacks the task. Suggested: "Surya saves 2/5 of his prize money for a canvas. Fill the four empty boxes with the percentages that go under 1/5, 2/5, 3/5 and 4/5 of the bar."
- **M1.S3.T3.C12 / C13 (Example 3).** The question text "Which variety is more sugary?" lacks the data. Suggested: "Sugar makes up 9/34 of Variety 1 and 13/45 of Variety 2 of a biscuit. Which variety is more sugary?" Also: the book prints 28.88% for Variety 2; 13/45 = 28.888...% which rounds to 28.89%, so the LP's "about 28.89%" is right and the book's value is a cut-off (no diagram is affected).
- **M1.S4.T4.C20 / C21 (FiO Q4).** The question text ends with a bracket that describes the picture: "(Line from Start to Finish with runners A, B, C, D; options 55%, 20%, ...)". With the diagram placed after the question this is a duplicate description; suggest removing it (or keeping only the six options if the build wants them in text).
- **M1.S4.T4.C17 (FiO Q2 solution).** Step 2 reads "Used as the diagnostic above; if already used there, ask for the reason only." That is an instruction to the AI, not a student sentence. Suggest deleting the step.
- **M1.S4.T4.C23 (FiO Q5 solution).** The only step compares 3/11 with 3/10 = 30%, which is correct but never reaches the asked comparison with 61%. Suggested addition: "So 3/11 is less than 30%, which is less than 61%."
- **M2.S5.T5.C25 ("Anything interesting in the table?").** The table itself is not in the text, so the student cannot see what to look at. Suggested: add the completed LaTeX table (rows 25%, 10%, 20%, 5% for 100, 200, 50, 80, 10, 35, 287, values as in the C26 answer) before the question, or write "In the table you just filled in, is there anything interesting?" and place the LaTeX table.
- **M2.S5.T5.C26 blocks 0 and 1.** The two blocks have the identical question, steps and answer text (only example_id differs: free_hand_40 and free_hand_15). Also the question gives the row and column labels in words only. Suggested: keep one block with the LaTeX table, or make block 1 only the 15% row.
- **M2.S5.T5.C27.** Step 1 says "Say a recipe from I2 before computing." "I2" is an internal image code, meaningless to the student. Suggested: "Say a recipe from the building-block picture (50%, 25%, 10%, 5%) before computing."
- **Diagnostic blocks (M1.S2.T2.C4, M2.S5.T5.C24, M2.S5.T5.C31).** The text holds the internal sentence "Act on the diagnosis table." and the answer ("Answer: (b), reason (i)") inside the same text as the question; check that the build shows these only to the AI.
- **M1.S1.T1.C1.** Block 0 of the concept (not a unit) mentions "a bar picture" in the recap; the five worked examples themselves are text and have no picture.

## 4. Book unclear / checked

- All six inventory entries of this chunk were checked against the page pictures (pp. 2, 3, 4, 5, 7); the base descriptions are right. P04's "unclear" (runner positions by eye) is settled by pixel measurement (see above).
- The book's Method 3 figure (p.3) shows the speech bubble under the second box; it is a hint, not part of the data.
- The book has no solutions section in this pdf, so there are no printed-answer pictures; the two solution figures are drawn from the LP solution text.
- Arithmetic re-checked in the LP texts of this chunk: 3/5 = 60%, 7/14 = 50%, 9/20 = 45%, 72/150 = 48%, 1/3 = 33 1/3%, 5/11 = 45.45%; 15/25 = 60%; 15/80 = 18.75%; Q5 (i) to (iv) results; the 7 x 6 mental table values (25%, 10%, 20%, 5%, 40%, 15% of 100, 200, 50, 80, 10, 35, 287); 60% of 30 = 18 and 40% of 50 = 20; 25% of the sum = 60 so the sum is 240. All correct.
