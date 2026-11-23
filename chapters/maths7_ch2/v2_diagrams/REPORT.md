# Class 7 Ch 2 Arithmetic Expressions - V2 diagram update, 23 Nov 2026

Source: LIVE V2 `cbse_eng_maths7_ch2` v44 (taken from staging). Result: new V2 version v45 (uploaded ACTIVE, read back identical). Rules: `spec/` v3 (docs/karan-MD). Tokens inserted, no pictures drawn, stamp skipped, videos/tools/concept images untouched.

## Decisions (108 items from 60 units)
{"worked_example": {"none": 11, "required": 1}, "question": {"none": 44, "required": 3, "optional": 1}, "solution": {"none": 39, "required": 7, "optional": 2}}

Optional, NOT added: [('C98', 'question'), ('C115', 'solution'), ('C121', 'solution')]

needs_lp_text_sync: []

## The 11 diagrams
| id | side | type |
|---|---|---|
| M1.S6.T6.C17.IMG1 | solution | other |
| M1.S6.T6.C19.IMG1 | solution | other |
| M2.S11.T11.C33.IMG1 | worked example | integer_tokens |
| M2.S15.T15.C53.IMG1 | question | other |
| M2.S15.T15.C54.IMG1 | solution | other |
| M2.S16.T16.C59.IMG1 | question | mensuration_figure |
| M2.S16.T16.C60.IMG1 | solution | mensuration_figure |
| M3.S19.T19.C72.IMG1 | solution | cell_grid |
| M3.S22.T22.C97.IMG1 | solution | other |
| M3.S22.T22.C99.IMG1 | solution | other |
| M3.S24.T24.C114.IMG1 | question | number_pattern |

### Chunk A notes (from the decision agent)
# Chunk A notes (Class 7 Ch 2, topics M1.S2.T2 to M2.S13.T13)

Result: 29 items (11 pairs = 22 items, 7 worked examples). Required 3 (Example 2 solution, Example 3 solution, worked example C33), optional 0, none 26. Validator: errors 0, warnings 0. 23 figure_inventory entries (22 base figures plus one NEW- accounting entry).

## 1. Judgement calls

1. **Example 2 and Example 3 solutions (M1.S6.T6.C17, C19): required.** The book explains both examples with a bar picture ("the situation can be represented as shown in the picture"), and the LP solution only describes it in words. Tie-breaker says optional-ish, but the picture is the book's whole argument and the earlier author's `s_figure` also treated it as the solution picture. The two are decided the same way (sibling). Reason codes FIG_REFERENCED + HIGHLIGHT_MEANING. If the content team wants fewer diagrams, these two are the first to demote to optional.
   - Questions C16 and C18: none. The question gives only the two expressions; the picture is the explanation, not given data (companion note: no question figure when the question gives none).
   - The same Example 2 picture is also the teaching image M1.S5.T5.C13.IMG1. It is not linked; the solution gets its own diagram (v3). Accounted by a second entry `NEW-P02-bar_model-1-teaching`.
