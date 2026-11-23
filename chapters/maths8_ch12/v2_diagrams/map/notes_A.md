# Notes, chunk A (topics M1.S2.T2 to M1.S7.T7), Class 8 Ch 12 "Tales by Dots and Lines"

Result: 29 items from 17 units. Required 5 (Q2 question + solution, Q4 question, More Q1 solution, More Q7 question), optional 2 (Q4 solution, More Q7 solution), none 22. Validator `--chunk A`: errors 0, warnings 0.

Required diagrams and media ids:
- M1.S4.T4.C15.IMG1 (Figure it Out Q2, the dot plot with the missing dot) and M1.S4.T4.C15.IMG2 (the same plot with the dot at 16, derived_from IMG1)
- M1.S4.T4.C17.IMG1 (Figure it Out Q4, the three album dot plots A, B, C)
- M1.S4.T4.C18.IMG1 (More Q1 solution, two filled 3 by 3 grids with the line totals 30; the question has no figure)
- M1.S4.T4.C20.IMG1 (More Q7, the dot plot of 25 values)

## 1. Judgement calls

- **Worked examples C2, C3, C4, C5 (T2) and C21 (T5): all `none` (TEXT_SUFFICIENT).** Every number is in the LP steps, and each concept already keeps its own teaching picture (C2.IMG1, C3.IMG1, C4.IMG1, C5.IMG1, C21.IMG1) that shows the same dot plot. In the book these pictures are teaching figures ("illustrated below"), not figures attached to a boxed worked example; the LP turned the prose into worked examples. A drawn copy would duplicate the kept concept image. Listed under Borderline.
- **Q2 (C15) question required, solution required.** The book gives the dot plot with the mean line at 9 and asks to mark the missing dot, so the plot is needed to attempt it (ACTION_ON_FIGURE) and the answer is a drawn dot (ANSWER_IS_FIGURE). The solution adds only the dot at 16 in ANSWER green; the distance check (5 + 2 + 1 + 1 = 9 and 2 + 7 = 9) stays in the LP steps.
- **Q4 (C17) question required.** The LP question gives no song lengths for albums B and C; they exist only in the book's picture. All three plots are drawn on the same 0 to 7.5 axis. I positioned the quarter values (5.25, 5.75, 0.75, 3.75, 4.25) by zooming into the page: they sit halfway between the half-unit grid lines, and plot A adds to 39, so the mean 5.57 confirms it. Letters A, B, C are drawn because the LP answer says "Album A" (decision 3). The book's small empty answer boxes beside the letters are not drawn.
- **Q4 and More Q7 solutions `optional`, not added.** Both answers are numbers worked out in text (39 / 7 = 5.57; 443 / 25 = 17.72). A mean line on the plot would help, but it would add numbers the LP does not state (means of B and C are not in the LP; the 17.72 line is in the LP, but the answer is not a picture). Sibling consistency: the two dot-plot questions with a numeric answer get the same decision.
- **More Q7 (C20) question required, drawn as dots.** The LP question lists the counts, but the book question points at "the data shown in the dot plot below" (decision 4: not flipped to none because the LP carries the numbers). The book prints blue x marks and no grid; I specified dots (the LP says "dots") and no grid, and say so in `render_note`.
- **More Q1 (C18) question `none`, solution required.** The book's picture is an empty 3 by 3 grid with no number; the LP question already says "a 3 by 3 grid". A blank grid carries nothing and the companion note says a blank image is worse than none. The solution's answer is itself a filled grid, so it is required (ANSWER_IS_FIGURE) and stands alone (derived_from null). It shows both grids of the LP steps: (i) 7, 12, 11 / 14, 10, 6 / 9, 8, 13 and (ii) the same grid reflected in its main diagonal (7, 14, 9 / 12, 10, 8 / 11, 6, 13), with the six changed cells shaded MARK_FILL and the 16 line totals of 30. Labels (i) and (ii) are shown because the LP steps refer to part (ii). Every row, column and diagonal sum was recomputed for both grids (all 30; the nine numbers of (i) are distinct; six cells differ).
- **Kushti example (C25/C26): `none`.** The book's picture (P07-notebook_list-1) is a handwritten list of nine numbers with a smudge and a circled "Avg 39.2"; the LP question lists all nine weights and the mean, so the list goes in text (NUMBER_LIST_IN_BOXES). Coconut example (C27/C28): the only picture is three palm trees (decoration).
- **T3 pairs (C9 to C14), T4 C16 and C19, T7 pair: all `none`.** Arithmetic, algebra or word questions; the book prints no figure, except C9 where the book's two hint dot plots are covered by concept image C6.IMG1.
- **Figures of book pages 1 to 7 are claimed in this chunk.** Topic T1 has no unit in any chunk, but T2's first paragraph (C2 block 0) carries the prompts of pages 1 to 3, so I claimed all 26 base figures of pages 1 to 7. The "Calculate and mark the mean" and "Mark the mean" plots (P01-dot_plot-2..5, P02-dot_plot-1..4) and the explore plot (P04-dot_plot-1) are `none:OPEN_ENDED` because the LP has no item for them. One extra entry, `NEW-P11-dot_plot-2-sol`, accounts for the Q2 solution figure (not printed: this pdf has no solutions section).
- **Concept-image accounting** (no link): P01-1 to C1.IMG1; P02-7 to C2.IMG1; P02-8 to C3.IMG1; P03-3 to C4.IMG1; P04-3, P04-4, P05-1 to C6.IMG1; P06-2 to C21.IMG1.
- **T9 note for the merge:** the teaching topic M1.S9.T9 (frequencies, book p.8) has no unit either, and is in none of the three chunk lists in meta.json. Its figures (P08-table-1, P08-dot_plot-2, P08-table-3 and maybe P09-table-1) are not claimed here; whoever merges should check they are claimed by chunk B.

