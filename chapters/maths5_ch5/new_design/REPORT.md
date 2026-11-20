# Class 5 Chapter 5, Far and Near: build report (local, placeholder route)

## 12 Nov 2026: tool phases removed

The tool write-ups no longer have Phase 1, Phase 2 and Phase 3. In `tools_*.py` the three "what the student does" entries are plain steps without a phase label, and the practice cards are named "Card N" or "Challenge" instead of "Phase N, card N". The same text is in the plan's tool_config, and Section C of `priority_doc.md` has one "What the student does" line per tool. Cards, book questions, feedback, hints and everything else are unchanged (the book's questions are still on the tool's cards). DESIGN.md and MEDIA_BRIEF.md still describe the older three-phase format; this note replaces it.


(Text written by the chapter helper and saved here by the lead session, because the helper could not write the file itself. The lead session re-checks every chapter's built plan afterwards.)

Built in `chapters/maths5_ch5/new_design/`. The helper subagents could not start (concurrent limit), so the chapter helper wrote everything itself. No upload; a live v1 exists on staging, this plan is v2.

## 1. Ids and files
- Maths Mela Class 5 Chapter 5, `textbooks/class-5/eemm105.pdf`, 13 PDF pages = printed 57 to 69 (the first page is an unnumbered opener, 57 by sequence). chapter_id `cbse_eng_maths5_ch5`, chapter_master_id 149, subject_ref_id 80, medium 1, publication 1, phase 2, media tag c5v.
- `check_master_id`: "MASTER IDS: clean". `set_version` found live max 1 and wrote version 2, plan_id `cbse_eng_maths5_ch5_v2`. No stamp (expected).
- Files: priority_doc.md, DESIGN.md, content.py, concept_plan.py, topics_1..3.py, tools_1..3.py, 33 media_specs, ch_latex_house.py, helper copies, built `cbse_eng_maths5_ch5.json`.
- Scripts, in scratchpad `/tmp/claude-1506/-root-maths-learning-plan/9dfc46bf-2f90-406d-86af-005a3698a5e2/scratchpad/c5ch5/`: verify_facts.py, check_numbers.py (unit-aware, 2,164 strings, 599 chains, 43 prose comparisons, 0 problems; tested on planted errors), measure_answers.py, sign_puzzle.py, gen_media_specs.py.

## 2. Counts
- 3 modules; 29 topics (13 authored: T1, T1B, T2 to T12, plus 16 "Questions:" topics); 125 concepts (33 authored, 92 question and answer); 30 objectives.
- 46 questions: 4 examples, 34 exercises, 8 prompts. 13 text and 2 talk ids stay in teaching text. 61 coverage ids, all attached.
- 66 videos: 1 hook, 19 concept (one is the sign puzzle video), 46 question. The summary has no video.
- 8 tools: Unit Picker (free try after the hook), Length Bars, Kilometre Track, Millimetre Ruler, Double Number Line, Length Columns, Cut and Share, Height Chart.
- 129 image nodes: 21 concept images (hook, 19 teaching concepts, summary), 46 question images, 62 solution cards (16 questions have a second card; 26 question cards carry a diagram). Every DOER has a no-image decision with a reason.

## 3. Gate state
- `build.py --placeholders`: "structure stage OK". Structure, coverage, skeleton, objectives, solution_content, latex_content, question_layout and the equation gate (508 chains, 0 failed) pass.
- `validate_local`: 132 failures, all "video_script_rules:" (per video: missing script keys, and no interaction point). Other families: 0. Chapter 2 had 118 for 59 videos, the same two per video. One advisory: coverage (question and answer concept both carry the id).
- Unit-aware numeric check: 599 chains, 0 problems.

## 4. Judgement calls and clashes
1. 8 tools, not 9 to 11, one per distinct objective. No tool for the train table, price line, estimates, sprout and walk activities, sign puzzle, or revision.
2. No recap video (pipeline): T12 is a text summary with concept checks. The framing topic holds only the hook and the free-try tool, so the concept videos come after the tool (T1B).
3. Question sets split by the book's own letters so answers fit 220 characters: statues Q2 into (a) to (d); conversions Q2 into (a)-(d), (e)-(i), (j)-(n); "circle the bigger length" into (a)-(d), (e)-(g); the three double number lines of Q1 into three.
4. Hands-on items (walk and count steps, sprout diary, three estimates, Measure Your Height) have worked sample answers on labelled practice values with "Your answer may differ". Values: 125 steps per 100 m (80 cm a step); tea shop 120 m, school gate 400 m, temple 1,600 m; sprout 3, 9, 16, 25 mm; floor 3 m x 5; friend 1 m 50 cm x 8; rope 7 m 50 cm; students 4 feet 3, 7 and 5 inches.
5. Kinds: printed solved examples are `example` (Examples 1 to 4: Saji, cable, shirts, price of 1 m). "Let Us ..." box items are `exercise`; untitled in-text tasks are `prompt`. The Note for the Teachers becomes the plan's own line on mental and column methods, with no teacher role.
6. Labels use the book's heading words, so "The World of Small Things" holds ruler marks, design, sprout and drawing; "Measuring Long Distances" holds the walk and ropes.
7. Heights are in words (4 feet 6 inches), no decimals, "half a metre" appears once (the 50 cm blank).
8. Gate trap: `eqcheck_plain` reads "18 km ÷ 3 = 6 km" as the chain "3 = 6" (false). Reworded to "divided by"; the gate was not touched. Length facts are not machine-checked beyond whole-number chains, so the helper checked all of them itself.
9. LaTeX quirks handled in ch_latex_house.py: blank before a unit, a lone unit in a sentence, "3 km 450 m" losing its space, article "a" before a number, bracketed sign list. Tight answers: sari.match 219/220, walk.steps 201.

## 5. Points the book leaves unclear, and the reading adopted
1. Opener unnumbered: page 57.
2. Let Us Find: the unit column holds numbers (42, 40, 50, 13, 2, 5). Read as the measure plus a unit to choose: 42 m, 40 cm, 50 m, 13 cm, 2 m, 5 cm. The well (50 m, since 50 cm deep is impossible) is the only doubtful one.
3. The table at the top of printed page 58 has no heading or instruction. Read as matching: 204 cm = 2 m 4 cm, 540 cm = 5 m 40 cm, 750 cm = 6 m 150 cm, 240 cm = 2 m 40 cm, 404 cm = 2 m 204 cm.
4. Kilometre Race: stop positions at the start and finish are not stated. Read: none at the start, the last at the finish line. So 6 water stations, 10 children, 60 flags (30 red, 30 blue; red first, counts independent of colour). A stop at the start would add one to each.
5. Train journey: the route starts at Dibrugarh (0 km); the gap between stations is the difference of distances; the route is 4,187 km. The book does not say this; the plan teaches it first.
6. Let Us Measure: no lengths printed. Eight lines measured on the PDF drawing at printed size (1 pt = 0.3528 mm): 48, 35, 60, 27, 22, 19, 44, 61 mm, each within 0.3 mm of a whole mm, which supports the printed-size assumption. A printed copy may be scaled, so the answer allows 1 mm. Lines are numbered 1 to 8 from top to bottom.
7. Anita's thread: 1 m of thread per 50 cm of border, so a 5 m border needs 10 m, costing ₹500.
8. The ruler pictures (pages 61, 68) are drawn about twice real size and the number lines are not to scale: only the count of 9 small marks is used. The child's height on page 69 is not stated. The QR code is unreadable.
9. The four long-distance tools are only named, no facts added.

## 6. Printed-book errors
1. Sign puzzle (page 69) says "each 4 x 4 box" but the grid is 4 by 4. Read as the four 2 x 2 boxes. Rows and columns alone give exactly one solution (checked over all grids) and it also has no repeat in any 2 x 2 box. The question card says 2 x 2.
2. Double number line (a), page 63: the last blank under 50 cm is printed with unit m, though every other blank on that line is mm. Answered 500 mm, noting 50 cm is also half a metre.
3. Minor: "1600 cm", "4625 cm" and "₹2000" are printed without a comma; the plan writes commas except in the cloth line, where ₹2000 is as printed.

## 7. Answers the book does not print, worked out by the helper
Only the four solved examples and the two margin cases (89 mm, 5,792 cm) are printed. Worked out: Let Us Find; the weaving-centre line and match; Let Us Compare Q1 and the statues (b: Statue of Liberty and The Motherland Calls, 2 m, checked over all 15 pairs; c: Statue of Unity and Christ the Redeemer, 144 m; d: The Motherland Calls, 91 m); the walk (sample); rope table; Kilometre Race; five train questions; ruler marks (9); the design; sprout (sample); lines to draw; the three number lines and 14 conversions; Rani 6 m; Bhopal to Sanchi 30 km 800 m; Gulmarg 4 km 950 m; the seven pairs; cloth line (₹200, ₹400, ₹800, 100 m; boxes x2, x20, x2, x20); Anita; road 2 km 100 m; estimates (samples); Measure Your Height (sample); sign puzzle (row 1 ÷ − × +, row 2 + × − ÷, row 3 − ÷ + ×, row 4 × + ÷ −).

## 8. Kit, cut-out and sheet assumptions
None. The chapter refers to no kit, cut-out or Learning Material Sheet, so the lead session's correction about the sheets in eemm115.pdf does not apply.

## 9. Decisions needed from the user
1. Confirm the readings in 5.2, 5.3, 5.4, 5.6, 5.7 and the printed-error readings in 6.1 and 6.2.
2. Confirm practice-value sample answers for the hands-on items, or say if any should become discussion prompts with no solution.
3. Confirm 8 tools (none for the sign puzzle or estimates) and the splits in 4.3.
4. A live v1 exists on staging; this plan is v2. Say whether and when to upload (not done).
5. The `eqcheck_plain` reading of "N unit ÷ k = v unit" (4.8) is a gate weakness; the helper left it unchanged.
