# Class 5 Chapter 7, Shapes and Patterns: build report (local, placeholder route)

## 12 Nov 2026: tool phases removed

The tool write-ups no longer have Phase 1, Phase 2 and Phase 3. In `tools_*.py` the three "what the student does" entries are plain steps without a phase label, and the practice cards are named "Card N" or "Challenge" instead of "Phase N, card N". The same text is in the plan's tool_config, and Section C of `priority_doc.md` has one "What the student does" line per tool. Cards, book questions, feedback, hints and everything else are unchanged (the book's questions are still on the tool's cards). DESIGN.md and MEDIA_BRIEF.md still describe the older three-phase format; this note replaces it.


(Text written by the chapter helper and saved here by the lead session, because the helper could not write the file itself. The lead session re-checks every chapter's built plan afterwards.)

## 1. Ids and files
Folder `chapters/maths5_ch7/new_design/`; chapter_id `cbse_eng_maths5_ch7`; chapter_master_id 151; subject_ref_id 80; medium 1; publication 1; phase 2; media_tag c5j. Book `eemm107.pdf`, 12 PDF pages = printed 92 to 103; PDF page 1 is the unnumbered opener (it shows only the chapter number 7), page 92 by sequence. Plan: `cbse_eng_maths5_ch7.json`, version 2 (live max 1). No stamp (expected). Scratch scripts (weave pixel reads, piece search, tangram search, cube folding, numeric check): `/tmp/claude-1506/-root-maths-learning-plan/9dfc46bf-2f90-406d-86af-005a3698a5e2/scratchpad/c5ch7/`.

## 2. Counts
- 4 modules, 29 segments, 29 topics (13 authored + 16 Questions), 136 concepts (32 authored + 104 question and answer).
- Authored topics: T1 Weaving Mats (framing), T1B Describing a Weave, T2 Tiles Around a Point, T3 Patterns with More Than One Shape, T4 Triangles from the Rhombus, T5 Four-Sided Shapes from the Rhombus, T6 Tangram, T7 Which Shape Am I?, T8 Play with Circles, T9 Cube Connections, T10 Puzzle: Tanu's Shapes, T11 Icosahedron and Dodecahedron, T12 Chapter Revision (summary).
- Questions 52 (51 prompts, 1 exercise = Let Us Try; no solved example, no Let Us Do), 17 text ids, 69 coverage ids all covered.
- Videos 71: 1 hook, 17 concept + 1 puzzle, 52 question. No recap video.
- Tools 11: Mat Weaver (free try), Weave Rules, Fit Around a Point, Pattern Tiler, Triangle Check, Rhombus Pieces, Tangram Maker, Shape Detective, Circle Stitcher, Cube Lab, Solid Counter.
- Image placeholders 159: 20 concept images, 52 question cards (33 with a diagram), 87 solution cards (35 second cards).

## 3. Gate state
- `build.py --placeholders`: structure stage OK; structure, coverage, skeleton, objectives, solution_content, latex_content, question_layout all 0; equation gate 198 chains, 0 failed. `check_master_id`: MASTER IDS: clean. `validate_local`: 142 failures, every one `video_script_rules` (2 per video slot x 71 slots, no-beats and interaction_point messages of placeholder videos); no other family.
- Independent numeric check: all whole-number chains true (97 by the helper's script); every weave row, corner fit, piece construction (2, 3, 4 pieces; the helpers' step constructions rebuilt with shapely), tangram answer, grid kite and parallelogram, circle paths (29 and 17 lines), cube, frame and painted counts, net folding, both puzzles (unique) and solid counts recomputed; text scan of the built JSON clean (dashes, NCERT, textbook, page, banned words, `$$`, unbalanced `$`).

## 4. Judgement calls and clashes
1. 11 tools: the chapter is hands-on; Shape Detective is droppable.
2. No recap video: T12 is a text summary with concept checks.
3. The framing topic holds only the hook and the free try; the first concept video and the opener questions are in T1B (the concept video comes after the tool).
4. Kite folding (printed after Which Shape Am I?) sits in T5 with kites; the "are the triangles equilateral?" question stays with the tessellation patterns.
5. Questions-topic headings are the book's box names; where none exists the plan names them (Tessellation Patterns, Triangles from the Rhombus, Shapes from the Rhombus).
6. Small wording changes: "sample/provided at the end of the book" dropped (the tool supplies the piece); "Cut the equilateral triangle provided" becomes "Take an equilateral triangle"; "3-D shapes" becomes "solid shapes"; "(5-sided)" becomes ", 5-sided"; "creating a (a) 3-sided shape, (b)..." becomes "creating: (a) a 3-sided shape; ..." (the LaTeX converter garbled the originals); part labels carry a colon.
7. Practice values: 8 slit columns, ruler lengths 4/7/8 cm in Triangle Check, 12-point circle, 12-tile border, 4x4x4 painted cube, every WE.
8. Only Nisha and Tanu are named; the opener girl is unnamed, the hook has no character.
9. Non-book facts: icosa = 20, dodeca = 12; 30 edges each; 5 and 3 faces at a vertex; the cube as the "other solid".

## 5. The kit (after the lead session's correction)
The helper used the real sheets in `textbooks/class-5/eemm115.pdf`: PDF page 15 "Tessellation and Shapes" = a rhombus cut into 4 triangles, the tangram (same as the page), 6 each of regular pentagon, regular hexagon (each cut into 6 triangles), square, equilateral triangle, circle, all one side length; page 19 nets (icosahedron 20 triangles, dodecahedron 12 pentagons); page 12 square dotted grid; page 21 isometric dot grid. No octagon, paper strips, cube or cube frames on the sheets.
IMPORTANT: the sheet's rhombus measures 457 wide x 748 tall (1 : 1.64), the same drawing as the page; two equilateral triangles joined would be 1 : 1.73 (about 5 percent off). The helper kept the reading "two equilateral triangles joined" (Try This halves an equilateral triangle and calls the halves scalene; "each triangle has 2 equal sides" holds for the two triangles two pieces make; kite, A, B match). If the printed ratio is literal, two pieces joined along the longer short side give sides 1.92 : 1.92 : 2 (nearly equilateral) and "Is an equilateral triangle possible?" becomes "nearly". All rhombus answers depend on this. Please confirm.

## 6. Unclear points and readings
1. Rhombus size (section 5).
2. "Regular shapes" = equal sides, so the rhombus also qualifies; "regular" is used only for equilateral triangle, square, pentagon, hexagon, octagon.
3. "How many 4-sided shapes?": the book shows 3; whole-side joins of 2 pieces give 4 (kite, rectangle, 2 parallelograms); answer "at least 4".
4. "Types of triangles": 2 pieces make 2 types.
5. 3 pieces make 3-, 4-, 5-sided shapes; 4 pieces make rectangle, triangle, pentagon, hexagon, not square, not octagon (whole sides joined; max 6 sides).
6. Squares-and-triangles pattern: on the dot grid each triangle has two sides equal to a square side and a shorter third side, so isosceles not equilateral; 2 squares and 3 triangles meet at every marked point.
7. Which Shape Am I?: statement 4 is read to include the rhombus; answer (1) Rectangle; (2) Rhombus; (3) Rhombus, Parallelogram; (4) Parallelogram, Rhombus; (5) Square; (6) all four; (7) Square, Rectangle.
8. Circle diameters: always a rectangle; a square at right angles, called a special rectangle.
9. Tangram outlines are unscaled; sample answers of the same proportions were checked by computer (rectangle and parallelogram = 2 small + medium triangle; triangle = medium triangle; short-top long-bottom shape = medium triangle + parallelogram).
10. Let Us Try: the design is 21 x 21 squares, the printed dot grid has 24 columns but only 18 rows of dots (3 short); the plan describes the whole design (left and right halves match, top and bottom alike not identical).
11. Cube views: they fit one cube only if the cream cross face is on two opposite faces (a single cross face makes view 3 a mirror image; checked by folding); net: row of 4 = brown, circle, diamond, star; cross above and cross below the diamond square.
12. Cube frames: a square tunnel through each pair of opposite faces; removed 7, 32, 81.
13. Puzzle: "the square" is one of the two in each clue, "between" = directly between; one arrangement: circle, square, rectangle, triangle, square, triangle, hexagon.
14. Kite folding: corners A, B are the two corners next to the same end of the crease; the kite shows 4 triangles.
15. Weave pictures read cell by cell (over = colour on top): Q2 mat 8 columns x 8 rows; Q3 16 x 16 repeats after 4 rows; Q4 design 1 (16 columns) repeats after 6 rows, design 2 (11 columns) after 4 rows.
16. The circle design needs 29 lines to return to 1; the overlapping-circles picture = five equal circles, one in the middle, four centred on it at the ends of two perpendicular diameters (measured).
17. The QR code on the opener is unreadable; nothing taken from it.

## 7. Printed-book oddities
The rhombus is drawn off 60/120; the "regular shapes" definition does not exclude the rhombus; the Let Us Try grid is 3 rows short; the cube views are inconsistent with a single cross face; statements 3, 4, 6 of Which Shape Am I? fit several shapes and statement 2 ("all my angles are not") is read as "not all equal"; the kite-fold letters A and B are unplaced; no octagon on the sheet.

## 8. Answers the book does not print
The book prints no answer in this chapter; all 52 are the plan's own (DESIGN.md section 4), checked by computer where a count or construction. Open items carry "Sample answer" and "Your answer may differ".

## 9. Decisions needed
Confirm the rhombus reading and the answers that follow; confirm the cube-views reading; confirm Which Shape Am I? statement 4 and the separate square and rectangle names; confirm the tool count (11) or drop Shape Detective; a gate remark (not changed): video_script_rules wants an interaction point in every question video; 142 messages remain until scripts exist.
