# -*- coding: utf-8 -*-
"""Class 5 Chapter 15 (Data Through Pictures): long-form tool descriptions in the master prompt format (17 Nov 2026).
Two dicts keyed by media_id. Every description has the headings A. to D. and 1. to 8. in order."""

DESCRIPTIONS = {
    "M1.S1.T1.C2.2D1": """A. TOOL TITLE
- Reporter's Notebook
B. TOOL INFO
- Tool ID: M1.S1.T1.C2.2D1
- Tool type: Exploration
- Textbook source: Chapter 15 Data Through Pictures, the opening topic Child TV Reporter: the notebook of 35 answers and the table with the rows 1/2 hour, 1 hour, 1 1/2 hour, 2 hours and More than 2 hours; counts 9, 13, 7, 3 and 3 read off the notebook picture (developer only). The practice notebooks of 8, 9 and 10 answers are practice values.
C. LEARNING OBJECTIVE
- The student sees that a crowd of answers becomes a table when every answer goes once into the row where it belongs, and that the counts of all the rows add up to the number of answers.
- Out of scope: "more than" and "less than" questions on a finished table, the four questions about the table (they follow the concept video), pictographs and bar graphs.
D. TOOL DESCRIPTION
1. Opening Screen
- A reporter's wooden desk seen from above, as a photo. An open spiral notebook with blue ruled lines is the largest thing on the stage. On it are 8 hand-drawn round faces, each with a white speech bubble about a thumb-width wide: 2 hr, 1 hr, 3 hr, 1 hr, 2 hr, 1 hr, 3 hr, 1 hr.
- Beside it a clipboard holds a table with the headings "No. of Hours Spent Watching TV" and "No. of Children" and three empty rows, "1 hour", "2 hours", "3 hours", each with a count box showing 0.
- Instruction line: "Every answer goes in the row where it belongs."
- The first bubble (1 hr) glows. The child is invited to tap it.
2. Scene and Objects
- Samaira (microphone) and Kabir (pen) are small flat drawings in the top-left corner, about a tenth of the stage height. They do not move or speak.
- Faces are flat pen-and-ink children, spread out so no bubble covers another. Bubble: white with a blue outline, the answer in dark handwriting-style type, readable on a tablet. A sorted bubble leaves a pale tick in its place, so no answer is counted twice.
- Table: a clipboard cut-out. Each row is about two bubbles tall; its count box is on the right. Under the table is a sum line that stays empty until every bubble is sorted.
- Goal chip at the top of the stage: "Answers left: 8", counting down to 0. A second chip "Counts add up" appears when the activity is done.
3. Main Interaction
- Drag a bubble onto a row, or tap the bubble and then the row. The bubble shrinks and slides in, the count box grows by 1 with a small pop and "Answers left" goes down by 1.
- Tap a bubble that is already in a row to send it back; the count goes down by 1 (there is no Undo button). A bubble sits in one row only; a row holds any number of bubbles.
- Bottom buttons, three only: "Reset" (sends every bubble of this activity back), "Hint", "Next" (grey until the activity is done). No typing: every answer is a moved bubble or a tapped choice.
4. Activities
- Activity 1 (guided). Goal line: "Move every answer into its row." Goal chip: "Answers left: 8". Setup: the 8 bubbles above; rows "1 hour", "2 hours", "3 hours". Guess: before the first move, "Which row will get the most answers?" with three buttons, one per row. Result: counts 4, 2 and 2; the chip turns green with a gentle bounce; the row "1 hour" pulses; the sum line shows "4 + 2 + 2 = 8". Why line: "Four bubbles say 1 hr, so the row 1 hour has 4. 4 + 2 + 2 = 8 and we had 8 answers." Help: guided; the next bubble glows and the row names use the bubbles' words.
- Activity 2 (guided). Goal line: "Sort the answers, then check the counts." Goal chip: "Answers left: 9". Setup: 9 bubbles: 1 hr, 1/2 hr, 1 1/2 hr, 1 hr, 1/2 hr, 1 hr, 1 1/2 hr, 1 hr, 1 hr; rows "1/2 hour", "1 hour", "1 1/2 hour". Guess: "The counts of the three rows will add up to..." with buttons 8, 9, 10. Result: counts 2, 5 and 2; sum line "2 + 5 + 2 = 9". Why line: "2 + 5 + 2 = 9 and there are 9 answers, so every answer is in one row, once." After a guess of 8 or 10 it adds: "The counts always add up to the number of answers, 9." Help: guided; no bubble glows, the sum line is shown.
- Activity 3 (independent). Goal line: "A row can name a group. Sort every answer." Goal chip: "Answers left: 10". Setup: 10 bubbles: 1/2 hr, 1 1/2 hr, 1 hr, 2 hr, 1/2 hr, 1 1/2 hr, 1 hr, 1 1/2 hr, 1/2 hr, 2 hr; rows "1/2 hour", "1 hour", "More than 1 hour". Guess: "Which row will the 1 1/2 hr answers go in?" with the three row names as buttons. Result: counts 3, 2 and 5; sum line "3 + 2 + 5 = 10". Why line: "1 1/2 hr and 2 hr are both more than 1 hr, so they share one row. 3 + 2 + 5 = 10." Help: independent; only Hint.
- Star Challenge 1 (independent), the opener's own task. Goal line: "Sort all 35 answers into the table." Goal chip: "Answers left: 35". Setup: 35 faces in 5 rows of 7, bubbles in hours, in this order. Row 1: 1 1/2, 1, 1, 2 1/2, 1, 2 1/2, 1 1/2. Row 2: 1/2, 1/2, 1, 1, 1 1/2, 1 1/2, 2. Row 3: 2, 1/2, 1 1/2, 1, 1/2, 1/2, 1 1/2. Row 4: 1, 1, 1/2, 1, 2, 1/2, 1. Row 5: 1 1/2, 2 1/2, 1, 1/2, 1/2, 1, 1. Table rows: "1/2 hour", "1 hour", "1 1/2 hour", "2 hours", "More than 2 hours". Guess: "Which row will have the most children?" with the five row names as buttons. Result: counts 9, 13, 7, 3 and 3; the row "1 hour" pulses; sum line "9 + 13 + 7 + 3 + 3 = 35". Why line: "9 + 13 + 7 + 3 + 3 = 35. All 35 answers are in a row, once each." The three 2 1/2 hr bubbles go in "More than 2 hours", the three 2 hr bubbles in "2 hours". Help: independent.
5. Mathematical Understanding
- Moving every bubble turns a crowd into a table; each count is read from its count box.
- The child notices: each answer goes into exactly one row (the pale tick); the counts add up to the number of answers (the sum line); a row can name one answer ("2 hours") or a group ("More than 2 hours"); 2 1/2 hr is more than 2 hr; 2 hr is exactly 2 hours, not more.
- Rule: "Every answer goes in one row. The counts add up to the number of answers."
6. Feedback and Hints
- Correct: the bubble slides in, the count box pops, "Answers left" goes down. At the end the chip turns green with a gentle bounce and the sum line joins the counts with plus signs.
- Every wrong drop: the bubble bounces back, the strip turns red, the row shakes a little, ONE line says what to look at. Retry is free.
- Mistake: any wrong row -> the strip reads the bubble, for example "This bubble says 2 hr. Find the row with the same words." The bubble's words and the right row's words glow.
- Mistake: 1/2 hr put in "1 hour" -> "1/2 hr is half an hour, not 1 hour. Look for the row 1/2 hour." That row pulses.
- Mistake: 1 1/2 hr put in "1 hour" -> "This bubble says 1 1/2 hr, not 1 hr. Look at the number in front of the fraction." The whole number glows.
- Mistake: 2 1/2 hr put in "2 hours" -> "2 1/2 hr is more than 2 hr, so it goes in the row More than 2 hours." That row pulses.
- Mistake: 2 hr put in "More than 2 hours" -> "2 hr is exactly 2 hours, not more than 2 hours. Use the row 2 hours." The same for 1 hr in "More than 1 hour".
- Mistake: tapping a ticked place in the notebook -> "This answer is already in a row. Tap it in the row to take it out." The bubble in the row pulses.
- Mistake: Next pressed with bubbles left -> "2 answers are still in the notebook." The unticked bubbles pulse.
- Hints: (1) "Read the bubble. Which row has the same words?" (2) the next unsorted bubble glows and the border of its row glows (3) the bubble floats halfway to its row with an arrow and the child lets go.
- Edge cases: an answer exactly on a row's value (1 hr, 2 hr) stays in its own row; in every activity each row ends with at least 2 bubbles, so no count box stays at 0.
7. Ending
- Star Challenge 1 above. Success: all 35 bubbles are in rows, the counts are 9, 13, 7, 3 and 3, and the sum line shows 35.
- End screen: "Well done!" Remember: "Every answer goes in one row, once." "The counts of all the rows add up to the number of answers." "A row can name a group, like More than 2 hours." Think and talk: "Which row has the most children, and what does that tell you about the friends?" Button: "Start again". A small confetti burst plays here only.
8. Assets and Language
- Images: top-view photo of a wooden desk; spiral notebook page with blue lines (cut-out); clipboard with a table (cut-out, rows and count boxes drawn by code); 35 flat pen-and-ink faces in several skin tones and hair styles with speech-bubble outlines (bubble text drawn by code); small flat drawings of Samaira with a microphone and Kabir with a pen; a pale tick. English, hours written as 1/2 hr, 1 hr, 1 1/2 hr, 2 hr and 2 1/2 hr.""",

    "M1.S4.T4.C17.2D1": """A. TOOL TITLE
- Pictograph Maker
B. TOOL INFO
- Tool ID: M1.S4.T4.C17.2D1
- Tool type: Concept-activity
- Textbook source: Chapter 15 Data Through Pictures, Stock-Taking in a Shop: Dipesh's pictograph (1 icon = 5; Toys 8, Board games 10, Sports items 12 icons) and its four questions (developer only). Other numbers are practice values.
C. LEARNING OBJECTIVE
- The student sees that one icon can stand for many items, that the number of items is the number of icons times the scale, and that a scale must fit every number with nothing left over.
- Out of scope: comparing rows, bar graphs, scales above 10.
D. TOOL DESCRIPTION
1. Opening Screen
- Joseph Uncle's toy shop, as a photo: two wooden shelves on a cream wall. A green chalkboard above the lower shelf is the pictograph board: 3 rows, each with a name on the left and an empty lane for icons.
- A small icon box (a shop sign) at the top-left of the board reads "1 icon = 5 kites". Price tags on the shelf read "Kites 15", "Puzzles 25", "Balls 45". A wooden tray under the board holds a kite, a puzzle box and a ball icon.
- Instruction line: "Show each number with icons. One icon is 5." The kite icon glows; the child is invited to drag it into the Kites row.
2. Scene and Objects
- Board: about 70% of the stage width. A lane holds up to 15 icons on one line and up to 30 on two lines. Icons are about a thumb-width wide, photo-style cut-outs; every icon in a row is the same.
- Icon box: "1 icon = ___" with the scale number and item name, always visible.
- Scale chips: round wooden buttons 2, 3, 4, 5, 6, 10 above the board. In Activities 1 and 2 only 5 is active. A chip is greyed, with the note "Too many icons. Pick a bigger scale.", when a row would need more than 30 icons.
- Fit light: a lamp beside the icon box. Green when every number gives a whole number of icons; orange when some items are left over (a leftover tile shows beside the row).
- Row read-out, right of each lane, live: "3 icons of 5 each: 3 × 5 = 15". A chip at the top counts the rows done.
3. Main Interaction
- Drag an icon from the tray into its row, or tap the row's plus button. Tap an icon in a row to take it away (there is no Undo button).
- Tap a scale chip: the icon box changes and the board redraws at once. In Activities 3 and 4 the rows draw their icons by themselves; the child places icons only in Activity 1 and Star Challenge 3.
- Tap a row's "?" tag to flip it to its number (Activity 2). Typed answers use a big answer box with a number pad (0 to 9 and delete).
- Bottom buttons, three only: "Reset" (clears this activity), "Hint", "Check" (it turns into "Next" when the activity is done).
4. Activities
- Activity 1 (guided). Goal line: "Show each number with icons. One icon is 5." Goal chip: "Rows done: 0 of 3". Setup: scale 5; tags Kites 15, Puzzles 25, Balls 45; empty rows. Guess: before the first icon, "How many icons will the kites need?" with buttons 3, 5, 15. The child places 3, 5 and 9 icons. Result: each right row turns green with "3 icons of 5 each: 3 × 5 = 15", "5 icons of 5 each: 5 × 5 = 25", "9 icons of 5 each: 9 × 5 = 45". Why line: "15 ÷ 5 = 3, so the kites need 3 icons. One icon stands for 5 kites." Help: guided; read-outs are live.
- Activity 2 (guided). Goal line: "Read each row. How many items are there?" Goal chip: "Rows read: 0 of 3". Setup: scale 5; a ready board with Robots 11 icons, Drums 1 icon, Dolls 15 icons, each with a "?" tag. Guess: for each row the child picks a number from three buttons (Robots 11, 16 or 55; Drums 1, 5 or 6; Dolls 15, 20 or 75), then taps the "?" to flip the tag. Why lines: "11 icons of 5 each: 11 × 5 = 55 robots." "1 icon stands for 5 drums, so 1 × 5 = 5 drums." "15 icons of 5 each: 15 × 5 = 75 dolls." Help: guided.
- Activity 3 (independent). Goal line: "Try a bigger scale and a smaller scale." Goal chip: "Scales tried: 0 of 2". Setup: tags Cars 70, Bears 80, Dice 90; empty board; chips 3, 4, 5, 6, 10 (chip 2 is greyed: 35 icons or more). Guess: "Which scale needs fewer icons, 5 or 10?" with two buttons. The child taps chip 10 and chip 5 and the rows draw themselves. Result: scale 10 gives 7, 8 and 9 icons; scale 5 gives 14, 16 and 18. Why line: "Scale 10 needs 7 + 8 + 9 = 24 icons and scale 5 needs 14 + 16 + 18 = 48 icons. A bigger scale needs fewer icons." Help: independent.
- Activity 4 (independent). Goal line: "Find a scale that fits all three numbers." Goal chip: "Scale that fits". Setup: Cars 70, Bears 80, Dice 90. Guess: "Will a scale of 4 fit?" with Yes and No. The child taps chip 4 (lamp orange: "With 1 icon = 4, 70 items need 17 icons and 2 items are left over. Try another scale."), then other chips until the lamp is green (5 or 10). Why line for 10: "With 1 icon = 10: 70 ÷ 10 = 7, 80 ÷ 10 = 8 and 90 ÷ 10 = 9. Nothing is left over." Help: independent.
- Star Challenge 1 (independent). Dipesh's pictograph is on the board: "1 train icon = 5 toys", "1 board game icon = 5 board games", "1 racket icon = 5 sports items"; rows Toys 8 train icons, Board games 10 board game icons, Sports items 12 racket icons. Goal chip: "Read the pictograph". The card asks, one after the other: "How many toys does Joseph Uncle have? ___" and "How many board games does Joseph Uncle have? ___" Guess: the typed number is the commitment; nothing shows until Check. Result: "Look at the icon box: 1 icon is 5 toys. 8 icons of 5 each: 8 × 5 = 40." and "10 icons of 5 each: 10 × 5 = 50." Help: independent.
- Star Challenge 2 (independent). Goal chip: "Add the rows". The card asks: "How many total play items does Joseph Uncle have? ___" The child types the total. Result: the rows flip to 40, 50 and 60. Why line: "40 + 50 + 60 = 150. Check: 8 + 10 + 12 = 30 icons, and 30 icons of 5 each: 30 × 5 = 150." Help: independent.
- Star Challenge 3 (independent, open). The card shows the book's sentence unchanged: "Is there any other scale that you can use to make the pictograph? Choose your scale and show the same data using a pictograph in your notebook." A small second line says "Build it on the empty board." Setup: empty board, tags Toys 40, Board games 50, Sports items 60, chips 2, 3, 4, 5, 6, 10. The child taps a chip (the commitment), sees the lamp, then drags icons into the rows. Result for scale 10: 4, 5 and 6 icons; why line "1 icon = 10. 40 ÷ 10 = 4, 50 ÷ 10 = 5 and 60 ÷ 10 = 6. Your answer may differ from this sample, and every scale that fits is right." For scale 2 the rows hold 20, 25 and 30 icons. Help: independent.
5. Mathematical Understanding
- One icon is a group of items. To read, count the icons and multiply by the scale; to draw, share the number into groups of the scale.
- Changing the scale shows that a bigger scale needs fewer icons, and that a number that does not share into groups leaves items over.
- Rules: "Number of items = number of icons × the scale." "A bigger scale needs fewer icons."
6. Feedback and Hints
- Correct: the row turns green with its number sentence; the goal chip bounces and turns green. Every wrong answer: red strip, a small shake, ONE friendly line, free retry.
- Mistake: one icon for every item (15 icons for 15 kites) -> "15 is the number of kites, not the number of icons. One icon stands for 5 kites." The icon box glows. A full row (30 icons) says "This row is full."
- Mistake: too many icons -> "You put 4 icons for 15 kites. 4 icons of 5 each: 4 × 5 = 20, but there are 15 kites." Too few -> "You put 2 icons for 15 kites. 2 icons of 5 each: 2 × 5 = 10, so 15 kites need more icons."
- Mistake: typing the number of icons (8 for the toys) -> "8 is the number of icons. One icon stands for 5 toys, so multiply the icons by 5." The toys row glows. Typing 30 for the total -> "30 is the number of icons. Each icon stands for 5 items. How many items do 30 icons stand for?"
- Mistake: guessing that scale 5 needs fewer icons than scale 10 -> "Look again. With a bigger scale each icon stands for more items, so fewer icons are needed."
- Mistake: Check on a scale that leaves items over -> "With 1 icon = 4, 70 items need 17 icons and 2 items are left over. Try another scale." (It names the first row that leaves items over.) Scale 5 in Star Challenge 3 -> "That is the scale Dipesh used. Choose a different scale."
- Hints: (1) "What does one icon stand for? Look at the icon box." (2) the icon box glows and the row's number shows brackets of 5 (3) the tool places all the icons but one, or fills in the icon count and leaves only the product.
- Edge cases: a row with one icon (Drums) still stands for 5 items; scale 1 is not offered (one icon for every item).
7. Ending
- Star Challenges 1 to 3 above. Success: both numbers and the total are right and a fitting scale other than 5 is shown with the right icons.
- End screen: "Well done!" Remember: "One icon stands for the scale." "Number of items = number of icons × the scale." "Choose a scale that fits every number, with nothing left over." Think and talk: "A shop has 500 toys. Which scale would you choose, and why?" Button: "Start again". A small confetti burst plays here only.
8. Assets and Language
- Images: toy-shop wall photo with wooden shelves; chalkboard (rows by code); wooden tray; price tags; photo cut-outs of a kite, puzzle box, ball, robot, drum, doll, toy car, teddy bear, dice set, toy train, board game box and racket; wooden scale chips; a lamp. English.""",

    "M2.S8.T8.C40.2D1": """A. TOOL TITLE
- Squares to Bars
B. TOOL INFO
- Tool ID: M2.S8.T8.C40.2D1
- Tool type: Concept-activity
- Textbook source: Chapter 15 Data Through Pictures, Recording a Day: Raman's table (one square = 1 hour: sleeping 9, school 6, studying 2, eating and playing 6, other activities 1), Sheela's bar graph (8, 7, 4, 3, 2) and the book's five questions (developer only). Samaira's and Kabir's weeks are practice values.
C. LEARNING OBJECTIVE
- The student sees that a row of squares stands up into a bar of the same height, reads the height of a bar on the vertical line, and compares two bars to say which is more and by how many.
- Out of scope: making a graph from a table of numbers, scales other than 1 square = 1 hour, totals of all bars.
D. TOOL DESCRIPTION
1. Opening Screen
- A classroom wall as a photo. On the left a cork pinboard holds three rows of glossy blue square tiles, each tile about a thumb-width: Homework 4, Games 2, TV 1. Each row has its name at the left end and its count under it ("4 squares").
- On the right an empty graph board in a wooden frame: the vertical line marked 0 to 10 and named "Number of Hours", the horizontal base named "Activities" with three places, and a thin dotted guide from each row to its place.
- Instruction line: "Stand each row up. The bar is as tall as the row is long."
- The Homework row glows. The child is invited to tap a mark on the vertical line first, then the row.
2. Scene and Objects
- Tiles are drawn by code, 1 square = 1 hour. The graph board is grid paper with equal marks and numbers 0 to 10. Bars are solid, all the same width, one colour per graph (warm orange; a second graph is sky blue). No number is printed on a bar.
- Reading line: a thin horizontal rod with a round handle, resting at 0, with a small tag showing the number it points to. Guess flag: a small flag the child drops on a mark. Goal chip at the top, for example "Bars: 0 of 3".
- Activity 4 shows two graphs side by side with the same marks. In the challenges the stage holds Raman's table on the left, Raman's empty graph in the middle and Sheela's graph on the right; once all five rows are up the table folds into a tab so the two graphs share the stage.
3. Main Interaction
- Tap a row of squares: it stands up with a soft slide into a bar of the same height; its row stays as a pale ghost. Tap the small "lay down" arrow on a bar to lay it back (there is no Undo button).
- Drag the reading line up or down; it snaps to whole marks. Tap two bars to compare them (a third tap replaces the older one).
- Activity 3 only: a small plus and minus at the foot of the TV bar add or take away one square.
- Bottom buttons, three only: "Reset", "Hint", "Check" (it turns into "Next" when the activity is done). Typed answers use a number pad.
4. Activities
- Activity 1 (guided). Goal line: "Stand each row up. The bar is as tall as the row is long." Goal chip: "Bars: 0 of 3". Setup: Samaira's week, Homework 4, Games 2, TV 1 squares (practice values). Guess: before touching the Homework row, the child drops a flag on the mark where the top of its bar will reach. Result: each tapped row stands up; the flag turns green if it was at 4, otherwise the strip adds "Your flag was at 6. The bar reaches 4." (with the child's own number). Why line: "The homework row has 4 squares, so the bar goes up to 4." Help: guided; counts and dotted guides are shown.
- Activity 2 (guided). Goal line: "Slide the line to the top of each bar and read the number." Goal chip: "Bars read: 0 of 3". Setup: the three bars stand; the line is at 0. Guess: "Which bar is the tallest?" The child taps a bar. Result: with the line on each top the tag reads 4, 2 and 1 and each bar gets a tick. Why line: "The line touches the top of the homework bar at 4, so it is 4 hours high. Homework is the tallest and TV is the shortest." Help: guided; the line snaps gently near a top.
- Activity 3 (independent). Goal line: "Make the TV bar as tall as the homework bar." Goal chip: "TV = Homework". Setup: TV bar 1 high, homework bar 4 high. Guess: "How many squares must be added?" with buttons 2, 3, 4. The child taps plus. Result: the TV bar rises to 4 and the chip turns green. Why line: "The TV bar was 1 high and the homework bar is 4 high. 4 − 1 = 3, so 3 squares were added." Help: independent.
- Activity 4 (guided, then independent). Goal line: "Tap two bars of the same activity. Who spent more time?" Goal chip: "Compared: 0 of 3". Setup: Samaira's graph (orange: Homework 4, Games 2, TV 1) beside Kabir's graph (blue: Homework 3, Games 4, TV 1), practice values. Guess, before each pair: the child taps "Samaira", "Kabir" or "The same". Result: a dotted line joins the two tops. Why lines: "Samaira's bar is 4 high and Kabir's is 3 high. 4 − 3 = 1, so Samaira spent 1 hour more." "Kabir's bar is 4 high and Samaira's is 2 high. 4 − 2 = 2, so Kabir spent 2 hours more." "Both bars are 1 high, so the time is the same." Help: guided for homework (the dotted line shows after the first tap); independent for games and TV.
- Star Challenge 1 (independent). Raman's five rows lie on the pinboard (Time spent sleeping 9, Time in school 6, Time spent studying 2, Time spent eating and playing 6, Other activities 1 squares). The child stands each up in Raman's graph beside Sheela's bar graph (Sleeping 8, Time in school 7, Studying 4, Eating and playing 3, Other activities 2). Goal chip: "Stand up Raman's 5 rows". Then three questions, one at a time, in the book's words: "Whose daily routine shows more time spent on sleeping? ___" (tap "Raman" or "Sheela"), "Who spends more hours in the school? ___" (tap a name), "How many more hours does Sheela spend studying compared to Raman? ___" (number pad). Guess: the child's own answer is the commitment. Results: "Raman's sleeping bar is 9 high and Sheela's is 8 high. 9 is more than 8, so Raman." "Raman's school bar is 6 high and Sheela's is 7 high, so Sheela." "Sheela's studying bar is 4 high and Raman's is 2 high. 4 − 2 = 2 hours more."
- Star Challenge 2 (independent). The same two graphs. Question 4, in the book's words: "Is there any activity on which they spend the same amount of time? If yes, name the activity ___" The child taps "No" or one of the five activity names. Result: each pair of bars lights in turn: "9 and 8, 6 and 7, 2 and 4, 6 and 3, 1 and 2. All five pairs are different, so the answer is No." Question 5: "Based on their data, whose routine do you think is more balanced? Why? ___" The child taps "Raman" or "Sheela", then taps two bars of that child as the reason; the tool says how far apart the two bars are. Sample shown after Check: "Sample answer: Sheela's, because her studying 4 and eating and playing 3 are closer than Raman's 2 and 6. Your answer may differ." Help: independent.
5. Mathematical Understanding
- Standing a row up shows that squares and bar are the same data: the bar is as tall as the row is long. The number is read where the top meets the vertical line, never from the width.
- Comparing shows the taller bar is more, equal tops are the same, and the gap between two tops is how many more.
- Rules: "A bar is as tall as its row of squares is long." "The taller bar is more. Take the smaller from the bigger to find how many more."
6. Feedback and Hints
- Correct: a green tick, a gentle bounce, one line with the numbers. Every wrong answer: red strip, a small shake, ONE friendly line, free retry.
- Mistake: line not on the top -> "The line is above the bar. Slide it down until it touches the top." or "The bar is taller. Slide the line up until it touches the top." The top pulses.
- Mistake: wrong number of squares in Activity 3 -> "The TV bar is now 5 high but the homework bar is 4 high. Take one square away." or "The TV bar is 3 high. One more square makes it 4."
- Mistake: the shorter bar named as more -> "Look again. The taller bar is the one with more hours. Which of the two bars is taller?" Both tops pulse.
- Mistake: adding instead of taking away -> "4 + 2 = 6 adds the two heights. To find how many more, take the smaller height from the bigger." Answering 4 for the studying question -> "4 is Sheela's hours. How many more is that than Raman's 2?"
- Mistake: "Time in school" or "Eating and playing" for question 4 (Raman has 6 and 6) -> "Raman has 6 hours for school and 6 for eating and playing, but those are two activities of one child. Compare the same activity of Raman and Sheela." The five pairs light up.
- Mistake: width used as the number -> "All the bars have the same width. Only the height tells the number of hours."
- Hints: (1) "How many squares are in this row? The bar is that tall." (2) dotted lines run from the tops to the vertical line (3) the reading line moves to the top of the bar, or both heights are shown and only the answer is left.
- Edge cases: two tops at the same height show "the same", never "0 more"; the open question never turns red and accepts any reason with two bars.
7. Ending
- Star Challenges 1 and 2 above. Success: all five rows stand up and all five questions are answered; question 5 needs a name and two bars.
- End screen: "Well done!" Remember: "A bar is as tall as its row of squares is long." "Read a bar where its top meets the vertical line." "The taller bar is more. Take the smaller from the bigger to find how many more." Think and talk: "Why do all the bars have the same width?" Button: "Start again". A small confetti burst plays here only.
8. Assets and Language
- Images: classroom wall photo with a cork pinboard; glossy blue square tile; wooden-framed graph board with grid paper; reading rod; small flag; arrow icon. Bars and marks by code. English.""",

    "M2.S10.T10.C53.2D1": """A. TOOL TITLE
- Bar Graph Builder
B. TOOL INFO
- Tool ID: M2.S10.T10.C53.2D1
- Tool type: Concept-activity
- Textbook source: Chapter 15 Data Through Pictures, Day in My Life (record the 24 hours, make a bar graph) and Whose Index Finger is Longer? (five paper strips, four questions); the book's sheets have the vertical line marked 0 to 9 and 1 to 10 with 1 cm at the foot (developer only). All sample numbers are practice values.
C. LEARNING OBJECTIVE
- The student sees how to make a bar graph: names along the horizontal base, a vertical line that reaches at least the biggest number, and each bar drawn up to its number or its length in cm.
- Out of scope: comparing two graphs, minutes, scales other than 1 hour or 1 cm per mark.
D. TOOL DESCRIPTION
1. Opening Screen
- A wooden drawing board with a sheet of graph paper (photo texture), a pencil and a ruler beside it. The vertical line is marked 0 to 10 and named "Number of Hours"; the horizontal base is named "Activities" with three empty name places, each with a small round knob at its foot.
- A small paper table pinned at the top-left: "School 5", "Studying 3", "Sleeping 7". Three paper name tags, "School", "Studying", "Sleeping", lie in a tray under the sheet.
- Instruction line: "Write the names on the base. Make each bar as tall as its number."
- The tag "School" glows. The child is invited to drag it onto the first place.
2. Scene and Objects
- Sheet: about 70% of the stage. Marks are equal; every bar and strip has the same width. Bars are warm orange; the bar being asked about glows tangerine. A small tag at a bar's top shows its height.
- Name tags are paper cut-outs. In the length activities the tray holds coloured paper strips and the vertical line is a ruler: 1 cm at the foot, then 2, 3 and so on to 10.
- Goal chip at the top, for example "Bars: 0 of 3"; a "Total" chip adds the table's numbers.
3. Main Interaction
- Drag a name tag onto a place on the base. Drag the round knob of a place up or down: the bar grows to the nearest whole mark. Tap a name on the base to take it back (there is no Undo button).
- Activity 2 only: an up arrow at the top of the vertical line adds one mark (to at most 12).
- Day in My Life: each table row has a minus and a plus around its hours; "Hours left" counts from 24. A chip "Use sample day" fills 9, 5, 2, 2, 3, 3 (whole hours only).
- Finger strips: five strips (Mine, Friend 1 to Friend 4); drag a strip's top to the length you measured outside the tool, 1 to 10 cm. A chip "Use sample strips" fills 6, 7, 5, 8, 6.
- Bottom buttons, three only: "Reset", "Hint", "Check" (it turns into "Next" when done). Typed answers use a number pad.
4. Activities
- Activity 1 (guided). Goal line: "Write the names on the base. Make each bar as tall as its number." Goal chip: "Bars: 0 of 3". Setup: table School 5, Studying 3, Sleeping 7 (practice values), line 0 to 10. Guess: before building, "Which bar will be the tallest?" with the three names as buttons. Result: bars at 5, 3 and 7; the tallest glows. Why line: "Sleeping is 7 hours, so the bar goes up to 7. 5 + 3 + 7 = 15 hours." Help: guided; each name tag matches the table and the target marks glow faintly.
- Activity 2 (guided). Goal line: "Make the line tall enough, then draw the bars." Goal chip: "Line and bars". Setup: Sunday table Playing 6, TV 3, Reading 2 (practice values); names already on the base; the line is marked 0 to 4 only. Guess: "How far must the line go?" with buttons "Up to 4", "Up to 6", "Up to 10". Result: the child adds marks to at least 6 and draws bars 6, 3 and 2. Why line: "The biggest number is 6, so the line must go up to 6 or more." Help: guided; names are placed.
- Activity 3 (independent). Goal line: "One bar does not match the table. Fix it." Goal chip: "Fix the bar". Setup: table Eating 2, Studying 4, Playing 5; the graph shows bars 2, 4 and 6. Guess: the child taps the bar they think is wrong; the table's number appears beside its top. Result: the child drags the playing knob from 6 down to 5. Why line: "The table says playing 5, but the bar went up to 6. Now the bar is at 5." A right bar tapped shows "Eating: the table says 2 and the bar is at 2. This bar is right. Look at the others." Help: independent.
- Activity 4 (independent). Goal line: "Show each strip as a bar. Read its length in cm." Goal chip: "Strips: 0 of 3". Setup: three strips marked 7 cm, 5 cm and 3 cm (practice values), places named A, B, C. Guess: "Which strip will be the tallest bar?" The child drags each strip to a place and pulls its top to its length, then taps the longest and the shortest bar. Result: bars at 7, 5 and 3. Why line: "The longest strip is 7 cm and the shortest is 3 cm. 7 − 3 = 4 cm longer." Help: independent.
- Star Challenge 1 (independent), in two steps with the book's words: "Record your daily routine (24 hours) in hours and minutes, as necessary. Note the time spent on activities like sleeping, studying, playing, eating, and others." then "Make a bar graph of the time you spend on different activities in the space given below." Goal chip: "Hours left: 24". Step 1: the table rows are Sleeping, Time in school, Studying, Eating, Playing, Other activities; the child sets the hours with plus and minus; a small note says "Use whole hours." Guess: before recording, the child taps the activity that will take the most hours. Step 2: the six names are on the base and the child drags each knob to its row's number. Result (sample day 9, 5, 2, 2, 3, 3): bars at those heights. Why line: "9 + 5 + 2 + 2 + 3 + 3 = 24. Your hours add up to 24. A day has 24 hours." The tool says "You guessed Playing. The tallest bar is Sleeping, 9 hours." when they differ. The numbers are the child's own; the sample is only a sample.
- Star Challenge 2 (independent). Goal chip: "Strips: 0 of 5". The base has five places: Mine, Friend 1, Friend 2, Friend 3, Friend 4. A pinned task note holds the book's words: "Cut long paper strips from waste paper. Give one strip (each of the same width) to each of your friends. Now, put the paper strip on your index finger and tear off the extra strip extending above your fingers." The instruction line: "Paste these paper strips along the horizontal line in the given bar graph." Guess: the child taps whose finger will be the longest. The child pulls each of the five strips to the measured length. Then four cards in the book's words: "Whose index finger is the longest? ___" (tap a bar), "The length of the longest index finger is ___ cm." (number pad), "The smallest index finger is ___ cm long." (number pad), "It belongs to ___." (tap a name). Result with the sample strips: "The tops are at 6, 7, 5, 8 and 6. Friend 3 reaches 8, the highest, so the longest index finger is Friend 3's, 8 cm. The lowest top is 5, so the smallest is 5 cm and it belongs to Friend 2." Answers follow the child's own strips; with two equal tallest strips either name is right.
5. Mathematical Understanding
- Building shows the steps: names on the base, a vertical line that reaches at least the biggest number, each bar up to its number, then a check against the table or the total of 24.
- A bar can be a real length: the tallest bar is the longest strip, the lowest is the shortest, and the gap is how much longer.
- Rules: "Write the names on the base and draw each bar up to its number." "The vertical line must reach at least the biggest number."
6. Feedback and Hints
- Correct: the bar settles with a small bounce, the tag and the goal chip turn green, one line with the numbers. Every wrong answer: red strip, a small shake, ONE friendly line, free retry.
- Mistake: bar at the wrong mark -> "The table says Sleeping 7, but the bar goes up to 8. Drag the top down to 7." The top pulses.
- Mistake: line too short -> "The playing bar needs 6, but the line stops at 4. Make the line longer."
- Mistake: hours do not add up -> "Your hours add up to 22. A day has 24 hours. 2 hours are still free." With no hours left, plus says "No hours are left. Take an hour from another row first."
- Mistake: strip at the wrong cm -> "This strip is 7 cm, but its top is at 6 on the ruler."
- Mistake: wrong bar for a finger card -> "Look again. The longest index finger is the tallest bar." Wrong length -> "Look at the top of that bar. Where does it meet the ruler?"
- Mistake: width used as the number -> "All the bars and strips have the same width. Only the height tells the number or the length."
- Hints: (1) "Which number goes with this name? Look at the table." (2) a dotted line runs from the table's number to its mark on the vertical line (3) the bar rises to one mark below its number and the child finishes it.
- Edge cases: a row with 0 hours shows no bar and its name stays on the base; a strip is at least 1 cm; two equal tallest strips show "Two strips are equally tall. Tap either one."
7. Ending
- Star Challenges 1 and 2 above. Success: hours add up to 24 and all six bars match the table; five strips are set and the four finger cards are answered.
- End screen: "Well done!" Remember: "Write the names on the base and draw each bar up to its number." "The vertical line must reach at least the biggest number." "A day has 24 hours, so the hours must add up to 24." Think and talk: "How could you use your bar graph to tell a friend about your day?" Button: "Start again". A small confetti burst plays here only.
8. Assets and Language
- Images: wooden drawing board with graph paper (photo); pencil and ruler cut-outs; paper name tags; coloured paper strips of one width; round knobs; cm marks by code. English.""",

    "M3.S15.T15.C83.2D1": """A. TOOL TITLE
- Picture Detective
B. TOOL INFO
- Tool ID: M3.S15.T15.C83.2D1
- Tool type: Puzzle
- Textbook source: Chapter 15 Data Through Pictures, True or False: the picture of 17 school children (8 girls, 9 boys; 10 caps, 7 pairs of glasses, 14 books, 4 backpacks) and its eight statements (developer only). The practice picture of 10 children is a practice value.
C. LEARNING OBJECTIVE
- The student sees that a statement about a picture is judged by counting the children it talks about and comparing the counts, including with half of all the children, and that "some", "all" and "no child" are judged by finding the children who do or do not.
- Out of scope: fractions beyond half, graphs, statements that need guessing.
D. TOOL DESCRIPTION
1. Opening Screen
- A school notice board as a photo. Pinned on it is a flat drawing of 10 children in two rows of 5 (the practice picture). Some wear a scarf, some carry a bag, some both, some neither.
- Under the picture, a count strip (empty) and a row of chips: "Scarf", "Bag", "Hat", and a small switch "and". At the bottom of the stage a statement card is blank.
- Instruction line: "To check a statement, count the children it talks about."
- The chip "Scarf" glows. The child is invited to tap it.
2. Scene and Objects
- Picture: about 55% of the stage height. Chips are large rounded tabs. A tapped chip lights the matching children (a bright outline and a glow) and fades the others; with "and" on, up to three chips narrow the group to children who match all of them.
- Counter badge on the picture corner: "Lit: 6". Count strip: up to 4 small vertical bars, each named and numbered (for example "Scarf 6"); a new count replaces the oldest. A "Half-way line" switch draws a dashed line across the strip at half of the children with its number, for example "Half of 10: 5".
- Statement card with two big tiles "TRUE" and "FALSE" (these are answer tiles, not bottom buttons).
- Practice picture, row 1: scarf and bag, scarf only, bag only, neither, scarf and bag. Row 2: scarf only, neither, bag only, scarf and bag, scarf only. Totals: 10 children; scarf 6; bag 5; both 3; no hats.
- Main picture (17 children, the girls in a blue pinafore over a cream shirt, the boys in a cream shirt and blue shorts). Back row, left to right: girl with cap, backpack and book; boy with book; boy with cap, glasses and book; girl with cap and book; boy with book; girl with cap, glasses and book; boy with glasses and book; boy with cap, glasses and book; boy with book. Front row: girl with cap, glasses and backpack; girl with cap, glasses and book; girl with cap and book; boy with cap, glasses and backpack; girl with book only; girl with cap and book; boy with book; boy with backpack only. Chips: Girls, Boys, Cap, Glasses, Book, Backpack.
3. Main Interaction
- Tap a chip to light its group; tap it again to switch it off. With "and" off, a new chip replaces the old one. With "and" on, chips add up (at most 3).
- Every statement has three steps. First the child taps TRUE or FALSE as a guess (not marked). Then the chips unlock: the child lights the groups the statement talks about. Then the child taps TRUE or FALSE again as the final answer. Only the final answer is checked. A final answer with nothing lit gets "Light up the children the statement talks about first."
- Bottom buttons, three only: "Reset" (clears the lights, bars and answer of this card), "Hint", "Next" (grey until the card is right). A wrong final answer can be changed at once.
4. Activities
- Activity 1 (guided). Goal line: "Count the children with a scarf, then with a bag." Goal chip: "Scarf ?  Bag ?". Setup: practice picture. Guess: "How many children have a scarf?" with buttons 4, 6, 8. Result: Scarf lights 6, then Bag lights 5; two bars appear. Why line: "6 children have a scarf and 5 have a bag." Help: guided; lit children glow strongly.
- Activity 2 (guided). Goal line: "More children have a scarf than a bag. True or false?" Goal chip: "Compare the bars". Guess: TRUE or FALSE. Result: the two bars side by side; Why line: "6 is more than 5, so it is True. 6 − 5 = 1 more child has a scarf." Help: guided; the bars from Activity 1 stay.
- Activity 3 (guided). Goal line: "Some children have a scarf and a bag. True or false?" Goal chip: "Scarf and Bag". Guess: TRUE or FALSE. The child switches "and" on and taps Scarf and Bag. Result: 3 children lit. Why line: "3 children have both. Some means at least one, and 3 is more than 0, so it is True." Help: guided.
- Activity 4 (independent). Goal chip: "Half of 10: 5". Two cards. Card (a): "More than half of the children have a scarf. True or false?" Card (b): "More than half of the children have a bag. True or false?" The child switches the half-way line on. Guess before each. Why lines: "Half of 10 is 5. 6 is more than 5, so it is True." "Half of 10 is 5. 5 is exactly half, not more than half, so it is False." Help: independent; the half-way line is the child's tool.
- Activity 5 (independent). Goal chip: "All and none". Card (a): "No child wears a hat. True or false?" Card (b): "All the children have a bag. True or false?" Why lines: "Hat lights no child. 0 children wear a hat, so it is True." "5 of the 10 children have a bag. 10 − 5 = 5 children have no bag, so it is False." Help: independent.
- Star Challenge 1 (independent), the picture of 17 children, instruction line "Observe the picture carefully. Based on your observation, is this statement true or false?" with the book's statements, one card each: (1) "All girls are wearing glasses." (2) "10 children are wearing caps on their heads." (3) "More boys are holding books than girls." (4) "More than half of the children are wearing glasses." Goal chip: "Cards done: 0 of 4". Why lines: (1) "Only 3 of the 8 girls wear glasses. 8 − 3 = 5 girls have no glasses, so it is False." (2) "5 caps in the back row and 5 in the front row: 5 + 5 = 10. It is True." (3) "7 boys and 7 girls hold books. 7 is not more than 7, so it is False." (4) "7 children wear glasses and half of 17 is 8 1/2. 7 is less than 8 1/2, so it is False." Help: independent.
- Star Challenge 2 (independent), the same instruction line: (5) "The number of children holding books is greater than the number of children wearing caps." (6) "The number of boys wearing glasses is greater than the number of girls wearing glasses." (7) "Some children are wearing both glasses and caps." (8) "There is no child who has all three items, a cap, a book and a backpack." Goal chip: "Cards done: 0 of 4". Why lines: (5) "14 children hold books and 10 wear caps. 14 is more than 10, so it is True." (6) "4 boys and 3 girls wear glasses. 4 is more than 3, so it is True." (7) "6 children wear both glasses and a cap. Some means at least one, so it is True." (8) "1 child has all three: the girl at the back on the left. So it is False." Help: independent.
5. Mathematical Understanding
- Lighting a group makes the counting exact; the bars put two counts side by side, so "more", "the same" and "more than half" become a comparison of numbers.
- The child sees: a quick look can fool you; "more than half" needs half of all the children, and half of an odd number is a number and a half (17 is 8 1/2); "some" needs one child; "all" fails with one child who does not; "no child" fails with one child who does.
- Rule: "Count the children the statement talks about, then compare the counts."
6. Feedback and Hints
- Correct: the card turns green, the tile bounces, the bars that settled the statement stay, one why line with the numbers. A guess that changes after counting gets: "Counting changed your mind. Good detective work."
- Every wrong final answer: red strip, a small shake, ONE friendly line, free retry, never the answer. Clues: (1) "Light up Girls, then Glasses with and. Is every girl lit?" (2) "Light up Cap and read the counter. What does it say?" (3) "Count the boys with books and the girls with books. Are the two counts different?" (4) "Switch on the half-way line. Is the glasses bar past it?" (5) "Light up Book, then Cap. Which bar is taller?" (6) "Light up Boys and Glasses together, then Girls and Glasses. Compare the two counts." (7) "Light up Cap and Glasses together. Is anyone lit?" (8) "Light up Cap, Book and Backpack together. Is anybody lit?"
- Mistake: the same counts called "more" -> "7 and 7 are the same, not more."
- Mistake: half of 17 called 8 -> "Half of 17 is not 8. 17 ÷ 2 is 8 with 1 left over, so half is 8 1/2."
- Mistake: exactly half called more than half -> "5 is exactly half of 10, so it is not more than half."
- Mistake: "some" read as "many" -> "Some means at least one child."
- Hints: (1) "Which children does the statement talk about? Count only them." (2) the matching chips light up and the bars show the counts (3) the half-way line or the one matching child is shown and only TRUE or FALSE is left.
- Edge cases: a group of 0 (Hat) lights nobody and shows 0; a count exactly equal to half; two equal counts; three chips at once for statement 8.
7. Ending
- Star Challenges 1 and 2 above. Success: all eight statements are answered right, each after counting.
- End screen: "Well done!" Remember: "Count the children the statement talks about, then compare the counts." "More than half means more than half of all the children." "One child is enough to make 'all' or 'no child' false." Think and talk: "A picture shows 9 children. Can exactly half of them wear caps? Why?" Button: "Start again". A small confetti burst plays here only.
8. Assets and Language
- Images: school notice board (photo); flat drawings of 10 practice children with scarf and bag variants; flat drawing of the 17 children with caps, glasses, books and backpacks, one cut-out per child so each can glow; chips, tiles and half-way line by code. English.""",

}

OBJECTIVES = {
    "M1.S1.T1.C2.2D1": "The student sees that sorting every answer into one row of a table turns a crowd of answers into counts, and that the counts of all the rows add up to the number of answers.",
    "M1.S4.T4.C17.2D1": "The student sees that one icon stands for a group of items, that the number of items is the number of icons × the scale, and that a scale must fit every number with nothing left over.",
    "M2.S8.T8.C40.2D1": "The student sees that a row of squares stands up into a bar as tall as the row is long, that the taller bar is more, and that the gap between two bars is how many more.",
    "M2.S10.T10.C53.2D1": "The student sees how to make a bar graph: names on the base, a vertical line that reaches the biggest number, and each bar drawn up to its number or its length in cm.",
    "M3.S15.T15.C83.2D1": "The student sees that a statement about a picture is judged by counting the children it talks about and comparing the counts, including with half of all the children.",
}
