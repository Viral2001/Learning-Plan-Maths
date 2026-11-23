# Audit of the teaching-image rule (user decision of 23 Nov 2026): Class 6 Chapter 9, Symmetry (chunks A to D)

Test used for every candidate: if no teaching image existed, would v3 make the item `required`? As a control I compared each candidate with its nearest sibling that has no teaching image. Edited: `out_A.json` only (backup `out_A.json.before_teaching_image_rule`); `validate_map.py --chunk A` prints errors 0, warnings 0. notes_A.md was not edited (it still says optional for C27).

## Flipped (concept id, role, new media_id, one phrase)

- M1.S7.T7.C27, worked_example, M1.S7.T7.C27.IMG2 (add_new_image, question_tex / after_question_text, block_index 0): lettered square ABCD with its vertical line (book p.6) and an answer that is where the labelled corners go; control C31 (same kind of answer, no teaching image) is required. Diagram: square, FOCUS dashed vertical line, two ANSWER double arrows (A-B, D-C), same visual language as C31. figure_inventory P06-shape-1 moved from `concept_image:M1.S7.T7.C27.IMG1` to `item:M1.S7.T7.C27 (question)`; coverage_report and counts updated.

## Examined, left as is

- M1.S2.T2.C3 (Taj Mahal, Gopuram, clouds): NOT_RENDERABLE photographs.
- M1.S4.T4.C9 (fold a square four ways): no figure given, answer is a count and a list of folds.
- M1.S5.T5.C14 and C16 (solutions, `optional`), C15 (question, `optional`): printed answers are text only ("4", "No"); the controls C13 (none) and C15 (optional, no teaching image on its own concept) have the same reason, so the teaching image was not decisive.
- M1.S10.T10.C38 (ink blot): hands-on, OPEN_ENDED.
- M2.S12.T12.C52 (rangoli, `optional`): the question text names the ring and the four red petals and the answer is a sentence; the control C53 (paper windmill, `optional`, no teaching image) has the same reason.
- M2.S12.T12.C55, C56, C57 (square: angles of symmetry, centre, other angles): the questions give no figure, answers are numbers. C55's answer mentions corners A to D that exist only in the book's figure (LP text issue, see notes_B.md); the figure is not what the question asks for.
- M2.S15.T15.C66 (4 radial arms), C71 (3 arms, unequal angles), C72 (change the three-arm figure): the question text gives every datum (equal arms, 90 degrees; unequal angles; make the angles equal); controls C70 and C71 (no teaching image) are `optional`/`none`. C69, C73, C74 (answer or labels only in a picture) are already required.
- M2.S20.T20.C97, C98, C99 (smallest angle, diameter, objects around us): decorative or no book figure; C99 is OPEN_ENDED.

## Unresolved

- M2.S15.T15.C66: the LP phrase "the angle between adjacent central dotted lines" has no referent without the book's plus-shaped figure (the author of chunk C already offered to promote it). Left `optional`; if the user wants the figure, the spec is in notes_C.md (plus shape, dashed centre lines, 90 degree arc).
