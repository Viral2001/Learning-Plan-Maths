# -*- coding: utf-8 -*-
"""Topics T6 to T8 (module M2: fractions greater than one, equivalent fractions, lowest terms). Sections 7.5, 7.6."""
from topics_common import A, DOER, TOPIC, book, fio, we

TOPICS = []

H_GT1 = "Fractions greater than one"
H_MIXED = "Writing fractions greater than one as mixed numbers"
H_REG = "Mixed numbers as regular fractions"
H_WALL = "Using a fraction wall to find equal fractional lengths!"
H_SHARE = "Understanding equivalent fractions using equal shares"
H_LOW = "Expressing a fraction in lowest terms (or in its simplest form)"

# ============================== T6 Mixed fractions (7.5) =====================================================
TOPICS.append(TOPIC(
    "T6", "M2", "Fractions Greater than One and Mixed Numbers", ["7.5"], "Apply",
    "Students sort fractions into less than 1 and more than 1 by comparing numerator and denominator, count the "
    "whole units in a fraction greater than 1, and convert between fractions and mixed numbers.",
    "A fraction with a numerator larger than its denominator holds whole units: 8/3 = 2 + 2/3 = 2 2/3, and back.",
    [A("T6.C1", "Fractions bigger than one whole", "Analyze",
       "Students classify fractions as less than or more than 1 unit, state the numerator and denominator pattern, "
       "and find how many whole units 3/2 and 5/2 contain.",
       textbook=book("7.5", H_GT1, stop=9),
       teach=["Predict first: is 3/2 more or less than one whole? What about 2/3?",
              "Fractions less than 1 have a numerator smaller than the denominator; fractions more than 1 have a "
              "larger numerator.",
              "Count the halves: 3/2 = 1/2 + 1/2 + 1/2 = 1 + 1/2, so it holds 1 whole.",
              "Three thirds make one whole, so one more third makes 4/3 > 1."],
       examples=[we("7.5.q1"), we("7.5.q2"), we("7.5.ex1"), we("7.5.ex2")],
       key_terms=["numerator", "denominator", "whole"], misconceptions=["M_LESS_THAN_ONE"], minutes=12),
     A("T6.C2", "Mixed numbers, and back to fractions", "Apply",
       "Students write a fraction greater than 1 as a whole part plus a fractional part, read and write it as a "
       "mixed number, and turn a mixed number back into a fraction by counting units.",
       textbook=book("7.5", H_GT1, start=8, stop=9) + book("7.5", H_MIXED, stop=2)
       + book("7.5", H_MIXED, start=3, stop=4) + book("7.5", H_MIXED, start=5, stop=6) + book("7.5", H_REG, stop=5),
       teach=["Predict first: how many wholes are hiding in 8/3?",
              "Group the units: 4/3 = 1/3 + 1/3 + 1/3 + 1/3 = 1 + 1/3.",
              "8/3 = 2 + 2/3, read 'two and two thirds' and written 2 2/3. It means 2 + 2/3, never 2 × 2/3.",
              "A mixed number has a whole part and a fractional part less than 1.",
              "Back again, Jaya's way: each whole is 4 quarters, so 3 + 3/4 is 4 + 4 + 4 + 3 = 15 quarters, 15/4."],
       examples=[we("7.5.ex3"), we("7.5.ex4"), we("7.5.ex5"), we("7.5.ex6")],
       key_terms=["mixed number", "whole part", "fractional part"],
       misconceptions=["M_MIXED_PRODUCT", "M_LESS_THAN_ONE"], minutes=12),
     DOER("T6.C3", "Pull it together and do it: Mixed Number Builder", "mixed_builder", "Apply",
          "Students hop fractional units past 1 on the tool, group them into wholes, and convert between fractions "
          "and mixed numbers both ways.",
          ["Numerator bigger than denominator means more than one whole.",
           "Divide: the quotient is the whole part, the remainder over the denominator is the fractional part.",
           "Back to a fraction: wholes × denominator + numerator, over the same denominator."],
          items=[fio("7.5.FiO1.Q1"), fio("7.5.FiO1.Q2"), fio("7.5.FiO2.Q1"), fio("7.5.FiO2.Q2"),
                 fio("7.5.FiO2.Q3"), fio("7.5.FiO3.Q1")],
          misconceptions=["M_MIXED_PRODUCT", "M_LESS_THAN_ONE"])]))

