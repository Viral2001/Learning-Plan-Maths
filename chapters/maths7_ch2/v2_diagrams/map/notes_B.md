# Chunk B notes: Class 7 Ch 2 "Arithmetic Expressions" (units 19 to 30)

Topics: M2.S15.T15 (Examples 7 to 11), M2.S16.T16 (Figure it Out 2.2 Q1 to Q3), M3.S18.T18 (Examples 12 to 14), M3.S19.T19 (Tinker the Terms I).
12 pair units, 24 items: required 5 (question 2, solution 3), optional 0, none 19. Validator: errors 0, warnings 0.

Note on the brief: it says the pdf has no printed-solutions section, but pdf pages 23 to 40 are the printed answers ("Ans:"). I used them (pages 26, 27, 28, 29 and 30 matter for this chunk).

## 1. Judgement calls

Required diagrams
- **Example 11 question (C53.IMG1), solution (C54.IMG1).** The LP question restates the two arrangements in words, so a careful student could attempt it from text. I still drew it, because the book's question is "here are two pictures, which one matches 5 x 2 + 3, and what is the expression for the other using its yellow and blue squares". The stacks and their colours are what the expressions are read from. Solution: braces and labels (5 x 2, 3, 2 x, 5, 3) add the grouping the steps only describe in words. If you want fewer images, the question is the one to drop (set to `optional`); the solution would then need `derived_from` null and a drawing of the whole arrangement. The teaching image M2.S14.T14.C44.IMG1 shows the same two arrangements with the answers on it. It is never linked (v3 rule), so the question figure carries no labels.
- **Figure it Out Q3 question (C59.IMG1), solution (C60.IMG1).** The figure belongs to part (c) only. The question figure is the window, to scale, with the book's three dimension marks and the Total Height arrow, and no values leaked. The solution is the borderline one: a figure-based question with a numeric answer is normally "Q required, S none". I made the solution required because it adds something visual that the question figure lacks (the length of all 15 parts: seven 5s, six 2s, two 3s, and 53 cm). It could be set to `optional` without harm.
- **Tinker the Terms I solution (C72.IMG1).** The book's printed answer is a drawn grid of 10 filled cards, so by B2 the solution is required. The question side is `none` (TEXT_SUFFICIENT): the LP question already lists every sum, so the blank-circle grid adds nothing, and the filled grid is shown once before the steps. The alternative (question grid with blanks required, solution derived from it) is also defensible. The solution figure covers both blocks of the pair (the main block and the -87 block), as one picture, because a pair gets one solution diagram.

None, and why
- **Oval term-marking lines (Examples 7, 8, 9, 11).** These are the book's way of marking terms inside its worked answer (e.g. "(4 x 23) + (5) = (92) + (5) = (97)"). They are not part of what any question gives, and every LP solution already names the terms in words and writes the chain in LaTeX. I did not treat the ovals as HIGHLIGHT_MEANING. The book itself says the oval marking "is not a usual practice".
- **Example 8 stick-figure children (six groups of 5 plus 3).** DECORATIVE_ONLY: the LP question states 33 students, groups of 5 and 6 x 5 + 3, then asks about groups of 4 and 7, which the picture does not show. The printed answer is text only. A dot-group picture for the solution would be nice but not needed (not even `optional`, since no book picture exists for it).
- **Examples 10, 12, 13, 14, Figure it Out Q1 and Q2:** plain arithmetic or open-ended, no book figure. The Example 12 to 14 teaching ideas already have teaching images in T17 (not touched here).
- No `optional` used in this chunk.

Figure inventory choices
- Reprints of a question figure on the answers page (P29 window, P30-table-1 grid) are `none:SAME_AS_QUESTION_DIAGRAM`.
- Second uses of a base figure (the Example 11 arrangements and the window, once more for the solution) have `NEW-<base id>-sol` ids. The two Example 11 arrangements are both claimed by the same question item because they are drawn as one picture.
- All 12 base figures of this chunk were checked against the page pictures. Counts verified: window has 6 grills, 7 gaps, 2 borders; Example 11 left = 5 stacks of 2 plus 1 stack of 3, right = 2 stacks of 5 yellow over 3 blue; Example 8 = 6 groups of 5 plus a group of 3. No base description needed correcting.

