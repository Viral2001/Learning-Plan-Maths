# Chunk B notes - Class 5 Ch 8 "Weight and Capacity"

Topics M2.S13.T13 to M2.S17.T17 (units 19-30, book pages 5-8). 22 items: required 4 / optional 0 / none 18. Validator: errors 0, warnings 0.

| Unit | Concept(s) | Question | Solution |
|---|---|---|---|
| 19 | C35 / C36 sugar sachet | none | none |
| 20 | C37 / C38 double number line (mg / g) | REQUIRED `C37.IMG1` | REQUIRED `C38.IMG1` (derived from C37.IMG1) |
| 21 | C39 / C40 goldsmith 10 g 500 mg | none | none |
| 22 | C41 / C42 compare g and mg | none | none |
| 23 | C43 / C44 elephant x 40 whale | REQUIRED `C43.IMG1` | REQUIRED `C44.IMG1` (derived from C43.IMG1) |
| 24 | C45 / C46 kg, quintal, tonne | none | none |
| 25 | C47 / C48 Example 3 ornament | none | none |
| 26 | C49 / C50 King's Weight | none | none |
| 27 | C51 worked, adding weights | none (worked) | |
| 28 | C52 worked, subtracting weights | none (worked) | |
| 29 | C54 / C55 Example 4 rice total | none | none |
| 30 | C56 / C57 Example 5 extra rice | none | none |

Figure inventory: 16 entries (13 base + 3 `NEW-`): 4 mapped to items, 1 to a concept image, 11 to `none:` codes.

## 1. Judgement calls

- **C37 / C38 (double number line), required both sides.** The question says "below", the whole figure is data (which ticks carry which values, where the 4 blanks are) and the learner completes it. The solution is the completed line (B2, ANSWER_IS_FIGURE). Ticks are drawn exactly in proportion to the gram values (x = 0.08 + 0.84 x (g - 1) / 30); the book's ticks are only roughly to scale. The first top label is printed "1000 mg" in the book (no comma, while the rest of that line has commas); I drew "1,000 mg" to match the line and the LP. No arrows are drawn (the book has none). Answers: 5,000 mg, 20 g, 25,000 mg, 31 g (all checked: mg = 1,000 x g on every tick).
- **C43 / C44 (elephant and whale), required both sides.** The book question is "Observe the pictures given below" (FIG_REFERENCED); the 5,000 kg, the x 40 arrow and the blank sit in the picture. The animals are decoration, so the diagram is two captioned boxes ("Elephant", "Whale") with the curved x 40 arrow, no clip-art. The solution fills the whale box with 200,000 kg (5,000 x 40; 200,000 / 40 = 5,000), ACTION_ON_FIGURE, derived from the question figure. See Borderline.
- **Compare tables (C41 / C42).** The book's pink panel is a plain 3-column table, so `LATEX_TABLE`. The solution is six signs plus conversions: kept `none` (a filled plain table of signs is LaTeX, not a diagram). Chunk A's "Comparison between Different Weights" Q2 (cmp1.signs) is the same kind of item and should get the same decision; I did not read it.
- **Column addition and subtraction (C51, C52, C55, C57; base figures P07-column_addition-1/2, P08-column_subtraction-1/2).** v3 Step C lists column addition and subtraction as `LATEX_ARITHMETIC`. The LP steps name every carry and borrow in words, and the T17 solutions do not even use the book's carry-arrow layout (they add kg and g separately, or convert to grams). The kept teaching images C51.IMG1 and C52.IMG1 were not a reason for the decision (user decision 5); the reason is the arithmetic rule. Each item has a `text_alternative` for the LaTeX array.
- **Dialogue bubbles (P05-dialogue-2, P07-dialogue-1, P08-dialogue-1).** Text in a speech bubble with a character: `none:TEXT_SUFFICIENT`. P05-dialogue-2 is also listed in chunk A's T12 refs (`mg.similar`); if A maps it differently, the merge should compare (both are "no diagram").
- **P06-unit_facts-1 ("Did you know?")** is claimed by me as `concept_image:M2.S12.T12.C32.IMG1` because C45 / C46 (Let Us Find Q6) use its facts, and it is also a chunk A figure (`qt.know`). Same meaning in both chunks is expected. P07-table-1 ("From Tiny to Big") is not used by any chunk B unit, so I left it to chunk A (`units.table`).
- **NEW-P05-sachet.** The sugar sachet "SUGAR 5g" beside Let Us Find 1-2 is not in the base inventory; added as `none:DECORATIVE_ONLY` (the 5 g is in the question text).
- **NEW-...-sol figures.** The completed double number line and the completed whale figure are second uses of base figures (the book prints no solutions), so each has its own `NEW-<base id>-sol` entry mapped to the solution item.
- **C47 / C48 (Example 3 ornament).** In the book this is Let Us Find Q3: a bubble with the worked line (4 g = 4,000 mg ...) and a precision balance whose display is unreadable. None.

