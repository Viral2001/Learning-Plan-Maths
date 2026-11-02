# Representative learning plan: Class 10, Circles (maths10_ch10)

A review copy of the restructured plan, down to concept level. Content is shown in full. Media are only named and never embedded.

Source: `learning_plan_std10_chap10_version1.json`. Shape follows the Class 9 circles plan and the Class 10 coordinate geometry plan.

## Read this first

**Standing decisions**
- No tools in this chapter. The five old `2d_tool` items are held (Appendix B).
- No videos for exercise questions. Each question concept gets one hint-free image spec and no video. The three old exercise videos are held (Appendix B).
- Examples keep the existing videos and images that match them. No new example media is planned.
- No grouping inside the question topics. Each textbook question is its own concept, in textbook order, named "<set name>, Q<n>". A question with separate lettered sub-parts is split: each sub-part is its own concept, named "<set name>, Q<n> (<roman>)", and keeps its parent question's objectives. Only the fill-in-the-blanks question of the first set has sub-parts, and they are independent, so none is kept whole for that reason. The (A)–(D) options of the multiple-choice questions are answer choices, not sub-parts, so they stay with their question.
- The textbook has two exercise sets and no starred or end-of-chapter set. Both are included, each with its own new name.
- The two theorems become try/prove pairs: TH1 (the tangent is perpendicular to the radius) and TH2 (the two tangents from an external point are equal).
- Topic flow follows the old plan: both exercise sets sit in the final practice module, as in the old plan, although the book prints the first set straight after the first theorem. The old plan's two Exercise 10.2 topics (computation, then proof) are merged into one question topic in textbook order, Q1 to Q13.

**What a concept entry shows**
- `kind`: try, prove, teach, enrich, hook, exercise or summary.
- `objectives`: objective IDs. Enrichment concepts have none.
- `media`: existing assets re-homed from the old plan, new asset specs, or none. Where the old title carries a book number (Theorem, Example, Exercise or Chapter), it is shown as found and marked for renaming at build.
- `[block_kind]` tags are review labels only. They never reach the student.

**Text cleanup applied to everything below**
- "Fig. 10.x", "see Fig. 10.x" and "In Fig. 10.x" are removed or turned into "the figure". The figure is carried by the image.
- "Section 10.x" and "the previous section" become a plain phrase.
- "Activity 1 :", "Activity 2 :" and "Activity 3 :" lose their numbers and become "Activity :". "while doing Activity 1" becomes "while doing the first activity".
- "Theorem 10.1" becomes "the tangent–radius theorem" or a plain statement of it; "Theorem 10.2" becomes "the equal-tangents theorem" or a plain statement of it. "(as shown in Theorem A1.7.)" becomes a plain statement of the fact it points to.
- "Example n :" and "Exercise 10.x" labels are removed. The stem "In Q.1 to 3, choose the correct option and give justification." becomes "Choose the correct option and give justification." on each of those three questions.
- Book references stay only in metadata (`ncert_refs`), which is not shown here.

**Marked in the text**
- `[authored]` marks text that is not in the old plan or the book. These are predictions and the answer to the one open "(Why?)" prompt. No objective wording is new; the carried objectives are only reworded to drop book numbers.
- Question solutions (`steps` and `answer`) are not in the old plan. They are marked *to author* and nothing is invented here.

## Plan at a glance

| Module | Topic | Concepts |
|---|---|---|
| M1 Tangent to a circle | T1 A Line and a Circle (hook) | C1 |
|  | T2 Three Ways a Line Can Meet a Circle | C2 |
|  | T3 A Tangent as the Limit of a Secant | C3–C5 |
|  | T4 The Tangent and the Radius | C6–C7 |
| M2 Tangents from an external point | T5 How Many Tangents from a Point? | C8 |
|  | T6 Two Tangents from an External Point | C9–C10 |
|  | T7 Examples: Using the Tangent Properties | C11–C14 |
| M3 Practice and wrap-up | T8 Questions: Tangents and Secants | C15–C21 |
|  | T9 Questions: Tangents from a Point | C22–C34 |
|  | T10 Chapter Summary | C35 |

Totals: 35 concepts and 15 objectives. 20 question concepts (7 + 13) need a new image, 4 of them from the book's own figure. 0 new videos. Media: 18 attached (9 videos, 9 images) and 11 held (5 tools, 3 exercise videos, 3 exercise reference images), 29 in all, which is the old total.

---

# M1 · Tangent to a circle

## T1 · A Line and a Circle (hook)

### C1 · A circle and a line in the same plane
`kind: hook` · `is_enrichment: true` · `objectives: none`
Media: new image spec "A circle and a straight line" — Three everyday pictures. A bicycle wheel rests on a straight road, a rope runs over a round pulley wheel above a well, and a straight pencil lies across a round plate. Each picture has a faint circle and a straight line drawn over it.

