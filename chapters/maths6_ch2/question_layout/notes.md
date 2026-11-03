# Class 6 Ch 2 Lines and Angles (cbse_eng_maths6_ch2, live v53): question layout notes

Spec: `layout_spec.json`. Result of `check`: 67 question concepts in 12 Questions topics (50 existing kept in book order
+ 17 new: 1 example, 0 exercise, 16 prompt), 2 of the 12 Questions topics are new (after "Degrees: Measuring a Turn" and
"Make Your Own Protractor"), 9 new videos needed, 8 live videos kept (2 of them cover only part of their question),
gates identical to live (video_script_rules 98 and skeleton 6 before and after), INTEGRITY clean.

## How a book question was recognised here

The book marks its own in-text questions with the round icon that is also printed on every "Figure it Out" heading
(checked on the PDF: book pages 18, 21, 23, 28, 29, 33, 34, 36, 40, 48 and 53 carry it beside a question), and its
solutions section answers most of them. Counted: (1) icon-marked items that have a definite answer and a plan block;
(2) prompts that the book leaves for the reader (a blank, a reading, a measure) with a definite answer and a plan block,
even without the icon. Not counted: items with no icon whose answer the book gives in the next sentence, open
discussion, hands-on activities whose result differs per student, and games with no single answer. The plan tags every
one of these as a worked example with an id like 2.9.q4, so the ids say nothing about whether the book treats the
item as a question. Plan-authored examples with their own numbers (C6 torch beam, C86 clock at 5 o'clock, C100 name each
angle, C101 reflex of 100 degrees) stay in their teaching concepts.

## New questions

`C<n>` is the live concept id in its topic (b2 = the worked-example block, "whole" = the thin-extra concept moved with its video).

