# -*- coding: utf-8 -*-
"""Class 5 Chapter 14, Maps and Locations: long-form tool descriptions in the master prompt's format (17 Nov 2026).
Two dicts keyed by the tool's media id: DESCRIPTIONS (the full text) and OBJECTIVES (one plain sentence each)."""

DESCRIPTIONS = {}
OBJECTIVES = {}

# ---------------------------------------------------------------------------------------------------------------
DESCRIPTIONS["M1.S1.T1.C2.2D1"] = """
A. TOOL TITLE
- Face the Rising Sun
B. TOOL INFO
- Tool ID: M1.S1.T1.C2.2D1
- Tool type: Exploration (the free first try, right after the story video)
- Textbook source: Maps and Locations, the opening activity: Manu facing the rising Sun, and the two questions repeated in Star Challenges 1 and 2. No numbers (developer only).
C. LEARNING OBJECTIVE
- The student finds east by turning to face the rising Sun, then names the directions of Manu's left hand, right hand and back from that one fact.
- Out of scope: reading a map, using a compass in the field, directions between the four, how birds find their way.
D. TOOL DESCRIPTION
1. Opening Screen
- A sunrise meadow seen from above (photo-style grass and sky). Manu, the boy of the opening story, stands at the centre of a round grass field, facing the top, both arms stretched out. At the right edge a bright Sun disc sits low over blue hills, its rays lying across the grass: the Sun is on Manu's right.
- Instruction line: "Turn Manu to face the rising Sun."
- The child is invited to tap one of the two big round turn arrows beside Manu's feet.
2. Scene and Objects
- Manu: a flat drawing seen from above and a little behind (round head, black hair, cream shirt, arms out, small shoes at the front), about 15 percent of the stage height. He turns on the spot, a quarter turn in half a second.
- The Sun: a flat glowing disc that never moves. Its caption (Activities 1 and 2 only) reads "The Sun is: on his right", then "in front of Manu", "behind him" or "on his left" after each turn.
- Arrows (from Activity 2): short arrows grow from Manu's chest (front), each hand and behind him, each ending in an empty dashed circle, a tag slot. They turn with Manu.
- Tag tray along the bottom: "North", "East", "South", "West". Two big round buttons, "Turn left" and "Turn right", with curved arrows, beside Manu's feet.
- Compass card (N top, E in red right, S bottom, W left): hidden until Activity 6, then in the top right corner. Before that the stage shows no direction letters (top is north, right east, bottom south, left west).
- One goal chip at the top shows the current goal.
3. Main Interaction
- Tap a turn arrow (or drag Manu round, snapping to a quarter): one quarter turn per tap. Tap a tag then a slot (or drag it); tap a tag in a slot to return it; one tag per slot.
- Any turn returns all tags to the tray, because the slots turn with Manu: "Manu turned, so his hands now point to other directions. Tag them again."
- Bottom buttons: "Hint", "Reset" and the main button "Check", which becomes "Next" when the goal chip is green. Reset restarts the activity.
4. Activities
- Activity 1 (guided). Goal line: "Turn Manu to face the rising Sun." Goal chip: "Face the Sun". Setup: Manu faces the top, the Sun is on his right, caption on, no arrows. Guess: the child taps the turn arrow they think brings the Sun in front of him, right or left; this tap is the guess. Result: after "Turn right" the rays brighten and the chip turns green with a bounce. Why line: "One quarter turn to the right, and the Sun is in front of Manu. He is facing the rising Sun." If the child turned left first, they keep turning until the Sun is in front; the line is then "Manu is facing the rising Sun." Help: guided, the caption changes after every turn.
- Activity 2 (guided). Goal line: "Which direction is in front of Manu?" Goal chip: "Front: ?", then "Front: East". Setup: Manu faces the Sun; only the front arrow and slot show; caption "in front of Manu". Guess: the child places a tag in the front slot and presses Check. Result: East turns green and bounces. Why line: "The Sun rises in the east, so the direction in front of Manu is east." Help: guided, a dotted ray joins the Sun and the front slot.
- Activity 3 (guided). Goal line: "Tag Manu's left hand and right hand." Goal chip: "Hands: ? ?". Setup: East stays in front; the hand arrows grow, labelled "left hand" and "right hand". Guess: the child is invited to face the Sun and stretch out their own left arm, then places two tags and presses Check. Result: North on the left hand and South on the right hand turn green. Why line: "Facing east, his left hand points north and his right hand points south." Help: guided, labels printed.
- Activity 4 (independent). Goal line: "Which direction is behind Manu?" Goal chip: "Behind: ?". Setup: East, North and South stand in their slots as plain grey words; the behind arrow grows; no labels, no caption. Guess: the child places a tag and presses Check. Result: West turns green. Why line: "West is behind Manu, opposite to east." Help: independent.
- Activity 5 (independent). Goal line: "Turn Manu to face north. Then tag his hands." Goal chip: "Face north". Setup: Manu faces the Sun, slots empty, no captions. Guess: the child taps Turn left or Turn right, the way they think Manu must turn to face north (his left hand pointed north in Activity 3). Result: after one quarter turn to the left the strip says "Manu faces north." and North fills the front slot; the child tags his right hand East and his left hand West. Why line: "Manu faces north, so his right hand points east, where the Sun is, and his left hand points west. A hand does not always point the same way." Help: independent.
- Activity 6 (independent). Goal line: "Match Manu to the compass card." Goal chip: "Match the card". Setup: Manu turns back to face the Sun by himself; the compass card opens in the corner with a small Manu at its centre and a short arrow from his chest. Guess: the child drags the arrow tip to the letter they think Manu faces. Result: the arrow snaps to E and the four tags show round the small Manu: East front, North left, South right, West behind. Why line: "Manu faces east, the right side of the card. North is at the top, on his left hand. South is at the bottom, on his right hand. West is on the left, behind him." Help: independent.
- Star Challenges: see section 7.
5. Mathematical Understanding
- Only the rising Sun is fixed. Facing it means facing east, so the left hand is north, the right hand south and the back west. Left and right turn with Manu; the four directions stay put.
- The rules to say at the end are the Remember lines of section 7.
6. Feedback and Hints
- Correct: the slot or chip turns green, the tag bounces gently, the strip shows the why line.
- Mistake: turns left in Activity 1 -> red strip, small shake: "The Sun is behind Manu now. Turn him the other way." The caption pulses.
- Mistake: a wrong front tag -> "Look at the Sun. It is straight in front of Manu. Which direction does the rising Sun come from?" After a second wrong tag: "The Sun rises in the east. Put the East tag in front of Manu."
- Mistake: West for the left hand (a hand always points west) -> "A hand does not always point west. Face the Sun yourself and stretch out your left arm. Which way does it point?" The left-hand arrow pulses. Hands swapped -> "You may have swapped the hands. Face the Sun yourself and stretch out your left arm first."
- Mistake: East behind Manu -> "East is in front of Manu. Behind him is the opposite way."
- Mistake: Activity 5, turns right (Manu faces south) -> "Manu faces south now. North is the way his left hand pointed when he faced the Sun. Turn him that way." A wrong tag for the right hand -> "The Sun has not moved: it is on Manu's right. Which direction is the Sun in?"
- Mistake: a wrong letter in Activity 6 -> "Manu faces the Sun, and the Sun is on the right of the stage. Which letter is on the right of the card?" Check with an empty slot -> "Put a tag in every empty circle first."
- Hint button, 3 levels: (1) words, for example "Where is the Sun? Turn Manu until the Sun is straight in front of him."; (2) visual: the Sun glows and a dotted ray joins it to Manu or to the slot to fill; (3) almost the answer: in Activity 1 the tool turns Manu one quarter turn right ("Now the Sun is in front of Manu. Press Check."); later "The Sun rises in the east. Facing east, your left arm points north and your right arm points south." and the first tag is placed.
- Edge cases: two turns put the Sun behind Manu; nothing can be dropped while Manu is turning.
7. Ending
- Star Challenge 1 (independent). Goal line, in the book's words: "Manu is facing the rising Sun. That direction is ___. His left hand is pointing in the ___ direction. His right hand is pointing in the ___ direction." Goal chip: "Fill the three blanks". Setup: Manu already faces the Sun; the three blanks are the front, left-hand and right-hand slots; no captions, no card. Guess: the child fills all three and presses Check. Success: East, North and South turn green. Why line: "Facing the Sun means facing east. His left hand points north and his right hand points south."
- Star Challenge 2 (independent). Goal line, in the book's words: "which way is west?" Goal chip: "Find west". Setup: the three green tags stay; the four arrow ends can be tapped. Guess: the child taps the arrow end they think points west. Success: the behind arrow takes the West tag with a bounce. Why line: "West is behind Manu, opposite to east." A tap on the front -> "That is east, where the Sun rises. West is the opposite way." A tap on a hand -> "That hand points north or south. West is opposite to east."
- End screen (confetti once): "Well done!" Remember: "Facing the rising Sun means facing east." "When you face east, your left hand points north, your right hand points south and west is behind you." "Left and right turn with you. North, east, south and west stay where they are." Think and talk: "If Manu turns his back on the rising Sun, which direction is he facing?" Button: "Start again".
8. Assets and Language
- Images: photo-style grass, sunrise sky and blue hills; the Sun disc (code glow); Manu as one flat drawing from above; tags, dashed circles, turn arrows and the compass card (code). English.
""".strip("\n")

