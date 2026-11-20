# -*- coding: utf-8 -*-
"""Tool specs for T5, T6 and T7 of Class 5 Chapter 5 (Far and Near): Millimetre Ruler, Double Number Line and Length
Columns. Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One activity at a
time, one instruction at a time, large controls, Back and Next in the same place, visible progress, Hint, Retry and
Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "millimetre_ruler": T(
        "tool_millimetre_ruler", "Millimetre Ruler", "manipulative",
        "Read and draw lengths in cm and mm using the small marks of a ruler: a length is the cm mark before its end "
        "plus the number of small marks after it, and 1 cm = 10 mm.",
        "The ruler desk of the village weaving centre, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. A big yellow ruler, the largest object on screen, is marked in cm with 10 equal parts in every cm: "
        "the cm marks are long and numbered, the 5 mm marks are medium and the other marks are short, so there are 9 "
        "small marks between two cm marks. A zoom lens on a handle magnifies the centimetre it covers. A line lies on "
        "the ruler with a draggable end point that snaps to each mm mark, and objects to measure (a sprout, a small "
        "screw and a nail, with practice lengths) lie beside the ruler. A read-out shows the length in two forms, for "
        "example 4 cm 6 mm = 46 mm. The design of four nested shapes in your maths book can be placed on the desk with "
        "its eight lines, each line with a box for cm and mm. An instruction strip at the top shows one sentence in "
        "large type with progress dots under it. Controls: drag the end of the line along the ruler; tap the lens to "
        "zoom; type into the cm box and the mm box; drag the ruler along a line of the design; Check, Hint, Retry "
        "(clears the line of this card), Reset (restores the ruler and the objects), Back and Next in the same places "
        "on every card. Read-outs: the length in cm and mm, the length in mm, and a card number out of 7.",
        ["Look at the video's ruler with the lens on 1 cm, cut into 10 equal parts. Count "
         "the small marks between two cm marks, then press Next.",
         "Read the length of a sprout and a screw on the ruler in cm and mm, drag the end of a "
         "line to draw a given length, and write each length in mm only.",
         "Do your maths book's own tasks: count the small marks between 1 cm and 2 cm, measure the "
         "eight lines of the design in cm and mm, and draw lines of 5 cm 5 mm, 3 cm 6 mm, 8 cm 3 mm, 36 mm and 67 mm."],
        ["Card 1 (practice values): the sprout ends on the 4th small mark after the 2 cm mark. Read its length. "
         "Answer: 2 cm 4 mm = 2 × 10 + 4 = 24 mm.",
         "Card 2 (practice values): the screw ends on the 9th small mark after the 3 cm mark. Read its length. "
         "Answer: 3 cm 9 mm = 3 × 10 + 9 = 39 mm.",
         "Card 3 (practice values): drag the end of a line to draw 4 cm 6 mm, then write it in mm. Answer: "
         "4 × 10 + 6 = 46 mm.",
         "Card 4 (practice values): drag the end of a line to draw 72 mm and write it in cm and mm. Answer: "
         "72 mm = 70 mm + 2 mm = 7 cm 2 mm.",
         "Card 5 (practice values): a nail is 2 cm 8 mm long and a bead is 25 mm long. Which is longer, and by "
         "how much? Answer: 2 cm 8 mm = 28 mm and 28 − 25 = 3 mm, so the nail is longer by 3 mm.",
         "Challenge: 'Let us look at the scale. Do you notice the small marks between 1 cm and 2 cm? Count how "
         "many marks there are between 1 cm and 2 cm.' Then: 'Measure the lines in the design and write their "
         "measurements in cm and mm.' Answer: 9 small marks; the eight lines measure 48 mm, 35 mm, 60 mm, 27 mm, 22 mm, "
         "19 mm, 44 mm and 61 mm, which are 4 cm 8 mm, 3 cm 5 mm, 6 cm, 2 cm 7 mm, 2 cm 2 mm, 1 cm 9 mm, 4 cm 4 mm and "
         "6 cm 1 mm. A ruler may read 1 mm different.",
         "Challenge: 'Draw lines of the following lengths in your notebook using a scale.' 5 cm 5 mm, 3 cm "
         "6 mm, 8 cm 3 mm, 36 mm and 67 mm. Answer: 55 mm, 36 mm, 83 mm, 3 cm 6 mm and 6 cm 7 mm. The sprout diary needs "
         "real seeds and is done at home."],
        ["The end point snaps to the nearest mm mark and the read-out says the length, for example: 4 cm and 6 small "
         "marks, 4 cm 6 mm, which is 46 mm.",
         "If the student reads only the cm mark, the tool says: The line goes past the 4 cm mark. Count the small marks "
         "after it.",
         "The lens makes the small marks big so that they can be counted one by one, and the counted marks light up in "
         "turn.",
         "A wrong mm number slides back with a clue such as: Each small mark is 1 mm. Count again from the cm mark.",
         "In the design, the ruler lays itself along the chosen line and the tool says the length only after the "
         "student has typed a reading."],
        "All five practice cards are solved, the small marks are counted, the eight lines of the design are measured and "
        "the five lines are drawn.",
        ["lineEnd", "lensOn", "readingCm", "readingMm", "objectIndex", "designLine", "challengeIndex"],
        ["M_CM_HUNDRED_MM"],
        ["Which centimetre mark is just before the end of the line?",
         "Count the small marks after that centimetre mark. Each small mark is 1 mm.",
         "Write the cm and the mm. In mm only, the cm are multiplied by 10 and the mm are added.",
         "The tool puts the end point on the right mark and shows the length in cm and mm and in mm."]),

    "double_number_line": T(
        "tool_double_number_line", "Double Number Line", "manipulative",
        "Change a length from one unit to another with the multipliers 10, 100 and 1,000 on two linked number lines, and "
        "split a length into a part in the bigger unit and a rest in the smaller unit.",
        "A pair of tapes on the weaving centre wall, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation: the top tape in the bigger unit and the bottom tape in the smaller unit, with their ticks lined up "
        "one under the other. The two lines are the largest object on screen. A draggable pointer moves along both tapes "
        "together, so one tick shows the same length in two units. A unit switch picks cm over mm, m over cm or km over "
        "m. Multiplier boxes sit on the arrows between the tapes (for example ×10 from the top tape down to the bottom "
        "tape) and take a number. Tick labels may be blank for the student to fill in. Under the tapes a split tray cuts "
        "a length such as 5,792 cm into a part that is whole metres (5,700 cm) and a rest (92 cm), and joins them as "
        "57 m 92 cm. An instruction strip at the top shows one sentence in large type with progress dots under it. "
        "Controls: drag the pointer; tap a blank label and type a number; tap a multiplier box and type; drag the split "
        "mark in the tray; Check, Hint, Retry (clears the blanks of this card), Reset (restores the lines), Back and "
        "Next in the same places on every card. Read-outs: the same length on both tapes, the multiplier used, the split "
        "parts, and a card number out of 7.",
        ["Look at the video's picture of 1 cm over 10 mm with the arrow ×10. Say how many "
         "mm are in 1 cm, then press Next.",
         "Slide the pointer and read the same length on both tapes, switch between the unit "
         "pairs, fill in blanks and multiplier boxes, and split a length into two units.",
         "Fill in your maths book's own three number lines with their blanks and multiplier boxes, "
         "and the conversions (a) to (n)."],
        ["Card 1 (practice values): cm over mm. Slide the pointer to 6 cm and read the mm. Answer: 6 × 10 = 60 "
         "mm.",
         "Card 2 (practice values): m over cm. Slide the pointer to 4 m and read the cm. Answer: 4 × 100 = 400 "
         "cm.",
         "Card 3 (practice values): km over m. Slide the pointer to 5 km and read the m. Answer: 5 × 1,000 = "
         "5,000 m.",
         "Card 4 (practice values): type the multiplier for the ticks 8 cm over 80 mm. Answer: ×10, because 8 × "
         "10 = 80.",
         "Card 5 (practice values): use the split tray on 4,205 cm. Answer: 4,205 cm = 4,200 cm + 5 cm = 42 m "
         "5 cm.",
         "Challenge: 'Fill in the blanks appropriately in the double number lines.' Line (a): cm over mm, top "
         "1 cm, 7 cm, 15 cm, three blanks, 50 cm, bottom 10 mm, two blanks, 250 mm, 320 mm, 450 mm and a blank, with ×7 "
         "and ×10. Line (b): m over cm, top 1 m, 4 m, 10 m, three blanks, 21 m, bottom three blanks, 1,200 cm, 1,400 cm, "
         "1,700 cm and a blank, with ×4 and ×100. Line (c): km over m, top 1 km, 9 km, 25 km, three blanks, 82 km, "
         "bottom 1,000 m, two blanks, 41,000 m, 55,000 m, 67,000 m and a blank, with ×9 and ×1,000. Answer: (a) 25 cm, "
         "32 cm, 45 cm and 70 mm, 150 mm, 500 mm, the boxes ×7 and ×10; (b) 12 m, 14 m, 17 m and 100 cm, 400 cm, "
         "1,000 cm, 2,100 cm, the boxes ×4 and ×100; (c) 41 km, 55 km, 67 km and 9,000 m, 25,000 m, 82,000 m, the boxes "
         "×9 and ×1,000.",
         "Challenge: 'Use your understanding from above to fill in the blanks appropriately.' (a) 4 cm 5 mm = "
         "___ mm; (b) 89 mm = ___ cm ___ mm; (c) 234 cm = ___ mm; (d) 514 mm = ___ cm ___ mm; (e) 6 m 34 cm = ___ cm; (f) "
         "20 m 12 cm = ___ cm; (g) 397 m = ___ cm; (h) 5,792 cm = ___ m ___ cm; (i) 9,108 cm = ___ m ___ cm; (j) 34 km = "
         "___ m; (k) 6,870 m = ___ km ___ m; (l) 10,552 m = ___ km ___ m; (m) 29 km 30 m = ___ m; (n) 32 km 359 m = ___ "
         "m. Answer: (a) 45 mm; (b) 8 cm 9 mm; (c) 2,340 mm; (d) 51 cm 4 mm; (e) 634 cm; (f) 2,012 cm; (g) 39,700 cm; "
         "(h) 57 m 92 cm; (i) 91 m 8 cm; (j) 34,000 m; (k) 6 km 870 m; (l) 10 km 552 m; (m) 29,030 m; (n) 32,359 m."],
        ["The pointer moves on both tapes at once and the read-out shows both numbers with their units and the "
         "multiplier, for example: 6 cm is 6 × 10 = 60 mm.",
         "A blank label accepts only the number that belongs to that tick. A wrong number slides back with a clue such "
         "as: Going down the multiplier is 10, so multiply the top number by 10.",
         "A multiplier box is checked against the two numbers above and below it, and the tool says, for example: ×10 is "
         "right because 7 × 10 = 70.",
         "In the split tray the part in the bigger unit and the rest are shown in two colours, and the tool says: 5,700 "
         "cm is 57 m, and 92 cm are left, so 57 m 92 cm.",
         "In the conversion tasks the tool says whether the answer is right and gives a clue; it never fills the answer "
         "in before the third hint."],
        "All five practice cards are solved, the three number lines are filled in, and the fourteen conversions are "
        "answered.",
        ["unitPair", "pointerValue", "blankValues", "multiplierBoxes", "splitMark", "challengeIndex"],
        ["M_M_TEN_CM", "M_KM_HUNDRED", "M_CM_HUNDRED_MM", "M_JOIN_NUMBERS"],
        ["Which unit is on the top tape and which is on the bottom tape? Which one is bigger?",
         "Going down from the bigger unit to the smaller unit you multiply. By which number: 10, 100 or 1,000?",
         "Multiply the top number by that multiplier to get the bottom number. To go up, divide.",
         "The tool slides the pointer to the tick and shows both numbers and the multiplier."]),

    "length_columns": T(
        "tool_length_columns", "Length Columns", "manipulative",
        "Add and subtract lengths given in two units in a column for each unit, with exchange chips for regrouping: "
        "1 km = 1,000 m and 1 m = 100 cm.",
        "The cutting table of the village weaving centre, drawn as a warm 3D isometric scene with soft shadows and "
        "gentle animation, with a chart of two columns on the wall. The chart is the largest object on screen: columns "
        "headed km and m (or m and cm), rows for the first length, the second length and the answer, and a plus or "
        "minus sign on the left. Number tiles sit in the cells. Exchange chips wait beside the chart: a chip marked 1 km "
        "turns into 1,000 m and back, and a chip marked 1 m turns into 100 cm and back. A check strip below changes the "
        "whole sum to the smaller unit as a second way. An instruction strip at the top shows one sentence in large type "
        "with progress dots under it. Controls: tap a cell and type a number; drag an exchange chip across a column "
        "border; tap Add or Subtract; Check, Hint, Retry (clears the cells of this card), Reset (restores the table), "
        "Back and Next in the same places on every card. Read-outs: the sum in the smaller unit, the carried or exchanged "
        "amount, and a card number out of 7.",
        ["Look at the video's table with two lengths, one unit in each column. Put each "
         "length in its columns, then press Next.",
         "Add lengths, carry a full bigger unit with an exchange chip, subtract by exchanging "
         "one bigger unit for the smaller unit, and check each answer by changing to the smaller unit.",
         "Work your maths book's own examples and questions: Saji's walk, the electricians' cable, "
         "Rani's ribbons, Bhopal to Sanchi, Gulmarg Gondola, and the seven pairs where the bigger length and the "
         "difference are asked."],
        ["Card 1 (practice values): add 2 km 900 m and 1 km 800 m in the km and m columns. Answer: 900 m + "
         "800 m = 1,700 m, carry 1 km and write 700 m, and 2 km + 1 km + 1 km = 4 km, so 4 km 700 m.",
         "Card 2 (practice values): add 5 m 60 cm and 3 m 70 cm in the m and cm columns. Answer: 60 cm + 70 cm "
         "= 130 cm, carry 1 m and write 30 cm, and 5 m + 3 m + 1 m = 9 m, so 9 m 30 cm.",
         "Card 3 (practice values): subtract 3 m 40 cm from 9 m. Answer: exchange 1 m for 100 cm, so 9 m "
         "becomes 8 m 100 cm, and 8 m 100 cm − 3 m 40 cm = 5 m 60 cm.",
         "Card 4 (practice values): subtract 2 km 600 m from 5 km 200 m. Answer: exchange 1 km for 1,000 m, so "
         "5 km 200 m becomes 4 km 1,200 m, and 4 km 1,200 m − 2 km 600 m = 2 km 600 m.",
         "Card 5: check card 4 by changing to m. Answer: 5,200 − 2,600 = 2,600 m = 2 km 600 m.",
         "Challenge: 'Saji saw on his smartphone that he walked 3 km 450 m in the morning and another 4 km 650 "
         "m in the evening. How much did he walk in the whole day?' and 'They need 63 m of cable for this purpose. They "
         "used 16 m 75 cm cable in the first room. What is the length of the cable left?' Answer: 8 km 100 m, and 46 m "
         "25 cm.",
         "Challenge: 'Rani has two red coloured ribbon rolls, one of length 3 m 75 cm and another 2 m 25 cm "
         "long. How much ribbon does she have?'; 'The distance from Bhopal to Sanchi is 48 km 700 m ... 17 km 900 m "
         "away from Bhopal. How far is Sanchi from the waterfall?'; 'The first section covers 2 km 300 m and the second "
         "section covers 2 km 650 m'; and 'Circle the bigger length and find the difference' for the seven pairs. "
         "Answer: 6 m; 30 km 800 m; 4 km 950 m; and the pairs: (a) 11 mm, 1 mm; (b) 26 mm, 6 mm; (c) 201 mm, 1 mm; (d) "
         "1,020 mm, 20 mm; (e) 245 cm, 45 cm; (f) 6 km, 322 m; (g) 6 km 1,480 m, 1 m."],
        ["Typing in a cell shows the number in its column. If a cell holds more than a full bigger unit, the tool says, "
         "for example: 1,700 m is more than 1,000 m, so exchange 1,000 m for 1 km.",
         "An exchange chip moves across the column border and the numbers change together, for example 1 km becomes "
         "1,000 m.",
         "In a subtraction, if the bottom number is bigger than the top number in a column, the tool says: You cannot "
         "take 40 cm from 0 cm. Exchange 1 m for 100 cm first.",
         "The check strip changes the whole sum to the smaller unit and shows that both ways give the same length.",
         "A wrong answer slides back with a clue such as: Did you exchange 1 m as 100 cm and not as 10 cm?"],
        "All five practice cards are solved, the two examples are worked, and the three word problems and the seven pairs "
        "are answered.",
        ["columns", "cellValues", "chipsUsed", "operation", "checkStripOn", "challengeIndex"],
        ["M_ADD_ALL", "M_BORROW_TEN"],
        ["Which two units are in the table? Put each length into its own columns.",
         "Start with the smaller unit. Can the answer in that column be changed to a bigger unit?",
         "1 km = 1,000 m and 1 m = 100 cm. Exchange one bigger unit for the smaller unit when you subtract, or carry it "
         "when you add.",
         "The tool does the exchange with the chip and shows the new numbers in both columns."]),
}
