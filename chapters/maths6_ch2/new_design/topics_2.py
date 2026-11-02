# -*- coding: utf-8 -*-
"""Topics T6 to T11: rotating arms, straight and right angles, acute and obtuse angles, degrees, reading a
protractor, the paper protractor. Book sections 2.7 to 2.9 (first half)."""
from topics_common import A, DOER, TOPIC, WE, book, fio, tb, we

TOPICS = []
H_LET = "Let's Explore"
H_CLASS = "Classifying Angles"
H_MEAS = "Measures of different angles"
H_HIST = "A pinch of history"
H_DEG = "Degree measures of different angles"
H_UNLAB = "Unlabelled protractor"
H_LAB = "Labelled protractor"
H_DIRECT = "How can we measure angles directly without having to subtract?"
H_OWN = "Make your own Protractor!"
H_BIS = "Angle Bisector"

# ============================== T6 Rotating arms (2.7) =======================================================
TOPICS.append(TOPIC(
    "T6", "M2", "Making Rotating Arms", ["2.7"], "Apply",
    "Students make rotating arms from two straws and a paper clip, use them to compare angles, and see that the "
    "length of the arms does not change an angle.",
    "Rotating arms model an angle; only the turn between the arms matters, not how long the arms are.",
    [A("T6.C1", "Rotating arms and the slit", "Apply",
       "Students make rotating arms, order them by superimposition, and find the one that passes through a slit "
       "of the same angle.",
       textbook=tb(book("2.7", stop=9)),
       teach=["Predict first: two paper straws and a paper clip. Can you make an angle that you can open and "
              "close?",
              "Put the straws into the two arms of the clip. This rotating arm has a vertex at the clip and two "
              "arms. Compare several by superimposition and arrange them from smallest to largest.",
              "Cut an angle-shaped slit in cardboard. Only the rotating arm whose angle equals the slit goes "
              "through, and the length of the arms does not matter."],
       examples=[we("2.7.q1"), we("2.7.q2")],
       key_terms=["rotating arms", "slit"], misconceptions=["M_ARM_LENGTH", "M_COMPARE_EYE"], minutes=10),
     A("T6.C2", "Cutting the arms does not shrink the angle", "Analyze",
       "Students explain why snipping the ends of the arms leaves an angle unchanged, and say how to really reduce "
       "it.",
       textbook=tb(book("2.7", start=9)),
       teach=["Predict first: a girl snips the ends off the arms of a V-shaped rotating arm. Is the angle now "
              "smaller?",
              "The two arms still meet at the same vertex with the same turn between them, so the angle is "
              "unchanged.",
              "To reduce the angle, turn one arm towards the other. The size of an angle is the amount of turn, "
              "not the length of the arms."],
       examples=[we("2.7.q3")],
       key_terms=["angle", "turn"], misconceptions=["M_ARM_LENGTH", "M_ANGLE_AS_GAP"], minutes=8)]))

# ============================== T7 Straight and right angles (2.8) ===========================================
TOPICS.append(TOPIC(
    "T7", "M2", "Straight Angles and Right Angles", ["2.8"], "Apply",
    "Students see the straight angle as a half turn, fold it into two equal angles to get right angles, and say "
    "that a right angle is a quarter turn.",
    "A straight angle is a half turn; folding it in half gives two equal angles, each a right angle or a quarter "
    "turn.",
    [A("T7.C1", "Folding a straight angle in half", "Apply",
       "Students fold a straight angle so that its two arms overlap, and explain why the two angles formed are "
       "equal.",
       textbook=tb(book("2.8", stop=5) + book("2.8", H_LET, stop=6)),
       teach=["Predict first: a straight angle AOB is a half turn. Can a ray OC split it into two equal angles?",
              "Mark the straight angle on a paper and fold so that OB lies on OA. The crease through O is OC.",
              "The two arms overlap exactly, so the two angles fit on each other and are equal. Folding is the "
              "superimposition. Each equal angle is a right angle."],
       examples=[we("2.8.q1"), we("2.8.q2"), we("2.8.q3")],
       key_terms=["straight angle", "right angle", "half turn"], misconceptions=["M_STRAIGHT_NOT_ANGLE"],
       minutes=10),
     A("T7.C2", "A right angle is a quarter turn", "Understand",
       "Students say that a right angle is a quarter of a full turn, and that it can be turned in any direction.",
       textbook=tb(book("2.8", H_LET, start=7, stop=9)),
       teach=["Predict first: a straight angle is half of a full turn. How much of a full turn is a right angle?",
              "A straight angle holds two right angles, so a right angle is half of a half turn, which is a "
              "quarter turn.",
              "A right angle looks like an L, and it stays a right angle however the paper is turned."],
       examples=[we("2.8.q4")],
       key_terms=["right angle", "quarter turn"], misconceptions=["M_RIGHT_UPRIGHT", "M_RIGHT_ANY_L"], minutes=8),
     DOER("T7.C3", "Pull it together and do it: Fold a Right Angle", "fold_right", "Apply",
          "Students fold a paper on the tool to make a straight angle, a right angle and a perpendicular crease, "
          "and find right angles on a grid and in the classroom.",
          ["A straight angle is a half turn and a right angle is a quarter turn.",
           "A fold that puts one arm of a straight angle on the other makes two right angles.",
           "Two creases at a right angle give four right angles."],
          items=[fio("2.8.FiO1.Q1"), fio("2.8.FiO1.Q2"), fio("2.8.FiO1.Q3"), fio("2.8.FiO1.Q4")],
          misconceptions=["M_RIGHT_UPRIGHT", "M_RIGHT_ANY_L"])]))

