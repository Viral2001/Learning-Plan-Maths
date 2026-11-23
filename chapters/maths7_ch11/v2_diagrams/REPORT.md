# Class 7 Ch 11 Finding Common Ground - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths7_ch11` v30 (taken from staging). Result: new V2 version v31 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (123 items from 69 units)
{"question": {"none": 51, "required": 3}, "solution": {"none": 42, "optional": 1, "required": 11}, "worked_example": {"none": 13, "required": 2}}

Optional, NOT added: [('C9', 'solution')]

needs_lp_text_sync: []

## The 16 diagrams
| id | side | type |
|---|---|---|
| M1.S9.T9.C26.IMG2 | worked example | division_ladder |
| M1.S10.T10.C29.IMG1 | solution | division_ladder |
| M1.S15.T15.C45.IMG1 | solution | other |
| M1.S15.T15.C47.IMG1 | solution | other |
| M1.S18.T18.C57.IMG1 | solution | other |
| M1.S18.T18.C59.IMG1 | solution | other |
| M3.S31.T31.C104.IMG1 | solution | other |
| M3.S31.T31.C106.IMG1 | solution | other |
| M3.S32.T32.C110.IMG2 | worked example | division_ladder |
| M3.S33.T33.C113.IMG1 | question | division_ladder |
| M3.S33.T33.C114.IMG1 | solution | division_ladder |
| M3.S33.T33.C115.IMG1 | question | division_ladder |
| M3.S33.T33.C116.IMG1 | solution | division_ladder |
| M3.S33.T33.C118.IMG1 | solution | division_ladder |
| M3.S37.T37.C137.IMG1 | question | object_row |
| M3.S37.T37.C138.IMG1 | solution | object_row |

### Chunk A notes (from the decision agent)
# Chunk A notes (Class 7 Ch 11, section 3.1, units 1-18, M1.S3.T3 to M1.S16.T16)

