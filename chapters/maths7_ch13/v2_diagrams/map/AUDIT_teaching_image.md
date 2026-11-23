# Audit of the teaching-image rule (user decision of 23 Nov 2026): Class 7 Ch 13, Connecting the Dots

Scope: chunks A, B, C, D (all `none` / `optional` items whose reason, codes or notes mention a teaching image, plus every figure_inventory entry mapped to a concept image). Only `out_C.json` changed (backup `out_C.json.before_teaching_image_rule`). Validator after the edit: chunk C errors 0 (the same 2 warnings as before, for the C85 and C87 solution graphs that are drawn from LP steps); chunks A, B, D untouched.

Test used for every candidate: if no teaching image existed, would v3 make the item `required` (the learner needs the figure to attempt it: data or instruction only in the figure; a referred or lettered figure; the answer is a figure; the steps rely on the figure)? All data in the item text, a plain table, a text-only answer, or a picture that would only repeat the text or the question diagram -> left as it is.

## Flipped

- M4.S21.T21.C90, worked_example, M4.S21.T21.C90.IMG2, the twelve School A / School B height dot plots with their printed means (FIG_REFERENCED, DATA_IN_FIGURE). The question says "Using the printed means" and the LP text never states them; the steps use all twelve (150.2, 155.41, 156.14 and 156.83 appear only on the book plots). It had been `optional` through the 'refer picture' logic, which does not apply: the picture is the teaching image of the SAME concept and the item is a worked example, not a 'refer picture' answer. Spec: 16:9, two columns of six plots (School A circles left, School B diamonds right; rows Grade 6, 7, 8 boys then girls), one shared scale 120 to 170, 176 markers read from the base inventory dot lists (every list reproduces the printed mean, which the book truncates), mean line and "Mean = x" per plot. The 12 inventory figures P30-dot_plot-1..12 moved from `concept_image:M4.S21.T21.C90.IMG1` to `item:M4.S21.T21.C90 (question)`; `needs_lp_text_sync` and `text_alternative` of the old item dropped (the figure now carries the means). `coverage_report` (mapped_to_items 15, mapped_to_concept_images 1, new_media_ids_created + C90.IMG2) and `meta.counts_by_role_and_decision` (worked_example required 1, optional 1, none 1) updated. `notes_C.md` (judgement call "Two-schools worked example", and the Chunk C result line) is now superseded and was not edited.

## Examined, left as is

Chunk A
- M1.S2.T2.C3 worked_example none: a verbal statement, the book prints no figure, ride times are in the steps.
- M1.S4.T4.C8 and C9 worked_example none: all scores are in the question; the book prints a plain table (LATEX_TABLE); the bars in the teaching image are not what the example needs.
- M1.S6.T6.C15 solution none (borderline, kept under rule 3): two sums and two divisions; the book's levelled-guava picture only illustrates the same arithmetic and a careful student loses nothing without it.
- M2.S8.T8.C28 worked_example none: the data are two plain 12-row price tables (LaTeX table, text sync already noted); the teaching image is a different 5-bar graph.
- M2.S10.T10.C37 and M2.S12.T12.C48 solution optional: the answers are numbers fully written in the steps; the mean/median lines or the 15 marked dots would only help. Not a teaching-image reason (the teaching image C32.IMG1 has the mean line only).
Chunk B
- M3.S17.T17.C76 worked_example optional (borderline, kept): the question states every reading the steps use (6.8 / 18.8 / 6 and 14.8 / 9.2 / 15.1), the patterns, ranges and the three-quarters / one-quarter comparison all follow from them; the 12-month clustered graph would help but is not needed (Step D). If the user wants the graph drawn anyway, this is the one item to flip (clustered column graph, values in base figure P23-bar_graph-1).
- M2.S13.T13.C49, C50, C51 and M3.S17.T17.C75 worked_example none: data in the text, arithmetic; no figure is printed for them. M3.S16.T16.C72, C74 and M2.S14.T14.C64 solutions none: `SAME_AS_QUESTION_DIAGRAM` (they mark nothing new on the question graph).
Chunk C
- M4.S22.T22.C97 solution none: subtractions and estimates, nothing to draw.
- M4.S23.T23.C98 worked_example optional: 165 and 155 and the 145 axis start are in the question; the figure that would help is a two-bar toy picture, not the teaching image (the marker chart of 28 countries).
- M4.S23.T23.C99 worked_example none: six heights in the question; sum, mean and a comparison.
Chunk D
- No item or figure depends on a teaching image; every `none` / `optional` there is a plain table, arithmetic, an open project or word reasoning.

## Unresolved

- C90: the book prints the School B Grade 7 boys and Grade 8 boys plots identical (same 21 values, mean 156.14). A correction is not provable, so both are drawn as printed (`render_note`).
- C90 is dense (12 plots, 176 markers of 12 px). If the renderer cannot hold 12 px markers legibly at 1920 x 1080, split it into the School A and School B halves as IMG2 / IMG3 (a new id and a second token would then be needed).
