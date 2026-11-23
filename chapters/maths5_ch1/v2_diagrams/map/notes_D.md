# Notes, chunk D (topics M3.S26.T26 to M3.S31.T31)

Result: 28 items = required 9 (question 3, solution 5, worked example 1), optional 2, none 17. Validator: errors 0, warnings 5.
The 5 warnings are required items whose figure is not printed in the book (C114, C125, C128, C130, C132): expected.

Required (media ids):
- M3.S28.T28.C114 solution: river crossing, 8 panels (Start, Trip 1 to Trip 7). No question diagram, so it stands alone.
- M3.S29.T29.C124 solution: Mira's chain 73-37, 63-36, 72-27, 54-45 (the book's printed answer picture). No question diagram, stands alone.
- M3.S30.T30.C125 worked example (IMG2, IMG1 is the kept teaching image): 12 children around a square, corners shaded.
- M3.S31.T31.C127 question (book's stable with 19 horses) and C128 solution (derived: 5 on each side, corner horse circled, 19 horses).
- M3.S31.T31.C129 question (empty stable) and C130 solution (derived: 18 horses).
- M3.S31.T31.C131 question (empty stable, identical to C129's) and C132 solution (derived: 16 horses).

Optional (not added): C116 solution (strip of pebble piles), C117 question (the chain picture the book calls "each step above").

I checked every base-inventory figure of this chunk against the page pictures (pages 11, 12, 13, 15, 16): all descriptions are right (7 pebbles per stack, the stable's 19 horses and side sums 5/5/5/5, the table's four rows, the four subtractions, the two empty frames). The only `unclear` entry (P11, boat in the middle of the river) does not matter for any decision. The decorative train picture on page 11 (Sanju, Mira and an adult) is not in the base and carries no mathematics, so I added no entry.

## Borderline

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

## Judgement calls

- **P15 stable counted twice.** The base figure P15-dot_pattern-2 is the picture of the question C127 (becomes its diagram) and also the story picture that exists as teaching image C125.IMG1. Base id maps to `item:M3.S31.T31.C127 (question)`; the teaching use is accounted as `NEW-P15-dot_pattern-2-teaching` -> `concept_image:M3.S30.T30.C125.IMG1`. Nothing is linked to the teaching image.
- **P11 river scene** maps to `concept_image:M3.S27.T27.C109.IMG1` (same scene, already a teaching image); C113 itself is none.
- **C114 strip.** The earlier hint said seven pictures; I added a Start panel (the LP says "At the start ...") so the eight panels read as a complete sequence. Labels used are only words the LP uses: Start, Trip 1 ... Trip 7, lion, sheep, grass, boatman. Left bank = near bank, right bank = far bank (by the Start panel); no bank names are drawn. The outlined chip (FOCUS) is who crossed in that trip; Trip 2 and Trip 6 outline the boatman (crosses alone). All 8 states were checked in code (no unsafe pair left without the boatman).
- **C124 colours.** Column 1 (73 - 37 = 36) is what the question gives (INK); columns 2 to 4 and the arrows are the solution (ANSWER). Nothing else is drawn.
- **Stable pictures.** Question figures show only what the book prints (C127: dots only, no 5s, no total; C129/C131: empty ring). Dot placement inside a stall is one fixed pattern per count (1 centre, 2 diagonal, 3 triangle), not copied from the book where the pairs sit side by side or diagonal; only the count per stall carries meaning. Horses in question figure C127 are SET_A; horses added by a solution (C130, C132) are ANSWER (rule: given INK, added ANSWER). Corner horses are circled (FOCUS) in every solution figure because the explanations are about corner horses counted on two sides.
- **C130** draws the LP's sample arrangement (1 horse top-left, 1 bottom-right, 2 in each of the 8 middle stalls). The LP says "your arrangement may differ".
- **C132** draws the LP's final state (16 horses). The middle stalls follow "2 then 1 going clockwise from each corner", which gives the LP's top side as 1 + 2 + 1 + 1 and the other sides the same by rotation. The second arrangement in the LP steps (3, 2, 3, 2 horses in the corner stalls, 10 horses) is not drawn: one solution diagram per item.
- **Totals in solution figures** are written as "19 horses", "18 horses", "16 horses" (two words, taken from the LP text).
- **Aspect ratio** 16:9 everywhere (the pipeline draws 16:9 cards), also for the chain and the stable.

## LP text issues

| Concept id | What is wrong or missing | Suggested sentence |
|---|---|---|
| M3.S31.T31.C127 (question) | The text never gives the horses' arrangement; only the book picture does. The figure carries it, but if the figure is ever dropped the question cannot be done. | "The stable is a square ring of 12 stalls. The horses stand like this: top row from the left 1, 2, 2, 0; left middle stalls from the top 1 and 3; right middle stalls from the top 2 and 3; bottom row from the left 0, 2, 3, 0." |
| M3.S31.T31.C129 and C131 (question) | The text says "square stable" but not that it is a ring of 12 stalls with shared corners. | "The stable is a square ring of 12 stalls: 4 along the top, 4 along the bottom and 2 on the left and on the right. A horse in a corner stall is on two sides." |
| M3.S31.T31.C132 (solution) | The answer "2 more horses" is one reading. The LP's own steps show that with the corner stalls crowded (3, 2, 3, 2) only 10 horses are left with 5 on every side, i.e. up to 8 more could be stolen. The book prints no number. Steps 8 and 9 also contain a sentence addressed to the author ("The book does not print a number for this, so this is one way to read the question"), which does not belong in a learner-facing solution. | Decide the intended answer. If "2 more" stays: "He can steal 2 more horses, leaving 16 with one horse in each corner stall. With fewer horses the corner stalls must be crowded, for example 3, 2, 3, 2 horses in the corners and 10 horses in all, and the king would notice." Remove the author-addressed sentence. |
| M3.S31.T31.C132 (solution) | Step 6 says "The other three sides are the same" without saying in which direction 2 and 1 run. | "Going clockwise from each corner, the two middle stalls hold 2 and then 1." |
| M3.S28.T28.C119 (item hint `q_figure`, not student text) | The hint says four empty rows follow the table; the book prints four filled rows only. | Not a student-text issue; fix or ignore the hint. |

## Book unclear or inexact

- Page 15: the dots inside a stall are drawn side by side, diagonal or in a triangle without meaning; only the count per stall matters (checked: 19 in all, each side 5).
- Page 16: the two empty stables are unlabelled; which one belongs to "arrange the 18 horses" and which to "how many more" is by position (left, right) only.
- Page 16: "How many more horses can the thief steal before the king notices something is wrong?" has no printed answer and no stated limit (see C132 above).
- Page 12 and page 13: the book has no printed solutions section; the LP solution text is the answer followed. Nothing in the LP contradicted the book in this chunk (all sums, counts and chains in the LP solutions for C104 to C132 were recomputed and are right).

## Book mistakes (decision 1)

None found in this chunk; nothing corrected. Figure letters (decision 3): the chunk has no lettered figures, none drawn.
