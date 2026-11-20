# -*- coding: utf-8 -*-
"""Tool spec for T7 of Class 5 Chapter 11 (Grandmother's Quilt): the Perimeter 24 Game, the book's Let Us Play with square
tiles and a die. Spec only; the tool page is built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One activity at a time, one
instruction at a time, large controls, Back and Next in the same place, visible progress, Hint, Retry and Reset always
present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "perimeter_game": T(
        "tool_perimeter_game", "Perimeter 24 Game", "manipulative",
        "Find the perimeter of a figure of square tiles by counting its outer edges, see how a tile added along one "
        "edge or in a corner changes it, and play the book's game to make the perimeter exactly 24.",
        "Grandmother's floor, drawn as a warm 3D isometric scene with soft shadows and gentle animation. Square tiles "
        "lie on a mat in a pile and the figure that the players are building is the largest thing on screen, in the "
        "middle of the mat; every tile side is 1. A big die sits at the side. Every outer edge of the figure is marked "
        "1 as in your maths book, and the marks light up as they are counted. Two player tags, Player 1 and Player 2, "
        "show whose turn it is, with an option to play against the tool instead of a friend. A banner says Make the "
        "perimeter 24. An instruction strip at the top shows one sentence in large type, with progress dots under it. "
        "Controls: a Roll button that rolls the die from 1 to 6 and sets that number of tiles ready; drag the tiles of "
        "this turn so that they touch the figure along whole edges, and a tile cannot be moved once it is placed; a "
        "Count the edges button that lights each outer edge in turn; an Undo this turn button that takes back the "
        "tiles of this turn only; a Next player button; Check, Hint, Retry (undoes this turn), Reset (clears the "
        "figure), Back and Next in the same places on every card. Read-outs: the die number, the tiles placed, the "
        "perimeter counter (for example 12), the distance to 24 (for example 12 more), and a card number out of 7.",
        ["Look at a figure of 3 tiles in a row (practice values) with its outer edges "
         "marked 1. Count the outer edges one by one and say what number you get. That number is the perimeter.",
         "Roll and place tiles in two different shapes and count the perimeters, add one tile "
         "along one edge, add one tile in a corner, and play to a perimeter of 16.",
         "Play the book's game: find the perimeter of the tiles, add tiles to the same figure "
         "without moving any tile, and take turns till the perimeter becomes 24. The one who makes the perimeter 24 "
         "wins the game."],
        ["Card 1 (practice values): the die shows 4. Place the 4 tiles in a row and count the perimeter, then "
         "place them as a square of 2 by 2 and count again. Answer: a row of 4 has 4 + 1 + 4 + 1 = 10 outer edges, "
         "and a 2 by 2 square has 8. The same number of tiles can have different perimeters.",
         "Card 2 (practice values): start with the 2 by 2 square, perimeter 8. Add 1 tile that touches the "
         "square along 1 edge. What is the perimeter now? Answer: 10, because 8 + 2 = 10. A tile along 1 edge makes the "
         "perimeter 2 more.",
         "Card 3 (practice values): start with 3 tiles placed like the letter L, perimeter 8. Add 1 tile in "
         "the corner where the two arms meet. What is the perimeter now? Answer: 8. The tile touches 2 edges, so the "
         "perimeter stays the same, and the figure becomes a 2 by 2 square.",
         "Card 4 (practice values): make a figure with a perimeter of exactly 16. Answer: any figure with 16 "
         "outer edges is right, for example a row of 7 tiles, because 7 + 1 + 7 + 1 = 16. Your figure may differ.",
         "Challenge: 'Find the perimeter of the tiles.' The figure has 4 tiles: a row of 3 and one tile below "
         "the left tile. Answer: the perimeter is 10, because the outer edges are 3 + 1 + 2 + 2 + 2 = 10.",
         "Challenge: 'Do not move the tiles. The second player can take turn and add tiles to the same tiled "
         "figure.' The die shows 1. Add 1 tile along 1 edge of the figure of 4 tiles. Answer: the figure has 5 tiles "
         "and the perimeter is 12, because 10 + 2 = 12.",
         "Challenge: 'Take turns and add tiles to the same figure till the perimeter becomes 24. The one "
         "who makes the perimeter 24 wins the game.' The die shows 6. Add 6 tiles to the figure of 5 tiles without "
         "moving any tile. Answer: the figure has 11 tiles and the perimeter is 24, so the player who rolled the 6 "
         "wins. Another game may go differently."],
        ["The perimeter counter changes each time a tile is placed, and the tool says for example: This figure has 12 "
         "outer edges, so its perimeter is 12.",
         "Count the edges lights each outer edge in turn and the counter goes up by one for each, so the student can "
         "check the total.",
         "A tile that touches the figure along 1 edge makes the tool say: This tile touches 1 edge, so the perimeter is "
         "2 more. A tile in a corner that touches 2 edges makes it say: This tile touches 2 edges, so the perimeter "
         "stays the same.",
         "A tile that does not touch the figure along a whole edge slides back softly and the tool says: Place the "
         "tile so that it touches the figure along a whole edge.",
         "When the perimeter goes past 24 the tool says: Past 24. A tile that fills a notch and touches 3 edges makes "
         "it 2 less. It never shows a red cross; the banner lights up and the player wins when the counter shows "
         "exactly 24."],
        "The student has counted the perimeter of figures of tiles by their outer edges, has seen what a tile along one "
        "edge and a tile in a corner do to the perimeter, has made a perimeter of 16, and has played the book's game "
        "to a perimeter of exactly 24.",
        ["dieNumber", "tilesPlaced", "perimeterCount", "edgesCounted", "currentPlayer", "againstTool", "challengeIndex"],
        ["M_ADD_TILE", "M_BORDER_PATCHES"],
        ["What does the perimeter of tiles count? Look at the edges on the outside of the figure.",
         "Count the outer edges one by one. An edge that two tiles share is inside and is not counted.",
         "Does the new tile touch the figure along 1 edge or along 2 edges? Along 1 edge the perimeter is 2 more, along "
         "2 edges it stays the same.",
         "To reach 24 from a perimeter of 12, you need 12 more. The tool places a tile along 1 edge so you can see the "
         "perimeter become 14."]),
}
