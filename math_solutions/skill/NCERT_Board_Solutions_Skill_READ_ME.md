# NCERT Board-Style Solutions: the skill in one file (v1)

This page holds everything in the `skill/` folder in a form you can read from top to bottom, check, and pass on. The same material is split across `SKILL.md`, `references/` and `templates/` so that Claude can load it as a skill. If you change a rule here, change it in `references/format-rules.md` as well.

**What it produces.** For one chapter of an NCERT maths book: a LaTeX file and a compiled PDF with a solution for every worked example and every exercise question, using the exact textbook wording.

**Who the solution is written for.** A student whose own answer did not match. They may have gone wrong in the reasoning (wrong property, wrong triangle, wrong hypotenuse) or in the calculation (a sign, a square, a dropped factor, a forgotten last step). Every step has to be checkable by that student on their own.

Worked on so far: Class 10 Ch 7 (Coordinate Geometry) and Ch 10 (Circles). Both are drafts for the teacher's verification.

---

## 1. The rules

| # | Rule | In practice |
|---|------|-------------|
| 1 | **Name the formula every time.** | Write it in general form before substituting: "By the distance formula, $d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$." Properties count too: "the tangent is perpendicular to the radius through the point of contact." |
| 2 | **Output is LaTeX** plus the PDF. | Never only HTML or Word. |
| 3 | **Question, then one merged Solution that ends in a highlighted answer.** | `Question.` in bold, `Solution.` in bold, working, then common-mistake note, then verification, then the `\ans{...}` box. No separate "Answer." section. An alternative method, if any, is its own block *after* the box. Multi-part questions get one block, one box, per part. |
| 4 | **Show every value before it is squared, rooted or multiplied.** | One operation per line: formula with symbols, then the same line with numbers put in (negatives in brackets), then the differences, then the squares, then the sum, then the root. The same for algebra: show a division as a division, name an identity when you expand it, write $PR^2=4^2=16$ rather than jumping to $16$. |
| 5 | **Common-mistake note** where a student is likely to slip. | `\slip{...}`: one or two sentences, what is done wrongly and why it is wrong. Leave it out where nothing plausible goes wrong. |
| 6 | **Exact NCERT wording**, including options (A)–(D). | Transcribed from rendered page images, never from the PDF text layer. |
| 7 | **Diagrams only when they help, never revealing, and matching the question.** | See section 3. |
| 8 | **Data read from a figure is an explicit setup step.** | "In Fig. 7.8 the horizontal axis is labelled Columns and the vertical axis Rows. Take columns along $x$ and rows along $y$." Flag it to the teacher. |
| 9 | **Cover every question**: solved examples and all exercises. | Sub-parts (i), (ii) count separately. |
| 10 | **Main method, alternate method, verification** during the validation phase. | The verification shows its values. |
| 11 | **Proofs** use Given / To prove / Construction / Step–Statement–Reason table. | Each reason names the property in words. Ends in `\ans{...(Proved)}`. |
| 12 | **Units and ending.** | The `\ans{}` box carries the value with its unit, or the option letter and its value. |
| 13 | **Layout.** | No stranded headings, no `Overfull \hbox`, no wall-of-text opening paragraph (use a short list or a table). |

---

## 2. What a finished solution looks like

This is the shape of Ex 10.1 Q3 in the Ch 10 book (figure omitted here):

