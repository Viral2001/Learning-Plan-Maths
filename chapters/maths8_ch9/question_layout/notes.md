# Class 8 Ch 9 "The Baudhāyana-Pythagoras Theorem" (cbse_eng_maths8_ch9, live v52; book text hegp202, printed chapter 2 of Part II): question layout notes

The live plan's concept-to-media links are intact (the repair was done before; `check` reports `INTEGRITY: clean`). Tool: `core/question_layout_live.py`.

Result of `check`: 23 question concepts in 5 Questions topics (11 new + 12 kept); tiers of the new ones: 1 example, 5 exercise, 5 prompt. 11 new videos needed (every new question is cut out by block; nothing can move whole because every concept of this plan carries an objective). Images: 23 question + 28 solution placeholder cards. `INTEGRITY: clean`, gates not worse than live: structure 0, coverage 27 before and 0 after (the engine rebuilds `ncert_coverage`), video_script_rules 76 to 72, skeleton 23 to 23, objectives 100 to 100. No `SPEC PROBLEMS`, no `GATES WORSE THAN LIVE`. No concept ends with an empty `content` list (0 before, 0 after, counted over every concept of the result).

Shape of this plan, which decided most of what follows: every teaching concept has an objective, and most of the worked questions sit in single-block concepts that carry an objective and a video (C4 to C9, C11, C12, C17, C18, C22, C25, C31, C45 to C47, C49 to C52, C54, C55 and so on). They cannot move whole (the engine refuses a concept with an objective) and cutting their only block would leave an empty shell, so they stay (list below). What moves is the worked block of the multi-block teaching concepts and the `exercise` blocks of the "Practice:" concepts.

The Questions topics (typed instructional/exploration, named "Questions: <topic>") exist after T4, T6, T8, T10 and T13. They already hold single-question concepts (existing ones are kept as they are). `split` is not used.

## New questions

Plan source is `live concept id, block index` (b3 = the worked_example block of a teaching concept; b1 = the exercise block of a Practice concept). All have `keep_video_of: null`. Concept ids are the live ids (the engine renumbers them). Book pages are the printed ones.

