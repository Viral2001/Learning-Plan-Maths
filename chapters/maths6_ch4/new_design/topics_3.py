# -*- coding: utf-8 -*-
"""Topics T9 to T11 (module M4: choosing and presenting well, summary). Book sections 4.4 (chapter box) and 4.5."""
from topics_common import A, DOER, TOPIC, BOOK_TEXT, book, fio, we

TOPICS = []
H44 = "Chapter box and Teacher's Note (end of 4.4)"

# ============================== T9 Choosing the right display (4.4) ==========================================
TOPICS.append(TOPIC(
    "T9", "M4", "Choosing the Right Display", ["4.4"], "Analyze",
    "Students decide whether a table, a pictograph or a bar graph suits a given set of data, and use all three "
    "to answer questions about wickets, vehicles, tractors, girls and dogs.",
    "A table keeps every number, a pictograph shows the data at a glance, and a bar graph compares frequencies "
    "fast; the scale is chosen from the smallest and the largest value.",
    [A("T9.C1", "Table, pictograph or bar graph: which one to use", "Analyze",
       "Students say what each of a table, a pictograph and a bar graph shows best, and choose the scale from "
       "the smallest and the largest frequency, starting from zero.",
       textbook=book("4.4", H44, stop=5),
       teach=["Predict first: the same data is given as a table, a pictograph and a bar graph. Which one shows "
              "the biggest category fastest?",
              "A pictograph shows the data with pictures, and a bar graph shows it with equally spaced bars of "
              "equal width, whose lengths give the frequencies.",
              "The bars help us read data much faster than a frequency table, since we compare frequencies "
              "at a glance.",
              "Choose the scale from the smallest and the largest frequency, so the graph fits the paper, and "
              "start the markings from zero."],
       video_focus=["CHOOSE"], key_terms=["scale", "bar graph", "pictograph"],
       misconceptions=["M_ALWAYS_GRAPH", "M_SCALE_UNEQUAL"], minutes=10),
     DOER("T9.C2", "Practice: Tables, pictographs and bar graphs together", None, "Analyze",
          "Students build frequency tables with tally marks, read and draw pictographs, and use totals, "
          "differences and halves to answer questions about the data.",
          ["Make a frequency table first: tally, then count.",
           "Read the key or the scale before reading any symbol or bar.",
           "A total is the sum of the frequencies, never of the values themselves."],
          items=[fio("4.4.FiO.Q3"), fio("4.4.FiO.Q4"), fio("4.4.FiO.Q5"), fio("4.4.FiO.Q6"),
                 fio("4.4.FiO.Q7", steps=[
              "Class 8 has the least, 6 girls",
              "Class 6 has 16 and Class 5 has 10, so the difference is 16 − 10 = 6",
              "Class 2 has 18 girls, and 18 + 2 = 20 is 5 full symbols",
              "Class 7 has 3 symbols of 4 girls each, so 3 × 4 = 12 girls"]), fio("4.4.FiO.Q8")],
          misconceptions=["M_COUNT_AS_VALUE", "M_KEY_IGNORED", "M_HALF_SYMBOL"])]))

