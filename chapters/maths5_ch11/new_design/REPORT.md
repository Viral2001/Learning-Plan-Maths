# Class 5 Chapter 11, Grandmother's Quilt: build report (local plan, placeholder route)

## 12 Nov 2026: tool phases removed

The tool write-ups no longer have Phase 1, Phase 2 and Phase 3. In `tools_*.py` the three "what the student does" entries are plain steps without a phase label, and the practice cards are named "Card N" or "Challenge" instead of "Phase N, card N". The same text is in the plan's tool_config, and Section C of `priority_doc.md` has one "What the student does" line per tool. Cards, book questions, feedback, hints and everything else are unchanged (the book's questions are still on the tool's cards). DESIGN.md and MEDIA_BRIEF.md still describe the older three-phase format; this note replaces it.


(Text written by the chapter helper and saved here by the lead session, because the helper could not write the file itself. The lead session re-checks every chapter's built plan afterwards.)

Nothing was uploaded, no git was run, and the helper touched only the chapter folder and its scratchpad subfolder. Folder: `chapters/maths5_ch11/new_design/`. Built plan: `cbse_eng_maths5_ch11.json`, version 2, plan_id `cbse_eng_maths5_ch11_v2` (the live max version is 1).

## Ids
- chapter_id `cbse_eng_maths5_ch11`, master id 213, subject 80, medium 1, publication 1, phase 2, media_tag c5k.
- Book: `eemm111.pdf`, 13 PDF pages = printed pages 142 to 154. PDF page 1 is the unnumbered opener (142 by sequence).
- The scaffold truncated the title to "Grandmother's"; config and content now say "Grandmother's Quilt" with a straight apostrophe.
- `check_master_id`: MASTER IDS: clean.

## Counts
- 3 modules; 9 authored topics (1 framing, 7 idea, 1 summary); 23 authored concepts.
- The built plan has 23 topics (9 authored + 14 Questions topics) and 93 concepts.
- Authored concepts: 1 hook, 1 try-it, 13 teaching (one WE each), 7 Practice, 1 summary.
- 35 book questions: 2 examples, 17 exercises, 16 prompts. 15 text ids. 50 coverage ids, 100% covered.
- 49 placeholder videos: 1 hook, 13 concept, 35 question.
- 6 tools: Quilt Lace (free try after the hook), Tile the Table, Grid Area, Shape Builder, Rectangle Maker, Perimeter 24 Game.
- 109 image placeholders: 15 concept images, 35 question cards, 59 solution cards. 28 question cards carry a diagram.
- The 8 tool and practice concepts carry no-image decisions with reasons.

## Gate state
- `build.py --placeholders` ends "structure stage OK". The only advisory is that 35 questions are mapped to more than one concept (question plus answer concept, as on Ch2). The repo gate checked 564 equations and none failed.
- `validate_local` gives 98 failures, all `video_script_rules`, no other family and no stamp. Grouped: 49 "missing keys", 35 exercise-video interaction_point, 13 worked-video interaction_point, 1 hook "shows a picture".
- The helper's own checks (scripts in the scratchpad c5ch11/):
  - verify_facts.py recomputes every figure fact from the grid cells counted off the page images; all pass.
  - numcheck.py re-checks every chain, comparison and "W by H ... area or perimeter" claim in all strings, tools, notes and media specs: 327 chains, 15 comparisons, 50 rectangle claims, 0 problems. The remaining number sentences were read by eye.
  - A scan of the built plan found no em or en dash, NCERT, "page N", "Fig.", banned word, digit-hyphen-digit, `$$` or unbalanced `$`.
  - `media_specs.check_all()` prints `[]`.

## Judgement calls and clashes
1. The helper tried to start 3 helper subagents and the platform refused (concurrent-subagent limit). It wrote every file itself.
2. The brief's revision video becomes the T8 text summary with short checks (no recap video in the pipeline).
3. Quilt Lace follows the hook directly, and the concept video "Perimeter: The Border of a Shape" is in T1B with the opener's questions. Quilt Lace does not use "perimeter" as taught.
4. 6 tools against the usual 9 to 11. The count follows the concepts; a tool for the missing side or a side in parts would only repeat Rectangle Maker.
5. Questions homed away from their book position:
   - LUD p.142 Q2 (draw rectangles of perimeter 26 and 18) is practised in T5, where "length + breadth is half the perimeter" is learnt.
   - The mats, Trisha, Let Us Explore Q1 and Q2, and LUD p.149 and p.150 are practised in T4 (area and perimeter differ).
6. Concepts added that the book only implies: Finding a Missing Side (p.153 Q5), A Side Given in Parts (Q6), and Counting the Outer Edges of Tiles (the labelled figures of p.154).
7. The Note for Teachers boxes are kept as coverage ids and no teacher has a role. The book's "Take the help of your teacher" in the classroom-floor question stays as printed.
8. Students never read: pentagon, polygon, diagonal ("cut from corner to corner"), formula ("rule"), textbook ("Maths textbooks" becomes "Maths books").
9. ch_latex_house.py:
   - A part label gets a colon only before a number.
   - fix_units puts the converter's reading of "square cm" and "square m" back as `\text{ square cm}` and `\text{ square m}`. Without it the build gave 100 advisory warnings. No gate or core file was changed.
10. The book's "cm square" (garden question) is written "square cm" everywhere.

## Points the book leaves unclear, and the reading adopted (to be confirmed)
1. The quilt has no numbers. Counted from the picture: 15 by 10 patches, patch side 1 unit, border 50 units. Green lace (50) is exact; red (40) and blue (25) are too short.
2. "Two coloured laces, how much of each?" does not say the split. Sample: 30 units for the two long sides and 20 for the two short sides (red 30, blue 20); any split that makes 50 and fits the reels is accepted.
3. LUD p.142 Q1's 5 cm shape is drawn as a bow-tie although all sides are equal. Read as 4 equal sides of 5 cm, so 20 cm. The shape with the 4 cm side has 5 sides, so 20 cm.
4. LUD p.142 Q2 is read as two rectangles for each perimeter. The answers are open (sample 8 by 5 and 10 by 3; 6 by 3 and 7 by 2).
5. "Which objects covered the region completely?" depends on the student's own table. Answer: all four are rectangles and rectangles tile; an exact fit depends on the table.
6. Counted from the pictures: rug 15 by 6 = 90; Table 1 has 5 by 2 squares each cut into 2 triangles, so 20; Table 3 has 8 squares; Table 4 has 12 rectangles; Table 2 has 8 circles with gaps.
7. The desk (p.144): grid squares are unit squares, 9 by 6 = 54. Blue squares 54; the green triangle is half a square, so 108; two red triangles make a 3 by 3 square and the desk holds 6 of them, so 12.
8. The mats (Q4): the patch size is not stated. The drawn patch equals a 1 cm grid square on the same pages, so a patch is 1 cm by 1 cm. Mat (a) 5 by 2: 10 patches, 10 square cm, perimeter 14 cm. Mat (b) 4 by 3: 12 patches, 12 square cm, perimeter 14 cm.
9. Palm, leaves, classroom floor and the table of objects use real objects, so there is no single answer, and the book does not say how to count a part square. The plan gives a method and a sample with practice values.
10. Gardens (p.145): an unlabelled pale strip is treated as part of neither garden. Garden A is 2 by 5 = 10 square cm, garden B is 4 by 3 = 12 square cm.
11. Let Us Explore counted cell by cell. Q1: shapes (a), (b), (c), (d), (f) have area 12 (perimeters 16, 18, 14, 14, 26); (e) has area 8 and perimeter 18. Q2: all five shapes have area 7; perimeters 12, 12, 16, 16, 16.
12. The patchwork figure puts "Length" under the 4-patch side and "Breadth" beside the 6-patch side, but the text says 6 is the length. The product is the same, and the plan follows the text.
13. The square of side 5 has no question sentence in the book; the plan adds "What are its area and its perimeter?". The book prints no example numbers, so the plan numbers the patchwork Example 1 and the square Example 2.
14. LUD p.152 Q2 has ten "___ cm" blanks. The plan asks length, breadth, area and perimeter: (a) 6 by 6, (b) 4 by 7, (c) 12 by 4, (d) 3 by 3, (e) 6 by 5.
15. LUD p.153 Q6 is not drawn to scale and has unnumbered dotted lines. Read as one rectangle 32 cm by (6 + 12) = 18 cm, area 576 square cm, checked by the two parts.
16. Let Us Play does not say what happens past 24 or whether tiles must touch along a whole edge. Plan: edge to edge as in the pictures, tiles not moved, exactly 24 wins, a notch tile touching 3 edges lowers the perimeter by 2. The pictures give 10 (4 tiles), 12 (5 tiles) and 24 (11 tiles).
17. The LUD on p.144 has no question number, and other boxes restart at Q1. The opener's QR code cannot be read; nothing is taken from it.

## Kit and sheet assumptions
None. The chapter refers to no Learning Material Sheet or kit. The only cut-out is the small square in the mats question, which the plan measures against the 1 cm grid on the same page. After the lead session's correction the helper looked at sheet 15 (Tessellation and Shapes in eemm115.pdf). It holds loose squares, triangles, circles, pentagons and hexagons, but the chapter never sends the student there, so the plan does not use it and no sheet assumption exists in `content.SOLUTION_NOTES`.

## Printed-book errors and oddities
- "of the size give below" in the mats question: corrected to "given below".
- The bow-tie shape for "all sides equal".
- The Length and Breadth words on the patchwork figure.
- "cm square" against "square cm".
- No question sentence for the square example.
- The Q6 figure is not to scale.
- No arithmetic error: 6 × 4 = 24, 5 × 5 = 25, 4 × 5 = 20 and the game's printed perimeters 10, 12, 24 all verify.

## Answers the book does not print (worked out and verified; DESIGN.md section 4)
- Opener: the lace tick, the two-laces sample, both equal-sided shapes (20 cm each).
- Tiles: rug 90; tables 20, 8, 12; the area sentences; the desk 108, 12, 54.
- Areas: A, B, C 12, 8, 10; the four comparison prompts; gardens 10, 12; mats; Trisha; Let Us Explore Q1 and Q2.
- Samples with practice values: palm, leaves, classroom floor, table of objects, same-area drawing, rectangles of perimeter 26 and 18.
- Square (a) and triangle (b) are both 9, so (a) is not less. The check of earlier examples holds.
- Rectangles and field: five shapes, field 1428 square m, garden breadth 4 m, figure 576 square cm.
- Game: the 4-tile perimeter 10, and a sample game to 24.
- The book prints only 24 (patchwork), 25 and 20 (square), and the game's 10, 12, 24.

## Decisions needed
- Confirm the quilt reading, the two-laces sample and the bow-tie reading (points 1 to 3).
- Confirm the desk answers and the 1 cm patch for the mats (points 7 and 8).
- Confirm the Let Us Play reading (point 16) and that 6 tools is acceptable against the usual 9 to 11.
- Confirm that LUD p.142 Q2 sits in T5 and the mats, Trisha, Let Us Explore and p.149/150 questions sit in T4.

## Files
- In the chapter folder: priority_doc.md (A to F), DESIGN.md, content.py, concept_plan.py, ch_latex_house.py, topics_1 to topics_3.py, tools_1 to tools_3.py, topics_common.py.
- Also: media_specs/*.json (23), media_specs.py, media_placeholders.py, cleanup_fields.py, server_ids.py, build.py, chapter.config.json, name_slots.json (Preetha, Adrit, Trisha; the grandmother is a kin word), book_rules.json.
- Worklists and plan: media_worklist.json, video_worklist.json, question_images_report.json, cbse_eng_maths5_ch11.json.
- Scaffold files: book/, lp_brief.md, lp_state.json, MEDIA_BRIEF.md, chapter.config.README.md.
- Scratch scripts are in `/tmp/claude-1506/-root-maths-learning-plan/9dfc46bf-2f90-406d-86af-005a3698a5e2/scratchpad/c5ch11/` (verify_facts.py, numcheck.py, gen_specs.py, figure extraction).
