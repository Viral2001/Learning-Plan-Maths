# Class 6 Ch 8 Playing with Constructions (cbse_eng_maths6_ch8, live v44): question layout notes

Spec: `layout_spec.json`. Result of `check`: 41 question concepts in 14 Questions topics (23 existing kept in book order + 18 new: 4 example, 5 exercise, 9 prompt), 13 new videos needed, 5 live videos kept (one of them, the XY table, covers only part of its question), no video folded away, gates identical to live (video_script_rules 68, skeleton 8, both before and after), INTEGRITY clean.

Layout: one Questions topic is new (after "How Far Apart Can Two Points Be?"); the other 13 already existed and keep all their concepts. "Constructing a Square" (M2.S12.T12) and "Diagonals of a Rectangle" (M3.S20.T20) have no Questions topic: nothing in them is a counted book question.

## How a book question was recognised here

The book marks its own questions with a round blue icon (checked on the PDF, pages 187 to 216): it sits on every Figure it Out and Construct heading and on the Think, Explore and "Which of the following is not a name" items, and the "Try This" tag is on Construct 3 (8.3), Figure it Out Q3 (8.1) and Construct 6 (8.4). The book also prints answers for these in its solutions section, and it calls its "Construct ... Solution" items "solved examples" (page 212 says "the second solved example of the previous section"). I counted:

