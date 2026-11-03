# A Square and A Cube  (cbse_eng_maths8_ch1, live v43)

Book text: `textbooks/extracted/hegp101.txt`

Topics in order. `C` lines are concepts; `b<i>` lines are content blocks (kind, item_kind, refs, steps, question). A concept topic is followed by its existing Questions topic (if any).

## M1.S1.T1  The Queen's Locker Puzzle  [FRAMING]
C M1.S1.T1.C1  'A hundred lockers and a hidden treasure'  [enrichment]  media=['IMG1', 'VID1']  refs=['opening']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Queen Ratnamanjuri of Khoisnam left a will. Her treasure was kept in one of the 100 lockers in her palace, all closed and locked. 100 people were called one after another
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: after all 100 people have passed, do you think most lockers end open, most end closed, or only a few end open? 2. Try a small case by hand: 10 lockers a

## M1.S2.T2  Which Lockers Stay Open?  [CONCEPT TOPIC]
C M1.S2.T2.C2  'Each toggle is a factor'  [obj O1]  media=['IMG1', 'VID1']  refs=['1.0.factors', '1.0.even_factors']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Locker 6 is toggled by person 1, person 2, person 3 and person 6. These are exactly the factors of 6. Each factor of 6 has a partner factor: 1 × 6 and 2 × 3. Does every n
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: who toggles locker 12? Write the list before you check. 2. Person k toggles locker 12 exactly when k divides 12, so the toggles are 1, 2, 3, 4, 6, 12: t
   b2 worked_example/None refs=['1.0.factors', '1.0.even_factors'] steps=4 video=VID1  Q: How many times is locker 12 toggled, and does it end open or closed?
C M1.S2.T2.C3  'Squares have an odd number of factors'  [obj O2]  media=['IMG1', 'VID1']  refs=['1.0.odd_insight', '1.0.square_def']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Can you use this insight to find more numbers with an odd number of factors? For 36: 1 × 36, 2 × 18, 3 × 12, 4 × 9 and 6 × 6. The factor 6 is paired with itself. Numbers 
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: does 36 have an odd or an even number of factors? 2. List the pairs: 1 × 36, 2 × 18, 3 × 12, 4 × 9, 6 × 6. The last pair uses 6 twice. 3. So 36 has 9 fa
   b2 worked_example/None refs=['1.0.odd_insight', '1.0.square_def'] steps=3 video=VID1  Q: Count the factors of 36 and say why the count is odd.
C M1.S2.T2.C4  'The open lockers are the squares'  [obj O3]  media=['IMG1', 'VID1']  refs=['1.0.open_lockers']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Write the locker numbers that remain open.
   b1 teaching_plan/None refs=[] steps=3 video=-  Q: 1. Predict first: which lockers between 1 and 30 stay open? 2. Open lockers are those toggled an odd number of times, so they are the square numbers. 3. Up to 100: 1, 4, 
   b2 worked_example/None refs=['1.0.open_lockers'] steps=3 video=VID1  Q: Which lockers remain open after all 100 people pass?
C M1.S2.T2.C5  'Practice: solve the locker puzzle'  [obj O4]  media=['IMG1', 'VID1', '2D1']  refs=['1.0.five_lockers']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: The queen's will also had a clue: the first five lockers that were touched exactly twice hold the code. Which are these five lockers? A locker touched exactly twice has e
   b1 recap/None refs=[] steps=0 video=-  Q: Each person who touches a locker is a factor of its number. Factors pair up, except a number times itself, so only square numbers have an odd number of factors. A locker 
   b2 exercise/None refs=[] steps=4 video=VID1  Q: The first five lockers that were touched exactly twice hold the code to the treasure. Which are these five lockers?

## M2.S3.T3  Squares as Areas, Digits and Zeros  [CONCEPT TOPIC]
C M2.S3.T3.C6  'A square number is an area'  [obj O5]  media=['IMG1', 'VID1']  refs=['1.1.area_table', '1.1.notation', '1.1.perfect_def']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: 1.1 Square Numbers The area of a square of side 1 unit is 1 sq unit, of side 2 units is 4 sq units, of side 3 units is 9 sq units. For sides 4, 5 and 10 the areas are 16,
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: a square has side 6 units. Is its area 12 square units or 36 square units? 2. Area is side times side: 6 × 6 = 36, written 6², read 6 squared. Squaring 
   b2 worked_example/None refs=['1.1.area_table', '1.1.notation', '1.1.perfect_def'] steps=4 video=VID1  Q: Find the areas of squares with sides 6 units, 3/5 unit and 2.5 units.
