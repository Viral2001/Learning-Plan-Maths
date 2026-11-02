# -*- coding: utf-8 -*-
"""Chapter-level content for Class 6 Chapter 4, Data Handling and Presentation (Ganita Prakash Grade 6, Chapter 4).
Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212."""
from __future__ import annotations

CHAPTER = {
    "grade": 6,
    "label": "Class 6",
    "chapter_no": 4,
    "name": "Data Handling and Presentation",
    "book_part": "Ganita Prakash Grade 6, Chapter 4",
    "source_pdf": "textbooks/class6/fegp104.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Collecting and Organising Data",
     "Data starts as a list of answers. Counting with tally marks gives a frequency table, and putting the data "
     "in order makes the largest, the smallest and the commonest value easy to see."),
    ("M2", "Pictographs",
     "A pictograph shows a frequency with pictures. A key says what one symbol stands for, and a bigger key or a "
     "half symbol keeps big numbers short."),
    ("M3", "Bar Graphs",
     "A bar graph shows each frequency as the length of a bar of equal width. Reading a bar graph needs the "
     "scale, and drawing one means choosing a scale that fits the data."),
    ("M4", "Choosing and Presenting Well",
     "A table, a pictograph or a bar graph suits different data. Vertical or horizontal bars and pictures that "
     "decorate a graph can help the reader, or mislead the reader."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's order. A question about the class gives a list, counting turns the "
             "list into a table, and the table is then shown as a pictograph and as a bar graph, with the "
             "scale as the idea that ties the pictures to the numbers.",
    "points": [
        {"title": "Ask a question, then collect",
         "text": "Every graph starts from a question such as which game is most popular, so the data is "
                 "collected, counted and ordered before it is drawn."},
        {"title": "Concept, then practice, topic by topic",
         "text": "Each idea gets its own topic: worked videos for the book's examples, a tool only where "
                 "handling the data is the idea, then the book's Figure it Out questions in a practice topic, "
                 "each with its own video."},
        {"title": "The scale tells the story",
         "text": "A symbol or a unit of bar length always stands for a number. Reading and drawing both start "
                 "by finding that number."},
        {"title": "Keeko's doubts",
         "text": "The common wrong ideas, such as 'the longest list entry is the most popular' or 'a bar of 6 "
                 "units is always 6', are raised by Keeko and fixed with a count or a scale, never just a rule."},
    ],
}

# Every book item, in book order. Ids come from the page-image inventory (book_items.json).
NCERT_ITEMS = [
    "opening",
    "4.1.q1", "4.1.q2", "4.1.FiO1.Q1", "4.1.FiO1.Q2", "4.1.FiO1.Q3", "4.1.FiO1.Q4", "4.1.FiO2.Q1",
    "4.1.FiO2.Q2", "4.1.FiO3.Q1", "4.1.FiO3.Q2", "4.1.FiO3.Q3", "4.1.FiO3.Q4", "4.1.FiO3.Q5",
    "4.2.q1", "4.2.q2", "4.2.ex1", "4.2.q3", "4.2.q4", "4.2.FiO.Q1", "4.2.FiO.Q2",
    "4.3.q1", "4.3.q2", "4.3.q3", "4.3.FiO.Q1", "4.3.FiO.Q2", "4.3.FiO.Q3", "4.3.FiO.Q4", "4.3.ex1",
    "4.4.ex1", "4.4.ex2", "4.4.q1", "4.4.q2", "4.4.q3", "4.4.FiO.Q1", "4.4.FiO.Q2", "4.4.FiO.Q3",
    "4.4.FiO.Q4", "4.4.FiO.Q5", "4.4.FiO.Q6", "4.4.FiO.Q7", "4.4.FiO.Q8", "4.4.FiO.Q9", "4.4.FiO.Q10",
    "4.4.FiO.Q11",
    "4.5.q1", "4.5.q2", "4.5.FiO.Q1", "4.5.FiO.Q2", "4.5.q3", "4.5.q4", "4.5.q5",
    "summary",
]

