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
