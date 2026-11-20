# -*- coding: utf-8 -*-
"""Tool specs for T6 and T8 of Class 5 Chapter 8 (Weight and Capacity): Weight Regrouper (adding and subtracting weights by
exchanging 1,000 g and 1 kg) and Scaling Line (cost and the double number line). Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One activity at a
time, one instruction at a time, large controls, Back and Next in the same place, visible progress, Hint, Retry and Reset
always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "weight_regrouper": T(
        "tool_weight_regrouper", "Weight Regrouper", "manipulative",
        "Add and subtract weights in kg and g by exchanging: when the g column reaches 1,000 g the student exchanges 1,000 g "
        "for 1 kg, and when the g on top are fewer the student breaks 1 kg into 1,000 g, so that the carry and the break are "
        "seen and done, not only written.",
        "The grocery counter of Anu's neighbourhood market, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation, with shelves of rice and flour behind it. Two trays sit on the counter, a kg tray on the left and a g tray "
        "on the right, and together they are the largest thing on screen. Each tray holds weight chips: 1 kg bags, 500 g, 250 g "
        "and 100 g packets. Above the trays is a two column sum, kg | g, with the two weights written in it and an empty "
        "result row. An exchange box between the trays shows 1,000 g = 1 kg. An instruction strip at the top shows one sentence "
        "in large type, with progress dots under it. Controls: drag chips into the columns; when the g column reaches 1,000 g "
        "or more the exchange box lights up and the student taps Exchange 1,000 g for 1 kg; for subtracting, tap Break 1 kg "
        "into 1,000 g on the top weight; a mode switch Add, Subtract; type the answer in the kg and g boxes; Check, Hint, "
        "Retry (clears the columns for this card), Reset (restores the trays), Undo, Back and Next in the same places on every "
        "card. Read-outs: the g column total, the kg column total, and a card number out of 6.",
        ["Look at the video's kg | g column sum with a carry. Say what happens to 1,300 g, then "
         "press Next.",
         "Add two weights where no exchange is needed and two where it is, then subtract where no "
         "break is needed and where a break is needed (practice values).",
         "Solve the book's questions on Rathna's rice and on the sand from a sack."],
        ["Card 1 (practice values): add 2 kg 100 g and 1 kg 300 g. Answer: g column 100 + 300 = 400 g, kg column 2 + "
         "1 = 3 kg, so 3 kg 400 g; no exchange is needed because 400 g is less than 1,000 g.",
         "Card 2 (practice values): add 3 kg 600 g and 2 kg 700 g. Answer: g column 600 + 700 = 1,300 g, exchange "
         "1,000 g for 1 kg and write 300 g; kg column 3 + 2 + 1 = 6 kg; so 6 kg 300 g.",
         "Card 3 (practice values): subtract 2 kg 300 g from 6 kg 800 g. Answer: g column 800 − 300 = 500 g, kg "
         "column 6 − 2 = 4 kg, so 4 kg 500 g; no break is needed because 800 g is more than 300 g.",
         "Card 4 (practice values): subtract 2 kg 800 g from 5 kg 200 g. Answer: 200 g is fewer than 800 g, so break "
         "1 kg into 1,000 g; 5 kg 200 g becomes 4 kg 1,200 g; 1,200 − 800 = 400 g and 4 − 2 = 2 kg, so 2 kg 400 g.",
         "Challenge: 'Rathna went to the local grocery store and bought several items. She bought 2 kg 500 g rice for "
         "daily use and 1 kg 750 g additional rice for the upcoming Pongal festival. How much total rice did she buy?' and "
         "'How much extra rice did she buy for household use than for the Pongal festival?' Answer: 4 kg 250 g in all, because "
         "500 + 750 = 1,250 g, exchange 1,000 g for 1 kg, and 2 + 1 + 1 = 4 kg; and 750 g extra, because 2,500 − 1,750 = 750.",
         "Challenge: '4 kg 500 g of sand is used from a sack weighing 10 kg. How much sand is left in the sack?' "
         "Answer: 10 kg is 9 kg 1,000 g after a break, 1,000 − 500 = 500 g and 9 − 4 = 5 kg, so 5 kg 500 g are left."],
        ["When the g column reaches 1,000 g or more the exchange box lights and says so, for example: 1,300 g. Exchange "
         "1,000 g for 1 kg and 300 g are left.",
         "A g column left at 1,250 g with no exchange gets a clue, for example: 1,000 g or more is 1 kg. Exchange first.",
         "When the g on top are fewer, the tool shows the break, for example: 200 g is fewer than 800 g. Break 1 kg into "
         "1,000 g: 1,200 g.",
         "A column answer that takes the smaller number from the bigger in each column gets the other answer, for example: "
         "800 − 200 = 600 g is not the g left. Check by adding back."],
        "All six cards are done, including Rathna's two questions and the sand question, with at least one exchange and one "
        "break done by the student.",
        ["currentCard", "mode", "kgColumn", "gColumn", "exchangeCount", "breakCount", "typedKg", "typedG"],
        ["M_NO_EXCHANGE", "M_SMALL_FROM_BIG"],
        ["Which column do you add or subtract first, the kg or the g? Look at the exchange box.",
         "Is the g column 1,000 g or more? If so, exchange 1,000 g for 1 kg. For a subtraction, are the g on top fewer?",
         "Exchange 1,000 g for 1 kg and carry it to the kg column, or break 1 kg into 1,000 g and add it to the g on top.",
         "Tap the exchange box. The tool moves 1,000 g into 1 kg and shows the new columns."]),

    "scaling_line": T(
        "tool_scaling_line", "Scaling Line", "manipulative",
        "Scale two linked quantities by the same number on a double number line, and find a cost from the cost of 1 kg: "
        "whatever happens to the top line happens to the bottom line, and adding the same number to both lines does not keep "
        "them in step.",
        "The price board of the grocery stall in Anu's neighbourhood market, drawn as a warm 3D isometric scene with soft "
        "shadows and gentle animation. A double number line is painted across the board and is the largest thing on screen: "
        "two rows with equal ticks, a pair of numbers given at the left of each row and a blank at the right (for example "
        "people above and grams below, or kg above and rupees below). Under the board are a price tag and a weighing pan. An "
        "instruction strip at the top shows one sentence in large type, with progress dots under it. Controls: drag the "
        "multiplier arrow along the top row and choose the number (× 2, × 3, × 10) or the divide arrow (÷ 2 for 500 g of 1 kg, "
        "÷ 10 for 100 g of 1 kg); the same arrow then appears on the bottom row; number keys to type the missing value; a Try "
        "adding instead button that adds the same number to both rows and shows that they no longer match; Check, Hint, "
        "Retry (clears this line), Reset (restores all lines), Back and Next in the same places on every card. Read-outs: the "
        "multiplier arrow on each row, the missing value as typed, and a card number out of 7.",
        ["Look at the video's double number line, the pair with an arrow × 3. Say what the "
         "bottom line must do when the top line is multiplied by 3, then press Next.",
         "Scale a line up by a whole number, find a cost from the cost of 1 kg, divide to find the "
         "cost of 1 kg, and try adding instead to see why it fails (practice values).",
         "Complete the book's lines for rice for 8 people, the price of 10 kg of tomatoes, and the scrap "
         "dealer's iron and plastic."],
        ["Card 1 (practice values): 3 plates need 240 g of lentils. How many grams do 9 plates need? Answer: the top "
         "line is × 3 because 3 × 3 = 9, so the bottom line is × 3 too: 240 × 3 = 720 g.",
         "Card 2 (practice values): 1 kg of rice costs ₹36. What do 4 kg 500 g cost? Answer: 4 kg cost 4 × 36 = ₹144, "
         "500 g is half of 1,000 g so it costs 36 ÷ 2 = ₹18, and 144 + 18 = ₹162.",
         "Card 3 (practice values): 6 kg cost ₹90. What does 1 kg cost? Answer: the top line goes ÷ 6 from 6 kg to 1 "
         "kg, so the bottom line goes ÷ 6 too: 90 ÷ 6 = ₹15.",
         "Card 4 (practice values): press Try adding instead on the 3 plates and 240 g line, adding 6 to both. What "
         "do you see? Answer: 9 plates but 246 g, which is far less than 720 g, so adding does not keep the lines in step; "
         "multiply both.",
         "Challenge: '4 people need 500 g rice for a meal. How much rice will be needed for 8 people if they eat "
         "similar quantity of rice?' Answer: 4 to 8 is × 2, so 500 × 2 = 1,000 g, which is 1 kg.",
         "Challenge: '5 kg of tomatoes cost ₹73. How much will 10 kg of tomatoes cost?' Answer: 5 to 10 is × 2, so "
         "73 × 2 = ₹146.",
         "Challenge: 'Nitesh is a scrap dealer. How much would he have paid for (a) 16 kg of old newspaper, if he "
         "paid ₹8 for every 1 kg of newspaper? (b) 20 kg iron, if he paid ₹200 for every 10 kg of iron? (c) 10 kg plastic, if "
         "he paid ₹30 for 5 kg of plastic? Make double number lines for answering (b) and (c).' Answer: (a) 16 × 8 = ₹128; "
         "(b) 10 to 20 is × 2, 200 × 2 = ₹400; (c) 5 to 10 is × 2, 30 × 2 = ₹60."],
        ["When the multiplier arrow is set the same arrow appears on the bottom row and the tool says so, for example: Top line "
         "× 3, so the bottom line × 3.",
         "A bottom value that was found by adding is answered with the check, for example: 3 plates to 9 plates is times 3, not "
         "plus 6. Try × 3 on the bottom line too.",
         "A cost that treats 500 g like 1 kg gets a clue, for example: 500 g is half of 1,000 g, so it costs half of ₹36.",
         "A correct line shows the working in one line, for example: 5 kg to 10 kg is × 2, so ₹73 × 2 = ₹146."],
        "All seven cards are done, including the book's rice, tomatoes and scrap dealer questions, and the student has used a "
        "multiplier and a divider on both rows.",
        ["currentCard", "topRow", "bottomRow", "multiplierArrow", "dividerArrow", "typedValue", "triedAdding"],
        ["M_ADD_TO_SCALE", "M_PART_FULL_PRICE"],
        ["Look at the top line. What happened to the first number to get the second number?",
         "Whatever you do to the top line, do the same to the bottom line. Is it times or plus?",
         "Set the arrow to the number you found on the top line, then use it on the bottom number.",
         "Drag the arrow × 2 onto the top line. The same arrow lands on the bottom line, and the product is shown."]),
}
