# -*- coding: utf-8 -*-
"""Topics T11, T12 (module M4: Even and Odd, Thinking Puzzles and Tables) and T13, the Chapter Revision summary: Let Us
Think with Jincy's coins and Raghu's torch, Reading Tables (the mountain table and the certificate table), and the text
summary with short concept checks. Every teaching concept has one worked example with the plan's own numbers (practice
values); the book's puzzles and table questions are FIO items of the DOERs, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T11 Let Us Think: Coins and a Torch ========================================
TOPICS.append(TOPIC(
    "T11", "M4", "Let Us Think: Coins and a Torch", ["Let Us Think"], "Apply",
    "Students list the ways to pay an exact amount with coins, one kind of coin at a time, and tell whether a switch is "
    "on or off after any press by looking at odd and even presses.",
    "To find all the ways to pay an amount, go through the number of coins of the biggest kind one at a time and fill the "
    "rest with smaller coins. A switch that flips with every press is ON after an odd press and OFF after an even press.",
    [A("T11.C1", "Paying an Exact Amount with Coins", "Apply",
       "Students list all the ways to pay an exact amount with a limited number of coins by taking the coins of the "
       "biggest kind first.",
       teach=["Predict first: a purse has 2 coins of ₹5, 3 coins of ₹2 and 4 coins of ₹1. Is there only one way to pay "
              "₹12, or more than one?",
              "Go through the coins one kind at a time, starting with the ₹5 coins. Try 2 coins of ₹5, then 1 coin, then "
              "none.",
              "With 2 coins of ₹5, which make ₹10, ₹2 more is needed: 1 coin of ₹2, or 2 coins of ₹1. That is 2 ways.",
              "With 1 coin of ₹5, ₹7 more is needed: 3 coins of ₹2 and 1 coin of ₹1, or 2 coins of ₹2 and 3 coins of "
              "₹1. That is 2 more ways.",
              "With no ₹5 coin, all the ₹2 and ₹1 coins make only ₹10, which is not enough. So there are 4 ways in all.",
              "Rule: take the coins of the biggest kind first, try each number of them, and fill the rest with smaller "
              "coins. Keep a list so no way is missed."],
       examples=[WE("A purse has 2 coins of ₹5, 3 coins of ₹2 and 4 coins of ₹1. List all the ways to pay ₹12 exactly "
                    "(practice values).",
                    ["Try the ₹5 coins first: 2 coins, 1 coin or none.",
                     "2 coins of ₹5 make ₹10, and ₹2 more is needed. Use 1 coin of ₹2, or 2 coins of ₹1: 10 + 2 = 12.",
                     "1 coin of ₹5 makes ₹5, and ₹7 more is needed. Use 3 coins of ₹2 and 1 coin of ₹1: 5 + 6 + 1 = "
                     "12. Or use 2 coins of ₹2 and 3 coins of ₹1: 5 + 4 + 3 = 12.",
                     "With no ₹5 coin, all the ₹2 and ₹1 coins make 6 + 4 = 10 rupees, which is not enough for ₹12.",
                     "So there are 4 ways in all: 5 + 5 + 2, 5 + 5 + 1 + 1, 5 + 2 + 2 + 2 + 1 and 5 + 2 + 2 + 1 + 1 + 1.",
                     "Check: 5 + 5 + 2 = 12 and 5 + 2 + 2 + 2 + 1 = 12."],
                    "4 ways, for example 5 + 5 + 2 = 12 and 5 + 2 + 2 + 2 + 1 = 12")],
       key_terms=["coins", "exact amount", "ways", "list"], misconceptions=["M_ONE_WAY_COINS"], minutes=6),
     A("T11.C2", "ON and OFF, Press by Press", "Apply",
       "Students tell whether a switch is on or off after a given press by deciding if the press number is odd or "
       "even.",
       teach=["Predict first: a lamp is OFF. You press its switch 14 times. Is the lamp ON or OFF after the 14th press?",
              "Press 1 turns it ON, press 2 turns it OFF, press 3 turns it ON, press 4 turns it OFF. The lamp keeps "
              "taking turns.",
              "ON comes after the odd presses 1, 3, 5, 7 and so on. OFF comes after the even presses 2, 4, 6, 8 and so "
              "on.",
              "You do not have to press 14 times. 14 is even, so the lamp is OFF. For the 31st press, 31 is odd, so the "
              "lamp is ON.",
              "Rule: a switch that flips with every press is ON after an odd press and OFF after an even press. Look at "
              "whether the press number is odd or even."],
       examples=[WE("A lamp is OFF at the start and each press of its switch flips it. Is the lamp ON or OFF after the "
                    "14th press and after the 31st press? Which presses give ON? (practice values)",
                    ["Press 1 gives ON, press 2 gives OFF, press 3 gives ON. The lamp takes turns.",
                     "The odd presses 1, 3, 5, and so on give ON. The even presses 2, 4, 6, and so on give OFF.",
                     "14 is even because it ends in 4, so after the 14th press the lamp is OFF.",
                     "31 is odd because it ends in 1, so after the 31st press the lamp is ON.",
                     "Check: every 2 presses bring the lamp back to OFF, and 14 = 7 + 7 is 7 pairs of presses, so the "
                     "lamp is OFF."],
                    "OFF after the 14th press and ON after the 31st press; ON after odd presses, OFF after even "
                    "presses")],
       key_terms=["odd", "even", "ON", "OFF", "press"], misconceptions=["M_TORCH_COUNT"], minutes=5),
     DOER("T11.C3", "Pull it together and do it: Coins and a Torch", None, "Apply",
          "Students list the coin combinations that pay an exact amount and tell whether a torch is on or off after any "
          "press.",
          ["To find every way to pay an amount, go through the number of coins of the biggest kind one at a time.",
           "A switch that flips with every press is ON after an odd press and OFF after an even press.",
           "Decide whether the press number is odd or even."],
          items=[FIO("jincy", "Let Us Think: Jincy's coins",
                     "Jincy opened her piggy bank. She found 8 coins of ₹1, 9 coins of ₹2 and 5 coins of ₹5. She wants "
                     "to buy stickers worth ₹38. What possible combination of coins can she use to pay the exact "
                     "amount?",
                     ["All the coins together make 8 + 18 + 25 = 51 rupees: 8 coins of ₹1 make ₹8, 9 coins of ₹2 make "
                      "₹18 and 5 coins of ₹5 make ₹25. So ₹38 can be paid.",
                      "Go through the number of ₹5 coins, from the most (5) to the fewest, and fill the rest with ₹2 and "
                      "₹1 coins.",
                      "5 coins of ₹5 make ₹25, and ₹13 more is needed: 6 coins of ₹2 and 1 coin of ₹1, or 5 coins of ₹2 "
                      "and 3 coins of ₹1, or 4 coins of ₹2 and 5 coins of ₹1, or 3 coins of ₹2 and 7 coins of ₹1. That is "
                      "4 ways.",
                      "4 coins of ₹5 make ₹20, and ₹18 more is needed: 9 coins of ₹2, or 8 coins of ₹2 and 2 coins of "
                      "₹1, or 7 coins of ₹2 and 4 coins of ₹1, or 6 coins of ₹2 and 6 coins of ₹1, or 5 coins of ₹2 and "
                      "8 coins of ₹1. That is 5 ways.",
                      "3 coins of ₹5 make ₹15, and ₹23 more is needed: 9 coins of ₹2 and 5 coins of ₹1, or 8 coins of "
                      "₹2 and 7 coins of ₹1. That is 2 ways.",
                      "With 2 coins of ₹5, which make ₹10, ₹28 more is needed, but all the ₹2 and ₹1 coins make only 18 + "
                      "8 = 26 rupees. So it cannot be done, and fewer ₹5 coins is even less possible.",
                      "In all there are 4 + 5 + 2 = 11 combinations.",
                      "Check one: 5 coins of ₹5, 6 coins of ₹2 and 1 coin of ₹1 make 25 + 12 + 1 = 38."],
                     "Sample answer: 5 coins of ₹5, 6 coins of ₹2 and 1 coin of ₹1 make 25 + 12 + 1 = 38. There are 11 "
                     "combinations in all. Your answer may differ.",
                     kind="exercise"),
                 FIO("torch23", "Let Us Think: Raghu's torch, the 23rd press",
                     "Raghu is fond of his grandfather's torch. He starts playing with it. He presses the switch once and "
                     "the light turns ON. He presses it a second time and the light turns OFF. He presses the switch a "
                     "third time and the light turns ON. He keeps doing this several times. Will the torch be ON or OFF "
                     "after the 23rd press? How do you know?",
                     ["The torch is OFF at the start. Press 1 turns it ON, press 2 turns it OFF, press 3 turns it ON, "
                      "and so on.",
                      "The odd presses 1, 3, 5, and so on turn it ON, and the even presses 2, 4, 6, and so on turn it OFF.",
                      "23 ends in 3, so 23 is odd.",
                      "So the torch is ON after the 23rd press.",
                      "Check: 22 is even, so after 22 presses the torch is OFF, and one more press turns it ON."],
                     "The torch is ON after the 23rd press, because 23 is odd.",
                     kind="exercise"),
                 FIO("torchrule", "Let Us Think: Raghu's torch, ON and OFF presses",
                     "For what number of presses will the torch be ON? For what number of presses of the switch will the "
                     "torch be OFF?",
                     ["Press 1 gives ON, press 2 gives OFF, press 3 gives ON, press 4 gives OFF.",
                      "The torch is ON after 1, 3, 5, 7 and so on presses. These are the odd numbers.",
                      "The torch is OFF after 2, 4, 6, 8 and so on presses. These are the even numbers.",
                      "Check: after 9 presses, which is odd, the torch is ON, and after 10 presses, which is even, it is "
                      "OFF."],
                     "ON after an odd number of presses and OFF after an even number of presses.",
                     kind="exercise")],
          misconceptions=["M_ONE_WAY_COINS", "M_TORCH_COUNT"])],
    key_terms=["coins", "odd", "even", "ON", "OFF"]))

# ============================== T12 Reading Tables =========================================================
TOPICS.append(TOPIC(
    "T12", "M4", "Reading Tables", ["Let Us Think", "Math Metric Mela"], "Apply",
    "Students read a table to find the highest and lowest values and the differences between values, and decide whether "
    "an amount is enough, short or extra.",
    "A table gives facts in rows and columns. To compare two numbers in a table, subtract the smaller from the bigger to "
    "find how much more or less. For a printed number and a used number, the difference tells how many are short or "
    "extra.",
    [A("T12.C1", "Reading a Table", "Apply",
       "Students read a table to find the highest and the lowest value, the difference between two values, and a year "
       "from an age.",
       textbook=["Priyanka Mohite is the first Indian woman to climb five Himalayan peaks above 8,000 metres. In "
                 "addition to that, she has also climbed mountain peaks in other parts of the world. Read the table "
                 "below and answer the questions that follow.",
                 "The Tenzing Norgay National Adventure Award, formerly called the National Adventure Award is the "
                 "highest adventure sports honour in India. Priyanka Mohite received this award in 2020."],
       teach=["Predict first: a table lists three buses with the kilometres they travelled: 4,215, 6,380 and 5,094. How "
              "do you find which bus travelled the most, and how much more than the least?",
              "A table has rows and columns. Each row is one thing, here one bus, and each column is one fact about it, "
              "such as the distance or the year.",
              "To find the highest, compare the numbers in a column. 6,380 is more than 5,094 and 4,215, so Bus B "
              "travelled the most. The lowest is 4,215, Bus A.",
              "To find the difference between two values, subtract the smaller from the bigger: 6,380 − 4,215 = 2,165.",
              "To find a birth year from an age, take the age from the year. If a driver was 25 in 2021, the driver was "
              "born in 2021 − 25 = 1996.",
              "Rule: read the row and the column, compare to find the highest and the lowest, and subtract the smaller "
              "from the bigger to find a difference."],
       examples=[WE("A table shows three buses (practice values). Bus A travelled 4,215 km and was bought in 2015, Bus B "
                    "travelled 6,380 km and was bought in 2018, and Bus C travelled 5,094 km and was bought in 2021. "
                    "Which bus travelled the most? What is the difference between the most and the least, and between "
                    "Bus B and Bus C? A driver was 25 years old when Bus C was bought. In which year was the driver "
                    "born?",
                    ["Compare the distances: 6,380 is the most, so Bus B travelled the most. 4,215 is the least, so Bus "
                     "A travelled the least.",
                     "The difference between the most and the least is 6,380 − 4,215 = 2,165 km.",
                     "The difference between Bus B and Bus C is 6,380 − 5,094 = 1,286 km.",
                     "Bus C was bought in 2021 and the driver was 25 then, so the driver was born in 2021 − 25 = 1996.",
                     "Check: 4,215 + 2,165 = 6,380, 5,094 + 1,286 = 6,380 and 1996 + 25 = 2021."],
                    "Bus B travelled the most; 2,165 km; 1,286 km; the driver was born in 1996")],
       ncert=["mtn.intro", "mtn.award"], key_terms=["table", "row", "column", "highest", "difference"],
       minutes=6),
     A("T12.C2", "Enough, Short or Extra?", "Apply",
       "Students compare the number printed with the number needed and find how many are short or extra by "
       "subtracting.",
       textbook=["A grand Math Metric Mela was held at the district level to celebrate young math whizzes. Every "
                 "participating student was to receive a certificate of participation. The organisers got certificates "
                 "printed for each district before the Mela. The number of certificates printed and the number of "
                 "students who attended the competition in each district are as follows."],
       teach=["Predict first: 12,450 tickets were printed and 12,615 people came. Were there enough tickets?",
              "Compare the two numbers. 12,615 is more than 12,450, so more people came than tickets were printed. The "
              "tickets were not enough.",
              "How many were short? Subtract the smaller from the bigger: 12,615 − 12,450 = 165. So 165 tickets were "
              "short.",
              "On another day 9,830 tickets were printed and 9,415 people came. The tickets are more than the people, so "
              "they are enough. The extra tickets are 9,830 − 9,415 = 415.",
              "Rule: compare what was printed with what was needed. If the printed number is less, the difference is how "
              "many are short. If it is more, the difference is how many are extra."],
       examples=[WE("12,450 tickets were printed for a fair and 12,615 people came. Were the tickets enough, and how many "
                    "were short or extra? On another day 9,830 tickets were printed and 9,415 people came (practice "
                    "values).",
                    ["Compare 12,450 and 12,615. 12,450 is less than 12,615, so the tickets were not enough.",
                     "The number short is 12,615 − 12,450 = 165.",
                     "Compare 9,830 and 9,415. 9,830 is more than 9,415, so the tickets were enough.",
                     "The number extra is 9,830 − 9,415 = 415.",
                     "Check: 12,450 + 165 = 12,615 and 9,415 + 415 = 9,830."],
                    "First day: not enough, 165 short. Second day: enough, 415 extra")],
       ncert=["mela.text"], key_terms=["enough", "short", "extra", "difference"], minutes=5),
     DOER("T12.C3", "Practice: Tables", None, "Apply",
          "Students read the mountain table and the certificate table to find the highest and lowest values, the "
          "differences, and how many are short or extra.",
          ["Read the row and the column of the fact you need.",
           "Compare to find the highest and the lowest, and subtract the smaller from the bigger for a difference.",
           "If the printed number is less than the needed number the difference is how many are short, and if it is more the "
           "difference is how many are extra."],
          items=[FIO("mtn", "Let Us Think: Mountain climbing",
                     "Priyanka Mohite is the first Indian woman to climb five Himalayan peaks above 8,000 metres. Read "
                     "the table and answer the questions that follow. (a): Which is the highest peak she climbed? (b): "
                     "What is the difference in height between the highest and lowest peaks she has climbed, as per the "
                     "table? (c): What is the difference between heights of Mount Elbrus and Mount Kanchenjunga? (d): If "
                     "Priyanka was 20 years old when she summited Mount Everest in 2013, in which year was she born?",
                     ["(a): Compare the heights: 8,848 metres is the most. The highest peak is Mount Everest.",
                      "(b): The lowest peak in the table is Mount Elbrus, 5,642 metres. The difference is 8,848 − 5,642 "
                      "= 3,206 metres.",
                      "(c): Mount Kanchenjunga is 8,586 metres and Mount Elbrus is 5,642 metres. The difference is 8,586 "
                      "− 5,642 = 2,944 metres.",
                      "(d): She was 20 years old in 2013, so she was born in 2013 − 20 = 1993.",
                      "Check: 5,642 + 3,206 = 8,848, 5,642 + 2,944 = 8,586 and 1993 + 20 = 2013."],
                     "(a): Mount Everest; (b): 3,206 metres; (c): 2,944 metres; (d): 1993",
                     kind="exercise",
                     q_figure="A table of seven mountains with their heights in metres and the year climbed: Mount "
                              "Kanchenjunga 8,586 in 2022, Mount Everest 8,848 in 2013, Mount Makalu 8,485 in 2019, Mount "
                              "Lhotse 8,516 in 2018, Mount Kilimanjaro 5,895 in 2016, Mount Elbrus 5,642 in 2017 and "
                              "Mount Annapurna I 8,091 in 2021."),
                 FIO("mela", "Math Metric Mela: certificates",
                     "For each district, find out if the number of certificates were sufficient? If insufficient, "
                     "calculate how many certificates fell short. If extra, calculate how many certificates were in "
                     "excess.",
                     ["Chittoor: 18,225 printed and 18,104 attended. 18,225 is more than 18,104, so the certificates were "
                      "sufficient.",
                      "The extra certificates are 18,225 − 18,104 = 121.",
                      "Jaunpur: 19,043 printed and 19,265 attended. 19,043 is less than 19,265, so the certificates were "
                      "not sufficient.",
                      "The certificates that fell short are 19,265 − 19,043 = 222.",
                      "Raigad: 20,863 printed and 19,974 attended. 20,863 is more than 19,974, so the certificates were "
                      "sufficient.",
                      "The extra certificates are 20,863 − 19,974 = 889.",
                      "Check: 18,104 + 121 = 18,225, 19,043 + 222 = 19,265 and 19,974 + 889 = 20,863."],
                     "Chittoor: sufficient, 121 extra. Jaunpur: not sufficient, 222 short. Raigad: sufficient, 889 extra.",
                     kind="exercise",
                     q_figure="A table of three districts with the certificates printed and the students attended: "
                              "Chittoor, A.P. 18,225 and 18,104; Jaunpur, U.P. 19,043 and 19,265; Raigad, Maharashtra "
                              "20,863 and 19,974.")])],
    key_terms=["table", "difference", "enough", "short", "extra"]))

# ============================== T13 Chapter Revision (summary) =============================================
TOPICS.append(TOPIC(
    "T13", "M4", "Chapter Revision: We the Travellers - II", ["Chapter summary"], "Understand",
    "",
    "The chapter's ideas in one drive along the road trip: swapping to balance sums, adding and subtracting with place "
    "value, the link between them, consecutive sums, large numbers, journey problems, round number tricks, "
    "palindromes, grids, even and odd, coins and a switch, and tables.",
    [A("T13.C1", "Chapter Revision: We the Travellers - II", "Understand",
       "",
       teach=["Predict first: you have driven the whole road trip, from the number cards to the tables. Can you say one "
              "idea from each stop? Read the lines below and tick each idea you remembered.",
              "Swapping: when a smaller number and a bigger number change groups, one sum goes up and the other goes "
              "down by the same amount. To make two sums equal, swap two numbers whose difference is half of the gap.",
              "Check: the groups 2, 6, 9 and 4, 7, 10 add up to 17 and 21. Swap 2 and 4 and both groups add up to 19.",
              "Adding: add one place at a time from the ones, and regroup 10 as 1 of the next place. For 67 + 58: 7 + 8 = "
              "15, then 6 + 5 + 1 = 12, so the sum is 125.",
              "Easier ways: a number just below a round number can be added by adding the round number and taking the "
              "extra back. 54 + 98 = 54 + 100 − 2 = 152.",
              "Subtracting and the link: regroup 1 ten as 10 ones when there are too few ones, and check by adding. "
              "72 − 38 = 34 and 38 + 34 = 72. From 35 + 28 = 63 you also know 63 − 28 = 35.",
              "Consecutive numbers: the difference between successive sums is the number of numbers added, and pairs "
              "from the two ends make the same total. 41 + 42 + 43 + 44 + 45 = 5 × 43 = 215.",
              "Large numbers: the same steps as small numbers, with the digits aligned. 3,486 + 2,729 = 6,215 and 6,402 "
              "− 2,758 = 3,644.",
              "Journey problems: read one step at a time, add for gets and totals, take away for spends and what is left, "
              "and estimate first by rounding up. 15,000 − 4,250 + 2,000 − 3,160 = 9,590.",
              "Round numbers: make nines and add 1 to reach 100, and take away 10 or 100 then add 1 to take away 9 or "
              "99. 46 + 54 = 100 and 52 − 9 = 43.",
              "Palindromes: a palindrome number reads the same both ways. 2,442 is one, and the palindromes from 300 to "
              "340 are 303, 313, 323 and 333.",
              "Grids: the arrows tell where the smallest and the biggest number go. Check every row and every column.",
              "Even and odd: pairs with none left over mean even, and one left over means odd. Even plus even is even, "
              "odd plus odd is even and odd plus even is odd.",
              "Coins and the switch: list the ways one kind of coin at a time. A switch that flips with each press is ON "
              "after an odd press and OFF after an even press.",
              "Tables: subtract the smaller from the bigger to find a difference. 6,380 − 4,215 = 2,165. If the number "
              "printed is less than the number needed, the difference is how many are short.",
              "Check: is 17 + 6 odd or even? 17 + 6 = 23, which is odd, because 17 is odd and 6 is even.",
              "Check: find 87 + ___ = 100. 87 needs 12 to make 99, so the blank is 13.",
              "Check: add 6 + 7 + 8 + 9 by pairs. 6 + 9 = 15 and 7 + 8 = 15, so the sum is 15 + 15 = 30."],
       ncert=["summary"], key_terms=["swap", "place value", "regroup", "consecutive numbers", "even", "odd"], minutes=6,
       enrichment=True)],
    topic_type="summary"))
