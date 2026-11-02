# -*- coding: utf-8 -*-
"""Topics T7 to T11 (module M2: constructing squares and rectangles, an exploration in rectangles).
Book sections 8.3 and 8.4."""
from topics_common import A, DOER, TOPIC, book, fio, we

TOPICS = []

# ============================== T7 Constructing a square (8.3) ===============================================
TOPICS.append(TOPIC(
    "T7", "M2", "Constructing a Square", ["8.3"], "Apply",
    "Students construct a square of a given side with a ruler and a protractor or compass by drawing perpendiculars "
    "at the ends of one side, and explain why the other sides and angles follow.",
    "Draw one side, raise perpendiculars at both ends, and cut them at the side length: the fourth side and all "
    "four angles then come out right.",
    [A("T7.C1", "Constructing a square of side 6 cm", "Apply",
       "Students construct a square PQRS of side 6 cm by drawing PQ, two perpendiculars and two equal lengths, and "
       "check its sides and angles.",
       textbook=book("8.3", start=0, stop=5),
       teach=["Predict first: you have drawn PQ = 6 cm. How many more lines and points do you need to finish the "
              "square?",
              "At P draw a perpendicular to PQ with a protractor or set square, and mark S on it with PS = 6 cm.",
              "At Q draw another perpendicular and mark R with QR = 6 cm. With a compass, keep the opening at 6 cm "
              "and put the tip at P and then at Q.",
              "Join R and S, then check RS and the angles with a ruler and a protractor."],
       examples=[we("8.3.ex1")],
       key_terms=["perpendicular", "construct"], misconceptions=["M_RULER_END"], minutes=10),
     A("T7.C2", "Why the other sides and angles come out right", "Understand",
       "Students use the square's properties to explain why PS must be 6 cm and why RS, the angle at R and the "
       "angle at S are fixed once PQ and two perpendiculars are drawn.",
       textbook=book("8.3", start=5, stop=9),
       teach=["Predict first: you only measured PQ, QR and PS. Will RS also be 6 cm, and what will the angles at R "
              "and S be?",
              "A square has all sides equal, S1, so PS has to be as long as PQ, which is 6 cm.",
              "For the same reason RS is 6 cm, and the angles at R and S are 90° because a square has all angles "
              "90°, S2.",
              "Keeko thinks you must measure every side. You only construct what is needed, and the properties "
              "give the rest."],
       examples=[we("8.3.q1"), we("8.3.q2")],
       key_terms=["square", "property"], misconceptions=["M_EQUAL_SIDES_SQUARE"], minutes=8),
     DOER("T7.C3", "Pull it together and do it: Construction Stepper", "construction_stepper", "Apply",
          "Students carry out each step of a square or rectangle construction on the stepper tool, choosing the "
          "ruler, protractor or compass action, and check the finished figure.",
          ["Draw the first side, then perpendiculars at both ends.",
           "Mark the other corners at the right length with the ruler, or with the compass.",
           "Join the last two corners and check sides and angles."],
          textbook=book("8.3", start=9, stop=10),
          items=[],
          misconceptions=["M_RULER_END", "M_EQUAL_SIDES_SQUARE"])]))

# ============================== T8 Constructing a rectangle (8.3) ============================================
TOPICS.append(TOPIC(
    "T8", "M2", "Constructing a Rectangle", ["8.3"], "Apply",
    "Students construct a rectangle from two side lengths, and explain why a four-sided figure with four right "
    "angles must have equal opposite sides.",
    "A rectangle needs one length and one breadth; two perpendiculars at the ends of one side stay the same "
    "distance apart, so opposite sides are equal.",
    [A("T8.C1", "Four right angles force equal opposite sides", "Analyze",
       "Students explain why a four-sided figure with all angles 90° cannot have unequal opposite sides, by "
       "using the equal distance between two perpendiculars.",
       textbook=book("8.3", start=12, stop=13),
       teach=["Predict first: can you draw a four-sided figure with all four angles 90° but opposite sides "
              "unequal?",
              "Draw one side. The perpendiculars at its two ends never come closer or move apart, so they stay the "
              "same distance apart.",
              "That makes the opposite side as long as the first side. So the opposite sides are always equal.",
              "A four-sided figure with all angles 90° is therefore a rectangle."],
       examples=[we("8.3.q3")],
       key_terms=["rectangle", "perpendicular"], misconceptions=["M_EQUAL_SIDES_SQUARE"], minutes=8),
     DOER("T8.C2", "Practice: rectangles with a given length and breadth", None, "Apply",
          "Students construct rectangles of 4 cm by 6 cm and 2 cm by 10 cm with a ruler and a set square or "
          "compass, and check both rectangle properties.",
          ["Draw one side, then perpendiculars at both ends.",
           "Mark the breadth on each perpendicular, then join the last two corners.",
           "Check R1 and R2: opposite sides equal and all angles 90°."],
          textbook=book("8.3", start=10, stop=12),
          items=[fio("8.3.ex2"), fio("8.3.ex3")],
          misconceptions=["M_EQUAL_SIDES_SQUARE", "M_RULER_END"])]))

