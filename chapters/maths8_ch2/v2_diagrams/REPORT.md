# Class 8 Ch 2 Power Play - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths8_ch2` v35 (taken from staging). Result: new V2 version v36 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (109 items from 62 units)
{"worked_example": {"none": 13, "required": 1, "optional": 1}, "question": {"none": 44, "required": 3}, "solution": {"none": 43, "required": 3, "optional": 1}}

Optional, NOT added: [('C55', 'solution'), ('C123', 'worked_example')]

needs_lp_text_sync: []

## The 7 diagrams
| id | side | type |
|---|---|---|
| M3.S8.T8.C32.IMG1 | question | other |
| M3.S8.T8.C33.IMG1 | solution | other |
| M4.S20.T20.C91.IMG2 | worked example | number_line |
| M4.S21.T21.C96.IMG1 | question | number_line |
| M4.S21.T21.C97.IMG1 | solution | number_line |
| M5.S23.T23.C108.IMG1 | question | number_line |
| M5.S23.T23.C109.IMG1 | solution | number_line |

### Chunk A notes (from the decision agent)
# Chunk A notes: Class 8 Ch 2 "Power Play" (plan cbse_eng_maths8_ch2_v35)

Units: 17 (3 worked examples, 14 pairs) = 31 items. Result: required 2 / optional 0 / none 29. Validator: errors 0, warnings 0.
Only the Stones that Shine tree needs a diagram: question M3.S8.T8.C32 (media M3.S8.T8.C32.IMG1) and solution M3.S8.T8.C33 (M3.S8.T8.C33.IMG1, derived_from the question figure).

Note on the brief: it says the pdf has no printed-solutions section. It does: pdf pages 30 to 38 are the NCERT answers (Page No. 22 ... 45). I read them against my units. All of their answers are text; none has a picture (the only answer pictures in the pdf are P33 and P34, which belong to other chunks). The LP solution text was still the one followed.

## Judgement calls

1. M3.S8.T8.C32 question (required). The LP text says only "In the story, find ...". The story's branching (king, 3 daughters, 3 baskets each, 3 keys each, 3 rooms each) is what the book's tree shows (P05), and the learner counts the rooms from it, so FIG_REFERENCED + DATA_IN_FIGURE. The tree stops at the rooms level; the tables, necklaces and diamonds of the story are not in the book's picture and are not drawn. I checked the base description against a zoomed crop of page 5: 3 keys under each of the 9 baskets (27 keys), each key has 3 prongs (27 fork icons x 3 = 81 rooms). The base `unclear` doubt (is an icon one room or three) is settled by the picture: one icon = 3 prongs = 3 rooms.
2. M3.S8.T8.C33 solution (required). The solution counts level by level (3, 9, 27, 81). The complete final state is the same tree with those four counts in ANSWER green, before step 1. The 2187 diamonds come from the text, not from the picture. Used two inventory entries for the one book tree: P05-tree_diagram-1 (question) and NEW-P05-tree_diagram-1-sol (solution).
3. Diagram type `other` (a plain branching tree; the catalogue has no tree type that fits). Layout is given by unit coordinates (x formulas: rooms x = k, keys 3j-1, baskets 9i-4, daughters 27d-13, King 41) so the renderer cannot guess; all positions were recomputed in code (each parent is at the mean x of its 3 children).
4. The book's tree has coloured panels, daughter faces, baskets and keys as pictures. The spec uses plain circles and squares (no cartoon art), because the figure rule allows only what carries the maths.
5. Plain Fold/Thickness tables (P02-table-1 to 4, P03-table-1 to 3) are all LATEX_TABLE, siblings of each other. P03-table-4 (coloured header, x1024 table) is mapped to concept image M1.S2.T2.C4.IMG1 (same idea, accounting only).
6. Factorisation items (C17/C18 the 32400 item, C21/C22, C23/C24) are all `none` for the same reason (number chains = LATEX_ARITHMETIC), so the siblings agree. The book's division ladder (P04) is a worked-example teaching picture; mapped none:LATEX_ARITHMETIC.
7. Figure it Out items (C21 = book FiO Q1, C23 = Q2, C25 = Q3, C40 = Q4 of the second set, C42 = Q10): all have text answers in the book too, all `none`.
8. Book figures P06-brace_diagram-1 and P06-table-2 are teaching working; mapped to concept images M3.S7.T7.C27.IMG1 and M3.S7.T7.C29.IMG1 (accounting only, nothing linked).
9. Not added to the inventory (decoration, Step 0): the Burj Khalifa picture on page 2, the king-and-daughters art on page 5, the paper-stack art and children on page 2, the two banknote photographs on page 26 (they belong to the "Pinch of History" text, other chunk).

