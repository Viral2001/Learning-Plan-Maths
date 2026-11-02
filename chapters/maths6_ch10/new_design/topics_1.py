# -*- coding: utf-8 -*-
"""Topics T1 to T6 (modules M1 and the start of M2). Chapter opening and book section 10.1, first half."""
from topics_common import A, DOER, TOPIC, BOOK_TEXT, book, fio, we

TOPICS = []
S = "10.1"
H_NUM = "Numbering the floors in the building of fun"
H_ADD = "Addition to keep track of movement"
H_COMB = "Combining button presses is also addition"
H_ZERO = "Back to zero!"
H_CMP = "Comparing numbers using floors"
H_SUB = "Subtraction to find which button to press"
H_MINE = "Adding and subtracting larger numbers"
H_ANY = "Adding, subtracting, and comparing any numbers"
OPEN = [x.replace("—", ", ") for x in BOOK_TEXT["extra_inv_A.json"]["opening"]["textbook_lines"]]

# ============================== T1 Chapter opening ===========================================================
TOPICS.append(TOPIC(
    "T1", "M1", "More and More Numbers", ["Chapter opening"], "Understand",
    "",
    "Counting numbers, zero and fractions came one after another, and the number ray stops at 0, so the question "
    "is whether there are numbers on the other side of zero.",
    [A("T1.C1", "Can a number be less than zero?", "Remember", "",
       textbook=OPEN[2:],
       teach=["Think first: the number ray starts at 0 and runs to the right. Can you think of a time when you "
              "had less than zero of something?",
              "Counting numbers came first, then 0 before 1, then fractions between the numbers. Each time, the "
              "numbers grew by something new.",
              "Now the question is the one on the other side of zero: is there a number that comes before 0 and "
              "is less than 0? That is what this chapter investigates."],
       examples=[],
       key_terms=["number line", "zero"], misconceptions=["M_NEG_NOTHING"], video_focus=["HOOK"], minutes=4,
       enrichment=True)],
    topic_type="framing"))

# ============================== T2 Floors above and below the ground (10.1) ==================================
TOPICS.append(TOPIC(
    "T2", "M1", "Floors Above and Below the Ground", [S], "Understand",
    "Students name the floors above and below the ground in Bela's Building of Fun, read a lift button press as "
    "a number, and number every floor with the ground floor as Floor 0.",
    "Floors above the ground are positive, floors below are negative, the ground floor is Floor 0, and a press of "
    "the lift is a number too.",
    [A("T2.C1", "Floors below the ground", "Understand",
       "Students point out the floors that lie below the ground in the Building of Fun and say what the ground "
       "floor holds.",
       textbook=book(S, None, stop=3),
       teach=["Think first: a building can go up, but can a floor go below the ground? What would you find "
              "there?",
              "In Bela's Building of Fun, some floors are below the ground: a Toy Store, a Video Games shop, a "
              "Cinema, a Ghost House and a Dinosaur floor.",
              "The ground floor is the Welcome Hall. So there are places that are not above the start but below "
              "it, and we need numbers for them."],
       examples=[we("10.1.q1")],
       key_terms=["ground floor", "below the ground"], misconceptions=["M_NEG_NOTHING", "M_BELOW_POSITIVE"],
       minutes=6),
     A("T2.C2", "The lift buttons are numbers", "Understand",
       "Students read pressing '+' as going up, pressing '−' as going down, and write four floors up and three "
       "floors down as +4 and −3.",
       textbook=book(S, None, start=3, stop=10),
       teach=["Think first: the lift has two buttons, '+' and '−'. If you press '+' four times, what single "
              "number could stand for that?",
              "Each '+' press takes you up one floor and each '−' press takes you down one floor. Four '+' presses "
              "are written +4, and three '−' presses are written −3.",
              "So a button press is a number with a direction: the sign says up or down, and the number says how "
              "many floors."],
       examples=[we("10.1.q2"), we("10.1.q3")],
       key_terms=["lift", "button press"], misconceptions=["M_BUTTON_ADD_ONLY"], minutes=8),
     A("T2.C3", "Floor numbers and Floor 0", "Understand",
       "Students number every floor of the Building of Fun from the ground floor, and explain why the ground "
       "floor is Floor 0.",
       textbook=book(S, H_NUM),
       teach=["Think first: if the Food Court is one press of '+' from the ground floor, what number would you "
              "give it? What about the Toy Store, one press of '−' down?",
              "The Food Court is Floor +1 and the Toy Store is Floor −1. A number with a '+' sign is positive and "
              "a number with a '−' sign is negative.",
              "The ground floor is the reference point. No button is needed to be there, so it is Floor 0, and "
              "zero is neither positive nor negative."],
       examples=[we("10.1.q4"), we("10.1.q5")],
       key_terms=["positive number", "negative number", "Floor 0"],
       misconceptions=["M_BELOW_POSITIVE", "M_ZERO_SIGNED"], minutes=8),
     DOER("T2.C4", "Pull it together and do it: Floors as Numbers", None, "Understand",
          "Students say which floor numbers are positive, which are negative and which is neither, and match a "
          "button press to a floor.",
          ["Floors above the ground are positive and floors below are negative.",
           "The ground floor is Floor 0, and zero is neither positive nor negative.",
           "A press of '+' goes up and a press of '−' goes down; the number says how many floors."],
          misconceptions=["M_BELOW_POSITIVE", "M_ZERO_SIGNED"])]))