# ============================== T8 Acute and obtuse angles (2.8) =============================================
TOPICS.append(TOPIC(
    "T8", "M2", "Acute, Right and Obtuse Angles", ["2.8"], "Apply",
    "Students sort angles into three groups by comparing each with a right angle, and name them acute, right "
    "and obtuse.",
    "Compared with a right angle, an angle is acute if it is smaller, right if it fits exactly, and obtuse if it "
    "is bigger but less than a straight angle.",
    [A("T8.C1", "Sorting angles by the right angle", "Apply",
       "Students sort angles into three groups by comparing each with a right angle, and name the groups acute, "
       "right and obtuse.",
       textbook=tb(book("2.8", H_CLASS)),
       teach=["Predict first: three boxes hold angles. In the middle box are right angles. What do the angles in "
              "the other two boxes have in common?",
              "Every angle in the first box is smaller than a right angle, less than a quarter turn. These are "
              "acute angles.",
              "Every angle in the third box is bigger than a right angle but smaller than a straight angle. These "
              "are obtuse angles."],
       examples=[we("2.8.q5")],
       key_terms=["acute angle", "obtuse angle", "right angle"],
       misconceptions=["M_ACUTE_SMALL_DRAWING", "M_RIGHT_ANY_L"], minutes=8),
     DOER("T8.C2", "Pull it together and do it: Spot the Type", None, "Apply",
          "Students identify acute, right, obtuse and straight angles in figures, draw some in different "
          "orientations, say why the words acute and obtuse were chosen, and count acute angles in a pattern.",
          ["Less than a right angle is acute, exactly a right angle is right.",
           "More than a right angle and less than a straight angle is obtuse.",
           "The size of the turn decides the type, not the length of the arms or the way the angle points."],
          items=[fio("2.8.FiO2.Q1"), fio("2.8.FiO2.Q2"), fio("2.8.FiO2.Q3"),
                 fio("2.8.FiO2.Q4", answer="3, 12, 21 and 30 acute angles. Each small triangle has 3 acute "
                                           "angles, and the figures have 1, 4, 7 and 10 small triangles, so the "
                                           "next figure has 30. The numbers go up by 9 each time.")],
          misconceptions=["M_ACUTE_SMALL_DRAWING", "M_RIGHT_UPRIGHT"])]))

