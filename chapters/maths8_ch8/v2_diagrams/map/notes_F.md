# Notes, chunk F (Class 8 Ch 8 "Fractions in Disguise", plan cbse_eng_maths8_ch8_v56)

Units: M3.S13.T13 (8 pairs, Figure it Out of 1.3), M4.S14.T14 (2 worked blocks: C139, C140), M4.S15.T15 (5 pairs: Example 7, Example 8, Math Talk, Example 10, Example 11). 28 items.

Result: required 1 / optional 1 / none 26. Validator errors 0, warnings 0.

- required: M4.S15.T15.C144 (solution of Example 7), media id `M4.S15.T15.C144.IMG1`, one 16:9 card with both year-by-year tables.
- optional (not added): M4.S14.T14.C139 worked example (book's bar model, 100% to 110%).
- none: all 8 Figure it Out pairs (16 items), C140 check-my-thinking, and the Example 7 question, Example 8, Math Talk, Example 10, Example 11 (both sides).

Pages looked at: 19, 20, 21, 22, 24, 25 (and the p.21 bar diagram at 3x zoom). The Figure it Out pages (19, 20), p.24 and p.25 hold no figure for my items; the only pictures are on p.21 and p.22 (plus p.23, see below).

## 1. Judgement calls

1. **Example 7 solution (C144): required.** The book's worked solution of Example 7 is two annotated year-by-year tables (Option 1 interest paid out; Option 2 interest added back, with x 0.10 and x 1.10 arrows). A filled table that is the answer counts as ANSWER_IS_FIGURE (B2). The LP solution has only "Option 1: 1800 + 6000 / Option 2: x 1.1 three times", so the yearly interest (600, 660, 726) and amounts (6600, 7260) exist only in the picture. Both tables go on ONE card (a pair gets one solution diagram). Teaching image M4.S14.T14.C140.IMG1 shows the same story but is never linked; the item has its own diagram. The two base figures P21-table-1 and P22-table-1 both map to this item.
2. **Example 7 question (C143): none.** The question gives no figure ("a question with no given figure gets no question diagram"), so the solution diagram has `derived_from` null.
3. **Example 8, Math Talk, Example 10, Example 11 solutions: none.** Their printed solutions are two-column arithmetic or formulas in words, not figures. Sibling consistency inside T15: only Example 7's printed solution is a picture, so only that one is drawn.
4. **Figure it Out (T13): all none.** No question has a given figure on p.19-20 and no answer is a picture. Word problems with numbers in the text (TEXT_SUFFICIENT) and arithmetic answers (LATEX_ARITHMETIC).
5. **C140 "Check my thinking": none.** Multiple choice in words and numbers. The concept's teaching image (C140.IMG1) stays untouched.
6. **Figures P23-annotated_expression-1 and -2 claimed by this chunk** (mapped `none:LATEX_ARITHMETIC`). They are the Example 9 expressions on p.23, which sit in concept M4.S14.T14.C141 ("Writing the pattern with letters"). C141 is in my topic T14 but has no question or worked unit in any chunk, so nobody else would claim them. If another chunk also claims them it should use the same meaning (LaTeX lines).
7. **Tags "Option 1" / "Option 2" in the Example 7 diagram.** Rule 4 of section 4 says no headings, but allows tags of at most 3 words that the LP solution text uses; the LP solution says "Option 1" and "Option 2". They are the only text outside the tables. A reviewer who reads the rule more strictly can delete both tags; the column headers ("Interest returned" and "Interest added back") already tell the tables apart.
8. **Colours in the Example 7 diagram.** No question figure exists, so the whole figure is drawn by the solution: table text INK, arrows FOCUS (x 0.10) and SET_A (x 1.10), only the two final totals (7800 and 7986) in ANSWER.

## Borderline

- **C144 required vs LaTeX arrays.** The tables are plain numbers, so a LaTeX array would also work. I kept it as a figure because the printed answer IS this picture and the arrows (x 0.10, x 1.10) carry the idea of "interest grows because the base grows". If the content team prefers arrays, the item becomes `none` (LATEX_TABLE) and the two figures map to `none:LATEX_TABLE`.
- **C139 optional vs none.** The book's rough bar diagram (principal = 100%, interest 10%, amount = 110%) would help, but no Step-B trigger holds: the data is in the steps and answer, the question names no figure, and the figure is a teaching figure with no concept image in the plan. Marked optional (reason says which figure). If it is ever drawn: principal line 6000 (100%), 10% = 600, amount 6600 (110%), long arrow "Amount after 1 year" spanning from 0 to the right-hand line (see section 3).
- **Figure it Out Q3 (company, C127/C128), Q6 (election, C133/C134), Q8 (milkman, C137/C138):** a bar or table picture could help the reader but would only make it nicer; kept none.

## 2. LP text issues

Only listed, nothing changed (decision 2 of 23 Nov).

T13 (Figure it Out):
- **C131 / C132, C133 / C134, C135 / C136, C137 / C138:** the LP copies the book's printed question numbers (3, 4, 6, 7). On p.20 the book restarts numbering at 3 (a print slip: it follows 5, so these are 6, 7, 9, 10 in sequence of the set), so the plan shows "3." twice. Suggested: drop the printed number from `question_tex` or use the corrected 6, 7, 9, 10 (and the book_number fields likewise).
- **The set also has four questions that are not in my units:** printed 5 on p.19 (petrol price rise, 6 options), printed 5 on p.20 (rice inflation 38 to 42), 8 (elephants, p x 1.05) and 9 (cameras, demand fell by 85%). Please check they exist elsewhere in the plan (they do not appear in chunk F).
- **C124 (Ans1):** the steps are only "Profit over cost." Suggested: "Profit = 110 - 75 = 35. Profit margin on cost = 35/75 x 100, about 46.67%."
- **C128 (Ans3):** steps and answer contain teacher-facing text: "Discuss the base first.", "(see 4.4)", "Accept either when the student names the base; a good 4.4 check." Suggested: "Margin on revenue: profit = 25% of 2.5 crore = 0.625 crore, so costs = 2.5 - 0.625 = 1.875 crore. If the margin were taken on cost, cost = 2.5 / 1.25 = 2 crore."
- **C136 (Ans7):** the answer ends "...which is 72; M4". The misconception code "M4" has leaked into learner text. Suggested: "90 / 1.2 = 75 (not 90 - 18 = 72, because 18 is 20% of 90, not of the number)."
- **C138 (Ans8):** the only step is "The topic's one faded multi-step problem (see faded ladder below)." This is not a solution. Suggested: "Buffalo 1 (profit 5%): cost = 80,000 / 1.05, about 76,190. Buffalo 2 (loss 10%): cost = 80,000 / 0.9, about 88,889. Total cost about 1,65,079; total selling price 1,60,000; loss about 5,079, which is about 3.08% of the cost." (checked: 5079.37 / 165079.37 = 3.077%).
- **C125:** `question` says "I am a carpenter", `question_tex` says "You are a carpenter" (small mismatch; the book has "I").

T14:
- **C139 (worked example):** the question text is only "Interest and amount after 1 year"; the data (6000, 10% p.a., 1 year) appears only in the steps. Suggested: "A bank pays 10% p.a. on a fixed deposit. If 6000 rupees is deposited for 1 year, what is the interest and what is the amount after 1 year?"
- **C140 (check my thinking):** the text ends "Act on the diagnosis table." (an internal instruction in learner text). Answer (b) 1100 is right: year-2 interest is 10% of 11,000.

T15:
- **C143 (Example 7 question):** the text is only "Example 7". Missing: "If one deposits 6000 rupees in the bank at 10% p.a., what is the amount after 3 years? Option 1: the interest is paid out every year. Option 2: the interest is added back (compounding)." The rate 10% p.a. appears in neither the question nor the solution text; the diagram shows it (from the book).
- **C144 (Example 7 answer):** "7800 against 7986" has no labels. Suggested: "Option 1 (interest paid out): 7800. Option 2 (compounding): 7986."
- **C145 (Example 8 question):** only "Example 8". Suggested: "What percent is the total amount received of the amount deposited (6000), in both options of Example 7?"
- **C147 / C148:** named "Example 3: Q / Ans" (and book_number "Example 3: Compounding: total interest in both options"), but this is the Math Talk on p.24, not an Example 3 (the book's Example 3 is on p.16). The question text "Math Talk: total interest" lacks the question. Suggested: "What is the formula for the total interest at the end of the maturity period, for each of the two options (without compounding and with compounding)?"
- **C149 (Example 10 question):** only "TV value after 1 year", no data. Suggested: "A TV is bought at 21,000 rupees. After 1 year its value depreciates by 5%. Find the value of the TV after one year."
- **C151 (Example 11 question):** only "Village after 3 decades", no data. Suggested: "The population of a village is reducing by about 10% every decade. If the current population is 1250, what is the expected population after 3 decades?"
- **C152 (Example 11 answer):** "About 911, i.e. around 910" is fine, but the book shows two routes (911.25 without rounding, 912 rounding each step) before saying "around 910"; the LP states only the first.

## 3. Where the book itself is unclear or wrong

- **p.20 numbering:** the Figure it Out set is numbered 1 to 5 on p.19 and then 3 to 9 on p.20 (print slip; see section 2).
- **p.21 bar diagram (P21-bar_model-1):** prints "1000" above the principal line although the principal is 6000 (the text above it says 6000 and 600). The diagram is not drawn (optional item), so nothing is corrected in a spec; the base inventory keeps what the book prints. Also the long arrow "Amount after 1 year" stops short of the "?" line (the base inventory's doubt); it should span 0 to "?". Both points matter only if someone draws it later.
- **p.22 Option 2 table (P22-table-1):** the third year's "726" has no "added back" caption (years 1 and 2 have it). Kept as printed in the Example 7 diagram (stated in its `render_note`). Not a mathematical error.
- **Growth label:** the book writes "x 1.10" on the compounding arrows, the LP writes "x 1.1". The diagram follows the book.
- All inventory descriptions of P21-table-1, P22-table-1, P23-annotated_expression-1/-2 matched the page pictures; none needed "CORRECTED".
- Recomputed in the spec: Option 1 interest 600 x 3 = 1800, total 7800; Option 2 6000 -> 6600 -> 7260 -> 7986, interest 600, 660, 726 (each Ending = Beginning + interest). The LP answers of every unit with a numeric answer were recomputed and are right (46.67%, 712.50, 1.875 crore or 2 crore, 225, 5,17,647, 31.25% and 4 candidates, 75, loss about 5,079, 130% and 133.1%, 19,950, 911.25).
