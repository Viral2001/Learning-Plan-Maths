# -*- coding: utf-8 -*-
"""Chapter-level content for Class 7 Chapter 3, A Peek Beyond the Point (Ganita Prakash Grade 7 Part I,
Chapter 3). Book lines elsewhere are verbatim except: the book's dashes become commas, colons or "to"; minus is
U+2212."""
from __future__ import annotations

CHAPTER = {
    "grade": 7,
    "label": "Class 7",
    "chapter_no": 3,
    "name": "A Peek Beyond the Point",
    "book_part": "Ganita Prakash Grade 7 Part I, Chapter 3",
    "source_pdf": "textbooks/class7/gegp103.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Tenths and Hundredths",
     "Why a ruler needs smaller units, then lengths in tenths and in hundredths: reading, writing, ordering, "
     "adding and subtracting them."),
    ("M2", "Decimal Place Value and Units",
     "Why the unit is split into ten, the extension of the place value ladder to thousandths, writing and "
     "reading decimals, and changing units of length, weight and money."),
    ("M3", "Locating, Comparing and Computing",
     "Decimals on the number line, comparing and finding the closest decimal, adding and subtracting decimals "
     "with estimates, and decimal sequences."),
    ("M4", "More on the Decimal System",
     "Everyday decimal mix-ups, the history of decimal notation, and a closing summary of the chapter."),
]

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "The chapter follows the book's own order: smaller units first, then tenths and hundredths as parts "
             "of a unit, then the decimal point as a way of writing them, then comparing and computing. Every "
             "decimal rule is reached from the fractions the student already knows.",
    "points": [
        {"title": "Try first, name later",
         "text": "The hook video leaves Sonu's two screws unmeasured. The tenth, the hundredth and the decimal "
                 "point arrive only after the student has met a gap that a whole mark cannot name."},
        {"title": "Fractions underneath every decimal",
         "text": "A decimal is a count of tenths, hundredths or thousandths. Adding, subtracting and comparing "
                 "decimals use the same place value moves as whole numbers, so nothing is a trick to remember."},
        {"title": "One zoom per digit",
         "text": "On the number line each digit names one more zoom into ten equal parts, and the end marks of a "
                 "line decide what one division is worth."},
        {"title": "Concept, then practice, topic by topic",
         "text": "Each idea gets its own topic with one video per concept and a practice concept at the end; "
                 "interactive tools appear only where handling the numbers is the idea. The book's questions "
                 "follow in their own topic, one question and one video per concept."},
    ],
}

NCERT_ITEMS = [
    # 3.1
    "3.1.story", "3.1.which_scale", "3.1.screws", "3.1.meaning", "3.1.why_smaller", "3.1.measure", "3.1.objects"
    # 3.2
    "3.2.pencil", "3.2.reading", "3.2.usb", "3.2.order1", "3.2.order2", "3.2.arm", "3.2.honeybee", "3.2.finger",
    "3.2.convert_tenths", "3.2.fish", "3.2.seq"
    # 3.3
    "3.3.paper", "3.3.hundredth", "3.3.mathtalk", "3.3.wire", "3.3.wire_boxes", "3.3.read_lengths",
    "3.3.longest", "3.3.add", "3.3.add_mathtalk", "3.3.add_hundredths", "3.3.sub", "3.3.sub_hund", "3.3.sub2",
    "3.3.sub_mathtalk", "3.3.FiO"
    # 3.4
    "3.4.why_ten", "3.4.thousandth", "3.4.howbig", "3.4.notation", "3.4.mathtalk", "3.4.readtable_a",
    "3.4.readtable_e", "3.4.tenths", "3.4.hundredths"
    # end.FiO13
    "end.FiO13"
    # end.FiO1
    "end.FiO1"
    # end.FiO2
    "end.FiO2"
    # end.FiO14
    "end.FiO14"
    # end.FiO16
    "end.FiO16"
    # 3.5
    "3.5.mm_cm", "3.5.mm_cm_blanks", "3.5.small_things", "3.5.cm_m", "3.5.cm_m_blanks", "3.5.m_mm",
    "3.5.facts_cm", "3.5.g_kg", "3.5.g_kg_blanks", "3.5.rice", "3.5.mg", "3.5.facts_nature", "3.5.paise",
    "3.5.paise_blanks", "3.5.old_prices"
    # end.FiO11
    "end.FiO11"
    # end.FiO12
    "end.FiO12"
    # 3.6
    "3.6.one_four", "3.6.divisions", "3.6.identify_abcd", "3.6.zoom_4185", "3.6.zoom_q", "3.6.zoom_make",
    "3.6.line5to10", "3.6.line_def", "3.6.zero_dilemma", "3.6.zero_order", "3.6.same", "3.6.compare_6456",
    "3.6.why_stop", "3.6.compare_three", "3.6.closest1", "3.6.closest109", "3.6.closest4", "3.6.closest_1b",
    "3.6.closest25"
    # end.FiO3
    "end.FiO3"
    # end.FiO4
    "end.FiO4"
    # end.FiO5
    "end.FiO5"
    # end.FiO6
    "end.FiO6"
    # 3.7
    "3.7.cloth_add", "3.7.detail_add", "3.7.est_sum", "3.7.FiO1", "3.7.cloth_sub", "3.7.detail_sub",
    "3.7.est_diff", "3.7.FiO2", "3.7.seq_try", "3.7.seq_more", "3.7.seq_own"
    # end.FiO7
    "end.FiO7"
    # end.FiO15
    "end.FiO15"
    # end.FiO8
    "end.FiO8"
    # end.FiO9
    "end.FiO9"
    # end.FiO10
    "end.FiO10"
    # 3.8
    "3.8.disasters", "3.8.fuel", "3.8.bus", "3.8.door", "3.8.overs", "3.8.nondecimals", "3.8.history_india",
    "3.8.history_point_comma"
    # summary
    "summary",
]


