# Representative learning plan: Class 10, Coordinate Geometry (maths10_ch7)

A review copy of the restructured plan, down to concept level. Content is shown in full. Media are only named and never embedded.

Source: `learning_plan_std10_chap7_version1.json`. Shape follows the Class 9 circles plan.

## Read this first

**Standing decisions**
- No tools in this chapter. The six old `2d_tool` items are held (Appendix B).
- No videos for exercise questions. Each question concept gets one hint-free image spec and no video.
- Examples keep the existing videos and images that match them. No new example media is planned.
- The question order inside a Questions topic is by group, then by book question number.

**What a concept entry shows**
- `kind`: try, prove, teach, enrich, hook, exercise or summary.
- `objectives`: objective IDs. Enrichment concepts have none.
- `media`: existing assets re-homed from the old plan, new asset specs, or none.
- `[block_kind]` tags are review labels only. They never reach the student.

**Text cleanup applied to everything below**
- "Fig. 7.x" and "see Fig. 7.x" are removed. The figure is carried by the image.
- "Section 7.x" becomes a plain phrase.
- "Chapter 2" and "Chapter 6" become "earlier".
- "Example n:" and "Exercise 7.x" labels are removed.
- Book references stay only in metadata (`ncert_refs`), which is not shown here.

**Marked in the text**
- `[authored]` marks text that is not in the old plan or the book. These are predictions, answers to "(Why?)" prompts and new objective wording.
- Question solutions (`steps` and `answer`) are not in the old plan. They are marked *to author* and nothing is invented here.

## Plan at a glance

| Module | Topic | Concepts |
|---|---|---|
| M1 Locating points on a plane | T1 Finding Our Way on a Plane (hook) | C1 |
| | T2 Points on the Coordinate Plane | C2–C3 |
| M2 Distance between two points | T3 How Far Apart Are Two Points? | C4–C6 |
| | T4 Examples: Distance Between Points | C7–C11 |
| | T5 Questions: Distance Between Points | C12–C21 |
| M3 Dividing a segment | T6 Dividing a Segment in a Ratio | C22–C25 |
| | T7 Examples: Dividing a Segment | C26–C30 |
| | T8 Questions: Dividing a Segment | C31–C40 |
| M4 Wrap-up | T9 Chapter Summary | C41–C42 |

Totals: 42 concepts and 28 objectives. 20 question concepts need a new image. 0 new videos.

---

# M1 · Locating points on a plane

## T1 · Finding Our Way on a Plane (hook)

### C1 · Pictures from points, and where this chapter goes
`kind: hook` · `is_enrichment: true` · `objectives: none`
Media: existing video "From Coordinates to Curves — Linear and Quadratic Graphs Side by Side" (old T2 VID1)

[textbook_text]
> Coordinate geometry has been developed as an algebraic tool for studying geometry of figures. It helps us to study geometry using algebra, and understand algebra with the help of geometry. Because of this, coordinate geometry is widely applied in various fields such as physics, engineering, navigation, seismology and art!
>
> You have seen that a linear equation in two variables of the form ax + by + c = 0 (a, b not both zero), when represented graphically, gives a straight line. You have also seen that the graph of y = ax² + bx + c (a ≠ 0) is a parabola.
>
> In this chapter, you will learn how to find the distance between two points whose coordinates are given. You will also study how to find the coordinates of the point which divides a line segment joining two given points in a given ratio.

*(Cleanup: the "Chapter 2" pointer became "earlier". The "Also…" sentence was reordered so the paragraph opens on the idea. No words dropped.)*

---

## T2 · Points on the Coordinate Plane

### C2 · Axes, quadrants and the address of a point
`kind: teach` · `objectives: O1, O2`
Media: existing video "Building the Coordinate Plane — Step-by-Step Animation" (old T1 VID1); existing image "Four-Quadrant Coordinate Plane with Labeled Axes and Sample Points" (old T1 E1)

[textbook_text]
> In Class IX, you have studied that to locate the position of a point on a plane, we require a pair of coordinate axes. The distance of a point from the y-axis is called its x-coordinate, or abscissa. The distance of a point from the x-axis is called its y-coordinate, or ordinate. The coordinates of a point on the x-axis are of the form (x, 0), and of a point on the y-axis are of the form (0, y).

### C3 · Plot a picture from points
`kind: teach` · `objectives: O3`
Media: existing image "Delhi Metro Stations on a Coordinate Grid" (old T2 O1.E1)

[textbook_text]
> Here is a play for you. Draw a pair of perpendicular axes on a graph paper. Now plot the following points and join them as directed:
> Join the point A(4, 8) to B(3, 9) to C(3, 8) to D(1, 6) to E(1, 5) to F(3, 3) to G(6, 3) to H(8, 5) to I(8, 6) to J(6, 8) to K(6, 9) to L(5, 8) to A.
> Then join the points P(3.5, 7), Q(3, 6) and R(4, 6) to form a triangle. Also join the points X(5.5, 7), Y(5, 6) and Z(6, 6) to form a triangle. Now join S(4, 5), T(4.5, 4) and U(5, 5) to form a triangle. Lastly join S to the points (0, 5) and (0, 6) and join U to the points (9, 5) and (9, 6).
> What picture have you got?

---

# M2 · Distance between two points

