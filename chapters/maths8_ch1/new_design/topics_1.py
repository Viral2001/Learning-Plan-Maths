# -*- coding: utf-8 -*-
"""Topics T1 to T5: the locker puzzle (M1), squares as areas and digits, squares from odd numbers, and counting
between squares (M2). Book pp 1 to 7 and 10 to 11."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 The queen's locker puzzle ================================================
TOPICS.append(TOPIC(
    "T1", "M1", "The Queen's Locker Puzzle", ["Chapter opening"], "Understand",
    "",
    "A hundred lockers, a hundred people opening and closing them, and the question that drives the chapter: which "
    "lockers stay open at the end?",
    [A("T1.C1", "A hundred lockers and a hidden treasure", "Understand",
       "",
       textbook=["Queen Ratnamanjuri of Khoisnam left a will. Her treasure was kept in one of the 100 lockers in her "
                 "palace, all closed and locked.",
                 "100 people were called one after another. The first person opened every locker. The second person "
                 "closed every second locker: locker 2, 4, 6, and so on. The third person toggled every third "
                 "locker: if it was open it was closed, and if it was closed it was opened. The fourth person toggled "
                 "every fourth locker, and so on, until the hundredth person toggled locker 100.",
                 "After all 100 people had done this, which lockers remain open?",
                 "Hint: Find the number of times each locker is toggled."],
       teach=["Predict first: after all 100 people have passed, do you think most lockers end open, most end closed, "
              "or only a few end open?",
              "Try a small case by hand: 10 lockers and 10 people. Keep a record of which lockers each person touches.",
              "A locker that is touched an odd number of times ends open; an even number of times, closed.",
              "So the real question is: how many times is each locker touched? Keep that question open for the next topic."],
       ncert=["opening"], key_terms=["toggle", "locker"], video_focus=["HOOK"], minutes=4, enrichment=True)],
    topic_type="framing"))

# ============================== T2 Which lockers stay open? =================================================
TOPICS.append(TOPIC(
    "T2", "M1", "Which Lockers Stay Open?", ["Chapter opening"], "Analyze",
    "Students connect each toggle of a locker to a factor of its number, explain why factors usually pair up, show "
    "that only square numbers have an odd number of factors, and use this to name the open lockers and the five "
    "lockers touched exactly twice.",
    "A locker is toggled once for each of its factors. Factors pair up, except when a number is a factor times itself, "
    "so only square numbers have an odd number of factors, and lockers 1, 4, 9, up to 100 stay open.",
    [A("T2.C1", "Each toggle is a factor", "Understand",
       "Students list the people who toggle a given locker, recognise them as the factors of the locker number, and "
       "pair each factor with its partner factor.",
       textbook=["Locker 6 is toggled by person 1, person 2, person 3 and person 6. These are exactly the factors of 6.",
                 "Each factor of 6 has a partner factor: 1 × 6 and 2 × 3.",
                 "Does every number have an even number of factors?",
                 "Write the factors of 1, 4 and 9 in the boxes."],
       teach=["Predict first: who toggles locker 12? Write the list before you check.",
              "Person k toggles locker 12 exactly when k divides 12, so the toggles are 1, 2, 3, 4, 6, 12: the factors.",
              "Factors come in partner pairs: 1 × 12, 2 × 6, 3 × 4. Six factors, six toggles: closed.",
              "Now look at 1, 4 and 9. Does every factor still have a different partner?"],
       examples=[
           WE("How many times is locker 12 toggled, and does it end open or closed?",
              ["Locker 12 is toggled by every person whose number divides 12.",
               "The factors of 12 pair up: 12 = 1 × 12 = 2 × 6 = 3 × 4.",
               "That is 6 factors, so locker 12 is toggled 6 times.",
               "An even number of toggles brings it back to closed."],
              "6 times, so locker 12 ends closed", ncert=["1.0.factors", "1.0.even_factors"])],
       key_terms=["factor", "partner factor"], misconceptions=["M_FACTORS_EVEN"], minutes=8),
     A("T2.C2", "Squares have an odd number of factors", "Analyze",
       "Students find the numbers whose factors do not all pair with a different partner, explain that a factor "
       "multiplied by itself has no separate partner, and name such numbers square numbers.",
       textbook=["Can you use this insight to find more numbers with an odd number of factors?",
                 "For 36: 1 × 36, 2 × 18, 3 × 12, 4 × 9 and 6 × 6. The factor 6 is paired with itself.",
                 "Numbers like 1 × 1, 2 × 2, 3 × 3, 4 × 4 are called square numbers.",
                 "Square numbers have an odd number of factors."],
       teach=["Predict first: does 36 have an odd or an even number of factors?",
              "List the pairs: 1 × 36, 2 × 18, 3 × 12, 4 × 9, 6 × 6. The last pair uses 6 twice.",
              "So 36 has 9 factors, an odd number. This happens only when a number is some number times itself.",
              "Such numbers, 1, 4, 9, 16, 25 and so on, are square numbers."],
       examples=[
           WE("Count the factors of 36 and say why the count is odd.",
              ["Write the factor pairs: 36 = 1 × 36 = 2 × 18 = 3 × 12 = 4 × 9 = 6 × 6.",
               "The factors are 1, 2, 3, 4, 6, 9, 12, 18 and 36.",
               "That is 9 factors, because 6 pairs with itself and is counted once."],
              "36 has 9 factors; the odd count comes from 6 × 6",
              ncert=["1.0.odd_insight", "1.0.square_def"])],
       key_terms=["square number", "factor pair"], misconceptions=["M_FACTORS_EVEN"], minutes=8),
     A("T2.C3", "The open lockers are the squares", "Apply",
       "Students list the lockers that stay open after all 100 people pass as the square numbers up to 100.",
       textbook=["Write the locker numbers that remain open."],
       teach=["Predict first: which lockers between 1 and 30 stay open?",
              "Open lockers are those toggled an odd number of times, so they are the square numbers.",
              "Up to 100: 1, 4, 9, 16, 25, 36, 49, 64, 81 and 100, ten open lockers."],
       examples=[
           WE("Which lockers remain open after all 100 people pass?",
              ["A locker ends open when it is toggled an odd number of times.",
               "Open lockers have an odd number of factors, so they are the square numbers.",
               "The squares up to 100 are 1, 4, 9, 16, 25, 36, 49, 64, 81 and 100."],
              "Lockers 1, 4, 9, 16, 25, 36, 49, 64, 81 and 100 stay open",
              ncert=["1.0.open_lockers"])],
       key_terms=["square number", "odd number of factors"], misconceptions=["M_FACTORS_EVEN"], minutes=8),
     DOER("T2.C4", "Practice: solve the locker puzzle", "locker_toggle", "Apply",
          "Students decide for any locker number how many times it is toggled by counting its factors, and find "
          "the lockers touched exactly twice as the prime numbers.",
          ["Each person who touches a locker is a factor of its number.",
           "Factors pair up, except a number times itself, so only square numbers have an odd number of factors.",
           "A locker touched exactly twice has exactly two factors, so its number is prime."],
          textbook=["The queen's will also had a clue: the first five lockers that were touched exactly twice hold the "
                    "code. Which are these five lockers?",
                    "A locker touched exactly twice has exactly two factors, 1 and itself. So these are the prime "
                    "numbers 2, 3, 5, 7 and 11."],
          items=[FIO("1.0.five_lockers", "The locker puzzle (the secret code)",
                     "The first five lockers that were touched exactly twice hold the code to the treasure. Which are "
                     "these five lockers?",
                     ["Each person who touches a locker is a factor of its number.",
                      "Touched exactly twice means exactly two factors: 1 and the number itself.",
                      "A number with exactly two factors is a prime number. 1 has one factor and 4 has three.",
                      "The first five primes are 2, 3, 5, 7 and 11."],
                     "Lockers 2, 3, 5, 7 and 11")])],
    key_terms=["factor", "square number", "prime number"]))

# ============================== T3 Squares as areas and their digits ========================================
TOPICS.append(TOPIC(
    "T3", "M2", "Squares as Areas, Digits and Zeros", ["1.1"], "Analyze",
    "Students read a square number as the area of a square, write squares with the n squared notation including "
    "fractions and decimals, find the digits a square can end in, and predict the zeros and the parity of a square.",
    "A square number is the area of a square with a whole number side. Squares end only in 0, 1, 4, 5, 6 or 9, a "
    "square has twice as many end zeros as the number, and a number and its square have the same parity.",
    [A("T3.C1", "A square number is an area", "Understand",
       "Students find the area of squares of given sides, write the result with the n squared notation, and extend "
       "squaring to fractions and decimals.",
       textbook=["1.1 Square Numbers",
                 "The area of a square of side 1 unit is 1 sq unit, of side 2 units is 4 sq units, of side 3 units is "
                 "9 sq units. For sides 4, 5 and 10 the areas are 16, 25 and 100 sq units.",
                 "A square of side n units has area n × n = n² sq units, read as n squared.",
                 "We can square fractions and decimals too: (3/5)² = 9/25 and 2.5² = 6.25.",
                 "Numbers like 1, 4, 9, 16, 25 which are squares of natural numbers are called perfect squares."],
       teach=["Predict first: a square has side 6 units. Is its area 12 square units or 36 square units?",
              "Area is side times side: 6 × 6 = 36, written 6², read 6 squared. Squaring is not doubling.",
              "Fractions and decimals square the same way: (3/5)² = 9/25 and 2.5² = 6.25.",
              "Squares of natural numbers, 1, 4, 9, 16, 25, are called perfect squares."],
       examples=[
           WE("Find the areas of squares with sides 6 units, 3/5 unit and 2.5 units.",
              ["Side 6: 6² = 6 × 6 = 36 square units.",
               "Side 3/5: (3/5)² = 9/25 square unit.",
               "Side 2.5: 2.5² = 2.5 × 2.5 = 6.25 square units.",
               "Only 36 is a perfect square, because only 6 is a natural number."],
              "36, 9/25 and 6.25 square units", ncert=["1.1.area_table", "1.1.notation", "1.1.perfect_def"])],
       key_terms=["square number", "perfect square", "n squared"], misconceptions=["M_SQUARE_DOUBLE"], minutes=8),
     A("T3.C2", "The last digit of a square", "Analyze",
       "Students show from the table that squares end only in 0, 1, 4, 5, 6 or 9, that such an ending does not "
       "guarantee a square, and predict the last digit of a square.",
       textbook=["Fill in the table of squares from 1 to 30.",
                 "What patterns do you notice? The squares end only in 0, 1, 4, 5, 6 or 9.",
                 "If a number ends in 0, 1, 4, 5, 6 or 9, is it always a square? No: 26 ends in 6 but is not a square.",
                 "Write 5 numbers such that by looking at their units digit it can be said that they are not squares.",
                 "1², 9², 11², 19², 21², 29² all end in 1. Write the next two squares ending in 1.",
                 "If a number has 1 or 9 in the units place, its square ends in 1.",
                 "The squares 16, 36, 196, 256, 576 and 676 end in 6. Which of 38², 34², 46², 56², 74², 82² have 6 "
                 "in the units place?",
                 "Find more such patterns by observing the numbers and their squares in the table."],
       teach=["Predict first: can a perfect square end in 7?",
              "Only the last digit of a number decides the last digit of its square. Squaring 0 to 9 gives last "
              "digits 0, 1, 4, 9, 6, 5, 6, 9, 4, 1.",
              "So squares end only in 0, 1, 4, 5, 6 or 9. A number ending in 2, 3, 7 or 8 is never a square.",
              "The converse fails: 26 ends in 6 but is not a square. A last digit can rule a square out, never in.",
              "A number ending in 4 or 6 has a square ending in 6; ending in 1 or 9, a square ending in 1."],
       examples=[
           WE("Which of 38², 34², 46², 56², 74² and 82² end in 6?",
              ["Only the last digit matters: 38 and 82 end in 8 or 2, and 8² = 64 and 2² = 4 end in 4.",
               "34 and 74 end in 4, and 4² = 16 ends in 6.",
               "46 and 56 end in 6, and 6² = 36 ends in 6.",
               "Check one: 34² = 1156, which ends in 6."],
              "34², 46², 56² and 74² end in 6; 38² and 82² end in 4",
              ncert=["1.1.which6", "1.1.ends6", "1.1.table30", "1.1.mt_patterns"])],
       key_terms=["units digit", "perfect square"], misconceptions=["M_DIGIT_ENOUGH"], minutes=10),
     A("T3.C2x", "Squares that end in 1, and numbers that cannot be squares", "Apply",
       "Students list squares ending in 1 from numbers ending in 1 or 9 and write numbers ruled out as squares by "
       "their units digit alone.",
       teach=["Predict first: what are the next two squares ending in 1 after 29²?",
              "Numbers ending in 1 or 9 have squares ending in 1, so the next are 31² and 39².",
              "Numbers ending in 2, 3, 7 or 8 can never be squares."],
       examples=[
           WE("Write the next two squares ending in 1 after 29², and five numbers that cannot be squares.",
              ["Squares end in 1 when the number ends in 1 or 9.",
               "After 29 the next such numbers are 31 and 39: 31² = 961 and 39² = 1521.",
               "Numbers ending in 2, 3, 7 or 8 are never squares, for example 52, 73, 107, 218 and 1003."],
              "961 and 1521; for example 52, 73, 107, 218 and 1003 are not squares",
              ncert=["1.1.ends1", "1.1.five_nonsquares", "1.1.mt_always", "1.1.more_patterns"])],
       key_terms=["units digit"], misconceptions=["M_DIGIT_ENOUGH"], minutes=6, thin=True),
     A("T3.C3", "Zeros at the end and odd or even", "Analyze",
       "Students predict how many zeros end the square of a number ending in zeros, explain why a square always ends "
       "in an even number of zeros, and show that a number and its square are both odd or both even.",
       textbook=["10² = 100, 20² = 400, 100² = 10000.",
                 "If a number ends in 3 zeros, how many zeros will its square have at the end?",
                 "Notice the number of zeros at the end of a number and its square. Is this pattern always true? Can "
                 "we say that squares can only have an even number of zeros at the end?",
                 "What can we say about the parity of a number and its square?"],
       teach=["Predict first: 3000 ends in 3 zeros. How many zeros end 3000²?",
              "3000² = 3000 × 3000. Each factor brings 3 zeros, so the square ends in 6 zeros: 9000000.",
              "The zeros double, so a perfect square always ends in an even number of zeros.",
              "Odd times odd is odd and even times even is even, so a number and its square have the same parity."],
       examples=[
           WE("How many zeros end 3000², and is 3000² odd or even?",
              ["3000² = 3000 × 3000 = 9000000.",
               "3 zeros from each factor give 3 + 3 = 6 zeros at the end.",
               "3000 is even, and even × even is even, so 3000² is even."],
              "6 zeros, and 3000² is even", ncert=["1.1.zeros", "1.1.parity"])],
       key_terms=["parity", "zeros"], misconceptions=["M_ZEROS_SAME"], minutes=8),
     DOER("T3.C4", "Practice: build squares and read their digits", "square_builder", "Analyze",
          "Students build squares of tiles of growing side, read the area as the square, and use the last digit, "
          "the end zeros and the parity to decide quickly whether a number can be a square.",
          ["A square of side n holds n² unit tiles; squaring is not doubling.",
           "Squares end only in 0, 1, 4, 5, 6 or 9, and that ending alone never proves a number is a square.",
           "A square ends in an even number of zeros and has the same parity as the number."],
          items=[
              FIO("FiO1.q2", "Figure it Out (square numbers, question 2)",
                  "Which of the following numbers have the digit 4 in the units place? (i) 64² (ii) 108² (iii) 292² "
                  "(iv) 36²",
                  ["Only the last digit of each number matters.",
                   "64 and 36 end in 4 and 6, and 4² = 16 and 6² = 36 both end in 6.",
                   "108 and 292 end in 8 and 2, and 8² = 64 and 2² = 4 both end in 4.",
                   "So 108² and 292² end in 4."],
                  "(ii) 108² and (iii) 292²")])],
    key_terms=["square number", "units digit", "parity"]))

# ============================== T4 Squares from odd numbers =================================================
TOPICS.append(TOPIC(
    "T4", "M2", "Squares from Odd Numbers", ["1.1"], "Analyze",
    "Students show that consecutive squares differ by consecutive odd numbers and that the first n odd numbers add "
    "to n squared, test a number for being a square by subtracting odd numbers, and find the next square from the "
    "nth odd number.",
    "The first n odd numbers add up to n², seen as inverted L shapes around a square. Subtracting 1, 3, 5 and so on "
    "reaches 0 exactly for a square, and (n + 1)² is n² plus the (n + 1)th odd number.",
    [A("T4.C1", "Odd numbers build squares", "Understand",
       "Students find the differences between consecutive squares, recognise them as the odd numbers, and explain "
       "with the inverted L picture why the first n odd numbers add to n squared.",
       textbook=["Perfect Squares and Odd Numbers",
                 "Look at the differences between consecutive squares: 4 − 1 = 3, 9 − 4 = 5, 16 − 9 = 7, 25 − 16 = 9. "
                 "See if this pattern continues.",
                 "1 + 3 + 5 + 7 + 9 + 11 = 36.",
                 "Each square is the previous square with an inverted L shape added to it. The inverted L shapes have "
                 "1, 3, 5, 7, ... dots. So the sum of the first n odd numbers is n².",
                 "Such pictures are visual proofs."],
       teach=["Predict first: what is 1 + 3 + 5 + 7 + 9 + 11? Guess before you add.",
              "Draw a 1 by 1 square of dots, then wrap an inverted L of 3 dots to make 2 by 2, then 5 dots to make 3 by 3.",
              "Each new L is the next odd number, so 6 odd numbers make a 6 by 6 square: 36.",
              "The sum of the first n odd numbers is n², and consecutive squares differ by consecutive odd numbers."],
       examples=[
           WE("Find 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 without adding term by term.",
              ["These are the first 8 odd numbers.",
               "The first n odd numbers add up to n².",
               "So the sum is 8² = 64.",
               "Check: 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 = 64."],
              "64", ncert=["1.1.odd_diffs", "1.1.odd_sum"])],
       key_terms=["odd number", "visual proof"], misconceptions=["M_SQUARE_DOUBLE"], minutes=8),
     A("T4.C2", "Subtract odd numbers to test a square", "Apply",
       "Students subtract 1, 3, 5 and so on from a number in turn and decide it is a perfect square exactly when the "
       "subtractions reach 0, counting the steps to find the root.",
       textbook=["Is 25 a perfect square? 25 − 1 = 24, 24 − 3 = 21, 21 − 5 = 16, 16 − 7 = 9, 9 − 9 = 0. "
                 "We reached 0 after subtracting 5 odd numbers, so 25 = 5².",
                 "Is 38 a perfect square? 38 − 1 = 37, 37 − 3 = 34, 34 − 5 = 29, 29 − 7 = 22, 22 − 9 = 13, "
                 "13 − 11 = 2, and 2 − 13 is less than 0. So 38 is not a perfect square."],
       teach=["Predict first: is 38 a perfect square?",
              "Subtract the odd numbers in order. If you land exactly on 0, the number is the sum of the first few odd "
              "numbers, so it is a square.",
              "For 38 we reach 2 and the next odd number, 13, is too big: 38 is not a square.",
              "The number of odd numbers subtracted is the square root."],
       examples=[
           WE("Use successive subtraction of odd numbers to decide whether 38 is a perfect square.",
              ["38 − 1 = 37, 37 − 3 = 34, 34 − 5 = 29.",
               "29 − 7 = 22, 22 − 9 = 13, 13 − 11 = 2.",
               "The next odd number is 13 and 2 − 13 = −11, below 0.",
               "We never land on 0, so 38 is not a perfect square."],
              "38 is not a perfect square", ncert=["1.1.subtract_test"])],
       key_terms=["successive subtraction", "perfect square"], misconceptions=["M_DIGIT_ENOUGH"], minutes=8),
     A("T4.C3", "From one square to the next", "Apply",
       "Students find the nth odd number as 2n − 1 and use it to get the next square from a given square.",
       textbook=["Using the pattern, find 36² given that 35² = 1225.",
                 "How do we find the 36th odd number? What is the nth odd number?",
                 "The nth odd number is 2n − 1. The 36th odd number is 71. So 36² = 1225 + 71 = 1296."],
       teach=["Predict first: if 35² = 1225, is 36² closer to 1260 or to 1300?",
              "36² is 35² plus the 36th odd number, because the first 36 odd numbers add to 36².",
              "The odd numbers are 1, 3, 5, ..., and the nth one is 2n − 1, so the 36th is 2 × 36 − 1 = 71.",
              "36² = 1225 + 71 = 1296."],
       examples=[
           WE("Given 35² = 1225, find 36² without multiplying.",
              ["36² is the sum of the first 36 odd numbers, which is 35² plus the 36th odd number.",
               "The nth odd number is 2n − 1, so the 36th is 2 × 36 − 1 = 71.",
               "36² = 1225 + 71 = 1296.",
               "Check: 36 × 36 = 1296."],
              "36² = 1296", ncert=["1.1.next_square", "1.1.nth_odd"])],
       key_terms=["nth odd number", "consecutive squares"], misconceptions=["M_SQUARE_DOUBLE"], minutes=8),
     DOER("T4.C4", "Practice: squares from odd numbers", "odd_corner_builder", "Apply",
          "Students use the odd number pattern to get squares from neighbouring squares and to check number "
          "patterns built from squares.",
          ["The first n odd numbers add to n².",
           "Subtracting 1, 3, 5, ... reaches exactly 0 only for a perfect square.",
           "(n + 1)² is n² plus the (n + 1)th odd number, which is 2n + 1."],
          items=[
              FIO("FiO1.q3", "Figure it Out (square numbers, question 3)",
                  "Given that 125² = 15625, what is the value of 126²? (i) 15625 + 126 (ii) 15625 + 26² "
                  "(iii) 15625 + 253 (iv) 15625 + 251 (v) 15625 + 512",
                  ["126² is 125² plus the 126th odd number.",
                   "The 126th odd number is 2 × 126 − 1 = 251.",
                   "So 126² = 15625 + 251 = 15876.",
                   "Check: 126 × 126 = 15876."],
                  "(iv) 15625 + 251, which is 15876"),
              FIO("FiO1.q8", "Figure it Out (square numbers, question 8)",
                  "Look at the pattern 1² + 2² + 2² = 3², 2² + 3² + 6² = 7², 3² + 4² + 12² = 13². Fill in "
                  "4² + 5² + 20² = (___)² and 9² + 10² + (___)² = (___)².",
                  ["In each line the third number is the product of the first two: 1 × 2 = 2, 2 × 3 = 6, 3 × 4 = 12.",
                   "The number on the right is one more than that product: 3, 7, 13.",
                   "4 × 5 = 20, so 4² + 5² + 20² = 21². Check: 16 + 25 + 400 = 441 = 21².",
                   "9 × 10 = 90, so 9² + 10² + 90² = 91². Check: 81 + 100 + 8100 = 8281 = 91²."],
                  "4² + 5² + 20² = 21² and 9² + 10² + 90² = 91²")])],
    key_terms=["odd number", "successive subtraction"]))

# ============================== T5 Counting between squares =================================================
TOPICS.append(TOPIC(
    "T5", "M2", "Gaps Between Squares and Triangular Numbers", ["1.1"], "Analyze",
    "Students count the numbers lying between consecutive squares, count the squares in each block of 100 up to "
    "1000, and show that two consecutive triangular numbers add to a square.",
    "There are 2n numbers between n² and (n + 1)², so squares thin out as numbers grow: 10 squares up to 100 but "
    "only 1 between 901 and 1000. Two consecutive triangular numbers always add to a square.",
    [A("T5.C1", "How many numbers lie between two squares", "Analyze",
       "Students count the numbers strictly between consecutive squares, find that there are 2n between n squared "
       "and the next square, and explain the count with the odd number gap.",
       textbook=["Find how many numbers lie between two consecutive perfect squares. Do you notice a pattern?",
                 "Between 1 and 4 lie 2 numbers, between 4 and 9 lie 4 numbers, between 9 and 16 lie 6 numbers."],
       teach=["Predict first: how many whole numbers lie strictly between 25 and 36?",
              "The gap from n² to (n + 1)² is the odd number 2n + 1, and the numbers strictly between are one fewer.",
              "So there are 2n numbers between n² and (n + 1)²: 10 between 25 and 36.",
              "In general, the count between p and q is q − p − 1."],
       examples=[
           WE("How many whole numbers lie strictly between 25 and 36?",
              ["25 = 5² and 36 = 6² are consecutive squares.",
               "The numbers between them are 26 to 35.",
               "That is 36 − 25 − 1 = 10 numbers, which is 2 × 5."],
              "10 numbers", ncert=["1.1.between"])],
       key_terms=["consecutive squares"], misconceptions=["M_BETWEEN_N"], minutes=8),
     A("T5.C2", "Squares thin out in each hundred", "Analyze",
       "Students count the perfect squares in each block of 100 numbers up to 1000, explain why the count drops, and "
       "find the largest square below 1000.",
       textbook=["How many square numbers are there between 1 and 100? How many are there between 101 and 200? "
                 "Write your answers in the table: 1 to 100, 101 to 200, and so on up to 901 to 1000.",
                 "What is the largest square less than 1000?"],
       teach=["Predict first: are there more squares between 1 and 100 or between 901 and 1000?",
              "List them: 1 to 100 has 10 squares, 101 to 200 has 4 (121, 144, 169, 196), 201 to 300 has 3.",
              "301 to 400 has 3, then each block from 401 to 900 has 2, and 901 to 1000 has only 961.",
              "The gaps 2n + 1 keep growing, so squares get rarer. The largest square below 1000 is 31² = 961, "
              "because 32² = 1024."],
       examples=[
           WE("How many perfect squares lie between 101 and 200, and what is the largest square less than 1000?",
              ["10² = 100 is just below 101 and 15² = 225 is above 200.",
               "So the squares are 11² = 121, 12² = 144, 13² = 169 and 14² = 196: 4 squares.",
               "31² = 961 and 32² = 1024, so 961 is the largest square below 1000."],
              "4 squares; the largest square below 1000 is 961", ncert=["1.1.blocks"])],
       key_terms=["perfect square"], misconceptions=["M_BETWEEN_N"], minutes=8),
     A("T5.C3", "Two triangular numbers make a square", "Analyze",
       "Students list the triangular numbers, add consecutive pairs, and explain with a dot picture why each sum is "
       "a perfect square.",
       textbook=["Perfect Squares and Triangular Numbers",
                 "Triangular numbers: 1, 3, 6, 10, 15, ...",
                 "Do you see any relation between triangular numbers and square numbers? Extend the pattern shown and "
                 "draw the next figure.",
                 "1 + 3 = 4, 3 + 6 = 9, 6 + 10 = 16."],
       teach=["Predict first: what do 6 and 10 add to? Is it special?",
              "Triangular numbers are dots stacked in rows of 1, 2, 3, ...: 1, 3, 6, 10, 15.",
              "Fit two consecutive triangles together, one turned over, and they fill a square.",
              "1 + 3 = 4, 3 + 6 = 9, 6 + 10 = 16, and the next is 10 + 15 = 25."],
       examples=[
           WE("Add the next pair of consecutive triangular numbers after 6 and 10, and check that the sum is a square.",
              ["The triangular numbers are 1, 3, 6, 10, 15, made by adding 1, 2, 3, 4, 5.",
               "The pair after 6 and 10 is 10 and 15.",
               "10 + 15 = 25 = 5²."],
              "10 + 15 = 25, which is 5²", ncert=["1.1.triangular"])],
       key_terms=["triangular number"], minutes=6),
     DOER("T5.C4", "Practice: count between squares", "square_gap_counter", "Analyze",
          "Students count the numbers between consecutive squares for large squares using 2n instead of listing.",
          ["Between n² and (n + 1)² lie exactly 2n numbers.",
           "Squares get rarer as numbers grow.",
           "Two consecutive triangular numbers add up to a square."],
          items=[
              FIO("FiO1.q7", "Figure it Out (square numbers, question 7)",
                  "How many numbers lie between the squares of the following numbers? (i) 16 and 17 (ii) 99 and 100",
                  ["Between n² and (n + 1)² lie 2n numbers.",
                   "(i) n = 16: 2 × 16 = 32. Check: 289 − 256 − 1 = 32.",
                   "(ii) n = 99: 2 × 99 = 198. Check: 10000 − 9801 − 1 = 198."],
                  "(i) 32 (ii) 198")])],
    key_terms=["consecutive squares", "triangular number"]))
