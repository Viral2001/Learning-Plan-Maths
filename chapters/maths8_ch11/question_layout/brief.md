# Exploring Some Geometric Themes  (cbse_eng_maths8_ch11, live v29)

Book text: `textbooks/extracted/hegp204.txt`

Topics in order. `C` lines are concepts; `b<i>` lines are content blocks (kind, item_kind, refs, steps, question). A concept topic is followed by its existing Questions topic (if any).

## M1.S1.T1  Shapes Within Shapes  [FRAMING]
C M1.S1.T1.C1  'A fern made of smaller ferns'  [enrichment]  media=['IMG1', 'VID1']  refs=['opening', '4.1.nature']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: In this chapter, we will explore two geometric themes. We will study fractals which are self-similar shapes. They exhibit the same or similar pattern over and over again,
   b1 teaching_plan/None refs=[] steps=3 video=-  Q: 1. Predict first: look at one leaf of a fern. Does it look like a small copy of the whole fern? 2. Each leaf is a smaller fern, and each sub-leaf is a smaller copy again.

## M1.S2.T2  The Sierpinski Carpet  [CONCEPT TOPIC]
C M1.S2.T2.C2  'Building the carpet step by step'  [obj O1]  media=['IMG1', 'VID1']  refs=['4.1.carpet_steps', '4.1.carpet_pattern']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: The Polish mathematician Sierpinski discovered a type of fractal known as the Sierpinski Carpet. It is made by taking a square, breaking it into 9 smaller squares, and th
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: Step 1 leaves 8 squares. How many small squares remain after Step 2? 2. At Step 1 the square is split into a 3 by 3 grid and the centre is removed: 8 sq
   b2 worked_example/None refs=['4.1.carpet_steps', '4.1.carpet_pattern'] steps=4 video=VID1  Q: Draw Steps 0, 1 and 2 of the Sierpinski Carpet and count the remaining squares and the holes at each step.
C M1.S2.T2.C3  'Remaining squares multiply by 8'  [obj O2]  media=['IMG1', 'VID1']  refs=['4.1.carpet_Rn']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Let Rn represent the number of remaining squares at the nth step, and Hn represent the number of holes at the nth step. Every square that remains at a given step, say Ste
   b1 teaching_plan/None refs=[] steps=3 video=-  Q: 1. Predict first: does the number of squares grow by adding 8 each time, or by multiplying by 8? 2. Each remaining square becomes 8 remaining squares, so the count is mul
   b2 worked_example/None refs=['4.1.carpet_Rn'] steps=3 video=VID1  Q: Find the number of remaining squares at Step 3 and at Step 4 of the Sierpinski Carpet.
C M1.S2.T2.C4  'Holes: old holes plus one for every square'  [obj O3]  media=['IMG1', 'VID1']  refs=['4.1.carpet_holes']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Similarly, how do we find the number of holes at a given step? Every square that remains at the nth step gives rise to a hole in the (n + 1)th step. All the holes present
   b1 teaching_plan/None refs=[] steps=3 video=-  Q: 1. Predict first: Step 2 has 9 holes. Is the number of holes at Step 3 equal to 64, or more? 2. The 64 squares of Step 2 each lose a centre at Step 3, making 64 new holes
   b2 worked_example/None refs=['4.1.carpet_holes'] steps=3 video=VID1  Q: Find the number of holes at Step 3 and at Step 4 of the Sierpinski Carpet.
C M1.S2.T2.C5  'Practice: grow the carpet'  [obj O4]  media=['IMG1', '2D1']  refs=[]
   b0 recap/None refs=[] steps=0 video=-  Q: Remaining squares multiply by 8 at each step: 1, 8, 64, 512. Holes add the squares of the step before: 0, 1, 9, 73. Each step keeps 8 of every 9 parts of the area that wa

