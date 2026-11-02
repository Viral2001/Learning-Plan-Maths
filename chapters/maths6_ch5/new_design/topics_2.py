# -*- coding: utf-8 -*-
"""Topics T7 to T11 (modules M3 and M4): book sections 5.4 and 5.5."""
from topics_common import A, DOER, TOPIC, BOOK_TEXT, book, fio, we, wem

TOPICS = []

# ============================== T7 Prime factorisation (5.4 first half) ======================================
TOPICS.append(TOPIC(
    "T7", "M3", "Prime Factorisation", ["5.4"], "Apply",
    "Students see why one factor pair cannot show every factor, write a number as a product of primes with a "
    "factor tree, and explain why the primes are the same whichever way and in whichever order they are found.",
    "Break a number into factors until all are prime; the primes found are the same every time, in any order.",
    [A("T7.C1", "One factor pair is not enough", "Analyze",
       "Students explain why writing 56 as 14 times 4 does not show all the factors of 56, and why a systematic "
       "way of checking factors is needed.",
       textbook=book("5.4", "Checking if two numbers are co-prime"),
       teach=["Predict first: Anshu writes 56 = 14 × 4 and 63 = 21 × 3 and says they have no common factor. Is he "
              "right?",
              "Guna writes 56 = 7 × 8 and 63 = 9 × 7. Now 7 is common, so 56 and 63 are not co-prime.",
              "Anshu's pair only shows that 14 and 4 are factors of 56; it does not list all the factors.",
              "One way of splitting a number can hide a factor, so we need a systematic approach."],
       examples=[we("5.4.q1"), we("5.4.q2")],
       key_terms=["factor", "co-prime"], misconceptions=["M_ONE_PAIR_ENOUGH"], minutes=10),
     A("T7.C2", "The prime factorisation is unique", "Understand",
       "Students write a number as a product of primes, see that different ways of splitting give the same primes "
       "in the same counts, and that the order of multiplying does not matter.",
       textbook=book("5.4", "Prime factorisation") + book("5.4", "Does the order matter?"),
       teach=["Predict first: split 63 as 9 × 7, then 9 = 3 × 3. Another way gives 3 × 7 × 3. Are they different?",
              "Both have two 3s and one 7. Multiplying in a different order gives the same number.",
              "36 broken four ways always gives two 2s and two 3s.",
              "Every number above 1 has one prime factorisation, apart from the order of the primes."],
       examples=[we("5.4.q3"), we("5.4.q4"), we("5.4.q5")],
       key_terms=["prime factorisation"], misconceptions=["M_TREE_DIFFERENT", "M_ORDER_MATTERS",
                                                          "M_STOP_AT_COMPOSITE"], minutes=10),
     A("T7.C3", "Prime factorisation of a product", "Apply",
       "Students find the prime factorisation of a product by putting together the factorisations of its two "
       "factors, and check by multiplying back.",
       textbook=book("5.4", "Prime factorisation of a product of two numbers", stop=6),
       teach=["Predict first: 72 = 12 × 6. What primes does 72 have?",
              "12 = 2 × 2 × 3 and 6 = 2 × 3. Put them together: 2 × 2 × 3 × 2 × 3.",
              "In any order, that is 2 × 2 × 2 × 3 × 3.",
              "Multiply back: 8 × 9 = 72. The 2s and 3s in 72 are the 2s and 3s of 12 and 6 together."],
       examples=[we("5.4.q6"), we("5.4.q7"), we("5.4.q8")],
       key_terms=["prime factorisation"], misconceptions=["M_STOP_AT_COMPOSITE"], minutes=10),
     DOER("T7.C4", "Pull it together and do it: Factor Tree Builder", "factor_tree", "Apply",
          "Students split numbers into factor trees on the tool, compare different trees of one number, and write "
          "prime factorisations, even of products, without multiplying first.",
          ["Keep splitting until every leaf is prime.",
           "Different trees of one number end in the same primes.",
           "The factorisation of a product is the factorisations of its factors put together."],
          items=[fio("5.4.FiO1.Q1", tool="factor_tree",
                     answer="64 = 2 × 2 × 2 × 2 × 2 × 2; 104 = 2 × 2 × 2 × 13; 105 = 3 × 5 × 7; "
                            "243 = 3 × 3 × 3 × 3 × 3; 320 = 2 × 2 × 2 × 2 × 2 × 2 × 5; 141 = 3 × 47; "
                            "1728 = 2 × 2 × 2 × 2 × 2 × 2 × 3 × 3 × 3; 729 = 3 × 3 × 3 × 3 × 3 × 3 (six 3s); "
                            "1024 = ten 2s multiplied; 1331 = 11 × 11 × 11; 1000 = 2 × 2 × 2 × 5 × 5 × 5."),
                 fio("5.4.FiO1.Q2", tool="factor_tree"), fio("5.4.FiO1.Q3", tool="factor_tree"),
                 fio("5.4.FiO1.Q4"), fio("5.4.FiO1.Q5")],
          misconceptions=["M_TREE_DIFFERENT", "M_STOP_AT_COMPOSITE"])]))

