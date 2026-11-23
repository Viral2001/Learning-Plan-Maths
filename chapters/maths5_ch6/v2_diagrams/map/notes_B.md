# Chunk B notes - Class 5 Ch 6 "The Dairy Farm" (topics M2.S9.T9 to M2.S16.T16)

Result: 14 units, 24 items. Required 9 (question 4, solution 3, worked example 2), optional 1, none 14.
Figure inventory: 12 entries = 9 base figures of chunk B + 3 second-use `NEW-` entries (one per solution diagram that redraws a book picture).
Validator: errors 0, warnings 2 (C40 and C53 worked examples are required but their pictures are not printed in the book; expected).

Required diagrams (media ids):
- M2.S10.T10.C40.IMG2 (worked, 8 x 13 cut -> 4 x 26; kept teaching image IMG1 untouched)
- M2.S11.T11.C43.IMG1 (question, 3 x 18 cut and stacked as 6 x 9)
- M2.S12.T12.C45.IMG1 (question, 22 x 5 cut, blank equation) and M2.S12.T12.C46.IMG1 (solution, derived from it)
- M2.S13.T13.C53.IMG2 (worked, 6 x 19 and 13 x 31 in one two-panel picture; kept teaching image IMG1 untouched)
- M2.S14.T14.C55.IMG1 / C56.IMG1 (4 x 19 question / solution) and C57.IMG1 / C58.IMG1 (14 x 21 question / solution)

Colour mapping used (book picture to style token): light orange squares = light tint of SET_B (the 'yellow' of the LP steps), green column = MARK_FILL, white column = BG, red cut lines / arrows / dashed boxes = FOCUS, blue dashed box 6 x 9 = 54 = SET_A, everything added by a solution = ANSWER.

## Borderline

1. M2.S11.T11.C43 question (3 x 18), required. The question text states the cut and the result in words, so a strict tie-breaker could say none. Chosen required because "arranged in the following way" points at the book's picture and the task is to discuss why the two are the same; sibling of 22 x 5.
2. M2.S12.T12.C45 question (22 x 5), required. Again the text describes the whole arrangement. Chosen required for sibling consistency with a) and because the book's blank equation sits inside the figure. If the user prefers none here, C46 solution stays required but must be redrawn stand-alone (`derived_from` null) and the figure inventory entry P06-array_cut-2 moves to the solution.
3. C44 solution none vs C46 solution required (same NCERT set). Reason: in a) the book's picture already holds the result (6 x 9 = 54 is printed in it), so a solution figure would only repeat it (`SAME_AS_QUESTION_DIAGRAM`). In b) the picture holds a blank equation; the solution fills it (11 x 10 = 110) and marks 11 rows and 10 squares across. The addition is small (an equation and two brackets), so this is a close call; if the user wants strict symmetry, either both are required or C46 becomes none.
4. M2.S10.T10.C40 and M2.S13.T13.C53 worked examples, required under user decision 5 although a teaching image of the same concept shows the figure. C53's single diagram draws both parts (6 x 19 and 13 x 31) in two panels (61 x 18.5 units, about 30 px per square on a 1920 card). If it looks crowded when rendered, the alternative is the first part only.
5. M2.S9.T9.C39 solution, none. The old `s_figure` hint was an array of 5 rows of 18 split 10 and 8, which would show only way (3) of the five children's ways; the answer is a reasoned yes, not a drawing. Optional idea only.
6. M2.S12.T12.C47 question none and C48 solution optional. The four book frames (Half / Double arrows with empty boxes) are a fill-in form; the problems and blanks are in the question text. Per the `NUMBER_LIST_IN_BOXES` rule the filled arrow frames are at most optional because the LaTeX lines give every step. Not added.
7. M2.S15.T15.C62 solution, none. The steps talk about "strips" of squares, but this question has no picture and the answers are arithmetic; no diagram drawn (sibling of C50 which is also arithmetic).
8. M2.S10.T10.C41 and M2.S16.T16.C63 worked examples, none (halving/doubling chain and a mix of three strategies, all arithmetic).
9. M2.S14.T14.C55 / C57 questions: the picture has no text in the book either, so `visible_text` is empty; the equation sits in the question text and is not drawn. The solutions add the outline of the white / green column and the calculation lines of the LP steps ("4 x 20 = 80", "4 extra squares", "80 - 4 = 76"; "14 x 20 = 280", "14 left out", "280 + 14 = 294"), each of which uses the LP's own words and numbers.