MISCONCEPTIONS = [
    ("M_PART_AS_UNIT", "A part of a unit is counted as a whole unit, so a length of 7 tenths is read as 7 units."),
    ("M_BIGGER_DENOMINATOR", "A fraction with a bigger denominator is a bigger number, so 1/100 is bigger than 1/10."),
    ("M_ADD_DENOMINATORS", "When fractions with a common denominator are added, the denominators are added too, "
                           "so 7/10 + 6/10 is written as 13/20."),
    ("M_BORROW_ONE", "When a digit is too small, the neighbouring digit is changed by the wrong amount, or the "
                     "borrowed unit is not turned into ten of the next smaller place."),
    ("M_POINT_ALIGN", "Decimals are lined up at the right end instead of at the decimal point."),
    ("M_READ_PLACE", "The digits after the point are read as one whole number, or a zero place holder is left out, "
                     "so 4.06 is written as 4.6."),
    ("M_TWO_WHOLE", "The part after the decimal point is a second whole number, so 2.35 is thought of as 2 and 35."),
    ("M_UNIT_SHIFT", "Changing to a smaller unit makes the number smaller, or the decimal point is moved the wrong "
                     "number of places."),
    ("M_LINE_MARKS", "Every division on a number line is worth one tenth, whatever the end marks of the line are."),
    ("M_MORE_DIGITS_BIGGER", "A decimal with more digits is a bigger number."),
    ("M_RIGHT_ZERO", "Zeroes at the right end of a decimal change its value, or zeroes before a digit do not."),
    ("M_FIRST_DIGIT", "Closeness or size is judged from the first digit alone, without comparing the next places or "
                      "the size of the gap."),
    ("M_EST_RANGE", "The estimate of a sum or a difference is taken as the answer, or the range is placed wrongly."),
    ("M_TIME_DECIMAL", "A number written with a point, such as hours and minutes or overs, is a decimal fraction "
                       "of ten parts."),
]

SOLUTION_NOTES = [
    "Hand, box and leaf readings (a tenth part): the book gives only the USB cable reading in the text, the other "
    "three objects are in a picture; the plan uses sample readings 1 6/10, 2 3/10 and 3 9/10.",
    "Identify the decimals against A, B, C and D (locating decimals): the answer is in a picture; the plan uses "
    "5.09, 5.13, 5.2 and 5.31, described in words.",
    "In each group of lengths, part (e) in the book's answer lists 9/100 as the shortest, but 2/100 is shorter; "
    "2/100 is taught.",
    "In each group of lengths, part (f) in the book's answer prints the longest as 7 5/100; the group has 7 5/10, "
    "which is the longest, so 7 5/10 is taught.",
    "End of chapter Figure it Out Q10: the question prints 6.18, 6.17 after 7.28, but the pattern (plus 0.9, minus "
    "0.01) and the book's answer both need 8.18, 8.17, so 8.18, 8.17 is taught.",
    "End of chapter Figure it Out Q15: the book's boxes are in a picture; with two decimals of one whole digit and "
    "three decimal digits the sum 10.500 is reachable (0.643 + 9.857), which beats the book's 10.501, so 10.500 is "
    "taught.",
    "End of chapter Figure it Out Q3: the marks are described in words from the picture (6.45, 6.525, 6.55).",
    "Dosa and rice prices (Try This in units of measurement): an open discussion with adults; the plan only "
    "converts the printed prices.",
]
ERRATA = []

DESIGN_REFERENCES = [
    {"text": "docs/25_new_design_learning_plan_playbook.md: framing intro, idea topics ending in "
             "a practice concept, a question topic after each idea topic, and one summary topic; the Class 7 "
             "Chapter 10 plan for one video per concept and one question per concept.", "url": ""},
]

FIGURES = {
    "T1.C1": ["Two screws that look the same but differ slightly in length, lying next to a ruler with no numbers."],
    "T2.C1": ["A ruler with each centimetre split into 10 equal parts and a screw ending between two whole marks."],
    "T4.C1": ["A paper strip folded in half, with a unit split into 10 tenths and each tenth into 10 hundredths."],
    "T7.C2": ["A place value table with columns Hundreds, Tens, Ones, Tenths, Hundredths and Thousandths."],
    "T9.C2": ["A number line that zooms in three times to locate 4.185."],
}

# Hook slot extras (build.py passes these into the hook's worklist slot).
HOOK_HANDOVER = ("Try it: for two screws that look the same, write how you would measure the gap between their "
                 "lengths, before the next topic.")
HOOK_NOTE = ("The hook leaves Sonu's two screws unmeasured. Do not confirm any length; the tenth and the hundredth "
             "in the next topics settle it.")

# Words the narration may need that are hard for a Class 7 reader; the script author defines or avoids them.
HARD_WORDS = ["fraction", "regroup", "estimate", "sequence", "decimal", "equivalent", "thousandth", "hundredth"]
