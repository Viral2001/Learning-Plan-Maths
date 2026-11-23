# Agent notes, Class 5 to 8 diagram rollout (raw, per chapter and chunk)

LP text issues and borderline calls exactly as the decision agents wrote them. Per chapter: chapters/maths<C>_ch<N>/v2_diagrams/REPORT.md and map/notes_<chunk>.md.

## LP text issues reported by the agents (not changed: your order covers image placeholders only)

### Class 5 Ch 1, chunk A
- **M1.S6.T6.C13** (question): says "Fill in the token table" but there is no table in the text, and the tokens of Row 2 are not stated (only its number 10,458), although the solution's last step checks "with the tokens". Suggested sentence: "Fill in the token table, one row at a time. Row 1: the tokens are one 10,000, three 10s and three 1s. Row 2: the tokens are one 10,000, four 100s, five 10s and eight 1s. For each row write the number and its digits under TTh, Th, H, T, O." (The new diagram shows the tokens, so the sentence is optional but removes the hidden dependency.)
- **M1.S6.T6.C15** (question): the token counts of (b), (c), (d) are not stated; (a) is. Suggested: "(b) one 10,000, three 1,000s, five 100s and two 10s; (c) two 10,000s; (d) four 10,000s, five 1,000s, eight 100s, six 10s and seven 1s." Same remark about the missing table.
- **M1.S7.T7.C17 / C18 and M1.S9.T9.C22 / C23** (Let Us Do Q2): the book's table starts with two finished example rows, 8,045 = Eight thousand forty-five and 20,869 = Twenty thousand eight hundred sixty-nine, which the LP omits. Suggested: "For example, 8,045 is Eight thousand forty-five and 20,869 is Twenty thousand eight hundred sixty-nine."
- **M1.S11.T11.C31 / C32:** the letter "(i)" is not in math mode while "(h)" is `$(h)$` (question_tex of C31, steps_tex and answer_tex of C32). Suggested: write `$(i)$`.
- **M1.S4.T4.C8** `q_figure` hint says the boxes are "joined by arrows"; the book strip has no arrows (hint only, no effect now).
- **Old image markers:** the `text` field of every solution concept of this chunk (C9, C14, C16, C18, C23, C28, C30; C32 has none mid-text) still carries `[Image: ... solution]` lines in the middle of the steps and `(continued)` at the end, and the plan has old cards C9.IMG1/IMG2, C14.IMG1/IMG2 and so on. All 8 solutions here are none, so these cards and markers must be dropped (builder, `drop_image`); the new tokens are only C13.IMG1, C15.IMG1 (question side) and C34.IMG2.
- No contradiction found between an LP solution and the book; all LP arithmetic (names, sequences, token sums) was recomputed and is right.

### Class 5 Ch 1, chunk B
- **M2.S13.T13.C49 (question) and C50 (solution).** The question says "The following table shows the population of some towns" but the table is only written inline ("Town 1: 65,232, Town 2: ..."); there is no table. Suggested: add a LaTeX table after the question sentence: columns Town, Population; rows Town 1 65,232; Town 2 53,231; Town 3 56,380; Town 4 51,336; Town 5 45,858; Town 6 66,540. In the solution, an ordered table or the existing sentence is fine.
- **M2.S17.T17.C68 (solution, step (a)).** The book's note "3 Tens is 30, 90 Tens in 900, and 700 Tens in 7000" is not in the LP. Suggested sentence for step (a): "793 Tens is 700 Tens + 90 Tens + 3 Tens, which is 7,000 + 900 + 30 = 7,930, so 793 notes of ₹10 make ₹7,930."
- **M2.S17.T17.C62, C64, C68, step 1.** The text "(a): is done: ..." reads awkwardly. Suggested: "(a) is already done for you: ...". Same in C64 step 1 ("(a): is done: 90 Tens is 900 ...") and C68 step 1.
- **Numbering.** Concept names restart at "Let us do: Q1 / Ans1" in T13, T15 and T17, but the book numbers are different (T13: book Q3, Q4 of the first set and Q1 to Q6 of the second set; T17: book Q7, Q8, Q9). The `book_number` field carries the right numbers; the names only matter if learners see them.
- **M2.S13.T13.C37 (question).** The text says "the numbers below" and "the number line below"; both exist only in the figure (the number line) or the text (the numbers). Nothing to change if the diagram is built; if it were dropped, the scale 0 to 80,000 would have to be written in the text.

### Class 5 Ch 1, chunk C
(Nothing was edited and no decision was changed because of these.)

- **M2.S20.T20.C81**: the question text says "Fill in the boxes appropriately" but carries no table, so there are no boxes to fill. Suggested: add a LaTeX array to the question text, header `Number | Nearest Tens | Nearest Hundreds | Nearest Thousands`, rows 3,176; 4,017; 5,789; 8,203, three blank cells each.
- **M2.S20.T20.C82**: the answer is one run of text (12 numbers). Suggested: show it as the same LaTeX array filled in (3,176: 3,180 / 3,200 / 3,000; 4,017: 4,020 / 4,000 / 4,000; 5,789: 5,790 / 5,800 / 6,000; 8,203: 8,200 / 8,200 / 8,000).
- **M2.S19.T19.C75, M2.S20.T20.C77, M2.S20.T20.C79**: the question text never points at the road figure that is now added. Suggested closing sentence: "Look at the road in the picture: the rabbit and the two carrots." (The figure also shows the halfway tick, which the text does not mention.)
- **M3.S23.T23.C93, C95, C97 and M3.S25.T25.C101** carry `q_figure` hints (a road with four stretches, a school group beside four vehicles, an open book with labels) and C94 / C96 / C98 / C102 carry `s_figure` hints that are not figures of the book. Not used.
- **M3.S23.T23.C97** is named "Let us do: Q3" in the LP but is part (e) to (h) of the book's Let Us Do Q2 (book_number is right). Cosmetic.
- **M2.S21.T21.C88 (b)**: "7,970 is 70 jumps from 7,900" states the distance to the farther neighbour (7,970 is only 30 jumps from 8,000); the conclusion (nearest hundred 8,000) is right. Suggested: add "and 30 jumps from 8,000" for clarity.
- All sums, counts and answers of the 29 items were recomputed (4,197, 6,731, 5,380 / 5,420, 7,997 / 8,002; 46 / 54; 346 / 654; the 12-cell table; 7,126 / 7,835 / 7,030 / 6,999; the sample pairs of Q2 and Q3; 15 x 4; 461 + 439 = 900 and the eight divisions; 120 / 4 and 120 / 6; 100 x 40; 200 x 50): no arithmetic mistake found. No book print slip was found in this chunk, so nothing had to be corrected in a spec.

### Class 5 Ch 1, chunk D
| Concept id | What is wrong or missing | Suggested sentence |
|---|---|---|
| M3.S31.T31.C127 (question) | The text never gives the horses' arrangement; only the book picture does. The figure carries it, but if the figure is ever dropped the question cannot be done. | "The stable is a square ring of 12 stalls. The horses stand like this: top row from the left 1, 2, 2, 0; left middle stalls from the top 1 and 3; right middle stalls from the top 2 and 3; bottom row from the left 0, 2, 3, 0." |
| M3.S31.T31.C129 and C131 (question) | The text says "square stable" but not that it is a ring of 12 stalls with shared corners. | "The stable is a square ring of 12 stalls: 4 along the top, 4 along the bottom and 2 on the left and on the right. A horse in a corner stall is on two sides." |
| M3.S31.T31.C132 (solution) | The answer "2 more horses" is one reading. The LP's own steps show that with the corner stalls crowded (3, 2, 3, 2) only 10 horses are left with 5 on every side, i.e. up to 8 more could be stolen. The book prints no number. Steps 8 and 9 also contain a sentence addressed to the author ("The book does not print a number for this, so this is one way to read the question"), which does not belong in a learner-facing solution. | Decide the intended answer. If "2 more" stays: "He can steal 2 more horses, leaving 16 with one horse in each corner stall. With fewer horses the corner stalls must be crowded, for example 3, 2, 3, 2 horses in the corners and 10 horses in all, and the king would notice." Remove the author-addressed sentence. |
| M3.S31.T31.C132 (solution) | Step 6 says "The other three sides are the same" without saying in which direction 2 and 1 run. | "Going clockwise from each corner, the two middle stalls hold 2 and then 1." |
| M3.S28.T28.C119 (item hint `q_figure`, not student text) | The hint says four empty rows follow the table; the book prints four filled rows only. | Not a student-text issue; fix or ignore the hint. |

### Class 5 Ch 2, chunk A
(Nothing in the LP was edited; the suggested sentences would make text and picture agree.)

- **M1.S3.T3.C6, C8, M1.S5.T5.C13, C15, M1.S8.T8.C27, C33, C35:** the `text` fields still carry the old card markers "[Image: ...: solution]" in the middle of the steps and "[Image: ...: solution (continued)]" at the end (the other solution concepts have none). The new solution token must come before step 1; the old markers should be removed by the builder.
- **M1.S3.T3.C6:** the steps do not say which blocks are the group. Suggested sentence after step 3: "In the picture, the top row of each bar is one group: 2 blocks of the small bar and 3 blocks of the big bar."
- **M1.S5.T5.C13:** answer says "Your squares may be in different places" but gives no sample. Suggested: "In the picture, Grid A has the first column shaded red, Grid B the top row blue and Grid C the top-left 2 by 2 block yellow."
- **M1.S5.T5.C14:** the question does not say which grids. Suggested: "Look at Grids A, B and C. Do you see 1/3 in any of the grids? Mark it."
- **M1.S5.T5.C15:** step 3 and 4 say "Mark 2 parts in Grid B" / "Mark 4 parts in Grid C" without saying which. Suggested: "In the picture, the bottom 2 rows of Grid B and of Grid C are marked."
- **M1.S8.T8.C31:** counts only. Suggested: "(a): shade the first column of the grid. (b): shade the first 2 columns."
- **M1.S8.T8.C33:** counts only. Suggested: "(a): the first 2 columns. (b): the first row. (c): the first column. (d): the first 2 squares of the first row."
- **M1.S8.T8.C35:** the answer sentence lists four sums; suggested: "In the picture, the four bars are these four wholes in order."
- **Possible contradiction, C27 vs C17:** C27 says 4/16 "is not on the kit", while the worked example C17 and its teaching image C17.IMG1 use pieces of 1/16 ("a piece of 1/8 can be covered by two pieces of 1/16"). The fraction kit is at the end of the textbook and is not in the 15 pdf pages, so I could not check which pieces exist. One of the two statements is probably wrong.
- **M1.S8.T8.C26 / C27:** the book Q1 is a group kit activity; C27 lists names "on the kit" (1/6, 1/9, 1/12 for 1/3; 1/8, 1/12 for 1/4; 1/10 for 1/5; 1/12 for 1/6): same unverifiable-kit caveat.
- **LP hints versus book:** the `q_figure` hint of C14 shows shaded grids (the book prints them blank); the `s_figure` hint of C15 says "first 2 rows" (I used the bottom 2); the `s_figure` hint of C35 shows one circle for one task (I show all four tasks). Hints were not followed where they disagree with the book or the answer text.

### Class 5 Ch 2, chunk B
(Not edited; listed only.)

- **M1.S10.T10.C39** (Q1, equivalents of 1/3): the question text says "Sameer has shaded one-third of the figures. He draws horizontal lines to divide the shapes..." but the figures it talks about (page 4: four squares showing 1/3, 2/6, 3/9, 4/12) are not in the question picture, and the figure now added shows the three blank wholes. Suggested sentence: "Sameer shaded one-third of a square. When he cuts it into 2, 3 and 4 equal rows he gets 2/6, 3/9 and 4/12. Divide each of the three wholes below into more equal rows with horizontal lines and write the equivalent fraction in the box under it."
- **M1.S10.T10.C41** (Q2, equivalents of 2/5): the text says "write your fractions below each image", but only the third and fourth rectangles have an empty slot; the first two are labelled 2/5 and 4/10. Suggested sentence: "Write the fraction of the shaded part in the empty box under the third and the fourth picture, then complete the line below."
- **M2.S13.T13.C51/C52** (Example 1, chikki): neither the question nor the solution says which piece of the chikki is Sevi's. The figure assumes the top strip is Sevi's and the other two strips are Shami's. Suggested sentence for the solution, step 1: "The chikki is cut into 3 equal pieces. Sevi ate the top piece, 1 piece of 1/3."
- **M2.S16.T16.C57** (Example 2, paratha): "One child says: I ate 4/6 ... The other says: I ate 4/5 ... Between Sevi and Shami" never says which child is Sevi. In the book the girl (Sevi) says 4/6 and the boy (Shami) says 4/5. Suggested sentence: "Sevi says: I ate 4/6 paratha yesterday evening. Shami says: I ate 4/5 paratha yesterday evening. Can you tell who ate more? Use your fraction kit to find the answer."
- **M2.S18.T18.C61** (worked example, 9 halves): step 5 says "Check on the number line: 9 jumps of 1/2 from 0 land on 9/2", but the worked-example block shows no number line (only the teaching image of the concept does). Suggested sentence: add "(look at the number line in the picture above)" to that step, or draw the number line (see 1.1).

### Class 5 Ch 2, chunk C
- **M2.S19.T19.C73 (Example 7: Q).** The question text "Raman could eat only 2 slices of pizza. So, he gave 1 to Radhika. How much pizza does Radhika have now?" does not say that Radhika already has 3 slices (1 whole pizza) from Example 6, so it cannot be solved from the question alone (the LP solution's first steps supply this). Suggested sentence: "In the family pizza, Radhika ended up with 3 slices of 1/3, that is 1 whole pizza. Raman could eat only 2 of his 3 slices, so he gave 1 slice to Radhika. How much pizza does Radhika have now?"
- **M2.S19.T19.C73 `q_figure` hint and M2.S19.T19.C71 `q_figure` hint.** C73's hint ("three slices as one round pizza and one more slice") describes the answer picture, and C71's hint ("two round pizzas each cut into 3 slices") is not in the book. No question figure is drawn for either; the hints can be ignored or removed.
- **M2.S22.T22.C89 (Try This: Q).** The text says "Use the number line given below" but carries no figure; the figure comes from the diagram C89.IMG1. The question says 16 ants and the book draws 17 (see section 3). The LP is right (16 x 1/4 = 4 cm).
- **M2.S20.T20.C77 and C81.** "Use the number line" / "Use a number line" also point at figures that the diagrams C77.IMG1 / C81.IMG1 supply.
- **M2.S20.T20.C75, C77, C79 (names).** The book itself mixes "Dadiji" and "Dadaji" (page 9: "Dadiji had 7 pieces", then "Dadaji ate 7 pieces"); the LP follows the book. The diagrams use the LP's names (Dadaji on the three lines, Dadiji on the five lines).
- **M3.S23.T23.C91 and C93.** The worked examples have no `ncert_refs`: they are LP-made examples, not from the book (C92 has `rh.pictures`). Nothing wrong, just not traceable to a book page.
- No numeric error found in the LP solutions of this chunk: C66 (5/2 = 2 1/2), C68 (6/2 = 3), C70 (9/4 = 2 1/4), C72 (3 slices each, 1 + 1 = 2 pizzas), C74 (4/3 = 1 1/3), C76 (7/2 = 3 1/2), C78 (3, 3 1/2, 2 1/2), C80 (36/2 = 18, 5 + 6 + 7 + 6 + 7 + 5 = 36), C82 (7/4, 6/4, 8/4, 10/4, 12/4), C84 (9 + 7 + 6 + 8 + 10 + 12 = 52, 52/4 = 13), C86, C88 (7 + 7 = 14), C90 (16/4 = 4), C91 to C93 all recomputed.

### Class 5 Ch 2, chunk D
(No LP text was edited and no decision changed because of these.)

- **M3.S24.T24.C95 and C97 (question text):** the question names "Sevi and Shami" but then says "One child says ... The other says ...", so the learner cannot tell who ate which amount. Suggested: "Sevi says: I ate 7/8 paratha yesterday evening. Shami says: I ate 8/6 paratha yesterday evening." (and for C97: "Sevi says: I ate 5/8 paratha ... Shami says: I ate 3/6 paratha ..."; in the book the girl on the left holds the first amount and the boy on the right the second, but the pictures do not name them).
- **M3.S24.T24.C96 and C98 (solution text):** no sentence refers to the picture that now opens the solution. Suggested first line for C96: "Look at the picture: 7 of the 8 pieces of one paratha, and one whole paratha cut into 6 plus 2 more pieces of the other." For C98: "Look at the picture: the half line cuts the paratha cut into 6 exactly in half; the paratha cut into 8 has 4 pieces on one side of the line and 1 more piece past it."
- **M3.S27.T27.C110 (solution text):** the tree includes a box "You"; step 4 could say "a child of your father is another child in your family: your brother or sister" so that the box makes sense (the answer text "brother or sister" is unchanged).
- **M3.S25.T25 (question names and book numbers):** the concept names run Q2, Q3, Q4 (counting from the "reference to 1" set) while `book_number` says "Let Us Do (reference to 1/2), Q1 / Q2 / Q3" (the book numbers them 1, 2, 3 within that set). Not wrong, but the two numberings differ.
- **Order:** in the book the two box questions (circle equal to 1/2, circle less than half) come BEFORE Example 9 ("Now let us compare fractions using 1/2"); the LP puts Example 9 (topic T24) before them (topic T25). Teaching order is fine in the LP; just not the book's order.

### Class 5 Ch 3, chunk A
- **M1.S4.T4.C7 (worked)**: the steps say "the seat is back at the starting position E" but the question never says what E is. Suggested: "A seat E on the giant wheel starts at the top. It takes 1 half turn and then 2 quarter turns, all in the same direction. What turn is that in all?"
- **M1.S5.T5.C9, C11, C13 (questions)**: "the starting position E": E exists only in the book's wheel picture (letter above the top seat) and no wheel picture is added. Suggested: "A giant wheel makes a full turn when it comes back to the starting position E, the seat at the top of the wheel."
- **M1.S3.T3.C5 (question)**: "the child in the picture" does not say there are two pictures. Suggested: "Look at the two pictures of the children, before and after the call STATUE. Can you recognise the child who has made a full turn? ..." The figure labels the pictures Before and After while the solution says "first picture" and "second picture": either say "the Before picture / the After picture" in the steps or accept.
- **M1.S7.T7.C20 (solution)**: the sample ticks read as exact: scissors "a 1/4 turn", tongs "less than a 1/4 turn". Real scissors open to nearly a half turn. Suggested: "(d): the scissors open about a 1/4 turn" (it already says "Your answer may differ").
- **M1.S9.T9.C29 (solution answer)**: the answer line leaves out the right angle that the steps and the figure show. Suggested: "Sample answer: less than a 1/4 turn is acute; exactly a 1/4 turn is a right angle; between a 1/4 and a 1/2 turn is obtuse. Your answer may differ."
- **M1.S9.T9.C31 (solution)**: the answer says "two bigger ones can make a right angle or an obtuse angle", but step 3 says a right angle comes from two turns that add to exactly a quarter turn (not necessarily bigger). Suggested: "Sometimes. Two small acute turns can together be acute; two acute turns that add up to exactly a quarter turn make a right angle; two bigger acute turns can make an obtuse angle." The figure shows them in the order acute, right, obtuse; the steps list obtuse before right.
- **M1.S6.T6.C15 (worked)**: "(a practice picture)" is now backed by the new diagram; if the diagram were dropped the phrase would point at nothing.
- No book/LP number clashes found: C33 counts (3 right, 3 acute, 2 obtuse = 8), C35 steps (angles sum 540), C37 order all agree with the pictures.

### Class 5 Ch 3, chunk B
- M2.S11.T11.C41 (Q1), C47 (Q4), C49 (Q5): the questions say "the straw" / "the starting point" without naming the circle. Suggested: "On your circle folded into 8 equal parts, with the straw on the starting point A: show a 1/8 turn of the straw. Show a 2/8 turn. Show a 1/4 turn. Show a 3/8 turn." (C47: "On the same circle, continue turning by 5/8, 6/8, 7/8 and 8/8 ..."; C49: "On your circle folded into 6 equal parts, with the straw on the starting point, show the turns of the straw equal to 1/6, 2/6, and so on until you complete a full circle.")
- M2.S11.T11.C42, C48, C50 (Angle Measuring Tool solutions): no turning direction is stated. Suggested first step: "Turn the straw the way the hands of a clock move."
- M2.S11.T11.C42 (and the other solution concepts that had two cards): the old `text` carries two image markers, one in the middle of the steps and one after the answer. The new rule is one figure before the first step, so the markers have to go when the placeholder is written.
- M2.S14.T14.C57: the question does not number the angles but the solution (C58) says "Angle 1" to "Angle 7". Suggested sentence for the question: "The angles are numbered 1 to 7 from left to right; angle 4 is the upper of the two angles in the middle."
- M2.S14.T14.C58: the LP writes "about" before 1/12 (angle 1), 1/6 (angle 4) and 1/3 (angle 6). The measured angles are 31, 59 and 119.7 degrees, so "about" is right; the diagram boxes show the plain fractions to fit the box.
- M2.S14.T14.C59 / C60: the end arrow of (d) is drawn by the book about 5 degrees further than 5/12 of a turn; the LP says "about 5/12". Nothing to change in the text; the diagram draws exactly 5/12.
- M2.S16.T16.C66: the sample drawing uses these corners, all turning clockwise: the lower end of the 1/2 line, the upper end of the 1/4 diagonal, the top end of the 1/8 line, the upper-right end of the 1/12 line, the right end of the bottom 1/4 line. Suggested first step: "Take the lower end of the 1/2 line, the upper end of the diagonal, ... as the corners and turn each line clockwise" (or keep "your drawing may differ" and accept the sample).
- Concept names inside T14 / T16 / T18 restart at "Q1" (C57 "Q1", C59 "Q2", C61 "Q3", C65 "Q1", C67 "Q2", C71 "Q1") while the book numbers are Let Us Do Q1 to Q6. Cosmetic: the `book_number` fields are right.

### Class 5 Ch 3, chunk C
- **M3.S21.T21.C80 / C81 (row g):** the book prints no number before "right angles clockwise" in the last row (print slip), and the LP question has a blank "___". The LP answer uses a sample "if it is 3, North". Suggested sentence for the question: "(g): West, ___ right angles clockwise (the number is missing in the book; take 3 as an example), four 1/2 right angles anti-clockwise." No diagram of mine shows this row, so no value is corrected in a spec.
- **M3.S21.T21.C84 (question):** "the same place" is not named. Suggested sentence: "Padma is facing the toy shop and takes a half turn clockwise to face the ice cream cart. What other way can she turn to face the same place?" (it reveals the answer to the previous question, which the learner has just done).
- **M3.S21.T21.C82 and C84 (questions):** the LP question text does not say where the other places are; only the figure does. This is fine as long as the question diagram is shown; if the figure is ever dropped, add: "The bookstall is on her left, the parking sign on her right and the ice cream cart behind her."
- **M3.S20.T20.C76 (question):** the text names the creatures but not which way they face before and after; this is carried only by the figure.
- **M3.S20.T20.C77 and M3.S21.T21.C81, C83 (`text` field):** the old text has `[Image: ...]` markers in the middle of the steps and after the answer (from the old cards). The builder should remove them when the token is put before step 1.
- **Wording:** LP says "bookstall"; the book's sign says BOOKSTORE. The diagram uses the LP word. Either word is fine, but the LP and the picture must agree.

### Class 5 Ch 4, chunk A
- **M1.S2.T2.C3** (worked, step 5): "...group 1 becomes 18 and group 2 becomes 20, and the gap is still 2." The gap was 4 before this swap and is 2 after it, so "still" is wrong (checked: swapping 6 and 7 gives 2 + 7 + 9 = 18 and 4 + 6 + 10 = 20). Suggested sentence: "They differ by 1, so group 1 becomes 18 and group 2 becomes 20, and the gap is now 2, not 0."
- **M1.S3.T3.C5** (question text): omits the book's hint (an arrow between 2 and 5 and the note "Think what will happen to the sums if we interchange 2 and 5?"), but the solution C6 step 2 starts "The hint swaps 2 and 5". Suggested sentence to add to the question: "A hint arrow joins the 2 of group 1 and the 5 of group 2: think what happens to the sums if we interchange 2 and 5."
- **M1.S3.T3.C8** (`answer_tex` and the Answer line of `text`): broken LaTeX: `Swap $5$ and $9 ($or $7$ and $11)$: ...`. Suggested: "Swap $5$ and $9$ (or $7$ and $11$): both groups add up to $43$. This takes $1$ move."
- **M1.S3.T3.C10** (step 2): the list of pairs that differ by 2 is incomplete: "11 and 13, 15 and 17, 19 and 21, and 23 and 25" leaves out the pairs with the Group 2 number smaller. Suggested sentence: "The pairs that differ by $2$ are $11$ and $13$, $13$ and $15$, $15$ and $17$, $17$ and $19$, $19$ and $21$, $21$ and $23$, and $23$ and $25$. Every other pair differs by $6$ or more." (The conclusion, no pair differs by 4, is true: every difference is 2 plus a multiple of 4.)
- **M1.S10.T10.C28** (`answer_tex`): gives one sentence per part while the steps give two for (a) and (b) (two subtractions) and two for (c) and (d). Suggested: "Sample answer: $(a)$: $242 - 164 = 78$ and $242 - 78 = 164$; $(b)$: $1,301 - 839 = 462$ and $1,301 - 462 = 839$; $(c)$: $784 + 137 = 921$ and $921 - 784 = 137$; $(d)$: $590 + 234 = 824$ and $824 - 590 = 234$. Your answer may differ."
- **M1.S11.T11.C29** (`q_figure` hint only): says "A bar from 18 litres to 65 litres"; the book shows two boxes (18 l and 65 l) joined by a curved arrow. No diagram is made for this item, so only the hint is wrong.
- All other solution arithmetic in this chunk was recomputed and is correct (T4, T5 lorry 103, T6 138, T7 152 and 93, T8 six sums, T9, T10, T11 47, T12 45 and the eight differences, T13 33, 36, 39).

### Class 5 Ch 4, chunk B
- **M2.S14.T14.C37 and M2.S14.T14.C39 (question text):** "In each of the boxes above ..." and "... in each box?" depend completely on the figure; the LP text never states the sums. With the required diagram this is fine; if the text must also stand alone, add: "The boxes show: sums of 2 consecutive numbers 3, 5, 7, 9; sums of 3 consecutive numbers 6, 9, 12, 15; sums of 4 consecutive numbers 10, 14, 18, 22."
- **M2.S19.T19.C59 (question text):** "Look at the distances marked on the map" while the four distances only exist in the figure. Suggested extra sentence if wanted: "The legs are Delhi to Mumbai 1,600 km, Mumbai to Goa 590 km, Goa to Hyderabad 670 km and Hyderabad to Puri 1,055 km."
- **M2.S14.T14.C38 and M2.S16.T16.C46 (answer `text` field):** the plain `text` of the answer still carries `[Image: ...: solution]` and `[Image: ...: solution (continued)]` markers from the old cards, placed inside the steps (after step 5 of C38, after step 3 of C46) and at the end. Neither item gets a solution diagram now, so the build must drop these markers (and, for every other concept in the chunk, the old card markers in `text`).
- **M2.S21.T21.C65, C66, C67, C68:** the label "(i)" is written without math mode while (a) to (h) are `$(a)$` ... `$(h)$` (question_tex, steps_tex, answer_tex). Suggest `$(i)$`.
- **M2.S21.T21.C66, step (i):** "put the 1 in a new place on the left. The sum is 1,05,050" does not name the place (lakhs) and switches to the Indian grouping `1,05,050` while the rest of the chapter has no 6-digit number. Suggested sentence: "Ten thousands: 5 + 5 = 10, so write 0 and put the 1 in the lakhs place. The sum is 1,05,050."
- **M2.S14.T14 and M2.S16.T16:** concept names repeat ("Sums of Consecutive Numbers: Q1/Ans1" in both topics); cosmetic.
- All other LP numbers were recomputed (sums, differences, regroups, the ten pair sums of C62, the closest pairs): no arithmetic error found in this chunk.

### Class 5 Ch 4, chunk C
- M3.S27.T27.C87 (question): "Try this method for the number 59." never says what the method is, and the ovals of the figure carry it. Suggested: "Use Piku's method: make 9 in each place, then add 1. Fill the two ovals. 59 + ___ = 100."
- M3.S27.T27.C89 (question): "Now, use this method to solve the following." names no method. Suggested: "Now, use the make-9-then-add-1 method to solve the following."
- M3.S27.T27.C95 (question): "Now, use the above solutions to find answers to the following problems. Do not calculate again." points at the answers of C93 without naming them. Suggested: "Use your answers to the question about taking away 9 or 99. Do not calculate again."
- M3.S27.T27.C96 (steps_tex, first step): broken math delimiters, `$9 ($or $99)$`. Suggested: "...so the blank is the first number minus $9$ (or minus $99$)." The same string should be checked in the `text` field.
- M3.S29.T29.C104 (steps_tex, first step): `$A 5$ digit number` has the letter A inside the math. Suggested: "A $5$ digit number between $25,000$ and $27,000$ ...".
- M3.S27.T27.C92 (steps_tex, step 4): "The last nine is 9, and adding 1 makes it carry." is unclear. Suggested: "The units digit 0 needs 9 to make 9, so the blank ends in 9, and adding 1 makes it carry."
- M3.S25.T25.C83 and M3.S28.T28.C97 (worked example question text): the learner-facing question ends with "(practice values)". Suggested: delete that bracket from the learner text (it is a note for the author).
- LP numbering differs from the book's: C71/C73/C75 are called Q1/Q2/Q3 in the LP but are book Q2/Q3/Q4 (p.10); C77/C79/C81 "Let us do Q1/Q2/Q3" are book Let Us Do Q3/Q4/Q5 (p.15). C85's book note says "blanks" in the book (one blank is printed). Only the labels differ; the questions match the book text.
- All LP answers were recomputed (Mary 10,245; council 68,878 and 1,622 left; truck 6,525 and 1,725; Ambrish 62,873 and 29,502 more; factory 31,300; Virat/Sachin 34,357; 32 + 68; 59 + 41; 123, 334, 5,897, 4,445; 820, 240, 600; 58, 74, 135, 88, 148, 664; 23, 47, 778, 567; palindromes 10 / 12 / 20). No arithmetic error found.

### Class 5 Ch 4, chunk D
- **M4.S41.T41.C145** (question): says "Read the table and answer the questions that follow" but the table is not in the question text or LaTeX (only the old card showed it). With the old card dropped the learner has no data. Suggested: add to the question text a LaTeX array with columns Mountain | Height (in metres) | Climbed in the year and these rows: Mount Kanchenjunga (India and Nepal border) 8,586 2022; Mount Everest (Nepal-China border) 8,848 2013; Mount Makalu (China-Nepal border) 8,485 2019; Mount Lhotse (Tibet-Nepal border) 8,516 2018; Mount Kilimanjaro (Africa) 5,895 2016; Mount Elbrus (Russia) 5,642 2017; Mount Annapurna I (Nepal) 8,091 2021.
- **M4.S42.T42.C147** (question): "For each district, find out if the number of certificates were sufficient?" has no table and no story (the book: a Math Metric Mela where certificates were printed per district). Suggested: "A Math Metric Mela was held and every student was to get a certificate. The table shows the certificates printed and the students who attended." plus a LaTeX array District | Certificates Printed | Students Attended with rows Chittoor, A.P. 18,225 18,104; Jaunpur, U.P. 19,043 19,265; Raigad, Maharashtra 20,863 19,974.
- **M3.S31.T31.C109** (question): "This time, fill the grid such that each row and column has numbers in decreasing (dec) order." has no "3 by 3" and no "numbers 1 to 9, each once" (it relies on the previous question). Suggested: "In a $3 \times 3$ grid, arrange the numbers $1$ to $9$ such that each row and each column has numbers in a decreasing (dec) order. Each number should be used only once."
- **M4.S33.T33.C119** (question) and **C120** (steps): items (a) to (h) are written `$(a)$` but (i), (j), (k), (l) are plain "(i)"; make them `$(i)$`, `$(j)$`, `$(k)$`, `$(l)$` (also in C120's answer_tex for "(i): $846$").
- **M4.S33.T33.C124** (step 1): "(a row of $12$ and a row of $11)$" has the closing bracket inside the math; suggested "(a row of $12$ and a row of $11$)".
- **M4.S33.T33.C121 and C123** (question): the sentence "Paired arrangement for $18$" is the book's picture caption and reads as a loose phrase once the picture is a separate figure. Suggested: "The picture shows $18$ counters in two rows of $9$, each counter paired with the one below it." (and "twelve counters above eleven, the last top counter has no partner" for 23).
- Naming only (not read by the learner): concept names "Let Us Think and Solve (grids): Q1 to Q5" are the five grids of book Q2 (the book's Q1 is the palindrome question, topic T28); "Even and Odd Numbers: Q2/Q3" (T33) are the 18 and the 23 picture of book Q2; "Q1 to Q3" in T35 are book Q3 (a), (b), (c); "Let Us Think: Q1/Q2" in T37/T39 are book Let Us Think Q1 and Q2; T41 "Q1" is book Q3 (Mountain climbing).

LP maths I re-checked and found right: the 11 combinations of Jincy's coins (4 + 5 + 2, total 51 rupees available, 38 payable), the 4 ways of the coin worked example, all subtraction answers in C143, C146 and C148, the parity sample sums in C128, C130 and C132.

### Class 5 Ch 5, chunk A
- **M1.S4.T4.C8** (question): the text lists the labels but not the two arrows, ×2 (100 cm to the first blank) and ×100 (1 m to 100 cm), which only the figure carries; the solution C9 refers to both arrows. Suggested sentence to add (only if the figure is ever missing): "The arrow ×100 goes from 1 m to 100 cm and the arrow ×2 goes from 100 cm to the first blank."
- **M1.S6.T6.C17, C19, C21, C23** (Let Us Compare Q2 a-d, questions): each says only "Look at the picture of some of the world's tallest statues" and carries none of the six names and heights, so the question cannot be solved without the figure. Suggested sentence: "The heights are: Statue of Unity, India, 182 m; Spring Temple Buddha, China, 128 m; Guanyin of Nanshan, China, 108 m; Statue of Liberty, USA, 93 m; The Motherland Calls, Russia, 91 m; Christ the Redeemer, Brazil, 38 m."
- **M2.S9.T9.C32, C34, C36** (Kilometre Race Q1-Q3): the LP hint `q_figure` says "a straight race track of 3 km from the starting point to the finish line"; the book has no such figure (pdf p.4 is text only). No question diagram is made.
- **M2.S9.T9.C33, C35**: the solutions count a station / a child at the finish line (6 stations at 500 m ... 3 km, 10 children at 300 m ... 3,000 m). The book's question does not say whether the finish line counts; the LP choice is followed and drawn.
- **Stale image markers in `text`** of answer concepts, e.g. C7 ("[Image: Let Us Find: Ans1: solution]" after step 6 and "(continued)" at the end), C9, C11 and the other answer concepts: they mark the old card positions in the middle of the steps and after the answer. With the v3 rule (solution token first, before step 1) the old markers must be removed or replaced when the builder writes the new token.
- **M2.S8.T8.C29**: all numbers are practice values (125 steps for 100 m, one step 80 cm): the arithmetic checks (10,000 / 125 = 80; 12,000 / 80 = 150; 40,000 / 80 = 500; 160,000 / 80 = 2,000), no change needed; mentioned only because the question text is the book's open activity.

All other LP solutions in this chunk were recomputed and agree with the book's question and with themselves (Let Us Compare Q1 a-e, Q2 a-d, rope table, race Q1-Q3, sari match, worked examples).

### Class 5 Ch 5, chunk B
(Not edited, only listed, as decided.)
- **M2.S11.T11.C40, C42, C44, C46, C48 (questions):** the text says "shown in the table" but gives none of the data. The diagram now supplies the table. Alternative: add a LaTeX array to `question_tex` (header Station number | Name of the station | Distance from Dibrugarh, then the 8 rows 9 Dimapur 306 km, 14 Guwahati 556 km, 22 Jalpaiguri Road 983 km, 34 Bhubaneswar 2,007 km, 40 Visakhapatnam 2,450 km, 45 Vijayawada JN 2,800 km, 55 Coimbatore JN 3,675 km, 65 Kanniyakumari 4,187 km).
- **M2.S11.T11.C48 / C49:** "Coimbatore $JN$" is set in maths italic in `question_tex` and `steps_tex`; JN is a name, suggest plain text (or `\text{JN}`). The other rows write "Vijayawada JN" in plain text.
- **M2.S10.T10.C38:** the first block (textbook text) says "Look at the stations on the route shown in the table below and answer the questions", but no table is attached to C38 (the table is only in the T11 questions). Suggested sentence: "Look at the stations on the route in the table in the questions that follow."
- **M2.S13.T13.C55 (question):** the text says the lines "are numbered from the top of the picture to the bottom", which is only roughly true: line (5) (upper left side of the small tilted shape) sits higher than (3) and (4). The book prints no numbers. Suggested sentence: "The eight boxes are numbered (1) to (8) in the picture." (The diagram now prints these tags.)
- **M2.S13.T13.C55 / C56 (design):** the LP calls the inner shape a "rectangle" and the second shape a "diamond"; in the book picture they are not exact (inner shape sides 35.0 / 27.0 / 34.7 / 28.9 mm; diamond sides 48.0 / 44.9 / 41.2 / 44.0 mm). Harmless for the measuring, but the words 'nearly a rectangle' would be more exact.
- **M2.S13.T13.C56 (solution step 1):** "These lengths were measured on the picture at its printed size, so your ruler may read 1 mm different." On a screen the learner cannot measure at printed size. Suggested sentence: "Measure the design in your book, or check your numbers against these lengths; they may differ by 1 mm."
- **M2.S13.T13.C57 (question):** says "Fill in the table" but no table is in the text. Suggested: add a LaTeX array with the header "Number of days | Length of the sprout (in mm)" and rows Day 1 to Day 4 with empty right cells.
- **M2.S13.T13.C59 / C60:** the LP numbers the five lengths (a) to (e); the book prints 1 to 5. The diagram uses the LP's letters. The book's follow-up "How did you draw lines of lengths 36 mm and 67 mm? Share your thoughts in class." is not in the LP (not a diagram matter).

LP arithmetic checked: C38 615 - 340 = 275; C41 4,187; C43 2,800 - 983 = 1,817; C45 2,800 - 2,450 = 350; C47 556 - 306 = 250 and 2,007 - 983 = 1,024; C49 3,675 - 556 = 3,119; C54 9 marks; C58 3 < 9 < 16 < 25; C60 55, 36, 83, 36 mm, 6 cm 7 mm; C61 60, 900, 8,000; C62 7,305 = 73 m 5 cm, 307 cm. All correct, no contradiction with the book.

### Class 5 Ch 5, chunk C
- **M2.S15.T15.C64 (question, Q1 (a)), also C65's `question` copy:** the last bottom-line blank is written `___ m` in `question`, `question_tex` and `text`. It should be `___ mm` (50 cm = 500 mm). Suggested: "Bottom line: 10 mm, ___ mm, ___ mm, 250 mm, 320 mm, 450 mm, ___ mm." (The solution step 5 already says "Your maths book prints m under this tick, but 50 cm is 500 mm", so it can stay or be shortened.)
- **M2.S15.T15.C64, C66, C68 (question and the copy in C65, C67, C69):** "Fill in the two boxes x___ as well: the arrow on the top line is x7 and the arrow from the top line to the bottom line is x10." does not say that x7 and x10 are already printed and which two boxes are empty. Suggested for (a): "The top arrow is x7 and the left arrow is x10. Fill in the two empty boxes x___ as well: the right arrow from 7 cm down to the bottom line, and the arrow along the bottom line." (for (b) use x4 and x100, for (c) x9 and x1,000).
- **M2.S15.T15.C65, C67, C69 (`answer` / `answer_tex`):** "Boxes: x7, x10" (and "x4, x100", "x9, x1,000") does not say which box is which. Suggested for (a): "Boxes: x10 on the arrow from 7 cm down to 70 mm, and x7 on the bottom-line arrow from 10 mm to 70 mm."
- **M2.S15.T15.C72, C73:** item (i) is written "(i): ..." without the `$...$` that (e) to (h) use (`$(e)$`). Formatting only.
- **LP numbering differs from the book's:** LP "Let us do: Q4, Q5, Q6" (T15) are the book's Q2 (a) to (d), (e) to (i), (j) to (n); LP "Q1 to Q3" are Q1 (a) to (c). In T18, LP "Q4" and "Q5" are the book's Q4 (a) to (d) and Q4 (e) to (g). The `book_number` fields are right; only the concept names differ.
- **M3.S17.T17.C79:** the book's "Share your thoughts in class" is left out; harmless.
- **M3.S17.T17.C80 and C82 (answers with the column picture removed):** the LP `s_figure` hints describe a column picture ("a carried 1 into the km column", "the borrowed digits marked"); with the decision none the LaTeX steps must carry this. They do (regroup 1,100 m = 1 km 100 m; 63 m = 6,300 cm). If the column layout is wanted as LaTeX, the text alternatives are in the items.
- No wrong arithmetic found: I recomputed every LP answer of T15 to T19 (3 m 75 cm + 2 m 25 cm = 6 m; 48,700 - 17,900 = 30,800 m; 2,300 + 2,650 = 4,950 m; Q4 differences 1, 6, 1, 20 mm and 45 cm, 322 m, 1 m; 6,300 - 1,675 = 4,625; 12 x 240 = 2,880; 18,900 / 3 = 6,300; 90 / 3 = 30).

### Class 5 Ch 5, chunk D
- **M3.S28.T28.C123**: the text says "each row and column and each 2 x 2 box" without saying which boxes. Suggested sentence: "...such that each row, each column and each of the four 2 x 2 corner boxes (top left, top right, bottom left, bottom right) does not repeat the sign."
- **M3.S28.T28.C124**: formatting nits in steps_tex, answer_tex and text (spaces before commas and full stops after \times and \div, see section 2).
- **M3.S21.T21.C101**: the text asks for "the four boxes" and does not say where they are; the figure carries them (above the top line, left arrow, below the bottom line, right arrow). If the figure is ever not shown, suggest adding: "The four boxes are on the arrow from 5 m to 10 m, the arrow from 5 m down to ₹100, the arrow from ₹100 to the next amount, and the arrow from 10 m down to the second amount."
- **M3.S25.T25.C118**: step 1 mentions an inch scale on the other ruler edge, but the figure (as in the book) shows a cm ruler with a 1 inch bracket beneath it and no inch scale; no change needed, noted for the reviewer.
- **M3.S26.T26.C119**: `q_figure` describes a wall chart picture that the plan does not draw (decision none); nothing in the question text depends on it.

### Class 5 Ch 6, chunk A
Not edited, no decision changed because of them.

- M1.S3.T3.C7 (Let Us Think Q2): the question text does not say that the frame is "a two-digit number times a one-digit number" (three boxes); only the picture and solution step 1 say so. Suggested sentence: "Use the frame: a two-digit number times a one-digit number, with three boxes for the digits."
- M1.S3.T3.C11 (Q4): the question text has no number chart, but solution step 1 says "Use the number chart". Suggested sentence for the question: "Use the number chart from 0 to 99 (10 rows of 10)." or add the chart as a LaTeX array (the question diagram is `optional`, not added).
- M1.S3.T3.C11 / C12: clues (d) "I am an odd number" and (g) "My ones digit is even" cannot both be true, so no number fits all eight clues. The LP says exactly that (18 fits all but (d)). If (d) read "even", 18 would be the single answer; it may be a print slip in the book. Nothing to change in the LP; flagged for the teacher.
- M1.S3.T3.C9 (Q3): the question text gives (a) to (d) but the book prints no letters on the pictures. Suggested sentence: "The four pictures are lettered (a) to (d) in the order printed."
- M1.S3.T3.C13 (Q5): the nine numbers and four signs of the grid are only in the picture (now drawn). Optional sentence for the text: "The grid has the numbers 100, 25, 5, 10, 2, 36, 12, 4 and 3 and the signs -, x, +, ÷."
- M1.S5.T5.C17 (order of numbers): the text names (a), (b), "the two big arrays", (e), (f), (g); the book prints no letters c) and d). Fine as it is; the diagram follows the book.
- M1.S7.T7.C26 (Q2): the question text lists the table row "700 x 8 =" and the box "700 x 4 =" without saying they differ; only the solution (step 6) says so. Suggested sentence in the question: "The table row says 700 x 8 and the box says 700 x 4: do both."
- M1.S7.T7.C24 and C25: letters (a) to (h) are wrapped in LaTeX ($(a)$) but "(i)" is plain text, in the question and in step 9 of the answer. Suggested: write $(i)$ like the others.
- M1.S7.T7.C31 (multiplying by 1,000): step 3 speaks of "the place value board" that no text defines; the new diagram supplies it (nothing to edit if the diagram is kept).
- M1.S2.T2.C3, M1.S4.T4.C15, M2.S8.T8.C36: the worked examples use their own numbers (36 pouches, 7 x 12, 6 x 14) and have no book ref. Not wrong, just LP-authored; the book's own figures on those pages are 6 x 13 and 13 x 6 (page 3) and 18 x 5 (page 5).

### Class 5 Ch 6, chunk B
(No LP text was edited and no decision was changed because of these.)

- M2.S13.T13.C53 (worked example): the question gives the tray only for 6 x 19 ("A tray has 6 rows with 19 squares in each row ... Then find 13 x 31 the same way"), but the steps use "the 31st square of every row" and "a strip of 13 squares", so the learner is never told there are 13 rows of 31 squares. The diagram draws 13 rows of 31. Suggested sentence: "Then find 13 × 31 the same way, with a tray of 13 rows and 31 squares in each row."
- M2.S12.T12.C48 (solution, step 4): the learner-facing step says "the book does not label the arrows of this box". This is also true of the 16 x 4 box, and a solution should not talk about the book. Suggested sentence: "$35 \times 14$: $35$ is odd and cannot be halved into a whole number, so halve the $14$ and double the $35$. Half of $14$ is $7$ and double $35$ is $70$. The new problem is $70 \times 7 = 490$, so $35 \times 14 = 490$."
- M2.S15.T15.C62 (solution): steps (1) to (6) speak of "the strip is 2 squares in each row", "the strip is 15 squares", but the question shows no tray or squares. Suggested wording: "the extra part is 2 in each row, 7 × 2 = 14" (and the same for the other five).
- M2.S16.T16.C63 (worked example, step 4): "The strip is 8 packets too many" refers to a strip no picture shows. Suggested sentence: "That counts 8 packets too many, one for each of the 8 trays: 320 − 8 = 312, so 8 × 39 = 312 packets."
- M2.S14.T14.C58 (solution, step 2): the LP says the first 20 squares are "yellow" and the last "green"; the book prints light orange and light green. The diagram uses a yellow-orange tint and a light green, so the words still fit; no change needed unless the user wants "orange".
- Old image hints: the `q_figure` / `s_figure` strings of the old cards (for example C39 "array of 5 rows of 18", C44 "54 written beside both", C48 "four boxes filled in") describe pictures that are not drawn in this run; the lines of the new plan should not refer to them.

### Class 5 Ch 6, chunk C
- **M2.S17.T17.C70 (Let Us Solve Ans3), step 3**: "The strip is 2 books in each box, 36 × 2 = 72. Take it away." The strip is never defined in the text (a leftover of a picture). Suggested sentence: "50 is 2 more than 48, so $36 \times 50$ counts 2 extra books in every box: $36 \times 2 = 72$. Take 72 away."
- **M3.S19.T19.C80 (Example 4: Q), `question_tex`**: the last sentence ends with `$\underline{\hspace{1.2em}} kg$`, so "kg" is set in italic math (every other item uses `\text{ kg}`). Suggested: `The family produces $\underline{\hspace{1.2em}}\text{ kg}$ of waste in a year.`
- **M3.S19.T19.C80 and C82, `q_figure` hints**: they describe a woman pouring waste (decoration) and a heap of compost with a price tag (invented). Neither is a given figure; hints only, ignored.
- **M3.S19.T19.C83 (Example 5: Ans)**: the LP names the first written method Kanti's four lines and the second John's two lines. The book prints the first one without a name and the second as "Another way". Not an error (the same naming as in Example 4), but a teacher reading the book will not find the names there.
- **M3.S20.T20.C84 (Let Us Multiply Q1) and C86 (Q2), `question_tex`**: the LP text has blanks "$\underline{\hspace{1.2em}}0 (8 \times 30)$" and "$\underline{\hspace{1.2em}}00 (40 \times 60)$", while the book prints "0 (8 × 30)" and "00 (40 × 60)" with no blank drawn. The LP and its solution treat them as blanks (24 and 24), which is right; the figures draw the blank.
- **M3.S20.T20.C85 (Ans1), `answer_tex`**: "The blanks are 16, 24 and 24." does not say which blank is which. Suggested: "Kanti's blanks: 16 and 24. John's blank: 24. Box cells 240 and 16. Total 256."
- **M3.S20.T20.C84 and C86 question text**: both give the box and two line forms only in words ("Fill the box with columns 30 and 2 and row 8, then complete the line methods ..."); without the figure the learner cannot see where the blanks sit. Covered by the required question diagrams; no change needed beyond placing them.
- **M3.S18.T18.C77 and C78**: the examples (23 x 14 with 14 shelves of 23 ghee jars, 26 x 13 with 13 trays of 26 butter packets) are the LP's own, not the book's; nothing wrong, but they have no book figure to map (see the warnings below).
- No missing data was found in the Let Us Solve texts: every number the solutions use is in the question, and every solution result recomputes (1,470; 124; 1,728; 32; 145; 5,346).

### Class 5 Ch 6, chunk D
- **M3.S21.T21.C88 (question).** The text never mentions the tables that the figure shows. Suggested sentence: "Use a table like Nida's for each problem: write the digits of the first number across the top, the digits of the second number down the side, a row for the column sums and one last cell for the total."
- **M3.S24.T24.C117 (question).** The text names the frames but not what is to be completed. Suggested sentence: "Complete each frame: write every carry in its circle and the digits of every row in the boxes, then write the product."
- **M3.S24.T24.C117 / C118.** The text says the first two frames have columns thousands to ones, but the sum of frame (ii) is 11,830 (five digits) and the book prints no sum row. Suggested sentence for C118: "The sum 11,830 has a digit in the ten thousands place, so write it one place to the left of the thousands."
- **M3.S24.T24.C118 (steps for (ii) row 2).** Gives only "2 x 455 = 910, so the row is 9,100". The figure shows the carries of the method. Suggested sentence: "(ii): row 2. Write a 0 first. 2 x 5 = 10, write 0 and carry 1. 2 x 5 = 10, and 10 + 1 = 11, write 1 and carry 1. 2 x 4 = 8, and 8 + 1 = 9, write 9. Row 2 is 9,100."
- **M3.S24.T24.C118 (steps for (iii) row 2).** "0 x 143 = 0, so the row is 0" while the book prints four boxes for that row. The figure shows 0 0 0 0. Suggested sentence: "(iii): the row for 0 tens is all zeros: 0 0 0 0."
- **M3.S24.T24.C118 (frame (ii) circle above Th).** The book prints a circle above Th; the figure puts the last carry 2 (6 x 4 + 3 = 27) in it. Suggested sentence in (ii) row 1: "6 x 4 = 24, and 24 + 3 = 27, write 7 and put the 2 in the thousands place."
- **M3.S23.T23.C112 (steps).** The LP explains the blue and red digits but not the orange ones that the book also prints (the 10 of 10,000 and the 1 of 1,400). Suggested sentence: "The orange digits are 10 thousands and 1 thousand: 10 + 1 = 11 thousands."
- **M3.S21.T21.C95 / old s_figure hint.** The old hint describes a seating plan with 48 seats marked; the book gives no positions. Nothing to change in the text; the hint should not be reused.
- **Hint wording.** The old q_figure of C88 says tables of two-digit multipliers have "2 columns and 2 rows"; the printed tables have 3 columns and 5 rows (headings and sums rows included).

### Class 5 Ch 6, chunk E
- **M4.S28.T28.C142** (Let Us Do Q4 question): the text never mentions the three arrays of squares, although the answer talks about "the new column" and "the new row". Suggested: "Look at the three arrays of squares: 17 rows of 23, 17 rows of 24 and 18 rows of 23. The blue squares are the ones added to the first array."
- **M4.S28.T28.C136** (Let Us Do Q1 question): the text runs the problems together ("(a): 12 × 17: 11 × 18, 6 × 34"); the meaning of "and" (plus) is only explained in the solution. Suggested: "Each box has one problem on top and problems below it. Here 'and' means plus. In each box find which problems below give the same answer as the one on top." The top cells read 1,001 and 1,999 in the LP but 1001 and 1999 in the book (both fine).
- **M4.S30.T30.C147** (Let Us Think (a) to (c)): the text does not say that the answer boxes all have the same colour. Suggested: "In each problem the boxes of the answer are all orange, so they hold one digit; the black boxes can hold any digits."
- **M4.S30.T30.C151** (g to i): "(h): red, green, purple × purple" and "(i): ... × green" do not say that the multiplier is ONE box. Suggested: "(h): a three-digit number (red, green, purple) times a one-digit number (purple) gives 5,999." and the same for (i) with the multiplier green.
- **M4.S30.T30.C150** (steps for (e)): "the top number is 11 and blue" is garbled. Suggested: "the top number is 11 followed by the blue digit".
- **M4.S30.T30.C152** (steps for (i)): "puzzle (i): has no answer" has a stray colon. Suggested: "so puzzle (i) has no answer."
- **Numbering**: the LP names the concepts of Let Us Think Q1 "Q1", "Q2", "Q3" (parts a to c, d to f, g to i) and the book's Q2 "Q4" (C153/C154); the book has only Q1 (a to i) and Q2. Only the labels are affected (book_number fields are right).
- **M4.S31.T31.C155** (The King's Reward): the LP example (two chests, 3 coins doubling and 1 coin tripling for 4 days) is a smaller invented version; the book's task is three choices over 7 days (5 coins x2, 3 coins x3, 1 coin x5: 640, 6,561 and 78,125 coins). No item in chunk E asks the book's own question; check whether another chunk or the LP covers it.
- **M3.S26.T26.C131** (Asher): the book's total 5,018 does not equal the sum of its own rows (5,008); the LP treats this as one of Asher's errors (also true for Pankaj: 92 + 115 = 207, printed 135). It is read as intended, because the exercise is "find the errors".

### Class 5 Ch 6, chunk F
- **M4.S34.T34.C168 (Q2 patterns, question).** The text lists the equations but drops the book's red hint notes. Suggested sentence to add after the four lists: "Hints from the book: beside 15 × 15 = 225 it writes 5 × 5 = 25 and 2 × 1 = 2; beside 25 × 25 = 625 it writes 5 × 5 = 25 and 3 × 2 = 6; beside 11 × 12 = 132 it writes, under Hundreds, Tens and Ones, 1 × 1, 1 + 2 and 1 × 2; beside 11 × 34 = 374 it writes 1 × 3, 3 + 4 and 1 × 4." The book's four boxes have no letters; (a) to (d) are the LP's own and the LP answer uses the same letters.
- **M4.S34.T34.C170 (number pairs, question).** The text has no numbers and no mention that only boxes joined by a line are a pair ("Here are some numbers. ..."). Fine once the diagram is shown after the question text; for any text-only use, add: "The numbers are 8, 35, 75 in the first row, 32, 62, 13 in the second row and 66, 11, 14 in the third row. Two boxes are a pair only when a line joins them."
- **M4.S34.T34.C159 (King's Reward Q2) q_figure hint** describes a strip of empty boxes that the book does not print. Do not rely on it (no change needed, no diagram was made).
- **M4.S33.T33.C162 (Patterns in Products).** `ncert_refs` is `mp.pairs_def`, but the example is the patterns of book Q2 (b) and (c) (65 × 65 and 11 × 36); the pairs/grid is C170. Probably a wrong tag.
- **Concept names versus book numbers in M4.S34.T34.** The concepts are named Q1, Q2, Q3, Q4 (C164, C166, C168, C170) but the book numbers are Q1 (a), Q1 (b), Q2, Q2 number pairs. Only the names differ; not a problem for the diagrams.
- **M4.S34.T34.C165, first step.** "Solve (a): completely: 16 × 44 = ..." has a stray colon; suggested "Solve (a) completely: 16 × 44 = ...".
- **Number style.** The book prints 1111 × 1111, 4489, 9900 without commas; the LP writes 1,111 × 1,111, 4,489, 9,900. No diagram uses these.
- Hint fields (q_figure, s_figure) are otherwise accurate for C168 and C170 (the board and the two circled pairs); the colour words in C171 s_figure were not followed (see Judgement calls).

### Class 5 Ch 7, chunk A
| Concept | What is wrong or missing | Suggested sentence |
|---|---|---|
| M1.S2.T2.C3, C4; M1.S3.T3.C7 (and C9, C11 steps) | "slits" is used for the places across the mat. In the book a slit is a cut: the 8-column mat has 7 slits. | "A mat is 10 places wide." / "The mat has 8 places across (8 columns)." |
| M1.S3.T3.C6 (Q2 question) | The text never gives the size of the mat (8 columns, 8 rows), which is only in the picture and in the solution. | "The mat is 8 columns wide and has 8 rows." |
| M1.S3.T3.C8 (Q3 question) | The text gives no mat size. The solution assumes 16 rows (4 x 4) and the figure uses 16 columns (the book's mat, which has 17 rows). | "Weave a mat that is 16 columns wide and 16 rows tall." |
| M1.S3.T3.C10 (Q4 question) | "any of these designs" has no description, so text alone says nothing about which designs. | "Look at the two designs: design 1 (purple strips on light blue) and design 2 (teal and light tiles)." |
| M1.S3.T3.C11 (Q4 solution) | Step 1 says "over means the colour of the strip shows on top" but design 2 has no paper colour: the rows only fit if the light tile is over. Rows of design 2 are half-tile bands, which is not said. | "In design 2 a light tile is over and a dark tile is under. A row of design 2 is one half-tile band." |
| M1.S4.T4.C12 / C13 (Let Us Try) | The grid size is not given; the book's dot paper (24 x 17 cells) is too short for the 21-row design. The centre bar (3, 5, 3 yellow squares in the middle three rows) is not mentioned. | "Use grid paper at least 21 squares wide and 21 squares tall." and "In the middle three rows there is a bar of 3, 5 and 3 yellow squares." |
| M2.S5.T5.C15 (worked) | "edge to edge" for rectangles of 6 cm and 4 cm: it does not say that equal edges must meet. | "Turn the rectangles so that equal edges meet: 4 cm against 4 cm and 6 cm against 6 cm." |
| M2.S7.T7.C27 (question_tex) | LaTeX: `$(6$-sided shapes with equal sides)` has the opening bracket inside the maths and the closing one outside. | `regular hexagons ($6$-sided shapes with equal sides)` |
| M2.S5.T5.C14 (worked) | "A regular shape has all its sides equal" follows the book's wording; the usual definition also needs equal angles (the book's rhombus has equal sides but is not regular). | Leave as the book says, or add "and all its angles equal" (the three shapes of this example give the same answer either way). |

### Class 5 Ch 7, chunk B
- **M3.S11.T11.C46**, "these triangles" has nothing to refer to in the LP text (the 4 pieces are only in the picture). Suggested: "A rhombus is cut along its two diagonals into 4 equal triangular pieces. What geometrical shapes can you make by fitting 2 of these pieces together? Trace the shapes you created."
- **M3.S11.T11.C48, C50, C52, C54** (rhombus questions 2 to 5) never say what to make the triangles from, while the solutions use the pieces ("Use 2 pieces joined side to side"; C55 uses up to 3 pieces). Suggested additions: C48 "...using the triangular pieces of the rhombus"; C50 "Trace the isosceles triangles you made..."; C52 "Is it possible to make a triangle where all three sides are equal (equilateral triangle) with the pieces?"; C54 "Is it possible to make a triangle where all three sides are unequal with the pieces?"
- **M3.S12.T12.C58**, "cut the equilateral triangle in half" does not name the cut. Suggested: "Now, cut the equilateral triangle in half along the line from one corner to the middle of the opposite side."
- **M2.S9.T9.C32**, step 4 "At every meeting point 2 hexagons and 2 triangles come together" holds for the meeting points inside the pattern, not at its cut edge. Suggested: "At every meeting point inside the pattern ...".
- **M2.S9.T9.C34, C36, C40, C42**, the sample answers give no extent. To match the figures, suggested sentences: C34 "Add 4 more hexagons and the triangles between them (7 hexagons and 25 triangles in all)"; C36 "Put 2 more columns of octagons next to the 4 columns and a small square in every gap between 4 octagons (24 octagons and 15 small squares in all)"; C40 "Continue until the pattern has 9 squares and 23 triangles"; C42 "Make a row of 6 squares, a row of 11 triangles (6 pointing up, 5 pointing down) and a row of 5 squares moved half a square along".
- **M2.S9.T9.C35, C39** (marked points): the question text does not say how many marked points there are or where (C35: the 4 corners of one small square; C39: 5 points); only the figure and the solution say it.
- **Answer concepts with two old cards** (C34, C36, C40, C47, C49, C51, C53, C55, C57, C59, C61 each list IMG1 and IMG2 as old cards; their `text` carries "[Image: ...: solution (continued)]" markers). Per the brief each solution gets exactly one new diagram (IMG1, `before_first_step`); the build must drop the old IMG2 card and the "(continued)" markers.
- **M2.S9.T9.C38** says "a little more than 2 grid steps"; the exact value is 2.236 (square root of 5). Fine as written; "about 2.2 grid steps" would be exact enough.

### Class 5 Ch 7, chunk C
(No LP text was changed; decisions were not changed because of them.)

- **M3.S14.T14.C65 (question), also C73 and C75:** the question does not say which pieces to use. Suggested: "Using 2 of the 4 triangular pieces of
  the rhombus, how many different 4-sided shapes (quadrilaterals) can you make?" (C73 already says "3 triangles from the rhombus"; C75 should say
  "all 4 triangular pieces of the rhombus").
- **M3.S14.T14.C67 and C69 (question):** "these two quadrilaterals A and B" is not tied to the picture. Suggested: add "(the two shapes in the picture)"
  after "A and B".
- **M3.S14.T14.C71 (question):** the grid is not described. Suggested: "In the grid of 43 by 12 squares given below, ...". **C72 (solution):** the
  corner numbers count from the bottom left of each drawing but the text does not say where each shape sits on the grid; the figure puts the shapes
  side by side with origins (3,2), (12,2), (23,2), (34,2). Suggested sentence: "Draw each shape on its own part of the grid; Kite 1 starts at (3, 2), Kite 2 at
  (12, 2), Parallelogram 1 at (23, 2) and Parallelogram 2 at (34, 2), and the corners above are counted from these points."
- **M3.S14.T14.C74 (solution, step 5):** "In all, 3 pieces make 13 different shapes: 2 with 3 sides, 5 with 4 sides and 6 with 5 sides" could not be
  reproduced. Joining 3 pieces side to side along whole equal sides (turning and flipping allowed) I count 9 different shapes: 1 with 3 sides,
  3 with 4 sides and 5 with 5 sides. The number depends on what counts as "different" and on whether sliding is allowed. Suggest removing the count
  or re-checking it. (The three shapes drawn in the diagram are verified.)
- **M3.S15.T15.C77 (question):** "corner A" and "corner B" are defined only by the picture. Suggested: "(A is the bottom-left corner and B the top-right
  corner of the square)".
- **M3.S15.T15.C78 (steps 5 and answer):** "the paper under them shows 2 more triangles" - in the folded kite the 2 other triangles are the uncovered
  parts next to the flaps, not under them. Suggested: "the paper that is not covered shows 2 more triangles". Step 3 says "from the same end of the
  crease" but not which end; the figure uses the end that is the kite's pointed tip.
- **M3.S17.T17.C89 (question):** the four outlines are not named. Suggested: "make a slanted parallelogram, a rectangle, a triangle and a four-sided shape
  with a short top and a long bottom".
- **M3.S17.T17.C90 (steps 5):** "put the parallelogram on the left and the medium triangle on the right" does not say how to turn the parallelogram.
  Suggested: "turn the parallelogram so that its short sides are the top and the bottom".
- **M4.S20.T20.C95 (worked example):** the angle between the two diameters of the first drawing is not given; the figure uses 60 degrees (any angle other
  than 90 degrees gives the same rectangle result).
- **M4.S20.T20.C96 (worked example):** the position of point 1 and the direction of numbering are not stated; the figure puts point 1 at the top and
  numbers clockwise (like the book's circle designs).
- No other LP text problems found in chunk C: C66, C68, C70, C72, C76, C86, C88 steps agree with the geometry (all side lengths, angles and joins were
  recomputed).

### Class 5 Ch 7, chunk D
- **M4.S22.T22.C107 (Circle Designs Ans2):** the question's picture has four extra arcs (the yellow end pieces) and colours; the LP answer only builds five circles. Suggested step after step 4: "To get the yellow end pieces, put the compass point at the far end of each outer circle (the point two radii from the middle) and draw a short arc inside that circle with the same opening."
- **M4.S24.T24.C112 (Cube Connections Ans1):** (a) calls the green square on purple a "diamond"; on the flat net it is a square. Suggested: "a green square on purple (it looks like a diamond in the picture)". (b) Step 5 says "the cross must be on two opposite faces" without a reason. Suggested: "The first and the third view both show the circle face next to a cross face, but with different top faces (purple and brown). On one cube that is only possible if the cube has two cross faces."
- **M4.S24.T24.C113 / C114 (cube frames):** the question text does not say the tunnels run right through; the LP solution assumes it (and the picture of (a) cannot show it). Suggested sentence for the question: "Each cube has a square tunnel going right through the middle of every pair of opposite faces."
- **M4.S24.T24.C116 (Cube Connections Ans3):** the diagram draws the cube as three layers (top, middle, bottom); the text never mentions layers. Suggested first step: "Think of the cube as three layers of 3 by 3 small cubes: top, middle and bottom."
- **M4.S23.T23.C108 and C109 (worked examples):** the question texts do not point to the picture. Suggested: "Look at the two views of the cube." (C108) and "Look at the four layers of the cube." (C109, the diagram numbers them layer 1 to 4).
- **M4.S22.T22.C105 step 3:** "From 15 go on by 10: 16, 17 and on to 24, then 1" is right (10 places, 15 + 10 = 25 = 1) but easy to misread as two moves. Suggested: "From 15 go on by 10 places: 16, 17, ..., 24, 1. So the last line joins 15 to 1."
- **M4.S21.T21.C99 step 1:** "Say the radius is 4 cm, so the diameter is 8 cm" is an example the book does not give; the diagram shows no length. No change needed unless a length is wanted in the picture.
- **M4.S26.T26.C119/C120 (Puzzle):** clue (c) "the two triangles are next to the square" is ambiguous with two squares; the LP resolves it ("the other square") but the question text does not. No sentence suggested (it is the book's wording).

### Class 5 Ch 7, chunk E
- **M4.S28.T28.C124 (Q1)**: the question text does not mention the solids or the picture, but the learner needs to see them. Suggested sentence added after the question: "Look at the picture of the two solids." (The book also says "Use the nets provided at the end of the book to make icosahedron and dodecahedron models"; the LP leaves it out.)
- **M4.S28.T28.C126, C128, C130 (Q2, Q3, Q4)**: same gap; suggested: "Look at the picture of the icosahedron and the dodecahedron." Without it the blanks "Icosahedron: ___ Dodecahedron: ___" have nothing to refer to.
- **M4.S28.T28.C125 (Ans1)**: steps 1 and 2 say "ticking each face once", but a single picture shows only 10 of the 20 icosahedron faces and 6 of the 12 dodecahedron faces. Suggested: add "Turn the solid, or use your paper model, to count the faces at the back too."
- **M4.S28.T28.C129 (Ans3)**: step 1 and step 3 can point at the figure: "Pick one vertex, the one ringed in the picture, ..." so the figure and the text match.
- **M4.S28.T28.C135 (Ans6)**: nothing wrong, but the three models the book shows are never named in the LP; optional sentence: "The book shows an octahedron frame (6 balls, 12 straws), a triangular prism frame (6 balls, 9 straws) and a pentagonal prism frame (10 balls, 15 straws)."
- All numbers in the LP solutions were checked and are mathematically correct: icosahedron 20 triangles, 5 at each vertex, 30 edges; dodecahedron 12 pentagons, 3 at each vertex, 30 edges; 20 x 3 = 60 and 12 x 5 = 60; cube 6 faces, 8 corners, 12 edges, 3 faces at a corner; 8 x 3 = 24 = 12 x 2.

### Class 5 Ch 8, chunk A
- M1.S3.T3.C6 step 1: "Use the 1 kg block as a guide" points to a block that is only in the teaching image of an earlier topic. Suggested sentence: "Think of a 1 kg packet of sugar as a guide: a thing that is heavier than the packet must weigh 1 kg or more."
- M1.S5.T5.C10 question text: the dial faces and needle positions are only in the picture (text holds just the blanks). The question cannot be attempted without M1.S5.T5.C10.IMG1; nothing to add if the figure is kept.
- M2.S7.T7.C15 question text: "You can use the double number line given below" with no line in the text; the figure M2.S7.T7.C15.IMG1 supplies it. Same for M2.S9.T9.C23 ("on which some numbers have been marked").
- M2.S9.T9.C24 check line uses only 7 of the book's 9 ticks; the last two ticks are not mentioned (book gives them no values).
- M2.S11.T11.C30 part (c): the solution writes "10 kg 35 g = 10035 g" right after "10,035 g" in the same step (the book prints 10035 g without a comma). Suggested: "10 kg 35 g = 10,035 g" for consistency (question text too: "10,035 g").
- M2.S8.T8.C17 / M2.S8.T8.C19 hold `q_figure` hints (Shrenu with a scale; none for C19) that describe pictures no longer needed; nothing to change in the text.
- M1.S4.T4.C7 and C8 worked examples say "These are practice values" after the question; the figure shows the same values (5 kg turn / 2 kg turn), so no text change is needed.

### Class 5 Ch 8, chunk B
- **M2.S13.T13.C37** (question): "Complete the double number line below appropriately." carries no data; everything is in the figure. Fine once the diagram is placed (it is required). If the diagram were ever missing, suggested text: "Complete the double number line. 1 g is 1,000 mg, 12 g is 12,000 mg and the 20,000 mg, 25 g and 31,000 mg marks are given. Find the mg at 5 g, the g at 20,000 mg, the mg at 25 g and the g at 31,000 mg."
- **M2.S13.T13.C43** (question): the text still starts "Observe the pictures given below", then narrates the picture. With the diagram this reads well; without it the lead-in would point at nothing. No change needed with the diagram.
- **M2.S13.T13.C39 ... C45 and M2.S14.T14.C47 (numbering vs the book):** LP "Let Us Find: Q3" (C39, goldsmith) is book Let Us Find Q4; LP Q4 (compare) is book Q5; LP Q5 (whale) is book Q6; LP Q6 (quintals) is book Q7; and the LP's "Example 3: the ornament" (C47) is book Let Us Find Q3. Suggested `book_number` labels: C39 "Let Us Find 4", C41 "Let Us Find 5", C43 "Let Us Find 6", C45 "Let Us Find 7", C47 "Let Us Find 3".
- **M2.S17.T17.C54:** "bought several items" is in the book text too; the question only asks about rice. No change needed.
- **M2.S17.T17.C56** (Example 5 question): "How much extra rice did she buy for household use than for the Pongal festival?" has no numbers of its own; they come from Example 4 (2 kg 500 g and 1 kg 750 g) and appear only in the solution. Suggested sentence: "Rathna bought 2 kg 500 g rice for daily use and 1 kg 750 g for the Pongal festival. How much extra rice did she buy for household use than for the Pongal festival?"
- **M2.S16.T16.C51 / C52:** the practice values (3 kg 600 g + 2 kg 700 g; 5 kg 200 g - 2 kg 800 g) differ from the book's Grocery Store numbers (2 kg 500 g and 1 kg 750 g), as the text says ("These are practice values"). Not an error.
- **M2.S13.T13.C46:** answer says "5 tonne" (singular), following the book's blank "_____ tonne". Consistent with the book; plural "tonnes" is used for 8.

All LP arithmetic in chunk B was recomputed and is correct (C36, C38, C40, C42 a-f, C44, C46, C48, C50, C51, C52, C55, C57).

### Class 5 Ch 8, chunk C
- **M2.S22.T22.C84 (Let us do: Q2) and C86 (Q3):** the question text does not mention the double number line the book gives and the learner completes. Suggested sentence: "Complete the double number line: 4 people need 500 g, so 8 people need ___ g (both lines are multiplied by the same number)." (C86: "5 kg cost ₹73, so 10 kg cost ₹___.")
- **M2.S22.T22.C82 (Let us do: Q1):** the table is written as a run-on sentence. Suggested: a LaTeX array as in the `text_alternative` of that item (and of C83 for the answer).
- **M2.S22.T22.C88 (Let us do: Q4):** the question text reads "(a) ... (b): 20 kg iron ... (c): 10 kg plastic" with colons after (b) and (c) only. Suggested: "(a) ... (b) ... (c) ..." with the same punctuation for all three; keep "Make double number lines for answering (b) and (c)."
- **M2.S22.T22.C89 (Ans4):** steps (b) and (c) describe the two number lines in words only. Once the diagram is placed before step 1, suggested wording for step 2: "Look at the double number line for (b): the top line goes from 10 kg to 20 kg."
- **M2.S21.T21.C80:** step 1 says "Draw a double number line" and steps 2-5 refer to "the top line" and "the bottom line" with no picture next to the example. Suggested: add "(see the double number line for this concept above)" or keep the picture decision as optional above.
- **M3.S23.T23.C90:** the question "A cup of juice holds 200 ml or 200 l? A drum of water holds 200 ml or 200 l?" is awkward. Suggested: "Which is right for a cup of juice, 200 ml or 200 l? Which is right for a drum of water, 200 ml or 200 l?" Also step 3 ("A drum holds much more than a cup. 200 ml is a small amount, so a drum holds 200 l") is circular; suggested: "A drum holds much more than a cup, and 200 l is much more than 200 ml, so a drum holds 200 l."
- **All worked blocks (C72, C73, C79, C80, C90):** every question ends with "These are practice values." which a learner reads as part of the problem. Suggested: remove it from the question text.
- **T20 titles "Example 6" / "Example 7":** the book prints these as plain "1." and "2." under More Operations on Weight (no example numbers), and the same two book examples are also the base of the T19 teaching concepts C72/C73 (mul.way / div.way), so the farmer's sacks and the nuts box are covered twice with different numbers. Not wrong, only a possible repetition for the reviewer.
- **T21 C79, C80 and T23 C90 have empty ncert_refs.** They are LP teaching examples, not book items; the book numbers given in `ncert_ref` of the items say where the book treats the idea.

### Class 5 Ch 8, chunk D
- **M3.S32.T32.C124** (Example 10 question): the text omits the data the question needs, the 5 l 300 ml that Sam put in (it exists only in Example 9 and in the book's arrow picture). The LP solution C125 uses it. Suggested sentence: "After refuelling, Sam found his fuel gauge reading 9 l. Sam had put in 5 l 300 ml of petrol. How much fuel did his bike have before refuelling?" (Also: the question writes "refueling", the steps "refuelling".)
- **M3.S26.T26.C103** (containers question): the question text does not describe the containers at all ("the following containers"); the data is only in the picture and the old q_figure hint. It works once the diagram C103.IMG1 is in. Suggested extra sentence: "Each beaker has a scale; the capacity of a beaker is its top mark. Group 1 to Group 4 are shown in the picture."
- **M3.S27.T27.C105** (milkman): "Complete the double number line" lists none of the given ticks; they live only in the picture C105.IMG1. Suggested: nothing to change once the picture is in, but without it the question cannot be attempted.
- **M3.S24.T24.C93** (tea solution), step 3: broken math delimiters, `$150\text{ ml} ($a practice value; ...` has the opening parenthesis inside the math and the rest outside. Suggested: "Take a cup of about $150\text{ ml}$ (a practice value; cups are not all the same). Two cups hold $2 \times 150 = 300\text{ ml}$." The answer_tex has the same pattern: `$(200\text{ ml}$ of water, ...`. Suggested: "Sample answer: about $300\text{ ml}$ in all (with $200\text{ ml}$ of water and $100\text{ ml}$ of milk). No, $1\text{ l}$ is not needed. Yes, $500\text{ ml}$ is enough. Your answer may differ."
- **M3.S31.T31.C118 / C120**: the LP numbering differs from the book. LP "Let Us Compare Q1" is the book's intro line 1 (Kiran's petrol pump) plus item 2 (the table with (a), (b)); LP Q2 is the book's item 3. Only a numbering remark; the text matches the book.
- **M3.S30.T30.C115 / C116, M3.S25.T25.C96 / C97**: these practice examples have no book source (ncert_refs empty or note only); no text problem found.

All sums, conversions and comparisons in the 14 pair solutions and the 4 worked blocks were recomputed and are right (for example C119: 1,500 + 1,800 + 500 + 96 + 125 = 4,021; C121: 5,600 > 5,400, 10,100 > 1,600, 990 > 909, 3,600 = 3,600, 4,050 < 4,500; C125: 9,000 - 5,300 = 3,700).

### Class 5 Ch 8, chunk E
(Listed only; no decision was changed because of them.)

- **M3.S33.T33.C126**: the question text ends with "These are practice values." This looks like a leftover authoring note, not part of the problem. Suggested: delete that sentence.
- **M3.S33.T33.C126**: the block has only plain `question` / `steps` / `text` (units written as "1 l 250 ml", "6 × 1 l 250 ml") and no `question_tex` / `steps_tex` / `answer_tex`, unlike the Let Us Solve concepts. If a diagram were ever added to this block, its token has no `question_tex` to go into. Suggested: add LaTeX versions, e.g. `$6 \times 1\text{ l}\; 250\text{ ml}$`.
- **M3.S33.T33.C126**: `ncert_refs` is "ls.dnl", which is not a book reference (the book has no printed example of multiplying or dividing capacities; the nearest book items are the weight examples on p.9). No `book_number` either.
- **M3.S34.T34.C130 / C131 (Q2)**: the LP solution step (b) says "each glass is filled to its capacity, so 2,880 ml was poured", but neither the LP question nor the book says the glasses are filled to capacity. Suggested sentence for the question: "Each glass is filled up to its capacity."
- **M3.S34.T34.C128 to C137 (Q1-Q5)**: the book's closing line "Use the double number line whenever needed to solve such problems." is not carried by any of these LP concepts. Suggested: add it once as a hint under Q1 (or as a closing line of the topic).
- **Answer concepts C129, C131, C133, C135, C137**: `item_kind` is "unsolved" although they hold the worked answers. Probably a harmless pipeline label; no change needed for diagrams.
- The question and answer concepts repeat the full question text (answer concept's `question` field). That is the LP design, not an error.

All LP solution arithmetic was recomputed and is right: Q1 4,000 and 2,250 ml, difference 1,750 ml; Q2 8 × 360 = 2,880, + 120 = 3,000, 3 × 40 = 120; Q3 5,000 ÷ 250 = 20, 5,000 − 2,500 = 2,500, 20 × 25 = 500; Q4 8,400 ÷ 7 = 1,200; Q5 8 × 1,075 = 8,600; C126 6 × 1,250 = 7,500 and 9,600 ÷ 8 = 1,200.

### Class 5 Ch 9, chunk A
- **M1.S2.T2.C3, C4, M1.S7.T7.C18, C19 (worked examples):** every question ends with "(practice values)", which reads like an authoring note. Suggested: delete the phrase.
- **M1.S5.T5.C14 / C15 (÷ puzzles), question text:** the order of the circles is not stated. The solution (108 / 2 = 54, 54 / 6 = 9) only works with "left circle ÷ right circle = square". Suggested sentence after "This row has the sign ÷.": "In every triangle, the first (left) circle divided by the second (right) circle gives the number in the square."
- **M1.S5.T5.C12 / C14:** the text calls the shapes "triangles" but the book draws them as a small square on top of a trapezoid with two circles; suggested: "puzzle" or "triangle puzzle" with "square" and "circles" as named.
- **M1.S8.T8.C32 (hexagon solution):** the steps use box names A to H ("A ÷ B = C", "A - D = F", "C x E = H", "F + G = H") but the question does not show those letters, and I do not draw letters in the figure (they are not lettered figures). Suggested sentence at the start of step 1: "Call the top boxes A, B, C from left to right, the two middle boxes D (left) and E (right), and the bottom boxes F, G, H from left to right."
- **M1.S8.T8.C31 (hexagon question):** the text says only "the following boxes"; the figure carries which boxes are joined by which sign. Suggested sentence: "Eight boxes are joined by signs: top row ÷ and =, bottom row + and =, a − under the first top box and a × under the last top box, and the two middle boxes each end a column sum."
- **Old card markers:** the `text` fields of C13, C15, C22, C32, C34 carry "[Image: ... solution]" lines in the middle of the steps and "[Image: ... solution (continued)]" after the answer (two old cards each). For C13, C15, C32 the new token goes before step 1 and these markers must go; C22 and C34 have no diagram (their two old cards are dropped), so their markers must go too.
- **M1.S8.T8.C16/C17:** the book question has (a) 30 x 30 with two division statements; the LP answer gives one statement for (a) (900 / 30 = 30) because both numbers are 30; fine, but the LP question does not say that the two statements can coincide. Optional hint, no change needed.
- All arithmetic of the chunk was rechecked (e.g. 150/3 = 50, 4200/100 = 42, 5500/5 = 1100, 5500/10 = 550, 10 x 1100 = 11000, 1800/18 = 100, 6100/10 = 610): no error found.

### Class 5 Ch 9, chunk B
- **M1.S9.T9.C37 / C38 and C39 / C40 (place value charts).** The question text only describes the chart in words. With the decision none (LATEX_TABLE) the table
  itself should be in the text. Suggested for C37: "Now fill the place value chart" followed by a LaTeX array with columns Problem, H, T, O and rows
  `40 \div 10 = | | | 4`, `400 \div 10 = | | 4 | 0`, `4000 \div 10 = | 4 | 0 | 0`, then four empty rows `700 \div 70`, `1400 \div 100`, `220 \div 20`,
  `2200 \div 20`. Suggested for C39: the same array with the six empty rows 110 ÷ 11, 860 ÷ 86, 7500 ÷ 750, 8800 ÷ 88, 2400 ÷ 24, 440 ÷ 22. The solutions (C38, C40)
  likewise: the filled arrays (values are in the `text_alternative` of each item). The book heads the columns H, T, O; the LP says Hundreds, Tens, Ones: pick one.
- **M1.S9.T9.C35 and C36, item (i).** "(i)" is not wrapped in math ($(i)$) while (a) to (h) are. Suggested: `$(i)$: $4000 \div 40 = ...$` in question_tex and steps_tex.
- **M2.S11.T11.C45 to C50 (book numbers).** The LP calls the book's three text boxes "Example 2", "Example 3", "Example 4"; the book prints them as 1, 2, 3.
  This may be on purpose (the LP's own Example 1 is the practice-value worked example C41); if not, `book_number` should read Example 1 to 3.
- **M2.S12.T12.C54 (repeated halving).** The text says "repeated halving works for the divisors 2, 4, 8 and 16", which reads as a complete list. Any power of 2
  works (32, 64, ...). Suggested sentence: "So repeated halving works for the divisors 2, 4, 8, 16 and every other power of 2, such as 32."
- **M2.S13.T13.C57 (Try It! Q2).** The question text does not mention the boxes or arrows (C55's does). With the diagram added this is fine; without it,
  add: "Fill the boxes: each arrow halves the number before it."
- **T10 and T15 worked examples (C41 to C43, C61 to C63).** The question lines end with "(practice values)", which is a build marker rather than text a child should read; consider removing it.

### Class 5 Ch 9, chunk C
- **M2.S16.T16.C66, C70; M2.S20.T20.C84, C86; M2.S21.T21.C90** (field `text`): stale `[Image: ... solution]` and `[Image: ... solution (continued)]` markers sit inside the step text (after step 4 in C66, for example). The old cards are dropped, and nothing replaces them (all `none`), so the builder must strip these markers.
- **M2.S21.T21.C90** (answer): the blanks are listed as "200, 1750, 140 and 4", but the question's blanks come in the order: quotient parts (200 and 4), then 1750, then 140, then the total. Suggested sentence: "The blanks, in order, are $200$, $4$, $1750$ and $140$, and Ibrahim sold $254$ tender coconuts."
- **M2.S21.T21.C91** (question): the number of coconuts is never stated. The question asks for "___ coconuts at ₹20 each" and the solution begins "Ibrahim sold 254 tender coconuts". The number only comes from the previous question. Suggested sentence added to the question: "Ibrahim sold $254$ tender coconuts (from the previous question)."
- **M2.S17.T17.C73** (question): the book frame has one more blank (the remainder 102 under -800) that the LP text does not mention. Not needed to answer; the LP solution gives it ("902 - 800 = 102").
- **M2.S16.T16.C67/C68**: LP is right ("4 bags are needed"); see section 3 for the book's wording.

### Class 5 Ch 9, chunk D
- **Example numbering.** C97/C98 to C103/C104 (book numbers "Example 10 to 13"): the book prints no "Example n" labels; its four examples are numbered 1 to 4 inside "Division Using Place Value". The LP's chapter-wide numbering is the LP author's, not the book's.
- **M3.S23.T23.C97 (question).** "She shows the following way of doing division using place value." The "following way" (blocks and long division) is not in the text. Suggested: "Look at the blocks: 6 tens and 2 ones. Divide 62 into 5 equal parts."
- **M3.S23.T23.C101 and C103 (questions).** The question text already contains the worked steps and results that the solution repeats ("24 Ones ÷ 3 = 8 Ones", "Total 13 Tens"), so the question gives the answer away and the question and solution cards duplicate text. Suggested questions: "324 ÷ 3: divide 324 into 3 equal parts. 324 = 3 Hundreds + 2 Tens + 4 Ones." and "136 ÷ 6: divide 136 into 6 equal parts. 136 = 1 Hundred + 3 Tens + 6 Ones."
- **M3.S24.T24.C105 (question).** "Look at the problems above" does not name them. Suggested: "Look at the four divisions 62 ÷ 5, 75 ÷ 8, 324 ÷ 3 and 136 ÷ 6."
- **M3.S25.T25.C107 (question, part a).** In the book the right-hand place-value layout of (a) is fully filled and is the model for (b) to (d). The LP gives only the quotient digits "1, 1, 7, 2", not the rows (7 - 6 = 1, 10, 43, 12), so the learner never sees the model. Suggested: add the filled layout as LaTeX, or its rows (the text_alternative on C107/C108 gives them).
- **C107, C109, C111, C113 (questions).** The two layouts (partial quotients; place value with Th H T O and the labelled rows) are only described in sentences. Suggested: write them as LaTeX layouts (text_alternative gives the layouts).
- **M3.S26.T26.C115 (question).** The part letter "(i)" is not wrapped in `$...$` like the other letters (formatting). The ten frames are written as prose; an explicit list is clearer.
- **M3.S29.T29.C123 (worked example).** Learner-visible "(practice values)", and two sub-questions with no context. Suggested: "Susie and Sunitha have 94 coconuts. (a) They pack them in bags of 8. How many bags do they need? (b) They share the 94 coconuts equally among 8 customers. How many does each customer get?"
- **M3.S29.T29.C124 (worked example).** Three sub-questions in one sentence, no bill shown, and missing data: "the quantity for a total of ₹990" does not say the price is the same ₹18 per kg (the solution uses 18). Also "(practice values)" shows to the learner. Suggested: "A bill: onions, ₹18 for 1 kg, 45 kg sold. (a) Find the total amount. (b) At ₹18 for 1 kg, how many kg give a total of ₹990? (c) 36 kg of another item cost ₹1260 in all. What is the cost of 1 kg?"
- **M3.S29.T29.C125 (worked example).** "(practice values)" in learner text.
- Solutions C106, C108, C110, C112, C114, C116, C118, C120, C122, C123 to C125: all arithmetic re-computed and correct (quotients, remainders, N = D x Q + R, the place-value digit strings, and all ten Let Us Do answers incl. (e) 848 / 868 and (g) 88 / 44 / 22 / 11). C118 step 1 assumes the first clue is an exact division; the second clue (x 2 = 420) fixes 210 anyway.

### Class 5 Ch 9, chunk E
1. **M3.S31.T31.C147 (Vegetable Market, question).** The question text is only "His naughty grandson has erased some numbers from his record book. Help Munshi Lal complete the table." The table itself (the data of the question) is not in `question`, `question_tex` or `text`; it exists only in the old question card. With the decision `none` / LATEX_TABLE, the table must be written into the question text (item has `needs_lp_text_sync: true`). Suggested sentence plus table, in LaTeX (KaTeX has no `\multicolumn`, so the last row puts the label in the Vegetable column):
   "Munshi Lal's record book for one Saturday is below. Some numbers are erased. Help Munshi Lal complete the table."
   `\begin{array}{|c|l|c|c|c|} \hline \text{S.No.} & \text{Vegetable} & \text{Cost of 1 kg} & \text{Quantity supplied (in kg)} & \text{Total amount} \\ \hline 1 & \text{Radish} & ₹26 & 78 & ₹\underline{\hspace{2em}} \\ \hline 2 & \text{Potato} & ₹20 & \underline{\hspace{2em}} & ₹2{,}240 \\ \hline 3 & \text{Cabbage} & ₹32 & 56 & ₹\underline{\hspace{2em}} \\ \hline 4 & \text{Green peas} & \underline{\hspace{2em}} & 125 & ₹3{,}125 \\ \hline & \text{Total money earned through the sale} & & & \underline{\hspace{2em}} \\ \hline \end{array}`
   (The text of Vegetable Market in the book calls the Peas price column blank and the total row blank: five blanks in all.)
2. **M3.S31.T31.C148 (Vegetable Market, solution).** The steps and the answer line give every value, but no table. Suggest adding the completed table as the first line of the steps: Radish ₹26, 78, ₹2,028; Potato ₹20, 112, ₹2,240; Cabbage ₹32, 56, ₹1,792; Green peas ₹25, 125, ₹3,125; total ₹9,185. (Arithmetic checked: 26 x 78 = 2,028; 2,240 / 20 = 112; 32 x 56 = 1,792; 3,125 / 125 = 25; 2,028 + 2,240 + 1,792 + 3,125 = 9,185.)
3. **M3.S30.T30.C141 (cycle rally, question).** The text has no 344 km / 232 km and does not say that Ratnagiri lies on the way, yet part (b) and the solution ("the map shows 344 km ... and 232 km") rely on them. They are carried by the new question diagram. If you want the text to be complete without the picture, suggested sentence: "On the route, Ratnagiri is 344 km from Mumbai and 232 km from Goa." (344 + 232 = 576, which matches the 576 km.)
4. **M3.S30.T30.C146 (bookshelves, solution).** Steps say "264 / 4 = 66 shelves", "38 shelves", "150 shelves", "30 shelves", "87 shelves" and "the smallest number is 30" while the question's long panels are the shelves of one bookshelf (4 per bookshelf). Suggested wording: "66 bookshelves", "38 bookshelves", and so on, and the sentence "The carpenter can only make as many bookshelves as the scarcest part allows." The numbers themselves are right (264/4 = 66; 306/8 = 38 r 2; 2400/16 = 150; 120/4 = 30; 2800/32 = 87 r 16).
5. **M3.S33.T33.C154 (relations B, solution).** The book prints (c) and (e) as the same 384 / 8, and (f) as 86 / 2, which does not follow from 192 / 4 by doubling or halving. The LP already handles it (answers (e) 48 as (c), (f) 43, and mentions 96 / 2 = 48). If the content team confirms a misprint in the book, the likely intent of (f) is 96 / 2 = 48 (both numbers of 192 / 4 halved); the intent of (e) is not known (a guess is 384 / 16 = 24 or 96 / 4 = 24). Nothing in the diagram specs depends on it.
6. **M3.S30.T30.C132 (Sofia, solution).** Step 1 says "Let the ₹50 notes be a few, from 0 to 10"; suggest "any whole number from 0 to 10". The list of six ways includes 0 notes of ₹50 and 1 note of ₹20 with 10 notes of ₹50; the last step already says the book does not say whether both kinds must be used (if both are needed there are five ways). Arithmetic is right (5a + 2b = 52 gives a = 0, 2, 4, 6, 8, 10).
7. **LP numbering vs the book (no action needed for diagrams).** The LP names the second set Q5-Q10 (C135, C137, C139, C141, C143, C145) while the book numbers them p.14 Q1, Q2, Q3, p.15 Q6, Q7, Q8; Q1-Q4 of p.8 are LP Q1-Q4. The book's p.14 Q4 (six divisions with remainders) and p.8 Q5 are in other topics, not in this chunk.
8. **Arithmetic re-checked, no errors found** in: C128 (250 = 6 x 41 + 4, 250 = 8 x 31 + 2), C130 (342 = 41 x 8 + 14), C134 (417 / 3 = 139), C136 (475 = 45 x 10 + 25; 11 = 2 x 5 + 1), C138 (4,600 / 23 = 200), C140 (15 x 8 / 6 / 4 = 5), C142 (576 / 12 = 48; 232 / 4 = 58), C144 (all values), C152, C154, C156 (all quotients), worked examples C149 and C157.

### Class 5 Ch 9, chunk F
- **M4.S37.T37.C171 (Q4 question):** the question does not name the three choices, so the text alone does not say
  what the cells are. Suggested sentence: "Tick one cell for each statement: Always True, Sometimes True or Never True."
- **M4.S37.T37.C171 `question_tex`, statement (e):** the quote marks are mixed up with the maths: `‘$0’$`. Suggested:
  `‘$0$’ in the Ones place`.
- **M4.S37.T37.C172 (Q4 answer text):** the sentence "This is the plan's reading with whole numbers." in step (b) is
  internal wording; suggested "Here we use whole numbers only." Also the old `text` field has `[Image: ...]` markers
  in the middle of the steps (after step 2) and one "(continued)" marker at the end; under v3 the one token goes before
  step 1 and both markers go.
- **M4.S37.T37.C165, C167, C169 (Q3 a, b, c):** the book's red hints "Always true" (a), "Never true" (b),
  "Sometimes true" (c) are not in the LP question text. Left out on purpose (they give the answer); if the user wants
  them, e.g. "Hint: this statement is always true."
- **M4.S37.T37.C167, C169:** the questions (b) and (c) start without the Q3 lead-in "Think about the following
  statements and find examples as suggested below." (only (a) carries it). Fine as separate cards, but (b) and (c) read
  better with "Think about this statement:" at the start.
- **M4.S36.T36.C163:** the question says "(practice values)", which is odd for the student; suggested: "Decide if each
  statement is always, sometimes or never true." Also the lead "Worked example:" in `text` is fine.
- Maths in the chunk was re-checked and holds: Q1 values 72/72 T, 14/21 F, 16/16 T, 80/90 F, 35/35 T; Q2 blanks 25, 3,
  7, 72; the Q3 sample equations; Q4 (a) to (e) answers.

### Class 5 Ch 10, chunk A
| Concept | What is wrong or missing | Suggested sentence |
|---|---|---|
| M1.S4.T4.C10 | The question sends the learner to "the border of the page", which the learner of the plan does not have. | "Look at the pictures: a diya and a paper boat. Use lines of symmetry to make paper cutouts of the diya, the boat and other designs." |
| M2.S5.T5.C13 | Steps give a dot for the Z (top left) but not for the T; the figure draws the T without a dot. | "T: put a dot at the left end of the bar of the T." (then the figure can draw that dot) |
| M2.S6.T6.C15 | The text does not say what the firki looks like or where the dot is (only the figure shows it). | "The firki has four blades and a green dot on one blade." |
| M2.S7.T7.C17 | "Dots have been marked on it" but not where. | "The H has a dot at its centre and a dot at the top of each of its two sides." |
| M2.S8.T8.C19 | "Fill the table" but the text has no table; the dots are not described. | "Fill the table below. Each letter has a dot at its centre (for the Y, at the bottom of its stem) and small dots that show which way it is turned." |
| M2.S9.T9.C21 | The plus sign has four lines of symmetry (vertical, horizontal and two diagonals); the steps name only two. Not wrong, but incomplete. The figure draws only the two named lines. | "The plus sign has a vertical line, a horizontal line and two diagonal lines." (then the figure would draw the diagonals too) |
| M2.S10.T10.C23 and M2.S10.T10.C25 | The question text does not say the digit 1 is drawn as a plain bar (only the solutions say so). | "In this book the digit 1 is drawn as a plain straight bar." |
| M3.S11.T11.C29 | "one triangle above it, pointing up" does not say the triangle touches the circle, and the direction of the turn is not stated in the question. | "A design has a circle in the middle and one triangle above it, with its flat side touching the circle and its point up. Turn it to the right." |
| M3.S12.T12.C32 | The question text says "the design" without describing it. | "The design has a circle in the middle, a triangle on each of its four sides and a second circle at the tip of the right triangle." |

### Class 5 Ch 10, chunk B
- **M3.S18.T18.C53 (question):** the text does not say that the shapes are numbered; the solution (C54) uses "Shape 1 ... Shape 19". Suggested sentence after the question: "The shapes are numbered 1 to 19 round the border, starting at the top-left corner and going to the right."
- **M3.S13.T13.C38 (question):** "Do these designs" does not say which designs. Suggested: "Look at the green and pink square and at the orange and blue square you coloured. Do these designs have reflection symmetry also? Draw the lines of symmetry."
- **M3.S19.T19.C55 (question):** "Some are shown below." but no picture follows in the LP (decision none). Suggested: "Create symmetrical patterns and designs using vegetable blocks, for example a cut ladyfinger or a carved potato."
- **M3.S14.T14.C40 (question):** "These are provided at the end of the book." the LP has no such pieces. Suggested: "Cut out squares and equilateral triangles of paper, all with the same side length."
- **M3.S14.T14.C41, C45, M3.S19.T19.C56 (solutions):** the closing sentences repeat each other ("Sample answer: ... Your answer may differ." appears as a step and again in the answer line). Suggested: keep one of the two.
- **M3.S18.T18.C54:** the steps for shape 4 and shape 9 say "drawn nearly even"; the diagram draws them exactly regular (see the book notes below). Shape 15 "with a square corner" is true (right angle between the two shorter sides, checked on the drawn coordinates).

### Class 5 Ch 11, chunk A
- **M1.S3.T3.C5 and C7 (questions):** the text never says how long one patch side is, yet the solution counts "one unit of lace for each patch side". Suggested sentence: "Each side
  of a patch is 1 unit long."
- **M1.S3.T3.C7 (question):** starts "She decides ..." with no antecedent once the question is shown alone. Suggested: "Grandmother decides to use two different coloured laces for
  the same quilt. How much lace of each kind will be needed to cover the entire border?"
- **M1.S4.T4.C9 (question) / C10 (solution):** the number of sides (5 and 4) exists only in the picture. In C10 step (b) add: "The two lines cross in the middle, but the crossing
  point is not a corner, so this shape has 4 sides."
- **M1.S6.T6.C16, C18, C22 (questions) and C17, C19, C21 (solutions):** they speak of "Table 1", "Table 2", "Table 3", "Table 4" but no text introduces the four tables. Suggested
  sentence for C16: "The picture shows four tables: Table 1, Table 2, Table 3 and Table 4." (The diagram numbers the tops 1 to 4.)
- **M1.S6.T6.C20 (question):** the solution begins "Look at Table 2" but the question does not mention it. Suggested: "Look at Table 2. Do circles tile? Can we use them to cover a region?"
- **M1.S6.T6.C24 (question):** the LP writes "Maths books"; the book says "Maths textbooks" (minor).
- No place where an LP solution contradicts the book: the tile counts (20, 8, 12), rug 15 x 6 = 90, quilt 15 and 10, desk 9 x 6 = 54, red triangle = 9 green triangles were all
  checked against the page pictures and the arithmetic.

### Class 5 Ch 11, chunk B
- **M2.S12.T12.C51**, steps_tex[2] and text: "`$A 6$ by $3$ rectangle has ...`" has the article "A" inside the maths. Suggested: "A $6$ by $3$ rectangle has $6 \times 3 = 18$ squares and perimeter $6 + 3 + 6 + 3 = 18\text{ cm}$."
- **M2.S13.T13.C55**, steps_tex[4] and text: "`$A 1$ by $8$ rectangle ... $A 3$ by $3$ square`" same slip. Suggested: "A $1$ by $8$ rectangle has area $1 \times 8 = 8$ and perimeter $1 + 8 + 1 + 8 = 18$. A $3$ by $3$ square has area $3 \times 3 = 9$ and perimeter $3 + 3 + 3 + 3 = 12$."
- **M2.S12.T12.C51**: the "18 by 1" strip is longer than the grid printed in the book (15 columns wide). Suggested sentence: "A thin strip standing up, $1$ square wide and $18$ squares tall (the grid is only $15$ squares wide), has $18 \times 1 = 18$ squares and perimeter $18 + 1 + 18 + 1 = 38\text{ cm}$."
- **M2.S12.T12.C48** (question): the size of one patch is not given in the book or in the question; the solution (C49 step 1) assumes "$1\text{ cm}$ by $1\text{ cm}$". Suggested sentence in the question: "Each small square patch is $1\text{ cm}$ by $1\text{ cm}$."
- **M1.S10.T10.C43** (question): "Put them on a square grid" gives no grid; the grid (15 x 18 squares of 1 cm) is printed only under the previous question. Suggested: "Put them on the square grid of $1\text{ cm}$ squares above and find their area."
- **M1.S9.T9.C34 steps_tex[1], C36 steps_tex[5], C38 steps_tex[1] and [5]** (and C38 answer_tex): the letter A is written outside the maths ("So A covers more", "count A row by row", "A covers $3$ columns", "Yes. A covers ...") while B and C are in `$...$`; make it `$A$`.
- **M1.S9.T9.C32, C36, C38 answer_tex:** "`$12\text{ unit}$ squares`" splits "unit squares" between maths and text; suggested "$12$ unit squares".
- **M2.S14.T14.C59**: the question "Tick the shapes with the same perimeter" has two groups (12 cm and 16 cm) and the answer ticks all five. Suggested answer sentence: "Tick $(a)$ and $(b)$ (perimeter $12\text{ cm}$) as one pair, and $(c)$, $(d)$, $(e)$ (perimeter $16\text{ cm}$) as another."
- **M2.S15.T15.C60**: the book's own example is 6 rows of 4 patches (24 patches, 6 x 4 cm), the LP example is 5 rows of 8 patches (not an error, a deliberate change); the diagram follows the LP. Likewise the LP's C61 (11 x 4) and C62 (7) replace the book's 6 x 4 and 5 x 5 teaching figures.
- Question texts of C31, C33, C35 carry no data of the rectangles (their proportions live only in the figure), which is why the figure is required. Nothing else was found missing; every LP solution number I recomputed was correct.

### Class 5 Ch 11, chunk C
- **M3.S22.T22.C89** question 'Find the perimeter of the tiles.': the tile side is not given in words (only the figure says 1). Suggested: "Each side of a tile is 1. Find the perimeter of the tiles."
- **M3.S22.T22.C91** question: neither the starting figure nor the die is named ("the same figure"). Suggested: "Look at the 5 tiles and the die, which shows 6. Take turns and add tiles to the same figure till the perimeter becomes 24. The one who makes the perimeter 24 wins the game."
  Also the solution (C92) step 1 starts from the 4 tiles of the earlier step, while the question figure shows the 5-tile figure of step 4: either start step 1 from the 5 tiles ("perimeter 12") or let the question say the figure was made in the earlier steps.
- **M2.S17.T17.C72** question says 'sides are 5 units long' but the solution answers in 'square cm' and 'cm'. Suggested: "a square whose sides are $5\text{ cm}$ long" (the book's picture is marked 5 cm).
- **M2.S17.T17.C71** solution: "The length of one side is 6 and the other side is 4, so Area = Length x Breadth = 6 cm x 4 cm" does not say which is which, while the book picture puts 'Breadth' beside the 6-patch side
  and 'Length' under the 4-patch side. Suggested: "The breadth is 6 (6 rows) and the length is 4 (4 patches in a row), so Area = Length x Breadth = 4 cm x 6 cm = 24 square cm."
- **M2.S19.T19.C77** worked example: "Its height is marked in two parts, 5 cm and 7 cm" does not say which part is on top, the solution does ("upper part 20 x 5, lower part 20 x 7"). Suggested: "...in two parts, 5 cm at the top and 7 cm below it."
- **M3.S22.T22.C90** solution counts 3 + 1 + 2 + 2 + 2 = 10 (step 5 includes the right edge of the lower tile); this is right, and it is the edge the book forgot to label (section 4). No change needed.
- **M2.S18.T18.C75** lists seven rectangles; the first Example (6 x 4 = 24 patches) is also an earlier rectangle and is not listed (not wrong, just not covered).

### Class 5 Ch 12, chunk A
- M1.S3.T3.C6, C8, C10 (Let us find out Q1 to Q3): the question text never mentions the clocks, and gives no time. Suggested sentence to add
  before the question: "Two clocks show the time before Raghav's yoga (first clock) and after his yoga (second clock)."
- M2.S8.T8.C28 and C30 (School Race): the question text does not give the three times (01:55, 01:56, 01:57) that exist only in the picture.
  Suggested sentence: "On the winners' stand the boards show 01:55 on stand 1, 01:56 on stand 2 and 01:57 on stand 3, in minutes and seconds."
  The names Akira, Sunita and Mary cannot be matched to stands (the book does not say; C31 already states this).
- M1.S3.T3.C14 (Q5): the text says "The table below shows ..." but the table is not in the text (the data is written as a sentence). With the
  diagram `none`, the table must be written in the text: suggested "Name | Time Taken: Raghav | 1 hour 20 minutes; Rani | 2 hours 10 minutes;
  Ritu | 1 hour 35 minutes".
- M1.S5.T5.C19 (Q6): the table wording "12-hour format and 24-hour format: 05:30 a.m. = 05:30 hours; ..." reads as equations; with `none` the
  question needs the LaTeX table of text_alternative so the blanks are visible as rows.
- M1.S5.T5.C21 (Q7): the two lists are in the printed order inside one sentence; with `none` they should be two lists or a two-column
  table so the learner can see the columns.
- M2.S9.T9.C32 (Let Us Do): the book table has Seconds and Minutes columns to tick; the LP text lists only the activities. With `none` the
  table (or "answer Seconds or Minutes for each activity") needs to be in the text.
- M2.S10.T10.C35: `answer_tex` lists four sample events, step 5 lists five ("a bell ringing once" is added) and step 3 also mentions "a ball dropping
  to the floor". Harmless for a sample answer, but the answer line and step 5 do not match.
- M1.S6.T6.C23 (Nana ji): "How long did he take to reach his house?" is the book's own wording (it means Nana ji's house); the LP copied it.
  Suggested: "How long did he take to reach his Nana ji's house?"
- M1.S3.T3.C13 and M1.S4.T4.C17 etc.: no mistakes found in the arithmetic of any chunk-A LP solution (27 min, 5 h, 2 h 15 min; 80, 130, 95
  min; 19:45 hours, 04:20 p.m.; 2 h 35 min; 08:35 a.m., 11:55, 17:30, 21:35; 20:45, 23:45, 19:30, 06:30, 04:30, 01:30; 108 s, 4 s; 115, 116,
  117 s; 8 and 2 ticks) - all recomputed.

### Class 5 Ch 12, chunk B
- **M2.S13.T13.C60 and C62 (solution `text` field):** the `text` still contains the old card markers "[Image: Let us do: Ans7: solution]", "[Image: ... (continued)]" (and the same for Ans8) between the steps, because these answers had two cards (IMG1, IMG2). The new plan has ONE solution diagram per answer, placed before the first step. Suggested: remove both marker lines from `text` (the build should regenerate `text` from the steps) so no stray marker is left.
- **M2.S13.T13.C51 (Ritu, observe Q3), steps_tex:** suggested extra sentence after step 2 so the picture and the words agree: "The minute hand in the right clock has also moved on by one mark, because the seconds hand has just finished a minute."
- **M2.S13.T13.C55, C57, C59, C61 (questions):** the question text does not say that the LEFT clock shows the starting time of the activity; the figure carries it. No change needed if the question figure is always shown; suggested sentence if you want the text to stand alone: "The clock on the left shows when the activity began."
- **M2.S13.T13.C47, C49, C51, C53 (questions):** same point: "The clock on the left shows the start and the clock on the right shows the end."
- **M2.S12.T12.C45 (worked example):** the question asks "what happens to the minute hand?" but gives no minute-hand position; the answer ("moves on by one mark") works without one. Fine; mentioned because the picture shows a seconds hand only.
- `q_figure` / `s_figure` hints in the units are not LP text; for the record, C49's hint "hour hand on 4" and C61's hint "minute hand on 12" on both clocks differ from the specs for the reasons in section 2.
- Book numbering: the LP calls the draw-the-hand questions "Let us do: Q5 to Q8" (concepts C55-C61) but the book numbers them 1-4 on p.160, and the `book_number` fields say "Q1..Q4 (drawing the seconds hand)". Consistent enough; just a note for anyone matching by number.

### Class 5 Ch 12, chunk C
- **M3.S15.T15.C68 (Q1b question text):** "You can use the above double number line" - in the LP the number line sits two cards earlier (C66 / C67), not directly above. Suggested sentence: "Do as instructed. You can use the double number line of the previous question for the following conversions." (Only a wording point; no decision depends on it.)
- **M3.S15.T15.C66 / C70 (question text):** the text lists the labels in tick order but says nothing of the arrows or that the ticks are not evenly spaced; the figure carries that. If the figure were ever missing the learner could not place the blanks. No change needed once the diagram is in.
- **M3.S15.T15.C67 steps:** step 2 says "The x 2 arrow joins 1 hour to 2 hours", which matches the figure; no step names the unlabelled left and bottom arrows. Not an error.
- **M3.S15.T15.C71 steps:** "The x 5 arrow joins 1 minute to 5 minutes" matches the figure. Fine.
- I recomputed every LP answer in this chunk: Q1a (2, 8, 11, 12 hr; 240, 420, 540 min), Q1b (70, 165, 195, 260 min; 1 h 15, 2 h 30, 3 h 40, 6 h 30), Q1c line (2, 20, 25 min; 300, 600, 900 sec), Q1c conversions (5 min 20 sec, 3 min 45 sec, 11 min 40 sec, 16 min 40 sec, 613, 248, 940 sec), Q2 (3 h 20 min), worked examples (05:10 p.m., 05:35 p.m., 02:10 p.m., 04:00 a.m. next day) and Q4 to Q10 (08:00 PM, 08:30 PM, 12:40 PM, 07:30 PM, 06:40 PM, 01:05 PM, 05:00 AM next day). All are correct and agree with the book text. No missing data found.

### Class 5 Ch 13, chunk A
- **M1.S5.T5.C11** - the question text does not say what the given array is (3 rows of 5, 3 x 5 = 15, with 3 and 5 as factors, 15 as the multiple); the new picture carries it. Suggested sentence: "The picture shows an array of 15 tiles in 3 rows of 5, so 3 × 5 = 15." **M1.S5.T5.C12**, step 1: "The array in your maths book" should read "The array in the picture".
- **M2.S9.T9.C28** - the question text does not say the road ends at stone 64 (only the picture and the solution step 1 say so). Suggested sentence: "The stones of the road are numbered 0 to 64 and the food is at the end of the road, after stone 64."
- **M2.S8.T8.C22** - "You can continue the number line" has no number line in the text. Suggested sentence: "The number line shows a rabbit jumping 4 at a time and a frog jumping 3 at a time from 0; they first land together on 12."
- **M1.S3.T3.C5 / C6** - "this box" refers to the picture only. Suggested sentence: "A box multiplies every number that goes in by the same hidden number." (the four out-numbers are already in the text).
- **M2.S8.T8.C23** - the LP answer lists "24, 36, 48, 60"; the picture stops at 48 (60 is named in step 4). Fine, but the answer line could say "(the line stops at 48)" if the reader looks for 60 on the picture.
- **M1.S6.T6.C18** - the earlier card hint (s_figure) described only the arrays of 54; the answer covers nine numbers (see judgement call on C17 / C18).

### Class 5 Ch 13, chunk B
- **M2.S12.T12.C43, C45, C47 (questions):** the text says "his friends" and "he" with no antecedent and no trail. Suggested: "Mowgli's friends live along the trail above. Which of his friends will he be able to meet if he jumps by 3 steps? 3 is a common factor of the numbers ___." (same for 5 and 10; for C45/C47 "Which numbers will he touch if he jumps by 5 steps? ___ ").
- **M2.S11.T11.C39 (question):** the numbers to test are missing from the text (only the picture has them). Suggested: "Find which of the following numbers can be reached by jumps of 4 steps: 0, 10, 16, 27, 36, 48. 4 is a common factor of the numbers ___."
- **M3.S14.T14.C58 (question):** the text lists the 15 numbers but never says they are sorted into the three circles. Suggested: add "Write each number in the right part of the three circles."
- **M2.S11.T11.C34 / C44:** the LP answers (ant, frog, bird, Baloo, rabbit for jumps of 2; spider, frog, Kaa, Baloo, deer, monkey for jumps of 3) are correct. The book's own sentences are shorter: p.5 names only 4, 12, 14, 50 for jumps of 2 and only 9, 21, 39, 57 for jumps of 3 (it leaves out Baloo 30, and 12 and 30). The LP is right; no change needed.
- **All pair solutions (cards removed):** the old `text` fields still carry `[Image: ... solution]` and `[Image: ... solution (continued)]` markers inside the steps (for example after step 3 of C34). The v3 token goes before step 1 in steps_tex; the builder should drop the old markers.
- **M3.S14.T14.C56 (question):** "What number of jumps (in steps) he could choose" is the book's own wording; the LP keeps it. Fine, only awkward.
- **M2.S11.T11.C42 (Q7):** the LP numbers the nine pairs (a) to (i); the book prints (f) twice (12 and 15, then 20 and 5), (g) 9 and 21, (h) 6 and 27. The LP's lettering is the correct one.

No arithmetic error was found in the LP solutions of this chunk (all factor lists, multiples and sort lists re-checked).

### Class 5 Ch 14, chunk A
- **M1.S3.T3.C7** (question): the text "Which way is west?" has lost the context; it should say who faces what. Suggested: "Manu is facing the rising Sun. Which way is west?" (with that sentence the figure becomes optional; the decision above follows the text as it is now).
- **M1.S3.T3.C5** (question): does not say that Manu stands with both arms stretched out to the sides, seen from behind (only in the book picture). Suggested: "Manu stands with both arms stretched out to the sides. He is facing the rising Sun. ..."
- **M1.S6.T6.C16** (question): the text does not say that a picture of a room is shown. Suggested: "Look at the picture of the room. Write the directions of the following in relation to the girl."
- **M1.S6.T6.C17** (solution, steps 4 and 5): the cupboard is on the back wall at about the girl's own depth (she stands in front of a table that is against the back wall), so "a little behind her" overstates; the bedside table is at the front right corner, far to her right (about 40 percent of the picture width) and clearly in front: it sits between south and east. Suggested step 5: "Bedside table: it is the round table at the front right corner, in front of her and to the right, between south and east, so name south or east. Your answer may differ." (the answer line says south).
- **M1.S6.T6.C21** (solution): "In the sample room the bed is there" refers to a sample room that appears only in C19's solution. Suggested: "In the sample room of the last question the bed is there."
- **M1.S6.T6.C19 / C21 / C13 / C17 / C26 / C28** (`text` field): the old card markers `[Image: ...: solution]` sit in the middle of the steps and again after the answer ("(continued)"); v3 puts the token before step 1 and nothing after the answer, so the builder must clear these markers.
- **M2.S7.T7.C22** (question): "What is just south of the Basketball Court, across Market Road ...?" does not name the map. Suggested: "On the street map of the zoo trip, what is just south of the Basketball Court, across Market Road, and what is just north of it?"
- **M2.S8.T8.C25 / C27** (question): the sentence "The street map shows the bus route with dotted lines" of the book is not in the question text; the figure carries the route. Optional addition: "Look at the street map and its red dotted bus route."
- **M1.S5.T5.C12 / C14** (question): the text does not say "in the picture of the camp". Suggested: "Look at the picture of the bird-watching camp. ..."

### Class 5 Ch 14, chunk B
- **M2.S13.T13.C54**, first block: "A sample map and its key are given below. Gate, Road, ..." refers to the book's school sample map, which the plan does not show (the teaching image is a library corner).
  Suggested: "Here is a sample map of a library corner and its key." or show the school sample.
- **M2.S14.T14.C57** (steps and answer): the sample map has a school wall (the gate is "in the west wall") but the key lists no wall; suggested: add "wall" to the key sentence and the key box, or
  say "the boundary line".
- **M2.S12.T12.C51 / C53** (and C50 / C52 questions): routes A, B, C are named only in the answer of the first question (C47); the questions of (c) and (d) do not define them. Suggested first step of C51: "Use
  the three routes A, B and C of the first question."
- **M2.S12.T12.C51**, Route C: "3 stations from Qutb Minar to Hauz Khas" includes Hauz Khas, while Route A counts Hauz Khas on its own ("(2), Hauz Khas (1)"). The total 25 is right. Suggested: "2 stations from
  Qutb Minar to Hauz Khas, Hauz Khas (1), 4 on the Magenta Line to Kalkaji Mandir, ..." giving 2 + 1 + 4 + 1 + 7 + 1 + 5 + 1 + 1 + 1 + 1 = 25.
- **M3.S16.T16.C61** question text: "To get to the laddoos" has no sentence saying that the ant and the laddoos are on the grid shown; the figure carries them, so the question diagram is required.
- No missing data was found for the street map items; all LP routes follow roads of the book picture (checked against the road bands).

### Class 5 Ch 14, chunk C
- **M3.S17.T17.C69 (Q4 question)**: "Identify other routes to reach the point where apple is located." gives no start point; the ant is only in the picture. Suggested: "Identify other routes from the ant to the point where the apple is located. Which one is the shortest?"
- **M3.S17.T17.C70 step 5**: "The route drawn in your maths book is 5 cm south, 3 cm east and 2 cm north." The learner sees the route in the figure, not the book. Suggested: "The route drawn in the figure is 5 cm south, 3 cm east and 2 cm north."
- **M3.S17.T17.C63, C65, C67, C69 question texts** never mention the grid, so the figure placed after the text has no sentence pointing to it. Suggested first sentence for each: "Look at the grid." (optional).
- **M3.S21.T21.C84 (Q3 question)**: "Place dots of different colours on the following positions." does not say on which picture. Suggested: "Place dots of different colours on the following positions on the zoo map."
- **Second old solution cards**: C66, C68, C70, C75, C77, C79, C81, C83, C85 each have two old solution cards (IMG1 and IMG2) and the text holds two "[Image: ... (continued)]" markers; the new plan has one solution figure at the start of the steps, so the IMG2 card and both in-text image markers should go in the build.
- **M3.S18.T18.C72 step 3** says (9,8) "is a spot on the path". True on the book picture (the east road arm at row 8) and true on the spec (which keeps roads); it would be false if a renderer drops the roads.
- **M3.S19.T19.C75 steps 2 and 3** say "one step horizontally towards the east ... one step up, towards the north": consistent with the book; no issue, listed only because the figure draws exactly this walk.

### Class 5 Ch 15, chunk A
- **M1.S3.T3.C5 (Q1)**: the question text never gives the table rows. Suggested: add the empty table as LaTeX with the rows 1/2 hour, 1 hour, 1 1/2 hour, 2 hours, More than 2 hours and a blank No. of Children column (the array is in the item's `text_alternative`).
- **M1.S3.T3.C7, C9, C11, C13 (Q2 to Q5)**: the questions say nothing of the data they need; the student must read the table filled in Q1. Suggested: add the filled table as LaTeX (1/2 hour 9, 1 hour 13, 1 1/2 hour 7, 2 hours 3, More than 2 hours 3), or the sentence "Use the table you filled in the first question." Without this the dropped old cards leave these questions with no data.
- **M1.S7.T7.C28**: "passing her house" has no "her" in the question; suggested "passing Deepti's house".
- **M1.S7.T7.C29 and later two-wheeler solutions**: step 1 of C29 says "Icon box"; in the book the key sits in the table header (the shop pictograph has a real icon box). Suggested "Key" for the two-wheelers.
- **M1.S7.T7.C37 step 5**: "The scales 1, 2, 4 and 12 fit too" leaves out 3 (the book's scale) and 6 (the one drawn); fine as "too" but could read "The scales 1, 2, 3, 4, 6 and 12 all fit."
- **Solution `text` fields (all pair answers)** still hold old markers such as "[Image: ...: solution]" and "[Image: ...: solution (continued)]" in the middle of the steps; they should be removed when the new token goes before step 1.

### Class 5 Ch 15, chunk B
- **M2.S9.T9.C41, C43, C45, C47, C49 (questions Q1-Q5):** the texts never say whose data they use, and Q4 says "they". Suggested sentence to add at the start of each: "Raman recorded his day in a table and Sheela in a bar graph (see the picture)."
- **M2.S10.T10.C52 (worked example):** the pencils have no names, but the figure needs them. Suggested sentence: "Samaira measures three pencils: Pencil 1 is 9 cm, Pencil 2 is 6 cm and Pencil 3 is 4 cm." The diagram uses Pencil 1, 2, 3 in that order (from the teaching image).
- **M2.S8.T8.C39 (worked example):** the vertical scale of Samaira's graph is not stated. The diagram uses 0 to 6 (as in the teaching image). Suggested sentence: "Samaira's graph has its vertical line marked 0 to 6."
- **M2.S13.T13.C68 (worked example):** the vertical scale and the graph title are not stated. The diagram uses 0 to 7 and the title Newspapers (kg) (from the teaching image). Suggested sentence: "The bar graph is called Newspapers (kg) and its vertical line is marked 0 to 7."
- **M2.S12.T12.C60, C62, C64, C66 (questions 2-5):** the question texts give no data; the sample strips (Mine 6, Friend 1 7, Friend 2 5, Friend 3 8, Friend 4 6 cm) appear only in the solutions, so a learner who has not made strips cannot attempt them. Suggested sentence: "Use the sample graph: Mine 6 cm, Friend 1 7 cm, Friend 2 5 cm, Friend 3 8 cm, Friend 4 6 cm."
- **M2.S12.T12.C66 (question 5):** "It belongs to ___." has no antecedent ("it" = the smallest index finger). Suggested sentence: "The smallest index finger belongs to ___."
- **M2.S11.T11.C54/C55:** the book leaves two table rows unnamed; the sample answer names them Playing and Other activities, but the question text does not say so. Suggested sentence in the question: "Use the two empty rows for playing and other activities."
- **M2.S12.T12.C58:** "the given bar graph" is not in the LP text; the diagram supplies it (no LP change needed once the figure is added).
- LP numbering differs from the book's: LP "Whose Index Finger is Longer?: Q1" is the book's strip activity; LP Q2-Q5 are the book's questions 1-4. Harmless.

### Class 5 Ch 15, chunk C
- **M2.S14.T14.C70, C72, C74, C76, C78, C80 (Food Wastage Q1 to Q6):** the question text never mentions the graph and gives no data; it only works with the picture. Suggested opening sentence for each: "Look at the Food Wastage bar graph." (C70: "Look at the Food Wastage bar graph. Which food item had the highest amount of wastage? ___"). Q4 (C76) uses the total of Q3, so "Use the total wastage from the bar graph." fits there.
- **M3.S16.T16.C85 (True or False answer 1), step 4:** "the girl in the front row with a cap and no glasses" fits two girls (front row 3rd and 6th). Suggested: "For example, the third girl from the left in the front row has a cap and no glasses."
- **M3.S15.T15.C82 worked example:** the question does not say which children have hats or flags (only the counts); the new diagram shows it. Optional sentence if the author wants the text to match the picture: "The first two children have a hat and a flag, the next two a hat only, the next three a flag only and the last two neither."
- **M2.S14.T14.C79 and C81 (also M3.S16.T16.C99):** the old `text` field has "[Image: ...]" lines inside the steps and after the answer, and the concepts list two old solution cards (IMG1, IMG2). The new plan has one solution diagram per answer (IMG1) before step 1; the build must drop the old slots (nothing to change in the step wording).
- **M3.S16.T16.C92, C94, C96, C98 (statements 5 to 8):** `q_figure` hint missing (the first four have it). Hint only, nothing to fix.
- The question texts of M3.S16.T16 use "the picture" with no picture in the text; this is fixed by the new question diagrams (no wording change needed).

### Class 7 Ch 15, chunk E
(No LP text was edited; suggestions only.)

- **C138, C140, C142, C144, C146, C148, C150, C152, C154 (boxes 1 to 9) and C156 (Q11 a, b, c): the steps are packed on one line.** The question_tex
  joins the printed lines with semicolons ("Box 1: 4x + 6 = 10; 4x = 10 + 6; 4x = 16; x = 4. ..."), but the solutions say "line 2", "line 3",
  "the last line", "line 5", which is hard to find in a run-on sentence. Suggested form (box 1):
  `Box $1$ (each line is one step):` followed by
  `\begin{array}{l} 4x + 6 = 10 \\ 4x = 10 + 6 \\ 4x = 16 \\ x = 4 \end{array}`, one array per box, and for Q11 one array per part (a), (b), (c).
  This is also why no picture is needed: a one-step-per-line array reproduces the book's box.
- **C143 (box 3 solution), wording.** "Mistake in line 2: the factor 2 was taken away by subtracting 2, and only from one term." The student's line 2 is
  `v - 4 = 6 - 2` (2v became v, and 2 was subtracted from the right side only). Suggested sentence: "Mistake in line 2: the 2 in 2v multiplies v, so it cannot
  be removed by subtracting 2 from the right side; either divide the whole of both sides by 2, or move -4 first."
- **C158 (ancient notation) steps, step 3 and 4.** The dot is only described in words. Suggested for step 4: "... written as yā 3 rū 4 with yā 2 rū 8 below it
  (this 8 is positive, so it has no dot): the two sides one below the other." (With the new diagram this is also visible.) If the team prefers text only,
  `yā\ 2\ r\bar{u}\ \dot{8}` in LaTeX does give a dot over the 8.
- **C160 step 4.** "the same as in Jahnavi and Sunita's savings" refers to Example 9 (m = 7, p.13-14); correct, but the learner may not remember it. Optional
  suggestion: "... m = 7, the same answer as Example 9 (Jahnavi and Sunita's savings)."
- **C170 blocks 0 to 3** are authored examples with no book number (`lp_book_number` null). Nothing wrong; noted because the items have no book reference.

Checked and found correct (recomputed): boxes 1 to 9 solutions (x = 1, z = 1/4, v = 5, z = -3, w = 26/11, x = -13/3, q = 21/8, x = 5/2, y = -3/16, each with the
LP check), Q11 (a) x = 19/2, (b) no mistake y = 6/7, (c) x = -13/5 with check -77/5 on both sides, Example 16 (100, both sides 900), Q1 of the Pinch of History
(2 and 10, checks 14 and 24), 2x + 3 = 4x + 5 (x = -1), Bakhshali (a = 4, 4 + 8 + 24 + 96 = 132), Summary examples (12, 4, 6, 12) and the magic trick (always 8, own trick always 4).

### Class 8 Ch 1, chunk A
Not edited and no decision changed because of them (user decision 2).
- `M2.S7.T7.C31` (question) and its echo in `C32`: option (v) reads "15625 + 512" but the book prints "15625 + 51²" (superscript 2; pdf p.10 and p.20). Suggested: "(v): $15625 + 51^2$". The separators are also uneven: "(ii): $15625 + 26^2$ (iii): ..." has no semicolon before (iii). The LP answer (iv) 15625 + 251 is right.
- `M2.S10.T10.C41` (question): it never mentions the dot pictures, although the book question and the required diagram do. Suggested: "Look at the pictures: $1 + 3 = 4 = 2^2$, $3 + 6 = 9 = 3^2$ and $6 + 10 = 16 = 4^2$. Draw the next term: add the next pair of consecutive triangular numbers after $6$ and $10$ and check that the sum is a square." Its `q_figure` hint is also wrong: it says the picture shows triangles of 1, 3, 6 and 10 dots with the sums beside them; the question picture is the three dot SQUARES each cut into two triangles.
- `M2.S10.T10.C42` (solution): the steps never refer to the picture. Suggested first step (after the figure): "The $5 \times 5$ square of dots splits into a triangle of $10$ dots and a triangle of $15$ dots."
- `M2.S10.T10.C39` (question): the LP asks only for the squares between 101 and 200 and the largest square below 1000. The book asks to enter the number of squares in each of ten blocks of 100 (1-100 ... 901-1000) first. If full coverage of the book question is wanted, add: "Complete the table of the number of squares in each block of $100$, from $1$-$100$ to $901$-$1000$." (a LaTeX table).
- `M2.S5.T5.C24` (answer): `answer_tex` is "(ii): $108^2$ and (iii) $292^2$" (a colon after (ii) only). Suggested: "(ii) $108^2$ and (iii) $292^2$". The question text of C23 also has "(i): ... (iv): ..." with colons; harmless.
- `M2.S8.T8.C33` / `C34`: `book_number` is "Figure it Out, Q1" but the book's number is Figure it Out Q8 (ncert_ref `FiO1.q8`). The other Figure it Out items of this chunk are labelled "Square Numbers, Q2/Q3/Q7", so the same exercise carries two label styles; only the ids matter for the build.
- Mathematical checks (all hold): C2 12 has 6 factors; C7 36 has 9 factors; C12 (3/5)² = 9/25, 2.5² = 6.25; C18 31² = 961, 39² = 1521; C20 34² = 1156; C22 3000² = 9000000 (6 zeros); C24 and the book agree on 108², 292²; C25 1+3+...+15 = 64; C26 chain ends 2 - 13 = -11; C30 71 and 1296; C32 251 and 15876; C34 16+25+400 = 441 = 21² and 81+100+8100 = 8281 = 91²; C40 121, 144, 169, 196 and 31² = 961 < 1000 < 32² = 1024; C44 2 x 16 = 32, 2 x 99 = 198. No LP solution contradicts the book's printed answer.

### Class 8 Ch 1, chunk B
No LP text was changed. All sums in the LP solutions were recomputed and hold (21^2 = 441 to 24^2 = 576, 324 = 2 x 2 x 3^4 = 18^2, 156 = 2 x 2 x 3 x 13, 1156 = 34^2, 2800 = 2^4 x 5^2 x 7, 180 and 900 for 4, 9, 10, 9408 = 2^6 x 3 x 7^2 and 28224 = 168^2, 2025 = 45^2, 44^2 = 1936 and 45^2 = 2025, 225 and 256 with gaps 6 and 25, 121 and 144, 2025 and 2116, 1024 and 1089, 8, 27, 64, 125 to 729, 99^3 = 970299). Cosmetic and labelling issues only:

| Concept id | What is wrong | Suggested sentence |
|---|---|---|
| `M2.S15.T15.C62`, `C63` | `book_number` says "Figure it Out, Q1" but this is NCERT Figure it Out (1.1) Q6 (9408). Other items in the same plan use the true number ("Square Numbers, Q4", "Q5", "Q1"). | "Figure it Out, Q6" (or "Square Numbers, Q6") |
| `M2.S15.T15.C64`, `C65` | `book_number` says "Figure it Out, Q2" but this is NCERT Q9 (tile picture). | "Figure it Out, Q9" (or "Square Numbers, Q9") |
| `M3.S19.T19.C81` | `answer_tex` is `$8$, $27$ and $64\text{ unit}$ cubes`: the word "unit" is inside the math part and "cubes" outside. | `$8$, $27$ and $64$ unit cubes` |
| `M3.S19.T19.C80` | `question_tex` has `$4\text{ units}$`: the unit is inside the math part. | "cubes of edge $2$, $3$ and $4$ units" |
| `M2.S17.T17.C74`, `C75` | Stray colons after the part labels: "(i): $2032$; (ii): ..." and the answer "(i): $2032$, (ii): $2048$ and (iii) $1027$" (the third label has no colon). | "(i) $2032$ (ii) $2048$ (iii) $1027$ (iv) $1089$" and "(i) $2032$, (ii) $2048$ and (iii) $1027$ are not perfect squares; $1089 = 33^2$" |
| `M3.S19.T19.C84`, `C85` | Same stray colons: "(i): The cube ...", and "(i): False: ..." with a double colon in every step. | "(i) False: odd x odd x odd is odd, for example $3^3 = 27$." |
| `M2.S11.T11.C45` (worked example) | Text says "the square roots of 64 are 8 and -8" and uses sqrt as the positive root in the last line; fine mathematically. It follows the book's p.8 sentence "Thus sqrt(64) = +-8" even though the same page then says "we shall only consider the positive square root" and the Summary prints sqrt(9) = 3. Not a LP mistake. Listed so the content team knows the book itself is inconsistent here. | no change needed |

Nothing is missing from a question that only a figure carries: the LP text of `M2.S15.T15.C64` states all the data of the tile picture (9 rows of 9, 5 by 5 per tile), so the picture is a repeat of data for counting, not a source of hidden numbers.

### Class 8 Ch 1, chunk C
- **M3.S21.T21.C92 (question 91 to 109).** The question says 'using the cube pattern' but does not print the pattern. A learner who skipped the teaching page cannot use it. Suggested sentence to add after the question: "Recall the pattern: $1 = 1^3$, $3 + 5 = 2^3$, $7 + 9 + 11 = 3^3$, $13 + 15 + 17 + 19 = 4^3$, $21 + 23 + 25 + 27 + 29 = 5^3$, $31 + 33 + 35 + 37 + 39 + 41 = 6^3$."
- **M3.S21.T21.C90 (4104).** The book's Try This asks for 4104 and 13832; the LP covers only 4104. Suggested extra question or sentence: "Show that $13832 = 2^3 + 24^3 = 18^3 + 20^3$" (2^3 + 24^3 = 8 + 13824 = 13832; 18^3 + 20^3 = 5832 + 8000 = 13832).
- **M4.S25.T25.C113 (worked example).** Step 2 starts "Start 16, 9, 7, ..." but the list is the whole row of 17 numbers, not a start. Suggested: "One arrangement is 16, 9, 7, 2, 14, 11, 5, 4, 12, 13, 3, 6, 10, 15, 1, 8, 17 (its reverse also works)." The book's other questions on the page (more than one way, why not; the 1 to 32 circle) are not in the LP.
- **Book numbering in the LP.** C107 and C109 are labelled 'Figure it Out, Q1' and 'Q2' but are the book's Figure it Out Q2 and Q4 (ncert_refs FiO2.q2 and FiO2.q4); C96 'Cubic Numbers, Q5' and C105 'Cubic Numbers, Q1' use the book's own numbers. The book's Q3 (true or false) is in another chunk.
- **Concept image C113.IMG1** (accounting only) shows 3, 6, 10, 15 with 9, 16, 25; the book's example is 3, 6, 10, 15, 1 with 9, 16, 25, 16. Not an LP text issue, but the teaching image is one number and one sum short.

### Class 8 Ch 2, chunk A
- M1.S3.T3.C8 (question): says "using the thickness table", but the table is not in the question text and the concept image C2.IMG1 shows only the first doublings. Suggested: add the table as a LaTeX array (folds 1 to 17, and fold 0 = 0.001 cm, fold 20 = about 1048.5 cm), or at least the values the solution uses: "Fold 3 = 0.008 cm, fold 4 = 0.016 cm, fold 5 = 0.032 cm, fold 7 = 0.128 cm, fold 0 = 0.001 cm, fold 10 = 1.024 cm, fold 20 = about 1048.5 cm."
- M3.S8.T8.C32 (question): "In the story" but the story is not stated. The figure covers king to rooms only, so the rest must be in the text. Suggested: "A king had three daughters. Each daughter got three baskets, each basket had three keys, each key opens three rooms, each room has three tables, each table has three necklaces and each necklace has three diamonds. Find the number of rooms and the number of diamonds." (The book words it as a verse: "Each room had tables - one, two, three, with three bright necklaces on each ... each necklace had three diamonds".)
- M1.S3.T3.C6 (question) and M1.S2.T2.C3 (worked): "starting from about 10.4 m after 20 folds" does not give the LP's own values: 10.4 x 2 = 20.8, then 41.6, 83.2, 166.4, 332.8, whereas the steps say 21, 42, 84, 168, 336. Those come from the exact 10.485 m (1048.576 cm), which C9 uses as "about 1048.5 cm". Suggested: "about 10.5 m (10.485 m)" in C6 and C3, or keep the book's "about 10.4 m" and say "values are rounded from 10.485 m".
- Book numbers: M2.S6.T6.C23 ("Figure it Out, Q1") is book FiO Q2 (648, 405, 540, 3600); M2.S6.T6.C25 ("Q2") is book FiO Q3; M3.S9.T9.C42 ("Figure it Out, Q1") is book FiO (second set) Q10. Two different questions are both labelled "Figure it Out, Q1". Suggested labels: "Figure it Out, Q2 (first set)", "Q3 (first set)", "Q10 (second set)". M3.S8.T8.C40 "Power Play, Q4" is book Q4 of the second set (correct).
- M2.S5.T5.C21 (question_tex): the sub-part separators are uneven: "(i): ...; (ii): ... (iii) ... (iv): ...; (v): ... (vi) ...". Suggested: one style, e.g. "(i) ... (ii) ... (iii) ...".
- M3.S8.T8.C35 and C37, C39, C41 (the plain `question` field): the exponents are spelled out ("p⁴ × p to the power 6", "4 to the power 6"). Suggested: use the symbols as in `question_tex` ("p⁴ × p⁶", "4⁶", "(2⁵)²", "q⁴⁶").
- No wrong answers found: I recomputed all LP numbers of the 17 units (thickness values from 21 m to 703687 km, ratio checks 4, 8, 1024, 2^10 v, 12 and 64, 32400 = 2^4 x 5^2 x 3^4, 648, 405, 540, 3600, the six values 2000 ... -32000000, 2187 = 81 x 27 = 9 x 243, 512, 78125, 4096 both ways, 1024, the power-of-a-power forms, the sixth powers 729 and 4096). All hold.

### Class 8 Ch 2, chunk B
No arithmetic mistake found: I recomputed every number in the 18 units (2^30 and 2^29; 16 x 81 = 1296; 10000 / 625 = 16; 11664 for all three equal expressions; 14 x 3 = 42; 26^6 = 308915776; 36^5 = 60466176; 10^9 < 8,500,000,000 < 10^10; 2^160 ends in 6; every simplification in C86 and C88). The points below are wording only; nothing was changed.

- M3.S11.T11.C54 (question): "Circle the numbers that are the same" cannot be done on a text-only page. Suggested sentence: "Which of these numbers are the same? 2^4 x 3^6, 6^4 x 3^2, 6^10, 18^2 x 6^2, 6^24. Write them down." (The answer text already names the three, so only the question needs it.)
- M4.S18.T18.C88 (solution step (iv)): "$-2 \times -3 = 6$" puts two minus signs side by side. Suggested: "$(-2) \times (-3) = 6$, so $13^{6}$."
- M4.S18.T18.C85 / C86 and C87 / C88: the question lists parts (i) to (v) (C87) or separates them with semicolons (C85) while the solution steps for C85 / C86 carry no part letters. Suggested for C86: start each step with its part letter, "(i): Add exponents ...", as C88 already does.
- M3.S13.T13.C60 (question): the book's hint "Try drawing a diagram like the one above" is missing from the LP question text; it is not needed for the answer, but if a choice tree is wanted later the question should say so.
- M3.S13.T13.C62 / C63: no missing data. The answer lists 100, 1000 and 100000 and the steps also give 4 digits (10000); fine.
- No missing data was found that only a figure could carry in any unit of this chunk.

### Class 8 Ch 2, chunk C
- **M5.S23.T23.C106** (question; also C107 steps refer to it): the question says "write the three large-number facts in scientific notation" but never states the facts. Suggested sentence: "The Sun is 30,00,00,00,00,00,00,00,00,000 m from the centre of the Milky Way; our galaxy has 1,00,00,00,00,000 stars; the Earth has a mass of 59,76,00,00,00,00,00,00,00,00,00,000 kg." (zeros checked: 3 x 10^20, 1 x 10^11, 5.976 x 10^24, as the LP solution says).
- **M5.S23.T23.C108** (question): it never says the Earth is to be marked on the number line with the Sun and Saturn ends. Suggested sentence: "On the number line below, with the Sun at one end and Saturn at the 1.4335 x 10^12 m mark, show where the Earth (1.496 x 10^11 m from the Sun) sits."
- **M4.S19.T19.C89, M5.S24.T24.C116, M5.S24.T24.C118** (book numbers): the LP calls them "Figure it Out, Q1", "Figure it Out, Q1", "Figure it Out, Q2"; in the book they are Q3, Q6 and Q12 (ncert_refs FiO2.q3, FiO2.q6, FiO2.q12 are right). The LP numbering restarts in each topic.
- **M4.S21.T21.C95** (answer_tex): "$4^2$ is $4^4$, which is $256$, times $4^{-2}$" is correct but reads awkwardly. Suggested: "$4^2$ is $4^4 = 256$ times larger than $4^{-2}$."
- **M5.S22.T22.C100**: ncert_refs lists `2.4.comic` but neither the question nor the steps use the dinosaur comic. Harmless.
- Checked and correct (recomputed): C90 (all nine products equal 2^18, 2^48 x 3^8, 2^-25), C91 (all three = 1024 = 4^5), C95 (16384/1024 = 16, 4^2 / 4^-2 = 256), C97 (eight results), C105, C107, C109 (0.104), C111 (4, 4, 6, 10), C113, C115, C117, C119, C121 (11250), C122 (16 days, 3066000 km, 76.65), C123 (1922000000 steps = 192 crore 20 lakh), C126 (200 = 2 x 10^2).

### Class 8 Ch 2, chunk D
- **M6.S28.T28.C132 (Q1 question):** the question asks for "the starling and mosquito populations" but never gives them, nor the numbers of people and elephants. Suggested sentence to add: "The starling population is about 1.3 billion (1.3 arab) and the mosquito population is about 110 trillion (11 neel); there are about 8 × 10^9 people and about 4 × 10^5 African elephants."
- **M6.S28.T28.C134 (Q2 question):** the ants, people, starlings and trees numbers and the leaves per tree are missing (only 10000 birds, 0.001 cm and 384400 km are given). Suggested sentence: "There are about 2 × 10^16 ants (20 quadrillion), 8 × 10^9 people, 1.3 × 10^9 starlings and 3 × 10^12 trees, and about 10^4 leaves on each tree."
- **M6.S28.T28.C135 (Ans2):** step 1 uses "2 ÷ 8" and "16 − 9" without saying the ants are 2 × 10^16 and the people 8 × 10^9. Suggested first step: "Ants per human: (2 × 10^16) ÷ (8 × 10^9), so 2 ÷ 8 = 0.25 and 16 − 9 = 7, giving 0.25 × 10^7, which is 2.5 × 10^6."
- **M6.S28.T28.C136 (Q3 question):** "decide what unit 6970710 is in" does not say who says it. The book's bubble reads Roxie: "I am 69,70,710 ... old." Suggested: "Roxie also says, 'I am 6970710 ... old.' Decide what unit 6970710 is in." Also the book asks for Estu's date of birth (4070 days) and for how old one is after a million seconds; the LP rewrites these as "age in years" and "how many days a million seconds is". The LP answers are right for what they ask (and match the book's 'about 12 days'), but the question no longer asks the book's question; consider "find Estu's date of birth" as in the book.
- **M6.S28.T28.C140 (Q5 question):** part (i) needs the world population, 8.2 × 10^9, which the book gives only in the facts list; the question text does not. The LP solution states it, the question does not. Suggested: add "The world population is about 8.2 × 10^9." Parts (iv) needs assumptions (the solution states 1 hour a day for 70 years); fine as the book's answer does the same.
- **M6.S29.T29.C142 (book number):** `book_number` is "Figure it Out, Q1" but this is end-of-chapter Q14 of the book (Try This, p.27); C140 is labelled "Power Play, Q13". Suggested labels "Figure it Out, Q13" and "Figure it Out, Q14" (or the same style for both).
- **M6.S30.T30.C145 (worked example, step 4):** "the atoms are at most 10^82, so a googol is 10^18 times as many" should read "at least 10^18 times as many" (the book gives 10^78 to 10^82 atoms, so the ratio is between 10^18 and 10^22). The question also never states the atoms figure, only the steps do.
- **M6.S31.T31.C148 (Ans1):** the question lists million first, but the answer starts at billion. Suggested extra step: "mi means 1: a million is 1000 with 1 more 1000 multiplied on, 10^(3+3×1) = 10^6."
- **M6.S31.T31.C147 (question):** the book prints the first part in bold (**mi**llion, **bi**llion, **tr**illion, **quad**rillion, **quin**tillion); the LP text does not, so the student is not told which part is meant. Suggest bolding them.

Arithmetic of all nine LP solutions was recomputed and holds (116160 hours; 6970710 / 1440 = 4840.77; 4070 = 11 × 365 + 55; 10^6 / 86400 = 11.57; 8.2 × 3 = 24.6 so 2.46e11; 3.8 × 8.2 = 31.16; 3600 × 365 × 70 = 91,980,000; 1.5 × 3.15 = 4.725; 2e25 / 16 = 1.25e24 ml, / 200 = 6.25e21 glasses, × 10 s = 6.25e22 s; 1e9 / 86400 = 11574; 10^100 / 10^82 = 10^18). The LP answers agree with the book's printed answers (pp.34-38), including 'about 12 days' (LP 11.57 / 11.6).

### Class 8 Ch 3, chunk A
- **M1.S2.T2.C4 (worked example)**: the question says "use Table 1 to write 13 and 18 in Roman symbols" but Table 1 is not in the question text, and the concept text above it lists the symbols in one line ("I, II, III, ... XX (Table 1)") without the numbers they belong to. Suggested sentence for the question: "Table 1 gives the Roman symbols for 1 to 20 in order: I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII, XIII, XIV, XV, XVI, XVII, XVIII, XIX, XX." (or a LaTeX array with the numbers 1 to 20 above them).
- **Figure it Out numbers in the LP labels do not match the book's** (book numbers in brackets):
  - M1.S3.T3.C7/C8 "The Mechanism of Counting, Q1" = book Figure it Out Q1 (p.7): fine.
  - M1.S4.T4.C9/C10 "Figure it Out, Q1" = book Q2 (p.7); M1.S4.T4.C11/C12 "Figure it Out, Q2" = book Q3 (p.7).
  - M1.S6.T6.C19/C20 "Early Number Systems, Q1" = book Figure it Out Q1 (p.13).
  - M1.S7.T7.C21/C22 "Figure it Out, Q1" = book Q2 (p.13-14).
  - M2.S11.T11.C36/C37 "Figure it Out, Q1" = book Q3 (p.14); M2.S11.T11.C38/C39 "Figure it Out, Q2" = book Q4 (p.14).
  - The same labels ("Figure it out: Q1") repeat across topics (M1.S4.T4.C9, M1.S7.T7.C21, M2.S11.T11.C36), which a learner will see side by side.
- **M1.S7.T7.C22, step (iii)**: the sentence "write the first number two times and then double the result, 4 copies in all" is confusing (the answer 18 ukasar is right: 9 x 4 = 36). Suggested: "ukasar-ukasar is 4, so write the first number 4 times: 16 ukasar and 4 urapon; the 4 urapon make 2 more ukasar, so 18 ukasar."
- **M2.S8.T8.C23 (worked example)**: the LP numeral MMCCCLXVII is right; the book prints MMCCCLXII (missing the V; 2367 = 1000 + 1000 + 100 + 100 + 100 + 50 + 10 + 5 + 1 + 1). No diagram is drawn for this item; if a figure of it is ever drawn it must show MMCCCLXVII.
- **M2.S9.T9.C31 and M2.S10.T10.C35**: the solution figure will sit before step 1. The steps' wording ("Count the symbols ...", "Five I's make one V") fits the figure, so no text change is needed; if the figure is added, "Look at the picture first" is not required.

Checks I did on the LP solutions (all correct): 1345 / 5 = 269; (i) 9 + 7 = 16 = 8 ukasar, (ii) 9 - 6 = 3, (iii) 9 x 4 = 36 = 18 ukasar, (iv) 16 / 4 = 4; MCCXXII, MMCMXCIX, CCCII, DCCXV; 87 + 78 = 165 = CLXV; 5 x 50 = 250 = CCL, 50 x 500 = 25000 (25 M's), 5 x 500 = 2500 = MMD, 7 x 9 = 63 = LXIII; 232 + 413 = 645 = DCXLV.

### Class 8 Ch 3, chunk B
(Not edited; listed for the user.)

1. **M2.S16.T16.C50, M2.S17.T17.C52, M2.S17.T17.C54, M2.S21.T21.C71, M2.S21.T21.C73 (question_tex / text).** "base$-5$", "base$-7$" are written with the hyphen inside the dollar signs, so the LaTeX shows a minus sign: "base -5 system". In C54 the second occurrence is written "base-$n$" (correct). Suggested: "base-$5$ system", "base-$7$ system", "base-$n$ system" (or plain "base-5").
2. **M2.S16.T16.C50 (question).** "using the symbols in Table $2$" refers to a table that is nowhere in the LP text, and the solution C51 uses the names triangle, square, hexagon, circle, wave without defining them. The diagram supplies the table. Suggested sentence if the text should stand alone: "Table 2: triangle $= 1$, square $= 5$, hexagon $= 25$, circle $= 125$, wave $= 625$, arrow $= 3125$."
3. **M2.S20.T20.C69 (question).** "Add $2907$ and $43$ on the counting board." says nothing about the board. Suggested: "On the counting board, a counter on a line is worth that line's value and a counter in the gap above a line is worth 5 times it. Put $2907$ on the left of the partition and $43$ on the right, then find the sum."
4. **M2.S20.T20.C70, step 1.** "$2907$ has $2$ counters on the thousands line, $9$ on the hundreds line (one above it for $5$ and $4$ on it), none for tens and $7$ for ones" reads as 9 counters on the hundreds line and 7 on the ones line; what is meant is 9 hundreds and 7 ones. Suggested: "$2907$ has $2$ counters on the thousands line, $9$ hundreds (one counter above the hundreds line for $500$ and $4$ on the line for $400$), no tens, and $7$ ones (one counter above the ones line for $5$ and $2$ on it); $43$ has $4$ tens and $3$ ones."
5. **Book numbers.** The LP restarts the "Figure it Out" numbers in each topic, so they do not match the book: C45/C46 "Figure it Out, Q1" is the book's page 62 Q2 (ncert_ref FiOD.q2 is right); C52-C55 "Q1", "Q2" are the book's page 63 Q2, Q3; C56-C59 "Q3", "Q4" are the book's page 69-70 Q1, Q2; C71/C72 "Q1" is the book's page 65 Q2; C73/C74 "Q2" is the book's page 70 Q3. Only the labels differ; the questions themselves are the right ones.
6. **M2.S13.T13.C43 `q_figure` hint** ("the table of Egyptian symbols") and **M2.S12.T12.C41**: the book question has no figure; nothing to change in the text, only the hint is wrong.

### Class 8 Ch 3, chunk C
- **M3.S23.T23.C80**, `answer_tex`: the semicolon between (iv) and (v) is missing: "(iv): $1$ | blank (v): $1$ | blank | $5$". Suggested: "(iv): $1$ | blank; (v): $1$ | blank | $5$".
- **M3.S23.T23.C80**, step (iv): "written 1 followed by a blank" cannot be seen in a numeral (a trailing blank is invisible; it looks like the numeral for 1, which is the ambiguity of the next section). Suggested: "(iv): 60 = (1) x 60, so the 1s place is empty: written 1, with the empty 1s place after it (marked in the picture)."
- **M3.S23.T23.C80**: the LP gives the compact form (1 | 3 ...) while the book's printed answer draws the older form with a landmark diamond. Not an error, but the two differ; the diagram follows the LP.
- **M3.S28.T28.C96**, `question_tex`: "hadn'$t$ been invented" has a stray math wrapper around the t. Suggested: "hadn't been invented".
- **M3.S27.T27.C94 / C95 and M3.S28.T28.C98**: "base$-2$", "base$-10$" are set in math mode (the minus becomes a math minus sign). Suggested plain text "base-2", "base-10" like the book.
- **M3.S27.T27.C95**: the LP answer does not carry the comparison table of the book answer (Number, Base-2 system with ur = 0 and uk = 1, Gumulgal system, rows 1 to 8). Suggested: add that table as a LaTeX array. The step "the Gumulgal ... stopped at 6" is true of the chapter text, but the book answer extends the Gumulgal column to 7 (uk-uk-uk-ur) and 8 (uk-uk-uk-uk) by the same counting-by-2 rule; a short clause such as "(the book answer continues the Gumulgal names to 8 by adding words)" would remove the apparent conflict (optional).
- **M3.S25.T25.C89**, step 3: "$2$ then $3 (23)$", "$3$ then $2 (32)$": the bracketed number is inside the same math group. Suggested: "$2$ then $3$ ($23$)", "$3$ then $2$ ($32$)".
- **M3.S28.T28.C99**, step 3: "$25 = (1) \times 25 + (0) \times 5 + 0$". Suggested: "$25 = (1) \times 5^2 + (0) \times 5 + (0) \times 1$" (the book writes it this way).
- **M3.S22.T22.C75**: ncert_refs cite meso_640 and meso_7530 but the example is 4000; the step "written as 1 with the 3600 symbol, 6 with the 60 symbol, and 40" has no numeral shown anywhere except in the new diagram. Fine once the diagram is added; no text change needed.
- **M3.S26.T26.C92**: `ncert_refs` is empty (an LP-made example, no book source). Not an error.
- **Book numbers**: the LP numbering differs from the book for the last Figure it Out set: C88 "Place Value, Q1" is book Q1; C94 "Place Value, Q2" is book Q2; C96 "Figure it Out, Q1" is book Q3; C98 "Figure it Out, Q2" is book Q4. The one book set is split over three topics with restarted numbering.

### Class 8 Ch 4, chunk A
- **M2.S3.T3.C11** (question_tex and text): stray colons: "(i) $30^\circ$ (ii): $40^\circ$ (iii): $90^\circ$ (iv): $140^\circ$". Suggested: "... intersect at an angle of (i) $30^\circ$ (ii) $40^\circ$ (iii) $90^\circ$ (iv) $140^\circ$." (the plain `question` field is right).
- **M2.S3.T3.C12**: the steps are written for all four angles but the only picture is for 30 degrees. Suggested extra sentence at the end of step 1: "The figure shows case (i), 30 degrees; (ii), (iii) and (iv) are drawn the same way."
- **M2.S3.T3.C10**: step 1 uses "the four angles at $O$" and triangles AOB, AOD without ever saying that the diagonals AC and BD meet at O (the question does not name O either). Suggested: start step 1 with "The diagonals $AC$ and $BD$ meet at $O$."
- **M2.S6.T6.C23**: the angle list and the steps leave out angle DBC = 60 degrees in rectangle (i) (the book's printed answer leaves it out as well). The figure marks it (90 - 30). Suggested: add "$\angle DBC = 60$" after "$\angle ACB = 60$" in step 3.
- **M2.S10.T10.C42**: the question text drops the book's "as shown in Figure (b)", yet the question picture carries the book's two figures. Suggested ending: "... lie on the sides of the outer square, as in the second square of the picture."
- **M2.S2.T2.C5** (worked example): the text names no vertices, the figure carries A, B, C, D and O (as the book's x-figure does); only O is used by the steps. Harmless, but the letters A-D could be dropped from the spec if the text is kept as it is.
- **LP numbering**: `book_number` restarts per topic ("Figure it Out, Q1" is book FiO Q4 for C13, Q5 for C24; Q1/Q2 in topics T10 are FiO3 Q6 / Q7; C26 is FiO3 Q5). The `ncert_refs` carry the true numbers (FiO1.q4, FiO1.q5, FiO3.q5, FiO3.q6, FiO3.q7), so nothing was changed.

### Class 8 Ch 4, chunk B
- **M3.S12.T12.C49** (question): the text does not say which corner caves in; the figure (and the book) caves in at D. Suggested: "(The quadrilateral $ABCD$ has one corner, $D$, that caves in.)"
- **M3.S12.T12.C50** (solution): the steps name neither the diagonal nor the triangles, so the figure's labels have no text to match. Suggested step 1: "Draw the diagonal $BD$ from the caved-in corner $D$ to the opposite corner $B$; it lies inside the figure." Step 2: "It splits $ABCD$ into triangles $ABD$ and $CBD$, each with angles adding up to $180$." Step 3: "At $D$, $\angle ADB$ and $\angle BDC$ together make the reflex angle of $ABCD$."
- **M4.S14.T14.C58** (solution): step 4 "$\angle C + \angle D = 180$" has no reason. Suggested: "$AD \parallel BC$ with transversal $CD$, so $\angle C + \angle D = 180$ and $\angle C = 180 - 150 = 30$."
- **M4.S14.T14.C60** (solution): step 6 is hard to follow. Suggested: "$\triangle ABD \cong \triangle CBD$ would match $A$ with $C$, $B$ with $B$ and $D$ with $D$, so it would make $AB = CB$; but $AB = 4\text{ cm}$ and $CB = 5\text{ cm}$."
- **M4.S16.T16.C66** (solution): steps 2 and 3 do not say which end of the line is B or D. Suggested step 3: "On it mark $D$ on the arm that makes the $140^\circ$ angle with $OC$, and $B$ on the opposite side of $O$, with $OB = OD = 2.5\text{ cm}$, so $BD = 5\text{ cm}$."
- **M4.S18.T18.C75 / C76**: inconsistent punctuation: the question has "(i): Parallelogram ..." in `question_tex` but "(i) Parallelogram ..." in `question`; the steps mix "(i):" with "(ii)". Suggested: use "(i)", "(ii)", "(iii)", "(iv)" with no colon everywhere.
- **M4.S19.T19.C77 / C78**: `book_number` is "Figure it Out, Q1" but the item is Figure it Out (p.102) Q3, and the sibling pairs of the same exercise say "Parallelograms and Rhombuses, Q1/Q2". Suggested: "Parallelograms and Rhombuses, Q3". The C77/C78 items also lack the `ncert_refs`/`example_id` that the other pairs carry.
- **M3.S12.T12.C47 / M4.S14.T14.C55 / C57 / C59 / C73 and others**: `book_number` is a description ("Quadrilateral Angles: find the fourth angle", "Parallelograms: construct with 4 cm, 5 cm and 30°") rather than a book question number; nothing to fix for diagrams.

### Class 8 Ch 4, chunk C
- **M5.S21.T21.C83 / C84, band length.** The question says "rubber bands of 4 cm"; the book prints no length. Its picture shows a 9 x 9 peg board, bands 4 gaps long, and the extended band 6 gaps long (one gap added at each end), and the book says "extend by 2 cm", which would make one gap 2 cm, the bands 8 cm and the extended band 12 cm. The LP numbers (4 cm, extended to 8 cm) are consistent with each other and give the same shapes (square, then rhombus); the diagrams use the LP numbers. Suggested sentence if the picture should match: "Two rubber bands of 8 cm cross at right angles at their midpoints ... one band is extended by 2 cm at each end (to 12 cm)."
- **M5.S21.T21.C85 / C86, equilateral case.** The question text covers only the 8, 8, 6 triangle, but step 4 and the answer also give two equilateral triangles of 8 cm. Suggested question: "Join two copies of the triangle with sides 8 cm, 8 cm and 6 cm in different ways and name the quadrilaterals. Then join two equilateral triangles of side 8 cm and name the quadrilateral."
- **Degree signs missing.** Angle values are written as bare numbers in the steps of C90 ("$60$", "$60 + 120 + 60 + 120 = 360$"), C94 ("$180$", "$90$"), C97 and C98 and C103 (plain "90", "115"), C101 ("$180 - 105 = 75$"), C106, C108 ("$360 - 270 = 90$"). Suggested: write $60^\circ$, $180^\circ$ etc.
- **M5.S23.T23.C93 / C94.** The question asks only that BD bisects angle ABC, but step 2 and the answer also state angle ADC (the book asks for both). Suggested question: "Show that BD bisects $\angle ABC$ and $\angle ADC$, and that BD is perpendicular to AC with AO = OC."
- **M5.S25.T25.C100.** (a) The old q_figure hint says 135 and 105 degrees are at the ends of "the longer lower side"; in the book they are at the ends of the shorter (bottom) parallel side, the longer one is on top. The diagram follows the book. (b) Text (ii) "An isosceles trapezium with an angle of 100 degrees" does not say where the angle is; the solution assumes it is next to the shorter parallel side (the only place an obtuse angle can be). Suggested: "(ii): An isosceles trapezium in which an angle next to the shorter parallel side is $100^\circ$."
- **M5.S24.T24.C98.** Steps use the points Y and Z, which neither the question nor step 1 introduces. Suggested step 1: "Draw XY and WZ perpendicular to UV, meeting UV at Y and Z; XWZY is a rectangle, so XY = WZ."
- **M5.S27.T27.C106.** The question asks for reasoning "as well as by construction and measurement"; the steps give only the reasoning. Suggested extra step: "Check by construction: draw a rhombus of side 5 cm with one angle of $90^\circ$; measuring gives four right angles, so it is a square."
- **M5.S26.T26.C104.** The answer (ii) "Yes, a square" is right and differs from the book (see section 4). The `text` starts with an internal label "Figure it Out (kites and trapeziums, question 4):" which a learner should not see if the text is shown as is.
- **M6.S28.T28.C110.** The question merges the book's questions 4 and 6 and leaves out question 5 (the nested creases), which appears only as step 4. No change needed, noted for completeness.

### Class 8 Ch 5, chunk A
- **M1.S8.T8.C25 (question) and M1.S8.T8.C26 (solution):** the question text never mentions the dot picture that the book gives
  ("Look at the following expressions and the visualisation"), yet the solution says "The full rows stack up and 2 dots are always
  left over", which only makes sense with the picture (or the teaching image of the previous topic). Suggested question sentence,
  to be placed before "write the explanation and examples": "Look at the expressions 4p + (4q + 2) = 4p + 4q + 2 = 4(p + q) + 2 and
  at the picture below, where p rows of 4 dots are joined to q rows of 4 dots and 2 more dots."
- **M1.S6.T6.C20 (question):** the book's list of algebraic expressions has nine cards; the LP lists eight (x^2 + 2 is left to the
  worked example C16, where it is handled). Suggested: either add "x^2 + 2" to the question list and a line to C21, or leave as is
  because C16 covers it.
- **M1.S11.T11.C36 (question_tex):** brackets are written "(i):", "(ii):" etc. with a colon, the plain `question` field and the
  book write "(i)" without it. Cosmetic.
- **LP book numbers differ from the book's:** C11 says "Figure it Out, Q1" (book: Figure it Out Q2 on p.11); C13 says "Figure it
  Out, Q2" (book: end-of-chapter Q9, p.22); C9 and C36 say "Multiples and Remainders, Q1 / Q3" (book: Figure it Out Q1 / Q3 on
  p.11); C27 says "Figure it Out, Q1" (book: end-of-chapter Q3, p.21). These are the LP's own labels; I found the items by text.
- No wrong number was found in any LP solution of this chunk: I re-added every sum, factorisation and example (for example the
  eight signed sums of 3, 4, 5, 6 and the claim that 0, -2, -4 appear for every four consecutive numbers, a - (a+1) - (a+2) + (a+3)
  = 0 and so on).

### Class 8 Ch 5, chunk B
(No LP text was changed and no decision depends on these.)

- M1.S12.T12.C38, question_tex: `don'$t$` puts the letter t in math mode. Suggested: "other multiples of $11$ don't remain multiples of $11$ when doubled."
- M1.S12.T12.C40, question_tex: "(i): ... (ii): ..." have a colon after each numeral (the book prints "(i) ..."). M1.S12.T12.C41: step 5 "so (iv): is never true" and answer_tex "(i): always (ii): always (iii): always (iv): never" carry the same stray colon. Suggested: "so (iv) is never true" and "(i) always, (ii) always, (iii) always, (iv) never".
- M1.S12.T12.C44, question_tex: the question does not name the four options although the LP answer says "Diagram (iv)". Suggested sentence: "Which of the four Venn diagrams (i) to (iv) shown below captures the relationship between the multiples of $4$, $8$, and $32$?" (the figure is placed after the question text).
- M1.S14.T14.C51, answer_tex: `$5k + 3 (k$ from $0)$ and $5k - 2 (k$ from $1)$` has math mode opened and closed in the wrong places. Suggested: "$5k + 3$ (with $k$ from $0$) and $5k - 2$ (with $k$ from $1$); the other four do not work".
- M1.S14.T14.C50, question_tex: the six expressions have no numerals (i) to (vi) although the book numbers them (i) to (vi); the answer text does not refer to them by number, so this is cosmetic. The book prints (iii) as the fraction 3k over 5; the LP writes `3k \div 5` (same value).
- M1.S15.T15.C54 and M1.S15.T15.C62: the pronoun is typeset as `$I$` (math italic) and the contractions as `won'$t$` (C54). Suggested: plain "I take", "I hold", "won't".
- M1.S15.T15.C59, steps: the picture is a part of the solution (placed before step 1); step 4 begins "Visually:". Suggested: "Visually (see the picture above):" so the learner knows the figure belongs to this step. The m and n of step 1 are the row counts written on the figure.
- Numbering: the LP's `book_number` labels do not match the book. T12 "Figure it Out, Q1 to Q4" are the end-of-chapter questions Q11, Q12, Q14, Q16; T15 "Figure it Out, Q1 to Q7" are section-5.1 Figure it Out Q5, Q6, Q7, Q8 (FiO1) followed by end-of-chapter Q2, Q7 and Q13 (FiO4); T14 C52 "Multiples and Remainders, Q4" is section-5.1 Figure it Out Q4. Not a diagram matter; suggested only if the numbers are shown to students.
- Missing data: none found. Every number a required figure needs is in the question, the LP solution or the book (Q7: 661 leaves 3, 4779 leaves 5, divisor 7).

### Class 8 Ch 5, chunk C
(Not edited; no decision was changed because of them.)

- **M2.S20.T20.C92** (`question_tex`, `text`): "If $I$ reverse its digits" has the pronoun I in math italics. Suggested sentence: `Sreelatha says, "I have a number that is divisible by $9$. If I reverse its digits, it will still be divisible by $9$".`
- **M2.S25.T25.C110** (`steps_tex` step 2, `text`): "needs three $2s$" renders as 2 times s. Suggested: `needs three $2$s` (or "three 2's").
- **M2.S23.T23.C103** (`steps_tex` step 4, `answer_tex`, `text`): math delimiters are misplaced, e.g. `gives $(7$, $0)$, $(5$, $2)$, ...` and `($p$, $q) = (7$, $0)$, ...`. Suggested step 4: `$p + q = 18$ needs $p = q = 9$, which is odd; $p + q = 7$ with $q$ even gives $(p, q) = (7, 0), (5, 2), (3, 4), (1, 6)$.` Suggested `answer_tex`: `$(p, q) = (7, 0), (5, 2), (3, 4), (1, 6)$`. (The plain `answer` is fine.)
- **M2.S22.T22.C101** (`answer_tex`, `text`): "(v): divisible (vi): divisible" lacks a separator. Suggested: `(v): divisible; (vi): divisible`.
- **M2.S24.T24.C106** (`text`): the opening repeats itself: "Checking Divisibility Quickly: fill the table: Fill in the following table: for each of ...". Suggested: `Checking Divisibility Quickly: Fill in the following table: for each of 128, 990, ...`. The ten answer lines have no column labels; the new diagram supplies them, so no text change is needed for the diagram.
- **Book numbering in the LP (`book_number` / concept names)**:
  - C82 says "Multiples of Nine, Q1"; the book has no such heading, it is Figure it Out Q1 on book p.126. Suggested: `Figure it Out, Q1`.
  - C84, C86, C88 say Q1, Q2, Q3; in the book they are Q2, Q3, Q4 of the same set (book p.126). Suggested: `Figure it Out, Q2`, `Q3`, `Q4`.
  - C90 and C92 say Q4 and Q5; in the book they are Q1 and Q4 of the end-of-chapter Figure it Out on book p.132. Suggested: `Figure it Out (p.132), Q1` and `Q4`.
  - C102 says Q1; in the book it is Q6 on book p.133. Suggested: `Figure it Out (p.133), Q6`.
- **C80/C81**: the book gives only the four statements; the test numbers 7309 and 4581 are the LP's own choice (4581 = 9 x 509). Not an error, noted so nobody looks for 4581 in the book.
- **C76**: the test number 123456 is the LP's own (the book only names 15, 33, 87). Not an error.

### Class 8 Ch 5, chunk D
No LP text was edited. Each item below: concept id, what is wrong or missing, suggested sentence.

- **M2.S26.T26.C112** (steps_tex step 4, answer_tex, text): the LaTeX is cut in the middle of each pair, so it will render oddly: `gives $(1$, $0)$`, `($a$, $b) = (1$, $0)$, $(2$, $8)$ ...`. Suggested: "$a + b = 1$ with $b$ even gives $(a, b) = (1, 0)$; $a + b = 10$ with $b$ even gives $(2, 8)$, $(4, 6)$, $(6, 4)$, $(8, 2)$." and answer "$(a, b) = (1, 0), (2, 8), (4, 6), (6, 4), (8, 2)$".
- **M3.S31.T31.C139** (question_tex): `$A_1 + 1B = B_0$` writes the digits as subscripts (A with a small 1), which reads like indexed variables, not the two-digit numbers A1, 1B, B0. Suggested: "Solve the cryptarithm $A1 + 1B = B0$ (each of A1, 1B and B0 is a 2-digit number)." Same slip in **M3.S31.T31.C147** (`$L_2N \times 2 = 2NP$`, should be `$L2N \times 2 = 2NP$`, three digits L, 2, N) and in **M3.S32.T32.C150** step 4 (`$5O_5 \times 5$`, should be `$5O5 \times 5$`).
- **M3.S32.T32.C150** (step 3): the math is split by the bracket: `so $W$ is $5 (W$ cannot be $0$ as a first digit).` Suggested: "so $W$ is $5$ ($W$ cannot be $0$ as a first digit)."
- **M3.S31.T31.C139 / C140** (second block): the LP labels the other three puzzles (i), (ii), (iii) (AB + 37 = 6A, ON + ON + ON = PO, QR + QR + QR = PRR); in the book they are (ii), (iii), (iv) because A1 + 1B = B0 is (i). Suggested: relabel them (ii), (iii), (iv) in the question and in the answer lines.
- **M2.S28.T28.C124 / C125** (riddle, missing data): the book asks "What's my number? What's my name?" and its answer gives both the number and its name in the Indian system ("11,11,11,111, Eleven crore eleven lakh eleven thousand one hundred eleven"). The LP question stops at "solve the riddle" and the answer gives only 111111111. Suggested: add "What is the number, and how do we read it?" to the question, and to the answer "$111111111$, read as eleven crore eleven lakh eleven thousand one hundred eleven ($11,11,11,111$)".
- **M2.S29.T29.C133** (step 1, weak example): 10 (even, root 1), 11 (odd, root 2), 12 (even, root 3) all show the parity of the root flipping, which does not show "no fixed link". Suggested: "$10$ and $20$ are both even, but their digital roots are $1$ (odd) and $2$ (even); so the parity of a number does not decide the parity of its digital root."
- **M3.S31.T31.C148** (missing eliminations): (v) lists P = 2, 3, 4 with Q = 1 but never says why P = 1 and P = 5 to 8 are out. Suggested: "$P = 1$ would make $P$ and $Q$ the same digit, and $P = 5, 6, 7, 8$ give $605, 726, 847, 968$, whose first digit is not $P$." In (i), after "$T = 0$" add "$3 \times U$ must end in $U$, so $U = 5$ (since $U \ne T$)".
- **M3.S31.T31.C146** (steps 3 and 4): $6 \times E$ ending in $Y$ also allows $E = Y$ ($E = 0$ for $Y = 0$, $E = 2$ for $Y = 2$, $E = 4$ for $Y = 4$); the LP names only $E = 5$, $7$, $9$ for those. Suggested: add "(the other choice $E = Y$ would use one digit for two letters)".
- **Labels:** "Figure it out: Q1" is the name of three different concepts (M2.S26.T26.C111, M2.S29.T29.C128, M3.S32.T32.C149), and M2.S28.T28.C126 is named "Digital Roots: Q3" while its `book_number` is "Digital Roots, Q1". The text of each question is right; only the labels collide. Suggested: use the book's own numbers (5.3 FiO Q5, Q8, Q10, Q15; digital-root FiO Q1 to Q4).
- **M3.S33.T33.C152** (worked example): "your partner completes a line of three next turn" is a placing-phase situation, while the book's rules (p.24, rule 2) describe lines being made by moving pawns after all are placed (rule 1 only talks about placing). The LP answer is consistent with rule 3 (a completed line removes a pawn). Suggested: begin the question with "While you are still placing pawns, ..." if the content team wants it to follow the standard game; otherwise leave as is.

### Class 8 Ch 6, chunk A
(No LP text was edited and no decision changed because of these.)

- **M2.S3.T3.C10** (question): the text says "Observe the multiplication grid" but never says what the grid is; the table exists only in the figure. Suggested sentence: "Observe the $10 \times 10$ multiplication grid below (the cell in row $i$ and column $j$ holds $i \times j$). The $3 \times 3$ frame outlined in it is shown enlarged beside it, next to an empty frame whose middle number is $pq$." The example in the LP omits the middle row $4 \times 5$, $4 \times 6$, $4 \times 7$ (not wrong, just short).
- **Book numbers.** C10 is labelled "Distributive Property, Q1" and C19 "Distributive Property, Q2" but both are Figure it Out Q1 and Q2 (book pp.142-143); C25, C27, C29 are labelled "Figure it Out, Q1/Q2/Q3" but are book Q3, Q4, Q5 (their ncert_refs FiO1.q3, q4, q5 are right). Suggest "Figure it Out, Q1" ... "Q5" for all six.
- **M2.S3.T3.C9** step 1: "which is negative when a is at least $b$": the letter a is not in math mode; suggest "$a$ is at least $b$".
- **M2.S6.T6.C22** last step: "No two of $a^2$, $ab$ and a have the same letter-numbers": suggest "$a$".
- **M2.S7.T7.C28** steps 3 and 6: "So (i): is $...$." and "So (ii): is $...$." have a stray colon; suggest "So (i) is $4a + 5ab + ab^2 - 12b^2 - 3b^3$." and "So (ii) is $4y^2 + 44yz - 5y + 77z - 21$."
- **M2.S5.T5.C20** answer_tex: semicolons are missing after (ii), (iii) and (v): "(ii): $10 + 4a$ (iii): ... (iv): ...; (v): ... (vi): ...". Suggest a semicolon after every part.
- **M2.S4.T4.C12** (worked example): the block has only plain text (`question`, `steps`, `answer`) and no `question_tex` / `steps_tex`, unlike the other blocks; suggest LaTeX versions, e.g. "$23 \times 27 = 621$. Use the four parts to find the product when $23$ grows by $2$ and $27$ grows by $5$."
- No answer in the chunk contradicts the book. Every LP number was recomputed: 644, 648, 51, 3, -28, 104, 42, 800 (increase 179), 27 = 27, (1,6) (2,8) (3,10), 42614, 62458, 1034, 5445, 36069, 52703816, 391274, 8989, 95849, 266096831, 1112111, 963666, 23454522.

### Class 8 Ch 6, chunk B
1. **M3.S11.T11.C47** (question): the text never says the 65 square is cut into four parts or that the areas of the parts are wanted, and it omits that the 30 + 35 split should be drawn. Suggested: "A square of side 65 is split as 60 + 5 into a 60 square, a 5 square and two 60 by 5 rectangles. Write the area of each part and add them to find $65^2$. Draw the square again split as $30 + 35$ and check that the area is the same."
2. **M3.S13.T13.C58** (question): "Find $55^2$ from the square of side $60$." does not say where the 55 square sits. Suggested: "A square of side $55$ sits in one corner of a square of side $60$. Use the area of the $60$ square and the strips around the $55$ square to find $55^2$."
3. **M4.S18.T18.C81, extra block (E1), part (a)**: `question_tex` has `\frac{1}{2(10s - 6)} + 3 = 5s`, which prints 1 over 2(10s - 6). Card 7 is one half times (10s - 6). Suggested: `$(a)$: $\frac{1}{2}(10s - 6) + 3 = 5s$`. The plain `question`/`text` also read "1/2(10s − 6)", which is ambiguous; suggested "(1/2)(10s − 6) + 3 = 5s".
4. **M4.S18.T18.C81 (both blocks): the working lines of the cards are missing.** The book cards show, for example, card 1 "−3p(−5p + 2q) = −3p + 5p − 2q = p − 2q", card 2 "= 2x − 1 + 3x + 4 = 5x + 3", card 3 "= (y + 2)^2 = y^2 + 4y + 4", card 6 "= 6ab × 9ac = 54a^2bc", card 7 "= 5s − 3 + 3 = 5s", card 10 "= (x + 2)x + (x + 2)5 = x^2 + 2x + 5x + 10 = x^2 + 7x + 10". The LP lists only the first and last expression, yet the question asks to explain what went wrong. Suggested: add the middle line to each of (a)-(f) in both blocks.
5. **M4.S18.T18.C82, answer_tex and steps_tex (f)**: `$18$abc` should be `$18abc$` (steps step 6 and answer_tex). Also in `answer_tex` the parts run together: `$(a)$: $15p^2 - 6pq (b)$: $5x + 10$; ... $25m^2 + 60mn + 36n^2 (e)$: correct $(f)$: $18$abc`. Suggested: `$(a)$: $15p^2 - 6pq$; $(b)$: $5x + 10$; $(c)$: $3y + 4$; $(d)$: $25m^2 + 60mn + 36n^2$; $(e)$: correct; $(f)$: $18abc$`. The extra block has the same problem: `$(c)$: $5a^3 + 6a^2b + 6ab^2 (d)$: $ab + 4a + 2b + 8$` should be `... 6ab^2$; $(d)$: ...`.
6. **M4.S18.T18.C81 / C82**: part letters (a)-(f) restart in the second block; the book numbers the cards 1 to 12. Suggested: keep the letters but add "cards 1 to 6" and "cards 7 to 12" to the two question texts so the learner can match the book.
7. **M3.S13.T13.C62 (question_tex)**: `(i)` has no colon but `(ii):` and `(iii):` do. Suggested: use `(i):`, `(ii):`, `(iii):` throughout. In **C63 steps_tex** step 5, "so (iii): is" reads wrongly; suggested "so (iii) is".
8. **Book numbers in T16** (`book_number`): "Figure it Out, Q1/Q2/Q3" are the book's Figure it Out Q2, Q3, Q4 on p.14 (the book's Q1 is "Which is greater", which the LP files in T15 C70 as "Squares and Patterns, Q1"). The `ncert_refs` (FiO2.q2, q3, q4) are right; only the displayed numbers are one too low.
9. **M3.S11.T11.C49** says "split 104 and 37 into sums of numbers"; the book hint says "sums or differences". Harmless; the LP solution uses sums for both.

### Class 8 Ch 6, chunk C
- T19 C85-C96 and T22 C112-C119: `book_number` says "Figure it Out, Q1..Q6" (T19) and "Q1..Q4" (T22) but the book questions are Q2, Q4, Q5, Q6, Q7, Q9 (T19) and Q3, Q8, Q10, Q11 (T22) (the ncert_refs say so). Suggest using the book numbers or dropping the numbers.
- M4.S19.T19.C87: the question never shows the calendar. Suggested: "The figure shows the February calendar with the 2 by 2 square 4, 5 over 11, 12 outlined. Find the products of the numbers lying along each diagonal of a 2 by 2 square, for example 4 x 12 = 48 and 5 x 11 = 55. Do this for other 2 by 2 squares of the calendar."
- M4.S19.T19.C92: `answer_tex` has unbalanced math: `$2 ($or $5$ the other way round)`. Suggested: "difference: remainder $2$ (or $5$ the other way round)".
- M4.S21.T21.C102: the question does not mention the figure or its counts, and drops the book's "draw the next figure". Suggested: "The figure shows Steps 1, 2 and 3 of a pattern of black circles, with 3, 8 and 15 circles. Draw Step 4. Write the number of circles in Step k in two ways, show that they agree, and find the number in Steps 4, 10 and 15."
- M4.S21.T21.C104: the question gives only the counts. Suggested: "The figure shows square tiles forming a square frame round an empty square; Steps 1, 2 and 3 have 8, 12 and 16 tiles. Find the tiles in Step 4, Step 10 and Step n."
- M4.S21.T21.C105: the solution speaks of "a square of side n + 2 with a hole of side n" and "four rows of n plus four corners"; only understandable with the figure (now provided).
- M4.S21.T21.C106: m and n are not defined. Suggested: "In the figure, four equal rectangles m by n surround a shaded square. Tadang finds the area of the shaded square as (m + n)^2 - 4mn and Yusuf as (n - m)^2. Show that the two expressions are equal."
- M4.S21.T21.C108: x, y, the figure and the three names are missing. Suggested: "In Fig. 1 three equal rectangles x by y form a capital I; find the area of the region with the slanting lines. Anusha, Vaishnavi and Aditya get x^2 - xy, x(x + 2y) - 3xy and x(x - y). Verify that the three are equal and find the area for x = 8, y = 3."
- M4.S21.T21.C109: the solution never says where the three expressions come from. Suggested additions: "Anusha: the x by x region between the bars minus the middle bar xy. Vaishnavi: the whole rectangle x by (x + 2y) minus the three rectangles. Aditya: the two side regions are each x by (x - y)/2, so 2 x x(x - y)/2."
- M4.S21.T21.C111: `steps_tex[2]` has broken math: `$(p - r)(s - r) = ps - pr -$ rs $+ r^2$`. Suggested: "$(p - r)(s - r) = ps - pr - rs + r^2$, so both methods agree."
- M4.S22.T22.C116: `question_tex` has "$w ft$." (math mode swallows the space) and "$g^2\text{ sq. ft}$."; it also does not say that the path between the two plots is 2w wide while it is w wide at the outside, which the solution uses. Suggested: "...a walking path $w$ ft. wide round them (2$w$ ft. wide between the two plots, see the figure)...".
- M4.S22.T22.C117: `answer_tex` malformed: `$8w^2 + 8gw sq$. $ft$., that is $8w(w + g)$`. Suggested: "$8w^2 + 8gw$ sq. ft., that is $8w(w + g)$ sq. ft."
- M4.S22.T22.C113: the LP answer (ii) lists m^2 + (m - 1)^2 as well as m^2 + (m + 1)^2; the book prints only the second. The LP is right (m - 1 and m are consecutive); no change needed, noted only.

### Class 8 Ch 7, chunk A
- **M1.S3.T3.C8** (solution of FiO Q4): never says which rectangles are similar; it also says "width : height", which has no meaning for tilted rectangles. Suggested closing sentence: "Measuring short side : long side gives about 1 : 3 for A and D, about 2 : 5 for C and E and about 2 : 3 for B, so A and D are similar, C and E are similar, and B is similar to none of the others."
- **M1.S4.T4.C10** (solution of FiO Q5): the example "6 cm : 4 cm" does not match the printed rectangle (about 5 : 3 on the page, no lengths printed); the hint `q_figure` of C9 ("6 cm wide and 4 cm high") is likewise an assumption. The spec follows the LP (3:2). Suggested sentence if the learner is to measure the printed rectangle: "Measure the rectangle; it is about 5 cm by 3 cm, so width : height is 5 : 3. A smaller one: 5 x 1/2 = 2.5 and 3 x 1/2 = 1.5; a bigger one: 5 x 2 = 10 and 3 x 2 = 6." (If this is adopted, the diagram numbers must be changed to match.)
- **M1.S4.T4.C12** (solution of FiO Q7): step 3 gives only the scaled head (2 cm) and torso (6 cm), and no step gives torso : arms although the question asks for it. The figure also labels arms 6 cm and legs 8 cm. Suggested sentences: "Torso : arms is 60 : 60, which is 1 : 1." and "60 x 1/10 = 6 cm for the arms and 80 x 1/10 = 8 cm for the legs."
- **M2.S8.T8.C26** (question of FiO Q6): the question text already states the per-row counts of block (a) (2, 3, 4 grey; 3, 2, 1 coloured) and the totals of block (b) (16 and 12), which the book leaves for the learner to find from the picture, and it speaks of "one block" without saying which bricks form a block. Suggested: ask only "In each wall find the ratio of grey bricks to coloured bricks in one repeating block" and keep the counts in the solution (C27). The decision was not changed (decision 2).
- **Book numbers in the LP.** C9/C10 "Figure it Out, Q1" is book Q5 (p.166); C11/C12 "Figure it Out, Q2" is book Q7 (p.167); C26/C27 "Figure it Out, Q2" is book Q6 (p.166); C28/C29 "Figure it Out, Q3" is Q1 of the 7.6 Figure it Out (p.176). C5/C6 also adds image E, which the book question (D only) does not.
- **M2.S6.T6.C21** (coffee solution): "200 : 400 is 1 : 2, so strong." gives no comparison number as the neighbouring lines do. Suggested: "$200 \div 400 = 0.5$, more than $0.43$, so strong."
- **M2.S10.T10.C34/C35** (Example 2): the LP says "18 glasses in all"; the book says "18 more glasses" but then solves 6 : 10 :: 18 : 30, i.e. 18 glasses in all. The LP wording is the consistent one (decision 1: follow the LP); no change needed.

### Class 8 Ch 7, chunk B
- `M3.S16.T16.C61` (mason, solution step 1): the sum "12 + 12 + 12 + 15 + 9 + 15 + 9 + 9 + 9 + 6 = 108 ft" does not say which wall each term is. Suggested sentence: "Walls: left $12$, inner $12$, right $12$; top $9 + 15$; bottom $9 + 15$; small room left $9$, right $9$, bottom $6$, so $12 + 12 + 12 + 9 + 15 + 9 + 15 + 9 + 9 + 6 = 108\text{ ft}$." (same ten numbers, in an order that follows the figure).
- `M3.S16.T16.C60` (mason, question): the text lists the five printed lengths but the learner needs the picture for the rest; once the token is inserted after the question text this is fine. The book's own sentences "He needs to construct both the outer walls and the inner wall that separates two rooms" were merged into one sentence.
- `M3.S16.T16.C62` (buses, question): LP says "This year we have 204 students" (as the chapter page 18 does); the book's printed answer (page 28) reads "204 students and teachers". Suggested question sentence: "This year we have $204$ students and teachers." (the numbers in the LP answer already treat 204 as the number of people).
- `M3.S16.T16.C64` (Lilavati, question): `question` keeps "O expert businessman! tell me quickly" while `question_tex` has "expert businessman! tell us quickly": the two fields differ from each other and from the book ("O expert businessman! tell me quickly").
- `M2.S11.T11.C40` (Example 4): `question` says "my school" and `question_tex` says "our school" (book: "my school"); the two fields differ.
- `M3.S18.T18.C73` (Example 6): the question ends "...when Neelima is 12?", the book also asks "Would it remain the same?". The answer steps (step 4) answer it. Suggested sentence: add "Does the ratio stay the same?" to the question.
- `lp_book_number` values are LP-internal, not the book's numbers: C46 "Figure it Out, Q1" is book FiO1 Q3; C60 "Figure it Out, Q1" is book FiO2 Q2; C64, C66, C68 "Q3, Q4, Q5" are book FiO4 Q5, Q7, Q9; C44 reads "Ratios and Proportions, Q2" (book FiO1 Q2). Items were found by their text.
- `M3.S13.T13.C49`: the worked example uses 120 : 15 :: 80 : 10 taken from Example 8; the book has no such separate example, so this is an LP-made worked example (fine, listed for completeness).

### Class 8 Ch 7, chunk C
(No LP text was edited and no decision was changed because of these.)

- `M5.S31.T31.C120` (worked example, step 3): "The fourth cell next to a vertical pair would make three verticals if cells 3, 4 and 5 were all vertical" is muddled: cells 3 and 5 are not a pair, cell 4 sits between them. Suggested sentence: "If cell 4 were vertical, cells 3, 4 and 5 would be three verticals in a row, so cell 4 is horizontal."
- `M5.S31.T31.C120` (question): the cells are never numbered, yet steps and answer say "third cell", "cell 4", "cell 6". Suggested addition: "Number the cells 1 to 6 from the left." (The diagram prints position numbers 1 to 6 under the cells for this reason.)
- `M5.S31.T31.C120` (book coverage): the book's Binairo page has a 6 x 6 solved example and three 6 x 6 practice puzzles (P20 grids 3, 4, 5). The LP keeps only a one-row example and its textbook block ends "Solve the following Binairo puzzles." with no puzzle given. Suggested: add the three practice grids as question items (each would be required: DATA_IN_FIGURE and ACTION_ON_FIGURE, with the given cells listed in the inventory descriptions of P20-binairo_grid-3/-4/-5), or drop that sentence.
- `M4.S25.T25.C92` (question) and C93 (steps): the steps say "Partner: 3 x 3 = 9; you: 1 x 3 = 3", but the question never mentions a partner or which share is whose. Suggested sentence: "Share 12 counters between you and your partner in the ratio 3 : 1 (partner : you), and then 42 counters in the ratio 4 : 3."
- Book-number labels differ from the book's own numbering (the LP's own numbering is used for the cards, the `ncert_refs` are right):
  - `M3.S20.T20.C79/C80` "Figure it Out, Q1" is the book's 7.6 Q11 (tractor).
  - `M4.S27.T27.C100/C101` "Figure it Out, Q1" is the book's 7.5 Q2; C102/C103 "Q2" is Q3; C104/C105 "Q3" is Q4; C106/C107 "Q4" is Q5 (the book's 7.5 Q1 is C94 "Ratio Sharing, Q1").
  - `M4.S27.T27.C108/C109` "Figure it Out, Q5" is the book's 7.6 Q4 (crane); C110/C111 "Q6" is Q12 (coin).
  - `M4.S30.T30.C117/C118` "Figure it Out, Q1" is the book's 7.6 Q10 (land price).
  Suggested: label them with the book's numbers (7.5 Q2, Q3, Q4, Q5; 7.6 Q11, Q4, Q12, Q10).
- `M3.S21.T21.C82` (worked example): the book's Activity 2 asks whether price is proportional to volume; the LP question asks "Which size gives the cheapest shampoo per mL?" and the answer says the sachet (about Rs 0.33 per mL) is cheapest. The arithmetic is right (2/6, 154/180, 276/340, 540/1000), only the question differs from the book's. No change needed unless the team wants the book's wording.
- Arithmetic of every pair in the chunk was re-computed and matches the LP text: 100 / 75 = 4/3 h = 1 h 20 min; 20 x 6 = 120 h and 20 x 1.5 = 30 h; 30000000 / 1484 = 20216 and 20000000 / 550 = 36364 (rounded); 12 / 4 = 3 rounds, 42 / 7 = 6; 4500 / 5 = 900; 4000 / 4 = 1000; 5 : 2 :: 30 : 12; 240 / 6 = 40; 40 / 8 = 5 and 15 : 45 = 1 : 3; 3 : 13; 4/10 of 155 = 62; 7.74 x 3 / 4 = 5.805 g, Rs 5.26 + Rs 2.59 = Rs 7.85; 1e9 / 43560 = 22956.8; 3.6e9 / 43560 = 82645.

### Class 8 Ch 8, chunk A
- **M1.S3.T3.C8 / C9 (Example 1).** The question text is just "Yellow paint?" and lacks the data. Suggested: "Surya mixes red paint and yellow paint. The red paint makes up 3/4 of the mixture, which is 75%. What percentage of the colour is made with yellow?" (the diagram carries the bar). The solution step "100% - 75%" presupposes the 75%.
- **M1.S3.T3.C10 / C11 (Example 2).** The question text is just "Method 3 boxes" and lacks the task. Suggested: "Surya saves 2/5 of his prize money for a canvas. Fill the four empty boxes with the percentages that go under 1/5, 2/5, 3/5 and 4/5 of the bar."
- **M1.S3.T3.C12 / C13 (Example 3).** The question text "Which variety is more sugary?" lacks the data. Suggested: "Sugar makes up 9/34 of Variety 1 and 13/45 of Variety 2 of a biscuit. Which variety is more sugary?" Also: the book prints 28.88% for Variety 2; 13/45 = 28.888...% which rounds to 28.89%, so the LP's "about 28.89%" is right and the book's value is a cut-off (no diagram is affected).
- **M1.S4.T4.C20 / C21 (FiO Q4).** The question text ends with a bracket that describes the picture: "(Line from Start to Finish with runners A, B, C, D; options 55%, 20%, ...)". With the diagram placed after the question this is a duplicate description; suggest removing it (or keeping only the six options if the build wants them in text).
- **M1.S4.T4.C17 (FiO Q2 solution).** Step 2 reads "Used as the diagnostic above; if already used there, ask for the reason only." That is an instruction to the AI, not a student sentence. Suggest deleting the step.
- **M1.S4.T4.C23 (FiO Q5 solution).** The only step compares 3/11 with 3/10 = 30%, which is correct but never reaches the asked comparison with 61%. Suggested addition: "So 3/11 is less than 30%, which is less than 61%."
- **M2.S5.T5.C25 ("Anything interesting in the table?").** The table itself is not in the text, so the student cannot see what to look at. Suggested: add the completed LaTeX table (rows 25%, 10%, 20%, 5% for 100, 200, 50, 80, 10, 35, 287, values as in the C26 answer) before the question, or write "In the table you just filled in, is there anything interesting?" and place the LaTeX table.
- **M2.S5.T5.C26 blocks 0 and 1.** The two blocks have the identical question, steps and answer text (only example_id differs: free_hand_40 and free_hand_15). Also the question gives the row and column labels in words only. Suggested: keep one block with the LaTeX table, or make block 1 only the 15% row.
- **M2.S5.T5.C27.** Step 1 says "Say a recipe from I2 before computing." "I2" is an internal image code, meaningless to the student. Suggested: "Say a recipe from the building-block picture (50%, 25%, 10%, 5%) before computing."
- **Diagnostic blocks (M1.S2.T2.C4, M2.S5.T5.C24, M2.S5.T5.C31).** The text holds the internal sentence "Act on the diagnosis table." and the answer ("Answer: (b), reason (i)") inside the same text as the question; check that the build shows these only to the AI.
- **M1.S1.T1.C1.** Block 0 of the concept (not a unit) mentions "a bar picture" in the recap; the five worked examples themselves are text and have no picture.

### Class 8 Ch 8, chunk B
The LP question texts of this topic are one-line stubs that omit the data of the examples. I did not change any decision because of it. For each, the sentence the card needs (suggested):

- M2.S6.T6.C33 (Example 1, Q): "Who ate more sugar?" lacks everything. Suggested: "Madhu ate 120 g of biscuits that have 25% sugar. Madhav ate 95 g of biscuits that have 35% sugar. Who ate more sugar?"
- M2.S6.T6.C35 (free-hand table, Q): "The table (25%, 10%, 20%, 5%, then 40% and 15%) for 100, 200, ..." has no instruction. Suggested: "Without pen and paper, find 25%, 10%, 20%, 5%, then 40% and 15%, of 100, 200, 50, 80, 10, 35 and 287 and write them in the table. The first entry (25% of 100) is 25." Also the book table has only the rows 25%, 10%, 20%, 5%; the rows 40% and 15% come from the later Math Talk prompts (the LP merged them, which is fine, but the hint `q_figure` still says four rows).
- M2.S6.T6.C39 (FDP table, Q): "Complete the FDP table" does not give the table. Suggested: "Complete the table: Per cent 50%, 100%, 25%, 75%, 10%, 1%, 5%, 43%; Fraction (50/100 is given under 50%); Decimal (0.5 is given under 50%)."
- M2.S6.T6.C41 (Example 3, Q): "Zubin's minimum score" lacks the data. Suggested: "The maximum marks in a test are 75. Students who score 80% or above get an A grade. How much should Zubin score at least to get an A grade?"
- M2.S6.T6.C43 (Example 4, Q): "Millet kanji" lacks the data. Suggested: "A millet kanji is made by mixing millet and water in the ratio 2:7. What percentage of the mixture is millet? How much millet is needed to make 500 ml of the mixture?"
- M2.S6.T6.C45 (Example 5, Q): lacks the data. Suggested: "A cyclist cycles from Delhi to Agra and completes 40% of the journey. He has covered 92 km. How many more kilometres does he have to travel to reach Agra?"
- M2.S6.T6.C47 (Example 6, Q): "Days 1 to 4" lacks target and sales. Suggested: "Kishanlal aims at daily sales of at least 5000 rupees. His sales on Days 1 to 4 were 2000, 3500, 5000 and 6000 rupees. What percentage of the target did he achieve on each day?"
- M2.S6.T6.C49 (Example 6, Q): "Days 5 and 6" lacks target and sales, and (because the question diagram is optional and not added) the text must carry them. Suggested: "Kishanlal's daily target is 5000 rupees. On Day 5 his sales were 7800 rupees and on Day 6 they were 9550 rupees. What percentage of the target did he achieve on each day?"
- M2.S6.T6.C51 (Example 6, Q): "Days 7 and 8" lacks the percentages and target. Suggested: "On Day 7 Kishanlal achieved 150% of his 5000-rupee target and on Day 8 he achieved 210% of it. Find the sales on these two days."
- M2.S6.T6.C53 (Example 11, Q): "The fraction and decimal table" lacks the nine percentages and the marking instruction (a diagram token will follow the text). Suggested: "Complete the table of fractions and decimals for 90%, 110%, 200%, 250%, 15%, 173%, 358%, 28.9% and 305%. Then mark their approximate places on the 0% to 400% diagram; 90% is marked for you." The table itself should be a LaTeX array in the question text.
- M2.S6.T6.C55 (Example 7, Q): "Wheat harvest" lacks the data. Suggested: "A farmer harvested 260 kg of wheat last year and 650 kg this year. What percentage of last year's harvest is this year's harvest?"
- M2.S6.T6.C46 (Example 5, solution): the steps give no numbers. Suggested steps: "40% is 92 km, so 20% is 46 km. The remaining 60% is three pieces of 46 km = 138 km."
- M2.S6.T6.C48 (Example 6, solution): suggested step "2000/5000 x 100 = 40%, 3500/5000 x 100 = 70%, 5000/5000 x 100 = 100%, 6000/5000 x 100 = 120%" so the numbers are in the solution.
- M2.S6.T6.C36 (free-hand table, solution): the steps "Row by row, easiest column first;" are not a working; the two hints 40% = 4 x 10% and 15% = 10% + 5% are fine.
- Wrong or clashing book numbers (`book_number`): C37/C38 and C35/C36 are both labelled "Example 2", but the book's Free-hand table is an unnumbered "Try" and Example 2 is the FDP Trio (the 10% question and the FDP table both belong to it); C39/C40 (FDP table) is labelled "Example 4" which clashes with C43/C44 "Example 4: Millet"; C49, C51, C53 are labelled "Example 9", "Example 10", "Example 11" but the book has only Examples 1 to 7 (Days 5 and 6, Days 7 and 8 are parts of Example 6; the table and number line is an unnumbered prompt on p.12). Suggested labels: C35 "Free-hand Computations", C39 "Example 2 (FDP table)", C49 "Example 6 (Days 5 and 6)", C51 "Example 6 (Days 7 and 8)", C53 "Percentages beyond 100: table and number line".

All LP answers were recomputed against the book and are correct (30 g and 33.25 g; the 42 table values; the FDP fractions and decimals; 60 marks; 22.22% / 77.78% / 111.1 ml; 138 km and 230 km; 40%, 70%, 100%, 120%; 156% and 191%; 7500 and 10,500; the nine fractions and decimals of C54; 250% = 2.5 times). No solution contradicts the book.

### Class 8 Ch 8, chunk C
(Nothing was edited; each is a suggestion.)

- **M3.S8.T8.C82, block 0 (Tomatoes):** the question is only the word "Tomatoes" and the step "12 over the old price 30." omits the new price. Suggested question: "The price of 1 kg of tomatoes was Rs 30 three years ago and is Rs 42 now. Find the percentage increase." Suggested step: "Increase = 42 - 30 = 12; 12 over the old price 30 gives 12/30 x 100."
- **M3.S8.T8.C82, block 1 (Footfall):** same problem. Suggested question: "The average footfall in a theatre was 160 before COVID and is 100 now. Find the percentage decrease." Suggested step: "Decrease = 160 - 100 = 60; 60 over the old footfall 160 gives 60/160 x 100."
- **M3.S8.T8.C82, block 2 (Check my thinking):** the learner-visible text ends with "Act on the diagnosis table.", an authoring instruction; remove it. The block also has no `steps` / `answer` fields (the answer "(b), reason (ii)" is only inside `text`).
- **M2.S7.T7.C57 (Q1 question):** the question text carries a parenthesis describing the figure ("Pairs of bar models: (i): 5 cells, one cell = 20% ..."). It reads like an authoring note and repeats the new diagram. Suggested question: "1. Find the missing numbers. The first problem has been worked out."
- **M2.S7.T7.C60 (Q2 solution):** the only step is "Each gets a quick bar sketch." and says nothing about what the sketches show. Suggested step (it now follows the six-panel figure): "In each bar, split the whole into equal cells and shade the cells that make the asked share."
- **M2.S7.T7.C66 (Q5 solution), part (iv):** "the $AI$ checks them" is internal wording in a learner answer, and `$AI$` in LaTeX is set as a variable. Suggested: "(iv): Any two questions of the same kind, with their answers, are fine."
- **M2.S7.T7.C78 (Q11 solution):** "The $AI$ uses the current year's figure if the student looks it up." has the same problem. Suggested: "Use the latest world population the student finds; with 8.2 billion (2025) the answer is about 7.4 billion."
- **M2.S7.T7.C67 (Q6 question):** `question_tex` writes "(ii)" without the colon that (i) and (iii) have: "(ii) \underline{...} is 40% of 4." Suggested "(ii):".
- The LP numbers checked out against the mathematics for Q1 to Q12 (for example 29% of 43 = 12.47, 92% of 110 = 101.2, 1% of 168 h = 1.68 h = 100.8 min, shown as "about 101"); no solution contradicts the book.

### Class 8 Ch 8, chunk D
(No LP text was edited; no decision was changed because of these.)
- M3.S9.T9.C83 (Example 1 question): text is only "Eesha: English or Science?"; the marks are missing. Suggested: "Eesha scored 42 out of 50 in English and 70 out of 80 in Science. She lost only 8 marks in English but 10 in Science, so she thinks she did better in English. Reema says Science, since she scored more marks there. Vishu says the scores cannot be compared because the maximum marks differ. Who is correct?"
- M3.S9.T9.C85 (Example 2 question): text is only "$KYC$ table", with no label data and no table. Suggested: "DEF pack (total 150 g): sugar 99 g, milk solids 30 g, badam powder 12 g, food chemicals 9 g. Zacni pack (total 400 g): sugar 272 g, milk solids 64 g, badam powder 40 g, food chemicals 24 g. Complete the table of percentages (DEF sugar is 66%): which product has the larger share of badam, which the smaller share of food chemicals?" (a LaTeX array for the table is in the item's `text_alternative`). Also KYC should be plain text, not math mode.
- M3.S9.T9.C86 (Example 2 answer): `answer_tex` has "$(6$%)" (the bracket is opened inside the math and closed outside); write "(6%)" as "($6$%)". Values checked: 99/150, 30/150, 12/150, 9/150 = 66, 20, 8, 6; 272/400, 64/400, 40/400, 24/400 = 68, 16, 10, 6; both rows add to 100.
- M3.S9.T9.C87 (Example 3 question): the two statements are missing. Suggested: "(i) The population of this state in 1991 is 165% of that in 1961. (ii) The population of this state has increased by 65% from 1961 to 1991. Do the two statements mean the same thing?"
- M3.S10.T10.C90 (petrol answer): the learner text shows an internal code, "(M_2)" / "(M2)". Suggested: "Option (ii), 40%, is wrong: it takes the new price (₹100) as the base instead of the old price (₹60)." Also "About 66.66%" is 66.67% rounded; the book's option (iv) prints 66.66%, so keep the LP wording but it is a truncation.
- M3.S10.T10.C96 (cameras answer): explains only why (v) is wrong, but (i), (ii), (iv), (v) and (vi) are all wrong. Suggested: "Only (iii). After an 85% fall, 15% is left, so now is 15% of a decade ago. (i) uses 85% as what is left. (ii), (iv), (v) turn the base around: a decade ago was about 667% of now (1/0.15), not 85%, 15% or 185%."
- M3.S11.T11.C97 (Kishanlal's profit): no numbers in the block. Suggested: "Kishanlal buys a sweater at ₹300 (cost price) and sells it at ₹430 (selling price). What is his profit?" and step "430 - 300 = 130".
- M3.S11.T11.C98 (crayon box): the unit's ncert_refs says "1.3.ex5_per_kg", which is Raghu's rice; the crayon question is the unnumbered one on p.17. The block text also holds tutor wording ("How sure are you?" with three emoji, "Act on the diagnosis table.") that reads as a script, not learner text. The option arithmetic is consistent: (a) 37.50 = 50 - 12.50, (b) 40 = 50 / 1.25, (c) 62.50 = 50 + 12.50.
- M3.S11.T11.C99 (Per kg?): the question gives no data. Suggested: "Raghu bought rice at ₹35 per kg and sold 10 kg for ₹300, that is ₹30 per kg. Is the percentage loss per kg the same as the loss on all 10 kg?" LP answer "about 14.29%" is the correct rounding of 5/35 = 50/350 = 14.2857; the book prints 14.28% in Example 5 (see below).
- M3.S11.T11.C101 (gross and net profit): no data in the block. Suggested: "Kishanlal's sales last month were ₹80,000; the goods he sold cost ₹48,000; his other expenses were ₹8,000. Find the gross profit and the net profit." Checked: 32,000 and 24,000.
- M3.S11.T11.C102 (Manisha): no data in the block. Suggested: "Manisha buys a bag of fertiliser at ₹500 and sells it at ₹750. Is her profit 50% or 33.33%? In a month her sales are ₹1,50,000, the goods cost ₹1,00,000 and expenses are ₹5,000: what percent of the monthly revenue is her net profit?" Checked: 250/500 = 50%, 250/750 = 33.33%, 45,000/1,50,000 = 30%.
- M3.S11.T11.C104 (A Bill from Home): the "answer" is a tutor instruction ("Open; the AI checks the student's bill"), not learner text. Worth rewording or hiding.

### Class 8 Ch 8, chunk E
Concept id, what is wrong or missing, suggested sentence.

- **M3.S12.T12.C105** question "Kishanlal's profit %": no data (cost 300, selling price 430). Suggest: "Kishanlal buys a sweater for ₹300 and sells it for ₹430. Find his percentage profit."
- **M3.S12.T12.C106** step "130 over the CP of 300.": does not say where 130 comes from. Suggest: "Profit = ₹430 − ₹300 = ₹130, and the cost price (₹300) is the 100%, so the profit is 130 over 300."
- **M3.S12.T12.C107** question "Wholesaler and manufacturer": no data; everything is in the picture. Suggest: "Use the prices in the picture. Find the profit percentage of the wholesaler and of the manufacturer." (the answer lists wholesaler first, then manufacturer: keep that order.)
- **M3.S12.T12.C108** steps "47 over 253; 23 over 230.": not said which is which or where 47 and 23 come from. Suggest: "Wholesaler: profit 300 − 253 = 47 over the CP 253. Manufacturer: profit 253 − 230 = 23 over the CP 230."
- **M3.S12.T12.C109** question "Notebooks": no data. Suggest: "Shambhavi buys 200-page notebooks at ₹36 each and sells them with a profit margin of 20%. Find the selling price of one notebook."
- **M3.S12.T12.C110** step "36 × 1.2.": Suggest: "20% profit on the cost: selling price = 36 × 1.2 = ₹43.20 per notebook."
- **M3.S12.T12.C111** question "Crayons": no data. Suggest: "Shambhavi sells crayon boxes at ₹50 each with a profit margin of 25% on the cost. At what price did she buy one box from the wholesaler?"
- **M3.S12.T12.C112** step "50 ÷ 1.25.": Suggest: "The selling price ₹50 is 125% of the cost price, so cost price = 50 ÷ 1.25 = ₹40."
- **M3.S12.T12.C113** question "Raghu's loss %": no data. Suggest: "Raghu bought rice at ₹35 per kg and sells 10 kg for ₹300. Find his percentage loss."
- **M3.S12.T12.C114** step "50 over the CP of 350." and the answer text: the step does not show 10 x 35 = 350 and 350 − 300 = 50; the answer carries a parenthetical "(the book shows 14.28%, cut off rather than rounded)" that a learner will read as part of the answer. Suggest: "Cost = 10 × ₹35 = ₹350; loss = ₹350 − ₹300 = ₹50; loss over the CP: 50 over 350." and move the book remark to a teacher note.
- **M3.S12.T12.C115** question "Damaged vase": no data. Suggest: "Shyamala bought a decorative vase for ₹2650. It is slightly damaged and she sells it at a loss of 18%. How much does she get? Try drawing a rough diagram first."
- **M3.S12.T12.C116** step "Keep 82% of 2650, or subtract 18% of it.": Suggest: "Two ways: 82% of 2650 = 0.82 × 2650 = 2173, or 2650 − (18% of 2650 = 477) = 2173."
- **M3.S12.T12.C117** question "Strawberries": no data. Suggest: "Snehal sells strawberries at ₹80 per kg and makes a 12% loss. What was the cost price per kg?"
- **M3.S12.T12.C119** question "Cooker": no data. Suggest: "A cooker with MRP ₹1800 is sold at a 35% discount. What is the selling price? If the cost price was ₹900, what is the percentage profit?"
- **M3.S12.T12.C120** step 2 "profit 270 over 900": does not show 1170 − 900 = 270. Suggest: "Step 2 base is the CP: profit = 1170 − 900 = 270, so 270 over 900."
- **M3.S12.T12.C121** question "Is the bill correct?": the bill exists only in the figure (that is why the figure is required); fine once the figure is added, but "Check if the calculations on the bill are correct." matches the book better.
- **Concept names and book numbers**: C105/C106 are named "Example 4" and C111/C112 also "Example 4"; C107/C108 "Example 2", C109/C110 "Example 3", C117/C118 "Example 7", C119/C120 "Example 8", C121/C122 "Example 9". In the book only Kishanlal (Ex 4), Raghu (Ex 5) and the vase (Ex 6) are numbered; the wholesaler/manufacturer, notebooks, crayons, strawberries, cooker and bill items are unnumbered "?" prompts, and the book's real Examples 7, 8 and 9 (the ₹6000 deposit, the total received, compounding) are later in the chapter (chunk F). The labels clash with those. Suggest names such as "Try this: wholesaler and manufacturer", "Try this: notebooks", "Try this: crayons", "Try this: strawberries", "Try this: cooker", "Try this: the bill".

### Class 8 Ch 8, chunk F
Only listed, nothing changed (decision 2 of 23 Nov).

T13 (Figure it Out):
- **C131 / C132, C133 / C134, C135 / C136, C137 / C138:** the LP copies the book's printed question numbers (3, 4, 6, 7). On p.20 the book restarts numbering at 3 (a print slip: it follows 5, so these are 6, 7, 9, 10 in sequence of the set), so the plan shows "3." twice. Suggested: drop the printed number from `question_tex` or use the corrected 6, 7, 9, 10 (and the book_number fields likewise).
- **The set also has four questions that are not in my units:** printed 5 on p.19 (petrol price rise, 6 options), printed 5 on p.20 (rice inflation 38 to 42), 8 (elephants, p x 1.05) and 9 (cameras, demand fell by 85%). Please check they exist elsewhere in the plan (they do not appear in chunk F).
- **C124 (Ans1):** the steps are only "Profit over cost." Suggested: "Profit = 110 - 75 = 35. Profit margin on cost = 35/75 x 100, about 46.67%."
- **C128 (Ans3):** steps and answer contain teacher-facing text: "Discuss the base first.", "(see 4.4)", "Accept either when the student names the base; a good 4.4 check." Suggested: "Margin on revenue: profit = 25% of 2.5 crore = 0.625 crore, so costs = 2.5 - 0.625 = 1.875 crore. If the margin were taken on cost, cost = 2.5 / 1.25 = 2 crore."
- **C136 (Ans7):** the answer ends "...which is 72; M4". The misconception code "M4" has leaked into learner text. Suggested: "90 / 1.2 = 75 (not 90 - 18 = 72, because 18 is 20% of 90, not of the number)."
- **C138 (Ans8):** the only step is "The topic's one faded multi-step problem (see faded ladder below)." This is not a solution. Suggested: "Buffalo 1 (profit 5%): cost = 80,000 / 1.05, about 76,190. Buffalo 2 (loss 10%): cost = 80,000 / 0.9, about 88,889. Total cost about 1,65,079; total selling price 1,60,000; loss about 5,079, which is about 3.08% of the cost." (checked: 5079.37 / 165079.37 = 3.077%).
- **C125:** `question` says "I am a carpenter", `question_tex` says "You are a carpenter" (small mismatch; the book has "I").

T14:
- **C139 (worked example):** the question text is only "Interest and amount after 1 year"; the data (6000, 10% p.a., 1 year) appears only in the steps. Suggested: "A bank pays 10% p.a. on a fixed deposit. If 6000 rupees is deposited for 1 year, what is the interest and what is the amount after 1 year?"
- **C140 (check my thinking):** the text ends "Act on the diagnosis table." (an internal instruction in learner text). Answer (b) 1100 is right: year-2 interest is 10% of 11,000.

T15:
- **C143 (Example 7 question):** the text is only "Example 7". Missing: "If one deposits 6000 rupees in the bank at 10% p.a., what is the amount after 3 years? Option 1: the interest is paid out every year. Option 2: the interest is added back (compounding)." The rate 10% p.a. appears in neither the question nor the solution text; the diagram shows it (from the book).
- **C144 (Example 7 answer):** "7800 against 7986" has no labels. Suggested: "Option 1 (interest paid out): 7800. Option 2 (compounding): 7986."
- **C145 (Example 8 question):** only "Example 8". Suggested: "What percent is the total amount received of the amount deposited (6000), in both options of Example 7?"
- **C147 / C148:** named "Example 3: Q / Ans" (and book_number "Example 3: Compounding: total interest in both options"), but this is the Math Talk on p.24, not an Example 3 (the book's Example 3 is on p.16). The question text "Math Talk: total interest" lacks the question. Suggested: "What is the formula for the total interest at the end of the maturity period, for each of the two options (without compounding and with compounding)?"
- **C149 (Example 10 question):** only "TV value after 1 year", no data. Suggested: "A TV is bought at 21,000 rupees. After 1 year its value depreciates by 5%. Find the value of the TV after one year."
- **C151 (Example 11 question):** only "Village after 3 decades", no data. Suggested: "The population of a village is reducing by about 10% every decade. If the current population is 1250, what is the expected population after 3 decades?"
- **C152 (Example 11 answer):** "About 911, i.e. around 910" is fine, but the book shows two routes (911.25 without rounding, 912 rounding each step) before saying "around 910"; the LP states only the first.

### Class 8 Ch 8, chunk G
- **M4.S16.T16.C164 (Q6 answer), steps_tex**: "The topic's faded problem (see the faded ladder)." is a pointer, not a solution step. Suggested: "Giridhar (no compounding): $12,500 \times 0.12 \times 3 = 4500$. Raghava (compounded): $12,500 \times 1.1^3 = 16,637.50$, so the interest is $16,637.50 - 12,500 = 4137.50$."
- **M4.S18.T18.C177 (Peaceful Knights), question**: "Place 8 peaceful knights" lacks the board and the rule. Suggested: "Place 8 knights on an 8 x 8 chess board so that no knight attacks another. A knight moves two steps in one direction and one step at right angles to it (an L-shape)." The steps and answer also assume the board colouring; suggested answer wording: "For example, the 8 light squares of the first two rows (row 1: columns 2, 4, 6, 8; row 2: columns 1, 3, 5, 7)."
- **M4.S17.T17.C171 blocks 0 and 1**: the block `question` fields are only titles ("Would you rather?", "20% or Rs 50 off?"); the data sit in the concept's textbook-text block. Suggested block 0: "Option A: deposit Rs 100, get back Rs 300. Option B: deposit Rs 1000, get back Rs 1500. What is the percentage gain of each?" Suggested block 1: "A shop offers 20% off or Rs 50 off on any purchase above Rs 150. Which is better for a bill of (i) Rs 180, (ii) Rs 225, (iii) Rs 300?"
- **M4.S17.T17.C172 block 1 (Check my thinking)**: the `question` field stops at "Compared with the start it is" (no options a/b/c); the options and the answer are in the `text` field only. Suggested: "A price rises by 10% and then falls by 10%. Compared with the start it is (a) the same (b) 1% lower (c) 1% higher."
- **M4.S17.T17.C173 blocks 0-3**: the questions "(i) No loss?", "(ii) Sold for Rs 12,000", "(iii) Break-even discount", "Arun's statement" are fragments that depend on the Example 13 set-up (50% margin, then 50% discount; Ariba has 120% of Arun's marbles) held in another block of the same concept. Suggested prefix for each: "Surbhi marks goods up by 50% and then gives a 50% discount." and, for Arun: "Ariba says she has 120% of the marbles Arun has. What can Arun say about his marbles compared with hers?"
- **M4.S17.T17.C176 (Summary)**: the worked-example answer "The 100%, the base" is fine; the question is a reflection with no data, so nothing is missing.
- **M4.S16.T16.C166 (Q7 answer)**: "just over 7 years (doubled by the end of year 8)" is correct (exact 7.27 years) but a reader could miss that compounding is paid per year; suggested addition: "(after 7 years Rs 1000 has become about Rs 1949; after 8 years about Rs 2144)".

### Class 8 Ch 8, chunk H
- **M4.S19.T19.C178 (Q2 question):** the card list is run together ("13% 8% 18% 10% 1% 35% 2% 2% 0.1%"), fine for the book but hard to read. Suggested: "Options: 13%, 8%, 18%, 10%, 1%, 35%, 2%, 2%, 0.1%."
- **M4.S19.T19.C179 (Q2 answer):** (a) says "about 4.2%" for the USA and then "4% is not among the options", which reads as if the answer were 4%; (b) it contains teacher-facing instructions in a student answer ("tell the student the true value and praise them for spotting it", "The other options are distractors."). Suggested: "USA: 347 million is about 4.2% of 8.2 billion. This is not among the options (and 2% is printed twice), so no card fits the USA; the other cards are distractors."
- **M4.S19.T19.C183 (Q4 answer):** "(iii) and (iv) are the $M_5$ trap." "M5" is an internal module code that means nothing to a student. Suggested: "(iii) and (iv) wrongly add or ignore the percentages; changes of percent multiply, they do not add."
- **M4.S19.T19.C186 (Q6 question):** question_tex contains an editor's bracket "(Dot-grid figure: an 8 x 8 square divided into A ... into D and E.)". Once the diagram is placed this bracket is redundant and reads as a note. It also does not say which triangle is E (D is the upper-left, E the lower-right one). Suggested: delete the bracket and keep "What percentage of area is occupied by the region marked E in the figure?"
- **M4.S19.T19.C187 (Q6 answer):** step 1 "Count squares: the whole is 8 x 8, 64 squares;" ends with a semicolon and step 2 is fine; suggested: "The whole big square is $8 \times 8 = 64$ small squares." and "E is half of a $4 \times 4$ square, so $8$ squares; $\frac{8}{64} = 12.5$%."
- **M4.S19.T19.C190 / C191 (Q8):** the LP answer says "Book data issue: ..." inside the answer; it is a note to the content team, not student text. Suggested: "24% of 160 is 38.4, which is not a whole number of students, so the numbers cannot all be exact; say about 38 and discuss why."
- **M4.S19.T19.C198 (Q12 question):** "(Label: Potato 70%, ...; net quantity 65 g)" is an editor's bracket describing the picture; once the label diagram is placed it is redundant. Suggested: "The percentage of ingredients in a 65 g chips packet is shown in the picture. Find out the weight each ingredient makes up in this packet." (the picture carries the label).
- **M4.S19.T19.C204 (Q15 question):** the long bracket "(Bar graph 'Ability to use computer by age and gender (2023)' - Children: Female 4%, Male about 5%; ... Subtitle: ... Source: ...)" is an editor's description of the graph; redundant after the diagram is placed. Suggested: delete it and keep "Look at the following graph." Also the LP says "Male about 5%" for Children, which the book itself does not print.
- **M4.S19.T19.C205 (Q15 answer):** "(iii) ... Not valid" is stronger than the book supports; the graph only shows percentages, so the statement "cannot be concluded" is the accurate verdict. Suggested: "(iii) cannot be said: the graph shows percentages within each group, not how many people each group has."
- **Duplicated numbering:** each answer's `text` field starts the steps with "$1$." and the question concepts have the book number as a prefix ("$2$. The population ..."); harmless, but the steps_tex of C179 ("Estimate with standard form, then match.") and C189 ("Compute each pair, then generalise with algebra.") are one-line placeholders, not steps. Suggested: write the actual estimate (for example $83$ million $\approx 8.3 \times 10^{7}$, $8.2$ billion $= 8.2 \times 10^{9}$, ratio about $1$%).

### Class 8 Ch 9, chunk A
- **M1.S2.T2.C6** question/steps: the pieces 5-8 are placed "against one side of Square 1" without saying which side each piece takes; "Square 1" and "Square 2" exist only in the book's picture. Suggested sentence: "Place piece 5 on the left side of Square 1, piece 6 on the top, piece 7 on the right and piece 8 on the bottom (any order gives the same shape)."
- **M1.S2.T2.C7** question: "Adding more lines gives a sequence of squares" does not say which squares. Suggested: "On the same grid of 8 small triangles look at the small square, the tilted square and the big square. How many small triangles make each of these squares?"
- **M1.S2.T2.C8** question: "All these small triangles" has nothing for "these" to point at. Suggested: "In the figure of the square on the diagonal with the extra east-west and north-south lines (8 small triangles in all), all the small triangles are congruent. Can you explain why?"
- **M1.S2.T2.C9** question: "the dotted square" is not introduced. Suggested: "the dotted square built on the diagonal of the original square".
- **M1.S2.T2.C11** question: P, Q, R, S are used before they are placed (step 1 says they are midpoints). Suggested: "P, Q, R and S are the midpoints of the bottom, right, top and left sides of the paper." The centre of the paper has no name; steps 2, 3 and 7 say "the centre".
- **M2.S3.T3.C14** steps: P, Q, R, S, U, V are used without saying which triangle is meant or where U and V are. Suggested first line: "Let PQS be the isosceles right triangle with the right angle at P, PS = PQ = a and hypotenuse SQ = c; R is the fourth corner of the square PQRS, and SQVU is the square on SQ, with U above R and V to the right of R."
- **M2.S5.T5.C28** steps: "the unit square PEAR", "ER" and "REST" are used without a description of where P, E, A, R, T, S are. Suggested: "Name the triangle PER with the right angle at P (PR = PE = 1); A is the fourth corner of the unit square PEAR; T is directly above A and S directly to the right of A, so REST is the square on ER."
- **M2.S5.T5.C33** question: "pieces 1 and 2, and 3 and 4" without saying which triangle is which. Suggested: "(in the book's picture pieces 1 and 3 are the lower-left triangles and pieces 2 and 4 the upper-right triangles)".
- **M2.S5.T5.C34** answer: "put the four right-angle corners together at the centre" does not say which piece goes where; suggested: "for example piece 1 upper right, 2 upper left, 3 lower left, 4 lower right".
- **M2.S3.T3.C19** `book_number` reads "Chapter Exercises, Q1" while the book heading at the end of section 2.7 is "Figure it Out", Q1 (p.52). Not wrong, only the label.
- No LP/book numeric contradictions found. All sums, squares and bounds were re-computed (1.1^2 to 1.415^2 of p.6; 4.2^2/4.3^2 for 18, 5.6^2/5.7^2 for 32, 8.4^2/8.5^2 for 72, 11.3^2/11.4^2 for 128, 12.7^2/12.8^2 for 162, 7.07^2/7.08^2 for 50).

### Class 8 Ch 9, chunk B
- **M3.S6.T6.C40, C41, C42**: the question and steps use T, U, V, W, X (and "the 4-sided figure T + U + V") without ever defining them; they exist only in the figure. Suggested sentence for the question or the first step: "Two squares of sides a and b are joined; T, U, W and X are four congruent right triangles with perpendicular sides a and b, and V is the five-sided middle piece."
- **M3.S6.T6.C42**: steps 2 and 3 name W and X but the book's angle figure has no piece letters. The diagram I specified shows W and X. If you prefer a text fix: "W is the lower-left triangle and X the lower-right triangle."
- **M3.S6.T6.C43**: step 5 says "turn each right triangle a quarter turn" without a direction. Suggested: "turn the left triangle a quarter turn anticlockwise about the top-left corner of the small square, and the right triangle a quarter turn clockwise about the top-right corner of the large square." The question also should say which square is larger: "(a < b)".
- **M3.S6.T6.C45**, step 5: "Baudhayana (c. 800 BCE)" is not in this chapter's text (page 15 gives only Pythagoras c. 500 BCE and "a couple hundred years" earlier). Not wrong, but a date from outside the book.
- **M3.S8.T8.C55 blocks 5 to 9**: the question text describes each printed triangle in words ("a thin tilted right triangle with sides 4 and 10 at the right angle"); once the diagram is placed after the question these phrases are redundant; keep or trim.
- **M3.S8.T8.C55 blocks 1 to 4 and 5 to 9 versus T9**: the same book question sets are split across topics: Q4 (i) is in T9 (C58/C59, whose `ncert_refs` list (i) to (v) but whose only item is (i)) while Q4 (ii) to (v) are practice blocks here; Q2 (a) is in T9 (C60/C61) while Q2 (b) to (f) are practice blocks here. The blocks also point at T9 videos (`M3.S9.T9.C59.VID1`, `M3.S9.T9.C61.VID1`). Not a diagram problem, but chunk C should give Q2 (a) the same decision as (b) to (f): question figure required.
- **M3.S7.T7.C47**: the question refers to "the earlier method" with no figure or link; fine as text.
- No other number, step or answer in the 27 items contradicts the book; I recomputed every sum, square and bounding interval of the T8 blocks (13, 12, 25, 10, 13, 81, 100, 250, 1296 and the decimal bounds) and all agree.

### Class 8 Ch 9, chunk C
- **M3.S9.T9.C60** (question, "Chapter Exercises, Q2 (a)"): the text says "Find the missing sidelengths in the following right triangles:" but lists only part (a) (plural "triangles"). Parts (b)-(f) are separate blocks in `M3.S8.T8.C55`; the same NCERT question is split over two topics (T9 for (a), T8 for (b)-(f)). Suggested sentence for C60: "Find the missing sidelength in this right triangle: the sides at the right angle are 7 and 9." Also the same for **C58** (Q4 (i) here, (ii)-(v) in `M3.S8.T8.C55` blocks 1-4): "Find the missing sidelength when a = 5 and b = 7."
- **M3.S9.T9.C58** `question_tex` / `text`: "Let a, $b$ and $c$ ..." the first letter is outside math mode. Suggested: "Let $a$, $b$ and $c$ denote the lengths of the sides of a right triangle, with $c$ the hypotenuse. Find the missing sidelength when $a = 5$, $b = 7$." Also "(i):" has a stray colon.
- **M3.S9.T9.C60**: `question_tex` has "$(a)$:" with a stray colon before the description.
- **M3.S9.T9.C63** `steps_tex[1]`: "so $c$ is more than a." The letter a is plain text; suggest "$a$". Same for "more than a" in the plain `steps`.
- **M3.S11.T11.C77** `question_tex` / `text`: "Is $(3k$, $4k$, $5k) a$ Baudhayana triple ..." has the closing bracket and the word "a" inside the last math segment. Suggested: "Is $(3k, 4k, 5k)$ a Baudhayana triple for every positive integer $k$?"
- **M3.S11.T11.C80** `steps_tex`, `answer_tex`, `text`: triples are written as "$(7$, $24$, $25)$" (brackets and numbers split over three math segments). Suggested: "$(7, 24, 25)$" and so on.
- **M3.S11.T11.C84** `steps_tex` and `answer_tex`: same split-bracket style "$(8$, $15$, $17)$". Suggested: "$(8, 15, 17)$".
- **M3.S11.T11.C86** `steps_tex[0]`: "greatest common factor of a, $b$ and $c$" - the first "a" is plain text. Suggested: "of $a$, $b$ and $c$". `steps_tex[2]` writes "$(\frac{a}{f}$, $\frac{b}{f}$, $\frac{c}{f})$": suggested "$\left(\frac{a}{f}, \frac{b}{f}, \frac{c}{f}\right)$".
- **M3.S11.T11.C88** `answer_tex`: "$6$ by $8 (10)$" mixes math and text brackets; suggested "$6$ by $8$ (diagonal $10$)" and the same for the other pairs.
- **M3.S9.T9.C57** `steps_tex[0]`: "the third side measures about $15\text{ cm}$" is right for a measurement; step 4 gives the exact 15 (17^2 - 8^2 = 225). No change needed, but the figure shows "15 cm" and the spec says so.
- Book numbers are fine (Q2, Q4 (i) in Figure it Out of section 2.4; Triples Q1-Q3 of section 2.5; Chapter Exercises Q2 (a), Q4, Q5, Q6). `M3.S10.T10.C64` to `C75` have no `book_number` (they are in-text worked examples), as expected.
- Maths re-checked (all hold): 17^2 - 8^2 = 225 = 15^2; 5^2 + 7^2 = 74 with 8.6^2 = 73.96 and 8.7^2 = 75.69; 7^2 + 9^2 = 130 with 11.4^2 = 129.96 and 11.5^2 = 132.25; 15^2 + 36^2 = 39^2; the six triples up to 20; the scaled lists of C70; the five odd-square triples of C80 (7,24,25), (9,40,41), (11,60,61), (13,84,85), (15,112,113); the three examples of C84 and their gaps; the five rectangles of C88.
- No concept in this chunk has a "refer picture" answer; no concept image is linked anywhere.

### Class 8 Ch 9, chunk D
- **M4.S13.T13.C92 (Q8 (ii) worked block).** The question reads "Suppose the grid extends indefinitely. What are the possible integer-valued areas of squares you can create in this manner?" with no setup: "the grid" and "this manner" refer to Q8 (i), which sits later (T15) and is not repeated. Suggested sentence: "Using the dots of a grid as the vertices, suppose the grid extends indefinitely. What are the possible integer-valued areas of squares you can create?" (No figure decision was changed because of this.)
- **M4.S15.T15.C97 (Q8 (i) question_tex).** Part labels are written inconsistently: `$(a) 2\text{ sq. units}$, $(b)$: $3\text{ sq. units}$, $(c)$: $4\text{ sq. units}$, and $(d) 5\text{ sq. units}$`. Suggested: "can you create a square that has an area of (a) 2 sq. units, (b) 3 sq. units, (c) 4 sq. units, and (d) 5 sq. units?" with the same form for every part.
- **M4.S15.T15.C98 (Q8 (i) solution).** The steps give only p and q for each square, not where to put it on the dots. Suggested extra sentence: "The figure shows one such square for each of (a), (c) and (d), with its corners on the dots." The diagram now shows one concrete square per part.
- **M4.S16.T16.C101 (summary matching).** The question says "Match each summary statement to an example from the chapter" but the six statements and the six examples appear only inside the steps; the question text does not list them. Suggested: list the six summary points in the question and let the steps give the matches.
- **M4.S16.T16.C103 (Find the Colours), step 3.** "Say it is blue: that box is BLUE." mixes the label and the contents. Suggested: "Say the ball is blue: the box labelled RED holds blue balls."
- Checked and correct: all arithmetic of C89 E0, E1, E2 (216 + 512 = 728, 729 + 1000 = 1729, 12^3 = 1728, 13^3 = 2197, 1994 - 1963 = 31), C96 (144 + 1225 = 1369 = 37^2), C98 ((a) 1 + 1 = 2, (c) 4, (d) 1 + 4 = 5, 3 not a sum of two squares), C100 (36 - 9 = 27, 5.1^2 = 26.01, 5.2^2 = 27.04, 3 sqrt(27) = 9 sqrt(3) ≈ 15.59), C94 (9 = 2x + 1, x = 4) and the two cases of C103.

### Class 8 Ch 10, chunk A
- **M1.S2.T2.C6** question says "Using the map" but the LP has no picture; the new diagram supplies it. Suggested: "Use the map of South India shown above (RF = 1 : 60,00,000, marked 'Map not to scale') ..." and in step 2 "On the page" -> "On the printed map in the book".
- **M1.S3.T3.C12** "What is the total volume of this purple paint?" has no numbers and the step "4 + 6 + 10 = 20" is unexplained. Suggested: "In Example 1, Yasmin's purple paint has 4 litres of red, 6 litres of blue and 10 litres of white. What is the total volume of this purple paint?"
- **M1.S4.T4.C14 / C15** the question never says what the four terms of 8 : 4 : 2 : 1 are, yet the answer names coriander, toor dal and fenugreek. Suggested: "Viswanath's spice mix uses 8 spoons of coriander seeds, 4 red chillies, 2 spoons of toor dal and 1 spoon of fenugreek seeds (8 : 4 : 2 : 1). Puneet has only 2 red chillies. How much of the other ingredients should he use ...?"
- **book_number labels are duplicated or shifted.** M1.S5.T5.C16/C17 say "Figure it Out 3.4, Q1" but are book Q2 (library); M1.S5.T5.C18/C19 say Q2 but are book Q4; M2.S8.T8.C27/C28 say Q1 (book Q1, correct); C29/C30 say Q2 but are book Q3; C31/C32 say Q3 but are book Q5. So "Q1" appears on two different questions. Suggested labels: C16/C17 "Figure it Out 3.4, Q2", C18/C19 "Q4", C27/C28 "Q1", C29/C30 "Q3", C31/C32 "Q5". The `ncert_refs` (FiO2, FiO4, FiO1, FiO3, FiO5) are right. The concept names "Figure it out: Q1/Ans1" are duplicated across M1.S5.T5 and M2.S8.T8 too, and the five exercise questions are split across two topics in an order different from the book.
- **M2.S7.T7.C25** `question_tex`: "How many $ml$ of each make $50\text{ ml}$?" sets the first unit in math italics. Suggested: "How many $\text{ml}$ of each make $50\text{ ml}$?"
- **M1.S2.T2.C5** steps use "290 km" without saying which pair; the question says "the same two pairs of cities". Suggested: add "(for example Bengaluru to Chennai, about 290 km)".
- **M1.S5.T5.C19** step 1 says "construct it with a ruler and compass" but gives no construction steps; the new figure shows the finished triangles only.
- **M2.S6.T6.C20** carries the concept image C20.IMG1 (the 110-units split of Example 3) although its own example is "Divide 12 in the ratio 2 : 1"; Example 3 is C21. Not an error for this run, only a placement oddity.

### Class 8 Ch 10, chunk B
- **M2.S9.T9.C33** (teaching text): "pie charts like the one shown in the figure" but this concept's own image is the halving bars (C33.IMG1); the pie chart appears only on a later card (C35.IMG1). Suggested: "(the finished pie chart is on the card after this)" or move the sentence.
- **M2.S9.T9.C36** worked question "Construct the pie chart for the grades." gives no data. Suggested: "Construct the pie chart for grades A to E with 12, 10, 8, 6 and 4 students (angles 108°, 90°, 72°, 54°, 36°)."
- **M2.S11.T11.C44** question text does not say which part of a ring is the time asleep (the book does not either); only the solution says so. Suggested sentence: "In each ring the dark part shows the hours asleep in a 24-hour day."
- **Wrong or duplicate book numbers.** C44/C45 are labelled "Figure it Out 3.6, Q1" but are the book's second 3.6 set, Q4; C46/C47 "Q2" is book Q5; C57-C60 "Q1", "Q2" are the first 3.6 set (p.65) Q1, Q2; C61/C62 "Q3" is the second set's Q1 (taps). So "Figure it Out 3.6, Q1" appears for two different book questions (C44 and C57). Suggested: "Figure it Out 3.6 (second set), Q4 / Q5 / Q1" for C44, C46, C61 and "(first set)" for C57, C59.
- **M2.S10.T10.C43** is built on a sample class invented by the LP (counts 6, 4, 2, 6, 8, 8, 6 for a class of 40). Fine, but the question text says "your class"; the solution text already says "this model uses a sample class of 40", so no change needed, just noted.
- No contradictions between LP solutions and the book. All sums and products were recomputed: 360 - 90 - 120 = 150; 3.6 x 50/25/15/10 = 180/90/54/36; 54+36+18+54+72+72+54 = 360 and 6+4+2+6+8+8+6 = 40; 108+90+72+54+36 = 360; 360 - 90 - 120 - 60 - 60 = 30; 18 x 12 = 216; products 800, 800, 312.5, 128 and 450; 2 x 18 / 4 = 9; 80 x 15 / 100 = 12; 20 x 4 / 10 = 8; 5 x 4 = 20; 1.5 / 18 = 5 / 60 = 1/12; 3/5 hour = 36 minutes.

### Class 8 Ch 10, chunk C
(No LP text was changed and no decision was altered because of these.)

1. **Book numbers repeat across topics (C72 to C89).** The questions of topic M3.S18.T18 are labelled "Figure it Out 3.6, Q1" to "Q9", but the same labels are used again in M3.S15.T15 (Q1 to Q3: inverse tables, fill cells, which pairs) and in M2.S11.T11 (Q1, Q2: sleep charts, transport pie chart). The `ncert_refs` give the real position in the book's second Figure it Out 3.6 set (pdf pages 13 and 14): C72/C73 = book Q2 (FiOb2), C74/C75 = Q3 (FiOb3), C76/C77 = Q6 (FiOb6), C78/C79 = Q7 (FiOb7), C80/C81 = Q8 (FiOb8), C82/C83 = Q9 (FiOb9), C84/C85 = Q10 (FiOb10), C86/C87 = Q11 (FiOb11), C88/C89 = Q12 (FiOb12). Suggested labels: "Figure it Out 3.6 (second set), Q2" and so on, using those book numbers (or one running LP number per topic).
2. **M3.S19.T19.C90 block 0 (E0): the question does not list the statements.** It says "Match each summary statement to an example from the chapter." but the four statements are only implied by the steps. Suggested question: "Match each of the four summary statements (many-term ratios, dividing a whole, direct proportion, inverse proportion) to an example from the chapter."
3. **M3.S19.T19.C90, blocks 1 to 3 (E1 to E3) are authored examples** (item_kind "authored") with no ncert_refs, while block 0 carries summary.1 to summary.4. Nothing is wrong with the numbers; just note that E1 to E3 are not from the book.

Checked and correct: every number in C73, C75, C77, C79, C81, C83, C85, C87, C89 and in the four Summary blocks was recomputed (120 / 24 = 5 and 5 x 20 = 100; 20 x 6 = 120, 120 / 30 = 4; 3 x 4 = 12, 12 / 4 = 3; 6 / 2 = 3 and 3 x 5 = 15; 25 x 12 = 300, 300 / 20 = 15; 8 x 45 = 360, 360 / 9 = 40; 1/3 + 1/2 = 5/6, 1 / (5/6) = 6/5 = 1.2 hours = 1 hour 12 minutes; 42 x 63 = 2646, 2646 / 54 = 49; 60 x 2 = 120, 120 / 80 = 1.5; 60 / 3 = 20 and 20 x 7 = 140; 6 x 10 = 60, 60 / 4 = 15; summary examples 110 / 5.5 = 20, 4500 / 5 = 18000 / 20 = 900, 20 x 4 = 10 x 8 = 80).

### Class 8 Ch 12, chunk A
- **M1.S3.T3.C9 / C10 (Relatively Unchanged).** The question asks for the mean, the mean after adding 10 and the mean after doubling, but the solution also works "every value minus 1" and the answer says "6.18 after subtracting 1". Suggested question sentence: "...then the mean when every value is increased by 10, when every value is decreased by 1, and when every value is doubled." (The book's own "reduce every value by 1" plot is applied to the +10 data, mean 16.18; the LP applies it to the original data, 6.18. Both are correct.)
- **M1.S3.T3.C11 / C12.** Subscripts are missing in LaTeX: `$x1$, $x2$, … $xn$` should be `$x_1$, $x_2$, \ldots, $x_n$`, and in the question `mean is a` should be `mean is $a$`.
- **M1.S4.T4.C16 (Q3, shoes).** The answer says "option (d)" but the question text does not list the options (a) to (g) of the book. Suggested addition to the question: "(a) 174.2 cm (b) 126.2 cm (c) 150.2 cm (d) 149.2 cm (e) 151.2 cm (f) None of the above (g) Insufficient information".
- **M1.S4.T4.C17 (Q4, albums).** The question text gives no data for albums B and C (they are only in the picture), so it depends on the figure; the plan's video metadata also has `final_answer.spoken` = "album eigh" (should be "album A").
- **M1.S4.T4.C15 to C20 (the six Figure it Out singles): wrong `book_number`.** All six carry "Figure it Out, Q1"; the correct numbers are Q2, Q3, Q4 (chapter-end part 5.1) and Q1, Q5, Q7 (the second Figure it Out, "More on Mean and Median"). The concept names ("Mean and Median, Q2", "More on Mean and Median, Q1", ...) are right.
- **M1.S5.T5.C21 (worked example, median).** The question gives only "a data set has median 8", not the data. The book's data is 4, 7, 8, 12, 14 (median 8); including 11 gives 4, 7, 8, 11, 12, 14. Suggested sentence: "The data 4, 7, 8, 12, 14 has median 8. Include the value 11 and find the new median."
- **M1.S2.T2.C2 block 0.** The paragraph says "Calculate and mark the mean of each collection of data below" and "Mark the mean for the collections below", but none of the eight collections (book p.1 and p.2) is given in the LP text, so the sentence points at nothing. Suggested: either list the data (6, 7, 8 / 3, 6, 9 / 2, 4, 9 / 4, 11, 15 / 11, 13, 17, 19 / 5, 6, 15, 16 / 10, 10, 11, 17 / 3, 5, 10, 12) or drop the sentence.
- **M1.S2.T2.C2 (worked example).** The LP tries 13 and 11 as other centres; the book's picture uses 12.5 and 11. Both are mathematically right; the LP numbers are the ones the text uses.
- **Small LaTeX slips:** M1.S7.T7.C30 `$41s$` should read `$41$s` (or "the two $41$s"); M1.S3.T3.C13 question uses `(i):` with a colon.
- Arithmetic of every LP solution in this chunk was recomputed and is correct (349, 392, 43; 384, 381, 25.4; 61 / 5 = 12.2; 66 / 6 = 11; 79 / 11 = 7.18; 1275, 2500; 443 / 25 = 17.72; the grids; the median 41).

### Class 8 Ch 12, chunk B
- **M1.S8.T8.C31 to C39 (all nine):** `item.book_number` is "Figure it Out, Q1" for every block, but the questions are FiO1 Q6, Q7, Q8, Q9 and FiO3 Q2, Q3, Q4, Q6, Q8 (the LP's own `lp_text` and card titles say the right numbers). Suggested: "Figure it Out, Q6", "Q7", ..., "Q8".
- **M1.S8.T8.C38 (FiO3 Q6):** the question drops the book's answer options (a) to (d) of parts (i), (ii) and (iii), but the LP solution (i) says "The others claim too much", which points at options the learner cannot see. Suggested: add to part (i) "(a) The average height of the class will increase as there are 2 new values. (b) The average height will remain the same. (c) The heights of the new students have to be measured to find out the new average height. (d) The heights of everyone in the class have to be measured again."; for (ii) and (iii) add the book's four options "will remain the same / will increase / will decrease / the information is not sufficient".
- **M1.S8.T8.C35 (FiO3 Q2):** "Give two examples" for each condition, but (iv) gives one concrete list plus "All six values equal also works" (no numbers) and (v) gives only one list. The LP's video uses 5, 5, 5, 5, 5, 5 for (iv) and 1, 1, 1, 1, 1, 7 (median 1, mean 2) for (v). Suggested: "(iv) ... also 5, 5, 5, 5, 5, 5 (mean 5, median 5)" and "(v) ... also 1, 1, 1, 1, 1, 7 (median 1, mean 2)".
- **M1.S10.T10.C43 and C45 (family-size examples):** the table is given only as a run-on sentence ("size 3, 4, ... occurs 3, 11, ... times"). Suggested: write it as a LaTeX table (row Number 3 to 10, row Frequency 3, 11, 9, 7, 3, 1, 1, 1) after the question.
- **M1.S11.T11.C47 (FiO1 Q10 question):** the counts exist only in the figure and the text has no pointer such as "the dot plot below". Suggested: "The number of times students rode their cycles in a week is shown in the dot plot below." The question text also has stray colons after the part labels ("(i): Find ...", "$(a)$: Everyone ...").
- **M1.S11.T11.C48 (FiO1 Q10 solution):** step (iii)(b) justifies "Almost everyone used their cycle a few times" with "39 of 42 rode at least once", which does not match "a few times". The plot gives 38 of 42 who rode two or more times. Suggested: "(b) is valid: 38 of 42 rode two or more times." Step (iii)(c) says someone who rode 8 or 10 times "must have ridden twice on a day"; this needs "a week has 7 days". Suggested: "...in a week of 7 days must have ridden at least twice on some day."
- **M1.S13.T13.C51 and C52 (worked examples):** the questions do not say where the marks sit; the formulas =SUM(B3:G3) and =AVERAGE(B7:D7) need the addresses. Suggested for C51: "Nagesh's marks are in row 3, columns B to G of the spreadsheet." For C52: "Gowri's marks in Odia, Telugu and English are in row 7, columns B, C and D."
- **M1.S14.T14.C54 (spreadsheet cells question):** the text never mentions the spreadsheet picture, yet the marks, names and column / row labels are only in it. Suggested: "Look at the spreadsheet of Sudhakar's class marks shown below." The LP's `q_figure` writes the headings as Odia, Telugu, English, Social; the book prints Odia(R1), Telugu(R2), English(R3), Social.
- **M1.S12.T12.C49 (FiO1 Q11):** the data is written as comma lists; a LaTeX table would read better (suggested array in `text_alternative` of each item).
- Checked and correct: all arithmetic in C31 to C39, C43 to C46, C48, C49, C51, C52, C55 (totals 24, 83, 70, 2010, 68, 39, 188, 193, 473; means 5.22, 4.6, 7.6, 150.22; medians 5, 4, 8).

### Class 8 Ch 12, chunk C
(Not edited; suggestions only.)

1. **M2.S17.T17.C62** (single, book Q9). (a) The block text is empty ("read the question in the book"); the real question is in the Practice block M2.S15.T15.C59 and does not contain the table. Suggested: add the LaTeX table of the book (columns Andaman and Nicobar Islands, Assam, Gujarat, Mizoram, Uttar Pradesh, West Bengal; rows 2016 to 2025: 16, 6, 16.5, 20, 16.15, 9.47 / 12, 12, 14.75, 20, 16.97, 11.65 / 12, 12, 14.75, 22, 16.18, 11.63 / 12, 12, 14.75, 22, 18.24, 11.43 / 13.88, 12, 13, 20, 18.96, 11.11 / 18.22, 15, 14.45, 22, 20.63, 12.79 / 18.73, 14, 14.28, 25, 21.3, 16.14 / 20.63, 12.02, 14.54, 27.65, 25.39, 18.43 / 19.73, 13.72, 14.8, 29.03, 26.9, 21.66 / 20.99, 12.35, 19.2, 29.8, 24.81, 23.99). (b) Step (i) does not name the 3 states. Suggested: "(i) Choose Gujarat, Uttar Pradesh and West Bengal: years 2016 to 2025 along the bottom, prices from 0 to 30 rupees up the side in steps of 5, one line per state."
2. **Wrong book numbers on the six singles**: M2.S17.T17.C62, M2.S20.T20.C71, M2.S20.T20.C72, M2.S23.T23.C81, M2.S23.T23.C82, M3.S28.T28.C96 all carry `book_number` "Figure it Out, Q1"; the book numbers are Q9, Q10, Q11, Q14, Q15, Q13. Their block text says "read the question in the book" and the real question text sits in Practice blocks of other concepts (M2.S15.T15.C59, M2.S18.T18.C66, M2.S21.T21.C76, M3.S26.T26.C93).
3. **M2.S19.T19.C67**: the question says "the World line" but not which graph. Suggested: "Use the World line of the graph of objects launched into space (2012 to 2024) to find two consecutive years where the count at least doubled."
4. **M2.S19.T19.C69 / C70** (births). The solution gives no value. Step (i) says "one sharp fall in a particular stretch", which the graph does not show (the real pattern: a rise to about 2 million in August to October each year, a fall to about 1.5 million by February to April with a small zig-zag in March). Step (iii) tells to read the first and last labelled months (Jul 2017, Jan 2020) but the line runs from April 2017 to March 2020. Suggested answers: "(ii) about 1.75 million (1.8 million); (iii) April 2017 to March 2020, 36 months; (iv) January 2018 about 1.67 million, January 2019 about 1.75 million, January 2020 about 1.77 million, so each January is a little higher; (v) the 12 monthly values of 2019 add to about 21.4 million (about 1.8 million a month)."
5. **M2.S20.T20.C71** (lighting). Steps leave (i) and (ii) as "check against the lines". Suggested: "(i) Valid: in 1983 rural kerosene is about 84% and urban electricity about 64%, both a majority. (ii) Valid: kerosene falls from about 84% to about 0% in rural homes and from about 34% to about 0% in urban homes. (iii) Not valid: in 2000 about 90% of urban households used electricity; about 10% used kerosene. (iv) Not supported: the graph shows the main source of lighting, not power cuts."
6. **M2.S20.T20.C72** (hobbies). No concrete answers. Suggested: "(i) about 2.1 hours; (ii) about 14 years, option (d); (iii)(a) not correct: the urban reading at 15 (about 1.1 hours) is about half the reading at 10 (about 2.1 hours), and the rural readings (about 1.3 and 2.4) also halve; (b) cannot be concluded: the graph shows an average."
7. **M2.S22.T22.C79 / C80** (rainy days). The question text omits the table (rows Mangaluru, Port Blair, Rameswaram with values, and the New Delhi row blank): suggested LaTeX array with the book values and an empty New Delhi row. Step (ii) should say "round half up" (24.5, 15.5 and 2.5 are halves). Checked and correct: the sums 112.1, 125.8, 42.3 and "about 36" (36.4), the rainy seasons.
8. **M2.S23.T23.C81 / C82** (sunrise, moon). No readings. Suggested C81: "The lower line of each place is sunrise, the upper line sunset. (i) Kibithu: sunrise about 05:55 and sunset about 16:30, a day of about 10 hours 35 minutes. (ii) Srinagar in June: sunset about 19:45 and sunrise about 05:20, about 14 hours 25 minutes, longer than Kibithu (13 h 55 min), Ghuar Moti (13 h 35 min) or Kanyakumari (12 h 35 min)." Suggested C82: "(i) Amavasya about the 28th or 29th (moonrise about 06:10 to 07:00, moonset about 17:00 to 18:00); purnima about the 13th or 14th (moonrise about 17:25 to 18:25, moonset about 06:40 to 07:30). The times shift 30 to 65 minutes later each day" (the step says about 50 minutes).
9. **M2.S24.T24.C83**: "Bihar is close to 0": the infographic prints +3 (the last digit hides under the red line); fine, but if the exact value is wanted write "about +3".
10. Checked with no problem: C56 to C58 numbers, C63 (2250 + 280 + 120 = 2650; 2850 - 2650 = 200), C65 (13 x 4 = 52), C73 (3400 / 4 = 850), C84 (298 / 5 = 59.6), C85 (193), C87 (box 20 to box 33), C88, C91, C92.

### Class 8 Ch 13, chunk A
- **M1.S3.T3.C12 (Q3), C14 (Q4), C16 (Q5):** the question text says "follows the steps" / "running the trick forward" / "the date trick" but never lists the six steps; in the book they appear only inside the comic strip. A student working the question alone cannot know them. Suggested sentence to add to each: "The steps are: think of a date, multiply the month by 5, add 6, multiply by 4, add 9, multiply by 5, add the day."
- **M2.S5.T5.C25 question_tex:** "bottom rows $6$, $2$ and $3$, $4$, $3$ and $5$, $4$, $5$, $0$" runs the three rows together. Suggested: "Fill three pyramids with bottom rows (i) $6$, $2$ (ii) $3$, $4$, $3$ (iii) $5$, $4$, $5$, $0$." Same grouping problem in **M2.S5.T5.C35** ("4, 13, 8 and 7, 11, 3 and 10, 14, 25"): suggested "(i) $4$, $13$, $8$ (ii) $7$, $11$, $3$ (iii) $10$, $14$, $25$."
- **M2.S5.T5.C27:** "middle row 4 and a blank, and bottom row 1 and two blanks" does not say the blank is to the right of the 4 / 1. Suggested: "the middle row has $4$ on the left and a blank on the right, the bottom row has $1$ on the left and two blanks".
- **M2.S5.T5.C33 question_tex:** "bottom row a, $b$, $c$" has the first letter outside math mode (reads as the article "a"). Suggested: "bottom row $a$, $b$, $c$".
- **M2.S5.T5.C30 steps_tex[3]:** "so $c$ is $20$, a is $32$ and $b$ is $28$": "a" is outside math mode. Suggested: "$a$ is $32$".
- **M2.S5.T5.C32 (extra block, answer_tex):** "First: bottom 5, 14, 7, 2 and top 70. Second: bottom 3, 5, 5, 2 with rows 8, 10, 7 and 18, 17" labels the book's second and third pyramids "First" and "Second", while its own steps call them "Second pyramid" and "Third pyramid". Suggested: "Second pyramid: bottom $5$, $14$, $7$, $2$ and top $70$. Third pyramid: bottom $3$, $5$, $5$, $2$ with rows $8$, $10$, $7$ and $18$, $17$." The old plan also holds two solution cards for this concept (C32.IMG1, C32.IMG2); the new map gives one solution diagram, M2.S5.T5.C32.IMG1, so the builder must not reuse the old C32.IMG2.
- All other LP answers recomputed and agree with the mathematics (pyramid sums, 1390 - 165 = 1225, 1269 - 165 = 1104, 394 - 165 = 229, 296 - 165 = 131, 4 + 26 + 8 = 38, 7 + 22 + 3 = 32, 10 + 28 + 25 = 63, the Q4 values 9, 1 / 14, 2 / 5, 2). No solution contradicts the book.

### Class 8 Ch 13, chunk B
(Not edited and decisions unchanged, as instructed.)

- **M2.S6.T6.C37, C39, C41, C43, C45 and their answers:** the LP calls them "Figure it Out, Q1" to "Q5", the book numbers are Q2 to Q6. The book's Q1 sits in
  chunk A's C35 labelled "Number Pyramids, Q1", so the LP's "Q1" appears to be reused (C35 and C37 are different questions). Suggest relabelling C37 to C45 as "Figure it Out, Q2" to "Q6".
- **M2.S6.T6.C38 steps_tex step 1:** "Bottom row a, $b$, $c$, $d$." the first letter is outside the maths. Suggest "Bottom row $a$, $b$, $c$, $d$."
- **M2.S6.T6.C46 steps_tex and answer_tex:** "$(2n - 1)th$" puts th inside the maths while C44 uses \text{th}. Suggest "$(2n - 1)\text{th}$" (three places in C46 text, steps, answer).
- **M2.S8.T8.C51 (question):** the question never says which calendar page. Suggest adding "the August 2025 calendar page" (the check block 6, 7, 13, 14 only makes sense on that page).
  Also C52 steps_tex: "Write the block as a, $a + 1$ ..." and "a is $5$" have unwrapped letters; suggest "$a$".
- **M2.S8.T8.C53 (question):** says "three squares make 27 and two circles with a square make 19" but not that each row's last box is the sum of the shapes to its left.
  Suggest: "In a grid, the last box of each row is the sum of the shapes to its left. Row 1 is three squares and ends in 27; row 2 is two circles and a square and ends in 19. Find the square and the circle."
- **M2.S8.T8.C55 (question):** "the last row is blank under every column" and "make a blank" are unclear, and the rule for the bottom row (each box is the sum of the column above it; the corner is the total)
  appears only in the answer (C56 step 6). Suggest: "In each grid the last box of a row is the sum of the shapes to its left; in the last row of Grid 2 each box is the sum of the column above it, and the corner box is the total." and "make an empty box" for "make a blank".
- **M2.S8.T8.C48 (worked example):** "a calendar page" without a month; optional "for example the August 2025 page" so 10, 17, 24 are visibly valid dates.
- **M3.S13.T13.C72, C74, C76 (questions):** all say "Mukta's trick" or "the trick given above" but the LP question text never states the four steps (they are only in the book's comic and in the teaching content of M3.S12.T12.C68).
  Suggest adding: "Mukta's trick: choose a 2-digit number with different digits, reverse the digits, find the difference of the two numbers, divide it by 9."
- **M3.S13.T13.C74 question_tex and C73 steps:** "when a $> b$" and "with $b$ larger than a" have unwrapped letters; suggest "$a > b$" and "larger than $a$".
- C44 step 4 and C46 are mathematically right (place 1 + 2 x 28 = 57; place 2n - 1; n = 3 gives the 5th term 8, n = 4 gives the 7th term 21).
  All other numbers in this chunk were recomputed and match the LP (141, 124, 56; 36 and block 5, 6, 12, 13; sum 40; squares 9 and 5; 11 and 5; 4 and 7 with sums 18, 15, 15, 48; 160; 217; 477; 512 against 504; 27 / 9 = 3; 45 / 9 = 5).

### Class 8 Ch 13, chunk C
- **M3.S14.T14.C78** (question and solution): the card names and `book_number` say "Figure it Out, Q1" but the text is book Q2 (the sum of the number and its reverse). Chunk B's C76 already carries book Q1. The same shift applies to C80 (book Q3, labelled Q2) and C82 (book Q4, labelled Q3). The `ncert_refs` (FiOC.q2, q3, q4) are right. Suggested labels: "Figure it Out, Q2", "Q3", "Q4".
- **M3.S17.T17.C90, C92, C94, C96, C98, C100**: labelled "Figure it Out, Q1" to "Q6" but they are book Q6 to Q11 (`ncert_refs` FiOC.q6 to q11 are right). Suggested labels: "Figure it Out, Q6" to "Q11".
- **M3.S14.T14.C78** question: says "In the trick given above" without stating the trick. Missing data for a standalone card. Suggested sentence to add before the question: "Mukta's trick: choose a 2 digit number with different digits, reverse the digits, find the difference of the two numbers, then divide by 9."
- **M3.S16.T16.C88** `answer_tex`: the closing bracket sits inside the maths: "(or any multiple, like $14$ and $16)$". Suggested: "(or any multiple, like $14$ and $16$)".
- **M3.S17.T17.C94** `question_tex`: the pronoun is typeset as maths: "if $I$ gave you". Suggested plain "if I gave you".
- **M3.S17.T17.C96** `question_tex`: "$I$ run a small dosa cart" and "how many dosas should $I$ aim to sell" have the pronoun as maths; "(i):" and "(ii):" have a stray colon that the plain `question` field does not have. Suggested plain "I", and "(i)", "(ii)".
- **M3.S17.T17.C100/C101**: the LP question does not repeat that the genie asks 8 coins per round until the sentence "gives the genie 8 coins"; this is fine. In part (ii) of the solution, "fewer than 7" holds only for the start of 7 coins, while the question asks in general; the sentence already says "here". No change needed.
- All arithmetic in the LP solutions of this chunk was re-checked and holds: 111 = 3 x 37, 123 + 231 + 312 = 666 = 37 x 18 = 3 x 222; 254254 / 7 = 36322, / 11 = 3302, / 13 = 254; t = 6 (14 bicycles); x = 7 stickers; p = 15; x = 7, k = 8 flowers (7, 14, 6, 12, 4, 8); h = 20 horses, 35 hens; d = 6; g = 6, Naina 12; p = 80 and n = 175; 4/12 and 9/27 are one third; Karim 7 coins, 8x - 7c.

### Class 8 Ch 14, chunk A
- **M1.S3.T3.C11** `question_tex`, part (ii): `$A 29\text{ m}^2$ piece` puts the article "A" inside the maths. Suggested: "(ii): A $29\text{ m}^2$ piece and an $11\text{ m}^2$ piece ...".
- **M1.S3.T3.C11** (and C12 `question`): figure (i) is called "a plus shaped figure"; the book figure is four rectangles round one common corner (a pinwheel). Suggested: "four rectangles arranged round one common corner like a pinwheel".
- **M1.S3.T3.C11**, part (ii): the text does not say that the 11 m² piece sits beside the 29 m² piece or that the bold outline encloses the 29 m² piece and the piece below it only for the area 50 m². Suggested: "The bold outline encloses the 29 m² piece and the piece below it; together they have area 50 m². The 11 m² piece is beside the 29 m² piece."
- **M1.S4.T4.C13 to C17** and **M1.S7.T7.C26 to C28**: `item.book_number` is "Figure it Out, Q1" for every one; the concept names say Q2..Q6 (Rectangles and Squares) and Q3..Q5 (Triangles). Suggested: "Figure it Out (Rectangles and Squares), Q2" ... "Q6" and "Figure it Out (Triangles), Q3" ... "Q5". Also these blocks only say "Read the question in the book"; the actual question sits in the Practice blocks of M1.S2.T2.C6 (blocks 0-4) and M1.S5.T5.C21 (blocks 0-2).
- **M1.S2.T2.C5** (worked): "a thin zigzag made of 9 unit squares joined edge to edge in one line with bends" does not fix the shape. Suggested: "a staircase of 9 unit squares: the squares go right, up, right, up and so on, each sharing a full side with the next".
- **M1.S4.T4.C14** (lp_text question): "A plot has sides 14 m and 12 m with a crosspath." Suggested: "A rectangular plot 14 m by 12 m has two paths crossing it, one along each pair of sides, each running right across the plot from one side to the opposite side."
- **M1.S4.T4.C16** (lp_text question): "A square is divided into regions 1, 2 and 3" does not say how. Suggested: "A square is cut by one diagonal and by a line from a corner to the midpoint of that diagonal into regions 1, 2 and 3: regions 1 and 2 are the two small triangles on one side of the diagonal and region 3 is the half of the square on the other side."
- **M1.S4.T4.C17** steps 1 and 2: "two perpendicular lines through the square that are not parallel to its sides; the 4 pieces are congruent" is only true when the lines pass through the centre, and "the long edges run round the outside" disagrees with the video ("the two equal edges", length 4.27 for a side-8 square, which are not the longest edges). Suggested: step 1 "Draw two perpendicular lines through the centre of the square that are not parallel to its sides"; step 2 "Turn the pieces so that each right angle points outward and the two equal edges that met at the centre run round the outside".
- **M1.S6.T6.C23** step 1: "Drop the altitude XY to DC" while the book's Fig. 7.1 (and the question picture) already shows XY. Suggested: "The altitude XY (from X, perpendicular to DC) splits the rectangle into two rectangles."
- **M1.S7.T7.C28** step 3: "Cut off the two small top triangles and turn each into the gap below it" - the two top triangles exist only after the top triangle AMN is cut along its height. Suggested: "Cut off the top triangle AMN, cut it along its height from A into two right triangles, and turn each half round into the gap beside the slanted side of the lower part."
- **M1.S4.T4.C15** (lp_text): the lengths 20, 20, 20, 15, 15, 10, 10, 5, 5 are in order from the outer end inwards; suggested to say so: "listed from the outer end of the tube inwards".

No print slip was found in the book (no wrong digit, missing sign or count) in the pages of this chunk, so nothing was corrected under user rule 1; the specs use true values where the book drawing is only schematic (spiral tube width 1 instead of the printed 0.84; lower piece of FiO1 Q1 (ii) drawn at 84/29 = 2.897 m, the book draws about 2.67 m).

### Class 8 Ch 14, chunk B
- **All singles C38, C39, C40, C46, C47, C48, C49:** the block's `item.book_number` says "Figure it Out, Q1" for every one; the concept names say Q6, Q7, Q8, Q2, Q3, Q4, Q5. Suggested book numbers: "Figure it Out (Triangles), Q6", "... Q7", "... Q8", "Figure it Out (Area of any Polygon), Q2", "... Q3", "... Q4", "... Q5" (I used these in `lp_book_number`).
- **Same seven singles:** the block holds only the sentence "Work through the practice problem. Read the question in the book ..." and has no `question_tex` or `steps_tex`; the real question and steps sit in the Practice blocks of the teaching concepts M1.S8.T8.C33 (blocks 0 to 2) and M2.S11.T11.C43 (blocks 0 to 3). The builder must put the question token and the solution token where the question and steps really are (or the question and steps must be moved into the singles).
- **M2.S13.T13.C46 (and its Practice block):** the text does not say that E is on AB and F is on AD. Suggested sentence: "E is a point on AB and F is a point on AD."
- **M1.S9.T9.C36 / C37:** the text does not say that X lies on BC extended, to the left of B (the figure shows it outside BC). Suggested sentence: "X is the foot of the height from A, on the line BC extended beyond B."
- **M2.S15.T15.C53 / C54:** "all on equal bases between the same two grid lines" is not what the figure shows (row one lies between grid lines 1 and 4, row two between 7 and 10; each parallelogram spans two lines 3 squares apart). Suggested sentence: "all with the same base (5 squares) and the same height (3 squares)."
- **M2.S11.T11.C42:** the LP pentagon (6 by 4 rectangle plus a triangle of height 3) is not the book's pentagon (a plain unlabelled pentagon), and the apex position along the 6 cm side is not given (it does not change the area). Suggested sentence: "... with a triangle of height 3 cm on its 6 cm side, the apex above the middle of that side."
- **M2.S11.T11.C41:** the numbers BD = 10, 4 and 3 are the LP's own (the book figure carries none). Fine for a worked example; noted only because the book picture is unlabelled.
- **M2.S13.T13.C49 (solution):** the text speaks of "the four corners" and "each pair of diagonal triangles" without a concrete quadrilateral; the solution figure uses a sample one (hence `needs_lp_text_sync: true`). Suggested opening: "Take any quadrilateral. Mark the midpoints of its four sides and join them in order."
- **M2.S13.T13.C47 video anchor:** it says "the book's regular hexagon with its centre joined to the six corners", but the book has no figure for this question (p.13 Q3 is text only).

### Class 8 Ch 14, chunk C
1. **Wrong book numbers.** M2.S16.T16.C55 ... C62 all say "Figure it Out, Q1"; the book numbers are Q2 to Q9 of the parallelogram set (pdf p.16-17). M2.S19.T19.C68 says "Figure it Out, Q1"; it is Q2 of the set after the trapezium section (pdf p.22). Suggested: "Figure it Out (parallelograms), Q2" ... "Q9"; "Figure it Out (rhombus and trapezium), Q2".
2. **M2.S16.T16.C60** (Q7): the question names triangles ADB and ADC but never defines A, B, C, D (the book's figure does). Suggested sentence: "In isosceles triangle ABC, AD is the altitude from A to the base BC (D lies on BC)."
3. **M2.S16.T16.C59** (Q6): step 2 "Drop perpendiculars from these midpoints to the base" and step 3 "Cut off the two small top pieces" do not match the method in the video, the answer and step 4. The video cuts the top triangle by the perpendicular from the apex to the line joining the midpoints and turns its two halves about the midpoints. Suggested step 2: "Drop the perpendicular from the top vertex to the line joining the midpoints; this cuts the small top triangle into two right triangles." (Perpendiculars from the midpoints to the base belong to another method, which gives a rectangle of half the base and the full height.) The diagram follows the video and the answer.
4. **M2.S16.T16.C61** (Q8): the steps speak of "length" and "width"; the diagram prints l, w and 2l (as in the video). Suggested: "Cut the rectangle (length l, width w) along a diagonal ..." and "base 2l, height w".
5. **M2.S20.T20.C71**: "Use Approach 2" is the book's label and the steps use G, ABGD and BGC without saying where G is. Suggested sentence: "Draw BG parallel to AD, meeting DC at G; the trapezium is the parallelogram ABGD plus the triangle BGC."
6. **M2.S21.T21.C74** (question concept): (a) the book's grid figure holds a third trapezium, the isosceles SPQR (ST = 2, TU = 6, UR = 2 squares, so PQ = 6, SR = 10, height 3), which the LP leaves out. Suggested extra question text: "Trapezium SPQR on the grid has PQ = 6 units, SR = 10 units and height 3 units, with ST = 2 and UR = 2." and solution: "Rectangle PQUT: 6 x 3 = 18. Each end triangle: 1/2 x 2 x 3 = 3. Total 18 + 3 + 3 = 24, and 1/2 x 3 x (6 + 10) = 24." (b) the text does not say that M and N are the feet of the perpendiculars from W and X to ZY; suggested: "where M and N are the feet of the perpendiculars from W and X to ZY." (c) for ABCD the text does not mention M, which the printed figure shows and the solution uses.
7. **M2.S16.T16.C55**: the book figure (ii) also carries a diagonal that plays no part; harmless, but the text could say "(ii) base 5 cm, height 3 cm (the diagonal drawn is not needed)".
8. **M2.S20.T20.C72**: "Use two copies" does not say how; suggested: "Join the trapezium to a copy of itself turned by a half turn along a slanted side, to make a parallelogram."

No solution contradicts the book's figures; all LP arithmetic was rechecked (28, 15, 24, 8.8; QN = 72 / 7.6 = 9.47; 150; 48; 30; 40; 54; 20 and 28; 136, 420, 100, 120).

### Class 8 Ch 14, chunk D
- **C78, C79, C80, C81, C82:** `book_number` says "Figure it Out, Q1" for all five; they are Q4, Q5, Q6, Q7, Q8 of the trapezium Figure it Out (the LP's own ncert_refs say FiO5.q4 to q8). **C93, C94, C95, C96:** `book_number` says "Areas in Real Life, Q1" for all four; they are in-text questions 2 to 5. The pair C91/C92 (the quotient 161.29 ÷ 6.4516) also carries "Areas in Real Life, Q1". Metadata only.
- **C78 (Q4):** the LP steps use a, b and h without defining them. Suggested sentence at the start of the steps: "Let the parallel sides be a (top) and b (bottom) and the height h."
- **C79 (Q5):** the question text does not say that I and J are the midpoints of AD and BC; the book shows this only by dots and tick marks in the figure. Suggested sentence: "In the figure, I and J are the midpoints of the slanting sides AD and BC, and EFGH is a rectangle."
- **C81 (Q7):** the question says "as shown" but the LP text carries no figure; the new question diagram supplies it (no text change needed once the token is placed).
- **C87 (A4 sheet):** the question does not state the sidelengths that the solution uses. Suggested sentence: "An A4 sheet has sidelengths 21 cm and 29.7 cm." Also "3 rows of 4 sheets" is the LP's own concrete choice; the book leaves the table to the learner.
- **C89 (conversions):** the question does not give "1 in = 2.54 cm", which every step uses. Suggested sentence: "(1 in = 2.54 cm)". The LP also keeps only 5 in and 11.43 cm of the book's four lengths (5 in, 7.4 in, 5.08 cm, 11.43 cm).
- **C94 (times bigger):** the question speaks of "your village/town/city" and "your school" but the solution computes with an example (school ground 100 m by 80 m, town 10 km²) that the question does not state. Suggested sentence: "For example, take a school ground of 100 m by 80 m and a town of 10 km²."
- **C85 (worked example):** "1000000" and "20833" are written without separators while the book prints "43,560"; minor style point.


## Borderline calls kept as the agents made them

### Class 5 Ch 1, chunk A
- Sequences with blanks (C8/C9, C27 to C32, 8 items): none by the explicit "sequences stay text/LaTeX" rule, although the book draws boxes. If you want them drawn, the figure would be an `arrow_map` chain (boxes with the given values, blanks, jump arcs in the solution).
- Token tables: question required, solution none. If you prefer the whole table as the figure (question with the given cells, solution with the filled cells in green), C14 and C16 would become required; I kept tokens only because the digit and name cells are a plain table.
- C34 required (number line with the four numbers placed, shown before the steps); the alternative is none with the steps in text.
- Place-value digit charts in worked examples (C6, C10, C11, C19, C20, C33): none (HEADER_BOXES_ONLY), although each has a coloured teaching image in the plan (never linked).
- C35 none (open answer); a number line with sample numbers would be the optional picture.

### Class 5 Ch 1, chunk B
1. C37 question: required, though the numbers are in the text and the line is "if required" (see above). Alternative reading: none with TEXT_SUFFICIENT.
2. C38 solution: required, though the answer is a text list. Alternative reading: none.
3. C42 / C44: none; optional number line possible.
4. C57: none; optional digit-swap arrows possible.
5. C48 / C50: none while C38 is required (explained by whether the question gives a line to place numbers on).
6. Worked examples C53, C54, C58, C59: none (teaching images already cover them; never linked).

### Class 5 Ch 1, chunk C
- **C76 / C78 / C80 solutions required**: the answer is words and numbers, but the jump arrows with the ring are exactly the added visual of Step E. Typical-pair table (Step E) would also allow "Q required, S none". I chose required because the arrows are what "jumps" means in the book and the LP solution is built on them.
- **C71 / C72 / C73 worked examples none**: the same rabbit scene is a required figure in T19 / T20, but there the book gives it as the question; here the LP wrote the examples in words and each concept already has its teaching image. Could be flipped if the content team wants a figure on every rabbit example.
- **C81 / C82 table none**: the "filled table" wording of ANSWER_IS_FIGURE versus the plain-table rule.
- **C84 optional, C94 optional, C86 / C88 none**: the picture would help a little in each, none is needed.
- **Rabbit and carrot icons** in a diagram image (the "no clip-art" rule): kept as plain flat icons because they are the objects of the question; the must_not_show list says so.

### Class 5 Ch 1, chunk D
- **C125 worked example, required (SPATIAL_GEOMETRY, HIGHLIGHT_MEANING).** The text gives every number, so a text-only reading is possible. I kept it required because the lesson (a corner child stands on two sides, so the side counts add to 16, not 12) is about where 12 children stand around a square; the learner has to see the ring and its corners. The figure shows only what the question gives (no 4, 12 or 16, no brackets). If you want it dropped, set it to `none` with TEXT_SUFFICIENT; nothing else depends on it.
- **C114 solution, required (ANSWER_IS_FIGURE, DATA_IN_FIGURE).** The LP answer is a list of seven trips in words. I treated it as an arrangement answer (B2): who is on which bank after each trip, and that the boatman is never away from a lion-and-sheep or sheep-and-grass pair, is what the picture shows. Sibling check against the pebble game (C116, optional): there the states are two numbers already written as numbers, here they are who stands where.
- **C124 solution, required (printed answer is a picture).** The LP steps carry every number, but the book prints the answer to Example 1 as the four-column chain (P12-subtraction_chain-3), so B2 makes it required. Per decision 4 not flipped to none.
- **C111 worked example (same chain for 2 and 5), none (LATEX_ARITHMETIC, REUSES_CONCEPT_IMAGE).** The book prints no picture for 2 and 5, and the same chain is already the kept teaching image of that concept, so it was not drawn. If sibling consistency with C124 is wanted, C111 could be made required with the same layout (digits 2, 5: 52-25=27, 72-27=45, 54-45=9).
- **C109, C110 worked examples, none.** Reasoning about pairs / moves on piles, all in the words; C110's game-state flow is already the kept teaching image.
- **C113 question and C115 question, none (DECORATIVE_ONLY) although the book has a picture.** The river scene and the two stacks of pebbles only illustrate numbers and rules the question states in words. The river scene is the same as teaching image C109.IMG1 (accounting only, never linked).
- **C119 question and C120 solution, none (LATEX_TABLE) although C120's answer is a filled table.** Plain numbers, headings, no colour meaning: LaTeX array (brief: plain tables stay LaTeX). The earlier hint that the book table has four empty rows is wrong: the book prints four filled rows only.
- **C117 question, optional.** The book says "each step above" (the 3-and-7 chain); the LP text already lists 36, 27, 45 and 9, so the question can be attempted without the picture. The chain is drawn once, as C124's solution figure.
- **C129 and C131 questions, required (ACTION_ON_FIGURE).** The empty stable is what the book gives for arranging horses; the 12-stall structure (4+4+2+2, corners shared) is not stated in the text. The book prints two identical frames on page 16; each question gets one, with the same spec (C131 says "same as C129").
- **C123 question, none.** The book's picture P12-steps-2 is the three steps joined to the example by arrows; every word is in the LP question text.
- **C103 to C108, C118, C121, C122:** open or arithmetic-only, none.

### Class 5 Ch 2, chunk A
- **All 8 worked examples are `optional` (not added):** C3 (roti), C9 (3x7 grid), C10 (6x4 grid, 1/24), C16 (circle in 1/4 and 1/8), C17 (circle 1/2 + 1/4 + 1/8 + 1/8, 1/16), C18 (strip of 20), C36 (bar 4/5 to 8/10), C37 (bars 3/8, 6/16, 9/24). Each is told fully in words (no figure referenced, answer a number or sentence), so by the tie-breaker the picture is not needed, but every one would clearly benefit from a bar, grid or circle; the reason line names the figure. This was NOT decided because a teaching image exists: all eight concepts do keep a teaching image of the same figure (kept_image_ids), and that played no part. If you want them drawn, flip these eight to `required` (`add_new_image`, question_tex / after_question_text) and ask for the specs.
- **C8 solution `optional`:** the answer is a rule; two equal bars of 6 blocks (3 shaded = 1/2, 2 shaded = 1/3) would help but every number is in the words.
- **C23 solution `optional`:** answer is a count (5 pieces); a circle cut into 5 pieces marked 1/5 would help but is not needed. (C35 is `required` because its answer is an arrangement of pieces; C23's is a number.)
- **C30 and C32 questions `required`:** the learner shades on blank 4x2 and 4x3 grids ("shade and check"); the grid size appears only in the picture. Sibling of Q2 A (C28), which is clearly required. Could be argued as optional because the fractions alone give the answer.
- **C21 and C29 solutions `required`:** they add only labels and outlines (groups, 1/6, 1/3) to the given figure; kept required as "act on the given figure" (Step E, Q required and S required).
- **C35 solution `required`:** B2 "answer is an arrangement" read for "Make a whole using ... pieces"; the LP answer writes the pieces as sums only.
- **C25 and C27 solutions `none`:** the answers are equation chains of equivalent fractions (LaTeX), no picture printed or asked for.

### Class 5 Ch 2, chunk B
- Worked examples C49, C55, C61, C62, C63: `optional` (see 1.1). These are the calls most likely to be reversed by the user.
- C52 and C58 solutions: `required` although the LP text carries every number (kept as required on purpose, per the 23 Nov decision 4, because the book's printed answer is a picture).
- C51 and C57 questions: `none` although the book prints a picture beside the question (the picture goes with the printed answer, the LP question text does not refer to it).
- C54 and C60 solutions: `none`. The six parts compare plain fractions; the book prints no figure, and six pictures would only restate the numbers. (Sibling check: the other "compare with < >" items of the chunk are all `none`.)
- C46 solution (ticks on (b) and (c)): `none`, a selection written in the answer line, not a drawing.
- C39 question: boxes drawn empty (1.3); Sameer's row not drawn (1.4).

### Class 5 Ch 2, chunk C
- **C88 (Let Us Do Q2, solution) `optional`.** The question's box of 14 loose fractions is `NUMBER_LIST_IN_BOXES` (question `none`, text already lists them). On the solution side the only picture is the same box with 9/4, 9/4, 5/4, 7/3, 13/11, 12/5, 12/8 circled; the LP answer names the seven fractions, so under the v3 rule ("arrows/circles only optional when the text gives the answer") it is not drawn. If the user prefers the circled box, flip to `required` with the 14 fractions at the page positions (box 739 x 204 px, positions read from page 12) and the seven circled in FOCUS. Chunk D's "circle the fractions" questions (Let Us Do Q1/Q2 on page 14) are the same type: they should get the same decision.
- **C91, C92, C93 (worked examples of T23) `optional`.** Questions and steps carry every number and compare top and bottom numbers in words; the teaching images (number line 0, 1, 2 with 3/5 and 10/9; circles with the half line; number line 0, 1/2, 1 with 5/12 and 7/10) exist and are not linked. They are not dropped because the teaching image exists, but because no v3 trigger applies; a picture would show the answer and would not be given data. If the user wants a diagram for each worked example, the figure to draw is named in each item's `reason`.
- **C65 to C74 question side `none` although the book prints a picture beside the question text.** The picture in the book is the worked answer, not a given.
- **C86 as one dense card** (see above).

### Class 5 Ch 2, chunk D
- **C102 and C104 (circled boxes): optional vs required.** Argument for required: ACTION_ON_FIGURE / HIGHLIGHT_MEANING (the answer is the circles on a given box) and the LP's own `s_figure` wanted "the same box with the fractions circled". Argument for none/optional (chosen): the box is a NUMBER_LIST_IN_BOXES and the Step C text says circles only become optional on the solution side when the text already gives the answer; the LP answer lists all chosen fractions, so by the tie-breaker the text alone is exact. If the user prefers the picture, the spec would be: a rounded box with the 10 (or 12) fractions at the book's positions, the six (or five) answers circled in FOCUS. Chunk C's "circle the fractions greater than one" box (p.12) should get the same decision for consistency.
- **C95 and C97 (question side).** The paratha pictures could be read as a given figure of the question; I read them as the printed answer (they sit with the answer bubble) because the amounts are given as numbers. If read the other way, both questions become required and the two solution diagrams would derive from them.
- **C107 worked example (none) against C110 solution (required).** See judgement call 4.
- **C99/C100 (reference to 1).** A number line placing the twelve fractions around 1 would be optional only; text is exact, so none.

### Class 5 Ch 3, chunk A
- **C6 (solution, Statue) required.** The LP answer is complete in words, but the steps go child by child on "the second picture". The solution figure is the same two pictures with A half turn, B and C full turn, D neither (HIGHLIGHT_MEANING). Chosen for the same reason as C33 and C37 (labelled final state of a figure the question gave).
- **C33 (solution, house) required, derived from C32.** The answer is eight words, one per marked corner. Kept as a figure because the steps describe the corners on the picture and the sibling question C37 (gymnasts, same kind of answer) is required (sibling consistency).
- **C15 and C25 (worked examples) required; C3, C7 and C26 optional.** All five have a kept teaching image of the same scene. C15 points at "a practice picture" and names hinges P, Q, R; C25 names places X, Y, Z that exist only in the picture; both ask the learner to read an opening against a quarter turn. C3, C7 and C26 carry the whole situation in words and fractions (full turn / half turn; 1/2 + 2/4 = 1; 1/2 + 1/4 = 3/4), so a picture would only help. If the user wants C7 and C26 drawn too, the specs are easy to add (giant wheel with three arrows; swept 3/4 turn).
- **Reema's giant wheel (C9, C11, C13 questions none; C10, C12, C14 solutions optional).** The book's wheel is an illustration; the turns are in the words. The solution arrow pictures (two half turns, two quarter turns, four quarter turns) are the Step D example "arrow picture for a sum already written" -> optional, not added.
- **C20 (solution, tick table) none / LATEX_TABLE.** The ANSWER_IS_FIGURE trigger lists "filled table", but this one is a plain 5 x 3 tick table with no colour or drawing; a LaTeX array shows it exactly. Question C19 got the same decision. If the user prefers an image, the table is 5 object rows against 3 columns with one tick each.
- **C31 (solution) required** with chosen angles. The LP gives no numbers (two small turns, turns that add to a quarter, two bigger turns each almost a quarter): the figure uses 30 + 30, 45 + 45 and 70 + 70 degrees, never written in the picture. `needs_lp_text_sync` is left false because the text only talks about acute / right / obtuse.
- **C29 (solution)** shows acute 50, right 90, obtuse 130 degrees (LP steps), while the book's own three fans under the activity are acute, acute, obtuse. The LP is followed.
- **C5 (question, Statue) required** although the same scene is the kept teaching image of topic T1 (decision 5). The 'refer picture' exception does not apply: this pdf has no printed answers.
- **C28, C30, C34 questions none (OPEN_ENDED).** They give no figure (hands-on or draw-your-own); the book's pictures under C28 (fans) and C30 (1/4, 1/2, 3/4 circles, which are not acute turns) are teaching/sample figures.
- **Schematic redraws.** The house of books is redrawn as flat polygons (boy and girl left out, books as plain boards); the gymnasts as stick figures with the leg angle equal to the angle diagram on the right; the Statue children as top-down glyphs with a nose triangle (facing direction exact, no faces). All angles were computed in code and checked: house A 120.0, B 90, C 43.98, D 51.6, E 51.6, F 90, G 90, H 111.99 degrees (obtuse, right, acute, acute, acute, right, right, obtuse = the LP answer); pentagon 90, 90, 153.43, 153.43, 53.13 (sum 540); gymnast rows 60, 90, 120, 150, 180.

### Class 5 Ch 3, chunk B
- Worked examples C38, C39, C55, C69 are `optional`. In this chapter a turn is an angle, so v3's SPATIAL_GEOMETRY trigger could be read to make them required; I judged them text-sufficient (all data in the words, numeric answers, tie-breaker: a careful student solves them from the text). The picture that would help is named in each `reason`. C63 is firm (answer is a drawing). If the user wants all five worked examples drawn, C38 / C39 / C55 / C69 only need their decision flipped (specs are easy: disc with straw at 5 and 7 parts; three rows of 1/12 pieces; right angle covered by a 1/6 and a 1/12 piece; clock hand 2 to 7).
- T11 Q2 and Q3 solutions `optional` (a right angle / a straight angle is a name given by 2/8 = 1/4 and 4/8 = 1/2), while Q1 / Q4 / Q5 solutions are required (their answers are straw positions). Same for T11 Q6 solution.
- T14 Q2 and Q3 solutions `optional` while Q1 solution is required: Q1's answer fills the figure's own answer boxes (a filled figure); Q2's and Q3's answers are written in the question text lines.
- T11 Q1, Q4, Q5 questions are `required` although the disc is the book's set-up figure rather than a figure printed inside the question; the questions say "the straw" and cannot be attempted without that disc.
- T11 Q2, Q3, Q6 questions are `none`: showing a turned straw would give the answer away, and showing only the blank disc adds nothing.
- T16 Q5 question `none`, solution `required` (typical "word question, figure answer" pair).

### Class 5 Ch 3, chunk C
- **C73 and C74 worked examples: optional.** The turn is a spatial idea (SPATIAL_GEOMETRY) and a figure (arrow down then left; compass with Padma facing West) would make it easier. But the book gives no figure, the LP question states both positions in words, and the steps give the clock numbers or the order West, South, East, North, so a careful student can solve it from the text. I applied the tie-breaker as written ("only makes it nicer" is optional). If the user wants a figure on every worked example of a teaching concept, flip these two to required: the specs would be an arrow before and after the quarter turn (C73) and a compass with Padma facing West (C74), no turning arrow.
- **C80 compass: required.** If the user thinks the clockwise order North, East, South, West is common knowledge, this is the item to drop (the LP solution states the order in its first step).
- **C84 question: required.** The answer (a half turn the other way) does not depend on the street at all, but the question points to "the same place" from the previous question and the book prints it under the picture. If dropped, C85's solution would stay required (draws the whole figure itself, derived_from null).
- **C79 tap, lid, nut solution: none.** The picture that would help is a tap, lid and nut with a curved arrow; not drawn because of the viewing-side problem above.

### Class 5 Ch 4, chunk A
- **Making Sums Equal question side (units M1.S3.T3.C5, C7, C9, C11), required.** All numbers and sums are also in the LP question text, so a reviewer could call these none (TEXT_SUFFICIENT). I kept them required because the book gives the puzzle as a figure that the learner acts on and the solution figure is derived from it. If the team prefers text-only questions, set the four question items to none and make the four solution diagrams stand alone (`derived_from` null).
- **Place-value tables (units M1.S5.T5 solution C16, M1.S6.T6 C17 and C18, M1.S11.T11 solution C30, M1.S12.T12 C31 and C32), none.** The book prints regroup marks (circled carries, struck digits) which a reviewer could read as HIGHLIGHT_MEANING or "printed answer is a picture". I followed the explicit v3 rules (column addition and subtraction are LaTeX, header boxes with digits are not a diagram). These items are the first to become required if the team decides otherwise.
- **Minibus question (M1.S11.T11.C29), none.** The book's two boxes joined by a curved arrow with a question mark would be an optional model of "fuel filled = jump from 18 to 65"; the text carries both readings.
- **Worked example M1.S2.T2.C3, none.** A picture of two groups of cards with a swap would suit it, but all the numbers are in the text and the teaching image already shows it.

### Class 5 Ch 4, chunk B
1. **T15 worked example C43 and T16 solution C46: optional, not added.** An arc picture (ends paired inward, each pair marked with its total) would help, but the sums are already written as expressions in the steps (v3 Step D: an arrow picture for a sum written as an expression). C43 already has the kept teaching image C43.IMG1 showing the same idea for 41 to 45; I did not use that as the reason. If the user wants these drawn, the specs are in the reasons: run 41-45 with arcs 41-45 = 86, 42-44 = 86, 43 alone; run 52-55 with arcs 52-55 = 107, 53-54 = 107; and the four runs of C45.
2. **T16 question C45 none.** "Notice how the sums of 3, 4 and 5 consecutive numbers are related to the numbers being added" points back at the book's arc-pattern figure (P05-pattern-1, which is the teaching figure of the previous topic), but all four runs to add are in the text and the book has no printed answer that merely points at a picture, so the 'refer picture' rule does not apply. A careful student can solve it from the text.
3. **Place-value chart solutions (C50, C52, C54, C56) and T17 worked example (C47) none.** Could be argued as HIGHLIGHT_MEANING (circled regroup marks, struck digits). I followed the explicit v3 lines (LATEX_ARITHMETIC, HEADER_BOXES_ONLY). Sibling consistency: all four examples and the worked example get the same decision.
4. **T14 C38, C40 none** (parity tags / difference arrows only annotate the given boxes, see above).
5. **C59 required with a schematic route** instead of NOT_RENDERABLE (see above).
6. **C49, C53 none** while a part-whole line (total, part, remaining part) would be a nice optional picture; not needed to solve.

### Class 5 Ch 4, chunk C
- M2.S23.T23.C71 (Mary, question): the book gives a route sketch (Delhi top left, Varanasi, Kolkata bottom right, with 1,275 / 2,645 / 3,275). I chose none (TEXT_SUFFICIENT): every amount and the order of the trip are in the question text, no v3 trigger applies (no "in the figure", data not only in the picture). If the user wants the book figure, it would be a route line Kolkata -> Varanasi -> Delhi with the three spending amounts; ask and I will write the spec.
- M2.S23.T23.C72 (Mary, solution): none (LATEX_ARITHMETIC). A running-balance route (12,540 -> 9,265 -> 14,165 -> 11,520 -> 10,245) would be optional at best and only repeats the LaTeX lines.
- M3.S25.T25.C83 (worked example, Quick Sums and Differences with Round Numbers): none. The example is practice values (46 + ___, 358 + ___, 52 - 9, 215 - 99) with no figure in the book; two kept teaching images already show the method and are not linked (not the reason: no v3 trigger applies). It has the same kind of answer as C86, but the example has only one image slot and four parts, so one picture would be overcrowded.
- M3.S28.T28.C97 (worked example, palindromes): none. Reading 2,442 from both ends and listing 303, 313, 323, 333 is plain text.
- M3.S27.T27.C90 (877 + ___ ...): the digit-by-digit "make nine" pairing could be drawn, but the book gives no figure here and the answer is numbers only (see judgement call 4).
- M3.S27.T27.C94 (subtract 9 or 99): a number-line hop would help but is optional at most; the LP carries every step.

### Class 5 Ch 4, chunk D
- C119 (circle the even numbers): question none (a plain list of 12 lettered numbers, no figure in the book), solution optional (a picture of the 12 numbers with 498, 724, 100, 846 and 222 ringed would help, but the LP answer lists them). Not added.
- C125 (worked, join 14+8, 9+13, 7+10) and the solutions C128, C130, C132 (Q3 a, b, c: sums of even/odd numbers): optional. Reason: the book says only "you may use the paired arrangement"; a counter picture of one chosen pair would help the explanation, the answers are sums and a rule in text. The same decision for all four. Not added.
- C133 (coins worked example) and C135/C136 (Jincy's coins): none. The answers are coin sums in LaTeX and no coin figure is printed in the book. A coin-mat picture would be "nicer" only.
- Torch items C137, C139/C140, C141/C142: none (parity argument in words; the kept teaching image already shows presses 1 to 8).
- C143 (worked, reading tables): none; all the data is in the question text and the kept teaching images are not linked.
- C145 and C147 (the two tables): none with LATEX_TABLE (plain tables, no colour meaning; the blue header of P15 is decoration). BUT the LP question text does not contain either table, see LP text issues. I did not change the decision (decision 2); `needs_lp_text_sync` is true and `text_alternative` carries the array content.
- C146, C148: none (answers are subtractions in text/LaTeX).

### Class 5 Ch 5, chunk A
Borderline (v3 rules applied as written, user decision 4):

- **C18, C20, C22, C24 (Let Us Compare Q2 a-d, solutions): all four required.** (b), (c), (d) pick out statues of the picture (HIGHLIGHT_MEANING, ANSWER_IS_FIGURE: two statues circled with their gap, a stacked second copy for the doubling). (a) is the weakest: its answer is one number (89 m), and the typical "figure question, numeric answer" pair is Q required / S none. I kept it required because the solution adds a visible mark (highlighted pair + the 89 m gap) and the four parts are one NCERT question set with the same kind of solution figure (sibling consistency). If the user wants fewer images, C18 is the one to drop (`drop_image`, reason SAME_AS_QUESTION_DIAGRAM).
- **Statues drawn as plain columns, not as statues.** The book picture is six sculpture illustrations; the figure carries only names and heights, so each statue becomes a plain rectangle to the book's own scale (checked on the page picture: heights are proportional to the printed metres within 3 percent). Scale 3.9 px per metre; the 2 m gap between Liberty (93) and Motherland Calls (91) is only 8 px, so (b) draws a small bracket and the label beside it.
- **C33, C35 (Kilometre Race Q1, Q2, solutions): required** as ANSWER_IS_FIGURE: the question asks where objects are to be placed along a 3 km track, so the answer is a placement (numbered stations/children on a line from Start to Finish). This is a judgement: the positions are also fully written in the steps, so a stricter reading (tie-breaker: text alone is enough) would make them optional. The book prints no figure for the race, so the question sides are `none` (companion note: do not invent a question figure) and the solutions draw the whole track (`derived_from` null). The LP's `q_figure` hint ("a straight race track of 3 km") describes a picture that is not in the book.
- **C37 (Kilometre Race Q3, solution): none.** Sibling reason: its answer is a count (60 flags, 30 red and 30 blue) and the question does not ask for positions; a picture of 60 flags would be overcrowded and only repeat the arithmetic. Q1 and Q2 ask for positions.
- **C26 (worked example, flags on a 2 km track): required** (same kind of answer as C33/C35: placement of flags along a track). A kept teaching image C26.IMG1 already shows the same track; per user decision 5 it is not a reason to drop and it is not linked. The picture shows the complete final placement. The other five worked examples (C3, C4, C12, C13, C25) are `none`: their steps are pure arithmetic or word reasoning with no figure given (LATEX_ARITHMETIC / TEXT_SUFFICIENT); their teaching images stay.
- **C10 q / C11 s (match the 204 cm... lengths): q none (LATEX_TABLE), s optional.** The book gives a plain 2-column list and asks "find which measures represent the same sari": it does not say join. The answer is five written equalities. A figure with lines joining the two columns would help but is not needed. (The LP `s_figure` hint describes such lines.)
- **C6/C7 (Let Us Find table), C30/C31 (rope table): none** (LATEX_TABLE / TEXT_SUFFICIENT). The question text already lists every row; the filled rope table is plain numbers. If a LaTeX table is wanted, `text_alternative` says what to write.
- **C28/C29 (Measuring Long Distances Let Us Do): none** (OPEN_ENDED). The four tool pictures carry no numbers (added to the inventory as NEW-P03-tools-pictures, DECORATIVE_ONLY). A line "home - tea shop 120 m - school gate 400 m - temple 1,600 m" would help the sample answer but the values are practice values only.
- **C15/C16 (Let Us Compare Q1): none**, the book has no picture for the five rods.
- **C8/C9 (sari double number line): required both**, S derived_from Q. The ticks are drawn exactly to scale for 1, 2, 4, 5, 7 m (the book is only roughly proportional: 72, 146, 71, 145 px gaps measured on the page picture, i.e. 72 px per metre).

Figure inventory choices:
- Base figures claimed (all in my chunk): P01-table-1, P01-double_number_line-2, P02-table-1, P02-labelled_picture-2, P03-table-1. Later uses of a figure by another item are `NEW-<base id>-<suffix>` entries: NEW-P01-double_number_line-2-sol (solution C9), NEW-P02-labelled_picture-2-q2b/q2c/q2d (questions C19, C21, C23) and NEW-P02-labelled_picture-2-sol-q2a..q2d (solutions C18, C20, C22, C24). NEW-P03-tools-pictures is a figure missing from the base (none:DECORATIVE_ONLY).
- No figure is mapped to a concept image: user decision 5 says an item that needs a figure draws its own.
- I checked the `unclear` doubts of the inventory against the page pictures: the double-number-line tick spacing (proportional, see above) and the statue heights (proportional, see above). No base description needed a CORRECTED note.

Book mistakes (user decision 1): none found in this chunk's pictures or printed numbers.

### Class 5 Ch 5, chunk B
1. **T11 Q1-Q5 (C40, C42, C44, C46, C48): the station table is `required` on the question side, 5 identical diagrams.** The table is a plain 3-column table of numbers (a LATEX_TABLE candidate), but every question says "look at the stations ... shown in the table" and NONE of the distances is in the question text (only in the book table and the LP hint field `q_figure`). The tie-breaker (could a careful student solve it from the text alone?) is "no", so FIG_REFERENCED + DATA_IN_FIGURE apply. Per the run rules the same book picture gets one diagram per item (identical spec; Q2-Q5 say "same as M2.S11.T11.C40.IMG1"). If the content team would rather put a LaTeX array into `question_tex`, these five can simply be switched to `none` / LATEX_TABLE (the spec is a full cell grid of 8 rows x 3 columns).
2. **T11 solutions (C41, C43, C45, C47, C49): `none` (SAME_AS_QUESTION_DIAGRAM, TEXT_SUFFICIENT).** The LP steps already name the two distances taken from the table and do one subtraction, or read the last row (Q1). Highlighting the rows used would be only a nicety (optional at most), so not added. Sibling consistency: all five treated alike.
3. **T10.C38 worked example: `optional`.** All numbers are in words (Q 340 km, R 615 km); steps are one subtraction. A route line 0 / 340 / 615 km would help but is not needed to follow it. (A teaching image of this exact route already exists; that is not the reason for the decision.) Flip to required if the team wants a figure for every distance example: spec would be a route line with three marked stations and the 275 km gap in ANSWER green.
4. **T12.C51 worked example (ruler line 4 cm 6 mm, draw 72 mm): `optional`.** The reading is given in words ("6th small mark after the 4 cm mark"); 72 mm is a calculation. A ruler would help but nothing must be read from it. Flip to required if the team wants a ruler for every ruler example: one ruler 0 to 8 cm with a line ending on the 6th small mark after 4 cm (do not draw the 72 mm line, it is the answer of the second part).
5. **T12.C50 (pin 3 cm = 30 mm, bead 8 mm), T14.C61 (6 cm, 9 m, 8 km), T14.C62 (7,305 cm, 3 m 7 cm): `none`.** Pure conversions given in words, no figure referred to (LATEX_ARITHMETIC / TEXT_SUFFICIENT). The teaching images (cm over mm, three double number lines, split bar) stay as teaching images.
6. **T13.Q3 sprout table (C57 question, C58 solution): both `none` (LATEX_TABLE, OPEN_ENDED).** The question names Day 1-4 and mm in words; the book table is a plain two-column table with empty cells for the learner's own measurement. The LP solution's "sample answer" (3, 9, 16, 25 mm) is a filled plain table, which I treat as LaTeX rather than ANSWER_IS_FIGURE because it has no colour meaning and is an open answer. `text_alternative` holds the array. If the team reads "filled table = ANSWER_IS_FIGURE", C58 would become required with a 2 x 5 cell grid.
7. **T13.Q1 solution (C54) is `required`.** The LP steps count the 9 small marks "one by one"; the figure is the same ruler with the nine marks numbered 1 to 9 in ANSWER green and a FOCUS bracket under 1 cm to 2 cm. Counting on the figure is an action on the figure (Q required, S required, derived from Q).
8. **T13.Q4 (C59/C60): question `none`, solution `required`.** The question gives only five lengths in words (no figure given: no question diagram). The answer to "draw lines of these lengths using a scale" is the drawn lines (ANSWER_IS_FIGURE), so the solution draws one ruler 0-9 cm and five lines from 0 with GUIDE dashes to the scale. Letters (a)-(e) are drawn because the LP answer refers to the lines by letter (user decision 3).
9. **T13.Q2 solution values are written in mm only** ("48", "35", ... plus the legend "in mm"), not "4 cm 8 mm". The LP's own answer line is "Sample answer in mm: (1): 48; ..."; the cm-and-mm form stays in the LP steps. Reason: at the 34 px minimum text size "4 cm 8 mm" does not fit the small boxes and cannot fit the tiny box (6) at all. Tags "(1)" to "(8)" are drawn in both figures because the LP answer text refers to the lines by number.

Other choices:
- Ruler and design are drawn with CELL_FILL / white because the style tokens have no yellow; the book's ruler is yellow and its boxes are blue (boxes use FOCUS).
- Design geometry (C55/C56): I measured the 16 corners on the page 5 picture (page image 990 px = 211 mm, 4.69 px per mm at printed size) and fitted them so that every corner of an inner shape lies on a side of the shape around it AND the eight numbered lines come out at exactly the LP's lengths: 48.00, 35.00, 60.00, 27.00, 22.00, 19.00, 44.00, 61.00 mm. The raw measurement was 48.1, 35.0, 59.8, 27.0, 21.9, 19.3, 44.0, 60.7 mm, so the LP's sample answer agrees with the book picture. Box (4) is drawn 12.2 mm long instead of 14.5 mm because the book's box touches the diamond; box (6) keeps the book's small size (8.0 x 4.2 mm).
- Aspect ratio 16:9 for everything (the pipeline's card); the long ruler strips are therefore small relative to the card but still above the minimum text size.
- Inventory: P05-ruler-2 (1 cm = 10 mm teaching figure) is mapped to concept image M2.S12.T12.C50.IMG1 (accounting only). P05-ruler-1 and P05-shape-3 are mapped to their question diagrams; their solution uses are `NEW-P05-ruler-1-sol` and `NEW-P05-shape-3-sol`. Further uses of the station table are `NEW-P04-table-1-q2` to `-q5`. P06-table-1 is `none:LATEX_TABLE`; P06-relation_box-2 is a text-only box `none:TEXT_SUFFICIENT`. The sprout / screws / nail pictures on page 5 are decoration and are not in the base inventory.
- The 'Practice' concepts C39, C52, C63 are not units of this chunk and were not touched.

### Class 5 Ch 5, chunk C
- **Q1 (a), (b), (c) question side, required** although the LP text lists all numbers (user decision 4): kept because the book gives a figure and the learner acts on it.
- **C80 and C82 solutions (Saji and cable column pictures), none.** The reader could argue "printed answer is a picture" (Step B2) or `HIGHLIGHT_MEANING` (circled carries, struck digits). I followed the explicit NONE rules (column addition and subtraction = LaTeX; header boxes with digits = not an image). These are the first items to flip to required if the team wants the book's regroup pictures. If flipped, the picture would be a column layout with header boxes km | m (or cm / m | cm), the carry oval, struck digits and the red notes, and P08-column_addition-1/-2, P09-column_subtraction-1/-2 would map to those solution items.
- **C76 worked example (2 km 700 m + 1 km 800 m), none** by the same rule: a column addition. Its kept teaching image shows a column layout, but that is not the reason.
- **C95 worked example "Price of a Length: Double Number Line", none.** The question does not reference a figure and the arithmetic is in the steps; a double number line (3 m, 6 m, 9 m over Rs 90, 180, 270, arrow x3) would clearly help. This is the item most likely to be wanted as required. (The kept teaching image C95.IMG1 shows exactly that; not the reason for none.)
- **C77 worked example (ribbon cut), none.** A tape model would only repeat the steps.
- **C85 Bhopal, waterfall and Sanchi, none.** A route strip with three marked points would not change how the learner solves it.
- **C89 and C91 (Q4 "circle the bigger length"), none.** The circling is done on a plain list of pairs and the LP answer names the bigger length.

### Class 5 Ch 5, chunk D
- **C107 worked example (estimating with a door).** none (TEXT_SUFFICIENT): every number is in the text and no figure is referred to. A wall with two doors stacked would help, and the kept teaching image C107.IMG1 shows it. If you want the example illustrated, flip to required: a wall about 4 m high, a door about 2 m high beside it, two doors stacked reaching the top.
- **C110, C112, C114 (sample answers of Let Us Estimate).** none: practice-value numbers are in the text. A stack-of-references picture (5 floors of 3 m; 8 friends of 1 m 50 cm; a rope lowered into a well) would only make them nicer.
- **C119 question (child at a wall scale).** none: the picture is an illustration of the activity; the LP's `q_figure` hint was not followed because the question gives no data in a figure.
- **C120 solution.** none: three heights changed to inches and compared; a bar picture would be nicer, not needed.
- **C104 solution (Anita).** none: a strip of 500 cm cut into 10 pieces of 50 cm is possible, but it is division written in LaTeX.
- **C115 worked example (feet and inches).** none: arithmetic; the teaching image C115.IMG1 stays.
- **C121 worked example.** required but draws the given grid only, not the filled one (one picture per worked example, placed after the question).

### Class 5 Ch 6, chunk A
- C3 worked example (36 pouches): `required`. The question says "turn the picture of the groups of 4" and no picture is in the text. The diagram shows 9 rows of 4 and the turned 4 rows of 9 with a turn arrow. It duplicates the kept teaching image C3.IMG1 on purpose (user decision 5).
- C15 worked example (tray 7 rows of 12 turned): `required`, borderline. Every number is in the text; drawn because turning the tray is a spatial idea and it is the sibling of C3. Spec = 7x12 and 12x7 arrays with "Groups" / "Group size" brackets, no totals.
- C36 worked example (6 rows of 14 split into 10 and 4): `required`, borderline. The array cut into a block of 10 columns and a block of 4 columns is the whole point of the example. If you prefer, this one and C15 can go to `optional` without touching anything else.
- Worked examples C21 and C22 are `required` without doubt: the questions say "Show how the digits of 37 move on the place value board" and "The counting board shows 60 x 70".
- C17 question (packet arrays, book page 3): `required`, borderline. "Arranged in the following ways" points at the arrays and the pattern is seen in the turned arrays, but the LP text already lists every expression. Pairs (a) and (b) show the letters (the LP answer uses them); the two big arrays have no letter (the book prints none; its letters run a, b, e, f, g). (e), (f), (g) are text boxes in the book, no picture.
- C18 solution (same arrays): `required`, borderline. It adds the totals (6, 40, 78) and the 10 + 3 split of the big arrays that the LP steps use (6 x 10 + 6 x 3, 10 x 6 + 3 x 6). The answers for (e), (f), (g) stay text because the book has no picture for them.
- C11 question (Which number am I, number chart): `optional` (not added). The book prints a plain, unmarked 0 to 99 chart as a working aid; all eight clues are in the text, so the question can be attempted without it. If you want the chart on the question side, change it to `required` and give the solution `derived_from` = the question diagram (the chart without marks); the spec of the chart is already in C12.IMG1.
- C12 solution: `required`, standalone (`derived_from` null) because the question side has no diagram: 18, 27, 36, 45 shaded, 27, 36, 45 crossed out in WRONG, 18 circled in FOCUS. WRONG is used because the LP solution itself shows these numbers being ruled out.
- C31 solution (multiplying by 1,000): `required`, borderline. The LP solution explains the rule on "the place value board" (every digit moves three places left) and the board is not given in the question. The question (C30) is `none`: the book's 2 and 5 green 1,000 tokens only illustrate "2 thousand" and "5 thousand" and have none for 10 and 20. If you judge the board "only nicer", set C31 to `optional`.
- C14 solution (Make your own numbers): `none`. The sample answer is a list of equations and is open-ended; the question grid is the figure. I verified the LP claims by brute force: with two different numbers and one operation, 0 and 19 cannot be made; only 11, 16, 17 and 18 have one way; 0 = (100 / 25) - 4 and 25 - (10 - 4) = 19 are right.
- Units 13, 14, 16, 17 (place value tables, Problem / Th / H / T / O or TTh ... O): all eight items `none` (`LATEX_TABLE`, `HEADER_BOXES_ONLY`). Header boxes with or without digits are a LaTeX array by the v3 list; the book's six problem cards (underlined digits) and the red "notice the underlined numbers" margin note are arithmetic (`LATEX_ARITHMETIC`). Sibling consistency kept across the four question sets.
- Units 9 and 12: `none` / `none` (no printed picture, words and equations only).
- The same-number-two-items rule: the shape set, digit frame, pouches and arrays are each drawn twice (question and solution) with the same layout, solution `derived_from` the question.

### Class 5 Ch 6, chunk B
1. M2.S11.T11.C43 question (3 x 18), required. The question text states the cut and the result in words, so a strict tie-breaker could say none. Chosen required because "arranged in the following way" points at the book's picture and the task is to discuss why the two are the same; sibling of 22 x 5.
2. M2.S12.T12.C45 question (22 x 5), required. Again the text describes the whole arrangement. Chosen required for sibling consistency with a) and because the book's blank equation sits inside the figure. If the user prefers none here, C46 solution stays required but must be redrawn stand-alone (`derived_from` null) and the figure inventory entry P06-array_cut-2 moves to the solution.
3. C44 solution none vs C46 solution required (same NCERT set). Reason: in a) the book's picture already holds the result (6 x 9 = 54 is printed in it), so a solution figure would only repeat it (`SAME_AS_QUESTION_DIAGRAM`). In b) the picture holds a blank equation; the solution fills it (11 x 10 = 110) and marks 11 rows and 10 squares across. The addition is small (an equation and two brackets), so this is a close call; if the user wants strict symmetry, either both are required or C46 becomes none.
4. M2.S10.T10.C40 and M2.S13.T13.C53 worked examples, required under user decision 5 although a teaching image of the same concept shows the figure. C53's single diagram draws both parts (6 x 19 and 13 x 31) in two panels (61 x 18.5 units, about 30 px per square on a 1920 card). If it looks crowded when rendered, the alternative is the first part only.
5. M2.S9.T9.C39 solution, none. The old `s_figure` hint was an array of 5 rows of 18 split 10 and 8, which would show only way (3) of the five children's ways; the answer is a reasoned yes, not a drawing. Optional idea only.
6. M2.S12.T12.C47 question none and C48 solution optional. The four book frames (Half / Double arrows with empty boxes) are a fill-in form; the problems and blanks are in the question text. Per the `NUMBER_LIST_IN_BOXES` rule the filled arrow frames are at most optional because the LaTeX lines give every step. Not added.
7. M2.S15.T15.C62 solution, none. The steps talk about "strips" of squares, but this question has no picture and the answers are arithmetic; no diagram drawn (sibling of C50 which is also arithmetic).
8. M2.S10.T10.C41 and M2.S16.T16.C63 worked examples, none (halving/doubling chain and a mix of three strategies, all arithmetic).
9. M2.S14.T14.C55 / C57 questions: the picture has no text in the book either, so `visible_text` is empty; the equation sits in the question text and is not drawn. The solutions add the outline of the white / green column and the calculation lines of the LP steps ("4 x 20 = 80", "4 extra squares", "80 - 4 = 76"; "14 x 20 = 280", "14 left out", "280 + 14 = 294"), each of which uses the LP's own words and numbers.

Figure letters (decision 3): none of my pictures holds several lettered figures, so no letter is drawn anywhere (the LP answers do not refer to the pictures by letter).

### Class 5 Ch 6, chunk C
- **C77 and C78 (worked examples)**: area-model box and written-method lines could be called LATEX_TABLE / LATEX_ARITHMETIC (all numbers are in the LP steps). Kept required because (a) the box is a filled figure whose position carries the meaning (B2), (b) the book itself draws these as pictures and the plan already has teaching images for them, (c) decision 4 says not to flip a required item to none only because the LP text carries the numbers. If the user wants a stricter reading, these two and the box/line parts of Examples 4 and 5 are the calls to revisit.
- **C80 question (optional)**: the token picture is a real book figure; call kept optional because the question text carries both numbers and no action is done on the picture. If the user wants every book figure drawn, flip it to required: 12 rows, each 3 blue tags "10" and 5 pink tags "1", rows 1-10 in one dashed box and rows 11-12 in another (nothing else needs deciding).
- **C70 solution (Let Us Solve Q3)**: step 3 speaks of "the strip", which only a picture would show. Kept none (decision 2: do not change a decision because of an LP text issue; siblings Q5 and Q6 have the same nearest-multiple method with no picture). If the user prefers a picture here, the one needed is the nearest-multiple array (36 rows of 48 in a frame of 50, with a strip of 36 x 2 marked).
- **C82 question (none)**: could be argued optional (a picture of 150 kg of compost at 24 rupees a kg), but the book has none and nothing needs to be read in one.
- **Examples 4 and 5 solutions** put the box and both written methods in ONE card. If it looks crowded when rendered, the fallback is to keep the box and John's two lines (the fewest lines) and leave Kanti's four lines to the text; the LP steps name all three.

### Class 5 Ch 6, chunk D
- **C104 worked example** (none): a Th H T O layout of the partial products 20, 120, 800 would help but a LaTeX array carries it. Flipping to optional/required needs a short spec only.
- **C105 worked example** (required): the steps also state every carry in words; the figure is kept because the carry positions are the point of the example and a teaching image of the same example is kept (decision 5).
- **C114 (Let Us Solve Q1 like Nida, 5 problems)** (none): the book gives no table here, so there is no printed blank table to complete; the cells, column sums and totals are in the LP steps. Five filled Nida boxes (as for Let Us Do Q1) would help. Sibling difference to C88/C89 is the printed blank tables.
- **C91, C93, C116 (Kanti and John lines)** (none): lines like those of the teaching image C78 could be drawn; they are vertical arithmetic, so LaTeX.
- **C120 (Let Us Solve Q3 second part, nine products)** (none): no frame is printed for (a) to (i); nine more frames would repeat one layout. The first part of the same NCERT question (C118) is required because the book prints frames to complete.
- **C88 / C89**: the blank boxes could also be seen as a LaTeX table; kept required because the book gives them as a figure to complete (ACTION_ON_FIGURE).
- **C95** (none): a seat plan of 8 rows of 12 seats would help but needs an invented position for the first 48 people.

### Class 5 Ch 6, chunk E
- **C145 (worked example, digit puzzle "two black boxes x 6")**: `required`. The LP text describes the boxes in words, so a careful student could solve it from the text; I drew it because box colour (same colour = same digit) is the whole rule of the example and the same kind of frame is required for the book's Let Us Think questions. If the user prefers "text carries it", flip to `none` (`TEXT_SUFFICIENT`).
- **C134 (worked example, "Grow from a Known Product")**: `required` with its own figure (media id IMG2, IMG1 is the kept teaching image). The steps start "Picture 7 rows of 14 squares" and argue only from the added column, the removed row and the ten added rows. Panels A and B repeat the teaching image by design (decision 5); panel C (17 × 14) is not in the teaching image.
- **C143 (Let Us Do Q4, solution)**: `required` although the book's question figure already shows the blue strips; the solution adds only the two tags "add 17" and "add 23" (the answer to "17 or 23?"). A reviewer who thinks this only repeats the question figure can switch it to `none` (`SAME_AS_QUESTION_DIAGRAM`). The LP steps also take a column and a row away for (c) and (d); the book's pictures show only the added strips, so only those are tagged.
- **T30 Let Us Think solutions**: the answer to "find the possible values" is a list of digits, drawn as one sample filled frame per frame (the LP's check line). (d) has ten answers and (f) has two (2,222 and 3,332); the figure shows one sample each and says so in `render_note`.
- **C131 / C132 (Asher, T26 e)**: `none` on both sides; the table with carries could also be argued as `required` (HIGHLIGHT_MEANING). Chosen `none` because of the explicit `HEADER_BOXES_ONLY` rule and sibling consistency with (a) to (d).
- **C154**: `optional` (matching lines), not `required` (ANSWER_IS_FIGURE), because of the explicit `NUMBER_LIST_IN_BOXES` rule.
- **C155**: a growth chart would be an alternative to the table; kept as LaTeX table (`none`).

### Class 5 Ch 6, chunk F
1. **C168 question and C169 solution, the four pattern boxes (P21-pattern-1 to 4): none.** The book prints four dashed boxes of equations with blanks and red hint notes. Every equation is already in the LP question text, and a picture of the boxes would copy the question text (question side) or the answer line (solution side). Equations and sequences are LaTeX by the v3 rule (Step C, LATEX_ARITHMETIC), the same as a fill-in table. Against this: the red notes (5 x 5 = 25 with 2 x 1 = 2 beside 15 x 15, and the H T O digit sources beside 11 x 12 and 11 x 34) are part of what the book gives and sit only in the picture. If you want the book's boxes drawn, the question and the solution (filled blanks in ANSWER green) would both become `required` with `cell_grid` or `other` specs; the numbers are all in the LP text and this note.
2. **C160 solution (King's Reward Q2): none.** A day-by-day filled strip would look nice, but it is a plain table of numbers (LATEX_TABLE). If the user wants it as a picture it would be `required`, derived from no question diagram (the question has none).
3. **C179, C183, C185: optional (not added).** Each would be a sketch of a rows-and-columns block (or the ground seen from above). The text carries every number and the answers are numbers, so they are not needed; they are the three places where a picture would clearly help understanding.
4. **C170 question: required although the LP text carries the question.** The figure is needed because the numbers are not in the LP text at all.

### Class 5 Ch 7, chunk A
- M1.S2.T2.C4 (worked, shifted rows of a 9-slit mat): none. The LP writes every shifted row slot by slot, so a careful student can follow from text, but a picture of the four rows (kept teaching image shows it) would clearly help. Would be `optional` ("4 rows of 9 cells, Row 4 = Row 1").
- M2.S5.T5.C14 (worked, regular shapes): none. All side lengths are in the text. An optional picture: square 6 cm, rectangle 6 x 4 cm, pentagon 3 cm with sides ticked.
- M2.S8.T8.C29 (worked, border of 12 tiles): none. Optional picture: a row of 12 tiles square, triangle, ... with a dot at each join.
- M1.S2.T2.C3 (worked, describe a 10-slit row in words): none, no picture would be needed at all.
- M1.S3.T3.C8 (Q3 question): none although the book prints a picture next to it (it is the answer picture). If the user prefers to copy the book (question = finished mat, solution = SAME_AS_QUESTION_DIAGRAM), flip C8 to required and C9 to none.
- M1.S3.T3.C7 (Q2 solution) and M1.S3.T3.C11 (Q4 solution): required because they add marks (row labels, copy tags, the repeat box) to the question figure; if the user reads "marks only" as SAME_AS_QUESTION_DIAGRAM these two become none.
- M1.S4.T4.C12 / C13: the print slip and the too-short dot grid are corrected (see 3 and 4).
- M1.S3.T3.C9: draws 16 rows (LP) although the book mat has 17.
- Find Out Q1: the book prints the answer picture right under the question text ("Do you see ... as shown here?"). I treated it as the answer picture (solution), not as a given figure.

### Class 5 Ch 7, chunk B
- **C32 (Q1 solution, hexagon pattern): required, but the figure adds only a circle** at one meeting point (HIGHLIGHT_MEANING). Without it the solution would repeat the question figure (`optional` / SAME_AS_QUESTION_DIAGRAM). Kept `required` because step 4 of the solution talks about "every meeting point" and its order.
- **C58 (Try This Q2 question) required** because the cut line is shown only in the book picture; "cut in half" alone leaves the cut open. Could be `none` if the LP text names the cut line (see LP text issues).
- **C56 (Try This Q1 question) none** while the book prints a picture (see above).
- **C48, C52, C54 optional, C50 none**: a different call from the LP hints of chunk C's questions rq.four and rq.three (in_C.json gives them a "rhombus divided into four pieces" figure). They are the same kind of question; the merge should treat the rhombus-piece questions alike.
- **C43, C44, C62, C63 worked-example figures**: every number is in the LP text, so by the tie-breaker alone C44 (three triangles given by their sides) would be `none`; kept `required` by user decisions 4 and 5 and because the steps use the fold and the matching of angles.
- **Solutions C38, C51, C57, C59, C61 (tick marks and angle arcs on a triangle)**: marks only, no new shape; required because the solution text speaks about equal sides and equal angles and these marks carry that meaning.

### Class 5 Ch 7, chunk C
1. **C65, C73, C75 questions are `required` (rhombus with its 4 pieces).** The book prints no figure with Activities 4, 7 and 8 themselves, but
   the whole activity set works on the cut-out rhombus of p.96 ("Cut out the triangular pieces for the following activities", p.97), and without
   the pieces the question cannot be attempted (tie-breaker). The three questions get the same picture (identical spec, "same as C65.IMG1"). The
   solutions C66, C74, C76 name this diagram in `derived_from` but re-arrange the same pieces (same size) instead of repeating the rhombus layout.
   If the literal rule "no printed figure = no question diagram" is preferred, flip the three questions to `none` (TEXT_SUFFICIENT) and set
   `derived_from` of C66, C74, C76 to null; nothing else changes.
2. **C79 worked example (tangram pieces) is `required`.** The text names and counts the pieces, but "what is special about the angles" can only be
   seen on the pieces. The picture shows the finished sorting (5 triangles under "3 sides", square and parallelogram under "4 sides") with
   right-angle marks and equal-angle arcs. It overlaps in content with the concept image of the same concept; per the 23 Nov decision it is drawn
   anyway and the concept image is not linked. Alternative: `optional`.
3. **C84 solution is `none` (SAME_AS_QUESTION_DIAGRAM) although C82, C86, C88 are required.** (b) angles and (c) sides add marks (right angles and
   equal angles, ticks) that carry the meaning; (a) "same or different" adds no mark, all of it can be read from the question picture. If a picture is
   wanted: the five triangles in a row from small to large plus the square and parallelogram (earlier author's hint); that would not keep the
   question layout.
4. **C83, C85, C87 questions each get a full tangram picture** (identical to C81). The book prints one tangram picture beside Q1 and its parts
   (a), (b), (c); the LP split them into 4 questions, so each part gets its own diagram (prompt section 2). The base inventory marks the picture a
   "teaching figure"; it is treated as the figure the question gives because "Name them" and "same or different" cannot be answered without it.
5. **C94 solution is `optional`, C93 question `none`, C91 worked example `none`.** C93: the 7 statements and the 4 names are in the LP text, the
   book's outlines add nothing. C94: matching answer is a complete list in the text; the arrows of a matching table follow the
   NUMBER_LIST_IN_BOXES rule (optional when the text already gives the answer). A picture (4 shapes with the statement numbers under them) is
   described in the reason. C91: the properties are given in words and a picture of X, Y, Z, W would show their names (the answer).
6. **C95 and C96 worked examples are `required`; their pictures show the finished figure** (rectangle/square in two circles; the full 17-line
   design), because question, steps and answer sit in one block and the steps refer to the drawing. C95 could be argued `none` (a student can draw
   it on paper); C96 could be argued text-only (the walk is arithmetic). I kept both because the drawing is the answer (B2) and the positions of the
   points are only clear in a picture.
7. **C71 question (empty 43 by 12 grid) is `required`** (ACTION_ON_FIGURE: draw on the printed grid). The picture is trivial but it is the figure
   the book gives, and the solution (C72) derives from it.
8. **C77 question is `required`** (corners A and B and the crease exist only in the picture). C78 shows the clean finished kite (book picture has
   hands; not renderable). Colours SET_B (flaps) and SET_A (uncovered triangles) follow the earlier author's hint; the word "flap" is the only text.
9. **Hexagon in C76 (e):** a convex hexagon made of 2 kites joined along their sides of length 1.7321 was chosen (a concave hexagon is also
   possible). Pentagon (d): kite on top of a rectangle (convex).
10. **Tangram tick marks (C88)** sit inside the piece they belong to (short stroke from the midpoint of the side into the piece), because most
    sides are shared with a neighbour piece and a tick across the edge would be ambiguous. Counts compare sides only inside one piece (stated in
    the spec).

### Class 5 Ch 7, chunk D
- C101 solution (required): "same kind of answer as Q1" rule; the LP text alone would also do.
- C103 solution (optional, not added): a rectangle-and-square picture would help.
- C114 solution (optional, not added): see above.
- C116 solution (required, spatial): the text solution is complete; the layer picture is the only way to show the hidden cube.
- C109 worked (required): same reason as C116; the teaching image exists but is not linked.
- C121 and C122 worked (required): a careful student could do both from the text (a matchbox is familiar, 6 x 4 / 2 is arithmetic). Kept required because the steps refer to faces at one corner and to edge groups that must be seen (SPATIAL_GEOMETRY, HIGHLIGHT_MEANING) and by decision 5 a teaching image is no reason to drop them. If you prefer less, these two are the first to turn optional.
- C108 worked (required): the text lists every face position, but "View 1 / View 2" are named figures and cube views are the typical case where seeing helps.
- C99 solution (required): printed figure is the finished drawing; the question side is none for the same reason.

### Class 5 Ch 7, chunk E
- C125 (Ans1), C127 (Ans2), C131 (Ans4): none (no new visual content). C129 (Ans3): required (vertex marking), as explained above. Sibling-consistency reason is stated in C129's `reason`.
- C133 (Ans5): none, a cube with one corner marked would be nicer, not needed.
- C134 (Q6): none (OPEN_ENDED), although the book prints three models next to the question; C135: required (the sample answer is a built model).
- C124 (Q1): required although the LP text names no picture.
- Book picture colours not copied (neutral fill), see section 1.

### Class 5 Ch 8, chunk A
- M1.S3.T3.C5 / C6 (Check! Check!): none / none. The book list has empty tick boxes and the answer is ticks and crosses, so ACTION_ON_FIGURE could be argued. Chosen: the seven item-and-weight lines are a plain list already in the question text (LATEX_TABLE) and the sample answer is seven yes/no marks that the LP states in words; Anu's room is a scene with no numbers (DECORATIVE_ONLY). If a figure is wanted: question = the list with seven empty boxes, solution = ticks on Bed, Rice Bag, Bucket, Water Bottle and crosses on Iron Almirah, Sofa, Refrigerator in ANSWER green.
- M1.S5.T5.C11 solution required (see above).
- M2.S6.T6.C12 worked example required (see above).
- M2.S9.T9.C23 / C24: the double number line is only an aid ("You can use the double number line given below"), so the question can be answered without it. Taken as required because the question text points to a figure that the LP text does not describe and the marks exist only in the picture (FIG_REFERENCED, DATA_IN_FIGURE); the solution fills the line as the LP's check line does. If the reviewer reads the aid as optional, both sides would become none/optional.
- M2.S11.T11.C28 (picnic fruits): "descending order" is a written list of four names, not an arrangement of pictures, so none.
- M2.S8.T8.C17 / C18 (Shrenu): the book's scale shows 3000 g but nobody reads it; the answer is the number 3,500 g, so none.
- Worked examples C13, C25, C31, C32, C33 are none because the rules give no figure for them (pure arithmetic or word problems with every number in the text); the kept teaching images (cells, number line, double line, unit boxes, blocks) are not the reason.

### Class 5 Ch 8, chunk B
- **C43 / C44 elephant and whale:** the LP question text already states 5,000 kg and x 40, so a careful student could solve it from text. Kept `required` because the book question is "Observe the pictures", the figure holds the data, and the text still points at the picture (user decision 4: do not flip only because the LP text carries the numbers). The solution side is "complete the blank in the figure"; it adds only one value, so it could be argued `none` (SAME_AS_QUESTION_DIAGRAM). Kept `required` for the Act-on-figure pair (Q required, S required) and to match C37 / C38.
- **C49 / C50 King's Weight picture:** a balance with the king against 10 sacks illustrates "10 times his weight". Judged `DECORATIVE_ONLY` (no numbers in the picture, relation stated in words). A balance figure would be nice but is not needed.
- **C41 / C42 compare:** question `LATEX_TABLE`, solution `none`; a filled table of signs could be read as a "filled figure" under B2, but plain tables stay LaTeX.
- **C51, C52, C55, C57 column work:** `none` under `LATEX_ARITHMETIC` even though the book draws carries and borrows with circles and arrows (HIGHLIGHT_MEANING could be argued). Reason: the LP text spells out each carry and borrow, and LaTeX arrays can show kg | g columns.
- **C35 / C39 / C47 pictures (sachet, precision balance):** decorative, numbers in the text.

### Class 5 Ch 8, chunk C
- **C84 and C86 question diagrams (required).** A careful student could compute the answer from the text alone, so by the tie-breaker alone they would be none. They are required because the book question is a figure to complete (blank value and blank multiplier on a given number line, ACTION_ON_FIGURE), and the LP's earlier card and `q_figure` note the figure belongs to the question. If the reviewer reads "the question text does not mention a figure" as decisive, the pair becomes: question none, solution required, `derived_from` null.
- **C80 worked example (optional, not added).** Could be read as required (steps ask for a double number line, B2 "the steps describe it in words"). I read it as optional because the question gives no figure and text carries every number. If the user wants it added, spec: double_number_line 16:9 in the layout of C84, top labels `3 plates` / `9 plates`, bottom labels `240 g` / `720 g`, both arrows `×3`, worked-example token after the question text.
- **C82/C83 table (none, LATEX_TABLE).** The filled answer is a table, so B2 "filled figure" could be argued; kept as a LaTeX array because it is a plain table without colour meaning (Step C, and the prompt's own example).
- **C88 question (none).** The book asks the learner to make number lines but gives none: no question figure is invented (companion note); only the solution has one.
- **T18 Q3, Q4, Q6, Q7 solutions (none).** Subtraction with borrowing could use a column picture, but column work is LATEX_ARITHMETIC and the book prints no picture for these questions.

### Class 5 Ch 8, chunk D
- **C104 solution (containers): required, could be none.** Step E lists "figure-based question, numeric answer: S none". Kept required because the printed blanks sit on the figure and the LP solution's key idea (capacity = top mark) is a highlight on the figure that text cannot show (HIGHLIGHT_MEANING). If the user prefers the typical-pair rule, change C104 to none (SAME_AS_QUESTION_DIAGRAM) and drop its four NEW- inventory entries (they would become none:SAME_AS_QUESTION_DIAGRAM).
- **C105 question: required although the book's own line already prints "2000 ml"** (the first question). Kept as the book prints it; the six blanks are the task.
- **C107 / C108 and C118 / C119: tables to complete are none** (LaTeX table) on both sides, although a filled table can count as ANSWER_IS_FIGURE; the plain-table rule was applied as in the Number Play precedent.
- **C125 solution optional** (the arrow model, see above).
- **C92 / C93 tea:** a measuring jug marked 300 ml / 500 ml / 1 l would be a nice picture, but the text carries everything (TEXT_SUFFICIENT, none on both sides).
- **C96, C97, C115, C116 worked examples:** none although each has a teaching image; the picture need was judged on the example itself.

### Class 5 Ch 8, chunk E
- **C126 worked example.** Could carry a jugs-and-cans picture (a teaching image of exactly that already exists), but no trigger makes the figure necessary and the tie-breaker answer is "a careful student solves it from the text". Kept none.
- **Q1 (Riya vs Aarav).** A side-by-side jugs comparison (Riya 4,000 ml against Aarav 2,250 ml) would be nice, but it only makes the answer prettier: optional at most, and optional is not added. Kept none.
- **Q3 (a) (5 l into 250 ml glasses).** A row of 20 glasses or a double number line would help some learners, and the book's closing line says to use a double number line "whenever needed". But the question gives no figure and the answer is the number 20 by division. Kept none.
- **Q2 (b) (bottle poured into 8 glasses).** A bottle-and-glasses picture would only restate the text. Kept none.

### Class 5 Ch 9, chunk A
1. **C3 worked example (27 coconuts, 3 rows of 9): optional (not added).** No v3 trigger: the example describes its own array in words (3 rows of 9), nothing is referenced in a figure, the answer is equations; the book prints no picture for it (practice values). The array with its 9 columns and 3 rows outlined would help, and the kept teaching image of this concept already shows exactly that; that image was NOT the reason, the tie-breaker was (a careful student can do it from the text). If the user wants it drawn, it would be the C7-style picture for 3 x 9 (27 coconuts: 9 column groups of 3 and 3 row groups of 9).
2. **C4 worked example (names of dividend, divisor, quotient of 45 / 5 = 9): none.** A labelled equation (arrows to Dividend, Divisor, Quotient) can be written in LaTeX (underbrace); the book's box is a teaching figure. Borderline because the answer is "labels on an equation".
3. **C19 worked example (70, 700, 7000 / 10 on a place value chart): none (HEADER_BOXES_ONLY, LATEX_TABLE).** v3 "not a diagram" list names place value header boxes with digits. The concept image C19.IMG1 stays untouched. If the user wants a chart anyway: Problem | H | T | O rows 70 / 10 = 7, 700 / 10 = 70, 7000 / 10 = 700.
4. **C11 solution (4 x 8 array) is required but only fills the two count boxes and adds the caption 4 x 8 = 32.** The book prints no answer picture here (its answer box is blank lines), so I did not draw the two regroupings as for C7; the LP steps describe the same column and row groups, so a reader could ask for the C7-style picture too (sibling consistency). My reason: the C7 picture is required because the BOOK's printed answer is that picture (B2); C11 has no printed answer picture.
5. **C21 (nine division problems with three red hints)** none: the LP question text already lists all nine problems and the hints; the boxes' positions and arrows carry no meaning (NUMBER_LIST_IN_BOXES idea, coded LATEX_ARITHMETIC).
6. **C13 and C15 sample answers.** The puzzles have many correct answers; I drew exactly the LP's sample answer (C13: 36x2=72, 6x10, 6x8, 4x9, 3x8, 5x8; C15: 108/2, 84/2, 112/2, 54/6, 42/7, 56/8). Nothing in the picture says "sample"; the LP text does ("Sample answer ... Your answer may differ").
7. **C32 solution draws BOTH answers** (two boards side by side), because the LP answer is "yes, two answers" and the question asks "Is there more than one answer?". The LP's own s_figure hint mentions only the first. I verified by brute force over all 8! placements that exactly these two arrangements satisfy A/B=C, A-D=F, C x E=H, F+G=H.
8. **Questions with only words** (C8, C23, C25, C27, C29, C33 and all their answers): none, no figure in the book (the 35 / 1 bubble on p.1 shows a character only).
9. **Layout of the puzzle cards.** The book prints six puzzles in one row; on the 16:9 card they are drawn in two rows of three (reading order unchanged: 72, 60, 48 / 36, 24, 40 and 54, 42, 56 / three with 54, 42, 56 in the left circle). The book colours every puzzle differently (decorative); all use CELL_FILL. The book's puzzle body is a trapezoid, the LP calls them triangles; I drew the book's shape.

### Class 5 Ch 9, chunk B
1. **Place value charts, T9 Q2 and Q3 (C37/C38, C39/C40): none, code LATEX_TABLE + HEADER_BOXES_ONLY.**
   The book asks "Now fill the place value chart" (Problem | H | T | O). Two readings are possible: ACTION_ON_FIGURE /
   ANSWER_IS_FIGURE ("filled table") says required; the Step C rules say a plain table of numbers with no colour meaning, and place-value
   header boxes filled with digits, go to a LaTeX array (the audit's "not a diagram" list names both). I followed the Step C rule as written,
   because a LaTeX array shows the chart exactly (there is no colour, arrow or drawing in it). If the user wants these four
   drawn, each pair would be one 4-column table card (question: the three example rows filled and the empty rows; solution: all rows filled,
   `derived_from` the question). Note the headings: the book prints H, T, O; the LP text says Hundreds, Tens, Ones.
2. **Try It! Q1 and Q2: both sides required although the LP text carries every number.** The book question IS the box diagram the learner
   completes (split tree: split the dividend, divide each part, join with the sign; halving chain). The LP question of Q1 even says "The boxes show a plus sign
   ...", which points at a figure the text-only plan lacks. The answer is the completed diagram (step B2, arrangement / filled figure).
   Q2 (halving chains) has no such sentence, but it is the same kind of box diagram in the same Try It! set, so it got the same decision
   (sibling consistency). These are flow diagrams with arrows and operators, not plain tables, which is why they differ from point 1.
3. **One combined picture per side for Try It!.** The LP holds Q1 to Q4 in one concept (C55) and Q5 and Q6 in another (C57), with one
   question card each; the brief allows ONE question diagram and ONE solution diagram per pair. So the four split trees are one 2 x 2 picture
   and the two halving chains one two-row picture. The v3 prompt says a question split into parts gets one diagram per part, but the LP did
   not split them, so the brief's rule won. If the user prefers six separate pictures, the LP would first have to be split into six concepts.
4. **Panel/row numbers are drawn** ((1) to (4), (5), (6)) because the LP solution text refers to the items by these numbers (user decision 3).
5. **C35 (nine blue boxes of divisions): none.** Nine independent facts and the two hints are written in the question text; the boxes carry no
   position, colour or arrow meaning. Codes LATEX_ARITHMETIC + NUMBER_LIST_IN_BOXES. (The pink grid of Let Us Do Q2 is chunk A's.)
6. **Worked examples C41 and C61 (kept teaching images) and C42, C43, C62, C63: none.** They are practice-value arithmetic written as short
   equations; text alone solves them exactly as well. The decision does not depend on the kept teaching images (user decision 5): C41's bar and
   C61's bar are teaching images and stay untouched and unlinked.
7. **Open questions (C51 to C54): none** (OPEN_ENDED); the LP solutions are sample answers written as equations.

### Class 5 Ch 9, chunk C
- **C66, C70, C84, C86 (solutions with a printed layout).** Kept `none`. The coloured digit cells above the quotient (9|7, 2|1, 5|4|7, 4|3|1) only mirror the digits of the quotient. A side-by-side drawing of Susie's and Sunitha's layouts would compare the number of steps (6 against 2, 5 against 3), but the LP steps already say it in words ("Sunitha's way takes 2 steps and Susie's way takes 6 steps"). If the user wants a picture here, these four are the first to flip to `required` (type `other`, long-division layout, derived from nothing because the question side has no figure).
- **C71, C73, C89 (question side, partly blank frames).** Kept `none`: ACTION_ON_FIGURE could be argued (the student completes a frame), but the LP question text lists each blank, so the tie-breaker says the text is enough. The completed solution frames (C72, C74, C90) follow the question side (`none`).
- **C87 (blank column-multiplication frame).** Kept `none` (LaTeX array with H T O headings).
- **C93 and C94 (worked examples, `optional`).** Base-ten blocks sharing 83 on 6 plates and 412 on 4 plates would clearly help but are not needed to follow the steps. I decided this on the tie-breaker and the absence of a v3 trigger, not because the same figures already exist as kept teaching images C93.IMG1 and C94.IMG1 (user decision 5). If the user wants an own diagram for each worked example, flip both to `required`, `add_new_image`, `question_tex / after_question_text`, ids `M3.S22.T22.C93.IMG2` and `M3.S22.T22.C94.IMG2`; they would be copies of the two teaching images in content.
- **C81, C95 (worked examples with practice values).** `none` (take-away lines and two-way comparison are arithmetic). C95 has no teaching image.

### Class 5 Ch 9, chunk D
1. Question side of C97, C99, C101: the numbers are all in the text, so a strict "attempt" test could say none; I kept them required because the book prints the figure with the question and the question text points at it. If the user prefers, these three can drop to `optional`; the three solution diagrams would then need `derived_from: null` and would be redrawn as standalone figures.
2. Solutions C100 and C102 (and C104): required although the book prints no end-state picture; justified by the sibling rule and the LP's own s_figure hints for 10 to 12. If unwanted, C104 is the weakest (no figure at all in the book).
3. Let Us Divide (a) to (d), Let Us Do Q1, Let Us Solve 1 to 12: none by the v3 long-division rule although the book asks to complete a drawn layout. This is the biggest call (8 + 2 items). If the content team wants those layouts as pictures, they would be `other` diagrams of the two layouts per part.
4. C123 optional (not added).

### Class 5 Ch 9, chunk E
- C141 question: required, but the figure is a schematic redraw of a real map (see 1).
- C142 solution and C146 solution: optional (not added) rather than required (see 2 and 4).
- C145 question: bookshelf picture dropped as decoration (see 3). It does show the 4 long and 8 short panels of the list, so a reviewer could call it `optional`.
- C147 question and C148 solution: plain table kept as LaTeX instead of an image (see 5). If the table should be a picture, C147 would be `required` (DATA_IN_FIGURE, ACTION_ON_FIGURE) and C148 `required` derived from it; the spec would be a `cell_grid` with the 5 x 6 table and the five blanks (question) / the five filled values in ANSWER green (solution).
- C132 solution: table of combinations kept as LaTeX.
- C151/C153/C155 and solutions: kept as LaTeX equations.

### Class 5 Ch 9, chunk F
- **C171 / C172 (Q4 tick table) as required.** A careful student could decide always / sometimes / never from the text
  alone, and the LP text carries every statement and answer. I kept it required because the v3 rules say a printed
  filled/ticked table that is the answer is a figure (`ANSWER_IS_FIGURE`), the question acts on a given figure
  (`ACTION_ON_FIGURE`), and decision 4 says do not flip it to none because the text has the data. If the user prefers
  text, the fallback is a LaTeX array with the five statements and a tick column.
- **C163 worked example:** none, but a three-column picture "always / sometimes / never" would be the natural
  optional figure if the user ever wants one.
- **Row letters in the Q4 picture** (1.2): not in the book's table.

### Class 5 Ch 10, chunk A
- **Worked examples C3 (M), C4 (B, W, H), C21 (M, S, plus), C13 (Z, T), C12 (pinwheel)**: all required. The LP steps already carry the reasoning in words and the letters are familiar, so a careful student could follow them without a picture; I kept them required because every one asks about a fold line or a turn of a shape (`SPATIAL_GEOMETRY`) and the answer is itself a set of marks or positions on the shapes, and because of decisions 4 and 5. Weakest cases: C3 (the letter M) and C4.
- **T3 Q1 and Q2 questions**: the letters are also named in the text; required because the book prints the row and the symmetry of a letter is a property of its drawn shape.
- **T4 question (C10)**: the task is an open cutting activity; required only because it points at the printed pictures.
- **T6 solution (C16)**: `none` (could be argued `required` with ticks under the five pictures).
- **T10 Q3 (C27, C28)**: `none`; a picture of 69, 38 and 88 with a half-turn arrow and a horizontal line would be possible but the sample answer is a plain list of numbers.
- **T10 Q1 solution (C24)**: lines and half-turn arrows (not ticks and stars); ten digits with up to three marks each is the busiest of the letter/digit pictures.
- **T8 solution (C20)**: the largest spec (3 rows x 4 turned letters + 3 verdict texts). The verdict cell text "Yes, at 1/2 turn" has four words (the book's own wording, "values filled in").
- **T12 solution (C33)**: two designs in one picture; two designs because the LP describes both (b) and (c).

### Class 5 Ch 10, chunk B
- **M3.S13.T13.C35 (Let Us Think Q1, solution): optional, not added.** Figure-based question with a Yes/No answer; the LP steps name every colour cell by cell, so text carries it ("typical pair": Q required, S none). Figures that would help: the square after a 1/2 turn (identical) and after a 1/4 turn (green and pink swapped). If the user wants them drawn, flip to required and derive it from C34.IMG1.
- **M3.S17.T17.C52 (design B, solution): none.** The question figure already shows the 4 hearts and both dashed lines (the book draws them); the answer is two words. Only a turn arrow would be new. Sibling check: C35 and C52 are the same kind of answer (figure given, short fill-in) and are treated alike (nothing drawn); C35 is `optional` because the turned pictures carry new information, C52 is `none` because they would not.
- **M3.S15.T15.C46 and C47 (worked examples): required, one diagram each.** The book has no figure for these LP-authored examples. C46: the answer to "what does the whole print look like" IS a drawing (ANSWER_IS_FIGURE), so the single diagram shows the given half print, an arrow, and the whole print with the copied half in ANSWER green. This shows the answer before the steps (a worked example is not a test), the alternative would be to draw the half print only. C47: SPATIAL_GEOMETRY, the print (flower at the top, the same flower turned a half turn at the bottom). Per the 23 Nov decision both get their own diagram although the kept teaching images show the same pictures; media ids C46.IMG2 and C47.IMG2 (IMG1 is the kept teaching image).
- **M3.S16.T16.C49 / C50 (matching blocks to prints): required, but the book shows PHOTOGRAPHS** of carved wooden blocks. The rule list has NOT_RENDERABLE for photographs; I kept it required because the question cannot be attempted without the blocks and prints (FIG_REFERENCED / DATA_IN_FIGURE / ACTION_ON_FIGURE all hold). The spec asks for flat line-art glyphs that keep each block's identifying shape and its exact half print (drop, lotus, rosette, fan, plant; halves cut on the vertical middle line, sides checked on the page picture). If the team prefers the real photographs cropped from the book (page 5, tiles (i)-(v) and (a)-(e)), the layout and the lines of the solution stay as specified. Decide before drawing.
- **M3.S14.T14.C41, C45 and M3.S19.T19.C56 (open sample answers): required.** The questions are open ("make your own designs", "create patterns"), but the LP solution gives a concrete sample (three designs; a block printed 4 times at quarter turns), and the answer is an arrangement (Step B2, ANSWER_IS_FIGURE). The questions C40, C44, C55 get no diagram (no given figure). C41 and C45 draw the same three designs (C45 regrouped under the three category titles the LP uses, exactly as in C41). C56: the LP only says "a simple shape", so I chose a drop-shaped print so that each quarter turn is visible; `needs_lp_text_sync: true` (the LP text could say "a drop shape").
- **M3.S13.T13.C38 (Let Us Think Q3, question): required, two designs.** The book says only "these designs" (the 2 x 2 square above and the square the student colours). The LP's own figure hint shows both designs, so the question figure shows the green-pink square and the orange-blue square, the latter coloured as in the LP solution of the previous question (orange first, going clockwise from the top of the vertical line). Strictly the second design is the answer of the previous question, not given by the book. Alternative: draw only the green-pink square on the question side.
- **M3.S18.T18.C53 / C54 (19 border shapes): required.** Numbers 1 to 19 are shown next to the shapes in BOTH figures because the LP solution refers to "Shape 13" etc. (see LP text issues). Layout: the book border is a page frame (5 shapes on the top, 5 on the right, 4 at the bottom, 5 on the left); the diagram uses a 7 x 5 ring (7, 3, 6, 3 shapes) so that it fits a 16:9 card; the order round the ring is unchanged. Solution marks differ in shape (tick, star) and colour (ANSWER green, SET_A blue).
- **M3.S14.T14.C42 / C43:** the triangles of the 4-square shape are drawn as printed (base 1.8, height 1.8, not equilateral); the LP calls them just "triangles", while C40/C41 talk about equilateral triangles (those are the cut-outs).
- **Colours:** green, pink, blue and sand of the designs are the book's own colours (explicit hex values, since the style tokens have no pink or sand). In the orange-blue square the fills use SET_B and SET_A (the LP names the colours) instead of ANSWER green.
- **Figure claims:** P05-photo_pair-2 (block and print photographs) and P06-photo_pair-1 (design A print) are teaching figures that no LP item draws; mapped to none (DECORATIVE_ONLY, TEXT_SUFFICIENT). Design A (4 leaf motifs at quarter turns) is the book's own example; the LP's worked example C47 replaces it with a two-stamp flower, and no LP item asks about design A. The two NEW- entries are the second uses of P04-pattern-2 and P04-grid-3 in the question of C38.

### Class 5 Ch 11, chunk A
- **C3, C12, C28 (worked, required).** The text carries every number; only the steps' wording ("add all 5 sides", "4 rows of 6, cut corner to corner", "lay Q on P") points at a
  picture. They are the weakest of the five; if the team wants worked examples drawn only when the text says "drawn / shown", set these three to `none`. C11 (gaps must be
  seen) and C29 ("is drawn on a grid", whole and half squares told apart on the picture) are firmer.
- **C15 (rug solution) and C19 (tables solution) add only count labels** (15 and 6; 5 x 2 etc. and totals). Under Step D ("row totals beside a grid") these are close to
  `optional`; I kept them required because the LP's steps are exactly those counts and the figure ties them to the picture.
- **C10 (all sides labelled)** is also a label-only solution figure; kept required because the question figure labels one side of each shape and the hourglass sides are
  hard to count.
- **C6 (border traced)** required; the border outline is the core idea of the chapter.
- **C20 / C21 / C23 / C25** as in section 1 (5 to 7).
- **Same figure three times (C16, C18, C22).** One figure per item, identical specs; the build can render it once and copy it.

### Class 5 Ch 11, chunk B
- **C41 question (empty palm grid): required** (`FIG_REFERENCED`, "the square grid given below", the learner acts on it). It could be `none`: a blank grid is a thin figure, and a learner cannot really trace a palm on a screen image.
- **C45, C46, C60 required; C61, C62 none.** In all five the LP text carries every number, so the tie-breaker alone would give `none`. I made C45 (three rectangles of 16 unit squares) and C46 (three rectangles of border 20) required because the example *is* the visual comparison of three shapes,
  and C60 because the book's own example is a picture of patches in rows and the LP's steps count by rows (decisions 4 and 5: not flipped to none only because the text has the numbers). C61 (one rectangle 11 cm by 4 cm) and C62 (one square 7 cm) are one plain labelled shape each: `TEXT_SUFFICIENT`.
  If you want all five alike, either add C61 and C62 (a rectangle labelled 11 cm and 4 cm, a square labelled 7 cm) or drop C45, C46 and C60.
- **C38, C40, C55 optional (not added)** versus C32, C36, C49, C51, C53, C57, C59 required: the first three would only add numbers (counts, areas, perimeters) beside a figure the question already shows; in the required ones the solution adds the grid, the patches, new shapes, marks or ticks.
  C32 and C36 and C38 would look nearly alike; C38 is the odd one because the grid is already in its question figure.
- **C34 required** (overlay of B on A and on C): it is an arrangement answer, but the text states the result completely; drop it if you think words are enough.
- **C42 none, C43 none, C44 none:** open answers of the learner's own palm/leaves; a sample palm outline would be invented.
- **C57 and C59 solutions** carry tags (area, perimeter) beside every shape as well as ticks; the tags could be dropped if only the ticks are wanted.
- **Same figure three times (C31, C33, C35 questions)** and near-identical grid solutions (C32, C36): kept as one diagram per item, as the brief says.

### Class 5 Ch 11, chunk C
- C71 solution required (adds the filling and the counts) rather than none / SAME_AS_QUESTION_DIAGRAM. The question figure already shows the empty cells, so one could call it repeating.
- C69 solution required (the filled lengths); C86 solution required (only the 18 cm arrow is new).
- C72 / C73 none although the book prints a square picture next to the example (a teaching figure; the words carry everything).
- C74 / C75 none although the question says "go back to the previous examples" (figures live with their own questions).
- C76 none (lawn) against C77 required (side marked in parts): C76 is a plain word problem, C77 refers to a marked figure.
- C87 worked required although the L is described in words: the counting is easier and safer on a picture (tie-breaker); the kept teaching image shows the same tiles but is not linked.
- C65 required even though the learner's own answer will differ; the LP gives a concrete sample, so the figure draws exactly that sample.
- C79 / C80 none: a filled table could also be read as ANSWER_IS_FIGURE, but it is a plain table (LATEX_TABLE).
- C91 question required with the die showing 6: the die roll is random in the real game, but the book (step 5) and the LP q_figure both give it.

### Class 5 Ch 12, chunk A
- C7, C9 (clock-reading solutions) `required`; C11 `none` (see 3). If the content team wants fewer diagrams, C7 and C9 are the ones that could
  become `none` (SAME_AS_QUESTION_DIAGRAM) without breaking anything else.
- C22 (Q7 matching solution) `optional`, not `required`: six lines joining two columns of times is an arrangement (ANSWER_IS_FIGURE), but
  the LP answer lists all six pairs and the question lists are plain numbers in boxes (NUMBER_LIST_IN_BOXES says "optional if the expression
  already gives the answer"). If the user wants the matching drawn, C22 becomes required: two columns of six times (the printed order) with
  six ANSWER lines.
- Optional (not added): C3 (time line 04:25 p.m. to 05:10 p.m.), C17 (time line 13:40 to 16:15 hours), C13 (three time lines for Q4),
  C24 (time line 08:00 to 09:05 hours), C15 (Q5 table with a minutes column and longest / least marked), C22 (above). They only make the
  text nicer; none is needed to attempt or to follow the steps. The teaching images already in the plan show some of these time lines, but
  that was not the reason for the decision.
- Tables with blanks or ticks (Q6 C19/C20, Let Us Do C32/C33, estimate and verify C36/C37) are `none` with LATEX_TABLE: plain tables,
  no colour meaning, the same call as the Number Play precedent in the prompt ("complete the table" is LATEX_TABLE). A tick is a LaTeX symbol.
- Worked examples C4, C16, C25, C26 `none` (word comparison, arithmetic, word choice).

### Class 5 Ch 12, chunk B
1. **T12 C44 and C45 `required`** although the data are in the question text: the dial is the subject (MEASUREMENT_READING) and (b) crosses 12; judged that the picture changes how correctly and how easily the child solves it. If you read the tie-breaker more strictly ("text alone is enough") these two become `none` with TEXT_SUFFICIENT; they are the only required items that rest on that judgement.
2. **T13 observe solutions `none`.** A shaded sweep from start to stop (labelled 30 / 35 / 15 / 60 seconds) would be a nicety, and it is the same kind of addition for all four, so all four stay `none`. Q4 (the full round, 60 seconds) is the one where a picture helps most; kept `none` for sibling consistency. If you want it, Q4 is the candidate for `optional`/`required`.
3. **T11 Let Us Find solutions `none`.** Sample answers mention hand positions; open activity, no figure in the book.
4. **T14 worked examples `none`.** A double number line would help the idea, but it is the job of the kept teaching image; the question itself is arithmetic.
5. **Minute-hand corrections** (observe Q3, draw Q4): see section 2. Borderline between "drawing inaccuracy" and "print slip".

### Class 5 Ch 12, chunk C
- **C76, C77, C78 worked examples (time after, time before, crossing noon and midnight): none.** A time line would help, and each concept already has a kept teaching time line (C76.IMG1, C77.IMG1, C78.IMG1, never linked). Judged on its own, no v3 trigger applies: no figure is referenced, nothing is read from a picture, the answer is a time, and a careful student can solve each from the text (tie-breaker). If the team wants a time line on the worked example itself, the three could be switched to required and the existing teaching time lines used as the spec (the C78 one would need two panels, a bus across noon and a train across midnight).
- **C68 Q1b question** says "You can use the above double number line". I read this as an optional help, not a reference the question cannot be answered without. If the team wants the line repeated here, it would be a second copy of C66.IMG1 (a repeat is the only change).
- **C69 solution** could draw a few of the answers on the number line, but the LP solution never uses the line, so none.

### Class 5 Ch 13, chunk A
- **C5 (required)**: LP text carries all four numbers; kept because the book question is the picture of the box.
- **C6 (required)**: the sample-answer box with the in-numbers; the answer could be read as only numbers.
- **C3, C8, C19, C20, C30, C31 (none)**: a picture would help a little, text suffices.
- **C16, C18, C25 (optional, not added)**: see judgement calls; C18 breaks the B2 "answer is an arrangement" rule only because nine numbers cannot share one picture.
- **C12 and C23 (required)**: the solution adds one array / the continued line to a figure the question already shows.
- **C29 (required)**: the answer ("only Robby reaches the food") could be argued in text, but the marked landings on the given road are the evidence.

### Class 5 Ch 13, chunk B
- C34, C44, C46, C48 trail solutions: the LP text lists every landing and friend, but the answer is marked on the picture in the book (jumps of 2 and 3) and the siblings follow.
- C40 solution (hops on the Q6 line): the answer is a list of three numbers; kept required because the task is to jump along the given line and the solution adds the hops and skipped numbers.
- C43, C45, C47 questions required although the p.5 book questions print no new picture.
- C58 question required although the LP text lists the 15 numbers.
- C50 worked example required (see above).
- C56 question optional and C57 solution none although the earlier author's hint `s_figure` suggests "jumps of 6 marked, landing on 30 and skipping 25" (one example of the check, not the whole answer).

### Class 5 Ch 14, chunk A
1. M1.S3.T3.C5 question none (book picture is illustration, text complete) while C7 is required. Flip C5 to required and the spec is identical to C7's (add `NEW-P01-scene-1-q1`).
2. M1.S3.T3.C6, C8 (Manu answers), M1.S6.T6.C17 (room answers), M2.S8.T8.C26, C28 (bus answers): optional, i.e. not added. Rule used: word answers read off a figure the question already shows do not need their own figure; labelled copies would "clearly help".
3. M1.S2.T2.C3 and M2.S7.T7.C23 (turn-left worked examples): optional; M1.S4.T4.C9 and C10 required although the text states the layout in words (they speak of a picture/plan).
4. M1.S6.T6.C19 required (sample drawing) but C21 none: the same sample room would repeat.
5. M1.S5.T5.C13 solution figure carries the colour words as text labels; remove them if the user prefers colour alone.

### Class 5 Ch 14, chunk B
- T9 solutions Q1 (C30), Q3 (C34), Q5 (C38): the answer is complete in text (two house names, "Stop 1", "south"), but each adds rings, lines or an arrow on the map; required for consistency with the route
  solutions Q2 and Q4 (printed answer is a drawing).
- T11 Q1 question required, solution none (see above).
- T12 (c) C51 and (d) C53 solutions: the answer is a number / an opinion; required because the solution counts along three routes on the map and the figure shows those routes with the counts
  (sibling consistency with (a) and (b)). (d) is an open answer, drawn as the LP sample (route A).
- T14 C56 question none although the book prints a sample map "given below": the learner can do the task without it.
- T15 C58 and C59: all data is in words, but the steps say "count the squares" of a grid and Route 3's wrong-way step is spatial; required.
- C39 and C40: required although teaching images show similar pictures (decision 5).
- T11 Q2 solution (C45): two rings on the map; required (the marked map is the answer).

### Class 5 Ch 14, chunk C
Applied the v3 rules as written; none flipped to `none` because the LP text carries the numbers.
1. **Eight solution figures that only mark the walk, the rings or the length labels on the question figure** (the answer is blanks, a pair of numbers or an animal name): M3.S17.T17.C64, C66, C68 (labels 3 cm north / 3 cm west + 2 cm south / 5 cm south + 3 cm east + 2 cm north), M3.S19.T19.C75 (panda), M3.S20.T20.C77 (tortoise), C79 (snake), M3.S21.T21.C81 (six animals), C83 (six positions). I kept them `required` because the solutions are counts and walks along the figure and the figure adds new marks (v3 Step E: "new marks, a highlighted part"). By the Step E pair "figure-based question, numeric answer: Q required, S none" they could also be `none`; if the user wants text-only solutions for fill-in questions, these eight become `none` (SAME_AS_QUESTION_DIAGRAM or TEXT_SUFFICIENT) and nothing else changes. Sibling consistency holds: all eight are alike, and the two with answers that are themselves drawings (C70 routes, C85 dots) are `required` for B2 reasons.
2. C71 / C72 worked-example figures (see above): given-state vs complete picture.
3. Ant Q4 solution colours (ANSWER / SET_A / SET_B for three routes).

### Class 5 Ch 15, chunk A
- Q2 to Q5 of Child TV Reporter question side `none` (plain table to LaTeX). An alternative reading is `required` (FIG_REFERENCED: "Look at the table"), a plain filled table as a picture. I followed `LATEX_TABLE`; this only works if the LP text sync is done.
- Q1 question draws the notebook only; the empty table is LaTeX. An alternative is one picture with the notebook and the empty table side by side (and a solution picture with the counts filled in).
- C6 solution `optional` (notebook bubbles coloured by answer value would help counting 35 bubbles).
- All seven pictograph numeric solutions `optional` (see above); the old plan had a picture for each. If the team wants "outline + value" solution pictures, these seven flip to `required` with `derived_from` the question diagram.
- C26 worked example `required` although the numbers are in the text; C3 worked example `none`.
- C16 holds two pictographs in one picture (could be split in two).
- Question side of C24 and C36 ("choose another scale") `required`: the data to re-scale lives only in the book pictograph.

### Class 5 Ch 15, chunk B
- **Recording a Day solutions (C42, C44, C46, C48, C50) = none.** A highlighted copy of the same figure (the two compared rows circled, hours written beside them) could be argued as HIGHLIGHT_MEANING. I kept `none`: the question figure is already in the card above it and the LP text lists every number. C48 (the five pairs, answer No) and C50 (balanced routine, an opinion) are the two I am least sure about.
- **Worked examples C38/C51/C52 show the answer (finished graph) before the steps**, because a worked-example token must sit after the question text. If the content team wants only the given data, the bars would have to be removed (then C38 would show the rows only; C51 and C52 would need no figure).
- **C61/C63/C65/C67 required.** The LP text lists all five heights, so a strict reading could make them `none`/TEXT_SUFFICIENT. I kept them because the solution reads a graph that has no other figure on its card, and C59 (same kind of answer set) is required.
- **C54/C55 none (LATEX_TABLE)** against a possible ANSWER_IS_FIGURE reading of "filled table" (see above).
- **C56 question required.** The frame is only a template (scale, axis titles, place names), but it is what the book gives and what the child draws on; the alternative is OPEN_ENDED/none.

### Class 5 Ch 15, chunk C
1. **M3.S15.T15.C82 worked example: required (own diagram M3.S15.T15.C82.IMG2).** The text says "A picture shows 9 children (practice values)" and gives all counts in words (4 hats, 5 flags, 2 both). By the tie-breaker alone this could be `none`. I applied v3 as written (FIG_REFERENCED, the whole topic is "reading a picture") and the user's rules 4 and 5 of 23 Nov: the same arrangement is the kept teaching image C82.IMG1, it is not linked, the item gets its own picture. The picture is the arrangement of that teaching image (children 1-2 hat + flag, 3-4 hat, 5-7 flag, 8-9 neither). If the user prefers `none` for this item, only this entry changes.
2. **Food Wastage solution Q3 (M2.S14.T14.C75): optional (not added).** Numeric answer by arithmetic (5 + 6 + 8 + 7 + 4 = 30) from a given figure: Step E "figure-based question, numeric answer: Q required, S none (or optional)". A graph copy with the five readings and the total would help a little (Step D, totals beside a figure).
3. **Food Wastage solution Q4 (M2.S14.T14.C77): none (LATEX_ARITHMETIC).** 30 x 3 = 90 does not touch the graph. Kept `none` rather than `optional` because the figure would be an arrow picture, not the graph.
4. **Food Wastage solutions Q1, Q2, Q5, Q6: required.** The answer is a bar (or two bars) of the graph: "boxed largest / circled smallest" is the named HIGHLIGHT_MEANING case. Each also writes the five readings above the bars (LP step 1 reads them). Q6 is a prediction (sample answer) but its answer is the tallest bar with the reason "its bar is the tallest", so it gets the same mark as Q1 (sibling consistency). Q5 boxes Monday and Friday, the pair the LP sample answer uses.
5. **True or False solutions, all 8 required.** Every solution counts a group of children in a picture of 17; the figure rings every counted child (HIGHLIGHT_MEANING), so the learner can check each count. The LP text carries the counts (user's rule 4: not flipped to none for that reason). Sibling consistency: all eight get a figure.
6. **T/F statement 5 solution (books 14 vs caps 10):** only the 14 book holders are ringed (as the LP step counts), the 10 caps are not ringed again (they are ringed in the solution of statement 2 and are visible as caps on the glyphs). A second ring style would crowd 14 of 17 children.
7. **T/F statement 1 solution:** only the 3 girls with glasses are ringed. The LP's "for example, the girl in the front row with a cap and no glasses" is not marked because two front-row girls fit it (see LP text issues).
8. **Solution key tags** ("3 girls", "10 children", "7 boys" / "7 girls", "7 children", "14 children", "4 boys" / "3 girls", "6 children", "1 child") use only words and numbers of the LP solution text, at most 3 words, in ANSWER green, beside a sample ring.
9. **Colours in the people pictures.** The book shows red caps and blue clothes; the style tokens have no red and WRONG is reserved, so caps are SET_B (amber), books SET_A (blue), backpacks GUIDE (grey), clothes CELL_FILL / MARK_FILL. Rings are FOCUS. Boys' rings solid, girls' rings dashed where two groups are compared (a key tells which).
10. **People are drawn as flat glyphs, not as the book's illustration.** I rejected NOT_RENDERABLE: the figure's information (who wears what) is fully carried by the glyph attributes, and no statement needs faces or art. Every child's attributes are listed in `content` and in `manim_description`, and the counts are asserted in the generator.
11. **Worked example picture:** the nine children alternate pinafore / shorts only as decoration; no statement uses gender. Hats are drawn as the cap shape.
12. **Same book picture or graph used by several items:** one diagram per item, identical spec (render_note says "same as ..."). Their inventory entries are `P08-bar_graph-1` / `P09-arrangement-1` for the first use and `NEW-<id>-q<n>` for each further question use.

### Class 7 Ch 15, chunk E
1. **M4.S25.T25.C158 worked example (ancient Indian notation), REQUIRED.** The LP steps and answer carry every word of the notation
   ("yā 2 rū 8 with a dot over the 8", "yā 3 rū 4 above yā 2 rū 8"), so a strict "text carries all" reading gives `none`. I chose `required`
   (ANSWER_IS_FIGURE + HIGHLIGHT_MEANING) because the answer IS the notation table (a filled table), a dot over a digit is a mark that
   carries meaning (a negative number) and cannot be shown reliably in plain text, and "the two sides one below the other" is a layout.
   No concept image shows this table (`concept_images.json` has nothing for M4.S25), and teaching images are never linked anyway.
   Spec: 4 x 2 table, header "Modern" / "Ancient Indian" (the book's column labels, shortened), three body rows, one drawn dot over the 8
   of body row 2 only, the lower 8 of body row 3 has no dot; the book's three bracketed notes are left out (the steps carry that wording).
2. **Q11 (a) (C156 / C157), `none`.** In the book, part (a) has red slashes through the 6 of 6x and of 66 and an "11" above 66. That only
   shows how line 2 ("x + 9 = 11") arises, and line 2 is in the LP text; the LP solution also says "6x and 66 were divided by 6, but 9 was not".
   A careful student loses nothing, so `none` (LATEX_ARITHMETIC). Same decision for (b) and (c) (sibling rule). If the team wants the slashes
   kept, this is the one question to flip.
3. **Mend the Mistake boxes 1 to 9 (C138 to C155), question side `none`.** The printed boxes are in the book's inventory as "worked_steps
   given in question". They are chains of equations (LATEX_ARITHMETIC, explicitly a Step C case); the peach fill and the number badge carry no
   meaning and every line is already in the LP text. Solution side `none` too: the answer is the named mistake plus corrected equations, and the
   book has no printed answer picture. All nine boxes and Q11 (a)(b)(c) get the same decision.
4. **Summary block 4, the magic trick (C170, block 4), `none`.** A flow strip of the operations (x, then x2, +10, /2, -x, +3, giving 8) would only make it nicer (the book has
   no such figure; the only picture on p.27 is a group of children, decoration), so I did not even mark it `optional`.
5. **Cut-out sheets (P28 tangram, P30 / P32 / P34 dot paper), `none:OPEN_ENDED`.** No question, example or LP item refers to them. I claimed them
   here because they sit after the Summary (the last book section of my chunk) and no other chunk has an end section. Another chunk could claim the
   same figures with `DECORATIVE_ONLY`; any `none:` code means the same thing (no diagram, no link). The four blank cut pages (29, 31, 33, 35) carry only the
   scissors line and are not in the base inventory.
6. **P18 / P19 boxes claimed here.** Chunk D owns the teaching topic M3.S23.T23 (same book section 7.3) and may claim these nine figures too; I mapped
   them all `none:LATEX_ARITHMETIC`, which is the natural code, so a duplicate should compare equal.

### Class 8 Ch 1, chunk A
Apply the v3 rules as written; these are the calls where a reviewer might want the other answer:
- `M2.S10.T10.C41` / `C42`: required although the LP text carries all the numbers (see above).
- `M1.S3.T3.C8` / `C9` (which lockers stay open): none. The printed answer is the list 1, 4, 9, ..., 100; the 10x10 locker grid (C4.IMG1) is a teaching image and would only make the list nicer.
- `M1.S3.T3.C6` / `C7` (factors of 36): none. The book prints no answer picture; the pairs are LaTeX equations.
- `M2.S6.T6.C25` worked (sum of the first 8 odd numbers): none. An 8x8 dot square built from L shapes would help but the rule n² = sum is stated in the text and the 6x6 teaching image C25.IMG1 exists. Could be `optional` if the reviewer wants the figure.
- `M2.S6.T6.C26` worked (subtract odd numbers from 38): none. The book prints it as a chain of subtractions on a cream band; number chains are LaTeX.
- `M2.S8.T8.C33` / `C34` (pattern, Figure it Out Q8): none. The book's pattern and its printed answer are typeset equations with bold underline on the three filled numbers (21, 90, 91), not a drawn picture.
- `M2.S10.T10.C39` (blocks of 100): none. The book's ten-block table is a plain fill-in table.
- `M2.S9.T9.C35` worked (numbers between 25 and 36): none. The number line is a teaching image (C35.IMG1).
- `M2.S4.T4.C12` worked (areas for sides 6, 3/5, 2.5): none; three squarings.
- `M1.S2.T2.C2` worked (locker 12): none.

### Class 8 Ch 1, chunk B
1. `M2.S15.T15.C64` question (FiO1 Q9, tile picture): `required`. The LP text states "9 rows of 9 tiles ... 5 by 5 tiny squares", so a text-only student could count 81 x 25, but the book question is "How many tiny squares are there in the following picture?", so the picture is the thing counted. Kept `required` under user decision 4.
2. `M2.S15.T15.C65` solution: `optional` (not added). The answer is a number. A figure repeating the tile picture with the 9 by 9 tiles and one 5 by 5 tile marked would be the Step D "row totals beside a grid" case. It would not repeat the question figure exactly, so I did not use `SAME_AS_QUESTION_DIAGRAM` alone (both codes are given).
3. `M3.S19.T19.C80` question (cubes of edge 2, 3, 4): `none`. The book draws a 2 x 2 x 2 cube beside its own version of the question (`P11-solid-4`, listed as "given in question" in the base), but the LP question gives only the three edges in words and the tie-breaker answer is yes (a careful student solves it from the text). A question picture of three cubes cut into unit cubes would also nearly hand over the counts.
4. `M3.S19.T19.C81` solution: `optional` (not added). Three cubes of edge 2, 3 and 4 in layers of 4, 9 and 16 unit cubes would be the natural picture and the book draws the edge 3 and edge 4 cubes, but the steps already state the layers and the answers are numbers. If the user wants it, a `solid_3d` spec is easy (oblique drawing, three separated layers, counts 4, 9, 16 only in the solution colours). The edge 3 and edge 4 cubes are teaching images C79.IMG1 and C76.IMG1, which are never linked.
5. Square-root answers that "pin down" a root with a number line in the teaching image (`M2.S16.T16.C66` worked, `M2.S17.T17.C71`, `C73`): `none`. The book prints no figure for them and the steps are inequalities and products; the number lines exist as teaching images C66.IMG1, C67.IMG1 and C68.IMG1. Decided for sibling consistency with the rest of T11 to T17.
6. Prime-factor solutions (`C57`, `C59`, `C61`, `C63`): all `none` (`LATEX_ARITHMETIC`). The grouping brackets (2 x 3 x 3) x (2 x 3 x 3) are written in the steps and the book prints them as text. Same decision on all four, as the prime-factor pairs are siblings.
7. `M2.S11.T11.C45` worked example (square of area 64): `none`. No picture in the book; the square of side 8 is teaching image C45.IMG1.
8. `M2.S11.T11.C47` worked example (81 down to 0): `none`. The book's yellow band (`P08-number_chain-1`) is nine plain subtractions, no arrows or highlights, so `LATEX_ARITHMETIC`.

### Class 8 Ch 1, chunk C
- C95 solution **required** (filled difference tower) while the question is **none**. A reviewer may prefer the question to be required as well (book figure to be completed: ACTION_ON_FIGURE). I kept it none because the figure repeats the numbers already in the question text.
- C113 worked example **required**. The answer is a list of 17 numbers that the LP already writes out; I applied B2 (answer is an arrangement / filled figure) as written and did not flip it to none.
- C93 solution **optional** rather than none (the pairing check would benefit from a picture but is complete in text).
- P14-number_pattern-1 is **none** (LATEX_ARITHMETIC): a typeset pattern, no colour or boxes.

### Class 8 Ch 2, chunk A
- C6/C7 (fill the thickness table, folds 21 to 45): `none` via LATEX_TABLE for both sides. The answer is a filled 25-row table, so ANSWER_IS_FIGURE could be argued, but the table is plain numbers with no colour meaning, and the tie-breaker (a careful student loses nothing with a LaTeX array) says text. If the user wants it as a picture, C7 solution is the place (derived_from none, since the question side stays none).
- C8 question: the book question depends on the plain thickness table (FIG_REFERENCED could be argued, "cannot be answered without it"). Kept `none` because the LATEX_TABLE rule delivers a plain table as text, but this item needs the LP text issue above fixed to be answerable.
- C33 solution: `required` because the counts are written on the tree and the solution is built on them. It could be argued `none` (SAME_AS_QUESTION_DIAGRAM + numbers in text). Kept required: the picture shows the final state with the new marks.
- C17/C18, C23/C24 factorisation ladders: a prime ladder would help, but the divisions are a number chain already in the steps (v3: LATEX_ARITHMETIC). Not made `optional` so that no ladder is requested for the four sub-parts of C24.
- C3 worked example: a height scale (670 m against 830 m, 10.7 km against 11 km) would be nice, but the plan already has it as teaching image C3.IMG1 (never linked), so `none`.

### Class 8 Ch 2, chunk B
1. M3.S11.T11.C54 / C55 (Figure it Out Q7, "Circle the numbers that are the same"). Chosen: question `none` (NUMBER_LIST_IN_BOXES, TEXT_SUFFICIENT), solution `optional` (NUMBER_LIST_IN_BOXES, HIGHLIGHT_MEANING), not added. Why: the book prints five expressions in one plain row (no boxes, no colour) and the LP question text already lists all five; v3 "Not a diagram" says a board of numbers to choose from is listed in text, and for the solution side (arrows or circles on such a list) allows only `optional` when the LaTeX answer already gives the result. The printed answer on pdf page 36 is words ("2^4 x 3^6, 6^4 x 3^2 and 18^2 x 6^2 are same"), not a marked picture. If the user wants a circled-row picture anyway, it would be a `cell_row`-style card: five expressions in one row, the first, second and fourth circled in FOCUS, nothing else. Not specified in full because it is not added.
2. M3.S13.T13.C60 / C61 (Estu's and Roxie's outfits). Chosen: both sides `none` (TEXT_SUFFICIENT / LATEX_ARITHMETIC). The book hint says "Try drawing a diagram like the one above" and the book does draw Estu's tree (a teaching figure, mapped to concept image C56), but the question gives no figure and the printed answer is only "7 x 2 x 3 ways". A choice tree for Roxie (7 dresses x 2 hats x 3 shoes) would be nicer but is not needed to solve it exactly as well from the text.
3. M4.S15.T15.C70 (halving a line of 16 units, worked example) and M4.S17.T17.C78 (halving past 1). Chosen: `none`. A picture of the line halved would be a nice visual, but the book draws no line here (it is "imagine a line of length 16 units"), the numbers are all in the text, and the plan already carries a teaching image for each idea (C70.IMG1, C78.IMG1) that stays and is not linked.
4. M3.S13.T13.C62 and C64 (password locks). The book's digit-mapping picture (lines from digit 0 to all ten digits) is a teaching figure and was mapped to the nearest plan teaching image (C57 "Five slots, ten choices each"): the idea is the same (10 choices per slot) but it is not the same drawing. If the merge wants an exact match, change the mapping to `none:TEXT_SUFFICIENT`; nothing else changes.
5. P11-table-2 (the green box of three general rules on pdf page 11): claimed by this chunk as `none:TEXT_SUFFICIENT` because it sits in the 2.3 section of C79, C83 and C85. If chunk C (Power Lines, same page) also claims it, the meaning should stay "formulas only, no figure needed".

### Class 8 Ch 2, chunk C
- **C91 required** (the LP steps already give 65536 = 4^8 etc., so a careful student could follow from text; kept required because the example is explicitly "use the power line" and for consistency with C96). Alternative: none / TEXT_SUFFICIENT.
- **C94 question: none** although the power line of 4 (pdf p.11) is on the previous page. The question text carries 16384, 1024, 4^2 and 4^-2 and never says "use the line". Alternative: required (DATA_IN_FIGURE).
- **C123 worked example: optional** (not added): the Earth-ladder-Moon sketch with "20 cm" and "3,84,400 km" would help but the text gives both numbers; the two growth expressions (20 + 20 + ..., 0.001 x 2 x 2 ...) can be LaTeX.
- **C106 question: none**: the three large-number facts are plain text in the book; they are missing from the LP text (see below), which does not change the decision.
- **Tall figures at 4:3**: if the builder wants every card strictly 16:9, the power-line figures will be letterboxed.

### Class 8 Ch 2, chunk D
- C147 question: bold first parts (HIGHLIGHT_MEANING could be argued; bold is plain text, so none).
- C147 solution and worked examples C144, C145: a picture (strips of 1000s, staircase of names) would help understanding, but the concept images already teach it and the text is complete. Kept `none`, not `optional`.
- C132 and C134 questions: the data is outside the LP text (see section 2). Kept `none` as the book gives no figure.
- C136 question: comic panel with the number in a bubble (decorative, number in text).

### Class 8 Ch 3, chunk A
- **M2.S9.T9.C31 required** (the only one that could go either way). Reason for required: sibling consistency with (a) in the same example, and the four-step carry is where learners slip. Reason it could be optional: the book prints no picture for (b) and the LP steps carry every count. Flip to `optional` (action `drop_image`) if you prefer picture-only-where-the-book-has-one; the validator then needs the C31 item to be changed and the counts in `meta` adjusted.
- **M2.S10.T10.C35 required**: the LP steps already carry all the counts (decision 4: not flipped to none for that reason); required by B2 because the book's own answer is the picture.
- **M1.S2.T2.C4**: FIG_REFERENCED ("use Table 1") against LATEX_TABLE (plain table). I chose none + LaTeX array; the cost is only the LP text issue above.
- **M1.S3.T3.C8 optional vs none**: a four-picture stick strip would help; nothing in the book needs it.
- **M2.S11.T11.C37**: a filled comparison table could be read as ANSWER_IS_FIGURE; it is a plain table of words with no colour or marks, so none.
- **Worked examples with teaching images** (C3, C13, C14, C23): none, since the figure the example would need is the teaching image, which is never linked and would leak the answer if placed after the question.
- Figures P04, P05-table-2, P01 are mapped to concept images although the match is of idea rather than of the exact book picture (teaching images are redrawn, not copies); P03, P08, P09-map and P10 use `NOT_RENDERABLE` only to say "not drawn, no item needs it", not that an item is blocked.

### Class 8 Ch 3, chunk B
- **C62 required vs C41 optional.** Both examples give their numerals in words in the LP. C62 is required because the book itself works that example with drawn symbol numerals (the figure the book gives is the data and the answer picture); C41 ("An Egyptian numeral shows 3 lotuses, 4 heels and 6 strokes") is the LP's own example with no book figure and a teaching image of the concept that shows the numeral, so a picture would help but is not needed (optional, not added). If the team prefers one rule for both, C41 could be made required with a single 3 lotuses / 4 heels / 6 strokes numeral; it is not done here because no book figure exists for it.
- **C45, C67, C71 questions** stay required although the LP text carries the counts (decision 4 of 23 Nov).
- **C61** is required although the LP steps already write 1000, 100000 and 3125 as numbers: the question asks for the answer in Egyptian numerals.
- **C40 and C47** are required although the LP steps describe the symbol counts in words (the answer is the picture).
- **C46 none.** A figure annotated with the place values (200, 70, 6 ...) would be possible, but it would only repeat the question figure.
- **C43 question none, C50 question required.** The first has no named figure although the symbols are needed to attempt it; the second names Table 2. This follows the "named table" rule of v3 B2 literally.
- **C48 none.** The teaching image of the concept (base-3 landmarks) shows what a picture could show; the answer is numbers only.

### Class 8 Ch 3, chunk C
- **C81 (two wedges, gap, five wedges) and C82 (Mayan numeral: two dots, three dots, one bar), both `optional`.** Both questions describe the numeral completely in words and the answer is a number (125 or 7205; 785), so the tie-breaker says text is enough. A picture of the numeral would clearly help and the book shows the same idea (ambiguity table p.26; Mayan numeral p.28), so I did not choose a plain `none`. Neither is added to the plan. If you want them drawn they are easy upgrades: C81 = two wedges, a wide gap, five wedges (3 over 2); C82 = three rows stacked: 2 dots (360s), 3 dots (20s), 1 bar (1s).
- **C75 required vs C77 / C76 none**, see above (answer is a drawing in C75 only).
- **C89**: only five vertical lines, but the printed answer is a picture and the rule says solution required; kept required under user decision 4.
- **C84**: required although the LP text carries "5 heng, a blank, 7 heng, 2 zong"; kept required under user decision 4.
- **C90** (4072 as digits in places): a filled place value row is `none` (LaTeX) by the HEADER_BOXES_ONLY / LATEX_TABLE rule, even though a teaching image shows it.

### Class 8 Ch 4, chunk A
- **C7 (carpenter), C9 (60 degrees), C18, C20 questions: none.** The book's text points to a lesson figure for each ("as shown in Fig. 1", "as shown in the figure to the right", "Join BD", the plain rectangle of p.9) but the LP question is self-contained and the picture would either give away step 1 (C7, C18) or only repeat the words (C9, C20). If the content team wants a question picture for these, the figures to use are book Fig. 1 / Fig. 2 (C7), the p.4 figure with 60 degrees marked (C9), the p.8 rectangle with four right-angle marks (C18), the p.9 rectangle (C20).
- **C3 and C5 worked examples: required.** Each question picture is simple (rectangle with O and 8 cm; two diagonals with 40 degrees); required because the steps refer to triangles and angles at O that the learner must see.
- **C24/C25 solution: required.** The counterexample is a drawing but the book prints no picture for it (its text answer is only "No").
- **C32 question required, C33 solution none.** The LP text carries all four size pairs, but the book question is "in the quadrilaterals below"; the solution would only add the words rectangle and square.
- **C34/C35, C40/C41 solutions: required** although C34 has no printed picture (construction answers).
- **C37 marks only the two angles asked** (DAC, DCA), not all four halves of the right angles.

### Class 8 Ch 4, chunk B
- **C57, C59, C73 questions (none)**: the book shows the parallelogram/rhombus beside the deduction, but the LP question names the shape and gives all data in the text and refers to no figure. If you want a question figure for these, the specs would be: parallelogram ABCD with angle A = 30 (C57); parallelogram ABCD with AB = 4 cm and AD = 5 cm (C59); rhombus ABCD with angle A = 50 (C73).
- **C57, C59, C73 solutions (required)**: could be argued `optional` because the answers are numbers; kept required because the book's own answer is the filled figure and the steps rely on it.
- **M4.S15.T15.C63 and M4.S17.T17.C69 worked examples (optional, not added)**: the figure (parallelogram EASY with diagonals AY, ES at O, 10 cm and 6 cm; rhombus GAME with diagonals GM, EA at O, 8 cm and 6 cm) would clearly help, but the question names every point and length and exactly this figure is the concept's own teaching image (C63.IMG1, C69.IMG1), which stays. Flip to required if you want a drawn copy; the spec would copy that figure with the lengths and no answer halves.
- **M3.S11.T11.C44 worked example (none)**: three numbers, no figure, arithmetic working.
- **C75 question (required)**: the LP text carries every number, but the book gives the four figures with the question and the arrow/tick marks carry meaning (decision 4: kept required).
- **C48 solution (none)**: 360 - 270 = 90 needs no picture; a rectangle would only repeat the sentence.
- **C49 question**: the reflex arc at D and the shape come only from the figure; the LP text adds "one corner that caves in".

### Class 8 Ch 4, chunk C
- **C93 question required, C103 optional.** Both are proofs about a quadrilateral with diagonals meeting at O. C93 is required because the book itself prints the figure ("In the kite, show that the diagonal BD ...", ticks give the equal sides); C103 is an LP-written example with no book figure and the text names every point, so it is optional (figure that would help: ABCD with the diagonals crossing at O at a right angle, OA = OC and OB = OD marked). If the content team wants proofs drawn regardless of a book figure, C103 would be the quadrilateral with those marks (the same layout as D6, without shading).
- **C97, C98 required although the LP text carries all numbers** and the concepts have a teaching image of the same trapezium: the book gives the figure (page 25) and the angle relations (co-interior angles, equal base angles) are read off the figure; decision 4 applied.
- **C110 optional.** A fold puzzle whose question is complete in words; a picture of the quarter-folded sheet with the slanting crease would help, but the LP gives no numbers or positions to draw, and the opened sheet is already the teaching image.
- **C102 none.** The five family names of a square are a list of words; the teaching image already shows them.
- **C106 / C108 none.** Word reasoning; the book's printed answers have no figure. A rhombus with one right angle (C106) would be optional-grade at most.
- **C83, C85, C87 question none** although the book prints pictures of the activity (see judgement call 1).
- **C84 solution required** for an answer that is a name; kept because "join the ends" produces the figure the reasoning is about and the sibling activities (C86, C88) are required.
- **C94 solution required** although it adds marks to the question figure rather than a new figure (see judgement call 5).
- **C104 required** although concept image C104.IMG1 shows similar family rings; v3 never links a teaching image and the book's answer is a figure.
- **C88 density.** Six panels with 24 side labels in one card is the densest figure of the chunk; the bounding boxes of all labels were checked for overlap in a preview, none overlaps an outline.

### Class 8 Ch 5, chunk A
- **M1.S3.T3.C8 solution (the eight signed expressions): none.** A completed sign tree with all eight results next to its leaves
  would be a faithful answer picture (the book says "You can use the diagram below to systematically list all the possibilities
  ... write the result next to it"). I kept it as LaTeX arithmetic because the answer is a list of eight sums and the tree is
  already the teaching image `M1.S2.T2.C3.IMG1`. If you want it drawn, it is a `number_pattern` tree: 3, two 4s, four 5s, eight 6s,
  leaves = the eight expressions with values 18, 6, 8, -4, 10, -2, 0, -12 (tree order +++, ++-, +-+, +--, -++, -+-, --+, ---).
- **M1.S6.T6.C19 and C21 solutions: none.** Could be the eight cards with the four even ones in ANSWER green; judged not needed
  (the answer is a verdict with a parity reason, not a drawing).
- **M1.S7.T7.C22 worked example: none.** Six dot arrays in rows of four (4, 12, 36 fill rows; 18, 22, 42 leave 2 over) would help
  but duplicate teaching image `M1.S7.T7.C22.IMG1`.
- **M1.S8.T8.C25 question: required** is itself the closest call of the chunk (the algebra alone is enough to attempt the task);
  I followed the book's own wording "and the visualisation" and decision 4 (no flipping to none because the LP text has the algebra).

### Class 8 Ch 5, chunk B
1. **M1.S12.T12.C45 (Q16 solution) - required.** The book's printed answer is only "Ans. (iv)", and (iv) is already one panel of the question figure, so a plain copy of panel (iv) would be `SAME_AS_QUESTION_DIAGRAM` (none). I chose `required` (`ANSWER_IS_FIGURE`, the answer IS a Venn picture, B2) and made the figure add something: panel (iv) alone at 1.9x with the three example numbers that LP step 3 uses placed in their regions (4 in the outer set only, 8 in the middle ring, 32 in the innermost set), in ANSWER green. If the reviewer reads the rule strictly, the alternative is `none` / `SAME_AS_QUESTION_DIAGRAM` for this one item. The old LP author's hint (`s_figure`) also said "Diagram (iv) alone". `derived_from` = the question figure; note the solution is one panel of it, not the 2 x 2 layout.
2. **M1.S15.T15.C59 (Q7 solution) - required, and the question C58 - none.** The question says "Show the solution both algebraically and visually", the book's printed answer gives only the algebra and "For visual method refer P. 120 of the textbook", and LP step 4 describes the visual in words ("rows of 7 dots with 5 and 3 dots left over; the leftovers join to make a full row and 1 more, or 5 minus 3 leaves 2"). A word description of a dot picture does not replace the picture (B2, `ANSWER_IS_FIGURE`). The question side gives all its data in words and the book prints no figure with it, so no question figure (rule: no question figure when the question gives none). This is not the 'refer picture' case of B2: the question's data is not in a picture, and the picture the answer points to (7-wide dot rows for 7k, pdf page 9 / book p.120, base figures P09-dot_array-4/5) does not show remainders, so the solution draws its own figure (`derived_from` null).
3. **Worked examples C47 and C48 - none** although the book's What Remains? section has dot pictures and each concept already has a teaching image. The worked examples are plain remainder arithmetic and a short list of numbers; nothing asks the student to use a figure, and a teaching image is never linked. Tie-breaker: a careful student solves them exactly as well from the text. Same reasoning for C68 and C69 (place-value sums).
4. **Possible but not added:** C55 (pebbles, a number line of 31, 61, 91 with a divisible-by-7 check), C65 (the 12-periodic triples 2-3-4, 14-15-16), C67 (a table of remainder triples) and C51 (value table of 5k + 3 and 5k - 2) could each be drawn, but all of them are plain tables or number lists that the text carries (`LATEX_TABLE` / `TEXT_SUFFICIENT`). I gave C51 and C67 an optional LaTeX array in `text_alternative`.
5. **Venn colours.** The book tints the options differently (for example (i) blue, yellow, green but (iii) and (iv) in other greens/blues). The spec colours by set (4 = SET_A, 8 = SET_B, 32 = MARK_FILL) in every panel, so a colour always means the same set. Geometry, order of nesting and arrow targets are as printed.
6. **Figure letters.** Roman numerals (i) to (iv) are drawn in the Q16 question figure and (iv) in the solution figure because the LP answer says "Diagram (iv)" (decision 3). In the Q7 figure the panels are marked (i) and (ii) because LP steps 2 and 3 use "(i):" and "(ii):".

### Class 8 Ch 5, chunk C
**Borderline (v3 rules applied as written, user decision 4)**

1. **M2.S24.T24.C106 (worked example, the 10 x 9 Yes/No divisibility table): REQUIRED, the only diagram of the chunk.**
   - Why drawn: the book's printed answer to this question is the completed table (P29-table-1, "printed answer picture"), and the question gives a table to complete (P18-table-2). Step B2 says a printed answer that is a picture overrides text-first, and ANSWER_IS_FIGURE names a "filled table". The LP can only give the answer as ten lines of nine Yes/No words, where the column of each answer is lost.
   - Against: Step C `LATEX_TABLE` (plain table, no colour meaning) and the prompt's example of a fill-in count table that stays LaTeX. That example is a 5-entry table; this one has 90 position-dependent cells.
   - The single worked-example diagram shows the finished table (128 row corrected, see section 3). media_id `M2.S24.T24.C106.IMG2` (IMG1 is the kept teaching image of the concept; the build renumbers).
   - If the team prefers LaTeX: change this item to `none` / `LATEX_TABLE` and write the table as a LaTeX array with header "Number | Divisible by 2 3 4 5 6 8 9 10 11". Nothing else in the map depends on it, except that P18-table-2 and P29-table-1 would then become `none:LATEX_TABLE`.
2. **M2.S19.T19.C79 (solution of "remainders of 427 and 7309"): OPTIONAL, not added.** The book prints tile pictures for both answers (P13-tile_model-2/3 for 427, P14-tile_model-2 for 7309). The answer is a pair of numbers, the LP gives four complete equation steps, and teaching images C74.IMG1, C75.IMG1, C77.IMG1 already carry the model. The tie-breaker says a careful student loses nothing, so it is not required; it is optional (not `none`) because the book does print a picture for exactly this explanation. If the team wants it drawn, it needs ONE solution diagram, and the 427 and 7309 pictures would have to be combined or one of them dropped (a solution has at most one). The question side C78 stays `none`: the question gives only the two numbers.
3. **M2.S21.T21.C95 (worked example, 320185 excess and shortfall): OPTIONAL, not added.** The book's three pictures (P17-dot_model-1/2/3) colour digits 2, 1, 5 green and 3, 0, 8 red and end with 8 green circles over 11 red ones. This is the Step D case "grouping by colour for a sum already written", and the LP steps name every place and sum. Teaching image C95.IMG1 stays. If the team promotes it to required, draw the corrected labels (section 3, point 2).
4. **Number-line ideas, kept `none`**: C87 (closest multiple of 9 to 6000: marks 5994, 6000, 6003 with distances 6 and 3) and C89 (4302 to 4392 in steps of 9) would only make the answers nicer; the printed answers are plain numbers (6003, 11).
5. **C110 (prime factorisations of 12 and 24, LCM 12 and 24)**: word reasoning in products; teaching image C105.IMG1 draws the factor tiles. `none`. The book prints no picture.

**Sibling consistency**
- All Figure it Out items of this chunk (C84 to C93, C102/C103) and the in-text question pairs without a printed picture (C80/81, C98/99, C100/101, C107/108, C109/110) are `none` on both sides: a number or a word reasoning, no figure given, no figure printed in the answer.
- Optional (not none) only where the book prints a picture for that item's own explanation: C79 and C95. C99 (462) has no printed picture for its answer, so it is `none`.

**Figure accounting (14 base figures, all claimed)**
- Teaching pictures are accounted to the teaching image that shows the same idea (accounting only, nothing is linked): P13-tile_model-2 and P14-tile_model-1 to C74.IMG1; P13-tile_model-3 to C77.IMG1; P14-tile_model-2 to C75.IMG1; P16-table-1 to C94.IMG1; P17-table-1 and P17-dot_model-1/2/3 to C95.IMG1; P18-table-1 to C96.IMG1. The match is by idea, not pixel for pixel (P14-tile_model-1 also shows 999 and 9999, P16-table-1 also shows tens and thousands).
- P13-tile_model-1 (two blue 99|1 and three green 9|1 tile pairs, no labels): `none:TEXT_SUFFICIENT`. Its meaning is not stated in the book (the text beside it only says 99 is divisible by 9 and 109 is not) and it does not draw 99 or 109, so I did not map it to a teaching image.
- P14-annotated_equation-3 (equation chain with two underlines): `none:LATEX_ARITHMETIC`.
- P18-table-2 and P29-table-1 both map to `item:M2.S24.T24.C106 (question)`, the one worked-example item (the validator's candidate list for a worked item uses the role `question`).
- P19-illustration-1 (Digital Roots club cartoon) is on page 19 but belongs to the Digital Roots topic (M2.S27.T27), not to my chunk; I did not claim it.

### Class 8 Ch 5, chunk D
1. **C139 / C140** (addition cryptarithms in the book's column layout): none, but a reviewer could argue ANSWER_IS_FIGURE (a solved column addition). I applied the v3 rule as written (column addition is LaTeX). If the user wants pictures here, it is four question figures (one per puzzle) plus solved columns, which also would hit C148.
2. **C148** (six solved multiplications): none, same reasoning.
3. **C152 Navakankari worked example:** `optional` rather than `none`. A small picture (three connected board points on one line, two partner pawns on the first two, the third empty, my blocking pawn in ANSWER green) would clearly help, but the scenario is stated fully in words and the answer is one move, so by the tie-breaker the text is enough. Not added.
4. **C129 solution:** the printed answer looks like a two-column table (see above); judged text.
5. **C117, C119, C122/C123, C125, C127:** a teaching picture exists for each concept, which is never linked. Their decision does not rest on that; each is text/LaTeX because the content is plain numbers.

### Class 8 Ch 6, chunk A
1. **M2.S9.T9.C38 solution (Evaluate 94 x 11 ... 4791256 x 11): optional, not added.** The book answer page 26 prints a hand-style carry layout for part (ii) only ("Try other parts"): digits 4 9 5, two arcs, two circled carry 1s, "x 1 1", a rule, "(4 + 1) 4 4 5", "= 5445", notes "5 + 9 = 14", "9 + 4 = 13 + 1 = 14". Rule B2 says a printed picture answer is `required`; Step C names column arithmetic as LaTeX. I treated it as an arithmetic carry layout (the base inventory also says "LaTeX-able") and chose optional because: the LP steps state every sum and carry of all four parts, teaching images C31 and C34 show the same one-line picture, and one picture would cover only one of four sub-answers. If you want it drawn, it becomes a `required` solution (no question diagram, `derived_from` null) of one layout: INK digits 4 9 5, FOCUS arcs 4-9 and 9-5, circled 1s, ANSWER row (4 + 1) 4 4 5 and "5445". Decision for you.
2. **M2.S4.T4.C12 worked example ("use the four parts"): none.** The four-part rectangle is already the kept teaching image M2.S4.T4.C12.IMG1 of this same concept (book p.4 dot array), the four parts ab, mb, an, mn are named in the steps and every number is in the words. No v3 trigger applies; a new drawing would repeat the teaching image. If you prefer a drawing, spec it as 25 x 32 split into 23 x 27 = 621, 23 x 5 = 115, 2 x 27 = 54, 2 x 5 = 10.
3. **M2.S3.T3.C11 solution: required although the printed answer looks like a plain table.** The nine expressions could be a LaTeX array (LATEX_TABLE), but they complete the empty frame of the question figure, which is `ANSWER_IS_FIGURE` / `ACTION_ON_FIGURE`.
4. **M2.S3.T3.C6/C7 and M2.S5.T5.C17/C18: none.** An area-model rectangle (23 by 27 plus one column; 10 by 10 with a 3 by 4 corner removed twice) would help, but the data is all in words, no printed figure belongs to these questions and teaching images (M2.S2.T2.C2-C3, M2.S4.T4.C13) already show it.
5. **P26-column_addition-1 mapped to concept image C34** (same layout, other number) rather than to an item, because C38's solution is not required.

### Class 8 Ch 6, chunk B
1. **C47 question and C58 question: optional, not none, not required.** The text carries every number (the splits 60 + 5, 30 + 35; the squares 55 and 60), so a careful student can attempt both without a picture (tie-breaker: it only makes it nicer). The book figures on p.10 and p.11 also carry the part labels (60^2, 60 x 5, ... and -60 x 5, +5 x 5), which are the explanation, i.e. the solution. If the content team wants the question to show a picture anyway, the question figure would be: C47 = the 60 + 5 square with side lengths 60, 5 only; C58 = a 60 square with a 55 square in the corner, labels 60, 55, 5 only (no area labels). Then both solution diagrams could be marked `derived_from` those. I did not add them.
2. **C58 solution drawn although its twin question has no figure.** The book argues 55^2 only geometrically, so the answer is the picture (strips removed twice, corner added back once). Sibling check: the other answers of T13 (99^2/58^2, expansions) are plain evaluations, so they stay `none`, with a "Sibling note" in the reason.
3. **C50, C54 (104^2, 37^2 and (3j + 2k)^2) none although teaching images C46 and C45 draw the same squares.** The questions only ask to expand or evaluate and the book prints no figure for them; a teaching image is never linked.
4. **C64 and C66 worked examples (T14) none.** C64 has a teaching image of two 5 by 5 and two 6 by 6 squares, but that figure is not in the book; the worked example is a numeric check plus a general expansion. C66 is pure arithmetic.
5. **C81 / C82 (the 12 cards) none.** The cards are boxed equations; they match the "Not a diagram" family (list in boxes, equations). The only thing lost is the working lines of the cards, which is an LP text issue (below), not a figure issue.
6. **C73 (Express 100 as a difference of two squares) none, `LATEX_TABLE`.** The book's printed answer is a plain trial table of numbers; the LP solution uses the factor method (50 x 2) instead, and the LP text wins.
7. **Shape of the C48 figure: one card with two squares** (not two images), because the question gives one answer and the brief allows one solution diagram per pair. Strips of the 60 + 5 square are drawn 0.7 of 6.0 (true ratio would be 0.46); `to_scale` is false, as in the book.
8. **C59 figure: dashed full-length rectangles.** The book draws the strips 55 long with a separate darker corner but labels them "60 x 5" and "5 x 60". My spec draws the same cells and adds two dashed FOCUS rectangles of the full 5 by 60 length so that the labelled 300 is visibly 60 long and the overlap is the 5 by 5 corner.
9. **Callout wording uses no minus or plus signs** (book prints -60 x 5, -5 x 60, +5 x 5): the LP solution text carries the removal and the add-back in words, and a sign on a callout next to a positive area would read wrongly. Change if the team wants the book's signs.

### Class 8 Ch 6, chunk C
- C106 Tadang question `required`: the LP text is algebra only ("Show that ... are equal") and could be done without the figure, but the book question is "find the area of the shaded region in the figure" and the meaning of m, n and both expressions lives in the picture. Same reasoning for C108 (slanted region). If the team prefers text-only for these two, set both to none.
- C104 tiles question `required` although the LP text gives the counts 8, 12, 16 (the arithmetic pattern alone would give 4n + 4). The book question is figure-based and its point is the several methods of seeing the frame.
- C87 calendar question `required` although a calendar is a table of numbers: kept because the 2 by 2 outline carries meaning (HIGHLIGHT_MEANING) and calendars are listed under cell_grid in the catalogue.
- C107 Tadang solution `none` (SAME_AS_QUESTION_DIAGRAM) but C109 slanted solution `required`. Reason: the book prints no further picture for Tadang/Yusuf (one figure serves both methods), whereas for the slanted region it prints three extra sketches (printed answer is a picture, B2). The LP solution of C107 is pure algebra; a figure with m + n and n - m marked would be an optional enhancement (stated in `text_alternative`). The two items look alike in the LP text, so this is the call most worth confirming.
- C105 tiles solution and C103 circles solution `required` although the book prints no solution picture for tiles (a plain table P29-table-1, mapped `LATEX_TABLE`) and none at all in the answers section for circles: the LP solutions describe groupings of the figure that a student cannot see from the words alone.
- C117 park solution `required`: the 2w of the printed solution is the classic trap and the marks on the plan are the answer to "where does 2w come from".
- C119 solution repeats Steps 1 to 3 at a smaller scale next to the new Step 4 (so the card is `derived_from` the question figure). Showing only Step 4 would also satisfy the printed answer; chosen so the sequence is visible.

### Class 8 Ch 7, chunk A
- **M1.S3.T3.C8** solution `optional`: a colour-coded pairs picture would help, but the LP text does not state the pairs.
- **M1.S4.T4.C12** solution `required`: a sample drawing of an open-ended 'draw a figure' answer; arms and legs labels come from LP numbers (60 and 80 cm x 1/10) that the text does not spell out.
- **M2.S8.T8.C26** question `required` even though the LP text carries the counts (decision 4); **C27** solution `required` for the block outlines (the picture changes how clearly the counted bricks can be seen).
- **M1.S4.T4.C10** solution `required` and **C9** question `required`; the 3:2 shape against the book's 5:3 (see section 1).
- **Worked examples C2, C13, C16** `none`: a figure would help but a careful learner loses nothing without it and concept images exist.
- **C20/C21** `none` (`LATEX_TABLE`) although the printed answer is a filled table.
- **M2.S10.T10.C39** solution `optional`: book's arrow picture for the first blank only.
- **C24/C25** `none` ('circle' is an action on text, not on a figure).
- Sibling check: Q4 solution (procedure, optional) against Q5 and Q7 solutions (a drawing, required) differ because the answers differ in kind: Q4 names letters, Q5 and Q7 end in a drawing.

### Class 8 Ch 7, chunk B
- `M3.S16.T16.C61` solution (mason): required because it adds five labels the question figure lacks; it would be `none` (SAME_AS_QUESTION_DIAGRAM) if only the picture were repeated.
- `M2.S11.T11.C43` solution (Example 5): required because the answer is a drawing; a reader could say a student can draw it from the sizes given in text. Kept required under the rule as written.
- `M3.S13.T13.C49` worked example: none; a crossing-arrows picture of ad = bc could help, but it already exists as a teaching image and the rule forbids linking it.
- FiO1 Q2 and Q3, Examples 4, 8, 9, 6: none by the Step C tests (word or arithmetic only).

### Class 8 Ch 7, chunk C
- **`M5.S31.T31.C120` Binairo worked example, required.** Against: the question describes the row completely in words and the LP answer "H H V H V V" is a text string, so a careful student could solve it from the text alone (tie-breaker). For: the answer is an arrangement of drawn horizontal and vertical bars, rule B2 says an arrangement answer is drawn even when the steps describe it in words, and the steps point at cells by number. I kept it `required` (user decision 4, rules as written). The teaching image C120.IMG1 shows nearly the same row but is kept and never linked, and the id is `C120.IMG2` because IMG1 is kept.
  - Which state the single diagram shows: I drew the **complete final row** (given cells 1, 2, 5 in INK with a dashed FOCUS outline as in the book's solved example, found cells 3, 4, 6 in ANSWER green), because the worked-example figure sits before the steps and the answer is the arrangement. The alternative is the given state only (cells 3, 4, 6 blank), which would not draw the arrangement answer. If the user prefers the given-state row, change the three found cells to blank and drop the ANSWER colour; the id and placement stay the same.
- **`M4.S25.T25.C93` solution, optional rather than none.** The book does draw the method for this very activity (P15, P16), so the figure "would help"; but the steps carry all numbers and the answer is not an arrangement, so it is not required. Nothing is added either way.
- **`M3.S21.T21.C82`, none.** A bar or card picture of price per mL would be pleasant, but the book's figure is a plain table and the teaching image C82.IMG1 already shows the four sizes and the unit prices.
- **Sibling check (B2).** The five 7.5 Figure it Out items (C94, C100, C102, C104, C106) and the Examples 11 and 12 (C96, C98) all have text/number answers and are all none, as is every 7.6 Figure it Out item. No sibling is drawn.
- **P20 Binairo mapping.** Both book example grids (Puzzle and Solution) are mapped to the one worked item because its row is the one-row version of that example. The practice grids are mapped to none:OPEN_ENDED only because no LP item uses them (no code says "no LP item"); see LP text issues.

### Class 8 Ch 8, chunk A
- **M1.S3.T3.C9 (Example 1 solution) = none (SAME_AS_QUESTION_DIAGRAM + TEXT_SUFFICIENT).** One could argue for a solution figure that brackets the yellow quarter as 25%. The book picture already shows the yellow last quarter against the 25/50/75/100 scale, the answer is a number, and v3 Step E says "figure-based question, numeric answer: Q required, S none". If the reviewer wants it, the spec would be C8.IMG1 plus a bracket under the yellow part labelled 25% in ANSWER, derived_from M1.S3.T3.C8.IMG1.
- **M1.S4.T4.C21 (Q4 solution) = required.** The LP answer text carries every number, so a reviewer could call it none. I kept it required because the answer is a matching drawn on a given picture (ANSWER_IS_FIGURE) and the user's rule is not to flip a required item only because the LP text has the numbers.
- **M1.S1.T1.C1 block 3 (ratio 2 : 3)** is none. A bar of 5 parts would help, but the whole 2 + 3 = 5 is one line of words and the book gives no figure.
- **Diagnostics (C4, C24, C31, "Check my thinking")** are all none (text multiple choice, no book figure).

### Class 8 Ch 8, chunk B
1. C34 (Example 1, solution) - optional, not added. Figure that would help: the book's double scale on p.6 (0, 25%, 50%, 75%, 100% over 0, 30 g, 60 g, 90 g, 120 g, Sugar bar to 25%). Why not required: the LP steps are 25% of 120 and 35% of 95 as arithmetic, and the teaching image M2.S5.T5.C24.IMG1 shows the two biscuit bars. Tie-breaker: a careful student solves it from the text alone.
2. C42 (Example 3, solution) - optional, not added. Figure: the book's 0 to 75 marks over 0 to 1.0 scale with the band to 60 shaded. LP solution is "80% of 75 by fraction, decimal or proportion": one line of arithmetic.
3. C44 (Example 4, solution) - optional, not added. Figure: the ratio bar 2 | 7 with whole 9. The LP steps say "The whole is 9 parts" and the sum 2 + 7 = 9 is trivial; teaching image M2.S5.T5.C30.IMG1 already shows this bar. Closest call of the five: the word "parts" points at a picture. If the user wants it, the figure is the nine-cell bar, 2 cells millet, 7 cells water, drawn to scale (the book draws it off scale, see below).
4. C46 (Example 5, solution) - optional, not added. Figure: the Delhi to Agra bar cut into five 20% pieces (92 km on two, 138 km on three, 230 km whole). The LP steps say "one 20% piece, then the remaining three pieces", which is also a picture-flavoured wording. Teaching image M2.S5.T5.C31.IMG1 shows the same bar.
5. C48 (Example 6, days 1 to 4, solution) - optional, not added. Figure: four bars on a 0 to 5000 / 0% to 100% scale (2000, 3500, 5000, 6000; the last runs 20% past the line). The LP steps give the one rule "sales over 5000, times 100". The book prints these four bars as its explanation and writes the percent under each; the answer is still four numbers.
6. C49 (Example 6, days 5 and 6, QUESTION) - optional, not added. This is the closest call in the chunk: the book prints the two bars with the question (inventory says "given in question"), so I looked hard at making it required. Every number in the figure (target 5000, sales 7800 and 9550) is also in the question words, and 2800 and 4550 are only differences, so the learner loses nothing without it (tie-breaker, Step C TEXT_SUFFICIENT). The same two bars are teaching image M2.S5.T5.C32.IMG1. It is not the Step B2 "refer picture" case (no printed answer), so the text must carry the data: see LP text issues, C49. If the user prefers the book's figure with the question, it is: scale 0 / 5000 / 10,000 over 0% / 100% / 200%, red outline 0 to 5000, green Day 5 to 7800 with arrow "2800", green Day 6 to 9550 with arrow "4550".
7. C50 (Example 6, days 5 and 6, solution) - none. With no question diagram, the solution would only add the labels 156% and 191% at the bar ends: that is the typical "figure question, numeric answer" pair (question figure, no answer picture).
8. Plain tables (C35/C36 free-hand table, C39/C40 FDP table, and the table half of C53/C54) - none, LATEX_TABLE. The book colours the cells blue, but colour carries no meaning, and the answer is the same grid filled with numbers. Sibling decision for all three tables. I gave the LaTeX layout in `text_alternative`.
9. C54 solution is required although the book prints no answer picture: the LP answer instructs the learner to mark all nine values, so the answer IS the marked band (B2). Question diagram = the band with the 90% arrow the book gives; the eight other arrows come only in the solution (ANSWER green), `derived_from` = C53.IMG1. Arrow labels are placed on two rows so 15% / 28.9% (55.6 px apart) and 90% / 110% (80 px apart) do not collide.
10. Base inventory: I added `NEW-P12-bar_model-1-sol` for the second use of the printed band (solution of C54), as the brief says for a figure used by two items. Figures P06, P09-2, P10, P11-5, P11-6 are mapped to the teaching images that show the same quantity (accounting only; if chunk A claims the same figures it should be as concept images, and the table figures P07, P08, P12-table as `none:LATEX_TABLE`).
11. Figure letters (user decision 3): none of my figures carries letters.

### Class 8 Ch 8, chunk C
- Q1 question: kept `required` although the LP question text carries every number (decision 4); the figure is the book's given figure and the learner fills its "?" marks.
- Q2 solution: `required` on the strength of "also draw their bar models"; the LP text alone would not need a figure.
- Q3 (3/4 of 60 ml), Q9 (20% takes 18 days), Q10 (10 : 80 : 10 of 90 minutes), Q12(ii) (40 : 40 : 20 of 2 kg) and the worked blocks Tomatoes and Footfall: a bar model would be natural, but the book draws nothing, the question gives no figure and the numbers are one-step arithmetic, so `none` (tie-breaker). If more pictures are wanted, Q10 and Q3 (solution side) are the first candidates, then the Tomatoes worked example.
- Q4: the book says "Visualising or estimating can help" but gives no figure and the answers are symbols: `none`.
- Q5(iv) and Q7 ("Create such questions", "Make 2 more") are partly open-ended; the closed parts decide, `none`.

### Class 8 Ch 8, chunk D
1. M3.S9.T9.C85 (Example 2 question, KYC table): `none`, LATEX_TABLE + DECORATIVE_ONLY, `needs_lp_text_sync: true`. The data lives only in the book picture, so this is the call most open to challenge. I judged the two labels as plain ingredient/weight lists (no colour, position or arrows carry meaning; the pouch, almonds, barcode and how-to-use strip are decoration), the same kind of thing as the number lists the audit removed, and the table to complete is a plain table like P07/P08/P12. If you want the labels drawn instead, the figure would be one 16:9 `other` diagram with two label cards (DEF and Zacni, ingredient names and grams, total weight line) plus the table with 66% in the DEF Sugar cell, and the solution a derived diagram with the other 7 cells in ANSWER green. Say so and I will write the spec.
2. M3.S9.T9.C86 (Example 2 solution): `none`. A filled percentage table is a numeric table (LATEX_TABLE), not ANSWER_IS_FIGURE. Consistent with the question side.
3. M3.S11.T11.C97 (Kishanlal's profit): `none`. Numbers are in the book text, answer is 430 - 300 = 130, and the sweater journey is this concept's own teaching image (never linked).
4. M3.S11.T11.C98 (crayon box, check my thinking): `none`. Multiple choice in words; the book draws nothing for it; the five-part ₹10 bar is the teaching image C98.IMG1.
5. M3.S11.T11.C102 (Manisha, 50% or 33.33%): `none`. The book draws two bars, but they are teaching figures (concept image C101.IMG1) and the example does not refer to them; the numbers are three simple fractions. An optional two-bar picture (₹250 over ₹500 = 50%, over ₹750 = 33.33%) would help but only repeats C101.IMG1, so I did not mark it optional.
6. M3.S10.T10 (all four pairs): `none` on both sides, consistent with each other (no figure in the book, solutions are one or two lines of arithmetic).

### Class 8 Ch 8, chunk E
1. C107 question: required vs optional ('refer picture' exception). Chose required (reasons above).
2. C106 and C114 solutions: required vs none/optional (the bar restates numbers the LP text carries). Chose required per v3 B2 (printed solution picture) and user decision 4.
3. **C116 (vase) solution: required although the book prints no figure.** The book says right after Example 6: "Try making an estimate. Draw a rough diagram depicting the given situation", then shows two methods ("keep 82%" / "subtract 18%"). The answer to that prompt is a drawing (ANSWER_IS_FIGURE) and Examples 4 and 5 directly above have the same kind of bar printed (sibling consistency), so the solution draws that rough bar: buying price 2650 = 100%, loss 18% = 477, selling price 82% = 2173. All numbers are on book p.18 or in the LP solution. If the user would rather draw only what the book prints, flip C116 to optional (action drop_image) and delete its diagram; nothing else depends on it. This is the only required item with no inventory figure behind it (hence the validator warning).
4. C112 / C118 optional (not added) while C116 is required: the difference is the book's explicit "draw a rough diagram" prompt for the vase.
5. C121 solution none vs optional (circle the CGST / SGST lines): chose none.

### Class 8 Ch 8, chunk F
- **C144 required vs LaTeX arrays.** The tables are plain numbers, so a LaTeX array would also work. I kept it as a figure because the printed answer IS this picture and the arrows (x 0.10, x 1.10) carry the idea of "interest grows because the base grows". If the content team prefers arrays, the item becomes `none` (LATEX_TABLE) and the two figures map to `none:LATEX_TABLE`.
- **C139 optional vs none.** The book's rough bar diagram (principal = 100%, interest 10%, amount = 110%) would help, but no Step-B trigger holds: the data is in the steps and answer, the question names no figure, and the figure is a teaching figure with no concept image in the plan. Marked optional (reason says which figure). If it is ever drawn: principal line 6000 (100%), 10% = 600, amount 6600 (110%), long arrow "Amount after 1 year" spanning from 0 to the right-hand line (see section 3).
- **Figure it Out Q3 (company, C127/C128), Q6 (election, C133/C134), Q8 (milkman, C137/C138):** a bar or table picture could help the reader but would only make it nicer; kept none.

### Class 8 Ch 8, chunk G
1. **M4.S18.T18.C177 (Peaceful Knights), required, worked example.**
   - Which picture: a worked example has ONE diagram (after the question text). The book's given figure is an empty board; I drew the board WITH the example's 8 knights placed (final state), because the whole content of the example is the arrangement and an empty board adds nothing a learner cannot picture from "chess board". The v3 solution-figure-first convention supports showing the finished state before the steps. If the user wants the strict "given figure only" reading, the alternative is the same board with no knights (visible_text becomes empty).
   - Board size: see "Book mistakes" below (8 x 8, not the book's 10 x 10).
   - The book's small 5 x 5 knight-move board (P32-chess_board-2) is not drawn: the move rule is written in the book text, so `none:TEXT_SUFFICIENT`. The LP question text does not carry that rule (see LP text issues), so if the LP text is not fixed, that picture is the one a learner would miss.
   - Dark squares are drawn GUIDE grey (the "unused" colour), knights as the glyph U+265E in ANSWER green on light squares. If the renderer cannot print U+265E, a filled ANSWER disc of the same size is the only acceptable fallback.
2. **Example 13 model bars (book p.27: x, 1.5x, 0.75x), items C173 blocks 0-3 and C174, all none.** The figure is a "worked example picture" in the base inventory, but the plan already shows it as teaching image C173.IMG1, so P27-bar_model-1 is mapped `concept_image:M4.S17.T17.C173.IMG1`. No Step-B trigger applies to (i), (ii), (iii), Arun or Surbhi's Twelve Thousand: the numbers (50% margin, 50% discount, 12,000) are in the words and the steps carry x * 1.5 * 0.5 = 0.75x. If the user prefers a diagram per worked example, (i) "No loss?" (C173 block 0) is the item to turn required (three bars x, 1.5x, 0.75x, widths 4 : 6 : 3 units).
3. **M4.S16.T16.C166 (Q7 solution), optional.** A line graph of Rs 1000 over years 0 to 10 (straight line to 2000 at year 10; curve passing 2000 between year 7 and year 8) would clearly help "linear versus exponential" but the LP text answer is complete and the book draws nothing; not added. No other Q1-Q9 solution got this because only Q7 contrasts the two growth types (Q1, Q2, Q5, Q6, Q8, Q9 are plain arithmetic; Q3 and Q4 are text).
4. **Cakely/Cakify (C172 block 0) and 20% or Rs 50 (C171 block 1), none** although teaching images (C172.IMG1 bars, C171.IMG1 graph) exist. Neither is a book figure for the item; the two bakery pictures in the book are shop illustrations (decorative) and the sale question has no picture. Teaching images stay untouched and are never linked.
5. **Q3 (observe anything interesting?), question none (OPEN_ENDED)** and solution none: two sentences comparing 24,000/24,200 and 24,000/24,310.13.
6. **Summary (C176) none.** The two Summary figures (P31-bar_model-1 40% strip, P31-line_diagram-1 principal lines) are recap pictures of the Summary text, mapped `none:TEXT_SUFFICIENT`; the unit's question ("what did we find first?") is a reflection and carries no figure.
7. **P26-comic-1 (Puzzle-Solvers club comic), none:DECORATIVE_ONLY.** It is a teaching comic whose numbers (80%, 100%, 678 members) the LP text does not quote and no item asks about; if the content team wants it in the lesson, that is a teaching image job, not a diagram item.

### Class 8 Ch 8, chunk H
1. **Q6 solution (C187): optional, not added.** The LP solution only counts squares (64 in all, E is half of a 4 x 4 square = 8). A copy of the question grid with E shaded would help the counting step, but nothing new is drawn and the question figure already names E. I followed Step E ("figure-based question, numeric answer: Q required, S none or optional if the solution splits the shape"). If the user wants a solution picture, it is `derived_from` C186.IMG1: same grid, E filled MARK_FILL, the 64 unit squares faintly drawn in GUIDE.
2. **Q2 solution (C179): optional, not added.** Answer is a matching (arrangement of pairs). The v3 note on NUMBER_LIST_IN_BOXES says the arrows only become a diagram on the solution side and only optional when the written answer already gives it; the LP answer lists all four matches. Also the USA (about 4.2%) has no card to join to, so a drawn matching would leave one country unmatched.
3. **Q2 question (C178): none** although the book has a picture. It is two rows of plain cards with no joining line (a list of boxed values to choose from), and the LP question text lists every card in order.
4. **Q8 solution (C191): optional, not added.** The book's hint says "Drawing a rough diagram can help", but the book draws none and the LP solution is two multiplications (0.6 x 0.4, then x 160). A bar model (100% split 40% / 60%, 60% of the 40% marked = 24%) would be the picture. No question diagram, because the question gives no figure.
5. **Q12 question (C198): required** although the LP bracket "(Label: Potato 70%, ...; net quantity 65 g)" already carries every number. Kept required under decision 4: in the book the data lives only in the picture ("shown in the picture"). Only the label data is drawn (a plain table plus 'Approximate Values' and 'NET QTY: 65 g'); the packet art, plate of chips, barcode and 'Potato Chips' brand text are left out as decoration.
   - I left out the label's own heading 'Nutritional Information' because the brief forbids headings in a picture. It is a one-line change in the spec (add it above the table) if the user wants the label complete.
6. **Q15 question (C204): required** for the same reason (graph reading, LP bracket repeats the values). The chart title, subtitle, source line and 'Data For India' emblem are not drawn (headings/branding rule); the chart's title words survive only as the horizontal axis title 'Ability to use computer (2023)', because without some axis meaning the percentages are unlabelled. Colours: book teal and amber replaced by SET_A and SET_B.
7. **Q15 Male Children bar.** The book prints no number on it (bar measured at about 4.8); LP text says about 5%. Drawn to exactly the 5% gridline and left unlabelled, as in the book. Other bars are drawn at the PRINTED labels; in the book the bars differ from their labels by up to half a unit (Twenties Male ends near 36.5 under "37%", Seniors Female near 1.5 under "2%", Fifties Female near 3.7 under "4%"), which looks like rounding in the original NSS chart. No statement (i) to (vi) depends on this.
8. **Q15 solution (C205): none (SAME_AS_QUESTION_DIAGRAM).** Each statement looks at a different group, so no single complete final picture exists that the question graph does not already show.
9. **Q5, Q11 (and Q9) solutions: none.** A bar model or a before/after rectangle would only make them nicer; the questions give no figure and the working is a single product or algebra line. I did not mark them optional because, unlike Q8, the book does not suggest a diagram.

### Class 8 Ch 9, chunk A
- **M2.S5.T5.C27 (Q1 question) required.** The LP text already says "equal sides are 1 unit", so the tie-breaker alone would give none. Kept required because the book question gives this triangle with the lengths marked on its sides (DATA_IN_FIGURE, SPATIAL_GEOMETRY) and decision 4 says not to flip for the numbers being in the text. If flipped, C28 loses its `derived_from` (it would stand alone), nothing else changes.
- **M1.S2.T2.C4** required although the answer is one short phrase (see above).
- **C5, C8, C9, C10** required because the questions point at "the dotted square", "these small triangles", "the smaller inside square" without any other description; a reviewer who wants fewer pictures could treat C9 as the first to drop (same picture as C5).
- **C3, C12, C30** none although a small picture could help (2x2 copies, folded square, nested squares of area 1, 2, 4).
- **C16, C18** examples stay none although the General Solution figure (C14) exists; they are numeric.

### Class 8 Ch 9, chunk B
- **M3.S7.T7.C48 solution (required).** The answer is a geometric argument rather than a literal drawing. The question says "Can you see why", the argument is about the diagonal and the square on it, and the LP carries an `s_figure` hint. I kept it required (SPATIAL_GEOMETRY, HIGHLIGHT_MEANING); the alternative is none.
- **M3.S6.T6.C43 (required).** The diagram repeats the teaching image C43.IMG1. Kept because the answer is an arrangement and v3 never links a teaching image. Alternative: optional or none.
- **M3.S6.T6.C41 (required).** Same pieces as concept image C40.IMG2; required because the steps cite the lettered pieces.
- **M3.S8.T8.C53 (none).** The book prints a 3 cm, 4 cm, "?" triangle next to the text, but the text already gives 3 cm and 4 cm and says "draw it"; text sufficient. Alternative: required (given picture).
- **M3.S8.T8.C55 blocks 5 to 9 (required).** The LP text carries the numbers, but the book gives them only in the pictures; kept required as decided (not flipped because the text carries the numbers).
- **M3.S8.T8.C55 block 0 (none)** (draw it yourself) and **blocks 1 to 4 (none)** (pairs of numbers). **M3.S8.T8.C54 block 1 (optional)**: the turned triangle is the one example of the four where a figure clearly helps; kept out of the plan as optional.
- **M3.S6.T6.C39 (none)**: a picture of squares 9, 16, 25 on the 3-4-5 triangle would be nice; teaching image C39.IMG1 shows the arrangement.
- **T7 questions (none)** although all three solutions are drawn: the book gives no figure with these questions, so no question figure is invented.

### Class 8 Ch 9, chunk C
1. **C60 question (Chapter Exercises Q2 (a)) - required although the LP text carries 7 and 9.** The book gives a drawing (right angle marked, two labels, the third side blank); "in the following right triangles" refers to it. Kept required (FIG_REFERENCED, DATA_IN_FIGURE, SPATIAL_GEOMETRY). The figure follows the book: no "?" on the third side.
2. **C61 solution - none with SAME_AS_QUESTION_DIAGRAM.** The only addition would be the label sqrt(130) on the hypotenuse. Step E "typical pairs" (figure-based question, numeric answer: Q required, S none) and the tie-breaker (a careful student follows the text equally well) give none. It could be argued as required (value filled in on the figure). **Cross-chunk consistency:** parts (b)-(f) of the same question sit in chunk B (`M3.S8.T8.C55` blocks 5-9); their solutions should get the same decision as C61. If the merge reviewer wants the answer written on every triangle, C61 flips to required with `derived_from` = `M3.S9.T9.C60.IMG1` and the label `sqrt(130)` at about (4.244, 5.024) in ANSWER green (the coordinates are in the C60 spec).
3. **C57 solution (Figure it Out Q2, 8 cm side and 17 cm hypotenuse) - required.** The question has no figure but tells the student to draw the triangle and measure, and solution step 1 is that construction (side 8, right angle at one end, arc 17 from the other end, third side about 15). The figure draws the finished construction (arc in GUIDE, 15 cm in ANSWER green), `derived_from` null because the question has no figure. Reason codes SPATIAL_GEOMETRY + ANSWER_IS_FIGURE. Argument for none: the final answer is a number and the drawing is the student's own work. Chose required because Step B2 says a construction described in words still gets its picture. **Cross-chunk consistency:** Figure it Out Q1 (5 cm and 12 cm, "first draw the right-angled triangle ... and measure") sits in chunk B (`M3.S8.T8.C55` block 0); if its LP solution also describes a drawing, the same decision should apply.
4. **C88 solution (Chapter Exercises Q6, rectangles with integer diagonals) - optional, not added.** A rectangle with one diagonal (sides a, b, diagonal c) would help step 1, but the answer is a list of five triples carried by text and LaTeX.
5. **C73 (why (n - 1)^2 + (2n - 1) = n^2) - none.** The L-shape picture already exists as the teaching image `M3.S10.T10.C73.IMG1` (kept, never linked). The book itself shows only equations here, so no figure is invented.
6. **C65 (pattern among (3,4,5), (6,8,10), ...) and C70 (scaled versions) - none.** Plain lists of numbers; a LaTeX array does the job (LATEX_TABLE for C70). `text_alternative` says what to write.
7. **Q4 (i) pair (C58/C59) - none/none.** The question is symbolic (a = 5, b = 7), no figure in the book, the solution is arithmetic and two decimal bounds.

### Class 8 Ch 9, chunk D
- **C93 lotus question, required.** All numbers are in the text, so a "text sufficient" reading is possible. Kept required because the book prints the picture with the problem and the figure decides how easily the right triangle is found.
- **C92 Q8 (ii), none.** The book prints the grid beside both (i) and (ii). I treat (ii) as needing no picture (the answer is a list of numbers) and draw the grid once, for (i). If the user wants one grid per part ("same book picture, one diagram per item"), C92 would become a required worked example with the same spec as C97 (a 5 by 5 dot grid, "same as M4.S15.T15.C97.IMG1").
- **C96 rhombus and C100 equilateral solutions, required** although their answers are numbers: required on the strength of the spatial structure the solution describes (SPATIAL_GEOMETRY). A text-only reading would be defensible.
- **C94 lotus solution, required** although it also repeats the question picture: kept because it adds the right angle, the triangle, x + 1 and x = 4 (the complete final state).
- **C103 Find the Colours, none.** A picture of three labelled boxes could help, but the puzzle is word reasoning and the book prints no figure. `text_alternative` gives a LaTeX table of the two cases.
- **C101 summary matching, none.**

### Class 8 Ch 10, chunk A
- **M1.S2.T2.C2 block 0 (idli, P01 cross-multiplication arcs): none** (TEXT_SUFFICIENT). The arcs only show which pairs are multiplied (6 with 2, 3 with 4) and the LP steps write both products. Could be optional ("makes the cross visible"); either way no image is added. The figure is a teaching figure that is not among the plan's 11 concept images.
- **M1.S2.T2.C4 (Map Making Activity, 1 : 50): none** (OPEN_ENDED). A 16 cm by 12 cm rectangle with a 3 cm desk would only make it nicer; object positions are not given.
- **M1.S2.T2.C3 (what RF 1 : 60,00,000 means): none.** The concept image C3.IMG1 already shows map distance, road and scale bar; the printed map is used only by the distance question.
- **M2.S8.T8.C32 optional vs none vs required:** see above; a reason-only answer, not a drawing.
- **C6 map: required vs none (NOT_RENDERABLE):** see above.

### Class 8 Ch 10, chunk B
- **C33 worked: none vs optional/required.** The text points at "the pie chart" (a figure reference), but nothing is lost without it. If you want the book's grade pie chart on this block, it would be the 5-slice chart with counts 12, 10, 8, 6, 4 and no angles (book p.60).
- **C47 solution: required although it adds one label.** The only addition to the question figure is the Car slice mark 30 degrees (v3 "new marks"). The alternative is none with SAME_AS_QUESTION_DIAGRAM. I did not add highlights for the answers to (i) (Bus) or (iv) (Cycle and Two-wheeler): four sub-questions share one figure.
- **C59/C60 and C57/C58 (tables): none.** Could be read as ANSWER_IS_FIGURE (filled table) but the v3 prompt's own example makes a completed plain table LATEX_TABLE.
- **C42 question: none.** The book gives an empty table to fill (act-on-figure reading), but it is a plain table with only column headings.
- **C36: one picture for four book panels, with grade names, angles and point letters together** (about 16 text items). Checked in code that every label box lies inside its slice or outside the circle without overlaps. If it looks too busy, the grade names are the first thing to drop.
- **C45: required** (answer is the labelled rings). The alternative would be to leave the hours to text; I followed "printed answer is a picture".
- **C66, C69, C71 and C54 (work-and-time and bricks examples): none** although two teaching images show similar ideas; by the rules those are never linked and the items are fully text/arithmetic.

### Class 8 Ch 10, chunk C
- C75 and C77 (water tank, painters): the inverse relation could be shown as a "work rectangle" (20 x 6 = 30 x 4 family-days; 3 x 4 = 4 x 3 worker-days). That is a nice teaching picture but no v3 rule asks for it; none.
- C81 (chairs): see above; none.
- C85 solution: optional (see above).
- Summary block 0: matching picture would only make it nicer; none.

### Class 8 Ch 12, chunk A
- **Worked examples C2, C3, C4, C21 and C5 (none).** The book prints a dot plot that mirrors each example (P02-dot_plot-7, P02-dot_plot-8, P03-dot_plot-3, P06-dot_plot-2; for C5 the book uses other data), and a distance-arrow dot plot would be the natural picture. I chose `none` because the LP text carries every number and the kept concept image of the same concept shows the figure. If the user wants them, the specs would be: C2 dots 10, 10, 11, 17 with the mean line at 12 and arrows 2, 2, 1 | 5; C3 dots 2, 6, 10, 12 with the line at 7.5 and arrows 5.5, 1.5 | 2.5, 4.5; C4 the before and after plots of 5, 5, 10, 24 with 17 added (11 to 12.2); C21 dots 4, 7, 8, 12, 14 and the new 11 (median 8 to 9.5).
- **Q4 and More Q7 solutions (optional, not added).** See section 1.
- **More Q1 question (none).** Empty 3 by 3 grid in the book, no data in it (ACTION_ON_FIGURE could be argued for "fill the grid").
- **Kushti question C25 (none).** The book's notebook picture is referred to ("as shown") but the LP text carries every weight; a handwritten list of numbers is a plain list.
- **More Q7 question (required)** although the LP lists the counts, per decision 4.

### Class 8 Ch 12, chunk B
- **C55 (spreadsheet solution) required vs none/optional.** The answer is a cell address and a range, not a number. Step E lists "a highlighted part" as something visual a solution may add, and the figure ties the address E5 to column E and row 5, which is the point of the question. The text alone does carry the whole answer, so a stricter reading gives `optional`/`none`. Kept `required` per decision 4 (v3 rules as written).
- **C51 and C52 (spreadsheet worked examples) none vs required.** The cell addresses B3:G3 and B7:D7 are not given in the worked-example question; they come from the teaching text of C50 and the concept images. A reader could ask for a spreadsheet picture here (`DATA_IN_FIGURE`). I chose none because the text/LaTeX default holds, the concept images already show these exact formulas, and the two examples are kept consistent.
- **C48 (Q10 solution) none vs optional.** A dot plot with the mean 4.6 and the median 4 marked would be a nice extra, but the LP solution does not refer to marks on the figure.
- **C44 (Example 1 solution):** the book prints the family-size dot plot beside the working. Called none because the plot is already the teaching image of C40 and the arithmetic needs nothing from it.

### Class 8 Ch 12, chunk C
1. **C56** (worked, "where do April 33 and July 29 sit on the line graph"): none. Both values are in the question, the answer is a slope and a difference of 4. A picture of two points would only illustrate; if the user wants every line-graph worked example drawn, C56 and C58 would be the first to add.
2. **C83** (worked, Punjab -78 and Bihar close to 0 on the rice-wheat scale): none. The steps spell out what sign and size mean. The scale itself exists only in the book infographic (a colour bar from -100 "Mostly Wheat" to +100 "Mostly Rice"). If the user prefers it drawn: a number line -100, -50, 0, +50, +100 with the printed captions and markers at -78 and 0 would do.
3. **C84 / C85** (worked): none (arithmetic; C84 would need the real map, NOT_RENDERABLE).
4. **C87** (worked, school 9:30 am to 4:30 pm = 14 boxes from box 20): none. Pure arithmetic on the two-boxes-an-hour rule; the question does not read Manoj's printed strips.
5. **C68 and C78** (solutions): `optional`, not added. C68 answer = two year pairs (2016 to 2017, 2019 to 2020) and C78 answer = three peak-month ranges; all numbers are in the steps. The same graph with those segments or months highlighted would help (a v3 Step E "highlighted part"), but the book question only asks to identify them. If the user wants them, they derive from C67 and C77 and are easy to add: World segments in ANSWER with the readings 230, 480, 600, 1270; the peak months of Udupi, Rameswaram and Puri circled.
6. **C70, C71, C72, C81, C82 solutions**: none (SAME_AS_QUESTION_DIAGRAM). The LP solutions only say how to read the given graph and mark nothing (and give no concrete readings, see LP text issues). Kept consistent with each other.
7. **C98** (worked, Hex 3 by 3, "can the game end with neither player joining?"): `optional`. A 3 by 3 board with the red top and bottom and blue left and right sides would help, but the question gives no figure (the book gives only 11 by 11 boards) and states size and rule. SPATIAL_GEOMETRY would justify `required`; I applied "no question figure when the question gives none".
8. **C94/C95 and C96** (own strip, group project): none, OPEN_ENDED. The answer is a strip or graph made from the child's own timings; any picture would invent data. A v3 reader could also call C95 `ANSWER_IS_FIGURE` (the answer is a 48-box strip); if so a sample strip is needed and then `needs_lp_text_sync` must be true.
9. **C57**: required although the LP question is a worked example with a concept image of the same graph already in the plan; the question gives no Punjab value, so the graph is data, not decoration. The figure shows both states because the book graph does and the answer compares with Kerala's rise; no minimum or maximum is marked.
10. **C77**: both rainfall graphs (6 lines) in one 16:9 picture (a pair gets one question diagram). The coast is blank in the book, so no coast word is drawn (the question asks for it).
11. **C79/C80**: the New Delhi line is drawn unlabelled in the book; the spec adds a legend entry "New Delhi" because part (iii) names it. Rounded values for the three added lines use half up for the .5 values (24.5, 15.5, 2.5); the LP only says "nearest whole number". The three added lines share ANSWER green and are told apart by marker shape and legend (v3: solution content in ANSWER).
12. **Colour choice for several lines**: the palette has only SET_A / SET_B for two groups. For graphs with 3 or 4 lines (C62, C67, C77) the specs use SET_A, SET_B, INK, GUIDE or ANSWER plus different marker shapes and direct names; in C62 West Bengal (the largest rise) is in ANSWER.

### Class 8 Ch 13, chunk A
1. **T5 Q1, Q2, Q3, Q4 question diagrams (required).** The LP text carries the bottom rows and where the blanks are, so a careful student could attempt from text. I kept them `required` (ACTION_ON_FIGURE + DATA_IN_FIGURE) because the book question IS the picture (it prints only pyramids with ? or empty boxes, and the student completes them), and because the filled pyramid is the answer (ANSWER_IS_FIGURE) and the four pairs are siblings. Per decision 4 not flipped to none. Q2 (10 / 4 ? / 1 ? ?) is also the book's teaching example and concept image M2.S4.T4.C19.IMG1 covers its steps; the item still draws its own given-state picture (v3: a concept image is never linked).
2. **T5 Q5 (C33 / C34).** Question `none`: the book prints no empty pyramid for this; the figure it prints on page 6 is the finished a + 2b + c pyramid, which is the answer. The question names the bottom row a, b, c in words, and the companion note says not to invent a question figure. Solution `required` (printed answer is a pyramid, B2): ONE diagram holding two pyramids side by side, the letter pyramid (a + 2b + c / a + b, b + c / a, b, c) and the numeric one the LP answer uses (23 / 10 13 / 1 9 4). Given bottom rows in INK, everything the solution adds in ANSWER green. Sibling note: Q1 to Q4 have a question figure, Q5 does not, because the book gives none.
3. **T5 Q6 / Figure it Out Q1 (C35 / C36), both none.** The book draws each case as a plain row of three boxes (4 13 8, 7 11 3, 10 14 25). The answer is one number per case and no pyramid is built, so the boxes carry nothing the text lacks (NUMBER_LIST_IN_BOXES, TEXT_SUFFICIENT; solution LATEX_ARITHMETIC). If the user wants the boxes drawn it is a one-picture addition; I did not add it.
4. **Date trick (C12/C13, C14/C15, C16/C17) and worked C6, all none.** The book shows the date trick only as the Shubham and Mukta comic strip (P02-dialogue_strip-1). I treated it as a procedure plus a number chain (26/01, 1 x 5 = 5, 5 + 6 = 11, 11 x 4 = 44, 44 + 9 = 53, 53 x 5 = 265, 265 + 26 = 291) with characters as decoration, i.e. number chains go to LaTeX (LATEX_ARITHMETIC), not a printed answer picture. If the user reads the strip as a "printed answer is a picture" case, the three solutions (C13, C15, C17) and possibly C12 would turn required with a `flow` style chain; they are the only place where this call could go the other way. C14, C16 follow C12 for sibling consistency. No concept image shows the strip, so no REUSES_CONCEPT_IMAGE.
5. **P05-number_pyramid-6** (the two-row lead-in a + b / a b): mapped `none:TEXT_SUFFICIENT`. No item uses it and no concept image shows exactly it (C23 shows the three-row version).
6. **Question marks versus empty boxes.** The book prints "?" in the unknown boxes of the page-4 pyramids (Q1, Q2, Q3 figures) and leaves them empty on page 5 (Q4 figures). I followed the book per figure.
7. **Letters in the Q3 solution.** The LP steps name the unknown boxes a, b, c, but the figure is not a lettered figure; the solution diagram shows the final numbers (32, 28, 20) only, as the book's filled pyramid does. Decision 3 (figure letters) does not apply to box names.
8. **One picture per side for Q1 and Q4** (brief: at most one question and one solution diagram per pair). Q1 holds the three pyramids in one picture, Q4 the three four-row pyramids (both LP blocks E0 and E1 of C31/C32).
9. **Figure accounting.** Teaching figures keep the base id with `concept_image:` (P03 -> C18, P04 steps -> C19, P05-1 -> C20, P06-1 -> C23). Where an item draws the same figure itself I added a `NEW-` entry for the second use (NEW-P03-number_pyramid-1-q5sol, NEW-P04-number_pyramid_steps-5-final, NEW-P06-number_pyramid-1-q5sol). P04-number_pyramid-4 and P04-number_pyramid-6 are labelled "teaching"/"given in question" in the base; both are the given state of Q2 / Q3, so they map to those question items. The page-4 pyramids 1 to 3 all map to C25 (question), the page-5 pyramids 3 to 5 to C31 (question). I did not claim P06-box_row-5, -6, -7 (Figure it Out Q3): that question is a unit of chunk B.

### Class 8 Ch 13, chunk B
- C39 question required although the LP text lists all numbers (decision 4). The same logic makes C53 and C55 questions required (their shapes live only in the picture) and C51 required.
- C38 and C44 solutions required on the strength of the "filled figure described in words" rule, although the answer asked for is an expression (C38) or a statement (C44).
  If the rule is read as "the answer itself must be a picture", both would be none; C42 stays required either way.
- C54 solution required: the printed answer in the book is a picture (shape equations); the figure adds only the two values as a key. It is the thinnest of the required solutions.
- C60, C61, C64, C65, C66, C67: none although the book prints boxes; read as an inline blank in an expression (LATEX_ARITHMETIC), not a data figure.
- C72, C74, C76 questions: none under the procedure-picture rule; the text "Follow Mukta's trick" is also a FIG_REFERENCED-style pointer. If these should be drawn, one spec (the four steps worked on 47) fits all three.
- C48 worked example: none; a calendar with 10, 17, 24 marked would help but a teaching image of exactly that already exists (M2.S7.T7.C48.IMG1) and is never linked.
- C40 solution: none, no new visual.

### Class 8 Ch 13, chunk C
- C81, C89, C99, C101 solutions: optional rather than none (a figure would clearly make the idea visible; the text is already complete). They cost nothing either way because optional is not added.
- C91 solution: none, although the all-hens argument could be drawn as 55 animals with 2 legs each and 20 horses with 2 extra legs. I judged it plain arithmetic.
- C78 question: none, although the question refers to the trick "given above".
- C85 worked example (double and give 5 away, twice): none, while C89 and C101 (same process) are optional on the solution side. The difference is the side: a worked-example figure goes after the question, where nothing visual is given; a solution figure shows the complete final state.

### Class 8 Ch 14, chunk A
- C7 question and C9 question: required although the LP text states every number (book figure carries the data).
- C26 question: required although the text states every fact.
- C8, C10, C25 solutions: optional, not added (figure only repeats the question figure plus numbers).
- C23 solution (shaded half) and C26 solution (equal halves) and C15 solution (bend highlight) and C16 solution (doubled square): required although the arithmetic or argument is complete in text; kept because each adds a geometric fact the steps refer to.
- C5 worked example: required (shape not fixed by words); C4: none.
- C19 worked example: required (base, perpendicular height and the later 'outer rectangle' are only meaningful with a picture); a teaching image of the same idea exists and is not linked.

### Class 8 Ch 14, chunk B
- **C30, C41, C42, C50, C51 worked examples:** a careful student could read the numbers from the text, but each is a geometry example whose point is the shape (diagonals, a height on the opposite side of a diagonal, composite pentagon, cut-and-slide, any base). Kept `required` (decisions 4 and 5).
- **C35, C37 solutions `none`:** the solution only adds the value of BY on a figure that already has both heights.
- **C45, C46 solutions `optional`:** rule D (marking piece areas on the given figure). If the user prefers area labels on the pieces, these two would be `required` with `derived_from` the question figure.
- **C38 solution `required` versus C46 solution `optional`:** C38 adds a point and symbolic lengths that the steps need to be understood (DH meets AB at its midpoint); C46 only restates areas of pieces that are already visible.
- **C54 solution `required`:** it would also be defensible as `optional` (the letters already name (g) and (a)); chosen `required` because the answer is a selection among drawn figures (circled smallest / boxed largest).
- **C47 and C49 solutions `required`:** the answer is a construction described only in words (B2: "answer is a construction"), even though the question side has no figure.

### Class 8 Ch 14, chunk C
- C55 question, C56 question, C74 question, C76 question: `required` although the LP text carries the numbers (the book question refers to printed figures).
- C57 question `required` (the book prints the same-base figure with the hint) while C57 solution is `none` (it only states "height < 4", which the question figure already shows).
- C62 solution `optional` (a picture of the triangle beside the square with its height marked would help; the three text steps are complete; the question has no book figure). C62 question `none`.
- C58, C59, C61, C68 solutions `required` (ANSWER_IS_FIGURE: the answer is a dissection or construction described only in words); their question sides are `none` because the book gives no figure.
- C60 solution `required` (arrangement of two triangles into a rectangle).
- C63 and C64 worked examples `required` (the dissection of a rhombus and the split into two triangles are spatial, and the book draws both).
- C71 and C72 worked examples `required` (the construction BG and the two-copy parallelogram are the point of the example).
- C75 solution `required` (shaded pieces with areas); C55, C56, C77 solutions `none`.

### Class 8 Ch 14, chunk D
- **C79 (Q5) solution, required.** The book's question figure already draws the whole construction (dashed rectangle EFGH). The solution diagram only adds the four shaded congruent corner triangles AHI, DGI, BEJ, CFJ (the LP steps rest on them). Could be `SAME_AS_QUESTION_DIAGRAM` if the team wants fewer images.
- **C81 (Q7) solution, required.** Adds the three missing radii (so six equal triangles are visible) and colours the three pieces; the LP steps count 3, 1 and 2 triangles. No counts are printed in the picture (a number inside one small triangle would look like a count for that triangle only).
- **C82 (Q8) solution, required.** Adds the shaded triangles ZYA and BXA and the equal-angle arcs (single arcs at A, double arcs at Y and X). Same kind of answer as Q5, so the same decision.
- **C78 (Q4) and C80 (Q6) solutions, required** although the question side has no figure (word questions): the printed/LP answer is a dissection (Q4) and a constructed trapezium (Q6), Step B2 `ANSWER_IS_FIGURE`. No question diagram for either.
- **C78 (Q4) solution is one card with two panels** (cut and moved pieces on the left, finished rectangle on the right). Letters a, b, h come from the LP text; the drawing uses a = 4, b = 8, h = 4 only as proportions and prints no numbers.
- **C80 (Q6) solution:** the LP gives parallel sides 8 cm, 16 cm and height 12 cm only. I drew an isosceles trapezium (slant is my choice, any slant gives area 144); the 12 by 12 rectangle of the LP steps is not drawn.
- **C90 (pair Q2, "1 in² to square centimetres"), solution none.** The book's picture of two squares (1 in and 2.54 cm sides, base figure P23-shape-3) is the book's teaching explanation inside the section text; the pdf has no printed-solutions section and the question itself gives no figure. I mapped the figure to the teaching image C84.IMG1 (accounting). If the team counts that picture as a printed answer (Step B2), C90 solution becomes required: two equal squares, left "1 in" by "1 in", right "2.54 cm" by "2.54 cm", area labels "1 in²" and "6.4516 cm²". Sibling C93 (1 ft² = 144 in², no book figure) stays none either way.
- **C88 (A4 sheet) solution none:** a 3-by-4 layout of sheets would be nice to see, but all numbers are in text and the teaching image C83.IMG1 already shows it. Not even `optional`.
- **C85 worked example none:** an 8 m by 6 m classroom rectangle is not needed for 8 × 6 = 48 and 1000000 ÷ 48 (kept teaching image C85.IMG1 shows the km2 square).
- **C95 / C96 (largest / smallest city):** open research tasks, none on both sides (the video's empty city/area table is a plain table).
