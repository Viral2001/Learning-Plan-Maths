# Report: Class 5 Chapter 14, Maps and Locations (local plan, placeholder route)

## 12 Nov 2026: tool phases removed

The tool write-ups no longer have Phase 1, Phase 2 and Phase 3. In `tools_*.py` the three "what the student does" entries are plain steps without a phase label, and the practice cards are named "Card N" or "Challenge" instead of "Phase N, card N". The same text is in the plan's tool_config, and Section C of `priority_doc.md` has one "What the student does" line per tool. Cards, book questions, feedback, hints and everything else are unchanged (the book's questions are still on the tool's cards). DESIGN.md and MEDIA_BRIEF.md still describe the older three-phase format; this note replaces it.


(Text written by the chapter helper and saved here by the lead session, because the helper could not write the file itself. The lead session re-checks every chapter's built plan afterwards.)

Chapter folder: `chapters/maths5_ch14/new_design/`. Source: `textbooks/class-5/eemm114.pdf` (8 PDF pages = printed pages 171 to 178; the first page is the unnumbered opener, page 171 by sequence).
Ids: chapter_id `cbse_eng_maths5_ch14`, chapter_master_id 210, subject_ref_id 80, medium 1, publication 1, phase 2, media_tag c5s. `core/check_master_id.py` says "MASTER IDS: clean" (live name "Maps and Locations"). Nothing uploaded, no git, nothing touched outside this folder and the helper's scratchpad c5ch14. `core/set_version.py` set version 2, plan_id `cbse_eng_maths5_ch14_v2` (live max for this chapter is 1).

## 1. What was built
- 3 modules (M1 Directions and Pictures, M2 Street Maps, Metro Maps and Keys, M3 Grids, Distances and Positions).
- 9 authored topics (T1 framing, T1B, T2 to T7 idea topics, T8 summary), 22 authored concepts. Built plan: 22 topics (those 9 plus 13 "Questions: ..." topics) and 86 concepts (22 plus a question and an answer concept for each of the 32 book questions).
- Book questions: 32 = 2 solved examples (Example 1 the ant and the laddoos, Example 2 reaching the panda), 4 exercises (Let Us Do school map, zoo questions 1, 2, 3), 26 answerable prompts. 48 coverage ids (13 text, 3 talk, 32 questions). Coverage gate 0 problems.
- Videos (all placeholders): 45 = 1 hook + 12 concept (one per teaching concept) + 32 question videos.
- Tools (6, manipulative specs): Face the Rising Sun (free try in the framing topic), Direction Clues, Bus Route Driver, Metro Route Planner, Ant Path, Zoo Grid Locator.
- Image placeholders: 14 concept images (hook, T1B, T2 x2, T3 x2, T4 x2, T5, T6 x2, T7 x2, summary), 32 question cards (all with a diagram), 59 solution cards (27 questions have a second solution card). Image decisions with reasons for the 8 Practice and free-try concepts. `media_specs.check_all()` prints `[]`.
- Files: priority_doc.md (A to F), DESIGN.md, content.py, concept_plan.py, topics_1..3.py, tools_1..3.py, media_specs/ (22 files), name_slots.json (9 book names; unnamed characters noted), book_rules.json, ch_latex_house.py, copied helpers (build.py, cleanup_fields.py, server_ids.py, media_placeholders.py with DOC_PURPOSE for the 13 teaching videos, media_specs.py, topics_common.py), chapter.config.json, built plan JSON, media_worklist.json, video_worklist.json, question_images_report.json.

## 2. Gate state
- `build.py --placeholders` ends "structure stage OK": structure, equations (72 chains, 0 false), coverage, skeleton, objectives, solution_content, latex_content, question_layout all 0 problems.
- `validation/validate_local.py`: 90 failures, grouped: video_script_rules 90, every other family 0 (expected placeholder-video messages: 45 video slots x 2; Ch2 had 118). No stamp, as expected.
- Independent numeric check (scratchpad c5ch14/final_numeric_check.py, facts in verify_facts.py): 1,804 strings read; 57 whole-number sums, 40 turn and hand claims, every position pair (24 distinct, all inside the 12 by 12 grid) against animal and dot positions, 61 animal-position claims, 24 dot claims, 27 east-then-north walks, 201 ant legs, 37 station-count claims (Routes A, B, C recomputed from segment counts), grid sizes, tent counts: 0 problems (two early flags were false positives of the checker's patterns, fixed in the checker). The built plan has no `$$`, no unbalanced `$`, longest displayed answer 173 LaTeX characters (cap 220).

## 3. Judgement calls and clashes
1. Revision video: the brief asks for one; the pipeline has none, so T8 is a text summary with short checks.
2. One-video framing topic, tool before concept: T1 holds only the hook and the free-try tool; the first concept video and Manu's questions are in T1B. The tool's Phase 3 asks Manu's lines as an open challenge.
3. Six tools, not 9 to 11 (the brief fixes no number). No tool for the Let Us Do school map (a paper drawing; the key idea is met on the metro map) nor for the revision.
4. "Your own room": practised with Direction Clues on the book's room; the two own-room questions are open with a labelled sample answer.
5. The book prints no "Example N" headings; the two printed worked parts (ant to the laddoos, walk to the panda) are labelled Example 1 and 2, and their question cards do not contain the answer.
6. Question headings: labels sharing a heading share a Questions topic. "Answer the Following" (the book's words) was refused by the solution_content gate (the word "Answer" in a question card is hint-shaped), so it is "Zoo Grid Questions".
7. The worked examples of T3.C1, T4.C1, T4.C2 use the book's street and metro maps (a figure, not a book question): what is south of the Basketball Court, the Hauz Khas capsule, Hauz Khas to Kalkaji Mandir to Badarpur (4, 1, 6 stations). The giraffe at (8,9) is the plan's own zoo example. Playground, room plan, library corner and berry grids are plan practice values.
8. The three Notes for Teachers are kept as talk items inside teaching lines; no teacher role. The plan does not say how birds find their way (the book does not).
9. Only the four directions are used anywhere (a helper's "garden in the south west" became "near the south wall on the west side").
10. Tool 2's compass cross splits the picture into four zones along the diagonals (the plan's way to decide "north of"; the book states no rule).
11. Tool 1 has a practice card (face north: right hand east, left hand west) to show the directions stay put and only the hands turn; the book does not say this in words.
12. LaTeX: "Stop 1(S1)" is shown "Stop 1 (S1)" with S1 as a small maths label; "(right/left)", "station(s)", "route(s)" kept as printed; a blank followed by "cm" shows the unit as text (ch_latex_house.py, a chapter copy of the Ch2 house module).

## 4. Points the book leaves unclear, and the reading adopted (full list: priority_doc.md A6)
1. Room picture in perspective with a compass beside it: up the picture is north (back wall), right east, left west. Window north, bed east, cupboard west (a little behind the girl), bedside table south (the round table beside the bed; the dressing table with the mirror is not the bedside table). Cupboard and table sit between two directions, so the answer is a "Sample answer" with "Your answer may differ".
2. Bird Watching: west of the road = the tent left of the road (blue); closest to the lake = the tent just above it (green); north of the green tent = the tent near the top (purple); south of the lake = the tent below it (yellow); a tent east of the lake may be drawn anywhere right of the lake.
3. Own room and names in the four directions depend on the student: labelled sample answer from a sample room of the plan's own.
4. Street map route: extra red dashes near the parking area are not described in the text and the left road has no name; only the text's route is used (north, right turn onto Hospital Road driving east to Stop 1; right turn onto Park Road driving south to Stop 2).
5. (a) houses east of Jaideep's: Prem's and Raju's (across Park Road; neither exactly level). (b), (d): many routes right, one sample each. (c) Stop 1, judged from the picture (no distances printed). (d) the nearest stop is Stop 1. (e) south (Stop 2 is below Prem's house, a little to the left).
6. Metro map: counts are the circles drawn between two stations (a capsule counts one, the two ends not counted); not every station is named. Route A (Yellow to Rajiv Chowk, Blue to Supreme Court) 14 between, 1 change; Route B (Yellow to INA, Pink to Mayur Vihar, Blue) 15, 2 changes; Route C (Yellow to Hauz Khas, Magenta to Botanical Garden, Blue) 25, 2 changes. Also counted, not used: Yellow to Hauz Khas, Magenta west to Janakpuri West, Blue (31); Yellow to Central Secretariat, Violet, Pink, Blue (21).
7. Lali's suggestion: change again at Botanical Garden (Magenta meets Blue); the other way along Magenta meets Blue at Janakpuri West, longer (31 against 25), and is mentioned.
8. "Least number of stations" = Route A of those listed (no route on the map is shorter). "Best way" is an opinion: sample answer Route A.
9. Lines that cross without a capsule (for example Airport Express and Magenta) give no change; the book does not say it, the plan reads it from the key.
10. Ant grid: "dotted lines on the grid" read as the grid lines; the grid is 11 by 11 squares of 1 cm. The apple is 3 cm east and 3 cm south of the ant; the book's drawn route is 5 + 3 + 2 = 10 cm; the shortest routes are 6 cm (20 orders of 3 east and 3 south).
11. Zoo grid: numbers belong to the grid lines; positions are (column,row), east first; the panda (1,1) and tortoise (4,1) printed by the book were used to check the reading of every other position.
12. Animal names the book does not print, from the picture: toucan (11,11), tiger (2,6), flamingo (3,10), monkey (11,3), zebra (10,9), snake (1,4). "Deer" = the slim antelope-like animal at (10,6). Not asked: giraffe (8,9), big cat (8,7), hippo (6,8), parrot (1,11).
13. "Which way is west?" has no blank: answered as behind Manu, opposite to the rising Sun.
14. The book's sample school map has a small square near the lower right corner with no symbol in its key (not described). The QR code on the opener is unreadable; nothing taken from it.

## 5. Kit and sheet assumptions
None. The chapter refers to no kit, cut-out, token or Learning Material Sheet (the ant grid and zoo grid are printed in the chapter). The lead session's correction about the sheets in eemm115.pdf was read; it does not apply here.

## 6. Printed-book errors and oddities
- Zoo Q3 prints "(3,8 (Orange)" (missing bracket) and "(6, 6)" (space); the plan prints (3,8) and (6,6).
- Ant part (a) is printed already answered ("2 cm towards the east"); the plan makes it Example 1.
- "which way is west?" is a plain line with no blank.

## 7. Answers the book does not print (worked out by the plan)
Manu's blanks and "which way is west"; tent colours and the tent east of the lake; the room directions; sample answers for own room and school map; the two bus-route blanks and (a) to (e); every metro answer; the ant's (b), (c), (d) and the other routes with the shortest; the zoo walk to the tortoise, what is at (1,4) (a snake), questions 1 to 3. The book prints only the ant's (a), the panda at (1,1) and the tortoise at (4,1).

## 8. Needs a decision from the user
1. Confirm the metro counting rule (circles between the ends, capsule as one) and the three routes; confirm Botanical Garden for Lali's question.
2. Confirm the room reading (window north, bed east, cupboard west, bedside table south) or supply the book's answer key.
3. Confirm the animal names and "deer" on the zoo map, and the street-map answers (Prem and Raju, Stop 1, south).
4. Confirm no revision video is wanted and that six tools are right.
5. Confirm the question heading "Zoo Grid Questions" in place of the book's "Answer the following".

## 9. Method
Three helper subagents wrote topics, tools and image specs for M1, M2, M3 from DESIGN.md. The chapter helper read every file they returned in full, checked the pictures against the page images, re-ran all gates and its own numeric check, and made these edits: heading rename, the "how many cm" wording, LaTeX house fixes, answers that put a measurement in parentheses.
