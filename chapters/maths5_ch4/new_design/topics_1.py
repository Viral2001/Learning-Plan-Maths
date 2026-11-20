# -*- coding: utf-8 -*-
"""Topics T1, T1B, T2 and T3 (module M1: Balancing Sums, Adding and Subtracting). The framing intro (Nazrana's number
cards hook and the free Balance the Sums tool), the short idea topic T1B (Swap to Balance with the four puzzles), Fuel
Arithmetic: Adding, and Subtraction and Its Link with Addition.
Every teaching concept has one worked example with the plan's own numbers (practice values); every book question is an
FIO item of its topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Making Sums Equal (framing) =============================================
# The framing topic holds only the hook video and the free-try tool, and no book question. The concept video and the
# four puzzles follow in the short idea topic T1B.
TOPICS.append(TOPIC(
    "T1", "M1", "Making Sums Equal", ["Chapter opening"], "Understand",
    "",
    "Nazrana and her friends write numbers on small pieces of paper and make two groups. One group adds up to 19 and "
    "the other to 21. Try the cards and find out if a swap can make both sums equal.",
    [A("T1.C1", "Nazrana's Number Cards", "Understand",
       "",
       textbook=["In each of the following, there are two groups of numbers. Look carefully at the numbers in each "
                 "group and their sums. Interchange pairs of numbers between the two groups to make their sums equal. "
                 "Try to do this using the least number of moves. You could write each number on a small piece of "
                 "paper."],
       teach=["Predict first: two groups of cards add up to 19 and 21. Can swapping just one card from each group make "
              "both groups add up to the same number?",
              "Nazrana and her friends are on a long road trip across India, starting from Delhi.",
              "To pass the time, they write numbers on small pieces of paper and make two groups.",
              "One group has the cards 1, 2, 7 and 9. Its cards add up to 19. The other group has the cards 3, 4, 5 and "
              "9. Its cards add up to 21.",
              "The friends want both groups to add up to the same number. They may swap a card of one group with a "
              "card of the other, and they want to use the fewest swaps.",
              "Which two cards should change places? Think about it, then try the cards on the next screen."],
       ncert=["open.intro"], key_terms=["sum", "group", "swap"],
       video_focus=["HOOK"], enrichment=True, minutes=4),
     DOER("T1.C3", "Balance the Sums: Explore", "balance_sums", "Understand",
          "",
          ["Nazrana and her friends write numbers on small pieces of paper and make two groups.",
           "One group adds up to 19 and the other group adds up to 21.",
           "Swap cards between the groups and watch both sums change."],
          misconceptions=["M_SWAP_ONE_SUM"], role="try_it", enrichment=True)],
    topic_type="framing", key_terms=["sum", "group", "swap"]))

# ============================== T1B Swap to Balance ========================================================
TOPICS.append(TOPIC(
    "T1B", "M1", "Swap to Balance", ["Chapter opening"], "Understand",
    "Students explain how swapping a pair of numbers between two groups changes both sums, and find the swaps that make "
    "the sums equal.",
    "When a smaller number and a bigger number change groups, one sum goes up and the other goes down by the same "
    "amount, so the gap closes by twice that amount. To make two sums equal, swap two numbers whose difference is half "
    "the gap.",
    [A("T1B.C1", "Swapping a Pair Changes Both Sums", "Understand",
       "Students find the swap that makes two groups add up to the same sum by working out half of the gap between the "
       "sums.",
       textbook=["Think what will happen to the sums if we interchange 2 and 5? Try interchanging other pairs of "
                 "numbers and find the one that will make the sums equal."],
       teach=["Predict first: group 1 is 2, 6 and 9, and group 2 is 4, 7 and 10. If you swap the 6 with the 7, which "
              "sum goes up, and by how much?",
              "The 7 comes into group 1 and the 6 goes out, so group 1 goes up by 7 − 6 = 1. The 6 goes into group 2 "
              "and the 7 goes out, so group 2 goes down by 1.",
              "One swap changes both sums, by the same amount, in opposite ways. The gap between the sums closes by "
              "twice that amount.",
              "Here the sums are 17 and 21, so the gap is 4. To close a gap of 4, the two numbers you swap must "
              "differ by 2, which is half of the gap.",
              "Look for a number in group 1 and a number in group 2 that differ by 2: the 2 and the 4. Swap them and "
              "both sums become 19.",
              "Rule: to make two sums equal with one swap, swap two numbers whose difference is half of the gap "
              "between the sums."],
       examples=[WE("Group 1 is 2, 6 and 9, and group 2 is 4, 7 and 10 (practice values). Make both groups add up to "
                    "the same sum with one swap.",
                    ["Group 1: 2 + 6 + 9 = 17. Group 2: 4 + 7 + 10 = 21.",
                     "The gap is 21 − 17 = 4. Half of the gap is 4 ÷ 2 = 2.",
                     "Look for a number of group 1 and a number of group 2 that differ by 2. The numbers 2 and 4 "
                     "differ by 2, because 4 − 2 = 2.",
                     "Swap the 2 and the 4. Group 1 is now 4, 6 and 9, and 4 + 6 + 9 = 19. Group 2 is now 2, 7 and "
                     "10, and 2 + 7 + 10 = 19.",
                     "A swap that does not work: swap 6 and 7. They differ by 1, so group 1 becomes 18 and group 2 "
                     "becomes 20, and the gap is still 2.",
                     "Check: group 1 went up by 2 and group 2 went down by 2, so the gap closed by 2 + 2 = 4."],
                    "Swap the 2 and the 4: both groups add up to 19")],
       ncert=["open.hint"], key_terms=["swap", "gap", "sum"],
       misconceptions=["M_SWAP_ONE_SUM", "M_SWAP_BIGGEST"], minutes=5),
     DOER("T1B.C2", "Practice: Making Sums Equal", None, "Understand",
          "Students make the sums of two groups equal in the fewest swaps and explain why one swap is sometimes not "
          "enough.",
          ["A swap changes both sums by the same amount, in opposite ways.",
           "The gap closes by twice the difference of the two swapped numbers.",
           "To close the gap with one swap, the difference must be half of the gap. If no pair has that difference, use "
           "two swaps."],
          items=[FIO("msq.a", "Making Sums Equal: puzzle (a)",
                     "In each of the following, there are two groups of numbers. Look carefully at the numbers in each "
                     "group and their sums. Interchange pairs of numbers between the two groups to make their sums "
                     "equal. Try to do this using the least number of moves. (a): Group 1: 1, 2, 7, 9 (sum 19). "
                     "Group 2: 3, 4, 5, 9 (sum 21).",
                     ["Group 1: 1 + 2 + 7 + 9 = 19. Group 2: 3 + 4 + 5 + 9 = 21. The gap is 21 − 19 = 2, and half of "
                      "the gap is 1.",
                      "The hint swaps 2 and 5. Then group 1 is 1 + 5 + 7 + 9 = 22 and group 2 is 3 + 4 + 2 + 9 = 18. "
                      "The gap grows to 4, so that swap is not the one.",
                      "We need a number of group 1 and a number of group 2 that differ by 1. Only 2 and 3 differ by 1.",
                      "Swap 2 and 3. Group 1 is now 1, 3, 7 and 9, and 1 + 3 + 7 + 9 = 20. Group 2 is now 2, 4, 5 and "
                      "9, and 2 + 4 + 5 + 9 = 20.",
                      "The sums were not equal to begin with, so one move is the fewest. Check: both sums are 20."],
                     "Swap 2 and 3: both groups add up to 20. This takes 1 move.",
                     kind="prompt",
                     q_figure="Two groups of number cards side by side. Group 1 has the cards 1, 2, 7 and 9 with the "
                              "sum 19, and group 2 has the cards 3, 4, 5 and 9 with the sum 21.",
                     s_figure="The same two groups after the swap of the cards 2 and 3, with the sums 20 and 20."),
                 FIO("msq.b", "Making Sums Equal: puzzle (b)",
                     "In each of the following, there are two groups of numbers. Look carefully at the numbers in each "
                     "group and their sums. Interchange pairs of numbers between the two groups to make their sums "
                     "equal. Try to do this using the least number of moves. (b): Group 1: 5, 7, 12, 15 (sum 39). "
                     "Group 2: 9, 11, 13, 14 (sum 47).",
                     ["Group 1: 5 + 7 + 12 + 15 = 39. Group 2: 9 + 11 + 13 + 14 = 47. The gap is 47 − 39 = 8, and half "
                      "of the gap is 4.",
                      "We need a number of group 1 and a number of group 2 that differ by 4. The pairs 5 and 9, and 7 "
                      "and 11, both differ by 4.",
                      "Swap 5 and 9. Group 1 is now 9, 7, 12 and 15, and 9 + 7 + 12 + 15 = 43. Group 2 is now 5, 11, "
                      "13 and 14, and 5 + 11 + 13 + 14 = 43.",
                      "The other pair works too: swapping 7 and 11 gives 5 + 11 + 12 + 15 = 43 and 9 + 7 + 13 + 14 = "
                      "43.",
                      "One move is the fewest. Check: both sums are 43."],
                     "Swap 5 and 9 (or 7 and 11): both groups add up to 43. This takes 1 move.",
                     kind="prompt",
                     q_figure="Two groups of number cards side by side. Group 1 has the cards 5, 7, 12 and 15 with the "
                              "sum 39, and group 2 has the cards 9, 11, 13 and 14 with the sum 47.",
                     s_figure="The same two groups after the swap of the cards 5 and 9, with the sums 43 and 43."),
                 FIO("msq.c", "Making Sums Equal: puzzle (c)",
                     "In each of the following, there are two groups of numbers. Look carefully at the numbers in each "
                     "group and their sums. Interchange pairs of numbers between the two groups to make their sums "
                     "equal. Try to do this using the least number of moves. (c): Group 1: 11, 15, 19, 23 (sum 68). "
                     "Group 2: 13, 17, 21, 25 (sum 76).",
                     ["Group 1: 11 + 15 + 19 + 23 = 68. Group 2: 13 + 17 + 21 + 25 = 76. The gap is 76 − 68 = 8, and "
                      "half of the gap is 4.",
                      "One swap needs two numbers that differ by 4. The pairs that differ by 2 are 11 and 13, 15 and "
                      "17, 19 and 21, and 23 and 25. Every other pair differs by 6 or more. No pair differs by 4, so "
                      "one swap is not enough.",
                      "Use two swaps that each differ by 2. Together they close the gap: 2 + 2 = 4, which is half of "
                      "the gap.",
                      "Swap 11 and 13, and swap 15 and 17. Group 1 is now 13, 17, 19 and 23, and 13 + 17 + 19 + 23 = "
                      "72. Group 2 is now 11, 15, 21 and 25, and 11 + 15 + 21 + 25 = 72.",
                      "Two moves are the fewest. Check: both sums are 72."],
                     "Sample answer: swap 11 and 13, and swap 15 and 17. Both groups add up to 72. This takes 2 moves. "
                     "Your answer may differ.",
                     kind="prompt",
                     q_figure="Two groups of number cards side by side. Group 1 has the cards 11, 15, 19 and 23 with the "
                              "sum 68, and group 2 has the cards 13, 17, 21 and 25 with the sum 76.",
                     s_figure="The same two groups after the swaps of 11 with 13 and of 15 with 17, with the sums 72 and "
                              "72."),
                 FIO("msq.d", "Making Sums Equal: puzzle (d)",
                     "In each of the following, there are two groups of numbers. Look carefully at the numbers in each "
                     "group and their sums. Interchange pairs of numbers between the two groups to make their sums "
                     "equal. Try to do this using the least number of moves. (d): Group 1: 77, 78, 79, 80 (sum 314). "
                     "Group 2: 81, 82, 83, 84 (sum 330).",
                     ["Group 1: 77 + 78 + 79 + 80 = 314. Group 2: 81 + 82 + 83 + 84 = 330. The gap is 330 − 314 = 16, "
                      "and half of the gap is 8.",
                      "The biggest difference between a number of group 1 and a number of group 2 is 84 − 77 = 7. That "
                      "is less than 8, so one swap is not enough.",
                      "Use two swaps whose differences add up to 8. Two swaps that each differ by 4 do it: 4 + 4 = 8.",
                      "Swap 77 and 81, which differ by 81 − 77 = 4, and swap 78 and 82, which differ by 82 − 78 = 4. "
                      "Group 1 is now 81, 82, 79 and 80, and 81 + 82 + 79 + 80 = 322. Group 2 is now 77, 78, 83 and "
                      "84, and 77 + 78 + 83 + 84 = 322.",
                      "Two moves are the fewest. Check: both sums are 322."],
                     "Sample answer: swap 77 and 81, and swap 78 and 82. Both groups add up to 322. This takes 2 "
                     "moves. Your answer may differ.",
                     kind="prompt",
                     q_figure="Two groups of number cards side by side. Group 1 has the cards 77, 78, 79 and 80 with the "
                              "sum 314, and group 2 has the cards 81, 82, 83 and 84 with the sum 330.",
                     s_figure="The same two groups after the swaps of 77 with 81 and of 78 with 82, with the sums 322 "
                              "and 322.")],
          misconceptions=["M_SWAP_ONE_SUM", "M_SWAP_BIGGEST"])],
    key_terms=["swap", "gap", "sum"]))

# ============================== T2 Fuel Arithmetic: Adding =================================================
TOPICS.append(TOPIC(
    "T2", "M1", "Fuel Arithmetic: Adding", ["Fuel Arithmetic", "Let Us Solve"], "Apply",
    "Students add two numbers with place value, regrouping when a place makes 10 or more, and find easier ways to add "
    "a number that is just below a ten or a hundred.",
    "To add with place value, add the ones, then the tens, then the hundreds, and regroup 10 of one place as 1 of the "
    "next place on the left. A number just below a round number can be added the easier way: add the round number, "
    "then take the extra back.",
    [A("T2.C1", "Adding with Place Value", "Apply",
       "Students add two numbers using place value and regroup 10 ones as 1 ten and 10 tens as 1 hundred.",
       textbook=["Different vehicles need different quantities of fuel. This quantity can vary from 5 to 15 litres in "
                 "the case of motorbikes, 15 to 50 litres in the case of cars, 150 to 500 litres in the case of "
                 "lorries and trucks, and 5,000 litres in the case of a train.",
                 "Remember: We must save fuel as it is a limited resource. Reducing fuel usage also helps in cutting "
                 "down pollution. Electric vehicles are now available that help conserve natural fuel and reduce "
                 "pollution."],
       teach=["Predict first: you add 67 litres of fuel and 58 litres of fuel. The ones are 7 and 8. How many ones do "
              "you get, and what do you do with them?",
              "Add the ones first: 7 + 8 = 15 ones. That is 10 ones and 5 ones. Write 5 in the ones place and regroup "
              "the 10 ones as 1 ten.",
              "Add the tens next: 6 + 5 = 11 tens, and the 1 ten you regrouped makes 12 tens. That is 10 tens and 2 "
              "tens. Write 2 in the tens place and regroup the 10 tens as 1 hundred.",
              "Write the 1 hundred in the hundreds place. The sum is 125.",
              "Rule: add one place at a time, starting with the ones. When a place makes 10 or more, write the extra "
              "and regroup 10 as 1 of the next place on the left."],
       examples=[WE("Add 67 litres of fuel and 58 litres of fuel (practice values).",
                    ["Write 67 and 58 with ones under ones and tens under tens.",
                     "Ones: 7 + 8 = 15. Write 5 in the ones place and regroup 10 ones as 1 ten.",
                     "Tens: 6 + 5 + 1 = 12. Write 2 in the tens place and regroup 10 tens as 1 hundred.",
                     "Hundreds: write the 1 hundred.",
                     "The sum is 125.",
                     "Check: 67 + 58 = 60 + 50 + 7 + 8 = 110 + 15 = 125."],
                    "125 litres, because 67 + 58 = 125")],
       ncert=["fuel.facts", "fuel.remember"], key_terms=["place value", "regroup", "sum"],
       misconceptions=["M_NO_CARRY"], minutes=6),
     A("T2.C2", "Easier Ways to Add", "Apply",
       "Students add a number that is just below a ten or a hundred by adding the round number and taking the extra "
       "back, and add whole tens together.",
       textbook=["Add the following numbers. Wherever possible, find easier ways to add the pairs of numbers."],
       teach=["Predict first: to add 98 to 54, is it easier to add 98 as it is, or to add 100 and then do something "
              "about the 2 that is too much?",
              "98 is 2 less than 100. Adding 100 is easy: 54 + 100 = 154. But 2 too many were added, so take 2 back: "
              "154 − 2 = 152.",
              "Whole tens are easy to add too. For 63 + 30, add the tens: 6 tens and 3 tens make 9 tens, which is 90. "
              "The 3 ones stay, so the sum is 93.",
              "Look at the numbers first. If one is close to a round number, or is a whole number of tens, there may be "
              "an easier way. If not, use place value.",
              "Rule: to add a number that is just below a round number, add the round number and take back the "
              "difference."],
       examples=[WE("Find 54 + 98 and 63 + 30 by an easier way (practice values).",
                    ["98 is 2 less than 100, so add 100 and take 2 back.",
                     "54 + 100 = 154.",
                     "154 − 2 = 152, so 54 + 98 = 152.",
                     "30 is 3 tens. Add the tens: 6 tens and 3 tens make 9 tens, which is 90.",
                     "The 3 ones stay: 90 + 3 = 93, so 63 + 30 = 93.",
                     "Check 54 + 98 with place value: ones 4 + 8 = 12, tens 5 + 9 + 1 = 15, so the sum is 152."],
                    "54 + 98 = 152 and 63 + 30 = 93")],
       key_terms=["easier way", "round number", "take back"],
       misconceptions=["M_FORGET_ONE"], minutes=5),
     DOER("T2.C3", "Practice: Fuel Tank Adder", "fuel_tank_adder", "Apply",
          "Students add pairs of numbers with place value and with easier ways, and find the total quantity of fuel in "
          "a tank.",
          ["Add the ones first, then the tens, then the hundreds.",
           "When a place makes 10 or more, regroup: 10 ones are 1 ten and 10 tens are 1 hundred.",
           "If a number is just below a round number, add the round number and take the extra back."],
          items=[FIO("fuel.lorry", "Example 1: Lorry fuel",
                     "A lorry has 28 litres of fuel in its tank. An additional 75 litres is filled. What is the total "
                     "quantity of fuel in the lorry?",
                     ["The total is 28 litres + 75 litres, so add 28 and 75.",
                      "Ones: 8 + 5 = 13. Write 3 in the ones place and regroup 10 ones as 1 ten.",
                      "Tens: 2 + 7 + 1 = 10. Write 0 in the tens place and regroup 10 tens as 1 hundred.",
                      "Hundreds: write the 1 hundred. The sum is 103.",
                      "Check: 28 + 75 = 28 + 70 + 5 = 98 + 5 = 103."],
                     "The lorry has 103 litres of fuel in all.",
                     kind="example",
                     s_figure="A chart with hundreds, tens and ones columns: 28 above 75, a 1 above the tens column and a "
                              "1 above the hundreds column for the two regroups, and the sum 103 below."),
                 FIO("fuel.49_89", "Fuel Arithmetic: the sum of 49 and 89",
                     "Let us try one more. Find the sum of 49 and 89.",
                     ["Ones: 9 + 9 = 18. Write 8 in the ones place and regroup 10 ones as 1 ten.",
                      "Tens: 4 + 8 + 1 = 13. Write 3 in the tens place and regroup 10 tens as 1 hundred.",
                      "Hundreds: write the 1 hundred. The sum is 138.",
                      "Check: 49 + 89 = 50 + 90 − 2 = 138."],
                     "49 + 89 = 138",
                     kind="prompt",
                     s_figure="A chart with hundreds, tens and ones columns: 49 above 89, a 1 above the tens column and a "
                              "1 above the hundreds column, and the sum 138 below."),
                 FIO("LUS43.add", "Let Us Solve (adding): add the pairs",
                     "Add the following numbers. Wherever possible, find easier ways to add the pairs of numbers. (a): "
                     "15 + 79; (b): 46 + 99; (c): 38 + 35; (d): 5 + 89; (e): 76 + 28; (f): 69 + 20.",
                     ["(a): 79 is 1 less than 80. 15 + 80 = 95, then take 1 back: 95 − 1 = 94.",
                      "(b): 99 is 1 less than 100. 46 + 100 = 146, then take 1 back: 146 − 1 = 145.",
                      "(c): There is no easy way, so use place value. Ones: 8 + 5 = 13, write 3 and regroup. Tens: "
                      "3 + 3 + 1 = 7. So 38 + 35 = 73.",
                      "(d): Start from the bigger number. 89 + 1 = 90, and 4 more makes 94, so 5 + 89 = 94.",
                      "(e): 28 is 2 less than 30. 76 + 30 = 106, then take 2 back: 106 − 2 = 104.",
                      "(f): 20 is 2 tens. 6 tens and 2 tens make 8 tens, which is 80, and the 9 ones stay: 80 + 9 = 89.",
                      "Check (e) with place value: ones 6 + 8 = 14, tens 7 + 2 + 1 = 10, so the sum is 104."],
                     "(a): 94; (b): 145; (c): 73; (d): 94; (e): 104; (f): 89",
                     kind="exercise")],
          misconceptions=["M_NO_CARRY", "M_FORGET_ONE"])],
    key_terms=["place value", "regroup", "sum", "easier way"]))

# ============================== T3 Subtraction and Its Link with Addition ==================================
TOPICS.append(TOPIC(
    "T3", "M1", "Subtraction and Its Link with Addition",
    ["Relationship Between Addition and Subtraction", "More Fuel Arithmetic", "Let Us Solve"], "Apply",
    "Students write the addition and subtraction sentences that follow from one sentence, subtract with place value, "
    "and check a subtraction by adding.",
    "Addition and subtraction are linked: from one sentence with three numbers you can write the others. To subtract "
    "with place value, start with the ones, and if there are too few ones, regroup 1 ten as 10 ones. Check a "
    "subtraction by adding the answer to the smaller number.",
    [A("T3.C1", "Addition and Subtraction Are Linked", "Understand",
       "Students write the other addition and subtraction sentences that follow from one given sentence about three "
       "numbers.",
       teach=["Predict first: you know that 35 + 28 = 63. Can you write a subtraction sentence about the same three "
              "numbers without working anything out?",
              "Think of 63 as the whole, split into two parts, 35 and 28.",
              "Take one part away from the whole and you get the other part: 63 − 28 = 35 and 63 − 35 = 28.",
              "Put the two parts together in either order and you get the whole: 35 + 28 = 63 and 28 + 35 = 63.",
              "This works from a subtraction sentence too. From 74 − 29 = 45, the whole is 74 and the parts are 29 and "
              "45: 29 + 45 = 74 and 74 − 45 = 29.",
              "Rule: three numbers, one whole and two parts. The whole minus a part is the other part, and the two "
              "parts added make the whole. Use this to check an answer."],
       examples=[WE("If 35 + 28 = 63, write the two subtraction sentences. Then, from 74 − 29 = 45, write an addition "
                    "sentence and one more subtraction sentence (practice values).",
                    ["In 35 + 28 = 63 the whole is 63 and the parts are 35 and 28.",
                     "Take the part 28 from the whole: 63 − 28 = 35.",
                     "Take the part 35 from the whole: 63 − 35 = 28.",
                     "In 74 − 29 = 45 the whole is 74 and the parts are 29 and 45.",
                     "Add the two parts: 29 + 45 = 74.",
                     "Take the part 45 from the whole: 74 − 45 = 29.",
                     "Check: 35 + 28 = 63 is true, and 29 + 45 = 74 is true."],
                    "63 − 28 = 35 and 63 − 35 = 28; 29 + 45 = 74 and 74 − 45 = 29")],
       key_terms=["whole", "part", "sentence"], misconceptions=["M_UNRELATED"], minutes=5),
     A("T3.C2", "Subtracting with Place Value", "Apply",
       "Students subtract two numbers with place value, regroup 1 ten as 10 ones when there are too few ones, and "
       "check by adding.",
       teach=["Predict first: you take 38 away from 72. The ones are 2 and 8. Can you take 8 ones away from 2 ones? "
              "What can you do?",
              "You cannot take 8 from 2, so regroup: 1 ten is 10 ones. Take 1 ten from the 7 tens, which leaves 6 "
              "tens, and add the 10 ones to the 2 ones to make 12 ones.",
              "Now subtract the ones: 12 − 8 = 4. Then subtract the tens: 6 − 3 = 3. The difference is 34.",
              "Check by adding the answer to the smaller number: 38 + 34 = 72. It matches the number you started with, "
              "so the answer is right.",
              "Rule: when there are too few ones to take away, regroup 1 ten as 10 ones. Check a subtraction by adding "
              "the answer to the smaller number."],
       examples=[WE("Find 72 − 38 and check the answer (practice values).",
                    ["Write 72 with 38 below it, ones under ones.",
                     "Ones: 2 is less than 8, so regroup 1 ten as 10 ones. The 7 tens become 6 tens and the 2 ones "
                     "become 12 ones.",
                     "Ones: 12 − 8 = 4.",
                     "Tens: 6 − 3 = 3.",
                     "The difference is 34.",
                     "Check: 38 + 34 = 72."],
                    "72 − 38 = 34, and 38 + 34 = 72")],
       key_terms=["subtract", "regroup", "difference", "check"], misconceptions=["M_SMALL_FROM_BIG"], minutes=6),
     DOER("T3.C3", "Practice: Fuel Gauge Subtractor", "fuel_gauge_subtractor", "Apply",
          "Students find how much fuel is left or filled by subtracting with place value, write the sentences that "
          "follow from one sentence, and check a subtraction by adding.",
          ["From one addition or subtraction sentence you can write the others: the whole minus a part is the other "
           "part.",
           "If there are too few ones to take away, regroup 1 ten as 10 ones.",
           "Check a subtraction by adding the answer to the smaller number."],
          items=[FIO("rel.Q1", "Relationship Between Addition and Subtraction: fill the blanks",
                     "Find the relationship between the numbers in the given statements and fill in the blanks "
                     "appropriately. (a): If 46 + 21 = 67, then, 67 − 21 = ___. 67 − 46 = ___. (b): If 198 − 98 = "
                     "100, then, 100 + ___ = 198. 198 − ___ = 98. (c): If 189 + 98 = 287, then, 287 − 98 = ___. "
                     "287 − 189 = ___. (d): If 872 − 672 = 200, then, 200 + ___ = 872. 872 − ___ = 672.",
                     ["(a): In 46 + 21 = 67 the whole is 67. Take a part away: 67 − 21 = 46 and 67 − 46 = 21.",
                      "(b): In 198 − 98 = 100 the whole is 198 and the parts are 98 and 100. The parts added make the "
                      "whole: 100 + 98 = 198. The whole minus a part: 198 − 100 = 98.",
                      "(c): In 189 + 98 = 287 the whole is 287. Take a part away: 287 − 98 = 189 and 287 − 189 = 98.",
                      "(d): In 872 − 672 = 200 the whole is 872 and the parts are 672 and 200. The parts added make the "
                      "whole: 200 + 672 = 872. The whole minus a part: 872 − 200 = 672.",
                      "Check (a): 46 + 21 = 67 is true."],
                     "(a): 46 and 21; (b): 98 and 100; (c): 189 and 98; (d): 672 and 200",
                     kind="exercise"),
                 FIO("rel.Q2", "Relationship Between Addition and Subtraction: write the sentences",
                     "In each of the following, write the subtraction and addition sentences that follow from the "
                     "given sentence. (a): If 78 + 164 = 242, then, (b): If 462 + 839 = 1,301, then, (c): If 921 − "
                     "137 = 784, then, (d): If 824 − 234 = 590, then,",
                     ["(a): The whole is 242 and the parts are 78 and 164. Take a part away: 242 − 164 = 78 and "
                      "242 − 78 = 164.",
                      "(b): The whole is 1,301. Take a part away: 1,301 − 839 = 462 and 1,301 − 462 = 839.",
                      "(c): The whole is 921 and the parts are 137 and 784. The parts added make the whole: 784 + 137 "
                      "= 921. The whole minus a part: 921 − 784 = 137.",
                      "(d): The whole is 824. The parts added make the whole: 590 + 234 = 824. The whole minus a part: "
                      "824 − 590 = 234.",
                      "Check (b): 462 + 839 = 1,301 is true."],
                     "Sample answer: (a): 242 − 164 = 78; (b): 1,301 − 839 = 462; (c): 784 + 137 = 921; (d): 590 + "
                     "234 = 824. Your answer may differ.",
                     kind="exercise"),
                 FIO("fuel2.minibus", "Example 2: Minibus fuel",
                     "A minibus has 18 litres of fuel left. After refuelling, the fuel meter indicates 65 litres. How "
                     "much fuel has been filled in the fuel tank of the minibus?",
                     ["The fuel filled is 65 litres − 18 litres, so subtract 18 from 65.",
                      "Ones: 5 is less than 8, so regroup 1 ten as 10 ones. The 6 tens become 5 tens and the 5 ones "
                      "become 15 ones.",
                      "Ones: 15 − 8 = 7. Tens: 5 − 1 = 4. The difference is 47.",
                      "Check by adding: 18 + 47 = 65, which is the fuel meter reading."],
                     "47 litres of fuel have been filled.",
                     kind="example",
                     q_figure="A bar from 18 litres to 65 litres with a curved arrow between them and a question mark.",
                     s_figure="A chart with tens and ones columns: 65 above 18, the regroup marks 5 tens and 15 ones, and "
                              "the difference 47 below."),
                 FIO("LUS45.Q1", "Let Us Solve (subtracting): the difference between 82 and 37",
                     "What is the difference between 82 and 37? Check your answer. Is 37 + ___ = 82?",
                     ["The difference is 82 − 37.",
                      "Ones: 2 is less than 7, so regroup 1 ten as 10 ones. The 8 tens become 7 tens and the 2 ones "
                      "become 12 ones.",
                      "Ones: 12 − 7 = 5. Tens: 7 − 3 = 4. The difference is 45.",
                      "Check: 37 + 45 = 82, so the blank is 45."],
                     "82 − 37 = 45. Check: 37 + 45 = 82",
                     kind="exercise",
                     s_figure="A chart with tens and ones columns: 82 above 37, the regroup marks 7 tens and 12 ones, and "
                              "the difference 45 below."),
                 FIO("LUS45.Q2to9", "Let Us Solve (subtracting): eight more subtractions",
                     "(a): 57 − 11 = ___; (b): 23 − 19 = ___; (c): 49 − 21 = ___; (d): 56 − 18 = ___; (e): 93 − 35 = "
                     "___; (f): 84 − 23 = ___; (g): 70 − 43 = ___; (h): 65 − 47 = ___.",
                     ["(a): No regrouping is needed: 7 − 1 = 6 ones and 5 − 1 = 4 tens, so 57 − 11 = 46.",
                      "(b): Ones: 3 is less than 9, so regroup: 13 − 9 = 4. Tens: 1 − 1 = 0. So 23 − 19 = 4.",
                      "(c): Ones: 9 − 1 = 8. Tens: 4 − 2 = 2. So 49 − 21 = 28.",
                      "(d): Ones: 6 is less than 8, so regroup: 16 − 8 = 8. Tens: 4 − 1 = 3. So 56 − 18 = 38.",
                      "(e): Ones: 3 is less than 5, so regroup: 13 − 5 = 8. Tens: 8 − 3 = 5. So 93 − 35 = 58.",
                      "(f): Ones: 4 − 3 = 1. Tens: 8 − 2 = 6. So 84 − 23 = 61.",
                      "(g): Ones: 0 is less than 3, so regroup: 10 − 3 = 7. Tens: 6 − 4 = 2. So 70 − 43 = 27.",
                      "(h): Ones: 5 is less than 7, so regroup: 15 − 7 = 8. Tens: 5 − 4 = 1. So 65 − 47 = 18.",
                      "Check (h): 47 + 18 = 65."],
                     "(a): 46; (b): 4; (c): 28; (d): 38; (e): 58; (f): 61; (g): 27; (h): 18",
                     kind="exercise")],
          misconceptions=["M_UNRELATED", "M_SMALL_FROM_BIG"])],
    key_terms=["subtract", "regroup", "difference", "check"]))
