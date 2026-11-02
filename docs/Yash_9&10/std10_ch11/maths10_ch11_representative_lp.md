# Representative learning plan: Class 10, Areas Related to Circles (maths10_ch11)

A review copy of the restructured plan, down to concept level. Content is shown in full. Media are only named and never embedded.

Source: `learning_plan_std10_chap11_version1.json`. Shape follows the Class 9 circles plan and the Class 10 coordinate geometry plan.

## Read this first

**Standing decisions**
- No tools in this chapter. The six old `2d_tool` items are held (Appendix B).
- No videos for exercise questions. Each question concept gets one hint-free image spec and no video. The five old practice-topic videos are held (Appendix B).
- Examples keep the existing videos and images that match them. No new example media is planned.
- No grouping inside the question topic. Each textbook question is its own concept, in textbook order, named "<set name>, Q<n>". A question with separate sub-parts is split, and each sub-part keeps its parent question's objectives. Sub-parts that build on each other stay one concept (noted under the topic).
- The book has one exercise set and no starred or end-of-chapter set. All 14 of its questions are included.
- The book derives the sector area formula by the unitary method, so that formula is a try and prove pair. The arc length formula gets a one-sentence derivation in the book, so it is one teach concept that holds both the rule and its reason. The segment rule is read off the figure, with no derivation, so it is a teach concept.
- The book has no opening paragraph before its first section, so there is no hook topic. The plan opens on the definitions, as the old plan did.

**What a concept entry shows**
- `kind`: try, prove, teach, exercise or summary.
- `objectives`: objective IDs. There are no enrichment concepts in this chapter.
- `media`: existing assets re-homed from the old plan, new asset specs, or none. Where the old title carries a book number, it is shown as found and marked for renaming at build.
- `[block_kind]` tags are review labels only. They never reach the student.

**Text cleanup applied to everything below**
- "Fig. 11.x", "(see Fig. 11.x)" and "as shown in Fig. 11.x" are removed or turned into "the figure". The figure is carried by the image.
- The section heading "11.1 Areas of Sector and Segment of a Circle" and "11.2 Summary" are dropped.
- "Example n:" and "Exercise 11.1" labels are removed. The equation numbers inside solutions ("(1)") stay, because they belong to the working.
- The exercise set's opening line "Unless stated otherwise, use π = 22/7." is repeated, in the book's own words, at the top of each question that does not state its own value of π, because each question concept is shown on its own.
- Book references stay only in metadata (`ncert_refs`), which is not shown here.

**Marked in the text**
- `[authored]` marks text that is not in the old plan or the book. In this chapter that is one prediction only. No objective is authored.
- Question solutions (`steps` and `answer`) are not in the old plan. They are marked *to author* and nothing is invented here.

## Plan at a glance

| Module | Topic | Concepts |
|---|---|---|
| M1 Sectors, arcs and segments | T1 Sectors and Segments | C1 |
|  | T2 Area of a Sector | C2–C3 |
|  | T3 Length of an Arc | C4 |
|  | T4 Area of a Segment | C5–C6 |
| M2 Worked examples and practice | T5 Examples: Sectors and Segments | C7–C8 |
|  | T6 Questions: Sectors and Segments | C9–C24 |
| M3 Wrap-up | T7 Chapter Summary | C25 |

Totals: 25 concepts and 21 objectives. 16 question concepts need a new image. 0 new videos.

---

# M1 · Sectors, arcs and segments

## T1 · Sectors and Segments

### C1 · Sectors and segments, minor and major
`kind: teach` · `objectives: O1, O2`
Media: existing video "Pizza Slice and Chord Cut — Sector vs Segment" (old T1 VID1); existing image "Labelled Sector and Segment of a Circle" (old T1 O1.E1)

