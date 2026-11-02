# -*- coding: utf-8 -*-
"""Chapter-level content for Class 6 Chapter 10, The Other Side of Zero (Ganita Prakash Grade 6, Chapter 10).
Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212."""
from __future__ import annotations

import io as _io
import json as _json
import os as _os

CHAPTER = {
    "grade": 6,
    "label": "Class 6",
    "chapter_no": 10,
    "name": "The Other Side of Zero",
    "book_part": "Ganita Prakash Grade 6, Chapter 10",
    "source_pdf": "textbooks/class6/fegp110.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Floors Below the Ground",
     "Bela's Building of Fun has floors above and below the ground. Floor numbers, lift button presses, inverses "
     "and comparing floors give the first meaning of positive and negative numbers and of adding them."),
    ("M2", "Subtracting, Big Numbers and the Number Line",
     "Subtraction finds the button to press, mines and endless lifts carry the idea to big numbers, and the lift "
     "turns into the number line, the unmarked number line and the rule that subtracting a number is adding its "
     "inverse."),
    ("M3", "Tokens, Money, Heights and Temperatures",
     "Green and red tokens do addition and subtraction with zero pairs, and credits and debits, heights above and "
     "below sea level and temperatures below zero show integers at work."),
    ("M4", "Explorations, History and a Game",
     "Border-sum grids, an amazing grid and integer puzzles are explored, Brahmagupta's rules gather everything "
     "into five rules for adding and five for subtracting, and a snakes and ladders game and the summary close "
     "the chapter."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's order. One building with floors above and below the ground gives "
             "meaning to negative numbers, then the same lift, the number line and tokens are used to add and "
             "subtract any integers.",
    "points": [
        {"title": "One lift, many ideas",
         "text": "Every new idea starts in Bela's lift or on a number line: a floor is a number, a button press is "
                 "a movement, and Starting Floor + Movement = Target Floor."},
        {"title": "Concept, then practice, topic by topic",
         "text": "Each idea gets its own topic: worked videos for the book's questions, a tool only where "
                 "handling the lift, the line or the tokens is the idea, then the book's Figure it Out questions in "
                 "a practice topic, each with its own video."},
        {"title": "Why, not a trick",
         "text": "Signs are never handled by a memorised rule. A result such as 2 minus a negative is read off the "
                 "lift, the number line or the tokens first, and the rule is named afterwards."},
        {"title": "Keeko's doubts",
         "text": "The common wrong ideas, such as 'minus 4 is bigger than minus 3 because 4 is bigger than 3', are "
                 "raised by Keeko and fixed with a floor, a line or a token, never just a rule."},
    ],
}

# Every book item. Ids come from the page-image inventory (book_items.json); "summary" is the chapter summary.
with _io.open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "book_items.json"),
              encoding="utf-8") as _f:
    NCERT_ITEMS = [_i["id"] for _i in _json.load(_f)] + ["summary"]

MISCONCEPTIONS = [
    ("M_NEG_NOTHING", "Nothing can be less than 0, because 0 means nothing is there."),
    ("M_BELOW_POSITIVE", "Floors below the ground are numbered 1, 2, 3 like the floors above, with no sign to "
                         "tell them apart."),
    ("M_ZERO_SIGNED", "Zero is a positive number, so the ground floor should be Floor +1 or carry a sign."),
    ("M_BUTTON_ADD_ONLY", "A button press is only a count of presses, so pressing '−' three times is the number 3."),
    ("M_ADD_BIGGER", "Adding always makes a number bigger, so a total can never be lower than its start."),
    ("M_IGNORE_SIGN", "To add a positive and a negative number, subtract and keep the sign of the first number "
                      "written."),
    ("M_INVERSE_RECIP", "The inverse of a number is 1 divided by it, and 0 has no inverse."),
    ("M_BIGGER_DIGIT", "−4 is greater than −3, because 4 is greater than 3."),
    ("M_SUB_SMALLER", "Subtracting always makes a number smaller."),
    ("M_START_MINUS_TARGET", "The movement needed is Starting Floor − Target Floor."),
    ("M_DISTANCE_ONLY", "The movement from one place to another is just the distance between them, whatever the "
                        "direction."),
    ("M_SUB_NEG_SMALLER", "Subtracting a negative number takes you lower, because there is a minus sign."),
    ("M_ZERO_PAIR_CHANGES", "A zero pair changes the value of a set of tokens, so adding one is not allowed."),
    ("M_TOKEN_COUNT", "The value of a set of tokens is the number of tokens, and the colour does not matter."),
    ("M_NO_NEG_BALANCE", "A bank balance can never be negative, so a purchase above the balance is impossible."),
    ("M_DEEPER_HIGHER", "−1200 m is higher than −200 m, because 1200 is bigger than 200."),
    ("M_GRID_CHOICE", "The sum in the amazing grid depends on which numbers are circled, so different choices give "
                      "different sums."),
    ("M_BETWEEN_ENDS", "The integers between two numbers include the two numbers themselves."),
    ("M_YEAR_ZERO", "There is a year 0 between 1 BCE and 1 CE, so counting back across it needs no extra step."),
    ("M_SIGN_RULE_ALWAYS", "A sum of two integers with different signs always takes the sign of the first number "
                           "written."),
    ("M_DIE_CHOICE", "In the dice game the only allowed move is to add the two numbers rolled."),
]

