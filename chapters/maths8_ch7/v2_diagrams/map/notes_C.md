# Notes for chunk C (Class 8 Ch 7, topics M3.S19.T19 to M5.S31.T31)

Result: 38 items = 1 required, 1 optional, 36 none. Validator: errors 0, warnings 0.
Required: `M5.S31.T31.C120.IMG2` (Binairo worked example). Optional (not added): solution of `M4.S25.T25.C93`.

## 1. Judgement calls

- **Almost everything is none.** Every other pair or worked example in this chunk is a word problem or proportion arithmetic (speed and time, age, ploughing, tea prices, city crowding, sharing in a ratio, paint, idli, crane, coin, manure, land price, unit and temperature conversion). The book prints no figure for any of these questions or for their answers (the "Ans." pages 23 to 30 are text only; I looked at the page pictures). The answers are numbers, amounts or ratios, not drawings.
- **M3.S21.T21.C82 (shampoo worked example): none, LATEX_TABLE.** The book's Activity 2 table is a plain banded table with no colour meaning, and the question sentence already lists the four sizes and prices. `text_alternative` holds the LaTeX array to write if the content team wants the table.
- **M4.S25.T25.C92 / C93 (Activity 3, share 12 in 3 : 1 and 42 in 4 : 3).**
  - Question: none. The question gives no figure. The children-and-seeds picture is an illustration (a heap of 12 seeds, no numbers) and the three pink circles (3 + 9, 8 + 4, 2 + 10) are open examples, not the ratios asked.
  - Solution: **optional**, not added. The book's two flow diagrams (P15 for 12, P16 for 42) are in-chapter teaching figures, and the 42 one already has the teaching image `M4.S24.T24.C88.IMG1`. The LP steps carry every number and the answer is two pairs of numbers, not an arrangement. A single card with both trees side by side (whole 12 -> 3 : 1 x 3 -> 9 : 3, whole 42 -> 4 : 3 x 6 -> 24 : 18) would be the figure to add if the user wants it.
- **M4.S27.T27.C108 (crane).** The book's crane-and-girl picture on p.176 is a joke illustration with no measures on it. Question and solution are none. The picture was missing from the base inventory, so it is added as `NEW-P18-crane-girl` (none, DECORATIVE_ONLY).
- **M4.S29.T29.C115 (manure, plot 200 ft by 500 ft).** none. A rectangle with two side lengths would add nothing the sentence does not already say; the teaching image C114 is not linked.
- **M5.S31.T31.C120 (Binairo): required.** See Borderline.
- **Figure inventory (13 entries).** Items 2 (both book Binairo example grids, mapped to the worked item), concept image 1 (P16, the 42-counter teaching image), none 10 (P13 table LATEX_TABLE; P14 children DECORATIVE_ONLY; P14 pink circles OPEN_ENDED; P15 TEXT_SUFFICIENT; three Binairo practice grids OPEN_ENDED; two blank Dot Grid sheets OPEN_ENDED; the crane picture DECORATIVE_ONLY). I claimed the Dot Grid pages 21 and 22 because they follow the Binairo Puzzle Time page that belongs to my last unit; if another chunk also claims them, give them the same meaning (none:OPEN_ENDED, a blank drawing aid that no question refers to).
- **Base descriptions checked against the pictures.** P13 table, P14 (the circles were re-counted on a zoomed crop: 3 + 9, 8 + 4, 2 + 10 confirmed), P15, P16, P20 (all five grids, cell by cell) and P21 (14 x 22 dots) were right. No "CORRECTED:" entry was needed.
- **Book mistakes (user decision 1):** none found in the figures or printed answers of this chunk. The book's Harmain answer (x years later, x + 1 : x + 5 = 1 : 2, x = 3, age 4) and the LP's (x = her age, x : (x + 4) = 1 : 2, x = 4) reach the same age; the LP is right and was left alone.

## 2. LP text issues

(No LP text was edited and no decision was changed because of these.)

- `M5.S31.T31.C120` (worked example, step 3): "The fourth cell next to a vertical pair would make three verticals if cells 3, 4 and 5 were all vertical" is muddled: cells 3 and 5 are not a pair, cell 4 sits between them. Suggested sentence: "If cell 4 were vertical, cells 3, 4 and 5 would be three verticals in a row, so cell 4 is horizontal."
- `M5.S31.T31.C120` (question): the cells are never numbered, yet steps and answer say "third cell", "cell 4", "cell 6". Suggested addition: "Number the cells 1 to 6 from the left." (The diagram prints position numbers 1 to 6 under the cells for this reason.)
- `M5.S31.T31.C120` (book coverage): the book's Binairo page has a 6 x 6 solved example and three 6 x 6 practice puzzles (P20 grids 3, 4, 5). The LP keeps only a one-row example and its textbook block ends "Solve the following Binairo puzzles." with no puzzle given. Suggested: add the three practice grids as question items (each would be required: DATA_IN_FIGURE and ACTION_ON_FIGURE, with the given cells listed in the inventory descriptions of P20-binairo_grid-3/-4/-5), or drop that sentence.
- `M4.S25.T25.C92` (question) and C93 (steps): the steps say "Partner: 3 x 3 = 9; you: 1 x 3 = 3", but the question never mentions a partner or which share is whose. Suggested sentence: "Share 12 counters between you and your partner in the ratio 3 : 1 (partner : you), and then 42 counters in the ratio 4 : 3."
- Book-number labels differ from the book's own numbering (the LP's own numbering is used for the cards, the `ncert_refs` are right):
  - `M3.S20.T20.C79/C80` "Figure it Out, Q1" is the book's 7.6 Q11 (tractor).
  - `M4.S27.T27.C100/C101` "Figure it Out, Q1" is the book's 7.5 Q2; C102/C103 "Q2" is Q3; C104/C105 "Q3" is Q4; C106/C107 "Q4" is Q5 (the book's 7.5 Q1 is C94 "Ratio Sharing, Q1").
  - `M4.S27.T27.C108/C109` "Figure it Out, Q5" is the book's 7.6 Q4 (crane); C110/C111 "Q6" is Q12 (coin).
  - `M4.S30.T30.C117/C118` "Figure it Out, Q1" is the book's 7.6 Q10 (land price).
  Suggested: label them with the book's numbers (7.5 Q2, Q3, Q4, Q5; 7.6 Q11, Q4, Q12, Q10).