[textbook_text]
> You have already come across the terms sector and segment of a circle in your earlier classes. Recall that the portion (or part) of the circular region enclosed by two radii and the corresponding arc is called a sector of the circle and the portion (or part) of the circular region enclosed between a chord and the corresponding arc is called a segment of the circle.
>
> Thus, in the figure, shaded region OAPB is a sector of the circle with centre O. ∠ AOB is called the angle of the sector. Note that in this figure, unshaded region OAQB is also a sector of the circle. For obvious reasons, OAPB is called the minor sector and OAQB is called the major sector. You can also see that angle of the major sector is 360° – ∠ AOB.
>
> Now, look at the next figure, in which AB is a chord of the circle with centre O. So, shaded region APB is a segment of the circle. You can also note that unshaded region AQB is another segment of the circle formed by the chord AB. For obvious reasons, APB is called the minor segment and AQB is called the major segment.

[remark, from source]
> When we write 'segment' and 'sector' we will mean the 'minor segment' and the 'minor sector' respectively, unless stated otherwise.

*(Cleanup: the section heading is dropped. "in Fig. 11.1" becomes "in the figure" and "look at Fig. 11.2 in which" becomes "look at the next figure, in which". The image carries both figures in its two panels. No words dropped.)*

---

## T2 · Area of a Sector

### C2 · The area of a sector: try it first
`kind: try` · `objectives: O4`
Media: new image spec "A Sector of Angle Theta" — A circle with centre O and radius r, with a radius OA and a second radius OB drawn out to the circle. The region between the two radii and the arc APB is shaded as the sector OAPB, with the angle at O marked as theta degrees. Beside the circle, a label says the whole disc has area pi r squared. No formula for the sector is shown.
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[textbook_text]
> Now with this knowledge, let us try to find some relations (or formulae) to calculate their areas.
>
> Let OAPB be a sector of a circle with centre O and radius r. Let the degree measure of ∠ AOB be θ.
>
> You know that area of a circle (in fact of a circular region or disc) is πr².

