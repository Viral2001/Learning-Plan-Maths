# -*- coding: utf-8 -*-
"""Topics T9 to T11 (module M3: patterns in shapes, and the summary). Book sections 1.5 and 1.6."""
from topics_common import A, DOER, TOPIC, WE, BOOK_TEXT, book, fio, we

TOPICS = []

# ============================== T9 Patterns in shapes (1.5) ==================================================
TOPICS.append(TOPIC(
    "T9", "M3", "Shape Sequences", ["1.5"], "Apply",
    "Students describe how each shape in a shape sequence of Table 3 is formed from the one before, and draw "
    "the next shape.",
    "Shape sequences, studied in geometry, follow a rule just as number sequences do: add a side, add a point, add "
    "a row, or replace each segment.",
    [A("T9.C1", "Shapes that grow one step at a time", "Understand",
       "Students describe the rule for the regular polygon and complete graph sequences of Table 3 and name "
       "geometry as the study of patterns in shapes.",
       textbook=book("1.5", stop=3),
       teach=["Predict first: a triangle, a square, a pentagon, a hexagon. What would the next shape be, and "
              "what changed each time?",
              "Regular polygons: the next shape has one more side. Complete graphs: add a new point and join it to "
              "every point already there.",
              "The branch of mathematics that studies patterns in shapes is called geometry."],
       examples=[WE('The shapes triangle, square and pentagon are in a sequence. Draw the next two.',
                   ['The rule is one more side each time.', 'After the 5 sides of the pentagon comes a shape with 6 sides, a hexagon.', 'Then comes a shape with 7 sides, a heptagon.'],
                   'A hexagon, then a heptagon.')],
       key_terms=["shape sequence", "geometry", "regular polygon", "complete graph"],
       misconceptions=["M_SHAPE_ALWAYS_DRAWABLE", "M_SHAPES_NO_NUMBERS"], minutes=10),
     A("T9.C2", "Stacking squares and triangles, and the Koch snowflake", "Analyze",
       "Students describe the rule for the stacked squares, stacked triangles and Koch snowflake sequences, and "
       "say why the snowflake soon becomes hard to draw.",
       textbook=[],
       teach=["Predict first: a big square made of little squares, 1 by 1, then 2 by 2, then 3 by 3. What is the "
              "rule?",
              "Stacked squares add a row and a column. Stacked triangles add a new bottom row of little "
              "triangles.",
              "The Koch snowflake replaces each line segment by a speed bump, so the segments get tinier and "
              "tinier and the shapes become hard to draw."],
       examples=[WE('A stack of squares is 3 by 3 little squares. What is the next stack, and how many little squares does it have?',
                   ['Each stack adds a row and a column, so the next stack is 4 by 4.', '4 × 4 = 16.'],
                   'A 4 by 4 stack with 16 little squares.')],
       key_terms=["stacked squares", "stacked triangles", "Koch snowflake"],
       misconceptions=["M_SHAPE_ALWAYS_DRAWABLE", "M_KOCH_ADDS"], minutes=10),
     DOER("T9.C3", "Pull it together and do it: Next Shape Drawer", "shape_sequence_drawer", "Apply",
          "Students draw the next shape of each Table 3 sequence on the tool and state its rule in their own "
          "words.",
          ["Each shape sequence has a rule for getting from one shape to the next.",
           "Regular polygons add a side, complete graphs add a point, stacks add a row, the snowflake replaces "
           "segments.",
           "Some next shapes are very hard to draw by hand."],
          items=[fio("1.5.FiO.Q1"), fio("1.5.FiO.Q2")],
          misconceptions=["M_SHAPE_ALWAYS_DRAWABLE"])]))