C M2.S3.T3.C7  'The last digit of a square'  [obj O6]  media=['IMG1', 'VID1']  refs=['1.1.which6', '1.1.ends6', '1.1.table30', '1.1.mt_patterns']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Fill in the table of squares from 1 to 30. What patterns do you notice? The squares end only in 0, 1, 4, 5, 6 or 9. If a number ends in 0, 1, 4, 5, 6 or 9, is it always a
   b1 teaching_plan/None refs=[] steps=5 video=-  Q: 1. Predict first: can a perfect square end in 7? 2. Only the last digit of a number decides the last digit of its square. Squaring 0 to 9 gives last digits 0, 1, 4, 9, 6,
   b2 worked_example/None refs=['1.1.which6', '1.1.ends6', '1.1.table30', '1.1.mt_patterns'] steps=4 video=VID1  Q: Which of 38², 34², 46², 56², 74² and 82² end in 6?
C M2.S3.T3.C8  'Squares that end in 1, and numbers that cannot be squares'  [thin-extra, obj O7]  media=['IMG1', 'VID1']  refs=['1.1.ends1', '1.1.five_nonsquares', '1.1.mt_always', '1.1.more_patterns']
   b0 teaching_plan/None refs=[] steps=3 video=-  Q: 1. Predict first: what are the next two squares ending in 1 after 29²? 2. Numbers ending in 1 or 9 have squares ending in 1, so the next are 31² and 39². 3. Numbers endin
   b1 worked_example/None refs=['1.1.ends1', '1.1.five_nonsquares', '1.1.mt_always', '1.1.more_patterns'] steps=3 video=VID1  Q: Write the next two squares ending in 1 after 29², and five numbers that cannot be squares.
C M2.S3.T3.C9  'Zeros at the end and odd or even'  [obj O8]  media=['IMG1', 'VID1']  refs=['1.1.zeros', '1.1.parity']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: 10² = 100, 20² = 400, 100² = 10000. If a number ends in 3 zeros, how many zeros will its square have at the end? Notice the number of zeros at the end of a number and its
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: 3000 ends in 3 zeros. How many zeros end 3000²? 2. 3000² = 3000 × 3000. Each factor brings 3 zeros, so the square ends in 6 zeros: 9000000. 3. The zeros
   b2 worked_example/None refs=['1.1.zeros', '1.1.parity'] steps=3 video=VID1  Q: How many zeros end 3000², and is 3000² odd or even?
C M2.S3.T3.C10  'Practice: build squares and read their digits'  [obj O9]  media=['IMG1', 'VID1', '2D1']  refs=['FiO1.q2']
   b0 recap/None refs=[] steps=0 video=-  Q: A square of side n holds n² unit tiles; squaring is not doubling. Squares end only in 0, 1, 4, 5, 6 or 9, and that ending alone never proves a number is a square. A squar
   b1 exercise/None refs=[] steps=4 video=VID1  Q: Which of the following numbers have the digit 4 in the units place? (i) 64² (ii) 108² (iii) 292² (iv) 36²

## M2.S4.T4  Squares from Odd Numbers  [CONCEPT TOPIC]
C M2.S4.T4.C11  'Odd numbers build squares'  [obj O10]  media=['IMG1', 'VID1']  refs=['1.1.odd_diffs', '1.1.odd_sum']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Perfect Squares and Odd Numbers Look at the differences between consecutive squares: 4 − 1 = 3, 9 − 4 = 5, 16 − 9 = 7, 25 − 16 = 9. See if this pattern continues. 1 + 3 +
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: what is 1 + 3 + 5 + 7 + 9 + 11? Guess before you add. 2. Draw a 1 by 1 square of dots, then wrap an inverted L of 3 dots to make 2 by 2, then 5 dots to 
   b2 worked_example/None refs=['1.1.odd_diffs', '1.1.odd_sum'] steps=4 video=VID1  Q: Find 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 without adding term by term.
C M2.S4.T4.C12  'Subtract odd numbers to test a square'  [obj O11]  media=['IMG1', 'VID1']  refs=['1.1.subtract_test']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Is 25 a perfect square? 25 − 1 = 24, 24 − 3 = 21, 21 − 5 = 16, 16 − 7 = 9, 9 − 9 = 0. We reached 0 after subtracting 5 odd numbers, so 25 = 5². Is 38 a perfect square? 38
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: is 38 a perfect square? 2. Subtract the odd numbers in order. If you land exactly on 0, the number is the sum of the first few odd numbers, so it is a s
   b2 worked_example/None refs=['1.1.subtract_test'] steps=4 video=VID1  Q: Use successive subtraction of odd numbers to decide whether 38 is a perfect square.
