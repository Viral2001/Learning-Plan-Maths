# -*- coding: utf-8 -*-
"""Tool specs for the v3 structure of Class 5 Chapter 4 (We the Travellers - II): the 11 tools of the content team's
table. Three tools are new (Near-Round Number Adder, Pair-the-Ends Lab, Table Explorer) and six are re-aimed
(Fuel Tank Adder, Fuel Gauge Subtractor, Consecutive Sums Lab, Line Up and Solve, Round Number Hops, Pairs and
Leftovers); concept_plan.py does TOOLS.update(tools_4.TOOLS) after tools_1 to tools_3, so the six keys here REPLACE the v2
specs of the same name. Balance the Sums and Number Grid Puzzle stay as they are in tools_1 and tools_3. Specs only; the
tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values and differ from the
book's numbers and from the worked example of the tool's own topic. One activity at a time, one instruction at a time,
large controls, Back and Next in the same place, visible progress, Hint, Retry and Reset always present, immediate specific
feedback that is never red. A tool with two activities (Line Up and Solve, Round Number Hops, Pairs and Leftovers) shows
one activity at a time on one shared scene, each activity with its own instruction and its own feedback; the second opens
after the first is done."""
from topics_common import T

TOOLS = {
    # ------------------------------------------------------------------------------------------------------------
    # Tool 2, topic 2 (Fuel Arithmetic: Addition): the written method only.
    "fuel_tank_adder": T(
        "tool_fuel_tank_adder", "Fuel Tank Adder", "manipulative",
        "Add two numbers with place value on a chart with large aligned columns, ones first, regrouping 10 ones as 1 ten and "
        "10 tens as 1 hundred, and write the sum. One purpose, the written method. Adding with a nearby round number is a "
        "different strategy and has its own tool, the Near-Round Number Adder.",
        "A fuel station on the road trip, drawn as a warm 3D isometric scene with soft shadows and gentle animation. The "
        "pump's display is a large chart with three columns of equal width, Hundreds, Tens and Ones, and it is the largest "
        "thing on screen. The columns are wide and the digits are large, so the ones sit exactly under the ones and the tens "
        "under the tens. The two numbers sit in two rows of the chart, one above the other, with each digit shown as fuel "
        "tokens: ones as small drops, tens as bars, hundreds as tanks. A carry row above the chart is empty at first and an "
        "answer row below is empty. An instruction strip at the top shows one sentence in large type, with progress dots "
        "under it. Controls: tap Add the ones to slide the ones drops down into the answer row; when there are 10 or more, "
        "tap Regroup 10 ones as 1 ten and watch ten drops merge into one bar that moves to the carry row of the Tens column; "
        "the same for the tens; type the digit that results in each answer box; Check; Hint; Undo; Retry (clears the answer "
        "row of this sum); Reset (restores the chart); Back and Next in the same places on every card. Read-outs: the digit "
        "sum of each column (for example 8 + 5 = 13), the carry, and the whole sum in large type when finished, and a card "
        "number out of 7.",
        ["Look at the chart from the video with 67 and 58 and the ones about to be regrouped. "
         "Say how many ones there are altogether, then press Next.",
         "Build sums on the chart and regroup when a place makes 10 or more, regroup in the ones and "
         "in the tens, add a sum with a 0 in the answer, and add a sum that needs no regrouping.",
         "The book's own two fuel questions, added on the chart."],
        ["Card 1 (practice values): add 47 and 36 on the chart. Answer: ones 7 + 6 = 13, write 3 and regroup 10 ones "
         "as 1 ten; tens 4 + 3 + 1 = 8; the sum is 83.",
         "Card 2 (practice values): add 285 and 167 on the chart. Answer: ones 5 + 7 = 12, write 2 and regroup; tens "
         "8 + 6 + 1 = 15, write 5 and regroup 10 tens as 1 hundred; hundreds 2 + 1 + 1 = 4; the sum is 452.",
         "Card 3 (practice values): add 64 and 95 on the chart. Answer: ones 4 + 5 = 9, no regrouping; tens 6 + 9 = "
         "15, write 5 and regroup 10 tens as 1 hundred; the sum is 159.",
         "Card 4 (practice values): add 506 and 195 on the chart. Answer: ones 6 + 5 = 11, write 1 and regroup; tens "
         "0 + 9 + 1 = 10, write 0 and regroup 10 tens as 1 hundred; hundreds 5 + 1 + 1 = 7; the sum is 701.",
         "Card 5 (practice values): add 213 and 124 on the chart. Answer: no place makes 10 or more, so no "
         "regrouping: 3 + 4 = 7, 1 + 2 = 3, 2 + 1 = 3, and the sum is 337.",
         "Challenge: 'A lorry has 28 litres of fuel in its tank. An additional 75 litres is filled. What is the "
         "total quantity of fuel in the lorry?' Answer: 28 + 75 = 103 litres: ones 8 + 5 = 13, write 3 and regroup; tens 2 + "
         "7 + 1 = 10, write 0 and regroup 10 tens as 1 hundred; hundreds: the 1 hundred.",
         "Challenge: 'Let us try one more. Find the sum of 49 and 89.' Answer: 49 + 89 = 138: ones 9 + 9 = 18, write "
         "8 and regroup; tens 4 + 8 + 1 = 13, write 3 and regroup 10 tens as 1 hundred; hundreds: the 1 hundred."],
        ["Each column shows its own sum and the tool says what to do, for example: 8 ones and 5 ones make 13 ones: write 3 "
         "ones and regroup 10 ones as 1 ten.",
         "When ten drops are ready the Regroup button glows; if a column has fewer than 10 the tool says: There are only 7 "
         "ones, no regrouping is needed.",
         "When a column makes exactly 10 the tool says: 10 tens: write 0 in the tens place and regroup 10 tens as 1 hundred.",
         "A wrong digit shows a soft amber note, for example: The tens make 12 tens, so write 2 and regroup 10 tens as 1 "
         "hundred. The tool names the digit it expected only after the second try.",
         "A finished sum shows a green tick, the whole sum in large type, and a quick check such as 47 + 36 = 70 + 13 = 83."],
        "The five play cards are done and the book's two fuel questions are added on the chart.",
        ["topNumber", "bottomNumber", "carryRow", "answerRow", "regroupDone", "challengeIndex"],
        ["M_NO_CARRY"],
        ["Which place do you add first? Look at the ones column.",
         "How many ones are there altogether? Can you make a ten from them?",
         "Add the two ones digits. If the total is 10 or more, regroup: write the extra ones and carry 1 ten to the next column.",
         "For 47 + 36 the ones make 13. The tool writes 3 in the ones place and moves 1 ten to the carry row, and then the "
         "tens make 4 + 3 + 1 = 8."]),

    # ------------------------------------------------------------------------------------------------------------
    # Tool 3, topic 3 (Near-Round-Number Addition): NEW. The strategy, not the written method.
    "near_round_adder": T(
        "tool_near_round_adder", "Near-Round Number Adder", "manipulative",
        "Add two numbers with a convenient nearby round number and then compensate: when a number is just below a ten or a "
        "hundred, add the round number and take the extra back, and when a number is a whole number of tens, add the tens. "
        "The milestone shows three things, the original sum, the adjustment and the corrected total. One purpose, a "
        "different strategy from the written method of the Fuel Tank Adder: this tool has no place value chart and does not "
        "teach column addition.",
        "A road milestone on the road trip, drawn as a warm 3D isometric scene with soft shadows and gentle animation. A tall "
        "milestone stone with three plates, one under the other, is the largest thing on screen. The top plate is Original "
        "sum and shows the two numbers, for example 15 + 79. The middle plate is Adjustment and shows how far the chosen "
        "number is below its round number, for example 79 is 1 less than 80, with a short number line beside it that shows the "
        "number, the round number and the gap between them as a short hop. The bottom plate is Corrected total and starts "
        "empty: it fills first with the sum that uses the round number, for example 15 + 80 = 95, and then with the take "
        "back, 95 − 1 = 94. A round number signpost, a ten or a hundred, stands at the end of the short hop. An instruction "
        "strip at the top shows one sentence in large type, with progress dots under it. Controls: tap the number you want "
        "to round (it glows orange); move the round number signpost to the nearest ten or hundred above it with the up and "
        "down arrows; type the sum with the round number in the bottom plate; tap Take back and type the corrected total; for "
        "a whole number of tens tap Add the tens instead, and the plate shows the tens added and the ones that stay; I will "
        "add it another way, which accepts any typed total; Check; Hint; Undo; Retry (clears the three plates of this sum); "
        "Reset (restores the milestone); Back and Next in the same places on every card. Read-outs: the original sum, the "
        "adjustment (how many too many were added), the corrected total in large type, and a card number out of 7.",
        ["Look at the milestone from the video with 54 + 98, where 98 is 2 less than 100. Say "
         "what 54 + 100 is, then press Next.",
         "Add a number just below a ten, a number just below a hundred, a number 3 below a ten, a "
         "whole number of tens, and choose which of two numbers to round.",
         "The book's six pairs, adding in an easier way wherever possible."],
        ["Card 1 (practice values): add 37 and 49 with a round number. Answer: 49 is 1 less than 50, so 37 + 50 = 87, "
         "and take 1 back: 87 − 1 = 86.",
         "Card 2 (practice values): add 58 and 198 with a round number. Answer: 198 is 2 less than 200, so 58 + 200 = "
         "258, and take 2 back: 258 − 2 = 256.",
         "Card 3 (practice values): add 83 and 27 with a round number. Answer: 27 is 3 less than 30, so 83 + 30 = 113, "
         "and take 3 back: 113 − 3 = 110.",
         "Card 4 (practice values): add 66 and 40, a whole number of tens. Answer: 40 is 4 tens. 6 tens and 4 tens "
         "make 10 tens, which is 100, and the 6 ones stay: 100 + 6 = 106. There is no adjustment.",
         "Card 5 (practice values): add 24 and 68 and choose which number to round. Answer: 68 is 2 less than 70, so "
         "24 + 70 = 94 and take 2 back: 94 − 2 = 92. Rounding 24 up to 30 also works: 30 + 68 = 98 and take 6 back: 98 − 6 = "
         "92. The nearer round number means a smaller take back, and both ways give 92.",
         "Challenge: 'Add the following numbers. Wherever possible, find easier ways to add the pairs of numbers. (a): "
         "15 + 79; (b): 46 + 99; (c): 38 + 35; (d): 5 + 89; (e): 76 + 28; (f): 69 + 20.' Work (a), (b) and (c) on the "
         "milestone. Answer: (a): 79 is 1 less than 80, so 15 + 80 = 95 and 95 − 1 = 94. (b): 99 is 1 less than 100, so "
         "46 + 100 = 146 and 146 − 1 = 145. (c): 73. The tool accepts any way that gives the total: 38 is 2 less than 40, so "
         "40 + 35 = 75 and 75 − 2 = 73, or the written way from the fuel station.",
         "Challenge: the same question for (d): 5 + 89; (e): 76 + 28; (f): 69 + 20. Answer: (d): 89 is 1 less than 90, "
         "so 5 + 90 = 95 and 95 − 1 = 94. (e): 28 is 2 less than 30, so 76 + 30 = 106 and 106 − 2 = 104. (f): 20 is 2 tens, so "
         "6 tens and 2 tens make 8 tens, which is 80, and the 9 ones stay: 80 + 9 = 89."],
        ["Choosing the number to round lights the short hop and the Adjustment plate says what happened, for example: 79 is 1 "
         "less than 80. Adding 80 adds 1 too many, so take 1 back.",
         "Adding the round number fills the bottom plate with the first step, for example 15 + 80 = 95, and the tool asks: How "
         "many extra were added?",
         "A wrong total shows a soft amber note, for example: 99 is 1 less than 100. Did you take the 1 back? The tool names "
         "the number it expected only after the second try.",
         "For a whole number of tens the tool says: 20 is 2 tens. 6 tens and 2 tens make 8 tens, which is 80. The 9 ones stay.",
         "When the student chooses I will add it another way, the tool says: Any way that gives the total is fine. It checks "
         "the total and does not show another method.",
         "A finished sum shows a green tick and the corrected total on the milestone, with the three plates read out: the "
         "original sum, the adjustment and the corrected total."],
        "The five play cards are done and the book's six pairs are added, each in the way the student chooses, with the "
        "milestone used wherever a number is close to a round number.",
        ["firstNumber", "secondNumber", "numberToRound", "roundNumber", "adjustment", "roundSum", "correctedTotal",
         "challengeIndex"],
        ["M_FORGET_ONE"],
        ["Look at the two numbers. Is one of them just below a round number, or a whole number of tens?",
         "Add the round number instead. Then think: did you add too many or too few, and how many?",
         "The adjustment is the gap between the number and its round number. Take that many back from the sum that uses the "
         "round number.",
         "For 37 + 49, 49 is 1 less than 50, so the tool adds 37 + 50 = 87 and takes 1 back: 86."]),

    # ------------------------------------------------------------------------------------------------------------
    # Tool 4, topic 4 (Subtraction and Its Link with Addition): subtraction by place value; adding is only a check.
    "fuel_gauge_subtractor": T(
        "tool_fuel_gauge_subtractor", "Fuel Gauge Subtractor", "manipulative",
        "Subtract with place value on an aligned chart, regrouping 1 ten as 10 ones when there are too few ones, and read "
        "the fuel left or filled on a gauge. Adding the answer to the smaller number is an optional check after the answer, a "
        "secondary step and never the task itself. The two relationship questions of the book appear only as sentence cards "
        "at the end of the tool.",
        "The fuel gauge of a minibus on the road trip, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. A large aligned chart with two columns of equal width, Tens and Ones, is the largest thing on screen. The "
        "bigger number sits on top and the smaller number below it, with each digit shown as fuel tokens: tens as bars and "
        "ones as small drops. A regroup row above the chart is empty at first and an answer row below is empty. To the right a "
        "round fuel gauge has two marks, the smaller reading and the bigger reading, and the shaded arc between them is the "
        "difference, the fuel left or the fuel filled. An instruction strip at the top shows one sentence in large type, "
        "with progress dots under it. Controls: tap Regroup 1 ten as 10 ones when the top ones are fewer than the bottom "
        "ones and watch one bar break into ten drops that join the ones; tap Take away to remove the bottom tokens; type each "
        "digit of the answer; Check; once the answer is right a small button Check by adding (optional) appears under the "
        "chart, and tapping it fills a strip, for example 18 + 47 = 65, and moves the needle to the bigger reading; Hint; "
        "Undo; Retry (clears the answer row); Reset (restores the chart); Back and Next in the same places on every card. In "
        "the two sentence cards a row of sentence cards replaces the chart: number tiles to drop into the blanks "
        "of a sentence, and for the second card number tiles and the signs + − and = to build the sentences. Read-outs: the "
        "ones after regrouping (for example 12 ones), the tens left, the difference in large type, and a card number out of "
        "7.",
        ["Look at the chart from the video for 72 − 38, where 2 ones cannot lose 8 ones. Say "
         "what you can do about it, then press Next.",
         "Subtract with a regroup, subtract with no regroup, and subtract from a number with 0 ones, "
         "then press the optional Check by adding on one answer and watch the gauge.",
         "The book's own questions: the two sets of sentences that follow from one sentence, the fuel "
         "gauge question, the difference between 82 and 37 and the eight subtractions."],
        ["Card 1 (practice values): subtract 46 from 83 on the chart. Answer: 3 ones is less than 6 ones, so regroup "
         "1 ten as 10 ones, 13 − 6 = 7; tens 7 − 4 = 3; the difference is 37.",
         "Card 2 (practice values): subtract 24 from 79. Answer: no regrouping, ones 9 − 4 = 5 and tens 7 − 2 = 5; "
         "the difference is 55.",
         "Card 3 (practice values): subtract 27 from 60, then, if you wish, press Check by adding. Answer: ones 0 is "
         "less than 7, so regroup, 10 − 7 = 3; tens 5 − 2 = 3; the difference is 33, and the check 27 + 33 = 60 fills the "
         "strip and moves the needle to the bigger reading.",
         "Challenge, sentence cards: 'Find the relationship between the numbers in the given statements and fill in "
         "the blanks appropriately. (a): If 46 + 21 = 67, then, 67 − 21 = ___. 67 − 46 = ___. (b): If 198 − 98 = 100, then, "
         "100 + ___ = 198. 198 − ___ = 98. (c): If 189 + 98 = 287, then, 287 − 98 = ___. 287 − 189 = ___. (d): If 872 − 672 = "
         "200, then, 200 + ___ = 872. 872 − ___ = 672.' Drop number tiles into the blanks. Answer: (a): 46 and 21; (b): 98 "
         "and 100; (c): 189 and 98; (d): 672 and 200.",
         "Challenge, sentence cards: 'In each of the following, write the subtraction and addition sentences that "
         "follow from the given sentence. (a): If 78 + 164 = 242, then, (b): If 462 + 839 = 1,301, then, (c): If 921 − 137 = "
         "784, then, (d): If 824 − 234 = 590, then,' Build each sentence from number tiles and the signs. Sample answer: (a): "
         "242 − 164 = 78; (b): 1,301 − 839 = 462; (c): 784 + 137 = 921; (d): 590 + 234 = 824. Your answer may differ.",
         "Challenge: 'A minibus has 18 litres of fuel left. After refuelling, the fuel meter indicates 65 litres. How "
         "much fuel has been filled in the fuel tank of the minibus?' with 'Check if 18 + 47 = 65?', and 'What is the "
         "difference between 82 and 37? Check your answer. Is 37 + ___ = 82?' Answer: 65 − 18 = 47 litres, and 18 + 47 = "
         "65; 82 − 37 = 45, and 37 + 45 = 82.",
         "Challenge: the eight subtractions (a): 57 − 11 = ___; (b): 23 − 19 = ___; (c): 49 − 21 = ___; (d): 56 − 18 "
         "= ___; (e): 93 − 35 = ___; (f): 84 − 23 = ___; (g): 70 − 43 = ___; (h): 65 − 47 = ___. Answer: (a): 46; (b): 4; "
         "(c): 28; (d): 38; (e): 58; (f): 61; (g): 27; (h): 18."],
        ["When the top ones are fewer, the tool says what is happening, for example: 2 ones are fewer than 8 ones: regroup 1 "
         "ten as 10 ones, now there are 12 ones, then 12 − 8 = 4.",
         "A wrong digit shows a soft amber note, for example: Take the smaller digit from the bigger digit? In a column the top "
         "digit is the one you start with. The tool names the digit it expected only after the second try.",
         "The optional Check by adding fills the strip and moves the needle: 18 + 47 = 65. If the sum is not the bigger "
         "number the needle stops short and the tool says: The check does not match. Look at the ones again. The check is "
         "never needed to finish a card, except on the two cards where the book asks for it.",
         "In a sentence card a correct sentence locks in with a soft chime and the whole and the two parts light up, for "
         "example: 67 is the whole, 46 and 21 are the parts. A sentence that does not use the three numbers slides back with "
         "a clue: Use the same three numbers. The whole minus a part is the other part.",
         "A finished subtraction shows a green tick, the difference in large type and the shaded arc on the gauge."],
        "The three play cards are done and the book's two sets of sentences, the fuel gauge question, the difference between "
        "82 and 37 and the eight subtractions are answered.",
        ["topNumber", "bottomNumber", "regroupRow", "answerRow", "gaugeNeedle", "checkStrip", "checkOpened",
         "sentenceCards", "challengeIndex"],
        ["M_SMALL_FROM_BIG", "M_UNRELATED"],
        ["Which number is on top? Compare the top ones digit with the bottom ones digit.",
         "Are there enough ones to take away? If not, what can you break up to get more ones?",
         "Regroup 1 ten as 10 ones: the tens go down by 1 and the ones go up by 10. Then subtract the ones, then the tens. For "
         "a sentence card, the biggest number is the whole.",
         "For 83 − 46 the tool regroups for you: 13 ones take away 6 ones is 7, and 7 tens take away 4 tens is 3, so the "
         "difference is 37."]),

    # ------------------------------------------------------------------------------------------------------------
    # Tool 5, topic 5 (Sums of Consecutive Numbers): sums, parity and differences; no pairing of the ends.
    "consecutive_sums_lab": T(
        "tool_consecutive_sums_lab", "Consecutive Sums Lab", "manipulative",
        "Build runs of consecutive numbers on stepping stones and add them step by step with a running total: choose how many "
        "numbers to add and where to start, and see every sum, whether it is even or odd, and the difference between "
        "successive sums. Pairing the first and last numbers is a different shortcut and has its own tool, the Pair-the-Ends "
        "Lab.",
        "A row of numbered stepping stones beside the road on the road trip, each stone a milestone with its number, drawn as "
        "a warm 3D isometric scene with soft shadows and gentle animation. The long row of stones is the largest thing on "
        "screen. A window of 2 to 6 lit stones glows orange and slides along the row. Under the row is a running total strip: "
        "as the lit stones are added one after another from the left, the total grows, for example 20, then 41, then 63. "
        "Under it is a table of sums, one line for each start of the window, with the sum in large type, an even or odd tag "
        "beside it and the difference to the line above in a small strip between the lines. An instruction strip at the top "
        "shows one sentence in large type, with progress dots under it. Controls: a stepper for how many numbers are lit (2 "
        "to 6); a stepper for the first number; an Add the next stone button that adds the next lit stone to the running "
        "total; a Next start button that moves the window by one stone and adds a line to the table; answer cards for even "
        "or odd and for the difference; for the explanation question a set of reason cards to build an answer from; Check; "
        "Hint; Retry (clears the answers of this card); Reset (returns the window to its first place); Back and Next in the "
        "same places on every card. Read-outs: the lit numbers, the running total, the sum, the difference between "
        "successive sums, and a card number out of 7.",
        ["Look at the window of 3 lit stones from the video with the sums 33, 36 and 39. Say "
         "what happens to the sum when the window moves one stone, then press Next.",
         "Add the lit stones one by one with the running total, slide the window for runs of 3, 5 "
         "and 6 numbers and read the differences, and look at the even and odd tags for runs of 2, 3 and 4 numbers.",
         "The book's own three boxes of sums and its three questions about them."],
        ["Card 1 (practice values): set 3 numbers and start at 20, add the lit stones one by one, then press Next "
         "start three times. What is the difference between successive sums? Answer: the running total goes 20, 41, 63; the "
         "sums are 63, 66, 69 and 72, and the difference is 3 each time, because each of the 3 numbers goes up by 1.",
         "Card 2 (practice values): set 5 numbers and start at 30, then 6 numbers and start at 30. Answer: 5 numbers: "
         "the sums 160 and 165 differ by 5. 6 numbers: the sums 195 and 201 differ by 6. The difference is the number of "
         "numbers added.",
         "Card 3 (practice values): set 2 numbers and start at 60, then 4 numbers and start at 60, and read the "
         "tags. Answer: 2 numbers give the sums 121, 123 and 125, all odd. 4 numbers give the sums 246, 250 and 254, all "
         "even.",
         "Card 4 (practice values): set 3 numbers and start at 40 and read the tags of four lines. Answer: the sums "
         "are 123, 126, 129 and 132: odd, even, odd, even. They take turns, because the sum goes up by 3 each time and 3 is "
         "odd.",
         "Challenge: 'In each of the boxes above, state whether the sums are even or odd. Explain why this is "
         "happening.' The boxes show the sums of 2 consecutive numbers 3, 5, 7 and 9, of 3 consecutive numbers 6, 9, 12 and "
         "15, and of 4 consecutive numbers 10, 14, 18 and 22. Rebuild each box with the lab, read the tags and build the "
         "reason from the cards. Answer: box 1 is all odd, one even and one odd number; box 2 is even and odd in turn, 3 times "
         "the middle number; box 3 is all even, two odd pairs. Your words may differ.",
         "Challenge: 'What is the difference between two successive sums in each box? Is it the same throughout?' "
         "Answer: box 1: 2; box 2: 3; box 3: 4. Yes, the same throughout each box, the number of numbers added.",
         "Challenge: 'What will be the difference between two successive sums for (a): 5 consecutive numbers; (b): 6 "
         "consecutive numbers?' Answer: (a): 5; (b): 6."],
        ["Each Next start line adds the new sum and the difference to the table, and the tool says what changed, for example: "
         "The sum went from 63 to 66. Each of the 3 numbers went up by 1, so the sum went up by 3.",
         "Add the next stone grows the running total one stone at a time, for example: 20 + 21 = 41, then 41 + 22 = 63.",
         "The even or odd tag appears beside each sum. A wrong answer card slides back with a clue such as: Look at one pair "
         "of consecutive numbers. Is it odd plus even?",
         "A wrong sum shows a soft amber note, for example: Did you add all 3 stones? The running total shows what has been "
         "added so far. The tool names the number it expected only after the second try.",
         "Open explanations (why the sums are even or odd) are built from cards and are never marked wrong: the tool says "
         "Your words may differ."],
        "The four play cards are done and the book's three questions about the boxes are answered.",
        ["runLength", "firstNumber", "windowPosition", "runningTotal", "sumTable", "answerCards", "challengeIndex"],
        ["M_CONSEC_PARITY", "M_SUCC_DIFF_ONE"],
        ["How many numbers are lit? Look at the stepper and the running total under the row.",
         "When the window moves one stone, what happens to each lit number? What does that do to the sum?",
         "Each number goes up by 1, so the sum goes up by the number of lit stones. Find that difference in the table.",
         "For 3 lit stones the difference is 3. The tool writes 63, 66, 69, 72 and marks the difference 3 between each pair "
         "of lines."]),

    # ------------------------------------------------------------------------------------------------------------
    # Tool 6, topic 6 (Pair-the-Ends Shortcut): NEW.
    "pair_the_ends_lab": T(
        "tool_pair_the_ends_lab", "Pair-the-Ends Lab", "manipulative",
        "Add a run of consecutive numbers without adding one by one: the first and last numbers form a pair, then the second "
        "and the second from last, and every pair makes the same total; when there is an odd number of numbers the middle "
        "number stands alone. One purpose, the pairing shortcut; the patterns of the sums belong to the Consecutive Sums Lab.",
        "A long sequence strip painted on a roadside wall at a rest stop on the road trip, drawn as a warm 3D isometric scene "
        "with soft shadows and gentle animation. The strip of 3 to 6 number tiles, each tile a large square with its number, is "
        "the largest thing on screen. Pair brackets arch above the strip and a pair total plate hangs under each bracket. An "
        "instruction strip at the top shows one sentence in large type, with progress dots under it. Controls: a stepper for "
        "how many numbers are on the strip (3 to 6) and a stepper for the first number; tap Pair the ends and watch the first "
        "and last tiles slide inward and join under a bracket with their total, tap again for the next pair, and so on; when "
        "there is an odd number of numbers the middle tile stays in place with a small label, no partner; type the pair "
        "total, the number of pairs and the sum in three boxes; Check; Hint; Undo; Retry (clears the strip for this card); "
        "Reset (restores the strip); Back and Next in the same places on every card. Read-outs: each pair total, the number "
        "of pairs, the middle number when there is one, the sum in large type when finished, and a card number out of 6.",
        ["Look at the strip from the video with 41 to 45 and the first and last tiles moving "
         "inward. Say what 41 + 45 is, then press Next.",
         "Pair the ends of runs of 3, 4, 5 and 6 numbers, notice the middle number of a run with "
         "an odd count, and check a friend's claim about the sum.",
         "The book's four sums to find without adding the numbers directly."],
        ["Card 1 (practice values): set 3 numbers and start at 90, and pair the ends. Answer: 90 + 92 = 182, and the "
         "middle number 91 stands alone: 182 + 91 = 273.",
         "Card 2 (practice values): set 4 numbers and start at 83, and pair the ends. Answer: 83 + 86 = 169 and 84 + "
         "85 = 169, so the sum is 169 + 169 = 338. There is no middle number.",
         "Card 3 (practice values): set 5 numbers and start at 70, and pair the ends. A friend says the sum is 5 × 70 "
         "= 350. Is the friend right? Answer: 70 + 74 = 144 and 71 + 73 = 144, the middle number is 72, and the sum is 144 + "
         "144 + 72 = 360, which is 5 × 72. The friend is not right: 5 × 70 = 350 uses the first number, and the middle "
         "number gives the sum.",
         "Card 4 (practice values): set 6 numbers and start at 15, and pair the ends. Answer: 15 + 20 = 35, 16 + 19 = "
         "35 and 17 + 18 = 35, so the sum is 35 + 35 + 35 = 105.",
         "Challenge: 'Notice how the sums of 3, 4, and 5 consecutive numbers are related to the numbers being added. "
         "Use your understanding to find the following sums without adding the numbers directly. (a): 67 + 68 + 69; (b): 24 "
         "+ 25 + 26 + 27; (c): 48 + 49 + 50 + 51 + 52; (d): 237 + 238 + 239 + 240 + 241 + 242.' Pair the ends for (a) and "
         "(b). Answer: (a): 67 + 69 = 136, and the middle number 68: 136 + 68 = 204. (b): 24 + 27 = 51 and 25 + 26 = 51, so "
         "51 + 51 = 102.",
         "Challenge: the same question, pair the ends for (c): 48 + 49 + 50 + 51 + 52 and (d): 237 + 238 + 239 + 240 "
         "+ 241 + 242. Answer: (c): 48 + 52 = 100 and 49 + 51 = 100, the middle number is 50: 100 + 100 + 50 = 250. (d): 237 + "
         "242 = 479, 238 + 241 = 479 and 239 + 240 = 479, so 479 + 479 + 479 = 1,437."],
        ["Each tap of Pair the ends slides the next two numbers inward and writes their total, for example: 70 + 74 = 144. Then "
         "71 + 73 = 144. The pairs make the same total.",
         "The middle number stays alone and the tool says: 72 has no partner. It is half of 144.",
         "A wrong sum shows a soft amber note, for example: Did you add the pair totals and the middle number? The tool names "
         "the number it expected only after the second try.",
         "If the student types the count times the first number, the strip shows the pairs again and the tool says: The first "
         "number is the smallest on the strip, so that is too small. Look at the pair totals and the middle number.",
         "A finished sum shows a green tick, the sum in large type and the other way to say it, for example 5 × 72 = 360."],
        "The four play cards are done and the book's four sums are found by pairing the ends.",
        ["runLength", "firstNumber", "pairsMade", "pairTotal", "middleNumber", "sumBox", "challengeIndex"],
        ["M_FIRST_TIMES"],
        ["Look at the first and the last number of the strip. What do they make together?",
         "Pair the next two numbers, moving inward. Is the total the same? Is a number left without a partner?",
         "Count the pairs and multiply by the pair total, then add the middle number if there is one.",
         "For 83 + 84 + 85 + 86 the pairs are 83 + 86 = 169 and 84 + 85 = 169, so the sum is 169 + 169 = 338."]),

    # ------------------------------------------------------------------------------------------------------------
    # Tool 7, topic 7 (Adding and Subtracting Large Numbers): one board, two separate activities.
    "line_up_and_solve": T(
        "tool_line_up_and_solve", "Line Up and Solve", "manipulative",
        "One shared place value board for large numbers, up to 5 digits, with two clearly separate activities. The lining up "
        "of the digits, ones under ones, tens under tens and so on, is shown once; then Activity 1, Add, and Activity 2, "
        "Subtract, each have their own instruction and their own feedback and work one place at a time from the right.",
        "A toll plaza board on the road trip, drawn as a warm 3D isometric scene with soft shadows and gentle animation. A "
        "large plain board with five columns of equal width is the largest thing on screen; a sixth column opens on the left "
        "only when a sum needs it, and it is never named. A small dot marks the right edge of the Ones column and no place "
        "names are written at first. A row of digit tiles 0 to 9 sits under the board, and the plus or minus sign tile sits "
        "on the left of the second number. A regroup row above the board holds small marks and an answer row below is empty. "
        "Two big activity tabs sit at the top, Activity 1: Add and Activity 2: Subtract. The board is the same in both. Only "
        "one activity is on screen at a time, and Activity 2 opens after Activity 1 is done. An instruction strip at the top "
        "shows one sentence in large type, with progress dots under it, and it is the activity's own sentence. Controls in "
        "both activities: drag the digits of each number onto the board; a Show place names toggle that writes ten thousands, "
        "thousands, hundreds, tens and ones above the columns and is off at first; Check; Hint; Undo; Retry (clears the board "
        "for this question); Reset (restores the tiles); Back and Next in the same places on every card. Controls only in "
        "Activity 1: tap a column to put a regroup mark above the next place on the left; type each answer digit. Controls "
        "only in Activity 2: tap a column to regroup 1 from the place on its left as 10 here, and a small mark shows the left "
        "place going down by 1 and this place going up by 10; type each answer digit. In the first card of Activity 1 the "
        "digits are placed by the student with a thin guide through the columns; in the play cards of Activity 2 the numbers "
        "arrive already lined up. Read-outs: the column being worked, the digit sum or difference of that column, the whole "
        "answer in large type when finished, and a card number out of 7.",
        ["This card is shared by both activities and the lining up is shown only here. Look at "
         "the board from the video with 3,486 and 2,729 lined up from the right and no place names. Say which digit of 2,729 "
         "sits under the 8 of 3,486, then press Next.",
         "Activity 1: place the digits of numbers with different lengths and add them. Activity 2: on "
         "the same board, subtract across a zero and subtract a number with fewer digits.",
         "Activity 1: the book's sums, the corridor and Mahesh's journey, the six sums, the road trip, "
         "the closest sums and the nine sums. Activity 2: the book's subtractions, the ship and the land route, the six "
         "subtractions and the nine subtractions."],
        ["Activity 1, card 1 (practice values): place the digits of 481 and 56 and add. Answer: the 6 goes under the 1 "
         "and the 5 under the 8. Ones: 1 + 6 = 7. Tens: 8 + 5 = 13, write 3 and regroup. Hundreds: 4 + 1 = 5. The sum is 537.",
         "Activity 1, card 2 (practice values): place the digits of 7,258 and 14,963 and add. Answer: ones 8 + 3 = 11, "
         "write 1 and regroup; tens 5 + 6 + 1 = 12, write 2 and regroup; hundreds 2 + 9 + 1 = 12, write 2 and regroup; "
         "thousands 7 + 4 + 1 = 12, write 2 and regroup; ten thousands 0 + 1 + 1 = 2. The sum is 22,221.",
         "Activity 1, card 3: 'One of the places on the North-South Corridor was 1,855 km from Srinagar and 1,862 km "
         "from Kanniyakumari. What was the total length of the North-South Corridor in 2019?' and 'Mahesh and his family "
         "decide to drive from Srinagar to Kanniyakumari. He spends ₹21,880 on fuel and toll tax, and ₹38,900 on other "
         "expenses during this journey. How much did he spend in total?' and 'Find the following sums. Try not to write ten "
         "thousands, thousands, hundreds, tens and ones at the top. Just align the digits properly, at least for the smaller "
         "numbers. (a): 238 + 367; (b): 1,234 + 12,345; (c): 12 + 123; (d): 46,120 + 12,890; (e): 878 + 8,789; (f): 1,749 + "
         "17,490.' Answer: 3,717 km; ₹60,780; (a): 605; (b): 13,579; (c): 135; (d): 59,010; (e): 9,667; (f): 19,239.",
         "Activity 1, card 4: 'The great Indian road trip! Nazrana and her friends planned a road trip across India, "
         "starting from Delhi. They first drove to Mumbai, then Goa, then Hyderabad, and finally Puri. Look at the distances "
         "marked on the map and help them find the total distance travelled.' and 'Find 2 numbers among 5,205, 6,220, 7,095, "
         "8,455, and 4,840 whose sum is closest to the following. (a): 10,000; (b): 15,000; (c): 13,000; (d): 16,000.' and "
         "'Add. (a): 2,009 + 7,388; (b): 26,444 + 71,111; (c): 777 + 888; (d): 1,234 + 1,234; (e): 56 + 56,789; (f): 777 + "
         "77,777; (g): 5,922 + 9,221; (h): 4,321 + 8,765; (i): 50,050 + 55,000.' Answer: the legs 1,600 km, 590 km, 670 km and "
         "1,055 km make 3,915 km; (a): 5,205 and 4,840; (b): 6,220 and 8,455; (c): 8,455 and 4,840; (d): 7,095 and 8,455; "
         "the nine sums (a): 9,397; (b): 97,555; (c): 1,665; (d): 2,468; (e): 56,845; (f): 78,554; (g): 15,143; (h): 13,086; "
         "(i): 1,05,050, where the extra 1 sits in a new column on the left.",
         "Activity 2, card 5 (practice values): the digits of 8,305 and 2,467 are already lined up. Subtract. Answer: "
         "ones 5 is less than 7 and the tens digit is 0, so regroup 1 hundred as 10 tens and then 1 ten as 10 ones: ones 15 − "
         "7 = 8, tens 9 − 6 = 3; hundreds 2 is less than 4, so regroup 1 thousand as 10 hundreds: 12 − 4 = 8; thousands 7 − "
         "2 = 5. The difference is 5,838.",
         "Activity 2, card 6 (practice values): place the digits of 9,640 and 640 and subtract. Answer: the digits of "
         "640 sit under the hundreds, tens and ones, and the thousands column has nothing under it. Ones 0 − 0 = 0, tens 4 − "
         "4 = 0, hundreds 6 − 6 = 0, thousands 9. The difference is 9,000.",
         "Activity 2, card 7: 'The total distance of the sea route from Mumbai to Chennai is 2,700 km. A ship starting "
         "from Mumbai first reaches the Cochin port, travelling 1,083 km by sea. How much more distance does it have to "
         "travel to reach the Chennai port?' and 'As you learnt earlier, the longest land route is 15,150 km between Talon "
         "(Russia) and Sagres (Portugal). The longest highway in Africa is 10,228 km long, connecting the cities of Cairo, in "
         "Egypt and Cape Town, in South Africa. How much longer is the land route between Talon and Sagres compared to the "
         "highway between Cairo and Cape Town?' and 'Subtract the following. Try not to write ten thousands, thousands, "
         "hundreds, tens and ones at the top. Align the digits carefully. (a): 4,578 − 2,222; (b): 15,324 − 11,780; (c): "
         "5,423 − 423; (d): 123 − 12; (e): 77,777 − 777; (f): 826 − 752.' and 'Subtract. (a): 458 − 226; (b): 7,777 − 4,449; "
         "(c): 65,447 − 47,299; (d): 1,234 − 123; (e): 12,345 − 1,234; (f): 56,789 − 56; (g): 87,326 − 11,111; (h): 878 − 52; "
         "(i): 749 − 222.' Answer: 1,617 km; 4,922 km; (a): 2,356; (b): 3,544; (c): 5,000; (d): 111; (e): 77,000; (f): 74; the "
         "nine subtractions (a): 232; (b): 3,328; (c): 18,148; (d): 1,111; (e): 11,111; (f): 56,733; (g): 76,215; (h): 826; "
         "(i): 527."],
        ["A digit dropped in the wrong column shows a soft amber note that names the digit, for example: The 2 of 12 belongs "
         "in the Tens column. Ones go under ones. The tool never moves the digit for the student. This note and the thin "
         "guide are shared by both activities, and the lining up is not explained again in Activity 2.",
         "When the digits are lined up the board shows a thin guide through every column, and the tool says: Ones under "
         "ones, tens under tens. Now work from the right. This is said once, in the first card of Activity 1.",
         "Activity 1 only: each column shows its own result as the student works, for example: 8 + 3 = 11: write 1 and regroup "
         "10 ones as 1 ten. A wrong answer digit shows a soft amber note such as: Check the tens again, there is a regroup "
         "mark. The tool names the digit it expected only after the second try.",
         "Activity 2 only: each column shows its own result, for example: 5 ones is less than 7 ones: regroup 1 ten as 10 "
         "ones. When the tens digit is 0 the tool says: There is no ten to regroup, so go to the hundreds first. A wrong "
         "answer digit shows a soft amber note such as: Which number is on top in this column? The tool names the digit it "
         "expected only after the second try.",
         "A finished question shows a green tick and the whole answer in large type, and the tool adds the other way to say it, "
         "for example 481 + 56 = 537 in Activity 1 and 5,838 + 2,467 = 8,305 in Activity 2."],
        "Activity 1 is done when its two play cards are added and the book's corridor and Mahesh's journey, the six sums, "
        "the road trip, the closest sums and the nine sums are done. Activity 2 is done when its two play cards are "
        "subtracted and the book's ship and land route, the six subtractions and the nine subtractions are done.",
        ["activity", "boardDigits", "firstNumber", "secondNumber", "operation", "regroupMarks", "answerRow",
         "showPlaceNames", "sixthColumnOpen", "challengeIndex"],
        ["M_MISALIGN", "M_NO_CARRY", "M_SMALL_FROM_BIG"],
        ["Where is the ones digit of each number? Look at the right end of each number.",
         "Line up the ones digits first, then work one column at a time from the right. In Activity 2, ask whether there are "
         "enough in this column to take away.",
         "Put each digit of the shorter number under the matching place of the longer number, starting from the right. Empty "
         "places stay empty. Then add or subtract one column at a time.",
         "For 481 and 56 the tool slides the 6 under the 1 and the 5 under the 8, and the hundreds column of 56 stays empty."]),

    # ------------------------------------------------------------------------------------------------------------
    # Tool 8, topic 9 (Quick Sums and Differences): one number line, two labelled modes.
    "round_number_hops": T(
        "tool_round_number_hops", "Round Number Hops", "manipulative",
        "Use a round number as a stepping stone, in two separate modes on one number line. Mode A, Make a round number: make "
        "9 in every place and add 1 to find what to add to reach 100, 1,000 or 10,000. Mode B, Take away 9 or 99: take away "
        "10 or 100 and give 1 back. Each mode has its own instruction and its own feedback, and Mode B opens after Mode A is "
        "done.",
        "A long straight road on the road trip with signposts for 100, 1,000 and 10,000, drawn as a warm 3D isometric scene "
        "with soft shadows and gentle animation. A number line runs along the road and is the largest thing on screen. A small "
        "car waits on the start marker and hops along the line. Two big mode tabs sit at the top, Mode A: Make a round number "
        "and Mode B: Take away 9 or 99. Only one mode is on screen at a time. In Mode A the start number sits on a small "
        "marker on the line and a round target signpost stands ahead; beside the line is a digit partner panel, where each "
        "digit of the start number sits above a box that shows the digit that makes 9 with it. In Mode B the start number "
        "sits on the line and the digit partner panel is replaced by two hop buttons, and the signposts are the tens and "
        "hundreds just below the number. An instruction strip at the top shows one sentence in large type, with progress "
        "dots under it, and it is the mode's own sentence. Controls in Mode A: tap each digit to see its nine partner; tap "
        "Add 1 to hop one step to the round number; type the answer in the blank. Controls in Mode B: tap Hop back 10 or Hop "
        "back 100, then tap Hop forward 1; type the answer in the blank. In both modes: Check; Hint; Undo; Retry (clears the "
        "hops for this question); Reset (puts the car at the start); Back and Next in the same places on every card. "
        "Read-outs: in Mode A the nine partners, the number that makes 99, 999 or 9,999 and the number after the extra 1; in "
        "Mode B the number after each hop; in both the answer in large type when finished, and a card number out of 7.",
        ["Mode A: look at the road from the video with 46, the number 53 that makes 99 with it "
         "and the extra hop of 1 to 100. Say which number is 1 less than 100. Mode B: look at the road with 52, the hop back "
         "10 to 42 and the hop forward 1 to 43. Say how many too many the hop back 10 took away, then press Next.",
         "Mode A: make 100, 1,000 and 10,000 from a number with the nines and the extra 1. Mode B: "
         "take away 9 and 99 by hopping back to the round number and forward by 1.",
         "Mode A: the book's blanks that make 100, 1,000 and 10,000, with the nines method and with the "
         "numbers that end in 0. Mode B: the book's take away 9 or 99 and the blanks that leave 9 or 99."],
        ["Mode A, card 1 (practice values): make 100 from 63: 63 + ___ = 100. Answer: 6 needs 3 and 3 needs 6, so 63 + "
         "36 = 99, then add 1: 63 + 37 = 100.",
         "Mode A, card 2 (practice values): make 1,000 from 425: 425 + ___ = 1,000, and 10,000 from 6,284: 6,284 + ___ "
         "= 10,000. Answer: 4 needs 5, 2 needs 7 and 5 needs 4, so 425 + 574 = 999, then 425 + 575 = 1,000. The nine "
         "partners of 6,284 are 3, 7, 1 and 5, so 6,284 + 3,715 = 9,999, then 6,284 + 3,716 = 10,000.",
         "Mode A, card 3: 'Sukanta likes the numbers 10, 100, 1,000, and 10,000. He wants to figure out what number "
         "he should add to a given number such that the sum is 100 or 1,000. Help him fill in the blank with an appropriate "
         "number. 32 + ___ = 100' and 'Try this method for the number 59. 59 + ___ = 100' Answer: 32 + 68 = 100 and 59 + 41 "
         "= 100.",
         "Mode A, card 4: 'Now, use this method to solve the following. 877 + ___ = 1,000 and 666 + ___ = 1,000; "
         "4,103 + ___ = 10,000 and 5,555 + ___ = 10,000.' and 'Will this method work if the units digit is 0? What do you "
         "think? What other methods can you use to find the missing number to fill in the blanks? Share your thoughts in the "
         "class. (a): 180 + ___ = 1,000; (b): 760 + ___ = 1,000; (c): 400 + ___ = 1,000.' Answer: 877 + 123 = 1,000; 666 + "
         "334 = 1,000; 4,103 + 5,897 = 10,000; 5,555 + 4,445 = 10,000; (a): 820; (b): 240; (c): 600. Yes, the method works "
         "with a 0 in the units place, because the last nine is 9 and adding 1 carries. Another way is to count up to the next "
         "hundred and then to 1,000. Your words may differ.",
         "Mode B, card 5 (practice values): take away 9 from 84, and take away 99 from 342. Answer: 84: hop back 10 "
         "to 74, then forward 1 to 75, so 84 − 9 = 75. 342: hop back 100 to 242, then forward 1 to 243, so 342 − 99 = 243.",
         "Mode B, card 6: 'Namita likes the number 9. She wants to subtract 9 or 99 from any number. Find a way to "
         "quickly subtract 9 or 99 from any number. (a): 67 − 9 = ___; (b): 83 − 9 = ___; (c): 144 − 9 = ___; (d): 187 − 99 = "
         "___; (e): 247 − 99 = ___; (f): 763 − 99 = ___.' Answer: (a): 58; (b): 74; (c): 135; (d): 88; (e): 148; (f): 664.",
         "Mode B, card 7: 'Now, use the above solutions to find answers to the following problems. Do not calculate "
         "again. Namita wonders if she can get 9 or 99 as the answer to any subtraction problem. Find a way to get the "
         "desired answer. (a): 32 − ___ = 9; (b): 56 − ___ = 9; (c): 877 − ___ = 99; (d): 666 − ___ = 99.' Answer: (a): 23; "
         "(b): 47; (c): 778; (d): 567."],
        ["Mode A: the digit partner panel lights each pair that makes 9, and the tool says what to do next, for example: 6 and "
         "3 make 9. So 63 + 36 = 99. One more makes 100.",
         "Mode A: a wrong answer shows a soft amber note, for example: 99 is 1 less than 100. Did you add the 1? The tool "
         "names the number it expected only after the second try. On a number that ends in 0 the tool says: The method still "
         "works. The last nine is 9, and adding 1 carries.",
         "Mode B: each hop writes the result on the line, for example: 84 − 10 = 74, then 74 + 1 = 75. The tool says: 10 is 1 "
         "more than 9, so give 1 back. For 99 it says: 100 is 1 more than 99, so give 1 back.",
         "Mode B: a wrong answer shows a soft amber note, for example: You took away 10. Did you give 1 back? For a blank "
         "that leaves 9 the tool says: The blank is the first number minus 9: for 47 − ___ = 9, 47 − 10 = 37 and 37 + 1 = 38, "
         "so 47 − 38 = 9.",
         "A finished question shows a green tick, the answer in large type and the check, for example 63 + 37 = 100 in Mode A "
         "and 84 − 9 = 75 in Mode B."],
        "Mode A is done when its two play cards and the book's blanks that make 100, 1,000 and 10,000 are answered. Mode B is "
        "done when its play card and the book's two sets of take away 9 or 99 blanks are answered.",
        ["mode", "startNumber", "targetNumber", "nineDigits", "hopLog", "answerBlank", "challengeIndex"],
        ["M_NINES_ZERO", "M_FORGET_ONE"],
        ["Which round number are you hopping towards, or hopping back to? Look at the signpost on the road.",
         "Mode A: make 9 in every place. What does each digit need to make 9? Mode B: 9 is 1 less than 10, so what do you do "
         "after you hop back 10?",
         "Mode A: write the nine partner of each digit. That gives the number that makes 99, 999 or 9,999. What is left to "
         "reach the round number? Mode B: you took away too many, so how many do you give back?",
         "Mode A: for 63 the partners are 3 and 6, so 63 + 36 = 99. Add the extra 1 to the blank, and 63 + 37 = 100. Mode B: "
         "for 84 − 9 the tool hops back 10 to 74 and forward 1 to 75."]),

    # ------------------------------------------------------------------------------------------------------------
    # Tool 10, topic 13 (Sums of Even and Odd Numbers; also serves topic 12): one counter board, two activities.
    "pairs_and_leftovers": T(
        "tool_pairs_and_leftovers", "Pairs and Leftovers", "manipulative",
        "Arrange draggable counters into pairs, in two clearly separated activities. Activity 1, Pair up: decide whether a "
        "number is even or odd by pairing counters, with any leftover counter made visible. Activity 2, Combine two groups: "
        "join two counter groups, pair the joined group and inspect the leftover to see what happens in the sum of two even "
        "numbers, two odd numbers, and an odd and an even number. Activity 2 opens after Activity 1 is done.",
        "A wooden board on a bench at a bus stand with round blue counters, drawn as a warm 3D isometric scene with soft "
        "shadows and gentle animation. Two big activity tabs sit at the top, Activity 1: Pair up and Activity 2: Combine two "
        "groups, and only one activity is on screen at a time. In Activity 1 the board shows one large drop zone for a group "
        "of counters. In Activity 2 it shows a drop zone for Group 1, one for Group 2 and a combine zone between them. The "
        "counters in the zones are the largest things on screen. A counter group is arranged in two rows so that each counter "
        "in the top row is paired with the one below it; a counter with no partner is marked with a small orange ring. An "
        "instruction strip at the top shows one sentence in large type, with progress dots under it, and it is the "
        "activity's own sentence. Beside each group is its number in large type and an even or odd tag that appears after "
        "the student answers. Controls in Activity 1: a stepper for the number of counters (0 to 40); drag counters in or "
        "out; tap Pair up to arrange the group in two rows; answer cards even and odd. Controls in Activity 2: a stepper for "
        "the number of counters in each group; tap Pair up to arrange a group in two rows; tap Combine to join Group 1 and "
        "Group 2 in the combine zone, then tap Pair up again to pair the joined group; answer cards even and odd for the "
        "sum; for the book's questions a Choose a pair button that stores each chosen pair and its sum. In both: Check; Hint; "
        "Retry (clears this card); Reset (restores the board); Back and Next in the same places on every card. Read-outs: "
        "the number in each group, the number of pairs, the number of leftover counters (0 or 1), the joined number, and a "
        "card number out of 7.",
        ["Activity 1: look at the board from the earlier video with 14 counters in 7 pairs and "
         "15 counters in 7 pairs with 1 left over. Say which number has a leftover. Activity 2: look at the board from the "
         "video with 9 counters and 13 counters, each with a ringed leftover. Say what the two leftovers make when the groups "
         "join, then press Next.",
         "Activity 1: pair up groups of counters and tag each one even or odd. Activity 2: combine two "
         "even groups, two odd groups, and an odd and an even group, pair the joined group and read its leftover.",
         "Activity 2: the book's three questions, five pairs of two even numbers, five pairs of two odd "
         "numbers and five pairs of an odd and an even number, with what you notice about their sums."],
        ["Activity 1, card 1 (practice values): pair up 16 counters, then 21 counters, then 30 counters, and tag "
         "each one. Answer: 16 makes 8 pairs with none left over, so it is even. 21 makes 10 pairs with 1 left over, so it "
         "is odd. 30 makes 15 pairs with none left over, so it is even, like every number that ends in 0.",
         "Activity 2, card 2 (practice values): combine Group 1 with 6 counters and Group 2 with 10 counters, and pair "
         "the joined group. Answer: 6 + 10 = 16, no leftover in either group, so the joined group has none and 16 is even.",
         "Activity 2, card 3 (practice values): combine Group 1 with 11 counters and Group 2 with 15 counters. Answer: "
         "each group has 1 leftover. The two leftovers make one pair, so 11 + 15 = 26 has none left over and is even.",
         "Activity 2, card 4 (practice values): combine Group 1 with 19 counters and Group 2 with 6 counters. Answer: "
         "only the group of 19 has a leftover, and it stays alone, so 19 + 6 = 25 has 1 left over and is odd.",
         "Activity 2, card 5: 'What do you notice about the sums in each of the following cases? Do you think it will "
         "be true for all pairs of such numbers? Explain your observations. You may use the paired arrangement to explain "
         "your thinking. (a): 12 and 6 are a pair of even numbers. Choose 5 such pairs of even numbers. Add the numbers in "
         "each of the pairs.' Sample answer: 12 + 6 = 18, 4 + 8 = 12, 10 + 20 = 30, 14 + 16 = 30 and 2 + 6 = 8. Every sum "
         "is even, for all such pairs, because two even numbers pair up with none left over. Your pairs may differ.",
         "Activity 2, card 6: 'What do you notice about the sums in each of the following cases? Do you think it will "
         "be true for all pairs of such numbers? Explain your observations. You may use the paired arrangement to explain "
         "your thinking. (b): 13 and 9 are a pair of odd numbers. Choose 5 such pairs of odd numbers. Add the numbers in each "
         "of the pairs.' Sample answer: 13 + 9 = 22, 3 + 5 = 8, 7 + 11 = 18, 15 + 1 = 16 and 9 + 9 = 18. Every sum is even, "
         "for all such pairs, because each odd number has 1 left over and the two leftovers make a pair. Your pairs may "
         "differ.",
         "Activity 2, card 7: 'What do you notice about the sums in each of the following cases? Do you think it will "
         "be true for all pairs of such numbers? Explain your observations. You may use the paired arrangement to explain "
         "your thinking. (c): 7 and 12 are a pair of odd and even numbers. Choose 5 such pairs of odd and even numbers. Add "
         "the numbers in each of the pairs.' Sample answer: 7 + 12 = 19, 3 + 4 = 7, 5 + 10 = 15, 9 + 2 = 11 and 11 + 8 = "
         "19. Every sum is odd, for all such pairs, because the odd number's leftover has no partner. Your pairs may "
         "differ."],
        ["Activity 1: Pair up arranges the counters in two rows and rings a counter that has no partner, then says: 21 "
         "counters make 10 pairs and 1 is left over, so 21 is odd.",
         "Activity 2: Combine joins the two groups and the leftover rings move together, for example: The two leftovers make "
         "one pair. Nothing is left over, so the sum is even. When only one group has a leftover the tool says: The leftover "
         "stays alone, so the sum is odd.",
         "A wrong answer card slides back with a clue such as: Look for a ringed counter. Is one left over?",
         "Open answers (the pairs the student chooses and their words) are never marked wrong: the tool says Your pairs may "
         "differ, and checks only that each sum is read correctly as even or odd.",
         "After the fifth chosen pair the tool shows the five sums side by side and asks: Are they all even or odd? Is it true "
         "for every pair of such numbers?"],
        "Activity 1 is done when the three groups are paired and tagged. Activity 2 is done when its three play cards are "
        "answered and the book's three questions, each with five chosen pairs, are answered.",
        ["activity", "group1Count", "group2Count", "pairedRows", "leftoverMarks", "combinedGroup", "answerCards",
         "pairsChosen", "challengeIndex"],
        ["M_ZERO_NOT_EVEN", "M_ODD_ODD_ODD"],
        ["Are the counters in pairs? Look for a counter with no partner.",
         "Pair up the counters. How many pairs are there, and is one counter left over?",
         "When two groups join, what happens to the leftover counters? Do they make a pair?",
         "For 11 and 15 each group has 1 leftover. The tool joins them into one pair, and 11 + 15 = 26 has nothing left over, "
         "so it is even."]),

    # ------------------------------------------------------------------------------------------------------------
    # Tool 11, topic 16 (Reading Tables): NEW.
    "table_explorer": T(
        "tool_table_explorer", "Table Explorer", "manipulative",
        "Read a table: use the headings and the units to find a value, compare the numbers in a column to find the highest "
        "and the lowest, subtract the smaller from the bigger to find a difference, and for a printed number against a "
        "needed number say whether it is sufficient, how many are short or how many are extra.",
        "A travel information board in a station hall on the road trip, drawn as a warm 3D isometric scene with soft shadows "
        "and gentle animation. The board is a large table with a heading at the top of every column and its unit beside it, "
        "for example km or year, and one row for each thing; the table is the largest thing on screen and its numbers are in "
        "large type. The book's own tables are shown as the book prints them, with the same rows, the same headings and the "
        "same numbers. An instruction strip at the top shows one sentence in large type, with progress dots under it. A "
        "compare strip under the board shows two chosen numbers with the bigger first, the minus sign and a blank for the "
        "difference. Controls: tap a row to light it and tap a column heading to light the column, and the cell where they "
        "meet glows orange; tap two numbers of one column to put them in the compare strip; type the difference in the blank; "
        "for a printed number against a number of people, answer cards Sufficient, Short and Extra and a box for how many; "
        "type a year or a name in an answer box; Check; Hint; Undo; Retry (clears the answers of this card); Reset (restores "
        "the board); Back and Next in the same places on every card. Read-outs: the row and column in focus, the two numbers "
        "compared, the difference, and a card number out of 6.",
        ["Look at the board from the video with the three buses: 4,215 km and 2015, 6,380 km and "
         "2018, 5,094 km and 2021. Say which bus travelled the most, then press Next.",
         "Read a value from a row and a column, find the highest and the lowest and the difference "
         "between two values, work out a year from an age, and decide whether a printed number was sufficient, short or "
         "extra.",
         "The book's own two tables: the mountains and the certificates."],
        ["Card 1 (practice values): a railway board shows Train A 2,865 km and 2009, Train B 1,978 km and 2014, Train "
         "C 3,412 km and 2011, Train D 2,149 km and 2018, with the headings Distance in km and Year started. What unit is the "
         "distance column in, and how far does Train C run? Answer: kilometres, and Train C runs 3,412 km.",
         "Card 2 (practice values): on the same board, which train runs the longest distance, how much longer is it "
         "than the shortest, and what is the difference between Train A and Train D? Answer: Train C, 3,412 km. The shortest "
         "is Train B, 1,978 km, and 3,412 − 1,978 = 1,434 km. Train A and Train D: 2,865 − 2,149 = 716 km.",
         "Card 3 (practice values): on the same board, a guard was 30 years old when Train D started in 2018. In which "
         "year was the guard born? Answer: 2018 − 30 = 1988.",
         "Card 4 (practice values): a bus stand board shows tickets printed and passengers who came: stand P 14,320 "
         "printed and 14,095 came, stand Q 9,850 printed and 10,240 came, stand R 21,730 printed and 21,050 came. For each "
         "stand say whether the tickets were sufficient and how many were short or extra. Answer: stand P: sufficient, 225 "
         "extra (14,320 − 14,095). Stand Q: not sufficient, 390 short (10,240 − 9,850). Stand R: sufficient, 680 extra "
         "(21,730 − 21,050).",
         "Challenge: 'Priyanka Mohite is the first Indian woman to climb five Himalayan peaks above 8,000 metres. "
         "Read the table and answer the questions that follow. (a): Which is the highest peak she climbed? (b): What is the "
         "difference in height between the highest and lowest peaks she has climbed, as per the table? (c): What is the "
         "difference between heights of Mount Elbrus and Mount Kanchenjunga? (d): If Priyanka was 20 years old when she "
         "summited Mount Everest in 2013, in which year was she born?' The board shows the book's table of seven mountains: "
         "Mount Kanchenjunga 8,586 metres in 2022, Mount Everest 8,848 in 2013, Mount Makalu 8,485 in 2019, Mount Lhotse "
         "8,516 in 2018, Mount Kilimanjaro 5,895 in 2016, Mount Elbrus 5,642 in 2017 and Mount Annapurna I 8,091 in 2021. "
         "Answer: (a): Mount Everest; (b): 8,848 − 5,642 = 3,206 metres; (c): 8,586 − 5,642 = 2,944 metres; (d): 2013 − 20 = "
         "1993.",
         "Challenge: 'For each district, find out if the number of certificates were sufficient? If insufficient, "
         "calculate how many certificates fell short. If extra, calculate how many certificates were in excess.' The board "
         "shows the book's table of three districts with the certificates printed and the students attended: Chittoor, A.P. "
         "18,225 and 18,104; Jaunpur, U.P. 19,043 and 19,265; Raigad, Maharashtra 20,863 and 19,974. Answer: Chittoor: "
         "sufficient, 121 extra (18,225 − 18,104). Jaunpur: not sufficient, 222 short (19,265 − 19,043). Raigad: sufficient, "
         "889 extra (20,863 − 19,974)."],
        ["Tapping a row and a heading lights the cell where they meet and the tool says what it is, for example: Train C, "
         "Distance in km: 3,412.",
         "Tapping two numbers of one column fills the compare strip with the bigger first, for example 3,412 − 1,978 = ___, and "
         "the tool says: To find how much more, subtract the smaller from the bigger.",
         "A wrong difference shows a soft amber note, for example: Did you take the smaller from the bigger? 3,412 is more than "
         "1,978. The tool names the number it expected only after the second try.",
         "For printed against came, the tool says what the comparison means, for example: 9,850 tickets for 10,240 people. "
         "There are fewer tickets than people, so the tickets are not sufficient, and the difference is how many are short.",
         "For a year from an age the strip shows the year and the age with the note: Take the age from the year. A finished "
         "question shows a green tick, the answer in large type and a check by adding, for example 1,978 + 1,434 = 3,412."],
        "The four play cards are done and the book's two tables, the mountains and the certificates, are read and every part "
        "of both questions is answered.",
        ["tableShown", "focusRow", "focusColumn", "comparedValues", "differenceBox", "answerCards", "challengeIndex"],
        ["M_SMALL_FROM_BIG"],
        ["Which row is the thing you want, and which column is the fact? Look where they meet.",
         "To compare, find the two numbers in the same column. Which is bigger? To find how much more, subtract the smaller "
         "from the bigger.",
         "For sufficient, short or extra: put the printed number and the number who came side by side. If the printed number "
         "is less, the difference is how many are short, and if it is more, the difference is how many are extra.",
         "For Train C and Train B the tool puts 3,412 and 1,978 in the compare strip and writes the difference, 1,434 km."]),
}
