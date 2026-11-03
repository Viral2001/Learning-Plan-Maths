# Power Play  (cbse_eng_maths8_ch2, live v32)

Book text: `textbooks/extracted/hegp102.txt`

Topics in order. `C` lines are concepts; `b<i>` lines are content blocks (kind, item_kind, refs, steps, question). A concept topic is followed by its existing Questions topic (if any).

## M1.S1.T1  Power Play: Can Folded Paper Reach the Moon?  [FRAMING]
C M1.S1.T1.C1  'Fold a sheet as many times as you can'  [enrichment]  media=['IMG1', 'VID1']  refs=['2.1.intro']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: 2.1 Experiencing the Power Play An Impossible Venture! Take a sheet of paper, as large a sheet as you can find. Fold it once. Fold it again, and again. How many times can
   b1 teaching_plan/None refs=[] steps=3 video=-  Q: 1. Predict first: if a sheet could be folded 46 times, would the stack be as tall as a table, a building, a mountain, or taller? 2. Each fold puts one half of the stack o

## M1.S2.T2  Folding Paper: Doubling Every Time  [CONCEPT TOPIC]
C M1.S2.T2.C2  'The thickness doubles with each fold'  [obj O1]  media=['IMG1', 'VID1']  refs=['2.1.table17']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Let us find out how thick a sheet of paper will be after 46 folds. Assume that the thickness of the sheet is 0.001 cm. The following table lists the thickness after each 
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: after 10 folds, is the stack thinner or thicker than your finger? 2. Start at 0.001 cm. Each fold doubles: 0.002, 0.004, 0.008, 0.016 and so on. 3. Afte
   b2 worked_example/None refs=['2.1.table17'] steps=4 video=VID1  Q: A sheet is 0.001 cm thick. Find its thickness after 1, 2, 3, 10 and 17 folds.
C M1.S2.T2.C3  'Taller than a tower, deeper than the ocean'  [obj O2]  media=['IMG1', 'VID1']  refs=['2.1.mt_guess', '2.1.burj_mariana']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Now, what do you think the thickness would be after 30 folds? 45 folds? Make a guess. Fold 18: about 262 cm. Fold 19: about 524 cm. Fold 20: about 10.4 m. After 26 folds,
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: after 30 folds, would the stack be taller than a building, a mountain, or the height where planes fly? 2. From about 10.4 m at fold 20, six doublings re
   b2 worked_example/None refs=['2.1.mt_guess', '2.1.burj_mariana'] steps=5 video=VID1  Q: After 20 folds the stack is about 10.4 m. Find the thickness after 26, 27 and 30 folds and compare it with the Burj Khalifa (830 m) and the Mariana Trench (11 km).
C M1.S2.T2.C4  'Multiplicative growth: every 10 folds multiply by 1024'  [obj O3]  media=['IMG1', 'VID1']  refs=['2.1.two_folds', '2.1.three_folds', '2.1.ten_folds']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: It might be hard to digest the fact that after just 46 folds, the thickness is more than 7,00,000 km. This is the power of multiplicative growth, also called exponential 
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: from fold 5 to fold 7, does the thickness grow by adding a fixed amount or by multiplying? 2. Two folds double twice: 2 × 2 = 4, so the thickness become
   b2 worked_example/None refs=['2.1.two_folds', '2.1.three_folds', '2.1.ten_folds'] steps=4 video=VID1  Q: Check that two folds multiply the thickness by 4, three folds by 8, and ten folds by 1024, using the thickness table.
C M1.S2.T2.C5  'Practice: fill the folding table'  [obj O4]  media=['IMG1', 'VID1', '2D1']  refs=['2.1.fill_table']
   b0 recap/None refs=[] steps=0 video=-  Q: Each fold doubles the thickness. Every 10 folds the thickness becomes 1024 times as much.
   b1 exercise/None refs=[] steps=6 video=VID1  Q: Fill the table of thickness for folds 21 to 45, starting from about 10.4 m after 20 folds. After how many folds is the stack more than the 3,84,400 km distance to the Moo

## M2.S3.T3  Exponential Notation: Powers, Bases and Exponents  [CONCEPT TOPIC]
C M2.S3.T3.C6  'A power has a base and an exponent'  [obj O5]  media=['IMG1', 'VID1']  refs=['2.2.fold_power', '2.2.read_powers', '2.2.base_exponent']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: 2.2 Exponential Notation and Operations The initial thickness of the paper was 0.001 cm. Upon folding once, its thickness became 0.001 cm × 2 = 0.002 cm. Folding it twice
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: is 5⁴ equal to 20 or to 625? 2. The small raised number counts the factors: 5⁴ means four 5s multiplied, 5 × 5 × 5 × 5. 3. So 5⁴ is 625, not 5 × 4. The 
   b2 worked_example/None refs=['2.2.fold_power', '2.2.read_powers', '2.2.base_exponent'] steps=4 video=VID1  Q: Write the thickness after 4 folds as a power of 2, and find the value of 5⁴. Name the base and the exponent of 5⁴.
C M2.S3.T3.C7  'Repeated multiplication is not repeated addition'  [obj O6]  media=['IMG1', 'VID1']  refs=['2.2.ten_folds_v', '2.2.add_vs_mult']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Which expression describes the thickness of a sheet of paper after it is folded 10 times? The initial thickness is represented by the letter-number v. (i) 10v (ii) 10 + v
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: which expression, 10v or 2¹⁰v, gives the thickness after 10 folds? 2. Each fold doubles, so ten folds multiply v by 2 ten times: 2¹⁰v. 3. 10v adds v ten
   b2 worked_example/None refs=['2.2.ten_folds_v', '2.2.add_vs_mult'] steps=4 video=VID1  Q: A sheet has thickness v. Which expression gives its thickness after 10 folds: 10v, 10 + v, 2 × 10 × v, 2¹⁰, 2¹⁰v or 10²v? Then compare 4 + 4 + 4 with 4 × 4 × 4.
C M2.S3.T3.C8  'Powers of negative numbers and of zero'  [obj O7]  media=['IMG1', 'VID1']  refs=['2.2.neg_base', '2.2.neg1_powers', '2.2.neg2_pow4', '2.2.zero_powers']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: 4 × 4 × 4 = 4³ = 64. (−4) × (−4) × (−4) = (−4)³ = −64. What is (−1)⁵? Is it positive or negative? What about (−1)⁵⁶? Is (−2)⁴ = 16? Verify. What is 0², 0⁵? What is 0ⁿ?
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: is (−4)³ positive or negative? 2. Multiply in pairs: two negative factors make a positive, so an even number of negative factors gives a positive value 
   b2 worked_example/None refs=['2.2.neg_base', '2.2.neg1_powers', '2.2.neg2_pow4', '2.2.zero_powers'] steps=5 video=VID1  Q: Find (−4)³, (−1)⁵, (−1)⁵⁶, (−2)⁴, 0² and 0⁵.
