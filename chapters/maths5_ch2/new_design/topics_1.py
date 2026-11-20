# -*- coding: utf-8 -*-
"""Topics T1, T1B, T2 and T3 (module M1: Same Whole, Equal Parts and Equivalent Fractions). The framing intro (Tamanna's
two chocolates hook and the free Chocolate Compare), the short idea topic T1B (Same Whole, Fair Comparison with
Tamanna's two questions), Playing with a Grid, and Fun with the Fraction Kit.
Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of its
topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Which Chocolate Is Bigger? (framing) ====================================
# The framing topic holds only the hook video and the free-try tool, and no book question. The concept video and
# Tamanna's two questions follow in the short idea topic T1B.
TOPICS.append(TOPIC(
    "T1", "M1", "Which Chocolate Is Bigger?", ["Chapter opening"], "Understand",
    "",
    "Tamanna has two chocolates of different sizes. She says that 1/3 of one is bigger than 1/2 of the other. Try the "
    "two chocolate bars and find out.",
    [A("T1.C1", "Tamanna's Two Chocolates", "Understand",
       "",
       textbook=["Tamanna is a student of Grade 5. She has two chocolates of different sizes. She says that 1/3 of one "
                 "of her chocolates is bigger than 1/2 of the other chocolate."],
       teach=["Predict first: Tamanna has a small chocolate and a big chocolate. Can 1/3 of one of them be bigger than "
              "1/2 of the other?",
              "Tamanna is a student of Grade 5. She has two chocolates of different sizes.",
              "She says that 1/3 of one of her chocolates is bigger than 1/2 of the other chocolate.",
              "Is she right? Think about it, then try it with the two chocolate bars on the next screen."],
       ncert=["open.story"], key_terms=["fraction", "chocolate", "whole"],
       video_focus=["HOOK"], enrichment=True, minutes=4),
     DOER("T1.C3", "Chocolate Compare: Explore", "chocolate_compare", "Understand",
          "",
          ["Tamanna has two chocolates of different sizes.",
           "She says that 1/3 of one chocolate is bigger than 1/2 of the other.",
           "Mark the parts, count the blocks and find out."],
          misconceptions=["M_DIFF_WHOLE"], role="try_it", enrichment=True)],
    topic_type="framing", key_terms=["fraction", "whole", "chocolate"]))

# ============================== T1B Same Whole, Fair Comparison ============================================
TOPICS.append(TOPIC(
    "T1B", "M1", "Same Whole, Fair Comparison", ["Chapter opening"], "Understand",
    "Students explain why two fractions can be compared only when they are parts of wholes of the same size, and use "
    "this to answer Tamanna's questions about her chocolates.",
    "A fraction is a part of its own whole. A smaller fraction of a big whole can be more than a bigger fraction of a "
    "small whole, so to compare two fractions the wholes must be the same.",
    [A("T1B.C1", "Same Whole, Fair Comparison", "Understand",
       "Students explain that a fraction is a part of its own whole and compare two fractions only when the wholes are "
       "the same size.",
       textbook=["To compare two fractions of two wholes, the wholes from which the fractions are derived must be the "
                 "same."],
       teach=["Predict first: a small roti and a big roti are each cut in half. Is half of the big roti the same "
              "amount as half of the small roti?",
              "No. Both pieces are called 1/2, but half of the big roti has more roti in it, because the big roti is a "
              "bigger whole.",
              "A fraction is a part of its own whole. 1/2 always means one of two equal parts, but how big the part "
              "is depends on how big the whole is.",
              "So with two wholes of different sizes, a smaller fraction of the big whole can be more than a bigger "
              "fraction of the small whole.",
              "To compare fairly, take two wholes of the same size. Then the fraction that covers more of the whole "
              "is the bigger fraction.",
              "Rule: to compare two fractions, the wholes must be the same."],
       examples=[WE("Maa has a small roti with 10 equal pieces and a big roti with 16 equal pieces. Every piece is the "
                    "same size. Is 1/2 of the small roti the same amount as 1/2 of the big roti? Then compare 1/2 and "
                    "1/4 of two rotis of the same size, each cut into 12 equal pieces.",
                    ["The small roti has 10 pieces. Half of 10 is 10 ÷ 2 = 5, so 1/2 of the small roti is 5 pieces.",
                     "The big roti has 16 pieces. Half of 16 is 16 ÷ 2 = 8, so 1/2 of the big roti is 8 pieces.",
                     "Both amounts are called 1/2, but 5 pieces and 8 pieces are not the same amount. The wholes are "
                     "different sizes.",
                     "Now take two rotis of the same size, each with 12 pieces. 1/2 of 12 is 12 ÷ 2 = 6 pieces.",
                     "1/4 of 12 is 12 ÷ 4 = 3 pieces.",
                     "6 pieces are more than 3 pieces, so on the same whole 1/2 is more than 1/4.",
                     "Check: the pieces of both rotis are the same size, so 6 pieces really is more than 3 pieces."],
                    "No. 1/2 of the small roti is 5 pieces and 1/2 of the big roti is 8 pieces, because the wholes "
                    "are different sizes. On the same whole, 1/2 (6 pieces) is more than 1/4 (3 pieces)")],
       ncert=["open.rule"], key_terms=["whole", "same whole", "compare"],
       misconceptions=["M_DIFF_WHOLE"], minutes=5),
     DOER("T1B.C2", "Practice: Same Whole", None, "Understand",
          "Students explain why 1/3 of a big chocolate can be more than 1/2 of a small one, and say that two "
          "fractions can be compared only when they are parts of the same whole.",
          ["A fraction is a part of its own whole.",
           "Half of a big whole holds more than half of a small whole.",
           "To compare two fractions, the wholes must be the same."],
          items=[FIO("open.chocolate", "Tamanna's Chocolates: is she correct",
                     "Tamanna is a student of Grade 5. She has two chocolates of different sizes. She says that 1/3 of "
                     "one of her chocolates is bigger than 1/2 of the other chocolate. Is that correct? Explain why "
                     "this is so.",
                     ["Count the blocks. The small bar has 4 blocks, 2 rows of 2. The big bar has 9 blocks, 3 rows of "
                      "3. Every block is the same size.",
                      "Take 1/2 of the small bar: share 4 blocks into 2 equal groups, 4 ÷ 2 = 2 blocks.",
                      "Take 1/3 of the big bar: share 9 blocks into 3 equal groups, 9 ÷ 3 = 3 blocks.",
                      "3 blocks are more than 2 blocks, so 1/3 of the big bar is bigger than 1/2 of the small bar.",
                      "This happens because the two bars are different sizes. A fraction is a part of its own whole.",
                      "Check: the blocks are all the same size, so 3 blocks really is more chocolate than 2 blocks."],
                     "Yes, she is correct for these two chocolates. 1/3 of the big bar is 3 blocks and 1/2 of the "
                     "small bar is 2 blocks, because the two wholes are different sizes.",
                     kind="prompt",
                     q_figure="Two chocolate bars side by side. The small bar has 4 equal blocks in 2 rows of 2, with "
                              "the caption 'Identify 1/2 of the chocolate'. The big bar has 9 equal blocks in 3 rows "
                              "of 3, with the caption 'Identify 1/3 of the chocolate'. Every block is the same size.",
                     s_figure="The same two bars with 2 blocks of the small bar and 3 blocks of the big bar shaded "
                              "orange, and the labels '4 blocks' and '9 blocks' under the bars."),
                 FIO("open.when", "Tamanna's Chocolates: when is 1/2 more than 1/3",
                     "When can we say that 1/2 of something is greater than 1/3 of something?",
                     ["1/2 and 1/3 are parts of a whole. A fraction always belongs to its own whole.",
                      "Take two bars of the same size, each with 6 blocks.",
                      "1/2 of 6 blocks is 6 ÷ 2 = 3 blocks.",
                      "1/3 of 6 blocks is 6 ÷ 3 = 2 blocks.",
                      "3 blocks are more than 2 blocks, so when both are parts of the same whole, 1/2 is greater than "
                      "1/3.",
                      "If the wholes are different sizes the answer can change: in Tamanna's bars, 1/3 of the big bar "
                      "was 3 blocks and 1/2 of the small bar was 2 blocks.",
                      "Check: the rule is that the wholes must be the same."],
                     "When both fractions are parts of the same whole, that is, two wholes of the same size, 1/2 is "
                     "greater than 1/3. If the wholes are different sizes we cannot say.",
                     kind="prompt",
                     s_figure="Two bars of the same size, each with 6 equal blocks. The first bar has 3 blocks shaded "
                              "and is labelled 1/2. The second bar has 2 blocks shaded and is labelled 1/3.")],
          misconceptions=["M_DIFF_WHOLE"])],
    key_terms=["whole", "same whole", "compare"]))

# ============================== T2 Playing with a Grid =====================================================
TOPICS.append(TOPIC(
    "T2", "M1", "Playing with a Grid", ["Playing with a Grid"], "Apply",
    "Students find a fraction of a grid by sharing its squares into equal groups, and show that different fractions "
    "can cover the same area.",
    "To find a fraction of a grid, share the squares into equal groups: one group is 1/n of the grid. Small equal "
    "parts can join to cover the same area as a bigger fraction, so one shaded area can have two fraction names.",
    [A("T2.C1", "Finding a Fraction of a Grid", "Apply",
       "Students find 1/n of a grid by sharing its squares into n equal groups and counting the squares in one group.",
       textbook=["Playing with a Grid"],
       teach=["Predict first: a grid has 21 equal squares. How many squares make 1/3 of the grid, and how many make "
              "1/7?",
              "A fraction of a grid means: share all the squares into equal groups. The bottom number tells how many "
              "equal groups.",
              "For 1/3, share the 21 squares into 3 equal groups: 21 ÷ 3 = 7 squares in each group. One group is 1/3 "
              "of the grid.",
              "For 1/7, share the 21 squares into 7 equal groups: 21 ÷ 7 = 3 squares in each group. One group is 1/7 "
              "of the grid.",
              "Rule: to find 1/n of a grid, share the squares into n equal groups. One group is 1/n."],
       examples=[WE("A grid has 3 columns and 7 rows of equal squares. Find 1/3 of the grid and 1/7 of the grid.",
                    ["Count the squares: 3 × 7 = 21 squares in all.",
                     "1/3 means 3 equal groups. Share 21 squares: 21 ÷ 3 = 7 squares in each group.",
                     "One group is 1/3 of the grid, so 1/3 of the grid is 7 squares, for example one whole column.",
                     "1/7 means 7 equal groups. Share 21 squares: 21 ÷ 7 = 3 squares in each group.",
                     "One group is 1/7 of the grid, so 1/7 of the grid is 3 squares, for example one whole row.",
                     "Check: 3 groups of 7 squares make 3 × 7 = 21, and 7 groups of 3 squares make 7 × 3 = 21."],
                    "1/3 of the grid is 7 squares and 1/7 of the grid is 3 squares")],
       ncert=["grid.setup"], key_terms=["grid", "equal groups", "fraction of a grid"],
       misconceptions=["M_UNEQUAL_PARTS"], minutes=6),
     A("T2.C2", "Small Parts That Join", "Understand",
       "Students show that small equal parts can join to cover the same area as a bigger fraction of a grid, and name "
       "that area with both fractions.",
       teach=["Predict first: on a grid of 24 squares you shade one square at a time. After how many squares have you "
              "shaded exactly 1/8 of the grid?",
              "One square is 1 of the 24 equal squares, so it is 1/24 of the grid.",
              "1/8 of 24 squares is 24 ÷ 8 = 3 squares. So 3 squares, that is 3 pieces of 1/24, shade exactly 1/8 of "
              "the grid.",
              "Small equal parts can join to cover the same area as a bigger fraction. The shaded area is the same, "
              "only its name changes: 3/24 and 1/8.",
              "This is how a fraction can hide inside a grid that is cut in other ways: join small parts and count "
              "the squares.",
              "Rule: to see if small parts make a bigger fraction, count the squares in each and compare."],
       examples=[WE("A grid has 6 columns and 4 rows of equal squares. Show that 3 pieces of 1/24 shade the same area "
                    "as 1/8 of the grid, and find how many pieces of 1/24 shade the same area as 1/12 of the grid.",
                    ["Count the squares: 6 × 4 = 24 squares in all, so each square is 1/24 of the grid.",
                     "1/8 of the grid is 24 ÷ 8 = 3 squares.",
                     "Shade 3 squares, one at a time. 3 pieces of 1/24 shade 3 squares, the same area as 1/8, so "
                     "3/24 = 1/8.",
                     "1/12 of the grid is 24 ÷ 12 = 2 squares.",
                     "2 pieces of 1/24 shade 2 squares, the same area as 1/12, so 2/24 = 1/12.",
                     "Check: 8 groups of 3 squares make 8 × 3 = 24, and 12 groups of 2 squares make 12 × 2 = 24."],
                    "3 pieces of 1/24 shade the same area as 1/8 (3/24 = 1/8), and 2 pieces of 1/24 shade the same "
                    "area as 1/12 (2/24 = 1/12)")],
       key_terms=["parts", "same area", "join"], misconceptions=["M_BIGGER_DENOM"], minutes=6),
     DOER("T2.C3", "Practice: Grid Shader", "grid_shader", "Apply",
          "Students shade 1/8, 1/6 and 1/12 of a 48-square grid by sharing the squares into equal groups, and mark "
          "where 1/3 appears.",
          ["To find 1/n of a grid, share the squares into n equal groups. One group is 1/n.",
           "Count the squares in the whole grid first, then divide by the bottom number.",
           "Small equal parts can join to cover the same area as a bigger fraction."],
          items=[FIO("grid.shade", "Playing with a Grid: shade the three grids",
                     "Shade 1/8 of Grid A in red. Shade 1/6 of Grid B in blue. Shade 1/12 of Grid C in yellow.",
                     ["Each grid has 8 columns and 6 rows, so there are 8 × 6 = 48 squares.",
                      "Grid A: 1/8 means 8 equal groups. 48 ÷ 8 = 6 squares in one group. Shade 6 squares red.",
                      "Grid B: 1/6 means 6 equal groups. 48 ÷ 6 = 8 squares in one group. Shade 8 squares blue.",
                      "Grid C: 1/12 means 12 equal groups. 48 ÷ 12 = 4 squares in one group. Shade 4 squares yellow.",
                      "Check: 8 groups of 6 squares make 8 × 6 = 48, 6 groups of 8 squares make 6 × 8 = 48, and 12 "
                      "groups of 4 squares make 12 × 4 = 48."],
                     "Grid A: 6 squares in red. Grid B: 8 squares in blue. Grid C: 4 squares in yellow. Your squares "
                     "may be in different places.",
                     kind="prompt",
                     q_figure="Three empty grids A, B and C side by side. Each grid has 8 columns and 6 rows of equal "
                              "squares.",
                     s_figure="The same three grids. Grid A has one whole column of 6 squares shaded red. Grid B has "
                              "one whole row of 8 squares shaded blue. Grid C has one block of 2 by 2 squares shaded "
                              "yellow."),
                 FIO("grid.third", "Playing with a Grid: find 1/3",
                     "Do you see 1/3 in any of the grids? Mark it.",
                     ["1/3 of 48 squares is 48 ÷ 3 = 16 squares. Look for 16 squares made of whole parts.",
                      "Grid A is cut into parts of 1/8, with 6 squares in each part. Joining them gives 6, 12 or 18 "
                      "squares, never 16. So 1/3 is not made from the parts of Grid A.",
                      "Grid B has parts of 1/6 with 8 squares each. 2 × 8 = 16, so 2 parts of 1/6 make 16 squares. "
                      "2/6 = 1/3. Mark 2 parts in Grid B.",
                      "Grid C has parts of 1/12 with 4 squares each. 4 × 4 = 16, so 4 parts of 1/12 make 16 squares. "
                      "4/12 = 1/3. Mark 4 parts in Grid C.",
                      "Check: 2/6 = 1/3 and 4/12 = 1/3, and both are 16 squares out of 48."],
                     "Yes. Grid B: 2 parts of 1/6 make 16 squares. Grid C: 4 parts of 1/12 make 16 squares. Grid A "
                     "cannot.",
                     kind="prompt",
                     q_figure="Three grids A, B and C side by side, each with 8 columns and 6 rows of equal squares. "
                              "Grid A has one whole column of 6 squares shaded red. Grid B has one whole row of 8 "
                              "squares shaded blue. Grid C has one block of 2 by 2 squares shaded yellow.",
                     s_figure="Grid B with its first 2 rows (16 squares) outlined in orange and labelled 1/3. Grid C "
                              "with its first 2 rows (4 blocks of 4 squares) outlined in orange and labelled 1/3. "
                              "Grid A with its parts of 6 squares drawn and no orange outline.")],
          misconceptions=["M_UNEQUAL_PARTS"])],
    key_terms=["grid", "fraction of a grid", "equal groups"]))

# ============================== T3 Fun with the Fraction Kit ===============================================
TOPICS.append(TOPIC(
    "T3", "M1", "Fun with the Fraction Kit", ["Fun with Fraction Kit", "Let Us Do (fraction kit)"], "Apply",
    "Students make a whole from pieces of one size and of different sizes, find how many small pieces fit in a "
    "bigger piece, and write equivalent fractions for the same part.",
    "A whole can be made with pieces of one size, n pieces of 1/n, or with pieces of different sizes. Small pieces can "
    "cover a bigger piece, so one part gets two names, like 1/2 = 2/4 and 1/3 = 2/6. These are called equivalent "
    "fractions.",
    [A("T3.C1", "Making a Whole with Pieces of One Size", "Understand",
       "Students make a whole with pieces of one size and say how many pieces of 1/n are needed to fill it.",
       textbook=["Gurpreet is playing with his fraction kit (a kit is given at the end of the textbook). Do you "
                 "remember how to make a whole with pieces of the same size?"],
       teach=["Predict first: a circle is cut into equal pieces and one piece is 1/4. How many pieces fill the whole "
              "circle?",
              "The bottom number 4 says that the whole is cut into 4 equal pieces. All 4 pieces fill the circle.",
              "So 4 pieces of 1/4 make 4/4, and 4/4 is 1 whole.",
              "It works for every size: pieces of 1/3 need 3 pieces, pieces of 1/6 need 6 pieces.",
              "Rule: n pieces of 1/n make a whole. n/n = 1."],
       examples=[WE("A circle is cut into equal pieces of 1/4. How many pieces make the whole circle? Then the circle "
                    "is cut into equal pieces of 1/8. How many pieces make the whole?",
                    ["A piece of 1/4 is one of 4 equal parts of the circle.",
                     "To fill the circle we need all 4 parts, so we need 4 pieces of 1/4.",
                     "4 pieces of 1/4 make 4/4 = 1 whole circle.",
                     "A piece of 1/8 is one of 8 equal parts of the circle. We need all 8 parts, so we need 8 pieces "
                     "of 1/8.",
                     "8 pieces of 1/8 make 8/8 = 1 whole circle.",
                     "Check: the bottom number tells how many equal pieces the whole has, so it is also the number of "
                     "pieces we need: 4 for 1/4 and 8 for 1/8."],
                    "4 pieces of 1/4 make a whole, and 8 pieces of 1/8 make a whole")],
       ncert=["kit.intro"], key_terms=["fraction kit", "pieces", "whole"],
       misconceptions=["M_UNEQUAL_PARTS"], minutes=5),
     A("T3.C2", "Making a Whole with Different Pieces", "Understand",
       "Students make a whole with pieces of different sizes and write two names for the same part as equivalent "
       "fractions.",
       textbook=["He makes a whole using two different fraction pieces. The whole looks like the following.",
                 "One piece of 1/2 and two pieces of 1/4 make a whole.",
                 "What is the relation between 1/2 and 1/4? Discuss in class.",
                 "1/2 = 2/4 (1/2 is equivalent to 2/4).",
                 "When a 1/2 piece is broken into 2 equal parts, each part is a 1/4 piece.",
                 "2 pieces of 1/4 are equal to 1/2.",
                 "Do you see that 1/3 = 2/6? Yes. These are called 'equivalent fractions'.",
                 "Let us see how equivalent fractions can be generated."],
       teach=["Predict first: a circle holds one piece of 1/2. What other pieces can fill the empty half, and how many "
              "do you need?",
              "Pieces of different sizes can make a whole too. One piece of 1/2 and two pieces of 1/4 fill the circle.",
              "What is the relation between 1/2 and 1/4? Break the 1/2 piece into 2 equal parts: each part is a 1/4 "
              "piece. So 2 pieces of 1/4 cover exactly the same part as 1/2.",
              "That is why 1/2 = 2/4. Two names for the same part are called equivalent fractions. Another pair is "
              "1/3 = 2/6.",
              "Rule: a piece can be replaced by smaller equal pieces that cover it exactly. The new name is an "
              "equivalent fraction."],
       examples=[WE("A circle is made with one piece of 1/2, one piece of 1/4 and two pieces of 1/8. Show that these "
                    "pieces make a whole. Then show that a piece of 1/8 can be covered by two pieces of 1/16, and "
                    "write the two names.",
                    ["Rename every piece with the bottom number 8 and count: 1/2 + 1/4 + 1/8 + 1/8 = 4/8 + 2/8 + 1/8 "
                     "+ 1/8.",
                     "Count the pieces of 1/8: 4 + 2 + 1 + 1 = 8, so the pieces make 8/8 = 1 whole.",
                     "Now break one piece of 1/8 into 2 equal parts. Each part is a piece of 1/16.",
                     "2 pieces of 1/16 cover exactly the same part as 1 piece of 1/8, so 1/8 = 2/16.",
                     "Check: 8 pieces of 1/8 make a whole and 16 pieces of 1/16 make a whole. Each piece of 1/8 holds "
                     "2 pieces of 1/16, and 8 × 2 = 16."],
                    "The pieces make 8/8 = 1 whole, and 1/8 = 2/16, two names for the same part")],
       ncert=["kit.half_quarter", "kit.relation", "eq.term"], key_terms=["equivalent fractions", "pieces", "whole"],
       misconceptions=["M_EQUIV_ADD"], minutes=6),
     A("T3.C3", "How Many Small Pieces Fit in a Bigger One?", "Apply",
       "Students find how many small pieces fit in a bigger piece by counting the small pieces that cover it, and "
       "write the two names of that part.",
       textbook=["Do you see how to generate equivalent fractions for any given fraction? Discuss in class."],
       teach=["Predict first: a strip has 20 equal parts. The piece of 1/4 covers 5 of them. How many pieces of 1/20 "
              "fit inside the piece of 1/4?",
              "A piece of 1/20 is 1 of the 20 equal parts of the strip, so it covers 1 part.",
              "Count how many pieces of 1/20 cover the bigger piece: the piece of 1/4 covers 5 parts, so 5 pieces of "
              "1/20 fit inside it.",
              "So the same part has two names: 5/20 and 1/4.",
              "The same idea gives an equivalent fraction for any fraction: count the small pieces that cover it.",
              "Rule: the number of small pieces that fit in a bigger piece is the top number of its new name."],
       examples=[WE("A strip has 20 equal parts. How many pieces of 1/20 fit inside 1/4 of the strip? How many fit "
                    "inside 1/10 of the strip?",
                    ["One piece of 1/20 is 1 of the 20 equal parts, because 20 ÷ 20 = 1.",
                     "1/4 of the strip is 20 ÷ 4 = 5 parts.",
                     "5 parts are covered by 5 pieces of 1/20, so 5 pieces of 1/20 fit inside 1/4.",
                     "1/10 of the strip is 20 ÷ 10 = 2 parts.",
                     "2 parts are covered by 2 pieces of 1/20, so 2 pieces of 1/20 fit inside 1/10.",
                     "Check: 4 pieces of 5 parts fill the strip, 4 × 5 = 20, and 10 pieces of 2 parts fill it, "
                     "10 × 2 = 20."],
                    "5 pieces of 1/20 fit inside 1/4 (5/20 = 1/4), and 2 pieces of 1/20 fit inside 1/10 "
                    "(2/20 = 1/10)")],
       ncert=["kit.generate"], key_terms=["fit inside", "equivalent fractions", "small pieces"],
       misconceptions=["M_BIGGER_DENOM", "M_EQUIV_ADD"], minutes=6),
     DOER("T3.C4", "Practice: Fraction Kit", "fraction_kit", "Apply",
          "Students find equivalent fractions, find how many small pieces fit in a bigger piece, and make wholes "
          "with pieces of one size and of different sizes.",
          ["n pieces of 1/n make a whole.",
           "Pieces of different sizes can make a whole too, like 1/2 and two pieces of 1/4.",
           "Two names for the same part are equivalent fractions, like 1/2 = 2/4 and 1/3 = 2/6.",
           "To find how many small pieces fit in a bigger piece, count the small pieces that cover it."],
          items=[FIO("eq.strip", "Fun with Fraction Kit: the shaded strip",
                     "Is 1/3 equal to 2/6? Let us find out. Look at the picture and identify the fractions. Are "
                     "there two different ways to write the fraction represented by the shaded part? ___",
                     ["The strip has 6 equal parts and 2 of them are shaded, so the shaded part is 2/6.",
                      "Group the 6 parts into groups of 2: 6 ÷ 2 = 3 groups.",
                      "The 2 shaded parts are 1 of the 3 equal groups, so the shaded part is also 1/3.",
                      "The same shaded part is written in two ways: 2/6 and 1/3.",
                      "Check: 3 groups of 2 parts make 3 × 2 = 6 parts, so 2/6 = 1/3."],
                     "Yes. The shaded part is 2/6 and also 1/3, so 1/3 = 2/6.",
                     kind="prompt",
                     q_figure="A strip of 6 equal parts in a row. The first 2 parts are shaded.",
                     s_figure="The same strip with the 6 parts drawn as 3 groups of 2. The first group is outlined and "
                              "labelled 1/3, and the 2 shaded parts are labelled 2/6."),
                 FIO("kit.five", "Fun with Fraction Kit: pieces of 1/5",
                     "Do you remember how to make a whole with pieces of the same size? How many pieces of 1/5 will "
                     "you need to make a whole?",
                     ["A piece of 1/5 is one of 5 equal parts of the whole.",
                      "To fill the whole we need all 5 parts, so we need 5 pieces of 1/5.",
                      "5 pieces of 1/5 make 5/5 = 1 whole.",
                      "Check: 1/5 + 1/5 + 1/5 + 1/5 + 1/5 = 5/5 = 1."],
                     "5 pieces of 1/5 make a whole.",
                     kind="prompt",
                     s_figure="A circle cut into 5 equal pieces, each piece labelled 1/5."),
                 FIO("kit.half", "Fun with Fraction Kit: equivalents of 1/2",
                     "What else is equivalent to 1/2? 1/2 = 2/4 = ___ = ___ = ___",
                     ["The kit shows 1/2 = 2/4: 2 pieces of 1/4 fill the piece of 1/2.",
                      "Try pieces of 1/6: 3 pieces of 1/6 fill the piece of 1/2, so 1/2 = 3/6.",
                      "Try pieces of 1/8: 4 pieces of 1/8 fill the piece of 1/2, so 1/2 = 4/8.",
                      "Try pieces of 1/10: 5 pieces of 1/10 fill the piece of 1/2, so 1/2 = 5/10.",
                      "Try pieces of 1/12: 6 pieces of 1/12 fill the piece of 1/2, so 1/2 = 6/12.",
                      "Check: in each name the top number is half of the bottom number: 2 and 4, 3 and 6, 4 and 8, 5 "
                      "and 10, 6 and 12."],
                     "Sample answer: 1/2 = 2/4 = 3/6 = 4/8 = 5/10 = 6/12. Your answer may differ, other equivalent "
                     "fractions are also right.",
                     kind="prompt"),
                 FIO("LUD1.Q1", "Let Us Do (fraction kit), Q1",
                     "In groups of 3 or 4, find different ways of making a whole with different fraction pieces from "
                     "your kit. Write the equivalent fractions for the following that you may find in the process. "
                     "(a) 1/3 = ___ = ___ = ___ (b) 1/4 = ___ = ___ = ___ (c) 1/5 = ___ = ___ = ___ "
                     "(d) 1/6 = ___ = ___ = ___",
                     ["Fill each piece with smaller pieces and count them. The count is the top number of the new "
                      "name. The kit gives the names up to twelfths, and the rest come from cutting every part into "
                      "more equal parts.",
                      "(a) 2 pieces of 1/6, 3 pieces of 1/9 and 4 pieces of 1/12 each fill 1/3. All three names are "
                      "on the kit. So 1/3 = 2/6 = 3/9 = 4/12.",
                      "(b) 2 pieces of 1/8 and 3 pieces of 1/12 fill 1/4. Cutting each fourth into 4 equal parts "
                      "gives 4/16, which is not on the kit. So 1/4 = 2/8 = 3/12 = 4/16.",
                      "(c) 2 pieces of 1/10 fill 1/5. Cutting each fifth into 3 and 4 equal parts gives 3/15 and "
                      "4/20, which are not on the kit. So 1/5 = 2/10 = 3/15 = 4/20.",
                      "(d) 2 pieces of 1/12 fill 1/6. Cutting each sixth into 3 and 4 equal parts gives 3/18 and "
                      "4/24, which are not on the kit. So 1/6 = 2/12 = 3/18 = 4/24.",
                      "Check one name from each part: 2/6 = 1/3, 2/8 = 1/4, 2/10 = 1/5 and 2/12 = 1/6.",
                      "Your answer may differ: the kit may give other names, and any equivalent fractions are right."],
                     "Sample answer: 2/6, 3/9, 4/12; 2/8, 3/12, 4/16; 2/10, 3/15, 4/20; 2/12, 3/18, 4/24."),
                 FIO("LUD1.Q2A", "Let Us Do (fraction kit), Q2 A",
                     "Find the following using your kit. You can also shade and check by shading. A. How many pieces "
                     "of 1/6 make 1/3? The shaded part is 1/3. Identify 1/6 in the same whole and find how many "
                     "pieces of 1/6 fit into 1/3.",
                     ["The whole has 6 equal squares, so each square is 1/6 of the whole.",
                      "The shaded part is 1/3. It is the first column of 2 squares.",
                      "Each square is a piece of 1/6, so 2 pieces of 1/6 fit into 1/3.",
                      "Check: 3 columns of 2 squares make 3 × 2 = 6 squares, so 2/6 = 1/3."],
                     "2 pieces of 1/6 make 1/3.",
                     q_figure="A rectangle of 2 rows and 3 columns of equal squares, 6 squares in all. The first "
                              "column of 2 squares is shaded.",
                     s_figure="The same rectangle with each of the 2 shaded squares labelled 1/6 and the shaded "
                              "column labelled 1/3."),
                 FIO("LUD1.Q2B", "Let Us Do (fraction kit), Q2 B",
                     "B. How many pieces of 1/8 make (a) 1/4? (b) 1/2?",
                     ["Each grid has 8 equal squares, so each square is 1/8 of the whole.",
                      "(a) 1/4 of 8 squares is 8 ÷ 4 = 2 squares, so 2 pieces of 1/8 make 1/4.",
                      "(b) 1/2 of 8 squares is 8 ÷ 2 = 4 squares, so 4 pieces of 1/8 make 1/2.",
                      "Check: 2/8 = 1/4 and 4/8 = 1/2."],
                     "(a) 2 pieces (b) 4 pieces",
                     q_figure="Two grids side by side, each with 2 rows and 4 columns of equal squares, 8 squares in "
                              "all. The first grid is for part (a) and the second grid is for part (b).",
                     s_figure="The same two grids. In the first grid the first column of 2 squares is shaded. In the "
                              "second grid the first 2 columns, 4 squares, are shaded."),
                 FIO("LUD1.Q2C", "Let Us Do (fraction kit), Q2 C",
                     "C. How many pieces of 1/12 make (a) 1/2 (b) 1/3 (c) 1/4 (d) 1/6?",
                     ["Each grid has 12 equal squares, so each square is 1/12 of the whole.",
                      "(a) 1/2 of 12 squares is 12 ÷ 2 = 6 squares, so 6 pieces of 1/12 make 1/2.",
                      "(b) 1/3 of 12 squares is 12 ÷ 3 = 4 squares, so 4 pieces of 1/12 make 1/3.",
                      "(c) 1/4 of 12 squares is 12 ÷ 4 = 3 squares, so 3 pieces of 1/12 make 1/4.",
                      "(d) 1/6 of 12 squares is 12 ÷ 6 = 2 squares, so 2 pieces of 1/12 make 1/6.",
                      "Check: 6/12 = 1/2, 4/12 = 1/3, 3/12 = 1/4 and 2/12 = 1/6."],
                     "(a) 6 pieces (b) 4 pieces (c) 3 pieces (d) 2 pieces",
                     q_figure="Four grids in a row, each with 3 rows and 4 columns of equal squares, 12 squares in "
                              "all. The grids are for parts (a), (b), (c) and (d).",
                     s_figure="The same four grids. Grid (a) has the first 2 columns, 6 squares, shaded. Grid (b) has "
                              "the first row, 4 squares, shaded. Grid (c) has the first column, 3 squares, shaded. "
                              "Grid (d) has the first 2 squares of the first row shaded."),
                 FIO("LUD1.Q3", "Let Us Do (fraction kit), Q3",
                     "Do as instructed using your fraction kit. Make a whole using only 1/6 and 1/12 pieces. Make a "
                     "whole using 1/12, 1/4, and 1/2 pieces. Make a whole using any five pieces of the same size. "
                     "Make a whole using any seven pieces. Play in a group with this kit and find other interesting "
                     "combinations to make a whole. Write or draw your findings.",
                     ["First task, only pieces of 1/6 and 1/12: take 3 pieces of 1/6 and 6 pieces of 1/12. 3/6 = "
                      "6/12, so 3/6 + 6/12 = 6/12 + 6/12 = 12/12 = 1.",
                      "Second task, pieces of 1/12, 1/4 and 1/2: take one piece of 1/2, one piece of 1/4 and 3 pieces "
                      "of 1/12. 1/2 + 1/4 + 1/12 + 1/12 + 1/12 = 6/12 + 3/12 + 3/12 = 12/12 = 1.",
                      "Third task, five pieces of the same size: take five pieces of 1/5. 1/5 + 1/5 + 1/5 + 1/5 + "
                      "1/5 = 5/5 = 1.",
                      "Fourth task, any seven pieces: take two pieces of 1/4, one piece of 1/6 and four pieces of "
                      "1/12. 2 + 1 + 4 = 7 pieces. In twelfths, 6/12 + 2/12 + 4/12 = 12/12 = 1. Seven pieces of 1/7 "
                      "also make a whole: 7/7 = 1.",
                      "Your own findings: any pieces that add up to 12/12 make a whole. For example one piece each of "
                      "1/2, 1/3 and 1/6: 1/2 + 1/3 + 1/6 = 6/12 + 4/12 + 2/12 = 12/12 = 1.",
                      "Check: every whole adds up to 12/12 or 5/5, which is 1, so there is no gap and no overlap."],
                     "Sample answer: 3/6 + 6/12 = 1; 1/2 + 1/4 + 3/12 = 1; 5/5 = 1; 2/4 + 1/6 + 4/12 = 1. Your answer "
                     "may differ.",
                     s_figure="A whole circle made of one piece of 1/2, one piece of 1/4 and three pieces of 1/12, "
                              "each piece labelled with its fraction.")],
          misconceptions=["M_EQUIV_ADD"])],
    key_terms=["fraction kit", "equivalent fractions", "whole", "pieces"]))
