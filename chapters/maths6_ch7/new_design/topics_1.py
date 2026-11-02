# -*- coding: utf-8 -*-
"""Topics T1 to T5 (module M1: fractional units and equal shares). Book sections 7.1 to 7.4."""
from topics_common import A, DOER, TOPIC, BOOK_TEXT, book, fio, we

TOPICS = []

# ============================== T1 Introduction ==============================================================
TOPICS.append(TOPIC(
    "T1", "M1", "Sharing Rotis Fairly", ["Chapter opening"], "Understand",
    "",
    "One roti, a few hungry children and a fair share for each: how big is one share, and which share is bigger?",
    [A("T1.C1", "One roti, many children", "Remember", "",
       textbook=BOOK_TEXT["extra_inv_A.json"]["opening"]["textbook_lines"][:3],
       teach=["Picture one roti on a plate and two children waiting. Each must get exactly the same amount.",
              "Make a guess before the next step: if four children share the roti instead, does each get more or "
              "less? How would you write that share?"],
       ncert=["opening"], key_terms=["share", "half"], video_focus=["HOOK"], minutes=4, enrichment=True)],
    topic_type="framing"))

# ============================== T2 Fractional units and equal shares (7.1) ===================================
TOPICS.append(TOPIC(
    "T2", "M1", "Fractional Units and Equal Shares", ["7.1"], "Apply",
    "Students find the share each person gets when one whole is divided equally, name it as a fractional unit, and "
    "explain why sharing among more people gives a smaller unit.",
    "One whole shared equally among n people gives each the fractional unit 1/n; more sharers means smaller shares.",
    [A("T2.C1", "Halves and quarters of a roti", "Understand",
       "Students find each child's share when one roti is shared equally among 2 and among 4 children, write the "
       "shares as 1/2 and 1/4, and say which share is more.",
       textbook=BOOK_TEXT["extra_inv_A.json"]["opening"]["textbook_lines"],
       teach=["Predict first: two children or four children sharing one roti, who gets the bigger piece?",
              "Cut the roti into 2 equal parts: each part is 1/2 roti, read 'one half' or 'one upon two'.",
              "Cut it into 4 equal parts: each part is 1/4 roti.",
              "The same roti shared by more children gives each a smaller share, so 1/2 > 1/4."],
       examples=[we("7.0.ex1")],
       key_terms=["half", "quarter", "share"], misconceptions=["M_BIG_DENOM", "M_UNEQUAL_PARTS"], minutes=8),
     A("T2.C2", "Fractional units: more sharers, smaller share", "Analyze",
       "Students define a fractional unit, compare unit fractions such as 1/5 and 1/9 by thinking of shares, and "
       "collect the words for fractions used in their own languages.",
       textbook=book("7.1") + book("7.1", "Knowledge from the past!"),
       teach=["Predict first: which is greater, 1/5 or 1/9? Arvin says 1/9, because 9 is bigger than 5.",
              "Think of shares: 1/5 is one child's share when 5 children share a roti, 1/9 when 9 children share it.",
              "More children sharing the same roti means less for each, so 1/9 < 1/5.",
              "When one unit is divided into equal parts, each part is a fractional unit, also called a unit "
              "fraction.",
              "Fractions have Indian names from long ago: 3/4 is tri-pada in the Rig Veda, teen paav in Hindi and "
              "mukkaal in Tamil."],
       examples=[we("7.1.ex1"), we("7.1.q1")],
       key_terms=["fractional unit", "unit fraction"], misconceptions=["M_BIG_DENOM"], minutes=10),
     DOER("T2.C3", "Pull it together and do it: Equal Share Roti Dealer", "equal_share", "Apply",
          "Students share one whole equally on the tool, name each share as a fractional unit, and pick the bigger "
          "of two shares of the same whole.",
          ["One whole shared equally among n people gives each 1/n.",
           "The more people share, the smaller each share: 1/9 < 1/5.",
           "Several shares of 1/n are counted: 3 × 1/4 = 3/4."],
          items=[fio("7.1.FiO.Q1"), fio("7.1.FiO.Q2"), fio("7.1.FiO.Q3"), fio("7.1.FiO.Q4"), fio("7.1.FiO.Q5")],
          misconceptions=["M_BIG_DENOM", "M_UNEQUAL_PARTS"])]))

