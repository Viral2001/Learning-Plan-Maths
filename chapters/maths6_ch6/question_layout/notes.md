# Class 6 Ch 6 "Perimeter and Area" (cbse_eng_maths6_ch6, live v56): question layout notes

Spec: `layout_spec.json` (checked with `core/question_layout_live.py`, the version with `split`). Media links of the live plan are
sound (the check of an empty spec is `INTEGRITY: clean`), so nothing blocks the layout.

Result of `check`: 41 question concepts in 9 Questions topics. They are 13 existing concepts kept (10 listed with `keep`, 3 in the
Summary's Questions topic left untouched), 6 parts from 3 `split`s, and 22 questions cut out of teaching concepts. The 28 new
ones are 4 example, 12 exercise, 12 prompt. 25 new videos are needed (22 cut + 3 split parts); 3 live videos are kept
but each now covers only half of its old concept ("refresh"). No gate is worse than live (skeleton 11, objectives 18, video_script_rules 38 unchanged; coverage 16 down to 0), `INTEGRITY: clean`, no `GATES WORSE THAN LIVE`.

## How a book question was recognised here

In this edition the book marks its own questions with a swirl icon (printed before every "Figure it Out", "Deep Dive", "Estimate and Verify",
"Let's Explore" item and before several in-text questions, checked on the PDF), and it labels solved items "Example:". Counted: printed
Examples, Figure it Out items, and icon-marked in-text questions that have one definite answer and a plan block holding question,
steps and answer. The unlabelled "Consider a rectangle ABCD ... what is its perimeter?" style items of 6.1 are narrated derivations that the book
answers in the next line; they stay in the teaching concepts.

## Placement

* The live plan has no Questions topic after "Walking the Boundary" or after "Same Area, Different Boundary". A new Questions topic would be built
  from this chapter's template (typed "instructional", no topic objective) and adds 2 skeleton and 2 objectives problems, so none is created. The two
  printed Examples of 6.1 go first in "Questions: Perimeter Puzzles" (the book prints them straight before that Figure it Out); the three
  "Same Area" questions go in "Questions: Half of a Rectangle", in the book's page order (p13-14 Let's Explore, p14-16 triangles, p17-18 nine squares).
* `split` replaces a concept in place, so a split part cannot be interleaved with a neighbouring concept. Result: in "Questions: Perimeter Puzzles" Figure it Out Q3 comes before Q2
  and Q5 before Q4; in "Questions: Covering a Region" Q3 comes before Q2. Everything else is in book order.

## New questions cut out of teaching concepts (22)

Plan source is `concept block` (b2 etc. as in `brief.md`). All have `keep_video_of: null` (new video needed).

