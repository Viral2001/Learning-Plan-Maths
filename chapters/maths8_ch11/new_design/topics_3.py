# -*- coding: utf-8 -*-
"""Topics T10 to T13 (module M3: projections, shadows and isometric drawing) and T14 (summary). Book pp 88 to 102."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T10 Projections =============================================================
TOPICS.append(TOPIC(
    "T10", "M3", "Projections of Points, Lines and Shapes", ["4.2"], "Analyze",
    "Students define the projection of a point on a plane, compare the length of a line with the length of its "
    "projection, describe the projections of a square, a parallelogram and a regular polygon in different "
    "orientations, and find different objects with the same projection.",
    "The projection of a point is the foot of the perpendicular from it to the plane. A projected line is never longer "
    "than the line, and equal only when the line is parallel to the plane. Parallel lines project to parallel lines, "
    "and one projection can come from many objects.",
    [A("T10.C1", "Projecting a point and a line", "Analyze",
       "Students find the projection of a point as the foot of the perpendicular, and use a right triangle to show "
       "that a projected line is never longer than the line.",
       textbook=["Projections",
                 "The net of a solid (when it exists) is one way of representing a solid on the plane. But it can be "
                 "difficult to visualise the solid from the net, without physically cutting out the net and folding "
                 "it up.",
                 "Another way to represent a solid is by looking at the projections of all its points on a plane. This "
                 "idea is closely related to the profile of a solid from a specific viewpoint, which we discussed "
                 "earlier.",
                 "Consider a point P in space, and a plane M. Imagine a line from P intersecting the plane M at a point "
                 "O. We say that OP is perpendicular to the plane if for any line OX on the plane, angle POX = 90°. In "
                 "this case, we say that point O is the projection of point P on the plane. The projections of all the "
                 "points of an object together form the projection of the object on the plane.",
                 "Let us visualise the projection of a line.",
                 "What happens to the length of a line in its projection? Let l be the actual length of the line and p "
                 "be the length of its projection. Draw AE perpendicular to BC. AECD is a rectangle (why?). So, AE = DC "
                 "= p. Also, angle AEB = 90°.",
                 "Can you now compare the lengths p and l? When is the length of the projected line equal to its actual "
                 "length?"],
       teach=["Predict first: a pencil is held slanting above a table. Is its projection on the table longer, shorter "
              "or the same length as the pencil?",
              "Drop a perpendicular from each end of the pencil to the table; the feet join to give the projection.",
              "Slide the projection up to the lower end: the pencil, the projection and the height difference make a "
              "right triangle, and the pencil is its longest side.",
              "So the projection is shorter, and equal only when the pencil lies parallel to the table."],
       examples=[
           WE("A stick 5 cm long is held above a table so that one end is 3 cm higher than the other. How long is its "
              "projection on the table?",
              ["The stick, its projection and the height difference make a right triangle.",
               "The stick is the longest side, 5 cm; the height difference is 3 cm.",
               "Projection = √(5² − 3²) = √16 = 4 cm."],
              "4 cm, shorter than the stick",
              ncert=["4.2.proj_point", "4.2.proj_line", "4.2.proj_compare"])],
       key_terms=["projection", "perpendicular", "plane"], misconceptions=["M_PROJ_LONGER"], minutes=10),
     A("T10.C2", "Projections of a square and a parallelogram", "Analyze",
       "Students describe the projections of a square in different orientations, explain why the projection of a "
       "parallelogram is always a parallelogram or a line, and build the projection of a polygon from its sides.",
       textbook=["What do you think are the different possible projections of a square that we get based on its "
                 "orientation?",
                 "What do you think is the projection of a parallelogram under different orientations? Can this ever "
                 "be a quadrilateral that is not a parallelogram? As a starting point, you could think about the "
                 "projection of a pair of parallel lines.",
                 "What can you say about the projection of an n-sided regular polygon? [Hint: Projection of a polygon "
                 "is composed of the projections of its sides.]"],
       teach=["Predict first: a square card is tilted above the floor. Can its projection be a trapezium?",
              "Flat: a square. Tilted about one side: a rectangle. Tilted about a diagonal: a rhombus. Standing on "
              "edge: a line segment.",
              "Opposite sides of a parallelogram are parallel and equal, and their projections stay parallel and "
              "equal, so the projection is a parallelogram (or a line), never a trapezium.",
              "A regular polygon projects side by side: opposite parallel sides stay parallel, but the polygon can "
              "look squashed."],
       examples=[
           WE("A square card of side 5 cm is tilted about one of its sides so that the opposite side is 3 cm higher. "
              "What is its projection on the floor?",
              ["The two sides parallel to the floor keep their length of 5 cm.",
               "Each of the other two sides is 5 cm long and rises 3 cm, so it projects to √(5² − 3²) = 4 cm.",
               "Parallel sides stay parallel, and the angles at the hinge stay right angles."],
              "A rectangle 5 cm by 4 cm",
              ncert=["4.2.mt_proj_square", "4.2.mt_proj_parallelogram", "4.2.mt_proj_polygon"])],
       key_terms=["projection", "parallelogram", "orientation"], misconceptions=["M_PROJ_ANY"], minutes=10),
     A("T10.C3", "Same projection, different objects", "Evaluate",
       "Students describe the projections of a cube and a cone, see that a projection is the shape of the hole left "
       "when an object passes straight through a plane, and find different objects with the same projection.",
       textbook=["Let us consider projections of solids now. How would the projections of a cube and a cone look?",
                 "If an object were to pass perpendicularly through a plane and form a hole, the shape of the hole "
                 "would be the same as the shape of the projection of the object.",
                 "See Figures 4.2 to 4.5. In each case, see if you can visualise another object that gives the same "
                 "projection.",
                 "Different lines and different cuboids giving the same projections. We see that a given projection "
                 "is not made by a unique object.",
                 "Find another object that makes the same projection as that of a given cone."],
       teach=["Predict first: a cone standing on its base is projected onto the floor. Can a different solid give the "
              "very same shape?",
              "The cone's projection on the floor is a circle; a cylinder of the same radius also gives that circle, "
              "and so does a ball.",
              "A cube resting on a face projects to a square; a tall cuboid with the same square base gives the same "
              "square.",
              "One projection cannot tell us the object, so we will need more than one."],
       examples=[
           WE("A cone standing on its base has base radius 4 cm. Name three different solids whose projection on the "
              "floor is the same circle.",
              ["The cone's projection on the floor is a circle of radius 4 cm.",
               "A cylinder standing upright with radius 4 cm gives the same circle.",
               "A ball of radius 4 cm and a bowl with rim radius 4 cm give it too."],
              "A cylinder, a ball and a bowl, each with radius 4 cm",
              ncert=["4.2.proj_solids", "4.2.proj_same", "4.2.proj_cone_same"])],
       key_terms=["projection", "unique"], misconceptions=["M_ONE_PROFILE"], minutes=8),
     DOER("T10.C4", "Practice: predict the projection", "projection_tilter", "Analyze",
          "Students predict the projections of sticks, cards and solids held in different positions, check them with "
          "a torch or by looking straight down, and find a second object with each projection.",
          ["A projection is never longer than the object's line; it is equal only when the line is parallel to the "
           "plane.",
           "A parallelogram projects to a parallelogram or a line; one projection fits many objects."],
          examples=[
              WE("A rod 13 cm long is held above a table so that one end is 5 cm higher than the other. Predict the "
                 "length of its projection, and say when the projection would be 13 cm.",
                 ["The rod, its projection and the height difference make a right triangle with the rod as the "
                  "longest side.",
                  "Projection = √(13² − 5²) = √(169 − 25) = √144 = 12 cm.",
                  "The projection equals 13 cm only when the rod is held parallel to the table."],
                 "12 cm; it would be 13 cm only with the rod parallel to the table")])],
    key_terms=["projection", "plane", "orientation"]))

# ============================== T11 Front, top and side views ===============================================
TOPICS.append(TOPIC(
    "T11", "M3", "Front, Top and Side Views", ["4.2"], "Analyze",
    "Students name the vertical, horizontal and side planes, draw the front, top and side views of solids and of "
    "stacks of cubes, and match everyday objects with their three views.",
    "The front view is the projection on the vertical plane, the top view on the horizontal plane and the side view "
    "on the side plane. Three views together describe a solid much better than one.",
    [A("T11.C1", "Three planes, three views", "Understand",
       "Students describe the vertical, horizontal and side planes and draw the front, top and side views of a "
       "cylinder.",
       textbook=["For this reason, we often take three mutually perpendicular projections of an object. As shown in "
                 "the figure, we consider a plane in front of the object called the vertical plane, a plane below the "
                 "object called the horizontal plane and a plane to the side of the object called the side plane.",
                 "We give names to the projections on these three planes based on the directions from which the "
                 "object is viewed. The projection on the vertical plane is called the front view, on the horizontal "
                 "plane the top view and on the side plane the side view. These projections formalise the notion of "
                 "profiles that we explored in an earlier section.",
                 "Let us see what these projections are for the objects shown in Fig. 4.6, when the planes shown are "
                 "taken to be vertical planes. Projections of the different lines in Fig. 4.6. Projections of the "
                 "different cuboids in Fig. 4.6."],
       teach=["Predict first: a glass of water stands on the table. Which of its three views is a circle?",
              "Front view: look from the front onto the wall behind. Top view: look down onto the floor. Side view: "
              "look from the side onto the side wall.",
              "The glass gives a rectangle from the front, a circle from the top and a rectangle from the side.",
              "Two objects that share one view usually differ in another."],
       examples=[
           WE("A cylinder of radius 3 cm and height 8 cm stands on its base. Draw its front, top and side views.",
              ["Front view: the width is the diameter 2 × 3 = 6 cm and the height is 8 cm, a rectangle.",
               "Top view: the round top, a circle of radius 3 cm.",
               "Side view: the same as the front, a 6 cm by 8 cm rectangle."],
              "Front and side views are 6 cm by 8 cm rectangles; the top view is a circle of radius 3 cm",
              ncert=["4.2.views", "4.2.views_fig46"])],
       key_terms=["front view", "top view", "side view", "vertical plane", "horizontal plane"], minutes=10),
     A("T11.C2", "Views of a stack of cubes", "Analyze",
       "Students draw the three views of a stack of identical cubes by looking along each direction and showing one "
       "square for every column seen.",
       teach=["Predict first: four cubes stand as three in a row with one more on top of the left cube. How many "
              "squares does the top view show?",
              "From the front you see the whole shape: an L of 4 squares.",
              "From the top the extra cube hides the cube under it: a row of 3 squares.",
              "From the side the row hides behind its first cube: a column of 2 squares."],
       examples=[
           WE("Four identical cubes: three in a row on the floor, and one more on top of the left cube. Draw its front, "
              "top and side views.",
              ["Front view: 3 squares in a row with 1 square on top of the left one, an L of 4 squares.",
               "Top view: looking down, the top cube covers the cube under it, so 3 squares in a row.",
               "Side view: looking from the left, the row is hidden behind one cube, so a column of 2 squares."],
              "Front: an L of 4 squares; top: a row of 3 squares; side: a column of 2 squares")],
       key_terms=["front view", "top view", "side view"], misconceptions=["M_ONE_PROFILE"], minutes=8),
     DOER("T11.C3", "Practice: see it from three sides", "views_viewer", "Analyze",
          "Students compare the views of different lines, draw the three views of common solids, and match everyday "
          "objects with their front, top and side views.",
          ["Front view on the vertical plane, top view on the horizontal plane, side view on the side plane.",
           "A cylinder: rectangle, circle, rectangle. A cone: triangle, circle, triangle."],
          items=[
              FIO("FiO4.q1", "Figure it Out (views of solids, question 1)",
                  "Observe the front view, top view and side view of the different lines in Fig. 4.6. Is there any "
                  "relation between their lengths?",
                  ["Each view is a projection, so no view is longer than the line itself.",
                   "A view shows the full length only when the line is parallel to that plane.",
                   "If a line goes a cm along, b cm deep and c cm up, the views have squared lengths a² + c², a² + b² "
                   "and b² + c².",
                   "Adding these gives twice a² + b² + c², which is twice the square of the line's length."],
                  "No view is longer than the line; the squares of the three view lengths add up to twice the square "
                  "of the line's length"),
              FIO("FiO4.q2", "Figure it Out (views of solids, question 2)",
                  "Find the front view, top view and side view of each of the following solids, fixing its orientation "
                  "with respect to the vertical, horizontal and side planes: cube, cuboid, parallelepiped, cylinder, "
                  "cone, prism, and pyramid.",
                  ["Cube on a face: three squares.",
                   "Cuboid on a face: three rectangles.",
                   "Parallelepiped leaning forward: a parallelogram from the side, rectangles from the front and top.",
                   "Cylinder standing: rectangle, circle, rectangle.",
                   "Cone standing: triangle from the front and side, a circle with its centre point from the top.",
                   "Triangular prism with its triangle facing front: a triangle from the front, rectangles from the top "
                   "and side.",
                   "Square pyramid standing: triangles from the front and side, a square with both diagonals from the "
                   "top."],
                  "Cube: squares; cuboid: rectangles; cylinder: rectangle, circle, rectangle; cone: triangle, circle, "
                  "triangle; prism: triangle and rectangles; pyramid: triangles and a square with diagonals"),
              FIO("FiO4.q3", "Figure it Out (views of solids, question 3)",
                  "Match each of the following objects with its projections: a jug, a funnel, a hammer, a car, a "
                  "slide, a chair, a ceiling fan and a pressure cooker, each with a front, a top and a side view.",
                  ["Jug: from the top a circle with a spout and a handle sticking out.",
                   "Funnel: front and side views are funnel shapes; from the top a circle with a dot at the centre.",
                   "Hammer: a long handle with the head seen end on from one side.",
                   "Car: a long rectangle from the top and a car profile from the side.",
                   "Slide: a ladder and a ramp in the side view.",
                   "Chair: a seat square from the top and a chair profile from the side.",
                   "Ceiling fan: blades seen edge on from the front and side, three blades from the top.",
                   "Pressure cooker: a pot with a handle from the front, a circle with a handle from the top."],
                  "Match each object by its most telling view, such as the circle with spout and handle for the jug "
                  "and three blades from the top for the fan")])],
    key_terms=["front view", "top view", "side view"]))

# ============================== T12 Shadows =================================================================
TOPICS.append(TOPIC(
    "T12", "M3", "Shadows and Parallel Lines", ["4.2"], "Analyze",
    "Students explain how the size of a torch shadow depends on distance, explain why sunlight shadows match "
    "projections, use the fact that parallel lines stay parallel, and draw and read the three views of stacks of "
    "cubes.",
    "A nearby torch makes a shadow larger than the object; the farther the torch, the closer the shadow is to the "
    "projection. Sunlight is so far away that its shadows are projections, and parallel lines project to parallel "
    "lines.",
    [A("T12.C1", "Torch shadows and sunlight", "Analyze",
       "Students explain with similar triangles why a torch shadow shrinks towards the size of the object as the "
       "torch moves away, and why sunlight shadows match projections.",
       textbook=["Shadows",
                 "Place an object in front of a plane, such as a wall of your room. Shine a torch light on the object "
                 "in a direction perpendicular to the wall. What do you see?",
                 "We will see that the shape of the shadow on a plane is quite similar to the shape of the projection "
                 "on that plane! However the shadow may be scaled up, stretched, or even distorted slightly, "
                 "depending on how the object is held.",
                 "Observe what happens to the size of the shadow as you vary the distance between your torch and your "
                 "object. Why does this happen?",
                 "Now, imagine your torch is extremely powerful and will continue casting a shadow of the object on "
                 "the wall, no matter how far back you move it.",
                 "If this imaginary torch always points in a direction perpendicular to the wall, then, as the "
                 "distance between the torch and the object increases, the shadow of the object will become "
                 "indistinguishable from the projection of the object to the wall plane!",
                 "Although this experiment may sound fanciful, you have encountered one such extremely powerful and "
                 "distant torch before, namely, the Sun! Indeed, when sunlight is perpendicular to a plane, the "
                 "shadows it casts on that plane are indistinguishable from projections!"],
       teach=["Predict first: you move a torch away from a toy in front of a wall. Does the shadow grow or shrink?",
              "Light spreads out from the torch, so the shadow is larger than the toy.",
              "Moving the torch back makes the rays nearly parallel, and the shadow shrinks towards the toy's own "
              "size.",
              "The Sun is so far away that its rays are parallel: its shadow on a wall it shines straight at is the "
              "projection."],
       examples=[
           WE("A toy 10 cm tall stands 50 cm in front of a wall. A torch shines straight at the wall from 50 cm in "
              "front of the toy. How tall is the shadow? What if the torch is moved to 150 cm in front of the toy?",
              ["The rays spread from the torch, so the shadow and the toy make similar triangles.",
               "Torch to wall is 50 + 50 = 100 cm, twice the torch to toy distance.",
               "Shadow = 10 × 100 ÷ 50 = 20 cm.",
               "With the torch at 150 cm, torch to wall is 150 + 50 = 200 cm.",
               "Shadow = 10 × 200 ÷ 150 ≈ 13.3 cm, closer to the toy's 10 cm."],
              "20 cm, then about 13.3 cm: the farther the torch, the closer the shadow is to the projection",
              ncert=["4.2.shadow_torch", "4.2.shadow_why", "4.2.shadow_sun"])],
       key_terms=["shadow", "parallel rays", "projection"], misconceptions=["M_SHADOW_SIZE"], minutes=10),
     A("T12.C2", "Parallel lines stay parallel", "Analyze",
       "Students use sunlight shadows of a parallelogram cutout to see that parallel lines project to parallel lines, "
       "and use this to predict shadows of a square tilted in different ways.",
       textbook=["Earlier we asked what the projection of a parallelogram might look like. You can now physically "
                 "answer this question by making a cutout of a parallelogram and viewing its shadows under sunlight. "
                 "No matter how you orient the parallelogram, you will see that the shadow remains a parallelogram!",
                 "More generally, the projection of a pair of parallel lines will always remain parallel. This "
                 "property is useful for drawing projections of objects."],
       teach=["Predict first: turn a square card in the sun. Can its shadow ever be a trapezium?",
              "Opposite sides of the card are parallel, and parallel lines cast parallel shadows, so the shadow is "
              "always a parallelogram, never a trapezium.",
              "Tilt the card about a diagonal: that diagonal keeps its length and the other one shrinks, so the shadow "
              "is a rhombus."],
       examples=[
           WE("A square card has diagonals of 10 cm. It is tilted in sunlight about one diagonal, so the other "
              "diagonal's shadow is 6 cm. What is the shadow, and how long is each side?",
              ["The diagonal on the hinge stays 10 cm; the other diagonal's shadow is 6 cm.",
               "The shadows of the diagonals still cross at right angles at their midpoints, and opposite sides stay "
               "parallel.",
               "So the shadow is a rhombus with diagonals 10 cm and 6 cm.",
               "Each side = √(5² + 3²) = √34, about 5.83 cm."],
              "A rhombus with sides of about 5.83 cm", ncert=["4.2.shadow_parallel"])],
       key_terms=["parallel", "shadow", "rhombus"], misconceptions=["M_PROJ_ANY"], minutes=8),
     DOER("T12.C3", "Practice: views and shadows of cube stacks", None, "Evaluate",
          "Students draw and read the three views of stacks of identical cubes, build stacks that match given views, "
          "count cubes in a stack, and list the shapes a cube's projection can make.",
          ["Draw one square for every column seen along the direction of view.",
           "Different stacks can share some views; use all three views together."],
          items=[
              FIO("FiO5.q1", "Figure it Out (shadows and views, question 1)",
                  "Draw the top view, front view and the side view of each of the following combinations of "
                  "identical cubes.",
                  ["Look along each direction in turn: front, top, side.",
                   "Draw one square for every column of cubes seen; a column hidden behind another adds nothing.",
                   "Check: the front and top views share the same width, and the front and side views share the same "
                   "height."],
                  "For each combination, one square per visible column in each direction, with matching widths and "
                  "heights across the views"),
              FIO("FiO5.q2", "Figure it Out (shadows and views, question 2)",
                  "Imagine eight identical cubes, glued together along faces to form the letter C. (i) This looks like "
                  "a C from the front. What does it look like from the side? From the top? (ii) Glue additional cubes "
                  "to make a shape that looks like one letter from the front and another from the top. (iii) Now, can "
                  "you glue even more cubes to make it look like three given letters from the front, top and side? "
                  "(iv) Can you think of other letter combinations to make with a single combination of cubes in this "
                  "manner?",
                  ["The C is 4 cubes tall: a row of 3 on top, 1 cube on the left in each of the two middle rows, and "
                   "a row of 3 at the bottom, 3 + 1 + 1 + 3 = 8.",
                   "From the side every row hides behind its first cube: a column of 4 squares, like the letter I.",
                   "From the top the rows stack under each other: a row of 3 squares.",
                   "For (ii) to (iv), add cubes behind the front letter so the top view spells the second letter, "
                   "then check the side view."],
                  "(i) From the side a column of 4 squares, from the top a row of 3 squares; (ii) to (iv) are built "
                  "by adding cubes behind the letter"),
              FIO("FiO5.q3", "Figure it Out (shadows and views, question 3)",
                  "Which solid corresponds to the given top view, front view, and side view?",
                  ["A circle in one view and rectangles in the others: a cylinder.",
                   "A circle in one view and triangles in the others: a cone.",
                   "A triangle in one view and rectangles in the others: a triangular prism.",
                   "A square with diagonals and triangles: a square pyramid; three squares: a cube."],
                  "Read the most unusual view first, then check the other two against the solid")
              ,
              FIO("FiO5.q4", "Figure it Out (shadows and views, question 4)",
                  "Using identical cubes, make a solid that gives the following projections.",
                  ["Start from the top view: place one column of cubes on each square.",
                   "Use the front view to set the tallest column in each line from left to right.",
                   "Use the side view to set the tallest column in each line from front to back.",
                   "Build it and check all three views."],
                  "Columns placed on the top view squares, with heights fixed by the front and side views"),
              FIO("FiO5.q5", "Figure it Out (shadows and views, question 5)",
                  "Find the number of cubes in this stack of identical cubes.",
                  ["Read the stack as a staircase in a corner, with every visible cube resting on cubes below it.",
                   "Count by layers from the top: 1, then 3, then 6, then 10.",
                   "Total = 1 + 3 + 6 + 10 = 20."],
                  "20 cubes, if every hidden place under a visible cube is filled"),
              FIO("FiO5.q6", "Figure it Out (shadows and views, question 6)",
                  "What are the different shapes the projection of a cube can make under different orientations?",
                  ["Face on to the plane: a square.",
                   "Turned about one edge: a rectangle (two faces show).",
                   "Turned so three faces show: a hexagon, and a regular hexagon when it balances on a corner."],
                  "A square, a rectangle or a hexagon")])],
    key_terms=["shadow", "projection", "parallel"]))

# ============================== T13 Isometric projection ====================================================
TOPICS.append(TOPIC(
    "T13", "M3", "Isometric Projection and Drawing", ["4.2"], "Create",
    "Students explain why a cube balanced on a corner projects to a regular hexagon, draw solids made of cubes on an "
    "isometric grid by counting edges along the length, depth and height directions, and explain why impossible "
    "figures fool the eye.",
    "In an isometric projection all edges of a cube project to equal lengths, giving a regular hexagon. Tiling "
    "hexagons gives an isometric grid with three directions for length, depth and height, and equal units along "
    "each.",
    [A("T13.C1", "A cube on its corner: the regular hexagon", "Understand",
       "Students describe the isometric projection of a cube balanced on a corner, explain why all its projected edges "
       "are equal, and see how tiling the hexagons gives the isometric grid.",
       textbook=["Isometric Projections",
                 "In general we lose information when projecting a solid to a plane. But depending on the orientation "
                 "of the solid, we can sometimes recover much of the information we've lost.",
                 "Let us consider an orientation of a cube in which the lengths of the projections of all the edges of "
                 "the cube are equal. Such a projection is called the isometric projection of the cube. 'Isometric' "
                 "means 'equal measure' in Greek.",
                 "Imagine balancing a cube perfectly on one of its corner vertices, and then projecting it down to the "
                 "floor plane. This projection is isometric.",
                 "Construct a model of a cube and use your hands to keep it balanced on one corner vertex. Can you try "
                 "to understand why all the projected edges have equal length?",
                 "The isometric representation of a cube is a regular hexagon. If the cube is made of glass, then all "
                 "the edges would be visible.",
                 "This structure is the basis for isometric drawing! Tile the plane with hexagons and we get an "
                 "isometric grid.",
                 "Isometric grids are widely used in engineering. They make it easy to draw projections of solids and "
                 "to measure lengths along all the 3 primary directions, length, depth and height, as shown in Fig. "
                 "4.7."],
       teach=["Predict first: balance a cube on one corner and look straight down. What outline do you see?",
              "The cube looks the same after a turn of a third of a full turn about that corner, so its edges come in "
              "matching sets that all slope the same way: their projections are equal.",
              "The outline is a regular hexagon, with three edges meeting at its centre.",
              "Fit many such hexagons together and the lines form the isometric grid."],
       examples=[
           WE("A glass cube balanced on a corner is projected onto the floor. How many of its 12 edges form the "
              "hexagon outline, and how many lie inside it?",
              ["The top and bottom corners both project to the centre of the hexagon.",
               "The 3 edges at the top corner and the 3 at the bottom corner run from the centre outwards: 3 + 3 = 6 "
               "inside.",
               "The remaining 12 − 6 = 6 edges form the outline.",
               "All 12 projections have the same length, so the outline is a regular hexagon."],
              "6 edges make the regular hexagon and 6 run inside from its centre",
              ncert=["4.2.iso_cube", "4.2.mt_iso_equal", "4.2.iso_grid"])],
       key_terms=["isometric", "regular hexagon", "isometric grid"], misconceptions=["M_ISO_PERSPECTIVE"], minutes=8),
     A("T13.C2", "Drawing edge by edge on the grid", "Apply",
       "Students draw a 1 by 1 by 1 cube, a 2 by 2 by 2 cube and a row of four cubes on an isometric grid by counting "
       "units along the height, length and depth directions.",
       textbook=["Drawing on Isometric Grids",
                 "Have you played Tetris? There are five basic shapes in Tetris, corresponding to the different ways "
                 "of arranging four squares. Imagine these are cubes, not squares. Draw each of these on your "
                 "isometric paper (you can find it at the end of the book).",
                 "As seen in Fig. 4.7, there are three principal axes of the solid shape, which we will call the depth "
                 "axis, length axis, and height axis. The edges of the grid appear in three different orientations. "
                 "We will associate height to the vertical lines, and depth and length to the two slanting families.",
                 "While drawing on the grid, it may be useful to draw edge by edge, counting the number of units you "
                 "want to go along a given axis. For example, you can draw a 1 × 1 × 1 cube as follows. How would you "
                 "draw a 2 × 2 × 2 cube? Feel free to add shading, if it helps you visualise the solid.",
                 "The first tetris shape is a row of four cubes joined face-to-face. In order to draw this solid, you "
                 "will need to choose an orientation for the row of four cubes.",
                 "Let's draw it oriented along the depth axis. You could draw it cube-by-cube, but in that case you "
                 "may need to erase the lines that get hidden by additional cubes. (If you don't have an eraser, you "
                 "can also draw faint lines initially, and then darken the visible ones later.)",
                 "You could also draw it all at once, by counting edges as you go.",
                 "Similarly, you could draw the shape oriented along the height axis or the length axis."],
       teach=["Predict first: a 2 by 2 by 2 cube is drawn on the grid. How many units long is each visible edge?",
              "Vertical lines are height; the two slanting families are length and depth.",
              "Draw the front vertical edge first, then go round the top, then the side, counting units.",
              "A solid box shows 9 edges: 3 along each direction."],
       examples=[
           WE("Draw a 2 by 2 by 2 cube on an isometric grid. How many units of line do its visible edges use?",
              ["A box seen in isometric shows 9 edges: 3 along height, 3 along length, 3 along depth.",
               "Each edge of this cube is 2 units long.",
               "Total = 9 × 2 = 18 units."],
              "18 units of line over 9 visible edges",
              ncert=["4.2.tetris", "4.2.iso_axes_cube", "4.2.iso_row"])],
       key_terms=["isometric grid", "length axis", "depth axis", "height axis"], minutes=10),
     A("T13.C3", "Why the grid works", "Evaluate",
       "Students explain that parallel edges of a solid stay parallel and unit lengths stay equal on the grid, and use "
       "this to draw a cuboid and the other tetris shapes.",
       textbook=["In your drawing, moving in the vertical direction on the isometric paper corresponds to moving along "
                 "the height axis of the solid. Similarly, moving along the two slanting directions on the paper "
                 "corresponds to moving along the length or depth axis respectively of the solid.",
                 "Why is this correspondence between directions on isometric paper and axes of the solid so effective "
                 "for communicating the shape of the solid?",
                 "Earlier we observed that parallel lines project to parallel lines. This geometric fact ensures that "
                 "the three families of parallel edges on the solid (corresponding to height, the length, and depth) "
                 "project to three families of parallel edges on the isometric paper. Moreover, the isometric nature "
                 "of the projection ensures that the projections of unit distances along the three axes are equal.",
                 "Can you try drawing the other tetris shapes on isometric paper?"],
       teach=["Predict first: on the grid, is a 3 unit edge along the depth shown longer, shorter or the same as a 3 "
              "unit edge along the height?",
              "The same: isometric means equal measure along all three directions.",
              "Parallel edges of a box stay parallel on the paper, so each family of edges gets its own direction.",
              "So any solid made of cubes can be drawn just by counting units."],
       examples=[
           WE("Draw a cuboid 1 unit long, 2 units deep and 3 units tall on the grid. How many units of line do its "
              "visible edges use?",
              ["3 visible edges along length, each 1 unit: 3 × 1 = 3.",
               "3 visible edges along depth, each 2 units: 3 × 2 = 6.",
               "3 visible edges along height, each 3 units: 3 × 3 = 9.",
               "Total = 3 + 6 + 9 = 18 units."],
              "18 units of line", ncert=["4.2.iso_why", "4.2.iso_others"])],
       key_terms=["isometric", "parallel", "equal measure"], misconceptions=["M_ISO_PERSPECTIVE"], minutes=8),
     DOER("T13.C4", "Practice: draw it on isometric paper", "iso_grid_builder", "Create",
          "Students find and draw all the ways of gluing four cubes, copy given figures on the isometric grid and "
          "explain what makes the impossible ball path and the impossible triangle impossible.",
          ["Vertical is height; the two slanting directions are length and depth.",
           "Count units along one direction at a time and erase hidden lines."],
          items=[
              FIO("FiO6.q1", "Figure it Out (isometric drawing, question 1)",
                  "In addition to the 5 ways shown in Fig. 4.8, are there any additional ways of gluing four cubes "
                  "together along faces? Can you visualise and draw these as well?",
                  ["The 5 tetris shapes all lie flat.",
                   "Lift one cube out of the flat plane: an L of three cubes with a fourth cube on top of the corner "
                   "cube gives the tripod, three arms meeting at a corner.",
                   "An S shape with one end lifted up gives a twisted screw, and its mirror image twists the other "
                   "way.",
                   "So there are 3 more, 5 + 3 = 8 in all."],
                  "Yes: 3 more, the tripod and two mirror image screws, for 8 ways in all"),
              FIO("FiO6.q2", "Figure it Out (isometric drawing, question 2)",
                  "Draw the following figures on the isometric grid.",
                  ["Choose a starting corner and decide for each edge which direction it runs: height, length or "
                   "depth.",
                   "Decide whether the edge goes up or down, forward or back, and draw along or against that "
                   "direction.",
                   "Count units for each edge, then erase hidden lines."],
                  "Each figure is drawn edge by edge along the three grid directions, counting units"),
              FIO("FiO6.q3", "Figure it Out (isometric drawing, question 3)",
                  "Is there anything strange about the path of this ball? Recreate it on the isometric grid.",
                  ["Follow the path: every step seems to go down, yet the path returns to where it began.",
                   "Each small piece can be built, but the pieces cannot all join in real space.",
                   "On the isometric grid, points at different depths can land on the same spot, which hides the "
                   "break."],
                  "Yes: the ball keeps going down yet comes back to its start, which is impossible in real space"),
              FIO("FiO6.q4", "Figure it Out (isometric drawing, question 4)",
                  "Observe this triangle. (i) Would it be possible to build a model out of actual cubes? What are the "
                  "front, top, and side profiles of this impossible triangle? (ii) Recreate this on an isometric grid. "
                  "(iii) Why does the illusion work?",
                  ["(i) No: each corner looks like a right angle bend, but three such bends cannot close into a "
                   "triangle in real space. A real model of rows of cubes looks right only from one viewpoint.",
                   "(ii) Draw each arm as a row of cubes along a grid direction and join the ends where they appear "
                   "to meet.",
                   "(iii) An isometric drawing loses depth: a near end and a far end can project to the same point, so "
                   "the eye joins them."],
                  "It cannot be built; the illusion works because the projection loses depth, so far and near ends "
                  "appear to touch")])],
    key_terms=["isometric", "isometric grid", "tetris"]))

# ============================== T14 Summary =================================================================
TOPICS.append(TOPIC(
    "T14", "M3", "Summary: Exploring Some Geometric Themes", ["Summary"], "Remember",
    None,
    "Fractals repeat a rule; nets fold into solids and give shortest paths; front, top and side views and isometric "
    "drawings show solids on paper.",
    [A("T14.C1", "What we found about shapes and solids", "Remember",
       "Students restate how fractals are built by repeating a rule, which solids can be folded from nets, how nets "
       "give shortest paths, and how views and isometric drawings show solids on a plane.",
       textbook=["Fractals are self-similar geometric objects found in nature and in art.",
                 "The Sierpinski Carpet, Sierpinski Gasket, and Koch Snowflake are some examples of mathematical "
                 "fractals. They can be obtained by repeatedly applying certain geometric operations that generate a "
                 "sequence of shapes approaching the fractal.",
                 "Cuboids, tetrahedrons, cylinders, cones, prisms, pyramids, and octahedrons are some of the solids "
                 "that can be obtained by folding suitable nets.",
                 "The shortest path between two points on the surface of a cuboid can be found by using a suitable net "
                 "of the cuboid.",
                 "Any object can be represented on a plane surface by using its projections on plane surfaces. For "
                 "this purpose, we generally use the front view (projection on the vertical plane), top view "
                 "(projection on the horizontal plane), and side view (projection on the side plane) of the object.",
                 "A cube can be oriented such that the lengths of all its edges in the projection are equal. Such a "
                 "projection is called the isometric projection. Isometric projections of different solids can be "
                 "drawn using isometric grid paper."],
       teach=["Our opening fern is explained: a fractal repeats one rule, so every part looks like the whole.",
              "Nets turn solids into flat shapes, and a straight line on the right net is the shortest path on a box.",
              "Front, top and side views, shadows and isometric drawings put solids on paper. Still open for you: "
              "draw one object at home in all three views and on isometric paper."],
       ncert=["summary"], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