# ============================== T8 Using prime factorisation (5.4 second half) ===============================
TOPICS.append(TOPIC(
    "T8", "M3", "Using Prime Factorisation", ["5.4"], "Apply",
    "Students use prime factorisations to decide whether two numbers are co-prime and whether one number is "
    "divisible by another, without listing all the factors or dividing.",
    "No common prime factor means co-prime; if all the primes of one number are inside the other's, it divides it.",
    [A("T8.C1", "Co-prime from prime factors", "Apply",
       "Students write two numbers as products of primes and conclude they are co-prime when no prime appears in "
       "both, giving the reason.",
       textbook=book("5.4", "Using prime factorisation to check if two numbers are co-prime"),
       teach=["Predict first: 80 = 2 × 2 × 2 × 2 × 5 and 63 = 3 × 3 × 7. Are they co-prime?",
              "They share no prime. If they had a common factor above 1, a prime would divide both.",
              "So no common prime means no common factor above 1: co-prime.",
              "56 = 2 × 2 × 2 × 7 and 63 = 3 × 3 × 7 share 7, so they are not co-prime."],
       examples=[we("5.4.q9"), we("5.4.ex1"), we("5.4.ex2")],
       key_terms=["co-prime", "prime factorisation"], misconceptions=["M_COPRIME_BOTH_PRIME"], minutes=10),
     A("T8.C2", "Divisibility from prime factors", "Apply",
       "Students check whether one number divides another by seeing whether the prime factorisation of the second "
       "number sits inside that of the first.",
       textbook=book("5.4", "Using prime factorisation to check if one number is divisible by another", stop=10),
       teach=["Predict first: is 168 divisible by 12? 168 = 2 × 2 × 2 × 3 × 7 and 12 = 2 × 2 × 3.",
              "All the primes of 12 are in 168, so 168 = 12 × 14. It is divisible.",
              "75 = 3 × 5 × 5 and 21 = 3 × 7. 7 is not in 75, so 75 is not divisible by 21.",
              "42 = 2 × 3 × 7 and 12 = 2 × 2 × 3: 42 has one 2, 12 needs two, so 42 is not divisible by 12."],
       examples=[we("5.4.q10"), we("5.4.ex3"), we("5.4.ex4"), we("5.4.ex5")],
       key_terms=["divisible", "prime factorisation"], misconceptions=["M_SHARED_PRIME_DIVIDES"], minutes=10),
     DOER("T8.C3", "Pull it together and do it: Factorisation Compare", "prime_compare", "Analyze",
          "Students compare the prime factorisations of two numbers on the tool and decide whether they are "
          "co-prime and whether one divides the other.",
          ["No common prime means the numbers are co-prime.",
           "All primes of the smaller number inside the bigger one means it divides it.",
           "A shared prime alone is not enough for divisibility."],
          items=[fio("5.4.FiO2.Q1", tool="prime_compare"), fio("5.4.FiO2.Q2", tool="prime_compare"),
                 fio("5.4.FiO2.Q3", tool="prime_compare"),
                 fio("5.4.FiO2.Q4",
                     steps=["Two different primes, such as 2 and 3 or 3 and 11, have no common factor other than 1.",
                            "A prime with itself, such as 3 and 3, shares the factor 3."],
                     answer="Yes for two different primes; not for the same prime twice, such as 3 and 3.")],
          misconceptions=["M_SHARED_PRIME_DIVIDES", "M_COPRIME_BOTH_PRIME"])]))

