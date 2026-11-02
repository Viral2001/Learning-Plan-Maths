# -*- coding: utf-8 -*-
"""Topics T1 to T6 (modules M1 and M2): book sections 5.1 to 5.3."""
from topics_common import A, DOER, TOPIC, BOOK_TEXT, book, fio, we, wem

TOPICS = []

# ============================== T1 Framing ===================================================================
TOPICS.append(TOPIC(
    "T1", "M1", "Numbers That Meet", ["Chapter opening"], "Understand",
    "",
    "Two bells, two rhythms: when do they ring together, and why do some pairs of numbers never meet early?",
    [A("T1.C1", "Two bells, one moment", "Remember", "",
       textbook=[],
       teach=["A temple bell rings every 4 minutes and a school bell every 6 minutes. They ring together at noon.",
              "Make a guess before the next step: when will they ring together again?",
              "Count the 4s and the 6s. The first time both land on the same minute is 12 minutes later.",
              "Some pairs meet quickly, and some, like 5 and 7, meet only at 35. This chapter finds out why."],
       ncert=[], key_terms=["multiple"], video_focus=["HOOK"], minutes=4, enrichment=True)],
    topic_type="framing"))

# ============================== T2 Common multiples (5.1 idli-vada) ==========================================
TOPICS.append(TOPIC(
    "T2", "M1", "Multiples and Common Multiples", ["5.1"], "Apply",
    "Students list multiples of a number, find the numbers that two games share as common multiples, and decide "
    "when one number's multiples are all multiples of the other's.",
    "Multiples come from skip counting; numbers in both lists are common multiples, found at every multiple of the "
    "first one.",
    [A("T2.C1", "Multiples: idli and vada", "Understand",
       "Students list the multiples of 3 and of 5 by skip counting and use them to say which numbers get idli and "
       "which get vada.",
       textbook=book("5.1", "Idli-Vada Game", stop=5),
       teach=["Predict first: in a circle game, children say idli for every 3rd number. Which numbers is that?",
              "Skip count by 3: 3, 6, 9, 12, 15, and so on. These are the multiples of 3.",
              "For vada, skip count by 5: 5, 10, 15, 20, and so on, the multiples of 5.",
              "A multiple of a number is a number you reach by skip counting by it, never smaller than the number."],
       examples=[wem(["5.1.q1", "5.1.q2"],
                     q="In the idli-vada game, for which numbers do the players say 'idli' (every 3rd number) and "
                       "for which 'vada' (every 5th)?",
                     steps=["Idli is said for 3, 6, 9, 12, 15, 18, 21 and so on, the multiples of 3.",
                            "Vada is said for 5, 10, 15, 20, 25 and so on, the multiples of 5."],
                     answer="Idli for the multiples of 3, vada for the multiples of 5.")],
       key_terms=["multiple", "skip counting"], misconceptions=["M_MULTIPLE_FACTOR"], minutes=8),
     A("T2.C2", "Common multiples: idli-vada", "Apply",
       "Students find the numbers that are multiples of both numbers in a game, name them common multiples, and "
       "spot them on a table or a two-circle figure.",
       textbook=book("5.1", "Idli-Vada Game", start=5, stop=6) + book("5.1", "Idli-Vada Game", start=11, stop=13),
       teach=["Predict first: 15 is said by both the idli players and the vada players. What do we say?",
              "We say 'idli-vada'. 15 is a multiple of 3 and also of 5, so it is a common multiple.",
              "The next ones are 30, 45, 60: every multiple of 15 is a common multiple.",
              "Draw two circles, one for each list; the numbers in both go in the overlap."],
       examples=[we("5.1.q3"), we("5.1.q4"), we("5.1.q9")],
       key_terms=["common multiple"], misconceptions=["M_ONLY_FIRST_COMMON"], minutes=10),
     A("T2.C3", "When nobody says just vada", "Analyze",
       "Students decide which number pairs give idli or idli-vada but never just vada, and explain that every "
       "multiple of the larger number must be a multiple of the smaller.",
       textbook=book("5.1", "Idli-Vada Game", start=13),
       teach=["Predict first: if one of the numbers is 4, can the other be 8, so that nobody says just vada?",
              "Vada is said for multiples of the larger number. Every one must also be a multiple of the smaller.",
              "With 4 and 8, every multiple of 8 is also a multiple of 4, so no one says just vada.",
              "With 4 and 2 the larger is 4, and every multiple of 4 is a multiple of 2, so that works too."],
       examples=[we("5.1.q5", steps=["Vada is said for multiples of the larger number, so every one of them must also be a multiple of the smaller number.",
                                     "With 4 and 8, every multiple of 8 is a multiple of 4, so nobody says just vada.",
                                     "With 2 and 4, every multiple of 4 is a multiple of 2, so that works too.",
                                     "With 3, 5 or 10 someone says just vada: for 3 and 4 it is 4, for 4 and 5 it is 5, for 4 and 10 it is 10."],
                      answer="2 and 8 (the book names only 8).")],
       key_terms=["multiple", "common multiple"], misconceptions=["M_ONLY_FIRST_COMMON"], minutes=8),
     DOER("T2.C4", "Pull it together and do it: Idli-Vada Caller", "idli_vada", "Apply",
          "Students call the idli-vada game for chosen number pairs on the tool, find the common multiples and "
          "predict the first one before it comes.",
          ["A multiple is reached by skip counting by the number.",
           "A number that is in both lists is a common multiple of the two numbers.",
           "If the larger number is a multiple of the smaller, nobody says just vada."],
          items=[fio("5.1.FiO1.Q1", tool="idli_vada"), fio("5.1.FiO1.Q2", tool="idli_vada"),
                 fio("5.1.FiO1.Q3", tool="idli_vada"),
                 fio("5.1.FiO1.Q4",
                     steps=["Left circle: multiples of 3. Right circle: multiples of 5.",
                            "The overlap holds the multiples of both: 15, 30, 45, 60.",
                            "Multiples of 3 only: 3, 6, 9, 12, 18, 21, 24, 27, 33, 36, 39, 42, 48, 51, 54, 57.",
                            "Multiples of 5 only: 5, 10, 20, 25, 35, 40, 50, 55."],
                     answer="Yes: the overlap is where 'idli-vada' is said. Till 60 the overlap is 15, 30, 45, 60. "
                            "(The printed Fig. 5.1 leaves 6 out of the left circle; 6 belongs there.)"),
                 fio("5.1.FiO2.Q1"), fio("5.1.FiO2.Q5"),
                 fio("5.1.FiO2.Q6",
                     steps=["The first idli-vada is the first common multiple, and it must be more than 50.",
                            "7 and 8 first meet at 56, 8 and 9 at 72, and 7 and 9 at 63.",
                            "Each of these pairs is smaller than 10 and gives a first idli-vada after 50."],
                     answer="7 and 8, or 8 and 9, or 7 and 9."),
                 fio("5.1.FiO2.Q8",
                     steps=["The overlap shows only 24, 48 and 72, so the first common multiple is 24.",
                            "3 and 4 would also put 12, 36 and 60 in the overlap, so that pair is not right.",
                            "Choose a pair whose first common multiple is 24, such as 3 and 8.",
                            "Multiples of 3: 3, 6, 9, 12, 15 ... Multiples of 8: 8, 16, 24, 32 ... Both lists "
                            "meet only at 24, 48 and 72."],
                     answer="Multiples of 3 and multiples of 8 (many other pairs with first common multiple 24 "
                            "also work)."),
                 fio("5.1.FiO2.Q9"), fio("5.1.FiO2.Q10")],
          misconceptions=["M_ONLY_FIRST_COMMON"])]))

