# Audit of the two user decisions of 23 Nov 2026: Class 6 Chapter 2, Lines and Angles (chunks A to F)

Rule 1 = book mistakes: the diagram shows the CORRECT value. Rule 2 = figure letters: shown only if the LP answer refers to the figures by letter.
Only out_<CHUNK>.json was edited (backups out_<CHUNK>.json.before_user_decisions next to each edited file); validate_map.py prints errors 0 for every chunk of the chapter.

## Changed (concept id | role | rule | old -> new | why)

- M1.S4.T4.C15 | solution | rule 2 | no letters -> (a), (b), (c), (d) at the top-left corner of the four panels (panel order a b / c d) | the LP answer is keyed $(a)$ to $(d)$ ("Drawings: (a): two double-arrow lines crossing at O ...")
- M3.S25.T25.C139 | question | rule 2 | captions (a), (b), (c) under the three triangles -> removed (the corner letters A, B, C stay) | the LP answer says "each triangle" and never names the triangles by letter; content, manim_description, visible_text, alt_text, accuracy_checks and render_note updated

## Examined, left as is

- C29 (bicycle, crate, ladder, bridge): four object pictures, not lettered in the LP; the answer uses only the bicycle's point letters.
- C42, C43, C45 (angle panels): the learner labels the angles; the answer has no panel letters (O, A, B, X, Y are point letters).
- C72/C73, C74/C75 (two or three dot grids): the LP says left / right grid, no letters. C86/C87 (figures i to iii) and C93/C94 (ten circles): the LP answer has no letter references.
- C121 (six protractor panels): the captions 'angle U = 35' to 'angle Z = 85' are the readings of the LP question (angle names with data), not figure letters; the answer is open-ended.
- C131 and C175 (angles a to f): the lowercase letters are the angle names the LP answer uses ('a = 80'), kept.
- C144 (clocks, identified by the time shown), C162/C174 (five angles identified by their degree labels), C169/C170 (six dot grids): the LP answers do not refer to the figures by letter.
- Rule 1: Q4(b) XY (C15) is already drawn as a ray (the book prints an arrowhead at X); C164 already draws 116 degrees (the LP text says about 40, a text matter); C178 follows the printed 8-vertex picture; the P32-protractor-5 inventory entry already starts with CORRECTED:.

## Unresolved

- None for the two rules. (LP text of C164 and C178 still disagrees with the picture, as the chunk notes already say.)
