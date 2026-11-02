# -*- coding: utf-8 -*-
"""Topics T5 to T9 (module M2: visualising and making solids). Book section 4.2, pp 75 to 87."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T5 Build it in your imagination =============================================
TOPICS.append(TOPIC(
    "T5", "M2", "Build It in Your Imagination", ["4.2"], "Analyze",
    "Students picture cuts of a square and a triangle without drawing, name the shapes that are left, and describe "
    "solids and viewpoints that give a square, circular, triangular or two contrasting profiles.",
    "Cutting the corners of a square at the midpoints leaves a square of half the area; cutting a triangle at the "
    "thirds leaves a regular hexagon, and a square cut at the thirds leaves an octagon that is not regular. A solid "
    "shows different profiles from different viewpoints, and one profile can come from many solids.",
    [A("T5.C1", "Cutting corners in the mind", "Analyze",
       "Students visualise cutting the four corners of a square at the midpoints of its edges, name the shape left, "
       "and explain how the four corners make another square of the same area.",
       textbook=["4.2 Visualising Solids",
                 "Build it in Your Imagination",
                 "We will start this section by practising visualisation. For each prompt, feel free to talk to your "
                 "partner, gesture, draw it in the air, but do not actually draw on paper!",
                 "My method is different. I do not rush into actual work. When I get an idea I start at once building "
                 "it up in my imagination. I change the construction, make improvements, and operate the device "
                 "entirely in my mind. (Nikolas Tesla, 1856 to 1943, the great Serbian-American engineer and inventor)",
                 "1. Picture your name, then read off the letters backwards. Make sure to do this by sight, not by "
                 "sound, really see your name! Now try with your friend's name.",
                 "2. Cut off the four corners of an imaginary square, with each cut going between midpoints of "
                 "adjacent edges. What shape is left over? How can you reassemble the four corners to make another "
                 "square?"],
       teach=["Predict first: close your eyes and cut the four corners of a square from midpoint to midpoint. What "
              "shape is left, and is it bigger or smaller than the four corners put together?",
              "The four cuts are equal and meet at right angles, so a smaller square is left, standing on a corner.",
              "Each corner is a right triangle; turn the four triangles so their right angles meet at the centre and "
              "they form another square.",
              "The two squares have the same area, each half of the starting square."],
       examples=[
           WE("A square has side 4 cm. Its corners are cut off from midpoint to midpoint. Find the area of the square "
              "that is left and of the square made from the four corners.",
              ["The starting square has area 4 × 4 = 16 square cm.",
               "Each corner triangle has two sides of 2 cm at a right angle: area 2 × 2 ÷ 2 = 2 square cm.",
               "The four corners together: 4 × 2 = 8 square cm, and they fit together into a square.",
               "The square left over: 16 − 8 = 8 square cm."],
              "Both squares have area 8 square cm, half of the starting square",
              ncert=["4.2.imagine_intro", "4.2.imagine_square"])],
       key_terms=["visualise", "midpoint", "square"], minutes=8),
     A("T5.C1x", "Cutting at the thirds: hexagon or octagon?", "Analyze",
       "Students visualise cutting the corners of an equilateral triangle and of a square at the thirds of each side "
       "and decide whether the shapes left are regular.",
       textbook=["3. Mark the sides of an equilateral triangle into thirds. Cut off each corner of the triangle, as far "
                 "as the marks. What shape do you get?",
                 "4. Mark the sides of a square into thirds and cut off each of its corners as far as the marks. What "
                 "shape is left?"],
       teach=["Predict first: a triangle loses 3 corners and a square loses 4. How many sides does each shape left "
              "have, and are all its sides equal?",
              "Each corner of the triangle cut at the thirds is a small equilateral triangle, so all 6 sides left are "
              "equal: a regular hexagon.",
              "Each corner of the square cut at the thirds is a right triangle whose slanted side is longer than a "
              "third, so the octagon has two side lengths and is not regular."],
       examples=[
           WE("Cut the corners at the thirds of an equilateral triangle of side 9 cm and of a square of side 9 cm. "
              "Find the side lengths of the shapes left.",
              ["Triangle: each side keeps its middle third of 9 ÷ 3 = 3 cm.",
               "Each cut corner is an equilateral triangle of side 3 cm, so each cut edge is 3 cm: a regular "
               "hexagon of side 3 cm.",
               "Square: each side keeps its middle third of 3 cm.",
               "Each cut edge is the slanted side of a right triangle with sides 3 cm and 3 cm: √(3² + 3²) = √18, "
               "about 4.24 cm.",
               "So the octagon has sides 3 cm and about 4.24 cm, and it is not regular."],
              "A regular hexagon of side 3 cm; an octagon with sides 3 cm and about 4.24 cm, not regular",
              ncert=["4.2.imagine_triangle", "4.2.imagine_octagon"])],
       key_terms=["hexagon", "octagon", "regular"], minutes=6, thin=True),
     A("T5.C2", "Profiles: one solid, many outlines", "Analyze",
       "Students describe a solid and a viewpoint that give a square, a circular or a triangular profile, and explain "
       "that one solid can show different profiles from different viewpoints.",
       textbook=["When we see a solid object, we are really seeing its profile from a specific viewpoint. Depending on "
                 "our viewpoint, the outline of this profile can vary dramatically!",
                 "Perhaps you've noticed interesting profiles of objects yourself, while taking a photograph or "
                 "observing the shadow of an object? Or, maybe you've seen a cartoon in which a character bursts "
                 "through a wall and leaves a hole shaped like their outline!",
                 "In previous classes, you've seen solids that are much simpler than an elephant or cat, such as "
                 "cubes, spheres, cylinders, and cones. What would the profiles of these look like, from different "
                 "viewpoints?",
                 "Can you describe a solid and a viewpoint that would result in each of the following cases? If it "
                 "helps, you can imagine the solid passing through a wall like Tom did, and leaving a hole of the "
                 "appropriate shape.",
                 "5. A solid whose profile has a square outline",
                 "6. A solid whose profile has a circular outline",
                 "7. A solid whose profile has a triangular outline"],
       teach=["Predict first: a tin can passes through a paper wall. What shape is the hole if it goes in lid first, "
              "and what if it goes in lying on its side?",
              "Lid first: a circle. Lying on its side: a rectangle. One solid, two profiles.",
              "A cube face on gives a square; a sphere from any side gives a circle; a cone seen from the side gives a "
              "triangle."],
       examples=[
           WE("A tin can is a cylinder with radius 3 cm and height 10 cm. What profile does it show from directly "
              "above, and what from the side?",
              ["From directly above you see the round lid: a circle of radius 3 cm.",
               "From the side you see the height and the width: a rectangle.",
               "The width of the rectangle is the diameter, 2 × 3 = 6 cm, and its height is 10 cm."],
              "A circle of radius 3 cm from above; a 6 cm by 10 cm rectangle from the side",
              ncert=["4.2.profile_intro", "4.2.profile_square", "4.2.profile_circle", "4.2.profile_triangle"])],
       key_terms=["profile", "viewpoint", "outline"], misconceptions=["M_ONE_PROFILE"], minutes=10),
     A("T5.C2x", "Two profiles at once", "Create",
       "Students find solids that show two given contrasting profiles from two viewpoints and give more than one "
       "solid for the same pair.",
       textbook=["As we saw with the elephant, a given solid might have very different profiles from different "
                 "viewpoints. Can you visualise solids that have the following contrasting profiles?",
                 "8. A solid with a rectangular profile from one viewpoint and a circular profile from another "
                 "viewpoint",
                 "9. A solid with a circular profile from one viewpoint and a triangular one from another viewpoint",
                 "10. A solid with a rectangular profile from one viewpoint and a triangular one from another viewpoint",
                 "11. A solid with a trapezium shaped profile from one viewpoint and a circular one from another "
                 "viewpoint",
                 "12. A solid with a pentagonal profile from one viewpoint and a rectangular one from another viewpoint",
                 "Are there unique solids for each of the conditions, or can you come up with multiple possibilities?"],
       teach=["Predict first: which everyday object looks like a trapezium from the side and a circle from above?",
              "A bucket: its sides slope out, so from the side its outline is a trapezium; from above it is round.",
              "Rectangle and circle: a cylinder. Circle and triangle: a cone. Rectangle and triangle: a tent shaped "
              "triangular prism. Pentagon and rectangle: a pentagonal prism, like a hut.",
              "Each pair has more than one answer, so the solids are not unique."],
       examples=[
           WE("Give two different solids that each show a rectangular profile from one viewpoint and a triangular "
              "profile from another.",
              ["A tent shaped triangular prism: from the front a triangle, from the side a rectangle.",
               "A square pyramid seen from the side gives a triangle, but from above it gives a square, which is a "
               "rectangle with equal sides.",
               "So both a triangular prism and a square pyramid work, and there are more."],
              "A triangular prism and a square pyramid, among others",
              ncert=["4.2.profile_pairs", "4.2.profile_unique"])],
       key_terms=["profile", "viewpoint"], misconceptions=["M_ONE_PROFILE"], minutes=6, thin=True),
     DOER("T5.C3", "Practice: picture it before you draw it", None, "Create",
          "Students picture each visualisation prompt in their heads, then draw a sketch to check, and give at least "
          "two solids for each pair of profiles.",
          ["Picture first, then check with a sketch or an object at home.",
           "A cylinder, a cone, a prism and a bucket give the contrasting profiles; most pairs have more than one "
           "answer."],
          examples=[
              WE("A cylinder has radius 7 cm and height 14 cm. Picture it before you draw it: what profile does it "
                 "show from the side, and what from directly above?",
                 ["From the side you see its width and its height.",
                  "The width is the diameter: 2 × 7 = 14 cm, and the height is 14 cm.",
                  "Width and height are equal, so the side profile is a square of side 14 cm.",
                  "From directly above you see the round top: a circle of radius 7 cm."],
                 "A square of side 14 cm from the side and a circle of radius 7 cm from above")])],
    key_terms=["visualise", "profile", "viewpoint"]))

# ============================== T6 Prisms and pyramids ======================================================
TOPICS.append(TOPIC(
    "T6", "M2", "Faces, Edges and Vertices of Prisms and Pyramids", ["4.2"], "Analyze",
    "Students name faces, edges and vertices, define prisms and pyramids, and find the numbers of faces, edges and "
    "vertices of a prism and a pyramid with a 10 sided or an n sided polygon.",
    "A cube has 6 faces, 12 edges and 8 vertices. A prism on an n sided polygon has n + 2 faces, 3n edges and 2n "
    "vertices; a pyramid on an n sided base has n + 1 faces, 2n edges and n + 1 vertices.",
    [A("T6.C1", "Faces, edges and vertices", "Understand",
       "Students identify the faces, edges and vertices of solids made from flat materials and count them for a "
       "cuboid and a triangular prism.",
       textbook=["Making Solids",
                 "Many basic solid shapes such as a cuboid, parallelopiped, cylinder, cone, prism, and pyramid can be "
                 "made using foldable flat materials like paper, cardboard, and even metallic sheets! This is one of "
                 "the methods for manufacturing hollow solids.",
                 "While discussing solids that contain plane surfaces in their boundaries, the notion of faces, edges "
                 "and vertices serves a useful purpose.",
                 "Faces are the plane/flat surfaces of a solid that form its boundary. Edges are the line segments that "
                 "form the sides of the faces, and vertices are the points at which the edges meet. For example, a "
                 "cuboid or cube has 6 faces, 12 edges and 8 vertices."],
       teach=["Predict first: hold a matchbox. How many flat faces, straight edges and corners does it have?",
              "6 faces, 12 edges, 8 vertices: 4 edges around the top, 4 around the bottom and 4 upright.",
              "A triangular prism (like a tent) has 2 triangles and 3 rectangles."],
       examples=[
           WE("Count the faces, edges and vertices of a triangular prism.",
              ["Faces: 2 triangles and 3 rectangles, so 2 + 3 = 5.",
               "Edges: 3 on each triangle and 3 joining them, so 3 + 3 + 3 = 9.",
               "Vertices: 3 on each triangle, so 3 + 3 = 6."],
              "5 faces, 9 edges, 6 vertices", ncert=["4.2.solids_make", "4.2.fev_cube"])],
       key_terms=["face", "edge", "vertex"], minutes=8),
     A("T6.C2", "Counting the parts of a prism", "Analyze",
       "Students use the definition of a prism to find the faces, edges and vertices of a prism whose congruent "
       "polygons have 10 sides, and then n sides.",
       textbook=["There are multiple types of prisms and pyramids, whose names depend on the shapes of their faces.",
                 "Prism: A prism, in general, has two congruent polygons as opposite faces, with edges connecting the "
                 "corresponding vertices of these polygons. All the other faces are parallelograms. Based on the shape "
                 "of the congruent polygons, prisms may be called triangular prisms, pentagonal prisms, and so on.",
                 "If the congruent polygons of a prism have 10 sides, how many faces, edges and vertices does the "
                 "prism have? What if the polygons have n sides?"],
       teach=["Predict first: a prism on a 10 sided polygon. How many side faces does it need?",
              "One parallelogram face for each side of the polygon: 10, plus the 2 polygons.",
              "Edges: 10 on the top polygon, 10 on the bottom, 10 joining them. Vertices: 10 on each polygon.",
              "For n sides: n + 2 faces, 3n edges, 2n vertices."],
       examples=[
           WE("A prism has two congruent 10 sided polygons as opposite faces. Find its faces, edges and vertices.",
              ["Faces: 10 parallelograms and 2 polygons, 10 + 2 = 12.",
               "Edges: 10 + 10 + 10 = 30.",
               "Vertices: 10 + 10 = 20."],
              "12 faces, 30 edges, 20 vertices; for n sides, n + 2 faces, 3n edges and 2n vertices",
              ncert=["4.2.prism_def", "4.2.prism_count"])],
       key_terms=["prism", "congruent polygons", "parallelogram"], misconceptions=["M_PRISM_PYRAMID"], minutes=8),
     A("T6.C3", "Counting the parts of a pyramid", "Analyze",
       "Students use the definition of a pyramid to find the faces, edges and vertices of a pyramid with a 10 sided "
       "base, and then an n sided base.",
       textbook=["Pyramids: A pyramid, in general, has a polygonal base and a point outside it, and edges connect the "
                 "point with each of the vertices of the base. Based on the shape of the base, pyramids may be called "
                 "triangular pyramids, square pyramids, pentagonal pyramids, and so on. A triangular pyramid is also "
                 "known as a tetrahedron.",
                 "If the base of a pyramid has 10 sides, how many faces, edges and vertices does the pyramid have? "
                 "What if the base is an n-sided polygon?"],
       teach=["Predict first: a pyramid and a prism both on a 10 sided polygon. Which has more edges?",
              "The pyramid has one triangle on each side of the base: 10 triangles plus the base.",
              "Edges: 10 around the base and 10 up to the apex. Vertices: 10 on the base and the apex.",
              "For n sides: n + 1 faces, 2n edges, n + 1 vertices."],
       examples=[
           WE("A pyramid has a 10 sided base. Find its faces, edges and vertices.",
              ["Faces: 10 triangles and the base, 10 + 1 = 11.",
               "Edges: 10 + 10 = 20.",
               "Vertices: 10 + 1 = 11."],
              "11 faces, 20 edges, 11 vertices; for n sides, n + 1 faces, 2n edges and n + 1 vertices",
              ncert=["4.2.pyramid_def", "4.2.pyramid_count"])],
       key_terms=["pyramid", "base", "apex", "tetrahedron"], misconceptions=["M_PRISM_PYRAMID"], minutes=8),
     DOER("T6.C4", "Practice: count faces, edges and vertices", "solid_parts_counter", "Apply",
          "Students count the faces, edges and vertices of prisms and pyramids on different polygons and use the "
          "general rules to check their counts.",
          ["Prism on n sides: n + 2 faces, 3n edges, 2n vertices.",
           "Pyramid on n sides: n + 1 faces, 2n edges, n + 1 vertices."],
          examples=[
              WE("A gift box is a prism on an octagon, and its lid is a pyramid on the same octagon. Find the faces, "
                 "edges and vertices of each.",
                 ["Prism, n = 8: faces 8 + 2 = 10, edges 3 × 8 = 24, vertices 2 × 8 = 16.",
                  "Pyramid, n = 8: faces 8 + 1 = 9, edges 2 × 8 = 16, vertices 8 + 1 = 9.",
                  "Check the prism: faces + vertices − edges = 10 + 16 − 24 = 2.",
                  "Check the pyramid: 9 + 9 − 16 = 2."],
                 "Octagonal prism: 10 faces, 24 edges, 16 vertices; octagonal pyramid: 9 faces, 16 edges, 9 "
                 "vertices")])],
    key_terms=["face", "edge", "vertex", "prism", "pyramid"]))

# ============================== T7 Nets of a cube and a cuboid ==============================================
TOPICS.append(TOPIC(
    "T7", "M2", "Nets of a Cube and a Cuboid", ["4.2"], "Analyze",
    "Students explain what a net is, visualise folding the cross shaped net into a cube, decide which arrangements of "
    "six squares are nets of a cube, find all 11 nets and draw nets of cuboids with given side lengths.",
    "A net is a solid unfolded onto a plane. Six squares fold into a cube only when no two land on the same face; a "
    "cube has 11 nets. A cuboid net has three pairs of equal rectangles.",
    [A("T7.C1", "What is a net? Folding the cross", "Understand",
       "Students describe a net as a solid unfolded onto a plane, visualise folding the cross shaped net into a cube "
       "and name the pairs of opposite faces.",
       textbook=["Now we will see how to make different solids using a foldable flat surface such as paper, cardboard, "
                 "etc.",
                 "The basic idea is to create a shape on a flat surface that can be folded into the solid. Such a "
                 "shape is called a net. In other words, a net is obtained by 'unfolding' a solid onto a plane.",
                 "What is a net of a cube? Fig. 4.1 is a net of a cube.",
                 "Visualise how it can be folded to form a cube.",
                 "Practical Aspects of Using a Net: To make an actual cube from its net, certain practical aspects have "
                 "to be kept in mind. One is that the material used must have sufficient sturdiness for the cube to "
                 "stand. The second aspect is that there should be some mechanism for attaching the faces together. If "
                 "cardboard or a similar material is used, cello tape is one way to join the adjacent faces. For less "
                 "sturdy materials, such as chart paper, it is useful to have extra 'flaps' on some of the faces that "
                 "can be stuck to the adjacent faces.",
                 "However, when we talk about the net of a solid, we consider only the shape formed by unfolding the "
                 "solid, and not the other supporting flaps that we may use to actually make the solid.",
                 "There are multiple possible nets one can use to build a cube."],
       teach=["Predict first: in the cross shaped net, which square ends up opposite the bottom square?",
              "Fold the four squares around the bottom up to make the walls; the last square closes the lid.",
              "In a straight line of squares, squares with one square between them become opposite faces.",
              "Flaps help the cube hold together, but they are not part of the net."],
       examples=[
           WE("A cross shaped net has a column of four squares A, B, C, D from top to bottom, and two squares L and R "
              "on either side of B. Fold it into a cube with B as the bottom. Which faces are opposite each other?",
              ["B is the bottom; A, C, L and R fold up as the four walls.",
               "D is attached to C, so it folds over the top: D is opposite B.",
               "A and C are on opposite sides of B, so they are opposite walls.",
               "L and R are on opposite sides of B, so they are opposite walls too."],
              "B and D, A and C, L and R are the pairs of opposite faces",
              ncert=["4.2.net_def", "4.2.net_fold", "4.2.net_practical"])],
       key_terms=["net", "unfold", "opposite face"], minutes=8),
     A("T7.C2", "Will these six squares fold into a cube?", "Analyze",
       "Students test an arrangement of six squares by folding it in the mind, find where two faces would overlap, "
       "and decide whether it is a net of a cube.",
       teach=["Predict first: a row of four squares with both extra squares above the same end square. Will it fold "
              "into a cube?",
              "The row of four wraps round to make four walls. One extra square becomes the lid.",
              "The other extra square is attached to the lid, so it folds down onto a wall that is already there: two "
              "faces overlap and the bottom stays open.",
              "With a row of four, one extra square must go above the row and one below."],
       examples=[
           WE("Six squares: a row of four, one square above the first square of the row, and one more square to the "
              "left of that square. Is it a net of a cube?",
              ["The row of four folds round into four walls; call the first square the front.",
               "The square above the front folds over as the lid.",
               "The last square is attached to the left edge of the lid, so it folds down onto the left wall.",
               "Two faces land on the left wall and the bottom is missing."],
              "No, it is not a net of a cube")],
       key_terms=["net", "overlap"], misconceptions=["M_ANY_SIX"], minutes=8),
     A("T7.C3", "Drawing a net of a cuboid", "Apply",
       "Students draw a net of a cuboid with given side lengths by pairing equal rectangles, and check it with the "
       "total area.",
       teach=["Predict first: a cuboid has 6 faces. How many different sizes of rectangle does its net need?",
              "Opposite faces are equal, so there are 3 pairs: length by breadth, length by height, breadth by height.",
              "Draw a row of four walls whose heights match, then the top and bottom on the long edges.",
              "Every pair of edges that will be glued together must have the same length."],
       examples=[
           WE("Draw a net of a cuboid 4 cm by 2 cm by 1 cm and find the area of the net.",
              ["Rectangles needed: two of 4 cm by 2 cm, two of 4 cm by 1 cm, two of 2 cm by 1 cm.",
               "Draw the walls in a row: 4 by 1, 2 by 1, 4 by 1, 2 by 1, all 1 cm tall.",
               "Attach two 4 by 2 rectangles above and below a 4 by 1 wall as the top and bottom.",
               "Area = 2 × (8 + 4 + 2) = 28 square cm."],
              "A net of six rectangles with area 28 square cm")],
       key_terms=["cuboid", "net", "rectangle"], minutes=8),
     DOER("T7.C4", "Practice: fold the net", "cube_net_folder", "Analyze",
          "Students decide which arrangements of six squares fold into a cube, collect the 11 nets of a cube and draw "
          "nets of cuboids with given side lengths.",
          ["Visualise first, then fold to check.",
           "With a row of four, one square above and one below; there are 11 nets of a cube in all.",
           "A cuboid net has three pairs of equal rectangles."],
          items=[
              FIO("FiO3.q1", "Figure it Out (nets, question 1)",
                  "Which of the following are the nets of a cube? First, try to answer by visualisation. Then, you may "
                  "use cutouts and try. (i) two squares on top and a row of four below, joined only at the second "
                  "square; (ii) a row of three on top and a row of three below, joined at one square; (iii) a "
                  "staircase of 2, 2 and 2 squares; (iv) a row of four with one square above and one below the third "
                  "square; (v) a row of four with two squares hanging in a column below the second square; (vi) a row "
                  "of four with one square above the third square and one below the second square.",
                  ["(i): the row of four makes the walls, one square becomes the lid, and the sixth square folds onto "
                   "a wall: not a net.",
                   "(ii): the 3 and 3 staircase folds with no overlap: a net.",
                   "(iii): the 2, 2, 2 staircase folds with no overlap: a net.",
                   "(iv) and (vi): a row of four with one square above and one below: nets.",
                   "(v): both extra squares are below the row, so one lands on a wall: not a net."],
                  "(ii), (iii), (iv) and (vi) are nets of a cube; (i) and (v) are not"),
              FIO("FiO3.q2", "Figure it Out (nets, question 2)",
                  "A cube has 11 possible net structures in total. In this count, two nets are considered the same if "
                  "one can be obtained from the other by a rotation or a flip. Find all the 11 nets of a cube.",
                  ["Row of four with one square above and one below: 6 nets (the extra squares above positions 1 to "
                   "4 and below positions 1 to 4, removing turns and flips).",
                   "Row of three in the middle: 3 nets with 1 square on one side and 2 on the other, and 1 net of two "
                   "rows of three.",
                   "The staircase of 2, 2 and 2: 1 net.",
                   "Count: 6 + 4 + 1 = 11."],
                  "6 nets with a row of four, 4 with a longest row of three, and 1 staircase: 11 in all"),
              FIO("FiO3.q3", "Figure it Out (nets, question 3)",
                  "Draw a net of a cuboid having sidelengths: (i) 5 cm, 3 cm, and 1 cm (ii) 6 cm, 3 cm, and 2 cm",
                  ["(i): two rectangles 5 by 3, two 5 by 1, two 3 by 1; walls in a row 5, 3, 5, 3 long and 1 cm tall, "
                   "with 5 by 3 rectangles above and below a 5 cm wall.",
                   "Area of net (i) = 2 × (15 + 5 + 3) = 46 square cm.",
                   "(ii): two rectangles 6 by 3, two 6 by 2, two 3 by 2; walls 6, 3, 6, 3 long and 2 cm tall, with "
                   "6 by 3 rectangles above and below a 6 cm wall.",
                   "Area of net (ii) = 2 × (18 + 12 + 6) = 72 square cm."],
                  "Nets of six rectangles in three equal pairs, with areas 46 square cm and 72 square cm")])],
    key_terms=["net", "cube", "cuboid"]))

# ============================== T8 Nets of other solids =====================================================
TOPICS.append(TOPIC(
    "T8", "M2", "Nets of Other Solids", ["4.2"], "Analyze",
    "Students identify nets of a regular tetrahedron, draw nets of a square pyramid and a triangular prism, find the "
    "sides of the rectangle in a cylinder's net, describe the sector in a cone's net, and explore nets of the "
    "octahedron, the dodecahedron and the sphere.",
    "A regular tetrahedron has 2 nets. A cylinder unrolls into two circles and a rectangle whose sides are the "
    "circumference and the height; a cone unrolls into a circle and a part of a circle of radius equal to its slant "
    "length. An octahedron has 11 nets, a dodecahedron 43,380, and a sphere has none.",
    [A("T8.C1", "Nets of a tetrahedron, a pyramid and a prism", "Analyze",
       "Students decide which arrangements of four equilateral triangles fold into a regular tetrahedron and plan "
       "nets of a square pyramid and a triangular prism with measurements.",
       textbook=["Let us find out the nets of other solids.",
                 "A tetrahedron whose faces are equilateral triangles is called a regular tetrahedron.",
                 "What is a net of a regular tetrahedron? Which of the following are nets of a regular tetrahedron?",
                 "Are there any other possible nets? A regular tetrahedron has only 2 possible nets.",
                 "Draw a net with appropriate measurements that can be folded into a regular tetrahedron. Verify if it "
                 "works by making an actual cutout.",
                 "Draw a net with appropriate measurements that can be folded into a square pyramid. Verify if it "
                 "works by making an actual cutout.",
                 "Draw a net with appropriate measurements that can be folded into a triangular prism. Verify that it "
                 "works by making an actual cutout."],
       teach=["Predict first: four triangles all meet at one point in a shape. Can it fold into a tetrahedron?",
              "Only three faces meet at each corner of a tetrahedron, so four triangles around one point overlap.",
              "The two nets are a large triangle cut into four, and a strip of four triangles.",
              "A square pyramid net: a square with a triangle on each side. A triangular prism net: three rectangles "
              "in a row with a triangle on two opposite long edges."],
       examples=[
           WE("Four shapes are made of equilateral triangles: a large triangle of 4, four triangles that all meet at "
              "one point, a straight strip of 4, and a strip of 4 with a fifth triangle below. Which are nets of a "
              "regular tetrahedron?",
              ["A regular tetrahedron has 4 faces with 3 meeting at each corner.",
               "The large triangle of 4 folds its three corners up to meet: a net.",
               "Four triangles around one point would put 4 faces at one corner: not a net.",
               "The straight strip of 4 folds into a tetrahedron: a net.",
               "The last shape has 5 triangles, one too many: not a net."],
              "Only the large triangle and the straight strip of 4",
              ncert=["4.2.tetra_nets", "4.2.mt_tetra_pyramid", "4.2.prism_net"])],
       key_terms=["regular tetrahedron", "net", "square pyramid", "triangular prism"], misconceptions=["M_ANY_SIX"],
       minutes=10),
     A("T8.C2", "Unrolling a cylinder", "Apply",
       "Students explain that the net of a cylinder is two circles and a rectangle whose sides are the circumference "
       "of the base and the height, and find these sides.",
       textbook=["What is the net of a cylinder?",
                 "If the circular faces of a cylinder are unfolded, and if a cut is made along the height of the "
                 "cylinder, then we get two circles and a rectangle.",
                 "What are the sidelengths of the rectangle obtained?"],
       teach=["Predict first: the label of a tin is peeled off. Is the long side of the label as long as the tin is "
              "wide, or longer?",
              "The label went all the way round, so its long side is the circumference, about 3 times the width.",
              "The short side is the height of the tin.",
              "Long side = 2 × π × radius; short side = height."],
       examples=[
           WE("A cylinder has radius 7 cm and height 10 cm. Find the sides of the rectangle in its net, using π as "
              "22/7.",
              ["The long side wraps once round the base: the circumference 2 × π × 7.",
               "2 × 22/7 × 7 = 44 cm.",
               "The short side is the height, 10 cm."],
              "A 44 cm by 10 cm rectangle with two circles of radius 7 cm", ncert=["4.2.cyl_net"])],
       key_terms=["cylinder", "circumference", "net"], misconceptions=["M_CYL_RECT"], minutes=8),
     A("T8.C3", "Unrolling a cone", "Analyze",
       "Students explain that the curved surface of a cone unrolls into a part of a circle centred at the apex with "
       "radius equal to the slant length, and find what fraction of a full circle it is.",
       textbook=["How will the net of a cone look?",
                 "If the cone is slit open along the line l and then unrolled, what will we get?",
                 "Observe that all the points on the boundary of the base circle are at equal distances from 'O'. So "
                 "after unrolling the cone, the boundary of the net will be a portion of a circle with centre O.",
                 "What surface do you construct by using the above net, in which O is not the centre of the boundary "
                 "circle? Make a physical model to help you answer this question!"],
       teach=["Predict first: a birthday cap is slit along a line from the tip and laid flat. Is the flat shape a "
              "triangle?",
              "Every point of the rim is the slant length l from the tip, so the rim becomes an arc of a circle of "
              "radius l with centre at the tip: a sector.",
              "The arc is as long as the circumference of the base.",
              "If the tip is not the centre of the boundary, the cone leans to one side: a slanted (oblique) cone."],
       examples=[
           WE("A cone has base radius 5 cm and slant length 10 cm. What fraction of a full circle of radius 10 cm is "
              "its unrolled curved surface?",
              ["The arc of the sector equals the base circumference: 2 × π × 5 = 10π cm.",
               "A full circle of radius 10 cm has circumference 2 × π × 10 = 20π cm.",
               "Fraction = 10π ÷ 20π = 1/2."],
              "Half of the circle: a semicircle of radius 10 cm",
              ncert=["4.2.cone_net", "4.2.mt_oblique_cone"])],
       key_terms=["cone", "slant length", "sector"], minutes=8),
     DOER("T8.C4", "Practice: nets beyond the cube", "net_roller", "Create",
          "Students make cutouts of nets of a tetrahedron, a square pyramid, a triangular prism and an octahedron, and "
          "test whether a paper net can wrap a ball without wrinkles.",
          ["Tetrahedron: 2 nets. Octahedron: 11 nets. Dodecahedron: 43,380 nets.",
           "A cylinder net has a rectangle as long as the circumference; a cone net has a sector of radius l.",
           "A sphere has no net: paper cannot wrap a ball without wrinkles, gaps or overlaps."],
          textbook=["Here is a solid called the octahedron, made by joining two square pyramids at their square bases.",
                    "Can you visualise its net? This is one of its nets. Taking all the triangles in the net to be "
                    "equilateral, make a cutout of the net and fold it to form an octahedron.",
                    "As in the case of cubes, an octahedron too has 11 different nets.",
                    "So far, we have seen solids whose faces are all equilateral triangles (regular tetrahedrons), and "
                    "all squares (cubes). Does there exist a solid whose faces are all pentagons? Interestingly, the "
                    "answer is yes! This solid is called a dodecahedron. This solid too can be made from a net! "
                    "Mathematicians have been even able to determine exactly how many nets a dodecahedron has: 43,380.",
                    "Net of a sphere? Experiment and see if you can make a paper cutout that can perfectly wrap around "
                    "a ball without leaving any wrinkles, gaps or overlaps."],
          ncert=["4.2.dodeca", "4.2.sphere_net"],
          examples=[
              WE("An octahedron is two square pyramids joined at their square bases. Plan a net for it with equilateral "
                 "triangles, and count its faces, edges and vertices.",
                 ["Each pyramid gives 4 triangles around its apex, so the octahedron has 4 + 4 = 8 faces.",
                  "Unfold the top 4 triangles as a fan around the top corner, and the bottom 4 as a fan around the "
                  "bottom corner.",
                  "Join the two fans along one edge of the square, one fan on each side of it: 8 triangles with no "
                  "overlap.",
                  "Edges: 4 round the square, 4 up to the top and 4 down to the bottom, so 4 + 4 + 4 = 12.",
                  "Vertices: 4 on the square, the top and the bottom, so 4 + 1 + 1 = 6."],
                 "Two fans of 4 equilateral triangles joined along one edge; 8 faces, 12 edges and 6 vertices",
                 ncert=["4.2.octa_net"])])],
    key_terms=["net", "tetrahedron", "cylinder", "cone", "octahedron"]))

# ============================== T9 Shortest paths ===========================================================
TOPICS.append(TOPIC(
    "T9", "M2", "Shortest Paths on a Cuboid", ["4.2"], "Evaluate",
    "Students find the shortest path between two points on the surface of a cube or cuboid by drawing a straight line "
    "on a net, reject lines that leave the net, and compare unfoldings to choose the shortest path.",
    "A path on a box becomes a path of the same length on a net, so the shortest path is a straight line on a "
    "suitable net. The way the box is unfolded matters, so every unfolding must be compared.",
    [A("T9.C1", "Flatten the box, draw a straight line", "Analyze",
       "Students unfold the faces an ant must cross onto one plane and use a straight line on the net to find and "
       "justify the shortest path.",
       textbook=["Shortest Paths on a Cube",
                 "We know that on a plane, the shortest path between two points is the straight line between them. "
                 "Now, what is the shortest path between two points on the surface of a cuboid, if we are allowed to "
                 "travel only along its surface?",
                 "Let us imagine a hungry ant living on the surface of a cuboid. To its good fortune, there is a laddu "
                 "on the surface. Laddu at the centre of the top face, ant at the centre of the side face.",
                 "What is the shortest path for the ant to reach the laddu?",
                 "If we think that a certain path is the shortest, how can we be sure that it truly is, among all the "
                 "infinite possibilities? For example, are either of these the shortest path? [Hint: Draw the net and "
                 "see how these paths appear on the net.]",
                 "A path on the surface of the cuboid can be transformed to a path of the same length on the net. "
                 "Conversely, every path on the net transforms to a path of the same length on the cuboid.",
                 "In the first case, the path marked on the cuboid is the shortest since it transforms to a straight "
                 "line between the ant and laddu on the net, which is the shortest path between them.",
                 "Thus, by using a net, we convert the problem of finding the shortest path on a cuboid to the problem "
                 "of finding the shortest path on the net."],
       teach=["Predict first: the ant is at the centre of a side face and the laddu at the centre of the top face. "
              "Should the ant walk straight up and across, or cut diagonally?",
              "Unfold the top face so it lies flat beside the side face. Now both are on one flat piece.",
              "The straight line between them on the net is the shortest; fold it back and it goes straight up and "
              "straight across the middle.",
              "Any other path becomes a bent line on the net, which is longer."],
       examples=[
           WE("A cube has side 4 cm. An ant is at the centre of a side face and a laddu at the centre of the top face. "
              "Find the length of the shortest path.",
              ["Unfold the top face so it sits flat above the side face.",
               "The ant is 2 cm below the shared edge and the laddu is 2 cm beyond it, on the same straight line.",
               "Shortest path = 2 + 2 = 4 cm."],
              "4 cm, straight up the middle of the side face and across to the centre of the top",
              ncert=["4.2.path_cube", "4.2.path_sure"])],
       key_terms=["shortest path", "net", "straight line"], misconceptions=["M_STRAIGHT_BOX"], minutes=10),
     A("T9.C1x", "A laddu at the centre of an edge", "Analyze",
       "Students find the shortest path from the centre of a face to the middle of an edge that does not touch that "
       "face by drawing a slanted straight line on the net.",
       textbook=["What about in the following case? Laddu at the centre of the edge.",
                 "In the second case, the path marked on the cuboid does not transform to a straight line path on the "
                 "net, and hence is not the shortest path for the ant to take."],
       teach=["Predict first: the ant can go up to the top edge and then sideways, or cut across diagonally. Which "
              "is shorter?",
              "Unfold the right face beside the front face. The ant and the laddu are now on one flat piece.",
              "The straight line between them is the shortest, and it crosses the shared edge on the way."],
       examples=[
           WE("A cube has side 6 cm. An ant is at the centre of the front face, and a laddu at the middle of the edge "
              "between the top face and the right face. Find the shortest path.",
              ["Unfold the right face so it lies flat beside the front face.",
               "From the ant, the laddu is now 3 + 3 = 6 cm across and 3 cm up.",
               "Shortest path = √(6² + 3²) = √45, about 6.71 cm.",
               "Going up 3 cm and then across 6 cm would be 9 cm, which is longer."],
              "About 6.71 cm, a slanted straight line on the net", ncert=["4.2.path_edge"])],
       key_terms=["shortest path", "net"], misconceptions=["M_STRAIGHT_BOX"], minutes=6, thin=True),
     A("T9.C2", "The way you unfold matters", "Evaluate",
       "Students find that one unfolding can put the straight line outside the net, choose an unfolding that gives a "
       "real path, and compute its length.",
       textbook=["Have we now completely analysed the problem of finding the shortest path between two points on a "
                 "cuboid?",
                 "Find the shortest path between the ant and the laddu in the following case: a cuboid 8 cm by 4 cm by "
                 "4 cm, the ant at the centre of the end face, the laddu on the bottom edge, 2 cm from the end.",
                 "If we unfold the cuboid as before, we get a line segment between the ant and laddu going outside the "
                 "net! Obviously, this does not correspond to any path on the cuboid. So what do we do now?",
                 "If the net is unfolded in the following way, then we get a path on the cuboid.",
                 "Thus, the way a cuboid is unfolded matters!"],
       teach=["Predict first: if the straight line on a net leaves the net, is it still a path on the box?",
              "No. Part of the line runs over empty paper, so the ant cannot walk it.",
              "Unfold the end face so it lies against the face that holds the laddu's edge. Now the straight line "
              "stays on the net.",
              "Then measure it with a right triangle."],
       examples=[
           WE("A cuboid is 8 cm by 4 cm by 4 cm. An ant is at the centre of a 4 cm by 4 cm end face. A laddu sits on "
              "a long bottom edge, 2 cm from that end. Find the shortest path.",
              ["Unfold the end face flat against the long face that meets the laddu's edge.",
               "On this net the ant is 2 cm into the end face and 2 cm from the bottom edge line.",
               "The laddu is 2 cm on the other side of the fold, on the bottom edge line.",
               "So the line goes 2 + 2 = 4 cm along and 2 cm across.",
               "Shortest path = √(4² + 2²) = √20, about 4.47 cm."],
              "About 4.47 cm", ncert=["4.2.path_cuboid"])],
       key_terms=["unfolding", "shortest path"], misconceptions=["M_STRAIGHT_BOX"], minutes=10),
     A("T9.C3", "A trickier box: 40 cm beats 42 cm", "Evaluate",
       "Students compare two unfoldings of a 30 cm by 12 cm by 12 cm box, compute each path with the Baudhayana "
       "theorem where needed, and choose the shorter.",
       textbook=["Now we will look at a trickier case. What is the length of the shortest path between the ant and the "
                 "laddu? The box is 30 cm by 12 cm by 12 cm; the laddu is stuck to the back of the box, 1 cm from the "
                 "bottom, and the ant is 1 cm from the top of the opposite end, both on the middle line.",
                 "Here are some of the ways of unfolding the cuboid.",
                 "In the second case, the distance d between the ant and the laddu can be calculated using the "
                 "Baudhayana Theorem, since we have a right triangle here. d² = 24² + 32², d = √1600 = 40 cm.",
                 "We see that in each of these unfoldings, the lengths of the line segments between the ant and the "
                 "laddu are different! So we have to carefully list all the possible different unfoldings to find "
                 "the answer!"],
       teach=["Predict first: the ant walks down its end, along the floor and up the far end. Can a slanted route "
              "over more faces be shorter?",
              "The direct route: 11 cm down, 30 cm along, 1 cm up: 11 + 30 + 1 = 42 cm.",
              "A slanted unfolding crosses five faces, but on the net it is the long side of a right triangle with "
              "sides 24 cm and 32 cm.",
              "24² + 32² = 1600 and √1600 = 40, so the slanted path is shorter."],
       examples=[
           WE("For the 30 cm by 12 cm by 12 cm box, compare the 42 cm route with the slanted unfolding whose right "
              "triangle has sides 24 cm and 32 cm.",
              ["Straight route: 11 + 30 + 1 = 42 cm.",
               "Slanted route: d² = 24² + 32² = 576 + 1024 = 1600.",
               "d = √1600 = 40 cm.",
               "40 cm is less than 42 cm."],
              "The slanted route of 40 cm is shorter than 42 cm", ncert=["4.2.path_try"])],
       key_terms=["unfolding", "Baudhayana theorem", "shortest path"], misconceptions=["M_STRAIGHT_BOX"], minutes=10),
     DOER("T9.C4", "Practice: unfold and measure", "net_path_unfolder", "Evaluate",
          "Students place an ant and a laddu on a box, unfold it in different ways, reject lines that leave the net, "
          "and measure each straight line to choose the shortest.",
          ["The shortest path is a straight line on a net that stays inside the net.",
           "Compare every unfolding: the shortest one wins."])],
    key_terms=["shortest path", "net", "unfolding"]))