## LP text issues

- M1.S3.T3.C8 (question): says "using the thickness table", but the table is not in the question text and the concept image C2.IMG1 shows only the first doublings. Suggested: add the table as a LaTeX array (folds 1 to 17, and fold 0 = 0.001 cm, fold 20 = about 1048.5 cm), or at least the values the solution uses: "Fold 3 = 0.008 cm, fold 4 = 0.016 cm, fold 5 = 0.032 cm, fold 7 = 0.128 cm, fold 0 = 0.001 cm, fold 10 = 1.024 cm, fold 20 = about 1048.5 cm."
- M3.S8.T8.C32 (question): "In the story" but the story is not stated. The figure covers king to rooms only, so the rest must be in the text. Suggested: "A king had three daughters. Each daughter got three baskets, each basket had three keys, each key opens three rooms, each room has three tables, each table has three necklaces and each necklace has three diamonds. Find the number of rooms and the number of diamonds." (The book words it as a verse: "Each room had tables - one, two, three, with three bright necklaces on each ... each necklace had three diamonds".)
- M1.S3.T3.C6 (question) and M1.S2.T2.C3 (worked): "starting from about 10.4 m after 20 folds" does not give the LP's own values: 10.4 x 2 = 20.8, then 41.6, 83.2, 166.4, 332.8, whereas the steps say 21, 42, 84, 168, 336. Those come from the exact 10.485 m (1048.576 cm), which C9 uses as "about 1048.5 cm". Suggested: "about 10.5 m (10.485 m)" in C6 and C3, or keep the book's "about 10.4 m" and say "values are rounded from 10.485 m".
- Book numbers: M2.S6.T6.C23 ("Figure it Out, Q1") is book FiO Q2 (648, 405, 540, 3600); M2.S6.T6.C25 ("Q2") is book FiO Q3; M3.S9.T9.C42 ("Figure it Out, Q1") is book FiO (second set) Q10. Two different questions are both labelled "Figure it Out, Q1". Suggested labels: "Figure it Out, Q2 (first set)", "Q3 (first set)", "Q10 (second set)". M3.S8.T8.C40 "Power Play, Q4" is book Q4 of the second set (correct).
- M2.S5.T5.C21 (question_tex): the sub-part separators are uneven: "(i): ...; (ii): ... (iii) ... (iv): ...; (v): ... (vi) ...". Suggested: one style, e.g. "(i) ... (ii) ... (iii) ...".
- M3.S8.T8.C35 and C37, C39, C41 (the plain `question` field): the exponents are spelled out ("p⁴ × p to the power 6", "4 to the power 6"). Suggested: use the symbols as in `question_tex` ("p⁴ × p⁶", "4⁶", "(2⁵)²", "q⁴⁶").
- No wrong answers found: I recomputed all LP numbers of the 17 units (thickness values from 21 m to 703687 km, ratio checks 4, 8, 1024, 2^10 v, 12 and 64, 32400 = 2^4 x 5^2 x 3^4, 648, 405, 540, 3600, the six values 2000 ... -32000000, 2187 = 81 x 27 = 9 x 243, 512, 78125, 4096 both ways, 1024, the power-of-a-power forms, the sixth powers 729 and 4096). All hold.

## Borderline

- C6/C7 (fill the thickness table, folds 21 to 45): `none` via LATEX_TABLE for both sides. The answer is a filled 25-row table, so ANSWER_IS_FIGURE could be argued, but the table is plain numbers with no colour meaning, and the tie-breaker (a careful student loses nothing with a LaTeX array) says text. If the user wants it as a picture, C7 solution is the place (derived_from none, since the question side stays none).
- C8 question: the book question depends on the plain thickness table (FIG_REFERENCED could be argued, "cannot be answered without it"). Kept `none` because the LATEX_TABLE rule delivers a plain table as text, but this item needs the LP text issue above fixed to be answerable.
- C33 solution: `required` because the counts are written on the tree and the solution is built on them. It could be argued `none` (SAME_AS_QUESTION_DIAGRAM + numbers in text). Kept required: the picture shows the final state with the new marks.
- C17/C18, C23/C24 factorisation ladders: a prime ladder would help, but the divisions are a number chain already in the steps (v3: LATEX_ARITHMETIC). Not made `optional` so that no ladder is requested for the four sub-parts of C24.
- C3 worked example: a height scale (670 m against 830 m, 10.7 km against 11 km) would be nice, but the plan already has it as teaching image C3.IMG1 (never linked), so `none`.