C M2.S4.T4.C13  'From one square to the next'  [obj O12]  media=['IMG1', 'VID1']  refs=['1.1.next_square', '1.1.nth_odd']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Using the pattern, find 36² given that 35² = 1225. How do we find the 36th odd number? What is the nth odd number? The nth odd number is 2n − 1. The 36th odd number is 71
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: if 35² = 1225, is 36² closer to 1260 or to 1300? 2. 36² is 35² plus the 36th odd number, because the first 36 odd numbers add to 36². 3. The odd numbers
   b2 worked_example/None refs=['1.1.next_square', '1.1.nth_odd'] steps=4 video=VID1  Q: Given 35² = 1225, find 36² without multiplying.
C M2.S4.T4.C14  'Practice: squares from odd numbers'  [obj O13]  media=['IMG1', 'VID1', '2D1']  refs=['FiO1.q3']
   b0 recap/None refs=[] steps=0 video=-  Q: The first n odd numbers add to n². Subtracting 1, 3, 5, ... reaches exactly 0 only for a perfect square. (n + 1)² is n² plus the (n + 1)th odd number, which is 2n + 1.
   b1 exercise/None refs=[] steps=4 video=VID1  Q: Given that 125² = 15625, what is the value of 126²? (i) 15625 + 126 (ii) 15625 + 26² (iii) 15625 + 253 (iv) 15625 + 251 (v) 15625 + 512

## M2.S5.T5  Questions: Squares from Odd Numbers  [QUESTIONS TOPIC (follows M2.S4.T4)]
C M2.S5.T5.C15  'Square Numbers, Q8'  [obj O14]  media=['VID1']  refs=['FiO1.q8']
   b0 exercise/figure_it_out refs=[] steps=4 video=VID1  Q: Look at the pattern 1² + 2² + 2² = 3², 2² + 3² + 6² = 7², 3² + 4² + 12² = 13². Fill in 4² + 5² + 20² = (___)² and 9² + 10² + (___)² = (___)².

## M2.S6.T6  Gaps Between Squares and Triangular Numbers  [CONCEPT TOPIC]
C M2.S6.T6.C16  'How many numbers lie between two squares'  [obj O15]  media=['IMG1', 'VID1']  refs=['1.1.between']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Find how many numbers lie between two consecutive perfect squares. Do you notice a pattern? Between 1 and 4 lie 2 numbers, between 4 and 9 lie 4 numbers, between 9 and 16
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: how many whole numbers lie strictly between 25 and 36? 2. The gap from n² to (n + 1)² is the odd number 2n + 1, and the numbers strictly between are one
   b2 worked_example/None refs=['1.1.between'] steps=3 video=VID1  Q: How many whole numbers lie strictly between 25 and 36?
C M2.S6.T6.C17  'Squares thin out in each hundred'  [obj O16]  media=['IMG1', 'VID1']  refs=['1.1.blocks']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: How many square numbers are there between 1 and 100? How many are there between 101 and 200? Write your answers in the table: 1 to 100, 101 to 200, and so on up to 901 to
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: are there more squares between 1 and 100 or between 901 and 1000? 2. List them: 1 to 100 has 10 squares, 101 to 200 has 4 (121, 144, 169, 196), 201 to 3
   b2 worked_example/None refs=['1.1.blocks'] steps=3 video=VID1  Q: How many perfect squares lie between 101 and 200, and what is the largest square less than 1000?
C M2.S6.T6.C18  'Two triangular numbers make a square'  [obj O17]  media=['IMG1', 'VID1']  refs=['1.1.triangular']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Perfect Squares and Triangular Numbers Triangular numbers: 1, 3, 6, 10, 15, ... Do you see any relation between triangular numbers and square numbers? Extend the pattern 
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: what do 6 and 10 add to? Is it special? 2. Triangular numbers are dots stacked in rows of 1, 2, 3, ...: 1, 3, 6, 10, 15. 3. Fit two consecutive triangle
   b2 worked_example/None refs=['1.1.triangular'] steps=3 video=VID1  Q: Add the next pair of consecutive triangular numbers after 6 and 10, and check that the sum is a square.
C M2.S6.T6.C19  'Practice: count between squares'  [obj O18]  media=['IMG1', 'VID1', '2D1']  refs=['FiO1.q7']
   b0 recap/None refs=[] steps=0 video=-  Q: Between n² and (n + 1)² lie exactly 2n numbers. Squares get rarer as numbers grow. Two consecutive triangular numbers add up to a square.
   b1 exercise/None refs=[] steps=3 video=VID1  Q: How many numbers lie between the squares of the following numbers? (i) 16 and 17 (ii) 99 and 100

