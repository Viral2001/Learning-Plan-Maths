# Chunk A notes (Class 7 Ch 13, units 1 to 19, book pages 1 to 14)

Result: 32 items, required 6 / optional 2 / none 24. Validator: errors 0, warnings 0.
Required: C29 worked example (onion dot plot), C40 + C41 (Bookworm question + solution), C42 + C43 (Newspaper question + solution), C45 worked example (two "How long is a minute?" dot plots).

## 1. Judgement calls

- **C29 worked example (M2.S8.T8.C29.IMG2) and C45 worked example (M2.S11.T11.C45.IMG2): required, but they duplicate the kept teaching images of the same concepts** (C29.IMG1 = same onion dot plot; C45.IMG1 = same two minute-estimate dot plots). v3 says a teaching image is never linked and never stands in for a figure the item needs, so each block gets its own diagram. If the team finds two copies of one picture in one concept unwanted, these two are the ones to drop. Reasons: C29's task is "draw the dot plot" (answer is a figure) and every step points at it; C45's 61 estimates exist only in the book's two plots and the steps count them (20 of 33, 19 of 28).
- **C28 worked example (onions, five measures): none (LATEX_TABLE) with needs_lp_text_sync.** The data are the book's two 12-row price tables; the LP question text does not list the prices at all, so the table must be written into the text. Not drawn as a picture (plain numbers).
- **C40 / C42 (Bookworm, Newspaper) question: required.** The book gives an empty dot plot and the task "Mark the data, the mean, and the median on the dot plot below" (ACTION_ON_FIGURE). The LP question text drops that instruction; I set needs_lp_text_sync and gave the sentence in text_alternative. The question figure is the EMPTY frame only (what the book gives); the fifteen paper slips are left out because the values are in the text. Solutions C41 / C43 are the filled plot, derived_from the question frame (sibling decisions kept identical).
- **C41 solution shows the full-data mean and median only** (15 dots, mean about 8.13, median 6). The "without 40" recalculation (mean 5.86, median 5.5) is not drawn: the book only asks to mark data, mean and median, and the outlier tag is left out. Say if you want the outlier ring or the second pair of lines added.
- **Newspaper frame (C42/C43) runs to 30 with no label at 30**, copying the book: the value 26 needs the interval past the last label 25. The LP's q_figure says "0 to 25", which cannot hold 26. I did not add a "30" label (not in the book); add one if the team prefers.
- **Optional, not added:** C37 solution (book's P10 dot plots with mean and median lines on each family) and C48 solution (whole-class dot plot with the mean line at 144.5 and the 15 taller dots marked). Both answers are complete in text; the figure only helps.
- **C14/C15 guavas:** none on both sides. The book's levelled-guava picture illustrates the working; the kept teaching image C11 already levels Shreyas's group. Parag's group (P04-pictograph-2) is in no teaching image, so it is mapped none:TEXT_SUFFICIENT.
- **P10 plots:** P10-dot_plot-1/2 mapped to the teaching image M2.S9.T9.C32.IMG1 (two families' dot plots). P10-3/4 (same plots with median lines) are not in that image's description; mapped none:TEXT_SUFFICIENT because they are the figure named in the optional C37 solution.
- **Colours in the dot plots:** book uses green/purple (onions) and blue/orange; the diagrams use SET_A / SET_B plus circle / diamond for the onion plot, so colour is not the only cue.
- **Group names in C45:** LP says "first group / second group", book says Group A / Group B; the diagram follows the LP. The second mean is drawn 59.29 (LP; 1660 / 28 = 59.2857), the book prints 59.28.
- **Inventory extras:** NEW-P11-dot_plot-1-sol and NEW-P12-dot_plot-1-sol account for the completed plots (answer figures not printed in the book; the pdf has no solutions section). NEW-P01-statement-bubbles = page-1 speech bubbles (plain sentences). Pure illustrations (boy with bat, hibiscus girl, tossed newspapers, stopwatch, family picture, character portraits) were not inventoried (decoration).

## 2. Things in the LP that look wrong

- **M1.S6.T6.C17 (hibiscus solution), step 5:** "9 gives 4 to 2 to make 5 and 6; 7 gives 2 to 3 and 4 gives 1 to 6, so all are at 5". After the first two moves the values are 6, 5, 5, 4, 5, so it must read "6 gives 1 to 4". As written, "4 gives 1 to 6" gives 3 and 7. (Appears in steps, steps_tex and text.)
- **M2.S10.T10.C43/C41 etc. numbers are right** (all re-computed: totals 122 and 128, means 8.13 and 18.29, medians 6 and 18, heights 986 / 801, 683, 2430 / 1616 / 4046, onion totals 458 / 450, estimate sums 1921 / 1660).
- **M2.S10.T10.C41 step 7:** "the mean fell by about 2.27": exactly 122/15 - 82/14 = 2.276, so "about 2.28"; 2.27 comes from the rounded 8.13 - 5.86. Minor.
- **M2.S12.T12.C47 (class heights):** the question says "the heights in the table" but the LP question text carries no heights (only q_figure does). The table must be written into the text.
- **M2.S8.T8.C28:** question text has no monthly prices (see above); the steps' "6 months / 5 months / 1 equal" is correct (Y: Jan, Feb, Mar, Aug, Nov, Dec; W: Apr, May, Jul, Sep, Oct; equal Jun).
- **M1.S4.T4.C9:** question says Yashasvi "did not play one match" without saying which; the book table shows Match 4. Not needed for the mean.
- **M2.S10.T10.C40 / C42 question texts** do not say that the data, mean and median are to be marked on the dot plot (the book does); the figure would then arrive with no instruction.

## 3. Places where the book itself is unclear or wrong

- p.3: "Average number of runs scored by Shubman in a match = 110 / 5 = 21 runs" is wrong: 110 / 5 = 22. The LP uses 22 (C9 steps, concept image).
- p.13: whole-class mean printed 144.4; 4046 / 28 = 144.5 exactly (the LP uses 144.5). Girls' mean printed 146.9 (146.909); boys 142.94.
- p.14: Group B mean printed 59.28 (truncated 59.2857).
- p.12: the empty newspaper dot plot is labelled only to 25 but its grid runs to 30, and one value (26) lies beyond the last label.
- p.7: the callout boxes name the dots (two 39s, the 19, two 42s) but the figure has no axis title; the LP/concept image adds "Price of onions (in rupees per kg)", which the new diagram also carries.
- No printed-solutions section in this pdf: every solution figure here is drawn from the LP solution, not copied from a printed answer.