## 2. Things in the LP that look wrong or changed

- **Tinker the Terms I, LP versus book.** The book's question grid prints 54 + (-16) = 38 as the filled worked example (with a sentence), and leaves -87 + (-16) blank. The LP does the reverse: it asks the learner to find 54 + (-16), and gives -87 + (-16) = -103 as given in the second block. The LP wins; the solution figure draws 38 in ANSWER green and the -103 of the first card in column 3 in INK. The LP's `q_figure` hint for C71 is wrong in the same way (it also describes only some cards).
- **Example 11 wording.** The LP calls the vertical stacks "rows" ("5 rows of 2 squares", "2 rows, each with 5 yellow and 3 blue squares"). In the book picture they are vertical columns/stacks. A learner reading "rows" could picture horizontal rows. The figure keeps the book's vertical stacks. Suggest "stacks" or "columns" in the LP text.
- **Example 14 story changed.** The book: Hira has 28 coins in one bag and 35 in another, and gifts 10 coins from the second bag, so 28 + (35 - 10). The LP: "Meera has 28 coins in one bag and puts in a bag holding 35 - 10 coins". The expression is the same, but the story no longer matches the book's point (the bracket comes from taking 10 away from the second bag), and "puts in a bag holding 35 - 10 coins" is awkward.
- **Names changed from the book** (harmless): Example 7 (Amu, Charan, Madhu and John become "four friends"), Example 8 Ruby is now Tanvi, Example 9 Raghu is now Meera, Example 10 Kannan is now Joseph, Example 14 Hira is now Meera, Figure it Out Q3(a) Queen Alia, Elsa and Anna removed.
- **Figure it Out Q3 `answer_tex` / `answer`:** has a stray semicolon after "(b)": "$(b)$; (i): ..." (should read "(b): (i) ... (ii) ..."). The same slip is in the `text` field.
- **Figure it Out Q1(e):** the book's printed answer writes the terms as "6 x 3, 4 x 8 x 5" (minus sign missing); the LP correctly has "-4 x 8 x 5".
- **Example 10, one more way:** the book's printed answer is 40 x 10 + 3 x 10 + 2 x 1; the LP gives 4 x 100 + 3 x 10 + 2 x 1. Both equal 432.
- **Figure it Out Q2:** the book's story for (a) is about library books, the LP uses pencils; (b) and (c) are "make your own" in the book and the LP supplies samples. Fine, but the question side is open-ended, so no figure.
- **Stale ids:** ignored as instructed. Every old card id of this chunk (C45.IMG1 ... C72.IMG2) is dropped by the build; the 5 new ids are M2.S15.T15.C53.IMG1, C54.IMG1, M2.S16.T16.C59.IMG1, C60.IMG1 and M3.S19.T19.C72.IMG1.

## 3. Places where the book itself is unclear

- **Window (Figure it Out Q3c).** The picture is not to scale (gaps look far taller than 5:2). Only one border (top, 3 cm), one grill (2nd, 2 cm) and one gap (between grills 3 and 4, 5 cm) are dimensioned. The bottom border's size is not printed (the LP says 3 cm at top and bottom). The window's width is not given: drawn 36 units wide for proportion only. The cat, curtains and flower pot are decoration and are not drawn. The figure is drawn to scale because the LP gives every length.
- **Tinker printed answer (p.30).** Explanation sentences appear in column 1 card (c) and in column 3 cards (b), (c), (d) but not in column 1 and 2 cards (b); the text has typos ("les", "Yes, - 15 is one more than - 16?"). They are sentences, not diagram content, so the figure leaves all of them out (the LP steps carry the reasoning).
- **Example 8 picture.** Group boundaries are shown only by spacing, and the "+" signs sit between the three columns, not between every group. Not drawn.
- **Example 10 (text).** The book says "coins of Rs 1 and Rs 5, and notes of Rs 10, 20, 50 and 100" but then explains "2 notes of Rs 1" and "4 notes of Rs 5". The LP question avoids the words.
- **Colours of Example 11.** The book uses green and red on the left, yellow and blue on the right. Drawn in house tokens: green stacks = MARK_FILL, extra stack = FOCUS (pink), yellow = SET_B (amber), blue = SET_A. The LP's text mentions only "yellow and blue", so those two matter; the left-hand colours are cosmetic.
