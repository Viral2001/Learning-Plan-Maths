# -*- coding: utf-8 -*-
"""Topics T5 to T7: the Rule of Three, changes that are not proportional, and comparing by unit price (M3).
Book pp 164 and 167 to 172."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T5 The Rule of Three ========================================================
TOPICS.append(TOPIC(
    "T5", "M3", "The Rule of Three", ["7.4"], "Apply",
    "Students set up a proportion a : b :: c : ? from three given quantities, find the fourth by the factor of "
    "change or by cross multiplication (ad = bc), convert units so both ratios use the same units, and connect the "
    "method to Aryabhata's Rule of Three.",
    "When four quantities are linked proportionally and three are known, write a : b :: c : d. Then ad = bc, so "
    "d = bc ÷ a. Both ratios must use the same units. Aryabhata called this the Rule of Three.",
    [A("T5.C1", "Three known, one to find: the mid-day meal", "Apply",
       "Students write the mid-day meal problem as 120 : 15 :: 80 : ?, find the factor of change 2/3 and the amount "
       "of rice, and recognise a problem with three given quantities and one to find.",
       textbook=["For the mid-day meal in a school with 120 students, the cook usually makes 15 kg of rice. On a rainy "
                 "day, only 80 students came to school. How many kilograms of rice should the cook make so that the "
                 "food is not wasted?",
                 "The ratio of the number of students to the amount of rice needs to be proportional.",
                 "So, 120 : 15 :: 80 : ?",
                 "What is the factor of change in the first term?",
                 "The number of students is reduced by a factor of 2/3.",
                 "On multiplying the weight of rice by the same factor, we get, 15 × 2/3 = 10.",
                 "So, the cook should make 10 kg of rice on that day.",
                 "The situation above is a typical example of a problem where we need to use proportional reasoning "
                 "to find a solution. Four quantities are linked proportionally, out of which three are known and we "
                 "must find the fourth, unknown, quantity."],
       teach=["Predict first: 120 students eat 15 kg of rice. Only 80 come today. More or less than 10 kg?",
              "Students and rice must stay in the same ratio, so write 120 : 15 :: 80 : ?",
              "Factor of change for the students: 80 ÷ 120 = 2/3.",
              "Multiply the rice by the same factor. Three quantities are known and one is found: the Rule of Three."],
       examples=[
           WE("A cook makes 15 kg of rice for 120 students. On a rainy day only 80 students come. How much rice "
              "should the cook make?",
              ["Students to rice: 120 : 15 :: 80 : ?",
               "Factor of change: 80 ÷ 120 = 2/3.",
               "Rice: 15 × 2/3 = 10.",
               "Check: 120 : 15 is 8 : 1 and 80 : 10 is 8 : 1."],
              "10 kg of rice",
              ncert=["7.4.ex8", "7.4.trairasika"])],
       key_terms=["Rule of Three", "factor of change"], misconceptions=["M_ADD_SAME"], minutes=7),
     A("T5.C2", "Cross multiplication, and Aryabhata's rule", "Understand",
       "Students derive ad = bc from a : b :: c : d using one factor f, find the fourth term as d = bc ÷ a, and match "
       "the terms to Aryabhata's pramana, phala, ichchha and ichchhaphala.",
       textbook=["To solve such problems, we can model two proportional ratios using algebraic notation as a : b :: "
                 "c : d.",
                 "For these two ratios to be proportional, we know that term c should be a multiple of term a by a "
                 "factor, say f, and term d should be a multiple of term b by the same factor f.",
                 "Thus, when a : b :: c : d, then ad = bc. This is known as cross multiplication of terms.",
                 "Two ratios are proportional if their terms are equal when cross multiplied. The fourth unknown "
                 "quantity can be found through such cross multiplication.",
                 "In ancient India, Aryabhata and others called such problems of proportionality Rule of Three "
                 "problems. There were 3 numbers given, the pramana (measure, 'a' in our case), the phala (fruit, "
                 "'b' in our case), and the ichchha (requisition, 'c' in our case).",
                 "To find the ichchhaphala (yield, 'd' in our case), Aryabhata says, \"Multiply the phala by the "
                 "ichchha and divide the resulting product by the pramana.\"",
                 "Using the cross multiplication method proposed by Aryabhata, ancient Indians solved complex "
                 "problems that involved proportionality."],
       teach=["Predict first: in 120 : 15 :: 80 : 10, is 120 × 10 equal to 15 × 80? Guess before multiplying.",
              "If c = f × a and d = f × b, then c/a = d/b, and multiplying both sides by ab gives ad = bc.",
              "So the fourth term is d = bc ÷ a.",
              "Aryabhata's words say the same: multiply the phala by the ichchha and divide by the pramana."],
       examples=[
           WE("Check by cross multiplication that 120 : 15 :: 80 : 10, then use Aryabhata's rule to find the "
              "fourth term of 120 : 15 :: 80 : ?",
              ["Outer terms: 120 × 10 = 1200.",
               "Inner terms: 15 × 80 = 1200, so ad = bc and the ratios are proportional.",
               "Pramana 120, phala 15, ichchha 80.",
               "Phala times ichchha: 15 × 80 = 1200; divide by the pramana: 1200 ÷ 120 = 10."],
              "ad = bc holds (1200 = 1200); the fourth term is 10",
              ncert=["7.4.cross_mult", "7.4.aryabhata"])],
       key_terms=["cross multiplication", "Rule of Three", "pramana", "phala", "ichchha"],
       minutes=8),
     A("T5.C2x", "Same units first: a car's distance", "Apply",
       "Students notice that minutes and hours cannot sit in one proportion, convert 4 hours to 240 minutes and find "
       "the distance by cross multiplication.",
       textbook=["A car travels 90 km in 150 minutes. If it continues at the same speed, what distance will it cover "
                 "in 4 hours?",
                 "150 : 90 :: 4 : ? Is this the right way to formulate the question?",
                 "No, because 150 is in minutes, but 4 is in hours. The second ratio should use the same units for "
                 "time as the first ratio. Since 4 hours is 240 minutes, the right form is 150 : 90 :: 240 : ?",
                 "By cross multiplication, we get 150 × x = 240 × 90.",
                 "The distance covered by the car in 4 hours is 144 km.",
                 "Note to the Teacher: Instead of giving one 'method' to solve the problem of the distance, "
                 "encourage students to reason out the answer through different strategies. They can use their "
                 "understanding of equivalent fractions and equivalent ratios to find the answer."],
       teach=["Predict first: is 150 : 90 :: 4 : ? the right proportion?",
              "Put both times in minutes before writing the proportion; then cross multiply."],
       examples=[
           WE("A car travels 90 km in 150 minutes. At the same speed, how far does it go in 4 hours?",
              ["4 hours is 4 × 60 = 240 minutes, so the proportion is 150 : 90 :: 240 : x.",
               "Cross multiply: 150 × x = 240 × 90.",
               "x = 240 × 90 ÷ 150",
               "240 × 90 ÷ 150 = 144."],
              "144 km",
              ncert=["7.4.ex9"])],
       ncert=["7.4.note_strategies"],
       key_terms=["same units", "cross multiplication"], misconceptions=["M_MIXED_UNITS"], minutes=5, thin=True),
     DOER("T5.C3", "Practice: use the Rule of Three", "double_line", "Apply",
          "Students find the fourth quantity from three given quantities by the factor of change or "
          "by cross multiplication, and convert units first when they differ.",
          ["Write the proportion a : b :: c : d with the same units in both ratios.",
           "Cross multiply: ad = bc, so d = bc ÷ a.",
           "Or find the factor of change from a to c and apply it to b."],
          items=[
              FIO("FiO2.q1", "Figure it Out (rule of three, question 1)",
                  "The Earth travels approximately 940 million kilometres around the Sun in a year. How many "
                  "kilometres will it travel in a week?",
                  ["A year has about 52 weeks.",
                   "Distance to weeks: 940000000 : 52 :: x : 1.",
                   "x = 940000000 ÷ 52",
                   "940000000 ÷ 52 ≈ 18076923."],
                  "About 18076923 km in a week"),
              FIO("FiO2.q2", "Figure it Out (rule of three, question 2)",
                  "A mason is building a house in the shape shown in the diagram, with walls of 12 ft, 15 ft, 9 ft, "
                  "9 ft and 6 ft and an inner wall that separates two rooms. To build a wall of 10 feet, he requires "
                  "approximately 1450 bricks. How many bricks would he need to build the house? Assume all walls are "
                  "of the same height and thickness.",
                  ["Add all the outer walls and the inner wall: 12 + 12 + 12 + 15 + 9 + 15 + 9 + 9 + 9 + 6 = 108 ft.",
                   "Wall length to bricks: 10 : 1450 :: 108 : x.",
                   "x = 1450 × 108 ÷ 10",
                   "1450 × 108 ÷ 10 = 15660."],
                  "About 15660 bricks"),
              FIO("7.4.act1", "Activity (cook a dish for 15 guests)",
                  "Take your favourite dish. Find out all the ingredients and their respective quantities needed to "
                  "make the dish for your family. Suppose you are celebrating a festival and you want to invite 15 "
                  "guests. Find out the quantities of the ingredients required to cook the same dish for them.",
                  ["List each ingredient for your family, for example 5 people: 2 cups of rice, 1 cup of dal.",
                   "Factor of change from 5 people to 15 guests: 15 ÷ 5 = 3.",
                   "Multiply every ingredient by the same factor: 2 × 3 = 6 cups of rice and 1 × 3 = 3 cups of dal.",
                   "Every ingredient must use the same factor, or the dish will taste different."],
                  "Multiply every ingredient by the same factor, guests ÷ family size"),
              FIO("FiO4.q2", "Figure it Out (unit conversions, question 2)",
                  "Last year, we hired 3 buses for the school trip. We had a total of 162 students and teachers who "
                  "went on that trip and all the buses were full. This year we have 204 students. How many buses "
                  "will we need? Will all the buses be full?",
                  ["Each bus holds 162 ÷ 3 = 54 people.",
                   "Buses needed: 204 ÷ 54 ≈ 3.78, so 3 buses are not enough and we need 4.",
                   "4 buses hold 4 × 54 = 216 people.",
                   "216 − 204 = 12 seats stay empty, so not all buses are full."],
                  "4 buses; they will not all be full (12 seats empty)"),
              FIO("FiO4.q5", "Figure it Out (unit conversions, question 5)",
                  "Let us try an ancient problem from Lilavati. At that time weights were measured in a unit named "
                  "palas and niskas was a unit of money. \"If 2.5 palas of saffron costs 3/7 niskas, O expert "
                  "businessman! tell me quickly what quantity of saffron can be bought for 9 niskas?\"",
                  ["Niskas to palas: 3/7 : 2.5 :: 9 : x.",
                   "Cross multiply: 3/7 × x = 2.5 × 9.",
                   "x = 2.5 × 9 × 7 ÷ 3",
                   "2.5 × 9 × 7 ÷ 3 = 52.5."],
                  "52.5 palas of saffron"),
              FIO("FiO4.q7", "Figure it Out (unit conversions, question 7)",
                  "The mass of equal volumes of gold and water are in the ratio 37 : 2. If 1 litre of water is 1 kg "
                  "in mass, what is the mass of 1 litre of gold?",
                  ["Gold to water is 37 : 2 :: x : 1.",
                   "Cross multiply: 2 × x = 37 × 1.",
                   "37 ÷ 2 = 18.5."],
                  "18.5 kg"),
              FIO("FiO4.q9", "Figure it Out (unit conversions, question 9)",
                  "A tap takes 15 seconds to fill a mug of water. The volume of the mug is 500 mL. How much time "
                  "does the same tap take to fill a bucket of water if the bucket has a 10 litre capacity?",
                  ["Same units: 10 litres is 10000 mL.",
                   "Factor of change: 10000 ÷ 500 = 20.",
                   "Time: 20 × 15 = 300 seconds.",
                   "300 ÷ 60 = 5 minutes."],
                  "300 seconds, which is 5 minutes")])],
    key_terms=["Rule of Three", "cross multiplication", "same units"]))

# ============================== T6 Not every change is proportional ========================================
TOPICS.append(TOPIC(
    "T6", "M3", "Not Every Change Is Proportional", ["7.4"], "Analyze",
    "Students show that adding the same number of years to two ages changes their ratio, and that time does not grow "
    "with speed, so the Rule of Three cannot be used without first checking that the quantities are proportional.",
    "Adding or subtracting the same number from both terms changes a ratio. Some quantities change together without "
    "being proportional: when speed goes up, travel time goes down. Check the relationship before using the Rule of "
    "Three.",
    [A("T6.C1", "Ages: adding years changes the ratio", "Analyze",
       "Students compare Neelima's age to her mother's age now and 9 years later and explain why adding the same "
       "number to both terms does not keep the ratio.",
       textbook=["When Neelima was 3 years old, her mother's age was 10 times her age. What is the ratio of Neelima's "
                 "age to her mother's age? What would be the ratio of their ages when Neelima is 12 years old? Would "
                 "it remain the same?",
                 "The ratio of Neelima's age to her mother's age when Neelima is 3 years old is 3 : 30 (her mother's "
                 "age is 10 times Neelima's age). In the simplest form, it is 1 : 10.",
                 "When Neelima is 12 years old (i.e., 9 years later), the ratio of their ages will be 12 : 39 (9 "
                 "years later, her mother would be 39 years old). In the simplest form, it is 4 : 13.",
                 "When we add (or subtract) the same number from the terms of a ratio, the ratio changes and is not "
                 "necessarily proportional to the original ratio."],
       teach=["Predict first: Neelima's mother is 10 times as old as Neelima. Will she still be 10 times as old "
              "in 9 years?",
              "Both ages grow by the same number of years, which is adding, not multiplying.",
              "3 : 30 is 1 : 10, but 12 : 39 is 4 : 13.",
              "Adding the same number to both terms changes the ratio."],
       examples=[
           WE("Neelima is 3 and her mother is 10 times as old. What is the ratio of their ages now, and when Neelima "
              "is 12?",
              ["Mother's age now: 3 × 10 = 30, so the ratio is 3 : 30, which is 1 : 10.",
               "Neelima is 12 after 12 − 3 = 9 years; her mother is then 30 + 9 = 39.",
               "The ratio becomes 12 : 39; the HCF is 3, so it is 4 : 13.",
               "1 : 10 and 4 : 13 are different, so the ratio did not stay the same."],
              "1 : 10 now and 4 : 13 when Neelima is 12; the ratio changes",
              ncert=["7.4.ex6"])],
       key_terms=["ratio", "adding the same number"], misconceptions=["M_ADD_SAME"], minutes=7),
     A("T6.C2", "Faster speed, less time", "Analyze",
       "Students test whether 50 : 2 :: 75 : ? models a faster journey, reason that more speed means less time, and "
       "find the actual time from the distance.",
       textbook=["Puneeth's father went from Lucknow to Kanpur in 2 hours by riding his motorcycle at a speed of "
                 "50 km/h. If he drives at 75 km/h, how long will it take him to reach Kanpur? Can we form this "
                 "problem as a proportion, 50 : 2 :: 75 : __",
                 "Would it take Puneeth's father more time or less time to reach Kanpur? Think about it.",
                 "Even though this problem looks similar to the previous problems, it cannot be solved using the "
                 "Rule of Three!",
                 "The time of travel would actually decrease when the speed increases. So this problem cannot be "
                 "modelled as 50 : 2 :: 75 : __."],
       teach=["Predict first: riding faster, will the trip take more than 2 hours or less?",
              "50 : 2 :: 75 : ? would give 3 hours, more time at a faster speed, which cannot be right.",
              "Speed and time do not grow together, so the Rule of Three does not fit.",
              "Use the distance instead: it stays the same, so time is distance ÷ speed."],
       examples=[
           WE("Puneeth's father rides from Lucknow to Kanpur in 2 hours at 50 km/h. How long does the trip take at "
              "75 km/h?",
              ["The Rule of Three would give 2 × 75 ÷ 50 = 3 hours, more time at a higher speed, so it is wrong.",
               "The distance stays the same: 50 × 2 = 100 km.",
               "Time at 75 km/h: 100 ÷ 75 = 4/3 hours.",
               "4/3 hours is 1 hour and 20 minutes, less than 2 hours."],
              "1 hour 20 minutes; speed and time are not proportional, so the Rule of Three does not apply",
              ncert=["7.4.puneeth"])],
       key_terms=["speed", "not proportional"], misconceptions=["M_ALWAYS_PROPORTIONAL"], minutes=7),
     DOER("T6.C3", "Practice: multiplying change or adding change?", "add_mult_judge", "Analyze",
          "Students judge whether each change is multiplicative or additive before solving, and use the Rule of "
          "Three only when the quantities are proportional.",
          ["Adding the same number to both terms changes a ratio.",
           "Some quantities change together without being proportional.",
           "Check the relationship first; use the Rule of Three only for proportional quantities."],
          items=[
              FIO("FiO4.q6", "Figure it Out (unit conversions, question 6)",
                  "Harmain is a 1 year old girl. Her elder brother is 5 years old. What will be Harmain's age when "
                  "the ratio of her age to her brother's age is 1 : 2?",
                  ["The brother is always 5 − 1 = 4 years older, an additive change.",
                   "Let Harmain be x years old; her brother is x + 4 and we need x : (x + 4) = 1 : 2.",
                   "Cross multiply: 2x = x + 4, so x = 4.",
                   "Check: 4 : 8 is 1 : 2."],
                  "Harmain will be 4 years old"),
              FIO("FiO4.q11", "Figure it Out (unit conversions, question 11)",
                  "A tractor can plough the same area of a field 4 times faster than a pair of oxen. A farmer wants "
                  "to plough his 20 acre field. A pair of oxen takes 6 hours to plough an acre of land. How much time "
                  "would it take if the farmer used a pair of oxen to plough the field? How much time would it take "
                  "him if he decides to use a tractor instead?",
                  ["Oxen: area and time are proportional, so 20 × 6 = 120 hours.",
                   "A tractor 4 times faster takes less time, not more: 6 ÷ 4 = 1.5 hours for one acre.",
                   "Tractor for the field: 20 × 1.5 = 30 hours.",
                   "Check: 120 ÷ 4 = 30."],
                  "120 hours with oxen and 30 hours with a tractor")])],
    key_terms=["not proportional", "additive change", "multiplicative change"]))

# ============================== T7 Comparing by unit price ==================================================
TOPICS.append(TOPIC(
    "T7", "M3", "Comparing by Unit Price", ["7.4"], "Evaluate",
    "Students convert weights to the same unit, test whether weight and price are proportional, compare the price "
    "of the same amount (one kilogram or one millilitre) to decide which is more expensive, and discuss the pros "
    "and cons of different pack sizes.",
    "To compare prices of different packs, use the same unit and find the price for the same amount. Prices are often "
    "not proportional to amounts, so a bigger or a smaller pack is not automatically the better buy.",
    [A("T7.C1", "Which tea is more expensive?", "Evaluate",
       "Students write weight to price ratios for two teas in the same unit, see that they are not proportional, and "
       "decide which tea is more expensive by finding the price of 1 kg of each.",
       textbook=["A small farmer in Himachal Pradesh sells each 200 g packet of tea for ₹200. A large estate in "
                 "Meghalaya sells each 1 kg packet of tea for ₹800. Are the weight to price ratios in both places "
                 "proportional? Which tea is more expensive?",
                 "The ratio of weight to price of the Himachal tea is 200 : 200.",
                 "What is the weight to price ratio of the Meghalaya tea? Is it 1 : 800? This would not be "
                 "appropriate, because we considered the weight in grams in the case of Himachal. So, the weight to "
                 "price ratio is 1000 : 800 in Meghalaya after we convert the weight to grams.",
                 "The Himachal tea ratio in its simplest form is 1 : 1. The Meghalaya tea ratio in its simplest form "
                 "is 5 : 4. So, the ratios are not proportional.",
                 "To answer the question as to which tea is more expensive, we should compare the price of tea for "
                 "the same weight in both places.",
                 "So, the cost of 1 kg of tea is ₹800 in Meghalaya and ₹1,000 in Himachal Pradesh. Therefore, the tea "
                 "from Himachal Pradesh is more expensive.",
                 "Note to the Teacher: Encourage a discussion on the more expensive tea, how they came to their "
                 "conclusions and what the reasons for that tea being more expensive could be."],
       teach=["Predict first: a ₹200 packet or a ₹800 packet. Is the ₹800 tea the more expensive one?",
              "Use the same unit for weight: 1 kg is 1000 g.",
              "200 : 200 is 1 : 1 but 1000 : 800 is 5 : 4, so price is not proportional to weight here.",
              "Compare the price of the same weight, 1 kg of each."],
       examples=[
           WE("Himachal tea costs ₹200 for 200 g. Meghalaya tea costs ₹800 for 1 kg. Which tea is more expensive?",
              ["Same unit: 1 kg is 1000 g, so the ratios are 200 : 200 and 1000 : 800.",
               "Simplest forms: 1 : 1 and 5 : 4, so they are not proportional.",
               "200 g is 1/5 of 1 kg, so 1 kg of Himachal tea costs 200 × 5 = 1000 rupees.",
               "1 kg of Meghalaya tea costs 800 rupees, and 1000 is more than 800."],
              "Himachal tea is more expensive: ₹1000 a kg against ₹800 a kg",
              ncert=["7.4.ex10"])],
       ncert=["7.4.note_tea"],
       key_terms=["unit price", "same unit"], misconceptions=["M_BIGGER_COSTS_MORE", "M_MIXED_UNITS"], minutes=8),
     A("T7.C2", "Shampoo sizes: is price proportional to volume?", "Evaluate",
       "Students compare the price of one millilitre of shampoo in four container sizes, find that price is not "
       "proportional to volume, and discuss the pros and cons of each size, including the ecological footprint.",
       textbook=["Go to the market and collect the prices of different sizes of shampoo containers of the same "
                 "shampoo and create a table like the one given below. See if the volume of shampoo is proportional "
                 "to the price.",
                 "Sachet: 6 mL, ₹2. Small Bottle: 180 mL, ₹154. Medium Bottle: 340 mL, ₹276. Large Bottle: 1000 mL, "
                 "₹540.",
                 "The ratio of the volume of a sachet to a small bottle is 6 : 180. The ratio of their prices is "
                 "2 : 154. Are these ratios proportional?",
                 "Why do you think that the ratio of the prices is not proportional to the ratio of the volumes?",
                 "Discuss the pros and cons of different size bottles for the company and for customers. For "
                 "reducing ecological footprint, what would you recommend to the company and to the customer?",
                 "Does the same occur for other products? Make similar tables for other products in the market, "
                 "capturing different prices for different measures of the same product, e.g., rice or atta (flour).",
                 "Note to the Teacher: Give a project to students. Start by dividing the class into groups. Each "
                 "group should go to one shop and collect prices for different measures of the same product."],
       teach=["Predict first: the large bottle costs the most. Is it the most expensive way to buy shampoo?",
              "Find the price of one millilitre for each size: price ÷ volume.",
              "Volumes 6 : 180 is 1 : 30 but prices 2 : 154 is 1 : 77, so price is not proportional to volume.",
              "Here the sachet is cheapest per mL and the small bottle dearest; the sachet's cost is plastic waste."],
       examples=[
           WE("A sachet of 6 mL costs ₹2, a 180 mL bottle ₹154, a 340 mL bottle ₹276 and a 1000 mL bottle ₹540. "
              "Which size gives the cheapest shampoo per mL?",
              ["Sachet: 2 ÷ 6 ≈ 0.33 rupees per mL.",
               "Small bottle: 154 ÷ 180 ≈ 0.86 rupees per mL; medium: 276 ÷ 340 ≈ 0.81.",
               "Large bottle: 540 ÷ 1000 = 0.54 rupees per mL.",
               "Volumes 6 : 180 is 1 : 30 but prices 2 : 154 is 1 : 77, so they are not proportional."],
              "The sachet is cheapest per mL here (about ₹0.33), then the large bottle (₹0.54); price is not "
              "proportional to volume",
              ncert=["7.4.act2", "7.4.act2_eco"])],
       ncert=["7.4.note_project"],
       key_terms=["unit price", "not proportional"], misconceptions=["M_BIGGER_COSTS_MORE"], minutes=8),
     DOER("T7.C3", "Practice: compare by the rate for one unit", "unit_rate", "Evaluate",
          "Students compare two offers or places by finding the amount for one unit, such as the price of 1 kg or "
          "the number of people in 1 sq. km.",
          ["Use the same units on both sides.",
           "Divide to get the amount for one unit, then compare.",
           "A bigger total does not mean a bigger rate."],
          items=[
              FIO("FiO4.q3", "Figure it Out (unit conversions, question 3)",
                  "The area of Delhi is 1484 sq. km and the area of Mumbai is 550 sq. km. The population of Delhi is "
                  "approximately 30 million and that of Mumbai is 20 million people. Which city is more crowded? Why "
                  "do you say so?",
                  ["Compare people for each sq. km, not the totals.",
                   "Delhi: 30000000 ÷ 1484 ≈ 20216 people per sq. km.",
                   "Mumbai: 20000000 ÷ 550 ≈ 36364 people per sq. km.",
                   "36364 is more than 20216, so Mumbai has more people in each sq. km."],
                  "Mumbai is more crowded: about 36364 people per sq. km against about 20216 in Delhi")])],
    key_terms=["unit price", "unit rate"]))