# ============================== T3 Adding button presses (10.1) ==============================================
TOPICS.append(TOPIC(
    "T3", "M1", "Adding Button Presses", [S], "Apply",
    "Students use Starting Floor + Movement = Target Floor to add integers, combine several presses into one "
    "movement, and cancel a press with its inverse.",
    "Adding an integer is moving in the lift: start at a floor, press a movement, and read off the target floor.",
    [A("T3.C1", "Starting floor plus movement", "Apply",
       "Students write a move in the lift as Starting Floor + Movement = Target Floor, and find the target floor.",
       textbook=book(S, H_ADD, stop=3),
       teach=["Think first: you stand in the Food Court on Floor +1 and press +2. Which floor do you reach?",
              "Write it as an expression: Starting Floor + Movement = Target Floor. Here (+1) + (+2) = +3, the "
              "Book Store.",
              "Adding is a movement: the start is a floor, the second number is the movement, and the answer is "
              "the target floor."],
       examples=[we("10.1.q6")],
       key_terms=["starting floor", "movement", "target floor"], misconceptions=["M_ADD_BIGGER"], minutes=8),
     A("T3.C2", "Combining button presses", "Apply",
       "Students combine a run of '+' and '−' presses into one movement and write it as an addition.",
       textbook=book(S, H_COMB, stop=2),
       teach=["Think first: Gurmit presses '+' twice by mistake, then '−' three times. Does he end up above or "
              "below where he began?",
              "The two movements are +2 and −3, and combining them is the addition (+2) + (−3) = −1.",
              "So combining button presses is also addition, and he ends one floor below the Toy Store."],
       examples=[we("10.1.ex1")],
       key_terms=["combining movements", "addition"], misconceptions=["M_ADD_BIGGER", "M_IGNORE_SIGN"], minutes=8),
     A("T3.C3", "Back to zero: the inverse", "Understand",
       "Students cancel a press with the press of equal size in the other direction, and name the inverse of an "
       "integer.",
       textbook=book(S, H_ZERO, stop=6),
       teach=["Think first: Basant is on the ground floor and presses +3 by mistake. Which press takes him back "
              "to the ground floor?",
              "Pressing −3 cancels it: (+3) + (−3) = 0. We call −3 the inverse of +3, and +3 the inverse of −3.",
              "A number plus its inverse is 0, and the inverse of 0 is 0 itself."],
       examples=[we("10.1.q7"), we("10.1.q8"), we("10.1.q9"), we("10.1.q10")],
       key_terms=["inverse"], misconceptions=["M_INVERSE_RECIP"], minutes=8),
     DOER("T3.C4", "Pull it together and do it: Ride the Lift", "lift_mover", "Apply",
          "Students press lift buttons from different floors, read the target floor and write the addition.",
          ["Starting Floor + Movement = Target Floor.",
           "Several presses combine into one movement, and a press plus its inverse brings you back.",
           "Read the target floor off the lift, not from the signs alone."],
          items=[fio("10.1.FiO1.Q1"), fio("10.1.FiO1.Q2"), fio("10.1.FiO1.Q3"), fio("10.1.FiO2.Q1")],
          misconceptions=["M_ADD_BIGGER", "M_IGNORE_SIGN"])]))

