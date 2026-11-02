# -*- coding: utf-8 -*-
"""Topics T1 to T5 (module M1: letter-numbers and expressions). Book sections 4.1 to 4.3."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Introduction ==============================================================
TOPICS.append(TOPIC(
    "T1", "M1", "One Short Way to Say Every Order", ["Chapter opening", "4.1"], "Understand",
    "",
    "A sweet shop gets a different order every day, and one short rule is wanted that works for any order.",
    [A("T1.C1", "A different order every day", "Remember",
       "",
       textbook=["4 Expressions using Letter-Numbers",
                 "In this chapter we shall look at a concise way of expressing mathematical relations and patterns. "
                 "We shall see how this helps us in thinking about these relationships and patterns, and in "
                 "explaining why they may hold true."],
       teach=["Picture a sweet shop that makes coconut-jaggery laddus. Every day a customer orders a different "
              "number of coconuts and a different weight of jaggery.",
              "Make a guess before the next step: is there one short way to say the cost of any order, so that we "
              "do not work it out from scratch each time?"],
       ncert=["opening"], key_terms=["relation", "pattern"], video_focus=["HOOK"], minutes=4,
       enrichment=True),
     A("T1.C2", "The question to keep: one rule for every order", "Understand", "",
       teach=["Predict: if one day the order is ten coconuts and five kilograms of jaggery, and the next day it is "
              "eight coconuts and nine kilograms, what stays the same between the two bills?",
              "The way the bill is worked out stays the same. Only the numbers of coconuts and kilograms change.",
              "A short way to write that fixed way, with a place holder for the changing numbers, is what this "
              "chapter builds."],
       enrichment=True)],
    topic_type="framing"))

# ============================== T2 A letter-number for a relationship ========================================
TOPICS.append(TOPIC(
    "T2", "M1", "Letter-Numbers for a Relationship", ["4.1"], "Apply",
    "Students write a relationship between two quantities with letter-numbers, such as an age that is 3 more than "
    "another, and use the algebraic expression to find a value. They also write the number of matchsticks for any "
    "number of Ls.",
    "A letter-number stands for a number that can change, and an algebraic expression such as a + 3 or 2 × n gives "
    "the other quantity for every value.",
    [A("T2.C1", "Shabnam and Aftab: an age rule", "Apply",
       "Students write a rule linking two ages with letter-numbers, replace the letter-number by a number to find the "
       "other age, and write the rule in reverse.",
       textbook=["Example 1: Shabnam is 3 years older than Aftab. When Aftab's age is 10 years, Shabnam's age will be "
                 "13 years. Now Aftab's age is 18 years, what will Shabnam's age be?",
                 "Given Aftab's age, how will you find out Shabnam's age? We add 3 to Aftab's age to get Shabnam's "
                 "age. Shabnam's age = Aftab's age + 3.",
                 "Let us say we use the letter a to denote Aftab's age (we could have used any other letter), and s "
                 "to denote Shabnam's age. Then the expression to find Shabnam's age will be a + 3, which can be "
                 "written as s = a + 3.",
                 "Letters such as a and s that are used to represent numbers are called letter-numbers. "
                 "Mathematical expressions containing letter-numbers, such as the expression a + 3, are called "
                 "algebraic expressions.",
                 "Given the age of Shabnam, write an expression to find Aftab's age. Aftab's age is 3 less than "
                 "Shabnam's: a = s − 3, meaning 3 less than s."],
       teach=["Predict first: if Aftab is 18, how old is Shabnam? The same step works for every age, so write it once "
              "with a letter in place of the age.",
              "A letter such as a or s that stands for a number is a letter-number. An expression that has one, such "
              "as a + 3, is an algebraic expression.",
              "The relation can be turned around: if Shabnam's age is s, Aftab's age is s − 3."],
       examples=[
           WE("Shabnam is 3 years older than Aftab. Use a for Aftab's age and s for Shabnam's age, write the "
              "expression for Shabnam's age, and find it when Aftab is 23 years old.",
              ["When Aftab is 4, Shabnam is 4 + 3. When Aftab is 10, Shabnam is 10 + 3. When Aftab is 23, Shabnam is "
               "23 + 3.", "For any age a of Aftab, Shabnam's age is a + 3, so s = a + 3.",
               "Replace a by 23: s = 23 + 3 = 26 years."],
              "s = a + 3, and Shabnam is 26 years old", ncert=["4.1.ex1_s"]),
           WE("Shabnam is 3 years older than Aftab. Write an expression for Aftab's age using s for Shabnam's age, "
              "and find it when Shabnam is 20 years old.",
              ["Aftab is 3 years younger, so his age is 3 less than Shabnam's.", "That gives a = s − 3.",
               "Replace s by 20: a = 20 − 3 = 17 years."],
              "a = s − 3, and Aftab is 17 years old", ncert=["4.1.ex1_a"])],
       key_terms=["letter-number", "algebraic expression"], misconceptions=["M_LETTER_FIXED"], minutes=10),
     A("T2.C2", "Parthiv's matchstick Ls", "Apply",
       "Students count the matchsticks for several numbers of Ls, describe the pattern in words, and write the "
       "expression 2 × n for any number of Ls.",
       textbook=["Example 2: Parthiv is making matchstick patterns. He repeatedly places Ls next to each other. Each "
                 "L has two matchsticks.",
                 "How many matchsticks are needed to make 5 Ls? It will be 5 × 2. 7 Ls? 7 × 2. 45 Ls? 45 × 2.",
                 "Every L needs 2 matchsticks. So the number of matchsticks needed will be 2 times the number of Ls. "
                 "Number of matchsticks = 2 × Number of Ls.",
                 "Now, we can use any letter to denote the number of Ls. Let us use n. The algebraic expression for "
                 "the number of matchsticks will be 2 × n. To find the number of matchsticks, we just replace n by "
                 "the number of Ls."],
       teach=["Predict first: how many matchsticks make 5 Ls? And 45 Ls? Each L takes the same 2 sticks.",
              "Say the pattern in words first: the sticks are 2 times the number of Ls.",
              "Then use a letter-number n for the number of Ls: the expression 2 × n gives the sticks for any n."],
       examples=[
           WE("Each L in Parthiv's pattern uses 2 matchsticks. Find the sticks for 5, 7 and 45 Ls, then write an "
              "expression for n Ls.",
              ["5 Ls need 5 × 2 = 10 matchsticks.", "7 Ls need 7 × 2 = 14 matchsticks.",
               "45 Ls need 45 × 2 = 90 matchsticks.",
               "In words: matchsticks = 2 times the number of Ls. With n for the number of Ls, the expression is "
               "2 × n."],
              "10, 14 and 90 matchsticks, and 2 × n for n Ls", ncert=["4.1.ex2"])],
       key_terms=["letter-number", "pattern"], minutes=8),
     DOER("T2.C3", "Practice: say it with a letter-number", None, "Apply",
          "Students turn a plain-words relationship into an algebraic expression, choose their own letter, and use the "
          "expression for a few values.",
          ["First say the relationship in plain words.", "Then pick a letter for the quantity that can change.",
           "Write the expression, and replace the letter by a number to get a value."])]))

# ============================== T3 Two letter-numbers ========================================================
TOPICS.append(TOPIC(
    "T3", "M1", "Expressions with Two Letter-Numbers", ["4.1"], "Apply",
    "Students find a total cost for given quantities, write the expression for any quantities with two "
    "letter-numbers, read it as a sum of terms, and write formulas for the perimeter of regular shapes.",
    "A total made of two parts gives an expression with two letter-numbers; its value changes with the numbers "
    "used, and such a general relation is called a formula.",
    [A("T3.C1", "Ketaki's laddu order", "Apply",
       "Students find the cost of one order, write the expression c × 35 + j × 60 for any order, and evaluate it for "
       "new quantities, reading it as a sum of two terms.",
       textbook=["Example 3: Ketaki prepares and supplies coconut-jaggery laddus. The price of a coconut is ₹35 and "
                 "the price of 1 kg jaggery is ₹60. How much should she pay if she buys 10 coconuts and 5 kg "
                 "jaggery?",
                 "Total cost = 10 × 35 + 5 × 60 = 350 + 300 = 650 rupees.",
                 "Write an algebraic expression to find the total amount to be paid for a given number of coconuts "
                 "and quantity of jaggery.",
                 "Cost of coconuts is the number of coconuts × 35, written c × 35. Cost of jaggery is the number of "
                 "kg of jaggery × 60, written j × 60.",
                 "The total amount is the cost of coconuts + the cost of jaggery: c × 35 + j × 60.",
                 "Notice that for different values of c and j, the value of the expression also changes. Writing "
                 "this expression as a sum of terms gives the terms c × 35 and j × 60."],
       teach=["Predict first: for 10 coconuts and 5 kg of jaggery, what is each part of the bill, and what is the "
              "total?",
              "Name the quantities that change: c for the number of coconuts and j for the kilograms of jaggery.",
              "The expression c × 35 + j × 60 is a sum of two terms, c × 35 and j × 60. Different c and j give "
              "different values."],
       examples=[
           WE("Coconuts cost 35 rupees each and jaggery costs 60 rupees per kg. Find the total to pay for 10 "
              "coconuts and 5 kg of jaggery.",
              ["Cost of 10 coconuts = 10 × 35 = 350.", "Cost of 5 kg jaggery = 5 × 60 = 300.",
               "Total cost = 350 + 300 = 650 rupees."],
              "650 rupees", ncert=["4.1.ex3_a"]),
           WE("Write an expression for the total to pay for c coconuts and j kg of jaggery, then use it for 8 coconuts "
              "and 9 kg of jaggery.",
              ["Cost of coconuts = c × 35. Cost of jaggery = j × 60.", "Total = c × 35 + j × 60.",
               "Replace c by 8 and j by 9: 8 × 35 + 9 × 60 = 280 + 540 = 820 rupees."],
              "c × 35 + j × 60, and 820 rupees", ncert=["4.1.ex3_b"]),
           WE("Use the expression c × 35 + j × 60 for 7 coconuts and 4 kg of jaggery, and name its two terms.",
              ["Replace c by 7 and j by 4: 7 × 35 + 4 × 60 = 245 + 240 = 485 rupees.",
               "The two terms are c × 35 and j × 60.",
               "A different c or j gives a different value, so the value of the expression changes."],
              "485 rupees; the terms are c × 35 and j × 60", ncert=["4.1.ex3_c"])],
       key_terms=["expression", "term", "formula"], misconceptions=["M_LETTER_FIXED"], minutes=12),
     A("T3.C2", "Perimeters as formulas", "Apply",
       "Students write the perimeter of a square as 4 × q, evaluate it for a given side, and name a general relation "
       "written with letter-numbers a formula.",
       textbook=["Example 4: We are familiar with calculating the perimeters of simple shapes. Write expressions for "
                 "perimeters.",
                 "The perimeter of a square is 4 times the length of its side. This can be written as the "
                 "expression 4 × q, where q stands for the side length. What is the perimeter of a square with "
                 "side length 7 cm? Use the expression to find out.",
                 "You must have realised how the use of letter-numbers and algebraic expressions allows us to "
                 "express general mathematical relations in a concise way. Mathematical relations expressed this "
                 "way are often called formulas."],
       teach=["Predict first: what is the perimeter of a square of side 7 cm? What do you do with the side?",
              "The side can be any length, so call it q. The perimeter is 4 times q, written 4 × q.",
              "A relation written this way, true for every value, is called a formula."],
       examples=[
           WE("Write an expression for the perimeter of a square with side q, and use it for a side of 7 cm.",
              ["A square has 4 equal sides, so the perimeter is 4 times the side.", "The expression is 4 × q.",
               "Replace q by 7: 4 × 7 = 28 cm."],
              "4 × q, and 28 cm", ncert=["4.1.ex4"])],
       key_terms=["formula", "perimeter"], minutes=8),
     DOER("T3.C3", "Practice: words to expressions", "words_assembler", "Apply",
          "Students turn a situation told in words into an expression by naming the changing quantities, writing each "
          "part, and joining the parts, then check it with a few numbers.",
          ["Name the quantities that change with letters.", "Write each part of the situation as a term.",
           "Join the terms with the right operations, and test with numbers."],
          items=[
              FIO("4.1.FiO_1", "Figure it Out (expressions), Q1",
                  "Write formulas for the perimeter of: (a) a triangle with all sides equal. (b) a regular pentagon "
                  "(a regular figure has all side lengths and all angles equal). (c) a regular hexagon.",
                  ["Let each side have length a.", "(a) A triangle has 3 equal sides, so the perimeter is 3 × a = 3a.",
                   "(b) A regular pentagon has 5 equal sides, so the perimeter is 5a.",
                   "(c) A regular hexagon has 6 equal sides, so the perimeter is 6a."],
                  "(a) 3a (b) 5a (c) 6a", tool="words_assembler"),
              FIO("4.1.FiO_2", "Figure it Out (expressions), Q2",
                  "Munirathna has a 20 m long pipe. He wants a longer watering pipe for his garden, so he joins "
                  "another pipe of some length to this one. Give the expression for the combined length of the "
                  "pipe. Use the letter-number k to denote the length in metres of the other pipe.",
                  ["The combined length is the 20 m pipe plus the other pipe.", "The other pipe is k metres long.",
                   "So the combined length is 20 + k metres."],
                  "(20 + k) metres", tool="words_assembler"),
              FIO("4.1.FiO_3", "Figure it Out (expressions), Q3",
                  "What is the total amount Krithika has, if she has the following numbers of notes of 100, 20 and "
                  "5 rupees? Complete the table, where each row gives the number of 100 rupee notes, the number of "
                  "20 rupee notes and the number of 5 rupee notes: row 1 is 3, 5 and 6 notes. Row 2 is 6, 4 and 3 "
                  "notes (already worked: 6 × 100 + 4 × 20 + 3 × 5 = 695). Row 3 is 8 notes of 100, 4 notes of 20 "
                  "and z notes of 5. Row 4 is x notes of 100, y notes of 20 and z notes of 5.",
                  ["Each total is (notes of 100) × 100 + (notes of 20) × 20 + (notes of 5) × 5.",
                   "Row 1: 3 × 100 + 5 × 20 + 6 × 5 = 300 + 100 + 30 = 430.",
                   "Row 2: 6 × 100 + 4 × 20 + 3 × 5 = 600 + 80 + 15 = 695.",
                   "Row 3: 8 × 100 + 4 × 20 + z × 5 = 800 + 80 + 5z = 880 + 5z.",
                   "Row 4: x × 100 + y × 20 + z × 5 = 100x + 20y + 5z."],
                  "Row 1: 430. Row 2: 695. Row 3: 880 + 5z. Row 4: 100x + 20y + 5z", tool="words_assembler"),
              FIO("4.1.FiO_4", "Figure it Out (expressions), Q4",
                  "Venkatalakshmi owns a flour mill. It takes 10 seconds for the roller mill to start running. Once "
                  "it is running, each kg of grain takes 8 seconds to grind into powder. Which of the expressions "
                  "below describes the time taken to grind y kg of grain, assuming the machine is off initially? "
                  "(a) 10 + 8 + y (b) (10 + 8) × y (c) 10 × 8 × y (d) 10 + 8 × y (e) 10 × y + 8",
                  ["The machine first takes 10 seconds to start, once.", "Then each of the y kg takes 8 seconds, "
                   "so grinding takes 8 × y seconds.", "Total time = 10 + 8 × y.",
                   "Check with y = 3: 10 + 8 × 3 = 34 seconds, which is 10 to start and 24 to grind.",
                   "Option (d) is the match."],
                  "(d) 10 + 8 × y", tool="words_assembler"),
              FIO("4.1.FiO_5", "Figure it Out (expressions), Q5",
                  "Write algebraic expressions using letters of your choice. (a) 5 more than a number. (b) 4 less "
                  "than a number. (c) 2 less than 13 times a number. (d) 13 less than 2 times a number.",
                  ["Let the letter d stand for the number.", "(a) 5 more than d is d + 5.",
                   "(b) 4 less than d is d − 4.", "(c) 13 times d is 13 × d, and 2 less than that is 13d − 2.",
                   "(d) 2 times d is 2 × d, and 13 less than that is 2d − 13."],
                  "(a) d + 5 (b) d − 4 (c) 13d − 2 (d) 2d − 13", tool="words_assembler"),
              FIO("4.1.FiO_6", "Figure it Out (expressions), Q6",
                  "Describe situations corresponding to the following algebraic expressions: (a) 8 × x + 3 × y "
                  "(b) 15 × j − 2 × k",
                  ["(a) Think of two things bought in different numbers: 8 of one and 3 of the other. A shopkeeper "
                   "sells a pen for x rupees and a notebook for y rupees. Abha buys 8 pens and 3 notebooks. Her "
                   "total cost is 8 × x + 3 × y.",
                   "(b) Think of 15 of something made each day and 2 taken away each time. A factory makes 15 "
                   "chairs every day, so it makes 15 × j chairs in j days. Then 2 chairs are spoiled on each of k "
                   "days, which removes 2 × k chairs. The good chairs left are 15 × j − 2 × k.",
                   "Many other situations work. Try your own."],
                  "Open ended. Model answers: (a) 8 pens at x rupees and 3 notebooks at y rupees; (b) 15 chairs "
                  "made in each of j days, 2 spoiled on each of k days"),
              FIO("4.1.FiO_7", "Figure it Out (expressions), Q7",
                  "In a calendar month, a 2 by 3 grid full of dates is chosen: 2 rows and 3 columns. Write "
                  "expressions for the dates in the blank cells if the bottom middle cell has date w.",
                  ["In a calendar the date to the right is 1 more and the date to the left is 1 less.",
                   "The date in the row above is 7 less, because each week is 7 days.",
                   "Bottom row: w − 1, w, w + 1.", "Top row: w − 8, w − 7, w − 6."],
                  "Top row: w − 8, w − 7, w − 6. Bottom row: w − 1, w, w + 1")],
          ncert=["4.1.FiO_1", "4.1.FiO_2", "4.1.FiO_3", "4.1.FiO_4", "4.1.FiO_5", "4.1.FiO_6", "4.1.FiO_7"],
          misconceptions=["M_JOIN_DIGITS"])]))

# ============================== T4 Revisiting arithmetic expressions =========================================
TOPICS.append(TOPIC(
    "T4", "M1", "Revisiting Arithmetic Expressions", ["4.2"], "Apply",
    "Students read an arithmetic expression as a sum of terms, evaluate it using swapping and grouping, handle "
    "brackets with a negative sign outside, and note that algebraic expressions also take number values.",
    "An expression is read as a sum of terms; terms may be swapped and grouped, and brackets with a minus sign "
    "can be solved first or opened.",
    [A("T4.C1", "Evaluating expressions term by term", "Apply",
       "Students evaluate seven arithmetic expressions by writing their terms, converting each term to a number, "
       "using swapping and grouping, and opening brackets that have a minus sign outside.",
       textbook=["We learnt to write expressions as sums of terms and it became easy for us to read arithmetic "
                 "expressions. We used swapping and grouping to find easy ways of evaluating expressions. Swapping "
                 "and grouping terms does not change the value of the expression. We also learnt to use brackets "
                 "in expressions, including brackets with a negative sign outside.",
                 "Let us revise these concepts and find the values of: 1. 23 − 10 × 2. 2. 83 + 28 − 13 + 32. "
                 "3. 34 − 14 + 20. 4. 42 + 15 − (8 − 7). 5. 68 − (18 + 13). 6. 7 × 4 + 9 × 6. 7. 20 + 8 × (16 − 6).",
                 "23 − 10 × 2 = 23 + (−10 × 2) = 23 + (−20) = 3.",
                 "Algebraic expressions also take number values when the letter-numbers they contain are replaced "
                 "by numbers. In Example 1 we replaced the letter-number a in a + 3 by 23, and it took the value 26."],
       teach=["Predict first: in 23 − 10 × 2, which part is worked out first? Is the answer 26 or 3?",
              "Write the terms: 23 and −10 × 2. Turn each term into a number, then add.",
              "Swap and group the terms to make adding easy, for example pairing numbers that make a round total.",
              "A bracket with a minus outside can be solved first, or opened by changing the sign of every term inside.",
              "An algebraic expression takes a number value when its letter-numbers are replaced by numbers."],
       examples=[
           WE("Evaluate 23 − 10 × 2, then 7 × 4 + 9 × 6, then 20 + 8 × (16 − 6).",
              ["23 − 10 × 2 = 23 + (−10 × 2) = 23 + (−20) = 3.", "7 × 4 + 9 × 6 = 28 + 54 = 82.",
               "In 20 + 8 × (16 − 6), the bracket first: 16 − 6 = 10, so 20 + 8 × 10 = 20 + 80 = 100."],
              "3, 82 and 100", ncert=["4.2.arith_a"]),
           WE("Evaluate 83 + 28 − 13 + 32 by swapping and grouping, and then 34 − 14 + 20.",
              ["Write the terms: 83, 28, −13 and 32.", "Swap and group: (83 − 13) + (28 + 32) = 70 + 60 = 130.",
               "34 − 14 + 20: the terms are 34, −14 and 20, so 34 − 14 + 20 = 20 + 20 = 40."],
              "130 and 40", ncert=["4.2.arith_b"]),
           WE("Evaluate 42 + 15 − (8 − 7), and 68 − (18 + 13) in two ways.",
              ["42 + 15 − (8 − 7): the bracket is 8 − 7 = 1, so 42 + 15 − 1 = 56.",
               "68 − (18 + 13), way one: the bracket is 31, so 68 − 31 = 37.",
               "Way two: open the bracket and change both signs, 68 − 18 − 13 = 50 − 13 = 37.",
               "Both ways give the same value."],
              "56 and 37", ncert=["4.2.arith_c"])],
       ncert=["4.2.value"], key_terms=["term", "swapping", "grouping", "bracket"],
       misconceptions=["M_ORDER_OPS"], minutes=12),
     DOER("T4.C2", "Practice: evaluate by terms", None, "Apply",
          "Students evaluate arithmetic expressions with brackets and mixed signs by listing terms, swapping and "
          "grouping, and checking the value by solving the bracket first.",
          ["List the terms with their signs.", "Swap and group to add easily.",
           "For a minus bracket, solve it first or open it, and check both ways."])]))

# ============================== T5 Dropping the multiplication sign ==========================================
TOPICS.append(TOPIC(
    "T5", "M1", "Dropping the Multiplication Sign", ["4.3"], "Apply",
    "Students describe a sequence by its nth term, write 4 × n as 4n, evaluate expressions such as 7k and 5m + 3 "
    "for given values, and find and mend slips made when replacing letter-numbers by numbers.",
    "The multiplication sign is dropped between a number and a letter-number, so 4n means 4 × n; evaluating "
    "replaces the letter by its number, with care for brackets and signs.",
    [A("T5.C1", "The nth term of a sequence", "Apply",
       "Students describe a sequence of multiples, find its third and 29th terms, and write the nth term as 4n by "
       "skipping the multiplication sign.",
       textbook=["Look at this number sequence: 4, 8, 12, 16, 20, 24, 28, ... How can we describe this sequence "
                 "or pattern? These are the numbers appearing in the multiplication table of 4.",
                 "What is the third term of this sequence? It is 4 × 3. What is the 29th term? It is 4 × 29.",
                 "Find an algebraic expression to get the nth term of this sequence. Note that here n is a "
                 "letter-number that denotes a position in the sequence.",
                 "As it is the sequence of multiples of 4, the nth term will be 4 times n: 4 × n. As a standard "
                 "practice, we shorten 4 × n to 4n by skipping the multiplication sign. We write the number first, "
                 "followed by the letter(s)."],
       teach=["Predict first: what is the 10th term of 4, 8, 12, 16, ...? How did you get it?",
              "The 3rd term is 4 × 3 and the 29th term is 4 × 29. The position times 4 gives the term.",
              "With n for the position, the nth term is 4 × n, shortened to 4n. The number is written first, then "
              "the letter."],
       examples=[
           WE("In the sequence 4, 8, 12, 16, 20, 24, 28, ... find the third term and the 29th term, then write the "
              "nth term.",
              ["The terms are the multiples of 4, so the term at a position is 4 times that position.",
               "Third term = 4 × 3 = 12.", "29th term = 4 × 29 = 116.", "nth term = 4 × n, which is written 4n."],
              "12, 116, and 4n", ncert=["4.3.nth"])],
       key_terms=["term", "nth term", "sequence"], minutes=8),
     A("T5.C2", "Values of 7k and 5m + 3", "Apply",
       "Students find the value of 7k when k is 4 and of 5m + 3 when m is 2, reading 7k as 7 × k and following the "
       "usual order of operations.",
       textbook=["Find the value of the expression 7k when k = 4. The value is 7 × 4 = 28.",
                 "Find the value that the expression 5m + 3 takes when m = 2. As 5m stands for 5 × m, the value of "
                 "the expression when m = 2 is 5 × 2 + 3 = 13."],
       teach=["Predict first: if k is 4, is 7k equal to 74 or to 28?",
              "7k means 7 × k. Put the number in the letter's place and multiply.",
              "In 5m + 3, the 5m is multiplied first and then 3 is added."],
       examples=[
           WE("Find the value of 7k when k = 4.",
              ["7k stands for 7 × k.", "Replace k by 4: 7 × 4 = 28."], "28", ncert=["4.3.value_a"],
),
           WE("Find the value that 5m + 3 takes when m = 2.",
              ["5m stands for 5 × m, so 5m + 3 is 5 × m + 3.", "Replace m by 2: 5 × 2 + 3 = 10 + 3 = 13."],
              "13", ncert=["4.3.value_b"])],
       key_terms=["value of an expression"], misconceptions=["M_JOIN_DIGITS"], minutes=8),
     A("T5.C3", "Mind the Mistake, Mend the Mistake: replacing letters", "Apply",
       "Students check nine claimed values, spot the slip in each wrong one, say what might have gone wrong, and "
       "give the correct value, including with negative values and brackets.",
       textbook=["Some simplifications are shown below where the letter-numbers are replaced by numbers and the "
                 "value of the expression is obtained. Observe each of them and identify if there is a mistake. If "
                 "you think there is a mistake, try to explain what might have gone wrong. Then, correct it and "
                 "give the value of the expression.",
                 "1. If a = −4, then 10 − a = 6. 2. If d = 6, then 3d = 36. 3. If s = 7, then 3s − 2 = 15. "
                 "4. If r = 8, then 2r + 1 = 29. 5. If j = 5, then 2j = 10. 6. If m = −6, then 3(m + 1) = 19. "
                 "7. If f = 3 and g = 1, then 2f − 2g = 2. 8. If t = 4 and b = 3, then 2t + b = 24. "
                 "9. If h = 5 and n = 6, then h − (3 − n) = 4."],
       teach=["Predict first: for each claim, replace the letter and work it out yourself before you read the claimed "
              "value.",
              "Then compare. If the values differ, ask what slip could give the claimed value: a lost sign, digits "
              "joined side by side, or the wrong order of operations.",
              "Write the corrected value."],
       examples=[
           WE("Check these claims. 1: if a = −4, then 10 − a = 6. 2: if d = 6, then 3d = 36. 3: if s = 7, then "
              "3s − 2 = 15.",
              ["1: 10 − a with a = −4 is 10 − (−4) = 10 + 4 = 14. The claim 6 likely comes from ignoring the "
               "negative sign of a. The value is 14.",
               "2: 3d is 3 × d = 3 × 6 = 18. The claim 36 likely joins the digits 3 and 6. The value is 18.",
               "3: 3s − 2 is 3 × 7 − 2 = 21 − 2 = 19. The claim 15 likely takes 7 − 2 first and then multiplies "
               "by 3. The value is 19."],
              "1: 14. 2: 18. 3: 19. All three claims are wrong", ncert=["4.3.mtm1_a"],
),
           WE("Check these claims. 4: if r = 8, then 2r + 1 = 29. 5: if j = 5, then 2j = 10. 6: if m = −6, then "
              "3(m + 1) = 19.",
              ["4: 2r + 1 is 2 × 8 + 1 = 16 + 1 = 17. The claim 29 likely joins 2 and 8 into 28 and adds 1. "
               "The value is 17.", "5: 2j is 2 × 5 = 10. The claim is correct.",
               "6: 3(m + 1) with m = −6 is 3 × (−6 + 1) = 3 × (−5) = −15. The claim 19 is wrong, likely from "
               "dropping the signs and the bracket. The value is −15."],
              "4: 17. 5: correct, 10. 6: −15", ncert=["4.3.mtm1_b"],
),
           WE("Check these claims. 7: if f = 3 and g = 1, then 2f − 2g = 2. 8: if t = 4 and b = 3, then "
              "2t + b = 24. 9: if h = 5 and n = 6, then h − (3 − n) = 4.",
              ["7: 2f − 2g is 2 × 3 − 2 × 1 = 6 − 2 = 4. The claim 2 likely subtracts the numbers 3 and 1 before "
               "multiplying. The value is 4.",
               "8: 2t + b is 2 × 4 + 3 = 8 + 3 = 11. The claim 24 likely joins 2 and 4 into 24 and forgets b. "
               "The value is 11.",
               "9: h − (3 − n) is 5 − (3 − 6) = 5 − (−3) = 5 + 3 = 8. The claim 4 likely drops the sign of the "
               "bracket. The value is 8."],
              "7: 4. 8: 11. 9: 8", ncert=["4.3.mtm1_c"],
)],
       key_terms=["substitute", "value of an expression"], misconceptions=["M_SIGN_VALUE"], minutes=14),
     DOER("T5.C4", "Practice: replace and evaluate", "letter_slot_loader", "Apply",
          "Students replace each letter-number in an expression by a given number, write the product when a number "
          "and a letter sit together, and evaluate carefully with negative numbers and brackets.",
          ["A number written next to a letter means multiplication.",
           "Replace each letter by its number, keeping the sign, and put brackets round a negative number.",
           "Then follow the usual order of operations."])]))
