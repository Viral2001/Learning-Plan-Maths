---
name: ncert-board-solutions
description: Write board-exam-quality, step-by-step solutions to NCERT maths textbook questions as LaTeX plus a compiled PDF, written for students who may have made reasoning or calculation errors. Use when asked to solve, write up or verify the worked examples and exercises of a maths chapter (any class), with exact question wording, named formulas, every substituted value shown, a merged Solution-and-highlighted-Answer, common-mistake notes, proof tables and redrawn figures that match the question.
---

# NCERT board-style solutions (v1, after teacher review round 2)

Produces a LaTeX solution book for one chapter: every worked example and every exercise question, with the exact textbook wording, a main method, an alternate method where one exists, and a verification.

**Reader to keep in mind:** a student whose own answer was wrong, by a reasoning slip or a calculation slip. The write-up must let them find where they went wrong.

## Workflow

1. **Get the source.** A chapter PDF and, if available, a learning plan that lists the questions. Put copies in `<class>/<chapter>/source/`.
2. **Render the pages and transcribe the questions.** Follow `references/extraction-pitfalls.md`. The PDF text layer is not safe for maths. Make a numbered list of every item in scope: examples, then each exercise, with sub-parts as separate items.
3. **Classify each item** using `references/solution-types.md` (calculation, proof, MCQ, fill-in, figure reading, construction, word problem, verification).
4. **Solve in Python first** for every numeric answer. Write `source/check_numbers.py` (start from `templates/check_numbers_template.py`) that asserts each answer and prints it. Do not write a number into the LaTeX that the script has not confirmed.
5. **Write the LaTeX** in `latex/`: copy `templates/preamble.tex` and `templates/chapter_skeleton.tex`, then one file per exercise (`ex10_1.tex`) and one for the examples, joined by `\input` in `main.tex`. Follow `references/format-rules.md` exactly.
6. **Draw figures in TikZ** only where they help. Then re-read the question against the figure, point by point (rule 7 of the format rules): every given drawn, nothing revealing, and any right angle or shape the solution depends on visible.
7. **Compile three times** with `pdflatex -interaction=nonstopmode main.tex`, then search the log for `^!`, `Overfull`, `Rerun` and `Undefined`. There must be none.
8. **Look at every page.** Render with `pdftoppm -r 70 -png main.pdf pg` and view each image. Fix overlapping labels, stranded headings, messy opening paragraphs, big blank gaps and figures that reveal answers or do not match the question.
9. **Report to the teacher**: where the files are, every interpretation you made (figure axes, readings of an ambiguous question), what you left out (theorems, activities) and any question you could not solve with confidence.

## Folder layout

```
math_solutions/
  skill/                      this skill
    SKILL.md
    references/               format-rules.md, solution-types.md, extraction-pitfalls.md
    templates/                preamble.tex, chapter_skeleton.tex, check_numbers_template.py
    NCERT_Board_Solutions_Skill_READ_ME.md   one-file version of everything, for reading and sharing
  class10/
    ch07_coordinate_geometry/ (source/ and latex/)
    ch10_circles/             (source/ and latex/)
```

## Rules that matter most

- Name the general formula or property every time it is used.
- **Solution and answer are one block**: Question, then Solution, ending in a highlighted `\ans{}` box. No separate "Answer." section.
- **Show every value before it is squared, rooted or multiplied**, one operation per line (`\dist`/`\distn` for the distance formula).
- **Write for the student who went wrong**: explain each step, add `\slip{}` common-mistake notes, and show a verification with values.
- Diagrams never reveal the answer, derivation questions get none, and a figure must match its question (re-read the question against it).
- Cover every question in scope. Count them against the book.
- Never change a teacher-validated chapter without being asked.

## Tools needed

`pdflatex` (MiKTeX or TeX Live) with the packages in `templates/preamble.tex`, `pdftoppm` (Poppler) or PyMuPDF for page images, and Python 3 for number checks. On Windows, write `.tex` and `.py` files with a file-writing tool, not shell heredocs (they halve backslashes).

## Install

Copy the `skill/` folder into `~/.claude/skills/ncert-board-solutions/` (all projects) or `<project>/.claude/skills/ncert-board-solutions/` (one project). No project paths are baked in.
