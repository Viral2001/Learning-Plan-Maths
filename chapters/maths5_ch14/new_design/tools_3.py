# -*- coding: utf-8 -*-
"""Tool specs for T6 and T7 of Class 5 Chapter 14 (Maps and Locations): Ant Path (distance and direction on the ant
grid, and the shortest route) and Zoo Grid Locator (a position on the zoo grid as column and row). Specs only; the tool
pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds
are labelled practice values. One activity at a time, one instruction at a time, large controls, Back and Next in the
same place, visible progress, Hint, Retry and Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "ant_path": T(
        "tool_ant_path", "Ant Path", "manipulative",
        "Build a path on a grid one square at a time and read it as legs, each with a distance in cm and a "
        "direction, then compare routes to the same food by their lengths: the shortest route goes only towards the "
        "food.",
        "The ant grid board on the trip desk, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. A friendly wooden desk holds one large board: a grid of 11 by 11 squares, each square 1 cm, as in "
        "your maths book. The grid is the largest thing on screen. A compass card sits in the top left corner of the "
        "grid with N at the top, E in red on the right, S at the bottom and W on the left, and the label 1 cm with a "
        "small double arrow sits in the top right corner. A small ant stands on a grid point near the middle. In the "
        "book challenges the four foods sit where your maths book puts them: a plate of laddoos 2 squares to the "
        "right of the ant, a pile of sugar 3 squares above it, a slice of bread 3 squares to the left and 2 squares "
        "below it, and an apple 3 squares to the right and 3 squares below it. In the practice cards the foods are "
        "replaced by a leaf, a seed and a berry that the tool places (practice values). In the book challenges the "
        "red dashed route drawn in your maths book is shown as a faint guide to follow. An instruction strip at the "
        "top shows one sentence in large type, with progress dots under it. Controls: four large arrow buttons N, E, "
        "S and W on the right of the board, and each one moves the ant 1 cm along the grid line and draws a red "
        "dashed trail with small arrowheads behind it; Undo takes back the last cm; Clear trail puts the ant back on "
        "its start and removes the trail; Save route keeps the trail as a named route for comparing; Compare routes "
        "shows two saved routes side by side; a legs card with a number box and a direction chip (north, east, south "
        "or west) for each leg, with Add leg and Remove leg, where the answer is written; Check, Hint, Retry (clears "
        "the trail and the legs card of this step), Reset (puts the ant back and empties the saved routes), Back and "
        "Next in the same places on every card. Read-outs: the legs list that the tool writes as the ant moves (for "
        "example 3 cm east, then 3 cm south), a length counter in cm (for example Length: 6 cm), the direction of "
        "the ant's last move, and, in Compare routes, the two lengths and a line such as Route B is 2 cm longer.",
        ["Look at the small practice grid from the video, with the ant and a berry. "
         "Tap E two times to move the ant 2 cm towards the east, the first leg of the way to the berry, and read "
         "the legs list.",
         "Use the arrow buttons to move the ant to the practice foods, read the legs list "
         "and the length counter each time, and save two routes to one berry to compare their lengths.",
         "The book's own questions on the grid of your maths book: how far, and in which "
         "direction, the ant crawls to the laddoos, to the sugar, to the bread and to the apple, and the other routes "
         "to the apple with the shortest one."],
        ["Card 1 (practice values): a leaf lies 4 cm to the west of the ant. Move the ant to the leaf with "
         "the arrow buttons. What does the legs list say, and how long is the path? Answer: 4 cm west, and the "
         "length is 4 cm, because 4 squares of 1 cm each are 4 cm.",
         "Card 2 (practice values): a berry lies 2 cm to the east and 4 cm to the north of the ant. Move the "
         "ant to the berry and read the legs list and the length. Answer: 2 cm east, then 4 cm north, and the length "
         "is 2 + 4 = 6 cm.",
         "Card 3 (practice values): a berry lies 4 cm to the east and 3 cm to the north. Build Route A, 4 cm "
         "east then 3 cm north, and save it. Build Route B, 5 cm east, 3 cm north, then 1 cm west, and save it. Press "
         "Compare routes. Answer: Route A is 4 + 3 = 7 cm and Route B is 5 + 3 + 1 = 9 cm, so Route A is 2 cm shorter. "
         "Route B has a step 1 cm the wrong way.",
         "Card 4 (practice values): the berry is still 4 cm east and 3 cm north. Build a route with more "
         "turns: 2 cm east, 1 cm north, 2 cm east, then 2 cm north. Is it shorter than Route A, longer, or the same? "
         "Answer: the same. Its length is 2 + 1 + 2 + 2 = 7 cm. It has three turns but it never goes the wrong way, "
         "so it is a shortest route too.",
         "Challenge: 'To get to the laddoos, the ant has to crawl how far, and towards which "
         "direction? Each square of the grid is 1 cm.' Then: 'To get to the sugar, the ant has to crawl ___ cm in the ___ direction.' Then: 'To get to "
         "the bread, the ant has to crawl ___ cm in the ___ direction; then ___ cm in the ___ direction.' Move the "
         "ant with the arrow buttons, then fill the legs card. Answers: the laddoos: 2 cm towards the east. The "
         "sugar: 3 cm in the north direction. The bread: 3 cm in the west direction; then 2 cm in the south "
         "direction (5 cm in all).",
         "Challenge: 'To get to the apple, the ant needs to crawl ___ cm towards ___, and then ___ cm "
         "towards ___, and finally ___ cm towards ___.' Then: 'Identify other routes to reach the point where apple "
         "is located. Which one is the shortest?' Answers: the apple: 5 cm towards south, 3 cm towards east, and "
         "finally 2 cm towards north, which is 5 + 3 + 2 = 10 cm in all. Sample answer for the other routes: 3 cm east then "
         "3 cm south (6 cm); 3 cm south then 3 cm east (6 cm); 1 cm south, 3 cm east, then 2 cm south (6 cm). The "
         "shortest routes are 6 cm, and the route in your maths book is 10 cm. Your routes may differ."],
        ["Every tap moves the ant 1 cm and adds to the trail. The legs list joins moves in the same direction into one "
         "leg, for example: 3 cm east, then 3 cm south.",
         "The length counter adds the cm of all the legs, for example 3 + 3 = 6, and shows it as Length: 6 cm.",
         "If the ant is not on the food yet, a soft amber note says how far is left and which way, for example: The "
         "sugar is 1 cm more towards the north.",
         "A wrong number or direction on the legs card shows a soft amber note that points at the first thing to look "
         "at, for example: Count the squares on this leg again. Up is north. The tool shows the expected leg only "
         "after the second try.",
         "In Compare routes the tool writes the two lengths and why they differ, for example: Route A is 7 cm and "
         "Route B is 9 cm. Route B is 2 cm longer because it has a step 1 cm towards the west, away from the berry.",
         "The other routes to the apple are open answers and are never marked wrong: the tool checks that each route "
         "ends on the apple, reads its length, says whether it is a shortest route, and says: Your answer may "
         "differ."],
        "The student has moved the ant to the practice foods and read their legs and lengths, compared two routes to "
        "one berry, written the legs for the laddoos, the sugar, the bread and the apple, and named the shortest "
        "routes to the apple.",
        ["antPosition", "trail", "legsList", "lengthCm", "savedRoutes", "foodTarget", "challengeIndex"],
        ["M_FEW_TURNS"],
        ["Which food is the ant going to? Look at where it is on the grid: above, below, to the left or to the right "
         "of the ant, and about how many squares away.",
         "Count the squares along one straight grid line. Each square is 1 cm. When the route has to turn, a new leg "
         "starts. Say the direction of each leg with the compass.",
         "For a berry 2 cm east and 4 cm north: tap E 2 times, then N 4 times. The legs list says 2 cm east, then 4 cm "
         "north, and the length is 2 + 4 = 6 cm.",
         "The tool moves the ant 2 cm to the east for you and writes the first leg on the legs card. Now tap N to "
         "start the second leg."]),

    "zoo_grid": T(
        "tool_zoo_grid", "Zoo Grid Locator", "manipulative",
        "Read the position of a place on a grid as two numbers, the column first and the row second, by walking a "
        "marker east from 0 and then north, and see that swapping the two numbers gives a different place.",
        "The zoo grid board on the trip desk, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. A friendly wooden desk holds one large board: the zoo map of your maths book on a grid of 12 "
        "columns and 12 rows, with the lines numbered 1 to 12 along the bottom and up the left side, 0 at the bottom "
        "left corner and the ZOO sign at the bottom. The map is the largest thing on screen. The animals stand at "
        "their places as in your maths book: the parrot, flamingo, toucan, giraffe, zebra, big cat, deer, tiger, "
        "snake, elephant, lion, monkey, panda, tortoise and crocodile, and the hippo in the pond. A compass card sits "
        "beside the map with N at the top, E in red on the right, S at the bottom and W on the left. A round marker "
        "starts at 0. An instruction strip at the top shows one sentence in large type, with progress dots under it. "
        "Controls: an East step button and a North step button, and each one moves the marker 1 step along the "
        "bottom line or up a column line, and if North is tapped first the tool says: First move horizontally from 0, "
        "then vertically; tap an animal to read its position; two number boxes labelled column and row to type a "
        "pair, with a Go button that moves the marker there; a Swap button that swaps the two numbers of the pair and "
        "moves the marker; six dot colours (red, green, blue, orange, black and pink) with a Place dot button and a "
        "Remove dot button; Check, Hint, Retry (returns the marker to 0), Reset (clears the dots and returns the "
        "marker), Back and Next in the same places on every card. Read-outs: the pair (column,row) with live "
        "numbers, the steps counted so far (for example East 8, North 9), and a What is here line that names the "
        "animal at the marker or says no animal here. In the dot challenge the What is here line is hidden and the "
        "read-out shows only the pair.",
        ["Look at the giraffe walk from the video, east first and then north. Start at "
         "0, tap East 2 times and North 1 time, and read the pair.",
         "Walk the marker to the giraffe and read the pair as it grows, tap an animal to read "
         "its position, type a pair that is not the giraffe, and use Swap to see that two numbers in the other order "
         "are another place.",
         "The book's own questions on the zoo map: the way to the panda and to the tortoise, what "
         "is at (1,4), the animals at six positions, the positions of six animals, and six coloured dots."],
        ["Card 1 (practice values): walk the marker to the giraffe. Tap East 8 times, then North 9 times, "
         "and read the pair as it grows. Answer: after 8 steps east the pair is (8,0), and after 9 steps north it is "
         "(8,9). The giraffe is at (8,9).",
         "Card 2 (practice values): tap the parrot and read its position. Answer: (1,11), that is 1 step "
         "east and 11 steps north.",
         "Card 3 (practice values): type (9,8) in the number boxes and press Go. Is the giraffe there? "
         "Answer: no. The tool says no animal here. The giraffe is at (8,9). The first number is the column and the "
         "second number is the row.",
         "Card 4 (practice values): tap the big cat and read its position, then press Swap. Answer: the big "
         "cat is at (8,7). The swapped pair is (7,8), 7 steps east and 8 steps north, a place on the path with no "
         "animal. A pair with its numbers swapped is a different place.",
         "Challenge: 'Start from 0 on the zoo map. How do you reach the panda, and how do we write its "
         "position?' Then: 'To reach the tortoise, move ___ steps towards east and reach the ___ column. Then move "
         "___ step(s) ___ and reach the first ___.' Then: 'The location of the tortoise is (4,1). What is at (1,4)?' "
         "Then: 'Locate the animal at the following positions on the map. (a) (11,11) ___ (b) (2,6) ___ (c) (6,4) "
         "___ (d) (3,10) ___ (e) (11,3) ___ (f) (10,9) ___' Walk the marker for each one. Answers: the panda: 1 step "
         "east to the first column, then 1 step north to the first row, (1,1). The tortoise: 4 steps towards east and "
         "reach the 4th column; then 1 step north and reach the first row, (4,1). At (1,4): a snake. Q1: (a) toucan "
         "(b) tiger (c) elephant (d) flamingo (e) monkey (f) zebra.",
         "Challenge: 'Write the position of the following animals on the map. (a) Lion ___ (b) Elephant ___ "
         "(c) Tortoise ___ (d) Deer ___ (e) Panda ___ (f) Crocodile ___' Tap each animal to read its position. Then: "
         "'Place dots of different colours on the following positions. (a) (8,3) (Red) (b) (2,9) (Green) (c) (7,3) "
         "(Blue) (d) (3,8) (Orange) (e) (8,6) (Black) (f) (6,6) (Pink)' Walk the marker to each position and place "
         "the dot there. Answers: Q2: (a) lion (3,3) (b) elephant (6,4) (c) tortoise (4,1) (d) deer (10,6) (e) panda (1,1) (f) "
         "crocodile (10,1). Q3: red at (8,3), green at (2,9), blue at (7,3), orange at (3,8), black at (8,6), pink at "
         "(6,6)."],
        ["The pair (column,row) changes at once with every step: East changes the first number and North changes the "
         "second, for example: You went 1 step east and 4 steps north, so the pair is (1,4).",
         "At each stop the What is here line reads the place, for example: At (8,9) stands the giraffe, or: No animal "
         "here.",
         "A typed pair with the numbers in the wrong order moves the marker to the other place and says what is "
         "there, for example: (9,8) is 9 steps east and 8 steps north. The giraffe is at (8,9).",
         "A wrong answer on a card shows a soft amber note and never a red cross, for example: Which number is the "
         "column? Walk east first. The tool shows the expected pair only after the second try.",
         "A dot on the right meeting point locks in with a soft chime. A dot on another place slides back with a "
         "clue, for example: Move east 8 steps first, then north 3 steps. The tool does not say what is at a "
         "meeting point in the dot challenge."],
        "The student has walked the marker to the giraffe, read the position of an animal, seen that (9,8) is not the "
        "giraffe and that a swapped pair is another place, answered the panda, tortoise and (1,4) questions, named the "
        "animals at six positions, written the positions of six animals, and placed the six coloured dots.",
        ["markerPosition", "stepsEast", "stepsNorth", "typedPair", "placedDots", "swapUsed", "challengeIndex"],
        ["M_ORDER_SWAP"],
        ["Which number comes first in a position, and which way do you walk for it?",
         "Start at 0. Move east along the bottom to the column, then move north up the column line to the row.",
         "For the giraffe: 8 steps east, then 9 steps north, so the position is (8,9). The first number is the "
         "column.",
         "The tool moves the marker 8 steps east for you. Now tap North 9 times and read the pair."]),
}
