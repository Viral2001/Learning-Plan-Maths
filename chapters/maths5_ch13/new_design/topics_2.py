# -*- coding: utf-8 -*-
"""Topics T3 and T4 (module M2: Common Multiples and Common Factors). Common multiples with the animals' jumps on a
number line, and common factors with Mowgli's jumps on the trail. Every teaching concept has one worked example with the
plan's own numbers; every book question is an FIO item of its topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T3 Common Multiples =======================================================
TOPICS.append(TOPIC(
    "T3", "M2", "Common Multiples", ["Animal Jumps", "Let Us Do (common multiples)"], "Apply",
    "Students find common multiples of two numbers with jumps on a number line and with lists, and use the pattern of "
    "the first common multiple to write more of them.",
    "Two animals jump from 0 with different jump sizes. The numbers both of them touch are the common multiples. The "
    "first common multiple tells the rest: they are its multiples.",
    [A("T3.C1", "Common Multiples", "Apply",
       "Students find the numbers two jumpers both touch on a number line, name them common multiples, and say which "
       "one is the first common multiple.",
       textbook=["A rabbit takes a jump of 4 each time. A frog takes a jump of 3 each time. Use the number line to "
                 "figure out the numbers they will both touch. If the rabbit and the frog start from 0, the numbers "
                 "both of them will touch are called the common multiples of 3 and 4.",
                 "12 is the first common multiple of 3 and 4.",
                 "Let us write the multiples of two numbers, 4 and 6.",
                 "Multiples of 4: 4, 8, 12, 16, ...",
                 "Multiples of 6: 6, 12, 18, ..."],
       teach=["Predict first: Robby the rabbit jumps 2 at a time and Deeku the deer jumps 5 at a time. Both start at "
              "0. Which numbers will both of them touch?",
              "Robby touches 2, 4, 6, 8, 10, 12 and so on: the multiples of 2. Deeku touches 5, 10, 15, 20 and so on: "
              "the multiples of 5.",
              "Both touch 10, and then 20, and then 30. The numbers both of them touch are called the common "
              "multiples of 2 and 5.",
              "10 is the first common multiple of 2 and 5.",
              "Another way is to write the multiples of each number and circle the numbers that are in both lists. "
              "Multiples of 4 are 4, 8, 12, 16 and multiples of 6 are 6, 12, 18, so 12 is in both lists.",
              "Rule: a number that is a multiple of both numbers is a common multiple of them."],
       examples=[WE("Robby the rabbit jumps 2 at a time and Deeku the deer jumps 5 at a time. Both start at 0. Which "
                    "numbers up to 30 will both of them touch?",
                    ["Robby touches the multiples of 2: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30.",
                     "Deeku touches the multiples of 5: 5, 10, 15, 20, 25, 30.",
                     "The numbers in both lists are 10, 20 and 30. These are the common multiples of 2 and 5 up to "
                     "30.",
                     "10 is the first common multiple: 2 × 5 = 10, and Robby needs 5 jumps while Deeku needs 2.",
                     "Check: 20 ÷ 2 = 10 and 20 ÷ 5 = 4, both exact, so 20 is a multiple of both."],
                    "10, 20 and 30. The first common multiple of 2 and 5 is 10")],
       ncert=["cm.def34", "cm.lists46"], key_terms=["common multiples", "jumps", "number line", "first common multiple"],
       misconceptions=["M_CM_ONLY_PRODUCT", "M_CF_CM_MIX"], minutes=6),
     A("T3.C2", "The Pattern in Common Multiples", "Analyze",
       "Students describe the pattern of the common multiples of two numbers and use the first common multiple to "
       "write the next ones.",
       textbook=["12 is the first common multiple of 3 and 4. What are some other common multiples of 3 and 4?",
                 "What do you notice about the common multiples of 3 and 4? Discuss in class.",
                 "A spider takes a jump of 3 every time. A grasshopper takes a jump of 6 each time. Use the number line "
                 "to find the common multiples of 3 and 6.",
                 "6 and 12 are two common multiples of 3 and 6. You can continue the pattern to find more common "
                 "multiples. What do you notice about the common multiples of 3 and 6? Discuss.",
                 "What do you notice about the common multiples of different pairs of numbers? Discuss in class."],
       teach=["Predict first: the first common multiple of 4 and 10 is 20. What are the next common multiples, and how "
              "far apart are they?",
              "Robby (jumps of 4) and Deeku (jumps of 10) both touch 20, then 40, then 60. Each is 20 more than the "
              "one before.",
              "The common multiples 20, 40, 60 are the multiples of the first common multiple, 20.",
              "There is no last common multiple: the animals can keep jumping, so there are always more.",
              "When one number is a multiple of the other, such as 4 and 12, the common multiples are the multiples "
              "of the bigger number: 12, 24, 36, and so on.",
              "Rule: the common multiples of two numbers are the multiples of their first common multiple."],
       examples=[WE("Robby jumps 6 at a time and Deeku jumps 15 at a time from 0. Find three numbers both touch, and "
                    "say what you notice.",
                    ["Robby touches 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90.",
                     "Deeku touches 15, 30, 45, 60, 75, 90.",
                     "The numbers in both lists are 30, 60 and 90. The first common multiple is 30.",
                     "30 + 30 = 60 and 60 + 30 = 90, so each common multiple is 30 more than the one before.",
                     "30 × 1 = 30, 30 × 2 = 60 and 30 × 3 = 90, so they are the multiples of the first common "
                     "multiple, 30.",
                     "Check: 60 ÷ 6 = 10 and 60 ÷ 15 = 4; 90 ÷ 6 = 15 and 90 ÷ 15 = 6. All exact."],
                    "30, 60 and 90. They are the multiples of 30, the first common multiple")],
       ncert=["cm.spider", "cm.notice34", "cm.notice36", "cm.noticeQ1"],
       key_terms=["common multiples", "pattern", "first common multiple"],
       misconceptions=["M_CM_ONLY_PRODUCT", "M_FIRST_ONLY"], minutes=5),
     DOER("T3.C3", "Practice: Common Multiples", "jump_together", "Apply",
          "Students find common multiples of pairs of numbers by jumping and by lists, and decide which animal lands "
          "on a number at the end of the road.",
          ["Numbers both animals touch are the common multiples of their jump sizes.",
           "The first common multiple tells all the others: they are its multiples.",
           "A number is touched by a jumper only if it is a multiple of the jump size."],
          items=[FIO("cm.more34", "Animal Jumps: more common multiples of 3 and 4",
                     "12 is the first common multiple of 3 and 4. What are some other common multiples of 3 and 4? "
                     "You can continue the number line or take help from the times tables of 3 and 4.",
                     ["The rabbit's jumps of 4 touch 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48.",
                      "The frog's jumps of 3 touch 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48.",
                      "The numbers in both lists are 12, 24, 36 and 48.",
                      "Keep going: 4 × 15 = 60 and 3 × 20 = 60, so 60 is a common multiple too.",
                      "The common multiples are 12, 24, 36, 48, 60 and so on. Each one is 12 more than the one before.",
                      "Check: 36 ÷ 3 = 12 and 36 ÷ 4 = 9, both exact."],
                     "24, 36, 48, 60 and so on: the multiples of 12.",
                     kind="prompt",
                     q_figure="A number line from 0 to 12 with a rabbit hopping in jumps of 4 and a frog hopping in "
                              "jumps of 3, and the number 12 in a box.",
                     s_figure="A number line from 0 to 48 with the rabbit's landings and the frog's landings, and the "
                              "numbers 12, 24, 36 and 48 where both land marked in a box."),
                 FIO("cm.list46", "Animal Jumps: common multiples of 4 and 6",
                     "Let us write the multiples of two numbers, 4 and 6. Multiples of 4: 4, 8, 12, 16, ... Multiples "
                     "of 6: 6, 12, 18, ... 12 and 24 are two of the common multiples of 4 and 6. List a few more.",
                     ["Multiples of 4: 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48.",
                      "Multiples of 6: 6, 12, 18, 24, 30, 36, 42, 48.",
                      "The numbers in both lists are 12, 24, 36 and 48. Your maths book gave 12 and 24, so a few more "
                      "are 36 and 48.",
                      "More: 60 and 72, because 4 × 15 = 60, 6 × 10 = 60, 4 × 18 = 72 and 6 × 12 = 72.",
                      "Check: 36 ÷ 4 = 9 and 36 ÷ 6 = 6, both exact."],
                     "36, 48, 60 and 72: the multiples of 12.",
                     kind="prompt",
                     s_figure="Two lists, multiples of 4 and multiples of 6, with the numbers in both lists circled."),
                 FIO("LUD.Q1", "Let Us Do (common multiples), Q1",
                     "Find 5 common multiples of the following pairs of numbers. (a) 2 and 3 (b) 5 and 8 (c) 2 and 4 "
                     "(d) 3 and 9 (e) 5 and 10 (f) 9 and 12 (g) 8 and 12 (h) 6 and 8 (i) 6 and 9",
                     ["(a): the first common multiple of 2 and 3 is 6, because 2 × 3 = 6. Five common multiples: 6, 12, 18, "
                      "24, 30.",
                      "(b): the multiples of 8 are 8, 16, 24, 32, 40, and 40 is the first one that is also a multiple "
                      "of 5, because 5 × 8 = 40. Five common multiples: 40, 80, 120, 160, 200.",
                      "(c): 4 is a multiple of 2, so the common multiples are the multiples of 4: 4, 8, 12, 16, 20.",
                      "(d): 9 is a multiple of 3, so the common multiples are the multiples of 9: 9, 18, 27, 36, 45.",
                      "(e): 10 is a multiple of 5, so the common multiples are the multiples of 10: 10, 20, 30, 40, 50.",
                      "(f): the multiples of 12 are 12, 24, 36, and 36 is also a multiple of 9, because 9 × 4 = 36. Five "
                      "common multiples: 36, 72, 108, 144, 180.",
                      "(g): 24 is a multiple of both: 8 × 3 = 24 and 12 × 2 = 24. Five common multiples: 24, 48, 72, "
                      "96, 120.",
                      "(h): 24 is a multiple of both: 6 × 4 = 24 and 8 × 3 = 24. Five common multiples: 24, 48, 72, "
                      "96, 120.",
                      "(i): 18 is a multiple of both: 6 × 3 = 18 and 9 × 2 = 18. Five common multiples: 18, 36, 54, "
                      "72, 90.",
                      "Check: 108 ÷ 9 = 12 and 108 ÷ 12 = 9; 200 ÷ 5 = 40 and 200 ÷ 8 = 25. All exact."],
                     "Sample answer, the first common multiple: (a): 6; (b): 40; (c): 4; (d): 9; (e): 10; (f): 36; "
                     "(g): 24; (h): 24; (i): 18. Add its next multiples. Your answer may differ.",
                     kind="exercise"),
                 FIO("LUD.Q2", "Let Us Do (common multiples), Q2",
                     "Food is available at the end of a cobbled road. Robby, the rabbit, takes a jump of 4 each time. "
                     "Deeku, the deer, takes a jump of 6 each time. They both start at 0. Will both Robby and Deeku "
                     "reach the food? Who will reach first? How do you know? Explain your answer.",
                     ["The stones of the road are numbered 0 to 64 and the food is at the end of the road, so each "
                      "animal must land on stone 64.",
                      "Robby jumps 4 at a time and lands on the multiples of 4: 4, 8, 12, ..., 60, 64. 4 × 16 = 64, so "
                      "Robby lands on 64 after 16 jumps.",
                      "Deeku jumps 6 at a time and lands on the multiples of 6: 6, 12, 18, ..., 54, 60, 66. 6 × 10 = "
                      "60 and 6 × 11 = 66, so Deeku lands on 60 and then jumps past 64 to 66.",
                      "64 is a multiple of 4 but not a multiple of 6, so only Robby reaches the food.",
                      "Robby reaches the food first, because Deeku does not land on it at all. Together they land on "
                      "12, 24, 36, 48 and 60, the common multiples of 4 and 6.",
                      "Check: 16 × 4 = 64, but 64 is not in the multiples of 6: 6 × 10 = 60 and 6 × 11 = 66."],
                     "No, only Robby reaches the food: 64 = 4 × 16, but 64 is not a multiple of 6. Robby is first.",
                     kind="exercise",
                     q_figure="A winding cobbled road of stones numbered from 0 to 64, with Robby the rabbit and "
                              "Deeku the deer at stone 0 and the food after stone 64.",
                     s_figure="The same road with Robby's landings on 4, 8, ..., 64 marked in blue and Deeku's "
                              "landings on 6, 12, ..., 60 marked in orange, and Deeku's jump from 60 to 66 passing "
                              "over stone 64.")],
          misconceptions=["M_CM_ONLY_PRODUCT", "M_CF_CM_MIX"])],
    key_terms=["common multiples", "first common multiple", "jumps"]))

# ============================== T4 Common Factors =========================================================
TOPICS.append(TOPIC(
    "T4", "M2", "Common Factors", ["Mowgli's Trail", "Let Us Do (jumps and factors)"], "Apply",
    "Students use jumps from 0 to tell when a jump size is a factor of a number, and find the common factors of two "
    "or more numbers.",
    "A jump of n steps from 0 lands exactly on a number when n is a factor of it. A jump size that lands on several "
    "numbers is a common factor of them, and 1 is always one of them.",
    [A("T4.C1", "Jumps That Land on a Number", "Understand",
       "Students decide whether a jump size lands exactly on a number, and say that it does when the jump size is a "
       "factor of that number.",
       teach=["Predict first: Mowgli jumps 4 steps at a time from 0. His friends live at 8, 14, 20 and 26. Which of "
              "them can he land on?",
              "His jumps land on 4, 8, 12, 16, 20, 24, 28. So he lands on 8 and on 20, but he skips 14 and 26.",
              "He lands on a number only when a whole number of jumps of 4 makes it: 8 = 4 × 2 and 20 = 4 × 5. That "
              "means 4 divides 8 and 20 completely, so 4 is a factor of 8 and of 20.",
              "14 and 26 are not multiples of 4, so he jumps over them: 12 then 16, and 24 then 28.",
              "A jump size that lands on several numbers is a common factor of those numbers: 4 is a common factor of "
              "8 and 20.",
              "Rule: a jump of n steps from 0 lands exactly on a number when n is a factor of the number."],
       examples=[WE("Mowgli jumps 4 steps at a time from 0. Which of the places 8, 14, 20 and 26 can he land on? What "
                    "can you say about 4 and the places he lands on?",
                    ["His landing places are the multiples of 4: 4, 8, 12, 16, 20, 24, 28.",
                     "8 is on the list: 4 × 2 = 8, so he lands on 8 after 2 jumps.",
                     "14 is not on the list: he lands on 12 and then on 16, so he skips 14.",
                     "20 is on the list: 4 × 5 = 20, so he lands on 20 after 5 jumps.",
                     "26 is not on the list: he lands on 24 and then on 28, so he skips 26.",
                     "4 divides 8 and 20 completely, so 4 is a common factor of 8 and 20.",
                     "Check: 8 ÷ 4 = 2 and 20 ÷ 4 = 5, both exact."],
                    "He lands on 8 and 20, and skips 14 and 26. 4 is a common factor of 8 and 20")],
       key_terms=["jump", "factor", "land", "number"],
       misconceptions=["M_JUMP_NEAR", "M_FACTOR_MULTIPLE"], minutes=5),
     A("T4.C2", "Common Factors of Two Numbers", "Apply",
       "Students list the factors of two numbers, pick the common factors, and say which jump sizes reach both "
       "numbers.",
       textbook=["A common factor of two or more numbers exactly divides each of the numbers.",
                 "What do you notice about the common factors of different pairs of numbers. Discuss in class."],
       teach=["Predict first: which jump sizes land on both 18 and 30? Try 2, 4 and 6.",
              "A common factor of two or more numbers exactly divides each of the numbers. It is a jump size that "
              "lands on all of them.",
              "To find them, list the factors of each number, then pick the numbers that are in both lists.",
              "1 is always a common factor, because a jump of 1 lands on every number.",
              "A common factor can never be more than the smaller number, and some pairs have only 1 in common.",
              "Rule: the common factors of two numbers are the numbers that are in both lists of factors."],
       examples=[WE("Find the common factors of 18 and 30, and say which jump sizes reach both numbers.",
                    ["List the factors of 18 from its arrays 1 × 18, 2 × 9 and 3 × 6: 1, 2, 3, 6, 9, 18.",
                     "List the factors of 30 from its arrays 1 × 30, 2 × 15, 3 × 10 and 5 × 6: 1, 2, 3, 5, 6, 10, 15, "
                     "30.",
                     "Pick the numbers that are in both lists: 1, 2, 3 and 6.",
                     "Each of these is a jump size that lands on both 18 and 30. Jumps of 6 land on 6, 12, 18, 24, "
                     "30. Jumps of 9 land on 18 but skip 30: 9, 18, 27, 36.",
                     "1 is always a common factor, because a jump of 1 lands on every number.",
                     "Check: 18 ÷ 6 = 3 and 30 ÷ 6 = 5, both exact."],
                    "The common factors of 18 and 30 are 1, 2, 3 and 6")],
       ncert=["cf.def", "cf.notice7"], key_terms=["common factors", "factors", "two numbers"],
       misconceptions=["M_CF_CM_MIX", "M_CF_BIGGEST_ONLY"], minutes=5),
     DOER("T4.C3", "Practice: Common Factors on the Trail", "trail_jumper", "Apply",
          "Students find which friends a jump size reaches on the trail, and list the common factors of two numbers "
          "and of pairs of numbers.",
          ["A jump size lands on a number when it is a factor of the number.",
           "Common factors are the jump sizes that land on every number of the list.",
           "1 is a common factor of every list of numbers."],
          ncert=["trail.answer2"],
          items=[FIO("LUD.Q3", "Let Us Do (jumps and factors), Q3",
                     "Mowgli's friends live along the trail on the marked places below. Which of his friends will he "
                     "be able to visit, if he jumps by 2 steps starting from 0?",
                     ["Jumps of 2 from 0 land on 2, 4, 6, 8 and so on: the even numbers, the multiples of 2.",
                      "The friends live at these places: ant 4, spider 9, frog 12, bird 14, Kaa 21, Sher Khan 25, "
                      "Baloo 30, Akela 35, deer 39, rabbit 50, monkey 57.",
                      "4 = 2 × 2, 12 = 2 × 6, 14 = 2 × 7, 30 = 2 × 15 and 50 = 2 × 25, so a jump of 2 lands on all five "
                      "of these places.",
                      "9, 21, 25, 35, 39 and 57 are odd numbers, so jumps of 2 skip them.",
                      "Mowgli can visit the ant, the frog, the bird, Baloo and the rabbit. 2 is a common factor of 4, "
                      "12, 14, 30 and 50.",
                      "Check: 30 ÷ 2 = 15 and 50 ÷ 2 = 25, both exact."],
                     "The ant (4), frog (12), bird (14), Baloo (30) and rabbit (50): 2 is a common factor of 4, 12, "
                     "14, 30 and 50.",
                     kind="exercise",
                     q_figure="A winding trail of numbered stones from 0 to 60 with Mowgli at 0 and his friends at "
                              "these places: the ant at 4, the spider at 9, the frog at 12, the bird at 14, Kaa the "
                              "snake at 21, Sher Khan the tiger at 25, Baloo the bear at 30, Akela the wolf at 35, the "
                              "deer at 39, the rabbit at 50 and the monkey at 57.",
                     s_figure="The same trail with Mowgli's landings 2, 4, 6, ... marked, and the ant, the frog, the "
                              "bird, Baloo and the rabbit lit up."),
                 FIO("trail.three", "Mowgli's Trail: jumps of 3 steps",
                     "Which of his friends will he be able to meet if he jumps by 3 steps? 3 is a common factor of "
                     "the numbers ___.",
                     ["Jumps of 3 from 0 land on 3, 6, 9, 12, 15, 18, 21, 24, 27, 30 and so on: the multiples of 3.",
                      "Check each friend's place: 9 = 3 × 3, 12 = 3 × 4, 21 = 3 × 7, 30 = 3 × 10, 39 = 3 × 13 and "
                      "57 = 3 × 19.",
                      "The places 4, 14, 25, 35 and 50 are not multiples of 3, so he jumps over them.",
                      "He meets the spider, the frog, Kaa, Baloo, the deer and the monkey.",
                      "Check: 39 ÷ 3 = 13 and 57 ÷ 3 = 19, both exact."],
                     "The spider (9), frog (12), Kaa (21), Baloo (30), deer (39) and monkey (57): 3 is a common "
                     "factor of 9, 12, 21, 30, 39 and 57.",
                     kind="prompt",
                     s_figure="The trail with jumps of 3 marked and the spider, the frog, Kaa, Baloo, the deer and the "
                              "monkey lit up."),
                 FIO("trail.five", "Mowgli's Trail: jumps of 5 steps",
                     "Which numbers will he touch if he jumps by 5 steps? ___. 5 is a common factor of the numbers "
                     "___.",
                     ["Jumps of 5 from 0 touch 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55 and 60. The trail ends at 60.",
                      "Friends on these numbers: 25 = 5 × 5 (Sher Khan), 30 = 5 × 6 (Baloo), 35 = 5 × 7 (Akela) and "
                      "50 = 5 × 10 (the rabbit).",
                      "No other friend is on a multiple of 5: 4, 9, 12, 14, 21, 39 and 57 are not.",
                      "So he touches 5, 10, 15, ..., 60, and 5 is a common factor of the friends' numbers 25, 30, 35 "
                      "and 50.",
                      "Check: 25 ÷ 5 = 5 and 35 ÷ 5 = 7, both exact."],
                     "He touches 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55 and 60. 5 is a common factor of 25, 30, "
                     "35 and 50.",
                     kind="prompt"),
                 FIO("trail.ten", "Mowgli's Trail: jumps of 10 steps",
                     "Which numbers will he touch if he jumps by 10 steps? ___. 10 is a common factor of the numbers "
                     "___.",
                     ["Jumps of 10 from 0 touch 10, 20, 30, 40, 50 and 60. The trail ends at 60.",
                      "Friends on these numbers: 30 = 10 × 3 (Baloo) and 50 = 10 × 5 (the rabbit).",
                      "No other friend is on a multiple of 10.",
                      "Check: 30 ÷ 10 = 3 and 50 ÷ 10 = 5, both exact."],
                     "He touches 10, 20, 30, 40, 50 and 60. 10 is a common factor of 30 and 50.",
                     kind="prompt"),
                 FIO("LUD.Q4", "Let Us Do (jumps and factors), Q4",
                     "Let us find some common factors of the numbers 24 and 36. Note that all jumps in the following "
                     "questions start from 0. (a) Can we jump by 2 steps at a time to reach both 24 and 36? Yes/No. 2 "
                     "is/is not a common factor of 24 and 36. (b) Can we jump by 3 steps at a time to reach both 24 "
                     "and 36? Yes/No. 3 is/is not a common factor of 24 and 36. (c) Can we jump by 4 steps at a time "
                     "to reach both 24 and 36? Yes/No. 4 is/is not a common factor of 24 and 36. (d) What other jumps "
                     "can we take to reach both 24 and 36? (e) How many common factors can you find for 24 and 36? "
                     "List them. (f) What about jumping by 1 step each time to reach both 24 and 36?",
                     ["(a): 2 × 12 = 24 and 2 × 18 = 36, so jumps of 2 reach both. Yes, 2 is a common factor of 24 "
                      "and 36.",
                      "(b): 3 × 8 = 24 and 3 × 12 = 36, so jumps of 3 reach both. Yes, 3 is a common factor.",
                      "(c): 4 × 6 = 24 and 4 × 9 = 36, so jumps of 4 reach both. Yes, 4 is a common factor.",
                      "(d): jumps of 6 reach both, because 6 × 4 = 24 and 6 × 6 = 36, and so do jumps of 12, because "
                      "12 × 2 = 24 and 12 × 3 = 36. Jumps of 8 reach 24 but not 36, and jumps of 9 reach 36 but not 24. The other "
                      "jumps are 1, 6 and 12.",
                      "(e): the factors of 24 are 1, 2, 3, 4, 6, 8, 12, 24. The factors of 36 are 1, 2, 3, 4, 6, 9, "
                      "12, 18, 36. In both lists: 1, 2, 3, 4, 6, 12. That is 6 common factors.",
                      "(f): a jump of 1 lands on every number: 1 × 24 = 24 and 1 × 36 = 36. Yes, 1 is a common factor "
                      "of 24 and 36.",
                      "Check: 12 × 2 = 24 and 12 × 3 = 36, so 12, the biggest common factor, reaches both."],
                     "(a): Yes; (b): Yes; (c): Yes; (d): 1, 6 and 12; (e): 6 common factors: 1, 2, 3, 4, 6, 12; "
                     "(f): Yes, 1 is a common factor.",
                     kind="exercise",
                     s_figure="Two lists, the factors of 24 and the factors of 36, with the six numbers that are in "
                              "both lists circled."),
                 FIO("LUD.Q5", "Let Us Do (jumps and factors), Q5",
                     "What are the common factors of 12 and 13?",
                     ["The factors of 12 are 1, 2, 3, 4, 6, 12.",
                      "13 has only the array 1 × 13, so its factors are 1 and 13.",
                      "The only number in both lists is 1.",
                      "1 and the number itself are always factors of any number, so 1 is always a common factor.",
                      "Check: a jump of 3 lands on 12, because 3 × 4 = 12, but not on 13, because the next landing is 15."],
                     "Only 1. The common factor of 12 and 13 is 1.",
                     kind="exercise"),
                 FIO("LUD.Q6", "Let Us Do (jumps and factors), Q6",
                     "Find which of the following numbers can be reached by jumps of 4 steps? 4 is the common factor "
                     "of the numbers ___.",
                     ["Jumps of 4 land on the multiples of 4: 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48.",
                      "10 is not a multiple of 4: 4 × 2 = 8 and 4 × 3 = 12, so the jumps go from 8 to 12 and skip 10.",
                      "16 = 4 × 4, so a jump of 4 reaches 16.",
                      "27 is not a multiple of 4: 4 × 6 = 24 and 4 × 7 = 28, so 27 is skipped.",
                      "36 = 4 × 9 and 48 = 4 × 12, so both can be reached. 0 is the starting place.",
                      "Check: 16 ÷ 4 = 4, 36 ÷ 4 = 9 and 48 ÷ 4 = 12, all exact."],
                     "16, 36 and 48 can be reached. 4 is a common factor of 16, 36 and 48.",
                     kind="exercise",
                     q_figure="A number line with the numbers 0, 10, 16, 27, 36 and 48 marked.",
                     s_figure="The same number line with hops of 4 landing on 16, 36 and 48 and skipping 10 and 27."),
                 FIO("LUD.Q7", "Let Us Do (jumps and factors), Q7",
                     "Find the common factors of the following pairs of numbers. (a) 12 and 16 (b) 8 and 12 (c) 4 and "
                     "16 (d) 2 and 9 (e) 3 and 5 (f) 12 and 15 (g) 20 and 5 (h) 9 and 21 (i) 6 and 27",
                     ["(a): the factors of 12 are 1, 2, 3, 4, 6, 12 and of 16 are 1, 2, 4, 8, 16. Common: 1, 2, 4.",
                      "(b): the factors of 8 are 1, 2, 4, 8 and of 12 are 1, 2, 3, 4, 6, 12. Common: 1, 2, 4.",
                      "(c): the factors of 4 are 1, 2, 4 and of 16 are 1, 2, 4, 8, 16. Common: 1, 2, 4.",
                      "(d): the factors of 2 are 1, 2 and of 9 are 1, 3, 9. Common: 1.",
                      "(e): the factors of 3 are 1, 3 and of 5 are 1, 5. Common: 1.",
                      "(f): the factors of 12 are 1, 2, 3, 4, 6, 12 and of 15 are 1, 3, 5, 15. Common: 1, 3.",
                      "(g): the factors of 20 are 1, 2, 4, 5, 10, 20 and of 5 are 1, 5. Common: 1, 5.",
                      "(h): the factors of 9 are 1, 3, 9 and of 21 are 1, 3, 7, 21. Common: 1, 3.",
                      "(i): the factors of 6 are 1, 2, 3, 6 and of 27 are 1, 3, 9, 27. Common: 1, 3.",
                      "Check: 4 × 3 = 12 and 4 × 4 = 16, so jumps of 4 reach both 12 and 16; 3 × 3 = 9 and "
                      "3 × 7 = 21, so jumps of 3 reach both 9 and 21."],
                     "(a): 1, 2, 4; (b): 1, 2, 4; (c): 1, 2, 4; (d): 1; (e): 1; (f): 1, 3; (g): 1, 5; (h): 1, 3; "
                     "(i): 1, 3",
                     kind="exercise")],
          misconceptions=["M_CF_CM_MIX", "M_CF_BIGGEST_ONLY", "M_JUMP_NEAR"])],
    key_terms=["common factors", "jumps", "factor"]))