[textbook_text]
> You have studied in Class IX that a circle is a collection of all points in a plane which are at a constant distance (radius) from a fixed point (centre). You have also studied various terms related to a circle like chord, segment, sector, arc etc. Let us now examine the different situations that can arise when a circle and a line are given in a plane.

*(Cleanup: the section heading "10.1 Introduction" is dropped. No words dropped.)*

---

## T2 · Three Ways a Line Can Meet a Circle

### C2 · Non-intersecting line, secant and tangent
`kind: teach` · `objectives: O1, O2`
Media: existing video "Non-intersecting, secant, tangent — 90-second overview" (old T1 VID1); existing image "Three positions of a line with respect to a circle" (old T1 O1.E1)

[textbook_text]
> So, let us consider a circle and a line PQ. There can be three possibilities given in the figure below:
>
> In (i), the line PQ and the circle have no common point. In this case, PQ is called a non-intersecting line with respect to the circle. In (ii), there are two common points A and B that the line PQ and the circle have. In this case, we call the line PQ a secant of the circle. In (iii), there is only one point A which is common to the line PQ and the circle. In this case, the line is called a tangent to the circle.
>
> You might have seen a pulley fitted over a well which is used in taking out water from the well. Here the rope on both sides of the pulley, if considered as a ray, is like a tangent to the circle representing the pulley.
>
> Is there any position of the line with respect to the circle other than the types given above? You can see that there cannot be any other type of position of the line with respect to the circle. In this chapter, we will study about the existence of the tangents to a circle and also study some of their properties.

