# -*- coding: utf-8 -*-
"""Class 5 Chapter 6, The Dairy Farm: long-form tool descriptions in the master prompt's format (17 Nov 2026).
DESCRIPTIONS and OBJECTIVES are keyed by media_id (the Tool ID). Plain text, no markdown."""

DESCRIPTIONS = {}
OBJECTIVES = {}

# ======================================================================================================
# Tool 1: Pouch Packer
# ======================================================================================================
OBJECTIVES["M1.S1.T1.C2.2D1"] = (
    "The student sees that one total of pouches can be packed in equal groups in many ways, and that number of "
    "groups × group size gives the same total when the two numbers swap.")

DESCRIPTIONS["M1.S1.T1.C2.2D1"] = """
A. TOOL TITLE
- Pouch Packer
B. TOOL INFO
- Tool ID: M1.S1.T1.C2.2D1
- Tool type: Exploration (the free first try right after the opening story)
- Textbook source: The Dairy Farm, chapter opening: 60 butter milk pouches packed in pairs and in threes, the pouch pictures with 30 × 2 = 60 done for you, and "What other groups can you make?". The total 24 is a practice value of the plan (developer only).
C. LEARNING OBJECTIVE
- The student sees that one total of pouches can be packed in equal groups in many ways, and reads each way as number of groups × group size, which keeps the same total when the two numbers swap.
- Out of scope: division, leftover pouches, multiplying by 10 or 100, totals above 60.
D. TOOL DESCRIPTION
1. Opening Screen
- Photo scene of Daljeet Kaur's packing floor: a steel-topped table seen from slightly above, wooden crates at its left, a blurred cow-shed door behind. A small flat-drawn Daljeet Kaur stands at the left end of the table.
- 60 butter milk pouches (photo cut-outs of a blue and white milk pouch, front face, about a thumb-width each) lie loose on the table in 6 rows by 10 columns.
- Instruction line: "Daljeet Kaur has 60 pouches. Pack them in equal groups."
- The plus button of the group size stepper pulses once: the child taps it first.
2. Scene and Objects
- Stepper at the table's front edge: a round minus button, a big number window (starts at 2) and a round plus button. Sizes run from 2 to half of the total (30 for 60 pouches).
- Rings: each group sits in a thin white rubber ring, its pouches in a tidy block. Rings fill the table in rows; pouches shrink to fit, never below half a thumb-width.
- Plate on the table front: "__ groups × __ pouches = __ pouches". A round "Turn" button (curved arrow) at the table's right end and a small "Add" button by the plate.
- Wall chalkboard "Ways found" with 10 empty lines; each line holds one way such as "12 × 5 = 60".
- Goal chip: a wooden tag such as "Groups of 5". Guess cards: three big cards (two thumb-widths wide) stand on the table when a guess is asked.
3. Main Interaction
- Plus and minus change the group size. Pouches are packed only after the guess the activity asks for.
- A size that makes equal groups: the pouches slide into rings and the plate fills, for example "12 groups × 5 pouches = 60 pouches". Any other size: the last ring is not full (dashed empty places) and the plate stays empty. This is a try, not a mistake, so the strip keeps its normal colour.
- Turn: a quarter turn; the groups and the size swap (12 groups of 5 become 5 groups of 12). It works only after equal groups. Tap again to turn back.
- Add: writes the plate's sentence on the next chalk line. The same sentence twice gives "You found that one already."
- Bottom buttons (only three): "Hint", "Reset" (loosens the pouches, clears the board), "Next" (unlocks when the goal chip is green).
4. Activities
- Activity 1 (guided). Goal line: "Pack the 60 pouches in groups of 5." Goal chip: "Groups of 5". Setup: 60 loose pouches, stepper at 2; the child taps plus up to 5. Guess: cards "10 groups", "12 groups", "15 groups". Result: 12 rings form and the strip says "12 groups of 5 make 60, so 12 × 5 = 60." Help: guided, each ring shows "5" and the rings are numbered 1 to 12.
- Activity 2 (guided). Goal line: "Turn the table. What do you see?" Goal chip: "Turn it". Setup: the 12 groups of 5. Guess: cards "More than 60", "Still 60", "Less than 60". Result: 5 rings of 12 pouches; the strip says "12 groups of 5 turn into 5 groups of 12. The pouches are the same, so 12 × 5 = 5 × 12 = 60." Help: guided, the two numbers on the plate cross over with an arrow.
- Activity 3 (guided). Goal line: "Try 7 pouches in each group." Goal chip: "Try 7". Guess: cards "Equal groups", "Not equal groups". Result: 9 rings, the ninth with 4 pouches and 3 dashed empty places; the strip says "7 does not make equal groups of 60: 8 × 7 = 56 and 9 × 7 = 63, and neither is 60." Help: guided, empty places are dashed.
- Activity 4 (independent). Goal line: "Find every way to pack 60 pouches." Goal chip: "All the ways". Setup: 60 pouches, empty chalkboard. Guess (once, at the start): cards "Fewer than 5 ways", "5 to 9 ways", "10 or more ways". The child tries sizes, turns, and adds each way. Result: with 10 ways the board lights up and the strip says "30 × 2, 20 × 3, 15 × 4, 12 × 5, 10 × 6, 6 × 10, 5 × 12, 4 × 15, 3 × 20 and 2 × 30 all make 60." Help: independent.
- Activity 5 (independent, practice values). Goal line: "Now pack 24 pouches." Goal chip: "24 pouches". Setup: 24 pouches in 4 rows by 6 columns, stepper 2 to 12, clean chalkboard. Guess: cards "5 works", "5 does not work". Result: "5 does not make equal groups of 24: 4 × 5 = 20 and 5 × 5 = 25, and neither is 24." With 6 ways found: "12 × 2, 8 × 3, 6 × 4, 4 × 6, 3 × 8 and 2 × 12 all make 24." Help: independent.
5. Mathematical Understanding
- The total never changes while the number of groups and the group size change together. Turning shows that 12 groups of 5 and 5 groups of 12 are the same pouches. A ring that is not full shows that only some sizes work.
- Rule in the child's words: "A total can be packed in equal groups in many ways. Number of groups × group size gives the total. Swap the two numbers and the total stays the same."
6. Feedback and Hints
- Wrong guess or sentence: the strip turns red, the card or box shakes a little, one friendly line says what to look at. No scores, retry is free. After two wrong guesses the result plays anyway and the child taps the right card.
- Correct: the card turns green with a gentle bounce, the goal chip turns green, the pill gets a tick and Next unlocks.
- Mistake: guesses 10 groups in Activity 1 -> "Look at one group: it has 5 pouches. How many groups of 5 fit in 60?" One group pulses.
- Mistake: says 7 (Activity 3) or 5 (Activity 5) makes equal groups -> "Look at the last ring. Is it full?" The last ring pulses.
- Mistake: "More" or "Less" after Turn (M_ORDER_CHANGES) -> "Turning moves the pouches. It does not add or take away any. Count them again." All 60 pulse once.
- Mistake: presses Next with one way found (M_ONE_WAY) -> "You found one way. Can the same 60 pouches be packed in other equal groups?" The plus button pulses.
- Mistake: in Star Challenge 1 a total that is not 60, or only the groups across counted -> "Count all the groups, across and down." The groups pulse in two alternating tints.
- Hints (Hint button, 3 levels): (1) "How many pouches do you want in each group? Use the plus button." (2) the plus button glows at the next size that works and is not yet on the chalkboard. (3) the tool sets that size and gathers the rings: "Count the rings, then read the plate."
- Edge cases: size 30 gives 2 groups and size 2 gives 30 groups; at the end of the stepper the line is "Two groups is the fewest." Turning twice brings back the first picture.
7. Ending
- Star Challenge 1 (the book's question). Goal line: "A dairy has packed butter milk pouches in the following manner. Find the number of pouches kept in each arrangement. One is done for you." Goal chip: "Fill all arrangements". Setup: four thumbnails of the 60 pouches: (a) pairs, 6 across and 5 down, done for you as 30 × 2 = 60; (b) groups of 3 side by side, 4 across and 5 down; (c) 6 blocks side by side, each 2 pouches wide and 5 tall; (d) 5 rows of 12 pouches. The child opens each and fills "__ × __ = 60" with a small number pad; the answer typed is the guess. Result: the groups ring one by one and the strip says (b) "20 groups of 3 make 60, so 20 × 3 = 60." (c) "6 blocks of 10 pouches make 60, so 6 × 10 = 60." (d) "5 rows of 12 pouches make 60, so 5 × 12 = 60." The swapped sentence is accepted with "That is true too! We write the groups first: 20 × 3 = 60." Help: independent.
- Star Challenge 2 (the book's question): "What other groups can you make?" Goal chip: "3 new ways". The chalkboard is cleared. Done when it holds three ways that are not 30 × 2, 20 × 3, 6 × 10 or 5 × 12; the strip lists the child's three ways and says "All of these make 60 pouches. Many ways, one total." Help: independent.
- End screen: "Well done!" Remember: "One total can be packed in equal groups in many ways." "Number of groups × group size gives the total." "Turn the picture and the two numbers swap, but the total stays the same." Think and talk: "Why can 60 pouches be packed in groups of 5 but not in groups of 7?" Button: "Start again".
8. Assets and Language
- Images: photo of a steel-topped packing table from above on a dairy floor with a blurred cow-shed door; photo cut-out of a blue and white milk pouch (front face, one image used 60 times); photo cut-out of stacked wooden crates; flat drawing of Daljeet Kaur in a dairy apron; photo cut-out of a framed chalkboard; rings, arrows, dashed places, wooden tags, cards and number pad (code-drawn).
- Language: simple English for a 10 year old, one short line at a time; only the words "groups" and "group size".
"""