## Book doubts

- Page 2 and page 3: fold 20 is printed "about 10.4 m", the exact value is 10.4858 m (the book truncates). The LP mixes "about 10.4 m" (C3, C6) and "about 1048.5 cm" (C9).
- Page 3, table "Times increased by", row 2: "10.485 m - 1.024 cm = about 10.474 m". Exactly 10.485 m - 0.01024 m = 10.4748 m, so the book truncates instead of rounding (10.475). Not drawn (teaching table).
- Page 5, under the tree the book prints 3 x 3 = 9, 9 x 3 = 27, 27 x 3 = 81 and a fourth line 81 x 3 = 243. The fourth line is not a rooms count (the rooms are 81 = 3^4); 243 = 3^5 is the stepping stone to the diamonds (9 x 243 = 2187). The diagram follows the four levels only (3, 9, 27, 81).
- Page 5, tree picture: the picture shows rooms as 27 fork-like icons of 3 prongs; the book never says one prong is one room. The text (3^4 = 81 rooms) fixes it.
- Page 35, FiO Q4 (i): the printed reason says it holds "for numbers that have powers as 6" (n^6 = (n^2)^3 = (n^3)^2); the LP uses the counter-example 8 against 64. Same verdict (only sometimes true); the LP wins.

### Chunk B notes (from the decision agent)
# Chunk B notes (Class 8 Ch 2 "Power Play", plan cbse_eng_maths8_ch2_v35)

Units: topics M3.S11.T11, M3.S13.T13, M3.S14.T14, M4.S15.T15, M4.S16.T16, M4.S17.T17, M4.S18.T18 = 18 units (14 pairs, 4 worked examples) = 32 items.
Result: required 0 / optional 1 / none 31. Validator: errors 0, warnings 0.

