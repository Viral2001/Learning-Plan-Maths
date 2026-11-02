# -*- coding: utf-8 -*-
"""Topics T9 to T11 (module M3: cubic numbers and cube roots) and T12 (M4: summary, history and the Square Pairs
puzzle). Book pp 11 to 18."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T9 Cubes from unit cubes ====================================================
TOPICS.append(TOPIC(
    "T9", "M3", "Cubes: Building with Unit Cubes", ["1.2"], "Analyze",
    "Students count the unit cubes in a cube of given edge, write cubes with the n cubed notation, find the digits "
    "cubes can end in and how many cubes have one, two or three digits, and cube fractions, decimals and negative "
    "numbers.",
    "A cube of edge n holds n layers of n × n unit cubes, so n³ of them. Cubes can end in any digit, but end zeros "
    "come in threes, and the cube of a negative number is negative.",
    [A("T9.C1", "How many unit cubes make a cube", "Understand",
       "Students count the unit cubes that make cubes of edge 2, 3 and 4 as layers of squares, write the count with "
       "the n cubed notation, and decide whether numbers between cubes can be cubes.",
       textbook=["1.2 Cubic Numbers",
                 "How many cubes of side 1 cm make a cube of side 2 cm? 8.",
                 "How many cubes of side 1 cm will make a cube of side 3 cm? 27.",
                 "Numbers like 1, 8, 27 are called perfect cubes or cubic numbers. Is 9 a cube? No. In fact no number "
                 "from 10 to 26 is a cube.",
                 "Estimate the number of unit cubes in a cube with an edge of 4 units. There are 4 layers of 16 cubes, "
                 "so 64.",
                 "A cube of edge 5 units has 5 × 5 × 5 = 125 unit cubes. We write n × n × n = n³, read as n cubed."],
       teach=["Predict first: how many 1 cm cubes build a cube of edge 4 cm? Is it 12, 16 or 64?",
              "Build it in layers. The bottom layer is a 4 by 4 square, 16 cubes, and there are 4 layers: 64.",
              "So the count is 4 × 4 × 4 = 4³ = 64. Cubing is not multiplying by 3.",
              "2³ = 8 and 3³ = 27, and no number from 9 to 26 can be made into a solid cube."],
       examples=[
           WE("How many unit cubes make cubes of edge 2, 3 and 4 units?",
              ["Edge 2: 2 layers of 2 × 2 = 4 cubes, so 2³ = 8.",
               "Edge 3: 3 layers of 3 × 3 = 9 cubes, so 3³ = 27.",
               "Edge 4: 4 layers of 4 × 4 = 16 cubes, so 4³ = 64."],
              "8, 27 and 64 unit cubes", ncert=["1.2.cube_2", "1.2.cube_3", "1.2.cube_9", "1.2.cube_4"])],
       key_terms=["cube", "perfect cube", "n cubed"], misconceptions=["M_CUBE_TRIPLE"], minutes=8),
     A("T9.C2", "The last digits and the length of cubes", "Analyze",
       "Students use the table of cubes up to 20 to find that cubes can end in any digit, count the cubes with one, "
       "two and three digits, and explain why a cube cannot end in exactly two zeros.",
       textbook=["Complete the table of cubes from 1 to 20. What patterns do you notice in the table?",
                 "We know that the last digit of a square is 0, 1, 4, 5, 6 or 9. What are the possible last digits of "
                 "cubes?",
                 "How many cubes are there with 1 digit, 2 digits and 3 digits?",
                 "Can a cube end with exactly two zeros (00)? Explain."],
       teach=["Predict first: can a cube end in 7, which no square can?",
              "From the table, 1³ = 1, 2³ = 8, 3³ = 27, 7³ = 343: every digit 0 to 9 appears as a last digit.",
              "1 digit: 1 and 8. 2 digits: 27 and 64. 3 digits: 125, 216, 343, 512 and 729.",
              "Each zero at the end of the number gives three zeros at the end of its cube, so a cube ends in 0, 3, "
              "6, ... zeros, never exactly two."],
       examples=[
           WE("How many cubes have exactly 3 digits, and can a cube end in exactly two zeros?",
              ["4³ = 64 has 2 digits and 5³ = 125 has 3 digits.",
               "9³ = 729 has 3 digits and 10³ = 1000 has 4 digits.",
               "So the 3 digit cubes are 5³ to 9³: 125, 216, 343, 512 and 729, five cubes.",
               "10³ = 1000 ends in three zeros; each end zero of the number gives three in the cube, so exactly two "
               "zeros is impossible."],
              "Five 3 digit cubes; no cube ends in exactly two zeros",
              ncert=["1.2.cube_count_digits", "1.2.cube_00", "1.2.cube_table", "1.2.mt_cube_patterns",
                     "1.2.cube_digits"])],
       key_terms=["perfect cube", "units digit"], misconceptions=["M_CUBE_DIGITS", "M_CUBE_ZEROS"], minutes=10),
     A("T9.C3", "Cubes of fractions, decimals and negative numbers", "Apply",
       "Students cube fractions, decimals and negative numbers and explain why the cube of a negative number is "
       "negative while its square is positive.",
       textbook=["We can also find cubes of fractions, decimals and negative numbers: (4/6)³ = 64/216, "
                 "13.08³ = 2237.810112, (−6)³ = −216."],
       teach=["Predict first: is (−6)³ positive or negative?",
              "(−6)³ = −6 × −6 × −6. The first two give 36, and 36 × −6 = −216: negative.",
              "Compare (−6)² = 36, positive. An odd number of negative factors leaves the result negative.",
              "Fractions cube top and bottom: (4/6)³ = 64/216."],
       examples=[
           WE("Find (−6)³, (−6)² and (4/6)³.",
              ["(−6)³ = −6 × −6 × −6 = 36 × −6 = −216.",
               "(−6)² = −6 × −6 = 36.",
               "(4/6)³ = 64/216, cubing the top and the bottom."],
              "(−6)³ = −216, (−6)² = 36 and (4/6)³ = 64/216", ncert=["1.2.cube_other"])],
       key_terms=["cube", "negative number"], misconceptions=["M_CUBE_TRIPLE"], minutes=6),
     DOER("T9.C4", "Practice: stack the cubes", "cube_stacker", "Analyze",
          "Students stack layers of unit cubes to build cubes of growing edge, read the count as the cube, and test "
          "statements about cubes against the stacks.",
          ["A cube of edge n holds n layers of n² unit cubes, n³ in all.",
           "Cubes can end in any digit; their end zeros come in threes.",
           "The cube of an odd number is odd and the cube of a negative number is negative."],
          items=[
              FIO("FiO2.q3", "Figure it Out (cubic numbers, question 3)",
                  "State true or false. Explain your reasoning. (i) The cube of any odd number is even. (ii) There is "
                  "no perfect cube that ends with 8. (iii) The cube of a 2 digit number may be a 3 digit number. "
                  "(iv) The cube of a 2 digit number may have seven or more digits. (v) Cube numbers have an odd "
                  "number of factors.",
                  ["(i) False: odd × odd × odd is odd, for example 3³ = 27.",
                   "(ii) False: 2³ = 8 and 12³ = 1728 end in 8.",
                   "(iii) False: the smallest 2 digit number is 10, and 10³ = 1000 already has 4 digits.",
                   "(iv) False: the largest 2 digit number is 99, and 99³ = 970299 has only 6 digits.",
                   "(v) False: 8 = 2³ has the 4 factors 1, 2, 4 and 8."],
                  "All five statements are false")])],
    key_terms=["cube", "perfect cube"]))

# ============================== T10 Taxicab numbers, odd sums, differences ==================================
TOPICS.append(TOPIC(
    "T10", "M3", "Taxicab Numbers and Cube Patterns", ["1.2"], "Analyze",
    "Students check that some numbers are sums of two cubes in two different ways, find cubes as sums of "
    "consecutive odd numbers, and use successive differences to tell squares and cubes apart.",
    "1729 is the smallest number that is a sum of two cubes in two ways. The nth cube is the sum of n consecutive odd "
    "numbers, and successive differences of cubes become constant at the third level, of squares at the second.",
    [A("T10.C1", "Taxicab numbers", "Apply",
       "Students verify that 1729, 4104 and 13832 can each be written as a sum of two cubes in two different ways.",
       textbook=["Hardy came to see Ramanujan in a taxi numbered 1729 and remarked that the number seemed rather dull. "
                 "Ramanujan replied that it is a very interesting number: it is the smallest number expressible as a "
                 "sum of two cubes in two different ways.",
                 "1729 = 1³ + 12³ = 9³ + 10³.",
                 "Numbers like this are called taxicab numbers. Try this: 4104 = 2³ + 16³ = 9³ + 15³ and "
                 "13832 = 2³ + 24³ = 18³ + 20³.",
                 "Littlewood said that every positive integer was one of Ramanujan's personal friends."],
       teach=["Predict first: can 1729 be split into two cubes? Try 12³ first.",
              "12³ = 1728, and 1729 − 1728 = 1 = 1³. So 1729 = 1³ + 12³.",
              "Now 10³ = 1000 and 1729 − 1000 = 729 = 9³. A second way: 1729 = 9³ + 10³.",
              "1729 is the smallest number with two such ways; 4104 and 13832 are the next taxicab numbers."],
       examples=[
           WE("Show that 4104 is a sum of two cubes in two different ways.",
              ["16³ = 4096 and 4104 − 4096 = 8 = 2³, so 4104 = 2³ + 16³.",
               "15³ = 3375 and 4104 − 3375 = 729 = 9³, so 4104 = 9³ + 15³.",
               "So 4104 = 2³ + 16³ = 9³ + 15³."],
              "4104 = 2³ + 16³ = 9³ + 15³", ncert=["1.2.taxicab", "1.2.try_taxicab"])],
       key_terms=["taxicab number", "sum of cubes"], minutes=8),
     A("T10.C2", "Cubes from consecutive odd numbers", "Analyze",
       "Students group the odd numbers into blocks of 1, 2, 3, ... numbers, find that each block adds to a cube, and "
       "use the pattern to add a block of ten odd numbers without adding term by term.",
       textbook=["Perfect Cubes and Consecutive Odd Numbers",
                 "1 = 1 = 1³, 3 + 5 = 8 = 2³, 7 + 9 + 11 = 27 = 3³, 13 + 15 + 17 + 19 = 64 = 4³, "
                 "21 + 23 + 25 + 27 + 29 = 125 = 5³, 31 + 33 + 35 + 37 + 39 + 41 = 216 = 6³.",
                 "Using this pattern, find the value of 91 + 93 + 95 + ... + 109 without calculating."],
       teach=["Predict first: what is 7 + 9 + 11? Is it a square or a cube?",
              "Group the odd numbers: 1, then 3 + 5, then 7 + 9 + 11. The sums are 1, 8, 27: the cubes.",
              "The nth block has n consecutive odd numbers and adds to n³.",
              "91 to 109 is a block of 10 odd numbers, so it is the 10th block and adds to 10³ = 1000."],
       examples=[
           WE("Find 91 + 93 + 95 + 97 + 99 + 101 + 103 + 105 + 107 + 109 using the cube pattern.",
              ["The blocks of consecutive odd numbers add to 1³, 2³, 3³, and so on.",
               "The 9th block ends at 89, so the 10th block runs from 91 to 109: ten odd numbers.",
               "The 10th block adds to 10³ = 1000.",
               "Check: the numbers pair from the outside to 200 each, 5 pairs, 5 × 200 = 1000."],
              "1000", ncert=["1.2.odd_cubes", "1.2.odd_91"])],
       key_terms=["consecutive odd numbers", "perfect cube"], misconceptions=["M_CUBE_TRIPLE"], minutes=8),
     A("T10.C3", "Successive differences of squares and cubes", "Analyze",
       "Students take differences of consecutive squares and of consecutive cubes level by level until they become "
       "constant, and compare the level at which each becomes constant.",
       textbook=["Successive differences: for the squares 1, 4, 9, 16, 25, ... the first differences are 3, 5, 7, 9, "
                 "... and the second differences are all 2.",
                 "Compute the successive differences at levels 1, 2, 3 for cube numbers until you see a pattern."],
       teach=["Predict first: for cubes, after how many levels of differences do you get a constant?",
              "Cubes 1, 8, 27, 64, 125, 216: first differences 7, 19, 37, 61, 91.",
              "Second differences 12, 18, 24, 30; third differences 6, 6, 6.",
              "Squares become constant at level 2, cubes at level 3."],
       examples=[
           WE("Find the successive differences of the cubes 1, 8, 27, 64, 125 and 216 until they are constant.",
              ["Level 1: 8 − 1 = 7, 27 − 8 = 19, 64 − 27 = 37, 125 − 64 = 61, 216 − 125 = 91.",
               "Level 2: 19 − 7 = 12, 37 − 19 = 18, 61 − 37 = 24, 91 − 61 = 30.",
               "Level 3: 18 − 12 = 6, 24 − 18 = 6, 30 − 24 = 6.",
               "The differences are constant, 6, at level 3."],
              "Constant difference 6 at level 3", ncert=["1.2.diff_squares", "1.2.diff_cubes"])],
       key_terms=["successive differences"], minutes=8),
     DOER("T10.C4", "Practice: compare differences of cubes and squares", "difference_ladder", "Analyze",
          "Students use the difference patterns of squares and cubes to compare differences of consecutive powers "
          "without computing every power.",
          ["Consecutive squares differ by odd numbers that grow by 2.",
           "Consecutive cubes differ by numbers that grow much faster: 7, 19, 37, 61, 91, ...",
           "The nth cube is the sum of the nth block of n consecutive odd numbers."],
          items=[
              FIO("FiO2.q5", "Figure it Out (cubic numbers, question 5)",
                  "Which of the following is the greatest? Explain your reasoning. (i) 67³ − 66³ (ii) 43³ − 42³ "
                  "(iii) 67² − 66² (iv) 43² − 42²",
                  ["Differences of consecutive cubes grow quickly, and they are far bigger than differences of "
                   "consecutive squares.",
                   "67² − 66² = 67 + 66 = 133 and 43² − 42² = 43 + 42 = 85.",
                   "43³ − 42³ = 79507 − 74088 = 5419.",
                   "67³ − 66³ = 300763 − 287496 = 13267, the greatest."],
                  "(i) 67³ − 66³ is the greatest")])],
    key_terms=["taxicab number", "successive differences"]))

# ============================== T11 Cube roots ==============================================================
TOPICS.append(TOPIC(
    "T11", "M3", "Cube Roots by Grouping in Threes", ["1.2"], "Analyze",
    "Students find cube roots as the reverse of cubing, decide whether a number is a perfect cube by grouping its "
    "prime factors into three identical groups, and find the smallest multiplier that makes a perfect cube.",
    "A number is a perfect cube exactly when its prime factors split into three identical groups, so every prime "
    "appears a multiple of three times. One group multiplied out is the cube root.",
    [A("T11.C1", "Three equal groups of prime factors", "Analyze",
       "Students find the cube root of a number by splitting its prime factors into three identical groups, and "
       "decide that a number is not a perfect cube when they cannot.",
       textbook=["Cube Roots",
                 "The cube root of 8 is 2, the cube root of 27 is 3, and the cube root of 1000 is 10. The cube root of "
                 "n³ is n. The symbol for the cube root is a root sign with a small 3.",
                 "Check if 3375 is a perfect cube. 3375 = 3 × 3 × 3 × 5 × 5 × 5 = (3 × 5) × (3 × 5) × (3 × 5), so "
                 "3375 = 15³ and its cube root is 15.",
                 "Is 500 a perfect cube? 500 = 2 × 2 × 5 × 5 × 5. The 2s cannot be put into three equal groups, so "
                 "500 is not a perfect cube."],
       teach=["Predict first: is 3375 a perfect cube? Its last digit is 5, so its root would end in 5.",
              "Factorise: 3375 = 3 × 3 × 3 × 5 × 5 × 5. Each prime appears three times.",
              "Split into three equal groups, 3 × 5 in each: 3375 = 15 × 15 × 15, so the cube root is 15.",
              "500 = 2 × 2 × 5 × 5 × 5: only two 2s, so 500 is not a perfect cube."],
       examples=[
           WE("Decide whether 3375 and 500 are perfect cubes, and give the cube root of the one that is.",
              ["3375 = 3 × 3 × 3 × 5 × 5 × 5.",
               "Three equal groups of 3 × 5 = 15, so 3375 = 15 × 15 × 15 = 15³.",
               "500 = 2 × 2 × 5 × 5 × 5; two 2s cannot make three equal groups.",
               "So 3375 is a perfect cube with cube root 15, and 500 is not a perfect cube."],
              "3375 = 15³, cube root 15; 500 is not a perfect cube",
              ncert=["1.2.root_def", "1.2.root_3375", "1.2.root_500"])],
       key_terms=["cube root", "prime factorisation"], misconceptions=["M_CUBE_TRIPLE"], minutes=10),
     A("T11.C1x", "Cube roots of 64, 512 and 729", "Apply",
       "Students find the cube roots of 64, 512 and 729 by grouping prime factors in threes, using the table of cube "
       "factorisations.",
       teach=["Predict first: is the cube root of 512 bigger or smaller than 10?",
              "Group the prime factors into three equal groups and multiply one group."],
       examples=[
           WE("Find the cube roots of 64, 512 and 729.",
              ["64 = 2 × 2 × 2 × 2 × 2 × 2 = (2 × 2) × (2 × 2) × (2 × 2), so its cube root is 4.",
               "512 = 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 = 8 × 8 × 8, so its cube root is 8.",
               "729 = 3 × 3 × 3 × 3 × 3 × 3 = 9 × 9 × 9, so its cube root is 9."],
              "The cube roots are 4, 8 and 9", ncert=["1.2.root_find"])],
       key_terms=["cube root"], misconceptions=["M_CUBE_TRIPLE"], minutes=6, thin=True),
     DOER("T11.C2", "Practice: group the primes in threes", "cube_root_tripler", "Analyze",
          "Students sort prime factors into three identical groups to find cube roots, and find the smallest "
          "multiplier that completes the groups to make a perfect cube.",
          ["A perfect cube has every prime factor appearing a multiple of three times.",
           "One of the three equal groups, multiplied out, is the cube root.",
           "Multiplying by the missing primes completes the groups."],
          items=[
              FIO("FiO2.q1", "Figure it Out (cubic numbers, question 1)",
                  "Find the cube roots of 27000 and 10648.",
                  ["27000 = 27 × 1000 = 3 × 3 × 3 × 2 × 2 × 2 × 5 × 5 × 5.",
                   "Three equal groups of 3 × 2 × 5 = 30, so the cube root of 27000 is 30.",
                   "10648 = 2 × 2 × 2 × 11 × 11 × 11.",
                   "Three equal groups of 2 × 11 = 22, so the cube root of 10648 is 22."],
                  "30 and 22"),
              FIO("FiO2.q2", "Figure it Out (cubic numbers, question 2)",
                  "What number will you multiply by 1323 to make it a cube number?",
                  ["1323 = 3 × 3 × 3 × 7 × 7.",
                   "The 3s make a full group of three; the 7s need one more 7.",
                   "1323 × 7 = 9261 = 3 × 3 × 3 × 7 × 7 × 7 = 21³."],
                  "Multiply by 7, giving 9261 = 21³"),
              FIO("FiO2.q4", "Figure it Out (cubic numbers, question 4)",
                  "Guess the cube roots of the following numbers: (i) 1331 (ii) 4913 (iii) 12167 (iv) 32768",
                  ["1331 ends in 1 and lies between 10³ = 1000 and 20³ = 8000; 11³ = 1331.",
                   "4913 ends in 3, and only 7³ ends in 3 among 1 to 9, so try 17: 17³ = 4913.",
                   "12167 lies between 20³ = 8000 and 30³ = 27000 and ends in 7, so try 23: 23³ = 12167.",
                   "32768 lies between 30³ = 27000 and 40³ = 64000 and ends in 8, so try 32: 32³ = 32768."],
                  "(i) 11 (ii) 17 (iii) 23 (iv) 32")])],
    key_terms=["cube root", "prime factorisation"]))

# ============================== T12 Summary, history and Square Pairs =======================================
TOPICS.append(TOPIC(
    "T12", "M4", "Summary: A Square and A Cube", ["1.3", "Summary", "Puzzle Time"], "Remember",
    None,
    "Squares and cubes as areas and volumes, their digits and patterns, square roots and cube roots by several "
    "methods, the history of the words, and a puzzle of square sums.",
    [A("T12.C1", "What we found about squares and cubes", "Remember",
       "Students restate how squares and cubes are formed, the patterns and digit facts they follow, and the methods "
       "for finding square roots and cube roots.",
       textbook=["A number obtained by multiplying a number by itself is called a square number.",
                 "Squares of natural numbers are called perfect squares. All perfect squares end in 0, 1, 4, 5, 6 or 9.",
                 "Square numbers can be written as the sum of consecutive odd numbers starting with 1.",
                 "Finding the square root is the inverse operation of squaring.",
                 "A number obtained by multiplying a number by itself three times is called a cube number.",
                 "Cube numbers can be written as the sum of consecutive odd numbers.",
                 "Finding the cube root is the inverse operation of cubing; prime factorisation helps find square "
                 "roots and cube roots."],
       teach=["Our opening puzzle is settled: the lockers left open are the squares 1, 4, 9, up to 100, because only "
              "squares have an odd number of factors.",
              "Squares are areas, end only in 0, 1, 4, 5, 6 or 9, and are sums of the first odd numbers; cubes are "
              "volumes and are sums of blocks of consecutive odd numbers.",
              "Roots undo powers: list, subtract odd numbers, pair or triple the prime factors, or trap the root between "
              "two whole numbers. Still open for you: which taxicab number comes after 13832?"],
       ncert=["summary"], video_focus=["RECAP"], minutes=8),
     A("T12.C2", "A pinch of history: varga, ghana and mula", "Understand",
       "Students describe how squares and cubes were known to ancient mathematicians and where the words square, "
       "cube and root come from.",
       textbook=["1.3 A Pinch of History",
                 "Clay tablets from Babylon, from around 1700 BCE, list squares and cubes of numbers.",
                 "In India the square was called varga and the cube ghana, and the fourth power varga-varga. "
                 "Aryabhata, in 499 CE, explained varga as the area of a square figure and ghana as the volume of a "
                 "cube with equal sides.",
                 "The word mula, meaning the root of a plant, was used for the root of a number: varga-mula for the "
                 "square root and ghana-mula for the cube root. Brahmagupta, in 628 CE, also used pada for the square "
                 "root.",
                 "The word passed into Arabic as jidhr and into Latin as radix, the root of a plant, which is where "
                 "our word root comes from."],
       teach=["Predict first: why might people have called a square root a root, like the root of a plant?",
              "Babylonian tablets of about 1700 BCE already listed squares and cubes.",
              "Indian mathematicians named the square varga and the cube ghana, and Aryabhata tied them to the area "
              "of a square and the volume of a cube.",
              "The root, mula, grows into the square or cube: varga-mula and ghana-mula became jidhr, then radix, "
              "then root."],
       examples=[
           WE("Name the Indian words for the square, the cube, the square root and the cube root, and explain what the "
              "word root means.",
              ["The square was varga and the cube was ghana.",
               "Mula means the root of a plant, so the square root was varga-mula and the cube root ghana-mula.",
               "The idea is that the number grows from its root, just as a plant grows from its root.",
               "The word travelled through Arabic jidhr and Latin radix to our word root."],
              "Varga, ghana, varga-mula and ghana-mula; root means what the square or cube grows from",
              ncert=["history"])],
       key_terms=["varga", "ghana", "mula"], enrichment=True, minutes=5),
     A("T12.C3", "Square Pairs", "Apply",
       "Students arrange numbers in a row so that every pair of neighbours adds to a perfect square, reasoning about "
       "which numbers have only one possible neighbour.",
       textbook=["Puzzle Time: Square Pairs!",
                 "In the row 3, 6, 10, 15, 1, each pair of neighbours adds up to a perfect square: 3 + 6 = 9, "
                 "6 + 10 = 16, 10 + 15 = 25, 15 + 1 = 16.",
                 "Arrange the numbers 1 to 17, without repeating, in a row so that each pair of neighbours adds up to "
                 "a perfect square.",
                 "Can you arrange the numbers 1 to 32 in a circle so that each pair of neighbours adds up to a perfect "
                 "square?"],
       teach=["Predict first: which numbers from 1 to 17 can sit next to 16?",
              "Neighbour sums can only be 4, 9, 16 or 25. 16 pairs only with 9 to make 25, and 17 only with 8.",
              "A number with only one possible neighbour must sit at an end, so 16 and 17 are the two ends.",
              "Build inwards from both ends, checking each sum."],
       examples=[
           WE("Arrange 1 to 17 in a row so that each pair of neighbours adds to a perfect square.",
              ["16 can only sit next to 9, and 17 only next to 8, so they go at the two ends.",
               "Start 16, 9, 7, 2, 14, 11, 5, 4, 12, 13, 3, 6, 10, 15, 1, 8, 17.",
               "Check the sums: 25, 16, 9, 16, 25, 16, 9, 16, 25, 16, 9, 16, 25, 16, 9, 25, all squares."],
              "16, 9, 7, 2, 14, 11, 5, 4, 12, 13, 3, 6, 10, 15, 1, 8, 17", ncert=["puzzle"])],
       key_terms=["perfect square"], enrichment=True, minutes=6)],
    topic_type="summary"))