- `M3.S21.T21.C82` (worked example): the book's Activity 2 asks whether price is proportional to volume; the LP question asks "Which size gives the cheapest shampoo per mL?" and the answer says the sachet (about Rs 0.33 per mL) is cheapest. The arithmetic is right (2/6, 154/180, 276/340, 540/1000), only the question differs from the book's. No change needed unless the team wants the book's wording.
- Arithmetic of every pair in the chunk was re-computed and matches the LP text: 100 / 75 = 4/3 h = 1 h 20 min; 20 x 6 = 120 h and 20 x 1.5 = 30 h; 30000000 / 1484 = 20216 and 20000000 / 550 = 36364 (rounded); 12 / 4 = 3 rounds, 42 / 7 = 6; 4500 / 5 = 900; 4000 / 4 = 1000; 5 : 2 :: 30 : 12; 240 / 6 = 40; 40 / 8 = 5 and 15 : 45 = 1 : 3; 3 : 13; 4/10 of 155 = 62; 7.74 x 3 / 4 = 5.805 g, Rs 5.26 + Rs 2.59 = Rs 7.85; 1e9 / 43560 = 22956.8; 3.6e9 / 43560 = 82645.

## Borderline

- **`M5.S31.T31.C120` Binairo worked example, required.** Against: the question describes the row completely in words and the LP answer "H H V H V V" is a text string, so a careful student could solve it from the text alone (tie-breaker). For: the answer is an arrangement of drawn horizontal and vertical bars, rule B2 says an arrangement answer is drawn even when the steps describe it in words, and the steps point at cells by number. I kept it `required` (user decision 4, rules as written). The teaching image C120.IMG1 shows nearly the same row but is kept and never linked, and the id is `C120.IMG2` because IMG1 is kept.
  - Which state the single diagram shows: I drew the **complete final row** (given cells 1, 2, 5 in INK with a dashed FOCUS outline as in the book's solved example, found cells 3, 4, 6 in ANSWER green), because the worked-example figure sits before the steps and the answer is the arrangement. The alternative is the given state only (cells 3, 4, 6 blank), which would not draw the arrangement answer. If the user prefers the given-state row, change the three found cells to blank and drop the ANSWER colour; the id and placement stay the same.
- **`M4.S25.T25.C93` solution, optional rather than none.** The book does draw the method for this very activity (P15, P16), so the figure "would help"; but the steps carry all numbers and the answer is not an arrangement, so it is not required. Nothing is added either way.
- **`M3.S21.T21.C82`, none.** A bar or card picture of price per mL would be pleasant, but the book's figure is a plain table and the teaching image C82.IMG1 already shows the four sizes and the unit prices.
- **Sibling check (B2).** The five 7.5 Figure it Out items (C94, C100, C102, C104, C106) and the Examples 11 and 12 (C96, C98) all have text/number answers and are all none, as is every 7.6 Figure it Out item. No sibling is drawn.
- **P20 Binairo mapping.** Both book example grids (Puzzle and Solution) are mapped to the one worked item because its row is the one-row version of that example. The practice grids are mapped to none:OPEN_ENDED only because no LP item uses them (no code says "no LP item"); see LP text issues.

## 3. Book unclear or odd

- The book's Binairo pages (p.20) show a 6 x 6 solved example, not the one-row example the LP uses; the LP's row (H H _ _ V _ -> H H V H V V) is not printed in the book. It is unique under the book's rules (the other fill, V then H in cells 4 and 6, gives three verticals in cells 3 to 5).
- The book's answer to Figure it Out 7.6 Q4 (crane) gives only "4/10 x your height" with no number, so no figure could carry a value; the LP adds the example 150 cm -> 60 cm.
- The book's Q5 answer in 7.5 (bucket of orange paint) is "3 : 13" with the fractions 3/8 and 13/8; the LP says the same.
- The book's 7.5 Activity 3 pink circles (3 + 9, 8 + 4, 2 + 10) do not show the ratios discussed in the text (6 : 6, 5 : 7, 3 : 1); they only illustrate "different ways".
