# -*- coding: utf-8 -*-
"""Topics T6 to T9 (module M2: simplifying algebraic expressions). Book sections 4.4 and 4.5 (Formula Detective)."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T6 Simplifying like terms ====================================================
TOPICS.append(TOPIC(
    "T6", "M2", "Simplifying: Like Terms", ["4.4"], "Apply",
    "Students write the perimeter of a rectangle and simplify it, add like terms in sales totals and in areas, "
    "explain why like terms combine using the distributive property, and tell like terms from unlike terms.",
    "Terms with the same letter-numbers are like terms and combine into one term; terms with different "
    "letter-numbers cannot, so the expression is already in its simplest form.",
    [A("T6.C1", "Perimeter of a rectangle: l + b + l + b", "Apply",
       "Students write the perimeter of a rectangle as a sum of its sides, swap and group the terms to get 2l + 2b, "
       "and check that both expressions take the same value.",
       textbook=["Earlier we found expressions to find perimeters of different regular figures in terms of their "
                 "sides. Let us now find an expression to find the perimeter of a rectangle.",
                 "Find the sum of length + breadth + length + breadth. Let us use the letter-numbers l and b in "
                 "place of length and breadth respectively. Let p denote the perimeter. Then p = l + b + l + b.",
                 "The terms of an expression can be added in any order, so p = l + l + b + b. As l + l = 2 × l = 2l, "
                 "and b + b = 2 × b = 2b, we have p = 2l + 2b.",
                 "The initial expression and the final expression look different. However, they are equal in the "
                 "sense that they both take the same values when letter-numbers are replaced by numbers. If l = 3 "
                 "and b = 4, then l + b + l + b = 3 + 4 + 3 + 4 = 14 and 2l + 2b = 2 × 3 + 2 × 4 = 14. We call the "
                 "expression 2l + 2b the simplified form of l + b + l + b."],
       teach=["Predict first: a rectangle has two lengths and two breadths. Can the sum of its four sides be written "
              "with fewer terms?",
              "Swap the terms so that the same letters sit together, then count them: l + l is 2l and b + b is 2b.",
              "The two expressions look different but take the same value for every l and b, so 2l + 2b is the "
              "simplified form."],
       examples=[
           WE("A rectangle has length l and breadth b. Write its perimeter as a sum of sides, simplify it, and check "
              "with l = 3 and b = 4.",
              ["Perimeter p = l + b + l + b.", "Swap the terms: p = l + l + b + b.",
               "l + l = 2 × l = 2l and b + b = 2 × b = 2b, so p = 2l + 2b.",
               "Check with l = 3 and b = 4: l + b + l + b = 3 + 4 + 3 + 4 = 14.",
               "And 2l + 2b = 2 × 3 + 2 × 4 = 6 + 8 = 14. Both give 14."],
              "p = 2l + 2b, which is the simplified form; both forms give 14 for l = 3 and b = 4",
              ncert=["4.4.rect"])],
       key_terms=["simplified form"], minutes=8),
     A("T6.C2", "Pencils and erasers: adding like terms", "Apply",
       "Students write the money earned from each item as a multiple of its price, add the terms using the "
       "distributive property, and explain why 18c + 11d cannot be simplified further.",
       textbook=["Example 5: Here is a table showing the number of pencils and erasers sold in a shop. The price per "
                 "pencil is c, and the price per eraser is d. Find the total money earned by the shopkeeper during "
                 "these three days. Pencils sold on Days 1, 2, 3: 5, 3, 10. Erasers sold: 4, 6, 1.",
                 "The money earned by selling pencils on Day 1 is 5c. The total money earned by the sale of pencils "
                 "is 5c + 3c + 10c. Can we simplify this expression further and reduce the number of terms?",
                 "The letter-number c is added (5 + 3 + 10) times. This is the distributive property of numbers: "
                 "5 × c + 3 × c + 10 × c = (5 + 3 + 10) × c = 18 × c = 18c.",
                 "If c = 50, find the total amount earned by the sale of pencils.",
                 "The expression for the total money earned by selling pencils and erasers during these three days "
                 "is 18c + 11d. There is no way of further simplifying this expression as it contains different "
                 "letter-numbers. It is in its simplest form."],
       teach=["Predict first: if each pencil costs c, what did the shop earn from the 5 pencils on Day 1? From all "
              "three days?",
              "5c + 3c + 10c adds the letter c to itself (5 + 3 + 10) times, so it is 18c.",
              "Pencils and erasers have different prices c and d, so their terms cannot be joined: 18c + 11d is "
              "already simplest.",
              "Check that 5c + 3c + 10c and 18c give the same value for different c."],
       examples=[
           WE("Pencil sales on three days are 5, 3 and 10, each at price c. Simplify the total for pencils, and find "
              "it when c = 50 rupees.",
              ["Day 1 is 5c, Day 2 is 3c and Day 3 is 10c.", "Total = 5c + 3c + 10c.",
               "5 × c + 3 × c + 10 × c = (5 + 3 + 10) × c = 18 × c = 18c.",
               "With c = 50: 18c = 18 × 50 = 900 rupees.",
               "Check with c = 2: 5 × 2 + 3 × 2 + 10 × 2 = 10 + 6 + 20 = 36, and 18 × 2 = 36."],
              "18c, and 900 rupees when c = 50", ncert=["4.4.ex5_a"]),
           WE("Eraser sales on three days are 4, 6 and 1, each at price d. Write and simplify the total for erasers, "
              "then the total for pencils and erasers, and say whether it can be simplified further.",
              ["Erasers: 4d + 6d + 1d = (4 + 6 + 1) × d = 11d.", "Pencils and erasers together: 18c + 11d.",
               "The terms 18c and 11d have different letter-numbers, so they cannot be added into one term.",
               "So 18c + 11d is in its simplest form."],
              "11d for erasers, and 18c + 11d in simplest form", ncert=["4.4.ex5_b"])],
       key_terms=["distributive property", "simplest form"], misconceptions=["M_UNLIKE_ADD"], minutes=12),
     A("T6.C3", "Areas of split rectangles, and like terms", "Apply",
       "Students find the area of a big rectangle in two ways, reading 4v + 3v as 7v and 12n − 4n as 8n, and "
       "name sets of terms as like or unlike terms.",
       textbook=["Example 6: A big rectangle is split into two smaller rectangles. Write an expression describing "
                 "the area of the bigger rectangle. The areas of the smaller rectangles are 4v and 3v square units "
                 "(the side v is shared, and the other sides are 4 and 3).",
                 "The area of the bigger rectangle can be found in two ways: by directly using its side lengths v "
                 "and (4 + 3), or by adding the areas of the smaller rectangles. The first way gives 7v, and the "
                 "second way gives 4v + 3v. We know that they are equal: 4v + 3v = 7v.",
                 "A big rectangle ABCD is split into two rectangles with shared side n. The area of AEFD can be "
                 "found by using the side lengths n and (12 − 4), or by subtracting the area of EBCF from that of "
                 "ABCD. The first method gives 8n, and the second gives 12n − 4n, and they are equal.",
                 "Sets of terms such as (5c, c, 10c) and (12n, −4n) that involve the same letter-numbers are called "
                 "like terms. Sets of terms such as 18c and 11d are called unlike terms as they have different "
                 "letter-numbers. Like terms can be added together and simplified into a single term."],
       teach=["Predict first: a rectangle of height v is made of a 4 wide piece and a 3 wide piece. How wide is the "
              "whole, and what is its area?",
              "Two ways to find one area must agree: v times (4 + 3) is 7v, and 4v + 3v is also 7v.",
              "With subtraction: a rectangle of height n and width 12, with a piece of width 4 removed, has area "
              "n times (12 − 4) = 8n, and also 12n − 4n = 8n.",
              "Terms with the same letter-numbers are like terms and combine. Terms with different letter-numbers "
              "are unlike terms and stay apart."],
       examples=[
           WE("A big rectangle of height v is split into two rectangles of widths 4 and 3, with areas 4v and 3v. "
              "Write the area of the big rectangle in two ways.",
              ["Way 1: the width of the big rectangle is 4 + 3 = 7, so the area is 7 × v = 7v.",
               "Way 2: add the two parts, 4v + 3v.", "The two ways must agree, so 4v + 3v = 7v.",
               "4v and 3v have the same letter-number v, so they are like terms."],
              "7v, and 4v + 3v = 7v", ncert=["4.4.ex6_a"]),
           WE("A rectangle ABCD of height n and width 12 has a piece EBCF of width 4 cut off. Write the area of "
              "the piece AEFD that is left in two ways, and say which pairs are like terms.",
              ["Way 1: the width left is 12 − 4 = 8, so the area is 8 × n = 8n.",
               "Way 2: subtract the cut piece from the whole, 12n − 4n.", "The two ways agree, so 12n − 4n = 8n.",
               "12n and −4n are like terms. 18c and 11d from the pencil shop are unlike terms."],
              "8n, and 12n − 4n = 8n; 12n and −4n are like terms", ncert=["4.4.ex6_b"])],
       key_terms=["like terms", "unlike terms"], misconceptions=["M_UNLIKE_ADD"], minutes=12),
     DOER("T6.C4", "Practice: gather the like terms", "like_term_gatherer", "Apply",
          "Students sort the terms of an expression into like groups, add each group into one term, and test that the "
          "simplified form takes the same values as the original for a few numbers.",
          ["Look at the letter-numbers of each term to find the like terms.",
           "Add the numbers in front of each group of like terms.",
           "Terms with different letter-numbers stay as separate terms."])]))

# ============================== T7 Adding and subtracting expressions ========================================
TOPICS.append(TOPIC(
    "T7", "M2", "Adding and Subtracting Expressions", ["4.4"], "Apply",
    "Students subtract one expression from another by opening a bracket with a minus sign, add several expressions "
    "by grouping like terms, compare two totals by subtracting them, and simplify a bracketed expression.",
    "A minus sign before a bracket changes the sign of every term inside; after the brackets are opened, like terms "
    "are grouped and added.",
    [A("T7.C1", "Chairs and tables: a bracket with a minus sign", "Apply",
       "Students write the amount paid minus the amount returned as two brackets, open the second bracket by "
       "changing every sign, and group like terms to a simplified expression.",
       textbook=["Example 7: A shop rents out chairs and tables for a day's use. To rent them, one has to first pay "
                 "40 rupees per chair and 75 rupees per table. When the furniture is returned, the shopkeeper pays "
                 "back 6 rupees for a chair and 10 rupees for a table.",
                 "Write an expression for the total number of rupees paid if x chairs and y tables are rented. "
                 "The total amount paid at the beginning is 40x + 75y, and the total amount returned is 6x + 10y. "
                 "So, the total amount paid = (40x + 75y) − (6x + 10y). Can we simplify this expression?",
                 "Recalling how we open brackets in an arithmetic expression, (40x + 75y) − (6x + 10y) = "
                 "(40x + 75y) − 6x − 10y. Since the terms can be added in any order, the remaining bracket can be "
                 "opened and the expression becomes 40x + 75y + (−6x) + (−10y).",
                 "We can group the like terms together: 40x + (−6x) + 75y + (−10y) = (40 − 6)x + (75 − 10)y = "
                 "34x + 65y.",
                 "Math Talk: Could we have written the initial expression as (40x + 75y) + (−6x − 10y)?"],
       teach=["Predict first: for x chairs and y tables, what is paid at the start and what comes back?",
              "The net amount is paid minus returned. A minus sign before a bracket changes the sign of each term "
              "inside it.",
              "Group the like terms: the x terms together and the y terms together.",
              "Math Talk: subtracting (6x + 10y) is the same as adding (−6x − 10y), so both ways of writing agree."],
       examples=[
           WE("A shop charges 40 rupees per chair and 75 rupees per table, and returns 6 rupees per chair and 10 "
              "rupees per table. Find the amount paid for x chairs and y tables, and say if (40x + 75y) + "
              "(−6x − 10y) is the same.",
              ["Paid at the start: 40x + 75y. Returned: 6x + 10y.", "Amount paid = (40x + 75y) − (6x + 10y).",
               "Open the second bracket and change both signs: 40x + 75y − 6x − 10y.",
               "Group like terms: (40x − 6x) + (75y − 10y) = (40 − 6)x + (75 − 10)y = 34x + 65y.",
               "Math Talk: (40x + 75y) + (−6x − 10y) opens to 40x + 75y − 6x − 10y, the same expression, so yes."],
              "34x + 65y rupees; yes, writing (40x + 75y) + (−6x − 10y) gives the same expression",
              ncert=["4.4.ex7", "4.4.ex7_talk"])],
       key_terms=["bracket", "like terms"], misconceptions=["M_BRACKET_SIGN"], minutes=10),
     A("T7.C2", "Charu's quiz scores", "Apply",
       "Students read what 7p − 3q means, evaluate the three round scores for given p and q, add the expressions to "
       "get the total, and subtract two totals to see how much more one scored.",
       textbook=["Example 8: Charu has been through three rounds of a quiz. Her scores in the three rounds are "
                 "7p − 3q, 8p − 4q, and 6p − 2q. Here, p represents the score for a correct answer and q represents "
                 "the penalty for an incorrect answer.",
                 "What do each of the expressions mean? If p = 4 and q = 1, find Charu's score in the first round: "
                 "7 × 4 − 3 × 1 = 7 × 4 + (−3 × 1) = 28 + (−3) = 25. What are her scores in the second and third "
                 "rounds? What if there is no penalty? What will be the value of q in that situation?",
                 "What is her final score after the three rounds? It is the sum (7p − 3q) + (8p − 4q) + (6p − 2q) = "
                 "21p − 9q.",
                 "Her friend Krishita's score after three rounds is 23p − 7q. Math Talk: Give some possible scores "
                 "for Krishita in the three rounds so that they add up to 23p − 7q. Can we say who scored more? "
                 "How much more has Krishita scored than Charu? Simplify 23p − 7q − (21p − 9q)."],
       teach=["Predict first: in 7p − 3q, what could 7 and 3 count? Remember p is the score for a correct answer and "
              "q is the penalty for a wrong one.",
              "Replace p and q by numbers, then add the terms. With no penalty, q is 0.",
              "To add three scores, remove the brackets and group the p terms and the q terms.",
              "To find how much more one total is than another, subtract, with a bracket round the second total."],
       examples=[
           WE("In the quiz, p = 4 is the score for a correct answer and q = 1 is the penalty for a wrong one. Say what "
              "7p − 3q means, find Charu's three round scores 7p − 3q, 8p − 4q and 6p − 2q, and say what q would be "
              "with no penalty.",
              ["7p − 3q means 7 correct answers scoring p each, minus 3 wrong answers penalised q each.",
               "Round 1: 7 × 4 − 3 × 1 = 28 − 3 = 25.", "Round 2: 8 × 4 − 4 × 1 = 32 − 4 = 28.",
               "Round 3: 6 × 4 − 2 × 1 = 24 − 2 = 22.", "With no penalty, q = 0."],
              "Round scores 25, 28 and 22; with no penalty q is 0", ncert=["4.4.ex8_a"]),
           WE("Find Charu's final score as an expression by adding her three round scores 7p − 3q, 8p − 4q, "
              "6p − 2q, and check it when p = 4 and q = 1.",
              ["Final score = (7p − 3q) + (8p − 4q) + (6p − 2q).",
               "Remove the brackets: 7p − 3q + 8p − 4q + 6p − 2q.",
               "Group like terms: (7 + 8 + 6)p − (3 + 4 + 2)q = 21p − 9q.",
               "Check with p = 4 and q = 1: 21 × 4 − 9 × 1 = 84 − 9 = 75, and 25 + 28 + 22 = 75."],
              "21p − 9q, which is 75 when p = 4 and q = 1", ncert=["4.4.ex8_b"]),
           WE("Krishita's final score is 23p − 7q. Give three round scores that could add up to it, and find how much "
              "more she scored than Charu, whose score is 21p − 9q.",
              ["One possible set of rounds: 8p − 2q, 7p − 3q and 8p − 2q add to (8 + 7 + 8)p − (2 + 3 + 2)q = "
               "23p − 7q.", "Difference = 23p − 7q − (21p − 9q).",
               "Open the bracket and change both signs: 23p − 7q − 21p + 9q.",
               "Group like terms: (23 − 21)p + (−7 + 9)q = 2p + 2q.",
               "Since p and q are both positive, 2p + 2q is positive, so Krishita scored more. With p = 4 and "
               "q = 1 the difference is 2 × 4 + 2 × 1 = 10."],
              "Krishita scored 2p + 2q more, which is 10 when p = 4 and q = 1", ncert=["4.4.ex8_c"])],
       key_terms=["difference"], misconceptions=["M_BRACKET_SIGN"], minutes=14),
     A("T7.C3", "Simplify 4(x + y) − y", "Apply",
       "Students open a bracket with the distributive property, treat the last term as a negative term, and group "
       "like terms to simplify 4(x + y) − y.",
       textbook=["Example 9: Simplify the expression 4(x + y) − y. Using the distributive property, this "
                 "expression can be simplified to 4(x + y) − y = 4x + 4y − y = 4x + 4y + (−y) = 4x + (4 − 1)y = "
                 "4x + 3y."],
       teach=["Predict first: when 4 multiplies a bracket, does it multiply only the first term or every term inside?",
              "4 multiplies every term in the bracket: 4(x + y) = 4x + 4y.",
              "Then 4y − y has the like terms 4y and −y, which combine to 3y."],
       examples=[
           WE("Simplify 4(x + y) − y.",
              ["Distribute the 4 over both terms: 4(x + y) = 4x + 4y.", "So 4(x + y) − y = 4x + 4y − y.",
               "Write − y as + (−y): 4x + 4y + (−y).", "Group the like terms: 4x + (4 − 1)y = 4x + 3y.",
               "Check with x = 1 and y = 1: 4 × (1 + 1) − 1 = 7, and 4 × 1 + 3 × 1 = 7."],
              "4x + 3y", ncert=["4.4.ex9"])],
       key_terms=["distributive property"], misconceptions=["M_DISTRIB_FIRST"], minutes=8),
     DOER("T7.C4", "Practice: open the bracket, then combine", "minus_sign_flipper", "Apply",
          "Students open brackets that have a plus or a minus sign outside, or a number outside, and then group like "
          "terms to reach the simplest form.",
          ["A plus sign outside leaves the signs inside alone.",
           "A minus sign outside changes every sign inside.", "A number outside multiplies every term inside."])]))

# ============================== T8 Is it the same? ===========================================================
TOPICS.append(TOPIC(
    "T8", "M2", "Is it the Same? Checking Simplest Forms", ["4.4"], "Apply",
    "Students test whether two expressions are equal by comparing their values for several numbers, add the numbers "
    "in a picture in different ways, and check claimed simplest forms, correcting the slips and counting terms.",
    "Two expressions are equal only if they take the same value for every number; simplest forms have brackets "
    "removed, like terms added, and number terms added.",
    [A("T8.C1", "Are 5u and 5 + u equal?", "Apply",
       "Students replace the letter-number by several numbers in two expressions, compare the values, and decide "
       "from different values that 5u is not 5 + u and 10y − 3 is not 10(y − 3).",
       textbook=["Example 10: Are the expressions 5u and 5 + u equal to each other? The expression 5u means 5 times "
                 "the number u, and the expression 5 + u means 5 more than the number u. These two being different "
                 "operations, they should give different values for most values of u. Let us check this.",
                 "Fill the blanks by replacing the letter-numbers by numbers; an example is shown. Then compare the "
                 "values that 5u and 5 + u take. If the expressions are equal, then they should take the same "
                 "values for any given value of u.",
                 "Are the expressions 10y − 3 and 10(y − 3) equal? 10y − 3, short for 10 × y − 3, means 3 less than "
                 "10 times y. 10(y − 3), short for 10 × (y − 3), means 10 times (3 less than y). Let us compare the "
                 "values for different values of y. After filling in the two diagrams, do you think the two "
                 "expressions are equal?"],
       teach=["Predict first: is 5u the same as 5 + u? Try u = 2 in your head.",
              "Two expressions are equal only if they take the same value for every value of the letter-number. One "
              "number that gives different values is enough to show they are not equal.",
              "Do the same for 10y − 3 and 10(y − 3): the first is 3 less than 10 times y; the second is 10 times "
              "3-less-than-y."],
       examples=[
           WE("Replace u by 11, 8, 2 and 5 in 5u and in 5 + u, and say whether the two expressions are equal.",
              ["u = 11: 5u = 5 × 11 = 55 and 5 + u = 5 + 11 = 16.", "u = 8: 5u = 40 and 5 + u = 13.",
               "u = 2: 5u = 10 and 5 + u = 7.", "u = 5: 5u = 25 and 5 + u = 10.",
               "The values differ every time, so 5u and 5 + u are not equal."],
              "5u takes 55, 40, 10, 25 and 5 + u takes 16, 13, 7, 10, so they are not equal",
              ncert=["4.4.ex10_u"]),
           WE("Replace y by 2, 10, 0 and 7 in 10y − 3 and in 10(y − 3), and say whether the two expressions are "
              "equal.",
              ["y = 2: 10y − 3 = 10 × 2 − 3 = 17, and 10(y − 3) = 10 × (2 − 3) = 10 × (−1) = −10.",
               "y = 10: 10 × 10 − 3 = 97, and 10 × (10 − 3) = 10 × 7 = 70.",
               "y = 0: 10 × 0 − 3 = −3, and 10 × (0 − 3) = 10 × (−3) = −30.",
               "y = 7: 10 × 7 − 3 = 67, and 10 × (7 − 3) = 10 × 4 = 40.",
               "The values differ every time, so 10y − 3 and 10(y − 3) are not equal."],
              "10y − 3 takes 17, 97, −3, 67 and 10(y − 3) takes −10, 70, −30, 40, so they are not equal",
              ncert=["4.4.ex10_y"])],
       key_terms=["equal expressions"], misconceptions=["M_ADD_NOT_MULT", "M_BRACKET_EARLY"], minutes=12),
     A("T8.C2", "Adding the numbers in a picture", "Apply",
       "Students add the numbers in a picture in three different ways, row by row, by like terms, and by doubling "
       "the upper half, and see that all three simplify to 2r + 2s + 24.",
       textbook=["Example 11: What is the sum of the numbers in the picture (unknown values are denoted by "
                 "letter-numbers)? There are many ways to go about it.",
                 "1. Adding row wise gives (4 × 3) + (r + s) + (r + s) + (4 × 3). 2. Adding like terms together "
                 "gives (8 × 3) + (r + r) + (s + s). 3. Adding the upper half and doubling gives "
                 "2 × (4 × 3 + r + s).",
                 "The three expressions might seem different. We can simplify each one and see that they all are the "
                 "same: 2r + 2s + 24."],
       teach=["Predict first: in a picture with eight 3s, two r and two s, what is the total? Find it any way you like.",
              "Add by rows, by like terms, or by doubling the upper half. Each way gives an expression.",
              "Simplify each expression: all of them come to 2r + 2s + 24."],
       examples=[
           WE("A picture has a top row of four 3s, then two rows each with one r and one s, and a bottom row of four "
              "3s. Add all the numbers in three ways and simplify.",
              ["Row wise: (4 × 3) + (r + s) + (r + s) + (4 × 3) = 12 + r + s + r + s + 12 = 24 + 2r + 2s.",
               "Like terms: (8 × 3) + (r + r) + (s + s) = 24 + 2r + 2s.",
               "Upper half doubled: 2 × (4 × 3 + r + s) = 2 × (12 + r + s) = 24 + 2r + 2s.",
               "All three give the same simplified expression, 2r + 2s + 24."],
              "2r + 2s + 24", ncert=["4.4.ex11"])],
       key_terms=["simplified form"], minutes=10),
     A("T8.C3", "Mind the Mistake, Mend the Mistake: simplest forms", "Apply",
       "Students check eleven claimed simplest forms, spot which are wrong and what slip may have caused each, "
       "correct them, and compare the number of terms with the number of letter-numbers.",
       textbook=["Some simplifications of algebraic expressions are done below. The expression on the right-hand side "
                 "should be in its simplest form. Observe each of them and see if there is a mistake. If you think "
                 "there is a mistake, try to explain what might have gone wrong. Then, simplify it correctly.",
                 "1. 3a + 2b is claimed to be 5. 2. 3b − 2b − b is claimed to be 0. 3. 6(p + 2) is claimed to be "
                 "6p + 8. 4. (4x + 3y) − (3x + 4y) is claimed to be x + y. 5. 5 − (2 − 6z) is claimed to be "
                 "3 − 6z. 6. 2 + (x + 3) is claimed to be 2x − 6. 7. 2y + (3y − 6) is claimed to be −y + 6. "
                 "8. 7p − p + 5q − 2q is claimed to be 7p + 3q. 9. 5(2w + 3x + 4w) is claimed to be "
                 "10w + 15x + 20w. 10. 3j + 6k + 9h + 12 is claimed to be 3(j + 2k + 3h + 4). 11. "
                 "4(2r + 3s + 5) is claimed to be −20 − 8r − 12s.",
                 "Take a look at all the corrected simplest forms (brackets are removed, like terms are added, and "
                 "terms with only numbers are also added). Is there any relation between the number of terms and "
                 "the number of letter-numbers these expressions have?"],
       teach=["Predict first: simplify each expression yourself, then compare with the claim.",
              "Typical slips: adding unlike terms, multiplying only the first term in a bracket, forgetting to change "
              "signs after a minus bracket, and stopping before like terms are added.",
              "A simplest form has no brackets, all like terms added and all number terms added.",
              "After correcting, count the terms and the different letter-numbers in each simplest form and compare."],
       examples=[
           WE("Check claims 1 to 4. 1: 3a + 2b = 5. 2: 3b − 2b − b = 0. 3: 6(p + 2) = 6p + 8. 4: "
              "(4x + 3y) − (3x + 4y) = x + y.",
              ["1: 3a and 2b are unlike terms, so they cannot be added into 5. It stays 3a + 2b.",
               "2: (3 − 2 − 1)b = 0 × b = 0, so the claim 0 is correct.",
               "3: the 6 multiplies both terms, 6p + 6 × 2 = 6p + 12. The claim 6p + 8 multiplied only the p term "
               "or added 6 and 2.",
               "4: open the bracket: 4x + 3y − 3x − 4y = (4 − 3)x + (3 − 4)y = x − y. The claim x + y did not change "
               "the sign of 4y."],
              "1: 3a + 2b. 2: 0, correct. 3: 6p + 12. 4: x − y", ncert=["4.4.mtm2_a"]),
           WE("Check claims 5 to 8. 5: 5 − (2 − 6z) = 3 − 6z. 6: 2 + (x + 3) = 2x − 6. 7: 2y + (3y − 6) = "
              "−y + 6. 8: 7p − p + 5q − 2q = 7p + 3q.",
              ["5: open the bracket with the minus: 5 − 2 + 6z = 3 + 6z. The claim 3 − 6z did not change the sign "
               "of the second term.",
               "6: the plus bracket opens unchanged, 2 + x + 3 = x + 5. The claim 2x − 6 is not the same.",
               "7: 2y + 3y − 6 = 5y − 6. The claim −y + 6 has the wrong terms and signs.",
               "8: 7p − p = 6p and 5q − 2q = 3q, so the form is 6p + 3q. The claim kept 7p."],
              "5: 3 + 6z. 6: x + 5. 7: 5y − 6. 8: 6p + 3q", ncert=["4.4.mtm2_b"]),
           WE("Check claims 9 to 11, then compare the number of terms with the number of letter-numbers in all the "
              "corrected forms. 9: 5(2w + 3x + 4w) = 10w + 15x + 20w. 10: 3j + 6k + 9h + 12 = "
              "3(j + 2k + 3h + 4). 11: 4(2r + 3s + 5) = −20 − 8r − 12s.",
              ["9: 2w + 4w = 6w, and 5 times (6w + 3x) = 30w + 15x. The claim opened the bracket but did not add the "
               "like terms 10w and 20w.",
               "10: the expression 3j + 6k + 9h + 12 already has no brackets and no like terms, so it is in its "
               "simplest form. The claim writes it with a bracket, which is not simpler.",
               "11: 4 multiplies every term, 4 × 2r + 4 × 3s + 4 × 5 = 8r + 12s + 20. The claim has every sign wrong.",
               "Corrected forms, terms and letters: 3a + 2b has 2 terms and 2 letters; 0 has 1 term and no "
               "letter; 6p + 12 has 2 and 1; x − y has 2 and 2; 3 + 6z has 2 and 1; x + 5 has 2 and 1; 5y − 6 has 2 "
               "and 1; 6p + 3q has 2 and 2; 30w + 15x has 2 and 2; 3j + 6k + 9h + 12 has 4 and 3; 8r + 12s + 20 "
               "has 3 and 2.",
               "In every case the number of letter-numbers is at most the number of terms."],
              "9: 30w + 15x. 10: stays 3j + 6k + 9h + 12. 11: 8r + 12s + 20. The number of letter-numbers is never "
              "more than the number of terms",
              ncert=["4.4.mtm2_c", "4.4.terms_letters"])],
       key_terms=["simplest form", "term", "letter-number"], misconceptions=["M_UNLIKE_ADD"], minutes=16),
     DOER("T8.C4", "Practice: add pictures and simplify", None, "Apply",
          "Students add the numbers in a picture in more than one way, write and simplify the expression, and simplify "
          "a list of expressions with brackets and mixed signs.",
          ["Add in two different ways and see that you get the same thing.",
           "Open brackets carefully, changing signs after a minus.", "Add like terms and add number terms."],
          items=[
              FIO("4.4.FiO_1", "Figure it Out (simplifying), Q1",
                  "Add the numbers in each picture below. Write the corresponding expressions and simplify them. "
                  "Try adding the numbers in each picture in a couple of different ways and see that you get the same "
                  "thing. Picture (i) has two rows of three numbers: the top row is 5y, −6, x and the bottom row is "
                  "x, 2, 5y. Picture (ii) has four copies of 2p, four copies of 3q, and the numbers 3, −2, −2 and "
                  "3. Picture (iii) has four copies of −5g and twelve copies of 5k.",
                  ["(i) Add all the terms: 5y + (−6) + x + x + 2 + 5y. Group like terms: (5y + 5y) + (x + x) + "
                   "(−6 + 2) = 10y + 2x − 4.",
                   "(ii) 2p appears 4 times, giving 8p. 3q appears 4 times, giving 12q. The numbers are 3 + (−2) + "
                   "(−2) + 3 = 2. Total 8p + 12q + 2.",
                   "(iii) −5g appears 4 times, giving −20g. 5k appears 12 times, giving 60k. Total −20g + 60k.",
                   "Adding by rows or by columns gives the same results."],
                  "(i) 10y + 2x − 4 (ii) 8p + 12q + 2 (iii) −20g + 60k"),
              FIO("4.4.FiO_2", "Figure it Out (simplifying), Q2",
                  "Simplify each of the following expressions: (a) p + p + p + p (b) p + p + p + q "
                  "(c) p + q + p − q (d) p − q + p − q (e) p + q − p + q (f) p + q − (p + q) (g) p − q − p − q "
                  "(h) 2d − d − d − d (i) 2d − d − d − c (j) 2d − d − (d − c) (k) 2d − (d − d) − c "
                  "(l) 2d − d − c − c",
                  ["(a) p + p + p + p = 4p.", "(b) p + p + p + q = 3p + q.", "(c) p + q + p − q = 2p + 0 = 2p.",
                   "(d) p − q + p − q = 2p − 2q.", "(e) p + q − p + q = 2q.",
                   "(f) Open the bracket: p + q − p − q = 0.", "(g) p − q − p − q = −2q.",
                   "(h) 2d − d − d − d = −d.", "(i) 2d − d − d − c = −c.",
                   "(j) 2d − d − d + c = c.", "(k) d − d is 0, so 2d − 0 − c = 2d − c.",
                   "(l) 2d − d − c − c = d − 2c."],
                  "(a) 4p (b) 3p + q (c) 2p (d) 2p − 2q (e) 2q (f) 0 (g) −2q (h) −d (i) −c (j) c "
                  "(k) 2d − c (l) d − 2c")],
          ncert=["4.4.FiO_1", "4.4.FiO_2"], misconceptions=["M_BRACKET_SIGN"])]))

# ============================== T9 Number machines ===========================================================
TOPICS.append(TOPIC(
    "T9", "M2", "Number Machines and Formulas", ["4.5"], "Apply",
    "Students find the rule of a number machine from its inputs and outputs, write the rule as an expression in "
    "letter-numbers, check it on each set of inputs, and make a formula of their own.",
    "A number machine applies the same operations to its two inputs every time, so its rule can be written as one "
    "expression in letter-numbers and tested on every set of inputs.",
    [A("T9.C1", "Formula Detective: the machine 2a − b", "Apply",
       "Students study the inputs and outputs of a number machine, say its rule in words, write the rule as an "
       "expression, and check that it works for every set of inputs.",
       textbook=["4.5 Pick Patterns and Reveal Relationships. Remember the importance of describing in simple "
                 "language, or visualising mathematical relationships, before trying to write them as expressions.",
                 "Formula Detective. In each case, the number machine takes in the 2 numbers at the top of the Y as "
                 "inputs, performs some operations and produces the result at the bottom. The machine performs the "
                 "same operations on its inputs in each case. Find out the formula of this number machine.",
                 "The formula for the number machine above is two times the first number minus the second number. "
                 "When written as an algebraic expression, the formula is 2a − b. The expression for the first set "
                 "of inputs is 2 × 5 − 2 = 8. Check that the formula holds true for each set of inputs."],
       teach=["Predict first: the machine turns 5 and 2 into 8, and 8 and 1 into 15. What does it do to the two "
              "inputs? Try your own rule.",
              "Say the rule in words, then write it with a letter-number for each input: two times the first number "
              "minus the second is 2a − b.",
              "Check the rule on every set of inputs."],
       examples=[
           WE("A Y-shaped number machine gives these results: inputs 5 and 2 give 8; 8 and 1 give 15; 9 and 11 give "
              "7; 10 and 10 give 10. Find its formula and check it, including on the inputs 6 and 4.",
              ["Try a rule: two times the first input minus the second.",
               "5 and 2: 2 × 5 − 2 = 10 − 2 = 8. It matches.", "8 and 1: 2 × 8 − 1 = 16 − 1 = 15. It matches.",
               "9 and 11: 2 × 9 − 11 = 18 − 11 = 7. It matches.",
               "10 and 10: 2 × 10 − 10 = 20 − 10 = 10. It matches.",
               "6 and 4: 2 × 6 − 4 = 12 − 4 = 8.",
               "With the first input a and the second input b, the formula is 2a − b."],
              "Two times the first number minus the second, which is 2a − b; the inputs 6 and 4 give 8",
              ncert=["4.5.detective"])],
       key_terms=["formula", "number machine"], minutes=10),
     A("T9.C2", "Finding the formulas of two more machines", "Apply",
       "Students find the rule of two further number machines from several sets of inputs, write each as an "
       "expression in a and b, and write the expression for each set of inputs.",
       textbook=["Find the formulas of the number machines below and write the expression for each set of inputs. "
                 "Machine 1 has inputs (5, 2), (8, 1), (9, 11), (10, 10) and then a and b; the results shown are 5, "
                 "7, 18 and 18. Machine 2 has inputs (4, 1), (6, 0), (3, 2), (10, 3) and then a and b; the results "
                 "shown are 5, 1 and 7."],
       teach=["Predict first: for each machine, find the rule by trying simple operations on the two inputs, such as "
              "sum, difference, product, and then adding or subtracting a number.",
              "Say the rule in words, write it with a and b, and write the expression for every set of inputs."],
       examples=[
           WE("A machine gives: inputs 5 and 2 give 5; 8 and 1 give 7; 9 and 11 give 18; 10 and 10 give 18. Find its "
              "formula, and write the expression for each set of inputs and for a and b.",
              ["Try: add the two inputs and take away 2.", "5 and 2: 5 + 2 − 2 = 5. It matches.",
               "8 and 1: 8 + 1 − 2 = 7. It matches.", "9 and 11: 9 + 11 − 2 = 18. It matches.",
               "10 and 10: 10 + 10 − 2 = 18. It matches.",
               "In words, 2 is subtracted from the sum of the two numbers. For inputs a and b the expression is "
               "a + b − 2."],
              "a + b − 2", ncert=["4.5.machines_1"]),
           WE("A machine gives: inputs 4 and 1 give 5; 6 and 0 give 1; 3 and 2 give 7. Find its formula, then write "
              "the expression for inputs 10 and 3, and for a and b.",
              ["Try: multiply the two inputs and add 1.", "4 and 1: 4 × 1 + 1 = 5. It matches.",
               "6 and 0: 6 × 0 + 1 = 1. It matches.", "3 and 2: 3 × 2 + 1 = 7. It matches.",
               "For 10 and 3: 10 × 3 + 1 = 30 + 1 = 31.",
               "In words, 1 is added to the product of the two numbers. For inputs a and b the expression is "
               "a × b + 1, written ab + 1."],
              "ab + 1, and 31 for the inputs 10 and 3", ncert=["4.5.machines_2"])],
       key_terms=["formula"], minutes=12),
     A("T9.C3", "Make a formula of your own", "Apply",
       "Students invent a rule on two letter-numbers, write number machines for it with several inputs, and "
       "challenge a classmate to find the rule.",
       textbook=["Now, make a formula on your own. Write a few number machines as examples using that formula. "
                 "Challenge your classmates to figure it out!",
                 "Note to the Teacher: Not just solving problems but creating new questions is also very much a part "
                 "of learning and doing mathematics!"],
       teach=["Predict first: what rule would you choose? Keep it a short rule on two inputs.",
              "Compute the outputs for four or five sets of inputs, and show only the inputs and outputs.",
              "A classmate then has to find the rule, say it in words and write the expression."],
       examples=[
           WE("Make a formula of your own with letter-numbers a and b, write four number machines for it, and show "
              "the rule hidden for a classmate to find.",
              ["Choose a rule in words: three times the first number plus the second number. The formula is "
               "3a + b.",
               "Inputs 2 and 5 give 3 × 2 + 5 = 6 + 5 = 11.", "Inputs 4 and 1 give 3 × 4 + 1 = 12 + 1 = 13.",
               "Inputs 0 and 7 give 3 × 0 + 7 = 7.", "Inputs 6 and 6 give 3 × 6 + 6 = 18 + 6 = 24.",
               "Show only the inputs and results, 2 and 5 giving 11, 4 and 1 giving 13, 0 and 7 giving 7, and 6 and "
               "6 giving 24, and ask a classmate for the rule."],
              "Open ended. Model answer: the formula 3a + b gives 11, 13, 7 and 24 for the inputs shown",
              ncert=["4.5.make_own"])],
       key_terms=["formula"], minutes=8),
     DOER("T9.C4", "Practice: read and write a number machine", None, "Apply",
          "Students find a machine's rule from its inputs and outputs, write it as an expression, and use it to find "
          "new outputs.",
          ["Try simple operations on the inputs and check each rule on every set.",
           "Write the rule in words, then as an expression in a and b.",
           "Use the expression for new inputs."])]))
