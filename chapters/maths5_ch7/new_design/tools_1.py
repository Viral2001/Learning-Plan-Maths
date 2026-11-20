# -*- coding: utf-8 -*-
"""Tool specs for T1, T1B, T2 and T3 of Class 5 Chapter 7 (Shapes and Patterns): Mat Weaver (the free try of the
intro, right after the hook), Weave Rules, Fit Around a Point and Pattern Tiler. Specs only; the tool pages are built
later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values.
The one chapter theme is The Craft Table. One activity at a time, one instruction at a time, large controls, Back and
Next in the same place, visible progress, Hint, Retry and Reset always present, immediate specific feedback that is
never red."""
from topics_common import T

TOOLS = {
    # ============================== Tool 1: Mat Weaver (free try after the hook) ===========================
    "mat_weaver": T(
        "tool_mat_weaver", "Mat Weaver", "manipulative",
        "Feel what over and under mean by weaving paper strips across a mat with slits, and see that the words for a "
        "row come from what you wove: 1 under, 1 over, repeat, and the next row swaps. This is the free first try of "
        "the chapter, so it asks and shows; the video that follows names how to describe a row in words.",
        "The craft table, drawn as a warm 3D isometric scene with soft shadows and gentle animation. A coloured "
        "paper mat with 8 upright slits (practice values) lies in the middle of the table and is the largest thing on "
        "screen. An instruction strip at the top shows one sentence in large type, with progress dots under it. To the "
        "right of the mat a tray holds the 8 paper strips of your maths book, 4 blue and 4 yellow, each one longer "
        "than the mat is wide. The strip in hand lies across the first free row of the mat, and every place where it "
        "crosses a slit is a round tap spot. Controls: tap a crossing to switch it between over (the strip lies on "
        "top and shows its colour) and under (the strip goes below the slit paper and hides); an Alternate button "
        "that sets the whole strip to 1 under, 1 over, and so on; a Next strip button that fixes the strip and "
        "brings the next one from the tray; Undo, Hint, Retry (clears the strip in hand), Reset (clears the mat), "
        "Back and Next in the same places on every card. Read-outs: a row read-out in words under the mat that grows "
        "as the strip is woven, for example Row 1: 1 under, 1 over, 1 under, 1 over, ... (repeat), with the word "
        "repeat added once the same group has come twice; a counter strips woven out of 8; and a card number out of "
        "6.",
        ["Think back to the woven baskets of the story, each one with its own weaving "
         "pattern. Look at the paper mat with 8 slits and the strip in hand. Tap one crossing twice to see the strip "
         "go over (it shows on top) and then under (it hides), then press Next.",
         "Weave strip 1 going 1 under and 1 over, weave strip 2 going 1 over and 1 under, "
         "guess Row 3 before you weave it, press Alternate to finish all 8 strips, then press Reset and try a rule of "
         "your own (practice values: 2 over, 1 under).",
         "Answer the open question of the story. Weave your own mat and describe Row 1 and Row 2 "
         "in words, as your maths book does."],
        ["Card 1: weave strip 1 across the 8 slits going 1 under and 1 over, again and again. Read the row "
         "read-out. Answer: the strip goes under slit 1, over slit 2, under slit 3, over slit 4, and so on, so it "
         "goes over slits 2, 4, 6 and 8: 4 overs and 4 unders, and 4 + 4 = 8 slits. The read-out says Row 1: 1 "
         "under, 1 over, 1 under, 1 over, ... (repeat).",
         "Card 2: weave strip 2 across the next row going 1 over and 1 under, again and again. Compare it "
         "with the row above. Answer: strip 2 goes over slits 1, 3, 5 and 7, and the read-out says Row 2: 1 over, 1 "
         "under, 1 over, 1 under, ... (repeat). Row 2 does the opposite of Row 1: where Row 1 goes over, Row 2 goes "
         "under.",
         "Card 3: guess first. What will Row 3 be if it swaps over and under in Row 2? Tap your guess, then "
         "weave strip 3. Answer: Row 3 is the same as Row 1, because swapping Row 1 gave Row 2 and swapping Row 2 "
         "gives Row 1 back: 1 under, 1 over, 1 under, 1 over, ... (repeat).",
         "Card 4: press Alternate to weave strips 4 to 8, each strip doing the opposite of the strip above. "
         "How many strips are blue and how many are yellow? Answer: 4 blue and 4 yellow, because 4 + 4 = 8 strips. "
         "The odd rows go like Row 1 and the even rows go like Row 2, so the mat shows small checks.",
         "Card 5 (practice values): press Reset. Weave Row 1 with a rule of your own: 2 over, 1 under, again "
         "and again, then weave Row 2 by swapping over and under. Answer: Row 1: 2 over, 1 under, 2 over, 1 under, "
         "... (repeat) goes over, over, under, over, over, under, over, over across the 8 slits. Row 2 swaps it: 2 "
         "under, 1 over, 2 under, 1 over, ... (repeat).",
         "Challenge: 'We can describe the pattern of the above weave as follows.' Weave your own mat, then "
         "describe Row 1 and Row 2 in words. Answer: for the mat woven with 1 under and 1 over, Row 1: 1 under, 1 "
         "over, 1 under, 1 over, ... (repeat) and Row 2: 1 over, 1 under, 1 over, 1 under, ... (repeat). A rule of "
         "your own is fine too, if the words match what you wove. Your words may differ."],
        ["Tapping a crossing slides the strip over or under with a gentle movement, and the row read-out adds the "
         "step in words.",
         "A second strip that does the opposite of the row above gets a soft green note: This strip goes over where "
         "the last one goes under: the rows swap.",
         "A strip that copies the row above gets a soft amber note: This strip goes over where the strip above goes "
         "over. Look again: should this row swap?",
         "Alternate fills a strip with the pattern and says: 1 under, 1 over, again and again. Read the words in the "
         "read-out.",
         "When the student describes a row that does not match the read-out, the tool shows the row with each step "
         "numbered and says: Count the steps that stay together. It never shows a red cross."],
        "Strips 1 and 2 are woven with the rows swapped, all 8 strips are woven, the student has woven and read a row "
        "of their own rule, and has described Row 1 and Row 2 of their own mat in words.",
        ["stripInHand", "crossings", "rowReadOut", "stripsWoven", "ownRule", "cardIndex"],
        ["M_WEAVE_SAME"],
        ["What does the strip in hand do at each slit: does it lie on top, or go below the slit paper? Look at the "
         "first crossing and tap it.",
         "Go slit by slit. For Row 1 the strip goes under, then over, then under, then over. Say the steps out loud "
         "as you tap.",
         "For Row 1 tap slit 1 for under, slit 2 for over, slit 3 for under, and keep going to slit 8. The read-out "
         "should say 1 under, 1 over, ... (repeat).",
         "Press Alternate. The strip weaves itself: under, over, under, over across the 8 slits. Now read the "
         "read-out and say the row in your own words."]),

    # ============================== Tool 2: Weave Rules ====================================================
    "weave_rules": T(
        "tool_weave_rules", "Weave Rules", "manipulative",
        "Build the rows of a weave from rule cards (a count, over or under, repeat) and find the row where the "
        "pattern starts to repeat. The cards make the rule itself the thing that students handle, so long rules and "
        "many rows are quick to try.",
        "A weaving frame with 16 columns on the craft table, drawn as a warm 3D isometric scene with soft shadows "
        "and gentle animation. The grid of crossings, 16 columns wide, is the largest thing on screen: in each row "
        "a crossing shows the strip colour where the strip goes over and cream where it goes under. An instruction "
        "strip at the top shows one sentence in large type, with progress dots under it. Above each row sits a rule "
        "line where cards are dropped in order. A shelf under the frame holds the rule cards: the number cards 1, 2 "
        "and 3, the word cards over and under, a card (repeat) and a card (do not repeat). A small target card on the "
        "right shows the mat to copy when a challenge gives one. The frame can show 10, 12 or 16 slits: the cards of "
        "a challenge set the number. Controls: drag cards into the rule line of a row in order, for example 2, over, "
        "1, under, (repeat); a Weave button that colours the row from its cards; a Rows repeat from here button to "
        "tap on the row that is the same as Row 1; Undo, Hint, Retry (clears the row being built), Reset (clears the "
        "frame), Back and Next in the same places on every card. Read-outs: a row list on the left that gives every "
        "woven row in words, for example Row 3: 2 under, 1 over (repeat); a slit counter for the row being built (for "
        "example 10 of 10 slits); the number of rows woven; a marker under the row chosen as the repeat; and a card "
        "number out of 6.",
        ["Look at the row from the video, Row 1: 3 over, 2 under (repeat), woven on 10 "
         "slits, and at Row 2 that swaps it (practice values). Tap a card of the rule line to see which slits it "
         "covers, then press Next.",
         "Build rows from the cards (practice values), swap a row, then weave three rows "
         "where each row is the row above moved one slit to the right, and tap the row that is the same as Row 1. "
         "Say after how many rows the pattern repeats.",
         "Weave the four rules of your maths book and say when the pattern repeats, then work "
         "out the steps of a design until it starts repeating."],
        ["Card 1 (practice values, 12 slits): build Row 1 from the cards: 1 over, 3 under (repeat). Press "
         "Weave. How many slits go over and how many go under? Answer: the row goes over, under, under, under, over, "
         "under, under, under, over, under, under, under, so 3 slits go over and 9 go under, and 3 + 9 = 12.",
         "Card 2 (practice values, 12 slits): build Row 2 so that it swaps over and under in Row 1. Answer: "
         "Row 2: 1 under, 3 over (repeat), which goes under, over, over, over, under, over, over, over, under, over, "
         "over, over.",
         "Card 3 (practice values, 12 slits): build Row 1: 2 over, 1 under (repeat). Then build Row 2 as Row "
         "1 moved one slit to the right, so that the last step comes round to the front. Answer: Row 2: 1 under (do "
         "not repeat), 2 over, 1 under (repeat), which goes under, over, over, under, over, over, under, over, over, "
         "under, over, over.",
         "Card 4 (practice values, 12 slits): build Row 3 and Row 4 in the same way, each one moved one slit "
         "to the right. Which row is the same as Row 1? Tap Rows repeat from here on it. Answer: Row 3: 1 over (do "
         "not repeat), 1 under, 2 over (repeat). Row 4 is the same as Row 1: 2 over, 1 under (repeat). The rows "
         "repeat from Row 4, after 3 rows.",
         "Challenge: 'Try to weave a pattern, using the rules given below. Row 1: 2 over, 1 under, 2 over, "
         "1 under, ... (repeat). Row 2: 1 under (do not repeat), 3 over, 3 under, 3 over, 3 under, ... (repeat). Row "
         "3: 2 under, 1 over, 2 under, ... (repeat). Row 4: 1 over (do not repeat), 3 under, 3 over ... (repeat). "
         "Continue weaving in this order.' Build the four rows on 16 slits, then keep weaving. When does the "
         "pattern repeat? Answer: Row 3 swaps over and under in Row 1 and Row 4 swaps Row 2, and Row 5 follows the "
         "first rule again, so it is the same as Row 1. The pattern repeats after 4 rows.",
         "Challenge: 'Can you work out the steps for any of these designs and weave the pattern? Write the "
         "steps of the pattern in your notebook for each row until it starts repeating.' Choose the design on the "
         "target card, read it row by row, and build each row from the cards, so that the row list is your notebook. "
         "Answer: for the design of purple strips on 16 slits, Row 1: 1 under (do not repeat), 3 over, 3 under "
         "(repeat), then Rows 2 to 6 follow the target card, and Row 7 is the same as Row 1, so it repeats after 6 "
         "rows. The design of teal and lavender repeats after 4 rows. Your row list may differ in which design you "
         "choose."],
        ["A row built from cards is woven with a gentle slide and the row list adds its words, for example Row 1: 3 "
         "over, 2 under (repeat).",
         "If the row does not fill the slits, a soft amber note says how many slits are left, for example: Your row "
         "covers 9 of 10 slits: one more step is needed.",
         "A row that swaps over and under in the row above gets a soft green note: Row 3 swaps over and under in Row "
         "1: 2 under, 1 over.",
         "When a row is tapped as the repeat but is not the same as Row 1, the tool lays the two rows one over the "
         "other and shows the first slit where they differ, in soft amber. It says: Not the same as Row 1 yet. Move "
         "on to the next row.",
         "When a row starts its pattern in the same place as the row above, the tool says: Each new row can begin at a "
         "different place in the pattern. Compare where the first group starts."],
        "The rows of every card are built from cards and woven, the repeat is found on the rows of practice values "
        "and on the four rules, and the student has written the steps of a design until it repeats.",
        ["ruleCards", "rowRules", "wovenRows", "slitCount", "repeatRow", "targetCard", "cardIndex"],
        ["M_WEAVE_SAME", "M_WEAVE_RESTART"],
        ["Read the first row of the rule: how many slits does each step cover, and does the strip go over or under?",
         "Write a row, then the next row, and compare each new row with Row 1 to see where the pattern starts again.",
         "Build Row 1 from the cards and press Weave. Then build Row 2 as Row 1 moved one slit to the right: the last "
         "step comes round to the front. Compare with Row 1 again.",
         "The tool fills Row 2 for you. Look at where its first group starts, then build Row 3 yourself by moving "
         "that row one slit more."]),

    # ============================== Tool 3: Fit Around a Point =============================================
    "fit_around_point": T(
        "tool_fit_around_point", "Fit Around a Point", "manipulative",
        "Fit regular triangles, squares, pentagons, hexagons and octagons around a point and count how many fit, "
        "watching for the gap and the overlap: some shapes fill the space exactly, and others leave a gap that is too "
        "small to use.",
        "A tile mat on the craft table, drawn as a warm 3D isometric scene with soft shadows and gentle animation. A "
        "cream mat with one orange point marked in the middle is the largest thing on screen, and the shapes are "
        "placed on it. On a shelf at the left sit cutouts of five shapes, each with every side the same length: an "
        "equilateral triangle, a square, a regular pentagon, a regular hexagon and a regular octagon. An instruction "
        "strip at the top shows one sentence in large type, with progress dots under it. Controls: drag a shape so "
        "that one corner sits on the marked point; the shape turns and snaps edge to edge to the shape before it; "
        "Undo; Hint; Retry (clears the mat); Reset (clears the mat and the counter); Back and Next in the same places "
        "on every card. A gap that is left glows soft amber, and a shape that lies over another shows its overlap "
        "glowing soft amber. Read-outs: a counter shapes at the point (for example 3), a status line that says gap "
        "left, no gap, or overlap, a note that tells whether the gap left is big enough for one more of the shape in "
        "hand, and a card number out of 7.",
        ["Which regular shape did you meet in the video, a shape with all its sides "
         "equal? Take the square from the shelf and put one corner on the point. Then press Next.",
         "Fit triangles, squares and hexagons round the point and count how many fit; fit "
         "pentagons and see the gap that is too small; fit octagons, and then try a square in the gap (practice "
         "values for the square).",
         "Answer the book's questions about five squares and about regular hexagons, using the "
         "mat to check your answer."],
        ["Card 1: fit equilateral triangles round the point, edge to edge, until the space is full. How many "
         "fit? Answer: 6 triangles fit, with no gap and no overlap.",
         "Card 2: fit squares round the point. How many fit? Answer: 4 squares fit, with no gap and no "
         "overlap, because 4 right angle corners fill the space.",
         "Card 3: fit regular hexagons round the point. How many fit? Answer: 3 hexagons fit, with no gap "
         "and no overlap.",
         "Card 4: fit regular pentagons round the point. How many fit, and can one more go in the gap? "
         "Answer: 3 pentagons fit and a gap is left. The gap is too small for a 4th pentagon, which would overlap, so "
         "regular pentagons do not tessellate.",
         "Card 5 (practice values for the square): fit regular octagons round the point, then try a square "
         "in the gap. Answer: 2 octagons fit side by side and the gap is too small for a 3rd octagon, which would "
         "overlap. A square fits the gap exactly, so 2 octagons and 1 square fill the point.",
         "Challenge: 'Can five squares fit together around a point without any gaps or overlaps? Why or why "
         "not?' Try it on the mat. Answer: no. 4 squares already fill the space round the point, so a fifth square "
         "would overlap the first one.",
         "Challenge: 'Can regular hexagons (6-sided shapes with equal sides) fit together around a point "
         "without any gaps or overlaps? Try and see. How many fit together at a point?' Answer: yes. 3 regular "
         "hexagons fit together at a point with no gap and no overlap."],
        ["When the corners fill the space, the glow turns soft green and the status line says: No gap, no overlap. 6 "
         "triangles fit.",
         "When the space is not full, the gap glows soft amber and the note says how it compares with one more shape, "
         "for example: The gap is too small for another pentagon.",
         "When a shape would lie over another, the part that overlaps glows soft amber and the note says: A fifth "
         "square would overlap the first: 4 squares fill the space.",
         "A shape dropped far from the point slides back with a clue: Put one corner of the shape on the marked "
         "point.",
         "A small gap is never accepted as fitting: the tool says: A gap is left, so this shape does not tessellate "
         "by itself. It never shows a red cross."],
        "Triangles, squares, hexagons, pentagons and octagons have each been fitted round the point and counted, the "
        "gap that is too small has been seen for pentagons and octagons, and the two questions of your maths book "
        "are answered.",
        ["shapeInHand", "placedShapes", "shapesAtPoint", "gapStatus", "overlapStatus", "squareInGap", "cardIndex"],
        ["M_ALL_REGULAR_TILE", "M_NEARLY_FITS"],
        ["Which shape are you fitting, and where is its corner: is it on the marked point?",
         "Put the shapes next to each other, edge to edge, all with a corner on the point. Look at the glow after "
         "each shape: is there a gap, an overlap, or neither?",
         "Add shapes one at a time and watch the counter. Stop when the space is full, or when the next shape would "
         "overlap.",
         "The tool places the first two shapes for you, edge to edge round the point. Keep adding the same shape and "
         "read the status line after each one."]),

    # ============================== Tool 4: Pattern Tiler ==================================================
    "pattern_tiler": T(
        "tool_pattern_tiler", "Pattern Tiler", "manipulative",
        "Continue a pattern made of two shapes and list the shapes that meet at a point. Placing the tiles is the "
        "pattern, and the meeting-point list makes the question whether the same set of shapes meets at every point "
        "something that can be seen.",
        "A floor of dots on the craft table, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. A board with a dot grid is the largest thing on screen: a triangle dot grid for hexagons and "
        "triangles, and a square dot grid for squares, octagons and tilted squares. On a shelf at the left sit "
        "cutouts of a regular hexagon, an equilateral triangle, a regular octagon, a square, and the tilted square "
        "and the triangle with two equal sides that your maths book uses in its last pattern. Four or five marked "
        "points sit on the board when a card asks about them. An instruction strip at the top shows one sentence in "
        "large type, with progress dots under it. Controls: drag a tile, turn it with the Turn button, and it snaps "
        "to the dots and to the tile next to it; tap a marked point to open the checker list; a colour tool with "
        "purple, yellow, green, blue and orange; Undo; Hint; Retry (clears the last tiles placed); Reset (clears the "
        "board); Back and Next in the same places on every card. Read-outs: the checker list for a tapped point, "
        "written as a count for each shape, for example 2 octagons, 1 square; a line that says same set or different "
        "set when two points are compared; and a card number out of 6.",
        ["Look at the border of squares and triangles from the video, where the two "
         "shapes take turns. Tap one join and read the list of shapes that meet there, then press Next.",
         "Continue a border of squares and triangles (practice values), fill hexagons and "
         "triangles round a point, read the list at two points and compare them, then look at a border where the "
         "shapes do not take turns.",
         "Answer the book's questions about the pattern of octagons and squares, and about the "
         "pattern of hexagons and triangles."],
        ["Card 1 (practice values): a border starts with 4 tiles: square, triangle, square, triangle. Place "
         "4 more tiles to make a border of 8 tiles. How many squares and how many triangles are there? Answer: the "
         "tiles go square, triangle, square, triangle, square, triangle, square, triangle: 4 squares and 4 "
         "triangles, and 4 + 4 = 8.",
         "Card 2: on the triangle dot grid, place hexagons and triangles round one point until the space is "
         "full. Answer: 2 hexagons and 2 triangles fill the point with no gap and no overlap, in the order hexagon, "
         "triangle, hexagon, triangle.",
         "Card 3: tap two points of your pattern and read the checker lists. Are the same shapes meeting at "
         "both? Answer: at both points 2 hexagons and 2 triangles meet, so the same set of shapes meets at both "
         "points.",
         "Card 4 (practice values): the tool shows a border that goes square, triangle, triangle, square, "
         "triangle, triangle, and so on. Tap three joins and compare the lists. Answer: one join has a square and a "
         "triangle, the next has two triangles, and the next has a triangle and a square, so the same set does not "
         "meet at every join, because the shapes do not take turns.",
         "Challenge: 'Look at the pattern given below. What shapes are coming together at the marked "
         "points? Are the same set of shapes coming together at these points? Continue the pattern and colour it "
         "appropriately.' The board shows 4 rows of 4 regular octagons with a small square between each group of "
         "four. Answer: 2 octagons and 1 square come together at each marked point, and yes, it is the same set "
         "every time. Continue with octagons edge to edge and a small square wherever four octagons meet. Your "
         "colours may differ.",
         "Challenge: 'Here is a tessellating pattern with more than one shape. What shapes have been used "
         "in this pattern?' The board shows a pattern of hexagons and small triangles. Answer: regular hexagons and "
         "equilateral triangles."],
        ["A tile that snaps to the dots and to its neighbour slides into place with a soft click, and the checker "
         "list for its corners updates.",
         "Tapping a point opens the checker list and says what meets there, for example: At this point 2 octagons and "
         "1 square meet.",
         "When two points are compared the tool says either: Same set, 2 octagons and 1 square at both points, or: "
         "Different sets. Look again at the shapes that meet at each point.",
         "A point where the tiles leave a gap glows soft amber with the note: A gap is left here. Which shape would "
         "fill it? A small gap is not accepted as fitting.",
         "A tile put in the wrong place slides back with a clue, for example: Put the square where four octagons "
         "meet. The tool never shows a red cross."],
        "The border is continued, hexagons and triangles are placed round a point, two points are compared, the "
        "border that does not take turns has been checked, and the two questions of your maths book are answered.",
        ["placedTiles", "tileInHand", "markedPoints", "checkerList", "colourChoice", "sameSetResult", "cardIndex"],
        ["M_SAME_SET", "M_NEARLY_FITS"],
        ["Which point are you looking at? Name every shape that has a corner at that point.",
         "Count each kind of shape at the point, then do the same at another point and compare the two lists.",
         "At the first marked point count the shapes that meet: tap the point and read the checker. Then tap the "
         "second point and look at whether the list is the same.",
         "The tool shows the list at the first point: 2 octagons and 1 square. Now tap the next point and compare "
         "the lists yourself."]),
}
