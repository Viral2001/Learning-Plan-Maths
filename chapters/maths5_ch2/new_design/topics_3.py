# -*- coding: utf-8 -*-
"""Topics T7 and T8 (module M2 and M3) of Class 5 Chapter 2, Fractions: Fractions Greater Than 1 (halves, fourths and
thirds joined into whole parathas and pizzas, read on a number line) and Comparing with 1 and with 1/2.
Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of
its topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T7 Fractions Greater Than 1 ================================================
TOPICS.append(TOPIC(
    "T7", "M2", "Fractions Greater Than 1", ["Fractions Greater Than 1"], "Apply",
    "Students join pieces of 1/2, 1/4 and 1/3 into whole parathas, show them on a number line, write the total as a "
    "whole number and a part, and say a fraction is greater than 1 when its top number is more than its bottom "
    "number.",
    "Raman's father cuts parathas into halves or fourths, and the family cuts pizza into thirds. Pieces of one size "
    "join into whole parathas, and the pieces left over are the part. 5/2 is 2 whole parathas and 1/2 more, written "
    "2 1/2. A fraction is greater than 1 when its top number is more than its bottom number.",
    [A("T7.C1", "Halves Make Parathas", "Understand",
       "Students join pieces of 1/2 into whole parathas, count the whole parathas and the half left over, and write "
       "n pieces of 1/2 as a fraction and as a whole number and a part.",
       textbook=["Raman's father makes nice soft parathas. He cuts the parathas either into halves (2 equal parts) or "
                 "fourths (4 equal parts) before serving them. He asks his children (Raman and Radhika) each day to "
                 "find out the number of parathas he made.",
                 "We can also show the same on a number line. Divide the distance between 0 and 1 in two equal "
                 "parts. Each part is 1/2. 2 halves make 1. Placing 5 halves next to each other takes us to 5/2 or "
                 "2 1/2."],
       teach=["Predict first: Baba takes 9 pieces of 1/2 paratha. Is that more than 4 whole parathas, or less?",
              "2 pieces of 1/2 fit together to make 1 whole paratha. So join the pieces two at a time.",
              "9 pieces: 2 + 2 + 2 + 2 = 8 pieces make 4 whole parathas. 1 piece of 1/2 is left over.",
              "So 9 pieces of 1/2 paratha = 9/2 parathas = 4 + 1/2 parathas = 4 1/2 parathas. It is more than 4.",
              "On a number line, divide the gap from 0 to 1 into 2 equal parts. Each jump is 1/2. 2/2 lands on 1 and "
              "4/2 lands on 2. 9 jumps land on 9/2, halfway between 4 and 5.",
              "Rule: 2 halves make 1. Join the pieces in groups of 2. The groups are the whole parathas and the "
              "piece left over is the part."],
       examples=[WE("Raman's father cuts parathas into halves. Baba took 9 pieces of 1/2 paratha. How many parathas "
                    "did he eat?",
                    ["2 pieces of 1/2 make 1 paratha, so join the pieces two at a time.",
                     "9 pieces: 2 + 2 + 2 + 2 = 8 pieces make 4 whole parathas.",
                     "9 − 8 = 1 piece of 1/2 is left over.",
                     "9 pieces of 1/2 paratha = 9/2 parathas = 4 + 1/2 parathas = 4 1/2 parathas.",
                     "Check on the number line: 9 jumps of 1/2 from 0 land on 9/2. 8/2 is 4, and one more jump of "
                     "1/2 lands halfway between 4 and 5."],
                    "4 1/2 parathas")],
       ncert=["gt1.intro", "gt1.nl_halves"],
       key_terms=["halves", "number line", "whole paratha"],
       misconceptions=["M_NO_PAST_ONE", "M_MIXED_TIMES"], minutes=7),
     A("T7.C2", "Fourths and Thirds Past One Whole", "Apply",
       "Students join pieces of 1/4 and pieces of 1/3 into whole parathas and pizzas, find how many are left over, "
       "and write the total as a fraction and as a whole number and a part.",
       textbook=["We can also show the same on a number line. Divide the distance between 0 and 1 into four equal "
                 "parts. Each part is 1/4. 4 one-fourths make 1. Placing 9 one-fourths next to each other takes us "
                 "to 9/4 or 2 1/4."],
       teach=["Predict first: how many pieces of 1/4 make 1 whole paratha? With 11 pieces of 1/4, will you get more "
              "than 2 whole parathas?",
              "4 pieces of 1/4 make 1 paratha, so make groups of 4. The bottom number tells the size of a group.",
              "11 pieces: 4 + 4 = 8 pieces make 2 whole parathas. 3 pieces of 1/4 are left. So 11/4 = 2 + 3/4 = "
              "2 3/4.",
              "A pizza cut into 3 equal slices works the same way. 3 slices of 1/3 make 1 pizza. With 8 slices, "
              "3 + 3 = 6 slices make 2 pizzas and 2 slices are left. So 8/3 = 2 + 2/3 = 2 2/3.",
              "Rule: the bottom number says how many pieces make 1 whole. Make groups of that size. The groups are "
              "the whole number and the pieces left over are the part."],
       examples=[WE("(a) Radhika ate 11 pieces of 1/4 paratha. How many parathas did she eat? (b) A pizza is cut "
                    "into 3 equal slices. The family ate 8 slices, each slice 1/3 of a pizza. How much pizza is "
                    "that?",
                    ["(a) 4 pieces of 1/4 make 1 paratha, so make groups of 4.",
                     "11 pieces: 4 + 4 = 8 pieces make 2 whole parathas.",
                     "11 − 8 = 3 pieces of 1/4 are left over.",
                     "11 pieces of 1/4 paratha = 11/4 parathas = 2 + 3/4 parathas = 2 3/4 parathas.",
                     "(b) 3 slices of 1/3 make 1 pizza, so make groups of 3.",
                     "8 slices: 3 + 3 = 6 slices make 2 whole pizzas, and 8 − 6 = 2 slices are left over.",
                     "8 slices of 1/3 pizza = 8/3 pizzas = 2 + 2/3 pizzas = 2 2/3 pizzas.",
                     "Check: 2 whole parathas are 2 × 4 = 8 pieces, and 8 + 3 = 11 pieces. 2 whole pizzas are "
                     "2 × 3 = 6 slices, and 6 + 2 = 8 slices."],
                    "(a) 2 3/4 parathas (b) 2 2/3 pizzas")],
       ncert=["gt1.nl_fourths"],
       key_terms=["fourths", "thirds", "pieces left over"],
       misconceptions=["M_NO_PAST_ONE", "M_MIXED_TIMES"], minutes=7),
     A("T7.C3", "More Than One Whole? Top and Bottom", "Understand",
       "Students say whether a fraction is greater than 1, equal to 1 or less than 1 by comparing its top number "
       "with its bottom number, and explain the reason with pieces.",
       teach=["Predict first: is 8/5 more than 1 whole, equal to 1 whole, or less than 1 whole? And is 3/10?",
              "The bottom number tells how many pieces make 1 whole. 5 pieces of 1/5 make 1 whole.",
              "8/5 means 8 pieces of 1/5. 8 pieces are more than the 5 pieces that make 1 whole, so 8/5 is more "
              "than 1. 8 − 5 = 3 pieces are left over, so 8/5 = 1 3/5.",
              "3/10 means 3 pieces of 1/10. 3 pieces are fewer than the 10 pieces that make 1 whole, so 3/10 is "
              "less than 1.",
              "When the top and bottom numbers are the same, like 5/5 or 7/7, the pieces fill exactly 1 whole.",
              "Rule: top number more than bottom number, more than 1. Top number equal to bottom number, exactly 1. "
              "Top number less than bottom number, less than 1."],
       examples=[WE("Is each fraction more than 1, equal to 1 or less than 1? (a) 8/5 (b) 3/10 (c) 10/10",
                    ["(a) 8/5 is 8 pieces of 1/5, and 5 pieces of 1/5 make 1 whole.",
                     "8 is more than 5, so 8/5 is more than 1. 8 − 5 = 3 pieces are left over, so 8/5 = 1 3/5.",
                     "(b) 3/10 is 3 pieces of 1/10, and 10 pieces of 1/10 make 1 whole.",
                     "3 is less than 10, so 3/10 is less than 1.",
                     "(c) 10/10 is 10 pieces of 1/10, exactly the 10 pieces that make 1 whole, so 10/10 = 1.",
                     "Check: 8/5 = 1 3/5 is more than 1, 3/10 is less than 1 and 10/10 is exactly 1."],
                    "(a) more than 1 (it is 1 3/5) (b) less than 1 (c) equal to 1")],
       key_terms=["top number", "bottom number", "greater than 1"],
       misconceptions=["M_NO_PAST_ONE"], minutes=6),
     DOER("T7.C4", "Practice: Paratha Number Line", "paratha_number_line", "Apply",
          "Students show pieces of 1/2, 1/4 and 1/3 as whole parathas and a part on a number line, add the pieces "
          "of the family, and circle the fractions that are greater than 1 in the book's questions.",
          ["2 pieces of 1/2, 4 pieces of 1/4 or 3 pieces of 1/3 make 1 whole.",
           "Join the pieces in groups of the bottom number. The groups are the whole number and the pieces left over "
           "are the part.",
           "On a number line each piece is one jump of the same size, and the jumps go on past 1.",
           "A fraction is greater than 1 when its top number is more than its bottom number."],
          items=[
              FIO("gt1.maa", "Example 3: Maa's 5 halves",
                  "Raman's father cuts the parathas into halves (2 equal parts) before serving them. Maa took 5 "
                  "pieces of 1/2 paratha. How many parathas did she eat?",
                  ["2 pieces of 1/2 make 1 paratha, so join the pieces two at a time.",
                   "5 pieces: 2 + 2 = 4 pieces make 2 whole parathas.",
                   "5 − 4 = 1 piece of 1/2 is left over.",
                   "5 pieces of 1/2 paratha = 5/2 parathas = 2 + 1/2 parathas = 2 1/2 parathas.",
                   "Check on the number line: 5 jumps of 1/2 from 0 land on 5/2, which is halfway between 2 and 3."],
                  "2 1/2 parathas",
                  kind="example",
                  q_figure="Five pieces of paratha lie on a plate, and each piece is one half of a paratha.",
                  s_figure="The five half pieces joined in two groups of 2 pieces, each group a whole paratha, with "
                           "1 half piece left over, and a number line from 0 to 3 with marks at every 1/2 labelled "
                           "0, 1/2, 2/2 = 1, 3/2, 4/2 = 2 and 5/2."),
              FIO("gt1.radhika", "Example 4: Radhika's 6 halves",
                  "Raman's sister Radhika took 6 pieces of 1/2 paratha. How many parathas did she eat?",
                  ["2 pieces of 1/2 make 1 paratha, so join the pieces two at a time.",
                   "6 pieces: 2 + 2 + 2 = 6 pieces make 3 groups of 2, and no piece is left over.",
                   "1/2 + 1/2 + 1/2 + 1/2 + 1/2 + 1/2 = 6/2 parathas = 3 parathas.",
                   "Check on the number line: 6 jumps of 1/2 from 0 land on 6/2, which is the mark 3."],
                  "3 parathas",
                  kind="example",
                  q_figure="Six pieces of paratha lie on a plate, and each piece is one half of a paratha.",
                  s_figure="The six half pieces joined in three groups of 2 pieces, each group a whole paratha, and "
                           "a number line from 0 to 3 with marks at every 1/2 labelled 0, 1/2, 2/2 = 1, 3/2, "
                           "4/2 = 2, 5/2 and 6/2 = 3."),
              FIO("gt1.dadiji", "Fractions Greater Than 1: Dadiji's halves",
                  "Dadiji had 7 pieces of 1/2 paratha. How many parathas did she eat? Find out.",
                  ["2 pieces of 1/2 make 1 paratha, so make groups of 2.",
                   "7 pieces: 2 + 2 + 2 = 6 pieces make 3 whole parathas.",
                   "7 − 6 = 1 piece of 1/2 is left over.",
                   "7 pieces of 1/2 paratha = 7/2 parathas = 3 + 1/2 parathas = 3 1/2 parathas.",
                   "Check: 3 whole parathas are 3 × 2 = 6 pieces, and 6 + 1 = 7 pieces."],
                  "3 1/2 parathas",
                  kind="prompt",
                  s_figure="The seven half pieces joined in three groups of 2 pieces, each group a whole paratha, "
                           "with 1 half piece left over."),
              FIO("gt1.three_lines", "Fractions Greater Than 1: halves on number lines",
                  "Raman ate 6 pieces of 1/2 paratha, Dadaji ate 7 pieces of 1/2 paratha and Baba ate 5 pieces of "
                  "1/2 paratha. How many parathas did each of them eat? Use the number line to find the answer.",
                  ["Each jump on the number line is 1/2, and 2 jumps reach the mark 1.",
                   "Raman: 6 jumps land on 6/2. 6 ÷ 2 = 3, so he ate 3 parathas.",
                   "Dadaji: 7 jumps land on 7/2. 2 + 2 + 2 = 6 pieces make 3 parathas and 1 piece is left, so "
                   "7/2 = 3 1/2.",
                   "Baba: 5 jumps land on 5/2. 2 + 2 = 4 pieces make 2 parathas and 1 piece is left, so "
                   "5/2 = 2 1/2.",
                   "Check: Dadaji ate 1/2 more than Raman (3 1/2), and Baba ate 1/2 less than Raman (2 1/2)."],
                  "Raman 3 parathas, Dadaji 3 1/2 parathas, Baba 2 1/2 parathas",
                  kind="prompt",
                  q_figure="Three number lines, one for Raman's paratha, one for Dadaji's paratha and one for Baba's "
                           "paratha, each starting at 0 and drawn with equal marks, and only 0 and 1 are labelled.",
                  s_figure="The same three number lines with every mark labelled 0, 1/2, 2/2 = 1, 3/2 and so on, a "
                           "dot at 6/2 = 3 on Raman's line, at 7/2 on Dadaji's line and at 5/2 on Baba's line."),
              FIO("gt1.day_halves", "Fractions Greater Than 1: parathas made, halves day",
                  "Maa took 5, Radhika 6, Dadiji 7, Raman 6, Dadaji 7 and Baba 5 pieces of 1/2 paratha. How many "
                  "parathas were made on this day? Find out.",
                  ["The six family members took these pieces of 1/2 paratha: Maa 5, Radhika 6, Dadiji 7, Raman 6, "
                   "Dadaji 7 and Baba 5.",
                   "Add the pieces: 5 + 6 + 7 + 6 + 7 + 5 = 36 pieces.",
                   "2 pieces of 1/2 make 1 paratha, so 36 pieces make 36 ÷ 2 = 18 parathas.",
                   "36 pieces of 1/2 paratha = 36/2 parathas = 18 parathas.",
                   "Check: Maa's 2 1/2 and Baba's 2 1/2 make 5, Dadiji's 3 1/2 and Dadaji's 3 1/2 make 7, and "
                   "Radhika's 3 and Raman's 3 make 6. 5 + 7 + 6 = 18."],
                  "18 parathas",
                  kind="prompt",
                  s_figure="A table of the six family members with their pieces of 1/2 paratha, 5, 6, 7, 6, 7 and 5, "
                           "and under it the total, 36 pieces of 1/2, which make 18 parathas."),
              FIO("gt1.dadaji9", "Example 5: Dadaji's 9 fourths",
                  "Another day, Raman's father cut all the parathas in 1/4. Dadaji took 9 pieces of 1/4 paratha. "
                  "How many parathas did he eat?",
                  ["4 pieces of 1/4 make 1 paratha, so make groups of 4.",
                   "9 pieces: 4 + 4 = 8 pieces make 2 whole parathas.",
                   "9 − 8 = 1 piece of 1/4 is left over.",
                   "9 pieces of 1/4 paratha = 9/4 parathas = 2 + 1/4 parathas = 2 1/4 parathas.",
                   "Check on the number line: 9 jumps of 1/4 from 0 land on 9/4, one jump past the mark 2."],
                  "2 1/4 parathas",
                  kind="example",
                  q_figure="Nine pieces of paratha lie on a plate, and each piece is one fourth of a paratha.",
                  s_figure="The nine fourth pieces joined in two groups of 4 pieces, each group a whole paratha, "
                           "with 1 fourth piece left over, and a number line from 0 to 3 with marks at every 1/4 "
                           "labelled 0, 1/4, 2/4, 3/4, 4/4 = 1, up to 8/4 = 2 and 9/4."),
              FIO("gt1.five_lines", "Fractions Greater Than 1: fourths on number lines",
                  "Raman ate 7 pieces of 1/4, Radhika ate 6 pieces of 1/4, Maa ate 8 pieces of 1/4, Dadiji ate 10 "
                  "pieces of 1/4, and Baba ate 12 pieces of 1/4 paratha. Use a number line to find out how many "
                  "parathas were eaten by each of them.",
                  ["Each jump on the number line is 1/4, and 4 jumps reach the mark 1.",
                   "Raman: 7 pieces. 4 pieces make 1 paratha and 3 pieces are left, so 7/4 = 1 3/4 parathas.",
                   "Radhika: 6 pieces. 4 pieces make 1 paratha and 2 pieces are left, so 6/4 = 1 2/4 parathas. "
                   "2 pieces of 1/4 make 1/2, so this is also 1 1/2 parathas.",
                   "Maa: 8 pieces. 8 ÷ 4 = 2, so 8/4 = 2 parathas.",
                   "Dadiji: 10 pieces. 4 + 4 = 8 pieces make 2 parathas and 2 pieces are left, so 10/4 = 2 2/4 "
                   "parathas, the same as 2 1/2.",
                   "Baba: 12 pieces. 12 ÷ 4 = 3, so 12/4 = 3 parathas.",
                   "Check: the more pieces, the farther along the line. 6, 7, 8, 10 and 12 pieces land at 1 1/2, "
                   "1 3/4, 2, 2 1/2 and 3."],
                  "Raman 1 3/4, Radhika 1 2/4 (the same as 1 1/2), Maa 2, Dadiji 2 2/4 (the same as 2 1/2) and "
                  "Baba 3 parathas",
                  kind="prompt",
                  q_figure="Five number lines, one each for Raman's, Radhika's, Maa's, Dadiji's and Baba's paratha, "
                           "each with only the marks 0 and 1 drawn and labelled.",
                  s_figure="The same five number lines with marks at every 1/4 and a dot at 7/4 for Raman, 6/4 for "
                           "Radhika, 8/4 = 2 for Maa, 10/4 for Dadiji and 12/4 = 3 for Baba."),
              FIO("gt1.day_fourths", "Fractions Greater Than 1: parathas made, fourths day",
                  "Dadaji took 9 pieces of 1/4, and Raman 7, Radhika 6, Maa 8, Dadiji 10 and Baba 12. How many "
                  "parathas were made on this day? Find out.",
                  ["The six family members took these pieces of 1/4 paratha: Dadaji 9, Raman 7, Radhika 6, Maa 8, "
                   "Dadiji 10 and Baba 12.",
                   "Add the pieces: 9 + 7 + 6 + 8 + 10 + 12 = 52 pieces.",
                   "4 pieces of 1/4 make 1 paratha, so 52 pieces make 52 ÷ 4 = 13 parathas.",
                   "52 pieces of 1/4 paratha = 52/4 parathas = 13 parathas.",
                   "Check: 13 × 4 = 52, so 13 whole parathas use exactly 52 pieces and no piece is left over."],
                  "13 parathas",
                  kind="prompt",
                  s_figure="A table of the six family members with their pieces of 1/4 paratha, 9, 7, 6, 8, 10 and "
                           "12, and under it the total, 52 pieces of 1/4, which make 13 parathas."),
              FIO("gt1.pizza_share", "Example 6: the family pizza",
                  "Raman's family of 6 members ordered 2 pizzas and cut each pizza into 3 equal slices so that each "
                  "family member had one slice. Dadiji and Dadaji gave their slices to Raman, Maa and Baba gave "
                  "theirs to Radhika. How much pizza do each of them have after this?",
                  ["2 pizzas cut into 3 slices each make 2 × 3 = 6 slices, one slice for each of the 6 family "
                   "members.",
                   "Each slice is 1/3 of a pizza.",
                   "Raman has his own slice and the slices of Dadiji and Dadaji, so he has 3 slices.",
                   "Radhika has her own slice and the slices of Maa and Baba, so she has 3 slices.",
                   "3 slices of 1/3 pizza: 1/3 + 1/3 + 1/3 = 3/3 = 1 pizza.",
                   "So Raman has 1 whole pizza and Radhika has 1 whole pizza.",
                   "Check: 1 + 1 = 2 pizzas, the same as the 2 pizzas that were ordered."],
                  "Raman has 1 whole pizza and Radhika has 1 whole pizza.",
                  kind="example",
                  q_figure="Two round pizzas, each cut into 3 equal slices.",
                  s_figure="Raman's three slices of 1/3 placed together to make one whole round pizza, and a number "
                           "line from 0 to 1 with marks 0, 1/3, 2/3 and 3/3 = 1."),
              FIO("gt1.pizza_more", "Example 7: Radhika gets a slice",
                  "Raman could eat only 2 slices of pizza. So, he gave 1 to Radhika. How much pizza does Radhika "
                  "have now?",
                  ["Raman had 3 slices, ate 2 and gave 1 slice to Radhika.",
                   "Before this Radhika had 3 slices of 1/3, which is 1 whole pizza. Now she has 3 + 1 = 4 slices "
                   "of 1/3.",
                   "4 slices of 1/3 pizza = 4/3 pizzas.",
                   "3 slices make 1 pizza and 1 slice is left over, so 4/3 = 1 + 1/3 = 1 1/3 pizzas.",
                   "Check on the number line: 4 jumps of 1/3 from 0 pass the mark 3/3 = 1 and land one jump after "
                   "it, at 4/3."],
                  "1 1/3 pizzas",
                  kind="example",
                  q_figure="Three slices of pizza placed together as one round pizza and, next to it, one more slice; "
                           "each slice is 1/3 of a pizza.",
                  s_figure="The one whole round pizza of 3 slices and the 1 extra slice beside it, and a number line "
                           "from 0 to 2 with marks 0, 1/3, 2/3, 3/3 = 1 and 4/3."),
              FIO("LUDgt1.Q1", "Let Us Do (fractions greater than 1), Q1",
                  "Use parathas and number lines to show the following fractions in your notebook. (a) 2/3 and 5/3 "
                  "(b) 3/4 and 5/4 (c) 4/8 and 9/8",
                  ["(a) For 2/3, cut a paratha into 3 equal pieces and take 2 pieces. On the number line, cut the gap "
                   "from 0 to 1 into 3 equal parts and mark the 2nd mark.",
                   "5/3: 3 pieces of 1/3 make 1 paratha, so 5 pieces are 1 whole paratha and 2 pieces of a second "
                   "paratha. On the number line go past 1 to the 5th mark. 5/3 = 1 + 2/3 = 1 2/3.",
                   "(b) For 3/4, cut a paratha into 4 equal pieces and take 3 pieces. Mark the 3rd mark of 4 equal parts "
                   "from 0 to 1.",
                   "5/4: 4 pieces of 1/4 make 1 paratha, so 5 pieces are 1 whole paratha and 1 piece of a second "
                   "paratha. 5/4 = 1 + 1/4 = 1 1/4.",
                   "(c) For 4/8, cut a paratha into 8 equal pieces and take 4 pieces. 4 pieces of 1/8 are half of the "
                   "paratha, so 4/8 = 1/2.",
                   "9/8: 8 pieces of 1/8 make 1 paratha, so 9 pieces are 1 whole paratha and 1 piece of a second "
                   "paratha. 9/8 = 1 + 1/8 = 1 1/8.",
                   "Check: 2/3, 3/4 and 4/8 are less than 1 because the top number is less than the bottom number. "
                   "5/3, 5/4 and 9/8 are more than 1 because the top number is more than the bottom number."],
                  "(a) 2/3 is less than 1, 5/3 = 1 2/3; (b) 3/4 is less than 1, 5/4 = 1 1/4; (c) 4/8 is half, "
                  "9/8 = 1 1/8",
                  kind="exercise",
                  s_figure="For each of the six fractions, parathas drawn with the pieces shaded, and a number line "
                           "from 0 to 2 with a dot at the fraction, with marks at every 1/3 for part (a), every 1/4 "
                           "for part (b) and every 1/8 for part (c)."),
              FIO("LUDgt1.Q2", "Let Us Do (fractions greater than 1), Q2",
                  "Circle the fractions that are greater than one (whole). How do you know? Discuss your reasoning "
                  "in the class. 7/9, 3/9, 7/11, 9/4, 9/4, 2/5, 4/9, 5/7, 5/4, 7/3, 13/11, 12/5, 12/8, 2/3",
                  ["A fraction is greater than 1 when its top number is more than its bottom number. Check the "
                   "fractions one group at a time.",
                   "The top number is less than the bottom number in 7/9, 3/9, 7/11, 2/5, 4/9, 5/7 and 2/3, so "
                   "these 7 fractions are less than 1.",
                   "The top number is more than the bottom number in 9/4, 9/4, 5/4, 7/3, 13/11, 12/5 and 12/8, "
                   "because 9 is more than 4, 5 is more than 4, 7 is more than 3, 13 is more than 11, 12 is more "
                   "than 5 and 12 is more than 8.",
                   "Circle these 7 fractions: 9/4, 9/4, 5/4, 7/3, 13/11, 12/5 and 12/8.",
                   "Check: 7 + 7 = 14, so all 14 fractions in the box are sorted, and no top number equals its "
                   "bottom number."],
                  "9/4, 9/4, 5/4, 7/3, 13/11, 12/5 and 12/8 are greater than 1, because the top number is more "
                  "than the bottom number.",
                  kind="exercise",
                  q_figure="A box with 14 fractions scattered inside it: 7/9, 3/9, 7/11, 9/4, 9/4, 2/5, 4/9, 5/7, "
                           "5/4, 7/3, 13/11, 12/5, 12/8 and 2/3, each written with its top and bottom number.",
                  s_figure="The same box with the fractions 9/4, 9/4, 5/4, 7/3, 13/11, 12/5 and 12/8 circled."),
              FIO("try.ants", "Try This: the ants on the number line",
                  "If the length of an ant is 1/4 cm, then what is the total length of 16 such ants walking in a "
                  "line? Use the number line given below.",
                  ["Each ant is 1/4 cm long, so each ant is one jump of 1/4 cm on the number line.",
                   "16 ants are 16 pieces of 1/4 cm, so the total length is 16/4 cm.",
                   "4 pieces of 1/4 cm make 1 cm, so 16 ÷ 4 = 4 cm.",
                   "Check: 4 ants make 1 cm, 8 ants make 2 cm, 12 ants make 3 cm and 16 ants make 4 cm."],
                  "4 cm",
                  kind="prompt",
                  q_figure="Sixteen ants walking head to tail in a line along a number line that starts at 0, with "
                           "the first ant marked 1/4 cm.",
                  s_figure="The same line with marks at every 1/4 cm and the marks 4/4 = 1, 8/4 = 2, 12/4 = 3 and "
                           "16/4 = 4 labelled in cm, and a bracket from 0 to the end of the 16th ant at 4 cm.")],
          misconceptions=["M_NO_PAST_ONE", "M_MIXED_TIMES"])],
    key_terms=["fractions greater than 1", "number line", "whole number and a part"]))

# ============================== T8 Comparing with 1 and with 1/2 ===========================================
TOPICS.append(TOPIC(
    "T8", "M3", "Comparing with 1 and with 1/2", ["Comparing Fractions With Reference to 1 (a whole)",
                                                  "Comparing Fractions with Reference to 1/2"], "Analyze",
    "Students compare two fractions by placing each against the references 1 and 1/2, decide whether a fraction is "
    "less than, equal to or more than 1 or 1/2, and give the reason from its top and bottom numbers.",
    "To compare two fractions, check each one against 1. A fraction less than 1 is less than a fraction more than 1. "
    "A fraction is equal to 1/2 when its top number is half of its bottom number. Find half of the bottom number: a "
    "smaller top number means less than 1/2 and a bigger top number means more than 1/2.",
    [A("T8.C1", "Compare with 1", "Apply",
       "Students decide whether a fraction is less than 1, equal to 1 or more than 1, and use 1 as a reference to "
       "compare two fractions when one is less than 1 and the other is more than 1.",
       textbook=["Comparing Fractions With Reference to 1 (a whole)",
                 "Let us compare some more fractions."],
       teach=["Predict first: which is more, 3/5 or 10/9? You do not need to cut anything. Where does each fraction "
              "sit compared with 1?",
              "1 is a signpost on the number line. 3/5 is 3 pieces of 1/5, and 5 pieces would make 1, so 3/5 is "
              "less than 1.",
              "10/9 is 10 pieces of 1/9, and 9 pieces already make 1, so 10/9 is more than 1.",
              "3/5 is to the left of 1 and 10/9 is to the right of 1. A fraction to the left of 1 is less than a "
              "fraction to the right of 1, so 3/5 < 10/9.",
              "If both fractions are more than 1, then 1 cannot decide. Write each as a whole number and a part and "
              "compare the whole numbers first.",
              "Rule: check each fraction against 1. A fraction less than 1 is less than a fraction more than 1."],
       examples=[WE("Which is more, 3/5 or 10/9? Use 1 as the reference.",
                    ["3/5 is 3 pieces of 1/5. 5 pieces of 1/5 make 1, and 3 is less than 5, so 3/5 is less than 1.",
                     "10/9 is 10 pieces of 1/9. 9 pieces of 1/9 make 1, and 10 is more than 9, so 10/9 is more "
                     "than 1.",
                     "3/5 is on the left of 1 on the number line and 10/9 is on the right of 1.",
                     "A fraction less than 1 is less than a fraction more than 1, so 3/5 < 10/9.",
                     "Check: 3/5 + 2/5 = 5/5 = 1, so 3/5 falls short of 1, and 10/9 = 1 + 1/9 goes past 1."],
                    "10/9 is more than 3/5, because 3/5 is less than 1 and 10/9 is more than 1, so 3/5 < 10/9")],
       key_terms=["reference", "less than 1", "more than 1"],
       misconceptions=["M_NO_PAST_ONE", "M_TOP_ONLY"], minutes=6),
     A("T8.C2", "Half as a Reference", "Understand",
       "Students decide whether a fraction is equal to 1/2, less than 1/2 or more than 1/2 by finding half of its "
       "bottom number and comparing its top number with it.",
       textbook=["Comparing Fractions with Reference to 1/2",
                 "4/8 = 1/2",
                 "3/6 = 1/2"],
       teach=["Predict first: is 9/18 equal to 1/2, less than 1/2 or more than 1/2? And what about 7/15?",
              "1/2 is a signpost halfway between 0 and 1. In your maths book, 4 of 8 equal pieces and 3 of 6 equal "
              "pieces both fill exactly half of the paratha.",
              "A fraction is equal to 1/2 when its top number is half of its bottom number. Half of 18 is 9, so "
              "9/18 = 1/2.",
              "Half of 15 is 7 1/2. The top number 7 is less than 7 1/2, so 7/15 is less than 1/2. It is close to "
              "half, but close is not equal.",
              "Rule: find half of the bottom number and compare the top number with it. The same is equal to 1/2, "
              "less is less than 1/2 and more is more than 1/2."],
       examples=[WE("Compare each fraction with 1/2. Is it equal to, less than or more than 1/2? (a) 9/18 (b) 7/15",
                    ["(a) Half of the bottom number: 18 ÷ 2 = 9.",
                     "The top number is 9, the same as half of 18, so 9/18 = 1/2.",
                     "(b) Half of the bottom number 15 is 7 1/2, because 7 1/2 + 7 1/2 = 15.",
                     "The top number 7 is less than 7 1/2, so 7/15 is less than 1/2.",
                     "Check: 2 × 9 = 18, so 9/18 is exactly half. 2 × 7 = 14, and 14 is less than 15, so 7/15 is "
                     "less than half."],
                    "(a) 9/18 = 1/2 (b) 7/15 is less than 1/2")],
       ncert=["rh.pictures"],
       key_terms=["half", "reference", "equal to 1/2"],
       misconceptions=["M_NEAR_HALF"], minutes=7),
     A("T8.C3", "Less Than Half, More Than Half", "Analyze",
       "Students compare two fractions that sit on different sides of 1/2 by finding which one is less than 1/2 "
       "and which one is more than 1/2, and say which fraction is greater.",
       teach=["Predict first: which is more, 5/12 or 7/10? Neither is 1 or more. Can you still tell without "
              "cutting anything?",
              "Compare each fraction with 1/2. Half of 12 is 6, and the top number 5 is less than 6, so 5/12 is "
              "less than 1/2.",
              "Half of 10 is 5, and the top number 7 is more than 5, so 7/10 is more than 1/2.",
              "5/12 is to the left of 1/2 and 7/10 is to the right of 1/2, so 5/12 < 7/10.",
              "The bigger bottom number does not make the bigger fraction: 12 is more than 10, but 5/12 is less "
              "than 7/10.",
              "Rule: use 1/2 when it separates the two fractions. A fraction less than 1/2 is less than a fraction "
              "more than 1/2. If both are on the same side of 1/2, it cannot decide."],
       examples=[WE("Which is more, 5/12 or 7/10? Use 1/2 as the reference.",
                    ["Half of 12 is 6, because 6 + 6 = 12. The top number 5 is less than 6, so 5/12 is less than "
                     "1/2.",
                     "Half of 10 is 5, because 5 + 5 = 10. The top number 7 is more than 5, so 7/10 is more than "
                     "1/2.",
                     "5/12 is on the left of 1/2 and 7/10 is on the right of 1/2.",
                     "A fraction less than 1/2 is less than a fraction more than 1/2, so 5/12 < 7/10.",
                     "Check: 5/12 + 1/12 = 6/12 = 1/2, so 5/12 is 1/12 short of 1/2. 7/10 − 2/10 = 5/10 = 1/2, so "
                     "7/10 is 2/10 past 1/2."],
                    "7/10 is more. 5/12 is less than 1/2 and 7/10 is more than 1/2, so 5/12 < 7/10")],
       key_terms=["less than half", "more than half", "compare"],
       misconceptions=["M_BIGGER_DENOM", "M_NEAR_HALF"], minutes=7),
     DOER("T8.C4", "Practice: Benchmark Number Line", "benchmark_line", "Apply",
          "Students compare fractions using 1 and 1/2 as references, circle the fractions that are equal to 1/2 or "
          "less than 1/2, and give the reason from the top and bottom numbers in the book's questions.",
          ["Check a fraction against 1: top number less than bottom number is less than 1, equal is exactly 1 and "
           "more is more than 1.",
           "A fraction less than 1 is less than a fraction more than 1.",
           "A fraction is equal to 1/2 when its top number is half of its bottom number.",
           "Find half of the bottom number and compare the top number with it. Less means less than 1/2 and more "
           "means more than 1/2."],
          items=[
              FIO("r1.example", "Example 8: 7/8 paratha and 8/6 paratha",
                  "Let us compare some more fractions. Between Sevi and Shami can you tell who ate less? One child "
                  "says: I ate 7/8 paratha yesterday evening. The other says: I ate 8/6 paratha yesterday evening.",
                  ["7/8 is 7 pieces of 1/8. 8 pieces of 1/8 make 1 paratha, and 7 is less than 8, so 7/8 is less "
                   "than 1.",
                   "8/6 is 8 pieces of 1/6. 6 pieces of 1/6 make 1 paratha, and 8 is more than 6, so 8/6 is more "
                   "than 1.",
                   "7/8 is less than 1 and 8/6 is more than 1, so 7/8 < 8/6.",
                   "The child who ate 7/8 paratha ate less.",
                   "Check: 8/6 = 6/6 + 2/6 = 1 2/6, so that child ate 1 whole paratha and 2 more pieces, while the "
                   "other child did not finish 1 paratha."],
                  "The child who ate 7/8 paratha ate less, because 7/8 is less than 1 and 8/6 is more than 1, so "
                  "7/8 < 8/6.",
                  kind="example",
                  q_figure="One round paratha cut into 8 equal pieces with 7 pieces marked, and two round parathas "
                           "each cut into 6 equal pieces with 8 pieces marked in all.",
                  s_figure="A number line from 0 to 2 with a signpost at 1, a dot for 7/8 to the left of 1 and a dot "
                           "for 8/6 to the right of 1."),
              FIO("LUDr1.Q1", "Let Us Do (reference to 1), Q1",
                  "Compare the following fractions using 1 as a reference. Share your reasoning in the class. "
                  "(a) 8/7 ___ 9/15 (b) 13/20 ___ 17/15 (c) 7/6 ___ 8/8 (d) 6/6 ___ 19/12 (e) 12/9 ___ 4/5 "
                  "(f) 15/5 ___ 16/4",
                  ["(a) 8/7 is more than 1 (8 is more than 7) and 9/15 is less than 1 (9 is less than 15), so "
                   "8/7 > 9/15.",
                   "(b) 13/20 is less than 1 (13 is less than 20) and 17/15 is more than 1 (17 is more than 15), so "
                   "13/20 < 17/15.",
                   "(c) 7/6 is more than 1 (7 is more than 6) and 8/8 is exactly 1, so 7/6 > 8/8.",
                   "(d) 6/6 is exactly 1 and 19/12 is more than 1 (19 is more than 12), so 6/6 < 19/12.",
                   "(e) 12/9 is more than 1 (12 is more than 9) and 4/5 is less than 1 (4 is less than 5), so "
                   "12/9 > 4/5.",
                   "(f) 15/5 is more than 1 (15 is more than 5) and 16/4 is more than 1 (16 is more than 4). Both "
                   "are on the same side of 1, so 1 cannot decide.",
                   "Count the wholes instead: 15/5 = 15 ÷ 5 = 3 wholes, and 16/4 = 16 ÷ 4 = 4 wholes.",
                   "3 wholes are less than 4 wholes, so 15/5 < 16/4.",
                   "Check: in parts (a) to (e) the two fractions are on different sides of 1 or one of them is "
                   "exactly 1. Only part (f) needed a different reason."],
                  "(a): >; (b): <; (c): >; (d): <; (e): >; (f): <",
                  kind="exercise"),
              FIO("LUDh.Q1", "Let Us Do (reference to 1/2), Q1",
                  "Circle the fractions below that are equal to 1/2. 2/4, 3/5, 5/7, 7/14, 5/10, 8/16, 5/9, 6/12, "
                  "10/20, 6/8",
                  ["A fraction is equal to 1/2 when its top number is half of its bottom number. Check each "
                   "fraction.",
                   "2/4: half of 4 is 2, and the top number is 2, so 2/4 = 1/2.",
                   "3/5: half of 5 is 2 1/2, and 3 is not 2 1/2, so 3/5 is not equal to 1/2.",
                   "5/7: half of 7 is 3 1/2, and 5 is not 3 1/2, so 5/7 is not equal to 1/2.",
                   "7/14: half of 14 is 7, and the top number is 7, so 7/14 = 1/2.",
                   "5/10: half of 10 is 5, and the top number is 5, so 5/10 = 1/2.",
                   "8/16: half of 16 is 8, and the top number is 8, so 8/16 = 1/2.",
                   "5/9: half of 9 is 4 1/2, and 5 is not 4 1/2, so 5/9 is not equal to 1/2. It is close to half, "
                   "but close is not equal.",
                   "6/12: half of 12 is 6, and the top number is 6, so 6/12 = 1/2.",
                   "10/20: half of 20 is 10, and the top number is 10, so 10/20 = 1/2.",
                   "6/8: half of 8 is 4, and 6 is not 4, so 6/8 is not equal to 1/2. In fact 6/8 = 3/4.",
                   "Check: 6 fractions are equal to 1/2 and 4 are not, and 6 + 4 = 10 fractions in all."],
                  "2/4, 7/14, 5/10, 8/16, 6/12 and 10/20 are equal to 1/2",
                  kind="exercise",
                  q_figure="A box with 10 fractions scattered inside it: 2/4, 3/5, 5/7, 7/14, 5/10, 8/16, 5/9, 6/12, "
                           "10/20 and 6/8, each written with its top and bottom number.",
                  s_figure="The same box with the fractions 2/4, 7/14, 5/10, 8/16, 6/12 and 10/20 circled."),
              FIO("LUDh.Q2", "Let Us Do (reference to 1/2), Q2",
                  "Some fractions are written in the box below. Circle the fractions that are less than half. How "
                  "do you know? Discuss your reasoning in the class. 3/9, 2/4, 12/15, 8/15, 11/12, 3/15, 4/8, 1/3, "
                  "7/11, 11/16, 15/31, 6/18",
                  ["A fraction is less than half when its top number is less than half of its bottom number. Check "
                   "each fraction.",
                   "3/9: half of 9 is 4 1/2, and 3 is less than 4 1/2, so 3/9 is less than half.",
                   "2/4: half of 4 is 2, and the top number is 2, so 2/4 is equal to half, not less.",
                   "12/15: half of 15 is 7 1/2, and 12 is more than 7 1/2, so 12/15 is more than half.",
                   "8/15: half of 15 is 7 1/2, and 8 is more than 7 1/2, so 8/15 is more than half.",
                   "11/12: half of 12 is 6, and 11 is more than 6, so 11/12 is more than half.",
                   "3/15: half of 15 is 7 1/2, and 3 is less than 7 1/2, so 3/15 is less than half.",
                   "4/8: half of 8 is 4, and the top number is 4, so 4/8 is equal to half, not less.",
                   "1/3: half of 3 is 1 1/2, and 1 is less than 1 1/2, so 1/3 is less than half.",
                   "7/11: half of 11 is 5 1/2, and 7 is more than 5 1/2, so 7/11 is more than half.",
                   "11/16: half of 16 is 8, and 11 is more than 8, so 11/16 is more than half.",
                   "15/31: half of 31 is 15 1/2, and 15 is less than 15 1/2, so 15/31 is less than half.",
                   "6/18: half of 18 is 9, and 6 is less than 9, so 6/18 is less than half.",
                   "Circle the fractions less than half: 3/9, 3/15, 1/3, 15/31 and 6/18.",
                   "Check: 5 fractions are less than half, 2 are equal to half and 5 are more than half, and "
                   "5 + 2 + 5 = 12 fractions in all."],
                  "3/9, 3/15, 1/3, 15/31 and 6/18 are less than half. We know because the top number of each is "
                  "less than half of its bottom number.",
                  kind="exercise",
                  q_figure="A box with 12 fractions scattered inside it: 3/9, 2/4, 12/15, 8/15, 11/12, 3/15, 4/8, "
                           "1/3, 7/11, 11/16, 15/31 and 6/18, each written with its top and bottom number.",
                  s_figure="The same box with the fractions 3/9, 3/15, 1/3, 15/31 and 6/18 circled."),
              FIO("rh.example", "Example 9: 5/8 paratha and 3/6 paratha",
                  "Now let us compare fractions using 1/2. One child says: I ate 5/8 paratha yesterday evening. The "
                  "other says: I ate 3/6 paratha yesterday evening. Who do you think ate more paratha?",
                  ["3/6 is 3 pieces of 1/6. Half of 6 is 3, and the top number is 3, so 3/6 is exactly half of a "
                   "paratha.",
                   "5/8 is 5 pieces of 1/8. Half of 8 is 4, and 5 is more than 4, so 5/8 is more than 1/2.",
                   "5/8 is more than 1/2 and 3/6 = 1/2, so 5/8 > 3/6.",
                   "The child who ate 5/8 paratha ate more.",
                   "Check: 5/8 = 4/8 + 1/8 = 1/2 + 1/8, so 5/8 is 1/8 more than half, and 3/6 is exactly half."],
                  "The child who ate 5/8 paratha ate more, because 5/8 is more than 1/2 and 3/6 is equal to 1/2, "
                  "so 5/8 > 3/6.",
                  kind="example",
                  q_figure="A round paratha cut into 8 equal pieces with 5 pieces marked, and a round paratha cut "
                           "into 6 equal pieces with 3 pieces marked.",
                  s_figure="The same two parathas with a line across each one at half: the 3 marked pieces of 1/6 "
                           "fill exactly half of their paratha and the 5 marked pieces of 1/8 fill more than half "
                           "of theirs."),
              FIO("LUDh.Q3", "Let Us Do (reference to 1/2), Q3",
                  "Compare the following fractions. Where possible, compare the fractions with 1/2. (a) 2/9 and 4/7 "
                  "(b) 11/14 and 7/20 (c) 5/7 and 3/9 (d) 6/7 and 4/10 (e) 9/17 and 3/15 (f) 7/12 and 3/11 "
                  "(g) 1/3 and 5/9 (h) 3/9 and 4/7",
                  ["(a) 2/9 is less than 1/2, because half of 9 is 4 1/2 and 2 is less than 4 1/2. 4/7 is more than 1/2, "
                   "because half of 7 is 3 1/2 and 4 is more than 3 1/2. So 2/9 < 4/7.",
                   "(b) 11/14 is more than 1/2, because half of 14 is 7 and 11 is more than 7. 7/20 is less than "
                   "1/2, because half of 20 is 10 and 7 is less than 10. So 11/14 > 7/20.",
                   "(c) 5/7 is more than 1/2, because half of 7 is 3 1/2 and 5 is more than 3 1/2. 3/9 is less than "
                   "1/2, because half of 9 is 4 1/2 and 3 is less than 4 1/2. So 5/7 > 3/9.",
                   "(d) 6/7 is more than 1/2, because half of 7 is 3 1/2 and 6 is more than 3 1/2. 4/10 is less "
                   "than 1/2, because half of 10 is 5 and 4 is less than 5. So 6/7 > 4/10.",
                   "(e) 9/17 is more than 1/2, because half of 17 is 8 1/2 and 9 is more than 8 1/2. 3/15 is less "
                   "than 1/2, because half of 15 is 7 1/2 and 3 is less than 7 1/2. So 9/17 > 3/15.",
                   "(f) 7/12 is more than 1/2, because half of 12 is 6 and 7 is more than 6. 3/11 is less than "
                   "1/2, because half of 11 is 5 1/2 and 3 is less than 5 1/2. So 7/12 > 3/11.",
                   "(g) 1/3 is less than 1/2, because half of 3 is 1 1/2 and 1 is less than 1 1/2. 5/9 is more "
                   "than 1/2, because half of 9 is 4 1/2 and 5 is more than 4 1/2. So 1/3 < 5/9.",
                   "(h) 3/9 is less than 1/2, because half of 9 is 4 1/2 and 3 is less than 4 1/2. 4/7 is more "
                   "than 1/2, because half of 7 is 3 1/2 and 4 is more than 3 1/2. So 3/9 < 4/7.",
                   "Check: in every part one fraction is less than 1/2 and the other is more than 1/2, so 1/2 "
                   "decides all eight pairs."],
                  "(a): <; (b): >; (c): >; (d): >; (e): >; (f): >; (g): <; (h): <",
                  kind="exercise",
                  q_figure="A table with 2 rows and 4 columns, and each box holds a pair of fractions: 2/9 and 4/7, "
                           "11/14 and 7/20, 5/7 and 3/9, 6/7 and 4/10 in the first row, and 9/17 and 3/15, 7/12 and "
                           "3/11, 1/3 and 5/9, 3/9 and 4/7 in the second row.",
                  s_figure="The same table with the sign < or > written between the two fractions of every pair.")],
          misconceptions=["M_NEAR_HALF", "M_TOP_ONLY", "M_BIGGER_DENOM"])],
    key_terms=["reference", "less than", "more than", "half"]))
