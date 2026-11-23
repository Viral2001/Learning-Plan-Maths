# Class 6 Ch 6 Perimeter and Area - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths6_ch6` v58 (taken from staging). Result: new V2 version v59 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (100 items from 60 units)
{"worked_example": {"none": 15, "optional": 1, "required": 4}, "question": {"none": 23, "required": 17}, "solution": {"none": 18, "required": 17, "optional": 5}}

Optional, NOT added: [('C4', 'worked_example'), ('C84', 'solution'), ('C103', 'solution'), ('C105', 'solution'), ('C107', 'solution'), ('C115', 'solution')]

needs_lp_text_sync: [('C53', 'question')]

## The 38 diagrams
| id | side | type |
|---|---|---|
| M1.S7.T7.C34.IMG1 | question | mensuration_figure |
| M1.S7.T7.C35.IMG1 | solution | mensuration_figure |
| M1.S7.T7.C36.IMG1 | question | mensuration_figure |
| M1.S7.T7.C37.IMG1 | solution | mensuration_figure |
| M1.S7.T7.C38.IMG1 | question | mensuration_figure |
| M1.S7.T7.C39.IMG1 | solution | mensuration_figure |
| M1.S9.T9.C43.IMG1 | question | mensuration_figure |
| M1.S9.T9.C45.IMG1 | question | mensuration_figure |
| M1.S9.T9.C46.IMG1 | solution | mensuration_figure |
| M1.S10.T10.C49.IMG1 | worked example | mensuration_figure |
| M1.S11.T11.C51.IMG1 | question | mensuration_figure |
| M1.S11.T11.C52.IMG1 | solution | mensuration_figure |
| M1.S11.T11.C53.IMG1 | question | mensuration_figure |
| M1.S11.T11.C54.IMG1 | solution | mensuration_figure |
| M2.S14.T14.C68.IMG1 | question | mensuration_figure |
| M2.S14.T14.C69.IMG1 | solution | mensuration_figure |
| M2.S15.T15.C70.IMG1 | worked example | other |
| M2.S15.T15.C71.IMG2 | worked example | other |
| M2.S16.T16.C73.IMG1 | question | mensuration_figure |
| M2.S16.T16.C74.IMG1 | solution | mensuration_figure |
| M2.S19.T19.C82.IMG1 | solution | mensuration_figure |
| M2.S19.T19.C85.IMG1 | question | geometry_figure |
| M2.S19.T19.C86.IMG1 | solution | geometry_figure |
| M2.S19.T19.C87.IMG1 | question | mensuration_figure |
| M2.S19.T19.C88.IMG1 | solution | mensuration_figure |
| M2.S19.T19.C89.IMG1 | question | mensuration_figure |
| M2.S19.T19.C90.IMG1 | solution | mensuration_figure |
| M2.S19.T19.C92.IMG1 | solution | mensuration_figure |
| M2.S19.T19.C93.IMG1 | question | cell_grid |
| M2.S19.T19.C94.IMG1 | solution | cell_grid |
| M2.S21.T21.C98.IMG1 | question | mensuration_figure |
| M2.S21.T21.C99.IMG1 | solution | mensuration_figure |
| M2.S21.T21.C100.IMG1 | question | mensuration_figure |
| M2.S21.T21.C101.IMG1 | solution | mensuration_figure |
| M2.S21.T21.C104.IMG1 | question | mensuration_figure |
| M2.S21.T21.C106.IMG1 | question | mensuration_figure |
| M3.S22.T22.C108.IMG1 | worked example | mensuration_figure |
| M3.S23.T23.C113.IMG1 | solution | mensuration_figure |

### Chunk A notes (from the decision agent)
# Chunk A notes (Class 6 Ch 6, topics M1.S2.T2, M1.S4.T4, M1.S5.T5, M1.S7.T7)

Result: 31 items (18 units). Required 6 / optional 1 / none 24. Validator: errors 0, 2 warnings (both are the Q3 solution diagrams: the book prints no answer for Q3 marking, so no base figure maps to them; this is expected).

Required diagrams (each question figure is what the book gives; each solution figure is the same figure plus the answer marks, `derived_from` the question figure):

