# -*- coding: utf-8 -*-
"""Topics T9 to T13 (modules M3 and M4: comparing, adding, subtracting, history, summary). Sections 7.6 to 7.9."""
from topics_common import A, DOER, TOPIC, BOOK_TEXT, book, fio, we

TOPICS = []

H_SHARE = "Understanding equivalent fractions using equal shares"
H_ADD_SAME = "Adding fractions with the same fractional unit or denominator"
H_ADD_DIFF = "Adding fractions with different fractional units or denominators"
H_SUB_SAME = "Subtraction of fractions with the same fractional unit or denominator"
H_SUB_DIFF = "Subtraction of fractions with different fractional units or denominators"

# ============================== T9 Comparing fractions (7.6, 7.7) ============================================
TOPICS.append(TOPIC(
    "T9", "M3", "Comparing Fractions", ["7.6", "7.7"], "Analyze",
    "Students compare two fractions by thinking about shares and by rewriting both in the same fractional unit, "
    "then compare the numerators and put several fractions in order.",
    "To compare fractions, write them with the same denominator, then compare how many units each has.",
    [A("T9.C1", "Comparing shares of chikki", "Analyze",
       "Students decide which group's children get more chikki by writing 1/2 as 4/8, and explain why more units "
       "among the same children, or the same units among fewer children, gives a bigger share.",
       textbook=book("7.6", H_SHARE, start=38, stop=53),
       teach=["Predict first: 1 chikki between 2 children, or 5 chikkis among 8. Where is the share bigger?",
              "Write 1/2 as 4/8; then 4/8 < 5/8, so the second group gets more.",
              "Same units shared among more children gives less: 4/7 > 4/8 = 1/2.",
              "More units among the same children gives more: 1/5 < 2/5 and 3/7 < 4/7."],
       examples=[we("7.6.ex2"), we("7.6.ex3"), we("7.6.q12")],
       key_terms=["compare", "share"], misconceptions=["M_COMPARE_PARTS", "M_BIG_DENOM"], minutes=12),
     A("T9.C2", "Making the fractional units the same", "Apply",
       "Students compare fractions such as 3/4 and 7/10, 4/5 and 7/9, by writing equivalent fractions with a "
       "common denominator, and state the two steps of comparing.",
       textbook=book("7.6", H_SHARE, start=53, stop=70) + book("7.7") + book("7.7", "Let's Summarise!"),
       teach=["Predict first: which is greater, 3/4 or 7/10?",
              "Fractions are easy to compare when the fractional unit is the same.",
              "Go up to a common multiple of the denominators: 3/4 = 15/20 and 7/10 = 14/20, so 3/4 > 7/10.",
              "Step 1: make the denominators the same. Step 2: compare the numerators."],
       examples=[we("7.6.q13"), we("7.6.ex4"), we("7.7.q1"), we("7.7.q2")],
       key_terms=["common denominator", "common multiple"], misconceptions=["M_COMPARE_PARTS"], minutes=12),
     DOER("T9.C3", "Pull it together and do it: Fraction Comparator", "fraction_comparator", "Analyze",
          "Students re-cut two fractions into a common unit on the tool, compare them, and put sets of fractions in "
          "ascending and descending order.",
          ["Find a common multiple of the denominators.",
           "Rewrite each fraction with that denominator.",
           "Compare the numerators: more units means the bigger fraction."],
          items=[fio("7.6.q14"), fio("7.7.FiO.Q1"), fio("7.7.FiO.Q2"), fio("7.7.FiO.Q3")],
          misconceptions=["M_COMPARE_PARTS", "M_BIG_DENOM"])]))

