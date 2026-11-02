# -*- coding: utf-8 -*-
"""Topics T7 to T12: the number line, the unmarked number line, tokens, credits and debits, heights and
temperatures. Book sections 10.1 (second half), 10.2 and 10.3."""
from topics_common import A, DOER, TOPIC, book, fio, we

TOPICS = []
S = "10.1"
H_ANY = "Adding, subtracting, and comparing any numbers"
H_NL = "Back to the number line"
H_UNL = "Using the unmarked number line to add and subtract"
H_CONV = "Converting subtraction to addition and addition to subtraction"
T_ADD = "Using tokens for addition"
T_SUB = "Using tokens for subtraction"

# ============================== T7 The number line (10.1) ====================================================
TOPICS.append(TOPIC(
    "T7", "M2", "Back to the Number Line", [S], "Apply",
    "Students turn the endless lift into the number line, and find the movement between two numbers on it as a "
    "subtraction and an addition.",
    "Turn the endless lift on its side and it is a number line: right is positive, left is negative, smaller "
    "numbers sit to the left of bigger ones.",
    [A("T7.C1", "The lift is a number line", "Understand",
       "Students see that rotating the endless lift by 90° gives a number line, and say how the two are alike.",
       textbook=book(S, H_ANY, start=8) + book(S, H_NL, stop=4),
       teach=["Think first: picture the endless lift lying on its side. What does it remind you of?",
              "It becomes a number line: to the right is the positive (forward) direction and to the left is the "
              "negative (backward) direction.",
              "So the number ray from the start of the chapter is completed into a true number line, and smaller "
              "numbers lie to the left of bigger numbers: −5 < −3 and −3 < 2."],
       examples=[we("10.1.q17")],
       key_terms=["number line"], misconceptions=["M_NEG_NOTHING", "M_BIGGER_DIGIT"], minutes=8),
     A("T7.C2", "Travelling along the number line", "Apply",
       "Students find how far and in which direction to move from one number to another on the number line, and "
       "write the matching addition and subtraction.",
       textbook=book(S, H_NL, start=4, stop=14),
       teach=["Think first: from 5 you want to reach 9. How many steps do you take, and in which direction?",
              "Four steps forward: 5 + 4 = 9, and 9 − 5 = 4. From 9 to 3 you go six steps backward, which is "
              "−6, so 9 + (−6) = 3 and 3 − 9 = −6.",
              "From 3 to −2 you go five steps backward: 3 + (−5) = −2 and (−2) − 3 = −5. In every case Starting "
              "Number + Movement = Target Number."],
       examples=[we("10.1.q18"), we("10.1.q19"), we("10.1.q20")],
       key_terms=["steps", "forward", "backward"], misconceptions=["M_DISTANCE_ONLY", "M_START_MINUS_TARGET"],
       minutes=10),
     DOER("T7.C3", "Pull it together and do it: Walk the Number Line", "number_line_walker", "Apply",
          "Students mark positive and negative numbers, compare them on the line and walk from one number to "
          "another to complete sums and differences.",
          ["Right is positive and left is negative; smaller numbers lie to the left.",
           "Starting Number + Movement = Target Number.",
           "Target Number − Starting Number = Movement needed."],
          items=[fio("10.1.FiO6.Q1"), fio("10.1.FiO6.Q2"), fio("10.1.FiO6.Q3"), fio("10.1.FiO6.Q4")],
          misconceptions=["M_BIGGER_DIGIT", "M_DISTANCE_ONLY"])]))

