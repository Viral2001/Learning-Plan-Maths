# Audit of the two user decisions of 23 Nov 2026: Class 6 Chapter 10, The Other Side of Zero (chunks A to F)

Rule 1 = book mistakes: the diagram shows the CORRECT value. Rule 2 = figure letters: shown only if the LP answer refers to the figures by letter.
Only out_<CHUNK>.json was edited (backups out_<CHUNK>.json.before_user_decisions next to each edited file); validate_map.py prints errors 0 for every chunk of the chapter.

## Changed (concept id | role | rule | old -> new | why)

- M4.S39.T39.C191 | question | rule 1 | orange grid row 4, column 2: -7 -> -17 (content, manim_description, visible_text, accuracy_checks, render_note, reason); needs_lp_text_sync set to true with a text_alternative | book prints -7; every row of the grid is the row above minus 9 (-20, -17, -14, -11) and the printed answer -8 and the LP tries (7, 1, -5, -11 and 16, 4, -8, -20) hold only with -17; figure_inventory P24-grid-1 now says CORRECTED:
- M4.S39.T39.C193 | question | rule 1 | same correction in the identical spec (-7 -> -17) | same picture as C191 (one diagram per item); figure_inventory NEW-P24-grid-1-q3 now starts with CORRECTED:
- M3.S27.T27.C116 | question | rule 2 | no letters -> (a) above the left set, (b) above the right set | the LP answer is keyed $(a)$, $(b)$
- M3.S27.T27.C117 | solution | rule 2 | same letters and anchors as C116 | same pair
- M3.S30.T30.C131 | solution | rule 2 | no letters -> (a) to (f) as the first characters of the six captions (captions now read "(a) (+10) - (+7) = +3" ...) | the LP answer is keyed $(a)$ to $(f)$; letters put in the captions because the panels leave no margin around them
- M4.S37.T37.C178 | question | rule 2 | no letters -> A, B, C above the three grids (left to right) | the LP question and answer call them Grid A, Grid B, Grid C
- M4.S37.T37.C179 | solution | rule 2 | same letters and anchors as C178 | same pair
- M4.S37.T37.C182 | question | rule 2 | same letters and anchors as C178 (same three grids) | its LP answer speaks of Grid A and Grid B

## Examined, left as is

- C45 to C48 (floors A to H on one line), C159/C161/C163 (points A to G on one profile), C85/C86 (points A, B, C, P, Q, R): point letters of a single figure, not several lettered figures.
- C24/C25 (matching lines), C186 (four step panels, no letters in the LP), C173, C176, C180/C181, C185, C189 (single grids), C157 (two thermometers, left and right, no letters in the LP).
- T39 grids (C191, C193) are called Grid 1 and Grid 2 (numbers, colours orange and blue) in the LP: not letters, left as drawn.
- Rule 1: C157 right thermometer already drawn at 15 (the picture shows about 16); C131(f) already strikes the six negatives (the book print shows no slashes); C179 sample grid A differs from the book's but both are correct.

## Unresolved

- LP question text of M4.S39.T39.C191 (and the copy of the question in the answer concept C192) still prints -7 in the last row of the orange grid; it must read -17 so that text and picture agree (needs_lp_text_sync is set on C191).
