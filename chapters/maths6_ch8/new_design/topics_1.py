# -*- coding: utf-8 -*-
"""Topics T1 to T6 (modules M1 and M2: the compass and circles, then squares and rectangles). Book sections 8.1 and 8.2."""
from topics_common import A, DOER, TOPIC, BOOK_TEXT, book, fio, we

TOPICS = []

# ============================== T1 Opening ===================================================================
TOPICS.append(TOPIC(
    "T1", "M1", "Drawing with a Ruler and a Compass", ["Chapter opening"], "Understand",
    "",
    "A bangle, a coin and a plate are round, but a hand cannot draw a round shape. Which tool makes every point "
    "of a curve equally far from one spot?",
    [A("T1.C1", "Why a hand cannot draw a perfect circle", "Remember", "",
       textbook=BOOK_TEXT["extra_inv_A.json"]["opening"]["textbook_lines"] + book("8.1", start=0, stop=3),
       teach=["Make a guess before the next step: can you draw a perfect circle freehand, with no help at all? "
              "Try one on paper.",
              "Now trace a bangle and put the two next to each other. The freehand one wobbles, the traced one is "
              "round.",
              "A ruler draws straight lines and a compass draws round curves. With these two tools we can build "
              "faces, waves, houses, squares and rectangles exactly."],
       ncert=["opening"], key_terms=["compass", "circle"], video_focus=["HOOK"], minutes=4, enrichment=True)],
    topic_type="framing"))

# ============================== T2 Circles with a compass (8.1) ==============================================
TOPICS.append(TOPIC(
    "T2", "M1", "Circles with a Compass", ["8.1"], "Apply",
    "Students recognise circles in artwork, explain that a circle is all the points at one fixed distance from its "
    "centre, and draw a circle of a given radius with a compass set against a ruler.",
    "A circle is every point at the same distance, the radius, from one point, the centre; the compass keeps that "
    "distance fixed while the pencil moves.",
    [A("T2.C1", "Circles in the artwork", "Understand",
       "Students describe how the circles in each artwork picture touch, overlap or share a centre, and say why "
       "freehand circles come out uneven.",
       textbook=book("8.1", start=0, stop=4),
       teach=["Predict first: five pictures are all made of circles. Which one looks hardest to draw by hand, and "
              "why?",
              "Two equal circles can touch, two circles can share one centre with the inner one smaller, and three "
              "equal circles can overlap in a row.",
              "A mouse face is one big circle for the face and two smaller circles for the ears.",
              "Freehand circles are uneven. We need a tool that keeps one distance fixed."],
       examples=[we("8.1.q1")],
       key_terms=["circle", "centre"], misconceptions=["M_FREEHAND_CIRCLE"], minutes=8),
     A("T2.C2", "All the points 4 cm from P", "Understand",
       "Students mark points that are 4 cm from a point P with a ruler in many directions and say that together "
       "they form a circle with centre P.",
       textbook=book("8.1", start=4, stop=8),
       teach=["Predict first: mark P and then every point that is exactly 4 cm from P. What shape will the dots "
              "make?",
              "Put the 0 cm mark of the ruler on P, never the end of the ruler, and mark a point at 4 cm. Turn the "
              "ruler and mark another.",
              "After many turns the dots make a round shape around P: a circle with centre P."],
       examples=[we("8.1.q2"), we("8.1.q3")],
       key_terms=["circle", "centre", "distance"], misconceptions=["M_RULER_END"], minutes=8),
     A("T2.C3", "The compass draws the circle: centre and radius", "Apply",
       "Students open a compass to 4 cm against a ruler, draw the circle with the tip fixed at the centre, and "
       "state that every point on it is one radius from the centre.",
       textbook=book("8.1", start=8, stop=15),
       teach=["Predict first: with the tip fixed on P and the pencil swung around, is any point of the curve nearer "
              "to P than 4 cm?",
              "Open the compass against a ruler until the tip and the pencil are 4 cm apart. Fix the tip at P and "
              "move only the pencil.",
              "The pencil stays 4 cm from the tip all the way round. The fixed point is the centre and that fixed "
              "distance is the radius.",
              "Keeko thinks the compass opening is the width of the whole circle. It is only the radius; the width "
              "is twice as much."],
       examples=[we("8.1.q4"), we("8.1.q5")],
       key_terms=["radius", "centre", "compass"], misconceptions=["M_RADIUS_DIAMETER", "M_RULER_END"], minutes=10),
     DOER("T2.C4", "Pull it together and do it: Compass Circle Maker", "compass_circle", "Apply",
          "Students set a radius on the compass tool, fix the centre, draw circles that touch, overlap or share a "
          "centre, and check points on them with a ruler.",
          ["A circle is all the points at one fixed distance from the centre.",
           "Set the compass opening against a ruler before drawing, and keep the tip fixed.",
           "Touching circles have centres two radii apart; concentric circles share a centre."],
          textbook=book("8.1", start=15, stop=18),
          items=[fio("8.1.q6")],
          misconceptions=["M_RADIUS_DIAMETER", "M_RULER_END"])]))

