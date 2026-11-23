# Audit of the two user decisions (23 Nov 2026), Class 7 Ch 14 "Constructions and Tilings"

Scope: `out_A.json`, `out_B.json`, `out_C.json` (47 required items across 3 chunks; 74 items in all). Rule 1 (book mistakes: diagram shows the correct value) and Rule 2 (figure letters only when the LP answer uses them). Sources read: `notes_A/B/C.md`, both base inventories (all `unclear` fields), `book/chapter_text.md` (all pages), the book page pictures 2, 4, 6, 8-13, 16-21, 23-25, and the LP snapshot `source/cbse_eng_maths7_ch14_v39.json` (question, steps and answer text of every required item).

Result: NO item changed. No `out_*.json` file was edited, so no `.before_user_decisions` backup exists. Validator re-run on the untouched files: A errors 0 (9 warnings), B errors 0 (7 warnings), C errors 0 (1 warning); the warnings are the known "required solution figure not printed in the book" ones.

## Changed items
None.

## Rule 1 (book mistakes): examined, left as is
No print slip was found in any picture that a required item draws "as printed". The base inventories record none (their `unclear` entries are only estimates of sizes, counts of hatch lines, and artwork that cannot be counted), and notes A, B, C record none.
- C48/C49 gap-angle figure (book p.17): the printed angles 40, 60, 50, 30, 40, 90 and the 70 degree wedge agree with the printed equation (sum 310, gap 50). Both items are `none` anyway, so nothing is drawn.
- C50, C51, C44 (Fig. 6.12 hexagon, p.16-17): letters A to F, O and the three lines match the book; 6 x 60 = 360 holds.
- C53, C58, C60, C56 (60 and 120 degrees, 4 cm and 5 cm hexagons, p.17-18): values agree with the book text and the LP steps.
- C65 (30 and 15 degrees): AD at 30, AF at 15, E on AD with AE = AB, all asserted in code; book prints no figure.
- C66, C67 (6-pointed star, p.19): the book's hint letters (outer A to F clockwise from the top, inner G to L clockwise from the upper left) match the spec positions; triangles AGH, BHI, CIJ, DJK, ELK, FLG are the same triangles as in the book (ELK = EKL); 3 x 60 per point triangle and 120 at each inner corner re-add to 360.
- C89, C91, C93 (T25 Q1, Q2, Fig. 6.13, p.23-24): the removed squares in the book pictures are row 1 col 3, row 2 col 2 and row 1 col 2; the specs remove exactly those, 14 squares each.
- C94, C96, C100 (chessboard counts): 8 white and 6 black (the book prints the same for Fig. 6.14), 8 and 7 for the full 5 x 3 grid, 32 and 30 for the 8 x 8 grid minus the top-right and bottom-left squares (the book's p.25 picture removes those two); recomputed, all correct.
- C97, C98, C99 (FiO tilings, p.25): 12 squares and 62 squares match the pictures.
- C74, C75, C77, C81, C83 (tilings p.22-23): grid sizes and tile counts (12, 14, 12, 6) recomputed; the book says "4 x 6 ... 4 rows and 6 columns".
- C36, C37, C39 (copy an angle, p.11-12): labels A, B, C, X, Y, Z as printed; the four orientations of C39 are those of the book's FiO Q1 picture (sizes are chosen, not printed; not a slip).
- C40, C43 (parallel line construction, p.13): D, F, E, C placement as in Fig. 6.8 to 6.10; lowercase a (the printed angle label of Fig. 6.7) is not drawn.
- C4, C8, C10, C11, C14, C16, C18, C22, C23, C24, C27, C28, C29, C32, C33 (pages 2-10): no wrong digit, count or label in the book pictures (A, B, X, Y, O, C, D labels as printed); the 45 degree of Fig. 6.5 (360 / 8) is right. Pages 3, 5, 7 were read as text only; their pictures belong to items already covered (C4, C14, rope figure not used).
- Tangram silhouettes (p.20-21) and the tilings of p.26-27: all mapped `none` (no LP question), so Rule 1 cannot apply.

## Rule 2 (figure letters): examined, left as is
Items whose picture holds several figures, and the LP answer text checked for letter references such as "(a)", "figure (b)", "the second picture" (none found in any required item):
- C27 (four angles with bisectors, 2 x 2 panels): spec shows only point letters O, A, B, C; LP answer and steps say "four angles ... a small acute angle, a right angle ..." with no panel letters. No letters added.
- C39 (four angle copies, 2 x 2 panels): point letters only; LP names the four angles by direction ("one opening upwards, one sideways ..."), not by letter. No letters added.
- C43 (four pairs of parallel lines, 2 x 2 panels): point letters and line names l, m, n only; LP says "across, up and down, and two slanting ways". No letters added.
- C65 (one picture for the 30 and the 15 degree blocks): not a lettered set of figures; LP refers to points B, C, D and E, F only. No panel letters.
- C97/C98/C99/C100 and C74/C75 (region plus tile): the printed labels "Region to be tiled" and "Tile" are category labels, not figure letters; the book's FiO items are numbered 1 and 2, which the diagrams do not show.
- C94, C96 ("8 white", "6 black" counts) and all remaining required items: single figures, no figure letters shown.
- No spec shows "(a)", "(b)" or similar anywhere (checked the `visible_text`, `manim_description` and every text element of `content` of all 47 required items), so there is nothing to remove either.

## Unresolved
None.
