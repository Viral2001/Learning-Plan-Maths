# -*- coding: utf-8 -*-
"""Topics T7, T8, T9 (module M3: Number Tricks and Number Puzzles) and T10 (module M4): Quick Sums and Differences,
Palindrome Numbers, Number Grid Puzzles and Even and Odd Numbers.
Every teaching concept has one worked example with the plan's own numbers (practice values); every book question is an
FIO item of its topic's DOER, in the book's order. Grids are read with rows left to right and columns top to bottom."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T7 Quick Sums and Differences ==============================================
TOPICS.append(TOPIC(
    "T7", "M3", "Quick Sums and Differences", ["Quick Sums and Differences"], "Apply",
    "Students find the number to add to reach 100, 1,000 or 10,000 by making nines, and take away 9 or 99 quickly by "
    "taking away a round number and giving 1 back.",
    "A round number is a stepping stone. To find what to add to a number to make 100, 1,000 or 10,000, make 9 in every "
    "place and then add 1. To take away 9 or 99, take away 10 or 100 and add 1.",
    [A("T7.C1", "Making 100, 1,000 or 10,000 with Nines", "Apply",
       "Students find the number that must be added to a given number to make 100, 1,000 or 10,000 by making nines and "
       "adding 1.",
       textbook=["Sukanta likes the numbers 10, 100, 1,000, and 10,000. He wants to figure out what number he should add "
                 "to a given number such that the sum is 100 or 1,000.",
                 "Sukanta's friend Piku shows him an interesting way to solve the problems.",
                 "Do you think this method will always work?"],
       teach=["Predict first: you want 46 + ___ = 100. If you first find the number that makes 99, what is it, and what "
              "do you do next?",
              "Make a 9 in every place. In 46, the tens digit 4 needs 5 to make 9 and the ones digit 6 needs 3 to make "
              "9. So 46 + 53 = 99.",
              "99 is 1 less than 100. Add 1 to the number you added: 46 + 54 = 100. The blank is 54.",
              "It works for 1,000 too: make 999, then add 1. For 358: 3 needs 6, 5 needs 4 and 8 needs 1, so 358 + 641 "
              "= 999, and 358 + 642 = 1,000.",
              "It works when the units digit is 0 as well. For 270 the nines are 729, and 270 + 729 = 999, so 270 + 730 "
              "= 1,000. You can also count up: 270 + 30 = 300, then 300 + 700 = 1,000.",
              "Rule: to find what to add to reach 100, 1,000 or 10,000, make 9 in every place, then add 1. It always "
              "works, because 99, 999 and 9,999 are always 1 less than the round number."],
       examples=[WE("Find 46 + ___ = 100 and 358 + ___ = 1,000 by making nines (practice values).",
                    ["For 46: the tens digit 4 needs 5 to make 9 and the ones digit 6 needs 3 to make 9. So 46 + 53 = "
                     "99.",
                     "99 is 1 less than 100, so add 1 to the blank: 53 + 1 = 54, and 46 + 54 = 100.",
                     "For 358: 3 needs 6, 5 needs 4 and 8 needs 1 to make 9. So 358 + 641 = 999.",
                     "999 is 1 less than 1,000, so add 1 to the blank: 641 + 1 = 642, and 358 + 642 = 1,000.",
                     "Check: 46 + 54 = 100 and 358 + 642 = 1,000."],
                    "46 + 54 = 100 and 358 + 642 = 1,000")],
       ncert=["qs.intro", "qs.piku", "qs.always", "qs.zero"], key_terms=["round number", "nines", "add 1"],
       misconceptions=["M_NINES_ZERO"], minutes=6),
     A("T7.C2", "Taking Away 9 or 99 Quickly", "Apply",
       "Students subtract 9 or 99 quickly by taking away 10 or 100 and adding 1, and use it to find what to take away to "
       "leave 9 or 99.",
       textbook=["Namita likes the number 9. She wants to subtract 9 or 99 from any number. Find a way to quickly "
                 "subtract 9 or 99 from any number."],
       teach=["Predict first: to take 9 away from 52, you can take 10 away first. Did you take away too much or too "
              "little, and what do you do about it?",
              "10 is 1 more than 9, so taking 10 away takes 1 too many. Give 1 back: 52 − 10 = 42, then 42 + 1 = 43. So "
              "52 − 9 = 43.",
              "99 is 1 less than 100, so take 100 away and give 1 back. For 215: 215 − 100 = 115, then 115 + 1 = 116. "
              "So 215 − 99 = 116.",
              "It works backwards too. If 71 − ___ = 9, the blank is 71 − 9 = 62, and you find it with the same trick.",
              "Rule: to take away 9, take away 10 and add 1. To take away 99, take away 100 and add 1. To leave 9 or "
              "99, the number to take away is the first number minus 9 or minus 99."],
       examples=[WE("Find 52 − 9 and 215 − 99 by taking away 10 or 100 and adding 1 (practice values).",
                    ["10 is 1 more than 9, so take away 10 and give 1 back.",
                     "52 − 10 = 42, and 42 + 1 = 43, so 52 − 9 = 43.",
                     "100 is 1 more than 99, so take away 100 and give 1 back.",
                     "215 − 100 = 115, and 115 + 1 = 116, so 215 − 99 = 116.",
                     "Check: 43 + 9 = 52 and 116 + 99 = 215."],
                    "52 − 9 = 43 and 215 − 99 = 116")],
       ncert=["qs.namita", "qs.rev_intro"], key_terms=["take away", "give back", "round number"],
       misconceptions=["M_FORGET_ONE"], minutes=5),
     DOER("T7.C3", "Practice: Round Number Hops", "round_number_hops", "Apply",
          "Students find what to add to reach 100, 1,000 or 10,000 and what to take away to leave 9 or 99, using round "
          "numbers as stepping stones.",
          ["To reach a round number, make 9 in every place and add 1.",
           "To take away 9 or 99, take away 10 or 100 and add 1.",
           "To leave 9 or 99, the number to take away is the first number minus 9 or 99."],
          items=[FIO("qs.sukanta", "Example 7: Sukanta's blank",
                     "Sukanta likes the numbers 10, 100, 1,000, and 10,000. He wants to figure out what number he should "
                     "add to a given number such that the sum is 100 or 1,000. Help him fill in the blank with an "
                     "appropriate number. 32 + ___ = 100",
                     ["Make 9 in every place. The tens digit 3 needs 6 to make 9, and the ones digit 2 needs 7 to make "
                      "9. So 32 + 67 = 99.",
                      "99 is 1 less than 100, so add 1 to the blank: 67 + 1 = 68.",
                      "Check: 32 + 68 = 100."],
                     "The blank is 68, because 32 + 68 = 100.",
                     kind="example",
                     s_figure="The sum 32 + 67 = 99 with an arrow marked +1 leading to the sum 32 + 68 = 100."),
                 FIO("qs.fifty_nine", "Quick Sums and Differences: the number 59",
                     "Try this method for the number 59. 59 + ___ = 100",
                     ["The tens digit 5 needs 4 to make 9, and the ones digit 9 needs 0 to make 9. So 59 + 40 = 99.",
                      "Add 1 to the blank: 40 + 1 = 41.",
                      "Check: 59 + 41 = 100."],
                     "The blank is 41, because 59 + 41 = 100.",
                     kind="prompt"),
                 FIO("qs.use", "Quick Sums and Differences: 1,000 and 10,000",
                     "Now, use this method to solve the following. 877 + ___ = 1,000 and 666 + ___ = 1,000; 4,103 + ___ "
                     "= 10,000 and 5,555 + ___ = 10,000.",
                     ["877: 8 needs 1, 7 needs 2 and 7 needs 2 to make 9. So 877 + 122 = 999, and the blank is 122 + 1 = "
                      "123.",
                      "666: each 6 needs 3 to make 9. So 666 + 333 = 999, and the blank is 333 + 1 = 334.",
                      "4,103: 4 needs 5, 1 needs 8, 0 needs 9 and 3 needs 6. So 4,103 + 5,896 = 9,999, and the blank is "
                      "5,896 + 1 = 5,897.",
                      "5,555: each 5 needs 4 to make 9. So 5,555 + 4,444 = 9,999, and the blank is 4,444 + 1 = 4,445.",
                      "Check: 877 + 123 = 1,000, 666 + 334 = 1,000, 4,103 + 5,897 = 10,000 and 5,555 + 4,445 = 10,000."],
                     "877 + 123 = 1,000; 666 + 334 = 1,000; 4,103 + 5,897 = 10,000; 5,555 + 4,445 = 10,000",
                     kind="prompt"),
                 FIO("qs.zero_set", "Quick Sums and Differences: units digit 0",
                     "Will this method work if the units digit is 0? What do you think? What other methods can you use "
                     "to find the missing number to fill in the blanks? Share your thoughts in the class. (a): 180 + ___ "
                     "= 1,000; (b): 760 + ___ = 1,000; (c): 400 + ___ = 1,000.",
                     ["(a): 180: 1 needs 8, 8 needs 1 and 0 needs 9 to make 9. So 180 + 819 = 999, and the blank is 819 "
                      "+ 1 = 820.",
                      "(b): 760: 7 needs 2, 6 needs 3 and 0 needs 9. So 760 + 239 = 999, and the blank is 239 + 1 = 240.",
                      "(c): 400: 4 needs 5, 0 needs 9 and 0 needs 9. So 400 + 599 = 999, and the blank is 599 + 1 = 600.",
                      "Yes, the method works when the units digit is 0. The last nine is 9, and adding 1 makes it carry.",
                      "Another method: count up to the next hundred and then to 1,000. For 180: 180 + 20 = 200, then 200 "
                      "+ 800 = 1,000, so the blank is 20 + 800 = 820.",
                      "Check: 180 + 820 = 1,000, 760 + 240 = 1,000 and 400 + 600 = 1,000."],
                     "Sample answer: (a): 820; (b): 240; (c): 600. Yes, the method works with a 0 in the units place. "
                     "Your answer may differ.",
                     kind="exercise"),
                 FIO("qs.sub", "Quick Sums and Differences: take away 9 or 99",
                     "Namita likes the number 9. She wants to subtract 9 or 99 from any number. Find a way to quickly "
                     "subtract 9 or 99 from any number. (a): 67 − 9 = ___; (b): 83 − 9 = ___; (c): 144 − 9 = ___; (d): "
                     "187 − 99 = ___; (e): 247 − 99 = ___; (f): 763 − 99 = ___.",
                     ["To take away 9, take away 10 and give 1 back. To take away 99, take away 100 and give 1 back.",
                      "(a): 67 − 10 = 57, and 57 + 1 = 58. So 67 − 9 = 58.",
                      "(b): 83 − 10 = 73, and 73 + 1 = 74. So 83 − 9 = 74.",
                      "(c): 144 − 10 = 134, and 134 + 1 = 135. So 144 − 9 = 135.",
                      "(d): 187 − 100 = 87, and 87 + 1 = 88. So 187 − 99 = 88.",
                      "(e): 247 − 100 = 147, and 147 + 1 = 148. So 247 − 99 = 148.",
                      "(f): 763 − 100 = 663, and 663 + 1 = 664. So 763 − 99 = 664.",
                      "Check (f): 664 + 99 = 763."],
                     "(a): 58; (b): 74; (c): 135; (d): 88; (e): 148; (f): 664",
                     kind="exercise"),
                 FIO("qs.rev", "Quick Sums and Differences: leave 9 or 99",
                     "Now, use the above solutions to find answers to the following problems. Do not calculate again. "
                     "Namita wonders if she can get 9 or 99 as the answer to any subtraction problem. Find a way to get "
                     "the desired answer. (a): 32 − ___ = 9; (b): 56 − ___ = 9; (c): 877 − ___ = 99; (d): 666 − ___ = 99.",
                     ["The whole is the first number, and the blank and 9 (or 99) are the two parts. So the blank is the "
                      "first number minus 9 (or minus 99).",
                      "(a): 32 − 10 = 22, and 22 + 1 = 23. So 32 − 23 = 9.",
                      "(b): 56 − 10 = 46, and 46 + 1 = 47. So 56 − 47 = 9.",
                      "(c): The blank is 877 − 99. 877 − 100 = 777, and 777 + 1 = 778. So 877 − 778 = 99.",
                      "(d): The blank is 666 − 99. 666 − 100 = 566, and 566 + 1 = 567. So 666 − 567 = 99.",
                      "Check: 32 − 23 = 9, 56 − 47 = 9, 877 − 778 = 99 and 666 − 567 = 99."],
                     "(a): 23; (b): 47; (c): 778; (d): 567",
                     kind="exercise")],
          misconceptions=["M_NINES_ZERO", "M_FORGET_ONE"])],
    key_terms=["round number", "nines", "take away"]))

# ============================== T8 Palindrome Numbers ======================================================
TOPICS.append(TOPIC(
    "T8", "M3", "Palindrome Numbers", ["Let Us Think and Solve"], "Understand",
    "Students recognise palindrome numbers and list all the palindrome numbers between two given numbers.",
    "A palindrome number reads the same from left to right and from right to left, so its first and last digits match, "
    "and so do its second and second from last. To list the palindromes in a range, fix the first and last digits and "
    "let the middle digits change.",
    [A("T8.C1", "Palindrome Numbers", "Understand",
       "Students decide whether a number is a palindrome and list the palindrome numbers in a range by matching the "
       "first and last digits.",
       textbook=["Nitin likes numbers that read the same when read from left to right or from right to left. Such "
                 "numbers are called palindrome numbers. The numbers 22, 363, 404, and 8,558 are some examples."],
       teach=["Predict first: is 2,442 a palindrome? Read it from the left, then from the right.",
              "From the left it reads 2, 4, 4, 2. From the right it reads 2, 4, 4, 2. It is the same, so 2,442 is a "
              "palindrome.",
              "1,231 reads 1, 2, 3, 1 from the left and 1, 3, 2, 1 from the right. It is not the same, so it is not a "
              "palindrome.",
              "In a palindrome the first digit matches the last digit, and the second digit matches the second from "
              "last. The digits do not all have to be the same: 2,442 has two different digits.",
              "To list the palindromes between 300 and 340, the first and last digit must be 3 and only the middle digit "
              "changes: 303, 313, 323 and 333. 343 is too big.",
              "Rule: a palindrome number reads the same both ways. Match the first and last digits, then the next pair "
              "in, and so on."],
       examples=[WE("Is 2,442 a palindrome? List the palindrome numbers between 300 and 340 (practice values).",
                    ["Read 2,442 from the left: 2, 4, 4, 2. Read it from the right: 2, 4, 4, 2. It is the same, so "
                     "2,442 is a palindrome.",
                     "A number between 300 and 340 starts with 3, so it must end with 3. The number is 3, then one "
                     "digit, then 3.",
                     "The middle digit can be 0, 1, 2 or 3, because the number must be less than 340. 343 is more than "
                     "340.",
                     "The palindromes are 303, 313, 323 and 333.",
                     "Check: each of 303, 313, 323 and 333 reads the same from the right."],
                    "2,442 is a palindrome. Between 300 and 340: 303, 313, 323 and 333")],
       ncert=["pal.def"], key_terms=["palindrome", "first digit", "last digit"],
       misconceptions=["M_PAL_SAME"], minutes=5),
     DOER("T8.C2", "Practice: Palindromes", None, "Understand",
          "Students list all the palindrome numbers between two numbers by matching the first and last digits.",
          ["A palindrome number reads the same from left to right and from right to left.",
           "Match the first and last digits, then the next pair in.",
           "Fix the matching digits and let the middle digit change."],
          items=[FIO("pal.1", "Let Us Think and Solve (palindromes): 100 to 200",
                     "Nitin likes numbers that read the same when read from left to right or from right to left. Such "
                     "numbers are called palindrome numbers. The numbers 22, 363, 404, and 8,558 are some examples. List "
                     "all palindrome numbers between 100 and 200.",
                     ["A number between 100 and 200 has 3 digits and starts with 1, so it must end with 1.",
                      "The middle digit can be any digit from 0 to 9.",
                      "The palindromes are 101, 111, 121, 131, 141, 151, 161, 171, 181 and 191.",
                      "Check: there are 10 numbers, one for each middle digit, and each reads the same from the right."],
                     "101, 111, 121, 131, 141, 151, 161, 171, 181, 191",
                     kind="exercise"),
                 FIO("pal.2", "Let Us Think and Solve (palindromes): 900 to 1,200",
                     "List all palindrome numbers between 900 and 1,200.",
                     ["From 900 to 999 the number starts with 9, so it ends with 9. The middle digit is any digit from "
                      "0 to 9: 909, 919, 929, 939, 949, 959, 969, 979, 989 and 999.",
                      "From 1,000 to 1,200 the number has 4 digits and starts with 1, so it ends with 1. The second "
                      "digit must match the third digit.",
                      "The number is 1, then two digits that match, then 1. With 00 it is 1,001 and with 11 it is 1,111. "
                      "With 22 it would be 1,221, which is more than 1,200.",
                      "The palindromes are 909, 919, 929, 939, 949, 959, 969, 979, 989, 999, 1,001 and 1,111.",
                      "Check: 10 numbers below 1,000 and 2 numbers above make 12 palindromes."],
                     "909, 919, 929, 939, 949, 959, 969, 979, 989, 999, 1,001, 1,111",
                     kind="exercise"),
                 FIO("pal.3", "Let Us Think and Solve (palindromes): 25,000 to 27,000",
                     "List all palindrome numbers between 25,000 and 27,000.",
                     ["A 5 digit number between 25,000 and 27,000 starts with 2, so it must end with 2. The second digit "
                      "must match the fourth digit, and the middle digit can be any digit from 0 to 9.",
                      "Between 25,000 and 27,000 the second digit is 5 or 6.",
                      "With the second digit 5: 25,052, 25,152, 25,252, 25,352, 25,452, 25,552, 25,652, 25,752, 25,852 "
                      "and 25,952.",
                      "With the second digit 6: 26,062, 26,162, 26,262, 26,362, 26,462, 26,562, 26,662, 26,762, 26,862 "
                      "and 26,962.",
                      "27,072 is more than 27,000, so it is not in the list.",
                      "Check: 10 numbers with 5 and 10 numbers with 6 make 20 palindromes."],
                     "Twenty numbers: 25,052 to 25,952 and 26,062 to 26,962, going up by 100 each time.",
                     kind="exercise")],
          misconceptions=["M_PAL_SAME"])],
    key_terms=["palindrome", "digits"]))

# ============================== T9 Number Grid Puzzles =====================================================
TOPICS.append(TOPIC(
    "T9", "M3", "Number Grid Puzzles", ["Let Us Think and Solve"], "Apply",
    "Students fill a 3 by 3 grid with the numbers 1 to 9 so that every row and every column increases or decreases as "
    "asked.",
    "In a number grid puzzle, the arrows on the rows and columns tell where the smallest and the biggest numbers must "
    "go. Place them first, fill the rest, then check every row and every column.",
    [A("T9.C1", "Filling a Grid in Order", "Apply",
       "Students find where the smallest and the biggest number must go in a grid from its inc and dec arrows, and fill "
       "the grid so that every row and column follows its arrow.",
       textbook=["In a 3×3 grid, arrange the numbers 1 to 9 such that each row and each column has numbers in an "
                 "increasing (inc) order. Each number should be used only once."],
       teach=["Predict first: in a 2 by 2 grid with the numbers 1 to 4, every row and every column must increase. Which "
              "cell must hold 1, and which must hold 4?",
              "A row that increases grows to the right. A column that increases grows downwards. So the smallest number "
              "must be at the top left, where every row and column starts, and the biggest at the bottom right, where "
              "they end.",
              "Put 1 at the top left and 4 at the bottom right. Then 2 and 3 go in the other two cells. The top row 1, 2 "
              "and the bottom row 3, 4 work.",
              "If the rows increase but the columns decrease, a column shrinks downwards. Now 4 must be at the top right "
              "and 1 at the bottom left: the top row 3, 4 and the bottom row 1, 2.",
              "Check every row and every column, not only the rows.",
              "Rule: the arrows tell where the smallest and the biggest number go. Place them, fill the rest, then check "
              "every row and every column. Rows are read from left to right and columns from top to bottom."],
       examples=[WE("Fill a 2 by 2 grid with the numbers 1 to 4 so that every row and column increases. Then fill one so "
                    "that the rows increase and the columns decrease (practice values).",
                    ["Rows are read left to right and columns top to bottom. An increasing row grows to the right and an "
                     "increasing column grows downwards.",
                     "All increasing: the smallest number 1 goes top left and the biggest number 4 goes bottom right.",
                     "Put 2 and 3 in the other two cells: the top row is 1, 2 and the bottom row is 3, 4.",
                     "Check the rows: 1 is less than 2 and 3 is less than 4. Check the columns: 1 is less than 3 and 2 is "
                     "less than 4.",
                     "Rows increasing and columns decreasing: a column shrinks downwards, so the biggest number 4 goes "
                     "top right and the smallest number 1 goes bottom left.",
                     "Put 3 top left and 2 bottom right: the top row is 3, 4 and the bottom row is 1, 2.",
                     "Check the rows: 3 is less than 4 and 1 is less than 2. Check the columns: 3 is more than 1 and 4 is "
                     "more than 2."],
                    "Top row 1, 2 and bottom row 3, 4; and top row 3, 4 and bottom row 1, 2")],
       ncert=["grid.rules"], key_terms=["grid", "row", "column", "increasing", "decreasing"],
       misconceptions=["M_GRID_ROWS_ONLY"], minutes=6),
     DOER("T9.C2", "Practice: Number Grid Puzzle", "number_grid_puzzle", "Apply",
          "Students fill the five number grids so that every row and column follows its inc or dec arrow.",
          ["Rows are read left to right and columns top to bottom.",
           "The arrows tell where the smallest and the biggest number must go.",
           "Check every row and every column."],
          items=[FIO("grid.a", "Let Us Think and Solve (grids): all increasing",
                     "In a 3×3 grid, arrange the numbers 1 to 9 such that each row and each column has numbers in an "
                     "increasing (inc) order. Each number should be used only once.",
                     ["Rows are read left to right and columns top to bottom, and every row and column must increase.",
                      "The smallest number 1 goes top left and the biggest number 9 goes bottom right.",
                      "Fill the first row with the next small numbers: 1, 2, 3.",
                      "Fill the next two rows: 4, 5, 6 and 7, 8, 9.",
                      "Check the rows: each one grows to the right. Check the columns: 1, 4, 7 and 2, 5, 8 and 3, 6, 9 "
                      "each grow downwards."],
                     "Sample answer: Row 1: 1, 2, 3; Row 2: 4, 5, 6; Row 3: 7, 8, 9. Many grids work. Your answer may "
                     "differ.",
                     kind="exercise",
                     q_figure="An empty 3 by 3 grid with the word inc written to the right of each of the three rows and "
                              "under each of the three columns.",
                     s_figure="The same grid filled with 1, 2, 3 in the top row, 4, 5, 6 in the middle row and 7, 8, 9 in "
                              "the bottom row."),
                 FIO("grid.b", "Let Us Think and Solve (grids): all decreasing",
                     "This time, fill the grid such that each row and column has numbers in decreasing (dec) order.",
                     ["Every row and column must decrease: rows shrink to the right and columns shrink downwards.",
                      "The biggest number 9 goes top left and the smallest number 1 goes bottom right.",
                      "Fill the rows from the top with the biggest numbers: 9, 8, 7, then 6, 5, 4, then 3, 2, 1.",
                      "Check every row and every column: each number is bigger than the one after it."],
                     "Sample answer: Row 1: 9, 8, 7; Row 2: 6, 5, 4; Row 3: 3, 2, 1. Many grids work. Your answer may "
                     "differ.",
                     kind="exercise",
                     q_figure="An empty 3 by 3 grid with the word dec written to the right of each of the three rows and "
                              "under each of the three columns.",
                     s_figure="The same grid filled with 9, 8, 7 in the top row, 6, 5, 4 in the middle row and 3, 2, 1 in "
                              "the bottom row."),
                 FIO("grid.c", "Let Us Think and Solve (grids): rows dec, columns inc",
                     "Now, fill the grids below with numbers (1 to 9) based on the inc (increasing) and dec (decreasing) "
                     "conditions, as indicated below. Grid 1: the rows are dec, dec, dec and the columns are inc, inc, "
                     "inc.",
                     ["Every row decreases to the right and every column increases downwards.",
                      "The smallest number 1 must be at the top right, where a row ends and a column starts. The biggest "
                      "number 9 must be at the bottom left.",
                      "Fill each row from the right: the first row is 3, 2, 1, the second row is 6, 5, 4 and the third "
                      "row is 9, 8, 7.",
                      "Check the rows: each one shrinks to the right. Check the columns: 3, 6, 9 and 2, 5, 8 and 1, 4, 7 "
                      "each grow downwards."],
                     "Sample answer: Row 1: 3, 2, 1; Row 2: 6, 5, 4; Row 3: 9, 8, 7. Your answer may differ.",
                     kind="exercise",
                     q_figure="An empty 3 by 3 grid with the word dec written to the right of each of the three rows and "
                              "the word inc under each of the three columns.",
                     s_figure="The same grid filled with 3, 2, 1 in the top row, 6, 5, 4 in the middle row and 9, 8, 7 in "
                              "the bottom row."),
                 FIO("grid.d", "Let Us Think and Solve (grids): the second mixed grid",
                     "Fill the grid with numbers 1 to 9 as indicated. Grid 2: the rows are dec, dec, inc and the columns "
                     "are dec, dec, inc.",
                     ["Row 1 and row 2 decrease to the right, and row 3 increases to the right. Column 1 and column 2 "
                      "decrease downwards, and column 3 increases downwards.",
                      "The smallest number 1 goes top right: it is the end of the decreasing row 1 and the start of the "
                      "increasing column 3.",
                      "The biggest number 9 goes bottom right: it is the end of the increasing row 3 and the end of the "
                      "increasing column 3.",
                      "Column 3 increases from 1 to 9, so it is 1, 2, 9. Row 3 increases and ends in 9, so it is 3, 4, 9.",
                      "Fill the rest so that rows 1 and 2 decrease and columns 1 and 2 decrease: row 1 is 8, 6, 1 and "
                      "row 2 is 7, 5, 2.",
                      "Check the rows: 8, 6, 1 decreases, 7, 5, 2 decreases and 3, 4, 9 increases. Check the columns: "
                      "8, 7, 3 decreases, 6, 5, 4 decreases and 1, 2, 9 increases."],
                     "Sample answer: Row 1: 8, 6, 1; Row 2: 7, 5, 2; Row 3: 3, 4, 9. Your answer may differ.",
                     kind="exercise",
                     q_figure="An empty 3 by 3 grid with the words dec, dec, inc written to the right of the three rows "
                              "and the words dec, dec, inc under the three columns.",
                     s_figure="The same grid filled with 8, 6, 1 in the top row, 7, 5, 2 in the middle row and 3, 4, 9 in "
                              "the bottom row."),
                 FIO("grid.e", "Let Us Think and Solve (grids): the third mixed grid",
                     "Fill the grid with numbers 1 to 9 as indicated. Grid 3: the rows are inc, inc, dec and the columns "
                     "are inc, dec, dec.",
                     ["Row 1 and row 2 increase to the right, and row 3 decreases to the right. Column 1 increases "
                      "downwards, and columns 2 and 3 decrease downwards.",
                      "The smallest number 1 goes top left: it is the start of the increasing row 1 and the start of the "
                      "increasing column 1.",
                      "The biggest number 9 goes bottom left: it is the start of the decreasing row 3 and the end of the "
                      "increasing column 1.",
                      "Column 1 increases from 1 to 9, so it is 1, 2, 9. Row 3 decreases from 9, so it is 9, 4, 3.",
                      "Fill the rest: row 1 increases from 1, so it is 1, 6, 8, and row 2 increases from 2, so it is 2, "
                      "5, 7.",
                      "Check the rows: 1, 6, 8 increases, 2, 5, 7 increases and 9, 4, 3 decreases. Check the columns: "
                      "1, 2, 9 increases, 6, 5, 4 decreases and 8, 7, 3 decreases."],
                     "Sample answer: Row 1: 1, 6, 8; Row 2: 2, 5, 7; Row 3: 9, 4, 3. Your answer may differ.",
                     kind="exercise",
                     q_figure="An empty 3 by 3 grid with the words inc, inc, dec written to the right of the three rows "
                              "and the words inc, dec, dec under the three columns.",
                     s_figure="The same grid filled with 1, 6, 8 in the top row, 2, 5, 7 in the middle row and 9, 4, 3 in "
                              "the bottom row.")],
          misconceptions=["M_GRID_ROWS_ONLY"])],
    key_terms=["grid", "row", "column", "inc", "dec"]))

# ============================== T10 Even and Odd Numbers ===================================================
TOPICS.append(TOPIC(
    "T10", "M4", "Even and Odd Numbers", ["Even and Odd Numbers"], "Understand",
    "Students decide whether a number is even or odd using pairs, and explain what happens to the sum of two even "
    "numbers, two odd numbers, and an odd and an even number.",
    "A number is even when its counters pair up with none left, and odd when one is left. The units digit tells: 0, 2, "
    "4, 6 and 8 are even. Even plus even is even, odd plus odd is even because the two leftovers make a pair, and odd "
    "plus even is odd.",
    [A("T10.C1", "Even and Odd by Pairing", "Understand",
       "Students decide whether a number is even or odd by pairing counters and by looking at the units digit.",
       teach=["Predict first: you put 14 counters in pairs, then 15 counters in pairs. Which one has a counter left "
              "over?",
              "14 counters make 7 pairs and none is left over. A number is even when its counters pair up with none left.",
              "15 counters make 7 pairs and 1 counter is left over. A number is odd when one counter is left over.",
              "You do not need to draw counters for big numbers. Look at the units digit. If it is 0, 2, 4, 6 or 8 the "
              "number is even. If it is 1, 3, 5, 7 or 9 it is odd.",
              "3,468 ends in 8, so it is even. 5,127 ends in 7, so it is odd. 0 counts as even, so a number that ends in "
              "0 is even.",
              "Rule: even means pairs with none left, odd means one left over. The units digit tells which."],
       examples=[WE("Arrange 14 counters and 15 counters in pairs. Then say whether 3,468 and 5,127 are even or odd "
                    "(practice values).",
                    ["14 counters make 7 pairs: 7 + 7 = 14, and no counter is left over. So 14 is even.",
                     "15 counters make 7 pairs and 1 counter is left over: 7 + 7 + 1 = 15. So 15 is odd.",
                     "For big numbers look at the units digit: 0, 2, 4, 6 and 8 mean even, and 1, 3, 5, 7 and 9 mean odd.",
                     "3,468 has the units digit 8, so it is even.",
                     "5,127 has the units digit 7, so it is odd.",
                     "Check: 3,468 = 1,734 + 1,734, two equal parts, so nothing is left over."],
                    "14 and 3,468 are even; 15 and 5,127 are odd")],
       ncert=["eo.arrange"], key_terms=["even", "odd", "pairs", "units digit"],
       misconceptions=["M_ZERO_NOT_EVEN"], minutes=5),
     A("T10.C2", "Adding Even and Odd Numbers", "Understand",
       "Students explain with leftover counters why even plus even is even, odd plus odd is even, and odd plus even is "
       "odd.",
       teach=["Predict first: you join 9 counters and 13 counters. Each group has 1 counter left over. What happens to "
              "the two leftover counters?",
              "The two leftover counters make one new pair, so nothing is left over. 9 + 13 = 22 is even.",
              "Even plus even: neither group has a leftover, so the joined group has none. 14 + 8 = 22 is even.",
              "Odd plus even: only one group has a leftover and it stays alone. 7 + 10 = 17 is odd.",
              "Rule: even plus even is even, odd plus odd is even, odd plus even is odd. It is true for every pair, "
              "because the leftovers decide."],
       examples=[WE("Join 14 and 8, then 9 and 13, then 7 and 10, and say whether each sum is even or odd (practice "
                    "values).",
                    ["14 and 8 are both even, so no counter is left over in either group: 14 + 8 = 22, and 22 is even.",
                     "9 and 13 are both odd, so each group has 1 counter left over. The two leftovers make one pair: "
                     "9 + 13 = 22, and 22 is even.",
                     "7 is odd and 10 is even, so only 7 has a leftover counter. It stays alone: 7 + 10 = 17, and 17 is "
                     "odd.",
                     "Check: 22, 22 and 17 end in 2, 2 and 7, so they are even, even and odd."],
                    "14 + 8 = 22 is even; 9 + 13 = 22 is even; 7 + 10 = 17 is odd")],
       key_terms=["even", "odd", "leftover", "sum"], misconceptions=["M_ODD_ODD_ODD"], minutes=5),
     DOER("T10.C3", "Practice: Pairs and Leftovers", "pairs_and_leftovers", "Understand",
          "Students circle the even numbers, use pairs to say what changes when 2 is added to a number, and explain "
          "with the leftover counter the sums of two even numbers, two odd numbers, and an odd and an even number.",
          ["Even means pairs with none left over, and odd means one left over.",
           "The units digit tells: 0, 2, 4, 6 and 8 are even.",
           "Even plus even is even, odd plus odd is even, and odd plus even is odd."],
          items=[FIO("eo.circle", "Even and Odd Numbers: circle the even numbers",
                     "Circle the numbers that are even. (a): 297; (b): 498; (c): 724; (d): 100; (e): 199; (f): 789; (g): "
                     "49; (h): 6,893; (i): 846; (j): 111; (k): 222; (l): 1,023.",
                     ["Look at the units digit of each number. 0, 2, 4, 6 and 8 mean even.",
                      "(a): 297 ends in 7, odd. (b): 498 ends in 8, even. (c): 724 ends in 4, even. (d): 100 ends in 0, "
                      "even.",
                      "(e): 199 ends in 9, odd. (f): 789 ends in 9, odd. (g): 49 ends in 9, odd. (h): 6,893 ends in 3, "
                      "odd.",
                      "(i): 846 ends in 6, even. (j): 111 ends in 1, odd. (k): 222 ends in 2, even. (l): 1,023 ends in 3, "
                      "odd.",
                      "Check: the even numbers are 498, 724, 100, 846 and 222, five in all."],
                     "(b): 498; (c): 724; (d): 100; (i): 846; (k): 222",
                     kind="exercise"),
                 FIO("eo.add18", "Even and Odd Numbers: add 2 to 18",
                     "Observe the given arrangement. Paired arrangement for 18. Add 2 to 18. What changes or does not "
                     "change in the arrangement?",
                     ["18 counters make 9 pairs, two rows of 9, and no counter is left over.",
                      "Add 2 counters. They make one more pair, so the rows are now 10 and 10, and there are 10 pairs.",
                      "What changes: the number of pairs, from 9 to 10, and the number of counters, from 18 to 20.",
                      "What does not change: no counter is left over, so the number is still even.",
                      "Check: 18 + 2 = 20, and 20 = 10 + 10."],
                     "The pairs go from 9 to 10 and the counters from 18 to 20. Nothing is left over, so it is still "
                     "even.",
                     kind="exercise",
                     q_figure="18 round counters in two rows of 9, each counter paired with the one below it, with the "
                              "caption Paired arrangement for 18."),
                 FIO("eo.add23", "Even and Odd Numbers: add 2 to 23",
                     "Observe the given arrangement. Paired arrangement for 23. Add 2 to 23. What changes or does not "
                     "change in the arrangement?",
                     ["23 counters make 11 pairs, and 1 counter is left over (a row of 12 and a row of 11).",
                      "Add 2 counters. They make one more pair, so there are 12 pairs, and the same 1 counter is still "
                      "left over.",
                      "What changes: the number of pairs, from 11 to 12, and the number of counters, from 23 to 25.",
                      "What does not change: 1 counter is left over, so the number is still odd.",
                      "Check: 23 + 2 = 25, and 25 = 12 + 12 + 1."],
                     "The pairs go from 11 to 12 and the counters from 23 to 25. One counter is still left over, so it "
                     "is still odd.",
                     kind="exercise",
                     q_figure="23 round counters in two rows, a row of 12 and a row of 11, with the caption Paired "
                              "arrangement for 23."),
                 FIO("eo.q3a", "Even and Odd Numbers: two even numbers",
                     "What do you notice about the sums in each of the following cases? Do you think it will be true for "
                     "all pairs of such numbers? Explain your observations. You may use the paired arrangement to "
                     "explain your thinking. (a): 12 and 6 are a pair of even numbers. Choose 5 such pairs of even "
                     "numbers. Add the numbers in each of the pairs.",
                     ["Choose 5 pairs of even numbers and add each pair: 12 + 6 = 18, 4 + 8 = 12, 10 + 20 = 30, 14 + 16 "
                      "= 30 and 2 + 6 = 8.",
                      "What we notice: every sum is even.",
                      "It is true for all pairs. An even number pairs up with none left over, so two even numbers "
                      "together pair up with none left over.",
                      "Check: 18, 12, 30, 30 and 8 all end in 0, 2 or 8, which are even endings."],
                     "Sample answer: 12 + 6 = 18, 4 + 8 = 12, 10 + 20 = 30, 14 + 16 = 30, 2 + 6 = 8. All sums are even, "
                     "for all pairs. Your answer may differ.",
                     kind="exercise"),
                 FIO("eo.q3b", "Even and Odd Numbers: two odd numbers",
                     "What do you notice about the sums in each of the following cases? Do you think it will be true for "
                     "all pairs of such numbers? Explain your observations. You may use the paired arrangement to "
                     "explain your thinking. (b): 13 and 9 are a pair of odd numbers. Choose 5 such pairs of odd "
                     "numbers. Add the numbers in each of the pairs.",
                     ["Choose 5 pairs of odd numbers and add each pair: 13 + 9 = 22, 3 + 5 = 8, 7 + 11 = 18, 15 + 1 = 16 "
                      "and 9 + 9 = 18.",
                      "What we notice: every sum is even.",
                      "It is true for all pairs. Each odd number has 1 counter left over, and the two leftovers make a "
                      "pair, so nothing is left over.",
                      "Check: 22, 8, 18, 16 and 18 all end in 2, 8 or 6, which are even endings."],
                     "Sample answer: 13 + 9 = 22, 3 + 5 = 8, 7 + 11 = 18, 15 + 1 = 16, 9 + 9 = 18. All sums are even, "
                     "for all pairs. Your answer may differ.",
                     kind="exercise"),
                 FIO("eo.q3c", "Even and Odd Numbers: an odd and an even number",
                     "What do you notice about the sums in each of the following cases? Do you think it will be true for "
                     "all pairs of such numbers? Explain your observations. You may use the paired arrangement to "
                     "explain your thinking. (c): 7 and 12 are a pair of odd and even numbers. Choose 5 such pairs of "
                     "odd and even numbers. Add the numbers in each of the pairs.",
                     ["Choose 5 pairs of an odd and an even number and add each pair: 7 + 12 = 19, 3 + 4 = 7, 5 + 10 = "
                      "15, 9 + 2 = 11 and 11 + 8 = 19.",
                      "What we notice: every sum is odd.",
                      "It is true for all pairs. The odd number has 1 counter left over and the even number has none, so "
                      "1 counter is still left over.",
                      "Check: 19, 7, 15, 11 and 19 all end in 9, 7, 5 or 1, which are odd endings."],
                     "Sample answer: 7 + 12 = 19, 3 + 4 = 7, 5 + 10 = 15, 9 + 2 = 11, 11 + 8 = 19. All sums are odd, for "
                     "all pairs. Your answer may differ.",
                     kind="exercise")],
          misconceptions=["M_ZERO_NOT_EVEN", "M_ODD_ODD_ODD"])],
    key_terms=["even", "odd", "pairs", "leftover"]))