SOLUTION_NOTES = [
    "10.0.q1, 10.1.q1, 10.1.q2, 10.1.q4, 10.1.q5, 10.1.q6, 10.1.q7, 10.1.q8, 10.1.q14, 10.1.q22, 10.2.q2, 10.3.q5, "
    "10.3.q6, 10.3.FiO3.Q1, 10.4.FiO1.Q4, 10.4.FiO1.Q5, 10.4.FiO2.Q3, 10.5.FiO.Q1, 10.5.FiO.Q2, 10.G.ac1: the book "
    "gives no printed answer (open ended, read off a picture or stated in the text); the answers worked here "
    "follow the expected observation.",
    "10.1.q5: the solution page lists only floors +3 to −2. Floors +6, +5, +4 and −3, −4, −5 are counted from the "
    "picture: Space +6, Sports +5, Ice Cream +4, Book Store +3, Art Centre +2, Food Court +1, Welcome Hall 0, Toys "
    "−1, Video Games −2, Cinema −3, Ghost House −4, Dinosaur −5.",
    "10.1.q15: the solution page gives only parts a, b, d and f. Parts c, e, g and h are computed here: 160, 230, "
    "101 and 3000.",
    "10.1.FiO3.Q3: the picture is a vertical line with unmarked ticks, so the book answer (B = −9, C = −6, F = +2, "
    "G = +6, H = +11) is kept as printed and should be checked against the printed figure.",
    "10.1.ex9: the book prints only the rewritten forms; the values +2, −11, +10 and +15 are computed.",
    "10.4.FiO3.Q5: the book answer for parts a and b depends on the present year. It is worked here with the "
    "present year as 2026 (a: 1876, b: 175 BCE, since there is no year 0). Part c, 360 BCE, is the printed answer "
    "and is checked: 680 minus 320 is 360.",
    "10.4.FiO3.Q3: checked by listing all 36 pair sums. The sums that cannot be made from −10 to 12 are exactly "
    "−9, −7, −5, 0, 2, 7, 9, 11, as the book says.",
    "10.4.FiO3.Q6c, 10.4.FiO3.Q9: checked by differences (Q6c) and by blocks of 5 tokens (Q9); Q9 depends on the "
    "printed picture of 3 green then 2 red tokens, which should be checked against the figure.",
    "10.4.FiO1.Q2 and 10.4.FiO1.Q3: many fillings work; the book shows one for each, and one is shown here.",
    "10.G.ac1: board numbers are partly hidden by snakes and ladders in the scan; the game is taught from its "
    "rules, not from the board positions.",
]
ERRATA = [
    "10.4.FiO3.Q5: the book gives no answer for a and b because they depend on the present year; here "
    "2026 is used.",
]

DESIGN_REFERENCES = [
    {"text": "maths6_ch9 new_design plan: framing intro with one hook, idea topics ending in one doer, optional "
             "tool where the manipulation is the idea, a practice topic after each idea topic with one video per "
             "book question, one summary topic.",
     "url": ""},
]
