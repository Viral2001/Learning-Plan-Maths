# -*- coding: utf-8 -*-
"""Tool descriptions for Class 5 Chapter 11 (Grandmother's Quilt) in the master-prompt format. Plain text, UTF-8."""

DESCRIPTIONS = {
    "M1.S1.T1.C2.2D1": """
A. TOOL TITLE
- Quilt Lace

B. TOOL INFO
- Tool ID: M1.S1.T1.C2.2D1
- Tool type: Exploration
- Textbook source: Grandmother's Quilt, the opening story with the red, green and blue lace reels of 40, 50 and 25 units. The quilt is 15 patches by 10 patches, counted from the picture. Practice values added by the plan: a quilt of 7 by 5 patches, and a quilt of 10 by 8 patches with reels of 30, 36 and 40 units (developer only).

C. LEARNING OBJECTIVE
- The student sees that lace for a border must go all the way round the quilt, and finds how long it must be by adding the units along the four sides.
- Out of scope: the word "perimeter" (the video that follows names it), area, any length rule, rectangles as a topic.

D. TOOL DESCRIPTION

1. Opening Screen
- The stage shows Grandmother's quilt cover spread on a wooden floor, seen from above, filling most of the stage: 15 patches along the long side and 10 along the short side, each patch about 48 px across on a laptop. Below it, in a row, lie three ribbon reels about 90 px wide with a white label on each rim: red "40 units", green "50 units", blue "25 units".
- Instruction line: "Which lace will go all the way round the quilt? Tap your guess."
- Each reel gives one small hop to show it can be tapped.

2. Scene and Objects
- Background: a plain warm wooden floor of wide planks, photo, top view, no clutter.
- Quilt: drawn in code so the count is exact, 150 patches in rows from the top: green, red, yellow, green, red, yellow, green, red, yellow, green. Green patches have small dots, red patches a white weave, yellow patches spirals. Thin dark seams between patches and a pink frilled rim all round. One patch side is 1 unit.
- Lace: a ribbon 12 px thick in the colour of its reel, lying along the outer edge of the patches on the rim, with a small tick at every unit and a longer tick at every 5 units. It is pulled out of its reel, so the reel shrinks as lace is used.
- Reels: photo cut-outs of ribbon reels in red, green and blue.
- Chips on the stage: the goal chip of the activity (top left) and "Units laid: 0" (top right, counts up while laying).

3. Main Interaction
- Tap a reel to pick it: it lifts and its loose end goes to the top left corner of the quilt. Only one lace is out at a time; tapping another reel puts the first one back.
- Drag the lace tip clockwise along the border. The tip follows the finger's distance along the border, snaps to whole units, one unit for each patch side, and turns at the corners. Dragging back takes the lace back one unit at a time. When the reel is empty the lace stops and its loose end shows a flat cut end.
- Practice quilts: every outer edge is a small bar; tap a bar to count it (it turns orange, the counter goes up by 1), or drag a finger along the rim to count the bars it passes. A bar is counted once only. Tap a patch to mark it (it glows orange).
- Bottom buttons (at most 3): Hint, Reset (picks up the lace and the counts of this activity), and Check, which becomes Next when the activity is done.

4. Activities
- Activity 1 (guided). Goal line: "Lay each lace along the border and see where it ends." Goal chip: "Try all 3 laces". Setup: quilt 15 by 10, reels 40, 50 and 25 units. Guess: before laying, the child taps the reel they think goes all the way round; it gets a flag "my guess". The child picks each reel in turn, in any order, and drags its tip round from the top left corner. Result: the red lace stops at the bottom left corner after 15 + 10 + 15 = 40 units, strip: "The red lace has 40 units. It stops at the corner and 10 units are still to cover." The blue lace stops at the bottom right corner after 15 + 10 = 25 units, strip: "The blue lace has 25 units. 25 units are still to cover." The green lace meets its own start: the quilt glows, labels 15, 10, 15 and 10 appear on the four sides and the strip says "15 + 10 + 15 + 10 = 50. The border is 50 units, so the 50 unit green lace fits exactly." The guess flag turns green on the green reel and grey on another. The goal chip turns green when all 3 are tried. Help: guided, ticks on the lace, corners flash when passed, the running count is always visible.
- Activity 2 (guided). Goal line: "Tap every edge on the outside of the quilt." Goal chip: "Count the border". Setup: a small practice quilt of 7 by 5 patches (practice values) with 24 outer bars. Guess: "How many units is the border? Tap one: 12, 24 or 35." The child taps or sweeps over the outer bars until all 24 are counted. Result: the guess chip is compared; the four sides label themselves 7, 5, 7, 5 and the strip says "7 + 5 + 7 + 5 = 24. The border is 24 units." A plain note shows what the guess was, for example "You guessed 12. That is only one long side and one short side." Help: guided, the bars are drawn and the counter is shown.
- Activity 3 (independent). Goal line: "Tap the patches on the border. Then compare with the lace units." Goal chip: "Patches or units". Setup: the same 7 by 5 quilt, no bars, no labels. Guess: "Are the border patches and the lace units the same number? Tap Same or Different." The child taps every patch that touches the outside edge, 20 patches, counter "Border patches: 20". Result: the 4 corner patches pulse with a small "2 edges" tag, strip: "20 patches but 24 units. Each corner patch has 2 edges on the border: 20 + 4 = 24. Count units of lace, not patches." Help: independent, only the goal chip.
- Star Challenge 1 (practice values). Goal line: "Tick every lace that is long enough to go all the way round." Goal chip: "Long enough". Setup: a new quilt of 10 patches by 8 patches and three reels labelled purple "30 units", orange "36 units" and teal "40 units". Guess and do: the child ticks the reels they think are long enough, then presses Check; the tool lays each ticked lace round the border. Success condition: exactly the orange 36 and the teal 40 are ticked. Result: the orange lace closes the loop, the teal lace closes it with 4 units left over and scissors cut them off, the purple lace stops 6 units short, strip: "10 + 8 + 10 + 8 = 36. The border is 36 units. The 36 lace fits exactly and the 40 lace is long enough with 4 units to spare. The 30 lace is 6 units short." Help: independent. Retry is free and the ticks stay.

5. Mathematical Understanding
- By laying lace, running out and counting units on each side, the child sees that the lace needed is every side added together, and that it must go all the way round with no gap.
- By counting bars and then patches, the child sees that the corners are the trap: a corner patch has two edges on the border, so units are not patches.
- Rules in the child's words: "The lace must go all the way round." "Add the units along every side." "A longer lace also works." "Count units, not patches."

6. Feedback and Hints
- Correct: the goal chip turns green with a gentle bounce, the strip turns green and shows the one-line why, the finished quilt glows once. Wrong answer: red strip, small shake, one friendly line; retry is free, no scores. Confetti only on the end screen.
- Guess steps are never marked wrong. After the result a plain strip compares: "You guessed X. The answer is Y."
- Mistake: taps a seam inside the quilt -> red strip, small shake: "That edge is inside the quilt. Count only the edges on the outside." The outer rim lights up.
- Mistake: taps an edge twice -> "You counted this edge already." The bar blinks once.
- Mistake: lets go of the lace away from the border -> the tip waits at the last unit: "Keep the lace on the border."
- Mistake in Challenge 1: ticks the purple 30 -> "The 30 lace stops 6 units short of the corner. It is not long enough." Leaves out the teal 40 -> "The 40 lace is longer than the border, so it works too. The extra can be cut off." The reel in question pulses.
- Hints, three levels (Activities 1 to 3 and Challenge): (1) "Where does the lace start, and where does it have to end?" or, in Activity 3, "Which patches touch the outside?" (2) the four corners glow one after the other, or the outer rim lights; (3) "The long side is 15 units and the short side is 10 units. How many long sides and short sides are there? Add them all." For the small quilts the numbers 7 and 5, or 10 and 8, are used in the same words.
- Edge cases: a lace exactly as long as the border (50 on 50) closes the loop and the start and end meet; a lace longer than the border leaves extra that is cut; a lace that stops exactly at a corner (blue, red) still has whole sides left; a corner unit is counted once when the lace turns.

7. Ending
- Star Challenge 1 is described above; it is finished when the correct reels are ticked and checked.
- End screen: "Well done!" Remember: "The lace must go all the way round the border." "Add the units along every side to find how much lace you need." "Count units of lace, not patches." Think and talk: "A lace is longer than the border. What can you do with the extra lace?" Button: "Start again".

8. Assets and Language
- Images: top-view wooden plank floor photo; three photo cut-outs of ribbon reels (red, green, blue) plus the same reel shape recoloured purple, orange and teal for the challenge; fabric swatch textures for green dots, red weave and yellow spirals; pink frilled rim strip; small scissors cut-out for the challenge. Quilts, bars, ticks and counters are drawn in code.
- Language: English only, short sentences, the units are the word "units". Nothing on screen says perimeter.
""".strip("\n"),

    "M1.S5.T5.C13.2D1": """
A. TOOL TITLE
- Tile the Table

B. TOOL INFO
- Tool ID: M1.S5.T5.C13.2D1
- Tool type: Concept-activity
- Textbook source: Grandmother's Quilt, the rug (15 by 6), Tables 1 to 4, the notebooks question, Preetha's desk (9 by 6). Practice values added: trays 7 by 2 and 5 by 3, a table top 60 cm by 30 cm (developer only).

C. LEARNING OBJECTIVE
- The student finds which shapes cover a surface with no gaps and no overlaps, and says the area of a region as the number of tiles that cover it, named in the unit of the tile.
- Out of scope: the rule length × breadth, square cm, comparing two regions, perimeter.

D. TOOL DESCRIPTION

1. Opening Screen
- A wooden worktable seen from above. A bare table top, 7 squares long and 2 broad (each square place about 80 px), lies in the middle. A wooden tray along the bottom holds four loose tiles about 70 px across: a yellow triangle, a blue circle, a green square and a pink rectangle (1 square wide, 2 tall).
- Instruction line: "Which shapes can cover the table top with no gaps and no overlaps? Make a guess."
- The child is invited to tick the shapes they think will work.

2. Scene and Objects
- Table top on a wooden worktable photo, top view: light wood, the largest object; faint outlines show the places for the chosen tile.
- Tiles: glossy flat tiles. Triangle: half a square cut corner to corner, 2 per place. Circle: as wide as one place, so gaps stay. Square: 1 place. Rectangle: 1 wide, 2 tall.
- Chips: a tile counter with the name, for example "12 squares", and the goal chip of the activity. Two small round buttons at the table corners: Gaps (empty wood glows orange) and Fill the rest.

3. Main Interaction
- Tap a tile in the tray to pick it. Tap an empty place to drop a tile (it snaps in with a small bounce) or drag across places to drop one in each. Fill the rest covers all empty places. Tap a placed tile to remove it. A tile dropped on a covered place blinks and slides back.
- Counting: tap a tile for the next number badge (1, 2, 3 ...), or drag along a row to count the row. Number dial: 1 to 3 wheels, swipe up or down.
- Bottom buttons (at most 3): Hint, Reset (clears this step), Check, which becomes Next.

4. Activities
- Activity 1 (guided). Goal line: "Cover the tray with each shape and look for gaps." Goal chip: "Try all 4 shapes". Setup: a tray 7 long and 2 broad (practice values). Guess: the child ticks the shapes they think cover the tray with no gaps and no overlaps. The child covers the tray with each shape in turn. Result: squares (14), triangles (28) and rectangles (7) fit; circles (14) leave round gaps and Gaps turns on. Strip: "Triangles, squares and rectangles cover the tray. Circles leave gaps." Help: guided, places drawn.
- Activity 2 (guided). Goal line: "Cover the tray with squares and count them." Goal chip: "Find the area". Setup: a tray 5 long and 3 broad (practice values). Guess: "How many squares will cover it? Tap one: 8, 15 or 16." The child covers it row by row. Result: counter "15 squares", strip "3 rows of 5 squares: 3 × 5 = 15. The area of the tray is 15 square units." Help: guided, each row numbered as it fills.
- Activity 3 (guided, then free). Goal line: "Now cover the same tray with triangles." Goal chip: "Same tray, new tile". Setup: the same 5 by 3 tray with the 15 squares drawn faintly under the triangles. Guess: "Will it need fewer triangles, the same number, or more than squares? Tap one." The child covers it with triangles. Result: "30 triangles", strip "Each square is 2 triangles: 15 × 2 = 30. The tray is the same: 15 square units, or 30 triangle units." Help: the faint squares show the cuts, no row numbers.
- Star Challenge 1. Goal line: "Preetha and Adrit's grandmother is making a rug with square patches. The picture below shows the rug. How many patches have they used to make this?" Goal chip: "Count the patches". Setup: a rug of red and yellow check patches with a fringe, 15 patches in a row, 6 rows. The child counts by taps or by dragging along a row and sets the dial. Guess: the dial may be set first; nothing shows until Check. Result: "6 rows of 15 patches: 15 + 15 + 15 + 15 + 15 + 15 = 90, or 6 × 15 = 90." Help: independent.
- Star Challenge 2, four steps, on four table tops in a row, already covered: Table 1 triangles (5 by 2 squares, each cut in 2), Table 2 circles (4 by 2), Table 3 squares (4 by 2), Table 4 rectangles (3 by 4). Goal chip: "Tables 1 to 4". Each answer is the child's own commit before Check. Step 2a goal line: "Preetha and Adrit are trying to cover their table with different shapes. Preetha covered it with triangles and circles. Adrit covered with squares and rectangles. They found that ___, ___ and ___ shapes cover the top of the table without gaps and overlaps. ___ shape leaves gaps." The child drags the chips Triangle, Circle, Square, Rectangle into the blanks; right: Triangle, Square, Rectangle in any order, then Circle. Step 2b: "Do circles tile? Can we use them to cover a region?" Table 2 comes forward with Gaps on; the child taps Yes or No; right: No, strip "No. Circles leave gaps, so they do not tile." Step 2c: "___ triangles cover Table 1. ___ squares cover Table 3. ___ rectangles cover Table 4." The child counts and sets 3 dials; right: 20, 8, 12; strip "Table 1: 5 × 2 = 10 squares, each cut in 2, 10 × 2 = 20. Table 3: 4 × 2 = 8. Table 4: 3 × 4 = 12." Step 2d: "The area of Table 1 is ___ triangle units. The area of Table 3 is ___ square units. The area of Table 4 is ___ rectangle units." The counts become tags 20, 8 and 12; the child drags each to its sentence. Help: independent.
- Star Challenge 3 (practice values for the sizes). Goal line: "Now, try to cover the top of your table without gaps and overlaps with the following objects of same size. (a) Notebooks (b) Lunch boxes (c) Pencil boxes (d) Maths books. Which of the above objects covered the region completely?" Goal chip: "Which objects cover?" Setup: a table top 60 cm by 30 cm; four top-view photos: notebook 20 cm by 15 cm, lunch box 15 cm by 10 cm, pencil box 20 cm by 10 cm, maths book 30 cm by 15 cm. Guess: the child ticks the objects they think cover it. The child lays each object, then Fill the rest. Result: notebooks 6, lunch boxes 12, pencil boxes 9, maths books 4; all cover it. Strip: "All four are rectangles, and rectangles tile. Notebooks: 60 ÷ 20 = 3 in a row and 30 ÷ 15 = 2 rows, 3 × 2 = 6. Your own table may give a different answer." Help: independent.
- Star Challenge 4. Goal line: "Look at the different tiles on her desk and answer how many of the following shapes will cover the desk. (a) Green triangles ___ (b) Red triangles ___ (c) Blue squares ___" Goal chip: "Cover the desk". Setup: Preetha's desk, a white top of 9 columns by 6 rows of equal squares, and three tiles at true size: a blue square (1 square), a green triangle (half a square), a red triangle (two sides of 3 squares meeting in a corner). Guess: "Which tile will you need the most of? Tap blue, green or red." The child covers the desk with each tile; two red triangles snap into a 3 by 3 square. Then 3 dials. Right: (a) 108, (b) 12, (c) 54. Strip: "The desk has 9 × 6 = 54 squares. Blue squares: 54. Green triangles: 54 × 2 = 108. Two red triangles make a 3 by 3 square, the desk holds 3 × 2 = 6 of them: 6 × 2 = 12." Help: independent.

5. Mathematical Understanding
- Tiles meet edge to edge or leave gaps. The area is the count of tiles, named with the tile; one tray covered by squares and then triangles shows the count depends on the tile.
- Rules in the child's words: "Squares, rectangles and triangles tile. Circles leave gaps." "The area is the number of tiles that cover the region." "A different tile gives a different count."

6. Feedback and Hints
- Correct: the goal chip turns green with a gentle bounce and the strip shows the why. Wrong answer: red strip, small shake, one friendly line; retry is free, no scores. Confetti only on the end screen. Guesses are never marked wrong: a plain strip says "You guessed X. The answer is Y."
- Mistake: tile put on a covered place -> "This tile overlaps another one. Each tile needs its own place." The covered tile blinks.
- Mistake: Yes for circles -> "Look at the gaps between the circles. Circles leave gaps, so they do not tile." Gaps turns on.
- Mistake: 10 for Table 1 -> "10 is the number of squares. Count the triangles." The cut lines show. A tag on the wrong sentence -> "Table 3 is covered by squares. Use the number of squares."
- Mistake: 54 for red -> "A red triangle is bigger than a square. Two red triangles make a 3 by 3 square." A 3 by 3 block glows.
- Hints, three levels: (1) "Are there gaps between the tiles? Do any tiles lie on top of each other?" or "How many tiles are in one row, and how many rows?" (2) the empty wood glows, or the first row is numbered; (3) "Squares, rectangles and triangles fit edge to edge, circles do not." or "Tiles in a row times rows, for example 3 rows of 5: 3 × 5 = 15." Desk: "9 × 6 = 54 squares. A green triangle is half a square, so double 54."
- Edge case: a single triangle in a place leaves half of it empty and Gaps lights it.

7. Ending
- End screen: "Well done!" Remember: "Squares, rectangles and triangles tile. Circles leave gaps." "The area is the number of tiles that cover the region." "A different tile gives a different count." Think and talk: "The same desk needs 54 squares or 108 triangles. Why is the number different?" Button: "Start again".

8. Assets and Language
- Images: top-view wooden table photo; yellow triangle, blue circle, green square and pink rectangle tile cut-outs; red and yellow check rug with fringe; top-view photos of a notebook, a lunch box, a pencil box and a maths book. The desk grid, counters and dials are drawn in code.
- Language: English only; unit words "square units", "triangle units", "rectangle units".
""".strip("\n"),

    "M1.S8.T8.C30.2D1": """
A. TOOL TITLE
- Grid Area

B. TOOL INFO
- Tool ID: M1.S8.T8.C30.2D1
- Tool type: Concept-activity
- Textbook source: Grandmother's Quilt, Comparing Shapes: rectangles A (3 by 4), B (2 by 4), C (2 by 5), the gardens (A 2 by 5, B 4 by 3), the palm and the leaves. Practice values added: cut-outs D 6 by 2, E 8 by 4, F 3 by 5, a house of 12 square cm, leaves of 30, 18, 24 square cm (developer only).

C. LEARNING OBJECTIVE
- The student compares two areas by laying one shape on the other when one fits inside, and by counting the same unit squares on a grid when neither fits, counting two half squares as one.
- Out of scope: the rule length × breadth, perimeter, area of a triangle by a rule.

D. TOOL DESCRIPTION

1. Opening Screen
- A craft table seen from above. A grid sheet of 1 cm squares lies in the middle, 15 columns by 12 rows, each square about 36 px. Beside it lie two paper cut-outs: a light blue D and a larger orange E.
- Instruction line: "Which paper has the larger area, D or E? Make a guess."
- The child is invited to tap D or E.

2. Scene and Objects
- Grid sheet: thin pale blue lines, a key square marked "1 cm" and "1 unit square", on a light wooden craft table photo.
- Paper cut-outs: coloured paper with a slight shadow and a letter. Practice: D light blue 6 long and 2 broad, E orange 8 by 4, F green 3 by 5. Book shapes: A yellow 3 by 4, B pink 2 by 4, C purple 2 by 5.
- Chips: a counter such as "D: 12" and the activity's goal chip.

3. Main Interaction
- Drag a cut-out onto another: on release its top left corner lines up with the other's. If it fits inside, it clicks in; if not, the part that sticks out glows orange.
- Drag a cut-out onto the grid: it snaps to whole squares. Tap a square, drag across squares or tap a row to count (squares turn orange, counter goes up).
- A half square is a square cut corner to corner. Drag one half square onto another: they join into 1 whole square.
- Trace pad: draw a closed outline on the grid with a finger. Squares fully inside turn pale orange; squares the line crosses are hatched part squares.
- Number dial: 1 to 3 wheels, swipe up or down, "square cm" printed beside it.
- Bottom buttons (at most 3): Hint, Reset (returns the shapes of this step), Check, which becomes Next.

4. Activities
- Activity 1 (guided). Goal line: "Lay D on E. Does D fit inside?" Goal chip: "Lay one on the other". Setup: D (6 by 2) and E (8 by 4), practice values. Guess: the child taps the one with the larger area. The child drags D onto E. Result: D clicks inside E, strip "D fits inside E, so the area of E is larger." Help: guided, a corner dot shows where the corners meet.
- Activity 2 (guided). Goal line: "Lay D on F. Then count the squares." Goal chip: "Count to compare". Setup: D (6 by 2) and F (3 by 5). Guess: "Which has the larger area? Tap D, F or Can't tell by laying." The child lays D on F: D sticks out sideways, F sticks out at the top, strip "Neither shape fits inside the other. Count unit squares." The child drags both onto the grid and counts row by row. Result: "D: 2 rows of 6, 6 × 2 = 12. F: 5 rows of 3, 3 × 5 = 15. F has the larger area, though D is longer." Help: guided, rows numbered.
- Activity 3 (independent). Goal line: "Count the whole squares. Then put the half squares in pairs." Goal chip: "Find the area". Setup: a house on the grid, 4 columns wide: 2 rows of 4 whole squares, then a roof whose lower row is a half square, 2 whole squares and a half square, and whose top row is 2 half squares (10 whole and 4 half squares). Guess: "How many square cm is the house? Tap one: 10, 12 or 14." The child counts the whole squares, then joins the half squares in pairs. Result: "10 whole squares. 4 half squares make 2 squares, 4 ÷ 2 = 2. 10 + 2 = 12. The area is 12 square cm." Help: independent.
- Star Challenge 1 (book questions in order, on A, B and C). Goal line: "Which of the above rectangles has the largest area? Trace these shapes on to a paper and cut them to find out the one that has the largest area." Goal chip: "A, B or C?" Setup: cut-outs A, B, C on the table, no grid. Guess: the child taps the one they think is largest. Step 1a: "Do you see that the area of rectangle A is larger than that of B? What about B and C?" The child lays B on A and B on C (B fits inside both), then taps Yes and Yes. Step 1b: "Which shape has a larger area among A and C? How will you find out?" The child lays A on C (neither fits) and taps "Count unit squares on a grid" among 3 method chips. Step 1c: "Let us put these rectangles on a square grid. Now, can you identify the rectangle that has the largest area?" The child drags A, B, C onto a grid of 11 columns by 5 rows, counts, and taps the largest. Result: "A has 3 × 4 = 12 unit squares, C has 2 × 5 = 10 and B has 2 × 4 = 8. 12 is the most, so A has the largest area." Help: independent.
- Star Challenge 2. Goal line: "Compare the areas of the two gardens given below on the square grid. Share your observations. Area of Garden A: ___ square cm. Area of Garden B: ___ square cm." Goal chip: "Two gardens". Setup: a grid 7 columns by 6 rows of 1 cm squares: garden A green, 2 wide and 5 tall; a pale strip 1 square wide beside it, part of neither garden; garden B green, 4 wide and 3 tall. Guess: the child taps the garden they think is larger. The child counts each garden by rows and sets two dials: 10 and 12. Then taps "Garden B is larger by 2 square cm" among 3 chips. Result: "Garden A: 5 rows of 2, 5 × 2 = 10. Garden B: 3 rows of 4, 3 × 4 = 12. 12 − 10 = 2, so garden B is larger by 2 square cm. The pale strip is part of neither garden." Help: independent.
- Star Challenge 3. Goal line: "Trace your palm on the square grid given below and find the approximate area of your palm. Compare the area of your palm with your friend's palm. Who has a bigger palm?" Goal chip: "Trace and count". Setup: an empty grid of 15 by 12 squares. Guess: the child taps "Mine" or "My friend's" as the bigger palm. The child draws a palm outline, counts the whole squares and joins the part squares in pairs (a lone part square is left out); a friend does the same in another colour. Result: the strip shows the real numbers, for example "54 whole squares and 12 part squares: 12 ÷ 2 = 6, 54 + 6 = 60. About 60 square cm. 60 is more than 48, so this palm is bigger." The child taps who is bigger. Help: independent.
- Star Challenge 4 (practice values). Goal line: "Collect leaves of different kinds. Put them on a square grid and find their area. (a) Name the leaf with the largest area. (b) Name the leaf with the smallest area." Goal chip: "Leaves P, Q, R". Setup: three leaf photos P, Q, R. The outline of each, drawn in code over the photo, gives exactly P 24 whole and 12 part squares, Q 12 whole and 12 part, R 18 whole and 12 part (the builder checks). Guess: the child taps the leaf they think is largest. The child drags each leaf to the grid, counts, joins the part squares in pairs, then taps the largest leaf for (a) and the smallest for (b). Result: "P: 12 ÷ 2 = 6, 24 + 6 = 30. R: 18 + 6 = 24. Q: 12 + 6 = 18. The largest is leaf P and the smallest is leaf Q." Help: independent.

5. Mathematical Understanding
- Laying shows that a shape that fits inside the other has the smaller area, and that long is not the same as large. When neither fits, counting the same small squares decides. Two half squares make one whole square.
- Rules in the child's words: "If one fits inside the other, it has the smaller area." "If neither fits, count the same unit squares." "The area is the number of unit squares it covers."

6. Feedback and Hints
- Correct: the goal chip turns green with a gentle bounce and the strip shows the why. Wrong answer: red strip, small shake, one friendly line; retry is free, no scores. Confetti only on the end screen. Guesses are never marked wrong: a plain strip says "You guessed X. The answer is Y."
- Mistake: C is larger because it is taller -> "C is taller, but A is wider. Count the squares of each." Both sides pulse. B larger than A -> "B fits inside A. The shape that fits inside has the smaller area."
- Mistake: counts the pale strip -> "The pale strip is not part of a garden. Do not count it." A square tapped twice -> "You counted this square already."
- Mistake: 14 for the house -> "Two half squares make 1 square, not 2." 10 -> "The half squares are part of the house. Put them in pairs." The pairs link.
- Hints, three levels: (1) "Does one shape fit inside the other? Try laying one on the other." or "What can you count that is the same size in both?" (2) the first row is numbered, or the half squares link in pairs; (3) "A is 3 columns and 4 rows: 3 × 4 = 12. C is 2 columns and 5 rows: 2 × 5 = 10."
- Edge cases: equal areas ("Same area: 12 and 12"); a shape fits inside even when edges touch; an open outline asks "Close the outline."

7. Ending
- End screen: "Well done!" Remember: "If one shape fits inside the other, it has the smaller area." "If neither fits, count the same unit squares." "Two half squares make one whole square." Think and talk: "Is the longer rectangle always the one with the larger area? Why not?" Button: "Start again".

8. Assets and Language
- Images: top-view wood craft table photo; paper texture; three leaf photos with clean edges (mango-type, round, narrow). Grid sheet, house, gardens, rectangles and outlines in code.
- Language: English only.
""".strip("\n"),

    "M2.S11.T11.C47.2D1": """
A. TOOL TITLE
- Shape Builder

B. TOOL INFO
- Tool ID: M2.S11.T11.C47.2D1
- Tool type: Concept-activity
- Textbook source: Grandmother's Quilt, Area and Perimeter Are Different: the mats, Trisha's rectangles, the Let Us Explore shapes, the 9 by 2 shape, the 3 by 3 square and the triangle. Practice values added: 7 by 2, 5 by 4, 10 by 2, perimeter 24 (developer only).

C. LEARNING OBJECTIVE
- The student sees that area counts the squares inside a shape and perimeter counts the edges round the outside, so one can stay the same while the other changes.
- Out of scope: the rules length × breadth and 2 × length + 2 × breadth.

D. TOOL DESCRIPTION

1. Opening Screen
- A wooden building board seen from above with a grid of 15 columns by 12 rows of 1 cm squares, each about 40 px, and a 7 by 2 rug of orange patches at the upper left. Two chips above the grid: "Area ?" (orange) and "Perimeter ?" (dark grey).
- Instruction line: "Count the squares inside. Then count the edges round the outside."
- The child is invited to tap Same or Different (the first guess).

2. Scene and Objects
- Wooden board photo, top view, pale grid lines. Patches: orange fabric squares with a thin seam. The outer edges of a shape are a thick dark line.
- Shelf of 3 slots along the bottom; a saved shape shows as a small copy with its numbers, for example "A 20, P 18". Small stage buttons: Save, Clear, Undo.

3. Main Interaction
- Tap a square to place a patch, tap again to remove it; drag across squares to place several. Patches must touch along a whole edge and leave no hole, else a plain note says so.
- The Area and Perimeter chips update live. On shapes the tool shows, trace: drag a finger round the outline; each outer edge passed lights up with a running count, and the number stays on the shape when the loop closes. Drag across a shape to count its squares. Tap a shape to tick it; tap answer chips.
- Bottom buttons (at most 3): Hint, Reset (clears this step), Check, which becomes Next.

4. Activities
- Activity 1 (guided). Goal line: "Count the squares inside. Then count the edges round the outside." Goal chip: "Area and perimeter". Setup: the 7 by 2 rug; chips show "?". Guess: "Will Area and Perimeter be the same number? Tap Same or Different." The child counts the squares by dragging and traces the outline. Result: "Area 14: 2 rows of 7, 7 × 2 = 14. Perimeter 18: 7 + 2 + 7 + 2 = 18. They are two different measures." Help: guided, squares inside glow orange.
- Activity 2 (guided). Goal line: "Build two rectangles that each have 20 squares." Goal chip: "Area 20, twice". Setup: faint dotted outlines of 5 by 4, then 10 by 2; the child fills each and presses Save. Guess: after the first save, "Will the next one have the same perimeter? Tap Same or Different." Result: "Both have 20 squares: 5 × 4 = 20, 10 × 2 = 20. The perimeters are 5 + 4 + 5 + 4 = 18 and 10 + 2 + 10 + 2 = 24. Same area, different perimeters." Help: guided, dotted outlines.
- Activity 3 (independent). Goal line: "Build three different rectangles that each have a perimeter of 24." Goal chip: "Perimeter 24, three times". Setup: empty board. Guess: "Will rectangles with the same perimeter have the same area? Tap Same or Different." The child builds until Perimeter reads 24 and saves; any three different rectangles are right (a turned copy is the same). Result, for example 10 by 2, 9 by 3, 7 by 5: "All three have perimeter 24: 7 + 5 + 7 + 5 = 24. The areas are 20, 27 and 35. Same perimeter, different areas." Help: independent.
- Star Challenge 1 (two parts). Part 1a goal line: "The following mats are made of square patches of equal size. How many square patches will be required to cover each mat? Would both mats require an equal or different number of patches? Trace and cut out a small square of the size given below and find the area. (a) Area = ___ Perimeter = ___ (b) Area = ___ Perimeter = ___" Goal chip: "Two mats". Setup: mat (a) 5 long and 2 broad, mat (b) 4 long and 3 broad, empty outlines each with one 1 cm patch at its top left corner. Guess: the child taps Equal or Different for the number of patches. The child fills each mat (Area fills in), traces each outline (Perimeter fills in) and taps Equal or Different again. Right: Different. Result: "Mat (a): 5 × 2 = 10 patches, perimeter 5 + 2 + 5 + 2 = 14 cm. Mat (b): 4 × 3 = 12 patches, perimeter 4 + 3 + 4 + 3 = 14 cm. Different patches, same perimeter." Part 1b goal line: "Trisha makes these two rectangles. She says, "I increased the area of my rectangle, and the perimeter increased." Do you think this is always true?" The child builds Trisha's rectangles, 2 by 3 (Area 6, Perimeter 10) and 3 by 4 (Area 12, Perimeter 14), taps Always true or Not always true, then builds and saves two rectangles where the area goes up and the perimeter does not. Right: Not always true. Result, for example 10 by 1 then 5 by 3: "10 by 1: area 10, perimeter 10 + 1 + 10 + 1 = 22. 5 by 3: area 15, perimeter 5 + 3 + 5 + 3 = 16. The area went up and the perimeter went down, so it is not always true." Help: independent.
- Star Challenge 2. Goal line: "Tick the shapes with the same area. Find the perimeters of these shapes. What do you notice? Discuss." Goal chip: "Same area". Setup: six green shapes (wide by tall): (a) 6 by 2; (b) a 2 by 5 block with a row of 2 on top, shifted one square left; (c) 3 by 4; (d) 4 by 3; (e) a row of 8; (f) a row of 12. The child ticks the shapes with the same area (the guess) and presses Check; right: (a), (b), (c), (d), (f). Then traces each ticked outline; right: 16, 18, 14, 14, 26. Then taps "Same area, different perimeters" among 3 chips. Result: "These five cover 12 square cm each, but their perimeters 16, 18, 14, 14 and 26 differ." Help: independent.
- Star Challenge 3. Goal line: "Tick the shapes with the same perimeter. Find the areas of these shapes. What do you notice? Discuss." Goal chip: "Same perimeter". Setup: five pink shapes of 7 squares: (a) 3 by 2 with 1 square under its right end; (b) a row of 3 over a 2 by 2 block, sticking out right; (c) a column of 4 with a square on each side of its third square and one right of its top square; (d) a column of 5 with 2 more to the right of its bottom square; (e) a row of 7. The child traces each outline (12, 12, 16, 16, 16), then ticks one group and presses Check, then the other; right: (a) and (b); (c), (d) and (e). Then drags across each shape to count its squares (7) and taps "All areas are 7, the perimeters are not all the same" among 3 chips. Result: "Every shape has an area of 7 square cm, but the perimeter is 12 cm for two shapes and 16 cm for three." Help: independent.
- Star Challenge 4 (two parts). Part 4a goal line: "Draw different shapes having the same area as the given shape. Write the perimeter of each shape. What do you notice? Discuss." Setup: a given green rectangle 9 wide and 2 tall (Area 18, Perimeter 22). The child builds and saves 2 different shapes of exactly 18 squares (a turned 9 by 2 does not count). Result, for example 6 by 3: "All have 18 squares. The perimeters are 22 and 6 + 3 + 6 + 3 = 18. Same area, not the same perimeter." Part 4b goal line: "Is the area of shape (a) less than the area of shape (b) given below? Discuss." Setup: (a) a blue square 3 by 3, (b) an orange triangle with a top side of 6 squares and its point 3 squares below the middle. The child counts (a), taps the 6 whole squares of (b), joins its 6 half squares in 3 pairs and taps Yes or No. Right: No. Result: "(a): 3 × 3 = 9. (b): 6 whole squares and 6 ÷ 2 = 3 more, 6 + 3 = 9. The areas are equal." Help: independent.

5. Mathematical Understanding
- Reading both numbers while building shows the child that they move differently.
- Rules in the child's words: "Area counts the squares inside. Perimeter counts the edges round the outside." "The same area can have different perimeters." "A bigger area does not always mean a bigger perimeter."

6. Feedback and Hints
- Correct: the goal chip turns green with a gentle bounce and the strip shows the why. Wrong answer: red strip, small shake, one friendly line; retry is free, no scores. Confetti only on the end screen. Guesses are never marked wrong: a plain strip says "You guessed X. The answer is Y."
- Mistake: ticks (e) -> "Shape (e) has 8 squares, not 12. Count its squares again." Its squares light up with a count. Leaves out (f) -> "Count the squares of every shape, even the thin ones."
- Mistake: the loop skips an edge -> "Go all the way round. An edge was left out." It blinks. An inside edge -> "That edge is inside. Count only the outside edges."
- Mistake: a Trisha pair where the perimeter also goes up -> "Here the perimeter went up too. Try a pair where it stays the same or goes down." The given shape turned round -> "That is the same shape turned round. Make a different one."
- Hints, three levels: (1) "What does each number count? Area counts the squares inside. Perimeter counts the edges round the outside." (2) the squares inside glow orange, or the outline runs once round with a counter; (3) "For 5 by 4: 5 × 4 = 20 squares, and 5 + 4 + 5 + 4 = 18 edges." Trisha: "Try 10 by 1, then 5 by 3."
- Edge case: a single patch (Area 1, Perimeter 4).

7. Ending
- End screen: "Well done!" Remember: "Area counts the squares inside. Perimeter counts the edges round the outside." "Shapes with the same area can have different perimeters." "A bigger area does not always mean a bigger perimeter." Think and talk: "Can two rectangles have the same perimeter and different areas? Show one pair." Button: "Start again".

8. Assets and Language
- Images: top-view wooden board photo; orange fabric patch texture. Grid, shapes and chips are drawn in code.
- Language: English only.
""".strip("\n"),

    "M2.S15.T15.C63.2D1": """
A. TOOL TITLE
- Rectangle Maker

B. TOOL INFO
- Tool ID: M2.S15.T15.C63.2D1
- Tool type: Concept-activity
- Textbook source: Grandmother's Quilt, Area and Perimeter of Rectangles and Squares: the 6 by 4 patchwork, the earlier rectangles, the square of side 5, the five shapes, the classroom floor, perimeters 26 cm and 18 cm. Practice values added: 9 by 3, 10 by 4, a square of 9, perimeter 36, a floor of 8 m by 6 m (developer only).

C. LEARNING OBJECTIVE
- The student finds the area of a rectangle as rows times patches in a row (length × breadth) and its perimeter by adding the four sides, and sees that a square is a rectangle with equal sides.
- Out of scope: missing sides from a given area, sides given in parts, comparing two areas.

D. TOOL DESCRIPTION

1. Opening Screen
- A wooden rug-maker's frame on a table, seen from above: an empty rectangle 9 squares long and 3 broad, each square about 40 px, with side labels "9 cm" and "3 cm". A round handle sits on its bottom right corner; fabric patches lie beside it.
- Instruction line: "How many patches will cover the frame? Make a guess."
- The child is invited to tap one of three guess chips below the frame.

2. Scene and Objects
- Frame: dark wood border, pale cloth inside, the largest object, on a wooden table photo. Patches: 1 cm fabric swatches in 3 colours. A "Square" badge lights when length and breadth are equal. A red marker for walking the border, with a running-sum chip such as "10 + 4 = 14".

3. Main Interaction
- Drag the corner handle: length (across) and breadth (down) go from 1 to 12 cm, snapping to whole cm; a locked side shows a padlock. Tap the frame to lay one row of patches; tap a row to take it away.
- Drag the marker round the border: at each corner the running sum adds the side just walked.
- Number dial: 1 to 3 wheels, swipe up or down. Guess chips: tap one. Save: a small stage button puts the frame on a shelf of 4 slots.
- Bottom buttons (at most 3): Hint, Reset (returns this step), Check, which becomes Next.

4. Activities
- Activity 1 (guided). Goal line: "Lay the rows and count the patches." Goal chip: "Area". Setup: frame 9 long, 3 broad (practice values). Guess: "How many patches? Tap one: 12, 24 or 27." The child taps the frame 3 times, one row each. Result: "3 rows of 9 patches: 3 × 9 = 27. The length is 9 and the breadth is 3, so the area is 9 × 3 = 27 square cm." Help: guided, side labels and a row counter.
- Activity 2 (guided). Goal line: "Walk round the border and add the sides." Goal chip: "Perimeter". Setup: a full frame 10 long, 4 broad. Guess: "How far is it all the way round? Tap one: 14, 28 or 40." The child drags the marker round. Result: "10 + 4 + 10 + 4 = 28. Opposite sides are equal: 2 × 10 = 20, 2 × 4 = 8, 20 + 8 = 28 cm." Help: guided, each side lights as it is walked.
- Activity 3 (guided, then free). Goal line: "Drag the corner until all four sides are equal." Goal chip: "Make a square". Setup: frame 9 long (locked), 5 broad. Guess: "Which gives the perimeter of a square? Tap 4 × side or side × side." The child drags the breadth to 9; the Square badge lights. Result: "A square has 4 equal sides. Area: 9 × 9 = 81 square cm. Perimeter: 4 × 9 = 36 cm." Help: badge shown.
- Activity 4 (independent). Goal line: "The border is 36 cm and the length is 10 cm. Find the breadth." Goal chip: "Perimeter 36". Setup: length locked at 10, breadth free. Guess: "What is the breadth? Tap one: 8, 16 or 26." The child drags the handle and presses Check, which walks the border. Result: "Half of 36 is 36 ÷ 2 = 18, so length + breadth = 18. 18 − 10 = 8. The breadth is 8 cm. Check: 10 + 8 + 10 + 8 = 36." Help: independent.
- Star Challenge 1 (two parts). Part 1a goal line: "Preetha and Adrit's grandmother is making another square patchwork. She arranges the patches as shown below. Can you guess how many patches she will need? How did you find it?" Goal chip: "Guess the patches". Setup: a frame 4 across and 6 down; only the top row and left column hold pink patches; sides labelled 6 and 4. Guess: tap one: 9, 10 or 24; then "How did you find it?": tap "I counted one by one", "6 rows of 4: 6 × 4" or "6 + 4" (right: 24 and the middle one). The child taps the frame to lay the rows. Result: "6 rows of 4 patches: 6 × 4 = 24. Area = Length × Breadth = 6 × 4 = 24 square cm." Part 1b goal line: "Go back to the previous examples and check whether the product of the length and the breadth of the rectangles is the same as the area you had calculated by counting." Setup: seven cards in a row, each a rectangle with sides and counted area: A 3 by 4 (12), B 2 by 4 (8), C 2 by 5 (10), garden A 2 by 5 (10), garden B 4 by 3 (12), mat (a) 5 by 2 (10), mat (b) 4 by 3 (12). Guess: "Will the product match the count every time? Tap Yes or No." The child turns each card over: it shows the product and a green tick, for example "3 × 4 = 12". Result: "Yes. For every rectangle, length × breadth is the area counted." Help: independent.
- Star Challenge 2. Goal line: "All the sides of a rectangle are equal, that is, the case of a square. Think about a square whose sides are 5 units long. What are its area and its perimeter?" Goal chip: "Square of side 5". Setup: an empty square frame, every side 5 cm, locked. The child may lay rows or walk the border, then sets two dials (the guess is the dials before Check): 25 and 20. Result: "Area = 5 × 5 = 25 square cm. Perimeter = 4 × 5 = 20 cm." Help: independent.
- Star Challenge 3. Goal line: "Find the area and perimeter of the following shapes." Goal chip: "Five shapes". Setup: a 1 cm grid sheet with five orange shapes (wide by tall): (a) 6 by 6, (b) 4 by 7, (c) 12 by 4, (d) 3 by 3, (e) 6 by 5, each with two arrows. The child taps a shape, drags its two arrows along the sides (they snap and show cm), then sets dials Area and Perimeter (the guess is the dials before Check). Right: (a) 36 and 24, (b) 28 and 22, (c) 48 and 32, (d) 9 and 12, (e) 30 and 22. Result line for each, for example "(b) 4 × 7 = 28, 4 + 7 + 4 + 7 = 22." and "(a) a square: 6 × 6 = 36, 4 × 6 = 24." Help: independent.
- Star Challenge 4 (practice values). Goal line: "Find the area of your classroom floor in square meters. Take the help of your teacher to measure the length and breadth of the floor. What is the perimeter of the classroom floor?" Goal chip: "Classroom floor". Setup: a tiled classroom floor seen from above, 8 m long and 6 m broad, and a measuring tape: the child drags its end along each wall (snaps to whole metres). Guess: before measuring, tap the length: 5 m, 8 m or 12 m. Then two dials; right: 48 and 28. Result: "Area: 8 × 6 = 48 square m. Perimeter: 2 × 8 = 16, 2 × 6 = 12, 16 + 12 = 28 m. Your own classroom may give a different answer." Help: independent.
- Star Challenge 5. Goal line: "Draw two rectangles each having the following perimeters. (a) 26 cm (b) 18 cm" Goal chip: "Perimeter 26, then 18". Setup: the frame with both sides free. Guess: "For a perimeter of 26, length + breadth must be? Tap one: 13, 26 or 52." The child makes and saves two different rectangles with perimeter 26, then two with 18 (a live chip shows the perimeter); any different rectangles are right. Result: "Half of 26 is 26 ÷ 2 = 13: 8 + 5 + 8 + 5 = 26. Half of 18 is 18 ÷ 2 = 9: 6 + 3 + 6 + 3 = 18. Your answer may differ." Help: independent.

5. Mathematical Understanding
- Laying rows shows area as rows times patches in a row; walking the border shows that opposite sides are equal.
- Rules in the child's words: "Area is length times breadth." "Perimeter is 2 lengths and 2 breadths." "A square has area side times side and perimeter 4 times side."

6. Feedback and Hints
- Correct: the goal chip turns green with a gentle bounce and the strip shows the why. Wrong answer: red strip, small shake, one friendly line; retry is free, no scores. Confetti only on the end screen. Guesses are never marked wrong: a plain strip says "You guessed X. The answer is Y."
- Mistake: perimeter as length + breadth -> "That adds only 2 sides. Add all four." The missing sides blink.
- Mistake: area and perimeter swapped -> "Area counts the patches inside. Perimeter adds the sides round the outside." The patches inside glow.
- Mistake: square area as 4 × side or perimeter as side × side -> "For a square the area is side × side and the perimeter is 4 × side."
- Mistake: breadth 26 in Activity 4 -> "36 − 10 = 26 takes away only one length. First halve 36." In Challenge 5, a wrong perimeter -> "This rectangle has a perimeter of 28. Make it 26." (the real number).
- Hints, three levels: (1) "Is it about the patches inside, or the edge all the way round?" (2) the patches inside glow orange, or the border lights side by side; (3) "Area: rows times patches in a row. Perimeter: 2 lengths and 2 breadths. Half of the perimeter is length + breadth."
- Edge cases: a 1 by 1 frame (area 1, perimeter 4); a rectangle and its turned copy count as one.

7. Ending
- End screen: "Well done!" Remember: "Area of a rectangle is length × breadth." "Perimeter of a rectangle is 2 × length + 2 × breadth." "A square has area length × length and perimeter 4 × length." Think and talk: "A rectangle has a perimeter of 30 cm. Can its length be 20 cm? Why not?" Button: "Start again".

8. Assets and Language
- Images: top-view light wood table photo; dark wooden frame; fabric swatch cut-outs; tiled classroom floor photo; measuring tape cut-out. Shape sheet, grid, badges and dials in code.
- Language: English only.
""".strip("\n"),

    "M3.S21.T21.C88.2D1": """
A. TOOL TITLE
- Perimeter 24 Game

B. TOOL INFO
- Tool ID: M3.S21.T21.C88.2D1
- Tool type: Puzzle
- Textbook source: Grandmother's Quilt, Let Us Play: the 4 tiles (a row of 3 and one below the left tile, perimeter 10), 5 tiles after a die of 1 (perimeter 12), 11 tiles after a die of 6 (perimeter 24). Practice values added: a row of 6, a 2 by 2 square, an L of 3, a target of 18 (developer only).

C. LEARNING OBJECTIVE
- The student finds the perimeter of a figure of square tiles by counting its outer edges, and plans where to add tiles so that the perimeter becomes exactly 24.
- Out of scope: the rules 2 × length + 2 × breadth and 4 × length, area.

D. TOOL DESCRIPTION

1. Opening Screen
- A green felt play mat on a floor, seen from above. In the middle lies a row of 6 pink square tiles, each about 70 px, every outer edge marked with a small "1". A wooden die stands at the right and a pile of loose pink tiles at the left. A chip "Perimeter: ?" sits above the figure.
- Instruction line: "How many outer edges does this row of tiles have? Make a guess."
- The child is invited to tap one of three guess chips.

2. Scene and Objects
- Felt play mat on a wooden floor photo, top view. Tiles: pink squares with a slim darker edge and soft shadow, each side 1 unit. Die: a wooden die photo that tumbles and lands on a face from 1 to 6.
- Edge marks: a small "1" beside every outer edge, none on a shared edge; a counted edge turns orange.
- Chips: the perimeter chip (for example "Perimeter: 12"), "Tiles: 5", and in the game "12 more to 24". The banner "Make the perimeter 24" and player tags "Player 1" and "Player 2" appear only in Star Challenge 2; the tag of the player whose turn it is glows.

3. Main Interaction
- Drag a tile from the pile onto the mat. It snaps to the grid and must touch the figure along a whole edge; if it touches only at a corner or not at all, it slides back. A placed tile cannot be moved. A small Undo arrow takes back only the tiles of this turn.
- Tap an outer edge to count it (orange, counter goes up by 1). Tapping the die or Roll rolls it.
- Number dial: 1 to 3 wheels, swipe up or down. Guess chips: tap one.
- Bottom buttons (at most 3): Hint, Reset (clears the figure of this step), and one main button that reads Roll, Done, Check or Next as the step needs.

4. Activities
- Activity 1 (guided). Goal line: "Tap every outer edge. Each tile side is 1." Goal chip: "Count the edges". Setup: a row of 6 tiles (practice values). Guess: "How many outer edges? Tap one: 6, 14 or 24." The child taps the 14 outer edges. Result: the perimeter chip shows 14 and the strip says "6 on the top, 6 on the bottom, 1 at each end: 6 + 6 + 1 + 1 = 14. The perimeter is 14." Help: guided, edges are marked 1 and a running count shows.
- Activity 2 (guided). Goal line: "Add 1 tile that touches the square along 1 edge." Goal chip: "Tile on 1 edge". Setup: a square of 2 by 2 tiles, perimeter 8. Guess: "What happens to the perimeter? Tap one: 4 more, 2 more or the same." The child drags 1 tile to touch one edge. Result: perimeter 10, strip "This tile touches 1 edge. 3 new edges show and 1 old edge is hidden: 8 + 3 − 1 = 10. The perimeter is 2 more." Help: guided, the 3 new edges glow orange and the hidden edge turns grey.
- Activity 3 (guided, then free). Goal line: "Add 1 tile in the corner where the two arms meet." Goal chip: "Tile in a corner". Setup: 3 tiles placed like the letter L, perimeter 8. Guess: "What happens now? Tap one: 2 more, the same or 2 less." The child drags a tile into the corner. Result: the figure becomes a 2 by 2 square, perimeter 8, strip "This tile touches 2 edges. 2 new edges show and 2 old edges are hidden: 8 + 2 − 2 = 8. The perimeter stays the same." Help: the touched edges flash, no counts.
- Activity 4 (independent). Goal line: "Add tiles to the square until the perimeter is exactly 18." Goal chip: "Perimeter 18". Setup: the square of 2 by 2 tiles, perimeter 8, the pile open. Guess: "How many more edges do you need? Tap one: 10, 18 or 26." The child adds tiles in any way and presses Check when the chip shows 18. Any figure with exactly 18 outer edges is right. Result, for example 5 tiles each on 1 edge: "18 − 8 = 10 more. Each tile on 1 edge adds 2: 5 × 2 = 10, and 8 + 10 = 18." Help: independent, only the goal chip and the chip with the count.
- Star Challenge 1. Goal line: "Find the perimeter of the tiles." Goal chip: "Perimeter of the tiles". Setup: 4 tiles, a row of 3 and one tile below the left tile, every outer edge marked 1. Guess: the child sets a dial to the number they expect before tapping. The child then taps each outer edge and presses Check. Right: 10 edges, and the dial equals 10. Result: "3 on the top, 1 on the right, 2 under the top row, 2 round the lower tile's right and bottom, 2 on the left: 3 + 1 + 2 + 2 + 2 = 10. Check: 4 tiles have 4 × 4 = 16 edges, 3 places where tiles touch hide 2 edges each, 3 × 2 = 6, and 16 − 6 = 10." Help: independent.
- Star Challenge 2 (the game, three parts). Banner "Make the perimeter 24". Part 2a goal line: "Do not move the tiles. The second player can take turn and add tiles to the same tiled figure." Goal chip: "Add 1 tile". Setup: the 4 tiles, the die shows 1 as in the book (the child rolls and it lands on 1). Guess: "What will the perimeter be? Tap one: 10, 12 or 14." The child adds 1 tile along 1 edge. Result: 5 tiles, perimeter 12, strip "10 + 2 = 12. A tile on 1 edge makes the perimeter 2 more." Part 2b goal line: "Take turns and add tiles to the same figure till the perimeter becomes 24. The one who makes the perimeter 24 wins the game." Goal chip: "Reach 24". Setup: the 5 tiles, the die shows 6. Guess: "Can 6 tiles make exactly 24? Tap Yes or No." The child adds 6 tiles, each touching the figure along 1 edge, then presses Done. Result: 11 tiles, perimeter 24, a ribbon star on the player tag, strip "11 tiles have 11 × 4 = 44 edges. 10 places where tiles touch hide 2 edges each: 10 × 2 = 20. 44 − 20 = 24. This player wins." Part 2c, a free game: the child taps "Play with a friend" or "Play against the tool". Setup: the 4 tiles, perimeter 10. Players take turns: Roll, place every tile of the die number, press Done. A player wins when, after the last tile of their turn, the chip shows exactly 24. The tool, on its turn, rolls and places each tile on 1 edge (+2) if that keeps the perimeter at 24 or less, otherwise in a notch on 2 edges (+0) if one exists, otherwise on 1 edge, choosing at random, one tile at a time. Result: the winner's tag gets the ribbon, strip "This figure has 24 outer edges. Player 1 wins." Help: independent.

5. Mathematical Understanding
- Counting outer edges shows that the perimeter of tiles is the edges that are not shared. Adding tiles one at a time shows what each tile does: a tile on 1 edge adds 2, a tile in a corner on 2 edges adds nothing, a tile in a notch on 3 edges takes 2 away.
- Rules in the child's words: "The perimeter of tiles is the number of outer edges." "A tile on 1 edge makes it 2 more." "A tile on 2 edges leaves it the same."

6. Feedback and Hints
- Correct: the goal chip turns green with a gentle bounce and the strip shows the why. Wrong answer: red strip, small shake, one friendly line; retry is free, no scores. Confetti only on the end screen. Guesses are never marked wrong: a plain strip says "You guessed X. The answer is Y." For a guess of 4 more: "A tile on 1 edge hides 1 edge and shows 3 new ones: 3 − 1 = 2 more."
- Mistake: taps a shared edge -> "This edge is shared by two tiles. It is inside, so do not count it." The shared edge flashes.
- Mistake: a tile put where it touches only at a corner -> it slides back: "Place the tile so that it touches the figure along a whole edge."
- Mistake: tries to move a placed tile -> "Tiles cannot be moved. Use Undo to take back this turn's tiles."
- Mistake: Check in Activity 4 with a wrong perimeter -> "The perimeter is 16. You need 18." In Part 2b, not 24 after 6 tiles -> "The perimeter is 22. Undo and put every tile on 1 edge only." The tiles on 2 edges flash.
- Past 24: a plain note, no red strip: "Past 24. A tile in a notch on 3 edges makes it 2 less."
- Hints, three levels: (1) "Which edges are on the outside? An edge shared by two tiles is inside." or "Does the new tile touch the figure along 1 edge or along 2 edges?" (2) the shared edges turn grey and the outside edges stay bright, or the touched edges flash; (3) "A tile on 1 edge makes it 2 more, on 2 edges the same. To reach 24 from 12 you need 12 more: 6 tiles on 1 edge each."
- Edge cases: a tile on 3 edges makes the perimeter 2 less, on 4 edges 4 less; 24 in the middle of a turn does not win, only 24 after the last tile.

7. Ending
- End screen: "Well done!" Remember: "The perimeter of tiles is the number of outer edges." "A tile on 1 edge makes the perimeter 2 more." "A tile on 2 edges leaves the perimeter the same." Think and talk: "You are at 22 and the die shows 1. Where will you put the tile to win?" Button: "Start again".

8. Assets and Language
- Images: top-view green felt mat photo; wooden floor photo; pink square tile cut-outs; wooden die photo with six faces; small ribbon star. Edge marks, chips and counters in code.
- Language: English only.
""".strip("\n"),

}

OBJECTIVES = {
    "M1.S1.T1.C2.2D1": "The student understands that lace for a border must go all the way round the quilt, and that its length is found by adding the units along every side, not by counting patches.",
    "M1.S5.T5.C13.2D1": "The student understands that squares, rectangles and triangles cover a surface with no gaps and no overlaps while circles do not, and that area is the number of tiles that cover it, named in the unit of the tile.",
    "M1.S8.T8.C30.2D1": "The student understands how to compare two areas by laying one shape on the other when one fits inside, and by counting the same unit squares on a grid when neither fits.",
    "M2.S11.T11.C47.2D1": "The student understands that area counts the squares inside a shape and perimeter counts the edges round it, so one can stay the same while the other changes.",
    "M2.S15.T15.C63.2D1": "The student understands that the area of a rectangle is length times breadth and its perimeter is two lengths plus two breadths, and that a square is a rectangle with equal sides.",
    "M3.S21.T21.C88.2D1": "The student understands that the perimeter of a figure of square tiles is the number of its outer edges, and how a tile added along one edge or in a corner changes it.",
}
