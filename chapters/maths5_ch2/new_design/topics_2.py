# -*- coding: utf-8 -*-
"""Topics T4 to T6 (modules M1 and M2): making equivalent fractions, comparing fractions with the same
denominator, comparing fractions with the same numerator.
Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of
its topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T4 Making Equivalent Fractions (M1) =========================================
TOPICS.append(TOPIC(
    "T4", "M1", "Making Equivalent Fractions", ["Making Equivalent Fractions"], "Apply",
    "Students make equivalent fractions by cutting every part of a shape into more equal pieces, describe the "
    "pattern in the top and bottom numbers, and check whether two fractions are equivalent.",
    "Cutting every part of a shape into more equal pieces gives the same shaded part a new name. Fractions that name "
    "the same part of a whole are equivalent fractions. To make one, multiply the top number and the bottom number "
    "by the same number.",
    [A("T4.C1", "Cutting Parts into More Equal Parts", "Understand",
       "Students cut every part of a shaded shape into more equal pieces, write the new fraction, and explain that "
       "the shaded part stays the same while the fraction gets a different name.",
       textbook=["Sameer has shaded one-third of the following figures. He draws horizontal lines to divide the "
                 "shapes into more equal parts.",
                 "He observes an interesting pattern and says that 1/3, 2/6, 3/9, and 4/12 show the same shaded "
                 "region.",
                 "2/6, 3/9, and 4/12 are all equivalent to 1/3. We use the word 'equivalent' to indicate the same "
                 "part of a whole, with different names."],
       teach=["Predict first: a bar has 5 equal parts and 4 are shaded, so 4/5 of the bar is shaded. You cut every "
              "part into 2 equal pieces. Is more of the bar shaded now, or is it the same?",
              "Look at the bar. No new colour was added and no colour was rubbed out. Only cut lines were drawn, so "
              "the shaded area is the same.",
              "Every part was cut into 2 pieces, so the whole now has 5 × 2 = 10 equal parts. The shaded part has "
              "4 × 2 = 8 pieces. The new name is 8/10.",
              "4/5 and 8/10 show the same shaded region. We call them equivalent fractions: the same part of a "
              "whole, with different names.",
              "Rule: cut every part into the same number of equal pieces, and the fraction gets a new name but the "
              "shaded part stays the same."],
       examples=[WE("A bar is cut into 5 equal parts and 4 parts are shaded, so 4/5 of the bar is shaded. Now cut "
                    "every part into 2 equal pieces. What fraction names the shaded part now? Has the shaded area "
                    "changed?",
                    ["The bar has 5 equal parts and 4 of them are shaded, so the shaded part is 4/5.",
                     "Cut every part into 2 equal pieces. The whole now has 5 × 2 = 10 equal parts.",
                     "Each shaded part was cut into 2 pieces, so the shaded pieces are 4 × 2 = 8.",
                     "8 shaded pieces out of 10 equal pieces is the fraction 8/10.",
                     "Check the area: nothing was added to the colour and nothing was taken away. Only cut lines "
                     "were drawn, so the shaded area is the same.",
                     "The same part of the whole has two names, 4/5 and 8/10. They are equivalent fractions."],
                    "8/10. The shaded area has not changed, so 4/5 = 8/10")],
       ncert=["mk.sameer", "mk.equivalent_def"],
       key_terms=["equivalent fractions", "equal parts", "cutting", "shaded part"],
       misconceptions=["M_UNEQUAL_PARTS", "M_BIGGER_DENOM"], minutes=6),
     A("T4.C2", "The Pattern in Equivalent Fractions", "Analyze",
       "Students describe the pattern in a list of equivalent fractions, say that the top number and the bottom "
       "number are multiplied by the same number, and use it to write a new equivalent fraction.",
       textbook=["Do you see any pattern in all the equivalent fractions that you found?",
                 "How do you know when a fraction is equivalent to another? Discuss in class."],
       teach=["Predict first: the 8 equal parts of a bar have 3 shaded, so 3/8 is shaded. Cut every part into 2 "
              "equal pieces and the name becomes 6/16. What happened to the top number and to the bottom number?",
              "The top number went from 3 to 6 and the bottom number went from 8 to 16. Both were multiplied by 2.",
              "Cut every part into 3 pieces instead: the top is 3 × 3 = 9 and the bottom is 8 × 3 = 24. Both were "
              "multiplied by 3. So 3/8 = 6/16 = 9/24.",
              "Why the same number? Every part is cut into the same number of pieces, so the shaded pieces and all "
              "the pieces are multiplied by that same number.",
              "Adding does not work. Add 2 to the top and the bottom of 3/8 and you get 5/10. But cutting the 8 "
              "parts gives 8, 16, 24 parts and so on, never 10, so 5/10 is not the same part as 3/8.",
              "To check two fractions, find the number that takes the top and the bottom of the first to the top "
              "and the bottom of the second. If it is the same number for both, they are equivalent.",
              "Rule: multiply the top number and the bottom number by the same number to get an equivalent "
              "fraction."],
       examples=[WE("A bar has 8 equal parts and 3 parts are shaded, so 3/8 of the bar is shaded. Cut every part "
                    "into 2 equal pieces, and then, on a copy of the first bar, cut every part into 3 equal pieces. "
                    "Write the two new fractions and find the pattern.",
                    ["The bar has 8 equal parts and 3 are shaded: 3/8.",
                     "Cut every part into 2 equal pieces. The shaded pieces are 3 × 2 = 6. The equal pieces in the "
                     "whole are 8 × 2 = 16. The fraction is 6/16.",
                     "Cut every part of the first bar into 3 equal pieces. The shaded pieces are 3 × 3 = 9. The "
                     "equal pieces in the whole are 8 × 3 = 24. The fraction is 9/24.",
                     "Look at the top numbers: 3, 6, 9. Look at the bottom numbers: 8, 16, 24.",
                     "From 3/8 to 6/16 the top and the bottom were both multiplied by 2. From 3/8 to 9/24 they were "
                     "both multiplied by 3.",
                     "Check: the shaded area is the same in all three bars, so 3/8 = 6/16 = 9/24."],
                    "3/8 = 6/16 = 9/24. To make an equivalent fraction, multiply the top number and the bottom "
                    "number by the same number")],
       ncert=["mk.pattern"],
       key_terms=["pattern", "equivalent fractions", "top number", "bottom number"],
       misconceptions=["M_EQUIV_ADD"], minutes=7),
     DOER("T4.C3", "Practice: Equal Parts Splitter", "equal_parts_splitter", "Apply",
          "Students write fractions equivalent to a given fraction by cutting shapes into equal parts, tick the "
          "pairs that are equivalent, and fill in the missing top or bottom number to make two fractions "
          "equivalent.",
          ["Cutting every part into more equal pieces changes the name of the fraction, not the shaded part.",
           "Equivalent fractions name the same part of a whole, with different names.",
           "Multiply the top number and the bottom number by the same number to make an equivalent fraction.",
           "To check a pair, find the number that takes the top and the bottom of one fraction to the top and the "
           "bottom of the other."],
          items=[FIO("mk.third_divide", "Making Equivalent Fractions: equivalents of 1/3",
                     "Sameer has shaded one-third of the figures. He draws horizontal lines to divide the shapes "
                     "into more equal parts. Divide the wholes given below into more equal parts and find fractions "
                     "equivalent to 1/3. Write them in the boxes below the images. 1/3 = 2/6 = 3/9 = 4/12 = ___ = "
                     "___ = ___ = ___/24 = ___/36",
                     ["The shaded part is 1/3: the middle strip of 3 equal strips. Sameer cut each strip into 2, 3 "
                      "and 4 pieces. The three empty boxes continue with 5, 6 and 7 pieces.",
                      "Cut each strip into 5 pieces. The whole has 3 × 5 = 15 pieces and the shaded strip has "
                      "1 × 5 = 5 pieces. The fraction is 5/15.",
                      "Cut each strip into 6 pieces. The whole has 3 × 6 = 18 pieces and the shaded strip has "
                      "1 × 6 = 6 pieces. The fraction is 6/18.",
                      "Cut each strip into 7 pieces. The whole has 3 × 7 = 21 pieces and the shaded strip has "
                      "1 × 7 = 7 pieces. The fraction is 7/21.",
                      "For ___/24, the bottom must be 24. Each strip is cut into 8 pieces, because 3 × 8 = 24. The "
                      "top is 1 × 8 = 8, so the fraction is 8/24.",
                      "For ___/36, each strip is cut into 12 pieces, because 3 × 12 = 36. The top is 1 × 12 = 12, "
                      "so the fraction is 12/36.",
                      "Check: the bottom number is always 3 times the top number. 3 × 12 = 36, and the same is true "
                      "for 6/18 and 8/24."],
                     "Sample answer: 5/15, 6/18, 7/21, then 8/24 and 12/36. Your answer may differ.",
                     kind="prompt",
                     q_figure="Four squares in a row, each with the middle third shaded and cut by horizontal "
                              "lines into 3, 6, 9 and 12 equal parts and labelled 1/3, 2/6, 3/9 and 4/12, then "
                              "three more squares, each cut into 3 equal vertical strips with the middle strip "
                              "shaded and an empty box under each.",
                     s_figure="The three empty squares cut by horizontal lines into 15, 18 and 21 equal parts with "
                              "the middle strip still shaded, labelled 5/15, 6/18 and 7/21."),
                 FIO("mk.twofifths", "Making Equivalent Fractions: equivalents of 2/5",
                     "The below pictures show 2/5 of a whole. Find the different fractions that are equivalent to "
                     "2/5 and write your fractions below each image. 2/5 = 4/10 = ___ = ___ = ___/50 = ___/100",
                     ["The first picture shows 2/5: 2 shaded rows out of 5 equal rows.",
                      "The second picture has each row cut into 2 pieces: 5 × 2 = 10 pieces and 2 × 2 = 4 shaded. "
                      "That is 4/10, and it is given.",
                      "In the third picture cut each row into 3 pieces: 5 × 3 = 15 pieces and 2 × 3 = 6 shaded. "
                      "The fraction is 6/15.",
                      "In the fourth picture cut each row into 4 pieces: 5 × 4 = 20 pieces and 2 × 4 = 8 shaded. "
                      "The fraction is 8/20.",
                      "For ___/50, 5 × 10 = 50, so multiply the top by 10 too: 2 × 10 = 20. The fraction is 20/50.",
                      "For ___/100, 5 × 20 = 100, so multiply the top by 20 too: 2 × 20 = 40. The fraction is "
                      "40/100.",
                      "Check: each bottom number is 5 times a number and each top number is 2 times the same "
                      "number. For 40/100, 100 ÷ 5 = 20 and 2 × 20 = 40."],
                     "Sample answer: 6/15, 8/20, then 20/50 and 40/100. Your answer may differ.",
                     kind="prompt",
                     q_figure="Four equal rectangles, each cut into 5 equal rows with 2 rows shaded: the first is "
                              "labelled 2/5, the second has one more line down the middle that cuts it into 10 "
                              "equal parts and is labelled 4/10, and the third and fourth have an empty fraction "
                              "box under them.",
                     s_figure="The third rectangle cut into 3 equal columns and labelled 6/15 and the fourth cut "
                              "into 4 equal columns and labelled 8/20, with the same 2 rows shaded in all four."),
                 FIO("LUDeq.Q1", "Let Us Do (equivalent fractions), Q1",
                     "Fill in the blanks with equivalent fractions. There may be more than one answer. (a) 1/7 = "
                     "___ (b) 2/3 = ___ (c) 3/4 = ___ (d) 3/5 = ___",
                     ["To make an equivalent fraction, multiply the top and the bottom by the same number. Here "
                      "every part is cut into 2 pieces.",
                      "(a) For 1/7, 1 × 2 = 2 and 7 × 2 = 14, so 1/7 = 2/14.",
                      "(b) For 2/3, 2 × 2 = 4 and 3 × 2 = 6, so 2/3 = 4/6.",
                      "(c) For 3/4, 3 × 2 = 6 and 4 × 2 = 8, so 3/4 = 6/8.",
                      "(d) For 3/5, 3 × 2 = 6 and 5 × 2 = 10, so 3/5 = 6/10.",
                      "Check: in each answer the bottom number is 2 times the bottom number in the question, and the "
                      "top number is 2 times the top number in the question. Any other number to multiply by, such "
                      "as 3, also works."],
                     "Sample answer: (a) 1/7 = 2/14 (b) 2/3 = 4/6 (c) 3/4 = 6/8 (d) 3/5 = 6/10. Your answer may "
                     "differ."),
                 FIO("LUDeq.Q2", "Let Us Do (equivalent fractions), Q2",
                     "Put a tick against the fractions that are equivalent. (a) 2/3 and 3/4 (b) 3/5 and 6/10 (c) "
                     "4/12 and 2/6 (d) 6/9 and 1/3",
                     ["Two fractions are equivalent if one top and bottom are multiplied by the same number to "
                      "give the other top and bottom.",
                      "(a) For 2/3 and 3/4, write both with 12 parts. 2/3 = 8/12 because 2 × 4 = 8 and 3 × 4 = 12. 3/4 "
                      "= 9/12 because 3 × 3 = 9 and 4 × 3 = 12. 8/12 and 9/12 are different, so no tick.",
                      "(b) For 3/5 and 6/10, 3 × 2 = 6 and 5 × 2 = 10, so 3/5 = 6/10. Tick.",
                      "(c) For 4/12 and 2/6, 2 × 2 = 4 and 6 × 2 = 12, so 2/6 = 4/12. Tick.",
                      "(d) For 6/9 and 1/3, 1 × 3 = 3 and 3 × 3 = 9, so 1/3 = 3/9. 3/9 is not 6/9, so no tick.",
                      "Check: the ticks are on the two pairs where the same number multiplied both the top and the "
                      "bottom."],
                     "The ticks go on (b), 3/5 and 6/10, and on (c), 4/12 and 2/6. The pairs in (a) and (d) are not "
                     "equivalent."),
                 FIO("LUDeq.Q3", "Let Us Do (equivalent fractions), Q3",
                     "Fill in the boxes such that the fractions become equivalent. (a) 2/5 = ___/10 (b) 3/4 = "
                     "___/16 (c) 4/7 = 8/___ (d) 5/9 = 25/___",
                     ["In each pair, find the number that takes one number to the other, then multiply the other "
                      "number by it too.",
                      "(a) For 2/5 = ___/10, the bottom went from 5 to 10, and 5 × 2 = 10. So the top is 2 × 2 = 4.",
                      "(b) For 3/4 = ___/16, the bottom went from 4 to 16, and 4 × 4 = 16. So the top is 3 × 4 = 12.",
                      "(c) For 4/7 = 8/___, the top went from 4 to 8, and 4 × 2 = 8. So the bottom is 7 × 2 = 14.",
                      "(d) For 5/9 = 25/___, the top went from 5 to 25, and 5 × 5 = 25. So the bottom is 9 × 5 = 45.",
                      "Check (d): 45 ÷ 9 = 5 and 25 ÷ 5 = 5. The same number 5 takes both bottom and top, so the "
                      "fractions are equivalent."],
                     "(a) 4 (b) 12 (c) 14 (d) 45")],
          misconceptions=["M_EQUIV_ADD", "M_UNEQUAL_PARTS"])],
    key_terms=["equivalent fractions", "equal parts", "pattern", "top number", "bottom number"]))

# ============================== T5 Comparing Fractions: Same Denominator (M2) ================================
TOPICS.append(TOPIC(
    "T5", "M2", "Comparing Fractions: Same Denominator", ["Comparing Fractions, Same Denominator"], "Apply",
    "Students compare two fractions with the same denominator by counting pieces of the same size, write the "
    "comparison with the correct sign, and explain which fraction is greater.",
    "When two fractions have the same denominator, their pieces are the same size. The fraction with more pieces is "
    "the greater fraction.",
    [A("T5.C1", "More Pieces of the Same Size", "Understand",
       "Students compare two fractions that have the same denominator by counting the pieces of the same size, and "
       "say which fraction is greater and which is less.",
       teach=["Predict first: Tamanna ate 3/10 of a chocolate bar and Gurpreet ate 7/10 of a bar of the same size. "
              "Who ate more? Do you need a hard sum to decide?",
              "Both fractions have the same bottom number, 10. The bottom number is called the denominator. It tells "
              "into how many equal pieces the whole is cut, so it tells the size of each piece.",
              "The same denominator means the same size of piece. Here every piece is 1/10 of a bar.",
              "The top number is called the numerator. It counts the pieces taken: 3 pieces and 7 pieces.",
              "When the pieces are the same size, more pieces means more. 7 pieces of 1/10 are more than 3 pieces of "
              "1/10, so 7/10 > 3/10.",
              "Rule: when the denominators are the same, the fraction with the bigger numerator is the greater "
              "fraction. The bars must be the same size."],
       examples=[WE("Tamanna and Gurpreet have two chocolate bars of the same size. Each bar is cut into 10 equal "
                    "pieces. Tamanna ate 3/10 of her bar and Gurpreet ate 7/10 of his bar. Who ate more?",
                    ["Both bars are the same size and both are cut into 10 equal pieces, so every piece is 1/10 of "
                     "a bar.",
                     "Tamanna ate 3 pieces of 1/10. That is 3/10.",
                     "Gurpreet ate 7 pieces of 1/10. That is 7/10.",
                     "The pieces are the same size, so the one who ate more pieces ate more.",
                     "7 is greater than 3, so 7 pieces of 1/10 are more than 3 pieces of 1/10. That is, 7/10 > 3/10.",
                     "Check: 7 − 3 = 4, so Gurpreet ate 4 more pieces of 1/10 than Tamanna."],
                    "Gurpreet ate more, because 7/10 > 3/10")],
       key_terms=["denominator", "numerator", "same size pieces", "greater than", "less than"],
       misconceptions=["M_TOP_ONLY", "M_DIFF_WHOLE"], minutes=6),
     DOER("T5.C2", "Practice: Chikki Share", "chikki_share", "Apply",
          "Students share a slab of chikki between two plates, say who has more by counting pieces of the same "
          "size, and compare fractions with the same denominator using the signs for greater than and less than.",
          ["The denominator tells how many equal pieces the whole is cut into.",
           "With the same denominator the pieces are the same size, so the fraction with more pieces is greater.",
           "Compare the numerators, the top numbers, and write < or >.",
           "Check by counting the pieces of the same size on each plate."],
          items=[FIO("sd.chikki", "Example 1: Sevi and Shami share a chikki",
                     "Sevi and Shami divided a piece of chikki between themselves. Sevi ate 1/3 and Shami ate the "
                     "rest, that is, 2/3. Who ate more?",
                     ["The chikki is cut into 3 equal pieces. Sevi ate 1 piece of 1/3.",
                      "Shami ate the rest: 3 − 1 = 2 pieces of 1/3. That is 2/3.",
                      "Both fractions have the same denominator, 3, so the pieces are the same size. Compare how "
                      "many pieces each ate.",
                      "2 pieces of 1/3 are more than 1 piece of 1/3, so 2/3 > 1/3.",
                      "Check: 1/3 + 2/3 = 3/3 = 1. Their pieces together make the whole chikki."],
                     "Shami ate more, because 2/3 > 1/3",
                     kind="example",
                     q_figure="A slab of chikki cut into 3 equal pieces, with 1 piece marked 1/3 for Sevi and 2 "
                              "pieces marked 2/3 for Shami.",
                     s_figure="The same slab with Sevi's 1 piece and Shami's 2 pieces, and Shami's 2 pieces ringed "
                              "to show they cover more of the slab than Sevi's 1 piece."),
                 FIO("LUDsd.Q1", "Let Us Do (same denominator), Q1",
                     "Compare the fractions given below using < and > signs. (a) 1/4 ___ 3/4 (b) 3/5 ___ 4/5 (c) "
                     "5/7 ___ 2/7 (d) 7/8 ___ 3/8 (e) 5/10 ___ 6/10 (f) 2/6 ___ 1/6",
                     ["In each pair the denominators are the same, so the pieces are the same size. Compare the "
                      "numerators.",
                      "(a) 1 < 3, so 1/4 < 3/4.",
                      "(b) 3 < 4, so 3/5 < 4/5.",
                      "(c) 5 > 2, so 5/7 > 2/7.",
                      "(d) 7 > 3, so 7/8 > 3/8.",
                      "(e) 5 < 6, so 5/10 < 6/10.",
                      "(f) 2 > 1, so 2/6 > 1/6.",
                      "Check (f): 2 pieces of 1/6 are one piece more than 1 piece of 1/6, so 2/6 is the greater."],
                     "(a) 1/4 < 3/4 (b) 3/5 < 4/5 (c) 5/7 > 2/7 (d) 7/8 > 3/8 (e) 5/10 < 6/10 (f) 2/6 > 1/6")],
          misconceptions=["M_TOP_ONLY", "M_UNEQUAL_PARTS"])],
    key_terms=["denominator", "numerator", "same size pieces", "greater than", "less than"]))

# ============================== T6 Comparing Fractions: Same Numerator (M2) ==================================
TOPICS.append(TOPIC(
    "T6", "M2", "Comparing Fractions: Same Numerator", ["Comparing Fractions, Same Numerator"], "Apply",
    "Students compare two fractions with the same numerator by comparing the size of one piece, write the "
    "comparison with the correct sign, and explain why more pieces in the whole means smaller pieces.",
    "When two fractions have the same numerator, you take the same number of pieces, but the pieces are different "
    "sizes. The whole cut into more pieces has smaller pieces, so the fraction with the bigger denominator is the "
    "smaller fraction.",
    [A("T6.C1", "Same Number of Pieces, Different Sizes", "Understand",
       "Students compare two fractions that have the same numerator by comparing the size of one piece, and explain "
       "why the fraction with the bigger denominator is the smaller fraction.",
       textbook=["Do the following pictures help you reason? Share your thoughts in the class."],
       teach=["Predict first: two parathas are the same size. One is cut into 4 equal pieces and the other into 10 "
              "equal pieces. You take 3 pieces from each. Do you get the same amount?",
              "Look at the numerators. Both are 3, so you take 3 pieces each time. Counting the pieces will not "
              "decide, so compare the size of one piece.",
              "The denominator tells how many equal pieces the whole is cut into. Cut into 10 pieces, each piece is "
              "small. Cut into 4 pieces, each piece is big. The 1/10 piece is smaller than the 1/4 piece.",
              "3 big pieces are more than 3 small pieces, so 3/4 > 3/10.",
              "Rule: when the numerators are the same, the fraction with the bigger denominator is the smaller "
              "fraction, because its pieces are smaller."],
       examples=[WE("Radhika and Raman have two parathas of the same size. Radhika's paratha is cut into 4 equal "
                    "pieces and Raman's paratha is cut into 10 equal pieces. Each of them eats 3 pieces. Who ate "
                    "more?",
                    ["Radhika ate 3 pieces of a paratha cut into 4 equal pieces. That is 3/4.",
                     "Raman ate 3 pieces of a paratha cut into 10 equal pieces. That is 3/10.",
                     "Both ate 3 pieces, so the number of pieces does not decide. Compare the size of one piece.",
                     "The two parathas are the same size. Cut into 4 pieces, each piece is big. Cut into 10 pieces, "
                     "each piece is small. So the 1/4 piece is bigger than the 1/10 piece.",
                     "3 bigger pieces are more than 3 smaller pieces, so 3/4 > 3/10.",
                     "Check: it takes only 4 pieces of 1/4 to make a whole paratha but 10 pieces of 1/10, so the 1/4 "
                     "piece is the bigger piece."],
                    "Radhika ate more, because 3/4 > 3/10 and the 1/4 piece is bigger than the 1/10 piece")],
       ncert=["sn.reason"],
       key_terms=["numerator", "denominator", "size of a piece", "greater than", "less than"],
       misconceptions=["M_SAME_TOP_BIGGER", "M_BIGGER_DENOM"], minutes=6),
     DOER("T6.C2", "Practice: Paratha Pieces", "paratha_pieces", "Apply",
          "Students compare the size of one piece of each paratha, say who ate more when the same number of pieces "
          "is taken, and compare fractions with the same numerator using the signs for greater than and less than.",
          ["The numerator tells how many pieces are taken. The denominator tells how many equal pieces the whole is "
           "cut into.",
           "With the same numerator you take the same number of pieces, so compare the size of one piece.",
           "The bigger the denominator, the smaller each piece, so the smaller the fraction.",
           "Check by laying one piece over the other."],
          items=[FIO("sn.paratha", "Example 2: 4/6 paratha and 4/5 paratha",
                     "One child says: I ate 4/6 paratha yesterday evening. The other says: I ate 4/5 paratha "
                     "yesterday evening. Between Sevi and Shami, can you tell who ate more? Use your fraction kit "
                     "to find the answer.",
                     ["One child ate 4 pieces of a paratha cut into 6 equal pieces. The other ate 4 pieces of a "
                      "paratha cut into 5 equal pieces. The parathas are the same size.",
                      "Both ate 4 pieces, so compare one piece of each: the 1/6 piece and the 1/5 piece.",
                      "Lay the 1/6 piece from the kit over the 1/5 piece. The paratha cut into 6 is shared among more "
                      "pieces, so the 1/6 piece is smaller than the 1/5 piece.",
                      "4 smaller pieces are less than 4 bigger pieces, so 4/6 < 4/5.",
                      "The child who ate 4/5 ate more.",
                      "Check: 5 pieces of 1/5 fill a paratha, but it takes 6 of the smaller pieces of 1/6 to fill "
                      "one."],
                     "The child who ate 4/5 ate more, because the 1/6 piece is smaller than the 1/5 piece, so 4/6 < "
                     "4/5",
                     kind="example",
                     q_figure="Two round parathas of the same size: the first is cut into 6 equal pieces with 4 "
                              "pieces marked, and the second is cut into 5 equal pieces with 4 pieces marked.",
                     s_figure="The two parathas with one piece of each shown beside them, the 1/5 piece drawn "
                              "bigger than the 1/6 piece, and the 4 marked pieces of each laid in a row, the row "
                              "for 4/5 longer than the row for 4/6."),
                 FIO("LUDsn.Q1", "Let Us Do (same numerator), Q1",
                     "Compare the following fractions using < and > signs. (a) 3/8 ___ 3/7 (b) 4/9 ___ 4/10 (c) "
                     "2/7 ___ 2/5 (d) 5/7 ___ 5/6 (e) 6/9 ___ 6/10 (f) 7/9 ___ 7/11",
                     ["In each pair the numerators are the same, so compare the size of one piece. The bigger the "
                      "denominator, the smaller the piece.",
                      "(a) 8 > 7, so the 1/8 piece is smaller than the 1/7 piece. 3/8 < 3/7.",
                      "(b) 10 > 9, so the 1/10 piece is smaller than the 1/9 piece. 4/9 > 4/10.",
                      "(c) 7 > 5, so the 1/7 piece is smaller than the 1/5 piece. 2/7 < 2/5.",
                      "(d) 7 > 6, so the 1/7 piece is smaller than the 1/6 piece. 5/7 < 5/6.",
                      "(e) 9 < 10, so the 1/9 piece is bigger than the 1/10 piece. 6/9 > 6/10.",
                      "(f) 9 < 11, so the 1/9 piece is bigger than the 1/11 piece. 7/9 > 7/11.",
                      "Check (c): it takes 5 pieces of 1/5 to make a whole but 7 pieces of 1/7, so the pieces of "
                      "1/5 are bigger and 2/5 is greater."],
                     "(a) 3/8 < 3/7 (b) 4/9 > 4/10 (c) 2/7 < 2/5 (d) 5/7 < 5/6 (e) 6/9 > 6/10 (f) 7/9 > 7/11")],
          misconceptions=["M_SAME_TOP_BIGGER", "M_BIGGER_DENOM"])],
    key_terms=["numerator", "denominator", "size of a piece", "greater than", "less than"]))
