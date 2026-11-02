# -*- coding: utf-8 -*-
"""Tool specs for module M2 (triangles from angles)."""
from topics_common import T

TOOLS = {
    "two_angle_ray_explorer": T(
        "tool_two_angle_ray_explorer", "Two Angle Ray Explorer", "simulation",
        "Two rays from the ends of a base meet when the two angles add up to less than 180 degrees, whatever the "
        "length of the base.",
        "A base with two angle sliders at its ends; the two rays drawn upward; a meeting point if it exists; the sum of "
        "the two angles shown; a base-length slider.",
        ["Drag each angle slider and watch the two rays.",
         "Note when the rays stop meeting.",
         "Read the sum of the two angles at that point.",
         "Change the base length and see that the result does not change."],
        ["First angle 40: find where the other angle makes the rays fail.",
         "First angle 30: find the failing angle.",
         "First angle 70: find the failing angle.",
         "Angles 90 and 85: do the rays meet.",
         "Angles 50 and 150: do the rays meet.",
         "Change the base length for a failing pair."],
        ["Parallel rays are marked when the sum is exactly 180.",
         "A meeting point appears when the sum is below 180.",
         "The base length slider never changes the verdict."],
        "All six cards are decided and the rule on the sum is stated.",
        ["angleA", "angleB", "baseLen", "meets", "cardIndex"],
        ["M_ANGLE_PAIR"],
        ["What do the two rays do as the angles grow?",
         "Look at the sum of the two angles when the rays stop meeting.",
         "Find the second angle that makes the sum exactly 180.",
         "The failing angle for this card is shown with the sum, then a new card follows."]),

    "angle_sum_parallel": T(
        "tool_angle_sum_parallel", "Angle Sum with a Parallel Line", "manipulative",
        "A line through the top vertex parallel to the base turns the two base angles into alternate angles at the "
        "top, so the three angles fill a straight line.",
        "A triangle with angle sliders for the two base angles; a draggable parallel line through the top vertex; "
        "alternate angles highlighted; a straight-angle bar filled by the three angles; a readout of the third angle.",
        ["Set the two base angles.",
         "Draw the parallel line through the top vertex.",
         "Match each alternate angle to a base angle.",
         "Read the angle left on the straight line as the third angle."],
        ["Angles 36 and 72.", "Angles 150 and 15.", "Angles 90 and 30.", "Angles 75 and 45.",
         "Angles 70 and 70: what is the third angle.", "Angle 50 at the top with equal base angles."],
        ["Alternate angles flash in matching colours.",
         "The straight-angle bar shows how much is left.",
         "A pair that adds to 180 or more is stopped with a note."],
        "All six cards are done with the third angle correct.",
        ["baseB", "baseC", "parallelDrawn", "thirdAngle", "cardIndex"],
        ["M_THIRD_ANGLE_SIDE", "M_ANGLE_PAIR"],
        ["Which angles at the top are equal to the base angles?",
         "The three angles at the top fill a straight line of 180 degrees.",
         "Take the two base angles away from 180.",
         "The sums for this card are shown and the third angle is given, then a new card follows."]),

    "exterior_angle_explorer": T(
        "tool_exterior_angle_explorer", "Exterior Angle Explorer", "manipulative",
        "An exterior angle and the interior angle next to it make a straight angle, so the exterior angle equals the "
        "sum of the two opposite interior angles.",
        "A triangle with one side extended; sliders for two interior angles; the exterior angle marked; a readout of "
        "the two opposite angles added and the exterior angle side by side.",
        ["Set two interior angles.",
         "Read the exterior angle.",
         "Add the two opposite angles and compare.",
         "Try different angles to see whether the match always holds."],
        ["Angles 50 and 60.", "Angles 35 and 45.", "Angles 90 and 30.", "Angles 70 and 20.",
         "Exterior angle 120 and one opposite angle 80.", "Predict the exterior angle for 25 and 65."],
        ["The two opposite angles slide next to the exterior angle to show they fill it.",
         "A mismatch is flagged with the angle sum.",
         "The straight angle at the vertex is shown."],
        "All six cards are done and the match is stated.",
        ["angleA", "angleB", "exterior", "cardIndex"],
        ["M_EXTERIOR_ANGLE"],
        ["Which angle makes a straight angle with the exterior angle?",
         "Use the angle sum to find the third interior angle first.",
         "Subtract the third interior angle from 180.",
         "The steps are shown and the exterior angle matches the sum of the two opposite angles; a new card follows."]),
}