# ============================== T9 Degrees (2.9) =============================================================
TOPICS.append(TOPIC(
    "T9", "M3", "Degrees: Measuring a Turn", ["2.9"], "Understand",
    "Students say that one full turn is 360 degrees, name the degree measures of a half turn and a quarter turn, "
    "and find the angle when a circle is cut into equal parts.",
    "A circle is divided into 360 equal angles of 1 degree, so a full turn is 360°, a straight angle is 180° and a "
    "right angle is 90°.",
    [A("T9.C1", "Degrees: 360, 180 and 90", "Understand",
       "Students say that the angle measure is the number of 1° unit parts, and give the measure of a full turn, a "
       "straight angle and a right angle.",
       textbook=tb(book("2.9") + book("2.9", H_MEAS)),
       teach=["Predict first: a full turn of a circle is cut into 360 equal angles. What would a straight angle, "
              "which is half a turn, measure?",
              "Each equal part is a unit angle of 1 degree, written 1°. The measure of an angle is the number of "
              "1° parts in it.",
              "A full turn is 360°. A straight angle is half of it, 180°, and a right angle is half of that, 90°."],
       examples=[we("2.9.q1")],
       key_terms=["degree", "measure of an angle"], misconceptions=["M_DEGREE_FULL"], minutes=8),
     A("T9.C2", "Cutting a circle into equal angles", "Apply",
       "Students find the angle at the centre when a circle is cut into 1, 2, 3, 4, 5, 6, 8, 9, 10 or 12 equal "
       "parts, and see why 360 is a handy number.",
       textbook=tb(book("2.9", H_HIST)),
       teach=["Predict first: cut a circle into 4 equal parts. How many degrees is each angle at the centre?",
              "Divide 360 by the number of parts: 360 ÷ 4 = 90, so each is 90°.",
              "360 divides evenly by 1, 2, 3, 4, 5, 6, 8, 9, 10 and 12, so it gives whole-number angles for all of "
              "these cuts. That is one reason people kept it."],
       examples=[we("2.9.q2")],
       key_terms=["full turn", "equal parts"], misconceptions=["M_DEGREE_FULL"], minutes=8)]))

# ============================== T10 Reading a protractor (2.9) ===============================================
TOPICS.append(TOPIC(
    "T10", "M3", "Reading a Protractor", ["2.9"], "Apply",
    "Students read an angle on a protractor by counting units, by subtracting two readings, or directly with one "
    "arm on the 0 mark.",
    "Place the centre of the protractor on the vertex and one arm on 0, then read where the other arm crosses the "
    "scale that starts at 0.",
    [A("T10.C1", "Two scales on a protractor", "Understand",
       "Students say why a protractor has two sets of numbers and count 1° units on an unlabelled one.",
       textbook=tb(book("2.9", H_DEG) + book("2.9", H_UNLAB, stop=2) + book("2.9", H_LAB, stop=2)),
       teach=["Predict first: a protractor shows two rows of numbers, one growing left to right and one right to "
              "left. Why have both?",
              "The marks are 1° units, with a long mark every 10° and a medium one every 5°. You can count in "
              "5s and 10s instead of ones.",
              "The two scales let you start from 0 on whichever arm is the base arm, left or right."],
       examples=[we("2.9.q3")],
       key_terms=["protractor", "scale"], misconceptions=["M_WRONG_SCALE", "M_START_AT_ONE"], minutes=8),
     A("T10.C2", "Naming angles and reading them by subtracting", "Apply",
       "Students name every angle at a vertex with its measure, and find an angle between two arms by "
       "subtracting their two readings.",
       textbook=tb(book("2.9", H_LAB, start=2, stop=9)),
       teach=["Predict first: five rays from one point O make many angles together. How many different angles "
              "can you name, and how will you find each?",
              "List every pair of rays, name the angle, and read each ray on the scale. ∠TOQ and ∠QOT are the "
              "same angle.",
              "Without counting marks: if OT and OS pass the 20 and 55 marks, the angle is 55 − 20 = 35 degrees. "
              "Subtract the two readings."],
       examples=[we("2.9.q4"), we("2.9.q5"), we("2.9.q6")],
       key_terms=["subtraction", "angle measure"], misconceptions=["M_WRONG_SCALE"], minutes=10),
     A("T10.C3", "Measuring directly: one arm on 0", "Apply",
       "Students place the protractor centre on the vertex, set one arm on the 0 mark, and read the other arm "
       "directly.",
       textbook=tb(book("2.9", H_DIRECT, stop=4)),
       teach=["Predict first: can we measure an angle in one reading, without subtracting?",
              "Put the centre of the protractor on the vertex. Turn it so one arm passes through the 0 mark.",
              "Read the number where the other arm crosses the scale that starts at 0 on that arm. Here the arm "
              "OA passes the 80, so ∠AOB is 80°."],
       examples=[we("2.9.q7")],
       key_terms=["protractor", "0 mark"], misconceptions=["M_PROTRACTOR_ANYWHERE", "M_WRONG_SCALE"], minutes=8),
     DOER("T10.C4", "Pull it together and do it: Count the Degrees", None, "Apply",
          "Students count the 1° units between two arms on an unlabelled protractor, using 5s and 10s.",
          ["The vertex goes on the centre of the protractor.",
           "Count in tens and fives, then ones.",
           "The measure is the number of 1° units between the arms."],
          items=[fio("2.9.FiO1.Q1")],
          misconceptions=["M_START_AT_ONE"])]))

