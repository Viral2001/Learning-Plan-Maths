# -*- coding: utf-8 -*-
"""Topics T6, T7 and T8 (module M3: Grids, Distances and Positions). Distance and Direction on a Grid (the ant),
Locating Places on a Grid (the zoo) and the Chapter Revision summary.
Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of its
topic's DOER, in the book's order. The ant grid is 11 by 11 squares of 1 cm and the zoo grid is 12 by 12, as in your
maths book."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# What the book's two pictures hold, written once and reused by the question and solution cards.
ANT_GRID = ("A square grid of 11 by 11 squares, each square 1 cm, with the label 1 cm in the top right corner and a "
            "compass card in the top left corner with N at the top, E in red on the right, S at the bottom and W on "
            "the left. One ant stands on a grid point near the middle. Sugar lies above it near the top, a plate of "
            "laddoos lies to its right, a slice of bread lies at the lower left and an apple lies at the lower right.")
ZOO_MAP = ("A map of a zoo drawn on a grid of 12 columns and 12 rows, with dashed lines across and up, a cream path "
           "that loops round a round pond with a hippo in the middle, the lines numbered 1 to 12 along the bottom in "
           "teal and up the left side in pink, 0 at the bottom left corner, a sign ZOO at the bottom and a small "
           "compass card beside the map. The animals stand on the lawns and paths: a parrot on a tree at the top left "
           "corner, a flamingo near the top left, a toucan on a tree at the top right corner, a giraffe and a zebra "
           "in the upper right, a big cat to the right of the pond, a slim deer at the right, a tiger at the left, a "
           "snake at the left edge, an elephant in the middle below the pond, a lion at the lower left, a monkey on a "
           "big tree at the lower right, a panda at the bottom left corner, a tortoise at the bottom and a crocodile "
           "at the bottom right.")

# ============================== T6 Distance and Direction on a Grid ========================================
TOPICS.append(TOPIC(
    "T6", "M3", "Distance and Direction on a Grid", ["Anthill in the Zoo"], "Apply",
    "Students describe a path on a grid as distances in cm with directions, and find the shortest route to a point by "
    "counting squares and leaving out steps that go the wrong way.",
    "On a grid every square is 1 cm. A path is a list of legs, each with a distance in cm and a direction. Several "
    "routes can reach the same point, and the shortest route goes only towards the point.",
    [A("T6.C1", "Distance and Direction on a Grid", "Understand",
       "Students count the squares of a grid along a straight line to find a distance in cm, name its direction, and "
       "write a path with a turn as two legs.",
       textbook=["The arrows show the direction in which the ant can move.",
                 "Fill in the blanks below with the distances and the directions in which the ant must move from its "
                 "starting position."],
       teach=["Predict first: an ant stands on a grid point. A leaf lies 4 squares away along a grid line, on the west "
              "side. Each square is 1 cm. How far must the ant crawl, and in which direction?",
              "The ant can crawl only along the lines of the grid. The arrows show the direction in which it can move, "
              "and the compass tells you which way is north, east, south and west.",
              "Count the squares along the line. 4 squares of 1 cm each are 4 cm, so the leaf is 4 cm towards the "
              "west.",
              "A distance always comes with a direction. 6 cm towards the south is not the same place as 6 cm "
              "towards the north.",
              "Some food is not on one straight line. Take a berry 2 squares to the east and 4 squares to the "
              "north. The ant crawls 2 cm towards the east, turns, and crawls 4 cm towards the north. Each straight "
              "part is a leg. This path has two legs and its length is 2 + 4 = 6 cm.",
              "Say a path as a list of legs: 2 cm towards the east, then 4 cm towards the north.",
              "Rule: each square is 1 cm. Count the squares in a straight line for the distance, say the direction, "
              "and write a path with turns as one leg after another."],
       examples=[WE("An ant starts from its anthill, a grid point of a grid of 1 cm squares. A leaf is 4 squares to "
                    "the west. A seed is 6 squares to the south. A berry is 2 squares to the east and then 4 "
                    "squares to the north. How far, and in which direction, must the ant crawl to reach each one?",
                    ["Each square of the grid is 1 cm. Count the squares along a grid line to find a distance.",
                     "Leaf: count 4 squares to the west. The ant crawls 4 cm towards the west.",
                     "Seed: count 6 squares to the south. The ant crawls 6 cm towards the south.",
                     "Berry: it is not on one straight line. First count 2 squares to the east, then turn and count "
                     "4 squares to the north.",
                     "The path has two legs: 2 cm towards the east, then 4 cm towards the north.",
                     "Length of the path: 2 + 4 = 6 cm.",
                     "Check: 4 squares are 4 cm and 6 squares are 6 cm. The two legs of the berry path are 2 squares "
                     "and 4 squares, and 2 + 4 = 6 squares, which is 6 cm."],
                    "Leaf: 4 cm towards the west. Seed: 6 cm towards the south. Berry: 2 cm towards the east, then "
                    "4 cm towards the north, 6 cm in all")],
       ncert=["ant.setup"], key_terms=["distance", "direction", "grid", "leg", "cm"], minutes=6),
     A("T6.C2", "Finding the Shortest Route", "Analyze",
       "Students compare routes to the same point on a grid by adding the cm of their legs, and name the shortest "
       "route as the one with no step the wrong way.",
       teach=["Predict first: a berry is 4 cm to the east and 3 cm to the north of the ant. The ant can go east "
              "first or north first, or even wander a little. Which routes along the grid lines are the shortest?",
              "Route 1: crawl 4 cm towards the east, then 3 cm towards the north. The length is 4 + 3 = 7 cm.",
              "Route 2: crawl 3 cm towards the north, then 4 cm towards the east. The length is 3 + 4 = 7 cm. The "
              "same length, in a different order.",
              "Route 3: crawl 5 cm towards the east, then 3 cm towards the north, then 1 cm towards the west. The "
              "length is 5 + 3 + 1 = 9 cm. The step towards the west is a step the wrong way, and it adds length.",
              "The shortest routes are 7 cm. They go only towards the berry, east and north, and never west or "
              "south.",
              "Turns do not decide the length. Try 2 cm east, 1 cm north, 2 cm east, then 2 cm north. It has three "
              "turns. Its length is 2 + 1 + 2 + 2 = 7 cm, so it is a shortest route too. Count the cm, not the "
              "turns.",
              "Rule: the shortest route goes only towards the food. A step the wrong way adds to the length."],
       examples=[WE("A berry is 4 cm to the east and 3 cm to the north of the ant. Route 1: 4 cm east, then 3 cm "
                    "north. Route 2: 3 cm north, then 4 cm east. Route 3: 5 cm east, then 3 cm north, then 1 cm west. "
                    "Find the length of each route. Which routes are the shortest?",
                    ["Route 1 has two legs, 4 cm east and 3 cm north. Length: 4 + 3 = 7 cm.",
                     "Route 2 has two legs, 3 cm north and 4 cm east. Length: 3 + 4 = 7 cm.",
                     "Route 3 has three legs, 5 cm east, 3 cm north and 1 cm west. Length: 5 + 3 + 1 = 9 cm.",
                     "Routes 1 and 2 are both 7 cm. Route 3 is 9 cm, which is 2 cm longer.",
                     "Route 3 goes 1 cm towards the west, away from the berry, and so it also needs 1 cm more towards "
                     "the east. These two extra steps make the 2 cm.",
                     "Check: the berry is 4 cm east and 3 cm north, and 4 + 3 = 7. A route that goes only east and "
                     "north cannot be shorter than 7 cm."],
                    "Routes 1 and 2 are 7 cm and are the shortest. Route 3 is 9 cm, because it goes 1 cm the wrong "
                    "way")],
       key_terms=["shortest route", "legs", "wrong way"], misconceptions=["M_FEW_TURNS"], minutes=6),
     DOER("T6.C3", "Practice: Ant Path", "ant_path", "Apply",
          "Students trace the path of the ant on the grid to the laddoos, the sugar, the bread and the apple, say each "
          "leg as cm and a direction, and find the shortest route to the apple.",
          ["Each square of the grid is 1 cm. Count the squares for the distance and say the direction.",
           "A path with turns is a list of legs, for example 2 cm towards the east, then 4 cm towards the north.",
           "The shortest route goes only towards the food. A step the wrong way adds to the length.",
           "Count the cm of each route, not its turns."],
          items=[FIO("ant.laddoo", "Example 1: the ant and the laddoos",
                     "To get to the laddoos, the ant has to crawl how far, and towards which direction? Each square of the grid is 1 cm.",
                     ["Each square of the grid is 1 cm. The ant crawls along the grid line that goes from the ant to "
                      "the plate of laddoos.",
                      "Count the squares from the ant to the laddoos: 2 squares, so 2 cm.",
                      "Look at the compass. The laddoos are on the right of the ant, on the side of E, so the "
                      "direction is east.",
                      "Check: 2 squares of 1 cm each are 2 cm, and the compass says the right side is east."],
                     "2 cm towards the east.",
                     kind="example",
                     q_figure=ANT_GRID + " The ant may crawl along the grid lines only.",
                     s_figure="The same grid with a red dashed arrow from the ant to the laddoos, 2 squares long, "
                              "labelled 2 cm east."),
                 FIO("ant.b", "Anthill in the Zoo: the sugar",
                     "To get to the sugar, the ant has to crawl ___ cm in the ___ direction.",
                     ["Each square of the grid is 1 cm. Start at the ant.",
                      "The sugar is straight above the ant, on the same grid line. Count the squares up to the "
                      "sugar: 3 squares, so 3 cm.",
                      "Look at the compass. N is at the top, so up is north.",
                      "The ant crawls 3 cm in the north direction.",
                      "Check: 3 squares of 1 cm each are 3 cm, and the arrow on the route points up, towards N."],
                     "3 cm in the north direction.",
                     kind="prompt",
                     q_figure=ANT_GRID + " A red dashed route with an arrowhead leads from the ant to the sugar and "
                              "ends in a red dot. No distance is written.",
                     s_figure="The same grid with the red dashed arrow from the ant up to the sugar, 3 squares long, "
                              "labelled 3 cm north."),
                 FIO("ant.c", "Anthill in the Zoo: the bread",
                     "To get to the bread, the ant has to crawl ___ cm in the ___ direction; then ___ cm in the ___ "
                     "direction.",
                     ["The bread is not on the same line as the ant, so the route has two legs and turns once.",
                      "First leg: count the squares from the ant to the corner of the route on the left: 3 squares, "
                      "so 3 cm. The left side is the side of W, so the direction is west.",
                      "Second leg: at the corner the ant turns and crawls down to the bread: 2 squares, so 2 cm. "
                      "Down is the side of S, so the direction is south.",
                      "The whole path is 3 cm west, then 2 cm south. Its length is 3 + 2 = 5 cm.",
                      "Check: the two legs are 3 squares and 2 squares, and 3 + 2 = 5 squares of 1 cm each."],
                     "3 cm in the west direction; then 2 cm in the south direction, 5 cm in all.",
                     kind="prompt",
                     q_figure=ANT_GRID + " A red dashed route with arrowheads leads from the ant to the bread in two "
                              "straight parts joined by one turn, and ends in a red dot. No distance is written.",
                     s_figure="The same grid with the red dashed route to the bread, the first leg labelled 3 cm west "
                              "and the second leg labelled 2 cm south."),
                 FIO("ant.d", "Anthill in the Zoo: the apple",
                     "To get to the apple, the ant needs to crawl ___ cm towards ___, and then ___ cm towards ___, "
                     "and finally ___ cm towards ___.",
                     ["The route to the apple is drawn with three legs, so it turns twice.",
                      "First leg: count the squares down the grid line from the ant to the corner at the bottom: 5 "
                      "squares, so 5 cm towards south.",
                      "Second leg: at the corner the ant turns and crawls to the right: 3 squares, so 3 cm towards "
                      "east.",
                      "Third leg: it turns again and crawls up to the apple: 2 squares, so 2 cm towards north.",
                      "Length of the whole route: 5 + 3 + 2 = 10 cm.",
                      "Check: south 5 cm, east 3 cm, north 2 cm. The three legs are 5, 3 and 2 squares of 1 cm "
                      "each."],
                     "5 cm towards south, 3 cm towards east, and finally 2 cm towards north, 10 cm in all.",
                     kind="prompt",
                     q_figure=ANT_GRID + " A red dashed route with arrowheads leads from the ant to the apple in "
                              "three straight parts joined by two turns, and ends in a red dot. No distance is "
                              "written.",
                     s_figure="The same grid with the red dashed route to the apple, the legs labelled 5 cm south, "
                              "3 cm east and 2 cm north."),
                 FIO("ant.routes", "Anthill in the Zoo: other routes",
                     "Identify other routes to reach the point where apple is located. Which one is the shortest?",
                     ["Find where the apple is. It is 3 squares to the right of the ant and 3 squares below it: "
                      "3 cm towards the east and 3 cm towards the south.",
                      "Route 1: 3 cm towards east, then 3 cm towards south. Length: 3 + 3 = 6 cm.",
                      "Route 2: 3 cm towards south, then 3 cm towards east. Length: 3 + 3 = 6 cm.",
                      "Route 3: 1 cm towards south, 3 cm towards east, then 2 cm towards south. Length: "
                      "1 + 3 + 2 = 6 cm.",
                      "The route drawn in your maths book is 5 cm south, 3 cm east and 2 cm north. Length: "
                      "5 + 3 + 2 = 10 cm.",
                      "The shortest routes are the 6 cm routes. They go only east and south. The 10 cm route has a "
                      "step towards the north, away from the apple.",
                      "Check: any route made of 3 cm east and 3 cm south, in any order, is 6 cm. Your answer may "
                      "differ."],
                     "Sample answer: 3 cm east then 3 cm south, or 3 cm south then 3 cm east. Each is 6 cm, a shortest "
                     "route. Your answer may differ.",
                     kind="prompt",
                     q_figure=ANT_GRID + " One red dashed route with arrowheads leads from the ant to the apple in "
                              "three straight parts joined by two turns, and ends in a red dot.",
                     s_figure="The same grid with three shortest routes to the apple in three colours, each 6 cm: "
                              "teal 3 cm east then 3 cm south, amber 3 cm south then 3 cm east, green 1 cm south, 3 cm "
                              "east, then 2 cm south. The red route of 10 cm is drawn thin beside them.")],
          misconceptions=["M_FEW_TURNS"])],
    key_terms=["grid", "distance", "direction", "shortest route"]))

# ============================== T7 Locating Places on a Grid ================================================
TOPICS.append(TOPIC(
    "T7", "M3", "Locating Places on a Grid", ["Locating the Animals in the Zoological Park (Zoo)"], "Apply",
    "Students read the position of a place on a grid by moving east to its column and then north to its row, write it "
    "as (column,row), and see that the order of the two numbers matters.",
    "A position on a grid tells a place with two numbers. Start at 0, move east to the column, then north to the row, "
    "and write the column first and the row second. Two positions with the same numbers in another order are two "
    "different places.",
    [A("T7.C1", "Reading a Position: Column and Row", "Understand",
       "Students find the position of a place on a grid by moving east from 0 to its column and then north to its "
       "row, and write it as (column,row).",
       textbook=["Children observe a map of the zoo drawn on a grid. Each vertical line (column) and horizontal line "
                 "(row) is marked with a number.",
                 "First move horizontally from 0 and then vertically.",
                 "We write the meeting point of the first row and the first column as (1,1)."],
       teach=["Predict first: the zoo map is drawn on a grid with a number on every line. To find the giraffe you "
              "start at 0. Do you walk east first or north first?",
              "Each vertical line is a column and each horizontal line is a row, and every line has a number. The "
              "numbers belong to the lines, and an animal stands where a column line and a row line meet.",
              "Start at 0, the corner at the bottom left. First move horizontally towards the east along the "
              "bottom, counting the column lines, until you reach column 8. That is 8 steps east.",
              "Then move vertically towards the north, counting the row lines, until you reach row 9. That is 9 "
              "steps north. The giraffe stands at this meeting point.",
              "We write the two numbers in a bracket with the column first and the row second: (8,9). In the same "
              "way the meeting point of column 1 and row 1 is (1,1).",
              "Rule: start at 0, first move east to the column, then north to the row, and write (column,row)."],
       examples=[WE("Find the position of the giraffe on the zoo map. Start from 0, move east to the 8th column, then "
                    "move north to the 9th row. How do we write the position?",
                    ["Start at 0, the corner at the bottom left of the grid.",
                     "Move east along the bottom line, counting the numbered column lines 1, 2, 3 up to 8. Stop at "
                     "column 8. That is 8 steps east.",
                     "From there move north along the column line, counting the row lines 1, 2, 3 up to 9. Stop at "
                     "row 9. That is 9 steps north.",
                     "The giraffe stands where column 8 and row 9 meet.",
                     "Write the column first and the row second: (8,9).",
                     "Check: 8 steps east first, then 9 steps north, and the bracket (8,9) lists the column and then "
                     "the row."],
                    "The giraffe is at (8,9): 8 steps east, then 9 steps north")],
       ncert=["zoo.setup", "zoo.rule", "zoo.hint"], key_terms=["position", "column", "row"], minutes=6),
     A("T7.C2", "The Order of the Two Numbers", "Understand",
       "Students explain why the order of the two numbers in a position matters, and tell (8,9) from (9,8) by saying "
       "how many steps east and how many steps north each one is.",
       teach=["Predict first: you walk 8 steps east and 9 steps north to the giraffe. A friend walks 9 steps east "
              "and 8 steps north. Does the friend reach the giraffe?",
              "No. The friend reaches a different meeting point, (9,8), a spot on the path where no animal "
              "stands.",
              "The first number tells the steps east, the column. The second number tells the steps north, the "
              "row. So (8,9) and (9,8) are two different places.",
              "To read a position, say it as a walk: first east, then north.",
              "Rule: the first number is always the column, the second number is always the row."],
       examples=[WE("A child says that the giraffe is at (9,8). Is that right?",
                    ["The giraffe stands at (8,9): 8 steps east, then 9 steps north.",
                     "(9,8) means 9 steps east, then 8 steps north. That is a different meeting point.",
                     "Walk it on the map: start at 0, move east to column 9, then north to row 8. This is a spot on "
                     "the path, and no animal stands there.",
                     "The first number is the column and the second number is the row, so changing the order changes "
                     "the place.",
                     "Check: (8,9) is the giraffe and (9,8) is not, so (8,9) and (9,8) are not the same place."],
                    "No. The giraffe is at (8,9). (9,8) is 9 steps east and 8 steps north, a spot with no animal")],
       key_terms=["order", "column", "row", "numbers"], misconceptions=["M_ORDER_SWAP"], minutes=4),
     DOER("T7.C3", "Practice: Zoo Grid Locator", "zoo_grid", "Apply",
          "Students walk east and then north on the zoo grid to find the animal at a position, write the position of "
          "an animal, and mark positions with coloured dots.",
          ["Start at 0. Move east to the column, then north to the row.",
           "Write a position as (column,row), the column first and the row second.",
           "Two positions with the same numbers in another order are different places.",
           "To mark a position, walk to it in the same way and put the dot at the meeting point."],
          items=[FIO("zoo.panda", "Example 2: reaching the panda",
                     "Start from 0 on the zoo map. How do you reach the panda, and how do we write its position?",
                     ["Start from 0, the corner at the bottom left of the zoo map.",
                      "Move one step horizontally towards the east along the bottom line. You reach the first "
                      "column.",
                      "From there move one step up, towards the north, along the first column line. You reach the "
                      "first row.",
                      "The panda is where the first column and the first row meet.",
                      "Write the column number first and the row number second: (1,1).",
                      "Check: 1 step east and 1 step north end at the panda, and (1,1) says the same, column 1 and "
                      "row 1."],
                     "From 0, move 1 step east to the first column, then 1 step north to the first row. The panda is "
                     "at (1,1).",
                     kind="example",
                     q_figure=ZOO_MAP,
                     s_figure="The zoo map with a teal arrow from 0 east along the bottom to line 1, then a green "
                              "arrow 1 step north to the panda, and (1,1) written beside the panda."),
                 FIO("zoo.tortoise", "Locating the Animals: the tortoise",
                     "To reach the tortoise, move ___ steps towards east and reach the ___ column. Then move ___ "
                     "step(s) ___ and reach the first ___.",
                     ["Start from 0 and move horizontally towards the east along the bottom line, counting the "
                      "numbered column lines: 1, 2, 3, 4.",
                      "The tortoise stands on the fourth column line, so move 4 steps towards east and reach the "
                      "4th column.",
                      "Now move up towards the north. The tortoise is on the first row line, so move 1 step north "
                      "and reach the first row.",
                      "The blanks are: 4 steps, 4th column, 1 step, north, row.",
                      "Check: the position of the tortoise is (4,1), the column first and the row second."],
                     "Move 4 steps towards east and reach the 4th column. Then move 1 step north and reach the first "
                     "row. The position is (4,1).",
                     kind="prompt",
                     q_figure=ZOO_MAP,
                     s_figure="The zoo map with a teal arrow from 0 east along the bottom to line 4, then a green "
                              "arrow 1 step north to the tortoise, and (4,1) written beside the tortoise."),
                 FIO("zoo.at14", "Locating the Animals: what is at (1,4)",
                     "The location of the tortoise is (4,1). What is at (1,4)?",
                     ["The first number of a position is the column and the second number is the row. (4,1) is "
                      "column 4 and row 1: the tortoise.",
                      "(1,4) is column 1 and row 4. Start from 0 and move 1 step east to the first column.",
                      "Then move 4 steps north to the fourth row.",
                      "Look at the map where the first column and the fourth row meet: a snake lies there.",
                      "(1,4) is not the same place as (4,1). The numbers are in a different order, so a different "
                      "animal is there.",
                      "Check: column 1 and row 4 is the snake, and column 4 and row 1 is the tortoise."],
                     "A snake. (1,4) is 1 step east, then 4 steps north.",
                     kind="prompt",
                     q_figure=ZOO_MAP,
                     s_figure="The zoo map with a teal arrow from 0 east along the bottom to line 1, then a green "
                              "arrow 4 steps north to the snake, and (1,4) written beside the snake."),
                 FIO("ZQ1", "Zoo Grid Questions: Q1 locate the animal",
                     "Locate the animal at the following positions on the map. (a) (11,11) ___ (b) (2,6) ___ "
                     "(c) (6,4) ___ (d) (3,10) ___ (e) (11,3) ___ (f) (10,9) ___",
                     ["For every position, start from 0. The first number tells the steps east to the column. The "
                      "second number tells the steps north to the row.",
                      "Part (a), (11,11): 11 steps east, then 11 steps north. A toucan sits on the tree at the top "
                      "right corner.",
                      "Part (b), (2,6): 2 steps east, then 6 steps north. The animal is a tiger.",
                      "Part (c), (6,4): 6 steps east, then 4 steps north. The animal is an elephant.",
                      "Part (d), (3,10): 3 steps east, then 10 steps north. The animal is a flamingo.",
                      "Part (e), (11,3): 11 steps east, then 3 steps north. The animal is a monkey, on the big "
                      "tree.",
                      "Part (f), (10,9): 10 steps east, then 9 steps north. The animal is a zebra.",
                      "Check: each animal stands where its column line and its row line meet."],
                     "(a): toucan; (b): tiger; (c): elephant; (d): flamingo; (e): monkey; (f): zebra.",
                     kind="exercise",
                     q_figure=ZOO_MAP,
                     s_figure="The zoo map with six orange rings, one at each asked position, and the name beside each "
                              "ring: toucan, tiger, elephant, flamingo, monkey and zebra."),
                 FIO("ZQ2", "Zoo Grid Questions: Q2 write the position",
                     "Write the position of the following animals on the map. (a) Lion ___ (b) Elephant ___ "
                     "(c) Tortoise ___ (d) Deer ___ (e) Panda ___ (f) Crocodile ___",
                     ["For each animal, look at the numbers of the lines that meet at it. Read the column number "
                      "along the bottom and the row number up the side. Write the column first.",
                      "Part (a), lion: column 3 and row 3, so (3,3).",
                      "Part (b), elephant: column 6 and row 4, so (6,4).",
                      "Part (c), tortoise: column 4 and row 1, so (4,1).",
                      "Part (d), deer: column 10 and row 6, so (10,6).",
                      "Part (e), panda: column 1 and row 1, so (1,1).",
                      "Part (f), crocodile: column 10 and row 1, so (10,1).",
                      "Check: walk from 0 to each position, east first and then north, and you reach the animal."],
                     "(a): lion (3,3); (b): elephant (6,4); (c): tortoise (4,1); (d): deer (10,6); (e): panda (1,1); "
                     "(f): crocodile (10,1).",
                     kind="exercise",
                     q_figure=ZOO_MAP,
                     s_figure="The zoo map with six orange rings, one at each of the six animals, and its position "
                              "beside it: lion (3,3), elephant (6,4), tortoise (4,1), deer (10,6), panda (1,1) and "
                              "crocodile (10,1)."),
                 FIO("ZQ3", "Zoo Grid Questions: Q3 place the dots",
                     "Place dots of different colours on the following positions. (a) (8,3) (Red) (b) (2,9) (Green) "
                     "(c) (7,3) (Blue) (d) (3,8) (Orange) (e) (8,6) (Black) (f) (6,6) (Pink)",
                     ["For every dot, start from 0, move east to the column, then north to the row, and mark the "
                      "meeting point.",
                      "Part (a), (8,3): 8 steps east, then 3 steps north. Put a red dot there.",
                      "Part (b), (2,9): 2 steps east, then 9 steps north. Put a green dot there.",
                      "Part (c), (7,3): 7 steps east, then 3 steps north. Put a blue dot there.",
                      "Part (d), (3,8): 3 steps east, then 8 steps north. Put an orange dot there.",
                      "Part (e), (8,6): 8 steps east, then 6 steps north. Put a black dot there.",
                      "Part (f), (6,6): 6 steps east, then 6 steps north. Put a pink dot there.",
                      "Check: the six dots are in six different places, and each pair has the column first."],
                     "Dots at (8,3) red, (2,9) green, (7,3) blue, (3,8) orange, (8,6) black and (6,6) pink.",
                     kind="exercise",
                     q_figure=ZOO_MAP + " No dots are drawn yet.",
                     s_figure="The zoo map with six dots: red at (8,3), green at (2,9), blue at (7,3), orange at (3,8), "
                              "black at (8,6) and pink at (6,6), each at the meeting point of its column line and its "
                              "row line.")],
          misconceptions=["M_ORDER_SWAP"])],
    key_terms=["position", "column", "row", "order"]))

# ============================== T8 Chapter Revision (summary) ===============================================
TOPICS.append(TOPIC(
    "T8", "M3", "Chapter Revision: Maps and Locations", ["Chapter summary"], "Understand",
    "",
    "The whole school trip in one walk: finding east by the rising Sun, directions on a picture and from where you "
    "stand, turning right and left on a street map, the metro map with its lines and interchanges, a map with a key, "
    "distance and direction on a grid, the shortest route and the position of a place by its column and row.",
    [A("T8.C1", "Chapter Revision: Maps and Locations", "Understand",
       "",
       teach=["Predict first: you have taken the whole school trip. Can you say one idea from each stop, from the "
              "rising Sun to the zoo? Read the lines below and tick each idea you remembered.",
              "Finding directions: face the rising Sun and you face east. Your left hand points north, your right "
              "hand points south, and west is behind you.",
              "Check: if you face north, which hand points east? The right hand, and the left hand points west.",
              "Directions on a picture: with a compass, N is at the top, S at the bottom, E on the right and W on the "
              "left. If a swing is at the top left and a slide at the top right, the slide is east of the swing.",
              "Check: the swing is west of the slide. If A is east of B, then B is west of A.",
              "Directions from where you stand: the direction of a thing is said from a person or a place. A girl "
              "stands at the centre of a room. A table above her is north of her. A bed on her right is east. A "
              "door below her is south. A cupboard on her left is west.",
              "Check: from the bed, the girl is to the west.",
              "Street map: a map shows roads and places seen from above, the compass shows north, and a dotted line "
              "shows a route. A right turn takes north to east, east to south, south to west and west to north. A "
              "left turn goes the other way round.",
              "Check: a cycle drives north, turns left and turns left again. It drives west and then south. The bus "
              "that drives north and turns right drives east, and a second right turn makes it drive south.",
              "Metro map: coloured lines are different routes and a circle is a station. A capsule with two coloured "
              "dots is an interchange, where you can change from one line to the other. Where two lines cross without "
              "a capsule, you cannot change lines.",
              "Check: count the circles between two stations and do not count the two ends. A capsule counts as one "
              "station. Hauz Khas to Kalkaji Mandir has 4 stations between. Kalkaji Mandir to Badarpur has 6. So "
              "there are 4 + 1 + 6 = 11 stations between Hauz Khas and Badarpur. The 1 is Kalkaji Mandir, where you "
              "change lines.",
              "Making a map: a map uses symbols, and the key says what each symbol means. Mark a hidden thing with "
              "a red dot.",
              "Check: in a library corner, a long rectangle can be a shelf and a square with 4 small squares a table "
              "with 4 chairs. Every symbol on the map must be in the key.",
              "Distance and direction on a grid: each square is 1 cm. Count the squares for the distance and say the "
              "direction. A path with turns is a list of legs.",
              "Check: 2 cm towards the east, then 4 cm towards the north is 2 + 4 = 6 cm.",
              "Shortest route: it goes only towards the food. A berry 4 cm east and 3 cm north is 4 + 3 = 7 cm away "
              "along the lines. A route with a step 1 cm the wrong way is longer: 5 + 3 + 1 = 9 cm.",
              "Check: the apple of your maths book is 3 cm east and 3 cm south of the ant. A shortest route is 3 + 3 = 6 "
              "cm. The route drawn there is 5 + 3 + 2 = 10 cm, so it is not the shortest.",
              "Position on a grid: start at 0, move east to the column, then north to the row, and write "
              "(column,row). The giraffe is 8 steps east and 9 steps north, so it is at (8,9). The panda is at (1,1) "
              "and the tortoise is at (4,1).",
              "Check: (9,8) is another place, because the column comes first. The first number is the steps east.",
              "Which stop would you like to try again? Pick one idea and say its rule aloud."],
       ncert=["summary"], key_terms=["direction", "map", "position", "route"], minutes=6, enrichment=True)],
    topic_type="summary"))