| # | New question concept | Book label or quote | Plan source (ref) | Tier | Why it counts |
|---|---|---|---|---|---|
| 1 | Example 1: Lace round a tablecloth | p131 "Example: Akshi wants to put lace all around a rectangular tablecloth 3 m long and 2 m wide" | M1.S2.T2.C6 b0 (p3.lace) | example | Printed Example. It is the only block of C6, which is left empty (judgement call 2). |
| 2 | Example 2: Usha runs three rounds | p131 "Example: ... Usha ... three rounds of a square park of side 75 m" | M1.S2.T2.C5 b4 (p3.usha) | example | Printed Example. |
| 3 | Which side is missing in the 14 cm rectangle and the 20 cm square? | p132 Figure it Out 1 a, b | M1.S3.T3.C8 b2 (p4.q1ab) | exercise | Parts a, b of Q1; part c is the split part below (judgement call 4). |
| 4 | What is the side of the square bent from the wire? | p132 FiO 2 | M1.S3.T3.C9 b2 (p4.q2) | exercise | Figure it Out item. |
| 5 | How long is each side when 36 cm of string is shaped? | p132 FiO 5 (a square, b triangle, c hexagon) | M1.S3.T3.C9 b3 (p4.q5) | exercise | Figure it Out item, one block for a, b, c. |
| 6 | How far does Akshi run in five rounds? | p133 FiO 1 | M1.S5.T5.C13 b2 (p5.q1) | exercise | Figure it Out item. |
| 7 | How far does Toshi run, and who ran further? | p133 FiO 2 | M1.S5.T5.C13 b3 (p5.q2) | exercise | Figure it Out item. |
| 8 | Where is Akshi after 250 m, 500 m and 1000 m? | p133 FiO 3 a, b, c | M1.S5.T5.C14 b2 (p5.q3abc) | exercise | Parts a to c of Q3; d to f are the kept "Where is Toshi after each distance?" (judgement call 4). |
| 9 | Is the perimeter of the dot grid triangle 9 units? | p134 icon "Akshi says the perimeter of this triangle is 9 units. Toshi says ... more than 9. What do you think?" | M1.S7.T7.C18 b2 (p6.nine_units) | prompt | Book's solutions give the answer (more than 9, a diagonal is longer than a side). |
| 10 | What is the perimeter of any regular polygon? | p136 icon "Find various objects ... that have regular shapes and find their perimeters. Also, generalise ... for other regular polygons" | M1.S7.T7.C19 b4 (p8.regular) | prompt | Book's solutions give the rule (number of sides times a side). The "find objects around you" part is an activity; counted for the rule. |
| 11 | Can you join the two pieces to make a perimeter of 22 cm? | p136 icon "Arrange the two pieces to form a figure with a perimeter of 22 cm" | M1.S9.T9.C22 b3 (p8.make22) | prompt | One definite answer (join along 5 cm). Follows the kept "find each new perimeter" item, as in the book. |
| 12 | Example 3: A carpet on a floor | p137 "Example: A floor is 5 m long and 4 m wide. A square carpet of sides 3 m ..." | M2.S11.T11.C26 b2 (p9.carpet) | example | Printed Example. |
| 13 | Example 4: Flower beds in the corners | p137-138 "Example: Four square flower beds each of side 4 m ... 12 m long and 10 m wide" | M2.S11.T11.C26 b3 (p10.beds) | example | Printed Example. |
| 14 | Which rectangle of a given area has the greatest perimeter? | p141-142 Let's Explore: rectangles of area 24 (a greatest, b least perimeter), c "area 32 sq cm ... Given any area, is it possible to predict ... ?" | M2.S15.T15.C35 b2 + b3 + b4 (p13.rect24, p14.rect32, p14.predict) | prompt | One printed question with parts a, b, c, so three blocks and one ref (canon). Definite answers (50 and 20; 66 and 24; longest thin and nearest square). Math Talk icon beside it does not disqualify it. |
| 15 | Do the two triangles from a diagonal cut have the same area? | p142 icon "Check! whether the two triangles overlap each other exactly. Do they have the same area?" | M2.S16.T16.C38 b2 (p14.diagonal) | prompt | Same result for every rectangle (yes, each is half). |
| 16 | Is the blue rectangle bigger than the yellow triangle? | p142 icon "Is the area of the blue rectangle more or less than the yellow triangle? ... Write the relationship" | M2.S16.T16.C38 b3 (p14.yellow) | prompt | Definite answer (equal areas). |
| 17 | What are the areas of the blue and red triangles on the grid? | p143 icon "calculate the area ... 1. Find the area of blue triangle BAD. 2. ... red triangle ABE." | M2.S16.T16.C39 b2 + b3 (p15.bad, p15.abe) | prompt | One printed question, two parts; ids folded. |
| 18 | Which perimeters can nine unit squares make? | p145 icon "Using 9 unit squares, solve the following. 1 smallest 2 largest 3 make 18 4 other shapes" | M2.S15.T15.C36 b2-b5 (p17.smallest, largest, make18, other_shapes) | prompt | The book's solutions print it as one question with four numbered answers (12, 20, a figure, "yes except 12"); item 4 depends on 1 to 3. Ids folded (judgement call 5). |
| 19 | What happens to the perimeter when a square is added? | p145-146 icon "Let's do something tricky ... a perimeter of 24 ... can you place the square so that the perimeter a) increases b) decreases c) stays the same?" | M2.S15.T15.C36 b6 (p18.attach) | prompt | Definite answer (26, 22 or 24 by where it goes). |
| 20 | What are the missing sizes and the area of Charan's house? | p146 icon "house plan of Charan ... a. Find the missing measurements. b. Find out the area of his house." | M2.S18.T18.C42 b2 + b3 (p18.charan, p18.charan_area) | prompt | One printed question with parts a, b. See judgement call 6 (hall). |
| 21 | How do Sharan's house and Charan's house compare? | p147 "What are the dimensions of all the different rooms in Sharan's house? Compare the areas and perimeters of Sharan's house and Charan's house." | M2.S18.T18.C42 b4 (p19.compare) | prompt | Book's solutions give it (equal areas 1,050 sq ft; perimeters 130 ft and 134 ft). Follows the kept Sharan concept. |
| 22 | What is the missing area in the first area maze? | p148 icon "Area Maze Puzzles ... find the missing value" part a | M2.S18.T18.C43 b2 (p20.maze_a) | prompt | Part a of the printed puzzle; b, c, d are the kept "Can you solve the other three mazes?" (judgement call 4). |

