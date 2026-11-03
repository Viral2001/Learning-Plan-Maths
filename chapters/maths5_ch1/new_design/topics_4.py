# -*- coding: utf-8 -*-
"""Topics T12 to T14 (module M3) of Class 5 Chapter 1, We the Travellers - I: the Pastime Mathematics puzzles on the
train (river crossing, pile of pebbles, Mira's subtract and repeat puzzle), the King's Horses, and the chapter revision.

The three puzzle concepts present the book's exact puzzle and rules and teach the thinking tool with ONE worked example
of the plan's own (the safe pairs of the river, a small pile game of 2 and 2, Mira's digits 2 and 5). The book's full
answers belong to the Questions: they are the FIO items of the two DOERs."""
from __future__ import annotations

from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T12 Pastime Mathematics: Puzzles on the Train ===============================
TOPICS.append(TOPIC(
    "T12", "M3", "Pastime Mathematics: Puzzles on the Train", ["Pastime Mathematics"], "Analyze",
    "Students solve the river crossing puzzle in the fewest trips, win the pile of pebbles by playing small piles first, "
    "and explain why Mira's subtract and repeat puzzle always ends in 9.",
    "Puzzles train us to think logically and strategically. In the river puzzle the safe pairs decide the first "
    "crossing, in the pile of pebbles the small games show the winning plan, and in Mira's puzzle every difference is "
    "in the table of 9.",
    [A("T12.C1", "River Crossing Puzzle", "Analyze",
       "Students list which pairs the boatman can leave alone on a bank, use the safe pair to find the first crossing, "
       "and explain why the sheep, which is in both unsafe pairs, has to cross first.",
       textbook=["Sanju and Mira are traveling on a train. To pass time, they challenge each other with games and "
                 "puzzles.",
                 "Mira poses the river crossing puzzle to Sanju.",
                 "A boatman wants to cross a river in a boat. He has to take a lion, a sheep, and a bundle of grass with "
                 "him. He can take one of them at a time. If the sheep and grass are left on the shore, the sheep will "
                 "eat the grass. And, if the sheep and lion are left on the shore, the lion will eat the sheep."],
       teach=["Predict first: the boatman takes one thing at a time. Which one should he take first, so that nothing is "
              "eaten?",
              "Sanju and Mira use puzzles to pass the time on the train. A puzzle is solved by thinking, step by step, "
              "and puzzles like this train us to think logically and strategically.",
              "Start with the rules. Whatever the boatman takes across, the other two stay behind, so list the pairs "
              "that could be left alone.",
              "The lion and the sheep cannot stay together, and the sheep and the grass cannot stay together. The lion "
              "and the grass can.",
              "The sheep is in both pairs that cannot stay together, so it cannot be left behind with anything. The "
              "first crossing is forced.",
              "Rule: before you move anything, list which pairs are safe to leave alone, because the safe pairs decide "
              "your moves."],
       examples=[WE("The boatman has a lion, a sheep and a bundle of grass. Which pairs can he leave alone on a bank, and "
                    "what does that tell us about his first crossing?",
                    ["The boat takes one thing at a time, so every crossing leaves two things behind on the bank.",
                     "List the three pairs he could leave behind: lion and sheep, sheep and grass, lion and grass.",
                     "Lion and sheep: the lion eats the sheep, so this pair cannot be left alone.",
                     "Sheep and grass: the sheep eats the grass, so this pair cannot be left alone.",
                     "Lion and grass: nothing in the rules is eaten, so this pair can be left alone.",
                     "If he takes the lion first, the sheep and the grass are left behind. That is not allowed. If he "
                     "takes the grass first, the lion and the sheep are left behind. That is not allowed either.",
                     "If he takes the sheep first, the lion and the grass are left behind, which is allowed. So the "
                     "first crossing is forced: the sheep goes first."],
                    "Only the lion and the grass can be left alone, so the sheep must cross first")],
       key_terms=["pair", "safe", "trip"], misconceptions=["M_RIVER_BOTH"],
       ncert=["pm.intro", "note.puzzles"], minutes=7),
     A("T12.C2", "Pile of Pebbles", "Analyze",
       "Students play small piles of pebbles such as 2 and 2, write every move of both players, and say what stays the "
       "same after the second player's move.",
       textbook=["Sanju introduces a game called pile of pebbles to Mira.",
                 "There are two piles of pebbles. Each pile contains 7 pebbles. Each player can pick as many pebbles "
                 "they want from either of the piles. The player who picks the last pebble wins.",
                 "Try this game with your friends. Now, how do you play so that you win?",
                 "To find a winning strategy, try playing with 1 pebble in each pile, two in each, three in each, and so "
                 "on."],
       teach=["Predict first: two piles have 2 pebbles each, and you play second. Can you always win?",
              "In one turn a player picks as many pebbles as they want from one pile. The player who picks the last "
              "pebble wins.",
              "A big game is hard to see, so play the smallest game first. With 1 and 1, your friend takes 1 pebble and "
              "you take the last one.",
              "Now play 2 and 2. Write every move your friend can make and your answer to it. In both cases you take "
              "the last pebble.",
              "Rule: when a game is big, play the small game first, write every move, and look for what stays the "
              "same."],
       examples=[WE("Two piles have 2 pebbles each. You play second. Write every first move your friend can make and "
                    "your answer to it. Who wins, and what stays the same?",
                    ["Start with 2 and 2. Your friend can take 2 pebbles from one pile, or take 1 pebble from one pile.",
                     "If your friend takes 2 from one pile, the piles are 0 and 2.",
                     "You take the 2 pebbles of the other pile. The piles are 0 and 0. You took the last pebble and "
                     "win.",
                     "If your friend takes 1 from one pile, the piles are 1 and 2.",
                     "You take 1 from the pile of 2. The piles are 1 and 1.",
                     "Your friend must take 1 from a pile. The piles are 0 and 1.",
                     "You take the last pebble and win.",
                     "Look at the piles after each of your moves: 0 and 0, and 1 and 1. Both times the two piles were "
                     "equal."],
                    "With 2 and 2 the player who goes second wins every game, and after each move of that player the "
                    "two piles are equal")],
       key_terms=["strategy", "pile", "pebbles"], minutes=6),
     A("T12.C3", "Fun Puzzle: subtract and repeat", "Analyze",
       "Students follow Mira's subtract and repeat steps with a pair of digits they choose, write every step, and find "
       "what is common to all the differences.",
       textbook=["Now, it's Mira's turn. She gives a fun puzzle to Sanju with the following steps:",
                 "(a) Take any two different digits.",
                 "(b) Make two 2-digit numbers using them.",
                 "(c) Subtract the smaller number from the bigger number.",
                 "Now, use the two digits in the difference and repeat steps (b) and (c).",
                 "Continue this process until you get a 1-digit number. Even before everyone could finish, Mira "
                 "exclaimed, \"Mind you! No matter which two numbers you choose, you will get 9 in the end.\""],
       teach=["Predict first: take the digits 2 and 5 and follow Mira's steps. What do you think you will get at the end?",
              "Step (a): the digits are 2 and 5. Step (b): the numbers are 25 and 52. Step (c): 52 − 25 = 27.",
              "Repeat with the digits 2 and 7: 72 − 27 = 45. Repeat with 4 and 5: 54 − 45 = 9. We stop at a 1-digit "
              "number.",
              "Write every step in a row and look for what is common. The differences 27, 45 and 9 are all in the table "
              "of 9.",
              "Do not mix up two differences. The digits 2 and 5 differ by 3, but the numbers 25 and 52 differ by 27.",
              "Rule: when a puzzle repeats a step, write down every round and look for what stays the same."],
       examples=[WE("Follow Mira's steps with the digits 2 and 5. What do you get at the end, and what do you notice "
                    "about the differences?",
                    ["Take the digits 2 and 5. The two 2-digit numbers are 25 and 52.",
                     "Subtract the smaller from the bigger: 52 − 25 = 27.",
                     "Use the two digits of 27, which are 2 and 7. The numbers are 27 and 72, and 72 − 27 = 45.",
                     "Use the two digits of 45, which are 4 and 5. The numbers are 45 and 54, and 54 − 45 = 9.",
                     "9 has one digit, so we stop. The end is 9.",
                     "Look at the differences 27, 45 and 9. They are all in the table of 9: 27 = 9 × 3, 45 = 9 × 5 and "
                     "9 = 9 × 1.",
                     "The digits 2 and 5 differ by 3, because 5 − 2 = 3. The numbers 25 and 52 differ by 27. These are "
                     "two different differences."],
                    "52 − 25 = 27, 72 − 27 = 45, 54 − 45 = 9: the end is 9, and the differences are all in the table "
                    "of 9")],
       key_terms=["difference", "digits", "repeat"], misconceptions=["M_DIGIT_DIFF"],
       ncert=["pm.mira_steps"], minutes=8),
     DOER("T12.C4", "Practice: Puzzle Lab", "puzzle_lab", "Analyze",
          "Students solve the river crossing puzzle in the fewest trips, win the pile of pebbles, and explain why the "
          "differences in Mira's puzzle are in the table of 9 and the end is 9.",
          ["In the river puzzle, list which pairs can be left alone. The sheep is in both unsafe pairs, so it crosses "
           "first.",
           "In the pile of pebbles, play the small piles first and look for what stays the same after the second "
           "player's move.",
           "In Mira's puzzle, write every step. The differences are in the table of 9, and the end is 9."],
          items=[
              FIO("pm.river", "Pastime Mathematics (river crossing), Q1",
                  "A boatman wants to cross a river in a boat. He has to take a lion, a sheep, and a bundle of grass with "
                  "him. He can take one of them at a time. If the sheep and grass are left on the shore, the sheep will "
                  "eat the grass. And, if the sheep and lion are left on the shore, the lion will eat the sheep. How can "
                  "the boatman take the lion, sheep, and grass across the river? Help him so that he can ferry the lion, "
                  "sheep, and grass across the river safely, and in the minimum number of trips.",
                  ["Call the two banks the near bank and the far bank. At the start the lion, the sheep, the grass and the "
                   "boatman are on the near bank.",
                   "The boat takes one thing at a time. Only the lion and the grass can be left alone together.",
                   "Trip 1: take the sheep across. The lion and the grass stay on the near bank, which is safe. The sheep "
                   "is on the far bank.",
                   "Trip 2: go back alone. The sheep waits alone on the far bank.",
                   "Trip 3: take the lion across. The grass is alone on the near bank. The lion and the sheep are on the "
                   "far bank with the boatman.",
                   "Trip 4: bring the sheep back. The lion waits alone on the far bank. The sheep and the grass are on the "
                   "near bank with the boatman.",
                   "Trip 5: take the grass across. The sheep waits alone on the near bank. The lion and the grass are "
                   "together on the far bank, which is safe.",
                   "Trip 6: go back alone. The lion and the grass stay together on the far bank, which is safe.",
                   "Trip 7: take the sheep across. The lion, the sheep and the grass are all on the far bank.",
                   "Count the trips: 4 trips to the far bank and 3 trips back, and 4 + 3 = 7 trips.",
                   "Fewer trips do not work. After the sheep and the lion are both across, going back alone would leave "
                   "them together, so the sheep must come back once.",
                   "Check: in every trip the boatman left behind only the lion and the grass, or one thing alone. The "
                   "sheep was never left with the lion or with the grass."],
                  "7 trips: take the sheep across, go back alone, take the lion across, bring the sheep back, take the "
                  "grass across, go back alone, take the sheep across",
                  kind="prompt",
                  q_figure="A river with two banks: the lion, the sheep and a bundle of grass on the left bank, a small "
                           "boat with the boatman on the water, and an empty right bank.",
                  s_figure="Seven small pictures of the river, one after each trip, showing who stands on the left bank "
                           "and who on the right bank, with the boat on the side where the trip ends."),
              FIO("pm.pebbles", "Pastime Mathematics (pile of pebbles), Q2",
                  "There are two piles of pebbles. Each pile contains 7 pebbles. Each player can pick as many pebbles "
                  "they want from either of the piles. The player who picks the last pebble wins. Try this game with "
                  "your friends. Now, how do you play so that you win? To find a winning strategy, try playing with 1 "
                  "pebble in each pile, two in each, three in each, and so on.",
                  ["Let your friend play first. You play second. In one turn a player takes pebbles from one pile.",
                   "The plan: whatever number of pebbles your friend takes from one pile, take the same number from the "
                   "other pile.",
                   "Start with 7 and 7. Your friend takes 3 from the first pile: the piles are 4 and 7.",
                   "You take 3 from the second pile: the piles are 4 and 4.",
                   "Your friend takes 1 from the second pile: the piles are 4 and 3.",
                   "You take 1 from the first pile: the piles are 3 and 3.",
                   "Your friend takes 3 from the first pile: the piles are 0 and 3.",
                   "You take 3 from the second pile: the piles are 0 and 0. You took the last pebble and you win.",
                   "Why it works: after each of your moves the two piles are equal (4 and 4, 3 and 3, 0 and 0). Your "
                   "friend takes from only one pile, so your friend can never empty both piles at once.",
                   "Check with small piles: with 1 and 1, your friend takes 1 and you take the last one. With 2 and 2 and "
                   "with 3 and 3 the same copying wins."],
                  "Let your friend play first. Whatever your friend takes from one pile, take the same number from the "
                  "other pile. The piles stay equal and you take the last pebble",
                  kind="prompt",
                  q_figure="Two piles of pebbles side by side, each pile with 7 pebbles.",
                  s_figure="The two piles after each move of a sample game: 7 and 7, 4 and 7, 4 and 4, 4 and 3, 3 and 3, "
                           "0 and 3, 0 and 0."),
              FIO("pm.mira_process", "Pastime Mathematics (Mira's puzzle), Q3 the process",
                  "(a) Take any two different digits, for example 3 and 7. (b) Make two 2-digit numbers using them: 37 "
                  "and 73. (c) Subtract the smaller number from the bigger number: 73 − 37 = 36. Now, use the two digits "
                  "in the difference and repeat steps (b) and (c). Continue this process until you get a 1-digit number. "
                  "Write the whole process.",
                  ["Start with the digits 3 and 7. The numbers are 73 and 37, and 73 − 37 = 36.",
                   "Use the digits 3 and 6 of the difference. The numbers are 63 and 36.",
                   "63 − 36 = 27.",
                   "Use the digits 2 and 7. The numbers are 72 and 27.",
                   "72 − 27 = 45.",
                   "Use the digits 4 and 5. The numbers are 54 and 45.",
                   "54 − 45 = 9.",
                   "9 has one digit, so the process stops.",
                   "Check by adding back: 9 + 45 = 54, 45 + 27 = 72, 27 + 36 = 63 and 36 + 37 = 73."],
                  "73 − 37 = 36, 63 − 36 = 27, 72 − 27 = 45, 54 − 45 = 9. The process ends in 9",
                  kind="example",
                  q_figure="The three steps of Mira's puzzle in a row, with the example beside them: the digits 3 and 7, "
                           "the numbers 37 and 73, and the first subtraction 73 − 37 = 36.",
                  s_figure="The four subtractions of the whole process written in columns and joined by arrows: 73 − 37 = "
                           "36, 63 − 36 = 27, 72 − 27 = 45, 54 − 45 = 9."),
              FIO("pm.mira_explore", "Pastime Mathematics (Mira's puzzle), Q3 explore (1) to (4)",
                  "How did Mira know what the 1-digit number in the end would be? Let us explore. (1) Observe the "
                  "differences you get in each step of the process for the digits 3 and 7: 36, 27, 45 and 9. Do you "
                  "notice anything in common? (2) Try the puzzle using any other pair of digits. What is common to these "
                  "differences? What do you get in the end? (3) What digits can you choose so that you get a 1-digit "
                  "number in the first step itself? Give some examples. Describe the pattern in the digits. (4) Now, "
                  "find different digits such that the difference between the numbers is 27.",
                  ["(1) Look at the four differences: 36, 27, 45 and 9.",
                   "36 = 9 × 4, 27 = 9 × 3, 45 = 9 × 5 and 9 = 9 × 1. All four are in the table of 9. That is what they "
                   "have in common.",
                   "(2) Try the digits 4 and 9. The numbers are 49 and 94, and 94 − 49 = 45.",
                   "Use the digits 4 and 5. The numbers are 45 and 54, and 54 − 45 = 9.",
                   "The difference 45 is in the table of 9, and the end is 9 again.",
                   "(3) A 1-digit number in the first step needs a difference of 9. Try 21 − 12 = 9, 32 − 23 = 9 and "
                   "54 − 45 = 9.",
                   "In each pair the digits are next to each other, like 1 and 2, 2 and 3, 4 and 5. They differ by 1.",
                   "(4) Try the digits 1 and 4. The numbers are 14 and 41, and 41 − 14 = 27.",
                   "Other pairs that differ by 3 also work. The digits 2 and 5: 52 − 25 = 27. The digits 3 and 6: 63 − 36 = 27. "
                   "The digits 4 and 7: 74 − 47 = 27. The digits 5 and 8: 85 − 58 = 27. The digits 6 and 9: "
                   "96 − 69 = 27.",
                   "Check: 41 − 14 = 27, and 4 − 1 = 3."],
                  "(1) all in the table of 9 (2) the digits 4 and 9 also end in 9, with differences in the table of 9 "
                  "(3) digits next to each other, such as 4 and 5 (4) digits that differ by 3, such as 1 and 4",
                  kind="prompt",
                  q_figure="Mira's process for the digits 3 and 7 in four columns joined by arrows: 73 − 37 = 36, 63 − 36 "
                           "= 27, 72 − 27 = 45, 54 − 45 = 9."),
              FIO("pm.mira_table", "Pastime Mathematics (Mira's puzzle), Q3 (5) the table",
                  "Mira found an interesting relationship between the two digits and the difference obtained. Can you see "
                  "it in the table that Mira made? Digits 3, 7: 7 − 3 = 4 and 73 − 37 = 36. Digits 1, 9: 9 − 1 = 8 and "
                  "91 − 19 = 72. Digits 2, 8: 8 − 2 = 6 and 82 − 28 = 54. Digits 4, 5: 5 − 4 = 1 and 54 − 45 = 9. Extend "
                  "this table by choosing appropriate digits so that the resulting differences are 2, 3, 5, and 7 "
                  "respectively. What do the differences between the digits indicate?",
                  ["Difference 2: choose the digits 1 and 3, because 3 − 1 = 2. Then 31 − 13 = 18.",
                   "Difference 3: choose the digits 1 and 4, because 4 − 1 = 3. Then 41 − 14 = 27.",
                   "Difference 5: choose the digits 1 and 6, because 6 − 1 = 5. Then 61 − 16 = 45.",
                   "Difference 7: choose the digits 1 and 8, because 8 − 1 = 7. Then 81 − 18 = 63.",
                   "Compare each digit difference with its number difference: 36 = 9 × 4, 72 = 9 × 8, 54 = 9 × 6 and "
                   "9 = 9 × 1.",
                   "The new rows agree: 18 = 9 × 2, 27 = 9 × 3, 45 = 9 × 5 and 63 = 9 × 7.",
                   "So the difference of the numbers is 9 times the difference of the digits.",
                   "Why: 73 has 4 more tens than 37, which is 40 more, but 4 fewer ones. So 40 − 4 = 36, and 36 = 9 × 4.",
                   "Check: the digits 4 and 5 differ by 1 and 54 − 45 = 9 = 9 × 1."],
                  "New rows: 1 and 3 give 18, 1 and 4 give 27, 1 and 6 give 45, 1 and 8 give 63. The difference of the "
                  "numbers is 9 times the difference of the digits",
                  kind="prompt",
                  q_figure="Mira's table with three columns: Digits, Differences in digits, and Difference in numbers "
                           "formed by the digits. Four rows are filled: 3, 7; 1, 9; 2, 8; 4, 5. Four empty rows follow, "
                           "marked for the digit differences 2, 3, 5 and 7.",
                  s_figure="Mira's table with the four new rows filled: 1, 3 with 3 − 1 = 2 and 31 − 13 = 18; 1, 4 with "
                           "4 − 1 = 3 and 41 − 14 = 27; 1, 6 with 6 − 1 = 5 and 61 − 16 = 45; 1, 8 with 8 − 1 = 7 and "
                           "81 − 18 = 63."),
              FIO("pm.mira_asks", "Pastime Mathematics (Mira's puzzle), Q3 three questions",
                  "List the numbers that give a 1-digit number in the third subtraction. Identify pairs of digits that "
                  "lead to the 1-digit number after the maximum possible number of subtractions. Compare your answers "
                  "with your friends.",
                  ["Use the digits 1 to 9, so that both numbers have 2 digits. Count the subtractions for each gap between "
                   "the digits.",
                   "Gap 1, such as 4 and 5: 54 − 45 = 9. That is 1 subtraction.",
                   "Gap 2, such as 1 and 3: 31 − 13 = 18, 81 − 18 = 63, 63 − 36 = 27, 72 − 27 = 45, 54 − 45 = 9. That is "
                   "5 subtractions.",
                   "Gap 3, such as 2 and 5: 52 − 25 = 27, 72 − 27 = 45, 54 − 45 = 9. That is 3 subtractions.",
                   "Gap 4, such as 3 and 7: 73 − 37 = 36, 63 − 36 = 27, 72 − 27 = 45, 54 − 45 = 9. That is 4 "
                   "subtractions.",
                   "Gap 5, such as 1 and 6: 61 − 16 = 45, 54 − 45 = 9. That is 2 subtractions. Gap 6, such as 1 and 7: "
                   "71 − 17 = 54, 54 − 45 = 9. That is 2 subtractions.",
                   "Gap 7, such as 1 and 8: 81 − 18 = 63, 63 − 36 = 27, 72 − 27 = 45, 54 − 45 = 9. That is 4 "
                   "subtractions.",
                   "Gap 8, such as 1 and 9: 91 − 19 = 72, 72 − 27 = 45, 54 − 45 = 9. That is 3 subtractions.",
                   "A 1-digit number comes in the third subtraction for gap 3 or gap 8. The pairs are 1 and 4, 2 and 5, "
                   "3 and 6, 4 and 7, 5 and 8, 6 and 9, and 1 and 9.",
                   "The numbers they make are 14 and 41, 25 and 52, 36 and 63, 47 and 74, 58 and 85, 69 and 96, and 19 "
                   "and 91.",
                   "The most subtractions is 5, for gap 2. The pairs are 1 and 3, 2 and 4, 3 and 5, 4 and 6, 5 and 7, 6 "
                   "and 8, 7 and 9.",
                   "Check with 2 and 4: 42 − 24 = 18, 81 − 18 = 63, 63 − 36 = 27, 72 − 27 = 45, 54 − 45 = 9. That is 5 "
                   "subtractions."],
                  "Third subtraction: digits that differ by 3 (1 and 4, 2 and 5, 3 and 6, 4 and 7, 5 and 8, 6 and 9) or "
                  "by 8 (1 and 9). Most subtractions, 5: digits that differ by 2 (1 and 3, 2 and 4, 3 and 5, 4 and 6, "
                  "5 and 7, 6 and 8, 7 and 9)",
                  kind="prompt")],
          misconceptions=["M_RIVER_BOTH", "M_DIGIT_DIFF"]),
     ],
    key_terms=["puzzle", "strategy", "difference"]))

