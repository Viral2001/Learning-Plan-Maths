# Format rules for board-style solutions

These come from a teacher's two rounds of review of Class 10 Ch 7 (Coordinate Geometry) and were then applied to Ch 10 (Circles). Apply them to every solution. The teacher checks each solution personally, so an unnamed formula, a hidden value or a figure that gives away the answer counts as an error.

## The reader

**Write for the student who got it wrong.** The solution will be read by a student whose own answer did not match: they may have gone wrong in the reasoning (wrong property, wrong triangle, wrong hypotenuse) or in the calculation (a sign, a square, a dropped factor, a forgotten last step). So every step must be checkable on its own: say which property is used, show every number that goes in, and show the check at the end. A bare chain of results is not enough.

## Rules

1. **Name the general formula every time it is used.** Write it in general form with its name before substituting, for example "By the distance formula, $d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$". It does not need to be its own step, but it must be stated. The same goes for properties used as reasons: "the tangent is perpendicular to the radius through the point of contact", "angle-sum property of a triangle", "a point on the x-axis has the form $(x,0)$".
2. **Output is LaTeX** (`.tex` source plus the compiled PDF). Never hand over only HTML or docx.
3. **Question, then one merged Solution that ends in a highlighted answer.**
   - Label the item `Question.` in bold with the exact wording, then `Solution.` in bold.
   - There is **no separate "Answer." section**. The final result is the last line of the Solution, in the `\ans{...}` box (see `templates/preamble.tex`). The order is always: main working, then the `\slip{}` note, then the verification, then the `\ans{}` box. An alternative method, if there is one, goes in its own block *after* the box, headed "Alternative solution" (the box closes the main solution; the alternative is extra).
   - Fill-in and multi-part questions get one block per part, for example "Question 2 (i)", each ending in its own `\ans{}`.
4. **Show every value before it is squared, rooted or multiplied.** A student who does not know the step must be able to redo it. Write one operation per line:
   - First the formula with the symbols,
   - then the same line with the numbers put in (negative numbers in brackets: $(-5)^2$),
   - then the differences or products worked out,
   - then the squares, then the sum, then the root.
   The same holds for algebra: show a cancellation or a division as the division (for example $\dfrac{48x(x+14)}{16(x+14)}=\dfrac{16(x+14)^2}{16(x+14)}$, then "$48\div16=3$"), name an identity when it is expanded ("by $(a+b)^2=a^2+2ab+b^2$"), and write a substituted value such as $PR^2=4^2=16$ instead of jumping to $16$.
   Example: $PQ^2=OQ^2-OP^2=12^2-5^2=144-25=119$, not just $PQ=\sqrt{119}$. For the distance formula use the `\dist` / `\distn` macros; TeX computes each displayed number, so the working cannot disagree with the answer.
5. **Add a "Common mistake" note** (`\slip{...}`) wherever a student is likely to go wrong: sign errors when squaring a negative, swapping $m_1$ and $m_2$ in the section formula, taking the wrong side as the hypotenuse, forgetting that a half-chord must be doubled, using the triangle angle-sum where the quadrilateral sum is needed. One or two sentences: what is done wrongly, and why it is wrong. Skip it for steps where nothing plausible goes wrong.
6. **Use the exact NCERT wording** for the question, including options (A)-(D). Transcribe from rendered page images, not from the PDF text layer (see `extraction-pitfalls.md`).
7. **Diagrams only when they help, and never reveal the answer.**
   - No result lengths, solved coordinates or angle values the question asks for.
   - Pure formula or derivation questions get no diagram.
   - If the book has a figure for the question, redraw it, caption it "(redrawn)", and mark only the givens.
   - **The figure must match the question.** After drawing, re-read the question word by word and tick each given against the picture: every named point and line is drawn, every given length is on the right segment, and the shape the solution relies on is visible (for example, if the solution uses a right triangle, the right-angle mark is drawn).
   - **Right-angle marks** (`\draw pic[draw,angle radius=0.3cm] {right angle=A--B--C};`): draw one in every figure of a calculation or MCQ whose solution uses a right triangle, such as the tangent-radius angle at the point of contact. The angle must run anticlockwise from `BA` to `BC`, otherwise the square is drawn outside the corner; swap `A` and `C` if it looks wrong. In a *proof* figure leave the mark off when the 90° is a step of the proof (it would show the conclusion).
   - Construction lines used in a proof may be drawn dashed and labelled "construction".
   - A construction question is the exception: the figure is the answer.
   - If an honest figure would itself show the result (for example a parallelogram that is already a rhombus), omit it and say so in a one-line "Note on the figure".
8. **Data read from a figure becomes an explicit setup step tied to the figure.** Example: "In Fig. 7.8 the horizontal axis is labelled Columns and the vertical axis Rows. Take columns along the x-axis and rows along the y-axis. Then A is $(3,4)$." State the interpretation to the teacher for confirmation.
9. **Cover every question of the chapter**: solved examples and all exercises, unless the teacher narrows the scope. Keep steps meticulous: reasoning, substitution, simplification, conclusion.
10. **Give three things during the validation phase**: the main method, an alternate method where one exists, and a verification (a check by substitution or a second route, with the values shown). Keep them until the teacher says to drop them.
11. **Proofs** use the layout in `solution-types.md`: Given, To prove, Construction (if needed), then a Step / Statement / Reason table. Each reason names the property in words. A proof also ends in `\ans{}` with the proved statement, followed by "(Proved)".
12. **Units and ending**: carry units through the working; the `\ans{}` box states the value with its unit, or the option letter and its value for an MCQ.
13. **Layout**: no heading stranded at the foot of a page, no `Overfull \hbox`, no paragraph that is a wall of text. If an opening paragraph mixes several ideas (a list of methods, a table of cases), split it into a short list or a table.
