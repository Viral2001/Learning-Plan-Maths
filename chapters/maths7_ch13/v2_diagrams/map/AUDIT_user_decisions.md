# Audit of the user's two decisions (23 Nov 2026): Class 7 Ch 13, Connecting the Dots

Scope: all four chunks (A, B, C, D), 29 required diagrams. Only `out_B.json` changed (backup `out_B.json.before_user_decisions`). Validator after the edit: chunk B errors 0, warnings 0; chunks A, C, D untouched (errors 0).

## Changed items

| concept id | role | rule | old -> new | why |
|---|---|---|---|---|
| M2.S14.T14.C63 | question | 1 | Boys plot, dashed median line and label "Median = 143" -> "Median = 143.5" (content, manim_description, visible_text, accuracy_checks) | Book p.17 prints boys' median 143 (also in the LP question text and C64 step 1). The 18 boys' dots (130, 133, 136, 138, 140, 142, 143 x3, 144 x2, 145 x3, 146 x3, 148; sum 2557 reproduces the printed mean 142.05) have 143 as 9th and 144 as 10th value, so the median is 143.5. Re-counted on a 4x crop of book page 17. |
| M2.S14.T14.C63 | question | 1 | `render_note` gets "Book prints the whole-class dots as the first section's 28 dots (mean 144.5); corrected to the 18 boys plus 14 girls (32 dots)." and "Book prints the boys' median as 143; corrected to 143.5." | The whole-class correction was already drawn by the chunk B agent (32 dots = boys + girls, mean 141.21875, median 142.5, recomputed); only the required sentence was missing. Book p.17 whole-class plot is a copy of the p.13 first-section plot (checked on both page images). |
| M2.S14.T14.C63 | question | 1 | `needs_lp_text_sync: true` and `text_alternative` added | The LP question text ("boys: ... median 143") and the C64 solution (step 1 "median (143 against 140)" and the answer text) still carry the printed 143. They need 143.5 so the text agrees with the figure. C64 itself stays `none`, no diagram. |
| figure_inventory P17-dot_plot-2 | - | 1 | description now starts "CORRECTED:" | Base inventory records the slip in `unclear`. |
| figure_inventory P17-dot_plot-3 | - | 1 | "median 143 (as printed)" -> "CORRECTED: ... the book prints median 143, the diagram draws 143.5 ..." | Description must match the diagram. |
| meta.notes (chunk B "BOOK FLAW" entry) | - | 1 | "Needs the user's confirmation." -> records the decision and the boys' median change | Entry was waiting on this decision. |

Note: `notes_B.md` judgement calls 1 and 2 (whole-class dots; boys' median "kept as printed") are now superseded by the table above; the notes file was not edited (brief: out files only).

## Examined, left as is

- C29 (onion dot plots): 24 dots equal the two onion tables (sums 458 / 450); no slip.
- C40/C41 (Bookworm): 15 slips recomputed, mean 122/15 = 8.13, median 6; matches the book's "median 6".
- C42/C43 (Newspaper): 7 values, mean 128/7 = 18.29, median 18; the unlabelled right edge at 30 copies the book and is not a wrong value.
- C45 (two minute plots): means 1921/33 = 58.21, 1660/28 = 59.2857, medians 60 and 59.5 recomputed; the book's 59.28 is a truncation and 59.29 (LP) is already drawn and recorded in `render_note`.
- C57/C58 (palm trees): 29 values, sum 1621, mean 55.9, median 56, 13 shorter; the 4-row frame (book 3 rows) is a layout choice, not a value.
- C61/C62 (newborn weights): table equals the book; sums 20.6 / 20.1.
- C67 (onion double column graph): 24 column heights equal the two tables.
- C71/C73 (rocket graph): no printed numbers; values measured; "Other 2023" 26 vs the book's words "around 25" is an estimate that the LP also uses, not a print slip.
- C80/C81 (cricket graph): the base inventory's "red has 19 columns, over 19 = 17" misreads the picture; the diagram (red stops after over 18, 17 in over 18) is right (book page 26 re-checked).
- C82 (speeds infographic): bar values and bar lengths agree; the tick labels 96 and 112 are not changed to 97 and 113 because the book labels the first step "16 kph" (6 x 16 = 96, 7 x 16 = 112) and only later labels follow the exact mph conversion, so a slip is not proved; no answer uses them.
- C85/C87 (own-data graphs from the tables): counts a 13/8, w 6/6, s 2/9, n 4/2 and the temperatures, sums 188 / 295, recomputed.
- C88/C89 (electric vehicles): the five drawn states have no printed numbers (LP readings used; West Bengal 2022 = 10500 LP vs 10200 measured is an estimate); Gujarat and Delhi equal the printed table.
- C101 (pockets): 12 boys and 13 girls markers equal the LP lists (sums 56 and 45).
- C108 (sports): equals the printed table (athletics "participating" 105 looks odd but the book table and the LP agree, so no correction is proved).
- C115/C116 (skyscrapers): the book's bars are not proportional (Mumbai 86 drawn as long as Seoul 82, Jakarta 112 as long as Bangkok 110); the diagram already draws exact lengths and says so in `render_note`.
- C118 (own-data sample graph): LP sample numbers only.
- C119/C120 (Sudoku weeks): 9 + 8 values, sums 3240 / 2230, one shared frame as the book; the book's offset small ticks are already placed on the labelled values and noted.
- C130 (number lock): 415 satisfies all five clues and is unique (re-verified by hand and by the chunk D search); the book prints no answer.
- C90 and C98 (optional, no diagram): the book's identical School B Grade 7 and Grade 8 boys plots (P30-dot_plot-9/-11) live only in the teaching image C90.IMG1; nothing to change in a required diagram.

Rule 2 (figure letters): no required diagram holds lettered figures (a), (b), ... Pictures with several plots (C29, C45, C63, C101, C119/C120) identify them by names or colours (Yahapur/Wahapur, First/Second group, Whole class/Boys/Girls, Boys/Girls, Week 1/Week 2), and the LP answers refer to them the same way, never by letter. The "(a)" to "(f)" in C73, C82, C88/C89, C101, C115 and C120 are question parts or statements, not figures. No letter was added or removed.

## Unresolved

- C80/C81 (cricket graph, book p.122): the LP and the book say red won because it stopped after over 18 without losing all its wickets, but the drawn red columns (overs 1 to 18) add to 152 and the blue columns to 163 (about +/-0.3 run per column), so the picture does not show red passing blue. The book picture is probably what is wrong, but which red values should be higher is not forced by the LP solution or by arithmetic, so the figure stays as printed. The diagram states no totals.
- C63 LP text: the corrected boys' median 143.5 needs the text sync named in C63 (question text, C64 step 1 and answer text). Until then the figure and the LP sentence disagree about 143 versus 143.5.
