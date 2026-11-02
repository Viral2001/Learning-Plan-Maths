# -*- coding: utf-8 -*-
"""Tool specs for modules M2 to M4 (distance explorer, diagonals, side and diagonal builder, equal distance)."""
from topics_common import T

TOOLS = {
    "xy_explorer": T(
        "tool_m2s9c4", "Rectangle Distance Explorer", "simulation",
        "Between two points sliding on opposite sides of a rectangle, the length XY is shortest when the points "
        "are level, and longest when they are at opposite corners, where XY is a diagonal.",
        "A rectangle with side lengths on sliders; a point X on one side and a point Y on the opposite side, each "
        "draggable; a live read-out of XY; a table that records each position.",
        ["Predict where XY is shortest and where it is longest.",
         "Drag X and Y and record positions in the table.",
         "Type the shortest or the longest length."],
        ["Rectangle 7 cm by 4 cm, X and Y on the two 4 cm sides: shortest XY? (7 cm)",
         "The same rectangle: longest XY, to the nearest tenth. (8.1 cm)",
         "Rectangle 6 cm by 3 cm, points on the two 3 cm sides: shortest XY? (6 cm)",
         "Rectangle 4 cm by 3 cm, points on the two 3 cm sides: longest XY? (5 cm)",
         "Rectangle 8 cm by 6 cm, points on the two 6 cm sides: longest XY? (10 cm)",
         "Rectangle 12 cm by 5 cm, points on the two 5 cm sides: longest XY? (13 cm)"],
        ["A slanting XY looks shorter to the eye; the table shows it longer than the level one.",
         "When X and Y are level, the tool shades ABYX and shows it as a rectangle with XY the same as AB.",
         "A solved card shows the position and the XY read-out."],
        "All six cards are solved.",
        ["xPosition", "yPosition", "xyLength", "answer", "cardIndex"],
        ["M_SLANT_SHORTER", "M_RULER_END"],
        ["Which two sides do X and Y slide on?",
         "XY is shortest when X and Y are level and longest when they are at opposite corners.",
         "Slide the points to the level position and to opposite corners, and read XY.",
         "The tool shows both positions with their XY; a similar card follows."]),

    "diagonal_explorer": T(
        "tool_m3s12c3", "Diagonal Explorer", "simulation",
        "In every rectangle the two diagonals are equal, and each diagonal splits a corner into two angles that "
        "add up to 90°; the two angles are equal only for a square.",
        "A rectangle with two side sliders; both diagonals drawn and labelled with their lengths; the eight small "
        "angles marked with read-outs; a corner total read-out.",
        ["Predict the diagonal or an angle before moving the sliders.",
         "Change the sides and read both diagonals and the angles.",
         "Type the length or the missing angle."],
        ["Rectangle 6 cm by 4 cm: diagonal, to the nearest tenth. (7.2 cm)",
         "Rectangle 8 cm by 6 cm: diagonal? (10 cm)",
         "One angle at a corner is 50°: the other angle? (40°)",
         "Rectangle 12 cm by 5 cm: diagonal? (13 cm)",
         "Square of side 5 cm: each small angle at a corner? (45°)",
         "Rectangle 4 cm by 3 cm: how long is the second diagonal? (5 cm, the same as the first)"],
        ["Expecting a longer diagonal for a longer side pair: the tool shows both diagonals equal.",
         "Expecting equal corner angles: the tool shows them equal only when the two sides are equal.",
         "A solved card shows both diagonals and the corner angles."],
        "All six cards are solved.",
        ["lengthSide", "breadthSide", "diagonal", "answer", "cardIndex"],
        ["M_DIAG_EQUAL_SQUARE", "M_DIAG_BISECT_ANGLES", "M_SQUARE_NOT_RECT"],
        ["What does the card ask: a length or an angle?",
         "The two diagonals are equal, and the two angles at a corner add up to 90°.",
         "Set the sides from the card and read the diagonal or take the angle from 90°.",
         "The tool shows the diagonals and the angles; a similar card follows."]),

    "side_diagonal_builder": T(
        "tool_m3s15c4", "Side and Diagonal Builder", "manipulative",
        "A rectangle with a given side and diagonal is built by drawing the base, a perpendicular at one end, and "
        "an arc around the other end with the diagonal as radius; the arc meets the perpendicular at the third "
        "corner.",
        "A base line with a ruler; a perpendicular at one end; a compass whose opening is set to the diagonal; "
        "an arc around the far end; a button that completes the rectangle and shows the second side.",
        ["Predict whether the second side is shorter or longer than the diagonal.",
         "Draw the base, the perpendicular and the arc.",
         "Complete the rectangle and read the second side."],
        ["Side 5 cm, diagonal 7 cm: second side, to the nearest tenth. (4.9 cm)",
         "Side 4 cm, diagonal 8 cm: second side, to the nearest tenth. (6.9 cm)",
         "Side 3 cm, diagonal 7 cm: second side, to the nearest tenth. (6.3 cm)",
         "Side 3 cm, diagonal 5 cm: second side? (4 cm)",
         "Side 6 cm, diagonal 10 cm: second side? (8 cm)",
         "Side 5 cm, diagonal 13 cm: second side? (12 cm)"],
        ["Putting the compass tip on the wrong end leaves the arc far from the perpendicular, and the tool shows "
         "the miss.",
         "A diagonal shorter than the side cannot make an arc that reaches the perpendicular; the tool shows the "
         "arc falling short.",
         "A solved card shows the base, the arc, the third corner and the finished rectangle."],
        "All six cards are solved.",
        ["side", "diagonal", "arcPlaced", "answer", "cardIndex"],
        ["M_ARC_FROM_ONE_POINT", "M_NAME_ANY_ORDER"],
        ["Which line is drawn first?",
         "The third corner is on the perpendicular and is as far from the other end of the base as the diagonal.",
         "Set the compass to the diagonal in the card and put the tip at the far end of the base.",
         "The tool shows the arc meeting the perpendicular; a similar card follows."]),

    "equidistant_explorer": T(
        "tool_m4s16c3", "Equal Distance Explorer", "simulation",
        "A point at a given distance from each of two points lies where an arc around the first meets an arc "
        "around the second; the arcs meet only if the radius is big enough.",
        "Two points B and C with a distance slider; a radius dial; arcs drawn around B and C that sweep out; the "
        "crossing point marked with its distance from B and from C.",
        ["Predict whether the arcs will cross before setting the radius.",
         "Set the distance between B and C and the radius.",
         "Read the crossing point and its distance, or say that there is none."],
        ["B and C are 5 cm apart, radius 5 cm: distance of the crossing point from B? (5 cm)",
         "B and C are 6 cm apart, radius 5 cm: how high above the middle of BC is the crossing point? (4 cm)",
         "B and C are 8 cm apart, radius 5 cm: how high above the middle? (3 cm)",
         "B and C are 8 cm apart, radius 3 cm: do the arcs cross? (no)",
         "B and C are 10 cm apart, radius 5 cm: where do the arcs meet? (at the middle of BC)",
         "B and C are 5 cm apart, radius 5 cm: how high is the crossing point above BC, to the nearest tenth? "
         "(4.3 cm)"],
        ["Drawing only one arc leaves many possible points; the tool shows the second arc cutting it at the "
         "point.",
         "A radius that is too small leaves a gap between the arcs, and the tool shows it.",
         "A solved card shows both arcs and the crossing point with its two distances."],
        "All six cards are solved.",
        ["pointDistance", "radius", "crossing", "answer", "cardIndex"],
        ["M_ARC_FROM_ONE_POINT", "M_ARC_TIP_ON_FIGURE"],
        ["What must be true about the distance of the new point from B and from C?",
         "Draw an arc around each point; they cross where the point is that far from both.",
         "Set the radius from the card and find out whether the arcs reach each other.",
         "The tool shows both arcs and the crossing; a similar card follows."]),
}
