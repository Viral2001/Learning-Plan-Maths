# -*- coding: utf-8 -*-
"""Topics T6 to T8 (module M2): square roots as sides, the prime factor test, and estimating square roots.
Book pp 7 to 11."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T6 Square roots as side lengths =============================================
TOPICS.append(TOPIC(
    "T6", "M2", "Square Roots: The Side from the Area", ["1.1"], "Apply",
    "Students find the side of a square from its area as a square root, recognise that a square has two square "
    "roots of which the positive one is used here, and find square roots by listing squares and by subtracting odd "
    "numbers.",
    "Squaring and finding the square root undo each other. A positive number has two square roots, one positive and "
    "one negative; the side of a square is the positive one. Roots can be found by listing squares near the number "
    "or by subtracting consecutive odd numbers.",
    [A("T6.C1", "The side of a square from its area", "Understand",
       "Students find the side of a square of given area, describe finding a square root as the reverse of squaring, "
       "and explain why 64 has the two square roots 8 and −8.",
       textbook=["Square Roots",
                 "The area of a square is 49 sq cm. What is the length of its side? It is 7 cm, because 7² = 49.",
                 "If y = x², then x is a square root of y.",
                 "What is the square root of 64? Both 8² = 64 and (−8)² = 64, so 64 has two square roots, 8 and −8. "
                 "Similarly the square roots of 100 are 10 and −10.",
                 "In this chapter we will only consider the positive square root, written with the symbol √."],
       teach=["Predict first: a square has area 64 square cm. Is its side 32 cm, 16 cm or 8 cm?",
              "The side times itself must give 64, and 8 × 8 = 64, so the side is 8 cm. Halving gives 32, which is wrong.",
              "Finding a square root undoes squaring. But (−8)² = 64 as well, so 64 has two square roots, 8 and −8.",
              "A length cannot be negative, so for sides and in this chapter we use the positive root: √64 = 8."],
       examples=[
           WE("A square has area 64 square cm. Find its side, and give both square roots of 64.",
              ["The side s satisfies s × s = 64.",
               "8 × 8 = 64, so the side is 8 cm.",
               "Also (−8)² = −8 × −8 = 64, so the square roots of 64 are 8 and −8.",
               "A side is a length, so it is the positive root, 8 cm."],
              "The side is 8 cm; the square roots of 64 are 8 and −8", ncert=["1.1.root_side", "1.1.root_def"])],
       key_terms=["square root", "positive square root"], misconceptions=["M_ROOT_HALF", "M_ROOT_ONE_SIGN"], minutes=8),
     A("T6.C2", "Find a root by listing squares", "Apply",
       "Students rule out numbers as squares by their last digit and find the square root of a perfect square by "
       "listing the squares of numbers close to its root.",
       textbook=["Is 576 a perfect square? Is 327? How can we find their square roots?",
                 "Squares end in 0, 1, 4, 5, 6 or 9, so 327, which ends in 7, is not a perfect square.",
                 "Method 1: list the squares near it. 20² = 400, 21² = 441, 22² = 484, 23² = 529, 24² = 576. "
                 "So √576 = 24."],
       teach=["Predict first: which of 576 and 327 could be a perfect square?",
              "327 ends in 7, and no square ends in 7, so 327 is out.",
              "For 576: 20² = 400 is too small and 30² = 900 too big, so the root is in the twenties.",
              "List 21², 22², 23², 24² until you hit 576: √576 = 24."],
       examples=[
           WE("Decide whether 576 and 327 are perfect squares, and find the square root of the one that is.",
              ["327 ends in 7, and no square ends in 7, so 327 is not a perfect square.",
               "20² = 400 and 30² = 900, so the root of 576 is between 20 and 30.",
               "21² = 441, 22² = 484, 23² = 529, 24² = 576.",
               "So 576 is a perfect square and √576 = 24."],
              "Only 576 is a perfect square, and √576 = 24", ncert=["1.1.mt_576"])],
       key_terms=["square root", "listing"], misconceptions=["M_DIGIT_ENOUGH"], minutes=8),
     A("T6.C3", "Find a root by subtracting odd numbers", "Apply",
       "Students find the square root of a perfect square by counting the consecutive odd numbers subtracted to "
       "reach 0, and judge when this method is too slow.",
       textbook=["Method 2: successive subtraction of odd numbers. 81 − 1 = 80, 80 − 3 = 77, 77 − 5 = 72, "
                 "72 − 7 = 65, 65 − 9 = 56, 56 − 11 = 45, 45 − 13 = 32, 32 − 15 = 17, 17 − 17 = 0. We subtracted "
                 "9 odd numbers, so √81 = 9.",
                 "Finding √729 this way would take a long time."],
       teach=["Predict first: how many odd numbers must you subtract from 81 to reach 0?",
              "81 is the sum of the first few odd numbers; the count of those odd numbers is the root.",
              "Subtract 1, 3, 5, ... and count: 9 steps reach 0, so √81 = 9.",
              "For a big number like 729 this needs 27 steps, so a faster method is needed."],
       examples=[
           WE("Find √81 by successive subtraction of odd numbers.",
              ["81 − 1 = 80, 80 − 3 = 77, 77 − 5 = 72.",
               "72 − 7 = 65, 65 − 9 = 56, 56 − 11 = 45.",
               "45 − 13 = 32, 32 − 15 = 17, 17 − 17 = 0.",
               "9 odd numbers were subtracted, so √81 = 9."],
              "√81 = 9", ncert=["1.1.subtract_root"])],
       key_terms=["square root", "successive subtraction"], misconceptions=["M_ROOT_HALF"], minutes=6),
     DOER("T6.C4", "Practice: find the side from the area", "root_as_side", "Apply",
          "Students resize a square to match a given area, read off the side as the square root, and see that an "
          "area that is not a perfect square has a side between two whole numbers.",
          ["The side of a square is the positive square root of its area.",
           "A square root is not half the number.",
           "List squares near the number, or subtract odd numbers, to find a root."],
          items=[
              FIO("FiO1.q4", "Figure it Out (square numbers, question 4)",
                  "What is the length of the side of a square whose area is 441 m²?",
                  ["The side is √441.",
                   "20² = 400 and 30² = 900, so the side is between 20 and 30.",
                   "441 ends in 1, so the root ends in 1 or 9: 21 or 29.",
                   "21² = 441, so the side is 21 m."],
                  "21 m")])],
    key_terms=["square root", "side"]))

# ============================== T7 The prime factor test ====================================================
TOPICS.append(TOPIC(
    "T7", "M2", "Prime Factors Decide Squares", ["1.1"], "Analyze",
    "Students write the prime factorisation of a number, decide whether it is a perfect square by splitting the "
    "primes into two equal groups, read off the square root, and find the smallest number that turns a number into "
    "a perfect square.",
    "A number is a perfect square exactly when its prime factors can be split into two identical groups, that is, "
    "when every prime appears an even number of times. One group multiplied out is the square root.",
    [A("T7.C1", "Two equal groups of prime factors", "Analyze",
       "Students factorise a number into primes, split the primes into two identical groups when possible, and "
       "conclude whether the number is a perfect square and what its root is.",
       textbook=["Method 3: prime factorisation.",
                 "Is 324 a perfect square? 324 = 2 × 2 × 3 × 3 × 3 × 3. The prime factors can be split into two equal "
                 "groups, 2 × 3 × 3 and 2 × 3 × 3. So 324 = (2 × 3 × 3)² = 18², and √324 = 18.",
                 "Is 156 a perfect square? 156 = 2 × 2 × 3 × 13. The factors 3 and 13 cannot be paired, so 156 is not "
                 "a perfect square."],
       teach=["Predict first: is 324 a perfect square? It ends in 4, so it might be.",
              "Factorise: 324 = 2 × 2 × 3 × 3 × 3 × 3. Every prime appears an even number of times.",
              "Split into two equal groups, 2 × 3 × 3 each, so 324 = 18 × 18 and √324 = 18.",
              "For 156 = 2 × 2 × 3 × 13, the 3 and the 13 have no partner, so 156 is not a square. Having one "
              "repeated prime is not enough."],
       examples=[
           WE("Use prime factorisation to decide whether 324 and 156 are perfect squares.",
              ["324 = 2 × 2 × 3 × 3 × 3 × 3.",
               "The primes split into two equal groups: (2 × 3 × 3) × (2 × 3 × 3) = 18 × 18 = 324.",
               "156 = 2 × 2 × 3 × 13; the 3 and the 13 cannot be paired.",
               "So 324 = 18² is a perfect square and 156 is not."],
              "324 is a perfect square with √324 = 18; 156 is not a perfect square",
              ncert=["1.1.prime_324", "1.1.prime_156"])],
       key_terms=["prime factorisation", "pairing"], misconceptions=["M_PRIME_ANY", "M_DIGIT_ENOUGH"], minutes=10),
     A("T7.C1x", "Test 1156 and 2800 by pairing primes", "Apply",
       "Students factorise 1156 and 2800 into primes and use the pairing test to decide which is a perfect square.",
       teach=["Predict first: 1156 ends in 6 and 2800 ends in two zeros. Are both squares?",
              "Factorise and look for a prime with no partner."],
       examples=[
           WE("Using prime factorisation, find whether 1156 and 2800 are perfect squares.",
              ["1156 = 2 × 2 × 17 × 17, so it splits as (2 × 17) × (2 × 17) = 34 × 34.",
               "So 1156 = 34², a perfect square.",
               "2800 = 2 × 2 × 2 × 2 × 5 × 5 × 7; the single 7 has no partner.",
               "So 2800 is not a perfect square, even though it ends in two zeros."],
              "1156 = 34² is a perfect square; 2800 is not", ncert=["1.1.prime_try"])],
       key_terms=["prime factorisation"], misconceptions=["M_DIGIT_ENOUGH", "M_PRIME_ANY"], minutes=6, thin=True),
     DOER("T7.C2", "Practice: pair the prime factors", "prime_pairing", "Analyze",
          "Students drag prime factors into pairs, decide whether a number is a perfect square, and find the "
          "smallest multiplier or divisor that leaves every prime paired.",
          ["A perfect square has every prime factor appearing an even number of times.",
           "One group of the pairs, multiplied out, is the square root.",
           "Multiplying by the unpaired primes makes the smallest perfect square multiple."],
          items=[
              FIO("FiO1.q5", "Figure it Out (square numbers, question 5)",
                  "Find the smallest square number that is divisible by each of the following numbers: 4, 9 and 10.",
                  ["The number must be a multiple of 4 = 2 × 2, 9 = 3 × 3 and 10 = 2 × 5.",
                   "The smallest such multiple is 2 × 2 × 3 × 3 × 5 = 180.",
                   "In 180 the 5 has no partner, so multiply by 5: 180 × 5 = 900.",
                   "900 = 2 × 2 × 3 × 3 × 5 × 5 = 30², and it is divisible by 4, 9 and 10."],
                  "900"),
              FIO("FiO1.q6", "Figure it Out (square numbers, question 6)",
                  "Find the smallest number by which 9408 must be multiplied so that the product is a perfect square. "
                  "Find the square root of the product.",
                  ["9408 = 2 × 2 × 2 × 2 × 2 × 2 × 3 × 7 × 7.",
                   "The 2s and the 7s pair up; the single 3 has no partner.",
                   "Multiply by 3: 9408 × 3 = 28224.",
                   "28224 = (2 × 2 × 2 × 3 × 7)² = 168²."],
                  "Multiply by 3; the product 28224 has square root 168"),
              FIO("FiO1.q9", "Figure it Out (square numbers, question 9)",
                  "How many tiny squares are there in the picture of 9 rows of 9 tiles, where every tile, upright or "
                  "turned, is a grid of 5 by 5 tiny squares? Write the prime factorisation of the number of tiny "
                  "squares.",
                  ["There are 9 × 9 = 81 tiles.",
                   "Each tile has 5 × 5 = 25 tiny squares.",
                   "Total: 81 × 25 = 2025.",
                   "2025 = 3 × 3 × 3 × 3 × 5 × 5 = 3⁴ × 5², so the primes pair up and 2025 = 45²."],
                  "2025 tiny squares, and 2025 = 3⁴ × 5², which is 45²")])],
    key_terms=["prime factorisation", "perfect square"]))

# ============================== T8 Estimating square roots ==================================================
TOPICS.append(TOPIC(
    "T8", "M2", "Estimating Square Roots", ["1.1"], "Evaluate",
    "Students trap a square root between two consecutive whole numbers using nearby squares, use the last digit to "
    "pin down the root of a perfect square, and judge estimates in a real problem.",
    "Nearby squares trap a square root: if a² is below the number and (a + 1)² above, the root lies between a and "
    "a + 1. For a perfect square, the tens are fixed by the trap and the units by the last digit.",
    [A("T8.C1", "Pin down the root of a perfect square", "Apply",
       "Students locate the root of a large perfect square between two multiples of 10, narrow it to two candidates "
       "with the last digit, and choose by comparing with the square of the middle number.",
       textbook=["Estimating Square Roots",
                 "Find √1936. Since 40² = 1600 and 50² = 2500, the root lies between 40 and 50.",
                 "1936 ends in 6, so the root ends in 4 or 6: it is 44 or 46.",
                 "45² = 2025, which is more than 1936, so the root is less than 45. So √1936 = 44."],
       teach=["Predict first: is √1936 nearer 40 or nearer 50?",
              "40² = 1600 and 50² = 2500 trap the root between 40 and 50.",
              "Squares ending in 6 come from numbers ending in 4 or 6, so the root is 44 or 46.",
              "45² = 2025 is above 1936, so the root is below 45: √1936 = 44."],
       examples=[
           WE("Find √1936 without long multiplication.",
              ["40² = 1600 < 1936 < 2500 = 50², so the root is between 40 and 50.",
               "1936 ends in 6, so the root ends in 4 or 6: 44 or 46.",
               "45² = 2025 > 1936, so the root is less than 45.",
               "So √1936 = 44. Check: 44 × 44 = 1936."],
              "√1936 = 44", ncert=["1.1.est_1936"])],
       key_terms=["estimate", "square root"], misconceptions=["M_ROOT_NEAREST"], minutes=8),
     A("T8.C2", "A root between two whole numbers", "Analyze",
       "Students trap the square root of a number that is not a perfect square between two consecutive whole numbers "
       "and say which one it is closer to.",
       textbook=["Aribam and Bijou play a game. One says a number and the other guesses its square root. Aribam says "
                 "25, Bijou says 5. Bijou says 81, Aribam says 9. Then Aribam says 250.",
                 "250 is not a perfect square. 10² = 100 and 14² = 196 are too small, and 15² = 225 and 16² = 256 "
                 "trap it: √250 lies between 15 and 16, closer to 16."],
       teach=["Predict first: Bijou must guess √250. Is it a whole number?",
              "250 ends in a single 0, and squares end in an even number of zeros, so 250 is not a perfect square.",
              "15² = 225 < 250 < 256 = 16², so √250 lies between 15 and 16.",
              "250 is much closer to 256 than to 225, so √250 is a little less than 16."],
       examples=[
           WE("Between which two consecutive whole numbers does √250 lie, and which is it closer to?",
              ["15² = 225 and 16² = 256.",
               "225 < 250 < 256, so √250 is between 15 and 16.",
               "256 − 250 = 6 while 250 − 225 = 25, so √250 is closer to 16."],
              "√250 lies between 15 and 16, closer to 16", ncert=["1.1.est_game"])],
       key_terms=["estimate", "consecutive whole numbers"], misconceptions=["M_ROOT_NEAREST"], minutes=8),
     A("T8.C3", "Akhil's handkerchief", "Evaluate",
       "Students decide whether a square of a given whole number side can be cut from a square cloth of given area, "
       "and find the largest whole number side possible.",
       textbook=["Akhil has a square piece of cloth of area 125 cm². He wants to make a square handkerchief of side "
                 "15 cm. Is it possible? If not, what is the largest whole number side of the handkerchief he can "
                 "make?"],
       teach=["Predict first: can a 15 cm handkerchief come out of a cloth of area 125 cm²?",
              "A 15 cm square needs 15² = 225 cm², far more than 125 cm².",
              "11² = 121 ≤ 125 < 144 = 12², so the side of the cloth is between 11 and 12 cm.",
              "The largest whole number side is 11 cm."],
       examples=[
           WE("Akhil's square cloth has area 125 cm². Can he cut a square handkerchief of side 15 cm? What is the "
              "largest whole number side he can cut?",
              ["A side of 15 cm needs an area of 15² = 225 cm², but the cloth has only 125 cm².",
               "So 15 cm is not possible.",
               "11² = 121 and 12² = 144, so the cloth's side is between 11 cm and 12 cm.",
               "The largest whole number side is 11 cm."],
              "No; the largest whole number side is 11 cm", ncert=["1.1.est_cloth"])],
       key_terms=["estimate", "area"], misconceptions=["M_ROOT_NEAREST"], minutes=6),
     DOER("T8.C4", "Practice: trap the root", "root_between", "Evaluate",
          "Students slide two whole number bounds until their squares trap a given number, decide whether it is a "
          "perfect square, and say which bound the root is closer to.",
          ["If a² < N < (a + 1)², then √N lies between a and a + 1.",
           "A number whose root is trapped strictly between two whole numbers is not a perfect square.",
           "For a perfect square, the units digit narrows the root to two choices."],
          items=[
              FIO("FiO1.q1", "Figure it Out (square numbers, question 1)",
                  "Which of the following numbers are not perfect squares? (i) 2032 (ii) 2048 (iii) 1027 (iv) 1089",
                  ["2032 ends in 2 and 2048 ends in 8, and no square ends in 2 or 8.",
                   "Also 45² = 2025 and 46² = 2116, so both are trapped strictly between two squares.",
                   "32² = 1024 and 33² = 1089, so 1027 is trapped strictly between them; it ends in 7 too.",
                   "1089 = 33², a perfect square."],
                  "(i) 2032, (ii) 2048 and (iii) 1027 are not perfect squares; 1089 = 33²")])],
    key_terms=["estimate", "square root"]))
