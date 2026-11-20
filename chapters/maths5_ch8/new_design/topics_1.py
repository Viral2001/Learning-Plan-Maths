# -*- coding: utf-8 -*-
"""Topics T1, T1B, T2 (module M1: Weight, Choosing Units and Reading Scales) and T3, T4, T5 (module M2, the first three
topics: Same Weight Different Units, Comparing Weights, Milligram Quintal and Tonne). The framing intro (Anu's weight
list hook and the free Weight Check), the short idea topic T1B (Gram or Kilogram with the Check! Check! question), Reading
Weighing Scales, Same Weight Different Units, Comparing Weights and Milligram Quintal and Tonne.
Every teaching concept has one worked example with the plan's own numbers (practice values); every book question is an FIO
item of its topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Does This Weight Look Right? (framing) ==================================
# The framing topic holds only the hook video and the free-try tool, and no book question. The concept video and
# Anu's Check! Check! question follow in the short idea topic T1B.
TOPICS.append(TOPIC(
    "T1", "M1", "Does This Weight Look Right?", ["Chapter opening"], "Understand",
    "",
    "Anu has written down the weight of each thing in her house. Some of the numbers look strange. Try the balance and "
    "find out which ones look right.",
    [A("T1.C1", "Anu's Weight List", "Understand",
       "",
       textbook=["Anu has recorded the weights of the items in her house. Check if she has recorded them correctly by "
                 "putting a tick against them if they look correct."],
       teach=["Predict first: Anu says her iron almirah weighs 40 g. Can that be right?",
              "Anu has recorded the weights of the items in her house: an iron almirah 40 g, a bed 60 kg, a rice bag 5 kg, "
              "a sofa 30 g, a bucket 1 kg 800 g, a water bottle 650 g and a refrigerator 50 g.",
              "Some of these weights look right. Some look very strange.",
              "Is Anu's list right? Think about it, then try the balance on the next screen."],
       ncert=["open.story"], key_terms=["weight", "gram", "kilogram"],
       video_focus=["HOOK"], enrichment=True, minutes=4),
     DOER("T1.C3", "Weight Check: Explore", "weight_check", "Understand",
          "",
          ["Anu has written the weight of each thing in her house.",
           "Put each thing on the balance against the 1 kg block.",
           "Find out which weights look right."],
          misconceptions=["M_UNIT_SIZE"], role="try_it", enrichment=True)],
    topic_type="framing", key_terms=["weight", "gram", "kilogram"]))

# ============================== T1B Grams and Kilograms ====================================================
TOPICS.append(TOPIC(
    "T1B", "M1", "Grams and Kilograms", ["Chapter opening"], "Understand",
    "Students choose gram or kilogram as the unit that fits the weight of a thing, and use 1 kg = 1,000 g to say which "
    "weights in Anu's list look right and which do not.",
    "Light things are weighed in grams and heavy things in kilograms. 1 kg is 1,000 g, so a number with kg is much more "
    "weight than the same number with g.",
    [A("T1B.C1", "Gram or Kilogram?", "Understand",
       "Students choose gram or kilogram as the unit that fits the weight of a thing, and say that 1 kg is 1,000 g, so "
       "6 kg is far more than 6 g.",
       teach=["Predict first: a pencil and a school bag are on the balance. Is the pencil 6 g or 6 kg? Is the school bag "
              "4 g or 4 kg?",
              "Grams are for light things. Kilograms are for heavy things.",
              "1 kg is 1,000 g. So 6 kg is 1,000 times as much weight as 6 g.",
              "Always read the number and the unit together. 40 g and 40 kg are very different weights.",
              "A thing as light as a pencil is weighed in grams. A thing as heavy as an almirah is weighed in kilograms.",
              "Rule: light things are weighed in grams, heavy things in kilograms, and 1 kg = 1,000 g."],
       examples=[WE("Which is the sensible weight of a pencil, 6 g or 6 kg? Which is the sensible weight of a school "
                    "bag, 4 g or 4 kg? Then say 4 kg in grams. These are practice values.",
                    ["1 kg is 1,000 g, so a kilogram is a big weight and a gram is a very small weight.",
                     "6 kg is 6 × 1,000 = 6,000 g. A pencil is much lighter than 6,000 g, so the pencil is 6 g.",
                     "4 g is even lighter than a pencil, and a school bag is not that light. The school bag is 4 kg.",
                     "4 kg in grams is 4 × 1,000 = 4,000 g.",
                     "Check: 4 kg and 4,000 g are the same weight, and the school bag is much heavier than the pencil."],
                    "The pencil is 6 g, the school bag is 4 kg, and 4 kg is 4,000 g")],
       key_terms=["gram", "kilogram", "unit", "weight"], misconceptions=["M_UNIT_SIZE"], minutes=5),
     DOER("T1B.C2", "Practice: Check! Check!", None, "Understand",
          "Students check a list of weights and tick those that look correct, and explain with grams and kilograms why "
          "a weight looks wrong.",
          ["Grams are for light things and kilograms are for heavy things.",
           "1 kg is 1,000 g, so a weight like 40 g is very small.",
           "Read the number and the unit together."],
          items=[FIO("open.check", "Check! Check!: Anu's list",
                     "Anu has recorded the weights of the items in her house. Check if she has recorded them correctly "
                     "by putting a tick against them if they look correct. 1. Iron Almirah: 40 g; 2. Bed: 60 kg; "
                     "3. Rice Bag: 5 kg; 4. Sofa: 30 g; 5. Bucket: 1 kg 800 g; 6. Water Bottle: 650 g; "
                     "7. Refrigerator: 50 g",
                     ["1 kg is 1,000 g. Use the 1 kg block as a guide: a thing that is heavier than the block must weigh "
                      "1 kg or more.",
                      "Iron Almirah: 40 g. An almirah is far heavier than 1 kg, but 40 g is much less than 1,000 g. This "
                      "does not look right.",
                      "Bed: 60 kg. A bed is heavy, and 60 kg is much more than 1 kg. This looks right.",
                      "Rice Bag: 5 kg. A rice bag is heavier than 1 kg, and 5 kg looks right.",
                      "Sofa: 30 g. A sofa is far heavier than 1 kg, but 30 g is much less than 1,000 g. This does not "
                      "look right.",
                      "Bucket: 1 kg 800 g. This is more than 1 kg, and a bucket can weigh this much. It looks right.",
                      "Water Bottle: 650 g. This is less than 1 kg, and a bottle of water can weigh this much. It looks "
                      "right.",
                      "Refrigerator: 50 g. A refrigerator is far heavier than 1 kg, but 50 g is much less than 1,000 g. "
                      "This does not look right.",
                      "Check: the three weights 40 g, 30 g and 50 g are all far less than 1,000 g, which is 1 kg."],
                     "Sample answer: ticks on Bed, Rice Bag, Bucket and Water Bottle; crosses on Iron Almirah, Sofa and "
                     "Refrigerator. Your answer may differ for the bed, the bucket and the bottle.",
                     kind="prompt",
                     q_figure="Anu's room with an iron almirah, a bed, a rice bag, a sofa, a bucket, a water bottle and a "
                              "refrigerator, and the list of seven recorded weights with an empty tick box beside each "
                              "one.",
                     s_figure="The same list with a tick beside Bed, Rice Bag, Bucket and Water Bottle and a cross beside "
                              "Iron Almirah, Sofa and Refrigerator.")],
          misconceptions=["M_UNIT_SIZE"])],
    key_terms=["gram", "kilogram", "unit", "weight"]))

# ============================== T2 Reading Weighing Scales ================================================
TOPICS.append(TOPIC(
    "T2", "M1", "Reading Weighing Scales", ["Let Us Do"], "Apply",
    "Students read a weighing scale by finding what one small mark stands for and counting the marks from 0 to the needle.",
    "On a scale with a needle, start at 0, find the last label the needle has passed, work out what one small mark stands "
    "for, and count the marks after the label.",
    [A("T2.C1", "Reading a Scale With a Needle", "Apply",
       "Students read a weighing scale with a needle by starting at 0, finding the last label the needle has passed, and "
       "counting the small marks after it.",
       teach=["Predict first: a scale has 0 at the top and the labels 1 kg, 2 kg, 3 kg, 4 kg and 5 kg round the face. The "
              "needle is past the 3 kg label. Is the weight 3 kg?",
              "No. The needle is past 3 kg, so the weight is more than 3 kg, and the small marks tell how much more.",
              "Start at 0, which is at the top, and follow the face clockwise. Find the last label the needle has passed.",
              "On this scale the gap between two labels has 5 equal parts, and each part is 200 g.",
              "The reading is the weight at the last label, plus the marks after it counted one by one.",
              "Rule: start at 0, find the last label the needle has passed, then count the marks after it."],
       examples=[WE("A scale has 0 at the top and the labels 1 kg to 5 kg round the face, so one full turn is 5 kg. "
                    "Between two labels there are 5 equal gaps. The needle is on the 3rd mark after the 3 kg label. What "
                    "is the weight? These are practice values.",
                    ["Between two labels there is 1 kg, which is 1,000 g, shared into 5 equal gaps. 1,000 ÷ 5 = 200 g, so "
                     "one mark is 200 g.",
                     "The last label the needle has passed is 3 kg. 3 kg is 3,000 g.",
                     "The needle is 3 marks after 3 kg. 3 × 200 = 600 g.",
                     "Add: 3,000 g + 600 g = 3,600 g, which is 3 kg 600 g.",
                     "Check: 3 kg 600 g is between the 3 kg label and the 4 kg label, and the needle is between them."],
                    "The weight is 3 kg 600 g")],
       ncert=["scale.note"], key_terms=["weighing scale", "needle", "label", "marks"],
       misconceptions=["M_NEAR_LABEL"], minutes=6),
     A("T2.C2", "What Does One Small Mark Stand For?", "Understand",
       "Students find what one small mark stands for by dividing the weight between two labels by the number of gaps, and "
       "then read a needle on that scale.",
       teach=["Predict first: the needle is on the 6th mark after 0 on two different scales. On one scale the weight is "
              "600 g. Can it be 60 g on the other?",
              "Yes. Different scales have different small marks. One small mark does not always stand for 1 g.",
              "To find what one mark stands for, take two labels that are next to each other. Find the weight between "
              "them and count the gaps between them.",
              "The weight between two labels, divided by the number of gaps, is the weight of one mark.",
              "Then read the needle: the last label it has passed, plus the marks counted times the weight of one mark.",
              "Rule: first find what one mark stands for, then count."],
       examples=[WE("A scale has a full turn of 2 kg. Its labels are 0, 500 g, 1 kg and 1 kg 500 g, and between two "
                    "labels there are 10 equal gaps. The needle is on the 7th mark after the 1 kg 500 g label. What does "
                    "one mark stand for, and what is the weight? These are practice values.",
                    ["The weight between two labels is 500 g, and there are 10 gaps.",
                     "500 ÷ 10 = 50 g, so one mark stands for 50 g.",
                     "The last label the needle has passed is 1 kg 500 g, which is 1,500 g.",
                     "The needle is 7 marks after that label. 7 × 50 = 350 g.",
                     "1,500 g + 350 g = 1,850 g, which is 1 kg 850 g.",
                     "Check: 1 kg 850 g is more than 1 kg 500 g and less than 2 kg, which is the full turn."],
                    "One mark stands for 50 g and the weight is 1 kg 850 g")],
       key_terms=["small mark", "gaps", "needle", "weight"], misconceptions=["M_MARK_IS_ONE", "M_NEAR_LABEL"],
       minutes=6),
     DOER("T2.C3", "Practice: Scale Reader", "scale_reader", "Apply",
          "Students read each weighing scale by finding what one mark stands for and counting the marks from 0 to the "
          "needle, and write the weight in g or in kg and g.",
          ["Start at 0 and find the weight between two labels.",
           "Divide that weight by the number of gaps to get the weight of one mark.",
           "Count the marks to the needle and write the weight."],
          items=[FIO("scale.read", "Let Us Do: reading the scales",
                     "Read the scales. Write the correct weight in the space given below. (a) ___ g (b) ___ kg ___ g "
                     "(c) ___ kg ___ g (d) ___ kg ___ g (e) ___ g (f) ___ g",
                     ["(a): The face has a full turn of 4 kg and 40 marks. 4 kg is 4,000 g and 4,000 ÷ 40 = 100 g, so "
                      "one mark is 100 g.",
                      "The needle is on the 6th mark after 0. 6 × 100 = 600 g.",
                      "(b): The face has a full turn of 2 kg and 20 marks. 2 kg is 2,000 g and 2,000 ÷ 20 = 100 g, so "
                      "one mark is 100 g.",
                      "The needle is on the 18th mark after 0. 18 × 100 = 1,800 g, which is 1 kg 800 g.",
                      "(c): The face has a full turn of 6 kg and 60 marks. 6 kg is 6,000 g and 6,000 ÷ 60 = 100 g, so "
                      "one mark is 100 g.",
                      "The needle is on the 25th mark after 0. 25 × 100 = 2,500 g, which is 2 kg 500 g.",
                      "(d): This face is the same as (a): a full turn of 4 kg and 40 marks, so one mark is 100 g.",
                      "The needle is on the 26th mark after 0. 26 × 100 = 2,600 g, which is 2 kg 600 g.",
                      "(e): The face has a full turn of 1 kg and 100 marks. 1 kg is 1,000 g and 1,000 ÷ 100 = 10 g, so "
                      "one mark is 10 g.",
                      "The needle is on the 15th mark after 0. 15 × 10 = 150 g.",
                      "(f): This face is the same as (e): a full turn of 1 kg and 100 marks, so one mark is 10 g.",
                      "The needle is on the 66th mark after 0. 66 × 10 = 660 g.",
                      "Check: (b), (c) and (d) are 1 kg or more, so they are written in kilograms and grams. (a), (e) and (f) are "
                      "less than 1 kg, so they are written in grams."],
                     "(a): 600 g; (b): 1 kg 800 g; (c): 2 kg 500 g; (d): 2 kg 600 g; (e): 150 g; (f): 660 g",
                     kind="exercise",
                     q_figure="Six round weighing scales labelled (a) to (f), each with 0 in red at the top, a needle and "
                              "an empty box below it for the weight: (a) has a full turn of 4 kg, the labels 1 kg, 2 kg, "
                              "3 kg and 4 kg every quarter turn and 40 small marks, with the needle on the 6th mark "
                              "after 0; (b) has a full turn of 2 kg, 1 kg at the bottom, 2 kg at the top and 20 small "
                              "marks, with the needle on the 18th mark; (c) has a full turn of 6 kg, the labels 1 kg to "
                              "6 kg and 60 small marks, with the needle on the 25th mark; (d) has the same face as (a), "
                              "with the needle on the 26th mark; (e) has a full turn of 1 kg, the labels 250 g, 500 g, "
                              "750 g and 1 kg and 100 small marks, with the needle on the 15th mark; (f) has the same "
                              "face as (e), with the needle on the 66th mark (marks counted clockwise from the 0).")],
          misconceptions=["M_MARK_IS_ONE", "M_NEAR_LABEL"])],
    key_terms=["weighing scale", "needle", "marks", "weight"]))

# ============================== T3 Same Weight, Different Units ===========================================
TOPICS.append(TOPIC(
    "T3", "M2", "Same Weight, Different Units", ["Different Units but Same Measure", "Let Us Find"], "Apply",
    "Students change kilograms to grams and grams to kilograms with a double number line, and write mixed weights such as "
    "6 kg 40 g in grams and back.",
    "1 kg is 1,000 g. To change kg to g multiply by 1,000, and to change g to kg divide by 1,000. A mixed weight keeps its g "
    "part in three places.",
    [A("T3.C1", "Kilograms and Grams", "Understand",
       "Students change a weight in kilograms to grams by multiplying by 1,000 and a weight in grams to kilograms by dividing "
       "by 1,000, and put both on a double number line.",
       textbook=["Bags are weighed on two different weighing balances. One weighing balance displays weight in kilograms and "
                 "other displays weight in grams."],
       teach=["Predict first: one bag is weighed on two balances. One balance shows 2 kg. What does the other balance, which "
              "shows grams, read?",
              "The same weight can be written in two units: 2 kg and 2,000 g are the same weight.",
              "1 kg is 1,000 g. To change kg to g, multiply by 1,000. To change g to kg, divide by 1,000.",
              "A double number line puts the two units on two lines. The top line is in kg and the bottom line is in g. Each "
              "mark has a kg number above and the matching g number below.",
              "Going from the top line to the bottom line is × 1,000. Going back is ÷ 1,000.",
              "Rule: kg to g, multiply by 1,000; g to kg, divide by 1,000."],
       examples=[WE("Use a double number line with 1 kg and 1,000 g. Find 4 kg in grams, 16 kg in grams and 9,000 g in "
                    "kilograms. These are practice values.",
                    ["1 kg is 1,000 g, so every kg on the top line matches 1,000 times as many g on the bottom line.",
                     "4 kg in grams: 4 × 1,000 = 4,000 g.",
                     "16 kg in grams: 16 × 1,000 = 16,000 g.",
                     "9,000 g in kilograms: 9,000 ÷ 1,000 = 9 kg.",
                     "Check: 9 × 1,000 = 9,000, so the number on each line matches the number on the other line."],
                    "4 kg is 4,000 g, 16 kg is 16,000 g and 9,000 g is 9 kg")],
       ncert=["units.same", "units.relation"], key_terms=["kilograms", "grams", "double number line"],
       misconceptions=["M_KG_100G"], minutes=6),
     A("T3.C2", "Mixed Weights in Grams, and Back", "Apply",
       "Students change a weight in kg and g to grams, keeping the g part in three places, and change grams to kg and g by "
       "taking out whole thousands.",
       teach=["Predict first: a weight is 6 kg 40 g. Is it 6,040 g or 6,400 g?",
              "Change the kg part first: 6 kg is 6 × 1,000 = 6,000 g. Then add the g part: 6,000 + 40 = 6,040 g.",
              "The g part takes three places because 1 kg is 1,000 g. 40 g is 040, so it goes next to the 6 as 6,040. 6,400 g "
              "would mean 6 kg 400 g.",
              "To go back, take out the whole thousands. 11,205 g has 11 thousands, so it is 11 kg, and 205 g are left over. "
              "11,205 g is 11 kg 205 g.",
              "Rule: kg to g, multiply by 1,000 and add the g part in three places; g to kg and g, take out the thousands."],
       examples=[WE("Change 6 kg 40 g to grams. Change 11,205 g to kilograms and grams. These are practice values.",
                    ["6 kg 40 g: change the 6 kg first. 6 × 1,000 = 6,000 g.",
                     "Add the gram part: 6,000 + 40 = 6,040 g. The g part 40 g takes three places, 040.",
                     "A slip to avoid: 6,400 g is 6 kg 400 g, which is a different weight.",
                     "11,205 g: take out the whole thousands. 11,205 − 11,000 = 205, so 11 thousands and 205 g are left over.",
                     "11 thousands of grams are 11 kg, so 11,205 g is 11 kg 205 g.",
                     "Check: 11 × 1,000 = 11,000 and 11,000 + 205 = 11,205."],
                    "6 kg 40 g is 6,040 g and 11,205 g is 11 kg 205 g")],
       key_terms=["mixed weights", "grams", "kilograms"], misconceptions=["M_PART_PLACE"], minutes=6),
     DOER("T3.C3", "Practice: Kilogram and Gram Line", "kg_g_line", "Apply",
          "Students change weights between kg and g on a double number line, match bags that have the same weight, and write "
          "mixed weights in grams and back.",
          ["1 kg is 1,000 g, so kilograms to grams is × 1,000 and g to kg is ÷ 1,000.",
           "Change the kg part first and add the g part in three places.",
           "To go back, take out the whole thousands."],
          items=[FIO("units.match", "Different Units but Same Measure (weight): match the bags",
                     "Bags are weighed on two different weighing balances. One weighing balance displays weight in "
                     "kilograms and other displays weight in grams. Match the bags that have the same weights. You can use "
                     "the double number line given below. Weighing Balance 1: 5 kg, 10 kg, 3 kg, 6 kg, 25 kg, 30 kg. "
                     "Weighing Balance 2: 3,000 g, 6,000 g, 10,000 g, 30,000 g, 5,000 g, 25,000 g.",
                     ["1 kg is 1,000 g, so kilograms to grams is × 1,000.",
                      "5 kg: 5 × 1,000 = 5,000 g, so 5 kg matches 5,000 g.",
                      "10 kg: 10 × 1,000 = 10,000 g, so 10 kg matches 10,000 g.",
                      "3 kg: 3 × 1,000 = 3,000 g, so 3 kg matches 3,000 g.",
                      "6 kg: 6 × 1,000 = 6,000 g, so 6 kg matches 6,000 g.",
                      "25 kg: 25 × 1,000 = 25,000 g, so 25 kg matches 25,000 g.",
                      "30 kg: 30 × 1,000 = 30,000 g, so 30 kg matches 30,000 g.",
                      "On the double number line: 3 kg is 3,000 g (× 3 on both lines), 8 kg is 8,000 g, 15,000 g is 15 kg, "
                      "20 kg is 20,000 g, 25,000 g is 25 kg and 30 kg is 30,000 g.",
                      "Check: every gram number is 1,000 times the kilogram number it matches."],
                     "5 kg: 5,000 g; 10 kg: 10,000 g; 3 kg: 3,000 g; 6 kg: 6,000 g; 25 kg: 25,000 g; 30 kg: 30,000 g",
                     kind="prompt",
                     q_figure="Two weighing balances each with a bag on it, one showing 2 kg and the other 2000 g; two "
                              "columns, Weighing Balance 1 with 5 kg, 10 kg, 3 kg, 6 kg, 25 kg and 30 kg and Weighing "
                              "Balance 2 with 3,000 g, 6,000 g, 10,000 g, 30,000 g, 5,000 g and 25,000 g; and a double "
                              "number line with kg above and g below, an arrow marked × 1000 between the lines, an arrow "
                              "× 3 from 1 kg to 3 kg and an arrow × ___ from 1,000 g to the next mark, with the kg marks "
                              "1 kg, 3 kg, 8 kg, a blank, 20 kg, a blank and 30 kg, and the g marks 1,000 g, a blank, a "
                              "blank, 15,000 g, a blank, 25,000 g and a blank, not drawn to scale.",
                     s_figure="The two columns joined by six lines, 5 kg to 5,000 g, 10 kg to 10,000 g, 3 kg to 3,000 g, "
                              "6 kg to 6,000 g, 25 kg to 25,000 g and 30 kg to 30,000 g, and the double number line with "
                              "every blank filled in."),
                 FIO("ex.shrenu", "Example 1: Shrenu's flour",
                     "Shrenu is baking cakes for her shop. She needs 3 kg 500 g flour. Her kitchen scale measures only in "
                     "grams. What should her kitchen scale show for 3 kg 500 g of flour?",
                     ["The scale measures only in grams, so change 3 kg 500 g to grams.",
                      "3 kg is 3 × 1,000 = 3,000 g.",
                      "Add the gram part: 3,000 + 500 = 3,500 g.",
                      "Check: 3,500 − 3,000 = 500, so 3,500 g is 3 kg 500 g."],
                     "The scale should show 3,500 g",
                     kind="example",
                     q_figure="Shrenu holding a whisk beside a bowl of flour on a kitchen scale whose display reads in "
                              "grams only."),
                 FIO("ex.flour", "Example 2: 2 kg 250 g of flour",
                     "What would be 2 kg 250 g flour in grams?",
                     ["Change the 2 kg first. 2 × 1,000 = 2,000 g.",
                      "Add the gram part: 2,000 + 250 = 2,250 g.",
                      "Check: 2,250 − 2,000 = 250, so 2,250 g is 2 kg 250 g."],
                     "2 kg 250 g is 2,250 g",
                     kind="example"),
                 FIO("lf1.sugar", "Let Us Find: sugar in grams",
                     "Shamim and Rehan observed someone buying sugar weighing 5 kg 50 g. They thought of the quantity in "
                     "grams. How much is it? One child says 5,050 g. The other says: No, it is 5,500 g. Who do you think "
                     "is right and why?",
                     ["5 kg 50 g: change the 5 kg first. 5 × 1,000 = 5,000 g.",
                      "Add the gram part. 50 g takes three places, 050. 5,000 + 50 = 5,050 g.",
                      "So 5 kg 50 g is 5,050 g, and the child who says 5,050 g is right.",
                      "The other child says 5,500 g. But 5,500 g is 5,000 g + 500 g, which is 5 kg 500 g, a different "
                      "weight.",
                      "Check: 5,050 − 5,000 = 50, so 50 g are left over after 5 kg."],
                     "5,050 g is right: 5 kg 50 g is 5,000 g + 50 g. 5,500 g would be 5 kg 500 g.",
                     kind="exercise"),
                 FIO("lf1.convert", "Let Us Find: conversions",
                     "Complete the conversions by filling in the blanks. You can use the double number line given below on "
                     "which some numbers have been marked. (a) 7 kg 67 g = ___ g (b) 3 kg 300 g = ___ g "
                     "(c) 8 kg 69 g = ___ g (d) 10,760 g = ___ kg ___ g (e) 4,080 g = ___ kg ___ g "
                     "(f) 12,042 g = ___ kg ___ g",
                     ["(a): 7 kg 67 g: 7 × 1,000 = 7,000 g, and 7,000 + 67 = 7,067 g.",
                      "(b): 3 kg 300 g: 3 × 1,000 = 3,000 g, and 3,000 + 300 = 3,300 g.",
                      "(c): 8 kg 69 g: 8 × 1,000 = 8,000 g, and 8,000 + 69 = 8,069 g.",
                      "(d): 10,760 g: take out the thousands. 10,760 − 10,000 = 760, so it is 10 kg 760 g.",
                      "(e): 4,080 g: 4,080 − 4,000 = 80, so it is 4 kg 80 g.",
                      "(f): 12,042 g: 12,042 − 12,000 = 42, so it is 12 kg 42 g.",
                      "Check with the double number line: 3 kg is 3,000 g, 4,000 g is 4 kg, 7 kg is 7,000 g, 8 kg is "
                      "8,000 g, 10,000 g is 10 kg and 12,000 g is 12 kg."],
                     "(a): 7,067 g; (b): 3,300 g; (c): 8,069 g; (d): 10 kg 760 g; (e): 4 kg 80 g; (f): 12 kg 42 g",
                     kind="exercise",
                     q_figure="A double number line, kg above and g below, with the marks 1 kg and 1,000 g, 3 kg and a "
                              "blank g, a blank kg and 4,000 g, 7 kg and a blank g, 8 kg and a blank g, a blank kg and "
                              "10,000 g, a blank kg and 12,000 g, and two more marks at the right end with blanks for kg "
                              "and g, not drawn to scale.")],
          misconceptions=["M_KG_100G", "M_PART_PLACE"])],
    key_terms=["kilograms", "grams", "double number line", "mixed weights"]))

# ============================== T4 Comparing Weights ======================================================
TOPICS.append(TOPIC(
    "T4", "M2", "Comparing Weights", ["Comparison between Different Weights"], "Apply",
    "Students compare weights given in different units by changing both to grams, and find the highest, the least and the "
    "order of a list of weights.",
    "To compare weights in different units, change both to the same unit, then compare the numbers. If a weight is a sum, work "
    "the sum out first.",
    [A("T4.C1", "Comparing Weights in Different Units", "Apply",
       "Students compare two weights given in different units by changing both to grams, use the signs <, = and >, and put "
       "weights in order.",
       teach=["Predict first: which is heavier, 4 kg 200 g or 4,020 g?",
              "You cannot compare the numbers 4,200 and 4,020 until both weights are in the same unit. Change both to grams.",
              "4 kg 200 g is 4,200 g. The other weight is already 4,020 g. 4,200 is more than 4,020, so 4 kg 200 g is heavier.",
              "If a weight is a sum, work out the sum first. 1 kg 250 g + 750 g is 1,250 + 750 = 2,000 g, which is 2 kg.",
              "To put weights in order, change all of them to grams and order the numbers.",
              "Rule: change to the same unit first, then compare the numbers."],
       examples=[WE("Compare 4 kg 200 g and 4,020 g. Then compare 1 kg 250 g + 750 g with 2 kg. Use <, = or >. These are "
                    "practice values.",
                    ["Change both weights to grams. 4 kg 200 g is 4 × 1,000 + 200 = 4,200 g.",
                     "The other weight is 4,020 g. Compare the numbers: 4,200 is more than 4,020.",
                     "So 4 kg 200 g > 4,020 g.",
                     "Work out the sum first. 1 kg 250 g is 1,250 g, and 1,250 + 750 = 2,000 g.",
                     "2 kg is 2 × 1,000 = 2,000 g.",
                     "2,000 g and 2,000 g are the same, so 1 kg 250 g + 750 g = 2 kg.",
                     "Check: 4,200 − 4,020 = 180, so the first weight is 180 g more."],
                    "4 kg 200 g > 4,020 g, and 1 kg 250 g + 750 g = 2 kg")],
       key_terms=["comparing weights", "different units", "grams"], misconceptions=["M_BIG_NUMBER"], minutes=5),
     DOER("T4.C2", "Practice: Comparing Weights", None, "Apply",
          "Students compare weights in different units using <, = and >, and find the highest, the least and the descending "
          "order of a list of weights.",
          ["Change both weights to the same unit.",
           "Compare the numbers and write <, = or >.",
           "To order a list, change every weight to grams first."],
          items=[FIO("cmp1.fruits", "Comparison between Different Weights: the picnic fruits",
                     "Harpreet's family planned a picnic over the weekend. Her mother and father packed different food "
                     "items to take along. The following is the list of fruits they carried. Watermelon: 3 kg; "
                     "Pineapple: 1 kg 750 g; Apples: 1 kg 250 g; Mangoes: 2 kg. Among the fruits they carried, which one "
                     "has the (a) highest weight? (b) least weight? (c) Arrange the items in descending order of their "
                     "weight.",
                     ["Change every weight to grams. Watermelon: 3 kg is 3,000 g.",
                      "Pineapple: 1 kg 750 g is 1,000 + 750 = 1,750 g.",
                      "Apples: 1 kg 250 g is 1,000 + 250 = 1,250 g.",
                      "Mangoes: 2 kg is 2,000 g.",
                      "Compare the numbers: 3,000 is the biggest and 1,250 is the smallest. 2,000 is more than 1,750.",
                      "(a): the highest weight is Watermelon.",
                      "(b): the least weight is Apples.",
                      "(c): the descending order, from the heaviest to the lightest, is Watermelon, Mangoes, Pineapple, "
                      "Apples.",
                      "Check: 3,000 > 2,000 > 1,750 > 1,250."],
                     "(a): Watermelon; (b): Apples; (c): Watermelon, Mangoes, Pineapple, Apples",
                     kind="prompt",
                     q_figure="A picnic mat with a watermelon, a pineapple, apples and mangoes, and a card listing "
                              "Watermelon 3 kg, Pineapple 1 kg 750 g, Apples 1 kg 250 g and Mangoes 2 kg."),
                 FIO("cmp1.signs", "Comparison between Different Weights: compare the weights",
                     "Compare the weights using <, =, > signs. (a) 1 kg 600 g ___ 1,700 g (b) 1 kg 600 g ___ 1 kg 60 g "
                     "(c) 10 kg 35 g ___ 10035 g (d) 1 kg 600 g ___ 2 kg 500 g (e) 5 kg 50 g ___ 4 kg 500 g "
                     "(f) 900 g + 7,000 g ___ 7 kg + 900 g",
                     ["Change the weights to grams and compare.",
                      "(a): 1 kg 600 g is 1,600 g. 1,600 is less than 1,700, so 1 kg 600 g < 1,700 g.",
                      "(b): 1 kg 60 g is 1,060 g. 1,600 is more than 1,060, so 1 kg 600 g > 1 kg 60 g.",
                      "(c): 10 kg 35 g is 10,000 + 35 = 10,035 g. It is the same as 10,035 g, so 10 kg 35 g = 10035 g.",
                      "(d): 1 kg 600 g is 1,600 g and 2 kg 500 g is 2,500 g. 1,600 is less than 2,500, so 1 kg 600 g < "
                      "2 kg 500 g.",
                      "(e): 5 kg 50 g is 5,050 g and 4 kg 500 g is 4,500 g. 5,050 is more than 4,500, so 5 kg 50 g > "
                      "4 kg 500 g.",
                      "(f): 900 g + 7,000 g is 7,900 g. 7 kg + 900 g is 7,000 + 900 = 7,900 g. They are the same, so "
                      "900 g + 7,000 g = 7 kg + 900 g.",
                      "Check: in every part both weights were changed to grams first."],
                     "(a): <; (b): >; (c): =; (d): <; (e): >; (f): =",
                     kind="prompt")],
          misconceptions=["M_BIG_NUMBER", "M_PART_PLACE"])],
    key_terms=["comparing weights", "grams", "units"]))

# ============================== T5 Milligram, Quintal and Tonne ===========================================
TOPICS.append(TOPIC(
    "T5", "M2", "Milligram, Quintal and Tonne", ["Milligram", "Let Us Find", "Did you know?", "From Tiny to Big"], "Apply",
    "Students change grams to milligrams, change between kilograms, quintals and tonnes, and use times as heavy to find a "
    "bigger or a smaller weight.",
    "1 g = 1,000 mg, 100 kg = 1 quintal and 10 quintals = 1 tonne = 1,000 kg. A weight that is n times as heavy is found by "
    "multiplying by n, and the smaller weight by dividing by n.",
    [A("T5.C1", "Milligram", "Understand",
       "Students change grams to milligrams by multiplying by 1,000, write a weight in g and mg in milligrams, and change "
       "milligrams back to g and mg.",
       textbook=["Ants weigh between 1 milligram and 5 milligrams. They can carry a lot more weight than their own weight.",
                 "1 g = 1,000 milligram (mg)",
                 "Converting g to mg is similar to converting kg to g."],
       teach=["Predict first: an ant weighs between 1 and 5 milligrams. Is a milligram bigger or smaller than a gram?",
              "A milligram is much smaller than a gram. 1 g = 1,000 mg.",
              "Very light things, like the medicine in a tablet or the gold in an ornament, are weighed in milligrams.",
              "Converting g to mg is just like converting kg to g: multiply by 1,000. 8 g is 8 × 1,000 = 8,000 mg.",
              "A mixed weight works the same way. 2 g 40 mg is 2,000 + 40 = 2,040 mg, and the mg part keeps three places.",
              "To go back, take out the thousands. 6,300 mg is 6 g 300 mg.",
              "Rule: g to mg, multiply by 1,000; mg to g, divide by 1,000."],
       examples=[WE("Change 8 g to milligrams, 2 g 40 mg to milligrams and 6,300 mg to g and mg. These are practice values.",
                    ["1 g is 1,000 mg, so grams to milligrams is × 1,000.",
                     "8 g: 8 × 1,000 = 8,000 mg.",
                     "2 g 40 mg: 2 × 1,000 = 2,000 mg. The mg part takes three places, 040. 2,000 + 40 = 2,040 mg.",
                     "6,300 mg: take out the whole thousands. 6,300 − 6,000 = 300, so it is 6 g 300 mg.",
                     "Check: 6 × 1,000 = 6,000 and 6,000 + 300 = 6,300."],
                    "8 g is 8,000 mg, 2 g 40 mg is 2,040 mg and 6,300 mg is 6 g 300 mg")],
       ncert=["mg.ants", "mg.what", "mg.similar", "mg.note"], key_terms=["milligram", "grams", "weighed"],
       misconceptions=["M_QUINTAL", "M_PART_PLACE"], minutes=5),
     A("T5.C2", "Quintal and Tonne", "Understand",
       "Students use 100 kg = 1 quintal, 10 quintals = 1 tonne and 1,000 kg = 1 tonne to change between kg, quintals and "
       "tonnes.",
       textbook=["100 kg = 1 quintal", "10 quintals = 1 tonne", "1,000 kg = 1 tonne"],
       teach=["Predict first: how many kg make 1 quintal, and how many quintals make 1 tonne?",
              "Very heavy things, like a load of wheat or a truck, are weighed in kg, quintals and tonnes.",
              "100 kg = 1 quintal. 10 quintals = 1 tonne. So 1 tonne is 10 × 100 = 1,000 kg.",
              "To change kg to quintals, divide by 100. To change quintals to tonnes, divide by 10. To change tonnes to kg, "
              "multiply by 1,000.",
              "Keep the facts in order, from tiny to big: 1,000 mg = 1 g, 1,000 g = 1 kg, 100 kg = 1 quintal, 10 quintals = "
              "1 tonne.",
              "Rule: 100 kg = 1 quintal, and 10 quintals = 1 tonne = 1,000 kg."],
       examples=[WE("Change 700 kg to quintals. Change 3 tonnes to kg. Change 20 quintals to tonnes and to kg. These are "
                    "practice values.",
                    ["100 kg is 1 quintal, so kg to quintals is ÷ 100.",
                     "700 kg: 700 ÷ 100 = 7 quintals.",
                     "1 tonne is 1,000 kg, so tonnes to kg is × 1,000.",
                     "3 tonnes: 3 × 1,000 = 3,000 kg.",
                     "10 quintals is 1 tonne, so quintals to tonnes is ÷ 10.",
                     "20 quintals: 20 ÷ 10 = 2 tonnes.",
                     "2 tonnes: 2 × 1,000 = 2,000 kg. Check: 20 × 100 = 2,000 kg."],
                    "700 kg is 7 quintals, 3 tonnes is 3,000 kg, and 20 quintals is 2 tonnes, which is 2,000 kg")],
       ncert=["qt.know", "units.table"], key_terms=["quintal", "tonne", "kilograms"], misconceptions=["M_QUINTAL"],
       minutes=5),
     A("T5.C3", "Times as Heavy", "Apply",
       "Students find a weight that is a number of times as heavy as another by multiplying, and find the smaller weight by "
       "dividing.",
       teach=["Predict first: a big load is 6 times as heavy as a load of 3,000 kg. Do you multiply or divide to find the "
              "big load?",
              "6 times as heavy means 6 loads of the same weight. Multiply: 3,000 × 6 = 18,000 kg.",
              "To go back, divide. If a load is 9 times as heavy as a small load, divide its weight by 9 to find the small "
              "load.",
              "Rule: n times as heavy, multiply to go up and divide to come back."],
       examples=[WE("A load is 6 times as heavy as a load of 3,000 kg. How heavy is it? Another load weighs 450 kg and is 9 "
                    "times as heavy as a small load. How heavy is the small load? These are practice values.",
                    ["6 times as heavy means 6 copies of 3,000 kg. Multiply: 3,000 × 6 = 18,000 kg.",
                     "The second load is 9 times as heavy as the small load, so 9 copies of the small load make 450 kg.",
                     "Divide to find one copy: 450 ÷ 9 = 50 kg.",
                     "Check: 50 × 9 = 450, the weight of the second load."],
                    "The first load is 18,000 kg and the small load is 50 kg")],
       key_terms=["times", "heavy", "multiply", "divide"], minutes=4),
     DOER("T5.C4", "Practice: Milligrams, Quintals and Tonnes", None, "Apply",
          "Students change weights between g, milligrams, kg, quintals and tonnes, compare weights in g and milligrams, and "
          "solve problems on times as heavy.",
          ["g to mg is × 1,000; 100 kg = 1 quintal; 10 quintals = 1 tonne = 1,000 kg.",
           "Change both weights to the same unit before comparing.",
           "n times as heavy: multiply to go up, divide to come back."],
          items=[FIO("lf2.sachet", "Let Us Find: sugar sachet",
                     "If a sugar sachet weighs 5 g, how much will it be in milligrams?",
                     ["1 g is 1,000 mg, so grams to milligrams is × 1,000.",
                      "5 × 1,000 = 5,000 mg.",
                      "Check: 5,000 ÷ 1,000 = 5 g."],
                     "A 5 g sugar sachet weighs 5,000 mg",
                     kind="exercise",
                     q_figure="A sugar sachet marked 5 g."),
                 FIO("lf2.mgline", "Let Us Find: double number line in mg",
                     "Complete the double number line below appropriately.",
                     ["1 g is 1,000 mg, so each gram on the bottom line matches 1,000 times as many milligrams on the top line.",
                      "5 g: 5 × 1,000 = 5,000 mg.",
                      "20,000 mg: 20,000 ÷ 1,000 = 20 g.",
                      "25 g: 25 × 1,000 = 25,000 mg.",
                      "31,000 mg: 31,000 ÷ 1,000 = 31 g.",
                      "Check: 12 g is 12 × 1,000 = 12,000 mg, which is the number already on the line."],
                     "Top line: 5,000 mg and 25,000 mg. Bottom line: 20 g and 31 g",
                     kind="exercise",
                     q_figure="A double number line, mg above and g below, with the marks 1000 mg and 1 g, a blank mg and "
                              "5 g, 12,000 mg and 12 g, 20,000 mg and a blank g, a blank mg and 25 g, 31,000 mg and a "
                              "blank g.",
                     s_figure="The same double number line with the blanks filled in: 5,000 mg, 20 g, 25,000 mg and 31 g."),
                 FIO("ex.ornament", "Example 3: the ornament",
                     "An ornament weighs 4 g 100 mg. What will be the weight in milligrams?",
                     ["Change the 4 g first. 4 × 1,000 = 4,000 mg.",
                      "Add the milligram part: 4,000 + 100 = 4,100 mg.",
                      "Check: 4,100 − 4,000 = 100 mg."],
                     "4,100 mg",
                     kind="example"),
                 FIO("lf2.goldsmith", "Let Us Find: the goldsmith's ornament",
                     "A goldsmith has made an ornament weighing 10 g 500 mg. What will its weight be in milligrams?",
                     ["Change the 10 g first. 10 × 1,000 = 10,000 mg.",
                      "Add the milligram part: 10,000 + 500 = 10,500 mg.",
                      "Check: 10,500 − 10,000 = 500 mg."],
                     "10,500 mg",
                     kind="exercise"),
                 FIO("lf2.compare", "Let Us Find: compare in g and mg",
                     "Compare the weights using <, =, > signs. (a) 20 g ___ 200 mg (b) 16 g 50 mg ___ 50 g 16 mg "
                     "(c) 2,010 mg ___ 2 g 100 mg (d) 9,000 mg ___ 90 g (e) 5,000 g ___ 7,500 g "
                     "(f) 800 mg + 88 mg ___ 880 mg + 8 mg",
                     ["Change both weights to the same unit and compare.",
                      "(a): 20 g is 20 × 1,000 = 20,000 mg. 20,000 is more than 200, so 20 g > 200 mg.",
                      "(b): 16 g 50 mg is 16,000 + 50 = 16,050 mg. 50 g 16 mg is 50,000 + 16 = 50,016 mg. 16,050 is less "
                      "than 50,016, so 16 g 50 mg < 50 g 16 mg.",
                      "(c): 2 g 100 mg is 2,000 + 100 = 2,100 mg. 2,010 is less than 2,100, so 2,010 mg < 2 g 100 mg.",
                      "(d): 9,000 mg is 9,000 ÷ 1,000 = 9 g. 9 g is less than 90 g, so 9,000 mg < 90 g.",
                      "(e): both are in grams. 5,000 is less than 7,500, so 5,000 g < 7,500 g.",
                      "(f): 800 mg + 88 mg is 888 mg and 880 mg + 8 mg is 888 mg. They are the same, so 800 mg + 88 mg = "
                      "880 mg + 8 mg.",
                      "Check: in every part both weights were in the same unit before they were compared."],
                     "(a): >; (b): <; (c): <; (d): <; (e): <; (f): =",
                     kind="exercise"),
                 FIO("lf2.whale", "Let Us Find: elephant and whale",
                     "Observe the pictures given below and fill in the blanks. An elephant weighs 5,000 kg. An arrow marked "
                     "× 40 goes from the elephant to a whale. The whale weighs ___ kg.",
                     ["The arrow × 40 means the whale weighs 40 times as much as the elephant, so multiply the elephant's "
                      "weight by 40.",
                      "5,000 × 40 = 200,000.",
                      "The whale weighs 200,000 kg.",
                      "Check: 200,000 ÷ 40 = 5,000, which is the weight of the elephant."],
                     "The whale weighs 200,000 kg",
                     kind="exercise",
                     q_figure="An elephant labelled 5,000 kg, a curved arrow marked × 40 from the elephant to a whale, and "
                              "a box labelled kg under the whale."),
                 FIO("lf2.quintal", "Let Us Find: kg, quintals and tonnes",
                     "Answer the following questions. (a) 5,000 kg = ___ quintals = ___ tonne (b) 9,000 kg = ___ quintals "
                     "(c) ___ kg = 8 tonnes",
                     ["100 kg is 1 quintal and 10 quintals is 1 tonne.",
                      "(a): 5,000 ÷ 100 = 50, so 5,000 kg is 50 quintals.",
                      "50 ÷ 10 = 5, so 50 quintals is 5 tonne.",
                      "(b): 9,000 ÷ 100 = 90, so 9,000 kg is 90 quintals.",
                      "(c): 1 tonne is 1,000 kg, so 8 tonnes is 8 × 1,000 = 8,000 kg.",
                      "Check: 5 × 1,000 = 5,000 kg and 90 × 100 = 9,000 kg."],
                     "(a): 50 quintals, 5 tonne; (b): 90 quintals; (c): 8,000 kg",
                     kind="exercise"),
                 FIO("king.weight", "King's Weight: the king's wheat",
                     "In a kingdom, the king donates wheat grains equal to 10 times his weight on his birthday. (a) If he "
                     "donates 800 kg of wheat grain this birthday, what is his current weight? ___ kg. (b) If he had "
                     "donated 780 kg of wheat grain on his last birthday, what was his weight last year? ___ kg. (c) How "
                     "much weight did he gain in a year until this birthday? ___ kg.",
                     ["The wheat weighs 10 times the king's weight, so divide the wheat by 10 to find his weight.",
                      "(a): 800 ÷ 10 = 80 kg.",
                      "(b): 780 ÷ 10 = 78 kg.",
                      "(c): he gained 80 − 78 = 2 kg in a year.",
                      "Check: 80 × 10 = 800 and 78 × 10 = 780."],
                     "(a): 80 kg; (b): 78 kg; (c): 2 kg",
                     kind="prompt")],
          misconceptions=["M_QUINTAL", "M_BIG_NUMBER"])],
    key_terms=["milligram", "quintal", "tonne", "times as heavy"]))
