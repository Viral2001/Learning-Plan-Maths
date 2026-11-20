# -*- coding: utf-8 -*-
"""Tool specs for T6, T8 and T9 of Class 5 Chapter 6 (The Dairy Farm): Nearest Multiple Grid (Tool 4), Box and Lines
(Tool 5) and Carry Columns (Tool 6). Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One activity at a
time, one instruction at a time, large controls, Back and Next in the same place, visible progress, Hint, Retry and
Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "nearest_multiple_grid": T(
        "tool_nearest_multiple_grid", "Nearest Multiple Grid", "manipulative",
        "See with a tray of squares why rounding one number to a multiple of 10 needs an adjustment: the rounded grid "
        "has a strip of squares that is not really there (take it away) or leaves a strip out (add it), and the strip "
        "has one square in each row.",
        "The packing table of the village dairy, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. A wooden tray of squares sits in the middle and is the largest thing on screen: rows by columns of "
        "equal squares, with the length of a row close to a multiple of 10. Beside the tray stands a friendly number "
        "card, for example 30. An instruction strip at the top shows one sentence in large type, with progress dots "
        "under it. When the number is rounded, a strip of squares appears at the end of every row. It is white with a "
        "dashed edge when the rounded grid counts squares that are not really there, and green when the rounded grid "
        "leaves squares out. Under the tray sit two number boxes for the plan, the rows times the friendly number, then "
        "a minus or plus choice and the strip, and a product box. Controls: a stepper for the number of rows and a "
        "stepper for the length of a row; a Round to the nearest multiple of 10 button; drag the strip away from the "
        "tray and back; a Take away or Add choice; type the plan and the product; Check, Hint, Retry (clears the strip "
        "and the plan of this card), Reset (returns the first grid), Back and Next in the same places on every card. "
        "Read-outs: rows times squares in a row, the nearest multiple of 10, the number of squares in the strip, the "
        "plan as it is typed, and a card number out of 7.",
        ["Look at the tray from the video, 6 rows of 19 squares inside a frame of 6 rows "
         "of 20. Round one number to a multiple of 10 and watch the strip. Press Next.",
         "Build 6 × 29 (practice values) and round 29 to 30: the white strip of 6 squares "
         "appears, and you take it away. Build 13 × 31 (practice values): the green strip of 13 squares appears, and "
         "you add it. Build 7 × 38 (practice values), where the strip has 2 squares in each row, and then choose Take "
         "away or Add for three more grids.",
         "The questions of your maths book. Round 19 to 20 in 4 × 19 and find why we need to "
         "subtract 4. Round 21 to 20 in 14 × 21 and find why we need to add 14. Then find the products of 7 × 52, "
         "12 × 28, 75 × 31, 99 × 15, 8 × 25 and 22 × 42 by finding the nearest multiple."],
        ["Card 1 (practice values): build 6 rows of 29 squares and press Round to the nearest multiple of 10. "
         "Which strip appears, and what is the plan? Answer: 29 rounds to 30, a white strip of 6 squares appears, and "
         "6 × 30 − 6 = 180 − 6 = 174.",
         "Card 2 (practice values): build 13 rows of 31 squares and round. Answer: 31 rounds to 30, a green "
         "strip of 13 squares appears, and 13 × 30 + 13 = 390 + 13 = 403.",
         "Card 3 (practice values): build 7 rows of 38 squares and round. Answer: 38 rounds to 40, and the "
         "white strip has 2 squares in each row, so 7 × 2 = 14 squares are taken away: 7 × 40 − 14 = 280 − 14 = 266.",
         "Card 4 (practice values): three grids are shown, 8 × 49, 11 × 51 and 6 × 99. Choose Take away or "
         "Add for each, then type the plan. Answer: 8 × 49 takes away 8, 8 × 50 − 8 = 400 − 8 = 392. 11 × 51 adds 11, "
         "11 × 50 + 11 = 550 + 11 = 561. 6 × 99 takes away 6, 6 × 100 − 6 = 600 − 6 = 594.",
         "Challenge: 'Find 4 × 19 using the nearest multiple of 10. 4 × 19 = 4 × 20 − 4 = 80 − 4 = 76. "
         "Observe the picture and find why we need to subtract 4.' Round 19 to 20 and watch the white strip. Answer: "
         "the 20th square of every row is counted but is not there. There are 4 rows, so 4 squares are counted by "
         "mistake and we subtract 4: 4 × 19 = 80 − 4 = 76.",
         "Challenge: 'Find 14 × 21 using the nearest multiple of 10. 14 × 21 = 14 × 20 + 14 = 280 + 14 = 294. "
         "Observe the picture and find why we need to add 14.' Round 21 to 20 and watch the green strip. Answer: 14 × 20 "
         "leaves out the 21st square of every row. There are 14 rows, so a green strip of 14 squares is left out and we "
         "add 14: 14 × 21 = 280 + 14 = 294.",
         "Challenge: 'Find the products of the following numbers by finding the nearest multiple.' 7 × 52, "
         "12 × 28, 75 × 31, 99 × 15, 8 × 25, 22 × 42. Answer: 7 × 52 = 350 + 14 = 364; 12 × 28 = 360 − 24 = 336; "
         "75 × 31 = 2,250 + 75 = 2,325; 99 × 15 = 1,500 − 15 = 1,485; 8 × 25 = 240 − 40 = 200; 22 × 42 = 880 + 44 = "
         "924."],
        ["When the number is rounded, the strip appears and the tool names it, for example: 29 is 1 less than 30, so "
         "every row is 1 square short. The white strip has 6 squares, one for each of the 6 rows.",
         "Dragging the strip away from the tray shows what the plan must do: a white strip is taken away, a green strip "
         "is added. The tool says, for example: The 20th square of each row was counted but is not there. 4 rows, so "
         "take away 4.",
         "A plan that uses the wrong strip gets a soft amber note, for example: The strip is 6 squares, not 1. There are "
         "6 rows and each row is 1 square short. The tool says the number of rows only after the second try.",
         "A wrong choice of Take away or Add shows the strip again with a clue: White squares are not really there. "
         "Green squares were left out. Which one is this?",
         "Check compares the product with the plan and says what it found, for example: 6 × 30 − 6 = 174. A correct "
         "card locks in with a soft chime. A wrong answer shows an amber note and never a red cross."],
        "Every grid is rounded and adjusted correctly, the student has chosen Take away or Add for each strip, and the "
        "two pictures and six products of the student's own maths book are done.",
        ["rows", "rowLength", "friendlyNumber", "stripShown", "stripKind", "planChoice", "typedPlan", "challengeIndex"],
        ["M_NO_ADJUST", "M_WRONG_STRIP"],
        ["Which multiple of 10 is nearest to the number in each row?",
         "After you round, is the grid short or too big? White squares are not really there, so take them away. Green "
         "squares were left out, so add them.",
         "Count the squares in the strip. It has one square in each row, so it has as many squares as there are rows.",
         "For 6 × 29 the tool shows the white strip of 6 squares: 6 × 30 = 180, and taking away the strip gives "
         "180 − 6 = 174."]),

    "box_and_lines": T(
        "tool_box_and_lines", "Box and Lines", "manipulative",
        "See that the box, Kanti's four lines and John's two lines are three layouts of the same small products: split "
        "both numbers into tens and ones, find every small product with its zeros, and add them.",
        "The compost pit at the village dairy, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. A wooden notice board stands beside the pit and the working is drawn on it, so the board is the "
        "largest thing on screen. The board holds a box: a top row for the parts of the first number, a left column for "
        "the parts of the second number, one cell for each small product, a row for the column sums and a total cell. "
        "Above the box the two numbers sit as large number cards, and a tray at the side holds product chips, each chip "
        "showing one small product, for example 200. An instruction strip at the top shows one sentence in large type, "
        "with progress dots under it. A switch with three positions, Box, Kanti's lines and John's lines, shows the same "
        "chips in a new layout: four lines in Kanti's layout, two lines in John's layout. Controls: tap a number card to "
        "split it into tens and ones, and into hundreds when it has them; tap a cell and type its product; press Add "
        "to add the column sums and the total; drag a chip into a cell or a line; switch the layout; Check, Hint, "
        "Retry (clears the cells of this card), Reset (clears the box), Back and Next in the same places on every "
        "card. Read-outs: each split number as a sum, for example 20 + 3, the two parts that make the selected cell, "
        "the column sums, the total, and a card number out of 7.",
        ["Look at the box from the video, with 20 and 3 along the top and 10 and 4 down "
         "the side. Split the numbers and fill the box. Press Next.",
         "Build 23 × 14 (practice values) with the parts 20 and 3 against 10 and 4. Fill the "
         "four cells, press Add for the column sums and the total, then switch to Kanti's lines and to John's lines and "
         "watch the same chips move.",
         "The questions of your maths book. 12 × 35 for the kitchen waste of a year and 24 × 150 "
         "for the compost savings. Let Us Multiply with 32 × 8 and 69 × 45. Let Us Do: solve like Nida, like Kanti and "
         "like John."],
        ["Card 1 (practice values): split 23 into 20 + 3 and 14 into 10 + 4, and fill the four cells of the "
         "box. Answer: 10 × 20 = 200, 10 × 3 = 30, 4 × 20 = 80 and 4 × 3 = 12.",
         "Card 2 (practice values): press Add. Which column sums and which total do you get? Answer: the "
         "column of 20 gives 200 + 80 = 280, the column of 3 gives 30 + 12 = 42, and the total is 280 + 42 = 322.",
         "Card 3 (practice values): switch to Kanti's lines, then to John's lines. What stays the same? "
         "Answer: the same four small products. Kanti's four lines are 12 (4 × 3), 80 (4 × 20), 30 (10 × 3) and 200 "
         "(10 × 20), and 12 + 80 + 30 + 200 = 322. John's two lines are 80 + 12 = 92 (4 × 23) and 200 + 30 = 230 "
         "(10 × 23), and 92 + 230 = 322.",
         "Challenge: 'A family of 4 produces around 35 kg of kitchen waste in a month. How much waste will the "
         "family produce in a year? Quantity of kitchen waste in 1 month is 35 kg. Quantity of kitchen waste in 12 "
         "months is 12 × 35 kg.' Build the box, then switch to Kanti's lines and John's lines. Answer: the cells are "
         "300, 50, 60 and 10, the column sums are 360 and 60, and 360 + 60 = 420 kg.",
         "Challenge: 'The family regularly composts the collected waste. They get around 150 kg of compost "
         "each year, which they use in their garden. 1 kg of compost is often sold in the market at ₹24. By creating "
         "their own compost, how much money have they saved in a year?' Savings on 150 kg will be ₹24 × 150. Answer: "
         "the cells are 2,000, 1,000, 400 and 200, the column sums are 2,400 and 1,200, and 2,400 + 1,200 = ₹3,600.",
         "Challenge: Let Us Multiply, 32 × 8 and 69 × 45. Fill each box and complete the lines. Answer: "
         "32 × 8 has the cells 240 and 16 and the total 256. 69 × 45 has the cells 2,400, 360, 300 and 45, the column "
         "sums 2,700 and 405, and the total 3,105.",
         "Challenge: Let Us Do. 'Solve the following problems like Nida did.' 78 × 4, 83 × 9, 67 × 28, 53 × "
         "37. 'Solve the following problems like Kanti.' 94 × 5, 49 × 6, 37 × 53, 28 × 79. 'Solve the following "
         "problems like John.' 86 × 3, 72 × 7, 94 × 36, 66 × 22. Answer: 312, 747, 1,876, 1,961; 470, 294, 1,961, "
         "2,212; 258, 504, 3,384, 1,452."],
        ["A cell that holds the right product lights up and shows how it was made, for example: 10 × 20 = 200. A wrong "
         "product gets a soft amber note, for example: 20 × 3 is 60, not 6. The 2 is 2 tens.",
         "Add shows the column sums one at a time and then the total, for example: 200 + 80 = 280. A sum that does not "
         "match its cells blinks softly in amber.",
         "Switching the layout moves the same chips and the tool says what is the same and what is different: The four "
         "small products are the same. John joins two of them in each line, so he needs two lines.",
         "A missing zero is named: 10 × 20 has 1 ten times 2 tens, which is 2 hundreds, so the product is 200 and not "
         "20.",
         "A wrong answer never shows a red cross. The tool names the product it expected only after the second try."],
        "The box is filled and added for 23 × 14, the same four small products have been seen in Kanti's four lines and "
        "John's two lines, and the questions of the student's own maths book are done.",
        ["firstNumberParts", "secondNumberParts", "cellValues", "columnSums", "total", "layout", "chipPositions",
         "challengeIndex"],
        ["M_MISSING_ZERO", "M_ZERO_COUNT", "M_SPLIT_ONE"],
        ["How many tens and ones does each number have? Split both numbers first.",
         "Which two numbers make this cell? Look at the top of its column and the side of its row, and multiply them.",
         "Keep the zeros: in the cell of 10 and 20, 1 ten times 2 tens is 2 hundreds, so the product is 200.",
         "The tool fills one cell for you: 10 × 20 = 200. Now fill the other three cells the same way."]),

    "carry_columns": T(
        "tool_carry_columns", "Carry Columns", "manipulative",
        "Multiply place by place from the ones, write each carry above the next place, and add it only after "
        "multiplying that place, so that every carry goes to the right place at the right time.",
        "The office desk of the dairy cooperative, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. A large ledger lies open on the desk and is the largest thing on screen. It has columns for ten "
        "thousands, thousands, hundreds, tens and ones. The first number sits in the middle of the ledger with a carry "
        "circle above each column, the second number is below it with the multiplication sign, and under a line are "
        "empty boxes for one row for each digit of the second number, with a 0 or 00 already printed at the end of the "
        "tens and hundreds rows, and a total row at the bottom. A pointer arrow steps column by column, starting at the "
        "ones. An instruction strip at the top shows one sentence in large type, with progress dots under it. "
        "Controls: move the pointer to a column; type the digit to write and the carry; drag the carry into the circle "
        "of the next column; press Add rows; Check, Hint, Retry (clears the rows of this question), Reset (clears the "
        "ledger), Back and Next in the same places on every card. Read-outs: the multiplication at the pointer, for "
        "example 4 × 6 = 24, the carry that is waiting, the sum with the carry, and a card number out of 7.",
        ["Look at the ledger from the video, 176 × 24 with its carry circles. Multiply "
         "one column and write the carry above the next column. Press Next.",
         "Multiply 235 × 4 (practice values) column by column and write each carry. Then "
         "multiply 68 × 4 (practice values) and drag the carry to the right circle. Then fill the two rows of 176 × 24 "
         "(practice values) and add them.",
         "The questions of your maths book. 268 × 4 for the cows of the cooperative, 453 × 13 for "
         "the milk of the Gir cows, and 574 × 125 for the ghee. Then solve like Mili's father: 806 × 9, 455 × 26 and "
         "143 × 208."],
        ["Card 1 (practice values): multiply 235 × 4. Move the pointer to the ones, the tens and the hundreds. "
         "Answer: ones 4 × 5 = 20, write 0, carry 2. Tens 4 × 3 = 12, and 12 + 2 = 14, write 4, carry 1. Hundreds "
         "4 × 2 = 8, and 8 + 1 = 9. So 235 × 4 = 940.",
         "Card 2 (practice values): multiply 68 × 4 and drag the carry to its circle. When is the carry "
         "added? Answer: 4 × 8 = 32, write 2, carry 3 above the tens. Then 4 × 6 = 24, and the carry is added after "
         "that: 24 + 3 = 27. So 68 × 4 = 272. The 3 is not added to the 6 before multiplying.",
         "Card 3 (practice values): fill the two rows of 176 × 24 and press Add rows. Answer: row 1 is "
         "4 × 176 = 704, row 2 is 20 × 176 = 3,520 with the 0 already placed, and 704 + 3,520 = 4,224.",
         "Challenge: 'A dairy cooperative in a small town gets its milk from 268 villagers. Each villager has "
         "at least 4 milk-giving cows. What is the minimum number of cows the dairy cooperative gets its milk from? 1 "
         "villager has at least 4 milk-giving cows. 268 villagers will have at least 268 × 4 cows.' Answer: 4 × 8 = 32, "
         "write 2, carry 3. 4 × 6 = 24, and 24 + 3 = 27, write 7, carry 2. 4 × 2 = 8, and 8 + 2 = 10. So 268 × 4 = "
         "1,072 cows.",
         "Challenge: 'The villagers rear various breeds of cows. Gir is an Indian cow breed from Gujarat, with "
         "a high milk-producing capacity. Among the villagers, there are 453 Gir cows. Each of these cows give 13 litres "
         "of milk each day. How many litres of milk does the dairy cooperative receive from Gir cows everyday? One Gir "
         "cow produces 13 litres of milk. 453 Gir cows will produce 453 × 13 litres of milk.' Answer: row 1 is "
         "3 × 453 = 1,359, row 2 is 10 × 453 = 4,530, and 1,359 + 4,530 = 5,889 litres.",
         "Challenge: 'The dairy cooperative sells 1 kg cow ghee for ₹574. The cooperative is able to produce "
         "around 125 kg of ghee in a month. How much do they earn by selling ghee in a month?' Answer: the rows are "
         "2,870, 11,480 and 57,400, and 2,870 + 11,480 + 57,400 = ₹71,750.",
         "Challenge: 'Let us solve a few questions like Mili's father.' 806 × 9, 455 × 26 and 143 × 208. "
         "Answer: 806 × 9 = 7,254; 455 × 26 = 2,730 + 9,100 = 11,830; 143 × 208 = 1,144 + 0 + 28,600 = 29,744."],
        ["The pointer shows the multiplication of its column and waits for the digit and the carry, for example: 4 × 6 "
         "= 24. Write 4 and carry 2. A correct digit locks in with a soft chime and the carry hops to the circle of the "
         "next column.",
         "When the carry is added at the wrong time, the tool says: 30 from 32 is added to 4 × 60, not to 60. Multiply "
         "the column first, then add the carry.",
         "A carry dropped in the wrong circle slides back with a clue: The carry goes above the next column to the "
         "left.",
         "A tens or hundreds row without its 0 or 00 is named: This row is for tens, so it starts with a 0. Without it "
         "the product is 10 times too small.",
         "Add rows shows each row and the total. A wrong total shows an amber note and never a red cross, and the tool "
         "names the digit it expected only after the second try."],
        "Every column of every card has its digit and carry in the right place, the rows are added, and the questions of "
        "the student's own maths book are done.",
        ["pointerColumn", "digitsWritten", "carries", "carryCircles", "rows", "total", "challengeIndex"],
        ["M_CARRY_FIRST", "M_MISSING_ZERO"],
        ["Which column is the pointer on? Multiply its digit by the digit of the number below.",
         "Multiply the column first, then add the carry that came from the column to the right.",
         "Write only the last digit of the answer in the column. The other digit is the carry for the next column.",
         "For 4 × 6 with a carry of 3: 4 × 6 = 24, and 24 + 3 = 27. The tool writes 7 and puts the carry 2 above the "
         "next column."]),
}
