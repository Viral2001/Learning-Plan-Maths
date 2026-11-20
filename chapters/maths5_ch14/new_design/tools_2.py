# -*- coding: utf-8 -*-
"""Tool specs for T3 and T4 of Class 5 Chapter 14 (Maps and Locations): Bus Route Driver (Reading a Street Map) and
Metro Route Planner (Reading a Metro Map). Specs only; the tool pages are built later.

Each tool is made from its concept description: the idea, the screen, what the student does, the practice cards (practice values the plan adds, and the book's own questions with their own wording and values), feedback and hints. Numbers the plan adds are labelled practice values. One activity at a
time, one instruction at a time, large controls, Back and Next in the same place, visible progress, Hint, Retry and
Reset always present, immediate specific feedback that is never red."""
from topics_common import T

TOOLS = {
    "bus_route": T(
        "tool_bus_route", "Bus Route Driver", "manipulative",
        "Steer a bus along the street map and see that a turn is right or left while a direction is north, east, south "
        "or west: a right turn changes north to east, east to south, south to west and west to north, and a left turn "
        "changes the direction the other way round.",
        "The street map board on the trip desk, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. The street map of your maths book is the largest thing on screen, seen from above: the PARKING "
        "area at the bottom, Hospital Road along the top with the Hospital above it, Park Road down the right side "
        "with the Children's Park at the top right, Market Road across the middle between the Basketball Court and "
        "the Shopping Centre, and the houses of Lali, Rohan, Ravi, Prem, Raju, Tinku, Jaideep and Golu. Stop 1 (S1) "
        "stands at the hospital gate and Stop 2 (S2) beside the Shopping Centre. A yellow school bus stands on the "
        "PARKING area facing north. A compass card in the top right corner shows N at the top, E in red on the right, "
        "S at the bottom and W on the left. An instruction strip at the top shows one sentence in large type, with "
        "progress dots under it. A heading panel under the compass reads The bus is driving: north, with a small "
        "arrow that turns with the bus, and a line Last turn: none that changes to right or left after each turn. A "
        "road strip lists the names of the roads the bus has driven on, in order. Controls: Forward (one block), Turn "
        "right and Turn left (the bus turns on the spot at a junction and leaves a red dotted trail behind it); road "
        "name tags Hospital Road, Market Road and Park Road that can be tapped; a tap on a house or a stop selects "
        "it; a Trace switch that, when it is on, puts a round orange marker on the gate of the house the student "
        "taps instead of the bus, so that the same Forward, Turn right and Turn left buttons steer it along the "
        "roads and leave an orange trail; an answer strip for the book's sentences with blank slots and chips "
        "(road chips Hospital, Market and Park; direction chips north, east, south and west; turn chips right and "
        "left); Check, Hint, Undo (takes back the last move), Retry (returns the bus to its last stop), Reset "
        "(returns the bus to the PARKING area and clears the trail), Back and Next in the same places on every card. "
        "Read-outs: the heading panel, the road strip, a blocks driven counter and a card number out of 7.",
        ["The video's small map, where a cycle drove north and a left turn changed its "
         "direction to west. Drive the bus north from the PARKING area up the left main road to the Hospital Road "
         "corner.",
         "Steer the bus with Forward, Turn right and Turn left, read the direction in the "
         "heading panel after every turn, try the same turns on the side roads, and tap the road name tag of the road "
         "the bus is on after a turn.",
         "The book's own bus route sentences for Stop 1 and Stop 2, with the heading panel and the "
         "road strip hidden, and the book's five questions (a) to (e) on the street map: the houses east of "
         "Jaideep's house, the route from Ravi's house to the children's park, the stop closer to Lali's house, "
         "Golu's route to the nearest stop, and the direction Prem moves to reach Stop 2."],
        ["Card 1: drive the bus north from the PARKING area to the Hospital Road corner, then press Turn "
         "right. Read the heading panel. Which direction is the bus driving after the turn? Answer: east, because a "
         "right turn changes north to east.",
         "Card 2: drive east along Hospital Road to the Park Road corner and press Turn right again. Which "
         "direction is the bus driving now? Answer: south, because a right turn changes east to south.",
         "Card 3 (practice values): put the bus on a side road facing north and press Turn right four times, "
         "reading the heading panel each time. Answer: east, then south, then west, then north. After four right "
         "turns the bus faces north again.",
         "Card 4 (practice values): put the bus on a side road facing east and press Turn left, then Turn "
         "left again. Answer: north, then west, because a left turn changes east to north and north to west.",
         "Card 5 (practice values): drive the bus north from the PARKING area only as far as the Market Road "
         "corner, press Turn right and tap the road name tag of the road the bus is on. Which road, and which "
         "direction? Answer: Market Road, driving east, because a right turn changes north to east.",
         "Challenge: 'The bus will start from the parking area. It will go north and then it will take a "
         "right turn onto ___ Road driving in the ___ direction to reach Stop 1 (S1).' and 'To reach Stop 2 (S2), it "
         "will turn ___ (right/left) onto ___ Road driving in the ___ direction.' Drive the route with the heading "
         "panel hidden, then fill the blanks with the chips. Answer: Hospital, east; then right, Park, south. A right "
         "turn changes north to east and a right turn changes east to south.",
         "Challenge: (a) 'Whose houses are situated to the east of Jaideep's house?' (b) 'Mark the route from "
         "Ravi's house to the children's park.' (c) 'Which stop is closer to Lali's house?' (d) 'Golu is running "
         "late. Trace the route to help him reach the nearest bus stop.' (e) 'In which direction would Prem have to "
         "move to reach Stop 2?' Answers: (a) Prem's house and Raju's house. (b) Sample answer: south to the small "
         "road, east to the main road, north to Hospital Road, east to Park Road and the Children's Park. (c) Stop 1 "
         "(S1). (d) Sample answer: south to the road below, east to Park Road, north to Hospital Road, west to Stop "
         "1. (e) South. Other routes along the roads are right too, and your answer may differ."],
        ["Every turn updates the heading panel with a sentence that names both the turn and the direction, for "
         "example: The bus was driving north. A right turn makes it drive east.",
         "Forward moves the bus one block along its road and adds to the red dotted trail. If the bus faces a corner "
         "where it cannot go on, a soft amber note says: The road ends here. Turn right or turn left.",
         "A tap on a road name tag checks the road under the bus. A wrong tag shows a soft amber note such as: Look at "
         "the name written on the road under the bus.",
         "In Trace mode, a move that leaves the roads is refused with: The marker can move only along the roads. "
         "Press Undo to go back to the last junction.",
         "For the questions about houses and stops, a wrong tap shows a clue, for example: East is on the right of "
         "the compass. Look across Park Road, to the right of Jaideep's House. The tool never shows the full answer "
         "before the last hint.",
         "A traced route is never marked wrong when it stays on the roads and ends at the right place. The tool says "
         "Your answer may differ and offers Next."],
        "The bus has been steered with right and left turns, the direction after each turn has been read, the blanks "
        "for Stop 1 and Stop 2 are filled correctly, and the five questions on the street map are answered, with a "
        "route traced from Ravi's house and from Golu's house.",
        ["busPosition", "busHeading", "trail", "roadStrip", "traceMode", "chipsPlaced", "selectedHouseOrStop",
         "challengeIndex"],
        ["M_RIGHT_EAST", "M_SAME_DIRECTION"],
        ["Which way is the bus facing now? Look at the heading panel, or at the arrow on the bus. Is the next turn "
         "right or left?",
         "Say the direction before the turn. Then ask: after a right turn, which direction comes next? A right turn "
         "goes north, east, south, west. A left turn goes north, west, south, east.",
         "If the bus drives north and turns right, it drives east. If it drives east and turns right, it drives "
         "south. Use this to fill the blank.",
         "The tool turns the bus for you and shows the new direction in the heading panel. Then it gives you a "
         "similar turn to try yourself."]),

    "metro_planner": T(
        "tool_metro_planner", "Metro Route Planner", "manipulative",
        "Read the metro map as a network: ride a coloured line, change lines only at a capsule that shows both "
        "colours, and read the counter of stations between two stations, counting every circle and capsule between "
        "the two ends but not the ends.",
        "A station information board on the trip desk, drawn as a warm 3D isometric scene with soft shadows and gentle "
        "animation. The Delhi metro map of your maths book is the largest thing on screen: eight coloured lines (Red, "
        "Yellow, Blue, Airport Express, Green, Violet, Pink and Magenta), circles for stations, capsules for "
        "interchanges, and the station names that are printed on the map, such as Qutb Minar, Hauz Khas, INA, Rajiv "
        "Chowk, Supreme Court, Mayur Vihar and Botanical Garden. A key panel beside the map lists the 10 symbols of "
        "the key: the 8 coloured lines, 9 Metro Station (a plain circle) and 10 Interchange Line (a capsule with two "
        "coloured dots). A route card at the right lists the lines used and the stations where the lines change. An "
        "instruction strip at the top shows one sentence in large type, with progress dots under it. Controls: tap a "
        "start station and an end station; tap a line colour in the key panel to ride along that line, and a thick "
        "highlight in that colour grows along the line; tap a capsule to change line; a Mark switch that puts an "
        "orange ring on a tapped station; a Save route button that keeps up to 3 routes on the route card; "
        "answer cards that click into an answer strip; Undo (takes back the last ride), Clear route, Check, Hint, "
        "Retry (clears the route of this question), Reset (clears the whole board), Back and Next in the same places "
        "on every card. Read-outs: a counter stations between that updates with every circle or capsule passed, "
        "not counting the two ends, a changes count and the list of change stations on the route card, and a card "
        "number out of 7.",
        ["The video's strip with Hauz Khas, where the Yellow Line and the Magenta Line "
         "meet. Find the capsule on the map. Which two lines meet there?",
         "Match the key symbols to their names, ride the Blue Line and the Pink Line and read "
         "the counter, tap a crossing of two lines that has no capsule, and ride a line past a capsule that counts "
         "as one station.",
         "The book's own metro questions: what the coloured lines represent, marking the Qutb "
         "Minar and Supreme Court stations, tracing different routes between them, Lali's suggestion, the route "
         "with the fewest stations, and the best way to the zoo."],
        ["Card 1: match the key. Drag the names to the symbols: a plain circle and a capsule with two "
         "coloured dots. Answer: the plain circle is a Metro Station and the capsule with two coloured dots is an "
         "Interchange Line.",
         "Card 2 (practice values): ride the Blue Line from Mayur Vihar to Botanical Garden and read the "
         "counter. Answer: 5 stations between, not counting Mayur Vihar and Botanical Garden.",
         "Card 3 (practice values): ride the Pink Line from INA to Mayur Vihar and read the counter. Answer: "
         "5 stations between. The capsule where the Pink Line meets the Violet Line counts as one of the 5.",
         "Card 4: tap the place where the Airport Express Line crosses the Magenta Line. Can you change "
         "lines there? Answer: no. There is no capsule, so the lines only cross. You can change lines only at a "
         "capsule that shows both colours.",
         "Card 5 (practice values): ride the Yellow Line from Hauz Khas to Central Secretariat. The capsule "
         "at INA counts as one station. How many stations are between? Answer: 2 + 1 + 3 = 6 stations between.",
         "Challenge: 'What do the different coloured lines represent?' and 'Mark the Qutb Minar station on "
         "the Yellow Line and the Supreme Court station on the Blue Line.' Build the first answer from the cards and "
         "mark the two stations with rings. Answer: each coloured line is a different metro route; Qutb Minar is the "
         "labelled circle on the lower part of the Yellow Line, next to Saket, and Supreme Court is the labelled "
         "circle on the Blue Line, the third station after Rajiv Chowk.",
         "Challenge: (a) 'Look at the metro map and trace different routes from the Qutb Minar metro station "
         "to the Supreme Court metro station.' (b) 'Lali says, \"We can take the Yellow Line and change the metro at "
         "Hauz Khas to take the Magenta Line.\" If the children follow Lali's suggestion, at which station(s) do "
         "they need to change the metro line again to reach the Supreme Court metro station?' (c) 'Which route has "
         "the least number of stations between Qutb Minar and Supreme Court?' (d) 'Which metro route(s), do you "
         "think, is/are the best way to reach the zoo from Qutb Minar?' Answers: (a) Sample answer: Route A, the "
         "Yellow Line to Rajiv Chowk and then the Blue Line, 14 stations between and 1 change; Route B, the Yellow "
         "Line to INA, the Pink Line to Mayur Vihar and then the Blue Line, 15 stations between and 2 changes; "
         "Route C, the Yellow Line to Hauz Khas, the Magenta Line to Botanical Garden and then the Blue Line, 25 "
         "stations between and 2 changes. (b) Botanical Garden, where the Magenta Line meets the Blue Line. (c) "
         "Route A, with 14 stations between. (d) Sample answer: Route A, because it has the fewest stations (14) and "
         "only one change, at Rajiv Chowk. Your answer may differ."],
        ["Each ride highlights the part of the line in its own colour and the counter updates at once, for example: "
         "Between Mayur Vihar and Botanical Garden there are 5 stations, not counting the two ends.",
         "A tap on a capsule shows its two colours and offers the change, for example: Hauz Khas shows yellow and "
         "magenta, so you can change from the Yellow Line to the Magenta Line here.",
         "A tap on a crossing without a capsule gives a soft amber note: You can change lines only where the capsule "
         "shows both colours. Here the lines only cross.",
         "A route that stops before the end station says where it stopped, for example: This route stops at Hauz "
         "Khas. Keep riding until you reach Supreme Court.",
         "A count that includes the two ends shows a clue, for example: Do not count the first and the last "
         "station. Count only the circles between them.",
         "Open questions, the routes and the best way, are never marked wrong when every change is at a capsule that "
         "shows both colours: the tool says Your answer may differ and offers Next."],
        "The key symbols are matched, the counter has been read on two lines, the crossing without a capsule has been "
        "tested, the two stations are marked, at least two routes are traced from Qutb Minar to Supreme Court with "
        "their stations between counted, and the questions about Lali's suggestion, the fewest stations and the best "
        "way are answered.",
        ["startStation", "endStation", "routeLegs", "changes", "stationsBetween", "keyMatches", "savedRoutes",
         "answerCards", "challengeIndex"],
        ["M_COUNT_ENDS", "M_CROSS_CHANGE"],
        ["Which line are you on? Look at the colour of the highlight and at the route card.",
         "Where does your line meet the next line? A capsule shows two coloured dots. You can change lines only at a "
         "capsule that shows both colours.",
         "Count the circles between the two ends, not the ends. A capsule counts as one station. Watch the counter "
         "as you ride.",
         "The tool highlights the route for you and reads the count of stations between. Then it gives you a similar "
         "route to try yourself."]),
}