- the icon-marked items that the plan has a block for, whose answer is definite (those in the book's solutions section);
- the "Construct ... Solution" items (tier example);
- the Construct list items of 8.1, 8.3 and 8.4 (tier exercise), named in the chapter's existing style "Construct n: <subject> (section 8.x)".

The in-text sentences with no icon that the book answers in the next line or figure, the why-questions, the discussions and the "predict, then measure" experiments are not counted (see Borderline). The plan tags all of them as worked examples with ids like 8.4.q2, so the ids say nothing about whether the book treats an item as a question.

## New questions

Plan source is `concept block` (b2 = the teaching concept's worked-example block, cut out) or `concept, whole` (a thin-extra concept moved with its video).

| # | New question concept | Book label or quote | Plan source (ref) | Tier | Why it counts |
|---|---|---|---|---|---|
| 1 | Think (section 8.1): all points 4 cm from P | p188 "Think: Imagine marking all the points of 4 cm distance from the point P. How would they look?" | M1.S2.T2.C4, whole (8.1.q3); video kept | prompt | Icon-marked Think; book answer in its solutions (a circle). Goes before the Activity, as printed. |
| 2 | Construct 2: Wavy Wave (section 8.1) | p191 "2. Wavy Wave. Construct this." (central line AB = 8 cm) | M1.S4.T4.C9 b2 (8.1.ex2); new video | exercise | Item of the icon-marked Construct list; the plan block uses the book's AB = 8 cm. Goes before Figure it Out Q1 and Q2, which are about the same wave. |
| 3 | Construct 1: A Person (section 8.1) | p190 "1. A Person. How will you draw this?" | M1.S6.T6.C13 b2 (8.1.ex1); new video | exercise | Same Construct list. Placed before Figure it Out Q3 (p191) and Eyes, the printed order. |
| 4 | Construct 3: Eyes (section 8.1) | p192 "3. Eyes. How do you draw these eyes with a compass?" | M1.S6.T6.C14 b2 (8.1.ex3); new video | exercise | Same Construct list. |
| 5 | Naming by Corners: which is not a name | p193 "Which of the following is not a name for this square? 1. PQSR 2. SPQR 3. RSPQ 4. QRSP" | M2.S8.T8.C19, whole (8.2.q3); video kept | prompt | Icon-marked; answer PQSR in the book's solutions, same in the plan. Before Figure it Out Q2. |
| 6 | Think (section 8.2): sides and angles from dots | p194 inside Figure it Out Q2: "Think: Is it possible to reason out if the sides are equal or not, and if the angles are right or not without using any measuring instruments ... by only looking at the position of corners in the dot grid?" | M2.S10.T10.C23 b2 (8.2.q5); new video | prompt | Icon-marked Think; answer "Yes" in the book's solutions. See judgement call 4. |
| 7 | Construct Q3 (section 8.3) | p197 Construct 3 (Try This): "Is it possible to construct a 4-sided figure in which all the angles are equal to 90 degrees but opposite sides are not equal?" | M2.S13.T13.C31 b2 (8.3.q3); new video | exercise | Third item of the Construct list whose Q1 and Q2 are already kept; answer No in the solutions. Named like them. |
| 8 | Rectangle Exploration: table of XY lengths | p198 "When X is 5 mm away from A and Y is 3 cm away from B, XY = __ cm __ mm ..." and "Is there a shorthand way of writing it down? ... a table" | M2.S15.T15.C38 b2 (8.4.q3) + C39, whole (8.4.q4); video of C39 kept | prompt | Icon-marked; the book's solutions answer it with one table (7.4, 7, 7.3 cm), which is the answer to the three sentences too, so one question; ids folded. |
| 9 | Rectangle Exploration: XY at equal distances | p199 "Have you checked what happens to the length XY when X and Y are placed at the same distance away from A and B ... table" | M2.S15.T15.C40 b2 (8.4.q5); new video | prompt | Icon-marked; table answer in the solutions (7 cm each). |
| 10 | Rectangle Exploration: XY and the shape ABYX | p199 "In each of these cases, observe 1. how the length XY compares to that of AB and 2. the shape of the 4-sided figure ABYX." | M2.S15.T15.C41, whole (8.4.q6); video kept | prompt | Icon-marked; solutions: XY = AB, ABYX is a rectangle. |
| 11 | Rectangle Exploration: the farthest distance | p199 "How does the farthest distance between X and Y compare with the length of AC? BD?" | M2.S15.T15.C42, whole (8.4.q7); video kept | prompt | Icon-marked; solutions: equal to AC or BD. |
| 12 | Example 1: Breaking Rectangles into squares | p199 Construct "Breaking Rectangles: Construct a rectangle that can be divided into 3 identical squares", with its "Solution", the Explore on two identical squares (AF = 4 cm, AC?) and p201 "With this idea, try constructing a rectangle that can be divided into three identical squares" | M2.S16.T16.C45 b2 (8.4.ex2) then C44 b2 (8.4.ex3); new video | example | A printed Construct with a Solution, so tier example; the two-squares step is part of its solution, so one question, ids folded into 8.4.ex2. The solutions section answers it ("length three times its breadth"). |
| 13 | Breaking Rectangles: sides that cannot be split | p201 "Give the lengths of the sides of a rectangle that cannot be divided into two identical squares; three identical squares." | M2.S16.T16.C46 b2 (8.4.q8); new video | prompt | Icon-marked; solutions give 4 cm by 2.5 cm and 7 cm by 2 cm, as the plan does. |
| 14 | Construct 4: Square with a Hole (section 8.4) | p203 "4. Square with a Hole" (circular hole at the centre of the square) | M2.S18.T18.C49 b2 (8.4.ex7); new video | exercise | The missing number in the Construct list of 8.4: Constructs 1, 2, 3, 5, 6 are existing concepts. Answer in the solutions (the meeting point of the diagonals). Goes between Construct 3 and 5. |
| 15 | Explore (section 8.5): diagonal splitting a corner equally | p204 "Explore: How should the rectangle be constructed so that the diagonal divides the opposite angles into equal parts?" | M3.S21.T21.C59 b2 (8.5.q4); new video | prompt | Icon-marked; solutions: the adjacent sides equal, a square. Before the two existing Math Talk concepts, as printed. |
| 16 | Example 2: Rectangle with a 60° and 30° diagonal | p205 Construct 1 "Construct a rectangle in which one of the diagonals divides the opposite angles into 60 and 30 degrees", with "Solution" | M3.S23.T23.C64 b2 (8.5.ex1); new video | example | Printed solved example (Solution, Steps 1 to 4, two methods). Before the exercise Q1 and Q2. |
| 17 | Example 3: Rectangle from a side and a diagonal | p208 Construct 2 "Construct a rectangle where one of its sides is 5 cm and the length of a diagonal is 7 cm", with "Solution" | M3.S25.T25.C69 b2 (8.5.ex2); new video | example | Printed solved example. Before the exercise Q3 and Q4. |
| 18 | Example 4: Recreating the house figure | p211 "House: Recreate this figure ... Solution" (all border lines 5 cm) | M4.S27.T27.C79 b2 (8.6.ex1); new video | example | Printed solved example. Named differently from the teaching concept "Building the house", so the subject is not given twice. |

Placement: in-text and Construct items go where the book prints them relative to the section's Figure it Out and Construct exercise items. The existing 23 are all listed with `keep`, in book order.

## Borderline, not moved

- 8.1.q1 (C2 b2) draw the five artwork pictures freehand: open drawing, no answer; its compass version is the existing Activity (C8).
- 8.1.q2 (C3 b2) "Mark a point P ... as many points as possible 4 cm away": hands-on, result differs for every student; it sets up the Think (row 1).
- 8.1.q4 (C5 b2) "How can this be done?" and the icon "Now, try to get the full curve": the book explains the method and answers "It is a circle!" in the next lines.
- 8.1.q5 (C6, thin-extra, own video) "Take a point on the circle. Is its distance from P equal to, less than or greater than 4 cm?": no icon, not in the solutions, answered by the definition of radius that follows. The nearest candidate to promote: move whole, video kept.
- 8.2.q1 (C17 b2) "What makes them squares and rectangles?", 8.2.q2 (C18 b2) "Can you see what names are allowed?", 8.2.q4 (C22 b2) "Is it still a square?" (answered "Yes" in the same lines): narration and discussion.
- 8.3.ex1 (C27 b2) "How would you construct a square with a side of 6 cm?": guided construction in the running text, no icon, not in the solutions, no "Solution" label. The strongest candidate to promote as an example if wanted; its block stays in the teaching concept.
- 8.3.q1 (C28 b2) "Can you see why PS should be 6 cm long?" (a why-question) and 8.3.q2 (C29, thin-extra) "How long is the side RS and what are the measures of angle R and angle S?" (the next figure, Step 6, shows 6 cm, 90, 90): narration.
- 8.4.ex1 (C35 b2) "Construct a rectangle ABCD with AB = 7 cm and BC = 4 cm": set-up for the exploration, no icon.
- 8.4.q1 (C36, thin-extra) closest and farthest positions: Math Talk, "What does your intuition say? Discuss with your classmates."
- 8.4.q2 (C37, thin-extra) "How does the minimum distance between the points X and Y compare to the length of AB?": no icon, not in the solutions, a measurement step of the same investigation; candidate to promote (video kept).
- 8.5.q1 (C55 b2) compare the diagonals, 8.5.q2 (C56 b2) are g and h, c and d equal, 8.5.q3 (C57, thin-extra) which of the eight angles are equal, 8.5.q7 (C60 b2) the square case ("See what happens"): predict-then-measure investigations, no icon, not in the solutions, "what do you observe" in nature. This is why "Diagonals of a Rectangle" has no Questions topic.
- 8.5.q5 and 8.5.q6, the two Math Talk items (C62, C63): discussion. They are existing question concepts, so the engine keeps them (listed with `keep` after the Explore).
- Steps inside the solved examples: 8.5.q8 (C65, thin-extra) "Check what the other angle is" (Example 2), 8.5.q9 (C70) "which line can be drawn first?", 8.5.q10 (C71 b2, icon, answered in the next line), 8.5.q11 (C72), 8.5.q12 (C73 b2) "Check if ABCD is a rectangle" (Example 3), 8.6.q1 (C77 b2) and 8.6.q2 (C78, Think answered inline) (Example 4). They are narration inside a worked solution. Their concepts and videos stay in the teaching topics.
- Hints A and B (Eyes, rhombus), "Make other artwork of your choice", the Summary: not questions.

## Gaps (book questions the plan has no content for)

None among the counted questions. "Make other artwork of your choice with a ruler and a compass" (p192) and the 8.5 recording table "Sides A B C D E F G H" (p204) have no block, and are open activities in any case.

## Judgement calls

1. The icon criterion (above) decides which in-text items count. It is stricter than the brief's wording ("how many ...? put straight to the reader and having a definite answer"): several unmarked in-text questions of this chapter have definite answers but are answered by the book in the next sentence or figure. The promote candidates are 8.1.q5 (C6), 8.3.ex1 (C27 b2), 8.4.q2 (C37) and 8.5.q1 to q3. Promoting one is a one-entry change; the thin-extra ones keep their videos.
2. The Construct items of 8.1 (A Person, Wavy Wave, Eyes) are counted as exercises although the book does not solve them: they head an icon-marked Construct list like those of 8.3 and 8.4, and 8.6 Construct Q2 asks for them again. The plan's blocks are open ended ("Open ended" answers, steps given).
3. The four solved examples are unnumbered in the book (8.5 numbers them "Construct 1" and "Construct 2", which would clash with the existing "Construct Q1 to Q4 (section 8.5)"), so they are named Example 1 to 4 in chapter order.
4. The Think of 8.2 is printed inside Figure it Out Q2, but the plan keeps Q2 in the Questions topic of "What Makes a Square or a Rectangle" and the dot-grid teaching one topic later. I made the Think its own prompt in the Questions topic of "Rotated Squares and Rectangles", between Figure it Out Q1 and Q3 (book order Q1, Q2 with its Think, Q3). Folding it into Q2 would pull a block from the later topic into the earlier one.
5. Two printed questions are built from two blocks each: Breaking Rectangles (three-squares block first, because that is the question the card shows, then the two-squares step) and the XY table (the three sentences and the shorthand table). `canon` folds 8.4.ex3 into 8.4.ex2 and 8.4.q3 into 8.4.q4. The XY table keeps the video of C39, which covers only the table part (the report says refresh).
6. `rename_teach` is empty: no teaching concept is named after a moved example. After the cuts, 15 teaching concepts keep their text, teaching plan and own video but no worked-example block; their refs for the moved items are removed by the engine.
7. Figures: `q_figure` is set where the printed question shows a picture (the artwork, the wave, the person, the eyes, the dot-grid collection, the rectangle with X and Y, the squares, the house), `s_figure` where the solution is a drawing or table. They were also added to the existing Figure it Out and Construct concepts, which have none in the live plan; text-only items have none. Descriptions follow the PDF pages. The compass-tip points for Construct 6 (curves) follow the plan's answer.
8. The live plan answers match the book's solutions everywhere checked (PQSR, A is a square, No, the 7.4 / 7 / 7.3 cm table, 4 by 2.5 and 7 by 2, the diagonals' meeting point, a square). Nothing was left out for a contradiction.
