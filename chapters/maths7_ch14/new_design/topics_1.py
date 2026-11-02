# -*- coding: utf-8 -*-
"""Topics T1 to T4 (module M1: the perpendicular bisector and a right angle at a point). Book section 6.1, opening."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Introduction ==============================================================
TOPICS.append(TOPIC(
    "T1", "M1", "Drawing Eyes with a Compass", ["Chapter opening", "6.1"], "Understand",
    "",
    "Two eyes drawn with arcs, and an open question: where exactly must the compass point go so that the upper and "
    "lower arcs meet at the corners and look the same?",
    [A("T1.C1", "Two arcs make an eye", "Remember",
       "",
       textbook=["6 Constructions and Tilings", "6.1 Geometric Constructions", "Eyes",
                 "Do you recall the 'Eyes' construction we did in Grade 6?",
                 "Of course, eyes can be drawn freehand, but we wanted to construct them so that the lower arc and "
                 "upper arc of each eye look symmetrical. We relied on our spatial estimation to determine the two "
                 "centres, A and B (see the figure), from which we drew the lower arc and upper arc respectively.",
                 "The arcs define a line XY that 'supports' the drawing though it is not part of the final figure. "
                 "We can start with this supporting line and systematically find the centres A and B."],
       teach=["Picture an eye drawn with a compass: an upper arc and a lower arc that meet at two corners, X and Y.",
              "Make a guess before the next step: where must the compass point be placed for each arc, so that "
              "both arcs pass through X and Y and the eye looks the same above and below?"],
       ncert=["opening.eyes"], key_terms=["arc", "centre"], video_focus=["HOOK"], minutes=4, enrichment=True),
     A("T1.C2", "The question to keep: where are the two centres?", "Understand", "",
       teach=["Predict: if the upper arc is drawn from a centre below XY, how far must that centre be from X, and "
              "from Y?",
              "Each arc passes through both corners, so its centre is the same distance from X as from Y.",
              "Keep this question in mind: the next topic finds the two centres exactly and names the line through "
              "them."],
       enrichment=True)],
    topic_type="framing"))

# ============================== T2 Eyes and the perpendicular bisector =========================================
TOPICS.append(TOPIC(
    "T2", "M1", "Eyes and the Perpendicular Bisector", ["6.1"], "Analyze",
    "Students find the two centres of an eye's arcs as points equally far from X and Y, prove with SSS and then SAS "
    "that the line through them is the perpendicular bisector of XY, and explain why every point equally far from X "
    "and Y lies on that line.",
    "Points equally far from X and Y lie on one line, the perpendicular bisector of XY, and congruent triangles prove it.",
    [A("T2.C1", "Finding the centres A and B", "Apply",
       "Students locate the centres A and B of the eye's arcs by drawing equal-radius arcs from X and Y above and "
       "below XY, and explain why AX = AY = BX = BY makes the eye symmetrical.",
       textbook=["For the eye to be symmetrical, or for the supporting line to be the line of symmetry, the upper and "
                 "lower arcs should have the same radius. In other words, we must have AX = BX. Since AX = AY and "
                 "BX = BY, this means AX = AY = BX = BY.",
                 "How do we find such A and B?",
                 "From X and Y, draw arcs above and below XY, with the same radii. The two points at which the arcs "
                 "meet, above and below XY, give us A and B, respectively.",
                 "Use this to construct an eye.",
                 "Join A and B with a line. Where does AB intersect XY, and what is the angle formed between them?",
                 "We observe that AB passes through the midpoint of XY, and is also perpendicular to it.",
                 "A division of a line, or any geometrical object, into two identical parts is called bisection. A "
                 "line that bisects a given line and is perpendicular to it, is called the perpendicular bisector."],
       teach=["Predict first: if an arc is centred at A and passes through X and Y, what must be true of AX and AY?",
              "Arcs of one radius from X and from Y meet at a point A above XY and at a point B below XY; then "
              "AX = AY = BX = BY.",
              "With A as centre draw the lower arc through X and Y; with B as centre draw the upper arc. The eye is "
              "symmetrical about XY.",
              "Join A and B: the line AB passes through the midpoint of XY and makes a right angle with it. Such a "
              "line is called the perpendicular bisector of XY."],
       examples=[
           WE("XY is a line segment. Using only a ruler and a compass, find the centres A and B for the two arcs of "
              "an eye with corners X and Y, and draw the eye.",
              ["Open the compass to a radius more than half of XY.",
               "With centre X, draw an arc above XY and an arc below XY.",
               "With centre Y and the same radius, draw arcs that cut the first two arcs.",
               "Name the meeting point above XY as A and the one below XY as B. Then AX = AY = BX = BY.",
               "With centre A and radius AX, draw the lower arc from X to Y.",
               "With centre B and the same radius, draw the upper arc from X to Y. The two arcs make the eye."],
              "A and B are the meeting points of equal arcs from X and Y; the arc centred at A is the lower arc and "
              "the arc centred at B is the upper arc",
              ncert=["6.1.eye_centres"])],
       key_terms=["bisection", "perpendicular bisector"], misconceptions=["M_RADIUS_SMALL"], minutes=10),
     A("T2.C2", "Why AB is the perpendicular bisector", "Analyze",
       "Students prove that AB is the perpendicular bisector of XY by showing ΔABX ≅ ΔABY by SSS, then "
       "ΔAOX ≅ ΔAOY by SAS, and using the straight angle at O to get two 90° angles.",
       textbook=["Will the line joining the two points at which the arcs meet, above and below XY, always be the "
                 "perpendicular bisector of XY, i.e., when XY is of any length, and the arcs are drawn using a "
                 "radius of any length?",
                 "This can be answered through congruence. Let us consider a line segment XY. Find points A and B "
                 "such that AX = AY = BX = BY. Draw the lines AB, AX, AY, BX and BY. Let O be the point of "
                 "intersection between AB and XY.",
                 "Which two triangles should be congruent for AB to be the perpendicular bisector of XY (that is, O "
                 "is the midpoint of XY and AB is perpendicular to XY)?",
                 "If we show that ΔAOX ≅ ΔAOY, then OX = OY, and ∠AOX = ∠AOY because they are corresponding parts "
                 "of congruent triangles. Since ∠AOX and ∠AOY together form a straight angle, we have "
                 "∠AOX + ∠AOY = 180°. Thus, ∠AOX = ∠AOY = 90°. This establishes that O is the midpoint of XY and AB "
                 "is perpendicular to XY.",
                 "In ΔAOX and ΔAOY, we already know that AX = AY, and AO is common to both triangles.",
                 "If we can show that ∠XAO = ∠YAO then, by the SAS congruence condition, we can conclude that the "
                 "triangles are congruent.",
                 "To show this, we observe that ΔABX ≅ ΔABY. This is so because AX = AY, BX = BY, and AB is common "
                 "to both the triangles.",
                 "Thus, we have ∠XAB = ∠YAB, or ∠XAO = ∠YAO because they are corresponding parts of congruent "
                 "triangles.",
                 "Hence, AB is the perpendicular bisector of XY."],
       teach=["Predict first: which pair of triangles, if congruent, would give OX = OY and a right angle at O?",
              "Step one: ΔABX ≅ ΔABY by SSS, since AX = AY, BX = BY and AB is common. So ∠XAO = ∠YAO.",
              "Step two: ΔAOX ≅ ΔAOY by SAS, since AX = AY, ∠XAO = ∠YAO and AO is common. So OX = OY and "
              "∠AOX = ∠AOY.",
              "The two angles at O make a straight angle of 180°, so each is 90°."],
       examples=[
           WE("Points A and B satisfy AX = AY = BX = BY, and AB meets XY at O. Prove that O is the midpoint of XY and "
              "that AB is perpendicular to XY.",
              ["In ΔABX and ΔABY: AX = AY, BX = BY, and AB is common. So ΔABX ≅ ΔABY by the SSS condition.",
               "Corresponding parts are equal, so ∠XAB = ∠YAB, that is, ∠XAO = ∠YAO.",
               "In ΔAOX and ΔAOY: AX = AY, ∠XAO = ∠YAO, and AO is common. So ΔAOX ≅ ΔAOY by the SAS condition.",
               "Corresponding parts are equal, so OX = OY: O is the midpoint of XY.",
               "Also ∠AOX = ∠AOY, and together they make a straight angle of 180°.",
               "So each of ∠AOX and ∠AOY is half of 180°, which is 90°."],
              "ΔABX ≅ ΔABY by SSS, then ΔAOX ≅ ΔAOY by SAS; so OX = OY and ∠AOX = ∠AOY = 90°: AB is the "
              "perpendicular bisector of XY",
              ncert=["6.1.why_bisector"])],
       key_terms=["congruent", "SSS", "SAS"], misconceptions=["M_CONGRUENCE_GUESS", "M_MIDPOINT_ONLY"], minutes=12),
     A("T2.C3", "Every point equally far from X and Y lies on AB", "Analyze",
       "Students explain why other centres C and D with CX = CY = DX = DY lie on the line AB, and justify that any "
       "point equally far from X and Y lies on the perpendicular bisector of XY.",
       textbook=["We can have eyes of different shapes. How do we get these different shapes? Try!",
                 "One way is to choose two other points C and D such that CX = CY = DX = DY. An eye of a different "
                 "shape can be drawn using these points.",
                 "Will C and D lie on the perpendicular bisector AB?",
                 "The points C and D are at the same distance from both X and Y. We have just seen that joining any "
                 "two such points gives the perpendicular bisector of XY. Since XY has only one perpendicular "
                 "bisector, which is the line AB, the points C and D must lie on the line AB.",
                 "Justify the following statement using the facts that we have established. Any point that has the "
                 "same distance from X and Y lies on the perpendicular bisector of XY.",
                 "Thus, eyes of different shapes can be drawn by suitably choosing different pairs of points on the "
                 "perpendicular bisector as centres to construct the upper and lower arcs of the eyes."],
       teach=["Predict first: a new point C has CX = CY. Will it lie on the line AB, or somewhere else?",
              "Pair C with A, or with B on the other side: the line through two points that are each equally far "
              "from X and Y is the perpendicular bisector of XY, by the same SSS then SAS proof.",
              "XY has only one perpendicular bisector, so that line is AB, and C is on it.",
              "Different pairs of centres on AB give eyes of different shapes."],
       examples=[
           WE("A point P is the same distance from X and Y, that is, PX = PY. Justify that P lies on the "
              "perpendicular bisector AB of XY.",
              ["If P is on the same side of XY as A, pair P with B; otherwise pair P with A. Say we pair P with B.",
               "Then PX = PY and BX = BY, so P and B are each equally far from X and Y.",
               "In ΔPBX and ΔPBY: PX = PY, BX = BY, and PB is common, so ΔPBX ≅ ΔPBY by SSS.",
               "So ∠XPB = ∠YPB, and if PB meets XY at O, then ΔPOX ≅ ΔPOY by SAS (PX = PY, equal angles at P, PO "
               "common). So OX = OY and the angles at O are 90°.",
               "So the line PB is the perpendicular bisector of XY.",
               "XY has only one perpendicular bisector, the line AB, so P lies on AB."],
              "The line through P and B is the perpendicular bisector of XY (SSS, then SAS); XY has only one "
              "perpendicular bisector, so P lies on AB",
              ncert=["6.1.equidistant"])],
       key_terms=["equidistant", "perpendicular bisector"], misconceptions=["M_EQUIDISTANT_OFF"], minutes=10),
     DOER("T2.C4", "Practice: find points equally far from X and Y", "pb_locus", "Analyze",
          "Students place points that are equally far from X and Y, see that they all fall on one line, and name "
          "the congruence conditions that prove the line is the perpendicular bisector.",
          ["Arcs of the same radius from X and from Y meet at points equally far from X and Y.",
           "The line through two such points cuts XY in half at a right angle: SSS, then SAS.",
           "Every point equally far from X and Y lies on this one line."])]))

# ============================== T3 Constructing the perpendicular bisector =====================================
TOPICS.append(TOPIC(
    "T3", "M1", "Constructing the Perpendicular Bisector", ["6.1"], "Apply",
    "Students construct the perpendicular bisector of a segment with an unmarked ruler and a compass, use it to "
    "find a midpoint exactly, and test which radius choices are necessary and which are free.",
    "Two points each equally far from X and Y fix the perpendicular bisector; ruler and compass draw it exactly.",
    [A("T3.C1", "Steps to construct the perpendicular bisector", "Apply",
       "Students construct the perpendicular bisector of a given segment XY in three steps with an unmarked ruler "
       "and a compass, and use it to mark the midpoint of XY.",
       textbook=["Construction of Perpendicular Bisector",
                 "Given a line segment XY, how do we draw its perpendicular bisector using only an unmarked ruler and "
                 "a compass?",
                 "We have seen that joining any two points, one above XY and one below, that are at equal distances "
                 "from X and Y, gives the perpendicular bisector of XY. This gives a method to construct the "
                 "perpendicular bisector.",
                 "1. Taking some fixed radius, from X and then Y, construct two sufficiently long arcs above XY. Name "
                 "the point where the arcs meet as A.",
                 "2. Using the same radius, from X and then Y, construct two sufficiently long arcs below XY. Name "
                 "the point where the arcs meet as B.",
                 "3. AB is the required perpendicular bisector.",
                 "Thus, the perpendicular bisector can be constructed using the simplest geometric tools, an "
                 "unmarked ruler and a compass. We will use only these two tools for all the other geometric "
                 "constructions in this chapter, unless there is a need for drawing lines of specific lengths in "
                 "standard units.",
                 "This method of constructing the perpendicular bisector is not only geometrically exact but also a "
                 "practical way to construct it accurately.",
                 "This method to find the midpoint of a line segment is more accurate than measuring the length "
                 "using a marked scale."],
       teach=["Predict first: what is the smallest radius that still lets the arcs from X and Y meet?",
              "Step 1: with a radius more than half of XY, draw arcs from X and from Y above XY; they meet at A.",
              "Step 2: with the same radius, draw arcs from X and from Y below XY; they meet at B.",
              "Step 3: join A and B with the ruler. AB is the perpendicular bisector, and it meets XY at the "
              "midpoint O."],
       examples=[
           WE("Draw a line segment XY. Construct its perpendicular bisector using only an unmarked ruler and a "
              "compass, and mark the midpoint of XY.",
              ["Open the compass to a radius more than half of XY, so that the arcs will meet.",
               "With centre X, draw a long arc above XY. With centre Y and the same radius, draw an arc above XY "
               "that cuts it. Name the meeting point A.",
               "Keep the same radius. With centres X and Y, draw two arcs below XY that cut each other at B.",
               "Join A and B with the ruler. AB is the perpendicular bisector of XY.",
               "Mark O where AB crosses XY. O is the midpoint of XY, and ∠AOX = 90°.",
               "Reason: AX = AY and BX = BY, so ΔABX ≅ ΔABY by SSS and then ΔAOX ≅ ΔAOY by SAS."],
              "AB, the line through the two meeting points of equal arcs, is the perpendicular bisector; it meets "
              "XY at its midpoint O",
              ncert=["6.1.pb_steps"])],
       key_terms=["perpendicular bisector", "midpoint"], misconceptions=["M_RADIUS_SMALL"], minutes=10),
     DOER("T3.C2", "Practice: construct perpendicular bisectors", "pb_radius_bench", "Apply",
          "Students construct the perpendicular bisector of segments of different lengths, test which radius choices "
          "still work, and justify each choice with congruent triangles.",
          ["Use a radius more than half of the segment so that the arcs meet.",
           "Within one pair of arcs, the radius must be the same; different pairs may use different radii.",
           "Any two points each equally far from X and Y fix the perpendicular bisector."],
          items=[
              FIO("6.1.FiO_pb1", "Figure it Out (perpendicular bisector), Q1",
                  "When constructing the perpendicular bisector, is it necessary to have the same radius for the arcs "
                  "above and below XY? Explore this through construction, and then justify your answer. [Hint 1: Any "
                  "point that is of the same distance from X and Y lies on the perpendicular bisector. Hint 2: We can "
                  "draw the whole line if any two of its points are known.]",
                  ["Construct: arcs of radius r from X and Y above XY meet at A, so AX = AY.",
                   "Arcs of a different radius s from X and Y below XY meet at B, so BX = BY.",
                   "A is equally far from X and Y, so A lies on the perpendicular bisector. B is equally far from X "
                   "and Y, so B lies on it too.",
                   "Why: ΔABX ≅ ΔABY by SSS (AX = AY, BX = BY, AB common), so ∠XAO = ∠YAO; then ΔAOX ≅ ΔAOY by SAS "
                   "(AX = AY, equal angles at A, AO common), so OX = OY and ∠AOX = ∠AOY = 90°.",
                   "Two points fix a whole line, so AB is the perpendicular bisector."],
                  "No. The radius above may differ from the radius below; A and B are each equally far from X and Y, "
                  "so both lie on the perpendicular bisector (SSS, then SAS), and two points fix the line",
                  tool="pb_radius_bench"),
              FIO("6.1.FiO_pb2", "Figure it Out (perpendicular bisector), Q2",
                  "Is it necessary to construct the pairs of arcs above and below XY? Instead, can we construct both "
                  "the pairs of arcs on the same side of XY? Explore this through construction, and then justify "
                  "your answer.",
                  ["Construct: arcs of radius r from X and Y above XY meet at A.",
                   "Arcs of a larger radius s from X and Y, also above XY, meet at a second point P. The radii must "
                   "differ, or the arcs meet at A again.",
                   "AX = AY and PX = PY, so A and P are each equally far from X and Y.",
                   "Why: by SSS, ΔAPX ≅ ΔAPY (AX = AY, PX = PY, AP common), so line AP makes equal angles with AX and "
                   "AY; then SAS on the triangles at the meeting point O gives OX = OY and two 90° angles.",
                   "So the line AP, extended to cross XY, is the perpendicular bisector."],
                  "No. Both pairs can be on the same side if the two radii are different; each meeting point is "
                  "equally far from X and Y, so both lie on the perpendicular bisector (SSS, then SAS), and the line "
                  "through them, extended, is the perpendicular bisector",
                  tool="pb_radius_bench"),
              FIO("6.1.FiO_pb3", "Figure it Out (perpendicular bisector), Q3",
                  "While constructing one pair of intersecting arcs, is it necessary that we use the same radii for "
                  "both of them? Explore this through construction, and then justify your answer.",
                  ["Construct: an arc of radius r from X and an arc of a different radius s from Y meet at a point P.",
                   "Then PX = r and PY = s, so PX ≠ PY.",
                   "Every point on the perpendicular bisector is equally far from X and Y: if Q is on it and QO meets "
                   "XY at O, then ΔQOX ≅ ΔQOY by SAS (OX = OY, ∠QOX = ∠QOY = 90°, QO common), so QX = QY.",
                   "P is not equally far from X and Y, so P is not on the perpendicular bisector.",
                   "So a line through P is not the perpendicular bisector."],
                  "Yes. Within one pair the two arcs must have the same radius; otherwise the meeting point is not "
                  "equally far from X and Y, and every point of the perpendicular bisector is (SAS), so it would not "
                  "lie on the perpendicular bisector",
                  tool="pb_radius_bench"),
          ])]))

# ============================== T4 90 degrees at a point =====================================================
TOPICS.append(TOPIC(
    "T4", "M1", "A Right Angle at a Point on a Line", ["6.1"], "Apply",
    "Students construct a 90° angle at a given point O on a line by marking a segment with O as its midpoint and "
    "drawing one pair of equal arcs, and explain why one pair is enough.",
    "Mark X and Y equally far from O; one point equally far from X and Y, joined to O, gives the right angle.",
    [A("T4.C1", "Construct a 90° angle at a given point", "Apply",
       "Students construct a 90° angle at a point O on a line by marking X and Y equally far from O and drawing "
       "one pair of equal arcs, and justify the right angle with SSS.",
       textbook=["Construction of a 90° Angle at a Given Point",
                 "Can we extend the method of constructing the perpendicular bisector to construct a 90° angle at "
                 "any point on a line? Draw a line and mark a point O on it. Construct a 90° angle at point O.",
                 "Find a segment of this line for which O is the midpoint.",
                 "Extend the line on either side of O. Using a compass, mark two points X and Y at equal distance "
                 "from O, so that O is the midpoint of XY.",
                 "The perpendicular bisector of XY will pass through O and is perpendicular to the given line.",
                 "In this case, do we need to draw two pairs of intersecting arcs to get the perpendicular bisector "
                 "of XY?",
                 "No, we don't. We already have one point, O, lying on the perpendicular bisector."],
       teach=["Predict first: we already know one point of the perpendicular bisector. How many more points do we "
              "need?",
              "With centre O, cut the line at X and Y, so that OX = OY and O is the midpoint of XY.",
              "With a larger radius, draw arcs from X and Y on one side; they meet at A. Then AX = AY.",
              "Join OA. ΔAOX ≅ ΔAOY by SSS, so ∠AOX = ∠AOY, and they make 180°, so each is 90°."],
       examples=[
           WE("Draw a line and mark a point O on it. Construct a 90° angle at O using only a ruler and a compass, "
              "and say why the angle is 90°.",
              ["With centre O and any radius, draw arcs that cut the line at X and at Y. Then OX = OY.",
               "Open the compass wider than OX. With centre X, draw an arc above the line.",
               "With centre Y and the same radius, draw an arc that cuts it at A. Then AX = AY.",
               "Join O and A. ∠AOX is the required 90° angle.",
               "Reason: in ΔAOX and ΔAOY, AX = AY, OX = OY, and AO is common, so ΔAOX ≅ ΔAOY by SSS.",
               "So ∠AOX = ∠AOY. Together they make 180°, so each is 90°."],
              "∠AOX = 90°, since ΔAOX ≅ ΔAOY by SSS and the two equal angles make a straight angle",
              ncert=["6.1.right_angle"])],
       key_terms=["perpendicular", "right angle"], misconceptions=["M_SAME_RADIUS_ALL"], minutes=10),
     DOER("T4.C2", "Practice: right angles at points on a line", None, "Apply",
          "Students construct 90° angles at given points on lines in different positions, including a point near "
          "one end, and give the SSS reason each time.",
          ["Make O the midpoint of a segment XY with one compass setting.",
           "One pair of equal arcs from X and Y gives a second point of the perpendicular bisector.",
           "Join it to O: ΔAOX ≅ ΔAOY by SSS, so the angle at O is 90°."])]))
