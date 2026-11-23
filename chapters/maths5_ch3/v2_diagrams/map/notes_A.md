# Chunk A notes (Class 5 Ch 3 "Angles as Turns", topics M1.S2.T2 to M1.S9.T9, units 1-18)

Result: 31 items = required 11 / optional 6 / none 14. Validator: errors 0, 3 warnings (C15, C31, C35 are required but print no matching book figure: expected, the LP's own scenes).
All 17 inventory entries claimed: 14 base figures (P01 to P05, minus P05-angle_tool-2 which belongs to chunk B) + 3 `NEW-<base>-sol` entries for the solution use of the Statue pictures, the house and the gymnast rows.

Required items (own media ids; kept teaching images are never reused, user decision 5):
C5 Q + C6 S (Statue pictures), C15 worked (hinges P, Q, R; id IMG2 because IMG1 is the kept teaching image), C25 worked (fan X, Y, Z; id IMG2), C29 S (fan acute / right / obtuse), C31 S (two acute turns), C32 Q + C33 S (house of books), C35 S (5-sided shape), C36 Q + C37 S (gymnasts).

## 1. Judgement calls

### Borderline (user decision 4)
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

### Other calls
- Statue figure: B faces the front (the LP says so); the book draws B slightly angled in the second picture.
- Figure letters (decision 3): the house letters A to H are the figure's own circled letters and the LP refers to them, so they are drawn; X, Y, Z (fan) and P, Q, R (hinges) are drawn because the questions name them; the five gymnast rows and the three fans of C29 carry no letters.
- Inventory mapping: P03-straw_angle-1 (three straw angles) is mapped to the C25 worked example (its fan figure shows the same three openings); P03-fan_angle-4 to the C29 solution; P04-table-1 and the teaching circles go to concept images (accounting only). P02-straws-3 (hands holding straws) none / DECORATIVE_ONLY; P03-fan_steps-3 (craft steps) none / TEXT_SUFFICIENT; P02-table-2 none / LATEX_TABLE.
- Base description corrected: P04-book_house-3 (entry starts "CORRECTED:"): B is the quarter mark in the gap between the two stacks (right face of the left stack on the flat book), D and E are the two ends of the leaning board in the lower box; all eight kinds are right/acute/obtuse as in the LP.

## 2. LP text issues (not edited, decisions not changed)
- **M1.S4.T4.C7 (worked)**: the steps say "the seat is back at the starting position E" but the question never says what E is. Suggested: "A seat E on the giant wheel starts at the top. It takes 1 half turn and then 2 quarter turns, all in the same direction. What turn is that in all?"
- **M1.S5.T5.C9, C11, C13 (questions)**: "the starting position E": E exists only in the book's wheel picture (letter above the top seat) and no wheel picture is added. Suggested: "A giant wheel makes a full turn when it comes back to the starting position E, the seat at the top of the wheel."
- **M1.S3.T3.C5 (question)**: "the child in the picture" does not say there are two pictures. Suggested: "Look at the two pictures of the children, before and after the call STATUE. Can you recognise the child who has made a full turn? ..." The figure labels the pictures Before and After while the solution says "first picture" and "second picture": either say "the Before picture / the After picture" in the steps or accept.
- **M1.S7.T7.C20 (solution)**: the sample ticks read as exact: scissors "a 1/4 turn", tongs "less than a 1/4 turn". Real scissors open to nearly a half turn. Suggested: "(d): the scissors open about a 1/4 turn" (it already says "Your answer may differ").
- **M1.S9.T9.C29 (solution answer)**: the answer line leaves out the right angle that the steps and the figure show. Suggested: "Sample answer: less than a 1/4 turn is acute; exactly a 1/4 turn is a right angle; between a 1/4 and a 1/2 turn is obtuse. Your answer may differ."
- **M1.S9.T9.C31 (solution)**: the answer says "two bigger ones can make a right angle or an obtuse angle", but step 3 says a right angle comes from two turns that add to exactly a quarter turn (not necessarily bigger). Suggested: "Sometimes. Two small acute turns can together be acute; two acute turns that add up to exactly a quarter turn make a right angle; two bigger acute turns can make an obtuse angle." The figure shows them in the order acute, right, obtuse; the steps list obtuse before right.
- **M1.S6.T6.C15 (worked)**: "(a practice picture)" is now backed by the new diagram; if the diagram were dropped the phrase would point at nothing.
- No book/LP number clashes found: C33 counts (3 right, 3 acute, 2 obtuse = 8), C35 steps (angles sum 540), C37 order all agree with the pictures.

## 3. Where the book itself is unclear
- No printed solutions section in this pdf: every answer comes from the LP.
- Statue picture: facings are judged by eye (B slightly angled in the second picture).
- Fan pictures (P03-fan_angle-4): the three openings are about 30, 55 and 108 degrees by eye; the book shows two acute and one obtuse fan under "show different acute angles and obtuse angles".
- House of books: the marks are small; G's book leans slightly (the LP calls it right), D/E sit on a leaning board whose exact slope is not stated; the book states no angle measures. The redraw only keeps the kinds right / acute / obtuse.
- Gymnast rows: the book gives no numbers; 60, 90, 120, 150 and 180 degrees are chosen to agree with the LP wording.
- Fan-making steps (P03-fan_steps-3): step 1 shows 19 strips but step 2 about 10 panels (schematic); not used by any item.
- The three shaded circles printed under "Make an acute turn..." (P04-circle_turns-2) show 1/4, 1/2 and 3/4 turns, not acute turns, so they do not serve the C30/C31 items.