## 2. LP text issues

- **M1.S3.T3.C9 / C10 (Relatively Unchanged).** The question asks for the mean, the mean after adding 10 and the mean after doubling, but the solution also works "every value minus 1" and the answer says "6.18 after subtracting 1". Suggested question sentence: "...then the mean when every value is increased by 10, when every value is decreased by 1, and when every value is doubled." (The book's own "reduce every value by 1" plot is applied to the +10 data, mean 16.18; the LP applies it to the original data, 6.18. Both are correct.)
- **M1.S3.T3.C11 / C12.** Subscripts are missing in LaTeX: `$x1$, $x2$, … $xn$` should be `$x_1$, $x_2$, \ldots, $x_n$`, and in the question `mean is a` should be `mean is $a$`.
- **M1.S4.T4.C16 (Q3, shoes).** The answer says "option (d)" but the question text does not list the options (a) to (g) of the book. Suggested addition to the question: "(a) 174.2 cm (b) 126.2 cm (c) 150.2 cm (d) 149.2 cm (e) 151.2 cm (f) None of the above (g) Insufficient information".
- **M1.S4.T4.C17 (Q4, albums).** The question text gives no data for albums B and C (they are only in the picture), so it depends on the figure; the plan's video metadata also has `final_answer.spoken` = "album eigh" (should be "album A").
- **M1.S4.T4.C15 to C20 (the six Figure it Out singles): wrong `book_number`.** All six carry "Figure it Out, Q1"; the correct numbers are Q2, Q3, Q4 (chapter-end part 5.1) and Q1, Q5, Q7 (the second Figure it Out, "More on Mean and Median"). The concept names ("Mean and Median, Q2", "More on Mean and Median, Q1", ...) are right.
- **M1.S5.T5.C21 (worked example, median).** The question gives only "a data set has median 8", not the data. The book's data is 4, 7, 8, 12, 14 (median 8); including 11 gives 4, 7, 8, 11, 12, 14. Suggested sentence: "The data 4, 7, 8, 12, 14 has median 8. Include the value 11 and find the new median."
- **M1.S2.T2.C2 block 0.** The paragraph says "Calculate and mark the mean of each collection of data below" and "Mark the mean for the collections below", but none of the eight collections (book p.1 and p.2) is given in the LP text, so the sentence points at nothing. Suggested: either list the data (6, 7, 8 / 3, 6, 9 / 2, 4, 9 / 4, 11, 15 / 11, 13, 17, 19 / 5, 6, 15, 16 / 10, 10, 11, 17 / 3, 5, 10, 12) or drop the sentence.
- **M1.S2.T2.C2 (worked example).** The LP tries 13 and 11 as other centres; the book's picture uses 12.5 and 11. Both are mathematically right; the LP numbers are the ones the text uses.
- **Small LaTeX slips:** M1.S7.T7.C30 `$41s$` should read `$41$s` (or "the two $41$s"); M1.S3.T3.C13 question uses `(i):` with a colon.
- Arithmetic of every LP solution in this chunk was recomputed and is correct (349, 392, 43; 384, 381, 25.4; 61 / 5 = 12.2; 66 / 6 = 11; 79 / 11 = 7.18; 1275, 2500; 443 / 25 = 17.72; the grids; the median 41).

## 3. Where the book itself is unclear

- P02-dot_plot-8 (mean 7.5) uses the data 2, 6, 10, 12, while the unmarked "Mark the mean" plot above it (P02-dot_plot-4) uses 3, 5, 10, 12; both have mean 7.5. The base inventory already noted this.
- The book gives the quarter dot positions of Figure it Out Q4 only by position between grid lines; confirmed by the zoomed pictures and by the mean of plot A.
- Book print slips: none found in the figures of this chunk (the book axis of Q2 runs a little past 16, to about 17, which the spec follows).

## Borderline

- **Worked examples C2, C3, C4, C21 and C5 (none).** The book prints a dot plot that mirrors each example (P02-dot_plot-7, P02-dot_plot-8, P03-dot_plot-3, P06-dot_plot-2; for C5 the book uses other data), and a distance-arrow dot plot would be the natural picture. I chose `none` because the LP text carries every number and the kept concept image of the same concept shows the figure. If the user wants them, the specs would be: C2 dots 10, 10, 11, 17 with the mean line at 12 and arrows 2, 2, 1 | 5; C3 dots 2, 6, 10, 12 with the line at 7.5 and arrows 5.5, 1.5 | 2.5, 4.5; C4 the before and after plots of 5, 5, 10, 24 with 17 added (11 to 12.2); C21 dots 4, 7, 8, 12, 14 and the new 11 (median 8 to 9.5).
- **Q4 and More Q7 solutions (optional, not added).** See section 1.
- **More Q1 question (none).** Empty 3 by 3 grid in the book, no data in it (ACTION_ON_FIGURE could be argued for "fill the grid").
- **Kushti question C25 (none).** The book's notebook picture is referred to ("as shown") but the LP text carries every weight; a handwritten list of numbers is a plain list.
- **More Q7 question (required)** although the LP lists the counts, per decision 4.