C M2.S3.T3.C9  'Prime factors and letters in exponential form'  [thin-extra, obj O8]  media=['IMG1', 'VID1']  refs=['2.2.letters', '2.2.prime_32400']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: a × a × a × b × b can be expressed as a³b² (read as a cubed b squared). a × a × b × b × b × b can be expressed as a²b⁴ (read as a squared b raised to the power 4). Expres
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: how many 3s are hidden in 32400? 2. Group equal factors and count each group: a × a × a × b × b is a³b². 3. Divide 32400 by primes again and again: by 2
   b2 worked_example/None refs=['2.2.letters', '2.2.prime_32400'] steps=4 video=VID1  Q: Write a × a × b × b × b × b in exponential form, and express 32400 as a product of powers of primes.
C M2.S3.T3.C10  'Practice: write and evaluate powers'  [obj O9]  media=['IMG1', 'VID1', '2D1']  refs=['FiO1.q1']
   b0 recap/None refs=[] steps=0 video=-  Q: A power counts factors: nᵃ is a factors of n multiplied together. An even number of negative factors gives a positive value; an odd number gives a negative value.
   b1 exercise/None refs=[] steps=4 video=VID1  Q: Express the following in exponential form: (i) 6 × 6 × 6 × 6 (ii) y × y (iii) b × b × b × b (iv) 5 × 5 × 7 × 7 × 7 (v) 2 × 2 × a × a (vi) a × a × a × c × c × c × c × d

## M2.S4.T4  Questions: Exponential Notation: Powers, Bases and Exponents  [QUESTIONS TOPIC (follows M2.S3.T3)]
C M2.S4.T4.C11  'Exponential Notation, Q2'  [obj O10]  media=['VID1']  refs=['FiO1.q2']
   b0 exercise/figure_it_out refs=[] steps=4 video=VID1  Q: Express each of the following as a product of powers of their prime factors in exponential form. (i) 648 (ii) 405 (iii) 540 (iv) 3600
C M2.S4.T4.C12  'Exponential Notation, Q3'  [obj O11]  media=['VID1']  refs=['FiO1.q3']
   b0 exercise/figure_it_out refs=[] steps=6 video=VID1  Q: Write the numerical value of each of the following: (i) 2 × 10³ (ii) 7² × 2³ (iii) 3 × 4⁴ (iv) (−3)² × (−5)² (v) 3² × 10⁴ (vi) (−2)⁵ × (−10)⁶

## M3.S5.T5  Multiplying Powers of the Same Base  [CONCEPT TOPIC]
C M3.S5.T5.C13  'The Stones that Shine: counting by powers of 3'  [obj O12]  media=['IMG1', 'VID1']  refs=['2.2.stones_rooms', '2.2.stones_diamonds']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: The Stones that Shine Once upon a time, there lived a king who had 3 daughters. Each daughter had 3 baskets, each basket had 3 keys, each key opened 3 rooms, each room ha
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: are there a few hundred diamonds or a few thousand? 2. Each level multiplies by 3: daughters 3, baskets 9, keys 27, rooms 81, so the rooms are 3⁴. 3. Th
   b2 worked_example/None refs=['2.2.stones_rooms', '2.2.stones_diamonds'] steps=4 video=VID1  Q: In the story, find the number of rooms and the number of diamonds.
C M3.S5.T5.C14  'Multiply powers of the same base: add the exponents'  [obj O13]  media=['IMG1', 'VID1']  refs=['2.2.why_3p2_3p5', '2.2.p4p6', '2.2.product_law', '2.2.compute_three']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: We can write 3 to the power 7 as (3 × 3 × 3 × 3) × (3 × 3 × 3) = 3⁴ × 3³ = 81 × 27 = 2187. 3 to the power 7 can also be written as 3² × 3 to the power 5. Can you reason o
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: is p⁴ × p to the power 6 equal to p to the power 10 or p to the power 24? 2. Write out the factors: four p's then six p's in one row make ten p's. 3. So
   b2 worked_example/None refs=['2.2.why_3p2_3p5', '2.2.p4p6', '2.2.product_law', '2.2.compute_three'] steps=4 video=VID1  Q: Write p⁴ × p to the power 6 as one power, and compute 2 to the power 9 and 5 to the power 7 by splitting the exponents.
C M3.S5.T5.C15  'A power of a power: multiply the exponents'  [obj O14]  media=['IMG1', 'VID1']  refs=['2.2.four_pow6', '2.2.seven4_two10', '2.2.power_of_power']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: 4 to the power 6 can be evaluated in these two ways: (4 × 4 × 4) × (4 × 4 × 4) = 4³ × 4³ = 64 × 64 = 4096, and (4 × 4) × (4 × 4) × (4 × 4) = 4² × 4² × 4² = 16 × 16 × 16 =
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: is (4³)² equal to 4 to the power 5 or 4 to the power 6? 2. (4³)² means two copies of 4³, that is two groups of three 4s, six 4s in all. 3. So a power of
   b2 worked_example/None refs=['2.2.four_pow6', '2.2.seven4_two10', '2.2.power_of_power'] steps=4 video=VID1  Q: Evaluate 4 to the power 6 in two ways, and check whether 2 to the power 10 equals (2 to the power 5)².
C M3.S5.T5.C16  'Write a power as a power of a power in two ways'  [thin-extra, obj O15]  media=['IMG1', 'VID1']  refs=['2.2.mt_two_ways']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Write the following expressions as a power of a power in at least two different ways: (i) 8 to the power 6 (ii) 7 to the power 15 (iii) 9 to the power 14 (iv) 5 to the po
   b1 teaching_plan/None refs=[] steps=3 video=-  Q: 1. Predict first: how many ways can the exponent 6 be split into two factors? 2. Split the exponent as a product: 6 is 2 × 3 or 3 × 2. 3. A base can also be rewritten: 8 
   b2 worked_example/None refs=['2.2.mt_two_ways'] steps=4 video=VID1  Q: Write 8 to the power 6, 7 to the power 15, 9 to the power 14 and 5 to the power 8 as a power of a power in two ways.
C M3.S5.T5.C17  'Practice: products and powers of powers'  [obj O16]  media=['IMG1', 'VID1', '2D1']  refs=['FiO2.q4']
   b0 recap/None refs=[] steps=0 video=-  Q: Multiplying powers of the same base adds the exponents. A power of a power multiplies the exponents, in either order.
   b1 exercise/None refs=[] steps=5 video=VID1  Q: Examine each statement and find out if it is Always True, Only Sometimes True, or Never True. (i) Cube numbers are also square numbers. (ii) Fourth powers are also square