## Existing concepts that hold several printed questions (3 splits, 6 parts)

Each part keeps the plan's own question, steps and answer. The first part keeps the live concept's video, images and objective (its video
still covers both questions: refresh); the second part is a new enrichment concept with no video.

| Split concept | Part | Book question | Tier | Video |
|---|---|---|---|---|
| M1.S4.T4.C11 "Two more missing sides..." | Which side is missing in the 12 m rectangle? | p132 FiO 1 c | exercise | kept, refresh |
| | What is the third side of the 55 cm triangle? | p132 FiO 3 | exercise | new |
| M1.S4.T4.C12 "Fence and rope..." | What does it cost to fence the park? | p132 FiO 4 | exercise | kept, refresh |
| | How much rope fences the field three times round? | p132 FiO 6 | exercise | new |
| M2.S12.T12.C28 "Area is given..." | What is the width of the garden? | p138 FiO 1 | exercise | kept, refresh |
| | How many coconut trees fit in the grove? | p138 FiO 3 | exercise | new |

## Kept as they are

Listed with `keep`, in book order, with `q_figure` / `s_figure` added because each printed question depends on a figure (the live concepts have none):
M1.S6.T6.C16 (Toshi's track), C17 (Deep Dive), M1.S8.T8.C21 (four dot-grid shapes), M1.S10.T10.C24 (arrangements b, c, d), M2.S12.T12.C30 (two figures to split),
M2.S14.T14.C34 (four dot-grid areas), M2.S17.T17.C41 (five grid figures), M2.S19.T19.C45 (Sharan's plan), C46 (mazes b, c, d). M2.S12.T12.C29 (tiling cost) is text only.
C45 holds two blocks (a missing sizes, b area) that are one printed question; `canon` folds p19.sharan_area into p19.sharan. The three concepts of
"Questions: Pulling It Together" are not touched (see judgement call 8). New concepts carry figures where the printed question draws one; text-only ones carry none.

## Borderline, not moved

- p129-130 rectangle ABCD (p1.rectangle), p130 Debojeet's square frame (p2.square), p131 triangle 4, 5, 7 (p3.triangle): unlabelled derivations of the perimeter rules, answered in the next line. They stay as the worked examples of C4 and C5.
- p135 "What is a similarity between a square and an equilateral triangle?" (p7.similar): no icon, no book answer, several valid similarities. p7.equilateral is a derivation, and p8.arr_a (p136) is the book's own "for example, arrangement a has a perimeter of 28 cm". All three stay in teaching.
- p137 "Area of a square = ___ , Area of a rectangle = ___" (p9.area_def): recall blanks, a text block with no steps; stays in C25 teaching. p144 "Conclusion ___" (p16.conclusion): a text block with no steps; stays in C39.
- p140 icon "guess which one has the larger area" (p12.guess): the book prints no answer and the plan's answer is "a guess, settled by counting". p141 "Draw a circle of diameter 3 ... estimate the area" (p13.circle): estimation activity, no book answer. p141 Math Talk "Why can't we use circles instead of squares" (p13.why_squares) and "Try using different shapes ... list the points": discussion. All stay in C31 and C32.
- p145 "Observe these two figures. Is there any similarity or difference?" and Charan's "What do you notice?": discussion, no block.

## Gaps (book questions the plan has no content for)

The plan lists these itself as flow gaps (`source_metadata.flow_gaps_against_the_book`):
- p139 tangram Figure it Out, 8 questions (which pieces have the same area, D against C, D or F, F or G, A against G, the big square, the rectangle, the two perimeters).
- p134 "Estimate and Verify" (cut random paper shapes, estimate and measure the boundary).
- p141 Let's Explore 1 and 2: the area of the floor outside the corridor (its figure is not in the plan) and the area of the school playground (needs the child's own surroundings).

## Judgement calls

1. The icon plus a definite answer decides in-text items; the unlabelled narrated derivations of 6.1 are excluded, though the brief's wording ("find ... put to the reader") could stretch to them. To promote p1.rectangle, p2.square or p3.triangle later, add them as new `prompt` entries from C4 b2, C5 b2, C5 b3.
2. Example 1 (lace) is the only block of C6, which carries objective O3 and cannot move whole. Cutting it leaves C6 with no content blocks; its live video (about the lace) stays on it and the new Example 1 has no video. Gates do not mind. I renamed C6 to "Using the perimeter rule: lace for a tablecloth" through `rename_teach` so the example is not named twice. To keep the lace in teaching instead, delete the first entry of topic M1.S3.T3 and the `rename_teach`.
3. No kept concept name carries a page number or a book-exercise number, so no page-free renaming was needed. The new names use the chapter's question style, and "Example N" for the four printed Examples, numbered in chapter order (the book leaves its Examples unnumbered).
4. Three printed questions end up as two concepts each, because the plan itself cut them across a teaching concept and a Questions concept that carries an objective, and the engine cannot join a teaching block to such a concept: FiO p132 Q1 (a, b / c), FiO p133 Q3 (a to c Akshi / d to f Toshi), Area Maze (a / b to d). Each half is a complete answerable question.
5. Multi-part items kept as one concept with one ref: Let's Explore rectangles (a, b, c), nine unit squares (items 1 to 4, one question in the book's solutions: split into four if a video per item is wanted), the two triangles on the grid, Charan's house (a, b), Sharan's house (a, b, the kept C45). `canon`: p14.rect32 and p14.predict into p13.rect24; p17.largest, make18, other_shapes into p17.smallest; p15.abe into p15.bad; p18.charan_area into p18.charan; p19.sharan_area into p19.sharan.
6. Charan's hall: the plan gives 265 sq ft (an L shape, 20 x 12 plus a 5 x 5 strip under the toilet), the printed solution 240. The plan is right against the figure and the book's own total of 1,050 (`source_metadata.solution_notes` says so), so it was moved. Likewise p4.q1c: the plan says 3 m, the printed solution writes 3 cm. If the printed key must win, drop the Charan entry.
7. The three live videos kept on the first split parts cover both of the old concept's questions, so the report marks them "refresh"; the lace video stays on the emptied C6 (judgement call 2).
8. The Summary "The final questions" (C47) holds five Figure it Out items (p149 Q1, Q2, Q3, Q6, Q7) as blocks, and the engine cannot use a Summary topic as a source, so they stay there; "Questions: Pulling It Together" is left as it is (its refs p21.q7 and p21.q6 sit on concepts whose block is another question: live quirk, not touched). p149 Q3 repeats Example 3 (the carpet) with the same numbers.
9. The engine does not rewrite block text: the first block of the three first split parts still begins with the old concept name (for example "Two more missing sides, can you find them?: ..."). Cosmetic.
