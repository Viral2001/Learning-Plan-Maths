# -*- coding: utf-8 -*-
"""Topics T7 to T11 of Class 5 Chapter 7, Shapes and Patterns: Which Shape Am I? (module M3), then Play with Circles,
Cube Connections, Puzzle: Tanu's Shapes and Icosahedron and Dodecahedron (module M4).
Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of its
topic's DOER, in the book's order, with the book's own wording."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T7 Which Shape Am I? ======================================================
TOPICS.append(TOPIC(
    "T7", "M3", "Which Shape Am I?", ["Which Shape Am I?"], "Analyze",
    "Students sort four-sided shapes into square, rectangle, rhombus and parallelogram by their sides and angles, and "
    "explain why one statement can describe more than one shape.",
    "Square, rectangle, rhombus and parallelogram are told apart by two questions: are all the sides equal, and are "
    "all the angles right angles? One statement, such as opposite sides equal, can fit more than one shape.",
    [A("T7.C1", "Square, Rectangle, Rhombus and Parallelogram", "Understand",
       "Students name a four-sided shape as a square, rectangle, rhombus or parallelogram by checking its sides and "
       "its angles, and say which statements fit more than one of these shapes.",
       teach=["Predict first: a shape has opposite sides equal. Is it a square, a rectangle, a rhombus or a "
              "parallelogram?",
              "Ask two questions about a four-sided shape. Are all four sides equal? Are all four angles right "
              "angles?",
              "All sides equal and all angles right angles: a square. Opposite sides equal and all angles right "
              "angles: a rectangle.",
              "All sides equal and the angles are not right angles: a rhombus. Opposite sides equal, the sides next "
              "to each other different and no right angles: a parallelogram.",
              "Opposite sides equal is true of all four shapes. So that one statement fits all four shapes, and a "
              "rectangle is a special parallelogram.",
              "Rule: check the sides, then the angles. One statement can fit more than one shape."],
       examples=[WE("Four shapes are described. X: all sides 6 cm and all angles right angles. Y: sides 9 cm, 4 cm, "
                    "9 cm, 4 cm and all angles right angles. Z: all sides 7 cm and the angles are not right angles. "
                    "W: sides 8 cm, 5 cm, 8 cm, 5 cm in order and the angles are not right angles. Name each shape. "
                    "Which of them have opposite sides equal?",
                    ["X: all four sides are equal (6 cm) and all four angles are right angles: a square.",
                     "Y: the sides are not all equal (9 cm and 4 cm), but opposite sides are equal and all angles "
                     "are right angles: a rectangle.",
                     "Z: all four sides are equal (7 cm) and the angles are not right angles: a rhombus.",
                     "W: opposite sides are equal (8 cm and 8 cm, 5 cm and 5 cm), the sides are not all equal and "
                     "the angles are not right angles: a parallelogram.",
                     "Now test the statement opposite sides are equal: X yes, Y yes, Z yes, W yes. All four shapes "
                     "have it.",
                     "Check: a statement about opposite sides alone does not tell the four shapes apart, so it fits "
                     "more than one shape. Adding all angles are right angles keeps only X and Y."],
                    "X is a square, Y is a rectangle, Z is a rhombus and W is a parallelogram. All four have opposite "
                    "sides equal, so that one statement fits all four")],
       key_terms=["square", "rectangle", "rhombus", "parallelogram", "opposite sides"],
       misconceptions=["M_RECT_NOT_PARA"], minutes=6),
     DOER("T7.C2", "Practice: Shape Detective", "shape_detective", "Apply",
          "Students match seven statements about sides and angles with the square, rectangle, rhombus or "
          "parallelogram they describe, and find which statements fit more than one shape.",
          ["A square has all sides equal and all angles right angles.",
           "A rectangle has opposite sides equal and all angles right angles.",
           "A rhombus has all sides equal and no right angles. A parallelogram has opposite sides equal and no right "
           "angles.",
           "For each statement, check the sides, then the angles, for all four shapes. One statement can fit more "
           "than one shape."],
          items=[FIO("ws.match", "Which Shape Am I?: match the statements",
                     "Match the statements with appropriate shapes. Do some of them describe more than one shape? "
                     "(1): All my angles are right angles, but all my sides are not equal. "
                     "(2): All my sides are equal, but all my angles are not. "
                     "(3): My opposite angles are equal, but my sides do not make a right angle. "
                     "(4): Two pairs of sides are equal, but they do not make a right angle. "
                     "(5): All my sides make right angles with each other and are equal. "
                     "(6): My opposite angles are equal and so are my sides. "
                     "(7): My opposite angles are equal and my sides make right angles. "
                     "The shapes: Square, Rectangle, Rhombus, Parallelogram.",
                     ["First write what each shape has. A square has all sides equal and all angles right angles. A "
                      "rectangle has opposite sides equal and all angles right angles. A rhombus has all sides equal "
                      "and no right angles. A parallelogram has opposite sides equal and no right angles. All four "
                      "have opposite sides equal and opposite angles equal.",
                      "(1): all angles are right angles but the sides are not all equal. A square has all sides "
                      "equal, so it is left out: Rectangle.",
                      "(2): all sides are equal but the angles are not all right angles. A square has right "
                      "angles, so it is left out: Rhombus.",
                      "(3): opposite angles are equal but the sides do not make a right angle: Rhombus and "
                      "Parallelogram.",
                      "(4): two pairs of equal sides and no right angle: Parallelogram and Rhombus.",
                      "(5): all sides make right angles and are equal: Square.",
                      "(6): opposite angles equal and opposite sides equal is true of all four shapes: all four.",
                      "(7): opposite angles equal and the sides make right angles: Square and Rectangle.",
                      "Check: statements 3, 4, 6 and 7 name more than one shape, so yes, some statements describe "
                      "more than one shape."],
                     "(1): Rectangle; (2): Rhombus; (3): Rhombus, Parallelogram; (4): Parallelogram, Rhombus; "
                     "(5): Square; (6): all four; (7): Square, Rectangle. Yes: 3, 4, 6 and 7 fit more than one "
                     "shape.",
                     kind="prompt",
                     q_figure="A square, a rectangle, a slightly slanted rhombus and a long slanted parallelogram, "
                              "each with its name under it.",
                     s_figure="The four shapes in a row, each with the numbers of the statements that describe it "
                              "written under it: Square 5, 6, 7; Rectangle 1, 6, 7; Rhombus 2, 3, 4, 6; "
                              "Parallelogram 3, 4, 6.")],
          misconceptions=["M_RECT_NOT_PARA"])],
    key_terms=["square", "rectangle", "rhombus", "parallelogram"]))

# ============================== T8 Play with Circles ======================================================
TOPICS.append(TOPIC(
    "T8", "M4", "Play with Circles", ["Play with Circles", "Circle Designs"], "Understand",
    "Students draw two diameters of a circle and name the shape made by joining their ends, and join points round a "
    "circle by a repeating move to make a string design.",
    "Two diameters of a circle always make a rectangle when their ends are joined, and a square when they cross at a "
    "right angle. Joining points round a circle by a repeating move, such as on by 4 and back by 3, makes a string "
    "design that closes when the thread is back at the start.",
    [A("T8.C1", "Two Diameters Make a Rectangle", "Understand",
       "Students join the ends of two diameters of a circle and name the shape formed by checking its sides and its "
       "angles.",
       teach=["Predict first: draw two diameters of a circle and join their four ends. What shape do you get? Are its "
              "angles right angles?",
              "A diameter is a line from one side of the circle to the other that passes through the centre. Every "
              "diameter of a circle has the same length, and the radius is half of it.",
              "Two diameters cross at the centre. All four ends are the same distance from the centre.",
              "Join the four ends in order and check. Opposite sides are equal and all four angles are right angles: "
              "a rectangle.",
              "Turn one diameter and join again. The sides change, but the shape is still a rectangle.",
              "If the two diameters cross at a right angle, all four sides are equal: a square, which is a special "
              "rectangle.",
              "Rule: the four ends of two diameters always make a rectangle."],
       examples=[WE("A circle has a diameter of 10 cm. Draw two diameters and join their four ends. What is the "
                    "radius? What shape is formed? What shape is formed when the two diameters cross at a right "
                    "angle?",
                    ["The diameter is 10 cm, so the radius is half of it: 10 ÷ 2 = 5 cm.",
                     "Draw one diameter and a second diameter. Both go through the centre, so both are 10 cm long.",
                     "Join the four ends in order. The shape has 4 sides: it is a quadrilateral.",
                     "Check the sides: opposite sides are equal.",
                     "Check the angles: all four are right angles. Opposite sides equal and four right angles: a "
                     "rectangle.",
                     "Now turn the second diameter until it crosses the first one at a right angle. All four sides "
                     "come out equal: a square. A square is a special rectangle.",
                     "Check: the four ends are all 5 cm from the centre and the two diameters are 10 cm each, so "
                     "every pair of diameters gives a rectangle."],
                    "The radius is 5 cm. Two diameters joined at their ends make a rectangle. If they cross at a "
                    "right angle it is a square, a special rectangle")],
       key_terms=["diameter", "rectangle", "circle", "centre", "radius"],
       misconceptions=["M_CIRCLE_ANY"], minutes=6),
     A("T8.C2", "Joining Points on a Circle", "Apply",
       "Students join points round a circle by a repeating move, such as on by 4 and back by 3, and count the lines "
       "when the thread is back at the start.",
       teach=["Predict first: a circle has 12 points numbered 1 to 12. You join 1 to 5, then 5 to 2, then 2 to 6, and "
              "keep going. Does the thread ever come back to 1?",
              "Look for the move. 1 to 5 goes on by 4. 5 to 2 goes back by 3. 2 to 6 goes on by 4 again.",
              "Keep the same moves: on by 4, back by 3, on by 4, back by 3. Each pair of moves goes on by 1 in all, "
              "so the thread starts a little further round each time.",
              "When you pass 12, the numbers start again from 1. From 9, going on by 4 takes you to 10, 11, 12 and "
              "then 1.",
              "The thread is back at 1 and the design is closed. Now count the lines.",
              "Rule: find the move, repeat it until the thread is back at the start, then count the lines."],
       examples=[WE("A circle has 12 points numbered 1 to 12 round it. Join 1 to 5, 5 to 2, 2 to 6, 6 to 3, and so on "
                    "until you reach 1 again. How many lines do you draw?",
                    ["Find the move: 1 to 5 is on by 4, 5 to 2 is back by 3, 2 to 6 is on by 4.",
                     "Keep the same moves: on by 4, back by 3, on by 4, back by 3.",
                     "Write the points in order: 1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6, 10, 7, 11, 8, 12, 9. From 9 go on "
                     "by 4: 10, 11, 12, then 1. The thread is back at 1.",
                     "Count the lines: each line joins a point to the next one in the list. The list has 18 points "
                     "with the last 1, so there are 18 − 1 = 17 lines.",
                     "Check: 8 pairs of moves (on by 4, back by 3) use 16 lines, and one last move on by 4 closes the "
                     "design, so 8 × 2 + 1 = 17 lines."],
                    "17 lines. The path is 1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6, 10, 7, 11, 8, 12, 9, 1")],
       key_terms=["points", "circle", "move", "lines", "thread"], minutes=6),
     DOER("T8.C3", "Practice: Circle Stitcher", "circle_stitcher", "Apply",
          "Students draw two diameters of a circle, join the ends and check the shape, and thread the points of a "
          "circle to make a string design.",
          ["The four ends of two diameters always make a rectangle, and a square when the diameters cross at a right "
           "angle.",
           "To thread points round a circle, find the move first, then repeat it until the thread is back at the "
           "start.",
           "Count the lines when the design is closed."],
          items=[FIO("pc.shape", "Play with Circles: the shape formed",
                     "(a): Draw a circle with a compass and mark its centre. "
                     "(b): Draw its diameter. Mark the endpoints of the diameter. "
                     "(c): Draw another diameter of the circle and mark the endpoints. "
                     "(d): Now join the four points. What shape is formed? Check the sides of the quadrilateral and "
                     "the angles obtained.",
                     ["Draw a circle with a compass. Say the radius is 4 cm, so the diameter is 4 × 2 = 8 cm. Mark "
                      "the centre.",
                      "Draw one diameter through the centre and mark its two ends.",
                      "Draw a second diameter through the centre and mark its two ends. You now have four points.",
                      "Join the four points in order round the circle. The shape has 4 sides.",
                      "Look at the sides: opposite sides are equal.",
                      "Look at the angles: all four are right angles.",
                      "Check: opposite sides equal and four right angles are both true, so the shape is a "
                      "rectangle."],
                     "A rectangle: opposite sides are equal and all four angles are right angles.",
                     kind="prompt",
                     q_figure="A circle with its centre marked and two diameters drawn, with the four ends of the "
                              "diameters joined by thin dotted lines.",
                     s_figure="The same circle with the four-sided shape drawn in orange and a small square mark at "
                              "each of its four corners."),
                 FIO("pc.diff", "Play with Circles: a different pair of diameters",
                     "Try with a different pair of diameters. What do you notice about the shape that is formed?",
                     ["Turn the second diameter so that it crosses the first one at a different slant, and join the "
                      "four ends again.",
                      "Check the sides: opposite sides are still equal, but the lengths of the sides have changed.",
                      "Check the angles: all four are still right angles.",
                      "Try one more pair of diameters. It is a rectangle again.",
                      "Check: in every try the sides change but the four angles stay right angles, so the shape is "
                      "always a rectangle."],
                     "It is a rectangle again. The sides change, but opposite sides are equal and all four angles "
                     "are right angles.",
                     kind="prompt"),
                 FIO("pc.other", "Play with Circles: another four-sided shape",
                     "Is it possible to create a 4-sided shape other than a rectangle through this process?",
                     ["Every pair of diameters gives a rectangle: opposite sides equal and four right angles.",
                      "Turn one diameter all the way round the centre. The four ends always make a rectangle, and "
                      "never a different 4-sided shape.",
                      "When the two diameters cross at a right angle, all four sides are equal: a square. A square "
                      "is a special rectangle, so it is not a different shape.",
                      "Check: in every try the four angles were right angles, so the shape is a rectangle."],
                     "No. The shape is always a rectangle. When the diameters cross at a right angle it is a "
                     "square, which is a special rectangle.",
                     kind="prompt"),
                 FIO("cd.join", "Circle Designs: join the points",
                     "Look at the circle given below. It is marked with points 1 to 24. Join points 1 to 11, 11 to 2, "
                     "2 to 12, and so on till you reach back at 1.",
                     ["Find the move: 1 to 11 goes on by 10. 11 to 2 goes back by 9. 2 to 12 goes on by 10 again.",
                      "Keep the same moves, on by 10 and back by 9: 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, "
                      "8, 18, 9, 19, 10, 20, 11, 21, 12, 22, 13, 23, 14, 24, 15.",
                      "From 15 go on by 10: 16, 17 and on to 24, then 1. The thread is back at 1.",
                      "Count the lines: 14 pairs of moves make 14 × 2 = 28 lines, and the last move on by 10 makes "
                      "1 more line, so 28 + 1 = 29.",
                      "Check: the list of points has 30 places with the last 1, so there are 30 − 1 = 29 lines."],
                     "29 lines. The thread goes on by 10, back by 9, and is back at 1 after 29 lines.",
                     kind="prompt",
                     q_figure="A circle with 24 points numbered 1 to 24 round it, and the first lines 1 to 11, 11 to "
                              "2, 2 to 12 and 12 to 3 already drawn.",
                     s_figure="The 24-point circle with all 29 lines drawn as coloured threads, making a closed "
                              "design that comes back to point 1."),
                 FIO("cd.flower", "Circle Designs: the circle flower",
                     "Can you think of a way to make a design exactly like the image given here? Try to make it.",
                     ["Look at the picture: 5 circles of the same size, one in the middle and four round it.",
                      "Draw a circle with a compass and mark its centre.",
                      "Draw two diameters at right angles to each other. The circle now has 4 points on it.",
                      "Do not change the compass opening. Put the compass point on one of the 4 points and draw a "
                      "circle. Do the same on each of the other 3 points.",
                      "Count: 1 circle in the middle and 4 round it make 1 + 4 = 5 circles, all the same size.",
                      "Check: each of the 4 new circles passes through the centre of the middle circle, as in the "
                      "picture."],
                     "Sample answer: draw a circle and two diameters at right angles, then with the same compass "
                     "opening draw a circle at each of the 4 points. Your answer may differ.",
                     kind="prompt",
                     q_figure="A design of five overlapping circles of the same size: one in the middle and four "
                              "round it.",
                     s_figure="The finished design: a middle circle with four circles of the same size round it, "
                              "each drawn from one end of the two diameters.")],
          misconceptions=["M_CIRCLE_ANY"])],
    key_terms=["diameter", "circle", "points", "rectangle"]))

# ============================== T9 Cube Connections =======================================================
TOPICS.append(TOPIC(
    "T9", "M4", "Cube Connections", ["Cube Connections"], "Analyze",
    "Students use views of a cube to find opposite faces, fold a net, and count the small cubes of a painted big cube "
    "that have three, two, one or no painted faces.",
    "Two faces that touch the same two touching faces are opposite. A big painted cube has corner cubes with three "
    "painted faces, edge cubes with two, face middles with one and an inside with none.",
    [A("T9.C1", "Faces of a Cube and Its Net", "Analyze",
       "Students use two views of a cube to name the face opposite a given face and say which clue they used.",
       teach=["Predict first: in one view of a cube the heart touches the sun and the leaf. In another view the moon "
              "touches the sun and the leaf. Which face is opposite the heart?",
              "Faces that you see together in one view touch each other, so they are not opposite. Opposite faces "
              "are never seen together.",
              "The heart touches the sun and the leaf. The moon also touches the sun and the leaf. The sun and the "
              "leaf touch each other along one edge, and the two faces at the two ends of that edge are opposite.",
              "So the heart is opposite the moon.",
              "A net is a cube cut open and laid flat: 6 squares joined by their sides. In a straight row of 3 "
              "squares, the first and the third fold up to opposite faces.",
              "Rule: two faces that both touch the same two touching faces are opposite each other."],
       examples=[WE("A cube has six faces: sun, moon, heart, leaf, star and a plain face. In View 1 the sun is on top, "
                    "the heart is on the left and the leaf is on the right. In View 2 the sun is on top, the leaf is "
                    "on the left and the moon is on the right. Which face is opposite the heart?",
                    ["View 1: the heart touches the sun and the leaf.",
                     "View 2: the moon touches the sun and the leaf.",
                     "So the heart and the moon both touch the same two faces, the sun and the leaf.",
                     "The sun and the leaf touch each other along one edge. The two faces at the two ends of that "
                     "edge are opposite each other, and they are the heart and the moon.",
                     "So the heart is opposite the moon.",
                     "Check: opposite faces are never seen together. The heart is in View 1 and the moon is in View "
                     "2, and they never appear in the same view."],
                    "The moon is opposite the heart")],
       key_terms=["face", "cube", "opposite", "net", "view"], minutes=6),
     A("T9.C2", "Counting Small Cubes in a Big Cube", "Apply",
       "Students sort the small cubes of a big painted cube into corners, edges, face middles and inside, and count "
       "how many have three, two, one or no painted faces.",
       teach=["Predict first: a big cube is made of 4 × 4 × 4 small cubes and its whole outside is painted. How many "
              "small cubes have no paint at all?",
              "Sort the small cubes by where they sit: corners, edges, face middles and inside.",
              "A corner cube touches 3 faces of the big cube, so it has 3 painted faces. A cube has 8 corners.",
              "An edge cube that is not a corner has 2 painted faces. Each edge has 4 − 2 = 2 of them, and a cube "
              "has 12 edges.",
              "A face middle cube has 1 painted face. Each face has 2 × 2 = 4 of them, and a cube has 6 faces.",
              "An inside cube touches no outside face. Take away the outer layer all round and 2 × 2 × 2 = 8 cubes "
              "are left inside.",
              "Rule: corners 3 faces, edges 2 faces, face middles 1 face, inside none, and the four counts add up "
              "to all the small cubes."],
       examples=[WE("A big cube is made of 4 × 4 × 4 small cubes and all of its outside is painted. How many small "
                    "cubes have 3, 2, 1 and 0 painted faces?",
                    ["Count all the small cubes: 4 × 4 × 4 = 64.",
                     "3 painted faces: the corners. A cube has 8 corners, so 8 small cubes.",
                     "2 painted faces: the edge cubes that are not corners. Each edge has 4 − 2 = 2 of them and "
                     "there are 12 edges: 12 × 2 = 24 small cubes.",
                     "1 painted face: the face middle cubes. Each face has 2 × 2 = 4 of them and there are 6 faces: "
                     "6 × 4 = 24 small cubes.",
                     "0 painted faces: the cubes inside. Take off the outer layer: 2 × 2 × 2 = 8 small cubes.",
                     "Check: 8 + 24 + 24 + 8 = 64, all the small cubes."],
                    "3 faces: 8 small cubes. 2 faces: 24. 1 face: 24. No face: 8. Together 8 + 24 + 24 + 8 = 64")],
       key_terms=["corners", "edges", "small cubes", "painted", "inside"],
       misconceptions=["M_FORGET_INSIDE"], minutes=7),
     DOER("T9.C3", "Practice: Cube Lab", "cube_lab", "Apply",
          "Students find opposite faces of a cube, place pictures on a net, and count painted and removed small cubes "
          "in a cube frame and in a painted cube.",
          ["Faces seen together touch each other. Two faces that touch the same two touching faces are opposite.",
           "On a net, the first and the third square of a straight row of 3 fold up to opposite faces.",
           "In a painted big cube, sort the small cubes: corners, edges, face middles and inside.",
           "The inside cubes have no paint, and the counts of all the kinds add up to all the small cubes."],
          items=[FIO("cc.views", "Cube Connections: three views on the net",
                     "Here are three views of a cube. Can you draw them on the net in the correct order?",
                     ["Name the pictures: a green diamond on purple, an orange circle on blue, a red cross on cream, "
                      "a blue star on pink, and a plain brown face.",
                      "Faces seen together in one view touch each other, so they are next to each other and not "
                      "opposite.",
                      "The diamond face and the brown face both touch the circle face and the cross face, so the "
                      "diamond is opposite the brown face.",
                      "The circle face and the star face both touch the diamond face and the cross face, so the "
                      "circle is opposite the star.",
                      "A cube has 6 faces: diamond, brown, circle, star and two more. The third view shows a cross "
                      "next to the circle and the brown face, so the cross must be on two opposite faces.",
                      "Draw the net: a row of 4 squares with the brown face, the circle, the diamond and the star "
                      "from left to right, then a cross above the diamond square and a cross below it. Turn each "
                      "picture so it looks as it does in the views.",
                      "Check: in the row, brown and diamond have one square between them, and so do circle and star, "
                      "so each pair is opposite. The two crosses are above and below the diamond square, so they "
                      "are opposite too."],
                     "Sample answer: a net with a row of 4 squares, brown, circle, diamond, star, and a cross above "
                     "and below the diamond square. Your net may differ if it keeps the same opposite faces.",
                     kind="prompt",
                     q_figure="Three views of a cube with pictures on its faces, and a cross-shaped net of 6 empty "
                              "squares.",
                     s_figure="The cross-shaped net filled in: a row of four squares with the brown face, the circle "
                              "face, the diamond face and the star face from left to right, and a cross face above "
                              "and below the diamond square."),
                 FIO("cc.frames", "Cube Connections: cube frames",
                     "Here are some big solid cube frames. How many small cubes have been removed from each cube? "
                     "(a), (b), (c)",
                     ["(a): the cube is 3 by 3 by 3, so it has 3 × 3 × 3 = 27 small cubes.",
                      "A square tunnel goes through the middle of every pair of opposite faces. What is left is the "
                      "8 corners and 1 cube on each of the 12 edges: 8 + 12 × 1 = 20. Removed: 27 − 20 = 7.",
                      "(b): the cube is 4 by 4 by 4, so it has 4 × 4 × 4 = 64 small cubes. Left: the 8 corners and "
                      "2 cubes on each of the 12 edges: 8 + 12 × 2 = 32. Removed: 64 − 32 = 32.",
                      "(c): the cube is 5 by 5 by 5, so it has 5 × 5 × 5 = 125 small cubes. Left: the 8 corners and "
                      "3 cubes on each of the 12 edges: 8 + 12 × 3 = 44. Removed: 125 − 44 = 81.",
                      "Check: 20 + 7 = 27, 32 + 32 = 64 and 44 + 81 = 125."],
                     "(a): 7 small cubes; (b): 32 small cubes; (c): 81 small cubes.",
                     kind="prompt",
                     q_figure="Three solid cubes made of small cubes (3 by 3 by 3, 4 by 4 by 4 and 5 by 5 by 5) "
                              "marked (a), (b) and (c), each beside the same cube with a square tunnel cut through "
                              "every pair of opposite faces.",
                     s_figure="Each cube frame with its left-over small cubes counted: 20 left of 27, 32 left of 64 "
                              "and 44 left of 125."),
                 FIO("cc.paint", "Cube Connections: the painted cube",
                     "Nisha has glued 27 small cubes together to make a large solid cube. She paints the large cube "
                     "red. How many of the original small cubes have "
                     "(a): three faces painted red? ___ "
                     "(b): two faces painted red? ___ "
                     "(c): one face painted red? ___ "
                     "(d): no faces painted red? ___",
                     ["27 small cubes make a cube 3 by 3 by 3, because 3 × 3 × 3 = 27.",
                      "(a): three faces painted: the corners. A cube has 8 corners, so 8 small cubes.",
                      "(b): two faces painted: the cube in the middle of each edge. A cube has 12 edges and 1 cube "
                      "in the middle of each: 12 × 1 = 12 small cubes.",
                      "(c): one face painted: the cube in the middle of each face. A cube has 6 faces and 1 cube in "
                      "the middle of each: 6 × 1 = 6 small cubes.",
                      "(d): no face painted: the one cube hidden in the middle of the big cube, so 1 small cube.",
                      "Check: 8 + 12 + 6 + 1 = 27, all the small cubes."],
                     "(a): 8; (b): 12; (c): 6; (d): 1.",
                     kind="prompt",
                     s_figure="The 3 by 3 by 3 cube with its small cubes coloured by the number of painted faces: "
                              "8 corners, 12 edge cubes, 6 face middle cubes and 1 hidden cube in the middle.")],
          misconceptions=["M_FORGET_INSIDE"])],
    key_terms=["cube", "faces", "painted", "net"]))

# ============================== T10 Puzzle: Tanu's Shapes =================================================
TOPICS.append(TOPIC(
    "T10", "M4", "Puzzle: Tanu's Shapes", ["Puzzle"], "Apply",
    "Students solve a shape puzzle by placing the surest clue first, using one clue at a time to fill the next place, "
    "and checking every clue against the finished line.",
    "A clue puzzle is solved by placing the surest clue first and using one clue at a time to fill the next place. "
    "At the end, read every clue again to check the line.",
    [A("T10.C1", "Solving a Shape Puzzle with Clues", "Apply",
       "Students place five shapes in a line by using each clue in turn, starting with the surest clue, and check "
       "every clue against the finished line.",
       teach=["Predict first: five shapes stand in a line and one clue says the circle is at the left end. Which clue "
              "do you use first?",
              "Start with the clue that gives a sure place. The circle is at the left end, so the circle goes first.",
              "Then use each clue to fill the next place. Draw empty boxes and write each shape in its box as you "
              "place it.",
              "When a clue says a shape is between two others, it sits directly between them.",
              "At the end read every clue again and check it against the finished line.",
              "Rule: place what is surest first, then use each clue to fill the next place."],
       examples=[WE("Nisha puts 5 shapes in a line: a circle, a square, a triangle, a hexagon and a rectangle. Clues: "
                    "(a) The circle is at the left end. (b) The square is next to the circle. (c) The triangle is "
                    "between the square and the hexagon. (d) The rectangle is to the right of the hexagon. In what "
                    "order are the shapes?",
                    ["Draw 5 boxes in a line, numbered 1 to 5 from the left.",
                     "Clue (a): the circle is at the left end, so the circle is in box 1.",
                     "Clue (b): the square is next to the circle. Box 1 is the circle, so the square is in box 2.",
                     "Clue (c): the triangle is between the square and the hexagon. The square is in box 2, so the "
                     "triangle is in box 3 and the hexagon is in box 4.",
                     "Clue (d): the rectangle is to the right of the hexagon. Box 5 is the only box to the right of "
                     "box 4, so the rectangle is in box 5.",
                     "Check: the line is circle, square, triangle, hexagon, rectangle. Clue (a): the circle is at "
                     "the left end, yes. Clue (b): the square is next to the circle, yes. Clue (c): the triangle is "
                     "between the square and the hexagon, yes. Clue (d): the rectangle is to the right of the "
                     "hexagon, yes."],
                    "From left to right: circle, square, triangle, hexagon, rectangle")],
       key_terms=["puzzle", "clue", "shapes", "line"], minutes=5),
     DOER("T10.C2", "Pull it together and do it: Tanu's Shapes", None, "Apply",
          "Students place seven shapes in a line by using five clues one at a time, and check every clue against the "
          "finished line.",
          ["Place the surest clue first, then use one clue at a time to fill the next place.",
           "Between means directly between, and next to means touching.",
           "Read every clue again at the end to check the line."],
          items=[FIO("puz.tanu", "Puzzle: Tanu's seven shapes",
                     "Tanu arranged 7 shapes in a line. She used 2 squares, 2 triangles, 1 circle, 1 hexagon, and 1 "
                     "rectangle. Find her arrangement using the following clues: "
                     "(a): The square is between the circle and the rectangle. "
                     "(b): The rectangle is between the square and the triangle. "
                     "(c): The two triangles are next to the square. "
                     "(d): The hexagon is to the right of the triangle. "
                     "(e): The circle is to the left of the square.",
                     ["Draw 7 boxes in a line. The shapes are 2 squares, 2 triangles, 1 circle, 1 hexagon and 1 "
                      "rectangle, and 2 + 2 + 1 + 1 + 1 = 7.",
                      "Clues (a) and (e): the square is directly between the circle and the rectangle, and the "
                      "circle is to the left of the square. So three shapes sit side by side: circle, square, "
                      "rectangle.",
                      "Clue (b): the rectangle is between the square and the triangle. The square is on its left, so "
                      "a triangle is on its right: circle, square, rectangle, triangle.",
                      "Clue (c): the two triangles are next to the square. The first square already has the circle "
                      "and the rectangle beside it, so the triangles are on both sides of the other square: "
                      "triangle, square, triangle. One triangle is already placed, so the line goes on with square, "
                      "triangle: circle, square, rectangle, triangle, square, triangle.",
                      "Clue (d): the hexagon is to the right of the triangle. The only shape left is the hexagon, "
                      "and it goes at the right end: circle, square, rectangle, triangle, square, triangle, "
                      "hexagon.",
                      "Check: there are 2 squares, 2 triangles, 1 circle, 1 hexagon and 1 rectangle. Clue (a): the "
                      "square in box 2 is between the circle and the rectangle, yes. Clue (b): the rectangle in box "
                      "3 is between the square and the triangle, yes. Clue (c): the triangles in boxes 4 and 6 are "
                      "next to the square in box 5, yes. Clue (d): the hexagon is to the right of the triangle, yes. "
                      "Clue (e): the circle is to the left of the square, yes."],
                     "From left to right: circle, square, rectangle, triangle, square, triangle, hexagon.",
                     kind="prompt",
                     s_figure="Seven boxes in a line holding, from left to right, a circle, a square, a rectangle, "
                              "a triangle, a square, a triangle and a hexagon.")])],
    key_terms=["puzzle", "clue", "shapes"]))

# ============================== T11 Icosahedron and Dodecahedron ==========================================
TOPICS.append(TOPIC(
    "T11", "M4", "Icosahedron and Dodecahedron", ["Icosahedron and Dodecahedron"], "Understand",
    "Students count the faces, vertices and edges of a solid by ticking each one once, and find the edges by adding "
    "the sides of all the faces and halving.",
    "Count faces and vertices by ticking each one once. Count the edges by adding the sides of all the faces and "
    "halving, because every edge is the side of two faces.",
    [A("T11.C1", "Faces and Corners of a Solid", "Understand",
       "Students count the faces and vertices of a solid by ticking each one once, and say how many faces meet at a "
       "vertex.",
       teach=["Predict first: a matchbox is a solid. How many faces does it have, and how many corners? Count every "
              "one only once.",
              "A face is a flat side of a solid. The box has 6 faces, and all of them are rectangles. Opposite faces "
              "are the same.",
              "A vertex is a point where faces meet. It is the corner of the solid. At every vertex of the box, 3 "
              "faces meet.",
              "Count the vertices the same way, ticking each one once. The box has 8 vertices.",
              "Models of solids such as the icosahedron and the dodecahedron can be made from nets, or built from "
              "straws and clay. You count their faces and vertices in the same way.",
              "Rule: count face by face and tick each one; a vertex is a point where faces meet."],
       examples=[WE("A matchbox is a solid. How many faces does it have and what shape are they? How many faces meet "
                    "at each vertex? How many vertices does it have?",
                    ["Hold the box and tick each face once: top, bottom, front, back, left and right.",
                     "That makes 6 faces. Every face is a rectangle, and opposite faces are the same.",
                     "Look at one corner. A vertex is a point where faces meet. At this vertex 3 faces meet: the "
                     "top, the front and the right.",
                     "Every vertex of the box looks the same, so 3 faces meet at every vertex.",
                     "Count the vertices: 4 on the top face and 4 on the bottom face, so 4 + 4 = 8.",
                     "Check: ticking each face and each vertex once gives 6 faces and 8 vertices, with none missed "
                     "and none counted twice."],
                    "The box has 6 faces, all rectangles. 3 faces meet at every vertex, and it has 8 vertices")],
       ncert=["ico.intro"], key_terms=["faces", "vertex", "corners", "solid"], minutes=5),
     A("T11.C2", "Counting the Edges of a Solid", "Apply",
       "Students count the edges of a solid by adding the sides of all its faces and halving the total, because each "
       "edge is the side of two faces.",
       teach=["Predict first: the box has 6 faces and each face has 4 sides. If you add up all the sides, do you get "
              "the number of edges?",
              "An edge is a line where two faces meet. Count the sides of every face: 6 × 4 = 24 sides.",
              "But each edge is a side of 2 faces, so every edge was counted twice.",
              "So halve the count: 24 ÷ 2 = 12 edges.",
              "Check by counting the edges another way: 4 round the top, 4 round the bottom and 4 standing up "
              "between them, so 4 + 4 + 4 = 12.",
              "Rule: count the sides of all the faces, then halve, because each edge belongs to 2 faces."],
       examples=[WE("A box has 6 faces and each face has 4 sides. How many edges does the box have? How can you count "
                    "them without missing an edge or counting one twice?",
                    ["Count the sides of all the faces: 6 faces with 4 sides each, 6 × 4 = 24 sides.",
                     "An edge is the line where 2 faces meet, so every edge is a side of 2 faces.",
                     "So the 24 sides count every edge twice. Halve the count: 24 ÷ 2 = 12 edges.",
                     "Check another way: 4 edges round the top, 4 round the bottom and 4 standing up between them, "
                     "so 4 + 4 + 4 = 12."],
                    "The box has 12 edges. Count the sides of all the faces, 6 × 4 = 24, then halve it: 24 ÷ 2 = 12")],
       key_terms=["edges", "sides", "faces", "solid", "halve"],
       misconceptions=["M_COUNT_EDGE_TWICE"], minutes=5),
     DOER("T11.C3", "Practice: Solid Counter", "solid_counter", "Apply",
          "Students count the faces, vertices and edges of each solid, the icosahedron and the dodecahedron, and say "
          "how many faces meet at each vertex.",
          ["Tick each face and each vertex once, so none is missed and none is counted twice.",
           "A vertex is a point where faces meet. Count the faces that touch it.",
           "To count the edges, add the sides of all the faces and halve, because each edge is a side of 2 faces."],
          items=[FIO("ico.names", "Icosahedron and Dodecahedron: the names",
                     "What do these names mean? Once you count their faces, you will know.",
                     ["Count the faces of the icosahedron one by one, ticking each face once: there are 20.",
                      "Count the faces of the dodecahedron the same way: there are 12.",
                      "The word icosa means 20, dodeca means 12 and hedron means face. So an icosahedron is a solid "
                      "with 20 faces and a dodecahedron is a solid with 12 faces.",
                      "Check: the names give 20 and 12, and your ticks gave the same counts."],
                     "Icosahedron: icosa means 20, so it has 20 faces. Dodecahedron: dodeca means 12, so it has 12 "
                     "faces.",
                     kind="prompt",
                     q_figure="An icosahedron and a dodecahedron drawn side by side, each with its name under it."),
                 FIO("ico.shapes", "Icosahedron and Dodecahedron: shapes of the faces",
                     "What shapes do you see in an icosahedron and a dodecahedron? "
                     "Icosahedron: ___ Dodecahedron: ___ "
                     "Do all the faces look the same? "
                     "Icosahedron: ___ Dodecahedron: ___",
                     ["Turn the icosahedron and look at its faces. Each face has 3 sides: a triangle.",
                      "Turn the dodecahedron and look at its faces. Each face has 5 sides: a pentagon.",
                      "In the icosahedron all 20 faces are triangles of the same size. In the dodecahedron all 12 "
                      "faces are pentagons of the same size.",
                      "Check: one kind of face in each solid, so all the faces look the same."],
                     "Icosahedron: triangles; Dodecahedron: pentagons. Do all faces look the same? Icosahedron: yes; "
                     "Dodecahedron: yes.",
                     kind="prompt",
                     q_figure="The same two solids, an icosahedron and a dodecahedron, drawn side by side with "
                              "their names under them."),
                 FIO("ico.vertex", "Icosahedron and Dodecahedron: faces at a vertex",
                     "How many faces meet at a vertex (point)? "
                     "Icosahedron: ___ Dodecahedron: ___ "
                     "Do the same number of faces meet at each vertex? "
                     "Icosahedron: ___ Dodecahedron: ___",
                     ["Pick one vertex of the icosahedron and tick the faces that touch it: 5 triangles meet there.",
                      "Pick a different vertex of the icosahedron: again 5 faces meet.",
                      "Pick one vertex of the dodecahedron and tick the faces that touch it: 3 pentagons meet there.",
                      "Pick a different vertex of the dodecahedron: again 3 faces meet.",
                      "Check: in each solid the count is the same at every vertex you tried."],
                     "Icosahedron: 5 faces; Dodecahedron: 3 faces. The same number of faces meet at every vertex: "
                     "Icosahedron: yes; Dodecahedron: yes.",
                     kind="prompt",
                     q_figure="The same two solids, an icosahedron and a dodecahedron, drawn side by side with "
                              "their names under them."),
                 FIO("ico.edges", "Icosahedron and Dodecahedron: counting the edges",
                     "How many edges do you see? "
                     "Icosahedron: ___ Dodecahedron: ___ "
                     "How did you count them such that you do not miss out any edge or count an edge twice?",
                     ["Count the sides of all the faces. Icosahedron: 20 faces with 3 sides each, so 20 × 3 = 60 "
                      "sides.",
                      "Dodecahedron: 12 faces with 5 sides each, so 12 × 5 = 60 sides.",
                      "An edge is a side of 2 faces, so every edge was counted twice. Halve each count.",
                      "Icosahedron: 60 ÷ 2 = 30 edges. Dodecahedron: 60 ÷ 2 = 30 edges.",
                      "Check: every edge is shared by exactly 2 faces, so no edge is missed and none is counted "
                      "twice."],
                     "Icosahedron: 30 edges; Dodecahedron: 30 edges. Add the sides of all the faces (60), then halve "
                     "it, because each edge is a side of 2 faces.",
                     kind="prompt",
                     q_figure="The same two solids, an icosahedron and a dodecahedron, drawn side by side with "
                              "their names under them."),
                 FIO("ico.other", "Icosahedron and Dodecahedron: other solids",
                     "Can you think of any other solid shapes that have faces that look the same? Do the same number "
                     "of faces meet at each common vertex?",
                     ["Think of a solid whose faces are all the same. A cube is one: a dice has the shape of a cube.",
                      "A cube has 6 faces and all of them are squares of the same size.",
                      "Count the faces at one corner of the cube: 3 faces meet there.",
                      "Try another corner: again 3 faces meet. So yes, the same number of faces meet at every "
                      "vertex of a cube.",
                      "Check: the cube has 8 corners and 3 faces meet at each one."],
                     "Sample answer: a cube. All 6 faces are squares, and 3 faces meet at every vertex. Your answer "
                     "may differ.",
                     kind="prompt"),
                 FIO("ico.make", "Icosahedron and Dodecahedron: build with straws and clay",
                     "You can also build some solid shapes using straws or ice-cream sticks and clay or play dough. "
                     "Which shapes did you make?",
                     ["Choose a solid to build, for example a cube. A cube has 12 edges and 8 corners.",
                      "Each straw is one edge, so use 12 straws. Each ball of clay is one corner, so use 8 balls.",
                      "Put a ball of clay at the end of every straw and join 3 straws at each ball.",
                      "Check: 8 balls with 3 straws each give 8 × 3 = 24 straw ends, and 12 straws have 12 × 2 = 24 "
                      "ends. The counts match."],
                     "Sample answer: a cube frame made of 12 straws and 8 balls of clay. Your answer may differ.",
                     kind="prompt",
                     q_figure="Three solids built from straws, with a ball of clay at every corner.")],
          misconceptions=["M_COUNT_EDGE_TWICE"])],
    key_terms=["faces", "vertex", "edges", "solid"]))
