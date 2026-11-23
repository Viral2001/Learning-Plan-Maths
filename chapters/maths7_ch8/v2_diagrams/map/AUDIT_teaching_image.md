# Audit of the teaching-image rule (user decision 23 Nov 2026), Class 7 Ch 8 "Working with Fractions"

Rule: a question, solution or worked example that needs a figure gets its own diagram even when a kept teaching image shows the same figure. Chunks A, B, C read (notes, `reason` / `reason_codes` of every none and optional item, all figure_inventory entries mapped to a concept image, LP text in `in_*.json`). No file changed (no backup made); validator A, B, C errors 0 (same warnings as before).

Kept teaching images exist only on worked-example units: C28 (already required, own IMG2), C36, C37, C63 and C106 (already required, own IMG2). The pair units (T3 solutions C8 / C10, T7 solutions C31 / C33) have no kept image; C31 and C33 are already required with own diagrams although the teaching images C25 / C27 show the same unit squares.

## Flipped

- none.

## Examined, left as is

- M1.S14.T14.C63 (worked, none, `REUSES_CONCEPT_IMAGE`, 1/2 x 1/4 and 1/4 x 1/2): steps 1 and 2 are the arithmetic (1 x 1)/(2 x 4) = 1/8 and (1 x 1)/(4 x 2) = 1/8; step 3 states the equal rectangle areas in words; nothing refers to a figure. Without the teaching image C63.IMG1 (two unit squares, one turned) v3 would give none or optional (TEXT_SUFFICIENT: a careful student loses nothing). The teaching image was not the only reason.
- M1.S9.T9.C36 and C37 (worked, none): C36 literally says "without drawing the unit square"; both are plain arithmetic (18 x 12 = 216, 5 x 7 = 35, 12 x 18 = 216); the book's 216-cell grids are schematic ("18 parts", "12 parts") and unreadable at card size. Teaching images C36.IMG1 / C37.IMG1 stay.
- M1.S3.T3.C8 and C10 (solutions, optional): numeric answers with complete LaTeX steps; the book's number lines (pp.1, 3) are lesson figures, not printed-answer pictures (printed answers pp.31-32 are text). Step E: numeric answer, no new visual thing. Teaching images (T1 C1, T2 C4) were named only as where the line already exists.
- M1.S13.T13.C52 (solution, optional): subtraction in the steps is complete; a 36-part bar would be a nicety. Not teaching-image based.
- M3.S21.T21.C87 (solution, optional) and C89 (solution, none): tape strip (book Example 3 figure) and the 25-brick unit square are niceties for a numeric chain; C89's "unit square of 25 bricks" is the teaching image of an earlier topic and not a figure of the example.
- M3.S24.T24.C110, M3.S25.T25.C112, M3.S25.T25.C114 (solutions, optional, SAME_AS_QUESTION_DIAGRAM): figure-based question with a required question diagram and a numeric text answer; Step E precedent, no teaching image involved.
- Inventory entries mapped to a concept image (P01, P02, P03, P05, P06, P07, P09, P10, P14, P20, P21): the items that need the same figure already carry their own diagram (C26, C28, C31, C33, C35, C42, C106) or are decided none above (C8, C10, C36, C37, C63).

## Unresolved

- None. Borderline kept as is: C63 (if the user wants the two-square picture next to the text, id `M1.S14.T14.C63.IMG2`, same layout as the kept image).
