# -*- coding: utf-8 -*-
"""Topics T7 and T8 (module M3: Reading a Picture and Revision). True or False: reading a picture of 17 school children
by counting (eight statements, one question each), and the chapter revision as a text summary with short checks.
Every teaching concept has one worked example with the plan's own numbers (practice values); every book question is an
FIO item of its topic's DOER, in the book's order, with the verified answers of DESIGN section 4."""
from topics_common import A, DOER, FIO, TOPIC, WE
from figs import PIC

TOPICS = []

_OPEN = "Observe the picture carefully. Based on your observation, is this statement true or false? "


def _ring(what):
    return ("The same picture of the school children with %s ringed in orange and the answer written under the "
            "picture." % what)


# ============================== T7 True or False: Reading a Picture =======================================
TOPICS.append(TOPIC(
    "T7", "M3", "True or False: Reading a Picture", ["True or False"], "Analyze",
    "Students judge statements about a picture as true or false by counting the people each statement talks about "
    "and comparing the counts, including more than half, some, all and no child.",
    "To check a statement about a picture, do not trust a quick look. Count the children the statement talks about, "
    "then compare the counts: with each other, or with half of all the children.",
    [A("T7.C1", "Counting and Comparing in a Picture", "Analyze",
       "Students count the children a statement talks about, compare the counts and say whether the statement is true "
       "or false.",
       textbook=["Observe the above picture carefully. Based on your observation, find out which of the following "
                 "statements are true or false."],
       teach=["Predict first: a picture shows 9 children, some wear hats and some hold flags. How can we tell if the "
              "statement More than half of the children wear hats is true? Is a quick look enough?",
              "A quick look can fool us. Count the children the statement talks about.",
              "To compare two groups, compare their counts. The group with the bigger count has more children.",
              "More than half means more than half of all the children. Half of 9 is 4 1/2, so a group of 5 or more is "
              "more than half and a group of 4 is not.",
              "Some means at least one child. All means every child, so one child who does not is enough to make it "
              "false. No child means none, so one child who does is enough to make it false.",
              "Rule: count the children a statement talks about, then compare the counts."],
       examples=[WE("A picture shows 9 children (practice values). 4 of them wear hats, 5 hold flags, and 2 of the "
                    "children wear a hat and also hold a flag. True or false? (a): More than half of the children wear "
                    "hats. (b): Some children wear a hat and hold a flag. (c): More children hold flags than wear "
                    "hats.",
                    ["(a): The picture has 9 children. Half of 9 is 4 1/2, because 9 ÷ 2 is 4 with 1 left over.",
                     "(a): 4 children wear hats. 4 is less than 4 1/2, so it is not more than half. The statement is "
                     "false.",
                     "(b): 2 children wear a hat and hold a flag. Some means at least one, and 2 is more than 0. The "
                     "statement is true.",
                     "(c): 5 children hold flags and 4 wear hats. 5 > 4, so more children hold flags. The statement "
                     "is true.",
                     "Check: 5 − 4 = 1, so exactly 1 more child holds a flag than wears a hat."],
                    "(a): False; (b): True; (c): True")],
       ncert=["pic.setup"], key_terms=["count", "compare", "more than half", "true or false"],
       misconceptions=["M_ONE_LOOK", "M_HALF_ODD"], minutes=6),
     DOER("T7.C2", "Practice: Picture Detective", "picture_detective", "Analyze",
          "Students count the children with a cap, glasses, a book or a backpack in a picture and judge each "
          "statement about the picture as true or false.",
          ["Do not judge by a quick look. Count the children the statement talks about.",
           "To compare two groups, compare their counts. For more than half, compare with half of all the children.",
           "Some means at least one child. For no child, one child who does is enough to make the statement false.",
           "Check the count again before you answer true or false."],
          items=[
              FIO("tf.s1", "True or False: all girls wear glasses",
                  _OPEN + "All girls are wearing glasses.",
                  ["Count the girls in the picture: 8 girls.",
                   "Count the girls who wear glasses: 3 girls.",
                   "For all the girls, every one of the 8 girls must wear glasses.",
                   "3 is less than 8, so some girls do not wear glasses. For example, the girl in the front row with "
                   "a cap and no glasses.",
                   "Check: 8 − 3 = 5 girls do not wear glasses."],
                  "False. Only 3 of the 8 girls wear glasses.",
                  kind="prompt", q_figure=PIC,
                  s_figure=_ring("the 3 girls who wear glasses")),
              FIO("tf.s2", "True or False: 10 children wear caps",
                  _OPEN + "10 children are wearing caps on their heads.",
                  ["Count the red caps in the back row: 5 children.",
                   "Count the red caps in the front row: 5 children.",
                   "Add the two rows: 5 + 5 = 10 children wear caps.",
                   "The statement says 10 children, and 10 is exactly the number we counted.",
                   "Check: 17 children in all, so 17 − 10 = 7 children wear no cap."],
                  "True. 10 children wear caps.",
                  kind="prompt", q_figure=PIC,
                  s_figure=_ring("the 10 children who wear caps")),
              FIO("tf.s3", "True or False: boys and girls holding books",
                  _OPEN + "More boys are holding books than girls.",
                  ["Count the boys who hold a book: 6 in the back row and 1 in the front row, 6 + 1 = 7 boys.",
                   "Count the girls who hold a book: 3 in the back row and 4 in the front row, 3 + 4 = 7 girls.",
                   "More boys than girls would need the boys' count to be bigger than the girls' count.",
                   "7 is not more than 7. The counts are the same.",
                   "Check: 7 + 7 = 14 children hold books in all."],
                  "False. 7 boys and 7 girls hold books, the same number.",
                  kind="prompt", q_figure=PIC,
                  s_figure=_ring("the 7 boys and the 7 girls who hold books")),
              FIO("tf.s4", "True or False: more than half wear glasses",
                  _OPEN + "More than half of the children are wearing glasses.",
                  ["Count all the children: 17.",
                   "Half of 17 is 8 1/2, because 17 ÷ 2 is 8 with 1 left over.",
                   "Count the children who wear glasses: 3 girls and 4 boys, 3 + 4 = 7 children.",
                   "More than half would be 9 children or more. 7 is less than 8 1/2.",
                   "Check: 7 + 7 = 14, and 14 is less than 17, so 7 children cannot be half of the 17."],
                  "False. 7 children wear glasses and half of 17 is 8 1/2.",
                  kind="prompt", q_figure=PIC,
                  s_figure=_ring("the 7 children who wear glasses")),
              FIO("tf.s5", "True or False: books and caps",
                  _OPEN + "The number of children holding books is greater than the number of children wearing caps.",
                  ["Count the children who hold a book: 9 in the back row and 5 in the front row, 9 + 5 = 14.",
                   "Count the children who wear caps: 10.",
                   "Compare the two counts: 14 is greater than 10.",
                   "So more children hold books than wear caps, and the statement is true.",
                   "Check: 14 − 10 = 4 more children hold books than wear caps."],
                  "True. 14 children hold books and 10 wear caps.",
                  kind="prompt", q_figure=PIC,
                  s_figure=_ring("the 14 children who hold books")),
              FIO("tf.s6", "True or False: boys and girls wearing glasses",
                  _OPEN + "The number of boys wearing glasses is greater than the number of girls wearing glasses.",
                  ["Count the boys who wear glasses: 3 in the back row and 1 in the front row, 3 + 1 = 4 boys.",
                   "Count the girls who wear glasses: 1 in the back row and 2 in the front row, 1 + 2 = 3 girls.",
                   "Compare the two counts: 4 is greater than 3.",
                   "So more boys than girls wear glasses, and the statement is true.",
                   "Check: 4 + 3 = 7 children wear glasses in all."],
                  "True. 4 boys and 3 girls wear glasses.",
                  kind="prompt", q_figure=PIC,
                  s_figure=_ring("the 4 boys and the 3 girls who wear glasses")),
              FIO("tf.s7", "True or False: glasses and caps together",
                  _OPEN + "Some children are wearing both glasses and caps.",
                  ["Look for a child who wears glasses and a cap together.",
                   "The boy in the front row with a red cap, glasses and a backpack wears both.",
                   "Some means at least one child, and we have found one.",
                   "Counting every child with both gives 6 children, and 6 is more than 0.",
                   "Check: the statement is true because at least one child wears both."],
                  "True. 6 children wear both glasses and caps.",
                  kind="prompt", q_figure=PIC,
                  s_figure=_ring("the 6 children who wear both glasses and a cap")),
              FIO("tf.s8", "True or False: a cap, a book and a backpack",
                  _OPEN + "There is no child who has all three items, a cap, a book and a backpack.",
                  ["Look for a child who has a cap, a book and a backpack together.",
                   "The girl in the back row on the left wears a red cap, holds a book and wears a backpack.",
                   "The statement says that nobody has all three, but we found one child who does.",
                   "Check the others with backpacks: the girl and the boy in the front row with caps and backpacks hold "
                   "no book, and the last boy has no cap and no book. Only the girl in the back row has all three.",
                   "Check: 1 child has all three items, so the statement is false."],
                  "False. One child, the girl in the back row on the left, has all three.",
                  kind="prompt", q_figure=PIC,
                  s_figure=_ring("the girl in the back row on the left who has a cap, a book and a backpack"))],
          misconceptions=["M_ONE_LOOK", "M_HALF_ODD"])],
    key_terms=["count", "compare", "true or false"]))

