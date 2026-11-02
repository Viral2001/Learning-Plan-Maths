# -*- coding: utf-8 -*-
"""Topics T12 to T16 (module M3 end, module M4): using the protractor well, angles around us, drawing angles,
types of angles by degrees, summary. Book sections 2.9 (second half), 2.10, 2.11 and the Summary."""
from topics_common import A, DOER, TOPIC, WE as _WE, BOOK_TEXT, _clean, book, fio, tb, we


def WE(q, steps, answer, ncert=()):
    return _WE(_clean(q), _clean(steps), _clean(answer), ncert=ncert)

TOPICS = []
H_MIND = "Mind the Mistake, Mend the Mistake!"
H_G1 = "Let's Play a Game #1"
H_G2 = "Let's Play a Game #2"
H_LET = "Let's Explore"

# ============================== T12 Using the protractor well (2.9) ==========================================
TOPICS.append(TOPIC(
    "T12", "M3", "Using a Protractor Well", ["2.9"], "Apply",
    "Students measure angles of different sizes and directions, find the mistake in a wrong reading, and judge "
    "when a measure is sensible.",
    "Put the centre on the vertex, one arm on 0, and read the scale that starts at 0 on that arm; the answer "
    "must fit what the angle looks like.",
    [A("T12.C1", "Mind the mistake, mend the mistake", "Evaluate",
       "Students find what went wrong in a student's protractor reading, say which check was missed, and mend the reading.",
       textbook=tb(book("2.9", H_MIND)),
       teach=["Predict first: a student measured four angles with a protractor and got some wrong. What do you "
              "check first on each picture?",
              "Check three things: the centre is on the vertex, one arm is on the 0 mark, and the scale being "
              "read starts at 0 on that arm.",
              "An acute angle cannot read more than 90. If it does, the other scale was read, so mend it by "
              "reading the scale that starts at 0."],
       examples=[we("2.9.MtM")],
       key_terms=["protractor", "reading"], misconceptions=["M_PROTRACTOR_ANYWHERE", "M_WRONG_SCALE"],
       minutes=8),
     DOER("T12.C2", "Pull it together and do it: Measure with the Protractor", "protractor_reader", "Apply",
          "Students place the protractor on angles of different sizes and directions and read each one, find the "
          "angles in a classroom, and check that the three angles of a triangle add to 180°.",
          ["The centre of the protractor goes on the vertex.",
           "One arm goes on 0, and you read the scale that starts at 0 on that arm.",
           "Check the answer against how the angle looks: acute is under 90 and obtuse is over 90."],
          items=[fio("2.9.FiO2.Q1"), fio("2.9.FiO2.Q2"), fio("2.9.FiO2.Q3"), fio("2.9.FiO2.Q4"),
                 fio("2.9.FiO2.Q5"), fio("2.9.FiO2.Q6"), fio("2.9.FiO2.Q7"), fio("2.9.FiO2.Q8"),
                 fio("2.9.FiO2.Q9")],
          misconceptions=["M_PROTRACTOR_ANYWHERE", "M_WRONG_SCALE", "M_REFLEX_NOT_MEASURABLE"])]))

# ============================== T13 Angles around us (2.9) ===================================================
TOPICS.append(TOPIC(
    "T13", "M3", "Angles Around Us", ["2.9"], "Apply",
    "Students describe turns in clocks, doors, swings and toys as angle measures in degrees.",
    "A clock face is a full turn of 360°, so each hour is 30°; doors, swings and rotated pictures also turn "
    "through angles.",
    [A("T13.C1", "The clock as a full turn", "Apply",
       "Students find the angle between the clock hands at an hour by splitting 360° into 12 equal parts.",
       textbook=tb(book("2.9", "Figure it Out: Where are the angles?", stop=2)),
       teach=["Predict first: the hands of a clock make an angle at 5 o'clock. How many degrees is it?",
              "The 12 hours cut the full turn of 360° into 12 equal parts, so each hour is 360 ÷ 12 = 30°.",
              "At 5 o'clock the hands are 5 hours apart, so the angle is 5 × 30 = 150°."],
       examples=[WE("What is the angle between the hands of a clock at 5 o'clock?",
                    ["A full turn of the clock face is 360 degrees and it has 12 hours, so one hour is "
                     "360 ÷ 12 = 30 degrees.",
                     "At 5 o'clock the hands are 5 hours apart, so the angle is 5 × 30 = 150 degrees."],
                    "150 degrees", ncert=[])],
       key_terms=["clock", "full turn"], misconceptions=["M_DEGREE_FULL"], minutes=8),
     DOER("T13.C2", "Practice: Where Are the Angles", None, "Apply",
          "Students find angles in clocks, a door, a swing, a toy and a rotated picture, and give each as a turn "
          "in degrees.",
          ["A turn can be given as an angle in degrees.",
           "The bigger the swing or the opening, the bigger the angle.",
           "A clock face gives 30° for each hour."],
          items=[fio("2.9.FiO3.Q1"), fio("2.9.FiO3.Q2"), fio("2.9.FiO3.Q3"), fio("2.9.FiO3.Q4"),
                 fio("2.9.FiO3.Q5")],
          misconceptions=["M_DEGREE_FULL", "M_ANGLE_AS_GAP"])]))

