# Class 7 Ch 13 Connecting the Dots... - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths7_ch13` v33 (taken from staging). Result: new V2 version v34 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (101 items from 58 units)
{"worked_example": {"none": 9, "required": 4, "optional": 2}, "question": {"none": 30, "required": 13}, "solution": {"none": 24, "optional": 6, "required": 13}}

Optional, NOT added: [('C37', 'solution'), ('C48', 'solution'), ('C76', 'worked_example'), ('C98', 'worked_example'), ('C112', 'solution'), ('C122', 'solution'), ('C124', 'solution'), ('C126', 'solution')]

needs_lp_text_sync: [('C40', 'question'), ('C42', 'question'), ('C63', 'question'), ('C73', 'question')]

## The 30 diagrams
| id | side | type |
|---|---|---|
| M2.S8.T8.C29.IMG2 | worked example | data_graph |
| M2.S10.T10.C40.IMG1 | question | data_graph |
| M2.S10.T10.C41.IMG1 | solution | data_graph |
| M2.S10.T10.C42.IMG1 | question | data_graph |
| M2.S10.T10.C43.IMG1 | solution | data_graph |
| M2.S11.T11.C45.IMG2 | worked example | data_graph |
| M2.S14.T14.C57.IMG1 | question | data_graph |
| M2.S14.T14.C58.IMG1 | solution | data_graph |
| M2.S14.T14.C61.IMG1 | question | data_graph |
| M2.S14.T14.C62.IMG1 | solution | data_graph |
| M2.S14.T14.C63.IMG1 | question | data_graph |
| M3.S15.T15.C67.IMG2 | worked example | data_graph |
| M3.S16.T16.C71.IMG1 | question | data_graph |
| M3.S16.T16.C73.IMG1 | question | data_graph |
| M3.S19.T19.C80.IMG1 | question | data_graph |
| M3.S19.T19.C81.IMG1 | solution | data_graph |
| M3.S20.T20.C82.IMG1 | question | data_graph |
| M3.S20.T20.C85.IMG1 | solution | data_graph |
| M3.S20.T20.C87.IMG1 | solution | data_graph |
| M3.S20.T20.C88.IMG1 | question | data_graph |
| M3.S20.T20.C89.IMG1 | solution | data_graph |
| M4.S21.T21.C90.IMG2 | worked example | data_graph |
| M4.S24.T24.C101.IMG1 | question | data_graph |
| M4.S24.T24.C108.IMG1 | solution | data_graph |
| M4.S24.T24.C115.IMG1 | question | data_graph |
| M4.S24.T24.C116.IMG1 | solution | data_graph |
| M4.S24.T24.C118.IMG1 | solution | data_graph |
| M4.S24.T24.C119.IMG1 | question | data_graph |
| M4.S24.T24.C120.IMG1 | solution | data_graph |
| M5.S26.T26.C130.IMG1 | solution | other |

### Chunk A notes (from the decision agent)
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

### Chunk B notes (from the decision agent)
# Notes, chunk B (Class 7 Ch 13, topics T13, T14, T15, T16, T17, T19)

Result: 26 items = required 10 / optional 1 / none 15. Validator (`--chunk B`): errors 0, warnings 0.

Required diagrams (all data graphs):
- C57 / C58: Fig it Out 5.2 Q3, empty dot-plot frame (question) and the filled plot with mean and median (solution, derived from C57.IMG1)
- C61 / C62: Q5, empty dot-plot frame (question) and the filled two-group plot (solution, derived from C61.IMG1)
- C63: Q6, the three given dot plots (question only; solution is `none`)
- C67 (worked example, IMG2): the onion double column graph
- C71 and C73: the rocket launch graph, one diagram per question (identical spec); both solutions `none`
- C80 / C81: the cricket graph (question) and the same graph with two columns marked (solution, derived from C80.IMG1)

## 1. Judgement calls

