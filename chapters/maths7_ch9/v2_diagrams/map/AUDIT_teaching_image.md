# Audit of the teaching-image rule (user decision 23 Nov 2026), Class 7 Ch 9 "Geometric Twins"

Rule: a question, solution or worked example that needs a figure gets its OWN diagram (`required`), even when a kept teaching (concept) image of the same concept or topic shows the same figure. Test used for every candidate: if no teaching image existed, would v3 (Steps B, B2, C, E; tie-breaker) make the item `required`?

Edited: `out_A.json`, `out_B.json`, `out_C.json`, `out_D.json` (backups `out_<X>.json.before_teaching_image_rule`; the older `.before_user_decisions` backups untouched). Validator after the edit: A, B, C, D all `errors 0`. No figure_inventory change (the eight figures are LP "talk" pictures, not printed in the book, so no base figure maps to them: the validator's "required but no inventory figure" warning is expected). This chapter's PDF has no printed-solutions section, so the 'refer picture' exception of Step B2 does not occur here.

## Flipped to required (8)
All are worked-example blocks (`ask` blocks with a talk picture), `add_new_image`, token after the question text, codes `FIG_REFERENCED` + `DATA_IN_FIGURE`. Each question points at a picture the learner is not given in the text.
- M1.S2.T2.C6 block 1, worked_example, `M1.S2.T2.C6.IMG4` (was optional): one chair drawn four times (upright facing left, on its back, upside down, mirrored) on a dotted line; "How many chairs are in this picture?".
- M1.S3.T3.C8 block 1, worked_example, `M1.S3.T3.C8.IMG2` (was optional): a plain circle, rectangle and V symbol (arm ratio 1:2, angle 80), without measuring marks, which would answer the question.
- M1.S3.T3.C9 block 0, worked_example, `M1.S3.T3.C9.IMG2` (was optional): two posts, three arrow-shaped boards on the left post (7.0 at 40, 4.0 at 195, 5.5 at -50 degrees), three blank boards of the same size and angles on the right post.
- M2.S6.T6.C25 block 0, worked_example, `M2.S6.T6.C25.IMG3` (was optional): one rectangular room split corner to corner by one middle wall (the referent of "the middle one").
- M2.S8.T8.C34 block 1, worked_example, `M2.S8.T8.C34.IMG2` (was none): two-column sheet, TOLD (two lines written) and FREE (empty).
- M3.S11.T11.C47 block 0, worked_example, `M3.S11.T11.C47.IMG2` (was optional): two straight lines crossing at 60 degrees, a separate equal arc on each of the four angles (the teaching image colours the equal pair, which would answer).
- M3.S11.T11.C48 block 1, worked_example, `M3.S11.T11.C48.IMG3` (was optional): card split ANGLES / SIDES, two marks given and a dashed third in each half, no arrow and no "?" (the teaching image has both, which would answer).
- M4.S16.T16.C71 block 0, worked_example, `M4.S16.T16.C71.IMG2` (was none): board with a scalene, an isosceles and an equilateral hole and the three matching tiles below, no counts.
Ids: next free number after the kept teaching images and the concept's other new ids (C6: IMG1, IMG2 kept, IMG3 used by block 0, so IMG4; C48: IMG1 kept, IMG2 used by block 0, so IMG3). `coverage_report.new_media_ids_created` and `meta.counts_by_role_and_decision` updated in A, B, C, D; a line was added to each chunk's `meta.notes`.

## Examined, left as is
- M1.S1.T1.C2 block 0 and 1, C3 block 0: all data in the words (torn corners, two tick marks, "the two angles facing each other"); the talk picture only illustrates.
- M1.S2.T2.C4 block 2, C6 block 2, M1.S3.T3.C8 block 0, M2.S6.T6.C23 block 1, C24 block 0, 1, 2, M2.S8.T8.C34 block 0, M3.S10.T10.C42 block 1, C43 block 2, M3.S11.T11.C48 block 2, M3.S13.T13.C60 block 2, M4.S16.T16.C69, C70 block 0 and 1: yes/no checks or word questions complete in the text.
- M1.S4.T4.C12 solution (SAME_AS_QUESTION_DIAGRAM, no measured values) and C16 solution (two short statements): the answer is not a figure.
- M2.S5.T5.C19 block 0 (sides 40, 60, 80 cm are in the words), C19 block 1 ("what is left on the floor": tape, protractor, scissors in a corridor scene), C21 block 1 ("a bag like this": two bags and three sticks, no numbers): scene pictures, `DECORATIVE_ONLY`, so not flipped (see Unresolved). C21 block 0: number reasoning.
- M2.S8.T8.C33 block 0 (optional): every datum (DF = DG, FE = GE, DE shared) is in the words; the arrowhead is drawn at C40.
- M3.S10.T10.C43 block 1 ("each of these": scissors, folding ruler, compass, door): `DECORATIVE_ONLY`, object illustrations, not flipped (see Unresolved).
- M3.S11.T11.C46 block 1 (torches): the question states both children and their torches; C61 block 0: a list of names.
- M4.S14.T14.C64 block 0 (optional): "all three sides are equal" is in the words, so the angles question needs no picture.
- M4.S14.T14.C64 block 2 (optional, "this sign"): the words give "three corners" and "a third of a turn", which is enough to answer; the picture (a triangular sign drawn three times) would only illustrate.
- M4.S14.T14.C65 block 0 and 1: the five real photographs and the Howrah Bridge photograph, `NOT_RENDERABLE`.
- Inventory: P04-illustration-1 (scenery), P07-diagram-1 (the four statements are written out in the C24 question), P19-photo-1 to 3, P19-pattern-1, P20-photo-1 (photographs / rangoli) stay `concept_image:` accounting.

## Unresolved
- Three ask questions point at an object scene and were left because the picture is an illustration, not a mathematical figure: M2.S5.T5.C19 block 1, M2.S5.T5.C21 block 1, M3.S10.T10.C43 block 1. Each question reads oddly without its picture ("what is left on the floor", "a bag like this", "each of these"). If the user wants them drawn anyway, they would be: tape, protractor and scissors as three plain tool outlines; a bag with three sticks of three lengths; four hinged two-arm figures (scissors, folding ruler, compass, door) with a dot at the pivot.
- M4.S14.T14.C64 block 2 ("this sign") is a close call (kept optional, text carries the data).
- The earlier chunk notes (notes_A to D) and the earlier `meta.notes` lines still describe the eight flipped items as optional or none; this file and the added meta note supersede them. The question text of these blocks is unchanged (the LP text is untouched).