# ============================== T9 Nearest and farthest points on opposite sides (8.4) ========================
TOPICS.append(TOPIC(
    "T9", "M2", "How Far Apart Can Two Points Be?", ["8.4"], "Analyze",
    "Students move a point X along one side of a rectangle and a point Y along the opposite side, record the "
    "length XY in a table, and find the nearest and farthest positions.",
    "Between two opposite sides of a rectangle the shortest XY equals the side length, when X and Y are level; "
    "the longest XY is a diagonal.",
    [A("T9.C1", "Setting up the rectangle and guessing", "Apply",
       "Students construct a rectangle with AB = 7 cm and BC = 4 cm, place X on AD and Y on BC, and predict where "
       "X and Y are closest and where they are farthest.",
       textbook=book("8.4", start=0, stop=6),
       teach=["Predict first: X slides on side AD and Y slides on side BC. Where will they be closest, and where "
              "farthest?",
              "Construct the rectangle first: AB = 7 cm, BC = 4 cm, with right angles at every corner.",
              "Try some positions. When X and Y are at the same height, the line XY goes straight across and is as "
              "long as AB.",
              "The minimum XY is 7 cm, the same as AB."],
       examples=[we("8.4.ex1"), we("8.4.q1"), we("8.4.q2")],
       key_terms=["distance", "rectangle"], misconceptions=["M_SLANT_SHORTER"], minutes=10),
     A("T9.C2", "Measuring XY and keeping a table", "Apply",
       "Students measure XY for chosen positions of X and Y and record each case as a row of a table with the "
       "distance of X from A, the distance of Y from B and the length XY.",
       textbook=book("8.4", start=6, stop=13),
       teach=["Predict first: X is 5 mm below A and Y is 3 cm below B. Will XY be shorter than, equal to, or longer "
              "than 7 cm?",
              "A slanting line across the rectangle is a little longer than the straight one. Measure it with a "
              "ruler.",
              "A table keeps track: one row for each case, with the distance of X from A, the distance of Y from "
              "B, and the length XY.",
              "The three cases give about 7.4 cm, 7 cm and 7.3 cm."],
       examples=[we("8.4.q3"), we("8.4.q4")],
       key_terms=["table", "distance"], misconceptions=["M_SLANT_SHORTER", "M_RULER_END"], minutes=10),
     A("T9.C3", "Level positions, and the farthest position", "Analyze",
       "Students show that equal distances of X from A and of Y from B give XY equal to AB and ABYX a rectangle, "
       "and that the farthest XY is a diagonal of the rectangle.",
       textbook=book("8.4", start=13, stop=16),
       teach=["Predict first: if X and Y are the same distance from A and B, what shape is ABYX?",
              "X and Y are at the same height, so XY runs straight across. All four angles of ABYX are 90° and "
              "opposite sides are equal, so ABYX is a rectangle and XY equals AB.",
              "The farthest apart are opposite corners: X at A and Y at C, or X at D and Y at B.",
              "Then XY is a diagonal, AC or BD, about 8.1 cm for this rectangle."],
       examples=[we("8.4.q5"), we("8.4.q6"), we("8.4.q7")],
       key_terms=["diagonal", "rectangle"], misconceptions=["M_SLANT_SHORTER"], minutes=10),
     DOER("T9.C4", "Pull it together and do it: Rectangle Distance Explorer", "xy_explorer", "Analyze",
          "Students drag X and Y along two opposite sides of a rectangle on the tool, read the length XY, and "
          "find the nearest and the farthest positions for different rectangles.",
          ["Level positions give the shortest XY, equal to the side length.",
           "Moving X and Y apart in height makes XY longer.",
           "The longest XY is a diagonal of the rectangle."],
          items=[],
          misconceptions=["M_SLANT_SHORTER"])]))

