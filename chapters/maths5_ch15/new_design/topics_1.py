# -*- coding: utf-8 -*-
"""Topics T1, T1B, T2 and T3 (module M1: Recording Data and Pictographs). The framing intro (Samaira and Kabir ask 35
friends, hook and the free Reporter's Notebook), the idea topic T1B (Recording Data in a Table with the opener's
table and its four questions), Pictographs and Scales (Joseph Uncle's shop) and Reading a Pictograph (Deepti's
two-wheelers).
Every teaching concept has one worked example with the plan's own numbers (practice values); every book question is
an FIO item of its topic's DOER, in the book's order, with the verified answers of DESIGN section 4."""
from topics_common import A, DOER, FIO, TOPIC, WE
from figs import ROAD, SHOP, TV_NOTEBOOK, TV_TABLE, TV_TABLE_EMPTY

TOPICS = []


def _join(first, second):
    """Two figure sentences of figs.py joined into one plain sentence."""
    return first.rstrip(".") + ", and " + second[0].lower() + second[1:]


# ============================== T1 Child TV Reporter (framing) =============================================
# The framing topic holds only the hook video and the free-try tool, and no book question. The concept video and the
# four table questions follow in the idea topic T1B.
TOPICS.append(TOPIC(
    "T1", "M1", "Child TV Reporter", ["Chapter opening"], "Understand",
    "",
    "Samaira and Kabir ask 35 friends how many hours a day they watch TV and write every answer in a notebook. Open "
    "the notebook, sort the answers into the rows of a table and see what the notebook says.",
    [A("T1.C1", "Samaira and Kabir Ask 35 Friends", "Understand",
       "",
       textbook=["Samaira and Kabir decided to act like reporters and collect information from their friends.",
                 "How many hours a day do you spend watching TV?",
                 "They collected data from 35 friends and recorded it in a notebook as shown below."],
       teach=["Predict first: Samaira and Kabir fill a whole notebook with answers from their friends. What could they "
              "do to find out what all the answers say?",
              "Samaira and Kabir decided to act like reporters and collect information from their friends.",
              "They asked every friend one question: How many hours a day do you spend watching TV?",
              "They collected data from 35 friends and recorded every answer in a notebook, in a speech bubble beside "
              "each face.",
              "The bubbles say 1/2 hr, 1 hr, 1 1/2 hr, 2 hr or 2 1/2 hr, all mixed up on one page.",
              "The notebook is full of answers, in no order at all. Can you find a way to see what the 35 answers "
              "say?"],
       ncert=["tv.story"], key_terms=["data", "notebook", "answers"],
       video_focus=["HOOK"], enrichment=True, minutes=4),
     DOER("T1.C3", "Reporter's Notebook: Explore", "reporters_notebook", "Understand",
          "",
          ["Samaira and Kabir asked 35 friends how many hours a day they watch TV.",
           "Every answer is in a speech bubble in the notebook.",
           "Move each answer into the row of the table where it belongs, then read the counts."],
          misconceptions=["M_COUNT_TWICE"], role="try_it", enrichment=True)],
    topic_type="framing", key_terms=["data", "notebook", "table"]))

