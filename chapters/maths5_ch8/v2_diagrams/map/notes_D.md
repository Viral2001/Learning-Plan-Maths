# Chunk D notes (Class 5 Ch 8 "Weight and Capacity", topics M3.S24.T24 to M3.S32.T32)

Result: 18 units, 32 items: required 4 (C103 q, C104 sol, C105 q, C106 sol), optional 1 (C125 sol), none 27. Validator: errors 0, warnings 0.
Figures claimed: 18 entries = 10 mapped to items (4 beaker groups + 4 "second use" entries for the solution, the double number line + 1 second use) + 8 none.

## 1. Judgement calls

- **C103 / C104 (Big to Small Q3, containers): ONE question diagram and ONE solution diagram for all four groups** (11 beakers on one 16:9 card, 2 x 2 grid like the book), not one per group, because the LP holds it as one question (brief: at most one question and one solution diagram per pair). Beaker heights/widths are not proportional to capacity (the book's are not either). The scale labels are 34 px or larger, so beakers are drawn 210 to 260 px wide and the labels sit inside them.
- **"Group 1:" to "Group 4:" labels are drawn** next to the blanks. The book prints no group labels, but the LP question and the LP solution both refer to "Group 1 ... Group 4", so the picture needs them (decision 3, applied by analogy to numbered groups).
- **C104 solution = required**: the filled totals go on the blank rules of the question figure and the top mark of every beaker is ringed (FOCUS), because the LP solution says a container's capacity is the top mark of its scale. See Borderline.
- **C105 / C106 (Milkman double number line): required on both sides.** The question side: the LP text does not list the ticks; the figure holds all the given values. The solution is the completed line (ANSWER_IS_FIGURE). Ticks are drawn equally spaced and equally long (the book spaces them unevenly, not to scale, and draws the first tick longer so "1 l" and "1000 ml" fit); order, values and blanks are exactly the book's. The book prints "1000 ml" / "2000 ml" without a comma; the LP's "1,000 ml" style is used.
- **Plain tables = text/LaTeX on both sides** (C107/C108 milk table, C118/C119 fuel table), even though each is a table to complete: Step C `LATEX_TABLE` and the Number Play "Counting Numbers" precedent. `text_alternative` gives the LaTeX array content for question and solution.
- **Column addition / subtraction pictures (Example 9 and 10, P13-column_addition-1, P14-column_addition-1, P14-column_subtraction-1) = none, LATEX_ARITHMETIC.** The C116 teaching image (column sums) is not linked and was not the reason.
- **Worked examples C96, C97, C115, C116 = none.** They are practice examples with every quantity in words and arithmetic work; they draw nothing of their own. The existence of the teaching images (C96.IMG1, C97.IMG1, C115.IMG1, C116.IMG1) was not used as a reason (decision 5).
- **C111 (Mary and Daisy) = none, DECORATIVE_ONLY**: the book picture is two girls at a tap with two speech bubbles; both claims are in the LP question text.
- **C125 (Example 10 solution) = optional (not added)**: the book's model "? ... 9 l with an arrow + 5 l 300 ml" would help, but the LaTeX subtraction carries it (Step D example "arrow picture for a sum already written as an expression"). The question side has no given figure (the page-14 pictures are the working), so none.
- **Not inventoried and not added:** the petrol-pump scene on page 12 (pump, car, attendant), the milkman on a bicycle on page 11 and the scrap dealer on page 10 are pure illustration without numbers.
- The figure-inventory entries `NEW-P11-measuring_container-1..4-sol` and `NEW-P11-double_number_line-1-sol` are the second uses (solution cards) of base figures, as the brief asks. The merge should treat them as extra entries, not as new book figures.

## 2. LP text issues

- **M3.S32.T32.C124** (Example 10 question): the text omits the data the question needs, the 5 l 300 ml that Sam put in (it exists only in Example 9 and in the book's arrow picture). The LP solution C125 uses it. Suggested sentence: "After refuelling, Sam found his fuel gauge reading 9 l. Sam had put in 5 l 300 ml of petrol. How much fuel did his bike have before refuelling?" (Also: the question writes "refueling", the steps "refuelling".)
- **M3.S26.T26.C103** (containers question): the question text does not describe the containers at all ("the following containers"); the data is only in the picture and the old q_figure hint. It works once the diagram C103.IMG1 is in. Suggested extra sentence: "Each beaker has a scale; the capacity of a beaker is its top mark. Group 1 to Group 4 are shown in the picture."
- **M3.S27.T27.C105** (milkman): "Complete the double number line" lists none of the given ticks; they live only in the picture C105.IMG1. Suggested: nothing to change once the picture is in, but without it the question cannot be attempted.
- **M3.S24.T24.C93** (tea solution), step 3: broken math delimiters, `$150\text{ ml} ($a practice value; ...` has the opening parenthesis inside the math and the rest outside. Suggested: "Take a cup of about $150\text{ ml}$ (a practice value; cups are not all the same). Two cups hold $2 \times 150 = 300\text{ ml}$." The answer_tex has the same pattern: `$(200\text{ ml}$ of water, ...`. Suggested: "Sample answer: about $300\text{ ml}$ in all (with $200\text{ ml}$ of water and $100\text{ ml}$ of milk). No, $1\text{ l}$ is not needed. Yes, $500\text{ ml}$ is enough. Your answer may differ."
- **M3.S31.T31.C118 / C120**: the LP numbering differs from the book. LP "Let Us Compare Q1" is the book's intro line 1 (Kiran's petrol pump) plus item 2 (the table with (a), (b)); LP Q2 is the book's item 3. Only a numbering remark; the text matches the book.
- **M3.S30.T30.C115 / C116, M3.S25.T25.C96 / C97**: these practice examples have no book source (ncert_refs empty or note only); no text problem found.

All sums, conversions and comparisons in the 14 pair solutions and the 4 worked blocks were recomputed and are right (for example C119: 1,500 + 1,800 + 500 + 96 + 125 = 4,021; C121: 5,600 > 5,400, 10,100 > 1,600, 990 > 909, 3,600 = 3,600, 4,050 < 4,500; C125: 9,000 - 5,300 = 3,700).

## 3. Borderline

- **C104 solution (containers): required, could be none.** Step E lists "figure-based question, numeric answer: S none". Kept required because the printed blanks sit on the figure and the LP solution's key idea (capacity = top mark) is a highlight on the figure that text cannot show (HIGHLIGHT_MEANING). If the user prefers the typical-pair rule, change C104 to none (SAME_AS_QUESTION_DIAGRAM) and drop its four NEW- inventory entries (they would become none:SAME_AS_QUESTION_DIAGRAM).
- **C105 question: required although the book's own line already prints "2000 ml"** (the first question). Kept as the book prints it; the six blanks are the task.
- **C107 / C108 and C118 / C119: tables to complete are none** (LaTeX table) on both sides, although a filled table can count as ANSWER_IS_FIGURE; the plain-table rule was applied as in the Number Play precedent.
- **C125 solution optional** (the arrow model, see above).
- **C92 / C93 tea:** a measuring jug marked 300 ml / 500 ml / 1 l would be a nice picture, but the text carries everything (TEXT_SUFFICIENT, none on both sides).
- **C96, C97, C115, C116 worked examples:** none although each has a teaching image; the picture need was judged on the example itself.

## 4. Where the book itself is unclear

- **Page 11 beaker scales are printed very small.** After enlarging the page 2 times I read: 1 l beaker with "1 l" at the top and "500 ml" at the middle, 4 short ticks in each half (100 ml steps); 500 ml beaker with labelled marks 100 to 500 ml and one short tick between each pair; 100 ml beaker with "100 ml" at the top, "50 ml" at the middle and 4 short ticks in each half. The exact short-tick counts of the 1 l and 100 ml beakers are at the edge of what the print shows (they follow the inventory), but no answer depends on them: capacity is the top mark.
- **Group 1, first beaker:** the "1 l" label is printed left of the scale line, in the other 1 l beakers to the right. The diagram puts every label to the right of its scale line.
- **Double number line (page 11):** the tick spacing is not to scale and does not carry meaning; see Judgement calls.
- No book print slip was found in the figures of this chunk (all values in the pictures agree with the LP solutions), so decision 1 (correct values) was not triggered.