## T3 · How Far Apart Are Two Points?

### C4 · The distance formula: try it first
`kind: try` · `objectives: O4`
Media: none
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[textbook_text]
> A town B is located 36 km east and 15 km north of the town A. How would you find the distance from town A to town B without actually measuring it? You may use the Pythagoras theorem to calculate this distance.
>
> Now, suppose two points lie on the x-axis. Can we find the distance between them? For instance, consider two points A(4, 0) and B(6, 0). The points A and B lie on the x-axis. From the figure you can see that OA = 4 units and OB = 6 units. Therefore, the distance of B from A, i.e., AB = OB – OA = 6 – 4 = 2 units. So, if two points lie on the x-axis, we can easily find the distance between them.
>
> Now, suppose we take two points lying on the y-axis. If the points C(0, 3) and D(0, 8) lie on the y-axis, similarly we find that CD = 8 – 3 = 5 units.
>
> Next, can you find the distance of A from C? Since OA = 4 units and OC = 3 units, the distance of A from C, i.e., AC = √(3² + 4²) = 5 units. Similarly, you can find the distance of B from D, BD = 10 units.
>
> Now, if we consider two points not lying on a coordinate axis, can we find the distance between them? Yes! We shall use the Pythagoras theorem to do so.

[theorem_statement] *(authored from the chapter summary)*
> The distance between P(x₁, y₁) and Q(x₂, y₂) is √((x₂ – x₁)² + (y₂ – y₁)²).

[predict] `[authored]`
> Two towns lie 36 km east and 15 km north of each other. Guess the straight-line distance before we derive anything. Is it nearer 40 km or nearer 50 km? Commit to an answer. The next concept shows why the formula gives the exact value.

### C5 · Why the distance formula works
`kind: prove` · `objectives: O5, O6`
Media: existing video "Animated Derivation of the Distance Formula Using Pythagoras" (old T3 VID1); existing images "Right Triangle PTQ for Distance Formula Derivation" (old T3 O1.E1) and "Distance from Origin — Right Triangle OPQ" (old T3 O2.E1)

[textbook_text]
> In the figure, the points P(4, 6) and Q(6, 8) lie in the first quadrant. How do we use the Pythagoras theorem to find the distance between them? Let us draw PR and QS perpendicular to the x-axis from P and Q respectively. Also, draw a perpendicular from P on QS to meet QS at T. Then the coordinates of R and S are (4, 0) and (6, 0), respectively. So, RS = 2 units. Also, QS = 8 units and TS = PR = 6 units. Therefore, QT = 2 units and PT = RS = 2 units.
>
> Now, using the Pythagoras theorem, we have
> PQ² = PT² + QT² = 2² + 2² = 8
> So, PQ = 2√2 units.
>
> How will we find the distance between two points in two different quadrants?
>
> Consider the points P(6, 4) and Q(–5, –3). Draw QS perpendicular to the x-axis. Also draw a perpendicular PT from the point P on QS (extended) to meet the y-axis at the point R. Then PT = 11 units and QT = 7 units. (Why?) Using the Pythagoras theorem on the right triangle PTQ, we get PQ = √(11² + 7²) = √170 units.
>
> Let us now find the distance between any two points P(x₁, y₁) and Q(x₂, y₂). Draw PR and QS perpendicular to the x-axis. A perpendicular from the point P on QS is drawn to meet it at the point T.
> Then, OR = x₁, OS = x₂. So, RS = x₂ – x₁ = PT.
> Also, SQ = y₂, ST = PR = y₁. So, QT = y₂ – y₁.
>
> Now, applying the Pythagoras theorem in △PTQ, we get
> PQ² = PT² + QT² = (x₂ – x₁)² + (y₂ – y₁)²
> Therefore, PQ = √((x₂ – x₁)² + (y₂ – y₁)²).
>
> Note that since distance is always non-negative, we take only the positive square root. So, the distance between the points P(x₁, y₁) and Q(x₂, y₂) is
> PQ = √((x₂ – x₁)² + (y₂ – y₁)²),
> which is called the distance formula.

[textbook_text · remarks]
> 1. In particular, the distance of a point P(x, y) from the origin O(0, 0) is given by OP = √(x² + y²).
> 2. We can also write PQ = √((x₁ – x₂)² + (y₁ – y₂)²). (Why?)

### C6 · More to explore: the book's "Why?" prompts
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: none

[enrichment] `[authored answers]`
> **Q.** For P(6, 4) and Q(–5, –3), why is PT = 11 units and QT = 7 units?
> **A.** PT runs along the horizontal line through P from x = 6 to x = –5, so PT = 6 – (–5) = 11. QT runs along the vertical line through Q from y = –3 to y = 4, so QT = 4 – (–3) = 7.

[enrichment] `[authored answers]`
> **Q.** Why can we also write PQ = √((x₁ – x₂)² + (y₁ – y₂)²)?
> **A.** (x₁ – x₂)² = (x₂ – x₁)² and (y₁ – y₂)² = (y₂ – y₁)², because squaring removes the sign. So swapping the points gives the same distance.

---

## T4 · Examples: Distance Between Points

