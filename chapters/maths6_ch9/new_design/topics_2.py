# -*- coding: utf-8 -*-
"""Topics T6 to T9 (module M2: rotational symmetry). Book section 9.2 up to the circle."""
from topics_common import A, DOER, TOPIC, book, fio, we

TOPICS = []
H_ARMS = "Rotational Symmetry of Figures with Radial Arms"
H_FIO1 = "Figure it Out (first block)"
H_CIRCLE = "Symmetries of a circle"

# ============================== T6 Rotational symmetry (9.2) =================================================
TOPICS.append(TOPIC(
    "T6", "M2", "Rotational Symmetry and Angles of Symmetry", ["9.2"], "Understand",
    "Students use a turn about a fixed centre to decide whether a figure looks the same, and list the angles of "
    "symmetry of windmills, squares and strips.",
    "A figure has rotational symmetry when a turn between 0° and 360° about its centre makes it look the same; "
    "360° always works.",
    [A("T6.C1", "The windmill and its centre of rotation", "Understand",
       "Students explain that a windmill with 4 equal blades looks the same after a 90° turn about its centre, "
       "and define the centre of rotation and an angle of symmetry.",
       textbook=book("9.2", stop=9),
       teach=["Predict first: a paper windmill has no line of symmetry. Will it still look the same if you turn "
              "it a quarter turn about the red centre?",
              "It does. A fixed point about which a figure turns is the centre of rotation.",
              "An angle through which a figure turns to look the same is an angle of symmetry. The windmill has "
              "90°, 180°, 270° and 360°, so 4 angles of symmetry.",
              "A turn of less than 90° does not make the windmill look the same."],
       examples=[we("9.1.q1"), we("9.2.q1"), we("9.2.q2")],
       key_terms=["rotational symmetry", "centre of rotation", "angle of symmetry"],
       misconceptions=["M_NO_LINE_NO_SYM", "M_ORDER_DISTINCT"], minutes=12),
     A("T6.C2", "The square: four angles of symmetry", "Apply",
       "Students list the angles of symmetry of a square and mark its centre of rotation at the crossing of the "
       "diagonals.",
       textbook=book("9.2", start=9, stop=12),
       teach=["Predict first: how many angles of symmetry does a square have, and what is the smallest?",
              "A 90° turn takes corner A to B, B to C, C to D and D back to A, so the square lands on itself.",
              "The other angles are 180°, 270° and 360°. The centre of rotation is where the two diagonals cross."],
       examples=[we("9.2.q3"), we("9.2.q4"), we("9.2.q5")],
       key_terms=["angle of symmetry", "centre of rotation"], misconceptions=["M_ORDER_DISTINCT"], minutes=10),
     A("T6.C3", "A figure with no rotational symmetry", "Analyze",
       "Students show by turning that a strip with one short side does not match itself after 180°, so its only "
       "angle of symmetry is 360°.",
       textbook=book("9.2", start=12),
       teach=["Predict first: turn a trapezium strip by 180°. Will it look the same?",
              "After 180° the short side is at the bottom and the long side at the top, so it does not overlap.",
              "Another 180° brings it back, so only a full 360° turn works. A figure whose only angle of symmetry "
              "is 360° does not have rotational symmetry."],
       examples=[we("9.2.ex1"), we("9.2.q6")],
       key_terms=["rotational symmetry"], misconceptions=["M_ORDER_DISTINCT"], minutes=8),
     DOER("T6.C4", "Pull it together and do it: Turn and Match", "rotate_match", "Apply",
          "Students turn a figure about its marked centre on the tool, note each turn at which it matches "
          "itself, and list the angles of symmetry.",
          ["Turn the figure about the marked centre and look for a match with the outline.",
           "Every figure matches itself after 360°, so 360° is always an angle of symmetry.",
           "A figure has rotational symmetry only if some angle below 360° also matches."],
          items=[fio("9.2.FiO1.Q1"), fio("9.2.FiO1.Q2")],
          misconceptions=["M_ORDER_DISTINCT", "M_NO_LINE_NO_SYM"])]))