2. **Names in the two bar pictures.** The book and the T5 teaching text/image use Raja and Joy; the LP solution steps C17/C19 use Kabir and Farhan; the videos use Jia and Ruhee. The specs use the names of the solution steps (Kabir, Farhan) because the picture is shown right above those steps. If the team prefers Raja and Joy, change the two captions in both specs.
3. **Example 3 brace label.** The book labels both braces 24, but Raja's brace runs under the extra circle too (it removes 25). The LP says Kabir loses 25, so Kabir's brace is labelled 25 and Farhan's 24 (LP text wins). Stated in the spec's `render_note`.
4. **Worked example M2.S11.T11.C33 ("say why using counters" for (-9) + 4): required** (ANSWER_IS_FIGURE + HIGHLIGHT_MEANING). This is the closest call. The answer to "using counters" is a counter arrangement that the steps only describe in words, and the printed answer of the matching Try This (token model, pdf p.24) is a picture (rule B2). The book has no picture for (-9) + 4, so there is no base figure for the item itself; the two printed token pictures of p.24 are claimed as the source idea (mapped to this item). If the team treats the counters as teaching only (the video M2.S11.T11.C33.VID1 and the teaching image C32.IMG1 already show counters), demote to optional. No other item in the chunk asks for counters.
5. **Grouping token pictures (P25-token_model-1, -2): none (TEXT_SUFFICIENT).** Same kind of printed answer as p.24 but the LP has no item that asks for counters on grouping (C34 is "add in three ways" in text). If counters on grouping are wanted, an item has to be added to the plan first.
6. **Oval marking of terms and red grouping ovals: not drawn.** The book's ovals (P05, P06, P07, P08) are a notation: terms in ovals, red ovals for groupings. All of them are written in LaTeX (`\boxed` for a term, brackets for a grouping), the LP steps already list the terms in words, and none is data a learner needs to attempt a question. Mapped none:LATEX_ARITHMETIC (P06-table-1 none:LATEX_TABLE). Applies to the worked examples C24, C34, C35 and to C30/C31, C38/C39.
7. **C30/C31 (the Try This table of terms): none/none.** The book question is "complete the table" (act on a given figure), but the LP rewrote it as four expressions in words, so the question is fully attempted from the text; the completed table is a plain three-column table (LaTeX array). The book's printed answers (pdf pp. 23 to 26) have no entry for it, so there is no printed-answer picture. A LaTeX array is given in `text_alternative` of C31. This is the second-closest call (rule B2 "filled table" could be read as ANSWER_IS_FIGURE); chosen none because the "Terms" column repeats what the ovals show.
8. **C12 (order the five expressions): none.** The answer is one chain of expressions (a sequence), not a drawn arrangement; the book's printed answer is the same chain in text.
9. **C40 (Manasa's list): none.** The five numbers and the forgotten 9055 are all in the LP question text, so the handwritten list of the book (P08-number_list-3, P26-number_list-1) adds nothing. TEXT_SUFFICIENT (not NUMBER_LIST_IN_BOXES: the numbers are a handwritten column, not boxes).
10. **Compare-five (C20/C21): none.** The empty boxes in the book are blanks for the sign, not a figure; I did not add a NEW- inventory entry for them.

## 2. Things in the LP that look wrong or worth a look

- The pdf is not "without printed answers": pages 23 to 40 are an answer key ("Page No. 24", "Page No. 25", ...) for the in-chapter Try This and Figure it Out items, with pictures on pp. 24 and 25 (token models and expression chains). The brief says there is none. I used pages 23 to 26 for this chunk; the LP solution text still wins where they differ (they do not differ in this chunk).
- Three name sets for one marble story: Raja/Joy (book, T5 teaching text and teaching image), Kabir/Farhan (C17, C19 steps), Jia/Ruhee (video titles C13.VID1, C19.VID1). Not a diagram problem but the learner meets all three.
- Example 5 (C28/C29) calls the buyer Farhan, and Example 2 uses Farhan for a marble story: same name in two stories (the book uses Irfan for Example 5). Examples 1, 4, 5 have renamed characters compared with the book (Mallika to Meera, Mallesh and Arun to Meera and a friend, Irfan to Farhan); fine, noted.
- C36 step 3: "...which is a different value, because the −5 term lost its sign." reads muddled (the point is that 5 − 12 is not the swap of 12 − 5 with its sign). Wording only.
- C21 `answer_tex` is "(a) > (b) = (c) < (d) < (e) <" (trailing "<", a copy of the book's printed answer); correct but awkward.
- Hints `q_figure` (C30) and `s_figure` (C31, C17, C19) were read as hints only. C30's `q_figure` describes the table that the LP question no longer shows; the question text has no row for the example row 13 − 2 + 6.
- Every number in the LP solutions of this chunk was recomputed and is right (e.g. 245 + 289 = 534 > 531 = 246 + 285; 364 + 587 = 951 < 952 = 363 + 589; 213 − 77 = 136 < 138 = 214 − 76; 1342 + 774 + 8611 + 1022 = 11749 and 11749 + 9055 = 20804; (−7) + 10 + (−11) = −8 in all three orders; 5 × (3 + 2) + 7 × 8 + 3 = 84).

## 3. Where the book is unclear

- Example 3 picture (pdf p.2): both braces carry the label 24 although Raja's brace also covers the extra circle; brace widths are only roughly equal. The spec uses 25 for Kabir's brace (see 1.3).
- Example 2 picture: Joy's 1022 bar is drawn about 8 percent longer than Raja's; the base inventory already noted it. The spec draws both 800 px (the picture is not to scale in the book either: the 125 bar is 40 percent of the 1022 bar).
- Base figure descriptions for all 22 chunk figures were checked against the page pictures (pp. 2, 5, 6, 7, 8, 24, 25, 26): all correct, no "CORRECTED:" needed.
- Book boxes for the compare-five question (p.3) and the Shalini and Manasa characters (pp. 3, 8, 9) were treated as blanks/decoration and left out of the inventory.

### Chunk B notes (from the decision agent)
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

### Chunk C notes (from the decision agent)
# Chunk C notes (Class 7 Ch 2, topics M3.S20.T20 to M3.S23.T23)

Result: 31 items (15 pairs + 1 worked example). Required 2, optional 1, none 28. Validator: errors 0 (one harmless warning: the label "2 × 43 + 2 × 24" has more than 6 words).

## 1. Judgement calls

1. **Example 15 solution (M3.S22.T22.C97) and Example 16 solution (M3.S22.T22.C99): REQUIRED (the only two diagrams in this chunk).**
   The book prints the tray picture (Example 15) and the coloured array (Example 16) with their braces as the worked answer itself:
   per friend vs per item for Example 15, and 3 × 5 + 4 × 5 vs (4 + 3) × 5 for Example 16. The braces and colours carry the meaning of removing the bracket, which LaTeX cannot show reliably.
   The earlier authors' `s_figure` hints also expected these pictures. Same kind of answer in the same example set, so the same decision for both (sibling rule).
   This is the main decision to confirm. Both pictures duplicate the teaching images M3.S21.T21.C91.IMG1 and C92.IMG1. Those stay untouched and are not linked (v3).
   If the user wants no duplicate of a teaching image here, flip both solutions to `none` with `REUSES_CONCEPT_IMAGE` plus `LATEX_ARITHMETIC` (nothing else changes).
   Content notes:
   - The book's photographs are redrawn as flat schematics (trays as rounded boxes; cutlet as a SET_B circle; rasgulla as a white circle; fleur-de-lis replaced by plain dots).
   - The book's two small curved arrows over the left label (Example 15) and the right label (Example 16) are left out: their arrowhead targets are not clear in the printed figure (the inventory agents also flagged this).
   - The Example 16 colours follow the concept image C92 (scouts blue = SET_A, guides amber = SET_B); the book is green (top 3 rows, guides) and yellow (bottom 4 rows, scouts).
   - Given content is INK, SET_A, SET_B; braces and their labels are ANSWER green, because they are what the solution adds.
2. **Example 16 question (C98): OPTIONAL, not added.** The book says "(see the figure below)", but the LP question was rewritten to state every count (4 rows of 5 scouts, 3 rows of 5 guides), so a careful student loses nothing without the picture (tie-breaker). The array without braces would help; it is not needed to attempt. The solution figure draws the whole array itself (`derived_from` null). Example 15's question is `none` (the book's question gives no figure; the tray picture only appears in the explanation).
3. **Worked example C93 (10 × 98 + 3 × 98, 14 × 10 − 6 × 10): NONE.** The two book figures on page 17 (repeated additions of 98 and of 10 with braces and a strike-through) are written lines. LaTeX `\underbrace` says the same, so they are mapped `none:LATEX_ARITHMETIC` and the item is `no_image`. The question gives no figure.
4. **Figure it Out 2.3 Q1 to Q9, Examples 17 and 18, "third friend" and "use the method": all none, both sides.** Plain arithmetic, equalities and reasoning.
   - Q1's empty squares are sign boxes inside lines of text, not a figure. `text_alternative` suggests `\square` and `\underline{\hspace{1.2em}}`, one part per line.
   - Q7 and Q8 are open ended.
   - Example 18: the area picture of the teaching topic (C94.IMG1, a 100 × 25 rectangle) is not in the book and is never linked; the arithmetic is complete in text.
   - "Third friend" (Sangmu in the book, Tanvi in the LP): a three-tray picture is not in the book and would only be decoration.
5. **Base figures claimed (6, all checked against pages 16 and 17):** P16-term_marking-1 and P16-term_marking-4 (terms in ovals) and P17-braced_sum-1 and P17-braced_sum-2 are `none:LATEX_ARITHMETIC`; P16-arrangement-2 maps to the C97 solution and P16-array-3 to the C99 solution. I did not claim P14-table-1 (Tinker the Terms I, belongs to topic M3.S19.T19) or the page-19 figures (belong to topic M3.S24.T24). The base inventory has no entry for the empty sign boxes of FiO 2.3 Q1, and I added none (they are text).

## 2. Things in the LP that look wrong (not fixed here; nothing outside the two output files was edited)

- **M3.S20.T20.C73 (Q1) `question_tex`:** parts (a), (b), (d), (e), (f) run into one paragraph, for example `... \underline{\hspace{1.2em}} (b): ...` with no line break between (a) and (b). The boxes are the plain text `[ ]`, not `\square`. Each part should be on its own line.
- **M3.S20.T20.C74 (Ans1) `answer_tex`:** the `$` signs are unbalanced and the `;` separators are missing in two places: `$(c)$: $- (d)$: $-$, $4$` and `$-$, $- (f)$: $8$, $-$, $3$`. This renders "(c): −(d) ..." with (d) and (f) inside the maths. It should read `$(c)$: $-$; $(d)$: $-$, $4$` and `$(e)$: $-$, $-$; $(f)$: $8$, $-$, $3$`.
- **C77 (Q3) and C79 (Q4):** the question text is as in the book. Q4(b) prints `87 + 46 − 109` three times (an NCERT misprint, also in the book itself); the LP solution explains it as "the same written three times", which is consistent.
- **C84 (Ans6) (a):** the sentence "the right side must add 4 more than the left blank" is muddled (it should say the right blank is 4 more than the left blank, e.g. 423 + 0 = 419 + 4). The stated answer 423 + 419 = 419 + 423 is correct.
- **C82 (Ans5) (c):** correct (−22 − 12 + 10 + 22 = −2 as printed, and −22 − (12 + 10) + 22 = −22).
- **`video_media_id` on the answer concepts (C74, C76, C78, ...):** the ids point to the next concept's video (for example C74 carries `C75.VID1`); these are the stale references the user told me to ignore.
- **C93 worked example:** its text omits the book's printed typo "98 × 10 + 9 × 83 = 98 (10 + 3)", which is good.
- **Names:** the LP uses Meera and Kabir (the book: Lhamo and Norbu), Tanvi (the book: Sangmu) and Meera (the book: Jasoda). The diagrams draw no names.
- **All arithmetic in this chunk was re-checked:** 2 × 67 = 134 and 86 + 48 = 134; 2 × 43 + 24 = 110; 20 + 15 = 35 = 7 × 5; 5 × 4 + 3 = 23; 63 × 18 = 954 + 180 = 1134; 97 × 25 = 2500 − 75 = 2425; 3 × 67 = 201; 95 × 8 = 760; 104 × 15 = 1560; 49 × 50 = 2450; the Q7 value set {10, 6, 4, 0, −4, −6}.

## 3. Where the book itself is unclear

- Page 15, FiO 2.3 Q4(b): the first three expressions are printed identically (`87 + 46 − 109` three times); the book probably meant three reorderings of the same terms. No figure is involved.
- Page 16, the two curved arrows over the labels 2 × (43 + 24) and (4 + 3) × 5: the arrowhead targets are not clear.
- Page 16: the book does not name the colours' groups; green = guides (top 3 rows) and yellow = scouts (bottom 4 rows) follow from the row counts in the text and the braces.
- Page 17: "98 × 10 + 9 × 83 = 98 (10 + 3)" is a printing error in the book (should be 98 × 10 + 98 × 3). It is not in the LP and no figure uses it.

### Chunk D notes (from the decision agent)
# Chunk D notes (Class 7 Ch 2, plan cbse_eng_maths7_ch2_v44)

Units: Figure it Out 2.4 Q1-Q4 (M3.S24.T24), three worked examples of "Solving Problems with Expressions" (M4.S25.T25),
Figure it Out 2.5 Q1-Q6 (M4.S26.T26), Puzzle "Expression Engineer" (M4.S27.T27). 24 items:
required 1 / optional 2 / none 21. Validator: errors 0, warnings 0.

## 1. Judgement calls

- **2.4 Q4 question (M3.S24.T24.C114): required, ONE diagram holding both pictures** (id `M3.S24.T24.C114.IMG1`, 16:9).
  The book question says "the numbers given in each picture below", so the pictures are the question (FIG_REFERENCED, DATA_IN_FIGURE).
  The pair is allowed one question diagram, so Picture I (3 x 3: yellow squares 4 at corners and centre, blue circles 8 at edge middles) and
  Picture II (4 x 4: blue 5 at corners and middle block, red 6 on the other edge circles) sit side by side, left and right as in the book.
  Checked against pdf page 19 and the reprint on page 37: the base descriptions are correct.
  Choices to confirm if you disagree: (a) the book's captions "(I)" and "(II)" (printed only on page 37) are NOT drawn, because figure letters are
  on the never-draw list and the LP text names the pictures; (b) the book's yellow / blue / red are approximated by the style-token pair
  SET_B (amber) for squares-4 and circles-6, SET_A (blue) for circles-8 and circles-5, as light tints with INK digits (the digit carries the
  meaning, not the colour). If you want an exact yellow/blue/red palette, the renderer needs three extra colours outside the token table.
- **2.4 Q4 solution (C115): optional, not added.** Both the printed answer (page 38) and the LP solution are arithmetic
  (5 x 4 + 4 x 8 = 52, 2 x (4 + 8 + 4) + (8 + 4 + 8) = 52, 8 x (5 + 6) = 88, 4 x 22 = 88). A marked-up copy of the question figure
  (braces 5 x 4 and 4 x 8, row totals 16, 20, 16, the 5s and 6s grouped) would help but a careful student loses nothing without it
  (tie-breaker -> optional, not required). If the team decides it wants it, the spec would be derived_from `M3.S24.T24.C114.IMG1`.
- **2.5 Q1 solution (C121): optional, not added.** Same logic: the snail part (c) would gain from a post with the height after each day and night
  (why 8 days and not 10) but the 7 x (3 - 2) + 3 = 10 line carries it, and the book prints no figure. Question side none (no given figure).
- **Everything else none.** All other questions and answers are fill-ins, comparisons, word problems and arithmetic (LATEX_ARITHMETIC / TEXT_SUFFICIENT / OPEN_ENDED).
  Siblings are consistent: all six 2.5 questions and Q1-Q3 of 2.4 are none on the question side; Q2/Q4/Q5 of 2.5 (sign and choice answers)
  and Q1/Q2 of 2.4 are none on the solution side.
- **Worked examples (baker, 57 x 30 - 20, 91 - (35 + 12)):** none. These are LP-made examples, not book figures; a 6 x 7 calendar for the baker would be nicer
  but the arithmetic carries it.
- **Inventory:** P19-pattern-1 and P19-pattern-2 both map to the Q4 question item (they are one diagram). P37-pattern-1 and P37-pattern-2 are the same
  two pictures reprinted in the book's answers section (with captions); the printed answer beneath them is text only, so they are
  `none:SAME_AS_QUESTION_DIAGRAM`. The Puzzle page (pdf page 22) has only the owl banner and the row of children: decoration, not inventoried.
  The distributive-property brace figures on page 17 (P17-braced_sum-1 and -2) belong to the section text, not to a unit of this chunk, so I did not claim them.

## 2. Things in the LP that look wrong or need a look

- **C108 question_tex (2.4 Q1) is garbled.** The (c) to (p) parts run together: e.g. `... 3 \times \underline{\hspace{1.2em}} (d)$: ...` (the next part label sits inside the previous
  maths), (i) has no `$`, and (m) to (p) are glued into one math span (`... 3 \times 7 (m) 5 \times (12 - ...`). The answer_tex of C109 has the same gluing
  (`$(l)$: $- (m)$ any $n (n) 6$ ...`). Not a diagram matter, but it will render badly; each part should be its own line.
- **C108 (e) in the book reads "3 ____ + ____" (the multiplication sign is lost in the print);** the LP reads it as `3 x ____ + ____`, which is the sensible reading. Book answer
  uses 10 in (e) and 3 in (m) with the remark "you may put any number other than 10 and 3 respectively"; the LP says "any number n works". Both fine.
- **2.4 Q3 solution differs from the book's printed answer:** LP gives 2 x (2 + 5), 2 x (3 + 4), 7 x (1 + 1), 1 x (5 + 9); the book gives 2 x (5 + 2), 2 x (3 + 4), 7 x (1 + 1), 2 x (6 + 1).
  All four LP fills equal 14 (14, 14, 14, 14). LP kept (it wins).
- **2.5 Q6 solution uses 24, the book uses 26.** All ten LP expressions for 24 check out (12 + 12, 4 x 6, 48 / 2, 34 - 10, 20 + 4, 30 - 6, 8 x 3, 100 - 76, 2 x (5 + 7), 72 / 3).
- **2.5 Q3(a):** the book's Way 1 groups all positives and all negatives; the LP gives the pairs method and a leave-out-the-ends method instead (both give -5). Fine.
- **2.4 Q4 question text restates the figure in words** ("Five squares ... eight cells show 5 and eight cells show 6"). With the diagram added this is redundant, and the last clause
  hints at the grouping the book wants the student to find. Suggest trimming it to the book wording once the figure exists (the data then lives only in the figure). Left as is, since I change nothing else.
- Stale ids: several answer items carry a `video_media_id` that belongs to the NEXT question's concept (e.g. C109's video is `C110.VID1`), and C117 and C118 share the
  concept name "Comparing and matching by reasoning". Ignored as instructed; items were matched by their own concept id.