# ============================== T3 Fractional units as parts of a whole (7.2) ================================
TOPICS.append(TOPIC(
    "T3", "M1", "Fractional Units as Parts of a Whole", ["7.2"], "Apply",
    "Students name a piece of a whole chikki as a fractional unit by finding how many equal copies of it make the "
    "whole, and measure a bigger piece in those units.",
    "A piece is 1/n of the whole when n equal copies of it make the whole, whatever its shape.",
    [A("T3.C1", "Measuring a chikki piece in quarters", "Apply",
       "Students find what fraction of a chikki each of two pieces is, by seeing how many copies of the small piece "
       "fill the whole, and explain why equal-sized pieces of different shapes are the same fraction.",
       textbook=book("7.2", start=0, stop=6),
       teach=["Predict first: the chikki breaks into a small rectangle and a big L-shaped piece. How much of the "
              "whole is each?",
              "Four copies of the small piece fill the whole chikki, so the small piece is 1/4.",
              "The bigger piece holds 3 of those quarters, so it is 3 × 1/4 = 3/4 chikki.",
              "Pieces of different shapes are the same fraction when they cover the same amount of the whole."],
       examples=[we("7.2.ex1"), we("7.2.q1")],
       key_terms=["fractional unit", "whole"], misconceptions=["M_COUNT_PIECES", "M_UNEQUAL_PARTS"], minutes=10),
     A("T3.C2", "Naming the fractional unit of a piece", "Apply",
       "Students name a piece as 1/n by counting how many equal pieces of that size make the whole chikki, and "
       "check the count with the small squares.",
       textbook=book("7.2", start=6),
       teach=["Predict first: one strip of the chikki is shown. How many such strips make the whole?",
              "Three equal strips make the whole, so one strip is 1/3 chikki.",
              "Check with squares: the strip has 8 small squares and 3 × 8 = 24, the whole chikki."],
       examples=[we("7.2.ex2")],
       key_terms=["fractional unit"], misconceptions=["M_COUNT_PIECES"], minutes=8),
     DOER("T3.C3", "Pull it together and do it: Chikki Part Namer", "chikki_namer", "Apply",
          "Students lay copies of a chikki piece across the whole on the tool and name each piece as a fractional "
          "unit, including triangles and L-shapes.",
          ["A piece is 1/n when n equal copies of it make the whole.",
           "Count small squares: the whole has 24, so a piece of 3 squares is 1/8.",
           "Shape does not matter, only how much of the whole the piece covers."],
          items=[fio("7.2.FiO.Q1")],
          misconceptions=["M_COUNT_PIECES", "M_UNEQUAL_PARTS"])]))

# ============================== T4 Measuring using fractional units (7.3) ====================================
TOPICS.append(TOPIC(
    "T4", "M1", "Measuring Using Fractional Units", ["7.3"], "Apply",
    "Students fold a paper strip into equal parts to make fractional units, measure lengths by collecting copies of "
    "a unit, write k × 1/n as k/n, and name the numerator and denominator.",
    "A fraction collects copies of one fractional unit: 3/4 is 3 × 1/4, three quarters.",
    [A("T4.C1", "Folding a strip into halves, quarters and eighths", "Apply",
       "Students fold a unit strip into 2, 4 and 8 equal parts, name each part, and write the lengths of several "
       "parts together as multiples of the unit, such as 3 × 1/8 = 3/8.",
       textbook=book("7.3", start=0, stop=7),
       teach=["Predict first: fold a strip in half, then in half again. How many parts, and how long is each?",
              "One fold gives 2 parts of 1/2. Folding again gives 4 parts of 1/4, and once more gives 8 parts of 1/8.",
              "Several parts together are counted in the unit: 3 × 1/4 = 3/4 and 8 × 1/8 = 8/8 = 1."],
       examples=[we("7.3.ex1"), we("7.3.ex2"), we("7.3.q1")],
       key_terms=["fractional unit", "fold"], misconceptions=["M_COUNT_PIECES"], minutes=12),
     A("T4.C2", "Collecting halves, and reading fractions", "Understand",
       "Students write repeated halves as addition statements, read a fraction such as 3/4 as 3 × 1/4, and name the "
       "numerator and the denominator.",
       textbook=book("7.3", start=7) + book("7.3", "Reading Fractions", stop=2),
       teach=["Predict first: five half rotis, how much roti is that?",
              "Each half roti is the unit 1/2; adding one more half counts the units: 1/2 + 1/2 + 1/2 = 3 × 1/2.",
              "Reading 3/4 as 3 × 1/4 shows the unit (1/4) and how many units there are (3).",
              "In 5/6, 5 is the numerator, the number of units taken, and 6 is the denominator, how many equal parts "
              "make one whole."],
       examples=[we("7.3.ex3")],
       key_terms=["numerator", "denominator"], misconceptions=["M_NUM_DENOM", "M_LESS_THAN_ONE"], minutes=10),
     DOER("T4.C3", "Pull it together and do it: Folding Strip Builder", "strip_measurer", "Apply",
          "Students fold a strip into equal parts on the tool, lay copies of one part from the left, and write the "
          "length as k × 1/n = k/n, including lengths past one whole.",
          ["Folding into n equal parts makes the unit 1/n.",
           "k copies of 1/n make k/n: count the parts, not the folds.",
           "When k is more than n the length is more than one whole."],
          items=[fio("7.3.FiO.Q1"), fio("7.3.FiO.Q2"), fio("7.3.FiO.Q3"), fio("7.3.FiO.Q4"), fio("7.3.FiO.Q5")],
          misconceptions=["M_COUNT_PIECES", "M_NUM_DENOM"])]))

