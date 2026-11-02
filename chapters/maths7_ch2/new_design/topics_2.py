# -*- coding: utf-8 -*-
"""Topics T5 to T7 (module M2): swapping and grouping, expressions from stories, removing brackets after + and −."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T5 Swapping and grouping =====================================================
TOPICS.append(TOPIC(
    "T5", "M2", "Swapping and Grouping Terms", ["2.2"], "Analyze",
    "Students show that swapping two terms or grouping three or more terms in a different way does not change the "
    "value of a sum, name these the commutative and associative properties, and see that a sign must travel with "
    "its number when terms are moved.",
    "In a sum of terms the order and the grouping can change without changing the value, as long as each term keeps "
    "its own sign.",
    [A("T5.C1", "Swapping two terms", "Analyze",
       "Students check that swapping the two terms of a sum, including a negative term, leaves the value unchanged, "
       "and explain it with counters that are positive or negative.",
       textbook=["Madhu is flying a drone from a terrace. The drone goes 6 m up and then 4 m down. Write an "
                 "expression to show how high the final position of the drone is from the terrace.",
                 "6 − 4 = 2, and as a sum of terms 6 + (−4) = 2. Swapping the terms gives (−4) + 6 = 2. It does not "
                 "change the value. In an expression having two terms, swapping them does not change the value."],
       teach=["Predict first: a drone goes 6 m up and 4 m down. If the drone went 4 m down first and then 6 m up, "
              "would it end higher, lower or at the same height?",
              "Write both orders as a sum of terms: 6 + (−4) and (−4) + 6.",
              "Think of positive and negative counters: 6 positive and 4 negative cancel in pairs, in whatever order "
              "you place them, and 2 positive counters are left.",
              "So in a sum of two terms, swapping them does not change the value."],
       examples=[
           WE("A drone goes 6 m up and then 4 m down. Write the final height as a sum of terms, then swap the two "
              "terms and compare.",
              ["Up 6 and down 4 gives 6 + (−4) = 2, so it ends 2 m above the start.",
               "Swapping the terms gives (−4) + 6 = 2.", "The value is the same, 2 m, in both orders."],
              "6 + (−4) = 2 and (−4) + 6 = 2, so swapping two terms does not change the value",
              ncert=["2.2.swap", "2.2.ex6"], fact="ex6", expect=[2, 2]),
           WE("Check whether swapping changes the value of (−9) + 4, and say why using counters.",
              ["(−9) + 4: nine negative counters and four positive counters. Four pairs cancel and 5 negative "
               "counters are left, so the value is −5.",
               "(4) + (−9): the same counters in the other order. The value is again −5.",
               "Counters do not change when you move them, so the sum cannot change."],
              "(−9) + 4 = −5 and 4 + (−9) = −5", ncert=["2.2.swap_neg"], fact="swap_neg", expect=[-5, -5])],
       key_terms=["term", "swap"], misconceptions=["M_TERM_SIGN"], minutes=10),
     A("T5.C2", "Grouping three or more terms", "Analyze",
       "Students add three terms in two different groupings and in different orders and get one value, extend the "
       "idea to any number of terms, and use it to add a forgotten number to an existing total.",
       textbook=["Consider an expression having three terms: (−7) + 10 + (−11). Adding the first two terms and then "
                 "the third, or the last two terms and then the first, gives the same sum, −8.",
                 "Adding the terms of an expression in any order gives the same value.",
                 "Manasa is adding a long list of numbers. It took her five minutes to add them all and she got the "
                 "answer 11749. Then she realised that she had forgotten to include the fourth number 9055. Does "
                 "she have to start all over again?"],
       teach=["Predict first: (−7) + 10 + (−11). If you add the last two first, do you expect the same total?",
              "Group the first two terms, or group the last two: the value does not change. Order does not matter "
              "either.",
              "With 4 or more terms the same is true: add in any order, in any groups.",
              "So a forgotten term can simply be added to the total you already have."],
       examples=[
           WE("Add (−7) + 10 + (−11) in three different ways and compare.",
              ["First two terms first: (−7) + 10 = 3, then 3 + (−11) = −8.",
               "Last two terms first: 10 + (−11) = −1, then (−7) + (−1) = −8.",
               "The two negative terms first: (−7) + (−11) = −18, then −18 + 10 = −8.",
               "All three orders give −8."],
              "(−7) + 10 + (−11) = −8 in any order or grouping", ncert=["2.2.three_terms"], fact="three_terms",
              expect=[-8]),
           WE("Meera added the numbers 1342, 774, 8611, 9055 and 1022 but forgot 9055 the first time and got 11749. "
              "What is the correct total, without starting again?",
              ["She had added 1342 + 774 + 8611 + 1022 = 11749.",
               "The order of adding does not matter, so the forgotten term can be added last.",
               "11749 + 9055 = 20804."],
              "The correct total is 20804", ncert=["2.2.any_terms", "2.2.manasa"], fact="manasa", expect=[11749, 20804])],
       key_terms=["term", "group"], misconceptions=["M_SWAP_ANYTHING"], minutes=10),
     A("T5.C3", "Naming the two properties, and when order matters", "Analyze",
       "Students name swapping and grouping as the commutative and associative properties of addition, evaluate "
       "an expression by working out each term first, and see that moving a term means moving its sign with it.",
       textbook=["In mathematics we use the phrase commutative property of addition instead of saying swapping terms "
                 "does not change the sum. Similarly, grouping does not change the sum is called the associative "
                 "property of addition.",
                 "The expression 5 × (3 + 2) + 7 × 8 + 3 is evaluated by terms: 25 + 56 + 3 = 84.",
                 "Wear your hat and shoes: either order gives the same look. Wear your socks and shoes: the order "
                 "matters."],
       teach=["Predict first: is putting on socks and then shoes the same as shoes and then socks? Is adding two "
              "numbers in either order the same?",
              "Adding in any order is called the commutative property, and adding in any grouping is called the "
              "associative property.",
              "Evaluate by terms: find the value of each term, then add them in any order you like.",
              "Not everything can be swapped. Moving a term means moving its sign with it: 12 − 5 has the terms 12 "
              "and −5, so it equals −5 + 12 but not 5 − 12."],
       examples=[
           WE("Evaluate 5 × (3 + 2) + 7 × 8 + 3 by terms, and name the property that lets you add the term values "
              "in any order.",
              ["The terms are 5 × (3 + 2), 7 × 8 and 3.", "5 × (3 + 2) = 5 × 5 = 25 and 7 × 8 = 56.",
               "25 + 56 + 3 = 84.",
               "Adding 25, 56 and 3 in any order gives 84, because addition is commutative and associative."],
              "84", ncert=["2.2.properties"], fact="eval_terms", expect=[25, 56, 84]),
           WE("Is 12 − 5 equal to 5 − 12? Write 12 − 5 as terms, swap them, and decide.",
              ["12 − 5 = 12 + (−5). The terms are 12 and −5, and the value is 7.",
               "Swapping the terms with their signs gives (−5) + 12 = 7, which is the same.",
               "But 5 − 12 = 5 + (−12) = −7, which is a different value, because the −5 term lost its sign.",
               "Like putting on socks and shoes, order matters when you do not move the whole term."],
              "12 − 5 = (−5) + 12 = 7, but 5 − 12 = −7", ncert=["2.2.swap_life"], fact="swap_sign",
              expect=[7, 7, -7])],
       key_terms=["commutative property", "associative property"], misconceptions=["M_SWAP_ANYTHING", "M_TERM_SIGN"],
       minutes=10),
     DOER("T5.C4", "Practice: reorder the terms to add quickly", "hop_reorder_line", "Apply",
          "Students reorder and regroup the terms of a sum, keeping each sign with its number, to make a "
          "sum quick to add, and check that the value stays the same.",
          ["Keep each sign with its number when you move a term.",
           "Group terms that cancel or make a round number first.",
           "Any order and any grouping of a sum gives the same value."])]))

# ============================== T6 More expressions and their terms ==========================================
TOPICS.append(TOPIC(
    "T6", "M2", "More Expressions and Their Terms", ["2.2"], "Apply",
    "Students write an expression for a story with equal groups and extras, with a division, and with a collection "
    "of notes, name its terms and find its value, and match an expression to a picture of squares.",
    "Stories with equal groups plus a few extra become expressions made of a times term and an extra term.",
    [A("T6.C1", "Equal groups plus extras", "Apply",
       "Students write an expression such as 4 × 23 + 5 for equal groups with an extra, change the numbers to match "
       "a new story, and name each term.",
       textbook=["Amu, Charan, Madhu, and John went to a hotel and ordered four dosas. Each dosa cost ₹23, and they "
                 "wish to thank the waiter by tipping ₹5. Write an expression describing the total cost.",
                 "If the total number of friends goes up to 7 and the tip remains the same, how much will they have "
                 "to pay?",
                 "Ruby wrote 6 × 5 + 3 when the teacher called out 5 and 33 students were playing."],
       teach=["Predict first: 4 dosas at ₹23 each, and a ₹5 tip. Is the bill 4 × 23 + 5 or 4 × (23 + 5)?",
              "The cost of 4 dosas is 4 × 23. The tip is a separate extra, so it is added: 4 × 23 + 5.",
              "Written as a sum of terms, 4 × 23 + 5 has two terms, 4 × 23 and 5.",
              "Groups plus left over: 33 students in groups of 5 make 6 full groups with 3 left, 6 × 5 + 3."],
       examples=[
           WE("Four friends order 4 dosas at ₹23 each and tip ₹5. Write the total as an expression, list its terms "
              "and find the value. Then do it again for 7 friends.",
              ["The cost of 4 dosas is 4 × 23. The tip is 5, so the total is 4 × 23 + 5.",
               "The terms are 4 × 23 and 5. Value: 4 × 23 = 92, then 92 + 5 = 97.",
               "For 7 friends: 7 × 23 + 5 with the terms 7 × 23 and 5.", "7 × 23 = 161, and 161 + 5 = 166."],
              "4 × 23 + 5 = ₹97 and 7 × 23 + 5 = ₹166", ncert=["2.2.ex7"], fact="ex7", expect=[97, 166]),
           WE("Tanvi sat out of a game and the other 33 students made equal groups. When the teacher called 5, "
              "Tanvi wrote 6 × 5 + 3. Write the matching expressions when the teacher calls 4 and 7, and list the "
              "terms of each.",
              ["Called 5: 33 = 6 groups of 5 with 3 left, so 6 × 5 + 3. The terms are 6 × 5 and 3.",
               "Called 4: 33 = 8 groups of 4 with 1 left, so 8 × 4 + 1. The terms are 8 × 4 and 1.",
               "Called 7: 33 = 4 groups of 7 with 5 left, so 4 × 7 + 5. The terms are 4 × 7 and 5.",
               "Each expression has the value 33: 30 + 3, 32 + 1 and 28 + 5."],
              "6 × 5 + 3, 8 × 4 + 1 and 4 × 7 + 5, each with value 33", ncert=["2.2.ex8"], fact="ex8",
              expect=[33, 33, 33])],
       key_terms=["term", "expression"], misconceptions=["M_TERM_PRODUCT"], minutes=10),
     A("T6.C2", "Packets and notes: a division and many ways to pay", "Apply",
       "Students write an expression with a division term for packets, and write a sum with several times terms to "
       "pay an amount in different ways.",
       textbook=["Raghu bought 100 kg of rice from the wholesale market and packed them into 2 kg packets. He already "
                 "had four 2 kg packets. Write an expression for the number of 2 kg packets he has now. It is "
                 "4 + 100 ÷ 2.",
                 "Kannan has to pay ₹432 using coins of ₹1 and ₹5, and notes of ₹10, ₹20, ₹50 and ₹100. There is "
                 "more than one possibility: 432 = 4 × 100 + 1 × 20 + 1 × 10 + 2 × 1 and "
                 "432 = 8 × 50 + 1 × 10 + 4 × 5 + 2 × 1."],
       teach=["Predict first: 100 kg packed into 2 kg packets, plus 4 packets already. How many packets in all?",
              "The new packets are 100 ÷ 2, a term by itself. The packets he already had are another term, 4.",
              "For money, each term is a number of notes times the value of the note.",
              "Different note choices give different expressions with the same value, 432."],
       examples=[
           WE("Meera packs 100 kg of rice into 2 kg packets and already has 4 packets. Write an expression for the "
              "packets she has now, list its terms and find the value.",
              ["The new packets are 100 ÷ 2. She already had 4.", "So the number of packets is 4 + 100 ÷ 2.",
               "The terms are 4 and 100 ÷ 2.", "100 ÷ 2 = 50, and 4 + 50 = 54."],
              "4 + 100 ÷ 2 = 54 packets, with terms 4 and 100 ÷ 2", ncert=["2.2.ex9"], fact="ex9", expect=[54]),
           WE("Joseph must pay ₹432 using notes and coins. Check 4 × 100 + 1 × 20 + 1 × 10 + 2 × 1 and "
              "8 × 50 + 1 × 10 + 4 × 5 + 2 × 1, name the terms of each, and find one more way.",
              ["First way: 4 × 100 = 400, 1 × 20 = 20, 1 × 10 = 10, 2 × 1 = 2. The terms are 4 × 100, 1 × 20, "
               "1 × 10 and 2 × 1. The total is 400 + 20 + 10 + 2 = 432.",
               "Second way: 8 × 50 = 400, 1 × 10 = 10, 4 × 5 = 20, 2 × 1 = 2. The terms are 8 × 50, 1 × 10, 4 × 5 and "
               "2 × 1. The total is 400 + 10 + 20 + 2 = 432.",
               "One more way: 4 × 100 + 3 × 10 + 2 × 1 = 400 + 30 + 2 = 432."],
              "Both ways give ₹432, and 4 × 100 + 3 × 10 + 2 × 1 is another way", ncert=["2.2.ex10"], fact="ex10",
              expect=[432, 432, 432])],
       key_terms=["term"], misconceptions=["M_TERM_PRODUCT"], minutes=10),
     A("T6.C3", "Matching an expression to squares", "Apply",
       "Students match 5 × 2 + 3 to a picture of squares, write an expression for another arrangement with a "
       "bracket, and see that one arrangement can have several expressions.",
       textbook=["Here are two pictures. Which of these two arrangements matches with the expression 5 × 2 + 3? "
                 "This expression can be understood as 3 more than 5 × 2, which describes the arrangement on the left. "
                 "What is the expression for the arrangement on the right making use of the number of yellow and "
                 "blue squares? 2 × (5 + 3), or 5 + 3 + 5 + 3, or 5 × 2 + 3 × 2."],
       teach=["Predict first: 5 × 2 + 3 means 5 groups of 2 squares and 3 more. Is it 13 squares or 16?",
              "On the left, 5 rows of 2 squares and 3 extra squares make 5 × 2 + 3 = 13.",
              "On the right, there are 2 rows, each with 5 yellow and 3 blue squares, so 2 × (5 + 3) = 16.",
              "The same 16 squares can be counted as 5 + 3 + 5 + 3 or 5 × 2 + 3 × 2."],
       examples=[
           WE("One arrangement has 5 rows of 2 squares and 3 extra squares. Another has 2 rows, each with 5 yellow "
              "and 3 blue squares. Write an expression for each and find the number of squares.",
              ["First arrangement: 5 × 2 + 3 = 10 + 3 = 13.",
               "Second arrangement: each row has 5 + 3 squares and there are 2 rows, so 2 × (5 + 3) = 2 × 8 = 16.",
               "The second can also be counted as 5 + 3 + 5 + 3 = 16 or 5 × 2 + 3 × 2 = 10 + 6 = 16."],
              "5 × 2 + 3 = 13 and 2 × (5 + 3) = 16, which also equals 5 + 3 + 5 + 3 and 5 × 2 + 3 × 2",
              ncert=["2.2.ex11"], fact="ex11", expect=[13, 16])],
       key_terms=["bracket", "term"], misconceptions=["M_BRACKET_IGNORED"], minutes=8),
     DOER("T6.C4", "Practice: write the story as an expression", "story_expression", "Apply",
          "Students write an expression for a story, list its terms and find its value, and also make up a story "
          "that fits a given expression.",
          ["Equal groups are a times term; extras are separate terms.",
           "Take away means a negative term.",
           "A story for an expression names what each term counts."],
          items=[
              FIO("2.2.FiO1", "Figure it Out, Q1",
                  "Find the values of the following expressions by writing the terms in each case. "
                  "(a) 28 − 7 + 8 (b) 39 − 2 × 6 + 11 (c) 40 − 10 + 10 + 10 (d) 48 − 10 × 2 + 16 ÷ 2 "
                  "(e) 6 × 3 − 4 × 8 × 5",
                  ["(a) Terms: 28, −7, 8. Value: 28 − 7 + 8 = 29.",
                   "(b) Terms: 39, −2 × 6, 11. Value: 39 − 12 + 11 = 38.",
                   "(c) Terms: 40, −10, 10, 10. Value: 40 − 10 + 10 + 10 = 50.",
                   "(d) Terms: 48, −10 × 2, 16 ÷ 2. Value: 48 − 20 + 8 = 36.",
                   "(e) Terms: 6 × 3, −4 × 8 × 5. Value: 18 − 160 = −142."],
                  "(a) 29 (b) 38 (c) 50 (d) 36 (e) −142", expect=[29, 38, 50, 36, -142]),
              FIO("2.2.FiO2", "Figure it Out, Q2",
                  "Write a story or situation for each of the following expressions and find their values. "
                  "(a) 89 + 21 − 10 (b) 5 × 12 − 6 (c) 4 × 9 + 2 × 6",
                  ["Any sensible story that matches each term works, for example:",
                   "(a) A shop has 89 pencils, 21 more arrive and 10 are sold: 89 + 21 − 10 = 100 pencils.",
                   "(b) Five packets hold 12 biscuits each and 6 biscuits are eaten: 5 × 12 − 6 = 54 biscuits.",
                   "(c) Four boxes hold 9 mangoes each and 2 bags hold 6 each: 4 × 9 + 2 × 6 = 36 + 12 = 48 mangoes."],
                  "Stories vary; the values are (a) 100 (b) 54 (c) 48", expect=[100, 54, 48]),
              FIO("2.2.FiO3", "Figure it Out, Q3",
                  "For each situation, write the expression, identify its terms and find its value. "
                  "(a) A queen gave 100 gold coins to each of two princesses last year. One princess used the coins "
                  "to start a business and doubled her coins. The other bought jewellery and has only half of her "
                  "coins left. Write an expression for how many coins the two princesses have together. "
                  "(b) A metro train ticket between two stations is ₹40 for an adult and ₹20 for a child. What is "
                  "the total cost of tickets (i) for four adults and three children, (ii) for two groups having three "
                  "adults each? (c) A window has a border of 3 cm at the top and at the bottom, six grills of 2 cm "
                  "each, and seven gaps of 5 cm each between and beside them. Find the total height of the window by "
                  "writing an expression.",
                  ["(a) One princess has 2 × 100 coins and the other has 100 ÷ 2. Expression: 2 × 100 + 100 ÷ 2. "
                   "Terms: 2 × 100 and 100 ÷ 2. Value: 200 + 50 = 250 coins.",
                   "(b)(i) 4 × 40 + 3 × 20 with terms 4 × 40 and 3 × 20. Value: 160 + 60 = ₹220.",
                   "(b)(ii) Two groups of three adults: 2 × (3 × 40), which is a single term. Value: 2 × 120 = ₹240.",
                   "(c) Two borders, six grills and seven gaps give the height 7 × 5 + 6 × 2 + 2 × 3. "
                   "Terms: 7 × 5, 6 × 2 and 2 × 3. Value: 35 + 12 + 6 = 53 cm."],
                  "(a) 2 × 100 + 100 ÷ 2 = 250 (b) (i) 4 × 40 + 3 × 20 = ₹220 (ii) 2 × (3 × 40) = ₹240 "
                  "(c) 7 × 5 + 6 × 2 + 2 × 3 = 53 cm", expect=[250, 220, 240, 53])],
          ncert=["2.2.FiO1", "2.2.FiO2", "2.2.FiO3"], misconceptions=["M_TERM_PRODUCT"])]))

# ============================== T7 Removing brackets I =======================================================
TOPICS.append(TOPIC(
    "T7", "M3", "Removing Brackets: After Minus and Plus", ["2.3"], "Analyze",
    "Students remove a bracket after a plus sign and after a minus sign, explain from the meaning why the terms "
    "inside change their signs after a minus, and predict the value of a sum by how much one number changed.",
    "A bracket after a plus sign can be dropped, a bracket after a minus sign flips every sign inside it, and the "
    "reason comes from what the bracket means.",
    [A("T7.C1", "A minus before a bracket", "Analyze",
       "Students remove a bracket that follows a minus sign by taking the terms away one at a time, and explain why "
       "200 − (40 + 3) is 200 − 40 − 3 and not 200 − 40 + 3.",
       textbook=["Removing Brackets I",
                 "Let us find the value of 200 − (40 + 3). We first evaluate the expression inside the bracket to 43 "
                 "and then subtract it from 200. But it is simpler to first subtract 40 from 200: 200 − 40 = 160. "
                 "And then subtract 3 from 160: 160 − 3 = 157.",
                 "What we did here was 200 − 40 − 3. Notice that we did not do 200 − 40 + 3. So 200 − (40 + 3) = "
                 "200 − 40 − 3.",
                 "Irfan paid ₹100 for ₹15 and ₹56: 100 − (15 + 56) = 100 − 15 − 56 = 29.",
                 "Notice how upon removing the brackets preceded by a negative sign, the signs of the terms inside "
                 "the brackets change."],
       teach=["Predict first: 200 − (40 + 3). Taking away 43 is the same as taking away 40 and then taking away 3. "
              "Does the 3 get added or taken away?",
              "Take away 40, and then take away 3 as well, so both numbers keep being taken away: 200 − 40 − 3.",
              "So the plus inside the bracket becomes a minus when the bracket is removed.",
              "Think about what the bracket means, rather than memorising a rule."],
       examples=[
           WE("Find 100 − (15 + 56) by taking the two prices away one at a time. Compare with working out the "
              "bracket first.",
              ["Take away the first price: 100 − 15 = 85.", "Take away the second price: 85 − 56 = 29.",
               "So 100 − (15 + 56) = 100 − 15 − 56 = 29.",
               "Working out the bracket first: 15 + 56 = 71 and 100 − 71 = 29, the same."],
              "100 − (15 + 56) = 100 − 15 − 56 = 29", ncert=["2.3.minus_bracket", "2.3.ex12"], fact="ex12",
              expect=[85, 29]),
           WE("Consider 500 − (250 − 100). Can we write it as 500 − 250 − 100? Find the right way to remove the "
              "bracket.",
              ["Working out the bracket first: 250 − 100 = 150, and 500 − 150 = 350.",
               "But 500 − 250 − 100 = 150, which is different.",
               "We take away 250 but 100 of it should be given back, since only 250 − 100 = 150 is taken away "
               "in all.",
               "So 500 − (250 − 100) = 500 − 250 + 100 = 350."],
              "500 − (250 − 100) = 500 − 250 + 100 = 350, not 500 − 250 − 100", ncert=["2.3.ex13"], fact="ex13",
              expect=[350, 150])],
       key_terms=["bracket", "term"], misconceptions=["M_MINUS_BRACKET"], minutes=10),
     A("T7.C2", "A plus before a bracket, and reasoning not rules", "Analyze",
       "Students remove a bracket that follows a plus sign, keep the signs inside unchanged, and say why in "
       "words about adding the parts one by one.",
       textbook=["Hira has a rare coin collection. She has 28 coins in one bag and 35 − 10 coins in another. "
                 "28 + (35 − 10) = 28 + 35 − 10 = 53.",
                 "Whenever you remove brackets, reason about what the expression means. Do not just memorise rules."],
       teach=["Predict first: 28 coins, plus a bag of 35 − 10. Do the signs inside the bracket change when it "
              "follows a plus sign?",
              "Adding 25 is the same as adding 35 and then taking away 10: nothing is reversed.",
              "So after a plus sign the bracket is simply dropped, and every sign inside stays as it was.",
              "Always check by working both forms out."],
       examples=[
           WE("Meera has 28 coins in one bag and puts in a bag holding 35 − 10 coins. Write the total as an "
              "expression, remove the bracket and find the value.",
              ["The total is 28 + (35 − 10).", "Bracket first: 35 − 10 = 25, and 28 + 25 = 53.",
               "Adding 35 and then taking away 10: 28 + 35 − 10 = 63 − 10 = 53.",
               "So 28 + (35 − 10) = 28 + 35 − 10, and the signs inside did not change."],
              "28 + (35 − 10) = 28 + 35 − 10 = 53", ncert=["2.3.ex14", "2.3.reason"], fact="ex14", expect=[25, 53])],
       key_terms=["bracket"], misconceptions=["M_MINUS_BRACKET", "M_BRACKET_IGNORED"], minutes=8),
     A("T7.C3", "One more, one less: predicting a sum", "Analyze",
       "Students practise predicting the value of a sum with a negative number by comparing it with a sum already worked out, "
       "asking whether one number is one more or one less, and use it for negative numbers.",
       textbook=["Tinker the Terms I: 53 + (−16) = 37. What is 54 + (−16)? 54 is one more than 53, so the value will "
                 "be 1 more than 37. What is 52 + (−16)? 53 + (−15)? 53 + (−17)? Is −17 one more or one less "
                 "than −16?",
                 "And −87 + (−16) = −103. Then −88 + (−15), −86 + (−18) and −97 + (−26)."],
       teach=["Predict first: 53 + (−16) = 37. What is 54 + (−16), without adding afresh?",
              "If one number goes up by 1 and the other stays the same, the sum goes up by 1. If one goes down by 1, "
              "the sum goes down by 1.",
              "A number that goes from −16 to −15 goes up by 1, and from −16 to −17 goes down by 1.",
              "If one number goes up and the other goes down by the same amount, the sum is unchanged."],
       examples=[
           WE("Given 53 + (−16) = 37, find 54 + (−16), 52 + (−16), 53 + (−15) and 53 + (−17) without adding afresh.",
              ["54 is one more than 53, so the sum is 1 more: 54 + (−16) = 38.",
               "52 is one less than 53, so the sum is 1 less: 52 + (−16) = 36.",
               "−15 is one more than −16, so 53 + (−15) = 38.",
               "−17 is one less than −16, so 53 + (−17) = 36."],
              "38, 36, 38 and 36", ncert=["2.3.tinker1"], fact="tinker1a", expect=[38, 36, 38, 36]),
           WE("Given −87 + (−16) = −103, find −88 + (−15), −86 + (−18) and −97 + (−26) by reasoning.",
              ["−88 is one less and −15 is one more, so the changes cancel: −88 + (−15) = −103.",
               "−86 is one more and −18 is two less, so the sum is one less: −86 + (−18) = −104.",
               "−97 is 10 less and −26 is 10 less, so the sum is 20 less than −103: −97 + (−26) = −123."],
              "−103, −104 and −123", ncert=["2.3.tinker1"], fact="tinker1b", expect=[-103, -104, -123])],
       key_terms=["term"], misconceptions=["M_TERM_SIGN"], minutes=10),
     DOER("T7.C4", "Practice: remove the brackets and check the value", "bracket_sign", "Apply",
          "Students remove brackets after plus and minus signs, check each by working out both forms, add brackets to "
          "reach a target value, and match expressions with the same terms.",
          ["After a plus sign, drop the bracket and keep the signs.",
           "After a minus sign, drop the bracket and flip every sign inside.",
           "Check by working both forms out."],
          items=[
              FIO("2.3.FiO1", "Figure it Out, Q1",
                  "Fill in the blanks with numbers, and boxes with operation signs such that the expressions on both "
                  "sides are equal. (a) 24 + (6 − 4) = 24 + 6 [ ] ____ (b) 38 + (____ [ ] ____) = 38 + 9 − 4 "
                  "(c) 24 − (6 + 4) = 24 [ ] 6 − 4 (d) 24 − 6 − 4 = 24 − 6 [ ] ____ "
                  "(e) 27 − (8 + 3) = 27 [ ] 8 [ ] 3 (f) 27 − (____ [ ] ____) = 27 − 8 + 3",
                  ["(a) A plus before the bracket keeps the signs: 24 + 6 − 4. The box is − and the blank is 4.",
                   "(b) The bracket is (9 − 4): the blanks are 9 and 4, and the box is −.",
                   "(c) A minus before the bracket flips the plus: 24 − 6 − 4. The box is −.",
                   "(d) Taking away 6 and then 4: the box is − and the blank is 4.",
                   "(e) 27 − 8 − 3: both boxes are −.",
                   "(f) 27 − 8 + 3 means taking away (8 − 3), so the blanks are 8 and 3 and the box is −."],
                  "(a) −, 4 (b) 9, −, 4 (c) − (d) −, 4 (e) −, − (f) 8, −, 3", expect=[4, 9, 4, 4, 8, 3]),
              FIO("2.3.FiO2", "Figure it Out, Q2",
                  "Remove the brackets and write the expression having the same value. (a) 14 + (12 + 10) "
                  "(b) 14 − (12 + 10) (c) 14 + (12 − 10) (d) 14 − (12 − 10) (e) −14 + (12 − 10) "
                  "(f) 14 − (−12 − 10)",
                  ["(a) 14 + 12 + 10 = 36.", "(b) 14 − 12 − 10 = −8.", "(c) 14 + 12 − 10 = 16.",
                   "(d) 14 − 12 + 10 = 12.", "(e) −14 + 12 − 10 = −12.",
                   "(f) The minus flips both signs inside: 14 + 12 + 10 = 36."],
                  "(a) 14 + 12 + 10 (b) 14 − 12 − 10 (c) 14 + 12 − 10 (d) 14 − 12 + 10 (e) −14 + 12 − 10 "
                  "(f) 14 + 12 + 10", expect=[36, -8, 16, 12, -12, 36]),
              FIO("2.3.FiO3", "Figure it Out, Q3",
                  "Find the values of the following expressions. For each pair, first try to guess whether they have "
                  "the same value. When are the two expressions equal? (a) (6 + 10) − 2 and 6 + (10 − 2) "
                  "(b) 16 − (8 − 3) and (16 − 8) − 3 (c) 27 − (18 + 4) and 27 + (−18 − 4)",
                  ["(a) (6 + 10) − 2 = 14 and 6 + (10 − 2) = 14. Equal.",
                   "(b) 16 − (8 − 3) = 16 − 5 = 11 but (16 − 8) − 3 = 8 − 3 = 5. Not equal.",
                   "(c) 27 − (18 + 4) = 27 − 22 = 5 and 27 + (−18 − 4) = 27 − 22 = 5. Equal.",
                   "The pairs are equal when the brackets change only the grouping of added terms, or when the signs "
                   "inside were flipped properly. In (b) the bracket after the minus was moved without flipping."],
                  "(a) 14 and 14, equal (b) 11 and 5, not equal (c) 5 and 5, equal", expect=[14, 14, 11, 5, 5, 5]),
              FIO("2.3.FiO4", "Figure it Out, Q4",
                  "In each of the sets of expressions below, identify those that have the same value. Do not evaluate "
                  "them, but rather use your understanding of terms. (a) 319 + 537, 319 − 537, −537 + 319, 537 − 319 "
                  "(b) 87 + 46 − 109, 87 + 46 − 109, 87 + 46 − 109, 87 − 46 + 109, 87 − (46 + 109), (87 − 46) + 109",
                  ["(a) 319 − 537 has the terms 319 and −537, and −537 + 319 has the same terms, so they are equal. "
                   "319 + 537 has 537 with a plus, and 537 − 319 has the terms 537 and −319, so each of those is "
                   "different from the rest.",
                   "(b) The first three expressions are the same written three times, so they are equal. "
                   "87 − 46 + 109 and (87 − 46) + 109 have the same terms 87, −46 and 109, so they are equal.",
                   "87 − (46 + 109) = 87 − 46 − 109 has a different term, −109, so it matches none of the others."],
                  "(a) 319 − 537 and −537 + 319 are equal (b) the first three are equal, and 87 − 46 + 109 equals "
                  "(87 − 46) + 109", expect=[319, 537, 87, 46, 109]),
              FIO("2.3.FiO5", "Figure it Out, Q5",
                  "Add brackets at appropriate places in the expressions such that they lead to the values indicated. "
                  "(a) 34 − 9 + 12 = 13 (b) 56 − 14 − 8 = 34 (c) −22 − 12 + 10 + 22 = −22",
                  ["(a) We need 13. Taking away both 9 and 12 gives 34 − 21 = 13, so 34 − (9 + 12) = 13.",
                   "(b) 56 − 14 − 8 already equals 34, so any bracket that keeps the value works, such as "
                   "(56 − 14) − 8 = 34 or 56 − (14 + 8) = 34.",
                   "(c) Written as printed, −22 − 12 + 10 + 22 = −2, so the bracket must change the value to −22: "
                   "−22 − (12 + 10) + 22 = −22 − 22 + 22 = −22."],
                  "(a) 34 − (9 + 12) = 13 (b) (56 − 14) − 8 = 34 (c) −22 − (12 + 10) + 22 = −22",
                  expect=[13, 34, -22]),
              FIO("2.3.FiO6", "Figure it Out, Q6",
                  "Using only reasoning of how terms change their values, fill the blanks to make the expressions on "
                  "either side of the equality equal. (a) 423 + ____ = 419 + ____ (b) 207 − 68 = 210 − ____",
                  ["(a) The left number is 4 more than 419, so the right side must add 4 more than the left blank: "
                   "423 + 419 = 419 + 423. Any pair with the same two terms works.",
                   "(b) 210 is 3 more than 207, so the number taken away must be 3 more than 68, which is 71. "
                   "Check: 207 − 68 = 139 and 210 − 71 = 139."],
                  "(a) 423 + 419 = 419 + 423 (b) 71", expect=[419, 71]),
              FIO("2.3.FiO7", "Figure it Out, Q7",
                  "Using the numbers 2, 3 and 5, and the operators + and −, and brackets, as necessary, generate "
                  "expressions to give as many different values as possible. For example, 2 − 3 + 5 = 4 and "
                  "3 − (5 − 2) = 0.",
                  ["Use each number once with + or − before it and optional brackets.",
                   "Without brackets: 2 + 3 + 5 = 10, 2 + 3 − 5 = 0, 2 − 3 + 5 = 4, 2 − 3 − 5 = −6.",
                   "With brackets: 2 − (3 + 5) = −6, 2 − (3 − 5) = 4, 3 − (5 − 2) = 0, 5 − (3 − 2) = 4, "
                   "5 − (2 + 3) = 0, 5 − 3 − 2 = 0, 3 − 2 − 5 = −4, 3 − 5 + 2 = 0, 5 − 2 + 3 = 6, 5 + 2 − 3 = 4, "
                   "3 + 5 − 2 = 6, 3 − 5 − 2 = −4.",
                   "The values found are 10, 6, 4, 0, −4 and −6, and 10 is the largest, using all plus signs."],
                  "Many answers; the possible values are 10, 6, 4, 0, −4 and −6", expect=[10, 6, 4, 0, -4, -6]),
              FIO("2.3.FiO8", "Figure it Out, Q8",
                  "Whenever Meera has to subtract 9 from a number, she subtracts 10 and adds 1 to it. For example, "
                  "36 − 9 = 26 + 1. (a) Do you think she always gets the correct answer? Why? (b) Can you think of "
                  "similar strategies? Give some examples.",
                  ["(a) Taking away 10 takes away 1 too many, so adding 1 back puts it right: −9 = −10 + 1. "
                   "36 − 10 + 1 = 27, and 36 − 9 = 27. Yes, it always works.",
                   "(b) Subtract 8 by subtracting 10 and adding 2: 36 − 8 = 36 − 10 + 2 = 28.",
                   "Add 9 by adding 10 and taking away 1: 36 + 9 = 36 + 10 − 1 = 45."],
                  "(a) Yes, always, since −9 = −10 + 1 (b) for example −8 = −10 + 2 and +9 = +10 − 1",
                  expect=[27, 28, 45]),
              FIO("2.3.FiO9", "Figure it Out, Q9",
                  "Consider the two expressions: a) 73 − 14 + 1, b) 73 − 14 − 1. For each of these expressions, "
                  "identify the expressions from the following collection that are equal to it. "
                  "(a) 73 − (14 + 1) (b) 73 − (14 − 1) (c) 73 + (−14 + 1) (d) 73 + (−14 − 1)",
                  ["73 − 14 + 1 = 60. Removing brackets: 73 − (14 − 1) = 73 − 14 + 1 = 60, and "
                   "73 + (−14 + 1) = 73 − 14 + 1 = 60.",
                   "73 − 14 − 1 = 58. Removing brackets: 73 − (14 + 1) = 73 − 14 − 1 = 58, and "
                   "73 + (−14 − 1) = 73 − 14 − 1 = 58.",
                   "So 73 − 14 + 1 equals (b) and (c), and 73 − 14 − 1 equals (a) and (d)."],
                  "73 − 14 + 1 equals (b) and (c); 73 − 14 − 1 equals (a) and (d)", expect=[60, 58])],
          ncert=["2.3.FiO1", "2.3.FiO2", "2.3.FiO3", "2.3.FiO4", "2.3.FiO5", "2.3.FiO6", "2.3.FiO7", "2.3.FiO8",
                 "2.3.FiO9"], misconceptions=["M_MINUS_BRACKET"])]))
