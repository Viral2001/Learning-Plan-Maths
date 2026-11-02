# -*- coding: utf-8 -*-
"""Topics T1 to T4: the chapter opening (M1), and rectangles and squares (M2). Book pp 82 to 94."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Four sides, four angles ===================================================
TOPICS.append(TOPIC(
    "T1", "M1", "Four Sides, Four Angles", ["Chapter opening"], "Understand",
    "",
    "Quadrilaterals are everywhere: in window frames, doors and tables. A quadrilateral is a closed figure made of "
    "four straight sides, and its angles are the angles between its sides. A carpenter's problem starts the chapter.",
    [A("T1.C1", "What makes a figure a quadrilateral?", "Understand",
       "",
       textbook=["In this chapter, we will study some interesting types of four-sided figures and solve problems "
                 "based on them. Such figures are commonly known as quadrilaterals. The word 'quadrilateral' is "
                 "derived from Latin words, quadri meaning four, and latus referring to sides.",
                 "Observe the following figures.",
                 "Figs. (i), (ii), and (iii) are quadrilaterals, and the others are not. Why?",
                 "The angles of a quadrilateral are the angles between its sides, as marked in Figs. (i), (ii), and "
                 "(iii).",
                 "We will start with the most familiar quadrilaterals, rectangles and squares."],
       teach=["Predict first: a carpenter's workshop is full of frames. Which of them are quadrilaterals, and which "
              "are not?",
              "A quadrilateral is a closed figure made of exactly four straight sides that meet only at their ends.",
              "A figure with a curved side, an open gap, or more than four sides is not a quadrilateral.",
              "The angles of a quadrilateral are the four angles between its sides, one at each corner.",
              "Keep this question open: the carpenter wants a frame that is exactly rectangular. How can she be "
              "sure it is?"],
       ncert=["opening"], key_terms=["quadrilateral", "side", "angle"], video_focus=["HOOK"], minutes=4,
       enrichment=True)],
    topic_type="framing"))

# ============================== T2 Rectangles from their diagonals ==========================================
TOPICS.append(TOPIC(
    "T2", "M2", "Rectangles from Their Diagonals", ["4.1"], "Analyze",
    "Students solve the Carpenter's Problem by deduction: they prove with congruent triangles that the diagonals of "
    "a rectangle are equal and bisect each other, and that equal diagonals which bisect each other at any angle "
    "always give a rectangle.",
    "The diagonals of a rectangle are equal and bisect each other. Conversely, two equal strips joined at their "
    "midpoints, at any angle, always give a rectangle, so a rectangle can be defined by its diagonals.",
    [A("T2.C1", "The Carpenter's Problem: the other strip", "Apply",
       "Students state the definition of a rectangle, model the carpenter's strips as diagonals, and prove by the "
       "SAS condition that the diagonals of a rectangle are equal.",
       textbook=["4.1 Rectangles and Squares",
                 "Rectangle: A rectangle is a quadrilateral in which (i) The angles are all right angles (90°), and "
                 "(ii) The opposite sides are of equal length.",
                 "Are there other ways to define a rectangle?",
                 "A carpenter needs to put together two thin strips of wood so that when a thread is passed through "
                 "their endpoints, it forms a rectangle. She already has one 8 cm long strip. What should be the "
                 "length of the other strip? Where should they both be joined?",
                 "1. What is the length of the other diagonal? 2. What is the point of intersection of the two "
                 "diagonals? 3. What should the angle be between the diagonals?",
                 "Since ABCD is a rectangle, we have AB = CD, ∠BAD = ∠CDA = 90°, and AD is common to both "
                 "triangles. So, ∆ADC ≅ ∆DAB by the SAS congruence condition.",
                 "Therefore, AC = BD. This shows that the diagonals of a rectangle always have the same length."],
       teach=["Predict first: the carpenter has one strip of 8 cm. Should the other strip be shorter, longer, or the "
              "same?",
              "The strips are the diagonals of the quadrilateral their ends make. Suppose the ends already form a "
              "rectangle ABCD.",
              "Compare ∆ADC and ∆DAB: AB = CD, the angles at A and D are both 90°, and AD is shared. SAS makes them "
              "congruent.",
              "So AC = BD: the diagonals of a rectangle are always equal. The other strip must also be 8 cm."],
       examples=[
           WE("The carpenter has one strip 8 cm long. How long must the other strip be for the thread to make a "
              "rectangle?",
              ["Model the strips as the diagonals AC and BD of a rectangle ABCD, with AC = 8 cm.",
               "In ∆ADC and ∆DAB: AB = CD, ∠BAD = ∠CDA = 90°, and AD is a common side.",
               "By the SAS condition, ∆ADC ≅ ∆DAB.",
               "So AC = BD, as corresponding parts of congruent triangles.",
               "The other strip must be 8 cm long."],
              "8 cm, because the diagonals of a rectangle are equal",
              ncert=["4.1.rect_def", "4.1.carpenter", "4.1.ded1"])],
       key_terms=["rectangle", "diagonal", "SAS"], misconceptions=["M_MEASURE_PROVES"], minutes=10),
     A("T2.C2", "The diagonals of a rectangle bisect each other", "Analyze",
       "Students prove by the AAS condition that the diagonals of a rectangle meet at their midpoints, and judge "
       "whether a given set of equalities is enough for a congruence.",
       textbook=["Deduction 2: What is the point of intersection of the two diagonals?",
                 "The blue angles are equal since they are vertically opposite angles. In order to show congruence, "
                 "consider ∠1 and ∠2. Are they equal?",
                 "Since ∠B is a right angle, ∠1 and ∠3 together make a right angle. In ∆BCD, ∠3 and ∠2 together "
                 "also make a right angle, because ∠C is a right angle. So, ∠1 = ∠2, each being 90° minus ∠3.",
                 "Thus, by the AAS condition for congruence, ∆AOB ≅ ∆COD. Hence OA = OC and OB = OD.",
                 "When the diagonals cross at their midpoints, we say that the diagonals bisect each other. "
                 "Bisecting a quantity means dividing it into two equal parts.",
                 "Can the following equalities be used to establish that ∆AOD ≅ ∆COB? AO = CO (proved above), "
                 "∠AOB = ∠COD (vertically opposite angles), AD = CB."],
       teach=["Predict first: where must the two strips cross, at their middles or somewhere else?",
              "Look at ∆AOB and ∆COD: AB = CD, the angles at O are vertically opposite, and ∠1 = ∠2 because each "
              "is 90° − ∠3.",
              "AAS makes the triangles congruent, so OA = OC and OB = OD: O is the midpoint of both diagonals.",
              "Check the Math Talk: ∠AOB and ∠COD are not angles of ∆AOD and ∆COB at all, so those three "
              "equalities cannot prove that congruence. Use ∠AOD = ∠COB and OD = OB instead, and SAS works."],
       examples=[
           WE("In rectangle ABCD the diagonals meet at O and AC = 8 cm. Find OA, OC, OB and OD.",
              ["In ∆AOB and ∆COD: AB = CD, ∠AOB = ∠COD (vertically opposite), and ∠ABD = ∠CDB (each is 90° "
               "minus the same angle).",
               "By the AAS condition, ∆AOB ≅ ∆COD, so OA = OC and OB = OD.",
               "The diagonals are equal, so BD = AC = 8 cm.",
               "Each half is 8 ÷ 2 = 4 cm."],
              "OA = OC = OB = OD = 4 cm; the strips are joined at their midpoints",
              ncert=["4.1.ded2", "4.1.mt_aod"])],
       key_terms=["bisect", "midpoint", "AAS", "vertically opposite angles"],
       misconceptions=["M_CONGRUENCE_ORDER"], minutes=10),
     A("T2.C3", "Equal diagonals that bisect each other make a rectangle", "Analyze",
       "Students find every angle of a quadrilateral whose equal diagonals bisect each other at 60°, show it is a "
       "rectangle, and explain the difference between a conjecture from measuring and a property proved by "
       "deduction.",
       textbook=["Deduction 3: What are the angles between the diagonals?",
                 "Let us check what quadrilateral we get if we draw the two diagonals such that their lengths are "
                 "equal, they bisect each other and have an arbitrary angle, say 60°, between them. Can you find all "
                 "the remaining angles?",
                 "In ∆AOB, since OA = OB, the angles opposite them are equal, say a. a + a + 60 = 180. Therefore "
                 "2a = 120. Thus a = 60.",
                 "We can see that ∆AOB ≅ ∆COD and ∆AOD ≅ ∆COB. Hence, AB = CD, and AD = CB. Therefore, ABCD is a "
                 "rectangle.",
                 "Carpenters in Europe use this method to get a rectangular frame. Farmers in Mozambique, a country "
                 "in Africa, use this method while constructing houses to get the base of the house in a "
                 "rectangular shape.",
                 "The Process of Finding Properties: observations through measurement give useful insights, but "
                 "with them we can only form a conjecture, a statement about which we are highly confident, but not "
                 "yet sure if it always holds true. The only way we can be sure is by justifying or proving the "
                 "statement.",
                 "Note to the Teacher: Gently encourage students to deduce or justify properties. Whenever students "
                 "face challenges, encourage them to experiment and observe, and use their intuition."],
       teach=["Predict first: two equal strips cross at their midpoints at 60°. Will the thread make a rectangle, "
              "or some slanted shape?",
              "The angles at O are 60°, 120°, 60° and 120°, by vertically opposite angles and linear pairs.",
              "All four half-diagonals are equal, so each small triangle is isosceles: the 60° triangles have base "
              "angles 60°, the 120° triangles have base angles 30°.",
              "Every corner is 60° + 30° = 90°, and congruent triangles give equal opposite sides: a rectangle.",
              "Carpenters in Europe and farmers in Mozambique use exactly this to set out rectangles.",
              "Measuring many rectangles only gives a conjecture; this deduction is what makes us sure."],
       examples=[
           WE("Two equal diagonals bisect each other and meet at 60°. Find all the angles of the quadrilateral ABCD "
              "and say what it is.",
              ["The four angles at O are 60°, 120°, 60° and 120°.",
               "In ∆AOB, OA = OB, so its two base angles are equal. Their sum is 180 − 60 = 120, so each is "
               "120 ÷ 2 = 60.",
               "In ∆AOD the angle at O is 120°, so its base angles add to 180 − 120 = 60, and each is 30.",
               "Each corner of ABCD is made of one angle of each kind: 60 + 30 = 90.",
               "∆AOB ≅ ∆COD and ∆AOD ≅ ∆COB by SAS, so AB = CD and AD = CB."],
              "Every angle of ABCD is 90° and its opposite sides are equal, so ABCD is a rectangle",
              ncert=["4.1.ded3_60"])],
       ncert=["4.1.carpenters_world", "4.1.process"],
       key_terms=["isosceles triangle", "conjecture", "deduction"],
       misconceptions=["M_MEASURE_PROVES"], minutes=10),
     A("T2.C3x", "Any angle between the diagonals", "Analyze",
       "Students repeat the argument with an angle of x between the diagonals and show every corner is still 90°.",
       textbook=["Take one of the angles between the diagonals as x. We can compute the four angles between the "
                 "diagonals to be x, x, 180 − x, and 180 − x.",
                 "a = (180 − x)/2 = 90 − x/2. Similarly, in the isosceles ∆AOD, let the base angles be b. b = x/2.",
                 "All the angles of the quadrilateral are a + b, which is 90 − x/2 + x/2 = 90.",
                 "Hence, no matter what the angles between the diagonals are, if the diagonals are equal and they "
                 "bisect each other, the quadrilateral is a rectangle."],
       teach=["Predict first: if the strips meet at 40° instead of 60°, are the corners still right angles?",
              "One small triangle has angle x at O and base angles (180 − x)/2 = 90 − x/2.",
              "The next has angle 180 − x at O and base angles x/2.",
              "Each corner is (90 − x/2) + x/2 = 90, whatever x is."],
       examples=[
           WE("Equal diagonals bisect each other at 40°. Find the angles of the quadrilateral.",
              ["In the triangle with 40° at O, the base angles add to 180 − 40 = 140, so each is 140 ÷ 2 = 70.",
               "The next triangle has 180 − 40 = 140 at O, so its base angles add to 180 − 140 = 40, and each "
               "is 20.",
               "Each corner of the quadrilateral is 70 + 20 = 90."],
              "All four angles are 90°, so it is again a rectangle",
              ncert=["4.1.ded3_x"])],
       key_terms=["bisect"], misconceptions=["M_MEASURE_PROVES"], minutes=6, thin=True),
     DOER("T2.C4", "Practice: join the strips to make a rectangle", "carpenter_strips", "Apply",
          "Students construct quadrilaterals from equal diagonals that bisect each other at a given angle and use "
          "the same idea to make an exact right angle with two sticks and a thread.",
          ["The diagonals of a rectangle are equal and bisect each other.",
           "Equal diagonals that bisect each other, at any angle, always make a rectangle.",
           "Measuring suggests a property; a deduction proves it."],
          items=[
              FIO("FiO1.q2", "Figure it Out (rectangles and squares, question 2)",
                  "Draw a quadrilateral whose diagonals have equal lengths of 8 cm that bisect each other, and "
                  "intersect at an angle of (i) 30° (ii) 40° (iii) 90° (iv) 140°.",
                  ["Draw AC = 8 cm and mark its midpoint O, so OA = OC = 4 cm.",
                   "At O draw a line making the given angle with OC.",
                   "On this line mark B and D on opposite sides of O with OB = OD = 4 cm, so BD = 8 cm.",
                   "Join A, B, C and D in order.",
                   "The diagonals are equal and bisect each other, so each figure is a rectangle; at 90° all four "
                   "sides are also equal."],
                  "All four are rectangles; the one with diagonals at 90° is a square"),
              FIO("FiO1.q4", "Figure it Out (rectangles and squares, question 4)",
                  "We have seen how to get 90° using paper folding. Now, suppose we do not have any paper but two "
                  "sticks of equal length, and a thread. How do we make an exact 90° using these?",
                  ["Cross the two equal sticks so that their midpoints meet at O.",
                   "Pass the thread round the four ends of the sticks in order.",
                   "The sticks are equal diagonals that bisect each other, so the thread makes a rectangle.",
                   "Every corner of a rectangle is 90°, so the thread turns through an exact 90° at each stick end."],
                  "Cross the sticks at their midpoints and run the thread round the four ends; each corner of the "
                  "thread is exactly 90°")])],
    key_terms=["rectangle", "diagonal", "bisect", "congruent"]))

# ============================== T3 Four right angles are enough ==============================================
TOPICS.append(TOPIC(
    "T3", "M2", "Four Right Angles Are Enough", ["4.1"], "Analyze",
    "Students define a rectangle by its diagonals and by its angles alone, prove that four right angles force the "
    "opposite sides to be equal, show that the opposite sides are parallel, and use the four properties of a "
    "rectangle to find unknown angles.",
    "A rectangle can be defined as a quadrilateral whose diagonals are equal and bisect each other, or simply as a "
    "quadrilateral whose angles are all 90°. Its opposite sides are equal and parallel, and its diagonals are equal "
    "and bisect each other.",
    [A("T3.C1", "Four right angles force equal opposite sides", "Analyze",
       "Students give the diagonal definition of a rectangle, prove by the AAS condition that a quadrilateral with "
       "four right angles has equal opposite sides, and write the congruence with the vertices in matching order.",
       textbook=["Rectangle: A rectangle is a quadrilateral whose diagonals are equal and bisect each other.",
                 "Would we be wrong if we just define a rectangle as a quadrilateral in which all the angles are 90°?",
                 "If you think that this definition is incomplete, try constructing a quadrilateral in which the "
                 "angles are all 90° but the opposite sides are not equal. Are you able to construct such a "
                 "quadrilateral?",
                 "Join BD. ∆BAD and ∆DCB seem congruent. Thus, by the AAS congruence condition, ∆BAD ≅ ∆DCB. "
                 "Therefore, AD = CB, and DC = BA.",
                 "Is it wrong to write ∆BAD ≅ ∆CDB? Why?",
                 "Rectangle: A rectangle is a quadrilateral in which the angles are all 90°."],
       teach=["Predict first: can you draw four right angles whose opposite sides are not equal?",
              "Join the diagonal BD. ∠A = ∠C = 90°, BD is shared, and ∠ABD = ∠CDB because each is 90° minus "
              "∠DBC.",
              "AAS gives ∆BAD ≅ ∆DCB, so the opposite sides are equal: four right angles are enough.",
              "Write the letters in matching order: A goes with C (both 90°), so ∆BAD ≅ ∆CDB is wrong."],
       examples=[
           WE("ABCD has all four angles 90°. Show that AD = CB and DC = BA, and say why writing ∆BAD ≅ ∆CDB is "
              "wrong.",
              ["Join the diagonal BD.",
               "∠BAD = ∠DCB = 90°, and BD is common to ∆BAD and ∆DCB.",
               "∠ABD + ∠DBC = 90° and ∠CDB + ∠DBC = 90°, so ∠ABD = ∠CDB.",
               "By AAS, ∆BAD ≅ ∆DCB, matching B with D, A with C and D with B.",
               "So AD = CB and BA = DC.",
               "∆CDB would match A with D, but the right angle at A matches the right angle at C, not D."],
              "AD = CB and DC = BA; ∆BAD ≅ ∆CDB is wrong because the vertices are not in matching order",
              ncert=["4.1.ded4", "4.1.wrong_bad"])],
       ncert=["4.1.alt_def", "4.1.all90_question"],
       key_terms=["definition", "AAS", "corresponding parts"],
       misconceptions=["M_RIGHT_ANGLES_ONLY", "M_CONGRUENCE_ORDER"], minutes=10),
     A("T3.C2", "Opposite sides of a rectangle are parallel", "Apply",
       "Students show with co-interior angles that the opposite sides of a rectangle are parallel and list the four "
       "properties of a rectangle.",
       textbook=["Property 1: All the angles of a rectangle are 90°.",
                 "Property 2: The opposite sides of a rectangle are equal.",
                 "Are the opposite sides of a rectangle parallel? AB acts as a transversal to AD and BC, and "
                 "∠A + ∠B = 90° + 90° = 180°. When the sum of the internal angles on the same side of the "
                 "transversal is 180°, the lines are parallel. So AD || BC.",
                 "Can you similarly show that AB is parallel to DC (AB||DC)?",
                 "Property 3: The opposite sides of a rectangle are parallel to each other.",
                 "Property 4: The diagonals of a rectangle are of equal length and they bisect each other."],
       teach=["Predict first: are the opposite sides of a rectangle parallel, and how could you be sure without "
              "measuring?",
              "Take a side as a transversal: the two angles on the same side of it are 90° and 90°, adding to 180°.",
              "Internal angles on the same side adding to 180° means the lines are parallel.",
              "So a rectangle has all angles 90°, opposite sides equal, opposite sides parallel, and equal "
              "diagonals that bisect each other."],
       examples=[
           WE("In rectangle ABCD, show that AB is parallel to DC.",
              ["Take AD as a transversal to the lines AB and DC.",
               "The internal angles on the same side of AD are ∠A and ∠D.",
               "∠A + ∠D = 90 + 90 = 180.",
               "Internal angles on the same side of a transversal adding to 180° means the lines are parallel."],
              "AB || DC", ncert=["4.1.parallel"])],
       ncert=["4.1.props"],
       key_terms=["parallel", "transversal", "co-interior angles"], misconceptions=["M_RIGHT_ANGLES_ONLY"],
       minutes=8),
     DOER("T3.C3", "Practice: use the properties of a rectangle", "quad_dragger", "Apply",
          "Students find unknown angles in rectangles from their diagonal properties and decide whether parallel, "
          "equal opposite sides are enough to make a rectangle.",
          ["A rectangle is a quadrilateral whose angles are all 90°.",
           "Its opposite sides are equal and parallel.",
           "Its diagonals are equal and bisect each other, so they cut it into isosceles triangles."],
          items=[
              FIO("FiO1.q1", "Figure it Out (rectangles and squares, question 1)",
                  "Find all the other angles inside the following rectangles. (i) Rectangle ABCD with diagonals "
                  "meeting at O and ∠CAB = 30°. (ii) Rectangle PQRS with diagonals meeting at O and ∠QOR = 110°.",
                  ["(i) OA = OB, because the diagonals are equal and bisect each other, so ∠ABD = ∠CAB = 30°.",
                   "∠CAD = 90 − 30 = 60, and OA = OD gives ∠ADB = 60.",
                   "In the same way ∠BDC = 30, ∠ACD = 30 and ∠ACB = 60.",
                   "At O: ∠AOB = 180 − 60 = 120 and ∠AOD = 180 − 120 = 60.",
                   "(ii) ∠POS = ∠QOR = 110 (vertically opposite), and ∠QOP = ∠ROS = 180 − 110 = 70.",
                   "In isosceles ∆QOR the base angles add to 180 − 110 = 70, so ∠OQR = ∠ORQ = 35.",
                   "∠OQP = 90 − 35 = 55, and in the same way ∠OPQ = ∠ORS = ∠OSR = 55 and ∠OPS = ∠OSP = 35."],
                  "(i) ∠ABD = 30°, ∠CAD = 60°, ∠ADB = 60°, ∠BDC = 30°, ∠ACD = 30°, ∠ACB = 60°, with 120° and 60° "
                  "at O; (ii) ∠POS = 110°, ∠QOP = ∠ROS = 70°, ∠OQR = ∠ORQ = 35°, ∠OQP = ∠OPQ = ∠ORS = ∠OSR = 55°, "
                  "∠OPS = ∠OSP = 35°"),
              FIO("FiO1.q5", "Figure it Out (rectangles and squares, question 5)",
                  "We saw that one of the properties of a rectangle is that its opposite sides are parallel. Can "
                  "this be chosen as a definition of a rectangle? In other words, is every quadrilateral that has "
                  "opposite sides parallel and equal, a rectangle?",
                  ["Draw two pairs of parallel lines that do not meet at right angles.",
                   "They make a quadrilateral with opposite sides parallel and equal, for example with angles 60°, "
                   "120°, 60° and 120°.",
                   "Its angles are not 90°, so it is not a rectangle."],
                  "No; a slanted parallelogram has opposite sides parallel and equal but is not a rectangle"),
              FIO("FiO3.q5", "Figure it Out (kites and trapeziums, question 5)",
                  "If PAIR and RODS are two rectangles, find ∠IOD. (O lies on AI, ∠ORI = 30°, PR = 5 cm and "
                  "RS = 5 cm.)",
                  ["In ∆ROI, ∠RIO = 90° because PAIR is a rectangle, and ∠ORI = 30°.",
                   "So ∠ROI = 180 − 90 − 30 = 60.",
                   "∠ROD = 90° because RODS is a rectangle.",
                   "∠IOD = ∠ROD − ∠ROI = 90 − 60 = 30."],
                  "∠IOD = 30°")])],
    key_terms=["rectangle", "parallel", "transversal"]))

# ============================== T4 The square, a special rectangle ===========================================
TOPICS.append(TOPIC(
    "T4", "M2", "The Square: A Special Rectangle", ["4.1"], "Analyze",
    "Students recognise a square as a rectangle with equal sides, show it in a Venn diagram, prove that the "
    "diagonals of a square bisect each other at right angles and bisect its angles, and construct squares from "
    "their diagonals.",
    "Every square is a rectangle, but not every rectangle is a square. The diagonals of a square are equal, bisect "
    "each other at 90° and bisect the angles of the square into 45° each.",
    [A("T4.C1", "Every square is a rectangle", "Understand",
       "Students identify which of several right-angled quadrilaterals are rectangles and which are squares, and "
       "draw the Venn diagram of squares inside rectangles.",
       textbook=["A Special Rectangle: In the quadrilaterals below, are there any non-rectangles?",
                 "All these quadrilaterals are rectangles, including (iv). However, it is a special kind of "
                 "rectangle with all sides of equal length. We know that this quadrilateral is also called a square.",
                 "Square: A square is a quadrilateral in which all the angles are equal to 90°, and all the sides "
                 "are of equal length.",
                 "Thus, every square is also a rectangle, but clearly every rectangle is not a square.",
                 "I am an Indian and I am a Malayali. Wait, which one of them are you, an Indian or a Malayali? How "
                 "can you be both?",
                 "In a Venn diagram, a set of objects is represented as points inside a closed curve. Since every "
                 "square is a rectangle, the oval of squares sits inside the oval of rectangles."],
       teach=["Predict first: a figure has four right angles and four sides of 4 cm. Is it a rectangle, a square, "
              "or both?",
              "A rectangle only needs all angles 90°. The figure has that, so it is a rectangle.",
              "It also has all sides equal, so it is a special rectangle: a square.",
              "Like a person who is both a Malayali and an Indian, a square is both a square and a rectangle. In a "
              "Venn diagram the squares sit inside the rectangles."],
       examples=[
           WE("Four quadrilaterals each have all angles 90°: 5 cm by 2 cm, 6 cm by 3.6 cm, 5 cm by 1 cm, and "
              "4 cm by 4 cm. Which are rectangles and which are squares?",
              ["A rectangle is a quadrilateral whose angles are all 90°, so all four are rectangles.",
               "A square also needs all four sides equal.",
               "Only the 4 cm by 4 cm figure has equal sides."],
              "All four are rectangles; only the 4 cm by 4 cm one is also a square",
              ncert=["4.1.special_rect", "4.1.square_def"])],
       ncert=["4.1.venn_square"],
       key_terms=["square", "Venn diagram"], misconceptions=["M_SQUARE_NOT_RECT", "M_ONE_NAME"], minutes=8),
     A("T4.C2", "The diagonals of a square meet at right angles", "Apply",
       "Students prove by the SSS condition that the diagonals of a square bisect each other at 90° and construct a "
       "square from an 8 cm diagonal.",
       textbook=["If the wooden strips have to be placed such that the thread passing through their endpoints forms "
                 "a square, what must be done?",
                 "What more needs to be done to get equal sidelengths as well? Can this be achieved by properly "
                 "choosing the angle between the diagonals?",
                 "By the SSS condition for congruence, ∆BOA ≅ ∆BOC. These angles are equal and together form a "
                 "straight angle. So ∠BOA + ∠BOC = 180°. Thus, these angles have to be 90° each.",
                 "This shows that the diagonals of a square bisect each other at right angles.",
                 "Using this fact, construct a square with a diagonal of length 8 cm.",
                 "Verify if this is true by going through geometric reasoning in Deduction 1 and Deduction 2, and "
                 "see if they apply to a square as well."],
       teach=["Predict first: the carpenter now wants a square. Which angle should the two strips make?",
              "A square is a rectangle, so the strips must still be equal and joined at their midpoints.",
              "In ∆BOA and ∆BOC: BA = BC, OA = OC, and BO is shared, so SSS makes them congruent.",
              "∠BOA = ∠BOC and together they make 180°, so each is 90°: the strips must cross at right angles."],
       examples=[
           WE("Construct a square with a diagonal of 8 cm.",
              ["Draw AC = 8 cm and mark its midpoint O, so OA = OC = 4 cm.",
               "Draw the line through O perpendicular to AC.",
               "On it mark B and D on opposite sides of O with OB = OD = 4 cm.",
               "Join A, B, C and D in order.",
               "The diagonals are equal, bisect each other and meet at 90°, so ABCD is a square."],
              "ABCD, with diagonals AC = BD = 8 cm crossing at right angles at their midpoints, is the square",
              ncert=["4.1.square_construct"])],
       ncert=["4.1.carpenter_square", "4.1.ded5"],
       key_terms=["SSS", "perpendicular", "straight angle"], misconceptions=["M_MEASURE_PROVES"], minutes=10),
     A("T4.C3", "The diagonals of a square bisect its angles", "Apply",
       "Students list the properties of a square and show that each diagonal splits a corner of the square into "
       "two angles of 45°.",
       textbook=["Since a square is a special type of rectangle, all the properties of a rectangle hold true for a "
                 "square.",
                 "Property 1: All the sides of a square are equal to each other. Property 2: The opposite sides of a "
                 "square are parallel to each other. Property 3: The angles of a square are all 90°. Property 4: The "
                 "diagonals of a square are of equal length and they bisect each other at 90°.",
                 "What are the measures of the four angles made by the diagonals at the corners? In ∆ADC, the "
                 "two angles at A and C together with the right angle at D make 180°. Since AD = DC, the angles "
                 "at A and C are equal. Thus, each is 45°.",
                 "Property 5: The diagonals of a square bisect the angles of the square."],
       teach=["Predict first: a diagonal cuts a corner of a square into two parts. Are the parts equal?",
              "∆ADC has a right angle at D and two equal sides AD and DC, so its other two angles are equal.",
              "Those two angles share 180° − 90° = 90°, so each is 45°.",
              "Every corner splits into 45° and 45°: the diagonals bisect the angles of a square."],
       examples=[
           WE("In square ABCD the diagonal AC is drawn. Find ∠DAC and ∠DCA.",
              ["In ∆ADC the angle at D is a right angle, so ∠DAC and ∠DCA share 180 − 90 = 90.",
               "AD = DC, so the angles opposite them are equal: ∠DAC = ∠DCA.",
               "So each is 90 ÷ 2 = 45."],
              "∠DAC = ∠DCA = 45°, so the diagonal bisects the right angles", ncert=["4.1.angles45"])],
       ncert=["4.1.square_props"],
       key_terms=["bisect", "isosceles right triangle"], misconceptions=["M_SQUARE_NOT_RECT"], minutes=8),
     DOER("T4.C4", "Practice: find and build squares", "square_in_square", "Apply",
          "Students recognise squares from their diagonals, construct a square from its diagonal without a "
          "protractor, and show that joining the midpoints of a square's sides gives a square.",
          ["A square is a rectangle with all sides equal.",
           "Its diagonals are equal and bisect each other at 90°.",
           "Each diagonal bisects the corner angles into 45°."],
          items=[
              FIO("FiO1.q3", "Figure it Out (rectangles and squares, question 3)",
                  "Consider a circle with centre O. Line segments PL and AM are two perpendicular diameters of the "
                  "circle. What is the figure APML? Reason and/or experiment to figure this out.",
                  ["AM and PL are the diagonals of APML.",
                   "Both are diameters, so they are equal.",
                   "Both pass through the centre O and OA = OM = OP = OL (radii), so they bisect each other.",
                   "They are perpendicular, so they meet at 90°.",
                   "Equal diagonals that bisect each other at 90° make a square."],
                  "APML is a square"),
              FIO("FiO3.q6", "Figure it Out (kites and trapeziums, question 6)",
                  "Construct a square with diagonal 6 cm without using a protractor.",
                  ["Draw AB = 6 cm.",
                   "With the compass open more than 3 cm, draw arcs from A and from B on both sides of AB; join "
                   "the two crossing points. This line is perpendicular to AB through its midpoint O.",
                   "With the compass set to 3 cm and centre O, mark C and D on this line on opposite sides of AB.",
                   "Join A, C, B and D in order.",
                   "The diagonals are 6 cm each, bisect each other and meet at 90°, so ACBD is a square."],
                  "ACBD is the square, with diagonals AB = CD = 6 cm"),
              FIO("FiO3.q7", "Figure it Out (kites and trapeziums, question 7)",
                  "CASE is a square. The points U, V, W and X are the midpoints of the sides of the square. What "
                  "type of quadrilateral is UVWX? Find this by using geometric reasoning, as well as by construction "
                  "and measurement. Find other ways of constructing a square within a square such that the vertices "
                  "of the inner square lie on the sides of the outer square.",
                  ["At each corner of CASE the two half sides are equal and the corner angle is 90°.",
                   "So the four corner triangles are congruent by SAS, and UV = VW = WX = XU.",
                   "Each corner triangle is isosceles and right-angled, so its base angles are 45° each.",
                   "On a side, the two 45° angles and the angle of UVWX make a straight angle: 180 − 45 − 45 = 90.",
                   "UVWX has four equal sides and four right angles, so it is a square.",
                   "Marking four points the same distance from each corner, all going the same way round, again "
                   "gives four congruent right triangles and so another square."],
                  "UVWX is a square; any four points at the same distance from the corners, taken the same way "
                  "round, also make a square")])],
    key_terms=["square", "diagonal", "Venn diagram"]))
