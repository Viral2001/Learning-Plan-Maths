# -*- coding: utf-8 -*-
"""Topics T9 to T12 (modules M5 and M6). Book sections 5.8 and 5.9 and the chapter summary."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T9 Alternate angles ===========================================================
TOPICS.append(TOPIC(
    "T9", "M5", "Alternate Angles", ["5.8"], "Analyze",
    "Students find the alternate angle of a given angle in two moves, prove that alternate angles of parallel "
    "lines are equal, find all eight angles from one, and use alternate angles to test a pair of lines.",
    "The alternate angle is reached through the corresponding angle and then the vertically opposite angle, so "
    "alternate angles of parallel lines are equal.",
    [A("T9.C1", "Reaching the alternate angle in two moves", "Understand",
       "Students find the alternate angle by going to the corresponding angle and then to the vertically opposite "
       "angle, and justify that alternate angles are equal.",
       textbook=["In the figure, ∠d is called the alternate angle of ∠f, and ∠c is the alternate angle of ∠e.",
                 "You can find the alternate angle of a given angle, say ∠f, by first finding the corresponding "
                 "angle of ∠f, which is ∠b and then finding the vertically opposite angle of ∠b, which is ∠d.",
                 "Activity 6: If ∠f is 120° what is the measure of its alternate angle ∠d?",
                 "We can find the measure of ∠d if we know ∠b because they are vertically opposite angles. Remember, "
                 "vertically opposite angles are equal. What is the measure of ∠b? It is 120° because it is the "
                 "corresponding angle of ∠f. So, ∠d also measures 120°.",
                 "In fact, ∠f = ∠b irrespective of the measure of ∠f. Why? Because ∠b is the corresponding angle of "
                 "∠f. Similarly, ∠b = ∠d irrespective of the measure of ∠b. Why? Because ∠d is the vertically "
                 "opposite angle of ∠b. So, it must always be the case that ∠f = ∠d.",
                 "Using our understanding of corresponding angles without any measurements, we have justified that "
                 "alternate angles are always equal.",
                 "Alternate angles formed by a transversal intersecting a pair of parallel lines are always equal to "
                 "each other."],
       teach=["Predict first: f is 120°; is its alternate angle d also 120°, or is it 60°?",
              "Eight angles a to h are named: a, b at the top and d, c below them at the upper crossing; e, f at "
              "the top and h, g below them at the lower crossing.",
              "Two moves: f to b (corresponding, same corner), then b to d (vertically opposite). Neither move "
              "changes the size."],
       examples=[
           WE("Lines l and m are parallel and t is a transversal. The angles a, b, d, c are at the upper crossing "
              "(a top left, b top right, d bottom left, c bottom right), and e, f, h, g are in the same corners at "
              "the lower crossing. If f is 120°, find its alternate angle d.",
              ["First move: b is the corresponding angle of f, so b = 120°.",
               "Second move: d is the vertically opposite angle of b, so d = 120°.",
               "So f = d = 120°, whatever the size of f.",
               "Alternate angles are equal when the lines are parallel."],
              "d = 120°, so alternate angles of parallel lines are equal",
              ncert=["5.8.act6"])],
       ncert=["5.8.alt"], key_terms=["alternate angles"], misconceptions=["M_ALT_SUM", "M_WRONG_PAIR"], minutes=10),
     A("T9.C2", "All eight angles from one", "Apply",
       "Students find all the other angles at a transversal of parallel lines from one given angle.",
       textbook=["Example 1: Parallel lines l and m are intersected by the transversal t. If ∠6 is 135°, what are "
                 "the measures of the other angles?",
                 "Solution: ∠6 is 135°, so ∠2 is also 135°, because it is the corresponding angle of ∠6 and the "
                 "lines l and m are parallel.",
                 "∠8 is 135°, because it is the vertically opposite angle of ∠6. ∠4 is 135° because it is the "
                 "corresponding angle of ∠8. ∠2 is 135° because it is the vertically opposite angle of ∠4. So, "
                 "∠2, ∠4, ∠6, and ∠8 are all 135°.",
                 "∠5 and ∠6 are a linear pair, together they measure 180°. If ∠6 is 135°, then ∠5 is 180 − 135 = "
                 "45°. We can similarly find out that ∠1, ∠3, and ∠7 measure 45°."],
       teach=["Predict first: one angle is 135°; how many of the eight are 135° and how many are smaller?",
              "Use only the three facts so far: corresponding angles are equal, vertically opposite angles are "
              "equal, a linear pair adds to 180°.",
              "Four angles are 135° and the other four are 45°."],
       examples=[
           WE("Lines l and m are parallel and t is a transversal. The angles 1, 2, 3, 4 go round the crossing with "
              "l and 5, 6, 7, 8 round the crossing with m in the same corners, so 2 and 6 correspond, and 6 and 8 "
              "are vertically opposite, and 5 and 6 are a linear pair. If angle 6 is 135°, find the other angles.",
              ["Angle 2 is the corresponding angle of 6, so angle 2 is 135°.",
               "Angle 8 is vertically opposite to 6, so it is 135°; angle 4 is the corresponding angle of 8, so it is 135°.",
               "So angles 2, 4, 6 and 8 are all 135°.",
               "Angles 5 and 6 are a linear pair, so angle 5 is 180 − 135 = 45.",
               "In the same way angles 1, 3 and 7 are 45°."],
              "Angles 2, 4, 6 and 8 are 135°; angles 1, 3, 5 and 7 are 45°", ncert=["5.8.ex1"])],
       key_terms=["alternate angles"], misconceptions=["M_ALT_SUM"], minutes=8),
     A("T9.C3", "Testing a pair of lines with an alternate angle", "Analyze",
       "Students decide whether two lines are parallel by comparing the corresponding angle found by reasoning "
       "with the given one.",
       textbook=["Example 2: Lines l and m are intersected by the transversal t. If ∠a is 120° and ∠f is 70°, are "
                 "lines l and m parallel to each other?",
                 "Solution: ∠a is 120°, so ∠b is 60° because ∠a and ∠b form a linear pair. ∠b is a corresponding "
                 "angle of ∠f. If l and m are parallel, ∠b should be equal to ∠f, however, they are not equal.",
                 "Therefore, lines l and m are not parallel to each other as the corresponding angles formed by the "
                 "transversal t are not equal to each other."],
       teach=["Predict first: a is 120° and f is 70°; from these two, can we tell whether the lines are parallel?",
              "Bring both angles to the same corner by reasoning, then compare.",
              "Equal corresponding angles would give parallel lines; unequal ones tell us the lines are not parallel."],
       examples=[
           WE("Lines l and m are cut by a transversal t, with the angles a, b, d, c at the upper crossing and e, f, "
              "h, g in the same corners at the lower crossing. The angle a is 120° and the angle f is 70°. Are l "
              "and m parallel?",
              ["a and b are a linear pair, so b = 180 − 120 = 60.",
               "b and f are corresponding angles. If l and m were parallel, b would be equal to f.",
               "But b = 60° and f = 70°, which are not equal, as 70 − 60 = 10.",
               "So l and m are not parallel."],
              "No: the corresponding angles are 60° and 70°, which are not equal", ncert=["5.8.ex2"])],
       key_terms=["corresponding angles"], misconceptions=["M_LOOKS_PARALLEL"], minutes=8),
     DOER("T9.C4", "Practice: alternate angles", "alternate_chaser", "Apply",
          "Students chase the alternate angle through the corresponding and vertically opposite angles, and use it "
          "to find angles and test lines.",
          ["Alternate angle: go to the corresponding angle, then to the vertically opposite angle.",
           "Alternate angles of parallel lines are equal; they do not add to 180°.",
           "If the angles reached do not match, the lines are not parallel."],
          misconceptions=["M_ALT_SUM", "M_WRONG_PAIR"])]))

# ============================== T10 Interior angles ===========================================================
TOPICS.append(TOPIC(
    "T10", "M5", "Interior Angles on the Same Side", ["5.8"], "Analyze",
    "Students show that interior angles on the same side of a transversal across parallel lines add to 180 "
    "degrees, use the rule and the earlier angle facts to find unknown angles in figures, and reason in a "
    "four-sided figure.",
    "Interior angles on the same side add to 180 degrees, because one is a linear pair of the corresponding angle "
    "of the other; with the earlier facts this finds the angles in a figure.",
    [A("T10.C1", "Interior angles on the same side", "Understand",
       "Students find an interior angle on the same side from a given one, and state and justify that the two add "
       "to 180 degrees.",
       textbook=["Example 3: Parallel lines l and m are intersected by the transversal t. If ∠3 is 50°, what is the "
                 "measure of ∠6?",
                 "Solution: ∠3 is 50°; therefore, ∠2 is 130°, because ∠2 and ∠3 form a linear pair, and linear "
                 "pairs always add up to 180°. ∠2 and ∠6 are corresponding angles, and they need to be equal since "
                 "lines l and m are parallel. So, ∠6 is 130°.",
                 "Angles ∠3 and ∠6 are called interior angles.",
                 "Is there a relation between ∠3 and ∠6? You could try to find the relationship by taking different "
                 "values for ∠3 and see what ∠6 is. Once you find a relation, try to justify it or prove that this "
                 "relation holds always. You will find that the sum of the interior angles on the same side of the "
                 "transversal always add up to 180°."],
       teach=["Predict first: angle 3 is 50°; is its interior partner on the same side 50°, or 130°?",
              "Interior angles sit between the two lines; here the two on the same side of the transversal.",
              "Try 70°, 90° and 110° for angle 3 and see what angle 6 is each time: the sum is always 180°.",
              "Proof: angle 3 and angle 2 make a linear pair, so they add to 180; angle 2 equals angle 6, so "
              "angle 3 and angle 6 add to 180."],
       examples=[
           WE("Lines l and m are parallel and t is a transversal. The angles 1, 2, 3, 4 go round the crossing with "
              "l and 5, 6, 7, 8 round the crossing with m in the same corners, with 2 and 6 corresponding and 2 and "
              "3 a linear pair. If angle 3 is 50°, find angle 6, and say what relation angles 3 and 6 have.",
              ["Angles 2 and 3 are a linear pair, so angle 2 is 180 − 50 = 130.",
               "Angles 2 and 6 are corresponding angles of parallel lines, so angle 6 is 130°.",
               "Angles 3 and 6 are interior angles on the same side, and 50 + 130 = 180.",
               "This holds for any angle 3: angle 3 and angle 2 add to 180, and angle 2 equals angle 6, so angle 3 and angle 6 add to 180."],
              "Angle 6 = 130°; interior angles on the same side add to 180°",
              ncert=["5.8.ex3"])],
       ncert=["5.8.interior"], key_terms=["interior angles"], misconceptions=["M_INTERIOR_EQUAL"], minutes=8),
     A("T10.C2", "Angles in a four-sided figure with parallel sides", "Analyze",
       "Students use the same-side interior rule on two pairs of parallel sides to find the angles of a "
       "four-sided figure.",
       textbook=["Example 4: Line segment AB is parallel to CD and AD is parallel to BC. ∠DAC is 65° and ∠ADC is "
                 "60°. What are the measures of angles ∠CAB, ∠ABC, and ∠BCD?",
                 "Solution: Let us observe the parallel lines AB and CD. AD is a transversal of these two lines.",
                 "We know that the sum of the interior angles formed by a transversal on a pair of parallel lines "
                 "adds up to 180°. So ∠ADC + ∠DAB = 180°. 60° + ∠DAB = 180°. So ∠DAB = 120°.",
                 "Can we find ∠CAB from this? ∠DAB = ∠DAC + ∠CAB. So 120° = 65° + ∠CAB. So ∠CAB = 55°.",
                 "Let us observe the parallel line segments AD and BC. They are intersected by a transversal CD. "
                 "So, ∠ADC + ∠BCD = 180°, because they are interior angles on the same side of the transversal. "
                 "Since ∠ADC is given as 60°, ∠BCD = 120°. Similarly, we find ∠ABC = 60°."],
       teach=["Predict first: the figure has two pairs of parallel sides and the angle at D is 60°; which other "
              "angle must be 120°?",
              "Treat one side as a transversal of the other two sides, and use the rule for interior angles on the "
              "same side.",
              "The 120° at A is split by the diagonal AC into 65° and the angle we want."],
       examples=[
           WE("A four-sided figure ABCD has AB parallel to CD and AD parallel to BC, and a line from A to C inside "
              "it. Angle DAC is 65° and angle ADC is 60°. Find angles DAB, CAB, BCD and ABC.",
              ["AB is parallel to CD and AD is a transversal, so angle ADC + angle DAB = 180°.",
               "60 + DAB = 180, so angle DAB = 180 − 60 = 120°.",
               "Angle DAB = angle DAC + angle CAB, so 120 = 65 + CAB, and angle CAB = 120 − 65 = 55°.",
               "AD is parallel to BC and CD is a transversal, so angle ADC + angle BCD = 180°, and angle BCD = "
               "180 − 60 = 120°.",
               "In the same way, angle ABC = 60°."],
              "Angle DAB = 120°, angle CAB = 55°, angle BCD = 120°, angle ABC = 60°",
              ncert=["5.8.ex4"])],
       key_terms=["interior angles"], misconceptions=["M_INTERIOR_EQUAL"], minutes=10),
     DOER("T10.C3", "Practice: finding angles in figures", "same_side_lab", "Apply",
          "Students find unknown angles in figures of parallel lines using corresponding, alternate, "
          "vertically opposite and same-side interior angles, and linear pairs.",
          ["Corresponding and alternate angles of parallel lines are equal.",
           "Interior angles on the same side add to 180°.",
           "A right angle is 90° and a straight angle is 180°; when a figure looks hard, add a line parallel to "
           "the given ones."],
          items=[
              FIO("5.8.FiO1", "Figure it Out (angles), Q1",
                  "Find the angles marked below. In every figure two or three lines are parallel and a transversal "
                  "crosses them. (a) An angle of 48° and a are corresponding angles. (b) An angle of 52° and b are "
                  "alternate angles. (c) An angle of 99° is shown, and c is its interior partner on the same side. "
                  "(d) An angle of 81° is shown, and d is its interior partner on the same side. (e) Angles of 97°, "
                  "83° and 69° are shown, and e is the alternate angle of the 69°. (f) An angle of 132° is shown, "
                  "and f is its interior partner on the same side. (g) Angles of 58° and 122° are shown on the "
                  "right line, and g is the angle in the matching lower left corner at the left line, "
                  "corresponding to the 122°. (h) Angles of 75° and 120° are shown, and h is the alternate angle "
                  "of the 75°. (i) Between two slanted parallel lines, the angles 54°, 70° and 56° lie along one "
                  "straight line, and i is the alternate angle of the 54° across the steep line. (j) Three "
                  "parallel lines are crossed by a line, with angles of 27°, 97° and 124° shown; j is the "
                  "vertically opposite angle of the corresponding angle of the 97°.",
                  ["(a) Corresponding angles of parallel lines are equal, so a = 48.",
                   "(b) Alternate angles of parallel lines are equal, so b = 52.",
                   "(c) Interior angles on the same side add to 180, so c = 180 − 99 = 81.",
                   "(d) In the same way, d = 180 − 81 = 99.",
                   "(e) Alternate angles are equal, so e = 69. The 97° and 83° are not needed.",
                   "(f) Interior angles on the same side add to 180, so f = 180 − 132 = 48.",
                   "(g) The 122° and 58° form a linear pair, 122 + 58 = 180, and g corresponds to the 122°, so "
                   "g = 122.",
                   "(h) Alternate angles are equal, so h = 75. The 120° is not needed.",
                   "(i) Alternate angles are equal, so i = 54. The 70° and 56° are not needed, but they fit with "
                   "i on a straight line: 54 + 70 + 56 = 180.",
                   "(j) The corresponding angle of 97° is 97°, and its vertically opposite angle is 97°, so "
                   "j = 97. The 27° and 124° are not needed."],
                  "a = 48°, b = 52°, c = 81°, d = 99°, e = 69°, f = 48°, g = 122°, h = 75°, i = 54°, j = 97°",
                  tool="same_side_lab"),
              FIO("5.8.FiO2", "Figure it Out (angles), Q2",
                  "Find the angle represented by a in each figure. (i) Two parallel lines with an angle of 42°; a "
                  "is its interior partner on the same side; a separate angle of 100° is shown but not needed. "
                  "(ii) Two parallel lines with an angle of 62°; a is the other angle of the linear pair of the "
                  "corresponding angle of the 62°. (iii) An angle of 110° contains an angle of 35°; the rest of "
                  "the 110° is the corresponding angle of the angle that makes a linear pair with a. (iv) An angle "
                  "of 67° and a make a right angle between a transversal and a line perpendicular to the "
                  "parallels.",
                  ["(i) Interior angles on the same side add to 180, so a = 180 − 42 = 138. The 100° is not "
                   "needed.",
                   "(ii) The corresponding angle of the 62° is 62°, and a is a linear pair of it, so a = 180 − 62 = "
                   "118.",
                   "(iii) The rest of the 110° is 110 − 35 = 75, which is the corresponding angle next to a on a "
                   "straight line, so a = 180 − 75 = 105.",
                   "(iv) The 67° and a fill a right angle, so a = 90 − 67 = 23."],
                  "(i) 138°, (ii) 118°, (iii) 105°, (iv) 23°"),
              FIO("5.8.FiO3", "Figure it Out (angles), Q3",
                  "In the figures, what angles do x and y stand for? (i) Two parallel lines and a transversal: a "
                  "right angle is split into 65° and x, and y makes a linear pair with x. (ii) Two lines cross "
                  "above a lower line; the lower line makes 78° with one of them and 53° with the other, and x is "
                  "the angle between the two upper lines.",
                  ["(i) x and 65° fill a right angle, so x = 90 − 65 = 25.",
                   "(i) y and x form a linear pair, so y = 180 − 25 = 155.",
                   "(ii) The two lines make angles of 78° and 53° with the lower line, so the angle between them "
                   "is the difference: x = 78 − 53 = 25."],
                  "(i) x = 25°, y = 155°; (ii) x = 25°"),
              FIO("5.8.FiO4", "Figure it Out (angles), Q4",
                  "Angle ABC is 45° and angle IKJ is 78°. The points D, E and G lie on a straight line, and the "
                  "rays EH and EF go up from E on one side, in the order G, H, F, D. The sides of angle GEH are "
                  "parallel to the sides of angle ABC, and the sides of angle FED are parallel to the sides of "
                  "angle IKJ. Find angle GEH, angle HEF and angle FED.",
                  ["Angle GEH is the corresponding angle of angle ABC, and then its vertically opposite angle, so "
                   "angle GEH = 45°.",
                   "Angle FED corresponds to angle IKJ in the same way, so angle FED = 78°.",
                   "G, E and D lie on a straight line, so the three angles GEH, HEF and FED add to 180°.",
                   "Angle HEF = 180 − 45 − 78 = 57°."],
                  "Angle GEH = 45°, angle HEF = 57°, angle FED = 78°"),
              FIO("5.8.FiO5", "Figure it Out (angles), Q5",
                  "AB is parallel to CD, and CD is parallel to EF. Also, EA is perpendicular to AB. The angle BEF "
                  "is 55°. Here x is the angle at B between BE and the part of AB going down from B, and y is the angle that corresponds to x where BE "
                  "crosses CD. Find the values of x and y.",
                  ["AB and EF are parallel and BE is a transversal. The angle x at B and the angle BEF at E are "
                   "interior angles on the same side, so they add to 180°.",
                   "x = 180 − 55 = 125.",
                   "y is the corresponding angle of x where BE crosses the parallel line CD, so y = 125.",
                   "The perpendicular EA is not needed for the values of x and y."],
                  "x = 125° and y = 125°"),
              FIO("5.8.FiO6", "Figure it Out (angles), Q6",
                  "What is the measure of angle NOP? The lines LM and PQ are parallel. At M the angle between ML and MN is 40°, at N "
                  "the angle between NM and NO is 96°, and at P the angle between PO and PQ is 52°. Hint: draw lines parallel to LM and PQ through the points N and "
                  "O.",
                  ["Draw a line through N and a line through O, both parallel to LM and PQ.",
                   "The line through N makes 40° with NM, an alternate angle of the 40° at M. The rest of the 96° at N is 96 − 40 = 56, between that line and NO.",
                   "The two new lines are parallel, so the angle at O between ON and the line through O is also 56°, an alternate angle. The angle between OP and that line is 52°, an alternate angle of the 52° at P.",
                   "Angle NOP is that 56° together with the 52°.",
                   "56 + 52 = 108, so angle NOP = 108°."],
                  "Angle NOP = 108°"),
          ],
          misconceptions=["M_ALT_SUM", "M_INTERIOR_EQUAL", "M_WRONG_PAIR"])]))

# ============================== T11 Parallel illusions ========================================================
TOPICS.append(TOPIC(
    "T11", "M6", "Parallel Illusions", ["5.9"], "Evaluate",
    "Students check that lines which look bent are straight and parallel by using a ruler and a measured gap, and say what in the picture fools the eye.",
    "Pictures can make straight, parallel lines look bent; a ruler and the angle tests decide.",
    [A("T11.C1", "Lines that look bent", "Evaluate", "",
       textbook=["There do not seem to be any parallel lines here. Or, are there?",
                 "What causes these illusions?"],
       teach=["Three pictures: upright lines through a burst of spokes, short slanted strokes in a brick pattern, "
              "and flat lines through another burst of spokes.",
              "Predict first: do the lines in each picture look straight or bent, and parallel or not?",
              "Test them: lay a ruler along each line, or measure the gap at the top, middle and bottom."],
       examples=[
           WE("In a picture, two upright lines run through a burst of spokes, and they seem to bend outwards in "
              "the middle. How can we check whether they are parallel? What causes the illusion?",
              ["Lay a ruler along each line: it fits the whole line, so each line is straight.",
               "Measure the gap between the two lines at the top, the middle and the bottom: it is the same each "
               "time, so the lines are parallel.",
               "The spokes cut the lines at many different angles, and the eye misjudges the angles, so the lines "
               "seem to bend.",
               "A measurement and a reason can overrule what the eye seems to see."],
              "The lines are straight and parallel; the crossing spokes trick the eye about angles",
              ncert=["5.9.illusions"])],
       key_terms=["illusion"], misconceptions=["M_LOOKS_PARALLEL"], enrichment=True, minutes=6),
     DOER("T11.C2", "Practice: trust the test, not the eye", None, "Evaluate",
          "",
          ["Straight lines can look bent next to slanted strokes or spokes.",
           "A ruler, a measured gap or equal corresponding angles decide whether lines are parallel."],
          enrichment=True)]))

# ============================== T12 Summary ===================================================================
TOPICS.append(TOPIC(
    "T12", "M6", "Summary: Parallel and Intersecting Lines", ["Summary"], "Remember",
    None,
    "Intersecting lines, perpendicular lines, parallel lines, transversals, and the four angle facts of parallel "
    "lines in one place.",
    [A("T12.C1", "What we found about lines and angles", "Remember",
       "Students restate the facts about intersecting, perpendicular and parallel lines and about the angles a "
       "transversal makes.",
       textbook=["Summary",
                 "When two lines intersect, they form four angles. The vertically opposite angles are equal and "
                 "the linear pairs add up to 180°.",
                 "When two lines intersect and the angles formed are 90° (i.e., all four angles are equal), the "
                 "lines are said to be perpendicular to each other.",
                 "When two lines never intersect on a plane, they are called parallel lines.",
                 "When a line t intersects another pair of lines, it is called a transversal and it forms 2 sets "
                 "of 4 angles. Each of the 4 angles in the first set has a corresponding angle in the second set.",
                 "When a transversal intersects a pair of parallel lines, the corresponding angles are equal. When "
                 "a transversal intersects a pair of lines and the corresponding angles are equal, then the pair "
                 "of lines is parallel.",
                 "When a transversal intersects a pair of parallel lines, the alternate angles are equal.",
                 "The interior angles on the same side formed by a transversal intersecting a pair of parallel "
                 "lines always add up to 180°."],
       teach=["Our opening question is settled: two creases on a sheet meet if they lean towards each other, and "
              "stay apart for ever if they are parallel; a transversal with equal corresponding angles decides it.",
              "One chain: linear pairs give vertically opposite angles; equal corresponding angles give parallel "
              "lines; corresponding plus vertically opposite give alternate angles; corresponding plus a linear "
              "pair give interior angles that add to 180°.",
              "Still open for you: why do the illusions fool the eye?"],
       ncert=["summary"], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