# ============================== T1B Recording Data in a Table ==============================================
TOPICS.append(TOPIC(
    "T1B", "M1", "Recording Data in a Table", ["Child TV Reporter"], "Apply",
    "Students record the answers of many friends in a table with one row for each kind of answer, count each row, "
    "check that the counts add up, and use the table to say how many children answered more than or less than an "
    "amount.",
    "A table has one row for each kind of answer. Count each row and check that the counts add up to the number of "
    "friends asked. Add the rows after a row for more than, and the rows before a row for less than.",
    [A("T1B.C1", "Counting and Recording in a Table", "Apply",
       "Students record 12 answers in a table with one row for each kind of answer, count each row, and check that "
       "the counts add up to 12.",
       textbook=["No. of Hours Spent Watching TV",
                 "No. of Children",
                 "Can watching TV for a long time be harmful to the eyes?"],
       teach=["Predict first: Kabir asks 12 friends how many hours a day they read. The answers are 1 hr, 2 hr, 1 hr, "
              "1 hr, 3 hr, 2 hr, 1 hr, 2 hr, 1 hr, 3 hr, 1 hr and 2 hr. How can he show them so that anyone can read "
              "them quickly?",
              "Make a table with one row for each kind of answer: 1 hour, 2 hours and 3 hours.",
              "Move each answer into its row, once. Then count each row: the row 1 hour has 6 answers, the row "
              "2 hours has 4 and the row 3 hours has 2.",
              "Check that the counts add up to the number of friends: 6 + 4 + 2 = 12. If they do not, an answer was "
              "counted twice or missed.",
              "A row can also name a group of answers, like the row More than 2 hours in your maths book's table. "
              "An answer of 2 1/2 hr goes in that row.",
              "For more than 1 hour, add the rows after the row 1 hour: 4 + 2 = 6. The row 1 hour is not in it.",
              "For less than 3 hours, add the rows before the row 3 hours: 6 + 4 = 10.",
              "Can watching TV for a long time be harmful to the eyes? Think about it.",
              "Rule: make one row for each kind of answer, count each row, and check that the counts add up to the "
              "number of friends."],
       examples=[WE("Kabir asks 12 friends how many hours a day they read (practice values). The answers are 1 hr, "
                    "2 hr, 1 hr, 1 hr, 3 hr, 2 hr, 1 hr, 2 hr, 1 hr, 3 hr, 1 hr and 2 hr. Make a table and find how "
                    "many friends read for more than 1 hour.",
                    ["The answers are 1 hr, 2 hr or 3 hr, so the table has three rows: 1 hour, 2 hours and 3 hours.",
                     "Move the answers of 1 hr into the row 1 hour. They are the 1st, 3rd, 4th, 7th, 9th and 11th "
                     "answers, so the row has 6 friends.",
                     "Move the answers of 2 hr into the row 2 hours. They are the 2nd, 6th, 8th and 12th answers, so "
                     "the row has 4 friends.",
                     "Move the answers of 3 hr into the row 3 hours. They are the 5th and 10th answers, so the row "
                     "has 2 friends.",
                     "More than 1 hour is the rows after the row 1 hour: the rows 2 hours and 3 hours. Add them: "
                     "4 + 2 = 6.",
                     "The 6 friends in the row 1 hour read for exactly 1 hour, not more, so they are left out.",
                     "Check: 6 + 4 + 2 = 12, so every answer was counted once. The 6 friends in the row 1 hour and "
                     "the 6 friends who read for more than 1 hour add up to 6 + 6 = 12."],
                    "6 friends read for more than 1 hour. The rows are 1 hour 6, 2 hours 4 and 3 hours 2, and "
                    "6 + 4 + 2 = 12.")],
       ncert=["tv.tablehead", "tv.eyes"], key_terms=["table", "row", "record", "data"],
       misconceptions=["M_COUNT_TWICE", "M_MORE_THAN_INCLUDES"], minutes=6),
     DOER("T1B.C2", "Practice: Child TV Reporter", None, "Apply",
          "Students fill the Child TV Reporter table by counting the 35 answers row by row, and use the counts to "
          "say how many children watch TV for more than, less than or exactly an amount of time.",
          ["Make one row for each kind of answer and count each row.",
           "Check that the counts add up to the number of friends asked, here 35.",
           "For more than, add the rows after a row. For less than, add the rows before a row.",
           "The row named in the question is left out: it is exactly that amount, not more and not less."],
          items=[FIO("tv.table", "Child TV Reporter: fill the table",
                     "Samaira and Kabir asked 35 friends: How many hours a day do you spend watching TV? Their "
                     "answers are in the notebook. Fill in the number of children in each row of the table.",
                     ["Each of the 35 speech bubbles is one child's answer. Mark each bubble as you count it, so no "
                      "answer is counted twice.",
                      "9 bubbles say 1/2 hr, so the row 1/2 hour is 9.",
                      "13 bubbles say 1 hr, so the row 1 hour is 13.",
                      "7 bubbles say 1 1/2 hr, so the row 1 1/2 hour is 7.",
                      "3 bubbles say 2 hr, so the row 2 hours is 3.",
                      "3 bubbles say 2 1/2 hr. These answers are more than 2 hours, so the three 2 1/2 hr answers go "
                      "in the row More than 2 hours: 3.",
                      "Check: add the rows, 9 + 13 + 7 + 3 + 3 = 35, the number of friends asked, so every answer is "
                      "in a row once."],
                     "1/2 hour 9, 1 hour 13, 1 1/2 hour 7, 2 hours 3, More than 2 hours 3, in all 35 children.",
                     kind="prompt",
                     q_figure=_join(TV_NOTEBOOK, TV_TABLE_EMPTY),
                     s_figure=TV_TABLE),
                 FIO("tv.q1", "Child TV Reporter: more than half an hour",
                     "How many children watch TV for more than half an hour?",
                     ["More than half an hour is every row after the row 1/2 hour.",
                      "The rows after 1/2 hour are 1 hour, 1 1/2 hour, 2 hours and More than 2 hours.",
                      "Read their counts from the table: 13, 7, 3 and 3.",
                      "Add the counts: 13 + 7 + 3 + 3 = 26.",
                      "The row 1/2 hour is exactly half an hour, not more, so its 9 children are left out.",
                      "Check: 35 − 9 = 26, the children left after taking away the 9 children of the row 1/2 hour."],
                     "26 children.",
                     kind="exercise",
                     q_figure=TV_TABLE,
                     s_figure="The same table with the counts 13, 7, 3 and 3 of the four rows after 1/2 hour "
                              "outlined in orange and the sum 26 written below the table."),
                 FIO("tv.q2", "Child TV Reporter: less than two hours",
                     "How many children watch TV for less than two hours?",
                     ["Less than two hours is every row before the row 2 hours.",
                      "The rows before 2 hours are 1/2 hour, 1 hour and 1 1/2 hour.",
                      "Read their counts from the table: 9, 13 and 7.",
                      "Add the counts: 9 + 13 + 7 = 29.",
                      "The row 2 hours is exactly two hours, not less, and the row More than 2 hours is more, so "
                      "their 3 + 3 children are left out.",
                      "Check: 29 + 3 + 3 = 35, so no row is missed."],
                     "29 children.",
                     kind="exercise",
                     q_figure=TV_TABLE,
                     s_figure="The same table with the counts 9, 13 and 7 of the rows 1/2 hour, 1 hour and 1 1/2 hour "
                              "outlined in orange and the sum 29 written below the table."),
                 FIO("tv.q3", "Child TV Reporter: more than two hours",
                     "The number of children who watch TV for more than two hours is ___.",
                     ["Find the row More than 2 hours in the table.",
                      "Read the number in that row: 3.",
                      "These are the three children whose answer in the notebook was 2 1/2 hr.",
                      "Check: 2 1/2 hr is more than 2 hr, and no other answer in the notebook is more than 2 hr."],
                     "3 children.",
                     kind="exercise",
                     q_figure=TV_TABLE,
                     s_figure="The same table with the count 3 in the row More than 2 hours outlined in orange."),
                 FIO("tv.q4", "Child TV Reporter: two hours or half an hour",
                     "More children watch TV for two hours than half an hour. (True/False)",
                     ["Find the row 2 hours in the table: 3 children.",
                      "Find the row 1/2 hour in the table: 9 children.",
                      "Compare the two counts: 3 is less than 9, so fewer children watch for two hours than for half "
                      "an hour.",
                      "The statement says that more children watch for two hours, so it is not true.",
                      "Check: the other way round, 9 is more than 3, so more children watch for half an hour."],
                     "False. 3 children watch for 2 hours and 9 children watch for half an hour.",
                     kind="exercise",
                     q_figure=TV_TABLE,
                     s_figure="The same table with the count 3 in the row 2 hours and the count 9 in the row 1/2 hour "
                              "outlined in orange, and the word False written below the table.")],
          misconceptions=["M_COUNT_TWICE", "M_MORE_THAN_INCLUDES"])],
    key_terms=["table", "row", "record", "data"]))

