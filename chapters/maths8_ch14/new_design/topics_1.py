# -*- coding: utf-8 -*-
"""Topics T1 to T4 (module M1: rectangles, squares and triangles). Book section 7.1 and Triangles, pp 148 to 158."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []
U1 = "Figure it Out (rectangles and squares, question %s)"
U2 = "Figure it Out (triangles, question %s)"

# ============================== T1 Four equal parts of a square ===============================================
TOPICS.append(TOPIC(
    "T1", "M1", "Four Equal Parts of a Square", ["Chapter opening", "7.1"], "Understand",
    "",
    "A square cut into 4 parts of equal area in more ways than we can count: equal area does not need equal shape.",
    [A("T1.C1", "How many ways to cut a square into 4 equal areas?", "Understand",
       "",
       textbook=["7.1 Rectangle and Squares",
                 "How many different ways can you divide a square into 4 parts of equal area?",
                 "One can actually think of infinitely many such ways! Consider a division, such as, and alter each "
                 "part as follows.",
                 "In each part, the area is compressed along one edge and expanded along another edge. If both the "
                 "compression and expansion are of the same magnitude, then all 4 parts still have the same area!",
                 "Try to think of different creative ways to divide a square into 4 parts of equal area."],
       teach=["Predict first: how many ways can a square be cut into 4 parts of equal area? Two? Five? More?",
              "Four small squares is one way. Push a notch into one edge of each part and push the same bump out of "
              "another edge: the shapes change, the areas do not.",
              "Since every notch can be a different shape, there are infinitely many ways. Equal area does not mean "
              "equal shape. So what exactly is area, and how do we measure it?"],
       ncert=["7.1.four_parts", "7.1.mt_creative"], key_terms=["area", "equal parts"],
       misconceptions=["M_EQUAL_SHAPE"], video_focus=["HOOK"], minutes=4, enrichment=True)],
    topic_type="framing"))

# ============================== T2 Rectangles: area, not perimeter ===========================================
TOPICS.append(TOPIC(
    "T2", "M1", "Rectangles: Area Is Not Perimeter", ["7.1"], "Analyze",
    "Students compute rectangle area as length times width in square units, find the area of the triangle cut off "
    "by a diagonal, and show with rectangles and other shapes that a longer perimeter does not mean a larger area.",
    "Area counts unit squares: a rectangle is length × width, a diagonal cuts it into two halves, and perimeter is a "
    "different measure that cannot replace area.",
    [A("T2.C1", "Rectangle area: length times width", "Apply",
       "Students compare two rectangles by counting unit squares, write the area as length times width, and record "
       "it in square centimetres.",
       textbook=["You might have seen the rangoli art form, in which regions of different shapes are beautifully "
                 "coloured using rangoli powder.",
                 "Which of these rectangles requires more rangoli powder to be coloured, if the colouring is done "
                 "evenly?",
                 "Clearly, the rectangle having sidelengths 7 cm and 4 cm contains 7 × 4 = 28 unit squares, and the "
                 "rectangle having sidelengths 8 cm and 3 cm contains 8 × 3 = 24 unit squares.",
                 "Area of a rectangle = length × width.",
                 "The areas of the rectangles as seen in the previous problem are generally written as 28 sq. cm and "
                 "24 sq. cm, or as 28 cm² and 24 cm²."],
       teach=["Predict first: the 8 cm by 3 cm rectangle is taller. Does it need more powder than the 7 cm by 4 cm one?",
              "Fill each rectangle with unit squares of side 1 cm. Rows times columns counts them quickly.",
              "The shorter, wider rectangle wins: it holds more unit squares. Area is written in cm² or sq. cm."],
       examples=[
           WE("A rangoli artist has a 7 cm by 4 cm rectangle and an 8 cm by 3 cm rectangle. Which needs more powder?",
              ["Count unit squares in the first: 7 × 4 = 28.", "Count unit squares in the second: 8 × 3 = 24.",
               "28 is more than 24."],
              "The 7 cm by 4 cm rectangle needs more powder: 28 cm² against 24 cm²",
              ncert=["7.1.rangoli", "7.1.rect_formula", "7.1.units"])],
       key_terms=["area", "unit square", "rectangle"], misconceptions=["M_PERIM_AREA"], minutes=8),
     A("T2.C2", "A diagonal halves a rectangle", "Apply",
       "Students explain why a diagonal splits a rectangle into two congruent triangles and compute the area of "
       "each triangle as half of length times width.",
       textbook=["What is the area of each triangle in this rectangle?",
                 "We have seen that the diagonal of a rectangle divides it into two congruent triangles. So, the area "
                 "of each triangle is half the area of the rectangle.",
                 "In terms of unit squares, half the area fills exactly half the number of unit squares.",
                 "So the area of each triangle is 1/2 × 7 × 4 = 14 cm²."],
       teach=["Predict first: a diagonal cuts a 7 cm by 4 cm rectangle. Is each piece exactly half?",
              "The two triangles are congruent: turn one round and it sits exactly on the other.",
              "So each triangle is half the rectangle, even though it cuts through unit squares."],
       examples=[
           WE("A diagonal is drawn in a 7 cm by 4 cm rectangle. Find the area of each triangle.",
              ["The rectangle has area 7 × 4 = 28 cm².", "The diagonal makes two congruent triangles.",
               "Each triangle is 1/2 × 28 = 14 cm²."],
              "Each triangle has area 14 cm²",
              ncert=["7.1.diag_triangle"])],
       key_terms=["diagonal", "triangle", "half"], minutes=6),
     A("T2.C3", "Why perimeter cannot measure area", "Analyze",
       "Students find two rectangles where the one with the larger perimeter has the smaller area and explain why "
       "the boundary length cannot measure area.",
       textbook=["Why do we count the number of unit squares to assign measures for area? Couldn't we have just used "
                 "the perimeter of a region, i.e., the length of its boundary as a measure of its area?",
                 "If two regions have the same perimeter, can't we conclude that they have the same area? Or, if one "
                 "region has a larger perimeter than another region, can't we conclude that it also has a larger area?",
                 "The perimeter of a region is not indicative of its area. The reason is that regions can have the "
                 "same perimeter but different areas, and vice versa.",
                 "Perimeter of Region 1 > Perimeter of Region 2, but Area of Region 1 < Area of Region 2.",
                 "Find two rectangles that are examples of such regions. If needed, use a grid paper for this."],
       teach=["Predict first: Keeko thinks the rectangle with the longer boundary must hold more squares. Is that right?",
              "A 10 by 1 strip has perimeter 22 and area 10. A 5 by 4 rectangle has perimeter 18 and area 20.",
              "The strip has the longer boundary but half the area. Perimeter measures the edge, area counts the inside."],
       examples=[
           WE("Compare a 10 cm by 1 cm strip with a 5 cm by 4 cm rectangle: perimeter and area.",
              ["Strip perimeter: 2 × (10 + 1) = 22 cm. Strip area: 10 × 1 = 10 cm².",
               "Rectangle perimeter: 2 × (5 + 4) = 18 cm. Rectangle area: 5 × 4 = 20 cm².",
               "22 > 18 but 10 < 20."],
              "The strip has the larger perimeter (22 cm) but the smaller area (10 cm²)",
              ncert=["7.1.perim_why", "7.1.perim_same", "7.1.perim_find_rects"])],
       key_terms=["perimeter", "area", "boundary"], misconceptions=["M_PERIM_AREA"], minutes=8),
     A("T2.C3x", "A longer boundary, a smaller area: other shapes", "Create",
       "Students design a pair of shapes other than rectangles in which the shape with the larger perimeter "
       "visibly has the smaller area.",
       textbook=["Also give an example of two regions of other shapes, where the region with the larger perimeter "
                 "has the smaller area! This property should be visually clear in your example."],
       teach=["Predict first: can a shape with a very long, wiggly boundary still have a tiny area?",
              "Take a 4 by 4 square of 16 unit squares. Now join 9 unit squares edge to edge in a thin zigzag.",
              "Each extra square adds 2 unit edges to the boundary, so the zigzag's boundary grows while its area "
              "stays small."],
       examples=[
           WE("Compare a 4 by 4 square with a thin zigzag made of 9 unit squares joined edge to edge in one line "
              "with bends.",
              ["Square: perimeter 4 × 4 = 16 units, area 16 square units.",
               "Zigzag: each square shares edges with its neighbours, leaving 2 × 9 + 2 = 20 unit edges on the "
               "boundary, so perimeter 20 units.",
               "Zigzag area: 9 square units."],
              "The zigzag has the larger perimeter (20 units against 16) but the smaller area (9 against 16)",
              ncert=["7.1.mt_perim_shapes"])],
       key_terms=["perimeter", "area"], misconceptions=["M_PERIM_AREA"], minutes=6, thin=True),
     DOER("T2.C4", "Practice: stretch a rectangle, compare area and perimeter", "rectangle_stretcher", "Analyze",
          "Students find missing sides from areas, find path and tube areas by splitting into rectangles, and predict "
          "how area grows when every side of a square is doubled.",
          ["Area counts unit squares; a rectangle is length × width.",
           "Split an awkward region into rectangles, or subtract the part that is not wanted.",
           "Perimeter and area are different: one can grow while the other shrinks."],
          items=[
              FIO("FiO1.q1", U1 % 1,
                  "Identify the missing sidelengths. (i) A plus shaped figure is made of four rectangles: a 28 in² "
                  "piece whose right edge rises 4 in above a 21 in² piece of length 7 in, a 35 in² piece of width "
                  "3 in plus the width of the 28 in² piece, and a 14 in² strip that hangs 2 in below the 35 in² "
                  "piece; find the width of the 14 in² strip. (ii) A 29 m² piece and an 11 m² piece are both 4 m "
                  "tall, and the bold rectangle made of the 29 m² piece and the piece below it has area 50 m²; find "
                  "the missing sides.",
                  ["(i) The 21 in² piece is 7 in long, so its height is 21 ÷ 7 = 3 in.",
                   "The 28 in² piece is 4 + 3 = 7 in tall, so its width is 28 ÷ 7 = 4 in.",
                   "The 35 in² piece is 3 + 4 = 7 in wide, so its height is 35 ÷ 7 = 5 in.",
                   "The 14 in² strip is 5 + 2 = 7 in tall, so its width is 14 ÷ 7 = 2 in.",
                   "(ii) Top widths: 29 ÷ 4 = 7.25 m and 11 ÷ 4 = 2.75 m.",
                   "The lower piece has area 50 − 29 = 21 m² and width 7.25 m, so its height is 21 ÷ 7.25 ≈ 2.9 m."],
                  "(i) 2 in, with 3 in, 4 in and 5 in on the way. (ii) 7.25 m and 2.75 m across the top, and a lower "
                  "height of 84/29 m, about 2.9 m"),
              FIO("FiO1.q2", U1 % 2,
                  "A path (the shaded portion) is laid around a rectangular park EFGH inside a rectangle ABCD. (i) What "
                  "measurements do you need to find the area of the path? Assign values and give a formula. (ii) If the "
                  "width of the path along each side is given, can you find its area? If not, what else do you need? "
                  "(iii) Does the area of the path change when the outer rectangle is moved while keeping the park "
                  "inside it?",
                  ["(i) Measure the length and width of ABCD and of EFGH.",
                   "Area of path = area of ABCD − area of EFGH. With ABCD 20 m by 14 m and EFGH 16 m by 10 m: "
                   "20 × 14 − 16 × 10 = 280 − 160 = 120 m².",
                   "(ii) The widths alone are not enough; we also need the park's length and width. With a park 16 m by "
                   "10 m and widths 2 m on every side, break the path into two long strips 20 m by 2 m and two short "
                   "strips 10 m by 2 m: 2 × 40 + 2 × 20 = 120 m².",
                   "(iii) Moving ABCD around the park changes the widths but not the two rectangles, so the path area "
                   "stays the same."],
                  "(i) Path area = area of ABCD − area of EFGH (120 m² for the chosen values). (ii) Also need the park's "
                  "sides; same 120 m². (iii) No, the area does not change"),
              FIO("FiO1.q3", U1 % 3,
                  "A plot has sides 14 m and 12 m with a crosspath. What other measurements do you need to find the area "
                  "of the crosspath? Assign values and give a formula.",
                  ["We need the widths of the two paths: p for the path along the 14 m side and q for the path along "
                   "the 12 m side.",
                   "The two strips are 14 × p and 12 × q, but they overlap in a p by q square counted twice.",
                   "Area = 14p + 12q − pq. With p = 1 m and q = 2 m: 14 × 1 + 12 × 2 − 1 × 2 = 14 + 24 − 2 = 36 m²."],
                  "The widths of the two paths; area = 14p + 12q − pq, which is 36 m² when the widths are 1 m and 2 m"),
              FIO("FiO1.q4", U1 % 4,
                  "Find the area of the spiral tube shown in the figure. The tube has the same width (1 unit) throughout, "
                  "and its straight parts measure 20, 20, 20, 15, 15, 10, 10, 5 and 5 along the outside.",
                  ["The hint: an L shaped tube with arms 5 and 5 has the same area as a straight tube of length "
                   "5 + 5 − 1 = 9, because the corner square is counted in both arms.",
                   "Add all the straight lengths: 20 + 20 + 20 + 15 + 15 + 10 + 10 + 5 + 5 = 120.",
                   "There are 8 bends, each counted twice, so subtract 8: 120 − 8 = 112.",
                   "The straightened tube is 112 units long and 1 unit wide: 112 × 1 = 112."],
                  "112 square units"),
              FIO("FiO1.q5", U1 % 5,
                  "A square is divided into regions 1, 2 and 3. If the sidelength of the square is doubled, what is the "
                  "increase in the areas of the regions 1, 2 and 3? Give reasons.",
                  ["Doubling the side doubles every length in the figure, both across and up.",
                   "Each region's area is multiplied by 2 × 2 = 4.",
                   "So each region grows by 4 − 1 = 3 times its old area."],
                  "Each region becomes 4 times as big, an increase of 3 times its original area"),
              FIO("FiO1.q6", U1 % 6,
                  "Divide a square into 4 parts by drawing two perpendicular lines inside the square, then rearrange the "
                  "pieces to get a larger square with a hole inside.",
                  ["Draw two perpendicular lines through the square that are not parallel to its sides; the 4 pieces "
                   "are congruent.",
                   "Turn the pieces so that each right angle points outward and the long edges run round the outside.",
                   "The outside forms a bigger square; the gap in the middle is a small square hole.",
                   "The area of the big square minus the hole equals the area of the original square."],
                  "The 4 congruent pieces form a larger square around a square hole; total area is unchanged")],
          misconceptions=["M_PERIM_AREA", "M_SCALE_AREA"])],
    key_terms=["area", "perimeter", "rectangle"]))

# ============================== T3 The area of a triangle =====================================================
TOPICS.append(TOPIC(
    "T3", "M1", "The Area of a Triangle", ["Triangles"], "Apply",
    "Students show that a triangle is half its enclosing rectangle, derive area as one half base times height, and "
    "extend the formula to a triangle whose height falls outside it by subtracting areas.",
    "A triangle is half the rectangle on its base and height, so area = 1/2 × base × height, and the formula still "
    "holds when the height lies outside the triangle.",
    [A("T3.C1", "Half the rectangle, wherever the top vertex sits", "Analyze",
       "Students compare triangles drawn on the same side of identical rectangles, drop an altitude, and show each "
       "triangle is half the rectangle.",
       textbook=["In the given figure, which triangle has a greater area: ΔXDC or ΔYDC, if both the rectangles are "
                 "identical?",
                 "In the given figure, which triangle has a greater area: ΔXDC or ΔYBC, if both the rectangles are "
                 "identical?",
                 "In each case, by dropping the altitudes from X and Y, it becomes clear that each triangle has exactly "
                 "half the area of the rectangle ABCD.",
                 "Find the area of ΔXDC."],
       teach=["Predict first: in two identical rectangles, X is near a corner and Y is in the middle of the top. "
              "Which triangle on DC is bigger?",
              "Drop the altitude from X to DC. It cuts the rectangle into two smaller rectangles, and each is halved "
              "by a side of the triangle.",
              "So the triangle is half of the left rectangle plus half of the right one: half the whole, wherever X is."],
       examples=[
           WE("X is on the top side of a rectangle with DC = 5 cm and height 4 cm. Find the area of ΔXDC.",
              ["Drop the altitude XY to DC. It splits the rectangle into two rectangles.",
               "Each small rectangle is cut in half by XD or XC.",
               "So ΔXDC is half of the whole rectangle: 1/2 × 5 × 4 = 10 cm²."],
              "10 cm²",
              ncert=["tri.xdc_ydc", "tri.xdc_ybc", "tri.fig_xdc"])],
       key_terms=["altitude", "triangle", "half"], misconceptions=["M_TOP_VERTEX"], minutes=8),
     A("T3.C2", "Base and height: one half base times height", "Apply",
       "Students build the outer rectangle of a triangle from a line parallel to its base and two perpendiculars, "
       "and compute area as one half times base times height.",
       textbook=["To find the area of a triangle, what measurements do we need?",
                 "We need the sidelengths of the outer rectangle.",
                 "How do we get the outer rectangle from the given triangle?",
                 "BCDE is a rectangle (how?). Let us take its sidelengths to be height and base. Then, "
                 "Area (ΔABC) = 1/2 × base × height.",
                 "Since BXAE is a rectangle (how?), the height of the rectangle is the same as the height of the "
                 "triangle.",
                 "Thus, if the height and the base of a triangle are known, we can find its area.",
                 "Area of a triangle = 1/2 × base × height."],
       teach=["Predict first: which measurements of a triangle do you need to find its area?",
              "Draw perpendiculars to BC at B and C, and a line through A parallel to BC. They meet to form "
              "rectangle BCDE, because all four angles are right angles.",
              "Its width is the base BC and its height is the altitude AX, so the triangle is 1/2 × base × height. "
              "Keeko leaves out the half; the rectangle shows why it must be there."],
       examples=[
           WE("A triangle has base 8 cm and height 5 cm. Find its area.",
              ["Its outer rectangle is 8 cm by 5 cm, area 8 × 5 = 40 cm².",
               "The triangle is half of it.", "Area = 1/2 × 8 × 5 = 20 cm²."],
              "20 cm²",
              ncert=["tri.measure", "tri.outer_rect", "tri.formula"])],
       key_terms=["base", "height", "triangle"], misconceptions=["M_TRI_FULL", "M_SLANT_HEIGHT"], minutes=8),
     A("T3.C3", "When the height falls outside the triangle", "Analyze",
       "Students find the area of an obtuse triangle as the difference of two right triangles and show it still "
       "equals one half times base times height.",
       textbook=["Will this formula hold for the kind of triangle, around which we cannot draw a rectangle with BC as "
                 "the base?",
                 "Here is one way to look at it. The area of ΔABC is the difference of the areas of ΔADC and ΔADB, each "
                 "of which can be enclosed in a rectangle.",
                 "Area (ΔABC) = 1/2 × h × DC − 1/2 × h × DB = 1/2 × h (DC − DB) = 1/2 × h × BC.",
                 "Thus, the area formula holds for all types of triangles."],
       teach=["Predict first: if the height from A lands outside BC, does the formula break?",
              "Extend CB to D below A. The big right triangle ADC minus the small right triangle ADB leaves ΔABC.",
              "Taking out the common half and height leaves DC − DB, which is BC. The formula holds for every triangle."],
       examples=[
           WE("In an obtuse triangle ABC the height from A meets CB extended at D, with h = 4 cm, DB = 3 cm and "
              "BC = 6 cm. Find the area.",
              ["DC = DB + BC = 3 + 6 = 9 cm.",
               "Area of ΔADC = 1/2 × 4 × 9 = 18 cm². Area of ΔADB = 1/2 × 4 × 3 = 6 cm².",
               "Area of ΔABC = 18 − 6 = 12 cm², and 1/2 × 4 × 6 = 12 cm² too."],
              "12 cm², the same as 1/2 × base × height",
              ncert=["tri.obtuse"])],
       key_terms=["obtuse triangle", "height"], misconceptions=["M_OUTSIDE_HEIGHT"], minutes=8),
     DOER("T3.C4", "Practice: find base, height and area", "triangle_height_finder", "Apply",
          "Students pick a base and its perpendicular height in triangles, find areas, and give methods to change a "
          "rectangle into a triangle and a triangle into a rectangle of equal area.",
          ["Area of a triangle = 1/2 × base × height.",
           "The height is perpendicular to the chosen base, even when it falls outside the triangle.",
           "A rectangle and a triangle have equal areas when the triangle has twice the rectangle's height on the "
           "same base, or twice its base with the same height."],
          items=[
              FIO("FiO2.q1", U2 % 1,
                  "Find the areas of the following triangles: (i) base BC with 4 cm marked and height AE = 3 cm, "
                  "(ii) base EF = 5 cm with height DN = 3.2 cm, (iii) right triangle NAT with NA = 4 cm and AT = 3 cm.",
                  ["(i) 1/2 × 4 × 3 = 6 cm².", "(ii) The height DN is drawn to EF, so 1/2 × 5 × 3.2 = 8 cm².",
                   "(iii) The two legs are a base and its height: 1/2 × 3 × 4 = 6 cm²."],
                  "(i) 6 cm² (ii) 8 cm² (iii) 6 cm²"),
              FIO("FiO2.q3", U2 % 3,
                  "Find the area of ΔSUB, given that it is isosceles, SE is perpendicular to UB, and the area of ΔSEB "
                  "is 24 sq. units.",
                  ["In an isosceles triangle the perpendicular from S to UB meets it at its midpoint, so UE = EB.",
                   "ΔSUE and ΔSEB have the same base length and the same height SE, so equal areas.",
                   "Area of ΔSUB = 24 + 24 = 48 sq. units."],
                  "48 sq. units"),
              FIO("FiO2.q4", U2 % 4,
                  "[Śulba-Sūtras] Give a method to transform a rectangle into a triangle of equal area.",
                  ["Take rectangle ABCD with base AB and height BC.",
                   "Extend AB to E so that BE = AB. Then AE is twice the base.",
                   "Join E to D. Triangle AED has base 2 × AB and height AD, so its area is 1/2 × 2AB × AD = AB × AD.",
                   "Another way: cut the rectangle along a diagonal and place the two halves side by side along the "
                   "height to form one triangle."],
                  "A triangle on double the base with the same height (or double the height on the same base) has "
                  "the rectangle's area"),
              FIO("FiO2.q5", U2 % 5,
                  "[Śulba-Sūtras] Give a method to transform a triangle into a rectangle of equal area.",
                  ["Draw the height AX of triangle ABC on base BC.",
                   "Mark the midpoints of AB and AC and join them; this line is parallel to BC at half the height.",
                   "Drop perpendiculars from the two midpoints to BC. Cut off the two small top triangles and turn "
                   "each into the gap below it.",
                   "The result is a rectangle with base BC and height 1/2 AX, so its area is 1/2 × BC × AX."],
                  "Cut along the line joining the midpoints of the two sides and swing the top pieces down: a rectangle "
                  "on the same base with half the height")],
          misconceptions=["M_TRI_FULL", "M_SLANT_HEIGHT"])],
    key_terms=["triangle", "base", "height"]))

# ============================== T4 Using the triangle formula =================================================
TOPICS.append(TOPIC(
    "T4", "M1", "Using the Triangle Formula", ["Some Applications of the Area Formula",
                                                "Triangles between Parallel Lines with a Common Base"], "Analyze",
    "Students use two base and height pairs to find an altitude, show that diagonals and medians split area equally, "
    "compare triangles between parallel lines, and use a reflection to find the triangle with the shortest perimeter.",
    "One area, two base and height pairs gives a missing altitude; equal bases and equal heights give equal areas; and "
    "between parallel lines the area is fixed while the perimeter is smallest at the perpendicular bisector.",
    [A("T4.C1", "Finding an altitude from the area", "Apply",
       "Students compute a triangle's area from one base and height pair, then use a second base to find the "
       "missing altitude.",
       textbook=["Find BY.", "BY can be found using the formula for the area of a triangle.",
                 "What is Area (ΔABC)?", "Area (ΔABC) = 1/2 × AX × BC = 15/2 sq. units.",
                 "The area of the triangle can also be written as Area (ΔABC) = 1/2 × BY × AC = 1/2 × 4 × BY = 2 BY.",
                 "Thus, 2 BY = 15/2. So, BY = 15/4 = 3.75 units."],
       teach=["Predict first: we know AX = 3 on base BC = 5, and AC = 4. Can we find the height BY to AC without "
              "measuring it?",
              "The triangle has one area, however we measure it. Use the pair we know to get the area.",
              "Then write the same area with the base AC and the unknown height, and solve."],
       examples=[
           WE("In ΔABC, AX = 3 is the height to BC = 5, and AC = 4. Find the height BY to AC.",
              ["Area = 1/2 × 3 × 5 = 7.5 square units.", "Also, area = 1/2 × 4 × BY, which is 2 × BY.",
               "So 2 × BY = 7.5, and BY = 7.5 ÷ 2 = 3.75 units."],
              "BY = 3.75 units",
              ncert=["app.find_by"])],
       key_terms=["altitude", "base", "area"], minutes=8),
     A("T4.C2", "Diagonals and medians split area equally", "Analyze",
       "Students show that the four triangles made by a rectangle's diagonals have equal areas and that a median "
       "splits any triangle into two equal areas.",
       textbook=["Are the 4 triangles obtained by drawing the diagonals of a rectangle (regions 1 to 4 in the figure) "
                 "of equal areas?",
                 "Clearly, the triangles 1 to 4 are not four congruent triangles.",
                 "If OD and OB are taken as the bases, then we see that both triangles have the same altitude! We also "
                 "have OB = OD, since the diagonals of a rectangle bisect each other. So, the triangles 1 and 2 have "
                 "equal areas.",
                 "In a triangle, the line joining a vertex to the midpoint of its opposite side divides the triangle "
                 "into two triangles of equal areas."],
       teach=["Predict first: the diagonals cut a rectangle into two thin triangles and two fat ones. Are their areas "
              "equal?",
              "Triangles 1 and 2 sit on OD and OB, which are equal halves of a diagonal, and share the altitude from A.",
              "Equal base, equal height, equal area. The same reasoning shows a median halves any triangle."],
       examples=[
           WE("The diagonals of an 8 cm by 6 cm rectangle meet at O. Find the area of each of the four triangles.",
              ["The rectangle has area 8 × 6 = 48 cm².",
               "Adjacent triangles have equal halves of a diagonal as bases and the same height, so equal areas.",
               "All four are equal: 48 ÷ 4 = 12 cm²."],
              "Each triangle is 12 cm², even though they are not congruent",
              ncert=["app.diag_four", "app.median"])],
       key_terms=["diagonal", "median", "equal areas"], minutes=8,
       tool="median_splitter"),
     A("T4.C3", "Triangles between parallel lines", "Analyze",
       "Students compare triangles on a common base with the top vertex on a parallel line, showing equal areas but "
       "different perimeters.",
       textbook=["Line l ∥ BC. Consider the different triangles that have BC as their base, and with their third vertex "
                 "lying anywhere on l.",
                 "(i) Which of these triangles has the maximum area, and which has the minimum area?",
                 "(ii) Which of these triangles has the maximum perimeter, and which has the minimum perimeter?"],
       teach=["Predict first: as the top vertex slides along l, does the area grow, shrink or stay the same?",
              "Every triangle has base BC and the same height, the distance between the parallel lines.",
              "So all the areas are equal: there is no largest or smallest. The perimeter does change: it keeps "
              "growing as the vertex slides far away, so there is no largest perimeter, but there is a smallest."],
       examples=[
           WE("BC = 6 cm and line l is parallel to BC, 4 cm away. Find the area of a triangle on BC with its top on l, "
              "and say how it changes as the top moves.",
              ["Base = 6 cm, height = 4 cm for every position of the top.",
               "Area = 1/2 × 6 × 4 = 12 cm².",
               "Moving the top changes the slanting sides, not the height."],
              "Always 12 cm²: equal areas; only the perimeter changes",
              ncert=["app.parallel_area", "app.parallel_perim"])],
       key_terms=["parallel lines", "common base", "perimeter"], misconceptions=["M_TOP_VERTEX"], minutes=8),
     A("T4.C3x", "The shortest perimeter by reflection", "Evaluate",
       "Students reflect one end of the base in the parallel line to find the top vertex giving the smallest "
       "perimeter and justify that it lies on the perpendicular bisector.",
       textbook=["Intuition might suggest that the triangle with the minimum perimeter can be obtained by constructing "
                 "the perpendicular bisector of BC. But how do we justify that this triangle has the least perimeter "
                 "among all the triangles?",
                 "Let us imagine the line l as a mirror.",
                 "What can we say about the lengths of AB and its reflection AB′? Since ΔAXB ≅ ΔAXB′, AB = AB′.",
                 "So, finding point A that gives the shortest possible path B → A → C is the same as finding a point A "
                 "that gives the shortest possible path B → A → C′. Choose A on the straight line BC′.",
                 "Analyse whether A lies on the perpendicular bisector of BC."],
       teach=["Predict first: is the top vertex for the shortest perimeter right above the middle of BC?",
              "Reflect C in l to C′. Any path from A to C is as long as the path from A to C′.",
              "The shortest way from B to C′ is a straight line. Where it crosses l is the best A, and by symmetry "
              "it is halfway along, on the perpendicular bisector of BC."],
       examples=[
           WE("B and C are 3 cm below line l and BC = 8 cm. Find the smallest possible value of AB + AC with A on l.",
              ["Reflect C in l: C′ is 3 cm above l, so 6 cm above the line BC, directly over C.",
               "BC′ is the hypotenuse of a right triangle with legs 8 and 6: √(64 + 36) = √100 = 10.",
               "The straight line BC′ crosses l halfway across, above the midpoint of BC."],
              "The smallest AB + AC is 10 cm, with A on the perpendicular bisector of BC",
              ncert=["app.reflect", "app.mt_bisector"])],
       key_terms=["reflection", "perpendicular bisector", "shortest path"], minutes=8, thin=True),
     DOER("T4.C4", "Practice: slide the top vertex along a parallel line", "triangle_slider", "Analyze",
          "Students find altitudes from two base and height pairs, compare areas of regions in joined squares and "
          "midpoint triangles, and plan a shortest path by reflection.",
          ["The same area written with two different bases gives a missing altitude.",
           "Equal base and equal height mean equal area.",
           "Reflecting a point in a line turns a bent shortest path into a straight one."],
          items=[
              FIO("FiO2.q2", U2 % 2,
                  "Find the length of the altitude BY in ΔABC, where AX = 4 units is the height to BC = 6 units and "
                  "AC = 8 units.",
                  ["Area = 1/2 × 6 × 4 = 12 square units.", "Also area = 1/2 × 8 × BY, which is 4 × BY.",
                   "4 × BY = 12, so BY = 12 ÷ 4 = 3 units."],
                  "BY = 3 units"),
              FIO("FiO2.q6", U2 % 6,
                  "ABCD, BCEF and BFGH are identical squares, with H directly above B. The red region is the triangle "
                  "DCH and the blue region is the part of square ABCD to the left of the line DH. (i) If the area of the "
                  "red region is 49 sq. units, what is the area of the blue region? (ii) In another version, if the blue "
                  "and red regions together are 180 sq. units, what is the area of each square?",
                  ["Let each square have side s. Red: base DC = s, height CH = 2s, so area 1/2 × s × 2s, which is s².",
                   "DH rises 2s over a run of s, so it crosses AB at its midpoint: the blue triangle has legs s and s/2, "
                   "area one quarter of s².",
                   "(i) s² = 49, so blue = 49 ÷ 4 = 12.25 sq. units.",
                   "(ii) Blue + red is five quarters of s², so s² = 180 × 4 ÷ 5 = 144 sq. units."],
                  "(i) 12.25 sq. units (ii) 144 sq. units"),
              FIO("FiO2.q7", U2 % 7,
                  "If M and N are the midpoints of XY and XZ, what fraction of the area of ΔXYZ is the area of ΔXMN? "
                  "(Hint: join NY.)",
                  ["NY is a median of ΔXYZ (N is the midpoint of XZ), so ΔXNY is half of ΔXYZ.",
                   "In ΔXNY, NM is a median (M is the midpoint of XY), so ΔXMN is half of ΔXNY.",
                   "1/2 × 1/2 = 1/4."],
                  "ΔXMN is 1/4 of ΔXYZ"),
              FIO("FiO2.q8", U2 % 8,
                  "Gopal needs to carry water from the river to his water tank. He starts from his house. What is the "
                  "shortest path from his house to the river and then to the water tank? Recreate the map and trace it.",
                  ["Treat the river bank as a mirror line and reflect the water tank to the far side of it.",
                   "Join the house to the reflected tank with a straight line.",
                   "Where this line meets the river bank is the best point to fill water.",
                   "Walk house to that point, then to the real tank: this is as long as the straight line, the "
                   "shortest possible."],
                  "Reflect the tank in the river bank; the straight line from the house to the reflection meets the bank "
                  "at the best point")],
          misconceptions=["M_TOP_VERTEX"])],
    key_terms=["altitude", "median", "parallel lines"]))