OBJECTIVES["M1.S1.T1.C2.2D1"] = "The student understands that turning to face the rising Sun gives east, and that Manu's left hand, right hand and back then point north, south and west."

# ---------------------------------------------------------------------------------------------------------------
DESCRIPTIONS["M1.S4.T4.C11.2D1"] = """
A. TOOL TITLE
- Direction Clues
B. TOOL INFO
- Tool ID: M1.S4.T4.C11.2D1
- Tool type: Concept-activity
- Textbook source: Maps and Locations, Bird Watching (colour four tents by clues, draw a tent east of the lake) and Map of a Room (directions from the girl, your own room with a direction arrow, names in the four directions). No numbers (developer only).
C. LEARNING OBJECTIVE
- The student says the direction of one thing from another thing or from a person on a picture with a compass, and places things in a given direction.
- Out of scope: in-between directions, distances, routes.
D. TOOL DESCRIPTION
1. Opening Screen
- A school ground seen from above on a photo-style grass texture: a white flagpole at the centre; a library with a blue roof above it, a canteen with a red roof below it, a green cricket net to its left and a round blue water tank to its right, all the same distance away. The compass card is in the top right corner; a round compass cross waits in a tray at the bottom left.
- Instruction line: "Which thing is north of the flagpole? Make a guess."
- The child is invited to tap one of the four things.
2. Scene and Objects
- Compass card on every board: N top, E in red right, S bottom, W left.
- Compass cross: a round card (10 percent of the stage width) with two thin diagonal lines and a centre dot. Dropped on a thing it snaps there and four wedges tint: north above, south below, east right, west left. In Activities 1 and 2 each wedge prints its letter at the stage edge.
- Camp board (Star Challenges 1 and 2), as in the book, from above: a grey road curving from the top to the bottom left; a lake with four ducks in the lower middle; four white tents with red flags (one left of the road, one near the top right of the road, one just above the lake, one below it); trees. Four pens (blue, green, purple, yellow), a spare tent at the bottom right, four clue chips along the top.
- Room board (Star Challenge 3), as in the book, in perspective: the girl near the back wall, a window on the back wall behind her, a cupboard on the back wall to her left, a bed on the right, a round bedside table with a glass and a bottle in front of the bed. Name boxes "Window", "Bed", "Cupboard", "Bedside table" with empty dashed boxes; word tags "North", "East", "South", "West".
- My room board (Star Challenge 4): a wooden-floor plan with a dot "You" at the centre; eight cut-outs (bed, cupboard, window, door, table, chair, bookshelf, sofa); a direction-arrow card with four empty spots and chips N, E, S, W; four lines "East ___", "West ___", "North ___", "South ___" with dashed boxes and a chip "nothing here"; a tip chip: "To find north in your room: face the rising Sun. That is east. North is on your left hand."
- One goal chip at the top shows the current goal.
3. Main Interaction
- Drag the cross onto a thing: it snaps and tints; tap a thing and the strip names its wedge. Tap a tent then a pen to colour it. Drag the spare tent, a word tag (reusable) or a cut-out (off the plan to remove it).
- Bottom buttons: "Hint", "Reset" and the main button "Check", which becomes "Next" when the goal chip is green. Reset restores the board.
4. Activities
- Activity 1 (guided). Goal line: "Put the compass cross on the flagpole. Which thing is north of it?" Goal chip: "North of the flagpole". Guess: the child taps the thing they think is north, then drags the cross onto the flagpole. Result: the cross lands on the flagpole, the north wedge tints, the library glows green with a bounce. Why line: "The library is in the north zone, above the flagpole. The library is north of the flagpole." Help: guided, the north wedge pulses.
- Activity 2 (guided). Goal line: "Now find the thing that is west of the flagpole." Goal chip: "West of the flagpole". Setup: the cross stays on the flagpole; wedges tint only after a tap. Guess: the child taps the thing they think is west. Result: the cricket net glows green. Why line: "The cricket net is in the west zone, to the left of the flagpole, so it is west of the flagpole."
- Activity 3 (independent). Goal line: "Move the cross to the water tank. From the water tank, which direction is the cricket net?" Goal chip: "Net from the tank". Setup: the library and the canteen fade out; no zone letters. Guess: before moving the cross, the child taps a letter on the compass card. Result: the net is in the west wedge and W glows green. Why line: "From the water tank, the cricket net is in the west zone, so it is west of the tank."
- Activity 4 (independent). Goal line: "The library is north of the flagpole. From the library, which direction is the flagpole?" Goal chip: "Flagpole from the library". Setup: all four things are back, no letters. Guess: the child taps a letter on the compass card. Result: the cross is on the library, the flagpole is in the south wedge, S glows green. Why line: "The library is north of the flagpole, so the flagpole is south of the library. North and south are opposite."
- Star Challenges: see section 7.
5. Mathematical Understanding
- With N at the top, above is north, below is south, right is east and left is west. A direction is said from somewhere: the water tank is east of the flagpole, but from the tank the flagpole is west.
- The rules to say at the end are the Remember lines of section 7.
6. Feedback and Hints
- Correct: the thing or tent turns green with a gentle bounce and the strip shows the why line.
- Mistake: east and west mixed up -> red strip, small shake: "West is on the left of the compass card. Look to the left of the flagpole." W pulses. Activity 4, the same direction from both things -> "From the library you look the other way. If the library is north of the flagpole, the flagpole is south of the library."
- Mistake: Challenge 1, wrong tent for blue -> "West is to the left. Which tent is on the left of the road?" For green -> "Closest to the lake means nearest to the water." For purple -> "North is up. Find the green tent first, then look above it."
- Mistake: Challenge 2, left of the lake -> "East is to the right on this picture. Move the tent to the other side of the lake."
- Mistake: Challenge 3, a wrong tag for the window -> "The window is on the back wall, behind the girl. Look up the picture, towards the top of the compass."
- Hint button, 3 levels: (1) words: "Where is the thing you are asked about? From which thing or person are you looking?"; (2) visual: the cross jumps onto the thing or person you look from and the wedges tint; (3) almost the answer: the correct wedge pulses (Challenge 1: the first tent turns green).
- Open items (the tent, the room, your own room) are never marked wrong.
7. Ending
- Star Challenge 1 (independent). Goal line, in the book's words: "Children are at a bird-watching camp. Read the clues and colour the tents in the camp accordingly." Clue chips: "The tent to the west of the road is blue." "The tent closest to the lake is green." "The tent north of the green tent is purple." "The tent south of the lake is yellow." Goal chip: "Colour 4 tents". Guess: the child colours all four tents and presses Check; nothing is said before Check. Success: the tent left of the road is blue, the one just above the lake green, the one above it near the top purple, the one below the lake yellow; each clue chip turns green with its why line: "West is left: the tent on the left of the road is blue." "The tent just above the lake is closest to it: green." "North is up: the tent above the green tent is purple." "South is down: the tent below the lake is yellow."
- Star Challenge 2 (independent). Goal line, in the book's words: "Now, draw a tent to the east of the lake." Goal chip: "A tent east of the lake". Guess: the child drags the spare tent where they choose and presses Check. Success: the tent stands on the ground inside the east wedge of an invisible cross on the lake and turns green: "This tent is east of the lake, on its right side. Your answer may differ: any place to the right of the lake is right."
- Star Challenge 3 (independent). Goal line, in the book's words: "Write the directions of the following in relation to the girl. Window ___ Bed ___ Cupboard ___ Bedside table ___" Goal chip: "Directions from the girl". Guess: the child drags a word tag to each name and presses Check. Success: Window North and Bed East turn green; the cupboard accepts West or North and the bedside table accepts South or East, with "This thing sits between two directions. We name the nearest one. Sample answer: window north, bed east, cupboard west, bedside table south. Your answer may differ."
- Star Challenge 4 (independent). Goal line, in the book's words: "Make a drawing of your room and locate the direction in which different things have been placed in relation to you standing at the centre of the room. Make the direction arrow for your room." then "Write the names of the things that are placed in the following directions. East ___ West ___ North ___ South ___" Goal chip: "Draw my room". The child drags at least 3 cut-outs onto the plan as in their own room, fills the direction arrow with N, E, S, W, then drags a placed thing into each name box (or "nothing here"). Guess: the child presses Check when done. Success: each thing is in the zone of its box; the strip reads the child's own answer, for example "East: bed. West: cupboard. North: window. South: door. Your answer may differ."
- End screen (confetti once): "Well done!" Remember: "North is up, south is down, east is right and west is left on a picture with a compass." "A direction is always said from a place or a person." "If A is east of B, then B is west of A." Think and talk: "The cupboard is west of the girl. Which direction is the girl from the cupboard?" Button: "Start again".
8. Assets and Language
- Images: photo-style grass; flat drawings of a flagpole, library, canteen, cricket net and water tank; the camp from above; the girl's room in perspective; a wooden floor; eight room cut-outs; four pens; compass card and cross (code). English.
""".strip("\n")

