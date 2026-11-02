# -*- coding: utf-8 -*-
"""Topics T12 to T18 (modules M3 and M4: diagonals of rectangles, points equidistant from two points, summary).
Book sections 8.5 and 8.6."""
from topics_common import A, DOER, TOPIC, BOOK_TEXT, book, fio, we

TOPICS = []

# ============================== T12 Diagonals of a rectangle (8.5) ===========================================
TOPICS.append(TOPIC(
    "T12", "M3", "Diagonals of a Rectangle", ["8.5"], "Analyze",
    "Students measure the diagonals of rectangles and the angles they make with the sides, and state which "
    "lengths and angles come out equal.",
    "The two diagonals of any rectangle are equal, and each diagonal splits a corner of 90° into two angles that "
    "add up to 90°.",
    [A("T12.C1", "The two diagonals are equal", "Analyze",
       "Students predict, construct and measure to show that the two diagonals of a rectangle are equal in length.",
       textbook=book("8.5", start=0, stop=2),
       teach=["Predict first: in a rectangle PQRS, are the diagonals PR and QS equal, or is one longer?",
              "Construct a rectangle 6 cm by 4 cm, join the opposite corners, and measure both diagonals.",
              "Both measure about 7.2 cm. Try a second rectangle: the two diagonals match again."],
       examples=[we("8.5.q1")],
       key_terms=["diagonal", "rectangle"], misconceptions=["M_DIAG_EQUAL_SQUARE"], minutes=8),
     A("T12.C2", "How a diagonal splits the corners", "Analyze",
       "Students measure the two angles a diagonal makes at a corner, show that they add up to 90°, and name "
       "the pairs of equal angles formed by both diagonals.",
       textbook=book("8.5", start=2, stop=5),
       teach=["Predict first: the diagonal PR cuts the 90° corner at P into two angles. Will the two angles be "
              "equal?",
              "Measure them in the 6 cm by 4 cm rectangle: about 34° and about 56°. They are not equal, but they "
              "add up to 90°.",
              "With both diagonals drawn there are eight small angles. The four next to the sides PQ and SR match, "
              "and the four next to PS and QR match.",
              "So angles come in two sizes, and each pair of sizes adds up to 90°."],
       examples=[we("8.5.q2"), we("8.5.q3")],
       key_terms=["angle", "diagonal"], misconceptions=["M_DIAG_BISECT_ANGLES"], minutes=10),
     DOER("T12.C3", "Pull it together and do it: Diagonal Explorer", "diagonal_explorer", "Analyze",
          "Students change the sides of a rectangle on the tool, read both diagonals and the angles they make with "
          "the sides, and describe what stays the same.",
          ["The two diagonals stay equal for every rectangle.",
           "The two angles at a corner always add up to 90°.",
           "The angles are equal only when the sides are equal."],
          items=[],
          misconceptions=["M_DIAG_EQUAL_SQUARE", "M_DIAG_BISECT_ANGLES"])]))