## M1.S3.T3  The Sierpinski Triangle  [CONCEPT TOPIC]
C M1.S3.T3.C6  'Midpoints make four identical triangles'  [obj O5]  media=['IMG1', 'VID1']  refs=['4.1.gasket_construct', '4.1.gasket_identical']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Sierpinski came up with another fractal made in a similar way. An equilateral triangle is broken up into 4 identical equilateral triangles by joining the midpoints of the
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: the triangle has side 8 cm. What is the side of each small triangle after joining the midpoints? 2. Each corner triangle has two sides of 4 cm (half of 
   b2 worked_example/None refs=['4.1.gasket_construct', '4.1.gasket_identical'] steps=4 video=VID1  Q: An equilateral triangle has side 8 cm. Show that joining the midpoints of its sides makes 4 identical equilateral triangles.
C M1.S3.T3.C7  'Counting what remains: triangles, holes and area'  [obj O6]  media=['IMG1', 'VID1']  refs=[]
   b0 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: each step keeps 3 of the 4 small triangles. After Step 3, how many triangles remain? 2. Remaining triangles multiply by 3: 1, 3, 9, 27. 3. Each remainin
   b1 worked_example/None refs=[] steps=3 video=-  Q: For the Sierpinski Triangle with starting area 1 square unit, find the remaining triangles, the holes and the remaining area at Step 3.
C M1.S3.T3.C8  'Practice: count the Sierpinski fractals'  [obj O7]  media=['IMG1', 'VID1', '2D1']  refs=['FiO1.q1']
   b0 recap/None refs=[] steps=0 video=-  Q: Remaining triangles multiply by 3; holes add the triangles of the step before. Area left at each step: three quarters for the triangle, eight ninths for the carpet.
   b1 exercise/None refs=[] steps=3 video=VID1  Q: Draw the initial few steps (at least till Step 2) of the shape sequence that leads to the Sierpinski Triangle.
   b2 exercise/None refs=[] steps=4 video=VID1  Q: Find the number of holes, and the triangles that remain at each step of the shape sequence that leads to the Sierpinski Triangle.
   b3 exercise/None refs=[] steps=4 video=VID1  Q: Find the area of the region remaining at the nth step in each of the shape sequences that lead to the Sierpinski fractals. Take the area of the starting square/triangle t

## M1.S4.T4  Questions: The Sierpinski Triangle  [QUESTIONS TOPIC (follows M1.S3.T3)]
C M1.S4.T4.C9  'Sierpinski Fractals, Q2'  [obj O8]  media=['VID1']  refs=['FiO1.q2']
   b0 worked_example/figure_it_out refs=[] steps=0 video=VID1  Q: Work through the practice problem. Read the question in the book and attempt it before watching the video solution.
C M1.S4.T4.C10  'Sierpinski Fractals, Q3'  [obj O9]  media=['VID1']  refs=['FiO1.q3']
   b0 worked_example/figure_it_out refs=[] steps=0 video=VID1  Q: Work through the practice problem. Read the question in the book and attempt it before watching the video solution.

## M1.S5.T5  The Koch Snowflake and Fractals in Art  [CONCEPT TOPIC]
C M1.S5.T5.C11  'The bump rule of the Koch Snowflake'  [obj O10]  media=['IMG1', 'VID1']  refs=['4.1.koch']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: The Koch Snowflake is another fractal, named after the Swedish mathematician Von Koch, who first described it in 1904. We have already encountered this fractal in Grade 6
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: a triangle has 3 sides. After every side gets a bump, how many sides are there? 2. One side becomes 4 shorter sides: the two outer thirds and the two si
   b2 worked_example/None refs=['4.1.koch'] steps=4 video=VID1  Q: Start with an equilateral triangle of side 1 unit. Find the number of sides, the length of each side and the perimeter at Step 1 of the Koch Snowflake.
C M1.S5.T5.C12  'Fractals in temples, blankets and prints'  [obj O11]  media=['IMG1', 'VID1']  refs=['4.1.art']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Fractals have also long been used in human-made art! Perhaps the oldest such fractals appear in the temples of India. An example occurs in the Kandariya Mahadev Temple in
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: a diamond is drawn inside a bigger one by joining the midpoints of its sides. Does the inner diamond take more or less than half the area? 2. Joining th
   b2 worked_example/None refs=['4.1.art'] steps=4 video=VID1  Q: A diamond pattern has area 64 square cm. Each new shape is drawn by joining the midpoints of the sides of the one before. What is the area of the third shape inside?
C M1.S5.T5.C13  'Practice: grow the snowflake'  [obj O12]  media=['IMG1', 'VID1', '2D1']  refs=['FiO2.q1']
   b0 recap/None refs=[] steps=0 video=-  Q: Every side becomes 4 sides, each one third as long. Sides are multiplied by 4 and the perimeter by four thirds at every step.
   b1 exercise/None refs=[] steps=3 video=VID1  Q: Draw the initial few steps (at least till Step 2) of the shape sequence that leads to the Koch Snowflake.
   b2 exercise/None refs=[] steps=3 video=VID1  Q: Find the number of sides in the nth step of the shape sequence that leads to the Koch Snowflake.
   b3 exercise/None refs=[] steps=4 video=VID1  Q: Find the perimeter of the shape at the nth step of the sequence. Take the starting equilateral triangle to have a sidelength of 1 unit.

## M1.S6.T6  Questions: The Koch Snowflake and Fractals in Art  [QUESTIONS TOPIC (follows M1.S5.T5)]
C M1.S6.T6.C14  'Koch Snowflake, Q2'  [obj O13]  media=['VID1']  refs=['FiO2.q2']
   b0 worked_example/figure_it_out refs=[] steps=0 video=VID1  Q: Work through the practice problem. Read the question in the book and attempt it before watching the video solution.
C M1.S6.T6.C15  'Koch Snowflake, Q3'  [obj O14]  media=['VID1']  refs=['FiO2.q3']
   b0 worked_example/figure_it_out refs=[] steps=0 video=VID1  Q: Work through the practice problem. Read the question in the book and attempt it before watching the video solution.

## M2.S7.T7  Build It in Your Imagination  [CONCEPT TOPIC]
C M2.S7.T7.C16  'Cutting corners in the mind'  [obj O15]  media=['IMG1', 'VID1']  refs=['4.2.imagine_intro', '4.2.imagine_square']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: 4.2 Visualising Solids Build it in Your Imagination We will start this section by practising visualisation. For each prompt, feel free to talk to your partner, gesture, d
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: close your eyes and cut the four corners of a square from midpoint to midpoint. What shape is left, and is it bigger or smaller than the four corners pu
   b2 worked_example/None refs=['4.2.imagine_intro', '4.2.imagine_square'] steps=4 video=VID1  Q: A square has side 4 cm. Its corners are cut off from midpoint to midpoint. Find the area of the square that is left and of the square made from the four corners.
C M2.S7.T7.C17  'Cutting at the thirds: hexagon or octagon?'  [thin-extra, obj O16]  media=['IMG1', 'VID1']  refs=['4.2.imagine_triangle', '4.2.imagine_octagon']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: 3. Mark the sides of an equilateral triangle into thirds. Cut off each corner of the triangle, as far as the marks. What shape do you get? 4. Mark the sides of a square i
   b1 teaching_plan/None refs=[] steps=3 video=-  Q: 1. Predict first: a triangle loses 3 corners and a square loses 4. How many sides does each shape left have, and are all its sides equal? 2. Each corner of the triangle c
   b2 worked_example/None refs=['4.2.imagine_triangle', '4.2.imagine_octagon'] steps=5 video=VID1  Q: Cut the corners at the thirds of an equilateral triangle of side 9 cm and of a square of side 9 cm. Find the side lengths of the shapes left.
C M2.S7.T7.C18  'Profiles: one solid, many outlines'  [obj O17]  media=['IMG1', 'VID1']  refs=['4.2.profile_intro', '4.2.profile_square', '4.2.profile_circle', '4.2.profile_triangle']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: When we see a solid object, we are really seeing its profile from a specific viewpoint. Depending on our viewpoint, the outline of this profile can vary dramatically! Per
   b1 teaching_plan/None refs=[] steps=3 video=-  Q: 1. Predict first: a tin can passes through a paper wall. What shape is the hole if it goes in lid first, and what if it goes in lying on its side? 2. Lid first: a circle.
   b2 worked_example/None refs=['4.2.profile_intro', '4.2.profile_square', '4.2.profile_circle', '4.2.profile_triangle'] steps=3 video=VID1  Q: A tin can is a cylinder with radius 3 cm and height 10 cm. What profile does it show from directly above, and what from the side?
C M2.S7.T7.C19  'Two profiles at once'  [thin-extra, obj O18]  media=['IMG1', 'VID1']  refs=['4.2.profile_pairs', '4.2.profile_unique']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: As we saw with the elephant, a given solid might have very different profiles from different viewpoints. Can you visualise solids that have the following contrasting prof
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: which everyday object looks like a trapezium from the side and a circle from above? 2. A bucket: its sides slope out, so from the side its outline is a 
   b2 worked_example/None refs=['4.2.profile_pairs', '4.2.profile_unique'] steps=3 video=VID1  Q: Give two different solids that each show a rectangular profile from one viewpoint and a triangular profile from another.
C M2.S7.T7.C20  'Practice: picture it before you draw it'  [obj O19]  media=['IMG1', 'VID1']  refs=[]
   b0 worked_example/None refs=[] steps=4 video=-  Q: A cylinder has radius 7 cm and height 14 cm. Picture it before you draw it: what profile does it show from the side, and what from directly above?
   b1 recap/None refs=[] steps=0 video=-  Q: Picture first, then check with a sketch or an object at home. A cylinder, a cone, a prism and a bucket give the contrasting profiles; most pairs have more than one answer

## M2.S8.T8  Faces, Edges and Vertices of Prisms and Pyramids  [CONCEPT TOPIC]
C M2.S8.T8.C21  'Faces, edges and vertices'  [obj O20]  media=['IMG1', 'VID1']  refs=['4.2.solids_make', '4.2.fev_cube']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Making Solids Many basic solid shapes such as a cuboid, parallelopiped, cylinder, cone, prism, and pyramid can be made using foldable flat materials like paper, cardboard
   b1 teaching_plan/None refs=[] steps=3 video=-  Q: 1. Predict first: hold a matchbox. How many flat faces, straight edges and corners does it have? 2. 6 faces, 12 edges, 8 vertices: 4 edges around the top, 4 around the bo
   b2 worked_example/None refs=['4.2.solids_make', '4.2.fev_cube'] steps=3 video=VID1  Q: Count the faces, edges and vertices of a triangular prism.
C M2.S8.T8.C22  'Counting the parts of a prism'  [obj O21]  media=['IMG1', 'VID1']  refs=['4.2.prism_def', '4.2.prism_count']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: There are multiple types of prisms and pyramids, whose names depend on the shapes of their faces. Prism: A prism, in general, has two congruent polygons as opposite faces
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: a prism on a 10 sided polygon. How many side faces does it need? 2. One parallelogram face for each side of the polygon: 10, plus the 2 polygons. 3. Edg
   b2 worked_example/None refs=['4.2.prism_def', '4.2.prism_count'] steps=3 video=VID1  Q: A prism has two congruent 10 sided polygons as opposite faces. Find its faces, edges and vertices.
C M2.S8.T8.C23  'Counting the parts of a pyramid'  [obj O22]  media=['IMG1', 'VID1']  refs=['4.2.pyramid_def', '4.2.pyramid_count']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Pyramids: A pyramid, in general, has a polygonal base and a point outside it, and edges connect the point with each of the vertices of the base. Based on the shape of the
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: a pyramid and a prism both on a 10 sided polygon. Which has more edges? 2. The pyramid has one triangle on each side of the base: 10 triangles plus the 
   b2 worked_example/None refs=['4.2.pyramid_def', '4.2.pyramid_count'] steps=3 video=VID1  Q: A pyramid has a 10 sided base. Find its faces, edges and vertices.
C M2.S8.T8.C24  'Practice: count faces, edges and vertices'  [obj O23]  media=['IMG1', 'VID1', '2D1']  refs=[]
   b0 worked_example/None refs=[] steps=4 video=-  Q: A gift box is a prism on an octagon, and its lid is a pyramid on the same octagon. Find the faces, edges and vertices of each.
   b1 recap/None refs=[] steps=0 video=-  Q: Prism on n sides: n + 2 faces, 3n edges, 2n vertices. Pyramid on n sides: n + 1 faces, 2n edges, n + 1 vertices.

## M2.S9.T9  Nets of a Cube and a Cuboid  [CONCEPT TOPIC]
C M2.S9.T9.C25  'What is a net? Folding the cross'  [obj O24]  media=['IMG1', 'VID1']  refs=['4.2.net_def', '4.2.net_fold', '4.2.net_practical']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Now we will see how to make different solids using a foldable flat surface such as paper, cardboard, etc. The basic idea is to create a shape on a flat surface that can b
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: in the cross shaped net, which square ends up opposite the bottom square? 2. Fold the four squares around the bottom up to make the walls; the last squa
   b2 worked_example/None refs=['4.2.net_def', '4.2.net_fold', '4.2.net_practical'] steps=4 video=VID1  Q: A cross shaped net has a column of four squares A, B, C, D from top to bottom, and two squares L and R on either side of B. Fold it into a cube with B as the bottom. Whic
C M2.S9.T9.C26  'Will these six squares fold into a cube?'  [obj O25]  media=['IMG1', 'VID1']  refs=[]
   b0 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: a row of four squares with both extra squares above the same end square. Will it fold into a cube? 2. The row of four wraps round to make four walls. On
   b1 worked_example/None refs=[] steps=4 video=-  Q: Six squares: a row of four, one square above the first square of the row, and one more square to the left of that square. Is it a net of a cube?
C M2.S9.T9.C27  'Drawing a net of a cuboid'  [obj O26]  media=['IMG1', 'VID1']  refs=[]
   b0 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: a cuboid has 6 faces. How many different sizes of rectangle does its net need? 2. Opposite faces are equal, so there are 3 pairs: length by breadth, len
   b1 worked_example/None refs=[] steps=4 video=-  Q: Draw a net of a cuboid 4 cm by 2 cm by 1 cm and find the area of the net.
C M2.S9.T9.C28  'Practice: fold the net'  [obj O27]  media=['IMG1', 'VID1', '2D1']  refs=['FiO3.q1']
   b0 recap/None refs=[] steps=0 video=-  Q: Visualise first, then fold to check. With a row of four, one square above and one below; there are 11 nets of a cube in all. A cuboid net has three pairs of equal rectang
   b1 exercise/None refs=[] steps=5 video=VID1  Q: Which of the following are the nets of a cube? First, try to answer by visualisation. Then, you may use cutouts and try. (i) two squares on top and a row of four below, j
   b2 exercise/None refs=[] steps=4 video=VID1  Q: A cube has 11 possible net structures in total. In this count, two nets are considered the same if one can be obtained from the other by a rotation or a flip. Find all th
   b3 exercise/None refs=[] steps=4 video=VID1  Q: Draw a net of a cuboid having sidelengths: (i) 5 cm, 3 cm, and 1 cm (ii) 6 cm, 3 cm, and 2 cm

## M2.S10.T10  Questions: Nets of a Cube and a Cuboid  [QUESTIONS TOPIC (follows M2.S9.T9)]
C M2.S10.T10.C29  'Nets, Q2'  [obj O28]  media=['VID1']  refs=['FiO3.q2']
   b0 worked_example/figure_it_out refs=[] steps=0 video=VID1  Q: Work through the practice problem. Read the question in the book and attempt it before watching the video solution.
C M2.S10.T10.C30  'Nets, Q3'  [obj O29]  media=['VID1']  refs=['FiO3.q3']
   b0 worked_example/figure_it_out refs=[] steps=0 video=VID1  Q: Work through the practice problem. Read the question in the book and attempt it before watching the video solution.

## M2.S11.T11  Nets of Other Solids  [CONCEPT TOPIC]
C M2.S11.T11.C31  'Nets of a tetrahedron, a pyramid and a prism'  [obj O30]  media=['IMG1', 'VID1']  refs=['4.2.tetra_nets', '4.2.mt_tetra_pyramid', '4.2.prism_net']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Let us find out the nets of other solids. A tetrahedron whose faces are equilateral triangles is called a regular tetrahedron. What is a net of a regular tetrahedron? Whi
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: four triangles all meet at one point in a shape. Can it fold into a tetrahedron? 2. Only three faces meet at each corner of a tetrahedron, so four trian
   b2 worked_example/None refs=['4.2.tetra_nets', '4.2.mt_tetra_pyramid', '4.2.prism_net'] steps=5 video=VID1  Q: Four shapes are made of equilateral triangles: a large triangle of 4, four triangles that all meet at one point, a straight strip of 4, and a strip of 4 with a fifth tria
C M2.S11.T11.C32  'Unrolling a cylinder'  [obj O31]  media=['IMG1', 'VID1']  refs=['4.2.cyl_net']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: What is the net of a cylinder? If the circular faces of a cylinder are unfolded, and if a cut is made along the height of the cylinder, then we get two circles and a rect
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: the label of a tin is peeled off. Is the long side of the label as long as the tin is wide, or longer? 2. The label went all the way round, so its long 
   b2 worked_example/None refs=['4.2.cyl_net'] steps=3 video=VID1  Q: A cylinder has radius 7 cm and height 10 cm. Find the sides of the rectangle in its net, using π as 22/7.
C M2.S11.T11.C33  'Unrolling a cone'  [obj O32]  media=['IMG1', 'VID1']  refs=['4.2.cone_net', '4.2.mt_oblique_cone']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: How will the net of a cone look? If the cone is slit open along the line l and then unrolled, what will we get? Observe that all the points on the boundary of the base ci
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: a birthday cap is slit along a line from the tip and laid flat. Is the flat shape a triangle? 2. Every point of the rim is the slant length l from the t
   b2 worked_example/None refs=['4.2.cone_net', '4.2.mt_oblique_cone'] steps=3 video=VID1  Q: A cone has base radius 5 cm and slant length 10 cm. What fraction of a full circle of radius 10 cm is its unrolled curved surface?
C M2.S11.T11.C34  'Practice: nets beyond the cube'  [obj O33]  media=['IMG1', 'VID1', '2D1']  refs=['4.2.dodeca', '4.2.sphere_net', '4.2.octa_net']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Here is a solid called the octahedron, made by joining two square pyramids at their square bases. Can you visualise its net? This is one of its nets. Taking all the trian
   b1 worked_example/None refs=['4.2.octa_net'] steps=5 video=VID1  Q: An octahedron is two square pyramids joined at their square bases. Plan a net for it with equilateral triangles, and count its faces, edges and vertices.
   b2 recap/None refs=[] steps=0 video=-  Q: Tetrahedron: 2 nets. Octahedron: 11 nets. Dodecahedron: 43,380 nets. A cylinder net has a rectangle as long as the circumference; a cone net has a sector of radius l. A s

## M2.S12.T12  Shortest Paths on a Cuboid  [CONCEPT TOPIC]
C M2.S12.T12.C35  'Flatten the box, draw a straight line'  [obj O34]  media=['IMG1', 'VID1']  refs=['4.2.path_cube', '4.2.path_sure']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Shortest Paths on a Cube We know that on a plane, the shortest path between two points is the straight line between them. Now, what is the shortest path between two point
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: the ant is at the centre of a side face and the laddu at the centre of the top face. Should the ant walk straight up and across, or cut diagonally? 2. U
   b2 worked_example/None refs=['4.2.path_cube', '4.2.path_sure'] steps=3 video=VID1  Q: A cube has side 4 cm. An ant is at the centre of a side face and a laddu at the centre of the top face. Find the length of the shortest path.
C M2.S12.T12.C36  'A laddu at the centre of an edge'  [thin-extra, obj O35]  media=['IMG1', 'VID1']  refs=['4.2.path_edge']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: What about in the following case? Laddu at the centre of the edge. In the second case, the path marked on the cuboid does not transform to a straight line path on the net
   b1 teaching_plan/None refs=[] steps=3 video=-  Q: 1. Predict first: the ant can go up to the top edge and then sideways, or cut across diagonally. Which is shorter? 2. Unfold the right face beside the front face. The ant
   b2 worked_example/None refs=['4.2.path_edge'] steps=4 video=VID1  Q: A cube has side 6 cm. An ant is at the centre of the front face, and a laddu at the middle of the edge between the top face and the right face. Find the shortest path.
C M2.S12.T12.C37  'The way you unfold matters'  [obj O36]  media=['IMG1', 'VID1']  refs=['4.2.path_cuboid']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Have we now completely analysed the problem of finding the shortest path between two points on a cuboid? Find the shortest path between the ant and the laddu in the follo
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: if the straight line on a net leaves the net, is it still a path on the box? 2. No. Part of the line runs over empty paper, so the ant cannot walk it. 3
   b2 worked_example/None refs=['4.2.path_cuboid'] steps=5 video=VID1  Q: A cuboid is 8 cm by 4 cm by 4 cm. An ant is at the centre of a 4 cm by 4 cm end face. A laddu sits on a long bottom edge, 2 cm from that end. Find the shortest path.
C M2.S12.T12.C38  'A trickier box: 40 cm beats 42 cm'  [obj O37]  media=['IMG1', 'VID1']  refs=['4.2.path_try']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Now we will look at a trickier case. What is the length of the shortest path between the ant and the laddu? The box is 30 cm by 12 cm by 12 cm; the laddu is stuck to the 
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: the ant walks down its end, along the floor and up the far end. Can a slanted route over more faces be shorter? 2. The direct route: 11 cm down, 30 cm a
   b2 worked_example/None refs=['4.2.path_try'] steps=4 video=VID1  Q: For the 30 cm by 12 cm by 12 cm box, compare the 42 cm route with the slanted unfolding whose right triangle has sides 24 cm and 32 cm.
C M2.S12.T12.C39  'Practice: unfold and measure'  [obj O38]  media=['IMG1', '2D1']  refs=[]
   b0 recap/None refs=[] steps=0 video=-  Q: The shortest path is a straight line on a net that stays inside the net. Compare every unfolding: the shortest one wins.

## M3.S13.T13  Projections of Points, Lines and Shapes  [CONCEPT TOPIC]
C M3.S13.T13.C40  'Projecting a point and a line'  [obj O39]  media=['IMG1', 'VID1']  refs=['4.2.proj_point', '4.2.proj_line', '4.2.proj_compare']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Projections The net of a solid (when it exists) is one way of representing a solid on the plane. But it can be difficult to visualise the solid from the net, without phys
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: a pencil is held slanting above a table. Is its projection on the table longer, shorter or the same length as the pencil? 2. Drop a perpendicular from e
   b2 worked_example/None refs=['4.2.proj_point', '4.2.proj_line', '4.2.proj_compare'] steps=3 video=VID1  Q: A stick 5 cm long is held above a table so that one end is 3 cm higher than the other. How long is its projection on the table?
C M3.S13.T13.C41  'Projections of a square and a parallelogram'  [obj O40]  media=['IMG1', 'VID1']  refs=['4.2.mt_proj_square', '4.2.mt_proj_parallelogram', '4.2.mt_proj_polygon']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: What do you think are the different possible projections of a square that we get based on its orientation? What do you think is the projection of a parallelogram under di
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: a square card is tilted above the floor. Can its projection be a trapezium? 2. Flat: a square. Tilted about one side: a rectangle. Tilted about a diagon
   b2 worked_example/None refs=['4.2.mt_proj_square', '4.2.mt_proj_parallelogram', '4.2.mt_proj_polygon'] steps=3 video=VID1  Q: A square card of side 5 cm is tilted about one of its sides so that the opposite side is 3 cm higher. What is its projection on the floor?
C M3.S13.T13.C42  'Same projection, different objects'  [obj O41]  media=['IMG1', 'VID1']  refs=['4.2.proj_solids', '4.2.proj_same', '4.2.proj_cone_same']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Let us consider projections of solids now. How would the projections of a cube and a cone look? If an object were to pass perpendicularly through a plane and form a hole,
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: a cone standing on its base is projected onto the floor. Can a different solid give the very same shape? 2. The cone's projection on the floor is a circ
   b2 worked_example/None refs=['4.2.proj_solids', '4.2.proj_same', '4.2.proj_cone_same'] steps=3 video=VID1  Q: A cone standing on its base has base radius 4 cm. Name three different solids whose projection on the floor is the same circle.
C M3.S13.T13.C43  'Practice: predict the projection'  [obj O42]  media=['IMG1', 'VID1', '2D1']  refs=[]
   b0 worked_example/None refs=[] steps=3 video=-  Q: A rod 13 cm long is held above a table so that one end is 5 cm higher than the other. Predict the length of its projection, and say when the projection would be 13 cm.
   b1 recap/None refs=[] steps=0 video=-  Q: A projection is never longer than the object's line; it is equal only when the line is parallel to the plane. A parallelogram projects to a parallelogram or a line; one p

## M3.S14.T14  Front, Top and Side Views  [CONCEPT TOPIC]
C M3.S14.T14.C44  'Three planes, three views'  [obj O43]  media=['IMG1', 'VID1']  refs=['4.2.views', '4.2.views_fig46']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: For this reason, we often take three mutually perpendicular projections of an object. As shown in the figure, we consider a plane in front of the object called the vertic
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: a glass of water stands on the table. Which of its three views is a circle? 2. Front view: look from the front onto the wall behind. Top view: look down
   b2 worked_example/None refs=['4.2.views', '4.2.views_fig46'] steps=3 video=VID1  Q: A cylinder of radius 3 cm and height 8 cm stands on its base. Draw its front, top and side views.
C M3.S14.T14.C45  'Views of a stack of cubes'  [obj O44]  media=['IMG1', 'VID1']  refs=[]
   b0 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: four cubes stand as three in a row with one more on top of the left cube. How many squares does the top view show? 2. From the front you see the whole s
   b1 worked_example/None refs=[] steps=3 video=-  Q: Four identical cubes: three in a row on the floor, and one more on top of the left cube. Draw its front, top and side views.
C M3.S14.T14.C46  'Practice: see it from three sides'  [obj O45]  media=['IMG1', 'VID1', '2D1']  refs=['FiO4.q1']
   b0 recap/None refs=[] steps=0 video=-  Q: Front view on the vertical plane, top view on the horizontal plane, side view on the side plane. A cylinder: rectangle, circle, rectangle. A cone: triangle, circle, trian
   b1 exercise/None refs=[] steps=4 video=VID1  Q: Observe the front view, top view and side view of the different lines in Fig. 4.6. Is there any relation between their lengths?
   b2 exercise/None refs=[] steps=7 video=VID1  Q: Find the front view, top view and side view of each of the following solids, fixing its orientation with respect to the vertical, horizontal and side planes: cube, cuboid
   b3 exercise/None refs=[] steps=8 video=VID1  Q: Match each of the following objects with its projections: a jug, a funnel, a hammer, a car, a slide, a chair, a ceiling fan and a pressure cooker, each with a front, a to

## M3.S15.T15  Questions: Front, Top and Side Views  [QUESTIONS TOPIC (follows M3.S14.T14)]
C M3.S15.T15.C47  'Views of Solids, Q2'  [obj O46]  media=['VID1']  refs=['FiO4.q2']
   b0 worked_example/figure_it_out refs=[] steps=0 video=VID1  Q: Work through the practice problem. Read the question in the book and attempt it before watching the video solution.
C M3.S15.T15.C48  'Views of Solids, Q3'  [obj O47]  media=['VID1']  refs=['FiO4.q3']
   b0 worked_example/figure_it_out refs=[] steps=0 video=VID1  Q: Work through the practice problem. Read the question in the book and attempt it before watching the video solution.

## M3.S16.T16  Shadows and Parallel Lines  [CONCEPT TOPIC]
C M3.S16.T16.C49  'Torch shadows and sunlight'  [obj O48]  media=['IMG1', 'VID1']  refs=['4.2.shadow_torch', '4.2.shadow_why', '4.2.shadow_sun']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Shadows Place an object in front of a plane, such as a wall of your room. Shine a torch light on the object in a direction perpendicular to the wall. What do you see? We 
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: you move a torch away from a toy in front of a wall. Does the shadow grow or shrink? 2. Light spreads out from the torch, so the shadow is larger than t
   b2 worked_example/None refs=['4.2.shadow_torch', '4.2.shadow_why', '4.2.shadow_sun'] steps=5 video=VID1  Q: A toy 10 cm tall stands 50 cm in front of a wall. A torch shines straight at the wall from 50 cm in front of the toy. How tall is the shadow? What if the torch is moved t
C M3.S16.T16.C50  'Parallel lines stay parallel'  [obj O49]  media=['IMG1', 'VID1']  refs=['4.2.shadow_parallel']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Earlier we asked what the projection of a parallelogram might look like. You can now physically answer this question by making a cutout of a parallelogram and viewing its
   b1 teaching_plan/None refs=[] steps=3 video=-  Q: 1. Predict first: turn a square card in the sun. Can its shadow ever be a trapezium? 2. Opposite sides of the card are parallel, and parallel lines cast parallel shadows,
   b2 worked_example/None refs=['4.2.shadow_parallel'] steps=4 video=VID1  Q: A square card has diagonals of 10 cm. It is tilted in sunlight about one diagonal, so the other diagonal's shadow is 6 cm. What is the shadow, and how long is each side?
C M3.S16.T16.C51  'Practice: views and shadows of cube stacks'  [obj O50]  media=['IMG1', 'VID1']  refs=['FiO5.q1']
   b0 recap/None refs=[] steps=0 video=-  Q: Draw one square for every column seen along the direction of view. Different stacks can share some views; use all three views together.
   b1 exercise/None refs=[] steps=3 video=VID1  Q: Draw the top view, front view and the side view of each of the following combinations of identical cubes.
   b2 exercise/None refs=[] steps=4 video=VID1  Q: Imagine eight identical cubes, glued together along faces to form the letter C. (i) This looks like a C from the front. What does it look like from the side? From the top
   b3 exercise/None refs=[] steps=4 video=VID1  Q: Which solid corresponds to the given top view, front view, and side view?
   b4 exercise/None refs=[] steps=4 video=VID1  Q: Using identical cubes, make a solid that gives the following projections.
   b5 exercise/None refs=[] steps=3 video=VID1  Q: Find the number of cubes in this stack of identical cubes.
   b6 exercise/None refs=[] steps=3 video=VID1  Q: What are the different shapes the projection of a cube can make under different orientations?

## M3.S17.T17  Questions: Shadows and Parallel Lines  [QUESTIONS TOPIC (follows M3.S16.T16)]
C M3.S17.T17.C52  'Shadows and Views, Q2'  [obj O51]  media=['VID1']  refs=['FiO5.q2']
   b0 worked_example/figure_it_out refs=[] steps=0 video=VID1  Q: Work through the practice problem. Read the question in the book and attempt it before watching the video solution.
C M3.S17.T17.C53  'Shadows and Views, Q3'  [obj O52]  media=['VID1']  refs=['FiO5.q3']
   b0 worked_example/figure_it_out refs=[] steps=0 video=VID1  Q: Work through the practice problem. Read the question in the book and attempt it before watching the video solution.
C M3.S17.T17.C54  'Shadows and Views, Q4'  [obj O53]  media=['VID1']  refs=['FiO5.q4']
   b0 worked_example/figure_it_out refs=[] steps=0 video=VID1  Q: Work through the practice problem. Read the question in the book and attempt it before watching the video solution.
C M3.S17.T17.C55  'Shadows and Views, Q5'  [obj O54]  media=['VID1']  refs=['FiO5.q5']
   b0 worked_example/figure_it_out refs=[] steps=0 video=VID1  Q: Work through the practice problem. Read the question in the book and attempt it before watching the video solution.
C M3.S17.T17.C56  'Shadows and Views, Q6'  [obj O55]  media=['VID1']  refs=['FiO5.q6']
   b0 worked_example/figure_it_out refs=[] steps=0 video=VID1  Q: Work through the practice problem. Read the question in the book and attempt it before watching the video solution.

## M3.S18.T18  Isometric Projection and Drawing  [CONCEPT TOPIC]
C M3.S18.T18.C57  'A cube on its corner: the regular hexagon'  [obj O56]  media=['IMG1', 'VID1']  refs=['4.2.iso_cube', '4.2.mt_iso_equal', '4.2.iso_grid']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Isometric Projections In general we lose information when projecting a solid to a plane. But depending on the orientation of the solid, we can sometimes recover much of t
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: balance a cube on one corner and look straight down. What outline do you see? 2. The cube looks the same after a turn of a third of a full turn about th
   b2 worked_example/None refs=['4.2.iso_cube', '4.2.mt_iso_equal', '4.2.iso_grid'] steps=4 video=VID1  Q: A glass cube balanced on a corner is projected onto the floor. How many of its 12 edges form the hexagon outline, and how many lie inside it?
C M3.S18.T18.C58  'Drawing edge by edge on the grid'  [obj O57]  media=['IMG1', 'VID1']  refs=['4.2.tetris', '4.2.iso_axes_cube', '4.2.iso_row']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Drawing on Isometric Grids Have you played Tetris? There are five basic shapes in Tetris, corresponding to the different ways of arranging four squares. Imagine these are
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: a 2 by 2 by 2 cube is drawn on the grid. How many units long is each visible edge? 2. Vertical lines are height; the two slanting families are length an
   b2 worked_example/None refs=['4.2.tetris', '4.2.iso_axes_cube', '4.2.iso_row'] steps=3 video=VID1  Q: Draw a 2 by 2 by 2 cube on an isometric grid. How many units of line do its visible edges use?
C M3.S18.T18.C59  'Why the grid works'  [obj O58]  media=['IMG1', 'VID1']  refs=['4.2.iso_why', '4.2.iso_others']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: In your drawing, moving in the vertical direction on the isometric paper corresponds to moving along the height axis of the solid. Similarly, moving along the two slantin
   b1 teaching_plan/None refs=[] steps=4 video=-  Q: 1. Predict first: on the grid, is a 3 unit edge along the depth shown longer, shorter or the same as a 3 unit edge along the height? 2. The same: isometric means equal me
   b2 worked_example/None refs=['4.2.iso_why', '4.2.iso_others'] steps=4 video=VID1  Q: Draw a cuboid 1 unit long, 2 units deep and 3 units tall on the grid. How many units of line do its visible edges use?
C M3.S18.T18.C60  'Practice: draw it on isometric paper'  [obj O59]  media=['IMG1', 'VID1', '2D1']  refs=['FiO6.q1']
   b0 recap/None refs=[] steps=0 video=-  Q: Vertical is height; the two slanting directions are length and depth. Count units along one direction at a time and erase hidden lines.
   b1 exercise/None refs=[] steps=4 video=VID1  Q: In addition to the 5 ways shown in Fig. 4.8, are there any additional ways of gluing four cubes together along faces? Can you visualise and draw these as well?
   b2 exercise/None refs=[] steps=3 video=VID1  Q: Draw the following figures on the isometric grid.
   b3 exercise/None refs=[] steps=3 video=VID1  Q: Is there anything strange about the path of this ball? Recreate it on the isometric grid.
   b4 exercise/None refs=[] steps=3 video=VID1  Q: Observe this triangle. (i) Would it be possible to build a model out of actual cubes? What are the front, top, and side profiles of this impossible triangle? (ii) Recreat

## M3.S19.T19  Questions: Isometric Projection and Drawing  [QUESTIONS TOPIC (follows M3.S18.T18)]
C M3.S19.T19.C61  'Isometric Drawing, Q2'  [obj O60]  media=['VID1']  refs=['FiO6.q2']
   b0 worked_example/figure_it_out refs=[] steps=0 video=VID1  Q: Work through the practice problem. Read the question in the book and attempt it before watching the video solution.
C M3.S19.T19.C62  'Isometric Drawing, Q3'  [obj O61]  media=['VID1']  refs=['FiO6.q3']
   b0 worked_example/figure_it_out refs=[] steps=0 video=VID1  Q: Work through the practice problem. Read the question in the book and attempt it before watching the video solution.
C M3.S19.T19.C63  'Isometric Drawing, Q4'  [obj O62]  media=['VID1']  refs=['FiO6.q4']
   b0 worked_example/figure_it_out refs=[] steps=0 video=VID1  Q: Work through the practice problem. Read the question in the book and attempt it before watching the video solution.

## M3.S20.T20  Summary: Exploring Some Geometric Themes  [SUMMARY]
C M3.S20.T20.C64  'What we found about shapes and solids'  [obj O63]  media=['IMG1']  refs=['summary']
   b0 textbook_text/None refs=[] steps=0 video=-  Q: Fractals are self-similar geometric objects found in nature and in art. The Sierpinski Carpet, Sierpinski Gasket, and Koch Snowflake are some examples of mathematical fra
   b1 teaching_plan/None refs=[] steps=3 video=-  Q: 1. Our opening fern is explained: a fractal repeats one rule, so every part looks like the whole. 2. Nets turn solids into flat shapes, and a straight line on the right n

## Book items the plan covers (coverage id -> concept)

- 4.1.art -> M1.S5.T5.C12
- FiO1.q1 -> M1.S3.T3.C8
- FiO1.q2 -> M1.S4.T4.C9
- FiO1.q3 -> M1.S4.T4.C10
- FiO2.q1 -> M1.S5.T5.C13
- FiO2.q2 -> M1.S6.T6.C14
- FiO2.q3 -> M1.S6.T6.C15
- FiO3.q1 -> M2.S9.T9.C28
- FiO3.q2 -> M2.S10.T10.C29
- FiO3.q3 -> M2.S10.T10.C30
- FiO4.q1 -> M3.S14.T14.C46
- FiO4.q2 -> M3.S15.T15.C47
- FiO4.q3 -> M3.S15.T15.C48
- FiO5.q1 -> M3.S16.T16.C51
- FiO5.q2 -> M3.S17.T17.C52
- FiO5.q3 -> M3.S17.T17.C53
- FiO5.q4 -> M3.S17.T17.C54
- FiO5.q5 -> M3.S17.T17.C55
- FiO5.q6 -> M3.S17.T17.C56
- FiO6.q1 -> M3.S18.T18.C60
- FiO6.q2 -> M3.S19.T19.C61
- FiO6.q3 -> M3.S19.T19.C62
- FiO6.q4 -> M3.S19.T19.C63
- opening -> M1.S1.T1.C1
- summary -> M3.S20.T20.C64
- 4.1.koch -> M1.S5.T5.C11
- 4.2.views -> M3.S14.T14.C44
- 4.1.nature -> M1.S1.T1.C1
- 4.2.dodeca -> M2.S11.T11.C34
- 4.2.tetris -> M3.S18.T18.C58
- 4.2.cyl_net -> M2.S11.T11.C32
- 4.2.iso_row -> M3.S18.T18.C58
- 4.2.iso_why -> M3.S18.T18.C59
- 4.2.net_def -> M2.S9.T9.C25
- 4.2.cone_net -> M2.S11.T11.C33
- 4.2.fev_cube -> M2.S8.T8.C21
- 4.2.iso_cube -> M3.S18.T18.C57
- 4.2.iso_grid -> M3.S18.T18.C57
- 4.2.net_fold -> M2.S9.T9.C25
- 4.2.octa_net -> M2.S11.T11.C34
- 4.2.path_try -> M2.S12.T12.C38
- 4.1.carpet_Rn -> M1.S2.T2.C3
- 4.2.path_cube -> M2.S12.T12.C35
- 4.2.path_edge -> M2.S12.T12.C36
- 4.2.path_sure -> M2.S12.T12.C35
- 4.2.prism_def -> M2.S8.T8.C22
- 4.2.prism_net -> M2.S11.T11.C31
- 4.2.proj_line -> M3.S13.T13.C40
- 4.2.proj_same -> M3.S13.T13.C42
- 4.2.iso_others -> M3.S18.T18.C59
- 4.2.proj_point -> M3.S13.T13.C40
- 4.2.shadow_sun -> M3.S16.T16.C49
- 4.2.shadow_why -> M3.S16.T16.C49
- 4.2.sphere_net -> M2.S11.T11.C34
- 4.2.tetra_nets -> M2.S11.T11.C31
- 4.2.path_cuboid -> M2.S12.T12.C37
- 4.2.prism_count -> M2.S8.T8.C22
- 4.2.proj_solids -> M3.S13.T13.C42
- 4.2.pyramid_def -> M2.S8.T8.C23
- 4.2.solids_make -> M2.S8.T8.C21
- 4.2.views_fig46 -> M3.S14.T14.C44
- 4.1.carpet_holes -> M1.S2.T2.C4
- 4.1.carpet_steps -> M1.S2.T2.C2
- 4.2.mt_iso_equal -> M3.S18.T18.C57
- 4.2.proj_compare -> M3.S13.T13.C40
- 4.2.shadow_torch -> M3.S16.T16.C49
- 4.2.imagine_intro -> M2.S7.T7.C16
- 4.2.iso_axes_cube -> M3.S18.T18.C58
- 4.2.net_practical -> M2.S9.T9.C25
- 4.2.profile_intro -> M2.S7.T7.C18
- 4.2.profile_pairs -> M2.S7.T7.C19
- 4.2.pyramid_count -> M2.S8.T8.C23
- 4.1.carpet_pattern -> M1.S2.T2.C2
- 4.2.imagine_square -> M2.S7.T7.C16
- 4.2.mt_proj_square -> M3.S13.T13.C41
- 4.2.profile_circle -> M2.S7.T7.C18
- 4.2.profile_square -> M2.S7.T7.C18
- 4.2.profile_unique -> M2.S7.T7.C19
- 4.2.proj_cone_same -> M3.S13.T13.C42
- 4.2.imagine_octagon -> M2.S7.T7.C17
- 4.2.mt_oblique_cone -> M2.S11.T11.C33
- 4.2.mt_proj_polygon -> M3.S13.T13.C41
- 4.2.shadow_parallel -> M3.S16.T16.C50
- 4.1.gasket_construct -> M1.S3.T3.C6
- 4.1.gasket_identical -> M1.S3.T3.C6
- 4.2.imagine_triangle -> M2.S7.T7.C17
- 4.2.mt_tetra_pyramid -> M2.S11.T11.C31
- 4.2.profile_triangle -> M2.S7.T7.C18
- 4.2.mt_proj_parallelogram -> M3.S13.T13.C41
