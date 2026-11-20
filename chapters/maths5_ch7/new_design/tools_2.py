# -*- coding: utf-8 -*-
"""Tool specs for T4, T5 and T6 of Class 5 Chapter 7 (Shapes and Patterns): Triangle Check, Rhombus Pieces and Tangram
Maker. Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. The pieces of the book's cut-out sheet are shown on screen. Numbers the plan adds are
labelled practice values. One activity at a time, large controls, Back and Next in the same place, visible progress,
Hint, Retry and Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "triangle_check": T(
        "tool_triangle_check", "Triangle Check", "manipulative",
        "Sort triangles made from the pieces of a rhombus by what you measure and fold: measure the sides with a ruler, "
        "fold to compare the angles, and see that equal sides go with equal angles. A triangle with 3 equal sides and 3 "
        "equal angles is equilateral, with 2 equal sides and 2 equal angles isosceles, and with no equal sides and no "
        "equal angles scalene. This tool measures and folds triangles that are given; it does not join pieces.",
        "The craft table seen from above, a warm wooden table drawn as a polished 3D isometric scene with soft shadows "
        "and gentle animation. A big paper triangle lies in the middle of the table and is the largest thing on screen. "
        "Along the left edge is a tray of 4 paper triangles made from the pieces of the rhombus, each with a number "
        "tag from 1 to 4: triangle 1 is 2 pieces joined along their middle sides (3 equal sides), triangle 2 is 2 "
        "pieces joined along their shortest sides (a wider triangle with 2 equal sides), triangle 3 is a single piece, "
        "and triangle 4 is 4 pieces joined into one big triangle. Tap a triangle in the tray to bring it to the middle. "
        "A wooden ruler lies across the top of the table. Drag the ruler onto a side, or tap a side, and the ruler "
        "slides along that side and a tag on the ruler shows its length. The ruler reads to the nearest whole cm, and "
        "the shortest side of a piece reads 4 cm, so the middle side of a piece reads about 7 cm and the longest side "
        "reads 8 cm (practice values). Beside the table a side list with 3 boxes shows the lengths measured so far for "
        "this triangle, and two boxes that hold the same number glow green with an equals sign between them. A Fold "
        "button sits under the triangle: tap a corner to choose it, and it glows orange; then tap Fold, and the "
        "triangle folds along the line from that corner to the middle of the opposite side. A fold read-out in words "
        "says whether the two halves match, and the corners that landed on each other show matching arcs, drawn in "
        "green when they match. An Unfold button opens the triangle again. A Halve button, switched on only for the book's questions, "
        "splits the triangle along the line from the chosen corner to the middle of the opposite side and slides "
        "the two halves apart so that the ruler can measure each half. Along the bottom edge are 3 sorting trays "
        "labelled Equilateral, Isosceles and Scalene. Drag a triangle into a tray; a tray takes a triangle only after "
        "its 3 sides are measured. An instruction strip at the top shows one sentence in large type, with progress "
        "dots under it. Hint, Retry (returns the triangle in the middle to its first state), Reset (returns all 4 "
        "triangles and clears the trays and the side list), Undo (takes back the last move), Back and Next are in the "
        "same places on every card. Read-outs: the side list, the number of equal sides found, the fold read-out, the "
        "tray counter (for example sorted 2 of 4), and the card number out of 7.",
        ["Look at the 2 triangles you made from 2 pieces in the video, triangle 1 with 3 "
         "equal sides and the wider triangle 2. Tap each one and say how many of its sides you think are equal, then "
         "press Next.",
         "For each of the 4 triangles, measure the 3 sides with the ruler, fold the triangle "
         "from each corner, and drag it into the tray it belongs in. See that the number of equal sides is also the "
         "number of equal angles.",
         "Answer 2 questions from your maths book: how many different types of triangles you can "
         "make from 2 pieces and what you notice about their sides, and how many sides of each half are equal when "
         "you halve the equilateral triangle."],
        ["Card 1: triangle 1 (2 pieces joined along their middle sides). Tap each of its 3 sides to measure "
         "it. What do the 3 sides read? Answer: 8 cm, 8 cm and 8 cm (practice values), so all 3 sides are equal.",
         "Card 2: fold triangle 1 from each of its 3 corners. What happens? Answer: the two halves match from "
         "every corner, so all 3 angles are equal. Triangle 1 has 3 equal sides and 3 equal angles: it is an "
         "equilateral triangle.",
         "Card 3: triangle 2 (2 pieces joined along their shortest sides). Measure its 3 sides and fold it "
         "from each corner. Answer: the sides read 8 cm, 8 cm and about 14 cm (practice values), so 2 sides are equal. "
         "The halves match only when you fold from the corner between the 2 equal sides, so 2 angles are equal. It is "
         "an isosceles triangle.",
         "Card 4: triangle 3 (a single piece). Measure its 3 sides and fold it from each corner. Answer: the "
         "sides read 4 cm, about 7 cm and 8 cm (practice values), so no 2 sides are equal. The halves never match, so "
         "no 2 angles are equal. It is a scalene triangle.",
         "Card 5: measure triangle 4 (4 pieces joined into one big triangle), then drag all 4 triangles into "
         "the trays. Answer: triangle 1 goes to Equilateral, triangle 2 to Isosceles, and triangles 3 and 4 to "
         "Scalene. Triangle 4 reads 8 cm, about 14 cm and 16 cm (practice values), so no 2 of its sides are equal.",
         "Challenge: 'How many different types of triangles can you make? Now, observe and measure the sides "
         "of these triangles. What do you notice?' Use triangles 1 and 2, which are made from 2 pieces. Answer: 2 types "
         "from 2 pieces: one with all 3 sides equal and a wider one with 2 equal sides. In both triangles, 2 sides are "
         "equal.",
         "Challenge: 'Now, cut the equilateral triangle in half. How many sides of each new triangle are "
         "equal?' Press Halve on triangle 1 and measure each half. Answer: none. The 3 sides of each half read 4 cm, "
         "about 7 cm and 8 cm (practice values), all different, so each half is a scalene triangle."],
        ["A side measured with the ruler shows its length in the side list. When 2 boxes hold the same number they glow "
         "green with an equals sign, and the tool says: Two sides are equal.",
         "A fold that matches shows the two halves lying on each other, matching arcs in green and the words: The two "
         "halves match, so these 2 angles are equal. A fold that does not match shows a soft amber note: The halves "
         "do not match from this corner. Try another corner.",
         "When all 3 corners of a triangle have been tried and none matches, the tool says: No fold matches, so no 2 "
         "angles are equal.",
         "A triangle dropped in a wrong tray slides back with a clue about what was measured, for example: Count the "
         "equal sides in your list. A triangle dropped in the right tray locks in with a soft chime. A triangle "
         "dropped before all its sides are measured slides back with: Measure all 3 sides first.",
         "After Halve the tool shows the two halves and lets the ruler measure each half. It never tells the count of "
         "equal sides before the student has measured.",
         "A wrong answer shows a soft amber note and never a red cross; the tool names the expected count only after "
         "the second try."],
        "All 4 triangles are measured, folded and sorted into the right trays, and the student has answered both of the "
        "book's questions: the types of triangles made from 2 pieces, and the number of equal sides in each half of the "
        "equilateral triangle.",
        ["rulerReadings", "foldResults", "trayAssignments", "halved", "challengeIndex"],
        ["M_ISO_ANGLES"],
        ["What is the card asking: how many sides of this triangle are the same length? Tap a side to measure it with "
         "the ruler.",
         "Measure all 3 sides and look for the same numbers. Then fold from a corner: if the two halves match, the 2 "
         "angles beside the fold are equal.",
         "For triangle 2, the first 2 sides read 8 cm and 8 cm, so 2 sides are equal. Fold from the corner between "
         "those 2 sides and see if the halves match.",
         "The tool measures the 3 sides for you and shows them in the side list. Read them, say how many are equal, "
         "and then a similar card follows."]),

    "rhombus_pieces": T(
        "tool_rhombus_pieces", "Rhombus Pieces", "manipulative",
        "Join 2, 3 and 4 triangular pieces of the rhombus whole side to whole side, count the sides round the outside "
        "of the shape made, and name it. A joined side hides inside and sides in one straight line make one longer "
        "side, so each new piece adds at most 1 side. This tool joins pieces and counts sides; it does not measure "
        "given triangles.",
        "The craft table seen from above, a warm wooden table drawn as a polished 3D isometric scene with soft shadows "
        "and gentle animation. In the middle lie the 4 triangular pieces of a rhombus, drawn large in blue, with a "
        "faint rhombus outline in the corner of the table that shows where they fit together. The pieces are the "
        "largest things on screen. Every piece is a triangle with 1 right angle, marked with a small square, and 3 "
        "different sides. To the right is a tracing sheet, a sheet of paper where the shape made is drawn as an "
        "outline with its outside edges thick. Under the table is a gallery strip with room for 6 small cards, where "
        "traced shapes are kept. Controls: drag a piece to move it; Turn turns the chosen piece one step at a time so "
        "that its sides line up with the other pieces; Flip flips the chosen piece over. A piece snaps whole side to "
        "whole side when one of its sides is brought near a side of the same length on another piece, with a soft "
        "click, and the joined sides turn into a dashed line inside the shape. Trace saves the shape to the tracing "
        "sheet and the gallery. Count lights each outside edge in orange one after the other while the side counter "
        "counts up. Name opens a label card with the names triangle, kite, parallelogram, rectangle, pentagon and "
        "hexagon to pick from. An instruction strip at the top shows one sentence in large type, with progress dots "
        "under it. Hint, Retry (separates the last piece), Reset (returns the 4 pieces to the rhombus), Undo, Back and "
        "Next are in the same places on every card. Read-outs: the number of pieces used (1 to 4), the live side "
        "counter for the outside of the shape (for example Sides: 4), the name label, the number of shapes in the "
        "gallery, and the card number out of 7. On the last card the six shape names each get Yes and No buttons.",
        ["Look at the kite and the parallelogram from the video. Make the kite from 2 "
         "pieces and count its sides, then press Next.",
         "Join 2 pieces to make a kite, a parallelogram and a rectangle, trace each one and "
         "count its sides; then join 3 pieces and watch the side counter.",
         "Answer 2 questions from your maths book about the shapes made from 3 pieces and from all "
         "4 pieces."],
        ["Card 1: join 2 pieces along their longest sides, with one piece flipped over. Trace it and count its "
         "sides. Answer: a kite with 4 sides. Side 1 = side 2 and side 3 = side 4, so the equal sides are adjacent.",
         "Card 2: join 2 pieces along their middle sides, with one piece turned half way round. Trace it and "
         "count its sides. Answer: a parallelogram with 4 sides. Its opposite sides are equal and none of its corners "
         "is a right angle, so it is not a rectangle.",
         "Card 3: join 2 pieces along their longest sides, with one piece turned half way round. Trace it "
         "and count its sides. Answer: a rectangle with 4 sides and 4 right angles. Its opposite sides are equal.",
         "Card 4: join 2 pieces along their middle sides, with one piece flipped over. Count the sides. "
         "Answer: 3 sides, not 4. The 2 shortest sides lie in one straight line and make one side. All 3 sides are "
         "equal: it is a triangle.",
         "Card 5: use 3 pieces. Take the triangle from card 4 and join 1 more piece, its longest side against "
         "a side of the triangle. How many sides does the shape have? Answer: 4 sides, because 3 − 1 + 2 = 4: the "
         "joined side hides inside and the new piece adds 2 sides.",
         "Challenge: 'Using 3 triangular pieces of the rhombus, try creating a (a) 3-sided shape, (b) 4-sided "
         "shape, and (c) 5-sided shape.' Build each one, trace it and read its sides. Answer: all three can be made. "
         "(a): join the wider triangle (2 pieces joined along their shortest sides) and 1 more piece, its longest "
         "side against one of the 2 equal sides, and flip the piece until the outside has 3 sides. (b): join the "
         "triangle with 3 equal sides and 1 more piece along a longest side, and the outside has 4 sides. (c): join 2 "
         "pieces along their shortest sides with one turned half way round, put the third piece with its longest side "
         "against one of the 2 long sides, and flip it until the outside has 5 sides. In all, 3 pieces make 13 "
         "different shapes, so your shapes may differ.",
         "Challenge: 'Which of these shapes can be made with all 4 pieces? Try and find out. (a) Square (b) "
         "Rectangle (c) Triangle (d) Pentagon (5-sided) (e) Hexagon (6-sided) (f) Octagon (8-sided)' Try each one, "
         "then press Yes or No for each name. Answer: a rectangle, a triangle, a pentagon and a hexagon can be made. A "
         "square and an octagon cannot: each piece adds at most 1 side, so 4 pieces make at most 3 + 3 = 6 sides, and "
         "no four-sided shape made of 4 pieces has 4 equal sides and 4 right angles."],
        ["When 2 sides touch whole side to whole side the pieces snap with a soft click, and the joined sides turn into "
         "a dashed line inside the shape. The tool says: Two sides are joined inside, so the outside has 4 sides.",
         "Count lights each outside edge in orange one by one and the side counter counts up. Sides that line up in one "
         "straight line count as one side.",
         "A piece brought near a side of a different length does not snap and wobbles gently with the note: These "
         "sides are not the same length. Try another side or turn the piece.",
         "A name that does not fit the shape shows a soft amber note with a clue about sides or angles, for example: "
         "Are the equal sides next to each other or opposite each other?",
         "On the book's cards the tool says what the shape has, for example: Your shape uses 3 pieces and has 5 "
         "sides. On the last card a Yes for a shape that has not been traced from all 4 pieces gets the note: Show "
         "it with all 4 pieces first. A wrong answer shows a soft amber note and never a red cross."],
        "The student has made a kite, a parallelogram and a rectangle from 2 pieces and counted their sides, and has "
        "answered both of the book's questions: the 3-, 4- and 5-sided shapes from 3 pieces, and which of the six shapes "
        "can be made from all 4 pieces.",
        ["piecePositions", "joinedSides", "outsideSideCount", "gallery", "challengeIndex"],
        ["M_PIECES_AREA", "M_KITE_OPPOSITE", "M_RECT_NOT_PARA"],
        ["What does the card ask you to make? Look at which sides of the pieces must touch.",
         "Join whole side to whole side: a longest side with a longest side, a middle side with a middle side, or a "
         "shortest side with a shortest side. Flip a piece, or turn it half way round, to change the shape.",
         "Count the sides round the outside only. A joined side hides inside, and 2 sides in one straight line count "
         "as 1 side.",
         "The tool shows one join for you and counts the outside sides, and then a similar card follows."]),

    "tangram_maker": T(
        "tool_tangram_maker", "Tangram Maker", "manipulative",
        "Name the seven tangram pieces and make target shapes from some or all of them: sort the pieces by their number "
        "of sides, make a square from 2 small triangles, and fill outlines by turning and flipping pieces, finding that "
        "a shape can often be made in more than one way.",
        "A wooden tangram tray on the craft table, drawn as a polished 3D isometric scene with soft shadows and gentle "
        "animation. The 7 pieces lie in the tray as flat coloured pieces, large and clear: 2 large triangles, 1 medium "
        "triangle, 2 small triangles, a square and a parallelogram. An outline of the shape to make sits in the middle "
        "of the table and is the largest thing on screen; the pieces are dragged onto it. Above the table, 4 outline "
        "cards sit in a row: a slanted parallelogram, a rectangle twice as long as it is tall, a triangle with a right "
        "angle at the top, and a four-sided shape with a short top and a long bottom. Tap a card to bring its outline "
        "to the middle. Controls: drag a piece to move it; Turn turns the chosen piece one step at a time; Flip flips "
        "the chosen piece over; a piece snaps to a side or a corner of the outline when it is close, with a soft "
        "click; tap a piece to show its name label (for example large triangle); Check looks at the outline. Two "
        "sorting trays labelled 3 sides and 4 sides appear on the sorting card. An instruction strip at the top shows "
        "one sentence in large type, with progress dots under it. Hint, Retry (clears the outline), Reset (returns all "
        "the pieces to the tray), Undo, Back and Next are in the same places on every card. Read-outs: the name label "
        "of the chosen piece, the number of pieces in the outline (for example pieces in the outline: 3), a message "
        "line that says what Check found, and the card number out of 5.",
        ["Look at the 7 pieces from the video, the 5 triangles and the 2 four-sided "
         "pieces. Tap one piece of each kind and say how many sides it has, then press Next.",
         "Tap each piece to read its name label, make a square from 2 small triangles, and "
         "fill the triangle outline in 2 different ways.",
         "Use some or all of the pieces to make the 4 shapes from your maths book, and find a way "
         "to fill each outline."],
        ["Card 1: sort the 7 pieces into the trays 3 sides and 4 sides, and tap each piece to read its name. "
         "Answer: 3 sides: 2 large triangles, 1 medium triangle and 2 small triangles (5 pieces). 4 sides: the square "
         "and the parallelogram (2 pieces). 5 + 2 = 7 pieces.",
         "Card 2: make a square from 2 small triangles. Answer: join the 2 small triangles along their "
         "longest sides. They make a square the same size as the tangram square.",
         "Card 3: fill the triangle outline (a right angle at the top) with 1 piece. Answer: the medium "
         "triangle fills it, with its longest side at the bottom.",
         "Card 4: clear the triangle outline and fill it again with 2 pieces. Answer: the 2 small triangles "
         "fill it, side by side with their right angles together at the middle of the bottom. A shape can be made in "
         "more than one way.",
         "Challenge: 'Now, use some or all of the pieces of your tangram set to make the following shapes. "
         "There may be more than one way to do it.' Fill all 4 outlines. Answer: one way for each, and yours may "
         "differ. The rectangle: the medium triangle in the middle with its longest side at the bottom and a small "
         "triangle in the gap on each side. The slanted parallelogram: the medium triangle on the left and the 2 small "
         "triangles together on the right. The triangle: the medium triangle. The four-sided shape with a short top "
         "and a long bottom: the parallelogram on the left and the medium triangle on the right, with the longest side "
         "of the medium triangle at the bottom. The rectangle can also be made from the square and the 2 small "
         "triangles."],
        ["A piece brought close to a side or a corner of the outline snaps in with a soft click. Pieces that overlap "
         "each other or stick out of the outline glow soft amber with the note: These pieces overlap. Move one piece.",
         "Check says what it sees. A full outline gets: The outline is full with no gap and no overlap. A gap glows "
         "amber with a clue, for example: A gap is left near the top corner. Which piece has a corner that fits it?",
         "After an outline is filled the tool says: These pieces fit the shape: more than one way is allowed. It then "
         "invites the student to press Retry and fill the same outline with a different set of pieces.",
         "On the sorting card a piece dropped in the wrong tray slides back with the clue: Count the sides of this "
         "piece. A name label that does not fit the piece shows the amber note: Look at the size and at the number of "
         "sides.",
         "A wrong answer shows a soft amber note and never a red cross; the tool names the piece it expected only "
         "after the second try."],
        "All 7 pieces are sorted and named, a square is made from 2 small triangles, the triangle outline is filled in 2 "
        "different ways, and all 4 outlines from the book are filled.",
        ["piecePositions", "pieceFlips", "pieceNames", "filledOutlines", "challengeIndex"],
        ["M_PIECES_AREA"],
        ["Look at the biggest corner of the outline: which piece has a corner like it?",
         "Place the largest piece that fits first, then fill the gaps that are left with smaller pieces. Turn or flip a "
         "piece if it does not fit.",
         "For the rectangle, lay the longest side of the medium triangle along the bottom. A small triangle fits the gap "
         "on each side.",
         "The tool places one piece in the outline for you, and then a similar card follows."]),
}