# ============================== T10 Breaking rectangles into squares (8.4) ===================================
TOPICS.append(TOPIC(
    "T10", "M2", "Breaking Rectangles into Squares", ["8.4"], "Apply",
    "Students plan a construction with a rough diagram, build a rectangle that splits into two or into three "
    "identical squares, and say when a rectangle cannot be split like that.",
    "A rectangle splits into identical squares only when its length is a whole number of times its breadth; a rough "
    "diagram helps plan the steps.",
    [A("T10.C1", "A rectangle of two identical squares", "Apply",
       "Students draw a rough diagram of a rectangle ACDF made of squares ABEF and BCDE, name the equal sides, and "
       "construct it for AF = 4 cm.",
       textbook=book("8.4", "Breaking Rectangles", start=2, stop=10),
       teach=["Predict first: if the shorter side AF is 4 cm, how long must AC be so the rectangle holds two "
              "identical squares?",
              "Plan with a rough diagram. The two squares are identical, so AB = BC and AF = AB, and tick marks "
              "show equal sides.",
              "AC is two squares side by side: 4 cm and 4 cm give 8 cm.",
              "Draw AF, a perpendicular at A, and cut it with the compass at 4 cm twice."],
       examples=[we("8.4.ex3")],
       key_terms=["rough diagram", "identical"], misconceptions=["M_SPLIT_ANY"], minutes=10),
     A("T10.C2", "A rectangle of three identical squares", "Apply",
       "Students construct a rectangle that divides into three identical squares by repeating one compass length "
       "along a line, and give its sides.",
       textbook=book("8.4", "Breaking Rectangles", start=0, stop=2) + book("8.4", "Breaking Rectangles", start=10, stop=12),
       teach=["Predict first: if the square has side 3 cm, how long is a rectangle of three squares in a row?",
              "Choose the square side, 3 cm, and draw a rough diagram of three squares side by side.",
              "Draw one square, then use the compass to transfer 3 cm along the line two more times.",
              "The rectangle is 9 cm by 3 cm, so its length is 3 times its breadth."],
       examples=[we("8.4.ex2")],
       key_terms=["identical", "compass"], misconceptions=["M_SPLIT_ANY"], minutes=10),
     A("T10.C3", "Rectangles that cannot be split", "Analyze",
       "Students give sides of a rectangle that cannot be split into two identical squares and of one that cannot "
       "be split into three, using the length-to-breadth test.",
       textbook=book("8.4", "Breaking Rectangles", start=12, stop=13),
       teach=["Predict first: can a rectangle 4 cm by 2.5 cm be cut into two identical squares?",
              "Two identical squares need the length to be 2 times the breadth. Here 2 times 2.5 cm is 5 cm, not "
              "4 cm.",
              "Three identical squares need the length to be 3 times the breadth. A rectangle 7 cm by 2 cm fails, "
              "because 3 times 2 cm is 6 cm.",
              "Many answers are possible, so test any pair with the length-to-breadth rule."],
       examples=[we("8.4.q8")],
       key_terms=["identical", "breadth"], misconceptions=["M_SPLIT_ANY"], minutes=8),
     DOER("T10.C4", "Practice: a square inside a rectangle", None, "Apply",
          "Students construct an 8 cm by 4 cm rectangle with a square drawn inside it that shares its centre, using "
          "a rough diagram to find the side and the gaps.",
          ["Make a rough diagram first and write what each length must be.",
           "The square touches the top and the bottom, so its side equals the breadth.",
           "The leftover length is shared equally on both sides."],
          items=[fio("8.4.ex4")],
          misconceptions=["M_SPLIT_ANY"])]))

# ============================== T11 Squares with holes and curves (8.4) ======================================
TOPICS.append(TOPIC(
    "T11", "M2", "Squares with Holes, Shadings and Curves", ["8.4"], "Apply",
    "Students find the centre of a square as the meeting point of its diagonals, and use it to place a circular "
    "hole, then construct staircase, shaded and curved-side figures.",
    "The centre of a square is where its two diagonals meet; a circle drawn from that point sits in the middle.",
    [A("T11.C1", "The centre of a square: where the diagonals meet", "Apply",
       "Students locate the centre of a square as the meeting point of its two diagonals and use it as the compass "
       "tip for a circular hole in the middle.",
       textbook=book("8.4", "Construct (section 8.4)", start=3, stop=4),
       teach=["Predict first: a circular hole must sit exactly in the middle of a square. Where will the compass "
              "tip go?",
              "Join the opposite corners. The two diagonals cross at one point, and that point is the centre of the "
              "square.",
              "Put the tip there and draw a circle inside the square. The hole is centred."],
       examples=[we("8.4.ex7")],
       key_terms=["diagonal", "centre"], misconceptions=["M_CENTRE_ON_SIDE"], minutes=8),
     DOER("T11.C2", "Practice: staircases, shadings, holes and curves", None, "Apply",
          "Students plan and construct a staircase, a shading, a hole and a curve built from squares, circles and "
          "arcs, using a rough diagram to choose lengths and tip positions.",
          ["Make a rough diagram, mark each length, and decide the order of drawing.",
           "A centre of a square is where its diagonals meet.",
           "For an arc that bulges inward, the compass tip is outside the side, equally far from both ends."],
          textbook=book("8.4", "Construct (section 8.4)", start=0, stop=3)
          + book("8.4", "Construct (section 8.4)", start=4, stop=6),
          items=[fio("8.4.ex5"), fio("8.4.ex6"), fio("8.4.ex8"), fio("8.4.ex9")],
          misconceptions=["M_CENTRE_ON_SIDE", "M_ARC_TIP_ON_FIGURE"])]))
