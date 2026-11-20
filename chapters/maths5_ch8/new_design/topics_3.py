# -*- coding: utf-8 -*-
"""Topics T9 to T12 (module M3: Capacity, Litres and Millilitres): Measuring Capacity (which unit), Litres and Millilitres
(changing, mixed capacities, container scales), Comparing and Combining Capacities (the petrol pump) and Multiplying and
Dividing Capacities (Let Us Solve). Every teaching concept has one worked example with the plan's own numbers (practice
values); every book question is an FIO item of its topic's DOER, in the book's order. The litre is the letter l after a
number and the word litre in a sentence; no decimals are used anywhere."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T9 Measuring Capacity =====================================================
TOPICS.append(TOPIC(
    "T9", "M3", "Measuring Capacity", ["Measuring Capacity"], "Understand",
    "Students choose the unit, litre or millilitre, for the capacity of a container, and use 1 l = 1,000 ml.",
    "Capacity is how much a container holds. Small amounts are measured in millilitres and big amounts in litres, and "
    "1 l = 1,000 ml.",
    [A("T9.C1", "Litre or Millilitre?", "Understand",
       "Students say that capacity is how much a container holds, choose litre or millilitre for the thing being measured, "
       "and use 1 l = 1,000 ml.",
       teach=["Predict first: a cup of juice and a big drum of water. Which one holds 200 ml and which one holds 200 l?",
              "Capacity is how much a container can hold. Water, milk and juice are measured by capacity.",
              "The small unit is the millilitre, ml. The big unit is the litre, l. 1 l = 1,000 ml.",
              "Use ml for small amounts, like a cup. Use l for big amounts, like a drum or a bucket.",
              "Read the number and the unit together. 200 l is 200 × 1,000 = 200,000 ml, which is far too much for a cup.",
              "Rule: ml for small amounts, l for big amounts, and 1 l = 1,000 ml."],
       examples=[WE("A cup of juice holds 200 ml or 200 l? A drum of water holds 200 ml or 200 l? These are practice values.",
                    ["1 l is 1,000 ml, so a litre is a big amount and a millilitre is a very small amount.",
                     "200 l is 200 × 1,000 = 200,000 ml. A cup cannot hold 200,000 ml, so a cup of juice holds 200 ml.",
                     "A drum holds much more than a cup. 200 ml is a small amount, so a drum holds 200 l.",
                     "Check: 200 ml is far less than 1 l, and 200 l is far more than 1 l."],
                    "The cup holds 200 ml and the drum holds 200 l")],
       key_terms=["capacity", "litre", "millilitre", "container"], misconceptions=["M_UNIT_SIZE"], minutes=5),
     DOER("T9.C2", "Practice: Which Unit?", None, "Understand",
          "Students choose the unit, litre or millilitre, for the capacity of a container, and explain why an amount does not "
          "fit a container.",
          ["ml is for small amounts and l is for big amounts.",
           "1 l = 1,000 ml, so 20 ml is a very small amount.",
           "Read the number and the unit together."],
          items=[FIO("cap.tea", "Measuring Capacity: tea for 2 cups",
                     "You must have seen tea being prepared at your home. How much water and milk do we need to make 2 cups "
                     "of tea? Do we need 1 l of water to make 2 cups of tea? Is 500 ml of water enough for 2 cups of tea?",
                     ["A cup is small, so two cups need only a small amount of water and milk.",
                      "1 l is 1,000 ml. That is far more than two cups need, so we do not need 1 l of water.",
                      "Take a cup of about 150 ml (a practice value; cups are not all the same). Two cups hold "
                      "2 × 150 = 300 ml.",
                      "For example, 200 ml of water and 100 ml of milk make 200 + 100 = 300 ml.",
                      "300 ml is less than 500 ml, so 500 ml of water is enough for 2 cups, and it is more than enough.",
                      "Check: 300 ml is less than 500 ml, and 500 ml is less than 1,000 ml."],
                     "Sample answer: about 300 ml in all (200 ml of water, 100 ml of milk). No, 1 l is not needed. Yes, "
                     "500 ml is enough. Your answer may differ.",
                     kind="prompt"),
                 FIO("cap.bucket", "Measuring Capacity: the bucket",
                     "A bucket can hold a maximum of 20 ml of water. Is this statement correct? Which unit should be used in "
                     "such a situation?",
                     ["20 ml is a very small amount, and a bucket holds much more than that.",
                      "A water bottle of 500 ml holds 25 times as much as 20 ml, because 500 ÷ 20 = 25.",
                      "A bucket holds much more than a water bottle, so it cannot hold at most 20 ml. The statement is not "
                      "correct.",
                      "A bucket holds a big amount, so the unit to use is the litre, l.",
                      "Check: for example, a bucket of 10 l holds 10 × 1,000 = 10,000 ml, which is much more than 20 ml."],
                     "No, the statement is not correct. A bucket should be measured in litres.",
                     kind="prompt")],
          misconceptions=["M_UNIT_SIZE"])],
    key_terms=["capacity", "litre", "millilitre", "unit"]))

# ============================== T10 Litres and Millilitres ================================================
TOPICS.append(TOPIC(
    "T10", "M3", "Litres and Millilitres", ["Big to Small, Small to Big", "Different Units but Same Measure", "Let Us Think"],
    "Apply",
    "Students change between litres and millilitres, write mixed capacities such as 3 l 40 ml in millilitres, and read and add "
    "the capacities of containers.",
    "1 l = 1,000 ml. Litres to millilitres is × 1,000 and back is ÷ 1,000. The ml part of a mixed capacity takes three places. "
    "A container's capacity is the top mark of its scale.",
    [A("T10.C1", "Litres into Millilitres, and Back", "Apply",
       "Students change litres to millilitres by multiplying by 1,000 and millilitres to litres by dividing by 1,000, and "
       "find how many small containers fill a big one.",
       teach=["Predict first: a jug holds 4 l. How many ml is that? And how many 200 ml cups can you fill from it?",
              "1 l is 1,000 ml. Big to small: multiply by 1,000. 4 l is 4 × 1,000 = 4,000 ml.",
              "Small to big: divide by 1,000. A tank of 6,000 ml is 6,000 ÷ 1,000 = 6 l.",
              "A double number line works here too. The top line is in l and the bottom line is in ml, and each mark is × 1,000 "
              "from the top to the bottom.",
              "To find how many small containers fill a big one, change both to the same unit first, then divide. 4 l is "
              "4,000 ml, and 4,000 ÷ 200 = 20 cups.",
              "Rule: l to ml, × 1,000; ml to l, ÷ 1,000; to count small containers, use the same unit and divide."],
       examples=[WE("A jug holds 4 l. Change 4 l to ml. Change 6,000 ml to l. How many 200 ml cups can be filled from the jug? "
                    "These are practice values.",
                    ["1 l is 1,000 ml, so litres to millilitres is × 1,000 and ml to l is ÷ 1,000.",
                     "4 l: 4 × 1,000 = 4,000 ml.",
                     "6,000 ml: 6,000 ÷ 1,000 = 6 l.",
                     "To count cups, use the same unit. The jug holds 4,000 ml and a cup holds 200 ml.",
                     "4,000 ÷ 200 = 20 cups.",
                     "Check: 20 × 200 = 4,000 ml, which is 4 l."],
                    "4 l is 4,000 ml, 6,000 ml is 6 l, and the jug fills 20 cups")],
       key_terms=["litres", "millilitres", "double number line", "containers"], misconceptions=["M_KG_100G", "M_MIXED_UNITS"],
       minutes=6),
     A("T10.C2", "Mixed Capacities and Container Scales", "Apply",
       "Students write a capacity in l and ml in millilitres and back, read the top mark of a container's scale, and add the "
       "capacities of containers.",
       teach=["Predict first: a capacity is 3 l 40 ml. Is it 3,040 ml or 3,400 ml?",
              "It works like kg and g. Change the litres first: 3 l is 3 × 1,000 = 3,000 ml. Add the millilitre part in three places: "
              "3,000 + 40 = 3,040 ml.",
              "To go back, take out the whole thousands. 5,030 ml has 5 thousands, so it is 5 l 30 ml.",
              "A container with a scale shows its capacity at the top mark. A jug with 1 l at the top holds 1 l. A cup with "
              "250 ml at the top holds 250 ml.",
              "To find the capacity of several containers, add them: a 2 l jug and a 250 ml cup hold 2 l 250 ml together, "
              "which is 2,250 ml.",
              "Rule: l and ml to ml, multiply the l by 1,000 and add the ml in three places; add containers l with l and ml "
              "with ml."],
       examples=[WE("Change 3 l 40 ml to ml. Change 5,030 ml to l and ml. A jug has 2 l at its top mark and a cup has 250 ml "
                    "at its top mark. What is the capacity of both together? These are practice values.",
                    ["3 l 40 ml: change the 3 l first. 3 × 1,000 = 3,000 ml.",
                     "Add the millilitre part in three places, 040: 3,000 + 40 = 3,040 ml.",
                     "5,030 ml: take out the whole thousands. 5,030 − 5,000 = 30, so it is 5 l 30 ml.",
                     "The capacity of a container is its top mark. The jug holds 2 l and the cup holds 250 ml.",
                     "Add: 2 l + 250 ml = 2 l 250 ml. In ml, 2,000 + 250 = 2,250 ml.",
                     "Check: 2,250 − 2,000 = 250, so 2,250 ml is 2 l 250 ml."],
                    "3 l 40 ml is 3,040 ml, 5,030 ml is 5 l 30 ml, and the jug and cup hold 2 l 250 ml (2,250 ml)")],
       key_terms=["mixed capacities", "container", "scale", "millilitres"], misconceptions=["M_PART_PLACE"], minutes=6),
     DOER("T10.C3", "Practice: Measuring Jug", "measuring_jug", "Apply",
          "Students change between l and ml, read the capacity of containers by measuring with their scales, and solve "
          "problems on bottles, milk and water.",
          ["1 l is 1,000 ml: l to ml is × 1,000 and ml to l is ÷ 1,000.",
           "The ml part of a mixed capacity takes three places.",
           "A container's capacity is the top mark of its scale; add the containers litres with litres and millilitres with millilitres."],
          items=[FIO("bs.ramiz", "Big to Small, Small to Big: Ramiz's bottles",
                     "Ramiz brings a 500 ml water bottle to school. He drinks two bottles at school. How much water does he "
                     "drink at school? Ramiz drinks ___ ml + ___ ml = ___ ml. Ramiz drinks ___ l of water in a day.",
                     ["Ramiz drinks two bottles of 500 ml, so add 500 ml and 500 ml.",
                      "500 + 500 = 1,000 ml.",
                      "1 l is 1,000 ml, so 1,000 ml is 1 l.",
                      "The question counts only these two bottles, so Ramiz drinks 1 l of water in a day.",
                      "Check: 1 × 1,000 = 1,000 ml."],
                     "500 ml + 500 ml = 1,000 ml; 1 l",
                     kind="prompt"),
                 FIO("bs.muskaan", "Big to Small, Small to Big: Muskaan's bottle",
                     "Muskaan drinks 3 l of water in a day. How many times would she need to refill a 500 ml water bottle? "
                     "___. Muskaan drinks ___ ml of water in a day.",
                     ["Muskaan drinks 3 l a day. Change to millilitres: 3 × 1,000 = 3,000 ml.",
                      "A bottle holds 500 ml. To find how many bottles make 3,000 ml, divide: 3,000 ÷ 500 = 6.",
                      "She needs 6 bottles of 500 ml, so 6 times.",
                      "Muskaan drinks 3,000 ml of water in a day.",
                      "Check: 6 × 500 = 3,000 ml."],
                     "6 times; 3,000 ml",
                     kind="prompt"),
                 FIO("bs.containers", "Big to Small, Small to Big: capacity of containers",
                     "Write the total capacity of the following containers in each blank. Group 1: ___ l ___ ml. Group 2: "
                     "___ l ___ ml. Group 3: ___ l ___ ml. Group 4: ___ l ___ ml.",
                     ["A container's capacity is the top mark of its scale. Add the containers of each group: litres with "
                      "litres and millilitres with millilitres.",
                      "Group 1: 1 l, 500 ml and 100 ml. 500 + 100 = 600 ml, so 1 l 600 ml.",
                      "Group 2: 1 l and 500 ml, so 1 l 500 ml.",
                      "Group 3: 100 ml, 100 ml and 500 ml. 100 + 100 + 500 = 700 ml, which is 0 l 700 ml.",
                      "Group 4: 1 l, 1 l and 100 ml. 1 + 1 = 2 l, so 2 l 100 ml.",
                      "Check in millilitres: group 1 is 1,000 + 600 = 1,600 ml and group 4 is 2,000 + 100 = 2,100 ml."],
                     "Group 1: 1 l 600 ml; Group 2: 1 l 500 ml; Group 3: 0 l 700 ml; Group 4: 2 l 100 ml",
                     kind="prompt",
                     q_figure="Four groups of beakers, each beaker with a scale: group 1 has a beaker to 1 l with a 500 ml mark "
                              "in the middle, a beaker to 500 ml with marks every 100 ml and a beaker to 100 ml with a 50 ml "
                              "mark; group 2 has a beaker to 1 l and a beaker to 500 ml; group 3 has two beakers to 100 ml and "
                              "one beaker to 500 ml; group 4 has two beakers to 1 l and one beaker to 100 ml; under each group "
                              "is a blank line for l and ml."),
                 FIO("dm.milkman", "Different Units but Same Measure (capacity): the milkman's delivery",
                     "Khayal chacha delivers fresh cow milk to homes. Bhalerao's family orders 2 l of milk everyday. This "
                     "family has a vessel marked in millilitres only. What mark will you see in the vessel corresponding to 2 l? "
                     "Complete the double number line.",
                     ["1 l is 1,000 ml, so litres to millilitres is × 1,000.",
                      "2 l: 2 × 1,000 = 2,000 ml. The vessel marked in millilitres shows 2,000 ml for 2 l.",
                      "Complete the line. 6 l is 6 × 1,000 = 6,000 ml.",
                      "8 l is 8 × 1,000 = 8,000 ml.",
                      "12,000 ml is 12,000 ÷ 1,000 = 12 l.",
                      "14 l is 14 × 1,000 = 14,000 ml.",
                      "20,000 ml is 20,000 ÷ 1,000 = 20 l, and 25,000 ml is 25,000 ÷ 1,000 = 25 l.",
                      "Check: 2,000 ÷ 1,000 = 2 l."],
                     "2,000 ml. Line: 6,000 ml, 8,000 ml, 12 l, 14,000 ml, 20 l, 25 l",
                     kind="prompt",
                     q_figure="A double number line, l above and ml below, with the marks 1 l and 1000 ml, 2 l and 2000 ml, "
                              "6 l and a blank ml, 8 l and a blank ml, a blank l and 12,000 ml, 14 l and a blank ml, a blank l "
                              "and 20,000 ml, a blank l and 25,000 ml, not drawn to scale."),
                 FIO("dm.table", "Different Units but Same Measure (capacity): milk each week",
                     "Khayal chacha delivers the following amounts of milk each week to different families. Fill in the "
                     "table. Arora's family: 8 l, ___ ml. Nair's: 14 l, ___ ml. Shrivastava's: ___ l, 12,000 ml. Das's: ___ l, "
                     "20,000 ml. Rao's: ___ l, 25,000 ml.",
                     ["Use × 1,000 to change litres to millilitres and ÷ 1,000 to change millilitres to litres.",
                      "Arora's: 8 l is 8 × 1,000 = 8,000 ml.",
                      "Nair's: 14 l is 14 × 1,000 = 14,000 ml.",
                      "Shrivastava's: 12,000 ml is 12,000 ÷ 1,000 = 12 l.",
                      "Das's: 20,000 ml is 20,000 ÷ 1,000 = 20 l.",
                      "Rao's: 25,000 ml is 25,000 ÷ 1,000 = 25 l.",
                      "Check: each millilitre number is 1,000 times the litre number next to it."],
                     "Arora's: 8,000 ml; Nair's: 14,000 ml; Shrivastava's: 12 l; Das's: 20 l; Rao's: 25 l",
                     kind="prompt",
                     q_figure="A table with the columns Family, Milk Delivered in a Week in l and Quantity in ml, and five rows: "
                              "Arora's with 8 l, Nair's with 14 l, Shrivastava's with 12,000 ml, Das's with 20,000 ml and Rao's "
                              "with 25,000 ml, the other cell of each row empty."),
                 FIO("ex.dev", "Example 8: Dev's family",
                     "Dev's family needs 1 l milk every day. On Sunday, they need 500 ml more. How much milk do they need on "
                     "Sunday?",
                     ["Dev's family needs 1 l every day and 500 ml more on Sunday, so add 1 l + 500 ml.",
                      "Change the litres to millilitres: 1 l is 1,000 ml.",
                      "1,000 + 500 = 1,500 ml.",
                      "Check: 1,500 − 1,000 = 500 ml more than 1 l."],
                     "They need 1,500 ml (1 l 500 ml) of milk on Sunday",
                     kind="example"),
                 FIO("lt.mary", "Let Us Think: Mary and Daisy",
                     "Mary and Daisy filled their bottle with 1 l 400 ml of water. They wondered about the capacity of the "
                     "bottle in millilitres. How much is it? One child says 1,400 ml. The other says: No, it is 1,040 ml. Who do you "
                     "think is correct and why?",
                     ["1 l 400 ml: change the 1 l first. 1 × 1,000 = 1,000 ml.",
                      "Add the millilitre part: 1,000 + 400 = 1,400 ml.",
                      "So the child who says 1,400 ml is correct.",
                      "The other child says 1,040 ml. But 1,040 ml is 1,000 ml + 40 ml, which is 1 l 40 ml, a different "
                      "capacity.",
                      "Check: 1,400 − 1,000 = 400, so 1 l 400 ml is 1,400 ml."],
                     "1,400 ml is correct: 1 l 400 ml is 1,000 ml + 400 ml. 1,040 ml would be 1 l 40 ml.",
                     kind="exercise"),
                 FIO("lt.convert", "Let Us Think: conversions",
                     "Convert and fill in the blanks appropriately. You can use the double number line given earlier. "
                     "(a) 3 l 8 ml = ___ ml (b) 9 l 90 ml = ___ ml (c) 14,075 ml = ___ l ___ ml (d) 8 l 86 ml = ___ ml "
                     "(e) 12,200 ml = ___ l ___ ml (f) 18,350 ml = ___ l ___ ml",
                     ["(a): 3 l 8 ml: 3 × 1,000 = 3,000 ml, and 3,000 + 8 = 3,008 ml.",
                      "(b): 9 l 90 ml: 9 × 1,000 = 9,000 ml, and 9,000 + 90 = 9,090 ml.",
                      "(c): 14,075 ml: 14,075 − 14,000 = 75, so it is 14 l 75 ml.",
                      "(d): 8 l 86 ml: 8 × 1,000 = 8,000 ml, and 8,000 + 86 = 8,086 ml.",
                      "(e): 12,200 ml: 12,200 − 12,000 = 200, so it is 12 l 200 ml.",
                      "(f): 18,350 ml: 18,350 − 18,000 = 350, so it is 18 l 350 ml.",
                      "Check: the millilitre part of a mixed capacity takes three places: 8 ml is 008 and 90 ml is 090."],
                     "(a): 3,008 ml; (b): 9,090 ml; (c): 14 l 75 ml; (d): 8,086 ml; (e): 12 l 200 ml; (f): 18 l 350 ml",
                     kind="exercise")],
          misconceptions=["M_KG_100G", "M_PART_PLACE"])],
    key_terms=["litres", "millilitres", "capacities", "containers"]))

# ============================== T11 Comparing and Combining Capacities ====================================
TOPICS.append(TOPIC(
    "T11", "M3", "Comparing and Combining Capacities", ["Let Us Compare"], "Apply",
    "Students compare capacities by changing to millilitres, and add and subtract capacities by exchanging 1,000 ml for 1 l.",
    "To compare capacities, change both to ml and compare the numbers. To add and subtract capacities, do what you did for "
    "weights: exchange 1,000 ml for 1 l, break 1 l into 1,000 ml, or work in ml.",
    [A("T11.C1", "Comparing Capacities", "Apply",
       "Students compare capacities given in l and ml by changing both to ml, use the signs <, = and >, and work out a sum "
       "before comparing.",
       teach=["Predict first: which holds more, 2 l 50 ml or 2,500 ml?",
              "Change both to ml. 2 l 50 ml is 2 × 1,000 + 50 = 2,050 ml. The other is already 2,500 ml.",
              "Compare the numbers: 2,050 is less than 2,500, so 2 l 50 ml < 2,500 ml.",
              "If a capacity is a sum, work the sum out first: 600 ml + 700 ml = 1,300 ml, which is 1 l 300 ml.",
              "Rule: change to ml first, then compare."],
       examples=[WE("Compare 2 l 50 ml and 2,500 ml. Then compare 600 ml + 700 ml with 1 l 300 ml. Use <, = or >. These are "
                    "practice values.",
                    ["Change both capacities to ml. 2 l 50 ml is 2 × 1,000 + 50 = 2,050 ml.",
                     "The other capacity is 2,500 ml. 2,050 is less than 2,500.",
                     "So 2 l 50 ml < 2,500 ml.",
                     "Work out the sum first: 600 + 700 = 1,300 ml.",
                     "1 l 300 ml is 1 × 1,000 + 300 = 1,300 ml.",
                     "1,300 ml and 1,300 ml are the same, so 600 ml + 700 ml = 1 l 300 ml.",
                     "Check: 2,500 − 2,050 = 450, so the second capacity is 450 ml more."],
                    "2 l 50 ml < 2,500 ml, and 600 ml + 700 ml = 1 l 300 ml")],
       key_terms=["comparing capacities", "millilitres", "signs"], misconceptions=["M_BIG_NUMBER", "M_MIXED_UNITS"],
       minutes=5),
     A("T11.C2", "Adding and Subtracting Capacities", "Apply",
       "Students add and subtract capacities in l and ml in the same ways as weights, exchanging 1,000 ml for 1 l and breaking "
       "1 l into 1,000 ml.",
       textbook=["Sam found the quantity of petrol by adding like quantities."],
       teach=["Predict first: 4 l 600 ml + 3 l 700 ml. Do you add like quantities, litres with litres and millilitres with millilitres?",
              "Yes. It is the same as for weights. 1 l = 1,000 ml, just as 1 kg = 1,000 g.",
              "Add: 4 + 3 = 7 l and 600 + 700 = 1,300 ml. 1,300 ml is 1 l 300 ml, so the total is 7 l + 1 l 300 ml = 8 l 300 ml.",
              "Or change both to ml: 4,600 + 3,700 = 8,300 ml, which is 8 l 300 ml.",
              "To subtract, when the ml on top are fewer, break 1 l into 1,000 ml, or change both to ml. For 6 l 200 ml − "
              "2 l 900 ml: 6,200 − 2,900 = 3,300 ml, which is 3 l 300 ml.",
              "Rule: add and subtract capacities like weights: exchange 1,000 ml for 1 l, break 1 l into 1,000 ml, or work in ml."],
       examples=[WE("Add 4 l 600 ml and 3 l 700 ml. Then subtract 2 l 900 ml from 6 l 200 ml. These are practice values.",
                    ["Add like quantities. The l: 4 + 3 = 7 l.",
                     "The ml: 600 + 700 = 1,300 ml. 1,000 ml is 1 l, so 1,300 ml is 1 l 300 ml.",
                     "7 l + 1 l 300 ml = 8 l 300 ml. In ml: 4,600 + 3,700 = 8,300 ml, which is 8 l 300 ml.",
                     "To subtract, change both to ml. 6 l 200 ml is 6,200 ml and 2 l 900 ml is 2,900 ml.",
                     "6,200 − 2,900 = 3,300 ml, which is 3 l 300 ml.",
                     "Check by adding: 2,900 + 3,300 = 6,200 ml."],
                    "4 l 600 ml + 3 l 700 ml = 8 l 300 ml, and 6 l 200 ml − 2 l 900 ml = 3 l 300 ml")],
       ncert=["cap.note", "cap.add"], key_terms=["adding capacities", "subtracting", "exchange", "millilitres"],
       misconceptions=["M_NO_EXCHANGE", "M_SMALL_FROM_BIG"], minutes=6),
     DOER("T11.C3", "Practice: Petrol Pump", None, "Apply",
          "Students compare, add and subtract capacities in l and ml, and find the totals of petrol in a table by multiplying "
          "and adding.",
          ["Change both quantities to ml before comparing.",
           "Add and subtract capacities like weights, in l and ml or in ml.",
           "Find each total in a table first, then add the totals."],
          items=[FIO("lc.fuel", "Let Us Compare: fuel at the petrol pump",
                     "Kiran owns a petrol pump. She records the details of the sales of petrol in a day. Truck: 3 vehicles, "
                     "500 litres in each vehicle. Bus: 6 vehicles, 300 litres. Car: 10 vehicles, 50 litres. Auto Rickshaw: 12 "
                     "vehicles, 8 litres. Two-wheeler: 25 vehicles, 5 litres. The last column, total quantity of fuel in "
                     "litres, is empty. (a) How much more fuel is bought for buses than for trucks? (b) What is the total "
                     "quantity of fuel filled from the petrol pump on that day?",
                     ["Fill the last column first. Total fuel = number of vehicles × fuel in each vehicle.",
                      "Truck: 3 × 500 = 1,500 l.",
                      "Bus: 6 × 300 = 1,800 l.",
                      "Car: 10 × 50 = 500 l.",
                      "Auto Rickshaw: 12 × 8 = 96 l.",
                      "Two-wheeler: 25 × 5 = 125 l.",
                      "(a): buses minus trucks: 1,800 − 1,500 = 300 l more.",
                      "(b): the total: 1,500 + 1,800 + 500 + 96 + 125 = 4,021 l.",
                      "Check the total in two parts: 1,500 + 1,800 = 3,300 and 500 + 96 + 125 = 721, and 3,300 + 721 = 4,021."],
                     "(a): 300 l; (b): 4,021 l",
                     kind="exercise",
                     q_figure="A table with the columns Vehicle, No. of Vehicles, Quantity of Fuel in Each Vehicle (in litres) "
                              "and Total Quantity of Fuel (in litres), the last column empty, and five rows: Truck 3 and 500, "
                              "Bus 6 and 300, Car 10 and 50, Auto Rickshaw 12 and 8, Two-wheeler 25 and 5."),
                 FIO("lc.compare", "Let Us Compare: compare the quantities",
                     "Compare the following quantities using the signs <, =, >. (a) 5 l 600 ml ___ 5,400 ml "
                     "(b) 10 l 100 ml ___ 1 l 600 ml (c) 190 ml + 800 ml ___ 800 ml + 109 ml (d) 3 l 600 ml ___ 3,600 ml "
                     "(e) 4 l 50 ml ___ 4 l 500 ml",
                     ["Change both quantities to millilitres and compare.",
                      "(a): 5 l 600 ml is 5,600 ml. 5,600 is more than 5,400, so 5 l 600 ml > 5,400 ml.",
                      "(b): 10 l 100 ml is 10,100 ml and 1 l 600 ml is 1,600 ml. 10,100 is more than 1,600, so 10 l 100 ml > "
                      "1 l 600 ml.",
                      "(c): 190 ml + 800 ml is 990 ml. 800 ml + 109 ml is 909 ml. 990 is more than 909, so 190 ml + 800 ml > "
                      "800 ml + 109 ml.",
                      "(d): 3 l 600 ml is 3,600 ml, the same as 3,600 ml, so 3 l 600 ml = 3,600 ml.",
                      "(e): 4 l 50 ml is 4,050 ml and 4 l 500 ml is 4,500 ml. 4,050 is less than 4,500, so 4 l 50 ml < 4 l 500 ml.",
                      "Check: in every part both quantities were in millilitres before they were compared."],
                     "(a): >; (b): >; (c): >; (d): =; (e): <",
                     kind="exercise"),
                 FIO("ex.sam", "Example 9: Sam and Tina",
                     "Sam and Tina fill petrol in their bikes. Tina bought 2 l 500 ml of petrol. Sam bought 2 l 800 ml more "
                     "petrol than Tina. How much petrol did Sam buy?",
                     ["Sam bought 2 l 800 ml more than Tina, so add Tina's 2 l 500 ml and 2 l 800 ml.",
                      "Add like quantities. The litres: 2 + 2 = 4 l.",
                      "The millilitres: 500 + 800 = 1,300 ml. 1,300 ml is 1 l 300 ml.",
                      "4 l + 1 l 300 ml = 5 l 300 ml.",
                      "Check in millilitres: 2,500 + 2,800 = 5,300 ml, which is 5 l 300 ml."],
                     "Sam bought 5 l 300 ml of petrol",
                     kind="example"),
                 FIO("ex.bike", "Example 10: Sam's bike",
                     "After refueling, Sam found his fuel gauge reading 9 l. How much fuel did his bike have before "
                     "refueling?",
                     ["After refuelling the gauge shows 9 l, and Sam put in 5 l 300 ml. So the fuel before was 9 l − 5 l 300 ml.",
                      "Change both to millilitres: 9 l is 9,000 ml and 5 l 300 ml is 5,300 ml.",
                      "9,000 − 5,300 = 3,700 ml.",
                      "3,700 ml is 3 l 700 ml.",
                      "Check by adding: 3,700 + 5,300 = 9,000 ml, which is 9 l."],
                     "The bike had 3 l 700 ml of fuel before refuelling",
                     kind="example")],
          misconceptions=["M_BIG_NUMBER", "M_NO_EXCHANGE", "M_SMALL_FROM_BIG"])],
    key_terms=["capacities", "millilitres", "petrol", "exchange"]))

# ============================== T12 Multiplying and Dividing Capacities ===================================
TOPICS.append(TOPIC(
    "T12", "M3", "Multiplying and Dividing Capacities", ["Let Us Solve"], "Apply",
    "Students multiply and divide capacities in l and ml, and solve multi-step problems on bottles, glasses and containers.",
    "To multiply or share a capacity, change to ml, or multiply and divide the l and the ml and exchange 1,000 ml for 1 l. To "
    "find how many small containers fill a big one, change both to ml and divide.",
    [A("T12.C1", "Multiplying and Dividing Capacities", "Apply",
       "Students multiply and divide capacities in l and ml, and find how many small containers fill a big one by changing "
       "both to ml.",
       textbook=["Use the double number line whenever needed to solve such problems."],
       teach=["Predict first: 6 jugs hold 1 l 250 ml each. Do you multiply both the l and the ml?",
              "Yes. Multiply the l and the ml parts, then exchange 1,000 ml for 1 l: 6 × 1 = 6 l and 6 × 250 = 1,500 ml, which "
              "is 1 l 500 ml. The total is 7 l 500 ml.",
              "To share equally, change to ml and divide. 9 l 600 ml is 9,600 ml, and 9,600 ÷ 8 = 1,200 ml, which is 1 l 200 ml.",
              "To find how many small containers fill a big one, change both to ml and divide. 3 l is 3,000 ml, and "
              "3,000 ÷ 300 = 10 glasses of 300 ml.",
              "Use a double number line whenever it helps: litres on one line and ml on the other, or a number of glasses on "
              "one line and ml on the other.",
              "Rule: change to one unit, multiply or divide, then change back."],
       examples=[WE("6 jugs hold 1 l 250 ml each. What is the total capacity? Then 9 l 600 ml of oil is shared equally into 8 "
                    "cans. How much is in each can? These are practice values.",
                    ["6 jugs make 6 times the capacity of one jug: 6 × 1 l 250 ml.",
                     "Multiply the l: 6 × 1 = 6 l.",
                     "Multiply the ml: 6 × 250 = 1,500 ml, which is 1 l 500 ml.",
                     "Add: 6 l + 1 l 500 ml = 7 l 500 ml.",
                     "To share 9 l 600 ml into 8 cans, change to ml: 9 l 600 ml is 9,600 ml.",
                     "9,600 ÷ 8 = 1,200 ml, which is 1 l 200 ml.",
                     "Check: 8 × 1,200 = 9,600 ml."],
                    "6 jugs hold 7 l 500 ml, and each can has 1 l 200 ml")],
       ncert=["ls.dnl"], key_terms=["multiplying", "dividing", "capacities", "containers"], misconceptions=["M_MIXED_UNITS"],
       minutes=6),
     DOER("T12.C2", "Pull it together and do it: Let Us Solve", None, "Apply",
          "Students solve multi-step problems on capacity and cost by changing to ml, multiplying, dividing, adding and "
          "subtracting, and use a double number line when it helps.",
          ["Change the capacities to one unit, usually ml.",
           "Multiply, divide, add or subtract, then change back to l and ml if it helps.",
           "Use a double number line whenever it helps."],
          items=[FIO("ls.Q1", "Let Us Solve: Riya and Aarav's bottles",
                     "Riya is filling water bottles for a picnic. She fills one 2 l bottle and four 500 ml bottles. Her "
                     "friend, Aarav fills three 750 ml bottles. Who filled more water, Riya or Aarav? How much more?",
                     ["Riya: one 2 l bottle and four 500 ml bottles. Change to millilitres: 2 l is 2,000 ml.",
                      "Four 500 ml bottles: 4 × 500 = 2,000 ml.",
                      "Riya's total: 2,000 + 2,000 = 4,000 ml, which is 4 l.",
                      "Aarav: three 750 ml bottles: 3 × 750 = 2,250 ml, which is 2 l 250 ml.",
                      "4,000 is more than 2,250, so Riya filled more water.",
                      "How much more: 4,000 − 2,250 = 1,750 ml, which is 1 l 750 ml.",
                      "Check: 2,250 + 1,750 = 4,000 ml."],
                     "Riya filled more, by 1 l 750 ml",
                     kind="exercise"),
                 FIO("ls.Q2", "Let Us Solve: milk in 8 glasses",
                     "A bottle of milk is poured equally into 8 glasses, leaving 120 ml of milk in the bottle. (a) If each "
                     "glass has a capacity of 360 ml, what is the total capacity of 8 glasses? (b) How much milk was there in "
                     "the bottle initially? (c) If 1 l of milk costs ₹40, how much will 3 l milk cost?",
                     ["(a): 8 glasses of 360 ml hold 8 × 360 = 2,880 ml, which is 2 l 880 ml.",
                      "(b): each glass is filled to its capacity, so 2,880 ml was poured and 120 ml was left in the bottle.",
                      "The bottle held 2,880 + 120 = 3,000 ml at first, which is 3 l.",
                      "(c): 1 l of milk costs ₹40, so 3 l cost 3 × 40 = ₹120.",
                      "Check: 3,000 − 120 = 2,880 ml."],
                     "(a): 2 l 880 ml; (b): 3 l; (c): ₹120",
                     kind="exercise"),
                 FIO("ls.Q3", "Let Us Solve: the juice vendor",
                     "A juice vendor has a 5 l container of orange juice. Each glass has a capacity 250 ml. (a) How many "
                     "full glasses can he serve before the container becomes empty? (b) If he has already served 10 glasses, "
                     "how much juice is left? (c) If 250 ml of juice is sold at ₹25, how much will he earn by selling 5 l "
                     "juice?",
                     ["(a): 5 l is 5,000 ml. Each glass holds 250 ml. 5,000 ÷ 250 = 20 glasses.",
                      "(b): 10 glasses of 250 ml are 10 × 250 = 2,500 ml. The juice left is 5,000 − 2,500 = 2,500 ml, which "
                      "is 2 l 500 ml.",
                      "(c): 20 glasses are sold at ₹25 each: 20 × 25 = ₹500.",
                      "Check (a): 20 × 250 = 5,000 ml."],
                     "(a): 20 glasses; (b): 2 l 500 ml; (c): ₹500",
                     kind="exercise"),
                 FIO("ls.Q4", "Let Us Solve: oil in 7 containers",
                     "In a factory, 8 l 400 ml of oil needs to be equally poured into 7 containers for storage. How much oil "
                     "will each container hold?",
                     ["8 l 400 ml is 8 × 1,000 + 400 = 8,400 ml.",
                      "Share equally into 7 containers: 8,400 ÷ 7 = 1,200 ml.",
                      "1,200 ml is 1 l 200 ml.",
                      "Check: 7 × 1,200 = 8,400 ml."],
                     "Each container holds 1 l 200 ml",
                     kind="exercise"),
                 FIO("ls.Q5", "Let Us Solve: buttermilk in 8 containers",
                     "If one container can hold 1 l 75 ml of buttermilk, how much buttermilk will be there in 8 such "
                     "containers?",
                     ["1 l 75 ml is 1 × 1,000 + 75 = 1,075 ml.",
                      "8 containers: 8 × 1,075 = 8,600 ml.",
                      "8,600 ml is 8 l 600 ml.",
                      "Check in parts: 8 × 1 = 8 l and 8 × 75 = 600 ml, so 8 l 600 ml."],
                     "8 containers hold 8 l 600 ml of buttermilk",
                     kind="exercise")],
          misconceptions=["M_MIXED_UNITS", "M_NO_EXCHANGE"])],
    key_terms=["capacities", "containers", "multi-step", "problems"]))
