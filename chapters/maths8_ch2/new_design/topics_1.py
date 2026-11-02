# -*- coding: utf-8 -*-
"""Topics T1 to T3 (modules M1 and M2). Book sections 2.1 and 2.2 up to the first Figure it Out, pp 19 to 23."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Framing: can paper reach the Moon? =======================================
TOPICS.append(TOPIC(
    "T1", "M1", "Power Play: Can Folded Paper Reach the Moon?", ["2.1"], "Understand",
    "",
    "Fold a sheet of paper again and again: the claim that 46 folds would reach the Moon opens the question that "
    "drives the chapter, how fast does repeated doubling grow?",
    [A("T1.C1", "Fold a sheet as many times as you can", "Understand",
       "",
       textbook=["2.1 Experiencing the Power Play",
                 "An Impossible Venture!",
                 "Take a sheet of paper, as large a sheet as you can find. Fold it once. Fold it again, and again.",
                 "How many times can you fold it over and over?",
                 "Estu says \"I heard that a sheet of paper can't be folded more than 7 times\".",
                 "Roxie replies \"What if we use a thinner paper, like a newspaper or a tissue paper?\"",
                 "Try it with different types of paper and see what happens.",
                 "Say you can fold a sheet of paper as many times as you wish. What would its thickness be after 30 "
                 "folds? Make a guess.",
                 "If you can fold a paper 46 times, it will be so thick that it can reach the Moon!"],
       teach=["Predict first: if a sheet could be folded 46 times, would the stack be as tall as a table, a building, "
              "a mountain, or taller?",
              "Each fold puts one half of the stack on the other half, so the thickness doubles every time.",
              "The claim is that 46 folds would reach the Moon. Keep the question open: by the end of the first topic "
              "we will check it fold by fold."],
       ncert=["2.1.intro"], key_terms=["fold", "thickness", "doubling"], video_focus=["HOOK"], minutes=4,
       enrichment=True)],
    topic_type="framing"))

# ============================== T2 Folding and doubling ====================================================
TOPICS.append(TOPIC(
    "T2", "M1", "Folding Paper: Doubling Every Time", ["2.1"], "Analyze",
    "Students build the thickness table fold by fold by doubling, compare thicknesses after 26 and 30 folds with a "
    "tall building and a deep trench, and show that every 10 folds multiply the thickness by 1024, which is "
    "multiplicative growth.",
    "Each fold doubles the thickness, so the thickness grows by multiplying: after 10 folds it is just over 1 cm, "
    "after 30 folds about 10.7 km, and after 46 folds more than 7 lakh km.",
    [A("T2.C1", "The thickness doubles with each fold", "Apply",
       "Students start from a sheet 0.001 cm thick, double the thickness for each fold, and fill the thickness table "
       "up to 17 folds, where it is about 131 cm.",
       textbook=["Let us find out how thick a sheet of paper will be after 46 folds. Assume that the thickness of the "
                 "sheet is 0.001 cm.",
                 "The following table lists the thickness after each fold. Observe that the thickness doubles after "
                 "each fold.",
                 "Fold 1: 0.002 cm, fold 2: 0.004 cm, fold 3: 0.008 cm, ..., fold 10: 1.024 cm, ..., fold 16: 65.536 cm, "
                 "fold 17: about 131 cm.",
                 "After 10 folds, the thickness is just above 1 cm (1.024 cm).",
                 "After 17 folds, the thickness is about 131 cm (a little more than 4 feet)."],
       teach=["Predict first: after 10 folds, is the stack thinner or thicker than your finger?",
              "Start at 0.001 cm. Each fold doubles: 0.002, 0.004, 0.008, 0.016 and so on.",
              "After 10 folds the thickness is 1.024 cm, just over a centimetre.",
              "Keep doubling: after 17 folds the stack is about 131 cm, taller than a small child."],
       examples=[
           WE("A sheet is 0.001 cm thick. Find its thickness after 1, 2, 3, 10 and 17 folds.",
              ["One fold doubles it: 0.001 × 2 = 0.002, so 0.002 cm.",
               "Two folds: 0.002 × 2 = 0.004, so 0.004 cm. Three folds: 0.004 × 2 = 0.008, so 0.008 cm.",
               "Doubling on: 0.016, 0.032, 0.064, 0.128, 0.256, 0.512 and then 1.024 cm after 10 folds.",
               "Seven more doublings: 2.048, 4.096, 8.192, 16.384, 32.768, 65.536 and about 131 cm after 17 folds."],
              "0.002 cm, 0.004 cm, 0.008 cm, 1.024 cm and about 131 cm",
              ncert=["2.1.table17"])],
       key_terms=["fold", "thickness", "double"], misconceptions=["M_LINEAR_EXP"], minutes=10),
     A("T2.C2", "Taller than a tower, deeper than the ocean", "Analyze",
       "Students guess and then find the thickness after 26, 27 and 30 folds by doubling, and compare them with the "
       "830 m Burj Khalifa and the 11 km deep Mariana Trench.",
       textbook=["Now, what do you think the thickness would be after 30 folds? 45 folds? Make a guess.",
                 "Fold 18: about 262 cm. Fold 19: about 524 cm. Fold 20: about 10.4 m.",
                 "After 26 folds, the thickness is approximately 670 m. Burj Khalifa in Dubai, the tallest building in "
                 "the world, is 830 m tall.",
                 "Fold 27: about 1.3 km.",
                 "After 30 folds, the thickness of the paper is about 10.7 km, the typical height at which planes fly. "
                 "The deepest point discovered in the oceans is the Mariana Trench, with a depth of 11 km."],
       teach=["Predict first: after 30 folds, would the stack be taller than a building, a mountain, or the height "
              "where planes fly?",
              "From about 10.4 m at fold 20, six doublings reach about 670 m at fold 26, close to the Burj Khalifa.",
              "One more fold passes 1.3 km; three more reach about 10.7 km at fold 30, the height where planes fly.",
              "The early folds hardly show, but each later fold adds more than all the earlier folds together."],
       examples=[
           WE("After 20 folds the stack is about 10.4 m. Find the thickness after 26, 27 and 30 folds and compare it "
              "with the Burj Khalifa (830 m) and the Mariana Trench (11 km).",
              ["Double from about 10.4 m: about 21 m, 42 m, 84 m, 168 m, 336 m and then about 670 m after 26 folds.",
               "That is a little less than the 830 m Burj Khalifa.",
               "Fold 27 doubles 670 m to about 1340 m, which is about 1.3 km, taller than the Burj Khalifa.",
               "Folds 28, 29 and 30 give about 2.7 km, 5.4 km and 10.7 km.",
               "10.7 km is just short of the 11 km depth of the Mariana Trench."],
              "About 670 m (just below the Burj Khalifa), about 1.3 km (above it), about 10.7 km (almost the depth "
              "of the Mariana Trench)",
              ncert=["2.1.mt_guess", "2.1.burj_mariana"])],
       key_terms=["thickness", "fold", "compare"], misconceptions=["M_LINEAR_EXP"], minutes=10),
     A("T2.C3", "Multiplicative growth: every 10 folds multiply by 1024", "Analyze",
       "Students show that any two folds multiply the thickness by 4, any three folds by 8, and any ten folds by 1024, "
       "and explain why this is called multiplicative or exponential growth.",
       textbook=["It might be hard to digest the fact that after just 46 folds, the thickness is more than 7,00,000 "
                 "km. This is the power of multiplicative growth, also called exponential growth.",
                 "Notice the change in thickness after two folds. By how much does it increase?",
                 "After any 3 folds, the thickness increases 8 times (= 2 × 2 × 2). Check if that is true.",
                 "Similarly, from any point, the thickness after 10 folds increases by 1024 times (= 2 multiplied by "
                 "itself 10 times).",
                 "Fold 0 to 10: 1.024 ÷ 0.001 = 1024. Fold 10 to 20, 20 to 30 and 30 to 40: the thickness is again "
                 "1024 times larger each time."],
       teach=["Predict first: from fold 5 to fold 7, does the thickness grow by adding a fixed amount or by "
              "multiplying?",
              "Two folds double twice: 2 × 2 = 4, so the thickness becomes 4 times as much, from any starting fold.",
              "Three folds give 2 × 2 × 2 = 8 times. Ten folds give 1024 times, which is 2 multiplied by itself 10 "
              "times.",
              "Growth by repeated multiplying is called multiplicative or exponential growth."],
       examples=[
           WE("Check that two folds multiply the thickness by 4, three folds by 8, and ten folds by 1024, using the "
              "thickness table.",
              ["Fold 3 is 0.008 cm and fold 5 is 0.032 cm: 0.032 ÷ 0.008 = 4, and 2 × 2 = 4.",
               "Fold 4 is 0.016 cm and fold 7 is 0.128 cm: 0.128 ÷ 0.016 = 8, and 2 × 2 × 2 = 8.",
               "Fold 0 is 0.001 cm and fold 10 is 1.024 cm: 1.024 ÷ 0.001 = 1024.",
               "Fold 10 is 1.024 cm and fold 20 is about 1048.5 cm: 1048.5 ÷ 1.024 ≈ 1024."],
              "Every 2 folds multiply by 4, every 3 by 8 and every 10 by 1024",
              ncert=["2.1.two_folds", "2.1.three_folds", "2.1.ten_folds"])],
       key_terms=["multiplicative growth", "exponential growth"], misconceptions=["M_LINEAR_EXP"], minutes=10),
     DOER("T2.C4", "Practice: fill the folding table", "fold_stack_doubler", "Apply",
          "Students fill the thickness table from fold 21 to fold 46 by doubling, converting centimetres to metres "
          "and kilometres, and find the fold where the stack passes the Moon.",
          ["Each fold doubles the thickness.",
           "Every 10 folds the thickness becomes 1024 times as much."],
          items=[
              FIO("2.1.fill_table", "Folding paper: fill the table",
                  "Fill the table of thickness for folds 21 to 45, starting from about 10.4 m after 20 folds. After how "
                  "many folds is the stack more than the 3,84,400 km distance to the Moon?",
                  ["Folds 21 to 25: about 21 m, 42 m, 84 m, 168 m and 336 m.",
                   "Folds 26 to 30: about 670 m, 1.3 km, 2.7 km, 5.4 km and 10.7 km.",
                   "Folds 31 to 35: about 21 km, 43 km, 86 km, 172 km and 344 km.",
                   "Folds 36 to 40: about 687 km, 1374 km, 2749 km, 5498 km and 10995 km.",
                   "Folds 41 to 45: about 21990 km, 43980 km, 87961 km, 175922 km and 351844 km.",
                   "Fold 45 is still short of the Moon; fold 46 doubles it to about 703687 km, more than 7 lakh km."],
                  "Fold 45 is about 3.5 lakh km; the 46th fold passes the Moon at more than 7 lakh km")],
          misconceptions=["M_LINEAR_EXP"])],
    key_terms=["fold", "thickness", "multiplicative growth"]))

# ============================== T3 Exponential notation ====================================================
TOPICS.append(TOPIC(
    "T3", "M2", "Exponential Notation: Powers, Bases and Exponents", ["2.2"], "Apply",
    "Students write repeated multiplication as a power with a base and an exponent, choose the expression for the "
    "thickness after 10 folds, find the sign of powers of negative bases and zero, and write prime factors and "
    "letter products in exponential form.",
    "n to the power a means a factors of n multiplied together: 5 to the power 4 is 625, a negative base gives a "
    "negative value for an odd exponent, and prime factors are written compactly with exponents.",
    [A("T3.C1", "A power has a base and an exponent", "Understand",
       "Students write the thickness after n folds as 0.001 × 2 to the power n, read powers aloud, and name the base "
       "and the exponent in 5 to the power 4, which is 625.",
       textbook=["2.2 Exponential Notation and Operations",
                 "The initial thickness of the paper was 0.001 cm. Upon folding once, its thickness became 0.001 cm × 2 "
                 "= 0.002 cm.",
                 "Folding it twice, its thickness became 0.001 cm × 2 × 2 = 0.004 cm, or 0.001 cm × 2² = 0.004 cm (in "
                 "shorthand).",
                 "n × n = n² (read as 'n squared' or 'n raised to the power 2'). n × n × n = n³ (read as 'n cubed').",
                 "In general, we write nᵃ to denote n multiplied by itself a times.",
                 "5⁴ = 5 × 5 × 5 × 5 = 625. 5⁴ is the exponential form of 625. Here, 4 is the exponent/power, and 5 is "
                 "the base.",
                 "2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 = 2¹⁰ = 1024. Remember the 1024 from earlier?"],
       teach=["Predict first: is 5⁴ equal to 20 or to 625?",
              "The small raised number counts the factors: 5⁴ means four 5s multiplied, 5 × 5 × 5 × 5.",
              "So 5⁴ is 625, not 5 × 4. The 5 is the base and the 4 is the exponent or power.",
              "The folding table is a table of powers of 2: after n folds the thickness is 0.001 × 2ⁿ cm."],
       examples=[
           WE("Write the thickness after 4 folds as a power of 2, and find the value of 5⁴. Name the base and the "
              "exponent of 5⁴.",
              ["Four folds double four times: 0.001 × 2 × 2 × 2 × 2 = 0.016, so 0.001 × 2⁴ cm.",
               "5⁴ means four factors of 5: 5 × 5 × 5 × 5.",
               "Multiply step by step: 5 × 5 = 25, 25 × 5 = 125, 125 × 5 = 625.",
               "In 5⁴ the base is 5 and the exponent is 4. It is read as 5 to the power 4."],
              "0.001 × 2⁴ cm, which is 0.016 cm; 5⁴ is 625 with base 5 and exponent 4",
              ncert=["2.2.fold_power", "2.2.read_powers", "2.2.base_exponent"])],
       key_terms=["base", "exponent", "power"], misconceptions=["M_POW_TIMES"], minutes=10),
     A("T3.C2", "Repeated multiplication is not repeated addition", "Analyze",
       "Students choose 2 to the power 10 times v as the thickness after 10 folds, reject the other expressions, and "
       "contrast 4 + 4 + 4, which is 12, with 4 × 4 × 4, which is 64.",
       textbook=["Which expression describes the thickness of a sheet of paper after it is folded 10 times? The initial "
                 "thickness is represented by the letter-number v.",
                 "(i) 10v (ii) 10 + v (iii) 2 × 10 × v (iv) 2¹⁰ (v) 2¹⁰v (vi) 10²v",
                 "Remember that 4 + 4 + 4 = 3 × 4 = 12, whereas 4 × 4 × 4 = 4³ = 64."],
       teach=["Predict first: which expression, 10v or 2¹⁰v, gives the thickness after 10 folds?",
              "Each fold doubles, so ten folds multiply v by 2 ten times: 2¹⁰v.",
              "10v adds v ten times, which is repeated addition, not doubling.",
              "Compare: 4 + 4 + 4 is 3 × 4, which is 12, but 4 × 4 × 4 is 4³, which is 64."],
       examples=[
           WE("A sheet has thickness v. Which expression gives its thickness after 10 folds: 10v, 10 + v, 2 × 10 × v, "
              "2¹⁰, 2¹⁰v or 10²v? Then compare 4 + 4 + 4 with 4 × 4 × 4.",
              ["One fold gives 2v, two folds give 2 × 2 × v, so ten folds give v multiplied by ten 2s, which is 2¹⁰v.",
               "10v, 10 + v and 2 × 10 × v add or multiply by 10 once; 2¹⁰ leaves out v; 10²v is 100v.",
               "Repeated addition: 4 + 4 + 4 = 3 × 4 = 12.",
               "Repeated multiplication: 4 × 4 × 4 = 4³ = 64."],
              "2¹⁰v; and 4 + 4 + 4 is 12 while 4 × 4 × 4 is 64",
              ncert=["2.2.ten_folds_v", "2.2.add_vs_mult"])],
       key_terms=["repeated multiplication", "expression"], misconceptions=["M_POW_TIMES", "M_LINEAR_EXP"], minutes=8),
     A("T3.C3", "Powers of negative numbers and of zero", "Analyze",
       "Students find (−4) cubed, decide whether (−1) to the powers 5 and 56 are positive or negative, verify that "
       "(−2) to the power 4 is 16, and find powers of zero.",
       textbook=["4 × 4 × 4 = 4³ = 64.",
                 "(−4) × (−4) × (−4) = (−4)³ = −64.",
                 "What is (−1)⁵? Is it positive or negative? What about (−1)⁵⁶?",
                 "Is (−2)⁴ = 16? Verify.",
                 "What is 0², 0⁵? What is 0ⁿ?"],
       teach=["Predict first: is (−4)³ positive or negative?",
              "Multiply in pairs: two negative factors make a positive, so an even number of negative factors gives a "
              "positive value and an odd number gives a negative value.",
              "(−1)⁵ has five negative factors, so it is −1; (−1)⁵⁶ has 56, an even number, so it is 1.",
              "Any power of 0 with a counting number exponent is 0, because one factor is already 0."],
       examples=[
           WE("Find (−4)³, (−1)⁵, (−1)⁵⁶, (−2)⁴, 0² and 0⁵.",
              ["(−4) × (−4) = 16, then 16 × (−4) = −64, so (−4)³ = −64.",
               "(−1)⁵ has five negative factors, an odd number, so it is −1, which is negative.",
               "(−1)⁵⁶ has 56 negative factors, an even number, so it is 1, which is positive.",
               "(−2) × (−2) × (−2) × (−2) = 16, so (−2)⁴ = 16 is true.",
               "0 × 0 = 0 and 0 × 0 × 0 × 0 × 0 = 0, so 0² and 0⁵ are both 0, and 0ⁿ is 0."],
              "(−4)³ is −64, (−1)⁵ is −1, (−1)⁵⁶ is 1, (−2)⁴ is 16, and 0² and 0⁵ are 0",
              ncert=["2.2.neg_base", "2.2.neg1_powers", "2.2.neg2_pow4", "2.2.zero_powers"])],
       key_terms=["negative base", "zero", "sign"], misconceptions=["M_NEG_BASE"], minutes=10),
     A("T3.C4", "Prime factors and letters in exponential form", "Apply",
       "Students write a × a × a × b × b as a cubed b squared, and express 32400 in exponential form as a "
       "product of powers of its prime factors 2, 3 and 5.",
       textbook=["a × a × a × b × b can be expressed as a³b² (read as a cubed b squared).",
                 "a × a × b × b × b × b can be expressed as a²b⁴ (read as a squared b raised to the power 4).",
                 "Express the number 32400 as a product of its prime factors and represent the prime factors in their "
                 "exponential form.",
                 "32400 = 2 × 2 × 2 × 2 × 5 × 5 × 3 × 3 × 3 × 3. In exponential form, this would be 32400 = 2⁴ × 5² × 3⁴."],
       teach=["Predict first: how many 3s are hidden in 32400?",
              "Group equal factors and count each group: a × a × a × b × b is a³b².",
              "Divide 32400 by primes again and again: by 2 four times, by 5 twice, by 3 four times.",
              "So 32400 is 2⁴ × 5² × 3⁴. Check by multiplying back."],
       examples=[
           WE("Write a × a × b × b × b × b in exponential form, and express 32400 as a product of powers of primes.",
              ["Two a's and four b's: a × a × b × b × b × b is a²b⁴.",
               "Divide 32400 by 2 four times: 16200, 8100, 4050, 2025.",
               "Divide 2025 by 5 twice: 405, 81. Divide 81 by 3 four times: 27, 9, 3, 1.",
               "So 32400 is 2⁴ × 5² × 3⁴. Check: 16 × 25 × 81 = 32400."],
              "a²b⁴, and 32400 is 2⁴ × 5² × 3⁴",
              ncert=["2.2.letters", "2.2.prime_32400"])],
       key_terms=["prime factors", "exponential form"], misconceptions=["M_POW_TIMES"], minutes=8, thin=True),
     DOER("T3.C5", "Practice: write and evaluate powers", "exponent_tower", "Apply",
          "Students write repeated products in exponential form, express numbers as products of powers of primes, and "
          "find the values of powers, including powers with negative bases.",
          ["A power counts factors: nᵃ is a factors of n multiplied together.",
           "An even number of negative factors gives a positive value; an odd number gives a negative value."],
          items=[
              FIO("FiO1.q1", "Figure it Out (exponential notation, question 1)",
                  "Express the following in exponential form: (i) 6 × 6 × 6 × 6 (ii) y × y (iii) b × b × b × b "
                  "(iv) 5 × 5 × 7 × 7 × 7 (v) 2 × 2 × a × a (vi) a × a × a × c × c × c × c × d",
                  ["Count each repeated factor and write the count as its exponent.",
                   "(i) four 6s: 6⁴. (ii) two y's: y². (iii) four b's: b⁴.",
                   "(iv) two 5s and three 7s: 5² × 7³. (v) two 2s and two a's: 2² × a².",
                   "(vi) three a's, four c's and one d: a³c⁴d."],
                  "(i) 6⁴ (ii) y² (iii) b⁴ (iv) 5² × 7³ (v) 2² × a² (vi) a³c⁴d"),
              FIO("FiO1.q2", "Figure it Out (exponential notation, question 2)",
                  "Express each of the following as a product of powers of their prime factors in exponential form. "
                  "(i) 648 (ii) 405 (iii) 540 (iv) 3600",
                  ["(i) 648 halves three times to 81, and 81 is 3 × 3 × 3 × 3, so 648 is 2³ × 3⁴. Check: 8 × 81 = 648.",
                   "(ii) 405 divided by 5 is 81, so 405 is 3⁴ × 5. Check: 81 × 5 = 405.",
                   "(iii) 540 halves twice to 135, which is 27 × 5, so 540 is 2² × 3³ × 5. Check: 4 × 27 × 5 = 540.",
                   "(iv) 3600 is 36 × 100, which is 2 × 2 × 3 × 3 × 2 × 2 × 5 × 5, so 3600 is 2⁴ × 3² × 5². "
                   "Check: 16 × 9 × 25 = 3600."],
                  "(i) 2³ × 3⁴ (ii) 3⁴ × 5 (iii) 2² × 3³ × 5 (iv) 2⁴ × 3² × 5²"),
              FIO("FiO1.q3", "Figure it Out (exponential notation, question 3)",
                  "Write the numerical value of each of the following: (i) 2 × 10³ (ii) 7² × 2³ (iii) 3 × 4⁴ "
                  "(iv) (−3)² × (−5)² (v) 3² × 10⁴ (vi) (−2)⁵ × (−10)⁶",
                  ["(i) 2 × 10³ = 2 × 1000 = 2000.",
                   "(ii) 7² × 2³ = 49 × 8 = 392.",
                   "(iii) 3 × 4⁴ = 3 × 256 = 768.",
                   "(iv) (−3)² × (−5)² = 9 × 25 = 225.",
                   "(v) 3² × 10⁴ = 9 × 10000 = 90000.",
                   "(vi) (−2)⁵ has five negative factors, so it is −32; (−10)⁶ has six, so it is 1000000. "
                   "So we get −32 × 1000000 = −32000000."],
                  "(i) 2000 (ii) 392 (iii) 768 (iv) 225 (v) 90000 (vi) −32000000")],
          misconceptions=["M_POW_TIMES", "M_NEG_BASE"])],
    key_terms=["base", "exponent", "power", "exponential form"]))
