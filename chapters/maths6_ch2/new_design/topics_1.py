# -*- coding: utf-8 -*-
"""Topics T1 to T5 (modules M1 and M2 begin): chapter opening, points and segments, lines and rays, angles,
comparing angles. Book sections 2.1 to 2.6."""
from topics_common import A, DOER, TOPIC, WE, BOOK_TEXT, book, fio, tb, we

TOPICS = []
H_SUP = "Comparing angles by superimposition"
H_WITHOUT = "Comparing angles without superimposition"
OPEN = BOOK_TEXT["extra_inv_A.json"]["opening"]["textbook_lines"]

# ============================== T1 Chapter opening ===========================================================
TOPICS.append(TOPIC(
    "T1", "M1", "Bends and Turns Around Us", ["Chapter opening"], "Understand",
    "",
    "Doors, scissors, arms and legs all bend or open by turning one part about a point, and the chapter asks how "
    "to name and measure that turn.",
    [A("T1.C1", "Where do bends and turns hide?", "Remember", "",
       textbook=tb(OPEN),
       teach=["Look at the dancing figures on the chapter page and at a door, a pair of scissors and your own arm. "
              "Before reading on, guess: what do they all do that a plain straight stick does not?",
              "Each one has two parts joined at one point, and one part can turn about that point.",
              "When the turn is small the parts stay close, and when it is big they open wide. How can we name "
              "that turn, compare two of them and measure one? That is what this chapter finds out."],
       key_terms=["point", "turn", "angle"], video_focus=["HOOK"], minutes=4, enrichment=True)],
    topic_type="framing"))

# ============================== T2 Points and line segments (2.1, 2.2) =======================================
TOPICS.append(TOPIC(
    "T2", "M1", "Points and Line Segments", ["2.1", "2.2"], "Understand",
    "Students name a point with a capital letter and say that a line segment is the shortest path between two "
    "points, including both end points.",
    "A point marks an exact place and is named by a capital letter; the line segment AB is the shortest path from "
    "A to B.",
    [A("T2.C1", "A point and a line segment from a crease", "Understand",
       "Students mark a point with a sharp pencil tip, label the dot with a capital letter, and see a folded crease as a "
       "line segment with two end points.",
       textbook=tb(book("2.1") + book("2.2", stop=1)),
       teach=["Predict first: you press a very sharp pencil on paper to make a dot. Does a sharper tip make the dot "
              "bigger or smaller?",
              "The sharper the tip, the thinner the dot. A point marks an exact place, and we name it with a "
              "capital letter such as A or B.",
              "Fold a paper and open it. The crease is straight and has two ends, A and B. A straight piece with "
              "two end points is a line segment."],
       examples=[we("2.2.q1")],
       key_terms=["point", "line segment", "end point"], misconceptions=["M_SEG_ANY_ROUTE"], minutes=8),
     A("T2.C2", "The shortest route from A to B", "Understand",
       "Students compare routes between two points and conclude that the straight one is the shortest and is the "
       "line segment AB.",
       textbook=tb(book("2.2", start=1)),
       teach=["Predict first: you join two points A and B by a zig-zag route, a curved route and a straight route. "
              "Which do you think is the shortest?",
              "Draw them and compare the lengths. The straight route is the shortest.",
              "This shortest path from A to B, including A and B, is the line segment AB."],
       examples=[we("2.2.q2")],
       key_terms=["line segment", "shortest path"], misconceptions=["M_SEG_ANY_ROUTE"], minutes=8)]))