# ============================== T14 Drawing angles (2.10) ====================================================
TOPICS.append(TOPIC(
    "T14", "M4", "Drawing Angles", ["2.10"], "Apply",
    "Students draw an angle of a given size with a protractor, and play guessing games that sharpen their "
    "sense of angle size.",
    "To draw an angle, draw one arm, put the protractor centre on the vertex with the arm on 0, mark the "
    "measure, and join.",
    [A("T14.C1", "Drawing a 30° angle", "Apply",
       "Students draw a given angle, such as ∠TIN of 30°, with a protractor, by marking the measure and joining.",
       textbook=tb(book("2.10")),
       teach=["Predict first: you know the measure 30°. Which arm do you draw first, and what do you do next?",
              "Draw a straight arm IN. Put the protractor centre on I with the arm IN on the 0 mark.",
              "Mark a dot at 30 on the scale that starts at 0, remove the protractor, and join I to the dot T. "
              "∠TIN is 30°."],
       examples=[we("2.10.ex1")],
       key_terms=["draw an angle", "protractor"], misconceptions=["M_WRONG_SCALE", "M_START_AT_ONE"], minutes=10),
     A("T14.C2", "Angle guessing games", "Evaluate",
       "Students guess and check angle sizes in two team games, and see how a good estimate comes from remembering "
       "30°, 45°, 60° and 90°.",
       textbook=tb(book("2.10", H_G1) + book("2.10", H_G2)),
       teach=["Predict first: Team 1 draws an angle without showing it. Can Team 2 guess within a few degrees?",
              "Guess, measure with the protractor, and score by how close you were. Closer guesses score more.",
              "Keep the benchmark angles in mind: a right angle is 90°, half of it is 45°, and a straight angle "
              "is 180°. Guessing is practice for the eye, and the protractor gives the exact number."],
       examples=[we("2.10.act1"), we("2.10.act2")],
       key_terms=["estimate", "guess"], misconceptions=["M_ESTIMATE_POINTLESS", "M_COMPARE_EYE"], minutes=8),
     DOER("T14.C3", "Pull it together and do it: Draw the Angle", "angle_drawer", "Apply",
          "Students list every angle in a figure, draw angles of given sizes, and copy an angle by measuring "
          "it.",
          ["Draw one arm first, then put the centre and the 0 mark on it.",
           "Mark the measure on the scale that starts at 0.",
           "Check the finished angle by measuring it again."],
          items=[fio("2.10.FiO.Q1"), fio("2.10.FiO.Q2"), fio("2.10.FiO.Q3")],
          misconceptions=["M_WRONG_SCALE", "M_ANGLE_P"])]))

