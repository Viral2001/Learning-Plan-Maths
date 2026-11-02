# -*- coding: utf-8 -*-
"""Topics T5 to T7 (module M2: bisecting an angle, copying an angle, the parallel line). Book section 6.1."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T5 Bisecting an angle =========================================================
TOPICS.append(TOPIC(
    "T5", "M2", "Bisecting an Angle", ["6.1"], "Apply",
    "Students bisect any angle with equal arcs and justify it with SSS, construct a 45° angle by bisecting a right "
    "angle, and use it for an eight-petal design.",
    "Equal arcs from the vertex, then equal arcs from the two marks, give two triangles congruent by SSS.",
    [A("T5.C1", "Steps to bisect an angle, and why they work", "Apply",
       "Students bisect a given angle ∠XOY by marking OA = OB and a point C with AC = BC, and justify that OC is the "
       "bisector by the SSS congruence condition.",
       textbook=["We will now develop a general method to bisect any angle. Consider an angle ∠XOY.",
                 "We can bisect it if we can draw two congruent triangles ΔOBC and ΔOAC as shown in the figure. Then "
                 "∠BOC = ∠AOC.",
                 "How do we construct these congruent triangles, given the angle?",
                 "If A and B are marked such that OA = OB, and if C is chosen such that BC = AC, then by the SSS "
                 "congruence condition, ΔOBC ≅ ΔOAC. So we can bisect an angle as follows.",
                 "Steps for Angle Bisection",
                 "1. Mark points A and B such that OA = OB.",
                 "2. Choosing any sufficiently long radius, cut arcs from A and B, keeping the radius same. Mark the "
                 "point of intersection as C.",
                 "3. OC bisects ∠AOB."],
       teach=["Predict first: to cut ∠XOY into two equal parts, which two triangles would you want to be congruent?",
              "Step 1: with centre O, draw an arc that cuts OY at A and OX at B, so OA = OB.",
              "Step 2: with one radius, draw arcs from A and from B that meet at C, so AC = BC.",
              "Step 3: join OC. ΔOAC ≅ ΔOBC by SSS, so ∠AOC = ∠BOC: OC bisects the angle."],
       examples=[
           WE("Draw any angle ∠XOY. Bisect it using only a ruler and a compass, and justify that the two parts are "
              "equal.",
              ["With centre O and any radius, draw an arc that cuts OY at A and OX at B. Then OA = OB.",
               "With centre A and a radius long enough for the arcs to meet, draw an arc inside the angle.",
               "With centre B and the same radius, draw an arc that cuts it at C. Then AC = BC.",
               "Join O and C.",
               "In ΔOAC and ΔOBC: OA = OB, AC = BC, and OC is common. So ΔOAC ≅ ΔOBC by SSS.",
               "So ∠AOC = ∠BOC, and OC bisects ∠XOY."],
              "OC bisects ∠XOY, because ΔOAC ≅ ΔOBC by SSS",
              ncert=["6.1.bisect_method"])],
       key_terms=["angle bisector", "SSS"], misconceptions=["M_ARC_RADIUS_CHANGE"], minutes=10),
     A("T5.C2", "A 45° angle and the eight-petal design", "Apply",
       "Students explain why eight equally spaced lines make 45° angles, and construct a 45° angle by bisecting a "
       "constructed 90° angle.",
       textbook=["Angle Bisection for a Design",
                 "How do we construct this figure? (Eight equal petals meet at one centre.)",
                 "The supporting lines for this figure will look like this.",
                 "What is the angle between two adjacent lines?",
                 "We need the angle between every pair of adjacent lines to be equal. Since 360° is equally divided "
                 "into 8 parts, every angle is 45°.",
                 "How do we construct a 45° angle using only a ruler and a compass?",
                 "We know how to construct a 90° angle. If we can divide it into two equal parts, or bisect it, then "
                 "we get a 45° angle.",
                 "So, a 45° angle can be constructed by first constructing a 90° angle and then bisecting it."],
       teach=["Predict first: eight lines from one centre, all equally spaced. What angle is between neighbours?",
              "The full turn of 360° split into 8 equal angles gives 45° each.",
              "Construct 90° at a point on a line, then bisect it to get 45°.",
              "Two perpendicular lines and their two bisectors give the eight supporting lines."],
       examples=[
           WE("Eight equal petals meet at a centre, along eight equally spaced supporting lines. Find the angle "
              "between neighbouring lines, and construct it with a ruler and a compass.",
              ["The eight angles round the centre are equal and make a full turn of 360°.",
               "The full turn of 360° shared by 8 equal angles gives 45° each.",
               "Draw a line and mark the centre O on it. Construct a 90° angle at O with equal arcs.",
               "Bisect the 90° angle: arcs from O cut the two arms at A and B, then equal arcs from A and B meet at "
               "C. OC makes 45° with each arm (SSS).",
               "Extend the two arms and the bisector through O, and bisect one more right angle; this gives four "
               "lines, which is eight half-lines from O at 45° to each other."],
              "Each angle is 45°; construct 90° and bisect it",
              ncert=["6.1.bisect_45"])],
       key_terms=["bisect"], misconceptions=["M_ANGLE_ARM_LENGTH"], minutes=10),
     DOER("T5.C3", "Practice: bisect angles and build designs", "angle_halver", "Apply",
          "Students bisect angles of different sizes, build angles such as 45° and 22.5° by repeated halving, and "
          "decide which angles halving can and cannot reach.",
          ["OA = OB from the vertex, AC = BC from the two marks: ΔOAC ≅ ΔOBC by SSS.",
           "Halving 90° gives 45°, then 22.5°; once 60° is built later, halving it gives 30°, then 15°.",
           "Halving only reaches angles of a special kind; 65.5° is not one of them."],
          items=[
              FIO("6.1.FiO_ab1", "Figure it Out (angle bisection), Q1",
                  "Construct at least 4 different angles. Draw their bisectors.",
                  ["Draw four angles of clearly different sizes, for example a small acute angle, a right angle "
                   "made with equal arcs, a large acute angle and an obtuse angle.",
                   "For each angle with vertex O: with centre O draw an arc that cuts the arms at A and B, so "
                   "OA = OB.",
                   "With one radius, draw arcs from A and from B that meet at C inside the angle.",
                   "Join OC. It is the bisector, because ΔOAC ≅ ΔOBC by SSS.",
                   "Check: fold the paper along OC; the two arms land on each other."],
                  "Each bisector is OC, where OA = OB and AC = BC; ΔOAC ≅ ΔOBC by SSS, so the two halves are equal",
                  tool="angle_halver"),
              FIO("6.1.FiO_ab3", "Figure it Out (angle bisection), Q3",
                  "In Step 2 of angle bisection, if arcs of equal radius are drawn on the other side, so that "
                  "the arcs from A and B meet at a point C on the far side of the vertex O, outside the "
                  "angle, will the line OC still be an angle bisector? Explore this through construction, and then "
                  "justify your answer.",
                  ["Mark A and B on the arms with OA = OB.",
                   "With a radius larger than OA, draw equal arcs from A and B on the far side of O; they meet at C, "
                   "with AC = BC.",
                   "In ΔOAC and ΔOBC: OA = OB, AC = BC, and OC is common.",
                   "So ΔOAC ≅ ΔOBC by SSS, and ∠AOC = ∠BOC.",
                   "Extend CO beyond O to a point D inside ∠AOB. ∠AOD and ∠AOC make a straight angle, and so do "
                   "∠BOD and ∠BOC.",
                   "So ∠AOD = 180° − ∠AOC and ∠BOD = 180° − ∠BOC; these are equal, so the line CO, extended beyond "
                   "O, bisects ∠AOB."],
                  "Yes. OA = OB, AC = BC and OC is common, so ΔOAC ≅ ΔOBC by SSS and ∠AOC = ∠BOC; their supplements "
                  "are equal too, so the line CO, extended beyond O, still bisects ∠AOB",
                  tool="angle_halver"),
              FIO("6.1.FiO_ab4", "Figure it Out (angle bisection), Q4",
                  "What are the other angles that can be constructed using angle bisection? Can you construct 65.5° "
                  "angle?",
                  ["From 180° by halving: 90°. From 90° by halving: 45°, 22.5°, and so on.",
                   "Sums of these also work, for example 90° + 45° = 135° and 45° + 22.5° = 67.5°.",
                   "Every angle made this way, doubled enough times, becomes a whole multiple of 45°.",
                   "65.5° doubled is 131°, and every further doubling is 131° times a power of 2, which is never a "
                   "multiple of 45°, because 131 is not divisible by 3 or by 5.",
                   "So 65.5° cannot be constructed by bisection.",
                   "Later in this chapter we build a 60° angle; halving it gives 30° and 15°, and sums such as 75°. "
                   "Those all double into multiples of 15°, and 131° times a power of 2 is not one of them either."],
                  "Angles such as 90°, 45°, 22.5°, 135° and 67.5° can be made (and, once 60° is built, 30°, 15° and "
                  "75°); 65.5° cannot, because no number of doublings turns it into a multiple of 45°, or even of 15°",
                  tool="angle_halver"),
              FIO("6.1.FiO_ab6", "Figure it Out (angle bisection), Q6",
                  "Construct the following figure: a square with four equal petals inside it, each petal running "
                  "from the centre of the square to one corner. How do we construct the petals so that they are of "
                  "the maximum possible size within a given square?",
                  ["Construct a square: a segment, right angles at both ends, equal sides cut with the compass, and "
                   "join the fourth side.",
                   "Find the midpoint of each side by constructing its perpendicular bisector.",
                   "The two bisectors through opposite midpoints cross at the centre of the square.",
                   "With centre the midpoint of one side and radius half the side, draw a semicircle inside the "
                   "square. It passes through the two corners at the ends of that side and through the centre.",
                   "Do the same from the other three midpoints. Each petal is where two semicircles overlap, from "
                   "the centre to a corner.",
                   "These arcs just touch the sides of the square at the corners, so the petals are as large as "
                   "they can be."],
                  "Find the midpoints of the four sides; from each midpoint draw a semicircle of radius half the "
                  "side inside the square; the four petals run from the centre to the corners and are the largest "
                  "possible"),
          ])]))

# ============================== T6 Copying an angle ============================================================
TOPICS.append(TOPIC(
    "T6", "M2", "Copying an Angle", ["6.1"], "Apply",
    "Students copy any angle to a new position with equal arcs and a transferred chord, justify the copy with SSS, "
    "and see why repeating units need copied angles.",
    "Equal arcs and an equal chord make two triangles congruent by SSS, so the copied angle is equal.",
    [A("T6.C1", "Steps to copy an angle", "Apply",
       "Students copy a given angle at A onto a ray from X by drawing equal arcs and transferring the chord BC, and "
       "justify ∠A = ∠X by the SSS congruence condition.",
       textbook=["Repeating Units and Repeating Angles",
                 "Consider a design made of a row of five equal sectors (shapes with two equal straight arms and an "
                 "arc), alternately pointing down and up, with neighbouring sectors sharing an arm. In this design, "
                 "there is a single unit repeating itself. To construct this figure, we need to make "
                 "exact copies of this unit in two different orientations.",
                 "In order to make exact copies, all the units must have the same arm lengths and the same angle "
                 "between the arms. We can ensure equal arm lengths using a compass, but how do we ensure equal "
                 "angles?",
                 "Let us develop a method to create an exact copy of a given angle.",
                 "Draw an angle. Create a copy of this angle using only a ruler and compass.",
                 "Steps of Construction to Copy an Angle",
                 "Draw an arc from A. This gives us three points that form the isosceles triangle ΔABC.",
                 "Draw an arc of the same radius from X.",
                 "Measure BC using a compass. Transfer this length on the arc from Z to get YZ = BC.",
                 "By the SSS congruence condition, ΔABC ≅ ΔXYZ. So, ∠A = ∠X."],
       teach=["Predict first: what must match, besides the arm lengths, for a copy to have the same angle?",
              "With centre A, draw an arc that cuts the arms at B and C.",
              "Draw a ray from X. With centre X and the same radius, draw an arc that cuts the ray at Z.",
              "Open the compass to BC. With centre Z, cut the arc at Y. Join XY. ΔABC ≅ ΔXYZ by SSS, so ∠X = ∠A."],
       examples=[
           WE("An angle with vertex A is drawn. Copy it onto a ray from a point X using only a ruler and a compass, "
              "and justify that the copy is equal.",
              ["With centre A and any radius, draw an arc that cuts the two arms at B and C. Then AB = AC.",
               "Draw a ray from X. With centre X and the same radius, draw a long arc that cuts the ray at Z. Then "
               "XZ = AB.",
               "Open the compass to the length BC.",
               "With centre Z and radius BC, cut the arc at Y. Then YZ = BC and XY = AC.",
               "Join X and Y.",
               "In ΔABC and ΔXYZ: AB = XZ, AC = XY, BC = ZY. So ΔABC ≅ ΔXYZ by SSS, and ∠YXZ = ∠CAB."],
              "∠YXZ is a copy of ∠A, because ΔABC ≅ ΔXYZ by SSS",
              ncert=["6.1.copy_steps"])],
       key_terms=["copy of an angle", "SSS"], misconceptions=["M_ARC_RADIUS_CHANGE", "M_ANGLE_ARM_LENGTH"],
       minutes=10),
     DOER("T6.C2", "Practice: copy angles in any orientation", "angle_copier", "Apply",
          "Students copy angles of different sizes and orientations onto new rays without measuring, and check each "
          "copy by SSS.",
          ["Use the same radius at the old vertex and the new vertex.",
           "Transfer the chord with the compass; never measure it with a scale.",
           "SSS makes the two triangles congruent, so the angles are equal."],
          items=[
              FIO("6.1.FiO_ca1", "Figure it Out (copying an angle), Q1",
                  "Construct at least 4 different angles in different orientations without taking any measurement. "
                  "Make a copy of all these angles.",
                  ["Draw four angles with the ruler only, each in a different direction on the page, for example one "
                   "opening upwards, one sideways, one downwards and one slanting.",
                   "For each angle with vertex A: draw an arc from A cutting the arms at B and C.",
                   "Draw a new ray from a point X, and with the same radius draw an arc from X cutting it at Z.",
                   "Open the compass to BC, and from Z cut the arc at Y. Join XY.",
                   "Each copy is equal because ΔABC ≅ ΔXYZ by SSS. Check by laying tracing paper over both."],
                  "For each angle, equal arcs from A and X and the chord BC moved to ZY give ΔABC ≅ ΔXYZ by SSS, so "
                  "every copy equals its angle",
                  tool="angle_copier"),
          ])]))

# ============================== T7 Parallel line ==============================================================
TOPICS.append(TOPIC(
    "T7", "M2", "A Line Parallel to a Given Line", ["6.1"], "Apply",
    "Students construct a line through a given point parallel to a given line by copying the corresponding angle "
    "made by a transversal, and justify it.",
    "Copy the angle a transversal makes with m at a point B on the transversal; equal corresponding angles give "
    "parallel lines.",
    [A("T7.C1", "Copy a corresponding angle to draw a parallel line", "Apply",
       "Students draw a transversal l through a point B and a line m, copy the angle at A to B as a corresponding "
       "angle, and explain why the new line n is parallel to m.",
       textbook=["This procedure to copy an angle finds an important application in constructing parallel lines "
                 "using only a ruler and compass.",
                 "Construction of a Line Parallel to the Given Line",
                 "Recall that we constructed equal corresponding angles to get parallel lines.",
                 "How do we implement this idea using a ruler and a compass?",
                 "Suppose there is a line m to which we need to draw a parallel line. We construct a line l that "
                 "intersects m. Line l will serve as a transversal to line m and to the line parallel to m that we "
                 "are going to construct.",
                 "Let us choose a point B on l through which we are going to draw the parallel line. This parallel "
                 "line must make the same corresponding angle, as shown in the figure. This can be done by copying "
                 "the angle between m and l.",
                 "Construct arcs of equal radius from A and B. Transfer the length CD to the arc from F (F is where the arc from B cuts l). These steps "
                 "give a method to construct a line parallel to the given line."],
       teach=["Predict first: a transversal crosses two lines. Which angles must be equal for the lines to be "
              "parallel?",
              "Draw a line l through B that cuts m at A. The angle a between m and l at A is the one to copy.",
              "Equal arcs from A and from B; the chord CD at A is transferred to the arc at B, giving E.",
              "The line n through B and E makes the same corresponding angle a, so n is parallel to m."],
       examples=[
           WE("A line m and a point B not on it are given. Construct a line through B parallel to m using only a "
              "ruler and a compass.",
              ["Draw a line l through B that cuts m at A. l is the transversal.",
               "With centre A and any radius, draw an arc that cuts m at C and cuts l at D, on the part of l between A and B.",
               "With centre B and the same radius, draw an arc that cuts l at F, on the side of B away from A, as "
               "for the matching corner.",
               "Open the compass to CD. With centre F, cut the arc at E, on the same side of l as C.",
               "Draw the line n through B and E. ΔBFE ≅ ΔADC by SSS, so the angle at B equals the angle at A.",
               "These are corresponding angles, so n is parallel to m."],
              "The line n through B and E, since the copied corresponding angles are equal (SSS), so n ∥ m",
              ncert=["6.1.parallel_steps"])],
       key_terms=["transversal", "corresponding angles", "parallel"], misconceptions=["M_ARC_RADIUS_CHANGE"],
       minutes=10),
     DOER("T7.C2", "Practice: draw parallel lines", "parallel_builder", "Apply",
          "Students construct lines parallel to given lines through given points in different orientations, by "
          "copying the corresponding angle each time.",
          ["Any line through the point that cuts m can be the transversal.",
           "Copy the angle at the crossing point to the given point, as a corresponding angle.",
           "Equal corresponding angles make the lines parallel."],
          items=[
              FIO("6.1.FiO_pl1", "Figure it Out (parallel lines), Q1",
                  "Construct 4 pairs of parallel lines in different orientations.",
                  ["Draw four lines m in different directions: across, up and down, and two slanting ways.",
                   "For each, mark a point B off the line and draw a transversal l through B cutting m at A.",
                   "Equal arcs from A and B; the chord CD at A is transferred to the arc at B to give E.",
                   "Draw n through B and E. ΔADC ≅ ΔBFE by SSS, so the corresponding angles are equal.",
                   "So each n is parallel to its m."],
                  "Four pairs m and n, each made by copying the corresponding angle at A to B (SSS), so each n ∥ m",
                  tool="parallel_builder"),
          ])]))