# ============================== T13 Squares and the laws of diagonals (8.5) ==================================
TOPICS.append(TOPIC(
    "T13", "M3", "When a Diagonal Splits a Corner Equally", ["8.5"], "Evaluate",
    "Students find the one rectangle whose diagonal splits the corners into equal parts, state the laws of "
    "diagonals in their own words, and say why measuring a few cases is not a proof.",
    "A diagonal splits a corner into two equal angles only in a square; measurements suggest a law, but a reason "
    "is needed to be sure it holds for every rectangle.",
    [A("T13.C1", "Which rectangle splits its corner equally?", "Analyze",
       "Students explain that the diagonal splits a corner into equal parts only when two adjacent sides are "
       "equal, so the rectangle is a square.",
       textbook=book("8.5", "Explore", start=0, stop=1),
       teach=["Predict first: how should the sides of a rectangle be chosen so that the diagonal splits the corner "
              "into two equal angles?",
              "Keep one side 4 cm and change the other: 5 cm, 6 cm, 4.5 cm. The two angles stay unequal.",
              "Only when the two sides are equal, 4 cm and 4 cm, do both angles come out 45°."],
       examples=[we("8.5.q4")],
       key_terms=["diagonal", "square"], misconceptions=["M_DIAG_BISECT_ANGLES"], minutes=8),
     A("T13.C2", "The square is a special case", "Understand",
       "Students show that in a square the two diagonals are equal and all eight angles formed with the sides "
       "are 45°.",
       textbook=book("8.5", "Explore", start=1, stop=3),
       teach=["Predict first: draw a square of side 5 cm and both diagonals. What will every small angle measure?",
              "All eight angles are 45°, and the two diagonals are equal, about 7.07 cm each.",
              "A square is a rectangle, so it follows every law of a rectangle, and it also has this extra one."],
       examples=[we("8.5.q7")],
       key_terms=["square", "diagonal"], misconceptions=["M_SQUARE_NOT_RECT"], minutes=8),
     DOER("T13.C3", "Practice: laws of rectangles and how sure we can be", None, "Evaluate",
          "Students state the laws of sides, angles and diagonals of a rectangle and explain why measuring a few "
          "rectangles cannot prove a law for all rectangles.",
          ["Opposite sides are equal and every angle is 90°.",
           "Both diagonals are equal and cut each other into equal halves.",
           "A few measurements suggest a law, a reason makes sure of it."],
          textbook=book("8.5", "Math Talk"),
          items=[fio("8.5.q5"), fio("8.5.q6")],
          misconceptions=["M_DIAG_EQUAL_SQUARE"])]))

# ============================== T14 Constructing a rectangle from a diagonal angle (8.5) ======================
TOPICS.append(TOPIC(
    "T14", "M3", "Constructing a Rectangle from a Diagonal Angle", ["8.5"], "Apply",
    "Students construct a rectangle in which a diagonal splits a corner into two given angles, by planning the "
    "order of steps from a rough diagram.",
    "Draw one side, a perpendicular at one end, and the diagonal at the given angle; the corner where the "
    "diagonal meets the second side fixes the rectangle.",
    [A("T14.C1", "A diagonal that splits a corner into 60° and 30°", "Apply",
       "Students construct a rectangle ABCD in which the diagonal AC splits the corner A into 60° and 30°, using "
       "the fact that the two angles add up to 90°.",
       textbook=book("8.5", "Construct (solved example 1)", start=0, stop=16),
       teach=["Predict first: if the diagonal makes 60° with AB, what angle does it make with AD?",
              "Draw a rough diagram and decide the order. AB is drawn first with any length.",
              "At A draw a line perpendicular to AB, then draw the diagonal AC at 60° from AB. The other angle "
              "is 30°.",
              "Mark C where the diagonal meets the perpendicular drawn at B, then find D with a perpendicular at "
              "C or with the compass so that AD matches BC."],
       examples=[we("8.5.ex1"), we("8.5.q8")],
       key_terms=["rough diagram", "diagonal"], misconceptions=["M_NAME_ANY_ORDER"], minutes=10),
     DOER("T14.C2", "Practice: rectangles from the angle of a diagonal", None, "Apply",
          "Students construct rectangles whose diagonal splits a corner into 50° and 40°, and into 45° and 45°, "
          "and say what the second one shows about the sides.",
          ["Draw AB, then the diagonal at the given angle from AB.",
           "The two angles at a corner always add up to 90°.",
           "When both angles are 45°, all four sides are equal and the rectangle is a square."],
          textbook=book("8.5", "Construct (solved example 1)", start=16, stop=21)
          + book("8.5", "Construct (exercise)", start=0, stop=2),
          items=[fio("8.5.FiO.Q1"), fio("8.5.FiO.Q2")],
          misconceptions=["M_DIAG_BISECT_ANGLES"])]))

