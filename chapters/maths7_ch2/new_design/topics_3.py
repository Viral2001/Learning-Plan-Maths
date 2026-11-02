# -*- coding: utf-8 -*-
"""Topics T8 to T11 (modules M3 and M4): multiplying a sum, problems with expressions, the puzzle and the summary."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T8 Removing brackets II ======================================================
TOPICS.append(TOPIC(
    "T8", "M3", "Removing Brackets: Multiplying a Sum", ["2.4"], "Apply",
    "Students show that a number multiplying a bracket multiplies every term inside it, state the distributive "
    "property for sums and differences, and use it to find products such as 97 × 25 quickly.",
    "A number outside a bracket multiplies every term inside, and this makes some products quick to find.",
    [A("T8.C1", "Two friends, one bracket", "Apply",
       "Students write the total for two or three friends with the same order as a number times a bracket, remove the "
       "bracket by multiplying each term, and explain why 2 × 43 + 24 is a different amount.",
       textbook=["Removing Brackets II",
                 "Lhamo and Norbu went to a hotel. Each of them ordered a vegetable cutlet and a rasgulla. A vegetable "
                 "cutlet costs ₹43 and a rasgulla costs ₹24. Write an expression for the amount they will have to pay.",
                 "As each of them had one vegetable cutlet and one rasagulla, each of their shares can be represented "
                 "by 43 + 24. What about the total amount they have to pay? Can it be described by the expression "
                 "2 × 43 + 24?",
                 "Writing it as a sum of terms, 2 × 43 + 24 means 24 more than 2 × 43. But we want an expression which "
                 "means twice or double of 43 + 24. We can make use of brackets to write such an expression: "
                 "2 × (43 + 24).",
                 "This is also the same as paying for two vegetable cutlets and two rasgullas: 2 × 43 + 2 × 24. "
                 "Therefore, 2 × (43 + 24) = 2 × 43 + 2 × 24.",
                 "If another friend, Sangmu, joins them and orders the same items, what will be the expression for "
                 "the total amount to be paid?"],
       teach=["Predict first: two friends each eat a ₹43 cutlet and a ₹24 rasgulla. Is the total 2 × 43 + 24 or "
              "2 × (43 + 24)?",
              "One share is 43 + 24. Two shares, double of it, need a bracket: 2 × (43 + 24).",
              "Counting items instead gives 2 cutlets and 2 rasgullas, 2 × 43 + 2 × 24. Both ways must agree.",
              "A third friend makes it 3 × (43 + 24) = 3 × 43 + 3 × 24."],
       examples=[
           WE("Meera and Kabir each order a ₹43 cutlet and a ₹24 rasgulla. Write the total with a bracket, remove "
              "the bracket, and compare with 2 × 43 + 24.",
              ["One share is 43 + 24 = 67, so two shares are 2 × (43 + 24) = 2 × 67 = 134.",
               "Counting items: 2 × 43 + 2 × 24 = 86 + 48 = 134.",
               "But 2 × 43 + 24 = 86 + 24 = 110, only one rasgulla, so it is not the same."],
              "2 × (43 + 24) = 2 × 43 + 2 × 24 = 134, while 2 × 43 + 24 = 110", ncert=["2.4.ex15"], fact="ex15",
              expect=[134, 134, 110]),
           WE("A third friend, Tanvi, joins and orders the same. Write the total for three friends with a bracket, "
              "remove it, and find the value.",
              ["Three shares: 3 × (43 + 24).", "Remove the bracket: 3 × 43 + 3 × 24 = 129 + 72.",
               "129 + 72 = 201. Check: 3 × 67 = 201."],
              "3 × (43 + 24) = 3 × 43 + 3 × 24 = 201", ncert=["2.4.sangmu"], fact="sangmu", expect=[201, 201])],
       key_terms=["bracket", "term"], misconceptions=["M_MULT_ONE_TERM"], minutes=10),
     A("T8.C2", "Rows of scouts, and the general rule", "Apply",
       "Students count scouts and guides in two ways, write the matching expression, and state that a multiple of a "
       "sum or a difference is the sum or the difference of the multiples.",
       textbook=["In the Republic Day parade, there are boy scouts and girl guides marching together. The scouts "
                 "march in 4 rows with 5 scouts in each row. The guides march in 3 rows with 5 guides in each row. "
                 "How many scouts and guides are marching in this parade?",
                 "The total number of scouts and guides will be 4 × 5 + 3 × 5. This can also be found by first "
                 "finding the total number of rows, 4 + 3, and then multiplying by the number of children in each "
                 "row, (4 + 3) × 5. Therefore, 4 × 5 + 3 × 5 = (4 + 3) × 5 = 35.",
                 "5 × 4 + 3 ≠ 5 × (4 + 3). Can you explain why?",
                 "Is 5 × (4 + 3) = 5 × (3 + 4) = (3 + 4) × 5?",
                 "Consider 10 × 98 + 3 × 98. This means taking the sum of 10 times 98 and 3 times 98. Clearly, this "
                 "is the same as 10 + 3 = 13 times 98. Thus, 10 × 98 + 3 × 98 = (10 + 3) × 98.",
                 "Similarly, 14 × 10 − 6 × 10 = (14 − 6) × 10. The multiple of a sum (difference) is the same as the "
                 "sum (difference) of the multiples."],
       teach=["Predict first: 4 rows of 5 and 3 rows of 5. Is the crowd 4 × 5 + 3 × 5, or can you count rows first?",
              "Counting rows first gives 4 + 3 = 7 rows of 5, which is (4 + 3) × 5 = 35.",
              "5 × 4 + 3 is 20 + 3 = 23, because the 5 multiplies only the 4. With the bracket it multiplies both.",
              "The same works for a difference: 14 tens take away 6 tens leaves 8 tens."],
       examples=[
           WE("In a parade, 4 rows of 5 scouts march beside 3 rows of 5 guides. Find the number of children in two "
              "ways, and say why 5 × 4 + 3 is different.",
              ["Scouts 4 × 5 = 20 and guides 3 × 5 = 15, so 4 × 5 + 3 × 5 = 20 + 15 = 35.",
               "Rows first: 4 + 3 = 7 rows of 5, so (4 + 3) × 5 = 7 × 5 = 35.",
               "5 × 4 + 3 = 20 + 3 = 23, because the 5 multiplies only the 4."],
              "4 × 5 + 3 × 5 = (4 + 3) × 5 = 35, while 5 × 4 + 3 = 23", ncert=["2.4.ex16"], fact="ex16",
              expect=[35, 35, 23]),
           WE("Write 10 × 98 + 3 × 98 as one product, and 14 × 10 − 6 × 10 as one product, and find both values.",
              ["10 times 98 and 3 times 98 together are 13 times 98: 10 × 98 + 3 × 98 = (10 + 3) × 98 = 13 × 98 = "
               "1274.",
               "14 tens take away 6 tens is 8 tens: 14 × 10 − 6 × 10 = (14 − 6) × 10 = 8 × 10 = 80.",
               "In words: the multiple of a sum or difference is the sum or difference of the multiples."],
              "10 × 98 + 3 × 98 = (10 + 3) × 98 = 1274 and 14 × 10 − 6 × 10 = (14 − 6) × 10 = 80",
              ncert=["2.4.general"], fact="general", expect=[1274, 80])],
       key_terms=["bracket", "distributive property"], misconceptions=["M_MULT_ONE_TERM"], minutes=10),
     A("T8.C3", "Quick products by splitting a number", "Apply",
       "Students change one number of a given product and fix the answer by adding or removing multiples, and split "
       "a number such as 97 into 100 − 3 to find products quickly.",
       textbook=["Tinker the Terms II: Let us understand what happens when we change the numbers occurring in a "
                 "product.",
                 "Given 53 × 18 = 954. Find out 63 × 18. As 63 × 18 means 63 times 18, 63 × 18 = (53 + 10) × 18 = "
                 "53 × 18 + 10 × 18 = 954 + 180 = 1134.",
                 "Find an effective way of evaluating 97 × 25. We can write it as (100 − 3) × 25. This is the same "
                 "as the difference of 100 times 25 and 3 times 25: 97 × 25 = 100 × 25 − 3 × 25. Find this value.",
                 "Use this method to find the following products: (a) 95 × 8 (b) 104 × 15 (c) 49 × 50. Is this "
                 "quicker than the multiplication procedure you use generally? Which other products might be "
                 "quicker to find like the ones above?"],
       teach=["Predict first: 53 × 18 = 954. Is 63 × 18 just 10 more, or 10 times 18 more?",
              "63 is 53 + 10, so there are 10 more lots of 18, which is 180 more.",
              "A number near 100 or 50 can be written as 100 or 50 plus or minus a small number.",
              "Numbers like 99, 101, 48 and 52 are good candidates for this method."],
       examples=[
           WE("Given 53 × 18 = 954, find 63 × 18 without multiplying afresh.",
              ["63 = 53 + 10, so 63 × 18 = (53 + 10) × 18.", "Remove the bracket: 53 × 18 + 10 × 18.",
               "954 + 180 = 1134."],
              "63 × 18 = 1134", ncert=["2.4.ex17", "2.4.tinker2"], fact="ex17", expect=[1134]),
           WE("Find 97 × 25 by writing 97 as 100 − 3.",
              ["97 × 25 = (100 − 3) × 25.", "Remove the bracket: 100 × 25 − 3 × 25 = 2500 − 75.",
               "2500 − 75 = 2425."],
              "97 × 25 = 2425", ncert=["2.4.ex18"], fact="ex18", expect=[2425]),
           WE("Use the same method for 95 × 8, 104 × 15 and 49 × 50, and say which other products suit it.",
              ["95 × 8 = (100 − 5) × 8 = 800 − 40 = 760.", "104 × 15 = (100 + 4) × 15 = 1500 + 60 = 1560.",
               "49 × 50 = (50 − 1) × 50 = 2500 − 50 = 2450.",
               "It is quicker when a number is just below or above 50 or 100 or 1000, so 99 × 12 or 102 × 25 suit it."],
              "95 × 8 = 760, 104 × 15 = 1560, 49 × 50 = 2450", ncert=["2.4.use_method"], fact="use_method",
              expect=[760, 1560, 2450])],
       key_terms=["bracket", "distributive property"], misconceptions=["M_MULT_ONE_TERM"], minutes=10),
     DOER("T8.C4", "Practice: share the multiplier across the bracket", "array_sharer", "Apply",
          "Students multiply a number across the terms of a bracket and gather a common multiplier back out, with "
          "sums and with differences, and use the idea to compare and to count a grid in two ways.",
          ["A number outside a bracket multiplies every term inside.",
           "Gathering a common multiplier undoes it.",
           "A sum or a difference works the same way."],
          items=[
              FIO("2.4.FiO1", "Figure it Out, Q1",
                  "Fill in the blanks with numbers, and boxes with signs, so that the expressions on both sides are "
                  "equal. (a) 3 × (6 + 7) = 3 × 6 + 3 × 7 (b) (8 + 3) × 4 = 8 × 4 + 3 × 4 "
                  "(c) 3 × (5 + 8) = 3 × 5 [ ] 3 × ____ (d) (9 + 2) × 4 = 9 × 4 [ ] 2 × ____ "
                  "(e) 3 × (____ + 4) = 3 × ____ + ____ (f) (____ + 6) × 4 = 13 × 4 + ____ "
                  "(g) 3 × (____ + ____) = 3 × 5 + 3 × 2 (h) (____ + ____) × ____ = 2 × 4 + 3 × 4 "
                  "(i) 5 × (9 − 2) = 5 × 9 − 5 × ____ (j) (5 − 2) × 7 = 5 × 7 − 2 × ____ "
                  "(k) 5 × (8 − 3) = 5 × 8 [ ] 5 × ____ (l) (8 − 3) × 7 = 8 × 7 [ ] 3 × 7 "
                  "(m) 5 × (12 − ____) = ____ [ ] 5 × ____ (n) (15 − ____) × 7 = ____ [ ] 6 × 7 "
                  "(o) 5 × (____ − ____) = 5 × 9 − 5 × 4 (p) (____ − ____) × ____ = 17 × 7 − 9 × 7",
                  ["The number outside multiplies each term inside, and the sign between the terms stays.",
                   "(a) and (b) are already filled in. (c) The box is + and the blank is 8. "
                   "(d) The box is + and the blank is 4.",
                   "(e) Any number n works: 3 × (n + 4) = 3 × n + 3 × 4. For example n = 5 gives 3 × 9 = 27. "
                   "(f) The blank in the bracket is 13 and the last blank is 6 × 4. "
                   "(g) 3 × (5 + 2). (h) (2 + 3) × 4.",
                   "(i) The blank is 2. (j) The blank is 7. (k) The box is − and the blank is 3. (l) The box is −.",
                   "(m) Any number n: 5 × (12 − n) = 5 × 12 − 5 × n. For example n = 3 gives 5 × 9 = 45. "
                   "(n) The bracket blank is 6, and the first blank on the right is 15 × 7, with the box −. "
                   "(o) 5 × (9 − 4). (p) (17 − 9) × 7."],
                  "(c) +, 8 (d) +, 4 (e) any n, 3 × n + 3 × 4 (f) 13, 6 × 4 (g) 5, 2 (h) 2, 3, 4 (i) 2 (j) 7 "
                  "(k) −, 3 (l) − (m) any n (n) 6, 15 × 7, − (o) 9, 4 (p) 17, 9, 7",
                  expect=[8, 4, 13, 2, 7, 3, 6, 9, 4, 17, 9, 7]),
              FIO("2.4.FiO2", "Figure it Out, Q2",
                  "In the boxes below, fill '<', '>' or '=' after analysing the expressions on the left and the "
                  "right. Use reasoning and understanding of terms and brackets to figure this out and not by "
                  "evaluating the expressions. (a) (8 − 3) × 29 [ ] (3 − 8) × 29 (b) 15 + 9 × 18 [ ] (15 + 9) × 18 "
                  "(c) 23 × (17 − 9) [ ] 23 × 17 + 23 × 9 (d) (34 − 28) × 42 [ ] 34 × 42 − 28 × 42",
                  ["(a) 8 − 3 is positive and 3 − 8 is negative, so the left side is greater: >.",
                   "(b) On the left the 18 multiplies only the 9. On the right it multiplies 15 + 9 as well, which "
                   "is more: <.",
                   "(c) Multiplying out the left gives 23 × 17 − 23 × 9, which is less than 23 × 17 + 23 × 9: <.",
                   "(d) Multiplying out the bracket on the left gives exactly the right side: =."],
                  "(a) > (b) < (c) < (d) =", expect=[]),
              FIO("2.4.FiO3", "Figure it Out, Q3",
                  "Here is one way to make 14: 2 × (1 + 6) = 14. Are there other ways of getting 14? Fill them out: "
                  "(a) ____ × (____ + ____) = 14 (b) ____ × (____ + ____) = 14 (c) ____ × (____ + ____) = 14 "
                  "(d) ____ × (____ + ____) = 14",
                  ["The product of the outside number and the bracket sum must be 14, and 14 = 1 × 14 = 2 × 7.",
                   "With the outside number 2, the bracket must be 7: 2 × (2 + 5) and 2 × (3 + 4).",
                   "With the outside number 7, the bracket must be 2: 7 × (1 + 1).",
                   "With the outside number 1, the bracket must be 14: 1 × (5 + 9).",
                   "Check: 2 × 7 = 14, 2 × 7 = 14, 7 × 2 = 14 and 1 × 14 = 14."],
                  "For example 2 × (2 + 5), 2 × (3 + 4), 7 × (1 + 1) and 1 × (5 + 9)", expect=[14, 14, 14, 14]),
              FIO("2.4.FiO4", "Figure it Out, Q4",
                  "Find the sum of the numbers given in each picture in at least two different ways. Describe how you "
                  "solved it through expressions. Picture I is a 3 by 3 grid. Five squares, at the four corners and "
                  "the centre, each show 4. Four circles, in the middle of each side, each show 8. Picture II is a "
                  "4 by 4 grid, with rows reading 5, 6, 6, 5 then 6, 5, 5, 6 then 6, 5, 5, 6 then 5, 6, 6, 5, "
                  "so eight cells show 5 and eight cells show 6.",
                  ["Picture I, by shape: 5 squares of 4 and 4 circles of 8, so 5 × 4 + 4 × 8 = 20 + 32 = 52.",
                   "Picture I, by rows: the top and bottom rows are 4 + 8 + 4 = 16 each and the middle row is "
                   "8 + 4 + 8 = 20, so 2 × (4 + 8 + 4) + (8 + 4 + 8) = 32 + 20 = 52.",
                   "Picture II, by number: eight 5s and eight 6s, so 8 × 5 + 8 × 6 = 8 × (5 + 6) = 8 × 11 = 88.",
                   "Picture II, by rows: two rows read 5 + 6 + 6 + 5 = 22 and two rows read 6 + 5 + 5 + 6 = 22, so "
                   "4 × 22 = 88."],
                  "Picture I: 52 (5 × 4 + 4 × 8). Picture II: 88 (8 × (5 + 6))", expect=[52, 52, 88, 88])],
          ncert=["2.4.FiO1", "2.4.FiO2", "2.4.FiO3", "2.4.FiO4"], misconceptions=["M_MULT_ONE_TERM"])]))

# ============================== T9 Using expressions to solve problems =======================================
TOPICS.append(TOPIC(
    "T9", "M4", "Solving Problems with Expressions", ["2.5"], "Apply",
    "Students choose an expression that fits a story with days taken out, compare two expressions by how their "
    "numbers differ, and match expressions that have the same value by rewriting the terms and brackets.",
    "A story becomes an expression, and reasoning about terms and brackets lets us compare and match expressions "
    "without working them all out.",
    [A("T9.C1", "Choosing the expression that fits the story", "Apply",
       "Students turn a story where some days are left out into an expression with a bracket, and show that two "
       "different looking expressions describe it.",
       teach=["Predict first: a baker bakes 14 loaves a day, except on Sundays. In 6 weeks, is the number of days "
              "7 × 6 or something smaller?",
              "Baking days in a week are 7 − 1 = 6, so the days in 6 weeks are (7 − 1) × 6.",
              "Loaves: (7 − 1) × 6 × 14. Or count all days then remove the shut days: 7 × 6 × 14 − 1 × 6 × 14.",
              "Check that two choices agree."],
       examples=[
           WE("A baker bakes 14 loaves every day except Sunday. Write expressions for the loaves in 6 weeks in two "
              "ways and find the value.",
              ["Baking days in a week: 7 − 1 = 6. In 6 weeks: (7 − 1) × 6 = 36 days.",
               "Loaves: (7 − 1) × 6 × 14 = 36 × 14 = 504.",
               "Other way: all days 7 × 6 × 14 = 588, take away the shut days 1 × 6 × 14 = 84, and 588 − 84 = 504.",
               "Both expressions give 504 loaves."],
              "(7 − 1) × 6 × 14 = 7 × 6 × 14 − 1 × 6 × 14 = 504 loaves", fact="baker", expect=[504, 504])],
       key_terms=["bracket", "term"], misconceptions=["M_BRACKET_IGNORED"], minutes=8),
     A("T9.C2", "Comparing and matching by reasoning", "Apply",
       "Students compare two expressions by asking which number changed and by how much, and match expressions "
       "with the same value by writing both as terms, without working them out.",
       teach=["Predict first: 57 × 30 − 20 and 57 × 31 − 20. Which is bigger, without multiplying?",
              "The second has one more lot of 57, so it is 57 bigger.",
              "To match expressions, rewrite each as terms: remove a bracket after a minus by flipping its signs.",
              "Then equal terms mean equal values."],
       examples=[
           WE("Compare 57 × 30 − 20 and 57 × 31 − 20 without working them out, then check.",
              ["The only change is 31 in place of 30, which gives one more 57.",
               "So the second expression is 57 more than the first.",
               "Check: 57 × 30 − 20 = 1690 and 57 × 31 − 20 = 1747, and 1747 − 1690 = 57."],
              "57 × 30 − 20 < 57 × 31 − 20", fact="cmp57", expect=[1690, 1747, 57]),
           WE("Which of 91 − (35 + 12), 91 − (35 − 12) and −35 + 91 − 12 equal 91 − 35 − 12?",
              ["As terms, 91 − 35 − 12 has the terms 91, −35 and −12.",
               "91 − (35 + 12) = 91 − 35 − 12, same terms. Equal.",
               "−35 + 91 − 12 has the terms −35, 91 and −12, same terms in a new order. Equal.",
               "91 − (35 − 12) = 91 − 35 + 12 has +12 instead of −12. Not equal. Values: 44, 44, 44 and 68."],
              "91 − (35 + 12) and −35 + 91 − 12 are equal to 91 − 35 − 12; 91 − (35 − 12) is not",
              fact="match91", expect=[44, 44, 44, 68])],
       key_terms=["term", "bracket"], misconceptions=["M_EVALUATE_TO_COMPARE"], minutes=8),
     DOER("T9.C3", "Pull it together and do it: write, compare and match", None, "Apply",
          "Students write expressions for stories, find different ways to evaluate, compare pairs by reasoning, "
          "and match equal expressions, and build ten expressions for a chosen number.",
          ["Read the story and write each part as a term.",
           "Compare by how the numbers change, not by working both out.",
           "Match expressions by writing them as terms."],
          items=[
              FIO("2.5.FiO1", "Figure it Out, Q1",
                  "Read the situations given below. Write appropriate expressions for each of them and find their "
                  "values. (a) The district market in Begur operates on all seven days of a week. Rahim supplies "
                  "9 kg of mangoes each day from his orchard and Shyam supplies 11 kg of mangoes each day from his "
                  "orchard to this market. Find the amount of mangoes supplied by them in a week. (b) Binu earns "
                  "₹20,000 per month. She spends ₹5,000 on rent, ₹5,000 on food, and ₹2,000 on other expenses every "
                  "month. What is the amount Binu will save by the end of a year? (c) During the daytime a snail "
                  "climbs 3 cm up a post, and during the night while asleep, accidentally slips down by 2 cm. The "
                  "post is 10 cm high, and a delicious treat is on its top. In how many days will the snail get "
                  "the treat?",
                  ["(a) Each day they supply 9 + 11 kg, for 7 days: 7 × (9 + 11) = 7 × 20 = 140 kg.",
                   "(b) Each month she saves 20000 − (5000 + 5000 + 2000) = 8000. In 12 months: "
                   "12 × 20000 − 12 × (5000 + 5000 + 2000) = 240000 − 144000 = ₹96000.",
                   "(c) Each full day the snail gains 3 − 2 = 1 cm, so after 7 days it is at 7 cm. On the 8th day it "
                   "climbs 3 cm to reach 10 cm before the night: 7 × (3 − 2) + 3 = 10. So 8 days."],
                  "(a) 7 × (9 + 11) = 140 kg (b) ₹96000 (c) 8 days", expect=[140, 96000, 8]),
              FIO("2.5.FiO2", "Figure it Out, Q2",
                  "Melvin reads a two-page story every day except on Tuesdays and Saturdays. How many stories would "
                  "he complete reading in 8 weeks? Which of the expressions below describes this scenario? "
                  "(a) 5 × 2 × 8 (b) (7 − 2) × 8 (c) 8 × 7 (d) 7 × 2 × 8 (e) 7 × 5 − 2 (f) (7 + 2) × 8 "
                  "(g) 7 × 8 − 2 × 8 (h) (7 − 5) × 8",
                  ["He reads on 7 − 2 = 5 days a week, one story a day, so 5 × 8 = 40 stories in 8 weeks.",
                   "(b) (7 − 2) × 8 = 5 × 8 = 40 matches.",
                   "(g) 7 × 8 − 2 × 8 = 56 − 16 = 40 also matches, as the multiple of a difference.",
                   "The others do not: (a) 80, (c) 56, (d) 112, (e) 33, (f) 72, (h) 16."],
                  "40 stories; expressions (b) and (g)", expect=[40, 40, 40]),
              FIO("2.5.FiO3", "Figure it Out, Q3",
                  "Find different ways of evaluating the following expressions: (a) 1 − 2 + 3 − 4 + 5 − 6 + 7 − 8 + 9 "
                  "− 10 (b) 1 − 1 + 1 − 1 + 1 − 1 + 1 − 1 + 1 − 1",
                  ["(a) In pairs: (1 − 2) + (3 − 4) + (5 − 6) + (7 − 8) + (9 − 10) = five lots of −1, which is −5.",
                   "(a) Another way: leave 1 and 10 out, then 1 + (−2 + 3) + (−4 + 5) + (−6 + 7) + (−8 + 9) − 10 = "
                   "1 + 4 − 10 = −5.",
                   "(b) In pairs: (1 − 1) five times is 0. Or group (−1 + 1) after the first 1: "
                   "1 + (−1 + 1) + (−1 + 1) + (−1 + 1) + (−1 + 1) − 1 = 0."],
                  "(a) −5 (b) 0", expect=[-5, 0]),
              FIO("2.5.FiO4", "Figure it Out, Q4",
                  "Compare the following pairs of expressions using '<', '>' or '=' or by reasoning. "
                  "(a) 49 − 7 + 8 and 49 − 7 + 8 (b) 83 × 42 − 18 and 83 × 40 − 18 (c) 145 − 17 × 8 and "
                  "145 − 17 × 6 (d) 23 × 48 − 35 and 23 × (48 − 35) (e) (16 − 11) × 12 and −11 × 12 + 16 × 12 "
                  "(f) (76 − 53) × 88 and 88 × (53 − 76) (g) 25 × (42 + 16) and 25 × (43 + 15) "
                  "(h) 36 × (28 − 16) and 35 × (27 − 15)",
                  ["(a) The two sides are the same expression, so they are equal: =.",
                   "(b) 83 × 42 has two more lots of 83 than 83 × 40: >.",
                   "(c) 17 × 8 takes away more than 17 × 6, so the left is smaller: <.",
                   "(d) On the left, only 35 is taken away from the whole product 23 × 48. On the right, 23 is "
                   "multiplied by a much smaller number, 48 − 35: >.",
                   "(e) The right side is 16 × 12 − 11 × 12 = (16 − 11) × 12: =.",
                   "(f) 76 − 53 = 23 is positive and 53 − 76 = −23 is negative: >.",
                   "(g) Both brackets add to 58: =.",
                   "(h) 36 is more than 35 and 28 − 16 = 12 equals 27 − 15 = 12, so the left is bigger: >."],
                  "(a) = (b) > (c) < (d) > (e) = (f) > (g) = (h) >", expect=[]),
              FIO("2.5.FiO5", "Figure it Out, Q5",
                  "Identify which of the following expressions are equal to the given expression without "
                  "computation. You may rewrite the expressions using terms or removing brackets. There can be more "
                  "than one expression which is equal to the given expression. (a) 83 − 37 − 12: (i) 84 − 38 − 12 "
                  "(ii) 84 − (37 + 12) (iii) 83 − 38 − 13 (iv) −37 + 83 − 12. (b) 93 + 37 × 44 + 76: "
                  "(i) 37 + 93 × 44 + 76 (ii) 93 + 37 × 76 + 44 (iii) (93 + 37) × (44 + 76) "
                  "(iv) 37 × 44 + 93 + 76",
                  ["(a) The terms of 83 − 37 − 12 are 83, −37 and −12. (iv) has the same terms in a new order: equal.",
                   "(i) 84 − 38 − 12: 84 and 38 are each one more, so the changes cancel: equal.",
                   "(ii) 84 − (37 + 12) = 84 − 37 − 12 has 84 where there was 83: one more, not equal. "
                   "(iii) 83 − 38 − 13 takes one extra away twice: not equal. Values: 34, 34, 35, 32, 34.",
                   "(b) The terms of 93 + 37 × 44 + 76 are 93, 37 × 44 and 76. Only (iv) has the same terms. "
                   "(i) and (ii) change the products, and (iii) multiplies two sums. "
                   "Values: 1797 for the given expression and for (iv)."],
                  "(a) (i) and (iv) are equal; (ii) and (iii) are not (b) only (iv) is equal",
                  expect=[34, 34, 35, 32, 34, 1797]),
              FIO("2.5.FiO6", "Figure it Out, Q6",
                  "Choose a number and create ten different expressions having that value.",
                  ["Choose 24. Any ten expressions with value 24 work, for example:",
                   "12 + 12, 4 × 6, 48 ÷ 2, 34 − 10, 20 + 4, 30 − 6, 8 × 3, 100 − 76, 2 × (5 + 7), 72 ÷ 3.",
                   "Check each: all of them equal 24."],
                  "Answers vary; ten expressions for 24 are 12 + 12, 4 × 6, 48 ÷ 2, 34 − 10, 20 + 4, 30 − 6, 8 × 3, "
                  "100 − 76, 2 × (5 + 7) and 72 ÷ 3", expect=[24])],
          ncert=["2.5.FiO1", "2.5.FiO2", "2.5.FiO3", "2.5.FiO4", "2.5.FiO5", "2.5.FiO6"],
          misconceptions=["M_EVALUATE_TO_COMPARE"])]))

# ============================== T10 Puzzle: Expression Engineer ==============================================
TOPICS.append(TOPIC(
    "T10", "M4", "Puzzle Time: Expression Engineer", ["Puzzle Time"], "Create",
    "Students build target values from a fixed set of digits using the four operations and brackets, and invent "
    "similar puzzles of their own.",
    "A few digits, four operations and brackets can build many different values.",
    [A("T10.C1", "Build values from three 3s", "Create",
       "",
       textbook=["Expression Engineer!",
                 "Using three 3's along with the four operations (addition, subtraction, multiplication, and "
                 "division) and brackets as needed we can create several expressions. For example, (3 + 3) ÷ 3 = 2, "
                 "3 + 3 − 3 = 3, 3 × 3 + 3 = 12, and so on.",
                 "Using four 4's, create expressions to get all values from 1 to 20.",
                 "Using the numbers 1, 2, 3, 4, and 5 exactly once in any order get as many values as possible "
                 "between −10 and +10.",
                 "Using the numbers 0 to 9 exactly once in any order, make an expression with a value 100.",
                 "What other similar interesting questions can you ask?"],
       teach=["Predict first: with three 3s, which values from 0 to 12 can you reach?",
              "Try each pairing of the operations and brackets, and keep a table of the values found.",
              "Three 3s reach 3 + 3 + 3 = 9, 3 × 3 − 3 = 6, 3 + 3 ÷ 3 = 4, 3 − 3 ÷ 3 = 2, 3 × (3 − 3) = 0."],
       examples=[
           WE("Using three 3s, the four operations and brackets, find expressions for 0, 2, 4, 6, 9 and 12.",
              ["0: 3 × (3 − 3) = 0.", "2: (3 + 3) ÷ 3 = 2.", "4: 3 + 3 ÷ 3 = 3 + 1 = 4.", "6: 3 × 3 − 3 = 9 − 3 = 6.",
               "9: 3 + 3 + 3 = 9.", "12: 3 × 3 + 3 = 9 + 3 = 12."],
              "0, 2, 4, 6, 9 and 12 are all reachable", ncert=["puzzle.engineer"], fact="three3s",
              expect=[0, 2, 4, 6, 9, 12])],
       key_terms=["expression"], enrichment=True, minutes=8),
     DOER("T10.C2", "Practice: engineer your own values", None, "Create",
          "",
          ["Four 4s can make 1 to 9 with plain operations. For example 4 ÷ 4 + 4 ÷ 4 = 2, 4 + 4 − 4 ÷ 4 = 7.",
           "Joining two 4s as 44 helps: (44 − 4) ÷ 4 = 10. Using 0.4 gives 4 ÷ 4 + 4 ÷ 0.4 = 11.",
           "With the digits 1 to 5 exactly once, values from −10 to 10 can all be made, for example "
           "1 + 2 + 3 + 4 − 5 = 5.",
           "With the digits 0 to 9, 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 × 9 = 100."],
          enrichment=True)]))

# ============================== T11 Summary ==================================================================
TOPICS.append(TOPIC(
    "T11", "M4", "Summary: Arithmetic Expressions", ["Summary"], "Remember",
    None,
    "Values, comparing by reasoning, terms and brackets, swapping, removing brackets and the distributive property in "
    "one place.",
    [A("T11.C1", "What we found about expressions", "Remember",
       "Students restate how expressions are compared by reasoning, read as sums of terms, swapped and grouped, "
       "and how brackets are removed after a plus sign, a minus sign and a multiplier.",
       textbook=["Summary",
                 "We have been reading and evaluating simple expressions for quite some time now. Here we started by "
                 "revising the meaning of some simple expressions and their values.",
                 "We learnt how to compare certain expressions through reasoning instead of bluntly evaluating them.",
                 "To help read and evaluate complex expressions without confusion, we use terms and brackets.",
                 "When an expression is written as a sum of terms, changing the order of the terms or grouping the "
                 "terms does not change the value of the expression. This is because of the commutative property of "
                 "addition and the associative property of addition, respectively.",
                 "To evaluate expressions within brackets, we saw that when we remove brackets preceded by a negative "
                 "sign, the terms within the bracket change their sign.",
                 "We also learnt about the distributive property: multiplying a number with an expression inside "
                 "brackets is equal to multiplying the number with each term in the bracket."],
       teach=["Our opening question is settled: different looking expressions can share one value.",
              "Terms are the unit: keep each sign with its number when you swap, group or remove brackets.",
              "Still open for you: write an expression for your own week of spending and find three ways to evaluate it."],
       ncert=["summary"], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