# ============================== T9 Divisibility by 10, 5 and 2 (5.5) =========================================
TOPICS.append(TOPIC(
    "T9", "M4", "Divisibility by 10, 5 and 2", ["5.5"], "Apply",
    "Students use the last digit to test divisibility by 10, 5 and 2 without long division, and give the reason "
    "from the pattern of the multiples.",
    "Multiples of 10 end in 0, multiples of 5 in 0 or 5, and multiples of 2 in 0, 2, 4, 6 or 8.",
    [A("T9.C1", "Divisibility by 10", "Understand",
       "Students list the multiples of 10, see that all end in 0, and decide whether a number such as 125 or 8560 "
       "is divisible by 10 from its last digit alone.",
       textbook=book("5.5", None) + book("5.5", "Divisibility by 10"),
       teach=["Predict first: which of 2 to 10 divide 8560? Is there a quick way without long division?",
              "Multiples of 10: 10, 20, 30, 40 and on. Every one ends in 0.",
              "125 does not end in 0; the list jumps from 120 to 130, so 125 is not a multiple of 10.",
              "8560 ends in 0, so it is divisible by 10."],
       examples=[we("5.5.q1",
                    steps=["10 divides 8560 because it ends in 0; 5 and 2 divide it for the same reason.",
                           "4 and 8 divide it too: 60 is a multiple of 4 and 560 is a multiple of 8.",
                           "3, 6, 7 and 9 do not divide 8560 exactly."],
                    answer="2, 4, 5, 8 and 10."),
                 wem(["5.5.q2", "5.5.q3"],
                     q="List the multiples of 10 and say whether 125 is one of them.",
                     steps=["10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130: each ends in 0.",
                            "The list goes from 120 to 130 and skips 125."],
                     answer="125 is not a multiple of 10 because it does not end in 0."),
                 wem(["5.5.q4", "5.5.q5"],
                     q="Is 8560 divisible by 10? Do you agree that numbers divisible by 10 are those that end "
                       "with 0?",
                     steps=["8560 ends in 0, like every multiple of 10.",
                            "A number ending in 0 is a whole number of tens, so it is a multiple of 10."],
                     answer="Yes, 8560 is divisible by 10; a number is divisible by 10 exactly when it ends in 0.")],
       key_terms=["divisible", "last digit"], misconceptions=["M_FIVE_ONLY_ENDS_FIVE"], minutes=10),
     A("T9.C2", "Divisibility by 5", "Understand",
       "Students list the multiples of 5, notice that the last digit is 0 or 5, and use it to test any number for "
       "divisibility by 5.",
       textbook=book("5.5", "Divisibility by 5"),
       teach=["Predict first: 5, 10, 15, 20, 25. What do you notice about the last digit?",
              "It alternates between 5 and 0.",
              "A number ending in 0 or 5 is a multiple of 5; any other last digit is not.",
              "Keeko thinks only numbers ending in 5 are multiples of 5. What about 20?"],
       examples=[wem(["5.5.q6", "5.5.q7"],
                     q="Look at the multiples of 5. What is the last digit? What is the largest number less than "
                       "399 divisible by 5, and is 8560 divisible by 5?",
                     steps=["5, 10, 15, 20, 25: the last digit is always 0 or 5.",
                            "The largest number below 399 that ends in 0 or 5 is 395.",
                            "8560 ends in 0, so it is divisible by 5."],
                     answer="Last digit 0 or 5; 395; yes."),
                 we("5.5.q8",
                    steps=["A multiple of 5 ends in 0 or 5.", "A number ending in 0 or 5 is a multiple of 5."],
                    answer="Yes, agree: a number is divisible by 5 exactly when its last digit is 0 or 5.")],
       key_terms=["divisible", "last digit"], misconceptions=["M_FIVE_ONLY_ENDS_FIVE"], minutes=8),
     A("T9.C3", "Divisibility by 2", "Understand",
       "Students list the multiples of 2, notice the last digit is 0, 2, 4, 6 or 8, and use it to test a number for "
       "divisibility by 2.",
       textbook=book("5.5", "Divisibility by 2"),
       teach=["Predict first: 2, 4, 6, 8, 10, 12, 14. What do the last digits do?",
              "They repeat 2, 4, 6, 8, 0: only the even digits.",
              "A number ending in 0, 2, 4, 6 or 8 is a multiple of 2.",
              "So 682 is divisible by 2 without any long division."],
       examples=[wem(["5.5.q9", "5.5.q10", "5.5.q11"],
                     q="What is the pattern in the last digit of the multiples of 2? Is 682 divisible by 2? Is "
                       "8560?",
                     steps=["2, 4, 6, 8, 10, 12, 14, 16, 18, 20: the last digit is 2, 4, 6, 8 or 0, repeating.",
                            "682 ends in 2, an even digit, so it is divisible by 2.",
                            "8560 ends in 0, an even digit, so it is divisible by 2."],
                     answer="Last digit 0, 2, 4, 6 or 8; both 682 and 8560 are divisible by 2."),
                 wem(["5.5.q12", "5.5.q13"],
                     q="Do you agree that numbers divisible by 2 end in 0, 2, 4, 6 or 8? List the multiples of 2 "
                       "between 399 and 411.",
                     steps=["Every multiple of 2 ends in an even digit, and every number ending in an even digit "
                            "is a multiple of 2.",
                            "From 400 to 410 the even numbers are 400, 402, 404, 406, 408, 410."],
                     answer="Yes, agree; 400, 402, 404, 406, 408, 410.")],
       key_terms=["divisible", "even number"], misconceptions=["M_FIVE_ONLY_ENDS_FIVE"], minutes=8),
     DOER("T9.C4", "Pull it together and do it: Last Digit Lens", "digit_lens", "Apply",
          "Students test numbers for 10, 5 and 2 with the last digit on the tool, check by division, and find "
          "remainders from the last digit.",
          ["Divisible by 10 means the last digit is 0.",
           "Divisible by 5 means the last digit is 0 or 5.",
           "Divisible by 2 means the last digit is 0, 2, 4, 6 or 8."],
          items=[fio("5.5.FiO.Q3"), fio("5.5.FiO.Q4", tool="digit_lens")],
          misconceptions=["M_FIVE_ONLY_ENDS_FIVE"])]))

