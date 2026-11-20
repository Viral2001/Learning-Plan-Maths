# -*- coding: utf-8 -*-
"""Chapter-level content for Class 5 Chapter 14, Maps and Locations (Maths Mela, Grade 5, Chapter 14).

The plan follows the "Class 5 Mathematics Learning Experience Designer" brief (priority_doc.md sections A to F) and the
/lp pipeline's structure; the book decides every picture and every question. Book lines are verbatim except: the book's
dashes become commas, colons or "to"; positions are written (column,row) with no space; the book's "(3,8 (Orange)" is
printed (3,8) and "(6, 6)" is printed (6,6). No em dash and no en dash anywhere here."""
from __future__ import annotations

CHAPTER = {
    "grade": 5,
    "label": "Class 5",
    "chapter_no": 14,
    "name": "Maps and Locations",
    "book_part": "Maths Mela, Grade 5, Chapter 14",
    "source_pdf": "textbooks/class-5/eemm114.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Directions and Pictures",
     "Finding east by facing the rising Sun, naming the four directions, and saying which thing is north, south, east "
     "or west of another thing or of a person on a picture with a compass."),
    ("M2", "Street Maps, Metro Maps and Keys",
     "Reading a street map and the direction a bus drives after a right or left turn, reading a metro map with its "
     "coloured lines, stations and interchanges, and making a map with a key."),
    ("M3", "Grids, Distances and Positions",
     "Describing a path on a grid with distances and directions, finding the shortest route, and locating a place by "
     "its column and row, in a revision of the whole trip."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows one school trip. It starts with a bird that finds its way and a child who faces the "
             "rising Sun, then reads the camp, a room, a street map with a bus route, a metro map, an ant's grid and "
             "the animals of a zoo. A short video explains each idea, and an interactive tool lets the student try it "
             "alone.",
    "points": [
        {"title": "Videos teach, tools explore",
         "text": "Every idea has one short concept video. The tool that follows is where the student explores, "
                 "steers, counts and checks the idea alone, with hints, retry and reset. Six tools, each with its own "
                 "purpose, follow the chapter's own plan."},
        {"title": "A tool in three steps",
         "text": "Each tool opens with a short recall of the video idea, then lets the student play and apply it, and "
                 "ends with the chapter's own questions, used exactly as the book gives them."},
        {"title": "Every book question has its own video",
         "text": "Every solved example and every answerable question of the book is its own short video with a step "
                 "by step solution and a question picture and a solution picture, in a Questions topic that follows "
                 "the idea it practises."},
        {"title": "The picture is the mathematics",
         "text": "Compass roses, street maps, the metro map, the ant's grid and the zoo grid carry each idea. The "
                 "compass is the same on every board: N at the top, E in red on the right."},
        {"title": "Only the book's pictures and numbers",
         "text": "Roads, stops, metro lines, grid sizes and the places of animals and foods are the book's own. Any "
                 "number the plan adds is a practice value and is said to be one."},
    ],
}

# {module_id: strand letter}: the subject strand each module belongs to (core/qt.py builds every objective's strand).
# CBSE maths catalog: N Number, A Algebra, G Geometry, M Measurement, D Data, S Statistics and Probability.
MODULE_STRANDS = {"M1": "G", "M2": "G", "M3": "G"}

# every book item, with its kind. Home concepts are listed in DESIGN.md section 3.
NCERT_ITEMS = [
    # the opener: finding directions
    "open.cranes", "open.poem", "open.sun", ("note.dir", "talk"),
    ("open.manu", "prompt"), ("open.west", "prompt"),
    # Bird Watching and Map of a Room
    "bird.setup",
    ("bird.colour", "prompt"), ("bird.draw", "prompt"),
    ("room.dir", "prompt"), ("room.draw", "prompt"), ("room.names", "prompt"),
    # Zoo Trip, the street map and the bus route
    "trip.story", ("note.street", "talk"),
    ("bus.s1", "prompt"), ("bus.s2", "prompt"), ("bus.a", "prompt"), ("bus.b", "prompt"), ("bus.c", "prompt"),
    ("bus.d", "prompt"), ("bus.e", "prompt"),
    # the metro map
    "metro.intro", "metro.key", ("note.metro", "talk"),
    ("metro.colours", "prompt"), ("metro.mark", "prompt"),
    ("metro.a", "prompt"), ("metro.b", "prompt"), ("metro.c", "prompt"), ("metro.d", "prompt"),
    # Let Us Do: a map of the school
    "school.sample", ("LUD.school", "exercise"),
    # Anthill in the Zoo
    "ant.setup", ("ant.laddoo", "example"), ("ant.b", "prompt"), ("ant.c", "prompt"), ("ant.d", "prompt"),
    ("ant.routes", "prompt"),
    # Locating the Animals in the Zoological Park
    "zoo.setup", "zoo.rule", "zoo.hint",
    ("zoo.panda", "example"), ("zoo.tortoise", "prompt"), ("zoo.at14", "prompt"),
    ("ZQ1", "exercise"), ("ZQ2", "exercise"), ("ZQ3", "exercise"),
    # the summary
    "summary",
]

