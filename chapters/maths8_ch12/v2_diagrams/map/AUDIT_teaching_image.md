# Audit of the teaching-image rule (user decision 23 Nov 2026): Class 8 Ch 12, chunks A, B, C

Result: 2 items flipped (chunk B). Backup: `out_B.json.before_teaching_image_rule`. Validator after the edit: chunk A errors 0, chunk B errors 0 (warnings 0), chunk C errors 0.

## Flipped
- M1.S13.T13.C51, worked_example (block 0), new media_id M1.S13.T13.C51.IMG2: 'find his total and say the formula' needs the row and column of Nagesh's marks, readable only from the spreadsheet; draws the plain marks grid (A to H, rows 1 to 8, Total empty), no formula shown. Base figure P11-spreadsheet-1 moved from concept_image:M1.S13.T13.C51.IMG1 to item:M1.S13.T13.C51 (question).
- M1.S13.T13.C52, worked_example (block 0), new media_id M1.S13.T13.C52.IMG2: same reason for Gowri's average (row 7, columns B to D); identical grid, new inventory entry NEW-P11-spreadsheet-1-C52 maps to it.
Counts and meta updated (worked_example required 2, none 0; inventory 10 figures, mapped_to_items 5, mapped_to_concept_images 1).

## Examined, left as is
- M1.S2.T2.C2, C3, C4, C5 and M1.S5.T5.C21 (worked, mean and median examples): every datum, sum and distance is in the question or the steps; the dot plots (balance, new value, median) are illustrations of arithmetic already written, so v3 gives none/optional without them (tie-breaker: a careful student loses nothing). C5 also uses other data than the book's plot.
- M1.S3.T3.C9 (question, +10 and doubling): the LP question lists all eleven values; the book's two dot plots are only hints.
- M1.S10.T10.C44 (solution, mean family size): the question gives a plain frequency table (LATEX_TABLE) and the solution is arithmetic; the book's dot plot beside it adds no mark (it also carries a print slip, see notes).

## Unresolved
- M2.S15.T15.C56 (worked, Kerala April 33 and July 29 'on the line graph'): not a teaching-image `none` (the old reason is 'numbers are in the text'), so left, but the question points at the line graph and its steps describe the graph ('the point sits at the top of its column', 'the line joins the points'); the concept's kept image C56.IMG1 shows the same thing. If the user wants it, add M2.S15.T15.C56.IMG2 with the same spec as C57's graph (render_note 'same as M2.S15.T15.C57.IMG2'). Also borderline and left: C83 and C85 ('on the scale', the scale is given in numbers in the steps).