# ============================== T10 Divisibility by 4 (5.5) ==================================================
TOPICS.append(TOPIC(
    "T10", "M4", "Divisibility by 4", ["5.5"], "Apply",
    "Students see that the last digit cannot decide divisibility by 4, find that the last two digits can, and "
    "use that to test numbers.",
    "A number is divisible by 4 when the number made of its last two digits is divisible by 4.",
    [A("T10.C1", "The last digit is not enough for 4", "Analyze",
       "Students list the multiples of 4, test whether the last digit decides divisibility, and see with 12 and 22 "
       "that it does not.",
       textbook=book("5.5", "Divisibility by 4", stop=4),
       teach=["Predict first: the multiples of 4 are 4, 8, 12, 16, 20. Is there a last-digit pattern like for 2 "
              "and 5?",
              "Their last digits are 4, 8, 2, 6, 0, and these repeat, but they are all even digits.",
              "12 and 22 have the same last digit 2; 12 is a multiple of 4 and 22 is not.",
              "So the last digit alone cannot test divisibility by 4."],
       examples=[we("5.5.q14",
                    steps=["Multiples of 4: 4, 8, 12, 16, 20, 24, 28, 32.",
                           "12 is a multiple of 4 and 22 is not, yet both end in 2.",
                           "So the last digit alone cannot decide divisibility by 4."],
                    answer="No: the last digit alone does not work; 12 and 22 end in the same digit.")],
       key_terms=["divisible"], misconceptions=["M_LAST_DIGIT_FOR_4"], minutes=8),
     A("T10.C2", "The last two digits decide 4", "Analyze",
       "Students list multiples of 4 in different hundreds and thousands, and see that the last two digits stay "
       "multiples of 4, so 100 does not change divisibility.",
       textbook=book("5.5", "Divisibility by 4", start=4, stop=6),
       teach=["Predict first: which numbers from 330 to 340 are multiples of 4?",
              "332 and 336. From 1730 to 1740: 1732 and 1736. From 2030 to 2040: 2032 and 2036.",
              "The last two digits are 32 and 36 each time, and both are multiples of 4.",
              "100 is a multiple of 4, so the hundreds and above never change the answer."],
       examples=[wem(["5.5.q15", "5.5.q16"],
                     q="Make a list of the multiples of 4 from 1 to 200. Find the multiples of 4 between 330 and "
                       "340, between 1730 and 1740, and between 2030 and 2040.",
                     steps=["Between 330 and 340: 332 and 336.",
                            "Between 1730 and 1740: 1732 and 1736.",
                            "Between 2030 and 2040: 2032 and 2036.",
                            "In each case the last two digits are 32 or 36, which are multiples of 4."],
                     answer="A number is a multiple of 4 when the number formed by its last two digits is.")],
       key_terms=["divisible", "last two digits"], misconceptions=["M_LAST_DIGIT_FOR_4"], minutes=10),
     A("T10.C3", "Testing a number for 4", "Apply",
       "Students test numbers for divisibility by 4 using the last two digits, and judge three statements about the "
       "rule with examples.",
       textbook=book("5.5", "Divisibility by 4", start=6),
       teach=["Predict first: is 8536 divisible by 4? Do you need to divide 8536?",
              "Look only at 36. 36 = 4 × 9, so 36 is a multiple of 4.",
              "So 8536 is divisible by 4.",
              "If the last two digits are not a multiple of 4, the number is not."],
       examples=[we("5.5.q17"), we("5.5.q18")],
       key_terms=["divisible", "last two digits"], misconceptions=["M_LAST_DIGIT_FOR_4"], minutes=8),
     DOER("T10.C4", "Pull it together and do it: Last Two and Three Digits", "digit_lens_48", "Apply",
          "Students use the lens on the tool to test numbers for 4, apply the rule to leap years and palindromes, "
          "and explore even and odd sums.",
          ["Look at the last two digits for 4.",
           "A number is divisible by 4 if the number formed by its last two digits is.",
           "The same idea with three digits works for 8."],
          items=[fio("5.5.FiO.Q1", tool="digit_lens_48",
                     steps=["2024, 2028, ..., 2096 are the multiples of 4 from 2024 to 2099.",
                            "2096 minus 2024 is 72, and 72 ÷ 4 gives 18 steps, so there are 19 years.",
                            "No century year lies between 2024 and 2099, so the century rule changes nothing."],
                     answer="b. 19 leap years (2024, 2028, ..., 2096). Part a depends on the year of birth."),
                 fio("5.5.FiO.Q2", tool="digit_lens_48",
                     steps=["The first and last digits are equal, so the last digit is even for divisibility by 4: "
                            "the number starts with 2, 4, 6 or 8.",
                            "Largest: 8 b b 8 with b as big as possible and the last two digits a multiple of 4. "
                            "88 is a multiple of 4, but 98 is not, so b = 8: 8888.",
                            "Smallest: 2 b b 2 with b as small as possible. 02 is not a multiple of 4, but 12 is, "
                            "so b = 1: 2112."],
                     answer="Largest 8888, smallest 2112 (the printed answers 9999 and 1001 are odd numbers).")],
          misconceptions=["M_LAST_DIGIT_FOR_4"])]))

