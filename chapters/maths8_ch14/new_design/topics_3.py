# -*- coding: utf-8 -*-
"""Topics T9 (module M3, areas in real life) and T10 (summary). Book pp 170 to 171."""
from topics_common import A, DOER, FIO, TOPIC, WE

TOPICS = []
U9 = "In-text question (areas in real life, question %s)"

# ============================== T9 Areas in real life =========================================================
TOPICS.append(TOPIC(
    "T9", "M3", "Areas in Real Life", ["Areas in Real Life"], "Apply",
    "Students measure and estimate the areas of sheets, tables, rooms, schools and towns, convert between inches "
    "and centimetres and between square units, and choose sensible units from square centimetres to square kilometres.",
    "Real areas use many units: cm², in², ft², m², acres and km². A square unit converts by the length factor "
    "squared, so 1 in² = 6.4516 cm² and 1 km² = 1000000 m².",
    [A("T9.C1", "The area of an A4 sheet and a tabletop", "Apply",
       "Students compute the area of an A4 sheet from its side lengths and estimate a tabletop's area by counting "
       "how many sheets cover it.",
       textbook=["Areas in Real Life",
                 "What do you think is the area of an A4 sheet? Its sidelengths are 21 cm and 29.7 cm. Now find its "
                 "area.",
                 "What do you think is the area of the tabletop that you use at school or at home? You could perhaps "
                 "try to visualise how many A4 sheets can fit on your table."],
       teach=["Predict first: guess the area of an A4 sheet in square centimetres before measuring.",
              "Its sides are 21 cm and 29.7 cm, so length times width gives the area.",
              "Now use the sheet as a unit: count how many sheets would cover a table and multiply."],
       examples=[
           WE("Find the area of an A4 sheet, then estimate a table that is covered by 3 rows of 4 sheets.",
              ["A4 sheet: 21 × 29.7 = 623.7 cm².", "The table holds 3 × 4 = 12 sheets.",
               "Table ≈ 12 × 623.7 = 7484.4 cm², about 7500 cm²."],
              "The sheet is 623.7 cm²; the table is about 7500 cm²",
              ncert=["rl.a4", "rl.tabletop"])],
       key_terms=["area", "estimate", "sheet"], minutes=6),
     A("T9.C2", "Inches, centimetres and square inches", "Apply",
       "Students convert lengths between inches and centimetres, then show that one square inch equals 2.54 × 2.54 "
       "square centimetres and convert square units both ways.",
       textbook=["The dimensions of furniture like tables and chairs are sometimes measured in inches (in) and feet "
                 "(ft). 1 in = 2.54 cm, 1 ft = 12 in.",
                 "Express the following lengths in centimeters: (i) 5 in (ii) 7.4 in",
                 "Express the following lengths in inches: (i) 5.08 cm (ii) 11.43 cm",
                 "How many cm² is 1 in²? So, 1 in² = 2.54² cm² = 6.4516 cm².",
                 "How many cm² is 10 in²? 10 in² = 10 × 6.4516 cm² = 64.516 cm²."],
       teach=["Predict first: Keeko thinks that since 1 inch is 2.54 cm, 1 square inch is 2.54 square centimetres. "
              "Is that right?",
              "Lengths convert by multiplying or dividing by 2.54.",
              "A square inch is 2.54 cm long and 2.54 cm wide, so it holds 2.54 × 2.54 = 6.4516 cm², not 2.54."],
       examples=[
           WE("Convert 5 in to centimetres, 11.43 cm to inches, and 1 in² to square centimetres.",
              ["5 in = 5 × 2.54 = 12.7 cm.", "11.43 cm = 11.43 ÷ 2.54 = 4.5 in.",
               "1 in² = 2.54 × 2.54 = 6.4516 cm²."],
              "12.7 cm, 4.5 in and 6.4516 cm²",
              ncert=["rl.to_cm", "rl.to_inch", "rl.sq_in", "rl.ten_sq_in"])],
       key_terms=["square inch", "conversion", "centimetre"], misconceptions=["M_UNIT_SQUARE"], minutes=8),
     A("T9.C3", "Big areas: square metres, acres and square kilometres", "Apply",
       "Students choose square metres, acres or square kilometres for rooms, schools and towns, find how many "
       "square metres make a square kilometre, and meet local area units.",
       textbook=["What do you think is the area of your classroom? Areas of classroom, house, etc., are generally "
                 "measured in ft² or m².",
                 "What do you think is the area of your school? Make an estimate and compare it with the actual data.",
                 "Larger areas of land are also measured in acres. 1 acre = 43560 ft².",
                 "Besides these units, different parts of India use different local units for measuring area, such as "
                 "bigha, gaj, katha, dhur, cent, ankanam, etc.",
                 "Find out the local unit of area measurement in your region.",
                 "What do you think is the area of your village/town/city? Make an estimate and compare it with the "
                 "actual data. Larger areas are measured in km².",
                 "How many m² is a km²?"],
       teach=["Predict first: a square kilometre is 1000 m on each side. Is it 1000 square metres?",
              "A classroom suits square metres, a school suits square metres or acres, a town suits square kilometres. "
              "Many regions also use local units like bigha or cent.",
              "A square kilometre is 1000 m by 1000 m, so it holds 1000 × 1000 = 1000000 m²."],
       examples=[
           WE("A classroom is 8 m by 6 m. How many such classrooms would fit in 1 km²?",
              ["Classroom: 8 × 6 = 48 m².", "1 km² = 1000 × 1000 = 1000000 m².",
               "1000000 ÷ 48 ≈ 20833 classrooms."],
              "About 20833 classrooms",
              ncert=["rl.classroom", "rl.school", "rl.local_unit", "rl.village", "rl.km2"])],
       key_terms=["square kilometre", "acre", "square metre"], misconceptions=["M_UNIT_SQUARE"], minutes=8),
     DOER("T9.C4", "Practice: convert and compare real areas", "square_unit_scaler", "Apply",
          "Students convert between square centimetres, square inches and square feet, compare the sizes of a town "
          "and a school, and plan how to find the largest and smallest cities.",
          ["A square unit converts by the length factor multiplied by itself.",
           "1 in² = 6.4516 cm², 1 ft² = 144 in², 1 km² = 1000000 m².",
           "To compare two areas, write them in the same unit and divide."],
          items=[
              FIO("rl.convert", U9 % 1,
                  "Convert 161.29 cm² to in². Every 6.4516 cm² gives an in². Evaluate the quotient 161.29 ÷ 6.4516.",
                  ["1 in² = 6.4516 cm², so divide by 6.4516.", "161.29 ÷ 6.4516 = 25.",
                   "Check: 25 × 6.4516 = 161.29."],
                  "161.29 cm² = 25 in²"),
              FIO("rl.sq_ft", U9 % 2,
                  "How many in² is 1 ft²?",
                  ["1 ft = 12 in, so a square foot is 12 in by 12 in.", "1 ft² = 12 × 12 = 144 in²."],
                  "144 in²"),
              FIO("rl.times_bigger", U9 % 3,
                  "How many times is your village/town/city bigger than your school?",
                  ["Write both areas in the same unit, for example m².",
                   "For a school ground 100 m by 80 m: 100 × 80 = 8000 m². For a town of 10 km²: "
                   "10 × 1000000 = 10000000 m².",
                   "Divide: 10000000 ÷ 8000 = 1250."],
                  "For a 10 km² town and an 8000 m² school, 1250 times; use your own town and school data"),
              FIO("rl.largest_city", U9 % 4,
                  "Find the city with the largest area in (i) India, and (ii) the world.",
                  ["Decide what counts as the city: the area run by the city's own government.",
                   "Look up the areas in km² from an atlas, a census report or a government website.",
                   "Compare them in the same unit and pick the largest."],
                  "An open research task: find official areas in km² and compare; answers depend on how a city's "
                  "boundary is defined"),
              FIO("rl.smallest_city", U9 % 5,
                  "Find the city with the smallest area in (i) India, and (ii) the world.",
                  ["Use the same definition of a city as before.",
                   "Look up the areas in km² from reliable sources.",
                   "Compare them in the same unit and pick the smallest."],
                  "An open research task: compare official areas in km²; answers depend on the definition used")],
          ncert=["rl.quotient"], misconceptions=["M_UNIT_SQUARE"])],
    key_terms=["area", "square units", "conversion"]))