# ============================== T2 Pictographs and Scales ==================================================
TOPICS.append(TOPIC(
    "T2", "M1", "Pictographs and Scales", ["Stock-Taking in a Shop"], "Apply",
    "Students show numbers with icons using a scale, read a row of icons back as a number, choose a scale that fits "
    "every number and show the same data with another scale.",
    "A scale lets one icon stand for several items, so a large number needs fewer icons. The number of items is the "
    "number of icons × the scale, and a scale must fit every number with nothing left over.",
    [A("T2.C1", "One Icon for Many Items", "Apply",
       "Students show numbers as icons using a scale of 5 and read a row of icons back as a number by multiplying the "
       "number of icons by the scale.",
       textbook=["Joseph Uncle takes stock of the play items (toys, board games, and sports items) in his store a week "
                 "before the summer break. He tries to record the items in his shop using a pictograph.",
                 "He notices that there are too many items of each kind in his shop and it is not easy to make a "
                 "picture for every item.",
                 "How can I show these with pictures?",
                 "Suggest some ways to him.",
                 "Dipesh, one of his helpers, suggested using one picture (icon) for every 5 items of each kind.",
                 "Dipesh used a scale while recording the items in the pictograph. A scale helps record a large number "
                 "of things using fewer icons."],
       teach=["Predict first: a shop has 35 erasers. Drawing one picture for each eraser is too much work. What could "
              "the shopkeeper do?",
              "Use one icon for 5 erasers. This is what Dipesh suggests to Joseph Uncle: one icon for every 5 items.",
              "The icon box tells what one icon stands for. It is called the scale: 1 icon = 5 items.",
              "7 icons show 35 erasers, because 7 × 5 = 35. That is 7 icons instead of 35 pictures.",
              "To read a pictograph, count the icons in a row and multiply by the scale.",
              "Rule: the number of items = the number of icons × the scale. A scale helps record a large number of "
              "things using fewer icons."],
       examples=[WE("A stationery shop has 10 pens, 20 pencils and 35 erasers (practice values). Show them in a "
                    "pictograph where one icon stands for 5 items, then read the pictograph back.",
                    ["The scale is 1 icon = 5 items, so each row needs as many icons as there are groups of 5 in its number.",
                     "Pens: 10 ÷ 5 = 2, so the row has 2 icons.",
                     "Pencils: 20 ÷ 5 = 4, so the row has 4 icons.",
                     "Erasers: 35 ÷ 5 = 7, so the row has 7 icons.",
                     "Read the rows back, icons × scale: 2 × 5 = 10 pens, 4 × 5 = 20 pencils and 7 × 5 = 35 erasers.",
                     "Count all the icons: 2 + 4 + 7 = 13 icons, and 13 × 5 = 65 items in all.",
                     "Check: 10 + 20 + 35 = 65, the same 65 items."],
                    "Pens 2 icons, pencils 4 icons and erasers 7 icons. The 13 icons stand for 65 items.")],
       ncert=["shop.story", "shop.suggest", "shop.scale"], key_terms=["pictograph", "icon", "scale"],
       misconceptions=["M_ICON_IS_ONE"], minutes=6),
     A("T2.C2", "Choosing a Different Scale", "Apply",
       "Students choose a scale that fits all the numbers of a table, show the numbers with it and explain why another "
       "scale does not fit.",
       teach=["Predict first: a fruit stall has 12 apples, 18 oranges and 30 bananas. Can one icon stand for 4 "
              "fruits?",
              "Try a scale of 4. For the apples, 12 ÷ 4 = 3, which fits. For the oranges, 18 ÷ 4 is 4 with 2 left "
              "over. So a scale of 4 does not fit.",
              "A scale of 6 fits every number: 12 ÷ 6 = 2, 18 ÷ 6 = 3 and 30 ÷ 6 = 5. The rows have 2, 3 and 5 icons.",
              "A scale of 3 fits too: 12 ÷ 3 = 4, 18 ÷ 3 = 6 and 30 ÷ 3 = 10. The rows have 4, 6 and 10 icons.",
              "A bigger scale needs fewer icons: the scale 6 needs 2 + 3 + 5 = 10 icons and the scale 3 needs "
              "4 + 6 + 10 = 20 icons.",
              "Rule: choose a scale that fits every number, so that every number can be shared into groups of the "
              "scale with nothing left over."],
       examples=[WE("A fruit stall has 12 apples, 18 oranges and 30 bananas (practice values). Does a scale of 4 fit? "
                    "Choose a scale that fits and show the numbers with icons.",
                    ["A scale fits when every number can be shared into groups of the scale with nothing left over.",
                     "Try a scale of 4. For the apples, 12 ÷ 4 = 3, which fits.",
                     "For the oranges, 18 ÷ 4 is 4 with 2 left over, so a scale of 4 does not fit.",
                     "Try a scale of 6. 12 ÷ 6 = 2, 18 ÷ 6 = 3 and 30 ÷ 6 = 5. Every number fits, so 1 icon = 6 fruits "
                     "works, with 2, 3 and 5 icons.",
                     "Try a scale of 3. 12 ÷ 3 = 4, 18 ÷ 3 = 6 and 30 ÷ 3 = 10, so 1 icon = 3 fruits works too, with "
                     "4, 6 and 10 icons.",
                     "The bigger scale 6 needs fewer icons than the scale 3: 2 + 3 + 5 = 10 icons and 4 + 6 + 10 = 20 "
                     "icons.",
                     "Check: read the scale 6 back, 2 × 6 = 12, 3 × 6 = 18 and 5 × 6 = 30."],
                    "A scale of 4 does not fit. A scale of 6 fits, with 2, 3 and 5 icons, and a scale of 3 fits, with "
                    "4, 6 and 10 icons.")],
       key_terms=["scale", "icon", "fit", "pictograph"],
       misconceptions=["M_SCALE_NO_FIT", "M_BIG_SCALE_MORE"], minutes=6),
     DOER("T2.C3", "Practice: Stock-Taking in a Shop", "pictograph_maker", "Apply",
          "Students read the pictograph of the shop as icons times the scale to find the number of toys, board games "
          "and all the play items in stock, and show the same stock with another scale.",
          ["One icon stands for the scale, so the number of items = the number of icons × the scale.",
           "To find a total, find every row and add them, or add all the icons and multiply by the scale.",
           "A scale must fit every number, with nothing left over.",
           "The same data can be shown with another scale that fits."],
          items=[FIO("shop.q1", "Stock-Taking in a Shop: toys",
                     "How many toys does Joseph Uncle have? ___",
                     ["Look at the icon box: 1 train icon stands for 5 toys.",
                      "Count the train icons in the row Toys: 8.",
                      "Multiply the icons by the scale: 8 × 5 = 40.",
                      "Check: 40 ÷ 5 = 8, the number of train icons."],
                     "40 toys.",
                     kind="exercise",
                     q_figure=SHOP,
                     s_figure="The same pictograph with the 8 train icons of the row Toys outlined in orange and the "
                              "number 40 written at the end of the row."),
                 FIO("shop.q2", "Stock-Taking in a Shop: board games",
                     "How many board games does Joseph Uncle have? ___",
                     ["Look at the icon box: 1 board game icon stands for 5 board games.",
                      "Count the board game icons in the row Board games: 10.",
                      "Multiply the icons by the scale: 10 × 5 = 50.",
                      "Check: 50 ÷ 5 = 10, the number of board game icons."],
                     "50 board games.",
                     kind="exercise",
                     q_figure=SHOP,
                     s_figure="The same pictograph with the 10 board game icons of the row Board games outlined in "
                              "orange and the number 50 written at the end of the row."),
                 FIO("shop.q3", "Stock-Taking in a Shop: total play items",
                     "How many total play items does Joseph Uncle have? ___",
                     ["Find the number in each row first. Toys: 8 icons, 8 × 5 = 40.",
                      "Board games: 10 icons, 10 × 5 = 50.",
                      "Sports items: 12 icons, 12 × 5 = 60.",
                      "Add the three rows: 40 + 50 + 60 = 150.",
                      "Check: count all the icons, 8 + 10 + 12 = 30, and 30 × 5 = 150."],
                     "150 play items.",
                     kind="exercise",
                     q_figure=SHOP,
                     s_figure="The same pictograph with the numbers 40, 50 and 60 written at the end of the three rows "
                              "and the total 150 written below."),
                 FIO("shop.choose", "Stock-Taking in a Shop: choose your scale",
                     "Is there any other scale that you can use to make the pictograph? Choose your scale and show the "
                     "same data using a pictograph in your notebook.",
                     ["The numbers to show are 40 toys, 50 board games and 60 sports items.",
                      "A scale fits when every number can be shared into groups of the scale with nothing left over.",
                      "Try a scale of 10: 40 ÷ 10 = 4, 50 ÷ 10 = 5 and 60 ÷ 10 = 6. Every number fits.",
                      "With 1 icon standing for 10 items, toys have 4 icons, board games have 5 icons and sports items have 6 "
                      "icons.",
                      "A scale of 2 fits too, with 20, 25 and 30 icons. A scale of 4 does not fit, because 50 ÷ 4 is "
                      "12 with 2 left over.",
                      "Draw the icons of each row and write the icon box: 1 icon stands for 10 items.",
                      "Check: read back, 4 × 10 = 40, 5 × 10 = 50 and 6 × 10 = 60, the same numbers as before."],
                     "Sample answer: scale 10, with toys 4 icons, board games 5 icons and sports items 6 icons. Your "
                     "answer may differ.",
                     kind="prompt",
                     q_figure=SHOP,
                     s_figure="A pictograph with the icon box 1 train icon = 10 toys, 1 board game icon = 10 board "
                              "games and 1 racket icon = 10 sports items, and three rows: Toys with 4 train icons, "
                              "Board games with 5 board game icons and Sports items with 6 racket icons.")],
          misconceptions=["M_ICON_IS_ONE", "M_SCALE_NO_FIT"])],
    key_terms=["pictograph", "icon", "scale"]))

