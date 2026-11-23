# Chunk E notes (Class 6 Ch 2, Lines and Angles)

Topics: M3.S25.T25 (Figure it Out 2.9, Q1-Q9, book pp 40-43 = pdf pages 28-31), M3.S26.T26 (clock worked example), M3.S27.T27 (Where are the angles, Q1-Q5, book pp 45-46 = pdf pages 33-34), M4.S28.T28 (two angle games).
Result: 31 items, required 15 / optional 2 / none 14, validator errors 0.

## 1. Judgement calls

T25 Figure it Out 2.9 (measure with a protractor)
- Q1, Q3, Q5, Q6, Q7: question side REQUIRED (the angles to be measured exist only in the figure). Printed answers on pdf p.50 are plain text, so no picture-answer rule applies.
- Solution side is split, and the split is deliberate:
  - Q1 (C124), Q3 (C128), Q5 (C132), Q7 (C136): `none` (SAME_AS_QUESTION_DIAGRAM + TEXT_SUFFICIENT). The question figure already has the arcs; the solution would only write numbers (47/23/108, 42/116, six readings, 45/100/150) on it, and the text lists them completely. If you prefer "values written on the figure" for every measuring question, flip these four to required (they would be derived_from their question figure); the rule text allows both, I chose the stricter reading of "solution adds something visual".
  - Q4 (C130) required: the method uses the UNMARKED 100 degree angle, which the question figure does not show; the solution figure adds that arc and 100 / 260.
  - Q6 (C134) required: the question figure has no arcs at all; the LP solution derives BXC = BXE - CXE and checks A, X, E on a line, which needs four arcs (65, 30, 85, 115) to be seen. This is the reason Q7 (arcs already given) is `none` while Q6 is required.
- Q2 (classroom angles): `none` both sides (OPEN_ENDED, no figure in the book).
- Q5: ONE question figure with six angles (the LP keeps the six book parts in one concept). The lowercase angle names a-f are in the image because the question text says "angle a ... angle f" (they are angle names, written without a full stop); this slightly bends the "no figure letters" rule, flagged here.
- Q8 (origami): question REQUIRED (the eight folding pictures are the instructions: "as per the given instructions"). Spec traced from the page picture (see section 3). Solution `optional`: a crease pattern with measured angles would help, but neither the book nor the LP states the creases or angles (LP answer "open-ended"); nothing invented.
- Q9: question REQUIRED (lettered Fig. 2.21 (a), (b), (c)). The captions (a), (b), (c) are kept in the image because the question text names the triangles by them (again a small bend of the "no figure letters" rule). Solution `optional`: the LP gives no measured values ("about 180 degrees every time"); a figure with measured angles would help but the numbers would have to be invented from the picture. Page-picture estimates for a text sync: (a) about 46, 65, 69; (b) about 54, 63, 63; (c) about 31, 52, 97.

