# -*- coding: utf-8 -*-
"""Topics T10 to T12 (module M3: both symmetries together, tiles and the game, summary). Sections 9.2 and 9.3."""
from topics_common import A, DOER, TOPIC, BOOK_TEXT, book, fio, we

TOPICS = []

# ============================== T10 Lines and turns together (9.2) ===========================================
TOPICS.append(TOPIC(
    "T10", "M3", "Lines and Turns Together", ["9.2", "9.3"], "Analyze",
    "Students decide for a figure whether it has lines of symmetry, angles of symmetry, both or neither, and "
    "count both for regular polygons.",
    "Lines and turns are separate: a figure can have lines only, turns only, both, or neither.",
    [A("T10.C1", "Lines but no turns, turns but no lines", "Analyze",
       "Students give an example of a figure with a line of symmetry but no rotational symmetry, and one with "
       "rotational symmetry but no line, and explain why one does not imply the other.",
       textbook=book("9.3", "Summary", start=5),
       teach=["Predict first: a kite has a line of symmetry. Does it also turn onto itself at 180°?",
              "No: a kite has one line and only the 360° turn. A twisted six-petal flower turns onto itself at 60° "
              "steps, but has no line.",
              "So a figure with a line need not have turns, and a figure with turns need not have a line."],
       key_terms=["reflection symmetry", "rotational symmetry"],
       misconceptions=["M_NO_LINE_NO_SYM", "M_ORDER_LINES"], minutes=8),
     A("T10.C2", "Figures with both kinds of symmetry", "Apply",
       "Students count the lines and the angles of symmetry of a square and an equilateral triangle, and see "
       "that a regular figure with n sides has n of each.",
       textbook=[],
       teach=["Predict first: an equilateral triangle. How many lines of symmetry, and how many angles of symmetry?",
              "3 lines, and the angles 120°, 240° and 360°, so 3 angles.",
              "A square has 4 lines and 4 angles. A regular figure with n equal sides has n lines and n angles of "
              "symmetry.",
              "The equal counts are special to regular shapes. A kite has 1 line and 1 angle, and the twisted "
              "flower has 0 lines and 6 angles."],
       key_terms=["regular polygon", "order"], misconceptions=["M_ORDER_LINES", "M_EVERY_LINE"], minutes=8),
     DOER("T10.C3", "Pull it together and do it: Lines and Turns Sorter", "symmetry_sorter", "Analyze",
          "Students sort figures on the tool by lines of symmetry and angles of symmetry, and sketch figures that "
          "have a stated mix of the two.",
          ["Test lines by folding and turns by rotating, as two separate tests.",
           "Regular polygons with n sides have n lines and n angles of symmetry.",
           "Some figures have lines but no turns, others turns but no lines, others both."],
          items=[fio("9.2.FiO2.Q2"), fio("9.2.FiO2.Q3"), fio("9.2.FiO2.Q7"), fio("9.2.FiO2.Q8"),
                 fio("9.2.FiO2.Q9"), fio("9.2.FiO2.Q10")],
          misconceptions=["M_NO_LINE_NO_SYM", "M_ORDER_LINES"])]))

# ============================== T11 Playing with tiles and a game (9.2, 9.3) =================================
TOPICS.append(TOPIC(
    "T11", "M3", "Playing with Tiles and a Symmetry Game", ["9.2", "9.3"], "Apply",
    "Students complete tile designs with a stated number of lines of symmetry and use a half turn to win a grid "
    "game.",
    "Tiles and a grid game use the same two moves: copy a part across a line, or copy it by a half turn.",
    [A("T11.C1", "Completing a tile design with two lines", "Apply",
       "Students complete a tile figure by reflecting the filled quarter so that it has exactly 2 lines of "
       "symmetry.",
       textbook=book("9.2", "Playing with Tiles", stop=1),
       teach=["Predict first: one quarter of a square grid is filled with colour tiles. How can the other three "
              "quarters give exactly 2 lines of symmetry?",
              "Copy the filled quarter as a mirror image across the vertical line, then copy the top half "
              "across the horizontal line.",
              "Check for extra lines: if the tiles in the quarter slant one way, the diagonals fail and there are "
              "exactly 2 lines."],
       examples=[we("9.2.q23")],
       key_terms=["tile", "line of symmetry"], misconceptions=["M_ONE_LINE"], minutes=8),
     A("T11.C2", "A game won by a half turn", "Analyze",
       "Students explain why the second player always wins the 6 by 6 line-placing game by answering each move with "
       "its 180° rotation about the centre of the grid.",
       textbook=book("9.3", "Game"),
       teach=["Predict first: two players cover two adjacent squares with a line in turn, and the player who "
              "cannot place a line loses. Who do you think wins?",
              "The centre of the 6 by 6 grid is a corner point where 4 squares meet, so no line covers it.",
              "After each move of the first player, the second player places a line on its 180° rotation about "
              "the centre. That place is free, so the second player always has a reply.",
              "The first player runs out of moves first, so the second player wins."],
       examples=[we("9.3.q1")],
       key_terms=["half turn", "strategy"], misconceptions=["M_NO_LINE_NO_SYM"], minutes=10),
     DOER("T11.C3", "Pull it together and do it: Tile Designer", "tile_designer", "Create",
          "Students lay colour tiles on a 4 by 4 grid on the tool, and make designs with exactly 1 line, exactly "
          "2 lines, or a turn of symmetry.",
          ["A line of symmetry needs each tile to match its mirror partner.",
           "Check for extra lines, diagonals included, before counting.",
           "A design can also be symmetric by a turn."],
          items=[fio("9.2.q24"), fio("9.2.q25")],
          misconceptions=["M_ONE_LINE", "M_BALANCED"])]))

# ============================== T12 Summary ==================================================================
TOPICS.append(TOPIC(
    "T12", "M3", "Summary: Symmetry", ["Summary"], "Remember",
    None,
    "Lines of symmetry and reflection, angles of symmetry and rotation, the circle, and how the two ideas relate.",
    [A("T12.C1", "What we found about symmetry", "Remember",
       "Students restate the meaning of a line of symmetry, an angle of symmetry and the centre of rotation, and "
       "say which figures have lines, turns, both or neither.",
       textbook=book("9.3", "Summary"),
       teach=["Our opening question is settled: a flower, a rangoli and a pinwheel repeat a part in a pattern, "
              "and the pattern is a line of symmetry, an angle of symmetry, or both.",
              "A line of symmetry is tested by a fold, an angle of symmetry by a turn about a fixed centre.",
              "Still open for you: how many lines and how many turns does a figure of your own design have?"],
       ncert=["summary"], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