# ============================== T3 Factors and common factors (5.1 jump jackpot) =============================
TOPICS.append(TOPIC(
    "T3", "M1", "Factors and Common Factors", ["5.1"], "Apply",
    "Students list all the factors of a number from the jump sizes that land on it, and find the common factors of "
    "two numbers as the jump sizes that reach both.",
    "A factor divides a number exactly; the jump sizes that reach a number are its factors, and those that reach "
    "two numbers are their common factors.",
    [A("T3.C1", "Factors: jump sizes that land", "Understand",
       "Students find every jump size that lands on a treasure number, include 1 and the number itself, and call "
       "these jump sizes the factors of the number.",
       textbook=book("5.1", "Jump Jackpot", stop=8),
       teach=["Predict first: Grumpy puts a treasure on 24. Jumpy can jump by 4. Which other jump sizes work?",
              "Jumping by 4 lands on 4, 8, 12, 16, 20, 24, so it works. So do 2, 3, 6, 8 and 12.",
              "Jump sizes 1 and 24 also land on 24.",
              "All of 1, 2, 3, 4, 6, 8, 12, 24 divide 24 exactly, so they are the factors of 24."],
       examples=[we("5.1.q6")],
       key_terms=["factor", "divisor"], misconceptions=["M_FACTORS_MISS_ENDS", "M_MULTIPLE_FACTOR"], minutes=8),
     A("T3.C2", "Common factors: reaching two treasures", "Apply",
       "Students find the jump sizes that reach two treasures by listing the factors of each number and picking the "
       "numbers in both lists.",
       textbook=book("5.1", "Jump Jackpot", start=8, stop=16),
       teach=["Predict first: treasures are on 14 and 36 and Jumpy jumps by 7. Does he reach both?",
              "He reaches 14 but jumps over 36: 28, 35, 42. So 7 does not work for both.",
              "Factors of 14: 1, 2, 7, 14. Factors of 36: 1, 2, 3, 4, 6, 9, 12, 18, 36.",
              "The jump sizes in both lists are 1 and 2: the common factors of 14 and 36."],
       examples=[we("5.1.q7"), we("5.1.q8")],
       key_terms=["common factor"], misconceptions=["M_FACTORS_MISS_ENDS"], minutes=10),
     DOER("T3.C3", "Pull it together and do it: Jump Jackpot", "jump_jackpot", "Apply",
          "Students place treasures on the tool, list the factors of one number and the common factors of two, and "
          "find numbers from clues about their factors and multiples.",
          ["A factor of a number divides it exactly, and 1 and the number itself are always factors.",
           "A common factor of two numbers is a factor of both.",
           "A multiple is bigger than or equal to the number; a factor is smaller than or equal to it."],
          items=[fio("5.1.FiO2.Q2", tool="jump_jackpot"), fio("5.1.FiO2.Q3", tool="jump_jackpot"),
                 fio("5.1.FiO2.Q4", tool="jump_jackpot"), fio("5.1.FiO2.Q7", tool="jump_jackpot")],
          misconceptions=["M_FACTORS_MISS_ENDS", "M_MULTIPLE_FACTOR"])]))

