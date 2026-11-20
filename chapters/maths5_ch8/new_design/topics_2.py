# -*- coding: utf-8 -*-
"""Topics T6, T7 and T8 (module M2: Weight, Units and Calculations): Adding and Subtracting Weights, Multiplying and Sharing
Weights, and Cost and Scaling (the cost of a weight and the double number line). Every teaching concept has one worked
example with the plan's own numbers (practice values); every book question is an FIO item of its topic's DOER, in the
book's order. The rupee sign is written before the number; no decimals are used anywhere."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T6 Adding and Subtracting Weights =========================================
TOPICS.append(TOPIC(
    "T6", "M2", "Adding and Subtracting Weights", ["From Tiny to Big", "The Grocery Store", "Let Us Do"], "Apply",
    "Students add and subtract weights in kg and g by exchanging 1,000 g for 1 kg, and solve word problems on the weights "
    "of everyday things.",
    "Add like quantities, kilograms with kilograms and grams with grams, and exchange 1,000 g for 1 kg when the g reach 1,000. To subtract, break "
    "1 kg into 1,000 g when the g on top are fewer.",
    [A("T6.C1", "Adding Weights", "Apply",
       "Students add weights in kg and g in three ways: kg and g separately, a column with a carry, and in grams, "
       "exchanging 1,000 g for 1 kg.",
       textbook=["We can add and subtract like quantities.", "1,000 g = 1 kg",
                 "We can also convert the quantities into grams."],
       teach=["Predict first: 3 kg 600 g + 2 kg 700 g. The g parts are 600 g and 700 g. Can the g part of the answer stay "
              "1,300 g?",
              "Add like quantities: kg with kg, and g with g.",
              "Way 1, in parts: add the kg, 3 + 2 = 5 kg. Add the g, 600 + 700 = 1,300 g. Since 1,000 g = 1 kg, 1,300 g is "
              "1 kg 300 g. So the weight is 5 kg + 1 kg 300 g = 6 kg 300 g.",
              "Way 2, in a column: write kg and g in two columns. Add the g column first: 600 + 700 = 1,300. Write 300 and "
              "carry 1 kg to the kg column. Then add the kg column: 3 + 2 + 1 = 6.",
              "Way 3, in grams: change both to grams and add. 3,600 + 2,700 = 6,300 g, which is 6 kg 300 g.",
              "Choose the way that suits the numbers. When the numbers are like 250, 500 or 750, you can add in your head.",
              "Rule: add like quantities, and when the g column reaches 1,000 g or more, exchange 1,000 g for 1 kg."],
       examples=[WE("Add 3 kg 600 g and 2 kg 700 g in three ways. These are practice values.",
                    ["Way 1, in parts. Add the kilograms: 3 + 2 = 5 kg.",
                     "Add the grams: 600 + 700 = 1,300 g. 1,000 g is 1 kg, so 1,300 g is 1 kg 300 g.",
                     "Put the parts together: 5 kg + 1 kg 300 g = 6 kg 300 g.",
                     "Way 2, in a column. Add the g column: 600 + 700 = 1,300. Write 300 g and carry 1 kg.",
                     "Add the kg column: 3 + 2 + 1 = 6 kg. The answer is 6 kg 300 g.",
                     "Way 3, in grams. 3 kg 600 g is 3,600 g and 2 kg 700 g is 2,700 g. 3,600 + 2,700 = 6,300 g.",
                     "6,300 g is 6 kg 300 g. All three ways give the same weight."],
                    "3 kg 600 g + 2 kg 700 g = 6 kg 300 g")],
       ncert=["add.ways", "addsub.note"], key_terms=["adding weights", "carry", "exchange", "grams"],
       misconceptions=["M_NO_EXCHANGE"], minutes=7),
     A("T6.C2", "Subtracting Weights", "Apply",
       "Students subtract weights in kg and g in three ways: taking away in parts, a column with 1 kg broken into 1,000 g, "
       "and in grams.",
       teach=["Predict first: 5 kg 200 g − 2 kg 800 g. The g on top, 200 g, are fewer than 800 g. Can you take 800 g away "
              "from 200 g?",
              "Not yet. But the top weight has whole kilograms that you can break up.",
              "Way 1, take away in parts: from 5 kg 200 g take away 200 g and 5 kg is left. Take away 2 kg and 3 kg is left. "
              "Take away the other 600 g: 3 kg − 600 g = 2 kg 400 g.",
              "Way 2, in a column: break 1 kg into 1,000 g. Then 5 kg 200 g becomes 4 kg 1,200 g. Now 1,200 − 800 = 400 g "
              "and 4 − 2 = 2 kg.",
              "Way 3, in grams: 5,200 − 2,800 = 2,400 g, which is 2 kg 400 g.",
              "A slip to avoid: do not take the smaller number from the bigger one in each column. 800 − 200 = 600 g would "
              "give 3 kg 600 g, which is wrong.",
              "Rule: when the g on top are fewer, break 1 kg into 1,000 g first, or change both weights to grams."],
       examples=[WE("Subtract 2 kg 800 g from 5 kg 200 g in three ways. These are practice values.",
                    ["Way 1, take away in parts. 5 kg 200 g − 200 g leaves 5 kg.",
                     "5 kg − 2 kg leaves 3 kg.",
                     "Still to take away: 800 − 200 = 600 g. 3 kg is 3,000 g and 3,000 − 600 = 2,400 g, which is 2 kg 400 g.",
                     "Way 2, in a column. 200 g is fewer than 800 g, so break 1 kg into 1,000 g. 5 kg 200 g becomes "
                     "4 kg 1,200 g.",
                     "1,200 − 800 = 400 g and 4 − 2 = 2 kg. The answer is 2 kg 400 g.",
                     "Way 3, in grams. 5 kg 200 g is 5,200 g and 2 kg 800 g is 2,800 g. 5,200 − 2,800 = 2,400 g.",
                     "2,400 g is 2 kg 400 g. All three ways give the same weight."],
                    "5 kg 200 g − 2 kg 800 g = 2 kg 400 g")],
       ncert=["sub.ways"], key_terms=["subtracting weights", "break", "column", "grams"],
       misconceptions=["M_SMALL_FROM_BIG", "M_NO_EXCHANGE"], minutes=7),
     DOER("T6.C3", "Practice: Weight Regrouper", "weight_regrouper", "Apply",
          "Students add and subtract weights in kg and g by exchanging 1,000 g for 1 kg and 1 kg for 1,000 g, and solve word "
          "problems on weights.",
          ["Add like quantities: kilograms with kilograms and grams with grams.",
           "Exchange 1,000 g for 1 kg when the g column reaches 1,000 g or more.",
           "To subtract, break 1 kg into 1,000 g when the g on top are fewer."],
          items=[FIO("ex.rice_total", "Example 4: Rathna's rice",
                     "Rathna went to the local grocery store and bought several items. She bought 2 kg 500 g rice for daily "
                     "use and 1 kg 750 g additional rice for the upcoming Pongal festival. How much total rice did she buy?",
                     ["Add like quantities: kilograms with kilograms and grams with grams.",
                      "Add the kilograms: 2 + 1 = 3 kg.",
                      "Add the grams: 500 + 750 = 1,250 g. 1,000 g is 1 kg, so 1,250 g is 1 kg 250 g.",
                      "3 kg + 1 kg 250 g = 4 kg 250 g.",
                      "Check in grams: 2,500 + 1,750 = 4,250 g, which is 4 kg 250 g."],
                     "Rathna bought 4 kg 250 g of rice",
                     kind="example",
                     s_figure="A kg and g column sum, 2 kg 500 g plus 1 kg 750 g, with the carry of 1 kg written above the kg "
                              "column and the result 4 kg 250 g."),
                 FIO("ex.rice_extra", "Example 5: extra rice",
                     "How much extra rice did she buy for household use than for the Pongal festival?",
                     ["The extra rice is the difference: 2 kg 500 g − 1 kg 750 g.",
                      "Change both to grams: 2 kg 500 g is 2,500 g and 1 kg 750 g is 1,750 g.",
                      "2,500 − 1,750 = 750 g.",
                      "Check in parts: take 500 g from 2 kg 500 g to leave 2 kg, take 1 kg to leave 1 kg, then take 250 g "
                      "more to leave 750 g.",
                      "Check by adding: 1,750 + 750 = 2,500 g."],
                     "She bought 750 g more rice for daily use",
                     kind="example"),
                 FIO("lud2.Q1", "Let Us Do: onions",
                     "A restaurant owner uses 5 kg 200 g, 8 kg 900 g, and 12 kg 600 g of onions over 3 days. What is the "
                     "total weight of onions used by the restaurant owner in 3 days?",
                     ["Add the three weights: 5 kg 200 g + 8 kg 900 g + 12 kg 600 g.",
                      "Add the kilograms: 5 + 8 + 12 = 25 kg.",
                      "Add the grams: 200 + 900 + 600 = 1,700 g. 1,700 g is 1 kg 700 g.",
                      "25 kg + 1 kg 700 g = 26 kg 700 g.",
                      "Check in grams: 5,200 + 8,900 + 12,600 = 26,700 g, which is 26 kg 700 g."],
                     "26 kg 700 g",
                     kind="exercise"),
                 FIO("lud2.Q2", "Let Us Do: apples",
                     "Aarav is helping his grandfather at the fruit stall. He lifts two baskets of apples weighing 2 kg 100 g "
                     "and 3 kg 950 g. What is the total weight of apples he lifted?",
                     ["Add the two weights: 2 kg 100 g + 3 kg 950 g.",
                      "Add the kilograms: 2 + 3 = 5 kg.",
                      "Add the grams: 100 + 950 = 1,050 g. 1,000 g is 1 kg, so 1,050 g is 1 kg 50 g.",
                      "5 kg + 1 kg 50 g = 6 kg 50 g.",
                      "Check in grams: 2,100 + 3,950 = 6,050 g, which is 6 kg 50 g."],
                     "6 kg 50 g",
                     kind="exercise"),
                 FIO("lud2.Q3", "Let Us Do: sand",
                     "4 kg 500 g of sand is used from a sack weighing 10 kg. How much sand is left in the sack?",
                     ["The sand left is 10 kg − 4 kg 500 g.",
                      "Change both to grams: 10 kg is 10,000 g and 4 kg 500 g is 4,500 g.",
                      "10,000 − 4,500 = 5,500 g.",
                      "5,500 g is 5 kg 500 g.",
                      "Check by adding: 4,500 + 5,500 = 10,000 g, which is 10 kg."],
                     "5 kg 500 g of sand are left",
                     kind="exercise"),
                 FIO("lud2.Q4", "Let Us Do: rice sack",
                     "A rice sack weighs 9 kg 750 g. After some rice is used, it weighs 3 kg 700 g. How much rice was used?",
                     ["The rice used is 9 kg 750 g − 3 kg 700 g.",
                      "Subtract the grams: 750 − 700 = 50 g. No break is needed, because 750 is more than 700.",
                      "Subtract the kilograms: 9 − 3 = 6 kg.",
                      "The rice used is 6 kg 50 g.",
                      "Check in grams: 9,750 − 3,700 = 6,050 g, which is 6 kg 50 g."],
                     "6 kg 50 g of rice was used",
                     kind="exercise"),
                 FIO("lud2.Q5", "Let Us Do: delivery truck",
                     "A delivery truck delivered 17 kg 900 g of supplies in the morning and 12 kg 700 g in the afternoon. "
                     "How much total supplies did it deliver?",
                     ["Add the two weights: 17 kg 900 g + 12 kg 700 g.",
                      "Add the kilograms: 17 + 12 = 29 kg.",
                      "Add the grams: 900 + 700 = 1,600 g. 1,600 g is 1 kg 600 g.",
                      "29 kg + 1 kg 600 g = 30 kg 600 g.",
                      "Check in grams: 17,900 + 12,700 = 30,600 g, which is 30 kg 600 g."],
                     "30 kg 600 g",
                     kind="exercise"),
                 FIO("lud2.Q6", "Let Us Do: box of books",
                     "A box of books weighs 14 kg 750 g. After removing some books, the weight of the box is 10 kg 500 g. "
                     "What is the weight of the books removed?",
                     ["The books removed weigh 14 kg 750 g − 10 kg 500 g.",
                      "Subtract the grams: 750 − 500 = 250 g.",
                      "Subtract the kilograms: 14 − 10 = 4 kg.",
                      "The weight of the books removed is 4 kg 250 g.",
                      "Check in grams: 14,750 − 10,500 = 4,250 g, which is 4 kg 250 g."],
                     "4 kg 250 g",
                     kind="exercise"),
                 FIO("lud2.Q7", "Let Us Do: flour for the langar",
                     "In a community kitchen of a Gurdwara, 65 kg of flour was purchased on one day. Out of this, 42 kg 275 g "
                     "flour was used for preparing langar. The next day, an additional 52 kg 500 g of flour was bought. What "
                     "is the total quantity of flour now available in the kitchen store?",
                     ["The flour left after the langar is 65 kg − 42 kg 275 g. Then add the flour bought the next day, "
                      "52 kg 500 g.",
                      "Change to grams: 65 kg is 65,000 g, 42 kg 275 g is 42,275 g and 52 kg 500 g is 52,500 g.",
                      "65,000 − 42,275 = 22,725 g.",
                      "22,725 + 52,500 = 75,225 g.",
                      "75,225 g is 75 kg 225 g.",
                      "Check: 75,225 − 52,500 = 22,725 and 22,725 + 42,275 = 65,000."],
                     "75 kg 225 g of flour",
                     kind="exercise")],
          misconceptions=["M_NO_EXCHANGE", "M_SMALL_FROM_BIG"])],
    key_terms=["weights", "exchange", "grams", "column"]))

# ============================== T7 Multiplying and Sharing Weights ========================================
TOPICS.append(TOPIC(
    "T7", "M2", "Multiplying and Sharing Weights", ["More Operations on Weight"], "Apply",
    "Students multiply a weight in kg and g by a whole number and share a weight equally, working in kg and g or in grams.",
    "To multiply a weight, multiply the kg and the g and exchange 1,000 g for 1 kg, or change to grams. To share a weight "
    "equally, divide the kg and the g, or change to grams and divide.",
    [A("T7.C1", "Multiplying a Weight", "Apply",
       "Students multiply a weight in kg and g by a whole number, by multiplying the kg and the g separately or by changing "
       "to grams, and exchange 1,000 g for 1 kg.",
       textbook=["You can find the product by multiplying the kg and g separately and adding the two. You can also convert "
                 "the quantity into grams and then multiply."],
       teach=["Predict first: 6 sacks each weigh 2 kg 500 g. Do you multiply only the 2 kg, or the 500 g as well?",
              "Multiply both parts. 6 sacks of the same weight make 6 times that weight.",
              "Way 1, kg and g separately: 6 × 2 = 12 kg and 6 × 500 = 3,000 g. 3,000 g is 3 kg, so the total is 12 kg + 3 kg "
              "= 15 kg.",
              "Way 2, in grams: 2 kg 500 g is 2,500 g and 2,500 × 6 = 15,000 g, which is 15 kg.",
              "A slip to avoid: do not leave the g part out. 6 × 2 kg = 12 kg is only part of the weight.",
              "Rule: multiply the kg part and the g part, then exchange 1,000 g for 1 kg; or change to grams, multiply and "
              "change back."],
       examples=[WE("6 sacks each weigh 2 kg 500 g. How much do they weigh in all? These are practice values.",
                    ["6 sacks of the same weight make 6 times that weight: 6 × 2 kg 500 g.",
                     "Way 1, kg and g separately. Multiply the kilograms: 6 × 2 = 12 kg.",
                     "Multiply the grams: 6 × 500 = 3,000 g. 1,000 g is 1 kg, so 3,000 g is 3 kg.",
                     "Add the parts: 12 kg + 3 kg = 15 kg.",
                     "Way 2, in grams. 2 kg 500 g is 2,500 g. 2,500 × 6 = 15,000 g.",
                     "15,000 g is 15 kg. Both ways give the same weight."],
                    "6 sacks weigh 15 kg in all")],
       ncert=["mul.way"], key_terms=["multiplying", "weight", "separately", "grams"],
       misconceptions=["M_ONE_PART"], minutes=6),
     A("T7.C2", "Sharing a Weight Equally", "Apply",
       "Students share a weight in kg and g equally by dividing the kg and the g separately or by changing to grams, and "
       "check by multiplying.",
       textbook=["We can also convert the quantity into grams and divide"],
       teach=["Predict first: 9 kg 600 g is shared equally into 3 boxes. Do you divide the kg and the g separately?",
              "Yes, you can. Sharing equally means dividing.",
              "Way 1, kg and g separately: 9 ÷ 3 = 3 kg and 600 ÷ 3 = 200 g, so each box has 3 kg 200 g.",
              "Way 2, in grams: 9 kg 600 g is 9,600 g and 9,600 ÷ 3 = 3,200 g, which is 3 kg 200 g.",
              "Check by multiplying: 3,200 × 3 = 9,600 g.",
              "Rule: divide the kg part and the g part, or change to grams and divide, then check by multiplying."],
       examples=[WE("9 kg 600 g of rice is shared equally into 3 bags. How much rice is in each bag? These are practice "
                    "values.",
                    ["Sharing equally means dividing: 9 kg 600 g ÷ 3.",
                     "Way 1, kg and g separately. Divide the kilograms: 9 ÷ 3 = 3 kg.",
                     "Divide the grams: 600 ÷ 3 = 200 g.",
                     "Each bag has 3 kg 200 g.",
                     "Way 2, in grams. 9 kg 600 g is 9,600 g. 9,600 ÷ 3 = 3,200 g, which is 3 kg 200 g.",
                     "Check by multiplying: 3,200 × 3 = 9,600 g, the whole weight."],
                    "Each bag has 3 kg 200 g")],
       ncert=["div.way"], key_terms=["sharing", "weight", "equally", "dividing"],
       misconceptions=["M_ONE_PART"], minutes=6),
     DOER("T7.C3", "Practice: Multiply and Divide Weights", None, "Apply",
          "Students multiply a weight by a whole number and share a weight equally, working in kg and g or in grams, and "
          "write the answer in the unit asked for.",
          ["Multiply the kg part and the g part, then exchange 1,000 g for 1 kg.",
           "To share equally, divide the kg part and the g part, or change to grams.",
           "Check by doing the opposite operation."],
          items=[FIO("ex.farmer", "Example 6: the farmer's sacks",
                     "A farmer weighs a sack of potatoes and finds it to be 10 kg 500 g. If the farmer has 4 such potato "
                     "sacks, what is the total weight of all the sacks?",
                     ["4 sacks of the same weight make 4 times that weight: 4 × 10 kg 500 g.",
                      "Multiply the kilograms: 4 × 10 = 40 kg.",
                      "Multiply the grams: 4 × 500 = 2,000 g. 1,000 g is 1 kg, so 2,000 g is 2 kg.",
                      "Add the parts: 40 kg + 2 kg = 42 kg.",
                      "Check in grams: 10 kg 500 g is 10,500 g and 10,500 × 4 = 42,000 g, which is 42 kg."],
                     "The 4 sacks weigh 42 kg in all",
                     kind="example"),
                 FIO("ex.nuts", "Example 7: the box of nuts",
                     "A box of nuts weighing 4 kg 800 g is equally distributed into 4 smaller boxes. What is the weight of "
                     "each small box in grams?",
                     ["Sharing equally into 4 boxes means dividing by 4: 4 kg 800 g ÷ 4.",
                      "Divide the kilograms: 4 ÷ 4 = 1 kg.",
                      "Divide the grams: 800 ÷ 4 = 200 g.",
                      "Each small box weighs 1 kg 200 g.",
                      "The question asks for grams. 1 kg is 1,000 g, so 1 kg 200 g is 1,200 g.",
                      "Check in grams: 4 kg 800 g is 4,800 g and 4,800 ÷ 4 = 1,200 g."],
                     "Each small box weighs 1,200 g (1 kg 200 g)",
                     kind="example")],
          misconceptions=["M_ONE_PART"])],
    key_terms=["multiplying", "sharing", "weight", "grams"]))

# ============================== T8 Cost and Scaling =======================================================
TOPICS.append(TOPIC(
    "T8", "M2", "Cost and Scaling", ["More Operations on Weight", "Let Us Do"], "Apply",
    "Students find the cost of a weight from the cost of 1 kg, and complete a double number line by doing the same to both "
    "lines.",
    "The cost of a weight is the cost of 1 kg times the kg, plus the cost of the part of a kg. On a double number line, do the "
    "same to both lines: multiply or divide both by the same number.",
    [A("T8.C1", "Cost of a Weight", "Apply",
       "Students find the cost of a weight in kg and g from the cost of 1 kg, using whole kilograms and a part of a kilogram "
       "taken from 1,000 g.",
       teach=["Predict first: rice costs ₹36 for 1 kg. What does 500 g of rice cost: ₹36, more, or less?",
              "500 g is less than 1 kg, so it costs less than ₹36. 500 g is half of 1,000 g, so it costs half of ₹36.",
              "The cost of whole kilograms is the number of kg times the cost of 1 kg.",
              "The cost of a part of a kilogram: 500 g is half of 1,000 g, 250 g is a quarter of 1,000 g, and 100 g is a "
              "tenth of 1,000 g. Take that part of the cost of 1 kg, when the price divides evenly.",
              "Then add: the cost of the whole kg and the cost of the part.",
              "Rule: whole kg times the cost of 1 kg, plus the cost of the part of a kg, taken from 1,000 g."],
       examples=[WE("Rice costs ₹36 for 1 kg. What is the cost of 4 kg 500 g of rice? These are practice values.",
                    ["Split the weight: 4 kg 500 g is 4 kg and 500 g.",
                     "The cost of 4 kg: 4 × 36 = ₹144.",
                     "500 g is half of 1,000 g, so it costs half of ₹36: 36 ÷ 2 = ₹18.",
                     "Add: 144 + 18 = ₹162.",
                     "Check: 4 kg 500 g is more than 4 kg and less than 5 kg. 4 kg costs ₹144 and 5 kg costs 5 × 36 = ₹180, "
                     "and ₹162 is between them."],
                    "4 kg 500 g of rice costs ₹162")],
       key_terms=["cost", "weight", "kilogram", "part"], misconceptions=["M_PART_FULL_PRICE"], minutes=6),
     A("T8.C2", "Scaling Both Lines Together", "Apply",
       "Students complete a double number line by finding the number the first line is multiplied by and multiplying the "
       "second line by the same number.",
       teach=["Predict first: 3 plates need 240 g of lentils. For 9 plates, do you add 6 to the 240 g, or multiply it?",
              "Look at the top line: 3 plates to 9 plates is × 3, because 3 × 3 = 9.",
              "A double number line keeps two quantities in step. Whatever you do to the top number, you do the same to the "
              "bottom number.",
              "So the bottom line is also × 3: 240 × 3 = 720 g.",
              "Adding the same number to both lines does not work. 3 + 6 = 9 plates, but 240 + 6 = 246 g is far too little "
              "for 9 plates.",
              "To go down, divide both lines by the same number.",
              "Rule: find what the first line was multiplied by, then multiply the second line by the same number."],
       examples=[WE("3 plates need 240 g of lentils. How many grams do 9 plates need? These are practice values.",
                    ["Draw a double number line. The top line is plates: 3 and 9. The bottom line is lentils: 240 g and ___ g.",
                     "From 3 plates to 9 plates the top line is multiplied by 3, because 3 × 3 = 9.",
                     "Multiply the bottom line by the same number: 240 × 3 = 720 g.",
                     "Do not add: adding 6 to 240 g gives 246 g, which is far too little.",
                     "Check: 9 plates are 3 times as many as 3 plates, so they need 3 times the lentils, and 3 × 240 = 720."],
                    "9 plates need 720 g of lentils")],
       key_terms=["scaling", "lines", "double number line", "multiplied"], misconceptions=["M_ADD_TO_SCALE"], minutes=6),
     DOER("T8.C3", "Practice: Scaling Line", "scaling_line", "Apply",
          "Students find the total cost of weights from the cost of 1 kg and complete double number lines by multiplying both "
          "lines by the same number.",
          ["The cost of whole kilograms is the number of kg times the cost of 1 kg.",
           "A part of a kg is taken from 1,000 g: 500 g is half, 250 g is a quarter and 100 g is a tenth.",
           "On a double number line, do the same to both lines."],
          items=[FIO("lud3.Q1", "Let Us Do: cost of grocery items",
                     "The cost of some grocery items is given in the following table. Find the total cost of each item. "
                     "Rice: 12 kg 500 g, cost of 1 kg ₹60. Flour: 7 kg 250 g, ₹40. Sugar: 5 kg, ₹45. Chana dal: 3 kg 600 g, "
                     "₹70. Besan: 4 kg, ₹60. Jaggery: 1 kg 400 g, ₹50.",
                     ["The total cost is the cost of 1 kg times the weight. Split each weight into whole kilograms and a part of a kilogram.",
                      "Rice, 12 kg 500 g at ₹60: 12 × 60 = ₹720. 500 g is half of 1,000 g, so it costs 60 ÷ 2 = ₹30. "
                      "720 + 30 = ₹750.",
                      "Flour, 7 kg 250 g at ₹40: 7 × 40 = ₹280. 250 g is a quarter of 1,000 g, so it costs 40 ÷ 4 = ₹10. "
                      "280 + 10 = ₹290.",
                      "Sugar, 5 kg at ₹45: 5 × 45 = ₹225.",
                      "Chana dal, 3 kg 600 g at ₹70: 3 × 70 = ₹210. 100 g is a tenth of 1,000 g, so 100 g costs 70 ÷ 10 = ₹7 "
                      "and 600 g costs 6 × 7 = ₹42. 210 + 42 = ₹252.",
                      "Besan, 4 kg at ₹60: 4 × 60 = ₹240.",
                      "Jaggery, 1 kg 400 g at ₹50: 1 × 50 = ₹50. 100 g costs 50 ÷ 10 = ₹5 and 400 g costs 4 × 5 = ₹20. "
                      "50 + 20 = ₹70.",
                      "Check: ₹750 for the rice is more than 12 kg at ₹720 and less than 13 kg at 13 × 60 = ₹780."],
                     "Rice: ₹750; Flour: ₹290; Sugar: ₹225; Chana dal: ₹252; Besan: ₹240; Jaggery: ₹70",
                     kind="exercise",
                     q_figure="A table with the columns Item, Weight, Cost of 1 kg and Total cost, the last column empty, and "
                              "six rows: Rice 12 kg 500 g ₹60, Flour 7 kg 250 g ₹40, Sugar 5 kg ₹45, Chana dal 3 kg 600 g ₹70, "
                              "Besan 4 kg ₹60 and Jaggery 1 kg 400 g ₹50."),
                 FIO("lud3.Q2", "Let Us Do: rice for 8 people",
                     "4 people need 500 g rice for a meal. How much rice will be needed for 8 people if they eat similar "
                     "quantity of rice?",
                     ["Draw a double number line. The top line is people: 4 and 8. The bottom line is rice: 500 g and ___ g.",
                      "From 4 people to 8 people the top line is multiplied by 2, because 4 × 2 = 8.",
                      "Multiply the bottom line by the same number: 500 × 2 = 1,000 g, so the arrow below is also × 2.",
                      "1,000 g is 1 kg.",
                      "Check: 8 people are twice as many as 4 people, so they need twice the rice."],
                     "8 people need 1,000 g (1 kg) of rice",
                     kind="exercise",
                     q_figure="A double number line with people above, 4 people and 8 people, and rice below, 500 g and a "
                              "blank g, an arrow × 2 above the lines and an arrow × ___ below them."),
                 FIO("lud3.Q3", "Let Us Do: tomatoes",
                     "5 kg of tomatoes cost ₹73. How much will 10 kg of tomatoes cost?",
                     ["Draw a double number line. The top line is in kilograms: 5 and 10. The bottom line is cost: ₹73 and ₹___.",
                      "From 5 kg to 10 kg the top line is multiplied by 2, because 5 × 2 = 10.",
                      "Multiply the bottom line by the same number: 73 × 2 = ₹146.",
                      "Check: 10 kg is twice 5 kg, so the cost is twice ₹73. 73 + 73 = ₹146."],
                     "10 kg of tomatoes cost ₹146",
                     kind="exercise",
                     q_figure="A double number line with kg above, 5 kg and 10 kg, and rupees below, ₹73 and a blank, an "
                              "arrow × 2 above the lines and an arrow × ___ below them."),
                 FIO("lud3.Q4", "Let Us Do: Nitesh the scrap dealer",
                     "Nitesh is a scrap dealer. How much would he have paid for (a) 16 kg of old newspaper, if he paid ₹8 for "
                     "every 1 kg of newspaper? (b) 20 kg iron, if he paid ₹200 for every 10 kg of iron? (c) 10 kg plastic, if "
                     "he paid ₹30 for 5 kg of plastic? Make double number lines for answering (b) and (c).",
                     ["(a): 1 kg of newspaper costs ₹8, so 16 kg cost 16 × 8 = ₹128.",
                      "(b): Make a double number line. The top line is in kilograms: 10 and 20. The bottom line is rupees: ₹200 and ₹___.",
                      "From 10 kg to 20 kg the top line is multiplied by 2, because 10 × 2 = 20. Multiply the bottom line by "
                      "2: 200 × 2 = ₹400.",
                      "(c): Make a double number line. The top line is in kilograms: 5 and 10. The bottom line is rupees: ₹30 and ₹___.",
                      "From 5 kg to 10 kg the top line is multiplied by 2, because 5 × 2 = 10. Multiply the bottom line by 2: "
                      "30 × 2 = ₹60.",
                      "Check (a): 10 × 8 = 80 and 6 × 8 = 48, and 80 + 48 = ₹128."],
                     "(a): ₹128; (b): ₹400; (c): ₹60",
                     kind="exercise")],
          misconceptions=["M_PART_FULL_PRICE", "M_ADD_TO_SCALE"])],
    key_terms=["cost", "weight", "double number line", "scaling"]))
