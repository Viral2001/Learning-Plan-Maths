# -*- coding: utf-8 -*-
"""Topics T8 to T10: many ways to see (M4), mending mistakes and choosing identities, one pattern described in
several ways, and the summary with Coin Conjoin (M5). Book pp 150 to 158."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T8 Mind the mistake, mend the mistake =======================================
TOPICS.append(TOPIC(
    "T8", "M4", "Mind the Mistake, Mend the Mistake", ["6.3"], "Evaluate",
    "Students check simplifications of algebraic expressions for mistakes, explain what went wrong in each wrong "
    "simplification, write the correct expression, and choose a suitable identity or the distributive property "
    "to find products.",
    "Most mistakes come from multiplying only part of a bracket, slipping a sign, forgetting the 2ab of a square, "
    "multiplying a factor into both parts of a product, or adding unlike terms. Checking each step against the "
    "distributive property finds and mends them.",
    [A("T8.C1", "Finding and mending mistakes", "Evaluate",
       "Students check six simplifications, explain each mistake such as a forgotten term, a sign slip or a missing "
       "2ab, and write the correct simplified expression.",
       textbook=["We have expanded and simplified some algebraic expressions below to their simplest forms.",
                 "(i) Check each of the simplifications and see if there is a mistake.",
                 "(ii) If there is a mistake, try to explain what could have gone wrong.",
                 "(iii) Then write the correct expression.",
                 "−3p (−5p + 2q) = −3p + 5p − 2q = p − 2q",
                 "2(x − 1) + 3 (x + 4) = 2x − 1 + 3x + 4 = 5x + 3",
                 "y + 2 (y + 2) = (y + 2)² = y² + 4y + 4",
                 "(5m + 6n)² = 25m² + 36n²",
                 "(−q + 2)² = q² − 4q + 4",
                 "3a (2b × 3c) = 6ab × 9ac = 54a²bc"],
       teach=["Predict first: −3p(−5p + 2q) was simplified to p − 2q. Is that right?",
              "Check every step against the distributive property: each term inside the bracket must be multiplied.",
              "Common slips: a term left unmultiplied, a sign lost, the 2ab of a square forgotten, or a factor "
              "multiplied into both parts of a product.",
              "Mend each one and check by putting in a number."],
       examples=[
           WE("Check each simplification, explain any mistake and write the correct expression: (a) −3p(−5p + 2q) "
              "= p − 2q; (b) 2(x − 1) + 3(x + 4) = 5x + 3; (c) y + 2(y + 2) = y² + 4y + 4; (d) (5m + 6n)² = 25m² + "
              "36n²; (e) (−q + 2)² = q² − 4q + 4; (f) 3a(2b × 3c) = 54a²bc.",
              ["(a) −3p must multiply both terms: (−3p)(−5p) + (−3p)(2q) = 15p² − 6pq.",
               "(b) 2 and 3 must multiply the second terms too: 2x − 2 + 3x + 12 = 5x + 10.",
               "(c) y + 2(y + 2) is a sum, not a square: y + 2y + 4 = 3y + 4.",
               "(d) The 2ab term is missing: 25m² + 2 × 5m × 6n + 36n² = 25m² + 60mn + 36n².",
               "(e) Correct: (2 − q)² = 4 − 4q + q².",
               "(f) 2b × 3c is one product, 6bc, so 3a × 6bc = 18abc."],
              "(a) 15p² − 6pq (b) 5x + 10 (c) 3y + 4 (d) 25m² + 60mn + 36n² (e) correct (f) 18abc",
              ncert=["6.3.cards_a"])],
       key_terms=["mistake", "simplification", "expression"],
       misconceptions=["M_DISTRIBUTE_FIRST_ONLY", "M_SIGN_DISTRIBUTE", "M_SUM_SQUARE", "M_MULTIPLY_EACH_FACTOR"],
       minutes=9),
     A("T8.C1x", "More mistakes to mend", "Evaluate",
       "Students check six more simplifications, spot unlike terms added together and missing products, and write "
       "the correct expression for each mistake.",
       textbook=["1/2 (10s − 6) + 3 = 5s − 3 + 3 = 5s",
                 "5w² + 6w = 11w²",
                 "2a³ + 3a³ + 6a²b + 6ab² = 5a³ + 12a²b²",
                 "(a + 2) (b + 4) = ab + 8",
                 "ab² + a²b + a²b² = ab (a + b + ab)",
                 "(x + 2)(x + 5) = (x + 2)x + (x + 2)5 = x² + 2x + 5x + 10 = x² + 7x + 10"],
       teach=["Predict first: can 5w² + 6w be written as 11w²?",
              "Only like terms combine: w² and w are different kinds.",
              "A product of two sums has four parts before like terms are collected."],
       examples=[
           WE("Check each simplification and mend it if needed: (a) 1/2(10s − 6) + 3 = 5s; (b) 5w² + 6w = 11w²; "
              "(c) 2a³ + 3a³ + 6a²b + 6ab² = 5a³ + 12a²b²; (d) (a + 2)(b + 4) = ab + 8; (e) ab² + a²b + a²b² = "
              "ab(a + b + ab); (f) (x + 2)(x + 5) = x² + 7x + 10.",
              ["(a) Correct: 5s − 3 + 3 = 5s.",
               "(b) w² and w are unlike terms, so 5w² + 6w cannot be simplified.",
               "(c) Only 2a³ + 3a³ = 5a³ combine; 6a²b and 6ab² are unlike: 5a³ + 6a²b + 6ab².",
               "(d) Four parts are needed: ab + 4a + 2b + 8.",
               "(e) Correct: ab × a = a²b, ab × b = ab², ab × ab = a²b².",
               "(f) Correct: x² + 2x + 5x + 10 = x² + 7x + 10."],
              "(a) correct (b) cannot be simplified (c) 5a³ + 6a²b + 6ab² (d) ab + 4a + 2b + 8 (e) correct "
              "(f) correct",
              ncert=["6.3.cards_b"])],
       key_terms=["mistake", "like terms"], misconceptions=["M_UNLIKE_ADD", "M_TWO_TERMS_ONLY"], minutes=6,
       thin=True),
     DOER("T8.C2", "Practice: choose the identity", "identity_match_sort", "Apply",
          "Students decide which identity fits each product, a square of a sum, a square of a difference or a sum "
          "times a difference, and use it to compute 46², 397 × 403, 91² and 43 × 45.",
          ["(a + b)² = a² + 2ab + b² and (a − b)² = a² − 2ab + b².",
           "(a + b)(a − b) = a² − b².",
           "When no identity fits, the distributive property always works."],
          items=[
              FIO("FiO3.q1", "Figure it Out (identities and patterns, question 1)",
                  "Compute these products using the suggested identity. (i) 46² using the square of a sum (ii) "
                  "397 × 403 using the difference of squares (iii) 91² using the square of a difference (iv) "
                  "43 × 45 using the difference of squares",
                  ["(i) 46² = (40 + 6)² = 1600 + 480 + 36 = 2116.",
                   "(ii) 397 × 403 = (400 − 3)(400 + 3) = 160000 − 9 = 159991.",
                   "(iii) 91² = (100 − 9)² = 10000 − 1800 + 81 = 8281.",
                   "(iv) 43 × 45 = (44 − 1)(44 + 1) = 1936 − 1 = 1935."],
                  "(i) 2116 (ii) 159991 (iii) 8281 (iv) 1935"),
              FIO("FiO3.q2", "Figure it Out (identities and patterns, question 2)",
                  "Use either a suitable identity or the distributive property to find each of the following "
                  "products. (i) (p − 1)(p + 11) (ii) (3a − 9b)(3a + 9b) (iii) −(2y + 5)(3y + 4) (iv) (6x + 5y)² "
                  "(v) (2x − 1/2)² (vi) (7p) × (3r) × (p + 2)",
                  ["(i) p² + 11p − p − 11 = p² + 10p − 11.",
                   "(ii) Sum times difference: (3a)² − (9b)² = 9a² − 81b².",
                   "(iii) (2y + 5)(3y + 4) = 6y² + 8y + 15y + 20 = 6y² + 23y + 20, so the product is −6y² − 23y − 20.",
                   "(iv) 36x² + 2 × 6x × 5y + 25y² = 36x² + 60xy + 25y².",
                   "(v) 4x² − 2 × 2x × 1/2 + 1/4 = 4x² − 2x + 1/4.",
                   "(vi) 7p × 3r = 21pr, and 21pr(p + 2) = 21p²r + 42pr."],
                  "(i) p² + 10p − 11 (ii) 9a² − 81b² (iii) −6y² − 23y − 20 (iv) 36x² + 60xy + 25y² "
                  "(v) 4x² − 2x + 1/4 (vi) 21p²r + 42pr"),
              FIO("FiO3.q4", "Figure it Out (identities and patterns, question 4)",
                  "Consider any 2 by 2 square of numbers in a calendar. Find the products of the numbers lying along "
                  "each diagonal, for example 4 × 12 = 48 and 5 × 11 = 55. Do this for the other 2 by 2 squares. "
                  "What do you observe about the diagonal products? Explain why this happens. (Hint: label the "
                  "numbers in each 2 by 2 square as a, a + 1 in the top row and a + 7, a + 8 in the bottom row.)",
                  ["Another square: 3, 4 over 10, 11 gives 3 × 11 = 33 and 4 × 10 = 40; again 40 − 33 = 7.",
                   "The diagonals are a × (a + 8) and (a + 1) × (a + 7).",
                   "a(a + 8) = a² + 8a.",
                   "(a + 1)(a + 7) = a² + 7a + a + 7 = a² + 8a + 7.",
                   "The difference is always 7."],
                  "The diagonal products always differ by 7, because (a + 1)(a + 7) − a(a + 8) = 7"),
              FIO("FiO3.q5", "Figure it Out (identities and patterns, question 5)",
                  "Verify which of the following statements are true. (i) (k + 1)(k + 2) − (k + 3) is always 2. "
                  "(ii) (2q + 1)(2q − 3) is a multiple of 4. (iii) Squares of even numbers are multiples of 4, and "
                  "squares of odd numbers are 1 more than multiples of 8. (iv) (6n + 2)² − (4n + 3)² is 5 less "
                  "than a square number.",
                  ["(i) k² + 3k + 2 − k − 3 = k² + 2k − 1; for k = 1 it is 2 but for k = 2 it is 7. False.",
                   "(ii) 4q² − 6q + 2q − 3 = 4q² − 4q − 3, which is odd. False.",
                   "(iii) (2m)² = 4m², and (2m + 1)² = 4m² + 4m + 1 = 4m(m + 1) + 1; m(m + 1) is even, so 4m(m + 1) "
                   "is a multiple of 8. True.",
                   "(iv) 36n² + 24n + 4 − (16n² + 24n + 9) = 20n² − 5; 20n² is not a square for n = 1. False."],
                  "(i) False (ii) False (iii) True (iv) False"),
              FIO("FiO3.q6", "Figure it Out (identities and patterns, question 6)",
                  "A number leaves a remainder of 3 when divided by 7, and another number leaves a remainder of 5 "
                  "when divided by 7. What is the remainder when their sum, difference, and product are divided "
                  "by 7?",
                  ["Write the numbers as 7a + 3 and 7b + 5.",
                   "Sum: 7a + 7b + 8 = 7(a + b + 1) + 1, remainder 1.",
                   "Difference: (7b + 5) − (7a + 3) = 7(b − a) + 2, remainder 2; the other order leaves 5.",
                   "Product: 49ab + 35a + 21b + 15 = 7(7ab + 5a + 3b + 2) + 1, remainder 1."],
                  "Sum: remainder 1; difference: remainder 2 (or 5 the other way round); product: remainder 1"),
              FIO("FiO3.q7", "Figure it Out (identities and patterns, question 7)",
                  "Choose three consecutive numbers, square the middle one, and subtract the product of the other "
                  "two. Repeat the same with other sets of numbers. What pattern do you notice? How do we write "
                  "this as an algebraic equation? Expand both sides of the equation to check that it is a true "
                  "identity.",
                  ["5, 6, 7: 6² − 5 × 7 = 36 − 35 = 1. 9, 10, 11: 100 − 99 = 1.",
                   "Call the numbers n − 1, n and n + 1.",
                   "n² − (n − 1)(n + 1) = n² − (n² − 1).",
                   "= 1, for every n."],
                  "The result is always 1: n² − (n − 1)(n + 1) = 1"),
              FIO("FiO3.q9", "Figure it Out (identities and patterns, question 9)",
                  "Which is larger? Find out without fully computing the product. (i) 14 × 26 or 16 × 24 "
                  "(ii) 25 × 75 or 26 × 74",
                  ["(i) 14 × 26 = (20 − 6)(20 + 6) = 400 − 36 and 16 × 24 = (20 − 4)(20 + 4) = 400 − 16.",
                   "Less is taken away from 400 in 16 × 24, so 16 × 24 = 384 is larger than 14 × 26 = 364.",
                   "(ii) 25 × 75 = (50 − 25)(50 + 25) = 2500 − 625 and 26 × 74 = (50 − 24)(50 + 24) = 2500 − 576.",
                   "So 26 × 74 = 1924 is larger than 25 × 75 = 1875."],
                  "(i) 16 × 24 is larger (ii) 26 × 74 is larger")])],
    key_terms=["mistake", "simplification", "identity"]))

# ============================== T9 This way or that way ======================================================
TOPICS.append(TOPIC(
    "T9", "M4", "This Way or That Way", ["6.4"], "Analyze",
    "Students describe a growing pattern of circles or tiles and the area of a region in several different ways, "
    "simplify every expression to show the ways agree, and use the expression to find later steps and areas.",
    "One pattern or region can be seen in many ways: (k + 1)² − 1, k² + 2k, k(k + 1) + k and k(k + 2) all count "
    "the same circles. Expanding the expressions shows they are equal, and creative ways of seeing are all "
    "welcome.",
    [A("T9.C1", "Many ways to count one growing pattern", "Analyze",
       "Students count the circles in a growing pattern four ways, simplify each expression to k² + 2k, and find "
       "the number of circles in Step 10 and Step 15.",
       textbook=["Observe the pattern in the figure below. Draw the next figure in the sequence. How many circles "
                 "does it have? How many total circles are there in Step 10? Write an expression for the number of "
                 "circles in Step k.",
                 "There are many ways of interpreting this pattern.",
                 "Does your method match any of these, or is it different? Each expression that we have identified "
                 "appears different, but are they really different? Since they describe the same pattern, they "
                 "should all be the same. Let us simplify each expression and find out.",
                 "When carried out correctly, all methods lead to the same answer; k² + 2k. The expression k² + 2k "
                 "gives the number of circles at Step k of this pattern.",
                 "Use this formula to find the number of circles in Step 15.",
                 "In Mathematics, there are often multiple ways of looking at a pattern, and different ways of "
                 "approaching and solving the same problem."],
       teach=["Predict first: Step 1 has 3 circles, Step 2 has 8, Step 3 has 15. How many in Step 4?",
              "See it as a square of side k + 1 with one circle missing: (k + 1)² − 1.",
              "Or as a k by k square with two strips of k: k² + 2k. Or k(k + 1) + k, or a k by (k + 2) rectangle.",
              "Every way simplifies to k² + 2k, so the different-looking answers are all right."],
       examples=[
           WE("Write the number of circles in Step k in two ways, show they agree, and find Steps 4, 10 and 15.",
              ["One way: a square of side k + 1 with one circle missing, (k + 1)² − 1 = k² + 2k + 1 − 1 = k² + 2k.",
               "Another way: a rectangle of k by k + 2, k(k + 2) = k² + 2k.",
               "Step 4: 16 + 8 = 24.",
               "Step 10: 100 + 20 = 120.",
               "Step 15: 225 + 30 = 255."],
              "k² + 2k circles; Step 4 has 24, Step 10 has 120, Step 15 has 255",
              ncert=["6.4.circles", "6.4.circles_step15"])],
       ncert=["6.4.many_ways"],
       key_terms=["pattern", "expression", "step"], misconceptions=["M_ONE_RIGHT_WAY"], minutes=9),
     A("T9.C1x", "Counting square tiles two ways", "Analyze",
       "Students count the square tiles in a growing pattern, find the tiles in Step 4 and Step 10, and write the "
       "tiles in Step n in two ways.",
       textbook=["Consider the pattern made of square tiles in the picture below.",
                 "How many square tiles are there in each figure?",
                 "How many are there in Step 4 of the sequence? What about Step 10?",
                 "Write an algebraic expression for the number of tiles in Step n.",
                 "Share your methods with the class. Can you find more than one method to arrive at the answer?"],
       teach=["Predict first: the steps have 8, 12 and 16 tiles. How many in Step 10?",
              "The tiles form a square frame round an empty square of side n.",
              "Big square minus hole: (n + 2)² − n². Or four sides: 4n + 4."],
       examples=[
           WE("The tile pattern has 8, 12 and 16 tiles in its first three steps. Find the tiles in Step 4, Step 10 "
              "and Step n.",
              ["Step n is a square of side n + 2 with a hole of side n.",
               "(n + 2)² − n² = n² + 4n + 4 − n² = 4n + 4.",
               "Counted as four rows of n plus four corners, it is again 4n + 4.",
               "Step 4: 16 + 4 = 20. Step 10: 40 + 4 = 44."],
              "Step 4 has 20 tiles, Step 10 has 44, Step n has (n + 2)² − n² = 4n + 4",
              ncert=["6.4.tiles"])],
       key_terms=["pattern", "square tiles"], misconceptions=["M_ONE_RIGHT_WAY"], minutes=5, thin=True),
     A("T9.C2", "One area, several expressions", "Analyze",
       "Students find the area of the shaded square inside four equal rectangles by Tadang's method and Yusuf's "
       "method, and expand both expressions to show (m + n)² − 4mn = (n − m)².",
       textbook=["Find the area of the (interior) shaded region in the figure below. All four rectangles have the "
                 "same dimensions.",
                 "Tadang's method: The total region is a square of side (m + n) with an area (m + n)². Subtracting "
                 "the area of four rectangles from the total area will give the area of the interior shaded region. "
                 "That is, (m + n)² − 4mn.",
                 "Yusuf's method: The shaded region is a square with sidelength (n − m). So, its area is (n − m)².",
                 "By expanding both expressions, check that (m + n)² − 4mn = (n − m)²."],
       teach=["Predict first: four m by n rectangles surround a small square. Is its area found by adding or by "
              "taking away?",
              "Tadang takes the four rectangles away from the big square: (m + n)² − 4mn.",
              "Yusuf reads the side of the small square directly: n − m, so (n − m)².",
              "Expand both: they are the same expression."],
       examples=[
           WE("Show that Tadang's expression (m + n)² − 4mn and Yusuf's expression (n − m)² are equal.",
              ["Tadang: (m + n)² − 4mn = m² + 2mn + n² − 4mn.",
               "= m² − 2mn + n².",
               "Yusuf: (n − m)² = n² − 2mn + m².",
               "Both are m² − 2mn + n², so the two methods agree."],
              "(m + n)² − 4mn = (n − m)² = m² − 2mn + n²",
              ncert=["6.4.tadang_yusuf"])],
       key_terms=["area", "expression", "region"], misconceptions=["M_ONE_RIGHT_WAY"], minutes=8,
       tool="four_rectangles_square"),
     A("T9.C2x", "Three ways to the slanted region", "Analyze",
       "Students check that Anusha's, Vaishnavi's and Aditya's expressions for the area of the region with slanting "
       "lines are equal and find the area when x = 8 and y = 3.",
       textbook=["Find out the area of the region with slanting lines in the figure. All three rectangles have the "
                 "same dimensions.",
                 "Anusha's method: Required area = Area (ABCD) − Area (EFGH). Area of ABCD = x². Area of EFGH = xy. "
                 "Required area = x² − xy.",
                 "Vaishnavi's method: QS = y + x + y = x + 2y. Area of PQSR = x (x + 2y). Required area = Area of "
                 "PQSR − (area of the three rectangles) = x (x + 2y) − 3xy.",
                 "Aditya's method: The required area is 2 times the area of JKLM. JK = (x − y)/2, KM = x. Required "
                 "area = 2x ((x − y)/2) = x (x − y).",
                 "By expanding the expressions, verify that all three expressions are equivalent. If x = 8 and "
                 "y = 3, find the area of the shaded region."],
       teach=["Predict first: will three different methods give three different areas?",
              "Expand each expression and compare.",
              "Put in x = 8 and y = 3 at the end."],
       examples=[
           WE("Verify that x² − xy, x(x + 2y) − 3xy and x(x − y) are equal, and find the area for x = 8, y = 3.",
              ["Anusha: x² − xy.",
               "Vaishnavi: x(x + 2y) − 3xy = x² + 2xy − 3xy = x² − xy.",
               "Aditya: x(x − y) = x² − xy.",
               "For x = 8, y = 3: 64 − 24 = 40."],
              "All three equal x² − xy; the area is 40 square units",
              ncert=["6.4.slanted"])],
       key_terms=["area", "region"], misconceptions=["M_ONE_RIGHT_WAY"], minutes=5, thin=True),
     DOER("T9.C3", "Practice: describe it more than one way", "pattern_regrouper", "Analyze",
          "Students describe the area of the dashed region in two ways, simplify both expressions to the same "
          "expression, and find the area when p = 6, r = 3.5 and s = 9.",
          ["A pattern or an area can be described by several expressions.",
           "Correct expressions for the same thing simplify to the same expression.",
           "Check an expression by putting in a step number or a value."],
          items=[
              FIO("6.4.dashed", "Math Talk (area of the dashed region)",
                  "Write an expression for the area of the dashed region in the figure, a p by s rectangle with a "
                  "strip of width r removed along one side and one end. Use more than one method to arrive at the "
                  "answer. Substitute p = 6, r = 3.5 and s = 9, and calculate the area.",
                  ["Method 1: the dashed region is a rectangle of sides p − r and s − r, area (p − r)(s − r).",
                   "Method 2: the whole rectangle minus the two strips plus the corner removed twice: ps − pr − sr + "
                   "r².",
                   "(p − r)(s − r) = ps − pr − rs + r², so both methods agree.",
                   "For p = 6, r = 3.5, s = 9: (6 − 3.5)(9 − 3.5) = 2.5 × 5.5 = 13.75."],
                  "(p − r)(s − r) = ps − pr − sr + r²; the area is 13.75 square units"),
              FIO("FiO3.q3", "Figure it Out (identities and patterns, question 3)",
                  "For each statement identify the appropriate algebraic expression(s). (i) Two more than a square "
                  "number: 2 + s, (s + 2)², s² + 2, s² + 4, 2s², 2²s. (ii) The sum of the squares of two "
                  "consecutive numbers: m² + n², (m + n)², m² + 1, m² + (m + 1)², m² + (m − 1)², (m + (m + 1))², "
                  "(2m)² + (2m + 1)².",
                  ["(i) A square number is s²; two more than it is s² + 2.",
                   "(s + 2)² is the square of a number two more, not two more than a square.",
                   "(ii) Two consecutive numbers are m and m + 1, or m − 1 and m.",
                   "So m² + (m + 1)² and m² + (m − 1)² both fit; (2m)² + (2m + 1)² fits only some pairs."],
                  "(i) s² + 2 (ii) m² + (m + 1)² and m² + (m − 1)²"),
              FIO("FiO3.q8", "Figure it Out (identities and patterns, question 8)",
                  "What is the algebraic expression describing the following steps: add any two numbers, then "
                  "multiply this by half of the sum of the two numbers? Prove that this result will be half of the "
                  "square of the sum of the two numbers.",
                  ["Call the numbers a and b; their sum is a + b.",
                   "Half of the sum is (a + b)/2.",
                   "(a + b) × (a + b)/2 = (a + b)²/2.",
                   "That is half of the square of the sum. Check with 3 and 5: 8 × 4 = 32 and 64/2 = 32."],
                  "(a + b) × (a + b)/2 = (1/2)(a + b)²"),
              FIO("FiO3.q10", "Figure it Out (identities and patterns, question 10)",
                  "A tiny park is coming up in Dhauli. Two square plots, each of area g² sq. ft., will have a green "
                  "cover. All the remaining area is a walking path w ft. wide that needs to be tiled. Write an "
                  "expression for the area that needs to be tiled.",
                  ["The park is w + g + 2w + g + w = 2g + 4w long and w + g + w = g + 2w wide.",
                   "Whole park: (2g + 4w)(g + 2w) = 2g² + 4gw + 4gw + 8w² = 2g² + 8gw + 8w².",
                   "Take away the two plots, 2g².",
                   "Area to be tiled = 8gw + 8w² = 8w(g + w)."],
                  "8w² + 8gw sq. ft., that is 8w(w + g)"),
              FIO("FiO3.q11", "Figure it Out (identities and patterns, question 11)",
                  "For each of the two patterns shown, (i) draw the next figure in the sequence, (ii) find how many "
                  "basic units there are in Step 10, (iii) write an expression for the number of basic units in "
                  "Step y. Pattern (a) has 9, 16 and 25 units in Steps 1 to 3; pattern (b) has 5, 11 and 19.",
                  ["(a) The steps are squares of side 3, 4, 5, so Step 4 has 6² = 36 and Step y has (y + 2)².",
                   "(a) Step 10: 12² = 144.",
                   "(b) The steps are 2² + 1, 3² + 2, 4² + 3, so Step 4 has 5² + 4 = 29 and Step y has (y + 1)² + y.",
                   "(b) Step 10: 11² + 10 = 131."],
                  "(a) (y + 2)², Step 10 has 144 (b) (y + 1)² + y, Step 10 has 131")])],
    key_terms=["pattern", "expression", "area"]))

# ============================== T10 Summary and Coin Conjoin =================================================
TOPICS.append(TOPIC(
    "T10", "M5", "Summary: We Distribute, Yet Things Multiply", ["Summary", "Puzzle Time"], "Remember",
    None,
    "The product of two sums, the square of a sum, the square of a difference, the difference of two squares, many "
    "ways of seeing one pattern, and the Coin Conjoin puzzle.",
    [A("T10.C1", "What we found about distributing", "Remember",
       "Students restate the product of two sums (a + b)(c + d), the square of a sum, the square of a difference and "
       "the difference of two squares, and recall that one pattern has many expressions.",
       textbook=["We extended the distributive property to find the product of two expressions each of which has two "
                 "terms. The general form for the same is (a + b) × (c + d) = ac + ad + bc + bd.",
                 "We saw some special cases of this identity. (a + b)² = a² + 2ab + b², (a − b)² = a² − 2ab + b², "
                 "(a + b) (a − b) = a² − b².",
                 "We considered different patterns, and explored how to understand them using algebra. We saw that, "
                 "often, there are multiple ways to solve a problem and arrive at the same correct answer. Finding "
                 "different methods to approach and solve the same problem is a creative process."],
       teach=["The mango tray has its answer: one more row adds a whole row, and a(b + c) = ab + ac.",
              "Each term times each term: (a + b)(c + d) = ac + ad + bc + bd.",
              "Three special cases: (a + b)² = a² + 2ab + b², (a − b)² = a² − 2ab + b², (a + b)(a − b) = a² − b².",
              "One pattern can be seen many ways, and every correct way simplifies to the same expression."],
       ncert=["summary"], video_focus=["RECAP"], key_terms=["identity", "product of two sums"], minutes=8),
     A("T10.C2", "Coin Conjoin", "Analyze",
       "Students find the fewest coin moves that turn triangles of 3, 6, 10 and 15 coins upside down and look for a "
       "rule for any triangular number of coins.",
       textbook=["Coin Conjoin",
                 "Arrange 10 coins in a triangle as shown in the figure below on the left. The task is to turn the "
                 "triangle upside down by moving one coin at a time. How many moves are needed? What is the minimum "
                 "number of moves?",
                 "A triangle of 3 coins can be inverted (turned upside down) with a single move, and a triangle of 6 "
                 "coins can be inverted by moving 2 coins.",
                 "The 10-coin triangle can be flipped with just 3 moves; did you figure out how? Find out the minimum "
                 "possible moves needed to flip the next bigger triangle having 15 coins. Try the same for bigger "
                 "triangular numbers.",
                 "Is there a simple way to calculate the minimum number of coin moves needed for any such triangular "
                 "arrangement?"],
       teach=["Predict first: how many coins must move to turn a triangle of 10 coins upside down?",
              "Keep the largest possible block of coins still; move only the corners that stick out.",
              "The counts 1, 2, 3, 5 follow the number of coins divided by 3, rounded down."],
       examples=[
           WE("Find the fewest moves that turn a triangle of 10 coins upside down, and then a triangle of 15 coins.",
              ["For 10 coins (rows 1, 2, 3, 4), keep the middle block still and move the three corner coins: 3 "
               "moves.",
               "The pattern so far: 3 coins need 1 move, 6 need 2, 10 need 3.",
               "For 15 coins (rows 1 to 5), keeping the largest block still leaves 5 coins to move.",
               "Each count is the number of coins divided by 3, rounded down: 3, 6, 10, 15 give 1, 2, 3, 5."],
              "10 coins need 3 moves and 15 coins need 5; in general the coins divided by 3, rounded down",
              ncert=["puzzle"])],
       key_terms=["triangular number", "coins"], enrichment=True, minutes=6)],
    topic_type="summary"))
