# -*- coding: utf-8 -*-
"""Topics T3 to T5 (module M2: Street Maps, Metro Maps and Keys): Reading a Street Map (with the bus route questions),
Reading a Metro Map (with the metro questions), and Making a Map with a Key (the Let Us Do school map).
Every teaching concept has one worked example with the plan's own numbers; every book question is an FIO item of its
topic's DOER, in the book's order. The street map and the metro map are the book's pictures: the figure sentences below
say what each picture holds, read from the page images."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# What the street map holds (read from the page image; N at the top). Used by every question card of T3.
STREET_MAP = (
    "The street map seen from above, with a compass card beside it (N at the top, E in red on the right, S at the "
    "bottom, W on the left). Hospital Road runs along the top with the Hospital above it and the stop sign S1 at the "
    "hospital gate. Park Road runs down the right side, with the Children's Park at the top right and Prem's House and "
    "Raju's House below the park on its east side. In the middle, below Hospital Road, are Tinku's House and Golu's "
    "House, then a block with a pond and Jaideep's House, then the Basketball Court, then Market Road, then the "
    "Shopping Centre with the stop sign S2 beside it, and the PARKING area at the bottom. On the left are Lali's House "
    "and Rohan's House at the top, Ravi's House in the middle and a green space with trees below. A red dotted route "
    "with arrows runs from the PARKING area north up the left main road, east along Hospital Road, south down Park "
    "Road and west along the road below the Shopping Centre.")

# What the metro map holds (read from the page image).
METRO_MAP = (
    "The Delhi metro map with the heading Delhi Metro Map and a key panel at the bottom right. The key lists 1 Red "
    "Line, 2 Yellow Line, 3 Blue Line, 4 Airport Express Line (orange), 5 Green Line, 6 Violet Line, 7 Pink Line, 8 "
    "Magenta Line, 9 Metro Station (a plain circle) and 10 Interchange Line (a capsule with two coloured dots). "
    "Stations are circles along the coloured lines and interchanges are capsules. The Yellow Line runs from Millenium "
    "City Centre Gurugram at the bottom left through Chattarpur, Qutb Minar, Saket, Hauz Khas, INA, Central "
    "Secretariat, Rajiv Chowk and New Delhi Stn. up to Kashmeri Gate. The Blue Line runs from Dwarka Sec 21 at the "
    "bottom left through Janakpuri West, Rajouri Garden, Kriti Nagar, Rajiv Chowk, Supreme Court and Yamuna Bank, then "
    "splits towards Vaishali and, through Mayur Vihar and Botanical Garden, to Noida City Centre. The Magenta Line "
    "runs from Janakpuri West through Hauz Khas and Kalkaji Mandir to Botanical Garden. The Violet Line runs from "
    "Central Secretariat to Kalkaji Mandir and Badarpur. The Pink Line runs round the middle of the map from the top "
    "left through INA to Mayur Vihar.")

# ============================== T3 Reading a Street Map (M2) =================================================
TOPICS.append(TOPIC(
    "T3", "M2", "Reading a Street Map", ["Zoo Trip", "Bus Route"], "Apply",
    "Students read a street map with its compass, say the direction a bus drives after each right or left turn, name "
    "the roads and stops on its route, and find houses and stops from the map.",
    "A street map is a picture of roads and places seen from above, and its compass shows which way is north. A right "
    "turn changes north to east, east to south, south to west and west to north. A left turn changes the direction "
    "the other way round.",
    [A("T3.C1", "Reading a Street Map", "Understand",
       "Students read a street map from above, use the compass to say which place is north, south, east or west of "
       "another place, and follow a dotted route along named roads.",
       textbook=["Children! Be ready at your nearby bus stop by 8:00 a.m. The school bus will take you to the Qutb "
                 "Minar in Delhi. After that, we will visit the zoo by a metro train.",
                 "The street map shows the bus route with dotted lines. The bus will pick up children from Stop 1 and "
                 "Stop 2 marked on the map.",
                 "Observe the map carefully and help the children board the bus."],
       teach=["Predict first: you stand at the Basketball Court on the street map and walk down the map, across "
              "Market Road. Which place do you reach first?",
              "You reach the Shopping Centre. The compass beside the map has S at the bottom, so down the map is "
              "south. The Shopping Centre is south of the Basketball Court.",
              "A street map is a picture of roads and places seen from above. Roads have names, like Hospital Road, "
              "Market Road and Park Road.",
              "The school bus will take the children to the Qutb Minar in Delhi, and then they will go to the zoo by "
              "a metro train. The bus picks up children from Stop 1 (S1) and Stop 2 (S2), marked on the map.",
              "The compass shows the directions on the map. N is at the top, E in red is on the right, S is at the "
              "bottom and W is on the left.",
              "The red dotted line is the route of the bus. Follow it with your finger and read the name of each "
              "road it uses.",
              "Look at the map and talk about it. Which places are near each other? Which way is one place from "
              "another? Ask your own questions by looking at the map.",
              "Rule: on a street map up is north, down is south, right is east and left is west, and the dotted "
              "line shows the route."],
       examples=[WE("What is just south of the Basketball Court, across Market Road, and what is just north of it?",
                    ["A street map is a picture of roads and places seen from above. The compass has N at the top, E "
                     "on the right, S at the bottom and W on the left.",
                     "Find the Basketball Court in the middle of the map. Market Road runs along the bottom of the "
                     "court.",
                     "Go down the map, across Market Road. Down the map is south, so the place just south of the "
                     "Basketball Court is the Shopping Centre.",
                     "Now go up the map from the court, across the small road above it. Up the map is north, so just "
                     "north of the court is the block with the pond and Jaideep's House.",
                     "Turn it round. If the Shopping Centre is south of the court, then the court is north of the "
                     "Shopping Centre.",
                     "Check with the compass: up is N, so north is up the map and south is down the map."],
                    "The Shopping Centre is just south of the Basketball Court. The block with the pond and "
                    "Jaideep's House is just north of it.")],
       ncert=["trip.story", "note.street"],
       key_terms=["street map", "compass", "route", "road", "stop"],
       misconceptions=["M_SAME_DIRECTION"], minutes=5),
     A("T3.C2", "Turning Right and Left on a Route", "Apply",
       "Students say the direction a bus or a cycle is driving after each right turn or left turn, starting from "
       "north, east, south or west, and name the road it turns onto.",
       teach=["Predict first: a bus is driving north and takes a right turn. Which direction is it driving now: east, "
              "south or west?",
              "East. A turn says which hand you turn towards. A direction says where you are going. They are two "
              "different things.",
              "Face north and hold out your arms. Your right hand points east and your left hand points west. A "
              "right turn takes you towards your right hand.",
              "A right turn changes north to east, east to south, south to west and west to north.",
              "A left turn changes the direction the other way round: north to west, west to south, south to east and "
              "east to north.",
              "A right turn does not always make a bus drive east. A bus that is driving east and turns right drives "
              "south.",
              "To read a route, say two things at every turn: right or left, and the direction after the turn.",
              "Rule: a right turn takes the direction through north, east, south, west in that order. A left turn "
              "takes it through north, west, south, east."],
       examples=[WE("A cycle drives north along a road and turns left at a junction. Which direction is it driving "
                    "after the turn? At the next junction it turns left again. Which direction is it driving now?",
                    ["The cycle drives north. Face north: your left hand points west and your right hand points "
                     "east.",
                     "A left turn is a turn towards the left hand. The left hand points west, so after the first "
                     "turn the cycle drives west.",
                     "Now the cycle drives west. Face west: your left hand points south.",
                     "The second left turn is towards south, so the cycle now drives south.",
                     "Check with the rule: a left turn takes north to west, and west to south.",
                     "The two left turns together made the cycle drive the opposite way to the way it started: it "
                     "started north and now drives south."],
                    "After the first left turn the cycle drives west. After the second left turn it drives south")],
       key_terms=["turn right", "turn left", "direction", "route"],
       misconceptions=["M_RIGHT_EAST"], minutes=5),
     DOER("T3.C3", "Practice: Bus Route Driver", "bus_route", "Apply",
          "Students name the roads, turns and directions of the bus route on the street map, and find houses and "
          "stops by reading the map and the compass.",
          ["A street map is a picture of roads and places seen from above. N is at the top of the compass.",
           "A right turn changes north to east, east to south, south to west and west to north.",
           "A left turn changes north to west, west to south, south to east and east to north.",
           "Say a direction with north, east, south or west, and a turn with right or left."],
          items=[FIO("bus.s1", "Bus Route: Stop 1",
                     "The bus will start from the parking area. It will go north and then it will take a right turn "
                     "onto ___ Road driving in the ___ direction to reach Stop 1 (S1).",
                     ["Find the PARKING area at the bottom of the map. The red dotted route goes up the map from "
                      "there, and up the map is north.",
                      "Near the top of the map the route meets the road with the Hospital above it. The name on that "
                      "road is Hospital Road.",
                      "The bus drives north and takes a right turn. A right turn changes north to east, so the bus "
                      "drives east along Hospital Road.",
                      "Stop 1 is at the hospital gate on Hospital Road, so the bus reaches Stop 1 driving "
                      "east.",
                      "Check: the red arrows on Hospital Road point to the right, and the compass has E on the "
                      "right."],
                     "The blanks are Hospital and east. The bus turns right onto Hospital Road driving east.",
                     kind="prompt",
                     q_figure=STREET_MAP,
                     s_figure="The same street map with the red dotted route from the PARKING area north to Hospital "
                              "Road, a right turn arrow onto Hospital Road, and the words Hospital Road and east "
                              "written beside the route near S1."),
                 FIO("bus.s2", "Bus Route: Stop 2",
                     "To reach Stop 2 (S2), it will turn ___ (right/left) onto ___ Road driving in the ___ "
                     "direction.",
                     ["The bus is driving east on Hospital Road. It goes on east until it meets the road down the "
                      "right side of the map. That road is Park Road.",
                      "The route now goes down the map. Down the map is south.",
                      "The bus changes from driving east to driving south. A right turn changes east to south, so "
                      "the turn is a right turn.",
                      "Stop 2 is beside the Shopping Centre, near the south end of Park Road, so the bus "
                      "reaches Stop 2 driving south.",
                      "Check: facing east, your right hand points south."],
                     "The blanks are right, Park and south. The bus turns right onto Park Road driving south.",
                     kind="prompt",
                     q_figure=STREET_MAP,
                     s_figure="The same street map with the red dotted route turning right at Park Road and driving "
                              "south to S2, and the words right, Park Road and south written beside the turn."),
                 FIO("bus.a", "Street Map: east of Jaideep's house",
                     "Whose houses are situated to the east of Jaideep's house? ___",
                     ["Find Jaideep's House in the middle of the map, below Tinku's House and Golu's House.",
                      "East is to the right of Jaideep's House. Look across Park Road, the road down the right "
                      "side.",
                      "On the east side of Park Road are two houses near the height of Jaideep's House: Prem's House "
                      "a little higher and Raju's House a little lower.",
                      "Check with the compass: E is on the right, and Prem's House and Raju's House are the houses "
                      "to the right of Park Road."],
                     "Prem's house and Raju's house.",
                     kind="prompt",
                     q_figure=STREET_MAP,
                     s_figure="The same street map with Jaideep's House ringed in teal, Prem's House and Raju's "
                              "House ringed in orange, and an arrow from Jaideep's House pointing east across Park "
                              "Road."),
                 FIO("bus.b", "Street Map: Ravi's house to the park",
                     "Mark the route from Ravi's house to the children's park.",
                     ["Find Ravi's House on the left side of the map and the Children's Park at the top right. The "
                      "gate of Ravi's House opens to the south, onto a small road.",
                      "Go south out of the gate to the small road, then turn left and go east along it to the main "
                      "road on the left.",
                      "Turn left and go north up the main road, all the way to Hospital Road.",
                      "Turn right and go east along Hospital Road to Park Road. The Children's Park is on the east "
                      "side of Park Road, at the top right.",
                      "Check: every part of the route is on a road, and it ends at the Children's Park.",
                      "Your answer may differ: other routes along the roads are right too."],
                     "Sample answer: south to the small road, east to the main road, north to Hospital Road, east to "
                     "Park Road and the park. Your answer may differ.",
                     kind="prompt",
                     q_figure=STREET_MAP,
                     s_figure="The same street map with a sample route in orange from Ravi's House south to the small "
                              "road, east to the left main road, north to Hospital Road and east to Park Road and the "
                              "Children's Park."),
                 FIO("bus.c", "Street Map: the stop closer to Lali's house",
                     "Which stop is closer to Lali's house? ___",
                     ["Find Lali's House at the top left of the map.",
                      "Find the two stops. Stop 1 is at the hospital gate on Hospital Road, near the top of the "
                      "map. Stop 2 is beside the Shopping Centre, near the bottom right.",
                      "From Lali's House, Stop 1 is a short way along Hospital Road to the east. Stop 2 is a long "
                      "way, down the map and over to the right.",
                      "No distances are printed on the map, so we judge from the picture. Stop 1 is closer.",
                      "Check: Stop 1 is at about the same height as Lali's House, near the top, and Stop 2 is at "
                      "the bottom."],
                     "Stop 1.",
                     kind="prompt",
                     q_figure=STREET_MAP,
                     s_figure="The same street map with Lali's House, S1 and S2 marked, a short orange line from "
                              "Lali's House to S1 and a longer grey line from Lali's House to S2."),
                 FIO("bus.d", "Street Map: Golu runs late",
                     "Golu is running late. Trace the route to help him reach the nearest bus stop.",
                     ["Find Golu's House just below Hospital Road. Stop 1 is at the hospital gate, close above it. "
                      "Stop 2 is far away at the bottom right. The nearest stop is Stop 1.",
                      "The gate of Golu's House opens to the south, onto the road below the house. Go south out of "
                      "the gate to that road.",
                      "Turn left and go east along the road to Park Road.",
                      "Turn left and go north up Park Road to Hospital Road.",
                      "Turn left and go west along Hospital Road to the hospital gate, where Stop 1 stands.",
                      "Check: the route stays on the roads and ends at Stop 1. The way along the left main road is "
                      "longer.",
                      "Your answer may differ: other routes along the roads to Stop 1 are right too."],
                     "Sample answer: south to the road below, east to Park Road, north to Hospital Road, west to "
                     "Stop 1. Your answer may differ.",
                     kind="prompt",
                     q_figure=STREET_MAP,
                     s_figure="The same street map with a sample route in orange from Golu's House south to the road "
                              "below it, east to Park Road, north to Hospital Road and west to S1."),
                 FIO("bus.e", "Street Map: Prem to Stop 2",
                     "In which direction would Prem have to move to reach Stop 2?",
                     ["Find Prem's House on the east side of Park Road, on the right of the map.",
                      "Find Stop 2 beside the Shopping Centre, near the bottom of the map.",
                      "Stop 2 is below Prem's House, so Prem has to move down the map. Down the map is south.",
                      "Stop 2 is also a little to the left of Prem's House, but this chapter uses only the four "
                      "directions, so the nearest direction is south.",
                      "Check with the compass: S is at the bottom, and Stop 2 is at the bottom of the map."],
                     "South. Stop 2 is below Prem's house.",
                     kind="prompt",
                     q_figure=STREET_MAP,
                     s_figure="The same street map with an orange arrow from Prem's House pointing down the map to "
                              "S2 and the word south beside it.")],
          misconceptions=["M_RIGHT_EAST", "M_SAME_DIRECTION"])],
    key_terms=["street map", "compass", "route", "turn right", "turn left"]))

# ============================== T4 Reading a Metro Map (M2) ==================================================
TOPICS.append(TOPIC(
    "T4", "M2", "Reading a Metro Map", ["Delhi Metro Train Stations", "Metro routes"], "Apply",
    "Students read the key of a metro map, follow a coloured line, change lines only at an interchange capsule, and "
    "count the stations between two stations without counting the two ends.",
    "A metro map shows coloured lines for routes, circles for stations and capsules for interchanges. You can change "
    "lines only at a capsule. The stations between two stations are the circles strictly between them, and a capsule "
    "counts as one station.",
    [A("T4.C1", "Reading a Metro Map: Lines, Stations and Key", "Understand",
       "Students read the key of a metro map, name what the coloured lines, the circle and the capsule mean, and find "
       "the stations where two lines meet.",
       textbook=["Children will get off the bus at the Qutb Minar metro station. To reach the zoo, they need to get "
                 "off the metro at the Supreme Court metro station.",
                 "Here is the metro map for your reference.",
                 "Read the key to the symbols and identify them on the map."],
       teach=["Predict first: at Hauz Khas the map does not show a plain circle but a capsule with a yellow dot and a "
              "magenta dot. What do you think the two dots tell you?",
              "The two dots tell you that two lines meet at that station, the Yellow Line and the Magenta Line. Here "
              "you can change from one line to the other.",
              "Read the key. It numbers 10 symbols. Symbols 1 to 8 are the coloured lines: Red, Yellow, Blue, Airport "
              "Express, Green, Violet, Pink and Magenta.",
              "Symbol 9, a plain circle, is a Metro Station. Symbol 10, a capsule with two coloured dots, is an "
              "Interchange Line, a place where two lines meet.",
              "Each coloured line is a different metro route. The colours make it easier to find and follow a route "
              "on the map.",
              "Observe the map carefully. The children get off the bus at the Qutb Minar metro station, and to reach "
              "the zoo they get off the metro at the Supreme Court metro station. Find both names on the map.",
              "Rule: a coloured line is one metro route, a circle is a metro station, and a capsule with two coloured "
              "dots is an interchange where those two lines meet."],
       examples=[WE("On the metro map, look at Hauz Khas. Which two lines meet there, and how do you know you can "
                    "change lines there?",
                    ["Find Hauz Khas in the lower middle of the metro map. Its symbol is not a plain circle. It "
                     "is a capsule with two coloured dots.",
                     "The two dots are yellow and magenta. In the key, the yellow colour is the Yellow Line and the "
                     "magenta colour is the Magenta Line.",
                     "Now read the key. Symbol 9, a plain circle, is a Metro Station. Symbol 10, a capsule with two "
                     "coloured dots, is an Interchange Line.",
                     "So Hauz Khas is an interchange. The Yellow Line and the Magenta Line meet there, and you can "
                     "change from one line to the other.",
                     "Check: the capsule has two dots, one dot for each line that meets there."],
                    "The Yellow Line and the Magenta Line meet at Hauz Khas. Its symbol is the interchange capsule "
                    "from the key, so you can change lines there")],
       ncert=["metro.intro", "metro.key", "note.metro"],
       key_terms=["metro map", "line", "station", "interchange", "key"],
       misconceptions=["M_CROSS_CHANGE"], minutes=6),
     A("T4.C2", "Changing Lines and Counting Stations", "Apply",
       "Students count the stations between two stations on a metro map, count an interchange capsule as one "
       "station, and change lines only at a capsule where the two lines meet.",
       teach=["Predict first: you ride from Hauz Khas to Kalkaji Mandir and on to Badarpur. When you count the "
              "stations between, do you count Hauz Khas and Badarpur?",
              "No. The stations between are only the ones strictly between the two ends. Hauz Khas and Badarpur are "
              "the ends, so we do not count them.",
              "Count every station between the two ends, one by one. A capsule is a station too, so it counts as "
              "one, whether you change there or ride past it.",
              "To change lines, get off at a capsule that shows the colours of both lines. At Kalkaji Mandir the "
              "capsule has a magenta dot and a violet dot, so you can change from the Magenta Line to the Violet Line "
              "there.",
              "Two lines can cross on the map without a capsule. Then there is no interchange, and you cannot change "
              "lines at that crossing.",
              "To count a route with a change, count the stations on the first line, then the capsule where you "
              "change, then the stations on the next line.",
              "Rule: count the circles between the two ends, count a capsule as one station, do not count the two "
              "ends, and change lines only at a capsule."],
       examples=[WE("Ride the Magenta Line from Hauz Khas to Kalkaji Mandir, change to the Violet Line and ride on to "
                    "Badarpur. How many stations are between Hauz Khas and Kalkaji Mandir, and between Kalkaji Mandir "
                    "and Badarpur?",
                    ["Start at Hauz Khas and ride along the Magenta Line towards Kalkaji Mandir. Count only the "
                     "circles between the two stations, not the two ends.",
                     "There are 4 circles between Hauz Khas and Kalkaji Mandir, so 4 stations between them.",
                     "Kalkaji Mandir is a capsule with a magenta dot and a violet dot. The Magenta Line and the "
                     "Violet Line meet there, so we change lines at Kalkaji Mandir.",
                     "Now ride along the Violet Line towards Badarpur. There are 6 circles between Kalkaji Mandir "
                     "and Badarpur, so 6 stations between them.",
                     "In all, between Hauz Khas and Badarpur there are 4 stations, then Kalkaji Mandir, then 6 "
                     "stations: 4 + 1 + 6 = 11 stations.",
                     "Check: the capsule counts as one station, and we did not count Hauz Khas or Badarpur, the two "
                     "ends."],
                    "There are 4 stations between Hauz Khas and Kalkaji Mandir, and 6 between Kalkaji Mandir and "
                    "Badarpur. In all, 4 + 1 + 6 = 11 stations between Hauz Khas and Badarpur")],
       key_terms=["stations between", "change lines", "capsule", "counting"],
       misconceptions=["M_COUNT_ENDS", "M_CROSS_CHANGE"], minutes=6),
     DOER("T4.C3", "Practice: Metro Route Planner", "metro_planner", "Analyze",
          "Students trace routes on the metro map between two stations, mark stations on their lines, count the "
          "stations between, and say which route has the fewest stations and where to change lines.",
          ["A coloured line is one metro route. A circle is a station. A capsule with two coloured dots is an "
           "interchange.",
           "You can change lines only at a capsule that shows the colours of both lines.",
           "Count the circles between the two ends. A capsule counts as one station. Do not count the two ends.",
           "To compare routes, count the stations between for each route."],
          items=[FIO("metro.colours", "Metro Map: the coloured lines",
                     "What do the different coloured lines represent?",
                     ["Read the key at the bottom right of the map. Symbols 1 to 8 are coloured lines: Red, Yellow, "
                      "Blue, Airport Express, Green, Violet, Pink and Magenta.",
                      "Find each colour on the map. A coloured line passes through a row of circles, and each circle "
                      "is a metro station on that line.",
                      "Each coloured line is a different metro route. The colours make it easier to find and follow "
                      "a route.",
                      "Check: the key has 8 coloured lines, and the map has 8 colours of line."],
                     "Each coloured line is a different metro route: Red, Yellow, Blue, Airport Express, Green, "
                     "Violet, Pink and Magenta. The colour tells which route a station is on.",
                     kind="prompt",
                     q_figure=METRO_MAP,
                     s_figure="The metro key panel with the 8 coloured lines named, each with a short sample of its "
                              "own colour, and the same colours shown running through the map."),
                 FIO("metro.mark", "Metro Map: mark two stations",
                     "Mark the Qutb Minar station on the Yellow Line and the Supreme Court station on the Blue Line.",
                     ["Find the Yellow Line. It is the yellow line that runs from the bottom left up the middle of "
                      "the map.",
                      "Follow it up from the bottom left. The labelled circle Qutb Minar is on the lower part of the "
                      "Yellow Line, and the next station up the line is Saket. Mark Qutb Minar with a ring.",
                      "Find the Blue Line. Rajiv Chowk is a capsule where the Blue Line meets the Yellow Line. "
                      "Follow the Blue Line to the right of Rajiv Chowk.",
                      "The third station after Rajiv Chowk is Supreme Court, the labelled circle between Rajiv Chowk "
                      "and Yamuna Bank. Mark Supreme Court with a ring.",
                      "Check: Qutb Minar is on the Yellow Line, Supreme Court is on the Blue Line, and both names "
                      "are printed beside their circles."],
                     "Qutb Minar: the labelled circle on the lower part of the Yellow Line, next to Saket. Supreme "
                     "Court: the labelled circle on the Blue Line, third after Rajiv Chowk.",
                     kind="prompt",
                     q_figure=METRO_MAP,
                     s_figure="The metro map with the Qutb Minar circle on the Yellow Line and the Supreme Court "
                              "circle on the Blue Line each ringed in orange."),
                 FIO("metro.a", "Metro Routes: trace the routes",
                     "Look at the metro map and trace different routes from the Qutb Minar metro station to the "
                     "Supreme Court metro station.",
                     ["Start at Qutb Minar on the Yellow Line. Supreme Court is on the Blue Line, so every route must "
                      "change to the Blue Line. We can change only at a capsule.",
                      "Route A: ride the Yellow Line up to Rajiv Chowk, change to the Blue Line there, and ride to "
                      "Supreme Court. This route has one change.",
                      "Route B: ride the Yellow Line to INA, change to the Pink Line and ride to Mayur Vihar, then "
                      "change to the Blue Line and ride to Supreme Court. This route has two changes.",
                      "Route C: ride the Yellow Line to Hauz Khas, change to the Magenta Line and ride to Botanical "
                      "Garden, then change to the Blue Line and ride to Supreme Court. This route has two changes.",
                      "Check each change: Rajiv Chowk, INA, Mayur Vihar, Hauz Khas and Botanical Garden are all "
                      "capsules that show the colours of both lines.",
                      "Your answer may differ: other routes on the map are right too."],
                     "Sample answer: A, Yellow to Rajiv Chowk, then Blue. B, Yellow to INA, Pink to Mayur Vihar, then "
                     "Blue. C, Yellow to Hauz Khas, Magenta to Botanical Garden, then Blue.",
                     kind="prompt",
                     q_figure=METRO_MAP,
                     s_figure="The metro map with three routes in three colours: Route A in orange from Qutb Minar "
                              "along the Yellow Line to Rajiv Chowk and then along the Blue Line to Supreme Court, "
                              "Route B in teal along the Yellow Line to INA, the Pink Line to Mayur Vihar and the "
                              "Blue Line to Supreme Court, and Route C in green along the Yellow Line to Hauz Khas, "
                              "the Magenta Line to Botanical Garden and the Blue Line to Supreme Court, with each "
                              "change station ringed."),
                 FIO("metro.b", "Metro Routes: Lali's suggestion",
                     "Lali says, \"We can take the Yellow Line and change the metro at Hauz Khas to take the Magenta "
                     "Line.\" If the children follow Lali's suggestion, at which station(s) do they need to change "
                     "the metro line again to reach the Supreme Court metro station?",
                     ["Lali's plan: ride the Yellow Line from Qutb Minar to Hauz Khas and change there to the "
                      "Magenta Line.",
                      "Ride the Magenta Line to the right on the map. It passes Kalkaji Mandir, a capsule where the "
                      "Violet Line meets it, but the children stay on the Magenta Line, so they need no change "
                      "there.",
                      "The Magenta Line meets the Blue Line at the capsule Botanical Garden, which has a magenta dot "
                      "and a blue dot. They change there to the Blue Line.",
                      "Ride the Blue Line to Supreme Court. So the children change again at Botanical Garden.",
                      "The Magenta Line also runs the other way from Hauz Khas, to Janakpuri West, where it meets "
                      "the Blue Line. That way is much longer: 31 stations between instead of 25.",
                      "Check: Botanical Garden is a capsule that shows the colours of both lines, Magenta and Blue."],
                     "Botanical Garden, where the Magenta Line meets the Blue Line. The other way, at Janakpuri "
                     "West, is much longer.",
                     kind="prompt",
                     q_figure=METRO_MAP,
                     s_figure="The metro map with Lali's route in orange: the Yellow Line from Qutb Minar to Hauz "
                              "Khas, the Magenta Line to Botanical Garden and the Blue Line to Supreme Court, with "
                              "Hauz Khas and Botanical Garden ringed."),
                 FIO("metro.c", "Metro Routes: the fewest stations",
                     "Which route has the least number of stations between Qutb Minar and Supreme Court?",
                     ["Count the stations between Qutb Minar and Supreme Court on each route. A capsule where we "
                      "change counts as one station. Do not count Qutb Minar or Supreme Court.",
                      "Route A: count the circles on the Yellow Line from Qutb Minar to Hauz Khas (2), Hauz Khas "
                      "(1), then 2 to INA, INA (1), 3 to Central Secretariat, Central Secretariat (1), 1 to Rajiv "
                      "Chowk, Rajiv Chowk (1), then 2 on the Blue Line to Supreme Court. 2 + 1 + 2 + 1 + 3 + 1 + 1 "
                      "+ 1 + 2 = 14.",
                      "Route B: 5 stations from Qutb Minar to INA, INA (1), 5 on the Pink Line to Mayur Vihar, Mayur "
                      "Vihar (1), 1 to Yamuna Bank, Yamuna Bank (1), 1 to Supreme Court. 5 + 1 + 5 + 1 + 1 + 1 + 1 "
                      "= 15.",
                      "Route C: 3 stations from Qutb Minar to Hauz Khas, 4 on the Magenta Line to Kalkaji Mandir, "
                      "Kalkaji Mandir (1), 7 to Botanical Garden, Botanical Garden (1), 5 on the Blue Line to Mayur "
                      "Vihar, Mayur Vihar (1), 1 to Yamuna Bank, Yamuna Bank (1), 1 to Supreme Court. 3 + 4 + 1 + 7 "
                      "+ 1 + 5 + 1 + 1 + 1 + 1 = 25.",
                      "14 is less than 15, and 15 is less than 25, so Route A has the fewest stations between.",
                      "Check: Route A changes at Rajiv Chowk, the capsule where the Yellow Line meets the Blue Line, "
                      "so it stays on the Yellow Line the longest."],
                     "Route A: the Yellow Line to Rajiv Chowk, then the Blue Line. It has 14 stations between, fewer "
                     "than Route B (15) and Route C (25).",
                     kind="prompt",
                     q_figure=METRO_MAP,
                     s_figure="The metro map with Route A in orange and the count 14 stations between written beside "
                              "it, and Routes B and C faint with their counts 15 and 25."),
                 FIO("metro.d", "Metro Routes: the best way to the zoo",
                     "Which metro route(s), do you think, is/are the best way to reach the zoo from Qutb Minar? ___",
                     ["The best way is your own opinion, but give a reason from the map. Compare the routes by the "
                      "stations between and by the changes.",
                      "Route A has 14 stations between and 1 change, at Rajiv Chowk.",
                      "Route B has 15 stations between and 2 changes, at INA and Mayur Vihar.",
                      "Route C has 25 stations between and 2 changes, at Hauz Khas and Botanical Garden.",
                      "Route A has the fewest stations and the fewest changes, so it is a good choice.",
                      "Check: the reason uses numbers from the map, 14 stations and 1 change.",
                      "Your answer may differ: you may choose another route and give your own reason."],
                     "Sample answer: Route A, because it has the fewest stations (14) and only one change, at Rajiv "
                     "Chowk. Your answer may differ.",
                     kind="prompt",
                     q_figure=METRO_MAP,
                     s_figure="The metro map with Route A in orange, and its 14 stations between and its 1 change at "
                              "Rajiv Chowk written beside it.")],
          misconceptions=["M_COUNT_ENDS", "M_CROSS_CHANGE"])],
    key_terms=["metro map", "line", "station", "interchange", "key"]))

# ============================== T5 Making a Map with a Key (M2) ==============================================
TOPICS.append(TOPIC(
    "T5", "M2", "Making a Map with a Key", ["Let Us Do (a map of your school)"], "Apply",
    "Students make a map of a place with a key that explains each symbol, hide objects in it, mark them with red dots, "
    "and use a map and its key to find something hidden.",
    "A map uses symbols for the things in a place seen from above. The key explains what each symbol means, so every "
    "symbol on the map must be in the key. A hidden thing is marked with a red dot.",
    [A("T5.C1", "Making a Map with a Key", "Understand",
       "Students make a map of a place seen from above, draw a key that explains each symbol, and mark a hidden thing "
       "with a red dot.",
       textbook=["A sample map and its key are given below.",
                 "Gate, Road, Building, Tank, Hidden Objects, Wall, Fence, Seat/Bench, Path, Garden, Tree"],
       teach=["Predict first: your friend sees a long rectangle on your map. How can your friend know that it means a "
              "shelf and not a table?",
              "Your friend needs a key. A key is a box on the map that shows each symbol and says what it means.",
              "A map uses symbols, small simple drawings, for the things in a place seen from above. Look at the "
              "sample map in your maths book. Its key shows symbols for Gate, Road, Building, Tank, Hidden Objects, "
              "Wall, Fence, Seat or Bench, Path, Garden and Tree.",
              "The key of the sample map shows a red circle for Hidden Objects, a thick hatched line for a Wall and a "
              "line with small ticks for a Fence.",
              "To make your own map, first draw the place from above. Then choose one symbol for each kind of thing, "
              "and write each symbol in the key with its name.",
              "To hide something, choose a place on the map and mark it with a red dot. Then give your friend a clue "
              "that uses directions, like: start at the door and walk north.",
              "Rule: every symbol on a map is explained in the key, and a hidden thing is marked with a red dot."],
       examples=[WE("Make a map of a library corner seen from above: 2 shelves on the west wall, 1 table with 4 chairs "
                    "in the middle, and the door on the south wall. Make a key, and hide a bookmark with a red dot.",
                    ["Draw the floor of the corner from above as a large rectangle. With N at the top, the west wall "
                     "is the left side and the south wall is the bottom side.",
                     "Draw 2 long rectangles along the west wall, one for each shelf. A long rectangle is the symbol "
                     "for a shelf.",
                     "Draw 1 square in the middle for the table and 4 small squares around it for the 4 chairs.",
                     "Draw a gap in the south wall for the door.",
                     "Hide the bookmark under the table and mark it with a red dot.",
                     "Make the key. A long rectangle means shelf. A square with 4 small squares around it means "
                     "table and chairs. A gap in the wall means door. A red dot means the hidden bookmark.",
                     "Read the map to find the bookmark: start at the door on the south wall, walk north to the "
                     "table, and look under it.",
                     "Check: every symbol on the map is in the key, and there is 1 red dot."],
                    "The map has 2 shelves, a table with 4 chairs and a door, a key that explains each symbol, and a "
                    "red dot under the table. From the door, walk north to the table to find the bookmark")],
       ncert=["school.sample"],
       key_terms=["map", "key", "symbol", "hidden object"],
       minutes=5),
     DOER("T5.C2", "Pull it together and do it: Our School Map", None, "Apply",
          "Students make a map of their school with a key for every symbol, hide objects and mark them with red "
          "dots, and write a clue that tells a friend how to find one.",
          ["A map is a picture of a place seen from above. It uses symbols for the things in the place.",
           "The key tells what each symbol means. Every symbol on the map must be in the key.",
           "Mark a hidden thing with a red dot or a red flag.",
           "Give a clue with directions: start at the gate and walk east to the tree."],
          items=[FIO("LUD.school", "Let Us Do: a map of your school",
                     "Make a map showing the different places in your school. Make a key for the symbols used in the "
                     "map. Hide some objects in these places. Mark the positions where things are hidden with red "
                     "dots or flags. Now, challenge your friends to find the hidden things by reading the map.",
                     ["Choose the places to show. In this sample school there is a gate in the west wall, a road "
                      "along the west side, a building on the east side, a tree and a bench near the middle, and a "
                      "garden near the south wall on the west side.",
                      "Draw the school from above with N at the top, and draw one symbol for each kind of place. "
                      "For example a rectangle with two squares for the building, a long rectangle for the bench, a "
                      "cloud shape for the tree.",
                      "Make the key: a small box that shows each symbol with its name, gate, road, building, tree, "
                      "seat or bench, garden, and the red dot for a hidden object.",
                      "Hide 3 objects: one beside the bench, one beside the tree and one in the garden. Mark each "
                      "place with a red dot.",
                      "Write a challenge for a friend: start at the gate and walk east to the tree. The hidden "
                      "object is a little south of the tree.",
                      "Check: every symbol on the map is in the key, there are 3 red dots, and the clue uses only "
                      "north, east, south and west.",
                      "Your map will be different: use your own school, your own symbols and your own clue."],
                     "Sample answer: a map with a key and 3 red dots. Clue: start at the gate, walk east to the tree. "
                     "The object is a little south of it. Your map will be different.",
                     kind="exercise",
                     q_figure="A sketch map of a school seen from above on a cream card. A wall and a fence enclose "
                              "a yard, and a gate in the west side opens onto a road that runs down the west side. A "
                              "dotted path loops round the yard. Inside are a bench near the top, a tree inside a "
                              "small fenced square, a garden in the bottom left corner, a tank, and three buildings in a "
                              "column on the east side. Five red circles mark hidden objects. Two key panels list "
                              "Gate, Road, Building, Tank and Hidden Objects on the left, and Wall, Fence, Seat or "
                              "Bench, Path, Garden and Tree on the right.",
                     s_figure="A sample school map from above with N at the top: the gate in the west wall, a road "
                              "along the west side, a building on the east side, a tree and a bench near the "
                              "middle, a garden near the south wall on the west side, three red dots (beside the bench, beside the tree "
                              "and in the garden), and a key box that lists gate, road, building, tree, seat or "
                              "bench, garden, and red dot for a hidden object.")])],
    key_terms=["map", "key", "symbol", "hidden object"]))