# ============================== T13 King's Horses ==========================================================
TOPICS.append(TOPIC(
    "T13", "M3", "King's Horses", ["King's Horses"], "Analyze",
    "Students explain why 5 counted on each of the 4 sides of the stable does not give 20 horses, arrange 18 horses with "
    "5 on each side, and find how many more horses the thief can steal.",
    "Counting along the four sides counts every corner stall twice, so the horses are 20 minus the horses in the corner "
    "stalls. The caretaker's mistake, the 18 horses and the horses the thief can still steal all follow from this.",
    [A("T13.C1", "King's Horses: counting along the sides", "Analyze",
       "Students explain why counting along the four sides of a square counts each corner twice, and find the real total "
       "by subtracting the corner ones that were counted twice.",
       textbook=["Once upon a time, there was a king who was very fond of horses. He had 20 horses of the best breed. The "
                 "horses were kept in the royal stable, and cared for by a caretaker.",
                 "One night, a thief stole one of the horses. Fearing punishment, the caretaker arranged the horses in "
                 "the stable as shown in the picture here.",
                 "The next day, when the king came to check on the horses, the caretaker led him around the square "
                 "stable. \"Please count the number of horses along each side, your majesty,\" he said.",
                 "The king counted 5 horses along each side. \"We have 5 horses along each side and there are 4 sides. "
                 "So there are a total of 20 horses, your majesty,\" the caretaker explained.",
                 "Satisfied with the explanation, the king returned to his palace."],
       teach=["Predict first: 12 children stand around a square, 4 on each side, and the 4 corner children belong to two "
              "sides. Will 4 + 4 + 4 + 4 give the number of children?",
              "4 + 4 + 4 + 4 = 16, which is more than 12. Each corner child was counted on two sides, once for each "
              "side.",
              "There are 4 corners, so 4 children were counted twice. Take the extra counts away: 16 − 4 = 12.",
              "Rule: counting along the sides counts every corner twice, so the real number is the total of the sides "
              "minus the corner ones counted twice.",
              "Keep this rule in mind for the king's stable: a square stable has corners too."],
       examples=[WE("12 children stand around a square, 4 on each side, with one child at each corner. Sanju adds the four "
                    "side counts. What does he get, and why is it not 12?",
                    ["Each side has 4 children, counted from corner to corner.",
                     "Add the four sides: 4 + 4 + 4 + 4 = 16.",
                     "16 is more than 12, so some children were counted twice.",
                     "A corner child stands on two sides, so that child is counted once for each side.",
                     "There are 4 corner children, each counted twice, so there are 4 extra counts.",
                     "Take the extra counts away: 16 − 4 = 12.",
                     "Check by counting each child once: 4 corner children, and 2 children between the corners on each "
                     "side, 4 × 2 = 8. Then 4 + 8 = 12."],
                    "He gets 16, but there are only 12 children, because the 4 corner children are counted twice: "
                    "16 − 4 = 12")],
       key_terms=["corner", "counted twice", "side"], misconceptions=["M_CORNER_TWICE"],
       ncert=["kh.story"], minutes=6),
     DOER("T13.C2", "Practice: King's Horses Challenge", "kings_horses", "Analyze",
          "Students place the horses in the stable so that every side shows 5, count them one by one, and find how many "
          "more horses the thief can steal.",
          ["A horse in a corner stall is counted on two sides.",
           "The horses in the stable = 4 × 5 − the horses in the corner stalls.",
           "Count the horses one by one to check the total."],
          items=[
              FIO("kh.mistake", "King's Horses (the count), Q1",
                  "The king counted 5 horses along each side. \"We have 5 horses along each side and there are 4 sides. So "
                  "there are a total of 20 horses, your majesty,\" the caretaker explained. But wait, were there really "
                  "20 horses in the stable? Count the horses one by one and check! What was the mistake in the "
                  "caretaker's explanation?",
                  ["Count the top row from the left: 1 + 2 + 2 + 0 = 5.",
                   "Count the left side from the top corner down: 1 + 1 + 3 + 0 = 5.",
                   "Count the right side from the top corner down: 0 + 2 + 3 + 0 = 5.",
                   "Count the bottom row from the left: 0 + 2 + 3 + 0 = 5.",
                   "Every side shows 5, so the caretaker counted 4 × 5 = 20.",
                   "Now count the horses one by one, each stall once. Top row: 1 + 2 + 2 + 0 = 5. The two middle stalls on "
                   "the left: 1 + 3 = 4. The two middle stalls on the right: 2 + 3 = 5. Bottom row: 0 + 2 + 3 + 0 = 5.",
                   "Add the four groups: 5 + 4 + 5 + 5 = 19. There are 19 horses, not 20.",
                   "The mistake: the horse in the top left corner stall stands on two sides, the top and the left, so it "
                   "was counted twice.",
                   "Check: 4 × 5 − 1 = 19, with 1 corner horse counted twice."],
                  "There are 19 horses. The horse in the corner stall was counted on two sides, so 20 − 1 = 19",
                  kind="prompt",
                  q_figure="The square stable of 12 stalls with the horses as red dots: the top row has 1, 2, 2 and 0 "
                           "horses from the left; the two middle stalls on the left have 1 and 3; the two middle stalls "
                           "on the right have 2 and 3; the bottom row has 0, 2, 3 and 0.",
                  s_figure="The same stable with each side marked by a bracket showing 5, the top left corner stall "
                           "circled, and the total 19 written below."),
              FIO("kh.eighteen", "King's Horses (18 horses), Q2",
                  "The following night, the thief stole another horse from the stable. Now, only 18 horses remained. The "
                  "caretaker once again cleverly arranged the 18 horses, so that there were 5 horses on each side of the "
                  "square stable. How do you think he was able to do it? Arrange the 18 horses in the stable with 5 on "
                  "each side.",
                  ["The caretaker counted 5 on each of the 4 sides: 4 × 5 = 20 counts.",
                   "Only 18 horses stand there, so 20 − 18 = 2 counts are extra.",
                   "Each horse in a corner stall is counted twice, so exactly 2 horses must stand in corner stalls.",
                   "Put 1 horse in the top left corner stall and 1 horse in the bottom right corner stall. The other two "
                   "corner stalls stay empty.",
                   "Top side: the top left corner has 1, so the two middle stalls must hold 4. Put 2 in each: "
                   "1 + 2 + 2 + 0 = 5.",
                   "Right side: 0 + 2 + 2 + 1 = 5.",
                   "Bottom side: 1 + 2 + 2 + 0 = 5.",
                   "Left side: 0 + 2 + 2 + 1 = 5.",
                   "Count the horses one by one: 2 in the corners, and 8 middle stalls with 2 horses each, 8 × 2 = 16. "
                   "Then 2 + 16 = 18.",
                   "Check: 4 × 5 − 2 = 18, and every side shows 5."],
                  "Put 1 horse in the top left and 1 in the bottom right corner stall, and 2 horses in each of the 8 "
                  "middle stalls. Every side shows 5 and there are 18 horses. Your arrangement may differ",
                  kind="prompt",
                  q_figure="The empty square stable of 12 stalls: 4 stalls along the top, 4 along the bottom, and 2 stalls "
                           "in the middle on the left and on the right.",
                  s_figure="The stable with 1 horse in the top left corner stall, 1 horse in the bottom right corner "
                           "stall, 2 horses in each of the 8 middle stalls, each side marked 5 and the total 18 written "
                           "below."),
              FIO("kh.more", "King's Horses (how many more), Q3",
                  "How many more horses can the thief steal before the king notices something is wrong? Try making the "
                  "arrangements yourself.",
                  ["Counting 5 along each of the 4 sides gives 4 × 5 = 20 counts.",
                   "A horse in a corner stall is counted twice. So the number of horses = 20 − the horses in the corner "
                   "stalls.",
                   "19 horses need 20 − 19 = 1 corner horse. 18 horses need 20 − 18 = 2 corner horses.",
                   "Fewer horses need more corner horses. 17 horses need 20 − 17 = 3. 16 horses need 20 − 16 = 4, one in "
                   "each corner stall.",
                   "Try 16 horses with 1 horse in each corner stall. Each side already has 2 from its corners, so its two "
                   "middle stalls hold 5 − 2 = 3, for example 2 and 1.",
                   "Top side: 1 + 2 + 1 + 1 = 5. The other three sides are the same. The horses are 4 + 4 × 3, and "
                   "4 × 3 = 12, so 4 + 12 = 16.",
                   "From 18 horses to 16 horses the thief takes 18 − 16 = 2 more.",
                   "To keep 5 on every side with fewer than 16 horses, a corner stall must hold more than 1 horse. Put 3, "
                   "2, 3 and 2 horses in the four corner stalls and leave the middle stalls empty. Every side shows "
                   "3 + 2 = 5 and there are 3 + 2 + 3 + 2 = 10 horses.",
                   "All the horses then crowd into the corners and the stalls between them are empty. The king would "
                   "notice. The book does not print a number for this, so this is one way to read the question.",
                   "Check: 20 − 4 = 16 with one horse in each corner stall, and 20 − 10 = 10 with the corner stalls "
                   "crowded."],
                  "2 more horses, leaving 16 with one horse in each corner stall (horses = 20 − the horses in the corner "
                  "stalls). Taking more means crowding the corner stalls, which the king would notice",
                  kind="prompt",
                  q_figure="Two empty square stables of 12 stalls each, side by side, for trying arrangements: 4 stalls "
                           "along the top, 4 along the bottom, and 2 in the middle on the left and on the right.",
                  s_figure="A stable with 1 horse in each corner stall and 2 and 1 horses in the two middle stalls of "
                           "every side, each side marked 5 and the total 16 written below.")],
          misconceptions=["M_CORNER_TWICE"]),
     ],
    key_terms=["corner", "side", "arrangement"]))

