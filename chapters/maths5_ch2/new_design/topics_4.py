# -*- coding: utf-8 -*-
"""Topics T9 and T10 (module M3): Fun with Relations (the chapter's closing puzzle, a puzzle video plus the book's own
puzzle) and the Chapter Revision summary. Every teaching concept has one worked example with the plan's own words;
the book's puzzle is an FIO item of the DOER."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []

# ============================== T9 Fun with Relations ======================================================
TOPICS.append(TOPIC(
    "T9", "M3", "Fun with Relations", ["Fun with Relations"], "Apply",
    "Students follow a family relation one link at a time and name the relation in the book's puzzle.",
    "A relation puzzle is a chain. Start with yourself, take one link, name the person you reach, then take the next "
    "link from that person. When the puzzle says the only brother, ask whether that person is already in the chain.",
    [A("T9.C1", "Fun with Relations: One Link at a Time", "Apply",
       "Students follow a family relation one link at a time and name the person at the end of the chain.",
       teach=["Predict first: who is your father's father's wife to you? Say it slowly, one link at a time.",
              "A relation puzzle is a chain. Start with yourself, take one link, name the person you reach, then take "
              "the next link from that person.",
              "Link 1: your father's father is your grandfather. Link 2: his wife is your grandmother. So your "
              "father's father's wife is your grandmother.",
              "Draw each person you find and stop at each name before you take the next link.",
              "When a puzzle says the only brother or the only sister, ask: is this person already in the chain? That "
              "is often the clue."],
       examples=[WE("Who is your mother's only sister's daughter to you?",
                    ["Start with your mother and take the link to her only sister: she is your aunt, your mother's "
                     "sister.",
                     "Take the next link: the daughter of your aunt.",
                     "The daughter of your mother's sister is your cousin sister.",
                     "Check each link again: mother, her sister, her sister's daughter. No link was skipped."],
                    "She is your cousin sister.")],
       key_terms=["relation", "link", "only brother"], misconceptions=["M_NEW_PERSON"], minutes=5),
     DOER("T9.C2", "Pull it together and do it: Fun with Relations", None, "Apply",
          "Students name the child's relation to themselves in the book's puzzle and give each link of the chain.",
          ["Follow the chain one link at a time and name every person you reach.",
           "Ask whether a person in the puzzle is already in the chain.",
           "Say the last relation in a short phrase."],
          items=[FIO("rel.puzzle", "Fun with Relations: the only brother",
                     "If the only brother of your father's sister had a child, what would be the child's "
                     "relationship with you?",
                     ["Start with your father and take the link to his sister: she is your aunt, your father's sister.",
                      "Take the next link: the brother of your father's sister. Your father is her brother.",
                      "She has only one brother, so the only brother of your father's sister is your father himself.",
                      "Take the last link: a child of your father is your brother or your sister.",
                      "Check: father, his sister, her only brother (your father), his child. The chain ends at a "
                      "brother or a sister of yours."],
                     "The child is your brother or sister.",
                     kind="prompt",
                     s_figure="A small family tree: your father and his sister side by side, your father's child "
                              "below him, with a thin line showing that the only brother of the sister is the "
                              "father.")],
          misconceptions=["M_NEW_PERSON"])],
    key_terms=["relation", "link"]))

# ============================== T10 Chapter Revision (summary) =============================================
TOPICS.append(TOPIC(
    "T10", "M3", "Chapter Revision: Fractions", ["Chapter summary"], "Understand",
    "",
    "The chapter's ideas in one walk through the kitchen: the same whole, fractions of a grid, making a whole from "
    "pieces, equivalent fractions, comparing with the same denominator, the same numerator, with 1 and with 1/2, "
    "fractions greater than 1, and the relations puzzle.",
    [A("T10.C1", "Chapter Revision: Fractions", "Understand",
       "",
       teach=["Predict first: you have walked through the whole kitchen of fractions. Can you say one idea from each "
              "stop, from the two chocolates to the puzzle? Read the lines below and tick each idea you remembered.",
              "Same whole: two fractions can be compared only when they are parts of the same whole. 1/3 of a big "
              "chocolate can be more than 1/2 of a small one.",
              "Check: the small chocolate has 4 blocks and the big one has 9 blocks, all blocks the same size. 1/2 of "
              "the small one is 4 ÷ 2 = 2 blocks and 1/3 of the big one is 9 ÷ 3 = 3 blocks. The third of the big "
              "chocolate is more.",
              "Fraction of a grid: split the squares into equal groups, and one group is the fraction. A grid of 48 "
              "squares has 48 ÷ 8 = 6 squares in 1/8 and 48 ÷ 6 = 8 squares in 1/6.",
              "Making a whole: 5 pieces of 1/5 make 5/5 = 1. Pieces of different sizes make a whole too, such as "
              "1/2 + 1/4 + 1/4 = 1.",
              "Equivalent fractions name the same part of a whole with different names: 1/3 = 2/6 = 3/9 = 4/12. Cut "
              "every part into more equal parts and the top and bottom numbers grow by the same number of times.",
              "Check: 2/5 = 6/15. Top and bottom both grew 3 times, because 2 × 3 = 6 and 5 × 3 = 15.",
              "Same denominator: count the pieces. 2/3 is more than 1/3 because 2 pieces of 1/3 are more than 1 "
              "piece of 1/3.",
              "Same numerator: look at the size of one piece. 4/5 is more than 4/6 because a 1/5 piece is bigger "
              "than a 1/6 piece.",
              "Check: which is more, 3/8 or 3/7? 3/7, because a 1/7 piece is bigger than a 1/8 piece.",
              "Fractions greater than 1: 5 pieces of 1/2 make 5/2 = 2 1/2 and 9 pieces of 1/4 make 9/4 = 2 1/4. A "
              "fraction is greater than 1 when its top number is more than its bottom number.",
              "Check: how many parathas are 8 pieces of 1/4? 8/4 = 2 parathas, because 8 ÷ 4 = 2.",
              "Compare with 1: a fraction below 1 is less than a fraction above 1. 7/8 is less than 1 and 8/6 is "
              "more than 1, so 7/8 < 8/6.",
              "Compare with 1/2: a fraction is equal to 1/2 when its top is half of its bottom, like 4/8 and 3/6. "
              "5/8 is more than 1/2 and 3/6 is half, so 5/8 > 3/6.",
              "Check: is 3/15 more or less than 1/2? Less, because half of 15 is more than 3.",
              "Ants: 16 ants, each 1/4 cm long, make 16 × 1/4 = 16/4 = 4 cm.",
              "Puzzle: follow a relation one link at a time. The only brother of your father's sister is your "
              "father, so his child is your brother or sister."],
       ncert=["summary"], key_terms=["equivalent fractions", "same whole", "reference"], minutes=6,
       enrichment=True)],
    topic_type="summary"))