# ============================== T10 Adding fractions (7.8) ===================================================
TOPICS.append(TOPIC(
    "T10", "M3", "Adding Fractions", ["7.8"], "Apply",
    "Students add fractions with the same fractional unit by counting units, and add fractions with different "
    "units by Brahmagupta's method: make the units the same, add the numerators, then simplify.",
    "Same unit: add the units. Different units: first rewrite in a common unit (Brahmagupta's method).",
    [A("T10.C1", "Adding fractions with the same unit", "Apply",
       "Students add fractions with the same denominator using strips and the number line, by counting the "
       "fractional units, and write a sum greater than 1 as a mixed number.",
       textbook=book("7.8") + book("7.8", H_ADD_SAME),
       teach=["Predict first: Meena ate 1/2 and her brother 1/4 of a chikki. How much did they eat together?",
              "Cut the half into two quarters: 1/2 + 1/4 = 3 × 1/4 = 3/4, and 1/4 is left.",
              "With the same unit, just count units: 2/5 + 1/5 = 3/5.",
              "4/7 + 6/7 = 10/7 = 1 + 3/7. Jumps on the number line give the same answer."],
       examples=[we("7.8.q1"), we("7.8.q2"), we("7.8.ex1"), we("7.8.ex2"), we("7.8.q3")],
       key_terms=["sum", "fractional unit"], misconceptions=["M_ADD_TOPS_BOTTOMS"], minutes=12),
     A("T10.C2", "Brahmagupta's method for adding", "Apply",
       "Students add fractions with different denominators by rewriting them with a common multiple of the "
       "denominators, adding the numerators, and giving the answer in lowest terms.",
       textbook=book("7.8", H_ADD_DIFF),
       teach=["Predict first: is 1/4 + 1/3 equal to 2/7? Keeko thinks so.",
              "Different units cannot be counted together. Rewrite: 1/4 = 3/12 and 1/3 = 4/12.",
              "Now count twelfths: 3/12 + 4/12 = 7/12. Keeko's 2/7 is less than 1/3 alone, so it cannot be right.",
              "Brahmagupta, in 628 CE: make the units the same, add the numerators, simplify."],
       examples=[we("7.8.ex3"), we("7.8.ex4"), we("7.8.ex5")],
       key_terms=["Brahmagupta's method", "common denominator"],
       misconceptions=["M_ADD_TOPS_BOTTOMS", "M_SAME_UNIT_ONLY"], minutes=12),
     DOER("T10.C3", "Pull it together and do it: Fraction Bar Combiner", "unit_adder", "Apply",
          "Students re-cut fraction bars into a common unit on the tool, slide the units together, and write the "
          "sum in lowest terms or as a mixed number.",
          ["Same unit: add the numerators, keep the denominator.",
           "Different units: rewrite with a common multiple of the denominators first.",
           "Give the answer in lowest terms."],
          items=[fio("7.8.FiO1.Q1"), fio("7.8.FiO1.Q2"), fio("7.8.FiO1.Q3")],
          misconceptions=["M_ADD_TOPS_BOTTOMS", "M_SAME_UNIT_ONLY"])]))

# ============================== T11 Subtracting fractions (7.8) ==============================================
TOPICS.append(TOPIC(
    "T11", "M3", "Subtracting Fractions", ["7.8"], "Apply",
    "Students subtract fractions with the same fractional unit by taking away units, and subtract fractions with "
    "different units by Brahmagupta's method, explaining why each fraction is multiplied as it is.",
    "Subtract like adding: make the units the same, then take away the numerators and keep the denominator.",
    [A("T11.C1", "Subtracting fractions with the same unit", "Apply",
       "Students subtract fractions with the same denominator by removing units on a strip and by jumping back on "
       "the number line.",
       textbook=book("7.8", H_SUB_SAME),
       teach=["Predict first: what is left when you take 4/7 from 6/7?",
              "Both are in sevenths, so remove 4 of the 6 shaded sevenths: 2 are left, 6/7 − 4/7 = 2/7.",
              "On the number line, start at 6/7 and jump back 4 sevenths to land on 2/7."],
       examples=[we("7.8.q4"), we("7.8.q5")],
       key_terms=["difference"], misconceptions=["M_SUB_TOPS_BOTTOMS"], minutes=10),
     A("T11.C2", "Brahmagupta's method for subtracting", "Analyze",
       "Students subtract fractions with different denominators by converting both to a common unit, and explain "
       "why 3/4 is multiplied by 3/3 and 2/3 by 4/4.",
       textbook=book("7.8", H_SUB_DIFF),
       teach=["Predict first: what is 3/4 − 2/3? Is it more or less than 1/4?",
              "Rewrite in twelfths: 3/4 = 9/12 and 2/3 = 8/12.",
              "Then 9/12 − 8/12 = 1/12.",
              "Multiplying 3/4 by 3 over 3 turns the denominator into 12, a common multiple of 4 and 3."],
       examples=[we("7.8.ex6"), we("7.8.q6"), we("7.8.q7")],
       key_terms=["Brahmagupta's method", "common denominator"],
       misconceptions=["M_SUB_TOPS_BOTTOMS", "M_SAME_UNIT_ONLY"], minutes=12),
     DOER("T11.C3", "Pull it together and do it: Fraction Bar Combiner", "unit_subtractor", "Apply",
          "Students re-cut fraction bars into a common unit on the tool, take away units, and write the difference "
          "in lowest terms, including word problems about distance and time.",
          ["Same unit: subtract the numerators, keep the denominator.",
           "Different units: rewrite with a common multiple first.",
           "Simplify the answer to lowest terms."],
          items=[fio("7.8.FiO2.Q1"), fio("7.8.FiO2.Q2"), fio("7.8.FiO2.Q3"), fio("7.8.FiO3.Q1"),
                 fio("7.8.FiO3.Q2"), fio("7.8.FiO3.Q3")],
          misconceptions=["M_SUB_TOPS_BOTTOMS", "M_SAME_UNIT_ONLY"])]))