# ======================================================================================================
# Tool 2: Place Value Shifter
# ======================================================================================================
OBJECTIVES["M1.S6.T6.C23.2D1"] = (
    "The student sees that multiplying by 10, 100 and 1,000 moves each digit 1, 2 or 3 places left with zeros filling "
    "the empty places, and that tens, hundreds and thousands multiply by multiplying the digits and writing the zeros.")

DESCRIPTIONS["M1.S6.T6.C23.2D1"] = """
A. TOOL TITLE
- Place Value Shifter
B. TOOL INFO
- Tool ID: M1.S6.T6.C23.2D1
- Tool type: Concept-activity
- Textbook source: The Dairy Farm, Patterns in Multiplication by 10s and 100s: the revision of ×10 and ×100, the tables with 100 × 90, 60 × 50, 700 × 4, 10 × 45, the question about writing 450 in the table, and the tables for 1,000 and 100. Practice values of the plan: 26, 304, 50 × 30, 50 × 80, 6 × 4,000 (developer only).
C. LEARNING OBJECTIVE
- The student sees that multiplying by 10, 100 and 1,000 moves every digit 1, 2 or 3 places to the left with zeros filling the empty places, and that tens, hundreds and thousands are multiplied by multiplying the digits and then writing the zeros of both numbers.
- Out of scope: dividing, numbers above 99,999.
D. TOOL DESCRIPTION
1. Opening Screen
- Photo of the dairy cooperative's counting board: a rustic wooden board with five deep slots headed "Ten thousands", "Thousands", "Hundreds", "Tens", "Ones", beside two steel milk cans. Wooden digit tiles (black digit on yellow wood, a thumb-width each) show 26 in Tens and Ones.
- Instruction line: "Press ×10 and watch every digit." The round "×10" button under the board pulses once: the child taps it.
2. Scene and Objects
- Two rows: a thin "Number" strip keeping the starting number, and a big "Product" row below. A shelf holds loose digit tiles 0 to 9. A zero that fills an empty place is a grey stone tile; a zero inside a number is black on yellow wood.
- Three big round buttons "×10", "×100", "×1,000" (Activities 1 and 2, Star Challenge 3 screen 1) and a "places moved" counter.
- For tens and hundreds: two number cards such as "50" and "30", each a digit tile plus grey zeros, with "×" between, and a thin "Digits" strip with two slots under them.
- Goal chip: a wooden tag above the board, for example "26 × 10".
3. Main Interaction
- Move buttons slide every tile of the Number strip into the Product row, left by 1, 2 or 3 slots; grey zeros drop into the empty places.
- Build: the child drags digit tiles into the Product row; a 0 tile must be placed in an empty slot. Tapping a placed tile returns it to the shelf.
- Tens and hundreds: the child drags tiles into the Digits strip, then each grey zero after them; the row then slides right until its last tile sits in Ones.
- Bottom buttons (only three): "Hint", "Reset", "Check" (becomes "Next" after a right answer).
4. Activities
- Activity 1 (guided). Goal line: "Press ×10 and watch every digit." Goal chip: "26 × 10". Setup: 26 in the Number strip. Guess: the child taps where the 2 will land: Thousands, Hundreds or Tens. Result: the 2 slides to Hundreds, the 6 to Tens, a grey 0 fills Ones; the strip says "26 × 10 = 260: every digit moved 1 place to the left, and a 0 fills the empty ones place." Help: guided, arrows show each slide.
- Activity 2 (guided). Goal line: "Now press ×100, then ×1,000." Goal chip: "26 × 100 and 26 × 1,000". Guess: places moved by ×1,000: cards "1", "2", "3". Result: 2,600, then 26,000; the strip says "26 × 1,000 = 26,000: every digit moved 3 places to the left, and 3 zeros fill the empty places." Help: guided, places are counted on the board.
- Activity 3 (independent). Goal line: "Multiply 304 by 10." Goal chip: "304 × 10". Setup: 304, its 0 a black tile. Guess: where the black 0 goes: "It stays in Tens", "It moves to Hundreds", "It disappears". The child builds the row. Result: 3,040; the strip says "304 × 10 = 3,040: every digit moved 1 place to the left, even the 0, and a new 0 fills the ones place." Help: independent.
- Activity 4 (guided). Goal line: "Multiply the digits, then write the zeros." Goal chip: "50 × 30". Cards "50" and "30". Guess: zeros at the end of the answer: "1", "2", "3". The child puts 1 and 5 in the Digits strip, then drags the two zeros after them. Result: 1,500; the strip says "5 × 3 = 15, and 50 × 30 has 2 zeros, one from each number: 50 × 30 = 1,500." Help: guided, each zero is labelled with its number.
- Activity 5 (independent). Same goal line. Goal chip: "50 × 80". Guess: zeros at the end: "2", "3", "4". Result: 4,000; the strip says "5 × 8 = 40 already ends in a 0. Keep it and add the 2 zeros: 50 × 80 = 4,000." Help: independent.
- Activity 6 (independent). Same goal line. Goal chip: "6 × 4,000". Cards "6" and "4,000". Guess: zeros at the end: "3", "4", "5". Result: 24,000; the strip says "6 × 4 = 24, and the 3 zeros of 4,000 go at the end: 6 × 4,000 = 24,000." Help: independent.
5. Mathematical Understanding
- The three buttons show each digit moving 1, 2 or 3 places to a place 10, 100 or 1,000 times bigger; the grey zeros show the empty places hold 0 because the digits moved away. Splitting 50 × 30 into 5 × 3 and the zeros shows that tens times tens makes hundreds.
- Rules: "Multiplying by 10 moves every digit 1 place to the left, by 100 moves it 2 places and by 1,000 moves it 3 places." "Multiply the digits, then write the zeros."
6. Feedback and Hints
- Wrong answer: the strip turns red, the tiles shake a little, one friendly line says what to look at. No scores, retry is free; the right place is named only after the second try.
- Correct: right tiles turn green with a bounce, the goal chip turns green, the pill gets a tick, "Next" appears.
- Mistake: empty slot instead of a 0 tile (M_ADD_ZERO) -> "An empty place is not a zero: use the 0 tile." The empty slot pulses.
- Mistake: forgets zeros, for example 15 for 50 × 30 (M_ZERO_COUNT) -> "50 × 30 is tens times tens. Where are the zeros of 50 and 30?" The two grey zeros pulse.
- Mistake: the wrong number of places -> "×10 moves 1 place, ×100 moves 2 places, ×1,000 moves 3 places. Count the slots to the left." The slots light up.
- Mistake: wrong zero count, for example 400 for 50 × 80 -> "5 × 8 = 40 already has a 0. Count it, then add the 2 zeros of 50 and 80." The zeros blink.
- Hints (Hint button, 3 levels): (1) "Which place is each digit in now? Look at the columns of the board." (2) the columns light up with 1, 2 or 3 steps, or the zeros of both numbers blink. (3) the tool slides the digits and leaves the empty places: "Put a 0 tile in every place the digits left."
- Edge cases: the black 0 of 304 moves like any digit; the 0 of 5 × 8 = 40 is kept; 10 × 1,000 = 10,000 puts the 1 in Ten thousands.
7. Ending
- Star Challenge 1 (the book's question). Goal line: "Let us revise multiplication by 10 and by 100." Goal chip: "Revise ×10 and ×100". Nine cards in order: (a) 4 × 10, (b) 20 × 10, (c) 10 × 40, (d) 10 × 10 = 100 (given), (e) 20 × 50, (f) 80 × 10, (g) 3 × 100 = 100 × 3 = 300 (given), (h) 8 × 100 = ___ = ___, (i) 10 × 100 = ___ = ___. Given cards: the tiles slide, the child taps on. Otherwise the child builds the product (the build is the guess) and taps Check; in (h) and (i) the child first drags the card's two numbers into the first blank in swapped order. Answers: 40; 200; 400; 1,000; 800; (h) 100 × 8 = 800; (i) 100 × 10 = 1,000. Why line: "2 × 5 = 10, then 2 zeros: 20 × 50 = 1,000." Help: independent.
- Star Challenge 2 (the book's question). Goal line: "Find answers to the following questions. Fill in the table below and describe the pattern. Discuss in class." Goal chip: "Fill the tables". Four screens. Screen 1: the boxes 100 × 90, 400 × 10, 60 × 50, 30 × 20 = 600 (given), 700 × 4, 10 × 45. Screen 2: the table Problem, Thousands, Hundreds, Tens, Ones with rows 10 × 45, 30 × 20 (6, 0, 0 given), 400 × 10, 700 × 8, 100 × 90 (9, 0, 0, 0 given), and the question "How should we write 450 in the table below?" at the row of 10 × 45. Screens 3 and 4: the tables 60 × 50, 220 × 20, 11 × 300 and 80 × 90, 10 × 63, 40 × 12. Answers: 9,000; 4,000; 3,000; 2,800; 450 (4 Hundreds, 5 Tens, 0 Ones); 5,600; then 3,000; 4,400; 3,300; 7,200; 630; 480. Why line, for example: "40 × 12: 4 × 12 = 48, then 1 zero: 480." After each table the child taps "Multiply the digits, then write the zeros of both numbers." to describe the pattern (two wrong cards). Help: independent.
- Star Challenge 3 (the book's question). Goal line: "What will happen if we multiply numbers by 1,000?" Goal chip: "Multiply by 1,000". Screen 1: the facts 2 × 1,000 = 2,000, 5 × 1,000 = 5,000, 10 × 1,000 = 10,000, 20 × 1,000 = 20,000; the child presses ×1,000 on each, then taps "Every digit moves 3 places to the left, and 3 zeros fill the empty places." (two wrong cards). Screen 2: "Let us fill in the table and observe the patterns." The table (Ten thousands to Ones) shows the four facts and blank rows 3 × 5,000, 8 × 3,000, 5 × 7,000. Answers: 15,000; 24,000; 35,000. Why: "3 × 5 = 15, then 3 zeros: 3 × 5,000 = 15,000." Help: independent.
- Star Challenge 4 (the book's question). Goal line: "Let us fill in the table and observe the patterns." Goal chip: "Fill the table". Two screens (4 rows, then 3 rows): 20 × 100, 40 × 500, 60 × 300, 600 × 30, 80 × 900, 70 × 600, 5 × 7,000. Answers: 2,000; 20,000; 18,000; 18,000; 72,000; 42,000; 35,000. Why: "40 × 500: 4 × 5 = 20, then 3 zeros: 20,000." Help: independent.
- End screen: "Well done!" Remember: "Multiplying by 10, 100 or 1,000 moves every digit 1, 2 or 3 places to the left." "Zeros fill the places the digits left." "Multiply the digits, then write the zeros of both numbers." Think and talk: "Why is 50 × 80 equal to 4,000 and not 400?" Button: "Start again".
8. Assets and Language
- Images: photo of a rustic wooden counting board with five deep slots and two steel milk cans; wooden digit tiles 0 to 9 and a grey stone zero tile (photo cut-outs or code-drawn); number cards, tags, round buttons, arrows and table grids (code-drawn). Simple English, column names in full, no scores.
"""

