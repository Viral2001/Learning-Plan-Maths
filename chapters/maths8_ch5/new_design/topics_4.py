# -*- coding: utf-8 -*-
"""Topics T12 (module M3, cryptarithms) and T13 (summary and Navakankari). Book section 5.3, pp 131 to 135, with the
cryptarithm question of the last Figure it Out set."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

FIO4 = "number play"

# ============================== T12 Digits in disguise =====================================================
TOPICS.append(TOPIC(
    "T12", "M3", "Digits in Disguise", ["5.3"], "Analyze",
    "Students solve addition and multiplication cryptarithms by reasoning about units digits, carries and the size of "
    "the product, and check whether a puzzle has more than one solution.",
    "In a cryptarithm each letter stands for one digit, different letters for different digits, and a first digit is "
    "never 0. The units column, the carries and the number of digits in the answer narrow the choices.",
    [A("T12.C1", "Rules of the puzzle and addition cryptarithms", "Apply",
       "Students state the rules of a cryptarithm and solve an addition cryptarithm column by column, using the units "
       "digit and the carry.",
       textbook=["5.3 Digits in Disguise",
                 "Last year, we saw cryptarithms, puzzles where each letter stands for a digit, each digit is "
                 "represented by at most one letter, and the first digit of a number is never 0.",
                 "Solve the cryptarithms given below. (i) A1 + 1B = B0"],
       teach=["Predict first: in A1 + 1B = B0, which letter can you find first?",
              "Start with the units column: 1 + B must end in 0, so B is 9 and 1 is carried.",
              "Then the tens column: A + 1 + the carry 1 makes B, which is 9, so A is 7.",
              "Always check the finished sum and make sure different letters got different digits."],
       examples=[
           WE("Solve the cryptarithm A1 + 1B = B0.",
              ["Units column: 1 + B ends in 0, and B is a single digit, so 1 + B is 10 and B is 9, carrying 1.",
               "Tens column: A + 1 + 1 must give the tens digit B, which is 9, so A is 7.",
               "Check: 71 + 19 = 90, and A, B are different digits."],
              "A = 7 and B = 9: 71 + 19 = 90",
              ncert=["5.3.rules"])],
       key_terms=["cryptarithm", "carry", "units digit"], misconceptions=["M_CRYPT_SAME"], minutes=8),
     A("T12.C2", "Multiplication puzzles: the size of the product", "Analyze",
       "Students use the number of digits in a product to limit the possible values in a multiplication cryptarithm.",
       textbook=["Let us now try solving some cryptarithms involving multiplication. (v) PQ × 8 = RS.",
                 "Guna says, \"Oh, this means a 2-digit number multiplied by 8 should give another 2-digit number. I "
                 "know that 10 × 8 = 80. But the units digits of 10 and 80 are the same, which we don't want. For the "
                 "same reason PQ cannot be 11 as P and Q correspond to different digits. 12 × 8 = 96 fits all the "
                 "conditions\". Can PQ be 13? Think.",
                 "It is not possible because 13 × 8 = 104. For all 2-digit numbers greater than 12, the product with 8 "
                 "is a 3-digit number."],
       teach=["Predict first: which 2-digit numbers, multiplied by 8, still give a 2-digit number?",
              "13 × 8 = 104 already has three digits, so PQ can only be 10, 11 or 12.",
              "10 and 11 break the rules, since S would equal Q or P would equal Q, so PQ is 12."],
       examples=[
           WE("Solve PQ × 8 = RS.",
              ["RS has two digits, and 13 × 8 = 104 has three, so PQ is 10, 11 or 12.",
               "10 × 8 = 80 gives S = Q = 0, two letters for one digit, which is not allowed.",
               "11 has P = Q, which is not allowed either.",
               "12 × 8 = 96 uses four different digits for P, Q, R and S."],
              "PQ = 12 and RS = 96",
              ncert=["5.3.mult_pq8"])],
       key_terms=["cryptarithm", "product"], misconceptions=["M_CRYPT_SAME"], minutes=8),
     A("T12.C2x", "Units digits in GH × H = 9K", "Analyze",
       "Students match the multiplier H with the units digit of GH to pick the one solution of the cryptarithm "
       "GH × H = 9K from a list of options.",
       textbook=["(vi) Try this now: GH × H = 9K.",
                 "This means a 2-digit number multiplied by a 1-digit number gives another 2-digit number in the 90s. "
                 "Observe the letters corresponding to the units digits in this cryptarithm. Pick the solution to this "
                 "question from the options given below:",
                 "11 × 9 = 99, 12 × 8 = 96, 46 × 2 = 92, 24 × 4 = 96, 47 × 2 = 94, 31 × 3 = 93, 16 × 6 = 96."],
       teach=["Predict first: the multiplier is H. Which digit of GH must it match?",
              "The units digit of GH is also H, so the multiplier must equal the units digit.",
              "The product's units digit K must be different from G and H."],
       examples=[
           WE("Pick the solution of GH × H = 9K from 11 × 9, 12 × 8, 46 × 2, 24 × 4, 47 × 2, 31 × 3 and 16 × 6.",
              ["The multiplier must equal the units digit of GH: of the options only 24 × 4 and 16 × 6 match.",
               "In 11 × 9 the units digit is 1, not 9, and G and H would be the same digit.",
               "16 × 6 = 96 gives K = 6, the same digit as H, which is not allowed.",
               "24 × 4 = 96 gives G = 2, H = 4 and K = 6, all different."],
              "24 × 4 = 96",
              ncert=["5.3.mult_gh"])],
       key_terms=["cryptarithm", "units digit"], misconceptions=["M_CRYPT_SAME"], minutes=5, thin=True),
     A("T12.C3", "Reasoning step by step: BYE × 6 = RAY", "Analyze",
       "Students solve a three digit multiplication cryptarithm by bounding the hundreds digit, then the tens digit, "
       "and then the units digit.",
       textbook=["(vii) Here is one more: BYE × 6 = RAY.",
                 "Anshu says, \"Since the product is a 3-digit number, B can't be 2 or more. If B = 2, i.e., 2 hundreds, "
                 "the product will be more than 1200. So, B = 1.\"",
                 "What can you say about 'Y'? What digits are possible/not possible?",
                 "\"Y cannot be 7 or more because, if Y = 7, then 170 × 6 = 1020; but we want a 3-digit product. Also, "
                 "Y will be even\", Anshu explains.",
                 "We can solve cryptarithms using patterns, properties, and reasoning related to numbers and "
                 "operations."],
       teach=["Predict first: if BYE × 6 has only three digits, how big can B be?",
              "200 × 6 = 1200 has four digits, so B is 1.",
              "170 × 6 = 1020 is too big, so Y is at most 6, and Y is the units digit of 6 × E, so Y is even.",
              "Try the few cases left, checking the tens digit Y and keeping all letters different."],
       examples=[
           WE("Solve BYE × 6 = RAY.",
              ["B is 1, since 200 × 6 = 1200 is already too big.",
               "Y is the units digit of 6 × E, so Y is even, and Y is at most 6: Y is 0, 2, 4 or 6.",
               "6 × E ends in Y: Y = 0 needs E = 5; then 105 × 6 = 630, so R = 6, A = 3 and Y = 0.",
               "Y = 2 needs E = 7, and 127 × 6 = 762 repeats 7; Y = 4 needs E = 9, and 149 × 6 = 894 repeats 9; Y = 6 "
               "needs E = 1 or 6, both already used."],
              "105 × 6 = 630, so B = 1, Y = 0, E = 5, R = 6, A = 3",
              ncert=["5.3.mult_bye"])],
       key_terms=["cryptarithm", "product", "units digit"], misconceptions=["M_CRYPT_SAME"], minutes=10),
     DOER("T12.C4", "Practice: solve the digit puzzles", "digit_puzzle_solver", "Analyze",
          "Students solve addition and multiplication cryptarithms in the puzzle solver, using units digits, carries and "
          "the size of the product, and find every solution when there is more than one.",
          ["Each letter is one digit, different letters are different digits, and a first digit is never 0.",
           "Start with the most restricted letter: the units column or the size of the product."],
          items=[
              FIO("5.3.add_more", "Digits in Disguise: more addition puzzles",
                  "Solve the cryptarithms: (i) AB + 37 = 6A (ii) ON + ON + ON = PO (iii) QR + QR + QR = PRR",
                  ["(i) Without a carry the tens would make A = 3, and then B + 7 could not end in 3; so B + 7 carries "
                   "1, A is 2 and B is 5: 25 + 37 = 62.",
                   "(ii) ON × 3 has only two digits, so O is 1, 2 or 3, and 3 × N ends in O.",
                   "O = 1 needs N = 7: 17 × 3 = 51. O = 2 needs N = 4: 24 × 3 = 72. O = 3 needs N = 1: 31 × 3 = 93.",
                   "(iii) 3 × R ends in R, so R is 0 or 5; R = 0 would force Q = 0 too, so R = 5 with a carry of 1, and "
                   "3 × Q + 1 ends in 5, so Q = 8: 85 × 3 = 255."],
                  "(i) 25 + 37 = 62 (ii) three solutions: 17, 24 or 31, giving 51, 72 or 93 (iii) 85 + 85 + 85 = 255"),
              FIO("5.3.solve_six", "Digits in Disguise: solve the six",
                  "Solve the following: (i) UT × 3 = PUT (ii) AB × 5 = BC (iii) L2N × 2 = 2NP (iv) XY × 4 = ZX "
                  "(v) PP × QQ = PRP (vi) JK × 6 = KKK",
                  ["(i) 3 × T ends in T, so T is 0 or 5; T = 5 fails because 3 × U + 1 cannot end in U, and T = 0 "
                   "gives 50 × 3 = 150.",
                   "(ii) AB × 5 has two digits, so AB is at most 19, and A is 1; 19 × 5 = 95.",
                   "(iii) 2 × N ends in P and 2 × 2 plus the carry gives N, so N is 4 or 5: 124 × 2 = 248 and "
                   "125 × 2 = 250.",
                   "(iv) XY × 4 has two digits, so X is 1 or 2, and 4 × Y ends in X, so X is 2; 23 × 4 = 92.",
                   "(v) PP × QQ is P × Q × 121, and a 3-digit product needs P × Q to be at most 8.",
                   "The units digit of the product is then P × Q itself, and it must be P, so Q = 1: 22 × 11 = 242, "
                   "33 × 11 = 363, 44 × 11 = 484.",
                   "(vi) KKK divided by 6 must be a 2-digit number ending in K: 222, 444, 666 and 888 give 37, 74, 111 "
                   "and 148, and only 74 ends in 4; 74 × 6 = 444."],
                  "(i) 50 × 3 = 150 (ii) 19 × 5 = 95 (iii) 124 × 2 = 248 or 125 × 2 = 250 (iv) 23 × 4 = 92 "
                  "(v) 22 × 11 = 242, 33 × 11 = 363 or 44 × 11 = 484 (vi) 74 × 6 = 444"),
              FIO("FiO4.q15", "Figure it Out (%s, question 15)" % FIO4,
                  "Solve the cryptarithms: (i) EF × E = GGG (ii) WOW × 5 = MEOW",
                  ["(i) GGG is 111 × G, which is 3 × 37 × G, so EF × E must contain the factor 37.",
                   "EF is a 2-digit number, so EF is 37 or 74; E would be 3 or 7, and 37 × 3 = 111 works while "
                   "74 × 7 = 518 does not, so E = 3, F = 7 and G = 1.",
                   "(ii) 5 × W ends in W, so W is 5 (W cannot be 0 as a first digit).",
                   "5O5 × 5 ends in 25 when O is even and in 75 when O is odd, so O is 2 or 7; 525 × 5 = 2625 repeats "
                   "2, so O = 7: 575 × 5 = 2875, giving M = 2 and E = 8."],
                  "(i) 37 × 3 = 111 (ii) 575 × 5 = 2875")],
          misconceptions=["M_CRYPT_SAME"])],
    key_terms=["cryptarithm", "carry", "units digit"]))

# ============================== T13 Summary and Navakankari ================================================
TOPICS.append(TOPIC(
    "T13", "M3", "Summary: Number Play", ["Summary"], "Remember",
    None,
    "Properties of divisibility, the shortcuts for 3, 9 and 11 and why they work, and proving patterns with algebra, "
    "pictures, examples and counterexamples.",
    [A("T13.C1", "What we found about divisibility", "Remember",
       "Students restate the properties of divisibility, the shortcuts for 3, 9 and 11 with their reasons, and the "
       "role of algebra, pictures, examples and counterexamples in proving patterns.",
       textbook=["We explored and learnt various properties of divisibility:",
                 "If a is divisible by b, then all multiples of a are divisible by b. If a is divisible by b, then a is "
                 "divisible by all the factors of b. If a divides m and a divides n, then a divides m + n and m − n. If "
                 "a is divisible by b and is also divisible by c, then a is divisible by the LCM of b and c.",
                 "We learnt shortcuts to check divisibility by 3, 9 and 11, and why they work.",
                 "Through all this we were exposed to the power of mathematical thinking and reasoning, using algebra, "
                 "visualisation, examples and counterexamples."],
       teach=["Our opening question is settled: signs between four numbers always give results of one parity, because "
              "switching a sign changes the result by twice a number.",
              "Divisibility passes to multiples, to factors, to sums and differences, and to the LCM of two divisors, "
              "but not always to their product.",
              "Place values leave remainder 1 on division by 9 and 3, and alternately one more and one less on "
              "division by 11. Still open for you: find a shortcut of your own for 99."],
       ncert=["summary"], video_focus=["RECAP"], minutes=8),
     A("T13.C2", "Navakankari", "Apply",
       "Students play the traditional board game Navakankari, forming lines of three pawns, and reflect on the "
       "strategy they used.",
       textbook=["Navakankari, also known as Sālu Mane Āṭa, Chār-Pār, or Navkakrī, is a traditional Indian board game "
                 "that is the same as 'Nine Men's Morris' or 'Mills' in the West. It is a strategy game for two "
                 "players where the goal is to form lines of three pawns to eliminate the opponent's pawns or block "
                 "their movement.",
                 "Gameplay. 1. Each player starts with 9 pawns. The players take turns in placing their pawns on the "
                 "marked intersections. An intersection can have at most one pawn. 2. Once all the pawns are placed, "
                 "the players take turns to move one of their pawns to adjacent empty intersections to form lines of "
                 "three. The line can be horizontal or vertical. 3. Once a player makes a line with their pawns they "
                 "can remove any one of the opponent's pawns as long as it is not a part of one of their lines.",
                 "A player wins if the opponent has less than 3 pawns or is unable to make a move."],
       teach=["Predict first: is it better to place your pawns at the corners or at the middle points of the sides?",
              "Each line of three lets you remove one of your partner's pawns that is not in a line.",
              "Play with a partner on paper and talk about the moves that helped."],
       examples=[
           WE("Your partner has two pawns in a line with the third point empty, and it is your turn to place a pawn. "
              "What should you do, and why?",
              ["If you leave the empty point, your partner completes a line of three next turn.",
               "A completed line lets your partner remove one of your pawns.",
               "Placing your pawn on the empty point blocks the line."],
              "Place your pawn on the empty point to block the line of three")],
       ncert=["navakankari"], key_terms=["Navakankari", "strategy"], enrichment=True, minutes=5)],
    topic_type="summary"))