# ============================== T7 Radial arms (9.2) =========================================================
TOPICS.append(TOPIC(
    "T7", "M2", "Radial Arms: Turning 4, 2 and 3 Ways", ["9.2"], "Apply",
    "Students build figures with radial arms that have exactly 4, 2 or 3 angles of symmetry, and explain why the "
    "angles between arms must be equal.",
    "Equal arms spaced at equal angles of 360 ÷ n give exactly n angles of symmetry.",
    [A("T7.C1", "Four radial arms", "Apply",
       "Students list the 4 angles of symmetry of a figure with 4 equal arms 90° apart, and check by turning a "
       "cut-out copy.",
       textbook=book("9.2", H_ARMS, stop=3),
       teach=["Predict first: a plus-shaped figure has 4 equal arms with 90° between neighbours. How many angles "
              "of symmetry does it have?",
              "Turns of 90°, 180°, 270° and 360° match, so 4 angles of symmetry.",
              "To check, trace the figure on two sheets, cut out one, and turn it over the fixed copy."],
       examples=[we("9.2.q7"), we("9.2.q8"), we("9.2.q9")],
       key_terms=["radial arms", "angle of symmetry"], misconceptions=["M_ARMS_ENOUGH"], minutes=10),
     A("T7.C2", "Exactly two angles, and three unequal arms", "Analyze",
       "Students change a 4-arm figure to have only 2 angles of symmetry, and show that 3 arms with unequal angles "
       "give only 360°.",
       textbook=book("9.2", H_ARMS, start=3, stop=10),
       teach=["Predict first: how can you change the plus figure so that it has only two angles of symmetry?",
              "Make opposite arms alike but the two pairs different. Now only 180° and 360° match.",
              "Three arms with unequal angles between them: only a full turn of 360° brings the figure back, so "
              "it has no rotational symmetry."],
       examples=[we("9.2.q10"), we("9.2.q11"), we("9.2.q12")],
       key_terms=["radial arms"], misconceptions=["M_ARMS_ENOUGH", "M_ORDER_DISTINCT"], minutes=10),
     A("T7.C3", "Why three equal arms need 120°", "Analyze",
       "Students show that three arms give 3 angles of symmetry only when each angle between arms is "
       "360 ÷ 3 = 120°, and list the angles 120°, 240° and 360°.",
       textbook=book("9.2", H_ARMS, start=10, stop=20),
       teach=["Predict first: if a 3-arm figure turns onto itself, what must be true of the three angles between "
              "the arms?",
              "Angle A must land on B, B on C and C on A, so the three angles are equal.",
              "The full turn of 360° is shared equally, so each angle is 360 ÷ 3 = 120°.",
              "The figure then turns onto itself at 120°, 240° and 360°."],
       examples=[we("9.2.q13"), we("9.2.q14"), we("9.2.q15")],
       key_terms=["radial arms", "angle of symmetry"], misconceptions=["M_ARMS_ENOUGH"], minutes=10),
     DOER("T7.C4", "Pull it together and do it: Radial Arms Builder", "radial_arms", "Apply",
          "Students set the number of arms and the angles between them on the tool, turn the figure, and give "
          "its angles of symmetry and its order.",
          ["Equal arms spaced equally: n arms give n angles of symmetry.",
           "The order of rotational symmetry is the number of angles of symmetry, counting 360°.",
           "Unequal spacing leaves only 360°."],
          items=[fio("9.2.FiO1.Q3")],
          misconceptions=["M_ARMS_ENOUGH", "M_ORDER_DISTINCT"])]))

