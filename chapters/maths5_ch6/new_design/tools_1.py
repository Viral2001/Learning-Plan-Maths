# -*- coding: utf-8 -*-
"""Tool specs for T1, T3 and T5 of Class 5 Chapter 6 (The Dairy Farm): Pouch Packer (the free try of the intro, right
after the hook), Place Value Shifter and Halve and Double Packets. Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One
activity at a time, one instruction at a time, large controls, Back and Next in the same place, visible progress,
Hint, Retry and Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "pouch_packer": T(
        "tool_pouch_packer", "Pouch Packer", "manipulative",
        "Find out by packing the same 60 pouches again and again that one total can be packed in equal groups in many "
        "ways, and read each way as number of groups × group size. Turning the picture shows that swapping the two "
        "numbers keeps the total. This is the free first try of the chapter, so it asks and shows; the video that "
        "follows names the idea.",
        "The packing floor of Daljeet Kaur's dairy, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. A long wooden table carries a belt of 60 butter milk pouches, and the pouches are the largest "
        "things on screen. A few crates stand beside the table. An instruction strip at the top shows one sentence in "
        "large type, with progress dots under it. Controls: a group size stepper from 2 to 30 with a plus button and a "
        "minus button and the chosen size in big numbers; rings that gather the pouches into equal groups when the "
        "size makes equal groups; a Turn button that rotates the picture so that rows become columns; an Add to my "
        "list button; a Next total switch that changes the 60 pouches to 36 pouches (practice values); then "
        "four arrangement cards, the first one done for you as 30 × 2 = 60 and the other three with two empty boxes "
        "for the number of groups and the group size; Check, Hint, Retry (regroups this total), Reset (clears the "
        "list), Back and Next in the same places on every card. Read-outs: the sentence number of groups × group "
        "size = total, for example 12 × 5 = 60, a list called Ways found that shows every way added, and a card "
        "number out of 7.",
        ["Look at the 60 pouches from the story on Daljeet Kaur's packing table, first "
         "packed in pairs and then in threes. Pack the 60 pouches in equal groups: choose a group size with the "
         "stepper and watch the rings.",
         "Choose a group size and read the sentence number of groups × group size, press "
         "Turn and read the new sentence, add every way you find to the list Ways found, then press Next total and "
         "find the ways for 36 pouches (practice values).",
         "Answer the question from your maths book as it is. Find the number of pouches in each "
         "arrangement, with one done for you, and then say what other groups you can make."],
        ["Card 1: choose 5 as the group size. How many groups do you get? Write it as number of groups × "
         "group size. Answer: 12 groups, so 12 × 5 = 60.",
         "Card 2: press Turn and read the new sentence. Answer: 5 × 12 = 60. The pouches are the same, so "
         "swapping the two numbers keeps the total.",
         "Card 3: find every group size from 2 to 30 that packs the 60 pouches in equal groups, and add each "
         "way to the list. Answer: 10 ways, 30 × 2, 20 × 3, 15 × 4, 12 × 5, 10 × 6, 6 × 10, 5 × 12, 4 × 15, 3 × 20 "
         "and 2 × 30, all equal to 60.",
         "Card 4: try 7 as the group size. What does the tool say? Answer: 7 does not make equal groups of "
         "60, because 8 × 7 = 56 and 9 × 7 = 63, and neither is 60.",
         "Card 5 (practice values): press Next total to get 36 pouches and find every way with a group size "
         "from 2 to 30. Answer: 7 ways, 18 × 2, 12 × 3, 9 × 4, 6 × 6, 4 × 9, 3 × 12 and 2 × 18, all equal to 36.",
         "Challenge: 'A dairy has packed butter milk pouches in the following manner. Find the number of "
         "pouches kept in each arrangement. One is done for you.' The first arrangement shows 30 × 2 = 60. Fill the "
         "boxes of the other three arrangements. Answer: (b) groups of 3, 4 across and 5 down: 20 × 3 = 60; (c) 6 "
         "blocks of 2 by 5 pouches: 6 × 10 = 60; (d) 5 rows of 12 pouches: 5 × 12 = 60.",
         "Challenge: 'What other groups can you make?' Use the stepper and the list Ways found. Answer: any "
         "equal groups of 60, such as 4 × 15, 3 × 20 and 2 × 30, and each one swapped. Your list may be in a "
         "different order."],
        ["A group size that makes equal groups shows rings around every group and says, for example: 12 pouches in "
         "each group make 5 groups, and 5 × 12 = 60.",
         "A group size that does not make equal groups says, for example: 7 pouches in each group would not make "
         "equal groups of 60. Try another size.",
         "After Turn the tool says: 12 groups of 5 turn into 5 groups of 12. Both make 60 pouches.",
         "A way that is already in the list is not added twice. The tool says: You found that one already, and "
         "shows it in the list.",
         "In the book's questions a wrong box shows a soft amber note and never a red cross, for example: Count the groups first. "
         "4 groups across and 5 down is 4 × 5 = 20 groups. The tool names the number it expected only after the "
         "second try."],
        "The student has packed the 60 pouches in several equal groupings, turned a picture and seen that the total "
        "stays 60, tried 36 pouches, and completed the three arrangements and the open question of your maths book.",
        ["groupSize", "total", "groupsFound", "waysList", "turned", "challengeIndex"],
        ["M_ONE_WAY", "M_ORDER_CHANGES"],
        ["How many pouches do you want in each group? Choose a group size with the stepper.",
         "Count the groups the rings make. The number of groups times the group size must make the total number of "
         "pouches.",
         "Press Turn and read the new sentence. The rows become columns and the two numbers swap places.",
         "Try a group size of 5. The 60 pouches make 12 groups of 5, so 12 × 5 = 60, and turned it is 5 × 12 = 60."]),

    "place_value_shifter": T(
        "tool_place_value_shifter", "Place Value Shifter", "manipulative",
        "See every digit slide to the left on a place value board, with the empty places filling with zeros, to learn "
        "that multiplying by 10, 100 and 1,000 moves every digit 1, 2 or 3 places, and that multiplying tens, "
        "hundreds and thousands means multiplying the digits and writing the zeros of both numbers.",
        "The counting board of the village dairy cooperative, drawn as a warm 3D isometric scene with soft shadows "
        "and gentle animation. A wooden board with a place value table is the largest thing on screen. It has five "
        "columns named ten thousands, thousands, hundreds, tens and ones, in the same fixed colour order for ones, "
        "tens, hundreds and thousands as in every tool of this chapter. Digit tiles sit in the columns, and zero "
        "tiles that fill empty places have a different colour. A tray on the left holds the digit tiles 0 to 9. "
        "Three buttons, ×10, ×100 and ×1,000, sit under the board. A mode switch has two modes, Move digits and Tens "
        "and hundreds. In the second mode the board shows two numbers such as 60 and 70, their digits as 6 × 7, and "
        "their zeros as grey tiles that can be dragged to the end of the answer. An instruction strip at the top "
        "shows one sentence in large type, with progress dots under it. Controls: tap a digit tile in the tray and "
        "tap a column to place it, or type the number; press ×10, ×100 or ×1,000 and watch every digit slide left; "
        "drag the zeros to the end in the second mode; then fill the cells of the tables of your maths book "
        "one digit at a time; Check, Hint, Retry (returns the number to the board), Reset (clears the board), Back "
        "and Next in the same places on every card. Read-outs: a digits moved counter, for example 2 places, the "
        "problem with its product, for example 37 × 100 = 3,700, and a card number out of 7.",
        ["Look at the number from the video on the place value board. Press a button "
         "and watch every digit.",
         "Put 37 on the board and press ×10, ×100 and ×1,000, reading how many places each "
         "digit moved and what fills the empty places. Then switch to Tens and hundreds and do 60 × 70 (practice "
         "values) as 6 × 7 and two zeros.",
         "Fill in the tables of your maths book as they are asked: the six products and the "
         "table with the question about 450, the table of 2 × 1,000 to 5 × 7,000, and the table of 20 × 100 to "
         "70 × 600."],
        ["Card 1: put 37 on the board and press ×10. How many places did each digit move, and what is in the "
         "ones place now? Answer: 1 place to the left, and a 0 fills the ones place: 37 × 10 = 370.",
         "Card 2: put 37 back and press ×100. Answer: every digit moves 2 places to the left and two zeros "
         "fill the tens and ones places: 37 × 100 = 3,700.",
         "Card 3: put 37 back and press ×1,000. Answer: every digit moves 3 places to the left and three "
         "zeros fill the hundreds, tens and ones places: 37 × 1,000 = 37,000.",
         "Card 4 (practice values): switch to Tens and hundreds and do 60 × 70. Multiply the digits, then "
         "drag the zeros to the end. Answer: 6 × 7 = 42, then two zeros, so 60 × 70 = 4,200.",
         "Card 5 (practice values): in Tens and hundreds do 30 × 400. Answer: 3 × 4 = 12, then three zeros, "
         "so 30 × 400 = 12,000.",
         "Challenge: 'Find answers to the following questions. Fill in the table below and describe the "
         "pattern.' The six products are 100 × 90, 400 × 10, 60 × 50, 30 × 20 = 600, 700 × 4 and 10 × 45. Then "
         "answer 'How should we write 450 in the table below?' Answer: 9,000; 4,000; 3,000; 600; 2,800; 450. Write "
         "450 as hundreds 4, tens 5, ones 0.",
         "Challenge: 'Let us fill in the table and observe the patterns.' The first table has 2 × 1,000, "
         "5 × 1,000, 10 × 1,000, 20 × 1,000, 3 × 5,000, 8 × 3,000 and 5 × 7,000. The second table has 20 × 100, "
         "40 × 500, 60 × 300, 600 × 30, 80 × 900, 70 × 600 and 5 × 7,000. Answer: 2,000; 5,000; 10,000; 20,000; "
         "15,000; 24,000; 35,000, and 2,000; 20,000; 18,000; 18,000; 72,000; 42,000; 35,000."],
        ["After each button the digits slide and the tool says, for example: 37 × 100: each digit moved 2 places to "
         "the left, so 3,700.",
         "The zero tiles have a different colour, so the student sees that a zero fills every place the digits "
         "left.",
         "In Tens and hundreds a wrong number of zeros shows a soft amber note, for example: 30 × 20 has two zeros, "
         "one from each number, and 3 × 2 = 6, so 6 then 00 makes 600.",
         "A table cell with a wrong digit shows a soft amber note and the place it expected, for example: 450 has 4 "
         "in the hundreds place, 5 in the tens place and 0 in the ones place.",
         "A wrong answer never shows a red cross. The tool names the number it expected only after the second try."],
        "The student has moved 37 left by 10, 100 and 1,000, done two products of tens and hundreds by multiplying "
        "the digits and dragging the zeros, and filled in the tables of your maths book.",
        ["boardDigits", "multiplier", "placesMoved", "mode", "zerosDragged", "tableCells", "challengeIndex"],
        ["M_ADD_ZERO", "M_ZERO_COUNT"],
        ["Which place is each digit in now? Look at the columns of the board.",
         "How many places does each digit move? Multiplying by 10 moves it 1 place, by 100 moves it 2 places and by "
         "1,000 moves it 3 places.",
         "What fills the empty places on the right? Put a zero tile in every place the digits left.",
         "Here are the tiles slid for you: for 37 × 100 the 3 moves two places to the thousands place, the 7 moves to "
         "the hundreds place, and zeros fill the tens and ones places: 3,700."]),

    "halve_double_packets": T(
        "tool_halve_double_packets", "Halve and Double Packets", "manipulative",
        "Cut an array of butter packets in the middle and move the halves to see that halving one number and "
        "doubling the other gives a new problem with the same total, because the same packets only move.",
        "The dairy packing table with rows of butter packets, drawn as a warm 3D isometric scene with soft shadows "
        "and gentle animation. An array of equal yellow butter packets, in rows and columns up to 40 rows by 20 "
        "columns, is the largest thing on screen. A scissors line sits across the middle of the rows and can be "
        "dragged to cut across the rows or along the columns. Two number boxes with a times sign show the problem, "
        "with arrows marked Half and Double under them. An instruction strip at the top shows one sentence in large "
        "type, with progress dots under it. Controls: a stepper for the rows and a stepper for the columns; drag the "
        "scissors line to the middle and press Cut; drag one half below or beside the other half; type the new "
        "problem in two empty number boxes; Check, Hint, Retry (restores the array), Reset (clears the table), Back "
        "and Next in the same places on every card. Read-outs: the problem, for example 8 × 14, a total counter that "
        "shows the packets before and after the move, the new problem in the two number boxes, and a card number out "
        "of 7.",
        ["Look at the cut array of packets from the video. Cut the packets in the "
         "middle and put the halves together a new way.",
         "Cut an array of 8 rows of 14 packets (practice values) across the rows and put "
         "the halves side by side, read both totals, cut the columns instead, and try an array with an odd number "
         "of rows to see that it cannot be cut into two equal halves.",
         "Answer the questions of your maths book as they are: 3 × 18 into 6 × 9 and 22 × 5, "
         "the four problems like the previous ones, and the six products by halving and doubling."],
        ["Card 1 (practice values): build 8 rows of 14 packets. Cut across the rows and put the two halves "
         "side by side. What is the new problem? Answer: half of 8 is 4 and double 14 is 28, so 8 × 14 = 4 × 28 = "
         "112.",
         "Card 2 (practice values): build 8 rows of 14 packets again. Cut the 14 columns in the middle and "
         "put one half below the other. What is the new problem? Answer: half of 14 is 7 and double 8 is 16, so "
         "16 × 7 = 112.",
         "Card 3 (practice values): build 9 rows of 16 packets and try to cut across the rows. What does "
         "the tool say? Cut the columns instead. Answer: 9 rows cannot be cut into two equal halves. Cut the 16 "
         "columns into 8 and 8 and put one half below the other: 9 × 16 = 18 × 8 = 144.",
         "Card 4 (practice values): cut the new array of 4 rows of 28 across the rows again. Answer: half "
         "of 4 is 2 and double 28 is 56, so 4 × 28 = 2 × 56 = 112, and the total is still 112.",
         "Challenge: 'Butter packets are arranged in the following way. Let us find a strategy to "
         "calculate the total number of packets.' Cut 3 rows of 18 packets in the middle and put the halves one "
         "below the other, and 'Discuss why these are the same.' Then 22 rows of 5 packets are cut in the middle and "
         "put side by side: 22 × 5 becomes ___ × ___ = ____. Answer: 3 × 18 = 6 × 9 = 54, and 22 × 5 = 11 × 10 = "
         "110.",
         "Challenge: 'Solve the following problems like the previous ones.' Halve one number, double the "
         "other: 14 × 3, 16 × 4, 38 × 5 and 35 × 14. Answer: 7 × 6 = 42, 8 × 8 = 64, 19 × 10 = 190 and 70 × 7 = "
         "490. 35 is odd, so halve the 14 and double the 35.",
         "Challenge: 'Find the product by halving and doubling either the multiplier or the "
         "multiplicand.' 5 × 18, 50 × 28, 15 × 22, 25 × 12, 12 × 45 and 16 × 45. Answer: 90, 1,400, 330, 300, 540 "
         "and 720."],
        ["A cut in the middle splits the array into two equal halves and the tool says, for example: Half of 8 is 4 "
         "and double 14 is 28, and 4 × 28 = 112 is the same 112 packets.",
         "The total counter shows the packets before and after the move and says: Same packets, same total.",
         "A cut that is not in the middle shows two unequal parts and a soft amber note: The two halves must be "
         "equal. Move the scissors line to the middle.",
         "An odd number of rows or columns cannot be cut into two equal halves. The tool says, for example: 9 is odd, "
         "so cut the other side instead.",
         "A wrong new problem shows a soft amber note and never a red cross, and the tool names the numbers it "
         "expected only after the second try."],
        "The student has cut an array across the rows and along the columns, seen that the total stays the same, "
        "found that an odd number cannot be cut into two equal halves, and answered the cut-and-move questions and "
        "the halve-and-double questions of your maths book.",
        ["rows", "columns", "cutLine", "halvesPlaced", "newProblem", "totalBefore", "totalAfter", "challengeIndex"],
        ["M_HALVE_BOTH", "M_DOUBLE_BOTH"],
        ["Which number can be cut into two equal halves? Look at the rows and at the columns.",
         "What is half of that number? Move the scissors line to the middle.",
         "What do you do to the other number? Put the two halves together a new way and read the new problem.",
         "Here is the cut for you: for 8 rows of 14, half of 8 is 4 and double 14 is 28, so the new problem is "
         "4 × 28 = 112."]),
}