# ============================== T8 Unmarked number line and converting subtraction (10.1) ====================
TOPICS.append(TOPIC(
    "T8", "M2", "The Unmarked Number Line", [S], "Apply",
    "Students use an unmarked number line to add and subtract large integers, and change a subtraction into an "
    "addition of the inverse.",
    "An unmarked number line shows only zero and the scale you imagine, and any subtraction can be turned into "
    "adding the inverse.",
    [A("T8.C1", "Adding on an unmarked number line", "Apply",
       "Students show a sum of large integers on an unmarked number line and read off the result.",
       textbook=book(S, H_UNL, stop=4),
       teach=["Think first: how would you find 85 + (−60) without drawing every number from 0 to 85?",
              "Draw a line that shows only 0, mark 85, then move 60 to the left. The scale is imagined.",
              "You land at 25, so 85 + (−60) = 25. A rough line is enough when only the movement matters."],
       examples=[we("10.1.ex7")],
       key_terms=["unmarked number line"], misconceptions=["M_IGNORE_SIGN"], minutes=8),
     A("T8.C2", "Subtracting on an unmarked number line", "Apply",
       "Students show a subtraction as a missing addend on an unmarked number line and read off the movement.",
       textbook=book(S, H_UNL, start=4),
       teach=["Think first: for (−100) − (+250), what number added to 250 gives −100?",
              "Start at 250 and travel to −100: you pass 0 after 250 steps backward and go 100 more, in all 350 "
              "steps backward.",
              "So the missing number is −350. The same line also evaluates a list of sums and differences."],
       examples=[we("10.1.ex8"), we("10.1.q21")],
       key_terms=["missing addend"], misconceptions=["M_DISTANCE_ONLY", "M_START_MINUS_TARGET"], minutes=10),
     A("T8.C3", "Subtraction becomes addition of the inverse", "Understand",
       "Students rewrite a subtraction as the addition of the inverse, and check it on the number line.",
       textbook=book(S, H_CONV),
       teach=["Think first: from 2 to −3 the movement needed is −3 − 2. Can you find the same movement in two "
              "steps that need no subtraction?",
              "Go from 2 to 0, which is −2, and then from 0 to −3, which is −3. Together −3 + (−2) = −5.",
              "So subtracting a number is the same as adding its inverse, and adding a number is the same as "
              "subtracting its inverse."],
       examples=[we("10.1.q22"), we("10.1.ex9")],
       key_terms=["inverse", "convert subtraction"], misconceptions=["M_SUB_NEG_SMALLER", "M_INVERSE_RECIP"],
       minutes=10),
     DOER("T8.C4", "Pull it together and do it: Sub to Add", None, "Apply",
          "Students rewrite subtractions as additions of the inverse and say what each pair of expressions "
          "shares.",
          ["A subtraction can be written as the addition of the inverse.",
           "An unmarked number line needs only zero and the movement.",
           "Both forms give the same target number."],
          misconceptions=["M_SUB_NEG_SMALLER"])]))

# ============================== T9 Tokens for addition (10.2) ================================================
TOPICS.append(TOPIC(
    "T9", "M3", "Adding with Tokens", ["10.2"], "Apply",
    "Students add integers with green positive tokens and red negative tokens, cancelling zero pairs.",
    "A positive token and a negative token cancel to zero, so a set of tokens is read by removing zero pairs.",
    [A("T9.C1", "A pocket of tokens", "Understand",
       "Students read the lift attendant's tokens as a floor number by counting positive and negative tokens.",
       textbook=book("10.2", T_ADD, stop=6),
       teach=["Think first: the lift attendant starts on Floor 0 and collects a green token for every '+' press "
              "and a red token for every '−' press. After an hour he holds 5 green and 3 red tokens. Which floor "
              "is he on?",
              "He pressed '+' five times and '−' three times, so (+5) + (−3) = +2. A green token and a red token "
              "make a zero pair.",
              "Cancel three zero pairs and two green tokens remain, so he is on Floor +2."],
       examples=[we("10.2.q1")],
       key_terms=["token", "zero pair"], misconceptions=["M_TOKEN_COUNT", "M_ZERO_PAIR_CHANGES"], minutes=8),
     A("T9.C2", "Adding by cancelling zero pairs", "Apply",
       "Students add two integers of different sign by cancelling zero pairs and reading what is left.",
       textbook=book("10.2", T_ADD, start=6, stop=8),
       teach=["Think first: to add +5 and −8 with tokens, how many zero pairs can you find?",
              "Put down 5 green and 8 red tokens. Remove five zero pairs, and three red tokens remain.",
              "So (+5) + (−8) = −3. The sign of the answer is the colour of the tokens left over."],
       examples=[we("10.2.ex1")],
       key_terms=["zero pair", "token"], misconceptions=["M_IGNORE_SIGN", "M_ZERO_PAIR_CHANGES"], minutes=8),
     DOER("T9.C3", "Pull it together and do it: Token Board", "token_board", "Apply",
          "Students add integers by putting down green and red tokens, cancelling zero pairs and reading the floor.",
          ["Green is positive and red is negative.",
           "A green and a red token cancel to zero.",
           "What is left after cancelling is the sum."],
          items=[fio("10.2.FiO1.Q1"), fio("10.2.FiO1.Q2")], misconceptions=["M_TOKEN_COUNT", "M_IGNORE_SIGN"])]))