OBJECTIVES["M1.S4.T4.C11.2D1"] = "The student says the direction of a thing from another thing or from a person on a picture with a compass, and sees that if A is east of B then B is west of A."

# ---------------------------------------------------------------------------------------------------------------
DESCRIPTIONS["M2.S7.T7.C24.2D1"] = """
A. TOOL TITLE
- Bus Route Driver
B. TOOL INFO
- Tool ID: M2.S7.T7.C24.2D1
- Tool type: Concept-activity
- Textbook source: Maps and Locations, Zoo Trip and Bus Route: the street map with its red dotted route, the two sentences for Stop 1 and Stop 2, and questions (a) to (e). No numbers (developer only).
C. LEARNING OBJECTIVE
- The student says the direction a bus drives after a right or a left turn, names the road it turns onto, and reads a street map to find houses, stops and routes.
- Out of scope: distances on the map, in-between directions.
D. TOOL DESCRIPTION
1. Opening Screen
- A practice map, Orchard Town, seen from above: four grey roads make a square ring, Mill Road (top), Dairy Road (bottom), Well Road (left), Temple Road (right), names written along them; orchard trees and a pond inside. A yellow school bus (top view, about 12 percent of the stage width long) stands at the top right corner facing south, with a round dial above it: "The bus is driving: south". The compass card (N top, E red right, S bottom, W left) is in the top right corner.
- Instruction line: "Drive the bus to the corner. Then turn right."
- The child is invited to press "Go" on the steering pad.
2. Scene and Objects
- Steering pad: three big round buttons at the bottom centre: "Go" (the bus drives straight to the next corner or junction), "Turn left" and "Turn right" (a quarter turn onto the road that begins there). The bus leaves a red dotted trail. Practice map corners: Mill and Well (top left), Mill and Temple (top right), Dairy and Well (bottom left), Dairy and Temple (bottom right); no other road joins the ring.
- The book's street map (Star Challenges), from above, N at the top: Hospital Road along the top with the Hospital above it; Children's Park at the top right; Park Road down the right side; Tinku's House and Golu's House just below Hospital Road; below them a pond block with Jaideep's House; the Basketball Court; Market Road; the Shopping Centre; PARKING at the bottom; Lali's House and Rohan's House top left, Ravi's House left in the middle; Prem's House and Raju's House east of Park Road. Stop 1 (S1) is at the hospital gate, Stop 2 (S2) beside the Shopping Centre, near Park Road.
- Chips for the book's sentences: "Hospital", "Market", "Park"; "north", "east", "south", "west"; "right", "left". One goal chip at the top; a curved-arrow icon is Undo.
3. Main Interaction
- "Go", "Turn left" and "Turn right" steer the bus; a turn works only at a corner or junction, towards a road that exists. After a turn the child taps the name of the road the bus is on, printed on the map.
- In the book's map challenges the child taps chips into blanks, taps houses, stops or a compass letter, or drags a finger along the roads (the line snaps to the roads and is read out, for example "south, east, north, east").
- Bottom buttons: "Hint", "Reset" and the main button "Check", which becomes "Next" when the goal chip is green.
4. Activities
- Activity 1 (guided). Goal line: "Drive the bus to the corner and turn right." Goal chip: "Turn right at the corner". Setup: bus at the top right corner facing south, dial on. The child presses Go: the bus drives down Temple Road to the bottom right corner. Guess: before turning, the child taps a letter on the compass card for the direction the bus will drive after the turn. Result: the bus drives west along Dairy Road; the guessed W turns green with a bounce; then the child taps "Dairy Road". Why line: "The bus was driving south. A right turn makes it drive west." Help: guided, the road under the bus pulses.
- Activity 2 (guided). Goal line: "Turn right again at the next corner." Goal chip: "Turn right again". Setup: the bus at the bottom right corner facing west, dial on. The child presses Go to the bottom left corner. Guess: the child taps a letter. Result: the bus drives north along Well Road; the child taps "Well Road". Why line: "The bus was driving west. A right turn makes it drive north."
- Activity 3 (guided, less help). Goal line: "Now turn left at the corner." Goal chip: "Turn left at the corner". Setup: the bus is carried to the bottom left corner facing east, dial on. The child presses Go to the bottom right corner. Guess: the child taps a letter. Result: the bus drives north along Temple Road; the child taps "Temple Road". Why line: "The bus was driving east. A left turn makes it drive north."
- Activity 4 (independent). Goal line: "The bus drives south. Turn left at the corner." Goal chip: "Turn left, driving south". Setup: the bus at the top left corner facing south on Well Road; dial hidden. The child presses Go to the bottom left corner. Guess: the child taps a letter. Result: the bus drives east along Dairy Road; the child taps "Dairy Road". Why line: "The bus was driving south. A left turn makes it drive east." Help: independent, no dial.
- Star Challenges: see section 7.
5. Mathematical Understanding
- A turn tells which hand you turn towards; a direction tells where you go. The same turn gives different directions, depending on the way the bus drives now.
- A right turn takes north to east, east to south, south to west and west to north; a left turn goes the other way round. The Remember lines of section 7 say it.
6. Feedback and Hints
- Correct: the letter turns green with a bounce, the dial arrow turns, the strip shows the why line.
- Mistake: taps E after a right turn from south (a right turn always means east) -> red strip, small shake: "A right turn does not always make the bus drive east. Look at which way the bus drives now, then turn to your right." The dial arrow pulses. The direction it already drives -> "A turn changes the direction. Look at the dial."
- Mistake: wrong road name -> "Look at the name written on the road under the bus." Go at a dead end -> "The road ends here. Turn right or turn left."
- Mistake: Challenge 1, Market -> "That is Market Road, across the middle of the map. Stop 1 is at the hospital gate. Read the name of the road near the Hospital."
- Mistake: Challenge 2, a house left of Park Road -> "East is on the right of the compass. Look across Park Road, to the right of Jaideep's House." Stop 2 for Lali -> "Look at where Lali's House is, at the top left. Which stop is nearer to it?" W for Prem -> "Stop 2 is more below Prem's House than to the left. Which of the four directions is it mostly?"
- Mistake: Challenge 3, a line off the roads -> "The line must stay on the roads. Go back to the last junction."
- Hint button, 3 levels: (1) words: "Which way is the bus driving now? Look at the dial. Is the turn right or left?"; (2) visual: two small hands appear on the bus with their directions written (driving south: right hand "west", left hand "east"); (3) almost the answer: "The bus is driving south. Its right hand points west. A right turn makes it drive west." For map questions: the place you look from pulses, an arrow runs in the direction asked, then the answer pulses.
7. Ending
- Star Challenge 1 (independent). Goal line, in the book's words: "The bus will start from the parking area. It will go north and then it will take a right turn onto ___ Road driving in the ___ direction to reach Stop 1 (S1)." and "To reach Stop 2 (S2), it will turn ___ (right/left) onto ___ Road driving in the ___ direction." Goal chip: "Fill the blanks". Setup: the book's street map; the bus on the PARKING area facing north; chips under the sentences. Guess: the child taps chips into the five blanks and presses Check; nothing is said before Check. Success: the bus drives the child's route with the dial on: north, a right turn onto Hospital Road driving east to Stop 1, on to Park Road, a right turn onto Park Road driving south to Stop 2. Blanks: Hospital, east; right, Park, south. Why line: "The bus was driving north and turned right onto Hospital Road. A right turn makes it drive east. Then it turned right onto Park Road: east to south." A wrong answer makes the bus drive the wrong road and stop.
- Star Challenge 2 (independent). Goal line, in the book's words: "Whose houses are situated to the east of Jaideep's house? ___" then "Which stop is closer to Lali's house? ___" then "In which direction would Prem have to move to reach Stop 2?" Goal chip: "3 questions on the map". Guess: the child taps houses, a stop and a compass letter, then presses Check for each. Success: Prem's House and Raju's House glow; Stop 1 is chosen; S glows. Why lines: "Prem's House and Raju's House are on the right of Park Road, on the east side." "No distances are printed, so we judge from the picture: Stop 1 is near the top, close to Lali's House." "Stop 2 is below Prem's House, so Prem moves south."
- Star Challenge 3 (independent). Goal line, in the book's words: "Mark the route from Ravi's house to the children's park." then "Golu is running late. Trace the route to help him reach the nearest bus stop." Goal chip: "Trace 2 routes". Guess: the child drags a finger from the house gate along the roads and presses Check. Success: a route on the roads that ends at the Children's Park gate, and a route from Golu's House that ends at Stop 1, turn green and are read in words. Sample routes: Ravi's house south, east to the main road, north to Hospital Road, east to Park Road and the park; Golu's house south, east to Park Road, north to Hospital Road, west to Stop 1. "Your answer may differ: other routes along the roads are right too."
- End screen (confetti once): "Well done!" Remember: "A right turn takes north to east, east to south, south to west and west to north." "A left turn goes the other way round: north to west, west to south, south to east and east to north." "A turn is right or left. A direction is north, east, south or west." Think and talk: "Can a right turn make a bus drive west? Which way was the bus driving before the turn?" Button: "Start again".
8. Assets and Language
- Images: flat top-view Orchard Town; a yellow school bus (top-view cut-out); the book's street map redrawn from above (roads, Hospital, park, court, shopping centre, parking, eight houses with labels, stop signs S1 and S2); the red dotted route (code); the compass card. English.
""".strip("\n")

