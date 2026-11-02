# -*- coding: utf-8 -*-
"""Topics T4 to T8 (modules M2, M3, M4). Book sections 5.3 to 5.7."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T4 Parallel lines =============================================================
TOPICS.append(TOPIC(
    "T4", "M2", "Parallel Lines", ["5.3"], "Understand",
    "Students describe how pairs of line segments meet or cross, judge whether two segments would meet if they "
    "were extended, and name lines on one plane that never meet as parallel.",
    "Lines on one plane that never meet, however far they run, are parallel; by eye we can only guess, so a sure "
    "test is needed.",
    [A("T4.C1", "Do the segments meet, cross or stay apart?", "Understand",
       "Students describe pairs of segments using the words point, endpoint, midpoint, meet and intersect with "
       "angle measures, and judge whether two segments would meet if extended.",
       textbook=["Describe the way the line segments meet or cross each other in each case, with appropriate "
                 "mathematical words (a point, an endpoint, the midpoint, meet, intersect) and the degree measure of "
                 "each angle.",
                 "For example, line segments FG and FH meet at the endpoint F at an angle 115.3°.",
                 "Are line segments ST and UV likely to meet if they are extended?",
                 "Are line segments OP and QR likely to meet if they are extended?"],
       teach=["Predict first: two segments that share one end, two that cross near their middles, and two that "
              "run side by side, which of them will meet if you extend them?",
              "Use the words: a point where they meet, an endpoint, the midpoint, meet, intersect, and read the "
              "angle.",
              "Segments that lean even a little towards each other meet when extended far enough; segments that keep "
              "the same gap do not seem likely to."],
       examples=[
           WE("Five pairs of segments are drawn. FG and FH share the end F, with 115.3° between them. AB and CD "
              "cross at X, at about 60°, a little past the middle of each. IJ and LM cross at Y, at about 80°, close "
              "to the middle of both. Describe each pair in mathematical words.",
              ["FG and FH meet at the endpoint F, at an angle of 115.3°.",
               "AB and CD intersect at the point X, at an angle of about 60°. X is not the midpoint of either "
               "segment.",
               "IJ and LM intersect at the point Y, at an angle of about 80°. Y is close to the midpoint of both "
               "segments.",
               "The 60° and 80° are measured, so they are close values, as the earlier topic explained."],
              "FG and FH meet at the endpoint F at 115.3°; AB and CD intersect at X at about 60°; IJ and LM "
              "intersect close to both midpoints at about 80°",
              ncert=["5.3.fig55"]),
           WE("Two more pairs are drawn: ST and UV lean towards each other by about 2.5° and look nearly side by "
              "side; OP and QR keep about the same gap along their whole length. Are ST and UV likely to meet if "
              "extended? Are OP and QR?",
              ["ST and UV lean towards each other, so far beyond T and V they would meet, about four lengths of the "
               "segment beyond the ends.",
               "OP and QR keep the same gap from one end to the other, so they are not likely to meet.",
               "By eye we can only guess for lines this close, so we will need a sure test."],
              "ST and UV would meet if extended far enough; OP and QR are not likely to meet",
              ncert=["5.3.extend"])],
       key_terms=["endpoint", "midpoint", "meet", "intersect"], misconceptions=["M_LOOKS_PARALLEL"], minutes=10),
     A("T4.C2", "Parallel lines, in pictures and around us", "Understand",
       "Students define parallel lines, name examples around them, and pick out the parallel pairs in a picture of "
       "segments.",
       textbook=["Here are some examples of lines we notice around us. What is common to the lines in the pictures? "
                 "They do not seem likely to intersect each other. Such lines are called parallel lines.",
                 "Parallel lines are a pair of lines that lie on the same plane, and do not meet however far we "
                 "extend them at both ends.",
                 "Name some parallel lines you can spot in your classroom.",
                 "Parallel lines are often used in artwork and shading.",
                 "Which pairs of lines appear to be parallel in the figure of nine segments?",
                 "Note: It is important that the lines lie on the same plane. A line drawn on a table and a line "
                 "drawn on the board may never meet but that does not make them parallel."],
       teach=["Predict first: the two long edges of a ruler, a railway track, the top and bottom of a window; which "
              "pairs of lines in your classroom stay the same gap apart?",
              "Parallel needs two things together: the lines lie on one plane, and they never meet however far they "
              "are extended in both directions.",
              "A line on a table and a line on the board may never meet but they lie on different planes, so they "
              "are not parallel."],
       examples=[
           WE("Nine segments a to i are drawn on a grid. a, h and i are upright. c and g are flat. d and f lean one "
              "way, each along the diagonal of a square. b and e lean the other way, also along the diagonal of a "
              "square. Which pairs of lines appear to be parallel?",
              ["Upright segments: a, h and i keep the same gap, so they appear parallel to each other.",
               "Flat segments: c and g appear parallel to each other.",
               "Segments leaning one way: d and f appear parallel to each other.",
               "Segments leaning the other way: b and e appear parallel to each other.",
               "A flat segment and an upright one cross; they are not parallel."],
              "a, h and i; c and g; d and f; b and e", ncert=["5.3.fig56"])],
       ncert=["5.3.parallel_def", "5.3.classroom", "5.3.same_plane"], key_terms=["parallel", "plane"],
       misconceptions=["M_PARALLEL_SAME_PLANE", "M_LOOKS_PARALLEL"], minutes=8),
     DOER("T4.C3", "Practice: meet, cross or parallel", None, "Apply",
          "Students sort pairs of lines into meeting, crossing and parallel, and say why a line on a table and a "
          "line on a board are not parallel.",
          ["Lines that meet at a point intersect; lines on one plane that never meet are parallel.",
           "By eye we can only guess, so a sure test is needed."],
          misconceptions=["M_PARALLEL_SAME_PLANE", "M_LOOKS_PARALLEL"])]))

# ============================== T5 Parallel and perpendicular lines in paper folding ===========================
TOPICS.append(TOPIC(
    "T5", "M2", "Folding and Dot Paper", ["5.4"], "Apply",
    "Students find parallel and perpendicular lines in folded paper, count parallel creases, mark parallel and "
    "perpendicular lines with arrow marks and a square, and draw them on dot paper.",
    "Opposite edges of a sheet are parallel, adjacent edges are perpendicular, each fold gives a new parallel or "
    "perpendicular line, and arrow marks and a square show them on a drawing.",
    [A("T5.C1", "Folding a sheet in half again and again", "Understand",
       "Students describe the edges of a sheet, fold it in half horizontally, and count the parallel lines after "
       "each fold.",
       textbook=["Activity 2: Use a plain square sheet of paper (use a newspaper for this activity).",
                 "How would you describe the opposite edges of the sheet? They are parallel to each other.",
                 "How would you describe the adjacent edges of the sheet? The adjacent edges are perpendicular to "
                 "each other. They meet at a point. They form right angles.",
                 "Fold the sheet horizontally in half. A new line is formed. How many parallel lines do you see now? "
                 "How does the new line segment relate to the vertical sides?",
                 "Make one more horizontal fold in the folded sheet. How many parallel lines do you see now?",
                 "What will happen if you do it once more? How many parallel lines will you get? Is there a "
                 "pattern? Check if the pattern extends further, if you make another horizontal fold."],
       teach=["Predict first: after one fold in half, how many parallel lines does the sheet have, counting its "
              "two edges?",
              "The two original edges and the first crease give three parallel lines, and the crease is "
              "perpendicular to the upright sides.",
              "Each fold in half splits every gap into two, so the number of gaps doubles and the lines are one "
              "more than the gaps."],
       examples=[
           WE("A square sheet has two flat edges. Fold it horizontally in half again and again. Count the parallel "
              "lines, including the two edges, after one, two, three and four folds. What is the pattern?",
              ["Opposite edges are parallel, and adjacent edges are perpendicular.",
               "After 1 fold there are 2 gaps, so 2 + 1 = 3 parallel lines.",
               "After 2 folds there are 4 gaps, so 4 + 1 = 5 parallel lines.",
               "After 3 folds there are 8 gaps, so 8 + 1 = 9 parallel lines.",
               "After 4 folds there are 16 gaps, so 16 + 1 = 17 parallel lines.",
               "Every fold doubles the gaps, so the number of lines is 1 more than the gaps, 3, 5, 9, 17, ..."],
              "3, 5, 9 and 17 parallel lines; the gaps double and the lines are one more than the gaps",
              ncert=["5.4.act2_counts"])],
       ncert=["5.4.act2_edges"], key_terms=["parallel", "perpendicular"], misconceptions=["M_ONE_FOLD"], minutes=8),
     A("T5.C2", "Perpendicular and parallel folds", "Apply",
       "Students fold a perpendicular and a line parallel to a diagonal, and decide whether folded creases are "
       "parallel.",
       textbook=["Make a vertical fold in the square sheet. This new vertical line is perpendicular to the previous "
                 "horizontal lines.",
                 "Fold the sheet along a diagonal. Can you find a fold that creates a line parallel to the diagonal "
                 "line?",
                 "Here is another activity for you to try. Fold a square sheet of paper in the middle and unfold it. "
                 "Fold the edges towards the centre line and unfold them. Fold the top right and bottom left corners "
                 "onto the creased line to create triangles. The triangles should not cross the crease lines.",
                 "Are a, b and c parallel to p, q and r respectively? Why or why not?"],
       teach=["Predict first: if you fold a sheet along a diagonal, where would a second crease run to be "
              "parallel to it?",
              "A vertical fold across flat lines meets each of them at 90°.",
              "A fold that puts one corner on the centre of the sheet makes a crease at right angles to the other "
              "diagonal, so it is parallel to the first diagonal."],
       examples=[
           WE("Fold a square sheet along one diagonal. Describe a fold that makes a line parallel to this diagonal "
              "and say why it is parallel.",
              ["Fold the corner that is not on the diagonal onto the centre of the sheet.",
               "The crease is at right angles to the other diagonal, because the fold sends the corner straight "
               "along it to the centre.",
               "The first diagonal is also at right angles to the other diagonal.",
               "Two lines at right angles to the same line are parallel, so the crease is parallel to the diagonal."],
              "Fold a corner onto the centre; the crease is parallel to the diagonal",
              ncert=["5.4.act2_diag"]),
           WE("A square sheet is folded in the middle both ways, the edges are folded to the centre line, and then "
              "two opposite corners are folded onto a centre crease to make triangles. Pairs of creases a and p, b "
              "and q, c and r are marked. Are they parallel?",
              ["a and p lie along folds that run the same way, so they lie on parallel lines.",
               "b and q are both perpendicular to those lines, so b and q are parallel to each other.",
               "c and r are the slanting edges of the two folded triangles. Both triangular folds are made against "
               "the same diagonal direction, so c and r are parallel.",
               "So a is parallel to p, b to q, and c to r."],
              "Yes: a is parallel to p, b to q and c to r", ncert=["5.4.fig58"])],
       key_terms=["crease", "diagonal"], misconceptions=["M_LOOKS_PARALLEL", "M_PERP_TILT"], minutes=10),
     A("T5.C3", "Arrow marks and the square: notation", "Remember",
       "Students mark parallel lines with arrow marks, one kind of arrow for each set, and perpendicular lines "
       "with a square.",
       textbook=["Notations",
                 "In mathematics, we use an arrow mark (>) to show that a set of lines is parallel. If there is more "
                 "than one set of parallel lines, the second set is shown with two arrow marks and so on. "
                 "Perpendicular lines are marked with a square angle between them."],
       teach=["Predict first: if a drawing has two different sets of parallel lines, how could we tell them apart "
              "without using colours?",
              "One arrow mark on each line of the first set, two arrow marks on each line of the second set.",
              "A small square in the corner between two lines shows a right angle."],
       examples=[
           WE("A drawing has two flat parallel lines, two slanting parallel lines, and one upright line that "
              "crosses a flat line at 90°. How are these marked?",
              ["The flat parallel lines are the first set: one arrow mark on each.",
               "The slanting parallel lines are the second set: two arrow marks on each.",
               "The upright line and the flat line are perpendicular: a small square in the corner between them.",
               "The 90° is not written out; the square says it."],
              "One arrow on each flat line, two arrows on each slanting line, and a square at the right angle",
              ncert=["5.4.notation"])],
       key_terms=["arrow mark", "square angle"], minutes=6),
     DOER("T5.C4", "Practice: parallel and perpendicular on dot paper", "dot_paper_studio", "Apply",
          "Students draw perpendicular and parallel lines on dot paper, mark parallel and perpendicular lines, and "
          "explain how they spotted them.",
          ["On dot paper a line has steps across and steps up.",
           "A parallel line repeats the same steps; a perpendicular line swaps the steps and changes one sign.",
           "Mark parallel lines with arrow marks, and a right angle with a square."],
          ncert=["5.4.dot_note"],
          items=[
              FIO("5.4.FiO1", "Figure it Out (parallel and perpendicular lines), Q1",
                  "Draw some lines perpendicular to the lines given on the dot paper. There are two grids, each "
                  "3 dots across and 4 dots up. In the left grid, one segment is flat, 2 steps long, and another "
                  "leans with 2 steps across and 2 steps up. In the right grid, one segment has 2 steps across and "
                  "3 steps down, and another is upright, 2 steps long.",
                  ["Flat segment: an upright segment is perpendicular to it, so draw upright segments between dots "
                   "(0 steps across, some steps up).",
                   "Leaning segment with 2 across and 2 up: swap the steps and change one sign, giving 2 across and "
                   "2 down. Draw leaning segments of 2 across and 2 down.",
                   "Upright segment: a flat segment is perpendicular to it, so draw flat segments between dots.",
                   "Segment with 2 across and 3 down: the perpendicular needs 3 across and 2 up, and the grid is "
                   "only 3 dots, that is 2 steps, across. It cannot be drawn between dots on this grid, so it "
                   "needs a wider grid or a set square.",
                   "Perpendicular lines need not be one flat and one upright: the leaning ones also meet at 90°."],
                  "Upright lines for the flat segment, flat lines for the upright one, lines of 2 across and 2 down "
                  "for the leaning one; the 2-across-3-down segment needs a wider grid",
                  tool="dot_paper_studio"),
              FIO("5.4.FiO2", "Figure it Out (parallel and perpendicular lines), Q2",
                  "Five shapes are drawn on a dot grid. Each corner is given as (across, down) from the top left. "
                  "Shape 1: (0,0), (2,2), (2,4), (3,5), (0,5). Shape 2: (6,1), (10,1), (8,3), (4,3). Shape 3: (5,4), "
                  "(7,6), (7,8), (5,8), (3,6), (5,6). Shape 4: (0,7), (3,7), (0,10). Shape 5: (5,9), (8,9), (11,7), "
                  "(11,11), (5,11). Mark the parallel lines with arrow marks (a single arrow, double arrow and so "
                  "on) and the angle between perpendicular lines with a square. (a) How did you spot the "
                  "perpendicular lines? (b) How did you spot the parallel lines?",
                  ["Shape 1: the side (0,0) to (2,2) and the side (2,4) to (3,5) both go 1 across and 1 down in "
                   "each step, so they are parallel (single arrow). The upright sides (2,2) to (2,4) and (0,5) to "
                   "(0,0) are parallel (double arrow). One right angle, at (0,5), between the upright side and the flat bottom.",
                   "Shape 2: (6,1) to (10,1) and (8,3) to (4,3) are both flat, so parallel (single arrow). (10,1) "
                   "to (8,3) and (4,3) to (6,1) both go 2 across and 2 down, so parallel (double arrow). No right "
                   "angle.",
                   "Shape 3: three pairs. (5,4) to (7,6) with (5,8) to (3,6) (single arrow). (7,6) to (7,8) with "
                   "(5,6) to (5,4) (double arrow). (7,8) to (5,8) with (3,6) to (5,6) (triple arrow). Right angles at "
                   "(7,8) and at (5,6).",
                   "Shape 4: only one right angle, at (0,7), between the flat side and the upright side. No pair of "
                   "parallel sides.",
                   "Shape 5: (5,9) to (8,9) with (11,11) to (5,11) are flat, parallel (single arrow). (11,7) to "
                   "(11,11) with (5,11) to (5,9) are upright, parallel (double arrow). Right angles at (5,9), "
                   "(5,11) and (11,11).",
                   "(a) Perpendicular lines: a flat line and an upright line on the grid meet at a right angle.",
                   "(b) Parallel lines: segments that repeat the same steps across and down, so the gap between "
                   "them stays the same."],
                  "Shape 1: two pairs parallel and one right angle; shape 2: two pairs; shape 3: three pairs and two right angles; shape "
                  "4: one right angle; shape 5: two pairs and three right angles. (a) Flat and upright lines meet "
                  "at 90°. (b) Same steps, same gap"),
              FIO("5.4.FiO3", "Figure it Out (parallel and perpendicular lines), Q3",
                  "On dot paper, draw different sets of parallel lines. The line segments can be of different "
                  "lengths but should have dots as endpoints.",
                  ["Flat sets: draw two or three flat segments in different rows; they can have different "
                   "lengths.",
                   "Upright sets: draw two or three upright segments in different columns.",
                   "Leaning sets: start at different dots and take the same steps, for example 1 across and 1 up, "
                   "or 2 across and 1 up, each time.",
                   "Check each set: the steps are the same, so the lines keep the same gap and are parallel."],
                  "Sets of flat lines, upright lines and leaning lines that repeat the same steps, such as 1 across "
                  "and 1 up, or 2 across and 1 up"),
              FIO("5.4.FiO4", "Figure it Out (parallel and perpendicular lines), Q4",
                  "Using your sense of how parallel lines look, draw lines parallel to the line segments a to h on "
                  "dot paper (13 dots by 13 dots). Taking steps across to the right and then up or down: a is "
                  "1 across, 1 down; b is 2 across, 2 down; c is 3 across, 3 up; d is 4 across, 4 up; e is 1 across, "
                  "3 down; f is 1 across, 6 down; g is 5 across, 2 up; h is 10 across, 3 down. (a) Did you find it "
                  "challenging to draw some of them? (b) Which ones? (c) How did you do it?",
                  ["a, b, c and d lean at the diagonal of a square, so they are easy to copy by eye.",
                   "e, f, g and h have unusual steps, so they are harder to draw by eye.",
                   "Method: count the steps across and up of the given segment, start at a new dot, and take the "
                   "same steps. For e: 1 across and 3 down; for f: 1 across and 6 down; for g: 5 across and 2 up; for "
                   "h: 10 across and 3 down.",
                   "Because the steps are the same, the new segment keeps the same gap and is parallel."],
                  "(a) Yes. (b) The segments e, f, g and h. (c) Count the steps across and up and repeat them from "
                  "another dot"),
              FIO("5.4.FiO5", "Figure it Out (parallel and perpendicular lines), Q5",
                  "Which line is parallel to line a, line b or line c? How do you decide this? Line a, line b and "
                  "line c lean to the right. A steep line meets a at one end and b and c at its other end. The "
                  "angles the steep line makes are about 30° with a, about 29° with c and about 33° with b.",
                  ["Compare the angles the steep line makes: with a it is about 30°, with c about 29°, with b about "
                   "33°.",
                   "The angle with c is close to the angle with a; the angle with b is 3° more.",
                   "Equal corresponding angles mean parallel, so c is the line parallel to a.",
                   "Another way to see it: c stays the same gap from a, while b closes in."],
                  "Line c is parallel to line a, because the angles made with the steep line are about equal, 30° "
                  "and 29°"),
          ],
          misconceptions=["M_LOOKS_PARALLEL", "M_PERP_TILT"])]))

# ============================== T6 Transversals ==============================================================
TOPICS.append(TOPIC(
    "T6", "M3", "A Line Across Two Lines", ["5.5", "5.6"], "Understand",
    "Students name a transversal, count the eight angles it makes, show that at most four of the angles have "
    "different measures, and name the corresponding angles.",
    "A line across two lines is a transversal and makes eight angles in four pairs of vertically opposite angles, "
    "with at most four different measures, and the angles in the same corner at the two crossings are "
    "corresponding.",
    [A("T6.C1", "A transversal and its eight angles", "Understand",
       "Students count the eight angles, find the four vertically opposite pairs, and explain why they cannot "
       "all be different.",
       textbook=["We saw what happens when two lines intersect in different ways. Let us explore what happens when "
                 "one line intersects two different lines.",
                 "In the figure, line t intersects lines l and m. t is called a transversal. Notice that 8 angles "
                 "are formed when a line crosses a pair of lines.",
                 "Is it possible for all the eight angles to have different measurements? Why, why not?",
                 "What about five different angles, 6, 5, 4, 3 and 2?",
                 "Since ∠1 and ∠3 are vertically opposite angles, they are equal. Are there other pairs of "
                 "vertically opposite angles? We can see that there are a total of four pairs of vertically "
                 "opposite angles and in each pair, the angles are equal to each other.",
                 "Thus, when a transversal intersects two lines, it forms eight angles with a maximum of four "
                 "distinct angle measures."],
       teach=["Predict first: a line crosses two lines; how many angles are made, and how many different sizes "
              "could there be?",
              "Each crossing makes four angles, and there are two crossings, so eight angles.",
              "Each crossing gives two pairs of vertically opposite angles, and each pair is equal, so there are "
              "four pairs in all."],
       examples=[
           WE("A transversal t crosses lines l and m. The angles are numbered 1, 2, 3, 4 going round the crossing "
              "with l, and 5, 6, 7, 8 going round the crossing with m in the same way, so that 1 and 3, 2 and 4, 5 "
              "and 7, 6 and 8 are vertically opposite. Can all eight angles have different measures? Can the five "
              "angles 6, 5, 4, 3 and 2 be all different?",
              ["Vertically opposite angles are equal: angle 1 equals angle 3, 2 equals 4, 5 equals 7 and 6 equals 8.",
               "There are four pairs, so there are at most 4 different measures, and all eight cannot differ.",
               "Among the five angles 6, 5, 4, 3 and 2, the angles 2 and 4 are a vertically opposite pair, so they "
               "are equal.",
               "So these five angles cannot all be different."],
              "No: at most four different measures; and 2 and 4 are equal, so the five cannot all be different",
              ncert=["5.5.eight", "5.5.five", "5.5.max4"])],
       ncert=["5.5.transversal"], key_terms=["transversal"], misconceptions=["M_WRONG_PAIR"], minutes=8),
     A("T6.C2", "Corresponding angles", "Understand",
       "Students name the corresponding angle of an angle in a transversal figure, using the same corner at the "
       "other crossing.",
       textbook=["In the figure, we notice that the transversal t forms two sets of angles, one with line l and "
                 "another with line m. There are angles in the first set that correspond to angles in the second "
                 "set based on their position.",
                 "∠1 and ∠5 are called corresponding angles. Similarly, ∠2 and ∠6, ∠3 and ∠7, ∠4 and ∠8 are the "
                 "corresponding angles formed when transversal t intersects lines l and m."],
       teach=["Predict first: angle 1 is the top left corner at the first crossing; which angle sits in the top "
              "left corner at the second crossing?",
              "Corresponding angles are in the same corner at the two crossings.",
              "Each angle in the first set has exactly one corresponding angle in the second set."],
       examples=[
           WE("In the transversal figure, 1, 2, 3, 4 are at the crossing with l and 5, 6, 7, 8 at the crossing "
              "with m, with 1 and 5 in the same corner. Name the corresponding angle of each of 2, 3 and 4.",
              ["The corresponding angle is in the same corner at the other crossing.",
               "2 is in the same corner as 6, so 2 and 6 are corresponding.",
               "3 is in the same corner as 7, so 3 and 7 are corresponding.",
               "4 is in the same corner as 8, so 4 and 8 are corresponding."],
              "2 and 6, 3 and 7, 4 and 8", ncert=["5.6.corr"])],
       key_terms=["corresponding angles"], misconceptions=["M_WRONG_PAIR"], minutes=8),
     DOER("T6.C3", "Practice: the eight angles of a transversal", "transversal_board", "Apply",
          "Students name the corresponding angles in a transversal figure and count the different measures a transversal can make.",
          ["A transversal makes eight angles, with at most four different measures.",
           "Corresponding angles sit in the same corner at the two crossings.",
           "When the two lines are not parallel, corresponding angles are not equal; the next topic shows what "
           "happens when they are."],
          misconceptions=["M_WRONG_PAIR", "M_CORR_ANY"])]))

# ============================== T7 Corresponding angles and parallel lines =====================================
TOPICS.append(TOPIC(
    "T7", "M3", "Corresponding Angles and Parallel Lines", ["5.6"], "Analyze",
    "Students draw a pair of lines with equal corresponding angles and see they are parallel, state that "
    "corresponding angles of parallel lines are equal, and see that lines that are not parallel never give equal "
    "corresponding angles.",
    "Equal corresponding angles make a pair of lines parallel, parallel lines always give equal corresponding "
    "angles, and lines that are not parallel never do.",
    [A("T7.C1", "Drawing lines with equal corresponding angles", "Apply",
       "Students draw a second line making the same angle with a transversal as the first and see that the two "
       "lines are parallel.",
       textbook=["Activity 3: Draw a pair of lines and a transversal such that they form two distinct angles.",
                 "Step 1: Draw a line l and a transversal t intersecting it at point X.",
                 "Step 2: Measure ∠a formed by lines l and t (let us say it is 60°). How many distinct angles have "
                 "formed now? If one angle is 60°, the other angle of the linear pair should be 120°. So, we already "
                 "have two distinct angles. So, when we draw another line intersecting the transversal t we wish to "
                 "form only two angles, 60° and 120°.",
                 "Step 3: Mark a point Y on line t.",
                 "Step 4: Draw a line m through point Y that forms a 60° angle to line t. This can be done either by "
                 "copying ∠a with a tracing paper or you can use a protractor to measure the angles.",
                 "What do you observe about lines l and m? Do they appear to be parallel to each other? Yes, they "
                 "do appear to be parallel to each other. Angles ∠a and ∠b are corresponding angles formed by the "
                 "transversal t on lines l and m. These corresponding angles are equal to each other.",
                 "When the corresponding angles formed by a transversal on a pair of lines are equal to each other, "
                 "then the pair of lines are parallel to each other."],
       teach=["Predict first: if the angle at X is 60° and you draw the same 60° at Y, will the two lines ever "
              "meet?",
              "Copying an angle puts the second line in exactly the same slant as the first.",
              "Equal corresponding angles give parallel lines: that is a way to draw them and a way to test them."],
       examples=[
           WE("A line l and a transversal t meet at X, and the angle a between them is 60°. Describe how to draw "
              "a line m through a point Y on t that is parallel to l, and name the angles that are equal.",
              ["The other angle of the linear pair at X is 180 − 60 = 120, so there are two distinct angles, "
               "60° and 120°.",
               "Mark a point Y on t.",
               "Draw a line m through Y that makes a 60° angle with t, on the same side as a, by copying a on "
               "tracing paper or with a protractor.",
               "The angle b at Y is 60° and a at X is 60°; they are corresponding angles, and they are equal.",
               "So l and m are parallel."],
              "m is parallel to l, since the corresponding angles a and b are both 60°",
              ncert=["5.6.act3"])],
       ncert=["5.6.corr_rule"], key_terms=["corresponding angles"], misconceptions=["M_LOOKS_PARALLEL"], minutes=10),
     A("T7.C2", "Parallel lines give equal corresponding angles", "Analyze",
       "Students check that corresponding angles of a pair of parallel lines are equal, and find the other angles "
       "from one.",
       textbook=["Suppose, we have a transversal intersecting two parallel lines. What can be said about the "
                 "corresponding angles?",
                 "Activity 4: The figure has a pair of parallel lines l and m (what is the notation used in the "
                 "figure to indicate they are parallel?). Line t is the transversal across these two lines. ∠a and "
                 "∠b are corresponding angles. Trace ∠a on a tracing paper. Now place this tracing paper over ∠b "
                 "and see if the angles align exactly. You will observe that the angles match. Check the other "
                 "corresponding angles in the figure using a protractor. Are all the corresponding angles equal to "
                 "each other?",
                 "Corresponding angles formed by a transversal intersecting a pair of parallel lines are always "
                 "equal to each other."],
       teach=["Predict first: the lines are parallel and one angle is 65°; what is its corresponding angle?",
              "The two arrow marks in the figure tell us the lines are parallel.",
              "Trace one angle and slide the tracing over the corresponding one: they match."],
       examples=[
           WE("Lines l and m are parallel, with arrow marks, and t crosses both. The angle a at l is 65°, and b is "
              "its corresponding angle at m. Find b and the other three pairs of corresponding angles.",
              ["a and b are corresponding angles of parallel lines, so b = 65°.",
               "The angle next to a on the straight line is 180 − 65 = 115, and its corresponding angle is also "
               "115°.",
               "So of the four pairs of corresponding angles, two pairs are 65° and two pairs are 115°.",
               "Each pair is equal, because the lines are parallel."],
              "b = 65°; the four pairs of corresponding angles are 65°, 65°, 115° and 115°",
              ncert=["5.6.act4"])],
       key_terms=["parallel", "corresponding angles"], misconceptions=["M_CORR_ANY"], minutes=8),
     A("T7.C3", "Lines that are not parallel", "Analyze",
       "Students see that when two lines are not parallel, no transversal gives equal corresponding angles.",
       textbook=["Activity 5: In the figure, draw a transversal t to the lines l and m such that one pair of "
                 "corresponding angles is equal. You can measure the angles with a protractor.",
                 "Are you finding it hard to draw a transversal such that the corresponding angles are equal?",
                 "When a pair of lines are not parallel to each other, the corresponding angles formed by a "
                 "transversal can never be equal to each other."],
       teach=["Predict first: two lines lean 10° apart; can any transversal make equal corresponding angles?",
              "Whichever way t is drawn, the lines still lean 10° apart, so the two corresponding angles still "
              "differ by 10°.",
              "So equal corresponding angles happen only for parallel lines."],
       examples=[
           WE("Two lines l and m lean 10° apart, so they are not parallel. A transversal t makes 30° with l, and m "
              "leans 10° more towards t than l does, so t makes 20° with m on the matching side. Can the two "
              "corresponding angles be made equal by turning t?",
              ["The corresponding angles are 30° and 20°, and 30 − 20 = 10.",
               "Turn t to make 50° with l; then it makes 40° with m, and 50 − 40 = 10.",
               "Each time the two angles differ by 10°, because the lines lean 10° apart.",
               "So no transversal makes them equal: corresponding angles of lines that are not parallel are never "
               "equal."],
              "No; the corresponding angles always differ by 10°",
              ncert=["5.6.act5"])],
       ncert=["5.6.nonparallel"], key_terms=["parallel", "transversal"], misconceptions=["M_CORR_ANY"], minutes=8),
     DOER("T7.C4", "Practice: parallel or not, by corresponding angles", "corresponding_test", "Apply",
          "Students decide whether two lines are parallel by comparing a pair of corresponding angles, and find "
          "angles when the lines are parallel.",
          ["Equal corresponding angles give parallel lines.",
           "Parallel lines give equal corresponding angles.",
           "Corresponding angles of lines that are not parallel are never equal."],
          misconceptions=["M_LOOKS_PARALLEL", "M_CORR_ANY"])]))

# ============================== T8 Drawing parallel lines =====================================================
TOPICS.append(TOPIC(
    "T8", "M4", "Drawing Parallel Lines", ["5.7"], "Apply",
    "Students draw parallel lines with a ruler and a set square, say why they are parallel, draw a line parallel "
    "to a given line through a given point, and make one by paper folding.",
    "Sliding a set square along a ruler keeps the same angle, so the lines drawn are parallel; folding a "
    "perpendicular to a perpendicular through a point does the same on paper.",
    [A("T8.C1", "Sliding a set square along a ruler", "Apply",
       "Students draw two parallel lines with a set square and a ruler, and justify them by the equal "
       "corresponding angles.",
       textbook=["Can you draw a pair of parallel lines using a ruler and a set square?",
                 "Draw a line l with a scale. By sliding your set square you can make two lines perpendicular to "
                 "line l.",
                 "Are these two lines parallel to each other? How are we sure that they are parallel to each other? "
                 "What angles are formed between these lines and line l?",
                 "Since we used a set square, the angles measure 90°. The position of the lines is different, but "
                 "they make the same angle with l. If line l is seen as a transversal to the two new lines, then "
                 "the corresponding angles measure 90°. As we know these are corresponding angles and they are "
                 "equal, we can be sure that the lines are parallel.",
                 "Draw two more parallel lines using the long side of the set square.",
                 "How do you know these two lines are parallel? Can you check if the corresponding angles are "
                 "equal?",
                 "Note: Encourage checking the equality of corresponding angles both by using the tracing method "
                 "and using protractors to measure the angles. Pay attention to the language used to make the "
                 "relationship between corresponding angles and parallel lines. Equality of corresponding angles "
                 "is both necessary and sufficient for the pair of lines to be parallel to each other."],
       teach=["Predict first: you slide a set square along a ruler and draw along one edge twice; will the two "
              "lines be parallel?",
              "The set square does not turn while it slides, so it makes the same angle with the ruler every time.",
              "Equal corresponding angles are both a test and a guarantee: they give parallel lines, and parallel "
              "lines give them."],
       examples=[
           WE("Draw a line l with a ruler. Slide a set square along l and draw two lines along its upright edge. "
              "Are the two lines parallel? Which angles prove it?",
              ["The upright edge of the set square makes a 90° angle with l each time it is drawn.",
               "Seen with l as the transversal, the two angles of 90° are corresponding angles.",
               "The corresponding angles are equal, both 90°.",
               "So the two lines are parallel."],
              "Yes, parallel: the corresponding angles are both 90°",
              ncert=["5.7.set_square"]),
           WE("Place the long side of a 45° set square so that it makes 45° with l, and draw along it, then slide "
              "and draw again. Are the two lines parallel? How can you check?",
              ["The long side makes 45° with l each time, because the set square does not turn.",
               "The two angles of 45° are corresponding angles of the transversal l.",
               "They are equal, so the lines are parallel.",
               "To check, trace one angle and slide the tracing over the other, or measure both with a protractor."],
              "Yes, parallel: the corresponding angles are both 45°",
              ncert=["5.7.long_side"])],
       ncert=["5.7.nec_suff"], key_terms=["set square"], misconceptions=["M_LOOKS_PARALLEL"], minutes=10),
     A("T8.C2", "A parallel line through a point, by folding", "Apply",
       "Students fold a line parallel to a crease through a given point, and explain why it is parallel.",
       textbook=["Making Parallel Lines through Paper Folding",
                 "Let us try to do the same with paper folding. For a line l (given as a crease), how do we make a "
                 "line parallel to l such that it passes through point A?",
                 "We know how to fold a piece of paper to get a line perpendicular to l. Now, try to fold a "
                 "perpendicular to l such that it passes through point A. Let us call this new crease t.",
                 "Now, fold a line perpendicular to t passing through A again. Let us call this line m. The lines l "
                 "and m are parallel to each other.",
                 "Why are lines l and m parallel to each other?"],
       teach=["Predict first: first fold a line through A that is perpendicular to l; then which fold through A "
              "gives a line parallel to l?",
              "A second fold perpendicular to t, through A, gives m.",
              "Both l and m are perpendicular to t, so t is a transversal with two corresponding angles of 90°."],
       examples=[
           WE("A crease l and a point A are given. Fold a line m through A parallel to l, and say why it is "
              "parallel.",
              ["Fold the paper so that l falls on itself and the crease passes through A. This crease t is "
               "perpendicular to l.",
               "Unfold. Now fold the paper so that t falls on itself and the new crease passes through A. This "
               "crease is m, perpendicular to t.",
               "t crosses l at 90° and crosses m at 90°, and these are corresponding angles.",
               "The corresponding angles are equal, so l and m are parallel."],
              "m is parallel to l, since both are perpendicular to t, so the corresponding angles are both 90°",
              ncert=["5.7.fold_parallel"])],
       ncert=["5.7.why_parallel"], key_terms=["crease", "perpendicular"], misconceptions=["M_ONE_FOLD"], minutes=8),
     DOER("T8.C3", "Practice: parallel lines with a set square", "set_square_slider", "Apply",
          "Students draw a line parallel to a given line through a given point with a ruler and a set square, and "
          "explain the method.",
          ["Slide a set square along a ruler and draw along the same edge: the lines are parallel.",
           "To pass through a point, slide until the edge reaches that point.",
           "The reason is always equal corresponding angles."],
          items=[
              FIO("5.7.FiO1", "Figure it Out (drawing parallel lines), Q1",
                  "Can you draw a line parallel to l that goes through the point A? How will you do it with the "
                  "tools from your geometry box? Describe your method.",
                  ["You need a ruler, a set square, a pencil and an eraser.",
                   "Place the set square so that one side lies along l.",
                   "Hold the ruler against another side of the set square, so that the ruler will not move.",
                   "Slide the set square along the ruler until the side that was along l reaches the point A.",
                   "Draw a line along that side, through A.",
                   "This line is parallel to l: the set square did not turn, so it made the same angle with the "
                   "ruler, and the corresponding angles are equal."],
                  "Slide the set square along a ruler until its side reaches A and draw along it; the line "
                  "through A is parallel to l",
                  tool="set_square_slider"),
          ],
          misconceptions=["M_LOOKS_PARALLEL"])]))
