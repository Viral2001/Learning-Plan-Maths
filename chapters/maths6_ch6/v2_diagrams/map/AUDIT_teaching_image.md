# Audit of the teaching-image rule (user decision of 23 Nov 2026): Class 6 Chapter 6, Perimeter and Area (chunks A, B, C)

Rule: a question, solution or worked example that needs a figure gets its OWN diagram, even when a kept teaching image of the same concept shows the same figure.
Only `out_B.json` was edited (backup `out_B.json.before_teaching_image_rule`; the older `.before_user_decisions` backup is untouched). `validate_map.py --chunk B` prints errors 0 (5 old warnings, unchanged). Chunks A and C: no change.

## Flipped (concept id, role, new media_id, one phrase)

- M2.S15.T15.C71 (block 1, "Why can we not use circles instead of squares to find the area?"), worked_example, M2.S15.T15.C71.IMG2: the steps rest on the book's two packings of one rectangle with circles (gaps, 42 against 44), which exist only in the picture; was none / TEXT_SUFFICIENT + REUSES_CONCEPT_IMAGE. Diagram: the same 6.2 by 7.3 rectangle twice, left 42 circles (7 rows of 6), right 44 circles (8 staggered rows of 6 and 5), no text. Checked on page_13.png (7 rows of 6; 8 rows alternating 6 and 5). figure_inventory P13-pattern-1 and P13-pattern-2 moved from `concept_image:M2.S15.T15.C71.IMG1` to `item:M2.S15.T15.C71#1 (question)`; coverage_report (mapped_to_items 14, mapped_to_concept_images 0, new_media_ids_created + C71.IMG2) and meta counts (worked_example none 5, required 3) updated. Teaching image C71.IMG1 and its block links untouched.

## Examined, left as is

- M1.S2.T2.C3 (worked, definition of perimeter): a definition in words, the book prints no figure for it; the teaching image 'Two walks, one shape' was not the reason.
- M1.S3.T3.C21 (question, FiO Q5, string made into three shapes): all lengths in the words, numeric answers; no figure in the book.
- M2.S12.T12.C55 (worked, definition and two formulas): the book's blanks are text boxes, not figures.
- M2.S15.T15.C71 block 0 (worked, circle of diameter 3 on a graph sheet): OPEN_ENDED, the learner draws it; the half-square count depends on placement (4 to 9), a picture would invent an answer.
- M2.S19.T19.C84 (solution, optional, diagonal cut of a rectangle): the question gives no figure, the printed answer is words, 6 x 4 = 24 and 24 / 2 = 12 are in the text; the teaching image C78.IMG1 (three triangles in three rectangles) is a different figure, so it was not the reason.
- M2.S21.T21.C103, C105, C107 (solutions, optional): they would only repeat the question diagrams (C98 to C106 are required); no teaching image involved.
- M1.S9.T9.C44 (solution, none): the question diagram already shows the straight and slanted edges; the argument is in words.
- M2.S21.T21.C102 (question, none): no figure of its own; the two plans are the figures of C98 and C100 (required diagrams, not teaching images).
- M2.S18.T18.C79 (worked, write a conclusion): one sentence, no figure needed.

## Unresolved

- None.