# ============================== T14 Chapter Revision (summary) =============================================
TOPICS.append(TOPIC(
    "T14", "M3", "Chapter Revision", ["Chapter summary"], "Understand",
    "",
    "The journey of the chapter: travel then and now, the new TTh place, reading, writing, comparing and swapping large "
    "numbers, expanded form, the nearest ten, hundred and thousand, distances and vehicles, large counts around us, "
    "the three puzzles on the train and the King's Horses.",
    [A("T14.C1", "Chapter Revision: We the Travellers - I", "Understand",
       "",
       teach=["Predict first: you have travelled through the whole chapter. Can you say one idea from each stop, from the "
              "first journey to the king's stable? Read the lines below and tick each idea you remembered.",
              "Journeys: long ago people travelled on foot, on animals, and by boats and sailing ships. Today we use "
              "bicycles, motorbikes, cars, buses, trains, ships and aeroplanes, and submarines and spacecraft too.",
              "Place value: 10 Ones make 1 Ten, 10 Tens make 1 Hundred, 10 Hundreds make 1 Thousand, and 10 Thousands "
              "make Ten Thousand. 9,000 + 1,000 = 10,000, written in a new column, TTh.",
              "Check: which new column did the chart gain for ten thousand? The TTh column. A comma helps us read large "
              "numbers.",
              "Reading and writing: say the thousands part first, then the rest, and keep every zero in its place. 10,010 "
              "is ten thousand ten, and forty thousand eight is 40,008, because 40,000 + 8 = 40,008.",
              "Check: write fifty thousand five in digits. It is 50,005, with zeros in the thousands, hundreds and tens "
              "places.",
              "Patterns: find the step between neighbouring numbers and test it on the next pair. 456, 567, 678 goes up "
              "by 111, because 567 − 456 = 111 and 678 − 567 = 111.",
              "Comparing: more digits means a greater number. 49,014 has 5 digits and 9,990 has 4 digits, so 49,014 is "
              "greater. With the same number of digits, compare from the left.",
              "Digit swap: swapping two digits changes the number. In 1,478, swapping 7 and 4 gives 1,748.",
              "Expanded form: 9,123 = 9 Thousands + 1 Hundred + 2 Tens + 3 Ones, and 983 = 90 Tens + 83 Ones.",
              "Check: 90 Tens is how many? It is 900, and 900 + 83 = 983.",
              "Nearest numbers: the nearest ten, hundred or thousand is the neighbour that needs the fewest jumps. For "
              "2,346, the nearest ten is 2,350, after 4 jumps.",
              "In an hour a person can generally travel 3 to 5 km on foot, 12 to 20 km by cycle, 40 to 60 km by "
              "motorbike and 750 to 920 km by aircraft. For many hours, take the distance in one hour times the number "
              "of hours.",
              "Large numbers around us: a book with about 200 pages, and about 50 words in each, has about 10,000 "
              "words, because 200 × 50 = 10,000.",
              "Check: 200 × 5 = 1,000. Is that a 4-digit or a 5-digit count? It is a 4-digit count.",
              "Puzzles: in the river puzzle, list the pairs that can be left alone, and the sheep crosses first. In the "
              "pile of pebbles, play small piles and look for what stays the same. In Mira's puzzle, write every step: "
              "the differences are all in the table of 9 and the end is 9.",
              "King's Horses: counting 5 on each of 4 sides counts every corner horse twice, so the horses = 4 × 5 − the "
              "horses in the corner stalls.",
              "Check: 12 children stand around a square, 4 on each side. 4 × 4 − 4 = 12. We take away 4 because each of "
              "the 4 corner children was counted twice."],
       ncert=["summary"], key_terms=["place value", "nearest", "puzzle"], minutes=6, enrichment=True)],
    topic_type="summary"))
