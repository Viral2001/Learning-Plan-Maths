# -*- coding: utf-8 -*-
"""Tool specs for T8 and T10 of Class 5 Chapter 5 (Far and Near): Cut and Share and Height Chart. Specs only; the tool
pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One activity at a
time, one instruction at a time, large controls, Back and Next in the same place, visible progress, Hint, Retry and
Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "cut_and_share": T(
        "tool_cut_and_share", "Cut and Share", "manipulative",
        "Multiply and divide a length given in two units by working on each unit and then regrouping: copies of a length "
        "laid end to end give so many m and so many cm, and a road shared into equal days gives each day its km and m.",
        "The cutting table of the village weaving centre with a roll of cloth and a road strip beside it, drawn as a warm "
        "3D isometric scene with soft shadows and gentle animation. A strip of cloth of a chosen length in m and cm lies "
        "on a tape, and it is the largest object on screen. A Make copies stepper lays copies of the strip end to end "
        "along the tape, and two piles collect the parts: a m pile and a cm pile. An exchange chip turns 100 cm into "
        "1 m. For division, a road bar of a chosen length in km and m has a Share into stepper that fills equal day "
        "boxes, each with a km part and a m part, and a leftover chip turns 1 km into 1,000 m when the km do not share "
        "equally. An instruction strip at the top shows one sentence in large type with progress dots under it. "
        "Controls: the Make copies stepper; drag the parts of a strip into the m pile and the cm pile; tap the exchange "
        "chip; the Share into stepper; type an answer into a box; Check, Hint, Retry (clears the piles of this card), "
        "Reset (restores the roll and the road), Back and Next in the same places on every card. Read-outs: the number "
        "of copies, the m pile and the cm pile, the total after the exchange, and a card number out of 7.",
        ["Look at the video's picture of curtain strips of 2 m 40 cm laid end to end. Say "
         "which two parts you will multiply, the m and the cm, then press Next.",
         "Lay copies of a strip end to end, sort the m and the cm into their piles, exchange "
         "100 cm for 1 m, and share a road into equal days with a km part and a m part.",
         "Answer your maths book's own questions: the shirts for 20 children, Anita's thread and "
         "its cost, and the road laid in 6 equal days."],
        ["Card 1 (practice values): lay 5 copies of a strip of 3 m 20 cm and sort the parts. Answer: 5 × 3 m = "
         "15 m and 5 × 20 cm = 100 cm = 1 m, so 16 m.",
         "Card 2 (practice values): lay 6 copies of a strip of 1 m 50 cm and sort the parts. Answer: 6 × 1 m = "
         "6 m and 6 × 50 cm = 300 cm = 3 m, so 9 m.",
         "Card 3 (practice values): lay 8 copies of a strip of 2 m 25 cm and sort the parts. Answer: 8 × 2 m = "
         "16 m and 8 × 25 cm = 200 cm = 2 m, so 18 m.",
         "Card 4 (practice values): share a road of 24 km 800 m into 4 equal days. Answer: 24 km divided by 4 is 6 km "
         "and 800 m divided by 4 is 200 m, so 6 km 200 m a day.",
         "Card 5 (practice values): share a road of 7 km 200 m into 4 equal days. 7 km does not share equally "
         "among 4, so change the whole road to m. Answer: 7,200 ÷ 4 = 1,800 m = 1 km 800 m a day.",
         "Challenge: 'We need a 1 m 80 cm cloth to make a shirt for a 10 year old child. How much cloth will be "
         "needed to make shirts for 20 such children?' Then: 'Anita is making an embroidery on the border of a sari. She "
         "needs a 1 m long thread to embroider a 50 cm sari. How much thread would she need for a 5 m sari border? A 1 m "
         "long thread costs ₹50. How much money will be needed to buy the thread?' Answer: 20 × 1 m = 20 m and 20 × "
         "80 cm = 1,600 cm = 16 m, so 36 m; the 5 m border is 500 cm and 500 ÷ 50 = 10, so 10 m of thread, and "
         "10 × 50 = ₹500.",
         "Challenge: 'A road 12 km 600 m long is being laid in a town. The workers lay an equal length of road "
         "each day, and complete the work in 6 days. How much road laying work is done on each day?' Answer: 12 km divided by "
         "6 is 2 km and 600 m divided by 6 is 100 m, so 2 km 100 m a day."],
        ["Each copy lands at the end of the last one along the tape, and the piles count the parts: for example 5 copies "
         "give 15 m in the m pile and 100 cm in the cm pile.",
         "When the cm pile reaches 100 cm or more, the tool says: 100 cm make 1 m. Tap the chip to change them.",
         "For a road, each day box shows its km and its m. If the km do not share equally, the tool says: Change the "
         "whole road to m first, then share.",
         "A wrong total slides back with a clue such as: Did you multiply the cm as well as the m?",
         "After the exchange the tool shows the total in one line, for example 16 m, and checks it against the same "
         "length in cm."],
        "All five practice cards are solved, and the shirts, Anita's thread and its cost, and the road are answered.",
        ["stripLength", "copies", "mPile", "cmPile", "days", "roadLength", "dayBoxes", "challengeIndex"],
        ["M_MULT_PART"],
        ["How many copies or how many days? What are the two parts of the length?",
         "Multiply the m part and the cm part separately, or share the km part and the m part separately.",
         "If the cm pile has 100 or more, change 100 cm to 1 m. If the km do not share equally, change the road to m.",
         "The tool lays the pieces or shares the road and shows each pile: read the total."]),

    "height_chart": T(
        "tool_height_chart", "Height Chart", "manipulative",
        "Read a height in feet and inches (12 inches = 1 foot) and find the tallest in a list by changing every height "
        "to inches.",
        "The wall of the village weaving centre with a tall wooden height chart, drawn as a warm 3D isometric scene with "
        "soft shadows and gentle animation. The chart is the largest object on screen: a tall wooden scale with a foot "
        "mark and 12 inch marks in every foot on one edge and a cm scale on the other edge. A child figure stands "
        "against it with a draggable mark at the top of the head. A read-out beside the chart says the height in feet "
        "and inches and in inches only, for example 4 feet 6 inches = 54 inches, and a note says 1 inch = 2 cm 5 mm and "
        "1 foot = 12 inches = 30 cm. A class list on a board next to the chart has rows where the student types feet "
        "and inches, and a Find the tallest button sorts them. An instruction strip at the top shows one sentence in "
        "large type with progress dots under it. Controls: drag the head mark up or down (it snaps to an inch mark); type "
        "feet and inches into a list row; tap Find the tallest; Check, Hint, Retry (clears the row being worked), Reset "
        "(restores the chart and the list), Back and Next in the same places on every card. Read-outs: feet and inches, "
        "inches, cm, the sorted list, and a card number out of 6.",
        ["Look at the video's chart with a height of 4 feet 6 inches. Say how many inches "
         "are in 1 foot, then press Next.",
         "Drag the mark to a height and read feet and inches and inches, change inches into "
         "feet and inches, and put heights in the class list to find the tallest.",
         "Do your maths book's own Measure Your Height: stand against a wall, mark your height, "
         "measure it in feet and inches, let other students measure theirs, and find the tallest student in your class "
         "and his or her height in feet and inches."],
        ["Card 1 (practice values): drag the mark to 5 feet 2 inches and read the inches. Answer: 5 × 12 + 2 = "
         "62 inches.",
         "Card 2 (practice values): the mark is at 45 inches. Read it in feet and inches. Answer: 3 feet = 36 "
         "inches and 45 − 36 = 9 inches, so 3 feet 9 inches.",
         "Card 3 (practice values): read 2 feet in cm. Answer: 1 foot = 30 cm, so 2 feet = 2 × 30 = 60 cm.",
         "Card 4 (practice values): put the heights 4 feet 1 inch, 3 feet 11 inches and 4 feet 3 inches in the "
         "list and find the tallest. Answer: 49 inches, 47 inches and 51 inches, so the tallest is 4 feet 3 inches.",
         "Card 5 (practice values): how many cm and mm is 1 inch, and how many mm are in 2 inches? Answer: 1 "
         "inch = 2 cm 5 mm = 25 mm, so 2 inches = 2 × 25 = 50 mm, which is 5 cm.",
         "Challenge: 'Stand against a wall and mark your height. Measure the distance between the floor and the "
         "marked point in feet and inches. Similarly, other students in the class can also measure their heights. Find "
         "out who is the tallest student in your class. What is his or her height in feet and inches?' Type the real "
         "heights of your class into the list, or use the practice row of the tool: the first student 4 feet 3 inches, the "
         "second student 4 feet 7 inches and the third student 4 feet 5 inches. Answer: 51 inches, 55 inches and 53 "
         "inches, so the tallest is the second student, 4 feet 7 inches. Your answer may differ."],
        ["The head mark snaps to an inch mark and the read-out shows feet and inches, inches, and cm, for example: 4 feet "
         "6 inches is 4 × 12 + 6 = 54 inches.",
         "If the inches typed are 12 or more, the tool says: 12 inches make 1 foot. Change them to feet.",
         "Find the tallest sorts the heights by inches and shows the numbers, so that the student sees why 4 feet 7 "
         "inches is more than 4 feet 5 inches.",
         "A wrong inch count slides back with a clue such as: 1 foot is 12 inches, not 10 inches.",
         "In the book's task the tool keeps the student's list on the board and says how many students are in it."],
        "All five practice cards are solved and a class list has been entered and sorted to find the tallest.",
        ["headMark", "feet", "inches", "listRows", "sortedList", "challengeIndex"],
        ["M_FOOT_TEN"],
        ["How many inches are in 1 foot? Count the inch marks between two foot marks.",
         "Multiply the feet by 12 and add the inches to get inches. To compare heights, change them all to inches.",
         "To change inches to feet and inches, take out the full 12s. The rest are the inches.",
         "The tool snaps the mark to the height and shows feet and inches and inches."]),
}