## 2. LP text issues

- **M2.S13.T13.C37** (question): "Complete the double number line below appropriately." carries no data; everything is in the figure. Fine once the diagram is placed (it is required). If the diagram were ever missing, suggested text: "Complete the double number line. 1 g is 1,000 mg, 12 g is 12,000 mg and the 20,000 mg, 25 g and 31,000 mg marks are given. Find the mg at 5 g, the g at 20,000 mg, the mg at 25 g and the g at 31,000 mg."
- **M2.S13.T13.C43** (question): the text still starts "Observe the pictures given below", then narrates the picture. With the diagram this reads well; without it the lead-in would point at nothing. No change needed with the diagram.
- **M2.S13.T13.C39 ... C45 and M2.S14.T14.C47 (numbering vs the book):** LP "Let Us Find: Q3" (C39, goldsmith) is book Let Us Find Q4; LP Q4 (compare) is book Q5; LP Q5 (whale) is book Q6; LP Q6 (quintals) is book Q7; and the LP's "Example 3: the ornament" (C47) is book Let Us Find Q3. Suggested `book_number` labels: C39 "Let Us Find 4", C41 "Let Us Find 5", C43 "Let Us Find 6", C45 "Let Us Find 7", C47 "Let Us Find 3".
- **M2.S17.T17.C54:** "bought several items" is in the book text too; the question only asks about rice. No change needed.
- **M2.S17.T17.C56** (Example 5 question): "How much extra rice did she buy for household use than for the Pongal festival?" has no numbers of its own; they come from Example 4 (2 kg 500 g and 1 kg 750 g) and appear only in the solution. Suggested sentence: "Rathna bought 2 kg 500 g rice for daily use and 1 kg 750 g for the Pongal festival. How much extra rice did she buy for household use than for the Pongal festival?"
- **M2.S16.T16.C51 / C52:** the practice values (3 kg 600 g + 2 kg 700 g; 5 kg 200 g - 2 kg 800 g) differ from the book's Grocery Store numbers (2 kg 500 g and 1 kg 750 g), as the text says ("These are practice values"). Not an error.
- **M2.S13.T13.C46:** answer says "5 tonne" (singular), following the book's blank "_____ tonne". Consistent with the book; plural "tonnes" is used for 8.

All LP arithmetic in chunk B was recomputed and is correct (C36, C38, C40, C42 a-f, C44, C46, C48, C50, C51, C52, C55, C57).

## 3. Borderline

- **C43 / C44 elephant and whale:** the LP question text already states 5,000 kg and x 40, so a careful student could solve it from text. Kept `required` because the book question is "Observe the pictures", the figure holds the data, and the text still points at the picture (user decision 4: do not flip only because the LP text carries the numbers). The solution side is "complete the blank in the figure"; it adds only one value, so it could be argued `none` (SAME_AS_QUESTION_DIAGRAM). Kept `required` for the Act-on-figure pair (Q required, S required) and to match C37 / C38.
- **C49 / C50 King's Weight picture:** a balance with the king against 10 sacks illustrates "10 times his weight". Judged `DECORATIVE_ONLY` (no numbers in the picture, relation stated in words). A balance figure would be nice but is not needed.
- **C41 / C42 compare:** question `LATEX_TABLE`, solution `none`; a filled table of signs could be read as a "filled figure" under B2, but plain tables stay LaTeX.
- **C51, C52, C55, C57 column work:** `none` under `LATEX_ARITHMETIC` even though the book draws carries and borrows with circles and arrows (HIGHLIGHT_MEANING could be argued). Reason: the LP text spells out each carry and borrow, and LaTeX arrays can show kg | g columns.
- **C35 / C39 / C47 pictures (sachet, precision balance):** decorative, numbers in the text.

## 4. Where the book itself is unclear

- Let Us Find 2: top first label "1000 mg" has no comma; tick spacing is only roughly proportional.
- Example 4 bubble: "So, total rice bought is 4 kg 250." has no unit after 250 (a print slip; the LP says 4 kg 250 g). No diagram uses it.
- Column addition answer row prints "4 [1] 2 5 0" with the carried 1 boxed and crossed; the true answer is 4 kg 250 g (diagram not drawn, so no correction needed).
- King's balance: the beam is not level, so the picture is only a hint of "10 times".
- Precision balance display on page 5 is unreadable.
- No solutions section in this pdf; the LP solution text is the answer used everywhere.
