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
