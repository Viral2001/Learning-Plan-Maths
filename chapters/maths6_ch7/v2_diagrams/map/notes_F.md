# Chunk F notes (Class 6 Ch 7 "Fractions", plan cbse_eng_maths6_ch7_v35)

Topics: M3.S26.T26 (Examples 2-6), M3.S27.T27 (Figure it Out 7.8, addition), M3.S28.T28 (subtracting, four worked blocks),
M3.S29.T29 (Figure it Out 7.8, subtraction), M3.S30.T30 (Example 7), M4.S31.T31 (history), M4.S32.T32 (unit-fraction puzzle).
41 items: required 1 / optional 4 / none 36. Validator: errors 0, one expected warning (see 1.1).

## 1. Judgement calls

### 1.1 The only required diagram: M3.S28.T28.C165 (worked example, number line)
"Try doing 6/7 - 4/7 using the number line." The question gives no figure, but its answer IS a drawing (start at 6/7, four hops of
1/7 to the left, land on 2/7) that the LP only describes in words: Step B2 "answer is an arrangement / drawing even if the steps
describe it in words". Sibling: the printed answer of "Try adding 4/7 + 6/7 using a number line" (solutions page 47,
SOL47-number_line-1, which belongs to chunk E, T25.C146) is a number line with hops, so this one is drawn too.
One image (worked example = one diagram, placed after the question text): 0 to 1 in 8 labelled ticks (all eight labels, sevenths),
FOCUS dot at 6/7, four ANSWER-green hop arcs, ANSWER dot and label at 2/7, caption "- 4/7". The book prints no figure for this
"Try doing this" (page 30) and the printed solutions give no answer for it, so no base figure maps to the item (validator warning is expected).

### 1.2 Optional, NOT added: solutions of Example 2 (T26.C149) and Example 3 (T26.C151)  <- the call most worth a second look
The book works both examples with rectangular strips (P26-fraction_strip-1/2/3 for 2/5 + 1/5; P26-fraction_strip-4 and
P27-fraction_strip-1/2/3 for 4/7 + 6/7 = 1 3/7). I judged them teaching figures of the worked example, not figures the item needs:
the question gives no figure; the LP solution already says "2 units of 1/5 + 1 unit of 1/5 = 3 units", "7 sevenths make 1 whole";
tie-breaker "could a careful student solve it from text alone, exactly as well" = yes; and the same-unit idea is already taught with
a concept image (M3.S24.T24.C142.IMG1, chikki 1/2 + 1/4). So optional, with the figure named in `reason`. If you want these drawn,
the specs are easy: Example 2 = three 5-part strips (2, 1 and 3 parts shaded; the third in ANSWER green); Example 3 = two 7-part
strips (4 and 6 shaded) plus one full 7-part strip and a second strip with 3 parts shaded. Note the earlier LP author's `s_figure`
hint on both solutions described exactly these strips.
Examples 4, 5, 6 (different denominators) have no book figure: none. Different kind of example from 2 and 3, so no sibling conflict.

### 1.3 Optional, NOT added: solutions of the puzzle items T32.C187 (Try This 1) and T32.C189 (the 1/6 question)
The book's circle (base id P35-shape-1: 6 equal sectors, 3 green = 1/2, 2 orange = 1/3, 1 blue = 1/6, caption
1/2 + 1/3 + 1/6 = 1) is printed after the argument for both items, so it illustrates the answer 1/2 + 1/3 + 1/6 = 1 of both. The
answers are numbers and are complete with their arithmetic check, so the picture is a visualisation: optional. It is not a
concept image of the plan (concept_images.json has none for T32), so the base figure is mapped `none:TEXT_SUFFICIENT`.
T32.C191 (four units, six solutions) is none: the book draws no circle for it, it only says "try to divide a circle ... to visualise
it", and six solutions cannot be one figure.