# ============================== T15 Constructing a rectangle from a side and a diagonal (8.5) =================
TOPICS.append(TOPIC(
    "T15", "M3", "Constructing a Rectangle from a Side and a Diagonal", ["8.5"], "Apply",
    "Students construct a rectangle from one side and one diagonal, and use a circle or an arc of radius equal "
    "to the diagonal to find the missing corner.",
    "A corner that must be a fixed distance from a known point lies on a circle around that point; the circle "
    "meets the perpendicular at the corner we need.",
    [A("T15.C1", "A rectangle with a side of 5 cm and a diagonal of 7 cm", "Apply",
       "Students plan the order of steps for a rectangle with a side of 5 cm and a diagonal of 7 cm, and decide "
       "which line to draw first.",
       textbook=book("8.5", "Construct (solved example 2)", start=0, stop=12),
       teach=["Predict first: you know a side of 5 cm and a diagonal of 7 cm. Which line can you draw first?",
              "Draw the base CD of 5 cm. Then draw a perpendicular at C, the line l.",
              "The corner B has to be on l, and it has to be 7 cm from D because DB is the diagonal."],
       examples=[we("8.5.ex2"), we("8.5.q9")],
       key_terms=["diagonal", "perpendicular"], misconceptions=["M_ARC_FROM_ONE_POINT"], minutes=8),
     A("T15.C2", "A circle holds every point at 7 cm from D", "Understand",
       "Students use a circle or an arc of radius 7 cm centred at D to find the point B on the line l, and "
       "explain why only a short arc is needed.",
       textbook=book("8.5", "Construct (solved example 2)", start=12, stop=23),
       teach=["Predict first: which curve contains every point that is exactly 7 cm from D?",
              "Draw a circle of radius 7 cm with centre D. It meets the line l at one point, and that point is "
              "7 cm from D. So that point is B.",
              "We only need the arc near the line l, so a short arc is enough."],
       examples=[we("8.5.q10"), we("8.5.q11")],
       key_terms=["radius", "arc"], misconceptions=["M_ARC_FROM_ONE_POINT", "M_RADIUS_DIAMETER"], minutes=8),
     A("T15.C3", "Completing the rectangle and checking it", "Apply",
       "Students complete the rectangle with perpendiculars at D and B, and check that opposite sides are equal "
       "and every angle is 90°.",
       textbook=book("8.5", "Construct (solved example 2)", start=23, stop=27),
       teach=["Predict first: with three corners marked, how will you find the fourth?",
              "Draw perpendiculars to DC and BC at D and at B. They meet at the fourth corner.",
              "Check the two properties: opposite sides are equal, and all angles are 90°. The sides come to 5 cm "
              "and about 4.9 cm."],
       examples=[we("8.5.q12")],
       key_terms=["rectangle", "perpendicular"], misconceptions=["M_NAME_ANY_ORDER"], minutes=8),
     DOER("T15.C4", "Pull it together and do it: Side and Diagonal Builder", "side_diagonal_builder", "Apply",
          "Students build a rectangle from a side and a diagonal on the tool, and read the second side that "
          "comes out.",
          ["Draw the base, a perpendicular at one end, and an arc around the other end.",
           "The arc meets the perpendicular at the third corner.",
           "Finish with perpendiculars and check both properties."],
          textbook=book("8.5", "Construct (exercise)", start=2, stop=4),
          items=[fio("8.5.FiO.Q3"), fio("8.5.FiO.Q4")],
          misconceptions=["M_ARC_FROM_ONE_POINT"])]))

# ============================== T16 Points equidistant from two points (8.6) =================================
TOPICS.append(TOPIC(
    "T16", "M4", "Points the Same Distance from Two Points", ["8.6"], "Apply",
    "Students find the point that is a given distance from each of two points by crossing two arcs, and use it "
    "to build the house figure.",
    "Draw an arc of the same radius around each of the two points; where the arcs cross, the point is that far "
    "from both.",
    [A("T16.C1", "Where two circles meet", "Understand",
       "Students show that a point where two circles of radius 5 cm meet is 5 cm from both centres, and say why "
       "short arcs are enough.",
       textbook=book("8.6", "Construct: House (solved example)", start=5, stop=24),
       teach=["Predict first: B and C are 5 cm apart in a house figure. Where is the apex A, 5 cm from both?",
              "A circle around B holds every point 5 cm from B, and a circle around C does the same for C.",
              "They meet at A, which is 5 cm from B and 5 cm from C.",
              "Two short arcs that cross are enough, no full circles needed."],
       examples=[we("8.6.q1"), we("8.6.q2")],
       key_terms=["circle", "arc"], misconceptions=["M_ARC_FROM_ONE_POINT", "M_ARC_TIP_ON_FIGURE"], minutes=10),
     A("T16.C2", "Building the house", "Apply",
       "Students construct the house with sides of 5 cm, finding the apex with two arcs and drawing the curved "
       "top from the apex.",
       textbook=book("8.6", "Construct: House (solved example)", start=0, stop=5)
       + book("8.6", "Construct: House (solved example)", start=24, stop=31),
       teach=["Predict first: which part of the house do you draw first, and which last?",
              "Draw the rectangle with the door, then find the apex A by crossing two arcs of 5 cm from B and C.",
              "Join A to B and A to C. Then put the compass tip at A and draw the arc from B to C.",
              "The house is ready: every border line is 5 cm."],
       examples=[we("8.6.ex1")],
       key_terms=["apex", "arc"], misconceptions=["M_ARC_TIP_ON_FIGURE"], minutes=10),
     DOER("T16.C3", "Pull it together and do it: Equal Distance Explorer", "equidistant_explorer", "Apply",
          "Students place two points on the tool, set a radius, and watch where the two arcs cross to locate the "
          "point at that distance from both, then build a bigger house.",
          ["An arc around each point holds the points at that distance from it.",
           "The crossing point is the same distance from both points.",
           "The radius must be big enough for the arcs to meet."],
          textbook=book("8.6", "Construct (exercise)", start=0, stop=1),
          items=[fio("8.6.FiO.Q1")],
          misconceptions=["M_ARC_FROM_ONE_POINT"])]))

