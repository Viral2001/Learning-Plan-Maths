# -*- coding: utf-8 -*-
"""Topics T1 to T4: the chapter opening (M1), and distributing and multiplying (M2). Book pp 136 to 144."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 How much does a product grow? ===========================================
TOPICS.append(TOPIC(
    "T1", "M1", "How Much Does a Product Grow?", ["Chapter opening"], "Understand",
    "",
    "Algebra writes general statements about patterns compactly and can prove them. Distributivity links "
    "multiplication and addition, and it explains how a product grows when the numbers in it grow.",
    [A("T1.C1", "A product is a rectangle of rows and columns", "Understand",
       "",
       textbook=["We have seen how algebra makes use of letter symbols to write general statements about patterns "
                 "and relations in a compact manner. Algebra can also be used to justify or prove claims and "
                 "conjectures (like the many properties you saw in the previous chapter) and to solve problems of "
                 "various kinds.",
                 "Distributivity is a property relating multiplication and addition that is captured concisely "
                 "using algebra. In this chapter, we explore different types of multiplication patterns and show how "
                 "they can be described in the language of algebra by making use of distributivity."],
       teach=["Predict first: a tray holds mangoes in 23 rows of 27. One more row is laid along the edge. How many "
              "mangoes does that add: 1, 23 or 27?",
              "A product is a rectangle of rows and columns, so one more row adds a whole row of 27.",
              "Splitting a rectangle into parts and adding the parts is the distributive property.",
              "Keep this question open: what happens when both numbers grow, or one grows and the other shrinks?"],
       ncert=["opening"], key_terms=["product", "distributivity"], video_focus=["HOOK"], minutes=4,
       enrichment=True)],
    topic_type="framing"))

# ============================== T2 Increments in products ==================================================
TOPICS.append(TOPIC(
    "T2", "M2", "Increments in Products", ["6.1"], "Apply",
    "Students use the distributive property to expand a(b + c) and (a + b)c, find how much a product increases "
    "when one or both numbers grow by 1, and find when the product decreases, including for negative integers, "
    "naming such equalities identities.",
    "a(b + c) = ab + ac. Increasing one number of a product ab by 1 adds the other number; increasing both adds "
    "a + b + 1; increasing one and decreasing the other gives ab + b − a − 1, which can be smaller than ab. These "
    "equalities are identities: true for all integers.",
    [A("T2.C1", "The distributive property", "Apply",
       "Students expand a(b + c) and (a + b)c with the distributive property and find the increase in 23 × 27 when "
       "either number is increased by 1.",
       textbook=["Consider the multiplication of two numbers, say, 23 × 27.",
                 "1. By how much does the product increase if the first number (23) is increased by 1? 2. What if "
                 "the second number (27) is increased by 1? 3. How about when both numbers are increased by 1?",
                 "If a, b and c are three numbers, then a (b + c) = ab + ac.",
                 "This is called the distributive property of multiplication over addition. Using the identity "
                 "a (b + c) = ab + ac with a = 23, b = 27, and c = 1, we have 23 (27 + 1) = 23 × 27 + 23.",
                 "Remember that here, a (b + c) and 23 (27 + 1) mean a × (b + c), and 23 × (27 + 1), respectively. "
                 "We usually skip writing the '×' symbol before or after brackets, just as in the case of "
                 "expressions like 5a, xy, etc.",
                 "(a + b) c = c (a + b) (commutativity of multiplication) = ca + cb (distributivity) = ac + bc "
                 "(commutativity of multiplication)"],
       teach=["Predict first: 23 × 27 = 621. If 27 becomes 28, does the product grow by 1, by 23 or by 27?",
              "Draw 23 rows and 27 columns. One more column adds one dot in each of the 23 rows.",
              "In letters: a(b + c) = ab + ac, the distributive property. With a = 23, b = 27, c = 1 it gives "
              "23 × 27 + 23.",
              "Turning the product round, (a + b)c = c(a + b) = ca + cb = ac + bc, so increasing 23 by 1 adds 27."],
       examples=[
           WE("23 × 27 = 621. By how much does the product increase if 27 is increased by 1? If 23 is increased "
              "by 1?",
              ["23 × (27 + 1) = 23 × 27 + 23 × 1 by the distributive property.",
               "So the product increases by 23: 23 × 28 = 621 + 23 = 644.",
               "(23 + 1) × 27 = 23 × 27 + 1 × 27, by distributing from the other side.",
               "So the product increases by 27: 24 × 27 = 621 + 27 = 648."],
              "Increasing 27 by 1 adds 23; increasing 23 by 1 adds 27",
              ncert=["6.1.increments_q", "6.1.dist_prop"])],
       ncert=["6.1.ab_c"],
       key_terms=["distributive property", "expand", "commutativity"],
       misconceptions=["M_DISTRIBUTE_FIRST_ONLY"], minutes=8),
     A("T2.C2", "Both numbers grow, or one grows and one shrinks", "Apply",
       "Students expand (a + 1)(b + 1) and (a + 1)(b − 1), state the increase in each product, and explain why "
       "such equalities are called identities.",
       textbook=["Now let us see what happens if both numbers in a product are increased by 1. If in a product ab, "
                 "both a and b are increased by 1, then we obtain (a + 1) (b + 1).",
                 "Let us consider (a + 1) as a single term. Then, by the distributive property, we have "
                 "(a + 1) (b + 1) = (a + 1) b + (a + 1) 1 = ab + (b + a + 1).",
                 "Thus, the product ab increases by a + b + 1 when each of a and b are increased by 1.",
                 "What would we get if we had expanded (a + 1) (b + 1) by first taking (b + 1) as a single term? "
                 "Try it?",
                 "If a is increased by 1 and b is decreased by 1, then their product will be (a + 1) (b − 1). "
                 "Expanding this, we get (a + 1) (b − 1) = (a + 1) b − (a + 1) 1 = ab + b − (a + 1) = ab + b − a − 1.",
                 "Mathematical statements that express the equality of two algebraic expressions, such as "
                 "a (b + 8) = ab + 8a, (a + 1) (b − 1) = ab + b − a − 1, etc., are called identities."],
       teach=["Predict first: if both 23 and 27 grow by 1, is the increase 23 + 27 = 50, or something else?",
              "Treat (a + 1) as one term: (a + 1)(b + 1) = (a + 1)b + (a + 1) × 1 = ab + b + a + 1.",
              "The extra 1 is the corner dot where the new row meets the new column, so the increase is a + b + 1.",
              "Taking (b + 1) as the single term instead gives a(b + 1) + 1 × (b + 1), the same four parts.",
              "With one up and one down: (a + 1)(b − 1) = ab + b − a − 1.",
              "An equality of two expressions that holds for every value of the letter-numbers is an identity."],
       examples=[
           WE("23 × 27 = 621. Find the change in the product when both numbers are increased by 1, and when 23 is "
              "increased by 1 and 27 decreased by 1.",
              ["(a + 1)(b + 1) = ab + a + b + 1, so the increase is 23 + 27 + 1 = 51.",
               "Check: 24 × 28 = 672 and 672 − 621 = 51.",
               "(a + 1)(b − 1) = ab + b − a − 1, so the change is 27 − 23 − 1 = 3.",
               "Check: 24 × 26 = 624 and 624 − 621 = 3."],
              "Both up by 1: the product increases by 51; one up and one down: it increases by 3",
              ncert=["6.1.both_inc", "6.1.inc_dec"])],
       ncert=["6.1.both_inc_other_order", "6.1.identities"],
       key_terms=["increase", "identity", "term"],
       misconceptions=["M_PRODUCT_INCREASE", "M_TWO_TERMS_ONLY"], minutes=10),
     A("T2.C2x", "When the product decreases", "Analyze",
       "Students find pairs for which increasing one number by 1 and decreasing the other by 1 makes the product "
       "decrease, and check the identity with negative integers.",
       textbook=["Will the product always increase? Find 3 examples where the product decreases.",
                 "What happens when a and b are negative integers? Check by substituting different values for a and "
                 "b in each of the above cases. For example, a = −5, b = 8; a = −4, b = −5; etc.",
                 "We have seen that integers also satisfy the distributive property, that is, if x, y and z are any "
                 "three integers, then x (y + z) = xy + xz.",
                 "Thus, the expressions we have for increase of products hold when the letter-numbers take on "
                 "negative integer values as well."],
       teach=["Predict first: does making one number bigger and the other smaller always raise the product?",
              "The change is b − a − 1, so the product goes down whenever a is at least as big as b.",
              "Integers satisfy the distributive property, so the identity also works for negative a and b."],
       examples=[
           WE("Using (a + 1)(b − 1) = ab + b − a − 1, find three pairs where the product decreases, and check the "
              "identity for a = −5, b = 8.",
              ["The change is b − a − 1, which is negative when a is at least b.",
               "a = 5, b = 3: 5 × 3 = 15 but 6 × 2 = 12.",
               "a = 10, b = 10: 10 × 10 = 100 but 11 × 9 = 99.",
               "a = 7, b = 2: 7 × 2 = 14 but 8 × 1 = 8.",
               "a = −5, b = 8: ab = −40, and the identity gives −40 + 8 − (−5) − 1 = −28.",
               "Directly: (−5 + 1) × (8 − 1) = (−4) × 7 = −28."],
              "The product decreases for 5 and 3, 10 and 10, 7 and 2; the identity holds for negative integers too",
              ncert=["6.1.decrease_examples", "6.1.negatives"])],
       key_terms=["decrease", "negative integers"], misconceptions=["M_PRODUCT_INCREASE"], minutes=6, thin=True),
     DOER("T2.C3", "Practice: grow a product by parts", "distributive_area", "Apply",
          "Students write the products around a middle product pq in a multiplication grid as expressions, using "
          "the distributive property to grow and shrink each factor by 1.",
          ["a(b + c) = ab + ac, and (a + b)c = ac + bc.",
           "Increasing one number by 1 adds the other number; increasing both adds a + b + 1.",
           "An identity is true for every value of its letter-numbers, negative integers included."],
          items=[
              FIO("FiO1.q1", "Figure it Out (distributive property, question 1)",
                  "Observe the multiplication grid. Each number inside the grid is formed by multiplying two "
                  "numbers. If the middle number of a 3 × 3 frame is given by the expression pq, write the "
                  "expressions for the other numbers in the frame. (For example, the frame with 4 × 6 in the middle "
                  "has 3 × 5, 3 × 6, 3 × 7 in its top row and 5 × 5, 5 × 6, 5 × 7 in its bottom row.)",
                  ["The middle number is p × q, with row number p and column number q.",
                   "The row above has row number p − 1, and the row below has p + 1.",
                   "The column to the left has column number q − 1, and the column to the right has q + 1.",
                   "Top row: (p − 1)(q − 1), (p − 1)q, (p − 1)(q + 1).",
                   "Middle row: p(q − 1), pq, p(q + 1).",
                   "Bottom row: (p + 1)(q − 1), (p + 1)q, (p + 1)(q + 1).",
                   "Check with p = 4, q = 6: (p − 1)(q + 1) = 3 × 7 = 21, which is in the grid."],
                  "Top row (p − 1)(q − 1), (p − 1)q, (p − 1)(q + 1); middle row p(q − 1), pq, p(q + 1); bottom row "
                  "(p + 1)(q − 1), (p + 1)q, (p + 1)(q + 1)")])],
    key_terms=["distributive property", "increase", "identity"]))

# ============================== T3 Multiplying two sums =====================================================
TOPICS.append(TOPIC(
    "T3", "M2", "Multiplying Two Sums", ["6.1"], "Apply",
    "Students multiply two sums term by term as (a + m)(b + n) = ab + mb + an + mn, handle minus signs with the "
    "rules of integer multiplication, expand brackets with several terms, and collect like terms.",
    "The product of two sums is the sum of the products of each term of one with each term of the other: "
    "(a + m)(b + n) = ab + mb + an + mn. Minus signs follow the rules of integer multiplication, and like terms "
    "are added into a single term.",
    [A("T3.C1", "Each term times each term", "Apply",
       "Students expand (a + m)(b + n) into four products, link each product to a part of the rectangle, and use "
       "it to find how a product changes when both numbers grow.",
       textbook=["By how much will the product of two numbers change if one of the numbers is increased by m and "
                 "the other by n?",
                 "If a and b are the initial numbers being multiplied, they become a + m and b + n.",
                 "(a + m) (b + n) = (a + m)b + (a + m)n = ab + mb + an + mn",
                 "The increase is an + bm + mn.",
                 "Notice that the product is the sum of the product of each term of (a + m) with each term of "
                 "(b + n).",
                 "A Pinch of History: The first explicit statement of the distributive property was given by "
                 "Brahmagupta in his work Brahmasphuṭasiddhānta (Verse 12.55), who referred to the use of the "
                 "property for multiplication as khaṇḍa-guṇanam (multiplication by parts). His verse states, \"The "
                 "multiplier is broken up into two or more parts whose sum is equal to it; the multiplicand is then "
                 "multiplied by each of these and the results added\"."],
       teach=["Predict first: if one number grows by m and the other by n, how many new pieces does the rectangle "
              "gain?",
              "Split the rows into a and m, and the columns into b and n: the rectangle falls into four parts.",
              "The four parts are ab, an, mb and mn, so (a + m)(b + n) = ab + mb + an + mn.",
              "Every term of the first bracket meets every term of the second: two terms times two terms make four "
              "products.",
              "Brahmagupta called this multiplication by parts, more than 1300 years ago."],
       examples=[
           WE("23 × 27 = 621. Use the four parts to find the product when 23 grows by 2 and 27 grows by 5.",
              ["Take a = 23, m = 2, b = 27, n = 5.",
               "(a + m)(b + n) = ab + mb + an + mn.",
               "mb = 2 × 27 = 54, an = 23 × 5 = 115, mn = 2 × 5 = 10.",
               "So 25 × 32 = 621 + 54 + 115 + 10 = 800.",
               "The increase is 54 + 115 + 10 = 179."],
              "25 × 32 = 800, an increase of 179",
              ncert=["6.1.identity1"])],
       ncert=["6.1.history_khanda"],
       key_terms=["term", "product", "expand"], misconceptions=["M_TWO_TERMS_ONLY"], minutes=9),
     A("T3.C2", "Products with decreases: signs by integer rules", "Apply",
       "Students use the four-part product with negative changes to expand (a − 2)(b + 3), (a − 3)(b − 4) and "
       "(a ± u)(b ± v), fixing each sign by the rules of integer multiplication.",
       textbook=["This identity can be used to find how products change when the numbers being multiplied are "
                 "increased or decreased by any amount.",
                 "Let us write the product (a + 1) (b − 1) as (a + 1) (b + (−1)). Taking m = 1 and n = −1 in "
                 "Identity 1, we have ab + (1) × b + a × (−1) + (1) × (−1) = ab + b − a − 1.",
                 "Use Identity 1 to find how the product changes when (i) one number is decreased by 2 and the other "
                 "increased by 3; (ii) both numbers are decreased, one by 3 and the other by 4.",
                 "(a + u) (b − v) = (a + u) b − (a + u) v = ab + ub − (av + uv) = ab + ub − av − uv.",
                 "Notice that the signs of the terms in the products can be determined using the usual rules of "
                 "integer multiplication.",
                 "Expand (i) (a − u) (b + v), (ii) (a − u) (b − v). We get (a − u) (b + v) = ab − ub + av − uv, and "
                 "(a − u) (b − v) = ab − ub − av + uv."],
       teach=["Predict first: in (a − 3)(b − 4), is the last term −12 or +12?",
              "A decrease is an increase by a negative number: b − 1 is b + (−1).",
              "Each of the four products takes its sign from integer multiplication: (−3) × (−4) = +12.",
              "So (a + u)(b − v) = ab + ub − av − uv, (a − u)(b + v) = ab − ub + av − uv and "
              "(a − u)(b − v) = ab − ub − av + uv."],
       examples=[
           WE("Find how the product ab changes when (i) one number is decreased by 2 and the other increased by 3, "
              "(ii) one is decreased by 3 and the other by 4. Check each with a = 10, b = 10.",
              ["(i) (a − 2)(b + 3) = ab + 3a − 2b + (−2) × 3 = ab + 3a − 2b − 6.",
               "Check: 8 × 13 = 104, and 100 + 30 − 20 − 6 = 104.",
               "(ii) (a − 3)(b − 4) = ab − 4a − 3b + (−3) × (−4) = ab − 4a − 3b + 12.",
               "Check: 7 × 6 = 42, and 100 − 40 − 30 + 12 = 42."],
              "(a − 2)(b + 3) = ab + 3a − 2b − 6 and (a − 3)(b − 4) = ab − 4a − 3b + 12",
              ncert=["6.1.id1_decrease_task"])],
       ncert=["6.1.id1_minus1", "6.1.au_bv", "6.1.au_bv_expand"],
       key_terms=["integer multiplication", "decrease", "sign"],
       misconceptions=["M_SIGN_DISTRIBUTE"], minutes=9),
     A("T3.C3", "Several terms in a bracket, and like terms", "Apply",
       "Students distribute a term over a bracket of three terms, simplify each product with exponent notation, and "
       "decide which terms are like terms that can be added.",
       textbook=["The distributive property is not restricted to two terms within a bracket.",
                 "Example 1: Expand 3a/2 (a − b + 1/5).",
                 "3a/2 (a − b + 1/5) = (3a/2 × a) − (3a/2 × b) + (3a/2 × 1/5).",
                 "Using exponent notation, we can write 3/2 × (a × a) = (3/2) a².",
                 "So we get 3a/2 (a − b + 1/5) = (3/2) a² − (3/2) ab + (3/10) a.",
                 "Can any two terms be added to get a single term? We see that no two terms have exactly the same "
                 "letter-numbers, which would have allowed them to be simplified into a single term.",
                 "Recall that we call terms having the same letter-numbers like terms."],
       teach=["Predict first: in 3a/2 × (a − b + 1/5), how many terms will the answer have?",
              "Multiply 3a/2 by each of the three terms in turn.",
              "3a/2 × a = (3/2)a², 3a/2 × b = (3/2)ab and 3a/2 × 1/5 = (3/10)a.",
              "Only like terms, with exactly the same letter-numbers, can be added; a² and a are not like terms."],
       examples=[
           WE("Expand 3a/2 × (a − b + 1/5) and simplify.",
              ["Distribute over the three terms: (3a/2 × a) − (3a/2 × b) + (3a/2 × 1/5).",
               "3a/2 × a = (3/2) × (a × a) = (3/2)a².",
               "3a/2 × b = (3/2)ab.",
               "3a/2 × 1/5: here 3/2 × 1/5 = 3/10, so it is (3/10)a.",
               "No two of a², ab and a have the same letter-numbers, so nothing more can be added."],
              "(3/2)a² − (3/2)ab + (3/10)a",
              ncert=["6.1.ex1"])],
       ncert=["6.1.like_terms"],
       key_terms=["like terms", "exponent notation"], misconceptions=["M_UNLIKE_ADD"], minutes=8),
     A("T3.C3x", "Collecting like terms in bigger products", "Apply",
       "Students expand (a + b)(a + b) and (a + b)(a² + 2ab + b²), collect like terms, and check the result with "
       "numbers.",
       textbook=["Example 2: Expand (a + b) (a + b). We have (a + b) (a + b) = (a + b) a + (a + b) b = a × a + b × a + "
                 "ab + b × b = a² + ba + ab + b². Since ba = ab, we have two terms having the same letter-numbers ab "
                 "(or, that are like terms), and so can be added: ba + ab = ab + ab = 2ab. So we get "
                 "(a + b) (a + b) = a² + 2ab + b².",
                 "Example 3: Expand (a + b) (a² + 2ab + b²).",
                 "So, (a + b)(a² + 2ab + b²) = a³ + a²b + 2a²b + 2ab² + ab² + b³.",
                 "a²b + 2a²b = (1 + 2) a²b = 3a²b. Similarly, ab² and 2ab² are like terms and so can be added: "
                 "ab² + 2ab² = (1 + 2)ab² = 3ab².",
                 "Thus, we have (a + b) × (a² + 2ab + b²) = a³ + 3a²b + 3ab² + b³."],
       teach=["Predict first: (a + b) times a bracket of three terms gives how many products before collecting?",
              "(a + b)(a + b) = a² + ab + ba + b², and ba = ab, so it is a² + 2ab + b².",
              "Multiplying that by (a + b) gives six products; a²b with 2a²b and ab² with 2ab² are like terms."],
       examples=[
           WE("Expand (a + b)(a² + 2ab + b²) and check with a = 1, b = 2.",
              ["Distribute: (a + b)a² + (a + b) × 2ab + (a + b)b².",
               "= a³ + a²b + 2a²b + 2ab² + ab² + b³.",
               "Collect like terms: a²b + 2a²b = 3a²b and 2ab² + ab² = 3ab².",
               "So the product is a³ + 3a²b + 3ab² + b³.",
               "Check with a = 1, b = 2: (1 + 2) × (1 + 4 + 4) = 3 × 9 = 27, and 1 + 6 + 12 + 8 = 27."],
              "a³ + 3a²b + 3ab² + b³",
              ncert=["6.1.ex2", "6.1.ex3"])],
       key_terms=["like terms", "collect"], misconceptions=["M_UNLIKE_ADD"], minutes=6, thin=True),
     DOER("T3.C4", "Practice: multiply two sums", "binomial_tiles", "Apply",
          "Students multiply two sums and other brackets with numbers, letters and minus signs, collect like terms, and "
          "find a pattern in products of the form (a − b)(a + b) and (a − b)(a² + ab + b²).",
          ["Each term of one bracket multiplies each term of the other.",
           "Signs follow the rules of integer multiplication.",
           "Like terms, with the same letter-numbers, are added into one term."],
          items=[
              FIO("FiO1.q2", "Figure it Out (distributive property, question 2)",
                  "Expand the following products. (i) (3 + u)(v − 3) (ii) 2/3 × (15 + 6a) (iii) (10a + b)(10c + d) "
                  "(iv) (3 − x)(x − 6) (v) (−5a + b)(c + d) (vi) (5 + z)(y + 9)",
                  ["(i) 3v − 9 + uv − 3u, that is, 3v − 3u + uv − 9.",
                   "(ii) 2/3 × 15 = 10 and 2/3 × 6a = 4a, so 10 + 4a.",
                   "(iii) 100ac + 10ad + 10bc + bd.",
                   "(iv) 3x − 18 − x² + 6x, which is −x² + 9x − 18.",
                   "(v) −5ac − 5ad + bc + bd.",
                   "(vi) 5y + 45 + yz + 9z, that is, 5y + yz + 9z + 45."],
                  "(i) 3v − 3u + uv − 9 (ii) 10 + 4a (iii) 100ac + 10ad + 10bc + bd (iv) −x² + 9x − 18 "
                  "(v) −5ac − 5ad + bc + bd (vi) 5y + yz + 9z + 45"),
              FIO("FiO1.q3", "Figure it Out (distributive property, question 3)",
                  "Find 3 examples where the product of two numbers remains unchanged when one of them is increased "
                  "by 2 and the other is decreased by 4.",
                  ["(a + 2)(b − 4) = ab − 4a + 2b − 8.",
                   "The product is unchanged when −4a + 2b − 8 = 0, that is, when b = 2a + 4.",
                   "a = 1, b = 6: 1 × 6 = 6 and 3 × 2 = 6.",
                   "a = 2, b = 8: 2 × 8 = 16 and 4 × 4 = 16.",
                   "a = 3, b = 10: 3 × 10 = 30 and 5 × 6 = 30."],
                  "Any pair with b = 2a + 4, for example 1 and 6, 2 and 8, 3 and 10"),
              FIO("FiO1.q4", "Figure it Out (distributive property, question 4)",
                  "Expand (i) (a + ab − 3b²)(4 + b), and (ii) (4y + 7)(y + 11z − 3).",
                  ["(i) 4a + ab + 4ab + ab² − 12b² − 3b³.",
                   "4ab and ab are like terms: 4ab + ab = 5ab.",
                   "So (i) is 4a + 5ab + ab² − 12b² − 3b³.",
                   "(ii) 4y² + 44yz − 12y + 7y + 77z − 21.",
                   "−12y and 7y are like terms: −12y + 7y = −5y.",
                   "So (ii) is 4y² + 44yz − 5y + 77z − 21."],
                  "(i) 4a + 5ab + ab² − 12b² − 3b³ (ii) 4y² + 44yz − 5y + 77z − 21"),
              FIO("FiO1.q5", "Figure it Out (distributive property, question 5)",
                  "Expand (i) (a − b)(a + b), (ii) (a − b)(a² + ab + b²) and (iii) (a − b)(a³ + a²b + ab² + b³). Do "
                  "you see a pattern? What would be the next identity in the pattern? Can you check it by "
                  "expanding?",
                  ["(i) a² + ab − ba − b² = a² − b².",
                   "(ii) a³ + a²b + ab² − a²b − ab² − b³ = a³ − b³.",
                   "(iii) a⁴ + a³b + a²b² + ab³ − a³b − a²b² − ab³ − b⁴ = a⁴ − b⁴.",
                   "Every middle term cancels with a like term of opposite sign.",
                   "Next: (a − b)(a⁴ + a³b + a²b² + ab³ + b⁴) = a⁵ − b⁵, and expanding shows the same cancelling."],
                  "a² − b², a³ − b³, a⁴ − b⁴; next (a − b)(a⁴ + a³b + a²b² + ab³ + b⁴) = a⁵ − b⁵")])],
    key_terms=["term", "like terms", "integer multiplication"]))

# ============================== T4 Fast multiplication ======================================================
TOPICS.append(TOPIC(
    "T4", "M2", "Fast Multiplication", ["6.1"], "Apply",
    "Students use the distributive property to multiply by 11 in one line by adding neighbouring digits, extend "
    "the rule to multiplying by 101 and 1001, and multiply by 99 and 999 as a round number minus one.",
    "Multiplying by 11 = 10 + 1 adds each digit to its neighbour; multiplying by 101 = 100 + 1 adds digits two "
    "places apart; multiplying by 99 = 100 − 1 subtracts the number from a hundred times it.",
    [A("T4.C1", "Multiplying by 11 in one line", "Apply",
       "Students multiply a number by 11 by writing it as the number times 10 plus the number, and find the product "
       "in one line by adding neighbouring digits with carries.",
       textbook=["The distributive property can be used to come up with quick methods of multiplication when certain "
                 "types of numbers are multiplied.",
                 "Use the following multiplications to find the product of a number with 11 in a single step. "
                 "(a) 3874 × 11 (b) 5678 × 11",
                 "3874 × 11 = 3874 (10 + 1) = 38740 + 3874",
                 "Notice how the digits are getting added.",
                 "Let us take a 4-digit number dcba, that is, the number that has d in the thousands place, c in the "
                 "hundreds place, b in the tens place and a in the units place. dcba × (10 + 1) = dcba × 10 + dcba.",
                 "Describe a general rule to multiply a number (of any number of digits) by 11 and write the product "
                 "in one line."],
       teach=["Predict first: what are the last and first digits of 3874 × 11?",
              "3874 × 11 = 3874 × 10 + 3874: the same digits, shifted one place, are added.",
              "So each digit of the answer is a digit plus its right-hand neighbour, working from the units and "
              "carrying.",
              "The rule: write the units digit, then each sum of neighbouring digits, then the first digit, carrying "
              "where a sum is 10 or more."],
       examples=[
           WE("Find 3874 × 11 in one line, and check with 5678 × 11.",
              ["Units digit: 4.",
               "Next: 7 + 4 = 11, write 1 and carry 1.",
               "Next: 8 + 7 + 1 = 16, write 6 and carry 1.",
               "Next: 3 + 8 + 1 = 12, write 2 and carry 1.",
               "First digit: 3 + 1 = 4. So 3874 × 11 = 42614, and indeed 38740 + 3874 = 42614.",
               "5678 × 11: 8; 7 + 8 = 15, write 5 carry 1; 6 + 7 + 1 = 14, write 4 carry 1; 5 + 6 + 1 = 12, "
               "write 2 carry 1; 5 + 1 = 6. So 5678 × 11 = 62458."],
              "3874 × 11 = 42614 and 5678 × 11 = 62458",
              ncert=["6.1.fast11"])],
       ncert=["6.1.fast11_rule"],
       key_terms=["neighbouring digits", "carry"], misconceptions=["M_DISTRIBUTE_FIRST_ONLY"], minutes=8),
     A("T4.C2", "Multiplying by 101 and 1001", "Apply",
       "Students multiply by 101 as the number times 100 plus the number, write the product in one line by adding "
       "digits two places apart, and extend the rule to 1001 and 10001.",
       textbook=["Can we come up with a similar rule for multiplying a number by 101? Multiply 3874 by 101.",
                 "dcba × 101 = dcba × (100 + 1) = dcba × 100 + dcba.",
                 "What could be a general rule to multiply a number by 101 and write the product in one line? Extend "
                 "this rule for multiplication by 1001, 10001, …",
                 "Such methods of applying the distributive property to easily multiply two numbers were discussed "
                 "extensively in the ancient mathematical works of Brahmagupta (628 CE), Sridharacharya (750 CE) and "
                 "Bhaskaracharya (Lilavati, 1150 CE). In his work Brahmasphuṭasiddhānta (Verse 12.56), Brahmagupta "
                 "refers to such methods for fast multiplication using the distributive property as ista-gunana."],
       teach=["Predict first: in 3874 × 101, which digits get added to each other?",
              "3874 × 101 = 387400 + 3874: the copy is shifted two places, so each digit meets the digit two places "
              "to its left.",
              "For 1001 the copy shifts three places, for 10001 four places.",
              "Brahmagupta called such quick methods ista-gunana."],
       examples=[
           WE("Multiply 3874 by 101 in one line.",
              ["3874 × 101 = 3874 × 100 + 3874 = 387400 + 3874.",
               "The last two digits are 7 and 4, copied down.",
               "Hundreds: 8 + 4 = 12, write 2 and carry 1.",
               "Thousands: 3 + 7 + 1 = 11, write 1 and carry 1.",
               "Then 8 + 1 = 9 and finally 3.",
               "So 3874 × 101 = 391274."],
              "3874 × 101 = 391274",
              ncert=["6.1.fast101"])],
       ncert=["6.1.fast101_rule", "6.1.history_ista"],
       key_terms=["distributive property", "place value"], misconceptions=["M_DISTRIBUTE_FIRST_ONLY"], minutes=8),
     A("T4.C2x", "Multiplying by 101, 1001, 99 and 999", "Apply",
       "Students multiply by 101 and 1001 in one line and multiply by 99 and 999 by subtracting the number from a "
       "hundred or a thousand times it.",
       textbook=["Use this to find (i) 89 × 101, (ii) 949 × 101, (iii) 265831 × 1001, (iv) 1111 × 1001, "
                 "(v) 9734 × 99 and (vi) 23478 × 999."],
       teach=["Predict first: can 99 be split so that the distributive property makes it easy?",
              "99 = 100 − 1, so a number times 99 is a hundred times the number minus the number.",
              "In the same way 999 = 1000 − 1."],
       examples=[
           WE("Find 89 × 101, 949 × 101, 265831 × 1001, 1111 × 1001, 9734 × 99 and 23478 × 999.",
              ["89 × 101 = 8900 + 89 = 8989.",
               "949 × 101 = 94900 + 949 = 95849.",
               "265831 × 1001 = 265831000 + 265831 = 266096831.",
               "1111 × 1001 = 1111000 + 1111 = 1112111.",
               "9734 × 99 = 973400 − 9734 = 963666.",
               "23478 × 999 = 23478000 − 23478 = 23454522."],
              "8989, 95849, 266096831, 1112111, 963666, 23454522",
              ncert=["6.1.fast101_eval"])],
       key_terms=["place value", "round number"], minutes=6, thin=True),
     DOER("T4.C3", "Practice: multiply by 11 in one line", "neighbour_digit_adder", "Apply",
          "Students multiply two-digit, three-digit, four-digit and seven-digit numbers by 11 in one line by adding "
          "neighbouring digits and carrying.",
          ["Multiplying by 11 = 10 + 1 adds each digit to its neighbour.",
           "Multiplying by 101 = 100 + 1 adds digits two places apart.",
           "Multiplying by 99 = 100 − 1 takes the number away from a hundred times it."],
          items=[
              FIO("6.1.fast11_eval", "Math Talk (fast multiplication by 11)",
                  "Evaluate (i) 94 × 11, (ii) 495 × 11, (iii) 3279 × 11, (iv) 4791256 × 11.",
                  ["(i) 4; 9 + 4 = 13, write 3 carry 1; 9 + 1 = 10. So 94 × 11 = 1034.",
                   "(ii) 5; 9 + 5 = 14, write 4 carry 1; 4 + 9 + 1 = 14, write 4 carry 1; 4 + 1 = 5. So "
                   "495 × 11 = 5445.",
                   "(iii) 9; 7 + 9 = 16, write 6 carry 1; 2 + 7 + 1 = 10, write 0 carry 1; 3 + 2 + 1 = 6; then 3. "
                   "So 3279 × 11 = 36069.",
                   "(iv) 47912560 + 4791256 = 52703816, the same as adding neighbouring digits.",
                   "So 4791256 × 11 = 52703816."],
                  "(i) 1034 (ii) 5445 (iii) 36069 (iv) 52703816")])],
    key_terms=["distributive property", "place value"]))