# ============================== T11 Divisibility by 8 (5.5) ==================================================
TOPICS.append(TOPIC(
    "T11", "M4", "Divisibility by 8", ["5.5"], "Apply",
    "Students see that the last two digits are not enough for 8, find that the last three digits are, and combine "
    "the tests to check divisibility by several numbers.",
    "A number is divisible by 8 when the number made of its last three digits is divisible by 8.",
    [A("T11.C1", "Two digits are not enough for 8", "Analyze",
       "Students test whether the last two digits decide divisibility by 8 by comparing numbers that end in the "
       "same two digits, and see that they do not.",
       textbook=book("5.5", "Divisibility by 8", stop=1),
       teach=["Predict first: can the last two digits decide divisibility by 8, like they did for 4?",
              "108 and 208 both end in 08, and 08 is a multiple of 8.",
              "But 208 = 8 × 26 is a multiple of 8, and 108 is not: 8 × 13 = 104, 8 × 14 = 112.",
              "100 is not a multiple of 8, so the hundreds digit matters."],
       examples=[we("5.5.q19",
                    steps=["108 and 208 end in the same two digits, 08.",
                           "208 = 8 × 26, so 208 is divisible by 8; 108 is between 104 = 8 × 13 and 112 = 8 × 14, "
                           "so 108 is not.",
                           "So the last two digits cannot decide divisibility by 8. 1000 = 8 × 125 is a multiple "
                           "of 8, so three digits are needed."],
                    answer="No: the last two digits are not enough for 8; the last three digits are needed.")],
       key_terms=["divisible"], misconceptions=["M_LAST_TWO_FOR_8"], minutes=8),
     A("T11.C2", "The last three digits decide 8", "Analyze",
       "Students list multiples of 8 in different thousands, see that the last three digits repeat, and state the "
       "rule that the last three digits decide divisibility by 8.",
       textbook=book("5.5", "Divisibility by 8", start=1, stop=2),
       teach=["Predict first: which numbers between 120 and 140 are multiples of 8?",
              "128 and 136. Between 1120 and 1140: 1128 and 1136. Between 3120 and 3140: 3128 and 3136.",
              "The last three digits are 128 and 136 every time.",
              "1000 is a multiple of 8, so the thousands never change the answer."],
       examples=[we("5.5.q20")],
       key_terms=["divisible", "last three digits"], misconceptions=["M_LAST_TWO_FOR_8"], minutes=8),
     A("T11.C3", "Making a multiple of 8", "Apply",
       "Students change the last digits of a number to make it divisible by 8 and judge statements about the "
       "last-three-digits rule.",
       textbook=book("5.5", "Divisibility by 8", start=2, stop=4),
       teach=["Predict first: change the last two digits of 8560 so that the number is a multiple of 8.",
              "The last three digits are 560 = 8 × 70, which is already a multiple of 8, so 8560 itself works.",
              "Keeping the hundreds digit 5, 552 = 8 × 69 also works, so 8552 is a multiple of 8.",
              "Only the last three digits matter, and the rule works both ways."],
       examples=[we("5.5.q21"), we("5.5.q22")],
       key_terms=["divisible", "last three digits"], misconceptions=["M_LAST_TWO_FOR_8"], minutes=8),
     DOER("T11.C4", "Pull it together and do it: Combining Tests", None, "Apply",
          "Students combine the tests for 2, 4, 5, 8 and 10 to check large numbers with the fewest tests, and "
          "build numbers with a given product.",
          ["8 covers 4 and 2, and 10 needs 2 and 5.",
           "5 and 8 together cover all of 2, 4, 5, 8 and 10.",
           "Factors of 10000 are only 2s and 5s, so a pair with no zero ending uses all the 2s in one number and all "
           "the 5s in the other."],
          items=[fio("5.5.FiO.Q5"), fio("5.5.FiO.Q6"), fio("5.5.FiO.Q7",
                     steps=["10000 is four 2s and four 5s multiplied together.",
                            "Put all the 2s in one number and all the 5s in the other: 2 × 2 × 2 × 2 is 16 and "
                            "5 × 5 × 5 × 5 is 625.",
                            "Neither 16 nor 625 ends in 0, and 16 × 625 = 10000."])],
          misconceptions=["M_LAST_TWO_FOR_8"])]))