# ============================== T8 Angles of symmetry: 360 divided by n (9.2) ================================
TOPICS.append(TOPIC(
    "T8", "M2", "Order and the Smallest Angle of Symmetry", ["9.2"], "Analyze",
    "Students find the smallest angle of symmetry as 360 ÷ n, list the other angles as its multiples, and decide "
    "which smallest angles are possible.",
    "With n angles of symmetry the smallest is 360 ÷ n and every other angle is a multiple of it.",
    [A("T8.C1", "Five, six and seven arms", "Apply",
       "Students find the smallest angle of symmetry of figures with 5, 6 and 7 equal arms as 360 ÷ n, and write "
       "it as a mixed fraction when it is not whole.",
       textbook=book("9.2", H_ARMS, start=20, stop=24),
       teach=["Predict first: for 5 equal arms, what is the angle between neighbours?",
              "360 ÷ 5 = 72°, so the angles of symmetry are 72°, 144°, 216°, 288° and 360°.",
              "For 6 arms, 360 ÷ 6 = 60°.",
              "For 7 arms, 360 ÷ 7 is 51 with remainder 3, so the smallest angle is 51 3/7°, not a whole number."],
       examples=[we("9.1.q2"), we("9.2.q16"), we("9.2.q17")],
       key_terms=["angle of symmetry", "order"], misconceptions=["M_ANY_SMALLEST"], minutes=12),
     A("T8.C2", "Angles are multiples of the smallest", "Analyze",
       "Students explain that the angles of symmetry of a figure are the multiples of its smallest angle and that "
       "360° is always one of them.",
       textbook=book("9.2", H_FIO1, start=3, stop=12),
       teach=["Predict first: a figure has exactly 4 angles of symmetry: 90°, 180°, 270°, 360°. What do these "
              "numbers have in common?",
              "They are all multiples of 90°, the smallest angle. With 3 angles they are multiples of 120°, with "
              "2 angles multiples of 180°.",
              "True: every figure has 360° as an angle of symmetry. True: if the smallest angle is a whole number "
              "of degrees, it is a factor of 360."],
       examples=[we("9.2.q18"), we("9.2.q19")],
       key_terms=["multiple", "factor"], misconceptions=["M_ANY_SMALLEST", "M_ORDER_DISTINCT"], minutes=10),
     DOER("T8.C3", "Pull it together and do it: Angle Ladder", "angle_ladder", "Apply",
          "Students pick the number of equal turns on the tool, read the smallest angle 360 ÷ n and the ladder "
          "of its multiples, and decide whether a given smallest angle is possible.",
          ["The smallest angle is 360 ÷ n and the other angles are its multiples.",
           "A whole-number smallest angle must be a factor of 360.",
           "To colour a circle of 12 sectors, the pattern must repeat every 1, 2, 3, 4, 6 or 12 sectors."],
          items=[fio("9.2.FiO2.Q1"), fio("9.2.FiO2.Q4"), fio("9.2.FiO2.Q5"), fio("9.2.FiO2.Q6")],
          misconceptions=["M_ANY_SMALLEST"])]))

# ============================== T9 The circle and objects around us (9.2) ====================================
TOPICS.append(TOPIC(
    "T9", "M2", "Symmetries of a Circle", ["9.2"], "Understand",
    "Students explain that a circle has every angle as an angle of symmetry and every diameter as a line of "
    "symmetry, and find turning objects around them.",
    "A circle matches itself after any turn, and about every diameter.",
    [A("T9.C1", "A circle has no smallest angle", "Understand",
       "Students explain that a circle looks the same after a turn of any angle, so it has no smallest angle of "
       "symmetry.",
       textbook=book("9.2", H_FIO1, start=12) + book("9.2", H_CIRCLE, stop=1),
       teach=["Predict first: turn a circle about its centre by a tiny angle. Does it still match itself?",
              "It does, whatever the angle, so every angle is an angle of symmetry.",
              "Most figures have a smallest angle of symmetry. The circle does not."],
       examples=[we("9.2.q20")],
       key_terms=["circle", "angle of symmetry"], misconceptions=["M_CIRCLE_SMALLEST"], minutes=8),
     A("T9.C2", "Every diameter is a line of symmetry", "Understand",
       "Students show that every diameter of a circle is a line of symmetry, so the circle has endless lines of "
       "symmetry.",
       textbook=book("9.2", H_CIRCLE, start=1, stop=2),
       teach=["Predict first: pick a point on the rim and join it to the centre. Is the diameter through it a "
              "line of symmetry?",
              "Fold along it: the two half circles overlap exactly.",
              "The point on the rim can be anywhere, so every diameter is a line of symmetry."],
       examples=[we("9.2.q21")],
       key_terms=["diameter", "line of symmetry"], misconceptions=["M_ONE_LINE"], minutes=8),
     A("T9.C3", "Turning objects around us", "Apply",
       "Students name everyday objects that look the same after a turn, such as wheels and fan blades, and give "
       "how many turns each has.",
       textbook=book("9.2", H_CIRCLE, start=2),
       teach=["Predict first: look at a bicycle wheel, a ceiling fan and a three-bladed propeller. Which turn "
              "onto themselves, and how many times in one full turn?",
              "A fan with 3 equal blades matches itself 3 times in a full turn, a wheel with 8 equal spokes 8 "
              "times.",
              "Objects like these have rotational symmetry."],
       examples=[we("9.2.q22")],
       key_terms=["rotational symmetry"], misconceptions=["M_ORDER_DISTINCT"], minutes=8),
     DOER("T9.C4", "Pull it together and do it: Wheel Counting", None, "Apply",
          "Students count the lines of symmetry and the angles of symmetry of a wheel with equal spokes such as "
          "the Ashoka Chakra.",
          ["A wheel with n equal spokes has n angles of symmetry.",
           "It also has n lines of symmetry when the spokes are drawn straight.",
           "Count them with a fold and a turn."],
          items=[fio("9.2.FiO2.Q11")],
          misconceptions=["M_ORDER_DISTINCT"])]))
