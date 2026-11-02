# -*- coding: utf-8 -*-
"""Topics T12 to T17 (modules M5 and M6): multiplication shortcut, length of a product, large-number facts,
Did You Ever Wonder, the toothpick digit puzzle, and the summary."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T12 A multiplication shortcut ================================================
TOPICS.append(TOPIC(
    "T12", "M5", "A Multiplication Shortcut", ["1.5"], "Apply",
    "Students multiply by 5 or 25 by dividing and multiplying by 10 or 100, explain why halving then multiplying by "
    "ten gives the same answer, and regroup factors to make products such as 125 times 8 simple.",
    "Multiplying by 5 is dividing by 2 and multiplying by 10; regrouping factors into tens, hundreds and thousands "
    "makes large products quick.",
    [A("T12.C1", "Two quick ways to multiply", "Apply",
       "Students multiply 116 by 5 by multiplying by 10 and halving, and multiply 824 by 25 by multiplying by 100 and "
       "dividing by 4.",
       textbook=["1.5 Patterns in Products",
                 "Roxie and Estu are playing with multiplication. They encounter an interesting technique for "
                 "multiplying a number by 10, 100, 1000, and so on.",
                 "A Multiplication Shortcut",
                 "Roxie evaluated 116 × 5 as follows: 116 × 5 = (116 × 10) ÷ 2 = 1160 ÷ 2 = 580.",
                 "Estu evaluated 824 × 25 as follows: 824 × 25 = (824 × 100) ÷ 4 = 82,400 ÷ 4 = 20,600."],
       teach=["Predict first: is 116 × 5 half of 116 × 10, or twice it?",
              "5 is 10 ÷ 2, so multiplying by 5 is multiplying by 10 and then halving.",
              "25 is 100 ÷ 4, so multiplying by 25 is multiplying by 100 and then dividing by 4."],
       examples=[
           WE("Roxie finds 116 × 5 by multiplying by 10 and halving. Estu finds 824 × 25 by multiplying by 100 and "
              "dividing by 4. Do both.",
              ["116 × 10 = 1160.", "1160 ÷ 2 = 580, so 116 × 5 = 580.", "824 × 100 = 82,400.",
               "82,400 ÷ 4 = 20,600, so 824 × 25 = 20,600."],
              "116 × 5 = 580 and 824 × 25 = 20,600", ncert=["1.5.shortcut_roxie", "1.5.shortcut_estu"])],
       key_terms=["shortcut", "halve"], misconceptions=["M_SHORTCUT_ORDER"], minutes=6),
     A("T12.C2", "Why times five is halve then times ten", "Understand",
       "Students explain using the meaning of multiplication and division why multiplying by 5 matches multiplying by "
       "10 and dividing by 2.",
       textbook=["Using the meaning of multiplication and division, can you explain why multiplying by 5 is the same "
                 "as dividing by 2 and multiplying by 10?"],
       teach=["Predict first: 8 × 5 is how many groups of 5? How does that compare with 8 × 10?",
              "Ten in each group is twice as many as five in each group, so 8 × 5 is half of 8 × 10.",
              "Dividing by 2 and multiplying by 10 scales by 10 ÷ 2, which is 5."],
       examples=[
           WE("Explain why a number times 5 is the number times 10 divided by 2, using 8 × 5.",
              ["8 × 10 means 8 groups of 10, which is 80.", "5 is half of 10, so each group has half as many.",
               "So 8 × 5 is half of 80, which is 40.", "In general, 5 = 10 ÷ 2, so n × 5 = (n × 10) ÷ 2.",
               "Dividing first also works: (8 ÷ 2) × 10 = 40."],
              "5 = 10 ÷ 2, so times 5 is times 10 then halve, e.g. 8 × 5 = 40", ncert=["1.5.why_five"])],
       key_terms=["multiplication", "division"], misconceptions=["M_SHORTCUT_ORDER"], minutes=6),
     DOER("T12.C3", "Practice: halve, double and regroup", "halve_double", "Apply",
          "Students regroup the factors of a product into tens, hundreds and thousands by halving and doubling, and use "
          "the regrouping to find products quickly.",
          ["Halve one factor and double another to keep the product the same.",
           "Pair factors that make 10, 100 or 1000.",
           "Multiply by the power of ten last."],
          items=[
              FIO("1.5.FiO_1", "Figure it Out, Q1 (quick products)",
                  "Find quick ways to calculate these products: (a) 2 × 1768 × 50 (b) 72 × 125 [Hint: 125 = "
                  "1000 ÷ 8] (c) 125 × 40 × 8 × 25",
                  ["(a) Pair 2 and 50 to make 100. Then 1768 × 100 = 1,76,800.",
                   "(b) 125 is 1000 ÷ 8. So 72 × 125 = (72 × 1000) ÷ 8. 72,000 ÷ 8 = 9000.",
                   "(c) Pair 125 with 8 to make 1000, and 40 with 25 to make 1000. Then 1000 × 1000 = 10,00,000."],
                  "(a) 1,76,800 (b) 9000 (c) 10,00,000", tool="halve_double"),
              FIO("1.5.FiO_2", "Figure it Out, Q2 (calculate quickly)",
                  "Calculate these products quickly. (a) 25 × 12 (b) 25 × 240 (c) 250 × 120 (d) 2500 × 12 "
                  "(e) ____ × ____ = 120000000",
                  ["(a) 25 × 12: 4 × 25 = 100, and 12 is 3 × 4, so 25 × 12 = 100 × 3 = 300.",
                   "(b) 25 × 240: 240 is 10 × 24, and 25 × 24 = 600, so the product is 6000.",
                   "(c) 250 × 120 = (25 × 12) × 100 = 300 × 100 = 30,000.",
                   "(d) 2500 × 12 = (25 × 12) × 100 = 300 × 100 = 30,000.",
                   "(e) Many answers work. One pair: 1200 × 1,00,000 = 12,00,00,000. Another pair: 12,000 × 10,000 = "
                   "12,00,00,000."],
                  "(a) 300 (b) 6000 (c) 30,000 (d) 30,000 (e) for example 1200 and 1,00,000", tool="halve_double")],
          ncert=["1.5.FiO_1", "1.5.FiO_2"], misconceptions=["M_SHORTCUT_ORDER"])]))

# ============================== T13 How long is the product ==================================================
TOPICS.append(TOPIC(
    "T13", "M5", "How Long is the Product?", ["1.5"], "Analyze",
    "Students extend multiplication patterns, test a claim about the number of digits in a product by using the "
    "smallest and largest numbers, and state how many digits the product of an m-digit and an n-digit number can "
    "have.",
    "The product of an m-digit and an n-digit number has m plus n digits or one fewer; the smallest and largest "
    "numbers show why.",
    [A("T13.C1", "Patterns in products", "Analyze",
       "Students evaluate three boxes of multiplications, spot the pattern in each box, and extend each pattern to a "
       "larger multiplication.",
       textbook=["How Long is the Product?",
                 "In each of the following boxes, the multiplications produce interesting patterns. Evaluate them to "
                 "find the pattern. Extend the multiplications based on the observed pattern.",
                 "Box one: 11 × 11, 111 × 111, 1111 × 1111.",
                 "Box two: 66 × 61, 666 × 661, 6666 × 6661.",
                 "Box three: 3 × 5, 33 × 35, 333 × 335.",
                 "Box four: 101 × 101, 102 × 102, 103 × 103."],
       teach=["Predict first: 11 × 11 is 121. What will 111 × 111 look like?",
              "Work each product, then look at how the answer grows when one more digit is added to the numbers.",
              "Use the pattern to jump to a longer multiplication, then check one of them with the usual method."],
       examples=[
           WE("Evaluate the four boxes and extend each pattern: 11 × 11, 111 × 111, 1111 × 1111; 66 × 61, 666 × 661, "
              "6666 × 6661; 3 × 5, 33 × 35, 333 × 335; 101 × 101, 102 × 102, 103 × 103.",
              ["11 × 11 = 121, 111 × 111 = 12,321 and 1111 × 1111 = 12,34,321. The digits climb and then fall back. "
               "So 11111 × 11111 = 12,34,54,321 in this pattern.",
               "66 × 61 = 4026, 666 × 661 = 4,40,226 and 6666 × 6661 = 4,44,02,226. A run of 4s, then 0, then a run of "
               "2s, then 6. So 66666 × 66661 = 4,44,40,22,226.",
               "3 × 5 = 15, 33 × 35 = 1155 and 333 × 335 = 1,11,555. A run of 1s then a run of 5s. So 3333 × 3335 = "
               "1,11,15,555.",
               "101 × 101 = 10,201, 102 × 102 = 10,404 and 103 × 103 = 10,609. So 104 × 104 = 10,816."],
              "Next in each box: 12,34,54,321; 4,44,40,22,226; 1,11,15,555; 10,816", ncert=["1.5.patterns"])],
       key_terms=["pattern", "extend"], misconceptions=["M_DIGIT_PRODUCT"], minutes=10),
     A("T13.C2", "Roxie's claim about 2-digit numbers", "Evaluate",
       "Students test Roxie's claim that two 2-digit numbers give a product of 3 or 4 digits by using the smallest and "
       "largest numbers, and decide whether two 3-digit numbers give 4 digits and whether 4-digit and 2-digit numbers give 5.",
       textbook=["Observe the number of digits in the two numbers being multiplied and their product in each case. Is "
                 "there any connection between the numbers being multiplied and the number of digits in their "
                 "product?",
                 "Roxie says that the product of two 2-digit numbers can only be a 3- or a 4-digit number. Is she "
                 "correct?",
                 "Should we try all possible multiplications with 2-digit numbers to tell whether Roxie's claim is "
                 "true? Or is there a better way to find out?",
                 "She explains her reasoning: \"We want to know about the number of digits in the product of two "
                 "2-digit numbers. To know the smallest such product I took 10 × 10, so all other products will be "
                 "greater than 100. To know the greatest such product I multiplied the smallest 3-digit numbers "
                 "(100 × 100) to get 10,000; so the product of all the 2-digit multiplications will be less than "
                 "10,000.\"",
                 "Can multiplying a 3-digit number with another 3-digit number give a 4-digit number?",
                 "Can multiplying a 4-digit number with a 2-digit number give a 5-digit number?"],
       teach=["Predict first: is the largest product of two 2-digit numbers, 99 × 99, below 10,000?",
              "The smallest product comes from the smallest numbers and the largest product from the largest numbers, "
              "so two checks cover every case.",
              "Check the smallest and the largest products for each pair of digit counts."],
       examples=[
           WE("Is Roxie right that two 2-digit numbers give a 3-digit or 4-digit product? Can two 3-digit numbers give a "
              "4-digit product? Can a 4-digit number times a 2-digit number give a 5-digit product?",
              ["Smallest: 10 × 10 = 100, which has 3 digits.", "Largest: 99 × 99 = 9801, which has 4 digits.",
               "Every other product lies between them, so Roxie is right.",
               "Two 3-digit numbers: the smallest is 100 × 100 = 10,000, which already has 5 digits. So never 4 digits.",
               "A 4-digit and a 2-digit number: the smallest is 1000 × 10 = 10,000, which has 5 digits, so yes.",
               "The largest is 9999 × 99 = 9,89,901, which has 6 digits."],
              "Roxie is right; two 3-digit numbers never give 4 digits; a 4-digit times a 2-digit number can give 5 "
              "digits (or 6)", ncert=["1.5.roxie_claim", "1.5.three_by_three", "1.5.four_by_two"])],
       key_terms=["smallest product", "largest product"], misconceptions=["M_DIGIT_PRODUCT"], minutes=10),
     A("T13.C3", "The digit-count rule", "Analyze",
       "Students read the table of digit counts, state that an m-digit number times an n-digit number has m plus n or "
       "m plus n minus one digits, and apply it to three new pairs.",
       textbook=["Observe the multiplication statements below. Do you notice any patterns? See if this pattern "
                 "extends for other numbers as well.",
                 "A 1-digit number times a 1-digit number gives a 1-digit or 2-digit number.",
                 "A 2-digit number times a 1-digit number gives a 2-digit or 3-digit number.",
                 "A 2-digit number times a 2-digit number gives a 3-digit or 4-digit number.",
                 "A 3-digit number times a 3-digit number gives a 5-digit or 6-digit number.",
                 "A 5-digit number times a 5-digit number gives a ___-digit or ___-digit number.",
                 "An 8-digit number times a 3-digit number gives a ___-digit or ___-digit number.",
                 "A 12-digit number times a 13-digit number gives a ___-digit or ___-digit number."],
       teach=["Predict first: a 2-digit times a 2-digit gives 3 or 4 digits. What is 2 + 2, and what is one fewer?",
              "The smallest m-digit number is 1 followed by m − 1 zeros, and the smallest product is 1 followed by "
              "m + n − 2 zeros, which has m + n − 1 digits.",
              "The largest product is below the smallest (m + n)-digit number, so the product has at most m + n "
              "digits."],
       examples=[
           WE("Fill in the table: 5-digit times 5-digit, 8-digit times 3-digit, and 12-digit times 13-digit. State the "
              "rule.",
              ["For a 1-digit number times a 1-digit number the counts are 1 and 2: 1 + 1 − 1 = 1 and 1 + 1 = 2.",
               "A 5-digit number times a 5-digit number gives 5 + 5 − 1 = 9 or 5 + 5 = 10 digits.",
               "An 8-digit number times a 3-digit number gives 8 + 3 − 1 = 10 or 8 + 3 = 11 digits.",
               "A 12-digit number times a 13-digit number gives 12 + 13 − 1 = 24 or 12 + 13 = 25 digits.",
               "Rule: an m-digit number times an n-digit number has m + n − 1 or m + n digits."],
              "9 or 10; 10 or 11; 24 or 25 digits. The rule is m + n − 1 or m + n digits",
              ncert=["1.5.digit_rule", "1.5.digit_5_5", "1.5.digit_8_3", "1.5.digit_12_13"])],
       key_terms=["digits", "rule"], misconceptions=["M_DIGIT_PRODUCT"], minutes=10),
     DOER("T13.C4", "Practice: predict the digits of a product", "digit_count_predictor", "Apply",
          "Students predict the number of digits in a product from the digit counts of the two numbers, check the "
          "prediction with the smallest and the largest numbers, and decide when each count can occur.",
          ["Add the digit counts of the two numbers.",
           "The product has that many digits or one fewer.",
           "Check with the smallest and largest numbers of those lengths."])]))

# ============================== T14 Fascinating facts ========================================================
TOPICS.append(TOPIC(
    "T14", "M5", "Fascinating Facts about Large Numbers", ["1.5"], "Apply",
    "Students multiply and divide large numbers to uncover facts, read each result in the Indian and the American "
    "naming systems, and raise questions about the fact.",
    "Large products and quotients reveal real facts; each answer can be named in the Indian and the American system.",
    [A("T14.C1", "Facts hidden in products", "Apply",
       "Students multiply 1250 by 380, 2100 by 70,000 and 6400 by 62,500, and read each product in the Indian and the "
       "American naming systems.",
       textbook=["Fascinating Facts about Large Numbers",
                 "Some interesting facts about large numbers are hidden below. Calculate the product or quotient to "
                 "uncover the facts. Once you find the product or quotient, read the number in both Indian and "
                 "American naming systems. Share your thoughts and questions about the fact with the class after you "
                 "discover each number.",
                 "1250 × 380 is the number of kirtanas composed by Purandaradasa according to legends. Purandaradasa "
                 "was a composer and singer in the 15th century. His kirtanas spanned social reform, bhakti and "
                 "spirituality. He systematised methods for teaching Carnatic music which is followed to the present "
                 "day. How many years did he live to compose so many songs? At what age did he start composing "
                 "songs? If he composed 4,75,000 songs, how many songs per year did he have to compose?",
                 "2100 × 70,000 is the approximate distance in kilometres between the Earth and the Sun. This "
                 "distance keeps varying throughout the year. The farthest distance is about 152 million kilometres. "
                 "How did they measure the distance between the Earth and the Sun?",
                 "6400 × 62,500 is the average number of litres of water the Amazon river discharges into the "
                 "Atlantic Ocean every second. The river's flow into the Atlantic is so much that drinkable "
                 "freshwater is found even 160 kilometres into the open sea."],
       teach=["Predict first: 1250 × 380 is about 1000 × 400. Is the answer nearer to four lakh or to four crore?",
              "Multiply the non-zero parts, then count the zeros that were left out.",
              "Name each answer twice: in the Indian system with lakh and crore, and in the American system with "
              "thousand and million."],
       examples=[
           WE("Find 1250 × 380, 2100 × 70,000 and 6400 × 62,500, and name each in both systems.",
              ["1250 × 380 = 4,75,000: four lakh seventy five thousand in the Indian system, and four hundred seventy "
               "five thousand in the American system.",
               "2100 × 70,000 = 14,70,00,000: fourteen crore seventy lakh, or one hundred forty seven million.",
               "6400 × 62,500 = 40,00,00,000: forty crore, or four hundred million.",
               "To ask how long Purandaradasa composed, suppose he composed for 50 years. Then 4,75,000 ÷ 50 = 9,500 "
               "songs a year.",
               "The Earth to Sun distance is about 14,70,00,000 km, which is about 147 million km."],
              "4,75,000; 14,70,00,000; 40,00,00,000 (named in both systems above)",
              ncert=["1.5.fact_songs", "1.5.fact_sun", "1.5.fact_amazon"])],
       key_terms=["product", "Indian system", "American system"], misconceptions=["M_COMPARE_UNITS"], minutes=10),
     A("T14.C2", "Facts hidden in quotients", "Apply",
       "Students divide 13,95,000 by 150, 10,50,00,000 by 700 and 52,00,00,00,000 by 130, read each quotient in both "
       "systems, and read the soil fact with million and billion.",
       textbook=["As you did before, divide the given numbers to uncover interesting facts about division. Share your "
                 "thoughts and questions with the class after you uncover each number.",
                 "13,95,000 ÷ 150 is the distance (in kms) of the longest single-train journey in the world. The "
                 "train runs in Russia between Moscow and Vladivostok. The duration of this journey is about 7 days. "
                 "The longest train route in India is from Dibrugarh in Assam to Kanyakumari in Tamil Nadu; it covers "
                 "4219 kms in about 76 hours.",
                 "Adult blue whales can weigh more than 10,50,00,000 ÷ 700 kilograms. A newborn blue whale weighs "
                 "around 2,700 kg, which is similar to the weight of an adult hippopotamus. Blue whales can eat up to "
                 "3500 kg of krill every day.",
                 "52,00,00,00,000 ÷ 130 was the weight, in tonnes, of global plastic waste generated in the year "
                 "2021.",
                 "Large Number Fact: In a single gram of healthy soil there can be 100 million to 1 billion bacteria "
                 "and 1 lakh to 1 million fungi, which can support plants' growth and health.",
                 "Share such large-number facts you know / come across with your class."],
       teach=["Predict first: 13,95,000 ÷ 150 is about 14,00,000 ÷ 150. Is the answer in thousands or lakhs?",
              "Cancel zeros from both numbers before dividing.",
              "Name each quotient in both systems, then read the soil fact with million and billion."],
       examples=[
           WE("Find 13,95,000 ÷ 150, 10,50,00,000 ÷ 700 and 52,00,00,00,000 ÷ 130, and name each in both systems.",
              ["13,95,000 ÷ 150 = 9,300: nine thousand three hundred in both systems.",
               "10,50,00,000 ÷ 700 = 1,50,000: one lakh fifty thousand, or one hundred fifty thousand.",
               "52,00,00,00,000 ÷ 130 = 40,00,00,000: forty crore, or four hundred million.",
               "In a gram of soil, 100 million to 1 billion bacteria and 1 lakh to 1 million fungi: 1 million is "
               "10 lakh, so the fungi are 1 lakh to 10 lakh."],
              "9,300; 1,50,000; 40,00,00,000 (named in both systems above)",
              ncert=["1.5.fact_train", "1.5.fact_whale", "1.5.fact_plastic", "1.5.fact_soil"])],
       key_terms=["quotient", "million", "billion"], misconceptions=["M_COMPARE_UNITS"], minutes=10),
     DOER("T14.C3", "Practice: find and share a large number fact", None, "Apply",
          "Students multiply or divide to uncover a large number fact, read the result in both systems, and ask a "
          "question about it.",
          ["Remove common zeros before dividing.",
           "Name the answer in the Indian and the American system.",
           "Ask how, why or how long for the fact."])]))

# ============================== T15 Did you ever wonder ======================================================
F6_Q = [
    ("1.6.FiO_1", "Figure it Out, Q1 (ten digits once each)",
     "Using all digits from 0 to 9 exactly once (the first digit cannot be 0) to create a 10-digit number, write the "
     "(a) largest multiple of 5 (b) smallest even number.",
     ["A multiple of 5 ends in 0 or 5. For the largest, put the digits in the biggest order, which ends with 0: "
      "9876543210.",
      "An even number ends in an even digit. The smallest start is 1, then 0, then the other digits in order.",
      "That order is 1023456789, but it ends in 9, which is odd.",
      "Swap the last two digits to end with 8: 1023456798. This is the smallest even number."],
     "(a) 9876543210 (b) 1023456798"),
    ("1.6.FiO_2", "Figure it Out, Q2 (the longest name)",
     "The number 10,30,285 in words is Ten lakhs thirty thousand two hundred eighty five, which has 42 letters. Give a "
     "7-digit number name which has the maximum number of letters.",
     ["Use the same style of naming as the book, with the plural in ten lakhs.",
      "Choose the lakh digits, the thousand digits and the last three digits so that each part has a long word.",
      "Seventy seven lakhs seventy seven thousand seven hundred seventy seven is 77,77,777. It has 61 letters.",
      "Checking all 7-digit numbers by computer gives 61 as the maximum, reached by 81 numbers; 73,73,373 is the "
      "smallest of them."],
     "The largest number of letters is 61, for example 77,77,777"),
    ("1.6.FiO_3", "Figure it Out, Q3 (swap and get bigger)",
     "Write a 9-digit number where exchanging any two digits results in a bigger number. How many such numbers "
     "exist?",
     ["Exchanging two digits makes the number bigger only if the smaller digit is on the left.",
      "So every digit must be smaller than all the digits to its right: the digits increase from left to right.",
      "The digits must be different, and zero cannot lead. The only choice is the nine digits 1 to 9 in increasing "
      "order.",
      "So the number is 1,23,45,67,89 and it is the only one."],
     "1,23,45,67,89; exactly one such number"),
    ("1.6.FiO_4", "Figure it Out, Q4 (strike out ten digits)",
     "Strike out 10 digits from the number 12345123451234512345 so that the remaining number is as large as possible.",
     ["The number has 20 digits, so 10 digits remain.",
      "Put the largest digit first. Strike out the four digits 1, 2, 3, 4 in front of the first 5.",
      "Strike out the next four digits 1, 2, 3, 4 so that a second 5 follows. That is 8 digits struck.",
      "Two strikes remain. Strike out the next 1 and 2 so that 3 comes next.",
      "What remains is 5534512345."],
     "5534512345"),
    ("1.6.FiO_5", "Figure it Out, Q5 (letters shared by number names)",
     "The words 'zero' and 'one' share letters 'e' and 'o'. The words 'one' and 'two' share a letter 'o', and the "
     "words 'two' and 'three' also share a letter 't'. How far do you have to count to find two numbers, one after "
     "the other, which do not share an English letter in common?",
     ["Write each number name and compare it with the next one.",
      "Names like nineteen and twenty share n, t and e. Ninety nine and one hundred share n and e.",
      "Checking every pair of neighbours up to three million, in the Indian and the international spelling, finds "
      "no pair without a shared letter.",
      "So there may be no such pair at all; the search turns up none."],
     "No such pair was found, however far we count"),
    ("1.6.FiO_6", "Figure it Out, Q6 (digits written one after the other)",
     "Suppose you write down all the numbers 1, 2, 3, 4, ..., 9, 10, 11, ... The tenth digit you write is '1' and the "
     "eleventh digit is '0', as part of the number 10. (a) What would the 1000th digit be? At which number would it "
     "occur? (b) What number would contain the millionth digit? (c) When would you have written the digit '5' for "
     "the 5000th time?",
     ["Count the digits by length: numbers 1 to 9 use 9 digits, 10 to 99 use 90 × 2 = 180 digits, so 189 digits in "
      "all, and 3-digit numbers use 900 × 3 = 2700 digits.",
      "(a) 1000 − 189 = 811 digits into the 3-digit numbers. 811 ÷ 3 gives 270 whole numbers and 1 left over. So "
      "the digit is the first digit of the 271st 3-digit number, 100 + 270 = 370. The digit is 3, in 370.",
      "(b) Up to 5-digit numbers: 9 + 180 + 2700 + 36,000 + 4,50,000 = 4,88,889 digits. The millionth digit is "
      "10,00,000 − 4,88,889 = 5,11,111 digits into the 6-digit numbers. 5,11,111 ÷ 6 gives 85,185 whole numbers and "
      "1 left over. So it is the first digit of 1,00,000 + 85,185 = 1,85,185, and the digit is 1.",
      "(c) Counting the fives written by computer, the digit 5 is written for the 5000th time in the number "
      "13,495."],
     "(a) 3, in the number 370 (b) 1,85,185 (c) at the number 13,495"),
    ("1.6.FiO_7", "Figure it Out, Q7 (two buttons)",
     "A calculator has only '+10,000' and '+100' buttons. Write an expression describing the number of button clicks "
     "to be made for the following numbers: (a) 20,800 (b) 92,100 (c) 1,20,500 (d) 65,30,000 (e) 70,25,700",
     ["Use as many +10,000 presses as fit, then press +100 for the rest.",
      "(a) 20,800 = (2 × 10,000) + (8 × 100). Clicks: 2 + 8 = 10.",
      "(b) 92,100 = (9 × 10,000) + (21 × 100). Clicks: 9 + 21 = 30.",
      "(c) 1,20,500 = (12 × 10,000) + (5 × 100). Clicks: 12 + 5 = 17.",
      "(d) 65,30,000 = 653 × 10,000. Clicks: 653.",
      "(e) 70,25,700 = (702 × 10,000) + (57 × 100). Clicks: 702 + 57 = 759."],
     "(a) 10 (b) 30 (c) 17 (d) 653 (e) 759 clicks"),
    ("1.6.FiO_8", "Figure it Out, Q8 (lakhs in a billion)",
     "How many lakhs make a billion?",
     ["A billion is 100 crore, and a crore is 100 lakh.",
      "So a billion is 100 × 100 lakh = 10,000 lakh.",
      "Check: 10,000 × 1,00,000 = 1,00,00,00,000, which is 1 followed by 9 zeros."],
     "10,000 lakhs make a billion"),
    ("1.6.FiO_9", "Figure it Out, Q9 (two sets of cards)",
     "You are given two sets of number cards numbered from 1 to 9. Place a number card in each box below to get the "
     "(a) largest possible sum (b) smallest possible difference of the two resulting numbers. The boxes are a row of "
     "7 boxes on top and a row of 5 boxes below, lined up on the right.",
     ["Each digit 1 to 9 can be used twice, so 18 cards are available.",
      "(a) For the largest sum put the largest digits in the highest places of both numbers: 99,87,654 on top and "
      "87,654 below.",
      "The sum is 99,87,654 + 87,654 = 1,00,75,308.",
      "(b) For the smallest difference make the top number as small as possible and the bottom number as large as "
      "possible: 11,22,334 on top and 99,887 below.",
      "The difference is 11,22,334 − 99,887 = 10,22,447."],
     "(a) 1,00,75,308 (b) 10,22,447"),
    ("1.6.FiO_10", "Figure it Out, Q10 (get close with cards)",
     "You are given some number cards: 4000, 13000, 300, 70000, 150000, 20, 5. Using the cards get as close as you can "
     "to the numbers below using any operation you want. Each card can be used only once for making a particular "
     "number. (a) 1,10,000 (b) 2,00,000 (c) 5,80,000 (d) 12,45,000 (e) 20,90,800",
     ["(a) (13000 × 20) − 150000 = 2,60,000 − 1,50,000 = 1,10,000.",
      "(b) (70000 × 5) − 150000 = 3,50,000 − 1,50,000 = 2,00,000.",
      "(c) 150000 + (((4000 + 300) × 20) × 5) = 1,50,000 + 4,30,000 = 5,80,000.",
      "(d) (13000 + 70000) × (20 − 5) = 83,000 × 15 = 12,45,000.",
      "(e) ((300 + 70000) × 20) + ((150000 − 13000) × 5) = 14,06,000 + 6,85,000 = 20,91,000, which is 200 more than "
      "20,90,800."],
     "(a) 1,10,000 (b) 2,00,000 (c) 5,80,000 (d) 12,45,000 exactly; (e) 20,91,000, only 200 away"),
    ("1.6.FiO_11", "Figure it Out, Q11 (coins to match a statue)",
     "Find out how many coins should be stacked to match the height of the Statue of Unity. Assume each coin is 1 mm "
     "thick.",
     ["The Statue of Unity is about 180 metres tall.", "1 metre is 1000 mm, so 180 m = 180 × 1000 mm = 1,80,000 mm.",
      "Each coin is 1 mm, so 1,80,000 coins are needed."],
     "1,80,000 coins"),
    ("1.6.FiO_12", "Figure it Out, Q12 (an albatross trip)",
     "Grey-headed albatrosses have a roughly 7-feet wide wingspan. They are known to migrate across several oceans. "
     "Albatrosses can cover about 900 to 1000 km in a day. One of the longest single trips recorded is about 12,000 km. "
     "How many days would such a trip take to cross an ocean approximately?",
     ["Days = distance ÷ distance each day.",
      "At 1000 km a day: 12,000 ÷ 1000 = 12 days.",
      "At 900 km a day: 12,000 ÷ 900 is about 13.3 days.",
      "So the trip takes about 12 to 14 days."],
     "About 12 to 14 days"),
    ("1.6.FiO_13", "Figure it Out, Q13 (a godwit's flight)",
     "A bar-tailed godwit holds the record for the longest recorded non-stop flight. It travelled 13,560 km from "
     "Alaska to Australia without stopping. Its journey started on 13 October 2022 and continued for about 11 days. "
     "Find out the approximate distance it covered every day. Find out the approximate distance it covered every "
     "hour.",
     ["Distance each day = 13,560 ÷ 11, which is about 1233 km.",
      "A day has 24 hours, so the distance each hour is 1233 ÷ 24, which is about 51 km."],
     "About 1233 km each day and about 51 km each hour"),
    ("1.6.FiO_14", "Figure it Out, Q14 (heights against Somu's building)",
     "Bald eagles are known to fly as high as 4500 to 6000 m above the ground level. Mount Everest is about 8850 m "
     "high. Aeroplanes can fly as high as 10,000 to 12,800 m. How many times bigger are these heights compared to "
     "Somu's building?",
     ["Somu's building is 40 m tall.",
      "Eagles: 4500 ÷ 40 = 112.5 and 6000 ÷ 40 = 150. So about 112 to 150 times.",
      "Mount Everest: 8850 ÷ 40 = 221.25, so about 221 times.",
      "Aeroplanes: 10,000 ÷ 40 = 250 and 12,800 ÷ 40 = 320. So 250 to 320 times."],
     "Eagles 112.5 to 150 times, Everest about 221 times, aeroplanes 250 to 320 times"),
]

TOPICS.append(TOPIC(
    "T15", "M6", "Did You Ever Wonder?", ["1.6"], "Evaluate",
    "Students test fun what-if questions by making stated assumptions, multiply in stages to compare a total with a "
    "benchmark, and decide whether the result is more or less than the target.",
    "A what-if question about a large number becomes a calculation once you state an assumption and work in stages.",
    [A("T15.C1", "Could Mumbai fit into buses and ships", "Evaluate",
       "Students assume a bus holds 50 people, find the people in one lakh buses, compare with Mumbai's population, "
       "and test 5000 ships of 2500 people.",
       textbook=["1.6 Did You Ever Wonder...?",
                 "Estu is amused by all these interesting facts about large numbers. He came up with an unusual "
                 "question, \"Could the entire population of Mumbai fit into 1 lakh buses?\" What do you think? How "
                 "can we find out?",
                 "Let us assume a bus can accommodate 50 people. Then 1 lakh buses can accommodate 1 lakh × 50 = "
                 "50 lakh people.",
                 "The population of Mumbai is more than 1 crore 24 lakhs (we saw this in an earlier table). So, the "
                 "entire population of Mumbai cannot fit in 1 lakh buses.",
                 "The RMS Titanic ship carried about 2500 passengers. Can the population of Mumbai fit into 5000 such "
                 "ships?"],
       teach=["Predict first: one lakh buses of 50 people each. Is that more or less than one crore people?",
              "State the assumption, multiply, and compare with the population of Mumbai.",
              "A fit needs a capacity at least as big as the population."],
       examples=[
           WE("Could Mumbai's population, 1,24,42,373, fit into 1 lakh buses of 50 people each? Could it fit into 5000 "
              "ships of 2500 people each?",
              ["1,00,000 × 50 = 50,00,000 people in the buses.",
               "50,00,000 is less than 1,24,42,373, so no.",
               "5000 × 2500 = 1,25,00,000 people in the ships.",
               "1,25,00,000 − 1,24,42,373 = 57,627, so the ships have room for 57,627 more people than the city.",
               "So yes, 5000 such ships could carry everyone."],
              "No for the buses (50,00,000 is too few); yes for the ships (1,25,00,000 is more)",
              ncert=["1.6.buses", "1.6.ships"])],
       key_terms=["assumption", "capacity"], misconceptions=["M_ESTIMATE_SIDE"], minutes=8),
     A("T15.C2", "Reaching the Moon and the Sun", "Evaluate",
       "Students work out the distance travelled in a year and in ten years at 100 km a day, compare with the distance "
       "to the Moon, and find the days needed to reach the Sun at 1000 km a day.",
       textbook=["Inspired by this strange question, Roxie wondered, \"If I could travel 100 kilometers every day, "
                 "could I reach the Moon in 10 years?\" (The distance between the Earth and the Moon is 3,84,400 "
                 "km.)",
                 "How far would she have travelled in a year? How far would she have travelled in 10 years?",
                 "Is it not easier to perform these calculations in stages? You can use this method for all large "
                 "calculations.",
                 "Find out if you can reach the Sun in a lifetime, if you travel 1000 kilometers every day. (You had "
                 "written down the distance between the Earth and the Sun in a previous exercise.)"],
       teach=["Predict first: 100 km a day for ten years. Is it more or less than 3,84,400 km?",
              "Work in stages: first one year, then ten years, then compare.",
              "For the Sun, find the number of days needed and change it to years."],
       examples=[
           WE("At 100 km a day, how far is a year and ten years, and can Roxie reach the Moon (3,84,400 km)?",
              ["In a year: 100 × 365 = 36,500 km.", "In ten years: 36,500 × 10 = 3,65,000 km.",
               "3,84,400 − 3,65,000 = 19,400, so she is 19,400 km short of the Moon."],
              "36,500 km in a year; 3,65,000 km in 10 years; 19,400 km short of the Moon",
              ncert=["1.6.moon_year", "1.6.moon_ten"]),
           WE("At 1000 km a day, can you reach the Sun, 14,70,00,000 km away, in a lifetime of 100 years?",
              ["Days needed: 14,70,00,000 ÷ 1000 = 1,47,000 days.",
               "Days in 100 years: 365 × 100 = 36,500, which is less than 1,47,000.",
               "Years needed: 1,47,000 ÷ 365 is about 402.7 years.",
               "So no, a lifetime is not enough."],
              "1,47,000 days, about 402.7 years, so not in a lifetime", ncert=["1.6.sun"])],
       key_terms=["stages", "distance"], misconceptions=["M_ESTIMATE_SIDE"], minutes=10),
     A("T15.C3", "Sheets, babies and coins", "Evaluate",
       "Students make stated assumptions and test whether one lakh sheets of paper can be lifted, whether a million "
       "babies are born in a day, and whether a million coins can be counted in a day.",
       textbook=["Make necessary reasonable assumptions and answer the questions below:",
                 "(a) If a single sheet of paper weighs 5 grams, could you lift one lakh sheets of paper together at "
                 "the same time?",
                 "(b) If 250 babies are born every minute across the world, will a million babies be born in a day?",
                 "(c) Can you count 1 million coins in a day? Assume you can count 1 coin every second.",
                 "Think and create more such fun questions and share them with your class."],
       teach=["Predict first: one lakh sheets of five grams each. Is it more or less than a bag of rice of 50 kg?",
              "Turn units: 1000 grams make a kilogram, 60 minutes make an hour, 24 hours make a day.",
              "Always write the assumption you used before the answer."],
       examples=[
           WE("A sheet weighs 5 grams. Can you lift one lakh sheets at once?",
              ["1,00,000 × 5 g = 5,00,000 g.", "1000 g make 1 kg, so 5,00,000 g = 500 kg.",
               "A person cannot lift 500 kg, so no."],
              "No, one lakh sheets weigh 500 kg", ncert=["1.6.sheets"]),
           WE("250 babies are born every minute. Are a million babies born in a day? Can you count a million coins in a "
              "day at one coin every second?",
              ["Babies in a day: 250 × 60 × 24 = 3,60,000.", "3,60,000 is less than 10,00,000, so no.",
               "Seconds in a day: 60 × 60 × 24 = 86,400, so only 86,400 coins can be counted.",
               "86,400 is less than 10,00,000, so no."],
              "No for both: 3,60,000 babies and 86,400 coins in a day", ncert=["1.6.babies", "1.6.coins",
                                                                              "1.6.create"])],
       key_terms=["assumption", "unit"], misconceptions=["M_ESTIMATE_SIDE"], minutes=10),
     DOER("T15.C4", "Pull it together and do it: large number questions", None, "Evaluate",
          "Students solve the book's closing questions on large numbers by stating the assumption, working in stages "
          "and judging whether the answer is reasonable.",
          ["Write down what you assume.", "Work in stages and keep the units.",
           "Check whether the answer is more or less than the benchmark."],
          items=[FIO(c, b, q, s, a) for (c, b, q, s, a) in F6_Q],
          ncert=[c for (c, b, q, s, a) in F6_Q], misconceptions=["M_ESTIMATE_SIDE"])]))

# ============================== T16 Puzzle: Toothpick Digits =================================================
TOPICS.append(TOPIC(
    "T16", "M6", "Puzzle Time: Toothpick Digits", ["Puzzle Time"], "Analyze",
    "Students count the sticks in digits written like a calculator display, add or move sticks to make a bigger "
    "number, place a digit to make the biggest number, and find the biggest and smallest numbers for 24 sticks.",
    "Each digit takes a fixed number of sticks, so the stick count of a number is the sum for its digits.",
    [A("T16.C1", "Counting sticks and adding two more", "Apply",
       "",
       textbook=["Toothpick Digits",
                 "We can write digits as shown in the image below. You can either use toothpicks or matchsticks, or "
                 "just write the digits in this way, using lines to represent sticks.",
                 "To make the digit 7, three sticks are needed.",
                 "Write or make the number 5108. How many sticks are required?",
                 "1. Make or write the number 42,019. It would require exactly 23 sticks.",
                 "2. Starting with 42,019, add or write two more sticks, and make a bigger number. One example is "
                 "42,078. What other numbers bigger than 42,019 can you make in this way?"],
       teach=["The digits are drawn like a calculator display: 0 uses 6 sticks, 1 uses 2, 2 uses 5, 3 uses 5, 4 uses 4, "
              "5 uses 5, 6 uses 6, 7 uses 3, 8 uses 7 and 9 uses 6.",
              "Predict first: 5108 has digits 5, 1, 0 and 8. How many sticks in all?",
              "Adding exactly two sticks can change a digit to another that needs more sticks, or add a new digit."],
       examples=[
           WE("Count the sticks in 5108 and in 42,019. Then add exactly two sticks to 42,019 to make bigger numbers.",
              ["5108 uses 5 + 2 + 6 + 7 = 20 sticks.", "42,019 uses 4 + 5 + 6 + 2 + 6 = 23 sticks.",
               "Changing 0 to 8, 1 to 7 or 9 to 8 each adds one stick. Any two of these give 42,879, 42,818 or "
               "42,078.",
               "Changing 1 to 4, 2 to 8 or 4 to 9 adds two sticks. These give 42,049, 48,019 and 92,019.",
               "A new digit 1 uses exactly two sticks, so 1,42,019 is also bigger."],
              "5108 needs 20 sticks; 42,019 needs 23; for example 42,049, 42,078, 42,818, 42,879, 48,019, 92,019",
              ncert=["puzzle.tp_count", "puzzle.tp_add"])],
       key_terms=["sticks"], enrichment=True, minutes=8),
     A("T16.C2", "Placing a 1 and moving four sticks", "Analyze",
       "",
       textbook=["3. Preetham wants to insert the digit '1' somewhere among the digits '4', '2', '0', '1' and '9'. "
                 "Where should he place the digit '1' to get the biggest possible number?",
                 "4. What other numbers can he make by placing the digit '1'?",
                 "1. Make or write the number 63,890.",
                 "2. Starting with 63,890, rearrange exactly four sticks and make a bigger number. One example is "
                 "88,078. What other numbers bigger than 63,890 can you make in this way?"],
       teach=["Predict first: should a 1 go at the front, in the middle, or at the end for the biggest number?",
              "Try each place and compare the numbers.",
              "Moving four sticks keeps the total of 30 sticks the same."],
       examples=[
           WE("Where should the digit 1 go among 4, 2, 0, 1, 9 to get the biggest number, and what other numbers can be "
              "made? Then rearrange four sticks of 63,890.",
              ["Placing a 1 gives 1,42,019, 4,12,019, 4,21,019, 4,20,119 and 4,20,191.",
               "The biggest is 4,21,019: put the 1 after the 2.",
               "63,890 uses 6 + 5 + 7 + 6 + 6 = 30 sticks.",
               "Moving exactly four sticks can give 88,078, 66,006, 68,002, 80,020 and 99,985.",
               "The biggest of these is 99,985."],
              "Biggest with a 1 inserted: 4,21,019. Four sticks moved: 88,078, 66,006 and others; the biggest found is "
              "99,985",
              ncert=["puzzle.tp_insert", "puzzle.tp_other", "puzzle.tp_move"])],
       key_terms=["rearrange"], enrichment=True, minutes=8),
     A("T16.C3", "Twenty four sticks", "Analyze",
       "",
       textbook=["1. Make any number using exactly 24 sticks or lines.",
                 "2. What is the biggest number that can be made using 24 sticks or lines?",
                 "3. What is the smallest number that can be made using 24 sticks or lines?",
                 "Make your own questions and challenge each other."],
       teach=["Predict first: which digit uses the fewest sticks, and which the most?",
              "The digit 1 uses 2 sticks, so many 1s make the longest number. The digit 8 uses 7 sticks, so few 8s make "
              "the shortest number.",
              "A number is smaller when it has fewer digits, so look for the fewest digits that can hold 24 sticks."],
       examples=[
           WE("Make a number using exactly 24 sticks. Find the biggest and the smallest such numbers.",
              ["Example: 2008 uses 5 + 6 + 6 + 7 = 24 sticks.",
               "Biggest: use the cheapest digit 1 as many times as possible, 24 ÷ 2 = 12 times, and 12 digits make the "
               "longest number: 1,11,11,11,11,111.",
               "Smallest: three digits hold at most 3 × 7 = 21 sticks, which is under 24, so four digits are needed.",
               "The first digit should be as small as possible: 1 uses 2 sticks and leaves 22, more than the 21 that "
               "three digits can hold. The next choice is 2 with 5 sticks, leaving 19, and 0, 0, 8 uses 6 + 6 + 7 = 19.",
               "So the smallest is 2008."],
              "Example 2008; biggest 1,11,11,11,11,111; smallest 2008",
              ncert=["puzzle.tp_24", "puzzle.tp_24_big", "puzzle.tp_24_small", "puzzle.tp_own"])],
       key_terms=["sticks", "digits"], enrichment=True, minutes=8),
     DOER("T16.C4", "Practice: build numbers with sticks", "matchstick_builder", "Analyze",
          "",
          ["Count the sticks of each digit and add.",
           "The digit 1 is cheapest and 8 is dearest.",
           "Move sticks to change one digit into another."],
          enrichment=True)]))

# ============================== T17 Summary ==================================================================
TOPICS.append(TOPIC(
    "T17", "M6", "Summary: Large Numbers Around Us", ["Summary"], "Remember",
    None,
    "Lakhs, crores and arabs; millions and billions; rounding and estimating; shortcuts and the length of a product; "
    "and thought experiments, in one place.",
    [A("T17.C1", "What we found about large numbers", "Remember",
       "Students restate how a lakh, a crore, a million and an arab are written, when to round, how to feel the size of "
       "a number, and one thought experiment from the chapter.",
       textbook=["Summary",
                 "We came across large numbers, lakhs, crores and arabs; millions and billions. We learnt how to read "
                 "and write these numbers in the Indian and American/International naming systems.",
                 "(a) 1 lakh is 1 followed by 5 zeroes: 1,00,000",
                 "(b) 1 crore is 1 followed by 7 zeroes: 1,00,00,000",
                 "(c) 1 million is 1 followed by 6 zeroes: 1,000,000 (which is also ten lakhs)",
                 "(d) 1 arab is 1 followed by 9 zeroes: 1,000,000,000 (which is also 100 crore or 1 billion)",
                 "We generally round up or round down large numbers. Many times it is enough just to know roughly how "
                 "big or small something is.",
                 "To get a sense of large numbers or quantities, we can check how many times bigger they are compared "
                 "to numbers or quantities that are more familiar.",
                 "We saw how to factorise numbers and regroup them to make multiplications simpler.",
                 "We carried out interesting thought experiments such as, \"Would one be able to watch 1000 movies in "
                 "a year?\""],
       teach=["Estu's question is settled: 100 years of tasting one variety a day is 36,500, and three a day passes "
              "one lakh.",
              "A lakh has five zeros, a crore seven, an arab nine; ten lakh is a million.",
              "Still open for you: would you be able to watch 1000 movies in a year? State your assumption and test it."],
       ncert=["summary"], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
