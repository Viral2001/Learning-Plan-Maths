# Chunk A notes (Class 7 Ch 1, plan cbse_eng_maths7_ch1_v30)

Result: 32 items. Required 3 (C6 question, C7 solution, C19 question), optional 1 (C20 solution, not added), none 28. Validator: errors 0, warnings 0.

## 1. Judgement calls

1. **Plain press-count tables are LaTeX, not images (C41/C42 Creative Chitti, C50/C51 Systematic Sippy).**
   The book tables (P06-table-1, P07-table-1) and the printed answer table (P26-table-1, printed answers page 3) are plain black or red grids of whole numbers: rows are the seven buttons, columns are the ways, blank means 0 presses. No colour carries meaning (the pink pills in the book are styling). Run rule: "plain tables of numbers stay text/LaTeX" (`LATEX_TABLE`). I did consider the B2 line "printed answer is a picture, solution required". I read it as meant for stick-figure line-ups and coloured tables, not a plain numeric table that a LaTeX array reproduces exactly. Each `none` item carries a `text_alternative` with the array to write. **If the user wants these as pictures, flip C42 (solution) and C51 (solution) first; C41/C50 questions already state the counts in the text.**
   The printed answer table has three columns (5/_/7/2, 4/10/7/2, 1/40/6/12), not the two ways printed in the question; the LP answer uses column 3 (4, 10, 7, 2).

2. **C6/C7 ladder (Climbing to One Lakh) is required on both sides.** The book question is "fill in the boxes given below" on a ladder with +1 arrows (`ACTION_ON_FIGURE`); the filled ladder is the answer (`ANSWER_IS_FIGURE`). The text alone would also work (tie-breaker), so this is the most borderline of the three required items; it follows the "complete a given figure" trigger.
   **The question diagram leaves the last box empty.** The book prints 1,00,000 in the last box already, but the LP question asks the learner to give "the smallest 6-digit number" (and the LP solution derives 1,00,000 as its last step). To avoid showing an answer the LP asks for, the question figure has only 999 filled. If the LP text is later changed to give 1,00,000, the last box should be filled in INK (render_note says so).
   The book caption "1,00,000 is read as One Lakh" is not drawn (captions are not allowed).

3. **C19 Somu: question required, solution optional.** The LP text says "The picture shows 10 floors" and the book data (10 floors, the 0 to 500 m scale with the statue and the waterfall) is only in the pictures, so the question side is required (`FIG_REFERENCED`, `DATA_IN_FIGURE`). The answers are numbers with the arithmetic in the steps (typical pair "figure-based question, numeric answer: Q required, S none/optional"), so the solution is `optional` (not added). The figure that would help is written in the reason: the scale with Somu's building as a 40 m bar and the gaps 140 m and 410 m marked in ANSWER green. **Alternative if the user prefers fewer images: C19 question `none` and remove "The picture shows 10 floors." from the LP question text.**
   Drawing decisions for the C19 figure: two panels. The left panel is a zoom of the building as 10 equal cells (so the floor count can be counted) with one floor bracketed "4 m" (given in the question). The right panel is the 0 to 500 m scale with a bar for the Statue of Unity (180 m) and one for the Kunchikal waterfall (450 m), both numbers from the LP. The building's own height (40 m) is the answer, so it is not labelled or drawn as a bar in the question figure. Somu himself is not drawn: at the zoomed scale he would be 17 px tall, and his height (1 m) is in the text. The book's cartoon statue and waterfall are not reproduced (plain bars with names).

4. **C8/C9 (days in 100 years) and all Figure it Out 1.1/1.2 questions: none.** Numbers are in the text, arithmetic is in the steps. For C9 a number line comparing 36,500 / 73,000 / 1,09,500 with 1,00,000 would be nice but is not needed (marked `none`, not `optional`, because the steps state every gap).

5. **Land of Tens Q1-Q3 (C32, C34, C36), Chitti Q2 (C43), Sippy mascots.** The calculator pictures are mascots with one labelled button; the labels are already in the text (`DECORATIVE_ONLY`). Question side `none`, all three alike (sibling consistency).

