# -*- coding: utf-8 -*-
"""Topics T5 to T7: special products (M3), the square of a sum, the square of a difference, and the difference of
two squares with its number patterns. Book pp 145 to 149."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T5 The square of a sum =====================================================
TOPICS.append(TOPIC(
    "T5", "M3", "The Square of a Sum", ["6.2"], "Apply",
    "Students find 65² by splitting a square into two squares and two rectangles, state and use the square of a "
    "sum (a + b)² = a² + 2ab + b² to expand expressions, and decide when (a + b)² is greater than a² + b².",
    "A square of side a + b splits into a², b² and two rectangles ab, so (a + b)² = a² + 2ab + b². It is greater "
    "than a² + b² exactly when ab is positive. The identity squares numbers like 65 and 104 quickly and expands "
    "expressions like (6x + 5)².",
    [A("T5.C1", "Squaring 65 by splitting the square", "Apply",
       "Students split a square of side 65 into a square of 60, a square of 5 and two rectangles of 60 by 5, and "
       "add the four areas to find 65².",
       textbook=["The area of a square of sidelength 60 units is 3600 sq. units (60²) and that of a square of "
                 "sidelength 5 units is 25 sq. units (5²). Can we use this to find the area of a square of "
                 "sidelength 65 units?",
                 "A square of sidelength 65 can be split into 4 regions as shown in the figure, a square of "
                 "sidelength 60, a square of sidelength 5, and two rectangles of sidelengths 60 and 5.",
                 "65² = (60 + 5)² = 60² + 5² + 2 × (60 × 5) = 3600 + 25 + 600 = 4225 sq. units.",
                 "(60 + 5) × (60 + 5) = 60 × 60 + 5 × 60 + 60 × 5 + 5 × 5 = 60² + 2 × (60 × 5) + 5².",
                 "What if we write 65² as (30 + 35)² or (52 + 13)²? Draw the figures and check the area that you "
                 "get."],
       teach=["Predict first: 60² = 3600 and 5² = 25. Is 65² equal to 3600 + 25 = 3625?",
              "Split the square of side 65: a 60 by 60 square, a 5 by 5 square, and two 60 by 5 rectangles.",
              "The two rectangles are the parts 3600 + 25 forgets: 2 × (60 × 5) = 600.",
              "So 65² = 3600 + 600 + 25 = 4225. Any split of 65 works, because the four areas always fill the "
              "square."],
       examples=[
           WE("Find 65² by splitting 65 as 60 + 5, and check with the split 30 + 35.",
              ["The four parts: 60² = 3600, 5² = 25 and two rectangles of 60 × 5 = 300.",
               "65² = 3600 + 300 + 300 + 25 = 4225.",
               "With 30 + 35: 30² = 900, 35² = 1225 and two rectangles of 30 × 35 = 1050.",
               "900 + 1050 + 1050 + 1225 = 4225, the same area."],
              "65² = 4225",
              ncert=["6.2.sq65", "6.2.sq65_splits"])],
       key_terms=["square", "area", "rectangle"], misconceptions=["M_SUM_SQUARE"], minutes=8),
     A("T5.C2", "The square of a sum identity", "Apply",
       "Students state the square of a sum identity (a + b)² = a² + 2ab + b², decide when it exceeds a² + b², and "
       "expand (m + 3)², (6 + p)² and (6x + 5)².",
       textbook=["Let us look at the general expression for the square of sum of two numbers, (a + b)².",
                 "Using the distributive property, (a + b)² can be expanded as (a + b) × (a + b) = a × a + a × b + "
                 "b × a + b × b = a² + 2ab + b², as we had already seen in Example 2.",
                 "Identity 1A: (a + b)² = a² + 2ab + b²",
                 "If a and b are any two integers, is (a + b)² always greater than a² + b²? If not, when is it "
                 "greater?",
                 "Use Identity 1A to write the expressions for the following. (i) (m + 3)² (ii) (6 + p)²",
                 "Expand (6x + 5)². (6x + 5)² = (6x)² + 5² + 2 × (6x × 5) = 36x² + 25 + 60x.",
                 "If you have difficulty remembering or using the general rule, you can just apply the distributive "
                 "property to multiply and get the desired result."],
       teach=["Predict first: is (a + b)² always bigger than a² + b²?",
              "(a + b)² = a² + 2ab + b², so it is bigger by 2ab: bigger when a and b have the same sign, equal when "
              "one is 0, smaller when their signs differ.",
              "Use it on expressions: (m + 3)² = m² + 6m + 9 and (6 + p)² = 36 + 12p + p².",
              "If the rule slips your mind, the distributive property always gets you there."],
       examples=[
           WE("Expand (6x + 5)² with the identity and with the distributive property, and say when (a + b)² is "
              "greater than a² + b².",
              ["With the identity: (6x)² + 2 × (6x × 5) + 5² = 36x² + 60x + 25.",
               "With the distributive property: (6x + 5)(6x + 5) = 36x² + 30x + 30x + 25 = 36x² + 60x + 25.",
               "In general (a + b)² − (a² + b²) = 2ab.",
               "For a = 5, b = −2: (5 + (−2))² = 9 but 25 + 4 = 29, so it is not always greater."],
              "36x² + 60x + 25; (a + b)² is greater than a² + b² only when ab is positive",
              ncert=["6.2.6x5", "6.2.compare_sum_sq"])],
       ncert=["6.2.id_sum_sq", "6.2.m3_6p"],
       key_terms=["identity", "square of a sum"], misconceptions=["M_SUM_SQUARE"], minutes=9),
     A("T5.C2x", "Expanding the square of a sum two ways", "Apply",
       "Students expand (3j + 2k)² using the square of a sum identity and again using the distributive property, "
       "and compare the two results.",
       textbook=["Expand (3j + 2k)² using both the identity and by applying the distributive property."],
       teach=["Predict first: will the middle term of (3j + 2k)² be 6jk or 12jk?",
              "The identity takes a = 3j and b = 2k.",
              "The distributive property gives the same four products and adds the two like terms."],
       examples=[
           WE("Expand (3j + 2k)² both ways.",
              ["Identity: (3j)² + 2 × (3j × 2k) + (2k)² = 9j² + 12jk + 4k².",
               "Distributive: (3j + 2k)(3j + 2k) = 9j² + 6jk + 6jk + 4k².",
               "6jk + 6jk = 12jk, so both give 9j² + 12jk + 4k²."],
              "9j² + 12jk + 4k²",
              ncert=["6.2.3j2k"])],
       key_terms=["square of a sum", "like terms"], misconceptions=["M_SUM_SQUARE"], minutes=5, thin=True),
     DOER("T5.C3", "Practice: square a sum", "square_of_sum", "Apply",
          "Students square 104 and 37 quickly by splitting each into two parts whose squares are easy and using the "
          "square of a sum.",
          ["(a + b)² = a² + 2ab + b²: two squares and two equal rectangles.",
           "(a + b)² is more than a² + b² by 2ab.",
           "Split a number into parts whose squares are easy, such as 100 + 4."],
          items=[
              FIO("6.2.sq104_37", "Math Talk (square of a sum)",
                  "Use the square of a sum to find the values of 104² and 37². (Hint: split 104 and 37 into sums of "
                  "numbers whose squares are easy to compute.)",
                  ["104 = 100 + 4, so 104² = 100² + 2 × 100 × 4 + 4².",
                   "= 10000 + 800 + 16 = 10816.",
                   "37 = 30 + 7, so 37² = 30² + 2 × 30 × 7 + 7².",
                   "= 900 + 420 + 49 = 1369."],
                  "104² = 10816 and 37² = 1369")])],
    key_terms=["square of a sum", "identity", "area"]))

# ============================== T6 The square of a difference =============================================
TOPICS.append(TOPIC(
    "T6", "M3", "The Square of a Difference", ["6.2"], "Apply",
    "Students find 55² by removing two rectangles from a square of 60 and adding back the small square, state and "
    "use the square of a difference (a − b)² = a² − 2ab + b², and expand expressions with it.",
    "Taking two rectangles ab from a square a² removes the small square b² twice, so it is added back once: "
    "(a − b)² = a² − 2ab + b². It also follows from the square of a sum with b replaced by −b.",
    [A("T6.C1", "Squaring 55 inside a square of 60", "Apply",
       "Students find 55² from a square of 60 by removing two rectangles of 60 by 5 and adding back the small "
       "square of 5 that was removed twice.",
       textbook=["Can we use 60² (= 3600) and 5² (= 25) to find the value of (60 − 5)² or 55²? Let us approach this "
                 "through geometry by drawing a square of side length 55 sitting inside a square of sidelength 60.",
                 "We can get the area of the square of sidelength 55 by taking the area of the square of sidelength "
                 "60 and removing the areas of the two rectangles of sidelengths 60 and 5, i.e., 60² − (60 × 5) − "
                 "(5 × 60). By doing this, we remove the area of the small square of sidelength 5 twice.",
                 "We can add back the area of the square of sidelength 5 to this expression. That way, we are only "
                 "subtracting this area once.",
                 "So, (60 − 5)² = 60² − (60 × 5) − (5 × 60) + 5² = 3600 − 300 − 300 + 25 = 3025.",
                 "The area of the square of sidelength 55 is 3025 sq. units."],
       teach=["Predict first: is 55² equal to 3600 − 25?",
              "Draw a 55 square in the corner of a 60 square and cut away two 60 by 5 strips.",
              "The two strips overlap in the 5 by 5 corner, so that corner is removed twice.",
              "Add it back once: 55² = 3600 − 300 − 300 + 25 = 3025."],
       examples=[
           WE("Find 55² from the square of side 60.",
              ["Start with 60² = 3600.",
               "Remove two strips of 60 × 5 = 300 each: 3600 − 300 − 300 = 3000.",
               "The 5 by 5 corner was removed twice, so add 5² = 25 back once.",
               "55² = 3000 + 25 = 3025."],
              "55² = 3025",
              ncert=["6.2.sq55"])],
       key_terms=["square", "area", "rectangle"], misconceptions=["M_DIFF_SQUARE"], minutes=8),
     A("T6.C2", "The square of a difference identity", "Apply",
       "Students derive (a − b)² = a² − 2ab + b² by the distributive property and from the square of a sum, and "
       "expand (b − 6)², (−2a + 3)² and (7y − 3/(4z))².",
       textbook=["We have seen what (a + b)² gives when expanded. What is the expansion of (a − b)²?",
                 "Using the distributive property, (a − b)² = (a − b) × (a − b) = (a)² − ba − ab + (b)² = a² − 2ab + "
                 "b².",
                 "We can also use the expansion of (a + b)² to find the expansion of (a − b)². Think how. Hint: "
                 "(a − b)² = (a + (−b))².",
                 "Find the general expansion of (a − b)² using geometry, as we did for 55².",
                 "Identity 1B: (a − b)² = a² + b² − 2ab",
                 "Expand the following using both Identity 1B and by applying the distributive property "
                 "(i) (b − 6)² (ii) (−2a + 3)² (iii) (7y − 3/(4z))²"],
       teach=["Predict first: in (a − b)², is the b² term plus or minus?",
              "(a − b)(a − b) = a² − ab − ba + b², and (−b) × (−b) = +b².",
              "Or write a − b as a + (−b): (a + (−b))² = a² + 2a(−b) + (−b)² = a² − 2ab + b².",
              "The geometry of 55² is the same picture with letters: a² minus two strips ab, plus b² once."],
       examples=[
           WE("Expand (i) (b − 6)², (ii) (−2a + 3)², (iii) (7y − 3/(4z))².",
              ["(i) b² − 2 × b × 6 + 6² = b² − 12b + 36.",
               "(ii) Write it as (3 − 2a)²: 3² − 2 × 3 × 2a + (2a)² = 9 − 12a + 4a².",
               "(iii) (7y)² − 2 × 7y × 3/(4z) + (3/(4z))².",
               "2 × 7 × 3/4 = 42/4 = 21/2, so the middle term is 21y/(2z).",
               "(3/(4z))² = 9/(16z²), so (iii) is 49y² − 21y/(2z) + 9/(16z²)."],
              "(i) b² − 12b + 36 (ii) 4a² − 12a + 9 (iii) 49y² − 21y/(2z) + 9/(16z²)",
              ncert=["6.2.expand_diff_sq"])],
       ncert=["6.2.id_diff_sq", "6.2.diff_sq_geometry"],
       key_terms=["identity", "square of a difference"], misconceptions=["M_DIFF_SQUARE", "M_SIGN_DISTRIBUTE"],
       minutes=9),
     DOER("T6.C3", "Practice: square a difference", "square_of_difference", "Apply",
          "Students square 99 and 58 quickly by writing each as a round number minus a small number and using the "
          "square of a difference.",
          ["(a − b)² = a² − 2ab + b².",
           "The small square b² is added back because it was removed twice.",
           "Write a number as a round number minus a small one, such as 100 − 1."],
          items=[
              FIO("6.2.sq99_58", "Math Talk (square of a difference)",
                  "Use the square of a difference to find the values of (a) 99² and (b) 58².",
                  ["(a) 99 = 100 − 1, so 99² = 100² − 2 × 100 × 1 + 1².",
                   "= 10000 − 200 + 1 = 9801.",
                   "(b) 58 = 60 − 2, so 58² = 60² − 2 × 60 × 2 + 2².",
                   "= 3600 − 240 + 4 = 3364."],
                  "99² = 9801 and 58² = 3364")])],
    key_terms=["square of a difference", "identity", "area"]))

# ============================== T7 Patterns and the difference of squares ===================================
TOPICS.append(TOPIC(
    "T7", "M3", "Patterns and the Difference of Squares", ["6.2"], "Analyze",
    "Students explain the pattern that twice a sum of two squares is a sum of two squares, prove the difference "
    "of squares (a + b)(a − b) = a² − b² by expansion and by moving a piece, and use it for products and "
    "Sridharacharya's quick squares.",
    "Adding the square of a sum and the square of a difference gives 2(a² + b²) = (a + b)² + (a − b)². "
    "Multiplying a sum by a difference gives a² − b², which turns products like 98 × 102 into easy subtractions "
    "and gives a quick way to square numbers.",
    [A("T7.C1", "Twice a sum of squares", "Analyze",
       "Students test the pattern that twice a sum of two squares is a sum of two squares and explain it by adding "
       "the square of a sum and the square of a difference.",
       textbook=["Pattern 1: Look at the following pattern. 2 (2² + 1²) = 3² + 1², 2 (3² + 1²) = 4² + 2², "
                 "2 (6² + 5²) = 11² + 1², 2 (5² + 3²) = 8² + 2².",
                 "Take a pair of natural numbers. Calculate the sum of their squares. Can you write twice this sum "
                 "as a sum of two squares?",
                 "Notice that 2 (5² + 6²) = (6 + 5)² + (6 − 5)².",
                 "(a + b)² + (a − b)² = (a² + 2ab + b²) + (a² − 2ab + b²)",
                 "Adding the like terms a² + a² = 2a², b² + b² = 2b² and 2ab − 2ab = 0, we get 2 (a² + b²) = "
                 "(a + b)² + (a − b)²."],
       teach=["Predict first: 2 × (5² + 6²) = 122. Can 122 be written as a sum of two squares?",
              "Look at the lines of the pattern: the two new squares are the sum and the difference of the old "
              "numbers.",
              "Add the two identities: the 2ab and −2ab cancel, leaving 2a² + 2b².",
              "So 2(a² + b²) = (a + b)² + (a − b)² for every pair of numbers."],
       examples=[
           WE("Write 2 × (5² + 6²) as a sum of two squares, and explain why it works.",
              ["2 × (25 + 36) = 2 × 61 = 122.",
               "Use the sum and the difference: 6 + 5 = 11 and 6 − 5 = 1.",
               "11² + 1² = 121 + 1 = 122.",
               "In general (a + b)² + (a − b)² = a² + 2ab + b² + a² − 2ab + b² = 2a² + 2b²."],
              "2 × (5² + 6²) = 11² + 1², because 2(a² + b²) = (a + b)² + (a − b)²",
              ncert=["6.2.pattern1"])],
       key_terms=["pattern", "sum of squares"], misconceptions=["M_SUM_SQUARE"], minutes=8),
     A("T7.C2", "The difference of two squares", "Apply",
       "Students prove the difference of two squares (a + b)(a − b) = a² − b² by expansion and by moving a piece of "
       "a square, and use it to compute 98 × 102 and 45 × 55.",
       textbook=["Pattern 2: Here is a related pattern. 9 × 9 − 1 × 1 = 10 × 8, 8 × 8 − 6 × 6 = 14 × 2, 7 × 7 − "
                 "2 × 2 = 9 × 5, 10 × 10 − 4 × 4 = 14 × 6.",
                 "The pattern here appears to be a² − b² = (a + b) × (a − b). Is this a true identity?",
                 "Using the distributive property, we get (a + b) × (a − b) = a² − ab + ba − b². Adding the like "
                 "terms, ab + (−ab) = 0, we see that indeed (a + b) × (a − b) = a² − b².",
                 "Use Identity 1C to calculate 98 × 102, and 45 × 55.",
                 "Try This: Show that (a + b) × (a − b) = a² − b² geometrically. What do we get when this piece is "
                 "moved?"],
       teach=["Predict first: 9 × 9 − 1 × 1 = 80. Which product of two numbers near 9 gives 80?",
              "In every line the two factors are the sum and the difference of the two numbers.",
              "(a + b)(a − b) = a² − ab + ba − b², and −ab + ba = 0, so it is a² − b².",
              "Geometry: cut b² from the corner of a², slide one strip round, and the rest is an (a + b) by (a − b) "
              "rectangle.",
              "98 × 102 is (100 − 2)(100 + 2), a difference of squares."],
       examples=[
           WE("Calculate 98 × 102 and 45 × 55 using the difference of two squares.",
              ["98 × 102 = (100 − 2)(100 + 2) = 100² − 2².",
               "= 10000 − 4 = 9996.",
               "45 × 55 = (50 − 5)(50 + 5) = 50² − 5².",
               "= 2500 − 25 = 2475."],
              "98 × 102 = 9996 and 45 × 55 = 2475",
              ncert=["6.2.use_diff_squares", "6.2.pattern2"])],
       ncert=["6.2.id_diff_squares", "6.2.try_geometric"],
       key_terms=["difference of squares", "identity"], misconceptions=["M_DIFF_SQUARE"], minutes=9,
       tool="difference_of_squares_slide"),
     A("T7.C2x", "Sridharacharya's quick squares", "Apply",
       "Students explain why a² = (a + b)(a − b) + b² and use it to square 31 and 197 quickly.",
       textbook=["Sridharacharya (750 CE) gave an interesting method to quickly compute the squares of numbers using "
                 "Identity 1C! Consider the following modified form of this identity: a² = (a + b) (a − b) + b². Why "
                 "is this identity true?",
                 "Now, for example, 31² can be found by taking a = 31 and b = 1. 31² = (31 + 1) (31 − 1) + 1² = "
                 "32 × 30 + 1 = 961.",
                 "197² can be found by taking a = 197, and b = 3. 197² = (197 + 3) (197 − 3) + 3² = 200 × 194 + 9 = "
                 "38809."],
       teach=["Predict first: which b makes 197² easy, so that one factor is a round number?",
              "a² = (a + b)(a − b) + b² is the difference of squares with b² moved across.",
              "Choose b to make a + b or a − b a round number."],
       examples=[
           WE("Use a² = (a + b)(a − b) + b² to find 197².",
              ["Take a = 197 and b = 3, so a + b = 200.",
               "197² = (197 + 3)(197 − 3) + 3² = 200 × 194 + 9.",
               "200 × 194 = 38800.",
               "38800 + 9 = 38809."],
              "197² = 38809",
              ncert=["6.2.sridhara"])],
       key_terms=["difference of squares", "quick squares"], minutes=5, thin=True),
     DOER("T7.C3", "Practice: test and use the patterns", "identity_generaliser", "Analyze",
          "Students compare (a − b)² with (b − a)², express 100 as a difference of squares, square numbers with the "
          "identities, and test whether the patterns hold for negative integers and fractions.",
          ["2(a² + b²) = (a + b)² + (a − b)².",
           "(a + b)(a − b) = a² − b².",
           "An identity proved with letter-numbers holds for every number, not just the cases checked."],
          items=[
              FIO("FiO2.q1", "Figure it Out (squares and patterns, question 1)",
                  "Which is greater: (a − b)² or (b − a)²? Justify your answer.",
                  ["(a − b)² = a² − 2ab + b².",
                   "(b − a)² = b² − 2ba + a² = a² − 2ab + b².",
                   "Also b − a = −(a − b), and a number and its negative have the same square.",
                   "Check with a = 7, b = 2: (7 − 2)² = 25 and (2 − 7)² = 25."],
                  "Neither; they are always equal"),
              FIO("FiO2.q2", "Figure it Out (squares and patterns, question 2)",
                  "Express 100 as the difference of two squares.",
                  ["a² − b² = (a + b)(a − b), so look for two factors of 100 with an even sum.",
                   "100 = 50 × 2, so a + b = 50 and a − b = 2.",
                   "Then a = 26 and b = 24.",
                   "Check: 26² − 24² = 676 − 576 = 100."],
                  "100 = 26² − 24² (also 100 = 10² − 0²)"),
              FIO("FiO2.q3", "Figure it Out (squares and patterns, question 3)",
                  "Find 406², 72², 145², 1097² and 124² using the identities.",
                  ["406² = (400 + 6)² = 160000 + 4800 + 36 = 164836.",
                   "72² = (70 + 2)² = 4900 + 280 + 4 = 5184.",
                   "145² = (150 − 5)² = 22500 − 1500 + 25 = 21025.",
                   "1097² = (1100 − 3)² = 1210000 − 6600 + 9 = 1203409.",
                   "124² = (120 + 4)² = 14400 + 960 + 16 = 15376."],
                  "164836, 5184, 21025, 1203409, 15376"),
              FIO("FiO2.q4", "Figure it Out (squares and patterns, question 4)",
                  "Do the two patterns, twice a sum of two squares and the difference of two squares, hold only for "
                  "counting numbers? Do they hold for negative integers as well? What about fractions? Justify your "
                  "answer.",
                  ["Both patterns were proved by expanding with letter-numbers, using only the distributive property.",
                   "The distributive property holds for integers and fractions, so the identities hold for them too.",
                   "Check with a = −3, b = 1/2: 2 × (9 + 1/4) = 18.5, and (−2.5)² + (−3.5)² = 6.25 + 12.25 = 18.5.",
                   "Check with a = −5, b = 2: (−5 + 2) × (−5 − 2) = (−3) × (−7) = 21, and 25 − 4 = 21."],
                  "Yes; they hold for all numbers, including negative integers and fractions")])],
    key_terms=["difference of squares", "pattern", "identity"]))