MISCONCEPTIONS = [
    ("M_LIST_ENOUGH", "A list of answers already shows the most popular choice, so counting is not needed."),
    ("M_TALLY_SINGLES", "Tally marks are single strokes counted one by one, and the fifth stroke goes beside "
                        "the other four rather than across them."),
    ("M_COUNT_AS_VALUE", "The numbers in a frequency table can be added as the values themselves, so the total "
                         "wickets are 0 + 1 + 2 + 3 and so on."),
    ("M_ONE_SYMBOL_ONE", "Every symbol in a pictograph stands for exactly one thing, whatever the key says."),
    ("M_HALF_SYMBOL", "A half symbol means half a thing, not half of what the key says one symbol stands for."),
    ("M_KEY_IGNORED", "Count the symbols and ignore the key, so 5 triangles are 5 children."),
    ("M_BAR_HEIGHT_IS_VALUE", "The height of a bar in units is always the value itself, even when one unit "
                              "stands for 4 or 10."),
    ("M_SCALE_UNEQUAL", "The scale can jump by different amounts, or the axis can start anywhere, and the bars "
                        "still compare fairly."),
    ("M_BAR_WIDTH", "A wider bar means a bigger value, even when the heights match."),
    ("M_TALLER_WIDER", "A taller mountain must also be wider, so a picture that makes it wider is true to the "
                       "data."),
    ("M_PICTURE_PROPORTION", "If the picture of Everest looks twice as tall as Elbrus, then Everest is twice "
                             "as tall as Elbrus."),
    ("M_ALWAYS_GRAPH", "A graph is always better than a table, and the same graph suits all data."),
]

# Book choices recorded where the printed book disagrees with itself or with its own solutions.
# The plan always uses the solution-consistent, mathematically correct number.
SOLUTION_NOTES = [
    "4.4.FiO.Q2: the printed bars show Indore at about 4.5 units and Seoni at about 4; the solution gives the "
    "scale 1 unit = 4 tickets, so Indore (28 tickets) needs 7 units and is incorrect, and Seoni (16 tickets) "
    "is 4 units and correct. The plan uses these exact numbers, not the readings from the picture.",
    "4.4.FiO.Q10: the Monday bar looks slightly above 50 in the printed graph; the solution total 310 needs "
    "Monday = 50 (50 + 40 + 30 + 40 + 50 + 60 + 40 = 310), so the plan uses 50.",
    "4.4.FiO.Q11: the solution only names the wrong bars (2006, 2010, 2014 and 2018; 2022 is correct). The "
    "plan does not quote the wrong bar lengths read from the picture; each bar is checked against the table.",
    "4.5.q2: Kilimanjaro is printed as 5892 m in one picture label and 5895 m in the table and the triangle "
    "infographic; the plan uses 5895 m, so Denali (6194 m) is 299 m taller.",
    "4.1.FiO1.Q2, 4.3.ex1, 4.4.ex1: the book prints the list or graph but not the counts or unit heights; "
    "they are computed from the data (Hockey 8, Kabaddi 6, Cricket 6, Satoliya 5, Football 4, Badminton 2, "
    "total 31).",
    "4.1.FiO1.Q3, 4.1.FiO3.Q4, 4.1.FiO3.Q5, 4.4.FiO.Q4: open activities on the child's own data; the plan "
    "teaches the method, not a fixed answer.",
]
ERRATA = [
    "4.5 mountain table: Kilimanjaro 5892 m in one label against 5895 m in the table; 5895 m used.",
]

DESIGN_REFERENCES = [
    {"text": "maths6_ch7 and maths6_ch9 new_design Phase 2 plans: framing intro with one hook, idea topics "
             "ending in one doer (a tool only where handling the data is the idea), a practice topic after "
             "each idea topic with one video per book question, one summary topic.",
     "url": ""},
]

FIGURES = {
    "T2.C1": ["A class list of 31 names, each with a favourite game written beside it."],
    "T5.C1": ["A pictograph titled Modes of Travelling: one smiley is one student, with rows for car, bus, "
              "school bus, cycle and walking."],
    "T7.C1": ["A bar graph of students absent in each class, bars for Class 1 to Class 8 on equally spaced "
              "lines."],
    "T8.C3": ["A bar graph of Imran's family spending with bars of equal width and a scale of 200 rupees a "
              "unit."],
}
