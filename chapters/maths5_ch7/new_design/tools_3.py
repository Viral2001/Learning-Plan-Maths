# -*- coding: utf-8 -*-
"""Tool specs for T7, T8, T9 and T11 of Class 5 Chapter 7 (Shapes and Patterns): Shape Detective, Circle Stitcher, Cube
Lab and Solid Counter. Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. All tools share the craft table
look, one activity at a time, one instruction at a time, large controls, Back and Next in the same place, visible
progress, Hint, Retry and Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "shape_detective": T(
        "tool_shape_detective", "Shape Detective", "manipulative",
        "Drag the corners of one four-sided shape and switch two locks to see when it is a square, a rectangle, a "
        "rhombus or a parallelogram, then test seven statements about sides and angles and see that one statement can "
        "fit more than one shape.",
        "The detective's board on the craft table, drawn as a warm 3-D isometric scene with soft shadows and gentle "
        "animation. A pinboard in the middle holds one four-sided shape on a dot grid, and it is the largest thing on "
        "screen. The shape has four round corner handles that can be dragged. Its four sides show their lengths in "
        "centimetres next to them (practice values), and every corner that is a right angle carries a small square "
        "mark. To the left of the board are two locks: a Sides lock with three positions, Off, Opposite sides equal and "
        "All sides equal, and an Angles lock with two positions, Off and Right angles. A name plate above the shape "
        "reads Four-sided shape, Parallelogram, Rhombus, Rectangle or Square, whichever fits the shape now. Along the "
        "bottom lies a shelf of seven statement cards numbered 1 to 7 with the book's wording, and on the right are "
        "four shape cards: Square, Rectangle, Rhombus and Parallelogram. An instruction strip at the top shows one "
        "sentence in large type, with progress dots under it. Controls: drag a corner handle (the locks decide what "
        "the other corners do, so the sides or angles stay as set); switch each lock; drag a statement card onto the "
        "shape to test it, or onto a shape card to match it; Check, Hint, Undo, Retry (clears the last match), Reset "
        "(clears all matches and unlocks the shape), Back and Next in the same places on every card. Read-outs: the "
        "four side lengths, the right angle marks, the name plate, a tester light on each statement card that shows "
        "fits in green or look again in soft amber with the reason, and a match tally that counts how many statements "
        "are matched to each shape (for example Rhombus: 3).",
        ["Look at the four shapes from the video on the board. X has all sides 6 cm and "
         "all angles right angles. Y has sides 9 cm and 4 cm and all angles right angles. Z has all sides 7 cm and no "
         "right angles. W has sides 8 cm and 5 cm and no right angles. Name each shape and say what is the same in "
         "all four.",
         "Switch the locks one at a time and drag a corner to make a square, a rectangle, a "
         "rhombus and a parallelogram, reading the name plate each time. Then drag a statement card onto your shape "
         "and read whether it fits.",
         "The book's own question with the seven statement cards and the four shape cards. Match "
         "the statements with appropriate shapes. Do some of them describe more than one shape?"],
        ["Card 1: set the Sides lock to All sides equal and the Angles lock to Right angles, then drag a "
         "corner. What shape is it, and what happens to the sides when you drag? Answer: a square. The four sides grow "
         "or shrink together and stay equal, and the four angles stay right angles.",
         "Card 2: set the Sides lock to Opposite sides equal and the Angles lock to Right angles, then drag a "
         "corner. Which shape is it? Answer: a rectangle. Opposite sides stay equal, the four angles stay right "
         "angles, and the sides next to each other can be different.",
         "Card 3: set the Sides lock to All sides equal and the Angles lock to Off, then drag a corner until "
         "no angle is a right angle. Which shape is it? Answer: a rhombus. All four sides are equal and the angles "
         "are not right angles.",
         "Card 4: set the Sides lock to Opposite sides equal and the Angles lock to Off, then drag a corner "
         "so that the sides next to each other are different and no angle is a right angle. Which shape is it? "
         "Answer: a parallelogram. Opposite sides are equal and the angles are not right angles.",
         "Card 5: make each of your four shapes in turn and drag statement 6, 'My opposite angles are equal "
         "and so are my sides.', onto it. On which shapes does it fit? Answer: on all four, because each of them has "
         "opposite sides equal and opposite angles equal.",
         "Challenge: 'Match the statements with appropriate shapes. Do some of them describe more than one "
         "shape?' The statements are 1: All my angles are right angles, but all my sides are not equal. 2: All my "
         "sides are equal, but all my angles are not. 3: My opposite angles are equal, but my sides do not make a "
         "right angle. 4: Two pairs of sides are equal, but they do not make a right angle. 5: All my sides make "
         "right angles with each other and are equal. 6: My opposite angles are equal and so are my sides. 7: My "
         "opposite angles are equal and my sides make right angles. The shapes are Square, Rectangle, Rhombus and "
         "Parallelogram. Answer: 1 Rectangle; 2 Rhombus; 3 Rhombus and Parallelogram; 4 Parallelogram and Rhombus; 5 "
         "Square; 6 all four shapes; 7 Square and Rectangle. Yes, statements 3, 4, 6 and 7 describe more than one "
         "shape."],
        ["A statement card dropped on a shape shows a green tester light when it fits and a soft amber light when it "
         "does not, with the reason, for example: Statement 7 fits the rectangle: its opposite angles are equal and "
         "its sides make right angles.",
         "When a lock is set the shape keeps what the lock says while you drag. Under Opposite sides equal the other "
         "corners follow, so the opposite sides stay equal, and the name plate changes at once.",
         "A rectangle also has opposite angles equal: statement 7 fits it too, so the tool says that one statement "
         "can fit more than one shape.",
         "Statement 1 dropped on the square shows soft amber: all my angles are right angles is true for the square, "
         "but its sides are all equal, so all my sides are not equal does not fit.",
         "A wrong match slides back with a clue such as: Check the sides first. Are all four equal? It never shows a "
         "red mark. A shape card that has a match gets a small green tick and the tally counts it, for example: "
         "Statement 3 fits 2 shapes."],
        "All four shapes have been made with the locks, statements have been tested on them, all seven statements are "
        "matched, and the student has said which statements fit more than one shape.",
        ["sidesLock", "anglesLock", "cornerPositions", "namePlate", "statementMatches", "tally", "challengeIndex"],
        ["M_RECT_NOT_PARA"],
        ["Read the statement slowly. What does it say about the sides, and what does it say about the angles?",
         "Ask two questions about a shape: are all four sides equal, and are all four angles right angles? Use the "
         "locks to test each shape.",
         "Drag the statement onto the shape you think it fits and read the tester light. A statement can fit more "
         "than one shape, so try all four shapes.",
         "Statement 5 says all sides equal and all angles right angles. Set All sides equal and Right angles and the "
         "name plate says Square. The tool then matches statement 5 with Square so you can see how a match is made."]),

    "circle_stitcher": T(
        "tool_circle_stitcher", "Circle Stitcher", "manipulative",
        "Draw two diameters of a circle, join their four ends and check the sides and the angles to see that the shape "
        "is always a rectangle, then thread the points of a circle by a repeating move to make a string design that "
        "closes when the thread is back at the start.",
        "A compass board and a thread board on the craft table, drawn as a warm 3-D isometric scene with soft shadows "
        "and gentle animation. Three tabs at the top of the table switch between the Compass board, the Thread board "
        "and the Circle design mat. On the Compass board a circle with a diameter of 10 cm and its centre marked is "
        "the largest thing on screen. Two diameters pass through the centre and each end of each diameter is a round "
        "handle, so four points sit on the circle. Compass board controls: drag a handle to turn its diameter; a Join "
        "button that joins the four ends in order with a dotted line; a turn slider that turns the second diameter "
        "slowly all the way round; a Right angle snap that puts the second diameter at a right angle to the first. "
        "Compass board read-outs: the four side lengths in centimetres, a small square mark on every angle that is a "
        "right angle, and a name plate that reads Rectangle or Square. On the Thread board there is a circle with 12 "
        "points numbered 1 to 12 (practice values) or a circle with 24 points numbered 1 to 24, as in your maths "
        "book, with a tray of four coloured threads: teal, amber, green and reddish purple. Thread board controls: "
        "tap one point and then another to pull a thread between them; tap a colour in the tray to change the "
        "thread; Undo takes off the last thread. Thread board read-outs: a Move read-out that names the last move, "
        "for example on by 10 or back by 9, the number of lines threaded, and a Closed light that turns green when "
        "the thread is back at the first point. On the Circle design mat there is a circle with a radius of 3 cm "
        "(practice values), its centre marked and two diameters at right angles, so four points sit on the circle. "
        "Circle design mat controls: a Compass opening handle that sets the radius of the circle to draw, and a Draw "
        "circle button that draws a circle with its centre on the point you tap; read-outs: the compass opening in "
        "centimetres and the number of circles drawn. An instruction strip at the top shows one sentence in large "
        "type, with progress dots under it. Check, Hint, Undo, Retry (clears the last lines or the last circle), "
        "Reset (clears the board), Back and Next sit in the same places on every card.",
        ["Look at the 12-point circle from the video, where the thread goes 1, 5, 2, "
         "6, 3, 7 and on. Say the move: on by how many, then back by how many?",
         "On the Compass board draw two diameters, join the ends and read the sides and the "
         "angles, turn one diameter and look again, then make the diameters cross at a right angle. Then thread a "
         "12-point circle by a move of your own and try the compass on the design mat.",
         "The book's own questions. Is it possible to create a 4-sided shape other than a "
         "rectangle through this process? Then thread the 24 points: join points 1 to 11, 11 to 2, 2 to 12, and so "
         "on till you reach back at 1."],
        ["Card 1: on the Compass board drag the handles to make two diameters and press Join. Read the sides "
         "and the angles. What shape is it? Answer: a rectangle. Opposite sides are equal and all four angles are "
         "right angles.",
         "Card 2: turn the second diameter with the slider and watch the read-outs. What changes and what "
         "stays the same? Answer: the side lengths change, but the four angles stay right angles and the name plate "
         "stays Rectangle.",
         "Card 3: press Right angle snap. What shape is it now? Answer: a square. All four sides are equal "
         "and all four angles are right angles. A square is a special rectangle.",
         "Card 4 (practice values): on the Thread board with 12 points, join 1 to 4, 4 to 2, 2 to 5 and keep "
         "going until you are back at 1. What is the move, and how many lines did you thread? Answer: on by 3, then "
         "back by 2, and 19 lines.",
         "Card 5 (practice values): on the Circle design mat set the compass opening to 3 cm, the radius of "
         "the circle, and draw a circle with its centre on one of the 4 points. What do you see? Answer: a new circle "
         "of the same size that passes through the centre of the first circle.",
         "Challenge: 'Is it possible to create a 4-sided shape other than a rectangle through this "
         "process?' Turn the diameters into as many positions as you like before you answer. Answer: no. The shape is "
         "always a rectangle. When the two diameters cross at a right angle it is a square, which is a special "
         "rectangle.",
         "Challenge: 'Look at the circle given below. It is marked with points 1 to 24. Join points 1 to 11, "
         "11 to 2, 2 to 12, and so on till you reach back at 1.' Answer: 29 lines. The thread goes on by 10, then back "
         "by 9, and it is back at 1 after 29 lines."],
        ["When the four ends are joined, the read-outs show the four sides and the four angles and the tool says, for "
         "example: Opposite sides are equal and all four angles are right angles: a rectangle.",
         "When you turn a diameter the sides change and the tool says: The sides changed, the angles are still right "
         "angles, so it is still a rectangle.",
         "When the diameters cross at a right angle the name plate says Square and the tool says: All four sides are "
         "equal now, a square is a special rectangle.",
         "Each thread draws from one point to the next and the Move read-out names the move, for example: 1 to 11 is "
         "on by 10, 11 to 2 is back by 9. A tap on a point that does not follow the move gives a soft amber note such "
         "as: The move from 11 is back by 9, so look for point 2.",
         "When the thread is back at the first point the Closed light turns green and the tool shows the number of "
         "lines, for example 29 lines. On the design mat the new circle is drawn with its centre on the point you "
         "tapped and the tool says: Same opening, same size."],
        "The student has joined two diameters and seen a rectangle, turned a diameter and seen a rectangle again, made "
        "a square, threaded a closed design on the 12-point circle, answered the book's two questions and threaded the "
        "24 points back to point 1.",
        ["diameterOneEnd", "diameterTwoEnd", "joinedShape", "sidesAndAngles", "threadPath", "moveReadout", "lineCount",
         "compassOpening", "circlesDrawn", "challengeIndex"],
        ["M_CIRCLE_ANY"],
        ["What does the card ask: the shape made by the four ends, or the path of the thread? Look at what is on the "
         "board.",
         "For the diameters, check the sides and then the angles of the shape. For the thread, find the move from the "
         "first two lines.",
         "Turn one diameter a little and check again: what changes and what stays the same? For the thread, 1 to 11 is "
         "on by 10 and 11 to 2 is back by 9.",
         "The tool joins the four ends and shows the read-outs: opposite sides equal and four right angles. For the "
         "thread it draws 1 to 11 and 11 to 2, and you carry on: 2 to 12 is on by 10 again."]),

    "cube_lab": T(
        "tool_cube_lab", "Cube Lab", "manipulative",
        "Turn a cube and fold a net to say which faces are opposite, then paint and remove small cubes to count how "
        "many have three, two, one or no painted faces and how many are left in a cube frame.",
        "A cube, a net and small cubes on the craft table, drawn as a warm 3-D isometric scene with soft shadows and "
        "gentle animation. Three tabs at the top of the table switch between the Cube and net bench, the Paint bench "
        "and the Frame bench. On the Cube and net bench a big cube with a picture on each face is the largest thing "
        "on screen: a sun, a moon, a heart, a leaf, a star and a plain face. On the left sits a row of view cards: "
        "View 1 and View 2 from the video, and the three views of the book's question. On the right is a cross-shaped "
        "net of 6 empty squares, a row of 4 squares with one square above and one below the third square, with a "
        "tray of 6 picture tiles under it; the sixth tile can be set to show any one of the pictures. Cube and net "
        "controls: drag the cube to turn it; tap a view card to set the cube to that view; drag a picture tile onto a "
        "net square and tap the turn button to turn the picture; Fold folds the net into a cube and Unfold opens it. "
        "Cube and net read-outs: a line that names the three faces you can see, and, after Fold, a match light on "
        "each view card that says match or not yet with the reason. On the Paint bench a stack of small cubes "
        "(5 by 5 by 5 for practice values, 3 by 3 by 3 for the book's question) has a Paint button that paints the "
        "outside red, a Peel button that takes off one outer layer at a time, and a tap on any small cube lifts it "
        "out into one of four tally boxes: three painted faces, two, one and none. Paint bench read-outs: the number of "
        "small cubes in the stack and the number in each tally box. On the Frame bench a stack of small cubes (6 by 6 "
        "by 6, practice values) has a tunnel width control and a Cut tunnels button that removes a square tunnel "
        "through every pair of opposite faces; read-outs: the cubes removed and the cubes left. An instruction strip "
        "at the top shows one sentence in large type, with progress dots under it. Check, Hint, Undo, Retry (unfolds "
        "the net or puts back the last cubes), Reset (clears the bench), Back and Next sit in the same places on "
        "every card.",
        ["Look at View 1 and View 2 of the cube from the video, with the sun, the moon, "
         "the heart and the leaf, and at the 4 by 4 by 4 cube with 64 small cubes. Say which faces touch the heart.",
         "Turn the cube and find the face opposite the heart, fold a net, and paint and peel a "
         "stack of small cubes. Then cut a tunnel through a frame and count what is removed.",
         "The book's own questions. Here are three views of a cube. Can you draw them on the net "
         "in the correct order? Then Nisha's 27 small cubes painted red."],
        ["Card 1: tap View 1 and View 2 and turn the cube. Which face is opposite the heart? Answer: the "
         "moon. Both the heart and the moon touch the sun and the leaf.",
         "Card 2 (practice values): drop the six pictures on the net: the heart, the leaf, the moon and the "
         "plain face along the row of 4 squares from left to right, the sun above the third square and the star below "
         "it. Press Fold. Which faces are opposite? Answer: the cube matches View 1 and View 2. The heart and the moon "
         "have one square between them in the row, so they are opposite, and so are the leaf and the plain face. The sun above "
         "and the star below the third square are opposite too.",
         "Card 3 (practice values): on the Paint bench take the 5 by 5 by 5 stack, press Paint, then Peel and "
         "sort the small cubes. How many have three, two, one and no painted faces? Answer: 8, 36, 54 and 27, because "
         "12 × 3 = 36, 6 × 9 = 54 and 3 × 3 × 3 = 27, and 8 + 36 + 54 + 27 = 125.",
         "Card 4 (practice values): on the Frame bench take the 6 by 6 by 6 stack and cut a tunnel 4 by 4 "
         "through every pair of opposite faces. How many small cubes are removed? Answer: 160. What is left is the 8 "
         "corners and 4 cubes on each of the 12 edges, 8 + 12 × 4 = 56, and 6 × 6 × 6 = 216, so 216 − 56 = 160 are "
         "removed.",
         "Challenge: 'Here are three views of a cube. Can you draw them on the net in the correct order?' "
         "Answer: the diamond face is opposite the brown face, the circle face is opposite the star face, and the "
         "cross is on two opposite faces. Sample net: a row of 4 squares with the brown face, the circle, the diamond "
         "and the star from left to right, and a cross above and below the diamond square. Your net may differ if it "
         "keeps the same opposite faces.",
         "Challenge: 'Nisha has glued 27 small cubes together to make a large solid cube. She paints the "
         "large cube red. How many of the original small cubes have (a) three faces painted red? (b) two faces "
         "painted red? (c) one face painted red? (d) no faces painted red?' Answer: (a) 8, (b) 12, (c) 6 and (d) 1, "
         "because 8 + 12 + 6 + 1 = 27."],
        ["After Fold the tool says which views match, for example: View 1 matches. In View 2 the leaf and the moon "
         "should be next to the sun: look at what touches the sun.",
         "When you turn the cube the tool names the faces you see and says: Faces you see together touch each other, "
         "so they cannot be opposite.",
         "Both the heart and the moon touch the sun and the leaf: they are opposite. The tool shows this when the two "
         "views are set one after the other.",
         "On the Paint bench a small cube lifted into the wrong tally box slides back with a clue such as: Count the "
         "painted faces of this cube. How many outside faces does it touch? The cube hidden in the middle has none.",
         "On the Frame bench the tool says how many were removed and how many are left, and a count that does not add "
         "up gets a soft amber note, for example: Removed and left must make 216. A wrong answer is never shown in "
         "red."],
        "The student has turned the cube to find the opposite of the heart, folded the net, sorted a painted stack, cut "
        "a tunnel in a frame, placed the book's three views on a net and sorted Nisha's 27 small cubes by painted "
        "faces.",
        ["cubeTurn", "viewCard", "netSquares", "folded", "smallCubesPainted", "tallyBoxes", "removedCubes",
         "challengeIndex"],
        ["M_FORGET_INSIDE"],
        ["Which faces can you see together in one view? Faces seen together touch each other. For small cubes, ask "
         "how many outside faces a cube touches.",
         "Opposite faces never touch and are never seen together. Look for two faces that touch the same two "
         "touching faces. For small cubes, sort them: corner, edge, face middle, inside.",
         "Turn the cube to the view you need and name the faces you see. For small cubes, count the corners, then the "
         "cubes on each edge, then the cubes in the middle of a face, then the cubes inside.",
         "The tool places one picture on the net, the diamond in the third square of the row, so you can see how the "
         "other pictures fit round it. For small cubes it peels off the outer layer so you can count the cubes left "
         "inside."]),

    "solid_counter": T(
        "tool_solid_counter", "Solid Counter", "manipulative",
        "Tick the faces, vertices and edges of a box and then of the icosahedron and the dodecahedron, one tick for "
        "each, and find the number of edges by adding the sides of all the faces and halving, so that nothing is "
        "missed and nothing is counted twice.",
        "A turntable on the craft table with clay models, drawn as a warm 3-D isometric scene with soft shadows and "
        "gentle animation. The solid on the turntable is the largest thing on screen. Three model cards on the left "
        "choose the solid: Box, Icosahedron and Dodecahedron. An instruction strip at the top shows one sentence in "
        "large type, with progress dots under it. Controls: drag the turntable to turn the solid so that every side "
        "can be seen; a mode switch with Faces, Vertices and Edges that chooses what a tap ticks; tap a face, a "
        "vertex or an edge to tick it with an amber mark and tap it again to take the tick off; a Tally button that "
        "opens a strip adding the sides of every ticked face, and a Halve button on that strip; Check, Hint, Undo, "
        "Retry (clears the ticks of this card), Reset (clears the solid), Back and Next in the same places on every "
        "card. Read-outs: three counters, faces ticked, vertices ticked and edges ticked; a faces at this vertex "
        "read-out that lights up the faces touching a ticked vertex and shows their number; the sides tally, for "
        "example 6 faces × 4 sides = 24, and the halved number under it; and a line that says whether any face, "
        "vertex or edge is still unticked.",
        ["Look at the box from the video. Tick each of its faces once and say how many "
         "faces and how many vertices it has, and how many faces meet at a vertex.",
         "Count the edges of the box by adding the sides of all the faces and halving, then "
         "switch to the icosahedron and the dodecahedron and tick their faces.",
         "The book's own questions. How many faces meet at a vertex (point)? Then: How many edges "
         "do you see? How did you count them such that you do not miss out any edge or count an edge twice?"],
        ["Card 1: on the box choose Faces and tap each face once. How many faces are there, and what shape "
         "are they? Answer: 6 faces, all rectangles.",
         "Card 2: on the box choose Vertices and tap one vertex, then count all the vertices. How many faces "
         "meet at a vertex, and how many vertices are there? Answer: 3 faces meet at every vertex, and the box has 8 "
         "vertices.",
         "Card 3: on the box press Tally, then Halve. How many edges does the box have? Answer: 6 × 4 = 24 "
         "sides, and 24 ÷ 2 = 12 edges.",
         "Card 4: switch to the icosahedron, choose Faces and tick every face. How many faces, and what "
         "shape are they? Answer: 20 faces, all triangles.",
         "Card 5: switch to the dodecahedron, choose Faces and tick every face. How many faces, and what "
         "shape are they? Answer: 12 faces, all pentagons.",
         "Challenge: 'How many faces meet at a vertex (point)?' Tap vertices on the icosahedron and on the "
         "dodecahedron and compare. Answer: the icosahedron has 5 faces at a vertex and the dodecahedron has 3, and "
         "the same number of faces meet at every vertex of each solid.",
         "Challenge: 'How many edges do you see? How did you count them such that you do not miss out any "
         "edge or count an edge twice?' Answer: 30 edges in each solid. Add the sides of all the faces, 20 × 3 = 60 "
         "for the icosahedron and 12 × 5 = 60 for the dodecahedron, then halve it, because each edge is a side of 2 "
         "faces: 60 ÷ 2 = 30."],
        ["Each tick turns the face, vertex or edge amber and the counter goes up by one. Ticking the same one again "
         "shows a soft amber note: This face is already counted.",
         "A tap on a vertex lights the faces that touch it and says, for example: 5 faces meet at this vertex.",
         "The Tally strip adds the sides of the ticked faces and says, for example: 20 faces with 3 sides is 60. "
         "Every edge is counted twice, so halve it: 30 edges.",
         "When every face is ticked the tool says: All 20 faces are counted, none is missed. If one is still unticked "
         "it turns the solid to show where it is and says: One face is still hidden at the back.",
         "A wrong count shows a soft amber note and never a red cross; the tool names the number it expected only "
         "after the second try."],
        "The student has ticked the faces and vertices of the box, found its edges by adding the sides and halving, "
        "ticked the faces of the icosahedron and the dodecahedron, and answered the book's two questions about the "
        "faces at a vertex and the edges.",
        ["solidChoice", "tickMode", "ticks", "faceCount", "vertexCount", "edgeCount", "sideTally", "challengeIndex"],
        ["M_COUNT_EDGE_TWICE"],
        ["What are you counting: faces, vertices or edges? Choose the mode first.",
         "Tick each one once and watch the counter, and turn the solid so that no face is hidden. For edges, think "
         "about how many faces share each edge.",
         "For the edges, add the sides of all the faces, then halve it. Each edge is a side of how many faces?",
         "The tool ticks one face and then one edge and starts the sides tally, so you can see the method: add the "
         "sides of the faces, then halve."]),
}