# ============================== T3 Waves from half circles (8.1) =============================================
TOPICS.append(TOPIC(
    "T3", "M1", "Waves from Half Circles", ["8.1"], "Apply",
    "Students find the compass radius and the tip positions for half circles drawn on a straight line, and build "
    "a wave of equal half circles on a line of any length.",
    "A half circle on a segment has that segment as its diameter, so the radius is half the segment; the tip sits "
    "at the middle of the segment.",
    [A("T3.C1", "A half circle on a line segment", "Apply",
       "Students find the radius and the compass tip position for a half circle drawn on a segment, and draw two "
       "equal half circles on the two halves of a line, one above and one below.",
       textbook=book("8.1", start=20, stop=21),
       teach=["Predict first: a line AB is 8 cm long and two equal half circles share it, one above the line and "
              "one below. How long is the flat side of each half circle?",
              "The two flat sides split AB into two equal parts of 4 cm each. Each flat side is the diameter of "
              "its half circle.",
              "The radius is half of the diameter, so the radius is 2 cm. The tip goes at the middle of each flat "
              "side, 2 cm from the end.",
              "Keeko sets the compass to 4 cm, the whole flat side. That draws a half circle that is too big."],
       examples=[we("8.1.ex2")],
       key_terms=["half circle", "diameter", "radius"], misconceptions=["M_RADIUS_DIAMETER"], minutes=10),
     DOER("T3.C2", "Pull it together and do it: Wave Builder", "wave_builder", "Apply",
          "Students choose a central line length on the wave tool, set the radius for each half circle, and draw "
          "waves that alternate above and below the line.",
          ["The flat side of a half circle is its diameter; the radius is half of it.",
           "Two equal half circles on a line of length L each have a diameter of half of L.",
           "The tip of the compass sits at the middle of each flat side."],
          textbook=book("8.1", start=21, stop=24),
          items=[fio("8.1.FiO.Q1"), fio("8.1.FiO.Q2")],
          misconceptions=["M_RADIUS_DIAMETER"])]))

# ============================== T4 Arcs for a person and eyes (8.1) ==========================================
TOPICS.append(TOPIC(
    "T4", "M1", "Arcs for A Person and Eyes", ["8.1"], "Apply",
    "Students draw a curved arc between two given corners by placing the compass tip off the figure, and build an "
    "eye from two arcs of equal radius with symmetric tip positions.",
    "An arc is a part of a circle; to draw it between two points, place the tip off the figure and swing a radius "
    "that reaches both points.",
    [A("T4.C1", "A curved body top for A Person", "Apply",
       "Students draw a circle for a head and an arc for the curved top of a body by trying tip positions above the "
       "body until the arc passes through both top corners.",
       textbook=book("8.1", start=19, stop=20),
       teach=["Predict first: the top of the body dips in the middle like a smile. Does the compass tip go on the "
              "body, or somewhere above it?",
              "The head is a circle with centre in the middle above the neck. The body top is an arc, and the tip "
              "of the compass is above the body, in line with the middle.",
              "Fix a radius, try a tip point above the body, and check that the arc passes through both top corners "
              "and touches the neck."],
       examples=[we("8.1.ex1")],
       key_terms=["arc", "compass"], misconceptions=["M_ARC_TIP_ON_FIGURE"], minutes=10),
     A("T4.C2", "Eyes from two arcs of equal radius", "Apply",
       "Students draw an almond-shaped eye from an upper and a lower arc of the same radius, with the two compass "
       "tips the same distance from the middle line, and fill the pupil.",
       textbook=book("8.1", start=25, stop=26),
       teach=["Predict first: an eye is two curves meeting at two pointed ends. Do both curves use the same "
              "radius?",
              "Draw two light guide lines. The tip of the upper curve is on one line and the tip of the lower "
              "curve is on the other.",
              "Keep the same radius and the same distance from the middle for both tips. Then the eye is "
              "symmetrical, and the second eye is a copy of the first."],
       examples=[we("8.1.ex3")],
       key_terms=["arc", "symmetrical"], misconceptions=["M_ARC_TIP_ON_FIGURE"], minutes=10),
     DOER("T4.C3", "Practice: waves smaller than a half circle", None, "Apply",
          "Students draw two identical arcs, smaller than a half circle, one above and one below a central line, "
          "as in the neck of A Person.",
          ["An arc smaller than a half circle uses a radius bigger than half the chord.",
           "The two tips are the same distance from the line, one above and one below.",
           "Equal radius and equal tip distance make the two arcs identical."],
          items=[fio("8.1.FiO.Q3")],
          misconceptions=["M_ARC_TIP_ON_FIGURE"])]))

