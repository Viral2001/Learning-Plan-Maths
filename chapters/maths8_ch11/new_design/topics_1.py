# -*- coding: utf-8 -*-
"""Topics T1 to T4 (module M1: fractals). Book section 4.1, pp 70 to 75."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Shapes within shapes =====================================================
TOPICS.append(TOPIC(
    "T1", "M1", "Shapes Within Shapes", ["Chapter opening", "4.1"], "Understand",
    "",
    "A fern is made of smaller ferns: the idea of self-similarity that drives the first half of the chapter.",
    [A("T1.C1", "A fern made of smaller ferns", "Understand",
       "",
       textbook=["In this chapter, we will explore two geometric themes. We will study fractals which are self-similar "
                 "shapes. They exhibit the same or similar pattern over and over again, but at smaller and smaller "
                 "scales. We will then look at different ways of visualising solids.",
                 "4.1 Fractals",
                 "One of the most beautiful examples of a fractal that also occurs in nature is the fern. The fern is "
                 "seen to have smaller copies of itself as its leaves, and these in turn have even smaller copies of "
                 "themselves in their sub-leaves, and so on!",
                 "Similar phenomena of self-similarity occur in trees (where a trunk has limbs, and a limb has "
                 "branches, and the branches have branchlets, and so on), clouds, coastlines, mountains, lightning, "
                 "and many other objects in nature.",
                 "Other mathematical fractals can also be very beautiful. We will explore some of them here."],
       teach=["Predict first: look at one leaf of a fern. Does it look like a small copy of the whole fern?",
              "Each leaf is a smaller fern, and each sub-leaf is a smaller copy again. This is self-similarity.",
              "Trees, clouds, coastlines and lightning repeat the same pattern at smaller scales. Can a rule in "
              "mathematics make a shape like this, one step at a time?"],
       ncert=["opening", "4.1.nature"], key_terms=["fractal", "self-similar"], video_focus=["HOOK"], minutes=4,
       enrichment=True)],
    topic_type="framing"))

# ============================== T2 The Sierpinski Carpet ====================================================
TOPICS.append(TOPIC(
    "T2", "M1", "The Sierpinski Carpet", ["4.1"], "Analyze",
    "Students build the Sierpinski Carpet step by step, find that the remaining squares multiply by 8 at each step "
    "so that Rn is 8 to the power n, and find the holes by adding the squares of the step before to the old holes.",
    "Split each square into 9 and remove the centre. Remaining squares go 1, 8, 64, 512, multiplying by 8, and holes "
    "go 0, 1, 9, 73, each step adding the squares of the step before.",
    [A("T2.C1", "Building the carpet step by step", "Apply",
       "Students draw Step 0, Step 1 and Step 2 of the Sierpinski Carpet and count the remaining squares and the holes "
       "at each step.",
       textbook=["The Polish mathematician Sierpinski discovered a type of fractal known as the Sierpinski Carpet. It "
                 "is made by taking a square, breaking it into 9 smaller squares, and then removing the central square; "
                 "the same procedure is then repeated on the remaining 8 squares, and so on. One then sees the same "
                 "pattern at smaller and smaller scales.",
                 "Draw the initial few steps (at least till Step 2) of the shape sequence that leads to the Sierpinski "
                 "Carpet.",
                 "By its construction, each step in the sequence has (i) squares of the same size that remain in the "
                 "figure, and the size of these squares becomes smaller and smaller as the step number increases, and "
                 "(ii) square holes that are formed by removing square pieces.",
                 "Do you see any pattern in the number of holes and squares that remain at each step?"],
       teach=["Predict first: Step 1 leaves 8 squares. How many small squares remain after Step 2?",
              "At Step 1 the square is split into a 3 by 3 grid and the centre is removed: 8 squares remain, 1 hole.",
              "At Step 2 each of the 8 squares is split into 9 and loses its centre: 8 × 8 = 64 squares remain.",
              "The 8 new centres are new holes, and the first hole is still there, so there are 1 + 8 = 9 holes."],
       examples=[
           WE("Draw Steps 0, 1 and 2 of the Sierpinski Carpet and count the remaining squares and the holes at each "
              "step.",
              ["Step 0: one whole square, no hole.",
               "Step 1: a 3 by 3 grid with the centre removed leaves 8 squares and 1 hole.",
               "Step 2: each of the 8 squares loses its own centre, so 8 × 8 = 64 squares remain.",
               "Holes at Step 2: the old hole plus 8 new ones, 1 + 8 = 9."],
              "Remaining squares 1, 8, 64; holes 0, 1, 9",
              ncert=["4.1.carpet_steps", "4.1.carpet_pattern"])],
       key_terms=["Sierpinski Carpet", "step", "hole"], misconceptions=["M_FRACTAL_ADD"], minutes=10),
     A("T2.C2", "Remaining squares multiply by 8", "Analyze",
       "Students use the rule that each remaining square gives rise to 8 remaining squares at the next step to write "
       "Rn as 8 to the power n and find the count at Step 3 and Step 4.",
       textbook=["Let Rn represent the number of remaining squares at the nth step, and Hn represent the number of "
                 "holes at the nth step.",
                 "Every square that remains at a given step, say Step n, gives rise to 8 squares that remain at the "
                 "(n + 1)th step. Thus, we have R(n + 1) = 8 Rn.",
                 "Can this be used to get a formula for Rn?",
                 "We have R0 = 1, R1 = 8 × 1 = 8, R2 = 8 × 8 = 8². In general, Rn is 8 to the power n."],
       teach=["Predict first: does the number of squares grow by adding 8 each time, or by multiplying by 8?",
              "Each remaining square becomes 8 remaining squares, so the count is multiplied by 8 at every step.",
              "Starting from 1: 1, 8, 64, 512. The count at Step n is 8 multiplied by itself n times."],
       examples=[
           WE("Find the number of remaining squares at Step 3 and at Step 4 of the Sierpinski Carpet.",
              ["Step 2 has 8 × 8 = 64 remaining squares.",
               "Step 3: each of these gives 8, so 64 × 8 = 512.",
               "Step 4: 512 × 8 = 4096."],
              "512 squares at Step 3 and 4096 at Step 4", ncert=["4.1.carpet_Rn"])],
       key_terms=["remaining squares", "multiply", "power"], misconceptions=["M_FRACTAL_ADD"], minutes=8),
     A("T2.C3", "Holes: old holes plus one for every square", "Analyze",
       "Students use the rule that every remaining square makes one new hole while old holes stay to find the number "
       "of holes at any step.",
       textbook=["Similarly, how do we find the number of holes at a given step?",
                 "Every square that remains at the nth step gives rise to a hole in the (n + 1)th step. All the holes "
                 "present at the nth step remain in the (n + 1)th step as well. Thus, H(n + 1) = Hn + Rn.",
                 "So we have R0 = 1, H0 = 0; R1 = 8, H1 = 1; R2 = 8², H2 = 1 + 8; R3 = 8³, H3 = 1 + 8 + 8²."],
       teach=["Predict first: Step 2 has 9 holes. Is the number of holes at Step 3 equal to 64, or more?",
              "The 64 squares of Step 2 each lose a centre at Step 3, making 64 new holes.",
              "The 9 older holes remain, so Step 3 has 9 + 64 = 73 holes."],
       examples=[
           WE("Find the number of holes at Step 3 and at Step 4 of the Sierpinski Carpet.",
              ["Holes at Step 3: 1 + 8 + 64 = 73.",
               "Step 3 has 512 remaining squares, and each makes a new hole at Step 4.",
               "Holes at Step 4: 73 + 512 = 585."],
              "73 holes at Step 3 and 585 at Step 4", ncert=["4.1.carpet_holes"])],
       key_terms=["holes", "remaining squares"], misconceptions=["M_HOLES_EQUAL"], minutes=8),
     DOER("T2.C4", "Practice: grow the carpet", "fractal_stepper", "Apply",
          "Students step the Sierpinski Carpet forward, predict the remaining squares, holes and area left before each "
          "step, and check their predictions against the picture.",
          ["Remaining squares multiply by 8 at each step: 1, 8, 64, 512.",
           "Holes add the squares of the step before: 0, 1, 9, 73.",
           "Each step keeps 8 of every 9 parts of the area that was there."])],
    key_terms=["Sierpinski Carpet", "self-similar", "remaining squares", "holes"]))

# ============================== T3 The Sierpinski Triangle ==================================================
TOPICS.append(TOPIC(
    "T3", "M1", "The Sierpinski Triangle", ["4.1"], "Analyze",
    "Students show that joining the midpoints of an equilateral triangle gives 4 identical equilateral triangles, "
    "build the Sierpinski Triangle, and count its remaining triangles, holes and area at any step.",
    "Joining midpoints splits an equilateral triangle into 4 identical ones; removing the centre each time leaves 3 "
    "times as many triangles at every step, while the area left is multiplied by three quarters.",
    [A("T3.C1", "Midpoints make four identical triangles", "Analyze",
       "Students use the isosceles corner triangles to show that joining the midpoints of an equilateral triangle "
       "divides it into 4 identical equilateral triangles.",
       textbook=["Sierpinski came up with another fractal made in a similar way. An equilateral triangle is broken up "
                 "into 4 identical equilateral triangles by joining the midpoints of the bigger triangle, and then "
                 "the central triangle is removed. This procedure is repeated on the 3 remaining triangles, and so on.",
                 "Show that by joining the midpoints of an equilateral triangle, we divide it into 4 identical "
                 "equilateral triangles. [Hint: Note that the corner triangles are isosceles.]",
                 "This fractal is called the Sierpinski Triangle/Gasket."],
       teach=["Predict first: the triangle has side 8 cm. What is the side of each small triangle after joining the "
              "midpoints?",
              "Each corner triangle has two sides of 4 cm (half of each side) with a 60° angle between them.",
              "Two equal sides make the base angles equal; with 60° at the top, each base angle is (180° − 60°) ÷ 2 "
              "= 60°. So the corner triangle is equilateral with side 4 cm.",
              "The middle triangle's three sides are the bases of the three corner triangles, all 4 cm, so it is "
              "equilateral too. All four are identical."],
       examples=[
           WE("An equilateral triangle has side 8 cm. Show that joining the midpoints of its sides makes 4 identical "
              "equilateral triangles.",
              ["Each corner triangle has two sides of 8 ÷ 2 = 4 cm with the 60° angle of the big triangle between "
               "them.",
               "It is isosceles, so its base angles are equal: (180° − 60°) ÷ 2 = 60° each.",
               "All its angles are 60°, so it is equilateral and its third side is also 4 cm.",
               "The middle triangle has the three third sides as its sides: 4 cm, 4 cm and 4 cm."],
              "Four equilateral triangles, each of side 4 cm",
              ncert=["4.1.gasket_construct", "4.1.gasket_identical"])],
       key_terms=["midpoint", "equilateral triangle", "isosceles", "Sierpinski Triangle"], minutes=10),
     A("T3.C2", "Counting what remains: triangles, holes and area", "Analyze",
       "Students count the remaining triangles, the holes and the remaining area of the Sierpinski Triangle at a given "
       "step by applying the rule step by step.",
       teach=["Predict first: each step keeps 3 of the 4 small triangles. After Step 3, how many triangles remain?",
              "Remaining triangles multiply by 3: 1, 3, 9, 27.",
              "Each remaining triangle makes one new hole at the next step, so holes go 0, 1, 4, 13.",
              "Each step keeps 3 of every 4 equal parts, so the area is multiplied by three quarters each time."],
       examples=[
           WE("For the Sierpinski Triangle with starting area 1 square unit, find the remaining triangles, the holes "
              "and the remaining area at Step 3.",
              ["Remaining triangles: 3 × 3 × 3 = 27.",
               "Holes: 1 + 3 + 9 = 13.",
               "Area: each step keeps 3 of 4 parts, so 3/4 × 3/4 × 3/4 = 27/64 square unit."],
              "27 triangles, 13 holes and 27/64 square unit of area")],
       key_terms=["remaining triangles", "holes", "area"], misconceptions=["M_AREA_GROWS", "M_HOLES_EQUAL"],
       minutes=8),
     DOER("T3.C3", "Practice: count the Sierpinski fractals", "triangle_stepper", "Apply",
          "Students draw the Sierpinski Triangle to Step 2, find its remaining triangles and holes at every step, and "
          "find the remaining area at Step n for both Sierpinski fractals.",
          ["Remaining triangles multiply by 3; holes add the triangles of the step before.",
           "Area left at each step: three quarters for the triangle, eight ninths for the carpet."],
          items=[
              FIO("FiO1.q1", "Figure it Out (sierpinski fractals, question 1)",
                  "Draw the initial few steps (at least till Step 2) of the shape sequence that leads to the "
                  "Sierpinski Triangle.",
                  ["Step 0: draw an equilateral triangle.",
                   "Step 1: join the midpoints of its sides and shade out the middle triangle; 3 triangles remain.",
                   "Step 2: repeat on each of the 3 corner triangles; 3 × 3 = 9 triangles remain."],
                  "Step 0 is one triangle, Step 1 shows 3 triangles around 1 hole, Step 2 shows 9 triangles and 4 "
                  "holes"),
              FIO("FiO1.q2", "Figure it Out (sierpinski fractals, question 2)",
                  "Find the number of holes, and the triangles that remain at each step of the shape sequence that "
                  "leads to the Sierpinski Triangle.",
                  ["Each remaining triangle gives 3 remaining triangles at the next step: 1, 3, 9, 27, so the count "
                   "at Step n is 3 to the power n.",
                   "Each remaining triangle also makes one new hole, and the old holes stay.",
                   "Holes: 0, 1, 1 + 3 = 4, 1 + 3 + 9 = 13, and so on.",
                   "At Step n the holes are 1 + 3 + 9 + ... up to 3 to the power (n − 1), which equals (3 to the "
                   "power n, minus 1) divided by 2."],
                  "Remaining triangles: 3 to the power n. Holes: 1 + 3 + 9 + ... up to n terms, which is (3 to the "
                  "power n, minus 1) divided by 2"),
              FIO("FiO1.q3", "Figure it Out (sierpinski fractals, question 3)",
                  "Find the area of the region remaining at the nth step in each of the shape sequences that lead to "
                  "the Sierpinski fractals. Take the area of the starting square/triangle to be 1 sq. unit.",
                  ["Carpet: each step keeps 8 of the 9 equal parts of every square, so the area is multiplied by 8/9.",
                   "After Step 2 the carpet has 8/9 × 8/9 = 64/81 square unit left.",
                   "Triangle: each step keeps 3 of the 4 equal parts, so the area is multiplied by 3/4.",
                   "After Step 2 the triangle has 3/4 × 3/4 = 9/16 square unit left."],
                  "Carpet: (8/9) to the power n square unit. Triangle: (3/4) to the power n square unit. Both shrink "
                  "towards 0")])],
    key_terms=["Sierpinski Triangle", "equilateral triangle", "holes", "area"]))

# ============================== T4 Koch Snowflake and fractals in art =======================================
TOPICS.append(TOPIC(
    "T4", "M1", "The Koch Snowflake and Fractals in Art", ["4.1"], "Analyze",
    "Students build the Koch Snowflake by replacing every side with a bump, find that the number of sides is "
    "multiplied by 4 and the perimeter by four thirds at each step, and recognise fractal patterns in temples, "
    "blankets and prints.",
    "Every side of the Koch Snowflake becomes 4 sides, each a third as long, so sides go 3, 12, 48 and the perimeter "
    "grows by four thirds each step. Fractal patterns appear in Indian temples, Fulani blankets and Escher's prints.",
    [A("T4.C1", "The bump rule of the Koch Snowflake", "Apply",
       "Students apply the bump rule to an equilateral triangle and count the sides and the perimeter at Step 1.",
       textbook=["The Koch Snowflake is another fractal, named after the Swedish mathematician Von Koch, who first "
                 "described it in 1904. We have already encountered this fractal in Grade 6, Ganita Prakash.",
                 "To generate it, we start with an equilateral triangle. Each side is (i) divided into 3 equal parts, "
                 "and (ii) an equilateral triangle is raised over the middle part, and then the middle part is "
                 "removed.",
                 "Effectively, each side gets replaced by a 'bump' shaped structure.",
                 "This procedure is repeated on the sides of the new resulting shape, and so on."],
       teach=["Predict first: a triangle has 3 sides. After every side gets a bump, how many sides are there?",
              "One side becomes 4 shorter sides: the two outer thirds and the two sides of the bump.",
              "So 3 sides become 3 × 4 = 12 sides, each one third of the old length.",
              "The perimeter changes from 3 to 12 × 1/3 = 4 when each starting side is 1 unit."],
       examples=[
           WE("Start with an equilateral triangle of side 1 unit. Find the number of sides, the length of each side "
              "and the perimeter at Step 1 of the Koch Snowflake.",
              ["Each side is cut into 3 parts of 1/3 unit, and the middle part is replaced by two sides of a bump.",
               "So each side becomes 4 sides: 3 × 4 = 12 sides.",
               "Each side is 1/3 unit long.",
               "Perimeter = 12 × 1/3 = 4 units."],
              "12 sides, each 1/3 unit, perimeter 4 units", ncert=["4.1.koch"])],
       key_terms=["Koch Snowflake", "bump", "perimeter"], misconceptions=["M_KOCH_SIDES"], minutes=10),
     A("T4.C2", "Fractals in temples, blankets and prints", "Understand",
       "Students describe self-similar patterns in the Kandariya Mahadev Temple, Fulani wedding blankets and "
       "Escher's 'Smaller and Smaller', and compute how a nested diamond pattern shrinks.",
       textbook=["Fractals have also long been used in human-made art! Perhaps the oldest such fractals appear in the "
                 "temples of India. An example occurs in the Kandariya Mahadev Temple in Khajuraho, Madhya Pradesh "
                 "which was completed in around 1025 C.E.; there one sees a tall temple structure, which is made up of "
                 "smaller copies of the full structure, on which there are even smaller copies of the same structure, "
                 "and so on. Fractal-like patterns also occur in temples in Madurai, Hampi, Rameswaram, Varanasi, "
                 "among many others.",
                 "Fractals are also common in traditional African cultures. For example, patterns on Nigerian Fulani "
                 "wedding blankets often exhibit fractal structures.",
                 "In the blanket shown in the figure, there are diamond shaped patterns, inside of which there are "
                 "smaller diamond shaped patterns, and so on.",
                 "The modern maestro of fractal art is undoubtedly the Dutch artist M.C. Escher. One famous example "
                 "involving fractals is his work 'Smaller and Smaller', which exhibits the identical pattern of lizards "
                 "but at smaller and smaller scales."],
       teach=["Predict first: a diamond is drawn inside a bigger one by joining the midpoints of its sides. Does the "
              "inner diamond take more or less than half the area?",
              "Joining the midpoints of a rhombus gives a shape with exactly half its area, because each corner cut "
              "off matches a piece left inside.",
              "Repeating it gives a diamond pattern like the Fulani blankets, each shape half the one before.",
              "The temple spire is built of smaller spires in the same way; Escher's lizards shrink ring by ring."],
       examples=[
           WE("A diamond pattern has area 64 square cm. Each new shape is drawn by joining the midpoints of the "
              "sides of the one before. What is the area of the third shape inside?",
              ["Joining the midpoints keeps exactly half the area each time.",
               "First shape inside: 64 ÷ 2 = 32 square cm.",
               "Second: 32 ÷ 2 = 16 square cm.",
               "Third: 16 ÷ 2 = 8 square cm."],
              "8 square cm", ncert=["4.1.art"])],
       key_terms=["fractal art", "self-similar"], minutes=6),
     DOER("T4.C3", "Practice: grow the snowflake", "koch_bump_builder", "Apply",
          "Students draw the Koch Snowflake to Step 2 and find the number of sides and the perimeter at Step n.",
          ["Every side becomes 4 sides, each one third as long.",
           "Sides are multiplied by 4 and the perimeter by four thirds at every step."],
          items=[
              FIO("FiO2.q1", "Figure it Out (koch snowflake, question 1)",
                  "Draw the initial few steps (at least till Step 2) of the shape sequence that leads to the Koch "
                  "Snowflake.",
                  ["Step 0: draw an equilateral triangle with sides of 9 units on dot paper so thirds are easy.",
                   "Step 1: on each side raise a bump on the middle third; a six pointed star with 12 sides appears.",
                   "Step 2: put a smaller bump on the middle third of each of the 12 sides."],
                  "Step 0 has 3 sides, Step 1 is a star with 12 sides, Step 2 has 48 sides"),
              FIO("FiO2.q2", "Figure it Out (koch snowflake, question 2)",
                  "Find the number of sides in the nth step of the shape sequence that leads to the Koch Snowflake.",
                  ["Step 0 has 3 sides.",
                   "Each step turns every side into 4 sides, so the count is multiplied by 4.",
                   "Step 1: 3 × 4 = 12. Step 2: 12 × 4 = 48. Step 3: 48 × 4 = 192."],
                  "3 × (4 to the power n) sides at Step n"),
              FIO("FiO2.q3", "Figure it Out (koch snowflake, question 3)",
                  "Find the perimeter of the shape at the nth step of the sequence. Take the starting equilateral "
                  "triangle to have a sidelength of 1 unit.",
                  ["At Step n there are 3 × (4 to the power n) sides.",
                   "Each step makes every side one third as long, so each side is 1/3 to the power n.",
                   "Step 1: 12 × 1/3 = 4. Step 2: 48 × 1/9 = 16/3.",
                   "Each step multiplies the perimeter by 4/3."],
                  "3 × (4/3) to the power n units; the perimeter keeps growing")])],
    key_terms=["Koch Snowflake", "perimeter", "fractal art"]))
