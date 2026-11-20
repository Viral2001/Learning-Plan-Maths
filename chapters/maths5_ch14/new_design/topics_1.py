# -*- coding: utf-8 -*-
"""Topics T1, T1B and T2 (module M1: Directions and Pictures). The framing intro (the Siberian Crane and the four little
chicks hook, and the free try Face the Rising Sun), the short idea topic T1B (finding directions by the rising Sun,
with Manu's questions), and Directions on a Picture (the bird-watching camp and the room, with the tool Direction Clues).
Every teaching concept has one worked example with the plan's own numbers and objects; every book question is an FIO
item of its topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Finding Directions (framing) ============================================
# The framing topic holds only the hook video and the free-try tool, and no book question. The concept video and
# Manu's questions follow in the short idea topic T1B.
TOPICS.append(TOPIC(
    "T1", "M1", "Finding Directions", ["Chapter opening"], "Understand",
    "",
    "A Siberian Crane flies all the way from Siberia to India, and four little chicks fly from east to west and from "
    "north to south. People keep track of directions too. Try turning Manu to face the rising Sun.",
    [A("T1.C1", "Four Little Chicks and the Siberian Crane", "Understand",
       "",
       textbook=["I visited the Bharatpur Bird Sanctuary in Rajasthan and saw an amazing bird called the Siberian Crane!",
                 "Wow! Do you know that these birds fly all the way from Siberia, a very cold place, to India?",
                 "I wonder how they find their path.",
                 "Four Little Chicks of a bird set out to fly,",
                 "Spreading their wings they all flew high.",
                 "They flew away from East to West,",
                 "flew North to South, without any rest.",
                 "As they flew and explored the land,",
                 "finally, they returned home, hand in hand.",
                 "With their mother, they had so much to share,",
                 "Our home is the best, beyond compare!"],
       teach=["Predict first: a Siberian Crane flies all the way from Siberia, a very cold place, to India. How could "
              "anyone keep track of the way on such a long journey?",
              "A friend visited the Bharatpur Bird Sanctuary in Rajasthan and saw an amazing bird, the Siberian Crane. "
              "These birds fly all the way from Siberia to India.",
              "The children wonder how the cranes find their path. This story does not say. It is a question to wonder "
              "about.",
              "Now listen to a poem called Four Little Chicks. Four little chicks of a bird set out to fly. They flew "
              "away from East to West, and flew North to South, without any rest.",
              "As they flew and explored the land, they came back home with their mother. Our home is the best, beyond "
              "compare!",
              "East, West, North and South are the four directions. Human beings also keep track of directions. One of "
              "the ways is by facing the rising Sun. Let's try!"],
       ncert=["open.cranes", "open.poem"], key_terms=["Siberian Crane", "four little chicks", "directions"],
       video_focus=["HOOK"], enrichment=True, minutes=4),
     DOER("T1.C3", "Face the Rising Sun: Explore", "sun_compass", "Understand",
          "",
          ["Manu stands on a grassy hill in the morning with his arms stretched out.",
           "Human beings keep track of directions too. One of the ways is by facing the rising Sun.",
           "Turn Manu until he faces the rising Sun, and find which way his left hand, his right hand and his back "
           "point."],
          misconceptions=["M_LEFT_WEST"], role="try_it", enrichment=True)],
    topic_type="framing", key_terms=["directions", "rising Sun", "Siberian Crane"]))

# ============================== T1B The Four Directions ====================================================
TOPICS.append(TOPIC(
    "T1B", "M1", "The Four Directions", ["Chapter opening"], "Understand",
    "Students find east by facing the rising Sun, name the directions of the left hand, the right hand and behind, and "
    "write the four directions on a compass.",
    "Facing the rising Sun is facing east. With your arms stretched out, your left hand points north, your right hand "
    "points south and west is behind you. A compass rose shows the four directions: N at the top, E on the right, S at "
    "the bottom and W on the left.",
    [A("T1B.C1", "Finding Directions by the Rising Sun", "Understand",
       "Students find east by facing the rising Sun and name the direction of the left hand, the right hand and behind "
       "using the four directions of the compass.",
       textbook=["Human beings also keep track of directions. One of the ways we figure out directions is by facing the "
                 "rising Sun. Let's try!"],
       teach=["Predict first: it is early morning and you stand facing the rising Sun. Which of the four directions "
              "are you facing?",
              "You are facing east. The Sun rises in the east, so facing the rising Sun is facing east.",
              "Now stretch your arms out to the sides. Your left hand points north and your right hand points south.",
              "West is behind you. West is opposite to east, and south is opposite to north.",
              "Watch out: your left hand does not always point west. Turn to face north and your left hand points west. "
              "The directions stay where they are. Only your hands turn with you.",
              "A compass rose shows the four directions: N for north at the top, E for east on the right in red, S for "
              "south at the bottom and W for west on the left.",
              "Say the four names aloud: north, east, south, west. A compass is another way to find directions.",
              "Rule: face the rising Sun and you face east. Your left hand is north, your right hand is south and west "
              "is behind you."],
       examples=[WE("Lali faces the rising Sun on the school ground. She then turns to face the direction her left hand "
                    "was pointing to. Which direction is she facing now, and which direction is behind her?",
                    ["Lali faces the rising Sun. The rising Sun is in the east, so she faces east.",
                     "Facing east, her left hand points north and her right hand points south.",
                     "She turns to face the direction her left hand was pointing to. That is north, so she now faces "
                     "north.",
                     "Behind her is the opposite of north. North and south are opposite directions, so south is behind "
                     "her.",
                     "Check: north is at the top of the compass rose and south is at the bottom, so they are opposite "
                     "directions."],
                    "She is facing north, and south is behind her")],
       ncert=["open.sun", "note.dir"],
       key_terms=["rising Sun", "east", "left hand", "right hand", "compass", "directions"],
       misconceptions=["M_LEFT_WEST"], minutes=5),
     DOER("T1B.C2", "Practice: Manu and the Rising Sun", None, "Apply",
          "Students write the direction Manu faces and the directions of his left hand and right hand when he faces the "
          "rising Sun, and say which way is west.",
          ["Facing the rising Sun is facing east.",
           "Facing east, the left hand points north and the right hand points south.",
           "West is behind you, opposite to east."],
          items=[FIO("open.manu", "Finding Directions: Manu and the rising Sun",
                     "Manu is facing the rising Sun. That direction is ___. His left hand is pointing in the ___ "
                     "direction. His right hand is pointing in the ___ direction.",
                     ["Manu faces the rising Sun. The rising Sun is in the east, so Manu faces east. The first blank is "
                      "east.",
                      "Manu stretches both arms out to the sides. Facing east, his left hand points north. The second "
                      "blank is north.",
                      "His right hand points the opposite way, south. The third blank is south.",
                      "Check: his two hands point in opposite directions, north and south, and east is in front of "
                      "him."],
                     "East, north, south. Manu faces east, his left hand points north and his right hand points south.",
                     kind="prompt",
                     q_figure="Manu stands on a grassy hill, seen from behind, with both arms stretched out to the "
                              "sides. The Sun is in the sky above the hills in front of him. Beside the picture is a "
                              "compass card with N at the top, E in red on the right, S at the bottom and W on the "
                              "left.",
                     s_figure="The same picture of Manu seen from behind facing the Sun, with the label East in front "
                              "of him pointing to the Sun, the label North at the end of his left hand and the label "
                              "South at the end of his right hand."),
                 FIO("open.west", "Finding Directions: which way is west",
                     "Which way is west?",
                     ["Manu faces east, the direction of the rising Sun.",
                      "West is the direction opposite to east, so it is behind him.",
                      "Check: his left hand is north and his right hand is south, so west is the one direction left, "
                      "behind him."],
                     "West is behind Manu, opposite to the rising Sun, which is in the east.",
                     kind="prompt",
                     q_figure="Manu stands on a grassy hill, seen from behind, with both arms stretched out to the "
                              "sides and the Sun in the sky above the hills in front of him. Beside the picture is a "
                              "compass card with N at the top, E in red on the right, S at the bottom and W on the "
                              "left.",
                     s_figure="Manu seen from behind facing the Sun, with an arrow from Manu backwards, away from the "
                              "Sun, labelled West.")],
          misconceptions=["M_LEFT_WEST"])],
    key_terms=["rising Sun", "east", "compass", "directions"]))

# ============================== T2 Directions on a Picture =================================================
TOPICS.append(TOPIC(
    "T2", "M1", "Directions on a Picture", ["Bird Watching", "Map of a Room"], "Apply",
    "Students say which thing is north, south, east or west of another thing or of a person on a picture with a "
    "compass, and place a tent or a name in a given direction.",
    "On a picture with a compass, above is north, below is south, the right is east and the left is west. The direction "
    "of a thing is always said from a place or a person. If one thing is east of another, the other is west of it.",
    [A("T2.C1", "Reading Directions on a Picture", "Apply",
       "Students say which object is north, south, east or west of another object on a picture with a compass, reading "
       "the top of the picture as north and the right as east.",
       textbook=["Children are at a bird-watching camp."],
       teach=["Predict first: a picture has a compass with N at the top. A boat is drawn above a bridge. Is the boat "
              "north, south, east or west of the bridge?",
              "The boat is north of the bridge. The top of the picture is north.",
              "Read the compass first. N is at the top, S at the bottom, E on the right and W on the left.",
              "A thing drawn above another thing is north of it. Below is south. To the right is east. To the left is "
              "west.",
              "Try it on a playground: a swing at the top left, a slide at the top right, a sandpit at the bottom left "
              "and a seesaw at the bottom right. The slide is to the right of the swing, so the slide is east of the "
              "swing.",
              "Always begin from one thing and look in a direction. East of the swing is the slide. West of the seesaw "
              "is the sandpit.",
              "Rule: on a picture whose compass has N at the top, above is north, below is south, right is east and "
              "left is west."],
       examples=[WE("A playground picture has a compass with N at the top. A swing is at the top left, a slide at the top "
                    "right, a sandpit at the bottom left and a seesaw at the bottom right. Which thing is east of the "
                    "swing, south of the slide, west of the seesaw and north of the sandpit?",
                    ["The compass has N at the top, so above is north, below is south, the right is east and the left "
                     "is west.",
                     "East of the swing: look to the right of the swing. The slide is there.",
                     "South of the slide: look below the slide. The seesaw is there.",
                     "West of the seesaw: look to the left of the seesaw. The sandpit is there.",
                     "North of the sandpit: look above the sandpit. The swing is there.",
                     "Check: the swing and the slide are in the top row and the sandpit and the seesaw are in the "
                     "bottom row, and the top row is north of the bottom row."],
                    "The slide is east of the swing, the seesaw is south of the slide, the sandpit is west of the seesaw "
                    "and the swing is north of the sandpit")],
       ncert=["bird.setup"],
       key_terms=["picture", "compass", "north", "south", "east", "west"],
       minutes=5),
     A("T2.C2", "Directions from Where You Stand", "Understand",
       "Students write the direction of things in a room from a girl standing at the centre, and say that if one thing "
       "is east of another then the other is west of it.",
       teach=["Predict first: a girl stands at the centre of a room plan with N at the top. A shelf is on the wall "
              "above her. Which direction is the shelf from the girl, and which direction is the girl from the shelf?",
              "The shelf is north of the girl. From the shelf, the girl is south of it.",
              "The direction of a thing is always said from somewhere, from a person or from a place. We say the "
              "direction in relation to that person or place.",
              "Look at the room plan from the girl's place at the centre. Above her is north, to the right of her is "
              "east, below her is south and to the left of her is west. Name the things you find.",
              "Now turn the question round. If the bed is east of the girl, then the girl is west of the bed, not "
              "east. East and west are opposite directions.",
              "To find north in your own room, face the rising Sun. That is east. North is on your left hand.",
              "Rule: say what is in each direction while you stand at the centre. If A is east of B, then B is west of "
              "A."],
       examples=[WE("A girl stands at the centre of a room plan with a compass, N at the top. A table is above her, a bed "
                    "is to the right of her, a door is below her and a cupboard is to the left of her. Say the "
                    "direction of each thing from the girl. Then say in which direction the girl is from the bed.",
                    ["N is at the top, so above is north, the right is east, below is south and the left is west.",
                     "The table is above her, so the table is north of her.",
                     "The bed is to the right of her, so the bed is east of her.",
                     "The door is below her, so the door is south of her.",
                     "The cupboard is to the left of her, so the cupboard is west of her.",
                     "Now stand at the bed and look at the girl. She is to the left of the bed, so she is west of the "
                     "bed.",
                     "Check: the bed is east of the girl and the girl is west of the bed, and east and west are "
                     "opposite directions."],
                    "The table is north, the bed east, the door south and the cupboard west of the girl. From the bed "
                    "the girl is to the west")],
       key_terms=["directions", "girl", "centre", "relation", "opposite"],
       misconceptions=["M_SAME_DIRECTION"], minutes=6),
     DOER("T2.C3", "Practice: Direction Clues", "direction_clues", "Apply",
          "Students use clues about directions to colour four tents, draw a tent east of the lake, write the direction "
          "of things in a room from the girl, and name things in the four directions of their own room.",
          ["On a picture with a compass, above is north, below is south, right is east and left is west.",
           "Say the direction of a thing from a place or a person: east of the lake, west of the girl.",
           "If A is east of B, then B is west of A."],
          items=[FIO("bird.colour", "Bird Watching: colour the tents",
                     "Children are at a bird-watching camp. Read the clues and colour the tents in the camp "
                     "accordingly. The tent to the west of the road is blue. The tent closest to the lake is green. "
                     "The tent north of the green tent is purple. The tent south of the lake is yellow.",
                     ["Find the compass. N is at the top, so above is north, below is south, left is west and right "
                      "is east.",
                      "Clue 1: the tent to the west of the road is blue. West is to the left, so colour blue the tent "
                      "on the left of the road.",
                      "Clue 2: the tent closest to the lake is green. Colour green the tent just above the lake.",
                      "Clue 3: the tent north of the green tent is purple. North is above, so colour purple the tent "
                      "above the green tent, near the top.",
                      "Clue 4: the tent south of the lake is yellow. South is below, so colour yellow the tent below "
                      "the lake.",
                      "Check: there are four clues and four tents, and each tent has its own colour: blue, green, "
                      "purple and yellow."],
                     "Blue: the tent left of the road. Green: the tent just above the lake. Purple: the tent above the "
                     "green tent. Yellow: the tent below the lake.",
                     kind="prompt",
                     q_figure="A bird-watching camp seen from above, with a compass card (N at the top, E in red on the "
                              "right, S at the bottom, W on the left). A grey road curves from the top down to the "
                              "bottom left. A lake with four ducks lies in the lower middle. Four white tents with "
                              "small red flags stand in the camp: one on the left of the road, one near the top on the "
                              "right of the road, one just above the lake and one below the lake. Green and yellow "
                              "trees fill the ground.",
                     s_figure="The same camp with the four tents coloured: the tent on the left of the road blue, the "
                              "tent just above the lake green, the tent near the top above the green tent purple and "
                              "the tent below the lake yellow."),
                 FIO("bird.draw", "Bird Watching: a tent east of the lake",
                     "Now, draw a tent to the east of the lake.",
                     ["The compass has E on the right, so east is to the right.",
                      "Find the lake. East of the lake is the ground on the right side of the lake.",
                      "Draw a tent there, on the right of the lake and away from the water.",
                      "Check: the tent is to the right of the lake, so the lake is to the west of the tent."],
                     "Sample answer: a tent drawn on the ground to the right of the lake. Your answer may differ: any "
                     "place to the right of the lake is right.",
                     kind="prompt",
                     q_figure="The same bird-watching camp seen from above, with a compass card (N at the top, E in red "
                              "on the right, S at the bottom, W on the left): the grey road, the lake with four ducks "
                              "in the lower middle, four white tents with small red flags, and green and yellow "
                              "trees.",
                     s_figure="The camp with a fifth tent drawn on the ground to the right of the lake, and an arrow "
                              "from the lake to the new tent labelled East."),
                 FIO("room.dir", "Map of a Room: directions from the girl",
                     "Write the directions of the following in relation to the girl. Window ___ Bed ___ Cupboard ___ "
                     "Bedside table ___",
                     ["On the compass, N is at the top. In the picture, up towards the back wall is north, the right "
                      "is east, the left is west and towards us is south.",
                      "Window: it is on the back wall, behind the girl, so it is north of her.",
                      "Bed: it is on the right side of the picture, so it is east of her.",
                      "Cupboard: it is on the back wall at the left, a little behind her, so the nearest direction is "
                      "west.",
                      "Bedside table: it is the round table beside the bed, in front of her and a little to the "
                      "right, so the nearest direction is south.",
                      "Check: the cupboard and the bedside table sit between two directions. We use only four "
                      "directions, so we name the nearest one. Your answer may differ."],
                     "Sample answer: window north, bed east, cupboard west, bedside table south. Your answer may "
                     "differ.",
                     kind="prompt",
                     q_figure="A room drawn in perspective with a girl standing near the back wall. A window is on the "
                              "back wall behind her. A cupboard stands against the back wall at the left. A bed with a "
                              "round yellow headboard is on the right side of the picture. A small round table with a "
                              "glass and a bottle stands beside the bed. A dressing table with a mirror and a stool is "
                              "at the left. Beside the picture is a compass card with N at the top, E in red on the "
                              "right, S at the bottom and W on the left.",
                     s_figure="The same room with four labels: North on the window, East on the bed, West on the "
                              "cupboard and South on the round bedside table."),
                 FIO("room.draw", "Map of a Room: draw your room",
                     "Make a drawing of your room and locate the direction in which different things have been placed "
                     "in relation to you standing at the centre of the room. Make the direction arrow for your room.",
                     ["Draw your room as a square seen from above. Mark yourself with a dot at the centre.",
                      "Find north. Face the rising Sun, which is east. North is on your left hand.",
                      "Draw the direction arrow in a corner: N at the top, E on the right, S at the bottom and W on the "
                      "left, and draw the room so that north is at the top.",
                      "Draw each thing where it stands as seen from the dot. In a sample room the window is on the "
                      "north wall, the bed on the east side, the cupboard on the west side and the door on the south "
                      "wall.",
                      "Write the direction of each thing from you: window north, bed east, cupboard west, door south.",
                      "Check: each thing sits on the side of the square that matches its direction. Your answer may "
                      "differ."],
                     "Sample answer: window north, bed east, cupboard west, door south, with a direction arrow. Your "
                     "answer may differ.",
                     kind="prompt",
                     q_figure="A large empty rectangle with a dashed blue border, for the drawing of the room.",
                     s_figure="A sample drawing: a square room seen from above with a dot at the centre, the window on "
                              "the top wall, the bed on the right side, the cupboard on the left side and the door in "
                              "the bottom wall, and a direction arrow card with N at the top, E in red on the right, S "
                              "at the bottom and W on the left."),
                 FIO("room.names", "Map of a Room: names in the four directions",
                     "Write the names of the things that are placed in the following directions. East ___ West ___ "
                     "North ___ South ___",
                     ["Look at your drawing from the dot at the centre.",
                      "East is the right side. In the sample room the bed is there.",
                      "West is the left side. In the sample room the cupboard is there.",
                      "North is the top. In the sample room the window is there.",
                      "South is the bottom. In the sample room the door is there.",
                      "Check: each thing is on the side of the square that matches its direction. Your answer may "
                      "differ."],
                     "Sample answer: East: bed. West: cupboard. North: window. South: door. Your answer may differ, it "
                     "depends on your room.",
                     kind="prompt",
                     q_figure="Four lines to write on, labelled East, West, North and South.",
                     s_figure="The sample room seen from above with the bed on the east side, the cupboard on the west "
                              "side, the window on the north wall and the door on the south wall, each with its "
                              "direction word.")],
          misconceptions=["M_SAME_DIRECTION"])],
    key_terms=["picture", "compass", "directions", "girl"]))
