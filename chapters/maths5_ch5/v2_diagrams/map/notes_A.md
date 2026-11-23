# Chunk A notes (Class 5 Ch 5 "Far and Near", units 1-19, topics M1.S2.T2 to M2.S9.T9)

Result: 32 items = required 13 / optional 1 / none 18. Validator `--chunk A`: errors 0, 3 warnings (C26, C33, C35 are required but their figure is not printed in the book: expected).

Required (13): C8 q and C9 s (sari double number line), C17/C19/C21/C23 q and C18/C20/C22/C24 s (six tallest statues), C26 worked (flags on a 2 km track), C33 s and C35 s (water stations, children on the 3 km race).
Optional (1, not added): C11 s (lines joining the two columns of the sari match).
Media ids: all `<cid>.IMG1`, except C26 = `M2.S7.T7.C26.IMG2` (IMG1 is the kept teaching image).

## 1. Judgement calls and Borderline

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

## 2. LP text issues (user decision 2: no text edited, no decision changed because of them)

- **M1.S4.T4.C8** (question): the text lists the labels but not the two arrows, ×2 (100 cm to the first blank) and ×100 (1 m to 100 cm), which only the figure carries; the solution C9 refers to both arrows. Suggested sentence to add (only if the figure is ever missing): "The arrow ×100 goes from 1 m to 100 cm and the arrow ×2 goes from 100 cm to the first blank."
- **M1.S6.T6.C17, C19, C21, C23** (Let Us Compare Q2 a-d, questions): each says only "Look at the picture of some of the world's tallest statues" and carries none of the six names and heights, so the question cannot be solved without the figure. Suggested sentence: "The heights are: Statue of Unity, India, 182 m; Spring Temple Buddha, China, 128 m; Guanyin of Nanshan, China, 108 m; Statue of Liberty, USA, 93 m; The Motherland Calls, Russia, 91 m; Christ the Redeemer, Brazil, 38 m."
- **M2.S9.T9.C32, C34, C36** (Kilometre Race Q1-Q3): the LP hint `q_figure` says "a straight race track of 3 km from the starting point to the finish line"; the book has no such figure (pdf p.4 is text only). No question diagram is made.
- **M2.S9.T9.C33, C35**: the solutions count a station / a child at the finish line (6 stations at 500 m ... 3 km, 10 children at 300 m ... 3,000 m). The book's question does not say whether the finish line counts; the LP choice is followed and drawn.
- **Stale image markers in `text`** of answer concepts, e.g. C7 ("[Image: Let Us Find: Ans1: solution]" after step 6 and "(continued)" at the end), C9, C11 and the other answer concepts: they mark the old card positions in the middle of the steps and after the answer. With the v3 rule (solution token first, before step 1) the old markers must be removed or replaced when the builder writes the new token.
- **M2.S8.T8.C29**: all numbers are practice values (125 steps for 100 m, one step 80 cm): the arithmetic checks (10,000 / 125 = 80; 12,000 / 80 = 150; 40,000 / 80 = 500; 160,000 / 80 = 2,000), no change needed; mentioned only because the question text is the book's open activity.

All other LP solutions in this chunk were recomputed and agree with the book's question and with themselves (Let Us Compare Q1 a-e, Q2 a-d, rope table, race Q1-Q3, sari match, worked examples).

## 3. Where the book itself is unclear

- Kilometre Race: whether the station / child at the 3 km finish line is counted (see above). The LP counts it.
- Double number line (p.1): the tick spacing is only roughly proportional in the print; drawn exactly to scale here. The `×100` arrow runs from the m line (bottom) up to the cm line (top).
- Statue heights (pdf p.2): the names and heights are taken exactly as printed (Statue of Unity 182, Spring Temple Buddha 128, Guanyin of Nanshan 108, Statue of Liberty 93, The Motherland Calls 91, Christ the Redeemer 38); not checked against outside sources.
- Let Us Compare (pdf p.2): "Ritika is comparing the lengths of different rods" has no picture of rods in the book.
