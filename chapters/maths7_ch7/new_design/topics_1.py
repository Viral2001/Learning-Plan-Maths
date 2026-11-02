# -*- coding: utf-8 -*-
"""Topics T1 to T6 (module M1: triangles from three lengths). Book sections 7.1 and 7.2 and the triangle inequality."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Introduction ==============================================================
TOPICS.append(TOPIC(
    "T1", "M1", "Three Corners and a Straight Line", ["Chapter opening"], "Understand",
    "",
    "Three corner points make a triangle, and one question stays open: what happens when the three points lie on a "
    "straight line?",
    [A("T1.C1", "A frame of three beams", "Remember",
       "",
       textbook=["A triangle is the most basic closed shape. As we know, it consists of:",
                 "three corner points, that we call the vertex of the triangle, and",
                 "three line segments or the sides of the triangle that join the pairs of vertices.",
                 "Triangles come in various shapes.",
                 "Observe the symbol used to denote a triangle and how the triangles are named using their vertices. "
                 "While naming a triangle, the vertices can come in any order.",
                 "The three sides meeting at the corners give rise to three angles that we call the angles of the "
                 "triangle. For example, in ∆ABC, these angles are ∠CAB, ∠ABC, ∠BCA, which we simply denote as ∠A, "
                 "∠B and ∠C, respectively."],
       teach=["Picture three wooden beams of a shed roof, nailed together at their ends to make a triangle frame. "
              "The three nails are the corners, called vertices, and the beams are the sides.",
              "Make a guess before the next step: if the top nail is pressed down until all three nails lie on one "
              "straight line, do we still have a triangle?",
              "A triangle can be named with its vertices in any order: ∆ABC, ∆BCA and ∆CAB are the same triangle. "
              "Its angles are ∠A, ∠B and ∠C."],
       ncert=["opening"], key_terms=["vertex"], video_focus=["HOOK"], minutes=4, enrichment=True),
     A("T1.C2", "The question to keep: three points on a line", "Understand", "",
       textbook=["What happens when the three vertices lie on a straight line?"],
       teach=["Predict: when the three corners lie on one straight line, how many sides can you see?",
              "Keep this question in mind: the next topics build triangles from lengths and from angles, and "
              "ask each time when the triangle cannot be built."],
       ncert=["opening.collinear"], enrichment=True)],
    topic_type="framing"))

# ============================== T2 Equilateral triangles =======================================================
TOPICS.append(TOPIC(
    "T2", "M1", "Equilateral Triangles with Ruler and Compass", ["7.1"], "Apply",
    "Students construct a triangle with all sides 4 cm, first with a ruler alone and then with a compass, and "
    "explain why the point where two arcs cross is at the right distance from both ends of the base.",
    "A ruler alone needs many trials to place the third corner; two arcs of the same radius from the two ends of "
    "the base find it at once.",
    [A("T2.C1", "Building with a ruler alone", "Understand",
       "Students describe the ruler-only method for a triangle with all sides 4 cm and say why it needs many trials.",
       textbook=["7.1 Equilateral Triangles",
                 "Among all the triangles, the equilateral triangles are the most symmetric ones. These are "
                 "triangles in which all the sides are of equal lengths. Let us try constructing them.",
                 "Construct a triangle in which all the sides are of length 4 cm.",
                 "How did you construct this triangle and what tools did you use? Can this construction be done "
                 "only using a marked ruler (and a pencil)?",
                 "Constructing this triangle using just a ruler is certainly possible. But this might require "
                 "several trials. Say we draw the base, let us call it AB, of length 4 cm, and mark the third point "
                 "C using a ruler such that AC = 4 cm. This may not lead to BC also having a length of 4 cm. If "
                 "this happens, we will have to keep making attempts to mark C till we get BC to be 4 cm long.",
                 "How do we make this construction more efficient?"],
       teach=["Predict first: if AB = 4 cm and C is marked 4 cm from A, will BC also be 4 cm?",
              "An equilateral triangle has all three sides equal, so each side is 4 cm here.",
              "With a ruler alone, C is moved and measured again and again until both AC and BC are 4 cm: it "
              "works, but it takes several trials."],
       ncert=["7.1.ruler"], key_terms=["equilateral triangle"], minutes=6),
     A("T2.C2", "Two arcs find the third corner", "Apply",
       "Students construct an equilateral triangle with side 4 cm using two arcs of radius 4 cm and explain why C "
       "is 4 cm from both A and B.",
       textbook=["Recall solving a similar problem in the previous year using a compass (in the Chapter 'Playing "
                 "with Constructions'). We had to mark the top point of a 'house' which is 5 cm from two other "
                 "points. The method we used to get that point can also be used here.",
                 "After constructing AB = 4 cm, we can do the following.",
                 "Step 1: Using a compass, construct a sufficiently long arc of radius 4 cm from A. The point C is "
                 "somewhere on this arc. How do we mark it?",
                 "Step 2: Construct another arc of radius 4 cm from B. Let C be the point of intersection of the "
                 "arcs.",
                 "The construction ensures that both AC and BC are of length 4 cm. Can you see why?",
                 "Step 3: Join AC and BC to get the required equilateral triangle."],
       teach=["Predict first: every point on an arc of radius 4 cm from A is how far from A?",
              "The arc from A holds all the places that are 4 cm from A, and the arc from B holds all the places "
              "that are 4 cm from B. The point where they cross is on both, so it is 4 cm from each end."],
       examples=[
           WE("Construct a triangle in which all the sides are of length 4 cm, and explain why AC and BC are both "
              "4 cm.",
              ["Draw the base AB of length 4 cm.",
               "Step 1: with the compass set to 4 cm and the point on A, draw a long arc above the base.",
               "Step 2: keep the compass at 4 cm, put the point on B, and draw a second arc that crosses the "
               "first.",
               "Mark the crossing point C. It is on the arc from A, so AC = 4 cm, and on the arc from B, so "
               "BC = 4 cm.",
               "Step 3: join AC and BC. All three sides are 4 cm."],
              "An equilateral triangle ABC with AB = BC = CA = 4 cm", ncert=["7.1.compass"])],
       key_terms=["arc"], minutes=8),
     DOER("T2.C3", "Practice: build an equilateral triangle", None, "Apply",
          "Students construct an equilateral triangle of a chosen side length with a ruler and compass and check "
          "each side with the ruler.",
          ["Draw the base first.",
           "Use the same radius, equal to the side, for both arcs.",
           "The crossing point of the arcs is the third corner."])]))

# ============================== T3 Triangles from three sides ==================================================
TOPICS.append(TOPIC(
    "T3", "M1", "Triangles from Three Given Sides", ["7.2"], "Apply",
    "Students construct a triangle from three given side lengths with a ruler and compass, explain why the "
    "crossing point of two arcs is the third vertex, and name equilateral and isosceles triangles.",
    "Choose one length as the base, draw an arc of the second length from one end and an arc of the third length "
    "from the other end: the crossing point is the third vertex.",
    [A("T3.C1", "Constructing a triangle of sides 4, 5 and 6", "Apply",
       "Students construct a triangle with sides 4 cm, 5 cm and 6 cm and write the four steps of the "
       "construction.",
       textbook=["7.2 Constructing a Triangle When its Sides are Given",
                 "How do we construct triangles that are not equilateral?",
                 "Construct a triangle of sidelength 4 cm, 5 cm and 6 cm.",
                 "As in the previous case, this triangle can also be constructed using just a marked ruler. But it "
                 "will involve several trials.",
                 "How do we construct this triangle more efficiently?",
                 "Choose one of the given lengths to be the base of the triangle: say 4 cm. Draw the base. Let A "
                 "and B be the base vertices, and call the third vertex C. Let AC = 5 cm and BC = 6 cm.",
                 "Like we did in the case of equilateral triangles, let us first get all the points that are at a "
                 "5 cm distance from A. These points lie on the circle whose centre is A and has radius 5 cm. The "
                 "point C must lie somewhere on this circle. How do we find it?",
                 "We will make use of the fact that the point C is 6 cm away from B. Construct an arc of radius "
                 "6 cm from B.",
                 "Let us summarise the steps of construction, noting that constructing full circles is not "
                 "necessary to get the third vertex.",
                 "Step 1: Construct the base AB with one of the side lengths. Let us choose AB = 4 cm.",
                 "Step 2: From A, construct a sufficiently long arc of radius 5 cm.",
                 "Step 3: From B, construct an arc of radius 6 cm such that it intersects the first arc.",
                 "Step 4: The point where both the arcs meet is the required third vertex C. Join AC and BC to get "
                 "∆ABC."],
       teach=["Predict first: if C is 5 cm from A and 6 cm from B, how many arcs do we need to find it?",
              "The circle of radius 5 cm around A holds every point 5 cm from A; C must be one of them.",
              "The arc of radius 6 cm around B holds every point 6 cm from B; the crossing point is the only "
              "place that is 5 cm from A and 6 cm from B."],
       examples=[
           WE("Construct a triangle with sidelengths 4 cm, 5 cm and 6 cm.",
              ["Step 1: draw the base AB = 4 cm.",
               "Step 2: with the compass set to 5 cm and the point on A, draw a long arc above the base.",
               "Step 3: set the compass to 6 cm, put the point on B and draw an arc that crosses the first arc.",
               "Step 4: the crossing point is C. It is 5 cm from A and 6 cm from B. Join AC and BC.",
               "Check with the ruler: AB = 4 cm, AC = 5 cm, BC = 6 cm."],
              "Triangle ABC with AB = 4 cm, AC = 5 cm and BC = 6 cm", ncert=["7.2.build", "7.2.steps"])],
       key_terms=["base"], minutes=10),
     A("T3.C2", "Why the crossing point is the third vertex, and isosceles triangles", "Understand",
       "Students explain why the crossing point of the two arcs is at the right distance from both ends of the "
       "base, and construct a triangle with two equal sides.",
       textbook=["The required point C is one of the points of intersection of the two circles.",
                 "The reason why the point of intersection is the third vertex is the same as for equilateral "
                 "triangles. This point lies on both the circles. Hence its distance from A is the radius of the "
                 "circle centred at A (5 cm) and its distance from B is the same as the radius of the circle "
                 "centred at B (6 cm).",
                 "We have seen that triangles having all three equal sides are called equilateral triangles. Those "
                 "having two equal sides are called isosceles triangles."],
       teach=["Predict first: the two full circles cross in two points. Does either one give a triangle?",
              "Both crossing points are on both circles, so both give a triangle with the same three sides, one "
              "above the base and one below.",
              "A triangle with all three sides equal is equilateral. A triangle with two equal sides is isosceles. "
              "An equilateral triangle also has two equal sides."],
       examples=[
           WE("Construct a triangle with sidelengths 4 cm, 4 cm and 6 cm and say what kind of triangle it is.",
              ["Take the side of 6 cm as the base AB.",
               "From A draw an arc of radius 4 cm, and from B draw an arc of radius 4 cm. They cross at C.",
               "C is 4 cm from A and 4 cm from B, so AC = BC = 4 cm.",
               "Two sides are equal, so the triangle is isosceles."],
              "An isosceles triangle with sides 4 cm, 4 cm and 6 cm", ncert=["7.2.why", "7.2.iso"])],
       key_terms=["isosceles triangle"], minutes=8),
     DOER("T3.C3", "Practice: build triangles from three sides", "compass_triangle_builder", "Apply",
          "Students construct triangles from three given lengths, choose a base, set the compass to the other two "
          "lengths and name each triangle by its sides.",
          ["Choose a base, draw an arc of one length from each end, and join the crossing point to both ends.",
           "Equal radii give two equal sides.",
           "Three equal sides make an equilateral triangle, two equal sides make an isosceles triangle."],
          items=[
              FIO("7.2.construct", "Construct (triangles from three sides)",
                  "Construct triangles having the following sidelengths (all the units are in cm): (a) 4, 4, 6 "
                  "(b) 3, 4, 5 (c) 1, 5, 5 (d) 4, 6, 8 (e) 3.5, 3.5, 3.5. Say what kind of triangle each is.",
                  ["Each set satisfies the check: the two shorter lengths add to more than the longest "
                   "(4 + 4 > 6, 3 + 4 > 5, 1 + 5 > 5, 4 + 6 > 8, 3.5 + 3.5 > 3.5), so each triangle can be built.",
                   "For each set draw the longest side as the base, then an arc of one of the other lengths from "
                   "each end.",
                   "(a) 4, 4, 6 has two equal sides: isosceles. (b) 3, 4, 5 has three different sides: scalene. "
                   "(c) 1, 5, 5 has two equal sides: isosceles, with a very short base.",
                   "(d) 4, 6, 8 has three different sides: scalene. (e) 3.5, 3.5, 3.5 has three equal sides: "
                   "equilateral."],
                  "All five can be built: (a) isosceles, (b) scalene, (c) isosceles, (d) scalene, (e) equilateral",
                  tool="compass_triangle_builder"),
              FIO("7.2.FiOA1", "Figure it Out (equilateral and isosceles triangles), Q1",
                  "A circle is drawn with its centre marked, and some points are marked on the circle. Use the "
                  "points on the circle and/or the centre to form isosceles triangles.",
                  ["Mark the centre O and two points P and Q on the circle. Join OP, OQ and PQ.",
                   "OP and OQ are both radii of the same circle, so OP = OQ and triangle OPQ is isosceles.",
                   "Choosing P and Q so that PQ is also equal to the radius makes all three sides equal: an "
                   "equilateral triangle.",
                   "Three points on the circle can also give an isosceles triangle: take P and Q, then take R "
                   "halfway between them on the circle, so that RP = RQ."],
                  "Any two points on the circle with the centre give an isosceles triangle; two points whose "
                  "distance is one radius give an equilateral triangle", tool="compass_triangle_builder"),
              FIO("7.2.FiOA2", "Figure it Out (equilateral and isosceles triangles), Q2",
                  "Two circles of the same size have centres A and B, and each circle passes through the centre of "
                  "the other. Then three circles of the same size have centres A, B and C, and each circle passes "
                  "through the centres of the other two. Use the points on the circles and/or their centres to "
                  "form isosceles and equilateral triangles.",
                  ["Two circles: each passes through the other's centre, so the radius equals AB. Let C and D be "
                   "the two points where the circles cross.",
                   "C is on the circle at A, so AC = AB, and on the circle at B, so BC = AB. All three sides of "
                   "triangle ABC are equal: it is equilateral. In the same way triangle ABD is equilateral.",
                   "AC = AD because both are radii of the circle at A, so triangle ACD is isosceles; triangle BCD "
                   "is isosceles in the same way.",
                   "Three circles: A, B and C are the centres and every pair of centres is one radius apart, so "
                   "triangle ABC is equilateral. Each pair of circles crosses in two points, and each crossing "
                   "point together with those two centres gives another equilateral triangle.",
                   "Any point on a circle with the centre and another point on the same circle gives an isosceles "
                   "triangle, as in the single circle."],
                  "Triangles ABC and ABD are equilateral, and ACD and BCD are isosceles; with three circles "
                  "ABC is equilateral and each crossing point forms more equilateral triangles",
                  tool="compass_triangle_builder"),
          ])]))

# ============================== T4 Do three lengths always make a triangle ====================================
TOPICS.append(TOPIC(
    "T4", "M1", "Do Three Lengths Always Make a Triangle?", ["7.2"], "Analyze",
    "Students show that some sets of three lengths cannot make a triangle, compare a direct path with a "
    "roundabout path, and check a set of lengths with the three comparisons that define the triangle inequality.",
    "A direct path is always shorter than a roundabout path, so each side of a triangle must be shorter than the "
    "other two sides added together.",
    [A("T4.C1", "Lengths that fail: 3, 4, 8 and 2, 3, 6", "Analyze",
       "Students try to construct triangles with sidelengths 3, 4, 8 and 2, 3, 6, see that the arcs do not meet, "
       "and look for more sets that fail.",
       textbook=["Are Triangles Possible for any Lengths?",
                 "Can one construct triangles having any given sidelengths? Are there lengths for which it is "
                 "impossible to construct a triangle? Let us explore this.",
                 "Construct a triangle with sidelengths 3 cm, 4 cm, and 8 cm.",
                 "What is happening? Are you able to construct the triangle?",
                 "Here is another set of lengths: 2 cm, 3 cm, and 6 cm. Check if a triangle is possible for these "
                 "sidelengths.",
                 "Try to find more sets of lengths for which a triangle construction is impossible. See if you can "
                 "find any pattern in them.",
                 "We see that a triangle is possible for some sets of lengths and not possible for others. How do "
                 "we check if a triangle exists for a given set of lengths? One way is to actually try to "
                 "construct the triangle and check if it is possible. Is there a more efficient way to check "
                 "this?"],
       teach=["Predict first: with a base of 8 cm, can an arc of 3 cm from one end ever meet an arc of 4 cm from "
              "the other end?",
              "The two arcs reach only 3 cm and 4 cm from the two ends of an 8 cm base, which is 7 cm in all. "
              "They fall short and never cross, so there is no third vertex.",
              "The same happens for 2, 3 and 6: 2 + 3 = 5 is less than 6.",
              "Look for the pattern in other failing sets, such as 1, 2, 5 or 4, 5, 10: the two shorter lengths "
              "together are less than the longest."],
       examples=[
           WE("Try to construct a triangle with sidelengths 3 cm, 4 cm and 8 cm, then 2 cm, 3 cm and 6 cm, and say "
              "what happens to the arcs.",
              ["Take 8 cm as the base AB. Draw an arc of 3 cm from A and an arc of 4 cm from B.",
               "The arc from A reaches 3 cm along the base and the arc from B reaches 4 cm back, which covers "
               "3 + 4 = 7 cm of the 8 cm. They do not meet.",
               "For 2, 3 and 6, take 6 cm as the base. The arcs of 2 cm and 3 cm cover 2 + 3 = 5 cm of the 6 cm "
               "and do not meet.",
               "In both sets the two shorter lengths add to less than the longest: 3 + 4 = 7 < 8 and "
               "2 + 3 = 5 < 6."],
              "No triangle can be built for 3, 4, 8 or for 2, 3, 6: the arcs never meet",
              ncert=["imp.try", "imp.more"])],
       key_terms=[], misconceptions=["M_ANY_LENGTHS"], minutes=8),
     A("T4.C2", "A direct path and a roundabout path", "Understand",
       "Students compare a straight path with a path through a third point and state that the direct path is the "
       "shortest.",
       textbook=["Triangle Inequality",
                 "Consider the lengths 10 cm, 15 cm and 30 cm. Does there exist a triangle having these as "
                 "sidelengths?",
                 "To tackle this question, let us study a property of triangles. Imagine a small plot of plain "
                 "land having a tent, a tree, and a pole. Imagine you are at the entrance of the tent and want to "
                 "go to the tree. Which is the shorter path: (i) the straight-line path to the tree (the red "
                 "path) or (ii) the straight-line path from the tent to the pole, followed by the straight-line "
                 "path from the pole to the tree (the yellow path)?",
                 "Clearly, the direct straight-line path from the tent to the tree is shorter than the "
                 "roundabout path via the pole. In fact, the direct straight-line path is the shortest possible "
                 "path to the tree from the tent.",
                 "Will the direct path between any two points be shorter than the roundabout path via a third "
                 "point? Clearly, the answer is yes."],
       teach=["Predict first: on a plot, which is shorter, going straight from the tent to the tree or going "
              "from the tent to the pole and then to the tree?",
              "The straight path is the shortest possible path between two points. Going through a third point "
              "adds a bend, so the walk is longer, unless the pole lies on the straight path itself.",
              "Three points that are not on one line form a triangle. This gives the idea of the next concept: "
              "each side is a direct path, and the other two sides together are the roundabout path."],
       examples=[
           WE("A tent, a tree and a pole are the three corners of a plot. The tent to the tree is 30 m in a "
              "straight line, the tent to the pole is 20 m and the pole to the tree is 25 m. Which way is "
              "shorter?",
              ["Direct path from the tent to the tree: 30 m.",
               "Roundabout path from the tent to the pole and then to the tree: 20 m + 25 m = 45 m.",
               "30 m is less than 45 m, so the direct path is shorter.",
               "The same holds for every pair of the three corners: each direct path is shorter than the "
               "roundabout path through the third corner."],
              "The direct path of 30 m is shorter than the roundabout path of 45 m", ncert=["ti.path"])],
       key_terms=["direct path", "roundabout path"], minutes=8),
     A("T4.C3", "The triangle inequality: 10, 15, 30 and 3, 3, 7", "Analyze",
       "Students test lengths against the three direct-versus-roundabout comparisons and conclude that a triangle "
       "cannot exist when one comparison fails.",
       textbook=["Can this understanding be used to tell something about the existence of a triangle having "
                 "sidelengths 10 cm, 15 cm and 30 cm?",
                 "Let us suppose that there is a triangle for this set of lengths. Remember that at this point we "
                 "are not sure about the existence of the triangle but we are only supposing that it exists. Let "
                 "us draw a rough diagram.",
                 "If this triangle were possible, then the direct path between any two vertices should be shorter "
                 "than the roundabout path via the third vertex. Is this true for our rough diagram?",
                 "Let us consider the paths between B and C. Direct path length = BC = 10 cm. Roundabout path "
                 "length = BA + AC = 15 cm + 30 cm = 45 cm. Is the direct path length shorter than the roundabout "
                 "path length? Yes.",
                 "Let us now consider the paths between A and B. Direct path length = AB = 15 cm. Roundabout path "
                 "length = AC + CB = 30 cm + 10 cm = 40 cm. Is the direct path length shorter than the roundabout "
                 "path length? Yes.",
                 "Finally, consider paths between C and A. Direct path length = CA = 30 cm. Roundabout path "
                 "length = CB + BA = 10 cm + 15 cm = 25 cm. Is the direct path length shorter than the roundabout "
                 "path length? In this case, the direct path is longer, which is absurd. Can such a triangle "
                 "exist? No.",
                 "Therefore, a triangle having sidelengths 10 cm, 15 cm and 30 cm cannot exist.",
                 "We are thus able to see without construction why a triangle for the set of lengths 10 cm, 15 cm "
                 "and 30 cm cannot exist. We have been able to figure this out through spatial intuition and "
                 "reasoning.",
                 "Can we say anything about the existence of a triangle having sidelengths 3 cm, 3 cm and 7 cm? "
                 "Verify your answer by construction.",
                 "In the rough diagram, is it possible to assign lengths in a different order such that the direct "
                 "paths are always coming out to be shorter than the roundabout paths? If this is possible, then a "
                 "triangle might exist. Is such rearrangement of lengths possible in the triangle?"],
       teach=["Predict first: for 10, 15 and 30, is each length shorter than the other two added together?",
              "Three comparisons are needed, one for each side as the direct path.",
              "If even one comparison fails, no triangle exists. Moving the lengths to different sides of the "
              "rough figure does not help: the comparison 30 against 10 + 15 is the same wherever 30 is drawn.",
              "For 3, 3 and 7: 7 is more than 3 + 3 = 6, so there is no triangle, and a construction with a base of "
              "7 cm and arcs of 3 cm shows the arcs falling short."],
       examples=[
           WE("Does a triangle exist with sidelengths 10 cm, 15 cm and 30 cm? Compare each direct length with the "
              "roundabout length.",
              ["Between B and C: direct BC = 10 cm; roundabout BA + AC = 15 + 30 = 45 cm. 10 < 45, which is fine.",
               "Between A and B: direct AB = 15 cm; roundabout AC + CB = 30 + 10 = 40 cm. 15 < 40, which is fine.",
               "Between C and A: direct CA = 30 cm; roundabout CB + BA = 10 + 15 = 25 cm. 30 > 25, which is "
               "absurd.",
               "One direct path is longer than its roundabout path, so no triangle exists."],
              "No triangle exists: 30 is greater than 10 + 15 = 25", ncert=["ti.ex", "ti.mathtalk"]),
           WE("Can we say anything about the existence of a triangle having sidelengths 3 cm, 3 cm and 7 cm? "
              "Verify by construction.",
              ["The longest length is 7 cm. The other two add to 3 + 3 = 6 cm.",
               "7 > 6, so the direct path of 7 cm is longer than the roundabout path of 6 cm. No triangle exists.",
               "Check by construction: take the 7 cm side as the base and draw an arc of 3 cm from each end. The "
               "arcs cover 6 cm of the 7 cm and do not meet.",
               "Rearranging the lengths does not help: 7 is still more than 3 + 3."],
              "No triangle exists for 3, 3 and 7", ncert=["ti.337"])],
       key_terms=["triangle inequality"], misconceptions=["M_ANY_LENGTHS"], minutes=10),
     DOER("T4.C4", "Practice: check lengths against the triangle inequality", "triangle_inequality_checker",
          "Analyze",
          "Students decide whether three lengths can make a triangle by comparing each length with the sum of the "
          "other two, and state the definition of satisfying the triangle inequality.",
          ["Each length must be smaller than the sum of the other two.",
           "If even one comparison fails, there is no triangle.",
           "Comparing the longest length with the sum of the other two is the test that can fail."],
          textbook=["You would have realised that using a rough figure and comparing the direct path lengths with "
                    "their corresponding roundabout path lengths is the same as comparing each length with the "
                    "sum of the other two lengths. There are three such comparisons to be made.",
                    "Given three sidelengths, what do we need to compare to check for the existence of a "
                    "triangle?",
                    "When each length is smaller than the sum of the other two, we say that the lengths satisfy "
                    "the triangle inequality. For example, the set 3, 4, 5 satisfies the triangle inequality "
                    "whereas, the set 10, 15, 30 does not satisfy the triangle inequality.",
                    "We have seen that lengths such as 10, 15, 30 that do not satisfy the triangle inequality "
                    "cannot be the sidelengths of a triangle."],
          ncert=["ti.def"],
          items=[
              FIO("ti.FiOB1", "Figure it Out (the triangle inequality), Q1",
                  "We checked by construction that there are no triangles having sidelengths 3 cm, 4 cm and 8 cm; "
                  "and 2 cm, 3 cm and 6 cm. Check if you could have found this without trying to construct the "
                  "triangle.",
                  ["For 3, 4 and 8: the longest is 8 and the other two add to 3 + 4 = 7.",
                   "8 > 7, so the direct length is longer than the roundabout length: no triangle.",
                   "For 2, 3 and 6: the longest is 6 and the other two add to 2 + 3 = 5.",
                   "6 > 5, so again no triangle. No construction was needed."],
                  "Yes: 3 + 4 = 7 < 8 and 2 + 3 = 5 < 6, so neither set makes a triangle",
                  tool="triangle_inequality_checker"),
              FIO("ti.FiOB2", "Figure it Out (the triangle inequality), Q2",
                  "Can we say anything about the existence of a triangle for each of the following sets of "
                  "lengths? (a) 10 km, 10 km and 25 km (b) 5 mm, 10 mm and 20 mm (c) 12 cm, 20 cm and 40 cm",
                  ["Compare the longest length with the sum of the other two; all three lengths in a set have "
                   "the same unit.",
                   "(a) 10 + 10 = 20 and 20 < 25: no triangle.",
                   "(b) 5 + 10 = 15 and 15 < 20: no triangle.",
                   "(c) 12 + 20 = 32 and 32 < 40: no triangle."],
                  "No triangle exists in any of the three sets: (a) 20 < 25, (b) 15 < 20, (c) 32 < 40",
                  tool="triangle_inequality_checker"),
              FIO("ti.FiOB3", "Figure it Out (the triangle inequality), Q3 (Try This)",
                  "For the set 10 cm, 15 cm and 30 cm, two comparisons hold (10 < 15 + 30 and 15 < 10 + 30) but "
                  "the third does not (30 > 10 + 15). Will there always be at least two comparisons where the "
                  "direct length is less than the sum of the other two? Explore for different sets of lengths. "
                  "Is it possible to tell which lengths will immediately be less than the sum of the other two, "
                  "without calculations? [Hint: Consider the lengths in increasing order.]",
                  ["Write the lengths in increasing order: a, b, c with a ≤ b ≤ c.",
                   "The length c is the longest, so a < b + c is true because b + c is already at least c, which is "
                   "at least a. Also b < a + c, because a + c is at least c, which is at least b.",
                   "Only the comparison for c, c < a + b, can fail.",
                   "Test with 7, 10, 15: 7 < 10 + 15 = 25 and 10 < 7 + 15 = 22 hold, and the longest check 15 < 7 + 10 = 17 "
                   "holds too. For 10, 15, 30 the first two hold and only the longest check, 30 < 25, fails.",
                   "So at least two comparisons always hold, and the two that always hold belong to the two "
                   "shorter lengths. Only the longest length needs a check."],
                  "Yes, at least two comparisons always hold: the two shorter lengths are always less than the sum "
                  "of the other two, so only the longest length needs to be checked",
                  tool="triangle_inequality_checker"),
          ])]))

# ============================== T5 Does 4, 5, 8 make a triangle ===============================================
TOPICS.append(TOPIC(
    "T5", "M1", "Does 4, 5 and 8 Make a Triangle?", ["7.2"], "Analyze",
    "Students check the lengths 4, 5 and 8, explain why only the longest length needs a check, and picture two "
    "circles on the longest side to see that they must cross.",
    "When the longest length is less than the sum of the other two, the other two comparisons hold automatically, "
    "and the circles on the longest side cross in two points.",
    [A("T5.C1", "Seeing the circles for 4, 5 and 8", "Analyze",
       "Students draw two circles of radius 4 cm and 5 cm on a base of 8 cm and use the distance BX to explain why "
       "they cross in two points.",
       textbook=["Does a triangle exist with sidelengths 4 cm, 5 cm and 8 cm?",
                 "This satisfies the triangle inequality: 8 < 4 + 5 = 9",
                 "This means that all the direct path lengths are less than the roundabout path lengths. Does this "
                 "confirm the existence of a triangle?",
                 "If one of the direct path lengths had been longer, we could have concluded that a triangle "
                 "would surely not exist. But in this case, we can only say that a triangle may or may not exist.",
                 "For the triangle to exist, the arcs that we construct to get the third vertex must intersect. Is "
                 "it possible to determine that this will happen without actually carrying out the construction?",
                 "Visualising the construction of circles",
                 "Let us imagine that we start the construction by constructing the longest side as the base. Let "
                 "AB be the base of length 8 cm. The next step is the construction of sufficiently long arcs "
                 "corresponding to the other two lengths: 4 cm and 5 cm.",
                 "Instead of just constructing the arcs, let us complete the full circles. Suppose, we construct a "
                 "circle of radius 4 cm with A as the centre. Now, suppose that a circle of radius 5 cm is "
                 "constructed, centred at B. Can you draw a rough diagram of the resulting figure?",
                 "Note that in the figure below, AX = 4 cm and AB = 8 cm. So, what is BX? Does this length help in "
                 "visualising the resulting figure?",
                 "Since BX = 4 cm, and the radius of the circle centred at B is 5 cm, it is clear that the circles "
                 "will intersect each other at two points.",
                 "What does this tell us about the existence of a triangle? The points A and B along with either "
                 "of the points of intersection of the circles will give us the required triangle. Thus, there "
                 "exists a triangle having sidelengths 4 cm, 5 cm and 8 cm."],
       teach=["Predict first: the circle at A reaches 4 cm along the base, and the circle at B has radius 5 cm. "
              "Does the circle at B reach past that point?",
              "X is where the circle at A meets the base, so AX = 4 cm and BX = 8 − 4 = 4 cm.",
              "The circle at B has radius 5 cm, which is more than BX = 4 cm, so the circle at B goes inside the "
              "circle at A and out again: the circles cross at two points."],
       examples=[
           WE("Does a triangle exist with sidelengths 4 cm, 5 cm and 8 cm? Picture the circles on the longest "
              "side.",
              ["Check the longest length: 8 < 4 + 5 = 9, so the triangle inequality is satisfied.",
               "Take the base AB = 8 cm. Draw a circle of radius 4 cm at A and a circle of radius 5 cm at B.",
               "Let X be the point where the circle at A meets AB. Then AX = 4 cm, so BX = 8 − 4 = 4 cm.",
               "BX = 4 cm is less than the radius 5 cm of the circle at B, so the circle at B goes beyond X, "
               "into the circle at A. The circles cross at two points.",
               "Either crossing point with A and B gives a triangle with sides 4 cm, 5 cm and 8 cm."],
              "Yes, a triangle exists with sidelengths 4 cm, 5 cm and 8 cm: the two circles cross at two points",
              ncert=["c458.exists", "c458.circles"])],
       key_terms=["circle"], misconceptions=["M_SUM_EQUALS"], minutes=10),
     A("T5.C2", "Only the longest length needs checking", "Analyze",
       "Students explain why, once the longest length is less than the sum of the other two, the other two "
       "comparisons hold without calculation.",
       textbook=["Why do we not need to check the other two sides?"],
       teach=["Predict first: for 4, 5 and 8, is 5 less than 4 + 8? Is 4 less than 5 + 8?",
              "The sum of any other length and the longest length is already at least as big as the longest "
              "length, which is at least as big as any other length. So the two comparisons for the shorter "
              "lengths always hold.",
              "Only the comparison for the longest length can fail, so it is the only one to check: is the longest "
              "less than the sum of the other two?"],
       examples=[
           WE("Check the lengths 6, 7 and 12 by comparing only the longest length with the sum of the other two, "
              "and then check the other two comparisons to see that they hold.",
              ["The longest length is 12. The other two add to 6 + 7 = 13.",
               "12 < 13, so the longest comparison holds.",
               "The other two comparisons: 6 < 7 + 12 = 19 and 7 < 6 + 12 = 18. Both hold, as they must, because "
               "12 is already bigger than 6 and than 7.",
               "All three hold, so the lengths satisfy the triangle inequality."],
              "The lengths 6, 7 and 12 satisfy the triangle inequality: 12 < 13 is the only check needed",
              ncert=["c458.why_longest"])],
       key_terms=[], misconceptions=["M_TWO_COMPARISONS"], minutes=8),
     DOER("T5.C3", "Practice: check only the longest", None, "Analyze",
          "Students decide whether three lengths can make a triangle by comparing only the longest with the sum of "
          "the other two.",
          ["Find the longest length first.",
           "Add the other two and compare with the longest.",
           "Longest less than the sum: a triangle may exist. Longest more than the sum: no triangle."],
          items=[
              FIO("c458.FiOC1", "Figure it Out (which lengths make a triangle), Q1",
                  "Which of the following lengths can be the sidelengths of a triangle? Explain your answers. "
                  "Note that for each set, the three lengths have the same unit of measure. (a) 2, 2, 5 "
                  "(b) 3, 4, 6 (c) 2, 4, 8 (d) 5, 5, 8 (e) 10, 20, 25 (f) 10, 20, 35 (g) 24, 26, 28",
                  ["Compare the longest length with the sum of the other two.",
                   "(a) 2 + 2 = 4 < 5: no triangle. (b) 3 + 4 = 7 > 6: a triangle. (c) 2 + 4 = 6 < 8: no "
                   "triangle.",
                   "(d) 5 + 5 = 10 > 8: a triangle. (e) 10 + 20 = 30 > 25: a triangle. (f) 10 + 20 = 30 < 35: "
                   "no triangle.",
                   "(g) 24 + 26 = 50 > 28: a triangle."],
                  "Triangles exist for (b) 3, 4, 6; (d) 5, 5, 8; (e) 10, 20, 25; (g) 24, 26, 28. Not for (a), (c) "
                  "or (f)"),
          ])]))

# ============================== T6 When circles touch, miss or cross =========================================
TOPICS.append(TOPIC(
    "T6", "M1", "When Circles Touch, Miss or Cross", ["7.2"], "Analyze",
    "Students sort two circles on the longest side into three cases by comparing the sum of the radii with the "
    "base, conclude that a triangle exists exactly when the triangle inequality holds, and frame a complete test.",
    "Two circles on the longest side touch when the two smaller lengths add up to the longest, miss when they "
    "add up to less, and cross when they add up to more: only crossing gives a triangle.",
    [A("T6.C1", "Three cases for two circles", "Analyze",
       "Students describe how two circles on a base touch, miss each other or cross, and relate each case to the "
       "sum of the radii and the length of the base.",
       textbook=["Will triangles always exist when a set of lengths satisfies the triangle inequality? How can we "
                 "be sure?",
                 "We can be sure of the existence of a triangle only if we can show that the circles intersect "
                 "internally (as in Fig. 7.5) whenever the triangle inequality is satisfied. But are there other "
                 "possibilities when the two circles are constructed? Let us visualise and study them.",
                 "The following different cases can be conceived: Case 1: Circles touch each other. Case 2: "
                 "Circles do not intersect. Case 3: Circles intersect each other internally.",
                 "Note that while constructing the circles, we take (a) the length of the base AB = longest of the "
                 "given length (b) the radii of the circles to be the smaller two lengths.",
                 "Which of the above-mentioned cases will lead to the formation of a triangle? Clearly, triangles "
                 "are formed only when the circles intersect each other internally (Case 3).",
                 "Let us study each of these cases by finding the relation between the radii (the smaller two "
                 "lengths) and AB (longest length).",
                 "Case 1: Circles touch each other at a point. For this case to happen, sum of the two radii = AB "
                 "or sum of the two smaller lengths = longest length",
                 "Case 2: Circles do not intersect internally. For this case to happen, what should be the "
                 "relation between the radii and AB? It can be seen from the figure that, sum of the two radii < "
                 "AB or sum of the two smaller lengths < longest length",
                 "Case 3: Circles intersect each other. AB is composed of one radius and a part of the other. So, "
                 "sum of the two radii > AB, or sum of the two smaller lengths > longest length"],
       teach=["Predict first: if the two radii add up to exactly the base, where do the circles meet?",
              "Touch: the radii exactly fill the base, so the circles meet at one point on the base, and the "
              "three points are on one line. This is the answer to the question of three vertices on a line.",
              "Miss: the radii add up to less than the base, so a gap is left between the circles.",
              "Cross: the radii add up to more than the base, so the circles overlap and meet at two points."],
       examples=[
           WE("On a base AB, take two circles whose radii are the two smaller lengths. For the sets 3, 5, 8 and "
              "2, 5, 8 and 5, 6, 8 say whether the circles touch, miss or cross, and whether a triangle exists.",
              ["3, 5, 8: the base is 8 and the radii are 3 and 5. The radii add to 3 + 5 = 8, equal to the base, "
               "so the circles touch at one point. No triangle.",
               "2, 5, 8: the radii add to 2 + 5 = 7, less than 8, so the circles miss. No triangle.",
               "5, 6, 8: the radii add to 5 + 6 = 11, more than 8, so the circles cross in two points. A triangle "
               "exists."],
              "3, 5, 8: touch, no triangle; 2, 5, 8: miss, no triangle; 5, 6, 8: cross, a triangle exists",
              ncert=["case.three", "case.touch", "case.apart", "case.overlap"])],
       key_terms=[], misconceptions=["M_SUM_EQUALS"], minutes=10),
     A("T6.C2", "A complete test for a triangle", "Analyze",
       "Students conclude that a triangle exists exactly when the longest length is less than the sum of the other "
       "two, find sets that give touching or missing circles, and write a procedure.",
       textbook=["Can we use this analysis to tell if a triangle exists when the lengths satisfy the triangle "
                 "inequality?",
                 "If the given lengths satisfy the triangle inequality, then the sum of the two smaller lengths is "
                 "greater than the longest length. This means that this will lead to Case 3 where the circles "
                 "intersect internally, and so a triangle exists.",
                 "How will the two circles turn out for a set of lengths that do not satisfy the triangle "
                 "inequality? Find 3 examples of sets of lengths for which the circles: (a) touch each other at a "
                 "point, (b) do not intersect.",
                 "Frame a complete procedure that can be used to check the existence of a triangle.",
                 "Conclusion: If a given set of three lengths satisfies the triangle inequality, then a triangle "
                 "exists having those as sidelengths. If the set does not satisfy the triangle inequality, then a "
                 "triangle with those sidelengths does not exist."],
       teach=["Predict first: if the lengths satisfy the triangle inequality, which of the three cases happens?",
              "The inequality says the two smaller lengths add to more than the longest, which is Case 3: the "
              "circles cross and a triangle exists.",
              "If the inequality fails, the sum is equal to the longest length (the circles touch) or less (the "
              "circles miss): no triangle either way.",
              "Touching examples: 2, 3, 5; 4, 4, 8; 1, 6, 7. Missing examples: 1, 2, 5; 3, 3, 9; 2, 4, 10."],
       examples=[
           WE("Frame a complete procedure to check whether three lengths can make a triangle, and use it on "
              "3.5, 6 and 9, and on 4, 7 and 11.",
              ["Step 1: find the longest length.",
               "Step 2: add the other two lengths.",
               "Step 3: if the sum is more than the longest, a triangle exists; if the sum is equal or less, it "
               "does not.",
               "3.5, 6, 9: the longest is 9 and 3.5 + 6 = 9.5. 9.5 > 9, so a triangle exists.",
               "4, 7, 11: the longest is 11 and 4 + 7 = 11. The sum equals the longest, so the circles touch and "
               "no triangle exists."],
              "A triangle exists for 3.5, 6 and 9; none exists for 4, 7 and 11",
              ncert=["case.examples", "case.procedure", "case.conclusion"])],
       key_terms=[], misconceptions=["M_SUM_EQUALS", "M_TWO_COMPARISONS"], minutes=10),
     DOER("T6.C3", "Practice: sort lengths by touch, miss or cross", "two_circles_explorer", "Analyze",
          "Students decide whether two circles on a base touch, miss or cross for a set of lengths, give the third "
          "length that makes a triangle, and describe all such lengths.",
          ["Longest length as the base, the two smaller lengths as radii.",
           "Radii add to more than the base: cross, a triangle exists.",
           "A third length must be less than the sum of the two lengths and more than their difference."],
          items=[
              FIO("case.FiOD1", "Figure it Out (circles and the third length), Q1",
                  "Check if a triangle exists for each of the following set of lengths: (a) 1, 100, 100 "
                  "(b) 3, 6, 9 (c) 1, 1, 5 (d) 5, 10, 12",
                  ["(a) The longest is 100 and 1 + 100 = 101 > 100: a triangle exists.",
                   "(b) The longest is 9 and 3 + 6 = 9, equal to 9: the circles touch, so no triangle.",
                   "(c) The longest is 5 and 1 + 1 = 2 < 5: no triangle.",
                   "(d) The longest is 12 and 5 + 10 = 15 > 12: a triangle exists."],
                  "Triangles exist for (a) and (d); not for (b) (circles touch) or (c)",
                  tool="two_circles_explorer"),
              FIO("case.FiOD2", "Figure it Out (circles and the third length), Q2",
                  "Does there exist an equilateral triangle with sides 50, 50, 50? In general, does there exist an "
                  "equilateral triangle of any sidelength? Justify your answer.",
                  ["For 50, 50, 50 the longest is 50 and the other two add to 50 + 50 = 100.",
                   "50 < 100, so the triangle inequality holds and an equilateral triangle exists.",
                   "For any side length s the other two add to s + s = 2s, and s < 2s as long as s is more than "
                   "zero.",
                   "So the circles always cross: an equilateral triangle exists for every side length. It can "
                   "be built with the two-arcs method of the first topic."],
                  "Yes: 50 < 50 + 50, and in general s < s + s for any side length s above zero",
                  tool="two_circles_explorer"),
              FIO("case.FiOD3", "Figure it Out (circles and the third length), Q3 (Try This)",
                  "For each of the following, give at least 5 possible values for the third length so there "
                  "exists a triangle having these as sidelengths (decimal values could also be chosen): (a) 1, 100 "
                  "(b) 5, 5 (c) 3, 7. See if you can describe all possible lengths of the third side in each case, "
                  "so that a triangle exists with those sidelengths. For example, in case (a), all numbers "
                  "strictly between 99 and 101 would be possible.",
                  ["The third length x must be less than the sum of the other two, and the other two lengths must "
                   "each be less than the sum of x and the remaining length.",
                   "(a) 1 and 100: x < 1 + 100 = 101, and 100 < 1 + x gives x > 99. So x is strictly between 99 "
                   "and 101: for example 99.5, 100, 100.5, 99.9 and 100.9.",
                   "(b) 5 and 5: x < 5 + 5 = 10, and 5 < 5 + x gives x > 0. So x is strictly between 0 and 10: "
                   "for example 1, 3, 5, 7 and 9.",
                   "(c) 3 and 7: x < 3 + 7 = 10, and 7 < 3 + x gives x > 4. So x is strictly between 4 and 10: "
                   "for example 5, 6, 7, 8 and 9.",
                   "In general, for two lengths p and q, the third length is strictly between the difference of "
                   "p and q and the sum of p and q."],
                  "(a) strictly between 99 and 101, for example 99.5, 100, 100.5; (b) strictly between 0 and 10, "
                  "for example 1, 3, 5, 7, 9; (c) strictly between 4 and 10, for example 5, 6, 7, 8, 9",
                  tool="two_circles_explorer"),
          ],
          ncert=[])]))