```latex
\subsection*{Exercise 10.1, Question 3}
\textbf{Question.} A tangent $PQ$ at a point $P$ of a circle of radius $5$ cm meets a line
through the centre $O$ at a point $Q$ so that $OQ=12$ cm. Length $PQ$ is:\\
(A) $12$ cm \qquad (B) $13$ cm \qquad (C) $8.5$ cm \qquad (D) $\sqrt{119}$ cm.

\textbf{Solution.} Join $OP$. The tangent is perpendicular to the radius through the point of
contact, so $\ang OPQ=90\deg$. Hence $\tri OPQ$ is right-angled at $P$; its hypotenuse is $OQ$.

By the Pythagoras theorem, $OQ^2=OP^2+PQ^2$:
\begin{align*}
PQ^2&=OQ^2-OP^2\\
&=12^2-5^2\\
&=144-25=119\\
PQ&=\sqrt{119}\text{ cm}.
\end{align*}
\slip{The right angle is at $P$, so the hypotenuse is $OQ=12$ and we \emph{subtract}.
Adding, $12^2+5^2=169$, gives $13$, option (B): the tempting wrong choice.}

\textbf{Checking the other options.} ...
\textbf{Verification.} $OP^2+PQ^2=25+119=144=12^2=OQ^2$.

\ans{Option (D): $PQ=\sqrt{119}$ cm.}
```

For the distance formula the `\dist` macro prints all four rows (substitution, brackets, squares, sum and root) from the four coordinates, and TeX does the arithmetic, so the displayed numbers cannot disagree:

```latex
\distnote
\begin{align*}
\dist{PQ}{3}{2}{-2}{-3}{5\sqrt2\approx 7.07}\\
\distn{PR}{3}{2}{2}{3}
\end{align*}
```
gives, for the first row,
$PQ=\sqrt{(-2-3)^2+(-3-2)^2}=\sqrt{(-5)^2+(-5)^2}=\sqrt{25+25}=\sqrt{50}=5\sqrt2\approx7.07$.

---

## 3. Figures

- **Never show what the question asks for.** No result lengths, solved coordinates or angle values.
- **Pure formula or derivation questions get no figure.**
- **If the book has a figure, redraw it**, caption it "(redrawn)", and mark only the givens.
- **Match the figure to the question.** After drawing, read the question word by word and tick each given against the picture: every named point and line drawn, every given length on the right segment, and the shape the solution relies on visible. In every calculation or MCQ figure that uses a right triangle, draw the right-angle mark (`\draw pic[draw,angle radius=0.3cm] {right angle=A--B--C};`, angle anticlockwise from `BA` to `BC`). In a proof figure leave it off when the 90° is a proof step. (Review round 2 found a missing right-angle mark in Ex 10.1 Q3, and a figure in Ex 7.2 Q3 that did not represent the field described.)
- **Construction lines** used in a proof are dashed and labelled "construction".
- **A construction question is the exception**: the figure is the answer.
- **If an honest figure would itself show the result** (a parallelogram around a circle is already a rhombus), omit it and write a one-line "Note on the figure".

---

## 4. Types of question and how to present each

| # | Type | Typical wording | Core of the write-up |
|---|------|-----------------|----------------------|
| 1 | Numerical | "Find", "Calculate" | Named formula, values put in, simplification, verification, `\ans` with unit |
| 2 | Proof | "Prove", "Show that" | Given / To prove / Construction / Step–Statement–Reason table, then `\ans{... (Proved)}` |
| 3 | General derivation | "Derive" | Setup, symbols defined, each algebra step on its own line, boxed result |
| 4 | MCQ with justification | Options (A)–(D) | Work out the value, say why each other option fails and which slip leads to it, `\ans` gives letter and value |
| 5 | Fill in the blank | "Fill in the blanks" | One block per blank, a one-line reason, `\ans` holds the word |
| 6 | Reading data from a figure | "In Fig. …" | Setup step stating axes and scale first, then calculate |
| 7 | Construction | "Draw", "Construct" | Numbered steps, finished figure, reasoning, one-line `\ans` |
| 8 | Word problem | A story with numbers | "Let … be …" first, solve, reject roots that do not fit, `\ans` in words |
| 9 | Verification | "Is it true that…" | Compute both sides separately, compare, state the conclusion |

Method choice: use the textbook's method as the main one; add an alternate method only when it is genuinely different (similarity versus Pythagoras), not a re-wording; add a verification by substitution or a second route.

---

## 5. Step by step (the workflow)

