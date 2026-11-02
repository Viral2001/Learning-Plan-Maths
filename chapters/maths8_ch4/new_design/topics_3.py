# -*- coding: utf-8 -*-
"""Topics T9 to T13: playing with quadrilaterals, kites, trapeziums and the family (M5), and the summary (M6).
Book pp 103 to 111."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T9 Playing with quadrilaterals ================================================
TOPICS.append(TOPIC(
    "T9", "M5", "Playing with Quadrilaterals", ["4.5"], "Analyze",
    "Students build quadrilaterals from given diagonals on a geoboard and by joining two copies of a triangle, "
    "name each quadrilateral they get, and justify the name from its sides, angles or diagonals.",
    "The diagonals decide the quadrilateral: equal diagonals that bisect each other at right angles give a square, "
    "and unequal ones a rhombus. Two copies of a triangle joined along a side give a parallelogram when one is "
    "turned half round, and a kite when one is flipped over.",
    [A("T9.C1", "Quadrilaterals on a geoboard", "Analyze",
       "Students place equal perpendicular diagonals on a geoboard, name the quadrilateral, then lengthen one "
       "diagonal and name the new quadrilateral, justifying each from the diagonal properties.",
       textbook=["4.5 Playing with Quadrilaterals",
                 "Geoboard Activity: Take a geoboard and some rubber bands. If you do not have these, you could just "
                 "use the dot grid papers given at the end of the book for this activity.",
                 "Place two rubber bands perpendicular to each other, forming diagonals of equal length. Join the "
                 "ends. What is the quadrilateral that you get? Justify your answer.",
                 "Extend one of the diagonals on both sides by 2 cm. What quadrilateral will you get now? Justify "
                 "your answer."],
       teach=["Predict first: two equal rubber bands cross at right angles at their midpoints. What shape do their "
              "ends make?",
              "The diagonals are equal, bisect each other and meet at 90°, so the shape is a square.",
              "Now stretch one band 2 cm further at each end. Its midpoint stays at the crossing point.",
              "The diagonals still bisect each other at 90° but are no longer equal: the shape is a rhombus, not a "
              "square."],
       examples=[
           WE("Two rubber bands of 4 cm cross at right angles at their midpoints. Name the quadrilateral their ends "
              "make, and name it again after one band is extended by 2 cm at each end.",
              ["The diagonals are equal and bisect each other, so the quadrilateral is a rectangle.",
               "They also meet at 90°, so all four sides are equal: it is a square.",
               "The extended band is now 2 + 4 + 2 = 8 cm long and still has its midpoint at the crossing.",
               "The diagonals still bisect each other at 90°, so all four sides are equal, but the diagonals are "
               "4 cm and 8 cm, so it is not a rectangle."],
              "First a square; after extending one diagonal, a rhombus", ncert=["4.5.geoboard"])],
       key_terms=["geoboard", "diagonal", "square", "rhombus"],
       misconceptions=["M_DIAG_PERP_RHOMBUS", "M_ONE_NAME"], minutes=8),
     A("T9.C2", "Joining two triangles", "Analyze",
       "Students join two copies of an equilateral triangle and two copies of an isosceles triangle in every "
       "possible way and name each quadrilateral they get.",
       textbook=["Joining Triangles",
                 "1. Take two cardboard cutouts of an equilateral triangle of sidelength 8 cm. Can you join them to "
                 "get a quadrilateral? What type of a quadrilateral is this? Justify your answer.",
                 "2. Take two cardboard cutouts of an isosceles triangle with sidelengths 8 cm, 8 cm, and 6 cm. What "
                 "are the different ways they can be joined to get a quadrilateral?",
                 "What quadrilaterals are these? Justify your answers."],
       teach=["Predict first: two identical triangles are placed side by side along a common side. Which "
              "quadrilaterals can you get?",
              "Two equilateral triangles of 8 cm give four sides of 8 cm: a rhombus.",
              "Two 8, 8, 6 triangles joined along the 6 cm side give four sides of 8 cm: again a rhombus.",
              "Joined along an 8 cm side, one copy turned half round gives a parallelogram with sides 8, 6, 8, 6; "
              "one copy flipped over gives a kite with sides 8, 8, 6, 6."],
       examples=[
           WE("Join two copies of the triangle with sides 8 cm, 8 cm and 6 cm in different ways and name the "
              "quadrilaterals.",
              ["Along the 6 cm side: the four outer sides are all 8 cm, so the quadrilateral is a rhombus.",
               "Along an 8 cm side, with one copy turned half round: the outer sides are 8, 6, 8 and 6 cm, opposite "
               "sides are equal, so it is a parallelogram.",
               "Along an 8 cm side, with one copy flipped over: two neighbouring sides are 8 cm and the other two "
               "are 6 cm, so it is a kite.",
               "Two equilateral triangles of 8 cm, joined in the same way, give four sides of 8 cm: a rhombus."],
              "A rhombus, a parallelogram and a kite; two equilateral triangles give a rhombus",
              ncert=["4.5.join_equilateral", "4.5.join_isosceles"])],
       key_terms=["equilateral triangle", "isosceles triangle", "kite"], misconceptions=["M_ONE_NAME"],
       minutes=8),
     A("T9.C3", "Joining two scalene triangles", "Analyze",
       "Students find all six ways of joining two 6 cm, 9 cm, 12 cm triangles and sort them into parallelograms and "
       "kites.",
       textbook=["3. Take two cardboard cutouts of a scalene triangle with sides 6 cm, 9 cm, and 12 cm.",
                 "What are the different ways they can be joined to get a quadrilateral? Are you able to identify "
                 "the different quadrilaterals that are obtained by joining the triangles? Justify your answer "
                 "whenever you identify a quadrilateral."],
       teach=["Predict first: how many different quadrilaterals can two copies of a 6, 9, 12 triangle make?",
              "There are three sides to join along, and two ways to join along each: turned half round or flipped "
              "over.",
              "Turned half round always gives a parallelogram: 9, 12, 9, 12 or 6, 12, 6, 12 or 6, 9, 6, 9.",
              "Flipped over always gives two pairs of equal neighbouring sides, a kite. Only the kite flipped over "
              "the 12 cm side is the usual shape; the other two cave in at one corner."],
       examples=[
           WE("Two copies of a triangle with sides 6 cm, 9 cm and 12 cm are joined along a side. List the "
              "quadrilaterals you can get.",
              ["Along the 6 cm side, turned half round: sides 9, 12, 9 and 12, a parallelogram.",
               "Along the 9 cm side, turned half round: sides 6, 12, 6 and 12, a parallelogram.",
               "Along the 12 cm side, turned half round: sides 6, 9, 6 and 9, a parallelogram.",
               "Flipped over the 12 cm side: sides 6, 6, 9 and 9 with equal neighbours, a kite.",
               "Flipped over the 6 cm or the 9 cm side: again two pairs of equal neighbouring sides, a kite, but one "
               "that caves in at a corner."],
              "Three parallelograms and three kites; only the kite on the 12 cm side has no corner that caves in",
              ncert=["4.5.join_scalene"])],
       key_terms=["scalene triangle", "kite", "parallelogram"], minutes=6, thin=True),
     DOER("T9.C4", "Practice: build quadrilaterals from diagonals and triangles", "diagonal_lab", "Apply",
          "Students build quadrilaterals from their diagonals and from pairs of triangles and name every family "
          "each one belongs to.",
          ["Diagonals that bisect each other give a parallelogram.",
           "Equal ones give a rectangle, perpendicular ones a rhombus, all three a square.",
           "Two equal triangles joined along a side give a parallelogram or a kite."],
          items=[
              FIO("FiO3.q1", "Figure it Out (kites and trapeziums, question 1)",
                  "Find all the sides and the angles of the quadrilateral obtained by joining two equilateral "
                  "triangles with sides 4 cm.",
                  ["Each side of the quadrilateral is a side of an equilateral triangle, so all four sides are "
                   "4 cm.",
                   "Each angle of an equilateral triangle is 60.",
                   "The two corners not on the joined side are single triangle angles: 60 each.",
                   "The two corners on the joined side are made of two triangle angles: 60 + 60 = 120 each.",
                   "Check: 60 + 120 + 60 + 120 = 360."],
                  "All sides are 4 cm; the angles are 60°, 120°, 60° and 120°, a rhombus")])],
    key_terms=["diagonal", "kite", "rhombus"]))

# ============================== T10 The kite =================================================================
TOPICS.append(TOPIC(
    "T10", "M5", "The Kite", ["4.6"], "Analyze",
    "Students define a kite, prove that its main diagonal bisects two of its angles and is the perpendicular "
    "bisector of the other diagonal, and construct a kite from its diagonals.",
    "A kite has two pairs of equal neighbouring sides. Its diagonal between the equal pairs bisects the angles at "
    "its ends and cuts the other diagonal in half at right angles.",
    [A("T10.C1", "The diagonals of a kite", "Analyze",
       "Students define a kite and prove by the SSS and SAS conditions that its diagonal BD bisects ∠ABC and ∠ADC "
       "and is the perpendicular bisector of AC.",
       textbook=["4.6 Kite and Trapezium",
                 "One of the ways the two triangles of sides 6 cm, 9 cm and 12 cm can be joined together is as "
                 "follows. This quadrilateral looks like a kite. Observe that the adjacent sides are of the same "
                 "length.",
                 "Kite: A kite is a quadrilateral that can be labelled ABCD such that AB = BC, and CD = DA.",
                 "Property 1: In the kite, show that the diagonal BD (i) bisects ∠ABC and ∠ADC, (ii) bisects the "
                 "diagonal AC, that is, AO = OC, and is perpendicular to it.",
                 "Hint: Is ∆AOB ≅ ∆COB?"],
       teach=["Predict first: in a kite, does either diagonal cut the other in half? At what angle do they meet?",
              "A kite ABCD has AB = BC and CD = DA: two pairs of equal neighbouring sides.",
              "∆ABD ≅ ∆CBD by SSS, so BD bisects ∠ABC and ∠ADC.",
              "Then ∆AOB ≅ ∆COB by SAS, so AO = OC and the two angles at O are equal; they make 180°, so each is "
              "90°."],
       examples=[
           WE("ABCD is a kite with AB = BC and CD = DA, and its diagonals meet at O. Show that BD bisects ∠ABC and "
              "that BD is perpendicular to AC with AO = OC.",
              ["In ∆ABD and ∆CBD: AB = CB, AD = CD, and BD is common, so ∆ABD ≅ ∆CBD by SSS.",
               "So ∠ABD = ∠CBD: BD bisects ∠ABC (and likewise ∠ADC).",
               "In ∆AOB and ∆COB: AB = CB, ∠ABO = ∠CBO, and BO is common, so ∆AOB ≅ ∆COB by SAS.",
               "So AO = OC, and ∠AOB = ∠COB.",
               "These two angles make a straight angle of 180, so each is 180 ÷ 2 = 90."],
              "BD bisects ∠ABC and ∠ADC, and it cuts AC in half at right angles", ncert=["4.6.kite_prop"])],
       ncert=["4.6.kite_def"],
       key_terms=["kite", "perpendicular bisector", "SSS", "SAS"],
       misconceptions=["M_KITE_RHOMBUS", "M_DIAG_PERP_RHOMBUS"], minutes=10),
     DOER("T10.C2", "Practice: construct a kite from its diagonals", "kite_slider", "Apply",
          "Students construct a kite from the lengths of its diagonals using the perpendicular bisector property.",
          ["A kite has two pairs of equal neighbouring sides.",
           "One diagonal is the perpendicular bisector of the other.",
           "The other diagonal need not be bisected."],
          items=[
              FIO("FiO3.q2", "Figure it Out (kites and trapeziums, question 2)",
                  "Construct a kite whose diagonals are of lengths 6 cm and 8 cm.",
                  ["Draw AC = 6 cm and draw its perpendicular bisector, meeting AC at O.",
                   "On the bisector mark B 2 cm from O on one side and D 6 cm from O on the other side, so "
                   "BD = 2 + 6 = 8 cm.",
                   "Join A, B, C and D in order.",
                   "B and D lie on the perpendicular bisector of AC, so BA = BC and DA = DC: ABCD is a kite.",
                   "Splitting 8 cm as 4 cm and 4 cm would give a rhombus, which is a special kite."],
                  "ABCD with AC = 6 cm, BD = 8 cm, BD the perpendicular bisector of AC and O not the midpoint of BD")])],
    key_terms=["kite", "perpendicular bisector"]))

# ============================== T11 The trapezium ============================================================
TOPICS.append(TOPIC(
    "T11", "M5", "The Trapezium", ["4.6"], "Apply",
    "Students define a trapezium and an isosceles trapezium, find the remaining angles of a trapezium from co-interior "
    "angles, and prove by congruent triangles that the base angles of an isosceles trapezium are equal.",
    "A trapezium has at least one pair of parallel opposite sides, so the two angles along each non-parallel side "
    "add up to 180°. In an isosceles trapezium the angles opposite the equal sides are equal.",
    [A("T11.C1", "Trapeziums and their angles", "Apply",
       "Students define a trapezium and use co-interior angles to find its remaining angles from its base angles.",
       textbook=["Trapezium: Parallelograms are quadrilaterals that have parallel opposite sides. We get a new type "
                 "of quadrilateral if we relax this condition.",
                 "Trapezium: A trapezium is a quadrilateral with at least one pair of parallel opposite sides.",
                 "Construct a trapezium. Measure the base angles (marked in the figure). Can you find the remaining "
                 "angles without measuring them?",
                 "Since PQ||SR, we have Property 1: ∠S + ∠P = 180° and ∠R + ∠Q = 180°.",
                 "Using these facts, the remaining angles can easily be found. Verify your answer after finding them."],
       teach=["Predict first: a trapezium has base angles 70° and 55°. Can you find the top angles without "
              "measuring?",
              "A trapezium needs at least one pair of parallel opposite sides, so a parallelogram is a trapezium "
              "too.",
              "With PQ || SR, each slanting side is a transversal, so the two angles along it add up to 180°.",
              "So ∠S = 180° − ∠P and ∠R = 180° − ∠Q."],
       examples=[
           WE("Trapezium PQRS has PQ || SR, ∠P = 70° and ∠Q = 55°. Find ∠S and ∠R.",
              ["PS is a transversal to the parallel lines PQ and SR, so ∠S + ∠P = 180.",
               "So ∠S = 180 − 70 = 110.",
               "QR is a transversal too, so ∠R = 180 − 55 = 125.",
               "Check: 70 + 55 + 125 + 110 = 360."],
              "∠S = 110° and ∠R = 125°", ncert=["4.6.trap_prop1"])],
       ncert=["4.6.trap_def"],
       key_terms=["trapezium", "co-interior angles"], misconceptions=["M_TRAP_EXACTLY_ONE"], minutes=8),
     A("T11.C2", "The isosceles trapezium", "Analyze",
       "Students define an isosceles trapezium, prove with a rectangle and congruent right triangles that its base "
       "angles are equal, and find its other angles.",
       textbook=["When the non-parallel sides of a trapezium have the same lengths, the trapezium is called an "
                 "isosceles trapezium.",
                 "Construct an isosceles trapezium UVWX, with UV||XW. Measure ∠U. Can you find the remaining angles "
                 "without measuring them?",
                 "Consider line segments XY and WZ perpendicular to UV. What type of quadrilateral is XWZY?",
                 "Since XW||UV, a = 180° − ∠XYZ = 90°, and b = 180° − ∠WZY = 90°. Hence, XWZY is a rectangle.",
                 "Now, it can be shown that ∆UXY ≅ ∆VWZ. (How?) Thus, ∠U = ∠V.",
                 "Property 2: In an isosceles trapezium, the angles opposite to the equal sides are equal."],
       teach=["Predict first: in a trapezium whose slanting sides are equal, are the two base angles equal?",
              "Drop XY and WZ perpendicular to UV. XWZY has four right angles, so it is a rectangle and XY = WZ.",
              "∆UXY and ∆VWZ are right triangles with UX = VW and XY = WZ, so they are congruent by RHS.",
              "So ∠U = ∠V, and each top angle is 180° minus the base angle below it."],
       examples=[
           WE("UVWX is an isosceles trapezium with UV || XW, UX = VW and ∠U = 65°. Find ∠V, ∠W and ∠X.",
              ["Draw XY and WZ perpendicular to UV; XWZY is a rectangle, so XY = WZ.",
               "∆UXY and ∆VWZ have right angles at Y and Z, UX = VW and XY = WZ, so ∆UXY ≅ ∆VWZ by RHS.",
               "So ∠V = ∠U = 65.",
               "UX is a transversal to the parallel sides, so ∠X = 180 − 65 = 115, and likewise ∠W = 115."],
              "∠V = 65°, ∠W = 115°, ∠X = 115°", ncert=["4.6.iso_prop2"])],
       ncert=["4.6.iso_trap"],
       key_terms=["isosceles trapezium", "RHS"], misconceptions=["M_TRAP_EXACTLY_ONE"], minutes=10),
     DOER("T11.C3", "Practice: angles of trapeziums", "trapezium_slider", "Apply",
          "Students find the remaining angles of a trapezium from co-interior angles and of an isosceles trapezium "
          "from its equal base angles.",
          ["A trapezium has at least one pair of parallel opposite sides.",
           "The two angles along each slanting side add up to 180°.",
           "In an isosceles trapezium the base angles are equal."],
          items=[
              FIO("FiO3.q3", "Figure it Out (kites and trapeziums, question 3)",
                  "Find the remaining angles in the following trapeziums. (i) A trapezium with angles 105° and 135° "
                  "at the ends of one parallel side. (ii) An isosceles trapezium with an angle of 100°.",
                  ["(i) Each slanting side is a transversal to the parallel sides, so its two angles add up to 180.",
                   "The remaining angles are 180 − 105 = 75 and 180 − 135 = 45.",
                   "(ii) The slanting sides are equal, so the angles at the ends of the same parallel side are equal: "
                   "the other one next to 100 is also 100.",
                   "The angles below them are 180 − 100 = 80 each."],
                  "(i) 75° and 45°; (ii) 100°, 80° and 80°")])],
    key_terms=["trapezium", "isosceles trapezium"]))

# ============================== T12 The quadrilateral family =================================================
TOPICS.append(TOPIC(
    "T12", "M5", "The Quadrilateral Family", ["4.6"], "Evaluate",
    "Students place every kind of quadrilateral in one family diagram, give every name a figure deserves, and "
    "decide from given conditions on sides, angles or diagonals which family a quadrilateral must belong to.",
    "The families sit inside one another: squares are rectangles and rhombuses, rectangles and rhombuses are "
    "parallelograms, parallelograms are trapeziums, and rhombuses are kites. A condition decides a family only if "
    "it forces every property in that family's definition.",
    [A("T12.C1", "One quadrilateral, several names", "Understand",
       "Students draw the family diagram of quadrilaterals and give all the names that belong to a square and to a "
       "rhombus.",
       textbook=["Parallelogram, Kite, Trapezium, Rectangle, Square, Rhombus.",
                 "A kite is a quadrilateral with two non-overlapping adjacent pairs of sides having the same length.",
                 "A trapezium is a quadrilateral having at least one pair of parallel opposite sides."],
       teach=["Predict first: how many family names does a square have?",
              "A figure belongs to every family whose definition it meets.",
              "A square has parallel opposite sides, equal sides, right angles and equal neighbouring sides, so it "
              "is a parallelogram, a rectangle, a rhombus, a kite and a trapezium.",
              "In the family diagram, squares sit in the overlap of rectangles and rhombuses, inside parallelograms, "
              "inside trapeziums; rhombuses also sit inside kites."],
       examples=[
           WE("Give every family name that belongs to a square.",
              ["All its angles are 90°, so it is a rectangle.",
               "All its sides are equal, so it is a rhombus.",
               "Its opposite sides are parallel, so it is a parallelogram, and so also a trapezium.",
               "Its neighbouring sides are equal in two pairs, so it is a kite."],
              "A square is a rectangle, a rhombus, a parallelogram, a trapezium and a kite")],
       key_terms=["family diagram", "Venn diagram"],
       misconceptions=["M_ONE_NAME", "M_SQUARE_NOT_RECT", "M_TRAP_EXACTLY_ONE"], minutes=8),
     A("T12.C2", "Deciding the family from the diagonals", "Evaluate",
       "Students prove that diagonals that bisect each other at right angles always make a rhombus, and check "
       "whether a condition is enough to decide a family.",
       textbook=["The diagonals of a rhombus bisect each other at right angles.",
                 "A quadrilateral whose diagonals are perpendicular to each other must be a rhombus. (State whether "
                 "this is true or false.)"],
       teach=["Predict first: the diagonals of a quadrilateral bisect each other at right angles. Must it be a "
              "rhombus?",
              "The four triangles at the crossing have two equal half-diagonals and a right angle between them.",
              "SAS makes them congruent, so all four sides are equal: a rhombus.",
              "But perpendicular diagonals alone are not enough: a kite has them and is not always a rhombus."],
       examples=[
           WE("The diagonals AC and BD of ABCD bisect each other at O at right angles. Show that ABCD is a rhombus.",
              ["OA = OC and OB = OD, because the diagonals bisect each other.",
               "The four angles at O are each 90.",
               "In ∆AOB and ∆COB: OA = OC, ∠AOB = ∠COB, and OB is common, so they are congruent by SAS and AB = CB.",
               "In the same way BC = CD and CD = DA.",
               "All four sides are equal, so ABCD is a rhombus."],
              "ABCD is a rhombus")],
       key_terms=["rhombus", "SAS", "counterexample"],
       misconceptions=["M_DIAG_PERP_RHOMBUS", "M_KITE_RHOMBUS"], minutes=8),
     DOER("T12.C3", "Practice: sort quadrilaterals into the family", "hierarchy_sorter", "Evaluate",
          "Students sort figures into the family rings and decide, with reasons, which conditions force which "
          "family.",
          ["A figure belongs to every family whose definition it meets.",
           "Squares are rectangles and rhombuses; rhombuses are parallelograms and kites.",
           "A condition decides a family only if it forces that family's definition."],
          items=[
              FIO("FiO3.q4", "Figure it Out (kites and trapeziums, question 4)",
                  "Draw a Venn diagram showing the set of parallelograms, kites, rhombuses, rectangles, and squares. "
                  "Then, answer the following questions. (i) What is the quadrilateral that is both a kite and a "
                  "parallelogram? (ii) Can there be a quadrilateral that is both a kite and a rectangle? (iii) Is "
                  "every kite a rhombus? If not, what is the correct relationship between these two types of "
                  "quadrilaterals?",
                  ["Draw parallelograms holding rectangles and rhombuses, with squares in their overlap; draw kites "
                   "overlapping parallelograms exactly in the rhombuses.",
                   "(i) A parallelogram has opposite sides equal; a kite has neighbouring sides equal in pairs, so "
                   "all four sides are equal: a rhombus (squares included).",
                   "(ii) A kite that is a rectangle has equal neighbouring sides and opposite sides equal, so all "
                   "sides are equal and all angles 90°: a square.",
                   "(iii) No. A kite can have sides 6, 6, 9 and 9, which is not a rhombus. Every rhombus is a kite."],
                  "(i) A rhombus; (ii) Yes, a square; (iii) No; every rhombus is a kite, but not every kite is a "
                  "rhombus"),
              FIO("FiO3.q8", "Figure it Out (kites and trapeziums, question 8)",
                  "If a quadrilateral has four equal sides and one angle of 90°, will it be a square? Find the "
                  "answer using geometric reasoning as well as by construction and measurement.",
                  ["Four equal sides make it a rhombus, so it is a parallelogram.",
                   "Adjacent angles of a parallelogram add up to 180, so the neighbours of 90 are 180 − 90 = 90.",
                   "The opposite angle equals 90 too, so all four angles are 90.",
                   "Four equal sides and four right angles make a square."],
                  "Yes, it is a square"),
              FIO("FiO3.q11", "Figure it Out (kites and trapeziums, question 11)",
                  "State whether the following statements are true or false. Justify your answers. (i) A "
                  "quadrilateral whose diagonals are equal and bisect each other must be a square. (ii) A "
                  "quadrilateral having three right angles must be a rectangle. (iii) A quadrilateral whose "
                  "diagonals bisect each other must be a parallelogram. (iv) A quadrilateral whose diagonals are "
                  "perpendicular to each other must be a rhombus. (v) A quadrilateral in which the opposite angles "
                  "are equal must be a parallelogram. (vi) A quadrilateral in which all the angles are equal is a "
                  "rectangle. (vii) Isosceles trapeziums are parallelograms.",
                  ["(i) False: such diagonals give a rectangle, which need not be a square.",
                   "(ii) True: the fourth angle is 360 − 270 = 90.",
                   "(iii) True: the triangles at the crossing are congruent in opposite pairs, giving equal alternate "
                   "angles, so opposite sides are parallel.",
                   "(iv) False: a kite has perpendicular diagonals but need not be a rhombus.",
                   "(v) True: with angles x, y, x, y we get 2x + 2y = 360, so neighbouring angles add up to 180 and "
                   "opposite sides are parallel.",
                   "(vi) True: each angle is 360 ÷ 4 = 90.",
                   "(vii) False: its slanting sides are not parallel, unless it is a rectangle."],
                  "(i) False (ii) True (iii) True (iv) False (v) True (vi) True (vii) False")])],
    key_terms=["family diagram", "kite", "trapezium", "parallelogram"]))

# ============================== T13 Summary and Which Quad? ==================================================
TOPICS.append(TOPIC(
    "T13", "M6", "Summary: Quadrilaterals", ["Summary", "Puzzle Time"], "Remember",
    None,
    "Rectangles, squares, parallelograms, rhombuses, kites and trapeziums with their properties, the angle sum of "
    "360°, and the Which Quad? folding puzzle.",
    [A("T13.C1", "What we found about quadrilaterals", "Remember",
       "Students restate the definition and properties of each kind of quadrilateral and the angle sum of a "
       "quadrilateral.",
       textbook=["A rectangle is a quadrilateral in which the angles are all 90°. Opposite sides of a rectangle are "
                 "equal and parallel; its diagonals are of equal length and they bisect each other.",
                 "A square is a quadrilateral in which all the angles are 90°, and all the sides are of equal length. "
                 "The diagonals of a square are of equal lengths, bisect each other at 90° and bisect its angles.",
                 "A parallelogram is a quadrilateral in which opposite sides are parallel. Its opposite sides are "
                 "equal, adjacent angles add up to 180°, opposite angles are equal, and its diagonals bisect each "
                 "other.",
                 "A rhombus is a quadrilateral in which all the sides have the same length. Its diagonals bisect each "
                 "other at right angles and bisect its angles.",
                 "A kite is a quadrilateral with two non-overlapping adjacent pairs of sides having the same length.",
                 "A trapezium is a quadrilateral having at least one pair of parallel opposite sides.",
                 "The sum of the angle measures in a quadrilateral is 360°."],
       teach=["Our carpenter's problem is settled: two equal strips joined at their midpoints, at any angle, make a "
              "rectangle, and at right angles a square.",
              "Each family has its properties: parallelograms have equal opposite sides and diagonals that bisect "
              "each other, rhombuses add perpendicular diagonals, kites have one diagonal bisecting the other at "
              "90°, and trapeziums need one pair of parallel sides.",
              "The families nest inside one another, the angles of every quadrilateral add up to 360°, and every "
              "property we used was proved, not just measured."],
       ncert=["summary"], video_focus=["RECAP"], minutes=8),
     A("T13.C2", "Which Quad?", "Apply",
       "Students predict the quadrilateral made by the creases of a folded sheet and work out how to fold for nested "
       "rhombuses and for a square.",
       textbook=["Puzzle Time: Which Quad?",
                 "1. Fold a sheet into half. 2. Now, fold it once more into a quarter. 3. Make a triangular crease at "
                 "the corner that is at the middle of the paper. 4. Open the sheet. What is the shape formed by the "
                 "creases?",
                 "5. How would you fold the quarter paper to get the kinds of creases shown in the following image.",
                 "6. How would you fold the quarter paper such that a square is formed?"],
       teach=["Predict first: a sheet folded into quarters gets one slanting crease across the middle corner. What "
              "shape appears when you open it?",
              "The two folds are lines of symmetry, so the crease is copied in all four quarters.",
              "The four copies are equal, so the shape has four equal sides: a rhombus, whose diagonals lie along "
              "the two folds.",
              "Several parallel creases give rhombuses inside one another; a crease that cuts equal lengths on both "
              "folds gives equal diagonals, so a square."],
       examples=[
           WE("A sheet is folded in half and then into a quarter, and one slanting crease is made across the corner "
              "at the middle of the sheet. What shape do the creases make, and how should you fold to get a square?",
              ["The two folds cross at right angles at the centre of the sheet.",
               "Unfolding copies the crease into all four quarters, so the shape has four equal sides.",
               "Its diagonals lie along the folds, so they bisect each other at right angles: a rhombus.",
               "Several creases parallel to the first give rhombuses inside one another.",
               "If the crease cuts off equal lengths along both folds, the diagonals are equal too, and the rhombus "
               "is a square."],
              "A rhombus; fold the crease at 45°, cutting equal lengths on both folds, to get a square",
              ncert=["puzzle"])],
       key_terms=["line of symmetry", "rhombus", "square"], enrichment=True, minutes=6)],
    topic_type="summary"))
