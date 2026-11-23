# Chunk B notes (Class 8 Ch 2 "Power Play", plan cbse_eng_maths8_ch2_v35)

Units: topics M3.S11.T11, M3.S13.T13, M3.S14.T14, M4.S15.T15, M4.S16.T16, M4.S17.T17, M4.S18.T18 = 18 units (14 pairs, 4 worked examples) = 32 items.
Result: required 0 / optional 1 / none 31. Validator: errors 0, warnings 0.

Why nothing is required: this chunk is exponent arithmetic (powers of 2, 5, 10, 26, 36, reciprocals, exponent rules). I looked at the page pictures of pdf pages 7, 8, 9, 10, 11, 26, 27 (questions) and 32, 35, 36, 37 (printed answers). The book gives none of these questions a figure of its own, and none of the printed answers is a picture. Every number a question needs is in the LP question text. The book pictures in these sections are teaching or decorative figures (pond girl, padlock photo, Estu's cap-and-dress arrows, the digit-mapping lines, the formula box, the "When Zero is in Power!" cartoon, banknote photographs).

Note for the brief: the brief says this pdf has no printed-solutions section, but pdf pages 30-38 do hold printed answers ("Page No. ... Ans:"). I read them for every item (all text, no pictures).

## Borderline

1. M3.S11.T11.C54 / C55 (Figure it Out Q7, "Circle the numbers that are the same"). Chosen: question `none` (NUMBER_LIST_IN_BOXES, TEXT_SUFFICIENT), solution `optional` (NUMBER_LIST_IN_BOXES, HIGHLIGHT_MEANING), not added. Why: the book prints five expressions in one plain row (no boxes, no colour) and the LP question text already lists all five; v3 "Not a diagram" says a board of numbers to choose from is listed in text, and for the solution side (arrows or circles on such a list) allows only `optional` when the LaTeX answer already gives the result. The printed answer on pdf page 36 is words ("2^4 x 3^6, 6^4 x 3^2 and 18^2 x 6^2 are same"), not a marked picture. If the user wants a circled-row picture anyway, it would be a `cell_row`-style card: five expressions in one row, the first, second and fourth circled in FOCUS, nothing else. Not specified in full because it is not added.
2. M3.S13.T13.C60 / C61 (Estu's and Roxie's outfits). Chosen: both sides `none` (TEXT_SUFFICIENT / LATEX_ARITHMETIC). The book hint says "Try drawing a diagram like the one above" and the book does draw Estu's tree (a teaching figure, mapped to concept image C56), but the question gives no figure and the printed answer is only "7 x 2 x 3 ways". A choice tree for Roxie (7 dresses x 2 hats x 3 shoes) would be nicer but is not needed to solve it exactly as well from the text.
3. M4.S15.T15.C70 (halving a line of 16 units, worked example) and M4.S17.T17.C78 (halving past 1). Chosen: `none`. A picture of the line halved would be a nice visual, but the book draws no line here (it is "imagine a line of length 16 units"), the numbers are all in the text, and the plan already carries a teaching image for each idea (C70.IMG1, C78.IMG1) that stays and is not linked.
4. M3.S13.T13.C62 and C64 (password locks). The book's digit-mapping picture (lines from digit 0 to all ten digits) is a teaching figure and was mapped to the nearest plan teaching image (C57 "Five slots, ten choices each"): the idea is the same (10 choices per slot) but it is not the same drawing. If the merge wants an exact match, change the mapping to `none:TEXT_SUFFICIENT`; nothing else changes.
5. P11-table-2 (the green box of three general rules on pdf page 11): claimed by this chunk as `none:TEXT_SUFFICIENT` because it sits in the 2.3 section of C79, C83 and C85. If chunk C (Power Lines, same page) also claims it, the meaning should stay "formulas only, no figure needed".

## Figures

- P08-arrangement-1 -> concept_image:M3.S12.T12.C56.IMG1 (Estu's caps and dresses arrows; description checked against page_08.png, correct).
- P09-mapping_diagram-1 -> concept_image:M3.S12.T12.C57.IMG1 (checked against page_09.png, correct).
- P11-table-2 -> none:TEXT_SUFFICIENT (checked against page_11.png, correct).
- P27-number_row-1 -> none:NUMBER_LIST_IN_BOXES (checked against page_27.png, correct).
- NEW-P10-zero-cartoon -> none:DECORATIVE_ONLY (found by me: the six-panel cartoon "When Zero is in Power!" on page_10.png; missing from the base inventory).
- Not listed, as pure decoration per Step 0: the girl by the lotus pond (page 7), the padlock photograph and the worried-girl speech bubble (page 9), the owl tip box (page 8), the two banknote photographs at the top of page 26 (sit above Figure it Out, shared with other chunks' questions).
- Not claimed by this chunk (they belong to other chunks' sections): P11-number_line-1 (power line of 4), P12-number_line-1, P33-power_line-1, P33-number_line-1, P34-number_line-1 and the P06 / P05 figures.

## LP text issues

No arithmetic mistake found: I recomputed every number in the 18 units (2^30 and 2^29; 16 x 81 = 1296; 10000 / 625 = 16; 11664 for all three equal expressions; 14 x 3 = 42; 26^6 = 308915776; 36^5 = 60466176; 10^9 < 8,500,000,000 < 10^10; 2^160 ends in 6; every simplification in C86 and C88). The points below are wording only; nothing was changed.

- M3.S11.T11.C54 (question): "Circle the numbers that are the same" cannot be done on a text-only page. Suggested sentence: "Which of these numbers are the same? 2^4 x 3^6, 6^4 x 3^2, 6^10, 18^2 x 6^2, 6^24. Write them down." (The answer text already names the three, so only the question needs it.)
- M4.S18.T18.C88 (solution step (iv)): "$-2 \times -3 = 6$" puts two minus signs side by side. Suggested: "$(-2) \times (-3) = 6$, so $13^{6}$."
- M4.S18.T18.C85 / C86 and C87 / C88: the question lists parts (i) to (v) (C87) or separates them with semicolons (C85) while the solution steps for C85 / C86 carry no part letters. Suggested for C86: start each step with its part letter, "(i): Add exponents ...", as C88 already does.
- M3.S13.T13.C60 (question): the book's hint "Try drawing a diagram like the one above" is missing from the LP question text; it is not needed for the answer, but if a choice tree is wanted later the question should say so.
- M3.S13.T13.C62 / C63: no missing data. The answer lists 100, 1000 and 100000 and the steps also give 4 digits (10000); fine.
- No missing data was found that only a figure could carry in any unit of this chunk.

## Places where the book itself is unclear or slipped

- pdf page 8 (book p.26): "You can list them all: 000, 001, 002, ....., 997, 997, 999." prints 997 twice; it should read 997, 998, 999. Print slip, in the teaching text for T12 (not an item of this chunk; no diagram is affected).
- pdf page 9 (book p.27): "Halving 16 cm three times may be written as ..." says cm while the lines before it say units. Not corrected anywhere (no diagram drawn).
- pdf page 27 (book p.45): Figure it Out Q12 labels its options "(ii) 20^9 (ii) 10^11 (iii) ..." with (ii) twice. Not an item of this chunk.
- The book's printed answer for the Figure it Out Q5 (iii) and (i) gives "9^-11 or 1/9^11" and "10^-7 or 1/10^7"; the LP (C88) gives only the negative-exponent form for (i) and (iii). Both forms are right.