# ======================================================================================================
# Tool 3: Halve and Double Packets
# ======================================================================================================
OBJECTIVES["M2.S10.T10.C42.2D1"] = (
    "The student sees that cutting an array of packets in the middle and putting the halves together a new way halves "
    "one number and doubles the other, so the product stays the same.")

DESCRIPTIONS["M2.S10.T10.C42.2D1"] = """
A. TOOL TITLE
- Halve and Double Packets
B. TOOL INFO
- Tool ID: M2.S10.T10.C42.2D1
- Tool type: Concept-activity
- Textbook source: The Dairy Farm, Doubling and Halving: 3 rows of 18 packets cut in the middle, giving 6 × 9 = 54, then 22 × 5, the problems 14 × 3, 16 × 4, 38 × 5, 35 × 14, the six products 5 × 18 to 16 × 45, and the question asking for 5 examples of the student's own. Practice values of the plan: 6 × 8, 7 × 10, 5 × 36, 25 × 16 (developer only).
C. LEARNING OBJECTIVE
- The student sees that cutting an array of packets in the middle and putting the halves together a new way halves one number and doubles the other, so the product stays the same, and that this makes a product easy with numbers like 5 and 25.
- Out of scope: halving odd numbers, dividing by other numbers.
D. TOOL DESCRIPTION
1. Opening Screen
- Photo of the dairy packing table, a wide steel table, with an array of yellow butter packets (photo cut-outs of a butter block in yellow foil, a thumb-width each) in 6 rows of 8. Above it two number boxes "6" and "8" with a "×" between and two arrows labelled "Half" and "Double".
- Instruction line: "Cut the packets in the middle and put the halves together a new way."
- A dashed cut line with a small scissors icon pulses at the top of the array: the child drags it.
2. Scene and Objects
- Array: the first number is the rows, the second the packets in each row. When both numbers are at most 12 every packet is drawn; a bigger array is drawn as a solid yellow block with a packet pattern and the two numbers written along its sides.
- Cut line: a dashed line with scissors, a horizontal line between two rows or a vertical line between two columns; it snaps to the gaps.
- Sum plate under the array: "__ × __ = __". Two small counters, "Before" and "After", show the total of packets.
- Goal chip: a wooden tag such as "6 × 8". Guess cards: three big cards on the table when a guess is asked. A number pad opens under a box when it is tapped.
3. Main Interaction
- Drag the cut line to a gap. In the exact middle the array parts a little. Not in the middle: the parts look unequal and the line is not accepted. An odd side cannot be cut in two equal halves.
- Cut between rows: the child drags one half beside the other (rows halve, packets in a row double). Cut between columns: one half goes below the other (packets in a row halve, rows double). The halves snap into a new array.
- The child writes the new problem in the two empty boxes with the pad, then the total. On a big block, tapping a side number draws the cut line at its middle.
- Bottom buttons (only three): "Hint", "Reset" (restores the array), "Check" (becomes "Next").
4. Activities
- Activity 1 (guided). Goal line: "Cut the packets in the middle." Goal chip: "6 × 8". Setup: 48 packets. The child drags the line between row 3 and row 4. Guess: the new problem when the halves go side by side: cards "3 × 16", "3 × 4", "12 × 16". Result: the halves slide side by side, the plate reads "3 × 16 = 48"; the strip says "Half of 6 is 3 and double 8 is 16, so 6 × 8 = 3 × 16 = 48. The same packets only moved." Help: guided, the Half and Double arrows light up.
- Activity 2 (guided). Goal line: "Now cut between the columns." Goal chip: "Cut the columns". Setup: 6 rows of 8; the vertical line goes between column 4 and column 5. Guess: cards "12 × 4", "6 × 4", "12 × 16". Result: one half moves below the other, "12 × 4 = 48"; the strip says "Half of 8 is 4 and double 6 is 12, so 6 × 8 = 12 × 4 = 48." Help: guided.
- Activity 3 (independent). Goal line: "Cut the array and write the new problem." Goal chip: "7 × 10". Setup: 7 rows of 10, 70 packets. Guess: which side can be cut into two equal halves: cards "The 7 rows", "The 10 columns". The child cuts, moves the halves and writes the new problem. Result: "14 × 5 = 70"; the strip says "7 is odd, so cut the 10 columns: half of 10 is 5 and double 7 is 14. 7 × 10 = 14 × 5 = 70." Help: independent.
- Activity 4 (independent). Goal line: "Halve and double to make it easy." Goal chip: "5 × 36". Setup: a block of 5 by 36, 180 packets. Guess: "Will one new number be 10?" cards "Yes", "No". Result: "10 × 18 = 180"; the strip says "Half of 36 is 18 and double 5 is 10, so 5 × 36 = 10 × 18 = 180. A 10 makes it easy." Help: independent.
- Activity 5 (independent). Goal line: "Halve and double again and again." Goal chip: "25 × 16". Setup: a block of 25 by 16, 400 packets. Guess: how many cuts until one number is 100: cards "1", "2", "3". The child cuts twice. Result: "25 × 16 = 50 × 8 = 100 × 4 = 400"; the strip says "Doubling 25 twice makes 100, and 100 × 4 = 400." Help: independent.
5. Mathematical Understanding
- Cutting and moving shows that no packet is added or lost, so the total is the same: one side halves and the other doubles. Rules: "Halve one number and double the other, and the product stays the same." "Halving and doubling works well with 5 and 25, because doubling makes 10 or 100."
6. Feedback and Hints
- Wrong answer: the strip turns red, the objects shake a little, one friendly line says what to look at. No scores, retry is free; the expected numbers are named only after the second try.
- Correct: the plate turns green, the halves bounce once, the goal chip turns green, the pill gets a tick, "Next" appears.
- Mistake: halves both numbers (M_HALVE_BOTH), for example 3 × 4 -> "Halve only one number and double the other. 3 × 4 is only 12 packets, but we started with 48." The Double arrow pulses.
- Mistake: doubles both (M_DOUBLE_BOTH), for example 12 × 16 -> "Doubling both would add packets. 12 × 16 is 192, but we can only move packets." The Half arrow pulses.
- Mistake: cut not in the middle -> "The two halves must be equal. Move the scissors line to the middle." The middle gap glows.
- Mistake: cuts an odd side -> "7 is odd, so 7 rows cannot be cut into two equal halves. Cut the other side." The other side glows.
- Hints (Hint button, 3 levels): (1) "Which number can be cut into two equal halves? Look at the rows and at the columns." (2) the side that can be halved glows and the cut line shows its middle. (3) the tool makes the cut and moves the halves; the child writes the new problem.
- Edge cases: when both sides are even either may be halved; any correct halve-and-double is accepted, for example 32 × 2 for 16 × 4. A new number that is 10 or 100 gets "That is an easy one!"
7. Ending
- Star Challenge 1 (the book's questions). Goal line: "Butter packets are arranged in the following way. Let us find a strategy to calculate the total number of packets." Goal chip: "Cut and move". Part (a): 3 rows of 18 packets are cut in the middle (between columns 9 and 10) and the halves put one below the other: the child builds 6 × 9 = 54 (Double the 3, Half the 18), then answers "Discuss why these are the same." by tapping "The same packets only moved." (two wrong cards). Part (b): "Butter packets are arranged in 22 rows of 5 packets. The arrangement is cut in the middle and the two halves are put side by side. 22 × 5 becomes ___ × ___ = ____." The child cuts, moves and writes 11 × 10 = 110. Why: "Half of 22 is 11 and double 5 is 10, so 22 × 5 = 11 × 10 = 110." Help: independent.
- Star Challenge 2 (the book's question). Goal line: "Solve the following problems like the previous ones. Halve one number, double the other." Goal chip: "4 problems". Problems 14 × 3, 16 × 4, 38 × 5, 35 × 14; the child writes each new problem as ___ × ___ and the product. Answers: 7 × 6 = 42; 8 × 8 = 64; 19 × 10 = 190; 70 × 7 = 490. 35 is odd, so the 14 is halved and the 35 doubled. Help: independent.
- Star Challenge 3 (the book's question). Goal line: "Find the product by halving and doubling either the multiplier or the multiplicand." Goal chip: "6 products". Products 5 × 18, 50 × 28, 15 × 22, 25 × 12, 12 × 45, 16 × 45. Answers: 10 × 9 = 90; 100 × 14 = 1,400; 30 × 11 = 330; 50 × 6 = 300 and again 100 × 3 = 300; 6 × 90 = 540; 8 × 90 = 720. The child may cut again and again before writing the product. Help: independent.
- Star Challenge 4 (the book's question). Goal line: "Give 5 examples of multiplication problems where halving and doubling will help in finding the product easily. Find the products as well." Goal chip: "5 examples". Two steppers (2 to 60) set the rows and the packets in a row; the child cuts, moves and writes the product. An example counts when the number that is doubled ends in 5 or is 50, so the new problem has a multiple of 10 in it, and the problem is new. After each: "Good one! 5 × 24 = 10 × 12 = 120." (the child's own numbers). Samples: 5 × 24 = 120, 25 × 24 = 600, 15 × 14 = 210, 50 × 36 = 1,800, 35 × 12 = 420. Help: independent.
- End screen: "Well done!" Remember: "Halve one number and double the other, and the product stays the same." "Never halve both or double both." "A 5 or a 25 makes it easy, because doubling gives 10 or 100." Think and talk: "Why does halving and doubling work well with 5 and 25?" Button: "Start again".
8. Assets and Language
- Images: photo of a steel packing table in a dairy; photo cut-out of a butter block in yellow foil (one image repeated); scissors icon, dashed cut line, number boxes, Half and Double arrows, tags, cards and the solid yellow block for big arrays (code-drawn). Simple English, no scores.
"""