# ============================== T5 What makes a square or a rectangle (8.2) ==================================
TOPICS.append(TOPIC(
    "T5", "M2", "What Makes a Square or a Rectangle", ["8.2"], "Understand",
    "Students state the two properties of a rectangle and of a square, tell the two shapes apart by checking sides "
    "and angles, and name a figure by taking its corners in order.",
    "A rectangle has opposite sides equal and all angles 90°; a square has all sides equal and all angles 90°, so "
    "every square is also a rectangle.",
    [A("T5.C1", "The two properties of a rectangle and of a square", "Understand",
       "Students state R1 and R2 for a rectangle and S1 and S2 for a square, and decide from sides and angles "
       "whether a figure is a rectangle, a square or neither.",
       textbook=book("8.2", start=0, stop=12),
       teach=["Predict first: a door, a notebook, a chessboard square. What do they share, and what is different?",
              "A rectangle satisfies R1, the opposite sides are equal in length, and R2, all the angles are 90°.",
              "A square satisfies S1, all the sides are equal, and S2, all the angles are 90°.",
              "A square also has opposite sides equal, so it meets R1 and R2 too. Keeko thinks a square is not a "
              "rectangle, but it is a special rectangle.",
              "Four equal sides are not enough. A slanted diamond has four equal sides and is not a square."],
       examples=[we("8.2.q1")],
       key_terms=["rectangle", "square", "opposite sides"],
       misconceptions=["M_SQUARE_NOT_RECT", "M_EQUAL_SIDES_SQUARE"], minutes=10),
     A("T5.C2", "Naming a figure by its corners in order", "Apply",
       "Students list the valid names of a square or rectangle by travelling round the corners in order, and say "
       "why a name that jumps across the figure is not valid.",
       textbook=book("8.2", start=12, stop=15),
       teach=["Predict first: a rectangle ABCD can be called BCDA. Can it also be called ABDC?",
              "In a valid name the corners come in an order of travel round the figure, starting from any corner "
              "and going either way.",
              "ABDC goes from B to D, and BD is a diagonal, not a side. So ABDC is not a name for the rectangle.",
              "Check each pair of neighbouring letters: it must be a side."],
       examples=[we("8.2.q2"), we("8.2.q3")],
       key_terms=["corner", "side"], misconceptions=["M_NAME_ANY_ORDER"], minutes=8),
     DOER("T5.C3", "Pull it together and do it: Shape Property Checker", "property_checker", "Apply",
          "Students measure sides and angles on the checker tool and classify each figure as a square, a "
          "rectangle, a rhombus or none of these.",
          ["Rectangle: opposite sides equal and all angles 90°.",
           "Square: all sides equal and all angles 90°.",
           "Equal sides alone do not give right angles; right angles alone do not give equal sides."],
          items=[fio("8.2.FiO.Q2")],
          misconceptions=["M_SQUARE_NOT_RECT", "M_EQUAL_SIDES_SQUARE"])]))

# ============================== T6 Rotated squares and rectangles (8.2) ======================================
TOPICS.append(TOPIC(
    "T6", "M2", "Rotated Squares and Rectangles", ["8.2"], "Apply",
    "Students explain why turning a square or a rectangle keeps it a square or a rectangle, and use dot positions "
    "across and down to decide on equal sides and right angles without measuring.",
    "Rotating a figure changes neither its lengths nor its angles, so a tilted square is still a square.",
    [A("T6.C1", "A rotated square is still a square", "Understand",
       "Students check the two square properties for a turned square and explain that rotation keeps lengths and "
       "angles, so the shape does not change.",
       textbook=book("8.2", "Rotated Squares and Rectangles", start=0, stop=7),
       teach=["Predict first: turn a square piece of paper so its corners point up, down, left and right. Is it "
              "still a square?",
              "Check S1: the sides are still equal, because turning does not stretch anything.",
              "Check S2: the angles are still 90°, because turning does not bend anything.",
              "So the tilted figure is a square. A rotated rectangle is a rectangle in the same way."],
       examples=[we("8.2.q4")],
       key_terms=["rotate", "square"], misconceptions=["M_TILT_NOT_SQUARE"], minutes=8),
     A("T6.C2", "Reading equal sides and right angles from dots", "Analyze",
       "Students move across and down by dot counts to show that two sides are equal and meet at 90°, without any "
       "measuring instrument.",
       textbook=book("8.2", "Rotated Squares and Rectangles", start=10, stop=11),
       teach=["Predict first: a tilted figure has its corners on dots. Can you tell that its sides are equal "
              "without a ruler?",
              "Go from one corner to the next by a number of dots across and a number down. If every side uses the "
              "same two numbers, the sides are equal.",
              "At the next corner swap the two numbers: across becomes down. That is a turn of 90°.",
              "So the dot positions alone show equal sides and right angles."],
       examples=[we("8.2.q5")],
       key_terms=["dot grid", "right angle"], misconceptions=["M_TILT_NOT_SQUARE"], minutes=8),
     DOER("T6.C3", "Practice: squares and rectangles on dot paper", None, "Apply",
          "Students draw a rectangle with four equal squares near its corners, and tilted squares and rectangles, "
          "on dot paper by counting dots, then check their properties.",
          ["Count the same dots across and down for every side of a square.",
           "Equal opposite sides and swapped counts at each corner make a rectangle.",
           "Check S1 and S2, or R1 and R2, to confirm each drawing."],
          textbook=book("8.2", "Rotated Squares and Rectangles", start=7, stop=10),
          items=[fio("8.2.FiO.Q1"), fio("8.2.FiO.Q3")],
          misconceptions=["M_TILT_NOT_SQUARE"])]))
