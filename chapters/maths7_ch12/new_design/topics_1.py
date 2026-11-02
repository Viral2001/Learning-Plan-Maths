# -*- coding: utf-8 -*-
"""Topics T1 to T5 (module M1: multiplying decimals). Book sections 4.1 and 4.2."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Introduction ==============================================================
TOPICS.append(TOPIC(
    "T1", "M1", "Arshad's Pens", ["Chapter opening", "4.2"], "Understand",
    "",
    "Five pens at nine rupees fifty paisa each, and an open question: how do we multiply a number that has a "
    "decimal point?",
    [A("T1.C1", "A bill with a decimal point in it", "Remember",
       "",
       textbook=["Another Peek Beyond the Point",
                 "We have already learned how to multiply and divide fractions. In this chapter, we will learn how to "
                 "perform these operations with decimals.",
                 "You will see that the procedures for multiplying and dividing decimals are natural extensions of the "
                 "procedures for multiplying and dividing counting numbers."],
       teach=["Picture a stationery shop counter. Arshad picks 5 pens, and each pen costs ₹9.5, that is 9 rupees "
              "and 50 paisa.",
              "Make a guess before the next step: what should he pay? Can you find it by adding, and can you find it "
              "by multiplying?"],
       ncert=["opening"], key_terms=["decimal"], video_focus=["HOOK"], minutes=4, enrichment=True),
     A("T1.C2", "The question to keep: how do we multiply decimals?", "Understand", "",
       teach=["Predict: is the cost of 5 pens more than ₹45 or less than ₹50?",
              "Adding 9.5 five times works for 5 pens, but it is slow for 7.5 litres or 13.3 cm.",
              "Keep this question in mind: the next topics turn a decimal into a fraction and multiply."],
       enrichment=True)],
    topic_type="framing"))

# ============================== T2 Recap of decimals ===========================================================
TOPICS.append(TOPIC(
    "T2", "M1", "A Quick Recap of Decimals", ["4.1"], "Understand",
    "Students read a decimal by its place values, write fractions with denominators 10, 100 and 1000 as decimals, "
    "express grams as decimal kilograms, and divide a number by 10, 100 or 1000 by moving the decimal point.",
    "A decimal is a sum of tenths, hundredths and thousandths, so a fraction with denominator 10, 100 or 1000 is "
    "written as a decimal at once.",
    [A("T2.C1", "Tenths, hundredths and thousandths", "Understand",
       "Students name the tenth, hundredth and thousandth place of each digit of a decimal and write fractions with "
       "denominators 10, 100 and 1000 as decimals, including grams written in kilograms.",
       textbook=["4.1 A Quick Recap of Decimals",
                 "Recall that decimals are the natural extension of the Indian place value system to represent decimal "
                 "fractions (1/10, 1/100, 1/1000, and so on) and their sums.",
                 "For example, 27.53 refers to a quantity that has: 2 Tens, 7 Units (Ones), 5 Tenths, 3 Hundredths.",
                 "Jonali and Pallabi play a game. Jonali says a fraction and Pallabi gives the equivalent decimal. "
                 "Write Pallabi's answer in the blank spaces.",
                 "Jonali goes to the market to buy spices. She purchases 50 g of Cinnamon, 100 g of Cumin seeds, 25 g "
                 "of Cardamom and 250 g of Pepper. Express each of the quantities in kilograms by writing them in "
                 "terms of fractions as well as decimals.",
                 "The fractions Jonali gave Pallabi have denominators 10, 100, 1000, and so on."],
       teach=["Predict first: in 27.53, which digit counts hundredths?",
              "27.53 is 2 Tens, 7 Ones, 5 Tenths and 3 Hundredths.",
              "A denominator of 10, 100 or 1000 tells how many places come after the point: 4/100 = 0.04, "
              "67/1000 = 0.067, 457/100 = 4.57, 71/100 = 0.71, 43/100 = 0.43 and 9/100 = 0.09.",
              "1 kg is 1000 g, so grams become kilograms by dividing by 1000."],
       examples=[
           WE("Jonali buys 50 g of cinnamon, 100 g of cumin seeds, 25 g of cardamom and 250 g of pepper. Write each "
              "quantity in kilograms as a fraction and as a decimal.",
              ["1 kg is 1000 g, so each quantity in grams is divided by 1000.",
               "Cinnamon: 50/1000 = 1/20 kg, which is 0.05 kg.",
               "Cumin seeds: 100/1000 = 1/10 kg, which is 0.1 kg.",
               "Cardamom: 25/1000 = 1/40 kg, which is 0.025 kg.",
               "Pepper: 250/1000 = 1/4 kg, which is 0.25 kg."],
              "Cinnamon 1/20 kg or 0.05 kg; cumin 1/10 kg or 0.1 kg; cardamom 1/40 kg or 0.025 kg; pepper 1/4 kg "
              "or 0.25 kg", ncert=["4.1.place_value", "4.1.game", "4.1.spices"])],
       key_terms=["tenth", "hundredth", "thousandth"], misconceptions=["M_MISSING_ZERO"], minutes=10),
     A("T2.C2", "Expanding a fraction, and dividing by 10, 100, 1000", "Apply",
       "Students expand a fraction with denominator 10, 100, 1000 or 10000 as a sum of tenths, hundredths and "
       "thousandths, and divide any number by 10, 100 or 1000 by moving the decimal point left.",
       textbook=["Write the following fractions as a sum of fractions and also as decimals: 254/1000 = 200/1000 + "
                 "50/1000 + 4/1000 = 2/10 + 5/100 + 4/1000, that is 0.2 + 0.05 + 0.004 = 0.254; then 847/10000, "
                 "173/100, 23/1000.",
                 "Can you give a simple rule to divide any number by a number of the form 1 followed by zeroes, 10, "
                 "100, 1000, etc.? For example, 123/10, 24/100 or 678/1000? Look for a pattern in the previous "
                 "problems.",
                 "Here is one such rule. Let us consider the example 123 ÷ 10.",
                 "Step 1: Write the dividend as it is and place a decimal point at the end. 123.",
                 "Step 2: Count the number of zeroes in the divisor. 10 has 1 zero.",
                 "Step 3: Move the decimal point from Step 1 left by the same number of places as the count from "
                 "Step 2. Add zeroes in front if needed. 12.3",
                 "Examples: 24 ÷ 100 = 0.24, 678 ÷ 1000 = 0.678, 12 ÷ 1000 = 0.012, 12345 ÷ 1000 = 12.345."],
       teach=["Predict first: is 123 ÷ 10 more than 10 or less than 10?",
              "Split the numerator by place value: 847/10000 = 8/100 + 4/1000 + 7/10000, that is 0.0847.",
              "Dividing by 10, 100 or 1000 moves the decimal point left by 1, 2 or 3 places; write zeroes in front "
              "when the digits run out."],
       examples=[
           WE("Write 847/10000, 173/100 and 23/1000 as a sum of tenths, hundredths and thousandths, and as decimals.",
              ["847/10000 = 800/10000 + 40/10000 + 7/10000 = 8/100 + 4/1000 + 7/10000.",
               "So 847/10000 = 0.08 + 0.004 + 0.0007 = 0.0847.",
               "173/100 = 100/100 + 70/100 + 3/100 = 1 + 7/10 + 3/100, so 173/100 = 1.73.",
               "23/1000 = 20/1000 + 3/1000 = 2/100 + 3/1000, so 23/1000 = 0.023."],
              "0.0847, 1.73 and 0.023", ncert=["4.1.expand_table"]),
           WE("Use the rule of moving the decimal point to find 123 ÷ 10, 24 ÷ 100, 678 ÷ 1000 and 12 ÷ 1000.",
              ["123 ÷ 10: write 123. and move the point 1 place left, so 123 ÷ 10 = 12.3.",
               "24 ÷ 100: move the point 2 places left, so 24 ÷ 100 = 0.24.",
               "678 ÷ 1000: move the point 3 places left, so 678 ÷ 1000 = 0.678.",
               "12 ÷ 1000: there are only 2 digits, so write a zero in front, giving 12 ÷ 1000 = 0.012."],
              "12.3, 0.24, 0.678 and 0.012", ncert=["4.1.div_rule"])],
       key_terms=["place value", "dividend", "divisor"], misconceptions=["M_POINT_WRONG_WAY", "M_MISSING_ZERO"],
       minutes=10),
     DOER("T2.C3", "Practice: fractions, decimals and moving the point", None, "Apply",
          "Students write fractions with denominators 10, 100 and 1000 as decimals and divide whole numbers by 10, "
          "100 and 1000 by moving the decimal point.",
          ["The number of zeroes in the denominator is the number of digits after the decimal point.",
           "Dividing by 10, 100 or 1000 moves the decimal point left by 1, 2 or 3 places.",
           "Write zeroes in front when there are not enough digits."])]))

# ============================== T3 Multiplying via fractions ===================================================
TOPICS.append(TOPIC(
    "T3", "M1", "Multiplying Decimals through Fractions", ["4.2"], "Apply",
    "Students multiply a decimal by a whole number and by another decimal by writing each decimal as a fraction "
    "with denominator 10, 100 or 1000, multiplying numerators and denominators, and writing the result back as a "
    "decimal, in shopping, travel, walking and area problems.",
    "A decimal is a fraction, so multiplying decimals is multiplying fractions: numerators together, denominators "
    "together.",
    [A("T3.C1", "Pens and petrol: a decimal times a number", "Apply",
       "Students find the cost of pens and the distance a car covers by writing each decimal as a fraction, "
       "multiplying, and converting the product back to a decimal.",
       textbook=["4.2 Decimal Multiplication",
                 "Example 1: Arshad goes to a stationery shop and purchases 5 pens. If one pen costs ₹9.5 (9 rupees "
                 "and 50 paisa), how much should he pay the shopkeeper?",
                 "What operation must we use here?",
                 "We have to multiply 9.5 by 5, which is the same as adding 9.5, 5 times. That is 9.5 × 5 = 9.5 + "
                 "9.5 + 9.5 + 9.5 + 9.5 = 47.5.",
                 "We can also directly multiply the numbers by converting them into fractions. 9.5 is 95/10 and 5 is "
                 "5/1 as a fraction.",
                 "Recall that, to find the product of two fractions, we multiply the numerators and multiply the "
                 "denominators.",
                 "Example 2: A car travels 12.5 km per litre of petrol. What is the distance covered with 7.5 litres "
                 "of petrol?"],
       teach=["Predict first: is 5 pens at ₹9.5 nearer ₹45 or ₹50?",
              "Repeated addition works: 9.5 + 9.5 + 9.5 + 9.5 + 9.5 = 47.5.",
              "Writing 9.5 as 95/10 turns the problem into fraction multiplication, which also works when neither "
              "number is whole."],
       examples=[
           WE("Arshad buys 5 pens. One pen costs ₹9.5. How much should he pay?",
              ["Repeated addition: 9.5 + 9.5 + 9.5 + 9.5 + 9.5 = 47.5.",
               "As fractions: 9.5 is 95/10 and 5 is 5/1.",
               "5/1 × 95/10 = (5 × 95)/(1 × 10) = 475/10 = 47.5.",
               "So 5 pens cost ₹47.5."],
              "₹47.5", ncert=["4.2.ex1"]),
           WE("A car travels 12.5 km per litre of petrol. What distance does it cover with 7.5 litres?",
              ["We multiply 12.5 by 7.5.", "12.5 is 125/10 and 7.5 is 75/10.",
               "125/10 × 75/10 = (125 × 75)/(10 × 10) = 9375/100 = 93.75.",
               "The car covers 93.75 km."],
              "93.75 km", ncert=["4.2.ex2"])],
       key_terms=["product", "fraction"], misconceptions=["M_POINT_ALIGN"], minutes=10),
     A("T3.C2", "Can a product of decimals be a natural number?", "Analyze",
       "Students test whether the product of two decimals, or of a decimal and a natural number, can be a natural "
       "number, and explain the answer with fractions.",
       textbook=["Can the product of two decimals be a natural number?",
                 "Can the product of a decimal and a natural number be a natural number?"],
       teach=["Predict first: can two numbers with digits after the point multiply to give a whole number?",
              "Write the decimals as fractions: the product is a natural number when the numerator of the product "
              "is a multiple of its denominator.",
              "Yes to both: for example 2.5 × 0.4 = 1 and 0.25 × 8 = 2."],
       examples=[
           WE("Can the product of two decimals be a natural number? Can the product of a decimal and a natural number "
              "be a natural number? Test 2.5 × 0.4 and 0.25 × 8.",
              ["2.5 × 0.4 = 25/10 × 4/10 = 100/100 = 1, a natural number.",
               "0.25 × 8 = 25/100 × 8 = 200/100 = 2, a natural number.",
               "So the answer to both questions is yes.",
               "It happens when the product of the numerators is a multiple of the product of the denominators."],
              "Yes to both, for example 2.5 × 0.4 = 1 and 0.25 × 8 = 2", ncert=["4.2.natural"])],
       key_terms=["natural number"], misconceptions=["M_PRODUCT_BIGGER"], minutes=8),
     A("T3.C3", "Walking to school and the area of a rectangle", "Apply",
       "Students convert metres to kilometres and multiply a decimal twice to find a weekly walking distance, and "
       "multiply two decimals to find the area of a rectangle.",
       textbook=["Example 3: The distance between Ajay's school and his home is 827 m. He walks to school in the "
                 "morning and then walks back home in the evening, 6 days a week. How much does he walk in a week? "
                 "Answer in kilometres.",
                 "Each way between school and home, Ajay walks 827 metres, i.e., 0.827 km.",
                 "Example 4: Find the area of the given rectangle. (5.7 cm by 13.3 cm)"],
       teach=["Predict first: is Ajay's weekly walk more or less than 10 km?",
              "Convert first: 827 m is 827/1000 km, that is 0.827 km.",
              "The area of a rectangle is length times breadth, also when the sides are decimals."],
       examples=[
           WE("Ajay's school is 827 m from his home. He walks there and back 6 days a week. How far does he walk in "
              "a week, in kilometres?",
              ["827 m is 827/1000 km, that is 0.827 km.",
               "In a day: 0.827 × 2 = 827/1000 × 2 = 1654/1000 = 1.654 km.",
               "In a week: 1.654 × 6 = 1654/1000 × 6 = 9924/1000 = 9.924 km."],
              "9.924 km", ncert=["4.2.ex3"]),
           WE("Find the area of a rectangle 5.7 cm by 13.3 cm.",
              ["Area = 5.7 × 13.3.", "5.7 × 13.3 = 57/10 × 133/10 = 7581/100 = 75.81.",
               "The area is 75.81 sq cm."],
              "75.81 sq cm", ncert=["4.2.ex4"])],
       key_terms=["kilometre", "area"], misconceptions=["M_UNIT_MIX"], minutes=10),
     DOER("T3.C4", "Practice: multiply decimals as fractions", None, "Apply",
          "Students multiply decimals in shopping, cloth, coin and profit problems by writing each decimal as a "
          "fraction, multiplying, and converting back, checking units before multiplying.",
          ["Write each decimal as a fraction with denominator 10, 100 or 1000.",
           "Multiply the numerators, multiply the denominators, then write the result as a decimal.",
           "Convert units first when the answer is asked in a different unit."],
          items=[
              FIO("4.2.FiO1", "Figure it Out (decimal multiplication), Q1",
                  "Recall that a tenth is 0.1, a hundredth is 0.01, and so on. Find the following products in "
                  "tenths, hundredths and so on: (a) 6 × 4 tenths (24 tenths) (b) 7 × 0.3 (c) 9 × 5 hundredths",
                  ["(a) 6 times 4 tenths is 24 tenths, and 24/10 = 2.4.",
                   "(b) 0.3 is 3 tenths; 7 times 3 tenths is 21 tenths, so 7 × 0.3 = 2.1.",
                   "(c) 9 times 5 hundredths is 45 hundredths, and 45/100 = 0.45."],
                  "(a) 24 tenths, that is 2.4 (b) 21 tenths, that is 2.1 (c) 45 hundredths, that is 0.45"),
              FIO("4.2.FiO3", "Figure it Out (decimal multiplication), Q3",
                  "Thejus needs 1.65 m of cloth for a shirt. How many metres of cloth are needed for 3 shirts?",
                  ["Cloth for 3 shirts = 1.65 × 3.", "1.65 × 3 = 165/100 × 3 = 495/100 = 4.95."],
                  "4.95 m"),
              FIO("4.2.FiO4", "Figure it Out (decimal multiplication), Q4",
                  "Meenu bought 4 notebooks and 3 erasers. The cost of each book was ₹15.50 and each eraser was "
                  "₹2.75. How much did she spend in all?",
                  ["Notebooks: 15.50 × 4 = 1550/100 × 4 = 6200/100 = 62, so ₹62.",
                   "Erasers: 2.75 × 3 = 275/100 × 3 = 825/100 = 8.25, so ₹8.25.",
                   "In all: 62 + 8.25 = 70.25, so she spent ₹70.25."],
                  "₹70.25"),
              FIO("4.2.FiO5", "Figure it Out (decimal multiplication), Q5",
                  "The thickness of a rupee coin is 1.45 mm. What is the total height of the cylinder formed by "
                  "placing 36 rupee coins one over the other? Write the answer in centimetres.",
                  ["Height = 1.45 × 36 mm.", "1.45 × 36 = 145/100 × 36 = 5220/100 = 52.2 mm.",
                   "10 mm make 1 cm, so 52.2 mm is 52.2 ÷ 10 = 5.22 cm."],
                  "5.22 cm"),
              FIO("4.2.FiO7", "Figure it Out (decimal multiplication), Q7",
                  "Dwarakanath purchases notebooks at a wholesale price of ₹23.6 per piece and sells each notebook "
                  "at ₹30. How much profit does he make if he sells 50 books in a week?",
                  ["Profit on one notebook: 30 − 23.6 = 6.4, so ₹6.4.",
                   "Profit on 50 notebooks: 6.4 × 50 = 64/10 × 50 = 3200/10 = 320."],
                  "₹320"),
          ])]))

# ============================== T4 Decimal places rule =========================================================
TOPICS.append(TOPIC(
    "T4", "M1", "The Rule of Decimal Places", ["4.2"], "Apply",
    "Students observe that the number of digits after the decimal point in a product is the total of those in the "
    "multiplier and multiplicand, explain the rule from the denominators, and use a given product of whole numbers "
    "to place the decimal point in related products.",
    "Multiply as if there were no decimal points, then give the product as many decimal places as the two numbers "
    "have together.",
    [A("T4.C1", "Counting digits after the point", "Analyze",
       "Students compare the digits after the decimal point in the multiplier, the multiplicand and the product for "
       "several products, and link the count to the zeroes in the denominator.",
       textbook=["Observe the number of digits after the decimal point in the multiplier, the multiplicand and the "
                 "product. Also note the number of zeroes in the denominator.",
                 "9.5 × 5 = (95 × 5)/10 = 475/10 = 47.5: 1, 0, 1.",
                 "12.5 × 7.5 = 125/10 × 75/10 = 9375/100 = 93.75: 1, 1, 2.",
                 "1.64 × 6 = 164/100 × 6 = 984/100 = 9.84: 2, 0, 2.",
                 "5.7 × 13.35 = 57/10 × 1335/100 = (57 × 1335)/(10 × 100) = 76095/1000 = 76.095: 1, 2, 3."],
       teach=["Predict first: how many digits after the point will 5.7 × 13.35 have?",
              "Each decimal place is a factor of 10 in the denominator; multiplying the denominators adds the zeroes.",
              "So the digits after the point in the product are the sum of the digits after the point in the two "
              "numbers."],
       examples=[
           WE("Find 1.64 × 6 and 5.7 × 13.35 as fractions, and count the digits after the decimal point in each number "
              "and in the product.",
              ["1.64 × 6 = 164/100 × 6 = 984/100 = 9.84.",
               "Digits after the point: 2 in 1.64, 0 in 6, 2 in 9.84.",
               "5.7 × 13.35 = 57/10 × 1335/100 = 76095/1000 = 76.095.",
               "Digits after the point: 1 in 5.7, 2 in 13.35, 3 in 76.095.",
               "In both, the product has as many digits after the point as the two numbers together."],
              "9.84 (2 + 0 places) and 76.095 (1 + 2 places)", ncert=["4.2.digits_table"])],
       key_terms=["multiplier", "multiplicand", "decimal place"], misconceptions=["M_POINT_ALIGN"], minutes=10),
     A("T4.C2", "From whole-number products to decimal products", "Apply",
       "Students state the rule for multiplying decimals, use 596 × 248 = 147808 to write 5.96 × 24.8 at once, and "
       "find 5.8 × 1.24 by the rule and check it with fractions.",
       textbook=["Suppose we know that 596 × 248 = 147808, can you immediately write down the product of 5.96 × 24.8?",
                 "By looking at the above examples, can you frame a rule to multiply two decimals?",
                 "Multiplication of decimals is the same as the multiplication of their corresponding fractions. When "
                 "multiplying fractions, we multiply the numerators and denominators, respectively.",
                 "The product of the numerators = Product of the numbers with the decimal points removed.",
                 "Since both the denominators are of the form 1, 10, 100, 1000, …, the product of the denominators is "
                 "also of the form 1 followed by zeroes. The number of zeroes in the product is the sum of the number "
                 "of zeroes in each denominator.",
                 "In the product, the decimal point is placed based on the total number of zeroes in the denominator.",
                 "So, to multiply two decimals, we can multiply the two numbers obtained by removing the decimal "
                 "point, and then place the decimal point appropriately.",
                 "Example 5: Let us use the above rule to find the product of 5.8 and 1.24. Let us first multiply 58 "
                 "and 124. The product is 7192. The sum of the number of digits after the decimal point in the "
                 "multiplier and multiplicand is 3. So, the product is 7.192. Verify this by converting the "
                 "multiplier and multiplicand into fractions."],
       teach=["Predict first: 596 × 248 = 147808. Where does the point go in 5.96 × 24.8?",
              "Remove the points, multiply the whole numbers, then count the decimal places of both numbers together.",
              "Check the size: 5.96 × 24.8 is about 6 × 25, so the answer near 150 is sensible."],
       examples=[
           WE("Given 596 × 248 = 147808, write down 5.96 × 24.8.",
              ["Remove the points: 596 × 248 = 147808.",
               "5.96 has 2 decimal places and 24.8 has 1, so the product has 2 + 1 = 3 decimal places.",
               "So 5.96 × 24.8 = 147.808.",
               "Check the size: about 6 × 25 = 150, close to 147.808."],
              "147.808", ncert=["4.2.known_product", "4.2.rule"]),
           WE("Find 5.8 × 1.24 by the rule, and verify with fractions.",
              ["58 × 124 = 7192.",
               "5.8 has 1 decimal place and 1.24 has 2, so the product has 3 decimal places: 7.192.",
               "Check: 58/10 × 124/100 = 7192/1000 = 7.192."],
              "7.192", ncert=["4.2.ex5"])],
       key_terms=["decimal place"], misconceptions=["M_POINT_ALIGN"], minutes=10),
     DOER("T4.C3", "Practice: place the decimal point", "decimal_place_counter", "Apply",
          "Students multiply decimals by the rule of decimal places, use a given whole-number product to write "
          "related decimal products, and multiply decimals by 10, 100 and 1000.",
          ["Multiply the numbers with the points removed.",
           "Count the decimal places in both numbers and add them; that is the number of decimal places in the "
           "product.",
           "Zeroes at the end of a decimal do not change its value."],
          items=[
              FIO("4.2.FiO2", "Figure it Out (decimal multiplication), Q2",
                  "Find the products: (a) 27.34 × 6 (b) 4.23 × 3.7 (c) 0.432 × 0.23",
                  ["(a) 2734 × 6 = 16404; 2 + 0 = 2 decimal places, so 27.34 × 6 = 164.04.",
                   "(b) 423 × 37 = 15651; 2 + 1 = 3 decimal places, so 4.23 × 3.7 = 15.651.",
                   "(c) 432 × 23 = 9936; 3 + 2 = 5 decimal places, so 0.432 × 0.23 = 0.09936."],
                  "(a) 164.04 (b) 15.651 (c) 0.09936"),
              FIO("4.2.FiO6", "Figure it Out (decimal multiplication), Q6",
                  "The price of 1 kg of oranges is ₹56.50. What is the price of 2.250 kg of oranges? Can we write "
                  "56.50 as 56.5 and 2.250 as 2.25 and multiply? Will we get the same product? Why?",
                  ["565 × 225 = 127125; 1 + 2 = 3 decimal places, so 56.5 × 2.25 = 127.125.",
                   "With the zeroes: 5650 × 2250 = 12712500; 2 + 3 = 5 decimal places gives 127.12500, the same "
                   "number.",
                   "Yes: 56.50 = 56.5 and 2.250 = 2.25, because zeroes at the end after the point add 0 hundredths or "
                   "0 thousandths and do not change the value."],
                  "₹127.125; yes, the product is the same because zeroes at the end of a decimal do not change its "
                  "value"),
              FIO("4.2.FiO8", "Figure it Out (decimal multiplication), Q8",
                  "Given that 18 × 12 = 216, find the products: (a) 18 × 1.2 (b) 18 × 0.12 (c) 1.8 × 1.2 "
                  "(d) 0.18 × 0.12 (e) 0.018 × 0.012 (f) 1.8 × 12. In which of the cases above is the product less "
                  "than 1?",
                  ["(a) 1 decimal place: 18 × 1.2 = 21.6.", "(b) 2 decimal places: 18 × 0.12 = 2.16.",
                   "(c) 1 + 1 = 2 decimal places: 1.8 × 1.2 = 2.16.",
                   "(d) 2 + 2 = 4 decimal places: 0.18 × 0.12 = 0.0216.",
                   "(e) 3 + 3 = 6 decimal places: 0.018 × 0.012 = 0.000216.",
                   "(f) 1 decimal place: 1.8 × 12 = 21.6.",
                   "The products less than 1 are (d) and (e)."],
                  "(a) 21.6 (b) 2.16 (c) 2.16 (d) 0.0216 (e) 0.000216 (f) 21.6; less than 1 in (d) and (e)"),
              FIO("4.2.FiO10", "Figure it Out (decimal multiplication), Q10",
                  "Multiply the following numbers by 10, 100 and 1000 to complete the table: 5.7, 23.02, 0.92, "
                  "0.306, 24.67",
                  ["Multiplying by 10, 100 or 1000 moves the decimal point right by 1, 2 or 3 places.",
                   "5.7 × 10 = 57, 5.7 × 100 = 570, 5.7 × 1000 = 5700.",
                   "23.02 × 10 = 230.2, 23.02 × 100 = 2302, 23.02 × 1000 = 23020.",
                   "0.92 × 10 = 9.2, 0.92 × 100 = 92, 0.92 × 1000 = 920.",
                   "0.306 × 10 = 3.06, 0.306 × 100 = 30.6, 0.306 × 1000 = 306.",
                   "24.67 × 10 = 246.7, 24.67 × 100 = 2467, 24.67 × 1000 = 24670."],
                  "5.7: 57, 570, 5700; 23.02: 230.2, 2302, 23020; 0.92: 9.2, 92, 920; 0.306: 3.06, 30.6, 306; "
                  "24.67: 246.7, 2467, 24670", tool="decimal_place_counter"),
          ])]))

# ============================== T5 Is the product always greater ===============================================
TOPICS.append(TOPIC(
    "T5", "M1", "Is the Product Always Greater?", ["4.2"], "Analyze",
    "Students compare a product with the two numbers multiplied, sort products into three situations by whether "
    "each number is greater than 1 or between 0 and 1, and predict whether a product is less than 1 without "
    "multiplying.",
    "Multiplying by a number between 0 and 1 makes a number smaller; multiplying by a number greater than 1 makes "
    "it bigger.",
    [A("T5.C1", "Three products compared with their numbers", "Analyze",
       "Students compute 2.25 × 8, 0.25 × 8 and 0.25 × 0.8 and compare each product with the two numbers multiplied.",
       textbook=["Is the Product Always Greater than the Numbers Multiplied?",
                 "Recall multiplication of two fractions. Unlike counting numbers, when two fractions are multiplied "
                 "the product is not always greater than or equal to both numbers. Let us examine the case of the "
                 "product of two decimals.",
                 "2.25 × 8 = 18. In the above multiplication, the product (18) is greater than 2.25 and 8.",
                 "But in, 0.25 × 8 = 2, the product (2) is greater than 0.25 but less than 8.",
                 "In the case of 0.25 × 0.8 = 0.2, the product (0.2) is less than both 0.25 and 0.8.",
                 "When is the product of two decimals greater than both the numbers? When is it less than both the "
                 "numbers?"],
       teach=["Predict first: is 0.25 × 8 more than 8 or less than 8?",
              "Multiplying by 0.25 takes a quarter, so 0.25 × 8 is a quarter of 8, which is 2.",
              "A product can be greater than both numbers, between them, or less than both."],
       examples=[
           WE("Find 2.25 × 8, 0.25 × 8 and 0.25 × 0.8, and compare each product with the two numbers multiplied.",
              ["225 × 8 = 1800 with 2 decimal places, so 2.25 × 8 = 18, greater than both 2.25 and 8.",
               "0.25 × 8 = 2: greater than 0.25 but less than 8.",
               "25 × 8 = 200 with 3 decimal places, so 0.25 × 0.8 = 0.2, less than both 0.25 and 0.8."],
              "18 is greater than both; 2 is between 0.25 and 8; 0.2 is less than both", ncert=["4.2.size_three"])],
       key_terms=["product"], misconceptions=["M_PRODUCT_BIGGER"], minutes=8),
     A("T5.C2", "Three situations for a product", "Analyze",
       "Students sort products into three situations, both numbers greater than 1, both between 0 and 1, or one of "
       "each, and state how the product compares with the numbers in each.",
       textbook=["Since decimals are just representations of fractions, the relationship between the numbers "
                 "multiplied and the product are similar to fractions.",
                 "Situation 1: Both numbers are greater than 1 (e.g., 3.4 × 6.5). The product (22.1) is greater than "
                 "both the numbers.",
                 "Situation 2: Both numbers are between 0 and 1 (e.g., 0.75 × 0.4). The product (0.3) is less than "
                 "both the numbers.",
                 "Situation 3: One number is between 0 and 1 and one number is greater than 1 (e.g., 0.75 × 5). The "
                 "product (3.75) is less than the number greater than 1 and greater than the number between 0 and 1."],
       teach=["Predict first: without multiplying, is 0.75 × 0.4 less than 1?",
              "Taking a part of a number less than 1 gives an even smaller number.",
              "Taking a part of a number greater than 1 lands between the two numbers."],
       examples=[
           WE("Find 3.4 × 6.5, 0.75 × 0.4 and 0.75 × 5, and say how each product compares with the numbers multiplied.",
              ["34 × 65 = 2210 with 2 decimal places, so 3.4 × 6.5 = 22.1, greater than both numbers.",
               "75 × 4 = 300 with 3 decimal places, so 0.75 × 0.4 = 0.3, less than both numbers.",
               "75 × 5 = 375 with 2 decimal places, so 0.75 × 5 = 3.75, between 0.75 and 5."],
              "22.1 is greater than both; 0.3 is less than both; 3.75 is between 0.75 and 5",
              ncert=["4.2.situations"])],
       key_terms=["product"], misconceptions=["M_PRODUCT_BIGGER"], minutes=8),
     DOER("T5.C3", "Practice: predict the size of a product", "product_size_predictor", "Analyze",
          "Students predict whether a product is greater than both numbers, between them or less than both, and "
          "whether it is less than 1, before multiplying, then check.",
          ["Both numbers greater than 1: the product is greater than both.",
           "Both numbers between 0 and 1: the product is less than both.",
           "One of each: the product lies between the two numbers."],
          items=[
              FIO("4.2.FiO9", "Figure it Out (decimal multiplication), Q9",
                  "In which of the following multiplications is the product less than 1? Can you find the answer "
                  "without actually doing the multiplications? (a) 7 × 0.6 (b) 0.7 × 0.6 (c) 0.7 × 6 (d) 0.07 × 0.06",
                  ["When both numbers are between 0 and 1 the product is less than both, so less than 1: (b) and (d).",
                   "In (a) and (c), 0.6 of 7 and 0.7 of 6 are more than half of a number above 2, so more than 1.",
                   "Check: 7 × 0.6 = 4.2, 0.7 × 0.6 = 0.42, 0.7 × 6 = 4.2 and 0.07 × 0.06 = 0.0042."],
                  "(b) and (d); the products are 4.2, 0.42, 4.2 and 0.0042", tool="product_size_predictor"),
          ])]))