# ============================== T4 Prime and composite numbers (5.2 first half) ==============================
TOPICS.append(TOPIC(
    "T4", "M2", "Prime and Composite Numbers", ["5.2"], "Apply",
    "Students arrange a number of figs in rectangles to find its factors, call numbers with exactly two factors "
    "primes, and tell primes, composites and 1 apart.",
    "A number with exactly two factors is prime; more than two factors makes it composite; 1 is neither.",
    [A("T4.C1", "Packing figs in rectangles", "Understand",
       "Students list every rectangle that 12 figs and 7 figs can make, and see that 12 has several and 7 has only "
       "one.",
       textbook=book("5.2", None, stop=5),
       teach=["Predict first: Guna has 12 figs and Anshu has 7. Who can make more rectangular boxes?",
              "12 figs: 12 rows of 1, 6 of 2, 4 of 3, and the same turned round.",
              "7 figs: only 7 by 1 or 1 by 7.",
              "Each rectangle is a pair of numbers that multiply to the number, so it is a pair of factors."],
       examples=[we("5.2.q1")],
       key_terms=["rectangle", "factor pair"], misconceptions=["M_FACTORS_MISS_ENDS"], minutes=8),
     A("T4.C2", "Rows and columns are factors", "Analyze",
       "Students connect the rows and columns of each rectangle to the factors of the number and explain why a "
       "number with only one rectangle has just two factors.",
       textbook=book("5.2", None, start=5, stop=9),
       teach=["Predict first: in the second arrangement of 12, there are 2 rows and 6 columns. What is 2 × 6?",
              "It is 12, so rows times columns is always 12 and both are factors of 12.",
              "12 has the factors 1, 2, 3, 4, 6 and 12, so it can be arranged in more than one way.",
              "7 has only 1 and 7, so it makes only one rectangle."],
       examples=[we("5.2.q2")],
       key_terms=["factor"], misconceptions=["M_FACTORS_MISS_ENDS"], minutes=8),
     A("T4.C3", "Primes, composites and the number 1", "Understand",
       "Students call a number with exactly two factors prime, one with more composite, say why 1 is neither, and "
       "count the primes between 21 and 30.",
       textbook=book("5.2", None, start=9, stop=13),
       teach=["Predict first: is 1 a prime? Keeko thinks yes, because only 1 and itself divide it.",
              "1 has only one factor, itself. A prime needs exactly two factors, so 1 is not prime.",
              "Numbers with exactly two factors, like 2, 3, 5, 7, 11, are primes.",
              "Numbers with more than two factors, like 4, 6, 8, 9, are composite."],
       examples=[we("5.2.q3")],
       key_terms=["prime", "composite"], misconceptions=["M_ONE_IS_PRIME", "M_ALL_EVEN_COMPOSITE"], minutes=8),
     DOER("T4.C4", "Pull it together and do it: Rectangle Maker", "factor_rect", "Apply",
          "Students lay out dot rectangles on the tool to find factors, tag numbers as prime, composite or neither, "
          "and judge statements about primes.",
          ["A number with exactly two factors is prime.",
           "A number with more than two factors is composite.",
           "1 has one factor and is neither prime nor composite."],
          items=[fio("5.2.FiO.Q1", tool="factor_rect"), fio("5.2.FiO.Q4", tool="factor_rect"),
                 fio("5.2.FiO.Q9", tool="factor_rect")],
          misconceptions=["M_ONE_IS_PRIME", "M_ALL_EVEN_COMPOSITE", "M_ODD_MEANS_PRIME"])]))