1. **Get the source** (chapter PDF, learning plan if any) into `<class>/<chapter>/source/`.
2. **Render the pages and transcribe every question** from the images (section 6). Number every item in scope.
3. **Classify each item** using the table in section 4.
4. **Solve in Python first.** `source/check_numbers.py` asserts every numeric answer. No number goes into the LaTeX that the script has not confirmed. (Ch 7's script also re-checks the hand-typed value in every `\dist` row.)
5. **Write the LaTeX** with `templates/preamble.tex` and `templates/chapter_skeleton.tex`: one `.tex` per exercise and one for the examples, joined by `\input` in `main.tex`.
6. **Draw figures in TikZ** and check each against its question (section 3).
7. **Compile three times** with `pdflatex -interaction=nonstopmode main.tex`; the log must have no `^!`, `Overfull`, `Rerun` or `Undefined`.
8. **Look at every page** (`pdftoppm -r 70 -png main.pdf pg`) for overlapping labels, stranded headings, messy paragraphs, blank gaps and figures that reveal or mislead.
9. **Report** the file locations, every interpretation made, what was left out, and anything not solved with confidence.

---

## 6. Pitfalls when extracting questions from the PDF

1. Transcribe from rendered page images, not the text layer (it garbles ∠, ⊥, θ, ∥, △, fractions, blanks and primes).
2. Square roots and fractions come out as plain text ("119" for $\sqrt{119}$): check against the image.
3. Fill-in blanks vanish from the text: write them as `\underline{\hspace{2cm}}`.
4. Options (A)–(D) may be reordered or merged: copy the order from the image.
5. "See Fig. 10.11": redraw from the image, keep the book's labels, caption "(redrawn)".
6. Strip running heads ("Mathematics", the chapter title) that the text layer inserts mid-question.
7. "Why?" prompts inside solved examples are questions to the student: answer them.
8. Theorems, Activities and "Think and Discuss" boxes are not exercises: leave them out and say so.
9. Count the questions per exercise from the images and compare with the solution file.
10. On Windows write `.tex` and `.py` files with a file-writing tool, not shell heredocs (they halve backslashes); `sed -i` may silently do nothing.
11. PyMuPDF (`import pymupdf`) can render pages if `pdftoppm` is missing.

---

## 7. Files and tools

```
math_solutions/
  skill/
    SKILL.md                         the skill entry point (loaded by Claude)
    NCERT_Board_Solutions_Skill_READ_ME.md   this file (source)
    NCERT_Board_Solutions_Skill_READ_ME.pdf  this file as a PDF, for reading
    references/  format-rules.md, solution-types.md, extraction-pitfalls.md
    templates/   preamble.tex, chapter_skeleton.tex, check_numbers_template.py
    tools/       readme_to_pdf.py  (rebuilds the PDF from the .md)
  class10/
    ch07_coordinate_geometry/  source/check_numbers.py, latex/main.pdf
    ch10_circles/              source/check_numbers.py, latex/main.pdf
```

Needed: `pdflatex` (MiKTeX or TeX Live) with `amsmath, amssymb, graphicx, enumitem, tikz, xcolor, tabularx, array, needspace, longtable`; `pdftoppm` (Poppler) or PyMuPDF; Python 3.

**To hand to another teacher or another Claude chat:** share the whole `skill/` folder (or the read-me PDF alone, for reading; the `.md` is the source that Claude and the build script use). To install as a Claude skill copy the folder to `~/.claude/skills/ncert-board-solutions/` (all projects) or `<project>/.claude/skills/ncert-board-solutions/`.

---

## 8. Open points to confirm with the teacher

- **Ch 7:** columns are taken as $x$ and rows as $y$ in the figure-reading questions; in Ex 7.2 Q3 the field is read with $AD=100$ m; in Ex 7.1 Q6(ii) the answer is "no quadrilateral"; the TikZ figures are redraws and not to scale.
- **Ch 10:** Ex 10.2 Q11 has no figure on purpose (an accurate one would already be a rhombus); the Ex 10.1 Q4 figure is the answer by design; the Ex 10.2 Q5 figure has no dashed $OP$; theorems and activities are excluded.