MISCONCEPTIONS = [
    ("M_LEFT_WEST", "The left hand always points west and the right hand always points east, whichever way you face."),
    ("M_SAME_DIRECTION", "If the tent is east of the lake, then the lake is also east of the tent."),
    ("M_RIGHT_EAST", "A right turn always makes the bus drive east, whichever way it was driving before."),
    ("M_COUNT_ENDS", "The stations between two stations include the two end stations."),
    ("M_CROSS_CHANGE", "You can change from one metro line to another wherever the two lines cross on the map."),
    ("M_FEW_TURNS", "The route with the fewest turns is always the shortest route."),
    ("M_ORDER_SWAP", "The row number comes first in a position, so (4,1) and (1,4) are the same place."),
]

SOLUTION_NOTES = [
    {"item": "Map of a Room: directions from the girl",
     "printed_solution": "The book prints no answer. The room is drawn in perspective with a compass beside it.",
     "correct": "The plan reads the top of the picture as north, the right as east, the left as west. Window: north "
                "(back wall, behind the girl). Bed: east. Cupboard: west (a little behind her). Bedside table, the round "
                "table beside the bed: south (in front of her, a little to the right). The cupboard and the table sit "
                "between two directions, so the answer is a labelled sample answer that may differ."},
    {"item": "Bird Watching: the four clues",
     "printed_solution": "The book prints no answer.",
     "correct": "West of the road: the tent on the left of the road, blue. Closest to the lake: the tent just above the "
                "lake, green. North of the green tent: the tent above it near the top, purple. South of the lake: the "
                "tent below the lake, yellow. The tent to the east of the lake can be drawn anywhere to the right of "
                "the lake."},
    {"item": "Your own room (draw your room, names in the four directions)",
     "printed_solution": "These depend on the student's own room.",
     "correct": "The plan gives a labelled sample answer from a sample room of its own and says the student's answer "
                "will differ."},
    {"item": "Street map: the dotted route and the stops",
     "printed_solution": "The map shows extra dashes near the parking area and the road the bus drives north on has no "
                         "name.",
     "correct": "The plan uses only the route the text describes: north from the parking area, right turn onto Hospital "
                "Road (east) to Stop 1, right turn onto Park Road (south) to Stop 2. Stop 1 is at the hospital gate, "
                "Stop 2 beside the shopping centre."},
    {"item": "Street map questions (a) to (e)",
     "printed_solution": "The book prints no answers.",
     "correct": "(a) Prem's house and Raju's house (east of Park Road). (b) and (d) one sample route each, other routes "
                "along the roads are right too. (c) Stop 1. (e) south (Stop 2 is below Prem's house, a little to the "
                "left). No distances are printed, so closer is judged from the picture."},
    {"item": "Metro map: counting stations",
     "printed_solution": "The map is a drawing and the book prints no answer. Not every station is named.",
     "correct": "The plan counts the circles drawn between the two end stations, an interchange capsule counts as one "
                "station. Route A (Yellow Line to Rajiv Chowk, Blue Line): 14 between. Route B (Yellow to INA, Pink to "
                "Mayur Vihar, Blue): 15. Route C (Yellow to Hauz Khas, Magenta to Botanical Garden, Blue): 25. To be "
                "confirmed."},
    {"item": "Metro question (b): Lali's suggestion",
     "printed_solution": "The Magenta Line runs both east and west from Hauz Khas.",
     "correct": "East, it meets the Blue Line at Botanical Garden; west, at Janakpuri West (31 stations between "
                "instead of 25). The plan answers Botanical Garden and mentions the other."},
    {"item": "Metro questions (c) and (d)",
     "printed_solution": "(d) asks what the student thinks is best.",
     "correct": "(c) Route A has the fewest stations. (d) is an opinion: the plan's sample answer is Route A (fewest "
                "stations, one change) and it says the answer may differ."},
    {"item": "Let Us Do: a map of your school",
     "printed_solution": "The student's own drawing. The sample map shows a small square near the lower right corner that "
                         "has no symbol in its key.",
     "correct": "The plan gives a labelled sample answer and does not describe that small square."},
    {"item": "Anthill in the Zoo: the lines the ant crawls on",
     "printed_solution": "The book says the ant can only crawl along the dotted lines on the grid; the grid has solid "
                         "grey lines and the routes are red dashed lines.",
     "correct": "The plan reads the grid lines as the lines the ant may crawl on, otherwise there could be no other "
                "routes. The grid is 11 by 11 squares of 1 cm. Part (a), 2 cm towards the east, is printed already "
                "answered and is Example 1."},
    {"item": "Anthill in the Zoo: the shortest route to the apple",
     "printed_solution": "The book asks for other routes and the shortest, and prints no answer.",
     "correct": "The apple is 3 cm east and 3 cm south of the ant. The book's route is 5 + 3 + 2 = 10 cm. The shortest "
                "routes are 3 cm east and 3 cm south in any order, 6 cm."},
    {"item": "Zoo grid: what the numbers belong to",
     "printed_solution": "Each vertical line (column) and horizontal line (row) is marked with a number.",
     "correct": "The numbers belong to the grid lines. A position is written (column,row), east number first. The grid "
                "has 12 columns and 12 rows plus 0."},
    {"item": "Zoo grid: the names of the animals",
     "printed_solution": "The book names only the lion, elephant, tortoise, deer, panda and crocodile.",
     "correct": "The plan names the others from the picture: toucan (11,11), tiger (2,6), flamingo (3,10), monkey "
                "(11,3), zebra (10,9), snake (1,4). Deer is the slim antelope-like animal at (10,6). The plan's own "
                "examples use the giraffe (8,9)."},
    {"item": "Zoo grid Q3: the printed brackets",
     "printed_solution": "The book prints (3,8 (Orange) with a missing bracket and (6, 6) with a space.",
     "correct": "The plan prints (3,8) and (6,6). The book does not say what is at the six places."},
    {"item": "Opener: which way is west",
     "printed_solution": "The line has no blank and the book prints no answer.",
     "correct": "West is behind Manu, opposite to the rising Sun (east)."},
    {"item": "Notes for Teachers",
     "printed_solution": "Three notes speak to a teacher.",
     "correct": "The plan gives a teacher no role. The discussions the notes suggest are kept as talk items inside the "
                "teaching lines. The plan does not explain how birds find their way, because the book does not."},
    {"item": "Brief: revision video",
     "printed_solution": "The brief asks for an interactive recap or revision video.",
     "correct": "The pipeline has no recap video, so the last topic is a text summary with short concept checks."},
    {"item": "Open prompts (draw a tent, trace a route, a sample map, the best metro route, other routes)",
     "printed_solution": "No single answer.",
     "correct": "The plan gives one reasoned sample answer and says the student's answer may differ."},
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "priority_doc.md (the plan written to the 'Class 5 Mathematics Learning Experience Designer' brief, "
             "2026-11-06): topic flow, video types, the 6 tools, the shared visual language and the learning rules "
             "decide this chapter's design.", "url": ""},
    {"text": "docs/01_runbook.md and .claude/skills/lp/SKILL.md: framing intro with a free-try tool, idea topics each "
             "ending in a Practice concept, a Questions topic after every idea topic with a question concept and an "
             "answer concept per book question, and one summary topic.", "url": ""},
]

