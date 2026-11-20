# -*- coding: utf-8 -*-
"""Topics T5 and T6 (module M3: Using Factors and Multiples). Checking statements, sorting numbers by the factors 2, 5
and 10 with the book's last four questions, and the chapter revision (a text summary with short concept checks). Every
teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of the DOER of
its topic, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T5 Factors and Multiples at Work ==========================================
TOPICS.append(TOPIC(
    "T5", "M3", "Factors and Multiples at Work", ["Let Us Do (factors and multiples at work)"], "Apply",
    "Students test statements about factors and multiples with examples, and sort numbers by whether 2, 5 and 10 are "
    "their factors.",
    "A statement is false if one example breaks it, and true only if there is a reason it always works. A number is "
    "divisible by 2, 5 or 10 when that number is one of its factors.",
    [A("T5.C1", "Checking a Statement", "Analyze",
       "Students decide whether a statement about factors and multiples is true or false by testing it on examples, "
       "and give an example that makes a false statement fail.",
       teach=["Predict first: a friend says that every multiple of 5 ends in 5. Is that always true? Try 5, 10, 15 and "
              "20.",
              "5 and 15 end in 5, but 10 and 20 end in 0. One example that fails is enough to show that the statement "
              "is false.",
              "To show that a statement is true for every number, a few examples are not enough. Look for the reason "
              "that it always works.",
              "A reason for a true statement: every multiple of 10 is a multiple of 5, because 10 = 5 × 2, so each 10 "
              "is made of two 5s.",
              "Rule: one example that fails shows that a statement is false. To call a statement true, give the "
              "reason it always works."],
       examples=[WE("Check two statements. (1) Every multiple of 4 is also a multiple of 2. (2) Every multiple of 6 is "
                    "also a multiple of 4.",
                    ["(1): write some multiples of 4: 4, 8, 12, 16, 20. Each one is also a multiple of 2: 2 × 2 = 4, "
                     "2 × 4 = 8, 2 × 6 = 12, 2 × 8 = 16 and 2 × 10 = 20.",
                     "Why it always works: 4 = 2 × 2, so every multiple of 4 is made of 2s. Statement (1) is true.",
                     "(2): write some multiples of 6: 6, 12, 18, 24. 12 and 24 are multiples of 4, because 4 × 3 = 12 and "
                     "4 × 6 = 24, but 6 is not: 4 × 1 = 4 and 4 × 2 = 8.",
                     "One multiple of 6 that is not a multiple of 4 is enough. 6 is one, so statement (2) is false.",
                     "Check: 18 is another example. 4 × 4 = 16 and 4 × 5 = 20, so 18 is not a multiple of 4."],
                    "(1) is true because 4 = 2 × 2. (2) is false: 6 is a multiple of 6 but not of 4")],
       key_terms=["statement", "true", "false", "example"],
       misconceptions=["M_EVEN_FACTORS", "M_ODD_MULTIPLES"], minutes=5),
     A("T5.C2", "Divisible by 2, 5 and 10", "Apply",
       "Students tell whether a number is divisible by 2, by 5 and by 10 by checking which of these are its factors, "
       "and explain why a number divisible by 10 is divisible by 2 and 5.",
       teach=["Predict first: is 60 divisible by 2? By 5? By 10? And is 35 divisible by 10?",
              "A number is divisible by 2 when 2 divides it completely, that is, when 2 is a factor of it. The same "
              "is true for 5 and for 10.",
              "60 ÷ 2 = 30, 60 ÷ 5 = 12 and 60 ÷ 10 = 6, so 60 is divisible by 2, by 5 and by 10. 35 ÷ 5 = 7, but "
              "35 is not divisible by 2 or by 10, so 35 is divisible by 5 only.",
              "A number divisible by 10 is always divisible by 2 and by 5, because 10 = 2 × 5: each 10 is made of "
              "five 2s and of two 5s.",
              "A number divisible by both 2 and 5 is a common multiple of 2 and 5, so it is a multiple of 10: 10, 20, "
              "30, and so on. So no number is divisible by 10 only.",
              "Rule: check 2, 5 and 10 one by one. A number divisible by 10 is divisible by 2, 5 and 10."],
       examples=[WE("Sort the numbers 16, 35, 60, 48, 85 and 70 into: divisible by 2 only, divisible by 5 only, and "
                    "divisible by 2, 5 and 10.",
                    ["16: 16 ÷ 2 = 8 exactly. 5 × 3 = 15 and 5 × 4 = 20, so 16 is not divisible by 5. 16 is "
                     "divisible by 2 only.",
                     "35: 35 ÷ 5 = 7 exactly. 2 × 17 = 34 and 2 × 18 = 36, so 35 is not divisible by 2. 35 is "
                     "divisible by 5 only.",
                     "60: 60 ÷ 2 = 30, 60 ÷ 5 = 12 and 60 ÷ 10 = 6, all exact. 60 is divisible by 2, 5 and 10.",
                     "48: 48 ÷ 2 = 24 exactly. 5 × 9 = 45 and 5 × 10 = 50, so 48 is not divisible by 5. 48 is "
                     "divisible by 2 only.",
                     "85: 85 ÷ 5 = 17 exactly. 2 × 42 = 84 and 2 × 43 = 86, so 85 is not divisible by 2. 85 is "
                     "divisible by 5 only.",
                     "70: 70 ÷ 2 = 35, 70 ÷ 5 = 14 and 70 ÷ 10 = 7, all exact. 70 is divisible by 2, 5 and 10.",
                     "No number is divisible by 10 only: 60 and 70 are divisible by 10, and both are also divisible "
                     "by 2 and 5."],
                    "2 only: 16 and 48. 5 only: 35 and 85. 2, 5 and 10: 60 and 70. None is divisible by 10 only")],
       key_terms=["divisible", "factor", "factors"],
       misconceptions=["M_TEN_ONLY", "M_FACTOR_MULTIPLE"], minutes=6),
     DOER("T5.C3", "Pull it together and do it: Factors and Multiples at Work", "number_sorter", "Apply",
          "Students use factors, multiples and common multiples to decide true or false statements, find hunting "
          "days, choose jump sizes on the trail, and sort numbers by 2, 5 and 10.",
          ["One example that fails shows a statement is false; a true statement needs a reason.",
           "Days that two animals share are common multiples; jump sizes that reach two places are common factors.",
           "A number divisible by 10 is divisible by 2 and by 5, so no number is divisible by 10 only."],
          items=[FIO("LUD.Q8", "Let Us Do (factors and multiples at work), Q8",
                     "State whether the following statements are true (T) or false (F). (a) Factors of even numbers "
                     "must be even. (b) Multiples of odd numbers cannot be even. (c) Factors of odd numbers cannot "
                     "be even. (d) One of the common multiples of two consecutive numbers is their product. (e) The "
                     "only common factor of any two consecutive numbers is 1. (f) 0 cannot be a factor of any number.",
                     ["(a): False. 12 is even, and 3 is a factor of 12, because 3 × 4 = 12, but 3 is odd. 1 is also an odd "
                      "factor of every even number.",
                      "(b): False. 3 is odd, and 3 × 2 = 6 is a multiple of 3 that is even.",
                      "(c): True. If an even number were a factor of an odd number, the odd number would be a "
                      "multiple of an even number, and every multiple of an even number is even. The factors of 15 "
                      "are 1, 3, 5, 15 and of 21 are 1, 3, 7, 21: all odd.",
                      "(d): True. Take 4 and 5: 4 × 5 = 20, and 20 is a multiple of 4 and of 5. Take 8 and 9: "
                      "8 × 9 = 72, a multiple of both. A product is always a multiple of the numbers multiplied.",
                      "(e): True. The factors of 8 are 1, 2, 4, 8 and of 9 are 1, 3, 9: only 1 is common. The factors "
                      "of 14 are 1, 2, 7, 14 and of 15 are 1, 3, 5, 15: only 1 is common. A jump bigger than 1 lands "
                      "on a number and then at least 2 steps further, so it cannot land on both a number and the "
                      "next number.",
                      "(f): True. A jump of 0 steps stays at 0 for ever, so it can never reach a number. 0 × any "
                      "number is 0, so 0 only makes the number 0.",
                      "Check: 12 ÷ 3 = 4, so 3 does divide 12, and 3 × 2 = 6 is even."],
                     "(a): False; (b): False; (c): True; (d): True; (e): True; (f): True",
                     kind="exercise"),
                 FIO("LUD.Q9", "Let Us Do (factors and multiples at work), Q9",
                     "Sher Khan, the tiger, goes hunting every 3rd day. Bagheera, the panther, goes hunting every 5th "
                     "day. If both of them start on the same day, on which days will they be hunting together?",
                     ["Count the day they start together as day 0, like the start of a number line.",
                      "Sher Khan hunts on days 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, and so on: the multiples of 3.",
                      "Bagheera hunts on days 5, 10, 15, 20, 25, 30, and so on: the multiples of 5.",
                      "Both hunt on days 15, 30, 45 and so on. These are the common multiples of 3 and 5, and the "
                      "first is day 15, because 3 × 5 = 15.",
                      "Check: 3 × 10 = 30 and 5 × 6 = 30; 3 × 15 = 45 and 5 × 9 = 45."],
                     "On days 15, 30, 45, 60 and so on, the common multiples of 3 and 5, after the day they start "
                     "together.",
                     kind="exercise"),
                 FIO("LUD.Q10", "Let Us Do (factors and multiples at work), Q10",
                     "(a) In the trail shown earlier, Sher Khan's house is on number 25 and that of Baloo the bear is "
                     "on number 30. Mowgli wants to meet his friend Baloo the bear but wants to avoid Sher Khan's "
                     "house. How long (in steps) could each jump be? (b) What number of jumps (in steps) he could "
                     "choose so that he can meet both Kaa, the snake, at 21 and Akela, the wolf, at 35?",
                     ["(a): a jump meets Baloo at 30 when the jump size is a factor of 30. The factors of 30 are 1, 2, "
                      "3, 5, 6, 10, 15, 30.",
                      "A jump avoids Sher Khan at 25 when the jump size is not a factor of 25. The factors of 25 are "
                      "1, 5, 25.",
                      "Take out the jump sizes that land on 25: 1, because 1 × 25 = 25, and 5, because 5 × 5 = 25.",
                      "The jumps that meet Baloo and avoid Sher Khan are 2, 3, 6, 10, 15 and 30 steps.",
                      "(b): the jump must be a common factor of 21 and 35. The factors of 21 are 1, 3, 7, 21 and of 35 "
                      "are 1, 5, 7, 35. Common: 1 and 7.",
                      "Check: 7 × 3 = 21 and 7 × 5 = 35. Also 6 × 5 = 30, and jumps of 6 go 24 then 30, skipping 25."],
                     "(a): 2, 3, 6, 10, 15 or 30 steps. (b): 1 or 7 steps.",
                     kind="exercise",
                     q_figure="A winding trail of numbered stones from 0 to 60 with Mowgli at 0, Sher Khan the tiger "
                              "at 25, Baloo the bear at 30, Kaa the snake at 21 and Akela the wolf at 35.",
                     s_figure="The same trail with jumps of 6 marked, landing on 30 and skipping 25."),
                 FIO("LUD.Q11", "Let Us Do (factors and multiples at work), Q11",
                     "Sort the following numbers into those that are (a) divisible by 2 only (b) divisible by 5 only "
                     "(c) divisible by 10 only (d) divisible by 2, 5, and 10. 90, 22, 38, 30, 75, 45, 66, 78, 62, 40, "
                     "84, 56, 25, 95, 55",
                     ["A number is divisible by 2 when 2 is a factor of it. The same is true for 5 and for 10.",
                      "90: 90 ÷ 2 = 45, 90 ÷ 5 = 18 and 90 ÷ 10 = 9, all exact. 90 is divisible by 2, 5 and 10.",
                      "30: 30 ÷ 2 = 15, 30 ÷ 5 = 6 and 30 ÷ 10 = 3. 40: 40 ÷ 2 = 20, 40 ÷ 5 = 8 and 40 ÷ 10 = 4. All "
                      "exact, so 30 and 40 are divisible by 2, 5 and 10 too.",
                      "22, 38, 66, 78, 62, 84 and 56 are divisible by 2 but not by 5 (for example 22 ÷ 2 = 11, but "
                      "5 × 4 = 20 and 5 × 5 = 25 skip 22). So these 7 are divisible by 2 only.",
                      "75, 45, 25, 95 and 55 are divisible by 5 but not by 2, because they are odd (for example "
                      "45 ÷ 5 = 9). So these 5 are divisible by 5 only.",
                      "No number is divisible by 10 only: a number divisible by 10 is also divisible by 2 and 5 "
                      "(10 = 2 × 5), so 90, 30 and 40 go in the middle.",
                      "Check: 7 + 5 + 3 = 15, the same as the number of cards."],
                     "(a): 22, 38, 66, 78, 62, 84, 56; (b): 75, 45, 25, 95, 55; (c): none; (d): 90, 30, 40",
                     kind="exercise",
                     q_figure="Fifteen number cards: 90, 22, 38, 30, 75 in the first row, 45, 66, 78, 62, 40 in the "
                              "second row and 84, 56, 25, 95, 55 in the third row, and three overlapping circles "
                              "labelled divisible only by 2, divisible only by 5 and divisible only by 10, with the "
                              "middle labelled divisible by 2, 5 and 10.",
                     s_figure="The three overlapping circles with 7 numbers in the circle for 2 only, 5 numbers in the "
                              "circle for 5 only, 3 numbers in the middle and none in the circle for 10 only.")],
          misconceptions=["M_EVEN_FACTORS", "M_ODD_MULTIPLES", "M_ZERO_FACTOR", "M_TEN_ONLY"])],
    key_terms=["statement", "divisible", "factors", "multiples"]))

# ============================== T6 Chapter Revision (summary) =============================================
TOPICS.append(TOPIC(
    "T6", "M3", "Chapter Revision: Animal Jumps", ["Chapter summary"], "Understand",
    "",
    "The chapter's ideas in one walk along the trail: factors and multiples, arrays, prime numbers, common multiples, "
    "common factors, testing statements, and using them for the hunting days and the trail.",
    [A("T6.C1", "Chapter Revision: Animal Jumps", "Understand",
       "",
       teach=["Predict first: you have jumped along the whole trail. Can you say one idea from each stop, from the "
              "hidden box to the hunting days? Read the lines below and tick each idea you remembered.",
              "Factors and multiples: a number you multiply by is a factor of the answer, and the answer is a multiple "
              "of it. The box that gave 28, 36, 48 and 72 could multiply by 1, 2 or 4, the common factors of the four "
              "numbers.",
              "Check: 4 × 7 = 28 and 4 × 9 = 36, so 28 and 36 are multiples of 4.",
              "Arrays: the arrays of a number show its factors. 12 has the arrays 1 × 12, 2 × 6 and 3 × 4, so its "
              "factors are 1, 2, 3, 4, 6 and 12. 1 and the number itself are always factors, and a number is a "
              "multiple of each of its factors.",
              "Check: what are the factors of 10? 1, 2, 5 and 10, from the arrays 1 × 10 and 2 × 5.",
              "Prime numbers: a number whose only array is 1 × the number has only two factors, 1 and itself. 13 and "
              "37 are prime numbers.",
              "Check: is 14 a prime number? No, 14 has the factors 1, 2, 7 and 14.",
              "Common multiples: the numbers two jumpers both touch. 3 and 4 have the common multiples 12, 24, 36, "
              "and so on, the multiples of the first one, 12.",
              "Check: what are the first three common multiples of 4 and 6? 12, 24 and 36.",
              "Common factors: the jump sizes that land on every number of a list. The common factors of 24 and 36 "
              "are 1, 2, 3, 4, 6 and 12. 1 is always a common factor, and 12 and 13 have only 1.",
              "Check: which jump sizes reach both 8 and 12? Jumps of 1, 2 and 4.",
              "Testing statements: one example that fails shows a statement is false. A multiple of an odd number can "
              "be even, as in 3 × 2 = 6. A number divisible by 10 is divisible by 2 and by 5.",
              "Check: is every factor of an even number even? No, 3 is a factor of 12.",
              "Using the ideas: Sher Khan hunts every 3rd day and Bagheera every 5th day, so they hunt together on "
              "days 15, 30, 45 and so on. Mowgli can meet Baloo at 30 and avoid Sher Khan at 25 with jumps of 2, 3, "
              "6, 10, 15 or 30 steps."],
       ncert=["summary"], key_terms=["factors", "multiples", "common factors", "common multiples"], minutes=6,
       enrichment=True)],
    topic_type="summary"))