## M2.S7.T7  Square Roots: The Side from the Area  [CONCEPT TOPIC]
C M2.S7.T7.C20  'The side of a square from its area'  [obj O19]  media=['IMG1', 'VID1']  refs=['1.1.root_side', '1.1.root_def']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Square Roots The area of a square is 49 sq cm. What is the length of its side? It is 7 cm, because 7² = 49. If y = x², then x is a square root of y. What is the square ro
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: a square has area 64 square cm. Is its side 32 cm, 16 cm or 8 cm? 2. The side times itself must give 64, and 8 × 8 = 64, so the side is 8 cm. Halving gi
   b2 worked_example/None refs=['1.1.root_side', '1.1.root_def'] steps=4 video=VID1  Q: A square has area 64 square cm. Find its side, and give both square roots of 64.
C M2.S7.T7.C21  'Find a root by listing squares'  [obj O20]  media=['IMG1', 'VID1']  refs=['1.1.mt_576']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Is 576 a perfect square? Is 327? How can we find their square roots? Squares end in 0, 1, 4, 5, 6 or 9, so 327, which ends in 7, is not a perfect square. Method 1: list t
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: which of 576 and 327 could be a perfect square? 2. 327 ends in 7, and no square ends in 7, so 327 is out. 3. For 576: 20² = 400 is too small and 30² = 9
   b2 worked_example/None refs=['1.1.mt_576'] steps=4 video=VID1  Q: Decide whether 576 and 327 are perfect squares, and find the square root of the one that is.
C M2.S7.T7.C22  'Find a root by subtracting odd numbers'  [obj O21]  media=['IMG1', 'VID1']  refs=['1.1.subtract_root']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Method 2: successive subtraction of odd numbers. 81 − 1 = 80, 80 − 3 = 77, 77 − 5 = 72, 72 − 7 = 65, 65 − 9 = 56, 56 − 11 = 45, 45 − 13 = 32, 32 − 15 = 17, 17 − 17 = 0. W
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: how many odd numbers must you subtract from 81 to reach 0? 2. 81 is the sum of the first few odd numbers; the count of those odd numbers is the root. 3.
   b2 worked_example/None refs=['1.1.subtract_root'] steps=4 video=VID1  Q: Find √81 by successive subtraction of odd numbers.
C M2.S7.T7.C23  'Practice: find the side from the area'  [obj O22]  media=['IMG1', 'VID1', '2D1']  refs=['FiO1.q4']
   b0 recap/None refs=[] steps=0 video=-  Q: The side of a square is the positive square root of its area. A square root is not half the number. List squares near the number, or subtract odd numbers, to find a root.
   b1 exercise/None refs=[] steps=4 video=VID1  Q: What is the length of the side of a square whose area is 441 m²?

## M2.S8.T8  Prime Factors Decide Squares  [CONCEPT TOPIC]
C M2.S8.T8.C24  'Two equal groups of prime factors'  [obj O23]  media=['IMG1', 'VID1']  refs=['1.1.prime_324', '1.1.prime_156']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Method 3: prime factorisation. Is 324 a perfect square? 324 = 2 × 2 × 3 × 3 × 3 × 3. The prime factors can be split into two equal groups, 2 × 3 × 3 and 2 × 3 × 3. So 324
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: is 324 a perfect square? It ends in 4, so it might be. 2. Factorise: 324 = 2 × 2 × 3 × 3 × 3 × 3. Every prime appears an even number of times. 3. Split 
   b2 worked_example/None refs=['1.1.prime_324', '1.1.prime_156'] steps=4 video=VID1  Q: Use prime factorisation to decide whether 324 and 156 are perfect squares.
C M2.S8.T8.C25  'Test 1156 and 2800 by pairing primes'  [thin-extra, obj O24]  media=['IMG1', 'VID1']  refs=['1.1.prime_try']
   b0 teaching_plan/None refs=[] steps=2 video=-  Q: 1. Predict first: 1156 ends in 6 and 2800 ends in two zeros. Are both squares? 2. Factorise and look for a prime with no partner.
   b1 worked_example/None refs=['1.1.prime_try'] steps=4 video=VID1  Q: Using prime factorisation, find whether 1156 and 2800 are perfect squares.
C M2.S8.T8.C26  'Practice: pair the prime factors'  [obj O25]  media=['IMG1', 'VID1', '2D1']  refs=['FiO1.q5']
   b0 recap/None refs=[] steps=0 video=-  Q: A perfect square has every prime factor appearing an even number of times. One group of the pairs, multiplied out, is the square root. Multiplying by the unpaired primes 
   b1 exercise/None refs=[] steps=4 video=VID1  Q: Find the smallest square number that is divisible by each of the following numbers: 4, 9 and 10.

## M2.S9.T9  Questions: Prime Factors Decide Squares  [QUESTIONS TOPIC (follows M2.S8.T8)]
C M2.S9.T9.C27  'Square Numbers, Q6'  [obj O26]  media=['VID1']  refs=['FiO1.q6']
   b0 exercise/figure_it_out refs=[] steps=4 video=VID1  Q: Find the smallest number by which 9408 must be multiplied so that the product is a perfect square. Find the square root of the product.
