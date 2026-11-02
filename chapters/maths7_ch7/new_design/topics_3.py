# -*- coding: utf-8 -*-
"""Topics T12 to T15 (module M3: altitudes and kinds of triangles; module M4: puzzle and summary)."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T12 Altitudes ==================================================================
TOPICS.append(TOPIC(
    "T12", "M3", "Altitudes of a Triangle", ["7.4"], "Apply",
    "Students define the altitude as the perpendicular from a vertex to the opposite side, draw it with a set "
    "square, extend the base for an obtuse triangle, and find the triangles in which a side is an altitude.",
    "An altitude is the perpendicular from a vertex to the line of the opposite side; it can fall inside, outside "
    "or along a side of the triangle.",
    [A("T12.C1", "Height and altitude", "Understand",
       "Students define the altitude from a vertex and draw it with a ruler and a set square.",
       textbook=["7.4 Constructions Related to Altitudes of Triangles",
                 "There is another set of useful measurements with respect to a triangle, the height of each of "
                 "its vertices with respect to the opposite sides.",
                 "In the world around us, we talk of the heights of various objects: the height of a person, the "
                 "height of a tree, the height of a building, etc. What do we mean by the word 'height'?",
                 "Consider a triangle ABC. What is the height of the vertex A from its opposite side BC, and how "
                 "can it be measured?",
                 "Let AD be the line segment from A drawn perpendicular to BC. The length of AD is the height of "
                 "the vertex A from BC. The line segment AD is said to be one of the 'altitudes' of the "
                 "triangle. The other altitudes are BE and CF in the figure below: the perpendiculars drawn from "
                 "the other vertices to their respective opposite sides.",
                 "Whenever we use the word height of the triangle, we generally refer to the length of the "
                 "altitude to whatever side we take as base (this altitude is AD in the case of Fig. 7.8).",
                 "Construction of the Altitudes of a Triangle",
                 "Construct an arbitrary triangle. Label the vertices A, B, C taking BC to be the base.",
                 "Construct the altitude from A to BC.",
                 "Constructing the altitude using just a ruler is not accurate. To get a more precise angle of "
                 "90°, we use a set square along with a ruler. Can you see how to do this?",
                 "Step 1: Keep the ruler aligned to the base. Place the set square on the ruler as shown, such "
                 "that one of the edges of the right angle touches the ruler.",
                 "Step 2: Slide the set square along the ruler till the vertical edge of the set square touches "
                 "the vertex A.",
                 "Step 3: Draw the altitude to BC through A using the vertical edge of the set square."],
       teach=["Predict first: a triangle has three corners. How many altitudes does it have?",
              "The height of a vertex from the opposite side is the length of the perpendicular from the vertex to "
              "that side. The perpendicular segment is called an altitude, and every triangle has three, one from "
              "each vertex.",
              "Height of the triangle usually means the length of the altitude to the side taken as the base.",
              "A ruler alone is not accurate for a right angle, so use a set square: slide it along the base "
              "until its upright edge touches the vertex, then draw along that edge."],
       examples=[
           WE("Draw the altitude from A to the base BC of a triangle ABC using a ruler and a set square.",
              ["Step 1: keep the ruler along the base BC, and place the set square on the ruler with one edge "
               "of its right angle against the ruler.",
               "Step 2: slide the set square along the ruler until its upright edge touches A.",
               "Step 3: draw along the upright edge from A down to BC. This segment AD is the altitude.",
               "AD is perpendicular to BC, so the angle at D is 90°, and the length of AD is the height of A "
               "from BC."],
              "AD, the perpendicular from A to BC, is the altitude from A; its length is the height",
              ncert=["alt.height", "alt.setsquare"])],
       key_terms=["altitude"], misconceptions=["M_ALTITUDE_INSIDE"], minutes=8),
     A("T12.C2", "Altitudes that fall outside, and the paper fold", "Analyze",
       "Students draw the altitude of an obtuse triangle by extending the base and explain the paper-fold "
       "altitude.",
       textbook=["What would the altitude from A to BC be in this triangle?",
                 "We extend BC and then drop the perpendicular from A to this line.",
                 "Altitudes Using Paper Folding",
                 "Cut out a paper triangle. Fix one of the sides as the base. Fold it in such a way that the "
                 "resulting crease is an altitude from the top vertex to the base. Justify why the crease formed "
                 "should be perpendicular to the base."],
       teach=["Predict first: in a triangle with a very wide angle at B, where does the perpendicular from A "
              "land?",
              "It lands outside the triangle. Extend the base BC beyond B and drop the perpendicular from A to "
              "this extended line.",
              "Paper fold: fold the paper so that the base folds onto itself and the crease passes through the top "
              "vertex. The two parts of the base line match, so the two angles made by the crease are equal, and "
              "they make a straight angle of 180°. Each is therefore 90°, so the crease is perpendicular."],
       examples=[
           WE("In triangle ABC the angle at B is obtuse. Draw the altitude from A to BC and say where it lies.",
              ["Extend the base BC beyond B into a longer line.",
               "Slide the set square along the extended line until its upright edge touches A.",
               "Draw the perpendicular from A to the extended line. The foot D is on the extension, outside the "
               "triangle.",
               "So an altitude can lie outside the triangle.",
               "Paper fold check: fold so that the base falls on itself with the crease through A. The two angles "
               "at the crease are equal and add up to 180°, so each is 90°."],
              "The altitude from A meets the extended base outside the triangle; the paper crease is perpendicular "
              "because its two equal angles add up to 180°",
              ncert=["alt.obtuse", "alt.fold", "alt.others"])],
       key_terms=[], misconceptions=["M_ALTITUDE_INSIDE"], minutes=10),
     A("T12.C3", "A side that is also an altitude", "Analyze",
       "Students find that in a right-angled triangle two of the sides are themselves altitudes, and then locate the third altitude by drawing it carefully.",
       textbook=["Does there exist a triangle in which a side is also an altitude? Visualise such a triangle and "
                 "draw a rough diagram.",
                 "We see that this happens in triangles where one of the angles is a right angle.",
                 "Triangles having one right angle are called right-angled triangles or simply right triangles."],
       teach=["Predict first: can the perpendicular from a vertex be one of the sides of the triangle?",
              "In a triangle with a right angle at B, the side AB is perpendicular to BC. So AB is the altitude "
              "from A to BC, and BC is the altitude from C to AB.",
              "A triangle with one right angle is called a right-angled triangle, or a right triangle."],
       examples=[
           WE("In a triangle ABC with a right angle at B, name two altitudes that are also sides.",
              ["AB meets BC at 90°. The perpendicular from A to BC is AB itself, so AB is the altitude from A.",
               "In the same way BC meets AB at 90°, so BC is the altitude from C to AB.",
               "The altitude from B goes to the long side AC and lies inside the triangle."],
              "AB and BC are both sides and altitudes in a right-angled triangle with the right angle at B",
              ncert=["alt.right"])],
       key_terms=["right-angled triangle"], minutes=8),
     DOER("T12.C4", "Practice: draw the altitudes of different triangles", "altitude_explorer", "Apply",
          "Students draw the three altitudes of acute, right and obtuse triangles and say where each falls.",
          ["Take each side as the base in turn.",
           "Use the set square to draw the perpendicular from the opposite vertex.",
           "Extend the base when the foot of the altitude falls outside."])]))

# ============================== T13 Types of triangles ========================================================
TOPICS.append(TOPIC(
    "T13", "M3", "Types of Triangles", ["7.5"], "Apply",
    "Students sort triangles by sides and by angles, explain why an acute-angled triangle needs all three angles "
    "acute, and construct triangles from the figure-it-out questions.",
    "Triangles are equilateral, isosceles or scalene by their sides, and acute-angled, right-angled or "
    "obtuse-angled by their angles; an acute triangle has all three angles acute.",
    [A("T13.C1", "Sorting triangles by their sides", "Understand",
       "Students sort triangles into equilateral, isosceles and scalene groups by comparing the lengths of their three sides and giving a reason for each choice.",
       textbook=["7.5 Types of Triangles",
                 "In our study of triangles, we have encountered the following types of triangles; equilateral, "
                 "isosceles, scalene and right-angled triangles. Did you spot any other type of triangle?",
                 "The classification of triangles as equilateral and isosceles was based on equality of sides.",
                 "Equilateral triangles have sides of equal length. Isosceles triangles have two sides of equal "
                 "length. Scalene triangles have sides of three different lengths.",
                 "Can a similar classification be done based on equality of angles? Is there any relation between "
                 "these two classifications? We will answer these questions in a later chapter."],
       teach=["Predict first: a triangle has sides 5, 5 and 8. Is it equilateral, isosceles or scalene?",
              "Equilateral means all three sides are equal, isosceles means two sides are equal, and scalene "
              "means all three sides are different.",
              "Whether equal angles go with equal sides is answered in a later chapter."],
       examples=[
           WE("Name the kind of triangle with sides (a) 5 cm, 5 cm, 5 cm (b) 5 cm, 5 cm, 8 cm (c) 5 cm, 6 cm, "
              "7 cm, after checking each really is a triangle.",
              ["Check each with the triangle inequality: 5 < 5 + 5; 8 < 5 + 5; 7 < 5 + 6. All three exist.",
               "(a) All three sides are equal: equilateral.",
               "(b) Exactly two sides are equal: isosceles.",
               "(c) All three sides are different: scalene."],
              "(a) equilateral (b) isosceles (c) scalene",
              ncert=["types.sides"])],
       key_terms=["scalene"], minutes=8),
     A("T13.C2", "Sorting triangles by their angles", "Understand",
       "Students sort triangles into acute-angled, right-angled and obtuse-angled and explain why an acute-angled "
       "triangle cannot be defined as one with one acute angle.",
       textbook=["We used angle measures when classifying a triangle as a right-angled triangle. What are the "
                 "other types of triangles based on angle measures?",
                 "A classification of triangles based on their angle measures is acute-angled, right-angled and "
                 "obtuse-angled. We have already seen what a right-angled triangle is. It is a triangle with one "
                 "right angle. Similarly, an obtuse-angled triangle has one obtuse angle.",
                 "What could an acute-angled triangle be? Can we define it as a triangle with one acute angle? "
                 "Why not?",
                 "In an acute-angled triangle, all three angles are acute angles."],
       teach=["Predict first: can a triangle have two obtuse angles? Think about the angle sum.",
              "A right-angled triangle has one right angle, and an obtuse-angled triangle has one obtuse angle. "
              "Two such angles already use up 180° or more, so a triangle never has two of them.",
              "Can an acute-angled triangle be one with one acute angle? No: every triangle has at least two "
              "acute angles, because the other two angles can be 90° and more only once. A triangle with angles "
              "90°, 50°, 40° has acute angles and is still right-angled.",
              "So an acute-angled triangle has all three angles acute."],
       examples=[
           WE("Name the kind of triangle with angles (a) 50°, 60°, 70° (b) 90°, 50°, 40° (c) 120°, 30°, 30°. "
              "Which of them has at least one acute angle?",
              ["Check the angle sums: 50° + 60° + 70° = 180°; 90° + 50° + 40° = 180°; 120° + 30° + 30° = 180°.",
               "(a) All three are acute: acute-angled.",
               "(b) One angle is a right angle: right-angled.",
               "(c) One angle is obtuse: obtuse-angled.",
               "All three triangles have at least one acute angle, so having one acute angle does not tell the "
               "kind of triangle."],
              "(a) acute-angled (b) right-angled (c) obtuse-angled; all three have an acute angle",
              ncert=["types.angles", "types.acute"])],
       key_terms=["acute-angled triangle", "obtuse-angled triangle"], misconceptions=["M_ACUTE_ONE"], minutes=10),
     DOER("T13.C3", "Practice: construct triangles and sort them", "triangle_classifier", "Apply",
          "Students construct triangles with an altitude, a right-angled triangle on a given hypotenuse, and "
          "decide which kinds of triangles can be equilateral or isosceles.",
          ["Check that the measurements give a triangle.",
           "Construct, and draw the altitude with a set square.",
           "Name the triangle by its sides and by its angles."],
          items=[
              FIO("types.FiOI1", "Figure it Out (types of triangles), Q1",
                  "Construct a triangle ABC with BC = 5 cm, AB = 6 cm, CA = 5 cm. Construct an altitude from A "
                  "to BC.",
                  ["Check: 6 < 5 + 5, 5 < 5 + 6 and 5 < 6 + 5, so the triangle exists. Two sides are equal, so it "
                   "is isosceles.",
                   "Draw BC = 5 cm. Draw an arc of radius 6 cm from B and an arc of radius 5 cm from C. They cross "
                   "at A.",
                   "Slide the set square along BC until its upright edge touches A, and draw the perpendicular AD "
                   "to BC.",
                   "Measure AD with the ruler: the altitude is about 4.8 cm."],
                  "Isosceles triangle ABC; the altitude from A to BC measures about 4.8 cm",
                  tool="triangle_classifier"),
              FIO("types.FiOI2", "Figure it Out (types of triangles), Q2",
                  "Construct a triangle TRY with RY = 4 cm, TR = 7 cm, ∠R = 140°. Construct an altitude from T "
                  "to RY.",
                  ["Draw RY = 4 cm. At R make an angle of 140° and mark T at 7 cm along the arm. Join TY.",
                   "The angle at R is obtuse, so the altitude from T falls outside the triangle.",
                   "Extend YR beyond R. Slide the set square along it until its upright edge touches T, and draw "
                   "the perpendicular TD to the extended line.",
                   "The angle TRD outside the triangle is 180° − 140° = 40°. Measure TD with the ruler: it is about "
                   "4.5 cm."],
                  "The altitude from T meets YR extended beyond R; its length is about 4.5 cm",
                  tool="triangle_classifier"),
              FIO("types.FiOI3", "Figure it Out (types of triangles), Q3",
                  "Construct a right-angled triangle ABC with ∠B = 90° and AC = 5 cm. How many different "
                  "triangles exist with these measurements? Hint: the other measurements can take any values. "
                  "Take AC as the base. What values can ∠A and ∠C take so that the other angle is 90°?",
                  ["Draw AC = 5 cm. The angle at B is 90°, so ∠A + ∠C = 90°.",
                   "Choose ∠A = 30°, then ∠C = 60°, and the arms cross at B. Choose ∠A = 45°, then ∠C = 45°. "
                   "Choose ∠A = 70°, then ∠C = 20°. Each choice gives a different triangle.",
                   "∠A can be any value strictly between 0° and 90°, and ∠C is then 90° − ∠A.",
                   "There are infinitely many values to choose from, so there are infinitely many different "
                   "triangles."],
                  "Infinitely many: ∠A can be any value strictly between 0° and 90° with ∠C = 90° − ∠A",
                  tool="triangle_classifier"),
              FIO("types.FiOI4", "Figure it Out (types of triangles), Q4",
                  "Through construction, explore if it is possible to construct an equilateral triangle that is "
                  "(i) right-angled (ii) obtuse-angled. Also construct an isosceles triangle that is (i) "
                  "right-angled (ii) obtuse-angled.",
                  ["Every equilateral triangle has three equal angles, so each is 180° ÷ 3 = 60°. No angle is 90° "
                   "or more.",
                   "So an equilateral triangle can be neither right-angled nor obtuse-angled.",
                   "Isosceles right-angled: take a right angle with two equal sides, for example 4 cm and 4 cm. "
                   "The other two angles are equal and add up to 90°, so each is 45°.",
                   "Isosceles obtuse-angled: take an angle of 120° between two equal sides of 5 cm. The other two "
                   "angles are equal and add up to 60°, so each is 30°."],
                  "(i) and (ii): not possible for an equilateral triangle; an isosceles triangle can be "
                  "right-angled (90°, 45°, 45°) or obtuse-angled (120°, 30°, 30°)",
                  tool="triangle_classifier"),
          ])]))

# ============================== T14 Puzzle =====================================================================
TOPICS.append(TOPIC(
    "T14", "M4", "Shortest Path in a Box", ["7.5"], "Analyze",
    "Students find the shortest walk for a spider between opposite corners of a box by laying two faces flat and "
    "comparing three straight paths.",
    "Laying two faces flat turns a path across the box into a straight line, and the three possible straight "
    "paths for a 6 by 4 by 3 box measure about 9.2, 9.8 and 10.4.",
    [A("T14.C1", "The spider and the box", "Analyze",
       "Students compare the three flat-face paths across a box and choose the shortest.",
       textbook=["Shortest Path in a Box!",
                 "There is a spider in a corner of a box. It wants to reach the farthest opposite corner (marked "
                 "in the figure). Since it cannot fly, it can reach the opposite point only by walking on the "
                 "surfaces of the box. What is the shortest path it can take?",
                 "Take a cardboard box and mark the path that you think is the shortest from one corner to its "
                 "opposite corner. Compare the length of this path with that of the paths made by your friends."],
       teach=["Predict first: is the shortest path along the edges, or straight across a face?",
              "Take a box 6 cm long, 4 cm wide and 3 cm high. The spider crosses two faces, so lay those two "
              "faces flat side by side. The path is then a straight line on a flat picture.",
              "Three pairs of faces are possible, and the answer is the shortest of the three straight lines."],
       examples=[
           WE("A spider walks from one corner of a box 6 cm long, 4 cm wide and 3 cm high to the opposite "
              "corner, over two faces. Which path is shortest?",
              ["Lay two faces flat side by side. The path is a straight line across the joined faces.",
               "Case 1: the line goes 6 cm along and 4 + 3 = 7 cm across. Draw this rectangle and measure the "
               "diagonal: about 9.2 cm.",
               "Case 2: 4 cm along and 6 + 3 = 9 cm across. The diagonal measures about 9.8 cm.",
               "Case 3: 3 cm along and 6 + 4 = 10 cm across. The diagonal measures about 10.4 cm.",
               "The shortest is the first, about 9.2 cm. It is shorter than going along the edges, which is "
               "6 + 4 + 3 = 13 cm."],
              "About 9.2 cm, across the 6 by 4 face and the 6 by 3 face laid flat",
              ncert=["puzzle.spider"])],
       key_terms=[], enrichment=True, minutes=10),
     DOER("T14.C2", "Pull it together and do it: find the spider's path on a box of your own", None, "Analyze",
          "Students measure a real box, lay out the three flat paths and compare them with the guess they "
          "made first.",
          ["Mark your guess for the shortest path on a real box.",
           "Lay two faces flat for each pair and measure the straight line.",
           "Compare your guess with the shortest of the three."],
          enrichment=True)]))

# ============================== T15 Summary ====================================================================
TOPICS.append(TOPIC(
    "T15", "M4", "Summary: Three Intersecting Lines", ["7.5"], "Understand",
    "Students recall what decides whether a triangle can be built, the angle sum, altitudes and the kinds of "
    "triangles.",
    "A triangle needs lengths that satisfy the triangle inequality or angles that add to less than 180 degrees; "
    "its angles add to 180 degrees, and it is named by its sides and angles.",
    [A("T15.C1", "What the chapter found", "Understand",
       "Students recall the main findings of the chapter in one place, including the triangle inequality, the angle sum, the exterior angle and altitudes.",
       textbook=["Use of a compass simplifies the construction of triangles when the sidelengths are given.",
                 "A set of three lengths where the length of each is smaller than the sum of the other two is "
                 "said to satisfy the triangle inequality.",
                 "Sidelengths of a triangle satisfy triangle inequality, and, if a given set of lengths satisfy "
                 "the triangle inequality, a triangle can be constructed with those sidelengths.",
                 "Triangles can be constructed when the following measurements are given: (a) two of the sides and "
                 "their included angle (b) two angles and the included side",
                 "The sum of the angles of a triangle is always 180°.",
                 "An altitude of a triangle is a perpendicular line segment from a vertex to its opposite side.",
                 "Equilateral triangles have sides of equal length. Isosceles triangles have two sides of equal "
                 "length. Scalene triangles have sides of three different lengths.",
                 "Triangles are classified based on their angle measures as acute-angled, right-angled and "
                 "obtuse-angled triangles."],
       teach=["A compass makes it easy to build a triangle from three lengths.",
              "Three lengths make a triangle when each is less than the sum of the other two.",
              "A triangle can be built from two sides and the angle between them, or from two angles and the side "
              "between them.",
              "The three angles of a triangle always add up to 180°.",
              "An altitude is the perpendicular from a vertex to the opposite side.",
              "By sides: equilateral, isosceles, scalene. By angles: acute-angled, right-angled, obtuse-angled."],
       examples=[], video_focus=["RECAP"], ncert=["summary"], key_terms=[], minutes=5)],
    topic_type="summary"))