1. **Q6 whole-class dots (C63) - please confirm.** The book's printed whole-class plot has 28 grey dots with mean 144.5, which is the FIRST section's plot repeated (p.13). It contradicts its own labels (mean 141.21, median 142.5) and the Boys/Girls plots under it. I drew the whole-class dots as the 18 boys + 14 girls (32 dots, values read from the page), which reproduces the printed mean (4519/32 = 141.22) and median (142.5) exactly. The spec's `render_note` says so. If you prefer the book's literal 28 dots, replace the first plot's `dots_per_value` and the mean line (it would then not match 141.21).
2. **Q6 boys' median.** Printed and drawn 143, but the 18 dots read from the page give 143.5 (9th and 10th values 143 and 144). I kept the printed 143 (the question text states it) and noted it in `accuracy_checks`. Boys mean 2557/18 = 142.06 vs printed 142.05 (truncated); girls mean 1962/14 = 140.14 and median 140 match exactly, which also confirms the girls' dot positions.
3. **Q3 frame has 4 rows, the book's has 3.** The data has a stack of 4 at height 60, which does not fit the book's 3-row frame; the question figure and its derived solution figure both use 4 rows so the layout is identical (rule: same layout, same positions).
4. **Q5 solution (C62): no mean/median lines.** The question only says "fill the dot plot" (Q3 explicitly says mark mean and median, Q5 does not), and the four numbers 3.43 / 3.35 / 3.45 / 3.4 are less than 30 px apart on the axis. The solution figure is the filled plot only; the two groups use SET_A / SET_B (not ANSWER green) with a Boys/Girls legend. Q5's grid is a single plot, as in the book.
5. **C67 worked example is `required` although the teaching image C67.IMG1 shows the same graph.** v3 says a figure the item needs is drawn even if a teaching image shows it (the example's task is "Draw ... one double column graph"). Result: the concept will show two similar graphs (teaching image and DIAGRAM IMG2). Colours are SET_A / SET_B instead of the book's stripes and dots.
6. **C76 (worked, daylight graph) is `optional`, not added.** The question gives the three readings per city that the answer uses, and the concept already holds the 12-month clustered graph as teaching image C76.IMG1. The figure that would help is that clustered column graph (12 monthly averages, City 1 orange / City 2 blue in the book). If you want it drawn, it is a straightforward clustered column graph; values (hours per day) are in base figure P23-bar_graph-1.
7. **Rocket questions C71 and C73 are `required`, solutions `none`.** The LP texts give readings for only 4 (C71) or 6 (C73) of the 10 organisations; the 'USA' statement and the world-total estimate need the other bars. Solutions only list numbers and mark nothing on the graph, so `SAME_AS_QUESTION_DIAGRAM`. The rocket spec has no value labels (the book has none; the task is estimation) and uses SET_A / SET_B / INK for 2021 / 2022 / 2023 (three colour-blind-safe tones) instead of the book's three blues.
8. **Cricket (C80 / C81).** Question required (every value is only in the columns). Solution required because the LP solution reads two specific columns (blue over 12 about 15, red's shortest over 4 about 2) and the earlier author's `s_figure` hint says the same: I outline those two columns (FOCUS) and add the two tags "about 15" / "about 2" (ANSWER). The red team's column colour is the hex #D55E00 (the palette vermilion = same hex as token WRONG) because the question names a "red team" and a "blue team"; it is used only as the team colour, not as a "wrong" marker. SET_B (amber) would contradict the text.
9. **Q1 (C53) is `none` with LATEX_TABLE.** The data is the plain onion-price table (rupees per kg) printed earlier in the book; a table of numbers stays LaTeX. The LP question text does not contain it (see section 2), so `text_alternative` holds the LaTeX array and `needs_lp_text_sync` is true. Not a refer-picture case: the book question names no figure.
10. **Q2, Q4, Q7 and all the worked examples T13 / T17 C75 are `none`.** All data is in the text and the work is arithmetic or word reasoning. Q7's see-saw picture (sumo wrestler and dancers) is decoration.
11. **C64 (Q6 solution) is `none`.** The answer is a written comparison; it adds no mark to the three plots (`SAME_AS_QUESTION_DIAGRAM`).
12. **Figure accounting choices.** A figure used by two items is two entries: P16-dot_plot-1 (question C57) and NEW-P16-dot_plot-1-sol (solution C58); same for P17-dot_plot-1, P20 (C71, NEW-...-C73), P26 (C80, NEW-...-C81), P19 (teaching concept image, plus NEW-P19-bar_graph-1-C67 for the worked example). P21 (annotated rocket graph) and P23 (daylight graph) map to the concept images. I also claimed P06-table-1 / P06-table-2 (onion tables in chunk A's section) with `none:LATEX_TABLE` because Q1 uses them; if chunk A maps them differently the merge keeps both as separate uses. P18-bar_graph-1 / -2 (single-town graphs, teaching step) are `none:TEXT_SUFFICIENT` (same numbers as the table and the combined graph).
13. **Decoration not listed (not in the base inventory, left out on purpose):** Kobel woodcut (p.16), sumo/ballet see-saw (p.17), midnight-sun photo (p.25), cartoon characters.
14. **Placement of labels in the spec.** Q3 solution: the two marker labels sit at the top of the lines, "Mean" to the left and "Median" to the right, because the lines are only 1.7 px apart. Cricket solution: tags sit in the empty band above the columns with dotted pointers.

## 2. Things in the LP that look wrong or thin

- **C53 (Q1):** the question text "Find the median of onion prices in Yahapur and Wahapur." has no data at all; the learner cannot attempt it. The onion table must be written into the text (LaTeX array in `text_alternative`).
- **C73 (Q2):** the question text says "decide which statements (a) to (f) are justified" but the six statements and the four options for the 2023 total are not in the text (the old `q_figure` hint put them "beside the figure"); the solution then refers to them as (a) ... (f) and "option (b)". The statements and options must go into the question text. In the solution the letter (b) is used both for statement (b) and for the total option (b); consider "option 200 to 400".
- **C71 / C73:** readings given in the text are partial (4 and 6 of 10 organisations) and "about"; fine with the figure, not enough without it.
- **C80 (T19 Q1):** the LP packs the book's four questions into one question; its text describes the graph ("bars run through all 20 overs ... red bars stop after over 18"). That description is correct (red has 18 columns). The base inventory entry P26 is wrong here (red 19 columns, over 19 = 17); corrected in the figure entry.
- **C81:** "red stopped after 18 overs without losing all its wickets, so blue batted first and red won" is the book's logic, but the drawn bars sum to blue 163 and red 152 (target 164), so the drawing does not actually show red passing blue. Not a diagram problem; the diagram does not state totals.
- **C64:** quotes first-section numbers (146.91 vs 142.94, class mean 144.5) that belong to chunk A's unit 19; consistent with concept image M2.S11.T11.C44 (means about 142.9 and 146.9).
- All sums, means, medians and counts in the LP solutions of this chunk were recomputed and are correct (Q2 total 72, Q3 total 1621 / mean 55.9 / median 56 / 13 trees, Q4 total 87.39, Q5 totals 20.6 / 20.1, Q7 totals 1201.9 / 254.5, onion months, daylight divisions, rocket 2023 total 220).

## 3. Places where the book itself is unclear

- Q6 whole-class plot is the wrong picture (judgement call 1); boys' median 143 vs 143.5 (judgement call 2).
- Q3 frame has 3 rows but the answer needs 4 (judgement call 3).
- No numbers are printed on the rocket or cricket bars. Values were measured from the page pictures (rocket about +/-0.5 launch, cricket about +/-0.3 run). Rocket values agree with the book's remarks (SpaceX 2022 "perhaps 61", 2023 about 35 more, Arianespace 2023 about half of 2022, "Other" 2023 "around 25" read as 26, which the LP also uses). Cricket: blue over 2 = 10.7 (drawn 11), over 5 = 8.7 (9), over 18 = 12.8 (13), over 12 = 14.9 (15).
- The book's whole-class mean 141.21 and boys' mean 142.05 are truncated, not rounded (141.219 and 142.056).
- The cricket graph has no legend in the book; the wicket-circle meaning is only in the book text and the LP text ("wicket circles"). I added no legend.

### Chunk C notes (from the decision agent)
# Notes for chunk C (Class 7 Ch 13, units 36-44)

Result: required 5 / optional 2 / none 8 (15 items). Validator: errors 0, 2 warnings (the solution graphs of FiO 5.3 Q2 and Q3 are drawn from the LP steps; the pdf has no printed solutions, so no base figure maps to them).

## 1. Judgement calls

- **FiO 5.3 Q1 (C82 / C83).** Question `required` (the infographic is the whole data set and the scale). Solution `none`: the answers are words and ratios read off the question graph, a picture would only repeat it.
- **FiO 5.3 Q2 and Q3 (C84/C85, C86/C87).** Question `none`: the book gives only a plain table (letters; times and temperatures) that is already in the question text, and the student draws the graph from nothing, so a question figure would be invented. Solution `required`: "draw a double-bar graph" makes the finished graph the answer (ANSWER_IS_FIGURE); `derived_from` is null because the question has no figure. Category order for Q2 follows the LP answer (Aerial, Water-borne, Spaceborne, None). Q3 axis runs to 48 degrees C (1 unit = 4) so the label above the 43 bar stays inside the plot.
- **FiO 5.3 Q4 (C88 / C89).** Question `required` (given graph, Gujarat and Delhi empty). Solution `required`, `derived_from` the question diagram: same axes, legend and the 15 given columns, plus the six new columns. The new columns keep their year colours (the legend must still hold) and carry a 5 px ANSWER outline to show what was added. I did not put value labels on the new columns: 34 px numbers such as 69000 are wider than a 48 px column.
- **Column heights of the Q4 graph.** The book gives no numbers for the five drawn states. I measured the page picture (about 300 per pixel) and used the LP solution's rounded readings (Uttarakhand 15000/16500/19000, West Bengal 10500/21000/43000, Andhra Pradesh 29500/34500/55000, Odisha 27500/44000/62500, Assam 40000/60000/64500). Page measurement of West Bengal 2022 is 10200; the base inventory said 10000; the LP says 10500 (and 43000 / 10500 = 4.1 in part (e)). I kept the LP number. The 2023 values of West Bengal (21000), Andhra Pradesh (34500) and Odisha (44000) are not quoted in the LP; they are my page measurements rounded to 500.
- **Series colours.** Only two series tokens exist (SET_A, SET_B). For the three-series graphs I added the colour SERIES_3 = #56B4E9, written out in each description: air bars in the speeds graph, 2023 in the vehicle graph. The book's own colours are blue/red/yellow (vehicles) and light blue/terracotta/dark blue (speeds); only the legend mapping matters.
- **Speeds graph layout.** The 21 gridlines are drawn at exactly equal spacing and labelled with the book's printed numbers (0, 16, 32 ... 129 ... 322). At 34 px minimum text, 3-digit labels 67 px apart would touch, so odd gridlines carry their label on a second row. The book's silhouettes, falcon painting, beetle photo, two fact sentences and the heading "How fast?" are left out; values sit in INK beside the bar end (book: white inside the bar).
- **Two-schools worked example (C90), `optional`.** The example is about the 12 printed means. The 12 dot plots are already the concept image C90.IMG1 of this very concept, so I applied the 'refer picture' logic of Step B2 (optional, no diagram, no link) and put the 12 means in `text_alternative` with `needs_lp_text_sync: true`. If you prefer a drawn copy of the 12 plots for the example, flip it to required; the picture would then duplicate C90.IMG1.
- **Heights in India Q1 and Q2 (C94-C97), all `none`.** The big table (15 rows x 8 numbers) is a plain table of numbers (the coloured headers carry no meaning), so it is a LaTeX array in the question text (LATEX_TABLE). Solutions only compare named cells whose values the steps already quote. Sibling consistency: both questions and both solutions are `none`.
- **Chart that starts at 145 cm (C98), `optional`.** Both values are in the words and the work is arithmetic. A two-bar comparison (145-based axis against a zero-based axis) would help but is not required, so it is not added; the reason names it.
- **Door example (C99), `none`.** Six heights are in the question; the picture of sorted heights and the mean line is already the concept image C99.IMG1.
- **Figure inventory.** P30 dot plots 1-12 map to concept image C90.IMG1; P32 scatter chart to concept image C98.IMG1; P27, P28 graph to items; P28 tables, P29 table and P31 table to LATEX_TABLE. Added: `NEW-P28-bar_graph-1-sol` (second use of the vehicle graph, in the Q4 solution) and `NEW-P33-mean-decision-cartoons` (decorative, DECORATIVE_ONLY). P31-table-1 is used by two questions (C94 and C96); it has one entry because both are `none` with the same reason.

## 2. Things in the LP that look wrong or incomplete

- **C94 (Heights in India Q1):** the question text "Test the six statements against the table of average heights." contains neither the table nor the six statements; both were only on the old card picture. With the card gone, the text must add the table and the six statements (needs_lp_text_sync is true). Same for **C96**, which also lacks the table (it needs at least the 2009 and 2019 columns).
- **C90 (two schools):** "Using the printed means" refers to means that appear nowhere in the question text; add the 12 means (see `text_alternative`).
- **C84 (Preyashi):** the letters w, a, s, n are never explained in the question (the book does not explain them either); the LP solution's first step gives the key. The question text could say w = water-borne, a = air-borne, s = spaceborne, n = none.
- **C83 (speeds):** the solution says "about", "estimate" and "accept 160 to 180 / 105 to 113 / 22 to 30" but the book prints the exact value in every bar (swift 170, sailfish 109, humpback whale 26). The arithmetic is right (322/170 = 1.89, 109/56 = 1.95, 109/26 = 4.19), only the wording is off. The solution also says "10 miles per hour each": the book page does not mention miles.
- **C89 (vehicles), step (a):** it says the guidelines are at 25000, 50000, 75000, 100000, but the book graph has light guidelines every 5000 (the labelled values are 25000 apart); the book asks to place bars "between the two appropriate vertical guidelines", so 89000 lies between the 85000 and 90000 lines, 62000 between 60000 and 65000.
- All other LP numbers were recomputed and hold: Q2 counts (Grade 5 a 13, w 6, s 2, n 4; Grade 9 a 8, w 6, s 9, n 2), Q3 sums 188 and 295 and means 23.5 and 36.875, the two-schools differences and comparisons, the table comparisons in C95, the growth jumps 6.2 and 5.8 cm and the 2029 estimates in C97, the door example (986, 164.33, 3 members).

## 3. Where the book itself is unclear

- Book p.126: in School B the Grade 7 boys plot and the Grade 8 boys plot are printed identical, both with mean 156.14 (same 21 dots). It looks like a printing error in the book; the LP uses the printed means, so no change was made.
- Book p.123: the speed infographic is printed rotated 90 degrees, and its scale labels beyond 80 kph (96, 112, 129 ...) are the 10-mph steps converted and rounded; the spacing is equal.
- Book p.124: the vehicle graph has no value labels and no numbers for the drawn states; all column heights are estimates.

### Chunk D notes (from the decision agent)
# Chunk D notes: Class 7 Ch 13, Figure it Out 5.4 (Q1-Q13) and Puzzle Time number lock

Result: 28 items (14 pairs). Question side: required 3, optional 0, none 11. Solution side: required 5, optional 4, none 5.
Required diagrams (8): Q1 question; Q4 solution; Q8 question and solution; Q9 solution; Q10 question and solution; number-lock solution.
Validator: errors 0, 2 warnings (Q4 and Q9 solution graphs are drawings the learner makes, so no printed book figure maps to them; expected).

## 1. Judgement calls

- **Q1 (C101/C102)**: question required (two dot plots hold all the data; I counted the markers on the page picture: boys 1+4+5+2 = 12, girls 1+1+4+5+1+1 = 13, matching the LP solution lists). One diagram holds both plots. Solution none: it only adds computed numbers and no mark on the plots (SAME_AS_QUESTION_DIAGRAM).
- **Q2, Q4, Q9 tables (C103, C107, C117)**: all plain tables, kept as LaTeX (the Q9 table is blank for the learner to fill; a blank image would imply something was given). `text_alternative` gives the array.
- **Q4 solution (C108)** required: the answer is a double-bar graph (ANSWER_IS_FIGURE). The question has no figure, so the solution diagram stands alone with `derived_from` null. Series use SET_A (watching) and SET_B (participating) rather than ANSWER green, so the legend is readable. Scale: axis 0 to 1400 in steps of 200, value on every column (105 does not sit on a tick).
- **Q9 solution (C118)** required, but Q6, Q11, Q12, Q13 solutions are only optional. Why: Q9 is an own-data question too, but the LP solution itself contains the drawing step with a concrete scale and sample numbers ("Draw an estimate bar and a measure bar for each object, scale 1 unit = 5 cm"), so the LP answer IS a graph (B2: words describing a drawing are data for the picture). The other four LP solutions only compute statistics for sample data and leave the plotting to the learner's own data (OPEN_ENDED). If you prefer strict sibling consistency, either make Q9 optional or promote Q11/Q12/Q13/Q6 to required; the sample data are all in the LP (figures that would help are named in each optional entry's `text_alternative`).
- **Q8 (C115/C116)**: question required (reading three unlabelled bars, counting around Mumbai). Solution required with `derived_from` the question diagram: it adds the three estimates (about 315, 165, 28) and the counts 12 and 7, which are the filled-in reading of the figure. All bars are drawn exactly to scale (book bars are only roughly proportional). Hidden bars are drawn at 315, 165, 28 units; I measured the book bars on the page picture: about 313, 164, 27.6 on the Hong Kong = 553 scale, so the LP estimates are consistent. 20 rows in 16:9 leave a row pitch of 46 px with 34 px text: tight but workable; if the renderer cannot hold the 34 px minimum, use a tall ratio (3:4).
- **Q10 (C119/C120)**: question required although the frame is empty, because the book prints that frame and the learner acts on it (ACTION_ON_FIGURE); the 17 values are in the text. Solution required: the completed dot plot (derived from the frame). The two weeks share ONE frame (see section 2). Week 2 uses SET_B instead of the book's red; dots keep the legend colours (SET_A triangles, SET_B circles). Mean and median are not drawn: part (a) only asks for the plot.
- **Number lock (C129/C130)**: question none (TEXT_SUFFICIENT, NUMBER_LIST_IN_BOXES): the LP question text lists all five clues with their meaning, and the digit order gives the positions. Solution required (borderline, please confirm): the 7-step deduction ends "check: it fits all five clues", and a lock showing 415 with every clue digit marked right place / wrong place / not in code shows that check; I verified 415 satisfies all five clues and is the only 3-digit code that does (search over 000 to 999). The solution figure stands alone (`derived_from` null) and redraws the book's lock-and-tiles layout; figure P39 is therefore mapped to the solution item. If the question side should also show the lock, that is a one-line change to required with a blank lock and plain tiles.
- **Q5 (C109/C110)**: none/none. The question gives all 17 heights in the text; the "Telling Tall Tales" table it points to is a plain numeric table (P31-table-1, claimed by me as `none:LATEX_TABLE` only because Q5 uses it; the section 5.4 chunk owns it too and should give it the same meaning). The LP solution quotes the two values it needs.
- **Q3, Q7 (C105, C106, C113, C114)**: none; word problems or arithmetic.
- **Q6 solution (C112)**: optional. The LP step describes "a dot plot from 135 to 160", but the question only says "you can visualise"; not added.
- **Optional items are not added** (action `drop_image`, no spec). They are Q6, Q11, Q12, Q13 solutions.

## 2. Things in the LP that look wrong or thin

- **Q10 q_figure / s_figure hints are wrong**: they say "two empty dot plot grids, one for Week 1 and one for Week 2" and "two dot plots filled". The book (page 36 picture) prints ONE frame with a legend (blue triangle Week 1, red circle Week 2); both weeks go on the same axis. The diagrams follow the book. The values 320 (both weeks) therefore share a stack.
- **Q10 axis**: LP solution says "a line from 200 to 420 in steps of 20"; the book prints labels 200 to 400 only (axis line reaches about 420) and its small ticks sit at 210, 230, ..., 410, offset from the gridlines. I put long ticks on the labelled values, short ticks every 10 and a 420 label, so 410 can be placed.
- **Q5 solution, steps 3 and 4**: step 3 is right (7 below 115, 5 above) but step 4 ("the 8 shortest in one group, the 8 tallest in the other, and the middle student at 115 is left aside or helps; measure the 115 cm students more finely") is muddled: the 9th value is one of five students at 115 cm, so a strict less-than / greater-than split cannot give equal groups. The text should say plainly which student(s) to leave out or how to break the tie.
- **Number-lock solution wording**: step 4 ("2 cannot be first, so 5 is correct in the last place") is terse but sound (6 is already out by step 1 and 4 is first by step 3); step 6 ("only the middle is free, and 7 is already in the middle there, so 1 goes in the middle") is garbled: the point is that 7 cannot be in the code, because the only free place is the middle, where it already stands in 271 (that would make it well placed, not misplaced), so the digit is 1, moved from the last place to the middle. The final code 415 is correct.
- **Q8 question text** says only "Standing tall in the storm." and never says what the chart counts; the diagram carries the measure label "Skyscrapers (taller than 150 m)" (book subtitle). Part (iii) of the solution depends on that definition, so the LP question text could say it.
- **Q9 sample data** are labelled "Sample data" in the LP only; the diagram has no such word. The book's "plam" typo is not carried into the LP (good).
- **Q2 and Q4 questions** carry the table as a run-on line ("A: 14, 16, 10, 10. B: ...", "watching: cricket 1240, ...") rather than a table; a LaTeX array would read better (text_alternative gives it). Not a diagram issue.
- Q11 LP text drops the book's lead-in "The following are some interesting things you can do with this data!" for (b); harmless.
- All the arithmetic in the C102 to C126 solutions was rechecked (sums, means, medians, ranges, counts of 12 and 7): no errors found.

## 3. Places where the book is unclear

- Q8: the three values (New York, Tokyo, London) are not printed anywhere; they can only be estimated from bar length. The book's bars are not exactly proportional to the printed values (Mumbai 86 is drawn as long as Seoul 82; Jakarta 112 as long as Bangkok 110). The diagram draws exact proportions.
- Q10: tick marks versus labels offset (above).
- Q9: the table header reads "Positive Difference", with no hint of whether the sign matters; the LP uses positive differences.
- Q5: the book does not say which part of the Telling Tall Tales table to use (age or year); the LP solution uses the 2019 columns, age 6.
- Number lock: the book prints no answer; the LP's 415 was verified by search (unique).