# ============================== T10 Tokens for subtraction (10.2) ============================================
TOPICS.append(TOPIC(
    "T10", "M3", "Subtracting with Tokens", ["10.2"], "Apply",
    "Students subtract integers with tokens, taking tokens away and putting in zero pairs when there are not "
    "enough tokens to take.",
    "To subtract, take tokens away; when there are not enough of the kind to take, add zero pairs, which do not "
    "change the value.",
    [A("T10.C1", "Taking tokens away", "Apply",
       "Students subtract by taking tokens off the board when there are enough of that kind.",
       textbook=book("10.2", T_SUB, stop=4),
       teach=["Think first: from 5 green tokens, take away 4 green tokens. What is left?",
              "One green token is left, so (+5) − (+4) = +1. With red tokens, from 7 red take away 5 red and "
              "2 red are left: (−7) − (−5) = −2.",
              "Taking away 5 red tokens gives the same result as adding 5 green tokens: (−7) − (−5) and "
              "(−7) + (+5) are both −2."],
       examples=[we("10.2.ex2"), we("10.2.ex3"), we("10.2.q2")],
       key_terms=["take away", "token"], misconceptions=["M_SUB_NEG_SMALLER", "M_TOKEN_COUNT"], minutes=8),
     A("T10.C2", "Not enough tokens: put in a zero pair", "Apply",
       "Students subtract a larger positive from a smaller positive by adding a zero pair first.",
       textbook=book("10.2", T_SUB, start=4, stop=7),
       teach=["Think first: you have 5 green tokens and must take away 6 green tokens. What can you do?",
              "Put out an extra zero pair, one green and one red. The value stays the same, and now there are 6 "
              "green tokens to take.",
              "Take them away and one red token is left, so (+5) − (+6) = −1."],
       examples=[we("10.2.ex4")],
       key_terms=["zero pair"], misconceptions=["M_ZERO_PAIR_CHANGES", "M_SUB_SMALLER"], minutes=8),
     A("T10.C3", "Taking away a negative token", "Apply",
       "Students subtract a negative number by adding enough zero pairs and taking the red tokens away.",
       textbook=book("10.2", T_SUB, start=10, stop=15),
       teach=["Think first: start with 4 green tokens and take out 6 red tokens. There are no red tokens to take. "
              "What now?",
              "Add 6 zero pairs, which does not change the value. Now there are 6 red tokens to take away, and "
              "10 green tokens remain.",
              "So (+4) − (−6) = +10. Taking away a negative token gives a positive result."],
       examples=[we("10.2.ex5")],
       key_terms=["zero pair", "subtract a negative"], misconceptions=["M_SUB_NEG_SMALLER", "M_ZERO_PAIR_CHANGES"],
       minutes=10),
     DOER("T10.C4", "Pull it together and do it: Token Taker", "token_taker", "Apply",
          "Students subtract integers with tokens, adding zero pairs when they need more tokens to take away.",
          ["Take tokens away when there are enough.",
           "When there are not enough, add zero pairs until there are; the value does not change.",
           "Count the zero pairs added and read what is left."],
          items=[fio("10.2.FiO2.Q1"), fio("10.2.FiO2.Q2"), fio("10.2.FiO3.Q1"), fio("10.2.FiO3.Q2")],
          misconceptions=["M_ZERO_PAIR_CHANGES", "M_SUB_NEG_SMALLER"])]))

