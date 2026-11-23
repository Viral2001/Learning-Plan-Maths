# Notes for chunk B (Class 5 Ch 15 "Data Through Pictures"; topics M2.S8.T8 to M2.S13.T13)

Result: 29 items, required 18 / optional 0 / none 11. Validator: errors 0 (5 warnings: the five worked examples have no printed book figure, which the brief allows).

Counts by role: question required 7 / none 5; solution required 6 / none 6; worked example required 5.

## Judgement calls

1. **Recording a Day, Q1-Q5 (C41/C43/C45/C47/C49), question side required, solution side none.**
   The LP question texts carry no data. The hours of Raman (9, 6, 2, 6, 1) and Sheela (8, 7, 4, 3, 2) are only in the book's table of squares (p.4) and bar graph (p.5), and no teaching image holds them (the teaching images of T8 use Kabir and Samaira). So all five questions get the same picture, one copy per item (render_note says "Same picture as M2.S9.T9.C41.IMG1"). The solutions only read two values off the question figure, compare, and give a number or a name, so they are `none` (SAME_AS_QUESTION_DIAGRAM, TEXT_SUFFICIENT), as in the Step E pair "figure-based question, answer is a number or word".
   The picture shows the words **Raman** and **Sheela** above the two panels. They are not headings in the v3 sense: the questions ask "Whose ...", so the reader has to know which panel is whose. Please keep them.
2. **Worked examples C38, C39, C51, C52, C68 are all required** with their own diagram (user decision 5), although each has a kept teaching image of the same idea.
   - C38 and C51 and C52: the worked example's answer is a drawn graph, so the single diagram (placed after the question text) shows the finished state: C38 the three rows of squares, an arrow and the three bars; C51 the five bars; C52 the three strips. Bars/strips the example builds are ANSWER green.
   - C39 and C68: the data are read from the figure, so the figure shows what the question gives (Kabir's rows plus Samaira's bars; the newspaper bars). Nothing is marked.