# ============================== T4 Comparing floors (10.1) ===================================================
TOPICS.append(TOPIC(
    "T4", "M1", "Comparing Floors", [S], "Apply",
    "Students compare integers by their floors, using the fact that a lower floor is a smaller number, and place "
    "integers on a vertical line.",
    "A higher floor is a greater number, so every negative number is less than 0 and less than every positive "
    "number, and −4 is less than −3.",
    [A("T4.C1", "Who is on the lowest floor?", "Understand",
       "Students give the floor number of each child and decide who is on the lowest floor.",
       textbook=book(S, H_CMP, stop=5),
       teach=["Think first: Jay is on Floor +2, Asin on Floor +5, Binnu on Floor −3 and Aman on Floor −1. Who do "
              "you think is lowest?",
              "Put each child on the lift: the lowest floor is the lowest in the building, and Binnu on Floor −3 "
              "is below Aman on Floor −1.",
              "A lower floor means a smaller number, so any negative floor is lower than the ground floor."],
       examples=[we("10.1.q11")],
       key_terms=["lowest floor", "smaller number"], misconceptions=["M_BIGGER_DIGIT"], minutes=8),
     A("T4.C2", "Writing < and > for negative numbers", "Apply",
       "Students write < or > between two integers by asking which floor is higher, including two negative floors.",
       textbook=book(S, H_CMP, start=5, stop=8),
       teach=["Think first: Floor +3 is lower than Floor +4, so +3 < +4. Which is right for the basement floors, "
              "−3 < −4 or −4 < −3?",
              "Floor −4 is lower than Floor −3, so −4 < −3. We can also write −3 > −4.",
              "For negative numbers the bigger digit is the lower floor. Every negative number is less than 0 "
              "and every positive number is greater than 0."],
       examples=[we("10.1.q12")],
       key_terms=["less than", "greater than"], misconceptions=["M_BIGGER_DIGIT"], minutes=8),
     DOER("T4.C3", "Pull it together and do it: Floor Line", "floor_line", "Apply",
          "Students compare integers with < and >, fill in the numbers on a vertical line of floors and mark floors on it.",
          ["A higher floor is a greater number and a lower floor is a smaller number.",
           "All negative numbers are less than 0, and all positive numbers are greater than 0.",
           "Of two negative numbers, the one nearer to 0 is the greater."],
          items=[fio("10.1.FiO3.Q1"), fio("10.1.FiO3.Q2"), fio("10.1.FiO3.Q3"), fio("10.1.FiO3.Q4")],
          misconceptions=["M_BIGGER_DIGIT"])]))

# ============================== T5 Subtraction finds the button (10.1) =======================================
TOPICS.append(TOPIC(
    "T5", "M2", "Subtraction Finds the Button", [S], "Apply",
    "Students read subtraction as finding the missing movement, Target Floor − Starting Floor = Movement needed, "
    "and use it between any two floors.",
    "Subtraction asks how much must be added to the start to reach the target, so the movement is the target "
    "minus the start.",
    [A("T5.C1", "Subtraction as the missing number to add", "Understand",
       "Students read a subtraction as finding what must be added to the smaller quantity to make it equal to the "
       "larger.",
       textbook=book(S, H_SUB, stop=8),
       teach=["Think first: you have ₹10 and your sister has ₹6. How much more must she get to have the same "
              "amount?",
              "We write it as 6 + ? = 10, or 10 − 6 = ?, so subtraction also finds the missing number to be "
              "added.",
              "For positive and negative numbers we use this meaning: subtraction shows the change needed to go "
              "from the start to the target."],
       examples=[we("10.1.q13")],
       key_terms=["subtraction", "missing number"], misconceptions=["M_SUB_SMALLER"], minutes=8),
     A("T5.C2", "Target Floor minus Starting Floor", "Apply",
       "Students find the button to press between two floors as Target Floor − Starting Floor = Movement needed.",
       textbook=book(S, H_SUB, start=8, stop=15),
       teach=["Think first: your starting floor is the Art Centre on Floor +2 and your target is the Sports "
              "Centre on Floor +5. Which button do you press?",
              "You need three floors up, so you press +3. As a subtraction: (+5) − (+2) = +3.",
              "Starting Floor + Movement = Target Floor, so Movement = Target Floor − Starting Floor. The target "
              "is written first."],
       examples=[we("10.1.q14")],
       key_terms=["target floor", "movement needed"], misconceptions=["M_START_MINUS_TARGET"], minutes=8),
     A("T5.C3", "Subtracting when floors are below the ground", "Apply",
       "Students find the movement between floors when the start or the target is negative, and write it as a "
       "subtraction.",
       textbook=book(S, H_SUB, start=15, stop=19),
       teach=["Think first: you start on Floor −2 and want Floor −1. Is the movement up or down?",
              "One floor up, so (−1) − (−2) = +1. From Floor +3 to Floor −1 you go four floors down, so (−1) − "
              "(+3) = −4. From Floor −2 to Floor +2 you go four floors up, so (+2) − (−2) = +4.",
              "Read the movement off the lift, then write the subtraction. Taking away a negative start sends "
              "you up."],
       examples=[we("10.1.ex2"), we("10.1.ex3"), we("10.1.ex4")],
       key_terms=["movement needed"], misconceptions=["M_SUB_NEG_SMALLER", "M_START_MINUS_TARGET"], minutes=10),
     DOER("T5.C4", "Pull it together and do it: Which Button?", None, "Apply",
          "Students complete subtractions by finding the button that takes the lift from the starting floor to the "
          "target floor.",
          ["Target Floor − Starting Floor = Movement needed.",
           "Picture the lift first, then write the number.",
           "Going up gives a positive movement and going down gives a negative movement."],
          items=[fio("10.1.FiO4.Q1")], misconceptions=["M_START_MINUS_TARGET", "M_SUB_NEG_SMALLER"])]))