# ======================================================================================================
# Tool 4: Nearest Multiple Grid
# ======================================================================================================
OBJECTIVES["M2.S13.T13.C54.2D1"] = (
    "The student sees that rounding one number to the nearest multiple of 10 counts a strip of squares too many or too "
    "few, so the product is fixed by taking the strip away or adding it.")

DESCRIPTIONS["M2.S13.T13.C54.2D1"] = """
A. TOOL TITLE
- Nearest Multiple Grid
B. TOOL INFO
- Tool ID: M2.S13.T13.C54.2D1
- Tool type: Concept-activity
- Textbook source: The Dairy Farm, Nearest Multiple: the pictures of 4 × 19 (white strip, subtract 4) and 14 × 21 (green strip, add 14), the question asking for 5 examples of the student's own, and the six products 7 × 52, 12 × 28, 75 × 31, 99 × 15, 8 × 25, 22 × 42. Practice values of the plan: 7 × 29, 8 × 41, 6 × 38, 9 × 62, 5 × 48, 11 × 69, 6 × 35 (developer only).
C. LEARNING OBJECTIVE
- The student sees from a grid of squares why a product found with the nearest multiple of 10 needs a strip taken away when the number was rounded up, or added when it was rounded down.
- Out of scope: rounding to hundreds, estimating, rounding both numbers.
D. TOOL DESCRIPTION
1. Opening Screen
- Photo of a shallow wooden tray on the dairy packing table. The tray holds 7 rows of 29 small yellow square tiles (each about a finger-nail wide). The numbers are written along the tray: "7" down its left side and "29" along its top.
- Instruction line: "Round 29 to the nearest multiple of 10 and watch the strip."
- The number "29" pulses: the child is invited to tap it.
2. Scene and Objects
- Grid: rows of equal yellow squares. A grid with more than 20 rows or 49 squares in a row is drawn as a solid yellow block with a square pattern and its side numbers.
- Frame: when a number is rounded, a dashed frame shows the rounded grid, for example 7 by 30. The friendly product appears under the tray, for example "7 × 30 = 210".
- Strip: when the tapped number is the squares in a row, a column of squares at the end of the rows (1 or 2 squares wide); when it is the number of rows, a row of squares across the tray. White squares with a dashed edge mean the frame counts squares that are not there. Green squares mean the frame leaves squares out.
- Two big chips "Take away" and "Add", two empty number boxes (strip size, product) with a number pad that opens on tap.
- Goal chip: a wooden tag such as "7 × 29". Guess cards: three big cards when a guess is asked.
3. Main Interaction
- Tap a number to round it to the nearest multiple of 10 (either number may be tapped). The frame and the strip then appear.
- The child drags the strip away from the tray or onto it, picks "Take away" or "Add", types the number of squares in the strip and the product.
- Bottom buttons (only three): "Hint", "Reset" (restores the grid), "Check" (becomes "Next").
4. Activities
- Activity 1 (guided). Goal line: "Round 29 to the nearest multiple of 10." Goal chip: "7 × 29". Setup: 7 rows of 29. Guess: will the rounded grid hold "More", "Fewer" or "The same" squares than the tray? Result: a white strip of 7 squares, one in each row; the child takes it away and writes 203. Strip: "29 is 1 less than 30, so 30 counts 1 extra square in each of the 7 rows. Take away 7: 7 × 29 = 7 × 30 − 7 = 210 − 7 = 203." Help: guided, labels "1 in each row" and a count on the strip.
- Activity 2 (guided). Goal line: "Round 41 to the nearest multiple of 10." Goal chip: "8 × 41". Setup: 8 rows of 41. Same guess. Result: a green strip of 8 squares; the child adds it and writes 328. Strip: "41 is 1 more than 40, so 40 leaves out 1 square in each of the 8 rows. Add 8: 8 × 41 = 8 × 40 + 8 = 320 + 8 = 328." Help: guided.
- Activity 3 (guided). Goal line: "How many squares are in each row of the strip?" Goal chip: "6 × 38". Setup: 6 rows of 38. Guess: cards "1", "2", "3". Result: a white strip with 2 squares in each of the 6 rows, 12 in all. Strip: "38 is 2 less than 40, so the strip has 2 squares in each of the 6 rows: 6 × 2 = 12. 6 × 38 = 6 × 40 − 12 = 240 − 12 = 228." Help: guided, labels.
- Activity 4 (independent). Goal line: "Round, then take away or add the strip." Goal chip: "3 grids". Three grids: 9 × 62, 5 × 48, 11 × 69, each with the same guess. Answers: 9 × 62: add 18, 9 × 60 + 18 = 540 + 18 = 558; 5 × 48: take away 10, 5 × 50 − 10 = 250 − 10 = 240; 11 × 69: take away 11, 11 × 70 − 11 = 770 − 11 = 759. Help: independent, no labels.
- Activity 5 (independent). Goal line: "35 is in the middle. Try both ways." Goal chip: "6 × 35". Guess: which multiple of 10 is nearer to 35: cards "30", "40", "Both are the same". The child makes both plans. Result: round to 30, a green strip of 5 per row, 6 × 30 + 30 = 180 + 30 = 210; round to 40, a white strip, 6 × 40 − 30 = 240 − 30 = 210. Strip: "35 is as far from 30 as from 40. Both ways give 210." Help: independent.
5. Mathematical Understanding
- The frame of the rounded grid is easy to count but is not the real grid. A white strip is counted by mistake, so it is taken away; a green strip is left out, so it is added.
- The strip has as many squares as the other number for every 1 the rounded number moved: 7 rows and a gap of 1 make 7 squares. Rules: "Round one number to the nearest multiple of 10 and multiply. Take away the strip counted by mistake, or add the strip left out."
6. Feedback and Hints
- Wrong answer: the strip turns red, the grid shakes a little, one friendly line says what to look at. No scores, retry is free; the expected number is named only after the second try.
- Correct: the strip and the plan turn green, the grid bounces once, the goal chip turns green, the pill gets a tick, "Check" becomes "Next".
- Mistake: writes the rounded product only, for example 210 for 7 × 29 (M_NO_ADJUST) -> "210 is the answer for the rounded grid. The strip is still in the picture: take it away or add it." The strip pulses.
- Mistake: wrong strip size, for example 29 for 7 × 29 (M_WRONG_STRIP) -> "The strip has 1 square in each row. How many rows are there?" The rows pulse.
- Mistake: wrong choice of Take away or Add -> "White squares are not really there. Green squares were left out. Which colour is this strip?" The strip pulses.
- Mistake: rounds to the wrong multiple, for example 29 to 20 -> "29 is nearer to 30 than to 20. Which multiple of 10 is nearest?" The number pulses.
- Hints (Hint button, 3 levels): (1) "Which multiple of 10 is nearest to the number in each row?" (2) the frame of the rounded grid appears with the strip outlined. (3) the strip is counted for the child: "For 7 × 29 the white strip has 7 squares. 7 × 30 = 210, so take 7 away."
- Edge cases: a number exactly in the middle, 25 or 35, can be rounded either way and both plans are right. 99 rounds up to 100. A number that is already a multiple of 10 has no strip: "30 is already a multiple of 10, so there is no strip."
7. Ending
- Star Challenge 1 (the book's questions). Part (a) goal line: "Find 4 × 19 using the nearest multiple of 10. Observe the picture and find why we need to subtract 4." Goal chip: "Why subtract 4?" Setup: 4 rows of 19. The child rounds 19 to 20, sees the white strip, and taps the reason "The 20th square of each row is not there: 4 rows, so 4 squares." (two wrong cards: "Because 4 is the first number." "Because 19 is a big number."). Then the plan: 4 × 19 = 4 × 20 − 4 = 80 − 4 = 76. Part (b) goal line: "Find 14 × 21 using the nearest multiple of 10. Observe the picture and find why we need to add 14." Goal chip: "Why add 14?" Setup: 14 rows of 21; a green strip appears; reason: "14 × 20 leaves out the 21st square of each row: 14 rows, so 14 squares." Plan: 14 × 21 = 14 × 20 + 14 = 280 + 14 = 294. Help: independent.
- Star Challenge 2 (the book's question). Goal line: "Give 5 examples of problems where you can use the nearest multiple to find the product easily. Find the products as well." Goal chip: "5 examples". Two steppers (2 to 99) set the rows and the squares in a row; the child rounds, chooses, types the strip and the product. An example counts when the number is 1 or 2 away from a multiple of 10 and the problem is new. After each: "Good one! 6 × 29 = 6 × 30 − 6 = 174." (the child's own numbers). Sample answers: 6 × 29 = 174; 5 × 41 = 205; 13 × 19 = 247; 9 × 31 = 279; 8 × 99 = 792. Help: independent.
- Star Challenge 3 (the book's question). Goal line: "Find the products of the following numbers by finding the nearest multiple." Goal chip: "6 products". Products 7 × 52, 12 × 28, 75 × 31, 99 × 15, 8 × 25, 22 × 42, each with the guess. Answers: 7 × 52 = 350 + 14 = 364; 12 × 28 = 360 − 24 = 336; 75 × 31 = 2,250 + 75 = 2,325; 99 × 15 = 1,500 − 15 = 1,485; 8 × 25 = 240 − 40 = 200; 22 × 42 = 880 + 44 = 924. Any correct plan is accepted. Help: independent.
- End screen: "Well done!" Remember: "Round one number to the nearest multiple of 10, then fix the product." "A strip counted by mistake is taken away. A strip left out is added." "The strip has one square in each row." Think and talk: "Why do we add 14 for 14 × 21 but take away 4 for 4 × 19?" Button: "Start again".
8. Assets and Language
- Images: photo of a shallow wooden tray on a dairy packing table; yellow and green square tiles, white dashed squares, dashed frame, chips, tags, cards, number pad and the solid yellow block for big grids (code-drawn).
- Simple English, no scores.
"""