# ============================== T8 Chapter Revision (summary) =============================================
TOPICS.append(TOPIC(
    "T8", "M3", "Chapter Revision: Data Through Pictures", ["Chapter summary"], "Understand",
    "",
    "The chapter's ideas in one walk through the class newsroom: a table, a pictograph and its scale, comparing rows, "
    "squares to bars, reading and making a bar graph, a bar graph of lengths, totals and predictions, and reading a "
    "picture.",
    [A("T8.C1", "Chapter Revision: Data Through Pictures", "Understand",
       "",
       teach=["Predict first: you have been a reporter in the class newsroom. Can you say one idea from each stop, from "
              "the notebook of answers to the picture of children? Read the lines below and tick each idea you "
              "remembered.",
              "A table: record the answers in a table with one row for each kind of answer. Count each row and check "
              "that the counts add up to the number of friends asked, such as 6 + 4 + 2 = 12.",
              "Check: with the rows 1 hour 6, 2 hours 4 and 3 hours 2, how many are more than 1 hour? 4 + 2 = 6. The "
              "row 1 hour is not in it.",
              "A pictograph shows a number with icons, and a scale says how many items one icon stands for. With one "
              "icon = 5, 7 icons show 35 items, because 7 × 5 = 35.",
              "Choosing a scale: choose a scale that every number can be shared into with nothing left over. For 12, "
              "18 and 30, a scale of 6 gives 2, 3 and 5 icons. A bigger scale needs fewer icons.",
              "Check: does a scale of 4 fit 18? No, because 18 ÷ 4 is 4 with 2 left over.",
              "Comparing rows of a pictograph: read each row as icons × scale, then find the most, the total and how "
              "many more. With one icon = 10, 7 icons are 70 and 2 icons are 20, so 70 − 20 = 50 more.",
              "Squares to bars: a row of squares can stand up into a bar. The height of the bar is the number of "
              "squares. A bar graph has the vertical line for the numbers, the horizontal base for the activities and "
              "a bar for each.",
              "Reading bars: read the height where the top of the bar meets the vertical line. A taller bar is more, "
              "and the difference of two heights tells how many more: bars 5 and 3 differ by 5 − 3 = 2.",
              "Making a bar graph: write the names on the horizontal base, make the vertical line reach the biggest "
              "number, and draw each bar up to its number. A whole day of 8 + 6 + 3 + 4 + 3 = 24 hours.",
              "Lengths: a bar can be a length in cm. Strips of 9 cm and 4 cm: the longer one is 9 − 4 = 5 cm longer.",
              "Totals and predictions: add the bars for the total and use a rule on the total. 3 + 6 + 4 + 5 + 2 = 20 "
              "kg, and at 2 bags for each kg that is 20 × 2 = 40 bags. A prediction is a careful guess from the graph "
              "and can be wrong.",
              "A picture: to check a statement, count the children it talks about. Half of 11 is 5 1/2, so 5 children "
              "are not more than half of 11 children.",
              "Check: if 7 of 9 children hold flags and 4 of 9 wear hats, do more children hold flags? Yes, because "
              "7 > 4."],
       ncert=["summary"], key_terms=["table", "pictograph", "scale", "bar graph"], minutes=6,
       enrichment=True)],
    topic_type="summary"))