### 1.4 M3.S28.T28.C164 (worked 6/7 - 4/7): none
The strips of page 30 (P30-fraction_strip-1/2: 6 of 7 with a brace; 4 parts removed, 2 left) are the teaching picture of this very
concept, and the concept keeps M3.S28.T28.C164.IMG1 (chikki bar, 7 parts, 4 to Joseph, 2 left). Text is sufficient and a second
picture of the same story would sit on the same card. Both base figures are mapped to that concept image (accounting only). Note:
P30-fraction_strip-1 (the 6/7 strip with its brace) is the START state of the concept image's story rather than a separate part of it.

### 1.5 Everything else: none
Plain arithmetic (T27 Q1 a-m; T29 Q1-Q5; T30 Example 7; Examples 4-6): LATEX_ARITHMETIC. Word problems (paint, lace, Jaya, Jeevika and
Namit): TEXT_SUFFICIENT, no figure in the book, printed answers are numbers. The two "why multiply by 3 / by 4" blocks (C167, C168):
the book has only equations and a thought bubble. C184 (history question): answer is words; the concept keeps its Bhinna image.
No question side needs a figure anywhere in this chunk (nothing is given as a figure).

## 2. Things in the LP that look wrong or odd
- Numbering clash: T27 uses "Figure it Out 7.8, Q1-Q3" (addition), and T29 uses "Figure it Out 7.8, Q1-Q3" again for the first
  subtraction set (C170-C175, book page 181) and then "Q4-Q6" for the second set (C176-C181) whose book numbers are Q1-Q3 of
  page 182 (ncert_refs say 7.8.FiO2.Q1-3 and 7.8.FiO3.Q1-3). Book numbers repeat inside the plan.
- T27.C158 question_tex: part (i) is written `(i):` without the math delimiters the other parts have (`$(a)$`, ... `(i)`, `$(j)$`).
- T27.C158: the book's own list repeats (e) and (k) (3/4 + 1/3 + 1/5) and has (f), (g) as the same sum in two orders; the LP copies
  the book. Not an LP fault, but a learner will see duplicates.
- T27.C159 solution gives worked examples for only 4 of 13 parts ("for example ...") and the printed answers for all; fine as written.
- T31.C184 (worked): the single step "The answer is given in the history text that follows the question" is not a solution step
  (a pointer to the page text); the answer line carries the real content.
- T28.C164 / C165 unit-level `ncert_refs` differ from the item's (C165 unit lists none; the item says 7.8.q5): cosmetic.
- All the LP's arithmetic was recomputed against the printed answers (T27 Q1 a-m, Q2 1 5/12, Q3 1 3/20; T29 all; Examples 2-7; puzzle
  sums and the six four-unit solutions): every value agrees with the book. No contradiction found, so no LP-over-book override was needed.

## 3. Where the book itself is unclear
- Page 26 (print 176): the strip printed after "Therefore, 2/5 + 1/5 = 3/5" carries a stray question mark ("= 3/5?"). The LP drops it.
- The printed solutions have no answer for "Try doing this same exercise using the number line" (page 180), unlike the addition
  twin on page 177 (solutions page 47). The C165 figure therefore rests on the LP steps alone (render_note says so).
- Printed solutions page 49 lists the first subtraction set twice (Q1-Q3 with working, then again as "Ans. 1. 1/4 2. 2/9 3. 1/3"):
  same answers, no conflict.
- Page 35 (print 185): "divide a circle into parts like in the figure above" is an invitation for the four-unit puzzle; no figure is
  printed for any four-unit solution.
- Base inventory checks: all ten base figures of this chunk (P26 x4, P27 x3, P30 x2, P35 x1) were checked against the page pictures
  and the descriptions are correct (no CORRECTED entry). No figure was missing from the base for these pages; the thought
  bubbles on page 31 and the history pages carry no figure. SOL47-number_line-1 is NOT claimed here (it belongs to T25.C146, chunk E).