# ============================== T11 Credits and debits (10.3) ================================================
TOPICS.append(TOPIC(
    "T11", "M3", "Credits and Debits", ["10.3"], "Apply",
    "Students read credits as positive and debits as negative, follow a bank balance day by day, and see that a "
    "balance can go below zero.",
    "A credit adds and a debit takes away, and the total of all credits and debits is the bank balance, which can "
    "be negative.",
    [A("T11.C1", "Credit goes up, debit goes down", "Apply",
       "Students follow a savings account and say how each credit and each debit changes the balance.",
       textbook=book("10.3", "Credits and debits", stop=5),
       teach=["Think first: you open an account with ₹100, add ₹60 the next day and pay a ₹30 bill the day "
              "after. What is the balance now?",
              "The ₹60 deposited is a credit, so the balance is ₹160. The ₹30 paid is a debit, so the balance is "
              "now ₹130.",
              "Credits behave like positive numbers and debits like negative numbers."],
       examples=[we("10.3.q1"), we("10.3.q2")],
       key_terms=["credit", "debit", "balance"], misconceptions=["M_ADD_BIGGER"], minutes=8),
     A("T11.C2", "A balance below zero", "Understand",
       "Students find a balance after a debit larger than the balance, and say that it is a negative balance.",
       textbook=book("10.3", "Credits and debits", start=5, stop=12),
       teach=["Think first: your balance is ₹130 and you buy something for ₹150. Is that possible?",
              "Some banks allow it for a while. The balance is 130 − 150 = −20, and a later credit of ₹200 "
              "brings it to −20 + 200 = 180.",
              "The total of all credits (positive) and debits (negative) is the balance, which can be positive or "
              "negative. It is better to keep it positive."],
       examples=[we("10.3.q3"), we("10.3.q4")],
       key_terms=["negative balance"], misconceptions=["M_NO_NEG_BALANCE"], minutes=8),
     DOER("T11.C3", "Pull it together and do it: Passbook", None, "Apply",
          "Students total a list of credits and debits to find a balance and say what a negative balance means.",
          ["Credits are positive and debits are negative.",
           "The balance is the total of all of them, in any order.",
           "A negative balance means money is owed."],
          items=[fio("10.3.FiO1.Q1"), fio("10.3.FiO1.Q2"), fio("10.3.FiO1.Q3")],
          misconceptions=["M_NO_NEG_BALANCE", "M_ADD_BIGGER"])]))

# ============================== T12 Heights and temperatures (10.3) ==========================================
TOPICS.append(TOPIC(
    "T12", "M3", "Heights and Temperatures", ["10.3"], "Apply",
    "Students use sea level as 0 for heights and the freezing point as 0 for temperatures, and read, compare and "
    "order integers there.",
    "Heights are measured from sea level and temperatures from 0 °C; below those points the numbers are negative, "
    "and deeper or colder means smaller.",
    [A("T12.C1", "Heights from sea level", "Understand",
       "Students read heights above and below sea level as positive and negative numbers and compare them.",
       textbook=book("10.3", "Geographical cross sections"),
       teach=["Think first: a mountain top is above the sea and the ocean floor is below it. How could one scale "
              "measure both?",
              "Height is measured from sea level, which is 0 m. Heights above sea level are positive and heights "
              "below are negative.",
              "A point at −1200 m is lower than a point at −200 m, so the deeper point is the smaller number."],
       key_terms=["sea level", "height"], misconceptions=["M_DEEPER_HIGHER"], minutes=8),
     A("T12.C2", "Temperatures below zero", "Understand",
       "Students read a thermometer in °C, say what a negative reading means, and compare temperatures.",
       textbook=book("10.3", "Temperature", stop=3),
       teach=["Think first: a thermometer shows 40 °C on a hot day and 15 °C on a cool one. Can it show a number "
              "below 0?",
              "Yes. On a very cold day the temperature can be −4 °C, which is 4 degrees below the freezing "
              "point of water.",
              "Colder means a smaller number: −4 °C is colder than −2 °C, and every temperature below 0 is "
              "colder than every temperature above 0."],
       examples=[we("10.3.q5"), we("10.3.q6", q="Look at the two thermometers showing 40 °C and 15 °C. How could a "
                                              "thermometer show a temperature below 0 °C, and what would it mean?",
                   steps=["The scale of the thermometer continues below 0 °C.",
                          "A reading below 0 °C is a negative number: the temperature is below the freezing point "
                          "of water."],
                   answer="A thermometer can show a negative reading below 0 °C, for example −4 °C, which is colder "
                          "than 0 °C.")],
       key_terms=["temperature", "degrees Celsius"], misconceptions=["M_NEG_NOTHING", "M_BIGGER_DIGIT"], minutes=8),
     DOER("T12.C3", "Pull it together and do it: Sea Level and Freezing Point", None, "Apply",
          "Students fill in heights from a cross section, order them, name the highest and lowest places on Earth "
          "and match temperatures to times.",
          ["Sea level is 0 m and the freezing point of water is 0 °C.",
           "Higher or warmer means a greater number; deeper or colder means a smaller number.",
           "Order negative numbers by how far below zero they are, deeper being smaller."],
          items=[fio("10.3.FiO2.Q1"), fio("10.3.FiO2.Q2"), fio("10.3.FiO2.Q3"), fio("10.3.FiO2.Q4"),
                 fio("10.3.FiO2.Q5"), fio("10.3.FiO3.Q1"), fio("10.3.FiO3.Q2")],
          misconceptions=["M_DEEPER_HIGHER", "M_BIGGER_DIGIT"])]))
