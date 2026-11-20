# -*- coding: utf-8 -*-
"""Tool specs for T7, T9 and T10 of Class 5 Chapter 4 (We the Travellers - II): Round Number Hops, Number Grid Puzzle and
Pairs and Leftovers. Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One activity at a
time, one instruction at a time, large controls, Back and Next in the same place, visible progress, Hint, Retry and Reset
always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "round_number_hops": T(
        "tool_round_number_hops", "Round Number Hops", "manipulative",
        "Use a round number as a stepping stone: make nines and add 1 to find what to add to reach 100, 1,000 or 10,000, and "
        "take away 10 or 100 and add 1 to take away 9 or 99.",
        "A long straight road on the road trip with signposts for 100, 1,000 and 10,000, drawn as a warm 3D isometric scene "
        "with soft shadows and gentle animation. A number line runs along the road and is the largest thing on screen. The "
        "start number sits on a small marker on the line and a round target signpost stands ahead. A small car waits on the "
        "start marker and hops along the line. Beside the line is a digit partner panel: each digit of the start number sits "
        "above a box that shows the digit that makes 9 with it. An instruction strip at the top shows one sentence in large "
        "type, with progress dots under it. Controls: pick one of two modes, Make a round number or Take away 9 or 99; tap "
        "each digit to see its nine partner; tap Add 1 to hop one step to the round number; in the other mode tap Hop back "
        "10 or Hop back 100 and then Hop forward 1; type the answer in the blank; Check; Hint; Undo; Retry (clears the hops "
        "for this question); Reset (puts the car at the start); Back and Next in the same places on every card. Read-outs: "
        "the nine partners, the sum or difference after each hop (for example 99, then 100), the answer in large type when "
        "finished, and a card number out of 7.",
        ["Look at the road from the video with 46, its nine partner 53 and the extra hop of 1 "
         "to 100. Say which number is 1 less than 100, then press Next.",
         "Make 100, 1,000 and 10,000 from a number with the nines and the extra 1, and take away 9 "
         "and 99 by hopping back to the round number and forward by 1.",
         "The book's own blanks with the nines method and with the take away method."],
        ["Card 1 (practice values): make 100 from 63: 63 + ___ = 100. Answer: 6 needs 3 and 3 needs 6, so 63 + 36 = "
         "99, then add 1: 63 + 37 = 100.",
         "Card 2 (practice values): make 1,000 from 425: 425 + ___ = 1,000. Answer: 4 needs 5, 2 needs 7 and 5 needs "
         "4, so 425 + 574 = 999, then add 1: 425 + 575 = 1,000.",
         "Card 3 (practice values): make 10,000 from 6,284: 6,284 + ___ = 10,000. Answer: the nine partners are 3, 7, "
         "1 and 5, so 6,284 + 3,715 = 9,999, then add 1: 6,284 + 3,716 = 10,000.",
         "Card 4 (practice values): take away 9 from 84. Answer: hop back 10 to 74, then forward 1 to 75, so 84 − 9 "
         "= 75.",
         "Card 5 (practice values): take away 99 from 342. Answer: hop back 100 to 242, then forward 1 to 243, so "
         "342 − 99 = 243.",
         "Challenge: 'Sukanta likes the numbers 10, 100, 1,000, and 10,000. He wants to figure out what number he "
         "should add to a given number such that the sum is 100 or 1,000. Help him fill in the blank with an appropriate "
         "number.' (a) 32 + ___ = 100 (b) 59 + ___ = 100 (c) 877 + ___ = 1,000 and 666 + ___ = 1,000 (d) 4,103 + ___ = 10,000 "
         "and 5,555 + ___ = 10,000 (e) 180 + ___ = 1,000 (f) 760 + ___ = 1,000 (g) 400 + ___ = 1,000. Answer: (a) 68 (b) 41 (c) "
         "123 and 334 (d) 5,897 and 4,445 (e) 820 (f) 240 (g) 600.",
         "Challenge: 'Namita likes the number 9. She wants to subtract 9 or 99 from any number. Find a way to quickly "
         "subtract 9 or 99 from any number. (a) 67 − 9 (b) 83 − 9 (c) 144 − 9 (d) 187 − 99 (e) 247 − 99 (f) 763 − 99' and "
         "'(a) 32 − ___ = 9 (b) 56 − ___ = 9 (c) 877 − ___ = 99 (d) 666 − ___ = 99' Answer: (a) 58 (b) 74 (c) 135 (d) 88 (e) 148 "
         "(f) 664; the blanks are 23, 47, 778 and 567."],
        ["The digit partner panel lights each pair that makes 9, and the tool says what to do next, for example: 6 and 3 make "
         "9. So 63 + 36 = 99. One more makes 100.",
         "Each hop writes the result on the line, for example: 84 − 10 = 74, then 74 + 1 = 75. The tool says: 10 is 1 more than "
         "9, so give 1 back.",
         "A wrong answer shows a soft amber note, for example: 99 is 1 less than 100. Did you add the 1? The tool names the "
         "number it expected only after the second try.",
         "On a number that ends in 0 the tool says: The method still works. The last nine is 9, and adding 1 carries.",
         "A finished question shows a green tick, the answer in large type and the check, for example 63 + 37 = 100."],
        "The five play cards are done and the book's blanks with the nines method and the take away method are answered.",
        ["startNumber", "targetNumber", "mode", "nineDigits", "hopLog", "answerBlank", "challengeIndex"],
        ["M_NINES_ZERO", "M_FORGET_ONE"],
        ["Which round number are you hopping towards? Look at the signpost on the road.",
         "To reach the signpost, first make 9 in every place. What does each digit need to make 9?",
         "Write the nine partner of each digit. That gives the number that makes 99, 999 or 9,999. What is left to reach the "
         "round number?",
         "For 63 the partners are 3 and 6, so 63 + 36 = 99. Add the extra 1 to the blank, and 63 + 37 = 100."]),

    "number_grid_puzzle": T(
        "tool_number_grid_puzzle", "Number Grid Puzzle", "manipulative",
        "Place the numbers 1 to 9 in a 3 by 3 grid so that every row and every column follows its inc or dec arrow, by finding "
        "first where the smallest and the biggest number must go.",
        "A 3 by 3 floor of tiles in a railway waiting hall, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. The grid of nine large square tiles is the largest thing on screen. To the right of each row and under "
        "each column sits a small arrow plate with the word inc or dec, as in your maths book. A tray under the grid holds "
        "nine number plates, 1 to 9, one of each. An instruction strip at the top shows one sentence in large type, with "
        "progress dots under it. A rule checker lights the arrow plate of each row and column green when its numbers follow "
        "the arrow and soft amber when they break it. Controls: drag a plate into a cell and drag it out again; tap a plate "
        "to put it back in the tray; Check; Hint; Undo; Retry (clears the grid); Reset (returns all plates to the tray); Back "
        "and Next in the same places on every card. Read-outs: the plates left in the tray, which rows and columns are green "
        "or amber, and a card number out of 6. Rows are read left to right and columns top to bottom.",
        ["Look at the small grid from the video with 1 to 4 and every arrow inc. Say where 1 "
         "and 4 must go, then press Next.",
         "Fill a small grid whose rows and columns shrink, fill a 3 by 3 grid with the corners "
         "given, fill a grid whose rows grow and columns shrink, then repair a grid that has one row breaking its arrow.",
         "The book's own five grids."],
        ["Card 1 (practice values): fill a 2 by 2 grid with 1 to 4 so that every row and column decreases. Answer: 4 "
         "goes top left and 1 goes bottom right. For example the top row is 4, 3 and the bottom row is 2, 1.",
         "Card 2 (practice values): the tool puts 1 top left and 9 bottom right. Fill the rest of the 3 by 3 grid so "
         "that every row and column increases. Answer: for example 1, 2, 3 over 4, 5, 6 over 7, 8, 9 (many grids work).",
         "Card 3 (practice values): fill a 3 by 3 grid so that every row increases and every column decreases. "
         "Answer: the biggest number 9 goes top right and the smallest number 1 goes bottom left. For example 7, 8, 9 over 4, "
         "5, 6 over 1, 2, 3.",
         "Card 4 (practice values): the grid shows 1, 2, 3 over 4, 6, 5 over 7, 8, 9 with every arrow inc, and the "
         "middle row is amber. Swap two plates to repair it. Answer: swap the 6 and the 5, so the middle row is 4, 5, 6.",
         "Challenge: 'In a 3×3 grid, arrange the numbers 1 to 9 such that each row and each column has numbers in an "
         "increasing (inc) order. Each number should be used only once.' and 'This time, fill the grid such that each row and "
         "column has numbers in decreasing (dec) order.' Answer: for example 1, 2, 3 over 4, 5, 6 over 7, 8, 9 for inc, and 9, "
         "8, 7 over 6, 5, 4 over 3, 2, 1 for dec. Your grids may differ.",
         "Challenge: 'Now, fill the grids below with numbers (1 to 9) based on the inc (increasing) and dec "
         "(decreasing) conditions, as indicated below.' Grid 1: rows dec, dec, dec and columns inc, inc, inc. Grid 2: rows dec, "
         "dec, inc and columns dec, dec, inc. Grid 3: rows inc, inc, dec and columns inc, dec, dec. Answer: for example Grid 1 "
         "is 3, 2, 1 over 6, 5, 4 over 9, 8, 7; Grid 2 is 8, 6, 1 over 7, 5, 2 over 3, 4, 9; Grid 3 is 1, 6, 8 over 2, 5, 7 over "
         "9, 4, 3. Your grids may differ."],
        ["The rule checker lights each arrow plate as plates are placed, and the tool says what it found, for example: Row 2 "
         "should decrease, but 4 comes before 7. Swap them.",
         "A plate placed where it cannot work is never refused: the row and column turn soft amber and stay that way until "
         "they follow their arrows.",
         "Where do 1 and 9 go: the tool outlines the cell that is the smallest of its row and its column, and says: The "
         "smallest number must be at the end of a decreasing row and the start of an increasing column.",
         "A finished grid shows every arrow plate green, a tick and the grid read out as three rows.",
         "Different correct grids are all accepted; the tool says: This grid works too."],
        "The four play cards are done and the book's five grids are filled so that every row and column follows its arrow.",
        ["gridCells", "trayPlates", "arrowPlates", "checkerStatus", "challengeIndex"],
        ["M_GRID_ROWS_ONLY"],
        ["Which arrow plates are amber? Look at the rows and the columns.",
         "Where must the smallest number go? It must be the first of an increasing line and the last of a decreasing line.",
         "Place 1 and 9 first. Then fill each row so it follows its arrow, and check the columns.",
         "For all arrows inc the tool places 1 top left and 9 bottom right, and you fill the other seven plates."]),

    "pairs_and_leftovers": T(
        "tool_pairs_and_leftovers", "Pairs and Leftovers", "manipulative",
        "Arrange counters in pairs to decide whether a number is even or odd, and see what happens to the leftover counters "
        "when two numbers are added.",
        "A wooden board on a bench at a bus stand with round blue counters, drawn as a warm 3D isometric scene with soft "
        "shadows and gentle animation. The board shows a large drop zone for Group 1, one for Group 2 and a combine zone "
        "between them, and the counters in the zones are the largest things on screen. A counter group is arranged in two "
        "rows so that each counter in the top row is paired with the one below it; a counter with no partner is marked with "
        "a small orange ring. An instruction strip at the top shows one sentence in large type, with progress dots under it. "
        "Beside each group is its number in large type and an even or odd tag that appears after the student answers. "
        "Controls: a stepper for the number of counters in each group; tap Pair up to arrange a group in two rows; tap Add 2 "
        "to put one more pair in a group; tap Combine to join Group 1 and Group 2 in the combine zone; answer cards even and "
        "odd; Check; Hint; Retry (clears this card); Reset (restores the board); Back and Next in the same places on every "
        "card. Read-outs: the number in each group, the number of pairs, the number of leftover counters (0 or 1), the "
        "joined number, and a card number out of 7.",
        ["Look at the board from the video with 14 counters in 7 pairs and 15 counters in 7 pairs "
         "with 1 left over. Say which number has a leftover, then press Next.",
         "Pair up groups and tag them even or odd, add 2 to an even and an odd group, and combine "
         "two even groups, two odd groups, and an odd and an even group.",
         "The book's own questions about even numbers, the paired arrangements for 18 and 23, and the "
         "sums of pairs of numbers."],
        ["Card 1 (practice values): pair up 16 counters and then 21 counters. Answer: 16 makes 8 pairs with none left "
         "over, so it is even. 21 makes 10 pairs with 1 left over, so it is odd.",
         "Card 2 (practice values): pair up 10 and 17 and press Add 2. Answer: 10 becomes 12, from 5 pairs to 6 pairs, "
         "and nothing is left over. 17 becomes 19, from 8 pairs to 9 pairs, and the same 1 counter is left over.",
         "Card 3 (practice values): combine Group 1 with 6 counters and Group 2 with 10 counters. Answer: 6 + 10 = "
         "16, no leftover in either group, so the joined group has none and 16 is even.",
         "Card 4 (practice values): combine Group 1 with 11 counters and Group 2 with 15 counters. Answer: each "
         "group has 1 leftover. The two leftovers make one pair, so 11 + 15 = 26 has none left over and is even.",
         "Card 5 (practice values): combine Group 1 with 19 counters and Group 2 with 6 counters. Answer: only the "
         "group of 19 has a leftover, and it stays alone, so 19 + 6 = 25 has 1 left over and is odd.",
         "Challenge: 'Circle the numbers that are even.' (a) 297 (b) 498 (c) 724 (d) 100 (e) 199 (f) 789 (g) 49 (h) "
         "6,893 (i) 846 (j) 111 (k) 222 (l) 1,023, and 'Observe the given arrangement. Paired arrangement for 18. Paired "
         "arrangement for 23. Add 2 to 18. What changes or does not change in the arrangement? Add 2 to 23. What changes or "
         "does not change in the arrangement?' Answer: the even numbers are 498, 724, 100, 846 and 222. 18 goes from 9 pairs "
         "to 10 pairs and nothing is left over. 23 goes from 11 pairs to 12 pairs and 1 counter is still left over.",
         "Challenge: 'What do you notice about the sums in each of the following cases? Do you think it will be true "
         "for all pairs of such numbers? Explain your observations. You may use the paired arrangement to explain your "
         "thinking. (a) 12 and 6 are a pair of even numbers. Choose 5 such pairs of even numbers. Add the numbers in each of "
         "the pairs. (b) 13 and 9 are a pair of odd numbers. Choose 5 such pairs of odd numbers. Add the numbers in each of "
         "the pairs. (c) 7 and 12 are a pair of odd and even numbers. Choose 5 such pairs of odd and even numbers. Add the "
         "numbers in each of the pairs.' Answer: (a) every sum is even, (b) every sum is even, (c) every sum is odd, for all "
         "such pairs, because the leftovers decide. Your pairs may differ."],
        ["Pair up arranges the counters in two rows and rings a counter that has no partner, then says: 21 counters make 10 "
         "pairs and 1 is left over, so 21 is odd.",
         "Add 2 puts one more pair in the group and the tool says what changed and what did not, for example: One more pair. "
         "The leftover is still there, so the number is still odd.",
         "Combine joins the two groups and the leftover rings move together, for example: The two leftovers make one pair. "
         "Nothing is left over, so the sum is even.",
         "A wrong answer card slides back with a clue such as: Look for a ringed counter. Is one left over?",
         "Open answers (the pairs the student chooses and their words) are never marked wrong: the tool says Your pairs may "
         "differ, and checks only that each sum is read correctly."],
        "The five play cards are done and the book's questions about even numbers, the arrangements for 18 and 23 and the sums "
        "of pairs of numbers are answered.",
        ["group1Count", "group2Count", "pairedRows", "leftoverMarks", "combinedGroup", "answerCards", "challengeIndex"],
        ["M_ZERO_NOT_EVEN", "M_ODD_ODD_ODD"],
        ["Are the counters in pairs? Look for a counter with no partner.",
         "Pair up the counters. How many pairs are there, and is one counter left over?",
         "When two groups join, what happens to the leftover counters? Do they make a pair?",
         "For 11 and 15 each group has 1 leftover. The tool joins them into one pair, and 11 + 15 = 26 has nothing left over, "
         "so it is even."]),
}