| # | New question concept | Book label or quote | Plan source (ref) | Tier | Why it counts |
|---|---|---|---|---|---|
| 1 | Angle: arms and vertex in six cases | p18 "Do you see angles being made in each of these cases? Can you mark their arms and vertex?" (Vidya, Case 1 to 6) | M1.S5.T5.C14 b2 (2.5.q1); new video | prompt | Icon-marked. Arms are the cover and the rest of the book, vertex is the hinge. Placed before the section's Figure it Out. |
| 2 | Comparing Angles: is it always easy? | p21 "Is it always easy to compare two angles?" with the four angles drawn below | M2.S7.T7.C31 b2 (2.6.q2); new video | prompt | Icon-marked; the book's solutions answer it (No, 89 and 91 degrees cannot be told apart by eye, the given figures can). |
| 3 | Comparing Angles: other uses of superimposition | p23 "Where else do we use superimposition to compare?" | M2.S7.T7.C30 whole (2.6.q5); video kept | prompt | Icon-marked; the solutions give line segments, squares, circles. See judgement call 3. |
| 4 | Straight Angle: splitting it into two equal angles | p28 "Is it possible to draw OC such that the two angles are equal to each other in size?" and the Let's Explore fold "How can it be done?" | M2.S10.T10.C42 b2 (2.8.q1) + C43 whole (2.8.q2, folded by canon); C43 video kept, covers only the folding | prompt | Icon-marked; the solutions answer it (yes, fold OB onto OA). The fold is the method for the same problem, so one question. |
| 5 | Right Angle: what part of a full turn | p29 "If a straight angle is formed by half of a full turn, how much of a full turn will form a right angle?" | M2.S10.T10.C45 b2 (2.8.q4); new video | prompt | Icon-marked; the solutions answer 1/4. |
| 6 | Degrees: a straight angle and a right angle | p33 "What is the measure of a straight angle in degrees? ... of a right angle in degrees?" | M3.S14.T14.C57 b2 (2.9.q1); new video | prompt | Icon-marked; definite answers 180 and 90. The Questions topic after "Degrees: Measuring a Turn" is new. |
| 7 | Degrees: a circle cut into equal parts | p34 "The circle has been divided into 1, 2, 3, 4, 5, 6, 8, 9, 10 and 12 parts below. What are the degree measures of the resulting angles?" | M3.S14.T14.C58 b2 (2.9.q2); new video | prompt | Icon-marked; ten definite answers (360 divided by the number of parts), left to the reader by the book. |
| 8 | Protractor: naming and measuring every angle | p36 "Name the different angles in the figure and write their measures." and p37 "Did you include angles such as ∠TOQ? ... What is the measure of ∠TOS?" | M3.S15.T15.C61 b2 (2.9.q4) + C62 whole (2.9.q5, folded by canon); C62 video kept, covers only the follow-up | prompt | Icon-marked; the solutions list 14 angles with their measures. The follow-up is on the same figure. |
| 9 | Protractor: the angle between two readings | p37 "OT and OS pass through the numbers 20 and 55 on the outer scale. How many units of 1 degree are contained between these two arms? Can subtraction be used here?" | M3.S15.T15.C63 whole (2.9.q6); video kept | prompt | No icon, but put to the reader with the book's own numbers and a definite answer (35 degrees, equal to ∠SOT in the book's list). |
| 10 | Protractor: reading the angle AOB directly | p37 "What is the degree measure of ∠AOB?" (ray OB on the 0 mark) | M3.S15.T15.C64 b2 (2.9.q7); new video | prompt | No icon; a measurement with a definite answer. Checked on the PDF figure: OA passes through 80 from the arm on 0, as the plan says. |
| 11 | Paper Protractor: half a circle | p38 step 2 "the measure of half a turn = 1/2 of ____ = 180°" | M3.S17.T17.C68 whole (2.9.q8); video kept | prompt | A blank to fill (360). Moves with its video. The Questions topic after "Make Your Own Protractor" is new. |
| 12 | Paper Protractor: a quarter circle | p38 step 3 "1/4 of 360° = ______. Or 1/2 of 180° = ______" | M3.S17.T17.C69 whole (2.9.q9); video kept | prompt | Two blanks, both 90. |
| 13 | Paper Protractor: the 45° fold | p39 step 4 "1/8 of 360°, or 1/4 of 180° or 1/2 of 90° = ________" | M3.S17.T17.C70 b2 (2.9.q10); new video | prompt | A blank to fill (45); the plan block holds the question, steps and answer. |
| 14 | Paper Protractor: the next half fold | p39 step 5 "Continuing with another half fold as shown in Fig. 2.18, we get an angle of measure ____" | M3.S17.T17.C71 whole (2.9.q11); video kept | prompt | A blank to fill (22.5). |
| 15 | Paper Protractor: eight equal angles | p40 Think! "∠AOB = ∠BOC = ... = ∠HOI = _____. Why?" | M3.S17.T17.C72 whole (2.9.q12); video kept | prompt | Icon-marked and answered in the solutions (22.5 degrees, 180 divided by 8). |
| 16 | Example 1: Draw a 30° angle ∠TIN | p46 to 47 "Vidya wants to draw a 30° angle and name it ∠TIN using a protractor", Step 1 to Step 4 | M4.S22.T22.C93 b2 (2.10.ex1); new video | example | The only solved example of the chapter. See judgement call 5. |
| 17 | Types of Angles: finding ∠BET and ∠SET | p53 Let's Explore "In this figure, ∠TER = 80°. What is the measure of ∠BET? ... of ∠SET?" | M4.S24.T24.C102 b2 (2.11.q1); new video | prompt | Icon-marked; the solutions give 100 and 10 degrees. It sits between Figure it Out box 1 and box 2, where the book prints it. |

Placement: new questions go before the section's Figure it Out items, as the book orders them, with two exceptions. In
"Reading a Protractor" the existing Figure it Out Q1 (unlabelled protractor, p35) stays first because the book prints it
before the labelled-protractor questions. The Let's Explore (row 17) sits between the two Figure it Out boxes of 2.11.
All 50 existing Figure it Out concepts are listed with `keep`, in book order.

## Borderline, not moved

