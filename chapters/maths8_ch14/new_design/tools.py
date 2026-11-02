# -*- coding: utf-8 -*-
"""Tool specs for Class 8 Chapter 14 (Area). A tool appears only where moving the shape is the idea itself;
nine tools, none carried over from an earlier plan, each used once. Eight sit in the practice concept of their
topic and one (the median splitter) sits in a teaching concept whose idea is a manipulation of its own."""
from topics_common import T

TOOLS = {
    "rectangle_stretcher": T(
        "tool_rectangle_stretcher", "Rectangle Stretcher: Area or Perimeter", "manipulative",
        "Area counts unit squares inside a shape, perimeter measures its boundary. Two rectangles can share a "
        "perimeter and have different areas, and a rectangle with a longer boundary can still cover fewer squares.",
        "A square grid with a rectangle whose right and top edges can be dragged, live readouts of length, width, "
        "area and perimeter, and a second ghost rectangle to compare against.",
        ["Predict which of the two rectangles covers more squares before counting.",
         "Drag the edges and watch the area and perimeter readouts change separately.",
         "Keep the perimeter fixed and stretch the rectangle into a thin strip.",
         "Find a rectangle with a bigger perimeter but a smaller area than the ghost."],
        ["A 7 by 4 rectangle and an 8 by 3 rectangle: which needs more rangoli powder?",
         "Keep the perimeter at 20 and find the rectangle with the largest area.",
         "Keep the perimeter at 20 and make the area as small as you can.",
         "Make a rectangle with a larger perimeter than a 5 by 4 rectangle but a smaller area.",
         "A rectangle has area 21 and one side 7: drag the other side to fit.",
         "Draw the diagonal of a 7 by 4 rectangle and count the squares in one triangle."],
        ["A wrong guess shows both unit square counts side by side.",
         "When the perimeter is held, the area readout turns red as the strip gets thinner.",
         "A missing side is checked by multiplying back to the given area."],
        "All six cards are done and the student has shown one pair where the longer boundary has less area.",
        ["length", "width", "area", "perimeter", "ghostLength", "ghostWidth", "lockPerimeter", "cardIndex"],
        ["M_PERIM_AREA", "M_SCALE_AREA"],
        ["What does area count, and what does perimeter measure?",
         "Count the unit squares inside, then walk around the edge and add the sides.",
         "For a 10 by 1 strip the perimeter is 22 but the area is only 10; compare with 5 by 4.",
         "The pair is shown with both counts and a similar card follows."]),

    "triangle_slider": T(
        "tool_triangle_slider", "Triangle Slider: Parallel Lines", "manipulative",
        "Triangles on the same base whose top vertex lies on a line parallel to the base all have the same height, "
        "so the same area. Their perimeters differ, and the smallest perimeter comes when the top vertex sits on the "
        "perpendicular bisector of the base, found by reflecting one end of the base in the line.",
        "A base BC on a grid, a line l parallel to it, a draggable top vertex A on l, live readouts of base, height, "
        "area and perimeter, and a Reflect button that draws the mirror image of C in l.",
        ["Predict whether the area will change as A slides along l.",
         "Drag A and watch the area stay fixed while the perimeter changes.",
         "Press Reflect and draw the straight path from B to the image of C.",
         "Place A where that straight path crosses l and read the perimeter."],
        ["Base 6, height 4: slide A and record the area at three places.",
         "Where on l is the perimeter the largest that you can find?",
         "Use the reflection to place A for the smallest perimeter.",
         "Check that the smallest perimeter triangle has AB equal to AC.",
         "Change the height to 3 and predict the new area before sliding.",
         "Find the altitude from B when AX is 3, BC is 5 and AC is 4."],
        ["If the student predicts a change in area, the height bar is highlighted as unchanged.",
         "The perimeter readout leaves a trail so the lowest value can be seen.",
         "The reflected path is drawn in a second colour and its length is shown."],
        "All six cards are done and A has been placed at the smallest perimeter position.",
        ["baseB", "baseC", "lineHeight", "apexX", "area", "perimeter", "reflected", "cardIndex"],
        ["M_TOP_VERTEX", "M_SLANT_HEIGHT"],
        ["Which two measurements does the area of a triangle depend on?",
         "Is the distance from A to the base changing as A slides along l?",
         "Reflect C in l; the straight line from B to the image crosses l at the best A.",
         "The best A is shown on the perpendicular bisector of BC and a new card follows."]),

    "parallelogram_cutter": T(
        "tool_parallelogram_cutter", "Parallelogram Cutter: Cut and Slide", "manipulative",
        "Cutting a right triangle off one end of a parallelogram along a height and sliding it to the other end makes "
        "a rectangle with the same base and height, so the area of a parallelogram is base times height, using any "
        "side as base with its own perpendicular height.",
        "A parallelogram on a grid with a draggable cut line that stays perpendicular to the chosen base, a triangle "
        "piece that can be slid across, readouts of base, height, slanting side and area, and a Change base button.",
        ["Predict whether the rectangle will have the same area as the parallelogram.",
         "Drag the cut line to a vertex and cut off the right triangle.",
         "Slide the triangle to the far side and watch it fit exactly.",
         "Change the base to the other side and repeat with its height."],
        ["Base 7, height 4: cut, slide and read the area.",
         "Base 5, height 3: is the slanting side used anywhere?",
         "Make three different parallelograms on the same base and height and compare their areas.",
         "A rectangle and a parallelogram both have sides 5 and 4: which is bigger?",
         "Sides 12 and 7.6, height 6 on the side 12: find the height on the other side.",
         "Use the other side as base and cut again."],
        ["A cut that is not perpendicular is refused with a right angle marker shown.",
         "When the triangle fits, the rectangle outline lights up with its area.",
         "Using a slanting side as the height shows the two areas disagreeing."],
        "All six cards are done and the student has cut along two different bases.",
        ["base", "height", "side", "cutX", "slid", "baseChoice", "cardIndex"],
        ["M_SLANT_HEIGHT", "M_RECT_PARA"],
        ["What shape do you get if the slanting ends become upright?",
         "Cut along a height so the piece is a right triangle.",
         "The rectangle has the same base and the same height, so multiply them.",
         "The cut and slide is shown with the area and a similar card follows."]),

    "trapezium_joiner": T(
        "tool_trapezium_joiner", "Trapezium Joiner: Two Copies", "manipulative",
        "Two copies of a trapezium, one turned half way round and joined along a slanting side, make a parallelogram "
        "whose base is the sum of the parallel sides and whose height is the trapezium's height, so the trapezium is "
        "half of it: one half times height times the sum of the parallel sides.",
        "A trapezium with editable parallel sides a and b and height h, a Copy button, a rotate handle, snapping when "
        "a slanting side meets its twin, and readouts of the parallelogram base, height and area.",
        ["Predict what shape two copies will make when joined.",
         "Copy the trapezium, turn the copy and snap it to a slanting side.",
         "Read the base of the new parallelogram and compare with a plus b.",
         "Halve the parallelogram's area to get the trapezium's area."],
        ["Parallel sides 7 and 11, height 6: join and find the area.",
         "Parallel sides 24 and 36, height 14: predict the parallelogram base first.",
         "Change only the height and watch the area change.",
         "Make a trapezium with area 144.",
         "Turn a slanting trapezium (both slants leaning the same way) into a parallelogram too.",
         "Break the trapezium into a rectangle and two triangles instead and compare."],
        ["A copy joined without turning shows a six sided figure and a hint to rotate.",
         "When the copies snap, the long base is labelled a + b.",
         "A result that forgets the half is shown next to the parallelogram's area."],
        "All six cards are done and the student has stated the half of base times height rule.",
        ["a", "b", "h", "copied", "rotation", "snapped", "area", "cardIndex"],
        ["M_TRAP_ONE_SIDE", "M_SLANT_HEIGHT"],
        ["What shape has opposite sides parallel and an easy area?",
         "Turn the copy so its long side lines up with the short side of the first.",
         "The base becomes a + b and the height stays h, so the parallelogram is (a + b) × h.",
         "The joined parallelogram and its half are shown and a similar card follows."]),

    "triangle_height_finder": T(
        "tool_triangle_height_finder", "Triangle Height Finder: Pick a Base", "manipulative",
        "Any side of a triangle can be the base. Its height is the perpendicular distance from the opposite corner to "
        "the line of that base, which falls inside an acute triangle and outside an obtuse one, and 1/2 × base × height "
        "gives the same area for every choice. The slanting side is never the height.",
        "A triangle on a grid with draggable corners, a tap on any side to make it the base, a dashed perpendicular "
        "with a right angle marker (the base line is extended when the foot falls outside), live readouts of base, "
        "height and half base times height, and a switch that draws the enclosing rectangle.",
        ["Predict which segment is the height before it is drawn.",
         "Tap a side to make it the base and watch the perpendicular move.",
         "Drag the top corner until the height falls outside the triangle.",
         "Choose a second base on the same triangle and compare the two areas."],
        ["Base 8 and height 5: read the area.",
         "A triangle with base 5, slanting side 6 and height 4: which number goes in the area?",
         "A right triangle with sides 6, 8 and 10: use the side 10 as base, where the height is 4.8.",
         "Make the height fall outside a triangle with base 6 and height 4 and read its area.",
         "A triangle has area 30 with base 10 and height 6: find the height when the base is 12.",
         "Build a triangle of area 24 on a base of 8."],
        ["A slanting side used as height shows the larger, wrong area next to the true one.",
         "When the foot falls outside, the base line is extended with a dotted line and the height stays square to it.",
         "Two bases on one triangle show the two products side by side and they agree."],
        "All six cards are done and the student has seen a height outside a triangle and used two bases on one triangle.",
        ["baseChoice", "cornerA", "cornerB", "cornerC", "height", "area", "showRectangle", "cardIndex"],
        ["M_TRI_FULL", "M_SLANT_HEIGHT", "M_OUTSIDE_HEIGHT"],
        ["Which side is the base, and which corner is opposite to it?",
         "The height meets the base line at a right angle; extend the base line if it has to.",
         "Take 1/2 × 8 × 5 and compare it with the area readout.",
         "The area is 1/2 × 8 × 5 = 20 square units and a similar card follows."]),

    "median_splitter": T(
        "tool_median_splitter", "Median Splitter: Equal Areas", "manipulative",
        "A line from a corner of a triangle to the midpoint of the opposite side makes two triangles with equal bases "
        "and the same height, so equal areas, though the pieces need not match in shape. The same reasoning splits a "
        "rectangle into four triangles of equal area at the meeting point of its diagonals.",
        "A triangle on a grid with a point D that slides along the base BC, a midpoint marker, live area readouts of "
        "the two parts shown as bars, a corner that can slide along a parallel line, and a rectangle mode with both "
        "diagonals and the four triangles shaded.",
        ["Predict where D must sit for the two parts to be equal.",
         "Slide D along BC and watch the two area bars.",
         "Slide the top corner along the parallel line with D at the midpoint.",
         "Switch to the rectangle and read the four triangle areas."],
        ["BC is 10 and the height is 6: place D so the two parts have equal areas.",
         "Put D at 4 from B and read the two areas.",
         "Place D so that the part on the left is a quarter of the triangle.",
         "A rectangle 8 by 6 with both diagonals: find the area of each of the four triangles.",
         "Keep D at the midpoint and slide the top corner along the parallel line: do the two areas stay equal?",
         "BC is 12 and the height is 5: find BD so that the left part has area 10."],
        ["The two bars level out and turn green when D reaches the midpoint.",
         "Two parts of equal area that differ in shape are shown side by side with their bases and the shared height.",
         "A wrong placement shows both areas as half base times height with the same height."],
        "All six cards are done and the student has found D for equal areas in the triangle and the rectangle.",
        ["pointD", "baseBC", "height", "topCornerX", "mode", "areaLeft", "areaRight", "cardIndex"],
        ["M_EQUAL_SHAPE", "M_TOP_VERTEX"],
        ["Which two bases do the two parts stand on, and what height do they share?",
         "Equal heights mean the areas are equal exactly when the bases are equal.",
         "With BC = 10 and height 6, the left part is 1/2 × BD × 6; set it equal to 15.",
         "D sits at 5 from B, so each part is 1/2 × 5 × 6 = 15 and a similar card follows."]),

    "polygon_splitter": T(
        "tool_polygon_splitter", "Polygon Splitter: Parts or Cut Out", "manipulative",
        "The area of a polygon on a grid comes from splitting it into triangles and rectangles whose areas add, or "
        "from enclosing it in a rectangle and taking the corner pieces away, and both routes give the same area.",
        "A grid with a polygon whose corners sit on grid points, split lines drawn corner to corner with each part's "
        "area shown, and an enclosing rectangle with the corner pieces that can be lifted off one at a time.",
        ["Choose a route before drawing anything.",
         "Draw split lines and read each part's area as it is marked.",
         "Draw the enclosing rectangle and lift off each corner piece.",
         "Compare the two totals and say why they agree."],
        ["A quadrilateral with a diagonal of 14 and a height of 4 on one side and 2 on the other: split and add.",
         "A house shaped pentagon: a 6 by 4 rectangle with a triangle of height 3 on the side of 6.",
         "A figure inside a 10 by 6 rectangle with two corner triangles removed, each with legs 4 and 3.",
         "An 8 by 5 rectangle with a 2 by 2 notch cut out of one edge.",
         "A quadrilateral with a diagonal of 12 and heights of 5 and 3 on either side.",
         "A figure inside a 12 by 9 rectangle with two corner triangles removed, each with legs 6 and 3: use both "
         "routes and compare."],
        ["A split that leaves a gap or an overlap shades the squares that are wrong.",
         "Each part carries its own area as it is marked.",
         "When the two routes agree the matching totals are shown side by side."],
        "All six cards are done and the student has used both routes on one figure.",
        ["corners", "splitLines", "enclosingRectangle", "removedPieces", "cardIndex"],
        [],
        ["Which route would you try first, splitting or cutting out of a rectangle?",
         "Split into pieces whose areas you can find, or enclose the figure and take away the corners.",
         "For the quadrilateral with diagonal 14, find the two triangle areas from the diagonal and its heights.",
         "The two triangles are 1/2 × 14 × 4 = 28 and 1/2 × 14 × 2 = 14, so the area is 42 square units and a similar card follows."]),

    "rhombus_dissector": T(
        "tool_rhombus_dissector", "Rhombus Dissector: Diagonals to Rectangle", "manipulative",
        "Cutting a rhombus along both diagonals gives four right triangles that rearrange into a rectangle as long "
        "as one diagonal and as wide as half the other, so the area is 1/2 × d1 × d2. The full product of the "
        "diagonals is the rectangle drawn round the rhombus, which has twice the area.",
        "A rhombus with a draggable handle on each diagonal (the diagonals stay at right angles and cross at their "
        "midpoints), a Cut button, four pieces that can be dragged into a rectangle outline, a switch that draws the "
        "rectangle round the rhombus, and readouts of d1, d2, the side and the area.",
        ["Predict what the pieces will make before cutting.",
         "Cut along both diagonals and drag the four triangles into a rectangle.",
         "Read the sides of the rectangle in terms of the diagonals.",
         "Switch on the rectangle round the rhombus and compare the two areas."],
        ["Diagonals 12 and 8: cut, rearrange and read the area.",
         "Diagonals 10 and 6: find the area.",
         "Diagonals 16 and 30: find the area.",
         "One diagonal is 12 and the area is 60: find the other diagonal.",
         "Diagonals 6 and 8: find the area and the length of a side.",
         "Make a different rhombus with area 48."],
        ["Pieces that do not fit leave a gap, and the gap is shaded.",
         "When the four pieces fit, the rectangle lights up with its two sides marked.",
         "The full product of the diagonals is shown as the outer rectangle, twice the area of the rhombus."],
        "All six cards are done and the student has compared the rhombus with the rectangle round it.",
        ["d1", "d2", "cut", "piecePositions", "showOuterRectangle", "area", "cardIndex"],
        ["M_RHOMBUS_DIAG"],
        ["What shapes do the two diagonals cut the rhombus into?",
         "Fit the four triangles into a rectangle; one side is a whole diagonal, the other half of the other.",
         "For diagonals 12 and 8 the rectangle is 12 by 4, so multiply those two sides.",
         "The area is 12 × 4 = 48 square units, which is 1/2 × 12 × 8, and a similar card follows."]),

    "square_unit_scaler": T(
        "tool_square_unit_scaler", "Square Unit Scaler: Side and Area", "manipulative",
        "When one unit is k times as long as another, a square of the larger unit holds k × k squares of the smaller, so a "
        "square unit converts by the length factor multiplied by itself: 1 square foot is 12 × 12 = 144 square inches, "
        "and 1 square inch is 2.54 × 2.54 = 6.4516 square centimetres (a factor that is not whole leaves partial "
        "squares and strips in the tiling).",
        "A unit square that can be tiled by smaller squares, a unit pair chosen from metre and centimetre, foot and "
        "inch, inch and centimetre, kilometre and metre, a live readout of the length factor and the area factor, and "
        "a converter row that turns a given area from one unit to the other.",
        ["Predict the area factor before the square is tiled.",
         "Choose a unit pair and watch the side split into equal parts.",
         "Count the small squares by rows and compare with the length factor.",
         "Convert a given area using the area factor."],
        ["1 square foot in square inches.",
         "1 square metre in square centimetres.",
         "1 square inch in square centimetres: show why it is not 2.54.",
         "1 square kilometre in square metres.",
         "Convert 12.9032 square centimetres into square inches.",
         "Convert a room of 20 square metres into square centimetres."],
        ["The tiling is shown with the rows and columns counted, so the area factor is seen as rows times columns.",
         "A student who uses the length factor for the area gets a tiling that visibly does not fit.",
         "A correct conversion shows the factor used and the converted area."],
        "All six cards are done and the student has explained why the area factor is the length factor twice.",
        ["unitPair", "lengthFactor", "areaFactor", "givenArea", "convertedArea", "cardIndex"],
        ["M_UNIT_SQUARE", "M_SCALE_AREA"],
        ["How many small squares fit along one side, and how many rows are there?",
         "The area factor is the length factor times itself, because the squares fill rows and columns.",
         "For feet and inches the length factor is 12, so multiply 12 by 12.",
         "1 square foot is 12 × 12 = 144 square inches, and a similar card follows."]),
}
