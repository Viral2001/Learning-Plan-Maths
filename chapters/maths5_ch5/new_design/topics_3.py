# -*- coding: utf-8 -*-
"""Topics T8 to T12 (module M3): Multiplying and Dividing Lengths, Let Us Estimate, Feet and Inches, the sign puzzle (a
puzzle video plus the book's own puzzle) and the Chapter Revision summary.
Every teaching concept has one worked example with the plan's own numbers (practice values); every book question is an
FIO item of its topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T8 Multiplying and Dividing Lengths ========================================
TOPICS.append(TOPIC(
    "T8", "M3", "Multiplying and Dividing Lengths", ["Multiplying and Dividing Lengths"], "Apply",
    "Students multiply and divide a length given in two units by working on each unit and regrouping, and find the "
    "price of 1 m and of any length.",
    "To multiply a length, multiply the m and the cm separately and regroup, or change it to cm and multiply. To divide, "
    "divide each unit part, or change to the smaller unit and divide. The price of 1 m is the price divided by the "
    "number of metres.",
    [A("T8.C1", "Multiplying a Length", "Apply",
       "Students multiply a length given in m and cm by a whole number by multiplying the m and the cm separately and "
       "regrouping.",
       textbook=["Break the quantity into m and cm and multiply. You can also convert it into cm and multiply."],
       teach=["Predict first: Rani sews curtains and each curtain needs 2 m 40 cm of cloth. How much cloth do 12 "
              "curtains need?",
              "Break the length into m and cm: 2 m 40 cm is 2 m and 40 cm. Multiply each part by 12.",
              "12 × 2 m = 24 m. 12 × 40 cm = 480 cm.",
              "480 cm is more than 100 cm, so change it to m and cm: 480 cm = 4 m 80 cm.",
              "Add the parts: 24 m + 4 m 80 cm = 28 m 80 cm.",
              "You can also change the length to cm first and multiply: 12 × 240 = 2,880 cm = 28 m 80 cm.",
              "Rule: break the length into m and cm and multiply each part, or change it to cm and multiply, and then "
              "regroup."],
       examples=[WE("Rani sews curtains, and each curtain needs 2 m 40 cm of cloth (practice values). How much cloth "
                    "do 12 curtains need?",
                    ["Break 2 m 40 cm into 2 m and 40 cm and multiply each part by 12.",
                     "12 × 2 m = 24 m.",
                     "12 × 40 cm = 480 cm.",
                     "480 cm = 400 cm + 80 cm = 4 m 80 cm.",
                     "Add: 24 m + 4 m 80 cm = 28 m 80 cm.",
                     "Check in cm: 12 × 240 = 2,880 cm = 28 m 80 cm."],
                    "28 m 80 cm")],
       ncert=["md.method"], key_terms=["multiply", "break the length", "regroup"], misconceptions=["M_MULT_PART"],
       minutes=6),
     A("T8.C2", "Dividing a Length", "Apply",
       "Students divide a length given in km and m by a whole number by dividing each unit part, or by changing it "
       "to the smaller unit.",
       teach=["Predict first: a pipe line of 18 km 900 m is laid in 3 equal days. How much is laid each day?",
              "Break the length into km and m: 18 km and 900 m. Divide each part by 3.",
              "18 km divided by 3 is 6 km. 900 m divided by 3 is 300 m. So each day 6 km 300 m is laid.",
              "You can also change to m first: 18 km 900 m = 18,900 m, and 18,900 ÷ 3 = 6,300 m = 6 km 300 m.",
              "Check by multiplying: 3 × 6 km 300 m = 18 km 900 m.",
              "Rule: divide each unit part, or change to the smaller unit and divide, and then change back."],
       examples=[WE("A pipe line 18 km 900 m long is laid in 3 equal days (practice values). How much is laid each "
                    "day?",
                    ["Break 18 km 900 m into 18 km and 900 m.",
                     "Divide each part by 3: 18 km divided by 3 is 6 km.",
                     "900 m divided by 3 is 300 m.",
                     "So each day 6 km 300 m is laid.",
                     "Check by changing to m: 18,900 ÷ 3 = 6,300 m = 6 km 300 m.",
                     "Check by multiplying: 3 × 6,300 = 18,900 m."],
                    "6 km 300 m each day")],
       key_terms=["divide", "equal shares", "unit part"], minutes=5),
     A("T8.C3", "Price of a Length: Double Number Line", "Apply",
       "Students find the price of 1 m from the price of a longer piece and use it to find the cost of a given length "
       "and the length for a given cost.",
       teach=["Predict first: 3 m of ribbon costs ₹90. How much does 1 m cost? How much do 9 m cost?",
              "Share the price equally among the metres: 90 ÷ 3 = ₹30 for 1 m.",
              "A double number line shows both: the top line is metres and the bottom line is rupees. If you multiply "
              "the metres by 3, multiply the price by 3 too: 3 m is ₹90, so 9 m is ₹270.",
              "To find the length for a given cost, divide the cost by the price of 1 m: ₹300 buys 300 ÷ 30 = 10 m.",
              "Rule: the price of 1 m is the price ÷ the number of metres. Then multiply it by any length."],
       examples=[WE("A shop sells ribbon at ₹90 for 3 m (practice values). What does 1 m cost? What do 9 m cost? How "
                    "many m can you buy for ₹300?",
                    ["Share the ₹90 equally among the 3 m: 90 ÷ 3 = ₹30 for 1 m.",
                     "9 m is 3 times 3 m, so the price is 3 times ₹90: 3 × 90 = ₹270.",
                     "Or 9 m at ₹30 for each metre: 9 × 30 = ₹270.",
                     "For ₹300, divide by the price of 1 m: 300 ÷ 30 = 10 m.",
                     "Check: 10 × 30 = ₹300."],
                    "1 m costs ₹30, 9 m cost ₹270, and ₹300 buys 10 m")],
       key_terms=["price", "cost", "double number line"], minutes=6),
     DOER("T8.C4", "Practice: Cut and Share", "cut_and_share", "Apply",
          "Students find the cloth for many shirts, the price of 1 m, the thread and its cost for a border, and "
          "share a road into equal days to find the length laid each day.",
          ["Break the length into two units, work on each, and regroup.",
           "The price of 1 m is the price ÷ the number of metres.",
           "To divide a length, divide each unit part or change to the smaller unit."],
          items=[FIO("md.shirt", "Example 3: cloth for 20 shirts",
                     "We need a 1 m 80 cm cloth to make a shirt for a 10 year old child. How much cloth will be "
                     "needed to make shirts for 20 such children?",
                     ["Break the length into m and cm: 1 m 80 cm is 1 m and 80 cm. Multiply each part by 20.",
                      "20 × 1 m = 20 m.",
                      "20 × 80 cm = 1,600 cm.",
                      "1,600 cm = 16 m, because 1,600 ÷ 100 = 16.",
                      "Add: 20 m + 16 m = 36 m.",
                      "Check in cm: 20 × 180 = 3,600 cm = 36 m."],
                     "36 m", kind="example"),
                 FIO("md.bag", "Example 4: the price of 1 m of cloth",
                     "A shop sells cloth for making bags at ₹100 for 5 m. How much money is needed to buy a 1 m "
                     "cloth?",
                     ["₹100 buys 5 m of cloth. To find the price of 1 m, share the ₹100 equally among the 5 m.",
                      "100 ÷ 5 = ₹20.",
                      "So a 1 m cloth costs ₹20.",
                      "Check: 5 × 20 = ₹100."],
                     "₹20", kind="example"),
                 FIO("md.line", "Multiplying and Dividing Lengths: cloth price double number line",
                     "Now, use the double number line to find the cost of the cloth or the length of cloth that we can "
                     "buy at a particular cost. Top line: 5 m, 10 m, 20 m, 40 m, ___ m. Bottom line: ₹100, ₹___, "
                     "₹___, ₹___, ₹2000. Fill in the four boxes ×___ as well.",
                     ["On the double number line the top line is m and the bottom line is rupees. From 5 m to 10 m the "
                      "length is multiplied by 2, so the price is also multiplied by 2.",
                      "The box on the top arrow is ×2, and the box on the bottom arrow from ₹100 to the next amount "
                      "is also ×2.",
                      "10 m costs 2 × ₹100 = ₹200. 20 m is 2 times 10 m, so it costs 2 × 200 = ₹400. 40 m is 2 times "
                      "20 m, so it costs 2 × 400 = ₹800.",
                      "5 m costs ₹100 and 1 m costs ₹20, so from m to rupees multiply by 20. The box between 5 m and "
                      "₹100 is ×20, and the box on the arrow from 10 m down to ₹200 is ×20 too.",
                      "₹2000 buys 2000 ÷ 20 = 100 m.",
                      "Check: 5 × 20 = 100 and 100 × 20 = 2000."],
                     "Cost: ₹200, ₹400, ₹800. Length: 100 m. Boxes: ×2, ×20, ×2, ×20",
                     kind="prompt",
                     q_figure="A double number line with five ticks: the top line is labelled 5 m, 10 m, 20 m, 40 m "
                              "and a blank m, the bottom line is labelled ₹100, three blank amounts and ₹2000, with "
                              "four empty boxes ×___: one on the top arrow from 5 m to 10 m, one between 5 m and ₹100, "
                              "one on the bottom arrow from ₹100 to the next amount, and one on the long arrow from "
                              "10 m down to the second amount.",
                     s_figure="The same double number line with every blank filled in: ₹200, ₹400, ₹800 and 100 m, "
                              "and the boxes showing ×2, ×20, ×2 and ×20."),
                 FIO("md.anita", "Multiplying and Dividing Lengths: Anita's thread",
                     "Anita is making an embroidery on the border of a sari. She needs a 1 m long thread to embroider "
                     "a 50 cm sari. How much thread would she need for a 5 m sari border? A 1 m long thread costs ₹50. "
                     "How much money will be needed to buy the thread?",
                     ["The thread is 1 m for every 50 cm of the sari border. First change the 5 m border to cm: 5 × "
                      "100 = 500 cm.",
                      "How many pieces of 50 cm are in 500 cm? 500 ÷ 50 = 10.",
                      "Each 50 cm of border needs 1 m of thread, so 10 × 1 m = 10 m of thread.",
                      "The thread costs ₹50 for 1 m, so 10 m cost 10 × 50 = ₹500.",
                      "Check: 10 m of thread for 500 cm of border, and 10 × 50 = 500."],
                     "10 m of thread, costing ₹500", kind="exercise"),
                 FIO("md.road", "Multiplying and Dividing Lengths: the road",
                     "A road 12 km 600 m long is being laid in a town. The workers lay an equal length of road each "
                     "day, and complete the work in 6 days. How much road laying work is done on each day?",
                     ["Change the road to m: 12 km 600 m = 12 × 1,000 + 600 = 12,600 m.",
                      "The same length is laid each day for 6 days: 12,600 ÷ 6 = 2,100 m.",
                      "Change back: 2,100 m = 2,000 m + 100 m = 2 km 100 m.",
                      "Another way: 12 km divided by 6 is 2 km, and 600 m divided by 6 is 100 m.",
                      "Check: 6 × 2,100 = 12,600 m."],
                     "2 km 100 m each day", kind="exercise")],
          misconceptions=["M_MULT_PART"])],
    key_terms=["multiply", "divide", "price"]))

# ============================== T9 Let Us Estimate ==========================================================
TOPICS.append(TOPIC(
    "T9", "M3", "Let Us Estimate", ["Let Us Estimate"], "Apply",
    "Students estimate a height or a depth by choosing a reference length and counting how many times it fits.",
    "An estimate uses a reference, a length you already know. Count how many times the reference fits, multiply, and "
    "say about.",
    [A("T9.C1", "Estimating with a Reference", "Apply",
       "Students estimate a height or a depth by choosing a reference length and counting how many times it fits.",
       teach=["Predict first: how could you find out about how high a wall is without a long tape?",
              "Pick a reference, a length you already know: a door, a floor of a building, or a friend. Your maths "
              "book shows children standing on each other's shoulders to reach a roof, and a ladder against a pole. "
              "Each child and the ladder are references to count.",
              "Count how many times the reference fits along the height. If a door is about 2 m high and the wall is "
              "as high as 2 doors, the wall is about 2 × 2 = 4 m high.",
              "An estimate is not exact, so say about: the wall is about 4 m high.",
              "Always say what reference you used. A different reference gives a different but close estimate.",
              "Rule: pick a reference you know, count how many times it fits, multiply, and say about."],
       examples=[WE("Sonu wants to find the height of a wall. A door beside it is about 2 m high, and the wall is as "
                    "high as 2 doors (practice values). Estimate the height of the wall.",
                    ["Choose a reference: the door, which is about 2 m high.",
                     "Count how many doors fit in the height of the wall: 2.",
                     "Multiply: 2 × 2 = 4, so 2 doors of 2 m are 4 m.",
                     "An estimate is not exact, so say that the wall is about 4 m high.",
                     "Check: put 2 doors one on top of the other and they reach the top of the wall."],
                    "The wall is about 4 m high, using a door of about 2 m as the reference")],
       ncert=["est.pictures"], key_terms=["estimate", "reference", "about"], misconceptions=["M_GUESS"], minutes=5),
     DOER("T9.C2", "Practice: Estimating Lengths", None, "Apply",
          "Students estimate the height of a building, the height of a tree and the depth of a well or pool, and say "
          "which reference length they used.",
          ["Pick a reference length that you know.",
           "Count how many times it fits and multiply.",
           "Say about, and say which reference you used."],
          items=[FIO("est.q1", "Let Us Estimate: Q1 tallest building",
                     "Estimate the following. Share your reasoning in class. The height of the tallest building in "
                     "your neighbourhood. What did you use as a reference to estimate the height?",
                     ["This depends on your own neighbourhood. The numbers below are practice values that show the "
                      "method. Yours will differ.",
                      "Choose a reference: one floor of the building, which is about 3 m high (practice value).",
                      "Count the floors of the tallest building: 5 floors.",
                      "Multiply: 5 × 3 = 15 m.",
                      "The tallest building is about 15 m high, using one floor as the reference.",
                      "Check: 5 floors on top of each other, each about 3 m, reach about 15 m."],
                     "Sample answer, practice values: about 15 m, with one floor of about 3 m as the reference. Your "
                     "answer may differ.",
                     kind="exercise"),
                 FIO("est.q2", "Let Us Estimate: Q2 tallest tree",
                     "Estimate the following. Share your reasoning in class. The height of the tallest tree in your "
                     "neighbourhood. What did you use as a reference?",
                     ["This depends on your own neighbourhood. The numbers below are practice values that show the "
                      "method. Yours will differ.",
                      "Choose a reference: a friend who is 1 m 50 cm tall, standing beside the tallest tree.",
                      "Count how many friends would stand one on top of the other to reach the top of the tree: about "
                      "8.",
                      "Change the reference to cm: 1 m 50 cm = 150 cm. Multiply: 8 × 150 = 1,200 cm.",
                      "1,200 cm = 12 m, because 1,200 ÷ 100 = 12.",
                      "The tallest tree is about 12 m high, using a friend as the reference."],
                     "Sample answer, practice values: about 12 m, with a friend of 1 m 50 cm as the reference. Your "
                     "answer may differ.",
                     kind="exercise"),
                 FIO("est.q3", "Let Us Estimate: Q3 depth of a well or pool",
                     "Estimate the following. Share your reasoning in class. The depth of a well or swimming pool in "
                     "your neighbourhood. How did you find out?",
                     ["This depends on your own neighbourhood. The numbers below are practice values that show the "
                      "method. Yours will differ.",
                      "Tie a stone to one end of a rope and lower it into the well until it touches the water.",
                      "Mark the rope at the top of the well, pull the rope up, and measure the rope up to the mark "
                      "with a long tape.",
                      "Practice value: the rope up to the mark is 7 m 50 cm long.",
                      "So the well is about 7 m 50 cm deep. For a swimming pool you can read the depth marks on the "
                      "side wall.",
                      "Check: here the reference is the rope, measured with a long tape."],
                     "Sample answer, practice values: about 7 m 50 cm, found by lowering a rope and measuring it. "
                     "Your answer may differ.",
                     kind="exercise")],
          misconceptions=["M_GUESS"])],
    key_terms=["estimate", "reference", "about"]))

# ============================== T10 Feet and Inches =========================================================
TOPICS.append(TOPIC(
    "T10", "M3", "Feet and Inches", ["Let Us Explore", "Measure Your Height"], "Understand",
    "Students change a height between feet and inches and inches using 1 foot = 12 inches, and say that 1 inch is "
    "2 cm 5 mm.",
    "Height is usually measured in feet and inches. 1 foot = 12 inches = 30 cm, and 1 inch = 2 cm 5 mm. To change feet "
    "and inches to inches, multiply the feet by 12 and add the inches.",
    [A("T10.C1", "Feet and Inches", "Understand",
       "Students change a height between feet and inches and inches using 1 foot = 12 inches, and say that 1 inch is "
       "2 cm 5 mm.",
       textbook=["In daily life, we use other units of measuring length as well. Height is usually measured in feet "
                 "and inches.",
                 "1 inch = 2 cm 5 mm",
                 "1 foot = 12 inches or 30 cm."],
       teach=["Predict first: how would you say the height of a tall person in feet and inches? How many inches are in "
              "1 foot?",
              "In daily life, we use other units of length as well. Height is usually measured in feet and inches.",
              "1 foot = 12 inches. 1 foot is also 30 cm, and 1 inch = 2 cm 5 mm.",
              "To change feet and inches to inches, multiply the feet by 12 and add the inches: 4 feet 6 inches = "
              "4 × 12 + 6 = 54 inches.",
              "To change inches to feet and inches, take out the full feet: 30 inches = 24 inches + 6 inches = 2 feet "
              "6 inches.",
              "Rule: 1 foot = 12 inches, not 10 inches. 1 foot = 30 cm and 1 inch = 2 cm 5 mm."],
       examples=[WE("Shikha's height is 4 feet 6 inches (practice values). How many inches is that? Then change 30 "
                    "inches into feet and inches.",
                    ["1 foot = 12 inches, so multiply the feet by 12.",
                     "4 feet = 4 × 12 = 48 inches.",
                     "Add the 6 inches: 48 + 6 = 54 inches.",
                     "Now 30 inches: take out the full feet. 2 feet = 2 × 12 = 24 inches.",
                     "30 − 24 = 6 inches are left, so 30 inches = 2 feet 6 inches.",
                     "Check: 2 × 12 + 6 = 30."],
                    "4 feet 6 inches = 54 inches, and 30 inches = 2 feet 6 inches")],
       ncert=["inch.def"], key_terms=["foot", "inch", "1 foot = 12 inches"], misconceptions=["M_FOOT_TEN"],
       minutes=5),
     DOER("T10.C2", "Practice: Height Chart", "height_chart", "Apply",
          "Students find how many cm and mm make 1 inch, and write the heights of students in feet and inches and "
          "find the tallest.",
          ["1 foot = 12 inches, and 1 inch = 2 cm 5 mm.",
           "To compare heights in feet and inches, change them all to inches.",
           "The tallest student has the biggest number of inches."],
          items=[FIO("inch.find", "Let Us Explore (inches): how long is 1 inch",
                     "Look at your ruler to see if inches are also marked on it. Find out how many cm and mm equal "
                     "1 inch.",
                     ["Look at your ruler. One edge has cm and mm marks, and the other edge may have inch marks.",
                      "Put the 0 of the inch scale next to the 0 of the cm scale. The 1 inch mark falls 2 cm and 5 "
                      "small marks after 0.",
                      "So 1 inch = 2 cm 5 mm.",
                      "In mm, 2 cm 5 mm = 2 × 10 + 5 = 25 mm.",
                      "Check: 12 inches = 12 × 25 = 300 mm = 30 cm, which is 1 foot."],
                     "1 inch = 2 cm 5 mm", kind="prompt",
                     s_figure="A ruler with a cm scale and an inch scale: the bracket for 1 inch covers 2 cm 5 mm."),
                 FIO("height.measure", "Measure Your Height: the tallest student",
                     "Stand against a wall and mark your height. Measure the distance between the floor and the marked "
                     "point in feet and inches. Similarly, other students in the class can also measure their heights. "
                     "Find out who is the tallest student in your class. What is his or her height in feet and "
                     "inches?",
                     ["This is an activity in your class. The numbers below are practice values that show the method. "
                      "Yours will differ.",
                      "Stand against a wall, mark your height with a pencil, and measure from the floor to the mark "
                      "in feet and inches. Practice values: the first student is 4 feet 3 inches, the second student "
                      "is 4 feet 7 inches and the third student is 4 feet 5 inches.",
                      "To compare, change each height to inches: the first student is 4 × 12 + 3 = 51 inches, the "
                      "second is 4 × 12 + 7 = 55 inches and the third is 4 × 12 + 5 = 53 inches.",
                      "Compare: 55 is more than 53, and 53 is more than 51.",
                      "So the tallest student is the second student, 4 feet 7 inches.",
                      "Check: all three have 4 feet, and 7 inches is more than 5 inches and 3 inches."],
                     "Sample answer, practice values: the tallest is the second student, 4 feet 7 inches. Your "
                     "answer may differ.",
                     kind="prompt",
                     q_figure="A child standing against a wall chart with feet and inch marks, one hand on top of the "
                              "head.")],
          misconceptions=["M_FOOT_TEN"])],
    key_terms=["foot", "inch", "height"]))

# ============================== T11 The Sign Puzzle =========================================================
TOPICS.append(TOPIC(
    "T11", "M3", "The Sign Puzzle", ["Try This"], "Apply",
    "Students fill a grid with the signs +, −, × and ÷ so that no sign repeats in a row, a column or a small box, by "
    "finding the box with only one choice at a time.",
    "In a sign grid every row and every column has each sign once. Find the box that has only one choice left, fill it, "
    "and keep using the row and the column.",
    [A("T11.C1", "Sign Puzzle: One Clue at a Time", "Apply",
       "Students fill a small grid with three signs so that no sign repeats in a row or a column, using the clues one "
       "at a time.",
       teach=["Predict first: a 3 by 3 grid must have each of the signs +, − and × once in every row and once in every "
              "column. The top left box is +, the middle box is × and the bottom right box is −. Can you fill the "
              "rest?",
              "Start with a box that has only one choice. The top middle box: its row already has + and its column "
              "already has ×. So it must be −.",
              "Now the top row has +, − and ×, so the top right box is ×.",
              "The left box of the middle row: its column has + and its row has ×. So it must be −. Then the right "
              "box of the middle row is +.",
              "The bottom row: its left box must be × and its middle box must be +, with − on the right.",
              "Check every row and every column: each has +, − and × once.",
              "Rule: find the box with only one choice left, fill it, and keep using the row and the column."],
       examples=[WE("Fill the 3 by 3 grid with the signs +, − and × so that no sign repeats in a row or a column. The "
                    "top left box is +, the middle box is × and the bottom right box is − (practice values).",
                    ["Look for a box with only one choice. The top middle box: its row has + and its column has ×, so "
                     "it must be −.",
                     "The top right box: the top row has + and −, so it must be ×.",
                     "The left box of the middle row: its column has + and its row has ×, so it must be −.",
                     "The right box of the middle row: its row has − and ×, so it must be +.",
                     "The bottom left box: its column has + and −, so it must be ×.",
                     "The bottom middle box: its row has × and −, so it must be +.",
                     "Check: row 1 is +, −, ×, row 2 is −, ×, +, row 3 is ×, +, −, and each column has +, − and × once."],
                    "Row 1: +, −, ×; row 2: −, ×, +; row 3: ×, +, −")],
       key_terms=["grid", "sign", "row", "column"], misconceptions=["M_SIGN_REPEAT"], minutes=5),
     DOER("T11.C2", "Pull it together and do it: Sign Puzzle", None, "Apply",
          "Students fill the book's 4 by 4 grid with the signs +, −, × and ÷ so that no sign repeats in any row, "
          "column or 2 × 2 box.",
          ["Every row, every column and every 2 × 2 box has the four signs once.",
           "Start with a box that has only one choice.",
           "Use the row and the column to fill the next box."],
          items=[FIO("sign.puzzle", "Try This: the sign puzzle",
                     "Put an appropriate operation sign (+, −, ×, ÷) in the empty boxes of the grid such that each "
                     "row and column and each 2 × 2 box does not repeat the sign.",
                     ["Each row, each column and each 2 × 2 box has +, −, × and ÷ once. Start with a box that has only "
                      "one choice.",
                      "Row 1 has ÷ and +, so its other two boxes are − and ×. Column 2 already has × in row 2, so the "
                      "top second box is − and the top third box is ×.",
                      "Row 4 needs ÷, + and × in its first three boxes. Column 3 already has × and +, so the bottom "
                      "third box is ÷. Column 2 already has − and ×, so the bottom second box is +, and the bottom "
                      "first box is ×.",
                      "Row 2 needs ÷, + and − in its other boxes. Column 4 already has + and −, so the right box of "
                      "row 2 is ÷. Column 3 already has ×, + and ÷, so the third box of row 2 is −, and the first box "
                      "is +.",
                      "Row 3 needs −, ÷ and ×. Column 1 already has ÷, + and ×, so the first box of row 3 is −. "
                      "Column 2 already has −, × and +, so the second box is ÷, and the last box is ×.",
                      "The completed grid: row 1 ÷, −, ×, +; row 2 +, ×, −, ÷; row 3 −, ÷, +, ×; row 4 ×, +, ÷, −.",
                      "Check: every row, every column and every 2 × 2 box has all four signs once."],
                     "Row 1: ÷, −, ×, +; row 2: +, ×, −, ÷; row 3: −, ÷, +, ×; row 4: ×, +, ÷, −",
                     kind="prompt",
                     q_figure="A grid of 4 rows and 4 columns with ÷ in the top left box, + in the top right box, × in "
                              "the second box of the second row, + in the third box of the third row and − in the "
                              "bottom right box, all other boxes empty.",
                     s_figure="The completed grid, row 1: ÷, −, ×, +, row 2: +, ×, −, ÷, row 3: −, ÷, +, ×, row 4: ×, +, ÷, −.")],
          misconceptions=["M_SIGN_REPEAT"])],
    key_terms=["grid", "sign", "row", "column"]))

# ============================== T12 Chapter Revision (summary) ==============================================
TOPICS.append(TOPIC(
    "T12", "M3", "Chapter Revision: Far and Near", ["Chapter summary"], "Understand",
    "",
    "The chapter's ideas in one walk along the measuring tape: the unit that fits, one length in two units, comparing "
    "and the difference, the kilometre and equal pieces, distance between stations, the millimetre, changing units, "
    "adding, subtracting, multiplying and dividing lengths, the price of a length, estimating, feet and inches, and "
    "the sign puzzle.",
    [A("T12.C1", "Chapter Revision: Far and Near", "Understand",
       "",
       teach=["Predict first: you have walked along the whole measuring tape of the weaving centre. Can you say one "
              "idea from each stop, from the unit that fits to the sign puzzle? Read the lines below and tick each "
              "idea you remembered.",
              "Choosing a unit: short things such as a pencil are measured in cm and long things such as a wall are "
              "measured in m, so the number sounds sensible.",
              "One length, two names: 1 m = 100 cm. 3 m = 3 × 100 = 300 cm, and 450 cm = 4 m 50 cm.",
              "Check: 5 m = 5 × 100 = 500 cm, so 480 cm is less than 5 m.",
              "Comparing: change both lengths to the same unit, then compare. 4 m 3 cm = 403 cm, which is less than "
              "430 cm.",
              "Difference: the bigger length minus the smaller length in the same unit. 285 − 260 = 25 cm.",
              "The kilometre: 1 km = 1,000 m, so 7 km = 7 × 1,000 = 7,000 m.",
              "Equal pieces: a 2 km track with a flag after every 400 m needs 2,000 ÷ 400 = 5 flags.",
              "Check: how many ropes of 125 m make 1 km? 1,000 ÷ 125 = 8 ropes.",
              "Distance between two stations: subtract the two distances from the start. 615 − 340 = 275 km.",
              "The millimetre: 1 cm = 10 mm, so 3 cm = 3 × 10 = 30 mm, and 4 cm 6 mm = 4 × 10 + 6 = 46 mm.",
              "Changing units: from a bigger unit to a smaller unit multiply by 10, 100 or 1,000, and from a smaller "
              "unit to a bigger unit divide. 9 m = 9 × 100 = 900 cm and 4,000 m = 4,000 ÷ 1,000 = 4 km.",
              "Check: write 7,305 cm in m and cm. 7,305 cm = 7,300 cm + 5 cm = 73 m 5 cm.",
              "Adding: add like units and regroup. 2 km 700 m + 1 km 800 m = 4 km 500 m.",
              "Subtracting: change both to the smaller unit, or regroup 1 m as 100 cm. 9 m − 3 m 40 cm = 5 m 60 cm.",
              "Multiplying and dividing: break the length into two units and work on each. 12 × 2 m 40 cm = 28 m "
              "80 cm, and 18 km 900 m divided by 3 is 6 km 300 m.",
              "Price: 3 m of ribbon costs ₹90, so 1 m costs 90 ÷ 3 = ₹30.",
              "Estimating: pick a reference you know, count how many times it fits, and say about. A wall as high as "
              "2 doors of 2 m is about 4 m high.",
              "Feet and inches: 1 foot = 12 inches. 4 feet 6 inches = 4 × 12 + 6 = 54 inches.",
              "Sign puzzle: fill the box that has only one choice left, using its row and its column."],
       ncert=["summary"], key_terms=["unit", "1 m = 100 cm", "1 km = 1,000 m", "1 cm = 10 mm"], minutes=6,
       enrichment=True)],
    topic_type="summary"))
