# -*- coding: utf-8 -*-
"""Tool specs for module M3 (altitudes and kinds of triangles)."""
from topics_common import T

TOOLS = {
    "altitude_explorer": T(
        "tool_altitude_explorer", "Altitude Explorer", "manipulative",
        "The altitude from a vertex is the perpendicular to the line of the opposite side; it falls inside for an "
        "acute triangle, along a side for a right triangle and outside for an obtuse triangle.",
        "A triangle with draggable vertices; a set square that slides along the chosen base; the altitude from the "
        "top vertex with a right-angle mark; the base line extended when needed.",
        ["Pick a base and slide the set square to the top vertex.",
         "Draw the altitude and see where its foot lands.",
         "Drag a vertex to make the triangle acute, right or obtuse.",
         "Choose a different base and draw its altitude."],
        ["An acute triangle: all three altitudes lie inside.",
         "A right triangle: two altitudes are sides.",
         "An obtuse triangle: the altitude from the top falls outside.",
         "Draw the altitude from the obtuse vertex.",
         "Pick the base that makes the altitude shortest.",
         "Draw all three altitudes of one triangle."],
        ["The right-angle mark shows at the foot of each altitude.",
         "The base is extended with a dotted line when the foot is outside.",
         "A side that is an altitude is highlighted."],
        "All six cards are done with the altitude foot placed correctly.",
        ["vertices", "base", "foot", "extended", "cardIndex"],
        ["M_ALTITUDE_INSIDE"],
        ["Which line must the altitude be perpendicular to?",
         "Slide the set square along the base line until it touches the top vertex.",
         "If the foot would fall beyond the base, extend the base.",
         "The altitude is drawn for this card and a new card follows."]),

    "triangle_classifier": T(
        "tool_triangle_classifier", "Triangle Classifier", "manipulative",
        "A triangle has a name by its sides and a name by its angles, and the angle sum limits which pairs of names "
        "can go together.",
        "A triangle with draggable vertices; side lengths and angle measures shown; two label slots for the sides "
        "name and the angles name; a table of the names found so far.",
        ["Drag the vertices to a shape.",
         "Read the three sides and three angles.",
         "Choose the name by sides and the name by angles.",
         "Try to make a combination that the angle sum does not allow."],
        ["Make an equilateral triangle: what is its angle name.",
         "Make an isosceles triangle with a right angle.",
         "Make an isosceles triangle with an obtuse angle.",
         "Try to make an equilateral triangle with a right angle.",
         "Make a scalene triangle with all angles acute.",
         "Fill the table of names found."],
        ["The names change as the vertices move.",
         "An impossible combination is explained with the angle sum.",
         "The table keeps each name pair found."],
        "All six cards are done and the table has the possible name pairs.",
        ["vertices", "sideName", "angleName", "found", "cardIndex"],
        ["M_ACUTE_ONE", "M_EQUILATERAL_RIGHT"],
        ["What do the sides tell you, and what do the angles tell you?",
         "Add the three angles and think about what the biggest one can be.",
         "If two angles are equal, check the third with the angle sum.",
         "The angles for this card are shown with the names, then a new card follows."]),
}