6. **Figures claimed beyond the units' own items.** `P06-calculator-1` (Creative Chitti mascot, intro of Land of Tens Q4) and `P07-calculator-1` (Sippy mascot) sit in the 1.2 text between my units (topics T11 and T14); no other chunk has a unit there, so I claimed them as `none:DECORATIVE_ONLY` (another chunk that claims them should give the same meaning). `P02-pattern-2` (zigzag chain) is claimed as `none:LATEX_ARITHMETIC`.
   Two extra inventory entries use the NEW- scheme because one book figure serves two uses: `NEW-P02-pattern-1-sol` (the filled ladder, solution use of P02-pattern-1) and `NEW-P03-building-1-teaching` (accounting for the teaching image `M1.S5.T5.C16.IMG1`).

7. **Base descriptions checked against the page pictures.** I checked every base entry of my chunk against pages 2, 3, 5, 6, 7 and 26. All are correct as written (10 boxes and 9 arrows in the zigzag; 10 balcony floors with Somu on the top balcony; lines at the 200 and 500 labels with a pink strip near 60; calculators with the listed buttons; table cell values). No entry needed "CORRECTED:".

8. **Optional count.** Only C20 is optional. The answer-side `none` items whose figure "would be nice" are not marked optional, per "prefer none".

## 2. Things in the LP that look wrong or odd

- **C6 question text vs the book:** the book prints 1,00,000 as given in the last box; the LP asks the learner to give it (see above). Pick one: either drop "and the smallest 6-digit number" from the LP text, or keep it as is (current choice).
- **The zigzag chain of the book page 2** (boxes 99,995, 99,996, blank, 99,998, then six more blanks; the sequence runs 99,995 ... 1,00,004) belongs to the same "fill in the boxes" instruction but is **not in the LP at all** (no question or solution mentions 99,997 / 99,999 / 1,00,001 ... 1,00,004). The content team may want a question for it; if added, it is a plain sequence (LaTeX).
- **C19/C20 question text** says "The picture shows 10 floors" and "Statue of Unity (180 m)", "waterfall (450 m)". The book picture draws the statue's reference line at the 200 label and the waterfall at 500, and its pink strip for Somu's building near 60 m (not 40 m). The LP numbers (180, 450, 40) are consistent with the book text and printed answers (40 m, 140 m, 410 m, about 113 floors), so I used them.
- **LP hint `q_figure` for C19** says Somu stands "at its door"; the book picture has him on the top balcony. Hints were not used for the drawing.
- **C20 step 5** ("The statue is 180 / 40 = 4.5 times the building") is not in the printed answers (the book text says "close to 4 times"). Not wrong, only an addition.
- **Book printed answer for Figure it Out 1.2 Q1 (e) is wrong:** its second way "(36 x 10000) + (78 x 1000) + (13 x 1)" equals 4,38,013, not 3,67,813. The LP's second way for (e), (36 x 10000) + (7 x 1000) + (8 x 100) + (1 x 10) + (3 x 1) = 3,67,813, is correct and is the one to keep.
- **C37 step 9** begins "(i):" without math mode (the other steps use `$(a)$:`). Cosmetic. The LP text for C36's question also writes `(i)` outside math mode.
- **C44 step 4** reads "digit sum must be 30 - 9 = 21 or 30 - 18 = 12 or 3"; the last item should read "30 - 27 = 3". The results (largest 993, smallest 102) are right and match the printed answers; I re-derived both (digit sums 21 and 3, each trade adds 9 presses).
- **Systematic Sippy table (book p.7)** has a +10,00,000 row although Sippy's calculator has only six buttons up to +1,00,000 (and the text lists no +10,00,000). The LP question already ignores that row.

## 3. Places where the book itself is unclear

- The scale picture on p.3 (lines at 200 and 500 vs text 180 and 450; pink strip near 60 m for a 40 m building; statue "close to 4 times the height of Somu's building" while 180 / 40 = 4.5).
- Whether the plain base of the building (the door strip under the tenth balcony) counts as an eleventh floor. The text and answers (10 floors, 40 m) say ten.
- The printed answer table for the "different way to get 5072" shows three ways while the question's own table showed two; the printed headers of the extra columns are blank.
- The book's answer to the zigzag chain is not printed at all.