# ============================== T12 A pinch of history (7.9) =================================================
TOPICS.append(TOPIC(
    "T12", "M4", "A Pinch of History and the Unit Fraction Puzzle", ["7.9"], "Analyze",
    "Students recall how fractions were named and written in India and how they reached the world, then find "
    "different fractional units that add up to 1.",
    "Fractions were called bhinna in India; Egyptians used unit fractions, and 1/2 + 1/3 + 1/6 = 1.",
    [A("T12.C1", "Fractions in India's history", "Remember",
       "Students name the old Indian words for fraction, describe the Indian way of writing fractions, and state "
       "Brahmagupta's rule for adding and subtracting.",
       textbook=book("7.9"),
       teach=["Predict first: what do you think a fraction was called in ancient India?",
              "Bhinna, meaning broken, and also bhaga or ansha, meaning part.",
              "The Indian way of writing one number over another came to the world through the Arabs; Al-Hassar "
              "added the line between them.",
              "Brahmagupta's rule for adding and subtracting with a common denominator is what we use today."],
       examples=[we("7.9.q1")],
       key_terms=["bhinna", "unit fraction"], misconceptions=[], minutes=8),
     DOER("T12.C2", "Pull it together and do it: Unit Fraction Puzzle", "unit_fraction_puzzle", "Analyze",
          "Students fill a circle with different fractional units on the tool to find three and four different "
          "unit fractions that add up to 1.",
          ["Two different fractional units can never add to 1.",
           "Three different units add to 1 in only one way: 1/2 + 1/3 + 1/6.",
           "Four different units add to 1 in six ways."],
          items=[fio("7.9.q2"), fio("7.9.q3"), fio("7.9.q4")],
          misconceptions=["M_ADD_TOPS_BOTTOMS"])]))

# ============================== T13 Summary ==================================================================
TOPICS.append(TOPIC(
    "T13", "M4", "Summary: Fractions", ["Summary"], "Remember",
    None,
    "Equal shares and fractional units, the number line, mixed numbers, equivalent fractions, lowest terms, and "
    "Brahmagupta's way to compare, add and subtract.",
    [A("T13.C1", "What we found about fractions", "Remember",
       "Students restate the meaning of a fractional unit, the numerator and the denominator, mixed numbers, "
       "equivalent fractions and lowest terms, and Brahmagupta's method for adding and subtracting.",
       textbook=["Let's Summarise!"] + BOOK_TEXT["extra_inv_C.json"]["summary_points"],
       teach=["Our opening question is settled: when more children share one roti, each share is smaller, so 1/2 > "
              "1/4.",
              "Every fraction counts fractional units; equal shares in different units are equivalent fractions.",
              "To compare, add or subtract, make the units the same first.",
              "Still open for you: can you find all six ways to write 1 as four different unit fractions?"],
       ncert=["summary"], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
