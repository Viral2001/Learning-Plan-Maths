# -*- coding: utf-8 -*-
"""Topics T1, T1B (module M1: Folding and Lines of Symmetry) and T2, T3 (module M2: Turning and Rotational Symmetry).
The framing intro (Prem and Manu's birthday cutouts hook and the free Fold and Cut tool), the short idea topic T1B (half
and quarter cutouts, with the opener's letter questions), Turns and the Windmill Firki, and Reflection, Rotation or Both
(the digits). Every teaching concept has one worked example with the plan's own letters and shapes; every book question
is an FIO item of its topic's DOER, in the book's order."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T1 Happy Birthday Cutouts (framing) ========================================
# The framing topic holds only the hook video and the free-try tool, and no book question. The concept video and the
# opener's questions follow in the short idea topic T1B.
TOPICS.append(TOPIC(
    "T1", "M1", "Happy Birthday Cutouts", ["Chapter opening"], "Understand",
    "",
    "Prem and Manu are cutting the letters of 'Happy Birthday' out of paper for Lali's birthday wall. Some letters can be "
    "cut out in an easy way. Fold a paper, cut, open it and find out which ones.",
    [A("T1.C1", "Prem and Manu's Birthday Cutouts", "Understand",
       "",
       textbook=["Prem and Manu want to paste 'Happy Birthday' cutouts on a wall for Lali's birthday. While preparing "
                 "cutouts of letters, they observe that some letters can be cut out in an easy way. They remember that "
                 "they learnt about reflection symmetry and lines of symmetry in Grade 4."],
       teach=["Predict first: Prem and Manu are cutting the letters of 'Happy Birthday' out of paper for Lali's birthday "
              "wall. Do you think every letter has to be drawn and cut out all the way round?",
              "Prem and Manu want to paste 'Happy Birthday' cutouts on a wall for Lali's birthday.",
              "While preparing cutouts of letters, they observe that some letters can be cut out in an easy way.",
              "They remember that they learnt about reflection symmetry and lines of symmetry in Grade 4.",
              "Which letters can be cut out the easy way? Think about it, then try folding paper and cutting on the "
              "next screen."],
       ncert=["open.story"], key_terms=["cutout", "letter", "symmetry"],
       video_focus=["HOOK"], enrichment=True, minutes=4),
     DOER("T1.C3", "Fold and Cut: Explore", "fold_and_cut", "Understand",
          "",
          ["Prem and Manu cut letters out of folded paper.",
           "Some letters can be cut out by drawing only a part of the letter along the fold.",
           "Fold, draw, cut and open the paper to find out which letters work."],
          misconceptions=["M_ANY_LINE"], role="try_it", enrichment=True)],
    topic_type="framing", key_terms=["fold", "cutout", "letter"]))

# ============================== T1B Half and Quarter Cutouts ===============================================
TOPICS.append(TOPIC(
    "T1B", "M1", "Half and Quarter Cutouts", ["Alphabet Cutout"], "Understand",
    "Students cut out a letter by folding paper along its line of symmetry and drawing half or a quarter of it, and "
    "name the horizontal and vertical lines of symmetry of letters.",
    "A line of symmetry splits a shape into two halves that match when the shape is folded along the line. A letter "
    "with one line of symmetry can be cut out by drawing half of it on folded paper, and a letter with two lines by "
    "drawing a quarter of it. Lines go across (horizontal) or up and down (vertical).",
    [A("T1B.C1", "Fold on a Line of Symmetry", "Understand",
       "Students fold a paper along a line of symmetry and draw half or a quarter of a letter along the fold to make the "
       "full letter cutout.",
       textbook=["The letter A has a vertical line of symmetry. So, to cut out the letter A: 1. Fold a paper in half. "
                 "2. Draw half of the letter A along the fold. 3. Cut along the outline. 4. Open the paper to see the "
                 "full letter A.",
                 "The letter H has two lines of symmetry. 1. Fold the paper into one-fourth (once vertically, once "
                 "horizontally). 2. Draw one-fourth of the letter H along the fold. 3. Cut along the outline. 4. Open "
                 "the paper to see the full letter H."],
       teach=["Predict first: Prem folds a paper in half, draws half of the letter A along the fold and cuts along the "
              "outline. What will the opened paper show?",
              "It shows the full letter A. The letter A has a vertical line of symmetry: the two halves on either side "
              "of the line match.",
              "A line of symmetry is a line that splits a shape into two halves that match exactly when the shape is "
              "folded along it.",
              "To cut out the letter A: fold a paper in half, draw half of the letter A along the fold, cut along the "
              "outline, and open the paper to see the full letter A.",
              "The letter H has two lines of symmetry, one vertical and one horizontal. So fold the paper into "
              "one-fourth, once vertically and once horizontally, and draw one-fourth of the letter H along the folds. "
              "Cut and open: the full letter H appears.",
              "Rule: with one line of symmetry, half (1/2) of the letter is enough. With two lines of symmetry, a "
              "quarter (1/4) is enough."],
       examples=[WE("Prem wants to cut out the letter M from a folded paper. Which fold should Prem use, and how much of "
                    "the M must be drawn?",
                    ["Look at the M. The left side and the right side match, so the M has a vertical line of symmetry.",
                     "Fold the paper in half along the vertical line.",
                     "Draw half of the M, which is 1/2 of the letter, along the fold.",
                     "Cut along the outline and open the paper: the full M appears.",
                     "Check: the top and the bottom of the M do not match, so it has no horizontal line. One fold is "
                     "all that works, and a quarter is not enough."],
                    "Fold the paper in half along the vertical line and draw 1/2 of the M")],
       ncert=["open.A", "open.H"], key_terms=["fold", "line of symmetry", "half", "quarter", "cutout"],
       misconceptions=["M_ANY_LINE", "M_ONE_LINE"], minutes=6),
     A("T1B.C2", "Horizontal and Vertical Lines of Symmetry", "Understand",
       "Students name the horizontal and the vertical lines of symmetry of a letter and say which letters have both "
       "lines.",
       teach=["Predict first: look at the letter B. Does it have a line of symmetry that goes across, or one that goes "
              "up and down?",
              "A vertical line goes up and down. A horizontal line goes across, from left to right.",
              "The letter B has a horizontal line: the top half and the bottom half match. It has no vertical line, "
              "because the left side and the right side do not match.",
              "Some letters have both. The letter H has a vertical line and a horizontal line.",
              "To find a line, imagine folding the letter along a vertical line, then along a horizontal line. If the "
              "two halves land exactly on each other, that line is a line of symmetry.",
              "Rule: check the vertical line, then the horizontal line, then say vertical, horizontal, both or none."],
       examples=[WE("Which lines of symmetry do the letters B, W and H have?",
                    ["B: fold along a vertical line. The left side is straight and the right side has two bumps, so "
                     "the halves do not match. Fold along a horizontal line. The top bump lands on the bottom bump, so "
                     "the halves match. B has a horizontal line only.",
                     "W: fold along a vertical line. The left half lands on the right half, so they match. Fold along "
                     "a horizontal line. The top and the bottom do not match. W has a vertical line only.",
                     "H: fold along a vertical line and the halves match. Fold along a horizontal line and the halves "
                     "match. H has both lines.",
                     "Check: only H has two lines, so only H needs a quarter fold."],
                    "B: horizontal line only. W: vertical line only. H: both lines")],
       key_terms=["horizontal line", "vertical line", "lines of symmetry", "both"],
       misconceptions=["M_ONE_LINE", "M_ANY_LINE"], minutes=5),
     DOER("T1B.C3", "Practice: Letter Cutouts", None, "Apply",
          "Students find which letters can be cut out by drawing half or a quarter, and name the letters with a "
          "horizontal line, a vertical line or both lines of symmetry.",
          ["A letter can be cut out from folded paper only if it has a line of symmetry.",
           "One line of symmetry needs a fold in half. Two lines need a fold into one-fourth.",
           "Fold each letter along a vertical line, then along a horizontal line, and see if the halves match."],
          items=[FIO("open.cutouts", "Alphabet Cutout: which letters can be cut out",
                     "Which of the following alphabet cutouts can be made by just drawing half (1/2) or quarter (1/4) "
                     "of the letter? You can do it by drawing lines of symmetry on the letters. The letters are E, N, "
                     "X, T, K, V and O.",
                     ["A letter can be cut out from a folded paper only if it has a line of symmetry.",
                      "E has a horizontal line of symmetry. Fold the paper in half and draw 1/2 of the E.",
                      "N has no line of symmetry. Its two halves never match, so N cannot be cut out by drawing half or "
                      "a quarter of it.",
                      "X has a vertical and a horizontal line. Fold the paper into one-fourth and draw 1/4 of the X.",
                      "T has a vertical line. Fold the paper in half and draw 1/2 of the T.",
                      "K has a horizontal line. Fold the paper in half and draw 1/2 of the K.",
                      "V has a vertical line. Fold the paper in half and draw 1/2 of the V.",
                      "O has a vertical and a horizontal line. Fold the paper into one-fourth and draw 1/4 of the O.",
                      "Check: E, X, T, K, V and O have a line of symmetry, and N has none."],
                     "E, X, T, K, V and O can be cut out: 1/2 for E, T, K and V, and 1/4 for X and O. N cannot be cut "
                     "out this way.",
                     kind="prompt",
                     q_figure="The letters E, N, X, T, K, V and O in one row, each in a different colour, with no lines "
                              "drawn on them.",
                     s_figure="The same seven letters with a dashed line of symmetry drawn on each letter that has "
                              "one: a horizontal line on E and K, a vertical line on T and V, both lines on X and O, "
                              "and no line on N."),
                 FIO("open.lines", "Alphabet Cutout: lines of symmetry in the letters",
                     "Look at the letters E, N, X, T, K, V and O. (a) Which of the letters have a horizontal line of "
                     "symmetry? ___ (b) Which of the letters have a vertical line of symmetry? ___ (c) Which letters "
                     "have both vertical and horizontal lines of symmetry? ___",
                     ["(a): a horizontal line goes across. Fold each letter along a horizontal line: the top half and "
                      "the bottom half match for E, X, K and O.",
                      "(b): a vertical line goes up and down. Fold each letter along a vertical line: the left half "
                      "and the right half match for X, T, V and O.",
                      "(c): the letters in both lists have both lines: X and O.",
                      "Check: N is in neither list, because N has no line of symmetry."],
                     "(a): E, X, K, O; (b): X, T, V, O; (c): X, O",
                     kind="prompt",
                     q_figure="The letters E, N, X, T, K, V and O in one row, each in a different colour, with no lines "
                              "drawn on them.",
                     s_figure="The same seven letters with the horizontal lines of symmetry drawn on E, X, K and O and "
                              "the vertical lines drawn on X, T, V and O, and no line on N."),
                 FIO("open.diya", "Let Us Do (cutouts): diya and boat",
                     "Use lines of symmetry to make paper cutouts of diya, boat, and other designs. Look along the "
                     "border of the page to find the pictures.",
                     ["Look along the border of the page. The diya and the boat are there, with other pictures such as "
                      "the heart, the butterfly and the leaf.",
                      "The diya has a vertical line of symmetry, down the middle of the flame and the bowl.",
                      "Fold a paper in half. Draw half of the diya along the fold, cut along the outline and open the "
                      "paper: the full diya appears.",
                      "The boat also has a vertical line of symmetry, down the middle of the sail and the hull. Fold, "
                      "draw half of the boat along the fold, cut and open.",
                      "Any border picture with a line of symmetry can be cut out in the same way.",
                      "Sample answer: your cutouts may be of other pictures. Your answer may differ."],
                     "Sample answer: fold a paper in half, draw half of the diya or the boat along the fold, cut and "
                     "open it. Your answer may differ.",
                     kind="exercise",
                     q_figure="A diya and a paper boat side by side, each drawn as in the border of the page, with no "
                              "lines drawn on them.",
                     s_figure="The diya and the boat, each with a dashed vertical line of symmetry down the middle.")],
          misconceptions=["M_ANY_LINE", "M_ONE_LINE"])],
    key_terms=["fold", "line of symmetry", "cutout", "letter"]))

# ============================== T2 Turns and the Windmill Firki ============================================
TOPICS.append(TOPIC(
    "T2", "M2", "Turns and the Windmill Firki", ["Let Us Make a Windmill Firki", "Turning letters"], "Understand",
    "Students describe quarter, half, three-quarter and full turns, and decide whether a shape such as the firki or a "
    "letter has rotational symmetry by checking if it looks the same after a turn.",
    "A full turn is four quarter turns. A shape has rotational symmetry if it looks the same after a 1/4, 1/2 or 3/4 turn. "
    "A dot on the shape keeps track of how far it has turned. Every shape looks the same after a full turn, so only the "
    "smaller turns count.",
    [A("T2.C1", "Quarter, Half and Three-Quarter Turns", "Understand",
       "Students describe a 1/4 turn, a 1/2 turn, a 3/4 turn and a full turn, and say where a dot on a turning shape "
       "lands after each turn.",
       textbook=["Lali makes firkis for her friends. Follow the steps given below to make your own firki. 1. Take a "
                 "square paper. 2. Fold the paper in half diagonally to make two triangles. 3. Open and fold it the "
                 "other way to make two more triangles. 4. Open it again. You will see an 'X' shape on the paper. 5. Use "
                 "scissors to cut along the four lines of the 'X'. Stop cutting about halfway to the centre. 6. Take "
                 "one corner of each triangle and fold it gently towards the centre of the paper. Do not press it "
                 "flat. 7. Fold every other corner towards the centre. 8. Push a pin through the folded corners and "
                 "the centre of the paper. 9. Push the pin through a stick or straw.",
                 "Make sure the pin is not too tight. Check if your windmill spins when the wind is blowing."],
       teach=["Predict first: a windmill firki has a dot on one blade. You turn the firki a quarter of the way round. "
              "Where does the dot go?",
              "A full turn takes the dot all the way round, back to the place it started from.",
              "A 1/4 turn is a quarter of the way round. A 1/2 turn is half of the way round, so the dot is on the "
              "opposite side. A 3/4 turn is three quarters of the way round.",
              "Four quarter turns make a full turn, and two quarter turns make a 1/2 turn.",
              "Always turn the shape the same way, for example to the right, and use the dot to see how far it has "
              "turned.",
              "Rule: a 1/4 turn, a 1/2 turn and a 3/4 turn are all smaller than a full turn, and the dot tells you "
              "how far the shape has turned."],
       examples=[WE("A paper pinwheel has 4 blades and a dot on the top blade. Turn it to the right, the same way each "
                    "time. Where is the dot after a 1/4 turn, a 1/2 turn and a 3/4 turn?",
                    ["A full turn is 4 quarter turns, so each quarter turn moves the dot on by one blade.",
                     "After a 1/4 turn the dot moves from the top blade to the right blade.",
                     "After a second quarter turn the dot is on the bottom blade. Two quarter turns make a 1/2 turn, "
                     "because 1/4 + 1/4 = 1/2.",
                     "After a third quarter turn the dot is on the left blade. Three quarter turns make a 3/4 turn.",
                     "After the fourth quarter turn the dot is back on the top blade, where it started: a full turn.",
                     "Check: 1/4 turn, right blade; 1/2 turn, bottom blade; 3/4 turn, left blade; full turn, top "
                     "blade."],
                    "After a 1/4 turn the dot is on the right blade, after a 1/2 turn on the bottom blade, and after a "
                    "3/4 turn on the left blade")],
       ncert=["firki.steps", "firki.tips"], key_terms=["turn", "quarter turn", "half turn", "full turn", "dot"],
       misconceptions=["M_DOT_MOVES"], minutes=5),
     A("T2.C2", "Rotational Symmetry: Looks the Same After a Turn", "Understand",
       "Students turn a shape by 1/4, 1/2 and 3/4 and decide whether it has rotational symmetry by checking if it looks "
       "the same after a turn.",
       textbook=["Observe the letters below. Do they look the same when turned? Dots have been marked on the letters to "
                 "keep track of the orientation of letters. You may also cut out the letters and fix the centre point "
                 "of the letter by a nail or use a tracing paper to check if the letter looks the same when turned.",
                 "The letter H has rotational symmetry, as it looks the same when rotated by half a turn. A firki has "
                 "rotational symmetry, as it looks the same when rotated by 1/4, 1/2, and 3/4 turn."],
       teach=["Predict first: turn the letter H by a half turn. Does it look the same as before?",
              "Yes. After a 1/2 turn the H looks the same. A shape that looks the same after a turn smaller than a "
              "full turn has rotational symmetry.",
              "Every shape looks the same after a full turn, so a full turn does not count.",
              "The firki looks the same after a 1/4, a 1/2 and a 3/4 turn, so it has rotational symmetry. The letter H "
              "lies on its side after a 1/4 turn, so it looks the same after a 1/2 turn only.",
              "To check, put a dot on the shape, turn it a 1/4, a 1/2 and a 3/4 turn, and each time ask: does it look "
              "the same? You can cut out the shape and fix its centre with a nail, or use tracing paper.",
              "Rule: a shape has rotational symmetry if it looks the same after at least one of the turns 1/4, 1/2 "
              "or 3/4."],
       examples=[WE("Does the letter Z have rotational symmetry? Does the letter T? Turn each one by 1/4, 1/2 and 3/4.",
                    ["Z: put a dot on the top left of the Z.",
                     "After a 1/4 turn the Z lies on its side and looks like an N, so it does not look the same.",
                     "After a 1/2 turn the Z is upside down and looks the same, with the dot now at the bottom right.",
                     "After a 3/4 turn the Z lies on its other side and looks like an N again, so it does not look "
                     "the same.",
                     "The Z looks the same after a 1/2 turn, so it has rotational symmetry, at 1/2 turn.",
                     "T: after a 1/4 turn the T lies on its side. After a 1/2 turn it is upside down, with the bar at "
                     "the bottom. After a 3/4 turn it lies on its other side. None of these looks like the T, so the T "
                     "has no rotational symmetry.",
                     "Check: every shape looks the same after a full turn, so the full turn does not count."],
                    "The Z has rotational symmetry, at 1/2 turn. The T has no rotational symmetry")],
       ncert=["rot.method", "rot.box"],
       key_terms=["rotational symmetry", "turn", "looks the same", "full turn"],
       misconceptions=["M_FULL_TURN", "M_DOT_MOVES"], minutes=6),
     DOER("T2.C3", "Practice: Turn and Check", "turn_and_check", "Apply",
          "Students say whether the firki and the letters H, I, X and Y look the same after 1/4, 1/2, 3/4 and a full "
          "turn, and name the turn of their rotational symmetry.",
          ["Turn the shape by 1/4, 1/2 and 3/4 and check it against its starting position.",
           "The dot only keeps track of the turn. Look at the shape, not at the dot.",
           "A full turn always looks the same, so only the smaller turns decide."],
          items=[FIO("firki.same", "Let Us Make a Windmill Firki: does it look the same",
                     "Observe the dot in the firki. Does the firki look the same after 1/4, 1/2, 3/4, and a full turn? "
                     "___",
                     ["The firki has 4 equal blades. The dot only keeps track of the turn.",
                      "After a 1/4 turn each blade has moved to the place of the next blade, so the firki looks the "
                      "same.",
                      "After a 1/2 turn and after a 3/4 turn it looks the same in the same way.",
                      "After a full turn the dot is back where it started and the firki looks the same.",
                      "So the firki looks the same after a 1/4 turn, a 1/2 turn, a 3/4 turn and a full turn. The dot "
                      "moves, but the firki looks the same."],
                     "Yes, it looks the same after 1/4, 1/2, 3/4 and a full turn. The dot moves, but the firki looks "
                     "the same.",
                     kind="prompt",
                     q_figure="Five pictures of a windmill firki with four blades and a green dot on one blade, in a "
                              "row: the initial position, then the firki after a 1/4 turn, a 1/2 turn, a 3/4 turn and a "
                              "full turn, each with its caption.",
                     s_figure="The same five pictures with a tick mark under each picture after the initial one."),
                 FIO("rot.H", "Example 1: the letter H turned",
                     "Observe the letter H. Dots have been marked on it to keep track of its orientation. Does the H "
                     "look the same after a 1/4 turn, a 1/2 turn, a 3/4 turn and a full turn? Does it have rotational "
                     "symmetry? Yes/No.",
                     ["After a 1/4 turn the H lies on its side. It does not look the same.",
                      "After a 1/2 turn it is upside down and it looks the same. The dots have moved to the bottom.",
                      "After a 3/4 turn it lies on its other side. It does not look the same.",
                      "After a full turn it is back where it started and looks the same.",
                      "The H looks the same after a 1/2 turn, which is smaller than a full turn, so it has rotational "
                      "symmetry."],
                     "Yes, at 1/2 turn",
                     kind="example",
                     q_figure="The letter H in purple with a red dot at its centre and a small white dot at the top of "
                              "each of its two sides, in its starting position.",
                     s_figure="Five pictures of the H in a row: the start, the H lying on its side after a 1/4 turn "
                              "with the dashed outline of the start, the H after a 1/2 turn looking the same, the H on "
                              "its other side after a 3/4 turn, and the H after a full turn."),
                 FIO("rot.IXY", "Turning Letters: letters I, X and Y",
                     "Observe the letters. Dots have been marked on the letters to keep track of the orientation of "
                     "letters. You may also cut out the letters and fix the centre point of the letter by a nail or use "
                     "a tracing paper to check if the letter looks the same when turned. Fill the table for three "
                     "letters: (a) the letter I, (b) the letter X, (c) the letter Y. For each letter: does it look the "
                     "same after a 1/4 turn, a 1/2 turn, a 3/4 turn and a full turn? Does it have rotational symmetry "
                     "(Yes/No)?",
                     ["(a): the I is a straight bar. After a 1/4 turn it lies flat, so it does not look the same. "
                      "After a 1/2 turn it looks the same. After a 3/4 turn it lies flat again. After a full turn it "
                      "looks the same. Rotational symmetry: yes, at 1/2 turn.",
                      "(b): the X looks the same after a 1/4 turn, after a 1/2 turn, after a 3/4 turn and after a full "
                      "turn. Rotational symmetry: yes, at 1/4 turn.",
                      "(c): the Y lies on its side after a 1/4 turn, is upside down after a 1/2 turn and lies on its "
                      "other side after a 3/4 turn. None of these looks the same, only the full turn does. Rotational "
                      "symmetry: no.",
                      "Check: only a turn smaller than a full turn counts, so the Y has no rotational symmetry."],
                     "(a): Yes, at 1/2 turn; (b): Yes, at 1/4 turn; (c): No",
                     kind="prompt",
                     q_figure="Three rows of a table, one for each letter: a green bar I, a blue X and a tan Y, each "
                              "with a red dot at its centre (for the Y, at the bottom of its stem), and empty boxes for "
                              "the 1/4 turn, 1/2 turn, 3/4 turn, full turn and rotational symmetry.",
                     s_figure="The same three rows with each letter drawn after each turn and the last box filled: Yes, "
                              "at 1/2 turn for I; Yes, at 1/4 turn for X; No for Y.")],
          misconceptions=["M_DOT_MOVES", "M_FULL_TURN"])],
    key_terms=["turn", "rotational symmetry", "firki"]))

# ============================== T3 Reflection, Rotation or Both ============================================
TOPICS.append(TOPIC(
    "T3", "M2", "Reflection, Rotation or Both", ["Let Us Do (digits)"], "Analyze",
    "Students use a fold test and a turn test to decide whether a letter, digit or number has reflection symmetry only, "
    "rotational symmetry only, both or neither.",
    "Reflection symmetry and rotational symmetry are two different tests. Fold the shape along a line, then turn it a "
    "1/4, 1/2 or 3/4 turn. A shape can pass one test, both tests or neither.",
    [A("T3.C1", "Reflection Only, Turn Only or Both", "Analyze",
       "Students use a fold test and a turn test to decide whether a letter or sign has reflection symmetry only, "
       "rotational symmetry only, both or neither.",
       teach=["Predict first: the letter M has a vertical line of symmetry. Does it also look the same after a half "
              "turn?",
              "A shape can have reflection symmetry, rotational symmetry, both, or neither. They are two different "
              "tests.",
              "Test 1, reflection: fold the shape along a vertical or a horizontal line. Do the halves match?",
              "Test 2, rotation: turn the shape a 1/4, a 1/2 and a 3/4 turn. Does it look the same after any of them?",
              "M passes Test 1, because it has a vertical line. It does not pass Test 2, because after a 1/2 turn it "
              "looks like a W. So M has reflection symmetry only.",
              "H passes both tests, so H has both symmetries.",
              "Rule: run both tests every time. A line of symmetry does not tell you about turns, and a turn does not "
              "tell you about lines."],
       examples=[WE("Sort the letter M, the letter S and the plus sign into: reflection symmetry only, rotational "
                    "symmetry only, both symmetries, or neither.",
                    ["M, Test 1: it has a vertical line of symmetry. Test 2: after a 1/2 turn it looks like a W, so it "
                     "does not look the same. M has reflection symmetry only.",
                     "S, Test 1: fold it along a vertical line or a horizontal line and the halves do not match, so "
                     "there is no line of symmetry. Test 2: after a 1/2 turn the S looks the same. S has rotational "
                     "symmetry only.",
                     "The plus sign, Test 1: it has a vertical line and a horizontal line. Test 2: it looks the same "
                     "after a 1/4 turn. It has both symmetries.",
                     "Check: each of the three signs went to a different group."],
                    "M: reflection symmetry only. S: rotational symmetry only. The plus sign: both")],
       key_terms=["reflection symmetry", "rotational symmetry", "fold test", "turn test", "both"],
       misconceptions=["M_BOTH_ALWAYS", "M_FLIP_IS_TURN"], minutes=6),
     DOER("T3.C2", "Practice: Symmetry Sorter", "symmetry_sorter", "Analyze",
          "Students find the digits and numbers with reflection symmetry, rotational symmetry or both, and give examples "
          "of 2-, 3- and 4-digit numbers of each kind.",
          ["Run the fold test and the turn test on every digit.",
           "6 and 9 turn into each other, so neither looks the same after a half turn by itself.",
           "A number is tested as a whole: fold the whole number, and turn the whole number."],
          items=[FIO("dig.sym", "Let Us Do (digits): symmetry in the digits",
                     "Find symmetry in the digits 1, 2, 3, 4, 5, 6, 7, 8, 9, 0. (a) Which digits have reflection "
                     "symmetry? ___ (b) Which digits have rotational symmetry? ___ (c) Which digits have both "
                     "rotational and reflection symmetries? ___",
                     ["The digit 1 is drawn as a plain bar, so test the digits as they are drawn in your maths book.",
                      "Reflection: fold each digit along a vertical or a horizontal line. 0, 1 and 8 match on both "
                      "lines, and 3 matches on a horizontal line. 2, 4, 5, 6, 7 and 9 match on no line.",
                      "Rotation: turn each digit a 1/2 turn. 0, 1 and 8 look the same. A 1/2 turn turns 6 into 9 and 9 "
                      "into 6, so 6 and 9 do not look the same by themselves. 2, 3, 4, 5 and 7 do not look the same.",
                      "Both: the digits in both lists are 0, 1 and 8.",
                      "Check: 3 is in the first list only, and 6 and 9 are in neither list."],
                     "(a): 0, 1, 3, 8; (b): 0, 1, 8; (c): 0, 1, 8",
                     kind="exercise",
                     q_figure="The ten digits 1, 2, 3, 4, 5, 6, 7, 8, 9 and 0 in a row, each in a different colour, with "
                              "the digit 1 drawn as a plain straight bar.",
                     s_figure="The same ten digits with a green tick under 0, 1, 3 and 8 for reflection symmetry and a "
                              "blue star under 0, 1 and 8 for rotational symmetry."),
                 FIO("dig.nums", "Let Us Do (digits): the numbers 11 and 1001",
                     "Now, let us look at the following numbers: 11 and 1001. Do these have rotational symmetry, "
                     "reflection symmetry or both symmetries?",
                     ["The digit 1 is drawn as a plain bar. Test each number with a fold line and with a 1/2 turn.",
                      "11: fold along the vertical line between the two bars and the halves match. Turn it a 1/2 turn: "
                      "the two bars swap places and the number looks the same.",
                      "1001: fold along the vertical line between the two zeros and the halves match. Turn it a 1/2 turn: "
                      "the first 1 lands at the end, the last 1 lands at the start, and each 0 still looks like a 0, "
                      "so the number looks the same.",
                      "So 11 and 1001 both have reflection symmetry and rotational symmetry."],
                     "Both numbers have both symmetries, rotational and reflection",
                     kind="exercise",
                     q_figure="The two numbers 11 and 1001 side by side, with each digit 1 drawn as a plain straight "
                              "bar.",
                     s_figure="The same two numbers, each with a dashed vertical line down the middle and a curved arrow "
                              "for a 1/2 turn."),
                 FIO("dig.examples", "Let Us Do (digits): examples of 2-digit, 3-digit and 4-digit numbers",
                     "Give examples of 2-digit, 3-digit and 4-digit numbers which have rotational symmetry, reflection "
                     "symmetry, or both.",
                     ["Use the digits you found: 0, 1 and 8 have both symmetries, 3 has a horizontal line only, and 6 "
                      "and 9 turn into each other after a 1/2 turn.",
                      "Rotational symmetry only: 69, 619 and 6969. A 1/2 turn turns 6 into 9 and 9 into 6 and swaps "
                      "their places, so each number looks the same. None of them has a line of symmetry.",
                      "Reflection symmetry only: 38, 383 and 3883. Every digit has a horizontal line of symmetry, so "
                      "each number has a horizontal line. A 1/2 turn does not keep a 3, so none of them has rotational "
                      "symmetry.",
                      "Both: 88, 808 and 8118. 0, 1 and 8 have a vertical line, and each number reads the same from "
                      "both ends, so each has a vertical line, and a 1/2 turn keeps each number.",
                      "Sample answer: many other numbers work. Your answer may differ."],
                     "Sample answer. Rotation only: 69, 619, 6969. Reflection only: 38, 383, 3883. Both: 88, 808, 8118. "
                     "Your answer may differ.",
                     kind="exercise",
                     s_figure="The numbers 69, 38 and 88 each drawn large, with a curved arrow for a 1/2 turn on 69 and "
                              "88 and a dashed horizontal line on 38 and 88.")],
          misconceptions=["M_SIX_NINE", "M_BOTH_ALWAYS"])],
    key_terms=["reflection symmetry", "rotational symmetry", "digits"]))