# ============================== T10 Summary ===================================================================
TOPICS.append(TOPIC(
    "T10", "M3", "Summary: Area", ["Summary"], "Remember",
    None,
    "Triangle, polygon, parallelogram, rhombus and trapezium areas, each found by cutting and rearranging into "
    "rectangles and triangles.",
    [A("T10.C1", "What we found about area", "Remember",
       "Students restate the area formulas for triangles, parallelograms, rhombuses and trapeziums and explain that "
       "any polygon's area comes from breaking it into triangles.",
       textbook=["Area of a triangle = 1/2 × base × height.",
                 "The area of any polygon can be evaluated by breaking it into triangles.",
                 "Area of a parallelogram = base × height.",
                 "Area of a rhombus = 1/2 × product of its diagonals.",
                 "Area of a trapezium = 1/2 × height × sum of parallel sides."],
       teach=["Our opening puzzle is settled: a square can be cut into four equal areas in endless ways, because area "
              "counts squares, not shapes.",
              "A triangle is half a rectangle; any polygon is a set of triangles; a parallelogram slides into a "
              "rectangle; a rhombus is half the rectangle on its diagonals; two trapeziums make a parallelogram.",
              "Every height is perpendicular to its base. Still open for you: estimate the area of your town."],
       ncert=["summary"], key_terms=["area", "formula"], video_focus=["RECAP"], minutes=8)],
    topic_type="summary"))