OBJECTIVES["M2.S7.T7.C24.2D1"] = "The student understands that a turn is right or left while a direction is north, east, south or west, and says which direction a bus drives after each turn on a street map."

# ---------------------------------------------------------------------------------------------------------------
DESCRIPTIONS["M2.S10.T10.C41.2D1"] = """
A. TOOL TITLE
- Metro Route Planner
B. TOOL INFO
- Tool ID: M2.S10.T10.C41.2D1
- Tool type: Concept-activity
- Textbook source: Maps and Locations, Delhi Metro Train Stations: the metro map with its key of 10 symbols and the six questions on it. Counts used (circles and capsules between the two ends): Route A 14, Route B 15, Route C 25 (developer only).
C. LEARNING OBJECTIVE
- The student follows a coloured metro line, changes lines only at a capsule, and counts the stations between two stations without counting the two ends.
- Out of scope: fares, timetables, distances between stations.
D. TOOL DESCRIPTION
1. Opening Screen
- The Delhi metro map, redrawn from the book in clean lines, fills the stage: eight coloured lines (Red, Yellow, Blue, Airport Express in orange, Green, Violet, Pink, Magenta), a white circle at every station, a capsule with two coloured dots at every interchange, a pale blue river band and the station names. The key with its 10 symbols is at the bottom right. Two pills at the top left read "Stations between: 0" and "Changes: 0".
- Instruction line: "Find the capsule at Kashmeri Gate. Which two lines meet there?"
- The child is invited to tap two colours in the key, then the capsule.
2. Scene and Objects
- The map is code-drawn from the book's map with the same stations on each line. Printed names are those of the book's map, including Qutb Minar, Saket, Hauz Khas, INA, Rajiv Chowk, Supreme Court, Kashmeri Gate, Kalkaji Mandir, Botanical Garden and Mundka.
- Key: symbols 1 to 8 are the lines; 9 is a circle, "Metro Station"; 10 is a capsule with two coloured dots, "Interchange Line".
- A ride glows along the line in its colour, with an orange ring on the start and a green ring on the end. Small icons on the stage: Undo (curved arrow) and a star that saves a finished route (up to three, shown as chips "Route A", "Route B", "Route C"). One goal chip at the top.
3. Main Interaction
- Tap a start station, then a station farther along the same line: the part between glows and the counter shows the stations between. A station on another line gives "These two stations are on different lines. Ride to a capsule that shows both colours first."
- To change line, tap the capsule: its two dots become two colour buttons; tap a colour to ride on, then tap the next station. Lines that only cross give no change.
- Counting rule: every circle and capsule strictly between the first and the last station counts once; the two ends never count; a capsule where you change counts as one.
- Bottom buttons: "Hint", "Reset" and the main button "Check", which becomes "Next" when the goal chip is green. Reset clears the board.
4. Activities
- Activity 1 (guided). Goal line: "Find the capsule at Kashmeri Gate. Which two lines meet there?" Goal chip: "Two lines meet". Guess: before tapping the capsule, the child taps two colours in the key. Result: the capsule grows and shows a yellow dot and a red dot; the chips Yellow and Red turn green. Why line: "Kashmeri Gate has a yellow dot and a red dot, so the Yellow Line and the Red Line meet here. You can change lines here." Help: guided, the capsule and its key symbol pulse.
- Activity 2 (guided). Goal line: "Ride the Blue Line from Rajouri Garden to Kriti Nagar. How many stations are between?" Goal chip: "Stations between". Setup: Rajouri Garden (blue and pink capsule) is "start", Kriti Nagar (blue and green capsule) is "end". Guess: before riding, the child taps "2", "3" or "4". Result: the Blue Line glows, bubbles "1" and "2" pop over the two circles, the counter shows 2. Why line: "Between Rajouri Garden and Kriti Nagar there are 2 stations, not counting the two ends." Help: guided, bubbles on every station passed.
- Activity 3 (guided, less help). Goal line: "Ride the Blue Line from Janakpuri West to Kriti Nagar. Count the stations between." Goal chip: "Count with a capsule". Setup: Janakpuri West (a blue and magenta capsule) to Kriti Nagar; the Rajouri Garden capsule lies between. Guess: the child taps "6", "7" or "8". Result: the counter runs 1 to 4 over four circles, 5 at the Rajouri Garden capsule, 6 and 7 over two circles. Why line: "4 circles, then the capsule at Rajouri Garden counts as 1, then 2 circles: 4 + 1 + 2 = 7 stations between, not counting Janakpuri West and Kriti Nagar." Help: bubbles only on the capsule.
- Activity 4 (independent). Goal line: "Can you change lines where the Airport Express Line crosses the Magenta Line? Tap the crossing." Goal chip: "Cross or change?". Guess: the child taps "Yes" or "No", then the crossing near Delhi Aerocity. Result: the crossing shows no capsule; "No" turns green. Why line: "No. There is no capsule here, so the two lines only cross. You can change lines only at a capsule that shows both colours." Help: independent.
- Star Challenges: see section 7.
5. Mathematical Understanding
- A coloured line is one route, a circle is one station, a capsule with two dots is a station where two lines meet. The line changes only at a capsule. Routes are compared by their stations between.
- The rules to say at the end are the Remember lines of section 7.
6. Feedback and Hints
- Correct: the ring, card or chip turns green with a gentle bounce, the glow stays, the strip shows the why line.
- Mistake: two lines that are not the dots of the capsule -> red strip, small shake: "Look at the two dots in the capsule. What are their colours?" The capsule pulses.
- Mistake: counts the ends (taps 4 in Activity 2, or 8 in Activity 3) -> "Do not count the first and the last station. Count only the circles between them." The two ends pulse. Leaves out the capsule (taps 6 in Activity 3) -> "A capsule is a station too. Count it as one." The capsule pulses.
- Mistake: Yes in Activity 4 -> "A crossing is not a change. Look for a capsule with two dots."
- Mistake: a route that stops early -> "This route stops at Hauz Khas. Keep riding until you reach Supreme Court." Another card for the fewest stations -> "Count again: which route has the smallest number on the counter?"
- Hint button, 3 levels: (1) words: "Which line are you on? Look at the colour of the glow."; (2) visual: the capsules on your line that show a second colour pulse and the circles show number bubbles; (3) almost the answer: "Count the circles between the two ends, not the ends. A capsule counts as one station." and the tool rides the first leg for you.
7. Ending
- Star Challenge 1 (independent). Goal line, in the book's words: "What do the different coloured lines represent?" then "Mark the Qutb Minar station on the Yellow Line and the Supreme Court station on the Blue Line." Goal chip: "Lines and stations". A tap on a station puts an orange ring on it (two at most). Three answer cards: "Each coloured line is a different metro route.", "Each colour tells how many people travel.", "Each colour is a different station." Guess: the child taps a card, rings the two stations and presses Check. Success: the first card and both rings turn green. Why line: "Each coloured line is a different metro route. Qutb Minar is on the Yellow Line next to Saket. Supreme Court is on the Blue Line, the third station after Rajiv Chowk."
- Star Challenge 2 (independent). Goal line, in the book's words: "Look at the metro map and trace different routes from the Qutb Minar metro station to the Supreme Court metro station." Goal chip: "2 different routes". The child rides from Qutb Minar and saves each finished route with the star. Guess: the child saves at least two routes and presses Check. Success: every saved route ends at Supreme Court and changes only at capsules; the strip reads each one. Route A, Yellow Line to Rajiv Chowk then the Blue Line: 14 stations between, 1 change. Route B, Yellow Line to INA, Pink Line to Mayur Vihar, Blue Line: 15 stations between, 2 changes. Route C, Yellow Line to Hauz Khas, Magenta Line to Botanical Garden, Blue Line: 25 between, 2 changes. Any other valid route is read the same way, with "Your answer may differ."
- Star Challenge 3 (independent). Goal line, in the book's words: "Lali says, "We can take the Yellow Line and change the metro at Hauz Khas to take the Magenta Line." If the children follow Lali's suggestion, at which station(s) do they need to change the metro line again to reach the Supreme Court metro station?" Goal chip: "Where to change again". Setup: the ride is at Hauz Khas on the Magenta Line. Guess: the child taps the capsule where they would change again and presses Check. Success: Botanical Garden turns green. Why line: "The Magenta Line meets the Blue Line at Botanical Garden, which has a magenta dot and a blue dot. They change there and ride the Blue Line to Supreme Court." Kalkaji Mandir -> "The Violet Line does not go to Supreme Court. Look for the capsule where the Magenta Line meets the Blue Line." Janakpuri West -> "That works, but it is a much longer way. Is there a shorter one?"
- Star Challenge 4 (independent). Goal line, in the book's words: "Which route has the least number of stations between Qutb Minar and Supreme Court?" then "Which metro route(s), do you think, is/are the best way to reach the zoo from Qutb Minar? ___" Goal chip: "Fewest stations". Setup: route cards "Route A", "Route B", "Route C". Guess: the child taps the card they think has the fewest stations between; then each card rides and the counter runs to 14, 15 and 25. Success: Route A turns green. Why line: "Route A has 14 stations between. 14 is less than 15, and 15 is less than 25." For the best way the child taps a card and a reason chip ("It has the fewest stations." "It has the fewest changes."); any card with a reason turns green: "Sample answer: Route A, because it has the fewest stations (14) and only one change, at Rajiv Chowk. Your answer may differ."
- End screen (confetti once): "Well done!" Remember: "A coloured line is one metro route." "Change lines only at a capsule that shows both colours." "Count the stations between two stations, and do not count the two ends." Think and talk: "Why do we not count the first station and the last station when we count the stations between?" Button: "Start again".
8. Assets and Language
- Images: the metro map redrawn in code from the book (coloured lines, circles, two-dot capsules, a pale blue river band, names); the key; route chips; orange and green rings. English.
""".strip("\n")