Result: 32 items = required 4 / optional 1 / none 27. Questions: 14 none. Solutions: 3 required, 1 optional, 10 none. Worked examples: 1 required, 3 none.
Validator: errors 0 (4 warnings, all expected: 3 long factor-row strings in C47's visible_text, and C29 has no book figure to map to).

Required diagrams (media ids):
- M1.S9.T9.C26.IMG2 (worked example, add_new_image, block_index 0): the two division ladders for 105 and 30, side by side.
- M1.S10.T10.C29.IMG1 (solution): the division ladder for 1200 (6 rows, last number 5).
- M1.S15.T15.C45.IMG1 (solution): Example 1, three blocks with the matching subparts of 45 and 75 ringed, HCF = 15.
- M1.S15.T15.C47.IMG1 (solution): Example 2, five blocks with the matching subparts of 112 and 84 ringed, HCF = 28.

## 1. Judgement calls

1. **C28/C29, 1200 by the division method: solution required, question none.** The book prints no ladder for 1200 (only "Try finding ... using the method above"), so no base figure maps to C29 (validator warning is expected). I required it because the question names the method and the method IS the ladder layout (B2: answer is an arrangement/construction even when the steps describe it in words); the LP steps only list the divisions. The ladder is computed from the LP steps (2,2,2,2,3,5 then 5). If the user prefers text only, flip C29 to none (LATEX_ARITHMETIC); nothing else depends on it.
2. **C26 worked example (105 and 30): required, ladders only.** The LP question says "use the division method", the book draws the two ladders (P04-division_method-1 and -2), and the steps say "write 3 on the left and 35 below". One diagram holds both ladders (one block, one item). No result line ("105 = 3 × 5 × 7") is drawn, to keep the figure to the ladder; the divisors and last numbers are ANSWER green so the collected primes stand out.
3. **Circle trees of the book (P03-factor_tree-1, -2, P04-factor_tree-1) are not drawn.** The LP does not use trees for 105 and 30 (it teaches the division ladder; concept image C26.IMG1 is a ladder for 105) and no LP question works on them. They are mapped `none:TEXT_SUFFICIENT`, which is the nearest code, with the reason in the `note` field of each entry. **Decision for the user:** the tree for 30 has no picture anywhere in the LP; add a teaching image if the content team wants the book's tree procedure shown.
4. **P01-shape-1 (the room sketch, 12 ft x 16 ft) mapped to concept image M1.S1.T1.C1.IMG1** (accounting only). That teaching image is the same scenario (it also shows one tile with a "?"). No question of the tile problem needs the sketch: the question text gives 12 ft by 16 ft (C6, C8, C10 questions: none).
5. **C9 solution (how many 4 ft tiles): optional, not added.** A 16 ft by 12 ft room tiled 4 by 3 would help and the book suggests drawing such a rough diagram, but 12 ÷ 4 = 3, 16 ÷ 4 = 4, 3 × 4 = 12 is complete in text and concept image M1.S2.T2.C4.IMG1 already shows it.
6. **C37 solution (factors of 225): none, borderline.** The book's 225 ladder (P05-division_method-1, 5|225, 5|45, 3|9, 3|3, last 1) only produces "225 = 5 × 5 × 3 × 3", which the LP steps state in text; the question says "using its prime factorisation", not "division method" (unlike C28). Could be optional if the user wants the ladder shown; kept none, reason in the `note` of P05.
7. **C20 solution (Jump Jackpot, four pairs): none, borderline.** A number line of jumps would be nice; the answers are factor lists and one number each, and concept images M1.S6.T6.C16 to C18 already show jumps. The old pipeline had two cards (C20.IMG1/IMG2); not carried over.
8. **Examples 1 and 2 (C45, C47): solution required; Example 3 (C49): none.** Examples 1 and 2 are answered in the book by a ringed-subparts picture (P06, P07): which factors match is carried only by the rings (HIGHLIGHT_MEANING). Example 3 has no common subpart, nothing to ring and the book draws no figure for it; the reason says so (sibling rule). Question sides of all three: none (only the two numbers are given; the book's picture is the working).
9. **FiO 3.1 (second box), C51: solution none.** The book prints no answer figure for (a) to (e); a ringed-subpart picture per part (five diagrams) is not needed to check a list. This differs from Examples 1 and 2 only because their pictures are printed in the book.
10. **Added labels in the Example 1/2 figures** (not printed in the book, all taken from the LP solution): row labels "45 =" / "75 =" (and "112 =" / "84 ="), the values in the block labels ("3 × 5 = 15", "2 × 2 = 4", "2 × 7 = 14", "2 × 2 × 7 = 28") and a last line "HCF = 15" / "HCF = 28". Colours: factors INK, rings FOCUS (the book uses red digits in circles), labels ANSWER. Example 2 has five blocks, so the 16:9 card is scaled to the full height.
11. **All 14 question sides are none**: the book gives no figure for any of these questions (every figure in section 3.1 is a teaching or worked picture); data are in the words. Concept images are never linked.
12. Ids: C26 keeps IMG1 (teaching image), so the worked diagram is IMG2; the other three are IMG1 (old pair cards with ids IMG1/IMG2 are replaced; kept_image_ids was empty).

## 2. Things in the LP that look off

- **C19/C20 (Jump Jackpot Q1, two blocks sharing one card):** the question texts do not carry the book's part letters, but the answers do ("(a): 2; (b): 1" and "(c): 10; (d): 14"). A reader sees (a) to (d) in the answer without them in the question. Suggest writing "(a) 14 and 30 (b) 7 and 11" and "(c) 30 and 50 (d) 28 and 42" in the questions.
- **book_number "Figure it Out 3.1, Q1"** is used for M1.S13.T13 (page 5, list the factors), for M1.S16.T16 (page 7, common factors and HCF) and presumably again for page 8 (chunk B): three different Figure it Out boxes carry the same label. Not wrong, but ambiguous.
- **C23 worked example** ("Which of 1, 2, 9, 13, 21 and 29 are prime?") is not in the book (page 3 only recalls the definition); LP-authored, arithmetic correct.
- **C34 question** turns the book's "2 × 7", "2 × 2 × 2", "3 × 3 × 3" into 14, 8 and 27: fine, answer correct (14 and 8 are factors, 27 is not).
- **C10/C11** reword the book's "Try This" (would the answer change?) as "could a tile larger than 4 ft fit?"; the LP argument (counts 3 and 4, tile side 4 ÷ k) is correct.
- I recomputed every LP solution of this chunk (factor lists, common factors, HCFs, 84/108 bags, 1200 divisions, 360 has 24 and 840 has 32 factors, 96 = 2^5 × 3, 121 = 11 × 11): all correct, none contradicts the book.

## 3. Where the book is unclear

- The book has no printed-solutions section; its worked pictures (P06, P07, P04 ladders) are the only "answers" in pictures.
- Colour of the rings in P06/P07: they print as red digits inside rings; the base inventory said "black circle". Immaterial: our figure uses the FOCUS token for rings.
- Ladder geometry (P04, P05): rows step to the right because the numbers are right-aligned and each bar sits against its own number; the last number sits centred under the number above. The spec uses this reading for 105/30 and for 1200.
- P01: right-angle marks are drawn in three corners only (top-left, top-right, bottom-left); not needed by any item of this chunk.

### Chunk B notes (from the decision agent)
# Notes, chunk B (Class 7 Ch 11 "Finding Common Ground", plan cbse_eng_maths7_ch11_v30)

Result: 15 units, 28 items. Required 2 (both solutions) / optional 0 / none 26. Validator: errors 0, warnings 0.
Output: `map/out_B.json`. Figures claimed: P08-factorisation_match-1, P08-factorisation_match-2 (items), P09-illustration-1 (none:DECORATIVE_ONLY).

## 1. Judgement calls

1. **Example 4 and Example 5 solutions are REQUIRED (M1.S18.T18.C57.IMG1, M1.S18.T18.C59.IMG1).** This is the one real call in the chunk.
   - The book (p.8) prints each worked answer as a picture: the two factorisations aligned one under the other, the minimum-count common subparts boxed, then the HCF line. B2 says a printed answer that is a picture makes the solution required, and the boxes carry the meaning (which 2 and which 3, or which 3 and which two 5s, are shared).
   - The earlier author's `s_figure` hint describes the same picture for both.
   - Against it: a plain factorisation and a minimum-count step could also be written in LaTeX. If the user wants these two dropped to `none`, change them to `drop_image` with `LATEX_ARITHMETIC`; nothing else in the chunk depends on them.
   - Question side of both is `none`: the question gives only the two numbers, and the book's picture is the answer, so a question figure would leak it. `derived_from` is therefore null.
   - Spec details: the book's red/green digits and blue boxes are replaced by house tokens (digits INK, boxes FOCUS, result line ANSWER). The result line "HCF = 2 × 3 = 6" / "HCF = 3 × 5 × 5 = 75" is kept because the book prints it in the picture and the LP solution's last step uses the same words. Example 4 uses a connected step-shaped outline for the two 3s (row 1 factor 2, row 2 factor 4), as in the book. Example 5 uses a shared five-column grid so the three tall boxes (columns 2, 3, 4) line up.
2. **Why Examples 6 and 7 (LCM) and the Figure it Out answers are `none`, although Examples 4 and 5 are required.** The book prints no picture for them. The sibling rule is about the same kind of answer in the same question set; the reason is stated in each item. The Venn and stacks pictures for Examples 6 and 7 exist only as teaching images and are never linked.
3. **M1.S17.T17.C54 (worked example, HCF of 36, 60 and 84): `none`.** The book has no figure here (p.8 says only that a similar method can be followed), and this example is the plan's own. A three-row aligned figure with the minimum counts boxed would only make it nicer, so it is not marked optional either. Teaching image C55 shows it as three panels.
4. **Toran, gajak and idli-vada solutions: `none` (LATEX_ARITHMETIC).** Each is two plain lists of multiples and their first shared value. Two aligned rulers would only make them nicer, the book prints no such picture, and the three items get the same decision. The toran `s_figure` hint (two rows of strips meeting at 24 and 48) is therefore not followed; teaching image C64 covers it.
5. **P09-illustration-1** (boys laying cloth strips): the base entry was unsure whether it carries data. I checked the page picture: no lengths, counts or labels, and the 6 cm and 8 cm are in the question text. Decoration. The question side of the toran question is `none` with DECORATIVE_ONLY.
6. **M3.S27.T27.C88 (worked example, HCFs of consecutive numbers): `none`.** The book prints no figure (Figure it Out 3.3 Q1, Math Talk). The number line with arcs is already teaching image C88.IMG1 (kept, never linked).
7. **M3.S28 patterns:** Q1 is open-ended (find pairs, describe them in words), Q2 is algebra in symbols. Neither needs a picture. The book's picture on p.12 (the talking numbers 18 and 6) is decoration and gives no data.

## 2. Things in the LP that look off (none blocks a diagram)

- **M1.S18.T18.C56 (Example 4 question):** the LP question adds "using the minimum count of each common prime", which is not in the book ("Find the HCF of 30 and 72"). The book also states both factorisations before asking the example, while the LP question does not give them, so the factorisations appear only in the solution. Not a figure issue.
- **M2.S23.T23.C74 (gajak):** the LP says "free gajak every 7 days". The book says the shop gives gajak every Monday and today is a Monday, which is why the multiples of 7 appear. Same arithmetic, but the weekday context is lost.
- **M2.S23.T23.C76 / C77 (idli-vada):** the question text does not label the four pairs (a) to (d), but the answers do ("(a): 12; (b): 77" and "(c): 210; (d): 165"). A student cannot tell which letter is which pair.
- **M3.S27.T27.C88 (worked example):** it covers book Figure it Out 3.3 Q1 parts (a), (b), (d) and 12 and 13, but is written as a "find the HCF" example, not as the book's "make a general statement" question. Fine as a teaching example.
- **M3.S28.T28.C90:** "Find three more pairs" where the book says "Find more such number pairs". Harmless.
- All arithmetic in the chunk was re-checked: every factorisation multiplies back, and every HCF and LCM is right (Examples 4 to 7; Figure it Out 3.1 Q1 (a) to (e) = 12, 3, 6, 100, 100; Q2 HCF 72; Figure it Out 3.2 Q1 = 360, 108, 1365, 1110; gajak 70; idli-vada 12, 77, 210, 165; 3.3 pairs). No LP solution contradicts the book.

## 3. Where the book is unclear

- This pdf has no printed-solutions section, so no printed answer other than the Example 4 and Example 5 pictures was available; every other decision rests on the LP solution text.
- Pictures on the chapter pages in my chunk that carry no data and are not in the base inventory, not added: the gajak photograph (p.9, already noted by the inventory agent), and the talking-numbers art 18 and 6 (p.12). Both would be `none:DECORATIVE_ONLY` if the merge wants them listed.
- No picture on pp.10 to 13 carries mathematical content; I checked all four page images.

### Chunk C notes (from the decision agent)
# Chunk C notes (Class 7 Ch 11, section 3.3, units 1-18: M3.S29.T29, S31, S32, S33, S35, S36)

Result: 32 items = required 8 / optional 0 / none 24. Questions: 2 required (C113, C115), 12 none. Solutions: 5 required (C104, C106, C114, C116, C118), 9 none. Worked examples: 1 required (C110), 3 none (C133, C134, C135).
Validator: errors 0 (10 warnings: 9 are the short result equations such as "HCF = 2 x 5 = 10" in visible_text, which the validator counts as long strings because of the spaces; 1 is C118 solution, which has no book figure to map to, see 1.4).

Required diagrams (media ids):
- M3.S31.T31.C104.IMG1 (solution): 270/50 and 540/100 as two stacked factor blocks with the common subparts boxed, HCF 10 and HCF 20. One picture for the pair because a pair gets one solution diagram.
- M3.S31.T31.C106.IMG1 (solution): 14 x 6 / 14 x 9 factor rows with the common 2 x 7 braced as 14 and boxed, the last 3s boxed, HCF 42.
- M3.S32.T32.C110.IMG2 (worked example, add_new_image, block_index 0): the two ladders (300/150 and 630/770) with one L-shaped outline each for the LCM. IMG1 is the kept teaching image, so this is IMG2.
- M3.S33.T33.C113.IMG1 (question) and C114.IMG1 (solution, derived_from C113): the ladder for 84 and 180, plain; then the same ladder with the divisors 2, 2, 3 ringed and "HCF = 2 x 2 x 3 = 12".
- M3.S33.T33.C115.IMG1 (question) and C116.IMG1 (solution, derived_from C115): the two ladders, plain; then the same with the divisors ringed and the two HCF lines.
- M3.S33.T33.C118.IMG1 (solution): two ladders computed from the LP steps (90/150 by 10 then 3; 84/132 by 12), solid ring on the divisors (HCF), dashed ring on the last pair (LCM = divisors x last pair), four result lines.

## 1. Judgement calls

1. **C104 and C106 (doubling, 270/50 and 14 x 6): solution required, question none.** The LP turned two worked pictures of the book (p.60, page 14) into "find the HCF" questions. The book answers them with a picture: the factorisations with the matching subparts boxed (HIGHLIGHT_MEANING), including the 5 taken from different positions in the two rows and the extra boxed 2 after doubling. B2 rule 1 (printed answer is a picture) applies; it is the same kind of picture chunk A uses for Examples 1 and 2 of 3.1. The tie-breaker (a careful student could solve it from the text) would say none, so these two are the least certain "required". **If the user wants text only, flip C104 and C106 solutions to none (LATEX_ARITHMETIC).** Nothing else depends on them. The question sides are none: the questions give only numbers (a blank figure would imply something was given).
2. **C108 (four more pairs, 18 x 10 ...): solution none** although C104/C106 are required. The book prints no picture for these four pairs, and four factor figures would not fit the "one diagram per solution" rule; the LP answer is one line per pair. Reason says so (sibling note).
3. **C113/C114 and C115/C116 (use the ladder): question required, solution required.** The text never shows the ladder rows (42, 90; 21, 45; 150, 75 ...), so the question needs the picture (FIG_REFERENCED, DATA_IN_FIGURE). The ringed divisors are the answer to "how do we use the ladder"; the solution is derived_from the question and adds only the ring(s) and the result line(s). The LP hints (q_figure / s_figure) say the same.
4. **C118 (bigger common divisors, 90/150 and 84/132): solution required, question none, no book figure maps to it.** The book prints no picture for these two pairs ("you can try this method"). I required the solution because the method asked for is the ladder, the answer is a ladder (divisors, last pair, what is multiplied), and the LP steps only describe it in words (B2: answer is an arrangement/filled figure, even if the steps describe it in words); same kind of answer as C114/C116. The ladders are computed from the LP steps (90,150 / 10 = 9,15 / 3 = 3,5; 84,132 / 12 = 7,11), all co-prime at the end. One picture holds both pairs (the LP did not split the question into parts). **If the user wants only book-printed pictures, flip C118 to none (or optional).** Marking: a solid ring on the divisors gives the HCF, a dashed ring on the last pair added gives the LCM; the result lines repeat the LP's own equations.
5. **C115 question diagram has no ovals and no captions, though the book prints them in the question** (p.61, "Find the HCF in the following cases": blue ovals round the divisors and "HCF = 2 x 5 x 5 x 3"). The LP treats the ringed divisors as the solution (hint s_figure) and C113/C114 is built the same way, so the question diagram stays plain and the ovals plus the numeric results go to the solution. If the user prefers the book's version, put the ovals in the question diagram and make C116 SAME_AS_QUESTION_DIAGRAM or keep it with the results only.
6. **C110 worked example: diagram with the LCM outlines, and follows the LP, not the book, for 630/770.** The book (p.61, page 15) divides once more by 3 (rows 3 | 9, 11 and last pair 3, 11; LCM = 2 x 5 x 7 x 3 x 3 x 11). The LP worked example stops at 9, 11 (LCM = 2 x 5 x 7 x 9 x 11 = 6930, same value). The diagram stops at 9, 11 with the L round 2, 5, 7 and 9, 11, so that the picture matches the steps. The outlines are drawn because the book prints them in the figure and the block is a worked example (steps follow at once); the LCM captions are not drawn. The kept teaching image C110.IMG1 shows only 630/770 and is never linked.
7. **Mapping of the repeated book figures.** A figure used by two items is two entries: P14-division_method-1 -> C113 question and NEW-P14-division_method-1-sol -> C114 solution; P15-division_method-1 and -2 -> C115 question and NEW-P15-division_method-1-sol and NEW-P15-division_method-2-sol -> C116 solution. P14-factorisation_match-1 and -2 are two figures of one picture (both map to C104 solution).
8. **P15-division_method-5 (Guna's 50, 3 ladder) -> concept image C111.IMG1** (literally the same ladder). **P16-division_method-1 (Anshu's 10, 7 ladder) -> none:TEXT_SUFFICIENT**: it illustrates the teaching narration of C111 (all numbers and results are in the text), no item of this chunk uses it, and C111.IMG1 already teaches the bigger-divisor idea. No concept image shows it exactly; if the content team wants it, it is a teaching image to add, not a question figure.
9. **FiO 3.3 Q1-Q3 (C94-C99): all none.** All data are words and numbers; the answers are statements with example pairs (LaTeX/text). Questions carry OPEN_ENDED as well (general statements).
10. **S35 (HCF x LCM = product), C123-C132: all none.** Arithmetic, factorisations and short arguments; the book prints no figure on p.62-63 (the factorisation lines are printed text). C129/C130 (explain with 12 and 18) is borderline: a sharing-out picture would be natural, but the LP steps carry the prime-by-prime count in full and the teaching image C121.IMG1 already shows the same pair; kept none, not optional, because the figure would only repeat that teaching image. C127/C128 has a `text_alternative` (a LaTeX array of pair, HCF, LCM, product).
11. **S36 worked examples C133, C134, C135: none.** Bells, ribbons and prime-factorisation reading: all data in the words; they are not in the book. The kept teaching images (C133.IMG1 split/meet, C135.IMG1 Venn) are never linked.
12. **Colours.** Given content INK, ladder rules GUIDE, rings/boxes/outlines FOCUS, added numbers and result lines ANSWER green. In the factor figures (C104, C106) the factors are INK and the matched digits ANSWER inside FOCUS boxes (the book prints red/green digits in blue boxes). Ladder geometry: rows step right as in the book; all coordinates are on a 1920 x 1080 canvas and the diagrams are 16:9 (a single ladder in 16:9 leaves white space; the pipeline draws 16:9 cards).
13. **Ids.** C110 keeps IMG1 as teaching image, so the worked diagram is IMG2; all others are IMG1 (kept_image_ids of the pairs were empty; the old pair cards C113.IMG1, C114.IMG1 ... are replaced by the same ids).

## 2. Things in the LP that look off

- **Most items of this chunk are LP-authored restatements of teaching narration, not NCERT Figure it Out questions** (S31, S33, S35 pairs: "Doubling: HCF of 270 and 50 and their doubles", "Common Division: bigger divisors for two pairs" ...; S36 worked examples have ncert_refs []). Only FiO 3.3 Q1-Q3 (S29) are printed questions. The book_number strings are descriptive labels, not book numbers.
- **C110 vs the book for 630/770:** the worked example says last row 9, 11 and LCM 2 x 5 x 7 x 9 x 11; the LP's own textbook_text for the same concept says "LCM = 2 x 5 x 7 x 3 x 3 x 11" (the book's version). Both equal 6930, but the two statements sit in one concept. Not wrong, only two ladders.
- **C113 and C115 question texts say "use the ladder(s)" without any ladder in the text**, so the question is not self-contained without the figure (the LP hints q_figure describe it). Fine now that the diagram is required; the placeholder goes after the question text.
- **C118 answer_tex** writes "(a): HCF = 30, LCM = 450; (b): HCF = 12, LCM = 924" but the question (C117) does not carry the letters (a) and (b) (the book has "(a) 90 and 150 (b) 84 and 132"). Suggest "(a) 90 and 150, (b) 84 and 132" in the question text. The diagram is drawn left = (a), right = (b) without letters.
- I recomputed every LP solution of this chunk (HCF/LCM of all pairs in C95-C99, 270/50/540/100, 14 x 6/14 x 9, the four multiples pairs in C108 (90, 10, 5, 48), every ladder row of C110/C114/C116/C118, 6/8 and 7/9, 105 and 95 (1995, 9975), the three pairs of C128 (15/315/4725, 11/8800/96800, 74/1110/82140), 12 and 18 (6, 36, 216), 4/6/10 (2, 60, 120 against 240), the bells (36), the ribbons (12 m, 5 pieces) and 1260): all correct, none contradicts the book.

## 3. Where the book is unclear

- The book has no printed-solutions section; its worked pictures are the only "answers" in pictures.
- p.60 (page 14), figure for 270/50: the connector joining the two boxed 5s is one L-shaped outline round both 5s (the 5 of 270 is at column 9, the 5 of 50 at column 5, so they are not in the same column). The spec draws two boxes and an elbow line through the gap between the rows; same reading for 540/100 (columns 11 and 7).
- p.61 (page 15), LCM loops: the hand-drawn loop passes through the "6, 3" row. The spec draws a clean L below the rule of the last divisor row so that no digit is cut.
- p.61, LCM ladder for 630/770: one more division by 3 than the LP (see 1.6).
- Ring colours: the book prints blue ovals and red/green digits; the spec uses the style tokens (FOCUS, ANSWER).
- Page-number rings on every page are the Mystery Colours scheme (decoration here, belongs to P20 of chunk D if anyone maps it).

### Chunk D notes (from the decision agent)
# Chunk D notes (Class 7 Ch 11, cbse_eng_maths7_ch11_v30)

Units 52 to 69 = topics T37 (Figure it Out Q1-Q7), T38 (3 worked examples), T39 (Figure it Out Q8-Q13), T40 (2 worked examples of the review).
31 items: required 2, optional 0, none 29. Validator: errors 0, warnings 0.

## 1. Judgement calls

- **T37 Q1 (stars), question: required.** The book prints two rows of 12 stars (checked on page 17: row 1 yellow, green, orange, blue, pink, grey twice; row 2 green, orange, yellow, blue three times; ellipsis after each). The LP question says "the two rows below ... as shown" and only spells the colours out in a bracket, so without the picture "below" points at nothing. Tie-breaker kept it required (FIG_REFERENCED, DATA_IN_FIGURE). The bracket text in the LP stays; it just repeats the picture.
- **T37 Q1, solution: required, derived_from the question diagram.** The question picture stops at 12 stars; the answer is the 16th star. The solution figure is the whole final state: both rows to column 16, columns numbered 1 to 16 (ANSWER), FOCUS boxes round columns 4 and 16 (both rows blue). Columns 1 to 12 keep the same x, y and colours as the question figure, so the question card is left-aligned with empty space on the right. I did not mark the other blue stars (row 1 col 10; row 2 cols 8, 12): the colour already shows them and the boxes would lose their point.
- **Star colours are not style tokens.** The six star colours (yellow, green, orange, blue, pink, grey) are data in the book picture, so the spec gives hex values (yellow #F4D41F, green #7BBF3A, orange #E8801E, blue #3C6DC5, pink #C768AE, grey #8C8C8C) and a 3 px INK outline (the book stars have no outline).
- **Second inventory entry `NEW-P17-pattern-1-sol`.** The solution reuses the same book picture, so by the brief's rule it is a second entry (a figure used by two items). It is not a figure printed in the book; it exists only for accounting.
- **P20-number_grid-1 (Mystery Colours, 10 x 10 ring badges) claimed by D.** It is a teaching figure of M4.S41.T41 (Puzzle Time), and T41/T42 are in none of the chunks A to D (no question items), so the merged base-inventory check would otherwise fail. Mapped `concept_image:M4.S41.T41.C171.IMG1` (Decode and draw a ring). Honest caveat: C170/C171 are small excerpts of the ring scheme, not the full 100-badge grid. If another chunk also claims it, the two entries should be reconciled at merge (either meaning, concept image, is fine).
- **T37 Q6 (box 12 x 18 x 36 and cubes): none on both sides.** The book gives no picture of the box. A cuboid sketch would be a nicety, but the question side may not invent a figure and a student solves it by divisibility. Not marked optional because the book supplies nothing to base it on.
- **T38 worked examples (C151, C152, C153) and T40 (C167, C168): none.** No figure is referred to; steps are arithmetic. C151, C153, C167, C168 already have a teaching image which stays and is never linked (v3). The cat and mouse example (C152) and the dog and rabbit question (T39 Q4, C161/C162) get the same decision (sibling consistency): story + arithmetic, no picture.
- **T39 Q8 solution: none** but with a `text_alternative`: a plain LaTeX array of multiples 420 ... 2100 against remainders 2, 4, 6, 8, 10 (LATEX_TABLE, not an image).
- **Q3, Q4, Q12, Q13 solutions (answers are factorisations, pairs, numbers, a sum): none.** The matched-subpart pictures of section 3.1 are teaching/worked-example figures owned by other chunks; the Figure it Out answers here are not pictures.

## 2. Things in the LP that look wrong

- **Book numbers in T39.** T39's concepts are labelled "Figure it Out 3.3, Q1" to "Q6" (same labels as T37's Q1 to Q6), but the book questions are Q8 to Q13 (ncert_refs end8 to end13 are correct). Two sets of Q1 to Q6 in one topic family may confuse learners and the diagram build; the map uses the LP string in `lp_book_number` and the right book number in `ncert_ref`.
- **T37 Q1 question text.** It contains the colour lists in brackets, which now duplicate the diagram (harmless; the diagram adds the rows, the bracket stays as a text alternative).
- **Worked-example blocks (C151, C152, C153, C167, C168) carry plain text only** (`question`, `steps`, `answer` with "7 - 5", "1/6", "x"), no `*_tex` fields. Not a diagram matter; whoever syncs LP text may want LaTeX there.
- Recomputed and found correct in the LP solutions: Q1 (blue at 4, 10, 16 and 4, 8, 12, 16; LCM(6,4) = 12 so 16), Q3 (HCF 21, LCM 97020; HCF 9, LCM 180), Q4 (66 = 2 x 3 x 11 pairs), Q5 (105 < 200 < 210), Q6 (HCF 6, cubes 6, 3, 2), Q7 (HCF 18), Q8 (2100; remainders 2, 4, 6, 8, 10), Q9 (72 and 36), Q10 (LCM = m x n so only c), Q11 (75 leaps, 675 = 675), Q12 (360), Q13 (LCM 1260; 672 + 63 + 245 + 220 + 60 = 1260), and the five worked examples (60; 24 leaps, 168 = 168; 5/12; 14 and 210, 2940; 1 and 120, 7 and 21, 1 and 156).

## 3. Where the book is unclear

- Figure it Out Q1: the book shows only 12 stars per row with "..."; the next meeting (16th star) lies beyond what is printed, so the solution figure extends the pattern by the stated cycle (6 and 4), as the LP solution does.
- Q9 ("Fire in the Mountain") relies on game rules that this chapter does not explain; the LP solution treats "nobody got out" as "number divisible by the called number". No figure is printed.
- This pdf has no printed-solutions section; every solution follows the LP text.