Why nothing is required: this chunk is exponent arithmetic (powers of 2, 5, 10, 26, 36, reciprocals, exponent rules). I looked at the page pictures of pdf pages 7, 8, 9, 10, 11, 26, 27 (questions) and 32, 35, 36, 37 (printed answers). The book gives none of these questions a figure of its own, and none of the printed answers is a picture. Every number a question needs is in the LP question text. The book pictures in these sections are teaching or decorative figures (pond girl, padlock photo, Estu's cap-and-dress arrows, the digit-mapping lines, the formula box, the "When Zero is in Power!" cartoon, banknote photographs).

Note for the brief: the brief says this pdf has no printed-solutions section, but pdf pages 30-38 do hold printed answers ("Page No. ... Ans:"). I read them for every item (all text, no pictures).

## Borderline

1. M3.S11.T11.C54 / C55 (Figure it Out Q7, "Circle the numbers that are the same"). Chosen: question `none` (NUMBER_LIST_IN_BOXES, TEXT_SUFFICIENT), solution `optional` (NUMBER_LIST_IN_BOXES, HIGHLIGHT_MEANING), not added. Why: the book prints five expressions in one plain row (no boxes, no colour) and the LP question text already lists all five; v3 "Not a diagram" says a board of numbers to choose from is listed in text, and for the solution side (arrows or circles on such a list) allows only `optional` when the LaTeX answer already gives the result. The printed answer on pdf page 36 is words ("2^4 x 3^6, 6^4 x 3^2 and 18^2 x 6^2 are same"), not a marked picture. If the user wants a circled-row picture anyway, it would be a `cell_row`-style card: five expressions in one row, the first, second and fourth circled in FOCUS, nothing else. Not specified in full because it is not added.
2. M3.S13.T13.C60 / C61 (Estu's and Roxie's outfits). Chosen: both sides `none` (TEXT_SUFFICIENT / LATEX_ARITHMETIC). The book hint says "Try drawing a diagram like the one above" and the book does draw Estu's tree (a teaching figure, mapped to concept image C56), but the question gives no figure and the printed answer is only "7 x 2 x 3 ways". A choice tree for Roxie (7 dresses x 2 hats x 3 shoes) would be nicer but is not needed to solve it exactly as well from the text.
3. M4.S15.T15.C70 (halving a line of 16 units, worked example) and M4.S17.T17.C78 (halving past 1). Chosen: `none`. A picture of the line halved would be a nice visual, but the book draws no line here (it is "imagine a line of length 16 units"), the numbers are all in the text, and the plan already carries a teaching image for each idea (C70.IMG1, C78.IMG1) that stays and is not linked.
4. M3.S13.T13.C62 and C64 (password locks). The book's digit-mapping picture (lines from digit 0 to all ten digits) is a teaching figure and was mapped to the nearest plan teaching image (C57 "Five slots, ten choices each"): the idea is the same (10 choices per slot) but it is not the same drawing. If the merge wants an exact match, change the mapping to `none:TEXT_SUFFICIENT`; nothing else changes.
5. P11-table-2 (the green box of three general rules on pdf page 11): claimed by this chunk as `none:TEXT_SUFFICIENT` because it sits in the 2.3 section of C79, C83 and C85. If chunk C (Power Lines, same page) also claims it, the meaning should stay "formulas only, no figure needed".

## Figures

- P08-arrangement-1 -> concept_image:M3.S12.T12.C56.IMG1 (Estu's caps and dresses arrows; description checked against page_08.png, correct).
- P09-mapping_diagram-1 -> concept_image:M3.S12.T12.C57.IMG1 (checked against page_09.png, correct).
- P11-table-2 -> none:TEXT_SUFFICIENT (checked against page_11.png, correct).
- P27-number_row-1 -> none:NUMBER_LIST_IN_BOXES (checked against page_27.png, correct).
- NEW-P10-zero-cartoon -> none:DECORATIVE_ONLY (found by me: the six-panel cartoon "When Zero is in Power!" on page_10.png; missing from the base inventory).
- Not listed, as pure decoration per Step 0: the girl by the lotus pond (page 7), the padlock photograph and the worried-girl speech bubble (page 9), the owl tip box (page 8), the two banknote photographs at the top of page 26 (sit above Figure it Out, shared with other chunks' questions).
- Not claimed by this chunk (they belong to other chunks' sections): P11-number_line-1 (power line of 4), P12-number_line-1, P33-power_line-1, P33-number_line-1, P34-number_line-1 and the P06 / P05 figures.

## LP text issues

No arithmetic mistake found: I recomputed every number in the 18 units (2^30 and 2^29; 16 x 81 = 1296; 10000 / 625 = 16; 11664 for all three equal expressions; 14 x 3 = 42; 26^6 = 308915776; 36^5 = 60466176; 10^9 < 8,500,000,000 < 10^10; 2^160 ends in 6; every simplification in C86 and C88). The points below are wording only; nothing was changed.

- M3.S11.T11.C54 (question): "Circle the numbers that are the same" cannot be done on a text-only page. Suggested sentence: "Which of these numbers are the same? 2^4 x 3^6, 6^4 x 3^2, 6^10, 18^2 x 6^2, 6^24. Write them down." (The answer text already names the three, so only the question needs it.)
- M4.S18.T18.C88 (solution step (iv)): "$-2 \times -3 = 6$" puts two minus signs side by side. Suggested: "$(-2) \times (-3) = 6$, so $13^{6}$."
- M4.S18.T18.C85 / C86 and C87 / C88: the question lists parts (i) to (v) (C87) or separates them with semicolons (C85) while the solution steps for C85 / C86 carry no part letters. Suggested for C86: start each step with its part letter, "(i): Add exponents ...", as C88 already does.
- M3.S13.T13.C60 (question): the book's hint "Try drawing a diagram like the one above" is missing from the LP question text; it is not needed for the answer, but if a choice tree is wanted later the question should say so.
- M3.S13.T13.C62 / C63: no missing data. The answer lists 100, 1000 and 100000 and the steps also give 4 digits (10000); fine.
- No missing data was found that only a figure could carry in any unit of this chunk.

## Places where the book itself is unclear or slipped

- pdf page 8 (book p.26): "You can list them all: 000, 001, 002, ....., 997, 997, 999." prints 997 twice; it should read 997, 998, 999. Print slip, in the teaching text for T12 (not an item of this chunk; no diagram is affected).
- pdf page 9 (book p.27): "Halving 16 cm three times may be written as ..." says cm while the lines before it say units. Not corrected anywhere (no diagram drawn).
- pdf page 27 (book p.45): Figure it Out Q12 labels its options "(ii) 20^9 (ii) 10^11 (iii) ..." with (ii) twice. Not an item of this chunk.
- The book's printed answer for the Figure it Out Q5 (iii) and (i) gives "9^-11 or 1/9^11" and "10^-7 or 1/10^7"; the LP (C88) gives only the negative-exponent form for (i) and (iii). Both forms are right.

### Chunk C notes (from the decision agent)
# Notes, chunk C (Class 8 Ch 2 "Power Play", plan cbse_eng_maths8_ch2_v35)

Result: 30 items (18 units). required 5, optional 1, none 24. Validator `--chunk C`: errors 0, warnings 0.

| Item | Decision | Diagram |
|---|---|---|
| M4.S20.T20.C91 worked example | required | power line of 4 + the 3 expressions (M4.S20.T20.C91.IMG2; IMG1 is the kept teaching image) |
| M4.S21.T21.C96 question | required | power line of 7 + the 8 expressions (IMG1) |
| M4.S21.T21.C97 solution | required | same, with the 8 results in ANSWER green (IMG1, derived_from C96.IMG1) |
| M5.S23.T23.C108 question | required | blank Sun-Saturn line (IMG1) |
| M5.S23.T23.C109 solution | required | same line in 10 equal parts, Earth at tick 1 (IMG1, derived_from C108.IMG1) |
| M6.S25.T25.C123 worked example | optional (not added) | the book's Earth-ladder-Moon sketch would help |
| all other 24 items | none | text / LaTeX |

Aspect ratios: the two power-line figures are tall (12 and 11 rows with stacked fractions), so they are 4:3 (canvas 12 x 9 units); the Sun-Saturn line is a long strip drawn on a 16:9 canvas. All coordinates in the specs are in canvas units (origin at the centre).

## 1. Judgement calls

- **C91 (worked example, power line of 4): required.** The example says "Use the power line of 4"; the values of 4^8 ... 4^-2 live only in that line, so it is treated exactly like the power line for 7 (C96). The diagram is the GIVEN state: the line plus the three expressions of the LP question (as the book prints the power line for 7 with its expressions beside it). The book's own picture of the line of 4 also carries curved arrows and two merging brackets (a teaching figure that shows the answer 4^5); those are not drawn. The book's right bracket reads `16384 x 1/16`, the LP reads `16384 / 16`; same value, the LP is followed. P11-number_line-1 is mapped to this item (the teaching image M4.S20.T20.C91.IMG1 is not linked).
- **C97 (solution of power line of 7): no arrows.** The book's printed answer picture has none. The LP `s_figure` hint speaks of arrows from each expression to the power it lands on; not drawn, because 7^-6 (the last result) lies below the end of the line (7^-4) and an arrow would have nowhere to land. One picture carries all eight results even though the LP card has two card ids (IMG1, IMG2): a pair gets one solution diagram.
- **Number style in the power-line figures.** No commas anywhere (823543, 2401 x 49, 16807, 117649, ...), as in the LP text and on the line itself. The book prints Indian commas in the expressions (2,401; 16,807; 8,23,543; 1,17,649) but plain digits on the line. The 8 expressions are reproduced from the book's picture, not as instructions.
- **C108 / C109 (Earth on the Sun-Saturn line).** Question figure = only what the book prints: the line with `Sun` and `Saturn` ticks (no values, no Earth). Solution figure = the book's printed answer: the line in 10 equal parts, `Earth` at the first tick (nearest tick to the true ratio 1.496e11 / 1.4335e12 = 0.104). The added ticks and the Earth label are ANSWER green (added by the solution); the given ticks and labels stay INK.
- **P33-number_line-1** is the question's number line reprinted in the answers part, so it is accounted as `none:SAME_AS_QUESTION_DIAGRAM` (the printed answer picture itself is P34-number_line-1, mapped to the C109 solution).
- **P14-illustration-1** (painted Sun, Saturn, Uranus strip, no labels or numbers) is `none:DECORATIVE_ONLY`; the question is answered from the printed distances.
- **P29-expression_pair-1 and -2** (handwritten Tremendous in Ten expressions): `none:TEXT_SUFFICIENT`. The same expressions are in the LP question text; the red/blue colour only says who wrote it. So C114 is none/none.
- **Concept-image accounting (nothing is linked):** P15-illustration-1 -> M6.S25.T25.C120.IMG1; P18-schematic-1 and P18-expression_braces-1 -> M6.S25.T25.C123.IMG1.
- **C120 (Tulabhara): none.** The book picture is two scene illustrations (Roxie and Estu in a balance pan against jaggery / wheat) with no numbers; the numbers are assumptions given in the text.
- **C121, C122: none.** The book prints no figure for the coin question; the padayatra crowd strip on p.17 is scene art.
- **Figures not claimed, deliberately.** (a) P11-table-2 (the green box of the three general forms on book p.29 / pdf p.11) sits in section 2.3 above the "Power Lines" heading and belongs to the Zero and Negative Exponents topics (chunk B); if no chunk claims it, the merged check will say so. (b) The two banknote photographs at the top of pdf p.26 (Hungarian 1 milliard pengo, Zimbabwe 100 trillion dollars), the dinosaur comic on p.14, the padayatra crowd strip and the ladder-to-the-Moon scene on p.17: photographs or pure scene art that no item of this chunk works on; the inventory rules skip them, so no `NEW-` entries were made.

### Borderline
- **C91 required** (the LP steps already give 65536 = 4^8 etc., so a careful student could follow from text; kept required because the example is explicitly "use the power line" and for consistency with C96). Alternative: none / TEXT_SUFFICIENT.
- **C94 question: none** although the power line of 4 (pdf p.11) is on the previous page. The question text carries 16384, 1024, 4^2 and 4^-2 and never says "use the line". Alternative: required (DATA_IN_FIGURE).
- **C123 worked example: optional** (not added): the Earth-ladder-Moon sketch with "20 cm" and "3,84,400 km" would help but the text gives both numbers; the two growth expressions (20 + 20 + ..., 0.001 x 2 x 2 ...) can be LaTeX.
- **C106 question: none**: the three large-number facts are plain text in the book; they are missing from the LP text (see below), which does not change the decision.
- **Tall figures at 4:3**: if the builder wants every card strictly 16:9, the power-line figures will be letterboxed.

## 2. LP text issues

- **M5.S23.T23.C106** (question; also C107 steps refer to it): the question says "write the three large-number facts in scientific notation" but never states the facts. Suggested sentence: "The Sun is 30,00,00,00,00,00,00,00,00,000 m from the centre of the Milky Way; our galaxy has 1,00,00,00,00,000 stars; the Earth has a mass of 59,76,00,00,00,00,00,00,00,00,00,000 kg." (zeros checked: 3 x 10^20, 1 x 10^11, 5.976 x 10^24, as the LP solution says).
- **M5.S23.T23.C108** (question): it never says the Earth is to be marked on the number line with the Sun and Saturn ends. Suggested sentence: "On the number line below, with the Sun at one end and Saturn at the 1.4335 x 10^12 m mark, show where the Earth (1.496 x 10^11 m from the Sun) sits."
- **M4.S19.T19.C89, M5.S24.T24.C116, M5.S24.T24.C118** (book numbers): the LP calls them "Figure it Out, Q1", "Figure it Out, Q1", "Figure it Out, Q2"; in the book they are Q3, Q6 and Q12 (ncert_refs FiO2.q3, FiO2.q6, FiO2.q12 are right). The LP numbering restarts in each topic.
- **M4.S21.T21.C95** (answer_tex): "$4^2$ is $4^4$, which is $256$, times $4^{-2}$" is correct but reads awkwardly. Suggested: "$4^2$ is $4^4 = 256$ times larger than $4^{-2}$."
- **M5.S22.T22.C100**: ncert_refs lists `2.4.comic` but neither the question nor the steps use the dinosaur comic. Harmless.
- Checked and correct (recomputed): C90 (all nine products equal 2^18, 2^48 x 3^8, 2^-25), C91 (all three = 1024 = 4^5), C95 (16384/1024 = 16, 4^2 / 4^-2 = 256), C97 (eight results), C105, C107, C109 (0.104), C111 (4, 4, 6, 10), C113, C115, C117, C119, C121 (11250), C122 (16 days, 3066000 km, 76.65), C123 (1922000000 steps = 192 crore 20 lakh), C126 (200 = 2 x 10^2).

## 3. Book doubts

- pdf p.27 Q12: the option labels are printed "(ii) 20^9, (ii) 10^11, (iii) 10^10 ..." (the first (ii) should be (i)); the LP relabels it (i). The book's printed answer says only (vi); the LP rightly says (v) is equally correct.
- pdf p.33 printed answer for the power line of 7: the equations show 49^3 = 7^6 and 1/343 x 1/343 = 7^-6, both right; no print slip found. The line itself ends at 7^-4, so 7^-6 is only a result, not a tick.
- pdf p.14 number line: the inventory said the Saturn tick is about 6/7 along the line; measured on the page picture it is at 0.9 (the line runs about one tenth of the Sun-Saturn length past Saturn, the same as the printed answer picture). Corrected in the figure_inventory description.
- pdf p.34 printed answer: Earth is drawn at tick 1 of 10 (0.1) while the exact ratio is 0.104; kept as drawn.
- pdf p.35 printed answer for Figure it Out Q3 (book numbering) (ii)/(iii): the book lists `2^40 x 2^8 x 3^8`, `2^40 x 6^8`, `4^-12 x 2^-1`; all are valid products but differ from the LP samples (also valid). Not a diagram.
- pdf p.33 printed answer (172 = 1 x 10^2 + 7 +10^1 + 2 x 10^0) has a slip ("7 +10^1" for "7 x 10^1"); the item in this plan (5642, 561.903) is not affected.

### Chunk D notes (from the decision agent)
# Chunk D notes (Class 8 Ch 2 "Power Play", topics M6.S28.T28, M6.S29.T29, M6.S30.T30, M6.S31.T31)

Result: 16 items (7 question, 7 solution, 2 worked example), required 0 / optional 0 / none 16. Validator: errors 0, warnings 0.
Figures claimed: 11 base figures, all `none` (4 LATEX_TABLE for the time table, 2 LATEX_TABLE for the names tables, 3 TEXT_SUFFICIENT for the facts lists, 2 DECORATIVE_ONLY). No concept image claimed.

Why nothing is drawn: I looked at pdf pages 18-25, 27 and the answers appendix pages 34, 35, 38. The book prints no drawing that a question of this chunk gives or that a printed answer is. What it prints is (a) a margin-label list of facts with blanks (pp.18-20), (b) a plain time table in four parts (pp.21-24), (c) two plain names tables (p.25), (d) a comic panel with the number 69,70,710 and a noodle comic, (e) illustrations (stamps, murmuration photo, krill, balance of ants and animals, sand castles, mayfly, Mangalyaan, mammoth, terror bird). The printed answers (pp.34-38) are text only. Every solution here is arithmetic with powers of 10 or one line of word reasoning, so each solution is `none` (LATEX_ARITHMETIC) and each question is `none` (TEXT_SUFFICIENT / DECORATIVE_ONLY).

## 1. Judgement calls
- **M6.S28.T28.C132 (Q1) and C134 (Q2), question side: none, although the LP question text does not carry the data.** The numbers (starlings 1.3 billion, mosquitoes 110 trillion, people 8e9, elephants 4e5; ants 2e16, trees 3e12, leaves per tree 1e4) live in the book's facts list. That list is a hanging-indent list of sentences, with no rules, colour or drawing; it is text, so no v3 trigger (FIG_REFERENCED / DATA_IN_FIGURE need a picture) applies. The earlier author's hint `q_figure` ("a short list of the numbers used") describes exactly that list. Per your decision 2 I did not turn the item into `required` to compensate; the missing sentences are in section 2. I put the sentence in `text_alternative` of the item so the text side can use it.
- **M6.S28.T28.C136 (Q3): none.** The only picture is the comic panel whose bubble reads "I am 69,70,710 ... old". The number is already in the question text, so DECORATIVE_ONLY + TEXT_SUFFICIENT. I read the digits in the page picture: plain digits, one size, no raised exponents (the base inventory was unsure).
- **M6.S28.T28.C138 (Q4): none.** The Kelenken blank (15 million years to seconds) and the Try This (stars, water) both give all numbers in the question text. The time table is plain.
- **Worked examples M6.S30.T30.C144 and C145: none.** The book's picture for them is the plain names table on p.25 (words | numerals | powers of 10, no colour). The concept images C144.IMG1 and C145.IMG1 are staircase drawings of the same names, not that table, so I did not claim the table as `concept_image` (accounting would be untrue); it is `none:LATEX_TABLE`. A LaTeX array for each is suggested in `text_alternative`, optional.
- **M6.S31.T31.C147/C148 (first part of each name): none/none.** The book bolds mi, bi, tr, quad, quin to point at the "first part"; bold is text. The answer is a sentence plus 10^(3+3n). The concept image C146.IMG1 already shows the picture of 1000 multiplied on.
- **Figures left to other chunks:** P18-schematic-1 (ladder Earth to Moon) and P18-expression_braces-1 belong to the "Linear Growth vs. Exponential Growth" part of p.18 (topics M6.S25/S26, chunk C), not to "Getting a Sense for Large Numbers". P27-number_row-1 is Figure it Out Q7 (another chunk), and the Puzzle Time figures P29-* sit in chunk C's units. I claimed none of these.

## Borderline
- C147 question: bold first parts (HIGHLIGHT_MEANING could be argued; bold is plain text, so none).
- C147 solution and worked examples C144, C145: a picture (strips of 1000s, staircase of names) would help understanding, but the concept images already teach it and the text is complete. Kept `none`, not `optional`.
- C132 and C134 questions: the data is outside the LP text (see section 2). Kept `none` as the book gives no figure.
- C136 question: comic panel with the number in a bubble (decorative, number in text).

## 2. LP text issues
- **M6.S28.T28.C132 (Q1 question):** the question asks for "the starling and mosquito populations" but never gives them, nor the numbers of people and elephants. Suggested sentence to add: "The starling population is about 1.3 billion (1.3 arab) and the mosquito population is about 110 trillion (11 neel); there are about 8 × 10^9 people and about 4 × 10^5 African elephants."
- **M6.S28.T28.C134 (Q2 question):** the ants, people, starlings and trees numbers and the leaves per tree are missing (only 10000 birds, 0.001 cm and 384400 km are given). Suggested sentence: "There are about 2 × 10^16 ants (20 quadrillion), 8 × 10^9 people, 1.3 × 10^9 starlings and 3 × 10^12 trees, and about 10^4 leaves on each tree."
- **M6.S28.T28.C135 (Ans2):** step 1 uses "2 ÷ 8" and "16 − 9" without saying the ants are 2 × 10^16 and the people 8 × 10^9. Suggested first step: "Ants per human: (2 × 10^16) ÷ (8 × 10^9), so 2 ÷ 8 = 0.25 and 16 − 9 = 7, giving 0.25 × 10^7, which is 2.5 × 10^6."
- **M6.S28.T28.C136 (Q3 question):** "decide what unit 6970710 is in" does not say who says it. The book's bubble reads Roxie: "I am 69,70,710 ... old." Suggested: "Roxie also says, 'I am 6970710 ... old.' Decide what unit 6970710 is in." Also the book asks for Estu's date of birth (4070 days) and for how old one is after a million seconds; the LP rewrites these as "age in years" and "how many days a million seconds is". The LP answers are right for what they ask (and match the book's 'about 12 days'), but the question no longer asks the book's question; consider "find Estu's date of birth" as in the book.
- **M6.S28.T28.C140 (Q5 question):** part (i) needs the world population, 8.2 × 10^9, which the book gives only in the facts list; the question text does not. The LP solution states it, the question does not. Suggested: add "The world population is about 8.2 × 10^9." Parts (iv) needs assumptions (the solution states 1 hour a day for 70 years); fine as the book's answer does the same.
- **M6.S29.T29.C142 (book number):** `book_number` is "Figure it Out, Q1" but this is end-of-chapter Q14 of the book (Try This, p.27); C140 is labelled "Power Play, Q13". Suggested labels "Figure it Out, Q13" and "Figure it Out, Q14" (or the same style for both).
- **M6.S30.T30.C145 (worked example, step 4):** "the atoms are at most 10^82, so a googol is 10^18 times as many" should read "at least 10^18 times as many" (the book gives 10^78 to 10^82 atoms, so the ratio is between 10^18 and 10^22). The question also never states the atoms figure, only the steps do.
- **M6.S31.T31.C148 (Ans1):** the question lists million first, but the answer starts at billion. Suggested extra step: "mi means 1: a million is 1000 with 1 more 1000 multiplied on, 10^(3+3×1) = 10^6."
- **M6.S31.T31.C147 (question):** the book prints the first part in bold (**mi**llion, **bi**llion, **tr**illion, **quad**rillion, **quin**tillion); the LP text does not, so the student is not told which part is meant. Suggest bolding them.

Arithmetic of all nine LP solutions was recomputed and holds (116160 hours; 6970710 / 1440 = 4840.77; 4070 = 11 × 365 + 55; 10^6 / 86400 = 11.57; 8.2 × 3 = 24.6 so 2.46e11; 3.8 × 8.2 = 31.16; 3600 × 365 × 70 = 91,980,000; 1.5 × 3.15 = 4.725; 2e25 / 16 = 1.25e24 ml, / 200 = 6.25e21 glasses, × 10 s = 6.25e22 s; 1e9 / 86400 = 11574; 10^100 / 10^82 = 10^18). The LP answers agree with the book's printed answers (pp.34-38), including 'about 12 days' (LP 11.57 / 11.6).

## 3. Where the book itself is unclear or slips (nothing is drawn from any of these)
- p.21 bubble "69,70,710": digits look plain; read as 6970710 (matches the LP: about 4840.8 days in minutes).
- p.25 International table, trillion row: "= 1,00,000,000,000" uses Indian-style commas; the international form is 1,000,000,000,000.
- p.22 Mangalyaan row: 298 days is printed as about 2.65 × 10^7 seconds, but 298 × 86400 = 2.57 × 10^7.
- p.21 first row of the time table: 10^2 s printed "≈ 1.6 minutes" (100 / 60 = 1.67, so about 1.7).
- p.24: the dash bullet before "The oldest fossil evidence ..." is missing in print.
- p.26-27 printing: Q12's sub-parts are labelled (ii), (ii), (iii), (iv), (v), (vi) (first should be (i)); not in this chunk.