- 2.2.q1 "Fold a piece of paper ... Do you see a crease?", 2.2.q2 "What is the shortest route from A to B?", 2.3.q1 "Do you think you can draw a complete picture of a line? No. Why?": no icon, and the book answers each in the same or next sentence (narration).
- 2.5.q2 "Which angle is greater, Case 1 or Case 2?": no icon, answered in the next paragraph. 2.5.q3 compass and 2.5.q4 scissors: no icon, and the sentence itself names the vertex and the blades. 2.5.q5 spectacles, wallet and other objects: a marking activity on pictures. 2.5.q6 "Do you see how these angles are formed by turning one arm ...?": rhetorical. C15 to C17 and C19 stay with their videos.
- 2.6.q1 animals' mouths (mark arms and arrange smallest to largest): picture activity with no printed answer. 2.6.q3 "Label each of the angles. How will you compare them?" (Math Talk): open. 2.6.q4 "∠AOB and ∠XOY, which is greater?": answered in the next paragraph. 2.6.q6 and 2.6.q7 the two cranes: the book prints no answer and the plan gives a method, not which crane (C32 and C33 stay).
- 2.7.q1 make rotating arms and arrange them, 2.7.q2 the slit (the book answers it in the next paragraph), 2.7.q3 comic "Challenge: Reduce this angle" (the comic answers it): hands-on or narration.
- 2.8.q3 "Justify why the two angles are equal. Is there a way to superimpose and check?" (Math Talk): discussion, C44 stays with its video. 2.8.q5 "What could be the common feature of the other two groups?": answered in the next paragraph.
- 2.9.q3 "Why does it include two sets of numbers?": open, the plan itself marks it open-ended. 2.9.act1 Make your own protractor: a craft with an open result (its blanks are counted separately, rows 11 to 14). 2.9.try1 "Identify the angle bisectors in your handmade protractor": open. 2.9.MtM Mind the Mistake (six protractor pictures): a discussion task, the book prints no answers and the plan block says "open-ended, no solution printed".
- 2.10 Let's Play a Game #1 and #2 (angle guessing): icon-marked but open games with no single answer (the plan says open-ended); C94 b2 and C95 stay.

## Gaps (book questions the plan has no content for)

None among the counted questions. Two partial cases: the icon question on p33 also asks "What is the measure of a full turn
in degrees?" (answer 360 in the next sentence); the plan block C57 b2 covers only the straight and the right angle. The
Mind the Mistake task (2.9.MtM) has a block but neither the book nor the plan gives the corrections, so it was not
moved and nothing was invented.

## Judgement calls

1. The icon criterion above is stricter than the brief's wording for items answered by the book in the next sentence
   (rows left in Borderline), and looser for rows 9, 10 and 11 to 14, which have no icon but are left to the reader with a
   definite answer, which the brief counts ("a blank to fill", "find ...").
2. The four blanks of the paper-protractor craft (rows 11 to 14) are counted one each, as the plan already has one
   concept per blank. To drop any of them, delete its entry in topic M3.S17.T17: its thin-extra concept then stays in the
   teaching topic with its video, and C70 keeps its block.
3. Row 3 ("Where else do we use superimposition?") has open-ended answers; counted because the icon is on it and the
   book's solutions print a short answer. To drop it, delete its entry in topic M2.S7.T7.
4. Folds: 2.8.q2 (the folding method) is folded into 2.8.q1 and 2.9.q5 (∠TOQ, ∠TOS follow-up) into 2.9.q4 with `canon`.
   2.9.q6 stays a separate question: it has its own numbers and answer. 2.8.q3 (justify) is not folded.
5. Example 1 is not labelled "Example" in the book (it is the Vidya walk-through in 2.10); counted as the only solved
   example. The plan block's question text already contains the four steps, so the question card must stop before them.
   Its teaching concept C93 "Drawing a 30° angle" keeps its name and its text and teaching blocks.
6. `rename_teach` is used on 23 kept Figure it Out concepts (2.4, 2.5, 2.6 and 2.8 sets) only to drop "(page N)", "Fig."
   and the section number from their names. The engine builds the question and solution image titles from the concept
   name, and the structure gate rejects "page N" (0 problems in live, 44 without the renames). The Class 6 Ch 10 spec also
   renames kept question concepts through `rename_teach`. No teaching concept is renamed. The other kept names (Figure it Out after the protractor, after the bisector,
   Where are the angles, box 1) are unchanged.
7. `q_figure` and `s_figure` were added to the kept Figure it Out concepts as well as the new ones, wherever the printed
   question depends on a picture (descriptions taken from the PDF pages). Text-only items (for example the classroom right
   angles, acute and obtuse words, draw M and Y, the puzzle) have none.
8. After a block is cut, teaching concepts C14, C31, C42, C45, C57, C58, C61, C64, C70, C93 and C102 keep their text,
   teaching plan and own video. C29 and C67 lose only concept-level refs that point at a question moved whole (2.6.q5, 2.9.q8 and q9). New videos needed (rows 1, 2, 5, 6, 7, 10, 13, 16, 17); C43's video covers only the fold of row 4 and C62's
   only the follow-up of row 8, so both are flagged "refresh".