# ============================== T5 Sieve of Eratosthenes (5.2 second half) ===================================
TOPICS.append(TOPIC(
    "T5", "M2", "The Sieve of Eratosthenes", ["5.2"], "Apply",
    "Students find all the primes up to 100 by crossing out multiples in order, and explain why every circled "
    "number is prime.",
    "Circle the next uncrossed number and cross out its multiples; what remains circled are exactly the primes.",
    [A("T5.C1", "Crossing out to find primes", "Apply",
       "Students follow the five steps of the sieve on a table of 1 to 100 and list the primes they find, "
       "crossing out 1 first and multiples of each circled number.",
       textbook=book("5.2", None, start=13, stop=22),
       teach=["Predict first: can you list all the primes from 1 to 100 without checking each number?",
              "Cross out 1, circle 2 and cross out every multiple of 2 after it.",
              "The next uncrossed number is 3. Circle it and cross out its multiples. Then 5, then 7.",
              "Continue until every number is circled or crossed. The circled numbers are the primes."],
       examples=[we("5.2.q4")],
       key_terms=["sieve", "prime"], misconceptions=["M_SIEVE_MAGIC"], minutes=10),
     A("T5.C2", "Why the sieve works", "Analyze",
       "Students explain why a number left uncrossed has no smaller factor, so it is prime, and why every crossed "
       "number is composite.",
       textbook=book("5.2", None, start=22, stop=24),
       teach=["Predict first: the sieve is not magic. Why is 7 left uncrossed?",
              "A number is crossed out when it is a multiple of a smaller circled number.",
              "A number nobody crossed has no smaller factor except 1, so it has only two factors.",
              "A number that was crossed is a multiple of a smaller number, so it has a third factor."],
       examples=[we("5.2.q5", steps=["Each circled number has not been crossed out by any smaller circled number.",
                                     "So it has no factor between 1 and itself: its only factors are 1 and "
                                     "itself.",
                                     "A crossed-out number is a multiple of a smaller number, so it has more "
                                     "than two factors."],
                    answer="Circled numbers have exactly two factors, so they are prime; crossed-out numbers "
                           "have more, so they are composite.")],
       key_terms=["sieve", "composite"], misconceptions=["M_SIEVE_MAGIC"], minutes=8),
     DOER("T5.C3", "Pull it together and do it: Eratosthenes Sieve", "sieve", "Analyze",
          "Students run the sieve on the tool, read off primes, and use the list of primes to answer questions about "
          "gaps, twins and consecutive composites.",
          ["Cross out the multiples of each circled number; what is left is prime.",
           "Twin primes differ by 2.",
           "Between two primes there can be a long run of composite numbers."],
          items=[fio("5.2.FiO.Q2", tool="sieve"), fio("5.2.FiO.Q3", tool="sieve"),
                 fio("5.2.FiO.Q5"), fio("5.2.FiO.Q6"), fio("5.2.FiO.Q7", tool="sieve"),
                 fio("5.2.FiO.Q8", tool="sieve"), fio("5.2.FiO.Q10"), fio("5.2.FiO.Q11"), fio("5.2.FiO.Q12")],
          misconceptions=["M_ODD_MEANS_PRIME", "M_SIEVE_MAGIC"])]))

