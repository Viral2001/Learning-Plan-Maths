# -*- coding: utf-8 -*-
"""Topics T5 and T6 (module M1, second half): always, sometimes or never, and what remains. Book section 5.1,
pp 118 to 123, with the first Figure it Out set and the related questions of the last set."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

FIO1 = "multiples and remainders"
FIO4 = "number play"

# ============================== T5 Always, sometimes or never ==============================================
TOPICS.append(TOPIC(
    "T5", "M1", "Always, Sometimes or Never", ["5.1"], "Evaluate",
    "Students decide whether statements about factors and multiples are always, sometimes or never true, proving "
    "'always' with algebra or dot rows, showing 'sometimes' with an example and a counterexample, and 'never' with a "
    "reason it cannot hold.",
    "If a divides M and N, it divides M + N and M − N. If A is divisible by k, so are all multiples of A, and A is "
    "divisible by every factor of k. A number divisible by k and by m is divisible by their LCM, not always by k × m.",
    [A("T5.C1", "Divisors of sums and differences", "Analyze",
       "Students show with algebra and dot rows that a number dividing two numbers divides their sum and difference, "
       "and use a counterexample to show the converse is only sometimes true.",
       textbook=["Always, Sometimes, or Never",
                 "We examine different statements about factors and multiples and determine whether a statement is "
                 "'Always True', 'Sometimes True', or 'Never True'. We know that the sum of any two multiples of 2 is "
                 "also a multiple of 2.",
                 "1. If 8 exactly divides two numbers separately, it must exactly divide their sum.",
                 "The two numbers have 8 as a factor; in other words, the two numbers are multiples of 8: 8a and 8b. As "
                 "multiples of 8 are obtained by repeatedly adding 8, the sum of two multiples of 8 will also be a "
                 "multiple of 8: 8a + 8b, which is 8(a + b). Examples: 8 and 16, 16 and 56, 80 and 120. "
                 "8 + 16 = 8 × (1 + 2) = 24. 16 + 56 = 72. 80 + 120 = 200.",
                 "Statement 1 is always true. Determine if it is true with subtraction.",
                 "In general, if a divides M and a divides N, then a divides M + N and a divides M − N. In other words, "
                 "if M and N are multiples of a, then M + N and M − N will also be multiples of a.",
                 "2. If a number is divisible by 8, then 8 also divides any two numbers (separately) that add up to the "
                 "number.",
                 "A number divisible by 8 is a multiple of 8: 8m. A number divisible by 8 can be expressed as a sum of "
                 "two multiples of 8 or sum of two non-multiples of 8: 8m is 8a + 8b, or 8m is p + q with p and q not "
                 "multiples of 8. Examples: 8, 16, 56, 72. 72 = 48 + 24 (8 × 9 = 8 × 6 + 8 × 3). 72 = 50 + 22.",
                 "So, statement 2 is sometimes true."],
       teach=["Predict first: 8 divides 16 and 56. Must it divide 16 + 56? Must it divide 56 − 16?",
              "8a + 8b is 8(a + b) and 8a − 8b is 8(a − b): rows of 8 stay rows of 8 when joined or taken away.",
              "The other way round fails: 72 is a multiple of 8, but 72 is also 50 + 22, and neither 50 nor 22 is a "
              "multiple of 8.",
              "One counterexample is enough to show a statement is not always true."],
       examples=[
           WE("Check that 8 divides 16 + 56 and 80 − 24. Then decide whether 8 must divide two numbers that add up to "
              "72.",
              ["16 is 8 × 2 and 56 is 8 × 7, so 16 + 56 = 8 × (2 + 7) = 72.",
               "80 is 8 × 10 and 24 is 8 × 3, so 80 − 24 = 8 × (10 − 3) = 56.",
               "72 = 48 + 24, and both are multiples of 8.",
               "But 72 = 50 + 22 too, and neither 50 nor 22 is a multiple of 8."],
              "8 divides the sum and the difference of its multiples, always; two numbers adding to a multiple of 8 "
              "are multiples of 8 only sometimes",
              ncert=["5.1.asn_s1", "5.1.asn_s2"])],
       key_terms=["divides", "multiple", "always true", "sometimes true"], misconceptions=["M_DIV_ADDENDS"],
       minutes=10),
     A("T5.C2", "Multiples and factors of a divisible number", "Analyze",
       "Students explain why multiples of a multiple of 7 stay multiples of 7, why a multiple of 12 is divisible by "
       "every factor of 12, and when a multiple of 7 is divisible by another multiple of 7.",
       textbook=["3. If a number is divisible by 7, then all multiples of that number will be divisible by 7.",
                 "Numbers divisible by 7 will have 7 as a factor: 7j. Examples: 14 = 7 × 2 (j = 2), 42 = 7 × 6 "
                 "(j = 6), 98 = 7 × 14 (j = 14). (7j) × m contains a total of mj rows. So this is also a multiple of 7. "
                 "Some multiples of 14: 28 = (7 × 2) × 2, 70 = (7 × 2) × 5, 154 = (7 × 2) × 11.",
                 "The number 7jm or (7 × j × m) has a factor of 7. We can see that Statement 3 is always true.",
                 "In general, if A is divisible by k, then all multiples of A are divisible by k.",
                 "4. If a number is divisible by 12, then the number is also divisible by all the factors of 12.",
                 "A number divisible by 12 is a multiple of 12: 12m. Factors of multiples of 12 will include factors "
                 "of 12: 12m is 2 × 6 × m and 3 × 4 × m. A factor of 12 covers a row fully. Hence, it covers all "
                 "multiples of 12 fully. Examples: 12, 24, 36, 48, 108, 132. Factors of 24: 1, 2, 3, 4, 6, 8, 12, 24.",
                 "In general, if A is divisible by k, then A is divisible by all the factors of k. Hence, Statement 4 is "
                 "always true.",
                 "5. If a number is divisible by 7, then it is also divisible by any multiple of 7.",
                 "Numbers divisible by 7 are multiples of 7: 7k. Multiples of 7: 7m. 7k will be divisible by 7m if and "
                 "only if m is a factor of k. If k = ym then 7k ÷ 7m is 7ym ÷ 7m, which is y.",
                 "42 (7 × 6) is divisible by 7 but it is not divisible by 28 (7 × 4). 42 (7 × 6) is divisible by 7 and "
                 "it is divisible by 14 (7 × 2).",
                 "We can see that this statement is only sometimes true."],
       teach=["Predict first: 42 is divisible by 7. Is it divisible by 14? By 28?",
              "A multiple of 7j is 7 × j × m: the factor 7 never goes away, so every multiple of a multiple of 7 is a "
              "multiple of 7, always.",
              "12m is 2 × 6 × m and 3 × 4 × m, so every factor of 12 divides a multiple of 12, always.",
              "7k is divisible by 7m only when m is a factor of k, so a multiple of 7 is divisible by another multiple "
              "of 7 only sometimes."],
       examples=[
           WE("36 is divisible by 12. Check that 36 is divisible by every factor of 12 and that its multiple 108 is "
              "divisible by 12. Then decide whether 42, a multiple of 7, is divisible by 28 and by 14.",
              ["Factors of 12: 1, 2, 3, 4, 6, 12. 36 ÷ 4 = 9, 36 ÷ 6 = 6, 36 ÷ 12 = 3, and 36 ÷ 2, 36 ÷ 3 are whole "
               "too.",
               "108 = 36 × 3, and 108 = 12 × 9, so the multiple is divisible by 12.",
               "42 = 7 × 6. 42 ÷ 14 = 3, so 14 divides it, because 2 is a factor of 6.",
               "42 = 28 + 14, so 28 leaves a remainder of 14: 4 is not a factor of 6."],
              "36 passes every factor of 12 and 108 is divisible by 12 (always true); 42 is divisible by 14 but not by "
              "28 (sometimes true)",
              ncert=["5.1.asn_s3", "5.1.asn_s4", "5.1.asn_s5"])],
       key_terms=["factor", "multiple", "divisible"], misconceptions=["M_DIV_MULTIPLE"], minutes=10),
     A("T5.C3", "Divisible by two numbers: the LCM rule", "Evaluate",
       "Students decide that a number divisible by 9 and by 4 is divisible by 36, but a number divisible by 6 and by 4 "
       "need not be divisible by 24, and state the LCM rule.",
       textbook=["Examine each of the following statements, and determine whether it is 'Always true', 'Sometimes "
                 "true', 'Never true'.",
                 "6. If a number is divisible by both 9 and 4, it must be divisible by 36.",
                 "7. If a number is divisible by both 6 and 4, it must be divisible by 24.",
                 "In general, if A is divisible by k and A is also divisible by m, then A is divisible by the LCM of k "
                 "and m. This is because A is a multiple of k and also a multiple of m, so A's prime factorisation "
                 "should contain the prime factorisation of LCM (k, m)."],
       teach=["Predict first: 12 is divisible by 6 and by 4. Is it divisible by 6 × 4?",
              "9 and 4 share no common factor, so their LCM is 36: divisible by 9 and by 4 always means divisible by "
              "36.",
              "6 and 4 share the factor 2, so their LCM is only 12: 12 is divisible by 6 and 4 but not by 24, while 48 "
              "is divisible by all three.",
              "A number divisible by k and by m is divisible by the LCM of k and m."],
       examples=[
           WE("Decide whether each claim is always, sometimes or never true: a number divisible by both 9 and 4 is "
              "divisible by 36; a number divisible by both 6 and 4 is divisible by 24.",
              ["9 and 4 share no factor except 1, so the LCM of 9 and 4 is 36.",
               "A number divisible by both must be a multiple of 36: 72 is 9 × 8, 4 × 18 and 36 × 2.",
               "The LCM of 6 and 4 is 12, not 24: 12 is divisible by 6 and by 4 but not by 24.",
               "48 is divisible by 6, 4 and 24, so the claim about 24 holds for some numbers."],
              "The claim about 36 is always true; the claim about 24 is sometimes true (12 fails, 48 works)",
              ncert=["5.1.asn_mt67"])],
       key_terms=["LCM", "prime factorisation"], misconceptions=["M_PRODUCT_RULE"], minutes=10),
     A("T5.C3x", "Odd plus even is never a multiple of 6", "Evaluate",
       "Students show with parity and with algebra that an odd number added to an even number can never give a "
       "multiple of 6.",
       textbook=["8. When you add an odd number to an even number we get a multiple of 6.",
                 "We know that multiples of 6 are all even numbers. The sum of an odd number and an even number will be "
                 "an odd number. Therefore, this statement is never true. We can also explain this algebraically.",
                 "\"Can I write an even and an odd number as 2n and 2n + 1 instead?\"",
                 "Suppose, (2n) + (2m + 1) = 6j, where 2n is an even number, 2m + 1 is an odd number, and 6j is a "
                 "multiple of 6. Then 2n + 2m = 6j − 1, 2(n + m) = 6j − 1, which means 2(n + m), which is an even "
                 "number, should be equal to 6j − 1, which is an odd number. This is never true."],
       teach=["Predict first: can you find an odd number and an even number that add to 12, 18 or 24?",
              "Every multiple of 6 is even, and odd plus even is always odd, so it can never happen.",
              "Using 2n and 2n + 1 would make the two numbers consecutive; to cover every pair we need different "
              "letters, 2n and 2m + 1."],
       examples=[
           WE("Try 7 + 8 and 9 + 12, then explain with algebra why an odd number plus an even number is never a "
              "multiple of 6.",
              ["7 + 8 = 15 and 9 + 12 = 21: both odd, neither a multiple of 6.",
               "Write the even number as 2n and the odd number as 2m + 1.",
               "Their sum is 2(n + m) + 1, which is one more than an even number, so it is odd.",
               "Every multiple of 6 is 6j, which is 2 × 3j, an even number, so the sum can never equal it."],
              "Never true: odd plus even is odd, and every multiple of 6 is even",
              ncert=["5.1.asn_s8"])],
       key_terms=["never true", "parity"], minutes=6, thin=True),
     DOER("T5.C4", "Practice: always, sometimes or never?", "claim_tester", "Evaluate",
          "Students sort statements about multiples, products and consecutive numbers into always, sometimes and never "
          "true, proving each verdict with algebra, an example or a counterexample.",
          ["Always true needs a reason for every number; one counterexample shows a statement is not always true.",
           "Write multiples as 6a, 9b and so on, and look for the common factor."],
          items=[
              FIO("FiO1.q3", "Figure it Out (%s, question 3)" % FIO1,
                  "For each statement below, determine whether it is always true, sometimes true, or never true. "
                  "Explain your answer, with examples and non-examples, and justify your claim using algebra. (i) The "
                  "sum of two even numbers is a multiple of 3. (ii) If a number is not divisible by 18, then it is "
                  "also not divisible by 9. (iii) If two numbers are not divisible by 6, then their sum is not "
                  "divisible by 6. (iv) The sum of a multiple of 6 and a multiple of 9 is a multiple of 3. (v) The sum "
                  "of a multiple of 6 and a multiple of 3 is a multiple of 9.",
                  ["(i) 2 + 4 = 6 is a multiple of 3, but 2 + 6 = 8 is not: sometimes true.",
                   "(ii) 10 is divisible by neither, but 27 is not divisible by 18 and is divisible by 9: sometimes "
                   "true.",
                   "(iii) 1 + 2 = 3 is not divisible by 6, but 8 + 10 = 18 is: sometimes true.",
                   "(iv) 6a + 9b is 3(2a + 3b), so it is always a multiple of 3: always true.",
                   "(v) 6a + 3b is 3(2a + b): 6 + 3 = 9 is a multiple of 9, but 6 + 6 = 12 is not: sometimes true."],
                  "(i) sometimes (ii) sometimes (iii) sometimes (iv) always (v) sometimes"),
              FIO("FiO4.q11", "Figure it Out (%s, question 11)" % FIO4,
                  "Deepak claims, \"There are some multiples of 11 which, when doubled, are still multiples of 11. But "
                  "other multiples of 11 don't remain multiples of 11 when doubled.\" Examine if his conjecture is "
                  "true; explain your conclusion.",
                  ["Write any multiple of 11 as 11k.",
                   "Doubling gives 2 × 11k, which is 11 × 2k, still a multiple of 11.",
                   "For example 33 doubled is 66 and 121 doubled is 242, both multiples of 11.",
                   "Every multiple of a number stays a multiple when doubled, so the second part of the claim is false."],
                  "The conjecture is false: every multiple of 11, doubled, is still a multiple of 11"),
              FIO("FiO4.q12", "Figure it Out (%s, question 12)" % FIO4,
                  "Determine whether the statements below are always true, sometimes true, or never true, and explain. "
                  "(i) The product of a multiple of 6 and a multiple of 3 is a multiple of 9. (ii) The sum of three "
                  "consecutive even numbers will be divisible by 6. (iii) If abcdef is a multiple of 6, then badcef "
                  "will be a multiple of 6. (iv) 8(7b − 3) − 4(11b + 1) is a multiple of 12.",
                  ["(i) 6a × 3b is 18ab, which is 9 × 2ab: always true.",
                   "(ii) 2n + (2n + 2) + (2n + 4) is 6n + 6, which is 6(n + 1): always true.",
                   "(iii) badcef has the same digits, so the same digit sum (the test for 3), and the same units digit f "
                   "(the test for 2): always true.",
                   "(iv) 8(7b − 3) − 4(11b + 1) is 56b − 24 − 44b − 4, which is 12b − 28, that is 12(b − 3) + 8.",
                   "It always leaves a remainder of 8 on division by 12, so (iv) is never true."],
                  "(i) always (ii) always (iii) always (iv) never"),
              FIO("FiO4.q14", "Figure it Out (%s, question 14)" % FIO4,
                  "Is the product of two consecutive integers always a multiple of 2? Why? Is the product of three "
                  "consecutive integers always a multiple of 6? Why or why not? What can you say about the product of 4 "
                  "consecutive integers? What about the product of five consecutive integers?",
                  ["Of two consecutive integers one is even, so their product is a multiple of 2.",
                   "Of three consecutive integers one is a multiple of 3 and at least one is even, so the product is a "
                   "multiple of 6: 4 × 5 × 6 = 120.",
                   "Four consecutive integers hold a multiple of 4, another even number and a multiple of 3, so the "
                   "product is a multiple of 24: 1 × 2 × 3 × 4 = 24.",
                   "Five consecutive integers also hold a multiple of 5, so the product is a multiple of 120: "
                   "1 × 2 × 3 × 4 × 5 = 120."],
                  "Always a multiple of 2, of 6, of 24 and of 120 respectively"),
              FIO("FiO4.q16", "Figure it Out (%s, question 16)" % FIO4,
                  "Which of the four Venn diagrams captures the relationship between the multiples of 4, 8, and 32?",
                  ["Every multiple of 32 is 8 × 4k, so it is also a multiple of 8.",
                   "Every multiple of 8 is 4 × 2k, so it is also a multiple of 4.",
                   "But 4 is not a multiple of 8, and 8 is not a multiple of 32.",
                   "So the circle for multiples of 32 sits inside the circle for multiples of 8, which sits inside the "
                   "circle for multiples of 4."],
                  "Diagram (iv): multiples of 32 inside multiples of 8, inside multiples of 4")],
          misconceptions=["M_PRODUCT_RULE", "M_DIV_ADDENDS"])],
    key_terms=["always true", "sometimes true", "never true", "LCM"]))

# ============================== T6 What remains? ===========================================================
TOPICS.append(TOPIC(
    "T6", "M1", "What Remains?", ["5.1"], "Apply",
    "Students describe numbers with a given remainder by an algebraic expression, combine remainders of sums and "
    "differences without calculating, and find numbers that meet two or more remainder conditions.",
    "Numbers with remainder r on division by d are of the form dk + r. Remainders add and subtract along with the "
    "numbers, and numbers meeting several remainder conditions repeat every LCM of the divisors.",
    [A("T6.C1", "Writing numbers with a given remainder", "Apply",
       "Students list numbers that leave remainder 3 on division by 5, choose the expressions 5k + 3 and 5k − 2 that "
       "capture all of them, and reject the others with a counterexample.",
       textbook=["What Remains?",
                 "Find a number that has a remainder of 3 when divided by 5. Write more such numbers.",
                 "Which algebraic expression(s) capture all such numbers? (i) 3k + 5 (ii) 3k − 5 (iii) 3k ÷ 5 "
                 "(iv) 5k + 3 (v) 5k − 2 (vi) 5k − 3",
                 "The numbers that leave a remainder of 0 when divided by 5 are the multiples of 5. But we want numbers "
                 "that leave a remainder of 3 when divided by 5. These numbers are 3 more than multiples of 5. "
                 "Multiples of 5 are of the form 5k. So, numbers that leave a remainder of 3 when divided by 5 are "
                 "those of the form 5k + 3. For k = 0, 1, 2, 3, 4, the values of 5k + 3 are 3, 8, 13, 18, 23.",
                 "Let us consider another expression, 5k − 2, and see the values it takes for different values of k. "
                 "Numbers that leave a remainder of 3 when divided by 5 can also be seen as 2 less than multiples of 5; "
                 "5k − 2, where k is at least 1. For k = 1, 2, 3, 4, 5, the values of 5k − 2 are 3, 8, 13, 18, 23.",
                 "Are there other expressions that generate numbers that are 3 more than a multiple of 5?"],
       teach=["Predict first: which comes first in the expression, the divisor 5 or the remainder 3?",
              "Remainder 3 on division by 5 means 3 more than a multiple of 5: 5k + 3.",
              "The same numbers are 2 less than the next multiple of 5: 5k − 2, starting from k = 1.",
              "One value that gives a wrong remainder rules an expression out."],
       examples=[
           WE("Which of 3k + 5, 3k − 5, 3k ÷ 5, 5k + 3, 5k − 2 and 5k − 3 give exactly the numbers that leave "
              "remainder 3 on division by 5?",
              ["The numbers are 3, 8, 13, 18, 23 and so on, each 5 more than the one before.",
               "5k + 3 with k = 0, 1, 2, 3 gives 3, 8, 13, 18, and 5k − 2 with k = 1, 2, 3, 4 gives the same numbers.",
               "3k + 5 with k = 2 gives 11, which leaves remainder 1; 3k − 5 with k = 2 gives 1.",
               "5k − 3 with k = 1 gives 2, and 3k ÷ 5 is often not even a whole number."],
              "5k + 3 (k from 0) and 5k − 2 (k from 1); the other four do not work",
              ncert=["5.1.remains_find", "5.1.remains_5k3", "5.1.remains_other"])],
       key_terms=["remainder", "algebraic expression"], misconceptions=["M_REMAINDER_FORM"], minutes=10),
     A("T6.C2", "Remainders of sums and differences", "Apply",
       "Students find the remainder of a sum or difference from the remainders of the two numbers, writing each number "
       "as a multiple plus its remainder.",
       teach=["Predict first: 17 leaves remainder 2 and 24 leaves remainder 4 on division by 5. What does 17 + 24 "
              "leave?",
              "Write each number as a multiple of 5 plus a remainder; the multiples add to a multiple of 5.",
              "So only the remainders matter: 2 + 4 makes 6, which is one more group of 5 and 1 left over.",
              "For a difference, take the remainders away: 4 − 2 leaves 2."],
       examples=[
           WE("17 leaves remainder 2 and 24 leaves remainder 4 on division by 5. Without adding, find the remainders "
              "of 17 + 24 and 24 − 17 on division by 5.",
              ["17 = 5 × 3 + 2 and 24 = 5 × 4 + 4.",
               "Sum: the multiples make 5 × 7 and the remainders make 6, which is 5 + 1, so the remainder is 1.",
               "Difference: the multiples make 5 × 1 and the remainders make 4 − 2, so the remainder is 2.",
               "Check: 17 + 24 = 41 = 5 × 8 + 1 and 24 − 17 = 7 = 5 × 1 + 2."],
              "17 + 24 leaves remainder 1 and 24 − 17 leaves remainder 2")],
       key_terms=["remainder", "sum", "difference"], misconceptions=["M_REMAINDER_FORM"], minutes=8),
     A("T6.C3", "Two remainder conditions at once", "Analyze",
       "Students list numbers that meet two remainder conditions, notice that they repeat every LCM of the divisors, "
       "and write one expression for all of them.",
       teach=["Predict first: which numbers leave remainder 1 both on division by 2 and on division by 3?",
              "Take 1 away and the number becomes a multiple of 2 and of 3, so a multiple of 6.",
              "So the numbers are 6k + 1: 1, 7, 13, 19 and so on, repeating every 6."],
       examples=[
           WE("Find numbers that leave remainder 1 on division by 2 and remainder 1 on division by 3, and write one "
              "expression for all of them.",
              ["Odd numbers leave remainder 1 on division by 2: 1, 3, 5, 7, 9, 11, 13.",
               "Of these, 1, 7 and 13 leave remainder 1 on division by 3.",
               "One less than each, 0, 6 and 12, is a multiple of both 2 and 3, so a multiple of 6.",
               "So the numbers are 6k + 1, and they repeat every 6."],
              "1, 7, 13, 19, and so on: all numbers of the form 6k + 1")],
       key_terms=["remainder", "LCM"], minutes=8),
     DOER("T6.C4", "Practice: what remains?", "remainder_rows", "Apply",
          "Students write expressions for numbers with given remainders, test claims about them, and solve remainder "
          "puzzles.",
          ["A number with remainder r on division by d is dk + r.",
           "Remainders add and subtract with the numbers; several conditions repeat every LCM of the divisors."],
          items=[
              FIO("FiO1.q4", "Figure it Out (%s, question 4)" % FIO1,
                  "Find a few numbers that leave a remainder of 2 when divided by 3 and a remainder of 2 when divided by "
                  "4. Write an algebraic expression to describe all such numbers.",
                  ["Take 2 away: the number becomes a multiple of 3 and of 4, so a multiple of 12.",
                   "So the numbers are 12k + 2: 2, 14, 26, 38 and so on.",
                   "Check 14: 14 = 3 × 4 + 2 and 14 = 4 × 3 + 2."],
                  "2, 14, 26, 38, ...; all numbers of the form 12k + 2"),
              FIO("FiO1.q5", "Figure it Out (%s, question 5)" % FIO1,
                  "\"I hold some pebbles, not too many. When I group them in 3's, one stays with me. Try pairing them "
                  "up, it simply won't do, a stubborn odd pebble remains in my view. Group them by 5, yet one's still "
                  "around, but grouping by seven, perfection is found. More than one hundred would be far too bold. Can "
                  "you tell me the number of pebbles I hold?\"",
                  ["One pebble is left over when grouping by 3, by 2 and by 5.",
                   "So one less than the number is a multiple of 30: the number is 31, 61 or 91 below one hundred.",
                   "Grouping by 7 leaves nothing: 31 and 61 are not multiples of 7, but 91 = 7 × 13."],
                  "91 pebbles"),
              FIO("FiO1.q6", "Figure it Out (%s, question 6)" % FIO1,
                  "Tathagat has written several numbers that leave a remainder of 2 when divided by 6. He claims, \"If "
                  "you add any three such numbers, the sum will always be a multiple of 6.\" Is Tathagat's claim true?",
                  ["Write the three numbers as 6a + 2, 6b + 2 and 6c + 2.",
                   "Their sum is 6a + 6b + 6c + 6, which is 6(a + b + c + 1).",
                   "Check: 2 + 8 + 14 = 24, a multiple of 6."],
                  "Yes, the claim is true: the three remainders of 2 make 6"),
              FIO("FiO1.q7", "Figure it Out (%s, question 7)" % FIO1,
                  "When divided by 7, the number 661 leaves a remainder of 3, and 4779 leaves a remainder of 5. Without "
                  "calculating, can you say what remainders the following expressions will leave when divided by 7? "
                  "Show the solution both algebraically and visually. (i) 4779 + 661 (ii) 4779 − 661",
                  ["Write 661 as 7m + 3 and 4779 as 7n + 5.",
                   "(i) The sum is 7(m + n) + 8; the 8 left over makes one more group of 7 with 1 left, so the "
                   "remainder is 1.",
                   "(ii) The difference is 7(n − m) + 2, so the remainder is 2.",
                   "Visually: rows of 7 dots with 5 and 3 dots left over; the leftovers join to make a full row and 1 "
                   "more, or 5 minus 3 leaves 2."],
                  "(i) remainder 1 (ii) remainder 2"),
              FIO("FiO1.q8", "Figure it Out (%s, question 8)" % FIO1,
                  "Find a number that leaves a remainder of 2 when divided by 3, a remainder of 3 when divided by 4, and "
                  "a remainder of 4 when divided by 5. What is the smallest such number? Can you give a simple "
                  "explanation of why it is the smallest?",
                  ["Each remainder is one less than the divisor, so one more than the number is a multiple of 3, 4 and "
                   "5.",
                   "The smallest common multiple of 3, 4 and 5 is their LCM, 60, so the number is 59.",
                   "Check: 59 = 3 × 19 + 2, 59 = 4 × 14 + 3 and 59 = 5 × 11 + 4."],
                  "59; it is the smallest because 60 is the smallest common multiple of 3, 4 and 5"),
              FIO("FiO4.q2", "Figure it Out (%s, question 2)" % FIO4,
                  "\"I take a number that leaves a remainder of 8 when divided by 12. I take another number which is 4 "
                  "short of a multiple of 12. Their sum will always be a multiple of 8\", claims Snehal. Examine his "
                  "claim and justify your conclusion.",
                  ["Write the numbers as 12n + 8 and 12m − 4.",
                   "Their sum is 12(n + m) + 4, which is always 4 more than a multiple of 12.",
                   "8 and 8 fit and make 16, a multiple of 8; but 20 and 8 fit too and make 28, which is not.",
                   "So the sum is always a multiple of 4, but only sometimes a multiple of 8."],
                  "The claim is false: the sum is 12(n + m) + 4, a multiple of 8 only sometimes (for example 28 is not)"),
              FIO("FiO4.q7", "Figure it Out (%s, question 7)" % FIO4,
                  "Find three consecutive numbers such that the first number is a multiple of 2, the second number is a "
                  "multiple of 3, and the third number is a multiple of 4. Are there more such numbers? How often do "
                  "they occur?",
                  ["Try small numbers: 2, 3 and 4 work.",
                   "If n, n + 1 and n + 2 work, then n − 2 is a multiple of 2, of 3 and of 4, so a multiple of 12.",
                   "So n is 12k + 2: 2, 3, 4, then 14, 15, 16, then 26, 27, 28."],
                  "2, 3, 4 and 14, 15, 16 and so on; a new set occurs every 12 numbers"),
              FIO("FiO4.q13", "Figure it Out (%s, question 13)" % FIO4,
                  "Choose any 3 numbers. When is their sum divisible by 3? Explore all possible cases and generalise.",
                  ["Look at the remainders of the three numbers on division by 3: each is 0, 1 or 2.",
                   "The sum is divisible by 3 when the remainders add to 0, 3 or 6.",
                   "That happens when all three remainders are the same, as in 4 + 7 + 10 = 21, or all different, as in "
                   "3 + 4 + 5 = 12.",
                   "In every other case it is not, as in 1 + 2 + 4 = 7."],
                  "When the three numbers leave the same remainder on division by 3, or three different remainders")],
          misconceptions=["M_REMAINDER_FORM"])],
    key_terms=["remainder", "algebraic expression", "LCM"]))
