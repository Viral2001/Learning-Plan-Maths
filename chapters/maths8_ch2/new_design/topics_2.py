# -*- coding: utf-8 -*-
"""Topics T4 to T9 (modules M3 and M4). Book section 2.2 from The Stones that Shine, and section 2.3, pp 23 to 30,
with the Figure it Out questions on these ideas homed in the doers."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T4 Multiplying powers of the same base =====================================
TOPICS.append(TOPIC(
    "T4", "M3", "Multiplying Powers of the Same Base", ["2.2"], "Apply",
    "Students count the stones in the story by repeated multiplication, multiply powers of the same base by adding "
    "exponents, and write a power of a power by multiplying exponents, checking each rule by expanding the factors.",
    "Joining strips of factors adds the counts, so n to the power a times n to the power b is n to the power a + b; "
    "repeating a power b times multiplies the exponents.",
    [A("T4.C1", "The Stones that Shine: counting by powers of 3", "Apply",
       "Students follow the king's 3 daughters, baskets, keys and rooms, find that there are 3 to the power 4 rooms "
       "and 3 to the power 7 diamonds, and compute both by repeated multiplication.",
       textbook=["The Stones that Shine",
                 "Once upon a time, there lived a king who had 3 daughters. Each daughter had 3 baskets, each basket "
                 "had 3 keys, each key opened 3 rooms, each room had 3 tables, each table had 3 necklaces, and each "
                 "necklace had 3 diamonds.",
                 "How many rooms were there? The number of rooms is 3 × 3 × 3 × 3 = 3⁴. This can be computed by "
                 "repeatedly multiplying 3 by itself: 3 × 3 = 9, 9 × 3 = 27, 27 × 3 = 81.",
                 "How many diamonds were there in total? Can we find out by just one multiplication using the products "
                 "above?",
                 "The number of diamonds is 3 × 3 × 3 × 3 × 3 × 3 × 3, which is 3 to the power 7."],
       teach=["Predict first: are there a few hundred diamonds or a few thousand?",
              "Each level multiplies by 3: daughters 3, baskets 9, keys 27, rooms 81, so the rooms are 3⁴.",
              "Three more levels, tables, necklaces and diamonds, multiply by 3 three more times.",
              "Instead of seven multiplications, multiply the 81 rooms by 27, the diamonds in each room."],
       examples=[
           WE("In the story, find the number of rooms and the number of diamonds.",
              ["Daughters 3, baskets 3 × 3 = 9, keys 9 × 3 = 27, rooms 27 × 3 = 81, so 3⁴ rooms.",
               "Each room has 3 × 3 × 3 = 27 diamonds, which is 3³.",
               "Diamonds: 81 × 27 = 2187, which is seven 3s multiplied together.",
               "Check another way: 9 × 243 = 2187."],
              "81 rooms and 2187 diamonds",
              ncert=["2.2.stones_rooms", "2.2.stones_diamonds"])],
       key_terms=["repeated multiplication", "stones", "diamonds"], misconceptions=["M_POW_TIMES"], minutes=10),
     A("T4.C2", "Multiply powers of the same base: add the exponents", "Apply",
       "Students regroup seven 3s into two powers of the same base in two ways, multiply p to the power 4 by "
       "p to the power 6 by adding the exponents, and compute three powers.",
       textbook=["We can write 3 to the power 7 as (3 × 3 × 3 × 3) × (3 × 3 × 3) = 3⁴ × 3³ = 81 × 27 = 2187.",
                 "3 to the power 7 can also be written as 3² × 3 to the power 5. Can you reason out why?",
                 "Write the product p⁴ × p to the power 6 in exponential form. "
                 "p⁴ × p to the power 6 = (p × p × p × p) × (p × p × p × p × p × p) = p to the power 10.",
                 "We can generalise this to: n to the power a × n to the power b = n to the power a + b, where a and b "
                 "are counting numbers.",
                 "Use this observation to compute the following. (i) 2 to the power 9 (ii) 5 to the power 7 "
                 "(iii) 4 to the power 6"],
       teach=["Predict first: is p⁴ × p to the power 6 equal to p to the power 10 or p to the power 24?",
              "Write out the factors: four p's then six p's in one row make ten p's.",
              "So multiplying powers of the same base adds the exponents; the base stays the same.",
              "Use it to compute big powers from small ones you know."],
       examples=[
           WE("Write p⁴ × p to the power 6 as one power, and compute 2 to the power 9 and 5 to the power 7 by splitting "
              "the exponents.",
              ["Four p's and six p's joined make ten p's, so p⁴ × p to the power 6 is p to the power 10.",
               "2 to the power 9 is 2⁴ × 2 to the power 5: 16 × 32 = 512.",
               "5 to the power 7 is 5³ × 5⁴: 125 × 625 = 78125.",
               "The exponents add: 4 + 5 = 9 and 3 + 4 = 7."],
              "p to the power 10; 512; 78125",
              ncert=["2.2.why_3p2_3p5", "2.2.p4p6", "2.2.product_law", "2.2.compute_three"])],
       key_terms=["product", "exponents", "same base"], misconceptions=["M_ADD_EXP_MULT"], minutes=10),
     A("T4.C3", "A power of a power: multiply the exponents", "Apply",
       "Students evaluate 4 to the power 6 as the square of 4 cubed and as the cube of 4 squared, rewrite two "
       "more numbers as a power of a power, and state the rule.",
       textbook=["4 to the power 6 can be evaluated in these two ways: (4 × 4 × 4) × (4 × 4 × 4) = 4³ × 4³ = 64 × 64 = "
                 "4096, and (4 × 4) × (4 × 4) × (4 × 4) = 4² × 4² × 4² = 16 × 16 × 16 = 4096.",
                 "4³ × 4³ is the square of 4³, written (4³)². 4² × 4² × 4² is the cube of 4², written (4²)³.",
                 "Similarly, 7⁴ = (7 × 7) × (7 × 7) = 7² × 7² = (7²)², and 2 to the power 10 is (2²) to the power 5.",
                 "Is 2 to the power 10 also equal to (2 to the power 5)²? Write it as a product.",
                 "In general, (n to the power a) to the power b = (n to the power b) to the power a = n to the power "
                 "a × b, where a and b are counting numbers."],
       teach=["Predict first: is (4³)² equal to 4 to the power 5 or 4 to the power 6?",
              "(4³)² means two copies of 4³, that is two groups of three 4s, six 4s in all.",
              "So a power of a power multiplies the exponents: 3 × 2 = 6.",
              "The order does not matter: (4³)² and (4²)³ are both 4 to the power 6, which is 4096."],
       examples=[
           WE("Evaluate 4 to the power 6 in two ways, and check whether 2 to the power 10 equals (2 to the power 5)².",
              ["(4³)²: 4³ = 64 and 64 × 64 = 4096.",
               "(4²)³: 4² = 16 and 16 × 16 × 16 = 4096.",
               "2 to the power 10 is (2 × 2 × 2 × 2 × 2) × (2 × 2 × 2 × 2 × 2), two groups of five 2s.",
               "So 2 to the power 10 is (2 to the power 5)², and 32 × 32 = 1024."],
              "4096 both ways; yes, 2 to the power 10 is (2 to the power 5)², which is 1024",
              ncert=["2.2.four_pow6", "2.2.seven4_two10", "2.2.power_of_power"])],
       key_terms=["power of a power", "exponents"], misconceptions=["M_POWPOW_ADD"], minutes=10),
     A("T4.C4", "Write a power as a power of a power in two ways", "Apply",
       "Students write 8 to the power 6, 7 to the power 15, 9 to the power 14 and 5 to the power 8 as a power of a "
       "power in two different ways by splitting each exponent into two factors.",
       textbook=["Write the following expressions as a power of a power in at least two different ways: "
                 "(i) 8 to the power 6 (ii) 7 to the power 15 (iii) 9 to the power 14 (iv) 5 to the power 8"],
       teach=["Predict first: how many ways can the exponent 6 be split into two factors?",
              "Split the exponent as a product: 6 is 2 × 3 or 3 × 2.",
              "A base can also be rewritten: 8 is 2³, so 8 to the power 6 is a power of 2."],
       examples=[
           WE("Write 8 to the power 6, 7 to the power 15, 9 to the power 14 and 5 to the power 8 as a power of a power "
              "in two ways.",
              ["8 to the power 6 is (8²)³, and since 8 is 2³ it is also (2³) to the power 6, which is 2 to the power 18.",
               "7 to the power 15 is (7³) to the power 5 or (7 to the power 5)³.",
               "9 to the power 14 is (9²) to the power 7, and since 9 is 3² it is also (3²) to the power 14.",
               "5 to the power 8 is (5²)⁴ or (5⁴)²."],
              "For example (8²)³ and (2³) to the power 6; (7³) to the power 5 and (7 to the power 5)³; (9²) to the "
              "power 7 and (3²) to the power 14; (5²)⁴ and (5⁴)²",
              ncert=["2.2.mt_two_ways"])],
       key_terms=["power of a power"], misconceptions=["M_POWPOW_ADD"], minutes=6, thin=True),
     DOER("T4.C5", "Practice: products and powers of powers", "product_law_deriver", "Evaluate",
          "Students decide whether statements about squares, cubes and higher powers are always, sometimes or never "
          "true, and describe the numbers that are both squares and cubes as sixth powers.",
          ["Multiplying powers of the same base adds the exponents.",
           "A power of a power multiplies the exponents, in either order."],
          items=[
              FIO("FiO2.q4", "Figure it Out (power play, question 4)",
                  "Examine each statement and find out if it is Always True, Only Sometimes True, or Never True. "
                  "(i) Cube numbers are also square numbers. (ii) Fourth powers are also square numbers. (iii) The "
                  "fifth power of a number is divisible by the cube of that number. (iv) The product of two cube "
                  "numbers is a cube number. (v) q to the power 46 is both a 4th power and a 6th power (q is a prime "
                  "number).",
                  ["(i) 8 is a cube but not a square, while 64 is both: only sometimes true.",
                   "(ii) n⁴ is (n²)², so every fourth power is a square: always true.",
                   "(iii) n to the power 5 is n³ × n², so it is divisible by n³: always true.",
                   "(iv) a³ × b³ is (a × b)³, a cube: always true.",
                   "(v) A 4th power of a prime needs an exponent divisible by 4, and 46 is not: never true."],
                  "(i) Only sometimes true (ii) Always true (iii) Always true (iv) Always true (v) Never true"),
              FIO("FiO2.q10", "Figure it Out (power play, question 10)",
                  "64 is a square number (8²) and a cube number (4³). Are there other numbers that are both squares "
                  "and cubes? Is there a way to describe such numbers in general?",
                  ["A sixth power is both: n to the power 6 is (n³)² and also (n²)³.",
                   "64 is 2 to the power 6: (2³)² is 8² and (2²)³ is 4³.",
                   "729 is 3 to the power 6: 27² = 729 and 9³ = 729.",
                   "4096 is 4 to the power 6, which is 64² and 16³."],
                  "Yes, infinitely many: the sixth powers, such as 1, 64, 729 and 4096")],
          misconceptions=["M_ADD_EXP_MULT", "M_POWPOW_ADD"])],
    key_terms=["product", "power of a power", "exponents"]))

# ============================== T5 Powers with the same exponent ===========================================
TOPICS.append(TOPIC(
    "T5", "M3", "Same Exponent, Different Bases", ["2.2"], "Apply",
    "Students use doubling to find when the magical pond was half covered, multiply powers with the same exponent "
    "by multiplying the bases, and divide powers with the same exponent by dividing the bases.",
    "When the exponents are the same, regroup the factors in pairs: m to the power a times n to the power a is "
    "(mn) to the power a, and m to the power a divided by n to the power a is (m over n) to the power a.",
    [A("T5.C1", "The magical pond: half covered the day before", "Analyze",
       "Students reason that a pond whose lotuses double every day and is full on day 30 was half covered on day 29, "
       "and write both counts in exponential form.",
       textbook=["Magical Pond",
                 "In the middle of a beautiful, magical pond lies a bright pink lotus. The number of lotuses doubles "
                 "every day in this pond. After 30 days, the pond is completely covered with lotuses. On which day "
                 "was the pond half full?",
                 "Since the number of lotuses doubles every day, the pond should be half covered on the 29th day.",
                 "Write the number of lotuses (in exponential form) when the pond was (i) fully covered "
                 "(ii) half covered"],
       teach=["Predict first: was the pond half covered on day 15 or on some other day?",
              "Work backwards: the lotuses double every day, so the day before full they were half.",
              "Starting from 1 lotus, after 30 doublings there are 2 to the power 30 lotuses.",
              "On day 29 there were 2 to the power 29, and 2 to the power 29 × 2 is 2 to the power 30."],
       examples=[
           WE("A pond starts with 1 lotus and the number doubles every day. It is full after 30 days. When was it "
              "half covered, and how many lotuses were there when full and when half covered?",
              ["Each day doubles the lotuses, so the day before full it was half: day 29, not day 15.",
               "Full after 30 doublings of 1 lotus: 2 to the power 30 lotuses.",
               "Half covered after 29 doublings: 2 to the power 29 lotuses.",
               "Check: doubling 2 to the power 29 gives 2 to the power 29 + 1, which is 2 to the power 30."],
              "Day 29; 2 to the power 30 lotuses when full and 2 to the power 29 when half covered",
              ncert=["2.2.pond_half", "2.2.pond_exp"])],
       key_terms=["doubling", "pond", "half"], misconceptions=["M_HALF_DAY"], minutes=8),
     A("T5.C2", "Multiply powers with the same exponent", "Apply",
       "Students count Damayanti's lotuses after 4 days of doubling and 4 days of tripling, show that the order "
       "does not change the count, and multiply powers with the same exponent by multiplying the bases.",
       textbook=["There is another pond in which the number of lotuses triples every day. When both the ponds had no "
                 "flowers, Damayanti placed a lotus in the doubling pond. After 4 days, she took all the lotuses from "
                 "there and put them in the tripling pond. How many lotuses will be in the tripling pond after 4 more "
                 "days?",
                 "After the first 4 days, the number of lotuses is 1 × 2 × 2 × 2 × 2 = 2⁴. After the next 4 days, the "
                 "number of lotuses is 2⁴ × 3 × 3 × 3 × 3 = 2⁴ × 3⁴.",
                 "What if Damayanti had changed the order in which she placed the flowers in the lakes?",
                 "By regrouping the numbers, (3 × 2) × (3 × 2) × (3 × 2) × (3 × 2) = (3 × 2)⁴ = 6⁴.",
                 "In general, m to the power a × n to the power a = (mn) to the power a, where a is a counting number.",
                 "Use this observation to compute the value of 2 to the power 5 × 5 to the power 5."],
       teach=["Predict first: if Damayanti uses the tripling pond first, will she end with more lotuses, fewer, or "
              "the same?",
              "Doubling 4 times gives 2⁴; tripling 4 more times gives 2⁴ × 3⁴, which is 16 × 81 = 1296.",
              "Swapping the order gives 3⁴ × 2⁴, the same factors, so the same 1296.",
              "Pair each 2 with a 3: four pairs of 6 make 6⁴, so when the exponents match, multiply the bases."],
       examples=[
           WE("Damayanti puts a lotus in the doubling pond for 4 days and then moves all the lotuses to the tripling "
              "pond for 4 days. Find the number of lotuses, and use the same idea to compute 2 to the power 5 × 5 to "
              "the power 5.",
              ["After 4 doubling days: 2⁴ = 16 lotuses.",
               "After 4 tripling days: 16 × 81 = 1296, which is 2⁴ × 3⁴.",
               "Pair each 2 with a 3: (2 × 3)⁴ = 6⁴, and 6 × 6 × 6 × 6 = 1296. Swapping the ponds gives the same.",
               "2 to the power 5 × 5 to the power 5 is (2 × 5) to the power 5, which is 10 to the power 5: "
               "32 × 3125 = 100000."],
              "1296 lotuses either way; 2 to the power 5 × 5 to the power 5 is 100000",
              ncert=["2.2.damayanti", "2.2.order_swap", "2.2.same_exp_law", "2.2.compute_2p5_5p5"])],
       key_terms=["same exponent", "bases", "multiply"], misconceptions=["M_ADD_EXP_MULT"], minutes=10),
     A("T5.C3", "Divide powers with the same exponent", "Apply",
       "Students simplify 10 to the power 4 divided by 5 to the power 4 by pairing each 10 with a 5, getting 2 to the "
       "power 4, which is 16, and state the rule for dividing powers with equal exponents.",
       textbook=["Simplify 10⁴ ÷ 5⁴ and write it in exponential form.",
                 "In general, we can show that m to the power a ÷ n to the power a = (m ÷ n) to the power a."],
       teach=["Predict first: is 10⁴ ÷ 5⁴ equal to 2, to 16, or to 2 to the power 0?",
              "Write it as a fraction with four 10s on top and four 5s below.",
              "Pair each 10 with a 5: each pair is 10 ÷ 5 = 2, and there are four pairs.",
              "So 10⁴ ÷ 5⁴ is 2⁴, which is 16."],
       examples=[
           WE("Simplify 10⁴ ÷ 5⁴ and write it in exponential form. Check by computing both powers.",
              ["10⁴ ÷ 5⁴ is (10 × 10 × 10 × 10) over (5 × 5 × 5 × 5).",
               "Pair each 10 with a 5: (10 ÷ 5) × (10 ÷ 5) × (10 ÷ 5) × (10 ÷ 5) = 2⁴.",
               "Check: 10⁴ is 10000 and 5⁴ is 625, and 10000 ÷ 625 = 16.",
               "2⁴ is also 16."],
              "2⁴, which is 16",
              ncert=["2.2.simplify_10p4_5p4", "2.2.quotient_same_exp"])],
       key_terms=["same exponent", "divide"], misconceptions=["M_DIV_EXP"], minutes=8),
     DOER("T5.C4", "Practice: spot equal products of powers", "pairing_bench", "Analyze",
          "Students rewrite products of powers on the prime bases 2 and 3 to decide which of five numbers written "
          "with exponents are the same number.",
          ["m to the power a times n to the power a is (mn) to the power a.",
           "Rewrite every number with prime bases to compare them."],
          items=[
              FIO("FiO2.q7", "Figure it Out (power play, question 7)",
                  "Circle the numbers that are the same: 2⁴ × 3 to the power 6, 6⁴ × 3², 6 to the power 10, 18² × 6², "
                  "6 to the power 24.",
                  ["Write each with the bases 2 and 3.",
                   "6⁴ × 3² is 2⁴ × 3⁴ × 3², which is 2⁴ × 3 to the power 6.",
                   "18² × 6² is (18 × 6)², and 108 is 2² × 3³, so 108² is 2⁴ × 3 to the power 6.",
                   "2⁴ × 3 to the power 6 is 16 × 729 = 11664.",
                   "6 to the power 10 is 2 to the power 10 × 3 to the power 10 and 6 to the power 24 is larger still, "
                   "so neither matches."],
                  "2⁴ × 3 to the power 6, 6⁴ × 3² and 18² × 6² are the same number, 11664")],
          misconceptions=["M_ADD_EXP_MULT"])],
    key_terms=["same exponent", "bases", "doubling"]))

# ============================== T6 Combinations ============================================================
TOPICS.append(TOPIC(
    "T6", "M3", "How Many Combinations?", ["2.2"], "Apply",
    "Students count outfits by multiplying the choices, count lock passwords as powers of 10 by solving simpler "
    "locks first, and count letter and alphanumeric codes as powers of 26 and 36.",
    "When each choice can be paired with every other choice, multiply: a lock with 5 digit slots has 10 to the power "
    "5 passwords, and 6 letter slots give 26 to the power 6.",
    [A("T6.C1", "Count outfits by multiplying the choices", "Apply",
       "Students count Estu's dress and cap combinations as 4 × 3, which is 12, using a tree of choices, and extend "
       "the idea to Roxie's dresses, hats and shoes.",
       textbook=["How Many Combinations",
                 "Estu has 4 dresses and 3 caps. How many different ways can Estu combine the dresses and caps?",
                 "For each cap, he can choose any of the 4 dresses, so for 3 caps, 4 + 4 + 4 = 4 × 3 = 12 combinations "
                 "are possible.",
                 "Roxie has 7 dresses, 2 hats, and 3 pairs of shoes. How many different ways can Roxie dress up?",
                 "Hint: Try drawing a diagram like the one above."],
       teach=["Predict first: does Estu have 7 outfits, 12, or some other number?",
              "Draw a tree: for each cap, every one of the 4 dresses can go with it, so 4 + 4 + 4 = 12.",
              "Adding the same number again and again is multiplying: 4 × 3 = 12.",
              "A third choice multiplies again: Roxie has 7 × 2 × 3 outfits."],
       examples=[
           WE("Estu has 4 dresses and 3 caps. Roxie has 7 dresses, 2 hats and 3 pairs of shoes. How many outfits can "
              "each make?",
              ["Each of Estu's 3 caps goes with each of 4 dresses: 4 + 4 + 4 = 12, which is 4 × 3.",
               "Roxie: each dress goes with each hat, giving 7 × 2 = 14 dress and hat pairs.",
               "Each of the 14 pairs goes with each of 3 pairs of shoes: 14 × 3 = 42."],
              "Estu has 12 outfits and Roxie has 42",
              ncert=["2.2.dresses_caps", "2.2.roxie_outfits"])],
       key_terms=["combinations", "choices"], misconceptions=["M_COMB_ADD"], minutes=8),
     A("T6.C2", "Lock passwords as powers of 10", "Apply",
       "Students count passwords for a 2-digit and a 3-digit lock by solving simpler locks first, and show that a "
       "5-digit lock has 10 to the power 5 passwords.",
       textbook=["Estu and Roxie came across a safe containing old stamps and coins that their great-grandfather had "
                 "collected. It was secured with a 5-digit password. They were unlucky and the lock only opened with "
                 "the last password. How many passwords did they end up checking?",
                 "Instead of a 5-digit lock, let us assume we have a 2-digit lock. There are 10 options for the first "
                 "digit (0 to 9). For each of these, there are 10 options for the second digit. Therefore the total "
                 "number of combinations for a 2-digit lock is 10 × 10 = 100.",
                 "Now, suppose we have a 3-digit lock. For each of the earlier 100 passwords there are 10 choices for "
                 "the third digit. So, there are 100 × 10 = 1000 combinations for a 3-digit lock.",
                 "If you can't solve a problem, try to find a simpler version of the problem that you can solve.",
                 "Each digit has 10 choices, so a 5-digit lock will have 10 × 10 × 10 × 10 × 10, which is 10 to the power 5, "
                 "passwords."],
       teach=["Predict first: does a 5-digit lock have about 50 passwords, about 1000, or many more?",
              "Solve a simpler lock first: 2 digits give 10 choices for each of 10 choices, so 100.",
              "Each new slot multiplies by 10: 3 digits give 1000, listed 000, 001, and so on up to 999.",
              "5 digits give 10 to the power 5, which is 1 lakh passwords, from 00000 to 99999."],
       examples=[
           WE("How many passwords does a 2-digit, a 3-digit and a 5-digit lock have?",
              ["2 digits: 10 choices for the first slot, and 10 for the second for each of them: 10 × 10 = 100.",
               "3 digits: each of the 100 passwords takes 10 third digits: 100 × 10 = 1000.",
               "4 digits: 1000 × 10 = 10000. 5 digits: 10000 × 10 = 100000.",
               "That is 10 to the power 5 passwords, from 00000 to 99999."],
              "100, 1000 and 100000 passwords",
              ncert=["2.2.lock_2digit", "2.2.lock_3digit", "2.2.lock_5digit"])],
       key_terms=["passwords", "combinations", "powers of 10"], misconceptions=["M_COMB_ADD"], minutes=10),
     A("T6.C3", "Letter locks and codes around us", "Apply",
       "Students count the passwords of a lock with 6 slots of letters A to Z as 26 to the power 6, and look at how "
       "pincodes, mobile numbers and vehicle numbers are built from slots.",
       textbook=["Estu says, \"Next time, I will buy a lock that has 6 slots with the letters A to Z. I feel it is "
                 "safer.\" How many passwords are possible with such a lock?",
                 "Think about how many combinations are possible in different contexts. Some examples are: "
                 "(i) Pincodes of places in India. The Pincode of Vidisha in Madhya Pradesh is 464001. The Pincode of "
                 "Zemabawk in Mizoram is 796017. (ii) Mobile numbers. (iii) Vehicle registration numbers.",
                 "Try to find out how these numbers or codes are allotted or generated."],
       teach=["Predict first: is a 6-letter lock safer than a 5-digit lock?",
              "Each slot now has 26 choices, so 6 slots give 26 multiplied by itself 6 times.",
              "26 to the power 6 is 308915776, more than 3000 times the 100000 passwords of the 5-digit lock.",
              "Pincodes use 6 digit slots, so at most 10 to the power 6 different pincodes are possible."],
       examples=[
           WE("How many passwords does a lock with 6 slots of letters A to Z have? Compare it with a 5-digit lock, "
              "and say how many 6-digit pincodes are possible.",
              ["Each slot has 26 choices: 26 × 26 × 26 × 26 × 26 × 26, which is 26 to the power 6.",
               "26 × 26 = 676, 676 × 676 = 456976, and 456976 × 676 = 308915776.",
               "308915776 ÷ 100000 is more than 3000, so the letter lock is much safer.",
               "A pincode has 6 digit slots: 10 to the power 6, which is 1000000 possible codes."],
              "26 to the power 6, which is 308915776 passwords; up to 1000000 pincodes",
              ncert=["2.2.letter_lock", "2.2.try_codes"])],
       key_terms=["codes", "combinations"], misconceptions=["M_COMB_ADD"], minutes=8),
     DOER("T6.C4", "Practice: count codes with powers", "code_lock_counter", "Apply",
          "Students count alphanumeric passcodes of length 5 as 36 to the power 5 and find how many digits a code "
          "needs to give 8.5 billion milk packets each a different code.",
          ["Each slot multiplies the count by the number of choices for that slot.",
           "n slots of 10 digits give 10 to the power n codes."],
          items=[
              FIO("FiO2.q11", "Figure it Out (power play, question 11)",
                  "A digital locker has an alphanumeric passcode of length 5. Some example codes are G89P0, 38098, "
                  "BRJKW and 003AZ. How many such codes are possible?",
                  ["Each slot can be one of 26 letters or 10 digits: 36 choices.",
                   "5 slots: 36 × 36 × 36 × 36 × 36, which is 36 to the power 5.",
                   "36 × 36 = 1296, 1296 × 36 = 46656, 46656 × 36 = 1679616, 1679616 × 36 = 60466176."],
                  "36 to the power 5, which is 60466176 codes"),
              FIO("FiO2.q9", "Figure it Out (power play, question 9)",
                  "A dairy plans to produce 8.5 billion packets of milk in a year. They want a unique ID code for each "
                  "packet. If they choose to use the digits 0 to 9, how many digits should the code consist of?",
                  ["n digit slots give 10 to the power n codes.",
                   "8.5 billion is 8500000000, which is 8.5 × 10 to the power 9.",
                   "10 to the power 9 is 1000000000, which is too few.",
                   "10 to the power 10 is 10000000000, which is enough."],
                  "10 digits")],
          misconceptions=["M_COMB_ADD"])],
    key_terms=["combinations", "passwords", "codes"]))

# ============================== T7 Dividing powers =========================================================
TOPICS.append(TOPIC(
    "T7", "M4", "Dividing Powers of the Same Base", ["2.3"], "Apply",
    "Students halve a line of 16 units again and again to see that dividing powers of the same base subtracts the "
    "exponents, use the rule on large exponents, and explain why the base cannot be zero.",
    "Dividing cancels matching factors, so n to the power a divided by n to the power b is n to the power a − b, "
    "for a base that is not zero.",
    [A("T7.C1", "Halving a line: 16, 8, 4, 2", "Apply",
       "Students use halving on a line of 16 units once, twice and three times, and write each length as a "
       "power of 2 as they cancel and divide out factors of 2.",
       textbook=["2.3 The Other Side of Powers",
                 "Imagine a line of length 16 units. Erasing half of it would result in 2⁴ ÷ 2 = 2 × 2 × 2 = 2³ = 8 "
                 "units.",
                 "Erasing half one more time would result in (2⁴ ÷ 2) ÷ 2 = 2⁴ ÷ 2² = 2 × 2 = 2² = 4 units.",
                 "Halving 16 cm three times may be written as 2⁴ ÷ 2³ = 2 units."],
       teach=["Predict first: after halving a 16-unit line three times, how long is it?",
              "16 is 2⁴. Halving once divides by 2 and cancels one factor of 2: 2³, which is 8.",
              "Halving twice divides by 2²: two factors cancel, leaving 2², which is 4.",
              "Halving three times divides by 2³, leaving one factor of 2."],
       examples=[
           WE("A line is 16 units long. Find its length after halving it once, twice and three times, as powers of 2.",
              ["16 is 2 × 2 × 2 × 2, which is 2⁴.",
               "Once: 2⁴ ÷ 2 = 8, which is 2³.",
               "Twice: 2⁴ ÷ 2² = 4, which is 2².",
               "Three times: 2⁴ ÷ 2³ = 2, which is 2 to the power 1."],
              "8 units (2³), 4 units (2²) and 2 units (2 to the power 1)",
              ncert=["2.3.halving_line"])],
       key_terms=["halving", "divide", "cancel"], misconceptions=["M_DIV_EXP"], minutes=8),
     A("T7.C2", "Divide powers of the same base: subtract the exponents", "Apply",
       "Students generalise the halving pattern: to divide powers of the same base, subtract the exponents. They "
       "use it for 2 to the power 100 divided by 2 to the power 25 and explain why the base cannot be 0.",
       textbook=["From this we can see that 2⁴ ÷ 2³ is 2 to the power 4 − 3, which is 2 to the power 1.",
                 "What is 2 to the power 100 ÷ 2 to the power 25 in powers of 2?",
                 "In a generalised form, n to the power a ÷ n to the power b = n to the power a − b, where n ≠ 0 and a "
                 "and b are counting numbers and a > b.",
                 "Why can't n be 0?"],
       teach=["Predict first: is 2 to the power 100 ÷ 2 to the power 25 equal to 2⁴ or to 2 to the power 75?",
              "Each factor below the bar cancels one factor above it, so the count left is the difference.",
              "100 − 25 = 75, so the answer is 2 to the power 75. Dividing the exponents gives 4, which is wrong.",
              "If n were 0 we would divide by 0, which has no meaning, so the base must not be 0."],
       examples=[
           WE("Write 2 to the power 100 ÷ 2 to the power 25 as a power of 2, and explain why the rule needs n ≠ 0.",
              ["Above the bar there are 100 factors of 2 and below it 25.",
               "Each of the 25 factors below cancels one above, leaving 100 − 25 = 75 factors.",
               "So 2 to the power 100 ÷ 2 to the power 25 is 2 to the power 75.",
               "With base 0, the divisor 0 to the power 25 is 0, and dividing by 0 is not defined."],
              "2 to the power 75; the base cannot be 0 because we cannot divide by 0",
              ncert=["2.3.two100_two25", "2.3.quotient_law", "2.3.mt_n_not_zero"])],
       key_terms=["divide", "exponents", "subtract"], misconceptions=["M_DIV_EXP"], minutes=10),
     DOER("T7.C3", "Practice: divide powers", "quotient_law_deriver", "Apply",
          "Students rewrite 4 to the power 32 as a power of 2, divide 2 to the power 224 by it by subtracting "
          "exponents, and find the units digit from the cycle of units digits of powers of 2.",
          ["Divide powers of the same base by subtracting the exponents.",
           "Rewrite bases so that both powers have the same base first."],
          items=[
              FIO("FiO2.q1", "Figure it Out (power play, question 1)",
                  "Find out the units digit in the value of 2 to the power 224 ÷ 4 to the power 32. Hint: 4 is 2².",
                  ["4 to the power 32 is (2²) to the power 32, which is 2 to the power 64.",
                   "2 to the power 224 ÷ 2 to the power 64 is 2 to the power 160.",
                   "Units digits of powers of 2 repeat in fours: 2, 4, 8, 6.",
                   "160 is a multiple of 4, so 2 to the power 160 ends in 6, like 2⁴ = 16."],
                  "6")],
          misconceptions=["M_DIV_EXP"])],
    key_terms=["divide", "exponents", "halving"]))

# ============================== T8 Zero and negative exponents =============================================
TOPICS.append(TOPIC(
    "T8", "M4", "Zero and Negative Exponents", ["2.3"], "Apply",
    "Students extend the division rule to show that a nonzero base to the power 0 is 1, halve a line more times "
    "than it has factors to meet negative exponents, and write negative powers as reciprocals of positive powers.",
    "Keeping the division rule true forces n to the power 0 to be 1 and n to the power −a to be 1 over n to the "
    "power a, so the rules hold for all integer exponents.",
    [A("T8.C1", "Why a power with exponent 0 is 1", "Apply",
       "Students define 2 to the power 0 so that the division rule still works, showing that 2⁴ divided by 2⁴ is 1, "
       "and generalise that x to the power 0 is 1 for any nonzero x.",
       textbook=["We have not covered the case when the exponent is 0; for example, what is 2 to the power 0?",
                 "Let us define 2 to the power 0 in a way that the generalised form above holds true.",
                 "2 to the power 0 is 2 to the power 4 − 4, which is 2⁴ ÷ 2⁴, and 2⁴ ÷ 2⁴ = 1.",
                 "In general, x to the power a ÷ x to the power a = x to the power a − a = x to the power 0, and so "
                 "1 = x to the power 0, where x ≠ 0 and a is a counting number."],
       teach=["Predict first: is 2 to the power 0 equal to 0, to 1, or to 2?",
              "Any number divided by itself is 1, so 2⁴ ÷ 2⁴ is 1.",
              "The rule says 2⁴ ÷ 2⁴ is 2 to the power 4 − 4, which is 2 to the power 0.",
              "For the rule to stay true, 2 to the power 0 must be 1, and the same holds for any nonzero base."],
       examples=[
           WE("Use 2⁴ ÷ 2⁴ to decide the value of 2 to the power 0, and then find 5 to the power 0 and 10 to the "
              "power 0.",
              ["2⁴ ÷ 2⁴ is 16 ÷ 16, which is 1, since every factor cancels.",
               "By the division rule, 2⁴ ÷ 2⁴ is 2 to the power 4 − 4, which is 2 to the power 0.",
               "So 2 to the power 0 must be 1, not 0.",
               "In the same way 5³ ÷ 5³ is 1, so 5 to the power 0 is 1, and 10 to the power 0 is 1."],
              "2 to the power 0, 5 to the power 0 and 10 to the power 0 are all 1",
              ncert=["2.3.zero_exponent"])],
       key_terms=["zero exponent"], misconceptions=["M_ZERO_POW"], minutes=8),
     A("T8.C2", "Halving past 1: negative exponents", "Apply",
       "Students continue halving a 16-unit line 5 times and 10 times, get half a unit and one sixty-fourth of a "
       "unit, and write these lengths with negative exponents as powers of 2.",
       textbook=["When Zero is in Power!",
                 "When a line of length 2⁴ units is halved 5 times, 2⁴ ÷ 2 to the power 5 gives 1/2 units.",
                 "Using the generalised form, we get 2⁴ ÷ 2 to the power 5 as 2 to the power (4 − 5), which is 2 to the power "
                 "−1. So, 2 to the power −1 is 1/2.",
                 "When a line of length 2⁴ units is halved 10 times, we get 2⁴ ÷ 2 to the power 10 as 2 to the power "
                 "(4 − 10), which is 2 to the power −6 units.",
                 "When expanded, the 4 factors above cancel 4 of the 10 below, leaving 1 over 2 to the power 6, which "
                 "is 1/64, also written as 2 to the power −6."],
       teach=["Predict first: if a 16-unit line is halved 5 times, is any of it left?",
              "Halving 4 times reaches 1 unit; a fifth halving gives half a unit.",
              "The rule gives 2 to the power 4 − 5, which is 2 to the power −1, so 2 to the power −1 is 1/2.",
              "Halving 10 times leaves 1 over 2 to the power 6, which is 1/64, written 2 to the power −6."],
       examples=[
           WE("A line is 16 units long. Find its length after halving it 5 times and 10 times, as a fraction and as a "
              "power of 2.",
              ["Halving 5 times: 16 ÷ 32 = 1/2.",
               "By the rule, 2⁴ ÷ 2 to the power 5 is 2 to the power −1, so 2 to the power −1 is 1/2.",
               "Halving 10 times: 16 ÷ 1024 = 1/64.",
               "By the rule, 2⁴ ÷ 2 to the power 10 is 2 to the power −6, so 2 to the power −6 is 1/64."],
              "1/2 unit, which is 2 to the power −1, and 1/64 unit, which is 2 to the power −6",
              ncert=["2.3.neg_halving"])],
       key_terms=["negative exponent", "halving"], misconceptions=["M_NEG_EXP_NEG"], minutes=10),
     A("T8.C3", "Negative powers are reciprocals", "Apply",
       "Students write 10 to the power −3 and 7 to the power −2 as fractions, show that 10 cubed is 1 over 10 to the "
       "power −3, and check that the exponent rules also hold for integer exponents.",
       textbook=["Similarly, 10 to the power −3 is 1/10³, 7 to the power −2 is 1/7², etc.",
                 "Can we write 10³ as 1 over 10 to the power −3? We can write 1 over 10 to the power −3 as 1 ÷ (1/10³), "
                 "and 1 ÷ (1/10³) = 1 × 10³ = 10³.",
                 "In a generalised form, n to the power −a = 1 over n to the power a, and n to the power a = 1 over n "
                 "to the power −a, where n ≠ 0.",
                 "We had required a and b to be counting numbers. Can a and b be any integers? Will the generalised "
                 "forms still hold true?"],
       teach=["Predict first: is 10 to the power −3 a negative number?",
              "10 to the power −3 is 1 over 10³, which is 1/1000, a small positive number.",
              "Dividing 1 by 1/1000 gives 1000, so 10³ is 1 over 10 to the power −3.",
              "Test a rule with integers: 2 to the power 3 × 2 to the power −1 should be 2²: 8 × 1/2 = 4. It works."],
       examples=[
           WE("Write 10 to the power −3 and 7 to the power −2 as fractions, show that 1 over 10 to the power −3 is "
              "10³, and check the product rule with exponents 3 and −1.",
              ["10 to the power −3 is 1/10³, which is 1/1000.",
               "7 to the power −2 is 1/7², which is 1/49.",
               "1 over 10 to the power −3 is 1 ÷ 1/1000, which is 1000, which is 10³.",
               "Product rule: 2³ × 2 to the power −1 should be 2 to the power 3 + (−1), which is 2². Check: 8 × 1/2 = "
               "4 = 2². The rule holds for integers."],
              "1/1000 and 1/49; 1 over 10 to the power −3 is 10³; yes, the rules hold for integer exponents",
              ncert=["2.3.reciprocal", "2.3.mt_integers"])],
       key_terms=["negative exponent", "reciprocal", "integers"], misconceptions=["M_NEG_EXP_NEG"], minutes=10),
     A("T8.C4", "Write negative powers as fractions", "Apply",
       "Students write 2 to the power −4, 10 to the power −5, (−7) to the power −2, (−5) to the power −3 and 10 to the "
       "power −100 as one over a positive power.",
       textbook=["Write equivalent forms of the following. (i) 2 to the power −4 (ii) 10 to the power −5 "
                 "(iii) (−7) to the power −2 (iv) (−5) to the power −3 (v) 10 to the power −100"],
       teach=["Predict first: is (−5) to the power −3 positive or negative?",
              "A negative exponent flips to the denominator: n to the power −a is 1 over n to the power a.",
              "The sign comes from the base: (−5)³ is −125, so (−5) to the power −3 is −1/125."],
       examples=[
           WE("Write 2 to the power −4, 10 to the power −5, (−7) to the power −2, (−5) to the power −3 and 10 to the "
              "power −100 in equivalent forms.",
              ["2 to the power −4 is 1/2⁴, which is 1/16.",
               "10 to the power −5 is 1 over 10 to the power 5, which is 1/100000.",
               "(−7) to the power −2 is 1/(−7)², which is 1/49.",
               "(−5) to the power −3 is 1/(−5)³, which is −1/125.",
               "10 to the power −100 is 1 over 10 to the power 100."],
              "1/16, 1/100000, 1/49, −1/125, and 1 over 10 to the power 100",
              ncert=["2.3.equiv_forms"])],
       key_terms=["negative exponent", "reciprocal"], misconceptions=["M_NEG_EXP_NEG"], minutes=6, thin=True),
     A("T8.C5", "Simplify products with integer exponents", "Apply",
       "Students simplify products of powers that have negative exponents by adding the exponents, including "
       "2⁴ × (−4) to the power −2 and 8 to the power p times 8 to the power q.",
       textbook=["Simplify and write the answers in exponential form. (i) 2 to the power −4 × 2 to the power 7 "
                 "(ii) 3² × 3 to the power −5 × 3 to the power 6 (iii) p³ × p to the power −10 (iv) 2⁴ × (−4) to the "
                 "power −2 (v) 8 to the power p × 8 to the power q"],
       teach=["Predict first: is 2 to the power −4 × 2 to the power 7 equal to 2³ or to 2 to the power −28?",
              "The product rule still adds exponents when some are negative: −4 + 7 = 3.",
              "Rewrite bases first when they differ: (−4)² is 16, which is 2⁴."],
       examples=[
           WE("Simplify: 2 to the power −4 × 2 to the power 7; 3² × 3 to the power −5 × 3 to the power 6; p³ × p to "
              "the power −10; 2⁴ × (−4) to the power −2; 8 to the power p × 8 to the power q.",
              ["Add exponents: −4 + 7 = 3, so 2³.",
               "2 + (−5) + 6 = 3, so 3³.",
               "3 + (−10) = −7, so p to the power −7.",
               "(−4) to the power −2 is 1/16, so 2⁴ × 1/16 = 16/16 = 1, which is 2 to the power 0.",
               "Add the exponents: 8 to the power p + q."],
              "2³, 3³, p to the power −7, 1, and 8 to the power p + q",
              ncert=["2.3.simplify"])],
       key_terms=["simplify", "integer exponents"], misconceptions=["M_ADD_EXP_MULT"], minutes=6, thin=True),
     DOER("T8.C6", "Practice: zero and negative exponents", "zero_exponent_staircase", "Apply",
          "Students simplify products, quotients and powers of powers with negative exponents into exponential form, "
          "and write one number as a product of powers in three different ways.",
          ["n to the power 0 is 1 and n to the power −a is 1 over n to the power a, for n ≠ 0.",
           "The product, quotient and power of a power rules work for all integer exponents."],
          items=[
              FIO("FiO2.q5", "Figure it Out (power play, question 5)",
                  "Simplify and write these in the exponential form. (i) 10 to the power −2 × 10 to the power −5 "
                  "(ii) 5 to the power 7 ÷ 5⁴ (iii) 9 to the power −7 ÷ 9⁴ (iv) (13 to the power −2) to the power −3 "
                  "(v) m to the power 5 n to the power 12 (mn) to the power 9",
                  ["(i) Add the exponents: −2 + (−5) = −7, so 10 to the power −7.",
                   "(ii) Subtract: 7 − 4 = 3, so 5³.",
                   "(iii) Subtract: −7 − 4 = −11, so 9 to the power −11.",
                   "(iv) Multiply: −2 × −3 = 6, so 13 to the power 6.",
                   "(v) (mn) to the power 9 is m to the power 9 n to the power 9; add: m to the power 14 n to the "
                   "power 21."],
                  "(i) 10 to the power −7 (ii) 5³ (iii) 9 to the power −11 (iv) 13 to the power 6 "
                  "(v) m to the power 14 n to the power 21"),
              FIO("FiO2.q3", "Figure it Out (power play, question 3)",
                  "Write the given number as the product of two or more powers in three different ways. The powers "
                  "can be any integers. (i) 64³ (ii) 192 to the power 8 (iii) 32 to the power −5",
                  ["(i) 64³ is 2 to the power 18: 2 to the power 10 × 2 to the power 8, 4 to the power 5 × 4⁴, and "
                   "8³ × 8³.",
                   "(ii) 192 is 2 to the power 6 × 3, so 192 to the power 8 is 2 to the power 48 × 3 to the power 8; "
                   "also 64 to the power 8 × 3 to the power 8, and 12 to the power 8 × 16 to the power 8.",
                   "(iii) 32 to the power −5 is 2 to the power −25: 2 to the power −10 × 2 to the power −15, "
                   "4 to the power −5 × 8 to the power −5, and 2 to the power 5 × 2 to the power −30."],
                  "For example (i) 2 to the power 10 × 2 to the power 8, 4 to the power 5 × 4⁴, 8³ × 8³ (ii) 2 to the "
                  "power 48 × 3 to the power 8, 64 to the power 8 × 3 to the power 8, 12 to the power 8 × 16 to the "
                  "power 8 (iii) 2 to the power −10 × 2 to the power −15, 4 to the power −5 × 8 to the power −5, 2 to "
                  "the power 5 × 2 to the power −30")],
          misconceptions=["M_ZERO_POW", "M_NEG_EXP_NEG"])],
    key_terms=["zero exponent", "negative exponent", "reciprocal"]))

# ============================== T9 Power lines =============================================================
TOPICS.append(TOPIC(
    "T9", "M4", "Power Lines", ["2.3"], "Analyze",
    "Students place powers of 4 along a line, move along it by multiplying or dividing by powers of 4, and compare "
    "two powers by finding how many times larger one is than the other.",
    "On a power line each step multiplies by the base, so moving a steps up multiplies by the base to the power a, "
    "and the gap between two powers is a quotient of powers.",
    [A("T9.C1", "The power line of 4", "Apply",
       "Students arrange the powers of 4 from 4 to the power −2 up to 4 to the power 8 on a line and compute products "
       "and quotients such as 65536 divided by 64 by moving along the line.",
       textbook=["Power Lines",
                 "Let us arrange the powers of 4 along a line.",
                 "4 to the power 8 is 65536, 4 to the power 7 is 16384, 4 to the power 6 is 4096, 4 to the power 5 is "
                 "1024, 4⁴ is 256, 4³ is 64, 4² is 16, 4 to the power 1 is 4, 4 to the power 0 is 1, 4 to the power −1 "
                 "is 1/4 and 4 to the power −2 is 1/16.",
                 "4 to the power 8 ÷ 4³, 4³ × 4², 4 to the power 7 × 4 to the power −2; 65536 ÷ 64, 64 × 16, "
                 "16384 ÷ 16."],
       teach=["Predict first: is 65536 ÷ 64 a power of 4?",
              "Each step up the line multiplies by 4; each step down divides by 4.",
              "65536 is 4 to the power 8 and 64 is 4³: dividing moves 3 steps down to 4 to the power 5, 1024.",
              "64 × 16 moves 2 steps up from 4³, landing on 4 to the power 5 again."],
       examples=[
           WE("Use the power line of 4 to find 65536 ÷ 64, 64 × 16 and 16384 ÷ 16 as powers of 4.",
              ["65536 is 4 to the power 8 and 64 is 4³: 8 − 3 = 5, so 4 to the power 5. Check: 65536 ÷ 64 = 1024.",
               "64 is 4³ and 16 is 4²: 3 + 2 = 5, so 4 to the power 5. Check: 64 × 16 = 1024.",
               "16384 is 4 to the power 7 and 16 is 4²: 7 − 2 = 5. Check: 16384 ÷ 16 = 1024.",
               "4 to the power 7 × 4 to the power −2 also lands on 4 to the power 5."],
              "All three are 4 to the power 5, which is 1024",
              ncert=["2.3.power_line4"])],
       key_terms=["power line", "powers of 4"], misconceptions=["M_DIV_EXP"], minutes=8),
     A("T9.C2", "How many times larger?", "Analyze",
       "Students show that 16384 is 16 times larger than 1024 by dividing two powers of 4, and find how many times "
       "larger 4 squared is than 4 to the power −2.",
       textbook=["Can we say that 16384 (4 to the power 7) is 16 (4²) times larger than 1024 (4 to the power 5)?",
                 "Yes, since 4 to the power 7 ÷ 4 to the power 5 is 4².",
                 "How many times larger than 4 to the power −2 is 4²?"],
       teach=["Predict first: is 4² four times larger than 4 to the power −2, or many more times?",
              "How many times larger is a quotient: divide the larger power by the smaller one.",
              "4 to the power 7 ÷ 4 to the power 5 is 4², so 16384 is 16 times 1024.",
              "4² ÷ 4 to the power −2 is 4 to the power 2 − (−2), which is 4⁴, which is 256 times."],
       examples=[
           WE("Show that 16384 is 16 times 1024, and find how many times larger 4² is than 4 to the power −2.",
              ["16384 is 4 to the power 7 and 1024 is 4 to the power 5.",
               "4 to the power 7 ÷ 4 to the power 5 is 4², which is 16. Check: 16384 ÷ 1024 = 16.",
               "4² ÷ 4 to the power −2 is 4 to the power 2 − (−2), which is 4⁴.",
               "Check: 16 ÷ (1/16) = 16 × 16 = 256, and 4⁴ = 256."],
              "16384 is 16 times 1024; 4² is 4⁴, which is 256, times 4 to the power −2",
              ncert=["2.3.times_larger"])],
       key_terms=["times larger", "power line"], misconceptions=["M_DIV_EXP"], minutes=8),
     DOER("T9.C3", "Practice: use the power line of 7", "power_line_walker", "Apply",
          "Students build the power line of 7 from 7 to the power −4 to 7 to the power 7 and write products and "
          "quotients of its numbers as single powers of 7.",
          ["Write each number as a power of 7 first.",
           "Multiplying adds exponents and dividing subtracts them."],
          items=[
              FIO("2.3.power_line7", "Power lines: the power line of 7",
                  "Use the power line for 7 to find: 2401 × 49, 49³, 343 × 2401, 16807 ÷ 49, 7 ÷ 343, 16807 ÷ 823543, "
                  "117649 × 1/343, and 1/343 × 1/343.",
                  ["The line: 7, 49, 343, 2401, 16807, 117649, 823543 are 7 to the powers 1 to 7.",
                   "2401 × 49 is 7⁴ × 7², which is 7 to the power 6; 49³ is (7²)³, also 7 to the power 6.",
                   "343 × 2401 is 7³ × 7⁴, which is 7 to the power 7, 823543.",
                   "16807 ÷ 49 is 7 to the power 5 − 2, which is 7³; 7 ÷ 343 is 7 to the power 1 − 3, which is 7 to the "
                   "power −2.",
                   "16807 ÷ 823543 is 7 to the power 5 − 7, which is 7 to the power −2.",
                   "117649 × 1/343 is 7 to the power 6 − 3, which is 7³; 1/343 × 1/343 is 7 to the power −6."],
                  "7 to the power 6, 7 to the power 6, 7 to the power 7, 7³, 7 to the power −2, 7 to the power −2, 7³, "
                  "and 7 to the power −6")],
          misconceptions=["M_DIV_EXP"])],
    key_terms=["power line", "times larger"]))