# ============================== T6 Co-prime numbers (5.3) ====================================================
TOPICS.append(TOPIC(
    "T6", "M2", "Co-prime Numbers", ["5.3"], "Apply",
    "Students find the pairs of numbers whose only common factor is 1, test pairs for being co-prime, link "
    "co-primes to the first common multiple, and see them in thread art.",
    "Two numbers are co-prime when their only common factor is 1; then the first common multiple is their product.",
    [A("T6.C1", "Safe pairs are co-prime", "Understand",
       "Students choose two treasure numbers that Jumpy cannot reach by a jump size above 1, and call such pairs, "
       "with only 1 as a common factor, co-prime.",
       textbook=book("5.3", "Which pairs are safe?", stop=4) + book("5.3", "Which pairs are safe?", start=5, stop=7),
       teach=["Predict first: Grumpy wants no jump size except 1 to reach both treasures. Will 12 and 26 work?",
              "No: a jump of 2 reaches both. Will 4 and 9 work?",
              "Factors of 4: 1, 2, 4. Factors of 9: 1, 3, 9. Only 1 is common, so Jumpy cannot reach both.",
              "Two numbers with no common factor other than 1 are co-prime."],
       examples=[we("5.3.q1"), we("5.3.ex1")],
       key_terms=["co-prime", "common factor"], misconceptions=["M_COPRIME_BOTH_PRIME", "M_JUMP_ONE_ALWAYS"],
       minutes=8),
     A("T6.C2", "Checking pairs for co-primes", "Apply",
       "Students list the factors of both numbers in each pair, look for a common factor other than 1, and decide "
       "whether the pair is co-prime.",
       textbook=book("5.3", "Which pairs are safe?", start=4, stop=5) + book("5.3", "Which pairs are safe?",
                                                                               start=7, stop=8),
       teach=["Predict first: is 15 and 39 safe? Factors of 15: 1, 3, 5, 15. Factors of 39: 1, 3, 13, 39.",
              "3 is common, so 15 and 39 are not co-prime.",
              "4 and 15 share only 1, so they are co-prime. Note that 4 and 15 are not themselves prime.",
              "Co-prime numbers need not be prime, only free of a common factor."],
       examples=[we("5.3.q2"), we("5.3.q3")],
       key_terms=["co-prime"], misconceptions=["M_COPRIME_BOTH_PRIME", "M_ONE_PAIR_ENOUGH"], minutes=10),
     A("T6.C3", "Co-primes and the first common multiple", "Analyze",
       "Students compare the first common multiple of a pair with the product of the pair, and see that the two are "
       "equal exactly when the pair is co-prime.",
       textbook=book("5.3", "Which pairs are safe?", start=8),
       teach=["Predict first: the first common multiple of 3 and 5 is 15. How does it compare with 3 × 5?",
              "3 × 5 = 15, the same. For 4 and 9 the first common multiple is 36, which is 4 × 9.",
              "For 3 and 6 the first common multiple is 6, less than 3 × 6 = 18.",
              "When the pair is co-prime, the first common multiple is the product."],
       examples=[we("5.3.q4")],
       key_terms=["common multiple", "co-prime"], misconceptions=["M_ONLY_FIRST_COMMON"], minutes=8),
     DOER("T6.C4", "Pull it together and do it: Thread Art Co-prime Check", "thread_art", "Analyze",
          "Students draw thread art on the tool for chosen peg counts and gaps, and link whether the thread reaches "
          "every peg to the pair being co-prime.",
          ["Two numbers are co-prime when their only common factor is 1.",
           "The first common multiple of co-prime numbers is their product.",
           "A thread with gap g on n pegs reaches every peg exactly when n and g are co-prime."],
          items=[], ncert=["5.3.q5"],
          misconceptions=["M_ONE_PAIR_ENOUGH"])]))
