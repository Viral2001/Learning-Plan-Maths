# Notes, chunk A (M1.S3.T3 and M1.S4.T4) - Class 7 Ch 6 "Number Play"

Result: 26 items = 13 questions + 13 solutions. Required 8 (1 question, 7 solutions), optional 2 (solutions), none 16. Validator: errors 0, 5 warnings
(the five Figure it Out Q1 (b)-(f) solutions are required but the book prints no picture for them, which is the expected case).

## 1. Judgement calls

1. **M1.S3.T3.C6 (question) = required, although the LP text already gives the heights (1, 5, 3, 6, 2, 7, 4).**
   Why: the book question is "the arrangement shown below" (a picture with empty bubbles) and the LP text says "the line in the figure", so the
   figure is the premise of the question; the 'refer picture' exception does not apply (the book's answer is a filled picture plus a list, not
   "refer picture"). The same picture is also the teaching image M1.S2.T2.C2.IMG2, which is never linked, so the item draws its own.
   A strict reading of the tie-breaker ("could the text alone do it?") would give `none`; I judged the dangling "in the figure" and the picture-first
   book question to outweigh that. If the team wants zero figures here, set it `none` and reword the text (drop "in the figure").
2. **M1.S3.T3.C7 (solution) = required** (printed answer is the same picture with the bubbles filled in: base figure P20), `derived_from` = the
   question diagram. Only the seven bubble digits (0, 0, 1, 0, 3, 0, 3) are new, in ANSWER green.
3. **Figure it Out Q1 (a)-(f), solutions = required, questions = none.** Only (a) has a printed answer picture (p.21); (b)-(f) get the same kind of
   figure by the sibling rule (answer IS an arrangement, B2). No question diagram: the book gives no figure with these questions (the stick-figure
   cut-outs are "at the end of the book", outside the 32 pages), so none is invented (companion note). Each solution figure therefore stands alone
   (`derived_from` null) and draws the whole line-up.
4. **What the figures show.** One scheme for all eight: seven plain stroke-figure children (no faces, single colour, simple glyphs), heights
   64 % to 100 % of the tallest in even 6 % steps (taken from the measured heights of the printed answer on p.21: 64, 70, 76, 82, 88, 94, 100 %),
   a speech bubble above each head, the height rank under each child with the one-word tag "height".
   - I ADDED the rank numerals + "height" so that the figure matches the LP text ("height 5", "Heights 7, 3, 5, 4, 1, 6, 2") and cannot be read as
     child numbers. The book picture itself has no rank numerals; in the unit-1 question they only repeat what the question text states.
   - Colours: unit 1 children and ranks in INK (given), bubble digits in ANSWER (new). Figure it Out Q1: children and rank numerals in ANSWER (the
     answer), bubble digits in INK (the sequence the question gives).
   - Left out on purpose: the book's colours, faces, the 11 ruled lines, the cut-out letters F C B G A D E (not in the LP), and the "Front" arrow
     of the teaching images (the front of the line is the left; the LP steps say "in front"). If the team wants the Front arrow, add one arrow
     labelled Front under the row in all eight specs.
5. **Q1(a) solution figure has bubbles, the book's printed picture has none.** The LP s_figure hint also says "with the speech bubbles above them reading
   0, 1, 1, 2, 4, 1, 5". The bubbles let the learner check each child, and they equal the given sequence (recomputed in code for all six parts).
6. **Figure it Out Q2 (a)-(f): all questions none; solutions (a), (b), (c), (f) none; (d) and (e) optional (not added).** The answers are verdicts
   ("Always / Only sometimes true") or a number, reached by word reasoning; no printed answer picture. (d) and (e) are the only ones whose steps
   give concrete counter-lines (heights 1, 2, 3, 4, 5 and 5, 4, 3, 2, 1; heights 7 .. 1 and 1, 7, 6), so a line-up would clearly help but is not needed
   (the verdict is not an arrangement, so ANSWER_IS_FIGURE does not apply). (a) is the same kind of answer but its counter-case ("the first child
   says 0 whatever the height") has no concrete line, hence `none`; this is the stated reason for the difference between (a) and (d)/(e).
7. **Inventory.** P01-arrangement-1 and P01-arrangement-2 (teaching line-ups opening 6.1) are claimed as `concept_image:M1.S2.T2.C2.IMG1` (both are
   its two panels). P02-arrangement-1 -> question item C6, P20 -> solution item C7, P21 -> solution item C9. No NEW- figure was needed. I checked all
   five against the page pictures (pages 1, 2, 20, 21): colours, order of heights, bubble numbers and the letters F C B G A D E are as the base describes.

## 2. Things in the LP that look wrong or thin

1. **Figure it Out Q1 (a)-(f) question text is only a bare sequence** ("(a): 0, 1, 1, 2, 4, 1, 5"). It never says what to do. The book says "Arrange
   the stick figure cutouts ... or draw a height arrangement such that the sequence reads". The text needs that sentence, at least on (a).
2. **Figure it Out Q2 (a)-(f) question text lacks the task** "Always True, Only Sometimes True, or Never True. Share your reasoning." The answers
   ("Only sometimes true") only make sense with it. Q2(f) is a question, so it is fine.
3. **Wrong wording in M1.S4.T4.C19 (Q1(f)) step 2:** "Each of the last four is shorter than the first three but taller than the others behind them."
   For heights 5, 6, 7, 1, 2, 3, 4 each of the last four is taller than the last-four children standing IN FRONT of it (not behind: those are taller).
   It should read "taller than the children of the last four who stand in front of it" or similar. The answer (heights 5, 6, 7, 1, 2, 3, 4) is correct.
4. **LP numbering differs from the book:** LP "Figure it Out, Q1 to Q6" are book Q1(a)-(f); LP "Q7 to Q12" are book Q2(a)-(f).
5. M1.S4.T4.C26 (Q2(d)) text is shortened ("cannot say 0") from the book's "if ... then they cannot say '0'"; harmless.
6. The old answer cards of C7 and C9 are two each (IMG1, IMG2); the new plan has one diagram per answer concept (IMG1), as the brief says the old cards
   are replaced.
7. Everything else recomputed with the rule "number of children in front (to the left) who are taller": the LP answers of unit 1 and Figure it Out
   Q1 (a)-(f), and the Q2 counter-lines, all agree with the figures I specified; no other contradiction with the book (p.20, p.21) found.

## 3. Where the book itself is unclear

1. Q1(a)'s printed answer (p.21) is a picture of cut-outs labelled F, C, B, G, A, D, E taken "from the cutouts at the back of the book"; those
   cut-outs are not in this 32-page pdf, so the letters cannot be tied to anything else. The picture has no bubbles or numbers.
2. "Try for other subparts": no picture is printed for (b)-(f).
3. The book's p.2 picture (question) is drawn with ranks 1, 5, 3, 6, 2, 7, 4, but its exact head heights were not measured separately; the specs use
   the even 6 % steps measured on p.21 (the order of heights is certain, the exact percentages are approximate, about plus or minus 3 %).
4. The book rule says "children in front"; the picture treats the left side as the front (the printed answer on p.20 reads "From left -> 0, 0, 1, 0, 3, 0, 3").
