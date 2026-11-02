# -*- coding: utf-8 -*-
"""Chapter-level content for Class 8 Chapter 12, Tales by Dots and Lines (Ganita Prakash Grade 8 Part II, Chapter 5).
Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is U+2212.
Values read off the book's graphs are approximate and are always worded that way."""
from __future__ import annotations

CHAPTER = {
    "grade": 8,
    "label": "Class 8",
    "chapter_no": 12,
    "name": "Tales by Dots and Lines",
    "book_part": "Ganita Prakash Grade 8 Part II, Chapter 5",
    "source_pdf": "textbooks/class8/hegp205.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "The Balancing Act: Mean and Median",
     "The mean is the balance point of a dot plot. Adding, removing or changing values moves the mean and the "
     "median in predictable ways, unknown values are found from a known mean, frequency tables and spreadsheets "
     "do the heavy counting."),
    ("M2", "Visualising and Interpreting Data",
     "Line graphs show change over time. Students read and compare them in a two step way (what is given, then "
     "what it says), catch seasonal patterns in rain, read a map based infographic, and read a day as a colour strip."),
    ("M3", "Your Own Data Story",
     "An individual and a small group project turn the chapter's habits into an investigation of the student's "
     "own day, sleep and school timings, followed by a closing summary."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's own order. Dot plots turn the mean into a balance point, and every "
             "change to the data (a new value, a missing value, every value shifted or doubled) is predicted first "
             "and then checked. The second half moves from numbers to pictures: line graphs, an infographic and "
             "colour strips, each read with the same two questions, what is given and what does it say.",
    "points": [
        {"title": "Predict, then check",
         "text": "Each idea opens with a question the student answers before the video reveals it: will the mean go "
                 "up or down, which dot is missing, which season is wet. The tool then lets the student test the guess."},
        {"title": "One tool, one idea",
         "text": "Every topic has one tool, and no tool is used twice. A tool appears only where handling the "
                 "data is the concept itself."},
        {"title": "Read a graph in two steps",
         "text": "Step one: what is given (axes, scale, marks, who collected it and how). Step two: what can be "
                 "inferred, and what cannot. Graph values are read approximately and said so."},
        {"title": "Ask your own questions",
         "text": "The chapter closes on projects: strips of the student's own day, sleep logs and school timings, "
                 "because looking at data leads to new questions."},
    ],
}

NCERT_ITEMS = [
    "opening",
    # 5.1 The Balancing Act (pp 103 to 105)
    "5.1.pairs", "5.1.three_collections", "5.1.centre_explain", "5.1.mt_distances", "5.1.mt_one_centre",
    "5.1.new_value", "5.1.remove_value", "5.1.mt_fair_share",
    # Unchanging mean, relatively unchanged (pp 105 to 108)
    "5.1.unchanged2", "5.1.unchanged3", "5.1.try_two_greater",
    "5.1.add_k", "5.1.try_subtract", "5.1.try_fair_share_shift", "5.1.multiply_k",
    # Median, finding the unknown, frequencies, spreadsheets
    "5.1.median_tinker", "5.1.kushti", "5.1.coconut",
    "5.1.family_mean", "5.1.family_median",
    "5.1.sheet_intro", "5.1.sheet_cells", "5.1.sheet_formulae", "5.1.sheet_tasks", "5.1.sheet_note",
    # Figure it Out, section 5.1 (questions 1 to 11)
    "FiO1.q1", "FiO1.q2", "FiO1.q3", "FiO1.q4", "FiO1.q5", "FiO1.q6", "FiO1.q7", "FiO1.q8", "FiO1.q9",
    "FiO1.q10", "FiO1.q11",
    # 5.2 Visualising and Interpreting Data
    "5.2.intro", "5.2.temp_compare", "5.2.temp_step1", "5.2.temp_step2", "5.2.temp_questions",
    "5.2.space_method", "5.2.space_steps", "5.2.space_valid", "5.2.space_double", "5.2.space_why_line",
    "5.2.rain_method", "5.2.rain_map", "5.2.rain_peaks", "5.2.rain_monsoon",
    "FiO2.q1", "FiO2.q2", "FiO2.q3",
    "5.2.info_intro", "5.2.info_scale", "5.2.info_questions", "5.2.info_wonder",
    "5.2.strip_intro", "5.2.strip_questions", "5.2.strip_own", "5.2.strip_adult",
    "5.2.sleep_intro", "5.2.sleep_observe", "5.2.sleep_smooth", "5.2.sleep_why",
    # Figure it Out, section 5.2 (questions 1 to 15)
    "FiO3.q1", "FiO3.q2", "FiO3.q3", "FiO3.q4", "FiO3.q5", "FiO3.q6", "FiO3.q7", "FiO3.q8", "FiO3.q9",
    "FiO3.q10", "FiO3.q11", "FiO3.q12", "FiO3.q13", "FiO3.q14", "FiO3.q15",
    "summary", "hex",
]

MISCONCEPTIONS = [
    ("M_MID_ENDS", "The mean is the midpoint of the smallest and the largest value."),
    ("M_MEAN_DATA", "The mean has to be one of the values in the data."),
    ("M_ADD_NO_CHANGE", "Adding any new value leaves the mean where it was."),
    ("M_RAW_FREQ", "To average a frequency table, add the distinct values and divide by how many distinct values there are."),
    ("M_MEDIAN_MEAN", "The median moves by the same amount as the mean when a value is added."),
    ("M_SHIFT_MEDIAN_ONLY", "If every value goes up by 10 only the biggest value changes, so the mean stays put."),
    ("M_DOUBLE_ADD", "Doubling every value adds the same amount to the mean instead of doubling it."),
    ("M_LINE_CAUSE", "A steep line segment means the quantity is large, rather than that it is changing fast."),
    ("M_LINE_COUNTRIES", "The lines of the countries on a graph must add up to the world line."),
    ("M_AXIS", "A graph's vertical axis always starts at zero and every graph uses the same scale."),
    ("M_COAST", "All east coast cities get their rain in the same months as west coast cities."),
    ("M_INFOG_100", "A value of +100 on the rice and wheat map means the state eats no wheat at all."),
    ("M_STRIP_SAME", "Each colour on a strip is a fixed activity for every strip; the key can be ignored."),
    ("M_SMOOTH", "A smooth curve means the data was measured continuously, not at many close points."),
]

SOLUTION_NOTES = []
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics each ending in one tool, a "
             "question topic after each idea topic, and one summary topic.", "url": ""},
]

FIGURES = {}
