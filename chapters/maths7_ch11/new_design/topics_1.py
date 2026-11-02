# -*- coding: utf-8 -*-
"""Topics T1 to T9 (module M1: common factors and HCF). Book section 3.1, pp 47 to 54."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Introduction ==============================================================
TOPICS.append(TOPIC(
    "T1", "M1", "Sameeksha's Tile Challenge", ["Chapter opening", "3.1"], "Understand",
    "",
    "A room 12 ft by 16 ft, square tiles with no gaps, and an open question: which tile sizes fit, and which is largest?",
    [A("T1.C1", "A room to cover with square tiles", "Remember",
       "",
       textbook=["3 Finding Common Ground", "3.1 The Greatest of All",
                 "Sameeksha is building her new house. The main room of the house is 12 ft by 16 ft. She feels that "
                 "the room would look nice if the floor is covered with square tiles of the same size. She also wants "
                 "to use as few tiles as possible, and for the length of the tile to be a whole number of feet. What "
                 "size tiles should she buy?"],
       teach=["Picture the floor from above: a rectangle 12 ft by 16 ft. Square tiles of one size must cover it with "
              "no gaps and no overlaps.",
              "Make a guess before the next step: which tile sizes could fit perfectly, and which is the largest "
              "that still fits, so that she buys the fewest tiles?"],
       ncert=["opening", "3.1.tile"], key_terms=["tile", "factor"], video_focus=["HOOK"], minutes=4,
       enrichment=True),
     A("T1.C2", "The question to keep: which tiles fit, and which is largest", "Understand", "",
       teach=["Predict: which square tile sizes could cover a 12 ft by 16 ft floor with no cutting?",
              "A tile fits only if its side divides both 12 and 16 exactly.",
              "Several sizes can fit; the question asks for the largest.",
              "Keep this question in mind: the next topic gives that largest number a name."],
       enrichment=True)],
    topic_type="framing"))

# ============================== T2 HCF / GCD =================================================================
TOPICS.append(TOPIC(
    "T2", "M1", "Introducing HCF or GCD", ["3.1"], "Apply",
    "Students find the common factors of two numbers, explain why the largest common factor gives the fewest tiles, "
    "count those tiles, and name the largest common factor as the HCF or GCD. They also test whether fractional tile "
    "sides would change the answer.",
    "A tile side must be a factor of both room lengths; the greatest such factor is the HCF, which also minimises tiles.",
    [A("T2.C1", "Common factors of 12 and 16: which tiles fit", "Apply",
       "Students list the factors of 12 and of 16, pick out the common factors, and explain why the largest common "
       "factor gives the fewest square tiles for the 12 ft by 16 ft room.",
       textbook=["Let us explore how to find the largest square tile that can be used. The breadth of the room is "
                 "12 ft and the length is 16 ft.",
                 "For the tiles to fit the breadth of the room exactly, the side of the tile should be a factor of "
                 "12. Similarly, for the tiles to fit the length of the room exactly, the side should be a factor of "
                 "16. So the side of the tile should be a factor of both 12 and 16. What are the common factors of "
                 "12 and 16?",
                 "The factors of 12 are 1, 2, 3, 4, 6, 12. The factors of 16 are 1, 2, 4, 8, 16. The common factors "
                 "are 1, 2, and 4.",
                 "So, the square tiles can have sides 1 ft, 2 ft, and 4 ft. Among these, she should use the largest "
                 "sized square tile. Can you explain why?",
                 "Therefore, she needs tiles of size 4 ft."],
       teach=["Predict first: which numbers divide 12 exactly, and which divide 16 exactly?",
              "A tile side that fits the breadth must be a factor of 12. A tile side that fits the length must be a "
              "factor of 16. So it must be a common factor.",
              "A larger tile covers more floor, so fewer tiles are needed. The largest common factor gives the "
              "fewest tiles."],
       examples=[
           WE("Sameeksha's room is 12 ft by 16 ft. List the factors of 12 and of 16, find the common factors, and "
              "say which square tile side she should choose and why.",
              ["The factors of 12 are 1, 2, 3, 4, 6, 12.", "The factors of 16 are 1, 2, 4, 8, 16.",
               "The common factors are 1, 2, 4.", "So tiles of side 1 ft, 2 ft or 4 ft fit perfectly.",
               "A larger tile covers more floor, so she needs fewer tiles.",
               "The largest common factor is 4, so she should buy tiles of side 4 ft."],
              "Common factors 1, 2, 4; she should choose the 4 ft tile because the largest fitting tile needs the fewest tiles",
              ncert=["3.1.tile_largest"], fact="common_factors", expect=[12, 16, [1, 2, 4]])],
       key_terms=["factor", "common factor"], misconceptions=["M_COMMON_ONLY", "M_HCF_BIG"], minutes=10),
     A("T2.C2", "The Highest Common Factor, and how many tiles", "Apply",
       "Students define the HCF, also called the GCD, count the 4 ft tiles needed for the room, and check that "
       "allowing fractional tile sides does not make a larger tile possible.",
       textbook=["How many tiles of this size should she purchase?",
                 "What if Sameeksha did not insist on the length of the tile to be a whole number of feet and the "
                 "length could be a fractional number of feet? Would the answer change?",
                 "The Highest Common Factor (HCF) of two or more numbers, is the highest (or greatest) of their common "
                 "factors. It is also known as the Greatest Common Divisor (GCD).",
                 "In the previous problem, 4 is the HCF of 12 and 16.",
                 "We can draw rough diagrams like the one shown on the previous page to visualise the given scenario. "
                 "It may help in understanding and solving."],
       teach=["The greatest of the common factors has a name: the Highest Common Factor, HCF, or the Greatest Common "
              "Divisor, GCD. For 12 and 16 it is 4.",
              "With 4 ft tiles the 12 ft side holds 3 tiles and the 16 ft side holds 4 tiles, so 3 × 4 tiles cover "
              "the floor.",
              "Rough diagrams help: draw the room and cut it into squares before calculating."],
       examples=[
           WE("Name the largest common factor of 12 and 16, and find how many 4 ft tiles cover the 12 ft by 16 ft "
              "room.",
              ["The largest common factor of 12 and 16 is 4, so the HCF (or GCD) of 12 and 16 is 4.",
               "Along the 12 ft side: 12 ÷ 4 = 3 tiles.", "Along the 16 ft side: 16 ÷ 4 = 4 tiles.",
               "Number of tiles = 3 × 4 = 12."],
              "HCF is 4, and she needs 12 tiles", ncert=["3.1.hcf_def", "3.1.tile_count"], fact="tiles_count",
              expect=[12, 16, 4, 12]),
           WE("What if the tile side could be a fractional number of feet? Could a tile larger than 4 ft fit the "
              "12 ft by 16 ft room?",
              ["A tile of some side fits only if it divides 12 ft into a whole number of tiles and 16 ft into a "
               "whole number of tiles.",
               "The two tile counts must be in the same proportion as 12 to 16, which is 3 to 4.",
               "The smallest whole counts in that proportion are 3 tiles and 4 tiles.",
               "That gives a tile side of 12 ÷ 3 = 4 ft, so no larger tile can fit.",
               "Smaller fractional tiles fit, but they need more tiles."],
              "No, the largest tile is still 4 ft", ncert=["3.1.tile_fraction"])],
       key_terms=["HCF", "GCD"], misconceptions=["M_HCF_BIG"], minutes=10),
     DOER("T2.C3", "Practice: list the common factors", "common_factor_lister", "Apply",
          "Students list the factors of two numbers, circle the common ones and name the HCF for several pairs, "
          "checking the largest common factor against a picture of squares on a rectangle.",
          ["A common factor divides both numbers exactly.",
           "The HCF is the greatest common factor, and every common factor divides it in these examples.",
           "A square tile of side equal to the HCF covers a rectangle with the fewest tiles."])]))

# ============================== T3 Lekhana's rice bags =======================================================
TOPICS.append(TOPIC(
    "T3", "M1", "Lekhana's Rice Bags", ["3.1"], "Apply",
    "Students turn a packing story into a common factor question: weights that divide both 84 kg and 108 kg, and "
    "the largest of them for the fewest bags. They check each trial weight against both quantities.",
    "Equal bags from each farm need a common factor of 84 and 108; the greatest one, 12, gives the fewest bags.",
    [A("T3.C1", "Equal bags from two farms", "Apply",
       "Students list the factors of 84 and 108, find their common factors, choose the weight giving the fewest bags, "
       "and count the bags from each farm.",
       textbook=["Lekhana purchases rice from two farms and sells it in the market. She bought 84 kg of rice from "
                 "one farm and 108 kg from the other farm. She wants the rice to be packed in bags, so each bag has "
                 "rice from only one farm and all bags have the same weight that is a whole number of kg. If she "
                 "wants to use as few bags as possible, what should the weight of each bag be?",
                 "To divide 84 kg of rice into bags of equal weight, we need the factors of 84. Similarly, for 108, "
                 "we need the factors of 108.",
                 "Factors of 84: 1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, and 84.",
                 "Factors of 108: 1, 2, 3, 4, 6, 9, 12, 18, 27, 36, 54, and 108.",
                 "Since, Lekhana wants to use bags of the same weight for both farms, the weight of the bag should be "
                 "a common factor. The common factors of 84 and 108 are 1, 2, 3, 4, 6, and 12.",
                 "She can use any of these weights to pack rice from both farms in bags of equal weight. But, she "
                 "wants to minimise the number of bags. Which weight should she choose to minimise the number of "
                 "bags?"],
       teach=["Predict first: could she pack both farms in bags of 5 kg? Of 8 kg? Test whether each divides both "
              "quantities.",
              "A bag weight must divide 84 and must also divide 108, so it is a common factor.",
              "Heavier bags mean fewer bags, so she picks the greatest common factor, which is the HCF."],
       examples=[
           WE("Lekhana has 84 kg and 108 kg of rice from two farms. Find the greatest equal bag weight in whole kg, "
              "with each bag from one farm, and how many bags she needs.",
              ["The factors of 84 are 1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, 84.",
               "The factors of 108 are 1, 2, 3, 4, 6, 9, 12, 18, 27, 36, 54, 108.",
               "The common factors are 1, 2, 3, 4, 6, 12.",
               "Fewest bags means the heaviest bag, so the weight is 12 kg.",
               "Bags from the first farm: 84 ÷ 12 = 7.", "Bags from the second farm: 108 ÷ 12 = 9.",
               "Total bags = 7 + 9 = 16."],
              "Each bag should weigh 12 kg, and she needs 16 bags", ncert=["3.1.rice"], fact="rice",
              expect=[84, 108, 12, 16])],
       key_terms=["common factor", "HCF"], misconceptions=["M_HCF_BIG", "M_COMMON_ONLY"], minutes=10),
     DOER("T3.C2", "Practice: equal bags and the HCF", None, "Apply",
          "Students find the largest equal bag weight for two quantities by listing the factors of each, keeping "
          "the common factors and choosing the greatest.",
          ["First list the factors of each quantity.", "Then keep only the factors that appear in both lists.",
           "The greatest of those is the weight that needs the fewest bags."])]))

# ============================== T4 Jump Jackpot ==============================================================
TOPICS.append(TOPIC(
    "T4", "M1", "Jump Jackpot", ["3.1"], "Apply",
    "Students recall the jumping game on the number line, find the longest jump that lands on two treasure numbers, and explain why "
    "this longest jump equals the HCF of the two numbers.",
    "A jump size lands on a number when it is a factor of it, so the longest jump landing on both numbers is their HCF.",
    [A("T4.C1", "Jumps that land on both treasures", "Apply",
       "Students find the longest jump from 0 that lands on both treasures for four number pairs, by listing the "
       "jump sizes that land on each number.",
       textbook=["Do you remember the 'Jump Jackpot' game from Grade 6 (see the chapter 'Prime Time')? Grumpy "
                 "places a treasure on a number and Jumpy chooses a jump size and tries to collect the treasure. In "
                 "each case below, the two numbers upon which treasures are kept are given. Find the longest jump "
                 "size (starting from 0) using which Jumpy can land on both the numbers having the treasure.",
                 "(a) 14 and 30 (b) 7 and 11 (c) 30 and 50 (d) 28 and 42"],
       teach=["Predict first: a jump of size 2 starts at 0 and lands on 2, 4, 6, and so on. Does it land on 14? On "
              "30?",
              "A jump size lands on a number exactly when it is a factor of that number. So a jump that lands on "
              "both treasures is a common factor.",
              "Take each pair in turn and find the longest jump."],
       examples=[
           WE("Treasures are on 14 and 30. Find the longest jump from 0 that lands on both. Then do the same for "
              "7 and 11.",
              ["Jump sizes landing on 14: 1, 2, 7, 14.", "Jump sizes landing on 30: 1, 2, 3, 5, 6, 10, 15, 30.",
               "Common jump sizes: 1 and 2, so the longest for 14 and 30 is 2.",
               "Jump sizes landing on 7: 1, 7.", "Jump sizes landing on 11: 1, 11.",
               "The only common jump size is 1, so the longest for 7 and 11 is 1."],
              "(a) 2 (b) 1", ncert=["3.1.jump_a", "3.1.jump_b"], fact="jump_ab", expect=[2, 1]),
           WE("Treasures are on 30 and 50. Find the longest jump from 0 that lands on both. Then do the same for "
              "28 and 42.",
              ["Jump sizes landing on 30: 1, 2, 3, 5, 6, 10, 15, 30.",
               "Jump sizes landing on 50: 1, 2, 5, 10, 25, 50.",
               "Common jump sizes: 1, 2, 5, 10, so the longest for 30 and 50 is 10.",
               "Jump sizes landing on 28: 1, 2, 4, 7, 14, 28.", "Jump sizes landing on 42: 1, 2, 3, 6, 7, 14, 21, 42.",
               "Common jump sizes: 1, 2, 7, 14, so the longest for 28 and 42 is 14."],
              "(c) 10 (d) 14", ncert=["3.1.jump_c", "3.1.jump_d"], fact="jump_cd", expect=[10, 14])],
       key_terms=["common factor", "jump size"], misconceptions=["M_COMMON_ONLY"], minutes=12),
     A("T4.C2", "Is the longest jump the HCF?", "Analyze",
       "Students compare the longest jump with the HCF for each pair, explain why a jump landing on both numbers is "
       "a common factor, and say why the longest such jump must be the HCF.",
       textbook=["Is the longest jump size for the numbers the same as their HCF? Explain why it is so."],
       teach=["Look back at the four pairs: the longest jumps were 2, 1, 10 and 14. Compare them with the HCFs.",
              "A jump size lands on a number only if the number is a multiple of the jump size, which means the jump "
              "size is a factor of it.",
              "Landing on both treasures makes the jump size a common factor, and the longest such jump is the "
              "highest common factor."],
       examples=[
           WE("Is the longest jump size for two treasure numbers always their HCF? Explain with 30 and 50.",
              ["A jump size lands on 30 only if 30 is a multiple of it, so the jump size is a factor of 30.",
               "In the same way the jump size must be a factor of 50.",
               "So the jump size is a common factor of 30 and 50.",
               "The longest possible jump is therefore the highest common factor, 10.",
               "This holds for every pair, so yes: the longest jump is the HCF."],
              "Yes, the longest jump landing on both numbers is their HCF", ncert=["3.1.jump_hcf"])],
       key_terms=["HCF"], misconceptions=["M_HCF_BIG"], minutes=8),
     DOER("T4.C3", "Practice: the longest jump on both treasures", None, "Apply",
          "Students find the longest jump that lands on both of two treasure numbers by listing the factors of each "
          "number and choosing the greatest common factor.",
          ["A jump size lands on a number exactly when it is a factor of that number.",
           "The longest jump that lands on both treasures is the HCF of the two numbers."])]))

# ============================== T5 Primes ====================================================================
TOPICS.append(TOPIC(
    "T5", "M1", "Prime Numbers Revisited", ["3.1"], "Understand",
    "Students recall that a prime is greater than 1 with exactly two factors, sort numbers into primes and composites, "
    "and see why 1 is neither. They use primes as the building blocks for the next step.",
    "Listing factors is slow and error-prone, so we turn to primes: a prime has only 1 and itself as factors.",
    [A("T5.C1", "Why look at primes, and what a prime is", "Remember",
       "Students explain why listing factors becomes slow and unreliable for numbers like 30, 50, 28 and 42, and "
       "decide whether a number is prime or composite by counting its factors.",
       textbook=["So far, we have been listing all the factors to find the HCF. This can become cumbersome for numbers "
                 "with many factors, as you would have observed for the numbers 30 and 50, and 28 and 42.",
                 "Sometimes, we may also miss some factors which can lead to errors. Can this process be simplified? "
                 "Can it be made more reliable?",
                 "It turns out that using prime factorisation can simplify the process. We will start by revisiting "
                 "primes and prime factorisation.",
                 "Recall that a prime is a number greater than 1 that has only 1 and the number itself as its "
                 "factors. Last year, we tried to find patterns amongst primes between 1 to 100. We also came across "
                 "the Sieve of Eratosthenes, a method to list all primes."],
       teach=["Predict first: is 1 a prime? Is 2? Is 9? Count the factors of each before answering.",
              "A prime has exactly two factors, 1 and itself. So 2, 3, 5, 7, 11 are prime, and 1 is not, because it "
              "has only one factor.",
              "A number greater than 1 with more than two factors is composite. The Sieve of Eratosthenes crosses "
              "out multiples to leave the primes."],
       examples=[
           WE("Which of 1, 2, 9, 13, 21 and 29 are prime? Give the factors that decide it.",
              ["1 has only one factor, itself, so it is neither prime nor composite.",
               "2 has factors 1 and 2 only, so it is prime.",
               "9 has factors 1, 3 and 9, so it is composite.",
               "13 has factors 1 and 13 only, so it is prime.",
               "21 has factors 1, 3, 7 and 21, so it is composite.",
               "29 has factors 1 and 29 only, so it is prime."],
              "2, 13 and 29 are prime; 9 and 21 are composite; 1 is neither", ncert=["3.1.primes"],
              fact="primes", expect=[2, 13, 29])],
       key_terms=["prime", "composite"], misconceptions=["M_PRIME_ONE"], minutes=8),
     DOER("T5.C2", "Practice: prime or composite", None, "Understand",
          "Students decide whether a number is prime or composite by counting its factors, and say why 1 and numbers "
          "such as 91 need extra care.",
          ["A prime is greater than 1 with exactly two factors.",
           "Odd does not mean prime: 9, 15, 21 and 91 are composite."])]))

# ============================== T6 Prime factorisation =======================================================
TOPICS.append(TOPIC(
    "T6", "M1", "Prime Factorisation", ["3.1"], "Apply",
    "Students write a number as a product of primes by splitting composite factors, see that every route gives the "
    "same primes in a different order, and use factor trees and the division method, including for 1200.",
    "Any number splits into primes; different routes give the same primes; the division method is the shortest.",
    [A("T6.C1", "A number as a product of primes", "Understand",
       "Students split 90 into primes along different routes, see the same primes appear in a different order, and "
       "state the prime factorisation of a prime number.",
       textbook=["Any number can be written as a product of primes, keep rewriting composite factors until only "
                 "primes are left.",
                 "Recall that we call this the prime factorisation of a given number. For example, we can find the "
                 "prime factorisation of 90 as follows: 90 = 3 × 3 × 2 × 5.",
                 "The number 90 could also have been factorised as 3 × 30 or 2 × 45 or in a few other different "
                 "ways. Will these all lead to the same prime factors?",
                 "Remarkably, the resulting prime factors are always the same with perhaps only a change in their "
                 "order. For example, if we consider factorising 3 × 30 further, we get 90 = 3 × 30 = 3 × 2 × 15 = "
                 "3 × 2 × 3 × 5, and we have arrived at the same prime factors, just in a different order.",
                 "Note that the prime factorisation of a prime number is the prime number itself."],
       teach=["Predict first: split 90 as 9 × 10, then as 3 × 30. Will the primes at the end match?",
              "Keep replacing any composite factor by two smaller factors until every factor is prime.",
              "Every route ends with the same primes, only in a different order. A prime is its own prime "
              "factorisation."],
       examples=[
           WE("Find the prime factorisation of 90 by starting with 3 × 30, and again by starting with 2 × 45. "
              "Compare the primes.",
              ["90 = 3 × 30.", "30 = 2 × 15 and 15 = 3 × 5, so 90 = 3 × 2 × 3 × 5.",
               "90 = 2 × 45.", "45 = 3 × 15 and 15 = 3 × 5, so 90 = 2 × 3 × 3 × 5.",
               "Both routes give one 2, two 3s and one 5, in a different order.",
               "The prime factorisation of a prime such as 13 is just 13."],
              "90 = 2 × 3 × 3 × 5 by either route", ncert=["3.1.pf_90", "3.1.pf_prime"], fact="pf90",
              expect=[90, [2, 3, 3, 5]])],
       key_terms=["prime factorisation"], misconceptions=["M_ORDER"], minutes=8),
     A("T6.C2", "Factor trees and the division method", "Apply",
       "Students read the factor figures for 105 and 30, use the division method with a vertical bar, and find the "
       "prime factorisation of 1200 by division.",
       textbook=["Can you see what is happening below? Each circled number is the product of the numbers that are to "
                 "its left and below. For example, 30 = 2 × 15, 15 = 3 × 5. Each time, a composite number is "
                 "factorised so that, at least one factor is prime. We stop when we reach a prime number.",
                 "Can you write the prime factorisation of 105 and 30 using these two figures? We collect the prime "
                 "factors along the left and the one at the bottom.",
                 "While carrying out factorisation, the circles are usually left out and the steps are carried out "
                 "in this format: the division method.",
                 "Try finding the prime factorisation of 1200 using the method above. If we had used the earlier "
                 "method, our calculation would have been as follows: 1200 = 40 × 30 = 5 × 8 × 5 × 6 = … Which "
                 "calculation is easier to carry out?"],
       teach=["Predict first: divide 105 by the smallest prime that goes in. What is left, and what next?",
              "In each step one factor is prime and is written on the left; the other factor goes below. Stop when "
              "the number left is prime.",
              "The primes on the left, with the last number, are the prime factorisation. Division is easier to "
              "organise than guessing factor pairs."],
       examples=[
           WE("Use the division method to find the prime factorisation of 105 and of 30.",
              ["105 ÷ 3 = 35, so write 3 on the left and 35 below.",
               "35 ÷ 5 = 7, so write 5 on the left and 7 below.", "7 is prime, so stop: 105 = 3 × 5 × 7.",
               "30 ÷ 2 = 15, so write 2 and then 15.", "15 ÷ 3 = 5, so write 3 and then 5.",
               "5 is prime, so stop: 30 = 2 × 3 × 5."],
              "105 = 3 × 5 × 7 and 30 = 2 × 3 × 5", ncert=["3.1.pf_trees"], fact="pf_trees",
              expect=[[105, [3, 5, 7]], [30, [2, 3, 5]]]),
           WE("Find the prime factorisation of 1200 using the division method.",
              ["1200 ÷ 2 = 600.", "600 ÷ 2 = 300.", "300 ÷ 2 = 150.", "150 ÷ 2 = 75.", "75 ÷ 3 = 25.",
               "25 ÷ 5 = 5.", "5 is prime, so stop.",
               "Collect the divisors and the last number: 2, 2, 2, 2, 3, 5, 5.",
               "So 1200 = 2 × 2 × 2 × 2 × 3 × 5 × 5."],
              "1200 = 2 × 2 × 2 × 2 × 3 × 5 × 5", ncert=["3.1.pf_division"], fact="pf1200",
              expect=[1200, [2, 2, 2, 2, 3, 5, 5]])],
       key_terms=["division method", "factor tree"], misconceptions=["M_ORDER"], minutes=12),
     DOER("T6.C3", "Practice: split into primes", "prime_splitter", "Apply",
          "Students split numbers into primes with a factor tree and with the division method, check that the product "
          "of the primes returns the number, and see different routes meet at the same primes.",
          ["Divide by a prime each time and carry the quotient down.",
           "Stop when the number left is prime.",
           "Multiply all the primes back to check the number."])]))

# ============================== T7 Factors from prime factorisation ==========================================
TOPICS.append(TOPIC(
    "T7", "M1", "Factors from Prime Factorisation", ["3.1"], "Apply",
    "Students use a prime factorisation to decide whether a number is a factor, build every factor of a number from "
    "subparts of its primes, and test Anshu's claim that larger numbers always have longer factorisations.",
    "Every factor is a subpart of the prime factorisation; all factors come from combining the primes systematically.",
    [A("T7.C1", "Is it a factor? Reading factors from primes", "Understand",
       "Students split 840 = 2 × 2 × 2 × 3 × 5 × 7 into two groups of primes to show a number is a factor, and say "
       "why 14 and 8 are factors but 27 is not.",
       textbook=["From the prime factorisation of a number, we can construct all its factors. This can be used to "
                 "simplify the procedure for finding the HCF of two numbers.",
                 "Consider the number 840 and its prime factorisation 2 × 2 × 2 × 3 × 5 × 7. Is 2 × 2 × 7 = 28 a "
                 "factor of 840? If yes, what should it be multiplied by to get 840?",
                 "To answer these questions, we can reorder the prime factors of 840 as follows (recall that "
                 "reordering factors does not change the product): 840 = (2 × 2 × 7) × (2 × 3 × 5). So, 840 = 28 × "
                 "30.",
                 "Thus, (2 × 2 × 7) = 28 is a factor of 840, and it should be multiplied by 30 (2 × 3 × 5) to get "
                 "840.",
                 "Similarly, is 2 × 7 = 14 a factor of 840? Why or why not? Is 2 × 2 × 2 a factor of 840? Why or why "
                 "not? Is 3 × 3 × 3 a factor of 840? Why or why not?"],
       teach=["Predict first: 840 has three 2s, one 3, one 5 and one 7. Is 3 × 3 × 3 a factor?",
              "Any group of these primes, taken from the factorisation, multiplies to a factor. The primes left over "
              "multiply to the partner factor.",
              "A product that uses a prime more times than 840 has it is not a factor."],
       examples=[
           WE("840 = 2 × 2 × 2 × 3 × 5 × 7. Is 28 = 2 × 2 × 7 a factor? What multiplies it to give 840? Are "
              "14, 8 and 27 factors?",
              ["Reorder: 840 = (2 × 2 × 7) × (2 × 3 × 5).", "So 840 = 28 × 30, and 28 is a factor with partner 30.",
               "14 = 2 × 7 uses one 2 and one 7, both available, so 14 is a factor.",
               "2 × 2 × 2 = 8 uses three 2s, and 840 has three 2s, so 8 is a factor.",
               "3 × 3 × 3 needs three 3s, but 840 has only one 3, so 27 is not a factor."],
              "28, 14 and 8 are factors of 840 (28 × 30 = 840); 27 is not", ncert=["3.1.f840"], fact="f840",
              expect=[840, 28, 30])],
       key_terms=["factor", "subpart"], misconceptions=["M_ORDER"], minutes=10),
     A("T7.C2", "All the factors of a number from its primes", "Apply",
       "Students list all the factors of 225 by combining its primes one, two, three and four at a time, add 1, and "
       "check the list against a direct count.",
       textbook=["Can we use this idea to list down all the possible factors of a number using just its prime "
                 "factors? Find the factors of 225 using prime factorisation.",
                 "Factorising 225 to its primes, we get 225 = 5 × 5 × 3 × 3. We have seen that any 'subpart' of "
                 "this factorisation gives us a factor. Let us systematically form these subparts.",
                 "Prime factors: 3, 5. Combination of two prime factors: 3 × 3 = 9, 5 × 5 = 25, 3 × 5 = 15. "
                 "Combination of three prime factors: 3 × 3 × 5 = 45, 3 × 5 × 5 = 75. Combination of four prime "
                 "factors: 3 × 3 × 5 × 5 = 225. Adding 1 to this list of factors, we see that the factors of 225 "
                 "are 1, 3, 5, 9, 15, 25, 45, 75, 225.",
                 "Check that all the factors of 225 occur in this list."],
       teach=["Predict first: how many factors might 225 have? Guess a number, then count.",
              "Take the primes one at a time, then two, then three, then all four. Remove repeats and add 1.",
              "Then check by division that no factor of 225 is missing."],
       examples=[
           WE("List all the factors of 225 using its prime factorisation.",
              ["225 = 5 × 5 × 3 × 3.", "One prime: 3 and 5.", "Two primes: 3 × 3 = 9, 5 × 5 = 25, 3 × 5 = 15.",
               "Three primes: 3 × 3 × 5 = 45, 3 × 5 × 5 = 75.", "Four primes: 3 × 3 × 5 × 5 = 225.",
               "Add the factor 1.", "The factors are 1, 3, 5, 9, 15, 25, 45, 75, 225."],
              "1, 3, 5, 9, 15, 25, 45, 75, 225", ncert=["3.1.f225"], fact="f225",
              expect=[1, 3, 5, 9, 15, 25, 45, 75, 225])],
       key_terms=["factor", "prime factorisation"], minutes=10),
     A("T7.C3", "Anshu's claim about longer factorisations", "Evaluate",
       "Students test the claim that a larger number always has a longer prime factorisation, disprove it with 96 and "
       "121, and name a conjecture and a counterexample.",
       textbook=["After observing a few prime factorisations, Anshu claims 'The larger a number is, the longer its "
                 "prime factorisation will be'. What do you think of Anshu's claim?",
                 "We can see that it is not true. For example, look at the prime factorisations of 96 and 121. "
                 "96 = 2 × 2 × 2 × 2 × 2 × 3, 121 = 11 × 11.",
                 "In mathematics, statements or claims made without proof or verification are called 'conjectures'. "
                 "Anshu's claim is a conjecture. We disproved this conjecture by finding a counterexample, i.e., an "
                 "example where the conjecture is false."],
       teach=["Predict first: which is longer, the factorisation of 96 or of 121? Which number is bigger?",
              "One counterexample is enough to show a claim is false.",
              "A claim that has not been proved or disproved is a conjecture."],
       examples=[
           WE("Anshu says: the larger a number is, the longer its prime factorisation will be. Test this with 96 and "
              "121.",
              ["96 = 2 × 2 × 2 × 2 × 2 × 3, which has six primes.", "121 = 11 × 11, which has two primes.",
               "121 is the larger number, but its factorisation is shorter.",
               "So the claim fails for this pair. One such example, a counterexample, disproves it."],
              "The claim is false: 121 is larger than 96 but has a shorter factorisation", ncert=["3.1.anshu_claim"],
              fact="anshu", expect=[96, 121])],
       key_terms=["conjecture", "counterexample"], misconceptions=["M_LONGER_BIGGER"], minutes=8),
     DOER("T7.C4", "Practice: build all the factors", "factor_builder", "Apply",
          "Students build the full factor list of a number from the subparts of its prime factorisation, in order, "
          "and check that no factor is missing and none is repeated.",
          ["List the primes, then combine them one, two, three and more at a time.",
           "Remove repeats, add 1, and check the count."],
          items=[FIO("3.1.FiO_factors", "Figure it Out (listing factors)",
                     "List all the factors of the following numbers: (a) 90 (b) 105 (c) 132 (d) 360 (this number has "
                     "24 factors) (e) 840 (this number has 32 factors)",
                     ["(a) 90 = 2 × 3 × 3 × 5. Factors: 1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45, 90.",
                      "(b) 105 = 3 × 5 × 7. Factors: 1, 3, 5, 7, 15, 21, 35, 105.",
                      "(c) 132 = 2 × 2 × 3 × 11. Factors: 1, 2, 3, 4, 6, 11, 12, 22, 33, 44, 66, 132.",
                      "(d) 360 = 2 × 2 × 2 × 3 × 3 × 5. It has 24 factors: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, "
                      "20, 24, 30, 36, 40, 45, 60, 72, 90, 120, 180, 360.",
                      "(e) 840 = 2 × 2 × 2 × 3 × 5 × 7. It has 32 factors: 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 15, "
                      "20, 21, 24, 28, 30, 35, 40, 42, 56, 60, 70, 84, 105, 120, 140, 168, 210, 280, 420, 840."],
                     "(a) 12 factors (b) 8 factors (c) 12 factors (d) 24 factors (e) 32 factors, listed above",
                     expect=[90, 105, 132, 360, 840], tool="factor_builder")],
          ncert=["3.1.FiO_factors"], misconceptions=["M_ORDER"])]))

# ============================== T8 HCF by common subparts ====================================================
TOPICS.append(TOPIC(
    "T8", "M1", "HCF from Common Subparts of Primes", ["3.1"], "Apply",
    "Students find the common factors and the HCF of two numbers by writing both prime factorisations and listing "
    "the subparts they share, including the case where only 1 is common.",
    "Common factors are subparts of both prime factorisations; the largest common subpart is the HCF.",
    [A("T8.C1", "Common subparts of 45 and 75", "Apply",
       "Students write the prime factorisations of 45 and 75, list the subparts common to both, and read off the "
       "common factors and the HCF.",
       textbook=["We now see how to make use of the observations made so far to find common factors and the Highest "
                 "Common Factor (HCF).",
                 "Example 1: Find the common factors, and the HCF of 45 and 75. Calculate the prime factorisation "
                 "for both numbers: 45 = 3 × 3 × 5, 75 = 3 × 5 × 5.",
                 "We have seen: Factors of 45 are subparts of factors occurring in 3 × 3 × 5 and factors of 75 are "
                 "subparts of factors occurring in 3 × 5 × 5. So the common factors should be subparts of both the "
                 "factorisations. Can you write them down?",
                 "3, 5, 3 × 5 = 15 are subparts of both, and hence, they are the common factors along with 1. The "
                 "highest among them is 15. So, their HCF = 15."],
       teach=["Predict first: which primes do 45 and 75 share, and how many of each?",
              "Write both factorisations one under the other and list the subparts that appear in both.",
              "Add 1. The greatest of these common factors is the HCF."],
       examples=[
           WE("Find the common factors and the HCF of 45 and 75.",
              ["45 = 3 × 3 × 5.", "75 = 3 × 5 × 5.",
               "Subparts in both: 3, 5 and 3 × 5 = 15.", "Together with 1, the common factors are 1, 3, 5, 15.",
               "The highest is 15."],
              "Common factors 1, 3, 5, 15; HCF is 15", ncert=["3.1.ex1"], fact="ex1_hcf", expect=[45, 75, 15])],
       key_terms=["common factor", "HCF"], misconceptions=["M_COMMON_ONLY"], minutes=8),
     A("T8.C2", "Common subparts of 112 and 84", "Apply",
       "Students list all the subparts common to 112 = 2 × 2 × 2 × 2 × 7 and 84 = 2 × 2 × 3 × 7, and name the "
       "common factors and the HCF.",
       textbook=["Example 2: Find the common factors, and the HCF of 112 and 84. Calculating prime factorisations, "
                 "we get, 112 = 2 × 2 × 2 × 2 × 7 and 84 = 2 × 2 × 3 × 7.",
                 "Finding the common subparts, we get 2, 7, 2 × 2, 2 × 7, 2 × 2 × 7.",
                 "The highest among the common factors, HCF, is 2 × 2 × 7 = 28."],
       teach=["Predict first: 112 has four 2s and 84 has two. How many 2s can a common subpart use?",
              "Match the subparts of the two factorisations: 2, 7, 2 × 2, 2 × 7 and 2 × 2 × 7.",
              "The largest common subpart is 2 × 2 × 7, so the HCF is 28."],
       examples=[
           WE("Find the common factors and the HCF of 112 and 84 from their prime factorisations.",
              ["112 = 2 × 2 × 2 × 2 × 7.", "84 = 2 × 2 × 3 × 7.",
               "Common subparts: 2, 7, 2 × 2 = 4, 2 × 7 = 14, 2 × 2 × 7 = 28.",
               "With 1, the common factors are 1, 2, 4, 7, 14, 28.", "The highest is 2 × 2 × 7 = 28."],
              "Common factors 1, 2, 4, 7, 14, 28; HCF is 28", ncert=["3.1.ex2"], fact="ex2_hcf",
              expect=[112, 84, 28])],
       key_terms=["common factor", "HCF"], minutes=8),
     A("T8.C3", "When only 1 is common: 96 and 275", "Apply",
       "Students show that 96 and 275 share no prime, conclude that 1 is their only common factor and so their HCF, "
       "and say what such numbers are called.",
       textbook=["Example 3: Find the common factors and the HCF of 96 and 275. We have 96 = 2 × 2 × 2 × 2 × 2 × 3, "
                 "275 = 5 × 5 × 11.",
                 "There is no subpart that is common amongst these two factorisations. So, 1 is the only common "
                 "factor. It is also their HCF."],
       teach=["Predict first: 96 and 275 share no prime. What does that say about their common factors?",
              "With no common prime there is no common subpart, so the only common factor is 1.",
              "When the HCF of two numbers is 1, the numbers are called co-prime."],
       examples=[
           WE("Find the common factors and the HCF of 96 and 275.",
              ["96 = 2 × 2 × 2 × 2 × 2 × 3.", "275 = 5 × 5 × 11.",
               "No prime appears in both factorisations, so no subpart is common.",
               "The only common factor is 1, so the HCF is 1."],
              "The only common factor is 1, so the HCF is 1", ncert=["3.1.ex3"], fact="ex3_hcf",
              expect=[96, 275, 1])],
       key_terms=["co-prime", "HCF"], misconceptions=["M_COPRIME_ONE_FACTOR"], minutes=6),
     DOER("T8.C4", "Practice: common subparts and the HCF", None, "Apply",
          "Students write two prime factorisations side by side, pick out the common subparts, and list the common "
          "factors and the HCF, including pairs with no common prime.",
          ["Factorise both numbers into primes.", "Common factors are the subparts present in both.",
           "If there is no common prime, the HCF is 1."],
          items=[FIO("3.1.FiO_common", "Figure it Out (common factors and HCF)",
                     "Find the common factors and the HCF of the following numbers: (a) 50, 60 (b) 140, 275 "
                     "(c) 77, 725 (d) 370, 592 (e) 81, 243",
                     ["(a) 50 = 2 × 5 × 5 and 60 = 2 × 2 × 3 × 5. Common subparts: 2, 5, 2 × 5 = 10. Common "
                      "factors 1, 2, 5, 10; HCF 10.",
                      "(b) 140 = 2 × 2 × 5 × 7 and 275 = 5 × 5 × 11. Common subpart: 5. Common factors 1, 5; HCF 5.",
                      "(c) 77 = 7 × 11 and 725 = 5 × 5 × 29. No common prime. Common factor 1; HCF 1.",
                      "(d) 370 = 2 × 5 × 37 and 592 = 2 × 2 × 2 × 2 × 37. Common subparts: 2, 37, 2 × 37 = 74. "
                      "Common factors 1, 2, 37, 74; HCF 74.",
                      "(e) 81 = 3 × 3 × 3 × 3 and 243 = 3 × 3 × 3 × 3 × 3. Common subparts are 3, 9, 27, 81. "
                      "Common factors 1, 3, 9, 27, 81; HCF 81."],
                     "(a) 1, 2, 5, 10; HCF 10 (b) 1, 5; HCF 5 (c) 1; HCF 1 (d) 1, 2, 37, 74; HCF 74 "
                     "(e) 1, 3, 9, 27, 81; HCF 81",
                     expect=[10, 5, 1, 74, 81])],
          ncert=["3.1.FiO_common"], misconceptions=["M_COMMON_ONLY"])]))

# ============================== T9 HCF as the minimum count ==================================================
TOPICS.append(TOPIC(
    "T9", "M1", "HCF by Taking the Minimum of Each Prime", ["3.1"], "Apply",
    "Students find the HCF directly, without listing common factors, by taking each common prime the minimum number of "
    "times it occurs, for two numbers or more, and test a claim about factorisations into composite numbers.",
    "HCF = product of the common primes, each taken the minimum number of times it occurs across the numbers.",
    [A("T9.C1", "Minimum count of each common prime: 30 and 72", "Apply",
       "Students identify the common primes of 30 and 72, count how many times each occurs in each number, and build "
       "the HCF by taking the minimum count of each.",
       textbook=["How do we directly find the HCF without listing all the factors?",
                 "Example 4: Find the HCF of 30 and 72. 30 = 2 × 3 × 5, 72 = 2 × 2 × 2 × 3 × 3. We need the largest "
                 "common subpart to find the HCF. Clearly, it will contain only those primes that occur in both the "
                 "factorisations: 2 and 3 in this case.",
                 "How many 2s will it contain? The prime factorisation of 30 has only one 2. So, the largest common "
                 "subpart should contain only one 2.",
                 "How many 3s will it contain? The prime factorisation of 30 has only one 3. So, the largest common "
                 "subpart should contain only one 3.",
                 "30 = 2 × 3 × 5, 72 = 2 × 2 × 2 × 3 × 3, HCF = 2 × 3 = 6. Thus, to find the HCF, we identify the "
                 "common primes and find the minimum number of times each of them appear in the factorisations of "
                 "the given numbers."],
       teach=["Predict first: 30 has one 2 and 72 has three 2s. How many 2s can the HCF have?",
              "Take only the primes in both numbers. For each, take the smaller count.",
              "Multiply those primes to get the HCF."],
       examples=[
           WE("Find the HCF of 30 and 72 using the minimum count of each common prime.",
              ["30 = 2 × 3 × 5.", "72 = 2 × 2 × 2 × 3 × 3.", "Common primes: 2 and 3.",
               "2 occurs once in 30 and three times in 72, so take it once.",
               "3 occurs once in 30 and twice in 72, so take it once.", "HCF = 2 × 3 = 6."],
              "6", ncert=["3.1.ex4"], fact="ex4_hcf", expect=[30, 72, 6])],
       key_terms=["HCF", "minimum"], misconceptions=["M_MIN_MAX"], minutes=8),
     A("T9.C2", "The same idea for 225 and 750, and for more numbers", "Apply",
       "Students find the HCF of 225 and 750 by minimum counts, and extend the same method to three numbers by "
       "keeping only primes that appear in all of them.",
       textbook=["Example 5: Find the HCF of 225 and 750. 225 = 3 × 3 × 5 × 5, 750 = 2 × 3 × 5 × 5 × 5. Common "
                 "primes: 3 and 5. Let us find the largest common subpart.",
                 "How many 3s will it contain? 750 contains only one 3, which is the minimum number of 3 across both "
                 "numbers. So the largest common subpart should contain only one 3.",
                 "How many 5s will it contain? 225 contains the minimum number of 5s which occurs two times. So, the "
                 "largest common subpart should contain two 5s, i.e., 5 × 5.",
                 "225 = 3 × 3 × 5 × 5, 750 = 2 × 3 × 5 × 5 × 5, HCF = 3 × 5 × 5 = 75.",
                 "To find the HCF of more than 2 numbers, a similar method of finding the largest common subpart of "
                 "the common primes can be followed."],
       teach=["Predict first: 225 has two 5s and 750 has three. How many 5s go in the HCF?",
              "Repeat the same steps prime by prime: 3 once, 5 twice. A prime missing from any one number is "
              "left out.",
              "With three or more numbers, keep only primes that appear in all of them, each at its minimum count."],
       examples=[
           WE("Find the HCF of 225 and 750.",
              ["225 = 3 × 3 × 5 × 5.", "750 = 2 × 3 × 5 × 5 × 5.", "Common primes: 3 and 5.",
               "3 occurs twice in 225 and once in 750, so take it once.",
               "5 occurs twice in 225 and three times in 750, so take it twice.",
               "HCF = 3 × 5 × 5 = 75."],
              "75", ncert=["3.1.ex5"], fact="ex5_hcf", expect=[225, 750, 75]),
           WE("Find the HCF of 36, 60 and 84 by the same method for more than two numbers.",
              ["36 = 2 × 2 × 3 × 3.", "60 = 2 × 2 × 3 × 5.", "84 = 2 × 2 × 3 × 7.",
               "Primes in all three: 2 and 3.", "The minimum count of 2 is two and of 3 is one.",
               "HCF = 2 × 2 × 3 = 12."],
              "12", ncert=["3.1.more_than_two"], fact="three_hcf", expect=[36, 60, 84, 12])],
       key_terms=["HCF", "minimum"], misconceptions=["M_MIN_MAX"], minutes=10),
     DOER("T9.C3", "Practice: minimum counts", "hcf_min_count", "Apply",
          "Students build the HCF prime by prime from the minimum count in each factorisation, for two or three "
          "numbers, and test why composite-looking factorisations can hide common primes.",
          ["Keep only primes that appear in every number.", "For each, take the smaller count.",
           "Multiply to get the HCF."],
          items=[FIO("3.1.FiO_hcf1", "Figure it Out (HCF), Q1",
                     "Find the HCF of the following numbers: (a) 24, 180 (b) 42, 75, 24 (c) 240, 378 (d) 400, 2500 "
                     "(e) 300, 800",
                     ["(a) 24 = 2 × 2 × 2 × 3, 180 = 2 × 2 × 3 × 3 × 5. Minimum counts: 2 twice, 3 once. "
                      "HCF = 2 × 2 × 3 = 12.",
                      "(b) 42 = 2 × 3 × 7, 75 = 3 × 5 × 5, 24 = 2 × 2 × 2 × 3. Only 3 is in all three, once. HCF = 3.",
                      "(c) 240 = 2 × 2 × 2 × 2 × 3 × 5, 378 = 2 × 3 × 3 × 3 × 7. Common: 2 once, 3 once. "
                      "HCF = 2 × 3 = 6.",
                      "(d) 400 = 2 × 2 × 2 × 2 × 5 × 5, 2500 = 2 × 2 × 5 × 5 × 5 × 5. Common: 2 twice, 5 twice. "
                      "HCF = 2 × 2 × 5 × 5 = 100.",
                      "(e) 300 = 2 × 2 × 3 × 5 × 5, 800 = 2 × 2 × 2 × 2 × 2 × 5 × 5. Common: 2 twice, 5 twice. "
                      "HCF = 2 × 2 × 5 × 5 = 100."],
                     "(a) 12 (b) 3 (c) 6 (d) 100 (e) 100", expect=[12, 3, 6, 100, 100], tool="hcf_min_count"),
                FIO("3.1.FiO_hcf2", "Figure it Out (HCF), Q2",
                    "Consider the numbers 72 and 144. Suppose they are factorised into composite numbers as: "
                    "72 = 6 × 12 and 144 = 8 × 18. Seeing this, can one say that these two numbers have no common "
                    "factor other than 1? Why not?",
                    ["The factors 6, 12, 8 and 18 are composite, so the factorisations are not prime factorisations.",
                     "Break them down: 72 = 6 × 12 = 2 × 3 × 2 × 2 × 3, and 144 = 8 × 18 = 2 × 2 × 2 × 2 × 3 × 3.",
                     "Both numbers contain 2 and 3, so they share primes.",
                     "Their HCF is 72, so they have many common factors."],
                    "No: 6 × 12 and 8 × 18 are not prime factorisations; in primes both contain 2 and 3, and the HCF "
                    "of 72 and 144 is 72", expect=[72, 144, 72], tool="hcf_min_count")],
          ncert=["3.1.FiO_hcf1", "3.1.FiO_hcf2"], misconceptions=["M_COPRIME_ONE_FACTOR", "M_MIN_MAX"])]))