# ============================== T15 Types of angles by degrees (2.11) ========================================
TOPICS.append(TOPIC(
    "T15", "M4", "Types of Angles by Their Measure", ["2.11"], "Apply",
    "Students sort any angle by its measure as acute, right, obtuse, straight or reflex, and find the measure "
    "of a reflex angle from the rest of the turn.",
    "Under 90° is acute, 90° is right, between 90° and 180° is obtuse, 180° is straight, and between 180° and "
    "360° is reflex.",
    [A("T15.C1", "Naming an angle from its degrees", "Understand",
       "Students name an angle as acute, right, obtuse or straight by comparing its measure with 90 and 180.",
       textbook=tb(book("2.11", stop=3)),
       teach=["Predict first: an angle measures 120°. Is it acute, right or obtuse?",
              "Compare the measure with 90° and 180°. Less than 90° is acute, exactly 90° is right, and more "
              "than 90° and less than 180° is obtuse.",
              "90° is right and not obtuse, and 180° is a straight angle."],
       examples=[WE("Name each angle as acute, right, obtuse or straight: 35°, 90°, 120°, 180°.",
                    ["35° is less than 90°, so it is acute.",
                     "90° is exactly a quarter turn, so it is a right angle.",
                     "120° is more than 90° and less than 180°, so it is obtuse.",
                     "180° is a half turn, so it is a straight angle."],
                    "35° is acute, 90° is right, 120° is obtuse and 180° is straight.", ncert=[])],
       key_terms=["acute", "right", "obtuse", "straight"], misconceptions=["M_90_OBTUSE"], minutes=8),
     A("T15.C2", "The reflex angle", "Understand",
       "Students say that an angle bigger than a straight angle and less than a full turn is reflex, and find "
       "its measure from the part of the turn that is left.",
       textbook=tb(book("2.11", start=3, stop=5)),
       teach=["Predict first: an angle opens past a straight angle. What do we call it, and how can we measure "
              "it with a protractor that stops at 180°?",
              "An angle of more than 180° and less than 360° is a reflex angle.",
              "Measure the smaller angle on the other side and take it from a full turn. If it is 100°, the "
              "reflex angle is 360 − 100 = 260°."],
       examples=[WE("The smaller angle at a vertex is 100°. What is the reflex angle on the other side?",
                    ["The two angles together make a full turn of 360 degrees.",
                     "The reflex angle is 360 − 100 = 260 degrees."],
                    "260 degrees", ncert=[])],
       key_terms=["reflex angle"], misconceptions=["M_REFLEX_NOT_MEASURABLE"], minutes=8),
     A("T15.C3", "Angles that add up to a straight angle", "Apply",
       "Students use the 180° straight angle to find an unknown neighbouring angle by subtracting the given one.",
       textbook=tb(book("2.11", H_LET)),
       teach=["Predict first: ∠TER is 80° and the line BER is straight. What is ∠BET?",
              "A straight angle is 180°, and the two angles make it up together.",
              "Subtract: 180 − 80 = 100°. So ∠BET is 100°, which is obtuse."],
       examples=[we("2.11.q1")],
       key_terms=["straight angle", "neighbouring angles"], misconceptions=["M_STRAIGHT_NOT_ANGLE"], minutes=8),
     DOER("T15.C4", "Pull it together and do it: Sort the Angle", "angle_classifier", "Apply",
          "Students measure or estimate angles, classify each, draw angles of given sizes and build figures and "
          "letters from angle clues.",
          ["Acute is under 90°, right is 90°, obtuse is between 90° and 180°.",
           "Straight is 180° and reflex is between 180° and 360°.",
           "Estimate first, then measure, and use 360° for a full turn."],
          items=[fio("2.11.FiO1.Q1"), fio("2.11.FiO1.Q2"), fio("2.11.FiO2.Q1"), fio("2.11.FiO2.Q2"),
                 fio("2.11.FiO2.Q3"), fio("2.11.FiO2.Q4"), fio("2.11.FiO2.Q5"), fio("2.11.FiO2.Q6"),
                 fio("2.11.FiO2.Q7")],
          misconceptions=["M_90_OBTUSE", "M_REFLEX_NOT_MEASURABLE", "M_ESTIMATE_POINTLESS"])]))

# ============================== T16 Summary ==================================================================
TOPICS.append(TOPIC(
    "T16", "M4", "Summary: Lines and Angles", ["Summary"], "Understand",
    "Students recall points, lines, rays, angles, degrees, the protractor and the types of angles.",
    "A point marks a place, a ray and a line go on, an angle is a turn measured in degrees, and angles are named "
    "by their measure.",
    [A("T16.C1", "Lines and angles: the whole chapter", "Understand",
       "Students recall how lines, rays and angles are named, how an angle is measured and drawn, and what each "
       "type of angle is.",
       textbook=tb(book("Summary")),
       teach=["Predict first: a line, a ray and a segment all lie along the same path. How do they differ?",
              "A segment has two ends, a ray has one end, and a line has none. An angle is the turn between two "
              "rays at a vertex, and its measure is in degrees: 90° is a right angle, and 360° is a full turn.",
              "Still open for you: can you draw an angle of 135° and name its type before you measure it?"],
       ncert=["summary"], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
