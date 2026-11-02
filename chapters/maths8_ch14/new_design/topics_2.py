# -*- coding: utf-8 -*-
"""Topics T5 to T8 (module M2: polygons and special quadrilaterals). Book pp 159 to 170."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []
U3 = "Figure it Out (area of any polygon, question %s)"
U4 = "Figure it Out (parallelograms, question %s)"
U5 = "Figure it Out (rhombus and trapezium, question %s)"

# ============================== T5 Area of any polygon ========================================================
TOPICS.append(TOPIC(
    "T5", "M2", "Area of Any Polygon", ["Area of any Polygon"], "Apply",
    "Students split quadrilaterals and pentagons into triangles along diagonals, find each triangle's area from a "
    "base and height, add them, and subtract corner triangles when a polygon sits inside a rectangle.",
    "Any polygon is a set of triangles: draw diagonals, find each triangle's area and add, or subtract the unwanted "
    "corners from an enclosing rectangle.",
    [A("T5.C1", "Split a polygon into triangles", "Apply",
       "Students cut a quadrilateral along a diagonal into two triangles, measure the height to the diagonal in each "
       "triangle, and add the two areas to get the polygon's area.",
       textbook=["Area of any Polygon",
                 "How do we find the area of this quadrilateral? What measurements do we need for this?",
                 "If we join BD, the quadrilateral ABCD gets divided into two triangles. By finding their areas, we can "
                 "find the area of ABCD.",
                 "Can any polygon be divided into triangles?",
                 "It can be seen that any polygon can be divided into triangles. Thus, by knowing how to compute the "
                 "area of a triangle, we can find the area of any polygon.",
                 "One can derive special formulae to find the areas of a parallelogram, rhombus and trapezium."],
       teach=["Predict first: a quadrilateral has no single base and height. Which measurements would let us find its "
              "area?",
              "Draw one diagonal. It cuts the quadrilateral into two triangles that share the diagonal as base.",
              "Drop a height from each of the other two corners to the diagonal, find both triangle areas and add."],
       examples=[
           WE("A quadrilateral ABCD has diagonal BD = 10 cm. The heights from A and C to BD are 4 cm and 3 cm. Find "
              "its area.",
              ["Area of ΔABD = 1/2 × 10 × 4 = 20 cm².", "Area of ΔBCD = 1/2 × 10 × 3 = 15 cm².",
               "Area of ABCD = 20 + 15 = 35 cm²."],
              "35 cm²",
              ncert=["poly.quad", "poly.any", "poly.special"])],
       key_terms=["polygon", "diagonal", "triangle"], minutes=8),
     A("T5.C1x", "A pentagon cut into pieces", "Apply",
       "Students divide a pentagon into a rectangle and a triangle, or into triangles by diagonals from one corner, "
       "and add the pentagon's parts.",
       textbook=["How do we find the area of this pentagon?"],
       teach=["Predict first: how many pieces must a pentagon be cut into, and which pieces are easiest?",
              "Two diagonals from one corner cut any pentagon into three triangles.",
              "A house shaped pentagon is even quicker: a rectangle with a triangle on top. Find each part and add."],
       examples=[
           WE("A pentagon is a 6 cm by 4 cm rectangle with a triangle of height 3 cm on its 6 cm side. Find its area.",
              ["Rectangle: 6 × 4 = 24 cm².", "Triangle: 1/2 × 6 × 3 = 9 cm².", "Pentagon: 24 + 9 = 33 cm²."],
              "33 cm²",
              ncert=["poly.pentagon"])],
       key_terms=["pentagon", "polygon"], minutes=6, thin=True),
     DOER("T5.C2", "Practice: polygon areas by splitting and subtracting", "polygon_splitter", "Analyze",
          "Students find polygon areas by splitting them into triangles, subtract corners from an enclosing rectangle, "
          "and reason about shaded fractions using equal bases and heights.",
          ["Cut the polygon into triangles and add their areas.",
           "Or enclose it in a rectangle and subtract the corner triangles.",
           "Joining the midpoints of a quadrilateral's sides cuts off exactly half its area."],
          items=[
              FIO("FiO3.q1", U3 % 1,
                  "Find the area of the quadrilateral ABCD given that AC = 22 cm, BM = 3 cm, DN = 3 cm, BM is "
                  "perpendicular to AC, and DN is perpendicular to AC.",
                  ["The diagonal AC splits ABCD into ΔABC and ΔACD.",
                   "Area of ΔABC = 1/2 × 22 × 3 = 33 cm². Area of ΔACD = 1/2 × 22 × 3 = 33 cm².",
                   "Area of ABCD = 33 + 33 = 66 cm²."],
                  "66 cm²"),
              FIO("FiO3.q2", U3 % 2,
                  "Find the area of the shaded region FECD given that ABCD is a rectangle, with AB = 18 cm, "
                  "BC = 10 cm, AE = 10 cm, EB = 8 cm, AF = 6 cm and FD = 4 cm.",
                  ["Rectangle ABCD: 18 × 10 = 180 cm².",
                   "Unshaded ΔAEF: 1/2 × 10 × 6 = 30 cm². Unshaded ΔEBC: 1/2 × 8 × 10 = 40 cm².",
                   "Shaded region = 180 − 30 − 40 = 110 cm²."],
                  "110 cm²"),
              FIO("FiO3.q3", U3 % 3,
                  "What measurements would you need to find the area of a regular hexagon?",
                  ["Join the centre to all six corners: six identical equilateral triangles.",
                   "Each triangle has a side of the hexagon as base and the distance from the centre to that side as "
                   "height.",
                   "So the side length and the centre to side distance are enough: area = 6 × 1/2 × side × that "
                   "distance."],
                  "The side length and the perpendicular distance from the centre to a side"),
              FIO("FiO3.q4", U3 % 4,
                  "What fraction of the total area of the rectangle is the area of the blue region? (Two blue triangles "
                  "stand on the top and bottom sides of the rectangle, with their tips meeting at a point inside.)",
                  ["Each blue triangle has a full side of the rectangle as base: the length L.",
                   "Their heights, from the shared point to the top and to the bottom, add up to the width W.",
                   "Blue = 1/2 × L × h1 + 1/2 × L × h2 = 1/2 × L × (h1 + h2) = 1/2 × L × W."],
                  "Half of the rectangle is blue"),
              FIO("FiO3.q5", U3 % 5,
                  "Give a method to obtain a quadrilateral whose area is half that of a given quadrilateral.",
                  ["Mark the midpoints of the four sides and join them in order.",
                   "Each corner triangle cut off is one quarter of the triangle made by a diagonal (both sides are "
                   "halved).",
                   "The four corners together are one quarter of each pair of diagonal triangles, so half the "
                   "quadrilateral; the inner quadrilateral is the other half."],
                  "Join the midpoints of the sides in order; the inner quadrilateral has half the area")])],
    key_terms=["polygon", "triangle", "diagonal"]))

# ============================== T6 Parallelogram: cut and slide ==============================================
TOPICS.append(TOPIC(
    "T6", "M2", "Parallelogram: Cut and Slide", ["Parallelogram"], "Apply",
    "Students cut a triangle off a parallelogram and slide it to form a rectangle, derive area as base times height, "
    "and use either side as base with its own perpendicular height.",
    "Cut along a height and slide: a parallelogram becomes a rectangle with the same base and height, so its area is "
    "base × height, using any side with its own height.",
    [A("T6.C1", "Turn a parallelogram into a rectangle", "Understand",
       "Students cut a right triangle off a parallelogram along a height, slide it to the other end, and use "
       "congruent triangles to show the rectangle formed has the same area.",
       textbook=["Parallelogram",
                 "Give a method to convert a parallelogram into a rectangle of equal area.",
                 "Construct AX perpendicular to CD. We call this a height of the parallelogram. Cut the parallelogram "
                 "into ΔAXD and trapezium ABCX.",
                 "Can ΔAXD and ABCX fit together, as shown in the figure, to get a rectangle?",
                 "So, by the RHS congruency criterion, ΔBYC ≅ ΔAXD. Thus, ΔAXD will fit exactly over the region "
                 "occupied by ΔBYC, and convert the parallelogram into a rectangle.",
                 "The process of cutting a figure into pieces and rearranging them to get a different figure of equal "
                 "area is called dissection."],
       teach=["Predict first: if we cut a parallelogram and move a piece, can it become a rectangle of the same area?",
              "Cut along the height from one top corner. A right triangle comes away.",
              "Slide it to the other end: it matches the gap exactly, because the two right triangles are congruent. "
              "Nothing is added or lost. This cut and rearrange is called dissection."],
       examples=[
           WE("A parallelogram has base 9 cm and height 5 cm. Cut and slide it into a rectangle and find its area.",
              ["Cut along a height of 5 cm and slide the triangle across.",
               "The rectangle is 9 cm long and 5 cm high.", "Area = 9 × 5 = 45 cm²."],
              "45 cm², the same as the parallelogram",
              ncert=["para.method", "para.fit", "para.dissection"])],
       key_terms=["parallelogram", "dissection", "rectangle"], misconceptions=["M_RECT_PARA"], minutes=8),
     A("T6.C2", "Base times height, with any base", "Apply",
       "Students apply parallelogram area as base times height, choose either side as base with its own "
       "perpendicular height, and find a missing height from the area.",
       textbook=["How do we find the area of a parallelogram by dissecting it into a rectangle?",
                 "Since DX = CY, we get DC = XY by adding the common part XC to DX and CY. Since DC is the base of the "
                 "parallelogram, we get",
                 "Area of the parallelogram = base × height.",
                 "Can the area of the parallelogram be determined by taking another side as the base and its "
                 "corresponding height?",
                 "Can the parallelogram be cut along CZ and rearranged to form a rectangle?",
                 "It can be seen that this is indeed possible, and so any side and its corresponding height can be used "
                 "to find the area of a parallelogram."],
       teach=["Predict first: does the rule still work if we choose the other side as the base?",
              "With the other side as base, the height is the perpendicular distance between that pair of sides.",
              "The area does not change, so base times height gives the same answer for both pairs. Keeko multiplies "
              "by the slanting side instead; a cut along a true height shows why that gives too much."],
       examples=[
           WE("A parallelogram has sides 10 cm and 6 cm. The height on the 10 cm side is 4.8 cm. Find the area and the "
              "height on the 6 cm side.",
              ["Area = 10 × 4.8 = 48 cm².", "With base 6 cm: 6 × height = 48.", "Height = 48 ÷ 6 = 8 cm."],
              "Area 48 cm²; the height on the 6 cm side is 8 cm",
              ncert=["para.formula", "para.other_base", "para.cut_cz"])],
       key_terms=["parallelogram", "base", "height"], misconceptions=["M_SLANT_HEIGHT"], minutes=8),
     DOER("T6.C3", "Practice: cut, slide and choose a base for parallelograms", "parallelogram_cutter", "Analyze",
          "Students compare parallelogram areas and perimeters on equal bases and heights, find areas and missing "
          "heights, and turn triangles and rectangles into each other by dissection.",
          ["Area of a parallelogram = base × height.",
           "Any side can be the base, with the height perpendicular to it.",
           "Same base and same height means the same area, whatever the slant."],
          items=[
              FIO("FiO4.q1", U4 % 1,
                  "Observe the parallelograms (a) to (g) drawn on a grid, all on equal bases between the same two grid "
                  "lines. (i) What can we say about the areas of all these parallelograms? (ii) What can we say about "
                  "their perimeters? Which figure appears to have the maximum perimeter, and which has the minimum "
                  "perimeter?",
                  ["(i) Each has the same base and the same height, so each has the same area, base × height.",
                   "(ii) The perimeter is twice the base plus twice the slanting side.",
                   "The more a parallelogram leans, the longer its slanting sides, so the larger its perimeter."],
                  "(i) All have equal areas. (ii) The perimeters differ: (g), leaning most, appears largest and (a), "
                  "almost upright, smallest"),
              FIO("FiO4.q2", U4 % 2,
                  "Find the areas of the following parallelograms: (i) base 7 cm, height 4 cm, (ii) base 5 cm, height "
                  "3 cm, (iii) side 5 cm with height 4.8 cm drawn to it, (iv) side 2 cm with height 4.4 cm drawn to it.",
                  ["(i) 7 × 4 = 28 cm².", "(ii) 5 × 3 = 15 cm².", "(iii) 5 × 4.8 = 24 cm².",
                   "(iv) 2 × 4.4 = 8.8 cm²."],
                  "(i) 28 cm² (ii) 15 cm² (iii) 24 cm² (iv) 8.8 cm²"),
              FIO("FiO4.q3", U4 % 3,
                  "Find QN in parallelogram PQRS, where SR = 12 cm, the height QM to SR is 6 cm, PS = 7.6 cm, and QN is "
                  "perpendicular to PS.",
                  ["Area = SR × QM = 12 × 6 = 72 cm².", "Also area = PS × QN = 7.6 × QN.",
                   "QN = 72 ÷ 7.6 ≈ 9.47 cm."],
                  "QN ≈ 9.47 cm"),
              FIO("FiO4.q4", U4 % 4,
                  "Consider a rectangle and a parallelogram of the same sidelengths: 5 cm and 4 cm. Which has the "
                  "greater area? (Hint: imagine constructing them on the same base.)",
                  ["Rectangle: 5 × 4 = 20 cm².",
                   "On the same 5 cm base, the parallelogram's height is shorter than its slanting 4 cm side.",
                   "So its area, 5 × height, is less than 20 cm²."],
                  "The rectangle has the greater area"),
              FIO("FiO4.q5", U4 % 5,
                  "Give a method to obtain a rectangle whose area is twice that of a given triangle. What are the "
                  "different methods that you can think of?",
                  ["Method 1: draw a line through the top vertex parallel to the base and perpendiculars to the base at "
                   "its ends; the rectangle on the base and height is twice the triangle.",
                   "Method 2: take two copies of the triangle, join them into a parallelogram, then cut and slide it "
                   "into a rectangle.",
                   "Either way the rectangle is base × height, twice 1/2 × base × height."],
                  "Build the rectangle on the base and height, or join two copies into a parallelogram and cut and "
                  "slide"),
              FIO("FiO4.q6", U4 % 6,
                  "[Śulba-Sūtras] Give a method to obtain a rectangle of the same area as a given triangle.",
                  ["Join the midpoints of the two sides; this line is parallel to the base at half the height.",
                   "Drop perpendiculars from these midpoints to the base.",
                   "Cut off the two small top pieces and turn each down into the gap below it.",
                   "The result is a rectangle with the same base and half the height: 1/2 × base × height."],
                  "Cut at half the height and swing the top pieces down: a rectangle on the base with half the height"),
              FIO("FiO4.q7", U4 % 7,
                  "[Śulba-Sūtras] An isosceles triangle can be converted into a rectangle by dissection in a simpler "
                  "way. Can you find out how to do it? (Hint: show that ΔADB and ΔADC can be made into halves of a "
                  "rectangle.)",
                  ["The altitude AD of isosceles ΔABC meets BC at its midpoint, giving two congruent right triangles.",
                   "Turn ΔADC over and place it against ΔADB with the hypotenuses together.",
                   "The two right triangles form a rectangle with sides BD and AD, area 1/2 × BC × AD."],
                  "Cut along the altitude and join the two right triangles along their slanting sides to make a "
                  "rectangle BD by AD"),
              FIO("FiO4.q8", U4 % 8,
                  "[Śulba-Sūtras] Give a method to convert a rectangle into an isosceles triangle by dissection.",
                  ["Cut the rectangle along a diagonal into two congruent right triangles.",
                   "Flip one triangle over and stand the two back to back, joined along the leg equal to the width.",
                   "They form an isosceles triangle with base twice the rectangle's length and height equal to its width."],
                  "Cut along a diagonal and stand the two right triangles back to back"),
              FIO("FiO4.q9", U4 % 9,
                  "Which has greater area: an equilateral triangle or a square of the same sidelength as the triangle? "
                  "Which has greater area: two identical equilateral triangles together or a square of the same "
                  "sidelength as the triangle? Give reasons.",
                  ["Square of side s: area s × s.",
                   "The triangle's height is less than its slanting side s, so its area is less than 1/2 × s × s.",
                   "Two triangles make a rhombus with base s and height less than s, so less than s × s too."],
                  "The square is greater in both cases")],
          misconceptions=["M_SLANT_HEIGHT", "M_RECT_PARA"])],
    key_terms=["parallelogram", "base", "height"]))

# ============================== T7 Rhombus ====================================================================
TOPICS.append(TOPIC(
    "T7", "M2", "Rhombus: Half the Product of Diagonals", ["Rhombus"], "Apply",
    "Students dissect a rhombus along its diagonals into a rectangle, derive area as half the product of the "
    "diagonals, and check it by splitting the rhombus into two triangles.",
    "A rhombus is half the rectangle on its diagonals: area = 1/2 × product of the diagonals, which the two triangle "
    "split confirms.",
    [A("T7.C1", "Dissect a rhombus into a rectangle", "Understand",
       "Students cut a rhombus along its diagonals into four right triangles, rearrange them into a rectangle, and "
       "read the rectangle's sides as one diagonal and half the other.",
       textbook=["Rhombus",
                 "Since a rhombus is a parallelogram, the area formula for a parallelogram holds for a rhombus as well. "
                 "However, the additional properties of a rhombus give us another method to transform a rhombus into a "
                 "rectangle of the same area by dissection. This method occurs in one of the Śulba-Sūtras.",
                 "Try working this out!",
                 "What are the sidelengths of the rectangle WXYZ?",
                 "XW = length of the diagonal AC, and WZ = half the length of the other diagonal BD.",
                 "Area of a rhombus = 1/2 × product of diagonals."],
       teach=["Predict first: a rhombus has four equal sides and no right angles. Can its pieces make a rectangle?",
              "The diagonals cross at right angles and halve each other, so they cut four right triangles.",
              "Pair them into two small rectangles and stack them: one whole diagonal by half the other."],
       examples=[
           WE("A rhombus has diagonals 12 cm and 8 cm. Dissect it into a rectangle and find the area.",
              ["The rectangle has one side 12 cm, the whole diagonal.", "Its other side is 8 ÷ 2 = 4 cm, half the other.",
               "Area = 12 × 4 = 48 cm²."],
              "48 cm²",
              ncert=["rhom.dissect", "rhom.sides"])],
       key_terms=["rhombus", "diagonals", "dissection"], misconceptions=["M_RHOMBUS_DIAG"], minutes=8),
     A("T7.C2", "Two triangles on one diagonal", "Apply",
       "Students split a rhombus along one diagonal into two triangles, add their areas, and simplify to half the "
       "product of the two diagonals.",
       textbook=["Area of rhombus ABCD can also be determined by finding the areas of ΔADB and ΔCDB. What formula does "
                 "this give us?",
                 "Since the diagonals are perpendicular to each other, we have Area (ΔADB) = 1/2 × AO × BD, and "
                 "Area (ΔCDB) = 1/2 × CO × BD.",
                 "Simplify the expression to show that we get the same formula for the area of a rhombus in terms of "
                 "its diagonals."],
       teach=["Predict first: Keeko multiplies the two diagonals of a rhombus. Is that the area?",
              "Cut along one diagonal. Each triangle has that diagonal as base and half the other diagonal as height.",
              "Add the two: half of one diagonal times the other. The full product is the rectangle round the rhombus, "
              "twice too big."],
       examples=[
           WE("A rhombus has diagonals 10 cm and 6 cm. Find its area using two triangles.",
              ["Each triangle has base 10 cm and height 6 ÷ 2 = 3 cm.", "Each triangle: 1/2 × 10 × 3 = 15 cm².",
               "Rhombus: 15 + 15 = 30 cm², and 1/2 × 10 × 6 = 30 cm²."],
              "30 cm²",
              ncert=["rhom.triangles", "rhom.simplify"])],
       key_terms=["rhombus", "diagonals", "triangle"], misconceptions=["M_RHOMBUS_DIAG"], minutes=8),
     DOER("T7.C3", "Practice: rhombus areas and dissections", "rhombus_dissector", "Apply",
          "Students find a rhombus area from its diagonals and give a dissection that turns a rectangle into a "
          "rhombus of equal area.",
          ["Area of a rhombus = 1/2 × product of the diagonals.",
           "The diagonals of a rhombus cross at right angles and bisect each other.",
           "Never use the full product of the diagonals."],
          items=[
              FIO("FiO5.q1", U5 % 1,
                  "Find the area of a rhombus whose diagonals are 20 cm and 15 cm.",
                  ["Area = 1/2 × 20 × 15.", "= 1/2 × 300 = 150 cm²."],
                  "150 cm²"),
              FIO("FiO5.q2", U5 % 2,
                  "Give a method to convert a rectangle into a rhombus of equal area using dissection.",
                  ["Cut the rectangle (length L, width W) into two halves, each L/2 long and W wide.",
                   "Cut each half along a diagonal: four congruent right triangles with legs L/2 and W.",
                   "Arrange them with the right angles meeting at one centre point: a rhombus with diagonals L and 2W.",
                   "Its area is 1/2 × L × 2W = L × W, the rectangle's area."],
                  "Cut into four congruent right triangles and put the right angles together at the centre")],
          misconceptions=["M_RHOMBUS_DIAG"])],
    key_terms=["rhombus", "diagonals"]))

# ============================== T8 Trapezium =================================================================
TOPICS.append(TOPIC(
    "T8", "M2", "Trapezium: Two Copies Make a Parallelogram",
    ["Trapezium", "Finding the Area Using Two Copies of the Trapezium"], "Analyze",
    "Students find trapezium areas on a grid, split a trapezium into a rectangle and triangles, join two copies into "
    "a parallelogram, and use area as one half the height times the sum of the parallel sides.",
    "A trapezium splits into a rectangle and triangles, or two copies make a parallelogram with base a + b: area = "
    "1/2 × h × (a + b).",
    [A("T8.C1", "Trapeziums on a grid", "Apply",
       "Students find the area of a trapezium on a grid by breaking it into a rectangle and right triangles and "
       "counting the square units in each trapezium part.",
       textbook=["Trapezium",
                 "Find the areas of the following trapeziums by breaking them into figures whose areas can be computed.",
                 "One way of finding the area of a trapezium is by breaking it into a rectangle and triangles."],
       teach=["Predict first: can a trapezium's area be found by counting squares, when its slanting side cuts "
              "through them?",
              "Drop a height from the end of the shorter parallel side. A rectangle and a right triangle appear.",
              "Count the rectangle's squares, find the triangle as half a rectangle, and add."],
       examples=[
           WE("Trapezium ABCD on a grid has AB = 4 units, DC = 6 units and height AD = 4 units, with a right angle at D. "
              "Find its area.",
              ["Drop BM perpendicular to DC. ABMD is a 4 by 4 square: 16 square units.",
               "ΔBMC has base MC = 6 − 4 = 2 and height 4: 1/2 × 2 × 4 = 4.",
               "Area of ABCD = 16 + 4 = 20 square units."],
              "20 square units",
              ncert=["trap.grid"])],
       key_terms=["trapezium", "grid"], minutes=6),
     A("T8.C2", "A rectangle and two triangles", "Apply",
       "Students cut a trapezium by two heights into a rectangle and two triangles, add the areas, and reach one "
       "half the height times the sum of the parallel sides.",
       textbook=["Consider a trapezium WXYZ with WX ∥ ZY. Find its area.",
                 "Construct WM ⊥ ZY, and XN ⊥ ZY (WM and XN perpendicular to ZY).",
                 "Is WXNM a rectangle?",
                 "Area WXYZ = Area (ΔWMZ) + Area WXNM + Area (ΔXNY).",
                 "Can the area of the trapezium be expressed in terms of a, b and h?",
                 "Area of a trapezium = 1/2 × height × sum of the parallel sides."],
       teach=["Predict first: is there one rule for every trapezium, the way there is for a triangle?",
              "Drop two heights from the shorter parallel side. The middle is a rectangle, the ends are two triangles "
              "with the same height.",
              "Adding the three pieces gives 1/2 × h × (a + b). Keeko uses only the longer side; that also counts "
              "area outside the trapezium."],
       examples=[
           WE("Trapezium WXYZ has WX = 5 units, ZY = 9 units and height 4 units, with ZM = 2 and NY = 2. Find its area.",
              ["Rectangle WXNM: 5 × 4 = 20.", "Each end triangle: 1/2 × 2 × 4 = 4.",
               "Total = 4 + 20 + 4 = 28, and 1/2 × 4 × (5 + 9) = 28."],
              "28 square units",
              ncert=["trap.wxyz", "trap.formula"])],
       key_terms=["trapezium", "parallel sides", "height"], misconceptions=["M_TRAP_ONE_SIDE"], minutes=8),
     A("T8.C2x", "When both slants lean the same way", "Analyze",
       "Students handle a trapezium whose height falls outside the longer side by adding and subtracting "
       "triangles, and check that the trapezium formula still holds.",
       textbook=["Will this formula hold for a trapezium that looks like this?",
                 "There are different ways of approaching this, which are sketched below. Complete the arguments.",
                 "Approach 1: Rectangle and Triangles. Area ABCD = Area ABED + Area ΔBEC. Area ABED = Area ABEF − "
                 "Area ΔAFD.",
                 "Approach 2: Parallelogram and Triangle. Draw BG ∥ AD.",
                 "Will Approach 2 work for any type of trapezium?"],
       teach=["Predict first: in this trapezium the height from A lands outside the bottom side. Does the rule break?",
              "Draw BG parallel to AD. The trapezium becomes a parallelogram ABGD and a triangle BGC.",
              "Parallelogram a × h plus triangle 1/2 × (b − a) × h gives 1/2 × h × (a + b): the rule holds."],
       examples=[
           WE("A slanting trapezium has parallel sides AB = 6 cm and DC = 10 cm and height 5 cm. Use Approach 2 to find "
              "its area.",
              ["Parallelogram ABGD: 6 × 5 = 30 cm².", "Triangle BGC has base 10 − 6 = 4 cm: 1/2 × 4 × 5 = 10 cm².",
               "Total = 30 + 10 = 40 cm², and 1/2 × 5 × (6 + 10) = 40 cm²."],
              "40 cm²",
              ncert=["trap.obtuse", "trap.approach1", "trap.approach2", "trap.mt_any"])],
       key_terms=["trapezium", "parallelogram"], misconceptions=["M_OUTSIDE_HEIGHT"], minutes=6, thin=True),
     A("T8.C3", "Two copies make a parallelogram", "Analyze",
       "Students join two copies of a trapezium into a parallelogram with base equal to the sum of the parallel "
       "sides and halve its area to get the trapezium's area.",
       textbook=["Finding the Area Using Two Copies of the Trapezium",
                 "Consider two copies of the given trapezium in which AB ∥ CD. Rotate the second copy as shown.",
                 "What figure will we get when the two trapeziums are joined along BC?",
                 "Since AB ∥ CD, we have x + y = 180, since they are internal angles along the same side of the "
                 "transversal (BC). Therefore, the resulting figure is a quadrilateral.",
                 "What type of a quadrilateral is this?",
                 "Area of the trapezium = 1/2 × Area of the parallelogram = 1/2 h(a + b)."],
       teach=["Predict first: two copies of a trapezium, one turned round, joined along a slanting side. What shape?",
              "The angles at the joint add to 180, so the edges run straight: the short side of one continues the "
              "long side of the other, making a side a + b long.",
              "Opposite sides are parallel: a parallelogram of area (a + b) × h, and the trapezium is half of it."],
       examples=[
           WE("A trapezium has parallel sides 7 cm and 11 cm and height 6 cm. Use two copies to find its area.",
              ["The parallelogram has base 7 + 11 = 18 cm and height 6 cm.", "Its area is 18 × 6 = 108 cm².",
               "The trapezium is half: 108 ÷ 2 = 54 cm²."],
              "54 cm²",
              ncert=["trap.two_copies", "trap.quad_type"])],
       key_terms=["trapezium", "parallelogram", "copies"], misconceptions=["M_TRAP_ONE_SIDE"], minutes=8),
     DOER("T8.C4", "Practice: join two copies, find trapezium areas", "trapezium_joiner", "Analyze",
          "Students find trapezium areas from parallel sides and height, convert trapeziums into rectangles and "
          "triangles by dissection, and compare the parts of a dissected hexagon.",
          ["Area of a trapezium = 1/2 × h × (a + b).",
           "Use the perpendicular height, never a slanting side.",
           "Cutting through the midpoint of a slanting side and turning the piece keeps the area."],
          items=[
              FIO("FiO5.q3", U5 % 3,
                  "Find the areas of the following figures: (i) a trapezium with parallel sides 10 ft and 7 ft and "
                  "height 16 ft between them, (ii) parallel sides 24 m and 36 m, height 14 m, (iii) parallel sides "
                  "14 in and 6 in, height 10 in, (iv) parallel sides 12 ft and 18 ft, height 8 ft.",
                  ["(i) 1/2 × 16 × (10 + 7) = 1/2 × 16 × 17 = 136 ft².",
                   "(ii) 1/2 × 14 × (24 + 36) = 1/2 × 14 × 60 = 420 m².",
                   "(iii) 1/2 × 10 × (14 + 6) = 1/2 × 10 × 20 = 100 in².",
                   "(iv) 1/2 × 8 × (12 + 18) = 1/2 × 8 × 30 = 120 ft²."],
                  "(i) 136 ft² (ii) 420 m² (iii) 100 in² (iv) 120 ft²"),
              FIO("FiO5.q4", U5 % 4,
                  "[Śulba-Sūtras] Give a method to convert an isosceles trapezium to a rectangle using dissection.",
                  ["Mark the midpoint of each slanting side.",
                   "Through each midpoint draw a line perpendicular to the parallel sides.",
                   "Cut off the small corner triangle below each midpoint and turn it about the midpoint into the gap "
                   "above it; the two halves of each slanting side match.",
                   "The result is a rectangle with height h and length 1/2 × (a + b)."],
                  "Cut through the midpoints of the slanting sides at right angles to the base and swing the corner "
                  "pieces up: a rectangle 1/2 × (a + b) by h"),
              FIO("FiO5.q5", U5 % 5,
                  "Here is one of the ways to convert trapezium ABCD into a rectangle EFGH of equal area. Given the "
                  "trapezium ABCD, how do we find the vertices of the rectangle EFGH? (Hint: if ΔAHI ≅ ΔDGI and "
                  "ΔBEJ ≅ ΔCFJ, then the trapezium and rectangle have equal areas.)",
                  ["Mark I and J, the midpoints of the slanting sides AD and BC.",
                   "Through I draw the line perpendicular to DC; it meets DC at G and the line AB extended at H.",
                   "Through J do the same to get F on DC and E on AB extended.",
                   "Since AI = DI and the angles match, ΔAHI ≅ ΔDGI and ΔBEJ ≅ ΔCFJ, so EFGH has the trapezium's area."],
                  "Take the midpoints I and J of the slanting sides and draw perpendiculars to DC through them; they "
                  "meet DC and line AB at G, H, F and E"),
              FIO("FiO5.q6", U5 % 6,
                  "Using the idea of converting a trapezium into a rectangle of equal area, and vice versa, construct a "
                  "trapezium of area 144 cm².",
                  ["A trapezium has the area of a rectangle with sides h and 1/2 × (a + b).",
                   "Choose a 12 cm by 12 cm rectangle: area 144 cm². So h = 12 and a + b = 24.",
                   "Take a = 8 and b = 16: 1/2 × 12 × (8 + 16) = 144."],
                  "For example, parallel sides 8 cm and 16 cm with height 12 cm (any a + b and h with "
                  "h × (a + b) = 288 works)"),
              FIO("FiO5.q7", U5 % 7,
                  "A regular hexagon is divided into a trapezium, an equilateral triangle, and a rhombus, as shown. Find "
                  "the ratio of their areas.",
                  ["Joining the centre to the corners splits a regular hexagon into 6 equal equilateral triangles.",
                   "The trapezium is half the hexagon: 3 of these triangles.",
                   "The rhombus is 2 of them and the equilateral triangle is 1."],
                  "Trapezium : triangle : rhombus = 3 : 1 : 2"),
              FIO("FiO5.q8", U5 % 8,
                  "ZYXW is a trapezium with ZY ∥ WX. A is the midpoint of XY. Show that the area of the trapezium ZYXW is "
                  "equal to the area of ΔZWB, where ZA extended meets WX extended at B.",
                  ["YA = XA, since A is the midpoint of XY.",
                   "∠ZAY = ∠BAX (vertically opposite) and ∠ZYA = ∠BXA (alternate angles, since ZY ∥ WB).",
                   "So ΔZYA ≅ ΔBXA (ASA): they have equal areas.",
                   "Trapezium ZYXW = ZAXW + ΔZYA = ZAXW + ΔBXA = ΔZWB."],
                  "ΔZYA ≅ ΔBXA, so swapping one for the other shows the trapezium and ΔZWB have equal areas")],
          misconceptions=["M_TRAP_ONE_SIDE", "M_SLANT_HEIGHT"])],
    key_terms=["trapezium", "parallel sides", "height"]))