## 3. Arithmetic re-checked (all hold)

- Q4 pictures: left 5 x 4 + 4 x 8 = 52, rows 16 + 20 + 16 = 52; right 8 x 5 + 8 x 6 = 88, rows 22 x 4 = 88.
- Baker: 7 - 1 = 6; 6 x 6 = 36; 36 x 14 = 504; 7 x 6 x 14 = 588; 1 x 6 x 14 = 84; 588 - 84 = 504.
- 57 x 30 - 20 = 1690, 57 x 31 - 20 = 1747, difference 57. 91 - (35 + 12) = 44, -35 + 91 - 12 = 44, 91 - 35 - 12 = 44, 91 - (35 - 12) = 68.
- 2.5 Q1: 7 x 20 = 140; 12 x 12000 = 144000, 240000 - 144000 = 96000; snail 7 x 1 + 3 = 10 on day 8.
- 2.5 Q2: values (a) 80, (b) 40, (c) 56, (d) 112, (e) 33, (f) 72, (g) 40, (h) 16. 2.5 Q4 and Q5 signs and values recomputed, all match the LP.
- Puzzle: 3 x (3 - 3) = 0, (3 + 3) / 3 = 2, 3 + 3 / 3 = 4, 3 x 3 - 3 = 6, 3 + 3 + 3 = 9, 3 x 3 + 3 = 12.

## 4. Where the book itself is unclear

- The Q4 pictures are printed with different gaps on page 19 and page 37 (page 37 has the circles of Picture II nearly touching); the spec uses pitch 1.4 for Picture I and 1.15 for
  Picture II and says so in `render_note`. Squares are very slightly smaller than circles in both prints (0.95 against 1.0).
- The book's text for 2.4 Q1 (e) loses the "x" sign (see above). Question 2.5 Q6's printed answer in the extracted text is partly garbled (the fourth line reads "52 / 4. 2", i.e. 52 / 2).
