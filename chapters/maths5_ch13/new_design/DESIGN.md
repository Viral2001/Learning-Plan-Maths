# Class 5 Ch 13 "Animal Jumps": design spec for authoring (structure stage)

Chapter folder: `chapters/maths5_ch13/new_design/` (call it NEW). Pipeline root: `/root/maths-learning-plan/Learning-Plan-Maths`.
Run Python as `python3 -B -X utf8` from inside NEW (the chapter modules import each other; `-I` cannot). **Local only. Never upload, never push.**
Book: `book/chapter_text.md` (the text layer scrambles the number lines, the trail and the cards: ALWAYS check numbers against `book/page_NNN.png`, 7 pages = printed pages 164 to 170; the first PDF page is the unnumbered opener, printed page 164 by sequence).
Priority doc (the plan for this chapter, wins over everything except hard rules): `priority_doc.md`. Section C is the tool spec, section B the topic flow.
Reference chapter of the same class, for STYLE only: `../../maths5_ch2/new_design/` (`DESIGN.md`, `topics_1.py`, `tools_1.py`, `topics_common.py`).
Helpers you write with: `topics_common.py` (A, WE, FIO, DOER, TOPIC, T). Read it first.
Verified facts: `/tmp/claude-1506/-root-maths-learning-plan/9dfc46bf-2f90-406d-86af-005a3698a5e2/scratchpad/c5ch13/verify_facts.py` recomputes every answer below with Python. Section 4 is the same data.