C M2.S9.T9.C28  'Square Numbers, Q9'  [obj O27]  media=['VID1']  refs=['FiO1.q9']
   b0 exercise/figure_it_out refs=[] steps=4 video=VID1  Q: How many tiny squares are there in the picture of 9 rows of 9 tiles, where every tile, upright or turned, is a grid of 5 by 5 tiny squares? Write the prime factorisation 

## M2.S10.T10  Estimating Square Roots  [CONCEPT TOPIC]
C M2.S10.T10.C29  'Pin down the root of a perfect square'  [obj O28]  media=['IMG1', 'VID1']  refs=['1.1.est_1936']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Estimating Square Roots Find √1936. Since 40² = 1600 and 50² = 2500, the root lies between 40 and 50. 1936 ends in 6, so the root ends in 4 or 6: it is 44 or 46. 45² = 20
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: is √1936 nearer 40 or nearer 50? 2. 40² = 1600 and 50² = 2500 trap the root between 40 and 50. 3. Squares ending in 6 come from numbers ending in 4 or 6
   b2 worked_example/None refs=['1.1.est_1936'] steps=4 video=VID1  Q: Find √1936 without long multiplication.
C M2.S10.T10.C30  'A root between two whole numbers'  [obj O29]  media=['IMG1', 'VID1']  refs=['1.1.est_game']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Aribam and Bijou play a game. One says a number and the other guesses its square root. Aribam says 25, Bijou says 5. Bijou says 81, Aribam says 9. Then Aribam says 250. 2
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: Bijou must guess √250. Is it a whole number? 2. 250 ends in a single 0, and squares end in an even number of zeros, so 250 is not a perfect square. 3. 1
   b2 worked_example/None refs=['1.1.est_game'] steps=3 video=VID1  Q: Between which two consecutive whole numbers does √250 lie, and which is it closer to?
C M2.S10.T10.C31  'Akhil's handkerchief'  [obj O30]  media=['IMG1', 'VID1']  refs=['1.1.est_cloth']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Akhil has a square piece of cloth of area 125 cm². He wants to make a square handkerchief of side 15 cm. Is it possible? If not, what is the largest whole number side of 
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: can a 15 cm handkerchief come out of a cloth of area 125 cm²? 2. A 15 cm square needs 15² = 225 cm², far more than 125 cm². 3. 11² = 121 ≤ 125 < 144 = 1
   b2 worked_example/None refs=['1.1.est_cloth'] steps=4 video=VID1  Q: Akhil's square cloth has area 125 cm². Can he cut a square handkerchief of side 15 cm? What is the largest whole number side he can cut?
C M2.S10.T10.C32  'Practice: trap the root'  [obj O31]  media=['IMG1', 'VID1', '2D1']  refs=['FiO1.q1']
   b0 recap/None refs=[] steps=0 video=-  Q: If a² < N < (a + 1)², then √N lies between a and a + 1. A number whose root is trapped strictly between two whole numbers is not a perfect square. For a perfect square, t
   b1 exercise/None refs=[] steps=4 video=VID1  Q: Which of the following numbers are not perfect squares? (i) 2032 (ii) 2048 (iii) 1027 (iv) 1089

## M3.S11.T11  Cubes: Building with Unit Cubes  [CONCEPT TOPIC]
C M3.S11.T11.C33  'How many unit cubes make a cube'  [obj O32]  media=['IMG1', 'VID1']  refs=['1.2.cube_2', '1.2.cube_3', '1.2.cube_9', '1.2.cube_4']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: 1.2 Cubic Numbers How many cubes of side 1 cm make a cube of side 2 cm? 8. How many cubes of side 1 cm will make a cube of side 3 cm? 27. Numbers like 1, 8, 27 are called
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: how many 1 cm cubes build a cube of edge 4 cm? Is it 12, 16 or 64? 2. Build it in layers. The bottom layer is a 4 by 4 square, 16 cubes, and there are 4
   b2 worked_example/None refs=['1.2.cube_2', '1.2.cube_3', '1.2.cube_9', '1.2.cube_4'] steps=3 video=VID1  Q: How many unit cubes make cubes of edge 2, 3 and 4 units?
C M3.S11.T11.C34  'The last digits and the length of cubes'  [obj O33]  media=['IMG1', 'VID1']  refs=['1.2.cube_count_digits', '1.2.cube_00', '1.2.cube_table', '1.2.mt_cube_patterns', '1.2.cube_digits']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Complete the table of cubes from 1 to 20. What patterns do you notice in the table? We know that the last digit of a square is 0, 1, 4, 5, 6 or 9. What are the possible l
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: can a cube end in 7, which no square can? 2. From the table, 1³ = 1, 2³ = 8, 3³ = 27, 7³ = 343: every digit 0 to 9 appears as a last digit. 3. 1 digit: 
   b2 worked_example/None refs=['1.2.cube_count_digits', '1.2.cube_00', '1.2.cube_table', '1.2.mt_cube_patterns', '1.2.cube_digits'] steps=4 video=VID1  Q: How many cubes have exactly 3 digits, and can a cube end in exactly two zeros?