T26 (C141, clock at 5 o'clock worked example): `none`, TEXT_SUFFICIENT. All data is in words (360 / 12 = 30, 5 x 30 = 150) and the concept keeps its own teaching image (never linked).

T27 Where are the angles (all five are "find the angle in a picture")
- Question side: `none` for all five. The book pictures are scene illustrations (clocks, a boy and a door, a girl on a swing, a toy with children, snail and ladybird); the questions are conceptual and the words carry everything needed. Q4 (toy) and Q5 (insects) say "Here is a toy" / "Observe the images below", so they carry FIG_REFERENCED + NOT_RENDERABLE and `needs_lp_text_sync: true` with a sentence to add (see section 2).
- Solution side: `required` for all five (sibling consistency: the answer is always "where the angle sits", i.e. a picture):
  - C144 (clocks): four clock faces 1, 2, 4, 6 o'clock with a green arc between the hands marked 30, 60, 120, 180. The book prints clocks at 1, 2, 4 only; the 6 o'clock clock is added because the question asks for it. 3 and 9 o'clock (part c) are not drawn.
  - C146 (door): clean top view, hinge = vertex, door and wall = arms. Opening drawn at 50 degrees (estimated from the book picture; no value printed, none shown).
  - C148 (swing): rope at rest straight down, rope at the highest position 35 degrees out, green arc at the hanging point. 35 degrees is a sample (book prints none).
  - C150 (toy slabs): one gentle (15 degrees) and one steeper (30 degrees) slab, dashed level ray = the arm that is not visible. The book's toy has only gentle slabs (about 10-16 degrees); the LP solution compares a gentle and a steeper slab, so both are drawn.
  - C152 (insect): one generic insect pair (resting + turned 80 degrees about its rear end), horizontal line and the line along the insect as the two arms. The book's rotation is about a quarter turn; 80 degrees avoids reading as exactly a right angle. Sample answer as in the LP.
- Because the question sides have no diagram, the solution diagrams have `derived_from: null` and draw the whole figure.

T28 (C154, C155): `none`. Rules of two team games in words, numbers (49/39/10, 34/25/9) in the text; C154 keeps its own teaching image.

Figure inventory choices
- 31 entries. Figures whose picture becomes a question diagram map to the question item; where the same picture is the base of a solution diagram (Q4, Q6) a second entry NEW-<id>-sol maps to the solution item.
- T27 scene pictures (clocks, door, swing, toy, insects) are mapped to the SOLUTION item whose schematic redraws them (their question items are `none`).
- Section 2.10 teaching figures on pp 35-36 (P35-ray-1, P35-protractor-1, P35-protractor-2, P36-shape-1) are mapped to concept_image:M4.S28.T28.C153.IMG1 (the Drawing a 30 degree angle concept; accounting only). C153 is not a unit of any chunk, so I claimed these by "book section of one of my units"; another chunk may claim them too with the same meaning.
- Base descriptions checked against the page pictures: all correct. Additional details noted in the entries: the stray small "c" in P29-angle-1; P29-angle-3 is a reflex marking with the open V arrowheads.

Numbers in the figures
- No angle value is printed on any book figure. Arm directions were read from the page pictures (about 2 degrees uncertainty) and set to the LP answers, which equal the printed answers: Q1 47/23/108, Q3 42/116, Q4 100/260, Q5 80/120/60/130/130/60, Q6 65/115/85/30, Q7 45/100/150. Every figure's accuracy_checks recomputes these from the stored directions.

## 2. Things that look wrong in the LP

- T27 book numbers: the LP numbers the "Where are the angles?" questions "Figure it Out 2.9, Q1..Q5", the same as the Figure it Out 2.9 measuring questions of T25. In the book they are the separate "Where are the angles?" set (ncert_refs 2.9.FiO3.Qn). Titles collide on the card.
- T25 Q1 and Q3 question texts embed descriptions of the figure ("(Three angles drawn, each with a small arc at vertex H.) first) angle at H between HI and HJ (here I is nearly straight up ...)", "(left drawing) / (right drawing)"). Harmless next to a real figure but redundant; Q5 also repeats the part list twice ("a. b. ... a) angle a ...").
- T27 Q1 question text repeats parts (a), (b), (c) twice ("Angles in a clock: (a) ... (b) ... (c) ... (a) At 1 o'clock ... (b) Angle at 2, 4 and 6 ... (c) Explore ...").
- T27 Q4 and Q5 question texts point at pictures that this plan does not carry ("Here is a toy ...", "Observe the images below"). Suggested sentences (also in text_alternative): Q4 "The toy has slanting slabs fixed to its side walls and the balls roll down them."; Q5 "An insect lies along a horizontal line, and the same insect is shown turned upwards by about a quarter of a turn from that line."
- T27 Q3 solution step 2 is muddled: "Fix one arm at the position where the swing starts; it begins at the point where the swing hangs." The figure follows step 4 (second arm from the hanging point to the highest position; first arm = rope hanging at rest).
- T27 Q4: the printed book answer contradicts itself ("The vertical arm is not visible ..." and then "Top horizontal ray is not visible"); the LP uses the horizontal ray and so does the figure.
- T25 Q2, Q8, Q9 have no printed answer in the book; the LP wrote its own. Q9's LP answer says "about 180 degrees every time" with no measured numbers.
- T28 C154 and C155 both carry the concept name "Angle guessing games" and a "Worked example:" prefix in `text`; the book calls them Let's Play a Game #1 and #2.

## 3. Where the book itself is unclear

- Figure it Out Q8 (origami, pdf p.31): steps 3 to 7 are small stylised drawings. The dashed fold lines, which flap lies over which, and the direction of the little arrows (steps 3, 4, 6, 7) could not be read with certainty; step 5's curly arrow is read as "turn the paper over". The spec traces the outlines and fold lines as seen and treats the arrow curves as schematic; step 8's rabbit face (two eyes, nose, mouth) is drawn as plain shapes. No angle or length is printed. If the renderer cannot reproduce this faithfully, treat C137 as NOT_RENDERABLE and keep text.
- Figure it Out Q3 left drawing has a tiny stray letter "c" inside the arc (not referred to anywhere); left out.
- Q6: which scale to read is not stated; the figure keeps both scales exactly as printed (outer scale 0 at the A end).
- T27 Q2 door angle, Q3 swing angle, Q5 insect rotation: no values printed; only estimated by eye from the pictures (about 50 degrees, about 20 degrees at rest, about a quarter turn).
- T27 Q1: only 1, 2, 4 o'clock clocks are pictured while part b also asks for 6 o'clock.