# ============================== T6 Bigger numbers: the mine and the endless lift (10.1) ======================
TOPICS.append(TOPIC(
    "T6", "M2", "Bigger Numbers in a Mine and an Endless Lift", [S], "Apply",
    "Students use the same lift ideas for large integers in a mine and in an endless lift, and see that "
    "subtracting a negative number is the same as adding its positive.",
    "A mine and an endless lift show that the lift rules work for any size, and subtracting a negative number "
    "gives the same result as adding the matching positive number.",
    [A("T6.C1", "The mine: levels in metres", "Apply",
       "Students add and subtract levels in a mine, where metres above the ground are positive and metres below "
       "are negative.",
       textbook=book(S, H_MINE, stop=7),
       teach=["Think first: a mine lift is at +40 m and goes 60 m up. Where does it stop? What if it were at −90 m "
              "and went 55 m further down?",
              "It is the same rule as in Bela's building: Starting Level + Movement = Target Level, so "
              "(+40) + (+60) = +100 and (−90) + (−55) = −145.",
              "And Target Level − Starting Level = Movement needed, so (+40) − (−50) = +90 and (−90) − (+40) = "
              "−130."],
       examples=[we("10.1.ex5")],
       key_terms=["level", "metres below the ground"], misconceptions=["M_IGNORE_SIGN", "M_SUB_NEG_SMALLER"],
       minutes=8),
     A("T6.C2", "An endless lift", "Apply",
       "Students imagine a lift that runs without end above and below the ground and use it to find +2000 − "
       "(−200).",
       textbook=book(S, H_ANY, stop=5),
       teach=["Think first: how many floors must a lift cover to go from Level −200 to Level +2000?",
              "From −200 you press +200 to reach 0, and +2000 more to reach +2000, in all +2200. So (+2000) − "
              "(−200) = +2200.",
              "We can imagine a lift as large as we like, with no building needed, and then add and subtract any "
              "integers."],
       examples=[we("10.1.ex6")],
       key_terms=["endless lift", "integers"], misconceptions=["M_SUB_NEG_SMALLER"], minutes=8),
     A("T6.C3", "Subtracting a negative is adding a positive", "Understand",
       "Students notice that subtracting a negative number gives the same result as adding the matching positive "
       "number.",
       textbook=book(S, H_ANY, start=5, stop=8),
       teach=["Think first: (+2000) − (−200) came to +2200. What is (+2000) + (+200)?",
              "It is +2200 too. Try more: +105 − (−55) and +105 + (+55) both give +160.",
              "So subtracting a negative number is the same as adding the corresponding positive number."],
       examples=[we("10.1.q15"), we("10.1.q16")],
       key_terms=["subtracting a negative"], misconceptions=["M_SUB_NEG_SMALLER", "M_SUB_SMALLER"], minutes=10),
     DOER("T6.C4", "Pull it together and do it: Mine Levels", None, "Apply",
          "Students fill in missing movements and evaluate sums and differences by thinking of the mineshaft.",
          ["Starting Level + Movement = Target Level.",
           "Target Level − Starting Level = Movement needed.",
           "Check every answer by picturing the lift in the mineshaft."],
          items=[fio("10.1.FiO5.Q1")], misconceptions=["M_IGNORE_SIGN", "M_SUB_NEG_SMALLER"])]))