C M3.S11.T11.C35  'Cubes of fractions, decimals and negative numbers'  [obj O34]  media=['IMG1', 'VID1']  refs=['1.2.cube_other']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: We can also find cubes of fractions, decimals and negative numbers: (4/6)³ = 64/216, 13.08³ = 2237.810112, (−6)³ = −216.
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: is (−6)³ positive or negative? 2. (−6)³ = −6 × −6 × −6. The first two give 36, and 36 × −6 = −216: negative. 3. Compare (−6)² = 36, positive. An odd num
   b2 worked_example/None refs=['1.2.cube_other'] steps=3 video=VID1  Q: Find (−6)³, (−6)² and (4/6)³.
C M3.S11.T11.C36  'Practice: stack the cubes'  [obj O35]  media=['IMG1', 'VID1', '2D1']  refs=['FiO2.q3']
   b0 recap/None refs=[] steps=0 video=-  Q: A cube of edge n holds n layers of n² unit cubes, n³ in all. Cubes can end in any digit; their end zeros come in threes. The cube of an odd number is odd and the cube of 
   b1 exercise/None refs=[] steps=5 video=VID1  Q: State true or false. Explain your reasoning. (i) The cube of any odd number is even. (ii) There is no perfect cube that ends with 8. (iii) The cube of a 2 digit number ma

## M3.S12.T12  Taxicab Numbers and Cube Patterns  [CONCEPT TOPIC]
C M3.S12.T12.C37  'Taxicab numbers'  [obj O36]  media=['IMG1', 'VID1']  refs=['1.2.taxicab', '1.2.try_taxicab']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Hardy came to see Ramanujan in a taxi numbered 1729 and remarked that the number seemed rather dull. Ramanujan replied that it is a very interesting number: it is the sma
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: can 1729 be split into two cubes? Try 12³ first. 2. 12³ = 1728, and 1729 − 1728 = 1 = 1³. So 1729 = 1³ + 12³. 3. Now 10³ = 1000 and 1729 − 1000 = 729 = 
   b2 worked_example/None refs=['1.2.taxicab', '1.2.try_taxicab'] steps=3 video=VID1  Q: Show that 4104 is a sum of two cubes in two different ways.
C M3.S12.T12.C38  'Cubes from consecutive odd numbers'  [obj O37]  media=['IMG1', 'VID1']  refs=['1.2.odd_cubes', '1.2.odd_91']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Perfect Cubes and Consecutive Odd Numbers 1 = 1 = 1³, 3 + 5 = 8 = 2³, 7 + 9 + 11 = 27 = 3³, 13 + 15 + 17 + 19 = 64 = 4³, 21 + 23 + 25 + 27 + 29 = 125 = 5³, 31 + 33 + 35 +
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: what is 7 + 9 + 11? Is it a square or a cube? 2. Group the odd numbers: 1, then 3 + 5, then 7 + 9 + 11. The sums are 1, 8, 27: the cubes. 3. The nth blo
   b2 worked_example/None refs=['1.2.odd_cubes', '1.2.odd_91'] steps=4 video=VID1  Q: Find 91 + 93 + 95 + 97 + 99 + 101 + 103 + 105 + 107 + 109 using the cube pattern.
C M3.S12.T12.C39  'Successive differences of squares and cubes'  [obj O38]  media=['IMG1', 'VID1']  refs=['1.2.diff_squares', '1.2.diff_cubes']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Successive differences: for the squares 1, 4, 9, 16, 25, ... the first differences are 3, 5, 7, 9, ... and the second differences are all 2. Compute the successive differ
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: for cubes, after how many levels of differences do you get a constant? 2. Cubes 1, 8, 27, 64, 125, 216: first differences 7, 19, 37, 61, 91. 3. Second d
   b2 worked_example/None refs=['1.2.diff_squares', '1.2.diff_cubes'] steps=4 video=VID1  Q: Find the successive differences of the cubes 1, 8, 27, 64, 125 and 216 until they are constant.
C M3.S12.T12.C40  'Practice: compare differences of cubes and squares'  [obj O39]  media=['IMG1', 'VID1', '2D1']  refs=['FiO2.q5']
   b0 recap/None refs=[] steps=0 video=-  Q: Consecutive squares differ by odd numbers that grow by 2. Consecutive cubes differ by numbers that grow much faster: 7, 19, 37, 61, 91, ... The nth cube is the sum of the
   b1 exercise/None refs=[] steps=4 video=VID1  Q: Which of the following is the greatest? Explain your reasoning. (i) 67³ − 66³ (ii) 43³ − 42³ (iii) 67² − 66² (iv) 43² − 42²

