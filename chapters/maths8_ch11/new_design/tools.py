# -*- coding: utf-8 -*-
"""Tool specs for Class 8 Chapter 11 (Exploring Some Geometric Themes). A tool only where handling the shape is
the idea itself; each tool is used once, on one practice concept."""
from topics_common import T

TOOLS = {
    "fractal_stepper": T(
        "tool_fractal_stepper", "Fractal Stepper: Grow the Carpet", "manipulative",
        "A fractal grows by repeating one rule. In the Sierpinski Carpet every remaining square splits into 9 and loses "
        "its centre, so the remaining squares multiply by 8 each step and the holes grow by the number of squares of "
        "the step before.",
        "A square canvas with Step 0 to Step 3 buttons, a tap mode that lets the student remove the centre of each "
        "square by hand, and a counter panel for remaining squares, holes and the area that is left.",
        ["Predict the number of remaining squares and holes for the next step before tapping.",
         "Tap the centre of each square to remove it, or press Next step to apply the rule everywhere.",
         "Read the counters and compare them with the prediction.",
         "Write the rule for remaining squares and for holes in words."],
        ["Step 1: how many squares remain and how many holes are there?",
         "Step 2: predict the remaining squares before removing any centre.",
         "Step 2: predict the number of holes.",
         "Step 3: predict the remaining squares using the rule multiply by 8.",
         "Step 3: predict the holes by adding the squares of Step 2 to the holes of Step 2.",
         "What fraction of the starting area is left after Step 2?"],
        ["A count that adds 8 instead of multiplying by 8 is shown next to the actual picture, square by square.",
         "A hole count that forgets older holes highlights the holes from the earlier steps in a second colour.",
         "An area answer is checked by showing 8 of 9 parts kept at each step."],
        "All six cards are answered with the prediction matching the counters.",
        ["step", "remaining", "holes", "areaLeft", "tapMode", "cardIndex"],
        ["M_FRACTAL_ADD", "M_HOLES_EQUAL", "M_AREA_GROWS"],
        ["What happens to one square when the rule is applied to it?",
         "Every remaining square becomes 8 smaller remaining squares and 1 new hole.",
         "Multiply the remaining squares of the last step by 8; add those same squares to the old holes.",
         "The count is shown on the picture and the next card follows."]),

    "cube_net_folder": T(
        "tool_cube_net_folder", "Net Folder: Will It Make a Cube?", "manipulative",
        "A net is a solid unfolded onto a plane. Six joined squares fold into a cube only when no two squares land on "
        "the same face; there are exactly 11 different nets of a cube.",
        "A square grid where the student places six squares edge to edge, a Fold button that animates the folding in "
        "3D and colours any overlapping faces, a gallery that collects each new working net up to 11, and a cuboid "
        "mode with editable length, breadth and height.",
        ["Arrange six squares on the grid and predict whether they fold into a cube.",
         "Press Fold and watch which faces meet, or overlap.",
         "Save each new working net; the gallery rejects a net that is a turn or a flip of one already saved.",
         "Switch to cuboid mode and build a net with the given side lengths."],
        ["Fold the cross shaped net and name the face opposite the bottom square.",
         "Build a row of four with both extra squares on the same side: predict, then fold.",
         "Build the staircase of 2, 2 and 2 squares and fold it.",
         "Find three different nets that are not crosses.",
         "Collect all 11 nets in the gallery.",
         "Cuboid mode: build a net for a 4 cm by 2 cm by 1 cm box."],
        ["An overlapping fold colours the two faces that land on the same place and the empty face of the cube.",
         "A repeated net in the gallery is shown turned or flipped onto the saved one.",
         "A cuboid net with a mismatched edge highlights the two edges that must be equal."],
        "The six cards are done and at least 6 of the 11 nets are in the gallery.",
        ["squares", "folded", "overlap", "gallery", "mode", "dims", "cardIndex"],
        ["M_ANY_SIX"],
        ["Which square will be the bottom of the cube?",
         "A row of four squares wraps around to make four side faces; where must the top and bottom go?",
         "In a row of four, put one extra square above the row and one below it.",
         "A working net is shown folding and the next card follows."]),

    "net_path_unfolder": T(
        "tool_net_path_unfolder", "Ant Path Unfolder", "manipulative",
        "A path on the surface of a box becomes a path of the same length on a net, so the shortest path is a straight "
        "line on a suitable net. Different unfoldings give different straight lines, and some leave the net.",
        "A 3D box with an ant and a laddu that can be placed on any face, an Unfold menu that lays the faces out in "
        "different ways, a ruler line drawn from ant to laddu on the net with its length, and a Fold back button that "
        "shows the same path on the box.",
        ["Place the ant and the laddu, then predict the shortest path on the box.",
         "Choose an unfolding and draw the straight line from ant to laddu.",
         "Check whether the line stays inside the net, and read its length.",
         "Try other unfoldings and keep the shortest line that stays inside the net."],
        ["Cube of side 4 cm: ant at the centre of a side face, laddu at the centre of the top face.",
         "Cube of side 6 cm: ant at the centre of the front face, laddu at the middle of the edge between the top and "
         "the right face.",
         "Box 8 cm by 4 cm by 4 cm: find an unfolding where the straight line leaves the net.",
         "Same box: find the unfolding that gives a real path and read its length.",
         "Box 30 cm by 12 cm by 12 cm: compare the 42 cm route with the 40 cm route.",
         "Fold back the shortest line and describe the faces it crosses."],
        ["A line that leaves the net turns red and the gap is highlighted.",
         "A longer line is shown beside the shortest one found so far with both lengths.",
         "Folding back shows the line as a bent path on the box with the same length."],
        "All six cards are done with the shortest valid line found each time.",
        ["box", "ant", "laddu", "unfolding", "lineLength", "insideNet", "cardIndex"],
        ["M_STRAIGHT_BOX"],
        ["Which faces must the ant walk across?",
         "Lay those faces flat side by side so the ant and the laddu are on one flat piece.",
         "Draw the straight line and use a right triangle to find its length.",
         "The shortest valid unfolding is shown with its length and the next card follows."]),

    "views_viewer": T(
        "tool_views_viewer", "Three Views Viewer", "manipulative",
        "Projecting a solid onto three perpendicular planes gives its front, top and side views. Different solids can "
        "share one view, so all three views together describe a solid much better than any single one.",
        "A 3D solid that can be turned freely, three panels showing its live front, top and side views, a shape "
        "picker (cube, cuboid, parallelepiped, cylinder, cone, prism, pyramid, everyday objects), and a cube builder "
        "for stacks of unit cubes.",
        ["Pick a solid and predict its three views before looking at the panels.",
         "Turn the solid and watch how each view changes.",
         "Build a stack of cubes and compare its views with a target set.",
         "Find two different solids that share the same top view."],
        ["Cylinder standing on its base: draw the three views, then check.",
         "Cone standing on its base: predict the front and top views.",
         "Square pyramid: predict the three views.",
         "Find another solid with the same top view as the cone.",
         "Build a stack of 4 cubes whose front view is an L shape.",
         "Match a funnel with its front, top and side views."],
        ["A wrong view prediction overlays the true view on the drawing.",
         "A stack with the wrong view highlights the column of cubes that differs.",
         "Two solids with one shared view are shown side by side with their other views differing."],
        "All six cards are done with each prediction matched to the live views.",
        ["solid", "rotation", "front", "top", "side", "cubes", "cardIndex"],
        ["M_ONE_PROFILE", "M_PROJ_LONGER"],
        ["Which plane is in front of the solid, which is below it, and which is beside it?",
         "Look straight at the solid from that plane: what outline does it leave?",
         "For a stack of cubes, count the tallest column seen along each line of sight.",
         "The correct view is drawn and the next card follows."]),

    "iso_grid_builder": T(
        "tool_iso_grid_builder", "Isometric Grid Builder", "manipulative",
        "On an isometric grid the three directions of length, depth and height are drawn along three families of "
        "parallel lines with equal unit lengths, so a solid made of cubes can be drawn by counting edges.",
        "An isometric dot grid with a cube stamp that snaps to the grid, a line pen that draws along the three "
        "directions only, an axis key for length, depth and height, and a hidden line eraser.",
        ["Predict how many units each edge needs before drawing.",
         "Stamp cubes or draw edge by edge along the three directions.",
         "Erase hidden lines so only the visible edges remain.",
         "Compare the drawing with the solid shown in 3D."],
        ["Draw a 1 by 1 by 1 cube edge by edge.",
         "Draw a 2 by 2 by 2 cube.",
         "Draw a row of four cubes along the depth axis.",
         "Draw the L shaped tetris piece as cubes.",
         "Draw the T shaped tetris piece as cubes.",
         "Glue four cubes in a shape that is not flat and draw it."],
        ["An edge drawn off the three directions is rejected and the nearest direction is shown.",
         "A hidden line left in place flashes until it is erased.",
         "A drawing with the wrong number of units on an edge is compared with the 3D solid."],
        "All six cards are drawn with every visible edge correct.",
        ["cubes", "edges", "hidden", "axis", "cardIndex"],
        ["M_ISO_PERSPECTIVE"],
        ["Which direction on the grid is height, which is length and which is depth?",
         "Count units along one direction at a time.",
         "Draw the front vertical edges first, then the top, then the side.",
         "The finished drawing is shown and the next card follows."]),

    "triangle_stepper": T(
        "tool_triangle_stepper", "Triangle Stepper: Grow the Gasket", "manipulative",
        "Every remaining triangle of the Sierpinski Triangle splits into 4 equal triangles and loses the middle one, so "
        "the remaining triangles are multiplied by 3 at each step, the holes grow by the triangles of the step before, "
        "and the area left is multiplied by three quarters.",
        "An equilateral triangle canvas with Step 0 to Step 4 buttons, a midpoint tool that joins the midpoints of any "
        "triangle and shades the middle one out, and a counter panel for remaining triangles, holes and the area left "
        "when the starting area is 1 square unit.",
        ["Predict the remaining triangles and the holes for the next step before pressing anything.",
         "Join the midpoints of a triangle by hand, or press Next step to apply the rule everywhere.",
         "Read the counters and compare them with the prediction.",
         "Write the rule for triangles, holes and area in words."],
        ["Step 1: how many triangles remain and how many holes are there?",
         "Step 2: predict the remaining triangles and the holes.",
         "Step 3: predict the remaining triangles and the holes.",
         "Step 4: use the rule to predict the remaining triangles and the holes.",
         "What area is left after Step 2 and after Step 3, if the starting area is 1 square unit?",
         "After Step 2, which has less area left: the carpet or the triangle?"],
        ["A count that adds 3 instead of multiplying by 3 is shown beside the real picture, triangle by triangle.",
         "A hole count that forgets the older holes highlights the holes from earlier steps in a second colour.",
         "An area answer is checked by shading 3 of every 4 parts at each step and showing the fraction that is left."],
        "All six cards are answered with the prediction matching the counters.",
        ["step", "remaining", "holes", "areaLeft", "midpointTool", "cardIndex"],
        ["M_AREA_GROWS", "M_HOLES_EQUAL"],
        ["What happens to one triangle when its midpoints are joined and the middle one is removed?",
         "Every remaining triangle becomes 3 smaller remaining triangles and makes 1 new hole.",
         "Multiply the remaining triangles of the last step by 3; add those same triangles to the old holes.",
         "The counts are shown on the picture and the next card follows."]),

    "koch_bump_builder": T(
        "tool_koch_bump_builder", "Bump Builder: Grow the Snowflake", "manipulative",
        "The Koch Snowflake grows by one rule: cut every side into 3 equal parts and raise a bump on the middle part. "
        "Every side becomes 4 sides, each a third as long, so the sides are multiplied by 4 and the perimeter by four "
        "thirds at every step.",
        "An equilateral triangle canvas with a bump tool that replaces a side by four shorter sides, Step 0 to Step 3 "
        "buttons that apply the rule to every side, a starting side length box, and a counter panel for the number of "
        "sides, the length of each side and the perimeter.",
        ["Predict the number of sides and the perimeter for the next step before pressing anything.",
         "Raise a bump on one side by hand, or press Next step to bump every side.",
         "Read the counters and compare them with the prediction.",
         "Write the rule for the sides and the perimeter in words."],
        ["Starting side 1 unit, Step 1: how many sides, how long is each side and what is the perimeter?",
         "Step 2: predict the sides, the length of each side and the perimeter.",
         "Step 3: predict the number of sides and the perimeter.",
         "By what number is the perimeter multiplied from Step 1 to Step 2?",
         "Starting side 9 units: find the perimeter at Step 0, Step 1 and Step 2.",
         "How many sides are there at Step 4?"],
        ["A count that adds 3 sides instead of multiplying by 4 is shown next to the picture, side by side.",
         "A perimeter that forgets that every side is a third as long is checked by drawing the old and the new sides "
         "on the same line.",
         "A perimeter answer is checked by showing the number of sides times the length of one side."],
        "All six cards are answered with the prediction matching the counters.",
        ["step", "sides", "sideLength", "perimeter", "startSide", "bumpTool", "cardIndex"],
        ["M_KOCH_SIDES"],
        ["What happens to one side when the bump rule is applied to it?",
         "One side becomes 4 sides, each one third as long as the old side.",
         "Multiply the sides by 4, divide the side length by 3, then multiply the two to get the perimeter.",
         "The counts are shown on the picture and the next card follows."]),

    "solid_parts_counter": T(
        "tool_solid_parts_counter", "Solid Parts Counter: Prisms and Pyramids", "manipulative",
        "A prism on an n sided polygon has n plus 2 faces, 3n edges and 2n vertices, while a pyramid on the same "
        "polygon has n plus 1 faces, 2n edges and n plus 1 vertices. Changing n shows how each count depends on the "
        "number of sides of the base.",
        "A 3D prism or pyramid that can be turned, a switch between Prism and Pyramid, a slider for the number of "
        "sides n of the base from 3 to 12, tap to highlight a face, an edge or a vertex, and a counter panel for "
        "faces, edges and vertices.",
        ["Choose a solid and a number of sides, and predict the faces, edges and vertices before reading the "
         "counter.",
         "Tap the faces, edges and vertices one by one to count them on the solid.",
         "Change n and watch which counts change and by how much.",
         "Write the rule for each count in terms of n."],
        ["Triangular prism: find the faces, edges and vertices.",
         "Square pyramid: find the faces, edges and vertices.",
         "Pentagonal prism: find the faces, edges and vertices.",
         "Hexagonal pyramid: find the faces, edges and vertices.",
         "A prism on a 12 sided polygon: find the faces, edges and vertices.",
         "A prism and a pyramid both have a 9 sided base: which has more edges, and what is faces plus vertices "
         "minus edges for each?",
         "A pyramid has 24 edges: how many sides does its base have?"],
        ["A prism count given for a pyramid is shown with the two solids side by side, with the extra edges and "
         "vertices highlighted.",
         "A count that misses the base faces highlights the two bases of the prism, or the single base of the "
         "pyramid.",
         "A rule that does not fit a second value of n is tested on the solid with that n."],
        "All seven cards are answered with the counts matching the counter.",
        ["solidType", "sides", "faces", "edges", "vertices", "highlight", "cardIndex"],
        ["M_PRISM_PYRAMID"],
        ["Which polygon is the base, and how many sides does it have?",
         "Count the side faces first: there is one for every side of the base.",
         "For a prism add the two bases; for a pyramid add one base. Count edges and vertices on the base polygon, "
         "then on the rest of the solid.",
         "The counts are shown on the solid with their rule in n and the next card follows."]),

    "net_roller": T(
        "tool_net_roller", "Net Roller: Unroll a Cylinder and a Cone", "manipulative",
        "A cylinder unrolls into two circles and a rectangle whose sides are the circumference of the base and the "
        "height. A cone unrolls into a circle and a sector of a circle whose radius is the slant length and whose arc "
        "is as long as the circumference of the base.",
        "A cylinder and a cone that unroll with a slider, sliders for the base radius, the height and the slant "
        "length, a switch between Cylinder and Cone, and a read-out of the rectangle sides, or of the sector as a "
        "fraction of a full circle and as an angle.",
        ["Predict the shape of the net and its measurements before unrolling.",
         "Drag the slider to unroll the solid and watch the curved surface open out flat.",
         "Change the radius, the height or the slant length and watch the net change.",
         "Write the rule for the net in words."],
        ["Cylinder of radius 14 cm and height 20 cm, with pi as 22 over 7: find the sides of the rectangle.",
         "Cylinder of radius 3.5 cm and height 5 cm: find the sides of the rectangle.",
         "A cylinder net has a rectangle 66 cm long and 4 cm tall, with pi as 22 over 7: find the radius of the base.",
         "Cone of base radius 7 cm and slant length 14 cm: what fraction of a full circle is the sector?",
         "Cone of base radius 3 cm and slant length 9 cm: what fraction of a full circle is the sector?",
         "Cone of base radius 4 cm and slant length 5 cm: find the fraction and the angle of the sector.",
         "A cone of base radius 6 cm unrolls into a quarter of a circle: find its slant length."],
        ["A rectangle side taken as the diameter instead of the circumference is shown wrapped round the base, "
         "falling short of going all the way round.",
         "A sector with the wrong fraction is rolled up and the gap or overlap at the seam is highlighted.",
         "A slant length that is shorter than the radius is rejected, since the slant length is the longest side of "
         "the cone."],
        "All seven cards are answered and the unrolled net closes up into the solid each time.",
        ["solidType", "radius", "height", "slant", "unrollAmount", "cardIndex"],
        ["M_CYL_RECT"],
        ["Which part of the solid is unrolled, and which part stays as circles?",
         "The curved edge of the net is as long as the circle it was wrapped round.",
         "For the cylinder, the long side is 2 times pi times the radius; for the cone, the sector fraction is the "
         "base radius divided by the slant length.",
         "The net is shown with its measurements and a similar card follows."]),

    "projection_tilter": T(
        "tool_projection_tilter", "Projection Tilter: Sticks and Cards", "manipulative",
        "The projection of a line on a plane is found by dropping perpendiculars, and it is never longer than the line: "
        "the line, its projection and the height difference make a right triangle. A flat card keeps parallel sides "
        "parallel when it is tilted, so a tilted parallelogram always projects to a parallelogram or a line.",
        "A table plane with a stick or a card that can be tilted by dragging one end up, perpendicular drop lines to "
        "the table, a live projection drawn on the table, a read-out of the stick length, the height difference and "
        "the projection length, and a switch between Stick and Card.",
        ["Predict whether the projection will be longer, shorter or equal before tilting.",
         "Drag an end of the stick or an edge of the card up and watch the projection change.",
         "Read the length of the stick, the height difference and the projection.",
         "Compare the three numbers and write the rule in words."],
        ["A stick 17 cm long has one end 8 cm higher than the other: find the length of its projection.",
         "A rod 25 cm long has one end 7 cm higher: find the length of its projection.",
         "A stick 10 cm long has a projection of 6 cm: find the height difference of its ends.",
         "Tilt the stick until its projection is as long as the stick: what is the height difference?",
         "A square card of side 10 cm is tilted about one side so that the opposite side is 6 cm higher: find the "
         "projection.",
         "A square card has diagonals of 16 cm and is tilted about one diagonal so that the other diagonal projects "
         "to 12 cm: find the shape and the side of the projection.",
         "Try to tilt a parallelogram card so that its projection is a trapezium, and say what you find."],
        ["A projection drawn longer than the stick is rejected and the right triangle is shown with the stick as its "
         "longest side.",
         "A card projection with sides that are not parallel is rejected and the matching pairs of parallel sides "
         "are highlighted.",
         "A projection answer is checked by showing the right triangle with the stick, the height difference and the "
         "projection."],
        "All seven cards are answered with the prediction matching the live projection.",
        ["mode", "stickLength", "heightDifference", "projectionLength", "tilt", "cardShape", "cardIndex"],
        ["M_PROJ_LONGER", "M_PROJ_ANY"],
        ["Where do the perpendiculars from the two ends of the stick meet the table?",
         "The stick, its projection and the height difference make a right triangle; which side is the longest?",
         "The square of the longest side equals the sum of the squares of the other two sides.",
         "The right triangle is shown with the projection length and a similar card follows."]),
}
