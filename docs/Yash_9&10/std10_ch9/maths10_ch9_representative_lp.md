# Representative learning plan: Class 10, Some Applications of Trigonometry (maths10_ch9)

A review copy of the restructured plan, down to concept level. Content is shown in full. Media are only named and never embedded.

Source: `learning_plan_std10_chap9_version1.json`. Shape follows the Class 9 circles plan and the Class 10 coordinate geometry plan.

## Read this first

**Standing decisions**
- No tools in this chapter. The four old `2d_tool` items are held (Appendix B).
- No videos for exercise questions. Each question concept gets one hint-free image spec and no video. The old videos that walk through exercise questions are held (Appendix B).
- Examples keep the existing videos and images that match them. No new example media is planned.
- No grouping inside the question topics. Each textbook question is its own concept, in textbook order, named "<set name>, Q<n>". No question in this chapter has lettered sub-parts, so every question is one concept.
- The book has one exercise set (15 questions). It is split across two question topics, as the old plan split it: the first six questions after the one-angle examples, the other nine after the depression and two-angle examples. The question numbers stay the book's numbers.
- The book has no theorem and no derivation in this chapter, so there is no try or prove concept. The ratio-choosing method is a teach concept.
- Topic order follows the old plan: angle of depression and its two examples come before the two two-angle-of-elevation examples (the book has them the other way round). The worked examples keep their book numbers in metadata only.

**What a concept entry shows**
- `kind`: teach, enrich, hook, exercise or summary.
- `objectives`: objective IDs. Enrichment concepts have none.
- `media`: existing assets re-homed from the old plan, new asset specs, or none. Where the old title carries a book number (Fig., Example or Exercise), the builder strips it at build.
- `[block_kind]` tags are review labels only. They never reach the student.

**Text cleanup applied to everything below**
- "Fig. 9.x", "see Fig. 9.x" and "In Fig. 9.x" are removed or become "the figure". The figure is carried by the image.
- "Fig. 8.1", "Fig. 8.2" and "Fig. 8.3" (pictures from the previous chapter) become "the picture of the minar from the previous chapter", "the situation from the previous chapter" and "the third picture from the previous chapter".
- "Example n :" and "Exercise 9.1" labels and the section heading "9.1 Heights and Distances" are removed.
- Three book typos are corrected: "prvious" (in a sentence that is rewritten anyway), "trigonometic" and "joing".
- Book references stay only in metadata (`ncert_refs`), which is not shown here.

**Marked in the text**
- `[authored]` marks text that is not in the old plan or the book. Here that is only the answer to the book's one "(Why?)" prompt. No objective is newly authored.
- Question solutions (`steps` and `answer`) are not in the old plan. They are marked *to author* and nothing is invented here.

## Plan at a glance

| Module | Topic | Concepts |
|---|---|---|
| M1 Line of sight and angle of elevation | T1 Trigonometry Around Us (hook) | C1 |
|  | T2 Line of Sight and Angle of Elevation | C2–C3 |
|  | T3 Choosing the Right Ratio | C4 |
|  | T4 Examples: One Angle of Elevation | C5–C7 |
|  | T5 Questions: Ratios at Work | C8–C13 |
| M2 Angle of depression and two-angle problems | T6 Angle of Depression | C14 |
|  | T7 Examples: Angles of Depression | C15–C17 |
|  | T8 Examples: Two Angles of Elevation | C18–C19 |
|  | T9 Questions: Two Sightings | C20–C28 |
| M3 Wrap-up | T10 Chapter Summary | C29 |

Totals: 29 concepts and 38 objectives. 15 question concepts (6 + 9) need a new image. 0 new videos.

---

# M1 · Line of sight and angle of elevation

## T1 · Trigonometry Around Us (hook)

### C1 · Where trigonometry meets the world around you
`kind: hook` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Right triangles hidden in everyday scenes" — A bright three-part illustration. A student looks up at a tall tower, a girl on a balcony looks down at a flower pot by a temple across a river, and a hot air balloon floats in the sky with a girl and her mother looking up. In each scene a faint dotted right triangle joins the viewer, the object and the ground.

[textbook_text]
> In the previous chapter, you have studied about trigonometric ratios. In this chapter, you will be studying about some ways in which trigonometry is used in the life around you.

*(Cleanup: the section heading "9.1 Heights and Distances" is dropped. No words dropped from the paragraph.)*

---

## T2 · Line of Sight and Angle of Elevation

### C2 · The line of sight
`kind: teach` · `objectives: O1, O2`
Media: existing video "Qutub Minar: Drawing the Line of Sight Step by Step" (old T1 VID1); existing image "Line of Sight: Observer, Horizontal, and Oblique Segment (Fig. 9.1 Style)" (old T1 O1.E1)