OBJECTIVES["M2.S10.T10.C41.2D1"] = "The student reads a metro map by following a coloured line, changing lines only at a capsule, and counting the stations between two stations without counting the two ends."

# ---------------------------------------------------------------------------------------------------------------
DESCRIPTIONS["M3.S15.T15.C60.2D1"] = """
A. TOOL TITLE
- Ant Path
B. TOOL INFO
- Tool ID: M3.S15.T15.C60.2D1
- Tool type: Concept-activity
- Textbook source: Maps and Locations, Anthill in the Zoo: a grid of 11 by 11 squares of 1 cm; the ant, laddoos 2 cm east, sugar 3 cm north, bread 3 cm west then 2 cm south, apple 5 cm south, 3 cm east, 2 cm north (10 cm), and the question on other routes (developer only). Practice values added here: honey 5 cm east; crumb 4 cm north then 4 cm west; jam 5 cm east and 3 cm north.
C. LEARNING OBJECTIVE
- The student writes a path on a grid as legs of distance in cm and direction, and sees that the shortest route to a place goes only towards it.
- Out of scope: other units of length, diagonal paths, positions written as pairs of numbers (the next tool).
D. TOOL DESCRIPTION
1. Opening Screen
- A flat grid of 11 by 11 squares fills the stage, each square 1 cm, grey lines on pale paper. A small brown ant stands on the grid point 5 lines from the left edge and 5 lines from the top edge, the anthill. The compass card is in the top left corner and the label "1 cm" with a small double arrow in the top right corner. A honey jar (photo-style cut-out) stands 5 squares to the right of the ant.
- Instruction line: "How far is the honey from the ant? Make a guess."
- The child is invited to tap a number chip.
2. Scene and Objects
- The ant moves only along grid lines, one square (1 cm) at a time, leaving a red dashed trail with arrowheads. The compass card is the steering pad: tap its N, E, S or W arrow to move the ant 1 cm that way; the ant can also be dragged along a line, snapping to grid points.
- Legs strip under the grid: the tool writes the path as it grows, for example "4 cm north, then 4 cm west", with a counter "Length: 8 cm". In the Star Challenges it is the child's answer sentence.
- Star Challenge places, as in the book: laddoos 2 squares right of the ant, sugar 3 above, bread 3 left and 2 below, a red apple 3 right and 3 below, with the book's red dashed routes drawn faintly. In the activities the foods are a honey jar, a cake slice and a jam jar.
- Answer blanks: a number blank opens a ring of the numbers 1 to 10; a direction blank opens four chips "north", "east", "south", "west". One goal chip at the top; a curved-arrow icon is Undo; a star icon saves a finished route (up to 3).
3. Main Interaction
- One tap on a compass arrow is one square; the ant never leaves the grid. Moves in the same direction join into one leg; a change of direction starts a new leg.
- Bottom buttons: "Hint", "Reset" and the main button "Check", which becomes "Next" when the goal chip is green. Reset puts the ant on the anthill and clears the trail and saved routes.
4. Activities
- Activity 1 (guided). Goal line: "Move the ant to the honey. Count the squares." Goal chip: "Reach the honey". Setup: honey 5 squares east of the ant; legs strip and length counter on; a number bubble pops over each square crossed. Guess: before moving, the child taps "4", "5" or "6" for the number of cm. Result: after five taps on E the ant stands on the honey and the guessed 5 turns green. Why line: "5 squares of 1 cm each are 5 cm. The honey is 5 cm towards the east." Help: guided, bubbles and labels.
- Activity 2 (guided, less help). Goal line: "Move the ant to the cake crumb. It is not in a straight line." Goal chip: "Reach the crumb". Setup: the cake slice is 4 squares north and 4 squares west of the ant; legs strip and counter on, no bubbles. Guess: before moving, the child taps the first direction to go, "north" or "west". Result: either order reaches the crumb; the strip writes "4 cm north, then 4 cm west". Why line: "Two legs: 4 cm north and 4 cm west. Length: 4 + 4 = 8 cm."
- Activity 3 (independent). Goal line: "Make two different routes to the jam. Which is shorter?" Goal chip: "Compare 2 routes". Setup: the jam jar is 5 squares east and 3 squares north of the ant. Guess: before building, the child taps "Route X is shorter", "Route Y is shorter" or "Same". The child builds and saves Route X, 5 cm east then 3 cm north, and Route Y, 2 cm south, 5 cm east, then 5 cm north. Result: both lengths appear side by side, Route X 5 + 3 = 8 cm and Route Y 2 + 5 + 5 = 12 cm, with "Route Y is 4 cm longer." Why line: "Route Y goes 2 cm south, away from the jam, and then needs 2 cm more to come back: 3 + 2 = 5 cm north." Any route that ends on the jam is read the same way. Help: independent.
- Activity 4 (independent). Goal line: "Is a route with more turns longer? Build this route to the jam." Goal chip: "Count cm, not turns". The child builds 2 cm east, 1 cm north, 3 cm east, then 2 cm north. Guess: before building, the child taps "longer than 8 cm", "8 cm" or "shorter than 8 cm". Result: the route ends on the jam; the strip writes 2 + 1 + 3 + 2 = 8 cm and "3 turns, and still 8 cm." Why line: "It never goes the wrong way, so it is as short as the route with one turn. Count the cm, not the turns." Help: independent.
- Star Challenges: see section 7.
5. Mathematical Understanding
- Each square is 1 cm, so counting squares along a line gives the distance and the compass the direction. A path with a turn is a list of legs; its length is their sum. A step the wrong way adds length because it must be walked back, so the shortest routes go only towards the place; the number of turns does not decide the length.
- The rules to say at the end are the Remember lines of section 7.
6. Feedback and Hints
- Correct: the guess chip or food turns green with a gentle bounce, the ant hops, the strip shows the why line.
- Mistake: the ant is not on the food -> red strip, small shake: "The honey is 1 cm more towards the east." The next square pulses.
- Mistake: counts grid lines instead of squares (says 6 for 5 squares) -> "Count the squares, not the lines. The ant stands on a line." Wrong direction (south for up) -> "Look at the compass. N is at the top, so up is north."
- Mistake: one leg for a food that needs two -> "The food is not in a straight line. How many legs does the route need?" Activity 3, "same" or "Route X is longer" -> "Add the legs of each route. Route X: 5 + 3. Route Y: 2 + 5 + 5." Activity 4, more turns is longer -> "Add the cm of each leg, not the turns: 2 + 1 + 3 + 2."
- Mistake: Challenge 2, the 10 cm route as the shortest -> "This route goes 2 cm north, away from the apple. Is there a route that goes only east and south?"
- Hint button, 3 levels: (1) words: "Which way is the food from the ant? Count the squares along one straight grid line."; (2) visual: the squares of the first leg are numbered 1, 2, 3 on the grid; (3) almost the answer: the tool moves the ant along the first leg and writes it: "Now tap the other arrow for the next leg."
- Edge cases: a move off the grid gives "The grid ends here."; Undo goes back square by square.
7. Ending
- Star Challenge 1 (independent). Goal line, in the book's words: "To get to the laddoos, the ant has to crawl how far, and towards which direction? Each square of the grid is 1 cm." then "To get to the sugar, the ant has to crawl ___ cm in the ___ direction." then "To get to the bread, the ant has to crawl ___ cm in the ___ direction; then ___ cm in the ___ direction." Goal chip: "Laddoos, sugar, bread". Guess: for each food the child fills the blanks and presses Check; the ant then walks the legs written and lands on the food (green) or stops short or over. Success: laddoos 2 cm towards the east; sugar 3 cm in the north direction; bread 3 cm in the west direction, then 2 cm in the south direction, 5 cm in all. Why lines: "2 squares of 1 cm each are 2 cm, and the laddoos are on the side of E." "3 squares up are 3 cm, and up is north." "3 cm west, then 2 cm south: 3 + 2 = 5 cm."
- Star Challenge 2 (independent). Goal line, in the book's words: "To get to the apple, the ant needs to crawl ___ cm towards ___, and then ___ cm towards ___, and finally ___ cm towards ___." then "Identify other routes to reach the point where apple is located. Which one is the shortest?" Goal chip: "The apple routes". Guess: the child fills the six blanks and presses Check. Success: 5 cm towards south, 3 cm towards east, and finally 2 cm towards north: 5 + 3 + 2 = 10 cm in all, saved as "Route 1, 10 cm". The child builds up to 2 other routes to the apple and saves them; the tool reads each, for example 3 cm east then 3 cm south, 3 + 3 = 6 cm; 1 cm south, 3 cm east, then 2 cm south, 1 + 3 + 2 = 6 cm. The child taps the route they think is shortest and presses Check; a route of 6 cm turns green. Why line: "The apple is 3 cm east and 3 cm south of the ant. The shortest routes go only east and south, and are 6 cm. Your routes may differ."
- End screen (confetti once): "Well done!" Remember: "Each square is 1 cm. Count the squares to find the distance and say the direction." "A path with turns is one leg after another." "The shortest route goes only towards the food." Think and talk: "Can a route with many turns be as short as a route with one turn? When?" Button: "Start again".
8. Assets and Language
- Images: pale paper with the grid (code); a brown ant (top-view cut-out); photo-style cut-outs of a honey jar, cake slice, jam jar, laddoos, sugar cubes, bread and a red apple; the red dashed trail (code); the compass card. English.
""".strip("\n")

