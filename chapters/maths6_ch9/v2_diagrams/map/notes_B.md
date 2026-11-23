# Chunk B notes (Class 6 Ch 9 Symmetry, topics T10 to T14)

Result: 25 items, required 16 / optional 2 / none 7. Validator: errors 0, warnings 0. Figure inventory: 56 base figures claimed (51 to items, 3 to concept images, 2 none).

Output: `map/out_B.json`. All specs are on a 16 by 9 unit canvas (1 unit = 120 px at 1920 by 1080), origin at the centre, y up; every coordinate is written out in `manim_description` and `content`.

## 1. Judgement calls

Required (16):
- C39 (paper folding and cutting, worked): the dotted cut on the folded sheet is the data of the sketch task; the text only says "a notch shape". One picture only: the book's second picture (hands and scissors) is decoration, the unfolded answer is not drawn. Media id C39.IMG2 (IMG1 is the kept concept image).
- C40 (blue cut-out design, worked): the question says "like the blue star-shaped cut-outs shown" and asks for the lines of symmetry of that design; drawn as 3 eight-pointed stars between two rows of 5 diamonds (SET_A). Media id C40.IMG2.
- FiO 9.1 Q1 to Q5: question diagrams required (all data is in the pictures). Solution diagrams required for Q1, Q2, Q4, Q5 because the printed answers are pictures (fold lines; second hole; opened sheets; fold-and-cut sequence).
- FiO 9.1 Q3 (C46) question: judged required although it is an introduction with no question to answer. The text says "we represent it this way" and the two fold icons (Vertical Fold, Horizontal Fold) are its only content. If the reviewer prefers text only, flip it to optional; nothing else depends on it. Solution C47 is none (no printed answer, nothing new to show).
- Example 1 strip (C60/C61): question = the given strip with centre dot; solution = original strip plus the strip turned by 180 degrees with a clockwise half-turn arrow marked 180°. The original is moved up to y = 2.2 to make room (same size and x position); `derived_from` is set but the layout is not identical.
- FiO 9.2 Q1 (C62) question required; solution C63 is none (printed answer is text only; a solution picture would only repeat the question figures).
- FiO 9.2 Q2 (C64/C65): question = 7 figures; solution = same 7 figures with a FOCUS box around the 5 that have more than one angle of symmetry. The book's printed answer repeats only the five; I kept all seven because the LP s_figure says so and the layout stays the same.

Optional (2), not added:
- C52 (rangoli): the text already describes the picture (ring and four red petals) and the same picture is concept image C52.IMG1 in the same concept. A faithful rangoli (ring, 8 green petals, 4 pink-red petals, squares, teardrops) would be decorative art.
- C53 (windmill): the text states 4 equal blades, red centre point, same after 90 degrees. A windmill picture would help (no concept image of it exists in T12), but the answer does not depend on it. If wanted, it would be a 4-bladed windmill with a red dot at the centre.