# ============================== T3 Lines and rays (2.3, 2.4) =================================================
TOPICS.append(TOPIC(
    "T3", "M1", "Lines and Rays", ["2.3", "2.4"], "Apply",
    "Students tell a line segment, a line and a ray apart, name them correctly, and say how many lines pass "
    "through one point or through two points.",
    "A line goes on forever both ways, a ray starts at one point and goes on one way, and two points fix exactly "
    "one line.",
    [A("T3.C1", "A line goes on forever", "Understand",
       "Students explain why a complete line cannot be drawn, say that two points fix exactly one line, and name a "
       "line through two points.",
       textbook=tb(book("2.3")),
       teach=["Predict first: extend a line segment AB past A and past B without ever stopping. Can you draw the "
              "whole of it on a sheet of paper?",
              "No. A line goes on forever in both directions, so we draw a part of it and put arrowheads at both "
              "ends.",
              "Any two points fix one line that passes through both of them. We write it as line AB or name it l "
              "or m."],
       examples=[we("2.3.q1")],
       key_terms=["line", "arrowhead"], misconceptions=["M_LINE_ENDS", "M_ONE_LINE_POINT"], minutes=8),
     A("T3.C2", "A ray starts at a point", "Understand",
       "Students recognise a ray as a part of a line with one starting point, and write its name with the starting point "
       "first.",
       textbook=tb(book("2.4", stop=2)),
       teach=["Predict first: a torch shines a beam. Does the beam have a start, an end, or both?",
              "The beam starts at the torch and goes on in one direction without stopping. A part of a line that "
              "starts at one point and goes on one way forever is a ray.",
              "We name a ray with the starting point first, so ray TL starts at T and passes through L. Ray LT "
              "would start at L."],
       examples=[WE("A torch at T shines a beam towards a lamp post L. The beam goes past L and never stops. Is the "
                    "beam a line segment, a ray or a line? Name it.",
                    ["The beam starts at T, a fixed starting point.",
                     "It passes through L and goes on in one direction without end.",
                     "A part of a line with one starting point is a ray.",
                     "The starting point comes first in the name, so the beam is ray TL."],
                    "It is a ray, named TL, with starting point T.")],
       key_terms=["ray", "starting point"], misconceptions=["M_RAY_BOTH", "M_RAY_ENDS"], minutes=8),
     DOER("T3.C3", "Pull it together and do it: Name It", "name_it", "Apply",
          "Students name the points, line segments, rays and lines in a figure, draw a figure from a description, "
          "and say whether two names of a ray are the same.",
          ["A line segment has two end points, a ray has one starting point, a line has none.",
           "The starting point comes first in the name of a ray, so OA and AO are different rays.",
           "Through one point many lines pass; through two points exactly one."],
          items=[fio("2.4.FiO.Q1"), fio("2.4.FiO.Q2"), fio("2.4.FiO.Q3"), fio("2.4.FiO.Q4"), fio("2.4.FiO.Q5"),
                 fio("2.4.FiO.Q6")],
          misconceptions=["M_RAY_BOTH", "M_ONE_LINE_POINT", "M_LINE_ENDS"])]))

# ============================== T4 Angle (2.5) ===============================================================
TOPICS.append(TOPIC(
    "T4", "M1", "What Is an Angle?", ["2.5"], "Apply",
    "Students name the vertex and the arms of an angle in everyday objects, see its size as the amount of turn, "
    "and name an angle with three letters.",
    "An angle is two rays from one point; its size is the amount one arm turns about the vertex, and the name "
    "puts the vertex in the middle.",
    [A("T4.C1", "Arms and vertex in everyday things", "Understand",
       "Students mark the two arms and the vertex of the angle in a book cover, a compass, scissors and a "
       "hinged object.",
       textbook=tb(book("2.5", stop=5) + book("2.5", start=9, stop=13)),
       teach=["Predict first: Vidya opens the cover of her book a little. Is there an angle here, and where is "
              "its corner?",
              "An angle is formed by two rays with a common starting point. The common point is the vertex, and "
              "the two rays are the arms.",
              "In the book the cover and the first page are the arms and the spine is the vertex. In a compass the "
              "legs are the arms and the joint is the vertex. In scissors the blades are the arms and the screw "
              "is the vertex."],
       examples=[we("2.5.q1"), we("2.5.q3"), we("2.5.q4"), we("2.5.q5")],
       key_terms=["angle", "vertex", "arm"], misconceptions=["M_STRAIGHT_NOT_ANGLE"], minutes=10),
     A("T4.C2", "An angle is the amount of turn", "Understand",
       "Students see that the size of an angle is the amount one arm turns about the vertex, so opening the cover "
       "more makes a greater angle.",
       textbook=tb(book("2.5", start=5, stop=9) + book("2.5", start=13, stop=14)),
       teach=["Predict first: Vidya opens her cover a little in Case 1 and more in Case 2. Which angle is "
              "greater, and what changed?",
              "In Case 2 she turns the cover more, so the angle is greater. The size of an angle is the amount "
              "of turn needed about the vertex to take the first ray to the second.",
              "Look at the crane's mouth, a door and a pair of scissors: each angle forms when one arm turns "
              "about the vertex."],
       examples=[we("2.5.q2"), we("2.5.q6")],
       key_terms=["turn", "size of an angle"], misconceptions=["M_ARM_LENGTH", "M_ANGLE_AS_GAP"], minutes=8),
     DOER("T4.C3", "Pull it together and do it: Name the Angle", "angle_namer", "Apply",
          "Students name angles with three letters with the vertex in the middle, find the arms and vertex in "
          "pictures, and count the angles formed by three or four points.",
          ["An angle is named with a point on each arm and the vertex in the middle.",
           "When more than one angle shares a vertex, one letter cannot name it.",
           "Three points not on one line give 3 angles, and four such points give 12."],
          items=[fio("2.5.FiO.Q1"), fio("2.5.FiO.Q2"), fio("2.5.FiO.Q3"), fio("2.5.FiO.Q4"), fio("2.5.FiO.Q5"),
                 fio("2.5.FiO.Q6")],
          misconceptions=["M_ANGLE_P", "M_ARM_LENGTH"])]))

