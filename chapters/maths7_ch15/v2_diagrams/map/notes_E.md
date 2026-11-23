# Chunk E notes (Class 7 Ch 15, topics M3.S24.T24, M4.S25.T25, M4.S26.T26, M4.S27.T27, M4.S28.T28)

Result: 35 items (21 units): required 1 / optional 0 / none 34. Validator `--chunk E`: errors 0, warnings 0.
The one required diagram is the ancient Indian notation table of the worked example `M4.S25.T25.C158` (`M4.S25.T25.C158.IMG1`).
Everything else in this chunk is equation chains, word problems and algebra: text and LaTeX.

## Borderline

1. **M4.S25.T25.C158 worked example (ancient Indian notation), REQUIRED.** The LP steps and answer carry every word of the notation
   ("yā 2 rū 8 with a dot over the 8", "yā 3 rū 4 above yā 2 rū 8"), so a strict "text carries all" reading gives `none`. I chose `required`
   (ANSWER_IS_FIGURE + HIGHLIGHT_MEANING) because the answer IS the notation table (a filled table), a dot over a digit is a mark that
   carries meaning (a negative number) and cannot be shown reliably in plain text, and "the two sides one below the other" is a layout.
   No concept image shows this table (`concept_images.json` has nothing for M4.S25), and teaching images are never linked anyway.
   Spec: 4 x 2 table, header "Modern" / "Ancient Indian" (the book's column labels, shortened), three body rows, one drawn dot over the 8
   of body row 2 only, the lower 8 of body row 3 has no dot; the book's three bracketed notes are left out (the steps carry that wording).
2. **Q11 (a) (C156 / C157), `none`.** In the book, part (a) has red slashes through the 6 of 6x and of 66 and an "11" above 66. That only
   shows how line 2 ("x + 9 = 11") arises, and line 2 is in the LP text; the LP solution also says "6x and 66 were divided by 6, but 9 was not".
   A careful student loses nothing, so `none` (LATEX_ARITHMETIC). Same decision for (b) and (c) (sibling rule). If the team wants the slashes
   kept, this is the one question to flip.
3. **Mend the Mistake boxes 1 to 9 (C138 to C155), question side `none`.** The printed boxes are in the book's inventory as "worked_steps
   given in question". They are chains of equations (LATEX_ARITHMETIC, explicitly a Step C case); the peach fill and the number badge carry no
   meaning and every line is already in the LP text. Solution side `none` too: the answer is the named mistake plus corrected equations, and the
   book has no printed answer picture. All nine boxes and Q11 (a)(b)(c) get the same decision.
4. **Summary block 4, the magic trick (C170, block 4), `none`.** A flow strip of the operations (x, then x2, +10, /2, -x, +3, giving 8) would only make it nicer (the book has
   no such figure; the only picture on p.27 is a group of children, decoration), so I did not even mark it `optional`.
5. **Cut-out sheets (P28 tangram, P30 / P32 / P34 dot paper), `none:OPEN_ENDED`.** No question, example or LP item refers to them. I claimed them
   here because they sit after the Summary (the last book section of my chunk) and no other chunk has an end section. Another chunk could claim the
   same figures with `DECORATIVE_ONLY`; any `none:` code means the same thing (no diagram, no link). The four blank cut pages (29, 31, 33, 35) carry only the
   scissors line and are not in the base inventory.
6. **P18 / P19 boxes claimed here.** Chunk D owns the teaching topic M3.S23.T23 (same book section 7.3) and may claim these nine figures too; I mapped
   them all `none:LATEX_ARITHMETIC`, which is the natural code, so a duplicate should compare equal.

## LP text issues

(No LP text was edited; suggestions only.)

- **C138, C140, C142, C144, C146, C148, C150, C152, C154 (boxes 1 to 9) and C156 (Q11 a, b, c): the steps are packed on one line.** The question_tex
  joins the printed lines with semicolons ("Box 1: 4x + 6 = 10; 4x = 10 + 6; 4x = 16; x = 4. ..."), but the solutions say "line 2", "line 3",
  "the last line", "line 5", which is hard to find in a run-on sentence. Suggested form (box 1):
  `Box $1$ (each line is one step):` followed by
  `\begin{array}{l} 4x + 6 = 10 \\ 4x = 10 + 6 \\ 4x = 16 \\ x = 4 \end{array}`, one array per box, and for Q11 one array per part (a), (b), (c).
  This is also why no picture is needed: a one-step-per-line array reproduces the book's box.
- **C143 (box 3 solution), wording.** "Mistake in line 2: the factor 2 was taken away by subtracting 2, and only from one term." The student's line 2 is
  `v - 4 = 6 - 2` (2v became v, and 2 was subtracted from the right side only). Suggested sentence: "Mistake in line 2: the 2 in 2v multiplies v, so it cannot
  be removed by subtracting 2 from the right side; either divide the whole of both sides by 2, or move -4 first."
- **C158 (ancient notation) steps, step 3 and 4.** The dot is only described in words. Suggested for step 4: "... written as yā 3 rū 4 with yā 2 rū 8 below it
  (this 8 is positive, so it has no dot): the two sides one below the other." (With the new diagram this is also visible.) If the team prefers text only,
  `yā\ 2\ r\bar{u}\ \dot{8}` in LaTeX does give a dot over the 8.
- **C160 step 4.** "the same as in Jahnavi and Sunita's savings" refers to Example 9 (m = 7, p.13-14); correct, but the learner may not remember it. Optional
  suggestion: "... m = 7, the same answer as Example 9 (Jahnavi and Sunita's savings)."
- **C170 blocks 0 to 3** are authored examples with no book number (`lp_book_number` null). Nothing wrong; noted because the items have no book reference.

Checked and found correct (recomputed): boxes 1 to 9 solutions (x = 1, z = 1/4, v = 5, z = -3, w = 26/11, x = -13/3, q = 21/8, x = 5/2, y = -3/16, each with the
LP check), Q11 (a) x = 19/2, (b) no mistake y = 6/7, (c) x = -13/5 with check -77/5 on both sides, Example 16 (100, both sides 900), Q1 of the Pinch of History
(2 and 10, checks 14 and 24), 2x + 3 = 4x + 5 (x = -1), Bakhshali (a = 4, 4 + 8 + 24 + 96 = 132), Summary examples (12, 4, 6, 12) and the magic trick (always 8, own trick always 4).

## Book unclear or misprinted

- **Box 8, line 2 (p.19):** the book prints `-6v - 8x = 14`, a stray letter v. The mathematics (and the LP) read `-6 - 8x = 14`. No diagram is drawn from it, so
  nothing is corrected in a picture; the base inventory records what the book prints and my figure entry says so.
- **Example 16 (p.20), line 2 of the solution:** the book prints `300 + 6x + (100) = 10x`. It should read `300 + 6x + 100 = 10x` (add 100 to both sides). The LP
  text ("Add 100 to both sides") is right.
- **Q11 (a) (p.24):** the red slash marks sit on the 6 of 6x and on the second 6 of 66 with "11" above; it is a hand-marked annotation, not a printed step, so
  I did not use it (see Borderline 2).
- **Pages 29, 31, 33, 35** are blank cut sheets (only the scissors line), and pages 30, 32, 34 are identical dot paper; the base inventory lists p.30, 32, 34 and
  the tangram p.28, and I claimed those four.