# ======================================================================================================
# Tool 5: Box and Lines
# ======================================================================================================
OBJECTIVES["M3.S18.T18.C79.2D1"] = (
    "The student sees that splitting both numbers into tens and ones gives small products that can sit in a box, in "
    "Kanti's four lines or in John's two lines, and that adding them gives the same product.")

DESCRIPTIONS["M3.S18.T18.C79.2D1"] = """
A. TOOL TITLE
- Box and Lines
B. TOOL INFO
- Tool ID: M3.S18.T18.C79.2D1
- Tool type: Concept-activity
- Textbook source: The Dairy Farm, Waste and Composting: Nida's box, Kanti's four lines and John's two lines for 12 × 35 and 24 × 150; Let Us Multiply 32 × 8 and 69 × 45; Let Us Do (like Nida, like Kanti, like John, five stories). Practice values: 42 × 13, 61 × 24, 140 × 15 (developer only).
C. LEARNING OBJECTIVE
- The student sees that splitting both numbers into tens and ones (and hundreds) gives small products that can be written in a box, in Kanti's four lines or in John's two lines, and that adding them gives the same product.
- Out of scope: carries, estimating, dividing.
D. TOOL DESCRIPTION
1. Opening Screen
- Photo of a village compost pit (brown heap, green leaves, low fence). In front stands a painted wooden notice board with number tags "42" and "13" and an empty chalk-drawn box. A wooden shelf under it holds round chips like bottle caps, each showing a number.
- Instruction line: "Tap 42 to split it into tens and ones." The tag "42" pulses; tapped, it splits into "40" and "2" above the box. "13" splits into "10" and "3" beside it.
2. Scene and Objects
- Box: parts of the first number across the top, parts of the second down the side, one cell for each small product. A zero place has no part: 140 is 100 + 40, 507 is 500 + 7.
- Chips: guided activities have only the right chips; independent ones add a look-alike with one zero more or less (20 beside 200). Guided cells show their multiplication, for example "40 × 10".
- Three tabs on the board's top edge: "Box", "Kanti's lines", "John's lines". Kanti: a line for each small product, its multiplication in brackets. John: a line for each part of the second number, with a slot for every place of the first number, labelled for example "(3 × 42)".
- A round "Add" button, a number pad, a goal chip and guess cards.
3. Main Interaction
- Tap a number tag to split it. Drag a chip into a cell or line slot: a right chip sticks with a soft pop, a wrong one bounces back.
- "Add" slides out the column sums, then the total; in independent activities and star challenges the child types the total.
- A tab moves the same chips into the other layout. A printed zero beside a blank stays: a chip 24 beside a printed 0 reads 240.
- Bottom buttons (only three): "Hint", "Reset", "Check" (becomes "Next").
4. Activities
- Activity 1 (guided). Goal line: "Split both numbers and fill the box." Goal chip: "42 × 13". Guess: small products in the box: "2", "4", "6". Result: cells 400 and 20 (row 10), 120 and 6 (row 3); column sums 520 and 26; total 546. Strip: "400 + 20 + 120 + 6 = 546, so 42 × 13 = 546." Help: guided, labelled cells.
- Activity 2 (guided). Goal line: "Kanti writes each small product on its own line." Goal chip: "Kanti's lines". Setup: the box of 42 × 13. Guess: "The same four products" or "New products". Result: lines 6 (3 × 2), 120 (3 × 40), 20 (10 × 2), 400 (10 × 40). Strip: "Kanti's four lines use the same four small products: 6 + 120 + 20 + 400 = 546." Help: guided.
- Activity 3 (guided). Goal line: "John joins small products in each line." Goal chip: "John's lines". Guess: lines John needs: "1", "2", "4". Result: 120 + 6 = 126 (3 × 42) and 400 + 20 = 420 (10 × 42). Strip: "John's two lines: 126 + 420 = 546, the same small products." Help: guided.
- Activity 4 (independent). Goal line: "Fill the box. Watch the zeros." Goal chip: "61 × 24". Guess: the product is nearest to "1,000", "1,500", "2,000". Result: cells 1,200, 20, 240, 4; sums 1,440 and 24; total 1,464. Strip: "61 × 24 = 1,200 + 20 + 240 + 4 = 1,464, close to 60 × 25 = 1,500." Help: independent, no cell labels.
- Activity 5 (independent). Goal line: "Fill the box." Goal chip: "140 × 15". Guess: cells: "4" or "6". Result: cells 1,000, 400, 500, 200; sums 1,500 and 600; total 2,100. Strip: "140 has no ones, so it splits into 100 + 40 only: 1,000 + 400 + 500 + 200 = 2,100." Help: independent.
5. Mathematical Understanding
- Every part of one number meets every part of the other. The box, Kanti's lines and John's lines hold the same small products; only the layout changes. Rule: "Split both numbers, multiply the parts, then add."
6. Feedback and Hints
- Wrong answer: the strip turns red, the chip or box shakes a little, one friendly line says what to look at. No scores, retry is free; the product is named only after the second try.
- Correct: the cell lights up, the goal chip turns green, the pill gets a tick, "Next" appears.
- Mistake: a missing zero (M_MISSING_ZERO), for example 4 for 40 × 10 -> "Keep the zeros: 40 × 10 is 4 tens times 1 ten, which is 4 hundreds, so 400." The tens parts glow.
- Mistake: Add with empty cells (M_SPLIT_ONE) -> "Every part of one number meets every part of the other. The empty cells are waiting." They pulse.
- Mistake: a chip in the wrong cell -> "That chip is 120, from 3 × 40. Look at the top of the column and the side of the row."
- Mistake: in a story, every pair multiplied (M_MULT_ALL) -> "Not every pair of numbers is multiplied. Which belong together in the story?"
- Hints (Hint button, 3 levels): (1) "How many tens and ones does each number have? Split both numbers first." (2) the row part and column part of the next empty cell glow: "Which two numbers make this cell?" (3) the tool fills one cell, for example "40 × 10 = 400", and the child fills the rest.
7. Ending
- Star Challenge 1 (the book's questions). Goal line: "A family of 4 produces around 35 kg of kitchen waste in a month. How much waste will the family produce in a year? Quantity of kitchen waste in 1 month is 35 kg. Quantity of kitchen waste in 12 months is 12 × 35 kg." Goal chip: "12 × 35". The child fills the box (300, 50, 60, 10), switches to Kanti's lines (10, 60, 50, 300) and John's lines, 60 + 10 = 70 and 300 + 50 = 350, and types 420 kg. The book's "How are these solutions same or different?" is the strip: "The same four small products, only the layout is different." Part 2: "The family regularly composts the collected waste. They get around 150 kg of compost each year, which they use in their garden. 1 kg of compost is often sold in the market at ₹24. By creating their own compost, how much money have they saved in a year? Savings on 1 kg compost is ₹24. Savings on 150 kg will be ₹24 × 150." Goal chip: "₹24 × 150". Cells 2,000, 1,000, 400, 200; sums 2,400 and 1,200; total ₹3,600. Kanti: 200, 400, 1,000, 2,000. John: 400 + 200 + 0 = 600 and 2,000 + 1,000 + 0 = 3,000 (the 0 is the ones of 150). Help: independent.
- Star Challenge 2 (the book's question). Goal line: "Let Us Multiply." Goal chip: "32 × 8 and 69 × 45". (a) 32 × 8: box with columns 30 and 2 and row 8; Kanti: ___ (8 × 2), ___0 (8 × 30), total 256; John: ___0 + 16 gives 256. Answers: cells 240 and 16; blanks 16, 24, 24. (b) 69 × 45: box with columns 60 and 9, rows 40 and 5 (sums and total given); Kanti: 45 (5 × 9), ___0 (5 × 60), ___0 (40 × 9), ___00 (40 × 60); John: 300 + ___ = 345 (5 × 69), ___ + ___ = 2,760 (40 × 69). Answers: cells 2,400, 360, 300, 45; Kanti blanks 30, 36, 24; John blanks 45, then 2,400 and 360. Help: independent.
- Star Challenge 3 (the book's questions). Goal lines: "Solve the following problems like Nida did." then "like Kanti." then "like John." Goal chip: "12 problems". Three rounds of four, each opening in its layout. Like Nida (box): 78 × 4, 83 × 9, 67 × 28, 53 × 37, answers 312, 747, 1,876, 1,961. Like Kanti (four lines): 94 × 5, 49 × 6, 37 × 53, 28 × 79, answers 470, 294, 1,961, 2,212. Like John (two lines): 86 × 3, 72 × 7, 94 × 36, 66 × 22, answers 258, 504, 3,384, 1,452. Help: independent.
- Star Challenge 4 (the book's questions). Goal line: "Solve the following problems." Goal chip: "5 stories". Each story is pinned on the board in the book's words; the child taps the numbers to multiply, fills a box for each multiplication and types the answers. (a) "A movie theater has 8 rows of seats, and each row has 12 seats. If half the seats are filled, how many people are watching the movie? If 3 more rows get filled, how many total people will be there?" Boxes 8 × 12 = 96 and 3 × 12 = 36; 48 people, then 48 + 36 = 84. (b) "In a test match between India and West Indies, the Indian team hit twenty-four fours and eighteen sixes across the two innings. How many runs were scored in fours and sixes each? 234 runs were made by running between the wickets. If 23 runs were extras, how many runs were scored by Indian team in the two innings?" Boxes 24 × 4 = 96 and 18 × 6 = 108; 96 + 108 + 234 + 23 = 461. (c) "Anjali buys 15 bulbs and 12 tube lights from Sudha Electricals. Each bulb costs ₹25 and each tube light costs ₹34. How much money should Anjali give to the shopkeeper?" 15 × 25 = 375 and 12 × 34 = 408; ₹783. (d) "A shopkeeper sold 28 bags of rice. Each bag costs ₹350. How much money did he earn by selling rice bags?" 28 × 350 = ₹9,800. (e) "A school library has 86 shelves and each shelf has 162 books. Find the number of books in the library." 86 × 162 = 13,932 books. Help: independent.
- End screen: "Well done!" Remember: "Split both numbers into tens and ones, and multiply every part by every part." "The box, Kanti's lines and John's lines hold the same small products." "Keep the zeros: 10 × 20 is 200." Think and talk: "Which way do you like best, the box or the lines? Why?" Button: "Start again".
8. Assets and Language
- Images: photo of a village compost pit with a fence; photo cut-out of a painted wooden notice board; round chips, number tags, tabs, goal tags and story notes (code-drawn). Simple English, no scores.
"""

