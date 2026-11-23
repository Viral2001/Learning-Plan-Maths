# Chunk C notes (Class 6 Ch 9 "Symmetry", topics T15 to T20)

Result: 31 items (22 units): required 8 / optional 3 / none 20. Validator `--chunk C`: errors 0, warnings 0.

| Role | required | optional | none |
|---|---|---|---|
| worked_example (13) | C69, C73, C74, C78 | C66, C70, C71 | C67, C68, C72, C97, C98, C99 |
| question (9) | C76, C89 | - | C81, C83, C85, C87, C91, C93, C95 |
| solution (9) | C82, C90 | - | C77, C84, C86, C88, C92, C94, C96 |

Media ids: C69.IMG2 and C78.IMG2 (IMG1 is the kept teaching image of those concepts); C73.IMG1, C74.IMG1, C76.IMG1, C82.IMG1, C89.IMG1, C90.IMG1.
Geometry of every required figure was computed in code and previewed (matplotlib) against the page pictures before writing.

## 1. Judgement calls

Rule I used for the 13 worked examples (one diagram each): required only when the learner cannot follow the example without the picture
(labels that exist only in the figure, a picture that is the answer, a picture the question tells you to look at). Where the LP text already
gives all the data and the concept keeps its own teaching image, the item is optional or none.

