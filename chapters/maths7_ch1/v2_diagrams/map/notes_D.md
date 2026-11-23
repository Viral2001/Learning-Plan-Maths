# Chunk D notes (Class 7 Ch 1, plan cbse_eng_maths7_ch1_v30)

Units: Figure it Out 1.6 Q1-Q14 (M6.S35.T35, units 48-61), Toothpick Digits worked examples C159 and C160 (M6.S36.T36, units 62-63), 24-sticks question pair (M6.S37.T37, unit 64). 32 items: required 5 / optional 2 / none 25. Validator: errors 0, warnings 0.

Required diagrams:

| Item | Media id | What it draws |
|---|---|---|
| Q9 question (C147) | M6.S35.T35.C147.IMG1 | 7 empty boxes over 5 empty boxes, right-aligned |
| Q9 solution (C148) | M6.S35.T35.C148.IMG1 | the same boxes twice, filled for the largest sum and for the smallest difference |
| C159 worked example | M6.S36.T36.C159.IMG2 | the book's p.23 digit strip 0-9 in sticks |
| C160 worked example | M6.S36.T36.C160.IMG2 | same strip, identical spec |
| C163 question (24 sticks) | M6.S37.T37.C163.IMG1 | same strip, identical spec |

## 1. Judgement calls

1. **Q9 solution holds both answers in one figure.** The item carries one media id, so the two finished arrangements (largest sum, smallest difference) are stacked in one picture, each under a short tag ("Largest sum", "Smallest difference", words the LP steps use). If the team wants one picture per part, the item would need two media ids (the validator allows one). Q9 question: required although the LP text describes the layout in words, because the book says "each box below" and the learner fills the boxes (FIG_REFERENCED, ACTION_ON_FIGURE); the printed answer is a picture, so the solution is required (sibling consistency).
2. **The stick-digit strip on three items (C159, C160, C163).** The only text fact the book gives is "the digit 7 needs three sticks"; the shape and stick count of every other digit exist only in the strip, so counting sticks, moving four sticks and "exactly 24 sticks" cannot be attempted without it (DATA_IN_FIGURE). The existing teaching images of C159 and C160 show only 42,019 and 63,890, not the strip, and are never linked. Per the brief, one diagram per item with an identical spec. C160 is the weakest of the three (the previous card already showed the strip); drop it if only one strip is wanted.
3. **The strip has no stick counts and no number built of sticks.** It shows only the ten digits with a numeral under each, so the counting in the example stays the learner's job. Drawn as two rows of five (0-4 over 5-9) instead of the book's single strip so that the 16:9 card is used and the sticks are large; reading order is kept.
4. **The digit 7 has three sticks.** The page picture draws the 7 with four bars (an extra upper-left bar); the book text says three, and the LP solutions only work with three (42,019 to 42,078 adds two sticks; 1 to 7 adds one). The diagram follows the text and says so in `render_note` (also flagged by the inventory agent).
5. **Optional, not added:** (a) Q4 solution (a picture of the 20 digits with the struck ones crossed would help, but the steps name the struck digits and the printed answer is the number only); (b) 24-sticks solution (2008 and twelve 1s drawn in sticks and counted to 24; the answer is numeric, the steps carry the counts, the book has no printed answer picture). I judged the stick drawings "nicer", not needed, once the question carries the strip. If the team reads "make a number with sticks" as a drawing answer, (b) becomes required with `derived_from` the strip.
6. **None by rule:** Q1-Q3, Q5-Q8, Q10-Q14 (text and LaTeX). Q7: the book draws no calculator on p.20. Q10: the seven cards are plain numbers in the text (NUMBER_LIST_IN_BOXES). Q12-Q14: the birds on p.21 are decoration and every datum is in the text. Q11: the Statue of Unity is not drawn. Q6: the LP answer card had two images in the old plan; a pure digit-count argument, no figure.
7. **Page 19 Titanic picture** (section 1.5, before "Figure it Out") is an illustration and belongs to another chunk; not claimed.

## 2. Things in the LP that look wrong or thin

