# REPORT: Class 5 Chapter 4, We the Travellers - II

## 12 Nov 2026: tool phases removed

The tool write-ups no longer have Phase 1, Phase 2 and Phase 3. In `tools_*.py` the three "what the student does" entries are plain steps without a phase label, and the practice cards are named "Card N" or "Challenge" instead of "Phase N, card N". The same text is in the plan's tool_config, and Section C of `priority_doc.md` has one "What the student does" line per tool. Cards, book questions, feedback, hints and everything else are unchanged (the book's questions are still on the tool's cards). DESIGN.md and MEDIA_BRIEF.md still describe the older three-phase format; this note replaces it.


## VERSION 3 (9 Nov 2026): the content team's 17-topic, 11-tool journey

Built plan `cbse_eng_maths5_ch4.json` is version 3 (plan_id `cbse_eng_maths5_ch4_v3`, live max was 2). Everything below the line "VERSION 2 REPORT" is the v2 report; its sections 4 to 6 (the points the book leaves unclear and the answers the plan worked out) still hold, its counts and gate lines are replaced by this block.

### Upload
Uploaded to STAGING on 9 Nov 2026 as `cbse_eng_maths5_ch4_v3`, ACTIVE (v2 and v1 archived), with the validation stamp skipped for this one chapter on the user's explicit choice (the only failures are the placeholder videos' `video_script_rules`). Read back from staging: the live v3 equals the local file exactly; 4 modules, 43 topics, 149 concepts, 32 objectives, 250 media, 11 tools. Never production.

### What changed against v2 (live, active)
- **Topics:** 17 learning topics as the content team listed them, held in 18 authored topics (their topic 1, Making Sums Equal, is T1 + T1B because the build allows one video in the opening topic). Near-Round-Number Addition, Pair-the-Ends Shortcut, Sums of Even and Odd Numbers, Let Us Think: Coins and Let Us Think: A Torch are now separate topics with their own video. Subtraction and its link with addition, Adding and Subtracting Large Numbers, Journey Problems, Quick Sums and Differences and Reading Tables are one concept video each, with labelled sections ("Section A", "Section B") and one worked example in two parts. The lining-up of digits is taught once (inside the adding section); the old "Aligned Digits, No Labels" concept is gone.
- **Videos:** 17 teaching videos (1 hook, 13 concept, 3 puzzle), down from 23. 57 question videos unchanged. 74 video slots in all.
- **Tools:** 11 (v2 had 8). New: Near-Round Number Adder, Pair-the-Ends Lab, Table Explorer. Re-aimed: Fuel Tank Adder (written addition only), Fuel Gauge Subtractor (adding back is a secondary check), Consecutive Sums Lab (no pairing), Line Up and Solve (separate Addition and Subtraction activities), Round Number Hops (two labelled modes), Pairs and Leftovers (two activities). Unchanged: Balance the Sums, Number Grid Puzzle.
- **Images:** 25 concept images in 18 concepts (merged concepts have one per section); the revision image is a journey map with one signpost per major idea; the picture of consecutive sums is now stepping stones with a running total; the number-grid image has blanks; the coin image is a coin mat with only the book's coins; the table image is an information board.
- **Modules** renamed to the content team's names.
- **Unchanged:** all 57 book questions, answers and cards. Checked against the live v2 plan by coverage id: 114 cards (57 question, 57 answer), 0 differences in text, steps, answers, LaTeX, figure descriptions or planned image links. Only the positional ids and the "Qn"/"Ansn" numbers inside the Questions topics follow the new positions (12 concept names changed).

### Gate state (v3)
- `build.py --placeholders`: structure stage OK; 0 structure, coverage, skeleton, objectives, solution_content, latex_content and question_layout problems; 1,651 equations checked, 0 failed. One advisory (the question and answer cards share a coverage id, as in v2).
- `core/check_master_id.py`: clean (master 148). `core/set_version.py`: live max 2, plan is v3.
- `validation/validate_local.py`: 148 failures, all `video_script_rules` (74 video slots with no script yet, 2 messages each). No stamp.
- `check_ch4_numbers.py` (independent, comma-aware, units and rupee chains, parity, "differ by", the book answers re-derived): 1,974 strings, 0 failures. The tool helper's own script rechecked 177 chains in `tools_4.py`.
- Scans of the built plan: no `$$`, no unbalanced `$`, no en or em dash, no "lamp" (the torch is a torch).

