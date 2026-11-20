# -*- coding: utf-8 -*-
"""Topics T4 and T5 (module M3: Designs, Block Prints and Revision): Making Designs that Turn (the designs, the Design
Studio and the Let Us Think and squares-and-triangles questions) and Block Printing and Patterns (a half print and its
line of symmetry, one block printed many times, the matching, design B, the border shapes and the project).
Every teaching concept has one worked example with the plan's own shapes; the book's questions are FIO items of the
DOERs, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T4 Making Designs that Turn ================================================
TOPICS.append(TOPIC(
    "T4", "M3", "Making Designs that Turn", ["Making Designs", "Let Us Think", "Let Us Do (squares and triangles)"],
    "Apply",
    "Students make a design look the same after a 1/2 turn and a 1/4 turn by adding or colouring parts, and find the "
    "lines of symmetry of the design by folding.",
    "To make a design look the same after a turn, copy every part to the place where it would land after that turn. "
    "Colours count as well as shapes. A design can have turn symmetry, reflection symmetry, both or neither, and each "
    "is checked on its own.",
    [A("T4.C1", "A Design That Looks the Same After a Turn", "Apply",
       "Students add shapes to a design so that it looks the same after a 1/2 turn and after a 1/4 turn, and count the "
       "turns at which the design matches in a full turn.",
       teach=["Predict first: a design has a circle in the middle and one triangle above it. What must you add so that "
              "it looks the same after a half turn?",
              "A design looks the same after a 1/2 turn when every part has a matching part on the opposite side of "
              "the middle. The top triangle needs a matching triangle at the bottom.",
              "For a 1/4 turn every part needs a matching part on each of the four sides: top, right, bottom and left.",
              "During a full turn, a design with matching parts on all four sides looks the same 4 times: after a 1/4 "
              "turn, a 1/2 turn, a 3/4 turn and the full turn.",
              "Rule: to make a design look the same after a turn, copy each part to the place where it would land "
              "after that turn."],
       examples=[WE("A design has a circle in the middle and one triangle above it, pointing up. Add triangles so that "
                    "the design looks the same after a 1/2 turn, and then after a 1/4 turn.",
                    ["After a 1/2 turn the top triangle lands at the bottom, pointing down. Add a triangle below the "
                     "circle, pointing down.",
                     "Now the design has 1 + 1 = 2 triangles, and it looks the same after a 1/2 turn.",
                     "After a 1/4 turn the top triangle lands on the right, pointing right, and the bottom triangle "
                     "lands on the left, pointing left. Add a triangle on the right and one on the left.",
                     "Now the design has 2 + 2 = 4 triangles, one on each side of the circle.",
                     "The design looks the same after a 1/4 turn, a 1/2 turn, a 3/4 turn and a full turn: 4 times in a "
                     "full turn.",
                     "Check: after a 1/4 turn each triangle lands on the place of the next triangle."],
                    "Add a triangle below the circle for a 1/2 turn, then a triangle on the left and on the right for a "
                    "1/4 turn")],
       key_terms=["design", "turn", "matching part", "same"], misconceptions=["M_HALF_IMPLIES_QUARTER"], minutes=6),
     A("T4.C2", "Turn Symmetry and Reflection Symmetry in a Design", "Analyze",
       "Students check shapes and colours to find whether a design looks the same after a turn, and find its lines of "
       "symmetry by folding.",
       teach=["Predict first: a square is cut by its two diagonals into 4 triangles. The top and bottom triangles are "
              "orange and the left and right triangles are blue. Does it look the same after a 1/2 turn? After a 1/4 "
              "turn?",
              "Colours count. After a 1/2 turn orange lands on orange and blue lands on blue, so it looks the same. "
              "After a 1/4 turn orange lands on blue, so it does not.",
              "To find the lines of symmetry of a design, fold it along a line and check that every shape and every "
              "colour lands on the same shape and colour.",
              "This design has 2 lines of symmetry, the vertical line and the horizontal line. A diagonal is not a line "
              "of symmetry here, because it would put orange on blue.",
              "A design can have turn symmetry only, reflection symmetry only, both, or neither.",
              "Rule: check the shapes and the colours, with a turn for rotational symmetry and with a fold for "
              "reflection symmetry."],
       examples=[WE("A square is cut by its two diagonals into 4 triangles. The top and bottom triangles are orange and "
                    "the left and right triangles are blue. Does it look the same after a 1/2 turn? After a 1/4 turn? "
                    "Find its lines of symmetry.",
                    ["Turn it a 1/2 turn: the top triangle lands on the bottom triangle, both orange, and the left "
                     "triangle lands on the right triangle, both blue. It looks the same.",
                     "Turn it a 1/4 turn: the top triangle lands on the right triangle, orange on blue. It does not "
                     "look the same.",
                     "Fold along the vertical line: the left triangle lands on the right triangle, blue on blue, and "
                     "the top and bottom triangles each land on themselves. It is a line of symmetry.",
                     "Fold along the horizontal line: the top triangle lands on the bottom triangle, orange on orange. "
                     "It is a line of symmetry.",
                     "Fold along a diagonal: the top triangle lands on the left triangle, orange on blue. It is not a "
                     "line of symmetry.",
                     "Check: the design looks the same after a 1/2 turn, not after a 1/4 turn, and it has 2 lines of "
                     "symmetry."],
                    "It looks the same after a 1/2 turn but not after a 1/4 turn, and it has 2 lines of symmetry: the "
                    "vertical line and the horizontal line")],
       key_terms=["design", "colours", "lines of symmetry", "turn symmetry", "reflection symmetry"],
       misconceptions=["M_COLOUR_IGNORED", "M_BOTH_ALWAYS", "M_HALF_IMPLIES_QUARTER"], minutes=6),
     DOER("T4.C3", "Practice: Design Studio", "design_studio", "Apply",
          "Students change and colour designs so that they look the same after a 1/2 turn and a 1/4 turn, and draw the "
          "lines of symmetry of the designs.",
          ["Copy each part to the place where it would land after the turn.",
           "Colours count: a part must land on a part of the same shape and colour.",
           "Fold along a line to look for lines of symmetry, and turn the design to check for turn symmetry."],
          items=[FIO("mk.design", "Making Designs: change the design",
                     "(a) Does the design have rotational symmetry? Yes/No. (b) Try to change the design by adding "
                     "some shapes so that the new design looks the same after a 1/2 turn. Draw the new design in your "
                     "notebook. (c) Now try to modify or add more shapes so that the new design looks the same after "
                     "1/4 turn. Draw the new design in your notebook. (d) Do the new designs have reflection "
                     "symmetry? If yes, draw the lines of symmetry.",
                     ["(a): look at the right side. There is a circle at the tip of the right triangle, but nothing at "
                      "the tip of the left triangle. After a 1/2 turn the circle would land on the left, where there "
                      "is no circle. So the answer is No.",
                      "(b): add a circle at the tip of the left triangle. After a 1/2 turn the top triangle lands on "
                      "the bottom triangle, the left arm lands on the right arm, and the two circles swap. The new "
                      "design looks the same after a 1/2 turn.",
                      "(c): make all four arms the same. Turn the top and bottom triangles round so that their flat "
                      "sides touch the middle circle, and put a circle at the tip of each of the four triangles. Every "
                      "arm is now a triangle with a circle at its tip, so the design looks the same after every 1/4 "
                      "turn.",
                      "(d): the design from (b) has 2 lines of symmetry, a vertical line and a horizontal line through "
                      "the middle circle. The design from (c) has 4 lines: the vertical line, the horizontal line and "
                      "the two diagonals.",
                      "Sample answer: other changes also work. Your answer may differ."],
                     "(a): No. (b): add a circle at the left tip. (c): four equal arms with a circle at each tip. (d): "
                     "yes, 2 lines for (b) and 4 lines for (c). Your drawings may differ.",
                     kind="prompt",
                     q_figure="A blue design: a circle in the middle; a triangle above it and a triangle below it, each "
                              "with its point touching the circle; a triangle on the left and a triangle on the right, "
                              "each with its flat side touching the circle and its point away; and a second circle "
                              "touching the point of the right triangle.",
                     s_figure="Two blue designs side by side. The first has the circle added at the tip of the left "
                              "triangle, with a dashed vertical line and a dashed horizontal line. The second has four "
                              "equal arms, each a triangle with a circle at its tip, with four dashed lines through the "
                              "middle."),
                 FIO("lt.half_quarter", "Let Us Think: the green and pink square",
                     "Look at the design made of 4 squares. Does this design look the same after 1/2 turn? ___ Does "
                     "the design look the same after 1/4 turn? ___",
                     ["The design is a square of 4 smaller squares. The top left and the bottom right are green. The top "
                      "right and the bottom left are pink.",
                      "After a 1/2 turn the top left square lands on the bottom right, both green, and the top right "
                      "square lands on the bottom left, both pink. The design looks the same.",
                      "After a 1/4 turn the top left square, green, lands where the top right square is, and that "
                      "square is pink. The design does not look the same.",
                      "Check: the colours decide the answer, so a 1/2 turn works and a 1/4 turn does not."],
                     "After a 1/2 turn: Yes. After a 1/4 turn: No.",
                     kind="prompt",
                     q_figure="A square made of 4 equal smaller squares in 2 rows of 2: the top left and bottom right "
                              "squares are light green and the top right and bottom left squares are pink.",
                     s_figure="The same square and the square after a 1/2 turn looking the same, and after a 1/4 turn "
                              "with the colours changed, with a curved arrow for each turn."),
                 FIO("lt.colour", "Let Us Think: colour the square",
                     "Colour the square given in the figure using two colours so that the design looks the same after "
                     "every 1/4 turn. How many times does this shape look the same during a full turn?",
                     ["The dashed lines cut the square into 8 equal triangles round the middle.",
                      "A 1/4 turn moves every triangle on by 2 places.",
                      "So colour the triangles one after the other in two colours, orange, blue, orange, blue, and so on "
                      "all the way round.",
                      "Now each triangle lands on a triangle of its own colour after a 1/4 turn.",
                      "The design looks the same after a 1/4 turn, a 1/2 turn, a 3/4 turn and the full turn: 4 times in a "
                      "full turn.",
                      "Check: 8 ÷ 2 = 4, so 4 quarter turns make a full turn."],
                     "Colour the 8 triangles in two colours, one after the other. The shape looks the same 4 times in a "
                     "full turn.",
                     kind="prompt",
                     q_figure="A square drawn with dashed lines: its two diagonals and its two middle lines, which cut it "
                              "into 8 equal triangles meeting at the middle. Nothing is coloured.",
                     s_figure="The same square with its 8 triangles coloured orange and blue one after the other round "
                              "the middle."),
                 FIO("lt.reflection", "Let Us Think: reflection symmetry in the designs",
                     "Do these designs have reflection symmetry also? Draw the lines of symmetry.",
                     ["The two designs are the green and pink square and the square coloured orange and blue.",
                      "Green and pink square: fold it along a diagonal, from one corner to the opposite corner. The two "
                      "halves land on each other, green on green and pink on pink. So each diagonal is a line of "
                      "symmetry.",
                      "Fold it along the vertical line: the green square would land on a pink square. That is not a "
                      "line of symmetry. The horizontal line does the same.",
                      "So the green and pink square has 2 lines of symmetry, the two diagonals.",
                      "Orange and blue square: fold it along any dashed line. Every triangle would land on a triangle of "
                      "the other colour. So there is no line of symmetry.",
                      "This design looks the same after a turn, but it has no reflection symmetry."],
                     "Green and pink square: yes, 2 lines (the two diagonals). Orange and blue square: no line of "
                     "symmetry.",
                     kind="prompt",
                     q_figure="Two designs side by side: a square of 4 smaller squares, green at the top left and bottom "
                              "right and pink at the other two, and a square cut into 8 triangles by its two diagonals "
                              "and two middle lines, coloured orange and blue one triangle after the other.",
                     s_figure="The green and pink square with its two diagonals drawn as dashed lines, and the orange and "
                              "blue square with no dashed line."),
                 FIO("sq.make", "Let Us Do (squares and triangles): make designs",
                     "Cut out squares and equilateral triangles with the same side length. These are provided at the "
                     "end of the book. Make different symmetrical designs by using these two shapes.",
                     ["Take squares and equilateral triangles with the same side length.",
                      "Place a square in the middle and a triangle on each of its 4 sides, with a side of the triangle "
                      "along a side of the square. The design looks the same after every 1/4 turn and has 4 lines of "
                      "symmetry.",
                      "Place one triangle on top of one square: a house shape. It has 1 vertical line of symmetry and "
                      "no turn that makes it look the same.",
                      "Place 4 triangles in a row, one pointing up, then one pointing down, and so on. This slanted "
                      "strip looks the same after a 1/2 turn and has no line of symmetry.",
                      "Sample answer: many other designs work. Your answer may differ."],
                     "Sample answer: a square with a triangle on each side, a house shape, a slanted strip of 4 "
                     "triangles. Your designs may differ.",
                     kind="exercise",
                     q_figure="4 sand-coloured equilateral triangles and 4 blue squares lying loose and turned in "
                              "different directions, all with the same side length.",
                     s_figure="Three designs side by side: a blue square with a sand triangle on each of its 4 sides, a "
                              "blue square with one sand triangle on top, and a slanted strip of 4 sand triangles."),
                 FIO("sq.shape", "Let Us Do (squares and triangles): the shape with four squares",
                     "Does this shape have reflection symmetry? If yes, draw its lines of symmetry. Does it have "
                     "rotational symmetry? If yes, at which turn? Does it have both symmetries?",
                     ["The shape has 4 squares in 2 rows of 2, and 4 triangles: one at the left end and one at the "
                      "right end of each row.",
                      "Vertical line: fold down the middle, between the two columns of squares. The left triangles land "
                      "on the right triangles and the left squares on the right squares. It is a line of symmetry.",
                      "Horizontal line: fold along the line between the two rows. The top row lands on the bottom row. "
                      "It is a second line of symmetry.",
                      "Turn: after a 1/4 turn the triangles would land above and below the squares, where there are "
                      "none, so it does not look the same.",
                      "After a 1/2 turn each triangle lands on the triangle at the other end and each square lands on "
                      "the square opposite to it, so it looks the same. It has rotational symmetry at 1/2 turn.",
                      "So the shape has both symmetries."],
                     "Reflection symmetry: yes, 2 lines (one vertical, one horizontal). Rotational symmetry: yes, at 1/2 "
                     "turn. Both: yes.",
                     kind="exercise",
                     q_figure="A shape of 4 blue squares in 2 rows of 2. A sand-coloured triangle sits on the left of "
                              "each row and another on the right of each row, 4 triangles in all, each with its flat "
                              "side against a square and its point away from the squares.",
                     s_figure="The same shape with a dashed vertical line down the middle, a dashed horizontal line "
                              "between the two rows and a curved arrow for a 1/2 turn."),
                 FIO("sq.sort", "Let Us Do (squares and triangles): sort your designs",
                     "Now, make your designs. Sort your designs in 3 categories: designs with only rotational symmetry, "
                     "designs with only reflection symmetry, and designs with both rotational and reflection "
                     "symmetry.",
                     ["Test each design twice: fold it along lines for reflection symmetry, and turn it a 1/4, 1/2 and "
                      "3/4 turn for rotational symmetry.",
                      "Only rotational symmetry: the slanted strip of 4 triangles. It looks the same after a 1/2 turn "
                      "and has no line of symmetry.",
                      "Only reflection symmetry: the house shape, a triangle on top of a square. It has 1 vertical line "
                      "and no turn that works.",
                      "Both: a square with a triangle on each side. It has 4 lines and looks the same after every 1/4 "
                      "turn.",
                      "Sample answer: your designs may be different. Your answer may differ."],
                     "Sample answer. Only rotational: slanted strip of 4 triangles. Only reflection: house shape. Both: "
                     "square with 4 triangles. Your answer may differ.",
                     kind="exercise",
                     s_figure="Three groups side by side with the labels only rotational, only reflection and both: the "
                              "slanted strip of 4 triangles, the house shape, and the square with a triangle on each "
                              "side.")],
          misconceptions=["M_COLOUR_IGNORED", "M_HALF_IMPLIES_QUARTER", "M_BOTH_ALWAYS"])],
    key_terms=["design", "turn", "lines of symmetry"]))

# ============================== T5 Block Printing and Patterns =============================================
TOPICS.append(TOPIC(
    "T5", "M3", "Block Printing and Patterns",
    ["Let Us Explore", "Designs A and B", "Let Us Do (border shapes)", "Project Work"], "Apply",
    "Students match wooden blocks to their half prints through the line of symmetry and say after which turn a block "
    "print looks the same.",
    "A block print often shows its design on both sides of a line of symmetry, so a half print and its copy make the "
    "whole. A block stamped round a centre by equal turns makes a print that looks the same after that turn.",
    [A("T5.C1", "A Half Print and Its Line of Symmetry", "Understand",
       "Students match a wooden block to its half print by finding the line of symmetry along the straight edge of the "
       "print.",
       textbook=["Block printing is a traditional craft of Rajasthan, known for beautiful patterns and bright colours. "
                 "Artisans use carved wooden blocks to print designs on fabric. This art has been practised for "
                 "centuries and makes Rajasthan's textiles special."],
       teach=["Predict first: a wooden block has a design carved on it. The print on the cloth shows only half of the "
              "design, cut by a straight edge. Where is the other half?",
              "Block printing is a traditional craft of Rajasthan, known for beautiful patterns and bright colours. "
              "Artisans use carved wooden blocks to print designs on fabric.",
              "Many blocks have a line of symmetry. A half print has one straight edge, and that edge is the line of "
              "symmetry.",
              "The other half is the same picture on the other side of the line, as if the print were folded along it.",
              "To match a block to a half print, find the block's line of symmetry, imagine cutting the block along it, "
              "and look for the half print with the same shapes along its straight edge.",
              "Rule: the two halves of a symmetrical print are the same shape on the two sides of the line of "
              "symmetry."],
       examples=[WE("A block is carved in the shape of a leaf with a stem down the middle. Its half print shows only the "
                    "left half of the leaf. What does the whole print look like?",
                    ["The half print has one straight edge. That edge is the line of symmetry.",
                     "The straight edge runs down the middle of the leaf, along the stem.",
                     "Draw the same half on the other side of the line, as if the paper were folded along the edge.",
                     "The two halves together make the whole leaf.",
                     "Check: fold the whole print along the line and the two halves land on each other."],
                    "The whole print is the half print together with its copy on the other side of the straight edge")],
       ncert=["block.intro", "block.example"],
       key_terms=["block", "print", "line of symmetry", "half print"], misconceptions=["M_ANY_LINE"], minutes=5),
     A("T5.C2", "One Block Printed Many Times", "Understand",
       "Students explain why a block stamped 2 times with a 1/2 turn, or 4 times with 1/4 turns, makes a print that "
       "looks the same after that turn.",
       textbook=["Observe the pattern made by the wooden block below. We get the final print by using the block 4 times. "
                 "The design A looks the same after every 1/4 turn."],
       teach=["Predict first: a printer stamps a leaf block, turns the block a 1/4 turn and stamps again, and does this 4 "
              "times in all. Will the final print look the same after a 1/4 turn?",
              "We get the final print of design A by using the block 4 times, turning it a 1/4 turn each time. The "
              "design A looks the same after every 1/4 turn.",
              "If a block is stamped 2 times, with a 1/2 turn between the stamps, the print looks the same after a "
              "1/2 turn.",
              "The number of stamps round the middle tells the turn: 4 stamps give a 1/4 turn and 2 stamps give a 1/2 "
              "turn.",
              "Rule: stamp the same block round a middle point by equal turns, and the print looks the same after "
              "that turn."],
       examples=[WE("A flower block is stamped 2 times, with a 1/2 turn between the stamps. Does the print look the same "
                    "after a 1/2 turn? After a 1/4 turn?",
                    ["The first stamp puts a flower at the top.",
                     "A 1/2 turn of the block puts the second flower at the bottom.",
                     "Turn the print a 1/2 turn: the top flower lands at the bottom and the bottom flower lands at the "
                     "top. The print looks the same.",
                     "Turn the print a 1/4 turn: the flowers would land at the sides, where there are none. The print "
                     "does not look the same.",
                     "Check: 2 stamps match after a 1/2 turn only."],
                    "After a 1/2 turn it looks the same, and after a 1/4 turn it does not")],
       ncert=["block.A"],
       key_terms=["block", "stamped", "print", "turn"], misconceptions=["M_HALF_IMPLIES_QUARTER", "M_FULL_TURN"],
       minutes=5),
     DOER("T5.C3", "Pull it together and do it: Prints, Shapes and Project", None, "Apply",
          "Students match blocks to their half prints, name the turn and the symmetry of a block print, mark border "
          "shapes for reflection and rotational symmetry, and plan a vegetable-block project.",
          ["The straight edge of a half print is the line of symmetry of its block.",
           "A block stamped round a middle point by equal turns gives a print that looks the same after that turn.",
           "Test every shape with a fold line and with a turn, and mark it for each test."],
          items=[FIO("bp.match", "Let Us Explore: match the blocks to the prints",
                     "Below are images of wooden blocks and a part of their prints. Match each block to its correct "
                     "print by drawing a line. One is done for you.",
                     ["Each print shows half of its block. The straight edge of a half print is the block's line of "
                      "symmetry.",
                      "(i): the drop-shaped block with a leaf in the middle and a wavy edge goes with print (c), a half "
                      "drop with a wavy curved edge.",
                      "(ii): the lotus block with leaves under it goes with print (d), half a lotus with a leaf.",
                      "(iii): the round flower block goes with print (a), half a round flower.",
                      "(iv): the fan block is already joined to print (e), half a fan.",
                      "(v): the tall block with a flower on a stem goes with print (b), a stem with leaves.",
                      "Check: five blocks and five prints, and each print is used once."],
                     "(i) to (c); (ii) to (d); (iii) to (a); (iv) to (e); (v) to (b)",
                     kind="prompt",
                     q_figure="Five wooden blocks in a row labelled (i) a drop-shaped block with a wavy edge, (ii) a lotus "
                              "block, (iii) a round flower block, (iv) a fan block, (v) a tall block with a flower on a "
                              "stem; below them five half prints labelled (a) a blue half flower, (b) a green stem "
                              "with leaves, (c) a teal half drop, (d) a yellow half lotus, (e) a red half fan; one line "
                              "already joins the fan block (iv) to the red print (e).",
                     s_figure="The same picture with five lines: (i) to (c), (ii) to (d), (iii) to (a), (iv) to (e), "
                              "(v) to (b)."),
                 FIO("bp.designB", "Block Printing: design B",
                     "The design B looks the same after every ___ turn. This design has ___ symmetry.",
                     ["The design B is made of 4 hearts placed round the middle.",
                      "Turn it a 1/4 turn: the top heart lands where the right heart is, the right heart where the "
                      "bottom heart is, and so on. The design looks the same after every 1/4 turn.",
                      "The dashed vertical line and the dashed horizontal line are lines of symmetry: the left half "
                      "matches the right half, and the top half matches the bottom half.",
                      "So the design has rotational symmetry and reflection symmetry.",
                      "Check: it looks the same after a turn and it has lines of symmetry, so it has both."],
                     "Every 1/4 turn. It has both rotational symmetry and reflection symmetry.",
                     kind="prompt",
                     q_figure="Design B: four purple hearts placed round a middle point, one above, one below, one to the "
                              "left and one to the right, each with its pointed end towards the middle, with a dashed "
                              "vertical line and a dashed horizontal line through the middle.",
                     s_figure="The same design with a curved arrow for a 1/4 turn and the two dashed lines marked as "
                              "lines of symmetry."),
                 FIO("bd.border", "Let Us Do (border shapes): reflection and rotational symmetry",
                     "Observe the shapes given on the border. Which of the shapes have reflection symmetry? Put a tick "
                     "mark on them. Put a star mark on the shapes that have rotational symmetry.",
                     ["Test each shape with a fold line (reflection symmetry) and with a turn (rotational symmetry). "
                      "The shapes are numbered 1 to 19 round the border from the top-left corner, going to the right, "
                      "then down, then to the left, then up.",
                      "Shape 1, three pink triangles touching at their corners: 3 lines of symmetry, and it looks the "
                      "same after a 1/3 turn. Tick and star.",
                      "Shape 2, the green six-pointed star: 6 lines, and it looks the same after a 1/6 turn. Tick and "
                      "star.",
                      "Shape 3, the yellow six-sided shape: it has a vertical line and a horizontal line of symmetry, and "
                      "it looks the same after a 1/2 turn. Tick and star.",
                      "Shape 4, three lilac circles joined to the middle, drawn nearly even: 3 lines, and a 1/3 turn. "
                      "Tick and star.",
                      "Shape 5, the green triangle with grey corners: 3 lines, and a 1/3 turn. Tick and star.",
                      "Shape 6, the pink rectangle: 2 lines, and a 1/2 turn. Tick and star.",
                      "Shape 7, the grey diamond: 2 lines, and a 1/2 turn. Tick and star.",
                      "Shape 8, the five-sided shape with equal sides: 5 lines, and a 1/5 turn. Tick and star.",
                      "Shape 9, the lilac ring of small triangles, drawn nearly even: 5 lines, and a 1/5 turn. Tick and "
                      "star.",
                      "Shape 10, the seven-sided shape with equal sides: 7 lines, and a 1/7 turn. Tick and star.",
                      "Shape 11, the blue shape of four triangles: 4 lines, and a 1/4 turn. Tick and star.",
                      "Shape 12, the pink triangle with three teal circles: 3 lines, and a 1/3 turn. Tick and star.",
                      "Shape 13, the orange slanted four-sided shape: no line of symmetry, but it looks the same after a "
                      "1/2 turn. Star only.",
                      "Shape 14, the yellow triangle with three small grey triangles: 3 lines, and a 1/3 turn. Tick and "
                      "star.",
                      "Shape 15, the thin pink triangle with a square corner: no line of symmetry and no turn that "
                      "works. No mark.",
                      "Shape 16, the two maroon triangles touching at their points: 2 lines, and a 1/2 turn. Tick and "
                      "star.",
                      "Shape 17, the circle: every line through the middle is a line of symmetry, and it looks the same "
                      "after every turn. Tick and star.",
                      "Shape 18, the blue square: 4 lines, and a 1/4 turn. Tick and star.",
                      "Shape 19, the purple triangle with three equal sides: 3 lines, and a 1/3 turn. Tick and star.",
                      "Check: 17 shapes get a tick mark, all except 13 and 15, and 18 shapes get a star mark, all except "
                      "15. 17 + 2 = 19 and 18 + 1 = 19."],
                     "Tick mark (reflection symmetry): all shapes except 13 and 15. Star mark (rotational symmetry): all "
                     "shapes except 15.",
                     kind="exercise",
                     q_figure="The 19 shapes of the page border drawn in a ring, each with a number from 1 to 19 going "
                              "round from the top-left corner: three pink triangles, a green star, a yellow "
                              "six-sided shape, three lilac circles joined by lines, a green triangle with grey "
                              "corners, a pink rectangle, a grey diamond, an olive five-sided shape, a lilac ring of "
                              "small triangles, a green seven-sided shape, a blue shape of four triangles, a pink "
                              "triangle with three teal circles, an orange slanted four-sided shape, a yellow triangle "
                              "with three grey triangles, a thin pink triangle, two maroon triangles touching at their "
                              "points, a light green circle, a light blue square and a purple triangle.",
                     s_figure="The same 19 numbered shapes with a green tick mark on every shape except 13 and 15 and "
                              "a blue star on every shape except 15."),
                 FIO("pw.veg", "Project Work: vegetable blocks",
                     "Create symmetrical patterns and designs using vegetable blocks. Some are shown below.",
                     ["Cut a vegetable, such as a potato, to get a flat face, and carve a simple shape on it. A "
                      "ladyfinger cut across also gives a flower-like face.",
                      "Dip the flat face in colour and press it on paper to make a print.",
                      "For a design that looks the same after every 1/4 turn, stamp the block, turn the paper a 1/4 "
                      "turn, and stamp again, 4 times in all.",
                      "For a design with a line of symmetry, use a block that has its own line of symmetry and stamp it "
                      "on the two sides of a line drawn on the paper, the same distance from the line.",
                      "Sort your prints: only rotational symmetry, only reflection symmetry, or both.",
                      "Sample answer: your patterns may be different. Your answer may differ."],
                     "Sample answer: print a vegetable block 4 times, turning a 1/4 turn each time, and sort your prints. "
                     "Your answer may differ.",
                     kind="prompt",
                     q_figure="Two pictures: green ladyfingers beside two flower-like prints made by a ladyfinger cut "
                              "across, and two potatoes cut in half beside six oval prints with red and yellow stripes "
                              "and blue stripes.",
                     s_figure="A paper with 4 prints of one block placed round a middle point, each turned a 1/4 turn "
                              "from the one before.")],
          misconceptions=["M_HALF_IMPLIES_QUARTER", "M_BOTH_ALWAYS"])],
    key_terms=["block", "print", "shapes", "project"]))