### C7 · Do these three points make a triangle?
`kind: exercise (worked example)` · `objectives: O7`
Media: existing video "Worked Walkthrough — Distance Formula to Triangle Classification" (old T4 VID1); existing image "Triangle A(3,2), Q(-2,-3), R(2,3) with Computed Side Labels" (old T4 E1)

[question]
> Do the points (3, 2), (–2, –3) and (2, 3) form a triangle? If so, name the type of triangle formed.

[worked solution, from source]
> Let us apply the distance formula to find the distances PQ, QR and PR, where P(3, 2), Q(–2, –3) and R(2, 3) are the given points. We have
> PQ = √((3+2)² + (2+3)²) = √(5² + 5²) = √50 = 7.07 (approx.)
> QR = √((–2–2)² + (–3–3)²) = √((–4)² + (–6)²) = √52 = 7.21 (approx.)
> PR = √((3–2)² + (2–3)²) = √(1² + (–1)²) = √2 = 1.41 (approx.)
> Since the sum of any two of these distances is greater than the third distance, the points P, Q and R form a triangle.
> Also, PQ² + PR² = QR², so by the converse of the Pythagoras theorem, ∠P = 90°. Therefore, PQR is a right triangle.

### C8 · Are these four points the corners of a square?
`kind: exercise (worked example)` · `objectives: O7`
Media: existing image "Coordinate Plot Forming a Rhombus — A(4,0), B(0,3), C(-4,0), D(0,-3)" (old T2 O2.E1). The fit is loose, so please check it in review.

[question]
> Show that the points (1, 7), (4, 2), (–1, –1) and (–4, 4) are the vertices of a square.

[worked solution, from source]
> Let A(1, 7), B(4, 2), C(–1, –1) and D(–4, 4) be the given points. One way of showing that ABCD is a square is to use the property that all its sides should be equal and both its diagonals should also be equal. Now,
> AB = √((1–4)² + (7–2)²) = √(9+25) = √34
> BC = √((4+1)² + (2+1)²) = √(25+9) = √34
> CD = √((–1+4)² + (–1–4)²) = √(9+25) = √34
> DA = √((1+4)² + (7–4)²) = √(25+9) = √34
> AC = √((1+1)² + (7+1)²) = √(4+64) = √68
> BD = √((4+4)² + (2–4)²) = √(64+4) = √68
> Since AB = BC = CD = DA and AC = BD, all four sides of the quadrilateral ABCD are equal and its diagonals AC and BD are also equal. Therefore, ABCD is a square.
>
> **Alternative solution.** We find the four sides and one diagonal, say AC, as above. Here AD² + DC² = 34 + 34 = 68 = AC². Therefore, by the converse of the Pythagoras theorem, ∠D = 90°. A quadrilateral with all four sides equal and one angle 90° is a square. So, ABCD is a square.