### Assumptions and judgement calls (v3)
1. The hook is kept (the pipeline requires one video in the opening topic). "Reuse relevant tools for practice" in the revision topic cannot be done: a tool lives in one concept and the summary topic has no tool. The revision topic carries a journey map with one signpost per idea, and the ideas are revisited through the practice sets and the existing videos.
2. Where the table gives one tool to two topics (Pairs and Leftovers for topics 12 and 13) the tool sits in the second topic with its two activities; the first topic's practice (circle the evens, add 2 to 18 and 23) has no tool.
3. The Great Indian road trip question stays in the Adding and Subtracting Large Numbers practice (as in v2); the Journey Problems picture uses the worked example's own traveller, because the book's own route (Mary's journey) stays on her question card.
4. Tools that hold few book questions: Near-Round Number Adder 1, Pair-the-Ends Lab 1, Fuel Tank Adder 2, Table Explorer 2 (their Phase 3 splits the parts over two cards). Balance the Sums holds none (its free try has no book questions; the four puzzles are in the next topic's practice).
5. Fuel Gauge Subtractor: the book's two relationship questions (Q1, Q2) cannot leave the concept, so they appear as sentence cards in its Phase 3 only; adding back is an optional step.
6. The Reading Tables picture uses the worked example's practice values on an information board; the book's own tables stay in the question cards and in the Table Explorer's Phase 3.
7. The Near-Round Number Adder's book question LUS43.add (c) 38 + 35 has a printed step "no easy way"; 38 is 2 below 40, so the near-round route also works. The book question and its answer are unchanged from v2.
8. Section D and E of `priority_doc.md` were renumbered for 11 tools; Section B has a map from the content team's topics 1 to 17 to the rows.

---

## VERSION 2 REPORT (kept for reference)

(Text written by the chapter helper and saved here by the lead session, because the helper could not write the file itself. The lead session re-checks every chapter's built plan afterwards. The helper could not read the live chapter name; the lead session checked it: the live record spells it "We the Travellers - II", as used.)

Folder: `chapters/maths5_ch4/new_design/`. Built plan: `cbse_eng_maths5_ch4.json` (version 2, plan_id `cbse_eng_maths5_ch4_v2`). Ids: chapter_id `cbse_eng_maths5_ch4`, chapter_master_id 148, subject_ref_id 80, medium 1, publication 1, phase 2, media_tag c5m.
Book: `textbooks/class-5/eemm104.pdf`, 15 PDF pages = printed pages 42 to 56. The first PDF page is the unnumbered opener (page 42 by sequence); the next page prints 43.
Nothing was uploaded, no git, nothing outside this folder and the helper's scratchpad subfolder was edited. The helper could not use helper subagents (the concurrent subagent limit was reached), so it wrote every file itself.

## 1. What exists
Files: priority_doc.md (A to F), DESIGN.md, content.py, concept_plan.py, topics_1.py to topics_4.py, tools_1.py to tools_3.py, media_specs/*.json (37), name_slots.json, book_rules.json, chapter.config.json (eqcheck plain, doer_tool_optional, media_placeholders, publication_id 1, field_cleanup, server_image_ids), build.py, cleanup_fields.py, server_ids.py, media_placeholders.py (with this chapter's DOC_PURPOSE), media_specs.py, topics_common.py (all copied from Chapter 2), ch_latex_house.py (adapted, not named latex_house.py), the built plan, media_worklist.json, video_worklist.json, question_images_report.json.
Scratch scripts in `/tmp/claude-1506/-root-maths-learning-plan/9dfc46bf-2f90-406d-86af-005a3698a5e2/scratchpad/c5ch4/`: verify_facts.py, verify2.py, check_chunk.py, check_ch4_numbers.py (step 9a), gen_media.py, grids.py, tool1_cards.py.

Counts: 4 modules; 14 authored topics plus 22 inserted "Questions: ..." topics = 36 topics; 151 concepts (37 authored, 114 question and answer). 23 teaching videos (1 hook, 19 concept, 3 puzzle: grids, coins, torch) + 57 question videos = 80 slots. Questions 57 = 7 solved examples (Example 1 to 7 in book order), 43 exercises, 7 prompts; 20 have a question-card diagram; 85 solution cards (28 questions have a second card). 8 tools: Balance the Sums, Fuel Tank Adder, Fuel Gauge Subtractor, Consecutive Sums Lab, Line Up and Solve, Round Number Hops, Number Grid Puzzle, Pairs and Leftovers. Image nodes (all placeholders): 24 concept images, 142 question and solution cards; 13 tool and practice concepts have a no-image decision with a reason. Coverage: 84 ids (57 questions, 22 text, 5 talk), all attached. The last topic is a text summary with short concept checks (no recap video).

## 2. Gate state
- `core/check_master_id.py`: MASTER IDS: clean.
- `core/set_version.py`: live max version is 1, so this plan is v2 and would replace the live v1. If v1 holds built images, tools or videos, run `core/published_media.py pull` first (runbook step 4). (The lead session found that the live v1 of chapters 3 to 15 all hold built tools.)
- `build.py --placeholders`: structure stage OK (0 structure, coverage, skeleton, objectives, solution_content, latex_content, question_layout problems; 1513 equations checked, 0 failed; one advisory coverage note: each question maps to its question and answer concepts).
- `validation/validate_local.py`: 160 failures, grouped by family: video_script_rules 160, all other families 0 (80 slots with no script, 2 messages each). No stamp, as expected.
- Built-plan scans: no `$$`, no unbalanced `$`, no stray single-letter maths, no dash.
- check_ch4_numbers.py: 1,975 strings scanned; 800 chains (including rupee and unit chains), 50 comparisons, 41 parity claims, 4 "differ by", 20 "K less/more than" claims, and the book answers re-derived from scratch (every swap in the opening puzzles, all 10 pairs for the closest sums, all coin combinations, every palindrome, every grid, tables, the nine sums and nine differences, quick sums): 0 failures. Word statements such as "6 tens and 3 tens make 9 tens" are not machine checked; the helper read them.

## 3. Judgement calls and clashes
1. Revision video: the pipeline has none; text summary instead.
2. Framing: the tool comes straight after the hook, and the concept video "Swapping a Pair Changes Both Sums" after it (the brief's usual order is video then tool). T1B holds that video and the four opening puzzles, as Chapter 2 did.
3. Hook: the book gives the opener no story (only "write each number on a small piece of paper"). The hook puts puzzle (a)'s cards in the hands of Nazrana and her friends on their road trip (the book's trip, page 48); the card-game frame is the helper's own. It does not solve the puzzle.
4. 8 tools (the usual 9 to 11 is a guideline). No tool for the add/subtract link (the check by adding is in the Fuel Gauge Subtractor), palindromes, coins, torch, journey problems, tables (reasons in priority_doc.md F2). Adder, subtractor and aligner all use place value but have different purposes (regroup up; regroup down with a check; line up digits of different lengths with no labels). Large-number adding and subtracting share Tool 5.
5. Topic merges: add/subtract link with "More Fuel Arithmetic" (T3); adding and subtracting large numbers (T5); mountain and certificate tables (T12).
6. Placement of questions: Let Us Do on page 56 is split: Q1 and Q2 (nine sums, nine differences) in T5; Q3 to Q5 (Ambrish, factory, runs) in T6. Pages 50 and 51 Q2 to Q4 (Mary, council, truck) are in T6. Some Questions topic names repeat ("Questions: Example", "Questions: Let us do", "Questions: Let Us Think"), as in Chapter 2.
7. Labels: boxes called Let Us Solve / Let Us Think / Let Us Think and Solve get topics named by heading with a bracket tag, e.g. "Let Us Solve (adding large numbers)"; only the real Let Us Do box lands in "Questions: Let us do".
8. "Regroup", not "trade", everywhere (the book says Regroup).
9. Two concepts the book only names by an instruction: "Easier Ways to Add" (page 43: add a number just below a round number by adding the round number and taking the extra back, and add whole tens) and "Estimate First, Then Check" (page 51: round each price up to the next thousand). Please confirm both readings.
10. The book's "Try not to write TTh, Th, H, T, and O" is written with place words because the letters become maths variables in LaTeX.
11. All 10 name slots used (Nazrana, Mahesh, Mary, Sukanta, Piku, Namita, Nitin, Jincy, Raghu, Ambrish). Sanju and Mira (Chapter 1) would need a freed slot. Priyanka Mohite, Virat Kohli and Sachin Tendulkar are real people in the book's data: written as printed, no token, no added fact; videos must follow the real-person rule.
12. book_rules banned words: lakh, crore, million, billion, decimal, fraction, percent, negative number, algebra, variable, equation, remainder, quotient, divisible, divisibility, prime, composite, average, median, estimation rule, rounding rule.
13. Equation gate set to plain; chains with rupee signs or units are skipped by it, so the working was written as plain number chains and unit chains were checked with the helper's own script.

## 4. Points the book leaves unclear (reading adopted; full list in priority_doc.md A6)
1. The map on page 46 prints 1885 km; the text and sum use 1,855 km (1,855 + 1,862 = 3,717). The plan uses 1,855. Please confirm.
2. "Least number of moves": a move interchanges one number from each group. Every swap checked: (a) 1 move, swap 2 and 3; (b) 1 move, swap 5 and 9 or 7 and 11; (c) 2 moves; (d) 2 moves. The hint's swap of 2 and 5 gives sums 22 and 18 (further apart); used as a first try.
3. Let Us Do Q1 and Q2 (page 56) print letters a to f then f to h (f twice) for nine parts; lettered (a) to (i).
4. Q1 (i) 50,050 + 55,000 has six digits, one place beyond the chapter's chart. Written 1,05,050 (Indian commas), the extra 1 goes in a new place on the left, no new place is named. Please confirm.
5. Consecutive sums Q1 to Q3 (no printed answers): sums of 2 consecutive numbers are always odd, of 3 take turns odd and even (3 times the middle number), of 4 always even (two odd pairs); differences between successive sums are 2, 3, 4 (the count of numbers added), and 5, 6 for five and six numbers.
6. "Notice how the sums are related": pairs from the two ends make the same total; the four sums are 204, 102, 250, 1,437.
7. Great Indian road trip: the label 590 km sits under the word Mumbai; read as Delhi to Mumbai 1,600, Mumbai to Goa 590, Goa to Hyderabad 670, Hyderabad to Puri 1,055; total 3,915 km whichever leg carries which label.
8. Closest sums (all ten pairs): 10,045 (5,205 + 4,840); 14,675 (6,220 + 8,455); 13,295 (8,455 + 4,840; the next, 13,315, is 20 further away); 15,550 (7,095 + 8,455).
9. Council estimate: round up to the next thousand, 70,000 is less than 70,500, so enough; exact 68,878, left 1,622.
10. "Will this method work if the units digit is 0?" and "always work?": yes, always; other methods: count up to the next hundred, or take the number from 1,000.
11. "Use the above solutions ... do not calculate again": read as the quick 9 and 99 method plus the add/subtract link; blanks 23, 47, 778, 567.
12. Grids: rows left to right, columns top to bottom; 42, 42, 42, 60, 60 valid fillings; any valid grid accepted, one shown.
13. Palindromes: 10 (100 to 200), 12 (900 to 1,200, including 1,001 and 1,111), 20 (25,000 to 27,000).
14. Paired arrangements counted on the page: 18 = two rows of 9; 23 = rows of 12 and 11.
15. Jincy: 11 combinations, one shown as sample; the torch is OFF at the start, odd presses ON, the 23rd press gives ON.
16. The book does not number solved examples (numbered 1 to 7 here); the eight bare subtractions numbered 2 to 9 on page 45 are one set lettered (a) to (h).
17. Printed 1301 and 2700 without commas (written 1,301 and 2,700); litres written in full instead of l.
18. The QR code on the opener is unreadable; nothing taken from it.

## 5. Kit and sheet assumptions
None. The helper checked the lead session's note about the Learning Material Sheets against this chapter: the text has no kit, sheet, token, cut-out, dot grid or graph paper. The only related words are "write each number on a small piece of paper" (ordinary scrap paper). No sheet page was rendered; no assumption is listed.

## 6. Answers the book does not print (worked out by the helper)
The four Making Sums Equal puzzles; the three consecutive-sums questions and four sums; the road trip; the closest sums; Mary, the council, the truck, Ambrish, the factory, the runs; the quick sums and 9 and 99 subtractions; the palindrome lists; the five grids (samples); the even/odd questions (sample pairs); Jincy's coins; both torch questions; the mountain and certificate questions. All other answers are arithmetic on printed numbers, all recomputed.

## 7. Decisions wanted
1. 1,855 km versus the map's 1885 km.
2. How 1,05,050 is written and explained.
3. The two concepts named only by an instruction (easier ways to add; estimate by rounding up).
4. The hook's frame.
5. Whether live v1 holds built media to pull first before uploading v2 (it does: built tools).
6. That the page 56 and pages 50 and 51 question sets sit in T5 and T6 rather than in book order.
7. 8 tools, with none for the add/subtract link or large numbers.
8. Videos, solutions.json, question and solution images and tool pages are all still placeholders.
