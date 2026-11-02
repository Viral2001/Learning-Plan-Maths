# -*- coding: utf-8 -*-
"""Topics T10 to T12 (module M2: common multiples and LCM). Book section 3.2, pp 55 to 58."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T10 Toran ====================================================================
TOPICS.append(TOPIC(
    "T10", "M2", "Anshu and Guna's Toran", ["3.2"], "Apply",
    "Students list the multiples of 6 and of 8 as possible toran lengths, find the lengths both can make, name the "
    "smallest as the LCM, and explain why no largest common multiple exists.",
    "A toran length both can make is a common multiple; the lowest common multiple is the shortest such toran.",
    [A("T10.C1", "Toran lengths from strips of 6 cm and 8 cm", "Apply",
       "Students list the multiples of 6 and 8, pick the toran lengths common to both lists, and identify 24 cm as the "
       "shortest toran both can stitch.",
       textbook=["3.2 Least, but not Last!",
                 "Anshu and Guna make torans out of strips of cloth. Multiple strips are placed one next to another "
                 "to make a toran. Anshu uses strips of length 6 cm and Guna uses strips of 8 cm length. If both have "
                 "to make torans of the same length, what is the smallest possible length, the torans could be? What "
                 "is the length of the shortest toran that they can both make?",
                 "Anshu uses cloth strips of 6 cm each. Any toran he makes will be a multiple of 6. So, the length of "
                 "the toran could be 6, 12, 18, 24, 30, 36, 42, 48, 54 cm, and so on.",
                 "Similarly, any toran Guna makes should be a multiple of 8. So, the length of the toran he makes "
                 "could be 8, 16, 24, 32, 40, 48, 56, 64, 72 cm, and so on.",
                 "From this, we can see that if both have to make torans of the same length, the length of the toran "
                 "should be a common multiple of 6 and 8."],
       teach=["Predict first: Anshu can make 6, 12, 18, and so on. Will Guna's lengths 8, 16, 24 ever meet them?",
              "List both sets of multiples side by side and look for lengths in both lists.",
              "A length in both lists is a common multiple, a toran both can make."],
       examples=[
           WE("Anshu's strips are 6 cm and Guna's are 8 cm. List the toran lengths each can make, and find the "
              "lengths both can make.",
              ["Anshu: 6, 12, 18, 24, 30, 36, 42, 48, 54.", "Guna: 8, 16, 24, 32, 40, 48, 56, 64, 72.",
               "Lengths in both lists: 24 and 48.", "So 24 cm and 48 cm are toran lengths both can stitch.",
               "24 is the smallest of them, so the shortest toran is 24 cm."],
              "Both can make 24 cm and 48 cm; the shortest toran is 24 cm", ncert=["3.2.toran"], fact="toran",
              expect=[6, 8, 24])],
       key_terms=["multiple", "common multiple"], misconceptions=["M_FACTOR_MULTIPLE"], minutes=10),
     A("T10.C2", "The Lowest Common Multiple, and why there is no largest", "Analyze",
       "Students define the LCM as the lowest common multiple, say why 24 is the LCM of 6 and 8, and explain why a "
       "largest common multiple cannot exist.",
       textbook=["From the two lists, we can see that 24 and 48 are two of the common multiples of 6 and 8. So, "
                 "24 cm and 48 cm are lengths of toran that Anshu and Guna can both stitch.",
                 "24 is the smallest among them. So, 24 cm is the length of the shortest toran that both can stitch. "
                 "24 is the lowest number among all the common multiples of 6 and 8.",
                 "What about the largest common multiple? Does such a number exist?"],
       teach=["The smallest of the common multiples is special: 24 is the lowest of all common multiples of 6 and 8.",
              "Predict first: after 48 comes 72, then 96. Where does the list of common multiples stop?",
              "Common multiples go on for ever, so there is no largest one. But there is always a lowest."],
       examples=[
           WE("Is there a largest common multiple of 6 and 8? Explain, and name the lowest.",
              ["The common multiples are 24, 48, 72, 96, and so on.",
               "Adding 24 to any common multiple gives a larger common multiple.",
               "So the list never ends and there is no largest common multiple.",
               "The lowest one is 24, which we call the LCM of 6 and 8."],
              "No largest common multiple exists; the LCM of 6 and 8 is 24", ncert=["3.2.toran_largest"])],
       key_terms=["LCM"], misconceptions=["M_LCM_BIG"], minutes=8),
     DOER("T10.C3", "Practice: build the toran", "toran_builder", "Apply",
          "Students lay strips of two lengths side by side to find the shortest equal toran, list common multiples on "
          "two rulers, and confirm that the LCM is the first match.",
          ["Multiples of a number are the lengths its strips can make.",
           "The first length that both rulers show is the LCM.",
           "Common multiples keep going, so there is no largest."])]))

# ============================== T11 Sweet shop and idli-vada =================================================
TOPICS.append(TOPIC(
    "T11", "M2", "Kabamai's Sweet Shop and Idli-Vada", ["3.2"], "Apply",
    "Students solve a repeating-days problem with multiples of 7 and 10, find the first common day, and use the same "
    "idea in the Idli-Vada game to show that the first number called out for both is always the LCM.",
    "A repeating event on two cycles first coincides at the LCM of the cycle lengths.",
    [A("T11.C1", "When Kabamai next gets free gajak", "Apply",
       "Students list the multiples of 7 and of 10 as days, find the first day common to both, and name 70 days as the "
       "LCM of 7 and 10.",
       textbook=["A sweet shop gives out free gajak to school children on Mondays. Today is a Monday and Kabamai "
                 "enjoyed eating the gajak. But she visits the sweet shop once every 10 days. When is the next time "
                 "she would be able to get free gajak from Sweet shop? (Answer in number of days.)",
                 "As we saw before, imagining or visualising the scenario helped us to see that it can be solved using "
                 "multiples of the strips' lengths.",
                 "Since the shop gives free sweets every Monday, it will give free sweets again after 7, 14, 21, 28, "
                 "35, 42, 49, 56, 63, 70, 77, ... days. These are multiples of 7.",
                 "Kabamai will arrive at the sweet shop again after 10, 20, 30, 40, 50, 60, 70, ... days. These are "
                 "multiples of 10.",
                 "When will Kabamai eat free sweets again? It will happen on days common to the sequences of multiples "
                 "above. It can be seen that this will first happen after 70 days.",
                 "Notice that, here too, 70 is the lowest among all the common multiples of 7 and 10.",
                 "For both these problems the solution was the lowest common multiple. The Lowest Common Multiple "
                 "(LCM) of two or more given numbers is the lowest (or smallest or least) of their common multiples."],
       teach=["Predict first: free gajak comes every 7 days and Kabamai visits every 10 days. Will they match on day "
              "14? On day 30?",
              "List the days of free sweets, the multiples of 7, and the days she visits, the multiples of 10.",
              "The first day in both lists is the answer, and it is the LCM."],
       examples=[
           WE("The shop gives free gajak every 7 days and Kabamai visits every 10 days. After how many days does she "
              "next get free gajak?",
              ["Free sweets after 7, 14, 21, 28, 35, 42, 49, 56, 63, 70 days.",
               "Kabamai visits after 10, 20, 30, 40, 50, 60, 70 days.",
               "The first day in both lists is 70.", "So she gets free gajak after 70 days, the LCM of 7 and 10."],
              "After 70 days", ncert=["3.2.sweet"], fact="sweet", expect=[7, 10, 70])],
       key_terms=["LCM", "multiple"], misconceptions=["M_LCM_PRODUCT"], minutes=10),
     A("T11.C2", "Idli-Vada: is the answer always the LCM?", "Analyze",
       "Students play Idli-Vada for four pairs, find the first number called out for both, and explain why this "
       "number is always the LCM of the two numbers.",
       textbook=["Do you remember the 'Idli-Vada' game from Grade 6 (see chapter 'Prime Time')? Two numbers are chosen "
                 "and whenever players come to their multiples, 'idli' or 'vada' should be called out depending on "
                 "whose multiple the number is. If the number happens to be a common multiple, then 'idli-vada' "
                 "should be called out. In each problem below, the two numbers corresponding to 'idli' and 'vada' are "
                 "given. Find the first number for which 'idli-vada' will be called out:",
                 "(a) 4 and 6 (b) 7 and 11 (c) 14 and 30 (d) 15 and 55",
                 "Is the answer always the LCM of the two numbers? Explain."],
       teach=["Predict first: for 4 and 6, will idli-vada be called at 6, at 12, or at 24?",
              "Idli-vada is called at a number that is a multiple of both, a common multiple.",
              "The first such number is the lowest common multiple, so the answer is always the LCM."],
       examples=[
           WE("Find the first number called idli-vada for 4 and 6, and for 7 and 11.",
              ["Multiples of 4: 4, 8, 12, 16.", "Multiples of 6: 6, 12, 18.", "The first common one is 12.",
               "Multiples of 7: 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77.", "Multiples of 11: 11, 22, 33, 44, 55, 66, 77.",
               "The first common one is 77."],
              "(a) 12 (b) 77", ncert=["3.2.idli_a", "3.2.idli_b"], fact="idli_ab", expect=[12, 77]),
           WE("Find the first number called idli-vada for 14 and 30, and for 15 and 55. Is it always the LCM?",
              ["Multiples of 14: 14, 28, 42, 56, 70, 84, 98, 112, 126, 140, 154, 168, 182, 196, 210.",
               "Multiples of 30: 30, 60, 90, 120, 150, 180, 210.", "The first common one is 210.",
               "Multiples of 15: 15, 30, 45, ... 165. Multiples of 55: 55, 110, 165.",
               "The first common one is 165.",
               "Idli-vada is called at the first common multiple, which by definition is the LCM, so yes."],
              "(c) 210 (d) 165; yes, the first number is always the LCM", ncert=["3.2.idli_c", "3.2.idli_d",
                                                                                 "3.2.idli_lcm"],
              fact="idli_cd", expect=[210, 165])],
       key_terms=["LCM", "common multiple"], misconceptions=["M_LCM_PRODUCT"], minutes=12),
     DOER("T11.C3", "Practice: when two schedules meet", None, "Apply",
          "Students list the multiples of two repeating schedules, find the first day both repeat, and explain why "
          "that day is the LCM of the two numbers.",
          ["Each repeating event gives a list of multiples.",
           "The first day or number shared by both lists is the LCM.",
           "Listing is slow for larger numbers, which is why primes help."])]))

# ============================== T12 LCM by prime factorisation ===============================================
TOPICS.append(TOPIC(
    "T12", "M2", "LCM from Prime Factorisation", ["3.2"], "Apply",
    "Students see that a multiple contains the primes of its number, build the LCM of two or more numbers by taking "
    "the maximum number of occurrences of each prime, and explain why more would not be lowest.",
    "LCM = product of all the primes that occur in any number, each taken the maximum number of times it occurs.",
    [A("T12.C1", "A multiple contains the primes of its number: 14 and 35", "Apply",
       "Students compare 36 with its multiple 648, see that the multiple holds all the primes of the number, and build "
       "the LCM of 14 and 35 as the smallest number holding both factorisations.",
       textbook=["As in the case of the HCF, the process of finding the LCM by listing down the multiples may get "
                 "tedious for larger numbers, as you would have seen for questions (c) and (d) above.",
                 "Prime factorisation can simplify the process of finding the LCM as well. How do we find the LCM of "
                 "two numbers using their prime factors?",
                 "Finding LCM through Prime Factorisation",
                 "We begin by comparing the prime factorisations of a number and a multiple of that number. For "
                 "example, let us take 36 and its multiple 648 (= 36 × 18). We get, 36 = 2 × 2 × 3 × 3, 648 = 36 × 18 = "
                 "(2 × 2 × 3 × 3) × (2 × 3 × 3).",
                 "What do you observe? We can see that the prime factors of the multiple contain the prime factors of "
                 "the number along with some more prime factors. Will this happen with every multiple?",
                 "Can this be used to find the LCM?",
                 "Example 6: Find the LCM of 14 and 35. We get, 14 = 2 × 7, 35 = 5 × 7. Common multiples should "
                 "contain each prime factor as a subpart: 2 × 7 as a subpart and 5 × 7 as a subpart.",
                 "For example, 2 × 7 × 5 × 7 × 3 is a common multiple of 14 and 35. 2 × 2 × 5 × 7 × 7 × 11 is another "
                 "common multiple. Is 2 × 3 × 5 × 7 also a common multiple? What is the lowest among all the common "
                 "multiples of 14 and 35?",
                 "It is 2 × 5 × 7 = 70 because 2 × 5 × 7 contains 14 = 2 × 7 as well as 35 = 5 × 7, and removing any "
                 "number from 2 × 5 × 7 will give a number that is not a common multiple of 14 and 35."],
       teach=["Predict first: 36 is 2 × 2 × 3 × 3 and 648 is 36 × 18. Do the primes of 36 still appear inside 648?",
              "A multiple always contains the primes of its number, plus possibly more.",
              "A common multiple must hold both factorisations, and the lowest one holds them with nothing extra."],
       examples=[
           WE("Find the LCM of 14 and 35 from their prime factorisations.",
              ["14 = 2 × 7 and 35 = 5 × 7.", "A common multiple must contain 2 × 7 and also 5 × 7.",
               "Share the 7: 2 × 5 × 7 contains both.", "Remove anything and one of 14 or 35 no longer fits.",
               "So the LCM is 2 × 5 × 7 = 70."],
              "70", ncert=["3.2.lcm_intro", "3.2.ex6"], fact="ex6_lcm", expect=[14, 35, 70])],
       key_terms=["LCM", "prime factorisation"], misconceptions=["M_LCM_PRODUCT", "M_COMMON_PRIMES_ONLY"], minutes=10),
     A("T12.C2", "Maximum occurrences of each prime: 96 and 360", "Apply",
       "Students build the LCM of 96 and 360 prime by prime using the maximum number of occurrences, and extend the "
       "method to three numbers.",
       textbook=["Example 7: Find the LCM of 96 and 360. We have, 96 = 2 × 2 × 2 × 2 × 2 × 3, 360 = 2 × 2 × 2 × 3 × "
                 "3 × 5.",
                 "Every common multiple should contain the prime factors of both 96 and 360. For the LCM, we will need "
                 "the smallest such number. Let us build the LCM looking at each prime factor.",
                 "The prime factors appearing in both the numbers are 2, 3 and 5. Now, we shall find out how many "
                 "occurrences there are for each prime factor.",
                 "How many 2s should the LCM contain? The factorisation of 96 contains 2 × 2 × 2 × 2 × 2 (five "
                 "occurrences of 2s) and the factorisation of 360 contains 2 × 2 × 2 (three occurrences of 2s). "
                 "Choosing five occurrences of 2s as part of LCM will contain both these subparts.",
                 "Choosing more than five occurrences of 2s will give a common multiple; but it will not be the "
                 "lowest. Are you able to see why?",
                 "How many 3s should the LCM contain? The factorisation of 96 contains 3 (one occurrence of 3) and "
                 "the factorisation of 360 contains 3 × 3 (two occurrences of 3s). Choosing two occurrences of 3s as "
                 "part of LCM will contain both these subparts.",
                 "How many 5s should the LCM contain? The factorisation of 96 doesn't have any 5s and the "
                 "factorisation of 360 has one occurrence of 5. So, we choose one occurrence of 5 to be a part of "
                 "the LCM.",
                 "Thus, the LCM of 96 and 360 will be 2 × 2 × 2 × 2 × 2 × 3 × 3 × 5 = 1440.",
                 "To build the LCM of two numbers, we can identify all the prime factors and find the maximum number "
                 "of times each of them occur in either of the factorisations. This process can be extended to find "
                 "the LCM of two or more numbers."],
       teach=["Predict first: 96 has five 2s and 360 has three. How many 2s must the LCM have?",
              "For each prime that appears anywhere, take the larger count. A prime missing from one number counts "
              "as zero there.",
              "Taking more than the maximum still gives a common multiple, but not the lowest."],
       examples=[
           WE("Find the LCM of 96 and 360 using the maximum number of occurrences of each prime.",
              ["96 = 2 × 2 × 2 × 2 × 2 × 3.", "360 = 2 × 2 × 2 × 3 × 3 × 5.", "Primes: 2, 3 and 5.",
               "2 occurs five times in 96 and three times in 360, so take five.",
               "3 occurs once in 96 and twice in 360, so take two.",
               "5 occurs zero times in 96 and once in 360, so take one.",
               "LCM = 2 × 2 × 2 × 2 × 2 × 3 × 3 × 5 = 1440."],
              "1440", ncert=["3.2.ex7"], fact="ex7_lcm", expect=[96, 360, 1440])],
       key_terms=["LCM", "maximum"], misconceptions=["M_MIN_MAX"], minutes=10),
     DOER("T12.C3", "Practice: build the LCM", "lcm_builder", "Apply",
          "Students build the LCM prime by prime from the maximum count in each factorisation, for two or three "
          "numbers, and check that every number divides the result.",
          ["List every prime that occurs in any number.", "For each prime, take the larger count.",
           "Multiply and check that each number divides the LCM."],
          items=[FIO("3.2.FiO_lcm", "Figure it Out (LCM)",
                     "Find the LCM of the following numbers: (a) 30, 72 (b) 36, 54 (c) 105, 195, 65 (d) 222, 370",
                     ["(a) 30 = 2 × 3 × 5, 72 = 2 × 2 × 2 × 3 × 3. Maximum counts: 2 three times, 3 twice, 5 once. "
                      "LCM = 2 × 2 × 2 × 3 × 3 × 5 = 360.",
                      "(b) 36 = 2 × 2 × 3 × 3, 54 = 2 × 3 × 3 × 3. Maximum counts: 2 twice, 3 three times. "
                      "LCM = 2 × 2 × 3 × 3 × 3 = 108.",
                      "(c) 105 = 3 × 5 × 7, 195 = 3 × 5 × 13, 65 = 5 × 13. Primes 3, 5, 7, 13 once each. "
                      "LCM = 3 × 5 × 7 × 13 = 1365.",
                      "(d) 222 = 2 × 3 × 37, 370 = 2 × 5 × 37. Primes 2, 3, 5, 37 once each. "
                      "LCM = 2 × 3 × 5 × 37 = 1110."],
                     "(a) 360 (b) 108 (c) 1365 (d) 1110", expect=[360, 108, 1365, 1110], tool="lcm_builder")],
          ncert=["3.2.FiO_lcm"], misconceptions=["M_MIN_MAX", "M_COMMON_PRIMES_ONLY"])]))
