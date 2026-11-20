# -*- coding: utf-8 -*-
"""Topics T4, T5 and T6 of Class 5 Chapter 7 (Shapes and Patterns), module M3 (Triangles, Four-Sided Shapes and
Tangram): Triangles from the Rhombus, Four-Sided Shapes from the Rhombus, and Tangram.
Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of its
topic's DOER, in the book's order. The rhombus on the book's cut-out sheet is read as two equilateral triangles joined, so the pieces are the halves of an
equilateral triangle (one right angle, the longest side twice the shortest, all three sides different); no student
text states an angle measure."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T4 Triangles from the Rhombus =============================================
TOPICS.append(TOPIC(
    "T4", "M3", "Triangles from the Rhombus", ["Rhombus", "Try This"], "Understand",
    "Students sort triangles into isosceles, equilateral and scalene by comparing their sides, and fold triangles to "
    "compare their angles.",
    "A rhombus has all sides equal, and it can be divided into four triangles. Two of these pieces can be joined to "
    "make a triangle. An isosceles triangle has 2 equal sides and 2 equal angles, an equilateral triangle has 3 equal "
    "sides and 3 equal angles, and a scalene triangle has no equal sides and no equal angles.",
    [A("T4.C1", "Isosceles Triangles", "Understand",
       "Students name an isosceles triangle by its 2 equal sides, and fold it in half to show that it also has 2 equal "
       "angles.",
       textbook=["A rhombus is a shape with all equal sides. It has been divided into four triangles.",
                 "Each triangle has 2 equal sides. Such triangles are called isosceles triangles.",
                 "Each isosceles triangle has 2 equal angles."],
       teach=["Predict first: a triangle has sides 5 cm, 5 cm and 3 cm. Fold it in half so that the two 5 cm sides lie "
              "on each other. Will the two angles at the ends of the 3 cm side match too?",
              "A rhombus is a shape with all sides equal. It can be divided into four triangles, and 2 of these "
              "triangles can be joined to make a new triangle.",
              "A triangle with 2 equal sides is called an isosceles triangle.",
              "Now fold the triangle. The two 5 cm sides lie exactly on each other, and the two angles at the ends of "
              "the 3 cm side land on each other too. They match.",
              "So an isosceles triangle has 2 equal sides and also 2 equal angles.",
              "Rule: an isosceles triangle has 2 equal sides and 2 equal angles; fold it in half to check."],
       examples=[WE("A triangle has sides 5 cm, 5 cm and 3 cm. Is it an isosceles triangle? Fold it in half and say "
                    "what you notice about its angles.",
                    ["Compare the sides: 5 cm, 5 cm and 3 cm. Two sides are equal (5 cm and 5 cm) and the third side "
                     "is different (3 cm).",
                     "A triangle with 2 equal sides is an isosceles triangle, so this is an isosceles triangle.",
                     "Fold it in half through the corner where the two 5 cm sides meet, so that the two 5 cm sides "
                     "lie on each other.",
                     "The two halves match exactly. The two corners at the ends of the 3 cm side land on each other.",
                     "So the two angles at the ends of the 3 cm side are equal.",
                     "Check: the fold splits the triangle into two halves that match, so equal sides and equal "
                     "angles come as a pair."],
                    "Yes, it is an isosceles triangle: it has 2 equal sides (5 cm and 5 cm). When it is folded in "
                    "half the two halves match, so it also has 2 equal angles")],
       ncert=["rh.def", "rh.iso"], key_terms=["isosceles", "equal sides", "equal angles", "fold"],
       misconceptions=["M_ISO_ANGLES"], minutes=6),
     A("T4.C2", "Equilateral and Scalene Triangles", "Understand",
       "Students name a triangle as equilateral, isosceles or scalene from the lengths of its sides, and say how many "
       "of its angles are equal.",
       textbook=["Equilateral triangles have equal angles.",
                 "Triangles that have no equal sides are called scalene triangles."],
       teach=["Predict first: triangle A has sides 6 cm, 6 cm and 6 cm. Triangle B has sides 7 cm, 5 cm and 4 cm. "
              "Triangle C has sides 8 cm, 8 cm and 3 cm. Which one has all 3 angles equal, and which one has no equal "
              "angles?",
              "Count the equal sides first. A has 3 equal sides, so A is an equilateral triangle. Fold A in half "
              "through any corner: the two halves lie exactly on each other and the other 2 corners land on each "
              "other, so all 3 angles are equal.",
              "B has no equal sides, so B is a scalene triangle. Fold B in half through each corner: the two halves "
              "never lie exactly on each other, so no two angles are equal.",
              "C has 2 equal sides, so C is an isosceles triangle with 2 equal angles.",
              "You can compare the angles of any shape by folding paper: angles that land exactly on each other are "
              "equal.",
              "Rule: 3 equal sides means equilateral, 2 equal sides means isosceles and no equal sides means scalene; "
              "equal sides go with equal angles."],
       examples=[WE("Triangle A has sides 6 cm, 6 cm and 6 cm. Triangle B has sides 7 cm, 5 cm and 4 cm. Triangle C "
                    "has sides 8 cm, 8 cm and 3 cm. Name each triangle and say how many of its angles are equal.",
                    ["Triangle A: the sides are 6 cm, 6 cm and 6 cm. All 3 sides are equal, so A is an equilateral "
                     "triangle.",
                     "Fold A in half through a corner, so that the two halves lie on each other. They match through "
                     "every corner, so all 3 angles of A are equal.",
                     "Triangle B: the sides are 7 cm, 5 cm and 4 cm. No two sides are equal, so B is a scalene "
                     "triangle.",
                     "Fold B in half through each of its corners. The two halves never lie exactly on each other, so "
                     "no two angles of B are equal.",
                     "Triangle C: the sides are 8 cm, 8 cm and 3 cm. Two sides are equal, so C is an isosceles "
                     "triangle with 2 equal angles.",
                     "Check: A has 3 equal sides and 3 equal angles, C has 2 and 2, and B has none and none. The "
                     "number of equal sides and the number of equal angles always match."],
                    "A is equilateral (3 equal sides, 3 equal angles), B is scalene (no equal sides, no equal "
                    "angles), C is isosceles (2 equal sides, 2 equal angles)")],
       ncert=["tr.equi"], key_terms=["equilateral", "scalene", "isosceles", "equal angles"],
       misconceptions=["M_ISO_ANGLES"], minutes=6),
     DOER("T4.C3", "Practice: Triangle Check", "triangle_check", "Apply",
          "Students make triangles from the pieces of a rhombus, measure their sides and fold them, and say whether "
          "each triangle is equilateral, isosceles or scalene.",
          ["A rhombus has all sides equal and it divides into 4 triangular pieces. Each piece has 1 right angle and 3 "
           "different sides.",
           "An isosceles triangle has 2 equal sides and 2 equal angles.",
           "An equilateral triangle has 3 equal sides and 3 equal angles.",
           "A scalene triangle has no equal sides and no equal angles. Fold a triangle to compare its angles."],
          items=[FIO("rh.two", "Triangles from the Rhombus: two pieces together",
                     "What geometrical shapes can you make by fitting 2 of these triangles together? Trace the shapes "
                     "you created.",
                     ["Each piece is a triangle with 1 right angle and 3 different sides: a shortest side, a middle "
                      "side and a longest side. The longest side is twice the shortest side.",
                      "Join 2 pieces side to side. They can meet along their shortest sides, their middle sides or "
                      "their longest sides, and the second piece can be flipped over or turned half way round.",
                      "Along the middle sides, with one piece flipped over: a triangle with all 3 sides equal.",
                      "Along the shortest sides, with one piece flipped over: a wider triangle with 2 equal sides.",
                      "Along the longest sides, with one piece flipped over: a kite. With one piece turned half way "
                      "round: a rectangle.",
                      "Along the middle sides or along the shortest sides, with one piece turned half way round: 2 "
                      "different parallelograms that are not rectangles.",
                      "Check: 2 triangles and 4 four-sided shapes make 2 + 4 = 6 shapes, and each one has 3 or 4 "
                      "sides."],
                     "Sample answer: 2 triangles (one with 3 equal sides, one wider with 2 equal sides), a kite, a "
                     "rectangle and 2 parallelograms that are not rectangles. Your answer may differ.",
                     kind="prompt",
                     q_figure="A rhombus divided by its two diagonals into four triangular pieces.",
                     s_figure="The six shapes made from 2 pieces, each with the line where the 2 pieces join dashed: "
                              "two triangles, a kite, a rectangle and two parallelograms."),
                 FIO("rh.q1", "Triangles from the Rhombus: types of triangles",
                     "How many different types of triangles can you make? Now, observe and measure the sides of these "
                     "triangles. What do you notice?",
                     ["Use 2 pieces joined side to side. Two different triangles can be made.",
                      "Join the pieces along their middle sides, with one piece flipped over. All 3 sides of this "
                      "triangle are equal.",
                      "Join the pieces along their shortest sides, with one piece flipped over. This triangle is "
                      "wider: 2 of its sides are equal and the third side is longer.",
                      "Measure the sides. The first triangle has 3 equal sides. The second triangle has 2 equal "
                      "sides.",
                      "So each triangle has 2 equal sides (in the first one all 3 sides are equal).",
                      "Check: the first triangle has 3 equal sides and the second has 2, so no triangle made from 2 "
                      "pieces has all its sides different."],
                     "2 types from 2 pieces: one with all 3 sides equal and a wider one with 2 equal sides. In both "
                     "triangles, 2 sides are equal.",
                     kind="prompt",
                     s_figure="The two triangles made from 2 pieces with the equal sides marked by matching ticks: "
                              "one triangle with 3 ticked sides and a wider triangle with 2 ticked sides."),
                 FIO("rh.fold", "Triangles from the Rhombus: fold an isosceles triangle",
                     "Trace the isosceles triangles on a paper and cut them out. Fold them in half. What do you "
                     "notice about their angles?",
                     ["Take an isosceles triangle, for example the wider one made from 2 pieces. Its 2 equal sides "
                      "meet at the top corner.",
                      "Fold it in half through the top corner, so that the 2 equal sides lie on each other. The fold "
                      "is the line where the 2 pieces were joined.",
                      "The two halves match exactly. The two corners at the ends of the third side land on each "
                      "other.",
                      "So the two angles at the ends of the third side are equal.",
                      "Check: fold the triangle with 3 equal sides in the same way. The halves match again, so equal "
                      "sides go with equal angles."],
                     "The two halves match when folded, so the two angles at the ends of the third side are equal. "
                     "Each isosceles triangle has 2 equal angles.",
                     kind="prompt",
                     s_figure="The wider isosceles triangle with a dashed fold line from the top corner to the middle "
                              "of the bottom side, and matching arcs at the two bottom corners."),
                 FIO("rh.q2", "Triangles from the Rhombus: an equilateral triangle",
                     "Is it possible to make a triangle where all three sides are equal (equilateral triangle)?",
                     ["We want a triangle with 3 sides of the same length.",
                      "Join 2 pieces along their middle sides, with one piece flipped over.",
                      "The longest sides of the 2 pieces become 2 sides of the new triangle. They are equal.",
                      "The 2 shortest sides of the pieces lie in one straight line and make the third side. The "
                      "shortest side is half the longest side, so 2 shortest sides are as long as 1 longest side.",
                      "So all 3 sides are equal: an equilateral triangle.",
                      "Check: measure the 3 sides with a ruler. They are the same."],
                     "Yes. Join 2 pieces along their middle sides, with one piece flipped over. All 3 sides are "
                     "equal, so it is an equilateral triangle.",
                     kind="prompt",
                     s_figure="Two pieces joined along their middle sides into one triangle, with the join dashed and "
                              "all 3 outside sides marked with matching ticks."),
                 FIO("rh.q3", "Triangles from the Rhombus: all sides unequal",
                     "Is it possible to make a triangle where all three sides are unequal?",
                     ["One piece is already a triangle. Its 3 sides are a shortest side, a middle side and a longest "
                      "side, and they are all different.",
                      "So a single piece is a triangle with all 3 sides unequal.",
                      "Bigger ones are possible too. Join the wider triangle (2 pieces) and 1 more piece, longest "
                      "side against one of the 2 equal sides, and flip the piece until the outside has only 3 sides. "
                      "The 3 sides are all different.",
                      "A triangle with all 3 sides unequal is called a scalene triangle.",
                      "Check: a single piece has 3 different sides, so the answer is yes."],
                     "Yes. A single piece has 3 different sides, and 3 pieces can also make a bigger triangle with 3 "
                     "different sides. It is a scalene triangle.",
                     kind="prompt",
                     s_figure="One piece drawn alone with its 3 sides marked short, middle and long, and beside it a "
                              "bigger triangle made of 3 pieces with its 3 sides different."),
                 FIO("try.equi", "Try This: angles of an equilateral triangle",
                     "Take an equilateral triangle. Check if all the angles of an equilateral triangle are equal, "
                     "just like you did with the isosceles triangle.",
                     ["An equilateral triangle has 3 equal sides.",
                      "Fold it in half through one corner, so that the 2 sides at that corner lie on each other.",
                      "The two halves match exactly, so the other 2 corners land on each other and those 2 angles "
                      "are equal.",
                      "Fold again through a different corner. The two halves match again, so another pair of angles "
                      "is equal.",
                      "Every pair of the 3 corners matches, so all 3 angles are equal.",
                      "Check: 3 equal sides go with 3 equal angles."],
                     "Yes. The two halves match when folded through every corner, so all 3 angles of an equilateral "
                     "triangle are equal.",
                     kind="prompt",
                     q_figure="An equilateral triangle with one corner at the top.",
                     s_figure="The same triangle with its 3 corners marked with matching arcs, and a dashed fold line "
                              "from the top corner to the middle of the bottom side."),
                 FIO("try.halve", "Try This: cut an equilateral triangle in half",
                     "Now, cut the equilateral triangle in half. How many sides of each new triangle are equal?",
                     ["Cut the equilateral triangle along a line from one corner to the middle of the opposite side. "
                      "Each half is a triangle.",
                      "Look at the 3 sides of one half: half of an old side, the cut line, and a whole old side.",
                      "The cut line is longer than half of an old side and shorter than a whole old side. So the 3 "
                      "sides are all different.",
                      "No side of the new triangle is equal to another side.",
                      "Check: each half has the same shape as a piece of the rhombus, with a shortest side, a middle "
                      "side and a longest side."],
                     "None. The 3 sides of each new triangle are all different, so each half is a scalene triangle.",
                     kind="prompt",
                     q_figure="An equilateral triangle cut into two halves by a line from the top corner to the "
                              "middle of the bottom side, with the halves a little apart.",
                     s_figure="One half drawn with its 3 sides marked short, middle and long, and its right angle "
                              "marked with a small square."),
                 FIO("try.scalene", "Try This: angles of a scalene triangle",
                     "Check in scalene triangles whether any two or more angles are equal?",
                     ["Take a scalene triangle, for example one piece of the rhombus. Its 3 sides are all different.",
                      "Try to fold it so that the two halves match. Try with each corner.",
                      "The halves never match, so no 2 angles are equal.",
                      "One angle is a right angle. The other 2 angles are smaller than a right angle, and they are "
                      "different from each other.",
                      "Check: all 3 sides different goes with all 3 angles different."],
                     "No. In a scalene triangle the 3 angles are all different, so no 2 angles are equal.",
                     kind="prompt",
                     s_figure="One piece with its 3 corners marked with 1, 2 and 3 arcs to show that the 3 angles are "
                              "all different.")],
          misconceptions=["M_ISO_ANGLES"])],
    key_terms=["isosceles", "equilateral", "scalene", "rhombus"]))

# ============================== T5 Four-Sided Shapes from the Rhombus =====================================
TOPICS.append(TOPIC(
    "T5", "M3", "Four-Sided Shapes from the Rhombus", ["Rhombus", "Kites"], "Apply",
    "Students name kites, parallelograms and rectangles by their sides and angles, and count the sides of shapes made "
    "by joining pieces of the rhombus.",
    "A kite has equal adjacent sides, side 1 = side 2 and side 3 = side 4. A parallelogram has equal opposite sides "
    "and equal opposite angles. A rectangle is a parallelogram with 4 right angles. The sides of a shape made of "
    "pieces are the straight edges round its outside.",
    [A("T5.C1", "Kites", "Understand",
       "Students tell a kite from a parallelogram by checking whether the equal sides are next to each other or "
       "opposite each other.",
       textbook=["This shape is called a kite.",
                 "What do you notice about the sides of a kite?",
                 "Side 1 = Side 2.",
                 "Similarly, Side 3 = Side 4.",
                 "These sides are called adjacent sides."],
       teach=["Predict first: one four-sided shape has sides 5 cm, 5 cm, 3 cm and 3 cm, going round in that order. "
              "Another has sides 5 cm, 3 cm, 5 cm and 3 cm in that order. Both have two 5 cm sides and two 3 cm sides. "
              "Which one is a kite?",
              "Adjacent sides are sides that meet at a corner. Opposite sides are across from each other.",
              "In the first shape the two 5 cm sides meet at a corner, and the two 3 cm sides meet at a corner. Side "
              "1 = side 2 and side 3 = side 4, so it is a kite.",
              "In the second shape the two 5 cm sides are across from each other, and so are the two 3 cm sides. The "
              "opposite sides are equal, so it is a parallelogram, not a kite.",
              "Both shapes have the same side lengths. Only the order of the sides round the shape tells them apart.",
              "Rule: in a kite the equal sides are adjacent (next to each other): side 1 = side 2 and side 3 = "
              "side 4."],
       examples=[WE("A four-sided shape has sides 5 cm, 5 cm, 3 cm and 3 cm going round in that order. Is it a kite? "
                    "Then check a shape whose sides going round are 5 cm, 3 cm, 5 cm and 3 cm.",
                    ["Name the sides in order: side 1 is 5 cm, side 2 is 5 cm, side 3 is 3 cm and side 4 is 3 cm.",
                     "Side 1 and side 2 are next to each other and both are 5 cm, so side 1 = side 2. They are "
                     "adjacent sides.",
                     "Side 3 and side 4 are next to each other and both are 3 cm, so side 3 = side 4.",
                     "Two pairs of adjacent sides are equal, so the shape is a kite.",
                     "Now the second shape: 5 cm, 3 cm, 5 cm and 3 cm. Side 1 and side 3 are both 5 cm, but they are "
                     "opposite sides, not next to each other.",
                     "Side 2 and side 4 are both 3 cm and also opposite. Equal opposite sides make a parallelogram, "
                     "so this shape is not a kite.",
                     "Check: both shapes have two 5 cm sides and two 3 cm sides. Only the order round the shape "
                     "decides."],
                    "The first shape is a kite, because its equal sides are next to each other (side 1 = side 2 and "
                    "side 3 = side 4). The second shape has equal opposite sides, so it is a parallelogram, not a "
                    "kite")],
       ncert=["kite.text"], key_terms=["kite", "adjacent sides", "opposite sides"],
       misconceptions=["M_KITE_OPPOSITE"], minutes=6),
     A("T5.C2", "Parallelograms and Rectangles", "Understand",
       "Students name a four-sided shape with equal opposite sides as a parallelogram, and tell a rectangle from other "
       "parallelograms by its right angles.",
       textbook=["Quadrilaterals whose opposite sides are equal are called parallelograms.",
                 "In parallelogram A, opposite angles are equal.",
                 "In parallelogram B, all angles are equal and are right angles. Such a parallelogram is called a "
                 "rectangle.",
                 "A rectangle is a special type of parallelogram."],
       teach=["Predict first: a four-sided shape has sides 8 cm, 5 cm, 8 cm and 5 cm going round. Is it a "
              "parallelogram? Is it a rectangle?",
              "Look at the opposite sides: 8 cm and 8 cm, and 5 cm and 5 cm. Opposite sides are equal, so it is a "
              "parallelogram.",
              "A parallelogram also has equal opposite angles. Now look at the angles. If all 4 angles are right "
              "angles, the parallelogram is a rectangle.",
              "A slanted shape can have the same sides, 8 cm, 5 cm, 8 cm and 5 cm, and no right angle. It is a "
              "parallelogram that is not a rectangle.",
              "So the sides alone do not tell us if a shape is a rectangle. We also need the angles.",
              "Rule: a four-sided shape with equal opposite sides is a parallelogram; a parallelogram with 4 right "
              "angles is a rectangle, so a rectangle is a special parallelogram."],
       examples=[WE("A four-sided shape has sides 8 cm, 5 cm, 8 cm and 5 cm going round. What is it called? What more "
                    "do we need to know to call it a rectangle?",
                    ["Look at the opposite sides: the first and third sides are 8 cm and 8 cm, and the second and "
                     "fourth sides are 5 cm and 5 cm.",
                     "Opposite sides are equal, so the shape is a parallelogram.",
                     "In a parallelogram the opposite angles are equal.",
                     "Now look at the angles. If all 4 angles are right angles, the parallelogram is a rectangle.",
                     "A slanted shape with the same sides 8 cm, 5 cm, 8 cm and 5 cm has no right angle. It is a "
                     "parallelogram that is not a rectangle.",
                     "Check: every rectangle is a parallelogram, but a parallelogram is a rectangle only when its "
                     "angles are right angles."],
                    "It is a parallelogram, because its opposite sides are equal. It is a rectangle only if all 4 "
                    "angles are right angles; a slanted shape with the same sides is not a rectangle")],
       ncert=["par.text"], key_terms=["parallelogram", "opposite sides", "right angle", "rectangle"],
       misconceptions=["M_RECT_NOT_PARA"], minutes=6),
     DOER("T5.C3", "Practice: Rhombus Pieces", "rhombus_pieces", "Apply",
          "Students join 2, 3 and 4 pieces of the rhombus side to side, count the sides of each shape made, and name "
          "the four-sided shapes by their sides and angles.",
          ["A kite has adjacent sides equal: side 1 = side 2 and side 3 = side 4.",
           "A parallelogram has equal opposite sides and equal opposite angles.",
           "A rectangle is a parallelogram with 4 right angles.",
           "The sides of a shape are the straight edges round its outside. Sides joined inside do not count, and sides "
           "in one straight line make one longer side."],
          items=[FIO("rq.four", "Shapes from the Rhombus: four-sided shapes",
                     "How many different 4-sided shapes (quadrilaterals) can you make?",
                     ["Join 2 pieces side to side. The joined side hides inside, so 2 pieces with 3 sides each give 3 "
                      "+ 3 − 2 = 4 sides outside, unless two sides line up in a straight line.",
                      "Join along the longest sides, with one piece flipped over: a kite.",
                      "Join along the longest sides, with one piece turned half way round: a rectangle.",
                      "Join along the middle sides, with one piece turned half way round: a parallelogram that is "
                      "not a rectangle. Join along the shortest sides, with one piece turned half way round: another "
                      "one.",
                      "That is 4 different four-sided shapes: a kite, a rectangle and 2 parallelograms. Sliding a "
                      "piece along a joined side makes even more, so there are at least 4.",
                      "Check: each of the 4 shapes has 4 sides, counted round the outside."],
                     "Sample answer: at least 4: a kite, a rectangle and 2 parallelograms that are not rectangles. "
                     "Your answer may differ.",
                     kind="prompt",
                     q_figure="A rhombus divided by its two diagonals into four triangular pieces.",
                     s_figure="The four shapes made from 2 pieces, each with the joined side dashed: a kite, a "
                              "rectangle and two parallelograms."),
                 FIO("rq.measure", "Shapes from the Rhombus: measure the sides",
                     "Measure the sides of each of these two quadrilaterals A and B. What do you notice? Are there any "
                     "pairs of sides that are equal? Which pairs are equal, adjacent or opposite?",
                     ["Shape A has 4 sides. Its 2 long sides are each the longest side of a piece, and its 2 short "
                      "sides are each the shortest side of a piece.",
                      "Measure: the 2 long sides are the same length, and the 2 short sides are the same length.",
                      "Each long side is across from the other long side. So the equal pairs of A are opposite "
                      "sides, not adjacent sides.",
                      "Shape B has 4 sides: 2 sides are the shortest side of a piece and 2 sides are the middle side "
                      "of a piece.",
                      "Measure: the 2 shorter sides are equal and the 2 longer sides are equal, and each equal pair "
                      "is opposite.",
                      "Check: in A and in B the equal sides are opposite each other, so none of the equal pairs is "
                      "adjacent."],
                     "In both A and B there are 2 pairs of equal sides, and the equal sides are opposite each other, "
                     "not adjacent.",
                     kind="prompt",
                     q_figure="Two four-sided shapes labelled A and B: A is slanted and made of two triangular pieces "
                              "joined along their middle sides, and B has square corners and is made of two "
                              "triangular pieces joined along their longest sides.",
                     s_figure="The same A and B with the equal sides marked by matching ticks: single ticks on the "
                              "long pair and double ticks on the short pair of each shape."),
                 FIO("rq.angles", "Shapes from the Rhombus: angles of A and B",
                     "What types of angles do quadrilaterals A and B have? Which angles are equal in each of the above "
                     "parallelograms?",
                     ["Shape A: 2 corners are wider than a right angle and 2 corners are narrower than a right "
                      "angle.",
                      "The 2 wide corners are across from each other and are equal. The 2 narrow corners are across "
                      "from each other and are equal. So the opposite angles of A are equal.",
                      "Shape B: all 4 corners are right angles, so all 4 angles are equal.",
                      "A parallelogram with 4 right angles is a rectangle, so B is a rectangle.",
                      "Check: A and B are both parallelograms, and B is a special one."],
                     "A has 2 angles wider than a right angle and 2 narrower, and opposite angles are equal. B has 4 "
                     "right angles, all equal, so B is a rectangle.",
                     kind="prompt",
                     q_figure="The same two shapes A and B: A is slanted and B has square corners.",
                     s_figure="A with matching arcs on its opposite corners, single arcs on the 2 narrow corners and "
                              "double arcs on the 2 wide corners, and B with a small square at each of its 4 "
                              "corners."),
                 FIO("rq.draw", "Shapes from the Rhombus: draw kites and parallelograms",
                     "In the grid given below, draw two different kites and parallelograms each.",
                     ["Give every corner two numbers: how many squares across, then how many up, counted from the "
                      "bottom left of your drawing.",
                      "A kite needs 2 pairs of equal adjacent sides. Kite 1 has corners (0,3), (2,0), (4,3) and "
                      "(2,7).",
                      "Its first 2 sides each go 2 across and 3 up or down, so they are equal. Its last 2 sides each "
                      "go 2 across and 4 up or down, so they are equal.",
                      "Kite 2 has corners (0,2), (3,0), (6,2) and (3,5). Its first 2 sides each go 3 across and "
                      "2 up or down. Its last 2 sides each go 3 across and 3 up or down.",
                      "A parallelogram needs equal opposite sides. Parallelogram 1 has corners (0,0), (5,0), (7,3) "
                      "and (2,3). Its bottom and top sides both go 5 across, and its 2 slanted sides both go 2 "
                      "across and 3 up.",
                      "Parallelogram 2 has corners (0,0), (4,0), (5,4) and (1,4). Its bottom and top sides both "
                      "go 4 across, and its 2 slanted sides both go 1 across and 4 up.",
                      "Check: in each kite the equal sides meet at a corner, and in each parallelogram the equal "
                      "sides are across from each other."],
                     "Sample answer: kites (0,3), (2,0), (4,3), (2,7) and (0,2), (3,0), (6,2), (3,5); "
                     "parallelograms (0,0), (5,0), (7,3), (2,3) and (0,0), (4,0), (5,4), (1,4). Your shapes "
                     "may differ.",
                     kind="prompt",
                     q_figure="An empty grid of small squares.",
                     s_figure="The same grid with two kites and two parallelograms drawn on it, each corner on a grid "
                              "point and each shape in a different colour."),
                 FIO("rq.three", "Shapes from the Rhombus: three triangles",
                     "Now, use 3 triangles from the rhombus to form shapes. How many sides do each one of them have? "
                     "Using 3 triangular pieces of the rhombus, try creating: (a) a 3-sided shape; (b) a 4-sided shape; "
                     "(c) a 5-sided shape.",
                     ["Each piece has 3 sides, so 3 pieces have 3 + 3 + 3 = 9 sides. Joining 3 pieces takes 2 joins, "
                      "and 4 of the 9 sides hide inside, so the outside has at most 9 − 4 = 5 sides. Sides that line "
                      "up in a straight line make one longer side, so a shape can have fewer.",
                      "(a): 3-sided shape. Join the wider triangle (2 pieces joined along their shortest sides) and "
                      "1 more piece, with the longest side of the new piece against one of the 2 equal sides of the "
                      "wider triangle. Flip the piece until the outside has 3 sides. It is a big triangle with 3 "
                      "different sides.",
                      "(b): 4-sided shape. Join the triangle with 3 equal sides (2 pieces joined along their middle "
                      "sides) and 1 more piece, with the longest side of the new piece against a side of the "
                      "triangle. The outside has 4 sides.",
                      "(c): 5-sided shape. Join 2 pieces along their shortest sides, with one turned half way round, "
                      "to make a slanted shape. Put the third piece with its longest side against one of the 2 long "
                      "sides, and flip it until the outside has 5 sides.",
                      "Check: count the sides round the outside of each shape: 3, 4 and 5. In all, 3 pieces make 13 "
                      "different shapes: 2 with 3 sides, 5 with 4 sides and 6 with 5 sides."],
                     "Sample answer: yes. (a): a big triangle with 3 different sides. (b): the triangle with 3 equal "
                     "sides and 1 more piece, 4 sides. (c): a slanted shape and 1 more piece, 5 sides. Your answer "
                     "may differ.",
                     kind="prompt",
                     q_figure="A rhombus divided by its two diagonals into four triangular pieces.",
                     s_figure="Three shapes made from 3 pieces, with the joins dashed and the outside sides counted: "
                              "a triangle with 3 sides, a shape with 4 sides and a shape with 5 sides."),
                 FIO("rq.four_pieces", "Shapes from the Rhombus: all four triangles",
                     "Which of these shapes can be made with all 4 pieces? Try and find out. (a) Square; (b) Rectangle; "
                     "(c) Triangle; (d) Pentagon, 5-sided; (e) Hexagon, 6-sided; (f) Octagon, 8-sided",
                     ["Each new piece joined along a whole side covers 1 side and adds 2 new sides, so it adds at "
                      "most 1 side.",
                      "A piece has 3 sides, and the other 3 pieces add at most 3 more. So 4 pieces make a shape with "
                      "at most 3 + 3 = 6 sides.",
                      "(a): no square. A square needs 4 equal sides and 4 right angles. The shape with 4 equal sides "
                      "that 4 pieces make is the rhombus, which has no right angle, and the rectangles have 2 "
                      "different side lengths.",
                      "(b): rectangle, yes. Make a rectangle from 2 pieces (longest sides together, one piece turned "
                      "half way round), make a second one the same, and join the 2 rectangles along sides of the "
                      "same length.",
                      "(c): triangle, yes. Join the triangle with 3 equal sides (2 pieces) and the wider triangle (2 "
                      "pieces) along sides of the same length, and turn them until the outside has only 3 sides. "
                      "They make a big triangle.",
                      "(d): pentagon, yes. Join a kite (2 pieces) and a rectangle (2 pieces) along sides of the same "
                      "length, and turn them until the outside has 5 sides.",
                      "(e): hexagon, yes. Join 2 kites along sides of the same length, and turn them until the "
                      "outside has 6 sides.",
                      "(f): no octagon. A shape made of 4 pieces has at most 6 sides, and an octagon has 8.",
                      "Check: yes for the rectangle, triangle, pentagon and hexagon, and no for the square and the "
                      "octagon."],
                     "A rectangle, a triangle, a pentagon and a hexagon can be made. A square and an octagon cannot.",
                     kind="prompt",
                     s_figure="Four shapes made from all 4 pieces, with the joins dashed: a rectangle, a big "
                              "triangle, a pentagon and a hexagon."),
                 FIO("kite.fold", "Kites: make a kite by folding",
                     "Make your own kite shape. (a) Start with a square piece of paper. (b) Take one corner of the "
                     "paper and fold it towards the opposite corner, creating a sharp crease along the diagonal. (c) "
                     "Open and fold the corner A inwards, aligning the edge with the crease you just made. (d) Repeat "
                     "on the other side, folding the other corner B inwards to align with the crease at the centre. "
                     "You have a kite shape! What shapes do you see in the kite?",
                     ["Fold the corner A onto the corner across from it, which is B, and open it again. The crease "
                      "runs along the other diagonal of the square.",
                      "Fold the corner A inwards so that one edge of the paper lies along the crease. The folded "
                      "part is a triangle.",
                      "Fold the corner B inwards in the same way, from the same end of the crease, so that its edge "
                      "lies along the crease too. This folded part is also a triangle.",
                      "The paper now has the shape of a kite: 2 pairs of adjacent sides are equal.",
                      "Look at the shapes: the 2 folded flaps are 2 triangles, and the paper under them shows 2 more "
                      "triangles. The crease also cuts the kite into 2 triangles.",
                      "Check: 2 flaps and 2 triangles under them make 2 + 2 = 4 triangles."],
                     "Sample answer: triangles. The kite is made of 4 triangles: the 2 folded flaps and 2 more under "
                     "them. It also splits along the crease into 2 triangles. Your answer may differ.",
                     kind="prompt",
                     q_figure="A square sheet of paper with a dashed crease along one diagonal, and the corner A at "
                              "the bottom left and the corner B at the top right marked.",
                     s_figure="The folded kite with the crease dashed, the 2 folded flaps coloured orange and the 2 "
                              "triangles under them coloured blue.")],
          misconceptions=["M_KITE_OPPOSITE", "M_RECT_NOT_PARA", "M_PIECES_AREA"])],
    key_terms=["kite", "parallelogram", "rectangle", "rhombus"]))

# ============================== T6 Tangram =================================================================
TOPICS.append(TOPIC(
    "T6", "M3", "Tangram", ["Tangram"], "Apply",
    "Students name the seven tangram pieces, compare their sides and angles, and make shapes from some or all of the "
    "pieces.",
    "A tangram has 7 pieces: 5 triangles in three sizes, a square and a parallelogram. Every triangle has a right "
    "angle and 2 equal sides. A shape can be made from some or all of the pieces, often in more than one way.",
    [A("T6.C1", "The Seven Tangram Pieces", "Understand",
       "Students sort the 7 tangram pieces by their number of sides, and name each piece as a small, medium or large "
       "triangle, a square or a parallelogram.",
       textbook=["Tangram"],
       teach=["Predict first: a tangram set has 7 pieces. If you sort them by the number of sides, how many pieces "
              "have 3 sides and how many have 4 sides?",
              "Pieces with 3 sides are triangles. There are 5 of them, in three sizes: 2 small, 1 medium and 2 large.",
              "Pieces with 4 sides are the square and the parallelogram. That makes 5 + 2 = 7 pieces.",
              "Look at the corners. Every triangle has 1 right angle and 2 equal angles. The square has 4 right "
              "angles and 4 equal sides. The parallelogram has no right angle.",
              "Rule: sort the pieces by their sides first, 5 triangles and 2 four-sided pieces, then compare their "
              "sizes, sides and angles."],
       examples=[WE("A tangram has 7 pieces: 2 small triangles, 1 medium triangle, 2 large triangles, a square and a "
                    "parallelogram. Sort them by the number of sides, and say what is special about the angles of "
                    "each group.",
                    ["Count the sides of each piece. A triangle has 3 sides. The square and the parallelogram have 4 "
                     "sides each.",
                     "3 sides: the 2 small triangles, the 1 medium triangle and the 2 large triangles. That is 2 + 1 "
                     "+ 2 = 5 triangles.",
                     "4 sides: the square and the parallelogram. That is 2 pieces.",
                     "Together the two groups hold 5 + 2 = 7 pieces.",
                     "Each of the 5 triangles has 1 right angle and 2 equal angles.",
                     "The square has 4 right angles and 4 equal sides. The parallelogram has no right angle.",
                     "Check: each of the 7 pieces is in exactly one group."],
                    "3 sides: 5 triangles (2 small, 1 medium, 2 large). 4 sides: the square and the parallelogram. "
                    "5 + 2 = 7 pieces. Every triangle has a right angle and 2 equal angles")],
       ncert=["tg.intro"], key_terms=["tangram", "triangle", "square", "parallelogram"],
       misconceptions=["M_ISO_ANGLES"], minutes=5),
     DOER("T6.C2", "Practice: Tangram Maker", "tangram_maker", "Apply",
          "Students name the seven tangram pieces, say how they are the same or different, and make shapes from some "
          "or all of the pieces in more than one way.",
          ["A tangram set has 7 pieces: 2 large triangles, 1 medium triangle, 2 small triangles, a square and a "
           "parallelogram.",
           "The 5 triangles have 3 sides, a right angle and 2 equal sides. The square and the parallelogram have 4 "
           "sides.",
           "A shape can be made from some or all of the pieces, and often in more than one way."],
          items=[FIO("tg.name", "Tangram: name the pieces",
                     "Look at the tangram set. Cut out all the shapes. Name them.",
                     ["Count the sides of each piece and compare the sizes.",
                      "5 pieces have 3 sides, so they are triangles. The 2 biggest are the large triangles, the 2 "
                      "smallest are the small triangles, and the one in between is the medium triangle.",
                      "2 pieces have 4 sides. One has 4 equal sides and 4 right angles: the square. The other is "
                      "slanted with equal opposite sides: the parallelogram.",
                      "Check: 2 + 1 + 2 + 1 + 1 = 7 pieces."],
                     "2 large triangles, 1 medium triangle, 2 small triangles, 1 square and 1 parallelogram.",
                     kind="prompt",
                     q_figure="A big square cut into seven pieces of different colours with no labels: two large "
                              "triangles, one medium triangle, two small triangles, one small square and one "
                              "parallelogram.",
                     s_figure="The same seven pieces, each with its name written on it."),
                 FIO("tg.same", "Tangram: same or different",
                     "(a): How are they same or different from each other?",
                     ["Look at what is the same. Every piece has straight sides and corners.",
                      "The 5 triangles have the same shape in 3 sizes: the 2 small triangles are the same size, the "
                      "2 large triangles are the same size, and the medium triangle is in between.",
                      "Look at what is different. The sizes are different, and the square and the parallelogram have "
                      "4 sides while the triangles have 3.",
                      "Check: 5 triangles and 2 four-sided pieces make 5 + 2 = 7 pieces."],
                     "Same: all have straight sides, and the 5 triangles have the same shape. Different: the sizes "
                     "differ, and the square and parallelogram have 4 sides, not 3.",
                     kind="prompt",
                     s_figure="The five triangles in a row from small to large, and beside them the square and the "
                              "parallelogram."),
                 FIO("tg.angles", "Tangram: angles",
                     "(b): What do you notice about the angles of each of the shapes?",
                     ["Look at the 5 triangles. Each triangle has 1 right angle and 2 equal angles.",
                      "Look at the square. All 4 angles are right angles, so all 4 are equal.",
                      "Look at the parallelogram. It has no right angle, and its opposite angles are equal.",
                      "Check: fold a triangle in half through its right angle. The other 2 corners land on each "
                      "other, so those 2 angles are equal."],
                     "Each triangle has 1 right angle and 2 equal angles. The square has 4 right angles. The "
                     "parallelogram has no right angle, and its opposite angles are equal.",
                     kind="prompt",
                     s_figure="The seven pieces with a small square marking each right angle: one in each triangle "
                              "and four in the square."),
                 FIO("tg.sides", "Tangram: sides",
                     "(c): What do you notice about the sides of each of the shapes?",
                     ["Look at the 5 triangles. Each triangle has 2 equal sides, and its third side is longer.",
                      "Look at the square. All 4 sides are equal.",
                      "Look at the parallelogram. Its opposite sides are equal, and it has 2 different lengths: 2 "
                      "longer sides and 2 shorter sides.",
                      "Check: lay pieces edge to edge to compare the sides. Equal sides match exactly."],
                     "Each triangle has 2 equal sides. The square has 4 equal sides. The parallelogram has equal "
                     "opposite sides, in 2 different lengths.",
                     kind="prompt",
                     s_figure="The seven pieces with the equal sides marked by matching ticks."),
                 FIO("tg.make", "Tangram: make the shapes",
                     "Now, use some or all of the pieces of your tangram set to make the following shapes. There may "
                     "be more than one way to do it.",
                     ["Use some or all of the 7 pieces. The pieces must not overlap, and they must fill the outline "
                      "with no gap.",
                      "Rectangle: put the medium triangle in the middle with its longest side at the bottom. Put a "
                      "small triangle in the gap on each side. The 3 pieces fill the rectangle.",
                      "Slanted parallelogram: put the medium triangle on the left. Put the 2 small triangles "
                      "together on the right, so that they make a second triangle the size of the medium one. The 2 "
                      "triangles side by side make the slanted shape.",
                      "Triangle: the medium triangle fills it, with its longest side at the bottom. The 2 small "
                      "triangles also fill it, side by side with their right angles together at the middle of the "
                      "bottom.",
                      "Four-sided shape with a short top and a long bottom: put the parallelogram on the left and "
                      "the medium triangle on the right, with the longest side of the medium triangle at the "
                      "bottom.",
                      "More than one way: the rectangle can also be made from the square and the 2 small triangles, "
                      "and the parallelogram from the square with a small triangle on each side.",
                      "Check: each outline is filled with no gap and no overlap."],
                     "Sample answer: rectangle and parallelogram: medium triangle and 2 small triangles. Triangle: "
                     "medium triangle. Last shape: parallelogram and medium triangle. Your answer may differ.",
                     kind="prompt",
                     q_figure="Four empty outlines with no pieces inside: a slanted four-sided shape with equal "
                              "opposite sides, a rectangle twice as long as it is tall, a triangle with a right angle "
                              "at the top, and a four-sided shape with a short top and a long bottom.",
                     s_figure="The same four outlines, each filled with tangram pieces of different colours.")],
          misconceptions=["M_PIECES_AREA"])],
    key_terms=["tangram", "triangle", "square", "parallelogram"]))