# ============================== T5 Comparing angles (2.6) ====================================================
TOPICS.append(TOPIC(
    "T5", "M2", "Comparing Angles", ["2.6"], "Apply",
    "Students compare two angles by placing one over the other, say when two angles are equal, and compare with "
    "a transparent circle when an overlap is hard.",
    "Two angles are compared by superimposition: put the vertices together and one arm over one arm, and see "
    "where the other arm falls.",
    [A("T5.C1", "Comparing by superimposition", "Apply",
       "Students compare two labelled angles by placing one over the other with the vertices together and one arm "
       "over one arm.",
       textbook=tb(book("2.6", stop=1) + book("2.6", start=2, stop=4) + book("2.6", H_SUP, stop=3)),
       teach=["Predict first: a snake, a fish, a bird and a crocodile open their mouths. Which angle is the "
              "biggest? How could you be sure?",
              "Trace one angle, place it over the other with the two vertices together and one arm over one arm.",
              "Now see where the second arm falls. If it lies outside the other angle that angle is larger, and "
              "label each angle first so you can say which is which."],
       examples=[we("2.6.q1"), we("2.6.q3")],
       key_terms=["superimposition", "compare"], misconceptions=["M_COMPARE_EYE", "M_ARM_LENGTH"], minutes=10),
     A("T5.C2", "Equal angles, whatever the arm length", "Analyze",
       "Students see that two angles are equal when they fit exactly on each other, and use the idea to compare "
       "other things.",
       textbook=tb(book("2.6", H_SUP, start=3, stop=8)),
       teach=["Predict first: ∠AOB has short arms and ∠XOY has long arms but the same opening. Which is greater?",
              "Place them over each other with O on O and OA on OX. OB also falls on OY, so the two angles are "
              "equal.",
              "Superimposition is used for other things too, such as comparing two line segments, two squares or "
              "two circles."],
       examples=[we("2.6.q4"), we("2.6.q5")],
       key_terms=["equal angles", "superimposition"], misconceptions=["M_ARM_LENGTH", "M_COMPARE_EYE"],
       minutes=8),
     A("T5.C3", "Comparing with a transparent circle", "Analyze",
       "Students place a transparent circle on an angle, mark where the arms cross it, and compare two angles by "
       "where the second arm meets the circle.",
       textbook=tb(book("2.6", H_WITHOUT, stop=9)),
       teach=["Predict first: is it always easy to compare two angles by eye? Think of angles of 89° and 91°.",
              "Place a transparent circle with its centre on the vertex and mark A and B where the arms cross the "
              "circle.",
              "Move the circle to the second angle, put one arm through A, and see where the other arm meets the "
              "circle compared with B. A point beyond B means a bigger angle."],
       examples=[
           we("2.6.q2"),
           we("2.6.q6", answer="Compare where the second arm meets the circle, at Y, with the point B. If Y is "
                               "beyond B the second angle is bigger, if Y falls on B they are equal, and if Y "
                               "falls short of B it is smaller. Here Y is very close to B, so the two angles are "
                               "nearly equal."),
           we("2.6.q7", answer="Trace both beak angles, place the transparent circle on each with its centre on "
                               "the vertex, mark where the arms cross, and compare the gaps between the marked "
                               "points on the circle. The crane whose arms are further apart makes the bigger "
                               "angle.")],
       key_terms=["transparent circle", "compare"], misconceptions=["M_COMPARE_EYE"], minutes=10),
     DOER("T5.C4", "Pull it together and do it: Which Angle Is Greater?", "angle_comparer", "Apply",
          "Students drag one angle over another on the tool, say which is greater or whether they are equal, and "
          "give a reason.",
          ["Put the vertices together and one arm over one arm.",
           "The angle whose second arm falls outside is the greater one.",
           "Arm length does not change the size of an angle."],
          items=[fio("2.6.FiO.Q1"), fio("2.6.FiO.Q2"), fio("2.6.FiO.Q3")],
          misconceptions=["M_COMPARE_EYE", "M_ARM_LENGTH"])]))


# T2 closes with a short recap-only doer (no tool, no exercises of its own)
assert TOPICS[1]["key"] == "T2"
TOPICS[1]["concepts"].append(DOER(
    "T2.C3", "Practice: Points and Segments", None, "Understand",
    "Students recall that a point marks an exact place and that the line segment is the shortest path between "
    "two points, and give an example of each from around them.",
    ["A point marks an exact place and is named by a capital letter.",
     "A line segment is the shortest path between two points and has two ends.",
     "A curved or zig-zag route between the same two points is longer than the segment."],
    items=[], misconceptions=["M_SEG_ANY_ROUTE"]))