# The book's own figures that carry mathematics, keyed by authored concept key. One concept image per teaching,
# hook and summary concept where a drawn figure is the maths; the tool concepts (Practice / free try) are pictured by
# their tool.
FIGURES = {
    "T1.C1": ["A Siberian Crane with four small chicks in flight over hills, and a compass rose with N at the top, E in "
              "red on the right, S at the bottom and W on the left."],
    "T1B.C1": ["A child seen from above standing in a ring, facing the rising Sun on the right of the picture, with the "
               "four directions marked around the child: east in front, north on the left hand, south on the right "
               "hand, west behind."],
    "T2.C1": ["A playground from above with a compass: a swing at the top left, a slide at the top right, a sandpit at "
              "the bottom left and a seesaw at the bottom right."],
    "T2.C2": ["A room plan from above: a girl at the centre, a table above her, a bed to her right, a door below her "
              "and a cupboard to her left, with a compass."],
    "T3.C1": ["A small street map from above: a basketball court in the middle, a road below it with a shopping centre "
              "south of that road, and a block with a pond and one house to the north of the court, with a compass."],
    "T3.C2": ["A road map with a cycle driving north and turning left, then left again, with a compass and a dotted "
              "route."],
    "T4.C1": ["A small part of a metro map: a yellow line and a magenta line crossing at one capsule marked Hauz Khas, "
              "with the key symbols for a metro station and an interchange."],
    "T4.C2": ["A strip of the metro map: the magenta line from Hauz Khas past 4 stations to Kalkaji Mandir, then the "
              "violet line past 6 stations to Badarpur."],
    "T5.C1": ["A plan of a library corner from above with a key of its symbols and one red dot for the hidden "
              "bookmark."],
    "T6.C1": ["A grid of 1 cm squares with an ant on a grid point, a leaf 4 cm to the west, a seed 6 cm to the south "
              "and a berry 2 cm east and 4 cm north."],
    "T6.C2": ["A grid of 1 cm squares with an ant and a berry 4 cm east and 3 cm north, and three routes in three "
              "colours of 7 cm, 7 cm and 9 cm."],
    "T7.C1": ["A 12 by 12 grid of the zoo with numbered lines 0 to 12 and the giraffe at the meeting point of column 8 "
              "and row 9, with the walk east then north drawn."],
    "T7.C2": ["The same grid with the giraffe at (8,9) and a red dot at (9,8) where no animal stands."],
    "T8.C1": ["A trip board with one small card for each idea of the chapter: the compass rose, the room, the street "
              "map, the metro map, the ant's grid and the zoo grid."],
}
