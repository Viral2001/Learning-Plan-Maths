# -*- coding: utf-8 -*-
"""Topics T7 to T11 (module M2: triangles from angles). Book section 7.3."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T7 Two sides and the included angle ============================================
TOPICS.append(TOPIC(
    "T7", "M2", "Two Sides and the Angle Between Them", ["7.3"], "Apply",
    "Students recognise the angle included between two sides, construct a triangle from two sides and the "
    "included angle, and say when no triangle can be built.",
    "Draw one side as the base, make the given angle at one end, mark the second side along the other arm, and "
    "join the ends: a triangle exists whenever the angle is between 0 and 180 degrees.",
    [A("T7.C1", "The included angle", "Understand",
       "Students pick out the angle that lies between two given sides and separate it from an angle that does not.",
       textbook=["7.3 Construction of Triangles When Some Sides and Angles are Given",
                 "We have seen how to construct triangles when their sidelengths are given. Now, we will take up "
                 "constructions where in place of some sidelengths, angle measures are given.",
                 "Two Sides and the Included Angle",
                 "How do we construct a triangle if two sides and the angle included between them are given? Here "
                 "are some examples of measurements showing the included angle.",
                 "4 cm, 60°, 3 cm; 5 cm, 30°, 6 cm; 2 cm, 40°, 3 cm"],
       teach=["Predict first: in the set 4 cm, 60°, 3 cm, which two sides does the 60° angle sit between?",
              "The included angle is the angle between the two given sides, where those two sides meet at a "
              "vertex.",
              "The three examples are: 4 cm, 60°, 3 cm; 5 cm, 30°, 6 cm; and 2 cm, 40°, 3 cm."],
       examples=[
           WE("A triangle has two sides of 6 cm and 5 cm that meet at a corner, and the angle at that corner is "
              "30°. Is 30° the included angle? What if the 30° angle were at the other end of the 6 cm side?",
              ["The two given sides, 6 cm and 5 cm, meet at one corner. The angle at that corner is between "
               "them, so 30° is the included angle.",
               "If the 30° angle were at the other end of the 6 cm side, one of its arms would be the 6 cm side "
               "but the other arm would be a side that is not given.",
               "That angle is not between the two given sides, so it is not the included angle. The measurements "
               "would then be a different kind of data."],
              "Yes, 30° is included when it sits between the 6 cm and 5 cm sides; at the other end it is not",
              ncert=["sas.included"])],
       key_terms=["included angle"], minutes=8),
     A("T7.C2", "Constructing 5 cm, 45° and 4 cm", "Apply",
       "Students construct a triangle ABC with AB = 5 cm, AC = 4 cm and angle A = 45° and write the four steps.",
       textbook=["Construct a triangle ABC with AB = 5 cm, AC = 4 cm and ∠A = 45°.",
                 "Let us take one of the given sides, AB, as the base of the triangle.",
                 "Step 1: Construct a side AB of length 5 cm.",
                 "Step 2: Construct ∠A = 45° by drawing the other arm of the angle.",
                 "Step 3: Mark the point C on the other arm such that AC = 4 cm.",
                 "Step 4: Join BC to get the required triangle."],
       teach=["Predict first: after AB and the 45° arm are drawn, is C anywhere on the arm, or at one exact "
              "place?",
              "C is at one exact place: 4 cm from A along the arm. Joining BC then closes the triangle, and "
              "BC comes out at about 3.6 cm."],
       examples=[
           WE("Construct a triangle ABC with AB = 5 cm, AC = 4 cm and ∠A = 45°.",
              ["Step 1: draw the base AB = 5 cm.",
               "Step 2: place the protractor at A and mark 45° from AB. Draw a long arm through the mark.",
               "Step 3: with the ruler or compass measure 4 cm from A along the arm and mark the point C.",
               "Step 4: join BC.",
               "Measuring BC gives about 3.6 cm, so the sides are 5 cm, 4 cm and about 3.6 cm."],
              "Triangle ABC with AB = 5 cm, AC = 4 cm, ∠A = 45° and BC about 3.6 cm", ncert=["sas.construct"])],
       key_terms=[], minutes=8),
     DOER("T7.C3", "Practice: build a triangle from two sides and the angle between them", None, "Apply",
          "Students construct triangles from two sides and the included angle and say when this cannot be done.",
          ["Draw one side as the base.",
           "Make the angle at one end of the base and mark the second side along the new arm.",
           "Join the free ends to close the triangle."],
          items=[
              FIO("sas.FiOE1", "Figure it Out (two sides and the included angle), Q1",
                  "Construct triangles for the following measurements where the angle is included between the "
                  "sides: (a) 3 cm, 75°, 7 cm (b) 6 cm, 25°, 3 cm (c) 3 cm, 120°, 8 cm",
                  ["Use the same four steps each time: draw the first side as the base, make the angle at one "
                   "end, mark the second side along the new arm, and join.",
                   "(a) AB = 3 cm, ∠A = 75°, AC = 7 cm. Joining BC gives a third side of about 6.9 cm.",
                   "(b) AB = 6 cm, ∠A = 25°, AC = 3 cm. The third side is about 3.5 cm, and the triangle is thin "
                   "because the angle is small.",
                   "(c) AB = 3 cm, ∠A = 120°, AC = 8 cm. The angle is obtuse, and the third side is about "
                   "9.8 cm."],
                  "(a) third side about 6.9 cm, (b) about 3.5 cm, (c) about 9.8 cm; all three triangles can be "
                  "built"),
              FIO("sas.FiOE2", "Figure it Out (two sides and the included angle), Q2",
                  "We have seen that triangles do not exist for all sets of sidelengths. Is there a combination of "
                  "measurements in the case of two sides and the included angle where a triangle is not possible? "
                  "Justify your answer using what you observe during construction.",
                  ["Draw the base and the arm for the angle, then mark the second side along the arm.",
                   "If the angle is 180° the arm points straight along the base, away from it, so the two sides "
                   "lie on one line and joining the ends gives no triangle. Examples: 3 cm, 180°, 7 cm.",
                   "If the angle is more than 180°, for example 4 cm, 210°, 6 cm, the angle on the other side is "
                   "less than 180° and the picture is the same as a smaller angle; a measure of 180° or more "
                   "cannot be the angle of a triangle.",
                   "An angle of 0° puts the arm on top of the base, so there is no triangle either.",
                   "For every angle strictly between 0° and 180° the free ends can be joined, so a triangle "
                   "always exists."],
                  "Yes: no triangle when the included angle is 180° or more (for example 3 cm, 180°, 7 cm or "
                  "4 cm, 210°, 6 cm), or 0°; for any angle strictly between 0° and 180° a triangle exists",
                  ),
          ])]))

# ============================== T8 Two angles and the included side ============================================
TOPICS.append(TOPIC(
    "T8", "M2", "Two Angles and the Side Between Them", ["7.3"], "Apply",
    "Students recognise the side included between two angles and construct a triangle from two angles and the "
    "included side.",
    "Draw the given side as the base, make the two angles at its ends, and the point where the two arms cross is "
    "the third vertex.",
    [A("T8.C1", "Constructing 45°, 5 cm and 80°", "Apply",
       "Students pick out the included side between two angles and construct a triangle with AB = 5 cm, angle A "
       "= 45° and angle B = 80°.",
       textbook=["Two Angles and the Included Side",
                 "In this case, we are given two angles and the side that is a part of both angles, which we call "
                 "the included side. Here are some examples of such measurements:",
                 "40°, 5 cm, 50°; 30°, 4 cm, 45°; 20°, 6 cm, 50°",
                 "Construct a triangle ABC where AB = 5 cm, ∠A = 45° and ∠B = 80°.",
                 "Let us take the given side as the base.",
                 "Step 1: Draw the base AB of length 5 cm.",
                 "Step 2: Draw ∠A and ∠B of measures 45°, and 80° respectively.",
                 "Step 3: The point of intersection of the two new line segments is the third vertex C."],
       teach=["Predict first: the 5 cm side has an angle at each end. Where will the two new arms meet?",
              "The included side is the side that is a part of both angles. In 40°, 5 cm, 50° it is the 5 cm "
              "side.",
              "The point where the two arms cross is C. It is the only point that is on both arms, so the "
              "triangle is fixed: AC is about 6.0 cm and BC about 4.3 cm."],
       examples=[
           WE("Construct a triangle ABC where AB = 5 cm, ∠A = 45° and ∠B = 80°.",
              ["Step 1: draw the base AB = 5 cm. It is the side that both angles share, the included side.",
               "Step 2: at A make an angle of 45° and draw a long arm. At B make an angle of 80° on the same side "
               "and draw a long arm.",
               "Step 3: the two arms cross at C, the third vertex.",
               "Measuring gives AC about 6.0 cm and BC about 4.3 cm, and the angle at C is "
               "180° − 45° − 80° = 55°."],
              "Triangle ABC with AB = 5 cm, ∠A = 45°, ∠B = 80°, AC about 6.0 cm, BC about 4.3 cm",
              ncert=["asa.included", "asa.construct", "asa.mathtalk"])],
       key_terms=["included side"], minutes=8),
     DOER("T8.C2", "Practice: build a triangle from two angles and the side between them", None, "Apply",
          "Students construct a triangle when two angles and the side between them are given, using a ruler, a protractor and a compass accurately.",
          ["Draw the included side as the base.",
           "Make one angle at each end of the base.",
           "The crossing point of the two arms is the third vertex."],
          items=[
              FIO("asa.FiOF1", "Figure it Out (two angles and the included side), Q1",
                  "Construct triangles for the following measurements: (a) 75°, 5 cm, 75° (b) 25°, 3 cm, 60° "
                  "(c) 120°, 6 cm, 30°",
                  ["Draw the given side as the base. Make the first angle at one end and the second at the other "
                   "end. The arms cross at the third vertex.",
                   "(a) 75° + 75° = 150° < 180°, so the arms cross; the third angle is 30° and the other two "
                   "sides are each about 9.7 cm.",
                   "(b) 25° + 60° = 85° < 180°; the third angle is 95° and the other two sides are about 2.6 cm "
                   "and 1.3 cm.",
                   "(c) 120° + 30° = 150° < 180°; the third angle is 30° and the other two sides are about "
                   "10.4 cm and 6 cm."],
                  "All three triangles can be built: (a) third angle 30°, (b) third angle 95°, (c) third angle 30°"),
          ])]))

# ============================== T9 When do two angles fail =====================================================
TOPICS.append(TOPIC(
    "T9", "M2", "When Do Two Angles Fail to Make a Triangle?", ["7.3"], "Analyze",
    "Students find that two angles of 90° or more cannot make a triangle, use a parallel line to find the "
    "smallest second angle that fails when the first is 40°, and state the rule on the sum of two angles.",
    "A triangle exists when the two angles add to less than 180°, and the length of the side between them plays "
    "no part.",
    [A("T9.C1", "Two big angles never meet", "Analyze",
       "Students explain why two base angles that are each 90° or more give arms that never meet.",
       textbook=["Do triangles always exist?",
                 "Do triangles exist for every combination of two angles and their included side? Explore.",
                 "As in the case when we are given all three sides, it turns out that there is not always a "
                 "triangle for every combination of two angles and the included side.",
                 "Find examples of measurements of two angles with the included side where a triangle is not "
                 "possible.",
                 "Let us try to visualise such a situation. Once the base is drawn, try to imagine how the other "
                 "sides should be so that they do not meet.",
                 "Here are some obvious examples.",
                 "If the two angles are greater than or equal to a right angle (90°), then it is clear that a "
                 "triangle is not possible."],
       teach=["Predict first: if both base angles are 90°, will the two arms ever meet?",
              "At 90° the arms stand straight up from the base and stay the same distance apart, so they never "
              "meet. When the angles are bigger than 90°, the arms lean away from each other and spread out.",
              "So two angles that are each 90° or more cannot be the base angles of a triangle, whatever the "
              "length of the base."],
       examples=[
           WE("Say why no triangle can be built from the angles 90°, 5 cm, 90°, and from 100°, 5 cm, 95°.",
              ["Draw the base of 5 cm.",
               "With 90° at both ends the arms are straight up from the base, side by side. They never meet.",
               "With 100° and 95° the arms lean outwards from the base, so they get further apart. They never "
               "meet.",
               "Two angles that are each 90° or more always give arms that do not meet."],
              "No triangle: arms at 90° or more do not meet",
              ncert=["ang.always", "ang.find", "ang.visual", "ang.ninety"])],
       key_terms=[], misconceptions=["M_ANGLE_PAIR"], minutes=8),
     A("T9.C2", "A 40° angle, and the line that never meets", "Analyze",
       "Students use the line through B parallel to the arm at A to find that no triangle exists when the angle at "
       "B is 140° or more.",
       textbook=["Now we make one of the base angles an acute angle, say 40°. What are the possible values that "
                 "the other angle should take so that the lines don't meet?",
                 "It is clear that if the line from B is 'inclined' sufficiently to the right, then it will not "
                 "meet the line l.",
                 "(a) Try to find a possible ∠B (marked in the figure) for this to happen.",
                 "(b) What could be smallest value of ∠B for the lines to not meet?",
                 "The blue line is the line with the least rightward bend that doesn't meet the line 'l'",
                 "Visually, it is clear that the line that creates the smallest ∠B has to be the one parallel to "
                 "l. Let us call this parallel line m.",
                 "Can you tell the actual value of ∠B be in this case? [Hint: Note that AB is the transversal.]",
                 "We have seen that when two lines are parallel, the internal angles on the same side of the "
                 "transversal add up to 180°. So ∠B = 140°.",
                 "So, for what values of ∠B, does a triangle not exist? Does the length AB play any part here?",
                 "From the discussion above, it can be seen that the length AB does not play any part in "
                 "deciding the existence of a triangle. We can say that a triangle does not exist when ∠B is "
                 "greater than or equal to 140°."],
       teach=["Predict first: with ∠A = 40°, if the line from B leans a lot to the right, does it meet the line l?",
              "The line that leans the least and still never meets l is the line m parallel to l. It "
              "makes the smallest angle B that fails.",
              "AB is a transversal of the parallel lines l and m, and the angles on the same side add to 180°: "
              "∠B = 180° − 40° = 140°.",
              "For ∠B less than 140° the line from B meets l and a triangle exists. For ∠B of 140° or more it "
              "does not. The length of AB was never used."],
       examples=[
           WE("The angle at A is 40°. Find the smallest angle at B for which the arms from A and B do not meet, "
              "and say whether the length AB matters.",
              ["Draw AB and the arm from A at 40°. Call the line along this arm l.",
               "The arm from B that does not meet l and leans the least is the line m parallel to l.",
               "AB is a transversal of the parallel lines l and m. The angles on the same side add to 180°.",
               "So ∠B = 180° − 40° = 140°.",
               "Any ∠B of 140° or more does not meet l; any ∠B less than 140° does. The length of AB is not used "
               "anywhere."],
              "∠B = 140°: no triangle when ∠B is 140° or more; the length of AB does not matter",
              ncert=["ang.forty", "ang.parallel"])],
       key_terms=["transversal"], misconceptions=["M_ANGLE_PAIR"], minutes=10),
     DOER("T9.C3", "Practice: which pairs of angles can make a triangle", "two_angle_ray_explorer", "Analyze",
          "Students decide whether two angles can be the angles of a triangle, find an angle that works and one "
          "that fails for a given angle, and state the rule on the sum of the two angles.",
          ["Two angles can be the angles of a triangle exactly when they add up to less than 180°.",
           "For a given angle, the other angle must be less than 180° minus the given angle.",
           "The length of the side between the angles does not matter."],
          items=[
              FIO("ang.FiOG1", "Figure it Out (when two angles fail), Q1",
                  "For each of the following angles, find another angle for which a triangle is (a) possible, "
                  "(b) not possible. Find at least two different angles for each category: (i) 30° (ii) 70° "
                  "(iii) 54° (iv) 144°",
                  ["The other angle must be less than 180° minus the given angle; at that value or more the arms "
                   "do not meet.",
                   "(i) 30°: possible if the other angle is less than 150°, for example 40° or 100°; not possible "
                   "for 150° or more, for example 150° or 170°.",
                   "(ii) 70°: possible below 110°, for example 20° or 100°; not possible at 110° or more, for "
                   "example 110° or 130°.",
                   "(iii) 54°: possible below 126°, for example 30° or 120°; not possible at 126° or more, for "
                   "example 126° or 150°.",
                   "(iv) 144°: possible below 36°, for example 10° or 30°; not possible at 36° or more, for "
                   "example 36° or 90°."],
                  "(i) 30°: possible 40°, 100°; not possible 150°, 170°. (ii) 70°: possible 20°, 100°; not possible "
                  "110°, 130°. (iii) 54°: possible 30°, 120°; not possible 126°, 150°. (iv) 144°: possible 10°, "
                  "30°; not possible 36°, 90°",
                  tool="two_angle_ray_explorer"),
              FIO("ang.FiOG2", "Figure it Out (when two angles fail), Q2",
                  "Determine which of the following pairs can be the angles of a triangle and which cannot: "
                  "(a) 35°, 150° (b) 70°, 30° (c) 90°, 85° (d) 50°, 150°",
                  ["Add the two angles. If the sum is less than 180° the arms meet; if it is 180° or more they do "
                   "not.",
                   "(a) 35° + 150° = 185° is more than 180°: cannot.",
                   "(b) 70° + 30° = 100° is less than 180°: can.",
                   "(c) 90° + 85° = 175° is less than 180°: can.",
                   "(d) 50° + 150° = 200° is more than 180°: cannot."],
                  "(b) and (c) can be the angles of a triangle; (a) and (d) cannot",
                  tool="two_angle_ray_explorer"),
              FIO("ang.FiOG3", "Figure it Out (when two angles fail), Q3",
                  "Like the triangle inequality, can you form a rule that describes the two angles for which a "
                  "triangle is possible? Can the sum of the two angles be used for framing this rule?",
                  ["Take the pairs from the last question: the pairs that work, 70° and 30°, and 90° and 85°, add "
                   "up to 100° and 175°. The pairs that fail add up to 185° and 200°.",
                   "For a first angle of 40° the second angle fails from 140° on, and 40° + 140° = 180°.",
                   "So the sum decides it: when the sum of the two angles is less than 180°, a triangle exists. "
                   "When the sum is 180° or more, there is no triangle.",
                   "Each angle must also be more than 0°."],
                  "A triangle exists when the two angles are each more than 0° and their sum is less than 180°; "
                  "if the sum is 180° or more there is no triangle",
                  tool="two_angle_ray_explorer"),
          ],
          textbook=["Like the triangle inequality, can you form a rule that describes the two angles for which a "
                    "triangle is possible?",
                    "When the sum of two given angles is less than 180°, a triangle exists with these angles. If "
                    "the sum is greater than or equal to 180°, there is no triangle with these angles."])]))

# ============================== T10 The third angle ============================================================
TOPICS.append(TOPIC(
    "T10", "M2", "Finding the Third Angle", ["7.3"], "Apply",
    "Students see that two angles fix the third angle whatever the side between them, and find the third angle "
    "with a line through the top vertex parallel to the base.",
    "The third angle of a triangle depends only on the other two angles: a line through the top vertex parallel to "
    "the base shows 180° − 50° − 70° = 60°.",
    [A("T10.C1", "The same angles with a longer side", "Analyze",
       "Students compare the third angle for angles 60° and 70° with a side of 5 cm and with a side of 7 cm.",
       textbook=["Let us take two angles, say 60° and 70°, whose sum is less than 180°. Let the included side be "
                 "5 cm.",
                 "What could the measure of the third angle be? Does this measure change if the base length is "
                 "changed to some other value, say 7 cm? Construct and find out.",
                 "In general, once the two angles are fixed, does the third angle depend on the included "
                 "sidelength? Try with different pairs of angles and lengths.",
                 "The measurements might show that the sidelength has no effect (or a very small effect) on the "
                 "third angle. With this observation, let us see if we can find the third angle without carrying "
                 "out the construction and measurement.",
                 "Try experimenting with different triangles to see if there is a relation between any two angles "
                 "and the third one. To find this relation, what data will you keep track of and how will you "
                 "organise the data you collect?"],
       teach=["Predict first: if the base is longer, will the third angle be bigger, smaller or the same?",
              "With 60° and 70° the third angle measures 50° for a base of 5 cm and also for a base of 7 cm: "
              "the longer base makes the whole triangle bigger, but the angles stay the same.",
              "To see a relation, make a table with the first angle, the second angle and the measured third "
              "angle, for several pairs. Look at the sum of the three angles in each row."],
       examples=[
           WE("Build a triangle with angles 60° and 70° at the ends of a base of 5 cm, then one with a base of "
              "7 cm, and compare the third angle.",
              ["Base 5 cm: arms at 60° and 70° cross at C. The angle at C measures 50°.",
               "Base 7 cm: arms at 60° and 70° cross at C. The angle at C still measures 50°.",
               "The triangle with the longer base is a bigger copy, with every length scaled up but the same "
               "angles.",
               "In both triangles 60° + 70° + 50° = 180°. The third angle is decided by the two given angles "
               "alone."],
              "The third angle is 50° for both bases; it does not depend on the length of the side",
              ncert=["third.same", "third.data"])],
       key_terms=[], misconceptions=["M_THIRD_ANGLE_SIDE"], minutes=8),
     A("T10.C2", "A parallel line through the top vertex", "Apply",
       "Students find angle A of a triangle with angle B = 50° and angle C = 70° using a line through A parallel "
       "to BC and alternate angles.",
       textbook=["Consider a triangle ABC with ∠B = 50° and ∠C = 70°. Let us see how we can find ∠A without "
                 "construction.",
                 "We saw that the notion of parallel lines was useful to determine that the sum of any two angles "
                 "of a triangle is less than 180°. Parallel lines can be used to find the third angle, ∠BAC as "
                 "well.",
                 "Let us suppose we construct a line XY parallel to BC through vertex A. We can see new angles "
                 "being formed here: ∠XAB, and ∠YAC. What are their values?",
                 "Since the line XY is parallel to BC, ∠XAB = ∠B and ∠YAC = ∠C, because they are alternate angles "
                 "of the transversals AB and AC.",
                 "Therefore, ∠XAB = 50°, and ∠YAC = 70°. Can we find ∠BAC from this?",
                 "We know that ∠XAB, ∠YAC and ∠BAC together form 180°. So ∠XAB + ∠YAC + ∠BAC = 180°, "
                 "50° + ∠BAC + 70° = 180°, 120° + ∠BAC = 180°. Thus, ∠BAC = 60°",
                 "Now construct a triangle (taking BC to be of any suitable length) and verify if this is indeed "
                 "the case."],
       teach=["Predict first: through A, one line is drawn parallel to BC. Which angles at A are equal to ∠B "
              "and ∠C?",
              "The alternate angles ∠XAB and ∠B are equal, and ∠YAC and ∠C are equal, because XY is parallel to "
              "BC and AB and AC are transversals.",
              "The three angles at A on the line XY form a straight angle of 180°. Taking away 50° and 70° leaves "
              "60° for ∠BAC.",
              "Verify by construction: draw BC of any length, make 50° at B and 70° at C, and measure the angle "
              "at A."],
       examples=[
           WE("In triangle ABC, ∠B = 50° and ∠C = 70°. Find ∠A using a line through A parallel to BC.",
              ["Draw the line XY through A parallel to BC.",
               "∠XAB and ∠B are alternate angles, so ∠XAB = 50°. ∠YAC and ∠C are alternate angles, so "
               "∠YAC = 70°.",
               "∠XAB, ∠BAC and ∠YAC together make the straight angle XAY: 50° + ∠BAC + 70° = 180°.",
               "120° + ∠BAC = 180°, so ∠BAC = 60°.",
               "Construct to check: with 50° at B and 70° at C, the angle at A measures 60°."],
              "∠BAC = 60°", ncert=["third.parallel"])],
       key_terms=["alternate angles"], misconceptions=["M_THIRD_ANGLE_SIDE"], minutes=10),
     DOER("T10.C3", "Practice: find the third angle", "angle_sum_parallel", "Apply",
          "Students find the third angle of a triangle from the other two using the parallel line, and use it for "
          "triangles with equal angles.",
          ["Draw a line through the top vertex parallel to the base.",
           "The two alternate angles equal the two base angles.",
           "The three angles on the straight line add up to 180°."],
          items=[
              FIO("third.FiOH1", "Figure it Out (finding the third angle), Q1",
                  "Find the third angle of a triangle (using a parallel line) when two of the angles are: "
                  "(a) 36°, 72° (b) 150°, 15° (c) 90°, 30° (d) 75°, 45°",
                  ["Draw a line through the third vertex parallel to the side between the two given angles; its "
                   "two alternate angles are equal to the two given angles.",
                   "The third angle is what remains of 180°.",
                   "(a) 180° − 36° − 72° = 72°. (b) 180° − 150° − 15° = 15°.",
                   "(c) 180° − 90° − 30° = 60°. (d) 180° − 75° − 45° = 60°."],
                  "(a) 72° (b) 15° (c) 60° (d) 60°", tool="angle_sum_parallel"),
              FIO("third.FiOH2", "Figure it Out (finding the third angle), Q2",
                  "Can you construct a triangle all of whose angles are equal to 70°? If two of the angles are "
                  "70° what would the third angle be? If all the angles in a triangle have to be equal, then what "
                  "must its measure be? Explore and find out.",
                  ["Three angles of 70° add up to 3 × 70° = 210°, which is more than 180°. So no triangle has "
                   "all angles equal to 70°.",
                   "If two angles are 70°, the third is 180° − 70° − 70° = 40°.",
                   "If all three angles are equal and each is x, then 3x = 180°, so x = 60°."],
                  "No triangle has three angles of 70°; two angles of 70° give a third of 40°; equal angles must "
                  "each be 60°", tool="angle_sum_parallel"),
              FIO("third.FiOH3", "Figure it Out (finding the third angle), Q3 (Try This)",
                  "Here is a triangle in which we know ∠B = ∠C and ∠A = 50°. Can you find ∠B and ∠C?",
                  ["The three angles add up to 180°, so ∠B + ∠C = 180° − 50° = 130°.",
                   "∠B and ∠C are equal, so each is half of 130°.",
                   "130° ÷ 2 = 65°."],
                  "∠B = ∠C = 65°", tool="angle_sum_parallel"),
          ])]))

# ============================== T11 Angle sum and exterior angles ==============================================
TOPICS.append(TOPIC(
    "T11", "M2", "Angle Sum and Exterior Angles", ["7.3"], "Analyze",
    "Students prove that the three angles of a triangle add up to 180°, verify it by paper folding, and show "
    "that an exterior angle equals the sum of the two opposite interior angles.",
    "The three angles of any triangle add up to 180°, and the exterior angle at a vertex is the sum of the two "
    "interior angles that are not next to it.",
    [A("T11.C1", "The angles of a triangle add up to 180°", "Analyze",
       "Students prove the angle sum property with a line through a vertex parallel to the opposite side and "
       "verify it by folding a paper triangle.",
       textbook=["Angle Sum Property",
                 "What can we say about the sum of the angles of any triangle?",
                 "Consider a triangle ABC. To find the sum of its angles, we can use the same method of drawing a "
                 "line parallel to the base: construct a line through A that is parallel to BC.",
                 "We need to find ∠A + ∠B + ∠C. We know that ∠B = ∠XAB, ∠C = ∠YAC. So, ∠A + ∠B + ∠C = ∠A + "
                 "∠XAB + ∠YAC = 180° as together they form a straight angle.",
                 "Thus we have proved that the sum of the three angles in any triangle is 180°! This rather "
                 "surprising result is called the angle sum property of triangles.",
                 "Take some time to reflect upon how we figured out the angle sum property. In the beginning, the "
                 "relationship between the third angle and the other two angles was not at all clear. However, a "
                 "simple idea of drawing a line parallel to the base through the top vertex suddenly made the "
                 "relationship obvious. This ingenious idea can be found in a very influential book in the "
                 "history of mathematics called 'The Elements'. This book is attributed to the Greek "
                 "mathematician Euclid, who lived around 300 BCE.",
                 "This solution is yet another example of how creative thinking plays a key role in mathematics!",
                 "There is a convenient way of verifying the angle sum property by folding a triangular cut-out of "
                 "a paper. Do you see how this shows that the sum of the angles in this triangle is 180°?"],
       teach=["Predict first: if the three angles of any triangle are measured and added, what total do you "
              "expect?",
              "Draw XY through A parallel to BC. ∠XAB = ∠B and ∠YAC = ∠C, and ∠XAB, ∠A and ∠YAC form a straight "
              "angle, so ∠A + ∠B + ∠C = 180°.",
              "Euclid used this idea in his book The Elements, around 300 BCE.",
              "Paper fold: fold the three corners of a paper triangle to meet at one point on the base. The three "
              "angles fit together along a straight edge, which is 180°."],
       examples=[
           WE("Prove that the three angles of a triangle ABC add up to 180°, and check it with the paper fold.",
              ["Draw a line XY through A parallel to BC.",
               "Alternate angles give ∠XAB = ∠B and ∠YAC = ∠C.",
               "∠XAB, ∠A and ∠YAC together make a straight angle: ∠XAB + ∠A + ∠YAC = 180°.",
               "Replace ∠XAB by ∠B and ∠YAC by ∠C: ∠B + ∠A + ∠C = 180°.",
               "Paper fold: fold the three corners of a paper triangle in so that they meet at one point on "
               "the base. The three angles sit side by side along the straight base, which is 180°."],
              "∠A + ∠B + ∠C = 180° for every triangle",
              ncert=["sum.property", "sum.history", "sum.fold"])],
       key_terms=["angle sum property"], minutes=10),
     A("T11.C2", "Exterior angles", "Analyze",
       "Students find an exterior angle of a triangle and show that it equals the sum of the two opposite interior "
       "angles.",
       textbook=["Exterior Angles",
                 "The angle formed between the extension of a side of a triangle and the other side is called an "
                 "exterior angle of the triangle. In this figure, ∠ACD is an exterior angle.",
                 "Find ∠ACD, if ∠A = 50°, and ∠B = 60°.",
                 "From the angle sum property, we know that 50° + 60° + ∠ACB = 180°. 110° + ∠ACB = 180°. So, "
                 "∠ACB = 70°. So, ∠ACD = 180° − 70° = 110°, since, ∠ACB and ∠ACD together form a straight angle.",
                 "Find the exterior angle for different measures of ∠A and ∠B. Do you see any relation between "
                 "the exterior angle and these two angles?",
                 "[Hint: From angle sum property, we have ∠A + ∠B + ∠ACB = 180°.] We also have ∠ACD + ∠ACB = "
                 "180°, since they form a straight angle. What does this show?"],
       teach=["Predict first: if ∠A = 50° and ∠B = 60°, is the exterior angle at C more or less than 100°?",
              "From the angle sum property ∠ACB = 70°, and ∠ACD = 180° − 70° = 110°.",
              "Since ∠A + ∠B + ∠ACB = 180° and ∠ACD + ∠ACB = 180°, the two sums are equal, and taking away ∠ACB "
              "from both leaves ∠ACD = ∠A + ∠B.",
              "Check: 50° + 60° = 110°. The exterior angle is the sum of the two interior angles that are not "
              "next to it."],
       examples=[
           WE("Find ∠ACD, if ∠A = 50° and ∠B = 60°, and then try ∠A = 35° and ∠B = 45°. What do you notice?",
              ["First case: 50° + 60° + ∠ACB = 180°, so ∠ACB = 70°.",
               "∠ACB and ∠ACD form a straight angle, so ∠ACD = 180° − 70° = 110°.",
               "Second case: 35° + 45° + ∠ACB = 180°, so ∠ACB = 100°, and ∠ACD = 180° − 100° = 80°.",
               "In the first case 110° = 50° + 60°; in the second case 80° = 35° + 45°.",
               "The exterior angle equals the sum of the two interior angles that are not next to it."],
              "∠ACD = 110°, and in general an exterior angle is the sum of the two opposite interior angles",
              ncert=["ext.def", "ext.ex", "ext.relation"])],
       key_terms=["exterior angle"], misconceptions=["M_EXTERIOR_ANGLE"], minutes=10),
     DOER("T11.C3", "Practice: use the angle sum and the exterior angle", "exterior_angle_explorer", "Apply",
          "Students find a missing angle with the angle sum, find an exterior angle, and check that it equals the "
          "sum of the two opposite angles.",
          ["The three angles of a triangle add up to 180°.",
           "An exterior angle and its neighbouring interior angle make a straight angle, 180°.",
           "An exterior angle equals the sum of the two opposite interior angles."])]))