*(Cleanup: "Fig. 10.1" becomes "the figure", and "In Fig. 10.1 (i)" becomes "In (i)". "Look at Fig. 10.2." is dropped: the book's pulley figure has no asset in the old plan, so no image is attached for it.)*

---

## T3 · A Tangent as the Limit of a Secant

### C3 · Rotating a wire about a point of the circle
`kind: teach` · `objectives: O3`
Media: existing video "Activities 1 and 2 — animated walkthrough" (old T2 VID1); existing image "Activity 1 and Activity 2 composite figures" (old T2 O1.E1). Both cover this concept and the next one (the book's two activities), so the fit is loose, please check. The titles carry activity numbers, which the leak check does not catch; please rename at build.

[textbook_text]
> Earlier, you have seen that a tangent to a circle is a line that intersects the circle at only one point.
>
> To understand the existence of the tangent to a circle at a point, let us perform the following activities:
>
> Activity : Take a circular wire and attach a straight wire AB at a point P of the circular wire so that it can rotate about the point P in a plane. Put the system on a table and gently rotate the wire AB about the point P to get different positions of the straight wire.
>
> In various positions, the wire intersects the circular wire at P and at another point Q₁ or Q₂ or Q₃, etc. In one position, you will see that it will intersect the circle at the point P only (see position A′B′ of AB). This shows that a tangent exists at the point P of the circle. On rotating further, you can observe that in all other positions of AB, it will intersect the circle at P and at another point, say R₁ or R₂ or R₃, etc. So, you can observe that there is only one tangent at a point of the circle.
>
> While doing activity above, you must have observed that as the position AB moves towards the position A′B′, the common point, say Q₁, of the line AB and the circle gradually comes nearer and nearer to the common point P. Ultimately, it coincides with the point P in the position A′B′ of AB. Again note, what happens if 'AB' is rotated rightwards about P? The common point R₃ gradually comes nearer and nearer to P and ultimately coincides with P. So, what we see is:
>
> The tangent to a circle is a special case of the secant, when the two end points of its corresponding chord coincide.

*(Cleanup: "In the previous section" becomes "Earlier", the asterisk on "tangent*" moves with its footnote to C5, "[see Fig. 10.3(i)]" is dropped, and "Activity 1 :" loses its number.)*

### C4 · Sliding a secant parallel to itself
`kind: teach` · `objectives: O3`
Media: new image spec "Sliding a secant parallel to itself" — A circle with a secant PQ drawn through it. Several lines parallel to PQ are drawn on both sides of it, each cutting a shorter chord than the one before. The two outermost parallel lines touch the circle at one point each, labelled P′Q′ and P″Q″ at their points of contact, one on each side of the circle.

[textbook_text]
> Activity : On a paper, draw a circle and a secant PQ of the circle. Draw various lines parallel to the secant on both sides of it. You will find that after some steps, the length of the chord cut by the lines will gradually decrease, i.e., the two points of intersection of the line and the circle are coming closer and closer. In one case, it becomes zero on one side of the secant and in another case, it becomes zero on the other side of the secant. See the positions P′Q′ and P″Q″ of the secant in the figure. These are the tangents to the circle parallel to the given secant PQ. This also helps you to see that there cannot be more than two tangents parallel to a given secant.
>
> This activity also establishes, what you must have observed, while doing the first activity, namely, a tangent is the secant when both of the end points of the corresponding chord coincide.
>
> The common point of the tangent and the circle is called the point of contact [the point A in the first figure (iii)] and the tangent is said to touch the circle at the common point.

*(Cleanup: "[see Fig. 10.3(ii)]" is dropped, "in Fig. 10.3 (ii)" becomes "in the figure", "Activity 2 :" loses its number, "while doing Activity 1" becomes "while doing the first activity", and "[the point A in Fig. 10.1 (iii)]" becomes "[the point A in the first figure (iii)]".)*

### C5 · More to explore: where the word "tangent" comes from
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "A line that just touches a circle" — A round coin with a straight ruler laid so that it touches the edge of the coin at one single point. The point of touching is marked with a dot, and a label beside the picture reads the Latin word tangere which means to touch.

[textbook_text · footnote]
> The word 'tangent' comes from the Latin word 'tangere', which means to touch and was introduced by the Danish mathematician Thomas Fineke in 1583.

---

## T4 · The Tangent and the Radius

### C6 · The tangent–radius theorem: try it first
`kind: try` · `objectives: O4`
Media: new image spec "A circle, a line touching it, and Q" — A circle with centre O and a straight line XY touching the circle at a point P. The radius OP is drawn. Another point Q is marked on the line XY away from P, and the segment OQ is drawn as a dashed line. No lengths or angle marks are shown.
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[textbook_text]
> Now look around you. Have you seen a bicycle or a cart moving? Look at its wheels. All the spokes of a wheel are along its radii. Now note the position of the wheel with respect to its movement on the ground. Do you see any tangent anywhere? In fact, the wheel moves along a line which is a tangent to the circle representing the wheel. Also, notice that in all positions, the radius through the point of contact with the ground appears to be at right angles to the tangent. We shall now prove this property of the tangent.

[theorem_statement] *(the book's own words)*
> The tangent at any point of a circle is perpendicular to the radius through the point of contact.

[predict] `[authored]`
> Draw a circle with centre O and a tangent touching it at P. Pick any other point Q on the tangent. Before any proof, guess: is OQ shorter than, equal to or longer than the radius OP? Commit to an answer. The next concept uses exactly this comparison to show why the radius OP must meet the tangent at a right angle.

*(Cleanup: "(See Fig. 10.4)" and "(see Fig. 10.4)" are dropped. The book's wheel figure has no asset in the old plan. No other words dropped.)*

### C7 · Why the tangent is perpendicular to the radius
`kind: prove` · `objectives: O4`
Media: existing video "Theorem 10.1 — narrated proof animation" (old T3 VID1) [title carries a book number, renamed at build]; existing image "Theorem 10.1 figure with perpendicularity marked" (old T3 O1.E1) [title carries a book number, renamed at build]

[textbook_text]
> Proof : We are given a circle with centre O and a tangent XY to the circle at a point P. We need to prove that OP is perpendicular to XY.
>
> Take a point Q on XY other than P and join OQ.
>
> The point Q must lie outside the circle. (Why? Note that if Q lies inside the circle, XY will become a secant and not a tangent to the circle). Therefore, OQ is longer than the radius OP of the circle. That is,
> OQ > OP.
>
> Since this happens for every point on the line XY except the point P, OP is the shortest of all the distances of the point O to the points of XY. So OP is perpendicular to XY (as you know, the shortest distance from a point to a line is the perpendicular one).

[textbook_text · remarks]
> 1. By the theorem above, we can also conclude that at any point on a circle there can be one and only one tangent.
> 2. The line containing the radius through the point of contact is also sometimes called the 'normal' to the circle at the point.

*(Cleanup: "(see Fig. 10.5)" is dropped. "(as shown in Theorem A1.7.)" points to the book's appendix; it becomes "(as you know, the shortest distance from a point to a line is the perpendicular one)", which states the fact the appendix theorem gives. "By theorem above" becomes "By the theorem above". The book answers its own "(Why?)" in the next sentence, so no enrichment is needed.)*

---

# M2 · Tangents from an external point

## T5 · How Many Tangents from a Point?

### C8 · No tangent, one tangent or two
`kind: teach` · `objectives: O5`
Media: existing video "Activity 3 — three cases animation" (old T4 VID1); existing image "Three cases of tangents from a point" (old T4 O1.E1). The video title carries an activity number, which the leak check does not catch; please rename at build.

[textbook_text]
> To get an idea of the number of tangents from a point on a circle, let us perform the following activity:
>
> Activity : Draw a circle on a paper. Take a point P inside it. Can you draw a tangent to the circle through this point? You will find that all the lines through this point intersect the circle in two points. So, it is not possible to draw any tangent to a circle through a point inside it.
>
> Next take a point P on the circle and draw tangents through this point. You have already observed that there is only one tangent to the circle at such a point.
>
> Finally, take a point P outside the circle and try to draw tangents to the circle from this point. What do you observe? You will find that you can draw exactly two tangents to the circle through this point.
>
> We can summarise these facts as follows:
> Case 1 : There is no tangent to a circle passing through a point lying inside the circle.
> Case 2 : There is one and only one tangent to a circle passing through a point lying on the circle.
> Case 3 : There are exactly two tangents to a circle through a point lying outside the circle.
>
> In (iii), T₁ and T₂ are the points of contact of the tangents PT₁ and PT₂ respectively.
>
> The length of the segment of the tangent from the external point P and the point of contact with the circle is called the length of the tangent from the point P to the circle.

*(Cleanup: the section heading "10.3 Number of Tangents from a Point on a Circle" is dropped, "Activity 3 :" loses its number, the three "[see Fig. 10.6 (i)/(ii)/(iii)]" pointers are dropped, and "In Fig. 10.6 (iii)" becomes "In (iii)". The case labels "Case 1 :" to "Case 3 :" stay, because they belong to the content.)*

---

## T6 · Two Tangents from an External Point

### C9 · The equal-tangents theorem: try it first
`kind: try` · `objectives: O6`
Media: new image spec "Two lines from a point outside" — A circle with centre O and a point P outside it. Two tangent lines from P touch the circle at T₁ and T₂. The segments PT₁ and PT₂ are drawn in colour, and the segments OP, OT₁ and OT₂ are drawn as dashed lines. No lengths or angle marks are shown.
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[textbook_text]
> Note that in the figure of a point outside the circle, PT₁ and PT₂ are the lengths of the tangents from P to the circle. The lengths PT₁ and PT₂ have a common property. Can you find this? Measure PT₁ and PT₂. Are these equal? In fact, this is always so. Let us give a proof of this fact in the following theorem.

[theorem_statement] *(the book's own words)*
> The lengths of tangents drawn from an external point to a circle are equal.

[predict] `[authored]`
> Join the external point P to the centre O, and join O to the two points of contact. Before any proof, guess: which two triangles would you compare to show that the two tangents are equal, and which fact about a tangent and a radius gives you a right angle in each? Commit to an answer. The next concept settles it.

*(Cleanup: "in Fig. 10.6 (iii)" becomes "in the figure of a point outside the circle". No words dropped.)*

### C10 · Why the two tangents are equal
`kind: prove` · `objectives: O6`
Media: existing video "Theorem 10.2 — narrated RHS proof" (old T5 VID1) [title carries a book number, renamed at build]; existing image "Theorem 10.2 figure with congruent right triangles" (old T5 O1.E1) [title carries a book number, renamed at build]

[textbook_text]
> Proof : We are given a circle with centre O, a point P lying outside the circle and two tangents PQ, PR on the circle from P. We are required to prove that PQ = PR.
>
> For this, we join OP, OQ and OR. Then ∠OQP and ∠ORP are right angles, because these are angles between the radii and tangents, and according to the tangent–radius theorem they are right angles. Now in right triangles OQP and ORP,
> OQ = OR (Radii of the same circle)
> OP = OP (Common)
> Therefore, ∆OQP ≅ ∆ORP (RHS)
> This gives PQ = PR (CPCT)

[textbook_text · remarks]
> 1. The theorem can also be proved by using the Pythagoras Theorem as follows:
> PQ² = OP² − OQ² = OP² − OR² = PR² (As OQ = OR)
> which gives PQ = PR.
> 2. Note also that ∠OPQ = ∠OPR. Therefore, OP is the angle bisector of ∠QPR, i.e., the centre lies on the bisector of the angle between the two tangents.

*(Cleanup: "(see Fig. 10.7)" is dropped, and "according to Theorem 10.1" becomes "according to the tangent–radius theorem". The closing line "Let us take some examples." moves to the first example, C11.)*

---

## T7 · Examples: Using the Tangent Properties

### C11 · A chord of the larger circle that touches the smaller one
`kind: exercise (worked example)` · `objectives: O7`
Media: existing video "Example 1 walkthrough — concentric rotis" (old T6 VID1) [title carries a book number, renamed at build]; existing image "Example 1 figure — concentric circles with tangent chord" (old T6 O1.E1) [title carries a book number, renamed at build]

[textbook_text · lead-in]
> Let us take some examples.

[question]
> Prove that in two concentric circles, the chord of the larger circle, which touches the smaller circle, is bisected at the point of contact.

[worked solution, from source]
> We are given two concentric circles C₁ and C₂ with centre O and a chord AB of the larger circle C₁ which touches the smaller circle C₂ at the point P. We need to prove that AP = BP.
>
> Let us join OP. Then, AB is a tangent to C₂ at P and OP is its radius. Therefore, by the tangent–radius theorem,
> OP ⊥ AB
>
> Now AB is a chord of the circle C₁ and OP ⊥ AB. Therefore, OP is the bisector of the chord AB, as the perpendicular from the centre bisects the chord,
> i.e., AP = BP

*(Cleanup: "Example 1 :" and "Solution :" labels are dropped, "(see Fig. 10.8)" is dropped, and "by Theorem 10.1" becomes "by the tangent–radius theorem".)*

### C12 · The angle between two tangents and the angle at the contact point
`kind: exercise (worked example)` · `objectives: O8`
Media: existing video "Example 2 proof — animated angle chase" (old T7 VID1) [title carries a book number, renamed at build]; existing image "Example 2 figure — angle relation ∠PTQ = 2 ∠OPQ" (old T7 O1.E1) [title carries a book number, renamed at build]

[question]
> Two tangents TP and TQ are drawn to a circle with centre O from an external point T. Prove that ∠PTQ = 2 ∠OPQ.

[worked solution, from source]
> We are given a circle with centre O, an external point T and two tangents TP and TQ to the circle, where P, Q are the points of contact. We need to prove that
> ∠PTQ = 2 ∠OPQ
> Let ∠PTQ = θ
> Now, by the equal-tangents theorem, TP = TQ. So, TPQ is an isosceles triangle.
> Therefore, ∠TPQ = ∠TQP = ½(180° − θ) = 90° − ½θ
> Also, by the tangent–radius theorem, ∠OPT = 90°
> So, ∠OPQ = ∠OPT − ∠TPQ = 90° − (90° − ½θ) = ½θ = ½ ∠PTQ
> This gives ∠PTQ = 2 ∠OPQ

*(Cleanup: "(see Fig. 10.9)" is dropped, "by Theorem 10.2" becomes "by the equal-tangents theorem", and "by Theorem 10.1" becomes "by the tangent–radius theorem".)*

### C13 · How long is the tangent from where two tangents meet?
`kind: exercise (worked example)` · `objectives: O9`
Media: existing video "Example 3 walkthrough — similarity and Pythagoras" (old T8 VID1) [title carries a book number, renamed at build]; existing image "Example 3 figure — chord, tangents, and intersection T" (old T8 O1.E1) [title carries a book number, renamed at build]

[question]
> PQ is a chord of length 8 cm of a circle of radius 5 cm. The tangents at P and Q intersect at a point T. Find the length TP.

[worked solution, from source]
> Join OT. Let it intersect PQ at the point R. Then ∆TPQ is isosceles and TO is the angle bisector of ∠PTQ. So, OT ⊥ PQ and therefore, OT bisects PQ which gives PR = RQ = 4 cm.
> Also, OR = √(OP² − PR²) = √(5² − 4²) cm = 3 cm.
> Now, ∠TPR + ∠RPO = 90° = ∠TPR + ∠PTR (Why?)
> So, ∠RPO = ∠PTR
> Therefore, right triangle TRP is similar to the right triangle PRO by AA similarity.
> This gives TP / PO = RP / RO, i.e., TP / 5 = 4 / 3 or TP = 20/3 cm.
>
> **Note.** TP can also be found by using the Pythagoras Theorem, as follows:
> Let TP = x and TR = y. Then
> x² = y² + 16 (Taking right ∆PRT)    (1)
> x² + 5² = (y + 3)² (Taking right ∆OPT)    (2)
> Subtracting (1) from (2), we get
> 25 = 6y − 7 or y = 32/6 = 16/3
> Therefore, x² = (16/3)² + 16 = 16(16/9 + 1) = 16(16 + 9)/9 = 16 · 25/9    [From (1)]
> or x = 20/3

*(Cleanup: "(see Fig. 10.10)" is dropped from the question. The "(Why?)" stays in the working; its answer is in C14.)*

### C14 · More to explore: the book's "Why?" prompt
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Angles at P beside the tangent" — A circle with centre O of radius 5 cm and a chord PQ of length 8 cm. The tangents at P and Q meet at a point T, and OT is drawn crossing PQ at R. The right triangles TRP and PRO are shaded. The angles TPR, RPO and PTR are marked with arcs.

[enrichment] `[authored answer]`
> **Q.** In the tangent-length example, why is ∠TPR + ∠RPO = 90° = ∠TPR + ∠PTR?
> **A.** ∠TPR + ∠RPO is the whole angle ∠TPO between the tangent TP and the radius OP, and a tangent is perpendicular to the radius at the point of contact, so it is 90°. In the right triangle TRP the right angle is at R, so the other two angles, ∠TPR and ∠PTR, add up to 180° − 90° = 90°.

---

# M3 · Practice and wrap-up

## T8 · Questions: Tangents and Secants

Objectives for this set: O10 (apply) answer basic questions on the number of tangents a circle has, tangent and secant definitions, the parallel-tangent count, and a tangent length found from tangent–radius perpendicularity with Pythagoras.

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, showing the statement (for a split question, the stem and that one sub-part only), no working and no answer. None of these questions comes with its own book figure, and the book prints no hint for any of them. There is no video. Solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for all 7.
The questions are in textbook order. The four blanks of the second question are independent, so each is its own concept.

### C15 · Tangents and Secants, Q1
`objectives: O10` · Media: new image spec (statement only)
> How many tangents can a circle have?

### C16 · Tangents and Secants, Q2 (i)
`objectives: O10` · Media: new image spec (statement and this sub-part only)
> Fill in the blanks :
> (i) A tangent to a circle intersects it in ______ point(s).

### C17 · Tangents and Secants, Q2 (ii)
`objectives: O10` · Media: new image spec (statement and this sub-part only)
> Fill in the blanks :
> (ii) A line intersecting a circle in two points is called a ______.

### C18 · Tangents and Secants, Q2 (iii)
`objectives: O10` · Media: new image spec (statement and this sub-part only)
> Fill in the blanks :
> (iii) A circle can have ______ parallel tangents at the most.

### C19 · Tangents and Secants, Q2 (iv)
`objectives: O10` · Media: new image spec (statement and this sub-part only)
> Fill in the blanks :
> (iv) The common point of a tangent to a circle and the circle is called ______.

### C20 · Tangents and Secants, Q3
`objectives: O10` · Media: new image spec (statement only)
> A tangent PQ at a point P of a circle of radius 5 cm meets a line through the centre O at a point Q so that OQ = 12 cm. Length PQ is :
> (A) 12 cm    (B) 13 cm    (C) 8.5 cm    (D) √119 cm.

### C21 · Tangents and Secants, Q4
`objectives: O10` · Media: new image spec (statement only)
> Draw a circle and two lines parallel to a given line such that one is a tangent and the other, a secant to the circle.

---

## T9 · Questions: Tangents from a Point

Objectives for this set: O11 (apply) compute tangent lengths, radii, angles and triangle sides from tangent–radius perpendicularity, equal tangents, Pythagoras and the angle sum of a quadrilateral; O12 (analyze) choose between Pythagoras, the quadrilateral angle sum and a system of equal tangent lengths for each computation; O13 (apply) prove relations about tangents from perpendicularity, equal tangents and congruence; O14 (evaluate) justify each proof step by the property or congruence criterion it uses.

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, statement only, no working and no answer. Four questions (Q2, Q8, Q9 and Q12) come with their own book figure, and their image is that figure only. The book prints no hint for any of them. There is no video. Solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for all 13.
The questions are in textbook order, Q1 to Q13. None has lettered sub-parts, so each is one concept. Computation questions (Q1, Q2, Q3, Q6, Q7, Q12) carry O11 and O12; proof questions (Q4, Q5, Q8, Q9, Q10, Q11, Q13) carry O13 and O14, as in the old plan's two topics.

### C22 · Tangents from a Point, Q1
`objectives: O11, O12` · Media: new image spec (statement only)
> Choose the correct option and give justification.
> From a point Q, the length of the tangent to a circle is 24 cm and the distance of Q from the centre is 25 cm. The radius of the circle is
> (A) 7 cm    (B) 12 cm    (C) 15 cm    (D) 24.5 cm

### C23 · Tangents from a Point, Q2
`objectives: O11, O12` · Media: new image spec (**the book's own figure only**, as it supplies the two tangents and the angle at the centre)
> Choose the correct option and give justification.
> In the figure, if TP and TQ are the two tangents to a circle with centre O so that ∠POQ = 110°, then ∠PTQ is equal to
> (A) 60°    (B) 70°    (C) 80°    (D) 90°

### C24 · Tangents from a Point, Q3
`objectives: O11, O12` · Media: new image spec (statement only)
> Choose the correct option and give justification.
> If tangents PA and PB from a point P to a circle with centre O are inclined to each other at angle of 80°, then ∠POA is equal to
> (A) 50°    (B) 60°    (C) 70°    (D) 80°

### C25 · Tangents from a Point, Q4
`objectives: O13, O14` · Media: new image spec (statement only)
> Prove that the tangents drawn at the ends of a diameter of a circle are parallel.

### C26 · Tangents from a Point, Q5
`objectives: O13, O14` · Media: new image spec (statement only)
> Prove that the perpendicular at the point of contact to the tangent to a circle passes through the centre.

### C27 · Tangents from a Point, Q6
`objectives: O11, O12` · Media: new image spec (statement only)
> The length of a tangent from a point A at distance 5 cm from the centre of the circle is 4 cm. Find the radius of the circle.

### C28 · Tangents from a Point, Q7
`objectives: O11, O12` · Media: new image spec (statement only)
> Two concentric circles are of radii 5 cm and 3 cm. Find the length of the chord of the larger circle which touches the smaller circle.

### C29 · Tangents from a Point, Q8
`objectives: O13, O14` · Media: new image spec (**the book's own figure only**, as it supplies the quadrilateral around the circle)
> A quadrilateral ABCD is drawn to circumscribe a circle (see the figure). Prove that
> AB + CD = AD + BC

### C30 · Tangents from a Point, Q9
`objectives: O13, O14` · Media: new image spec (**the book's own figure only**, as it supplies the two parallel tangents and the third tangent)
> In the figure, XY and X′Y′ are two parallel tangents to a circle with centre O and another tangent AB with point of contact C intersecting XY at A and X′Y′ at B. Prove that ∠AOB = 90°.

### C31 · Tangents from a Point, Q10
`objectives: O13, O14` · Media: new image spec (statement only)
> Prove that the angle between the two tangents drawn from an external point to a circle is supplementary to the angle subtended by the line-segment joining the points of contact at the centre.

### C32 · Tangents from a Point, Q11
`objectives: O13, O14` · Media: new image spec (statement only)
> Prove that the parallelogram circumscribing a circle is a rhombus.

### C33 · Tangents from a Point, Q12
`objectives: O11, O12` · Media: new image spec (**the book's own figure only**, as it supplies the triangle, the circle and the point of contact D)
> A triangle ABC is drawn to circumscribe a circle of radius 4 cm such that the segments BD and DC into which BC is divided by the point of contact D are of lengths 8 cm and 6 cm respectively (see the figure). Find the sides AB and AC.

### C34 · Tangents from a Point, Q13
`objectives: O13, O14` · Media: new image spec (statement only)
> Prove that opposite sides of a quadrilateral circumscribing a circle subtend supplementary angles at the centre of the circle.

---

## T10 · Chapter Summary

### C35 · Chapter summary
`kind: summary` · `objectives: O15`
Media: existing video "Chapter 10 — 90-second recap" (old T12 VID1) [title carries a book number, renamed at build]; existing image "Chapter 10 summary infographic" (old T12 O1.E1) [title carries a book number, renamed at build]

[summary_points]
> In this chapter, you have studied the following points :
> 1. The meaning of a tangent to a circle.
> 2. The tangent to a circle is perpendicular to the radius through the point of contact.
> 3. The lengths of the two tangents from an external point to a circle are equal.

*(Cleanup: the section heading "10.4 Summary" is dropped. The infographic's own fields name the two theorems by number; its title is renamed at build, and its caption is left for the media pass.)*

---

# Appendix A · Objectives

Format: ID · bloom level · wording · old objective(s) it carries. No objective is new. Wording changes only remove book numbers (Theorem, Exercise, Activity) or the question lists that pointed to them.

| ID | Bloom | Objective | Old ID |
|---|---|---|---|
| O1 | understand | Represent the three possible positions of a line relative to a circle — non-intersecting, secant, and tangent — by their number of common points. | T1.O1 |
| O2 | analyze | Classify the position of a given line with respect to a circle by counting the common points it shares with the circle. | T1.O2 |
| O3 | analyze | Determine, through the rotating-wire and parallel-secant explorations, that a tangent is a secant whose two intersection points coincide. | T2.O1 |
| O4 | evaluate | Prove that the tangent at any point of a circle is perpendicular to the radius through the point of contact, using the shortest-distance argument from the centre to the tangent line. | T3.O1 |
| O5 | analyze | Determine the number of tangents that can be drawn from a point to a circle (0, 1, or 2) and justify each case by the point's position relative to the circle. | T4.O1 |
| O6 | evaluate | Prove that the two tangents drawn from an external point to a circle are equal in length, using RHS congruence of the right triangles formed with the radii at the points of contact. | T5.O1 |
| O7 | apply | Solve the concentric-circle problem by proving that a chord of the larger circle which touches the smaller circle is bisected at the point of contact. | T6.O1 |
| O8 | apply | Compute angle relations between two tangents from an external point and the radii at the points of contact by combining the equal-tangents theorem with isosceles-triangle angle reasoning. | T7.O1 |
| O9 | apply | Solve for the tangent length TP from an external point T by combining similar triangles, the tangent–radius theorem, and the Pythagoras theorem in a chord-tangent configuration. | T8.O1 |
| O10 | apply | Answer basic questions on the number of tangents a circle has, tangent and secant definitions, the parallel-tangent count, and a tangent length found from tangent–radius perpendicularity with Pythagoras. | T9.O1 |
| O11 | apply | Compute tangent lengths, radii, angles and triangle sides using the tangent–radius theorem, the equal-tangents theorem, Pythagoras, and the quadrilateral-angle-sum technique. | T10.O1 |
| O12 | analyze | Determine whether Pythagoras in a right triangle, the quadrilateral-angle-sum trick, or a system built from equal external-tangent lengths best suits each computation on tangents. | T10.O2 |
| O13 | apply | Solve proof problems on tangents using tangent–radius perpendicularity, equal tangent lengths from an external point, and triangle-congruence reasoning. | T11.O1 |
| O14 | evaluate | Justify each proof step by citing the tangent–radius theorem or the equal-tangents theorem and the relevant congruence criterion (RHS / SAS / ASA) or quadrilateral-angle-sum identity. | T11.O2 |
| O15 | understand | Explain the three foundational tangent facts established in this chapter: a tangent meets a circle at exactly one point, is perpendicular to the radius at the point of contact, and has equal length to its partner from a common external point. | T12.O1 |

Notes:
- The try concepts (C6, C9) share their theorem's objective (O4, O6) with the prove concept that follows, so no new "state and predict" objective is authored. If the Class 10 pattern of a separate try objective is wanted, two new ones would take O16 and O17.
- Wording changes: T2.O1 drops "(Activity 1)" and "(Activity 2)"; T7.O1, T8.O1, T11.O2 and T12.O1 replace "Theorem 10.1" and "Theorem 10.2" with the theorem names or drop them; T9.O1, T10.O1 and T11.O1 drop "Exercise 10.1", "Exercise 10.2" and their question lists; T10.O2 drops "Exercise 10.2".
- Every old objective is carried. Enrichment concepts (C1, C5, C14) carry no objective.

# Appendix B · Held assets (not attached to the new plan; nothing deleted)

**Five old tools** (no tools in this chapter):
- T1 "Line & Circle Position Explorer" (T2D1)
- T4 "Number of Tangents from a Point" (T2D1)
- T5 "Circumscribed Polygon Tangent Property" (T2D1)
- T6 "Chord + External Tangent Intersection" (T2D1)
- T7 "Angle Relationships in Tangent Configurations" (T2D1)

**Three old exercise videos** (no question videos for now):
- T9 "Exercise 10.1 Q3 — worked solution" (VID1)
- T10 "Exercise 10.2 Q12 — triangle circumscribing a circle" (VID1)
- T11 "Exercise 10.2 Q8 — Pitot theorem walkthrough" (VID1)

**Three old exercise reference images** (each question concept carries exactly one hint-free image, and these mark the right angle at the point of contact, the equal-tangent ticks or the unknown being asked for, which are hints):
- T9 "Exercise 10.1 Q3 reference figure" (O1.E1). Marks the right angle at P and highlights PQ.
- T10 "Reference figures for Ex 10.2 Q2 and Q12" (O1.E1). Two panels; could serve as the source for the figure-question cards of Q2 and Q12 once the marks are removed.
- T11 "Reference figures for Ex 10.2 Q8 and Q9" (O1.E1). Two panels with equal-tangent tick marks; could serve as the source for the figure-question cards of Q8 and Q9 once the marks are removed.

Identity: 18 attached (9 videos, 9 images) + 11 held (5 tools, 3 videos, 3 images) = 29, the old media total. The old plan has no image records outside its media lists.

# Appendix C · Carried-over fields

Every old topic's `recall_questions`, `summary`, `key_terms`, `concept_bullets`, `detailed_summary`, `important_points` and `modified_chunk` carry into the new topic that holds its text. They are not shown here, to keep this file reviewable. The nothing-deleted check at build time compares them field by field.

Where each old topic's text and fields land:

| Old topic | New concepts |
|---|---|
| T1 Three positions of a line | C2, C1 (opening paragraph) |
| T2 Tangent as a limiting secant | C3, C4, C5 (footnote), C6 (wheel paragraph) |
| T3 First tangent theorem | C7, C6 (statement) |
| T4 Number of tangents from a point | C8, C9 (closing paragraph) |
| T5 Second tangent theorem | C10, C9 (statement), C11 (lead-in line) |
| T6 Concentric circles example | C11 |
| T7 Angle relation example | C12 |
| T8 Tangent length example | C13, C14 (the "Why?" answer) |
| T9 First exercise set | C15–C21 |
| T10 Second exercise set, computation | C22–C24, C27, C28, C33 |
| T11 Second exercise set, proofs | C25, C26, C29–C32, C34 |
| T12 Summary | C35 |