## M3.S13.T13  Cube Roots by Grouping in Threes  [CONCEPT TOPIC]
C M3.S13.T13.C41  'Three equal groups of prime factors'  [obj O40]  media=['IMG1', 'VID1']  refs=['1.2.root_def', '1.2.root_3375', '1.2.root_500']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Cube Roots The cube root of 8 is 2, the cube root of 27 is 3, and the cube root of 1000 is 10. The cube root of n³ is n. The symbol for the cube root is a root sign with 
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: is 3375 a perfect cube? Its last digit is 5, so its root would end in 5. 2. Factorise: 3375 = 3 × 3 × 3 × 5 × 5 × 5. Each prime appears three times. 3. 
   b2 worked_example/None refs=['1.2.root_def', '1.2.root_3375', '1.2.root_500'] steps=4 video=VID1  Q: Decide whether 3375 and 500 are perfect cubes, and give the cube root of the one that is.
C M3.S13.T13.C42  'Cube roots of 64, 512 and 729'  [thin-extra, obj O41]  media=['IMG1', 'VID1']  refs=['1.2.root_find']
   b0 teaching_plan/None refs=[] steps=2 video=-  Q: 1. Predict first: is the cube root of 512 bigger or smaller than 10? 2. Group the prime factors into three equal groups and multiply one group.
   b1 worked_example/None refs=['1.2.root_find'] steps=3 video=VID1  Q: Find the cube roots of 64, 512 and 729.
C M3.S13.T13.C43  'Practice: group the primes in threes'  [obj O42]  media=['IMG1', 'VID1', '2D1']  refs=['FiO2.q1']
   b0 recap/None refs=[] steps=0 video=-  Q: A perfect cube has every prime factor appearing a multiple of three times. One of the three equal groups, multiplied out, is the cube root. Multiplying by the missing pri
   b1 exercise/None refs=[] steps=4 video=VID1  Q: Find the cube roots of 27000 and 10648.

## M3.S14.T14  Questions: Cube Roots by Grouping in Threes  [QUESTIONS TOPIC (follows M3.S13.T13)]
C M3.S14.T14.C44  'Cubic Numbers, Q2'  [obj O43]  media=['VID1']  refs=['FiO2.q2']
   b0 exercise/figure_it_out refs=[] steps=3 video=VID1  Q: What number will you multiply by 1323 to make it a cube number?
C M3.S14.T14.C45  'Cubic Numbers, Q4'  [obj O44]  media=['VID1']  refs=['FiO2.q4']
   b0 exercise/figure_it_out refs=[] steps=4 video=VID1  Q: Guess the cube roots of the following numbers: (i) 1331 (ii) 4913 (iii) 12167 (iv) 32768

## M4.S15.T15  Summary: A Square and A Cube  [SUMMARY]
C M4.S15.T15.C46  'What we found about squares and cubes'  [obj O45]  media=['IMG1']  refs=['summary']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: A number obtained by multiplying a number by itself is called a square number. Squares of natural numbers are called perfect squares. All perfect squares end in 0, 1, 4, 
   b1 teaching_plan/None refs=[] steps=3 video=-  Q: 1. Our opening puzzle is settled: the lockers left open are the squares 1, 4, 9, up to 100, because only squares have an odd number of factors. 2. Squares are areas, end 
C M4.S15.T15.C47  'A pinch of history: varga, ghana and mula'  [enrichment]  media=['IMG1', 'VID1']  refs=['history']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: 1.3 A Pinch of History Clay tablets from Babylon, from around 1700 BCE, list squares and cubes of numbers. In India the square was called varga and the cube ghana, and th
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: why might people have called a square root a root, like the root of a plant? 2. Babylonian tablets of about 1700 BCE already listed squares and cubes. 3
   b2 worked_example/None refs=['history'] steps=4 video=VID1  Q: Name the Indian words for the square, the cube, the square root and the cube root, and explain what the word root means.
C M4.S15.T15.C48  'Square Pairs'  [enrichment]  media=['IMG1', 'VID1']  refs=['puzzle']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Puzzle Time: Square Pairs! In the row 3, 6, 10, 15, 1, each pair of neighbours adds up to a perfect square: 3 + 6 = 9, 6 + 10 = 16, 10 + 15 = 25, 15 + 1 = 16. Arrange the
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: which numbers from 1 to 17 can sit next to 16? 2. Neighbour sums can only be 4, 9, 16 or 25. 16 pairs only with 9 to make 25, and 17 only with 8. 3. A n
   b2 worked_example/None refs=['puzzle'] steps=3 video=VID1  Q: Arrange 1 to 17 in a row so that each pair of neighbours adds to a perfect square.

