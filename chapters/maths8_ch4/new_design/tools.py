# -*- coding: utf-8 -*-
"""Tool specs for Class 8 Chapter 4 (Quadrilaterals). One tool per doer that has one, each used once.

Five are carried over from the live built tools of maths8_ch4_live_v22 (angle_sum_folder, sides_angles_lab,
diagonal_lab, hierarchy_sorter, quad_dragger; see live_tools.json and build.py's carry-over step): the spec for
those is only the local placeholder that build_tool_node needs; build.py replaces each node with a copy of the live
node (new id, concept_id and home_concept_id kept). The other five (carpenter_strips, square_in_square,
rhombus_hinge, kite_slider, trapezium_slider) are new spec tools, built as placeholders. The live Quad Polygraph is
not carried: it needs every family met, and its only fitting topic (The Quadrilateral Family) already holds the
hierarchy sorter."""
from topics_common import T

TOOLS = {
    "angle_sum_folder": T(
        "tool_angle_sum_folder", "Angle Sum Folder", "simulation",
        "The four angles of any quadrilateral fill a whole turn, 360°, not a straight angle: torn off and placed "
        "edge to edge they close up exactly, and a diagonal shows why, because it splits the quadrilateral into two "
        "triangles of 180° each.",
        "A lettered quadrilateral ABCD with each angle drawn as a coloured wedge of the same radius, a meeting point "
        "beside it, a running total, and a button that draws a diagonal and names the two triangles.",
        ["Predict whether the four angles will fill a straight angle or a whole turn.",
         "Tear a corner off and drag it to the meeting point.",
         "Place all four corners and read the total when the gap closes.",
         "Draw a diagonal and add the two triangle totals."],
        ["Place two corners and say why 180° is not the answer for a quadrilateral.",
         "Place all four corners of a slanted quadrilateral and read the total.",
         "Three angles are 90°: predict the fourth before placing it.",
         "Three angles are 75°, 95° and 110°: find the fourth.",
         "Draw a diagonal and show the six triangle angles make the four corners.",
         "Reshape the quadrilateral so that one corner caves in, and check the total again."],
        ["Two wedges leave a half-turn gap, so the triangle rule is seen to fall short.",
         "The gap closing exactly shows 360° without measuring.",
         "The diagonal lights the two triangles with 180° written in each."],
        "All six cards are done and the diagonal argument has been used on a reshaped quadrilateral.",
        ["angles", "placed", "total", "diagonal", "cardIndex"],
        ["M_ANGLE_SUM_180", "M_MEASURE_PROVES"],
        ["How many corners does a quadrilateral have, and what do they make when put together?",
         "Split the quadrilateral into two triangles with one diagonal.",
         "Two triangles give 180 + 180 = 360, so subtract the three known angles from 360.",
         "The missing angle is shown with the full turn, and a similar card follows."]),

    "sides_angles_lab": T(
        "tool_sides_angles_lab", "Sides And Angles Lab", "simulation",
        "In every parallelogram the next-door angles add up to 180° and the opposite angles are equal, and the "
        "opposite sides are equal; sweeping the shape inside its family keeps these marks while coincidences switch "
        "off.",
        "One lettered parallelogram with hatch ticks on equal sides, matching arcs on equal angles, arrowheads on "
        "parallel sides and a linking arc printing the sum of each next-door pair, a slider that sweeps the shape, "
        "and family presets.",
        ["Read the marks on the parallelogram.",
         "Sweep the shape and watch which marks never go out.",
         "Switch the preset to rectangle, rhombus or square and see which marks are added.",
         "Answer a card by naming the equal pair and the pair that adds to 180°."],
        ["One angle is 30°: find the other three angles.",
         "Sides 4 cm and 5 cm: find the other two sides.",
         "Sweep the shape and say which two angles stay equal.",
         "Find a position where the diagonals look equal, then sweep on and see the mark switch off.",
         "Switch to the rhombus preset and name the mark it adds.",
         "One angle is x: write the other three angles."],
        ["A pair of next-door angles called equal is shown with its linking arc printing a sum of 180°.",
         "A coincidence is drawn dashed and captioned 'at this value only'.",
         "A forced mark never flickers during the sweep."],
        "All six cards are done and every forced mark has survived a full sweep.",
        ["shape", "family", "marks", "cardIndex"],
        ["M_ADJ_EQUAL", "M_DIAG_EQUAL_ALL", "M_MEASURE_PROVES"],
        ["Which two angles sit between the same pair of parallel sides?",
         "Next-door angles add up to 180°; opposite angles are equal.",
         "If one angle is 30°, its neighbours are 180 − 30 = 150 and the opposite angle is 30.",
         "The angles are shown with their arcs, and a similar card follows."]),

    "diagonal_lab": T(
        "tool_diagonal_lab", "Diagonal Lab", "simulation",
        "The diagonals decide the quadrilateral: diagonals that bisect each other give a parallelogram, equal ones a "
        "rectangle, perpendicular ones a rhombus, and all three together a square.",
        "Two crossing segments AC and BD meeting at O, with tick marks for halves, a right-angle mark at O, live "
        "lengths and angle, three conditions (bisect, equal, perpendicular) and the set of families they guarantee.",
        ["Drag the ends of the diagonals or slide the crossing point.",
         "Read which conditions hold.",
         "Name the families before showing the outline.",
         "Set a target family and change one condition to reach it."],
        ["Make equal diagonals that bisect each other and name the figure.",
         "Make the diagonals meet at right angles as well and name the figure again.",
         "Lengthen one diagonal by 2 cm at each end and name the new figure.",
         "Make diagonals 7 cm and 5 cm that bisect each other at 140°.",
         "Make a kite: perpendicular diagonals, only one of them bisected.",
         "Join two equilateral triangles of side 4 cm and read the diagonals of the rhombus."],
        ["A single name for a square is answered with all the families it belongs to.",
         "A condition that fails is struck through with the measurement that broke it.",
         "The outline appears only after a name is chosen."],
        "All six cards are done with every family named from the diagonals before the outline is shown.",
        ["A", "B", "C", "D", "O", "conditions", "cardIndex"],
        ["M_DIAG_PERP_RHOMBUS", "M_ONE_NAME", "M_DIAG_EQUAL_ALL"],
        ["What do the two diagonals do: bisect, match in length, meet at right angles?",
         "Bisecting gives a parallelogram; add equal for a rectangle, perpendicular for a rhombus.",
         "Equal, bisecting and perpendicular together give a square, which is also a rectangle and a rhombus.",
         "The families are listed with the conditions, and a similar card follows."]),

    "hierarchy_sorter": T(
        "tool_hierarchy_sorter", "Quad Hierarchy Sorter", "simulation",
        "The families sit inside one another: every square is a rectangle and a rhombus, every rectangle and rhombus "
        "is a parallelogram, and a figure belongs to every ring whose conditions it meets.",
        "Nested rings, Quadrilaterals holding Parallelograms, which hold overlapping Rectangles and Rhombuses with "
        "Squares in the overlap, and a tray of figure cards whose sides, angles and diagonals are measured.",
        ["Pick a figure card and read its measurements.",
         "Drop it on the innermost ring it belongs to.",
         "Read the reason when a card bounces back.",
         "Build a figure of your own and see which rings it reaches."],
        ["Place a square in its innermost ring and count the rings around it.",
         "Place a rhombus with angles 72° and 108°.",
         "Place a parallelogram that is neither a rectangle nor a rhombus.",
         "Decide whether any figure is both a kite and a parallelogram.",
         "Place a figure with four equal sides and one right angle.",
         "Place a figure whose opposite sides are equal."],
        ["A card that could go further in is accepted as true but incomplete.",
         "A card dropped on a wrong ring returns with the condition it failed.",
         "Counts in each ring fill from the outside in."],
        "All six cards are placed in their innermost rings.",
        ["rings", "cards", "placed", "cardIndex"],
        ["M_SQUARE_NOT_RECT", "M_ONE_NAME", "M_KITE_RHOMBUS"],
        ["Which conditions does this figure meet?",
         "Start at the outer ring and move in while every condition still holds.",
         "Four right angles and four equal sides: rectangle and rhombus, so the overlap, squares.",
         "The card is placed with its reasons, and a similar card follows."]),

    "carpenter_strips": T(
        "tool_crossing_strips", "Crossing Strips", "manipulative",
        "Two strips joined at their midpoints make a rectangle when they are equal, whatever angle they cross at: the "
        "angle changes the shape of the rectangle but never its corners. Unequal strips, or a joint off the middle, "
        "break it.",
        "Two strips AC and BD crossing at O with a length slider for each strip, a slider that slides the joint along "
        "a strip, a slider for the crossing angle, a thread round the four ends, and live read-outs of the four "
        "corner angles and the four side lengths.",
        ["Predict whether the thread will make a rectangle before moving anything.",
         "Set the lengths, the joint and the crossing angle.",
         "Read the four corners and the four sides.",
         "Change one thing at a time and see which change breaks the rectangle."],
        ["The strip AC is 8 cm: set the other strip so that the thread makes a rectangle.",
         "Cross two equal 8 cm strips at 60° and read the four corners.",
         "Cross two equal 8 cm strips at 140° and predict the four corners before reading them.",
         "Cross two equal 8 cm strips at 90° and read the four sides.",
         "Make the strips 8 cm and 6 cm, joined at their midpoints, and say whether any angle gives a rectangle.",
         "Slide the joint of one equal strip off its middle and say what happens to the corners."],
        ["Equal strips joined at their midpoints show every corner as 90°, and the sides change as the angle "
         "changes.",
         "Unequal strips show the corners that are not 90° with their values, so the failure is seen.",
         "A joint off the middle marks the two halves of the strip that are not equal."],
        "All six cards are done and the rectangle has been made at three different crossing angles.",
        ["lengthAC", "lengthBD", "jointAC", "jointBD", "crossingAngle", "cardIndex"],
        ["M_MEASURE_PROVES", "M_SQUARE_NOT_RECT"],
        ["What must be true of the two strips and of where they are joined?",
         "Make the strips equal and join them at their midpoints, then try different crossing angles.",
         "With equal strips of 8 cm joined at their midpoints, every corner is 90° at 60°, at 140° and at any angle.",
         "The strips are shown equal and joined at their midpoints, the rectangle is drawn, and a similar card "
         "follows."]),

    "square_in_square": T(
        "tool_square_in_square", "Square in a Square", "manipulative",
        "Marking the same distance from each corner of a square, always going the same way round, joins up into "
        "another square. The four corner triangles are equal right triangles, so each corner of the inner figure is "
        "90°, and the midpoints are only one special case.",
        "A square CASE of side 8 cm with one point on each side, a slider for the distance from the corner, a "
        "snap to the midpoints, the inner figure shaded, and live read-outs of its sides, its angles and its area. "
        "Each point can also be dragged alone.",
        ["Predict the inner figure before moving the slider.",
         "Slide the distance and watch the inner figure.",
         "Read its sides, its angles and its area.",
         "Drag one point alone and see what the inner figure becomes."],
        ["Snap the points to the midpoints and name the inner figure.",
         "Set the distance to 2 cm and read the side and the area of the inner figure.",
         "Find the distance that makes the inner area exactly 32 square centimetres.",
         "Find another distance that gives the same inner square as 2 cm.",
         "At the midpoints, read the two acute angles of a corner triangle and the angle of the inner figure.",
         "Drag a single point off its place and say whether the inner figure is still a square."],
        ["A square inner figure is shown with equal sides and four right angles marked.",
         "A wrong prediction shows the corner triangles side by side so the equal triangles are seen.",
         "A single point moved alone turns the inner figure into a shape with unequal sides, and the right angles "
         "go out."],
        "All six cards are done and the inner square has been made at three different distances.",
        ["distance", "points", "innerSide", "innerArea", "cardIndex"],
        ["M_MEASURE_PROVES", "M_SQUARE_NOT_RECT"],
        ["Which four points are marked, and how far is each one from its corner?",
         "Look at the four corner triangles: are they equal, and what are their acute angles?",
         "The two acute angles of a corner triangle add up to 90°, so the angle left on the straight line is 180° − 90° "
         "= 90°.",
         "The inner figure is shown as a square with its corner triangles marked, and a similar card follows."]),

    "rhombus_hinge": T(
        "tool_rhombus_hinge", "Rhombus Hinge", "manipulative",
        "Four equal rods hinged at the corners make a rhombus that changes shape as the hinge opens, but opposite "
        "angles stay equal, neighbouring angles stay at 180°, and the diagonals always bisect each other at 90° and "
        "bisect the corners. Only at 90° do the diagonals become equal, and the rhombus becomes a square.",
        "A rhombus ABCD with four equal rods, a handle that opens the angle at A, both diagonals meeting at O with a "
        "right angle mark, live read-outs of the four corners and of the angles the diagonal makes at each corner, "
        "and a diagonal mode with a slider for each diagonal.",
        ["Predict which marks stay while the hinge opens.",
         "Open and close the hinge and watch the angles and the diagonals.",
         "Switch to diagonal mode and set the two diagonals.",
         "Read the side that the diagonals force."],
        ["Open the hinge to 50° and read the other three angles.",
         "Set the diagonal angle at V of rhombus UVWX to 30° and read all four angles.",
         "Set the diagonals to 5 cm and 4 cm and read the side.",
         "Set the diagonals to 8 cm and 6 cm and read the side and the perimeter.",
         "Open the hinge to a square and say what happens to the diagonals.",
         "Sweep the hinge and look for an angle other than 90° at which the diagonals are equal."],
        ["Equal opposite angles and 180° neighbouring pairs stay marked as the hinge opens.",
         "The right angle mark at O never goes out, while the diagonal lengths change.",
         "The diagonals are shown equal only at 90°, and a coincidence is drawn dashed."],
        "All six cards are done and the diagonals have been shown perpendicular at every opening of the hinge.",
        ["hingeAngle", "diagonalAC", "diagonalBD", "side", "cardIndex"],
        ["M_DIAG_EQUAL_ALL", "M_DIAG_PERP_RHOMBUS", "M_SQUARE_NOT_RECT"],
        ["What stays the same while the hinge opens: the rods, the angles or the diagonals?",
         "The diagonals bisect each other at 90° and bisect the corners, so each corner is twice the angle the "
         "diagonal makes.",
         "A diagonal angle of 30° gives a corner of 30° + 30° = 60°, and the neighbouring corner is 180° − 60° = 120°.",
         "The corners are shown with their working, and a similar card follows."]),

    "kite_slider": T(
        "tool_kite_slider", "Kite Slider", "manipulative",
        "Fix one diagonal AC and slide the points B and D along the line that cuts AC in half at right angles: every "
        "position gives a kite. The diagonal BD always cuts AC in half at 90°, but AC cuts BD in half only when B and "
        "D are the same distance from it, which gives a rhombus.",
        "A diagonal AC with its midpoint O, the line through O at right angles to AC, two draggable points B and D on "
        "that line, a thread round A, B, C and D, hatch marks on equal sides, a right angle mark at O, and live "
        "read-outs of the four sides, of OB and OD, and of the angles at B and D.",
        ["Predict which sides will stay equal when B and D slide.",
         "Slide B and D and read the four sides.",
         "Check which diagonal cuts which in half.",
         "Set B and D the same distance from AC and name the new figure."],
        ["Make a kite with AC = 6 cm, OB = 2 cm and OD = 6 cm, and read its four sides.",
         "Keep BD = 8 cm and slide the split through 3 and 5, then 1 and 7, and say what stays the same.",
         "Say whether AC cuts BD in half, and whether BD cuts AC in half.",
         "Set OB = OD = 4 cm with AC = 6 cm and name the figure, then read its side.",
         "Set OB = OD = 3 cm with AC = 6 cm and name every figure it is."],
        ["Equal neighbouring sides are marked as B and D slide, so the kite is seen to hold.",
         "A kite with B and D at the same distance from AC is named as a rhombus too, with all four sides marked "
         "equal.",
         "The right angle mark at O never goes out as the points slide."],
        "All five cards are done and the kite has been shown at three different positions of B and D.",
        ["pointB", "pointD", "lengthAC", "sides", "cardIndex"],
        ["M_KITE_RHOMBUS", "M_DIAG_PERP_RHOMBUS"],
        ["Which diagonal stays fixed, and which line do B and D slide along?",
         "B and D sit on the line that cuts AC in half at right angles, so each is the same distance from A and from C.",
         "With AC = 6 cm, OB = 2 cm and OD = 6 cm, AB = BC and AD = CD, so the kite has two pairs of equal sides.",
         "The sides are shown with their working, and a similar card follows."]),

    "trapezium_slider": T(
        "tool_trapezium_slider", "Trapezium Slider", "manipulative",
        "Between two parallel lines each slanting side is a transversal, so the two angles along it add up to 180°. "
        "Making the slanting sides equal gives equal base angles, and sliding the top side until the slanting sides "
        "are parallel makes a parallelogram, which is also a trapezium.",
        "Two parallel lines carrying the sides PQ and SR of a trapezium, handles that slide the top side along its "
        "line and tilt the slanting sides, an equal slanting sides lock, live read-outs of the four angles with a "
        "linking arc printing the sum along each slanting side, and a running angle total.",
        ["Predict the two top angles from the two base angles.",
         "Slide the top side and tilt the slanting sides.",
         "Switch on the equal slanting sides lock and see which angles match.",
         "Slide until the slanting sides are parallel and name every figure it is."],
        ["Set the base angles to 70° and 55° and predict the two top angles.",
         "Set two angles of 105° and 135° at the ends of one parallel side and find the other two.",
         "Switch on the lock, set one angle to 100° and read all four angles.",
         "Switch on the lock and set the base angles to 65°: find the top angles.",
         "Slide the top side until the base angles are 70° and 110° and name every figure it is.",
         "Add the four angles of the 70° and 55° trapezium and compare the total with 360°."],
        ["A wrong prediction shows the linking arc with 180° along the slanting side and the missing angle.",
         "The lock makes the angles at the ends of one parallel side equal, and the other two equal too.",
         "A parallelogram is named as a trapezium as well, so the second name is not lost."],
        "All six cards are done and a parallelogram has been made from a trapezium and named as both.",
        ["baseAngleP", "baseAngleQ", "lock", "topAngles", "cardIndex"],
        ["M_TRAP_EXACTLY_ONE", "M_ANGLE_SUM_180"],
        ["Which sides are parallel, and which sides are the slanting ones?",
         "A slanting side is a transversal to the parallel sides, so the two angles along it add up to 180°.",
         "With 70° at P, the angle at S along the same slanting side is 180° − 70° = 110°.",
         "The angles are shown with the 180° arcs, and a similar card follows."]),

    "quad_dragger": T(
        "tool_quad_dragger", "Quad Dragger", "simulation",
        "A property that holds in the drawn position is not the same as a property the construction forces: dragging "
        "keeps the properties a figure is built with and switches off the ones that held only by coincidence.",
        "A quadrilateral on squared paper with four draggable corners, eight statements with live ticks, a badge for "
        "each saying whether the construction keeps it, and readouts of sides, angles and both diagonals.",
        ["Say which statements you expect to stay true while dragging.",
         "Drag a corner and watch which ticks stay lit.",
         "Name the first tick that goes out.",
         "Say why a surviving statement cannot be broken."],
        ["Read the eight statements on a parallelogram and say which four will never go out.",
         "Drag to the position where it looks like a rectangle, then drag on and name the ticks that go out.",
         "Count the statements a rectangle keeps through every drag.",
         "Lock one side length and see how much of the figure is still free.",
         "Put the same eight statements to a free quadrilateral and say how many are kept.",
         "Say why a statement that survived many drags cannot be broken."],
        ["A statement a drag switches off is struck through with the position that broke it.",
         "A kept statement never flickers while the lengths change.",
         "A free quadrilateral keeps none of the statements."],
        "All six cards are done and every kept statement has been explained from the construction.",
        ["vertices", "ticks", "kept", "locked", "cardIndex"],
        ["M_MEASURE_PROVES", "M_DIAG_EQUAL_ALL", "M_RIGHT_ANGLES_ONLY"],
        ["Which statements are about how the figure is built, and which about how it looks now?",
         "Drag a corner and see which ticks never go out.",
         "Equal diagonals and four right angles go out at the next drag, so the construction did not force them.",
         "The kept statements are shown with their reasons, and a similar card follows."]),
}
