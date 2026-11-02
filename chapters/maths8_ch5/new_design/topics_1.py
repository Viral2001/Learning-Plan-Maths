# -*- coding: utf-8 -*-
"""Topics T1 to T4 (module M1, first half): framing, sums of consecutive numbers and signs, breaking even, pairs to
make fours. Book section 5.1, pp 112 to 118."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

FIO1 = "multiples and remainders"
FIO4 = "number play"

# ============================== T1 Framing: will it always happen? ==========================================
TOPICS.append(TOPIC(
    "T1", "M1", "Number Play: Will It Always Happen?", ["5.1"], "Understand",
    "",
    "A pattern that keeps working on every number we try, and the question that drives the chapter: will it always "
    "happen, and how can we be sure without trying every number?",
    [A("T1.C1", "A pattern that keeps working", "Understand",
       "",
       textbook=["'What if ...?', 'Will it always happen?' Wondering and posing questions and conjectures is as much a "
                 "part of mathematics as problem solving."],
       teach=["Predict first: pick any four numbers in a row, like 3, 4, 5 and 6, and put plus or minus signs between "
              "them. Will the answer be even or odd?",
              "Try 3 + 4 − 5 + 6 and 5 − 6 − 7 − 8. The first gives 8 and the second gives −16: both even.",
              "Does it happen for every choice of four numbers, and for every way of placing the signs? Keep this "
              "question open: in this chapter we will learn to prove such patterns with algebra, dot pictures and "
              "place value, and to catch claims that are false."],
       ncert=["5.1.wonder"], key_terms=["pattern", "conjecture"], misconceptions=["M_EXAMPLES_PROVE"],
       video_focus=["HOOK"], minutes=4, enrichment=True)],
    topic_type="framing"))

# ============================== T2 Consecutive numbers and signs ============================================
TOPICS.append(TOPIC(
    "T2", "M1", "Consecutive Numbers and Signs", ["5.1"], "Analyze",
    "Students write numbers as sums of consecutive numbers, list and evaluate the eight signed expressions of four "
    "consecutive numbers, and explain with algebra why switching a sign never changes the parity of the result.",
    "Some numbers can be written as sums of consecutive numbers in one or more ways. For any four numbers, all eight "
    "ways of placing plus and minus signs give results of the same parity, because switching a sign changes the "
    "result by twice a number.",
    [A("T2.C1", "Sums of consecutive numbers", "Analyze",
       "Students write numbers as sums of two or more consecutive numbers, find numbers that can be written in more "
       "than one way, and notice which numbers cannot be written at all.",
       textbook=["5.1 Is This a Multiple Of?",
                 "Sum of Consecutive Numbers",
                 "Anshu is exploring sums of consecutive numbers. He has written the following:",
                 "7 = 3 + 4; 10 = 1 + 2 + 3 + 4; 12 = 3 + 4 + 5; 15 = 7 + 8, 15 = 4 + 5 + 6, 15 = 1 + 2 + 3 + 4 + 5.",
                 "Now, he is wondering:",
                 "\"Can I write every natural number as a sum of consecutive numbers?\"",
                 "\"Which numbers can I write as the sum of consecutive numbers in more than one way?\"",
                 "\"Ohh, I know all odd numbers can be written as a sum of two consecutive numbers. Can we write all "
                 "even numbers as a sum of consecutive numbers?\"",
                 "\"Can I write 0 as a sum of consecutive numbers? Maybe I should use negative numbers.\"",
                 "Explore these questions and any others that may occur to you. Discuss them with the class."],
       teach=["Predict first: can every number from 1 to 20 be written as a sum of two or more consecutive numbers?",
              "Two consecutive numbers always add to an odd number, so every odd number from 3 on is a sum of two.",
              "Three consecutive numbers add to three times the middle one, so 6, 9, 12 and so on work as sums of "
              "three.",
              "Some numbers, like 15, can be written in several ways, while 1, 2, 4, 8 and 16 cannot be written at "
              "all. With negative numbers, 0 works: −2, −1, 0, 1 and 2 add to 0."],
       examples=[
           WE("Find every way to write 15 and 9 as a sum of consecutive natural numbers. Can 8 be written this way?",
              ["15 as two numbers: 7 + 8 = 15. As three: 4 + 5 + 6 = 15. As five: 1 + 2 + 3 + 4 + 5 = 15.",
               "9 as two numbers: 4 + 5 = 9. As three: 2 + 3 + 4 = 9.",
               "8 as two numbers is impossible, since two consecutive numbers make an odd sum.",
               "8 as three numbers needs a middle number of 8 ÷ 3, which is not whole; four numbers starting at 1 "
               "already give 1 + 2 + 3 + 4 = 10, which is too big."],
              "15 can be written in three ways and 9 in two ways; 8 cannot be written as a sum of consecutive "
              "natural numbers",
              ncert=["5.1.anshu", "5.1.anshu_questions"])],
       key_terms=["consecutive numbers", "sum"], misconceptions=["M_CONSEC_ALL"], minutes=10),
     A("T2.C2", "Four consecutive numbers with plus and minus signs", "Apply",
       "Students list all eight ways of placing plus and minus signs between four consecutive numbers, evaluate each "
       "one, and notice that every result is even.",
       textbook=["Take any 4 consecutive numbers. For example, 3, 4, 5, and 6. Place '+' and '−' signs in between the "
                 "numbers. How many different possibilities exist? Write all of them.",
                 "Eight such expressions are possible. You can use the diagram below to systematically list all the "
                 "possibilities.",
                 "Evaluate each expression and write the result next to it. Do you notice anything interesting?",
                 "Now, take four other consecutive numbers. Place the '+' and '−' signs as you have done before. Find "
                 "out the results of each expression. What do you observe? Repeat this for one more set of 4 "
                 "consecutive numbers. Share your findings.",
                 "3 + 4 − 5 + 6 = 8; 3 − 4 − 5 − 6 = −12; 5 + 6 − 7 + 8 = 12; 5 − 6 − 7 − 8 = −16.",
                 "Some sums appear always no matter which 4 consecutive numbers are chosen. Isn't that interesting? "
                 "Do these patterns occur no matter which 4 consecutive numbers are chosen? Is there a way to find out "
                 "through reasoning? Hint: Use algebra and describe the 8 expressions in a general form.",
                 "You might have noticed that the results of all expressions are even numbers. Even numbers have a "
                 "factor of 2. Negative numbers having a factor 2 are also even numbers, for example, −2, −4, −6, and "
                 "so on. Check if anyone in your class got an odd number.",
                 "When 4 consecutive numbers are chosen, no matter how the '+' and '−' signs are placed between them, "
                 "the resulting expressions always have even parity."],
       teach=["Predict first: how many different ways are there to place three signs, each plus or minus?",
              "Each of the three gaps has 2 choices, so a tree diagram gives 2 × 2 × 2 = 8 expressions.",
              "Evaluate all eight for 3, 4, 5, 6: every result is even, including the negative ones.",
              "With letters a, a + 1, a + 2, a + 3, three of the results never change: a − (a + 1) − (a + 2) + (a + 3) "
              "is always 0, and two others are always −2 and −4."],
       examples=[
           WE("List all eight signed expressions for 3, 4, 5 and 6 and evaluate each. What do you notice?",
              ["With +4: 3 + 4 + 5 + 6 = 18, 3 + 4 + 5 − 6 = 6, 3 + 4 − 5 + 6 = 8, 3 + 4 − 5 − 6 = −4.",
               "With −4: 3 − 4 + 5 + 6 = 10, 3 − 4 + 5 − 6 = −2, 3 − 4 − 5 + 6 = 0, 3 − 4 − 5 − 6 = −12.",
               "All eight results are even: 18, 6, 8, −4, 10, −2, 0 and −12.",
               "The results 0, −2 and −4 appear for every set of four consecutive numbers."],
              "Eight expressions, and every result is even",
              ncert=["5.1.signs_list", "5.1.signs_evaluate", "5.1.even_parity"])],
       key_terms=["expression", "parity", "even"], misconceptions=["M_NEG_NOT_EVEN"], minutes=10),
     A("T2.C3", "Why switching a sign keeps the parity", "Analyze",
       "Students take any four numbers, show with algebra that switching one sign changes the value by twice a number, "
       "and conclude that all eight expressions have the same parity.",
       textbook=["Now take any 4 numbers, place '+' and '−' signs in the eight different ways, and evaluate the "
                 "resulting expression. What do you observe about their parities? Repeat this with other sets of 4 "
                 "numbers. Is there a way to explain why this happens? Hint: Think of the rules for parity of the sum "
                 "or difference of two numbers.",
                 "Explanation 1: Let us consider any of the 8 expressions formed by four numbers a, b, c, and d. When "
                 "one of its signs is switched, its value always increases or decreases by an even number! Let us see "
                 "why.",
                 "Consider one of the expressions: a + b − c − d. Replacing +b by −b, we get a − b − c − d.",
                 "By how much has the number changed? It has changed by (a + b − c − d) − (a − b − c − d), which is "
                 "a + b − c − d − a + b + c + d (notice how the signs changed when we opened the second set of "
                 "brackets), which is 2b (this is an even number).",
                 "If the difference between two numbers is even, can they have different parities? No! So either both "
                 "are even or both are odd.",
                 "Now, let us see what happens when a negative sign is switched to a positive sign. Replace any "
                 "negative sign in the expression a + b − c − d with a positive sign and find the difference between "
                 "the two numbers. What do you conclude from this observation?",
                 "Starting from any expression, we can get 7 expressions by switching one or more '+' and '−' signs. "
                 "Thus, all the expressions have the same parity!"],
       teach=["Predict first: if you change one plus to a minus, by how much does the answer move?",
              "Switching +b to −b takes b away twice, so the value drops by 2b, an even number.",
              "Switching −c to +c adds c back twice: (a + b + c − d) − (a + b − c − d) is 2c, again even.",
              "Two numbers that differ by an even number have the same parity, so all eight expressions match the "
              "parity of the first one."],
       examples=[
           WE("Take 3 + 4 − 5 − 6. Switch +4 to −4, then switch −5 to +5 in the original. How much does the value "
              "change each time, and what happens to its parity?",
              ["Original: 3 + 4 − 5 − 6 = −4.",
               "Switch +4 to −4: 3 − 4 − 5 − 6 = −12. The change is −4 − (−12) = 8, which is 2 × 4.",
               "Switch −5 to +5 in the original: 3 + 4 + 5 − 6 = 6. The change is 6 − (−4) = 10, which is 2 × 5.",
               "Each change is twice the switched number, so it is even and the parity stays even."],
              "The value changes by 8 and then by 10, twice the switched number each time, so the parity never changes",
              ncert=["5.1.any4", "5.1.expl1", "5.1.expl1_task"])],
       key_terms=["parity", "difference"], misconceptions=["M_SIGN_PARITY"], minutes=10),
     A("T2.C3x", "Parity rules, tokens and more than four numbers", "Evaluate",
       "Students use the rules for the parity of sums and differences, and the token model, to explain why the signed "
       "expressions share one parity for any count of numbers, not only four.",
       textbook=["Explanation 2: We know that odd ± odd is even, even ± even is even, odd ± even is odd.",
                 "We have seen that the parity of a + b and a − b is the same, regardless of the parities of a and b. "
                 "In short, a ± b have the same parity. By the same argument, a ± b + c and a ± b − c have the same "
                 "parity. Extending this further, we can say that all the expressions a ± b ± c ± d have the same "
                 "parity.",
                 "Explanation 3: This can also be explained using the positive and negative token model you studied "
                 "in the chapter on Integers. Try to think how.",
                 "The number of ways to choose 4 numbers a, b, c, d and combine them using '+' and '−' signs is "
                 "infinite. Mathematical reasoning allows us to prove that all the combinations a ± b ± c ± d always "
                 "have the same parity, without having to go through them one by one.",
                 "Several problems in mathematics can be thought about and solved in different ways. While the method "
                 "you came up with may be dear to you, it can be amusing and enriching to know how others thought "
                 "about it. Two tidbits: 'share' and 'listen'.",
                 "Is the phenomenon of all the expressions having the same parity limited to taking 4 numbers? What do "
                 "you think?"],
       teach=["Predict first: with five numbers and four signs, could one expression be odd and another even?",
              "a + b and a − b differ by 2b, so they always share a parity; adding or taking away the next number "
              "keeps the match going, for any count of numbers.",
              "With tokens, switching a sign turns some positive tokens into negative ones; each switched token moves "
              "the total by 2, so the parity holds."],
       examples=[
           WE("Place signs between 2, 7, 4, 9 and 6 in three different ways and evaluate. Do all results have the same "
              "parity, and why?",
              ["All plus: 2 + 7 + 4 + 9 + 6 = 28.",
               "Mixed: 2 − 7 + 4 − 9 + 6 = −4.",
               "All minus: 2 − 7 − 4 − 9 − 6 = −24.",
               "Each expression differs from the all plus sum by twice the numbers that were switched, so all are "
               "even, like 28."],
              "Yes; all results are even, because switching signs changes the total by an even amount for any count "
              "of numbers",
              ncert=["5.1.expl2", "5.1.expl3", "5.1.limit4"])],
       key_terms=["parity", "token model"], misconceptions=["M_SIGN_PARITY"], minutes=6, thin=True),
     DOER("T2.C4", "Practice: flip the signs, describe the numbers", "sign_flip_board", "Apply",
          "Students flip signs between four numbers to predict parity, and describe runs of consecutive numbers with "
          "a single letter-number.",
          ["Switching one sign changes a signed sum by twice that number, so the parity never changes.",
           "Consecutive numbers can all be written using one letter: n, n + 1, n + 2 and so on."],
          items=[
              FIO("FiO1.q1", "Figure it Out (%s, question 1)" % FIO1,
                  "The sum of four consecutive numbers is 34. What are these numbers?",
                  ["Call the numbers n, n + 1, n + 2 and n + 3; their sum is 4n + 6.",
                   "So 4n + 6 is 34, which gives 4n as 28 and n as 7.",
                   "Check: 7 + 8 + 9 + 10 = 34."],
                  "7, 8, 9 and 10"),
              FIO("FiO1.q2", "Figure it Out (%s, question 2)" % FIO1,
                  "Suppose p is the greatest of five consecutive numbers. Describe the other four numbers in terms of p.",
                  ["Each number is one less than the next one.",
                   "Counting down from p: p − 1, then p − 2, then p − 3, then p − 4.",
                   "Check with p as 10: the numbers are 6, 7, 8, 9 and 10."],
                  "p − 4, p − 3, p − 2 and p − 1"),
              FIO("FiO4.q9", "Figure it Out (%s, question 9)" % FIO4,
                  "The middle number in the sequence of 5 consecutive even numbers is 5p. Express the other four numbers "
                  "in sequence in terms of p.",
                  ["Consecutive even numbers differ by 2.",
                   "Two below the middle: 5p − 4 and 5p − 2. Two above: 5p + 2 and 5p + 4.",
                   "Check with p as 2: the middle is 10 and the five numbers are 6, 8, 10, 12 and 14."],
                  "5p − 4, 5p − 2, 5p, 5p + 2, 5p + 4")],
          misconceptions=["M_SIGN_PARITY"])],
    key_terms=["consecutive numbers", "parity", "expression"]))

# ============================== T3 Breaking even ===========================================================
TOPICS.append(TOPIC(
    "T3", "M1", "Breaking Even", ["5.1"], "Evaluate",
    "Students decide without computing whether sums, differences, products and powers are even, and decide whether "
    "an algebraic expression is even for every integer value, justifying with a factor of 2 or a counterexample.",
    "Odd ± odd and even ± even are even; odd ± even is odd; a product is even when any factor is even. An expression "
    "is always even when 2 is a factor of it; one counterexample shows it is not always even.",
    [A("T3.C1", "Even or odd without computing", "Apply",
       "Students use the parity rules for sums, differences, products and powers to tell whether an arithmetic "
       "expression is even without working it out.",
       textbook=["Breaking Even",
                 "We know how to identify even numbers. Without computing them, find out which of the following "
                 "arithmetic expressions are even.",
                 "43 + 37, 672 − 348, 4 × 347 × 3, 708 − 477, 809 + 214, 119 × 303, 543 − 479, 513³"],
       teach=["Predict first: is 543 − 479 even or odd? Decide before you subtract.",
              "Odd ± odd gives even, even ± even gives even, and odd ± even gives odd.",
              "A product is even if any factor is even; a product of odd numbers, such as an odd number cubed, is odd."],
       examples=[
           WE("Without computing, which of these are even: 43 + 37, 672 − 348, 4 × 347 × 3, 708 − 477, 809 + 214, "
              "119 × 303, 543 − 479, 513³?",
              ["43 + 37 is odd plus odd, so even. 672 − 348 is even minus even, so even.",
               "4 × 347 × 3 has the even factor 4, so even. 543 − 479 is odd minus odd, so even.",
               "708 − 477 is even minus odd and 809 + 214 is odd plus even, so both are odd.",
               "119 × 303 and 513³ are products of odd numbers, so both are odd.",
               "Check two of them: 43 + 37 = 80 and 543 − 479 = 64."],
              "Even: 43 + 37, 672 − 348, 4 × 347 × 3 and 543 − 479; the other four are odd",
              ncert=["5.1.breaking_numeric"])],
       key_terms=["even", "odd", "parity"], minutes=8),
     A("T3.C2", "Expressions that are always even", "Evaluate",
       "Students show that an expression such as 4m + 2q is even for all integers by finding a factor of 2, and show "
       "that x² + 2 is not always even with one example and one non-example.",
       textbook=["Using our understanding of how parity behaves under different operations, identify which of the "
                 "following algebraic expressions give an even number for any integer values for the letter-numbers.",
                 "2a + 2b, 3g + 5h, 4m + 2n, 2u − 4v, 13k − 5k, 6m − 3n, x² + 2, b² + 1, 4k × 3j",
                 "The expression 4m + 2q will always evaluate to an even number for any integer values of m and q. We "
                 "can justify this in two different ways: We know 4m is even and 2q is even for any integers m and q. "
                 "Therefore, their sum will also be even. The expression 4m + 2q is equal to the expression "
                 "2(2m + q). Here, the expression 2(2m + q) means 2 times 2m + q. In other words, 2 is a factor of this "
                 "expression. Therefore, this expression will always give an even number for any integers m and q.",
                 "For example, if m = 4 and q = −9, the expression 4m + 2q becomes 4 × 4 + 2 × (−9) = −2, which is an "
                 "even number.",
                 "In the expression x² + 2, x² is even if x is even, and x² is odd if x is odd. Therefore, the "
                 "expression x² + 2 will not always give an even number. An example and a non-example for when the "
                 "expression evaluates to an even number: (i) if x = 6, then x² + 2 = 38, and (ii) if x = 3, then "
                 "x² + 2 = 11."],
       teach=["Predict first: is 13k − 5k always even, even though 13 and 5 are odd?",
              "An expression is always even if it can be written as 2 times something, like 4m + 2q as 2(2m + q).",
              "To show an expression is not always even, one value that makes it odd is enough.",
              "13k − 5k simplifies to 8k, so it is always even."],
       examples=[
           WE("Show that 4m + 2q is always even and try it with m = 4, q = −9. Then decide whether x² + 2 is always "
              "even by trying x = 6 and x = 3.",
              ["4m + 2q is the same as 2(2m + q), so 2 is a factor for every integer m and q.",
               "With m = 4 and q = −9: 4 × 4 + 2 × (−9) = −2, which is even.",
               "With x = 6: 6² + 2 = 38, which is even.",
               "With x = 3: 3² + 2 = 11, which is odd, so x² + 2 is not always even."],
              "4m + 2q is always even; x² + 2 is even only when x is even",
              ncert=["5.1.breaking_algebra", "5.1.breaking_4m2q"])],
       key_terms=["algebraic expression", "factor", "counterexample"], misconceptions=["M_ODD_COEFF"], minutes=10),
     DOER("T3.C3", "Practice: always even or not?", None, "Evaluate",
          "Students sort the remaining expressions into always even and not always even, with examples and "
          "non-examples, and write expressions of their own that are always even.",
          ["An expression is always even when 2 is a factor of it.",
           "One value that gives an odd result shows the expression is not always even."],
          items=[
              FIO("5.1.breaking_task", "Breaking Even: decide and explain",
                  "Determine and explain which of these expressions always give even numbers: 2a + 2b, 3g + 5h, "
                  "4m + 2n, 2u − 4v, 13k − 5k, 6m − 3n, b² + 1, 4k × 3j. Write examples and non-examples, as "
                  "appropriate, for each. Then write a few algebraic expressions which always give an even number.",
                  ["2a + 2b is 2(a + b), 4m + 2n is 2(2m + n), 2u − 4v is 2(u − 2v): all always even.",
                   "13k − 5k is 8k and 4k × 3j is 12kj: both always even.",
                   "3g + 5h is odd when g is 1 and h is 2, giving 13; it is even when g is 1 and h is 1, giving 8.",
                   "6m − 3n is odd when m is 1 and n is 1, giving 3; b² + 1 is odd when b is 2, giving 5.",
                   "Expressions that always give even numbers: 2x + 6, 10y − 4z and 6p × q."],
                  "Always even: 2a + 2b, 4m + 2n, 2u − 4v, 13k − 5k, 4k × 3j. Not always even: 3g + 5h, 6m − 3n, "
                  "b² + 1")],
          misconceptions=["M_ODD_COEFF"])],
    key_terms=["even", "odd", "algebraic expression"]))

# ============================== T4 Pairs to make fours =====================================================
TOPICS.append(TOPIC(
    "T4", "M1", "Pairs to Make Fours", ["5.1"], "Analyze",
    "Students sort even numbers into multiples of 4 and numbers of the form 4p + 2, and explain with algebra and dot "
    "grids when the sum of two even numbers is a multiple of 4.",
    "Every even number is 4p or 4p + 2. Two numbers of the same type add to a multiple of 4; one of each type adds to "
    "4(p + q) + 2, which is never a multiple of 4.",
    [A("T4.C1", "Two kinds of even numbers", "Understand",
       "Students sort even numbers by their remainder on division by 4 into multiples of 4 (4p) and numbers that are 2 "
       "more than a multiple of 4 (4p + 2), using dot grids of four columns.",
       textbook=["Pairs to Make Fours",
                 "Take a pair of even numbers. Add them. Is the sum divisible by 4? Try this with different pairs of "
                 "even numbers. When is the sum a multiple of 4, and when is it not? Is there a general rule or a "
                 "pattern?",
                 "Even numbers can be of two types based on the remainders they leave when divided by 4.",
                 "Even numbers that are multiples of 4 leave a remainder of 0 when divided by 4. Even numbers that are "
                 "not multiples of 4 leave a remainder 2 when divided by 4."],
       teach=["Predict first: is 6 + 10 a multiple of 4? Is 4 + 10?",
              "Arrange an even number of dots in rows of four. Either the rows are full (4p) or 2 dots are left over "
              "(4p + 2).",
              "So every even number is of the form 4p or of the form 4p + 2."],
       examples=[
           WE("Sort 4, 12, 18, 22, 36 and 42 into numbers of the form 4p and numbers of the form 4p + 2.",
              ["4 = 4 × 1, 12 = 4 × 3 and 36 = 4 × 9: these fill rows of four exactly.",
               "18 = 4 × 4 + 2, 22 = 4 × 5 + 2 and 42 = 4 × 10 + 2: each leaves 2 dots over.",
               "So 4, 12 and 36 are of the form 4p, and 18, 22 and 42 are of the form 4p + 2."],
              "4p: 4, 12, 36. 4p + 2: 18, 22, 42",
              ncert=["5.1.pairs_question", "5.1.pairs_types"])],
       key_terms=["remainder", "multiple of 4"], misconceptions=["M_EVEN_SUM_4"], minutes=8),
     A("T4.C2", "When two even numbers make a multiple of 4", "Analyze",
       "Students explain with algebra and dot grids that two multiples of 4, or two numbers of the form 4p + 2, always "
       "add to a multiple of 4.",
       textbook=["When will two even numbers add up to give a multiple of 4? This problem is similar to the question "
                 "of identifying when adding two numbers will result in an even number. Can you see this? There are "
                 "three cases to examine:",
                 "Adding two (even) numbers that are multiples of 4 will always give a multiple of 4: 4p and 4q, "
                 "4p + 4q, which is 4(p + q). Examples: 4, 12, 16, 24, 36. 12 + 16 = 4 × (3 + 4) = 28. "
                 "16 + 28 = 4 × (4 + 7) = 44.",
                 "Adding two even numbers that are not multiples of 4 will always give a multiple of 4 because their "
                 "remainders of 2 add up to 4: (4p + 2) and (4q + 2), (4p + 2) + (4q + 2), which is 4p + 4q + 4, which "
                 "is 4(p + q + 1). Examples: 2, 6, 10, 18, 22, 42. 2 + 6 = 8. 6 + 10 = 16. 22 + 6 = 28."],
       teach=["Predict first: two leftovers of 2 dots, what happens when you put them together?",
              "4p + 4q is 4(p + q): the full rows just stack up.",
              "(4p + 2) + (4q + 2) is 4(p + q + 1): the two leftover pairs join into one more full row of four."],
       examples=[
           WE("Show that 12 + 16 and 22 + 6 are multiples of 4, using the forms 4p + 4q and (4p + 2) + (4q + 2).",
              ["12 is 4 × 3 and 16 is 4 × 4, so 12 + 16 = 4 × (3 + 4) = 28.",
               "22 is 4 × 5 + 2 and 6 is 4 × 1 + 2.",
               "Together the leftovers make 2 + 2 = 4, one more full row: 4 × (5 + 1 + 1) = 28.",
               "Both sums are multiples of 4."],
              "12 + 16 and 22 + 6 both make 28, a multiple of 4",
              ncert=["5.1.pairs_cases"])],
       key_terms=["multiple of 4", "dot grid"], misconceptions=["M_EVEN_SUM_4"], minutes=10),
     DOER("T4.C3", "Practice: pairs that make multiples", "pairs_dot_grid", "Analyze",
          "Students explain the mixed case of a multiple of 4 plus a number of the form 4q + 2, and extend the idea to "
          "sums of two multiples of 3.",
          ["Same type plus same type gives a multiple of 4; one of each type leaves a remainder of 2.",
           "Write each number in its form, add, and look for the common factor."],
          items=[
              FIO("5.1.pairs_task", "Pairs to Make Fours: the third case",
                  "What happens when we add a multiple of 4 to an even number that is not a multiple of 4? Is it similar "
                  "to the case of the parity of the sum of an even and an odd number? For 4p and (4q + 2), write the "
                  "explanation and examples.",
                  ["4p + (4q + 2) is 4p + 4q + 2, which is 4(p + q) + 2.",
                   "The full rows stack up and 2 dots are always left over, so the sum is never a multiple of 4.",
                   "Examples: 4 + 6 = 10, 12 + 18 = 30, 8 + 22 = 30; each leaves a remainder of 2 on division by 4.",
                   "It is like even plus odd: the leftover can never be paired away."],
                  "The sum is 4(p + q) + 2, so it always leaves a remainder of 2 and is never a multiple of 4"),
              FIO("FiO4.q3", "Figure it Out (%s, question 3)" % FIO4,
                  "When is the sum of two multiples of 3, a multiple of 6 and when is it not? Explain the different "
                  "possible cases, and generalise the pattern.",
                  ["Write the two multiples as 3m and 3n; their sum is 3(m + n).",
                   "It is a multiple of 6 when m + n is even, that is when m and n are both even or both odd.",
                   "Both odd: 3 + 9 = 12. Both even: 6 + 12 = 18. One of each: 3 + 6 = 9, not a multiple of 6.",
                   "This matches the parity rules: odd multiples of 3 behave like odd numbers, even multiples like even "
                   "numbers."],
                  "The sum is a multiple of 6 when both are odd multiples of 3 or both are even multiples of 3; one of "
                  "each gives an odd multiple of 3")],
          misconceptions=["M_EVEN_SUM_4"])],
    key_terms=["even", "multiple of 4", "remainder"]))