# ============================== T17 Equal sides but not a square (8.6) =======================================
TOPICS.append(TOPIC(
    "T17", "M4", "Equal Sides but Not a Square", ["8.6"], "Create",
    "Students construct a four-sided figure with four equal sides that is not a square, and use the arcs idea "
    "to recreate the artwork figures.",
    "The same two-arc idea gives a figure with four equal sides whose angles are not 90°, and it also redraws "
    "the artwork from the start of the chapter.",
    [A("T17.C1", "Four equal sides, angles not 90°", "Create",
       "Students construct a four-sided figure with all sides 5 cm and an angle other than 90°, by finding the "
       "fourth corner with two arcs.",
       textbook=book("8.6", "Hints", start=4, stop=8),
       teach=["Predict first: are there four-sided figures with four equal sides that are not squares?",
              "Draw a side BC of 5 cm and a side BA of 5 cm at a slant. The fourth corner D has to be 5 cm from "
              "A and from C.",
              "Cross two arcs of 5 cm to find D. The figure has four equal sides, but its angles are not 90°.",
              "This is a rhombus. Equal sides are not enough for a square, we also need right angles."],
       key_terms=["rhombus", "arc"], misconceptions=["M_EQUAL_SIDES_SQUARE"], minutes=10),
     DOER("T17.C2", "Practice: a rhombus and the artwork redrawn", None, "Create",
          "Students decide whether an equal-sided figure must be a square, construct one that is not, and "
          "recreate the Person, Wavy Wave and Eyes artwork with arcs.",
          ["Cross two arcs of the same radius to find a corner that is the same distance from two points.",
           "Equal sides alone do not make a square.",
           "For the Eyes, estimate the arc centres so the upper and lower curves match."],
          textbook=book("8.6", "Construct (exercise)", start=1, stop=3) + book("8.6", "Hints", start=0, stop=4),
          items=[fio("8.6.FiO.Q2"), fio("8.6.FiO.Q3")],
          misconceptions=["M_EQUAL_SIDES_SQUARE"])]))

# ============================== T18 Summary ==================================================================
TOPICS.append(TOPIC(
    "T18", "M4", "Summary: Playing with Constructions", ["Summary"], "Remember",
    None,
    "Circles and arcs from a compass, rectangles from sides, diagonals or angles, and points equally far from two "
    "points.",
    [A("T18.C1", "What we found about constructions", "Remember",
       "Students restate that a circle is all points at one distance from its centre, how a rough diagram plans "
       "a construction, and how a rectangle is built from sides or from a side and a diagonal.",
       textbook=["Let's Summarise!"] + book("8.6", "Summary"),
       teach=["Our opening question is settled: a compass keeps one distance fixed, so every point it draws is "
              "equally far from the centre.",
              "A rough diagram plans the order of steps, and a rectangle needs its sides, or a side and a "
              "diagonal.",
              "Still open for you: can you build a rectangle whose diagonal is exactly twice its shorter side?"],
       ncert=["summary"], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