None (7): C38 (ink blot activity, no figure in the book), C54 (open question), C55, C56, C57 (the question gives no figure; the book's labelled-square figures are the teaching figure of concept image C55.IMG1), C47, C63 (see above).

Style decisions to be aware of:
- Part letters (a), (b), ... are not drawn (v3 section 4). Multi-panel figures follow the order of the question text, left to right, top to bottom.
- Sheet tints PAPER_PURPLE #D9CCEF (Q4c, Q5) and PAPER_YELLOW #FBE9A6 (Q4d) are not style tokens. They match the purple and yellow sheets named in the question text; green sheets use MARK_FILL. Replace with tokens if the renderer cannot take extra colours.
- The word "fold" labels fold edges in Q4 and Q5, and the two words "Vertical Fold", "Horizontal Fold" label the icons in Q3. They are legends of the picture, not headings. Q5 solution also has the digits 1 and 2 (order of the two folds, as in the LP step text).
- Holes of Q2 are INK rings (the book colours them cyan); the answer hole is ANSWER green. Q1 sheet 2 and Q2 hole positions were measured from the book pictures and made exact mirror images (the book's pair of holes in Q1(b) is very slightly off).
- Q5 solution: the cut square is 0.3 of the piece side and the cut triangle legs are 0.424 of the piece side, chosen so that the opened hole equals the question's hole (square of side 0.3 of the sheet, diamond of half-diagonal 0.212). The book's printed (b) cut is about half the piece side, which would give a larger diamond than the question figure.
- Q4 solution sheets are drawn at the same 2 by 2 cells as the question; the opened (c) and (d) sheets are drawn at 0.75 scale in the boxes of the folded pieces. The wavy sides of (a) are a smooth curve through the listed points.

Figure inventory choices:
- P01-pattern-3 (chapter-opening rangoli) is claimed as `concept_image:M2.S12.T12.C52.IMG1`. Another chunk may map it to M1.S1.T1.C1.IMG1 (the four pictures); same meaning (a teaching figure).
- P14-rotation_figure-7 (windmill) -> none:TEXT_SUFFICIENT; P07-paper_fold-3 (Punching Game introduction) -> none:TEXT_SUFFICIENT; P15-rotation_figure-1/-2 -> concept_image C55.IMG1.
- Corrections to the base descriptions (marked "CORRECTED:" in the entries): SOL27-paper_fold-5 to -9 (the bold ring is the new hole, the given hole is the washed-out one; the base had them the other way round); SOL27-paper_fold-10, -11 and SOL28-paper_fold-1, -2 are the printed ANSWERS (opened sheets), not figures given in the question; P19-shape-5 is an isosceles triangle (flat side about 180, height about 181), not equilateral.

## 2. Things in the LP that look wrong or thin

- C46/C47 (FiO 9.1 Q3) is an introduction split into a question and an answer card; the answer text itself says "no question to answer".
- C48 text for Q4(d) says the notches are "along the open edge", but the book picture has one notch on the fold edge and one on the open edge (the opened sheet then has a middle hole and two side notches, which is what the LP answer says). The diagram follows the book.
- C51 answer text for Q5(a): "cut a small square with all sides closed". The book means "at the closed corner (all sides closed corner)"; the cut itself is a small square at the corner where the two folds meet.
- C39 text says "In two pictures"; only one picture is meaningful (the second only adds hands and scissors).
- C52, C53 and C54 all carry the concept name "The windmill and its centre of rotation", but C52's example is about the rangoli. C52 ncert_refs also list 9.1.q1.
- C55 answer says "A goes to B, B to C, C to D, D to A", but the question gives no labelled square and concept image C55.IMG1 shows corner ticks, not letters. A labelled square is only in the book's teaching figure.
- C65 steps name the order of each figure (4, 3, 4, 4, 5) before orders are taught (they come in FiO 9.2 Q3); harmless, but the diagram does not draw them.

## 3. Places where the book itself is unclear

- FiO 9.1 Q2 printed answer: only the new hole is bold; the given hole is almost invisible (see correction above).
- FiO 9.1 Q4(c): the question's sheet is about 0.83 wide to tall, the printed answer sheet about 0.64; the diagram uses 0.83. The printed answers of (c) and (d) show no fold lines; the diagram adds them in GUIDE.
- FiO 9.1 Q4(d): which edge of the folded strip is the fold is not printed; the arrow in the second panel (left half folded over to the right) and the printed answer (middle hole plus two side notches) give the left edge. Same reading for (a), (b), (c).
- FiO 9.1 Q4(a) wavy cut: vertices are approximate (read from a small picture).
- FiO 9.1 Q5(a) printed answer: the third panel shows only two tiny ticks, not a full cut square.
- The book's pinwheel (FiO 9.2 Q2): each blade is a lens with one straight edge on an axis and a curved edge; the curve is drawn as a circular arc of sagitta 0.15 of the blade length.
- Example 1 solution text says the strip is rotated clockwise; the diagram's turn arrow is clockwise.
