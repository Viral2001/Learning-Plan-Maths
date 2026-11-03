# -*- coding: utf-8 -*-
"""Topics T6 to T9 (module M2): comparing and ordering large numbers, digit swap, expanded form and counting tens,
hundreds and thousands, and the nearest ten, hundred and thousand."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T6 Comparing and Ordering Large Numbers ====================================
TOPICS.append(TOPIC(
    "T6", "M2", "Comparing and Ordering Large Numbers", ["Reading and writing large numbers"], "Apply",
    "Students compare large numbers by counting digits and then comparing place by place, arrange numbers in order "
    "on a number line, and write numbers that lie between two given numbers.",
    "A number with more digits is greater. With the same number of digits, compare from the left, place by place. "
    "On a number line the greater number is farther to the right, and many numbers lie between any two numbers.",
    [A("T6.C1", "Which number is greater?", "Understand",
       "Students compare two numbers by counting their digits first, and when the digits are equal they compare "
       "place by place from the left, to say which number is greater.",
       teach=["Predict first: which is greater, 8,965 or 21,304? The first digit 8 is bigger than 2. Does that decide "
              "it?",
              "Count the digits first. 8,965 has 4 digits and 21,304 has 5 digits.",
              "A number with more digits is greater. The 8 in 8,965 is only 8 Thousands, but the 2 in 21,304 is 2 "
              "Ten Thousands, worth 20,000.",
              "When both numbers have the same number of digits, compare from the left, place by place. Stop at the "
              "first place where the digits are different. The bigger digit there makes the greater number.",
              "Rule: count the digits first. If they are equal, compare from the left."],
       examples=[WE("Which is greater, 8,965 or 21,304? Then which is greater, 47,260 or 47,620?",
                    ["8,965 has 4 digits and 21,304 has 5 digits.",
                     "The number with more digits is greater, so 21,304 is greater than 8,965, even though 8 is "
                     "bigger than 2.",
                     "47,260 and 47,620 both have 5 digits, so compare place by place from the left.",
                     "The TTh digits are 4 and 4, equal. The Th digits are 7 and 7, equal. The H digits are 2 and 6, "
                     "different, so stop here.",
                     "6 is greater than 2, so 47,620 is greater than 47,260."],
                    "21,304 is greater than 8,965, and 47,620 is greater than 47,260")],
       key_terms=["digits", "greater than", "less than", "place value chart"],
       misconceptions=["M_FIRST_DIGIT"], minutes=7),
     A("T6.C2", "Ordering numbers on a number line", "Apply",
       "Students place numbers on a number line, read them from left to right to arrange them in increasing order, "
       "and read them from right to left to arrange them in decreasing order.",
       teach=["Predict first: on a number line from 0 to 40,000, which will sit farther to the right, 19,780 or "
              "24,305?",
              "A number line has equal gaps between its marks. Here the marks are 10,000 apart: 0, 10,000, 20,000, "
              "30,000 and 40,000.",
              "To place a number, find the two marks it lies between. 19,780 lies between 10,000 and 20,000. 24,305 "
              "lies between 20,000 and 30,000.",
              "A number farther to the right is greater. Reading the line from left to right gives the increasing "
              "order. Reading it from right to left gives the decreasing order."],
       examples=[WE("Place 31,250, 8,640, 24,305 and 19,780 on a number line with the marks 0, 10,000, 20,000, "
                    "30,000 and 40,000. Then write them in increasing order.",
                    ["The marks are 10,000 apart. Find the two marks each number lies between.",
                     "8,640 lies between 0 and 10,000. 19,780 lies between 10,000 and 20,000, just before 20,000.",
                     "24,305 lies between 20,000 and 30,000. 31,250 lies between 30,000 and 40,000.",
                     "Read the line from left to right. The farther a number is to the right, the greater it is.",
                     "Check with the digits: 8,640 has 4 digits and the others have 5 digits, so it is the smallest."],
                    "8,640, 19,780, 24,305, 31,250")],
       key_terms=["number line", "increasing order", "decreasing order"], minutes=7),
     A("T6.C3", "Numbers between two numbers", "Apply",
       "Students write numbers that lie between two given numbers, including numbers whose ones, tens and hundreds "
       "digits are all zero, by keeping the leading digits and changing a later place.",
       teach=["Predict first: how many numbers lie between 71,420 and 72,050? Is there only one?",
              "A number between two numbers is greater than the smaller one and less than the bigger one.",
              "Look at the leading digits. Both numbers start with 7. The thousands digits are 1 and 2. Keep the "
              "leading digits and change a later place to build numbers in between.",
              "There are many right answers. Always check the number against the smaller end and the bigger end.",
              "A number with 0 in the ones, tens and hundreds places is a whole number of thousands, like 72,000."],
       examples=[WE("(a) Write three numbers between 71,420 and 72,050. (b) Which of them has 0 in the ones, tens "
                    "and hundreds places?",
                    ["A number between them must be greater than 71,420 and less than 72,050.",
                     "Both numbers have 5 digits and start with 7. The Th digits are 1 and 2.",
                     "Keep Th as 1 and make the hundreds bigger: 71,500 and 71,900 are greater than 71,420 and less "
                     "than 72,050.",
                     "Make Th 2 and the hundreds 0: 72,000 is greater than 71,420 and less than 72,050.",
                     "72,000 has 0 in the ones, tens and hundreds places."],
                    "71,500, 71,900 and 72,000 lie between them (many answers are right); 72,000 has zero ones, "
                    "tens and hundreds")],
       key_terms=["between", "greater than", "less than"], minutes=7),
     DOER("T6.C4", "Pull it together and do it: Compare, Order and Find Numbers Between", None, "Apply",
          "Students compare and order large numbers and write numbers between two numbers in the book's questions, "
          "and explain why one number is greater by counting digits and comparing place by place.",
          ["Count the digits first. More digits means a greater number.",
           "With equal digits, compare from the left and stop at the first place that is different.",
           "On a number line, the greater number is farther to the right.",
           "A number between two numbers is greater than the smaller and less than the bigger."],
          items=[FIO("LUDa.Q3", "Let Us Do (large numbers), Q3 order",
                     "Arrange the numbers below in increasing order. You can use the number line below, if required. "
                     "40,347, 34,407, 40,473, 34,740, 73,404, 74,430, 47,340, 18,926.",
                     ["All eight numbers have 5 digits, so compare the TTh digits first: 4, 3, 4, 3, 7, 7, 4 and 1.",
                      "TTh digit 1: 18,926. It is the smallest.",
                      "TTh digit 3: 34,407 and 34,740. The Th digits are 4 and 4, so compare the H digits, 4 and 7. "
                      "34,407 is smaller.",
                      "TTh digit 4: 40,347, 40,473 and 47,340. The Th digits are 0, 0 and 7, so 47,340 is the "
                      "greatest of the three.",
                      "Compare the H digits of the other two, 3 and 4. 40,347 is smaller than 40,473.",
                      "TTh digit 7: 73,404 and 74,430. The Th digits are 3 and 4, so 73,404 is smaller.",
                      "Check: on the number line from 0 to 80,000 the eight numbers also sit from left to right in "
                      "this order."],
                     "18,926; 34,407; 34,740; 40,347; 40,473; 47,340; 73,404; 74,430",
                     q_figure="A number line from 0 to 80,000 with marks at 0, 20,000, 40,000, 60,000 and 80,000, "
                              "and eight number cards in a row above it.",
                     s_figure="The same number line with the eight numbers placed on it from left to right, 18,926 "
                              "first and 74,430 last."),
                 FIO("LUDa.Q4", "Let Us Do (large numbers), Q4 compare",
                     "A student said 9,990 is greater than 49,014 because 9 is greater than 4. Is the student "
                     "correct? Why or why not? Use the number line below to find the position of the numbers. Fill "
                     "in the blanks. You can use the place value chart to compare the numbers.",
                     ["Write both numbers in the place value chart. 9,990 is 9 Th, 9 H, 9 T and 0 O. It has 4 "
                      "digits and the TTh place is empty.",
                      "49,014 is 4 TTh, 9 Th, 0 H, 1 T and 4 O. It has 5 digits.",
                      "A number with more digits is greater, so 49,014 is greater than 9,990.",
                      "The student compared 9 with 4, but the 9 in 9,990 is in the Th place and the 4 in 49,014 is "
                      "in the TTh place. Compare first digits only when both numbers have the same number of "
                      "digits.",
                      "Fill the number line. The marks are 5,000 apart, so 10,000 − 5,000 = 5,000 and 50,000 − "
                      "45,000 = 5,000.",
                      "The blank marks are 15,000, 20,000, 25,000, 30,000, 35,000, 40,000 and 45,000.",
                      "9,990 sits just before the 10,000 mark. 49,014 sits just before the 50,000 mark, much farther "
                      "to the right.",
                      "Check: 49,014 is farther to the right than 9,990, so it is greater."],
                     "No, the student is not correct. 49,014 is greater than 9,990 because it has 5 digits and "
                     "9,990 has 4. The blanks are 15,000, 20,000, 25,000, 30,000, 35,000, 40,000 and 45,000.",
                     q_figure="A number line with ten equally spaced marks and a box under each mark, with 5,000 in "
                              "the first box, 10,000 in the second box, 50,000 in the last box and seven empty "
                              "boxes between; under it a place value chart with the columns TTh, Th, H, T and O, "
                              "a first row with 9, 9, 9 and 0 under Th, H, T and O and the TTh box empty, and a "
                              "second row with 4, 9, 0, 1 and 4.",
                     s_figure="The same number line with all ten marks named from 5,000 to 50,000, a dot just "
                              "before 10,000 for 9,990 and a dot just before 50,000 for 49,014, and the chart rows "
                              "lined up under TTh, Th, H, T and O."),
                 FIO("LUDc.Q1", "Let Us Do (comparing), Q1 between",
                     "Write 5 numbers between the numbers 23,568 and 24,234.",
                     ["A number between them must be greater than 23,568 and less than 24,234.",
                      "Both numbers have 5 digits and start with 2. The Th digits are 3 and 4.",
                      "With Th digit 3 and a bigger hundreds digit, 23,600 and 23,800 are greater than 23,568.",
                      "With Th digit 4 and a small hundreds digit, 24,000, 24,100 and 24,200 are less than 24,234.",
                      "Choose five of them: 23,600, 23,800, 24,000, 24,100 and 24,200.",
                      "Check: 23,568 is less than 23,600, and 24,200 is less than 24,234."],
                     "Sample answer: 23,600; 23,800; 24,000; 24,100 and 24,200. Your answer may differ."),
                 FIO("LUDc.Q2", "Let Us Do (comparing), Q2 more than and less than",
                     "Write 5 numbers that are more than 38,125 but less than 38,600.",
                     ["The numbers must be greater than 38,125 and less than 38,600.",
                      "All of them start with 38, so only the hundreds, tens and ones change. A hundreds digit "
                      "from 2 to 5 is safe: every such number is greater than 38,125 and less than 38,600.",
                      "38,200, 38,300, 38,400 and 38,500 use the hundreds digits 2, 3, 4 and 5.",
                      "38,599 is also less than 38,600, because 38,599 + 1 = 38,600.",
                      "Check: the smallest, 38,200, is greater than 38,125, and the biggest, 38,599, is less than "
                      "38,600."],
                     "Sample answer: 38,200; 38,300; 38,400; 38,500 and 38,599. Your answer may differ."),
                 FIO("LUDc.Q3", "Let Us Do (comparing), Q3 two cars",
                     "Ravi's car has been driven for 56,987 km till now. Sheetal's car has been driven 67,543 km. "
                     "Whose car has been driven more?",
                     ["56,987 and 67,543 both have 5 digits, so compare from the left.",
                      "The TTh digits are 5 and 6.",
                      "6 is greater than 5, so 67,543 is greater than 56,987.",
                      "Check: 56,987 is less than 60,000 and 67,543 is more than 60,000."],
                     "Sheetal's car, 67,543 km, has been driven more."),
                 FIO("LUDc.Q4", "Let Us Do (comparing), Q4 prices of electric bikes",
                     "The following are the prices of different electric bikes. Arrange the prices in ascending "
                     "(increasing) order. ₹90,000, ₹89,999, ₹94,983, ₹49,900, ₹93,743, ₹39,999.",
                     ["All six prices have 5 digits. Compare the TTh digits: 9, 8, 9, 4, 9 and 3.",
                      "The smallest TTh digit is 3, so ₹39,999 is first. Then 4 gives ₹49,900 and 8 gives ₹89,999.",
                      "Three prices have TTh digit 9: ₹90,000, ₹94,983 and ₹93,743. Compare their Th digits: 0, 4 "
                      "and 3.",
                      "0 is less than 3 and 3 is less than 4, so the order is ₹90,000, ₹93,743, ₹94,983.",
                      "Put the parts together: ₹39,999, ₹49,900, ₹89,999, then ₹90,000, ₹93,743 and ₹94,983.",
                      "Check: 89,999 + 1 = 90,000, so ₹89,999 comes just before ₹90,000."],
                     "₹39,999; ₹49,900; ₹89,999; ₹90,000; ₹93,743; ₹94,983"),
                 FIO("LUDc.Q5", "Let Us Do (comparing), Q5 population of towns",
                     "The following table shows the population of some towns. Arrange them in a descending "
                     "(decreasing) order. Town 1 65,232, Town 2 53,231, Town 3 56,380, Town 4 51,336, Town 5 "
                     "45,858, Town 6 66,540.",
                     ["All six populations have 5 digits. The TTh digits are 6, 5, 5, 5, 4 and 6.",
                      "The greatest TTh digit is 6: Town 1 (65,232) and Town 6 (66,540). The Th digits are 5 and 6, "
                      "so Town 6 is greater.",
                      "TTh digit 5: Town 2 (53,231), Town 3 (56,380) and Town 4 (51,336). The Th digits are 3, 6 and "
                      "1, so Town 3 is first, then Town 2, then Town 4.",
                      "TTh digit 4: Town 5 (45,858) is the smallest.",
                      "Put the parts together, greatest first: Town 6, Town 1, Town 3, Town 2, Town 4 and Town 5.",
                      "Check: 66,540, 65,232, 56,380, 53,231, 51,336 and 45,858 each get smaller."],
                     "Town 6 (66,540), Town 1 (65,232), Town 3 (56,380), Town 2 (53,231), Town 4 (51,336), "
                     "Town 5 (45,858)",
                     q_figure="A table with the headings Town and Population and six rows: Town 1 65,232, Town 2 "
                              "53,231, Town 3 56,380, Town 4 51,336, Town 5 45,858 and Town 6 66,540.",
                     s_figure="The same table with the rows reordered from the greatest population, Town 6, to the "
                              "smallest, Town 5."),
                 FIO("LUDc.Q6", "Let Us Do (comparing), Q6 zeros in ones, tens and hundreds",
                     "Find numbers between 42,750 and 53,500 such that the ones, tens, and hundreds digits are all "
                     "0.",
                     ["A number with 0 in the ones, tens and hundreds places is a whole number of thousands, like "
                      "43,000.",
                      "The first such number after 42,750 is 43,000, because 42,000 is less than 42,750.",
                      "The last such number before 53,500 is 53,000, because 54,000 is more than 53,500.",
                      "List them by adding 1,000 each time: 43,000, 44,000, 45,000, 46,000, 47,000, 48,000, 49,000, "
                      "50,000, 51,000, 52,000 and 53,000.",
                      "Count them: 53 − 43 + 1 = 11 numbers.",
                      "Check: every number has 0 in the ones, tens and hundreds places, and all lie between 42,750 "
                      "and 53,500."],
                     "43,000; 44,000; 45,000; 46,000; 47,000; 48,000; 49,000; 50,000; 51,000; 52,000 and 53,000 "
                     "(11 numbers)")],
          misconceptions=["M_FIRST_DIGIT"])],
    key_terms=["greater than", "less than", "increasing order", "decreasing order", "between"]))

# ============================== T7 Digit Swap ===========================================================
TOPICS.append(TOPIC(
    "T7", "M2", "Digit Swap", ["Reading and writing large numbers"], "Apply",
    "Students swap two digits of a number, say whether the new number is bigger, smaller or the same, and swap "
    "digits to make the biggest or the smallest number.",
    "Each digit has a place, and the place gives its value. When two different digits swap, both change their value "
    "and the number changes. A bigger digit in a bigger place makes a bigger number.",
    [A("T7.C1", "Swapping two digits changes the value", "Understand",
       "Students swap two digits of a number, write the new number, and say whether it is bigger or smaller by "
       "finding the new value of each swapped digit.",
       teach=["Predict first: in 3,925, swap the digits 3 and 9. Will the new number be the same, bigger or smaller?",
              "Each digit has a place, and the place gives its value. After the swap, each digit stands in the "
              "other digit's place, so its value changes.",
              "In 3,925 the 9 is worth 900. After the swap it stands in the thousands place and is worth 9,000. The "
              "3 was worth 3,000 and is now worth 300.",
              "Swapping two different digits always changes the number. Swapping two digits that are the same changes "
              "nothing.",
              "Rule: a bigger digit moving to a bigger place makes the number bigger."],
       examples=[WE("Swap the digits 3 and 9 in 3,925. Write the new number and say how it compares with 3,925.",
                    ["3,925 = 3 Thousands + 9 Hundreds + 2 Tens + 5 Ones.",
                     "Swap the 3 and the 9. The 9 moves to the thousands place and the 3 moves to the hundreds "
                     "place. The new number is 9,325.",
                     "The 9 was worth 900 and is now worth 9,000. It gained 9,000 − 900 = 8,100.",
                     "The 3 was worth 3,000 and is now worth 300. It lost 3,000 − 300 = 2,700.",
                     "The number changed by 8,100 − 2,700 = 5,400.",
                     "Check: 9,325 − 3,925 = 5,400, so 9,325 is 5,400 more than 3,925."],
                    "The new number is 9,325. It is 5,400 more than 3,925, so the swap changed the number.")],
       key_terms=["digit", "interchange", "place value"], misconceptions=["M_SWAP_VALUE"], minutes=7),
     A("T7.C2", "The biggest and the smallest by one swap", "Apply",
       "Students swap one pair of digits to make the biggest number and the smallest number they can, by moving "
       "the biggest or the smallest digit to the leftmost place.",
       teach=["Predict first: in 62,815, which digit should stand in the ten thousands place to make the number as "
              "big as it can be?",
              "The ten thousands place has the greatest value, so look at it first.",
              "To make the biggest number with one swap, bring the biggest digit to the leftmost place. To make the "
              "smallest number, bring the smallest digit there.",
              "A number cannot start with 0, so never bring a 0 to the front.",
              "If the biggest digit is already at the front, leave it and look at the next place."],
       examples=[WE("Swap two digits of 62,815 to make (a) the biggest number and (b) the smallest number you can "
                    "with one swap.",
                    ["62,815 has the digits 6, 2, 8, 1 and 5. The leftmost place, the ten thousands place, matters "
                     "most.",
                     "(a) Biggest: the biggest digit is 8. Bring it to the ten thousands place by swapping 6 and 8. "
                     "The new number is 82,615.",
                     "(b) Smallest: the smallest digit is 1. Bring it to the ten thousands place by swapping 6 and "
                     "1. The new number is 12,865.",
                     "Check: 82,615 is more than 62,815 and 12,865 is less than 62,815."],
                    "(a) 82,615 (swap 6 and 8). (b) 12,865 (swap 6 and 1).")],
       key_terms=["biggest number", "smallest number", "leftmost place"], misconceptions=["M_SWAP_VALUE"],
       minutes=7),
     DOER("T7.C3", "Practice: Swap It", "digit_swap", "Apply",
          "Students swap two digits of a number to make a number that is larger, in a given range, as small as "
          "possible or as big as possible, and compare the new number with the old one.",
          ["Swapping two different digits changes the number. Swapping two equal digits does not.",
           "A bigger digit moving to a bigger place makes the number bigger.",
           "For the biggest number, bring the biggest digit to the front. For the smallest, bring the smallest "
           "digit, but not 0."],
          items=[FIO("LUDa.Q5", "Let Us Do (large numbers), Q5 digit swap",
                     "Digit swap. (a) In the number 1,478, interchanging the digits 7 and 4 gives 1,748. Now, "
                     "interchange any two digits in the number 1,478 to make a number that is larger than 5,500. "
                     "(b) Interchange two digits of 10,593 to make a number (i) between 11,000 and 15,000 (ii) more "
                     "than 35,000. (c) Interchange two digits of 48,247 to make a number (i) as small as possible "
                     "(ii) as big as possible.",
                     ["(a) To be larger than 5,500, the thousands digit must be 5 or more. 1,478 has 1 in the "
                      "thousands place, and its digits are 1, 4, 7 and 8.",
                      "Bring 7 or 8 to the thousands place: swap 1 and 7 to get 7,418, or swap 1 and 8 to get 8,471.",
                      "(b)(i) For a number between 11,000 and 15,000, keep 1 in the TTh place and put 1, 2, 3 or 4 "
                      "in the Th place. 10,593 has 0 in the Th place, so swap 0 and 3 to get 13,590.",
                      "Swapping 0 with 5 gives 15,093 and swapping 0 with 9 gives 19,503, both too big. So 13,590 is "
                      "the only way.",
                      "(b)(ii) The TTh digit of 10,593 is 1. Swapping 1 and 3 gives only 30,591, which is less than "
                      "35,000.",
                      "Bring a bigger digit to the TTh place: swap 1 and 5 to get 50,193, or swap 1 and 9 to get "
                      "90,513. Both are more than 35,000.",
                      "(c)(i) 48,247 has the digits 4, 8, 2, 4 and 7. For the smallest number, bring the smallest "
                      "digit, 2, to the TTh place by swapping 4 and 2. The new number is 28,447.",
                      "(c)(ii) For the biggest number, bring the biggest digit, 8, to the TTh place by swapping 4 "
                      "and 8. The new number is 84,247.",
                      "Check: 7,418 is more than 5,500; 13,590 is between 11,000 and 15,000; 50,193 is more than "
                      "35,000; 28,447 is less than 48,247 and 84,247 is more than 48,247."],
                     "(a) 7,418 or 8,471. (b)(i) 13,590. (b)(ii) 50,193 or 90,513. (c)(i) 28,447. (c)(ii) 84,247.")],
          misconceptions=["M_SWAP_VALUE"])],
    key_terms=["digit", "interchange", "biggest number", "smallest number"]))

# ============================== T8 Expanded Form and Tens, Hundreds, Thousands ==============================
TOPICS.append(TOPIC(
    "T8", "M2", "Expanded Form and Tens, Hundreds, Thousands", ["Reading and writing large numbers"], "Apply",
    "Students write numbers in expanded form, write a number as tens, hundreds or thousands plus ones, and find how "
    "many tens, hundreds, thousands and notes a number holds.",
    "A number can be broken into the values of its digits, or counted in tens, hundreds or thousands. It is the same "
    "number in a different form, and a zero holds its place without adding anything.",
    [A("T8.C1", "Expanded form of a number", "Apply",
       "Students write a number in expanded form by adding the value of each digit, and leave out a zero term "
       "while the other digits keep their places.",
       teach=["Predict first: 5,207 has a 0 in the tens place. Will its expanded form have a tens part?",
              "Expanded form breaks a number into the values of its digits. The 5 is in the thousands place, so it "
              "is worth 5,000. The 2 is in the hundreds place, so it is worth 200. The 7 is worth 7.",
              "The 0 in the tens place is worth 0. It adds nothing, so we leave it out of the sum.",
              "The zero still holds the tens place. That is why the other digits do not move.",
              "Rule: add the values of the digits. The sum is the number."],
       examples=[WE("Write 5,207 and 36,050 in expanded form.",
                    ["5,207 has 5 Thousands, 2 Hundreds, 0 Tens and 7 Ones. Their values are 5,000, 200, 0 and 7.",
                     "The 0 adds nothing, so 5,207 = 5,000 + 200 + 7.",
                     "36,050 has 3 Ten Thousands, 6 Thousands, 0 Hundreds, 5 Tens and 0 Ones. Their values are "
                     "30,000, 6,000, 0, 50 and 0.",
                     "Leave out the zeros: 36,050 = 30,000 + 6,000 + 50.",
                     "Check: 5,000 + 200 + 7 = 5,207 and 30,000 + 6,000 + 50 = 36,050."],
                    "5,207 = 5,000 + 200 + 7 and 36,050 = 30,000 + 6,000 + 50")],
       key_terms=["expanded form", "value of a digit"], misconceptions=["M_ZERO_HOLDER"], minutes=7),
     A("T8.C2", "How many tens, hundreds or thousands?", "Apply",
       "Students find how many tens, hundreds and thousands a number holds, write it as tens plus ones, and find how "
       "many notes of 10, 100, 500 and 1,000 it makes.",
       teach=["Predict first: how many ₹10 notes are there in ₹574? Is it the tens digit, 7?",
              "No. One ₹10 note is 10, so count how many tens fit. 50 tens make 500 and 7 more tens make 70, so "
              "there are 57 tens in 574, with 4 ones left.",
              "To count the tens, drop the ones digit. To count the hundreds, drop the last two digits. To count the "
              "thousands, drop the last three digits.",
              "The same number can be grouped in more than one way. 574 = 57 Tens + 4 Ones, and also 50 Tens + 74 "
              "Ones. The number does not change.",
              "Two ₹500 notes make 1,000, so count the thousands and double them. Then see if the rest holds one "
              "more 500."],
       examples=[WE("Find the number of tens, hundreds and thousands in 2,745. Write 2,745 as 200 Tens + __ Ones. How "
                    "many ₹500 notes are there in ₹2,745?",
                    ["Tens: 274 × 10 = 2,740 and 2,745 − 2,740 = 5. So there are 274 tens, with 5 ones left.",
                     "Hundreds: 27 × 100 = 2,700 and 2,745 − 2,700 = 45. So there are 27 hundreds, with 45 left.",
                     "Thousands: 2 × 1,000 = 2,000 and 2,745 − 2,000 = 745. So there are 2 thousands, with 745 left.",
                     "200 Tens is 2,000 and 2,745 − 2,000 = 745, so 2,745 = 200 Tens + 745 Ones.",
                     "₹500 notes: 5 hundreds make one ₹500 note. 27 hundreds hold 5 notes, because 5 × 5 = 25 "
                     "hundreds and 2 hundreds are left over.",
                     "Check: 5 × 500 = 2,500, which is less than ₹2,745, and 6 × 500 = 3,000, which is more."],
                    "274 tens, 27 hundreds and 2 thousands; 2,745 = 200 Tens + 745 Ones; 5 notes of ₹500")],
       key_terms=["tens", "hundreds", "thousands", "notes"], misconceptions=["M_TENS_COUNT"], minutes=8),
     DOER("T8.C3", "Pull it together and do it: Expanded Form and Place Value Counts", None, "Apply",
          "Students write expanded forms, fill tens, hundreds and thousands plus ones, and count the notes of 10, "
          "100 and 500 and the thousands in a number, in the book's questions.",
          ["Expanded form adds the value of each digit. A zero adds nothing but still holds its place.",
           "The number of tens is the number with its ones digit dropped, not the tens digit.",
           "To count a part, take away what the other parts use and see what is left.",
           "Two ₹500 notes make 1,000."],
          items=[FIO("LUDc.Q7", "Let Us Do (place value), Q7 expanded form",
                     "Write the following numbers in the expanded form. One has been done for you. (a) 783 = 700 + "
                     "80 + 3 (b) 8,062 (c) 9,980 (d) 10,304 (e) 23,004 (f) 70,405.",
                     ["(a) is done: 783 = 700 + 80 + 3.",
                      "(b) 8,062 has 8 Thousands, 0 Hundreds, 6 Tens and 2 Ones. Leave out the 0: 8,000 + 60 + 2.",
                      "(c) 9,980 has 9 Thousands, 9 Hundreds, 8 Tens and 0 Ones. Leave out the 0: 9,000 + 900 + 80.",
                      "(d) 10,304 has 1 Ten Thousand, 0 Thousands, 3 Hundreds, 0 Tens and 4 Ones. Leave out the "
                      "zeros: 10,000 + 300 + 4.",
                      "(e) 23,004 has 2 Ten Thousands, 3 Thousands, 0 Hundreds, 0 Tens and 4 Ones. Leave out the "
                      "zeros: 20,000 + 3,000 + 4.",
                      "(f) 70,405 has 7 Ten Thousands, 0 Thousands, 4 Hundreds, 0 Tens and 5 Ones. Leave out the "
                      "zeros: 70,000 + 400 + 5.",
                      "Check: 8,000 + 60 + 2 = 8,062; 9,000 + 900 + 80 = 9,980; 10,000 + 300 + 4 = 10,304; "
                      "20,000 + 3,000 + 4 = 23,004; 70,000 + 400 + 5 = 70,405."],
                     "(b) 8,000 + 60 + 2; (c) 9,000 + 900 + 80; (d) 10,000 + 300 + 4; (e) 20,000 + 3,000 + 4; "
                     "(f) 70,000 + 400 + 5"),
                 FIO("LUDc.Q8ab", "Let Us Do (place value), Q8 tens and ones",
                     "Fill in the blanks with the correct answer. Share your thoughts in class. (a) 983 = 90 Tens + "
                     "83 Ones (b) 68 = ___ Tens + 18 Ones.",
                     ["(a) is done: 90 Tens is 900, so the remaining 83 are Ones.",
                      "(b) The Ones part is 18, so the Tens part is 68 − 18 = 50.",
                      "50 is 5 Tens, because 5 × 10 = 50.",
                      "Check: 5 Tens is 50 and 50 + 18 = 68."],
                     "(b) 5 Tens, so 68 = 5 Tens + 18 Ones."),
                 FIO("LUDc.Q8cg", "Let Us Do (place value), Q8 hundreds, thousands and ones",
                     "Fill in the blanks with the correct answer. (c) 607 = 4 Hundreds + ___ Ones (d) 5,621 = 4 "
                     "Thousand + ___ Hundreds + 2 Tens + ___ Ones (e) 7,069 = ___ Thousand + 20 Hundreds + ___ Ones "
                     "(f) 37,608 = ___ Ten Thousand + 17 Thousand + ___ Hundreds + 8 Ones (g) 43,001 = 3 Ten "
                     "Thousand + ____ Thousand + ____ Hundreds + 1 Ones.",
                     ["(c) 4 Hundreds is 400. 607 − 400 = 207, so the blank is 207 Ones.",
                      "(d) 4 Thousand is 4,000 and 2 Tens is 20. 5,621 − 4,000 − 20 = 1,601 is left.",
                      "1,601 is 16 Hundreds (1,600) and 1 One, so the blanks are 16 Hundreds and 1 Ones.",
                      "(e) 20 Hundreds is 2,000. 7,069 − 2,000 = 5,069 is left, which is 5 Thousand (5,000) and 69 "
                      "Ones.",
                      "(f) 17 Thousand is 17,000 and 8 Ones is 8. 37,608 − 17,000 − 8 = 20,600, which is 2 Ten "
                      "Thousand (20,000) and 6 Hundreds (600).",
                      "(g) 3 Ten Thousand is 30,000 and 1 Ones is 1. 43,001 − 30,000 − 1 = 13,000, which is 13 "
                      "Thousand and 0 Hundreds.",
                      "Check: 4,000 + 1,600 + 20 + 1 = 5,621; 5,000 + 2,000 + 69 = 7,069; 20,000 + 17,000 + 600 + 8 "
                      "= 37,608; 30,000 + 13,000 + 0 + 1 = 43,001."],
                     "(c) 207 Ones; (d) 16 Hundreds and 1 Ones; (e) 5 Thousand and 69 Ones; (f) 2 Ten Thousand and "
                     "6 Hundreds; (g) 13 Thousand and 0 Hundreds"),
                 FIO("LUDc.Q9a", "Let Us Do (place value), Q9 notes in ₹7,934",
                     "Fill in the blanks with the correct answers. (a) How many notes of ₹10 are there in ₹7,934? "
                     "793 (b) How many notes of ₹100 are there in ₹7,934? (c) How many thousands are there in "
                     "7,934? (d) How many ₹500 notes are there in ₹7,934? (Hint: Observe the answer of (c))",
                     ["(a) is done: 793 × 10 = 7,930 and 7,934 − 7,930 = 4, so there are 793 notes of ₹10.",
                      "(b) 79 × 100 = 7,900 and 7,934 − 7,900 = 34, so there are 79 notes of ₹100.",
                      "(c) 7 × 1,000 = 7,000 and 7,934 − 7,000 = 934, so there are 7 thousands.",
                      "(d) Two ₹500 notes make 1,000. From (c), 7 thousands hold 7 × 2 = 14 notes of ₹500.",
                      "The 934 that is left is more than 500, so there is one more note: 14 + 1 = 15.",
                      "Check: 15 × 500 = 7,500, which is less than ₹7,934, and 16 × 500 = 8,000, which is more."],
                     "(b) 79 notes; (c) 7 thousands; (d) 15 notes of ₹500"),
                 FIO("LUDc.Q9b", "Let Us Do (place value), Q9 notes in ₹65,342",
                     "Fill in the blanks with the correct answers. (e) How many notes of ₹10 are there in ₹65,342? "
                     "(f) How many notes of ₹100 are there in ₹65,342? (g) How many thousands are there in 65,342? "
                     "(h) How many ₹500 notes are there in ₹65,342?",
                     ["(e) 6,534 × 10 = 65,340 and 65,342 − 65,340 = 2, so there are 6,534 notes of ₹10.",
                      "(f) 653 × 100 = 65,300 and 65,342 − 65,300 = 42, so there are 653 notes of ₹100.",
                      "(g) 65 × 1,000 = 65,000 and 65,342 − 65,000 = 342, so there are 65 thousands.",
                      "(h) Two ₹500 notes make 1,000. From (g), 65 thousands hold 65 × 2 = 130 notes of ₹500.",
                      "The 342 that is left is less than 500, so there is no more note.",
                      "Check: 130 × 500 = 65,000, which is less than ₹65,342, and 131 × 500 = 65,500, which is more."],
                     "(e) 6,534 notes; (f) 653 notes; (g) 65 thousands; (h) 130 notes of ₹500")],
          misconceptions=["M_ZERO_HOLDER", "M_TENS_COUNT"])],
    key_terms=["expanded form", "tens", "hundreds", "thousands"]))

# ============================== T9 Nearest Numbers ======================================================
TOPICS.append(TOPIC(
    "T9", "M2", "Nearest Numbers", ["Nearest Tens (10s), Hundreds (100s), and Thousands (1,000s)"], "Apply",
    "Students find the nearest ten, hundred and thousand of a number by counting the jumps to its two neighbouring "
    "marks, and write numbers that have the same nearest ten, hundred or thousand.",
    "The nearest ten, hundred or thousand of a number is the neighbouring mark that needs fewer jumps. Check each "
    "line, because the nearest mark can be below or above the number, and different numbers can share one nearest "
    "mark.",
    [A("T9.C1", "The nearest ten", "Understand",
       "Students find the nearest ten of a number by counting the jumps from the number to its two neighbouring "
       "tens and choosing the one with fewer jumps.",
       teach=["Predict first: a rabbit sits at 4,197. Its food is kept at the two neighbouring tens. Which food will "
              "it jump to?",
              "The neighbouring tens are the ten just below and the ten just above. For 4,197 they are 4,190 and "
              "4,200.",
              "Count the jumps. From 4,197 to 4,200 is 3 jumps. From 4,197 to 4,190 is 7 jumps. Fewer jumps means "
              "nearer.",
              "The picture also marks the halfway point of the road, 4,195. The rabbit at 4,197 stands on the 4,200 "
              "side of it.",
              "If the rabbit stood at 4,192, it would be on the 4,190 side. It would need 2 jumps to 4,190 and 8 "
              "jumps to 4,200, so it would go down. The nearest ten can be below or above.",
              "Do not pick the food that looks most like the number. 4,190 shares more digits with 4,197, but 4,200 "
              "is nearer.",
              "Rule: the nearest ten is the neighbouring ten with fewer jumps."],
       examples=[WE("A rabbit is at 4,197. Its food is kept at the neighbouring tens. Which ten is nearest, and how "
                    "many jumps does the rabbit need?",
                    ["The neighbouring tens of 4,197 are 4,190 and 4,200.",
                     "Jumps to 4,200: 4,200 − 4,197 = 3.",
                     "Jumps to 4,190: 4,197 − 4,190 = 7.",
                     "3 is less than 7, so 4,200 is nearer. The rabbit stands to the right of the halfway point "
                     "4,195, on the 4,200 side.",
                     "Check: 3 + 7 = 10, the gap between 4,190 and 4,200."],
                    "4,200 is the nearest ten of 4,197. The rabbit needs 3 jumps.")],
       ncert=["note.rounding"], key_terms=["nearest ten", "jumps", "neighbouring"],
       misconceptions=["M_ROUND_UP", "M_NEAR_FAR"], minutes=7),
     A("T9.C2", "The nearest hundred and the nearest thousand", "Apply",
       "Students find the nearest hundred and the nearest thousand of a number by counting the jumps to the two "
       "neighbouring hundreds or thousands, and see that the two answers can differ.",
       teach=["Predict first: a rabbit is at 6,731. Will it go to the same side for the hundreds line and for the "
              "thousands line?",
              "On the hundreds line the foods are at 6,700 and 6,800. It is 6,731 − 6,700 = 31 jumps to 6,700 and "
              "6,800 − 6,731 = 69 jumps to 6,800.",
              "On the thousands line the foods are at 6,000 and 7,000. It is 6,731 − 6,000 = 731 jumps to 6,000 and "
              "7,000 − 6,731 = 269 jumps to 7,000.",
              "So the nearest hundred of 6,731 is 6,700, below it, and the nearest thousand is 7,000, above it. Each "
              "line has its own two neighbours.",
              "Rule: choose the line, find the two neighbours, count the jumps to each and choose the fewer."],
       examples=[WE("A rabbit is at 6,731. Find its nearest hundred and its nearest thousand, with the jumps.",
                    ["Hundreds: the neighbours of 6,731 are 6,700 and 6,800.",
                     "6,731 − 6,700 = 31 jumps and 6,800 − 6,731 = 69 jumps. 31 is less than 69, so the nearest "
                     "hundred is 6,700.",
                     "Thousands: the neighbours of 6,731 are 6,000 and 7,000.",
                     "6,731 − 6,000 = 731 jumps and 7,000 − 6,731 = 269 jumps. 269 is less than 731, so the nearest "
                     "thousand is 7,000.",
                     "Check: 31 + 69 = 100 and 731 + 269 = 1,000, the gaps between the neighbours."],
                    "The nearest hundred of 6,731 is 6,700 (31 jumps) and the nearest thousand is 7,000 "
                    "(269 jumps)")],
       key_terms=["nearest hundred", "nearest thousand", "jumps"], misconceptions=["M_ROUND_UP", "M_NEAR_FAR"],
       minutes=7),
     A("T9.C3", "Numbers with the same nearest number", "Analyze",
       "Students write two numbers that have the same nearest ten, hundred or thousand, and check their choice by "
       "counting the jumps of each number to both neighbours.",
       teach=["Predict first: can two different numbers have the same nearest hundred? Think of the rabbit and its "
              "food.",
              "Yes. Each food has numbers on both sides of it that are nearer to it than to any other food. Those "
              "numbers share the same nearest number.",
              "A number very close to a thousand, such as 8,000, is also close to the nearest hundred and the "
              "nearest ten, which are the same 8,000.",
              "To check two numbers, count the jumps of each to both of its neighbours on that line.",
              "Rule: two numbers have the same nearest number when both are nearer to the same food on that line."],
       examples=[WE("(a) Write two numbers that have the same nearest hundred. (b) Write two numbers that have the "
                    "same nearest ten, nearest hundred and nearest thousand.",
                    ["(a) Pick the hundred 5,400 and take one number below it and one above it: 5,380 and 5,420.",
                     "5,380 needs 5,400 − 5,380 = 20 jumps to 5,400 and 5,380 − 5,300 = 80 jumps to 5,300. 5,420 "
                     "needs 5,420 − 5,400 = 20 jumps to 5,400 and 5,500 − 5,420 = 80 jumps to 5,500. Both have "
                     "the nearest hundred 5,400.",
                     "(b) Pick the thousand 8,000 and take two numbers very close to it: 7,997 and 8,002.",
                     "Nearest ten: 7,997 needs 3 jumps to 8,000 and 7,997 − 7,990 = 7 jumps to 7,990. 8,002 needs "
                     "2 jumps to 8,000 and 8,010 − 8,002 = 8 jumps to 8,010. Both give 8,000.",
                     "Nearest hundred: 7,997 needs 3 jumps to 8,000 and 7,997 − 7,900 = 97 jumps to 7,900. 8,002 "
                     "needs 2 jumps to 8,000 and 8,100 − 8,002 = 98 jumps to 8,100. Both give 8,000.",
                     "Nearest thousand: 7,997 needs 3 jumps to 8,000 and 7,997 − 7,000 = 997 jumps to 7,000. 8,002 "
                     "needs 2 jumps to 8,000 and 9,000 − 8,002 = 998 jumps to 9,000. Both give 8,000."],
                    "(a) 5,380 and 5,420, nearest hundred 5,400. (b) 7,997 and 8,002, nearest ten, nearest hundred "
                    "and nearest thousand all 8,000.")],
       key_terms=["same nearest number", "nearest ten", "nearest hundred", "nearest thousand"],
       misconceptions=["M_NEAR_FAR"], minutes=8),
     DOER("T9.C4", "Practice: Nearest Numbers", "rounding_line", "Apply",
          "Students find the nearest ten, hundred and thousand of a number by counting jumps to the two neighbouring "
          "marks, fill the table, and write numbers that have the same nearest number.",
          ["Find the two neighbouring marks of the number on the line.",
           "Count the jumps to each mark. The nearer mark has fewer jumps.",
           "Check the tens, hundreds and thousands lines one by one. The nearest mark can be below or above the "
           "number."],
          items=[FIO("rab.tens", "Nearest Numbers (rabbit), the neighbouring tens",
                     "A rabbit is hungry. The rabbit is at 2,346. Its food has been kept at its neighbouring tens, "
                     "2,340 and 2,350. On which tens should the rabbit go to get its food, with the least number of "
                     "steps?",
                     ["The neighbouring tens of 2,346 are 2,340 and 2,350.",
                      "Jumps to 2,350: 2,350 − 2,346 = 4.",
                      "Jumps to 2,340: 2,346 − 2,340 = 6.",
                      "4 is less than 6, so 2,350 is nearer.",
                      "Check: 4 + 6 = 10, the gap between 2,340 and 2,350, and the rabbit stands just to the right "
                      "of the halfway mark 2,345."],
                     "2,350 is the nearest ten of 2,346. It will need 4 jumps to reach 2,350.",
                     kind="example",
                     q_figure="A road drawn as a line with a carrot at 2,340 on the left end and a carrot at 2,350 "
                              "on the right end, a mark at 2,345 in the middle and a rabbit just to the right of "
                              "that mark at 2,346.",
                     s_figure="The same road with an arrow of 4 jumps from the rabbit to the carrot at 2,350 and an "
                              "arrow of 6 jumps to the carrot at 2,340."),
                 FIO("rab.hundreds", "Nearest Numbers (rabbit), the neighbouring hundreds",
                     "The rabbit is at 2,346. Its food has been kept at its neighbouring hundreds, 2,300 and 2,400. "
                     "Which of the two hundreds should the rabbit go to? ___ is the nearest hundred of 2,346. It "
                     "will need ___ jumps to reach ___.",
                     ["The neighbouring hundreds of 2,346 are 2,300 and 2,400.",
                      "Jumps to 2,300: 2,346 − 2,300 = 46.",
                      "Jumps to 2,400: 2,400 − 2,346 = 54.",
                      "46 is less than 54, so 2,300 is nearer.",
                      "Check: 46 + 54 = 100, and the rabbit stands to the left of the halfway mark 2,350."],
                     "2,300 is the nearest hundred of 2,346. It will need 46 jumps to reach 2,300.",
                     kind="prompt",
                     q_figure="A road drawn as a line with a carrot at 2,300 on the left end and a carrot at 2,400 "
                              "on the right end, a mark at 2,350 in the middle and a rabbit just to the left of "
                              "that mark at 2,346.",
                     s_figure="The same road with an arrow of 46 jumps from the rabbit to the carrot at 2,300 and an "
                              "arrow of 54 jumps to the carrot at 2,400."),
                 FIO("rab.thousands", "Nearest Numbers (rabbit), the neighbouring thousands",
                     "The rabbit is at 2,346. Its food has been kept at its neighbouring thousands, 2,000 and 3,000. "
                     "Which number should the rabbit go to? ___ is the nearest thousand of 2,346. It will need ___ "
                     "jumps to reach ___.",
                     ["The neighbouring thousands of 2,346 are 2,000 and 3,000.",
                      "Jumps to 2,000: 2,346 − 2,000 = 346.",
                      "Jumps to 3,000: 3,000 − 2,346 = 654.",
                      "346 is less than 654, so 2,000 is nearer.",
                      "Check: 346 + 654 = 1,000, and the rabbit stands to the left of the halfway mark 2,500."],
                     "2,000 is the nearest thousand of 2,346. It will need 346 jumps to reach 2,000.",
                     kind="prompt",
                     q_figure="A road drawn as a line with a carrot at 2,000 on the left end and a carrot at 3,000 "
                              "on the right end, a mark at 2,500 in the middle and a rabbit on the left part of the "
                              "road at 2,346.",
                     s_figure="The same road with an arrow of 346 jumps from the rabbit to the carrot at 2,000 and "
                              "an arrow of 654 jumps to the carrot at 3,000."),
                 FIO("rab.table", "Nearest Numbers (table), tens, hundreds and thousands",
                     "Fill in the boxes appropriately. Find the nearest tens, nearest hundreds and nearest "
                     "thousands of 3,176, 4,017, 5,789 and 8,203.",
                     ["3,176, tens: 3,176 − 3,170 = 6 jumps and 3,180 − 3,176 = 4 jumps, so 3,180.",
                      "3,176, hundreds: 76 jumps to 3,100 and 24 jumps to 3,200, so 3,200. Thousands: 176 jumps to "
                      "3,000 and 824 jumps to 4,000, so 3,000.",
                      "4,017, tens: 7 jumps to 4,010 and 3 jumps to 4,020, so 4,020. Hundreds: 17 jumps to 4,000 and "
                      "83 jumps to 4,100, so 4,000. Thousands: 17 jumps to 4,000 and 983 jumps to 5,000, so 4,000.",
                      "5,789, tens: 9 jumps to 5,780 and 1 jump to 5,790, so 5,790. Hundreds: 89 jumps to 5,700 and "
                      "11 jumps to 5,800, so 5,800. Thousands: 789 jumps to 5,000 and 211 jumps to 6,000, so 6,000.",
                      "8,203, tens: 3 jumps to 8,200 and 7 jumps to 8,210, so 8,200. Hundreds: 3 jumps to 8,200 and "
                      "97 jumps to 8,300, so 8,200. Thousands: 203 jumps to 8,000 and 797 jumps to 9,000, so 8,000.",
                      "Check: the two jumps of each line add up to the gap, for example 6 + 4 = 10, 76 + 24 = 100 and "
                      "176 + 824 = 1,000."],
                     "3,176: 3,180; 3,200; 3,000. 4,017: 4,020; 4,000; 4,000. 5,789: 5,790; 5,800; 6,000. 8,203: "
                     "8,200; 8,200; 8,000.",
                     kind="prompt",
                     q_figure="A table with the headings Number, Nearest Tens, Nearest Hundreds and Nearest "
                              "Thousands, four rows 3,176, 4,017, 5,789 and 8,203, and an empty box in every other "
                              "column.",
                     s_figure="The same table with every box filled."),
                 FIO("LUT.Q1", "Let Us Think (nearest numbers), Q1 Vijay and Suma",
                     "Vijay rounded off a number to the nearest hundred. Suma rounded off the same number to the "
                     "nearest thousand. Both got the same result. Circle the numbers they might have used. 7,126, "
                     "7,835, 7,030, 6,999.",
                     ["Find the nearest hundred and the nearest thousand of each number.",
                      "7,126: 26 jumps to 7,100 and 74 jumps to 7,200, so 7,100. 126 jumps to 7,000 and 874 jumps "
                      "to 8,000, so 7,000. The results are different.",
                      "7,835: 35 jumps to 7,800 and 65 jumps to 7,900, so 7,800. 835 jumps to 7,000 and 165 jumps "
                      "to 8,000, so 8,000. The results are different.",
                      "7,030: 30 jumps to 7,000 and 70 jumps to 7,100, so 7,000. 30 jumps to 7,000 and 970 jumps to "
                      "8,000, so 7,000. The results are the same.",
                      "6,999: 99 jumps to 6,900 and 1 jump to 7,000, so 7,000. 999 jumps to 6,000 and 1 jump to "
                      "7,000, so 7,000. The results are the same.",
                      "Check: 7,030 is 30 above 7,000 and 6,999 is 1 below 7,000, so both stand right next to 7,000."],
                     "7,030 and 6,999 (both give 7,000)",
                     kind="exercise"),
                 FIO("LUT.Q2", "Let Us Think (nearest numbers), Q2 same nearest ten, hundred, thousand",
                     "Think and write two numbers that have the same (a) Nearest ten. (b) Nearest hundred. (c) "
                     "Nearest thousand. For example, 19 and 21 have the same nearest ten, that is, 20.",
                     ["(a) Pick the ten 3,140. 3,138 is 2 jumps below it and 3,142 is 2 jumps above it.",
                      "The other tens are far: 3,138 − 3,130 = 8 jumps and 3,150 − 3,142 = 8 jumps. Both have the "
                      "nearest ten 3,140.",
                      "(b) Pick the hundred 4,500. 4,480 is 20 jumps below it and 4,520 is 20 jumps above it.",
                      "The other hundreds are far: 4,480 − 4,400 = 80 jumps and 4,600 − 4,520 = 80 jumps. Both have "
                      "the nearest hundred 4,500.",
                      "(c) Pick the thousand 6,000. 5,900 is 100 jumps below it and 6,200 is 200 jumps above it.",
                      "The other thousands are far: 5,900 − 5,000 = 900 jumps and 7,000 − 6,200 = 800 jumps. Both "
                      "have the nearest thousand 6,000.",
                      "Check: 3,138 and 3,142 are both 2 from 3,140, 4,480 and 4,520 are both 20 from 4,500, and "
                      "5,900 and 6,200 are much nearer to 6,000 than to 5,000 or 7,000."],
                     "Sample answer: (a) 3,138 and 3,142; (b) 4,480 and 4,520; (c) 5,900 and 6,200. Your answer may "
                     "differ.",
                     kind="exercise"),
                 FIO("LUT.Q3", "Let Us Think (nearest numbers), Q3 same in two or three places",
                     "Think and write the numbers that have the same (a) Nearest ten and nearest hundred. (b) "
                     "Nearest hundred and nearest thousand. (c) Nearest ten, hundred and thousand.",
                     ["(a) Pick the hundred 5,300 and numbers right next to it: 5,297 is 3 jumps below it and 5,302 "
                      "is 2 jumps above it.",
                      "Their nearest ten is also 5,300: 5,297 is 7 jumps from 5,290 and 5,302 is 8 jumps from "
                      "5,310. Both give 5,300 for the ten and for the hundred.",
                      "(b) Pick the thousand 8,000. 7,970 is 30 jumps below it and 8,030 is 30 jumps above it. The "
                      "other thousands are 970 jumps away, so both give 8,000.",
                      "Their nearest hundred is also 8,000: 7,970 is 70 jumps from 7,900 and 8,030 is 70 jumps from "
                      "8,100.",
                      "(c) Pick 4,000 and numbers very close to it: 3,998 is 2 jumps below it and 4,003 is 3 jumps "
                      "above it.",
                      "The other tens are 3,998 − 3,990 = 8 and 4,010 − 4,003 = 7 jumps away. The other hundreds "
                      "are 3,998 − 3,900 = 98 and 4,100 − 4,003 = 97 jumps away. The other thousands are 3,998 − "
                      "3,000 = 998 and 5,000 − 4,003 = 997 jumps away.",
                      "So 3,998 and 4,003 both have the nearest ten, hundred and thousand 4,000.",
                      "Check: 5,297 and 5,302 are within 3 of 5,300, 7,970 and 8,030 are 30 from 8,000, and 3,998 and "
                      "4,003 are within 3 of 4,000, far less than the jumps to the other marks."],
                     "Sample answer: (a) 5,297 and 5,302; (b) 7,970 and 8,030; (c) 3,998 and 4,003. Your answer may "
                     "differ.",
                     kind="exercise")],
          misconceptions=["M_ROUND_UP", "M_NEAR_FAR"])],
    key_terms=["nearest ten", "nearest hundred", "nearest thousand", "jumps"]))