## 1. Hard rules (gates enforce most; fix content, never a gate)
- Class 5 students, 10 to 11 years old: short plain sentences. Characters and settings are the book's: Mowgli, Robby the rabbit, Deeku the deer, Sher Khan the tiger, Bagheera the panther, Baloo the bear, Kaa the snake, Akela the wolf, and the unnamed ant, spider, frog, bird, deer, rabbit, monkey, grasshopper; the cobbled road, the trail, the box, square tiles in arrays. The plan's own WE use the same animals. Do not invent facts or datasets: every number that is not a plain WE number comes from the book or from section 4.
- **No em dash and no en dash** in any string or comment (the book's dashes become commas, colons or "to"). Minus is U+2212 `−`. Use `×` and `÷`. Hyphen only inside words.
- Never write "NCERT", "textbook", "page N", "Fig.", "Figure N" or exercise numbers in anything the student reads (names, teach lines, steps, questions, tool text). Say "your maths book". Exception: the `textbook=[...]` argument of `A()` quotes the book verbatim (still no dashes; the book's two typos are corrected: "Multiples of 6", "each of the numbers").
- **Arithmetic must be true in every string.** The equation gate (`eqcheck_plain`) checks only whole-number chains `a op b = c` and skips a chain glued to a letter or a slash. Everything else (lists of factors, multiples, jump landings, divisibility, comparisons) is NOT machine checked: re-compute it with Python before you finish. Do not write a comma list without a space after each comma (the gate reads `2,4` as one number). Do not write an equation that is only approximately true.
- 100% coverage: every id in `content.NCERT_ITEMS` (section 3) is attached to a concept: a `text` or `talk` id through `A(..., ncert=[...])` or a DOER's `ncert=`, a question id as an `FIO` item of the DOER of its topic.
- **One video per concept.** A teaching concept `A()` has exactly ONE `WE` in `examples` (that WE is the concept video) with the PLAN's own numbers: never the exact number set of a book question. The hook concept has `video_focus=["HOOK"]`, `enrichment=True`, no WE. DOER concepts carry a recap, their question items and at most one tool, no WE.
- **Questions.** Every book question is a `FIO(cov, label, question, steps, answer, kind=...)` in the DOER of its topic, in the book's order; `core/qt.py` moves each into its own concept of the "Questions: ..." topic that follows. `question` is the book's wording (copy it; "textbook" becomes "maths book"; the part letters are the plan's where the book prints (f) twice). `steps` = the numbered working, one operation per line, values before combining, a check as the last step; `answer` = short final answer. Open-ended items get a labelled "Sample answer" built by reasoning and say "Your answer may differ". `q_figure` (one plain sentence: ONLY what the question gives, never the answer or a hint) when the question card needs a drawing, `s_figure` when the solution card needs one.
- **The answer is cut at 220 characters of its LaTeX form** and the converter wraps every number in `$...$`, so a list of numbers costs about 1.5 times its plain length: keep a number-heavy answer under about 130 plain characters and put the full lists in `steps`. Measure with `core.solutions.latex_convert.latex_wrap` after the house module.
- **Labels (`book`) decide the Questions topic** (`core/question_naming.py`): a label starting `Let Us Do` goes to "Questions: Let us do"; any other label goes to a topic named by the text before its first colon ("Arrays", "Animal Jumps", "Mowgli's Trail", "Find the hidden numbers"). Use the labels of section 3.
- Names: DOER name starts with `Practice: ` or `Pull it together and do it: `.
- An idea topic has 2 to 4 primary concepts INCLUDING its DOER (last). The intro T1 is `topic_type="framing"` with `""` objective, all concepts `enrichment=True`: C1 hook (`video_focus=["HOOK"]`) and C3 a DOER with `role="try_it"` and the free-try tool. The concept video and the book questions of the opener live in the idea topic T1B. The summary topic T6 is `topic_type="summary"`, one concept, no tool, no video_focus (there is no recap video).
- Objectives: one per non-enrichment concept (15 to 40 words), starts "Students ...", checkable (a verb you could test: find, list, make, decide, tell, explain, sort), shares a key term with its concept, never names a tool, never uses learn, know, understand or familiar. Topic objective (at most 55 words) on each idea topic. Bloom words: Remember, Understand, Apply, Analyze.
- Misconception ids come from `content.MISCONCEPTIONS` (section 6); attach the relevant ones to teach concepts and tools.
- `teach` lines: the first line is a prediction question ("Predict first: ..."), then the reveal, then the rule in one line. `minutes` 4 to 8.
- Tool specs (`T(...)`): section 5. Exactly 5 to 7 challenges, exactly 4 hints.
- Words outside the chapter (book_rules.json banned_words): no LCM, HCF, GCD, "lowest common multiple", "greatest common factor", composite, prime factorisation, factor tree, remainder, fraction, decimal, percent, negative. The chapter's own words are factor, multiple, common factor, common multiple, array, prime number, divisible, consecutive.

## 2. Topic plan (7 topics, 3 modules). Keys are fixed. Authored concept key = `T<n>.C<m>`.
A = teach concept with exactly one WE (one video), D = DOER.

| key | module | topic name | printed pages | concepts | tool |
|---|---|---|---|---|---|
| T1 | M1 | Find the Hidden Numbers (framing) | 164 | C1 hook "Find the Hidden Numbers"; C3 D(try_it) "Hidden Number Box: Explore" (no C2: the framing topic holds exactly one video, the hook, and no questions) | `hidden_number_box` |
| T1B | M1 | Factors and Multiples | 164 | C1 A "Factors and Multiples"; C2 D "Practice: Hidden Numbers" (the opener's three questions) | none |
| T2 | M1 | Arrays Show Factors | 164, 165 | C1 A "Arrays Show Factors"; C2 A "A Number Is a Multiple of Its Factors"; C3 A "Numbers With Only Two Factors"; C4 D "Practice: Arrays and Factors" | `array_maker` |
| T3 | M2 | Common Multiples | 165, 166, 167 | C1 A "Common Multiples"; C2 A "The Pattern in Common Multiples"; C3 D "Practice: Common Multiples" | `jump_together` |
| T4 | M2 | Common Factors | 167, 168, 169 | C1 A "Jumps That Land on a Number"; C2 A "Common Factors of Two Numbers"; C3 D "Practice: Common Factors on the Trail" | `trail_jumper` |
| T5 | M3 | Factors and Multiples at Work | 169, 170 | C1 A "Checking a Statement"; C2 A "Divisible by 2, 5 and 10"; C3 D "Pull it together and do it: Factors and Multiples at Work" | `number_sorter` |
| T6 | M3 | Chapter Revision: Animal Jumps (summary) | whole chapter | C1 A (no video_focus, no WE; revision lines and short concept checks as `teach` lines using only chapter content) | none |

Modules (content.py): M1 "Factors, Multiples and Arrays" (T1, T1B, T2), M2 "Common Multiples and Common Factors" (T3, T4), M3 "Using Factors and Multiples" (T5, T6).
Question order inside a DOER = the book's order. After build, each topic that has FIO items is followed by its "Questions: ..." topics.

Teaching concept seeds (the WE is the plan's own; none uses a book question's numbers):
- T1B.C1: a box that multiplies by 6 gives 30, 42, 54 from 5, 7, 9; the WE finds the multipliers of 30, 42, 54, 90 (1, 2, 3, 6).
- T2.C1: 18 tiles: arrays 1 × 18, 2 × 9, 3 × 6; factors 1, 2, 3, 6, 9, 18.
- T2.C2: 44 is a multiple of each of 1, 2, 4, 11, 22, 44, and not of 8.
- T2.C3: 19 has one array (prime), 21 has two (1 × 21, 3 × 7).
- T3.C1: Robby jumps 2 and Deeku jumps 5: common multiples 10, 20, 30.
- T3.C2: jumps of 6 and of 15: 30, 60, 90, the multiples of 30.
- T4.C1: jumps of 4 land on 8 and 20 but skip 14 and 26.
- T4.C2: common factors of 18 and 30: 1, 2, 3, 6.
- T5.C1: every multiple of 4 is a multiple of 2 (true); every multiple of 6 is a multiple of 4 (false).
- T5.C2: 16, 35, 60, 48, 85, 70 sorted by 2 only, 5 only, 2, 5 and 10.

## 3. Book items: coverage ids, kind, label, home (all in `content.NCERT_ITEMS`)
Printed pages: the opener is page 164 (no number printed), then 165 to 170.

Text and talk ids (no FIO):
| id | kind | what | home | page |
|---|---|---|---|---|
| open.story | text | "Find the hidden numbers. Numbers put in this box get multiplied by a number and come out." (box with 28, 36, 48, 72 coming out; "You can also play this game with your friends.") | T1.C1 | 164 |
| open.factors | text | the multipliers 1, 2, 4 are the factors of 28, 36, 48, 72; the common factors of all; the numbers are multiples of 1, 2 and 4 | T1B.C1 | 164 |
| open.product | text | "The product of two or more factors gives a multiple." | T1B.C1 | 164 |
| arr.def | text | a number arranged in an array shows its factors; the array 3 × 5 = 15 with the labels Factors and Multiple | T2.C1 | 164 |
| arr.twelve | text | arrays for 12: 3 × 4, 2 × 6, 1 × 12 | T2.C1 | 164 |
| mult.def | text | 1, 2, 3, 4, 6, 12 are all factors of 12; each divides 12 completely; 12 is a multiple of these numbers; the number itself is always a multiple of itself | T2.C2 | 165 |
| one.self | text | margin note: the number itself and 1 are always factors of any number | T2.C2 | 168 |
| cm.def34 | text | a rabbit jumps 4, a frog jumps 3; the numbers both touch are the common multiples of 3 and 4; 12 is the first | T3.C1 | 165 |
| cm.lists46 | text | the multiples of 4 (4, 8, 12, 16) and of 6 (6, 12, 18), 12 circled | T3.C1 | 166 |
| cm.spider | text | a spider jumps 3, a grasshopper jumps 6; 6 and 12 are common multiples of 3 and 6 | T3.C2 | 166 |
| cm.notice34 | talk | "What do you notice about the common multiples of 3 and 4? Discuss in class." | T3.C2 | 165 |
| cm.notice36 | talk | "What do you notice about the common multiples of 3 and 6? Discuss." | T3.C2 | 166 |
| cm.noticeQ1 | talk | "What do you notice about the common multiples of different pairs of numbers? Discuss in class." | T3.C2 | 166 |
| trail.answer2 | text | "Did Mowgli meet the ant, frog, bird and the rabbit? Notice their positions 4, 12, 14, and 50. 2 is a common factor of these numbers." (the book's partial answer to Q3) | T4.C3 (DOER ncert) | 168 |
| cf.def | text | pink box: "A common factor of two or more numbers exactly divides each of the numbers." | T4.C2 | 168 |
| cf.notice7 | talk | "What do you notice about the common factors of different pairs of numbers. Discuss in class." | T4.C2 | 169 |
| summary | text | chapter summary | T6.C1 | |

Question items (FIO). `label` is exact. Wording is the book's (blanks `___`). Letters (a) to (i) where the book prints (f) twice.
| id | kind | label | wording and figure | home | page |
|---|---|---|---|---|---|
| open.box | prompt | Find the hidden numbers: guess the multiplier | "Numbers put in this box get multiplied by a number and come out." Four numbers 28, 36, 48, 72 (read off the picture). (a) guess the multiplier (b) more than one? (c) what numbers might have been put inside? | T1B.C2 | 164 |
| arr.fifteen | prompt | Arrays: other arrays for 15 | "Are there other numbers that are factors of 15? Try to make other arrays for the number 15." Figure: an array of 15 tiles, 3 rows of 5. | T2.C4 | 164 |
| arr.blanks12 | prompt | Arrays: why 12 is a multiple of its factors | "Do you see why 12 is a multiple of 1, 2, 3, 4, 6, and 12?" blanks 2 × ___ = 12, 3 × ___ = 12, 12 × ___ = 12, 1 × ___ = 12 (the plan letters them (a) to (d)) | T2.C4 | 165 |
| LUDa.arrays | exercise | Let Us Do (arrays), Q1 | "Make different arrays for the following numbers. Identify the factors in each case." (a) 10 (b) 14 (c) 13 (d) 20 (e) 25 (f) 32 (g) 37 (h) 46 (i) 54 | T2.C4 | 165 |
| prime.why | prompt | Arrays: why 13 and 37 are called prime numbers | "Numbers like 13 and 37 are called prime numbers. Why?" (margin note beside (g)) | T2.C4 | 165 |
| cm.more34 | prompt | Animal Jumps: more common multiples of 3 and 4 | "12 is the first common multiple of 3 and 4. What are some other common multiples of 3 and 4? You can continue the number line or take help from the times tables of 3 and 4." Figure: a number line 0, 3, 4, 6, 8, 9, 12 with a rabbit (jumps of 4) and a frog (jumps of 3), 12 boxed. | T3.C3 | 165 |
| cm.list46 | prompt | Animal Jumps: common multiples of 4 and 6 | "Let us write the multiples of two numbers, 4 and 6. ... 12 and 24 are two of the common multiples of 4 and 6. List a few more." | T3.C3 | 166 |
| LUD.Q1 | exercise | Let Us Do (common multiples), Q1 | "Find 5 common multiples of the following pairs of numbers." (a) 2 and 3 (b) 5 and 8 (c) 2 and 4 (d) 3 and 9 (e) 5 and 10 (f) 9 and 12 (g) 8 and 12 (h) 6 and 8 (i) 6 and 9 | T3.C3 | 166 |
| LUD.Q2 | exercise | Let Us Do (common multiples), Q2 | "Food is available at the end of a cobbled road. Robby, the rabbit, takes a jump of 4 each time. Deeku, the deer, takes a jump of 6 each time. They both start at 0. Will both Robby and Deeku reach the food? Who will reach first? How do you know? Explain your answer." Figure: a winding cobbled road of stones 0 to 64, food after 64. | T3.C3 | 167 |
| LUD.Q3 | exercise | Let Us Do (jumps and factors), Q3 | "Mowgli's friends live along the trail on the marked places below. Which of his friends will he be able to visit, if he jumps by 2 steps starting from 0?" Figure: the trail, stones 0 to 60 (last stone printed 59 twice) with the 11 friends. | T4.C3 | 167 |
| trail.three | prompt | Mowgli's Trail: jumps of 3 steps | "Which of his friends will he be able to meet if he jumps by 3 steps? 3 is a common factor of the numbers ___." | T4.C3 | 168 |
| trail.five | prompt | Mowgli's Trail: jumps of 5 steps | "Which numbers will he touch if he jumps by 5 steps? ___. 5 is a common factor of the numbers ___." | T4.C3 | 168 |
| trail.ten | prompt | Mowgli's Trail: jumps of 10 steps | "Which numbers will he touch if he jumps by 10 steps? ___. 10 is a common factor of the numbers ___." | T4.C3 | 168 |
| LUD.Q4 | exercise | Let Us Do (jumps and factors), Q4 | "Let us find some common factors of the numbers 24 and 36. Note that all jumps in the following questions start from 0." (a) 2 steps (b) 3 steps (c) 4 steps (d) other jumps (e) how many common factors, list them (f) 1 step | T4.C3 | 168 |
| LUD.Q5 | exercise | Let Us Do (jumps and factors), Q5 | "What are the common factors of 12 and 13?" | T4.C3 | 168 |
| LUD.Q6 | exercise | Let Us Do (jumps and factors), Q6 | "Find which of the following numbers can be reached by jumps of 4 steps? 4 is the common factor of the numbers ___." Figure: a number line with 0, 10, 16, 27, 36, 48. | T4.C3 | 169 |
| LUD.Q7 | exercise | Let Us Do (jumps and factors), Q7 | "Find the common factors of the following pairs of numbers." (a) 12 and 16 (b) 8 and 12 (c) 4 and 16 (d) 2 and 9 (e) 3 and 5 (f) 12 and 15 (g) 20 and 5 (h) 9 and 21 (i) 6 and 27 | T4.C3 | 169 |
| LUD.Q8 | exercise | Let Us Do (factors and multiples at work), Q8 | "State whether the following statements are true (T) or false (F)." (a) Factors of even numbers must be even. (b) Multiples of odd numbers cannot be even. (c) Factors of odd numbers cannot be even. (d) One of the common multiples of two consecutive numbers is their product. (e) The only common factor of any two consecutive numbers is 1. (f) 0 cannot be a factor of any number. | T5.C3 | 169 |
| LUD.Q9 | exercise | Let Us Do (factors and multiples at work), Q9 | "Sher Khan, the tiger, goes hunting every 3rd day. Bagheera, the panther, goes hunting every 5th day. If both of them start on the same day, on which days will they be hunting together?" | T5.C3 | 169 |
| LUD.Q10 | exercise | Let Us Do (factors and multiples at work), Q10 | (a) "In the trail shown earlier, Sher Khan's house is on number 25 and that of Baloo the bear is on number 30. Mowgli wants to meet his friend Baloo the bear but wants to avoid Sher Khan's house. How long (in steps) could each jump be?" (b) "What number of jumps (in steps) he could choose so that he can meet both Kaa, the snake, at 21 and Akela, the wolf, at 35?" | T5.C3 | 169 |
| LUD.Q11 | exercise | Let Us Do (factors and multiples at work), Q11 | "Sort the following numbers into those that are (a) divisible by 2 only (b) divisible by 5 only (c) divisible by 10 only (d) divisible by 2, 5, and 10." Cards (row by row): 90, 22, 38, 30, 75 / 45, 66, 78, 62, 40 / 84, 56, 25, 95, 55, and three overlapping circles. | T5.C3 | 170 |

Counts: 21 questions (0 examples, 12 exercises, 9 prompts); 13 text ids and 4 talk ids. 38 coverage ids in all.
The book prints no solved example with a number in this chapter, so there is no `Example N` question; the trail lines that print an answer (jump of 2, of 3) are treated as the book's partial answer (`trail.answer2`) and as a prompt (`trail.three`).

## 4. Verified answers (computed with Python; use exactly these)
**Opener.** Out: 28, 36, 48, 72. Common factors 1, 2, 4. Multiplier 1: 28, 36, 48, 72 went in. Multiplier 2: 14, 18, 24, 36. Multiplier 4: 7, 9, 12, 18. 3 fails (9 × 3 = 27, 10 × 3 = 30). (The book prints no answer; the factors 1, 2, 4 are printed in the text below the picture.)
**Arrays.** 15: 1 × 15, 3 × 5, factors 1, 3, 5, 15. 12: 1 × 12, 2 × 6, 3 × 4, factors 1, 2, 3, 4, 6, 12. Blanks: 2 × 6, 3 × 4, 12 × 1, 1 × 12. LUD arrays factors: 10: 1, 2, 5, 10; 14: 1, 2, 7, 14; 13: 1, 13; 20: 1, 2, 4, 5, 10, 20; 25: 1, 5, 25 (5 × 5, three factors); 32: 1, 2, 4, 8, 16, 32; 37: 1, 37; 46: 1, 2, 23, 46; 54: 1, 2, 3, 6, 9, 18, 27, 54. Counts: 4, 4, 2, 6, 3, 6, 2, 4, 8. Prime: 13 and 37 have only the array 1 × n, two factors. (The book prints no answers.)
**Common multiples.** 3 and 4: 12, 24, 36, 48, 60, ... (first 12). 3 and 6: 6, 12, 18, ... 4 and 6: 12, 24, 36, 48, 60, 72 (the book names 12, 24). LUD Q1 first common multiples: (a) 2 and 3: 6; (b) 5 and 8: 40; (c) 2 and 4: 4; (d) 3 and 9: 9; (e) 5 and 10: 10; (f) 9 and 12: 36; (g) 8 and 12: 24; (h) 6 and 8: 24; (i) 6 and 9: 18; five each: (a) 6, 12, 18, 24, 30 (b) 40, 80, 120, 160, 200 (c) 4, 8, 12, 16, 20 (d) 9, 18, 27, 36, 45 (e) 10, 20, 30, 40, 50 (f) 36, 72, 108, 144, 180 (g) 24, 48, 72, 96, 120 (h) 24, 48, 72, 96, 120 (i) 18, 36, 54, 72, 90. Any five are right; the plan shows the first five.
**Q2 road.** Stones 0 to 64, food at the end (the plan reads: stone 64). Robby lands on 4, 8, ..., 64 (4 × 16 = 64). Deeku lands on 6, 12, ..., 60, then 66 (6 × 10 = 60, 6 × 11 = 66): never on 64. Only Robby reaches the food, so Robby is first. Both land on 12, 24, 36, 48, 60.
**Trail.** Friends: ant 4, spider 9, frog 12, bird 14, Kaa 21, Sher Khan 25, Baloo 30, Akela 35, deer 39, rabbit 50, monkey 57; the stones run 0 to 60 (the last stone is printed 59 twice, the plan reads 60). Jump 2: 4, 12, 14, 30, 50 (ant, frog, bird, Baloo, rabbit). Jump 3: 9, 12, 21, 30, 39, 57 (spider, frog, Kaa, Baloo, deer, monkey). Jump 5: touches 5, 10, ..., 60; friends 25, 30, 35, 50. Jump 10: touches 10, 20, 30, 40, 50, 60; friends 30, 50. The book prints 4, 12, 14, 50 for jump 2 and 9, 21, 39, 57 for jump 3 (see SOLUTION_NOTES).
**Common factors.** Q4: 24 and 36: 2, 3, 4 each yes; other jumps 1, 6, 12; common factors 1, 2, 3, 4, 6, 12 (six); 1 step: yes. Q5: 12 and 13: only 1. Q6: 16, 36, 48 reachable (0 is the start); 10 and 27 are not. Q7: (a) 12 and 16: 1, 2, 4; (b) 8 and 12: 1, 2, 4; (c) 4 and 16: 1, 2, 4; (d) 2 and 9: 1; (e) 3 and 5: 1; (f) 12 and 15: 1, 3; (g) 20 and 5: 1, 5; (h) 9 and 21: 1, 3; (i) 6 and 27: 1, 3.
**Q8.** (a) F (3 is a factor of 12); (b) F (3 × 2 = 6); (c) T; (d) T (for example 4 × 5 = 20, 8 × 9 = 72); (e) T; (f) T (the plan's reading: a jump of 0 never leaves 0; the book gives no key).
**Q9.** Common multiples of 3 and 5: 15, 30, 45, 60, ... counting the start as day 0 (the plan's reading).
**Q10.** (a) factors of 30: 1, 2, 3, 5, 6, 10, 15, 30; factors of 25: 1, 5, 25; jumps that meet Baloo and avoid Sher Khan: 2, 3, 6, 10, 15, 30. (b) common factors of 21 and 35: 1 and 7.
**Q11.** 2 only: 22, 38, 66, 78, 62, 84, 56 (7). 5 only: 75, 45, 25, 95, 55 (5). 10 only: none. 2, 5 and 10: 90, 30, 40 (3). 7 + 5 + 3 = 15.

## 5. Tool specs (the 5 tools; `T(...)` with `subtype="manipulative"`)
Build each from `priority_doc.md` section C (read the whole of section C and D first): same names, scenes, objects, phases. Fit the three phases into the `T()` fields: `student_does` has THREE labelled entries: "Phase 1, Recall and get ready: ...", "Phase 2, Play and apply: ...", "Phase 3, Challenge: ...". `challenges` (5 to 7): the first ones are Phase 2 play cards with their answers; the LAST one or two are Phase 3 and quote the book's own questions with their own values and wording (practice values elsewhere are labelled "practice values"). `screen` describes the scene and EVERY control and read-out. `idea` = the single mathematical purpose of this tool, different from every other tool. Feedback is specific; hints climb orienting, strategic, specific, bottom-out.
| doc tool | key | tool_id | title | topic |
|---|---|---|---|---|
| Tool 1 | `hidden_number_box` | `tool_hidden_number_box` | Hidden Number Box | T1 (free try) |
| Tool 2 | `array_maker` | `tool_array_maker` | Array Maker | T2 |
| Tool 3 | `jump_together` | `tool_jump_together` | Jump Together | T3 |
| Tool 4 | `trail_jumper` | `tool_trail_jumper` | Trail Jumper | T4 |
| Tool 5 | `number_sorter` | `tool_number_sorter` | Number Sorter | T5 |

## 6. Misconception ids (defined in content.py; attach by id)
M_ONE_MULTIPLIER (only the biggest multiplier is right), M_FACTOR_MULTIPLE (a factor and a multiple are the same), M_MISS_ONE_SELF (1 and the number itself are not factors), M_PRIME_NO_FACTORS (13 has no factors), M_CM_ONLY_PRODUCT (the first common multiple is the product), M_FIRST_ONLY (only one common multiple, or the list ends), M_CF_CM_MIX (common factors are common multiples), M_JUMP_NEAR (a jump reaches a number it jumps over), M_CF_BIGGEST_ONLY (only one common factor, the biggest), M_EVEN_FACTORS (every factor of an even number is even), M_ODD_MULTIPLES (every multiple of an odd number is odd), M_ZERO_FACTOR (0 is a factor), M_TEN_ONLY (a number divisible by 10 only exists).

## 7. Deliverable and self-check
Files: `topics_1.py` (T1, T1B, T2), `topics_2.py` (T3, T4), `topics_3.py` (T5, T6), `tools_1.py` (tools 1 and 2), `tools_2.py` (tools 3 to 5), each a module-level `TOPICS = []` / `TOOLS = {}` importing from `topics_common`. Check: `cd` into NEW and run the numeric check script in the scratchpad (`check_numbers.py`), the dash scan and the build (`build.py --placeholders`).