# ============================== T3 Reading a Pictograph ====================================================
TOPICS.append(TOPIC(
    "T3", "M1", "Reading a Pictograph", ["Two-wheelers on the Road"], "Apply",
    "Students read each row of a pictograph as icons × the scale, find the most and the total, and find how many more "
    "or how many fewer one row is than another.",
    "Read each row of a pictograph as icons × the scale. Then the most is the biggest number, the total is all the "
    "rows added, and how many more or fewer is the difference of two rows.",
    [A("T3.C1", "Comparing with a Pictograph", "Apply",
       "Students read the numbers of a pictograph, find the most and the total, and find how many more or how many "
       "fewer one row is than another.",
       textbook=["Deepti noted down the number of two-wheelers passing her house in one hour on three different days.",
                 "She used one icon to show 3 two-wheelers."],
       teach=["Predict first: a snack stall's pictograph has 3 icons for Tuesday and 7 icons for Thursday, and one icon "
              "= 10 samosas. Which day sold more samosas, and how many more?",
              "Read each row, icons × scale. Tuesday: 3 × 10 = 30 samosas. Thursday: 7 × 10 = 70 samosas.",
              "When every icon stands for the same number, the row with more icons is more. So Thursday sold more.",
              "How many more? Find the difference: 70 − 30 = 40. You can also take the icons first: 7 − 3 = 4 icons, "
              "and 4 × 10 = 40.",
              "For the total of the two days, add the rows: 30 + 70 = 100. You can also add the icons first: 3 + 7 = "
              "10 icons, and 10 × 10 = 100.",
              "Rule: read each row as icons × scale. The most is the biggest number, the total is all the rows added, "
              "and how many more or fewer is the difference."],
       examples=[WE("A snack stall's pictograph (practice values): one icon = 10 samosas. Tuesday has 3 icons, "
                    "Thursday has 7 icons and Saturday has 2 icons. Which day sold the most, how many samosas were "
                    "sold in all, how many fewer on Saturday than on Tuesday and how many more on Thursday than on "
                    "Saturday?",
                    ["Read each row, icons × scale: Tuesday 3 × 10 = 30, Thursday 7 × 10 = 70 and Saturday "
                     "2 × 10 = 20 samosas.",
                     "The most: 70 is more than 30 and 20, so Thursday sold the most, 70 samosas.",
                     "Count all the icons: 3 + 7 + 2 = 12 icons, and 12 × 10 = 120 samosas in all.",
                     "Fewer on Saturday than on Tuesday: find the difference, 30 − 20 = 10.",
                     "More on Thursday than on Saturday: find the difference, 70 − 20 = 50.",
                     "Check: add the three rows, 30 + 70 + 20 = 120, the same 120 samosas."],
                    "Thursday sold the most, 70. In all 120 samosas. Saturday sold 10 fewer than Tuesday, and Thursday "
                    "sold 50 more than Saturday.")],
       ncert=["road.story"], key_terms=["pictograph", "icon", "scale", "total"],
       misconceptions=["M_ICON_IS_ONE"], minutes=6),
     DOER("T3.C2", "Practice: Two-wheelers on the Road", None, "Apply",
          "Students read the two-wheelers on Deepti's pictograph as icons times the scale, find the most, the total "
          "and the differences, and show the same data with another scale.",
          ["Read each row as icons × scale.",
           "With the same icon and scale, the row with the most icons is the most.",
           "How many more or fewer is the difference of two rows.",
           "The total is all the rows added, or all the icons × the scale."],
          items=[FIO("road.q1", "Two-wheelers on the Road: the most",
                     "Which day had the most two-wheelers passing her house? ___",
                     ["Icon box: 1 scooter icon stands for 3 two-wheelers. Count the icons: Monday 8, Wednesday 4, Friday 12.",
                      "Monday: 8 × 3 = 24 two-wheelers.",
                      "Wednesday: 4 × 3 = 12 two-wheelers.",
                      "Friday: 12 × 3 = 36 two-wheelers.",
                      "Compare: 36 is more than 24 and 12, so Friday has the most.",
                      "Check: Friday has the most icons too, 12 icons, and every icon stands for 3."],
                     "Friday, with 36 two-wheelers.",
                     kind="exercise",
                     q_figure=ROAD,
                     s_figure="The same pictograph with the numbers 24, 12 and 36 written at the end of the three rows "
                              "and the Friday row outlined in orange."),
                 FIO("road.q2", "Two-wheelers on the Road: the total",
                     "How many total two-wheelers did she record over three days? ___",
                     ["Read each row. One icon is 3 two-wheelers.",
                      "Monday: 8 × 3 = 24.",
                      "Wednesday: 4 × 3 = 12.",
                      "Friday: 12 × 3 = 36.",
                      "Add the three days: 24 + 12 + 36 = 72.",
                      "Check: count all the icons, 8 + 4 + 12 = 24 icons, and 24 × 3 = 72 two-wheelers."],
                     "72 two-wheelers.",
                     kind="exercise",
                     q_figure=ROAD,
                     s_figure="The same pictograph with the numbers 24, 12 and 36 written at the end of the three rows "
                              "and the total 72 written below."),
                 FIO("road.q3", "Two-wheelers on the Road: fewer on Wednesday",
                     "How many fewer two-wheelers were seen on Wednesday than on Monday? ___",
                     ["Monday: 8 × 3 = 24 two-wheelers.",
                      "Wednesday: 4 × 3 = 12 two-wheelers.",
                      "Fewer is the difference of the two rows: 24 − 12 = 12.",
                      "Check: the rows differ by 8 − 4 = 4 icons, and 4 × 3 = 12."],
                     "12 fewer.",
                     kind="exercise",
                     q_figure=ROAD,
                     s_figure="The same pictograph with the Monday row and the Wednesday row outlined in orange and the "
                              "difference 12 written between them."),
                 FIO("road.q4", "Two-wheelers on the Road: more on Friday",
                     "How many more two-wheelers were seen on Friday than on Wednesday? ___",
                     ["Friday: 12 × 3 = 36 two-wheelers.",
                      "Wednesday: 4 × 3 = 12 two-wheelers.",
                      "More is the difference of the two rows: 36 − 12 = 24.",
                      "Check: the rows differ by 12 − 4 = 8 icons, and 8 × 3 = 24."],
                     "24 more.",
                     kind="exercise",
                     q_figure=ROAD,
                     s_figure="The same pictograph with the Friday row and the Wednesday row outlined in orange and the "
                              "difference 24 written between them."),
                 FIO("road.q5", "Two-wheelers on the Road: choose another scale",
                     "Choose any other scale and represent the same data using a pictograph in your notebook.",
                     ["The numbers to show are Monday 24, Wednesday 12 and Friday 36.",
                      "A scale fits when every number can be shared into groups of the scale with nothing left over.",
                      "Try a scale of 6: 24 ÷ 6 = 4, 12 ÷ 6 = 2 and 36 ÷ 6 = 6. Every number fits.",
                      "With 1 icon standing for 6 two-wheelers, Monday has 4 icons, Wednesday has 2 icons and Friday has 6 icons.",
                      "The scales 1, 2, 4 and 12 fit too. With a scale of 12, the rows have 2, 1 and 3 icons.",
                      "Draw the icons of each row and write the icon box: 1 icon stands for 6 two-wheelers.",
                      "Check: read back, 4 × 6 = 24, 2 × 6 = 12 and 6 × 6 = 36, the same numbers as before."],
                     "Sample answer: scale 6, with Monday 4 icons, Wednesday 2 icons and Friday 6 icons. Your answer "
                     "may differ.",
                     kind="prompt",
                     q_figure=ROAD,
                     s_figure="A pictograph titled Number of Two-wheelers with the icon box 1 scooter icon = 6 "
                              "two-wheelers, and three rows: Monday with 4 scooter icons, Wednesday with 2 scooter "
                              "icons and Friday with 6 scooter icons.")],
          misconceptions=["M_ICON_IS_ONE", "M_SCALE_NO_FIT"])],
    key_terms=["pictograph", "icon", "scale", "total"]))