[theorem_statement] *(the book's own words, from the end of its derivation)*
> Area of the sector of angle θ = (θ/360) × πr², where r is the radius of the circle and θ the angle of the sector in degrees.

[predict] `[authored]`
> A sector of angle 90° is one quarter of the whole disc. What fraction of the disc is a sector of angle 60°? What about a sector of angle θ? Commit to a rule for the area of a sector of angle θ in a circle of radius r before reading on. The next concept shows where the rule comes from.

*(Cleanup: "(see Fig. 11.3)" is dropped; the figure is carried by the image on the next concept. The formula line is shown first here and again at the end of the derivation.)*

### C3 · Why the sector formula works
`kind: prove` · `objectives: O3`
Media: existing video "Animated Derivation of the Sector Area Formula" (old T2 VID1); existing image "Sector OAPB With Central Angle θ and Unitary Derivation" (old T2 O1.E1)

[textbook_text]
> In a way, we can consider this circular region to be a sector forming an angle of 360° (i.e., of degree measure 360) at the centre O. Now by applying the Unitary Method, we can arrive at the area of the sector OAPB as follows:
>
> When degree measure of the angle at the centre is 360, area of the sector = πr²
>
> So, when the degree measure of the angle at the centre is 1, area of the sector = πr² / 360
>
> Therefore, when the degree measure of the angle at the centre is θ, area of the sector = (πr² / 360) × θ = (θ/360) × πr².
>
> Thus, we obtain the following relation (or formula) for area of a sector of a circle:
>
> Area of the sector of angle θ = (θ/360) × πr²,
>
> where r is the radius of the circle and θ the angle of the sector in degrees.

---

## T3 · Length of an Arc

### C4 · The length of an arc of a sector
`kind: teach` · `objectives: O5`
Media: existing video "Cricket Boundary Arc Walkthrough" (old T3 VID1); existing image "Arc APB With Central Angle θ and Chord Comparison" (old T3 O1.E1). The video works an example of its own (a 70 m boundary, 30°) that is not in the book, so the fit is loose. Please check it in review.

[textbook_text]
> Now, a natural question arises : Can we find the length of the arc APB corresponding to this sector? Yes. Again, by applying the Unitary Method and taking the whole length of the circle (of angle 360°) as 2πr, we can obtain the required length of the arc APB as (θ/360) × 2πr.
>
> So, length of an arc of a sector of angle θ = (θ/360) × 2πr.

---

## T4 · Area of a Segment

### C5 · A segment is a sector minus a triangle
`kind: teach` · `objectives: O6`
Media: existing video "Animated Sector-minus-Triangle Subtraction" (old T4 VID1); existing image "Segment as Sector Minus Triangle" (old T4 O1.E1)

[textbook_text]
> Now let us take the case of the area of the segment APB of a circle with centre O and radius r. You can see that :
>
> Area of the segment APB = Area of the sector OAPB – Area of Δ OAB
> = (θ/360) × πr² – area of Δ OAB

*(Cleanup: "(see Fig. 11.4)" is dropped; the figure is carried by the image.)*

### C6 · The major sector and the major segment
`kind: teach` · `objectives: O7`
Media: new image spec "Major Sector and Major Segment" — Two side-by-side circles with centre O and radius r. On the left, radii OA and OB split the disc into a small shaded minor sector OAPB and a larger differently coloured major sector OAQB. On the right, the chord AB splits the disc into a small shaded minor segment APB and a larger differently coloured major segment AQB. Each region carries its name label.

[textbook_text]
> From the figures for the sector and the segment, you can observe that:
>
> Area of the major sector OAQB = πr² – Area of the minor sector OAPB
>
> and Area of major segment AQB = πr² – Area of the minor segment APB
>
> Let us now take some examples to understand these concepts (or results).

*(Cleanup: "Note : From Fig. 11.3 and Fig. 11.4 respectively, you can observe that:" becomes "From the figures for the sector and the segment, you can observe that:". The book's closing line leads into the examples and is kept here.)*

---

# M2 · Worked examples and practice

## T5 · Examples: Sectors and Segments

### C7 · A sector and its major sector
`kind: exercise (worked example)` · `objectives: O8`
Media: existing video "Two-Method Walkthrough of Worked Example 1" (old T5 VID1) [title carries a book number, renamed at build]; existing image "Step Layout for Worked Example 1 — Sector and Major Sector Areas" (old T5 O1.E1) [title carries a book number, renamed at build]

[question]
> Find the area of the sector of a circle with radius 4 cm and of angle 30°. Also, find the area of the corresponding major sector (Use π = 3.14).

[worked solution, from source]
> Given sector is OAPB.
> Area of the sector = (θ/360) × πr²
> = (30/360) × 3.14 × 4 × 4 cm²
> = (12.56 / 3) cm² = 4.19 cm² (approx.)
>
> Area of the corresponding major sector
> = πr² – area of sector OAPB
> = (3.14 × 16 – 4.19) cm²
> = 46.05 cm² = 46.1 cm² (approx.)
>
> Alternatively, area of the major sector = ((360 – θ)/360) × πr²
> = ((360 – 30)/360) × 3.14 × 16 cm²
> = (330/360) × 3.14 × 16 cm² = 46.05 cm²
> = 46.1 cm² (approx.)

*(Cleanup: "(see Fig. 11.5)" is dropped; the figure is carried by the image.)*

### C8 · A segment with a 120° angle, using trigonometry
`kind: exercise (worked example)` · `objectives: O9`
Media: existing video "Example 2 Animated Walkthrough with Trigonometry" (old T6 VID1) [title carries a book number, renamed at build]; existing image "Construction Diagram for Segment AYB With OM ⊥ AB" (old T6 O1.E1)

[question]
> Find the area of the segment AYB shown in the figure, if radius of the circle is 21 cm and ∠ AOB = 120°. (Use π = 22/7)

[worked solution, from source]
> Area of the segment AYB
> = Area of sector OAYB – Area of Δ OAB    (1)
>
> Now, area of the sector OAYB = (120/360) × (22/7) × 21 × 21 cm² = 462 cm²    (2)
>
> For finding the area of Δ OAB, draw OM ⊥ AB as shown in the figure.
> Note that OA = OB. Therefore, by RHS congruence, Δ AMO ≅ Δ BMO.
> So, M is the mid-point of AB and ∠ AOM = ∠ BOM = (1/2) × 120° = 60°.
>
> Let OM = x cm
> So, from Δ OMA, OM / OA = cos 60°
> or, x / 21 = 1/2    [cos 60° = 1/2]
> or, x = 21/2
> So, OM = 21/2 cm
>
> Also, AM / OA = sin 60° = √3 / 2
> So, AM = (21√3) / 2 cm
> Therefore, AB = 2 AM = 2 × (21√3)/2 cm = 21√3 cm
>
> So, area of Δ OAB = (1/2) × AB × OM = (1/2) × 21√3 × (21/2) cm²
> = (441√3) / 4 cm²    (3)
>
> Therefore, area of the segment AYB = (462 – (441√3)/4) cm²    [From (1), (2) and (3)]
> = (21/4) (88 – 21√3) cm²

*(Cleanup: "shown in Fig. 11.6" and "as shown in Fig. 11.7" become "shown in the figure" and "as shown in the figure". The image carries both figures.)*

---

## T6 · Questions: Sectors and Segments

Objectives for this set: O10 (apply) direct sector, quadrant and right-angle segment problems; O11 (analyze) find the central angle or radius from indirect data such as a circumference, a clock or a right angle; O12 (apply) arc length, sector area and segment area for chords at 60° and 120°; O13 (analyze) choose between the equilateral-triangle and the sin/cos route for the triangle in a segment; O14 (apply) grazing area at a square corner, and its increase for a longer rope; O15 (analyze) see that the corner restricts the region to a quarter circle and that doubling the rope quadruples the area; O16 (apply) wire length and sector area for a brooch, the area between umbrella ribs, and the area swept by wipers; O17 (analyze) find each sector's angle by dividing 360° by the number of equal parts; O18 (apply) the lighthouse sector, the table-cover designs and the sector formula multiple-choice question; O19 (analyze) recognise the equilateral case at 60° and use its shortcut.

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, showing the statement (for a split question, the stem and that one sub-part only), no working and no answer. Four questions come with the book's own figure (the horse, the brooch, the umbrella and the table cover), and their image shows that figure only. The book prints no hint for any question. There is no video. Solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for all 16.
The questions are in textbook order. The sub-parts of the fourth and the ninth question are independent tasks, so each is its own concept. The fifth question stays one concept, because its third part (the segment) uses the sector area found in its second part. The eighth question stays one concept, because its second part asks for the increase over the area found in its first part.

### C9 · Sectors and Segments, Q1
`objectives: O10` · Media: new image spec (statement only)
> Unless stated otherwise, use π = 22/7.
> Find the area of a sector of a circle with radius 6 cm if angle of the sector is 60°.

### C10 · Sectors and Segments, Q2
`objectives: O10, O11` · Media: new image spec (statement only)
> Unless stated otherwise, use π = 22/7.
> Find the area of a quadrant of a circle whose circumference is 22 cm.

### C11 · Sectors and Segments, Q3
`objectives: O11` · Media: new image spec (statement only)
> Unless stated otherwise, use π = 22/7.
> The length of the minute hand of a clock is 14 cm. Find the area swept by the minute hand in 5 minutes.

### C12 · Sectors and Segments, Q4 (i)
`objectives: O10, O11` · Media: new image spec (statement and this sub-part only)
> A chord of a circle of radius 10 cm subtends a right angle at the centre. Find the area of the corresponding : (Use π = 3.14)
> (i) minor segment

### C13 · Sectors and Segments, Q4 (ii)
`objectives: O10` · Media: new image spec (statement and this sub-part only)
> A chord of a circle of radius 10 cm subtends a right angle at the centre. Find the area of the corresponding : (Use π = 3.14)
> (ii) major sector

### C14 · Sectors and Segments, Q5
`objectives: O12, O13` · Media: new image spec (statement only)
> Unless stated otherwise, use π = 22/7.
> In a circle of radius 21 cm, an arc subtends an angle of 60° at the centre. Find:
> (i) the length of the arc
> (ii) area of the sector formed by the arc
> (iii) area of the segment formed by the corresponding chord

### C15 · Sectors and Segments, Q6
`objectives: O12, O13` · Media: new image spec (statement only)
> A chord of a circle of radius 15 cm subtends an angle of 60° at the centre. Find the areas of the corresponding minor and major segments of the circle. (Use π = 3.14 and √3 = 1.73)

### C16 · Sectors and Segments, Q7
`objectives: O12, O13` · Media: new image spec (statement only)
> A chord of a circle of radius 12 cm subtends an angle of 120° at the centre. Find the area of the corresponding segment of the circle. (Use π = 3.14 and √3 = 1.73)

### C17 · Sectors and Segments, Q8
`objectives: O14, O15` · Media: new image spec (**the book's own figure only**, as it shows the field, the peg and the rope)
> A horse is tied to a peg at one corner of a square shaped grass field of side 15 m by means of a 5 m long rope (see the figure). Find
> (i) the area of that part of the field in which the horse can graze.
> (ii) the increase in the grazing area if the rope were 10 m long instead of 5 m. (Use π = 3.14)

### C18 · Sectors and Segments, Q9 (i)
`objectives: O16` · Media: new image spec (**the book's own figure only**, as it shows the brooch and its diameters)
> Unless stated otherwise, use π = 22/7.
> A brooch is made with silver wire in the form of a circle with diameter 35 mm. The wire is also used in making 5 diameters which divide the circle into 10 equal sectors as shown in the figure. Find :
> (i) the total length of the silver wire required.

### C19 · Sectors and Segments, Q9 (ii)
`objectives: O16, O17` · Media: new image spec (**the book's own figure only**, as it shows the brooch and its diameters)
> Unless stated otherwise, use π = 22/7.
> A brooch is made with silver wire in the form of a circle with diameter 35 mm. The wire is also used in making 5 diameters which divide the circle into 10 equal sectors as shown in the figure. Find :
> (ii) the area of each sector of the brooch.

### C20 · Sectors and Segments, Q10
`objectives: O16, O17` · Media: new image spec (**the book's own figure only**, as it shows the umbrella and its ribs)
> Unless stated otherwise, use π = 22/7.
> An umbrella has 8 ribs which are equally spaced (see the figure). Assuming umbrella to be a flat circle of radius 45 cm, find the area between the two consecutive ribs of the umbrella.

### C21 · Sectors and Segments, Q11
`objectives: O16` · Media: new image spec (statement only)
> Unless stated otherwise, use π = 22/7.
> A car has two wipers which do not overlap. Each wiper has a blade of length 25 cm sweeping through an angle of 115°. Find the total area cleaned at each sweep of the blades.

### C22 · Sectors and Segments, Q12
`objectives: O18` · Media: new image spec (statement only)
> To warn ships for underwater rocks, a lighthouse spreads a red coloured light over a sector of angle 80° to a distance of 16.5 km. Find the area of the sea over which the ships are warned. (Use π = 3.14)

### C23 · Sectors and Segments, Q13
`objectives: O18, O19` · Media: new image spec (**the book's own figure only**, as it shows the six designs on the cover)
> Unless stated otherwise, use π = 22/7.
> A round table cover has six equal designs as shown in the figure. If the radius of the cover is 28 cm, find the cost of making the designs at the rate of ₹ 0.35 per cm². (Use √3 = 1.7)

### C24 · Sectors and Segments, Q14
`objectives: O18` · Media: new image spec (statement only)
> Tick the correct answer in the following :
> Area of a sector of angle p (in degrees) of a circle with radius R is
> (A) (p/180) × 2πR
> (B) (p/180) × πR²
> (C) (p/360) × 2πR
> (D) (p/720) × 2πR²

---

# M3 · Wrap-up

## T7 · Chapter Summary

### C25 · Chapter summary
`kind: summary` · `objectives: O20, O21`
Media: existing video "60-Second Recap of Areas Related to Circles" (old T12 VID1); existing image "Chapter Summary Infographic — Three Key Formulas" (old T12 O1.E1); existing image "Equilateral vs Non-Equilateral Inscribed Triangles" (old T8 O2.E1)
The third image compares the triangle at 60° (equilateral) with the triangle at 120° (split by OM ⊥ AB). It gives away the method for several questions, so it is re-homed here from the old practice topic and not attached to any question concept.

[summary_points]
> In this chapter, you have studied the following points :
> 1. Length of an arc of a sector of a circle with radius r and angle with degree measure θ is (θ/360) × 2πr
> 2. Area of a sector of a circle with radius r and angle with degree measure θ is (θ/360) × πr²
> 3. Area of segment of a circle = Area of the corresponding sector – Area of the corresponding triangle.

---

# Appendix A · Objectives

Format: ID · bloom level · wording · old objective(s) it carries.

| ID | Bloom | Objective | Old ID |
|---|---|---|---|
| O1 | understand | Represent the sector and segment of a circle on a labelled diagram that marks the radii, chord, arc, and central angle. | T1.O1 |
| O2 | analyze | Distinguish between the minor and major sector (and minor and major segment) of a circle by inspecting the central angle. | T1.O2 |
| O3 | understand | Explain how the area-of-sector formula (θ/360) × πr² follows from treating the full circle as a 360° sector via the unitary method. | T2.O1 |
| O4 | apply | Compute the area of a sector when the radius and the central angle (in degrees) are given. | T2.O2 |
| O5 | apply | Compute the length of an arc subtending an angle θ at the centre using the formula (θ/360) × 2πr. | T3.O1 |
| O6 | understand | Explain that the area of a minor segment equals the area of its sector minus the area of the triangle formed by the chord and the two radii. | T4.O1 |
| O7 | apply | Compute the area of a major sector or major segment using the identity πr² minus the corresponding minor region. | T4.O2 |
| O8 | apply | Solve for the area of a minor sector and its corresponding major sector when the radius and central angle are given, using two equivalent methods. | T5.O1 |
| O9 | apply | Solve for the area of a segment when the central angle is not 90° by using trigonometric ratios (sin, cos) to compute the inscribed isosceles triangle's area. | T6.O1 |
| O10 | apply | Solve direct sector-area problems and a right-angle chord segment problem using the standard area formulas. | T7.O1 |
| O11 | analyze | Determine the central angle from indirect data such as elapsed time on a clock or a right angle subtended by a chord. | T7.O2 |
| O12 | apply | Compute arc length, sector area, and segment area for chord-formed segments at angles such as 60° and 120°. | T8.O1 |
| O13 | analyze | Determine when to use right-triangle methods versus sin/cos methods for the inscribed triangle's area in a segment. | T8.O2 |
| O14 | apply | Compute the grazing area of a horse tied to a square field's corner using the quarter-circle formula (1/4) × πr², and the increase when the rope length is doubled. | T9.O1 |
| O15 | analyze | Determine that two perpendicular field walls at a corner restrict the horse to one quarter of its rope's full circle, and verify that doubling the rope quadruples the grazing area. | T9.O2 |
| O16 | apply | Compute the wire length and per-sector area for a brooch made of one circle plus 5 diameters (10 sectors), the area between two ribs of an 8-rib umbrella, and the area cleaned by two non-overlapping wipers. | T10.O1 |
| O17 | analyze | Determine the central angle of each sector by dividing 360° by the number of equal subdivisions (10 for the brooch, 8 for the umbrella) when the angle is not stated directly. | T10.O2 |
| O18 | apply | Compute the warned-sea area for an 80° lighthouse beam and the cost of six equilateral-triangle segment designs on a 28 cm round table cover, and identify the correct sector formula in a multiple-choice question. | T11.O1 |
| O19 | analyze | Determine when an inscribed triangle is equilateral (when θ = 60°) so that the segment shortcut ((θ/360) × πr²) – ((√3 / 4) r²) applies, instead of falling back to the sin/cos derivation. | T11.O2 |
| O20 | understand | Explain how the chapter's three key formulas (arc length, sector area, segment area) all arise from the Unitary Method and the central-angle fraction (θ/360). | T12.O1 |
| O21 | analyze | Determine the correct major-region identity (πr² minus the minor region) and the segment identity (sector minus triangle) when answering wrap-up questions across the chapter. | T12.O2 |

Note: all 21 old objectives are kept word for word, one to one. None is new or authored. The try concept for the sector formula carries the old "compute the area of a sector" objective (O4), and the prove concept carries the old "explain how the formula follows" objective (O3).

# Appendix B · Held assets (not attached to the new plan; nothing deleted)

**6 old tools** (no tools in this chapter):
- T1 "Sector & Segment Identifier" (T2D1)
- T2 "Sector Area & Arc Length Formula Builder" (T2D1)
- T4 "Segment Area Calculator" (T2D1)
- T7 "Clock Hand Area Sweeper" (T2D1)
- T8 "Combined Figures Area Solver" (T2D1)
- T10 "Brooch / Umbrella Designer" (T2D1)

**5 old question videos** (no question videos for now):
- "Strategy Walkthrough — Reading the Givens for Q1–Q4" (T7 VID1)
- "Method-Selection Strategy for Segment Problems" (T8 VID1)
- "Why Doubling the Rope Quadruples the Grazing Area" (T9 VID1)
- "Why 5 Diameters Make 10 Sectors" (T10 VID1)
- "Equilateral-Triangle Shortcut for the Round Table" (T11 VID1)

**4 other old images** (held because each shows a question's set-up together with its hidden givens or answer cues; the question concepts carry hint-free specs instead):
- "Question-Cue Diagrams for Q1–Q4" (T7 O2.E1): marks the hidden input of each question (the angle in the clock, the radius in the circumference, the right angle).
- "Horse Tied at the Corner of a Square Field" (T9 O2.E1): shades the quarter-circle grazing region for both rope lengths.
- "Brooch, Umbrella, and Wiper Reference Designs" (T10 O1.E1): labels the sector angles 36° and 45°.
- "Lighthouse Beam and Round Table Cover" (T11 O1.E1): marks each table-cover design as an equilateral-triangle segment.

# Appendix C · Carried-over fields

Every old topic's `recall_questions`, `summary`, `key_terms`, `concept_bullets`, `brief_summary`, `detailed_summary` and `important_points` carry into the new topic that holds its text. They are not shown here, to keep this file reviewable. The nothing-deleted check at build time compares them field by field.

Where each old topic's text and fields land:

| Old topic | New concepts |
|---|---|
| T1 Sectors and Segments — Definitions and Anatomy | C1 |
| T2 Area of a Sector — Formula and Derivation | C2, C3 |
| T3 Length of an Arc of a Sector | C4 |
| T4 Area of a Segment — Sector minus Triangle | C5, C6 |
| T5 Worked Example — Minor and Major Sector Area | C7 |
| T6 Worked Example — Segment Area Using Trigonometry | C8 |
| T7 Practice — Direct Sector, Quadrant, and Right-Angle Segment Problems | C9–C13 (Q1 to Q4) |
| T8 Practice — Mixed Arc, Sector, and Segment Computations | C14–C16 (Q5 to Q7), C25 (one image) |
| T9 Practice — Grazing Horse and a Square Corner | C17 (Q8) |
| T10 Practice — Sector Subdivisions and Sweep Designs | C18–C21 (Q9 to Q11) |
| T11 Practice — Lighthouse Beam, Table Designs, and a Formula MCQ | C22–C24 (Q12 to Q14) |
| T12 Chapter Summary — Key Formulas of Areas Related to Circles | C25 |
