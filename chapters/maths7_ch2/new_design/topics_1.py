# -*- coding: utf-8 -*-
"""Topics T1 to T4 (module M1 and the start of M2): simple expressions, comparing them, terms and order of work."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Introduction ==============================================================
TOPICS.append(TOPIC(
    "T1", "M1", "A Week of Lunch Money", ["Chapter opening", "2.1"], "Understand",
    "",
    "A child spends the same amount on lunch each school day, and the question is how to write the total, and whether "
    "there is more than one way to write it.",
    [A("T1.C1", "Lunch money for five school days", "Remember",
       "",
       textbook=["Arithmetic Expressions",
                 "We have been reading and evaluating simple expressions for some time now.",
                 "Meera spends ₹25 every day for lunch at school. Write an expression for the amount she spends in 5 "
                 "days."],
       teach=["Picture a child paying for lunch at the school canteen, the same amount on each of five days.",
              "Make a guess before the next step: how could you write the total she spends in a way that someone "
              "else could read at a glance?"],
       ncert=["opening"], key_terms=["expression"], video_focus=["HOOK"], minutes=4, enrichment=True),
     A("T1.C2", "The question to keep: how can the total be written", "Understand", "",
       teach=["Predict: if the same amount is spent each day, is the total a sum, a product or both?",
              "A mathematical sentence made of numbers and operations is an expression, and the number it works out "
              "to is its value.",
              "Keep this in mind: the next topic writes the lunch money as an expression and finds its value."],
       enrichment=True)],
    topic_type="framing"))

# ============================== T2 Simple expressions ========================================================
TOPICS.append(TOPIC(
    "T2", "M1", "Expressions and Their Values", ["2.1"], "Apply",
    "Students write an expression for a simple situation, find its value, show that one value can have many "
    "different expressions, and compare two expressions by working out each value and using the signs for less than, "
    "greater than and equal.",
    "An expression is built from numbers and operations; its value is the number it works out to, and different "
    "expressions can have the same value.",
    [A("T2.C1", "Writing an expression and finding its value", "Apply",
       "Students write a repeated spend as an expression with a times sign, work it out to get its value, and then "
       "write several different expressions that share one value.",
       textbook=["Meera spends ₹25 every day for lunch at school. Write an expression for the amount she spends in 5 "
                 "days. Also find its value.",
                 "The value of this expression is 125. We write 5 × 25 = 125.",
                 "Many different expressions can have the same value. Choose a favourite number and write as many "
                 "different expressions for it as you can."],
       teach=["Predict first: Meera pays the same amount on each of 5 days. Will you add or multiply to get the total?",
              "Writing the same amount five times and adding is 25 + 25 + 25 + 25 + 25, which is the same as 5 × 25.",
              "The number an expression works out to is its value, and the equals sign joins an expression to its "
              "value.",
              "Different expressions can have one value: 12 can be written as 10 + 2, 15 − 3, 3 × 4 or 24 ÷ 2."],
       examples=[
           WE("Meera spends ₹25 every day for lunch at school. Write an expression for what she spends in 5 days and "
              "find its value.",
              ["Each day she spends 25, and there are 5 days.", "Five lots of 25 give the expression 5 × 25.",
               "Working out: 5 × 25 = 125."],
              "The expression is 5 × 25 and its value is ₹125", ncert=["2.1.ex1"], fact="ex1", expect=[125]),
           WE("Write four different expressions whose value is 12, and one more for a favourite number of your own.",
              ["10 + 2 = 12, adding.", "15 − 3 = 12, taking away.", "3 × 4 = 12, multiplying.",
               "24 ÷ 2 = 12, sharing.",
               "For a favourite number such as 20: 15 + 5, 25 − 5, 4 × 5 and 40 ÷ 2 all have the value 20."],
              "10 + 2, 15 − 3, 3 × 4 and 24 ÷ 2 all have the value 12", ncert=["2.1.same_value", "2.1.favourite"],
              fact="same_value", expect=[12, 20])],
       key_terms=["expression", "value"], misconceptions=["M_EQUALS_ANSWER"], minutes=10),
     A("T2.C2", "Comparing expressions by their values", "Apply",
       "Students work out the values of two expressions and use the signs for less than, greater than or equal to "
       "to say which is larger.",
       textbook=["We can compare two expressions by working out their values. 10 + 2 is greater than 7 + 1, and "
                 "13 − 2 is less than 4 × 3."],
       teach=["Predict first: is 10 + 2 greater or smaller than 7 + 1? Check by working each one out.",
              "Work out each expression to its value, then compare the two values.",
              "Use the signs > for greater than, < for less than, and = when the two values are the same."],
       examples=[
           WE("Compare 10 + 2 with 7 + 1, and 13 − 2 with 4 × 3, using <, > or =.",
              ["10 + 2 = 12 and 7 + 1 = 8. Since 12 is more than 8, 10 + 2 > 7 + 1.",
               "13 − 2 = 11 and 4 × 3 = 12. Since 11 is less than 12, 13 − 2 < 4 × 3."],
              "10 + 2 > 7 + 1 and 13 − 2 < 4 × 3", ncert=["2.1.compare"], fact="compare", expect=[12, 8, 11, 12])],
       key_terms=["value", "greater than", "less than"], misconceptions=["M_BIGGER_NUMBERS"], minutes=8),
     DOER("T2.C3", "Practice: make both sides equal and put them in order", None, "Apply",
          "Students fill in missing numbers so that both sides of an equals sign have the same value, and arrange "
          "several expressions in order of their values.",
          ["Work out the side that has no blank first, then find what the blank must be.",
           "To put expressions in order, find each value and then compare the values.",
           "The two sides of an equals sign need the same value, not the same look."],
          items=[
              FIO("2.1.FiO1", "Figure it Out, Q1",
                  "Fill in the blanks to make the expressions equal on both sides of the = sign: "
                  "(a) 13 + 4 = ____ + 6 (b) 22 + ____ = 6 × 5 (c) 8 × ____ = 64 ÷ 2 (d) 34 − ____ = 25",
                  ["(a) 13 + 4 = 17, and 17 = 11 + 6, so the blank is 11.",
                   "(b) 6 × 5 = 30, and 22 + 8 = 30, so the blank is 8.",
                   "(c) 64 ÷ 2 = 32, and 8 × 4 = 32, so the blank is 4.",
                   "(d) 34 − 9 = 25, so the blank is 9."],
                  "(a) 11 (b) 8 (c) 4 (d) 9", expect=[11, 8, 4, 9]),
              FIO("2.1.FiO2", "Figure it Out, Q2",
                  "Arrange the following expressions in ascending (increasing) order of their values. "
                  "(a) 67 − 19 (b) 67 − 20 (c) 35 + 25 (d) 5 × 11 (e) 120 ÷ 3",
                  ["Find each value: 67 − 19 = 48, 67 − 20 = 47, 35 + 25 = 60, 5 × 11 = 55, 120 ÷ 3 = 40.",
                   "In increasing order the values are 40, 47, 48, 55, 60.",
                   "So the expressions in order are 120 ÷ 3, 67 − 20, 67 − 19, 5 × 11, 35 + 25."],
                  "(e), (b), (a), (d), (c), that is 120 ÷ 3 < 67 − 20 < 67 − 19 < 5 × 11 < 35 + 25",
                  expect=[40, 47, 48, 55, 60])],
          ncert=["2.1.FiO1", "2.1.FiO2"], misconceptions=["M_EQUALS_ANSWER"])]))

# ============================== T3 Comparing by reasoning ====================================================
TOPICS.append(TOPIC(
    "T3", "M1", "Comparing Without Working Out", ["2.1"], "Analyze",
    "Students compare two sums or two differences by asking how far each number has moved from the other "
    "expression, without finding either value, and say when the two expressions end up equal.",
    "Comparing two expressions can be done by reasoning about how their numbers differ, which often saves long "
    "calculations.",
    [A("T3.C1", "Which is greater: imagine a situation", "Analyze",
       "Students compare two sums such as 1023 + 125 and 1022 + 128 by imagining a situation and tracking how much "
       "more each side starts with and gains, without finding either value.",
       textbook=["Which is greater? 1023 + 125 or 1022 + 128?",
                 "Imagining a situation could help us answer this without finding the values. Raja had 1023 marbles "
                 "and got 125 more today. Joy had 1022 marbles and got 128 more today. Who has more?"],
       teach=["Predict first: 1023 + 125 or 1022 + 128. One starts bigger, the other gains more. Which wins?",
              "Imagine two children with marbles. One starts with 1 more marble, but the other gains 3 more.",
              "Count the gap: the first start is 1 ahead, then the second gains 3 more, so the second ends 2 ahead.",
              "So the comparison needs only the small gaps, not the large totals."],
       examples=[
           WE("Which is greater, 1023 + 125 or 1022 + 128? Answer without working out either total.",
              ["Imagine Kabir has 1023 marbles and gets 125 more, and Farhan has 1022 and gets 128 more.",
               "To begin with, Kabir has 1 more marble than Farhan.",
               "But Farhan gets 128 − 125 = 3 more marbles than Kabir today.",
               "So Farhan ends with 3 − 1 = 2 more marbles than Kabir.",
               "That is, 1023 + 125 < 1022 + 128."],
              "1022 + 128 is greater by 2, so 1023 + 125 < 1022 + 128", ncert=["2.1.ex2"], fact="ex2",
              expect=[1148, 1150, 2]),
           WE("Which is greater, 113 − 25 or 112 − 24? Answer without working out either difference.",
              ["Imagine Kabir has 113 marbles and loses 25, and Farhan has 112 and loses 24.",
               "Kabir starts with 1 more marble than Farhan.",
               "But Kabir also loses 1 more marble than Farhan.",
               "The extra 1 he started with is cancelled by the extra 1 he loses, so they are left with the same.",
               "That is, 113 − 25 = 112 − 24."],
              "The two are equal: 113 − 25 = 112 − 24", ncert=["2.1.ex3"], fact="ex3", expect=[88, 88])],
       key_terms=["expression", "compare"], misconceptions=["M_EVALUATE_TO_COMPARE", "M_BIGGER_NUMBERS"], minutes=10),
     A("T3.C2", "Compare five pairs by reasoning", "Analyze",
       "Students decide whether each pair of sums or differences is less than, equal to or greater than the other "
       "by reasoning about the gaps in the numbers, and say why no long calculation is needed.",
       textbook=["Compare the following pairs of expressions using <, > or =. Can you do it without complicated "
                 "calculations? Explain.",
                 "(a) 245 + 289 and 246 + 285 (b) 273 − 145 and 272 − 144 (c) 364 + 587 and 363 + 589 "
                 "(d) 124 + 245 and 129 + 245 (e) 213 − 77 and 214 − 76"],
       teach=["Predict first: look at 273 − 145 and 272 − 144. Both numbers moved down by 1. Do you expect a change?",
              "In a sum, a number that moves up by 1 while the other moves down by 1 keeps the total the same.",
              "In a difference, if both numbers move by the same amount in the same direction, the difference "
              "stays the same.",
              "Ask how much each number moved, and in which direction, before touching a calculator."],
       examples=[
           WE("Compare using <, > or =, by reasoning: (a) 245 + 289 and 246 + 285 (b) 273 − 145 and 272 − 144 "
              "(c) 364 + 587 and 363 + 589 (d) 124 + 245 and 129 + 245 (e) 213 − 77 and 214 − 76.",
              ["(a) The first number goes up by 1 but the second goes down by 4, so the sum falls by 3: "
               "245 + 289 > 246 + 285.",
               "(b) Both numbers are 1 less, so the difference is unchanged: 273 − 145 = 272 − 144.",
               "(c) The first number is 1 less and the second is 2 more, so the sum rises by 1: "
               "364 + 587 < 363 + 589.",
               "(d) One number is 5 more and the other is the same, so 124 + 245 < 129 + 245.",
               "(e) The first number goes up by 1 and the second goes down by 1, so the difference goes up by 2: "
               "213 − 77 < 214 − 76."],
              "(a) > (b) = (c) < (d) < (e) <", ncert=["2.1.compare5"], fact="compare5",
              expect=[534, 531, 128, 128, 951, 952, 369, 374, 136, 138])],
       key_terms=["compare"], misconceptions=["M_EVALUATE_TO_COMPARE"], minutes=10),
     DOER("T3.C3", "Practice: judge the gap and compare", "gap_comparer", "Analyze",
          "Students compare pairs of sums and differences by judging how each number changed, and decide whether the "
          "first side is less than, equal to or greater than the second without working either out.",
          ["Look at how each number moved, and by how much.",
           "In a sum, a rise on one side can be paid back by a fall on the other.",
           "In a difference, moving both numbers the same way leaves it unchanged."])]))

# ============================== T4 Terms and order of work ===================================================
TOPICS.append(TOPIC(
    "T4", "M2", "Reading Expressions: Terms and Order", ["2.2"], "Apply",
    "Students use brackets to fix the order of work in an expression with more than one operation, write an "
    "expression as a sum of terms by treating a subtraction as adding a negative number, and evaluate by terms.",
    "Brackets and terms say what to work out first; an expression is a sum of terms, and each term is worked out "
    "before the terms are added.",
    [A("T4.C1", "Why we need rules: the order of work", "Apply",
       "Students see that an expression with a plus and a times can be read two ways, work out the times part "
       "first, and use a bracket when a different order is meant.",
       textbook=["Reading and Evaluating Complex Expressions",
                 "Shalini sat next to a friend with toys. Shalini, sat next to a friend, with toys. Where a comma "
                 "goes changes the meaning.",
                 "Mallesh brought 30 marbles to the playground. Arun gave him 5 bags with 4 marbles in each bag. "
                 "How many marbles does Mallesh have now? Purna says 140 and Mallesh says 50.",
                 "We write 30 + (5 × 4) to show that 5 × 4 is worked out first."],
       teach=["Predict first: 30 marbles, plus 5 bags of 4 marbles. Is 30 + 5 × 4 equal to 35 × 4 or to 30 + 20?",
              "Just as a comma changes a sentence, the order of work changes an expression. We agree to work "
              "out the times part first.",
              "A bracket tells you to do that part first, so 30 + (5 × 4) keeps the meaning clear.",
              "To change the order, put the bracket somewhere else: (30 + 5) × 4 means 35 lots of 4."],
       examples=[
           WE("Meera has 30 marbles. A friend gives her 5 bags with 4 marbles in each bag. Write an expression for "
              "her marbles now and find its value.",
              ["The 5 bags give 5 × 4 = 20 new marbles.", "She had 30, so the total is 30 + 5 × 4.",
               "Work out the times part first: 5 × 4 = 20, then 30 + 20 = 50.",
               "Working left to right, 30 + 5 = 35 and then 35 × 4 = 140 would be wrong, because it gives 35 bags "
               "of 4 marbles."],
              "30 + 5 × 4 = 50, which is the same as 30 + (5 × 4)", ncert=["2.2.language", "2.2.ex4"],
              fact="ex4", expect=[50, 140])],
       key_terms=["expression", "bracket"], misconceptions=["M_LEFT_TO_RIGHT"], minutes=10),
     A("T4.C2", "Brackets decide what is worked out first", "Apply",
       "Students use a bracket to show which part of a bought-and-spent story is worked out first, evaluate "
       "expressions with brackets, and see when removing the bracket would make the story absurd.",
       textbook=["Irfan bought a pack of biscuits for ₹15 and a packet of toor dal for ₹56. He paid with a ₹100 "
                 "note. How much money does he have left? 100 − (15 + 56) = 29. Without the bracket, "
                 "100 − 15 + 56 = 141, which is absurd."],
       teach=["Predict first: Farhan pays 100 for two items costing 15 and 56. How much change should he get? Could "
              "it be more than 100?",
              "The total spend 15 + 56 must be worked out first, then taken from 100. A bracket shows that.",
              "Without the bracket, 100 − 15 + 56 would add the 56 back to his money, which makes no sense for a "
              "purchase."],
       examples=[
           WE("Farhan bought a pack of biscuits for ₹15 and a packet of toor dal for ₹56. He paid with a ₹100 note. "
              "Write an expression for the money he has left and find its value.",
              ["He spends 15 + 56 in all, so the bracket is (15 + 56).", "Money left: 100 − (15 + 56).",
               "Bracket first: 15 + 56 = 71. Then 100 − 71 = 29.",
               "Without the bracket, 100 − 15 + 56 = 141, which is more than the 100 he began with, so it cannot be "
               "the change."],
              "100 − (15 + 56) = ₹29", ncert=["2.2.brackets", "2.2.ex5"], fact="ex5", expect=[29, 141])],
       key_terms=["bracket"], misconceptions=["M_BRACKET_IGNORED", "M_LEFT_TO_RIGHT"], minutes=8),
     A("T4.C3", "Terms: the parts of an expression", "Apply",
       "Students write an expression as a sum of terms by treating a subtraction as adding a negative number, "
       "identify the terms, and evaluate each term before adding them.",
       textbook=["Terms are the parts of an expression that are added. 12 + 7 has the terms 12 and 7. 83 − 14 can "
                 "be written as 83 + (−14), with the terms 83 and −14.",
                 "6 × 5 + 3 has the terms 6 × 5 and 3. 6 × 5 is a single term as it has no plus sign.",
                 "Writing 13 − 2 + 6 as a sum of terms gives 13 + (−2) + 6, with the terms 13, −2 and 6."],
       teach=["Predict first: how many terms does 6 × 5 + 3 have? Is it 2 or 3?",
              "A term is a part that is added. Subtracting 14 is the same as adding the opposite, −14, so "
              "83 − 14 = 83 + (−14).",
              "A times sign does not split a term: 6 × 5 is one term. Only plus signs separate terms, after every "
              "subtraction is rewritten as adding a negative.",
              "Work out each term first, then add the terms with their signs."],
       examples=[
           WE("Write 13 − 2 + 6 and 2 − 10 + 4 × 6 as sums of terms, list the terms and find the values.",
              ["13 − 2 + 6 = 13 + (−2) + 6. The terms are 13, −2 and 6. Value: 13 − 2 + 6 = 17.",
               "2 − 10 + 4 × 6 = 2 + (−10) + 4 × 6. The terms are 2, −10 and 4 × 6, since 4 × 6 is one term.",
               "Work out 4 × 6 = 24 first, then 2 − 10 + 24 = 16."],
              "13 − 2 + 6 = 17 with terms 13, −2, 6; 2 − 10 + 4 × 6 = 16 with terms 2, −10, 4 × 6",
              ncert=["2.2.terms", "2.2.subtract_add", "2.2.try_terms"], fact="terms", expect=[17, 16]),
           WE("Write each as a sum of terms and list the terms: (a) 5 + 6 × 3 (b) 4 + 15 − 9 (c) 23 − 2 × 4 + 16 "
              "(d) 28 + 19 − 8.",
              ["(a) 5 + 6 × 3. The terms are 5 and 6 × 3. Value: 5 + 18 = 23.",
               "(b) 4 + 15 + (−9). The terms are 4, 15 and −9. Value: 4 + 15 − 9 = 10.",
               "(c) 23 + (−2 × 4) + 16. The terms are 23, −2 × 4 and 16. Value: 23 − 8 + 16 = 31.",
               "(d) 28 + 19 + (−8). The terms are 28, 19 and −8. Value: 28 + 19 − 8 = 39."],
              "(a) 5, 6 × 3 → 23 (b) 4, 15, −9 → 10 (c) 23, −2 × 4, 16 → 31 (d) 28, 19, −8 → 39",
              ncert=["2.2.try_terms"], fact="terms_table", expect=[23, 10, 31, 39])],
       key_terms=["term"], misconceptions=["M_TERM_PRODUCT", "M_TERM_SIGN"], minutes=10),
     DOER("T4.C4", "Practice: cut into terms, then work out each", "term_splitter", "Apply",
          "Students cut an expression into its terms, keep each sign with its number, work out every term and add "
          "the terms to find the value of the expression.",
          ["Rewrite every subtraction as adding a negative number.",
           "Only plus signs separate terms; a times sign stays inside one term.",
           "Work out each term first, then add."])]))