[textbook_text]
> Let us consider the picture of the minar from the previous chapter, which is redrawn below.
>
> In this figure, the line AC drawn from the eye of the student to the top of the minar is called the line of sight. The student is looking at the top of the minar. The angle BAC, so formed by the line of sight with the horizontal, is called the angle of elevation of the top of the minar from the eye of the student.
>
> Thus, the line of sight is the line drawn from the eye of an observer to the point in the object viewed by the observer.

*(Cleanup: "Fig. 8.1 of prvious chapter, which is redrawn below in Fig. 9.1" becomes "the picture of the minar from the previous chapter, which is redrawn below". The image carries the figure.)*

### C3 · The angle of elevation
`kind: teach` · `objectives: O3, O4`
Media: existing video "Angle of Elevation: From Looking Straight Ahead to Looking Upward" (old T2 VID1); existing image "Angle of Elevation: Horizontal Reference and Upward Line of Sight (Fig. 9.2 Style)" (old T2 O1.E1)

[textbook_text]
> The angle of elevation of the point viewed is the angle formed by the line of sight with the horizontal when the point being viewed is above the horizontal level, i.e., the case when we raise our head to look at the object.

*(Cleanup: "(see Fig. 9.2)" is dropped.)*

---

## T3 · Choosing the Right Ratio

### C4 · What we need to know, and which ratio to use
`kind: teach` · `objectives: O5, O6`
Media: existing video "Which Ratio to Use: Priya's Mobile Tower — Step-by-Step Decision" (old T3 VID1); existing image "Ratio Selection Decision Tree: tan, sin, cos Based on Known and Unknown Sides" (old T3 O2.E1); existing image "Uttarayan Kite Festival: Kite String as Hypotenuse, Height Unknown (Indian Scenario)" (old T7 O1.E1). The kite image is a loose fit, please check: it is a new scenario (80 m string, 30°) where the sine is the right ratio, not a book question.

[textbook_text]
> Let us refer to the picture of the minar again. If you want to find the height CD of the minar without actually measuring it, what information do you need? You would need to know the following:
> (i) the distance DE at which the student is standing from the foot of the minar
> (ii) the angle of elevation, ∠BAC, of the top of the minar
> (iii) the height AE of the student.
>
> Assuming that the above three conditions are known, how can we determine the height of the minar?
>
> In the figure, CD = CB + BD. Here, BD = AE, which is the height of the student.
>
> To find BC, we will use trigonometric ratios of ∠BAC or ∠A.
>
> In △ABC, the side BC is the opposite side in relation to the known ∠A. Now, which of the trigonometric ratios can we use? Which one of them has the two values that we have and the one we need to determine? Our search narrows down to using either tan A or cot A, as these ratios involve AB and BC.
>
> Therefore, tan A = BC/AB or cot A = AB/BC, which on solving would give us BC.
>
> By adding AE to BC, you will get the height of the minar.
>
> Now let us explain the process, we have just discussed, by solving some problems.