# ============================== T5 Fractions on the number line (7.4) ========================================
TOPICS.append(TOPIC(
    "T5", "M1", "Marking Fraction Lengths on the Number Line", ["7.4"], "Apply",
    "Students divide the unit from 0 to 1 on the number line into equal parts, find the length of a line from 0 "
    "as a fraction, and mark given fractions by counting gaps.",
    "On the number line k/n is k equal gaps of 1/n from 0; count the gaps, never the marks.",
    [A("T5.C1", "Halves and thirds on the number line", "Apply",
       "Students find the length of a line from 0 when the unit is divided into 2 or 3 equal parts, by counting the "
       "equal gaps it covers.",
       textbook=book("7.4", start=0, stop=5),
       teach=["Predict first: a blue line starts at 0 and stops at the first mark between 0 and 1. How long is it?",
              "The distance from 0 to 1 is one unit. Divided into 2 equal parts, each part is 1/2 unit.",
              "With 3 equal parts each gap is 1/3, and a line covering 2 gaps is 2 × 1/3 = 2/3 unit.",
              "Count the gaps the line covers, not the marks it passes."],
       examples=[we("7.4.ex1"), we("7.4.q1")],
       key_terms=["number line", "unit"], misconceptions=["M_TICKS_NOT_GAPS"], minutes=10),
     A("T5.C2", "Fifths and eighths on the number line", "Apply",
       "Students write the fractions for the marks when a unit is divided into 5 and into 8 equal parts, and see "
       "that the last mark is n/n, which is 1.",
       textbook=book("7.4", start=5),
       teach=["Predict first: a unit is cut into 8 equal parts. What fraction is the third mark from 0?",
              "Each gap is 1/8, so the mark after n gaps is n/8.",
              "The eighth mark is 8/8, which is the whole unit, 1."],
       examples=[we("7.4.q2"), we("7.4.q3")],
       key_terms=["number line", "fifth", "eighth"], misconceptions=["M_TICKS_NOT_GAPS"], minutes=10),
     DOER("T5.C3", "Pull it together and do it: Number Line Marker", "number_line_marker", "Apply",
          "Students cut the unit into equal gaps on the tool, hop from 0 to mark fractions, and read the length of "
          "lines that end before or after 1.",
          ["Cut 0 to 1 into as many equal gaps as the denominator.",
           "Hop as many gaps from 0 as the numerator.",
           "Lines past 1 keep counting gaps: halfway between 1 and 2 is 3/2."],
          items=[fio("7.4.FiO.Q1"), fio("7.4.FiO.Q2"), fio("7.4.FiO.Q3"), fio("7.4.FiO.Q4"), fio("7.4.FiO.Q5")],
          misconceptions=["M_TICKS_NOT_GAPS", "M_LESS_THAN_ONE"])]))