# ======================================================================================================
# Tool 6: Carry Columns
# ======================================================================================================
OBJECTIVES["M3.S22.T22.C106.2D1"] = (
    "The student sees that multiplying place by place from the ones works when each carry is written above the next "
    "column and added after that column is multiplied.")

DESCRIPTIONS["M3.S22.T22.C106.2D1"] = """
A. TOOL TITLE
- Carry Columns
B. TOOL INFO
- Tool ID: M3.S22.T22.C106.2D1
- Tool type: Concept-activity
- Textbook source: The Dairy Farm, Dairy Cooperative: Mili's father's method for 268 × 4, 453 × 13 and 574 × 125 (with the same coloured digits), and Let Us Solve (problems like Nida, like John and like Mili's father). Practice values of the plan: 127 × 3, 358 × 4, 63 × 8, 138 × 24, 215 × 304 (developer only).
C. LEARNING OBJECTIVE
- The student sees that multiplying place by place from the ones works when each carry is written above the next column and added after that column is multiplied, and that each digit of the multiplier gets its own row with a 0 or 00 at the end.
- Out of scope: estimating as a topic, dividing, numbers above 99,999.
D. TOOL DESCRIPTION
1. Opening Screen
- Photo of the dairy cooperative's office desk: a wooden desk with an open ledger, a pen and a rubber stamp. The ledger page fills the stage, its columns headed "Ten thousands", "Thousands", "Hundreds", "Tens", "Ones". The number 127 sits in the last three columns with an empty carry circle above each, "× 3" below it, a ruled line and one empty row.
- Instruction line: "Multiply one column. Write the carry above the next column."
- A pencil pointer rests at the Ones column and pulses: the child is invited to start there.
2. Scene and Objects
- Carry page: the first number, a carry circle above each column, the multiplier below, one row for each digit of the multiplier (with a 0 already printed at the end of the tens row and 00 at the end of the hundreds row), and a "Total" row. The pencil shows the multiplication of its column, for example "3 × 7", and the carry that is waiting.
- Nida's page: a box with the parts of the first number across and of the second down, and a shelf of round chips, every right chip with a look-alike with one zero more or less. John's page: one line for each part of the second number, each with its label such as "(4 × 123)" and slots for the small products joined by "+".
- Number pad, round "Add rows" button, goal chip (wooden tag such as "127 × 3"), guess cards.
3. Main Interaction
- Carry page: the child types one number for the column, the product of the digits plus the carry waiting. Its digits appear as tiles: the last digit is dragged into the row under the column, the other digits into the carry circle of the next column. In the leftmost column the whole number is written.
- With more rows, the child fills each row from the right, then presses "Add rows" and types the total. Nida's and John's pages: drag chips into cells or slots, then type the total.
- Bottom buttons (only three): "Hint", "Reset" (clears this problem), "Check" (becomes "Next").
4. Activities
- Activity 1 (guided). Goal line: "Multiply 127 by 3, column by column." Goal chip: "127 × 3". Guess: 3 × 7 = 21, what goes in Ones: cards "21", "1 and carry 2", "2 and carry 1". Result: 1 in Ones, carry 2 above Tens; then 3 × 2 = 6 and 6 + 2 = 8; then 3 × 1 = 3: 381. Strip: "3 × 7 = 21: write 1 and carry 2. 3 × 2 = 6, and 6 + 2 = 8. So 127 × 3 = 381." Help: guided, the pencil shows each multiplication and the waiting carry.
- Activity 2 (guided). Goal line: "Multiply 358 by 4." Goal chip: "358 × 4". Guess: the product is nearest to "1,200", "1,400", "1,600". Result: 4 × 8 = 32, write 2, carry 3; 4 × 5 = 20, 20 + 3 = 23, write 3, carry 2; 4 × 3 = 12, 12 + 2 = 14, write 14: 1,432. Strip: "358 × 4 = 1,432, close to 360 × 4 = 1,440." Help: guided.
- Activity 3 (independent). Goal line: "Multiply 63 by 8." Goal chip: "63 × 8". Guess: when the carry 2 is added: cards "Before multiplying the 6", "After multiplying the 6". Result: 8 × 3 = 24, write 4, carry 2; 8 × 6 = 48, 48 + 2 = 50, write 0, carry 5; write 5: 504. Strip: "The carry is added after multiplying: 8 × 6 = 48, and 48 + 2 = 50. So 63 × 8 = 504." Help: independent.
- Activity 4 (guided). Goal line: "One row for each digit of 24." Goal chip: "138 × 24". Guess: rows needed: cards "1", "2", "3". Result: row 1 is 4 × 138 = 552; row 2 starts with the printed 0 and holds 2 × 138 = 276, so 2,760; Add rows: 552 + 2,760 = 3,312. Strip: "4 × 138 = 552 and 20 × 138 = 2,760, so 138 × 24 = 3,312." Help: guided.
- Activity 5 (independent). Goal line: "Multiply 215 by 304." Goal chip: "215 × 304". Guess: zeros printed at the end of the hundreds row: cards "1", "2", "3". Result: 4 × 215 = 860; the tens row is 0 because 304 has 0 tens; the hundreds row is 00 then 645, which is 64,500; 860 + 0 + 64,500 = 65,360. Strip: "304 has 0 tens, so that row is 0: 860 + 0 + 64,500 = 65,360." Help: independent.
5. Mathematical Understanding
- Each column's product is a number of that place's units, so only its last digit stays and the rest moves to the next place as the carry, added after that column is multiplied. A tens row is 10 times a ones row, so it ends with a 0, and a hundreds row ends with 00.
- Rules: "Multiply the column first, then add the carry." "Write a 0 at the end of the tens row and 00 at the end of the hundreds row."
6. Feedback and Hints
- Wrong answer: the strip turns red, the page shakes a little, one friendly line says what to look at. No scores, retry is free; the expected digit is named only after the second try.
- Correct: the digit locks in, the carry hops to the next circle, the goal chip turns green, the pill gets a tick, "Next" appears.
- Mistake: adds the carry before multiplying (M_CARRY_FIRST) -> "Multiply the column first, then add the carry: 8 × 6 = 48, and 48 + 2 = 50." The waiting carry pulses.
- Mistake: carry in the wrong circle -> "The carry goes above the next column to the left." It slides back.
- Mistake: writes both digits in one column -> "Only the last digit stays in the column. The other digit is the carry for the next column." The carry circle pulses.
- Mistake: tens or hundreds row without its 0 or 00 (M_MISSING_ZERO) -> "This row is for tens, so it starts with a 0. Without it the product is 10 times too small." The printed zeros blink.
- Hints (Hint button, 3 levels): (1) "Which column is the pencil on? Multiply its digit by the digit of the number below." (2) the waiting carry glows: "Multiply the column first, then add the carry that came from the right." (3) the tool shows the column: "For 4 × 6 with a carry of 3: 4 × 6 = 24, and 24 + 3 = 27. Write 7 and carry 2."
- Edge cases: a 0 digit still takes a column (806 × 9: 9 × 0 = 0, and 0 + 5 = 5); a 0 digit in the multiplier gives a row of 0; the leftmost column writes the whole number.
7. Ending
- Star Challenge 1 (the book's questions). Goal line: "A dairy cooperative in a small town gets its milk from 268 villagers. Each villager has at least 4 milk-giving cows. What is the minimum number of cows the dairy cooperative gets its milk from?" Goal chip: "268 × 4". Answer 1,072 cows: 4 × 8 = 32, write 2, carry 3; 4 × 6 = 24, 24 + 3 = 27, write 7, carry 2; 4 × 2 = 8, 8 + 2 = 10. Then "Among the villagers, there are 453 Gir cows. Each of these cows give 13 litres of milk each day. How many litres of milk does the dairy cooperative receive from Gir cows everyday?" Rows 3 × 453 = 1,359 and 10 × 453 = 4,530; total 5,889 litres. Then "The dairy cooperative sells 1 kg cow ghee for ₹574. The cooperative is able to produce around 125 kg of ghee in a month. How much do they earn by selling ghee in a month? Discuss what the same coloured digits might mean." Rows 2,870, 11,480, 57,400; total ₹71,750. In the ghee rows digits of one place share a colour; the child taps a same-coloured pair and the strip says "Digits of the same colour sit in the same place, so they are added together." Help: independent.
- Star Challenge 2 (the book's question). Goal line: "Solve the following problems like Nida." Goal chip: "5 problems". Nida's page: 548 × 6 = 3,288; 682 × 3 = 2,046; 324 × 18 = 5,832; 507 × 23 = 11,661; 190 × 65 = 12,350. A number with a 0 digit has no part for it. Help: independent.
- Star Challenge 3 (the book's question). Goal line: "Solve the following problems like John." Goal chip: "6 problems". John's page: 123 × 84 = 10,332; 368 × 32 = 11,776; 159 × 324 = 51,516; 239 × 401 = 95,839; 592 × 5 = 2,960; 101 × 22 = 2,222. A 0 digit of the multiplier has no line. Help: independent.
- Star Challenge 4 (the book's questions). Goal line: "Let us solve a few questions like Mili's father." Goal chip: "12 problems". Carry page with the place value frames: 806 × 9 = 7,254; 455 × 26 = 11,830; 143 × 208 = 29,744. Then "Now use Mili's father's method to solve the following questions.": 807 × 5 = 4,035; 143 × 28 = 4,004; 309 × 9 = 2,781; 450 × 38 = 17,100; 584 × 23 = 13,432; 302 × 13 = 3,926; 604 × 54 = 32,616; 112 × 23 = 2,576; 237 × 19 = 4,503. Help: independent.
- End screen: "Well done!" Remember: "Multiply the column first, then add the carry." "Write the carry above the next column." "Put a 0 at the end of the tens row and 00 at the end of the hundreds row." Think and talk: "Why is the carry added after multiplying and not before?" Button: "Start again".
8. Assets and Language
- Images: photo of an office desk with an open ledger, a pen and a rubber stamp; ledger page with ruled columns, pencil pointer, carry circles, digit tiles, chips and number pad (code-drawn). Simple English, no scores.
"""