- **C66 (4 radial arms, book's plus shape with dotted centre lines and a 90 degree arc): optional.** Text gives 4 equal arms, 90 degrees; the card keeps
  C66.IMG1. Caveat: the LP question says "the angle between adjacent central dotted lines", and those dotted lines exist only in the book's figure. If you want
  the phrase to have a referent, promote C66 to required (plus shape, band width 1/8 of length, dashed vertical and horizontal centre lines, 90 degree arc).
- **C70 (can 3 equal arms give 3 angles?): optional.** Answer is a rule ("3 equal arms 120 degrees apart"), the book prints no figure at that point.
  Figure that would help: three equal arms 120 degrees apart (same drawing as the left half of C73).
- **C71 (3 arms with unequal gaps): optional.** The words "angles not equal" give the answer. Figure that would help: the book's irregular 3-arm figure
  (gaps about 90, 155, 115 degrees, measured from the page, the book prints no values).
- **C69 required, although C69.IMG1 (kept) shows the same idea.** The book's answer is the picture "Here is one way" and the LP only describes it in words (v3 B2).
  Drawn as the final figure only (not the given plus shape): top arm bends right, bottom arm bends left, half-turn symmetric (checked in code).
- **C73 required.** The question and the steps use angles A, B, C that exist only as labels in the book's two rough diagrams (figure and rotated copy). One picture with both diagrams.
- **C74 required (the closest call).** The answer to "how many angles of rotation" is numeric, but the book's answer is the four-step coloured picture and the LP steps are its captions.
  If you prefer fewer images, drop it to optional; nothing else depends on it.
- **C72 none** (not optional): answer is a rule and the same card keeps C72.IMG1, which already shows gaps 100/120/140 changed to 120 each.
- **C76 question required; C77 solution none (SAME_AS_QUESTION_DIAGRAM).** The printed answer redraws the same six figures and only adds "order of symmetry = n"; the numbers stay in the answer text.
  All six figures are in ONE picture because the LP holds the whole question as one item. I kept the labels (a) to (f) in the picture because the question and the answer are keyed by them
  (the brief's "no figure letters" rule is meant for one-figure pictures). Remove them if you disagree.
- **C76 figure (a):** the book's lower flag is not an exact half turn of the upper flag (its tip hangs lower), but the book answers order 2. Drawn as an exact half-turn copy so the drawing really has order 2.
- **C76 figure (b):** the book marks only the top angle with an arc; strictly this breaks the 4-fold symmetry of the drawing, the book's answer (4) reads it as marking the right angle. Arc kept, no value written.
- **C76 figure (d):** the book's three hand-drawn arms with fists are redrawn as three identical bent bands with rounded-square fists, 120 degrees apart (stylised, simple). If a more faithful hand-drawn look is wanted, this one figure
  needs an illustrator or the image-model route.
- **C78 required** (pinwheel). Pinwheel built from 18 triangles of edge 1.5 (hexagon of 6, a rhombus of 2 on each of its 6 sides, all turned the same way, tilted 13 degrees as in the book), checked in code.
  Filled SET_A at 40 percent opacity because the LP text says "blue figure".
- **C81 question none, C82 solution required.** No question figure when the question only asks to draw. C82 shows both printed answer figures (5 wedge arms 72 apart, 6 lens petals 60 apart) in one picture with the angle marks 72 and 60
  (the LP steps' own numbers). Labels (a) and (b) kept for the same reason as in C76.
- **C89 question required, C90 solution required (derived_from C89).** C90 draws the LP solution (every 4th sector for 3 angles, every 3rd for 4 angles), NOT the book's printed pictures (see 3 below).
  The LP gives the rule, not the positions, so I picked sectors 1, 5, 9 and 1, 4, 7, 10 counting clockwise from the top; `needs_lp_text_sync: true` on C90 (the text could say "for example sectors 1, 5, 9").
- **C97, C98, C99 none.** C97: the book's rolling-wheel sketch is decoration, the answer is words. C98: no book figure. C99: open-ended "find objects"; the fan, flower, wheel pictures are examples
  (mapped to concept image C99.IMG1 in the inventory).
- **C83 to C88, C91 to C96 none/none:** numbers, true/false and yes/no answers; the book prints no figures for them.

Inventory choices: P16-radial_arms-3 and P17-shape-2 are mapped to the concept images C66.IMG1 / C72.IMG1 (accounting only; those drawings differ from the book's).
P01-pattern-4 (the chapter-opening pinwheel) is claimed here for C78. Chunk A (Figure it Out 9.1 Q1 "figures at the start of the chapter") may also use it:
at merge keep one meaning (item C78 here; the other use gets `NEW-P01-pattern-4-<suffix>` or none).

## 2. Things in the LP that look wrong

1. **Concept C78 "Five, six and seven arms"** actually holds the chapter-opening pinwheel question (ncert 9.1.q2), which belongs to the introduction, not to "Order and the Smallest Angle of Symmetry". Concept name and content do not match.
2. **C78.IMG1 description** says "a teal triangle on each of its 6 sides"; the book (and the LP answer) has a rhombus of two triangles on each side.
3. **C99 question text and its teaching image C99.IMG1 disagree with the book:** the book's flower has SIX petals (LP and image say five, "72 degrees"), the book's wheel has 23 spokes (image says 8 spokes, "45 degrees"). Fan = 3 blades is right.
4. **Printed answer to FiO 9.2 (second set) Q1 is wrong in the book** (solutions p.37): picture (i) shows 4 adjacent shaded sectors, (ii) shows 3 adjacent sectors; captions say 3 and (no number). A block of adjacent sectors has only the 360 degree angle of symmetry. The LP solution is right and is the one drawn.
   The book's (iii) says "12 angles of symmetry are possible"; the LP lists 1, 2, 3, 4, 6, 12 (the divisors of 12), which answers the question as asked.
5. **Book numbering in the LP restarts and repeats:** C76 is "Figure it Out 9.2, Q1" but is FiO (first set) Q3 (ncert 9.2.FiO1.Q3); C89, C91, C93, C95 are "Q1, Q2, Q3, Q4" but are FiO (second set) Q1, Q4, Q5, Q6. The "Q1" label also appears in chunk B's T14 and chunk D's T21.
6. **Duplicated text in questions:** C76, C81, C87, C89, C95 (and their solution copies) list the parts twice, once as a sentence and once as "a) ... b) ...". With the C76 picture added, the long word descriptions of the six figures in the C76 question are also redundant.
7. **C77 steps** justify only (a), (c), (d), (f); (b) and (e) appear only in the answer line.
8. **C73 question text** names angles A, B, C but does not define them (only the figure does); with the new picture they are defined.
9. **C66 question text** mentions "central dotted lines" that exist only in the book's figure (see judgement call above).

## 3. Where the book itself is unclear

- C74 figure: the book's arrows and colours turn ANTICLOCKWISE, while the book text for the strip example says "clockwise". Drawn anticlockwise as in the picture. Colours green, dark blue, red are drawn as ANSWER, SET_A, FOCUS.
- P17-shape-2 (the irregular 3-arm figure): the three gaps (about 90, 155, 115 degrees) are measured from the page picture, the book prints none.
- P18-shape-1/2: the book calls them "rough diagrams"; arms are drawn exactly 120 degrees apart and no angle value is written.
- The book's SOL34 figure (a) arms are drawn as long thin wedges with a flat end (about 5.2 times as long as wide); figure (b) as lens petals. Proportions taken from the solutions page picture.
