# -*- coding: utf-8 -*-
"""Tool specs for T1, T2 and T3 of Class 5 Chapter 4 (We the Travellers - II): Balance the Sums (the free try of the
intro, right after the hook), Fuel Tank Adder and Fuel Gauge Subtractor. Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One
activity at a time, one instruction at a time, large controls, Back and Next in the same place, visible progress,
Hint, Retry and Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "balance_sums": T(
        "tool_balance_sums", "Balance the Sums", "manipulative",
        "Swap one card from each tray and watch both sums change by the same amount in opposite ways, so the gap closes by "
        "twice the difference of the two cards, then make two sums equal in the fewest moves. This is the free first try of "
        "the chapter, so it asks and shows; the video that follows names the idea.",
        "The back seat of the car on Nazrana's road trip, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. A fold-down tray holds two paper trays side by side, Group 1 on the left and Group 2 on the right, and "
        "they are the largest things on screen. Each tray holds number cards written on small slips of paper, four cards in "
        "each tray for the book's puzzles. Under each tray is a live sum read-out in large type. Between the trays a gap bar "
        "shows how far apart the two sums are, with the gap written as a number, for example Gap 2. An instruction strip at "
        "the top shows one sentence in large type, with progress dots under it. A moves counter shows the swaps used so far "
        "and a Fewest moves badge lights up when the student has used the least number of swaps. Controls: tap one card in "
        "each tray to select it (the chosen cards glow orange), then press Swap, or drag a card onto a card of the other "
        "tray; Undo takes back the last swap; Check; Hint; Retry (returns the cards of this puzzle); Reset (restores all "
        "trays); Back and Next in the same places on every card. Read-outs: the two sums, the gap, the moves counter, and a "
        "card number out of 5.",
        ["Look at Nazrana's two groups of cards from the story, 1, 2, 7, 9 and 3, 4, 5, 9, "
         "with the sums 19 and 21. Say which group has the bigger sum, then press Next.",
         "Swap two cards of your choice and read both sums and the gap, find the one swap that makes "
         "two sums equal, then find the two swaps needed when one swap is not enough.",
         "The book's own four puzzles with the least number of moves: make the sums of the two groups "
         "equal."],
        ["Card 1 (practice values): Group 1 is 3, 5, 9 and Group 2 is 4, 6, 11. Swap the 5 and the 6 and read both "
         "sums. Answer: Group 1 becomes 3 + 6 + 9 = 18 and Group 2 becomes 4 + 5 + 11 = 20. Group 1 went up by 1, Group 2 went "
         "down by 1, and the gap shrank from 4 to 2.",
         "Card 2 (practice values): the same groups, with the sums 17 and 21. Find the one swap that makes both sums "
         "equal. Answer: swap 9 and 11, because 11 − 9 = 2 is half of the gap 4. Both sums become 19, because 3 + 5 + 11 = 19 "
         "and 4 + 6 + 9 = 19.",
         "Card 3 (practice values): Group 1 is 4, 9, 13, 17 with the sum 43 and Group 2 is 6, 10, 15, 20 with the sum "
         "51. No single swap works, so find two. Answer: the gap is 8, half of it is 4, and no two cards differ by 4. For "
         "example swap 4 and 6, and swap 13 and 15, which differ by 2 and 2. Both sums become 47. Your swaps may differ.",
         "Challenge: 'In each of the following, there are two groups of numbers. Look carefully at the numbers in "
         "each group and their sums. Interchange pairs of numbers between the two groups to make their sums equal. Try to do "
         "this using the least number of moves.' (a) 1, 2, 7, 9 and 3, 4, 5, 9 (b) 5, 7, 12, 15 and 9, 11, 13, 14. Answer: "
         "(a) swap 2 and 3, both sums are 20, 1 move. (b) swap 5 and 9, or 7 and 11, both sums are 43, 1 move.",
         "Challenge: the same instructions for (c) 11, 15, 19, 23 and 13, 17, 21, 25, and (d) 77, 78, 79, 80 and 81, "
         "82, 83, 84. Answer: (c) 2 moves, for example 11 with 13 and 15 with 17, both sums are 72. (d) 2 moves, for example "
         "77 with 81 and 78 with 82, both sums are 322. Your swaps may differ."],
        ["Pressing Swap moves the two cards and updates both sums and the gap at once. The tool says what happened, for "
         "example: After the swap the left sum is 22 and the right sum is 18. The gap grew from 2 to 4. A swap that closes the "
         "gap says: The gap closed from 4 to 2.",
         "When the two sums are equal the tool says: Both sums are 20. You used 1 move. If a shorter way exists the Fewest "
         "moves badge stays dim and the tool says: Can you do it with fewer moves?",
         "On a card where one swap cannot work, a soft amber note appears after the second try: No two cards differ by half "
         "of the gap. Try two swaps.",
         "A swap that makes the gap bigger is never marked wrong: the tool shows the new gap and offers Undo.",
         "Open answers (a different pair that also works) are accepted; the tool says: This pair works too."],
        "Card 1 to card 3 are done, and the four puzzles (a) to (d) are solved with their fewest number of moves.",
        ["trayGroup1", "trayGroup2", "selectedCards", "movesUsed", "gapValue", "fewestMovesBadge", "challengeIndex"],
        ["M_SWAP_ONE_SUM", "M_SWAP_BIGGEST"],
        ["Which group has the bigger sum? Look at the two sums and the gap bar between the trays.",
         "A swap moves one card each way. Which way must the bigger card go to bring the sums closer?",
         "The gap closes by twice the difference of the two cards. Find two cards, one in each tray, that differ by half of "
         "the gap.",
         "For the first puzzle the gap is 2, so look for two cards that differ by 1: the 2 and the 3. The tool swaps them for "
         "you and both sums show 20."]),

    "fuel_tank_adder": T(
        "tool_fuel_tank_adder", "Fuel Tank Adder", "manipulative",
        "Add two numbers on a place value chart, regrouping 10 ones as 1 ten and 10 tens as 1 hundred, and see an easier way "
        "to add a number just below a round number.",
        "A fuel station on the road trip, drawn as a warm 3D isometric scene with soft shadows and gentle animation. The "
        "pump's display is a large chart with three columns, Hundreds, Tens and Ones, and it is the largest thing on screen. "
        "The two numbers sit in two rows of the chart, one above the other, with each digit shown as fuel tokens: ones as "
        "small drops, tens as bars, hundreds as tanks. A carry row above the chart is empty at first, and an answer row below "
        "is empty. An instruction strip at the top shows one sentence in large type, with progress dots under it. Beside the "
        "chart is a small number line for the easier way, showing a long hop to the round number and a short hop back. "
        "Controls: tap Add the ones to slide the ones drops down into the answer row; when there are 10 or more, tap "
        "Regroup 10 ones as 1 ten and watch ten drops merge into one bar that moves to the carry row of the Tens column; the "
        "same for the tens; type the digit that results in each answer box; on the cards with an easier way, tap Hop to the "
        "round number and Take back; Check; Hint; Undo; Retry (clears the answer row of this sum); Reset (restores the "
        "chart); Back and Next in the same places on every card. Read-outs: the digit sum of each column (for example 8 + 5 = "
        "13), the carry, and the whole sum in large type when finished, and a card number out of 7.",
        ["Look at the chart from the video with 67 and 58 and the ones about to be regrouped. "
         "Say how many ones there are altogether, then press Next.",
         "Build sums on the chart and regroup when a place makes 10 or more, add a number just below "
         "a round number with the hop and the take back, and add a sum that needs no regrouping.",
         "The book's own fuel questions and the six pairs, using the chart or an easier way."],
        ["Card 1 (practice values): add 47 and 36 on the chart. Answer: ones 7 + 6 = 13, write 3 and regroup 10 ones "
         "as 1 ten; tens 4 + 3 + 1 = 8; the sum is 83.",
         "Card 2 (practice values): add 285 and 167 on the chart. Answer: ones 5 + 7 = 12, write 2 and regroup; tens "
         "8 + 6 + 1 = 15, write 5 and regroup 10 tens as 1 hundred; hundreds 2 + 1 + 1 = 4; the sum is 452.",
         "Card 3 (practice values): add 64 and 95 on the chart. Answer: ones 4 + 5 = 9, no regrouping; tens 6 + 9 = "
         "15, write 5 and regroup 10 tens as 1 hundred; the sum is 159.",
         "Card 4 (practice values): add 72 and 98 with the easier way. Answer: 98 is 2 less than 100, so 72 + 100 = "
         "172 and take 2 back: 172 − 2 = 170.",
         "Card 5 (practice values): add 213 and 124 on the chart. Answer: no place makes 10 or more, so no "
         "regrouping: 3 + 4 = 7, 1 + 2 = 3, 2 + 1 = 3, and the sum is 337.",
         "Challenge: 'A lorry has 28 litres of fuel in its tank. An additional 75 litres is filled. What is the "
         "total quantity of fuel in the lorry?' and 'Let us try one more. Find the sum of 49 and 89.' Answer: 28 + 75 = 103 "
         "litres (ones 8 + 5 = 13, tens 2 + 7 + 1 = 10, 1 hundred) and 49 + 89 = 138 (ones 9 + 9 = 18, tens 4 + 8 + 1 = 13).",
         "Challenge: 'Add the following numbers. Wherever possible, find easier ways to add the pairs of numbers. (a) "
         "15 + 79 (b) 46 + 99 (c) 38 + 35 (d) 5 + 89 (e) 76 + 28 (f) 69 + 20' Answer: (a) 94 (b) 145 (c) 73 (d) 94 (e) 104 "
         "(f) 89. Easier ways: 79 is 1 less than 80, 99 is 1 less than 100, 28 is 2 less than 30, 20 is 2 tens."],
        ["Each column shows its own sum and the tool says what to do, for example: 8 ones and 5 ones make 13 ones: write 3 "
         "ones and regroup 10 ones as 1 ten.",
         "When ten drops are ready the Regroup button glows; if a column has fewer than 10 the tool says: There are only 7 "
         "ones, no regrouping is needed.",
         "A wrong digit shows a soft amber note, for example: The tens make 12 tens, so write 2 and regroup 10 tens as 1 "
         "hundred. The tool names the digit it expected only after the second try.",
         "On a card with an easier way the hop appears on the number line and the tool says: 98 is 2 less than 100, so add 100 "
         "and take 2 back.",
         "A finished sum shows a green tick, the whole sum in large type, and a quick check such as 47 + 36 = 40 + 30 + 7 + 6."],
        "The five play cards are done and the book's fuel questions and the six pairs are answered with the chart or an easier "
        "way.",
        ["topNumber", "bottomNumber", "carryRow", "answerRow", "regroupDone", "hopLine", "challengeIndex"],
        ["M_NO_CARRY", "M_FORGET_ONE"],
        ["Which place do you add first? Look at the ones column.",
         "How many ones are there altogether? Can you make a ten from them?",
         "Add the two ones digits. If the total is 10 or more, regroup: write the extra ones and carry 1 ten to the next column.",
         "For 47 + 36 the ones make 13. The tool writes 3 in the ones place and moves 1 ten to the carry row, and then the "
         "tens make 4 + 3 + 1 = 8."]),

    "fuel_gauge_subtractor": T(
        "tool_fuel_gauge_subtractor", "Fuel Gauge Subtractor", "manipulative",
        "Subtract on a place value chart, regrouping 1 ten as 10 ones when there are too few ones, and check a subtraction by "
        "adding the answer to the smaller number.",
        "The fuel gauge of a minibus on the road trip, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. A large chart with two columns, Tens and Ones, is the largest thing on screen. The bigger number sits on "
        "top and the smaller number below it, with each digit shown as fuel tokens: tens as bars and ones as small drops. A "
        "regroup row above the chart is empty at first and an answer row below is empty. To the right a round fuel gauge has "
        "a needle that moves from the smaller reading to the bigger reading, and under the chart a Check by adding strip "
        "holds a sentence with a blank, for example 18 + ___ = 65. An instruction strip at the top shows one sentence in "
        "large type, with progress dots under it. Controls: tap Regroup 1 ten as 10 ones when the top ones are fewer than the "
        "bottom ones and watch one bar break into ten drops that join the ones; tap Take away to remove the bottom tokens; "
        "type each digit of the answer; tap Check by adding to fill the strip and move the gauge needle; Check; Hint; Undo; "
        "Retry (clears the answer row); Reset (restores the chart); Back and Next in the same places on every card. "
        "Read-outs: the ones sum after regrouping (for example 12 ones), the tens left, the difference in large type, and a "
        "card number out of 6.",
        ["Look at the chart from the video for 72 − 38, where 2 ones cannot lose 8 ones. Say "
         "what you can do about it, then press Next.",
         "Subtract with a regroup, subtract with no regroup, check by adding and watch the gauge, then "
         "write the sentences that follow from one sentence.",
         "The book's own fuel gauge question, the difference between 82 and 37 and the eight subtractions."],
        ["Card 1 (practice values): subtract 46 from 83 on the chart. Answer: ones 3 is less than 6, so regroup 1 ten "
         "as 10 ones, 13 − 6 = 7; tens 7 − 4 = 3; the difference is 37.",
         "Card 2 (practice values): subtract 35 from 79. Answer: no regrouping, ones 9 − 5 = 4 and tens 7 − 3 = 4; "
         "the difference is 44.",
         "Card 3 (practice values): subtract 27 from 60, then press Check by adding. Answer: ones 0 is less than 7, "
         "so regroup, 10 − 7 = 3; tens 5 − 2 = 3; the difference is 33, and 27 + 33 = 60 fills the strip.",
         "Card 4 (practice values): fill the sentences that follow from 52 + 29 = 81: 81 − 29 = ___ and 81 − 52 = "
         "___. Answer: 81 − 29 = 52 and 81 − 52 = 29, because the whole minus a part is the other part.",
         "Challenge: 'A minibus has 18 litres of fuel left. After refuelling, the fuel meter indicates 65 litres. "
         "How much fuel has been filled in the fuel tank of the minibus?' with 'Check if 18 + 47 = 65?', and 'What is the "
         "difference between 82 and 37? Check your answer. Is 37 + ___ = 82?' Answer: 65 − 18 = 47 litres, and 18 + 47 = 65; "
         "82 − 37 = 45, and 37 + 45 = 82.",
         "Challenge: the eight subtractions (a) 57 − 11 (b) 23 − 19 (c) 49 − 21 (d) 56 − 18 (e) 93 − 35 (f) 84 − 23 "
         "(g) 70 − 43 (h) 65 − 47. Answer: (a) 46 (b) 4 (c) 28 (d) 38 (e) 58 (f) 61 (g) 27 (h) 18."],
        ["When the top ones are fewer, the tool says what is happening, for example: 2 ones are fewer than 8 ones: regroup 1 "
         "ten as 10 ones, now there are 12 ones, then 12 − 8 = 4.",
         "A wrong digit shows a soft amber note, for example: Take the smaller digit from the bigger digit? In a column the top "
         "digit is the one you start with. The tool names the digit it expected only after the second try.",
         "Check by adding fills the strip and moves the gauge: 18 + 47 = 65. If the sum is not the bigger number the gauge stops "
         "short and the tool says: The check does not match. Look at the ones again.",
         "In the sentences card a correct sentence locks in with a soft chime and the other two numbers of the whole and "
         "parts light up.",
         "A finished subtraction shows a green tick, the difference in large type and the check sentence."],
        "The four play cards are done and the fuel gauge question, the difference between 82 and 37 and the eight subtractions "
        "are answered and checked by adding.",
        ["topNumber", "bottomNumber", "regroupRow", "answerRow", "checkStrip", "gaugeNeedle", "challengeIndex"],
        ["M_SMALL_FROM_BIG", "M_UNRELATED"],
        ["Which number is on top? Compare the top ones digit with the bottom ones digit.",
         "Are there enough ones to take away? If not, what can you break up to get more ones?",
         "Regroup 1 ten as 10 ones: the tens go down by 1 and the ones go up by 10. Then subtract the ones, then the tens.",
         "For 83 − 46 the tool regroups for you: 13 ones take away 6 ones is 7, and 7 tens take away 4 tens is 3, so the "
         "difference is 37. Check: 46 + 37 = 83."]),
}
