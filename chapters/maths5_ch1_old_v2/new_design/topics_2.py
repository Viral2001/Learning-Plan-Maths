# -*- coding: utf-8 -*-
"""Topics T5 to T9. Comparing and ordering, the number line and digit swap, place value in other forms (module M1);
nearest tens, hundreds and thousands, and travelling now and then (module M2)."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T5 Comparing and ordering ==================================================
TOPICS.append(TOPIC(
    "T5", "M1", "Comparing and Ordering Large Numbers", ["Reading and writing large numbers"], "Apply",
    "Students compare two numbers by counting digits first and then comparing place by place from the left, and "
    "arrange numbers in increasing and decreasing order.",
    "A number with more digits is greater. When the digits are equal, compare from the left, place by place; the "
    "first place where the digits differ decides which number is greater.",
    [A("T5.C1", "More digits, greater number", "Understand",
       "Students compare numbers with a different number of digits and say that the number with more digits is "
       "greater, whatever its first digit.",
       teach=["Predict first: which is greater, 9,876 or 10,012?",
              "Count the digits first. 9,876 has four digits and 10,012 has five digits.",
              "A number with more digits is greater, because its leftmost digit sits in a bigger place. The size of the "
              "first digit does not matter when the digits are not equal in number."],
       examples=[WE("Which is greater, 9,876 or 10,012?",
                    ["9,876 has 4 digits and 10,012 has 5 digits.",
                     "The number with more digits is greater.",
                     "10,012 is greater, even though 9 is greater than 1."],
                    "10,012 is greater than 9,876")],
       key_terms=["digits", "greater than", "less than"], misconceptions=["M_FIRST_DIGIT"], minutes=7),
     A("T5.C2", "Same number of digits: compare from the left", "Apply",
       "Students compare numbers with the same number of digits by looking at each place from the left on the place "
       "value chart, and stop at the first place where the digits differ.",
       teach=["Predict first: 56,321 and 56,298 both have five digits. Which is greater, and which digit tells you?",
              "Put both numbers on the place value chart, TTh Th H T O, one below the other.",
              "Move from the left. TTh is 5 and 5, equal. Th is 6 and 6, equal. H is 3 and 2, different, so stop.",
              "The number with the bigger digit at the first place where the digits differ is greater."],
       examples=[WE("Which is greater, 56,321 or 56,298?",
                    ["Both have 5 digits, so compare place by place from the left.",
                     "TTh: 5 and 5, equal. Th: 6 and 6, equal. H: 3 and 2, and 3 is greater than 2.",
                     "So 56,321 is greater than 56,298."],
                    "56,321 is greater than 56,298, because the hundreds digit 3 is greater than 2")],
       key_terms=["place value chart"], misconceptions=["M_FIRST_DIGIT"], minutes=7),
     A("T5.C3", "Arranging numbers in order", "Apply",
       "Students arrange numbers in increasing (ascending) and decreasing (descending) order by sorting them by "
       "number of digits first and then comparing within each group.",
       teach=["Predict first: to arrange 3,450, 34,500, 345 and 4,035 in increasing order, which one comes first?",
              "Group by number of digits, then compare inside each group from the left.",
              "Increasing means smaller to greater, ascending. Decreasing means greater to smaller, descending.",
              "A number line also arranges numbers: the greater a number, the farther to the right."],
       examples=[WE("Arrange 3,450, 34,500, 345 and 4,035 in increasing order.",
                    ["345 has 3 digits, 3,450 and 4,035 have 4 digits, 34,500 has 5 digits.",
                     "Among 3,450 and 4,035: Th is 3 and 4, so 3,450 is less than 4,035.",
                     "Smallest to greatest: 345, 3,450, 4,035, 34,500."],
                    "345, 3,450, 4,035, 34,500")],
       key_terms=["increasing order", "ascending", "decreasing order", "descending"], minutes=7),
     DOER("T5.C4", "Practice: compare and arrange", "compare_chart", "Apply",
          "Students compare and order numbers on the compare chart, with the digits in a place value chart and the "
          "numbers as markers on a number line.",
          ["Count the digits first.",
           "With equal digits, compare from the left and stop at the first place that differs.",
           "Increasing is smaller to greater; decreasing is greater to smaller."],
          items=[FIO("LUD3.order", "Let Us Do 3, arrange in increasing order",
                     "Arrange in increasing order: 40,347, 34,407, 40,473, 34,740, 73,404, 74,430, 47,340 and 18,926.",
                     ["18,926 is the only number with TTh digit 1.",
                      "With TTh digit 3: 34,407 and 34,740. Th is 4 and 4; H is 4 and 7, so 34,407 is less than 34,740.",
                      "With TTh digit 4: 40,347, 40,473 and 47,340. Th is 0, 0 and 7, so 47,340 is last of the three. "
                      "H is 3 and 4, so 40,347 is less than 40,473.",
                      "With TTh digit 7: 73,404 and 74,430. Th is 3 and 4, so 73,404 is less than 74,430."],
                     "18,926, 34,407, 34,740, 40,347, 40,473, 47,340, 73,404, 74,430"),
                 FIO("LUD4.claim", "Let Us Do 4, the student's claim",
                     "A student said 9,990 is greater than 49,014 because 9 is greater than 4. Is the student correct? "
                     "Why or why not?",
                     ["9,990 has 4 digits and 49,014 has 5 digits.",
                      "A number with more digits is greater, so 49,014 is greater.",
                      "The student compared 9 with 4 as if both numbers had the same number of digits."],
                     "The student is not correct: 9,990 < 49,014, because 49,014 has more digits"),
                 FIO("B3", "Let Us Do (second set) 3, the two cars",
                     "Ravi's car has been driven for 56,987 km till now. Sheetal's car has been driven 67,543 km. Whose "
                     "car has been driven more?",
                     ["Both numbers have 5 digits, so compare from the left.",
                      "TTh: 5 and 6, and 6 is greater than 5.",
                      "So 67,543 is greater than 56,987."],
                     "Sheetal's car, 67,543 km, has been driven more"),
                 FIO("B4", "Let Us Do (second set) 4, prices of electric bikes",
                     "Arrange the prices in ascending (increasing) order: 90,000, 89,999, 94,983, 49,900, 93,743 and "
                     "39,999.",
                     ["TTh digits: 9, 8, 9, 4, 9 and 3. The smallest is 39,999 (TTh 3), then 49,900 (TTh 4), then "
                      "89,999 (TTh 8).",
                      "The three numbers starting with 9: 90,000, 94,983 and 93,743. Th is 0, 4 and 3.",
                      "So 90,000 is less than 93,743, which is less than 94,983."],
                     "39,999, 49,900, 89,999, 90,000, 93,743, 94,983"),
                 FIO("B5", "Let Us Do (second set) 5, population of towns",
                     "Arrange the populations in descending (decreasing) order: Town 1 65,232, Town 2 53,231, Town 3 "
                     "56,380, Town 4 51,336, Town 5 45,858 and Town 6 66,540.",
                     ["All have 5 digits. TTh is 6, 5, 5, 5, 4 and 6.",
                      "TTh 6: Town 6 (66,540) and Town 1 (65,232). Th is 6 and 5, so Town 6 is greater.",
                      "TTh 5: Town 3 (56,380), Town 2 (53,231) and Town 4 (51,336). Th is 6, 3 and 1.",
                      "Town 5 (45,858) has TTh 4, the smallest."],
                     "Town 6 (66,540), Town 1 (65,232), Town 3 (56,380), Town 2 (53,231), Town 4 (51,336), Town 5 "
                     "(45,858)")])],
    key_terms=["greater than", "less than", "increasing order", "decreasing order"]))

# ============================== T6 Number line, between and digit swap ======================================
TOPICS.append(TOPIC(
    "T6", "M1", "Number Line, Numbers Between and Digit Swap", ["Reading and writing large numbers"], "Apply",
    "Students place large numbers on a number line, write numbers between two given numbers, and interchange two "
    "digits of a number to make a number that is larger, smaller, or in a given range.",
    "A number line shows how far a number is from 0. To write numbers between two numbers, compare place by place. "
    "Swapping two digits changes the number by a different amount depending on the places that change.",
    [A("T6.C1", "Where does a number sit on the line?", "Understand",
       "Students place a large number between two benchmark numbers on a number line by reading its leading digits.",
       teach=["Predict first: on a line marked 0, 20,000, 40,000, 60,000 and 80,000, where will 47,340 sit?",
              "Find the two marks it lies between. 47,340 is more than 40,000 and less than 60,000.",
              "Then look at how far it is from the nearer mark. It is only 7,340 past 40,000, so it sits closer to "
              "40,000.",
              "The greater the number, the farther to the right it is."],
       examples=[WE("Between which two marks of 0, 20,000, 40,000, 60,000 and 80,000 does 47,340 sit, and which mark "
                    "is it nearer to?",
                    ["47,340 is more than 40,000 and less than 60,000.",
                     "47,340 − 40,000 = 7,340 and 60,000 − 47,340 = 12,660.",
                     "7,340 is smaller than 12,660, so it is nearer to 40,000."],
                    "47,340 sits between 40,000 and 60,000, nearer to 40,000")],
       key_terms=["number line"], minutes=8),
     A("T6.C2", "Numbers between two numbers", "Apply",
       "Students write numbers that lie between two given numbers and numbers with zero ones, tens and hundreds in a "
       "range by comparing place by place.",
       teach=["Predict first: name a number between 12,350 and 12,800. Is it the only one?",
              "A number between them has to be greater than the first and less than the second. Keep the first digits "
              "the same and change the hundreds.",
              "There are many such numbers. We can name some in steps of 100: 12,400, 12,500, 12,600 and 12,700."],
       examples=[WE("Write three numbers between 12,350 and 12,800.",
                    ["Both numbers start with 12 thousand, so the hundreds decide.",
                     "12,400 is more than 12,350 and less than 12,800.",
                     "12,500 and 12,700 also lie between them."],
                    "12,400, 12,500 and 12,700 (many answers are right)")],
       key_terms=["between"], minutes=8),
     A("T6.C3", "Digit swap", "Apply",
       "Students interchange two digits of a number to make a larger or smaller number, and see that moving a digit "
       "to a bigger place changes the number more.",
       teach=["Predict first: in 2,935, which two digits do you swap to get the largest number?",
              "Swapping two digits changes two places at once. The place on the left matters more.",
              "To make a number large, put the biggest digit in the leftmost place. To make it small, put the smallest "
              "digit there, if you can."],
       examples=[WE("Swap two digits of 2,935 to make the largest number and the smallest number you can.",
                    ["Largest: the biggest digit, 9, should be in the thousands place. Swap 2 and 9 to get 9,235.",
                     "Smallest: 2 is already the smallest digit, in the thousands place. Now put the next smallest, 3, "
                     "in the hundreds place: swap 9 and 3 to get 2,395."],
                    "Largest 9,235 (swap 2 and 9), smallest 2,395 (swap 9 and 3)")],
       key_terms=["digit", "interchange"], minutes=8),
     DOER("T6.C4", "Practice: place it and swap it", "number_line_placer", "Apply",
          "Students place numbers on a number line, write numbers between two numbers and interchange digits to hit "
          "a target.",
          ["A number line puts greater numbers to the right.",
           "To find numbers between two numbers, keep the leading digits and change a later place.",
           "Swapping a digit into a bigger place makes a bigger change."],
          items=[FIO("B1", "Let Us Do (second set) 1, numbers between",
                     "Write 5 numbers between the numbers 23,568 and 24,234.",
                     ["Both have 5 digits and start 2. Th is 3 and 4.",
                      "Numbers just after 23,568 with Th 3: 23,600 and 23,750 and 23,999.",
                      "24,000 and 24,100 have Th 4 and are less than 24,234."],
                     "23,600, 23,750, 23,999, 24,000, 24,100 (many answers are right)"),
                 FIO("B2", "Let Us Do (second set) 2, more than and less than",
                     "Write 5 numbers that are more than 38,125 but less than 38,600.",
                     ["The numbers start 38 and the hundreds digit must be between 1 and 6.",
                      "38,200 is more than 38,125. 38,500 is less than 38,600.",
                      "38,300, 38,400 and 38,599 also fit."],
                     "38,200, 38,300, 38,400, 38,500, 38,599 (many answers are right)"),
                 FIO("B6", "Let Us Do (second set) 6, ones, tens and hundreds are 0",
                     "Find numbers between 42,750 and 53,500 such that the ones, tens, and hundreds digits are all 0.",
                     ["Ones, tens and hundreds are 0, so the number is a whole number of thousands.",
                      "The first thousand after 42,750 is 43,000 and the last before 53,500 is 53,000."],
                     "43,000, 44,000, 45,000, 46,000, 47,000, 48,000, 49,000, 50,000, 51,000, 52,000 and 53,000"),
                 FIO("LUD5.a", "Let Us Do 5 (a), digit swap in 1,478",
                     "In the number 1,478, interchanging the digits 7 and 4 gives 1,748. Now interchange any two digits "
                     "in the number 1,478 to make a number that is larger than 5,500.",
                     ["To be larger than 5,500 the thousands digit must be 5 or more.",
                      "Swap 1 with 7: the digits 1, 4, 7, 8 become 7, 4, 1, 8."],
                     "7,418 (swap 1 and 7); 8,471 also works"),
                 FIO("LUD5.b", "Let Us Do 5 (b), digit swap in 10,593",
                     "Interchange two digits of 10,593 to make a number (i) between 11,000 and 15,000 (ii) more than "
                     "35,000.",
                     ["(i) 10,593 is 10 thousand 5 hundred 93. Swap 0 and 3: 13,590, which is between 11,000 and "
                      "15,000.",
                      "(ii) The TTh digit must be 3 or more. Swap 1 and 5: 50,193, which is more than 35,000."],
                     "(i) 13,590 (swap 0 and 3); (ii) 50,193 (swap 1 and 5)"),
                 FIO("LUD5.c", "Let Us Do 5 (c), digit swap in 48,247",
                     "Interchange two digits of 48,247 to make a number (i) as small as possible (ii) as big as "
                     "possible.",
                     ["(i) The smallest digit is 2. Put it in the TTh place by swapping 4 and 2: 28,447.",
                      "(ii) The biggest digit is 8. Put it in the TTh place by swapping 4 and 8: 84,247."],
                     "(i) 28,447 (swap 4 and 2); (ii) 84,247 (swap 4 and 8)")])],
    key_terms=["number line", "between", "interchange"]))

# ============================== T7 Place value in other forms ===============================================
TOPICS.append(TOPIC(
    "T7", "M1", "Place Value in Other Forms", ["Reading and writing large numbers"], "Apply",
    "Students write numbers in expanded form, write a number as tens, hundreds or thousands plus ones, and tell how "
    "many notes of 10, 100, 500 or 1,000 there are in a number.",
    "A number can be broken by place value, as ones, tens, hundreds and thousands, or counted in tens, hundreds or "
    "thousands. The same number is only written in a different form.",
    [A("T7.C1", "Expanded form", "Apply",
       "Students write a number as the sum of the value of its digits, and use zero to hold an empty place.",
       teach=["Predict first: what does 6,508 add up from?",
              "Each digit has a value: 6 in the thousands is 6,000, 5 in the hundreds is 500, 0 in the tens is 0, 8 in "
              "the ones is 8.",
              "Write the values with plus signs. A zero digit adds nothing, so its place can be left out of the "
              "sum, but the zero still holds the place in the number."],
       examples=[WE("Write 6,508 and 41,230 in expanded form.",
                    ["6,508 = 6,000 + 500 + 0 + 8 = 6,000 + 500 + 8.",
                     "41,230 = 40,000 + 1,000 + 200 + 30 + 0 = 40,000 + 1,000 + 200 + 30."],
                    "6,508 = 6,000 + 500 + 8 and 41,230 = 40,000 + 1,000 + 200 + 30")],
       key_terms=["expanded form"], misconceptions=["M_ZERO_HOLDER"], minutes=7),
     A("T7.C2", "Counting in tens, hundreds and thousands", "Apply",
       "Students write a number as tens plus ones, hundreds plus ones, and thousands plus hundreds plus tens plus "
       "ones, and see that there is more than one way.",
       teach=["Predict first: 983 is 98 tens and 3 ones. Can you also write it as 90 tens and some ones?",
              "90 tens is 900. The remaining 83 are ones: 983 = 90 Tens + 83 Ones.",
              "The number is the same; only the way of grouping changes. Both are correct."],
       examples=[WE("Write 983 as 90 Tens + __ Ones, and 4,560 as 45 Hundreds + __ Ones.",
                    ["90 Tens = 900, and 983 − 900 = 83, so 983 = 90 Tens + 83 Ones.",
                     "45 Hundreds = 4,500, and 4,560 − 4,500 = 60, so 4,560 = 45 Hundreds + 60 Ones."],
                    "983 = 90 Tens + 83 Ones and 4,560 = 45 Hundreds + 60 Ones")],
       key_terms=["tens", "hundreds", "thousands"], minutes=7),
     A("T7.C3", "How many notes?", "Apply",
       "Students tell how many notes of 10, 100, 500 or 1,000 make up a number by dividing the number into groups, "
       "and see that the leftover amount is not a full note.",
       teach=["Predict first: how many 10 rupee notes make 3,250 rupees?",
              "3 Tens is 30, 90 Tens is 900 and 700 Tens is 7,000. In 3,250, the number of tens is 325.",
              "For hundreds, drop the last two digits: 32 hundreds are in 3,250. For thousands drop the last three: "
              "3 thousands.",
              "For 500 notes, count how many hundreds there are and divide by 5; the leftover is not enough for another "
              "note."],
       examples=[WE("How many notes of 10, of 100, of 1,000 and of 500 are there in 3,250?",
                    ["Notes of 10: 3,250 has 325 tens.",
                     "Notes of 100: 3,250 has 32 hundreds, with 50 left.",
                     "Notes of 1,000: 3,250 has 3 thousands, with 250 left.",
                     "Notes of 500: 32 hundreds is 5 hundreds six times with 2 hundreds over, so 6 notes of 500."],
                    "325 notes of 10, 32 notes of 100, 3 notes of 1,000 and 6 notes of 500")],
       key_terms=["notes"], minutes=8),
     DOER("T7.C4", "Practice: break numbers by place value", None, "Apply",
          "Students write expanded forms and counts of tens, hundreds, thousands and notes for the numbers in "
          "the book's exercises.",
          ["Expanded form adds the value of each digit.",
           "The same number can be written as tens, hundreds or thousands plus ones.",
           "The number of notes of 10, 100 and 1,000 is read off by dropping digits."],
          examples=[WE("Your turn: write 5,070 in expanded form and as 50 Hundreds + __ Ones.",
                       ["5,070 = 5,000 + 0 + 70 + 0 = 5,000 + 70.",
                        "50 Hundreds = 5,000, and 5,070 − 5,000 = 70."],
                       "5,070 = 5,000 + 70 and 5,070 = 50 Hundreds + 70 Ones")],
          items=[FIO("B7", "Let Us Do (second set) 7, expanded form",
                     "Write the following numbers in the expanded form. One has been done for you: 783 = 700 + 80 + 3. "
                     "(b) 8,062 (c) 9,980 (d) 10,304 (e) 23,004 (f) 70,405.",
                     ["(a) 783 = 700 + 80 + 3, done for you.",
                      "(b) 8,062 = 8,000 + 60 + 2.",
                      "(c) 9,980 = 9,000 + 900 + 80.",
                      "(d) 10,304 = 10,000 + 300 + 4.",
                      "(e) 23,004 = 20,000 + 3,000 + 4.",
                      "(f) 70,405 = 70,000 + 400 + 5."],
                     "(b) 8,000 + 60 + 2; (c) 9,000 + 900 + 80; (d) 10,000 + 300 + 4; (e) 20,000 + 3,000 + 4; "
                     "(f) 70,000 + 400 + 5"),
                 FIO("B8.ab", "Let Us Do (second set) 8 (a), (b), (c), tens and ones",
                     "Fill in the blanks: (a) 983 = 90 Tens + 83 Ones (b) 68 = __ Tens + 18 Ones (c) 607 = 4 Hundreds "
                     "+ __ Ones.",
                     ["(a) 90 Tens is 900, so the remaining 83 are Ones.",
                      "(b) 68 − 18 = 50, and 50 is 5 Tens.",
                      "(c) 4 Hundreds is 400, and 607 − 400 = 207."],
                     "(b) 5 Tens; (c) 207 Ones"),
                 FIO("B8.cdefg", "Let Us Do (second set) 8 (d) to (g), more place value forms",
                     "Fill in the blanks: (d) 5,621 = 4 Thousand + __ Hundreds + 2 Tens + __ Ones (e) 7,069 = __ "
                     "Thousand + 20 Hundreds + __ Ones (f) 37,608 = __ Ten Thousand + 17 Thousand + __ Hundreds + 8 "
                     "Ones (g) 43,001 = 3 Ten Thousand + __ Thousand + __ Hundreds + 1 Ones.",
                     ["(d) 5,621 − 4,000 = 1,621. 2 Tens and 1 One use 21, so the Hundreds are 1,600, which is 16 "
                      "Hundreds, and the Ones are 1.",
                      "(e) 20 Hundreds is 2,000, so the Thousand part is 5,000 and 7,069 − 7,000 = 69 Ones.",
                      "(f) 17 Thousand is 17,000 and 8 Ones is 8. 37,608 − 17,000 − 8 = 20,600, so 2 Ten Thousand and "
                      "6 Hundreds.",
                      "(g) 3 Ten Thousand is 30,000 and 1 One is 1. 43,001 − 30,000 − 1 = 13,000, so 13 Thousand and "
                      "0 Hundreds."],
                     "(d) 16 Hundreds and 1 Ones; (e) 5 Thousand and 69 Ones; (f) 2 Ten Thousand and 6 Hundreds; "
                     "(g) 13 Thousand and 0 Hundreds"),
                 FIO("B9.hundreds_tens", "Let Us Do (second set) 9 (a) to (d), notes in 7,934",
                     "How many notes of 10, how many notes of 100, how many thousands, and how many 500 notes are there "
                     "in 7,934?",
                     ["Notes of 10: 7,934 has 793 tens, with 4 left.",
                      "Notes of 100: 7,934 has 79 hundreds, with 34 left.",
                      "Thousands: 7,934 has 7 thousands.",
                      "Notes of 500: 79 hundreds is 5 hundreds fifteen times with 4 hundreds over, so 15 notes of 500."],
                     "793 notes of 10, 79 notes of 100, 7 thousands and 15 notes of 500"),
                 FIO("B9.big", "Let Us Do (second set) 9 (e) to (h), notes in 65,342",
                     "How many notes of 10, how many notes of 100, how many thousands, and how many 500 notes are there "
                     "in 65,342?",
                     ["Notes of 10: 65,342 has 6,534 tens, with 2 left.",
                      "Notes of 100: 65,342 has 653 hundreds, with 42 left.",
                      "Thousands: 65,342 has 65 thousands.",
                      "Notes of 500: 653 hundreds is 5 hundreds one hundred thirty times with 3 hundreds over, so 130 "
                      "notes of 500."],
                     "6,534 notes of 10, 653 notes of 100, 65 thousands and 130 notes of 500")])],
    key_terms=["expanded form", "tens", "hundreds", "thousands"]))

# ============================== T8 Nearest tens, hundreds, thousands (module M2) ============================
TOPICS.append(TOPIC(
    "T8", "M2", "Nearest Tens, Hundreds and Thousands", ["Nearest Tens (10s), Hundreds (100s), and Thousands (1,000s)"],
    "Apply",
    "Students find the nearest ten, hundred and thousand of a number by counting jumps to the two neighbouring "
    "numbers, and fill a table of nearest numbers.",
    "The nearest ten, hundred or thousand of a number is the neighbouring one that needs the fewest jumps. A number "
    "exactly halfway goes to the bigger neighbour.",
    [A("T8.C1", "The nearest ten", "Understand",
       "Students find the nearest ten of 2,346 by comparing the jumps to its two neighbouring tens.",
       teach=["Predict first: a rabbit sits at 2,346. Its food is at the two neighbouring tens. Which one is nearer?",
              "The neighbouring tens of 2,346 are 2,340 and 2,350.",
              "To 2,350 it needs 4 jumps and to 2,340 it needs 6 jumps. The fewest jumps wins.",
              "2,350 is the nearest ten of 2,346."],
       examples=[WE("The rabbit is at 2,346 and its food is at 2,340 and 2,350. Which is the nearest ten?",
                    ["2,350 − 2,346 = 4 jumps to 2,350.",
                     "2,346 − 2,340 = 6 jumps to 2,340.",
                     "4 is less than 6, so the rabbit goes to 2,350."],
                    "2,350 is the nearest ten of 2,346, with 4 jumps",
                    ncert=["rab.tens"])],
       key_terms=["nearest ten"], misconceptions=["M_ROUND_UP"], minutes=7),
     A("T8.C2", "The nearest hundred", "Understand",
       "Students find the nearest hundred of 2,346 by comparing the jumps to 2,300 and 2,400.",
       teach=["Predict first: the same rabbit at 2,346, now with food at the two neighbouring hundreds. Which way?",
              "The neighbouring hundreds are 2,300 and 2,400.",
              "To 2,300 it needs 46 jumps and to 2,400 it needs 54 jumps.",
              "46 is less than 54, so 2,300 is nearer, even though the tens digit 4 is only one step from 5."],
       examples=[WE("The rabbit is at 2,346 and its food is at 2,300 and 2,400. Which is the nearest hundred, and how "
                    "many jumps?",
                    ["2,346 − 2,300 = 46 jumps to 2,300.",
                     "2,400 − 2,346 = 54 jumps to 2,400.",
                     "46 is less than 54."],
                    "2,300 is the nearest hundred of 2,346, with 46 jumps",
                    ncert=["rab.hundreds"])],
       key_terms=["nearest hundred"], misconceptions=["M_ROUND_UP"], minutes=7),
     A("T8.C3", "The nearest thousand and the halfway rule", "Apply",
       "Students find the nearest thousand of 2,346 and decide where a number exactly halfway between two neighbours "
       "goes.",
       teach=["Predict first: the same rabbit again, food at the two neighbouring thousands, 2,000 and 3,000.",
              "To 2,000 it needs 346 jumps and to 3,000 it needs 654 jumps, so 2,000 is the nearest thousand.",
              "Look at the middle of 2,000 and 3,000: it is 2,500. A number exactly in the middle is the same distance "
              "from both. By the usual rule, it goes to the bigger one, 3,000."],
       examples=[WE("The rabbit is at 2,346 and its food is at 2,000 and 3,000. Which is the nearest thousand, and how "
                    "many jumps?",
                    ["2,346 − 2,000 = 346 jumps to 2,000.",
                     "3,000 − 2,346 = 654 jumps to 3,000.",
                     "346 is less than 654."],
                    "2,000 is the nearest thousand of 2,346, with 346 jumps",
                    ncert=["rab.thousands"])],
       key_terms=["nearest thousand", "halfway"], misconceptions=["M_HALFWAY"], minutes=8),
     DOER("T8.C4", "Practice: help the rabbit", "rabbit_rounder", "Apply",
          "Students move the rabbit on the number line to the nearest ten, hundred and thousand, count the jumps and "
          "fill the table.",
          ["The nearest number is the neighbour with fewer jumps.",
           "The two neighbours of a number are the next lower and the next higher ten, hundred or thousand.",
           "A number exactly halfway goes to the bigger neighbour."],
          items=[FIO("rab.table", "Let Us Do, the table of nearest numbers",
                     "Fill in the boxes: the nearest tens, hundreds and thousands of 3,176, 4,017, 5,789 and 8,203.",
                     ["3,176: tens 3,170 or 3,180, and 6 jumps against 4, so 3,180. Hundreds 3,100 or 3,200, 76 against "
                      "24, so 3,200. Thousands 3,000.",
                      "4,017: tens 4,020 (3 jumps), hundreds 4,000 (17 jumps), thousands 4,000.",
                      "5,789: tens 5,790, hundreds 5,800, thousands 6,000.",
                      "8,203: tens 8,200, hundreds 8,200, thousands 8,000."],
                     "3,176: 3,180, 3,200, 3,000. 4,017: 4,020, 4,000, 4,000. 5,789: 5,790, 5,800, 6,000. 8,203: "
                     "8,200, 8,200, 8,000"),
                 FIO("LUT1", "Let Us Think 1, Vijay and Suma",
                     "Vijay rounded off a number to the nearest hundred. Suma rounded off the same number to the "
                     "nearest thousand. Both got the same result. Circle the numbers they might have used: 7,126, "
                     "7,835, 7,030 and 6,999.",
                     ["7,126: nearest hundred 7,100, nearest thousand 7,000. Different.",
                      "7,835: nearest hundred 7,800, nearest thousand 8,000. Different.",
                      "7,030: nearest hundred 7,000, nearest thousand 7,000. Same.",
                      "6,999: nearest hundred 7,000, nearest thousand 7,000. Same."],
                     "7,030 and 6,999"),
                 FIO("LUT2", "Let Us Think 2, same nearest ten, hundred, thousand",
                     "Think and write two numbers that have the same (a) nearest ten (b) nearest hundred (c) nearest "
                     "thousand.",
                     ["(a) 3,142 and 3,138 both have the nearest ten 3,140.",
                      "(b) 4,520 and 4,480 both have the nearest hundred 4,500.",
                      "(c) 6,100 and 5,800 both have the nearest thousand 6,000."],
                     "(a) 3,142 and 3,138; (b) 4,520 and 4,480; (c) 6,100 and 5,800 (many answers are right)"),
                 FIO("LUT3", "Let Us Think 3, same in two or three places",
                     "Think and write the numbers that have the same (a) nearest ten and nearest hundred (b) nearest "
                     "hundred and nearest thousand (c) nearest ten, hundred and thousand.",
                     ["(a) 5,201 and 5,204: nearest ten 5,200 and nearest hundred 5,200.",
                      "(b) 6,980 and 7,020: nearest hundred 7,000 and nearest thousand 7,000.",
                      "(c) 6,998 and 7,001: nearest ten 7,000, nearest hundred 7,000 and nearest thousand 7,000."],
                     "(a) 5,201 and 5,204; (b) 6,980 and 7,020; (c) 6,998 and 7,001 (many answers are right)")])],
    key_terms=["nearest ten", "nearest hundred", "nearest thousand"]))

# ============================== T9 Travelling now and then ==================================================
TOPICS.append(TOPIC(
    "T9", "M2", "Travelling, Now and Then", ["Travelling, Now and Then"], "Apply",
    "Students read how far people generally travel in an hour by different means, find the distance covered in "
    "several hours, and find how many vehicles carry a group of people.",
    "People travelled on foot, on animals and in boats, and now travel by cycle, car, train, ship, aeroplane and "
    "spacecraft. Distance in many hours is the distance in one hour times the number of hours, and the vehicles "
    "needed are the number of people divided by the number a vehicle carries.",
    [A("T9.C1", "How people travelled then and now", "Understand",
       "Students match travel conditions to the animals and vehicles used in them, then and now.",
       teach=["Predict first: which animal would you use to travel in a desert, and which in a snow-covered hill?",
              "In the past people travelled on foot, on animals and in boats and sailing ships. Bullocks, horses, "
              "donkeys, mules and elephants carried people; yaks, dogs and reindeer were used in hilly and snow-covered "
              "regions, and camels in deserts.",
              "Now people use bicycles, motorbikes, cars, buses, trains, ships and aeroplanes. Submarines go deep under "
              "water and spacecraft go to outer space."],
       examples=[WE("Which would be used to travel (a) in a desert, (b) in a snow-covered region, (c) deep under water, "
                    "(d) to outer space?",
                    ["(a) Camels have been used in deserts.",
                     "(b) Yaks, dogs and reindeer have been used in hilly and snow-covered regions.",
                     "(c) Submarines are used to go deep under water.",
                     "(d) Humans use spacecraft to travel to outer space."],
                    "(a) camel, (b) yak, dog or reindeer, (c) submarine, (d) spacecraft",
                    ncert=["tr.intro"])],
       key_terms=["travel", "transport"], minutes=6),
     A("T9.C2", "How far in one hour?", "Apply",
       "Students read the ranges of distance covered in one hour by foot, horse, cycle, motorbike, train, ship, "
       "aircraft and spacecraft, and say how many digits each distance has.",
       teach=["Predict first: in one hour, how far can a person go on foot, and how far in a spacecraft?",
              "In an hour a person can generally travel 3 to 5 km on foot, 10 to 15 km on horseback and 12 to 20 km by "
              "cycle.",
              "By motorbike 40 to 60 km, by train 40 to 160 km, by ship 25 to 45 km and by aircraft 750 to 920 km.",
              "A spacecraft covers a minimum of 28,000 km in an hour. The distances range from a 1-digit number to a "
              "5-digit number."],
       examples=[WE("Which means of travel covers a 1-digit, a 3-digit and a 5-digit number of kilometres in an hour?",
                    ["On foot, 3 to 5 km is a 1-digit number.",
                     "By aircraft, 750 to 920 km is a 3-digit number.",
                     "By spacecraft, a minimum of 28,000 km is a 5-digit number."],
                    "On foot, by aircraft and by spacecraft",
                    ncert=["tr.speeds"])],
       key_terms=["kilometre", "speed"], minutes=7),
     A("T9.C3", "Distance in many hours", "Apply",
       "Students find the distance covered in several hours by repeated addition and by multiplying the distance in "
       "one hour by the number of hours.",
       teach=["Predict first: a motorbike goes 50 km in one hour. How far in 3 hours at the same speed?",
              "In 1 hour 50 km, in 2 hours 50 + 50 = 100 km, in 3 hours 150 km.",
              "The distance in many hours is the distance in one hour times the number of hours."],
       examples=[WE("A motorbike covers 50 km in one hour. How far does it go in 3 hours at the same speed?",
                    ["1 hour: 50 km. 2 hours: 50 + 50 = 100 km.",
                     "3 hours: 100 + 50 = 150 km.",
                     "Or 50 × 3 = 150 km."],
                    "150 km")],
       key_terms=["distance", "hours"], minutes=6),
     DOER("T9.C4", "Practice: load the vehicles", "vehicle_loader", "Apply",
          "Students load a crowd into vehicles of different sizes, find the number of vehicles for 900 people, and "
          "work out distance in hours.",
          ["Distance in many hours is the distance in one hour times the number of hours.",
           "Vehicles needed is the number of people divided by the number a vehicle carries.",
           "If some people are left over, one more vehicle is needed."],
          items=[FIO("tr.vehicles_ad", "Let Us Do 2, vehicles (a) to (d)",
                     "A school has 461 girls and 439 boys. How many vehicles are needed for all of them to go on a trip "
                     "using (a) bicycle (2) (b) autorickshaw (3) (c) car (4) (d) big car (6)?",
                     ["Total students: 461 + 439 = 900.",
                      "(a) 900 ÷ 2 = 450 bicycles.",
                      "(b) 900 ÷ 3 = 300 autorickshaws.",
                      "(c) 900 ÷ 4 = 225 cars.",
                      "(d) 900 ÷ 6 = 150 big cars."],
                     "(a) 450 (b) 300 (c) 225 (d) 150"),
                 FIO("tr.vehicles_eh", "Let Us Do 2, vehicles (e) to (h)",
                     "For the same 461 girls and 439 boys, how many vehicles are needed using (e) tempo traveller (10) "
                     "(f) boat (20) (g) minibus (25) (h) aeroplane (180)?",
                     ["Total students: 461 + 439 = 900.",
                      "(e) 900 ÷ 10 = 90 tempo travellers.",
                      "(f) 900 ÷ 20 = 45 boats.",
                      "(g) 900 ÷ 25 = 36 minibuses.",
                      "(h) 900 ÷ 180 = 5 aeroplanes."],
                     "(e) 90 (f) 45 (g) 36 (h) 5"),
                 FIO("tr.cyclist", "Let Us Do 1, the cyclist",
                     "A cyclist can cover 15 km in one hour. How much distance will she cover in 4 hours, if she "
                     "maintains the same speed?",
                     ["1 hour: 15 km. 2 hours: 15 + 15 = 30 km.",
                      "3 hours: 30 + 15 = 45 km. 4 hours: 45 + 15 = 60 km.",
                      "Or 15 × 4 = 60."],
                     "60 km")])],
    key_terms=["distance", "vehicles", "speed"]))
