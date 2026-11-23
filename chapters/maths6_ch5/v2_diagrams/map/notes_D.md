# Chunk D notes (Class 6 Ch 5 "Prime Time", topics T16 to T20, units 45-64)

Result: 31 items = 9 worked + 11 question + 11 solution. Required 2 (both worked examples), optional 0, none 29. Validator `--chunk D`: errors 0, warnings 0.

Figures in this part of the book: only two. I checked every page picture used (pdf pages 11-16 and the printed answers on pdf pages 29-30). Pages 11, 14, 15, 16 and the answer pages hold text only; the page 11 characters are not in the picture. The two base figures are right (counts and texts checked against the pictures), so nothing is marked "CORRECTED" and nothing is `NEW-`.

## 1. Judgement calls

1. **M3.S16.T16.C95 (36 broken four ways): required, factor tree (P12-factor_tree-1).** This is the closest call. The text alone is enough to compute 2 x 2 x 3 x 3 = 36, so a "text only" reading is possible (tie-breaker). I chose required because the question says "in all four cases" and "multiply back ... in all four cases", while the LP text names only the four first splits (2x18, 3x12, 4x9, 6x6). The four finished chains (3x3x2x2, 2x3x2x3 and so on) exist only in the book's tree. If the user wants fewer images, this is the one to drop (then `none` with TEXT_SUFFICIENT and the text must list the four chains). The figure is the whole printed tree, question side (worked example), nothing solved. No teaching image shows it.
2. **M3.S16.T16.C96 (cuboid, "Using this diagram"): required, solid_3d (P13-solid-1).** Clear case: the question points at the figure. The book colours the faces red, yellow and green; the colours carry no meaning, so I used tokens: front CELL_FILL, top MARK_FILL, right SET_B at 30 percent opacity (the renderer must support the opacity; if not, use a light amber tint). No labels are drawn (the book prints none); 3, 2 and 5 are said in the LP solution steps. 16:9 card with the cuboid centred; coordinates are given for a 1920 x 1080 canvas.
3. **Teaching images kept, nothing linked:** C94.IMG1 (same primes), C97.IMG1 (join the prime factors), C113.IMG1 (80 and 63 dots), C114.IMG1 (48 includes 12). The matching worked examples are `none` (the book has no picture for them; the text and LaTeX carry everything). Not coded REUSES_CONCEPT_IMAGE because that code is for the 'refer picture' case only.
4. **Figure it Out 5.4 Q1-Q5 (T18), all ten items `none`.** Questions are words or lists of numbers; printed answers (page 29-30) are product lines in text, not pictures. Sibling consistency: all five pairs get the same decision. A factor tree for Q4 (a, b, c) or Q1 would be a nice extra but is not needed (optional at most; not added).
5. **Example 2-6 pairs (T20, 10 items) `none`.** Both prime factorisations are given in the question; the answers are comparisons of prime lists in words. An "included / not included" picture (for 42 and 12, 75 and 21) would help a little but the text states it exactly (optional at most; not added).
6. **T17 Anshu dialogue (C101/C102) `none`.** A dialogue question with the factorisations in the text.

## 2. Things in the LP that look wrong

- **C101 question_tex / text (and C102, C116-C125 text):** the LaTeX is broken around "co-prime": `Are $56$ and $63 co$-prime?` puts "co" inside the maths of 63, and `$co$-prime` elsewhere sets "co" in maths italics. Plain text "co-prime" outside the dollar signs would be right.
- **C109 (Figure it Out Q4) and C111 (Q5):** question, question_tex and text list the parts twice (`(a): 56 x 25; (b): 108 x 75; (c): 1000 x 81; (a): ...; (b): ...; (c): ...`, and for Q5 `(a) three different prime numbers? (b) four different prime numbers? (a) three ... (b) four ...`). The same duplicate sits in the answer concepts' `question`. It looks like a scrape that took the part list from two places. The parts should appear once.
- **C104 (Q1 answer):** `answer_tex` writes 729 as `(six $3s$)` and 1024 as `$1024 =$ ten $2s$ multiplied` while `steps_tex` writes both products out in full. The numbers are right (729 = 3^6, 1024 = 2^10) but the style is not consistent; `$3s$` and `$2s$` put the plural s inside maths. Same `$3s$` in C105 question_tex ("two $3s$").
- **C96, C99, C113, C114:** `steps` and `answer` hold the same paragraph (steps has a single entry equal to the answer), so the solution text is shown twice for these worked examples.
- **C96 text** (cuboid): the question depends on the figure ("Using this diagram"), so the token placed after the question text is essential; without it the question has no figure.
- All arithmetic in the LP was recomputed and is correct: 80, 63, 36 = 2x2x3x3, 72 = 2x2x2x3x3 (8 x 9), 64 = 2^6, 104 = 2^3 x 13, 105, 243 = 3^5, 320 = 2^6 x 5, 141 = 3 x 47, 1728 = 2^6 x 3^3, 729 = 3^6, 1024 = 2^10, 1331 = 11^3, 1000, 198, 1955 = 5 x 17 x 23, 56x25, 108x75, 1000x81, 30, 210, 168 = 12 x 14, 75 vs 21 (7), 42 vs 12 (2 twice vs once).
- Outside my chunk (for the merger): printed answer page 30, Q.1 (second Figure it Out set) labels the fourth part "c. Yes" instead of "d. Yes"; and printed answer Q.2 a-d are fractions. That set is T21 (chunk E).

## 3. Places where the book itself is unclear

- The book's tree on p.118 has two identical last boxes in column 4 (2x3x2x3 twice, the last box adds nothing). I kept both, as printed, and said so in `render_note`.
- The cuboid has no printed dimensions; the numbers 3, 2, 5 come from counting the squares on the three faces (checked on an enlarged crop: front 3x2, top 3x5, right 5x2) and from the LP solution text, which agrees.
