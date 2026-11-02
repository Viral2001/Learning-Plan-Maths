# -*- coding: utf-8 -*-
"""Tool specs for module M1 (triangles from three lengths)."""
from topics_common import T

TOOLS = {
    "compass_triangle_builder": T(
        "tool_compass_triangle_builder", "Compass Triangle Builder", "manipulative",
        "Two arcs, one from each end of the base, cross at the third vertex; the crossing point is exactly the "
        "point that is the right distance from both ends.",
        "A horizontal base with draggable end points and a length readout; two radius sliders; two arcs drawn from the "
        "ends; the crossing point marked as the third vertex; a readout of the three sides.",
        ["Set the base and the other two lengths for the card.",
         "Drag each arc radius until it matches its length.",
         "Watch where the arcs cross and join the crossing point to both ends.",
         "Check the three side readouts against the card."],
        ["Sides 4, 5 and 6: the arcs cross above the base.",
         "Sides 4, 4 and 6: the triangle comes out isosceles.",
         "Sides 5, 5 and 5: an equilateral triangle.",
         "Sides 3, 4 and 5: a triangle with a right angle.",
         "Sides 3, 4 and 8: the arcs miss.",
         "Sides 2, 5 and 6: pick the arc radii and watch them cross."],
        ["A pair of arcs that cross shows the third vertex and the three side lengths.",
         "Arcs that miss show how far apart they are.",
         "Equal arc radii highlight the equal sides."],
        "All six cards are built or marked as impossible with the reason.",
        ["baseLen", "radiusA", "radiusB", "crossing", "cardIndex"],
        ["M_ANY_LENGTHS"],
        ["Which two lengths set the arcs, and from which ends?",
         "Draw an arc from each end of the base; the vertex is where they cross.",
         "Set the radii to the two given sides and look for the crossing.",
         "The arcs and the crossing are shown for this card, then a new card follows."]),

    "triangle_inequality_checker": T(
        "tool_triangle_inequality_checker", "Triangle Inequality Checker", "manipulative",
        "A triangle exists when every length is less than the sum of the other two, and it is enough to compare the "
        "longest length with the sum of the other two.",
        "Three length sliders; three bars; for each length a comparison line with the other two added; a verdict "
        "panel; a tent and two poles picture that stretches or goes slack as the lengths change.",
        ["Set three lengths with the sliders.",
         "Read the three comparisons and tick those that hold.",
         "Decide whether the triangle exists and then press check.",
         "Move one slider to find the exact length where the verdict flips."],
        ["3, 4 and 8: the longest is too long.",
         "5, 5 and 8: a triangle exists.",
         "3, 6 and 9: the sum equals the longest.",
         "10, 20 and 25: all three comparisons hold.",
         "1, 100 and 100: a very thin triangle exists.",
         "6, 7 and 12: only the longest comparison matters."],
        ["Each comparison line turns green when it holds and red when it fails.",
         "A flat triangle is shown when the sum equals the longest length.",
         "The verdict names the comparison that failed."],
        "All six sets are decided with the failing comparison named.",
        ["lenA", "lenB", "lenC", "checks", "verdict", "cardIndex"],
        ["M_ANY_LENGTHS", "M_TWO_COMPARISONS", "M_SUM_EQUALS"],
        ["Which length is the biggest, and what do the other two add up to?",
         "Compare the longest length with the sum of the other two.",
         "Add the two shorter lengths and see if the total is more than the longest.",
         "The sums for this set are shown beside the longest length and the verdict is given, then a new set follows."]),

    "two_circles_explorer": T(
        "tool_two_circles_explorer", "Two Circles Explorer", "simulation",
        "Two circles drawn from the ends of the base cross in two points exactly when the base is less than the sum "
        "of the radii and more than their difference, which matches the triangle inequality.",
        "A base AB with a draggable radius for each end; the two circles drawn on the base; the number of common "
        "points shown; the base length, the sum of the radii and the difference of the radii as readouts.",
        ["Drag each radius and watch the two circles.",
         "Note whether they miss, touch or cross.",
         "Read the sum of the radii against the base.",
         "Find the radii at which the circles first touch."],
        ["Base 8 with radii 3 and 5: the circles touch.",
         "Base 8 with radii 2 and 5: the circles miss.",
         "Base 8 with radii 5 and 6: the circles cross twice.",
         "Base 9 with radii 3.5 and 6: the circles touch.",
         "Base 11 with radii 4 and 7: the circles touch.",
         "Choose radii that make the circles cross for a base of 7."],
        ["Touching circles show the touching point on the base line.",
         "Missing circles show the gap.",
         "Crossing circles show both crossing points as the possible third vertices."],
        "All six cards are answered with the number of common points.",
        ["baseLen", "radiusA", "radiusB", "points", "cardIndex"],
        ["M_SUM_EQUALS", "M_ANY_LENGTHS"],
        ["Where do the two circles end up relative to each other?",
         "Compare the base with the sum of the two radii.",
         "Add the radii and see whether the total is more than the base.",
         "The sum and the number of common points are shown, then a new card follows."]),
}
