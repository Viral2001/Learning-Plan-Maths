# Class 5 Chapter 8, Weight and Capacity: build report (local, placeholder route)

## 12 Nov 2026: tool phases removed

The tool write-ups no longer have Phase 1, Phase 2 and Phase 3. In `tools_*.py` the three "what the student does" entries are plain steps without a phase label, and the practice cards are named "Card N" or "Challenge" instead of "Phase N, card N". The same text is in the plan's tool_config, and Section C of `priority_doc.md` has one "What the student does" line per tool. Cards, book questions, feedback, hints and everything else are unchanged (the book's questions are still on the tool's cards). DESIGN.md and MEDIA_BRIEF.md still describe the older three-phase format; this note replaces it.


(Text written by the chapter helper and saved here by the lead session, because the helper could not write the file itself. The lead session re-checks every chapter's built plan afterwards.)

## 1. Identity
Class 5 Chapter 8 Weight and Capacity (`textbooks/class-5/eemm108.pdf`, 15 PDF pages = printed pages 104 to 118; the opener has no printed number, it is 104 by sequence, the next page prints 105). chapter_id `cbse_eng_maths5_ch8`, master id 152, subject_ref_id 80, medium 1, publication 1, phase 2, media tag c5n. `check_master_id`: MASTER IDS: clean. `set_version`: live max is already 1, so plan_id `cbse_eng_maths5_ch8_v2`, version 2. Never uploaded, no git, nothing edited outside the chapter folder and the helper's scratchpad c5ch8. No helper subagents ran (the request was refused: concurrent subagent limit), so the chapter helper wrote every file itself.

## 2. Counts
- Modules 3; authored topics 14 (T1 framing, T1B, T2 to T12 idea topics, T13 summary) plus 21 Questions topics = 35 topics; authored concepts 36, 138 after the question layout (51 question + 51 answer concepts).
- Videos: 1 hook + 21 concept = 22 teaching (21 worked examples with the plan's own numbers) + 51 question videos = 73 slots. No recap video.
- Questions 51: 10 solved examples, 29 exercises (Let Us Do/Find/Think/Compare/Solve), 12 prompts. Coverage ids 71 (51 questions, 19 text, 1 talk), coverage gate 0 problems.
- Tools (specs only): Weight Check (free try, T1), Scale Reader (T2), Kilogram and Gram Line (T3), Weight Regrouper (T6), Scaling Line (T8), Measuring Jug (T10).
- Images: 23 concept figures with full specs (T1.C1, T1B.C1, T2.C1, T2.C2, T3.C1, T3.C2, T4.C1, T5.C1 to C3, T6.C1, C2, T7.C1, C2, T8.C1, C2, T9.C1, T10.C1, C2, T11.C1, C2, T12.C1, T13.C1), 13 no-image decisions (every tool and practice concept), 51 question cards (16 with a diagram), 61 solution cards (10 questions with a second card). `media_specs.check_all()` = `[]`.
- Files: priority_doc.md, DESIGN.md, content.py, concept_plan.py, topics_1..4.py, tools_1..3.py, media_specs/*.json (36), name_slots.json, book_rules.json, chapter.config.json, ch_latex_house.py, build.py + copied helpers, cbse_eng_maths5_ch8.json, media_worklist.json, video_worklist.json, question_images_report.json. Scratch (`/tmp/claude-1506/-root-maths-learning-plan/9dfc46bf-2f90-406d-86af-005a3698a5e2/scratchpad/c5ch8/`): verify_facts.py, numeric_check.py, gen_media_specs.py, dial measuring scripts.

## 3. Gate state
- `build.py --worklist`, `--video-worklist`, `--placeholders`: "structure stage OK". Counts: structure 0, equations checked 690 / failed 0, coverage 0, skeleton 0, objectives 0, solution_content 0, latex_content 0, question_layout 0, video_script_rules 146 (expected).
- `validate_local.py`: 146 failures, grouped: video_script_rules 146 = 73 "missing keys" (one per placeholder video) + 72 "interactive_video_variant needs an interaction_point" (21 worked, 51 exercise) + 1 "chapter hook shows a picture (a beat with a photo)". No other family. No stamp (expected). Same shape as Ch2 (118 = 59+58+1; here 146 = 73+72+1). Advisory: 1 coverage warning (question and answer concept pairs).
- Independent numeric and text check (numeric_check.py): reads every string of the built plan and the image specs; evaluated 1,158 chains, 477 "X is Y" statements and 63 "less/more than" statements with units (kg, g, mg, l, ml, quintal, tonne, rupees) in exact arithmetic; scanned dashes, NCERT, textbook, page N, Fig., decimals, fraction signs, banned words, `$` balance; compared every answer with the verified answers (DESIGN.md section 4). Result: 0 real problems (3 reports were checker false alarms, all true: "10,000 g is 10 kg and 12,000 g is 12 kg", "a 2 l jug and 250 ml make 2 l 250 ml"). Dial readings checked separately.
- Traps found and fixed: (a) `eqcheck_plain` reads "3 kg × 4 = 12 kg" as "4 = 12" and a chain right after "(" such as "(500 + 750 = 1,250 g" as "750 = 1,250" (4 failures, fixed by rewording); (b) the core LaTeX converter splits a bare "kg" after a word and turns bare g, l, mg into variables, so every question's text, working and answer spells unit words without a number in full (kilograms, grams, litres, millilitres); (c) ch_latex_house.py wraps units after numbers in `\text{ }` and adds a thin space between a unit and the next number; (d) the displayed answer is cut at 220 characters of LaTeX: the longest is 202.

## 4. Points the book leaves unclear (reading adopted; also in priority_doc.md A6 and content.SOLUTION_NOTES)
1. The six scales on the opener print no answers. Read by measuring the needle on a 400 to 500 dpi render and counting marks from 0: (a) 4 kg full turn, 40 marks of 100 g, 6th mark = 600 g; (b) 2 kg, 20 marks of 100 g, 18th = 1 kg 800 g; (c) 6 kg, 60 marks of 100 g, 25th = 2 kg 500 g; (d) same face as (a), 26th = 2 kg 600 g; (e) 1 kg, 100 marks of 10 g, 15th = 150 g; (f) same face as (e), 66th = 660 g. Needles meet the mark circle at 5.95, 17.99, 24.8, 26.02, 15.04, 65.9 marks; the answer boxes agree (grams only for a, e, f). To be confirmed.
2. Check! Check!: no printed answer. Ticks: Bed 60 kg, Rice Bag 5 kg, Bucket 1 kg 800 g, Water Bottle 650 g; crosses: Iron Almirah 40 g, Sofa 30 g, Refrigerator 50 g. Bed, bucket, bottle are judgement: labelled "Sample answer, your answer may differ".
3. p. 105 double number line is not to scale; blanks filled by x1,000 (3 kg = 3,000 g with the x3 arrow, 8 kg = 8,000 g, 15,000 g = 15 kg, 20 kg = 20,000 g, 25,000 g = 25 kg, 30 kg = 30,000 g).
4. p. 106 double number line: the last two marks have blanks for both kg and g and no given value; only the six marks with one given number are filled; the last two are left unfilled. Please say what they are for.
5. Which child is Shamim or Rehan and Mary or Daisy is not printed; the plan says "one child" and "the other".
6. "Ramiz drinks ___ l in a day": read as the two 500 ml bottles only, 1,000 ml = 1 l.
7. "How many times refill a 500 ml bottle": 3,000 ÷ 500 = 6; answered "6 times" (6 bottles), noting the first fill is not a refill.
8. Tea for 2 cups and the 20 ml bucket: open questions. Sample answer with a labelled practice cup size (about 150 ml); the bucket answer uses only the book's 500 ml bottle (500 ÷ 20 = 25) and says use litres.
9. Let Us Solve 2: every glass filled to its 360 ml capacity: 2,880 ml poured + 120 ml left = 3,000 ml = 3 l.
10. Fuel table: the empty last column is not asked for; the plan fills it (1,500; 1,800; 500; 96; 125) then answers (a) 300 l, (b) 4,021 l. The book's 500 litres per truck kept as printed.
11. Let Us Do 7 (langar flour): 65 kg bought, 42 kg 275 g used, 52 kg 500 g bought next day: 75 kg 225 g.
12. Box of nuts asks grams, the working prints 1 kg 200 g: answer 1,200 g (1 kg 200 g).
13. Elephant and whale: whale = 40 times the elephant: 200,000 kg (the book's numbers, not a real measure).
14. Cost table: no printed method for the g part; the plan uses the double number line idea (whole kg by the price of 1 kg; part from 1,000 g: 500 g half, 250 g a quarter, 100 g a tenth; no decimals). Totals: Rice ₹750, Flour ₹290, Sugar ₹225, Chana dal ₹252, Besan ₹240, Jaggery ₹70.
15. The four teacher notes (pp. 104, 108, 110, 117) are used inside concept videos only; no teaching role for a teacher.
16. KIT / SHEETS: this chapter refers to no kit, cut-out, token, grid or Learning Material Sheet. The only "kit" hits are "kitchen scale" (p. 106) and "community kitchen" (p. 111). The helper checked the lead session's correction against all 15 pages and the text layer; nothing was taken from the sheets and no kit assumption exists (priority_doc A6.16 and content.SOLUTION_NOTES say so).
17. The QR code on the opener is unreadable from the file; nothing taken from it.

## 5. Judgement calls and clashes
- Revision video: no recap video in the pipeline; T13 is a text summary with short "Check:" lines.
- Concept video before tool / one-video opener: the framing topic holds only the hook and the free-try Weight Check; the concept video "Gram or Kilogram?" and the Check! Check! question are in idea topic T1B. Free try Phase 1 recalls the hook, Phase 3 asks the opener question open.
- 6 tools, not 9 to 11. No tool for: comparing weights and capacities, milligram/quintal/tonne (the book: g to mg "is similar to converting kg to g"), times as heavy, multiply and share weights and capacities (Tool 4's exchange covers it), which unit for capacity (same judgement as Tool 1), adding and subtracting capacities (the book says do it as for weight), Let Us Solve. Tools 3 and 5 both use a double number line but for different purposes (fixed x1,000 unit change vs any multiplier on linked quantities).
- No puzzle video: the chapter has no puzzle; King's Weight is a word problem (question card + video).
- Question grouping: the pipeline groups a topic's questions by category, so examples follow the Let Us Find questions inside a topic and concept names count Q1, Q2 within a category (the goldsmith is "Let Us Find: Q3", book number 4).
- One question per numbered book question; lettered parts stay inside. Kinds: Let Us Do/Find/Think/Compare/Solve = exercise; numbered in-text questions under other headings = prompt; the 10 printed solved examples = example (Example 1 to 10 in book order).
- Practice values (all labelled): pencil 6 g, school bag 4 kg, egg 50 g, bag of cement 50 kg, sugar sachet 5 g, the two worked scale faces, 3 kg 600 g + 2 kg 700 g, 5 kg 200 g − 2 kg 800 g, 6 sacks of 2 kg 500 g, 9 kg 600 g shared by 3, rice ₹36 per kg, 3 plates 240 g, cup 200 ml and drum 200 l, 4 l jug and 200 ml cups, 3 l 40 ml, 4 l 600 ml + 3 l 700 ml, 6 jugs of 1 l 250 ml, a 150 ml cup for the tea question. None equals a book question's numbers.
- Characters: 19 names in the book, 10 tokens (Anu, Shrenu, Shamim, Rehan, Harpreet, Rathna, Aarav, Ramiz, Tina, Sam). Overflow, no token: Muskaan, Kiran, Riya, Mary, Daisy, Nitesh, Dev, Bhalerao, Khayal (a video must use the role).
- Theme: "Anu's Neighbourhood Market" (home, grocery store, fruit stall, milkman's cart, petrol pump); each tool is a counter of the lane. Image specs are flat countable figures (dials, double number lines, columns, bars).
- No decimals or fraction signs anywhere (500 g is "half of 1,000 g").

## 6. Printed-book errors and oddities
- p. 110 bubble: "total rice bought is 4 kg 250." has no unit; the plan writes 4 kg 250 g.
- p. 107 (c): "10035 g" has no comma; the question is kept as printed, the working writes 10,035 g.
- Double number lines on pp. 105, 106, 114 are hand drawn, not to scale; the last two marks of the p. 106 line carry no value.
- p. 116 fuel table: 500 litres per truck, 300 per bus, kept as printed.
- "Let Us Find" numbering runs 1 to 7 across two pages and "Let Us Do" numbering continues across pp. 112 to 113 without a repeated heading; the plan follows the printed numbers.
- p. 115 prints "1 l =1,000 ml"; the plan writes 1 l = 1,000 ml.

## 7. Answers the book does not print
The book prints an answer only for the 10 solved examples. Every other answer is the plan's own (the six scales, Check! Check!, matching and the p. 105 blanks, Shamim and Rehan, the conversions and the p. 106 line, fruits and comparisons, the milligram questions and g/mg comparisons, whale, quintals and tonnes, King's Weight, Let Us Do 1 to 7, the cost table, 4 people and 500 g, tomatoes, Nitesh, tea, bucket, Ramiz, Muskaan, the four container groups, the milkman's line and table, Mary and Daisy, the capacity conversions, the fuel table, the five quantity comparisons, Let Us Solve 1 to 5). All recomputed in verify_facts.py and matched to the text by numeric_check.py.

## 8. Needs a decision or check by the user
1. Confirm the six scale readings and the Check! Check! reading.
2. Which named characters get the 10 tokens.
3. What the last two marks of the p. 106 line are for (left unfilled).
4. The live row already has v1 (with built tools); this plan is v2; decide if it replaces v1 as active (upload only when asked).
5. The longest workings (the six scales, 13 steps about 1,200 characters; Check! Check!, 9 steps; the cost table, 8 steps) may need the card renderer to shrink the second card; the media team should look first.
6. The scales' question card `q_figure` names each needle mark (what the picture shows, not an answer); the picture must be drawn to exactly those marks.
