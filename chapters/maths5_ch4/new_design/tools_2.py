# -*- coding: utf-8 -*-
"""Tool specs for T4 and T5 of Class 5 Chapter 4 (We the Travellers - II): Consecutive Sums Lab and Line Up and Solve.
Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One activity at a
time, one instruction at a time, large controls, Back and Next in the same place, visible progress, Hint, Retry and Reset
always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "consecutive_sums_lab": T(
        "tool_consecutive_sums_lab", "Consecutive Sums Lab", "manipulative",
        "Choose how many consecutive numbers to add and where to start, and see every sum, whether it is even or odd, the "
        "difference between successive sums, and the pairs from the two ends that make the same total.",
        "A row of milestones along the road trip, drawn as a warm 3D isometric scene with soft shadows and gentle animation. "
        "Each milestone is a stone with a number on it, and the long row of stones is the largest thing on screen. A window "
        "of 2 to 6 lit stones glows orange and slides along the row. Under the row is a table of sums, one line for each "
        "start of the window, with the sum in large type, an even or odd tag beside it and the difference to the line above "
        "in a small strip between the lines. An instruction strip at the top shows one sentence in large type, with progress "
        "dots under it. Controls: a stepper for how many numbers are lit (2 to 6); a stepper for the first number; a Next "
        "start button that moves the window by one stone and adds a line to the table; a Show pairs toggle that draws "
        "arrows joining the first and last lit stones, then the second and second from last, and so on, each arrow marked "
        "with its total, and shows the middle stone alone when there is one; answer cards for even or odd and for the "
        "difference; Check; Hint; Retry (clears the answers of this card); Reset (returns the window to its first place); "
        "Back and Next in the same places on every card. Read-outs: the lit numbers added, the sum, the difference between "
        "successive sums, the pair totals, and a card number out of 7.",
        ["Look at the window of 3 lit stones from the video with the sums 33, 36 and 39. Say "
         "what happens to the sum when the window moves one stone, then press Next.",
         "Slide the window for runs of 3, 5 and 6 numbers and read the differences, look at the "
         "even and odd tags for runs of 2 and 4 numbers, then use Show pairs to add a run without adding one by one.",
         "The book's own boxes of sums, its three questions about them and its four sums to find "
         "without adding directly."],
        ["Card 1 (practice values): set 3 numbers and start at 20, then press Next start three times. What is the "
         "difference between successive sums? Answer: the sums are 63, 66, 69 and 72, and the difference is 3 each time, "
         "because each of the 3 numbers goes up by 1.",
         "Card 2 (practice values): set 5 numbers and start at 30, then 6 numbers and start at 30. Answer: 5 numbers: "
         "the sums 160 and 165 differ by 5. 6 numbers: the sums 195 and 201 differ by 6. The difference is the number of "
         "numbers added.",
         "Card 3 (practice values): set 2 numbers and start at 60, then 4 numbers and start at 60, and read the "
         "tags. Answer: 2 numbers give the sums 121, 123 and 125, all odd. 4 numbers give the sums 246, 250 and 254, all "
         "even.",
         "Card 4 (practice values): set 5 numbers and start at 70 and press Show pairs. Answer: 70 + 74 = 144 and "
         "71 + 73 = 144, the middle number is 72, and the sum is 144 + 144 + 72 = 360, which is 5 × 72.",
         "Card 5 (practice values): find 83 + 84 + 85 + 86 without adding one by one. Answer: 83 + 86 = 169 and 84 + "
         "85 = 169, so the sum is 169 + 169 = 338.",
         "Challenge: 'In each of the boxes above, state whether the sums are even or odd. Explain why this is "
         "happening.' 'What is the difference between two successive sums in each box? Is it the same throughout?' 'What "
         "will be the difference between two successive sums for (a) 5 consecutive numbers (b) 6 consecutive numbers' The "
         "boxes show the sums of 2 consecutive numbers 3, 5, 7, 9, of 3 consecutive numbers 6, 9, 12, 15 and of 4 "
         "consecutive numbers 10, 14, 18, 22. Answer: box 1 all odd, box 2 even and odd in turn, box 3 all even; the "
         "differences are 2, 3 and 4, the same throughout each box; for 5 and 6 numbers the differences are 5 and 6.",
         "Challenge: 'Notice how the sums of 3, 4, and 5 consecutive numbers are related to the numbers being "
         "added. Use your understanding to find the following sums without adding the numbers directly. (a) 67 + 68 + 69 (b) "
         "24 + 25 + 26 + 27 (c) 48 + 49 + 50 + 51 + 52 (d) 237 + 238 + 239 + 240 + 241 + 242' Answer: (a) 204 (b) 102 (c) 250 "
         "(d) 1,437, by pairing the ends."],
        ["Each Next start line adds the new sum and the difference to the table, and the tool says what changed, for example: "
         "The sum went from 63 to 66. Each of the 3 numbers went up by 1, so the sum went up by 3.",
         "The even or odd tag appears beside each sum. A wrong answer card slides back with a clue such as: Look at one pair "
         "of consecutive numbers. Is it odd plus even?",
         "Show pairs draws the arrows and writes each pair total, for example: 70 + 74 = 144 and 71 + 73 = 144. The pairs "
         "make the same total.",
         "A wrong sum shows a soft amber note, for example: Did you add the pair totals? The tool names the number it "
         "expected only after the second try.",
         "Open explanations (why the sums are even or odd) are built from cards and are never marked wrong: the tool says "
         "Your words may differ."],
        "The five play cards are done and the book's three questions about the boxes and its four sums are answered.",
        ["runLength", "firstNumber", "windowPosition", "sumTable", "showPairs", "answerCards", "challengeIndex"],
        ["M_CONSEC_PARITY", "M_SUCC_DIFF_ONE", "M_FIRST_TIMES"],
        ["How many numbers are lit? Look at the stepper and the table under the row.",
         "When the window moves one stone, what happens to each lit number? What does that do to the sum?",
         "Each number goes up by 1, so the sum goes up by the number of lit stones. Find that difference in the table.",
         "For 3 lit stones the difference is 3. The tool writes 63, 66, 69, 72 and marks the difference 3 between each pair "
         "of lines."]),

    "line_up_and_solve": T(
        "tool_line_up_and_solve", "Line Up and Solve", "manipulative",
        "Line up the digits of two numbers with different numbers of digits, ones under ones, tens under tens and so on, "
        "and then add or subtract one place at a time with regroup marks, up to 5 digits.",
        "A toll plaza board on the road trip, drawn as a warm 3D isometric scene with soft shadows and gentle animation. A "
        "large plain board with five columns of equal width is the largest thing on screen. A small dot marks the right "
        "edge of the Ones column and no place names are written at first. A row of digit tiles 0 to 9 sits under the "
        "board, and the plus or minus sign tile sits on the left of the second number. A regroup row above the board holds "
        "small marks and an answer row below is empty. An instruction strip at the top shows one sentence in large type, "
        "with progress dots under it. Controls: drag the digits of each number onto the board; tap a column to put a "
        "regroup mark above the next place; type each answer digit; a Show place names toggle that writes ten thousands, "
        "thousands, hundreds, tens and ones above the columns and is off at first; Check; Hint; Undo; Retry (clears the board "
        "for this question); Reset (restores the tiles); Back and Next in the same places on every card. Read-outs: the "
        "column being worked, the digit sum or difference of that column, and the whole answer in large type when "
        "finished, and a card number out of 6.",
        ["Look at the board from the video with 536 and 87 lined up, the 7 under the 6. Say "
         "which digit of 87 sits under the 3, then press Next.",
         "Place the digits of numbers with different lengths and add them, then subtract across a "
         "zero and subtract a number with fewer digits.",
         "The book's own sums and subtractions with the digits aligned and no place names."],
        ["Card 1 (practice values): place the digits of 481 and 56 and add. Answer: the 6 goes under the 1 and the 5 "
         "under the 8. Ones: 1 + 6 = 7. Tens: 8 + 5 = 13, write 3 and regroup. Hundreds: 4 + 1 = 5. The sum is 537.",
         "Card 2 (practice values): place the digits of 7,258 and 14,963 and add. Answer: ones 8 + 3 = 11, write 1 "
         "and regroup; tens 5 + 6 + 1 = 12, write 2 and regroup; hundreds 2 + 9 + 1 = 12, write 2 and regroup; thousands "
         "7 + 4 + 1 = 12, write 2 and regroup; ten thousands 0 + 1 + 1 = 2. The sum is 22,221.",
         "Card 3 (practice values): place the digits of 8,305 and 2,467 and subtract. Answer: ones 5 is less than 7 "
         "and the tens digit is 0, so regroup across: ones 15 − 7 = 8, tens 9 − 6 = 3, hundreds 12 − 4 = 8, thousands 7 − "
         "2 = 5. The difference is 5,838.",
         "Card 4 (practice values): place the digits of 9,640 and 640 and subtract. Answer: the digits of 640 sit "
         "under the hundreds, tens and ones, and the thousands column has nothing under it. Ones 0 − 0 = 0, tens 4 − 4 = 0, "
         "hundreds 6 − 6 = 0, thousands 9. The difference is 9,000.",
         "Challenge: 'Find the following sums. Try not to write ten thousands, thousands, hundreds, tens and ones at the top. Just align the "
         "digits properly, at least for the smaller numbers. (a) 238 + 367 (b) 1,234 + 12,345 (c) 12 + 123 (d) 46,120 + "
         "12,890 (e) 878 + 8,789 (f) 1,749 + 17,490' Answer: (a) 605 (b) 13,579 (c) 135 (d) 59,010 (e) 9,667 (f) 19,239.",
         "Challenge: 'Subtract the following. Try not to write ten thousands, thousands, hundreds, tens and ones at the top. Align the digits "
         "carefully. (a) 4,578 − 2,222 (b) 15,324 − 11,780 (c) 5,423 − 423 (d) 123 − 12 (e) 77,777 − 777 (f) 826 − 752' "
         "Answer: (a) 2,356 (b) 3,544 (c) 5,000 (d) 111 (e) 77,000 (f) 74."],
        ["A digit dropped in the wrong column shows a soft amber note that names the digit, for example: The 2 of 12 belongs "
         "in the Tens column. Ones go under ones. The tool never moves the digit for the student.",
         "When the digits are lined up the board shows a thin guide through every column, and the tool says: Ones under "
         "ones, tens under tens. Now work from the right.",
         "Each column shows its own result as the student works, for example: 8 + 3 = 11: write 1 and regroup 10 ones as 1 "
         "ten.",
         "A wrong answer digit shows a soft amber note such as: Check the tens again, there is a regroup mark. The tool "
         "names the digit it expected only after the second try.",
         "A finished question shows a green tick, the whole answer in large type and a quick check, for example 537 − 56 = "
         "481."],
        "The four play cards are done and the book's six sums and six subtractions are lined up and solved without place "
        "names.",
        ["boardDigits", "firstNumber", "secondNumber", "operation", "regroupMarks", "answerRow", "showPlaceNames",
         "challengeIndex"],
        ["M_MISALIGN", "M_NO_CARRY", "M_SMALL_FROM_BIG"],
        ["Where is the ones digit of each number? Look at the right end of each number.",
         "Line up the ones digits first. Then the tens digits go next to them on the left.",
         "Put each digit of the shorter number under the matching place of the longer number, starting from the right. Empty "
         "places stay empty.",
         "For 481 and 56 the tool slides the 6 under the 1 and the 5 under the 8, and the hundreds column of 56 stays empty."]),
}
