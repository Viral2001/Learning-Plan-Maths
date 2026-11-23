# Audit of the teaching-image rule (user decision 23 Nov 2026): Class 8 Ch 10, chunks A, B, C

Result: 1 item flipped (chunk B). Backup: `out_B.json.before_teaching_image_rule`. Validator after the edit: chunk A errors 0, chunk B errors 0 (3 old warnings: the FiO 3.5 solutions have no printed picture), chunk C errors 0.

## Flipped
- M2.S9.T9.C33, worked_example (block 0), new media_id M2.S9.T9.C33.IMG2: the question points at 'the pie chart' but gives no counts; draws the book's grade pie chart (slices A to E with the counts 12, 10, 8, 6, 4, no angles), data_graph. Base figure P06-pie_chart-1 moved from concept_image:M2.S9.T9.C35.IMG1 to item:M2.S9.T9.C33 (question). Counts and meta updated (worked_example required 2, none 6; mapped_to_items 8, mapped_to_concept_images 2).

## Examined, left as is
- M1.S2.T2.C2 (worked, idli, block 0): both ratios and the cross products are in the text; the book's arcs (P01) only restate 6 x 2 and 3 x 4. Block 1 cites no teaching image.
- M1.S2.T2.C3 (worked, meaning of RF): a definition question, text answer; the book's printed map belongs to C6 (required).
- M1.S3.T3.C10 (worked, Example 1 purple paint): the bar model exists only as the teaching image; the book prints no figure and the numbers are in the text.
- M1.S4.T4.C15 (solution, four-term ratio): arithmetic; the teaching image is a plain ratio table of another concept (LATEX_TABLE).
- M2.S6.T6.C20 (worked, divide 12 in the ratio 2 : 1): its reason only says the concept's image is a different example's picture; arithmetic.
- M2.S6.T6.C21 (worked, Example 3, 110 units): the book's heap-and-arrows picture only repeats 110, 20, 30, 60 that the text and steps carry; it is the 'arrow picture for a sum already written' of v3 Step D (optional band, not required). The code REUSES_CONCEPT_IMAGE stays as written.
- M2.S9.T9.C35 (worked, angle of each slice): the answer is a list of numbers (108, 90, 72, 54, 36), not a drawing; the finished chart is C36's required diagram. Not a referred figure ('each grade's slice' only continues C33).
- M3.S12.T12.C50 and C51 (worked, speed-time checks): the speed-time table is a plain table of numbers (LATEX_TABLE); the factors in the book's bracket picture are written in the steps.
- M3.S16.T16.C64 and C66 (worked), M3.S17.T17.C69 (solution): arithmetic with a number answer; the teaching images (worker-day grids, work in one hour) are other, authored pictures.

## Unresolved
- M2.S6.T6.C21 and M2.S9.T9.C35 are the two nearest calls (see above); if the user wants every book picture drawn for its example, these two would be next. Nothing else open.