# ============================== T10 Artistic and aesthetic considerations (4.5) ==============================
TOPICS.append(TOPIC(
    "T10", "M4", "Pretty Pictures and Honest Graphs", ["4.5"], "Evaluate",
    "Students compare a table with a bar graph, choose vertical or horizontal bars for heights and lengths, "
    "and check whether an infographic misleads about the facts.",
    "Heights are shown with vertical bars (columns) and lengths along the ground with horizontal bars; "
    "pictures added to a graph must not change what the bars say.",
    [A("T10.C1", "From a table of numbers to a column graph", "Apply",
       "Students see that a table of mountain heights makes it hard to compare quickly, draw it as bars, and "
       "choose vertical bars for heights measured upward.",
       textbook=book("4.5", None, start=1, stop=8),
       teach=["Predict first: Mount Everest is 8848 m and Mount Koscuiszko is 2228 m. How much taller is "
              "Everest, and can you see it quickly in a table?",
              "From the numbers, 8848 − 2228 = 6620 m, but in a long table this takes effort.",
              "Draw the table as a bar graph and the difference is seen at a glance. Heights go up from the "
              "ground, so vertical bars, called a column graph, suit them.",
              "Lengths along the ground, such as the length of a river, are best shown with horizontal bars."],
       examples=[we("4.5.q1"), we("4.5.q2")],
       key_terms=["column graph", "vertical", "horizontal"], misconceptions=["M_ALWAYS_GRAPH"], minutes=10),
     A("T10.C2", "Infographics: do taller mountains have to be wider?", "Evaluate",
       "Students say that an infographic adds pictures to a bar graph, and explain that triangles that grow "
       "wider with height tell something the data does not.",
       textbook=book("4.5", "Infographics", stop=5),
       teach=["Predict first: draw each mountain as a triangle, taller for Everest. Does the data say that "
              "taller mountains are wider?",
              "A graph with bars of the same width compares only the heights. In the triangle picture, the "
              "taller triangles are also wider.",
              "Width has nothing to do with height here, so the picture implies something the data never said.",
              "More lifelike mountains look better, but the picture may not be accurate."],
       examples=[we("4.5.q3"), we("4.5.q4")],
       key_terms=["infographic"], misconceptions=["M_TALLER_WIDER", "M_PICTURE_PROPORTION"], minutes=10),
     A("T10.C3", "Checking a picture against the numbers: Everest and Elbrus", "Evaluate",
       "Students check the claim that Everest looks twice as tall as Elbrus by doubling 5642 and comparing "
       "with 8848.",
       textbook=book("4.5", "Infographics", start=5, stop=8),
       teach=["Predict first: in the mountain-range picture Everest looks twice as tall as Elbrus. Is it?",
              "Elbrus is 5642 m, so twice Elbrus is 5642 × 2 = 11284 m.",
              "Everest is only 8848 m, which is less than 11284 m, so Everest is not twice as tall as Elbrus.",
              "Check the numbers before trusting how a picture looks, when you make an infographic and when "
              "you read one."],
       examples=[we("4.5.q5")],
       key_terms=["infographic"], misconceptions=["M_PICTURE_PROPORTION"], minutes=8),
     DOER("T10.C4", "Pull it together and do it: Honest Graph Checker", "honest_graph_checker", "Evaluate",
          "Students compare a bar graph with its decorated version on the tool, check each picture against "
          "the table, and choose vertical or horizontal bars for given data.",
          ["Heights go upward, so use vertical bars; lengths along the ground use horizontal bars.",
           "Bars of equal width compare only the heights.",
           "Check how a picture looks against the numbers in the table."],
          items=[fio("4.5.FiO.Q1"), fio("4.5.FiO.Q2")],
          misconceptions=["M_TALLER_WIDER", "M_PICTURE_PROPORTION", "M_ALWAYS_GRAPH"])]))

# ============================== T11 Summary ==================================================================
TOPICS.append(TOPIC(
    "T11", "M4", "Summary: Data Handling and Presentation", ["Summary"], "Remember",
    None,
    "Data, tally marks and frequencies, pictographs with a key, bar graphs with a scale, and care with "
    "pictures that decorate a graph.",
    [A("T11.C1", "What we found about data", "Remember",
       "Students restate what data and frequency mean, how tally marks organise data, how a key and a scale "
       "turn symbols and bars into numbers, and why pictures can mislead.",
       textbook=book("4.5", "Summary"),
       teach=["Our opening question is settled: ask everyone, count with tally marks, and the highest "
              "frequency tells the most popular game, hockey with 8.",
              "A pictograph and a bar graph show the same frequencies; read the key or the scale first.",
              "Choose a scale from the smallest and the largest value, and start from zero.",
              "Still open for you: collect data in your own class and show it in the way that suits it best."],
       ncert=["summary"], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
