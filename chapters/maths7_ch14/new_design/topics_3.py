# -*- coding: utf-8 -*-
"""Topics T8 to T10 (module M3: regular hexagons, 60°, 120°, 30° and 15°, the six-pointed star). Book section 6.1."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T8 Hexagon from six triangles ================================================
TOPICS.append(TOPIC(
    "T8", "M3", "A Regular Hexagon from Six Triangles", ["6.1"], "Analyze",
    "Students explain why six congruent equilateral triangles fit round a point with no gap and no overlap, find a "
    "missing gap angle from the 360° total, and explain why opposite corners of the hexagon lie on straight lines "
    "through the centre.",
    "Angles round a point add to 360°; six 60° angles fill it, so six equilateral triangles make a regular hexagon.",
    [A("T8.C1", "Six equilateral triangles round a point", "Understand",
       "Students explain why six congruent equilateral triangles placed round a centre make a hexagon with equal "
       "sides and angles of 120°.",
       textbook=["Regular Hexagons",
                 "Recall that a regular polygon has equal sides and equal angles. A regular polygon with 3 sides is an "
                 "equilateral triangle, and a regular polygon with 4 sides is a square. We have constructed these "
                 "figures earlier.",
                 "Constructing a regular hexagon is within our reach! Can we break a regular hexagon into smaller "
                 "pieces that can be constructed?",
                 "Regular Hexagon and Equilateral Triangles",
                 "What happens when we join the 'opposite' points of a regular hexagon? Since a regular hexagon has "
                 "equal sides and angles, can we expect a figure like this? Will all the triangles in the figure be "
                 "equilateral triangles?",
                 "To answer these questions, we will reverse our approach. Can six congruent equilateral triangles "
                 "be placed together as in the figure? If yes, will it result in a regular hexagon?",
                 "If six congruent equilateral triangles can indeed be placed as shown in the figure, then the sides "
                 "of the resulting hexagon are equal, and their angles are 60 + 60 = 120° (how?). So what we really "
                 "need to examine is whether 6 congruent equilateral triangles can fit this way without overlapping "
                 "and without leaving any gaps around the centre.",
                 "We have defined a degree by taking the complete angle around a point to be 360°. So all the angles "
                 "around the centre should add up to 360°.",
                 "Since each angle in an equilateral triangle is 60°, six such angles add up to 360°. Therefore, six "
                 "congruent triangles can be arranged as shown."],
       teach=["Predict first: how many equilateral triangles fit round one point without a gap?",
              "Each angle of an equilateral triangle is 60°, and 6 × 60 = 360, the full turn.",
              "The outer sides are all sides of congruent triangles, so they are equal.",
              "At each corner of the hexagon two triangle angles meet: 60° + 60° = 120°."],
       examples=[
           WE("Six congruent equilateral triangles are placed round a centre O. Do they fit with no gap and no "
              "overlap, and is the outer figure a regular hexagon?",
              ["Each angle of an equilateral triangle is 60°.",
               "At O, six such angles meet, and 6 × 60 = 360, the complete angle round a point.",
               "So the six triangles fit round O with no gap and no overlap.",
               "The six outer sides are sides of congruent triangles, so they are all equal.",
               "At each outer corner, two angles of 60° meet, making 120°. So all six angles are equal.",
               "Equal sides and equal angles: the outer figure is a regular hexagon."],
              "Yes: six 60° angles make 360°, so they fit; the hexagon has equal sides and every angle is 120°",
              ncert=["6.1.hex_triangles"])],
       key_terms=["regular hexagon", "equilateral triangle"], misconceptions=["M_HEX_ANGLE_60"], minutes=10),
     A("T8.C2", "Angles round a point add to 360°", "Apply",
       "Students find the gap left by six angles round a point using the 360° total, and decide whether a 70° "
       "angle fits it.",
       textbook=["Consider this figure. Will the 70° angle fit into the gap? What is the gap angle ∠AOI?",
                 "We have, 40° + 60° + 50° + 30° + 40° + 90° + gap angle = 360°.",
                 "Use this to determine whether the 70° angle fits the gap.",
                 "Thus, if there are angles that add up to 360°, their vertices can be joined together at a single "
                 "point such that (a) the angles do not overlap, and (b) they completely cover the region around "
                 "the point."],
       teach=["Predict first: the gap looks a little smaller than a 70° wedge. Is looking enough?",
              "Add the six known angles: 40° + 60° + 50° + 30° + 40° + 90° = 310°.",
              "The gap is what is left of 360°: 360° − 310° = 50°.",
              "A 70° angle is bigger than the 50° gap, so it does not fit; it would overlap."],
       examples=[
           WE("Angles of 40°, 60°, 50°, 30°, 40° and 90° are placed round a point O, leaving a gap ∠AOI. Find the "
              "gap angle. Will a 70° angle fit into the gap?",
              ["All the angles round a point add up to 360°.",
               "40° + 60° + 50° + 30° + 40° + 90° + gap angle = 360°.",
               "The six known angles add to 310°.",
               "So the gap angle is 360° − 310° = 50°.",
               "70° is more than 50°, so the 70° angle would overlap its neighbours."],
              "The gap is 50°, so the 70° angle does not fit",
              ncert=["6.1.gap_360"])],
       key_terms=["complete angle"], misconceptions=["M_GAP_GUESS"], minutes=8),
     A("T8.C3", "Opposite corners lie on straight lines", "Analyze",
       "Students explain why AOD, BOE and COF are straight lines in the hexagon made of six equilateral triangles.",
       textbook=["Can you explain why AOD, BOE and COF are straight lines?"],
       teach=["Predict first: from A through O to D, how many 60° angles are passed at O?",
              "Going round O from OA to OD passes three triangles: 60° + 60° + 60° = 180°.",
              "An angle of 180° is a straight angle, so A, O and D lie on one straight line.",
              "The same holds for B, O, E and for C, O, F."],
       examples=[
           WE("In a regular hexagon ABCDEF made of six equilateral triangles round the centre O, explain why AOD, "
              "BOE and COF are straight lines.",
              ["At O, ∠AOB, ∠BOC and ∠COD are angles of equilateral triangles, so each is 60°.",
               "∠AOD = ∠AOB + ∠BOC + ∠COD = 60° + 60° + 60° = 180°.",
               "An angle of 180° is a straight angle, so OA and OD point in opposite directions: AOD is a straight "
               "line.",
               "In the same way ∠BOE = 180° and ∠COF = 180°.",
               "So BOE and COF are straight lines too."],
              "Each of ∠AOD, ∠BOE and ∠COF is three 60° angles, which is 180°, a straight angle",
              ncert=["6.1.straight_lines"])],
       key_terms=["straight angle"], minutes=8),
     DOER("T8.C4", "Practice: close the gap round a point", "gap_closer", "Apply",
          "Students fit angle wedges round a point, find each missing gap from the 360° total, and test which wedge "
          "fills it exactly.",
          ["Angles round a point add up to 360°.",
           "The gap is 360° minus the sum of the angles already placed.",
           "Six 60° wedges fill the full turn exactly, which is why six equilateral triangles make a hexagon."])]))

# ============================== T9 60 and 120 degrees, hexagon construction =================================
TOPICS.append(TOPIC(
    "T9", "M3", "Constructing 60°, 120° and a Regular Hexagon", ["6.1"], "Apply",
    "Students construct a 60° angle with two equal arcs and explain it with an equilateral triangle, build 120° "
    "from two 60° angles, and construct regular hexagons of side 4 cm and 5 cm.",
    "Two arcs of one radius make an equilateral triangle, so they give 60°; two 60° angles give 120°.",
    [A("T9.C1", "Construct a 60° angle", "Apply",
       "Students construct a 60° angle at A on a segment AX with two equal arcs, and explain that triangle ABC is "
       "equilateral.",
       textbook=["We can construct a regular hexagon more directly if we can construct a 120° angle using a ruler "
                 "and a compass. How do we do it? This can be done if we can construct a 60° angle.",
                 "Construction of a 60° angle",
                 "How do we construct a 60° angle? We get a 60° angle if we construct an equilateral triangle! We can "
                 "use the following steps for this.",
                 "Suppose we need a 60° angle at point A on a line segment AX.",
                 "Step 1: Construct an arc with centre A and any radius. (It cuts AX at B.)",
                 "Step 2: With the same radius, cut another arc from B that meets the first arc. Let C be the point "
                 "at which the arcs meet. We have ∠CAX = 60°.",
                 "Why is ∠CAX = 60°? Is there an equilateral triangle here?"],
       teach=["Predict first: which triangle has every angle equal to 60°?",
              "An arc with centre A cuts AX at B; an arc of the same radius from B meets it at C.",
              "AB = AC (radii from A) and BA = BC (radii from B), so all three sides are equal.",
              "ABC is equilateral, so each angle is 60°, and ∠CAX = ∠CAB = 60°."],
       examples=[
           WE("Construct a 60° angle at A on a segment AX using only a ruler and a compass, and explain why it is "
              "60°.",
              ["With centre A and any radius, draw a long arc that cuts AX at B.",
               "With centre B and the same radius, draw an arc that cuts the first arc at C.",
               "Join A and C. ∠CAX is the required angle.",
               "Join B and C. AB = AC, because both are radii of the first arc.",
               "BA = BC, because both are radii of the second arc, which has the same radius.",
               "So AB = BC = CA: ΔABC is equilateral, and each of its angles is 60°. So ∠CAX = 60°."],
              "∠CAX = 60°, because ΔABC has three equal sides and so is equilateral",
              ncert=["6.1.angle_60"])],
       key_terms=["equilateral triangle"], misconceptions=["M_SAME_RADIUS_ALL"], minutes=10),
     A("T9.C2", "120° and regular hexagons of a given side", "Apply",
       "Students construct a 120° angle as two 60° angles, and construct regular hexagons of side 4 cm and 5 cm "
       "with a ruler and a compass.",
       textbook=["If we construct this (60°), we also get this (120°).",
                 "Construct a regular hexagon with a sidelength 4 cm using a ruler and a compass.",
                 "We can use these ideas to construct a regular hexagon. Construct a regular hexagon of sidelength "
                 "5 cm."],
       teach=["Predict first: a 60° angle sits on a straight line. What is the angle next to it on the line?",
              "60° next to it on a straight line leaves 180° − 60° = 120°; or put two 60° angles side by side.",
              "A regular hexagon is six equilateral triangles round a centre, so a circle with radius equal to the "
              "side carries all six corners.",
              "Step the compass, set to the side length, six times round the circle; it closes exactly."],
       examples=[
           WE("Construct a 120° angle at a point A on a line, using only a ruler and a compass.",
              ["Draw a line and mark A on it. Mark X on the line to the right of A.",
               "With centre A and any radius, draw a large arc that cuts AX at B.",
               "With centre B and the same radius, cut the arc at C. Then ∠CAB = 60°.",
               "With centre C and the same radius, cut the arc again at D. Then ∠DAC = 60°, by the same "
               "equilateral triangle reason.",
               "Join A and D. ∠DAX = 60° + 60° = 120°.",
               "Check: D lies on the side away from X, and the angle between AD and the line on the left is "
               "180° − 120° = 60°."],
              "∠DAX = 120°, made of two 60° angles from equilateral triangles",
              ncert=["6.1.angle_120"]),
           WE("Construct a regular hexagon with side 4 cm using a ruler and a compass.",
              ["Open the compass to 4 cm using the ruler, and draw a circle with centre O.",
               "Mark a point A on the circle.",
               "With centre A and radius 4 cm, cut the circle at B. ΔOAB is equilateral, so ∠AOB = 60°.",
               "With centre B, cut the circle at C; with centre C, cut at D; then E and F in the same way.",
               "Six angles of 60° at O make 360°, so the sixth step lands back on A.",
               "Join A, B, C, D, E, F in order. Every side is 4 cm and every angle is 60° + 60° = 120°."],
              "ABCDEF, with six sides of 4 cm and six angles of 120°",
              ncert=["6.1.hex_4cm"]),
           WE("Construct a regular hexagon with side 5 cm using the 120° construction at each corner.",
              ["Draw AB = 5 cm with the ruler.",
               "At B, construct 120° between BA and a new ray: two 60° steps with equal arcs. Cut the ray at C with "
               "BC = 5 cm.",
               "At C, construct 120° in the same way, turning the same direction, and cut CD = 5 cm.",
               "Repeat at D and E to get E and F with DE = EF = 5 cm.",
               "Join F to A. The angles of a regular hexagon add to 6 × 120 = 720 degrees, and FA comes out 5 cm.",
               "All six sides are 5 cm and all six angles are 120°."],
              "ABCDEF, with six sides of 5 cm and six angles of 120°",
              ncert=["6.1.hex_5cm"])],
       key_terms=["regular hexagon"], misconceptions=["M_HEX_ANGLE_60"], minutes=15),
     DOER("T9.C3", "Practice: build 60°, 120° and hexagons", "sixty_bench", "Apply",
          "Students construct 60° and 120° angles with equal arcs, explain each with an equilateral triangle, and "
          "construct regular hexagons of a given side.",
          ["Two arcs of the same radius, one from A and one from where it cuts the arm, make an equilateral triangle.",
           "Two 60° angles side by side make 120°.",
           "The side length, stepped six times round a circle of the same radius, closes the hexagon."])]))

# ============================== T10 30, 15, star, perpendicular from a point =================================
TOPICS.append(TOPIC(
    "T10", "M3", "30°, 15° and the Six-Pointed Star", ["6.1"], "Apply",
    "Students construct 30° and 15° by bisecting 60° and 30°, construct a six-pointed star and justify that its "
    "points are equilateral triangles, and drop a perpendicular from a point outside a line.",
    "Halving 60° gives 30° and 15°; a hexagon's 120° angles make the star's points equilateral.",
    [A("T10.C1", "Construct 30° and 15°", "Apply",
       "Students construct a 30° angle by bisecting a constructed 60° angle, and a 15° angle by bisecting 30°, "
       "naming the SSS reason for each bisection.",
       textbook=["Related Constructions", "Construction of 30° and 15° angles",
                 "How will you construct 30° and 15° angles?"],
       teach=["Predict first: which angle that we can already construct is twice 30°?",
              "Construct 60° with two equal arcs; bisect it to get 30°.",
              "Bisect 30° to get 15°.",
              "Each bisection is exact because of SSS."],
       examples=[
           WE("Construct a 30° angle at a point A on a line, using only a ruler and a compass.",
              ["With centre A and any radius, draw an arc that cuts the line at B.",
               "With centre B and the same radius, cut the arc at C. Then ∠CAB = 60° (ΔABC is equilateral).",
               "Now bisect ∠CAB: with one radius, draw arcs from B and from C that meet at D inside the angle.",
               "Join A and D.",
               "AB = AC, BD = CD and AD is common, so ΔABD ≅ ΔACD by SSS.",
               "So ∠DAB = ∠DAC, and each is half of 60°, which is 30°."],
              "∠DAB = 30°: a 60° angle from an equilateral triangle, bisected (SSS)",
              ncert=["6.1.angle_30"]),
           WE("Construct a 15° angle at a point A on a line, using only a ruler and a compass.",
              ["Construct ∠CAB = 60° with two equal arcs, and bisect it to get the ray AD with ∠DAB = 30°.",
               "The first arc from A cuts AD at a point E. Then AB = AE.",
               "With one radius, draw arcs from B and from E that meet at F inside ∠DAB.",
               "Join A and F.",
               "AB = AE, BF = EF and AF is common, so ΔABF ≅ ΔAEF by SSS.",
               "So ∠FAB is half of 30°, which is 15°."],
              "∠FAB = 15°: 60° bisected to 30°, then bisected again (SSS each time)",
              ncert=["6.1.angle_15"])],
       key_terms=["bisect"], misconceptions=["M_ANY_ANGLE_BISECT"], minutes=12),
     A("T10.C2", "The six-pointed star", "Analyze",
       "Students construct a six-pointed star from a regular hexagon and justify that each of its six points is an "
       "equilateral triangle by finding its angles.",
       textbook=["6-Pointed Star",
                 "Construct the following 6-pointed star. Note that it has a rotational symmetry.",
                 "Hint: Do you see a hexagon here?",
                 "Are the six triangles forming the 6 points of the star, ΔAGH, ΔBHI, ΔCIJ, ΔDJK, ΔELK, ΔFLG, "
                 "equilateral? Why? [Hint: Find the angles.]"],
       teach=["Predict first: the middle of the star is a hexagon GHIJKL. What is each of its angles?",
              "Construct a regular hexagon GHIJKL and extend each side both ways.",
              "Each angle of the hexagon is 120°; the angle next to it on a straight line is 180° − 120° = 60°.",
              "Each point triangle has two 60° base angles, so its third angle is 60° too: it is equilateral."],
       examples=[
           WE("A six-pointed star has outer points A, B, C, D, E, F and an inner regular hexagon GHIJKL. Are the six "
              "point triangles ΔAGH, ΔBHI, ΔCIJ, ΔDJK, ΔELK and ΔFLG equilateral? Why?",
              ["The inner figure GHIJKL is a regular hexagon, so each of its angles is 120°.",
               "In ΔAGH, side GH is a side of the hexagon, and AG and AH lie along the extended sides LG and IH.",
               "∠AGH and ∠LGH make a straight angle, so ∠AGH = 180° − 120° = 60°.",
               "In the same way ∠AHG = 180° − 120° = 60°.",
               "The angles of a triangle add to 180°, so ∠GAH = 180° − 60° − 60° = 60°.",
               "All three angles are 60°, so ΔAGH is equilateral; the same reasoning works for the other five "
               "points."],
              "Yes. Each base angle is 180° − 120° = 60°, so all three angles are 60° and each point is an "
              "equilateral triangle",
              ncert=["6.1.star"])],
       key_terms=["rotational symmetry"], misconceptions=["M_HEX_ANGLE_60"], minutes=12),
     DOER("T10.C3", "Practice: special angles and perpendiculars", "outside_perp", "Apply",
          "Students build 30° and 15° by bisection, construct the star, and drop perpendiculars from points outside "
          "a line by finding a segment whose perpendicular bisector passes through the point.",
          ["Bisect 60° for 30°, and 30° for 15°.",
           "The star's points are equilateral because the hexagon's angles are 120°.",
           "From a point P outside a line, one arc cuts the line at two points equally far from P."],
          items=[
              FIO("6.1.FiO_perp_outside", "Figure it Out (special angles), Q4",
                  "Draw a line l and mark a point P anywhere outside the line. Construct a perpendicular to the given "
                  "line l through P. [Hint: Find a line segment on l whose perpendicular bisector passes through P.]",
                  ["With centre P and a radius large enough, draw an arc that cuts l at two points X and Y. Then "
                   "PX = PY.",
                   "P is equally far from X and Y, so P lies on the perpendicular bisector of XY.",
                   "With centres X and Y and one radius, draw arcs on the other side of l that meet at Q. Then "
                   "QX = QY.",
                   "Join P and Q; PQ meets l at O.",
                   "ΔPXQ ≅ ΔPYQ by SSS, so ∠XPO = ∠YPO; then ΔPOX ≅ ΔPOY by SAS, so ∠POX = ∠POY = 90°.",
                   "So PQ is the perpendicular to l through P."],
                  "Cut l at X and Y with an arc from P, then find Q with QX = QY; PQ is the perpendicular bisector of "
                  "XY (SSS, then SAS), so it is perpendicular to l and passes through P",
                  tool="outside_perp"),
          ])]))
