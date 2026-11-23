# Audit of the teaching-image rule (user decision 23 Nov 2026), Class 7 Ch 5 "Parallel and Intersecting Lines"

Rule: a question, solution or worked example that needs a figure gets its own diagram even when a kept teaching image shows the same figure. Chunks A, B, C read (notes, `reason` / `reason_codes` of every none and optional item, all figure_inventory entries mapped to a concept image, the LP text in `in_*.json`, book pages 6, 20, 24). Only `out_C.json` was edited (backup `out_C.json.before_teaching_image_rule`). Validator after the edit: A errors 0, B errors 0, C errors 0 (the same 2 warnings as before in C: C90 and C94 have no printed figure).

Kept teaching images exist only on worked-example units here (C3, C5, C46, C51, C95); C46 and C51 already have their own diagram (IMG2). The pair units have no kept image.

## Flipped

- M6.S25.T25.C95, worked_example, M6.S25.T25.C95.IMG2: the Parallel Illusions example (two upright lines through a burst of spokes). Its steps lay a ruler along each line and measure the gap at the top, middle and bottom, so the picture is the subject of the example (FIG_REFERENCED, DATA_IN_FIGURE, SPATIAL_GEOMETRY). The earlier decision said "text is enough" because the teaching image shows the illusion. New spec of type `other`: 8 lines through (0, 0) at 22.5 degree steps (16 spokes, 5 px, length 3.30 each) and two exactly vertical 3 px lines at x = -0.80 and x = 0.80, from y = -4.10 to 4.10; no text, no parallel marks. Proportions measured on book p.20. figure_inventory P20-illusion-3 now maps to `item:M6.S25.T25.C95 (question)` (was `concept_image:M6.S25.T25.C95.IMG1`); coverage_report (mapped_to_items 20, mapped_to_concept_images 0, new_media_ids_created + C95.IMG2) and meta counts (worked_example required 1, optional 0) updated. The teaching image C95.IMG1 is untouched.

## Examined, left as is

- M1.S2.T2.C3 (worked, optional): every value and the order round the point are in the text ("a = 63, b = 117, c = 63, d = 117 going round the point"); steps are arithmetic. Without a teaching image it would still be optional (TEXT_SUFFICIENT); the teaching image C3.IMG1 was not the reason.
- M1.S2.T2.C5 (worked, optional): the text names the linear pairs (a with b, a with d) and c follows from them, so the letters are defined in words; tie-breaker says text is as good.
- M2.S10.T10.C29 (question, none): the question is a folding count fully described in words. Book p.6 prints Fig. 5.7 beside Activity 2 only as an illustration of the folds, it is not a given figure the question works on; no question figure without a given figure.
- M2.S10.T10.C30 (solution, optional): the answer is the count 3, 5, 9, 17 (text). Checked book p.24: the printed answers reprint Fig. 5.7 only as part of the reprinted question, the answer itself is text (so no ANSWER_IS_FIGURE). A row of creased squares would be a nicety.
- M1.S4.T4.C10 (solution, optional): the answer is a text table; four overlapping linear pairs cannot be marked cleanly on one figure. Not teaching-image based.
- M2.S8.T8.C20 and M2.S11.T11.C44 (solutions, optional): the 60, 80 degrees and 30, 29, 33 degrees are already in the question text; a copy of the figure would only write given numbers on it.
- M3.S13.T13.C49 (solution, optional): the steps list the four opposite pairs and the printed answer is words only (Step E: figure question, text answer). The colour-matched pairs figure would resemble the teaching image C45.IMG1 of the earlier topic, but that was not the reason.
- Solutions C84, C86, C88, C92 (none, SAME_AS_QUESTION_DIAGRAM): sibling rule inside Figure it Out 5.8, no teaching image involved.
- Question sides without a given figure (C14, C29, C31, C39, C58, C60) and the plain worked example C11: none for other reasons (OPEN_ENDED, no figure given, arithmetic).
- Figures mapped to a concept image in the inventory: P01 (Fig. 5.1), P06 and P24 (Fig. 5.7), P11-1 and P11-2 (Fig. 5.15, 5.16, early steps of Activity 3). No item needs them: Fig. 5.1 has no question unit, Fig. 5.7 see C29/C30, and C54 (question) already draws its own Fig. 5.17 with the point Y that the early steps lack.

## Unresolved

- None. Borderline kept as is: M1.S2.T2.C5 (a crossing with a, b, c, d would help a little; if the user wants it, copy the structure of M3.S12.T12.C46.IMG2 and give it id M1.S2.T2.C5.IMG2).
