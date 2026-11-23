# Notes for chunk F (Class 6 Ch 2, topics M4.S29.T29 to M4.S33.T33)

Result: 30 items = required 15 (6 question, 9 solution), optional 1, none 14. Validator: errors 0, 2 warnings (both are solution
figures that the book does not print: 2.10 Q2 and 2.11 Q3 drawings). The specs were also drawn once with a throw-away matplotlib
script (kept outside HERE) to check geometry; nothing else was edited.

## 1. Judgement calls

- **Example 1 (C157 / C158).** Question none: it gives no figure (draw a 30 degree angle), the four steps are in the text, and the book's
  step pictures (ray IN, protractor placed, T marked) are procedure illustrations. Solution required (printed answer is Fig. 2.22, a drawing).
  I drew the finished angle only (ray IN, ray IT, T, arc, 30 degrees). The LP hint `s_figure` also mentions the protractor on the figure;
  I left the protractor out because it is process, not the final state (and the teaching images already show it). If you want the
  protractor in, it is a content change to this one spec.
- **Figure it Out 2.10 Q1 (C159 / C160).** Q required (Fig. 2.23). Solution none: the printed answer is a text list of ten angles; ten arcs
  on the figure would only repeat it.
- **Drawing answers (2.10 Q2, 2.11 Q3, and the M, Y and polygon answers).** Solution required for all (Step B2, sibling consistency). For
  2.10 Q2 and 2.11 Q3 the book prints no answer picture, so the solution figure is a sample drawing of all five angles from a horizontal base
  ray (as the LP steps say). The question side is none for all of them (no given figure). 195 degrees is drawn as 165 plus the long way round, as the LP steps say.
- **2.10 Q3 (C163 / C164): the angle HIJ.** Q required; the solution keeps the given angle in INK and adds a copy in ANSWER green, both labelled
  116 degrees. See section 2 for the 40 versus 116 problem. The question card is the left half of the solution card (same positions); crop it tightly.
- **2.11 Q1 (six dot grids, C169 / C170).** One combined diagram per side (the LP keeps one card). Layout is three columns (acute, obtuse, reflex pair)
  by two rows (book left grid on top, book right grid below), chosen so the 16:9 card is used and the dots stay legible; the book's own row layout
  would make each grid tiny. The letter A is not printed in the book; it is added at the start dot of the red segment because the question says "join A".
  The book's red lines are drawn in INK (given marks). The question is open-ended and the LP gives no concrete drawing, so I chose one sample answer per
  grid (listed in the spec and in `text_alternative`); `needs_lp_text_sync` is true on the solution.
- **2.11 Q2 (C171 / C172).** Q required. Solution none (text answer, four numbers on the existing arcs would only repeat the question figure).
  Contrast with Let's Explore, where the solution adds NEW arcs (BET, SET), so that solution is required.
- **2.11 Q4, angles a to f (C175 / C176).** Q required; the lowercase letters a to f are drawn (without a full stop) because the question and the answer
  refer to "angle a" ... "angle f". Solution none (the answer is a classification in words).
- **2.11 Q8, Ashoka Chakra (C183 / C184).** Question none (the book picture is the emblem, 24 is in the text, DECORATIVE_ONLY). Solution `optional`:
  a wheel with one 15 degree gap and the 75 degree angle would help but LaTeX is complete.
- **Worked examples C165, C166.** none (numbers only; each concept already has its own teaching image, not linked).
- **Figure inventory.** 34 entries (31 base + 3 NEW second uses: HIJ in its solution, the six grids in their solution, the Let's Explore figure in its
  solution). The 7 teaching examples of acute/obtuse/reflex angles (P38-shape-2..4, P39-shape-1..4) are mapped to the T31 concept images C165 / C166 as
  accounting only (the concept images teach the same idea with their own pictures). P35-ray-1, P35-protractor-1, P35-protractor-2 are mapped to
  concept image C153 (Drawing a 30 degree angle).
- **Overlap with chunk E.** Section 2.10 (pdf pages 35 and 36) is shared with topic T28. P35-* and P36-shape-1 may be claimed by chunk E as well. My mapping:
  P35-* to concept image C153, P36-shape-1 (Fig. 2.22) to item C158 (solution). If chunk E maps P36-shape-1 to concept image C153, the two entries are
  compatible in meaning (one figure used by a teaching image and by my item); please keep the item entry.

## 2. Things in the LP that look wrong

1. **2.10 Q3 solution (M4.S30.T30.C164).** The answer text says "about 40 degrees by eye from the picture". The picture is an obtuse angle of
   about 116 degrees (pixel measurement 116.3), and the same H, I, J figure is printed in Section 2.9 Figure it Out Q3, whose printed answer is
   angle IHJ = 116 degrees. The figure uses 116 degrees; the LP answer text needs the same correction.
2. **2.11 "Make any figure" (M4.S32.T32.C178).** The LP answer says "A six-sided figure (hexagon ABCDEF) works". The printed answer figure has 8 vertices (two
   unlabelled reflex dents between A and B and between B and C), and no hexagon can have three acute, one right and two obtuse angles (their sum stays
   below 720 degrees). The figure follows the printed picture; the text needs fixing.
3. **Example 1 (M4.S29.T29.C157).** The question text contains the whole worked solution (all four steps and "angle TIN = 30 degrees is the required
   angle"), so it gives the answer away and duplicates the answer card.
4. **2.10 Q2 (C161 / C162).** The question text repeats the five measures twice ("(a): 110 degrees; ... (e): 134 degrees. (a): 110 degrees; ...").
5. **2.10 Q1 answer.** The book answer lists angle CLP, but C, D and L are collinear in Fig. 2.23 (D lies between C and L), so CLP is the same angle as DLP.
   Copied from the book; harmless.
6. **Numbering.** The LP numbers the 2.11 Figure it Out as Q1 to Q9. The book has two sets: Q1, Q2 (pages 51 and 52), Let's Explore, then Q1 to Q7 (page 53 and 54).
   The printed solutions number the second set Q.3 to Q.7 and have no answer for the second set's Q1 and Q2 (draw angles, estimate angles) or for the first set's Q1 (dot grids).
7. **Let's Explore (C187).** The LP question text does not state that angle SER is 90 degrees; it is only in the figure (the LP solution says "SER = 90 degrees (shown)").
   The figure is therefore required on the question side.
8. **2.11 Q4 answer (C176).** "angle e is about a right angle (or slightly obtuse)": the picture measures about 97 degrees, so it is slightly obtuse; fine as written.

## 3. Places where the book itself is unclear

- Letter A is not printed on the six dot grids (taken as the start dot of the red segment); the book also prints no answer for them.
- Fig. 2.23 prints dots only on A, B, C, D; P, R, L and S are bare letters at the crossings. A small dot is added at every named point in the spec.
- Angles a to f of 2.11 Q2 (second set) carry no values; directions in the spec are pixel measurements (a 45.5, b 165.7, c 120.2, d 32.7, e 97.4 and f reflex 348.3 degrees marked).
- 2.10 Q3: the book prints no measure for the angle; 116 degrees comes from the picture and from the identical figure in Section 2.9 Q3's answer.
- Fig. 2.22 shows a ruler along IT; the spec drops the ruler (an object, not part of the angle).
- The printed polygon (page 53) shows two unlabelled reflex dents; the question only asks about the lettered angles, so they stay unmarked, as printed. The spec moves F by 0.03 so that E is exactly 90 degrees.