## M3.S6.T6  Questions: Multiplying Powers of the Same Base  [QUESTIONS TOPIC (follows M3.S5.T5)]
C M3.S6.T6.C18  'Power Play, Q10'  [obj O17]  media=['VID1']  refs=['FiO2.q10']
   b0 exercise/figure_it_out refs=[] steps=4 video=VID1  Q: 64 is a square number (8²) and a cube number (4³). Are there other numbers that are both squares and cubes? Is there a way to describe such numbers in general?

## M3.S7.T7  Same Exponent, Different Bases  [CONCEPT TOPIC]
C M3.S7.T7.C19  'The magical pond: half covered the day before'  [obj O18]  media=['IMG1', 'VID1']  refs=['2.2.pond_half', '2.2.pond_exp']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Magical Pond In the middle of a beautiful, magical pond lies a bright pink lotus. The number of lotuses doubles every day in this pond. After 30 days, the pond is complet
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: was the pond half covered on day 15 or on some other day? 2. Work backwards: the lotuses double every day, so the day before full they were half. 3. Sta
   b2 worked_example/None refs=['2.2.pond_half', '2.2.pond_exp'] steps=4 video=VID1  Q: A pond starts with 1 lotus and the number doubles every day. It is full after 30 days. When was it half covered, and how many lotuses were there when full and when half c
C M3.S7.T7.C20  'Multiply powers with the same exponent'  [obj O19]  media=['IMG1', 'VID1']  refs=['2.2.damayanti', '2.2.order_swap', '2.2.same_exp_law', '2.2.compute_2p5_5p5']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: There is another pond in which the number of lotuses triples every day. When both the ponds had no flowers, Damayanti placed a lotus in the doubling pond. After 4 days, s
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: if Damayanti uses the tripling pond first, will she end with more lotuses, fewer, or the same? 2. Doubling 4 times gives 2⁴; tripling 4 more times gives
   b2 worked_example/None refs=['2.2.damayanti', '2.2.order_swap', '2.2.same_exp_law', '2.2.compute_2p5_5p5'] steps=4 video=VID1  Q: Damayanti puts a lotus in the doubling pond for 4 days and then moves all the lotuses to the tripling pond for 4 days. Find the number of lotuses, and use the same idea t
C M3.S7.T7.C21  'Divide powers with the same exponent'  [obj O20]  media=['IMG1', 'VID1']  refs=['2.2.simplify_10p4_5p4', '2.2.quotient_same_exp']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Simplify 10⁴ ÷ 5⁴ and write it in exponential form. In general, we can show that m to the power a ÷ n to the power a = (m ÷ n) to the power a.
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: is 10⁴ ÷ 5⁴ equal to 2, to 16, or to 2 to the power 0? 2. Write it as a fraction with four 10s on top and four 5s below. 3. Pair each 10 with a 5: each 
   b2 worked_example/None refs=['2.2.simplify_10p4_5p4', '2.2.quotient_same_exp'] steps=4 video=VID1  Q: Simplify 10⁴ ÷ 5⁴ and write it in exponential form. Check by computing both powers.
C M3.S7.T7.C22  'Practice: spot equal products of powers'  [obj O21]  media=['IMG1', 'VID1', '2D1']  refs=['FiO2.q7']
   b0 recap/None refs=[] steps=0 video=-  Q: m to the power a times n to the power a is (mn) to the power a. Rewrite every number with prime bases to compare them.
   b1 exercise/None refs=[] steps=5 video=VID1  Q: Circle the numbers that are the same: 2⁴ × 3 to the power 6, 6⁴ × 3², 6 to the power 10, 18² × 6², 6 to the power 24.

## M3.S8.T8  How Many Combinations?  [CONCEPT TOPIC]
C M3.S8.T8.C23  'Count outfits by multiplying the choices'  [obj O22]  media=['IMG1', 'VID1']  refs=['2.2.dresses_caps', '2.2.roxie_outfits']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: How Many Combinations Estu has 4 dresses and 3 caps. How many different ways can Estu combine the dresses and caps? For each cap, he can choose any of the 4 dresses, so f
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: does Estu have 7 outfits, 12, or some other number? 2. Draw a tree: for each cap, every one of the 4 dresses can go with it, so 4 + 4 + 4 = 12. 3. Addin
   b2 worked_example/None refs=['2.2.dresses_caps', '2.2.roxie_outfits'] steps=3 video=VID1  Q: Estu has 4 dresses and 3 caps. Roxie has 7 dresses, 2 hats and 3 pairs of shoes. How many outfits can each make?
C M3.S8.T8.C24  'Lock passwords as powers of 10'  [obj O23]  media=['IMG1', 'VID1']  refs=['2.2.lock_2digit', '2.2.lock_3digit', '2.2.lock_5digit']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Estu and Roxie came across a safe containing old stamps and coins that their great-grandfather had collected. It was secured with a 5-digit password. They were unlucky an
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: does a 5-digit lock have about 50 passwords, about 1000, or many more? 2. Solve a simpler lock first: 2 digits give 10 choices for each of 10 choices, s
   b2 worked_example/None refs=['2.2.lock_2digit', '2.2.lock_3digit', '2.2.lock_5digit'] steps=4 video=VID1  Q: How many passwords does a 2-digit, a 3-digit and a 5-digit lock have?
C M3.S8.T8.C25  'Letter locks and codes around us'  [obj O24]  media=['IMG1', 'VID1']  refs=['2.2.letter_lock', '2.2.try_codes']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Estu says, "Next time, I will buy a lock that has 6 slots with the letters A to Z. I feel it is safer." How many passwords are possible with such a lock? Think about how 
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: is a 6-letter lock safer than a 5-digit lock? 2. Each slot now has 26 choices, so 6 slots give 26 multiplied by itself 6 times. 3. 26 to the power 6 is 
   b2 worked_example/None refs=['2.2.letter_lock', '2.2.try_codes'] steps=4 video=VID1  Q: How many passwords does a lock with 6 slots of letters A to Z have? Compare it with a 5-digit lock, and say how many 6-digit pincodes are possible.
C M3.S8.T8.C26  'Practice: count codes with powers'  [obj O25]  media=['IMG1', 'VID1', '2D1']  refs=['FiO2.q11']
   b0 recap/None refs=[] steps=0 video=-  Q: Each slot multiplies the count by the number of choices for that slot. n slots of 10 digits give 10 to the power n codes.
   b1 exercise/None refs=[] steps=3 video=VID1  Q: A digital locker has an alphanumeric passcode of length 5. Some example codes are G89P0, 38098, BRJKW and 003AZ. How many such codes are possible?

