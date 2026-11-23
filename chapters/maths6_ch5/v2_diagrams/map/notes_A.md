# Chunk A notes (Class 6 Ch 5 "Prime Time", plan cbse_eng_maths6_ch5_v75)

Result: 18 units, 32 items. Required 7 (questions C12, C20, C26, C30; solutions C13, C21, C27), optional 0, none 25. Validator: errors 0, one expected warning (C27, the printed book has no answer picture for it).

Figures claimed (8): P01 (none, decorative ring), P02 (C12 question), NEW-P02-venn_diagram-1-C26 (C26 question, second use of Fig. 5.1), P03 (concept image C32.IMG1), P04 (C30 question), P05 (C20 question), SOL23 (C13 solution), SOL25 (C21 solution). The other base figures of chapter pages 1-5 and solutions pages 23-25 are all in this list; P06 onward belong to other chunks.

## 1. Judgement calls

1. **Fig. 5.1 has 6 added (C12 and C26 question diagrams).** The printed figure leaves 6 out of the left circle (a print slip; the LP solution C13 says "6 belongs there"). The diagram includes it so that every multiple of 3 up to 30 is shown. The inventory entry starts with "CORRECTED:". If you want the figure exactly as printed, delete 6 from the spec (row 1 of the left region would then be 3, 9, 12 and the solution's row 1 stays 3, 6, 9, 12).
2. **Tidy rows instead of the book's scattered numbers.** The numbers of Fig. 5.1 are placed in rows (the printed answer, SOL23, uses rows too). The question figure fills only the upper rows, so that the solution figure (game till 60) adds its green numbers below without moving any given number (v3 rule: the solution is the question figure plus the answer). Circle outlines use SET_A / SET_B instead of the book's green.
3. **C26 question (Draw a figure similar to Fig. 5.1 for 2 and 5, 3 and 7, 4 and 6): required.** The question names Fig. 5.1 and the LP text does not describe it, so the learner needs it; it is the same book picture as C12, so the spec is identical ("same as M1.S3.T3.C12.IMG1"). The other choice would be `none`; I did not take it because "similar to Fig. 5.1" is meaningless without the picture.
4. **C27 solution: three Venn diagrams on ONE 16:9 card (82 numbers).** The answer is three figures, but a pair gets one solution diagram and the validator rejects a second item. Layout: panel A (2 and 5, 36 numbers) on the left half, B (3 and 7, 26 numbers) top right, C (4 and 6, 20 numbers) bottom right, no panel letters. Text is 34 to 36 px; every number box was checked in code to lie inside its region with an 8 px margin. It is dense: if the render looks cramped, the clean fix is three parts (IMG2, IMG3), which needs a change of the one-diagram rule. `derived_from` names C26.IMG1 only because the validator demands it; the circle style, colours, labels and arrow are the same, the layout is not (three panels). No printed answer exists for this task in the book, so no base figure maps here.
5. **C21 solution (Q8): sample answer 3 and 8 from the LP**, not the book's 3 and 4. With 3 and 4 the overlap would also hold 12, 36, 60, but the question's overlap shows only 72, 48, 24. Left-only = 21 multiples of 3 up to 72, right-only = 6 multiples of 8 up to 72 (8, 16, 32, 40, 56, 64). The book's arrows from each circle to its blank label are replaced by a label directly above its circle.
6. **C20 question (Q8): required**, because the blank labels and the overlap numbers 72, 48, 24 are only in the picture and the task is to fill the empty regions.
7. **C30 question (shaded and circled table): required** although the LP question text repeats the shaded and circled numbers in brackets. The book gives the table as a picture and asks to look at it; shading and circles carry the meaning (HIGHLIGHT_MEANING). **C31 solution: none** (SAME_AS_QUESTION_DIAGRAM): 36, 48, 60 are already the cells that are both shaded and circled in the question figure, and the answers are words. A copy with FOCUS outlines on those three cells would be only nicer, so not optional.
8. **Worked examples C32 and C33 (jump sizes): none.** The numbers are listed in the steps. P03 (book's jump-arc number line, six jump sizes) is a teaching figure: mapped to concept image M1.S5.T5.C32.IMG1, which draws only the jump of 4 on it. If the content team wants the full six-jump line it is a teaching-image job, not part of this run.
9. **Worked examples C2 and C3: none.** P01 (chapter-opening ring of children with bubbles) is mapped `none:DECORATIVE_ONLY`; the plan's C2 teaching image is a hops number line, a different figure.
10. **Text only (none, TEXT_SUFFICIENT or LATEX_ARITHMETIC):** Figure it Out Q1 to Q3 (C6 to C11), Q5 to Q7 (C14 to C19), Q9, Q10 (C22 to C25), the other-number-with-4 pair (C28/C29) and the 15-and-30 pair (C35/C36). Their book answers are words or numbers, no figure is printed.
11. **diagram_type `other`** for the Venn diagrams (not in the section 7 catalogue); the table uses `cell_grid`. Figure letters (a, b, c) and the caption "Fig. 5.1" are not drawn.

## 2. Things in the LP that look wrong

- **Duplicated sub-questions.** C8 and C9 (Q2) list "(a) ... (b) ... (c) ..." twice (long wording, then short wording). C26 and C27 (the three pairs) and C30 and C31 (the table) do the same: the question text is followed by a second copy of the parts ("a) 2 and 5 up to 60 ...", "1) Is there anything common ..."). C12, C20, C26 and C30 also carry a bracketed description of the figure; once the diagram is in place these descriptions are redundant (the C30 one even lists the shaded and circled numbers, i.e. the data of the picture).
- **Broken LaTeX in C20** (`question_tex` and `text`): `$\underline{\hspace{1.2em}}’$` has the typographic closing quote inside the maths.
- **Book numbers.** The LP calls the second Figure it Out box Q5 to Q10, but the book restarts at Q1 on page 110 (the LP's Q5 is the book's Q1, Q6 is Q5, Q7 is Q6, Q8 is Q8, Q9 is Q9, Q10 is Q10; the book's Q2, Q3, Q4, Q7 are not in this chunk). The `ncert_refs` are right (5.1.FiO2.Qn), only `book_number` differs.
- **C27 answer text** says "Venn figures as in the parts"; there are no parts in the LP, so the text relies on the new picture. It should say the figures are above.
- **C13 answer text** says the printed Fig. 5.1 leaves out 6, which is right; with the new question diagram (6 added) the sentence still reads correctly because it speaks of the printed book.
- **C29** adds the pair 2 and 4 that the book does not name (the book says only 8). The LP is right: every multiple of 4 is a multiple of 2, so nobody says "vada" alone.
- **C19** adds the pair 7 and 9 (first idli-vada at 63); the book names 7, 8 and 8, 9 only. Checked: the three pairs below 10 whose first common multiple exceeds 50 are exactly (7, 8), (7, 9), (8, 9).
- All arithmetic of the 18 units was rechecked and holds (150; 30, 18, 6; 300, 180, 60; 320, 360, 400; 360; 2520; 10, 21, 12; 1, 3, 5, 15).

## 3. Where the book itself is unclear

- Fig. 5.1 (chapter p.2) omits 6 from the left circle.
- The printed answer to Q4 uses singular labels "Multiple of 3 / Multiple of 5" and its left-only list is the 16 numbers 3 to 57; it matches the LP.
- The printed answer to Q8 (solutions p.25): the Venn picture is not in the pdf (only the labels "Multiples of 3" and "Multiples of 4" and "Think of some more."), and the pair 3 and 4 is inconsistent with the question's overlap (see 1.5).
- The task "Draw a figure similar to Fig. 5.1 ... 2 and 5, 3 and 7, 4 and 6" has no printed answer in the solutions pdf; the figures are derived from the question (multiples up to 60, left = smaller number, as the task says).
- The jump-arc number line on p.3 prints no colour key; the plan's teaching image is the only guide to which colour is which jump.