# ============================== T11 Paper protractor (2.9) ===================================================
TOPICS.append(TOPIC(
    "T11", "M3", "Make Your Own Protractor", ["2.9"], "Apply",
    "Students fold a paper semicircle into halves again and again to get 90°, 45° and 22.5°, and call each fold "
    "an angle bisector.",
    "Each fold halves the angle, so a folded paper semicircle gets its marks at 180°, 90°, 45° and 22.5°.",
    [A("T11.C1", "Half a circle and a quarter: 180° and 90°", "Apply",
       "Students fold a circle into a semicircle and a quarter circle and work out 180° and 90° from the full "
       "turn.",
       textbook=tb(book("2.9", H_OWN, stop=6)),
       teach=["Predict first: you fold a paper circle in half. Which angle does the half circle show at its "
              "centre?",
              "A full turn is 360°, so half a turn is half of 360° and measures 180°.",
              "Fold the semicircle in half to get a quarter circle. A quarter of 360° is 90°, and half of 180° is "
              "also 90°, so write 90° at the top."],
       examples=[we("2.9.act1"), we("2.9.q8"), we("2.9.q9")],
       key_terms=["paper protractor", "semicircle"], misconceptions=["M_DEGREE_FULL"], minutes=10),
     A("T11.C2", "Halving again: 45° and 22.5°", "Apply",
       "Students fold again to get 45° and 22.5°, and say why all eight equal angles on the straight angle are "
       "22.5° each.",
       textbook=tb(book("2.9", H_OWN, start=6, stop=11)),
       teach=["Predict first: fold the quarter circle in half. What does the new angle measure?",
              "Half of 90° is 45°, and 180° less 45° is 135°. Fold again and half of 45° is 22.5°.",
              "The 180° straight angle is cut into 8 equal angles, so each is 180 ÷ 8 = 22.5°."],
       examples=[we("2.9.q10"), we("2.9.q11"), we("2.9.q12")],
       key_terms=["half", "22.5°"], misconceptions=["M_BISECT_ANY_PART"], minutes=10),
     A("T11.C3", "The angle bisector", "Understand",
       "Students name a fold that halves an angle as an angle bisector, and find the angle bisectors in the folded "
       "paper semicircle.",
       textbook=tb(book("2.9", H_BIS)),
       teach=["Predict first: each fold gave half of an angle. What could we call the crease?",
              "The process of getting half of a given angle is bisecting it, and the line that does it is the "
              "angle bisector.",
              "In the paper protractor OE bisects the straight angle into 90° and 90°, and OC bisects the angle "
              "of 90° into 45° and 45°."],
       examples=[we("2.9.try1")],
       key_terms=["angle bisector", "bisect"], misconceptions=["M_BISECT_ANY_PART"], minutes=8),
     DOER("T11.C4", "Pull it together and do it: Paper Protractor", "paper_protractor", "Apply",
          "Students fold a paper semicircle on the tool and place the marks 0°, 22.5°, 45°, 67.5°, 90°, 112.5°, "
          "135°, 157.5° and 180°.",
          ["Each fold halves the angle.",
           "The marks are 22.5° apart.",
           "A bisector halves an angle into two equal angles."],
          items=[],
          misconceptions=["M_BISECT_ANY_PART"])]))


# T6 and T9 close with a short recap-only doer (no tool, no exercises of their own)
assert TOPICS[0]["key"] == "T6" and TOPICS[3]["key"] == "T9"
TOPICS[0]["concepts"].append(DOER(
    "T6.C3", "Practice: Rotating Arms", None, "Apply",
    "Students explain that the size of an angle is the turn between the arms and use a rotating arm to match an "
    "angle, whatever the length of the arms.",
    ["A rotating arm has a vertex and two arms that open and close.",
     "Two angles are equal when the arms of one lie exactly on the arms of the other.",
     "Cutting the arms shorter does not change the angle."],
    items=[], misconceptions=["M_ARM_LENGTH"]))
TOPICS[3]["concepts"].append(DOER(
    "T9.C3", "Practice: Degrees", None, "Understand",
    "Students state that a full turn is 360 degrees, a straight angle is 180 degrees and a right angle is 90 "
    "degrees, and find the angle for equal cuts of a circle.",
    ["One degree is one of the 360 equal parts of a full turn.",
     "A straight angle is 180 degrees and a right angle is 90 degrees.",
     "Divide 360 by the number of equal parts to get each angle."],
    items=[], misconceptions=["M_DEGREE_FULL"]))
