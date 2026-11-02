# -*- coding: utf-8 -*-
"""Topics T13 to T21 (modules M3 and M4). Book section 3.3, pp 58 to 65, the summary and Puzzle Time."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T13 Patterns in HCF and LCM ==================================================
TOPICS.append(TOPIC(
    "T13", "M3", "Patterns in HCF and LCM", ["3.3"], "Analyze",
    "Students find pairs where the HCF is one of the numbers, state the pattern as a general statement and in algebra, "
    "and make general statements about the HCF and LCM of consecutive, even, odd and co-prime pairs.",
    "A general statement describes a pattern that holds in all cases; algebra writes it with letters.",
    [A("T13.C1", "When the HCF is one of the numbers", "Analyze",
       "Students find pairs whose HCF is one of the two numbers, state that one number must be a factor of the other, "
       "and write this pattern in algebra with n and 5n.",
       textbook=["3.3 Patterns, Properties, and a Pretty Procedure!",
                 "The HCF of 6 and 18 is 6, which is one of the two given numbers. Find more such number pairs where "
                 "the HCF is one of the two numbers.",
                 "How can we describe such pairs of numbers?",
                 "We can see that it happens when one number is a factor of the other. This also means the other "
                 "number will be a multiple of the first number!",
                 "Such a statement describing a pattern or a property that holds in all possible cases is called a "
                 "general statement. This process is called generalisation.",
                 "If n is a number, then any multiple of n can be written as a positive integer multiplied by n. For "
                 "example, if we take n and 5n (short for 5 × n), then 5n is a multiple of n, and n is a factor of 5n.",
                 "The HCF of n and 5n = n.",
                 "For number pairs satisfying this property (i.e., one of the numbers is the HCF), (a) if m is a "
                 "number, what could be the other number? (b) if 7k is a number, what could be the other number?"],
       teach=["Predict first: the HCF of 6 and 18 is 6. Will the HCF of 5 and 20 be 5? Of 9 and 27?",
              "Pairs like these have one number that is a factor of the other, and so the other is a multiple of it.",
              "A statement true for all such pairs is a general statement. Algebra writes it with a letter: for n and "
              "5n the HCF is n."],
       examples=[
           WE("Find three more pairs where the HCF is one of the two numbers, and describe all such pairs.",
              ["Try 5 and 20: the factors of 5 are 1, 5 and both go into 20, so the HCF is 5.",
               "Try 9 and 27: the HCF is 9. Try 4 and 28: the HCF is 4.",
               "In each pair the smaller number divides the larger one.",
               "So the HCF is one of the numbers exactly when one number is a factor of the other.",
               "In algebra: for n and any multiple such as 5n, the HCF is n."],
              "The HCF is one of the numbers exactly when one number is a factor of the other; for n and 5n it is n",
              ncert=["3.3.pattern_hcf", "3.3.pattern_algebra"], fact="pattern_hcf", expect=[6, 18, 6]),
           WE("If m is one of the numbers in such a pair, what could the other number be? Do the same when 7k is one "
              "of the numbers.",
              ["The other number can be any multiple of m, such as 2m, 3m or 10m.",
               "It can also be a factor of m, since then m is the multiple.",
               "For 7k: the other number can be a multiple of 7k, such as 14k or 21k.",
               "It can also be a factor of 7k, such as 7 or k."],
              "(a) any multiple or factor of m (b) any multiple or factor of 7k, such as 14k or 7",
              ncert=["3.3.pattern_algebra"])],
       key_terms=["general statement", "generalisation"], misconceptions=["M_FACTOR_MULTIPLE"], minutes=10),
     A("T13.C2", "General statements about consecutive, even and co-prime pairs", "Analyze",
       "Students try examples for consecutive even, consecutive odd, consecutive and co-prime pairs, and explain why "
       "each HCF and LCM pattern holds using common factors and primes.",
       textbook=["Figure it Out: Make a general statement about the HCF for the following pairs of numbers. You "
                 "could consider examples before coming up with general statements. Look for possible explanations "
                 "of why they hold.",
                 "Share your observations with the class."],
       teach=["Predict first: the HCF of 8 and 10, and of 14 and 16. Are both the same? What about 9 and 11?",
              "Try several examples, notice what stays the same, then explain why using a common factor.",
              "Two consecutive numbers cannot share a factor bigger than 1, because a common factor would divide "
              "their difference, which is 1."],
       examples=[
           WE("Find the HCF of 8 and 10, 14 and 16, 9 and 11, 15 and 17, and 12 and 13. State what you notice.",
              ["8 and 10: the HCF is 2. 14 and 16: the HCF is 2.",
               "Consecutive even numbers differ by 2, so a common factor divides 2, and both are even: the HCF is 2.",
               "9 and 11: the HCF is 1. 15 and 17: the HCF is 1.",
               "Consecutive odd numbers also differ by 2, but they are odd, so 2 is not a factor: the HCF is 1.",
               "12 and 13: the HCF is 1; consecutive numbers differ by 1, so the HCF is 1."],
              "Consecutive even numbers: HCF 2; consecutive odd numbers: HCF 1; consecutive numbers: HCF 1",
              fact="consecutive_hcf", expect=[2, 1, 1])],
       key_terms=["consecutive", "co-prime"], misconceptions=["M_COPRIME_ONE_FACTOR"], minutes=10),
     DOER("T13.C3", "Practice: explore pairs of numbers", "pattern_explorer", "Analyze",
          "Students generate many pairs of a chosen type, read the HCF and LCM for each, and state and explain a general "
          "statement for consecutive, even, odd, multiple and co-prime pairs.",
          ["Try several pairs before stating a pattern.",
           "A pattern is a general statement only if you can explain why it always holds.",
           "Co-prime pairs have HCF 1 and LCM equal to their product."],
          items=[FIO("3.3.FiO1", "Figure it Out (patterns), Q1",
                     "Make a general statement about the HCF for the following pairs of numbers. You could consider "
                     "examples before coming up with general statements. Look for possible explanations of why they "
                     "hold. (a) Two consecutive even numbers (b) Two consecutive odd numbers (c) Two even numbers "
                     "(d) Two consecutive numbers (e) Two co-prime numbers",
                     ["(a) 4 and 6, 10 and 12: HCF 2. Both are even and they differ by 2, so the HCF is 2.",
                      "(b) 5 and 7, 11 and 13: HCF 1. They differ by 2 but are odd, so 2 is not a common factor.",
                      "(c) 6 and 10, 8 and 12: the HCF is always even, at least 2, because 2 divides both.",
                      "(d) 7 and 8, 20 and 21: HCF 1, since a common factor divides the difference 1.",
                      "(e) Co-prime numbers have no common factor other than 1, so the HCF is 1."],
                     "(a) 2 (b) 1 (c) even, at least 2 (d) 1 (e) 1", expect=[2, 1, 2, 1, 1], tool="pattern_explorer"),
                FIO("3.3.FiO2", "Figure it Out (patterns), Q2",
                    "The LCM of 3 and 24 is 24 (it is one of the two given numbers). (a) Find more such number pairs "
                    "where the LCM is one of the two numbers. (b) Make a general statement about such numbers. "
                    "Describe such number pairs using algebra.",
                    ["(a) 5 and 20: LCM 20. 4 and 12: LCM 12. 7 and 14: LCM 14.",
                     "(b) The LCM is one of the numbers when one number is a factor of the other, so the other is a "
                     "multiple of it.",
                     "In algebra the pair is n and kn, where k is a positive whole number, and the LCM is kn."],
                    "(a) for example 5, 20 and 4, 12 (b) one number is a factor of the other; the pair n, kn has LCM kn",
                    expect=[20, 12], tool="pattern_explorer"),
                FIO("3.3.FiO3", "Figure it Out (patterns), Q3",
                    "Make a general statement about the LCM for the following pairs of numbers. You could consider "
                    "examples before coming up with these general statements. Look for possible explanations of why "
                    "they hold. (a) Two multiples of 3 (b) Two consecutive even numbers (c) Two consecutive numbers "
                    "(d) Two co-prime numbers",
                    ["(a) 6 and 9: LCM 18. Both are multiples of 3, so the LCM is also a multiple of 3.",
                     "(b) 4 and 6: LCM 12. 6 and 8: LCM 24. Their HCF is 2, so the LCM is the product divided by 2.",
                     "(c) 7 and 8: LCM 56. Consecutive numbers are co-prime, so the LCM is their product.",
                     "(d) 9 and 10: LCM 90. Co-prime numbers share no prime, so the LCM is their product."],
                    "(a) a multiple of 3 (b) product ÷ 2 (c) their product (d) their product", expect=[18, 12, 56, 90], tool="pattern_explorer")],
          ncert=["3.3.FiO1", "3.3.FiO2", "3.3.FiO3"], misconceptions=["M_COPRIME_ONE_FACTOR", "M_LCM_PRODUCT"])]))

# ============================== T14 Doubling and common multipliers ==========================================
TOPICS.append(TOPIC(
    "T14", "M3", "Doubling and Common Multipliers", ["3.3"], "Analyze",
    "Students explore what doubling both numbers does to the HCF, explain it using prime factors, find the HCF of two "
    "multiples of the same number, and decide when the HCF equals the common multiplier.",
    "Multiplying both numbers by the same amount multiplies the HCF by that amount; a common multiplier divides the HCF.",
    [A("T14.C1", "What happens to the HCF when both numbers are doubled", "Analyze",
       "Students double pairs of numbers, see that the HCF also doubles, and explain this using the extra prime 2 that "
       "both numbers gain and that joins the largest common subpart.",
       textbook=["What happens to the HCF of two numbers if both numbers are doubled? Take some pairs of numbers and "
                 "explore. Are you able to see why the HCF will also double?",
                 "If both numbers are doubled, then both numbers get an extra factor of 2 in their prime factors. This "
                 "2 will be included as a factor in the largest common subpart, and so the HCF will double. For "
                 "example, consider the numbers 270 and 50.",
                 "270 = 2 × 3 × 3 × 3 × 5, 50 = 2 × 5 × 5, HCF = 2 × 5 = 10",
                 "Let us double these numbers to get 540 and 100. 540 = 2 × 2 × 3 × 3 × 3 × 5, 100 = 2 × 2 × 5 × 5, "
                 "HCF = 2 × 2 × 5 = 20."],
       teach=["Predict first: the HCF of 12 and 18 is 6. What will the HCF of 24 and 36 be?",
              "Doubling both numbers gives each an extra prime 2. That extra 2 is common to both, so it joins the HCF.",
              "So the HCF doubles."],
       examples=[
           WE("Find the HCF of 270 and 50, and then of the doubled numbers 540 and 100. What do you see?",
              ["270 = 2 × 3 × 3 × 3 × 5 and 50 = 2 × 5 × 5, so the HCF is 2 × 5 = 10.",
               "540 = 2 × 2 × 3 × 3 × 3 × 5 and 100 = 2 × 2 × 5 × 5, so the HCF is 2 × 2 × 5 = 20.",
               "The HCF changed from 10 to 20, so it doubled.",
               "Both numbers gained one extra 2, and that 2 lies in the largest common subpart."],
              "The HCF of 270 and 50 is 10 and of 540 and 100 is 20; it doubles", ncert=["3.3.double"],
              fact="double", expect=[10, 20])],
       key_terms=["HCF", "prime factorisation"], minutes=8),
     A("T14.C2", "Multiples of the same number: is the HCF the common multiplier?", "Analyze",
       "Students find the HCF of two multiples of 14 and of four more pairs sharing a common multiplier, and say when "
       "the HCF equals the common multiplier.",
       textbook=["Consider the following two multiples of 14: 14 × 6, 14 × 9. What is their HCF?",
                 "Clearly, 14 is a common factor. Is it also the highest common factor? To see it, let us calculate "
                 "the prime factorisations.",
                 "14 × 6 = 2 × 7 × 2 × 3, 14 × 9 = 2 × 7 × 3 × 3. HCF = 14 × 3 = 42.",
                 "Here are some more numbers where both numbers are multiples of the same number. Find their HCF: "
                 "(a) 18 × 10, 18 × 15 (b) 10 × 38, 10 × 21 (c) 5 × 13, 5 × 20 (d) 12 × 16, 12 × 20",
                 "In which of these cases is the HCF the same as the common multiplier, like problem (b) where the "
                 "HCF is 10? Explore a few more examples of this type to understand when this happens."],
       teach=["Predict first: 14 × 6 and 14 × 9 share the factor 14. Is the HCF exactly 14, or more?",
              "The HCF is the common multiplier times the HCF of the other two factors. Here 6 and 9 share a 3, so "
              "the HCF is 14 × 3.",
              "The HCF equals the common multiplier exactly when the other two factors are co-prime."],
       examples=[
           WE("Find the HCF of 14 × 6 and 14 × 9.",
              ["14 × 6 = 2 × 7 × 2 × 3 and 14 × 9 = 2 × 7 × 3 × 3.", "Both contain 2 × 7 = 14 and also a 3.",
               "The HCF is 14 × 3 = 42, which is more than 14."],
              "42", ncert=["3.3.multiples14"], fact="multiples14", expect=[84, 126, 42]),
           WE("Find the HCF of (a) 18 × 10 and 18 × 15, (b) 10 × 38 and 10 × 21, (c) 5 × 13 and 5 × 20, "
              "(d) 12 × 16 and 12 × 20. In which is the HCF the common multiplier?",
              ["(a) The other factors 10 and 15 share 5, so the HCF is 18 × 5 = 90.",
               "(b) The other factors 38 and 21 share nothing, so the HCF is 10.",
               "(c) The other factors 13 and 20 share nothing, so the HCF is 5.",
               "(d) The other factors 16 and 20 share 4, so the HCF is 12 × 4 = 48.",
               "The HCF equals the common multiplier in (b) and (c), where the other factors are co-prime."],
              "(a) 90 (b) 10 (c) 5 (d) 48; the HCF is the common multiplier in (b) and (c)",
              ncert=["3.3.common_mult"], fact="common_mult", expect=[90, 10, 5, 48])],
       key_terms=["common multiplier", "co-prime"], misconceptions=["M_COPRIME_ONE_FACTOR"], minutes=10),
     DOER("T14.C3", "Practice: common multipliers and the HCF", None, "Analyze",
          "Students scale a pair by a common multiplier, explain why the HCF scales with it, and decide whether the HCF equals "
          "the multiplier by testing whether the remaining factors are co-prime.",
          ["Both numbers scaled by k have an HCF k times as big.",
           "The HCF equals the common multiplier only when the other factors are co-prime."])]))

# ============================== T15 Common division method ===================================================
TOPICS.append(TOPIC(
    "T15", "M3", "The Common Division Method", ["3.3"], "Apply",
    "Students read the common division method, use it to get the HCF from the divisors and the LCM from the divisors "
    "and the last row, and see why larger common divisors first give the same result faster.",
    "Divide both numbers by common factors until none is left; the HCF is the product of the divisors, the LCM adds the "
    "last row.",
    [A("T15.C1", "Reading the common division method and finding the HCF", "Apply",
       "Students explain the common division steps for 84 and 180, see that the divisors multiply to the HCF, and use the steps to "
       "find the HCF in two more cases.",
       textbook=["Efficient Procedures for HCF and LCM",
                 "See the procedure on the right. Can you explain how it has been carried out? The ladder: 84, 180 "
                 "divided by 2 gives 42, 90; divided by 2 gives 21, 45; divided by 3 gives 7, 15.",
                 "This is similar to the procedure for prime factorisation. At each step, the two numbers are divided "
                 "by a common prime factor, and the two quotients are written down in the next row. This continues "
                 "till we get two numbers that do not have any common prime factors.",
                 "How do we use this to find the HCF of 84 and 180? Explore. [Hint: Observe that 84 = 2 × 2 × 3 × 7, "
                 "and 180 = 2 × 2 × 3 × 15 similar to prime factorisation]",
                 "Find the HCF in the following cases. HCF = 2 × 5 × 5 × 3 for 300 and 150. HCF = 2 × 5 × 7 for 630 "
                 "and 770."],
       teach=["Predict first: in the ladder for 84 and 180 we divide by 2, 2, 3. What might these divisors give?",
              "The divisors 2, 2, 3 are the common primes. Their product is the largest common subpart, so the HCF is "
              "2 × 2 × 3 = 12.",
              "Stop when the last two numbers share no prime."],
       examples=[
           WE("Use the ladder for 84 and 180 to find the HCF.",
              ["Divide both by 2: 42 and 90.", "Divide both by 2: 21 and 45.", "Divide both by 3: 7 and 15.",
               "7 and 15 share no prime, so stop.", "HCF = 2 × 2 × 3 = 12."],
              "12", ncert=["3.3.div_explore"], fact="div_84_180", expect=[84, 180, 12]),
           WE("Use the ladders for 300 and 150, and for 630 and 770, to find the HCF in each case.",
              ["300, 150: divide by 2 to get 150, 75; by 5 to get 30, 15; by 5 to get 6, 3; by 3 to get 2, 1.",
               "HCF = 2 × 5 × 5 × 3 = 150.",
               "630, 770: divide by 2 to get 315, 385; by 5 to get 63, 77; by 7 to get 9, 11.",
               "9 and 11 share no prime, so HCF = 2 × 5 × 7 = 70."],
              "150 and 70", ncert=["3.3.div_hcf"], fact="div_hcf", expect=[150, 70])],
       key_terms=["common division method"], misconceptions=["M_PROCEDURE"], minutes=10),
     A("T15.C2", "The same ladder gives the LCM", "Apply",
       "Students find the LCM from the division steps by multiplying the divisors with the last row, and explain why this "
       "contains both numbers and is the smallest such number.",
       textbook=["This procedure not only gives the HCF but can also be used to find the LCM! Can you see how?",
                 "LCM = 2 × 5 × 5 × 3 × 2 × 1 for 300 and 150, LCM = 2 × 5 × 7 × 3 × 3 × 11 for 630 and 770.",
                 "Why are these the LCMs? [Hint: Will the product of the factors marked as the LCM of 300 and 150 "
                 "contain the prime factorisations of both 300 and 150? Is this the smallest such number?]"],
       teach=["Predict first: the divisors give the HCF. What do you get if you multiply them by the last row as "
              "well?",
              "The divisors are common, and the last row holds what each number has left over. Multiplying all of "
              "them gives a number containing both factorisations.",
              "Nothing in the product is extra, so it is the smallest such number: the LCM."],
       examples=[
           WE("Use the ladders to find the LCM of 300 and 150, and of 630 and 770.",
              ["300, 150: the divisors are 2, 5, 5, 3 and the last row is 2, 1.",
               "LCM = 2 × 5 × 5 × 3 × 2 × 1 = 300.",
               "630, 770: the divisors are 2, 5, 7 and the last row is 9, 11.",
               "LCM = 2 × 5 × 7 × 9 × 11 = 6930."],
              "300 and 6930", ncert=["3.3.div_lcm"], fact="div_lcm", expect=[300, 6930])],
       key_terms=["LCM", "common division method"], misconceptions=["M_PROCEDURE"], minutes=8),
     A("T15.C3", "Guna and Anshu remove the bigger common factors first", "Evaluate",
       "Students check Guna's and Anshu's faster division steps for 300 and 150 and for 630 and 770, explain why any common "
       "divisor works, and use the faster steps on two new pairs.",
       textbook=["Guna says \"I found a better way to factorise to find HCF/LCM. This is faster than what was taught "
                 "in class!\"",
                 "\"For the numbers 300 and 150, I can first directly divide both numbers by 50. The HCF will be "
                 "50 × 3. The LCM will be 50 × 3 × 2 × 1\"",
                 "Anshu also tried to remove the bigger common factors. \"For 630 and 770, I will divide both numbers "
                 "by 10 first. Now, I can divide them by 7. The HCF will be 10 × 7 = 70. The LCM will be 10 × 7 × 9 × "
                 "11 = 6930\".",
                 "Can you see why this works? We need not restrict ourselves to dividing only one prime factor at a "
                 "time. Both numbers can be divided by whatever common factor we are able to identify.",
                 "You can try this method for these pairs of numbers. (a) 90 and 150 (b) 84 and 132"],
       teach=["Predict first: dividing 300 and 150 by 50 in one step. Will the HCF still be found correctly?",
              "Dividing by 50 is the same as dividing by 2, 5 and 5 one after another. The product of the divisors "
              "is unchanged.",
              "Any common factor can be used. Keep going until the last two numbers are co-prime."],
       examples=[
           WE("Use bigger common divisors to find the HCF and LCM of 90 and 150, and of 84 and 132.",
              ["90 and 150: divide both by 10 to get 9 and 15, then by 3 to get 3 and 5.",
               "HCF = 10 × 3 = 30, and LCM = 10 × 3 × 3 × 5 = 450.",
               "84 and 132: divide both by 12 to get 7 and 11, which are co-prime.",
               "HCF = 12, and LCM = 12 × 7 × 11 = 924."],
              "(a) HCF 30, LCM 450 (b) HCF 12, LCM 924", ncert=["3.3.guna_anshu", "3.3.try_pairs"],
              fact="try_pairs", expect=[30, 450, 12, 924])],
       key_terms=["common division method"], misconceptions=["M_PROCEDURE"], minutes=10),
     DOER("T15.C4", "Practice: climb the division ladder", "division_ladder", "Apply",
          "Students climb the common division method for pairs of numbers, choosing any common divisor each step, and "
          "read the HCF from the divisors and the LCM from the divisors with the last row.",
          ["Divide both numbers by any common factor and write the quotients in the next row.",
           "Stop when the last two numbers are co-prime.",
           "HCF is the product of the divisors; LCM multiplies the divisors by the last row."])]))

# ============================== T16 HCF x LCM = product ======================================================
TOPICS.append(TOPIC(
    "T16", "M3", "HCF × LCM = Product", ["3.3"], "Analyze",
    "Students show the LCM is never greater than the product, discover that HCF × LCM equals the product of two "
    "numbers, explain why using primes, and test whether the rule holds for three numbers.",
    "For two numbers, the HCF times the LCM equals their product; common primes split between them.",
    [A("T16.C1", "Which is greater: the LCM or the product?", "Analyze",
       "Students compare the LCM with the product for several pairs and explain why the LCM is never greater, because "
       "the product is itself a common multiple.",
       textbook=["Property Involving both the HCF and the LCM",
                 "Which is greater, the LCM of two numbers or their product?",
                 "You could analyse the above statement using examples. Then try to reason or prove, why the LCM is "
                 "never greater than the product of the numbers. [Hint: Is the product also a common multiple of the "
                 "two numbers?]"],
       teach=["Predict first: the LCM of 6 and 8 is 24, and the product is 48. Which is greater? Is it ever the "
              "other way?",
              "The product is a multiple of each number, so it is a common multiple. The LCM is the lowest common "
              "multiple, so it cannot be greater.",
              "The two are equal when the numbers are co-prime."],
       examples=[
           WE("Compare the LCM with the product for 6 and 8, and for 7 and 9. Explain why the LCM is never greater.",
              ["6 and 8: LCM 24, product 48, so the LCM is smaller.", "7 and 9: LCM 63, product 63, so they are equal.",
               "The product of two numbers is a multiple of both, so it is a common multiple.",
               "The LCM is the lowest common multiple, so it is at most the product."],
              "The LCM is never greater than the product; they are equal for co-prime numbers", ncert=["3.3.lcm_vs_product"],
              fact="lcm_vs_prod", expect=[24, 48, 63, 63])],
       key_terms=["LCM", "product"], misconceptions=["M_LCM_PRODUCT"], minutes=8),
     A("T16.C2", "Discovering HCF × LCM = Product", "Analyze",
       "Students find the LCM of 105 and 95, see the product is the LCM times the HCF, test three more pairs, and "
       "state HCF × LCM = product of the two numbers.",
       textbook=["There is an interesting relation between the product of two numbers and their HCF and LCM.",
                 "Consider the numbers 105 and 95. Find their LCM. Factorising them into their primes: 105 = 3 × 5 × "
                 "7, 95 = 5 × 19, LCM = 3 × 5 × 7 × 19.",
                 "Let us consider the product in the factorised form: 105 × 95 = 3 × 5 × 5 × 7 × 19. Is the LCM a "
                 "factor of the product? If yes, what should it be multiplied with to get the product? It can be seen "
                 "that 105 × 95 = LCM × 5.",
                 "Explore whether the LCM is a factor of the product in the following cases. If yes, identify the "
                 "number that the LCM should be multiplied by to get the product. Do you see any pattern? Use these "
                 "numbers: (a) 45, 105 (b) 275, 352 (c) 222, 370",
                 "Do you see that, in each case, the number by which the LCM is multiplied to get the product is "
                 "actually the HCF? Thus, our observations seem to suggest the following: HCF × LCM = Product of the "
                 "two numbers."],
       teach=["Predict first: for 105 and 95 the LCM is 3 × 5 × 7 × 19. What must it be multiplied by to give the "
              "product?",
              "It is multiplied by 5, which is the HCF of 105 and 95.",
              "Test more pairs. The same thing happens every time: HCF × LCM = the product of the two numbers."],
       examples=[
           WE("For 105 and 95, find the HCF, the LCM and the product, and check that the product equals HCF × LCM.",
              ["105 = 3 × 5 × 7 and 95 = 5 × 19.", "HCF = 5 and LCM = 3 × 5 × 7 × 19 = 1995.",
               "Product = 105 × 95 = 9975.", "HCF × LCM = 5 × 1995 = 9975.", "So the product equals HCF × LCM."],
              "HCF 5, LCM 1995, product 9975 = 5 × 1995", ncert=["3.3.hcf_lcm_105_95"], fact="hl_105_95",
              expect=[5, 1995, 9975]),
           WE("Find the number the LCM must be multiplied by to get the product, for (a) 45 and 105, (b) 275 and "
              "352, (c) 222 and 370.",
              ["(a) HCF 15, LCM 315, and 315 × 15 = 4725 = 45 × 105.",
               "(b) HCF 11, LCM 8800, and 8800 × 11 = 96800 = 275 × 352.",
               "(c) HCF 74, LCM 1110, and 1110 × 74 = 82140 = 222 × 370.",
               "In every case the number is the HCF."],
              "(a) 15 (b) 11 (c) 74; each is the HCF", ncert=["3.3.hcf_lcm_try"], fact="hl_try",
              expect=[15, 11, 74])],
       key_terms=["HCF", "LCM", "product"], misconceptions=["M_LCM_PRODUCT"], minutes=10),
     A("T16.C3", "Why it works, and what about three numbers", "Evaluate",
       "Students explain HCF × LCM = product by splitting each prime between the HCF and the LCM, and show with a "
       "counter-example that the rule fails for three numbers.",
       textbook=["Why does this happen? Can you give an explanation or proof? [Hint: Consider the prime "
                 "factorisation of the given numbers. Among their prime factors, some are common to both "
                 "factorisations, and the rest occur in only one of them. Between the HCF and the LCM, see how the "
                 "common and non-common prime factors get distributed. In the product, observe how these two kinds "
                 "of prime factors occur. Compare them.]",
                 "Explore whether this property holds when 3 numbers are considered."],
       teach=["Predict first: for a prime that is in both numbers, the HCF takes the smaller count and the LCM takes "
              "the larger. Together how many of that prime is that?",
              "Together they have every copy of that prime from both numbers, exactly as in the product. A prime in "
              "only one number goes only to the LCM, also as in the product.",
              "With three numbers the minimum and maximum leave out the middle count, so the rule can fail."],
       examples=[
           WE("Explain with 12 = 2 × 2 × 3 and 18 = 2 × 3 × 3 why HCF × LCM equals the product.",
              ["The prime 2: counts 2 and 1. The HCF takes 1 and the LCM takes 2, together 3 twos, as in the product.",
               "The prime 3: counts 1 and 2. The HCF takes 1 and the LCM takes 2, together 3 threes, as in the product.",
               "HCF = 2 × 3 = 6 and LCM = 2 × 2 × 3 × 3 = 36.", "HCF × LCM = 6 × 36 = 216 = 12 × 18."],
              "Each prime's smaller count goes to the HCF and its larger count to the LCM, so together they use "
              "exactly the primes of the product: 6 × 36 = 216 = 12 × 18", ncert=["3.3.hcf_lcm_why"],
              fact="hl_why", expect=[6, 36, 216]),
           WE("Does HCF × LCM equal the product for three numbers? Test 4, 6 and 10.",
              ["4 = 2 × 2, 6 = 2 × 3 and 10 = 2 × 5.", "HCF = 2 and LCM = 2 × 2 × 3 × 5 = 60.",
               "HCF × LCM = 2 × 60 = 120.", "The product is 4 × 6 × 10 = 240.",
               "120 is not 240, so the rule does not hold for three numbers."],
              "No: for 4, 6 and 10, HCF × LCM is 120 but the product is 240", ncert=["3.3.three_numbers"],
              fact="three_nums", expect=[2, 60, 240])],
       key_terms=["HCF", "LCM", "counter-example"], misconceptions=["M_PROCEDURE", "M_MIN_MAX"], minutes=10),
     DOER("T16.C4", "Practice: check the product rule", "product_checker", "Analyze",
          "Students compute the HCF, the LCM and the product for pairs, check HCF × LCM, use it to find a missing "
          "value, and test the rule on three numbers.",
          ["The HCF times the LCM equals the product of two numbers.",
           "If three of the four quantities are known, the fourth follows.",
           "The rule is not true for three numbers."])]))

# ============================== T17 Applications, set one ====================================================
TOPICS.append(TOPIC(
    "T17", "M3", "Applying HCF and LCM, Part One", ["3.3"], "Apply",
    "Students decide whether a situation asks for splitting into equal parts, which uses the HCF, or for events meeting "
    "again, which uses the LCM. They read both values from prime factorisations and solve the first seven book problems.",
    "Splitting into equal parts points to the HCF; events lining up again point to the LCM.",
    [A("T17.C1", "Split or meet? Choosing HCF or LCM", "Analyze",
       "Students read a situation, decide whether it asks to split into equal pieces or to find when events meet, and "
       "so choose the HCF or the LCM, then compute it for two stories.",
       textbook=[],
       teach=["Predict first: two bells ring every 12 and 18 minutes. Is the time they ring together an HCF or an LCM "
              "question?",
              "Cutting or packing into equal pieces asks for a common factor, and the largest piece gives the HCF.",
              "Waiting for repeating events to line up asks for a common multiple, and the first time gives the LCM."],
       examples=[
           WE("Two bells ring every 12 and 18 minutes. They ring together now. After how many minutes will they ring "
              "together again?",
              ["Bell one rings at the multiples of 12 and bell two at the multiples of 18.",
               "They ring together at a common multiple, and the first time is the LCM.",
               "12 = 2 × 2 × 3 and 18 = 2 × 3 × 3, so the LCM is 2 × 2 × 3 × 3 = 36."],
              "After 36 minutes", fact="bells", expect=[12, 18, 36]),
           WE("Two ribbons, 24 m and 36 m long, are cut into equal pieces of the greatest whole length with nothing "
              "left. Find the length of a piece and the number of pieces.",
              ["Equal pieces with nothing left means a common factor, and the greatest gives the HCF.",
               "24 = 2 × 2 × 2 × 3 and 36 = 2 × 2 × 3 × 3, so the HCF is 2 × 2 × 3 = 12.",
               "Pieces: 24 ÷ 12 = 2 and 36 ÷ 12 = 3, so 2 + 3 = 5 pieces."],
              "Each piece is 12 m and there are 5 pieces", fact="ribbons", expect=[12, 5])],
       key_terms=["HCF", "LCM"], misconceptions=["M_HCF_BIG", "M_LCM_PRODUCT"], minutes=10),
     A("T17.C2", "Reading HCF and LCM from prime factorisations", "Apply",
       "Students find the HCF and LCM of numbers given as products of primes, taking minimum and maximum counts, and "
       "say why a product of primes is a multiple or factor of another.",
       textbook=[],
       teach=["Predict first: is 2 × 3 × 3 a factor of 2 × 2 × 3 × 3 × 5? Compare the counts of each prime.",
              "For a factor, every prime must appear at most as many times as in the bigger number. For a multiple, at "
              "least as many.",
              "The HCF uses the minimum counts and the LCM the maximum counts, so the answers can stay in prime form."],
       examples=[
           WE("Find the HCF and LCM of 2 × 2 × 3 × 5 and 2 × 3 × 3 × 7, giving the answers as prime "
              "factorisations and as numbers.",
              ["Primes: 2, 3, 5, 7.", "Minimum counts: 2 once, 3 once, and 5 and 7 are not in both.",
               "HCF = 2 × 3 = 6.", "Maximum counts: 2 twice, 3 twice, 5 once, 7 once.",
               "LCM = 2 × 2 × 3 × 3 × 5 × 7 = 1260."],
              "HCF = 2 × 3 = 6 and LCM = 2 × 2 × 3 × 3 × 5 × 7 = 1260", fact="pf_hcf_lcm", expect=[6, 1260])],
       key_terms=["HCF", "LCM", "prime factorisation"], misconceptions=["M_MIN_MAX"], minutes=8),
     DOER("T17.C3", "Practice: apply HCF and LCM", "hcf_or_lcm", "Apply",
          "Students read each problem, decide whether it asks for the HCF or the LCM, solve it from prime "
          "factorisations, and check that the answer suits the story.",
          ["Equal pieces and no leftovers point to the HCF.", "Meeting again points to the LCM.",
           "Use prime factorisations for larger numbers."],
          items=[
              FIO("3.3.end1", "End of chapter Figure it Out, Q1",
                  "In the two rows below, colours repeat as shown. When will the blue stars meet next? "
                  "(Row one repeats yellow, green, orange, blue, pink, grey. Row two repeats green, orange, yellow, "
                  "blue.)",
                  ["Row one repeats every 6 stars with blue at the 4th, 10th, 16th star, and so on.",
                   "Row two repeats every 4 stars with blue at the 4th, 8th, 12th, 16th star, and so on.",
                   "Both are blue at the 4th star, and the next shared position is 12 stars later, since the LCM of "
                   "6 and 4 is 12.",
                   "4 + 12 = 16, so the blue stars meet next at the 16th star."],
                  "At the 16th star", expect=[16], tool="hcf_or_lcm"),
              FIO("3.3.end2", "End of chapter Figure it Out, Q2",
                  "(a) Is 5 × 7 × 11 × 11 a multiple of 5 × 7 × 7 × 11 × 2? (b) Is 5 × 7 × 11 × 11 a factor of "
                  "5 × 7 × 7 × 11 × 2?",
                  ["(a) A multiple must contain the primes of the other number. 5 × 7 × 7 × 11 × 2 has two 7s and a 2, "
                   "but 5 × 7 × 11 × 11 has only one 7 and no 2. So it is not a multiple.",
                   "(b) A factor must use each prime no more often than the bigger number. 5 × 7 × 11 × 11 has two "
                   "11s, but 5 × 7 × 7 × 11 × 2 has only one 11. So it is not a factor."],
                  "(a) No (b) No", expect=[0]),
              FIO("3.3.end3", "End of chapter Figure it Out, Q3",
                  "Find the HCF and LCM of the following (state your answers in the form of prime factorisations): "
                  "(a) 3 × 3 × 5 × 7 × 7 and 12 × 7 × 11 (b) 45 and 36",
                  ["(a) 12 = 2 × 2 × 3, so 12 × 7 × 11 = 2 × 2 × 3 × 7 × 11.",
                   "Minimum counts: 3 once, 7 once. HCF = 3 × 7 = 21.",
                   "Maximum counts: 2 twice, 3 twice, 5 once, 7 twice, 11 once. "
                   "LCM = 2 × 2 × 3 × 3 × 5 × 7 × 7 × 11 = 97020.",
                   "(b) 45 = 3 × 3 × 5 and 36 = 2 × 2 × 3 × 3. HCF = 3 × 3 = 9. LCM = 2 × 2 × 3 × 3 × 5 = 180."],
                  "(a) HCF = 3 × 7 = 21, LCM = 2 × 2 × 3 × 3 × 5 × 7 × 7 × 11 = 97020 "
                  "(b) HCF = 3 × 3 = 9, LCM = 2 × 2 × 3 × 3 × 5 = 180", expect=[21, 97020, 9, 180], tool="hcf_or_lcm"),
              FIO("3.3.end4", "End of chapter Figure it Out, Q4",
                  "Find two numbers whose HCF is 1 and LCM is 66.",
                  ["HCF 1 means the numbers are co-prime, so the LCM is their product.",
                   "So the product is 66 = 2 × 3 × 11, and the two numbers share no prime.",
                   "Split the primes between them: 1 and 66, 2 and 33, 3 and 22, 6 and 11."],
                  "For example 6 and 11 (also 1 and 66, 2 and 33, 3 and 22)", expect=[66]),
              FIO("3.3.end5", "End of chapter Figure it Out, Q5",
                  "A cowherd took all his cows to graze in the fields. The cows came to a crossing with 3 gates. An "
                  "equal number of cows passed through each gate. Later at another crossing with 5 gates again an "
                  "equal number of cows passed through each gate. The same happened at the third crossing with 7 "
                  "gates. If the cowherd had less than 200 cows, how many cows did he have? (Based on the folklore "
                  "mathematics from Karnataka.)",
                  ["An equal number through each of 3 gates means the number of cows is a multiple of 3.",
                   "In the same way it is a multiple of 5 and of 7.",
                   "So it is a common multiple of 3, 5 and 7, and the lowest is 3 × 5 × 7 = 105.",
                   "The next common multiple is 210, which is more than 200, so he had 105 cows."],
                  "105 cows", expect=[105], tool="hcf_or_lcm"),
              FIO("3.3.end6", "End of chapter Figure it Out, Q6",
                  "The length, width, and height of a box are 12 cm, 18 cm, and 36 cm respectively. Which of the "
                  "following sized cubes can be packed in this box without leaving gaps? (a) 9 cm (b) 6 cm (c) 4 cm "
                  "(d) 3 cm (e) 2 cm",
                  ["The cube side must divide 12, 18 and 36, so it is a common factor of all three.",
                   "The HCF of 12, 18 and 36 is 6, so the common factors are 1, 2, 3 and 6.",
                   "9 does not divide 12, and 4 does not divide 18.", "So cubes of 6 cm, 3 cm and 2 cm fit."],
                  "(b) 6 cm, (d) 3 cm and (e) 2 cm", expect=[6, 3, 2], tool="hcf_or_lcm"),
              FIO("3.3.end7", "End of chapter Figure it Out, Q7",
                  "Among the numbers below, which is the largest number that perfectly divides both 306 and 36? "
                  "(a) 36 (b) 612 (c) 18 (d) 3 (e) 2 (f) 360",
                  ["The largest number dividing both is the HCF of 306 and 36.",
                   "306 = 2 × 3 × 3 × 17 and 36 = 2 × 2 × 3 × 3.", "HCF = 2 × 3 × 3 = 18.",
                   "18 is among the choices, so the answer is (c)."],
                  "(c) 18", expect=[18], tool="hcf_or_lcm")],
          ncert=["3.3.end1", "3.3.end2", "3.3.end3", "3.3.end4", "3.3.end5", "3.3.end6", "3.3.end7"],
          misconceptions=["M_HCF_BIG", "M_LCM_PRODUCT"])]))

# ============================== T18 Applications, set two ====================================================
TOPICS.append(TOPIC(
    "T18", "M3", "Applying HCF and LCM, Part Two", ["3.3"], "Apply",
    "Students use the LCM to solve remainder and catching-up problems, reason about the LCM of two primes, and add "
    "fractions with unlike denominators using the LCM, completing the last six book problems.",
    "Remainders, chases and fraction sums all turn into LCM and HCF questions once the repeating pattern is seen.",
    [A("T18.C1", "Remainders and catching up", "Apply",
       "Students find the smallest number divisible by several numbers that leaves a given remainder when divided by "
       "another, and the number of leaps for a chaser who gains a fixed distance each leap.",
       textbook=[],
       teach=["Predict first: the smallest number divisible by 5 and 6 is 30. Does it leave remainder 4 on division by "
              "7?",
              "Numbers divisible by 5 and 6 are multiples of the LCM, 30. Check each multiple against the remainder.",
              "For a chase, find how much the chaser gains in one leap, then divide the head start by the gain."],
       examples=[
           WE("Find the smallest number that is divisible by 5 and 6 but leaves a remainder of 4 when divided "
              "by 7.",
              ["Numbers divisible by 5 and 6 are multiples of their LCM, 30.", "30 = 7 × 4 + 2, so the remainder is 2.",
               "60 = 7 × 8 + 4, so the remainder is 4.", "So the smallest such number is 60."],
              "60", fact="remainder", expect=[60]),
           WE("A cat chases a mouse that has a head start of 48 feet. The cat jumps 7 feet every time the mouse "
              "jumps 5 feet. In how many leaps does the cat catch the mouse?",
              ["In each leap the cat gains 7 − 5 = 2 feet.", "It must gain 48 feet, so it needs 48 ÷ 2 = 24 leaps.",
               "Check: the cat goes 24 × 7 = 168 feet and the mouse 48 + 24 × 5 = 168 feet."],
              "24 leaps", fact="chase", expect=[24])],
       key_terms=["LCM", "remainder"], misconceptions=["M_LCM_PRODUCT"], minutes=10),
     A("T18.C2", "Adding fractions with the LCM of the denominators", "Apply",
       "Students use the LCM of the denominators as a common denominator, convert each fraction, and add them "
       "efficiently.",
       textbook=[],
       teach=["Predict first: to add 1/6 and 1/4, which common denominator is lowest? Is it 24 or 12?",
              "The lowest common denominator is the LCM of the denominators, which keeps numbers small.",
              "Rewrite each fraction over the LCM, add the numerators, and simplify."],
       examples=[
           WE("Add 1/6 and 1/4 using the LCM of the denominators.",
              ["The LCM of 6 and 4 is 12.", "1/6 = 2/12 and 1/4 = 3/12.", "2/12 + 3/12 = 5/12."],
              "5/12", fact="frac_add", expect=[12, 5])],
       key_terms=["LCM", "common denominator"], minutes=8),
     DOER("T18.C3", "Practice: more problems with HCF and LCM", None, "Apply",
          "Students solve remainder, chase, fraction-sum and prime-LCM problems, choosing HCF or LCM themselves, and "
          "check each answer against the story.",
          ["Divisible by several numbers means a multiple of their LCM.",
           "A chase is solved by the gain in one step.",
           "Use the LCM of the denominators to add fractions."],
          items=[
              FIO("3.3.end8", "End of chapter Figure it Out, Q8",
                  "Find the smallest number that is divisible by 3, 4, 5 and 7, but leaves a remainder of 10 when "
                  "divided by 11.",
                  ["A number divisible by 3, 4, 5 and 7 is a multiple of their LCM, 3 × 4 × 5 × 7 = 420.",
                   "Multiples of 420: 420, 840, 1260, 1680, 2100.",
                   "Check remainders on division by 11: 420 gives 2, 840 gives 4, 1260 gives 6, 1680 gives 8, 2100 "
                   "gives 10.",
                   "So the smallest such number is 2100."],
                  "2100", expect=[2100]),
              FIO("3.3.end9", "End of chapter Figure it Out, Q9",
                  "Children are playing 'Fire in the Mountain'. When the number 6 was called out, no one got out. "
                  "When the number 9 was called out, no one got out. But when the number 10 was called out, some "
                  "people got out. How many children could have been playing initially? (a) 72 (b) 90 (c) 45 (d) 3 "
                  "(e) 36 (f) None of these",
                  ["No one got out on 6 and on 9, so the children split into groups of 6 and of 9 with none left over.",
                   "So the number is a common multiple of 6 and 9, that is a multiple of their LCM, 18.",
                   "Some got out on 10, so the number is not a multiple of 10.",
                   "Multiples of 18 among the options: 72 and 36 (90 is also a multiple of 10, so nobody would be out on 10).",
                   "So 72 and 36 fit."],
                  "(a) 72 and (e) 36", expect=[72, 36]),
              FIO("3.3.end10", "End of chapter Figure it Out, Q10",
                  "Tick the correct statement(s). The LCM of two different prime numbers (m, n) can be: (a) Less than "
                  "both numbers (b) In between the two numbers (c) Greater than both numbers (d) Less than m × n "
                  "(e) Greater than m × n",
                  ["Two different primes are co-prime, so their LCM is their product m × n.",
                   "m × n is bigger than both m and n, since each is at least 2.",
                   "So (c) is true, and (a), (b), (d) and (e) are false."],
                  "(c) Greater than both numbers", expect=[0]),
              FIO("3.3.end11", "End of chapter Figure it Out, Q11",
                  "A dog is chasing a rabbit that has a head start of 150 feet. It jumps 9 feet every time the rabbit "
                  "jumps 7 feet. In how many leaps does the dog catch up with the rabbit?",
                  ["In each leap the dog gains 9 − 7 = 2 feet.", "It must gain 150 feet, so it needs 150 ÷ 2 = 75 "
                   "leaps.", "Check: the dog goes 75 × 9 = 675 feet and the rabbit 150 + 75 × 7 = 675 feet."],
                  "75 leaps", expect=[75]),
              FIO("3.3.end12", "End of chapter Figure it Out, Q12",
                  "What is the smallest number that is a multiple of 1, 2, 3, 4, 5, 6, 8, 9, 10? Do you remember the "
                  "answer from Grade 6, Chapter 5?",
                  ["The smallest such number is the LCM of 1, 2, 3, 4, 5, 6, 8, 9 and 10.",
                   "The highest powers: 2 three times (from 8), 3 twice (from 9), 5 once (from 5 and 10).",
                   "LCM = 2 × 2 × 2 × 3 × 3 × 5 = 360."],
                  "360", expect=[360]),
              FIO("3.3.end13", "End of chapter Figure it Out, Q13",
                  "Here is a problem posed by the ancient Indian Mathematician Mahaviracharya (850 C.E.). Add "
                  "together 8/15, 1/20, 7/36, 11/63 and 1/21. What do you get? How can we find this sum efficiently?",
                  ["The LCM of the denominators 15, 20, 36, 63 and 21 gives the lowest common denominator.",
                   "15 = 3 × 5, 20 = 2 × 2 × 5, 36 = 2 × 2 × 3 × 3, 63 = 3 × 3 × 7, 21 = 3 × 7.",
                   "LCM = 2 × 2 × 3 × 3 × 5 × 7 = 1260.",
                   "8/15 = 672/1260, 1/20 = 63/1260, 7/36 = 245/1260, 11/63 = 220/1260, 1/21 = 60/1260.",
                   "672 + 63 + 245 + 220 + 60 = 1260, so the sum is 1260/1260 = 1."],
                  "The sum is 1", expect=[1260, 1])],
          ncert=["3.3.end8", "3.3.end9", "3.3.end10", "3.3.end11", "3.3.end12", "3.3.end13"],
          misconceptions=["M_LCM_PRODUCT", "M_HCF_BIG"])]))

# ============================== T19 Chapter review ===========================================================
TOPICS.append(TOPIC(
    "T19", "M4", "Chapter Review: HCF, LCM and Their Methods", ["Review"], "Evaluate",
    "Students recall the tile, toran and sweet shop stories, choose between HCF and LCM, pick the method that suits "
    "the numbers, apply the relation HCF × LCM = product, and solve a closing challenge.",
    "One consolidated practice covering concepts, procedures and applications from the whole chapter.",
    [A("T19.C1", "Choosing the right idea and the right method", "Evaluate",
       "Students decide whether a problem needs the HCF or the LCM, choose listing, prime factorisation or the "
       "common division method as suits the numbers, and check with HCF × LCM = product.",
       textbook=[],
       teach=["Predict first: which would you use to find when two cycles meet, and which to cut equal pieces?",
              "Choose a method: list for small numbers, prime factorisation for bigger ones, the division ladder when "
              "both values are wanted.",
              "Check with HCF × LCM = the product of the two numbers."],
       examples=[
           WE("Find the HCF and LCM of 42 and 70, and check with the product rule.",
              ["42 = 2 × 3 × 7 and 70 = 2 × 5 × 7.", "Minimum counts: 2 once, 7 once, so HCF = 2 × 7 = 14.",
               "Maximum counts: 2, 3, 5 and 7 once each, so LCM = 2 × 3 × 5 × 7 = 210.",
               "Check: 14 × 210 = 2940 and 42 × 70 = 2940."],
              "HCF 14, LCM 210, and 14 × 210 = 2940 = 42 × 70", fact="review", expect=[14, 210, 2940])],
       key_terms=["HCF", "LCM"], misconceptions=["M_HCF_BIG", "M_LCM_PRODUCT", "M_MIN_MAX"], minutes=10),
     A("T19.C2", "Tricky cases and a closing challenge", "Evaluate",
       "Students handle co-prime pairs, one number a factor of the other, and consecutive numbers quickly, and solve "
       "a closing problem that combines splitting and meeting.",
       textbook=[],
       teach=["Predict first: what are the HCF and LCM of 8 and 15? Of 7 and 21? Of 12 and 13?",
              "Co-prime pairs: HCF 1 and LCM the product. A factor and its multiple: the HCF is the factor and the "
              "LCM is the multiple.",
              "Challenge: use both ideas in one problem."],
       examples=[
           WE("Find the HCF and LCM of 8 and 15, of 7 and 21, and of 12 and 13 without long working.",
              ["8 and 15 are co-prime: HCF 1 and LCM 8 × 15 = 120.",
               "7 is a factor of 21: HCF 7 and LCM 21.",
               "12 and 13 are consecutive, so co-prime: HCF 1 and LCM 12 × 13 = 156."],
              "(8, 15): 1 and 120; (7, 21): 7 and 21; (12, 13): 1 and 156", fact="quick_cases",
              expect=[1, 120, 7, 21, 1, 156])],
       key_terms=["co-prime"], misconceptions=["M_COPRIME_ONE_FACTOR"], minutes=8),
     DOER("T19.C3", "Pull it together and do it: the chapter practice", None, "Evaluate",
          "Students solve mixed questions on common factors, primes, HCF, LCM, patterns, the common division method and "
          "applications, choosing the idea and the method that suit each question.",
          ["Decide HCF or LCM from the story.", "Pick the method that suits the numbers.",
           "Check with the product rule or by dividing."])]))

# ============================== T20 Mystery Colours ==========================================================
TOPICS.append(TOPIC(
    "T20", "M4", "Puzzle Time: Mystery Colours", ["Puzzle Time"], "Analyze",
    "Students decode how each coloured ring around a page number shows the prime factorisation of that number, and extend the colour scheme to the numbers 101 to 110.",
    "The coloured ring around each page number hides its prime factorisation; decode the colour for each prime.",
    [A("T20.C1", "Decode the colour scheme", "Analyze",
       "",
       textbook=["Mystery Colours!",
                 "You might have noticed and wondered about these different circle designs around the page numbers "
                 "on each page! The picture below shows all the designs for the numbers from 1 to 100.",
                 "Try to decode the colour scheme for each number. There are several interesting patterns here. "
                 "Share your observations with your classmates.",
                 "Extending this scheme, colour the page numbers from 101 to 110."],
       teach=["Look at the rings for 2, 3, 5 and 7, then for 4, 6 and 12. Which colour goes with which prime?",
              "The ring is split into equal arcs, one for each prime in the prime factorisation, each coloured by its "
              "prime. Primes from 11 on share one colour, and 1 has its own.",
              "Use the rule to draw the rings for 101 to 110."],
       ncert=["puzzle.colours"], key_terms=["prime factorisation"], enrichment=True, minutes=6),
     DOER("T20.C2", "Practice: decode the rings", None, "Analyze",
          "",
          ["The number of arcs is the number of primes in the prime factorisation.",
           "Each arc takes the colour of its prime."],
          enrichment=True)]))

# ============================== T21 Summary ==================================================================
TOPICS.append(TOPIC(
    "T21", "M4", "Summary: Finding Common Ground", ["Summary"], "Remember",
    None,
    "Tiles and HCF, toran and LCM, prime factorisation, patterns, the division ladder and the product rule in one place.",
    [A("T21.C1", "What we found about HCF and LCM", "Remember",
       "Students restate how the HCF and LCM come from prime factorisations, recall the tile, toran and sweet shop "
       "stories, and name the patterns and the efficient procedure found in this chapter.",
       textbook=["Summary",
                 "Last year, we looked at common multiples, and common factors, and were also introduced to the "
                 "amazing world of primes!",
                 "In this chapter, we learnt a method to find the prime factorisation of a number.",
                 "Finding all the factors of a number from its prime factorisation is easy but quite tedious, we have "
                 "to list every possible subpart!",
                 "The Highest Common Factor (HCF) is the highest among all the common factors of a group of numbers. "
                 "Every common factor is contained in the prime factorisation of the number. To find the HCF, we "
                 "include the minimum number of occurrences of each prime across the prime factorisation of all the "
                 "numbers.",
                 "The Lowest Common Multiple (LCM) is the lowest among all the common multiples of a group of "
                 "numbers. Every common multiple contains the prime factorisation of the numbers. To find the LCM, "
                 "we include the highest number of occurrences of each prime across the prime factorisations of all "
                 "the numbers.",
                 "We explored more about HCF and LCM; we discovered related properties and patterns when numbers are "
                 "consecutive, even, co-prime, etc.",
                 "We learnt a procedure to get both the HCF and the LCM at the same time! We also saw how to make "
                 "this even quicker!",
                 "We learned some terms that are used when discussing mathematics, such as 'conjecture' and "
                 "'generalisation'.",
                 "The largest prime found so far has 4,10,24,320 digits! It was discovered on October 12, 2024."],
       teach=["Our opening guess is settled: the largest tile that fits a 12 ft by 16 ft room is the HCF, 4 ft.",
              "Toran and sweets: the first length or day that fits both is the LCM.",
              "Still open for you: can you explain why HCF × LCM fails for three numbers, and find the HCF and LCM "
              "of 56 and 84 with the division ladder?"],
       ncert=["summary"], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
