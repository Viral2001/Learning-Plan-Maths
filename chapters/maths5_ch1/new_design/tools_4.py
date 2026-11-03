# -*- coding: utf-8 -*-
"""Tool specs 7 and 8 of Class 5 Chapter 1, We the Travellers - I: Puzzle Lab (the book's three pastime puzzles) and the
King's Horses Challenge (the square stable). Specs only; the tool screens are built later. Every tool follows the shared
rules of the priority doc: one activity at a time, one instruction at a time, large controls, Back and Next in the same
place, visible progress, simple restart, immediate specific feedback, hints, retry and reset. Three phases per tool:
recall and get ready, play and apply, challenge (the book's own question, unchanged)."""
from topics_common import T

TOOLS = {
    "puzzle_lab": T(
        "tool_puzzle_lab", "Puzzle Lab", "manipulative",
        "Play the book's three pastime puzzles with their exact rules and find the thinking that wins each one: the "
        "safe pairs in the river, the equal piles in the pebbles game, and the table of 9 in Mira's digits.",
        "A warm, colourful, polished educational-game scene: a compact hub on a small isometric table inside a train "
        "compartment, with three large door cards, River Crossing, Pile of Pebbles and Fun Puzzle (digits), soft shadows, "
        "gentle animation and no clutter. One door opens one scene at a time, and the puzzle board is always the largest "
        "thing on screen. "
        "River Crossing: a river with a near bank and a far bank, a boat for the boatman and one thing, and a large lion, "
        "sheep and bundle of grass that the student taps to put in the boat. Controls: Cross (the boat moves), Undo, "
        "Reset. Read-outs: a trip counter (Trips), the names of who is on each bank, and a Safe or Not safe banner for "
        "the bank the boatman has just left. "
        "Pile of Pebbles: two large piles of pebbles drawn as stacks, with a pile size choice of 1, 2, 3 or 7 pebbles in "
        "each pile (1, 2 and 3 are practice games, 7 is the book's game). The student taps pebbles on one pile to choose "
        "how many to take and the chosen pebbles lift. Controls: Take, Who plays first (You or Computer), Undo, Reset. "
        "The computer partner plays any allowed move. Read-outs: Your turn or Computer's turn, and the number of pebbles "
        "in each pile. "
        "Fun Puzzle (digits): two digit slots with tiles 1 to 9, and a rule note that the two digits must be different. "
        "Controls: Make numbers (shows the two 2-digit numbers), Subtract (shows the bigger number minus the smaller "
        "number and the difference), Use these digits (feeds the two digits of the difference into the slots for the "
        "next round), Undo, Reset. Read-outs: a growing list of every round, and a stamp when one digit is left. "
        "On every scene: Hint, Back and Next in the same place, progress dots and a Restart button.",
        ["Phase 1, Recall and get ready: each door card shows one small picture and one question from the videos, which "
         "pair can be left alone on a bank, what stays the same after the second player's move, and what is common in "
         "the differences. The student taps an answer to open the door.",
         "Phase 2, Play and apply: the student moves the lion, sheep and grass into the boat and across the river and "
         "watches the Safe or Not safe banner, plays small piles of pebbles against the computer, and runs Mira's steps "
         "on digits of their own choice while reading each difference.",
         "Phase 3, Challenge: the student solves each puzzle exactly as the book gives it: the river crossing with the "
         "lion, sheep and grass in the fewest trips, the two piles of 7 pebbles played so that they win, and Mira's "
         "process with the digits 3 and 7, then digits whose numbers differ by 27."],
        ["Phase 2, river: tick the pairs that can be left alone on a bank: lion and sheep, sheep and grass, lion and "
         "grass. Answer: only the lion and the grass.",
         "Phase 2, river: make the first crossing so that nothing is eaten. Answer: take the sheep across, because the "
         "lion and the grass can stay together.",
         "Phase 2, pebbles: choose 2 pebbles in each pile and let the computer play first. Whatever the computer takes "
         "from one pile, take the same number from the other pile. Answer: you take the last pebble and win.",
         "Phase 2, digits: choose the digits 1 and 6, then press Make numbers, Subtract and Use these digits until one "
         "digit is left. Answer: 61 − 16 = 45, then 54 − 45 = 9.",
         "Phase 3, river: How can the boatman take the lion, sheep, and grass across the river? Help him so that he can "
         "ferry the lion, sheep, and grass across the river safely, and in the minimum number of trips. Answer: 7 trips: "
         "take the sheep across, go back alone, take the lion across, bring the sheep back, take the grass across, go "
         "back alone, take the sheep across.",
         "Phase 3, pebbles: There are two piles of pebbles. Each pile contains 7 pebbles. Each player can pick as many "
         "pebbles they want from either of the piles. The player who picks the last pebble wins. Try this game with "
         "your friends. Now, how do you play so that you win? Answer: let the other player go first, and whatever they "
         "take from one pile, take the same number from the other pile. You take the last pebble.",
         "Phase 3, Mira's puzzle: take any two different digits, make two 2-digit numbers using them, subtract the "
         "smaller number from the bigger number, then use the two digits in the difference and repeat until you get a "
         "1-digit number. Start with the digits 3 and 7. Then find different digits such that the difference between "
         "the numbers is 27. Answer: 73 − 37 = 36, 63 − 36 = 27, 72 − 27 = 45, 54 − 45 = 9. Digits that differ by 3 "
         "give 27, for example 1 and 4 with 41 − 14 = 27."],
        ["In the river scene a move that leaves the sheep with the lion or with the grass on a bank without the "
         "boatman makes the two shake and says which one eats which, then the boat goes back to where it was.",
         "A move that tries to put two things in the boat is refused with the message that the boat takes one thing at "
         "a time.",
         "In the pebbles scene every move is shown as the piles before and after, and the piles glow green when they "
         "are equal after the student's move.",
         "In the digits scene each round shows the two numbers, the difference of the numbers and the difference of "
         "the digits in two different colours, and a difference in the table of 9 glows.",
         "Two equal digits are turned back with a note that the digits must be different."],
        "Every card is done: the river is solved in 7 trips, a game of 7 and 7 pebbles is won, and Mira's process has "
        "been run on the digits 3 and 7 and on digits whose numbers differ by 27.",
        ["door", "bank", "trips", "piles", "turn", "digits", "differences", "cardIndex"],
        ["M_RIVER_BOTH", "M_DIGIT_DIFF"],
        ["What are the rules of this puzzle, and what must you find: a safe order, a winning way to play, or the number "
         "at the end?",
         "Look for what must be true: which pairs can stay alone, what stays the same after a move, or what the "
         "differences have in common.",
         "River: only the lion and the grass can stay alone together, so the sheep goes first. Pebbles: take the same "
         "number from the other pile as the other player took. Digits: write each difference and look at the table of "
         "9.",
         "The tool shows the next move itself, the sheep crossing, the copying move in the pebbles, or the next round of "
         "subtractions, and then gives a similar card."]),

    "kings_horses": T(
        "tool_kings_horses", "King's Horses Challenge", "manipulative",
        "Place horse tokens in the square stable and see that counting 5 along each side counts every corner horse "
        "twice, so the number of horses is 20 minus the horses in the corner stalls.",
        "A warm, colourful, polished educational-game scene: the square royal stable of 12 stalls on a soft isometric "
        "courtyard with soft shadows and gentle animation, the largest thing on screen. The 4 corner stalls are shaded in "
        "a different colour from the 8 edge stalls. Each stall shows its horses as large dots and a number. Controls: tap "
        "a stall, then + to add a horse or − to remove one (or drag a horse token from the tray), Check, Undo, Reset, "
        "Hint. Read-outs: four side counters, one beside each side (Top, Right, Bottom, Left), each adding the 4 stalls "
        "on its side and turning green when it reads 5; a total counter, Horses in the stable, that counts every horse "
        "once; a Count one by one button that lights each horse in turn with a running count; and a target card above "
        "the stable. A horse placed in a corner stall lights both of its sides. Before the stable, a small practice "
        "picture (a practice value, not from the book) shows 12 children in a ring around a square, 4 on each side; "
        "tapping a corner child lights its two sides. On every scene: Back and Next in the same place, progress dots and "
        "a Restart button.",
        ["Phase 1, Recall and get ready: a small ring of 12 children stands around a square, 4 on each side. The student "
         "taps a corner child to see two sides light up and says why adding the four sides gives more than 12.",
         "Phase 2, Play and apply: the student places horse tokens in the stalls, watches the four side counters and "
         "the total, copies the caretaker's arrangement from the story, counts the horses one by one, and makes "
         "arrangements with no horse in any corner stall.",
         "Phase 3, Challenge: the student arranges the 18 horses with 5 on each side, then tries fewer horses and finds "
         "how many more horses the thief can steal before the king notices something is wrong."],
        ["Phase 2, corner stall: put one horse in the top left corner stall and nowhere else. Which side counters change, "
         "and what does the total show? Answer: the Top and Left counters both show 1, but the total shows only 1 "
         "horse.",
         "Phase 2, the caretaker's stable: place the horses as the caretaker did: top row 1, 2, 2, 0; the two middle "
         "stalls on the left 1 and 3; the two middle stalls on the right 2 and 3; bottom row 0, 2, 3, 0. Read the four "
         "side counters and the total. Answer: every side shows 5 and the total is 19.",
         "Phase 2, count one by one: press Count one by one on the caretaker's stable. Answer: 1 + 2 + 2 + 0 + 1 + 3 + "
         "2 + 3 + 0 + 2 + 3 + 0 = 19 horses, not 20.",
         "Phase 2, no corner horses: put no horse in any corner stall and make every side show 5. How many horses are "
         "there? Answer: 20, because no horse is counted twice.",
         "Phase 3, the 18 horses: The following night, the thief stole another horse from the stable. Now, only 18 horses "
         "remained. The caretaker once again cleverly arranged the 18 horses, so that there were 5 horses on each side "
         "of the square stable. How do you think he was able to do it? Arrange the 18 horses in the stable with 5 on "
         "each side. Answer: 1 horse in the top left and 1 horse in the bottom right corner stall, and 2 horses in each "
         "of the 8 middle stalls. Every side shows 5 and 1 + 1 + 8 × 2 = 18. Other arrangements can work too.",
         "Phase 3, how many more: How many more horses can the thief steal before the king notices something is wrong? "
         "Try making the arrangements yourself. Answer: the horses = 20 − the horses in the corner stalls. With one "
         "horse in each corner stall there are 16 horses, so 2 more after the 18. Taking more means crowding the corner "
         "stalls, which the king would notice."],
        ["A horse placed in a corner stall lights both of its sides and raises both side counters by 1, while the total "
         "goes up by 1 only.",
         "A side counter that reads 5 turns green. The total counter shows the real number of horses, each horse counted "
         "once.",
         "Count one by one lights each horse in turn, so the student can compare the 4 sides added together with the real "
         "number of horses.",
         "A side that does not read 5 shows how many horses it still needs, and Check says which side is short."],
        "Every card is done: the caretaker's stable counted as 19, an arrangement of 18 horses with 5 on each side, and "
        "the number of horses the thief can still steal found.",
        ["stalls", "sideCounts", "total", "cornerHorses", "cardIndex"],
        ["M_CORNER_TWICE"],
        ["How many sides does the stall you are filling touch?",
         "Add the four side counters, then take away the horses that were counted twice, the horses in the corner "
         "stalls.",
         "For 18 horses: 20 − 18 = 2, so two horses must stand in corner stalls. Put one in the top left corner and one "
         "in the bottom right corner, then fill the other stalls so that every side adds to 5.",
         "The tool places 1 horse in the top left and 1 in the bottom right corner stall and 2 horses in each of the 8 "
         "middle stalls. Every side adds to 5 and the total is 18. Then a similar card follows."]),
}