# ============================== T10 Relation to number sequences (1.6) =======================================
TOPICS.append(TOPIC(
    "T10", "M3", "Shape Sequences Hide Number Sequences", ["1.6"], "Analyze",
    "Students count a part of each shape in a shape sequence, name the number sequence that results, and "
    "explain why.",
    "Counting sides, lines, little squares or segments in a shape sequence gives a number sequence from Table 1 or "
    "a related one.",
    [A("T10.C1", "Sides of regular polygons", "Understand",
       "Students link the shapes triangle, quadrilateral, pentagon and so on to the counting numbers starting at "
       "3, and say what regular means.",
       textbook=book("1.6", stop=3),
       teach=["Predict first: a triangle has 3 sides, a square 4. What number sequence do the sides of the next "
              "shapes follow?",
              "The sides of the regular polygons are 3, 4, 5, 6, 7, 8, 9, 10, the counting numbers starting at 3. "
              "That is why they are called triangle, quadrilateral, pentagon, hexagon, heptagon, octagon, "
              "nonagon and decagon.",
              "Regular means the sides have equal length and the corners look the same."],
       examples=[we("1.6.ex1")],
       key_terms=["regular polygon", "sides", "corners"], misconceptions=["M_SIDES_CORNERS"], minutes=10),
     A("T10.C2", "Counting a shape sequence gives a number sequence", "Analyze",
       "Students count the matchsticks in a row of triangles to get a number sequence, and see that other shape "
       "sequences have beautiful relationships with number sequences.",
       textbook=book("1.6", start=3, stop=4),
       teach=["Predict first: one matchstick triangle uses 3 sticks. A row of 2 triangles sharing a side uses "
              "5. How many sticks for a row of 3?",
              "The counts 3, 5, 7, 9 go up by 2 each time, the odd numbers after 1.",
              "So counting the sticks in a shape sequence gave a number sequence.",
              "The other sequences in Table 3 have such relationships too, and a relation helps us study both."],
       examples=[WE('How many matchsticks make a row of 5 triangles that share sides?',
                   ['One triangle uses 3 sticks, and each new triangle adds 2 sticks.', 'The counts are 3, 5, 7, 9, 11.', 'The fifth count is 9 + 2 = 11.'],
                   '11 matchsticks.')],
       key_terms=["shape sequence", "number sequence"],
       misconceptions=["M_SHAPES_NO_NUMBERS", "M_COMPLETE_SAME_ADD"], minutes=10),
     DOER("T10.C3", "Pull it together and do it: Shape Count Table", "shape_count_table", "Analyze",
          "Students count sides, lines, little squares, little triangles and segments on the tool and name the "
          "number sequence each count gives.",
          ["Count a part of each shape, and the counts form a number sequence.",
           "Complete graphs give triangular numbers, stacked shapes give squares, the snowflake gives 3 times "
           "powers of 4.",
           "A picture or a rule explains why."],
          items=[fio("1.6.FiO.Q1"), fio("1.6.FiO.Q2"), fio("1.6.FiO.Q3"), fio("1.6.FiO.Q4"), fio("1.6.FiO.Q5")],
          misconceptions=["M_SIDES_CORNERS", "M_COMPLETE_SAME_ADD", "M_STACK_ROWS_SAME", "M_KOCH_ADDS"])]))

# ============================== T11 Summary ==================================================================
TOPICS.append(TOPIC(
    "T11", "M3", "Summary: Patterns in Mathematics", ["Summary"], "Remember",
    None,
    "Patterns and their reasons, number sequences, pictures of sequences, relations among sequences and shape "
    "sequences.",
    [A("T11.C1", "What we found about patterns", "Remember",
       "Students restate that mathematics is the search for patterns and their reasons, name the main number "
       "sequences, and say how pictures explain relations among sequences and link shapes to numbers.",
       textbook=book("1.6", "Summary"),
       teach=["Our opening question is settled: the matchstick row grows by a rule, and a rule lets us say what "
              "comes next.",
              "Number sequences such as counting, odd, even, triangular, square, cube, Virahanka and powers of 2 "
              "follow rules, and pictures explain how they relate, as odd numbers adding up to squares.",
              "Shape sequences hide number sequences in their counts.",
              "Still open for you: find a pattern of your own and explain why it happens."],
       ncert=["summary"], key_terms=["pattern", "number sequence", "shape sequence"],
       video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