*(Cleanup: "Fig. 9.1" becomes "the picture of the minar". The book's prompt about the third picture of the previous chapter ("Are they angles of elevation or angles of depression?") opens this passage in the book, but it needs the angle of depression, so it moves to C14. No words dropped.)*

---

## T4 · Examples: One Angle of Elevation

### C5 · The height of a tower from one angle
`kind: exercise (worked example)` · `objectives: O7, O8`
Media: existing video "Example 1 Worked: Finding Tower Height with tan 60° — Animated Solution" (old T4 VID1) [title carries a book number, renamed at build]; existing image "Example 1 Diagram: Tower AB, Observer C at 15 m, Angle 60° (Fig. 9.4 Style)" (old T4 O1.E1) [title carries a book number, renamed at build]

[question]
> A tower stands vertically on the ground. From a point on the ground, which is 15 m away from the foot of the tower, the angle of elevation of the top of the tower is found to be 60°. Find the height of the tower.

[worked solution, from source]
> First let us draw a simple diagram to represent the problem. Here AB represents the tower, CB is the distance of the point from the tower and ∠ACB is the angle of elevation. We need to determine the height of the tower, i.e., AB. Also, ACB is a triangle, right-angled at B.
>
> To solve the problem, we choose the trigonometric ratio tan 60° (or cot 60°), as the ratio involves AB and BC.
>
> Now, tan 60° = AB/BC
> i.e., √3 = AB/15
> i.e., AB = 15√3
> Hence, the height of the tower is 15√3 m.

### C6 · How long a ladder, and how far from the pole?
`kind: exercise (worked example)` · `objectives: O9, O10`
Media: existing video "Example 2 Worked: Finding Ladder Length Using sin 60° — Animated Solution" (old T5 VID1) [title carries a book number, renamed at build]; existing image "Example 2 Diagram: Electrician Ladder Against Pole, Two Unknowns BC and DC (Fig. 9.5 Style)" (old T5 O1.E1) [title carries a book number, renamed at build]

[question]
> An electrician has to repair an electric fault on a pole of height 5 m. She needs to reach a point 1.3 m below the top of the pole to undertake the repair work. What should be the length of the ladder that she should use which, when inclined at an angle of 60° to the horizontal, would enable her to reach the required position? Also, how far from the foot of the pole should she place the foot of the ladder? (You may take √3 = 1.73)

[worked solution, from source]
> In the figure, the electrician is required to reach the point B on the pole AD.
> So, BD = AD – AB = (5 – 1.3) m = 3.7 m.
> Here, BC represents the ladder. We need to find its length, i.e., the hypotenuse of the right triangle BDC.
> Now, can you think which trigonometric ratio should we consider?
> It should be sin 60°.
> So, BD/BC = sin 60° or 3.7/BC = √3/2
> Therefore, BC = (3.7 × 2)/√3 = 4.28 m (approx.)
> i.e., the length of the ladder should be 4.28 m.
> Now, DC/BD = cot 60° = 1/√3
> i.e., DC = 3.7/√3 = 2.14 m (approx.)
> Therefore, she should place the foot of the ladder at a distance of 2.14 m from the pole.

*(Cleanup: "(see Fig. 9.5)" is dropped from the question and "In Fig. 9.5" becomes "In the figure". "trigonometic" is corrected.)*

### C7 · A chimney seen from an observer's eyes
`kind: exercise (worked example)` · `objectives: O11, O12`
Media: existing video "Example 3 Worked: Adding Observer Height to Find Total Chimney Height" (old T6 VID1) [title carries a book number, renamed at build]; existing image "Example 3 Diagram: Observer with Eye-Level Offset and Chimney (Fig. 9.6 Style)" (old T6 O1.E1) [title carries a book number, renamed at build]

[question]
> An observer 1.5 m tall is 28.5 m away from a chimney. The angle of elevation of the top of the chimney from her eyes is 45°. What is the height of the chimney?

[worked solution, from source]
> Here, AB is the chimney, CD the observer and ∠ADE the angle of elevation. In this case, ADE is a triangle, right-angled at E and we are required to find the height of the chimney.
> We have AB = AE + BE = AE + 1.5
> and DE = CB = 28.5 m
> To determine AE, we choose a trigonometric ratio, which involves both AE and DE. Let us choose the tangent of the angle of elevation.
> Now, tan 45° = AE/DE
> i.e., 1 = AE/28.5
> Therefore, AE = 28.5
> So the height of the chimney (AB) = (28.5 + 1.5) m = 30 m.

---

## T5 · Questions: Ratios at Work

Objectives for this set: O13 (create) formulate a right-triangle equation from an unfamiliar real-world scene; O14 (apply) solve one-angle height, distance and length problems by choosing sin, cos or tan from the two sides involved; O15 (evaluate) check an answer with the Pythagoras theorem or by substituting back.

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, statement only (for the first question, the book's own figure only), no working and no answer. There is no video. Solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for all 6.
The questions are in textbook order. None has lettered sub-parts. The third question asks for two slide lengths ("in each case") but has no lettered parts, so it stays one concept.

### C8 · Ratios at Work, Q1
`objectives: O14, O15` · Media: new image spec (**the book's own figure only**, as it shows the pole and the rope)
> A circus artist is climbing a 20 m long rope, which is tightly stretched and tied from the top of a vertical pole to the ground. Find the height of the pole, if the angle made by the rope with the ground level is 30° (see the figure).

### C9 · Ratios at Work, Q2
`objectives: O13` · Media: new image spec (statement only)
> A tree breaks due to storm and the broken part bends so that the top of the tree touches the ground making an angle 30° with it. The distance between the foot of the tree to the point where the top touches the ground is 8 m. Find the height of the tree.

### C10 · Ratios at Work, Q3
`objectives: O14` · Media: new image spec (statement only)
> A contractor plans to install two slides for the children to play in a park. For the children below the age of 5 years, she prefers to have a slide whose top is at a height of 1.5 m, and is inclined at an angle of 30° to the ground, whereas for elder children, she wants to have a steep slide at a height of 3 m, and inclined at an angle of 60° to the ground. What should be the length of the slide in each case?

### C11 · Ratios at Work, Q4
`objectives: O14` · Media: new image spec (statement only)
> The angle of elevation of the top of a tower from a point on the ground, which is 30 m away from the foot of the tower, is 30°. Find the height of the tower.

### C12 · Ratios at Work, Q5
`objectives: O13` · Media: new image spec (statement only)
> A kite is flying at a height of 60 m above the ground. The string attached to the kite is temporarily tied to a point on the ground. The inclination of the string with the ground is 60°. Find the length of the string, assuming that there is no slack in the string.

### C13 · Ratios at Work, Q6
`objectives: O14, O15` · Media: new image spec (statement only)
> A 1.5 m tall boy is standing at some distance from a 30 m tall building. The angle of elevation from his eyes to the top of the building increases from 30° to 60° as he walks towards the building. Find the distance he walked towards the building.

---

# M2 · Angle of depression and two-angle problems

## T6 · Angle of Depression

### C14 · The angle of depression
`kind: teach` · `objectives: O16, O17, O18`
Media: existing video "Angle of Depression: Juhu Beach Lifeguard and Alternate Interior Angles" (old T8 VID1); existing image "Angle of Depression: Elevated Observer, Downward Line of Sight, Alternate Angle (Fig. 9.3 Style)" (old T8 O3.E1)

[textbook_text]
> Now, consider the situation from the previous chapter. The girl sitting on the balcony is looking down at a flower pot placed on a stair of the temple. In this case, the line of sight is below the horizontal level. The angle so formed by the line of sight with the horizontal is called the angle of depression.
>
> Thus, the angle of depression of a point on the object being viewed is the angle formed by the line of sight with the horizontal when the point is below the horizontal level, i.e., the case when we lower our head to look at the point being viewed.
>
> Now, you may identify the lines of sight, and the angles so formed in the third picture from the previous chapter. Are they angles of elevation or angles of depression?

*(Cleanup: "given in Fig. 8.2" becomes "from the previous chapter", "(see Fig. 9.3)" is dropped, and "in Fig. 8.3" becomes "in the third picture from the previous chapter". The last paragraph is moved here from the minar passage (C4), so the student meets it after both angles are defined. No words dropped.)*

---

## T7 · Examples: Angles of Depression

### C15 · Two buildings, two angles of depression
`kind: exercise (worked example)` · `objectives: O19, O20`
Media: existing video "Example 6 Worked: Two Depression Angles — Setting Up and Solving Two Equations" (old T9 VID1) [title carries a book number, renamed at build]; existing image "Example 6 Diagram: Two Buildings, Depression Angles 30° and 45° (Fig. 9.9 Style)" (old T9 O1.E1) [title carries a book number, renamed at build]

[question]
> The angles of depression of the top and the bottom of an 8 m tall building from the top of a multi-storeyed building are 30° and 45°, respectively. Find the height of the multi-storeyed building and the distance between the two buildings.

[worked solution, from source]
> In the figure, PC denotes the multi-storyed building and AB denotes the 8 m tall building. We are interested to determine the height of the multi-storeyed building, i.e., PC and the distance between the two buildings, i.e., AC.
> Look at the figure carefully. Observe that PB is a transversal to the parallel lines PQ and BD. Therefore, ∠QPB and ∠PBD are alternate angles, and so are equal.
> So ∠PBD = 30°. Similarly, ∠PAC = 45°.
> In right △PBD, we have
> PD/BD = tan 30° = 1/√3 or BD = PD√3
> In right △PAC, we have
> PC/AC = tan 45° = 1
> i.e., PC = AC
> Also, PC = PD + DC, therefore, PD + DC = AC.
> Since, AC = BD and DC = AB = 8 m, we get PD + 8 = BD = PD√3 (Why?)
> This gives PD = 8/(√3 – 1) = 8(√3 + 1)/((√3 + 1)(√3 – 1)) = 4(√3 + 1) m.
> So, the height of the multi-storeyed building is {4(√3 + 1) + 8} m = 4(3 + √3) m
> and the distance between the two buildings is also 4(3 + √3) m.

### C16 · More to explore: the book's "Why?" prompt
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "A rectangle between two buildings" — Two buildings side by side, the taller one with its top at P and foot at C, and the 8 m building with its top at B and foot at A. A horizontal line is drawn from B to meet the taller building at D, and the rectangle ABDC is shaded. The side DC = AB is labelled 8 m, and the sides BD and AC are highlighted as the opposite sides of the rectangle. The sight lines PB and PA are dotted.

[enrichment] `[authored answer]`
> **Q.** For the two buildings, why is PD + 8 = BD = PD√3?
> **A.** In right △PBD, tan 30° = PD/BD, so BD = PD√3. In right △PAC, tan 45° = 1, so AC = PC. Now PC = PD + DC and DC = AB = 8, so AC = PD + 8. Since ABDC is a rectangle, BD = AC. So BD = PD + 8, and also BD = PD√3.

### C17 · How wide is the river?
`kind: exercise (worked example)` · `objectives: O21, O22`
Media: existing video "Example 7 Worked: Adding Two Horizontal Distances to Find River Width" (old T10 VID1) [title carries a book number, renamed at build]; existing image "Example 7 Diagram: Bridge Point P Looking at Both River Banks (Fig. 9.10 Style)" (old T10 O1.E1) [title carries a book number, renamed at build]

[question]
> From a point on a bridge across a river, the angles of depression of the banks on opposite sides of the river are 30° and 45°, respectively. If the bridge is at a height of 3 m from the banks, find the width of the river.

[worked solution, from source]
> In the figure, A and B represent points on the bank on opposite sides of the river, so that AB is the width of the river. P is a point on the bridge at a height of 3 m, i.e., DP = 3 m. We are interested to determine the width of the river, which is the length of the side AB of the △APB.
> Now, AB = AD + DB
> In right △APD, ∠A = 30°.
> So, tan 30° = PD/AD
> i.e., 1/√3 = 3/AD or AD = 3√3 m
> Also, in right △PBD, ∠B = 45°. So, BD = PD = 3 m.
> Now, AB = BD + AD = 3 + 3√3 = 3(1 + √3) m.
> Therefore, the width of the river is 3(√3 + 1) m.

---

## T8 · Examples: Two Angles of Elevation

### C18 · A flagstaff on a building
`kind: exercise (worked example)` · `objectives: O23, O24`
Media: existing video "Example 4 Worked: Shared Base Strategy — Flagstaff Length from Two Elevation Angles" (old T11 VID1) [title carries a book number, renamed at build]; existing image "Example 4 Diagram: Building AB with Flagstaff BD, Two Elevation Angles from P (Fig. 9.7 Style)" (old T11 O1.E1) [title carries a book number, renamed at build]

[question]
> From a point P on the ground the angle of elevation of the top of a 10 m tall building is 30°. A flag is hoisted at the top of the building and the angle of elevation of the top of the flagstaff from P is 45°. Find the length of the flagstaff and the distance of the building from the point P. (You may take √3 = 1.732)

[worked solution, from source]
> In the figure, AB denotes the height of the building, BD the flagstaff and P the given point. Note that there are two right triangles PAB and PAD. We are required to find the length of the flagstaff, i.e., DB and the distance of the building from the point P, i.e., PA.
> Since, we know the height of the building AB, we will first consider the right △PAB.
> We have tan 30° = AB/AP
> i.e., 1/√3 = 10/AP
> Therefore, AP = 10√3
> i.e., the distance of the building from P is 10√3 m = 17.32 m.
> Next, let us suppose DB = x m. Then AD = (10 + x) m.
> Now, in right △PAD, tan 45° = AD/AP = (10 + x)/(10√3)
> Therefore, 1 = (10 + x)/(10√3)
> i.e., x = 10(√3 – 1) = 7.32
> So, the length of the flagstaff is 7.32 m.

### C19 · A tower and two shadows
`kind: exercise (worked example)` · `objectives: O25, O26`
Media: existing video "Example 5 Worked: Two Shadow Equations — Substitution Method to Find Tower Height" (old T12 VID1) [title carries a book number, renamed at build]; existing image "Example 5 Diagram: Tower with Two Shadow Lengths at Different Sun Altitudes (Fig. 9.8 Style)" (old T12 O1.E1) [title carries a book number, renamed at build]

[question]
> The shadow of a tower standing on a level ground is found to be 40 m longer when the Sun's altitude is 30° than when it is 60°. Find the height of the tower.

[worked solution, from source]
> In the figure, AB is the tower and BC is the length of the shadow when the Sun's altitude is 60°, i.e., the angle of elevation of the top of the tower from the tip of the shadow is 60° and DB is the length of the shadow, when the angle of elevation is 30°.
> Now, let AB be h m and BC be x m. According to the question, DB is 40 m longer than BC.
> So, DB = (40 + x) m
> Now, we have two right triangles ABC and ABD.
> In △ABC, tan 60° = AB/BC
> or, √3 = h/x    (1)
> In △ABD, tan 30° = AB/BD
> i.e., 1/√3 = h/(x + 40)    (2)
> From (1), we have h = x√3
> Putting this value in (2), we get (x√3)√3 = x + 40, i.e., 3x = x + 40
> i.e., x = 20
> So, h = 20√3    [From (1)]
> Therefore, the height of the tower is 20√3 m.

---

## T9 · Questions: Two Sightings

Objectives for this set: O27 (analyze) classify a problem by its right triangles and unknowns and choose the strategy first; O28 (apply) write one right-triangle equation per angle and link them through the shared side; O29 (evaluate) check an answer against both equations; O30, O31 (understand, apply) elevation and depression from the same point; O32, O33 (create, apply) two ships seen from a lighthouse; O34, O35 (understand, apply) a moving car seen at two angles of depression, and the time it takes.

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, statement only (for the fifth and eighth questions of this set, the book's own figure only), no working and no answer. There is no video. Solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for all 9.
The questions are in textbook order (book numbers 7 to 15). None has lettered sub-parts, so each is one concept.

### C20 · Two Sightings, Q7
`objectives: O27, O28` · Media: new image spec (statement only)
> From a point on the ground, the angles of elevation of the bottom and the top of a transmission tower fixed at the top of a 20 m high building are 45° and 60° respectively. Find the height of the tower.

### C21 · Two Sightings, Q8
`objectives: O28, O29` · Media: new image spec (statement only)
> A statue, 1.6 m tall, stands on the top of a pedestal. From a point on the ground, the angle of elevation of the top of the statue is 60° and from the same point the angle of elevation of the top of the pedestal is 45°. Find the height of the pedestal.

### C22 · Two Sightings, Q9
`objectives: O27` · Media: new image spec (statement only)
> The angle of elevation of the top of a building from the foot of the tower is 30° and the angle of elevation of the top of the tower from the foot of the building is 60°. If the tower is 50 m high, find the height of the building.

### C23 · Two Sightings, Q10
`objectives: O28` · Media: new image spec (statement only)
> Two poles of equal heights are standing opposite each other on either side of the road, which is 80 m wide. From a point between them on the road, the angles of elevation of the top of the poles are 60° and 30°, respectively. Find the height of the poles and the distances of the point from the poles.

### C24 · Two Sightings, Q11
`objectives: O28, O29` · Media: new image spec (**the book's own figure only**, as it shows the tower, the canal and the two points)
> A TV tower stands vertically on a bank of a canal. From a point on the other bank directly opposite the tower, the angle of elevation of the top of the tower is 60°. From another point 20 m away from this point on the line joining this point to the foot of the tower, the angle of elevation of the top of the tower is 30° (see the figure). Find the height of the tower and the width of the canal.

### C25 · Two Sightings, Q12
`objectives: O30, O31` · Media: new image spec (statement only)
> From the top of a 7 m high building, the angle of elevation of the top of a cable tower is 60° and the angle of depression of its foot is 45°. Determine the height of the tower.

### C26 · Two Sightings, Q13
`objectives: O32, O33` · Media: new image spec (statement only)
> As observed from the top of a 75 m high lighthouse from the sea-level, the angles of depression of two ships are 30° and 45°. If one ship is exactly behind the other on the same side of the lighthouse, find the distance between the two ships.

### C27 · Two Sightings, Q14
`objectives: O28, O29` · Media: new image spec (**the book's own figure only**, as it shows the girl and the two balloon positions)
> A 1.2 m tall girl spots a balloon moving with the wind in a horizontal line at a height of 88.2 m from the ground. The angle of elevation of the balloon from the eyes of the girl at any instant is 60°. After some time, the angle of elevation reduces to 30° (see the figure). Find the distance travelled by the balloon during the interval.

### C28 · Two Sightings, Q15
`objectives: O34, O35` · Media: new image spec (statement only)
> A straight highway leads to the foot of a tower. A man standing at the top of the tower observes a car at an angle of depression of 30°, which is approaching the foot of the tower with a uniform speed. Six seconds later, the angle of depression of the car is found to be 60°. Find the time taken by the car to reach the foot of the tower from this point.

---

# M3 · Wrap-up

## T10 · Chapter Summary

### C29 · Chapter summary
`kind: summary` · `objectives: O36, O37, O38`
Media: existing video "Chapter Review: Heights and Distances in Indian Everyday Life — Three Core Concepts" (old T17 VID1); existing image "Review Infographic: Angle of Elevation vs Angle of Depression Side-by-Side" (old T17 O2.E1)

[summary_points]
> In this chapter, you have studied the following points:
> 1. (i) The line of sight is the line drawn from the eye of an observer to the point in the object viewed by the observer.
> (ii) The angle of elevation of an object viewed, is the angle formed by the line of sight with the horizontal when it is above the horizontal level, i.e., the case when we raise our head to look at the object.
> (iii) The angle of depression of an object viewed, is the angle formed by the line of sight with the horizontal when it is below the horizontal level, i.e., the case when we lower our head to look at the object.
> 2. The height or length of an object or the distance between two distant objects can be determined with the help of trigonometric ratios.

*(Cleanup: the heading "9.2 Summary" is dropped.)*

---

# Appendix A · Objectives

Format: ID · bloom level · wording · old objective(s) it carries.

| ID | Bloom | Objective | Old ID |
|---|---|---|---|
| O1 | understand | Explain what the line of sight is and how it is formed between an observer and a viewed point. | T1.O1 |
| O2 | apply | Represent the line of sight as a geometric segment in a right-triangle diagram for a given real scenario. | T1.O2 |
| O3 | understand | Explain the angle of elevation as the angle formed by the line of sight with the horizontal when the object is above the observer. | T2.O1 |
| O4 | apply | Draw a labelled right-triangle diagram marking the angle of elevation, horizontal, line of sight, height, and base for a given scenario. | T2.O2 |
| O5 | understand | Interpret a heights-and-distances diagram to determine which trigonometric ratio (tan, sin, or cos) connects the known and unknown quantities. | T3.O1 |
| O6 | evaluate | Justify the selection of a specific trigonometric ratio by referencing which two sides of the right triangle are involved. | T3.O2 |
| O7 | understand | Interpret a single-angle-of-elevation word problem by drawing the right-triangle diagram and labelling all known quantities. | T4.O1 |
| O8 | apply | Calculate the height of a vertical structure using tan of the given angle of elevation and the known horizontal distance. | T4.O2 |
| O9 | understand | Interpret a heights-and-distances problem where the hypotenuse or base (not height) is the unknown quantity. | T5.O1 |
| O10 | apply | Calculate the length of a ladder (hypotenuse) or the base distance using sin and cot of the angle of elevation. | T5.O2 |
| O11 | understand | Interpret a problem where the observer's eye level adds an offset to the computed height, requiring decomposition of the total height. | T6.O1 |
| O12 | apply | Calculate the total height of an object by adding the observer's eye-level height to the height derived from the angle of elevation. | T6.O2 |
| O13 | create | Formulate a right-triangle equation from an unfamiliar real-world single-angle-of-elevation scenario. | T7.O1 |
| O14 | apply | Solve for the unknown height, distance or length in single-angle elevation word problems by selecting sin, cos or tan according to which two sides of the right triangle are involved. | T7.O2, T18.O1 |
| O15 | evaluate | Verify answers by checking that the computed side lengths satisfy the Pythagoras theorem or reproduce the given trigonometric ratio when substituted back into the original equation. | T18.O2 |
| O16 | understand | Explain the angle of depression as the angle formed by the line of sight with the horizontal when the viewed point is below the observer. | T8.O1 |
| O17 | analyze | Distinguish the angle of depression from the angle of elevation by comparing the direction of the line of sight relative to the horizontal. | T8.O2 |
| O18 | apply | Draw a labelled diagram showing the angle of depression and its alternate interior angle in a parallel-lines configuration. | T8.O3 |
| O19 | understand | Interpret a problem involving two angles of depression from the top of a tall structure to the top and bottom of a shorter building. | T9.O1 |
| O20 | apply | Calculate the height of a multi-storeyed building and the distance between two structures by setting up and solving two right-triangle equations. | T9.O2 |
| O21 | understand | Interpret a problem where two angles of depression from a bridge are used to find the total width of a river. | T10.O1 |
| O22 | apply | Calculate the width of a river by summing two horizontal distances derived from separate right triangles with different angles of depression. | T10.O2 |
| O23 | understand | Interpret a two-triangle problem where angles of elevation to the top of a building and the top of a flagstaff are given from the same point. | T11.O1 |
| O24 | apply | Calculate the length of a flagstaff and the horizontal distance to a building by solving two simultaneous right-triangle equations. | T11.O2 |
| O25 | understand | Interpret a problem where two different sun altitudes produce shadows of different lengths from the same tower. | T12.O1 |
| O26 | apply | Derive and solve a system of two tan-ratio equations to find the height of a tower from two shadow-length conditions. | T12.O2 |
| O27 | analyze | Classify a multi-angle heights-and-distances problem by the number of right triangles and unknowns involved, and determine the solution strategy (single triangle, two triangles with a shared base, cross-angle equating, combined elevation-depression, or a proportional time-speed ratio) before setting up equations. | T13.O1, T19.O2 |
| O28 | apply | Solve multi-angle elevation and combined elevation-depression problems by writing one right-triangle equation per angle and linking the equations through the side that is common to both triangles. | T13.O2, T19.O1 |
| O29 | evaluate | Verify computed answers by substituting the result back into both original trigonometric equations and confirming that the given angle values are reproduced exactly. | T19.O3 |
| O30 | understand | Explain how both an angle of elevation and an angle of depression can appear in the same heights-and-distances problem. | T14.O1 |
| O31 | apply | Construct a unified right-triangle diagram that correctly positions both angles for a combined elevation-depression scenario. | T14.O2 |
| O32 | create | Formulate the right-triangle setup for a lighthouse problem involving two ships observed at different angles of depression. | T16.O1 |
| O33 | apply | Calculate the distance between two ships observed from the top of a lighthouse using two angle-of-depression equations. | T16.O2 |
| O34 | understand | Interpret a problem where a moving car is observed at two successive angles of depression from the top of a tower. | T15.O1 |
| O35 | apply | Calculate the time for the car to reach the tower by combining the distance from two right-triangle equations with the speed ratio. | T15.O2 |
| O36 | remember | Recall the definitions of line of sight, angle of elevation, and angle of depression, and state the conditions (observer position and direction of viewing) that distinguish the two angle types. | T17.O1 |
| O37 | understand | Compare the angle of elevation with the angle of depression by the direction of the line of sight, the observer position, the alternate angle property and the trigonometric ratio typically used. | T17.O2 |
| O38 | understand | Explain how changing the angle of elevation or depression, while holding the known side fixed, produces non-linear changes in the computed height or distance. | T20.O1 |

Notes:
- Three pairs of old objectives that say the same thing are merged, and both old IDs are kept: T7.O2 with T18.O1, T13.O1 with T19.O2, and T13.O2 with T19.O1. No objective is newly authored.
- Exercise and topic pointers inside old wording are dropped from the student-facing text: "from Exercise 9.1 Q1–Q6" (T18.O1, T18.O2), "for Q7–Q15" (T19.O1–O3) and "as introduced in T1, T2, and T8" (T17.O1). T17.O2 loses its "first-introduced topic" dimension for the same reason.
- T20.O1 was about reading the output of a held tool. Its idea (how the computed height changes as the angle changes) is kept without the tool and anchored on the summary. Please check this wording.

# Appendix B · Held assets (not attached to the new plan; nothing deleted)

**4 old tools** (no tools in this chapter):
- T12 "Shadow & Sun Altitude Simulator" (T2D1)
- T13 "Two-Triangle Problem Solver" (T2D1)
- T15 "Moving Object Tracker (time-based problems)" (T2D1)
- T17 "Angle of Elevation vs Depression Explainer" (T2D1)

**7 old question videos** (no question videos for now):
- "Application Framework: Problem→Situation→Known→Unknown→Solve→Check for Exercise 9.1 Q1" (T7 VID1)
- "Multi-Angle Framework Walkthrough: Q7 Transmission Tower Using Seven-Stage Method" (T13 VID1)
- "Combined Elevation and Depression: Jaipur Haveli Scenario — Setting Up Both Triangles" (T14 VID1); its scenario is the twelfth question's numbers (7 m platform, 60° and 45°), so it would give that question away
- "Q15 Worked: Moving Car and Tower — Distance Ratio Cancels Tower Height" (T15 VID1)
- "Q13 Worked: Lighthouse and Two Ships — Why Subtract, Not Add" (T16 VID1)
- "Q1 and Q6 Fully Worked: Ratio Selection for Hypotenuse and Observer-Offset Problems" (T18 VID1)
- "Strategy Selection Walkthrough: Classifying Q7–Q15 Before Computing" (T19 VID1)

**6 old images that show an exercise question's set-up or answer** (question concepts carry only the new hint-free spec):
- "Brahmaputra Bridge: Transmission Tower on Building, Two Elevation Angles (Indian Scenario)" (T13 O1.E1): the seventh question's figure, with its answer
- "Combined Elevation and Depression: Observer on 7 m Platform, Both Angles from Same Point" (T14 O2.E1): the twelfth question, with its answer
- "Moving Car: Tower Observer with Two Successive Depression Angles 30° and 60°" (T15 O1.E1): the fifteenth question's set-up
- "Vizhinjam Lighthouse: Two Ships on Same Side, Depression Angles 30° and 45°" (T16 O1.E1): the thirteenth question, with its answer
- "Q1 and Q6 Reference Diagrams: Circus Rope (Hypotenuse) and Observer-Offset Building" (T18 O2.E1): two questions, with answers
- "Q9 and Q12 Reference Diagrams: Cross-Angle Pattern and Combined Elevation-Depression" (T19 O1.E1): two questions, with answers

**2 old media that show the held tool**:
- "Problem Explorer Walkthrough: Exploring All Three Configurations with Angle Variation" (T20 VID1): a screen capture of the tool
- "Problem Explorer Layout: Right Triangle on Grid, θ = 60°, d = 15 m, Config A" (T20 O1.E1): a tool screenshot. Its numbers match the first worked example (C5), so it could be re-homed there if a tool screenshot is acceptable.

Media identity: 25 attached + 19 held (4 tools, 7 question videos, 6 question images, 2 tool media) = 44 old media.

# Appendix C · Old topic → new concepts

| Old topic | New concepts |
|---|---|
| T1 Line of Sight: Definition and Geometric Representation | C2 (and the hook C1) |
| T2 Angle of Elevation: Definition, Diagram, and Setup | C3 |
| T3 Selecting the Correct Trigonometric Ratio | C4 (its depression prompt moves to C14) |
| T4 Finding Height Using a Single Angle of Elevation | C5 |
| T5 Finding Hypotenuse or Base Using sin and cos | C6 |
| T6 Height Problems with Observer Eye-Level Offset | C7 |
| T7 Real-World Single-Angle Elevation Problems | C8–C13 (its kite image goes to C4) |
| T8 Angle of Depression: Definition, Diagram, and Alternate Angles | C14 |
| T9 Two Angles of Depression: Two Structures | C15–C16 |
| T10 Two Angles of Depression from a Bridge | C17 |
| T11 Two Angles of Elevation from a Single Point | C18 |
| T12 Two Shadow Angles | C19 |
| T13 Multi-Angle Elevation Application Problems | C20–C24 |
| T14 Combined Elevation and Depression | C25 |
| T15 Moving Observer or Moving Object | C28 |
| T16 Lighthouses, Ships, and Distant Objects | C26–C27 |
| T17 Review: Core Concepts | C29 |
| T18 Practice: Single-Angle Elevation Word Problems | C8–C13 |
| T19 Practice: Multi-Angle and Combined Problems | C20–C28 |
| T20 Interactive: Heights and Distances Problem Explorer | C29 (objective only; its media are held) |

Every old topic's `recall_questions`, `summary`, `key_terms`, `concept_bullets` and `detailed_summary` carry into the new topic that holds its text. They are not shown here, to keep this file reviewable. The nothing-deleted check at build time compares them field by field.
