# -*- coding: utf-8 -*-
"""Topics T6 to T11 (modules M2, M3, M4): Creative Chitti, Systematic Sippy, crores and the two naming systems,
exact and approximate values, estimating, and reading data."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# the city table, as in the book: rank, city, population in 2011, population in 2001
CITY_ROWS = [
    (1, "Mumbai", "1,24,42,373", "1,19,78,450"), (2, "New Delhi", "1,10,07,835", "98,79,172"),
    (3, "Bengaluru", "84,25,970", "43,01,326"), (4, "Hyderabad", "68,09,970", "36,37,483"),
    (5, "Ahmedabad", "55,70,585", "35,20,085"), (6, "Chennai", "46,81,087", "43,43,645"),
    (7, "Kolkata", "44,86,679", "45,72,876"), (8, "Surat", "44,67,797", "24,33,835"),
    (9, "Vadodara", "35,52,371", "16,90,000"), (10, "Pune", "31,15,431", "25,38,473"),
    (11, "Jaipur", "30,46,163", "23,22,575"), (12, "Lucknow", "28,15,601", "21,85,927"),
    (13, "Kanpur", "27,67,031", "25,51,337"), (14, "Nagpur", "24,05,665", "20,52,066"),
    (15, "Indore", "19,60,631", "14,74,968"), (16, "Thane", "18,18,872", "12,62,551"),
    (17, "Bhopal", "17,98,218", "14,37,354"), (18, "Visakhapatnam", "17,28,128", "13,45,938"),
    (19, "Pimpri-Chinchwad", "17,27,692", "10,12,472"), (20, "Patna", "16,84,222", "13,66,444"),
]
CITY_LINES = ["Rank %d, %s: population in 2011 was %s and in 2001 was %s." % r for r in CITY_ROWS]

# ============================== T6 Creative Chitti ===========================================================
TOPICS.append(TOPIC(
    "T6", "M2", "Creative Chitti", ["1.2"], "Apply",
    "Students write a number as button presses of place values in many ways, trade one press of a larger button for "
    "ten presses of the next smaller one, and use the total presses to answer challenges about exact press counts.",
    "A number can be made by many combinations of place value buttons; trading one press of a larger button for ten "
    "of the next one changes the press count by nine.",
    [A("T6.C1", "Many ways to make a number", "Apply",
       "Students write a number such as 5072 as button presses of place values in a second and a third way, and check "
       "each expression adds to the number.",
       textbook=["4. Creative Chitti is a different kind of calculator. It has the following buttons: +1, +10, +100, "
                 "+1000, +10000, +100000 and +1000000. It always has multiple ways of doing things. \"How so?\", you "
                 "might ask.",
                 "To get the number 321, it presses +10 thirty two times and +1 once. Will it get 321? "
                 "Alternatively, it can press +100 two times and +10 twelve times and +1 once.",
                 "5. Two of the many different ways to get 5072 are shown below. These two ways can be expressed as: "
                 "(a) (50 × 100) + (7 × 10) + (2 × 1) = 5072 (b) (3 × 1000) + (20 × 100) + (72 × 1) = 5072",
                 "Find a different way to get 5072 and write an expression for the same."],
       teach=["Predict first: can 321 be made only by pressing +10 thirty two times and +1 once?",
              "(32 × 10) + (1 × 1) = 321, and also (2 × 100) + (12 × 10) + (1 × 1) = 321.",
              "Each expression is presses × button value, added up. Check the total to see the number."],
       examples=[
           WE("Two ways to get 5072 are (50 × 100) + (7 × 10) + (2 × 1) and (3 × 1000) + (20 × 100) + (72 × 1). Find a "
              "different way and write its expression.",
              ["Start from 5072 = 5000 + 70 + 2.",
               "Use 4 presses of +1000 and trade the last 1000 for 10 presses of +100.",
               "(4 × 1000) + (10 × 100) + (7 × 10) + (2 × 1) = 4000 + 1000 + 70 + 2 = 5072.",
               "That is 4 + 10 + 7 + 2 = 23 presses; the sum is 5072, so the way works."],
              "(4 × 1000) + (10 × 100) + (7 × 10) + (2 × 1) = 5072", ncert=["1.2.chitti_5072"])],
       key_terms=["button presses", "expression"], misconceptions=["M_BUTTON_ONE_WAY"], minutes=8),
     A("T6.C2", "Chitti's challenges", "Analyze",
       "Students trade a press of a larger button for ten presses of the next one, see that each trade adds nine "
       "presses, and use it to make 997 in two ways and the extreme 3-digit numbers in 30 presses.",
       textbook=["Creative Chitti has some questions for you:",
                 "(a) You have to make exactly 30 button presses. What is the largest 3-digit number you can make? "
                 "What is the smallest 3-digit number you can make?",
                 "(b) 997 can be made using 25 clicks. Can you make 997 with a different number of clicks?",
                 "Create questions like these and challenge your classmates."],
       teach=["Predict first: 997 takes 9 + 9 + 7 = 25 presses. If one press of +100 is swapped for ten presses of "
              "+10, do the presses go up or down?",
              "A swap of one press for ten presses changes the count by 9. So the presses are the digit sum plus a "
              "multiple of 9.",
              "For exactly 30 presses the gap from the digit sum must be a multiple of 9."],
       examples=[
           WE("997 can be made with 25 presses. Make 997 with a different number of presses. Then find the largest and "
              "the smallest 3-digit number that can be made with exactly 30 presses.",
              ["997 = (9 × 100) + (9 × 10) + (7 × 1) takes 9 + 9 + 7 = 25 presses.",
               "Trade one +100 press for ten +10 presses: (8 × 100) + (19 × 10) + (7 × 1) = 997.",
               "That takes 8 + 19 + 7 = 34 presses, nine more than before.",
               "For 30 presses the digit sum must be 30 − 9 = 21 or 30 − 18 = 12 or 3, since each trade adds 9.",
               "Largest 3-digit number: 993, with the digit sum 21: (8 × 100) + (19 × 10) + (3 × 1) = 993 uses "
               "8 + 19 + 3 = 30 presses.",
               "Smallest 3-digit number: 102, with the digit sum 3: (8 × 10) + (22 × 1) = 102 uses 8 + 22 = 30 "
               "presses."],
              "997 in 34 presses too; largest 993 and smallest 102 with exactly 30 presses",
              ncert=["1.2.chitti_a", "1.2.chitti_b", "1.2.chitti_create"])],
       key_terms=["button presses", "digit sum"], misconceptions=["M_BUTTON_ONE_WAY"], minutes=10),
     DOER("T6.C3", "Practice: trade and write the expression", "trading_board", "Apply",
          "Students trade presses between place value buttons on a board, write an expression for each way to make a "
          "number, and check that each expression adds to the target.",
          ["Each button press adds its place value.",
           "Trade one press for ten presses of the next smaller button to get another way.",
           "Add the expression to check it matches the number."],
          items=[
              FIO("1.2.FiO_chitti", "Figure it Out (many ways with Chitti)",
                  "For each number given below, write expressions for at least two different ways to obtain the "
                  "number through button clicks. Think like Chitti and be creative. (a) 8300 (b) 40629 (c) 56354 "
                  "(d) 66666 (e) 367813",
                  ["(a) (8 × 1000) + (3 × 100) = 8300, or (5 × 1000) + (33 × 100) = 8300.",
                   "(b) (40 × 1000) + (6 × 100) + (2 × 10) + (9 × 1) = 40629, or "
                   "(30 × 1000) + (106 × 100) + (29 × 1) = 40629.",
                   "(c) (56 × 1000) + (3 × 100) + (5 × 10) + (4 × 1) = 56354, or "
                   "(46 × 1000) + (103 × 100) + (54 × 1) = 56354.",
                   "(d) (66 × 1000) + (6 × 100) + (66 × 1) = 66666, or "
                   "(6 × 10000) + (6 × 1000) + (6 × 100) + (6 × 10) + (6 × 1) = 66666.",
                   "(e) (3 × 100000) + (6 × 10000) + (7 × 1000) + (8 × 100) + (1 × 10) + (3 × 1) = 367813, or "
                   "(36 × 10000) + (7 × 1000) + (8 × 100) + (1 × 10) + (3 × 1) = 367813."],
                  "Each number has many ways; two ways for each are shown, and every expression adds to its number",
                  tool="trading_board")],
          ncert=["1.2.FiO_chitti"], misconceptions=["M_BUTTON_ONE_WAY"])]))

# ============================== T7 Systematic Sippy and crores ===============================================
TOPICS.append(TOPIC(
    "T7", "M2", "Systematic Sippy and the Crore", ["1.2"], "Apply",
    "Students make a number with the least number of button presses by using each digit as the presses for its place, relate "
    "that least number to the digit sum, and find the number made by ten presses of the plus-ten-lakh button, a "
    "crore.",
    "The fewest presses use each digit of the number as the presses for its place; ten lakhs times ten is a crore, "
    "1 followed by seven zeros.",
    [A("T7.C1", "Fewest button presses", "Apply",
       "Students make 5072 and 8300 with as few presses as possible by using each digit as the presses of its place "
       "value button, and compare with a longer way.",
       textbook=["Systematic Sippy is a different kind of calculator. It has the following buttons: +1, +10, +100, "
                 "+1000, +10000, +100000. It wants to be used as minimally as possible.",
                 "How can we get the numbers (a) 5072, (b) 8300 using as few button clicks as possible? Find out "
                 "which buttons should be clicked and how many times to get the desired numbers given in the table. "
                 "The aim is to click as few buttons as possible.",
                 "Here is one way to get the number 5072. This method uses 23 button clicks in total.",
                 "Is there another way to get 5072 using less than 23 button clicks? Write the expression for the "
                 "same."],
       teach=["Predict first: 5072 made with 5 presses of +1000, 6 of +10 and 12 of +1 takes 23 presses. Can it be done "
              "in fewer?",
              "Ten presses of one button can always be traded for one press of the next bigger button, which saves "
              "nine presses.",
              "So every button except the biggest is pressed at most nine times: the presses are the digits."],
       examples=[
           WE("Make (a) 5072 and (b) 8300 with the fewest button presses. One way to get 5072 takes 5 + 0 + 6 + 12 = 23 "
              "presses.",
              ["(a) 5072 = (5 × 1000) + (0 × 100) + (7 × 10) + (2 × 1): the presses are the digits 5, 0, 7 and 2.",
               "Number of presses: 5 + 7 + 2 = 14, which is fewer than 23.",
               "(b) 8300 = (8 × 1000) + (3 × 100).", "Number of presses: 8 + 3 = 11."],
              "(a) (5 × 1000) + (7 × 10) + (2 × 1) in 14 presses; (b) (8 × 1000) + (3 × 100) in 11 presses",
              ncert=["1.2.sippy_a", "1.2.sippy_b"])],
       key_terms=["fewest presses", "digit"], misconceptions=["M_FEWEST_BIG"], minutes=8),
     A("T7.C2", "Ten lakhs make a crore", "Understand",
       "Students press the plus ten lakh button ten times, read the number as 100 lakhs, and write it as 1 followed by "
       "seven zeros named a crore.",
       textbook=["What if we press the +10,00,000 button ten times? What number will come up? How many zeroes will it "
                 "have? What should we call it?",
                 "The number will be 100 lakhs, which is also called a crore. 1 crore is written as 1,00,00,000, it "
                 "is 1 followed by seven zeroes."],
       teach=["Predict first: ten presses of +10,00,000 give how many lakhs, and how many zeros will the number have?",
              "10 × 10,00,000 is ten times ten lakh, which is one hundred lakh.",
              "One hundred lakh is called a crore: 1,00,00,000, which is 1 followed by seven zeros."],
       examples=[
           WE("Press the +10,00,000 button ten times. What number appears, how many zeros does it have, and what is "
              "it called?",
              ["Ten presses: 10 × 10,00,000 = 1,00,00,000.", "10 lakhs ten times is 100 lakhs.",
               "Count the zeros in 1,00,00,000: there are seven.",
               "100 lakhs is called one crore."],
              "1,00,00,000, which is 100 lakhs, 1 followed by seven zeros, called a crore", ncert=["1.2.crore"])],
       key_terms=["crore", "lakh"], misconceptions=["M_LAKH_ZEROS"], minutes=6),
     DOER("T7.C3", "Practice: fewest presses and the digit sum", "fewest_presses", "Apply",
          "Students find the least number of presses for a number by reading its digits, compare the count with the sum of the "
          "digits, and explain why the expression matches the Indian place value notation.",
          ["The digits of a number are the fewest presses for each place.",
           "The fewest presses equal the sum of the digits.",
           "Ten presses of a button are never needed because one press of the next button does the same."],
          items=[
              FIO("1.2.FiO_sippy1", "Figure it Out, Q1 (fewest presses)",
                  "For the numbers in the previous exercise, find out how to get each number by making the smallest "
                  "number of button clicks and write the expression. The numbers are (a) 8300 (b) 40629 (c) 56354 "
                  "(d) 66666 (e) 367813.",
                  ["(a) 8300 = (8 × 1000) + (3 × 100); 8 + 3 = 11 clicks.",
                   "(b) 40629 = (4 × 10000) + (6 × 100) + (2 × 10) + (9 × 1); 4 + 6 + 2 + 9 = 21 clicks.",
                   "(c) 56354 = (5 × 10000) + (6 × 1000) + (3 × 100) + (5 × 10) + (4 × 1); 5 + 6 + 3 + 5 + 4 = 23 "
                   "clicks.",
                   "(d) 66666 = (6 × 10000) + (6 × 1000) + (6 × 100) + (6 × 10) + (6 × 1); 6 + 6 + 6 + 6 + 6 = 30 "
                   "clicks.",
                   "(e) 367813 = (3 × 100000) + (6 × 10000) + (7 × 1000) + (8 × 100) + (1 × 10) + (3 × 1); "
                   "3 + 6 + 7 + 8 + 1 + 3 = 28 clicks."],
                  "(a) 11 (b) 21 (c) 23 (d) 30 (e) 28 clicks", tool="fewest_presses"),
              FIO("1.2.FiO_sippy2", "Figure it Out, Q2 (a connection)",
                  "Do you see any connection between each number and the corresponding smallest number of button "
                  "clicks?",
                  ["Take the number 8300: its digits are 8, 3, 0 and 0, and 8 + 3 + 0 + 0 = 11 is its smallest "
                   "number of clicks.",
                   "40629 has digits adding to 4 + 0 + 6 + 2 + 9 = 21, the smallest clicks.",
                   "56354 gives 5 + 6 + 3 + 5 + 4 = 23, and 66666 gives 6 + 6 + 6 + 6 + 6 = 30.",
                   "367813 gives 3 + 6 + 7 + 8 + 1 + 3 = 28.",
                   "So the smallest number of clicks is the sum of the digits of the number."],
                  "The smallest number of clicks is the sum of the digits of the number", tool="fewest_presses"),
              FIO("1.2.FiO_sippy3", "Figure it Out, Q3 (why the expression is the place value notation)",
                  "If you notice, the expressions for the least button clicks also give the Indian place value "
                  "notation of the numbers. Think about why this is so.",
                  ["Ten presses of one button make the same amount as one press of the next bigger button.",
                   "So in the fewest way no button other than the biggest is pressed ten or more times.",
                   "Each press count is then a single digit from 0 to 9, written in that button's place.",
                   "Written side by side, these counts are the digits of the number in place value notation, for "
                   "example 5072 has 5 thousands, 0 hundreds, 7 tens and 2 ones."],
                  "Each place holds at most nine presses, so the counts are the digits of the number",
                  tool="fewest_presses")],
          ncert=["1.2.FiO_sippy1", "1.2.FiO_sippy2", "1.2.FiO_sippy3"], misconceptions=["M_FEWEST_BIG"])]))

# ============================== T8 Indian and International systems ==========================================
TOPICS.append(TOPIC(
    "T8", "M3", "Indian and International Systems", ["1.3"], "Apply",
    "Students place commas in the 3-2-2 Indian pattern and the 3-3-3 international pattern, count the zeros in a "
    "lakh, a crore and an arab, and read and write large numbers with lakh, crore, million and billion names.",
    "The Indian system groups digits as 3-2-2 and names lakh, crore and arab; the international system groups them "
    "as 3-3-3 and names million and billion.",
    [A("T8.C1", "Two comma patterns", "Understand",
       "Students compare the Indian 3-2-2 grouping with the international 3-3-3 grouping, and write the same number "
       "with commas and name it in both systems.",
       textbook=["1.3 Of Crores and Crores!",
                 "The table below shows some numbers according to both the Indian system and the American system "
                 "(also called the International system) of naming numerals and placing commas. Observe the placement "
                 "of commas in both systems.",
                 "Indian system: 1,000 One thousand; 10,000 Ten thousand; 1,00,000 One lakh; 10,00,000 Ten lakhs; "
                 "1,00,00,000 One crore; 10,00,00,000 Ten crores; 1,00,00,00,000 One arab or One hundred crores.",
                 "American system: 1,000 One thousand; 10,000 Ten thousand; 100,000 Hundred thousand; 1,000,000 One "
                 "million; 10,000,000 Ten million; 100,000,000 Hundred million; 1,000,000,000 One billion.",
                 "Notice that in the Indian system, commas are placed to group the digits in a 3-2-2-2... pattern "
                 "from right to left (thousands, lakhs, crores, etc.). In the American system, the digits are grouped "
                 "uniformly in a 3-3-3-3... pattern from right to left (thousands, millions, billions, etc.).",
                 "The Indian system of naming numbers is also followed in Bhutan, Nepal, Sri Lanka, Pakistan, "
                 "Bangladesh, Maldives, Afghanistan, and Myanmar. The words lakh and crore originate from the Sanskrit "
                 "words lakṣha and koṭi. The American system is also used in many countries."],
       teach=["Predict first: where do the commas go in 10,00,000 in the Indian system, and where in 1,000,000 in the "
              "American system?",
              "Indian: the first comma comes after 3 digits from the right, then after every 2 digits.",
              "American: a comma after every 3 digits from the right.",
              "Ten lakh is one million, one crore is ten million, and one hundred crore is one billion."],
       examples=[
           WE("Place commas in 12345678 in the Indian and the American system and read it in both.",
              ["Indian system, groups of 3 then 2s: the last three digits 678, then 45, then 23, then 1.",
               "So 12345678 is 1,23,45,678: one crore twenty three lakh forty five thousand six hundred seventy "
               "eight.",
               "American system, groups of 3: 678, then 345, then 12.",
               "So 12345678 is 12,345,678: twelve million three hundred forty five thousand six hundred seventy "
               "eight."],
              "Indian 1,23,45,678; American 12,345,678", ncert=["1.3.commas", "1.3.table"])],
       key_terms=["Indian system", "international system", "comma"], misconceptions=["M_COMMA_PLACE"], minutes=8),
     A("T8.C2", "Zeros in a lakh, a crore and an arab", "Analyze",
       "Students say that a lakh is a hundred thousands, a crore is a hundred lakhs and an arab is a hundred crores, "
       "count the zeros in each, and find the zeros in a thousand lakh and in a hundred thousand.",
       textbook=["Observe the number of zeroes in 1 lakh and 1 crore. 1 lakh, written in numbers would be 1 followed "
                 "by 5 zeroes. 1 crore, written in numbers would be 1 followed by 7 zeroes.",
                 "A lakh is a hundred times a thousand, a crore is a hundred times a lakh and an arab is a hundred "
                 "times a crore (i.e., a hundred thousand is 1 lakh, 100 lakhs is 1 crore, and 100 crores is 1 arab).",
                 "How many zeros does a thousand lakh have? ____",
                 "How many zeros does a hundred thousand have? ____"],
       teach=["Predict first: a lakh has 5 zeros and a crore has 7. How many zeros does an arab have?",
              "Each step multiplies by 100, which adds two zeros.",
              "A thousand lakh is 1000 × 1,00,000. A hundred thousand is 100 × 1000."],
       examples=[
           WE("Show that a lakh is a hundred thousands, a crore a hundred lakhs and an arab a hundred crores. Then "
              "find the zeros in a thousand lakh and in a hundred thousand.",
              ["A lakh: 100 × 1000 = 1,00,000, with 5 zeros.",
               "A crore: 100 × 1,00,000 = 1,00,00,000, with 7 zeros.",
               "An arab: 100 × 1,00,00,000 = 1,00,00,00,000, with 9 zeros.",
               "A thousand lakh: 1000 × 1,00,000 = 10,00,00,000, which has 8 zeros and is ten crore.",
               "A hundred thousand: 100 × 1000 = 1,00,000, which has 5 zeros and is one lakh."],
              "A thousand lakh has 8 zeros; a hundred thousand has 5 zeros",
              ncert=["1.3.zeros", "1.3.zeros_thousand_lakh", "1.3.zeros_hundred_thousand"])],
       key_terms=["lakh", "crore", "arab", "zeros"], misconceptions=["M_LAKH_ZEROS"], minutes=8),
     A("T8.C3", "Reading a ten-digit number in both systems", "Apply",
       "Students place commas in 9876501234 in both systems and read it as arab, crore and lakh in the Indian system "
       "and as billion, million and thousand in the international system.",
       textbook=["The number 9876501234 can be easily read by placing commas first:",
                 "(a) 9,87,65,01,234 → 9 arab 87 crore 65 lakhs 1 thousand and 234 or 987 crore 65 lakh 1 thousand "
                 "234 (in the Indian system).",
                 "(b) 9,876,501,234 → 9 billion 876 million 501 thousand 234 (in the American system).",
                 "We shall come across even bigger numbers in later grades."],
       teach=["Predict first: how many digits does 9876501234 have, and which name belongs to its first digit?",
              "Indian grouping from the right: 234, then 01, then 65, then 87, then 9.",
              "American grouping from the right: 234, then 501, then 876, then 9."],
       examples=[
           WE("Read 9876501234 in the Indian system and in the American system.",
              ["It has 10 digits.",
               "Indian: 9,87,65,01,234 is 9 arab 87 crore 65 lakh 1 thousand 234, or 987 crore 65 lakh 1 thousand "
               "234.",
               "American: 9,876,501,234 is 9 billion 876 million 501 thousand 234."],
              "Indian: 9 arab 87 crore 65 lakh 1 thousand 234. American: 9 billion 876 million 501 thousand 234",
              ncert=["1.3.read_big"])],
       key_terms=["arab", "billion", "million"], misconceptions=["M_COMMA_PLACE"], minutes=8),
     DOER("T8.C4", "Practice: convert between the systems", "system_converter", "Apply",
          "Students place commas in both systems, name each part with lakh, crore, million or billion, and convert "
          "between the names by multiplying and dividing by 10 lakh.",
          ["Indian commas: 3, then 2s. International commas: 3s.",
           "10 lakh is 1 million; 100 crore is 1 billion.",
           "Convert a name by moving the number to the same digits."],
          items=[
              FIO("1.3.FiO_1", "Figure it Out, Q1 (read and name in both systems)",
                  "Read the following numbers in Indian place value notation and write their number names in both the "
                  "Indian and American systems: (a) 4050678 (b) 48121620 (c) 20022002 (d) 246813579 (e) 345000543 "
                  "(f) 1020304050",
                  ["(a) Indian 40,50,678: forty lakh fifty thousand six hundred seventy eight. American 4,050,678: "
                   "four million fifty thousand six hundred seventy eight.",
                   "(b) Indian 4,81,21,620: four crore eighty one lakh twenty one thousand six hundred twenty. "
                   "American 48,121,620: forty eight million one hundred twenty one thousand six hundred twenty.",
                   "(c) Indian 2,00,22,002: two crore twenty two thousand two. American 20,022,002: twenty million "
                   "twenty two thousand two.",
                   "(d) Indian 24,68,13,579: twenty four crore sixty eight lakh thirteen thousand five hundred "
                   "seventy nine. American 246,813,579: two hundred forty six million eight hundred thirteen "
                   "thousand five hundred seventy nine.",
                   "(e) Indian 34,50,00,543: thirty four crore fifty lakh five hundred forty three. American "
                   "345,000,543: three hundred forty five million five hundred forty three.",
                   "(f) Indian 1,02,03,04,050: one arab two crore three lakh four thousand fifty. American "
                   "1,020,304,050: one billion twenty million three hundred four thousand fifty."],
                  "(a) 40,50,678 (b) 4,81,21,620 (c) 2,00,22,002 (d) 24,68,13,579 (e) 34,50,00,543 "
                  "(f) 1,02,03,04,050, each named in both systems as shown", tool="system_converter"),
              FIO("1.3.FiO_2", "Figure it Out, Q2 (names to numerals)",
                  "Write the following numbers in Indian place value notation: (a) One crore one lakh one thousand "
                  "ten (b) One billion one million one thousand one (c) Ten crore twenty lakh thirty thousand forty "
                  "(d) Nine billion eighty million seven hundred thousand six hundred",
                  ["(a) 1 crore, 01 lakh, 01 thousand, 010: 1,01,01,010.",
                   "(b) One billion one million one thousand one is 1,001,001,001. In the Indian system this is "
                   "1,00,10,01,001.",
                   "(c) 10 crore, 20 lakh, 30 thousand, 040: 10,20,30,040.",
                   "(d) Nine billion eighty million seven hundred thousand six hundred is 9,080,700,600. In the "
                   "Indian system this is 9,08,07,00,600."],
                  "(a) 1,01,01,010 (b) 1,00,10,01,001 (c) 10,20,30,040 (d) 9,08,07,00,600", tool="system_converter"),
              FIO("1.3.FiO_3", "Figure it Out, Q3 (compare)",
                  "Compare and write '<', '>' or '=': (a) 30 thousand ____ 3 lakhs (b) 500 lakhs ____ 5 million "
                  "(c) 800 thousand ____ 8 million (d) 640 crore ____ 60 billion",
                  ["(a) 30 thousand is 30 × 1000 = 30,000 and 3 lakhs is 3 × 1,00,000 = 3,00,000. So it is <.",
                   "(b) 500 lakhs is 500 × 1,00,000 = 5,00,00,000 and 5 million is 5 × 10,00,000 = 50,00,000. So it "
                   "is >.",
                   "(c) 800 thousand is 800 × 1000 = 8,00,000 and 8 million is 8 × 10,00,000 = 80,00,000. So it is <.",
                   "(d) 640 crore is 640 × 1,00,00,000 = 6,40,00,00,000 and 60 billion is 60 × 1,00,00,00,000 = "
                   "60,00,00,00,000. So it is <."],
                  "(a) < (b) > (c) < (d) <", tool="system_converter")],
          ncert=["1.3.FiO_1", "1.3.FiO_2", "1.3.FiO_3"], misconceptions=["M_COMPARE_UNITS", "M_COMMA_PLACE"])]))

# ============================== T9 Exact and approximate values ==============================================
TOPICS.append(TOPIC(
    "T9", "M4", "Exact and Approximate Values", ["1.4"], "Apply",
    "Students tell when an exact number is needed and when rounding up or down is better, round a number to the "
    "nearest thousand, ten thousand, lakh, ten lakh and crore, and find all numbers with the same five nearest "
    "neighbours.",
    "A rounded value is enough when the size matters more than the exact count; rounding to a place looks at the digit "
    "to its right.",
    [A("T9.C1", "Rounding up and rounding down", "Understand",
       "Students tell the difference between an exact and an approximate value, say when rounding up or down suits a "
       "situation, and give situations where an exact number is needed.",
       textbook=["1.4 Exact and Approximate Values",
                 "1 lakh people visited the book fair. \"Ohh, so many people!\" \"If I had not gone, they would have "
                 "written 99,999 people visited the book fair last week\".",
                 "What do you think of this conversation? Have you read or heard such headlines or statements?",
                 "Very often, exact numbers are not required and just an approximation is sufficient. For example, "
                 "according to the 2011 census, the population of Chintamani town is 76,068. Instead, saying that the "
                 "population is about 75,000 is enough to give an idea of how big the quantity is.",
                 "Bappi, call and check if Toofan Express is on time. \"What number did you call?\" \"I called the "
                 "rounded off number, of course! My teacher told us that efficient people deal with rounded off "
                 "numbers.\"",
                 "There are situations where it makes sense to round up a number (rounding up is when the "
                 "approximated number is more than the actual number). For example, if a school has 732 people "
                 "including students, teachers and staff: the principal might order 750 sweets instead of 700 sweets.",
                 "There are situations where it is better to round down (rounding down is when the approximated "
                 "number is less than the actual number). For example, if the cost of an item is ₹470, the shopkeeper "
                 "may say that the cost is around ₹450 instead of saying it is around ₹500.",
                 "Think and share situations where it is appropriate to (a) round up, (b) round down, (c) either "
                 "rounding up or rounding down is okay and (d) when exact numbers are needed."],
       teach=["Predict first: a school has 732 people. Should the principal order 700 sweets or 750?",
              "Rounding up gives a value more than the actual number; rounding down gives a value less than it.",
              "Choose by the situation: rounding up when falling short is a problem, rounding down when promising too "
              "much is a problem, and exact numbers when money or safety needs them."],
       examples=[
           WE("A school has 732 people and the principal orders sweets. An item costs 470 rupees and the shopkeeper "
              "says around 450 rupees. Which one rounds up and which rounds down? Give one situation for each of: "
              "round up, round down, either, exact.",
              ["732 is more than 700, so an order of 700 sweets leaves 732 − 700 = 32 people without.",
               "750 is more than 732, so ordering 750 rounds up and every person gets a sweet.",
               "450 is less than 470, so saying around 450 rounds down; 470 − 450 = 20 rupees less.",
               "Round up: buying food for a group. Round down: the time left to catch the school bus.",
               "Either: the distance between two far away places. Exact: handling money in a bank."],
              "Ordering 750 rounds up; saying around 450 rounds down; the four situations are given above",
              ncert=["1.4.round_updown", "1.4.think_share"])],
       key_terms=["approximate", "rounding up", "rounding down"], misconceptions=["M_ROUND_PLACE"], minutes=8),
     A("T9.C2", "Nearest neighbours of a large number", "Apply",
       "Students round a large number to the nearest thousand, ten thousand, lakh, ten lakh and crore by looking at the "
       "digit to the right of the place, and write the five nearest neighbours of two numbers.",
       textbook=["Nearest Neighbours",
                 "With large numbers it is useful to know the nearest thousand, lakh or crore. For example, the "
                 "nearest neighbours of the number 6,72,85,183 are shown in the table below.",
                 "Nearest thousand 6,72,85,000. Nearest ten thousand 6,72,90,000. Nearest lakh 6,73,00,000. Nearest "
                 "ten lakh 6,70,00,000. Nearest crore 7,00,00,000.",
                 "Similarly, write the five nearest neighbours for these numbers: (a) 3,87,69,957 (b) 29,05,32,481"],
       teach=["Predict first: 6,72,85,183 to the nearest thousand: is it 6,72,85,000 or 6,72,86,000?",
              "Keep the digits up to the place, look at the next digit to the right: 5 or more rounds up, less than 5 "
              "rounds down. Fill the rest with zeros.",
              "A number halfway between two neighbours is rounded up."],
       examples=[
           WE("Write the five nearest neighbours of (a) 3,87,69,957 and (b) 29,05,32,481.",
              ["(a) Nearest thousand: the next digit is 9, so round up to 3,87,70,000.",
               "Nearest ten thousand: the digits after are 9,957, so round up to 3,87,70,000.",
               "Nearest lakh: the digits after are 69,957, which is more than 50,000, so 3,88,00,000.",
               "Nearest ten lakh: the digits after are 7,69,957, which is more than 5,00,000, so 3,90,00,000.",
               "Nearest crore: the digits after are 87,69,957, which is more than 50,00,000, so 4,00,00,000.",
               "(b) Nearest thousand: 29,05,32,000. Nearest ten thousand: 29,05,30,000. Nearest lakh: "
               "29,05,00,000.",
               "Nearest ten lakh: 5,32,481 is more than 5,00,000, so 29,10,00,000.",
               "Nearest crore: 5,32,481 is less than 50,00,000, so 29,00,00,000."],
              "(a) 3,87,70,000; 3,87,70,000; 3,88,00,000; 3,90,00,000; 4,00,00,000. (b) 29,05,32,000; "
              "29,05,30,000; 29,05,00,000; 29,10,00,000; 29,00,00,000",
              ncert=["1.4.nn_example", "1.4.nn_a", "1.4.nn_b"])],
       key_terms=["nearest neighbour", "rounding"], misconceptions=["M_ROUND_PLACE"], minutes=10),
     A("T9.C3", "A number with five equal neighbours", "Analyze",
       "Students find the numbers whose nearest thousand, ten thousand, lakh, ten lakh and crore are all 5,00,00,000, "
       "and count how many there are by using the tightest neighbour.",
       textbook=["I have a number for which all five nearest neighbours are 5,00,00,000. What could the number be? "
                 "How many such numbers are there?",
                 "Note to the Teacher: Ask students questions like, what could the numbers be if the sum had to be "
                 "less than 8,50,000."],
       teach=["Predict first: is 5,00,00,000 itself such a number? Is 5,00,00,400?",
              "The nearest thousand is the strictest neighbour. If the number rounds to 5,00,00,000 at the thousand, "
              "it also does at the larger places.",
              "A number rounds to 5,00,00,000 at the thousand when it is within 500 below it or 499 above it."],
       examples=[
           WE("Find all numbers whose five nearest neighbours are all 5,00,00,000, and say how many there are.",
              ["The nearest thousand is the strictest: the number must be within half a thousand of 5,00,00,000.",
               "The smallest such number is 5,00,00,000 − 500 = 4,99,99,500, which rounds up.",
               "The largest is 5,00,00,000 + 499 = 5,00,00,499, since 5,00,00,500 rounds up to 5,00,01,000.",
               "Count: 5,00,00,499 − 4,99,99,500 + 1 = 1000.",
               "These numbers also round to 5,00,00,000 at ten thousand, lakh, ten lakh and crore."],
              "All numbers from 4,99,99,500 to 5,00,00,499; there are 1000 of them", ncert=["1.4.five_equal"])],
       key_terms=["nearest neighbour", "rounding"], misconceptions=["M_ROUND_PLACE"], minutes=8),
     DOER("T9.C4", "Practice: round to five places", "rounding_line", "Apply",
          "Students place a number on a number line, see which neighbour it is closer to, and write all five nearest "
          "neighbours of a number.",
          ["Look at the digit to the right of the place.",
           "5 or more rounds up; less than 5 rounds down.",
           "A number within half a unit of a neighbour has that neighbour."])]))

# ============================== T10 Estimating sums and differences ==========================================
TOPICS.append(TOPIC(
    "T10", "M4", "Estimating Sums and Differences", ["1.4"], "Evaluate",
    "Students estimate a sum and a difference by rounding, decide whether the exact value is above or below a "
    "benchmark by comparing parts, find which estimate is closer, and then calculate the exact value.",
    "An estimate by rounding shows about how big a sum or difference is; comparing parts with a benchmark tells "
    "whether it is greater or less.",
    [A("T10.C1", "Estimating a sum", "Evaluate",
       "Students test two estimates of 4,63,128 + 4,19,682, decide which is closer, argue whether the sum is above or "
       "below 8,50,000 and 8,83,128, and find the exact sum.",
       textbook=["Roxie and Estu are estimating the values of simple expressions.",
                 "1. 4,63,128 + 4,19,682. Roxie: \"The sum is near 8,00,000 and is more than 8,00,000.\" Estu: \"The "
                 "sum is near 9,00,000 and is less than 9,00,000.\"",
                 "(a) Are these estimates correct? Whose estimate is closer to the sum?",
                 "(b) Will the sum be greater than 8,50,000 or less than 8,50,000? Why do you think so?",
                 "(c) Will the sum be greater than 8,83,128 or less than 8,83,128? Why do you think so?",
                 "(d) Exact value of 4,63,128 + 4,19,682 = ____"],
       teach=["Predict first: is the sum nearer to 8,00,000 or to 9,00,000?",
              "Round each part, add, and decide whether the real sum is more or less by seeing which way each part was "
              "rounded.",
              "Compare each part with a benchmark part: if both parts are bigger than the benchmark parts, the sum is "
              "bigger."],
       examples=[
           WE("Check the estimates of 4,63,128 + 4,19,682 by Roxie (near 8,00,000, more) and Estu (near 9,00,000, "
              "less). Say whose is closer, whether the sum is above or below 8,50,000 and 8,83,128, and find the "
              "exact sum.",
              ["Roxie rounds down both parts to 4,00,000 + 4,00,000 = 8,00,000, so the sum is more than that.",
               "Estu rounds up to 5,00,000 + 4,00,000 = 9,00,000, so the sum is less than that. Both are correct.",
               "(d) The exact sum is 4,63,128 + 4,19,682 = 8,82,810.",
               "Distance from 9,00,000: 9,00,000 − 8,82,810 = 17,190. Distance from 8,00,000: 8,82,810 − 8,00,000 = "
               "82,810. Estu is closer.",
               "(b) 4,63,128 is more than 4,50,000 and 4,19,682 is more than 4,00,000, so the sum is more than "
               "8,50,000.",
               "(c) 8,83,128 is 4,63,128 + 4,20,000. Since 4,19,682 is less than 4,20,000, the sum is less than "
               "8,83,128."],
              "Both estimates are correct; Estu's is closer; more than 8,50,000; less than 8,83,128; exact sum "
              "8,82,810",
              ncert=["1.4.sum_a", "1.4.sum_b", "1.4.sum_c", "1.4.sum_d"])],
       key_terms=["estimate", "sum"], misconceptions=["M_ESTIMATE_SIDE"], minutes=10),
     A("T10.C2", "Estimating a difference", "Evaluate",
       "Students test two estimates of 14,63,128 − 4,90,020, decide which is closer, argue whether the difference is "
       "above or below 9,50,000 and 9,63,128, and find the exact difference.",
       textbook=["2. 14,63,128 − 4,90,020. Roxie: \"The difference is near 10,00,000 and is less than 10,00,000.\" "
                 "Estu: \"The difference is near 9,00,000 and is more than 9,00,000.\"",
                 "(a) Are these estimates correct? Whose estimate is closer to the difference?",
                 "(b) Will the difference be greater than 9,50,000 or less than 9,50,000? Why do you think so?",
                 "(c) Will the difference be greater than 9,63,128 or less than 9,63,128? Why do you think so?",
                 "(d) Exact value of 14,63,128 − 4,90,020 = ____"],
       teach=["Predict first: if the part taken away is rounded up, is the difference rounded up or down?",
              "A bigger amount taken away leaves less. So rounding the subtracted part up makes the estimate smaller than "
              "the real difference.",
              "Compare with a benchmark: 14,63,128 − 5,00,000 is 9,63,128, and 4,90,020 is less than 5,00,000."],
       examples=[
           WE("Check the estimates of 14,63,128 − 4,90,020 by Roxie (near 10,00,000, less) and Estu (near 9,00,000, "
              "more). Say whose is closer, whether the difference is above or below 9,50,000 and 9,63,128, and find "
              "the exact difference.",
              ["Roxie: 15,00,000 − 5,00,000 = 10,00,000, rounding the larger part up and the smaller up; the "
               "difference is less than 10,00,000.",
               "Estu: 14,00,000 − 5,00,000 = 9,00,000, and the real difference is more than that.",
               "(d) The exact difference is 14,63,128 − 4,90,020 = 9,73,108.",
               "Distance from 10,00,000: 10,00,000 − 9,73,108 = 26,892. Distance from 9,00,000: 9,73,108 − 9,00,000 = "
               "73,108. Roxie is closer.",
               "(b) 14,63,128 is more than 14,50,000 and 4,90,020 is less than 5,00,000, so the difference is more "
               "than 14,50,000 − 5,00,000 = 9,50,000.",
               "(c) 9,63,128 is 14,63,128 − 5,00,000. Since 4,90,020 is less than 5,00,000, the difference is more "
               "than 9,63,128."],
              "Both estimates are correct; Roxie's is closer; more than 9,50,000; more than 9,63,128; exact "
              "difference 9,73,108",
              ncert=["1.4.diff_a", "1.4.diff_b", "1.4.diff_c", "1.4.diff_d"])],
       key_terms=["estimate", "difference"], misconceptions=["M_ESTIMATE_SIDE"], minutes=10),
     DOER("T10.C3", "Practice: estimate, then check", None, "Evaluate",
          "Students estimate a sum or difference by rounding, say whether the real value is above or below the estimate, "
          "and check against the exact value.",
          ["Round each part to a friendly number.",
           "Say which way each part moved to know if the real value is above or below.",
           "Compare with a benchmark and then calculate the exact value."])]))

# ============================== T11 Reading data: populations of cities ======================================
TOPICS.append(TOPIC(
    "T11", "M4", "Reading Data: Populations of Cities", ["1.4"], "Analyze",
    "Students read a table of city populations for 2001 and 2011, write an observation and a title, find an "
    "approximate increase and the largest increase, pick the cities whose population nearly doubled, and find the "
    "multiplier from one city to another.",
    "Approximating lakh values lets us read a data table quickly; an increase is a subtraction and nearly doubled "
    "means the ratio is close to two.",
    [A("T11.C1", "What the table shows", "Analyze",
       "Students read the table of twenty cities, write an observation about the change from 2001 to 2011, and give "
       "the table a suitable title.",
       textbook=["Populations of Cities",
                 "Observe the populations of some Indian cities in the table below. Columns: Rank, City, Population "
                 "(2011), Population (2001)."] + CITY_LINES +
                ["From the information given in the table, answer the following questions by approximation:",
                 "1. What is your general observation about this data? Share it with the class.",
                 "2. What is an appropriate title for the above table?"],
       teach=["Predict first: did most cities grow or shrink from 2001 to 2011?",
              "The table lists twenty cities ranked by their 2011 population, with 2011 first and 2001 second.",
              "An observation is something you can see in the numbers, for example which city is largest or which one "
              "fell."],
       examples=[
           WE("Write a general observation about the table and an appropriate title.",
              ["Compare the 2011 and 2001 columns for each city.",
               "In nearly every row the 2011 number is larger, so most cities grew.",
               "Kolkata is the exception: 45,72,876 − 44,86,679 = 86,197, so it fell by about 86,000.",
               "Mumbai is the largest city in both years, and New Delhi is second.",
               "A title: Population of some Indian cities in 2001 and 2011."],
              "Most cities grew from 2001 to 2011 (Kolkata fell). Title: Population of some Indian cities in 2001 "
              "and 2011",
              ncert=["1.4.table_obs", "1.4.table_title"])],
       key_terms=["table", "observation", "title"], misconceptions=["M_ESTIMATE_SIDE"], minutes=8),
     A("T11.C2", "How much did a city grow", "Apply",
       "Students round two populations to lakhs to find an approximate increase for Pune, and compare increases to find "
       "the city whose population grew the most.",
       textbook=["3. How much is the population of Pune in 2011? Approximately, by how much has it increased compared "
                 "to 2001?",
                 "4. Which city's population increased the most between 2001 and 2011?"],
       teach=["Predict first: Pune grew from about 25 lakh to about 31 lakh. About how many lakh is the increase?",
              "Round each population to lakhs, then subtract. The increase is 2011 minus 2001.",
              "To find the largest increase, compare the increases of the cities that grew a lot."],
       examples=[
           WE("Find the population of Pune in 2011 and approximately how much it grew from 2001. Then find the city "
              "whose population grew the most.",
              ["Pune in 2011: 31,15,431, which is about 31 lakh. In 2001: 25,38,473, about 25 lakh.",
               "Approximate increase: 31 lakh − 25 lakh = 6 lakh. The exact increase is 31,15,431 − 25,38,473 = "
               "5,76,958.",
               "Look for large jumps: Bengaluru 84,25,970 − 43,01,326 = 41,24,644.",
               "Hyderabad grew by 31,72,487, Ahmedabad by 20,50,500 and Surat by 20,33,962, all less than "
               "Bengaluru.",
               "So Bengaluru grew the most, by 41,24,644."],
              "Pune: 31,15,431 in 2011, grew by about 6 lakh. Bengaluru grew the most, by 41,24,644",
              ncert=["1.4.pune", "1.4.most_increase"])],
       key_terms=["increase", "approximately"], misconceptions=["M_ESTIMATE_SIDE"], minutes=8),
     A("T11.C3", "Nearly doubled and how many times", "Analyze",
       "Students decide which cities nearly doubled by checking that the 2011 value is close to twice the 2001 value, "
       "and find by what number Patna's population is multiplied to come near Mumbai's.",
       textbook=["5. Are there cities whose population has almost doubled? Which are they?",
                 "6. By what number should we multiply Patna's population to get a number/population close to that of "
                 "Mumbai?"],
       teach=["Predict first: a city nearly doubled if its 2011 population is close to twice its 2001 population. "
              "Which row looks like that?",
              "Say nearly doubled when the 2011 value is at least 1.8 times the 2001 value.",
              "To find the multiplier, divide Mumbai by Patna and round."],
       examples=[
           WE("Find the cities whose population nearly doubled, and the number by which Patna's population is "
              "multiplied to come close to Mumbai's.",
              ["Bengaluru: about 43 lakh in 2001, twice is about 86 lakh, and 2011 is about 84 lakh. Close to double.",
               "Hyderabad: 36 lakh doubled is 72 lakh, and 2011 is 68 lakh. Surat: 24 lakh doubled is 48 lakh, and "
               "2011 is about 45 lakh.",
               "Vadodara: 17 lakh doubled is 34 lakh, and 2011 is about 36 lakh.",
               "Ahmedabad (55 lakh against 70 lakh) and Pimpri-Chinchwad (17 lakh against 20 lakh) are not close.",
               "Patna is about 17 lakh and Mumbai is about 124 lakh. Now 7 × 17 = 119 and 8 × 17 = 136, so about 7.",
               "Exact: 1,24,42,373 ÷ 16,84,222 is about 7.39."],
              "Bengaluru, Hyderabad, Surat and Vadodara nearly doubled; multiply Patna's population by about 7.39",
              ncert=["1.4.doubled", "1.4.patna_mumbai"])],
       key_terms=["ratio", "doubled", "multiply"], misconceptions=["M_ESTIMATE_SIDE"], minutes=10),
     DOER("T11.C4", "Practice: read the table", None, "Analyze",
          "Students pick two columns of a table, subtract to find an increase, divide to see how many times, and write "
          "an observation from the numbers.",
          ["Round to lakhs before comparing.",
           "Increase is later minus earlier; how many times is a division.",
           "Write what the numbers show in a sentence."])]))