## M3.S9.T9  Questions: How Many Combinations?  [QUESTIONS TOPIC (follows M3.S8.T8)]
C M3.S9.T9.C27  'Power Play, Q9'  [obj O26]  media=['VID1']  refs=['FiO2.q9']
   b0 exercise/figure_it_out refs=[] steps=4 video=VID1  Q: A dairy plans to produce 8.5 billion packets of milk in a year. They want a unique ID code for each packet. If they choose to use the digits 0 to 9, how many digits shoul

## M4.S10.T10  Dividing Powers of the Same Base  [CONCEPT TOPIC]
C M4.S10.T10.C28  'Halving a line: 16, 8, 4, 2'  [obj O27]  media=['IMG1', 'VID1']  refs=['2.3.halving_line']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: 2.3 The Other Side of Powers Imagine a line of length 16 units. Erasing half of it would result in 2⁴ ÷ 2 = 2 × 2 × 2 = 2³ = 8 units. Erasing half one more time would res
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: after halving a 16-unit line three times, how long is it? 2. 16 is 2⁴. Halving once divides by 2 and cancels one factor of 2: 2³, which is 8. 3. Halving
   b2 worked_example/None refs=['2.3.halving_line'] steps=4 video=VID1  Q: A line is 16 units long. Find its length after halving it once, twice and three times, as powers of 2.
C M4.S10.T10.C29  'Divide powers of the same base: subtract the exponents'  [obj O28]  media=['IMG1', 'VID1']  refs=['2.3.two100_two25', '2.3.quotient_law', '2.3.mt_n_not_zero']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: From this we can see that 2⁴ ÷ 2³ is 2 to the power 4 − 3, which is 2 to the power 1. What is 2 to the power 100 ÷ 2 to the power 25 in powers of 2? In a generalised form
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: is 2 to the power 100 ÷ 2 to the power 25 equal to 2⁴ or to 2 to the power 75? 2. Each factor below the bar cancels one factor above it, so the count le
   b2 worked_example/None refs=['2.3.two100_two25', '2.3.quotient_law', '2.3.mt_n_not_zero'] steps=4 video=VID1  Q: Write 2 to the power 100 ÷ 2 to the power 25 as a power of 2, and explain why the rule needs n ≠ 0.
C M4.S10.T10.C30  'Practice: divide powers'  [obj O29]  media=['IMG1', 'VID1', '2D1']  refs=['FiO2.q1']
   b0 recap/None refs=[] steps=0 video=-  Q: Divide powers of the same base by subtracting the exponents. Rewrite bases so that both powers have the same base first.
   b1 exercise/None refs=[] steps=4 video=VID1  Q: Find out the units digit in the value of 2 to the power 224 ÷ 4 to the power 32. Hint: 4 is 2².

## M4.S11.T11  Zero and Negative Exponents  [CONCEPT TOPIC]
C M4.S11.T11.C31  'Why a power with exponent 0 is 1'  [obj O30]  media=['IMG1', 'VID1']  refs=['2.3.zero_exponent']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: We have not covered the case when the exponent is 0; for example, what is 2 to the power 0? Let us define 2 to the power 0 in a way that the generalised form above holds 
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: is 2 to the power 0 equal to 0, to 1, or to 2? 2. Any number divided by itself is 1, so 2⁴ ÷ 2⁴ is 1. 3. The rule says 2⁴ ÷ 2⁴ is 2 to the power 4 − 4, 
   b2 worked_example/None refs=['2.3.zero_exponent'] steps=4 video=VID1  Q: Use 2⁴ ÷ 2⁴ to decide the value of 2 to the power 0, and then find 5 to the power 0 and 10 to the power 0.
C M4.S11.T11.C32  'Halving past 1: negative exponents'  [obj O31]  media=['IMG1', 'VID1']  refs=['2.3.neg_halving']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: When Zero is in Power! When a line of length 2⁴ units is halved 5 times, 2⁴ ÷ 2 to the power 5 gives 1/2 units. Using the generalised form, we get 2⁴ ÷ 2 to the power 5 a
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: if a 16-unit line is halved 5 times, is any of it left? 2. Halving 4 times reaches 1 unit; a fifth halving gives half a unit. 3. The rule gives 2 to the
   b2 worked_example/None refs=['2.3.neg_halving'] steps=4 video=VID1  Q: A line is 16 units long. Find its length after halving it 5 times and 10 times, as a fraction and as a power of 2.
