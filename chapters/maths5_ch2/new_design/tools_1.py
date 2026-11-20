# -*- coding: utf-8 -*-
"""Tool specs for T1, T2 and T3 of Class 5 Chapter 2 (Fractions): Chocolate Compare (the free try of the intro, right
after the hook), Grid Shader and Fraction Kit. Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One
activity at a time, one instruction at a time, large controls, Back and Next in the same place, visible progress,
Hint, Retry and Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "chocolate_compare": T(
        "tool_chocolate_compare", "Chocolate Compare", "manipulative",
        "Find out by marking and counting blocks that a fraction is a part of its own whole: 1/3 of the big chocolate "
        "can hold more blocks than 1/2 of the small one, while on two bars of the same size 1/2 holds more than 1/3. "
        "This is the free first try of the chapter, so it asks and shows; the video that follows names the rule.",
        "The dining table in Raman's kitchen, drawn as a warm 3D isometric scene with soft shadows and gentle animation. "
        "A wooden board holds two chocolate bars side by side, and they are the largest things on screen. The small bar "
        "has 4 equal blocks, 2 rows of 2, and the big bar has 9 equal blocks, 3 rows of 3. Every block is the same size, "
        "as in your maths book. Above the small bar sits a half frame card with the caption Identify 1/2 of the "
        "chocolate, and above the big bar a third frame card with the caption Identify 1/3 of the chocolate. An "
        "instruction strip at the top shows one sentence in large type, with progress dots under it. Below the board "
        "is a compare tray with two empty lanes. Controls: tap a block to mark it orange and tap it again to unmark it; "
        "drag marked blocks into the compare tray, where they line up side by side; a Same whole switch that replaces "
        "the pair with two equal practice bars of 6 blocks each (practice values); two bins, Fair to compare and Not "
        "fair yet, for three picture cards; a row of explanation cards that click into an answer strip; Check, Hint, "
        "Retry (clears the marks of this step), Reset (returns the two bars), Back and Next in the same places on "
        "every card. Read-outs: a block counter for each bar (for example marked 2 of 4), the two piles in the compare "
        "tray with their block counts, and a card number out of 7.",
        ["Look at Tamanna's two chocolates from the story, the small bar and the big "
         "bar on the wooden board. Tamanna says that 1/3 of one is bigger than 1/2 of the other. Tap the bar you think "
         "is the bigger whole, then press Next.",
         "Mark 1/2 of the small bar and 1/3 of the big bar by tapping blocks, drag the marked "
         "blocks into the compare tray and read the counts, press Same whole to get two bars of one size, mark 1/2 "
         "and 1/3 of them and compare again, then sort three picture cards.",
         "Answer Tamanna's own question from the story, Is that correct? Explain why this is so, "
         "and the question When can we say that 1/2 of something is greater than 1/3 of something? Build each answer "
         "from the explanation cards."],
        ["Card 1: tap blocks to mark 1/2 of the small bar, then 1/3 of the big bar. How many blocks did you "
         "mark in each bar? Answer: 2 blocks in the small bar, because 4 ÷ 2 = 2, and 3 blocks in the big bar, because "
         "9 ÷ 3 = 3.",
         "Card 2: drag the marked blocks into the compare tray and read the counts. Which pile is bigger? "
         "Answer: the 3 blocks from the big bar are more than the 2 blocks from the small bar, so here 1/3 of the big "
         "bar is bigger than 1/2 of the small bar.",
         "Card 3 (practice values): press Same whole. Two bars of the same size appear, each with 6 blocks. "
         "Mark 1/2 of one bar and 1/3 of the other. Answer: 3 blocks, because 6 ÷ 2 = 3, and 2 blocks, because "
         "6 ÷ 3 = 2.",
         "Card 4: drag the new marked blocks into the compare tray. Which pile is bigger now? Answer: 1/2 "
         "(3 blocks) is more than 1/3 (2 blocks). On two bars of the same size the answer is the other way round.",
         "Card 5 (practice values): sort the three picture cards into Fair to compare and Not fair yet. Card "
         "A: 1/2 of a small bar and 1/3 of a big bar. Card B: 1/2 and 1/4 of two bars of the same size. Card C: 1/2 "
         "and 1/3 of two chikki slabs of the same size. Answer: card A goes to Not fair yet, because the wholes are "
         "different sizes. Cards B and C go to Fair to compare, because the wholes are the same size.",
         "Challenge: 'Tamanna is a student of Grade 5. She has two chocolates of different sizes. She says "
         "that 1/3 of one of her chocolates is bigger than 1/2 of the other chocolate. Is that correct? Explain why "
         "this is so.' Check with the bars, then build your explanation from the cards. Answer: yes, she can be "
         "correct. 1/3 of the big bar is 3 blocks and 1/2 of the small bar is 2 blocks, because the two chocolates "
         "are different sizes. Cards that fit: The two bars are different sizes; Every block is the same size; 3 "
         "blocks are more than 2 blocks. Your explanation may use your own words.",
         "Challenge: 'When can we say that 1/2 of something is greater than 1/3 of something?' Use the Same "
         "whole switch to help you, then build your answer from the cards. Answer: when both are parts of two wholes "
         "of the same size, 1/2 is greater than 1/3. If the wholes are different sizes, we cannot say. Next stop: "
         "the rule for comparing fractions."],
        ["A tap on a block marks it orange and the counter for that bar shows how many blocks are marked. A wrong "
         "number of marks shows a soft amber note, for example: Each part must be equal: 4 blocks make the whole, so "
         "1/2 is 2 blocks. For the big bar the note says: 9 blocks make the whole, so 1/3 is 3 blocks.",
         "In the compare tray the two piles line up side by side and the tool says which pile is bigger in blocks, "
         "for example: 3 blocks are more than 2 blocks.",
         "After Same whole the tool says: Now the two bars are the same size. Mark 1/2 of one and 1/3 of the other.",
         "A picture card dropped in the wrong bin slides back with a clue, for example: Look at the two wholes. Are "
         "they the same size? A card in the right bin locks in with a soft chime.",
         "An explanation card that fits clicks into the answer strip. A card that does not fit slides back with a "
         "clue such as: Does this card talk about the size of the whole? The tool never shows the full explanation."],
        "Both pairs of bars are marked correctly, the three picture cards are sorted, and the student has built an "
        "explanation for each of Tamanna's two questions from the cards.",
        ["markedBlocksSmall", "markedBlocksBig", "sameWholeOn", "comparePiles", "cardBins", "explanationCards",
         "challengeIndex"],
        ["M_DIFF_WHOLE", "M_UNEQUAL_PARTS"],
        ["What is the whole in Tamanna's story? Look at the two chocolate bars: are they the same size?",
         "Count how many equal blocks make each whole. Then ask how many blocks are 1/2 of the small bar and how many "
         "are 1/3 of the big bar.",
         "Share the 4 blocks of the small bar into 2 equal groups and the 9 blocks of the big bar into 3 equal "
         "groups. One group is one part.",
         "Mark 2 blocks of the small bar, because 4 ÷ 2 = 2, and 3 blocks of the big bar, because 9 ÷ 3 = 3. The tray "
         "shows 3 blocks and 2 blocks."]),

    "grid_shader": T(
        "tool_grid_shader", "Grid Shader", "manipulative",
        "Find 1/8, 1/6 and 1/12 of a 48-square grid by sharing the squares into equal groups, and see that one area "
        "can be named by different fractions: 1/3 shows up as 2 parts of 1/6 and as 4 parts of 1/12.",
        "Three coloured mats on a kitchen table, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. Grid A, Grid B and Grid C each have 8 columns and 6 rows of equal squares, 48 squares in all, as "
        "in your maths book. The grid being worked on is the largest thing on screen, in the middle; the other two "
        "sit as small mats at the side, and a row of tabs A, B and C switches between them. An instruction strip at "
        "the top shows the fraction asked for in large type, for example 1/8 of Grid A in red, with progress dots "
        "under it. A tray of three shading pens, red, blue and yellow, sits on the right and the pen for the grid is "
        "pre-selected. Controls: tap a square or drag across squares to shade it, tap a shaded square to clear it; a "
        "Show equal parts toggle that outlines n equal groups of squares, where n is the bottom number of the "
        "fraction asked; a Mark 1/3 selector that gives an orange marker and an outline tool; Check, Hint, Undo, "
        "Retry (clears the grid being worked), Reset (clears all three grids), Back and Next in the same places on "
        "every card. Read-outs: squares in the whole (48), squares in one equal part when the parts are shown (for "
        "example 48 ÷ 8 = 6), a counter squares shaded (for example 6 of 48), and, after Mark 1/3, the squares marked "
        "and the equal parts they join.",
        ["Look at a small practice grid of 12 squares with 1/3 shaded (practice values). "
         "Count all the squares and the shaded squares, and say how many equal groups the grid is shared into.",
         "With Show equal parts on, shade one equal part of each grid, 1/8 of A, 1/6 of B and "
         "1/12 of C, and read how many squares are in one part each time. Then use Mark 1/3 to find how many squares "
         "1/3 is and which parts join to make it.",
         "The book's own items with the parts hidden. Shade 1/8 of Grid A in red, 1/6 of Grid B in "
         "blue and 1/12 of Grid C in yellow. Then answer: Do you see 1/3 in any of the grids? Mark it."],
        ["Card 1: Grid A, parts shown: the grid is cut into 8 equal parts. How many squares are in one part? "
         "Shade one part red. Answer: 6 squares, because 48 ÷ 8 = 6.",
         "Card 2: Grid B, parts shown: the grid is cut into 6 equal parts. Shade one part blue. Answer: 8 "
         "squares, because 48 ÷ 6 = 8.",
         "Card 3: Grid C, parts shown: the grid is cut into 12 equal parts. Shade one part yellow. Answer: 4 "
         "squares, because 48 ÷ 12 = 4.",
         "Card 4: tap Mark 1/3. How many squares make 1/3 of a grid of 48 squares? Answer: 16 squares, "
         "because 48 ÷ 3 = 16.",
         "Card 5: in Grid B, with the parts shown, mark parts until you have exactly 16 squares. How many "
         "parts of 1/6 did you mark? Answer: 2 parts, because 2 × 8 = 16, so 2/6 = 1/3.",
         "Challenge: 'Shade 1/8 of Grid A in red. Shade 1/6 of Grid B in blue. Shade 1/12 of Grid C in "
         "yellow.' The parts are hidden. Answer: 6 squares red in Grid A, 8 squares blue in Grid B and 4 squares "
         "yellow in Grid C, each in equal groups. Your squares may be in different places.",
         "Challenge: 'Do you see 1/3 in any of the grids? Mark it.' Answer: yes, in Grid B, where 2 parts of "
         "1/6 make 16 squares, and in Grid C, where 4 parts of 1/12 make 16 squares. In Grid A the parts of 1/8 have "
         "6 squares each, and joining them gives 6, 12 or 18 squares, never 16."],
        ["Each shaded square lights up in the pen colour and the counter shows how many squares are shaded. Check "
         "compares the count with the fraction and says what it found, for example: You shaded 7 squares. 1/8 of 48 "
         "is 6.",
         "Show equal parts outlines the equal groups and says how many squares are in one part, for example: 48 ÷ 8 = "
         "6 squares in one part. A group with a different number of squares blinks softly in amber.",
         "Mark 1/3 outlines the marked squares in orange and says how many squares there are and which equal parts "
         "they join, for example: 2 parts of 1/6 are 16 squares.",
         "In Grid A the tool shows the parts of 6 squares and says: Parts of 1/8 have 6 squares. Joining them gives 6, "
         "12, 18 squares, never 16, so 1/3 is not made from the parts of Grid A.",
         "A wrong count shows a soft amber note and never a red cross; the tool names the number of squares it "
         "expected only after the second try."],
        "Grids A, B and C are shaded correctly, first with the parts shown and then with the parts hidden, 1/3 is "
        "marked in Grid B and in Grid C, and the student has seen why the parts of Grid A do not make 1/3.",
        ["gridShading", "penColor", "partsShown", "squaresShaded", "marked13", "activeGrid", "challengeIndex"],
        ["M_UNEQUAL_PARTS"],
        ["How many equal parts is the grid shared into? Look at the bottom number of the fraction.",
         "How many squares are in the whole grid? Count the columns and the rows, then multiply.",
         "Share the 48 squares into that many equal groups. How many squares are in one group?",
         "For 1/8 of Grid A: 48 ÷ 8 = 6. The tool shades the first part of 6 squares so you can see it."]),

    "fraction_kit": T(
        "tool_fraction_kit", "Fraction Kit", "manipulative",
        "Build wholes from kit pieces of one size and of different sizes, fit small pieces inside a bigger piece, and "
        "read off the equivalent fraction that each fit shows.",
        "A wooden kit tray on the kitchen table, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. In the middle is a large whole-circle outline on a plate; pieces snap into it, and the circle is "
        "the largest thing on screen. The round fraction pieces look like the pie in your maths book, where a piece "
        "of 1/2 and two pieces of 1/4 make the whole; each piece is labelled with its fraction in large type and "
        "coloured by its size. The kit tray along the bottom holds the twelve round discs of the Fractions Kit sheet at "
        "the end of the maths book: the whole, and the discs cut into 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 and 12 equal "
        "pieces (1/2 to 1/12). Every size has its own number of pieces, as on the sheet, and no other sizes appear in "
        "the tray. To the right is a fit inside shelf: a big piece lies on the shelf "
        "and the student drops smaller pieces on top of it. Below the circle is a My findings sheet that lists the "
        "lines the student adds. An instruction strip at the top shows one sentence in large type, with progress dots "
        "under it. Controls: drag a piece from the tray into the circle or onto the shelf piece; tap a piece to put "
        "it back; a mode switch between Fill the circle and Fit inside; an Add to my findings button; Check, Hint, "
        "Retry (empties the circle), Reset (clears the circle, the shelf and the sheet), Back and Next in the same "
        "places on every card. Read-outs: a running total under the circle (for example These pieces make 11/12), a "
        "Whole! banner when the pieces fill the circle exactly, on the shelf the line n pieces of 1/d fill 1/D, so 1/D "
        "= n/d, and a counter of the pieces used.",
        ["The circle already holds one piece of 1/2, as in the picture in your maths "
         "book. Pick pieces from the tray to fill the empty half.",
         "Fill the circle with pieces of one size, then with two or three different sizes, "
         "then switch to Fit inside and drop smaller pieces on a bigger piece to see how many fit and what the tool "
         "writes.",
         "The book's own questions with the kit: how many pieces of 1/5 make a whole, what else is "
         "equivalent to 1/2, the equivalents of 1/3, 1/4, 1/5 and 1/6, how many small pieces make a bigger piece, and "
         "the wholes made from chosen pieces, with your own findings on the sheet."],
        ["Card 1 (practice values): fill the circle with pieces of one size, pieces of 1/6. How many do you "
         "need? Answer: 6 pieces of 1/6, because 6/6 = 1.",
         "Card 2 (practice values): put one piece of 1/2 in the circle and fill the rest with pieces of 1/8. "
         "How many pieces of 1/8? Answer: 4 pieces of 1/8, because 1/2 = 4/8 and 4/8 + 4/8 = 8/8 = 1.",
         "Card 3 (practice values): make a whole with one piece each of 1/2, 1/3 and 1/6. Answer: 1/2 + 1/3 + "
         "1/6 = 3/6 + 2/6 + 1/6 = 6/6 = 1.",
         "Card 4: switch to Fit inside. Put the piece of 1/2 on the shelf and drop pieces of 1/4 on it, then "
         "pieces of 1/6. How many of each fit? Answer: 2 pieces of 1/4 fill 1/2 and 3 pieces of 1/6 fill 1/2, so 1/2 "
         "= 2/4 and 1/2 = 3/6.",
         "Card 5 (practice values): put 1/2, 1/4 and one piece of 1/8 in the circle and read the total. Which "
         "piece fills the gap? Answer: the total is 7/8, because 4/8 + 2/8 + 1/8 = 7/8. One more piece of 1/8 fills "
         "the whole.",
         "Challenge: 'Do you remember how to make a whole with pieces of the same size? How many pieces of "
         "1/5 will you need to make a whole?' Then: 'What else is equivalent to 1/2? 1/2 = 2/4 = ___ = ___ = ___' "
         "Then, from the Let Us Do box: 'In groups of 3 or 4, find different ways of making a whole with different fraction "
         "pieces from your kit. Write the equivalent fractions for the following that you may find in the process. "
         "(a) 1/3 = ___ = ___ = ___ (b) 1/4 = ___ = ___ = ___ (c) 1/5 = ___ = ___ = ___ (d) 1/6 = ___ = ___ = ___' "
         "Answers: 5 pieces of 1/5; 1/2 = 2/4 = 3/6 = 4/8 = 6/12; sample for the equivalents: (a) 1/3 = 2/6 = 3/9 = "
         "4/12 (b) 1/4 = 2/8 = 3/12 = 4/16 (c) 1/5 = 2/10 = 3/15 = 4/20 (d) 1/6 = 2/12 = 3/18 = 4/24. The kit gives "
         "some of these and the rest come from cutting every part into more equal parts. Your answers may differ.",
         "Challenge: from the Let Us Do box: 'Find the following using your kit. You can also shade and check by "
         "shading. A. How many pieces of 1/6 make 1/3? B. How many pieces of 1/8 make (a) 1/4? (b) 1/2? C. How many "
         "pieces of 1/12 make (a) 1/2 (b) 1/3 (c) 1/4 (d) 1/6?' Then, in the same box: 'Do as instructed using your "
         "fraction kit. Make a whole using only 1/6 and 1/12 pieces. Make a whole using 1/12, 1/4, and 1/2 pieces. "
         "Make a whole using any five pieces of the same size. Make a whole using any seven pieces. Play in a group "
         "with this kit and find other interesting combinations to make a whole. Write or draw your findings.' "
         "Answers: A. 2 pieces. B. (a) 2 pieces (b) 4 pieces. C. (a) 6 pieces (b) 4 pieces (c) 3 pieces (d) 2 "
         "pieces. The make-a-whole tasks, sample: 3 pieces of 1/6 and 6 pieces of 1/12; one piece each of 1/2 and 1/4 and 3 "
         "pieces of 1/12; five pieces of 1/5; two pieces of 1/4, one piece of 1/6 and four pieces of 1/12, which is 7 "
         "pieces. Each makes 1 whole. Add your own findings to My findings. Your answers may differ."],
        ["The running total updates at once with every piece, for example: These pieces make 11/12. One more piece of "
         "1/12 fills the whole.",
         "A piece that is bigger than the gap springs back with: This piece is bigger than the gap. How much of the "
         "circle is left?",
         "On the shelf, when the smaller pieces cover the big piece exactly the tool writes: 2 pieces of 1/4 fill 1/2, "
         "so 1/2 = 2/4. If they do not cover it, the part still open glows in amber.",
         "When the circle is full the Whole! banner appears and the tool reads the pieces as one sum, for example 1/2 "
         "+ 1/4 + 1/4 = 2/4 + 1/4 + 1/4 = 4/4 = 1.",
         "Open questions, the equivalents and the findings, are never marked wrong: the sheet says Your answer may "
         "differ and offers Next."],
        "The circle has been filled with pieces of one size and with different sizes, small pieces have been fitted "
        "inside a bigger piece, the book's questions have been answered with the kit, and at least one finding is "
        "written on My findings.",
        ["circlePieces", "shelfBig", "shelfSmall", "runningTotal", "findingsSheet", "mode", "challengeIndex"],
        ["M_UNEQUAL_PARTS", "M_EQUIV_ADD"],
        ["What is the question asking: fill the whole circle, or fill one bigger piece? Look at how much of the circle "
         "is empty.",
         "Which is the biggest piece that still fits in the gap? Start with it, then fill what is left.",
         "Say how much of the circle is left, then pick pieces that fill exactly that much. If 1/12 is left, one piece "
         "of 1/12 fills it.",
         "The tool puts the next piece in the gap for you. For example, a circle that shows 11/12 gets its last piece "
         "of 1/12 and the banner says Whole!"]),
}