# ============================== T7 Equivalent fractions (7.6) ================================================
TOPICS.append(TOPIC(
    "T7", "M2", "Equivalent Fractions", ["7.6"], "Apply",
    "Students show with paper strips, rows of equal wholes and equal sharing that different fractions can name the same "
    "share, and make equivalent fractions by multiplying the numerator and the denominator by the same number.",
    "Equivalent fractions name the same share in different units: 1/2 = 2/4 = 3/6, made by multiplying top and "
    "bottom by the same number.",
    [A("T7.C1", "Equal lengths on the fraction wall", "Understand",
       "Students compare folded strips and rows of equal wholes cut into different units to decide whether two fractions are the same "
       "length, and count how many smaller units make a larger one.",
       textbook=book("7.6", H_WALL, stop=14),
       teach=["Predict first: a strip folded in half with 1 part shaded, and one folded in quarters with 2 shaded. "
              "Which is longer?",
              "They are the same length, so 1/2 = 2/4 = 4/8. Such fractions are called equivalent fractions.",
              "On the fraction wall, two fractions are equivalent when their shaded lengths end at the same place.",
              "Three sixths fill one half, and two sixths fill one third."],
       examples=[we("7.6.q1"), we("7.6.q2"), we("7.6.q3"), we("7.6.q4"), we("7.6.q5"), we("7.6.q6")],
       key_terms=["equivalent fractions", "fraction wall"], misconceptions=["M_EQUIV_DIFFERENT"], minutes=12),
     A("T7.C2", "Equal shares give equivalent fractions", "Apply",
       "Students write division, addition and multiplication facts for a sharing situation, and show that groups "
       "with twice the units and twice the children get the same share, so 2/5 = 4/10 and 1/2 = 2/4 = 3/6.",
       textbook=book("7.6", H_SHARE, stop=8) + book("7.6", H_SHARE, start=16, stop=29),
       teach=["Predict first: 2 cakes among 5 children, or 4 cakes among 10. Which child gets more?",
              "One roti among 4 children: 1 ÷ 4 = 1/4, 1 = 1/4 + 1/4 + 1/4 + 1/4, and 1 = 4 × 1/4.",
              "Put two groups of 2 cakes and 5 children together: 4 cakes among 10 children, the same share.",
              "So 2/5 = 4/10, and 1/2 = 2/4 = 3/6: fractions with equal shares are equivalent fractions."],
       examples=[we("7.6.ex1"), we("7.6.q7"), we("7.6.q8")],
       key_terms=["equivalent fractions", "share"], misconceptions=["M_EQUIV_DIFFERENT"], minutes=12),
     A("T7.C3", "The multiply rule for equivalent fractions", "Analyze",
       "Students list fractions equivalent to 1/2 and 2/3, notice that the numerator and the denominator are "
       "multiplied by the same number, and name the simplest form.",
       textbook=book("7.6", H_SHARE, start=29, stop=33),
       teach=["Predict first: write three more fractions equal to 1/2. What do they have in common?",
              "2 rotis among 3 children, 4 among 6 and 6 among 9 give the same share: 2/3 = 4/6 = 6/9.",
              "Each comes from 2/3 by multiplying the numerator and the denominator by the same number.",
              "Adding the same number to both does not work: 2/3 and 3/4 are not equal."],
       examples=[we("7.6.q9"), we("7.6.q10"), we("7.6.q11")],
       key_terms=["equivalent fractions", "simplest form"], misconceptions=["M_EQUIV_ADD"], minutes=10),
     DOER("T7.C4", "Pull it together and do it: Fraction Wall", "fraction_wall", "Apply",
          "Students shade lengths on rows of equal wholes to test whether two fractions are equivalent, and fill in "
          "missing numbers in equivalent fractions.",
          ["Equivalent fractions reach the same length on the same whole.",
           "Multiply the numerator and the denominator by the same number.",
           "Sharing twice the units among twice the people gives the same share."],
          items=[fio("7.6.FiO1.Q1"), fio("7.6.FiO1.Q2"), fio("7.6.FiO1.Q3"), fio("7.6.FiO2.Q1"),
                 fio("7.6.FiO2.Q2"), fio("7.6.FiO2.Q3"), fio("7.6.FiO3.Q1")],
          misconceptions=["M_EQUIV_ADD", "M_EQUIV_DIFFERENT"])]))

# ============================== T8 Lowest terms (7.6) ========================================================
TOPICS.append(TOPIC(
    "T8", "M2", "Fractions in Lowest Terms", ["7.6"], "Apply",
    "Students decide whether a fraction is in lowest terms and reduce it by dividing the numerator and the "
    "denominator by common factors, in steps or in one go with the HCF.",
    "Divide top and bottom by their common factors until only 1 is common: 36/60 = 3/5.",
    [A("T8.C1", "Reducing a fraction to lowest terms", "Apply",
       "Students test whether a fraction is in lowest terms, reduce 16/20 and 36/60 in steps and in one go, and "
       "explain why both ways give the same answer.",
       textbook=book("7.6", H_LOW, stop=15),
       teach=["Predict first: can 16/20 be written with smaller numbers?",
              "A fraction is in lowest terms when the numerator and denominator have no common factor except 1.",
              "Divide both by a common factor; the fraction stays equal. Keep going until no common factor is left.",
              "In one go: divide by the highest common factor."],
       examples=[we("7.6.ex5"), we("7.6.ex6")],
       key_terms=["lowest terms", "simplest form", "common factor"], misconceptions=["M_LOWEST_PARTIAL"],
       minutes=10),
     DOER("T8.C2", "Pull it together and do it: Fraction Reducer", "fraction_reducer", "Apply",
          "Students divide the numerator and the denominator by common factors on the tool until the fraction is in "
          "lowest terms.",
          ["Divide top and bottom by the same common factor.",
           "Repeat until the only common factor is 1.",
           "Dividing by the HCF does it in one step."],
          items=[fio("7.6.FiO4.Q1")],
          misconceptions=["M_LOWEST_PARTIAL"])]))