Figure letters (decision 3): none of my pictures holds several lettered figures, so no letter is drawn anywhere (the LP answers do not refer to the pictures by letter).

## LP text issues

(No LP text was edited and no decision was changed because of these.)

- M2.S13.T13.C53 (worked example): the question gives the tray only for 6 x 19 ("A tray has 6 rows with 19 squares in each row ... Then find 13 x 31 the same way"), but the steps use "the 31st square of every row" and "a strip of 13 squares", so the learner is never told there are 13 rows of 31 squares. The diagram draws 13 rows of 31. Suggested sentence: "Then find 13 × 31 the same way, with a tray of 13 rows and 31 squares in each row."
- M2.S12.T12.C48 (solution, step 4): the learner-facing step says "the book does not label the arrows of this box". This is also true of the 16 x 4 box, and a solution should not talk about the book. Suggested sentence: "$35 \times 14$: $35$ is odd and cannot be halved into a whole number, so halve the $14$ and double the $35$. Half of $14$ is $7$ and double $35$ is $70$. The new problem is $70 \times 7 = 490$, so $35 \times 14 = 490$."
- M2.S15.T15.C62 (solution): steps (1) to (6) speak of "the strip is 2 squares in each row", "the strip is 15 squares", but the question shows no tray or squares. Suggested wording: "the extra part is 2 in each row, 7 × 2 = 14" (and the same for the other five).
- M2.S16.T16.C63 (worked example, step 4): "The strip is 8 packets too many" refers to a strip no picture shows. Suggested sentence: "That counts 8 packets too many, one for each of the 8 trays: 320 − 8 = 312, so 8 × 39 = 312 packets."
- M2.S14.T14.C58 (solution, step 2): the LP says the first 20 squares are "yellow" and the last "green"; the book prints light orange and light green. The diagram uses a yellow-orange tint and a light green, so the words still fit; no change needed unless the user wants "orange".
- Old image hints: the `q_figure` / `s_figure` strings of the old cards (for example C39 "array of 5 rows of 18", C44 "54 written beside both", C48 "four boxes filled in") describe pictures that are not drawn in this run; the lines of the new plan should not refer to them.

## Book unclear

- Frames 16 x 4 and 35 x 14 (P06-half_double_frame-5 and -6) have empty upper boxes: the words Half and Double are not printed, and the book does not say which of the two numbers to halve in 35 x 14 (the LP solution halves the 14 because 35 is odd).
- Doubling and Halving b) shows the blank equation "__ x __ = ____" with no number printed in it; the only reading is 11 x 10 = 110 (halve the 22 rows).
- The pdf has no printed solutions section, so every solution here follows the LP text. No print slip (wrong digit, wrong count, missing sign) was found in the chunk B pictures; the counts on the page pictures were checked by pixel analysis (3 x 18 and 3 x 9 blocks, 22 x 5 and two 11 x 5 blocks, 4 x 20, 14 x 21), so the LP and the book agree and nothing needed correcting.
- Overlap with another chunk: P05-coloured_boxes-3 ("What is 18 x 5" boxes) sits in the book section "Many Ways to Multiply", which chunk A's topic M2.S8.T8 may also reach. I claimed it as `none:DECORATIVE_ONLY` because the question of my unit M2.S9.T9 uses it; at merge, give it the same meaning.
