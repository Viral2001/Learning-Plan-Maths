# -*- coding: utf-8 -*-
"""Topics T1 to T3 (module M1: lines that meet). Book sections 5.1 and 5.2."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Across the Line ===========================================================
TOPICS.append(TOPIC(
    "T1", "M1", "Across the Line", ["5.1"], "Understand",
    "",
    "Creases on a folded square of paper make lines, and a pair of them raises the question to keep: would they meet "
    "if they were drawn much longer?",
    [A("T1.C1", "Creases on a folded paper", "Remember",
       "",
       textbook=["Across the Line",
                 "Use a piece of square paper and fold it in different ways. Now, on the creases formed by the folds, "
                 "draw lines using a pencil and a scale.",
                 "You will notice different lines on the paper. Pick any pair of lines and observe their relationship "
                 "with each other. Do they meet? If they do not meet within the paper, do you think they would meet if "
                 "they were extended beyond the paper?"],
       teach=["Picture a square sheet folded a few times, with a pencil line drawn along each crease.",
              "Make a guess before the next step: do any two of these lines meet, and could two of them stay apart "
              "even on a much bigger sheet?"],
       ncert=["5.1.fold_lines"], key_terms=["crease"], video_focus=["HOOK"], minutes=4, enrichment=True),
     A("T1.C2", "The question to keep: do they meet?", "Understand", "",
       textbook=["In this chapter, we will explore the relationship between lines on a plane surface. The table top, "
                 "your piece of paper, the blackboard, and the bulletin board are all examples of plane surfaces."],
       teach=["Predict: of two creases on your sheet, which pairs meet inside the paper, and which pairs only could "
              "meet if the paper were bigger?",
              "A plane surface is flat: a table top, a page, a blackboard.",
              "Keep this question in mind: the next topics name each kind of pair and give a way to decide."],
       ncert=["5.1.plane"], key_terms=["plane surface"], enrichment=True)],
    topic_type="framing"))

# ============================== T2 Intersecting lines and linear pairs =========================================
TOPICS.append(TOPIC(
    "T2", "M1", "Intersecting Lines and Linear Pairs", ["5.1"], "Understand",
    "Students name the four angles that two intersecting lines make, find all four from one using the straight "
    "angle of 180 degrees, and prove that vertically opposite angles are equal.",
    "Two lines that cross make four angles: neighbours form a linear pair and add to 180 degrees, and opposite "
    "angles are equal.",
    [A("T2.C1", "Two lines that meet, and the four angles they make", "Understand",
       "Students state that two straight lines on a plane meet at one point only, that they make four angles, and "
       "that measured angles show a pattern.",
       textbook=["Let us observe a pair of lines that meet each other. You will notice that they meet at a point. "
                 "When a pair of lines meet each other at a point on a plane surface, we say that the lines "
                 "intersect each other.",
                 "Let us observe what happens when two lines intersect. How many angles do they form? Where line l "
                 "intersects line m, we can see that four angles are formed: a, b, c and d.",
                 "Can two straight lines intersect at more than one point?",
                 "Activity 1: Draw two lines on a plain sheet of paper so that they intersect. Measure the four "
                 "angles formed with a protractor. Draw four such pairs of intersecting lines and measure the angles "
                 "formed at the points of intersection.",
                 "What patterns do you observe among these angles?"],
       teach=["Predict first: if two straight lines cross, how many angles appear, and can they cross twice?",
              "Two straight lines can meet at one point only, so four angles are made, a, b, c and d, going round "
              "the point.",
              "Look at the measured angles in pairs: the ones that are neighbours and the ones that face each other.",
              "In every pair of lines drawn, neighbouring angles add to 180 degrees and facing angles are equal, or "
              "nearly equal when the pencil is thick."],
       examples=[
           WE("Farhan draws two lines that cross and measures the four angles with a protractor, going round the "
              "point: a = 63°, b = 117°, c = 63° and d = 117°. What pattern do the four angles show?",
              ["Neighbouring angles: 63 + 117 = 180, and 117 + 63 = 180.",
               "Angles that face each other: a and c are both 63°, and b and d are both 117°.",
               "So neighbouring angles add to 180° and facing angles are equal, in this pair of lines.",
               "Two straight lines meet at one point only, so there are exactly four angles at the crossing."],
              "Neighbours add to 180° and facing angles are equal; two straight lines meet at one point only",
              ncert=["5.1.two_points", "5.1.act1"])],
       ncert=["5.1.intersect"], key_terms=["intersect", "protractor"], misconceptions=["M_ADJACENT_EQUAL"],
       minutes=8),
     A("T2.C2", "Linear pairs and the straight angle", "Apply",
       "Students find the other three angles at a crossing from one angle, using that a linear pair adds to 180 "
       "degrees.",
       textbook=["If ∠a is 120°, can you figure out the measurements of ∠b, ∠c and ∠d, without drawing and "
                 "measuring them?",
                 "We know that ∠a and ∠b together measure 180°, because when they are combined, they form a straight "
                 "angle which measures 180°. So, if ∠a is 120°, then ∠b must be 60°.",
                 "Similarly, ∠b and ∠c together measure 180°. So, if ∠b is 60°, then ∠c must be 120°. And ∠c and ∠d "
                 "together measure 180°. So, if ∠c is 120°, then ∠d must be 60°.",
                 "Therefore, ∠a and ∠c measure 120°, and ∠b and ∠d measure 60°.",
                 "Adjacent angles, like ∠a and ∠b, formed by two lines intersecting each other, are called linear "
                 "pairs. Linear pairs always add up to 180°."],
       teach=["Predict first: if a is 120°, is b more or less than 90°?",
              "Angles a and b sit side by side on a straight line, so together they make a straight angle of 180°.",
              "Go round the point one angle at a time: each step takes the last angle away from 180°."],
       examples=[
           WE("Two lines cross. The angle a is 120°. Find b, c and d going round the point, without measuring.",
              ["a and b form a linear pair, so b = 180 − 120 = 60.",
               "b and c form a linear pair, so c = 180 − 60 = 120.",
               "c and d form a linear pair, so d = 180 − 120 = 60.",
               "So a and c are 120°, and b and d are 60°."],
              "b = 60°, c = 120°, d = 60°", ncert=["5.1.a120"])],
       key_terms=["linear pair", "straight angle"], misconceptions=["M_ADJACENT_EQUAL", "M_ARM_LENGTH"],
       minutes=8),
     A("T2.C3", "Vertically opposite angles, and a proof", "Understand",
       "Students prove, without using any measurement, that vertically opposite angles are equal, using two linear "
       "pairs.",
       textbook=["When two lines intersect each other and form four angles, labelled a, b, c and d, then ∠a and ∠c "
                 "are equal, and ∠b and ∠d are equal! Is this always true for any pair of intersecting lines?",
                 "Check this for different measures of ∠a. Using these measurements, can you reason whether this "
                 "property holds true for any measure of ∠a?",
                 "We can generalise our reasoning without assuming the values of ∠a. Since straight angles measure "
                 "180°, we must have ∠a + ∠b = ∠a + ∠d = 180°. Hence, ∠b and ∠d are always equal. Similarly, "
                 "∠b + ∠a = ∠b + ∠c = 180°, so ∠a and ∠c must be equal.",
                 "Opposite angles, like ∠b and ∠d, formed by two lines intersecting each other, are called "
                 "vertically opposite angles. Vertically opposite angles are always equal to each other.",
                 "From the above reasoning, we conclude that whenever two lines intersect, vertically opposite "
                 "angles are equal. Such a justification is called a proof in mathematics."],
       teach=["Predict first: if a is 35°, what are b and d, and does the answer depend on the 35?",
              "Keep a as an unknown: a + b = 180 and a + d = 180, so b and d must be equal.",
              "Nothing about 120° or 35° was used, so the reasoning holds for every pair of lines that cross: that "
              "is a proof."],
       examples=[
           WE("Two lines cross and a = 35°. Use linear pairs to find b and d, then show that they are equal for any "
              "value of a.",
              ["a and b form a linear pair, so b = 180 − 35 = 145.",
               "a and d form a linear pair, so d = 180 − 35 = 145.",
               "For any a: b = 180 − a and d = 180 − a, so b and d are equal whatever a is.",
               "In the same way, c = 180 − b = a, so a and c are equal. This justification is a proof."],
              "b = 145° and d = 145°; vertically opposite angles are always equal",
              ncert=["5.1.proof"])],
       ncert=["5.1.pairs_named"], key_terms=["vertically opposite angles", "proof"],
       misconceptions=["M_ADJACENT_EQUAL"], minutes=8),
     DOER("T2.C4", "Practice: linear pairs and vertically opposite angles", "crossing_angle_lab", "Apply",
          "Students list the linear pairs and the vertically opposite pairs at a crossing and find all four "
          "angles from one.",
          ["Neighbouring angles at a crossing make a linear pair and add to 180 degrees.",
           "Angles that face each other are vertically opposite and equal.",
           "One angle gives the other three: subtract it from 180 for the neighbours and copy it to the one "
           "opposite."],
          items=[
              FIO("5.1.FiO1", "Figure it Out (intersecting lines), Q1",
                  "Two lines l and m cross, and the four angles are named a, b, c and d going round the crossing, "
                  "with a and b neighbours. List all the linear pairs and all the pairs of vertically opposite "
                  "angles.",
                  ["Linear pairs are neighbouring angles that sit on a straight line: a and b, b and c, c and d, "
                   "d and a.",
                   "Vertically opposite angles face each other across the crossing: a and c, b and d.",
                   "Check: going round, there are four neighbouring pairs and two facing pairs."],
                  "Linear pairs: a and b, b and c, c and d, d and a. Vertically opposite pairs: a and c, b and d",
                  tool="crossing_angle_lab"),
          ],
          misconceptions=["M_ADJACENT_EQUAL"])]))

# ============================== T3 Ideal lines and perpendicular lines ========================================
TOPICS.append(TOPIC(
    "T3", "M1", "Ideal Lines and Perpendicular Lines", ["5.1", "5.2"], "Understand",
    "Students tell a measurement apart from a reason, explain why measured angles can be a degree or two off, and "
    "name lines that cross at four equal angles as perpendicular.",
    "Reasoning gives 180 degrees exactly, a protractor gives a close value, and lines that cross with four equal "
    "angles meet at right angles and are perpendicular.",
    [A("T3.C1", "Measuring and reasoning are not the same", "Understand",
       "Students explain that a measured linear pair may miss 180 degrees through measurement error, and that an ideal "
       "line gives the exact value by reasoning.",
       textbook=["You might have noticed that when you measure linear pairs, sometimes they may not add up to 180°. "
                 "Or, when you measure vertically opposite angles they may be unequal sometimes. What are the "
                 "reasons for this?",
                 "There could be different reasons: measurement errors because of improper use of measuring "
                 "instruments, in this case, a protractor; and variation in the thickness of the lines drawn. The "
                 "“ideal” line in geometry does not have any thickness! But it is not possible for us to draw lines "
                 "without any thickness.",
                 "In geometry, we create ideal versions of “lines” and other shapes we see around us, and analyse "
                 "the relationships between them. For example, we know that the angle formed by a straight line is "
                 "180°. So, if another line divides this angle into two parts, both parts should add up to 180°. "
                 "We arrive at this by reasoning and not by measurement. When we measure, it might not be exactly "
                 "so, for the reasons mentioned above. Still the measurements come out very close to what we "
                 "predict, because of which geometry finds widespread application in different disciplines such as "
                 "physics, art, engineering and architecture."],
       teach=["Predict first: one pair measures 63° and 119°; do they break the rule of 180°?",
              "A pencil line has a thickness, and a protractor is read by eye, so a reading is off by a degree or "
              "two.",
              "The rule comes from a straight line, an ideal line with no thickness, so reasoning gives the exact "
              "value and measuring gives a close value."],
       examples=[
           WE("Imran measures a linear pair as 63° and 119°. Their sum is not 180°. Does that break the rule? What "
              "should the second angle be?",
              ["63 + 119 = 182, which is 2° more than 180.",
               "The rule of 180° comes from a straight line with no thickness; a drawn line is thick and the reading "
               "of a protractor can be off by a degree or two.",
               "By reasoning, the second angle is 180 − 63 = 117.",
               "So the measure 119° is 2° off, a measurement error, and the rule is not broken."],
              "No; the second angle should be 117°, and the 2° is a measurement error",
              ncert=["5.1.measure_geom"])],
       key_terms=["ideal line", "measurement error"], misconceptions=["M_MEASURE_EXACT"], minutes=8),
     A("T3.C2", "All four angles equal: perpendicular lines", "Understand",
       "Students find that four equal angles at a crossing are each 90 degrees, and name such lines perpendicular, "
       "whatever their tilt.",
       textbook=["Can you draw a pair of intersecting lines such that all four angles are equal? Can you figure out "
                 "what will be the measure of each angle?",
                 "If two lines intersect and all four angles are equal, then each angle must be a right angle (90°).",
                 "Perpendicular lines are a pair of lines which intersect each other at right angles (90°). Lines l "
                 "and m in the figure are perpendicular to each other."],
       teach=["Predict first: if all four angles at a crossing are equal, what must each one be?",
              "A linear pair adds to 180°, and its two angles are equal, so each is half of 180°.",
              "Perpendicular lines need not be one upright and one flat: tilt both and they stay perpendicular as "
              "long as the angles are 90°."],
       examples=[
           WE("Two lines cross so that all four angles are equal. Find each angle, and say what the lines are "
              "called.",
              ["Two neighbouring angles are a linear pair, so together they are 180°.",
               "They are equal, so each is 180 ÷ 2 = 90.",
               "All four angles are 90°, that is, right angles.",
               "Lines that intersect at right angles are perpendicular, however the pair is tilted."],
              "Each angle is 90°, and the lines are perpendicular", ncert=["5.2.perp_def"])],
       ncert=["5.2.perp_q"], key_terms=["right angle", "perpendicular"], misconceptions=["M_PERP_TILT"], minutes=8),
     DOER("T3.C3", "Practice: measured and reasoned angles", None, "Apply",
          "Students decide which value to trust, a measurement or a reasoned one, and find the angles at a "
          "perpendicular crossing.",
          ["A linear pair adds to 180° by reasoning; a measured pair may be a degree or two off.",
           "Four equal angles at a crossing are 90° each, and the lines are perpendicular."],
          misconceptions=["M_MEASURE_EXACT", "M_PERP_TILT"])]))