| Item | Question id | Solution id |
|---|---|---|
| Matha Pachchi Q3 a-c (Akshi, outer track 70 m x 40 m) | M1.S7.T7.C34.IMG1 | M1.S7.T7.C35.IMG1 |
| Matha Pachchi Q3 d-f (Toshi, inner track 60 m x 30 m) | M1.S7.T7.C36.IMG1 | M1.S7.T7.C37.IMG1 |
| Deep Dive (two square tracks) | M1.S7.T7.C38.IMG1 | M1.S7.T7.C39.IMG1 |

## 1. Judgement calls

1. **C4 (rectangle ABCD, 12 cm x 8 cm) is `optional`, not `none`.** The steps name the sides AB, BC, CD, DA, which only the book figure defines, so a labelled rectangle would help. It is not needed: both lengths are in the text and the steps say which sides are equal. Not added. The square-frame (C5 block 0) and triangle (C5 block 1) worked examples are `none`: their steps use no vertex letters, so the difference from C4 is deliberate.
2. **Matha Pachchi Q1 and Q2 questions are `none` although the book prints the track figure next to them.** The LP text gives the track size and the number of rounds, so a careful student loses nothing. Their solutions are plain arithmetic.
3. **Q3 a-c and Q3 d-f questions are `required`.** The LP text does not say where the runner starts or which way she runs. Both are given only by the book figure: Start at the bottom-right corner of each track (the "Starting Point for Akshi / Toshi" pointers), running clockwise (arrows: left side up, top right, right side down, bottom left). Without them "30 m past the start" cannot be placed on the loop.
4. **One track per diagram.** The book figure holds both tracks; the LP questions are about one runner each (the LP `q_figure` hints say the same), so the Akshi diagram has only the 70 x 40 track and the Toshi diagram only the 60 x 30 track. Both entries map the same book figure: `P05-track_diagram-1` (Akshi) and `NEW-P05-track_diagram-1-q4` (Toshi).
5. **Dots every 10 m are kept in the question figures.** The book shows them (22 on the outer track, 18 on the inner); the 10 m spacing is not printed but follows from the labels (7 gaps = 70 m, 4 gaps = 40 m, 6 gaps = 60 m, 3 gaps = 30 m). All six answer points fall exactly on dots (Akshi (40,0), (10,0), (10,40); Toshi (0,10), (50,30), (10,30)).
6. **Solution marks are letters only (A, B, C / X, Y, Z / A, B), no distance tags and no route.** The LP gives the distances in text; the figure's job is the final marks. The Deep Dive solution matches the printed answer picture, which also shows only the two dots.
7. **Deep Dive geometry.** Drawn to scale and concentric (outer 150, inner 100, lane 25) although the printed picture is not to scale (inner about 0.55 of outer). Finishing pole placed at the exact middle of the bottom sides, as the text says; the printed pictures put it a little off-centre. The book draws the bottom red arrow inside the inner square; it is placed in the bottom lane here (same direction, right) so that it clearly applies to both tracks. The two flags are drawn in FOCUS (the book's orange and green are decoration, and green would clash with the ANSWER colour).
8. **P04 (farmer, rope field) and P03-scene-2 (Usha, park) are `none`, DECORATIVE_ONLY.** Both are cartoons with no measurement; the numbers and the "3 rounds" are in the LP text.
9. **Printed pictures of the rectangle, square and triangle (P01, P02, P03-shape-1) are `none:TEXT_SUFFICIENT`.** No concept image holds them and they carry only labels that the question text already states.
10. **Decorative figures not inventoried:** the chapter-opener strip of coloured shapes (pdf p.1), the girl at the tablecloth (pdf p.3, the lace example) and the girl in "Estimate and Verify" (pdf p.6). None carries mathematical content, so no `NEW-` entry was made.
11. **Figures NOT claimed by this chunk:** `P06-dot_grid-2` (the 9-unit triangle, "Estimate and Verify"), which belongs to topic M1.S8.T8 (Straight Units and Slanted Units), and `SOL26-shape-1`. I claimed only figures used by my own units.

## 2. Things in the LP that look wrong or thin

- **Question text of C34 and C36 omits the start corner and the direction** (clockwise). Only the figure carries them. If the figure fails to render, the question cannot be answered; consider adding "She starts at the bottom-right corner and runs clockwise" to the text.
- **Book printed answer Q1(c) says "breadth = 3cm"** (pdf p.23); the question is in metres. The LP says 3 m, which is right; LP wins.
- **The book's printed solutions give no answer at all for Q3 a-f** (marking A, B, C, X, Y, Z; and the number of full rounds). The LP answers (A 30 m, B 60 m, C 4 rounds and 120 m; X 70 m, Y 140 m, Z 5 rounds and 100 m) check out arithmetically, and the diagram positions follow from them.
- **LP numbering differs from the book's.** The `book_number` fields are descriptive titles, not numbers. LP "Perimeter Puzzles Q2" is book Q1c, LP "Q4" is book Q2, LP "Q6" is book Q4 and LP "Q7" is book Q6 (LP Q1, Q3 and Q5 match). LP "Round and Round the Track Q3" is book Q3 a-c, LP "Q4" is book Q3 d-f and LP "Q5" is the Deep Dive. The ncert_ref in the map names the book question, not the LP's number.
- **C39 (Deep Dive answer) had two old cards (IMG1, IMG2)** for a single printed answer picture; it now gets one solution diagram, `M1.S7.T7.C39.IMG1`.
- **C38/C39 wording check:** "B starts on the third side counted back from the flag, 125 m from the corner" means 125 m from the top-left corner (the corner reached coming back); the figure shows B on the top side, 25 m from the top-right corner. Same point, but a student may read "the corner" as the nearer one.
- C3 (definition) is a worked-example block with no figure of its own; its teaching image (two walks, one shape) stays untouched.

## 3. Places where the book itself is unclear

- The Matha Pachchi figure has a **white vertical line with a small green flag** across the bottom strip (about 20 m from the inner left corner). It is unlabelled and does not coincide with either "Starting Point" pointer. I treated the pointers (bottom-right corners) as the starts and left the line out.
- The 10 m dot spacing is inferred, not printed.
- The Deep Dive text says the flags are "in the center of one of the sides"; the printed figure and the printed answer picture put the pole slightly off centre, and the printed picture of B sits at about 80% along the outer top side (125 / 150 = 83% is the exact value). The diagram uses the exact values from the text and the printed answer (100 + 100 + 100 + 50 and 125 + 150 + 75).

## 4. Setup issues noticed (not part of my task)

- `map/in_B.json` and `map/in_C.json` are byte-identical (same units: M2.S18, M2.S19, M2.S21, M3.S22, M3.S23). Units of topics M1.S8.T8 to M2.S16.T16 (20 units: M1.S8, S9, S10, S11 and M2.S12, S13, S14, S15, S16) are in no chunk file, so a merged map checked with `--chunk all` would report them missing and leave their base figures unclaimed.

### Chunk B notes (from the decision agent)
# Chunk B notes (Class 6 Ch 6, units 19 to 38)

Result: 32 items, required 13 (6 question, 5 solution, 2 worked example), optional 0, none 19. Validator: errors 0, 5 warnings (the five required solution diagrams have no printed book picture to map to, which is expected: they are new final-state figures).

Checks I ran in code: the corner lists of the four dot-grid shapes reproduce the printed answers (8s+2d, 4s+6d, 12s+6d, 18s+6d for perimeter; 4, 9, 10, 11 for area, whole and half squares 3+2, 6+6, 7+6, 8+6 exactly as the LP solution says); the arrangements b, c, d have outline perimeters 28, 28, 26 and the 22 cm answer arrangement has 22; figure a of Q4 has area 28 and figure b has area 9, and my cuts tile each exactly (8+6+6+8, 5+2+2).

## 1. Judgement calls

- U19 (C41 block 0, perimeter of equilateral triangle ABC): none, TEXT_SUFFICIENT. The book's triangle has no lengths or marks, only A, B, C. The picture I considered as optional is a triangle with its equal sides marked; I did not call it "clearly helps".
- U20 (similarity of square and triangle): none, a word question.
- U21 (Akshi/Toshi triangle): question required. The book prints the triangle already coloured (top and left sides red, slanting side blue) in the question itself, so the question diagram carries that colouring (SET_B straight, SET_A slanted; the house palette has no red). Solution none, SAME_AS_QUESTION_DIAGRAM: it would only add the words 6s + 3d. This differs from U22 on purpose: in Q2 the book prints each shape in one colour, so the solution's straight/slanted colouring is new.
- U22 (four shapes, straight and diagonal units): question and solution both required. Solution marks every edge run in the two colours and writes the four results; counting 8 to 18 units from words alone is error-prone.
- U23 (regular polygons): question none (OPEN_ENDED, no figure in the book); solution none (the answer is a rule in words plus 6 x 5 = 30). A labelled hexagon would be "nice", not needed.
- U24 (T10 worked example, "this long strip"): required. I treated "this long strip" as a reference to the book's lettered arrangement a, and arrangements b, c, d are drawn in U25, so a is drawn too (sibling rule). I did not draw the uncut chit (4 cm by 6 cm with a dashed cut): the question text gives its size, the cut and the join.
- U25 (arrangements b, c, d): question required, solution required (join highlighted with its length, perimeters 28, 28, 26 under each). The diagram shows only the book's labels (2 cm, 2 cm, 2 cm, 3 cm); no letters b, c, d (the LP solution says "the L shape", "the T shape", "the last arrangement", which matches the left-to-right order).
- U26 (22 cm puzzle): question required although the book prints no figure beside it. Reason: "the two pieces" only means something through the book's cut chit and the question text never says they are each 6 cm by 2 cm (see section 2). The diagram is the two separate pieces with their sizes, nothing arranged. Flagged `needs_lp_text_sync`. Solution required (the answer IS an arrangement): the pieces slid so they touch along 5 cm. I chose horizontal pieces, lower one 1 cm to the right (outline 22); any arrangement with a 5 cm join is correct, the LP only says "slide one piece along the other".
- U27 to U32: none for all (text-only examples and questions, arithmetic answers). The book prints no figure for Example 3, Example 4 or Figure it Out Q1 to Q3.
- U33 (Q4, splitting figures a and b): the LP keeps Q4 as one question with one card, so ONE diagram holds both figures (left staircase, right arch). Solution required (ACTION_ON_FIGURE): dashed cuts and the area of each rectangle, with the cuts the LP describes.
- U34 (T15 worked example, "guess which has the larger area"): required. The learner cannot guess without the two outlines. They are freehand, so I traced them from the page (colour-segmented, simplified: 37 control points for the smooth curve, 17 corners for the jagged one) and kept their near-equal areas (curved about 1.1 times the spiky one). I considered NOT_RENDERABLE and rejected it: the guess needs "a curvy blob and a spiky leaf of about the same size", not an exact outline.
- U35 (four counting rules): none, the book gives the rules in words only.
- U36 (circle of diameter 3 on a graph sheet): none, OPEN_ENDED. The student draws it; no figure, no printed answer, and the count depends on the placement (section 2).
- U37 (why not circles): none, TEXT_SUFFICIENT + REUSES_CONCEPT_IMAGE. A "why" question; counts 42 and 44 are in the text; the same concept keeps the teaching image of the two packings (never linked).
- U38 (Counting Squares Q1): question required (same figure as U22's question, "same as M1.S9.T9.C45.IMG1"); solution required: whole squares shaded green, half squares orange, areas written. Same reason as U22 (solution adds exactly the counted squares).
- Colours: SET_B (orange) stands for the book's red straight units and SET_A (blue) for its blue slanted units, in U21, U22 and the key of U22/U38. Piece fill is CELL_FILL (the book's pale yellow has no token). All diagrams are 16:9; the 23 by 7 dot grid and the three arrangements are wide strips scaled to the card width.
- Inventory choices: P08-shape-1 (the uncut chit) is mapped to U26's question because that diagram shows the chit's two halves; P11-tangram-1 is used by no LP item (the LP leaves the tangram Figure it Out out) and sits between my units p.10 and p.12, so I claimed it as none:OPEN_ENDED only so it is accounted for. If chunk C or the merge already claims it, keep either.

## 2. Things in the LP that look wrong or thin

- M1.S11.T11.C51 and C53 (Split and Rejoin Q1, Q2): the question texts do not give the piece size (6 cm by 2 cm); it lives only in the earlier worked example and the book figure. Suggest adding "each 6 cm by 2 cm" to both question texts. For Q2 my question diagram carries the sizes and the item is flagged `needs_lp_text_sync`.
- M2.S14.T14.C64 and C66: the book order is Q1 garden width, Q2 tiling cost, Q3 coconut grove. The LP names C64 "Q2" (it is the coconut grove, book Q3) and C66 "Q3" (it is the tiling cost, ncert_ref p10.q2, book Q2), and C66's `book_number` says "Covering a Region, Q3" for the book's Q2. The LP order (coconut first, then tiling) is not the book order. Harmless for images; matters if anything is matched by number.
- M2.S14.T14.C69 solution text says "Figure a" and "Figure b"; my diagram has no letters (figure letters are never drawn). Suggest "the staircase figure (left)" and "the arch figure (right)" in that text, or leave as is, since the shapes are described.
- M2.S15.T15.C71 block 0 (circle of diameter 3): the LP answer "about 7 square units" is not forced by the half-square rule. I counted: centred on a grid point gives 4, centred in a cell gives 9, other placements give 6, 7 or 8. The true area is pi x 1.5^2 = 7.07. The book prints no answer for this Let's Explore. Worth rewording as "about 7 (it depends where you place the circle; the true area is about 7.07)".
- M2.S15.T15.C70 block 0 ("guess which is larger"): the LP answer "A guess, settled by counting squares" does not say which is larger; on the page the curved outline is slightly larger (about 1.1 times). Information only.
- The printed solutions (pdf pages 23 to 29) have NO answer for the whole "Split and rejoin" page (arrangement a 28 cm, b, c, d, the 22 cm puzzle). The LP values 28, 28, 26 and "join along 5 cm" are therefore the LP's own; I checked them geometrically and they are right.
- M1.S9.T9.C44 (Q1 solution): the LP reasons by laying a straight unit on a slanted unit; the printed answer reasons "a diagonal of a square is longer than its side". Same conclusion, no conflict.

## 3. Where the book itself is unclear

- P08-shape-1 (the chit) draws a thin wedge-shaped notch beside the dashed cut line, apparently the cut being started; its size is not given. Not drawn.
- Arrangements b, c, d print no piece lengths (only 2 cm, 2 cm, 2 cm and 3 cm); the 6 cm lengths are inferred from the proportions and from the 6 cm by 4 cm chit.
- Figure a of Q4 prints eight labels; two sides (top 2, right 4) are unlabelled and follow from the others (bottom 3 + 4 = top 2 + 3 + 2 = 7; left 4 + 2 + 1 = right 4 + 3 = 7). The question diagram leaves them unlabelled, as printed.
- The freehand shapes of p.140 have no measures at all; any redraw is approximate.
- P11 tangram: eight questions on the printed page, none of them in the LP.

### Chunk C notes (from the decision agent)
# Notes for chunk C (Class 6 Ch 6, topics M2.S18.T18, M2.S19.T19, M2.S21.T21, M3.S22.T22, M3.S23.T23)

Result: 22 units, 37 items: required 18 (8 question, 9 solution, 1 worked example), optional 5 (all solution side, not added), none 14. Validator: errors 0, 3 warnings (the three required items whose figure is not printed in the book: C82, C108 block 3, C113).

## 1. Judgement calls

Combined pictures (forced by "one question diagram and one solution diagram per pair")
- C89/C90 (five figures on the grid): ONE picture with all five outlines on the book's shared 24 by 21 grid. The figures carry NO letters (prompt section 4 forbids figure letters). The LP text calls them "first ... fifth", which matches reading order (top row left to right: 3 figures, bottom row left to right: 2 figures). If the team prefers letters a to e in the picture, the LP text should be switched to "figure a ... e" and the spec changed.
- C106/C107 (area mazes b, c, d): ONE picture with three drawings left to right (second, third, fourth maze), no letters. Each keeps the book's printed numbers and the shaded unknown. Splitting the card into three concepts would give three cleaner pictures; not done here (the brief says one diagram per pair).

Question diagrams that differ on purpose from the book picture
- C87 (grid ABCD): the book also prints F, the grid line EF and green/orange shading of AFED and BFEC. The LP solution introduces F and EF as its own first step ("Drop a line from E straight down to F"), so F, EF and the shading are in the SOLUTION diagram only. The question diagram keeps the grid, A B C D E, blue triangle BAD (SET_A) and red triangle ABE (FOCUS). If you want the book picture exactly, move F/EF/shading into the question diagram.
- C93 (new square): the book's dashed arrow (new square pointing at the corner cell that gives "stays 24") is left out; the LP question does not say "as shown" and the arrow would give away one of the three answers. The loose square is kept, outside the grid. The grid is cropped to 9 by 8 cells.
- Colours that are named in the text map to the nearest token: blue = SET_A, yellow = SET_B (it is amber), red = FOCUS (it is pink). Rooms/shapes have no fills except where the book colours something that the text names or marks an unknown (MARK_FILL).
- C98/C100 plans: only the printed labels are drawn, blanks as underscores; Utility and Entrance labels of Sharan's plan are written horizontally (the book rotates them).

Solution side
- C82 (rectangles of area 24): REQUIRED, ANSWER_IS_FIGURE (the task is "make as many rectangles as you can", the answer is the set of rectangles). Only the area-24 set is drawn (four rectangles, perimeters 50, 28, 22, 20, greatest and least marked). The area-32 set (E1) and the general prediction (E2) stay as text, since a pair gets one solution diagram.
- C84 (diagonal cut): OPTIONAL, not added. The text (6 x 4 = 24, 24 / 2 = 12) is complete and the teaching image C78.IMG1 already shows the idea. The question has no figure in the book, so no question diagram.
- C86 (blue rectangle / yellow triangle): REQUIRED. The solution argues from the picture; the figure adds two dashed 4 by 3 rectangles around the halves of the yellow triangle, right-angle marks and a half mark in each of the four triangles.
- C88 (grid): REQUIRED, because the solution adds point F, the line EF and the areas 6 and 4 that do not exist in the question figure (prompt Step E would call this "optional if the solution splits the shape"; I chose required because the new point makes the LP steps unfollowable without it). The three totals sit in a small key to the right so they do not collide with the grid.
- C90 (five figures): REQUIRED. The dividing lines and the five areas are the answer (the book prints only the numbers).
- C92 (nine unit squares): REQUIRED: the printed answer to "make a figure with a perimeter of 18" is a picture (SOL26-shape-1). The diagram draws the LP's three arrangements (3 by 3 = 12, row of 9 = 20, row of 7 with 2 on its left end = 18) from the LP's own s_figure. The 18-unit figure is NOT the printed picture (that one has rows 2, 4, 3); both are valid, LP wins. The book's second teaching figure P17-shape-2 (C shape, perimeter 20) is not drawn: no question or answer of the chunk shows it; I mapped it to none:TEXT_SUFFICIENT because it is not a plan concept image and no other chunk has a topic on page 17.
- C94 (square attached): REQUIRED, ANSWER_IS_FIGURE + ACTION_ON_FIGURE: three new squares (flat side 26, corner touching 2 sides 24, slot touching 3 sides 22) with the perimeter written in each. The loose square of the question diagram is not repeated. Checked by code: base figure perimeter 24; new squares give 26, 24, 22 and do not touch each other.
- C99/C101 (houses): REQUIRED, the answer is the completed plan. The solution diagram also gets the missing outer dimension (35 ft / 25 ft) and the total 1,050 sq ft because the card's second item asks for the whole area.
- C103 (compare houses) OPTIONAL: two outlines 35 x 30 and 42 x 25 on one scale would help, but 1050 against 1050 and 130 against 134 are complete in text.
- C105, C107 (area mazes) OPTIONAL: the printed answers are numbers; a maze with the derived sides filled in would help but only restates the question figure with values. Same decision for all four mazes (sibling consistency), question side required.
- C113 (shapes A and B) REQUIRED: "draw two such shapes" has a drawn answer; the LP's pair (A = 18 x 1, B = 5 x 4) is drawn to scale with area and perimeter tags. Question side none (no given figure).
- C115 (folded square) OPTIONAL: a square cut into two 10 x 5 rectangles with the new edges marked would help; the numeric example in text is complete.
- C111 (lawn): none, pure arithmetic. C110 question none: the book prints no figure.

Worked examples in M3.S22.T22.C108
- block 3 (book Q7, rectangle 12 x 8 with a half-area rectangle inside): REQUIRED, add_new_image: the example is a drawing task whose answer is the pair of rectangles; the book only says "draw the rectangles accordingly". The picture shows the finished drawing (outer 12 x 8, inner 8 x 6 from the LP step), so the token after the question text shows the answer before the steps: that is how the worked-example slot works in v3, but say so if the team does not want the answer visible there.
- block 4 (book Q6, border on your own page): none, OPEN_ENDED. The answer depends on the child's page ("never quote one perimeter"); no fixed figure. This is the only "draw" item left without a picture; the reason is that no size is fixed.
- blocks 0, 1, 2 (book Q1, Q2, Q3): none, arithmetic, no printed figure. C79 block 0 (conclusion sentence) and C109 (summary): none, text.

Inventory accounting
- P13-pattern-1/2 (circles in the rectangle, concept image M2.S15.T15.C71.IMG1) are claimed by chunk B (units p13.circle, p13.why_squares), not here. SOL24-shape-1 (Deep Dive) belongs to chunk A.
- Where a solution diagram redraws a book picture I added a `NEW-<base id>-sol` entry (11 entries) so the figure count per use is honest.

## 2. Things in the LP that look wrong or thin

- C114 question text (M3.S23.T23.C114) lacks the four statements a to d of the book; the answer ("the perimeters added are 1 1/2 times the square's") makes no sense to a learner who has never seen the options. The LP text needs the four statements (text sync, not an image matter).
- C99 vs the printed solution: the LP gives the hall as an L shape of 265 sq ft (20 x 12 = 240 plus a 5 x 5 strip under the toilet = 25); the printed solution says 240. The book's own plan does draw the L shape and 225 + 50 + 180 + 180 + 45 + 265 + 60 + 45 = 1050 = 35 x 30 confirms the LP. LP wins; drawn as L shape with 265.
- The unit ncert_refs are loose: C110's unit lists p21.q4 and p21.q7, C112's lists p21.q5 and p21.q6, but the cards hold q4 and q5 only; q7 and q6 are worked blocks of C108 (their video ids point to T23 videos C111 and C113). Harmless, but the numbering is confusing: LP "Pulling It Together Q1, Q2, Q3" are book Q4, Q5, Q8; book Q1, Q2, Q3, Q7, Q6 are worked blocks.
- C83 hint q_figure ("a rectangle with one diagonal") describes a figure the book does not print; the book question has no figure.
- C85/C86: the plan's own teaching note (C78) records a doubt that the book's answer list says "triangle = half of the rectangle". Measured on the printed picture the yellow triangle has the same height and twice the width of the blue rectangle, so the areas are equal; the LP solution (same area) and my diagrams follow the figure.
- The book's text extraction of page 18 puts "(15 ft x __ ft)" under Hall; in the picture it belongs to the Small Bedroom (Hall has only "Area = __").
- C98 solution step 6: the sentence "gap of 5 ft by 5 ft under the toilet also belongs to the hall" is right, but the diagram label for that part is just "5 × 5".

## 3. Where the book itself is unclear

- p13 "Let's Explore" (rectangles of area 24): no figure is printed and the printed solutions (pdf p.26) give no answer at all under "Let's Explore! Page No. 141". The LP answer (four rectangles, 50/28/22/20; 66/36/24 for 32) is the LP's own and checks out.
- p14 blue rectangle and yellow triangle: no numbers. Sizes are measured from the picture (rectangle about 4:3, triangle base about twice the width, equal height).
- p16 figures a to e: no lengths printed; corners read from the page picture on the 24 x 21 grid and checked: shoelace areas 24, 30, 48, 16, 12 match the printed answers and the LP pieces add to them.
- p17 tricky grid: the arrow tip lies between cells; read as pointing at the cell right of the vertical bar's neighbour in the horizontal bar (the corner cell). The loose square is drawn slightly off the grid in the book.
- p18/p19 plans: only "30 ft" (Charan) and "42 ft" (Sharan) are printed; every other length is measured from the picture (about 17.6 px and 16.55 px per ft) and agrees exactly with the LP's derived sizes (checked: the rooms tile the plot with no gap or overlap, 1050 sq ft each).
- p20 maze c: the printed 6 cm arrow is visibly shorter than 6/15 of the 15 cm arrow, so the book picture is not to scale. The diagram uses the sizes the printed numbers imply (widths 4, 7, 12; heights 4, 6, 5; total 15).
- Printed solutions: Q6 of "Pulling It Together" (the border) has no printed answer (pdf p.29 goes from Q5 to Q7).
