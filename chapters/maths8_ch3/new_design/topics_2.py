# -*- coding: utf-8 -*-
"""Topics T4 to T7 (module M2). Roman numerals (second half of 3.2) and 3.3 The Idea of a Base, pp 58 to 70.
Egyptian symbols are named in words: stroke 1, heel 10, coil 100, lotus 1000, finger 10000, tadpole 100000,
man 1000000, sun 10000000. The base-5 symbols of the book's Table 2 are: triangle 1, square 5, hexagon 25,
circle 125, wave 625, arrow 3125."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T4 Roman numerals ===========================================================
TOPICS.append(TOPIC(
    "T4", "M2", "Roman Numerals: Grouping into Landmarks", ["3.2"], "Apply",
    "Students write numbers in Roman numerals by grouping them into the landmark numbers I, V, X, L, C, D and M, "
    "add Roman numerals by regrouping symbols, and explain why multiplying Roman numerals is hard.",
    "Roman numerals group a number into landmark numbers, as many of the largest as possible first. Adding works by "
    "counting and regrouping symbols, but the group sizes change from landmark to landmark, so multiplying is hard.",
    [A("T4.C1", "Group a number into landmark numbers", "Apply",
       "Students write a number as a sum of the Roman landmark numbers, taking as many of the largest as possible "
       "first, and turn the sum into a Roman numeral such as MMCCCLXVII for 2367.",
       textbook=["IV. The Roman Numerals",
                 "To get the Roman numeral for any number till 39, it is first grouped into as many 10s as possible, "
                 "the remaining is grouped into as many 5s as possible, and finally the remaining is grouped into 1s.",
                 "Example: Let us take the number 27. 27 = 10 + 10 + 5 + 1 + 1. So, 27 in Roman numerals is XXVII.",
                 "Instead of representing 50 as XXXXX, a new symbol is given to it: L. Following the way the number 4 "
                 "is represented as 1 less than 5, that is, as IV, 40 is represented as 10 less than 50, that is, as "
                 "XL.",
                 "Let us call all these numbers that have a new basic symbol as landmark numbers.",
                 "I 1, V 5, X 10, L 50, C 100, D 500, M 1,000.",
                 "Consider the number 2367. Writing it as a sum of landmark numbers starting from 1000 such that we "
                 "take as many 1000s as possible, 500s as possible, and so on, we get 2367 = 1000 + 1000 + 100 + 100 "
                 "+ 100 + 50 + 10 + 5 + 1 + 1.",
                 "This system seems to have evolved out of the ancient Greek number system in around the 8th century "
                 "BCE in Rome, and evolved over time."],
       teach=["Predict first: how many M's, C's and other symbols will the Roman numeral for 2367 need?",
              "A landmark number is one with its own symbol: I, V, X, L, C, D, M stand for 1, 5, 10, 50, 100, 500, "
              "1000.",
              "Take as many of the largest landmark as fit, then the next, and so on down to I.",
              "Write the symbols from largest to smallest; 4 is IV and 40 is XL, one less or ten less than the next "
              "landmark."],
       examples=[
           WE("Write 2367 as a sum of Roman landmark numbers and then as a Roman numeral.",
              ["Two 1000s fit in 2367: 2367 − 2000 = 367. No 500 fits in 367.",
               "Three 100s fit: 367 − 300 = 67. One 50 fits: 67 − 50 = 17.",
               "One 10 fits: 17 − 10 = 7. One 5 fits: 7 − 5 = 2, which is two 1s.",
               "So 2367 = 1000 + 1000 + 100 + 100 + 100 + 50 + 10 + 5 + 1 + 1.",
               "Writing one symbol for each landmark, 2367 is written as MMCCCLXVII."],
              "2367 = 1000 + 1000 + 100 + 100 + 100 + 50 + 10 + 5 + 1 + 1, written as MMCCCLXVII",
              ncert=["3.2.roman_27", "3.2.roman_L_XL", "3.2.landmarks", "3.2.roman_2367", "3.2.roman_history"])],
       key_terms=["landmark number", "Roman numeral"], misconceptions=["M_ROMAN_PLACE"], minutes=10),
     A("T4.C2", "Adding Roman numerals by regrouping", "Apply",
       "Students add two Roman numerals without converting them, by counting each symbol and regrouping five I's "
       "into V, five C's into D and so on, as in CCXXXII + CCCCXIII.",
       textbook=["Despite the relative efficiency of the Roman system, it doesn't lend itself to an easy performance "
                 "of arithmetic operations, particularly multiplication and division.",
                 "Example: Try adding the following numbers without converting them to Hindu numerals: (a) CCXXXII + "
                 "CCCCXIII",
                 "Let us find the total number of Is, Xs, and Cs, and group them starting from the largest landmark "
                 "number.",
                 "Apparently, it looks like the largest landmark number is C, but note that 5 Cs (100s) make a D "
                 "(500).",
                 "The efficiency of this system is due to the grouping of a given number by not just one group size, "
                 "but a sequence of group sizes that we call landmark numbers."],
       teach=["Predict first: will the sum of CCXXXII and CCCCXIII need a D?",
              "Count each symbol in both numerals together: C's, X's and I's.",
              "Regroup: five I's make V, five X's make L, five C's make D; four of a symbol is written with the next "
              "landmark.",
              "Write the regrouped symbols from largest to smallest."],
       examples=[
           WE("Add CCXXXII and CCCCXIII without converting them to Hindu numerals.",
              ["Count the symbols: C's 2 + 4 = 6, X's 3 + 1 = 4, I's 2 + 3 = 5.",
               "Five I's make one V.",
               "Four X's are written as XL, ten less than fifty.",
               "Six C's: five C's make a D, and one C is left, so DC.",
               "The sum is DCXLV. Check with our numerals: 232 + 413 = 645."],
              "DCXLV",
              ncert=["3.2.roman_add_a"])],
       key_terms=["regroup", "Roman numeral"], misconceptions=["M_ROMAN_ADD_DIGITS"], minutes=8),
     A("T4.C3", "A second Roman sum: LXXXVII + LXXVIII", "Apply",
       "Students add LXXXVII and LXXVIII by counting L's, X's, V's and I's and regrouping each step into the next "
       "landmark.",
       textbook=["Do it yourself now: (b) LXXXVII + LXXVIII"],
       teach=["Predict first: will this sum need a C?",
              "Count each symbol: L's, X's, V's and I's.",
              "Regroup from the smallest: five I's make V, two V's make X, five X's make L, two L's make C.",
              "Write what is left from largest to smallest."],
       examples=[
           WE("Add LXXXVII and LXXVIII without converting them to Hindu numerals.",
              ["Count the symbols: L's 1 + 1 = 2, X's 3 + 2 = 5, V's 1 + 1 = 2, I's 2 + 3 = 5.",
               "Five I's make a V, so now there are 3 V's: two of them make an X and one V stays.",
               "That gives 6 X's: five make an L and one X stays, so now there are 3 L's.",
               "Two L's make a C and one L stays.",
               "The sum is CLXV. Check with our numerals: 87 + 78 = 165."],
              "CLXV",
              ncert=["3.2.roman_add_b"])],
       key_terms=["regroup"], misconceptions=["M_ROMAN_ADD_DIGITS"], minutes=6, thin=True),
     A("T4.C4", "Why multiplying Roman numerals is hard", "Analyze",
       "Students multiply pairs of Roman landmark numbers, find that some products such as L × D have no single "
       "symbol, and explain why Roman numerals make multiplication hard.",
       textbook=["How will you multiply two numbers given in Roman numerals, without converting them to Hindu "
                 "numerals? Try to find the product of the following pairs of landmark numbers: V × L, L × D, V × D, "
                 "VII × IX.",
                 "Multiply CCXXXI and MDCCCLII.",
                 "People using the Roman system made use of a calculating tool called the abacus to perform their "
                 "arithmetic operations. However, only specially trained people used this tool for calculation.",
                 "While going through the number systems discussed above, it should not be understood that, "
                 "historically, one system developed as an improvement over the previous system."],
       teach=["Predict first: is V × L another landmark number?",
              "V × L is 5 × 50 = 250, which is CCL: not a landmark, so it needs several symbols.",
              "L × D is 50 × 500 = 25000, which needs 25 M's, since no Roman symbol is bigger than M.",
              "Because the landmarks grow by 5 and then by 2, their products land anywhere, so there is no simple "
              "rule for multiplying."],
       examples=[
           WE("Find V × L, L × D, V × D and VII × IX in Roman numerals.",
              ["V × L is 5 × 50 = 250, which is 100 + 100 + 50, written as CCL.",
               "L × D is 50 × 500 = 25000, which is 25 thousands, written as M repeated 25 times.",
               "V × D is 5 × 500 = 2500, which is 1000 + 1000 + 500, written as MMD.",
               "VII × IX is 7 × 9 = 63, which is 50 + 10 + 1 + 1 + 1, written as LXIII.",
               "None of these products is a single landmark symbol, so there is no simple rule."],
              "V × L is CCL, L × D is 25 M's, V × D is MMD and VII × IX is LXIII",
              ncert=["3.2.roman_multiply", "3.2.roman_product_big", "3.2.abacus_note", "3.2.not_linear"])],
       key_terms=["product", "landmark number"], misconceptions=["M_LANDMARK_PRODUCT", "M_LINEAR_HISTORY"],
       minutes=8),
     DOER("T4.C5", "Practice: write and compare Roman numerals", "roman_builder", "Apply",
          "Students write numbers in Roman numerals, list the features that make the Hindu number system more "
          "efficient than the Roman system, and refine a number system of their own.",
          ["Group a number into landmarks, as many of the largest as possible first.",
           "Roman landmarks grow by 5 and then by 2, so adding needs care and multiplying is hard."],
          items=[
              FIO("FiOB.q1", "Figure it Out (Roman numerals, question 1)",
                  "Represent the following numbers in the Roman system. (i) 1222 (ii) 2999 (iii) 302 (iv) 715",
                  ["(i) 1222 = 1000 + 100 + 100 + 10 + 10 + 1 + 1, written as MCCXXII.",
                   "(ii) 2999 = 1000 + 1000 + 900 + 90 + 9; 900 is CM, 90 is XC and 9 is IX, so it is written as "
                   "MMCMXCIX.",
                   "(iii) 302 = 100 + 100 + 100 + 1 + 1, written as CCCII.",
                   "(iv) 715 = 500 + 100 + 100 + 10 + 5, written as DCCXV."],
                  "(i) MCCXXII (ii) MMCMXCIX (iii) CCCII (iv) DCCXV"),
              FIO("FiOC.q3", "Figure it Out (early number systems, question 3)",
                  "Identify the features of the Hindu number system that make it efficient when compared to the "
                  "Roman number system.",
                  ["Place value: in our numerals the position of a digit tells its landmark, so ten digits write every "
                   "number; Roman symbols have fixed values and need new symbols for bigger numbers.",
                   "Zero: we have a digit 0 for an empty place; the Roman system has no symbol for zero.",
                   "Calculation: adding, subtracting, multiplying and dividing follow simple column rules in our "
                   "system, while Roman numerals make them very hard."],
                  "Place value with ten digits, a symbol for zero, and easy calculation"),
              FIO("FiOC.q4", "Figure it Out (early number systems, question 4)",
                  "Using the ideas discussed in this section, try refining the number system you might have made "
                  "earlier.",
                  ["Look at your own system: does it need one mark for every object?",
                   "Add a group size: give a new symbol to a group, such as five marks.",
                   "Add landmark numbers: give new symbols to bigger groups too, such as five groups of five.",
                   "Write a few numbers in the refined system and check that they are shorter than before."],
                  "Open answer: for example, add symbols for groups and for groups of groups")],
          misconceptions=["M_ROMAN_PLACE", "M_ROMAN_ADD_DIGITS"])],
    key_terms=["landmark number", "Roman numeral", "regroup"]))

# ============================== T5 The Egyptian system ======================================================
TOPICS.append(TOPIC(
    "T5", "M2", "The Egyptian System: Landmarks that are Powers of Ten", ["3.3"], "Apply",
    "Students build the Egyptian landmark numbers by grouping 10 of each landmark into the next, and write and read "
    "Egyptian numerals by grouping a number into powers of 10.",
    "In the Egyptian system every landmark number is 10 times the one before, so the landmarks are 1, 10, 100, 1000 "
    "and so on, the powers of 10. A number is written with as many of each symbol as its grouping needs.",
    [A("T5.C1", "Each landmark is ten of the one before", "Apply",
       "Students build the Egyptian landmarks 1, 10, 100, 1000 and onwards by grouping 10 of each into the next, and "
       "write a number such as 2153 as lotuses, coils, heels and strokes.",
       textbook=["3.3 The Idea of a Base",
                 "I. The Egyptian Number System: We are now going to see a written number system that the Egyptians "
                 "developed around 3000 BCE.",
                 "Imagine making collections of pebbles. The first landmark number is 1. Group together 10 "
                 "collections of the previous landmark number (1). Its size is the second landmark number which is "
                 "10. Group together 10 collections of the previous landmark number (10). Its size is the third "
                 "landmark number which is 10 × 10 = 100, and so on.",
                 "Each landmark number is 10 times the previous one. Since 1 is the first landmark number, they are "
                 "all powers of 10.",
                 "As in the case of Roman numbers, a given number is counted in groups of the landmark numbers, "
                 "starting from the largest landmark number less than the given number.",
                 "For example 324 which equals 100 + 100 + 100 + 10 + 10 + 4 is written as three coils, two heels "
                 "and four strokes."],
       teach=["Predict first: if each new landmark is ten of the last, what comes after 1, 10 and 100?",
              "Ten 1s make 10, ten 10s make 100, ten 100s make 1000: every landmark is a power of 10.",
              "The Egyptians drew a stroke for 1, a heel for 10, a coil for 100, a lotus for 1000, and so on up to "
              "10000000.",
              "To write a number, take as many of the largest landmark as fit, then the next, and draw that many "
              "symbols."],
       examples=[
           WE("Write 2153 in Egyptian numerals.",
              ["The largest landmark that fits is 1000: two of them, 2153 − 2000 = 153.",
               "One 100 fits: 153 − 100 = 53.",
               "Five 10s fit: 53 − 50 = 3, which is three 1s.",
               "So 2153 = 1000 + 1000 + 100 + 10 + 10 + 10 + 10 + 10 + 1 + 1 + 1.",
               "It is written as 2 lotuses, 1 coil, 5 heels and 3 strokes."],
              "2 lotuses, 1 coil, 5 heels and 3 strokes",
              ncert=["3.3.egypt_landmarks", "3.3.egypt_symbols", "3.3.egypt_324"])],
       key_terms=["landmark number", "powers of 10"], misconceptions=["M_TEN_SYMBOLS_OK"], minutes=10),
     A("T5.C2", "Reading an Egyptian numeral", "Apply",
       "Students read an Egyptian numeral back into our numerals by adding the value of every symbol, even when a "
       "landmark is missing.",
       textbook=["Each landmark number is 10 times the previous one."],
       teach=["Predict first: if a numeral has lotuses, heels and strokes but no coils, what digit sits in the "
              "hundreds place?",
              "Each symbol keeps its own value wherever it is drawn: a lotus is always 1000.",
              "Add up the values of all the symbols.",
              "A landmark with no symbols simply adds nothing."],
       examples=[
           WE("An Egyptian numeral shows 3 lotuses, 4 heels and 6 strokes. What number is it?",
              ["3 lotuses: 1000 + 1000 + 1000 = 3000.",
               "No coils, so no hundreds.",
               "4 heels: 10 + 10 + 10 + 10 = 40. 6 strokes: 6.",
               "Total: 3000 + 40 + 6 = 3046."],
              "3046")],
       key_terms=["read a numeral"], misconceptions=["M_TEN_SYMBOLS_OK"], minutes=5, thin=True),
     DOER("T5.C3", "Practice: write and read Egyptian numerals", "egypt_board", "Apply",
          "Students write numbers in Egyptian numerals by grouping them into powers of 10, and read Egyptian "
          "numerals back into our numerals.",
          ["The Egyptian landmarks are 1, 10, 100, 1000, ...: each is 10 times the one before.",
           "Take as many of the largest landmark as fit, then move down."],
          items=[
              FIO("FiOD.q1", "Figure it Out (Egyptian numerals, question 1)",
                  "Represent the following numbers in the Egyptian system: 10458, 1023, 2660, 784, 1111, 70707.",
                  ["10458 = 10000 + 400 + 50 + 8: 1 finger, 4 coils, 5 heels and 8 strokes.",
                   "1023 = 1000 + 20 + 3: 1 lotus, 2 heels and 3 strokes. 2660 = 2000 + 600 + 60: 2 lotuses, 6 coils "
                   "and 6 heels.",
                   "784 = 700 + 80 + 4: 7 coils, 8 heels and 4 strokes. 1111 = 1000 + 100 + 10 + 1: one lotus, one "
                   "coil, one heel and one stroke.",
                   "70707 = 70000 + 700 + 7: 7 fingers, 7 coils and 7 strokes."],
                  "10458: 1 finger, 4 coils, 5 heels, 8 strokes; 1023: 1 lotus, 2 heels, 3 strokes; 2660: 2 lotuses, "
                  "6 coils, 6 heels; 784: 7 coils, 8 heels, 4 strokes; 1111: one of each of lotus, coil, heel, "
                  "stroke; 70707: 7 fingers, 7 coils, 7 strokes"),
              FIO("FiOD.q2", "Figure it Out (Egyptian numerals, question 2)",
                  "What numbers do these numerals stand for? (i) 2 coils, 7 heels and 6 strokes (ii) 4 lotuses, 3 "
                  "coils, 2 heels and 2 strokes",
                  ["(i) 2 coils make 200, 7 heels make 70 and 6 strokes make 6.",
                   "200 + 70 + 6 = 276.",
                   "(ii) 4 lotuses make 4000, 3 coils make 300, 2 heels make 20 and 2 strokes make 2.",
                   "4000 + 300 + 20 + 2 = 4322."],
                  "(i) 276 (ii) 4322")],
          misconceptions=["M_TEN_SYMBOLS_OK"])],
    key_terms=["Egyptian numerals", "powers of 10"]))

# ============================== T6 The idea of a base =======================================================
TOPICS.append(TOPIC(
    "T6", "M2", "The Idea of a Base", ["3.3"], "Apply",
    "Students build a base-5 system by grouping 5 of each landmark into the next, write numbers in it, define a "
    "base-n system and find its landmark numbers as the powers of n.",
    "A base-n system starts its landmarks at 1 and multiplies by the same n each time, so the landmarks are the "
    "powers of n. The Egyptian system is base 10; grouping by 5 gives a base-5 system with landmarks 1, 5, 25, 125.",
    [A("T6.C1", "A base-5 system", "Apply",
       "Students build the base-5 landmarks 1, 5, 25, 125, 625 and 3125 by grouping 5 of each into the next, and "
       "write a number such as 89 with triangles, squares and hexagons.",
       textbook=["II. Variations on the Egyptian System and the Notion of Base",
                 "Instead of grouping together 10 collections of size equal to the previous landmark number (as in "
                 "the case of the Egyptian system), can we get a number system by grouping together 5 collections of "
                 "size equal to the previous landmark number? Can this 5 be replaced by any positive integer?",
                 "Group together 5 collections of size equal to the previous landmark number (1). Its size is the "
                 "second landmark number which is 5.",
                 "Thus, we have a new number system where each landmark number is 5 times the previous one. Since 1 "
                 "is the first landmark number, they are all powers of 5.",
                 "Express the number 143 in this new system. Let us start grouping, starting with the size 5³ = 125, "
                 "as this is the largest landmark number smaller than 143. We get 143 = 125 + 5 + 5 + 5 + 1 + 1 + 1."],
       teach=["Predict first: if we group in fives instead of tens, what are the first four landmarks?",
              "Five 1s make 5, five 5s make 25, five 25s make 125, five 125s make 625: the powers of 5.",
              "Give each landmark a symbol: triangle 1, square 5, hexagon 25, circle 125, wave 625, arrow 3125.",
              "To write a number, take as many of the largest landmark as fit, then move down."],
       examples=[
           WE("Write 89 in the base-5 system with triangle 1, square 5, hexagon 25 and circle 125.",
              ["125 is bigger than 89, so start with 25: three 25s fit, 89 − 75 = 14.",
               "Two 5s fit in 14: 14 − 10 = 4, which is four 1s.",
               "So 89 = 25 + 25 + 25 + 5 + 5 + 1 + 1 + 1 + 1.",
               "It is written as 3 hexagons, 2 squares and 4 triangles."],
              "3 hexagons, 2 squares and 4 triangles",
              ncert=["3.3.base5_build", "3.3.base5_143"])],
       key_terms=["base 5", "landmark number"], misconceptions=["M_BASE_TEN_ONLY"], minutes=10),
     A("T6.C2", "Base n: the landmarks are the powers of n", "Analyze",
       "Students define a base-n number system, find the landmark numbers of base 3 as 1, 3, 9, 27, 81, and write a "
       "number such as 50 in base 3.",
       textbook=["Number systems having landmark numbers in which the (a) first landmark number is 1, and (b) every "
                 "next landmark number is obtained by multiplying the current landmark number by some fixed number n "
                 "is said to be a base-n number system.",
                 "The Egyptian number system is a base-10 system, and the number system that we created is a base-5 "
                 "system. A base-10 number system is also called a decimal number system.",
                 "The landmark numbers of a base-n number system are the powers of n starting from 1, n, n², n³, ..."],
       teach=["Predict first: what are the landmarks of a base-3 system?",
              "A base-n system starts at 1 and multiplies by n each time: 1, n, n², n³ and so on.",
              "Base 10 is the Egyptian system, also called a decimal system; base 5 is the one we built.",
              "Any counting number bigger than 1 can be a base."],
       examples=[
           WE("Find the first five landmark numbers of a base-3 system and write 50 as a sum of them.",
              ["Start at 1 and multiply by 3: 1, 3, 9, 27, 81.",
               "81 is bigger than 50, so start with 27: one fits, 50 − 27 = 23.",
               "Two 9s fit in 23: 23 − 18 = 5. One 3 fits: 5 − 3 = 2, which is two 1s.",
               "So 50 = 27 + 9 + 9 + 3 + 1 + 1."],
              "Landmarks 1, 3, 9, 27, 81; 50 = 27 + 9 + 9 + 3 + 1 + 1",
              ncert=["3.3.base_n_def", "3.3.base_n_landmarks"])],
       key_terms=["base", "base-n system", "decimal"], misconceptions=["M_BASE_TEN_ONLY"], minutes=8),
     DOER("T6.C3", "Practice: build numbers in a base", "base_builder", "Apply",
          "Students write numbers in the base-5 system, decide whether every number can be written, find the "
          "landmarks of base 7 and of base n, explain why no Egyptian symbol repeats 10 times, and create a base-4 "
          "system.",
          ["In a base-n system the landmarks are 1, n, n², n³, ...",
           "n of any landmark make the next, so no symbol is ever needed n or more times."],
          items=[
              FIO("FiOE.q1", "Figure it Out (base-n systems, question 1)",
                  "Write the following numbers in the above base-5 system using the symbols in Table 2: 15, 50, 137, "
                  "293, 651.",
                  ["15 = 5 + 5 + 5: 3 squares. 50 = 25 + 25: 2 hexagons.",
                   "137 = 125 + 5 + 5 + 1 + 1: 1 circle, 2 squares and 2 triangles.",
                   "293 = 125 + 125 + 25 + 5 + 5 + 5 + 1 + 1 + 1: 2 circles, 1 hexagon, 3 squares and 3 triangles.",
                   "651 = 625 + 25 + 1: 1 wave, 1 hexagon and 1 triangle."],
                  "15: 3 squares; 50: 2 hexagons; 137: 1 circle, 2 squares, 2 triangles; 293: 2 circles, 1 hexagon, "
                  "3 squares, 3 triangles; 651: 1 wave, 1 hexagon, 1 triangle"),
              FIO("FiOE.q2", "Figure it Out (base-n systems, question 2)",
                  "Is there a number that cannot be represented in our base-5 system above? Why or why not?",
                  ["Every counting number can be grouped into powers of 5, using each symbol at most 4 times.",
                   "As numbers grow, we only need more landmark symbols, which can always be invented.",
                   "But 0 is the number of objects in an empty collection, and there is no symbol to draw for it.",
                   "So 0 cannot be represented."],
                  "Yes: 0 cannot be represented, because the system has no symbol for it"),
              FIO("FiOE.q3", "Figure it Out (base-n systems, question 3)",
                  "Compute the landmark numbers of a base-7 system. In general, what are the landmark numbers of a "
                  "base-n system?",
                  ["Start at 1 and multiply by 7 each time: 1, 7, 7 × 7 = 49, 49 × 7 = 343, 343 × 7 = 2401.",
                   "In general, start at 1 and multiply by n each time.",
                   "So the landmarks of base n are 1, n, n², n³, and so on, the powers of n."],
                  "Base 7: 1, 7, 49, 343, 2401, ...; base n: 1, n, n², n³, ..., the powers of n"),
              FIO("FiOG.q1", "Figure it Out (bases and their limits, question 1)",
                  "Can there be a number whose representation in Egyptian numerals has one of the symbols occurring "
                  "10 or more times? Why not?",
                  ["Every Egyptian landmark is 10 times the one before.",
                   "If a symbol appeared 10 times, those 10 symbols would make exactly one symbol of the next "
                   "landmark.",
                   "Grouping always takes as many of the larger landmark as possible, so the 10 would be regrouped.",
                   "So no symbol is ever written 10 or more times."],
                  "No: 10 of any symbol make one of the next landmark, so they are always regrouped"),
              FIO("FiOG.q2", "Figure it Out (bases and their limits, question 2)",
                  "Create your own number system of base 4, and represent numbers from 1 to 16.",
                  ["Landmarks of base 4: 1, 4, 16. Give them symbols, for example a dot for 1, a stick for 4 and a "
                   "square for 16.",
                   "1, 2, 3 are 1, 2, 3 dots; 4 is a stick; 5, 6, 7 are a stick and 1, 2, 3 dots.",
                   "8 is 2 sticks; 9, 10, 11 add 1, 2, 3 dots; 12 is 3 sticks; 13, 14, 15 add 1, 2, 3 dots.",
                   "16 is one square, since four sticks make the next landmark."],
                  "Landmarks 1, 4, 16; for example 7 is a stick and 3 dots, 12 is 3 sticks, 16 is one square")],
          misconceptions=["M_BASE_TEN_ONLY", "M_TEN_SYMBOLS_OK"])],
    key_terms=["base", "landmark number", "powers"]))

# ============================== T7 Adding and multiplying with a base ========================================
TOPICS.append(TOPIC(
    "T7", "M2", "Adding and Multiplying with a Base", ["3.3"], "Apply",
    "Students add Egyptian and base-5 numerals by regrouping a full group of a landmark into the next, show that "
    "the product of two landmark numbers in a base is again a landmark, multiply by 10 by moving every symbol up one "
    "landmark, and add on a counting board.",
    "In a base the group size never changes, so adding regroups the same way at every step, and the product of two "
    "landmarks is a landmark. Multiplying by the base moves every symbol up one landmark.",
    [A("T7.C1", "Adding by regrouping tens", "Apply",
       "Students add two Egyptian numerals by counting each symbol and regrouping every 10 strokes into a heel and "
       "every 10 heels into a coil, as in 87 + 78.",
       textbook=["Advantages of a Base-n System",
                 "What is the advantage of having landmark numbers that are all the powers of a number? To understand "
                 "this, let us perform some arithmetic operations using them.",
                 "Let us find the total number of strokes and heels and group them starting from the largest possible "
                 "landmark number. It has a total of 15 heels and 15 strokes.",
                 "Since 10 heels gives the next landmark number, a coil, the sum can be regrouped.",
                 "I see a similarity in the method of adding numbers in the Egyptian and the Hindu system!",
                 "Contrast the addition done in a base-n number system with that done in the Roman system. In the "
                 "Roman system, the grouping and rearranging has to be done carefully as it is not always by the same "
                 "size that each landmark number has to be grouped to get the next one."],
       teach=["Predict first: when you add 87 and 78 in Egyptian numerals, will you need a coil?",
              "Put all the symbols together and count each kind.",
              "Every 10 strokes become 1 heel, every 10 heels become 1 coil: the same rule at every step.",
              "This is exactly the carrying we do when adding in columns; in Roman numerals the group size keeps "
              "changing."],
       examples=[
           WE("Add 8 heels and 7 strokes to 7 heels and 8 strokes in Egyptian numerals.",
              ["Count each kind: heels 8 + 7 = 15, strokes 7 + 8 = 15.",
               "Ten strokes make one heel: 15 strokes become 1 heel and 5 strokes, so there are now 16 heels.",
               "Ten heels make one coil: 16 heels become 1 coil and 6 heels.",
               "The sum is 1 coil, 6 heels and 5 strokes, which is 165. Check: 87 + 78 = 165."],
              "1 coil, 6 heels and 5 strokes, which is 165",
              ncert=["3.3.egypt_add", "3.3.contrast_roman", "3.3.reema_board"])],
       key_terms=["regroup", "carry"], misconceptions=["M_TEN_SYMBOLS_OK", "M_ROMAN_ADD_DIGITS"], minutes=10),
     A("T7.C2", "A landmark times a landmark is a landmark", "Analyze",
       "Students multiply Egyptian landmark numbers by 10 and by 100, find that each product is another landmark, "
       "check the same property in base 5, and explain why it holds in every base.",
       textbook=["How to multiply two numbers in Egyptian numerals? Let us first consider the product of two landmark "
                 "numbers.",
                 "What is any landmark number multiplied by a heel (that is 10)?",
                 "Each landmark number is a power of 10 and so multiplying it with 10 increases the power by 1, which "
                 "is the next landmark number.",
                 "Thus, the product of any two landmark numbers is another landmark number!",
                 "Does this property hold true in the base-5 system that we created? Does this hold for any number "
                 "system with a base?"],
       teach=["Predict first: is 100 × 1000 one Egyptian symbol or many?",
              "Multiplying a landmark by 10 gives the next landmark: 100 × 10 = 1000, a coil becomes a lotus.",
              "Multiplying by 100 moves two landmarks up: 1000 × 100 = 100000, a lotus becomes a tadpole.",
              "Landmarks are powers of the base, and a power times a power is a power, so this holds in every base, "
              "unlike in Roman numerals."],
       examples=[
           WE("Find 100 × 10, 1000 × 100 and 100 × 1000 in Egyptian numerals, and check 25 × 125 in base 5.",
              ["100 × 10 = 1000: a coil times a heel is a lotus.",
               "1000 × 100 = 100000: a lotus times a coil is a tadpole.",
               "100 × 1000 = 100000: a coil times a lotus is also a tadpole.",
               "In base 5, a hexagon times a circle: 25 × 125 = 3125, which is the arrow, another landmark.",
               "In each case the product is a single landmark symbol."],
              "A lotus, a tadpole, a tadpole, and in base 5 an arrow; each product is a landmark",
              ncert=["3.3.land_x10", "3.3.land_x100", "3.3.land_products", "3.3.base5_property_mt"])],
       key_terms=["product", "landmark number"], misconceptions=["M_LANDMARK_PRODUCT"], minutes=8),
     A("T7.C3", "Multiplying any number by 10", "Apply",
       "Students multiply an Egyptian numeral by 10 with the distributive property, moving every symbol up one "
       "landmark, as in 121 × 10, and state the rule for multiplying by the base.",
       textbook=["What can we conclude about the product of a number and a heel (10), in the Egyptian system?",
                 "Will the distributive property hold here? For the same reason that it holds for (a + b) × n, it "
                 "also holds when one of the numbers has more than 2 terms. For example, (a + b + c) × n = an + bn + "
                 "cn.",
                 "What would be a simple rule to multiply a number with a heel?",
                 "When the landmark numbers are powers of a number, then their product is another landmark number. "
                 "This fact simplifies the process of multiplication.",
                 "Thus, a number system whose landmark numbers are powers of a number, i.e., a number system with a "
                 "base, is efficient not only in number representation but also in its utility in carrying out "
                 "arithmetic operations."],
       teach=["Predict first: what happens to each symbol of 121 when the number is multiplied by 10?",
              "Split the number into its symbols and multiply each one by 10: the distributive property.",
              "Each symbol becomes the next landmark: a stroke becomes a heel, a heel a coil, a coil a lotus.",
              "So the rule is: to multiply by 10, move every symbol up one landmark."],
       examples=[
           WE("Multiply 121 (1 coil, 2 heels, 1 stroke) by 10, then use the rule to find 522 × 10.",
              ["121 = 100 + 10 + 10 + 1, so 121 × 10 = (100 + 10 + 10 + 1) × 10.",
               "By the distributive property: 100 × 10 + 10 × 10 + 10 × 10 + 1 × 10 = 1000 + 100 + 100 + 10.",
               "So 121 × 10 = 1210: 1 lotus, 2 coils and 1 heel; every symbol moved up one landmark.",
               "522 is 5 coils, 2 heels and 2 strokes; moving each up gives 5 lotuses, 2 coils and 2 heels, so "
               "522 × 10 = 5220."],
              "121 × 10 is 1210 (1 lotus, 2 coils, 1 heel) and 522 × 10 is 5220",
              ncert=["3.3.distributive_x10", "3.3.now_find", "3.3.x10_rule", "3.3.base_efficiency"])],
       key_terms=["distributive property", "multiply by 10"], misconceptions=["M_LANDMARK_PRODUCT"], minutes=8),
     A("T7.C4", "The counting board", "Apply",
       "Students show a number on a counting board with lines for powers of 10 and a counter above a line for 5, and "
       "add 2907 and 43 by bringing counters together and carrying 10 ones to the tens line.",
       textbook=["Abacus that Makes Use of the Decimal System",
                 "In around the 11th century, even the people still using the Roman numerals started using a "
                 "calculating device, the abacus, constructed using a decimal system.",
                 "Starting from the line that stood for 1, each successive line stood for a successive power of 10.",
                 "The presence of a counter above a line contributed a value of 5.",
                 "For example let us take the number 3426. It can be grouped as 3426 = 1000 + 1000 + 1000 + 100 + 100 "
                 "+ 100 + 100 + 10 + 10 + 1 + 1 + 1 + 1 + 1 + 1.",
                 "Let us consider a simple addition problem: 2907 + 43. The two numbers were taken on either side of "
                 "the vertical partition.",
                 "Hint: In this problem, the 7 ones and the 3 ones together make 10 ones which contributes a counter "
                 "to the line representing 10s."],
       teach=["Predict first: when 7 ones and 3 ones come together on the board, what must happen?",
              "Each line is a power of 10; a counter above a line is worth 5 of that line.",
              "Bring the counters of the two numbers together line by line.",
              "Ten counters on a line become one counter on the next line up, the same carrying as before."],
       examples=[
           WE("Add 2907 and 43 on the counting board.",
              ["2907 has 2 counters on the thousands line, 9 on the hundreds line (one above it for 5 and 4 on it), "
               "none for tens and 7 for ones; 43 has 4 tens and 3 ones.",
               "Bring the ones together: 7 + 3 = 10 ones, which become 1 counter on the tens line.",
               "Tens: 4 + 1 = 5, shown by one counter above the tens line.",
               "Hundreds stay 9 and thousands stay 2, so the board shows 2950."],
              "2950",
              ncert=["3.3.abacus_3426", "3.3.abacus_add"])],
       key_terms=["abacus", "counter"], misconceptions=["M_TEN_SYMBOLS_OK"], minutes=6, thin=True),
     DOER("T7.C5", "Practice: add and multiply in a base", "abacus", "Apply",
          "Students add Egyptian numerals and base-5 numerals by regrouping, and give a rule for multiplying a "
          "base-5 numeral by 5.",
          ["Regroup a full group of any landmark into one of the next landmark.",
           "Multiplying by the base moves every symbol up one landmark."],
          items=[
              FIO("FiOF.q1", "Figure it Out (adding with landmarks, question 1)",
                  "Add the following Egyptian numerals: (i) 9 lotuses, 6 coils and 8 strokes + 5 coils and 7 strokes "
                  "(ii) 1 lotus and 8 heels + 4 heels and 6 strokes",
                  ["(i) Strokes 8 + 7 = 15: 1 heel and 5 strokes. Coils 6 + 5 = 11: 1 lotus and 1 coil.",
                   "Lotuses 9 + 1 = 10: 1 finger. The sum is 1 finger, 1 coil, 1 heel and 5 strokes, which is 10115. "
                   "Check: 9608 + 507 = 10115.",
                   "(ii) Strokes: 6. Heels 8 + 4 = 12: 1 coil and 2 heels.",
                   "The sum is 1 lotus, 1 coil, 2 heels and 6 strokes, which is 1126. Check: 1080 + 46 = 1126."],
                  "(i) 1 finger, 1 coil, 1 heel, 5 strokes, which is 10115 (ii) 1 lotus, 1 coil, 2 heels, 6 strokes, "
                  "which is 1126"),
              FIO("FiOF.q2", "Figure it Out (adding with landmarks, question 2)",
                  "Add the following numerals that are in the base-5 system that we created: (1 circle, 2 hexagons, "
                  "1 square, 2 triangles) + (3 circles, 1 hexagon, 2 squares, 2 triangles). Remember that in this "
                  "system, 5 times a landmark number gives the next one!",
                  ["Count each kind: circles 1 + 3 = 4, hexagons 2 + 1 = 3, squares 1 + 2 = 3, triangles 2 + 2 = 4.",
                   "No kind reaches 5, so nothing needs to be regrouped.",
                   "The sum is 4 circles, 3 hexagons, 3 squares and 4 triangles.",
                   "Check in our numerals: 182 + 412 = 594, and 500 + 75 + 15 + 4 = 594."],
                  "4 circles, 3 hexagons, 3 squares and 4 triangles, which is 594"),
              FIO("FiOG.q3", "Figure it Out (bases and their limits, question 3)",
                  "Give a simple rule to multiply a given number by 5 in the base-5 system that we created.",
                  ["Each landmark times 5 is the next landmark: 1 × 5 = 5, 5 × 5 = 25, 25 × 5 = 125.",
                   "By the distributive property, multiply every symbol of the number by 5.",
                   "So every triangle becomes a square, every square a hexagon, every hexagon a circle, and so on.",
                   "Rule: replace each symbol by the symbol of the next landmark."],
                  "Replace every symbol by the symbol of the next landmark")],
          misconceptions=["M_TEN_SYMBOLS_OK", "M_LANDMARK_PRODUCT"])],
    key_terms=["regroup", "landmark product", "base"]))