- **Q9(a): the LP and the book disagree, and the LP is right.** The book's printed picture (top 9 9 8 8 7 7 6, bottom 6 5 5 4 4) gives 99,88,776 + 65,544 = 1,00,54,320. That is a valid use of the cards but not the largest sum. The LP's 99,87,654 + 87,654 = 1,00,75,308 is larger and is the maximum (greedy by place value: places 10^6 and 10^5 take one digit each, the rest two each). The solution diagram follows the LP. Q9(b) (11,22,334 and 99,887, difference 10,22,447) is the same as the book and correct.
- **Q2:** the LP says 61 letters for 77,77,777; the book's printed answer says 60. I recounted: seventy(7) seven(5) lakhs(5) seventy(7) seven(5) thousand(8) seven(5) hundred(7) seventy(7) seven(5) = 61. A brute-force check of all 7-digit numbers also gives maximum 61, reached by 81 numbers, smallest 73,73,373, as the LP step says. The LP is right.
- **Q3:** the book's example (987654312) does not meet the condition for every swap and it does not count; the LP (only 12,34,56,789) is right. **LP text inconsistency:** the plain `steps` and `answer` fields write "1,23,45,67,89" (wrong Indian grouping), while `steps_tex`, `answer_tex` and `text` write "12,34,56,789" (correct). The plain fields should be fixed.
- **Q6(c):** the LP says 13,495; the book prints 13995. Counting fives by computer gives the 5000th five in 13,495, so the LP is right. Q6(a) 3 in 370 and Q6(b) 1,85,185 are right.
- **Q10:** the LP gives exact results for (a)-(d) (checked: 13000 x 20 - 150000 = 1,10,000; 70000 x 5 - 150000 = 2,00,000; 150000 + ((4000 + 300) x 20) x 5 = 5,80,000; (13000 + 70000) x (20 - 5) = 12,45,000, each card used once) and 20,91,000 for (e), 200 away. The book only shows closer attempts ((a) 1,13,000, (d) 12,44,500). The LP question text leaves out the book's worked sample for (a) (4000 x (20 + 5) + 13000 = 1,13,000), which is fine because the LP's own (a) is exact.
- **Q12:** the LP question says "cross an ocean" (as in the book's answer page); the book's question page says "the Pacific Ocean". Trivial.
- **Q14:** the question depends on Somu's building being 40 m (from an earlier topic); the question text does not state it, only solution step 1 does. The book's printed answer writes "10,000 - 12,000 m" for aeroplanes in one place while the question says 12,800; the LP uses 12,800 (correct, 12,800 / 40 = 320).
- **C159 and C160 numbers checked by a stick-segment script:** 42,019 plus exactly two sticks gives exactly 42,049, 42,078, 42,818, 42,879, 48,019, 92,019 (the LP's list; the LP's extra 1,42,019 adds a new digit 1). All five numbers the LP gives for moving four sticks of 63,890 are real four-stick moves, and 99,985 is the biggest five-digit number reachable by moving four sticks. Placing a 1 in 4,2,0,1,9: the five numbers and the biggest 4,21,019 are right.
- **C164:** biggest 24-stick number = twelve 1s, 1,11,11,11,11,111 (12 x 2 = 24); smallest 2008 (5 + 6 + 6 + 7 = 24; three digits hold at most 21 sticks, and 1 as first digit leaves 22). Both right.

## 3. Where the book is unclear

- **Solutions pages exist.** The brief says the pdf has no printed-solutions section, but pdf pages 24-38 are printed answers; the only pictures among them for my chunk are the two Q9 arrangements (p.36, p.37).
- **P20 (Q9 boxes):** the page does not say which row is the larger number or which operation goes with which row; the 7-digit over 5-digit reading is taken from the box counts and the right alignment. Colours: peach (top) and lavender (bottom) in the book, mapped to the SET_B and SET_A outlines on white.
- **P23 digit strip:** the 7 has four bars in the picture but three sticks in the text (see 1.4). The book prints no answers for the toothpick puzzles and no pictures for them.
- **Q5:** the book's answer page has no printed answer for Q5 (question 5 is skipped between Q4 and Q6); the LP answer ("no such pair found") was not re-derived here.