## Book items the plan covers (coverage id -> concept)

- puzzle -> M4.S15.T15.C48
- FiO1.q1 -> M2.S10.T10.C32
- FiO1.q2 -> M2.S3.T3.C10
- FiO1.q3 -> M2.S4.T4.C14
- FiO1.q4 -> M2.S7.T7.C23
- FiO1.q5 -> M2.S8.T8.C26
- FiO1.q6 -> M2.S9.T9.C27
- FiO1.q7 -> M2.S6.T6.C19
- FiO1.q8 -> M2.S5.T5.C15
- FiO1.q9 -> M2.S9.T9.C28
- FiO2.q1 -> M3.S13.T13.C43
- FiO2.q2 -> M3.S14.T14.C44
- FiO2.q3 -> M3.S11.T11.C36
- FiO2.q4 -> M3.S14.T14.C45
- FiO2.q5 -> M3.S12.T12.C40
- history -> M4.S15.T15.C47
- opening -> M1.S1.T1.C1
- summary -> M4.S15.T15.C46
- 1.1.ends1 -> M2.S3.T3.C8
- 1.1.ends6 -> M2.S3.T3.C7
- 1.1.zeros -> M2.S3.T3.C9
- 1.1.blocks -> M2.S6.T6.C17
- 1.1.mt_576 -> M2.S7.T7.C21
- 1.1.parity -> M2.S3.T3.C9
- 1.1.which6 -> M2.S3.T3.C7
- 1.2.cube_2 -> M3.S11.T11.C33
- 1.2.cube_3 -> M3.S11.T11.C33
- 1.2.cube_4 -> M3.S11.T11.C33
- 1.2.cube_9 -> M3.S11.T11.C33
- 1.2.odd_91 -> M3.S12.T12.C38
- 1.0.factors -> M1.S2.T2.C2
- 1.1.between -> M2.S6.T6.C16
- 1.1.nth_odd -> M2.S4.T4.C13
- 1.1.odd_sum -> M2.S4.T4.C11
- 1.1.table30 -> M2.S3.T3.C7
- 1.2.cube_00 -> M3.S11.T11.C34
- 1.2.taxicab -> M3.S12.T12.C37
- 1.1.est_1936 -> M2.S10.T10.C29
- 1.1.est_game -> M2.S10.T10.C30
- 1.1.notation -> M2.S3.T3.C6
- 1.1.root_def -> M2.S7.T7.C20
- 1.2.root_500 -> M3.S13.T13.C41
- 1.2.root_def -> M3.S13.T13.C41
- 1.1.est_cloth -> M2.S10.T10.C31
- 1.1.mt_always -> M2.S3.T3.C8
- 1.1.odd_diffs -> M2.S4.T4.C11
- 1.1.prime_156 -> M2.S8.T8.C24
- 1.1.prime_324 -> M2.S8.T8.C24
- 1.1.prime_try -> M2.S8.T8.C25
- 1.1.root_side -> M2.S7.T7.C20
- 1.2.odd_cubes -> M3.S12.T12.C38
- 1.2.root_3375 -> M3.S13.T13.C41
- 1.2.root_find -> M3.S13.T13.C42
- 1.0.square_def -> M1.S2.T2.C3
- 1.1.area_table -> M2.S3.T3.C6
- 1.1.triangular -> M2.S6.T6.C18
- 1.2.cube_other -> M3.S11.T11.C35
- 1.2.cube_table -> M3.S11.T11.C34
- 1.2.diff_cubes -> M3.S12.T12.C39
- 1.0.odd_insight -> M1.S2.T2.C3
- 1.1.mt_patterns -> M2.S3.T3.C7
- 1.1.next_square -> M2.S4.T4.C13
- 1.1.perfect_def -> M2.S3.T3.C6
- 1.2.cube_digits -> M3.S11.T11.C34
- 1.2.try_taxicab -> M3.S12.T12.C37
- 1.0.even_factors -> M1.S2.T2.C2
- 1.0.five_lockers -> M1.S2.T2.C5
- 1.0.open_lockers -> M1.S2.T2.C4
- 1.2.diff_squares -> M3.S12.T12.C39
- 1.1.more_patterns -> M2.S3.T3.C8
- 1.1.subtract_root -> M2.S7.T7.C22
- 1.1.subtract_test -> M2.S4.T4.C12
- 1.1.five_nonsquares -> M2.S3.T3.C8
- 1.2.mt_cube_patterns -> M3.S11.T11.C34
- 1.2.cube_count_digits -> M3.S11.T11.C34
