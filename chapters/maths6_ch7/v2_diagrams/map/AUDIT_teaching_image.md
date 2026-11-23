# Audit of the teaching-image rule (user decision of 23 Nov 2026): Class 6 Chapter 7, Fractions (chunks A to F)

Test used for every candidate: if no teaching image existed, would v3 make the item `required`? As a control I compared each candidate with its nearest sibling that has no teaching image (same kind of question, same kind of answer). No file was edited (no backups were needed); `validate_map.py` was not re-run because nothing changed.

## Flipped (concept id, role, new media_id, one phrase)

- none

## Examined, left as is

- M1.S2.T2.C2 (roti shared by 2 and by 4 children): every number is in the question, the book picture only illustrates the sharing (DECORATIVE_ONLY).
- M1.S2.T2.C3 (1/5 or 1/9): the book prints no picture.
- M1.S7.T7.C23 (fold a strip in two), M1.S7.T7.C25 (halves as addition statements): one-line answer and LaTeX statements; the question gives no figure; the control C24 (fold again, strip of 4 parts, no teaching image) is `optional` for the same reason.
- M2.S13.T13.C58 (classify the fractions), C62 (why 4/3 > 1; the book gives a speech bubble only), M2.S15.T15.C81 (one roti, four children; decorative picture, answer = three equations): text / LaTeX answers, no figure given.
- M3.S21.T21.C122, M3.S22.T22.C127, M2.S18.T18.C114, M3.S30.T30.C183: equivalent-fraction arithmetic in LaTeX; the figures named in the reasons belong to other examples.
- M3.S25.T25.C144 (how much chikki is left): the LP question states the 3/4 eaten, the answer is 1 - 3/4; the book strip only repeats it.
- M3.S24.T24.C142 (Meena's chikki, `optional`), M3.S26.T26.C149 and C151 (same-unit addition with strips, `optional`), M3.S28.T28.C164 (6/7 - 4/7, `none`): the book works them with strips, but question and steps are complete in text and the question gives no figure; the controls C24 and C149/C151 (no teaching image on C149/C151) are `optional` for the same reason, so the teaching image was not the reason. (The number-line "Try" C165 is already required.)
- M4.S31.T31.C184 (history, answered in words).
- M1.S9.T9.C29 (optional, table of half rotis): the LP question text carries all five equations; not related to a teaching image.

## Unresolved

- None. Borderline calls the user may want to flip if every book strip picture of a worked example should be drawn: C142, C149, C151, C164 (specs are sketched in notes_E.md and notes_F.md).