3. **Day in My Life Q1/Ans1 (C54/C55): both `none` (LATEX_TABLE).** The book's blank table and the LP sample answer are plain tables of names and hours with no colour meaning. Text alternatives for both are in the items. This breaks the "filled table = ANSWER_IS_FIGURE" reading of B2 on purpose: Step C says a plain table goes to LaTeX.
4. **Day in My Life Q2/Ans2 (C56/C57): both required.** The question points at the blank graph template "in the space given below" (ACTION_ON_FIGURE), the answer is a drawn bar graph (ANSWER_IS_FIGURE). Solution is `derived_from` the question figure; it adds the six bars and the two names Playing and Other activities in ANSWER green.
5. **Whose Index Finger is Longer?**
   - C58 (paste the strips) question required: the given blank strip graph. C59 solution required, derived from it: five sample strips (6, 7, 5, 8, 6 cm) and the names Friend 1 to Friend 4.
   - C60, C62, C64, C66 (the four questions on the child's own graph): question `none` (OPEN_ENDED). The book gives no data here, only the child's own graph, and the LP question texts carry no figure or numbers; "a question with no given figure gets no question diagram".
   - C61, C63, C65, C67 solutions: required, each draws the whole sample graph (`derived_from` null, because there is no question figure) with the answer marked: longest strip boxed (C61); guide line from the top of the longest strip to the 8 mark (C63); shortest strip with guide line to the 5 mark (C65); shortest strip and its name box boxed (C67). Reason: GRAPH_CHART and HIGHLIGHT_MEANING (circled smallest / boxed largest), and the sample graph exists nowhere else on these cards.
6. **Figure inventory.** The base figure P04-pictograph-2 and P05-bar_graph-1 are each used five times (one per Recording a Day question): base id for the first use, `NEW-<base>-q2` to `-q5` for the other four. P06-bar_graph-1 and P07-bar_graph-1 have one entry for the question that shows the template and one `NEW-...-sol` / `-s59` .. `-s67` entry for every solution that redraws it with the sample answer. P06-table-1 maps to `none:LATEX_TABLE`. P06-activity_picture-1 (hand and strip) and P07-notice_board-1 map to `none:DECORATIVE_ONLY`.
   - **P08-bar_graph-1 (food-wastage graph) is deliberately not claimed here.** It belongs to the food questions of chunk C (T14). I only claimed the notice board of that section (P07), because no food question uses its 13 kg and 25 people. If chunk C does not claim P07-notice_board-1, the merge needs one of us to.

## Borderline
- **Recording a Day solutions (C42, C44, C46, C48, C50) = none.** A highlighted copy of the same figure (the two compared rows circled, hours written beside them) could be argued as HIGHLIGHT_MEANING. I kept `none`: the question figure is already in the card above it and the LP text lists every number. C48 (the five pairs, answer No) and C50 (balanced routine, an opinion) are the two I am least sure about.
- **Worked examples C38/C51/C52 show the answer (finished graph) before the steps**, because a worked-example token must sit after the question text. If the content team wants only the given data, the bars would have to be removed (then C38 would show the rows only; C51 and C52 would need no figure).
- **C61/C63/C65/C67 required.** The LP text lists all five heights, so a strict reading could make them `none`/TEXT_SUFFICIENT. I kept them because the solution reads a graph that has no other figure on its card, and C59 (same kind of answer set) is required.
- **C54/C55 none (LATEX_TABLE)** against a possible ANSWER_IS_FIGURE reading of "filled table" (see above).
- **C56 question required.** The frame is only a template (scale, axis titles, place names), but it is what the book gives and what the child draws on; the alternative is OPEN_ENDED/none.

## Book mistakes and corrections
- The book prints the header word **"Activites"** (a spelling slip) in Raman's table; the diagram shows "Activities". No numbers are wrong anywhere in my pages. Sheela's bars have no printed numbers; heights 8, 7, 4, 3, 2 were read against the grid and agree with the LP.
- The book's Day-in-My-Life graph prints "Time in School" (capital S) while its table prints "Time in school"; I kept each as printed.
- The book's grids carry half-lines (dashed) and a decorated frame; the specs use a clean grid at whole numbers only.

## LP text issues
- **M2.S9.T9.C41, C43, C45, C47, C49 (questions Q1-Q5):** the texts never say whose data they use, and Q4 says "they". Suggested sentence to add at the start of each: "Raman recorded his day in a table and Sheela in a bar graph (see the picture)."
- **M2.S10.T10.C52 (worked example):** the pencils have no names, but the figure needs them. Suggested sentence: "Samaira measures three pencils: Pencil 1 is 9 cm, Pencil 2 is 6 cm and Pencil 3 is 4 cm." The diagram uses Pencil 1, 2, 3 in that order (from the teaching image).
- **M2.S8.T8.C39 (worked example):** the vertical scale of Samaira's graph is not stated. The diagram uses 0 to 6 (as in the teaching image). Suggested sentence: "Samaira's graph has its vertical line marked 0 to 6."
- **M2.S13.T13.C68 (worked example):** the vertical scale and the graph title are not stated. The diagram uses 0 to 7 and the title Newspapers (kg) (from the teaching image). Suggested sentence: "The bar graph is called Newspapers (kg) and its vertical line is marked 0 to 7."
- **M2.S12.T12.C60, C62, C64, C66 (questions 2-5):** the question texts give no data; the sample strips (Mine 6, Friend 1 7, Friend 2 5, Friend 3 8, Friend 4 6 cm) appear only in the solutions, so a learner who has not made strips cannot attempt them. Suggested sentence: "Use the sample graph: Mine 6 cm, Friend 1 7 cm, Friend 2 5 cm, Friend 3 8 cm, Friend 4 6 cm."
- **M2.S12.T12.C66 (question 5):** "It belongs to ___." has no antecedent ("it" = the smallest index finger). Suggested sentence: "The smallest index finger belongs to ___."
- **M2.S11.T11.C54/C55:** the book leaves two table rows unnamed; the sample answer names them Playing and Other activities, but the question text does not say so. Suggested sentence in the question: "Use the two empty rows for playing and other activities."
- **M2.S12.T12.C58:** "the given bar graph" is not in the LP text; the diagram supplies it (no LP change needed once the figure is added).
- LP numbering differs from the book's: LP "Whose Index Finger is Longer?: Q1" is the book's strip activity; LP Q2-Q5 are the book's questions 1-4. Harmless.

## Where the book itself is unclear
- Sheela's bars carry no numbers (read from the grid, consistent with the LP).
- The book's Day in My Life and finger graphs are student templates; the sample values come only from the LP solutions (practice values), so the diagrams show those and nothing else.
- The notice board (13 kg feeds 25 people) is not the same ratio as the food question rule (1 kg feeds 3 children); this is as printed and belongs to chunk C's questions, not to any item here.

## Layout note for the renderer
All diagrams are 16:9 (1920 x 1080) with explicit pixel positions in `manim_description`. The five Recording a Day pictures are identical on purpose. Category-label wrapping is given line by line; at 34 px, "activities" is about 180 px wide and fits the 196 px slot of Sheela's graph.
