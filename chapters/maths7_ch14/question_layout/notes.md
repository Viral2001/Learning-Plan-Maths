# Class 7 Ch 14 Constructions and Tilings (cbse_eng_maths7_ch14, live v36; Part II chapter 6, book text gegp206): question layout notes

Spec: `layout_spec.json`. Result of `check`: 33 question concepts in 11 Questions topics (12 existing Figure it Out
concepts kept in book order + 21 new: 0 example, 0 exercise, 21 prompt). Five Questions topics are new (after "Eyes and
the Perpendicular Bisector", "A Right Angle at a Point on a Line", "A Regular Hexagon from Six Triangles",
"Constructing 60°, 120° and a Regular Hexagon", "Tiling Grids with 2 × 1 Tiles"); the other six already exist. 13 new
videos needed (every question cut out of a teaching concept by block), 7 live videos kept whole, 1 kept but covering
only part of its question (30° and 15°: refresh), 0 videos folded. `INTEGRITY: clean`; gates unchanged from live
(structure 0 to 0, coverage 0 to 0, video_script_rules 43 to 43, skeleton 2 to 2, objectives 0 to 0). The live
concept-to-media links are intact (checked before authoring).

## How a book question was recognised here

Every question in this edition carries the round "?" icon, including lead-ins that the book answers one line later
(checked on PDF pages 1 to 25), so the icon decides nothing. I counted a plan block when the book puts a task or a
concrete question straight to the reader (construct, draw, justify, explain why, find, "Is this grid tileable?", "Will
the 70° angle fit?") and the plan block holds that question, its steps and its answer. The book prints no label
"Example" anywhere, so every new question is a prompt. I did not count a block whose only book source is a general
lead-in ("how do we draw ...?", "will it always ...?", "which triangles should be congruent?") that the book itself
carries out step by step in the next lines (a printed method or a derivation), nor a block the plan wrote itself.
Those eight blocks stay in their teaching concepts (see Borderline).

## New questions

Plan source is `concept block` (b2 = the worked-example block of a teaching concept) or `whole` (a thin-extra concept,
moved with its video). Block-built questions have no video yet. Page numbers are the printed ones.

| # | New question concept | Book label or quote | Plan source (ref) | Tier | Why it counts |
|---|---|---|---|---|---|
| 1 | Eyes: construct an eye on XY | p137 "From X and Y, draw arcs above and below XY, with the same radii ... Use this to construct an eye." | M1.S2.T2.C3 b2 (6.1.eye_centres) | prompt | Imperative task with a definite drawing; the book gives only a two-sentence method. |
| 2 | Perpendicular Bisector: points equally far from X and Y | p139 "Justify the following statement using the facts that we have established. Any point that has the same distance from X and Y lies on the perpendicular bisector of XY." | M1.S2.T2.C5 b2 (6.1.equidistant) | prompt | Imperative with a definite justification, not worked out in the book. |
| 3 | Right Angle at a Point: construct 90° at O | p141 "Draw a line and mark a point O on it. Construct a 90° angle at point O." | M1.S5.T5.C12 b2 (6.1.right_angle) | prompt | Imperative task; the plan block asks the same and adds the reason. |
| 4 | Copying an Angle: copy an angle with a compass | p145 "Draw an angle. Create a copy of this angle using only a ruler and compass." | M2.S8.T8.C21 b2 (6.1.copy_steps) | prompt | Imperative task, then "Here is one simple approach". |
| 5 | Angles Round a Point: the gap and the 70° angle | p152 "Will the 70° angle fit into the gap? What is the gap angle ∠AOI? ... Use this to determine whether the 70° angle fits the gap." | M3.S12.T12.C28 b2 (6.1.gap_360) | prompt | Concrete numbers; the book sets up the equation and leaves the sum to the reader (gap 50°, so no). |
| 6 | Hexagon from Triangles: AOD, BOE and COF are straight lines | p152 "In Fig. 6.12 can you explain why AOD, BOE and COF are straight lines?" | M3.S12.T12.C29 b2 (6.1.straight_lines) | prompt | Put to the reader, not answered in the book; three 60° angles make 180°. |
| 7 | Regular Hexagon: side 4 cm | p152 "Construct a regular hexagon with a sidelength 4 cm using a ruler and a compass." | M3.S13.T13.C33 whole (6.1.hex_4cm); video kept | prompt | Imperative construction. Thin-extra, one block, so it moves whole. |
| 8 | 60° Angle: construct it and say why | p153 "How do we construct a 60° angle? ... Why is ∠CAX = 60°? Is there an equilateral triangle here?" | M3.S13.T13.C31 b2 (6.1.angle_60) | prompt | "Why is ∠CAX = 60°?" is put to the reader and left unanswered; the block holds the construction and the reason. |
| 9 | Regular Hexagon: side 5 cm | p153 "Construct a regular hexagon of sidelength 5 cm." | M3.S13.T13.C34 whole (6.1.hex_5cm); video kept | prompt | Imperative construction. |
| 10 | Related Constructions: 30° and 15° angles | p154 "How will you construct 30° and 15° angles?" | M3.S14.T14.C36 b2 (6.1.angle_30) + C37 whole (6.1.angle_15, folded by canon); C37 video kept | prompt | One printed question the plan split in two (30° in the teaching concept, 15° as a thin-extra). C37's video covers only the 15° part (refresh). |
| 11 | 6-Pointed Star: the six point triangles | p154 "Are the six triangles forming the 6 points of the star ... equilateral? Why? [Hint: Find the angles.]" | M3.S14.T14.C38 b2 (6.1.star) | prompt | Definite question (yes, each is 60° 60° 60°). The block does not cover "Construct the 6-pointed star" (see Gaps). |
| 12 | Tiling Grids: a 4 × 6 grid | p157 "Can a 4 × 6 grid be tiled using multiple copies of 2 × 1 tiles?" | M4.S16.T16.C41 b2 (6.2.grid_4x6) | prompt | Concrete question; the plan shows one tiling (the book shows another, "one way"). The definition ref tiling_def stays on C41. |
| 13 | Tiling Grids: a 4 × 7 grid | p157 "Can a 4 × 7 grid be tiled using 2 × 1 tiles?" | M4.S16.T16.C42 whole (6.2.grid_4x7); video kept | prompt | Concrete question, unanswered in the book (yes). |
| 14 | Tiling Grids: why 5 × 7 cannot be tiled | p157 to p158 "What about a 5 × 7 grid? ... observe that this grid has 35 unit squares. Each tile covers exactly 2 unit squares. ... Complete the justification." | M4.S16.T16.C43 b2 (6.2.grid_5x7) | prompt | "Complete the justification" is a task left to the reader (35 is odd). |
| 15 | Tiling m × n Grids: both even | p158 "Is an m × n grid tileable with 2 × 1 tiles, if both m and n are even? If yes, come up with a general strategy to tile it." | M4.S16.T16.C44 b2 (6.2.mn_even) | prompt | Asks the reader for a strategy. |
| 16 | Tiling m × n Grids: one even, one odd | p158 "... if one of m and n is even and the other is odd? If yes, come up with a general strategy to tile it." | M4.S16.T16.C45 whole (6.2.mn_mixed); video kept | prompt | Same shape; the book gives no answer. |
| 17 | Tiling m × n Grids: both odd | p158 "... if both m and n are odd? Give reasons." | M4.S16.T16.C46 whole (6.2.mn_odd); video kept | prompt | Asks for reasons; no answer in the book (no). |
| 18 | Missing Squares: top right of a 5 × 3 grid | p158 "Here is a 5 × 3 grid, with a unit square removed. Now, it has an even number of unit squares. Is it tileable with 2 × 1 tiles?" | M4.S17.T17.C48 b2 (6.2.minus_corner) | prompt | The printed figure has the top right square removed, as the plan says. Yes. |
| 19 | Missing Squares: middle of the second row | p158 "Is the following region tileable with 2 × 1 tiles?" | M4.S17.T17.C49 whole (6.2.minus_middle); video kept | prompt | The printed figure has the middle of row 2 removed, as the plan says. Yes. |
| 20 | Colouring Squares: top middle removed | p159 "What about this one? (Fig. 6.13) Were you able to tile this? How can we be sure that this is not tileable?" | M4.S17.T17.C50 b2 (6.2.colour_613) | prompt | Fig. 6.13 has the middle of the top row removed, as the plan says. No: 8 white and 6 black squares remain, as the book states for Fig. 6.14. |
| 21 | Colouring Squares: another square to remove | p159 "Can you find another unit square that, when removed from a 5 × 3 grid, makes it non-tileable?" and p160 "Use this idea to find another unit square ..." | M4.S17.T17.C51 whole (6.2.colour_another); video kept | prompt | The same question is printed twice; one concept. Any of the seven black squares. |

Placement: in each Questions topic the new questions come before the existing Figure it Out concepts, in the order the
book prints them (in-text questions before the section's Figure it Out). In "Constructing 60°, 120° and a Regular
Hexagon" the 4 cm hexagon comes first, then the 60° question, then the 5 cm hexagon, as on pp152 to 153. The existing
Figure it Out concepts are all listed with `keep` in book order; the engine would have kept them anyway, the `keep`
entries carry their figures.

## Borderline, not moved

Eight blocks stay in their teaching concepts. Each is a general lead-in that the book answers itself in the next lines,
or the plan's own framing; none has a printed task addressed to the reader.

- M1.S2.T2.C4 why_bisector: "Will the line joining ... always be the perpendicular bisector of XY?" and "Which two triangles should be congruent ...?" are answered by the book's two-page congruence derivation (SSS then SAS). The plan block is that derivation retold as "Prove that ...".
- M1.S4.T4.C7 pb_steps: "Given a line segment XY, how do we draw its perpendicular bisector ...?" is a method heading answered by the numbered steps 1 to 3 printed under it. The method stays as the teaching example; the application ("Use this to construct an eye") is question 1.
- M2.S6.T6.C14 bisect_method: "We will now develop a general method to bisect any angle" and "How do we construct these congruent triangles, given the angle?" are exposition; the practice is Figure it Out Q1.
- M2.S6.T6.C15 bisect_45: "What is the angle between two adjacent lines? ... How do we construct a 45° angle ...?" are answered in the next two lines (45°, construct 90° and bisect). The 8-petalled figure itself is a Gap.
- M2.S10.T10.C24 parallel_steps: "How do we implement this idea using a ruler and a compass?" is answered by Figs 6.7 to 6.10.
- M3.S12.T12.C27 hex_triangles: "Can six congruent equilateral triangles be placed together as in Fig. 6.12? If yes, will it result in a regular hexagon?" is answered by the derivation over the next paragraphs; the 70° gap question inside it is question 5.
- M3.S13.T13.C32 angle_120: the book never asks for a 120° angle as a task ("How do we do it? This can be done if we can construct a 60° angle", with a figure); the plan's example is its own step.
- M4.S19.T19.C55 plane: the book asks "Can you think of a shape whose copies can tile the entire plane?", "Are there other regular polygons ...?" and answers them in a line each; the 360° corner argument is the plan's own explanation.

Other items not moved:

- p137 "Join A and B ... Where does AB intersect XY, and what is the angle formed?": answered in the next sentence; no block.
- p139 "How do we get these different shapes? Try!": open. "Will C and D lie on the perpendicular bisector AB?": answered at once; folded into question 2's reasoning.
- p142 Figure it Out Q2 and p144 Q5 (rope methods): open Math Talk, no single answer.
- p151 "construct a pentagon and hexagon with equal sidelengths" (Try This): open; the book defers the pentagon to later years.
- p154 Figure it Out Q2 (optical illusion): "Do you notice anything interesting ... How does this happen?" discussion.
- p159 "If the plain grid is tileable, is the black-and-white grid tileable?" and the converse (Math Talk): answered in the next line (yes, yes); no block. p160 "Is the black-and-white region in Fig. 6.14 tileable?": answered at once; the plan's colour_613 holds it.
- p162 Escher tilings, bees and wasps, summary, chapter opener, the Śulba-Sūtra history: not questions.

## Gaps (book questions the plan has no block for)

The plan has no coverage ids for any of these, so nothing is invented:

- p140 Figure it Out Q4: recreate the four-petal design with ruler and compass.
- p142 Figure it Out Q1: justify why AB in Fig. 6.4 (the rope construction) is the perpendicular bisector. The plan has no Śulba-Sūtra content.
- p144 Figure it Out Q2: construct the 8-petalled figure of Fig. 6.5 (the plan's bisect_45 block covers only the 45° supporting lines, not the petals).
- p145 "Construct the following figure" (Fig. 6.6) and p147 Figure it Out Q2 "Construct the Fig. 6.6" (same figure).
- p148 Figure it Out Q2: construct the eight-pointed star figure with letters A to Z.
- pp149 to 151, Arch Designs: construct the trefoil arch ("How would you construct these support lines?"), the pointed arch ("What supporting lines will you use?"), and Figure it Out Q1 (pointed arches from the support lines of Fig. 6.11). Q2 "Make your own arch designs" is open.
- p154 "Construct the following 6-pointed star" (the plan's star block answers only the "equilateral? Why?" question).
- pp154 to 155 Figure it Out Q1 (a) to (e) (construct five figures) and Q3 (construct the star in a hexagon).
- p156 Figure it Out: rearrange the seven tangram pieces to form the printed figures.

The existing angle-bisection Figure it Out concepts are numbered Q1, Q3, Q4, Q6 and the copy, parallel and special-angle
ones Q1, Q1 and Q4 because the live plan holds only those; the missing numbers are the gaps above.

## Judgement calls

1. The counting rule above (task or concrete question addressed to the reader versus a lead-in the book answers itself)
   is mine; the "?" icon is on every question here. To promote one of the eight left-behind blocks, add a `new` entry for
   its block with a fresh ref; to drop one of the 21, delete its entry (questions 3 and 4 are the closest calls: the
   book shows its method right after the task).
2. `rename_teach` is empty. No kept concept name carries a page number or a book-exercise number (the Figure it Out
   names hold only the book's own question number, "Q1" to "Q6", which the structure gate accepts); structure
   problems are 0 before and after. The new names are `<Topic short>: <subject>` with no page, "NCERT", "textbook" or
   "Fig.".
3. Question 10 folds two plan ids into one printed question (`canon`: 6.1.angle_15 into 6.1.angle_30). Its kept video
   is C37's, which covers 15° only, so the report marks it "refresh".
4. Question 11 keeps only what the plan block answers (are the point triangles equilateral). Its name says so; the star's
   construction is a Gap.
5. Question 20's block question says "Colour it like a chessboard with white corners", which is the plan's own method
   wording; the book asks "Were you able to tile this? How can we be sure that this is not tileable?" The question card
   would show the method, so trim the block's question when the solutions are authored. Questions 15 to 17 also carry
   the plan's "Give a strategy" wording.
6. Question 12: the book's printed tiling mixes horizontal and vertical tiles, the plan's uses 12 vertical tiles; both
   answer "show one way", so the solution figure follows the plan.
7. All 21 new questions are `prompt` because the book prints no "Example" label in this chapter. The 12 kept Figure it
   Out concepts keep their live tier.
8. Figures: `q_figure` is set where the printed question shows or needs a drawing: the segment XY (question 1), the
   angle and ray to copy (4), the fan of angles (5), the hexagon with centre O (6), the star (11), the tiling grids and
   tiles (12, 13, 14, 18 to 21), the angle-bisection figures (Q3, Q6), the angles of copying Q1, the L-tile region and the
   8 × 8 board. Where the reader draws everything (3, 7, 8, 9, 10, 15, 16, and the kept construction items), only
   `s_figure` is set, since the solution card is the construction. The live Figure it Out concepts had no figures; I added
   them only where the book prints one or the solution is a drawing. No figure at all: question 17 (both odd) and angle
   bisection Q4. The `s_figure` of question 19 is the plan's own tiling, which the book does not draw.
9. After the cuts, 14 teaching concepts keep their text, teaching plan and own video but lose their worked example (C3,
   C5, C12, C21, C28, C29, C31, C36, C38, C41, C43, C44, C48, C50), and C32 loses two refs (hex_4cm and hex_5cm moved with
   their thin-extra concepts). Their live videos stay attached to them. The eight teaching concepts listed under
   Borderline keep their worked example.