OBJECTIVES["M3.S15.T15.C60.2D1"] = "The student writes a path on a grid as legs of distance in cm and direction, and sees that the shortest route goes only towards the place and not by fewest turns."

# ---------------------------------------------------------------------------------------------------------------
DESCRIPTIONS["M3.S18.T18.C73.2D1"] = """
A. TOOL TITLE
- Zoo Grid Locator
B. TOOL INFO
- Tool ID: M3.S18.T18.C73.2D1
- Tool type: Concept-activity
- Textbook source: Maps and Locations, Locating the Animals in the Zoological Park (Zoo): the 12 by 12 zoo grid, the panda (1,1), the tortoise (4,1), (1,4), and questions 1, 2 and 3 (developer only). Practice values added here: hippo (6,8), parrot (1,11), big cat (8,7) and (7,8), and the walks to (5,2), (9,5) and (12,8).
C. LEARNING OBJECTIVE
- The student finds a position on a grid by going east to the column and then north to the row, writes it as (column,row), and sees that the order of the two numbers matters.
- Out of scope: negative numbers, other quarters of a grid, distances between positions.
D. TOOL DESCRIPTION
1. Opening Screen
- The zoo map as a grid fills the stage: 12 columns and 12 rows of light green squares with cream paths, trees and a small pond. The vertical lines are numbered 1 to 12 along the bottom and the horizontal lines 1 to 12 up the left side, 0 at the bottom left corner; a wooden "ZOO" sign is at the bottom. Sixteen animals stand where lines meet (panda, tortoise, crocodile, lion, snake, elephant, monkey on a big tree, tiger, deer, big cat, hippo in the pond, giraffe, zebra, flamingo, parrot, toucan). The compass card is in the top right corner. A round orange marker sits at 0.
- Instruction line: "Walk the marker to the hippo. Do you go east first or north first?"
- The child is invited to tap "East first" or "North first".
2. Scene and Objects
- Marker: a round orange pin about one square wide. It moves only along grid lines: first east along the bottom line, then north up a column line, snapping to each line. The numbers it passes light up (columns along the bottom, rows on the left).
- Bracket card "( __ , __ )": the column first, the row second. In Activities 1 and 2 it shows the marker's position live; later it is empty until the child fills it by tapping the number on the bottom line for the column and the number on the left side for the row.
- "What is here" bubble at the marker: the animal's name or "No animal here" (Activities 1 to 3 only). Tapping an animal names it.
- Dot tray (Star Challenge 4): six large dots at the bottom: red, green, blue, orange, black, pink. One goal chip at the top.
3. Main Interaction
- Drag the marker east along the bottom line, then north up a column line. It cannot go up from 0 before going east: it stays and the strip says "First move horizontally from 0, then vertically." Reset goes back to 0.
- Tap a number on a line to put it in the bracket; tap a filled slot to clear it. In Star Challenge 4 tap a dot colour to drop that dot where the marker stands; the marker then hops back to 0.
- Bottom buttons: "Hint", "Reset" and the main button "Check", which becomes "Next" when the goal chip is green. Reset returns the marker to 0 and clears the bracket and dots.
4. Activities
- Activity 1 (guided). Goal line: "Walk the marker to the hippo. East first, then north." Goal chip: "Walk to the hippo". Setup: marker at 0; bracket live; bubble on; the pond glows. Guess: before moving, the child taps "East first" or "North first". Result: the child drags the marker 6 steps east, then 8 steps north; the bracket goes (0,0), (6,0), (6,8) and the bubble says "hippo". Why line: "You went 6 steps east and then 8 steps north, so the hippo is at (6,8)." Help: guided, live bracket and bubble.
- Activity 2 (guided, less help). Goal line: "Find the position of the parrot. Walk to it." Goal chip: "Position of the parrot". Setup: marker at 0; the parrot on the top left tree pulses. Guess: before walking, the child taps one of two brackets, "(1,11)" or "(11,1)". Result: the child walks east, then north, to the parrot; the bracket shows (1,11) and the bubble says "parrot". Why line: "1 step east, then 11 steps north: the parrot is at (1,11)." If the child chose (11,1), the marker goes 11 steps east and 1 north, the bubble says "No animal here" and the strip says "The first number is the column: 11 steps east. The parrot is up on the left."
- Activity 3 (independent). Goal line: "The big cat is at (8,7). A friend says it is at (7,8). Walk to (7,8)." Goal chip: "Is it (7,8)?" Setup: the big cat is shown with its bracket (8,7). Guess: before walking, the child taps "Yes, the big cat is there" or "No". Result: the child walks 7 steps east and 8 steps north; the bubble says "No animal here". Why line: "(7,8) is 7 steps east and 8 steps north. The big cat is at (8,7): 8 steps east and 7 steps north. The first number is the column."
- Activity 4, Practice block (independent). Goal line: "Walk to each place and write its position." Goal chip: "3 walks". Setup: three places one after the other, shown as small flags: (5,2), (9,5) and (12,8); bracket and bubble hidden. Guess: for each flag the child walks the marker there, fills the bracket by tapping the column and row numbers, and presses Check. Result: each bracket matches its flag. Why lines: "5 steps east, then 2 steps north: (5,2)." "9 steps east, then 5 steps north: (9,5)." "12 steps east, then 8 steps north: (12,8)." Help: independent.
- Star Challenges: see section 7.
5. Mathematical Understanding
- A place on a grid is told with two numbers. From 0 the child goes east to the column and then north to the row, and sees the bracket grow. (7,8) and (8,7) use the same numbers in another order, so they are two different places.
- The rules to say at the end are the Remember lines of section 7.
6. Feedback and Hints
- Correct: the bracket, dot or animal turns green with a gentle bounce, the marker hops, the strip shows the why line.
- Mistake: north before east -> red strip, small shake: "First move horizontally from 0, then vertically."
- Mistake: numbers in the wrong order (for example (6,10) for the deer at (10,6)) -> "(6,10) is 6 steps east and 10 steps north. Which number is the column? Walk east first." The marker walks to the written place and the bubble says what is there.
- Mistake: counts squares instead of lines -> "The numbers belong to the lines. Count the lines you pass."
- Mistake: Challenge 4, a dot on the wrong place -> it slides back: "Move east 8 steps first, then north 3 steps." (that part's numbers). Challenge 2, a wrong animal -> "Look at where the marker stands. Which animal is on that meeting point?"
- Hint button, 3 levels: (1) words: "Which number comes first, and which way do you walk for it?"; (2) visual: the column line of the place glows from 0 along the bottom, then the row line glows; (3) almost the answer: the marker walks the east part and stops at the column: "Now go north to the row."
- Edge cases: the marker stops at 12 on the bottom line and at 12 up the side; going back is done with Reset.
7. Ending
- Star Challenge 1 (independent). Goal line, in the book's words: "Start from 0 on the zoo map. How do you reach the panda, and how do we write its position?" then "To reach the tortoise, move ___ steps towards east and reach the ___ column. Then move ___ step(s) ___ and reach the first ___." then "The location of the tortoise is (4,1). What is at (1,4)?" Goal chip: "Panda, tortoise, (1,4)". Guess: for the panda the child walks and fills the bracket; for the tortoise the child fills the blanks (a number blank takes the number tapped on a line, a word blank takes the chip "north", "east", "column" or "row"); for (1,4) the child walks and taps the animal found. The child presses Check for each. Success: the panda is at (1,1); the tortoise: 4 steps towards east, the 4th column, 1 step north, the first row; at (1,4) a snake. Why lines: "1 step east to the first column, then 1 step north to the first row: (1,1)." "4 steps east and 1 step north: the tortoise is at (4,1)." "(1,4) is 1 step east and 4 steps north: a snake. It is not the same place as (4,1)."
- Star Challenge 2 (independent). Goal line, in the book's words: "Locate the animal at the following positions on the map. (a) (11,11) ___ (b) (2,6) ___ (c) (6,4) ___ (d) (3,10) ___ (e) (11,3) ___ (f) (10,9) ___" Goal chip: "Name 6 animals". Guess: for each position the child walks the marker from 0 (it hops back to 0 after each one), taps the animal where it stands and presses Check. Success: (a) toucan, (b) tiger, (c) elephant, (d) flamingo, (e) monkey, (f) zebra. Why line, for example: "11 steps east and 11 steps north: a toucan."
- Star Challenge 3 (independent). Goal line, in the book's words: "Write the position of the following animals on the map. (a) Lion ___ (b) Elephant ___ (c) Tortoise ___ (d) Deer ___ (e) Panda ___ (f) Crocodile ___" Goal chip: "Write 6 positions". Guess: for each animal, which pulses, the child fills the bracket with its column and row and presses Check; the marker then walks east and north from 0 to the written position. Success: lion (3,3), elephant (6,4), tortoise (4,1), deer (10,6), panda (1,1), crocodile (10,1). Why line, for example: "3 steps east and 3 steps north: the lion is at (3,3)."
- Star Challenge 4 (independent). Goal line, in the book's words: "Place dots of different colours on the following positions. (a) (8,3) (Red) (b) (2,9) (Green) (c) (7,3) (Blue) (d) (3,8) (Orange) (e) (8,6) (Black) (f) (6,6) (Pink)" Goal chip: "Place 6 dots". Guess: for each position the child walks the marker, taps the colour to drop the dot, and after all six presses Check. Success: red at (8,3), green at (2,9), blue at (7,3), orange at (3,8), black at (8,6), pink at (6,6). Why line, for example: "8 steps east, then 3 steps north: the red dot is at (8,3)."
- End screen (confetti once): "Well done!" Remember: "Start at 0. Go east to the column, then north to the row." "Write the column first and the row second." "The same two numbers in another order are another place." Think and talk: "Is (3,5) the same place as (5,3)? How do you know?" Button: "Start again".
8. Assets and Language
- Images: the zoo map as a code-drawn 12 by 12 grid (numbered lines, light green ground, cream paths, a small blue pond, a wooden ZOO sign); flat cut-outs of the sixteen animals; the orange marker pin; six coloured dots; the compass card. English.
""".strip("\n")

OBJECTIVES["M3.S18.T18.C73.2D1"] = "The student finds a position on a grid by going east to the column and then north to the row, and sees that the two numbers of a position cannot swap places."
