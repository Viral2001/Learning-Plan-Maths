# -*- coding: utf-8 -*-
"""Topics T5 to T8: angles in a quadrilateral (M3), parallelograms and rhombuses (M4). Book pp 94 to 102."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T5 The angle sum of a quadrilateral ==========================================
TOPICS.append(TOPIC(
    "T5", "M3", "The Angle Sum of a Quadrilateral", ["4.2"], "Apply",
    "Students prove with a diagonal that the angles of any quadrilateral add up to 360°, use the result to find a "
    "missing angle, and explain why a quadrilateral cannot have exactly three right angles.",
    "A diagonal splits a quadrilateral into two triangles, so its four angles add up to 180° + 180° = 360°. Three "
    "right angles therefore force the fourth angle to be a right angle too.",
    [A("T5.C1", "The four angles add up to 360°", "Apply",
       "Students split a quadrilateral by a diagonal into two triangles, add their angles to show the four angles "
       "of the quadrilateral total 360°, and find a missing angle.",
       textbook=["We have seen that the sum of the angles of a triangle is 180°. There is a similar regularity in "
                 "the sum of the angles of a quadrilateral.",
                 "Consider a quadrilateral SOME. Draw a diagonal SM. We get two triangles ∆SEM and ∆SOM.",
                 "In ∆SEM, the three angles add up to 180°. And in ∆SOM, the three angles add up to 180°.",
                 "What do we get when we add all six angles? We will have 180° + 180° = 360°.",
                 "The sum of all angles in any quadrilateral is 360°."],
       teach=["Predict first: do the four angles of a quadrilateral add up to 180°, like a triangle, or to "
              "something else?",
              "Draw the diagonal SM of quadrilateral SOME. It makes two triangles, ∆SEM and ∆SOM.",
              "The six angles of the two triangles together make exactly the four angles of SOME.",
              "So the four angles add up to 180° + 180° = 360°, for every quadrilateral."],
       examples=[
           WE("Three angles of a quadrilateral are 75°, 95° and 110°. Find the fourth angle.",
              ["A diagonal splits the quadrilateral into two triangles, so its angles add up to 180 + 180 = 360.",
               "The three known angles add up to 75 + 95 + 110 = 280.",
               "The fourth angle is 360 − 280 = 80."],
              "80°", ncert=["4.2.angle_sum"])],
       key_terms=["angle sum", "diagonal"], misconceptions=["M_ANGLE_SUM_180"], minutes=8),
     A("T5.C2", "Three right angles force the fourth", "Apply",
       "Students use the angle sum to explain why a quadrilateral with three right angles must have a fourth right "
       "angle.",
       textbook=["4.2 Angles in a Quadrilateral",
                 "Is it possible to construct a quadrilateral with three angles equal to 90° and the fourth angle "
                 "not equal to 90°?",
                 "You might have observed through constructions that this may not be possible. But why not?",
                 "This explains why it is impossible for a quadrilateral to have three right angles, with the fourth "
                 "angle not right angle."],
       teach=["Predict first: can you draw a quadrilateral with three right angles whose fourth angle is not a "
              "right angle?",
              "The four angles must add up to 360°.",
              "Three right angles already use 270°, which leaves exactly 90° for the fourth.",
              "So a quadrilateral with three right angles is a rectangle."],
       examples=[
           WE("A quadrilateral has three angles of 90°. Find the fourth angle.",
              ["The angles of a quadrilateral add up to 360.",
               "The three right angles add up to 90 + 90 + 90 = 270.",
               "The fourth angle is 360 − 270 = 90."],
              "90°, so the quadrilateral is a rectangle", ncert=["4.2.three_right"])],
       key_terms=["right angle", "angle sum"], misconceptions=["M_ANGLE_SUM_180"], minutes=6),
     DOER("T5.C3", "Practice: the angle sum of any quadrilateral", "angle_sum_folder", "Apply",
          "Students place the four angles of quadrilaterals together to see a full turn, find missing angles, and "
          "show that the angle sum is 360° even for a quadrilateral with a corner that caves in.",
          ["A diagonal splits a quadrilateral into two triangles.",
           "The four angles of any quadrilateral add up to 360°.",
           "A missing angle is 360° minus the other three."],
          items=[
              FIO("FiO3.q10", "Figure it Out (kites and trapeziums, question 10)",
                  "Will the sum of the angles in a quadrilateral such as the following one also be 360°? Find the "
                  "answer using geometric reasoning as well as by constructing this figure and measuring. (ABCD "
                  "has one corner that caves in.)",
                  ["Draw the diagonal from the caved-in corner to the opposite corner; it lies inside the figure.",
                   "It splits ABCD into two triangles, each with angles adding up to 180.",
                   "At the caved-in corner the two triangle angles together make the reflex angle of ABCD.",
                   "So the four angles of ABCD add up to 180 + 180 = 360."],
                  "Yes; the angle sum is still 360°, using the diagonal that lies inside the figure")])],
    key_terms=["angle sum", "diagonal"]))

# ============================== T6 Parallelograms =============================================================
TOPICS.append(TOPIC(
    "T6", "M4", "Parallelograms", ["4.3"], "Analyze",
    "Students construct a parallelogram from two sides and the angle between them, place it in a Venn diagram with "
    "rectangles and squares, and prove that its adjacent angles add up to 180°, its opposite angles are equal and "
    "its opposite sides are equal.",
    "A parallelogram is a quadrilateral whose opposite sides are parallel; every rectangle is one. Its adjacent "
    "angles add up to 180°, its opposite angles are equal, and its opposite sides are equal.",
    [A("T6.C1", "Parallel opposite sides that are not a rectangle", "Understand",
       "Students construct a parallelogram from adjacent sides of 4 cm and 5 cm with 30° between them, define a "
       "parallelogram, and show rectangles and squares inside the parallelograms in a Venn diagram.",
       textbook=["4.3 More Quadrilaterals with Parallel Opposite Sides",
                 "Rectangles (and therefore squares) have parallel opposite sides. Are there quadrilaterals that "
                 "have parallel opposite sides that are not rectangles?",
                 "This can be easily done by drawing two pairs of parallel lines, ensuring that they do not meet at "
                 "right angles.",
                 "Thus, a larger set of quadrilaterals exists in which the opposite sides are parallel. Such "
                 "quadrilaterals are called parallelograms.",
                 "Is a rectangle a parallelogram? A rectangle has opposite sides parallel. So, it satisfies the "
                 "parallelogram's definition. Hence, it is indeed a parallelogram.",
                 "Let us represent this relation using a Venn diagram.",
                 "Draw a parallelogram with adjacent sides of lengths 4 cm and 5 cm, and an angle of 30° between "
                 "them.",
                 "Step 1: Draw line segments AB = 4 cm and AD = 5 cm with an angle of 30° between them. Step 2: Draw "
                 "a line parallel to AB through the point D, and a line parallel to AD through B. Mark the point at "
                 "which these lines intersect as C."],
       teach=["Predict first: must a quadrilateral with parallel opposite sides be a rectangle?",
              "Draw two pairs of parallel lines that do not meet at right angles: the quadrilateral they make is "
              "not a rectangle.",
              "A quadrilateral whose opposite sides are parallel is a parallelogram.",
              "A rectangle has parallel opposite sides, so it is a special parallelogram; in the Venn diagram "
              "squares sit inside rectangles, which sit inside parallelograms."],
       examples=[
           WE("Construct a parallelogram ABCD with AB = 4 cm, AD = 5 cm and an angle of 30° between them.",
              ["Draw AB = 4 cm.",
               "At A draw a 30° angle and mark D on its arm with AD = 5 cm.",
               "Through D draw a line parallel to AB; through B draw a line parallel to AD.",
               "Mark the point where these two lines meet as C.",
               "ABCD has both pairs of opposite sides parallel, so it is a parallelogram."],
              "ABCD is the required parallelogram, and it is not a rectangle",
              ncert=["4.3.construct_4_5_30"])],
       ncert=["4.3.construct_parallel", "4.3.venn_pgram"],
       key_terms=["parallelogram", "parallel lines", "Venn diagram"], misconceptions=["M_ONE_NAME"], minutes=8),
     A("T6.C2", "The angles of a parallelogram", "Apply",
       "Students use co-interior angles to find the other angles of a parallelogram from one angle and show that "
       "its opposite angles are always equal.",
       textbook=["Deduction 6: What can we say about the angles of a parallelogram?",
                 "In the parallelogram ABCD, AB||CD, and AD is a transversal to them. ∠A + ∠D = 180° (sum of the "
                 "internal angles on the same side of a transversal). Therefore, ∠D = 180° − 30° = 150°.",
                 "Using these equations, we get ∠B = 150° and ∠C = 30°.",
                 "We see that in this parallelogram, the adjacent pairs of angles add up to 180° and opposite pairs "
                 "of angles are equal.",
                 "What about the opposite angles? Will they be equal in all parallelograms? If yes, how can we be "
                 "sure? Let us take one of the angles to be x.",
                 "Since ∠P + ∠R = 180°, ∠R = 180 − x. Similarly, ∠A = 180 − (180 − x) = x.",
                 "Therefore, this shows that the opposite angles of a parallelogram are always equal."],
       teach=["Predict first: one angle of a parallelogram is 30°. Are the other angles 30° too?",
              "Next-door angles sit between a pair of parallel sides, on the same side of a transversal, so they add "
              "up to 180°.",
              "So the neighbours of 30° are 150°, and the angle opposite 30° is 180° − 150° = 30°.",
              "With one angle x: its neighbours are 180° − x, and the opposite angle is 180° − (180° − x) = x. "
              "Opposite angles are always equal."],
       examples=[
           WE("In parallelogram ABCD, ∠A = 30°. Find ∠B, ∠C and ∠D.",
              ["AB || CD with transversal AD, so ∠A + ∠D = 180.",
               "So ∠D = 180 − 30 = 150.",
               "AD || BC with transversal AB, so ∠A + ∠B = 180, and ∠B = 150.",
               "∠C + ∠D = 180, so ∠C = 180 − 150 = 30."],
              "∠B = 150°, ∠C = 30°, ∠D = 150°", ncert=["4.3.ded6"])],
       key_terms=["adjacent angles", "opposite angles", "co-interior angles"],
       misconceptions=["M_ADJ_EQUAL"], minutes=8),
     A("T6.C3", "The opposite sides of a parallelogram are equal", "Analyze",
       "Students prove by the AAS condition that the opposite sides of a parallelogram are equal, write the "
       "congruence in matching order, and list the properties of a parallelogram.",
       textbook=["Deduction 7: What can we say about the sides of a parallelogram?",
                 "By looking at a parallelogram, it appears that the opposite sides are equal. Can we again use "
                 "congruence to show this? Which two triangles can be considered for this?",
                 "In ∆ABD and ∆CDB, the angles marked with a single arc are equal as they are the opposite angles "
                 "of a parallelogram. Since AD||BC, and BD is a transversal to it, the angles marked with double arcs "
                 "are equal as they are alternate angles.",
                 "So, by the AAS condition, the triangles are congruent, that is, ∆ABD ≅ ∆CDB. Therefore, AD = CB, "
                 "and AB = CD.",
                 "Is it wrong to write ∆ABD ≅ ∆CBD? Why?",
                 "Property 1: The opposite sides of a parallelogram are equal. Property 2: The opposite sides of a "
                 "parallelogram are parallel. Property 3: In a parallelogram, the adjacent angles add up to 180°, and "
                 "the opposite angles are equal."],
       teach=["Predict first: in the parallelogram with sides 4 cm and 5 cm, how long are the other two sides?",
              "Draw the diagonal BD. In ∆ABD and ∆CDB: ∠A = ∠C (opposite angles), ∠ADB = ∠CBD (alternate angles), "
              "and BD is shared.",
              "AAS makes them congruent, so AD = CB and AB = CD.",
              "Match the letters: A goes with C. Writing ∆CBD would pair AB with CB, which are not equal sides."],
       examples=[
           WE("In parallelogram ABCD, AB = 4 cm and AD = 5 cm. Find CB and CD, and say why ∆ABD ≅ ∆CBD is wrong.",
              ["Join the diagonal BD.",
               "∠BAD = ∠DCB, because they are opposite angles of the parallelogram.",
               "AD || BC with transversal BD, so ∠ADB = ∠CBD (alternate angles).",
               "BD is common, so by AAS ∆ABD ≅ ∆CDB.",
               "So CB = AD = 5 cm and CD = AB = 4 cm.",
               "∆CBD would match A with C but B with B, claiming AB equals CB, yet AB is 4 cm and CB is 5 cm."],
              "CB = 5 cm and CD = 4 cm; ∆ABD ≅ ∆CBD is wrong because its vertices do not match",
              ncert=["4.3.ded7", "4.3.wrong_abd"])],
       ncert=["4.3.props"],
       key_terms=["alternate angles", "AAS", "opposite sides"],
       misconceptions=["M_CONGRUENCE_ORDER"], minutes=10),
     DOER("T6.C4", "Practice: sides and angles of a parallelogram", "sides_angles_lab", "Apply",
          "Students sweep a parallelogram through its family, use its forced marks to find unknown sides and "
          "angles, and show that a quadrilateral with equal opposite sides is a parallelogram.",
          ["Opposite sides of a parallelogram are parallel and equal.",
           "Adjacent angles add up to 180°.",
           "Opposite angles are equal."],
          items=[
              FIO("FiO3.q9", "Figure it Out (kites and trapeziums, question 9)",
                  "What type of a quadrilateral is one in which the opposite sides are equal? Justify your answer. "
                  "(Hint: Draw a diagonal and check for congruent triangles.)",
                  ["Let ABCD have AB = CD and AD = CB, and draw the diagonal BD.",
                   "∆ABD ≅ ∆CDB by SSS, because BD is common.",
                   "So ∠ABD = ∠CDB; these are alternate angles for AB and DC with transversal BD, so AB || DC.",
                   "Also ∠ADB = ∠CBD, so AD || BC.",
                   "Both pairs of opposite sides are parallel."],
                  "A parallelogram")])],
    key_terms=["parallelogram", "transversal"]))

# ============================== T7 Diagonals of a parallelogram ==============================================
TOPICS.append(TOPIC(
    "T7", "M4", "Diagonals of a Parallelogram", ["4.3"], "Analyze",
    "Students check that the diagonals of a parallelogram need not be equal, prove by the ASA condition that they "
    "bisect each other, and use this to construct a parallelogram from its diagonals.",
    "The diagonals of a parallelogram need not be equal, but they always bisect each other. Conversely, any two "
    "segments that bisect each other are the diagonals of a parallelogram.",
    [A("T7.C1", "The diagonals of a parallelogram bisect each other", "Analyze",
       "Students prove by the ASA condition that the diagonals of a parallelogram meet at their midpoints and "
       "explain why the congruence must be written in matching order.",
       textbook=["Are the diagonals of a parallelogram always equal? Check with the parallelogram that you have "
                 "constructed. We see that the diagonals of a parallelogram need not be equal.",
                 "Deduction 8: What is the point of intersection of the two diagonals in a parallelogram?",
                 "AE = YS (as they are the opposite sides of the parallelogram). The angles marked using a single "
                 "arc are equal, and so are the angles marked using a double arc, since they are alternate angles of "
                 "parallel lines.",
                 "Thus, by the ASA condition, the triangles are congruent, that is, ∆AOE ≅ ∆YOS. Therefore, OA = OY, "
                 "and OE = OS.",
                 "Is it wrong to write ∆AOE ≅ ∆SOY? Why?",
                 "Property 4: The diagonals of a parallelogram bisect each other.",
                 "Do the diagonals of a parallelogram intersect at a particular angle?"],
       teach=["Predict first: are the diagonals of a parallelogram equal? Do they cross at their midpoints?",
              "In the 4 cm by 5 cm parallelogram the diagonals clearly differ in length, so they need not be equal.",
              "In EASY, compare ∆AOE and ∆YOS: AE = YS, and two pairs of alternate angles are equal. ASA makes them "
              "congruent, so OA = OY and OE = OS.",
              "The diagonals bisect each other. They meet at no fixed angle: it changes from one parallelogram to "
              "another."],
       examples=[
           WE("In parallelogram EASY the diagonals AY and ES meet at O, with AY = 10 cm and ES = 6 cm. Find OA, OY, "
              "OE and OS, and say why ∆AOE ≅ ∆SOY is wrong.",
              ["AE = YS, because they are opposite sides of the parallelogram.",
               "AE || YS, so ∠OAE = ∠OYS and ∠OEA = ∠OSY (alternate angles).",
               "By ASA, ∆AOE ≅ ∆YOS, so OA = OY and OE = OS.",
               "OA = OY = 10 ÷ 2 = 5 cm and OE = OS = 6 ÷ 2 = 3 cm.",
               "∆SOY would pair A with S and E with Y, but A matches Y and E matches S."],
              "OA = OY = 5 cm and OE = OS = 3 cm; ∆SOY is in the wrong order",
              ncert=["4.3.ded8", "4.3.wrong_aoe"])],
       ncert=["4.3.diag_equal", "4.3.diag_angle"],
       key_terms=["bisect", "ASA", "alternate angles"],
       misconceptions=["M_DIAG_EQUAL_ALL", "M_CONGRUENCE_ORDER"], minutes=10),
     DOER("T7.C2", "Practice: build a parallelogram from its diagonals", None, "Apply",
          "Students construct a parallelogram from the lengths of its diagonals and the angle between them.",
          ["The diagonals of a parallelogram bisect each other.",
           "They need not be equal and need not meet at a right angle.",
           "Two segments that bisect each other are the diagonals of a parallelogram."],
          items=[
              FIO("FiO2.q2", "Figure it Out (parallelograms and rhombuses, question 2)",
                  "Using the diagonal properties, construct a parallelogram whose diagonals are of lengths 7 cm and "
                  "5 cm, and intersect at an angle of 140°.",
                  ["Draw AC = 7 cm and mark its midpoint O, so OA = OC = 3.5 cm.",
                   "At O draw a line making 140° with OC.",
                   "On it mark B and D on opposite sides of O with OB = OD = 2.5 cm, so BD = 5 cm.",
                   "Join A, B, C and D in order.",
                   "The diagonals bisect each other, so ABCD is a parallelogram."],
                  "ABCD, with diagonals 7 cm and 5 cm bisecting each other at 140°, is the parallelogram")])],
    key_terms=["diagonal", "bisect", "parallelogram"]))

# ============================== T8 The rhombus =================================================================
TOPICS.append(TOPIC(
    "T8", "M4", "The Rhombus", ["4.4"], "Analyze",
    "Students construct a rhombus that is not a square, prove that a diagonal makes four equal angles so that every "
    "rhombus is a parallelogram, place rhombuses, rectangles and squares in a Venn diagram, and prove that the "
    "diagonals of a rhombus meet at right angles.",
    "A rhombus is a quadrilateral with all sides equal. Every rhombus is a parallelogram; its diagonals bisect each "
    "other at 90° and bisect its angles. A square is both a rectangle and a rhombus.",
    [A("T8.C1", "Equal sides without right angles", "Apply",
       "Students construct a quadrilateral with four equal sides and a 50° angle and define a rhombus.",
       textbook=["4.4 Quadrilaterals with Equal Sidelengths",
                 "Are squares the only quadrilaterals that have equal sidelengths? Let us explore this question "
                 "through construction.",
                 "Draw two equal sides AD and AB, that are not perpendicular to each other. Can we complete this "
                 "quadrilateral so that all its sides are of the same length?",
                 "Mark a point C whose distance from B and D is equal to AB (or AD). To do this, measure AB using a "
                 "compass. Keeping this length as the radius, cut arcs from B and D.",
                 "Note that we could have constructed such a quadrilateral by taking any angle less than 180° (in "
                 "place of 50°).",
                 "A quadrilateral in which all the sides have the same length is a rhombus."],
       teach=["Predict first: is a square the only quadrilateral with four equal sides?",
              "Draw AB = AD with an angle of 50° between them, not 90°.",
              "With the compass set to AB, cut arcs from B and from D. They cross at C, and all four sides are equal.",
              "A quadrilateral with all sides equal is a rhombus; any angle below 180° works in place of 50°."],
       examples=[
           WE("Construct a quadrilateral ABCD with all sides 5 cm and ∠A = 50°.",
              ["Draw AB = 5 cm.",
               "At A draw a 50° angle and mark D on its arm with AD = 5 cm.",
               "With the compass set to 5 cm, draw an arc from B and an arc from D.",
               "Mark the point where the arcs cross as C, and join BC and DC.",
               "AB = BC = CD = DA = 5 cm, so ABCD is a rhombus."],
              "ABCD is a rhombus with a 50° angle, and it is not a square", ncert=["4.4.construct_rhombus"])],
       key_terms=["rhombus", "compass", "arc"], misconceptions=["M_SQUARE_NOT_RECT"], minutes=8),
     A("T8.C2", "Every rhombus is a parallelogram", "Analyze",
       "Students show that a diagonal of a rhombus makes four equal angles, use this to find the angles of the 50° "
       "rhombus, and deduce that every rhombus is a parallelogram.",
       textbook=["Deduction 9: What can we say about the angles in a rhombus?",
                 "Consider a rhombus GAME. In ∆GAE, since GE = GA, a = d. Similarly, in ∆MAE, since ME = MA, b = c. "
                 "It can be seen that ∆GAE ≅ ∆MAE (How?). So, a = b, c = d and ∠G = ∠M.",
                 "Thus, we have, a = b = c = d.",
                 "In ∆ADB, we have a + a + 50 = 180°. So, a = 65°. Thus, the angles of the rhombus ABCD are 50°, "
                 "130°, 50°, and 130°.",
                 "Consider the lines EM and GA and its transversal AE. Since the alternate angles are equal, EM||GA. "
                 "Similarly, GE||AM.",
                 "As opposite sides are parallel, GAME is also a parallelogram. Thus, every rhombus is a "
                 "parallelogram, and the properties of a parallelogram hold true for a rhombus as well."],
       teach=["Predict first: in the rhombus with a 50° angle, what are the other three angles?",
              "Diagonal AE of rhombus GAME makes two isosceles triangles, and ∆GAE ≅ ∆MAE by SSS, so all four "
              "angles it makes are equal.",
              "Those equal angles are alternate angles, so EM || GA and GE || AM: every rhombus is a parallelogram.",
              "In the 50° rhombus, each angle made by the diagonal is half of 180° − 50°, which is 65°, so the "
              "rhombus has angles 50°, 130°, 50° and 130°."],
       examples=[
           WE("Rhombus ABCD has ∠A = 50°. Find its other angles.",
              ["Diagonal BD makes four equal angles a: two at B and two at D.",
               "In ∆ADB, a + a + 50 = 180, so the two angles a add up to 180 − 50 = 130.",
               "Each is 130 ÷ 2 = 65.",
               "∠B = ∠D = 65 + 65 = 130, and ∠C = ∠A = 50, because a rhombus is a parallelogram."],
              "The angles are 50°, 130°, 50° and 130°", ncert=["4.4.ded9"])],
       ncert=["4.4.rhombus_pgram"],
       key_terms=["isosceles triangle", "alternate angles", "parallelogram"],
       misconceptions=["M_ONE_NAME"], minutes=10),
     A("T8.C3", "The diagonals of a rhombus meet at right angles", "Analyze",
       "Students place rhombuses, rectangles and squares in one Venn diagram, list the properties of a rhombus, and "
       "prove by the SSS condition that its diagonals meet at 90°.",
       textbook=["So a rhombus is a parallelogram, and a rectangle is also a parallelogram. How can this be "
                 "represented using a Venn diagram? Where will the set of squares occur in this diagram?",
                 "We know that a square is a rectangle. Since the opposite sides of a square are parallel, a square "
                 "is also a parallelogram. Further, since all the sides of a square have the same length, a square "
                 "is also a rhombus.",
                 "Property 1: All the sides of a rhombus are equal to each other. Property 2: The opposite sides of a "
                 "rhombus are parallel to each other. Property 3: In a rhombus, the adjacent angles add up to 180°, "
                 "and the opposite angles are equal. Property 4: The diagonals of a rhombus bisect each other. "
                 "Property 5: The diagonals of a rhombus bisect its angles.",
                 "Are the diagonals of a rhombus equal?",
                 "Deduction 10: In the rhombus GAME, we have ∆GEO ≅ ∆MEO (why?). So, ∠GOE = ∠MOE. As they add up "
                 "to 180°, they should be 90° each.",
                 "Property 6: Diagonals of a rhombus intersect each other at an angle of 90°."],
       teach=["Predict first: do the diagonals of a rhombus meet at a special angle?",
              "Rectangles and rhombuses both sit inside parallelograms; their overlap is the squares.",
              "In ∆GEO and ∆MEO: GE = ME, GO = MO (diagonals bisect each other), and EO is shared, so SSS makes "
              "them congruent.",
              "∠GOE = ∠MOE and together they make 180°, so each is 90°. The diagonals need not be equal."],
       examples=[
           WE("In rhombus GAME the diagonals meet at O, with GM = 8 cm and EA = 6 cm. Find the angle at O, GO and "
              "EO.",
              ["A rhombus is a parallelogram, so its diagonals bisect each other: GO = MO and EO = AO.",
               "In ∆GEO and ∆MEO: GE = ME, GO = MO, and EO is common, so ∆GEO ≅ ∆MEO by SSS.",
               "So ∠GOE = ∠MOE, and together they make 180, so each is 90.",
               "GO = 8 ÷ 2 = 4 cm and EO = 6 ÷ 2 = 3 cm."],
              "The diagonals meet at 90°; GO = 4 cm and EO = 3 cm", ncert=["4.4.ded10"])],
       ncert=["4.4.venn", "4.4.props"],
       key_terms=["perpendicular", "SSS", "Venn diagram"],
       misconceptions=["M_DIAG_EQUAL_ALL", "M_DIAG_PERP_RHOMBUS"], minutes=10),
     DOER("T8.C4", "Practice: angles and diagonals of parallelograms and rhombuses", "rhombus_hinge", "Apply",
          "Students find the remaining angles of parallelograms and rhombuses and construct a rhombus from its "
          "diagonals.",
          ["A rhombus is a parallelogram with all sides equal.",
           "Adjacent angles add up to 180° and opposite angles are equal.",
           "The diagonals of a rhombus bisect each other at 90° and bisect its angles."],
          items=[
              FIO("FiO2.q1", "Figure it Out (parallelograms and rhombuses, question 1)",
                  "Find the remaining angles in the following quadrilaterals. (i) Parallelogram PEAR with ∠P = 40°. "
                  "(ii) Parallelogram PQRS with ∠P = 110°. (iii) Rhombus UVWX with diagonal XV and ∠XVU = 30°. "
                  "(iv) Rhombus OIEA with diagonal OE and ∠OEA = 20°.",
                  ["(i) Adjacent angles add up to 180, so ∠E = ∠R = 180 − 40 = 140, and ∠A = ∠P = 40.",
                   "(ii) ∠Q = ∠S = 180 − 110 = 70, and ∠R = ∠P = 110.",
                   "(iii) The diagonal XV bisects ∠V and ∠X, so ∠V = 30 + 30 = 60 and ∠X = 60.",
                   "Then ∠U = ∠W = 180 − 60 = 120.",
                   "(iv) The diagonal OE bisects ∠E and ∠O, so ∠E = 20 + 20 = 40 and ∠O = 40.",
                   "Then ∠A = ∠I = 180 − 40 = 140."],
                  "(i) ∠E = 140°, ∠A = 40°, ∠R = 140°; (ii) ∠Q = 70°, ∠R = 110°, ∠S = 70°; (iii) ∠V = ∠X = 60°, "
                  "∠U = ∠W = 120°; (iv) ∠E = ∠O = 40°, ∠A = ∠I = 140°"),
              FIO("FiO2.q3", "Figure it Out (parallelograms and rhombuses, question 3)",
                  "Using the diagonal properties, construct a rhombus whose diagonals are of lengths 4 cm and 5 cm.",
                  ["Draw AC = 5 cm and mark its midpoint O.",
                   "Draw the line through O perpendicular to AC.",
                   "On it mark B and D on opposite sides of O with OB = OD = 2 cm, so BD = 4 cm.",
                   "Join A, B, C and D in order.",
                   "The diagonals bisect each other at 90°, so all four sides are equal and ABCD is a rhombus."],
                  "ABCD, with diagonals 5 cm and 4 cm bisecting each other at right angles, is the rhombus")])],
    key_terms=["rhombus", "parallelogram", "diagonal"]))
