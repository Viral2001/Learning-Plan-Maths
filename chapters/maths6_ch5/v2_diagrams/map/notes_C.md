# Chunk C notes: Class 6 Ch 5 "Prime Time" (topics M2.S12.T12, M2.S14.T14, M2.S15.T15)

Result: 14 units, 28 items. Required 2 (question side of FiO 5.2 LP Q1 and Q2), optional 2 (their solutions), none 24. Validator: errors 0, warnings 0.
Output: `map/out_C.json` (written by a script kept outside HERE).

## 1. Judgement calls

1. **FiO 5.2 LP Q1 (C60) and LP Q2 (C62): question diagram required (the finished Sieve table).**
   Q1 says "Look at the list of primes till 100", Q2 says "the table on the previous page". The list is only the book's p.113 table, so the learner cannot attempt either question without it (FIG_REFERENCED, DATA_IN_FIGURE, HIGHLIGHT_MEANING).
   - This is NOT the "refer picture" case of Step B2. The printed answer is plain text, and the plan has no concept image of the full table (`M2.S11.T11.C57.IMG1` shows only 1 to 10 in a row). So the question is required, not optional.
   - Each item gets its own diagram with the identical spec (C62 says "same as M2.S12.T12.C60.IMG1" in `render_note`).
   - The figure is exactly what the book prints: 10 x 10 cells, 25 primes circled (FOCUS), the other 75 cells (1 and the 74 composites) crossed with a full X (GUIDE, behind the INK number). It states no row counts and no differences. I checked the book table by pixel count: every prime cell has green and no red, every non-prime cell has red strokes.
   - Aspect ratio 16:9 although the grid is square: the pipeline draws 16:9 cards. The spec fixes the grid at about 940 px high on a 1920 x 1080 canvas, so each cell is about 94 px and the digits stay at least 34 px high. The book has no row labels (even though the question says "decades"), and none are drawn, as the companion note requires.

2. **Solutions of C60 / C62: `optional`, not `none`, not `required`.**
   The LP text already gives everything (the two pairs and differences; the ten row counts and the least / most decades), and the printed answers are text. A marked copy of the same table (pairs 2, 3 and 89, 97 for Q1; a count beside each row for Q2) would help, which is the tie-breaker's "nicer" band. So optional, and nothing is added.
   Sibling consistency: both are answers read off the same table, so both get the same decision.

3. **Other FiO 5.2 items (C64 to C76) all `none`.**
   - C64 (pairs with sum a multiple of 5), C66 (13/31 type pairs), C68 (seven consecutive composites), C70 (twin primes), C72 (product of three distinct primes), C74 (digits 2, 4, 5), C76 (doubling and adding 1): word or arithmetic questions with no figure in the book; the answers are lists or equations (TEXT_SUFFICIENT or LATEX_ARITHMETIC).
   - C69 solution (89 and 97 are primes, 90 to 96 are between them): a strip 89 to 97 would be a nicety only. No question figure exists to derive from, so I did not make it optional.

4. **Co-prime practice (C82 to C89) and Example 1 (C90, C91): all `none`.**
   - The book prints no figure with any of them, and no printed answer is a picture. The plan's concept images (4 and 9, 15 and 39, number line of 3 and 5) are teaching figures and are not linked (v3 rule).
   - C82 (where to put the treasures) and C88 (Math Talk on the first common multiple) are open-ended; reason codes include OPEN_ENDED.

5. **Figure inventory claims (6 entries).**
   - `P07-number_grid-1` goes to item C60 (question) and `NEW-P07-number_grid-1-b` to item C62 (question): a figure used by two items is two entries.
   - Merge note: chunk B (Sieve topic T11) may also claim `P07-number_grid-1`, as a teaching figure. If B gives it a different meaning (for example a concept image or none), keep one entry for the base id and rename mine to `NEW-` ids. My two items stay required either way, because they need their own figure.
   - `P10-thread_art-1` to `-4` (Math Talk "Co-prime art", p.10): no question, solution or worked-example item of the plan carries them. The plan covers this Math Talk with the tool "Thread Art Co-prime Check" (`M2.S13.T13.C81.2D1`). Topic T13 has no units, and its book section 5.3 has units only in my chunk, so I claimed them here as `none:OPEN_ENDED`. If another chunk claims them too, the meaning is the same.
   - I checked the four base descriptions against the page 10 picture (12 pegs gap 4 triangle; 13 pegs gap 3 ring; 16 pegs 8-point star on the even pegs; 24 pegs square on 24, 6, 12, 18): correct, no "CORRECTED:" needed.

## 2. Things in the LP that look wrong or thin

- **Book numbers:** T12 labels its questions "Figure it Out 5.2, Q1 to Q9". The book numbers are Q2, Q3, Q5, Q6, Q7, Q8, Q10, Q11, Q12 (book Q1, Q4, Q9 are in topic T10). Also the `ncert_refs` ("5.2.FiO.Q2" and so on) follow the book, so LP Q1 and the ref Q2 differ.
- **C62 text:** "in the table on the previous page" is a page reference from the book. In the LP the table will be the diagram right under the question, so it should read "in the table above" (not changed by me; the item is not marked for text sync).
- **C84 / C85 / C86 / C87 text:** the parts are listed twice. `question_tex` has "(a): 15 and 39, (b): 4 and 15, ...; (a): 15 and 39; (b): 4 and 15; ..." and the plain `question` has "a. 15 and 39, b. ... a) 15 and 39 b) ...". The same duplication is in the question line of the solution concepts. A reader sees every pair twice.
- **LaTeX misuse of the word co-prime:** `$co$-prime` in C86, C87, C88, C90, C91 (the word "co" set as math italics). In C90 it is worse: `$39 co$-prime` puts "co" inside the math with the number 39. In C87 `answer_tex` is "a, $b$ and $d$ are $co$-prime", which mixes plain "a" with math "b" and "d".
- **Broken LaTeX around pairs:** `answer_tex` of C65 is `$(2$, $3)$, $(3$, $7)$, $(2$, $13)$` and of C89 `$(3$, $5)$ ...`: the brackets are split across the math segments.
- **C61 / C67 / C71 / C77:** `steps_tex` repeats `answer_tex` word for word (one line only), so the "steps" add nothing.
- **C73 (three distinct primes):** the steps list the factorisations of 45, 60, 91 and 330 without saying why each is rejected, and never factorise 105 (only the answer line does). 60 = 2 x 2 x 3 x 5 has three different prime factors, so a learner may think it qualifies; the missing line is "2 is repeated, so 60 is not a product of exactly three distinct primes". Not a diagram matter.
- **C83 (where to place the treasures):** the book prints no answer for this prompt (its printed answer on p.28 is for "Check if these pairs are safe"). The LP's "e.g. 4 and 9" comes from the paragraph on p.115. Fine, but it is the LP's own answer.

## 3. Where the book itself is unclear

- The p.113 table prints some crosses as a single diagonal stroke (30, 49, 91, 94). That is a print artefact: every non-prime cell does carry red strokes. The spec draws a full X on every crossed cell.
- The question speaks of "decades" and "rows" but the book table has no row labels.
- Co-prime art (p.10): the peg count and gap of diagrams 3 and 4 are not printed (read from the picture as 16 pegs gap 6 and 24 pegs gap 6), and the exact chords of diagram 2 cannot all be traced. None of this affects an item of this chunk.