| Topic | New question | Book label or quote | Plan source | Tier | Why it counts |
|---|---|---|---|---|---|
| The Hidden Length √2 | Hidden Length: the hypotenuse for sides 1 and 1 | p37 "Find the hypotenuse of this isosceles right triangle." (? icon; figure with sides 1, 1, ?) | M2.S4.T4.C20 b3 (ref 2.3.Q_hyp_1_1; hyp_def, REST, fixed_unit stay on the teaching concept) | prompt | "Find ..." put to the reader with a figure, answer √2. Has `q_figure` and `s_figure`. |
| The Hidden Length √2 | Hidden Length: √2 against 1 and 2 | p38 "Is √2 less than or greater than 1? ... Is √2 less than or greater than 2?" | M2.S4.T4.C21 b3 (Q_lt_2 folded into Q_gt_1; Q_value and bounds_def stay) | prompt | two closed questions, answer 1 < √2 < 2. |
| The Hidden Length √2 | Hidden Length: can √2 be a terminating decimal | p38 "Will we ever get a number with a terminating decimal representation whose square is 2?" | M2.S4.T4.C23 b3 (ref 2.3.Q_terminating) | prompt | closed question with a definite answer (no); the plan's block works it through the last digit of the square of 1.414...4. |
| The Hidden Length √2 | Isosceles Right Triangles, Q1 | p39 Figure it Out 1 "Can you arrange these pieces to create a square with double the area of either square?" | M1.S2.T2.C13 b1 (Practice concept of T2; recap, tool and video stay) | exercise | printed exercise; moved into this topic, see Judgement call 3. Has `q_figure` (the two cut squares, pieces 1 to 4) and `s_figure`. |
| The Hidden Length √2 | Isosceles Right Triangles, Q2 | p39 Figure it Out 2 (i) 3, (ii) 4, (iii) 6, (iv) 8, (v) 9 | M2.S4.T4.C26 b1 to b5 (Practice concept; recap, tool and video stay); FiO2ii to FiO2v folded into FiO2i | exercise | printed exercise, five lettered parts of ONE question, so one concept with five blocks. The plan's numbers check (e.g. 4.2² = 17.64, 4.3² = 18.49 for √18). |
| Two Squares Become One | Two Squares: the method on equal squares | p42 "Can you see why the method works in the case where the two squares are the same size? Does it agree with the method we used earlier ...?" (? icon) | M3.S6.T6.C28 b3 (ref 2.4.Q_same_size; equal_recap, Q_different, verse_1_12, method stay; the plan's own 9 and 16 example b4 stays) | prompt | closed question with a definite answer (yes: the hypotenuse is the diagonal, a² + a² = 2a²). Has `s_figure`. |
| Two Squares Become One | Missing Sides and New Squares, Q3 | p47 Figure it Out 3 "construct a square whose area is triple the area of a given square? Five times ...?" | M3.S6.T6.C35 b1 (Practice concept; recap, tool and video stay) | exercise | printed exercise. The plan's constructions (sides a and the diagonal give 3a²; sides a and 2a give 5a²) are right. Has `s_figure`. Placed before the kept end-of-chapter Q7. |
| Baudhāyana Triples | Scaled Triples: is (3k, 4k, 5k) a triple | p48 "Conjecture: (3k, 4k, 5k) is a Baudhāyana triple, where k is any positive integer. Is this true?" | M3.S10.T10.C48 b3 (ref 2.5.conjecture) | prompt | closed question with a definite answer (yes: 9k² + 16k² = 25k²). |
| Baudhāyana Triples | Triples, Q1 | p50 Figure it Out 1 "Find 5 more Baudhāyana triples using this idea." | M3.S10.T10.C56 b1 (Practice concept; recap, tool and video stay) | exercise | printed exercise; the five triples in the plan check (7 24 25, 9 40 41, 11 60 61, 13 84 85, 15 112 113). Placed before the kept Q2 and Q3, which refer to "this method". |
| Right Triangles Hiding Everywhere | Lotus Problem: depth of the lake | p52 the Līlāvatī lotus problem ("Quickly tell the depth of the lake.", ? icon) and its worked solution | M4.S13.T13.C63 b3 (lilavati folded into lotus_solution; intro stays on the teaching concept) | example | the book's one solved application, answer 4 units. Has `q_figure` (the lake and the bent stem) and `s_figure`. |
| Right Triangles Hiding Everywhere | Chapter Exercises, Q3 | p53 Figure it Out 3 "Find the sidelength of a rhombus whose diagonals are of length 24 units and 70 units." | M4.S13.T13.C64 b1 (Practice concept; recap, tool and video stay) | exercise | printed exercise, answer 37 (12² + 35² = 37²). Has `s_figure`. Placed before the kept Q8 (i) and Q9. |

Kept as they are (12, after the new ones of their topic): Isosceles Right Triangles Q3 (T5); Chapter Exercises Q7 (T7); Missing Sides and New Squares Q2, Q4 (i), Chapter Exercises Q2 (a), Q4 (T9, unchanged: see Judgement call 2); Triples Q2, Q3, Chapter Exercises Q5, Q6 (T11); Chapter Exercises Q8 (i), Q9 (T14). Figure sentences were added to kept concepts only where the printed question or its solution needs a drawing (checked against PDF pages 34, 36, 37, 39, 47, 52 and 53): Chapter Exercises Q2 (a) (`q_figure`, the tilted triangle with 7 and 9), Q7 (`s_figure`), Q8 (i) (`q_figure` the dot grid, `s_figure`), Q9 (`s_figure`). No `q_figure` has hint, answer, solution, therefore, since, because, hence, proof or thus.

All nine end-of-chapter Figure it Out items, all four Figure it Out items of 2.4, the three of 2.3 and the three of 2.5 are present in the plan. No `rename_teach`: no teaching concept is named after a moved question.

## Left in teaching: concept topics that have no Questions topic

T2 (Doubling and Halving a Square) and T3 (The Rule c² = 2a²) have no Questions topic in the live plan. The engine builds a new one as a copy of the chapter's first Questions topic (typed instructional, no tool, no objective); `check` printed `GATES WORSE THAN LIVE` for it (each new Questions topic adds 4 skeleton problems, "needs exactly 1 tool", "idea topic is missing its topic_objective", "last concept must be the doer", "last concept's name does not open with practice", plus 1 objectives problem: skeleton 23 to 27 and objectives 100 to 101 for either one). So their questions stay in teaching. T12 (Fermat) holds no book question (its three worked blocks are the plan's own cube checks and the Wiles dates). T15 is the Summary.

Ready to paste into `topics` (each is a new Questions topic: accept +4 skeleton and +1 objectives each, or paste after the engine types the new Questions topic `exercise`).

T2 (three prompts: p33 "Will this new square have double the area of the original square?", p34 "Why does the new dotted square have double the area ...?", p36 "Why is the smaller inside square half the area of the larger square?"; also add to `canon`: `"2.1.east_west": "2.1.Q_why_double", "2.1.two_vs_four": "2.1.Q_why_double"`; the Figure it Out 1 of T2's Practice concept is already in the √2 Questions topic):

`{"teach_topic":"M1.S2.T2","questions":[{"name":"Doubling a Square: doubling the side","tier":"prompt","refs":["2.1.first_guess"],"from":[{"concept":"M1.S2.T2.C3","block":3}],"keep_video_of":null,"q_figure":null,"s_figure":"A square of side 2 units divided into four squares of side 1 unit, beside the original square of side 1 unit."},{"name":"Doubling a Square: why the diagonal square is double","tier":"prompt","refs":["2.1.Q_why_double"],"from":[{"concept":"M1.S2.T2.C5","block":3}],"keep_video_of":null,"q_figure":"A square with its diagonal drawn and, standing on that diagonal, a larger tilted square drawn with dotted sides.","s_figure":"The same figure with the vertical and horizontal sides of the original square extended across the dotted square, cutting it into 4 small triangles and the original square into 2."},{"name":"Halving a Square: why the inside square is half","tier":"prompt","refs":["2.2.Q_why_half"],"from":[{"concept":"M1.S2.T2.C10","block":3}],"keep_video_of":null,"q_figure":"A square with a smaller tilted square drawn inside it, each corner of the tilted square at the middle of a side of the larger square.","s_figure":"The same figure with the east-west and north-south lines through the midpoints drawn, cutting the larger square into 4 small squares, each split by a diagonal of the tilted square."}]}`

T3 (p40 Example 1 and p52 end-of-chapter Q1; Example 2 cannot move, see below):

`{"teach_topic":"M2.S3.T3","questions":[{"name":"Example 1: Equal sides 12","tier":"example","refs":["2.3.Ex1"],"from":[{"concept":"M2.S3.T3.C16","block":3}],"keep_video_of":null,"q_figure":null,"s_figure":null},{"name":"Chapter Exercises, Q1","tier":"exercise","refs":["end.FiO1"],"from":[{"concept":"M2.S3.T3.C19","block":1}],"keep_video_of":null,"q_figure":null,"s_figure":null}]}`

## Left in teaching: two Questions topics are full

The skeleton gate wants 2 to 4 primary concepts in a topic of this type. In the live plan the Questions topics after T4 and T6 hold 1 concept each (already failing), the ones after T8 and T10 hold exactly 4 (passing). This layout takes the topic after T6 to 3 (fixes one failure), the one after T4 to 6 (still failing, no change) and the one after T10 to 6 (one new failure), net 23 to 23. Adding the T8 pair as well would make it 24 (`GATES WORSE THAN LIVE`, checked), so these stay in teaching. To use them instead of the T10 pair, paste this in place of the existing `M3.S8.T8` entry and remove the T10 new questions (or accept 24):

`{"teach_topic":"M3.S8.T8","questions":[{"name":"Using the Theorem: sides 3 cm and 4 cm","tier":"example","refs":["2.4.using_345"],"from":[{"concept":"M3.S8.T8.C37","block":3}],"keep_video_of":null,"q_figure":"A right-angled triangle with the two shorter sides 3 cm and 4 cm and the hypotenuse marked with a question mark.","s_figure":"The same triangle with a square drawn on each of its three sides, of areas 9, 16 and 25 square cm."},{"name":"Missing Sides and New Squares, Q1","tier":"exercise","refs":["2.4.FiO1"],"from":[{"concept":"M3.S8.T8.C39","block":1}],"keep_video_of":null,"q_figure":null,"s_figure":"A right triangle with the two sides at the right angle 5 cm and 12 cm and the hypotenuse 13 cm."},{"keep":"M3.S9.T9.C40"},{"keep":"M3.S9.T9.C41"},{"keep":"M3.S9.T9.C42","q_figure":"A tilted right triangle with the two sides at the right angle labelled 7 and 9 and the third side not labelled."},{"keep":"M3.S9.T9.C43"}]}`

(The first is the p47 worked demonstration "Using Baudhāyana's Theorem": 3 cm and 4 cm give 5 cm, unlabelled in the book but printed worked; the second is p47 Figure it Out 1.) The spec as written already carries this topic's kept entries, with the `q_figure` on Q2 (a).

## Not moved: would leave an empty concept

Each of these is a printed question held by a concept whose only content block is that question, and every one carries an objective and a video. Cutting the block would leave a shell, and the engine refuses to move such a concept whole, so the question stays in its teaching concept. (Those in T2 and T3 would also need the Questions topics above.)

- M1.S2.T2.C8: p34 "Moreover, all these small triangles are congruent to each other. Can you explain why?"
- M1.S2.T2.C9: p34 (Math Talk) "Why should the extension of the vertical and horizontal sides of the original square pass through the vertices of the dotted square?"
- M1.S2.T2.C11: p37 "Why is PQRS a square? Why is its area half that of the original paper?"
- M1.S2.T2.C12: p36 "Will the square having half the sidelength have half the area? Why not? How many such squares will fill the original square?"
- M2.S3.T3.C17: p41 "Use this formula to check your answers in the Figure it Out on page 39."
- M2.S3.T3.C18: p40 to p41 Example 2 (hypotenuse √72).
- M2.S4.T4.C22: p38 "Can we find closer bounds for √2?"
- M2.S4.T4.C25: p39 (Try This) "Can √2 be expressed as a fraction m/n, where m and n are counting numbers?"
- M3.S6.T6.C31: p44 "Explain why all the angles of this new 4-sided figure are right angles and so it is a square."
- M3.S10.T10.C45: p48 "Do you see any pattern among (3, 4, 5), (6, 8, 10), (9, 12, 15) and (12, 16, 20)?"
- M3.S10.T10.C46: p48 "Is (30, 40, 50) a Baudhāyana triple? Is (300, 400, 500)?"
- M3.S10.T10.C47: p48 "List down all the Baudhāyana triples with numbers less than or equal to 20."
- M3.S10.T10.C49: p49 "... is (a/f, b/f, c/f) a Baudhāyana triple? Check this statement for (9, 12, 15). Justify."
- M3.S10.T10.C50: p49 "Generate 5 scaled versions of each of these primitive triples. Are these scaled versions primitive?"
- M3.S10.T10.C51: p49 "Is (5, 12, 13) a primitive Baudhāyana triple? What are the other primitive Baudhāyana triples ...?"
- M3.S10.T10.C52: p49 (Math Talk) "If (a, b, c) is a Baudhāyana triple, then (ka, kb, kc) is also ... Is this statement true?"
- M3.S10.T10.C54 and C55: p50 the two worked cases "25 is an odd square ..." and "9 is an odd square ...".
- M4.S15.T15.C69: p54 (Try This) "Find the Colours!" (and the Summary has no Questions topic).

## Not moved: parts of a printed question whose first part is an existing question concept

Rule: a multi-part question stays ONE concept. In these three the live plan files part (i) or (a) as its own question concept (it keeps that concept's video) and the other parts as `exercise` blocks of the Practice concept, which keeps their video link. The engine can only fold a part into an existing question concept with `whole`, which it refuses for a concept with an objective; cutting that concept's only block instead removes it and its live video (`check` then reports "rendered video urls changed"). The parts stay in the Practice concept, the live shape, not made worse:

- p47 Figure it Out 4 (ii) a = 8, b = 12; (iii) a = 9, c = 15; (iv) a = 7, b = 12; (v) a = 1.5, b = 3.5: M3.S8.T8.C39 b2 to b5, with (i) in M3.S9.T9.C41.
- p52 Figure it Out 2 (b) to (f) (the five other right triangles): M3.S8.T8.C39 b6 to b10, with (a) in M3.S9.T9.C42.
- p53 Figure it Out 8 (ii) "Suppose the grid extends indefinitely ...": M4.S13.T13.C64 b2, with (i) in M4.S14.T14.C65.

## Borderline, not moved

- p33 "How can one construct a square having double the area of a given square?" (M1.S1.T1.C1): in the framing topic, which the engine cannot use as a source; open construction answered by the section. p33 "So how can one make a square that has double the area?" (M1.S2.T2.C4): lead-in, the answer is the Verse 1.9 quote.
- p35 "Doubling a Square Using Paper" (M1.S2.T2.C6, activity) and p36 "Halving a Square Using Paper", "Cut out a square ... make a square whose area is half" (M1.S2.T2.C10 b5, build_it): hands-on paper tasks, no single answer to attempt. p36 "How would you do it?" (halving): open, answered by the next paragraph.
- p35 "Each square has double the area of the previous one, as they are made up of 2, 4, and 8 small triangles" (M1.S2.T2.C7): a statement; the plan's "how many triangles" question is its own.
- p40 "General Solution" (M2.S3.T3.C14 b3, "Show that c² = 2a²"): the book's derivation, no question put to the reader.
- p42 "Why does Baudhāyana's method work?" and p44 "Why?" (M3.S6.T6.C29 b3, ids Q_why_works, Q_why_square): lead-ins; the plan's block asks "why are all four sides equal", which the book states as a fact right after ("As T, U, X and W are all congruent, the sides ... have the same length"). The question the book does ask there, about the angles, is C31 above.
- p44 "Baudhāyana's assertion is now clear" (M3.S6.T6.C30) and p46 "State Baudhāyana's theorem" (C34): statements, no question. p45 "Combining Two Squares Using Paper" (C32 b3): a paper demonstration with a printed result.
- p49 "What is the nth odd number? What is the sum of the first (n − 1) odd numbers?" (M3.S10.T10.C53 b3, plan question "Why is (n − 1)² + (2n − 1) = n²?"): lead-in questions answered in the next line; the plan's question restates the derived identity.
- p48 "Is there an unending sequence of Baudhāyana triples?" (Math Talk, ref Q_unending on M3.S10.T10.C46): open; answered by the (3k, 4k, 5k) work.
- Plan-authored blocks: M3.S6.T6.C28 b4 (areas 9 and 16), M3.S8.T8.C38 b2 to b5, M4.S12.T12.C61 b3 to b5 (cube near misses and the Wiles dates, history), M3.S10.T10.C44 b3 (checks two triples the book prints in its list), M4.S15.T15.C67 b3 (summary match). They use the plan's own numbers or are history, and stay.
- Stub concepts with no worked block (M2.S3.T3.C15, M2.S4.T4.C24, M3.S6.T6.C33, M4.S15.T15.C68, refs thm.*): plan-made theorem prompts, not book questions.

## Gaps (book questions the plan has no content for)

None found among the examples, Figure it Out items and in-text questions: every item listed above has a plan block (single-block or multi-block). The book's "What is the value of √2?" (p38, ref Q_value) is a heading question; the plan answers it through the bounds, closer-bounds and terminating-decimal blocks, so it stays on M2.S4.T4.C21.

## Judgement calls

1. **Substance over icons.** In this edition the ? icon sits beside real questions, lead-ins and demonstrations alike. I moved an item when the reader is asked something closed (a "find", a yes/no, a "show that/why" with one expected explanation) and the plan has a block with that question, steps and answer. Lead-ins whose answer is the next line, activities, statements and the plan's own examples were left (borderline list).
2. **Gate balance and which Questions topics grow.** See "Left in teaching: two Questions topics are full": the T10 pair (the (3k, 4k, 5k) prompt and Triples Q1) uses the one failure the layout can afford, because Triples Q2 and Q3 refer to "this method" and to "the triples generated", which Q1 produces; the T8 pair (3 cm and 4 cm example, Missing Sides Q1) does not depend on its neighbours.
3. **Figure it Out 1 (doubling by cutting along diagonals) is in the √2 Questions topic, not T2's.** The book prints Figure it Out 1, 2 and 3 together on p39 to p40, and the plan names them "Isosceles Right Triangles, Q1/Q2/Q3"; T2 has no Questions topic. Per the brief (another topic's only when the book clearly places it there) it goes with Q2 and Q3.
4. **Multi-part question = one concept.** Figure it Out 2 (i) to (v) has no existing concept, so it is one new concept with five blocks and the ids folded by `canon` (FiO2ii to FiO2v into FiO2i). The three questions whose first part is already an existing concept are left (section above). No `split`: no existing question concept holds several printed questions.
5. **`canon` folds only ids that belong to the moved question:** Q_lt_2 into Q_gt_1, FiO2ii to v into FiO2i, lilavati into lotus_solution. Ids that are teaching text (Q_value, bounds_def, hyp_def, REST, fixed_unit, equal_recap, Q_different, verse_1_12, method, intro) stay on their teaching concept.
6. **Tiers.** Examples are the printed solved examples (the Līlāvatī lotus problem here; Example 1 stays in teaching under T3). "Prompt" is an answerable in-text question. This book labels exercises "Figure it Out" under 2.3 to 2.5 and "Figure it Out" at the end, named "<Topic>, Qn" and "Chapter Exercises, Qn" the way the live question concepts are.
7. **Names.** New prompts and the example are `<Topic short>: <subject>`; exercises follow the plan's own `book_number` ("Isosceles Right Triangles, Q1", "Missing Sides and New Squares, Q3", "Triples, Q1", "Chapter Exercises, Q3"). No name has "page", "Fig.", "NCERT", "textbook" or a dash.
8. **The 11 new questions need new videos.** Their teaching concepts keep their videos (they covered the moved questions as well), so those videos are worth a look when the new ones are made.