### C9 · Are the three desks in a line?
`kind: exercise (worked example)` · `objectives: O8`
Media: none (the book's own figure of the desks is a source figure; to be confirmed)

[question]
> The figure shows the arrangement of desks in a classroom. Ashima, Bharti and Camella are seated at A(3, 1), B(6, 4) and C(8, 6) respectively. Do you think they are seated in a line? Give reasons for your answer.

[worked solution, from source]
> Using the distance formula, we have
> AB = √((6–3)² + (4–1)²) = √(9+9) = √18 = 3√2
> BC = √((8–6)² + (6–4)²) = √(4+4) = √8 = 2√2
> AC = √((8–3)² + (6–1)²) = √(25+25) = √50 = 5√2
> Since AB + BC = 3√2 + 2√2 = 5√2 = AC, we can say that the points A, B and C are collinear. Therefore, they are seated in a line.

### C10 · A rule for points equally far from two points
`kind: exercise (worked example)` · `objectives: O9, O10`
Media: existing video "Worked Walkthrough — Equidistant Point Derivation" (old T5 VID1); existing image "Mobile Tower Equidistant from Amarpur A(7,1) and Barauli B(3,5)" (old T5 E1)

[question]
> Find a relation between x and y such that the point (x, y) is equidistant from the points (7, 1) and (3, 5).

[worked solution, from source]
> Let P(x, y) be equidistant from the points A(7, 1) and B(3, 5). We are given that AP = BP. So, AP² = BP², i.e.,
> (x – 7)² + (y – 1)² = (x – 3)² + (y – 5)²
> i.e., x² – 14x + 49 + y² – 2y + 1 = x² – 6x + 9 + y² – 10y + 25
> i.e., x – y = 2
> which is the required relation.

[remark, from source]
> The graph of the equation x – y = 2 is a line. From your earlier studies, you know that a point which is equidistant from A and B lies on the perpendicular bisector of AB. Therefore, the graph of x – y = 2 is the perpendicular bisector of AB.

### C11 · A point on the y-axis equally far from two points
`kind: exercise (worked example)` · `objectives: O9`
Media: none

[question]
> Find a point on the y-axis which is equidistant from the points A(6, 5) and B(–4, 3).

[worked solution, from source]
> We know that a point on the y-axis is of the form (0, y). So, let the point P(0, y) be equidistant from A and B. Then
> (6 – 0)² + (5 – y)² = (–4 – 0)² + (3 – y)²
> i.e., 36 + 25 + y² – 10y = 16 + 9 + y² – 6y
> i.e., 4y = 36
> i.e., y = 9
> So, the required point is (0, 9).
>
> Let us check our solution: AP = √((6–0)² + (5–9)²) = √(36+16) = √52. BP = √((–4–0)² + (3–9)²) = √(16+36) = √52.
>
> **Note.** Using the remark above, we see that (0, 9) is the intersection of the y-axis and the perpendicular bisector of AB.

---

## T5 · Questions: Distance Between Points

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, statement only, no working and no answer. There is no video. Hint, solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for all 10.

**Group "Distance Between Two Points"** · objective **O11** (apply): find the distance between two given points, and find a missing coordinate from a given distance.

### C12 · Distance Between Two Points, Q1
`objectives: O11` · Media: new image spec (statement only)
> Find the distance between the following pairs of points:
> (i) (2, 3), (4, 1)  (ii) (–5, 7), (–1, 3)  (iii) (a, b), (–a, –b)

### C13 · Distance Between Two Points, Q2
`objectives: O11` · Media: new image spec (statement only)
> Find the distance between the points (0, 0) and (36, 15). Can you now find the distance between the two towns A and B discussed earlier?

### C14 · Distance Between Two Points, Q3
`objectives: O11` · Media: new image spec (statement only)
> Find the values of y for which the distance between the points P(2, –3) and Q(10, y) is 10 units.

**Group "Reading Shapes from Coordinates"** · objective **O12** (evaluate): verify a classification (collinear, isosceles, square, other quadrilateral) against the computed side and diagonal lengths.

### C15 · Reading Shapes from Coordinates, Q1
`objectives: O12` · Media: new image spec (statement only)
> Determine if the points (1, 5), (2, 3) and (–2, –11) are collinear.

### C16 · Reading Shapes from Coordinates, Q2
`objectives: O12` · Media: new image spec (statement only)
> Check whether (5, –2), (6, 4) and (7, –2) are the vertices of an isosceles triangle.

### C17 · Reading Shapes from Coordinates, Q3
`objectives: O12` · Media: new image spec (**the book's own figure only**, as it supplies the seat positions)
> In a classroom, 4 friends are seated at the points A, B, C and D as shown in the figure. Champa and Chameli walk into the class and after observing for a few minutes Champa asks Chameli, "Don't you think ABCD is a square?" Chameli disagrees. Using the distance formula, find which of them is correct.

### C18 · Reading Shapes from Coordinates, Q4
`objectives: O12` · Media: new image spec (statement only)
> Name the type of quadrilateral formed, if any, by the following points, and give reasons for your answer:
> (i) (–1, –2), (1, 0), (–1, 2), (–3, 0)
> (ii) (–3, 5), (3, 1), (0, 3), (–1, –4)
> (iii) (4, 5), (7, 6), (4, 3), (1, 2)

**Group "Equal Distances"** · objective **O13** (apply): set PA² = PB² and solve for a point or a relation.

### C19 · Equal Distances, Q1
`objectives: O13` · Media: new image spec (statement only)
> Find the point on the x-axis which is equidistant from (2, –5) and (–2, 9).

### C20 · Equal Distances, Q2
`objectives: O13` · Media: new image spec (statement only)
> If Q(0, 1) is equidistant from P(5, –3) and R(x, 6), find the values of x. Also find the distances QR and PR.

### C21 · Equal Distances, Q3
`objectives: O13` · Media: new image spec (statement only)
> Find a relation between x and y such that the point (x, y) is equidistant from the points (3, 6) and (–3, 4).

---

# M3 · Dividing a segment

## T6 · Dividing a Segment in a Ratio

### C22 · The section formula: try it first
`kind: try` · `objectives: O14`
Media: existing image "Segment AB with Division Point P — Ratio Labels m₁ and m₂" (old T8 E1)
No tool, so this concept has the statement and a prediction only.

[textbook_text]
> Recall the situation of the two towns. Suppose a telephone company wants to position a relay tower at P between A and B in such a way that the distance of the tower from B is twice its distance from A. If P lies on AB, it will divide AB in the ratio 1 : 2. If we take A as the origin O, and 1 km as one unit on both axes, the coordinates of B will be (36, 15). In order to know the position of the tower, we must know the coordinates of P. How do we find these coordinates?

[theorem_statement] *(authored from the chapter summary)*
> The coordinates of the point P(x, y) which divides the line segment joining A(x₁, y₁) and B(x₂, y₂) internally in the ratio m₁ : m₂ are
> ( (m₁x₂ + m₂x₁)/(m₁ + m₂), (m₁y₂ + m₂y₁)/(m₁ + m₂) ).

[predict] `[authored]`
> A tower stands one-third of the way from A(0, 0) to B(36, 15). Guess its coordinates before we derive anything. Which is more likely: (12, 5), (18, 7.5) or (24, 10)? Commit, then follow the next concept to settle it.

### C23 · Why the section formula works
`kind: prove` · `objectives: O15, O16`
Media: existing video "Animated Section Formula Derivation — AA Similarity Step by Step" (old T7 VID1); existing images "Section Formula Derivation — Segment AB with Perpendicular Projections and Ratio m₁:m₂" (old T7 O1.E1) and "AA Similarity Triangles APQ and BPC — Corresponding Sides and Angles Marked" (old T7 O1.E2)

[textbook_text]
> Let the coordinates of P be (x, y). Draw perpendiculars from P and B to the x-axis, meeting it in D and E, respectively. Draw PC perpendicular to BE. Then, by the AA similarity criterion studied earlier, △POD and △BPC are similar. Therefore,
> OD/PC = OP/PB = 1/2, and PD/BC = OP/PB = 1/2
> So, x/(36 – x) = 1/2 and y/(15 – y) = 1/2.
> These equations give x = 12 and y = 5.
> You can check that P(12, 5) meets the condition that OP : PB = 1 : 2.
>
> Now let us use the understanding that you may have developed through this example to obtain the general formula.
>
> Consider any two points A(x₁, y₁) and B(x₂, y₂) and assume that P(x, y) divides AB internally in the ratio m₁ : m₂, i.e., PA/PB = m₁/m₂.
>
> Draw AR, PS and BT perpendicular to the x-axis. Draw AQ and PC parallel to the x-axis. Then, by the AA similarity criterion, △PAQ ~ △BPC.
> Therefore, PA/BP = AQ/PC = PQ/BC  (1)
>
> Now,
> AQ = RS = OS – OR = x – x₁
> PC = ST = OT – OS = x₂ – x
> PQ = PS – QS = PS – AR = y – y₁
> BC = BT – CT = BT – PS = y₂ – y
>
> Substituting these values in (1), we get
> m₁/m₂ = (x – x₁)/(x₂ – x) = (y – y₁)/(y₂ – y)
>
> Taking m₁/m₂ = (x – x₁)/(x₂ – x), we get x = (m₁x₂ + m₂x₁)/(m₁ + m₂).
> Similarly, taking m₁/m₂ = (y – y₁)/(y₂ – y), we get y = (m₁y₂ + m₂y₁)/(m₁ + m₂).
>
> So, the coordinates of the point P(x, y) which divides the line segment joining A(x₁, y₁) and B(x₂, y₂) internally in the ratio m₁ : m₂ are
> ( (m₁x₂ + m₂x₁)/(m₁ + m₂), (m₁y₂ + m₂y₁)/(m₁ + m₂) )  (2)
> This is known as the section formula.
>
> This can also be derived by drawing perpendiculars from A, P and B on the y-axis and proceeding as above.
>
> If the ratio in which P divides AB is k : 1, then the coordinates of the point P will be
> ( (kx₂ + x₁)/(k + 1), (ky₂ + y₁)/(k + 1) ).

### C24 · The midpoint is a special case
`kind: teach` · `objectives: O17, O18`
Media: existing video "Midpoint Formula — Derived from Section Formula via 1:1 Substitution" (old T9 VID1); existing image "Midpoint M of Segment PQ with Equal Sub-Segments PM and MQ" (old T9 E1)

[textbook_text]
> The mid-point of a line segment divides the line segment in the ratio 1 : 1. Therefore, the coordinates of the mid-point P of the join of the points A(x₁, y₁) and B(x₂, y₂) is
> ( (1·x₁ + 1·x₂)/(1 + 1), (1·y₁ + 1·y₂)/(1 + 1) ) = ( (x₁ + x₂)/2, (y₁ + y₂)/2 ).

### C25 · More to explore: checking and cross-checking
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: none

[enrichment] `[authored answer]`
> **Q.** Check that P(12, 5) really satisfies OP : PB = 1 : 2 for O(0, 0) and B(36, 15).
> **A.** OP = √(12² + 5²) = 13 and PB = √(24² + 10²) = 26, so OP : PB = 13 : 26 = 1 : 2.

[enrichment, from source note]
> **Q.** You can also find a dividing ratio by calculating the distances PA and PB and taking their ratio. When is that allowed?
> **A.** Only when you know that A, P and B are collinear.

---

## T7 · Examples: Dividing a Segment

### C26 · The point three-quarters of the way along a segment
`kind: exercise (worked example)` · `objectives: O19`
Media: none

[question]
> Find the coordinates of the point which divides the line segment joining the points (4, –3) and (8, 5) in the ratio 3 : 1 internally.

[worked solution, from source]
> Let P(x, y) be the required point. Using the section formula, we get
> x = (3(8) + 1(4))/(3 + 1) = 7,  y = (3(5) + 1(–3))/(3 + 1) = 3
> Therefore, (7, 3) is the required point.

### C27 · In what ratio does a point divide a segment?
`kind: exercise (worked example)` · `objectives: O19`
Media: existing video "Dual Method — Section Formula vs. k:1 Ratio Trick" (old T8 VID1; its title names Example 6 but its content is the dual method used here, so please check the fit)

[question]
> In what ratio does the point (–4, 6) divide the line segment joining the points A(–6, 10) and B(3, –8)?

[worked solution, from source]
> Let (–4, 6) divide AB internally in the ratio m₁ : m₂. Using the section formula, we get
> (–4, 6) = ( (3m₁ – 6m₂)/(m₁ + m₂), (–8m₁ + 10m₂)/(m₁ + m₂) )  (1)
> Recall that if (x, y) = (a, b) then x = a and y = b.
> So, –4 = (3m₁ – 6m₂)/(m₁ + m₂) and 6 = (–8m₁ + 10m₂)/(m₁ + m₂).
> Now, –4 = (3m₁ – 6m₂)/(m₁ + m₂) gives us
> –4m₁ – 4m₂ = 3m₁ – 6m₂, i.e., 7m₁ = 2m₂, i.e., m₁ : m₂ = 2 : 7.
> You should verify that the ratio satisfies the y-coordinate also.
> Now, (–8m₁ + 10m₂)/(m₁ + m₂) = (–8(m₁/m₂) + 10)/((m₁/m₂) + 1)  (dividing throughout by m₂)
> = (–8 × (2/7) + 10)/((2/7) + 1) = 6.
> Therefore, the point (–4, 6) divides the line segment joining A(–6, 10) and B(3, –8) in the ratio 2 : 7.
>
> **Alternatively.** The ratio m₁ : m₂ can also be written as (m₁/m₂) : 1, or k : 1. Let (–4, 6) divide AB internally in the ratio k : 1. Using the section formula, we get
> (–4, 6) = ( (3k – 6)/(k + 1), (–8k + 10)/(k + 1) )  (2)
> So, –4 = (3k – 6)/(k + 1), i.e., –4k – 4 = 3k – 6, i.e., 7k = 2, i.e., k : 1 = 2 : 7.
> You can check for the y-coordinate also.
> So, the point (–4, 6) divides the line segment joining A(–6, 10) and B(3, –8) in the ratio 2 : 7.
>
> **Note.** You can also find this ratio by calculating the distances PA and PB and taking their ratio, provided you know that A, P and B are collinear.

### C28 · Points that cut a segment into three equal parts
`kind: exercise (worked example)` · `objectives: O21, O22`
Media: existing video "Animated Trisection — Why Ratio 1:2 for P and 2:1 for Q" (old T11 VID1); existing images "Jaipur–Agra Highway with Dhaba at Ratio 1:2 and Second Stop at 2:1" (old T11 O1.E1) and "Trisection of Segment A(2,-2) to B(-7,4) — Points P(-1,0) and Q(-4,2)" (old T11 O2.E1)

[question]
> Find the coordinates of the points of trisection (i.e., points dividing in three equal parts) of the line segment joining the points A(2, –2) and B(–7, 4).

[worked solution, from source]
> Let P and Q be the points of trisection of AB, i.e., AP = PQ = QB. Therefore, P divides AB internally in the ratio 1 : 2. Therefore, the coordinates of P, by applying the section formula, are
> ( (1(–7) + 2(2))/(1 + 2), (1(4) + 2(–2))/(1 + 2) ), i.e., (–1, 0).
> Now, Q also divides AB internally in the ratio 2 : 1. So, the coordinates of Q are
> ( (2(–7) + 1(2))/(2 + 1), (2(4) + 1(–2))/(2 + 1) ), i.e., (–4, 2).
> Therefore, the coordinates of the points of trisection of the line segment joining A and B are (–1, 0) and (–4, 2).
>
> **Note.** We could also have obtained Q by noting that it is the mid-point of PB. So, we could have obtained its coordinates using the mid-point formula.

### C29 · In what ratio does the y-axis cut a segment?
`kind: exercise (worked example)` · `objectives: O20`
Media: existing image "Segment A(5,-6) to B(-1,-4) Intersecting the y-Axis at P(0,-13/3)" (old T10 E1)

[question]
> Find the ratio in which the y-axis divides the line segment joining the points (5, –6) and (–1, –4). Also find the point of intersection.

[worked solution, from source]
> Let the ratio be k : 1. Then by the section formula, the coordinates of the point which divides AB in the ratio k : 1 are ( (–k + 5)/(k + 1), (–4k – 6)/(k + 1) ).
> This point lies on the y-axis, and we know that on the y-axis the abscissa is 0. Therefore, (–k + 5)/(k + 1) = 0. So, k = 5.
> That is, the ratio is 5 : 1. Putting the value of k = 5, we get the point of intersection as (0, –13/3).

### C30 · Finding a missing corner of a parallelogram
`kind: exercise (worked example)` · `objectives: O18`
Media: existing video "Animated Walkthrough — Parallelogram Diagonal Bisection" (old T10 VID1)

[question]
> If the points A(6, 1), B(8, 2), C(9, 4) and D(p, 3) are the vertices of a parallelogram, taken in order, find the value of p.

[worked solution, from source]
> We know that the diagonals of a parallelogram bisect each other. So, the coordinates of the mid-point of AC = the coordinates of the mid-point of BD, i.e.,
> ( (6 + 9)/2, (1 + 4)/2 ) = ( (8 + p)/2, (2 + 3)/2 )
> i.e., (15/2, 5/2) = ( (8 + p)/2, 5/2 )
> so, 15/2 = (8 + p)/2, i.e., p = 7.

---

## T8 · Questions: Dividing a Segment

Same rules as the distance questions: `attempt_first`, one new hint-free image spec each, no video, and steps and answer *to author*.

**Group "Dividing in a Ratio"** · objective **O23** (apply): coordinates of a point from a stated division, including fraction-to-ratio conversion.

### C31 · Dividing in a Ratio, Q1
`objectives: O23` · Media: new image spec (statement only)
> Find the coordinates of the point which divides the join of (–1, 7) and (4, –3) in the ratio 2 : 3.

### C32 · Dividing in a Ratio, Q2
`objectives: O23` · Media: new image spec (statement only)
> If A and B are (–2, –2) and (2, –4), respectively, find the coordinates of P such that AP = (3/7)AB and P lies on the line segment AB.

**Group "Finding the Ratio"** · objective **O24** (apply): find the ratio of a division, including by an axis.

### C33 · Finding the Ratio, Q1
`objectives: O24` · Media: new image spec (statement only)
> Find the ratio in which the line segment joining the points (–3, 10) and (6, –8) is divided by (–1, 6).

### C34 · Finding the Ratio, Q2
`objectives: O24` · Media: new image spec (statement only)
> Find the ratio in which the line segment joining A(1, –5) and B(–4, 5) is divided by the x-axis. Also find the coordinates of the point of division.

**Group "Equal Parts"** · objective **O23** (shared, as above).

### C35 · Equal Parts, Q1
`objectives: O23` · Media: new image spec (statement only)
> Find the coordinates of the points of trisection of the line segment joining (4, –1) and (–2, –3).

### C36 · Equal Parts, Q2
`objectives: O23` · Media: new image spec (statement only)
> Find the coordinates of the points which divide the line segment joining A(–2, 2) and B(2, 8) into four equal parts.

**Group "Midpoints at Work"** · objective **O25** (apply): use the midpoint in a figure or a real situation.

### C37 · Midpoints at Work, Q1
`objectives: O25` · Media: new image spec (**the book's own figure only**, as it supplies the school-ground grid)
> To conduct Sports Day activities, in your rectangular shaped school ground ABCD, lines have been drawn with chalk powder at a distance of 1 m each. 100 flower pots have been placed at a distance of 1 m from each other along AD, as shown in the figure. Niharika runs (1/4)th the distance AD on the 2nd line and posts a green flag. Preet runs (1/5)th the distance AD on the eighth line and posts a red flag. What is the distance between both the flags? If Rashmi has to post a blue flag exactly halfway between the line segment joining the two flags, where should she post her flag?

### C38 · Midpoints at Work, Q2
`objectives: O25` · Media: new image spec (statement only)
> Find the coordinates of a point A, where AB is the diameter of a circle whose centre is (2, –3) and B is (1, 4).

**Group "Shapes on the Grid"** · objective **O26** (evaluate): use diagonals, midpoints and distances to find a missing vertex or an area, then check the result against the figure's properties.

### C39 · Shapes on the Grid, Q1
`objectives: O26` · Media: new image spec (statement only)
> If (1, 2), (4, y), (x, 6) and (3, 5) are the vertices of a parallelogram taken in order, find x and y.

### C40 · Shapes on the Grid, Q2
`objectives: O26` · Media: new image spec (statement only)
> Find the area of a rhombus if its vertices are (3, 0), (4, 5), (–1, 4) and (–2, –1) taken in order.
> **Hint (shown only after the attempt):** Area of a rhombus = ½ × (product of its diagonals).

---

# M4 · Wrap-up

## T9 · Chapter Summary

### C41 · Chapter summary
`kind: summary` · `objectives: O27, O28`
Media: existing video "Chapter 7 Recap — One Example Per Formula with Selection Decision" (old T13 VID1); existing image "Chapter 7 Summary Infographic — Three Formulas with Diagrams and Selection Signals" (old T13 E1). Two images that give away the method are also re-homed here: "Exercise 7.1 Reference Card — Collinearity, Right Triangle, and Quadrilateral Checks" (old T6 E1) and "Formula Decision Tree — Which Formula to Use for Exercise 7.2" (old T12 E1). Both are renamed at build, since their titles carry the book's exercise numbers.

[summary_points]
> In this chapter, you have studied the following points:
> 1. The distance between P(x₁, y₁) and Q(x₂, y₂) is √((x₂ – x₁)² + (y₂ – y₁)²).
> 2. The distance of a point P(x, y) from the origin is √(x² + y²).
> 3. The coordinates of the point P(x, y) which divides the line segment joining the points A(x₁, y₁) and B(x₂, y₂) internally in the ratio m₁ : m₂ are ( (m₁x₂ + m₂x₁)/(m₁ + m₂), (m₁y₂ + m₂y₁)/(m₁ + m₂) ).
> 4. The mid-point of the line segment joining the points P(x₁, y₁) and Q(x₂, y₂) is ( (x₁ + x₂)/2, (y₁ + y₂)/2 ).

### C42 · A note on dividing from outside the segment
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: none

[textbook_text · "A note to the reader"]
> The section formula gives the coordinates (x, y) of a point P which divides internally the line segment joining the points A(x₁, y₁) and B(x₂, y₂) in the ratio m₁ : m₂:
> x = (m₁x₂ + m₂x₁)/(m₁ + m₂),  y = (m₁y₂ + m₂y₁)/(m₁ + m₂).
> Note that, here, PA : PB = m₁ : m₂.
>
> However, if P does not lie between A and B but lies on the line AB, outside the line segment AB, and PA : PB = m₁ : m₂, we say that P divides externally the line segment joining the points A and B. You will study the section formula for such a case in higher classes.

---

# Appendix A · Objectives

Format: ID · bloom level · wording · old objective(s) it carries.

| ID | Bloom | Objective | Old ID |
|---|---|---|---|
| O1 | remember | State the names and sign conventions of all four quadrants, both axes and the origin on the Cartesian plane. | T1.O1 |
| O2 | apply | Plot ordered pairs on the coordinate plane and interpret each point's quadrant position and perpendicular distance from each axis. | T1.O2 |
| O3 | apply | Construct a geometric figure by plotting and joining a given sequence of coordinate points on graph paper. | T2.O1 |
| O4 | apply | State the distance formula, that the distance between P(x₁, y₁) and Q(x₂, y₂) is √((x₂–x₁)² + (y₂–y₁)²), and predict and test it on points on and off the axes. `[authored]` | new |
| O5 | evaluate | Derive the distance formula by constructing right triangle PTQ from perpendiculars to the x-axis and applying the Pythagoras theorem to its sides. | T3.O1 |
| O6 | apply | Calculate the distance from any point P(x, y) to the origin using the special case OP = √(x² + y²). | T3.O2 |
| O7 | apply | Calculate side lengths and diagonals of a coordinate triangle or quadrilateral, then classify the figure by comparing computed values. | T4.O1 |
| O8 | analyze | Determine whether three coordinate points are collinear by computing all pairwise distances and checking the sum-of-two condition. | T2.O2 |
| O9 | apply | Solve equidistance problems by squaring both sides of AP = BP and simplifying to derive the algebraic relation or the point. | T5.O1 |
| O10 | evaluate | Justify that the locus of points equidistant from A and B is the perpendicular bisector of AB, interpreting the derived linear equation geometrically. | T5.O2 |
| O11 | apply | Find the distance between two given points, and a missing coordinate from a given distance. | T6.O1 (part) |
| O12 | evaluate | Verify a geometric classification (collinear, isosceles, square, other quadrilateral) against computed side and diagonal lengths. | T6.O3 |
| O13 | apply | Solve multi-step equidistance problems by setting PA² = PB², expanding and simplifying to find missing coordinates. | T6.O2 |
| O14 | apply | State the section formula for internal division in the ratio m₁ : m₂ and predict and test it on a known ratio. `[authored]` | new |
| O15 | evaluate | Derive the section formula for internal division in ratio m₁ : m₂ by applying the AA similarity criterion to perpendicular projections onto the x-axis. | T7.O1 |
| O16 | apply | Compute dividing-point coordinates using the k : 1 form, recognising it as the section formula with m₂ = 1 rather than a separate result. | T7.O2 |
| O17 | understand | Explain how the midpoint formula follows from the section formula when the division ratio is 1 : 1. | T9.O1 |
| O18 | apply | Calculate the midpoint of a segment and use it to solve problems such as parallelogram diagonal bisection, verifying by equal distances. | T9.O2 |
| O19 | apply | Calculate dividing-point coordinates for a given internal ratio, and determine an unknown ratio by equating the section formula to a known coordinate. | T8.O1 |
| O20 | apply | Solve axis-intersection problems by setting the relevant coordinate to zero in the k : 1 form and computing the division ratio and intersection point. | T10.O1 |
| O21 | apply | Solve trisection problems by applying the section formula at ratio 1 : 2 for the first point and 2 : 1 for the second. | T11.O1 |
| O22 | analyze | Determine internal division ratios for word problems by interpreting the geometric or contextual condition before substituting into the section formula. | T11.O2 |
| O23 | apply | Compute coordinates of division points and equal-part points by applying the section formula with the correct ratio assignment. | T12.O2 |
| O24 | apply | Find the ratio in which a point or an axis divides a segment, and the point of division. | T12.O1 (part) |
| O25 | apply | Use the midpoint formula in a figure or a real situation. | T12.O2 (part) |
| O26 | evaluate | Verify answers against geometric constraints such as diagonal bisection, and use distances to find an area. | T12.O3 |
| O27 | evaluate | Justify the choice of distance, section or midpoint formula for a coordinate geometry problem by matching problem signals to each formula's derivation and purpose. | T13.O1 |
| O28 | analyze | Distinguish between numerical calculation tasks and locus or relation-finding tasks, and determine the appropriate solution form. | T13.O2 |

Note: the old "classify each question by technique" objectives (T6.O1, T12.O1) are split across the practice groups. Choosing a technique is now part of each group's objective wording.

# Appendix B · Held assets (not attached to the new plan; nothing deleted)

**Six old tools** (no tools in this chapter):
- T3 "Distance Formula Visualizer" (T2D1)
- T4 "Triangle Type Detector" (T2D1)
- T5 "Equidistant Point Finder" (T2D1)
- T8 "Section Formula Explorer" (T2D1)
- T11 "Trisection & Division Points Builder" (T2D1)
- T11 "Relay Tower Puzzle" (T2D2)

**Two old question videos** (no question videos for now):
- "Narrated Model Solutions — Q1(i) and Q7" (T6 VID1)
- "Narrated Model — Q8 Fraction-to-Ratio Conversion" (T12 VID1)

# Appendix C · Carried-over fields

Every old topic's `recall_questions`, `summary`, `key_terms`, `concept_bullets` and `detailed_summary` carry into the new topic that holds its text. They are not shown here, to keep this file reviewable. The nothing-deleted check at build time compares them field by field.