C M4.S11.T11.C33  'Negative powers are reciprocals'  [obj O32]  media=['IMG1', 'VID1']  refs=['2.3.reciprocal', '2.3.mt_integers']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Similarly, 10 to the power −3 is 1/10³, 7 to the power −2 is 1/7², etc. Can we write 10³ as 1 over 10 to the power −3? We can write 1 over 10 to the power −3 as 1 ÷ (1/10
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: is 10 to the power −3 a negative number? 2. 10 to the power −3 is 1 over 10³, which is 1/1000, a small positive number. 3. Dividing 1 by 1/1000 gives 10
   b2 worked_example/None refs=['2.3.reciprocal', '2.3.mt_integers'] steps=4 video=VID1  Q: Write 10 to the power −3 and 7 to the power −2 as fractions, show that 1 over 10 to the power −3 is 10³, and check the product rule with exponents 3 and −1.
C M4.S11.T11.C34  'Write negative powers as fractions'  [thin-extra, obj O33]  media=['IMG1', 'VID1']  refs=['2.3.equiv_forms']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Write equivalent forms of the following. (i) 2 to the power −4 (ii) 10 to the power −5 (iii) (−7) to the power −2 (iv) (−5) to the power −3 (v) 10 to the power −100
   b1 teaching_plan/None refs=[] steps=3 video=-  Q: 1. Predict first: is (−5) to the power −3 positive or negative? 2. A negative exponent flips to the denominator: n to the power −a is 1 over n to the power a. 3. The sign
   b2 worked_example/None refs=['2.3.equiv_forms'] steps=5 video=VID1  Q: Write 2 to the power −4, 10 to the power −5, (−7) to the power −2, (−5) to the power −3 and 10 to the power −100 in equivalent forms.
C M4.S11.T11.C35  'Simplify products with integer exponents'  [thin-extra, obj O34]  media=['IMG1', 'VID1']  refs=['2.3.simplify']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Simplify and write the answers in exponential form. (i) 2 to the power −4 × 2 to the power 7 (ii) 3² × 3 to the power −5 × 3 to the power 6 (iii) p³ × p to the power −10 
   b1 teaching_plan/None refs=[] steps=3 video=-  Q: 1. Predict first: is 2 to the power −4 × 2 to the power 7 equal to 2³ or to 2 to the power −28? 2. The product rule still adds exponents when some are negative: −4 + 7 = 
   b2 worked_example/None refs=['2.3.simplify'] steps=5 video=VID1  Q: Simplify: 2 to the power −4 × 2 to the power 7; 3² × 3 to the power −5 × 3 to the power 6; p³ × p to the power −10; 2⁴ × (−4) to the power −2; 8 to the power p × 8 to the
C M4.S11.T11.C36  'Practice: zero and negative exponents'  [obj O35]  media=['IMG1', 'VID1', '2D1']  refs=['FiO2.q5']
   b0 recap/None refs=[] steps=0 video=-  Q: n to the power 0 is 1 and n to the power −a is 1 over n to the power a, for n ≠ 0. The product, quotient and power of a power rules work for all integer exponents.
   b1 exercise/None refs=[] steps=5 video=VID1  Q: Simplify and write these in the exponential form. (i) 10 to the power −2 × 10 to the power −5 (ii) 5 to the power 7 ÷ 5⁴ (iii) 9 to the power −7 ÷ 9⁴ (iv) (13 to the powe

## M4.S12.T12  Questions: Zero and Negative Exponents  [QUESTIONS TOPIC (follows M4.S11.T11)]
C M4.S12.T12.C37  'Power Play, Q3'  [obj O36]  media=['VID1']  refs=['FiO2.q3']
   b0 exercise/figure_it_out refs=[] steps=3 video=VID1  Q: Write the given number as the product of two or more powers in three different ways. The powers can be any integers. (i) 64³ (ii) 192 to the power 8 (iii) 32 to the power

## M4.S13.T13  Power Lines  [CONCEPT TOPIC]
C M4.S13.T13.C38  'The power line of 4'  [obj O37]  media=['IMG1', 'VID1']  refs=['2.3.power_line4']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Power Lines Let us arrange the powers of 4 along a line. 4 to the power 8 is 65536, 4 to the power 7 is 16384, 4 to the power 6 is 4096, 4 to the power 5 is 1024, 4⁴ is 2
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: is 65536 ÷ 64 a power of 4? 2. Each step up the line multiplies by 4; each step down divides by 4. 3. 65536 is 4 to the power 8 and 64 is 4³: dividing m
   b2 worked_example/None refs=['2.3.power_line4'] steps=4 video=VID1  Q: Use the power line of 4 to find 65536 ÷ 64, 64 × 16 and 16384 ÷ 16 as powers of 4.
C M4.S13.T13.C39  'How many times larger?'  [obj O38]  media=['IMG1', 'VID1']  refs=['2.3.times_larger']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Can we say that 16384 (4 to the power 7) is 16 (4²) times larger than 1024 (4 to the power 5)? Yes, since 4 to the power 7 ÷ 4 to the power 5 is 4². How many times larger
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: is 4² four times larger than 4 to the power −2, or many more times? 2. How many times larger is a quotient: divide the larger power by the smaller one. 
   b2 worked_example/None refs=['2.3.times_larger'] steps=4 video=VID1  Q: Show that 16384 is 16 times 1024, and find how many times larger 4² is than 4 to the power −2.
C M4.S13.T13.C40  'Practice: use the power line of 7'  [obj O39]  media=['IMG1', 'VID1', '2D1']  refs=['2.3.power_line7']
   b0 recap/None refs=[] steps=0 video=-  Q: Write each number as a power of 7 first. Multiplying adds exponents and dividing subtracts them.
   b1 exercise/None refs=[] steps=6 video=VID1  Q: Use the power line for 7 to find: 2401 × 49, 49³, 343 × 2401, 16807 ÷ 49, 7 ÷ 343, 16807 ÷ 823543, 117649 × 1/343, and 1/343 × 1/343.

## M5.S14.T14  Powers of 10 and Scientific Notation  [CONCEPT TOPIC]
C M5.S14.T14.C41  'Expanded form with powers of 10'  [obj O40]  media=['IMG1', 'VID1']  refs=['2.4.expanded', '2.4.write_three', '2.4.decimal']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: 2.4 Powers of 10 We have used numbers like 10, 100, 1000, and so on when writing Indian numerals in an expanded form. For example, 47561 = (4 × 10000) + (7 × 1000) + (5 ×
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: which power of 10 goes with the 4 in 47561? 2. Each place value is a power of 10: ones 10 to the power 0, tens 10 to the power 1, hundreds 10², and so o
   b2 worked_example/None refs=['2.4.expanded', '2.4.write_three', '2.4.decimal'] steps=5 video=VID1  Q: Write 5642 in expanded form with powers of 10, and write 561.903 using powers of 10.
C M5.S14.T14.C42  'Scientific notation for very large numbers'  [obj O41]  media=['IMG1', 'VID1']  refs=['2.4.facts', '2.4.5900', '2.4.write_facts', '2.4.sci_form']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Scientific Notation Let's look at some facts involving large numbers: (i) The Sun is located 300000000000000000000 m from the centre of our Milky Way galaxy. (ii) The num
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: how many zeroes does the mass of the Earth have, and could you read it aloud? 2. Move the decimal point until one nonzero digit is left before it, and c
   b2 worked_example/None refs=['2.4.facts', '2.4.5900', '2.4.write_facts', '2.4.sci_form'] steps=4 video=VID1  Q: Write 5900 in four ways using powers of 10, and write the three large-number facts in scientific notation.
C M5.S14.T14.C43  'The exponent matters more than the coefficient'  [obj O42]  media=['IMG1', 'VID1']  refs=['2.4.mumbai_kohima', '2.4.comic']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Often, the exponent y is more important than the coefficient x. When we write the 2 crore population of Mumbai as 2 × 10 to the power 7, the 7 is more important than the 
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: which change makes Mumbai's population bigger, changing the 2 to a 3 or the 7 to an 8? 2. Changing the coefficient from 2 to 3 adds half again: 2 crore 
   b2 worked_example/None refs=['2.4.mumbai_kohima', '2.4.comic'] steps=4 video=VID1  Q: Mumbai's population is about 2 × 10 to the power 7. Compare changing the coefficient to 3 with changing the exponent to 8. Then write Kohima's population of about 1 lakh 
C M5.S14.T14.C44  'Comparing distances in standard form'  [thin-extra, obj O43]  media=['IMG1', 'VID1']  refs=['2.4.distances', '2.4.mark_earth']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: The distance between the Sun and Saturn is 1433500000000 m, which is 1.4335 × 10 to the power 12 m. The distance between Saturn and Uranus is 1439000000000 m, which is 1.
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: 1.496 has the biggest coefficient, so is the Sun to Earth distance the largest? 2. Compare exponents first: 10 to the power 11 is one tenth of 10 to the
   b2 worked_example/None refs=['2.4.distances', '2.4.mark_earth'] steps=4 video=VID1  Q: Which is the smallest of the distances Sun to Saturn (1.4335 × 10 to the power 12 m), Saturn to Uranus (1.439 × 10 to the power 12 m) and Sun to Earth (1.496 × 10 to the 
C M5.S14.T14.C45  'Write numbers in standard form'  [thin-extra, obj O44]  media=['IMG1', 'VID1']  refs=['2.4.standard_form']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Express the following numbers in standard form. (i) 59853 (ii) 65950 (iii) 3430000 (iv) 70040000000
   b1 teaching_plan/None refs=[] steps=3 video=-  Q: 1. Predict first: what is the exponent of 10 for 3430000? 2. Place the point after the first digit and count the digits after it. 3. Drop zeroes at the end of the coeffic
   b2 worked_example/None refs=['2.4.standard_form'] steps=4 video=VID1  Q: Write 59853, 65950, 3430000 and 70040000000 in standard form.
C M5.S14.T14.C46  'Practice: compare powers and numbers in standard form'  [obj O45]  media=['IMG1', 'VID1', '2D1']  refs=['FiO2.q8']
   b0 recap/None refs=[] steps=0 video=-  Q: Compare numbers in standard form by the exponent first, then by the coefficient. A bigger base does not always mean a bigger power.
   b1 exercise/None refs=[] steps=4 video=VID1  Q: Identify the greater number in each of the following: (i) 4³ or 3⁴ (ii) 2 to the power 8 or 8² (iii) 100² or 2 to the power 100

## M5.S15.T15  Questions: Powers of 10 and Scientific Notation  [QUESTIONS TOPIC (follows M5.S14.T14)]
C M5.S15.T15.C47  'Power Play, Q6'  [obj O46]  media=['VID1']  refs=['FiO2.q6']
   b0 exercise/figure_it_out refs=[] steps=4 video=VID1  Q: If 12² = 144, what is (i) (1.2)² (ii) (0.12)² (iii) (0.012)² (iv) 120²?
C M5.S15.T15.C48  'Power Play, Q12'  [obj O47]  media=['VID1']  refs=['FiO2.q12']
   b0 exercise/figure_it_out refs=[] steps=4 video=VID1  Q: The worldwide population of sheep (2024) is about 10 to the power 9, and that of goats is also about the same. What is the total population of sheep and goats? (i) 20 to 
C M5.S15.T15.C49  'In a game, each player has 10 seconds to write the larger number. Roxi...'  [obj O48]  media=['VID1']  refs=['tremendous_ten']
   b0 exercise/unsolved refs=[] steps=4 video=VID1  Q: In a game, each player has 10 seconds to write the larger number. Roxie wrote 10000000000000 and Estu wrote 999999 × 999999. Whose number is greater? In Round 2, Roxie wr

## M6.S16.T16  Did You Ever Wonder? Guess, Model, Estimate  [CONCEPT TOPIC]
C M6.S16.T16.C50  'Tulabhara: worth of an offering'  [obj O49]  media=['IMG1', 'VID1']  refs=['2.5.tulabhara']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: 2.5 Did You Ever Wonder? Nanjundappa wants to donate jaggery equal to Roxie's weight and wheat equal to Estu's weight. He is wondering how much it would cost. Worth of ja
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: will the jaggery cost hundreds, thousands or lakhs of rupees? 2. Write the relationship in words: worth is weight in kg times the cost of 1 kg. 3. Assum
   b2 worked_example/None refs=['2.5.tulabhara'] steps=4 video=VID1  Q: Estimate the worth of jaggery equal to Roxie's weight and wheat equal to Estu's weight.
C M6.S16.T16.C51  'Coins equal to a weight'  [obj O50]  media=['IMG1', 'VID1']  refs=['2.5.coins_weight', '2.5.coins_notes']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Roxie wonders, "Instead of jaggery if we use 1-rupee coins, how many coins are needed to equal my weight?" 1. Guessing: Make an instinctive guess of what the answer could
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: are the coins in hundreds, thousands, lakhs or crores? 2. Number of coins is Roxie's weight divided by the weight of one coin. 3. Assume a 1-rupee coin 
   b2 worked_example/None refs=['2.5.coins_weight', '2.5.coins_notes'] steps=4 video=VID1  Q: About how many 1-rupee coins weigh as much as Roxie, if she weighs 45 kg and a coin weighs about 4 g?
C M6.S16.T16.C52  'Long walks: padayatra and walking around the Earth'  [thin-extra, obj O51]  media=['IMG1', 'VID1']  refs=['2.5.mt_donations', '2.5.padayatra', '2.5.circumnavigate']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Estu says, "When I become an adult, I would like to donate notebooks worth my weight every year". Roxie says, "When I grow up, I would like to do annadana worth my weight
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: could one person walk around the Earth once in a lifetime, ten times, or a hundred times? 2. Assume a walking pace of about 5 km an hour and a life of a
   b2 worked_example/None refs=['2.5.mt_donations', '2.5.padayatra', '2.5.circumnavigate'] steps=4 video=VID1  Q: A group walked about 400 km. If they walked about 25 km a day, how long ago did they start? How many times could a person walk around the 40000 km Earth in 70 years of no
C M6.S16.T16.C53  'Linear growth versus exponential growth'  [obj O52]  media=['IMG1', 'VID1']  refs=['2.5.ladder', '2.5.linear_exp_examples']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Linear Growth vs. Exponential Growth Roxie tells Estu about a science-fiction novel where they build a ladder to reach the moon: "I wonder if we actually had a ladder lik
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: would a ladder to the Moon have thousands, lakhs, crores or more steps? 2. Each step adds the same 20 cm, so the number of steps is distance divided by 
   b2 worked_example/None refs=['2.5.ladder', '2.5.linear_exp_examples'] steps=4 video=VID1  Q: How many 20 cm steps would a ladder to the Moon, 384400 km away, have? Compare it with folding paper.
C M6.S16.T16.C54  'Practice: model and estimate'  [obj O53]  media=['IMG1', 'VID1']  refs=['FiO2.q2']
   b0 recap/None refs=[] steps=0 video=-  Q: Guess first, then write how the quantities are related. A fixed amount added each day is linear growth.
   b1 exercise/None refs=[] steps=3 video=VID1  Q: There are 5 bottles in a container. Every day, a new container is brought in. How many bottles would there be after 40 days?

## M6.S17.T17  Getting a Sense for Large Numbers  [CONCEPT TOPIC]
C M6.S17.T17.C55  'Populations as powers of 10'  [obj O54]  media=['IMG1', 'VID1']  refs=['2.5.lakh_crore_arab', '2.5.species', '2.5.starling_mosquito', '2.5.per_elephant']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Getting a Sense for Large Numbers A lakh is 10 to the power 5 (100000), a crore is 10 to the power 7 (10000000), and an arab is 10 to the power 9, whereas a million is 10
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: are there more starlings or more people in the world? 2. 1.3 billion starlings is 1.3 × 10 to the power 9; people are 8.2 × 10 to the power 9, so more p
   b2 worked_example/None refs=['2.5.lakh_crore_arab', '2.5.species', '2.5.starling_mosquito', '2.5.per_elephant'] steps=4 video=VID1  Q: Write the starling and mosquito populations in scientific notation, and check that there are about 20000 people for every African elephant.
C M6.S17.T17.C56  'Calculating with numbers in scientific notation'  [obj O55]  media=['IMG1', 'VID1']  refs=['2.5.calc_four']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: The estimated population of ants globally is 20 padma or 20 quadrillion (2 × 10 to the power 16). The estimated number of trees (2023) globally stands at 3 trillion (3 × 
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: are there more ants per person or more leaves per tree? 2. To divide, divide the coefficients and subtract the exponents; to multiply, multiply and add.
   b2 worked_example/None refs=['2.5.calc_four'] steps=4 video=VID1  Q: Find, in scientific notation, the ants per human, the flocks of 10000 starlings, the leaves on all trees, and the sheets of paper (0.001 cm thick) needed to reach the Moo
C M6.S17.T17.C57  'A different way to say your age'  [thin-extra, obj O56]  media=['IMG1', 'VID1']  refs=['2.5.age_hours', '2.5.age_puzzle', '2.5.estu_birth', '2.5.million_seconds']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: A different way to say your age! "I'm 4840 days old today!" said Roxie. "I'm ______ hours old!" said Roxie. Make an estimate before finding this number. Roxie says, "I am
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: is a million seconds a few days, a few months or a few years? 2. Hours: 4840 days × 24 hours a day is 116160 hours. 3. 6970710 is too big for hours; in 
   b2 worked_example/None refs=['2.5.age_hours', '2.5.age_puzzle', '2.5.estu_birth', '2.5.million_seconds'] steps=4 video=VID1  Q: Roxie is 4840 days old. Find her age in hours, decide what unit 6970710 is in, find Estu's age in years for 4070 days, and find how many days a million seconds is.
C M6.S17.T17.C58  'A time scale in powers of 10 seconds'  [obj O57]  media=['IMG1', 'VID1']  refs=['2.5.time_table', '2.5.events_order', '2.5.terror_plants', '2.5.try_stars_water']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Time in seconds, compared to real-world events: 10 to the power 0 seconds, time taken for a ball thrown up to fall back; 10 to the power 1 seconds, time blood takes to co
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: is 10 to the power 9 seconds closer to a month, a year or a lifetime? 2. A year is about 3.15 × 10 to the power 7 seconds, so multiply years by that. 3.
   b2 worked_example/None refs=['2.5.time_table', '2.5.events_order', '2.5.terror_plants', '2.5.try_stars_water'] steps=4 video=VID1  Q: Convert 15 million years to seconds. How long would it take to count 2 × 10 to the power 23 stars at one per second, and to drink 2 × 10 to the power 25 drops of water (1
C M6.S17.T17.C59  'Practice: large numbers in scientific notation'  [obj O58]  media=['IMG1', 'VID1', '2D1']  refs=['FiO2.q13']
   b0 recap/None refs=[] steps=0 video=-  Q: Multiply coefficients and add exponents; then put the answer in standard form. A day has 86400 seconds and a year about 3.15 × 10 to the power 7 seconds.
   b1 exercise/None refs=[] steps=4 video=VID1  Q: Calculate and write the answer in scientific notation: (i) If each person in the world had 30 pieces of clothing, find the total number of pieces of clothing. (ii) There 

## M6.S18.T18  Questions: Getting a Sense for Large Numbers  [QUESTIONS TOPIC (follows M6.S17.T17)]
C M6.S18.T18.C60  'Power Play, Q14'  [obj O59]  media=['VID1']  refs=['FiO2.q14']
   b0 exercise/figure_it_out refs=[] steps=4 video=VID1  Q: What was the date 1 arab or 1 billion seconds ago?

## M6.S19.T19  A Pinch of History: Names for Powers of 10  [CONCEPT TOPIC]
C M6.S19.T19.C61  'Indian names for powers of 10'  [obj O60]  media=['IMG1', 'VID1']  refs=['hist.lalitavistara', 'hist.indian_names']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: 2.5 A Pinch of History In the Lalitavistara, a Buddhist treatise from the first century BCE, we see number-names for odd powers of ten up to 10 to the power 53. "Hundred 
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: how many zeroes does a crore have, and how many does an arab have? 2. Each new Indian name is a hundred of the previous one, so multiply by 10². 3. Mult
   b2 worked_example/None refs=['hist.lalitavistara', 'hist.indian_names'] steps=4 video=VID1  Q: Starting from a lakh as 10² × 10³, find the powers of 10 for a crore, an arab, a kharab and a neel.
C M6.S19.T19.C62  'International names, googol and googolplex'  [obj O61]  media=['IMG1', 'VID1']  refs=['hist.western_names', 'hist.googol_notes']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: In the American or International system, we say: A thousand thousand is a million, 10³ × 10³ is 10 to the power 6. A thousand million is a billion, 10³ × 10 to the power 
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: is a googol more or less than the number of atoms in the universe? 2. Each international name is a thousand of the previous one, so multiply by 10³ and 
   b2 worked_example/None refs=['hist.western_names', 'hist.googol_notes'] steps=4 video=VID1  Q: Find the powers of 10 for a billion, a trillion and a quintillion, and compare a googol with the number of atoms in the universe.
C M6.S19.T19.C63  'Practice: decode the number names'  [obj O62]  media=['IMG1', 'VID1']  refs=['hist.first_part']
   b0 recap/None refs=[] steps=0 video=-  Q: International names step up by 1000, adding 3 to the exponent. Indian names step up by 100, adding 2 to the exponent.
   b1 exercise/None refs=[] steps=4 video=VID1  Q: Observe the names million (10 to the power 6), billion (10 to the power 9), trillion (10 to the power 12), quadrillion (10 to the power 15), quintillion (10 to the power 

## M6.S20.T20  Summary: Power Play  [SUMMARY]
C M6.S20.T20.C64  'What powers did in this chapter'  [obj O63]  media=['IMG1']  refs=['summary']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: We analysed some situations, asked questions, and found answers by first guessing, then modelling the problem statement, followed by making assumptions and approximations
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Our opening question is settled: 46 folds of a 0.001 cm sheet give about 7 lakh km, beyond the Moon. 2. A power counts factors; the rules for exponents come from count

## Book items the plan covers (coverage id -> concept)

- FiO1.q1 -> M2.S3.T3.C10
- FiO1.q2 -> M2.S4.T4.C11
- FiO1.q3 -> M2.S4.T4.C12
- FiO2.q1 -> M4.S10.T10.C30
- FiO2.q2 -> M6.S16.T16.C54
- FiO2.q3 -> M4.S12.T12.C37
- FiO2.q4 -> M3.S5.T5.C17
- FiO2.q5 -> M4.S11.T11.C36
- FiO2.q6 -> M5.S15.T15.C47
- FiO2.q7 -> M3.S7.T7.C22
- FiO2.q8 -> M5.S14.T14.C46
- FiO2.q9 -> M3.S9.T9.C27
- summary -> M6.S20.T20.C64
- 2.2.p4p6 -> M3.S5.T5.C14
- 2.4.5900 -> M5.S14.T14.C42
- FiO2.q10 -> M3.S6.T6.C18
- FiO2.q11 -> M3.S8.T8.C26
- FiO2.q12 -> M5.S15.T15.C48
- FiO2.q13 -> M6.S17.T17.C59
- FiO2.q14 -> M6.S18.T18.C60
- 2.1.intro -> M1.S1.T1.C1
- 2.4.comic -> M5.S14.T14.C43
- 2.4.facts -> M5.S14.T14.C42
- 2.5.ladder -> M6.S16.T16.C53
- 2.1.table17 -> M1.S2.T2.C2
- 2.2.letters -> M2.S3.T3.C9
- 2.4.decimal -> M5.S14.T14.C41
- 2.5.species -> M6.S17.T17.C55
- 2.1.mt_guess -> M1.S2.T2.C3
- 2.2.neg_base -> M2.S3.T3.C8
- 2.2.pond_exp -> M3.S7.T7.C19
- 2.3.simplify -> M4.S11.T11.C35
- 2.4.expanded -> M5.S14.T14.C41
- 2.4.sci_form -> M5.S14.T14.C42
- 2.1.ten_folds -> M1.S2.T2.C4
- 2.1.two_folds -> M1.S2.T2.C4
- 2.2.damayanti -> M3.S7.T7.C20
- 2.2.four_pow6 -> M3.S5.T5.C15
- 2.2.neg2_pow4 -> M2.S3.T3.C8
- 2.2.pond_half -> M3.S7.T7.C19
- 2.2.try_codes -> M3.S8.T8.C25
- 2.4.distances -> M5.S14.T14.C44
- 2.5.age_hours -> M6.S17.T17.C57
- 2.5.calc_four -> M6.S17.T17.C56
- 2.5.padayatra -> M6.S16.T16.C52
- 2.5.tulabhara -> M6.S16.T16.C50
- 2.1.fill_table -> M1.S2.T2.C5
- 2.2.fold_power -> M2.S3.T3.C6
- 2.2.order_swap -> M3.S7.T7.C20
- 2.3.reciprocal -> M4.S11.T11.C33
- 2.4.mark_earth -> M5.S14.T14.C44
- 2.5.age_puzzle -> M6.S17.T17.C57
- 2.5.estu_birth -> M6.S17.T17.C57
- 2.5.time_table -> M6.S17.T17.C58
- tremendous_ten -> M5.S15.T15.C49
- 2.1.three_folds -> M1.S2.T2.C4
- 2.2.add_vs_mult -> M2.S3.T3.C7
- 2.2.letter_lock -> M3.S8.T8.C25
- 2.2.lock_2digit -> M3.S8.T8.C24
- 2.2.lock_3digit -> M3.S8.T8.C24
- 2.2.lock_5digit -> M3.S8.T8.C24
- 2.2.mt_two_ways -> M3.S5.T5.C16
- 2.2.neg1_powers -> M2.S3.T3.C8
- 2.2.prime_32400 -> M2.S3.T3.C9
- 2.2.product_law -> M3.S5.T5.C14
- 2.2.read_powers -> M2.S3.T3.C6
- 2.2.ten_folds_v -> M2.S3.T3.C7
- 2.2.why_3p2_3p5 -> M3.S5.T5.C14
- 2.2.zero_powers -> M2.S3.T3.C8
- 2.3.equiv_forms -> M4.S11.T11.C34
- 2.3.mt_integers -> M4.S11.T11.C33
- 2.3.neg_halving -> M4.S11.T11.C32
- 2.3.power_line4 -> M4.S13.T13.C38
- 2.3.power_line7 -> M4.S13.T13.C40
- 2.4.write_facts -> M5.S14.T14.C42
- 2.4.write_three -> M5.S14.T14.C41
- 2.5.coins_notes -> M6.S16.T16.C51
- hist.first_part -> M6.S19.T19.C63
- 2.1.burj_mariana -> M1.S2.T2.C3
- 2.2.dresses_caps -> M3.S8.T8.C23
- 2.2.same_exp_law -> M3.S7.T7.C20
- 2.2.seven4_two10 -> M3.S5.T5.C15
- 2.2.stones_rooms -> M3.S5.T5.C13
- 2.3.halving_line -> M4.S10.T10.C28
- 2.3.quotient_law -> M4.S10.T10.C29
- 2.3.times_larger -> M4.S13.T13.C39
- 2.3.two100_two25 -> M4.S10.T10.C29
- 2.5.coins_weight -> M6.S16.T16.C51
- 2.5.events_order -> M6.S17.T17.C58
- 2.5.mt_donations -> M6.S16.T16.C52
- 2.5.per_elephant -> M6.S17.T17.C55
- 2.2.base_exponent -> M2.S3.T3.C6
- 2.2.compute_three -> M3.S5.T5.C14
- 2.2.roxie_outfits -> M3.S8.T8.C23
- 2.3.mt_n_not_zero -> M4.S10.T10.C29
- 2.3.zero_exponent -> M4.S11.T11.C31
- 2.4.mumbai_kohima -> M5.S14.T14.C43
- 2.4.standard_form -> M5.S14.T14.C45
- 2.5.terror_plants -> M6.S17.T17.C58
- hist.googol_notes -> M6.S19.T19.C62
- hist.indian_names -> M6.S19.T19.C61
- 2.2.power_of_power -> M3.S5.T5.C15
- 2.5.circumnavigate -> M6.S16.T16.C52
- hist.lalitavistara -> M6.S19.T19.C61
- hist.western_names -> M6.S19.T19.C62
- 2.2.compute_2p5_5p5 -> M3.S7.T7.C20
- 2.2.stones_diamonds -> M3.S5.T5.C13
- 2.5.lakh_crore_arab -> M6.S17.T17.C55
- 2.5.million_seconds -> M6.S17.T17.C57
- 2.5.try_stars_water -> M6.S17.T17.C58
- 2.2.quotient_same_exp -> M3.S7.T7.C21
- 2.2.simplify_10p4_5p4 -> M3.S7.T7.C21
- 2.5.starling_mosquito -> M6.S17.T17.C55
- 2.5.linear_exp_examples -> M6.S16.T16.C53
