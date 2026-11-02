# Representative learning plan: Class 10, Triangles (maths10_ch6)

A review copy of the restructured plan, down to concept level. Content is shown in full. Media are only named and never embedded.

Source: `learning_plan_std10_chap6_version1.json` and the book chapter (2026-27 reprint). Shape follows the Class 9 circles plan.

## Read this first

**Standing decisions**
- No tools in this chapter. The eight old `2d_tool` items are held (Appendix B).
- No videos for exercise questions. Each question concept gets one hint-free image spec and no video. The three old exercise videos are held (Appendix B).
- The three old exercise-figure images are held too (Appendix B). Each question concept already gets its own new image spec, and these images name book figure numbers and in one case show more than the question gives. They stay as the source for the new "book's own figure" specs.
- Examples keep the existing videos and images that match them. No new example media is planned.
- Each theorem is a `try` concept (statement and prediction) followed by a `prove` concept. Five theorems: TH1 basic proportionality, TH2 its converse, TH3 AAA, TH4 SSS, TH5 SAS.
- The question order inside a Questions topic is the book order. Independent sub-parts (i), (ii), (iii) are separate concepts.

**What a concept entry shows**
- `kind`: try, prove, teach, enrich, hook, exercise or summary.
- `objectives`: objective IDs. Enrichment concepts have none.
- `media`: existing assets re-homed from the old plan, new asset specs, or none.
- `[block_kind]` tags are review labels only. They never reach the student.

**Text cleanup applied to everything below**
- "Fig. 6.x" and "see Fig. 6.x" are removed or become "the figure". The figure is carried by the image.
- "Theorem 6.x" becomes the theorem's name (the basic proportionality theorem, its converse, the AAA, SSS or SAS criterion).
- "Activity n", "Example n:", "Exercise 6.x" and "Section 6.x" labels are removed.
- Pointers to other chapters, Appendix 1 and Exercise 6.3 Q15 become plain phrases.
- Book references stay only in metadata (`ncert_refs`), which is not shown here.

**Marked in the text**
- `[authored]` marks text that is not in the old plan or the book. These are predictions and answers to "(Why?)" and "(How?)" prompts.
- Question solutions (`steps` and `answer`) are not in the old plan. They are marked *to author* and nothing is invented here.

## Plan at a glance

| Module | Topic | Concepts |
|---|---|---|
| M1 Similar figures | T1 Same Shape, Different Size (hook) | C1 |
| | T2 Similar Figures | C2 |
| | T3 Similar Polygons | C3–C6 |
| | T4 Questions: Similar Figures | C7–C13 |
| M2 The basic proportionality theorem | T5 Similar Triangles and the Basic Proportionality Theorem | C14–C18 |
| | T6 Examples: Basic Proportionality | C19–C21 |
| | T7 Questions: Basic Proportionality | C22–C34 |
| M3 Criteria for similarity of triangles | T8 Criteria for Similarity of Triangles | C35–C42 |
| | T9 Examples: Similarity Criteria | C43–C47 |
| | T10 Questions: Similarity Criteria | C48–C66 |
| M4 Wrap-up | T11 Chapter Summary | C67–C68 |

Totals: 68 concepts and 25 objectives (none new). 39 question concepts need a new image. 0 new videos. Old media: 42 = 28 attached + 14 held (8 tools, 3 question videos, 3 exercise-figure images).

---

# M1 · Similar figures

## T1 · Same Shape, Different Size (hook)

### C1 · How do we measure what we cannot reach?
`kind: hook` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Measuring What We Cannot Reach" — A scenic picture of a tall snow-capped mountain peak with a small hiker at its base holding a measuring tape that is clearly far too short, and the moon high in the night sky beside it. Faint dotted sight-lines run from the hiker's eye up towards the summit and the moon, and a question mark floats over each.

[textbook_text]
> You are familiar with triangles and many of their properties from your earlier classes. In Class IX, you have studied congruence of triangles in detail. Recall that two figures are said to be congruent, if they have the same shape and the same size. In this chapter, we shall study about those figures which have the same shape but not necessarily the same size. Two figures having the same shape (and not necessarily the same size) are called similar figures. In particular, we shall discuss the similarity of triangles and apply this knowledge in giving a simple proof of Pythagoras Theorem learnt earlier.
>
> Can you guess how heights of mountains (say Mount Everest) or distances of some long distant objects (say moon) have been found out? Do you think these have been measured directly with the help of a measuring tape? In fact, all these heights and distances have been found out using the idea of indirect measurements, which is based on the principle of similarity of figures (you will meet such problems later in this chapter and in later chapters).

*(Cleanup: the pointer "see Example 7, Q.15 of Exercise 6.3 and also Chapters 8 and 9 of this book" became "you will meet such problems later in this chapter and in later chapters". The Pythagoras sentence is kept as the book prints it, although this reprint no longer carries that proof; please check in review.)*

---

## T2 · Similar Figures

### C2 · Same shape, not necessarily the same size
`kind: teach` · `objectives: O1, O2`
Media: existing video "Similar vs Congruent: Passport Photo and Map Analogy" (old T1 VID1); existing image "Similar Figure Families: Circles, Squares, Equilateral Triangles" (old T1 O1.E1)

[textbook_text]
> In Class IX, you have seen that all circles with the same radii are congruent, all squares with the same side lengths are congruent and all equilateral triangles with the same side lengths are congruent.
>
> Now consider any two (or more) circles (see the figure). Are they congruent? Since all of them do not have the same radius, they are not congruent to each other. Note that some are congruent and some are not, but all of them have the same shape. So they all are, what we call, similar. Two similar figures have the same shape but not necessarily the same size. Therefore, all circles are similar. What about two (or more) squares or two (or more) equilateral triangles (see the figure)? As observed in the case of circles, here also all squares are similar and all equilateral triangles are similar.
>
> From the above, we can say that all congruent figures are similar but the similar figures need not be congruent.
>
> Can a circle and a square be similar? Can a triangle and a square be similar? These questions can be answered by just looking at the figures. Evidently these figures are not similar. (Why?)

*(Cleanup: "[see Fig. 6.1 (i)]" and "[see Fig. 6.1 (ii) and (iii)]" became "see the figure". The "(Why?)" is answered in C6.)*

---

## T3 · Similar Polygons

### C3 · When are two polygons similar?
`kind: teach` · `objectives: O2, O3`
Media: existing video "Two Conditions for Polygon Similarity: Animated Walkthrough" (old T2 VID1)

[textbook_text]
> What can you say about the two quadrilaterals ABCD and PQRS in the figure? Are they similar? These figures appear to be similar but we cannot be certain about it. Therefore, we must have some definition of similarity of figures and based on this definition some rules to decide whether the two given figures are similar or not. For this, let us look at some photographs.
>
> You will at once say that they are the photographs of the same monument (Taj Mahal) but are in different sizes. Would you say that the three photographs are similar? Yes, they are.
>
> What can you say about the two photographs of the same size of the same person one at the age of 10 years and the other at the age of 40 years? Are these photographs similar? These photographs are of the same size but certainly they are not of the same shape. So, they are not similar.
>
> What does the photographer do when she prints photographs of different sizes from the same negative? You must have heard about the stamp size, passport size and postcard size photographs. She generally takes a photograph on a small size film, say of 35mm size and then enlarges it into a bigger size, say 45mm (or 55mm). Thus, if we consider any line segment in the smaller photograph (figure), its corresponding line segment in the bigger photograph (figure) will be 45/35 or 55/35 of that of the line segment. This really means that every line segment of the smaller photograph is enlarged (increased) in the ratio 35:45 (or 35:55). It can also be said that every line segment of the bigger photograph is reduced (decreased) in the ratio 45:35 (or 55:35). Further, if you consider inclinations (or angles) between any pair of corresponding line segments in the two photographs of different sizes, you shall see that these inclinations (or angles) are always equal. This is the essence of the similarity of two figures and in particular of two polygons. We say that:

[method_statement]
> Two polygons of the same number of sides are similar, if (i) their corresponding angles are equal and (ii) their corresponding sides are in the same ratio (or proportion).

[textbook_text]
> Note that the same ratio of the corresponding sides is referred to as the scale factor (or the Representative Fraction) for the polygons. You must have heard that world maps (i.e., global maps) and blue prints for the construction of a building are prepared using a suitable scale factor and observing certain conventions.

*(Cleanup: "(see Fig 6.2)" became "in the figure"; "the photographs given in Fig. 6.3:" became "some photographs". The quadrilateral pair and the Taj Mahal photos are book figures with no old image; no new image is planned here.)*

### C4 · A shadow that is an enlargement
`kind: teach` · `objectives: O3`
Media: existing image "Activity 1: Lightbulb Shadow Enlargement of Quadrilateral ABCD" (old T2 O1.E1) [title carries an activity number, renamed at build]

[textbook_text]
> In order to understand similarity of figures more clearly, let us perform the following activity:
>
> Activity : Place a lighted bulb at a point O on the ceiling and directly below it a table in your classroom. Let us cut a polygon, say a quadrilateral ABCD, from a plane cardboard and place this cardboard parallel to the ground between the lighted bulb and the table. Then a shadow of ABCD is cast on the table. Mark the outline of this shadow as A'B'C'D' (see the figure).
>
> Note that the quadrilateral A'B'C'D' is an enlargement (or magnification) of the quadrilateral ABCD. This is because of the property of light that light propagates in a straight line. You may also note that A' lies on ray OA, B' lies on ray OB, C' lies on OC and D' lies on OD. Thus, quadrilaterals ABCD and A'B'C'D' are of the same shape but of different sizes.
>
> So, quadrilateral ABCD is similar to quadrilateral A'B'C'D'. We can also say that quadrilateral A'B'C'D' is similar to the quadrilateral ABCD.
>
> Here, you can also note that vertex A corresponds to vertex A', vertex B corresponds to vertex B', vertex C corresponds to vertex C' and vertex D corresponds to vertex D'. Symbolically, these correspondences are represented as A↔A', B↔B', C↔C' and D↔D'. By actually measuring the angles and the sides of the two quadrilaterals, you may verify that
> (i) ∠A = ∠A', ∠B = ∠B', ∠C = ∠C', ∠D = ∠D' and
> (ii) AB/A'B' = BC/B'C' = CD/C'D' = DA/D'A'.
>
> This again emphasises that two polygons of the same number of sides are similar, if (i) all the corresponding angles are equal and (ii) all the corresponding sides are in the same ratio (or proportion).
>
> From the above, you can easily say that the quadrilaterals ABCD and PQRS in the figure are similar.

[remark, from source]
> You can verify that if one polygon is similar to another polygon and this second polygon is similar to a third polygon, then the first polygon is similar to the third polygon.

### C5 · One condition is not enough
`kind: teach` · `objectives: O4`
Media: existing image "Counter-Examples: Square–Rectangle and Square–Rhombus" (old T2 O2.E1)

[textbook_text]
> You may note that in the two quadrilaterals (a square and a rectangle) in the figure, corresponding angles are equal, but their corresponding sides are not in the same ratio. So, the two quadrilaterals are not similar. Similarly, you may note that in the two quadrilaterals (a square and a rhombus) in the figure, corresponding sides are in the same ratio, but their corresponding angles are not equal. Again, the two polygons (quadrilaterals) are not similar.
>
> Thus, either of the above two conditions (i) and (ii) of similarity of two polygons is not sufficient for them to be similar.

### C6 · More to explore: shapes that can never be similar
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Shapes That Can Never Match" — Three pairs side by side. A circle beside a square, each labelled with its features (no corners, curved edge versus four corners, four straight sides). A triangle beside a square, labelled 3 sides and 4 sides. Two identical squares of side 2 cm with all angles marked 90 degrees, drawn beside one another.

[enrichment] `[authored answers]`
> **Q.** Why can a circle and a square never be similar, or a triangle and a square?
> **A.** Similar figures must have the same shape. A circle has no corners and no straight sides, while a square has four corners and four straight sides, so no enlargement or reduction can turn one into the other. A triangle and a square have different numbers of sides, so their sides and angles cannot even be paired off.

[enrichment] `[authored answers]`
> **Q.** Two squares of sides 2 cm and 2 cm are congruent. Are they also similar?
> **A.** Yes. Their corresponding angles are all 90° and their corresponding sides are in the ratio 1 : 1. Every pair of congruent figures is similar, with scale factor 1.

---

## T4 · Questions: Similar Figures

Objectives for this set: O5 (apply) use the definition of similar figures to complete statements, give examples and classify given shapes; O2 (apply) give everyday examples of similar and non-similar figures.

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, statement only (or the book's own figure only), no working and no answer. There is no video. Hint, solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for all 7.
The questions are in book order. The four blanks of the first question and the two parts of the second are independent tasks, so each is its own concept.

### C7 · Similar Figures, Q1 (i)
`objectives: O5` · Media: new image spec (statement only)
> Fill in the blank using the correct word given in brackets:
> (i) All circles are ___. (congruent, similar)

### C8 · Similar Figures, Q1 (ii)
`objectives: O5` · Media: new image spec (statement only)
> Fill in the blank using the correct word given in brackets:
> (ii) All squares are ___. (similar, congruent)

### C9 · Similar Figures, Q1 (iii)
`objectives: O5` · Media: new image spec (statement only)
> Fill in the blank using the correct word given in brackets:
> (iii) All ___ triangles are similar. (isosceles, equilateral)

### C10 · Similar Figures, Q1 (iv)
`objectives: O5` · Media: new image spec (statement only)
> Fill in the blanks using the correct words given in brackets:
> (iv) Two polygons of the same number of sides are similar, if (a) their corresponding angles are ___ and (b) their corresponding sides are ___. (equal, proportional)

### C11 · Similar Figures, Q2 (i)
`objectives: O2, O5` · Media: new image spec (statement only)
> Give two different examples of pair of
> (i) similar figures.

### C12 · Similar Figures, Q2 (ii)
`objectives: O2, O5` · Media: new image spec (statement only)
> Give two different examples of pair of
> (ii) non-similar figures.

### C13 · Similar Figures, Q3
`objectives: O5` · Media: new image spec (**the book's own figure only**, as it supplies the two quadrilaterals and their measures)
> State whether the following quadrilaterals are similar or not.

---

# M2 · The basic proportionality theorem

## T5 · Similar Triangles and the Basic Proportionality Theorem

### C14 · The basic proportionality theorem: try it first
`kind: try` · `objectives: O6`
Media: existing video "Thales of Miletus and the Discovery of BPT" (old T4 VID1); existing image "Activity 2: BPT Discovery Construction (Fig. 6.9)" (old T4 O1.E1) [title carries a book number, renamed at build]
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[textbook_text]
> What can you say about the similarity of two triangles?
>
> You may recall that triangle is also a polygon. So, we can state the same conditions for the similarity of two triangles. That is:
> Two triangles are similar, if
> (i) their corresponding angles are equal and
> (ii) their corresponding sides are in the same ratio (or proportion).
>
> Note that if corresponding angles of two triangles are equal, then they are known as equiangular triangles. A famous Greek mathematician Thales gave an important truth relating to two equiangular triangles which is as follows:
> The ratio of any two corresponding sides in two equiangular triangles is always the same.
> It is believed that he had used a result called the Basic Proportionality Theorem (now known as the Thales Theorem) for the same.
>
> To understand the Basic Proportionality Theorem, let us perform the following activity:
>
> Activity : Draw any angle XAY and on its one arm AX, mark points (say five points) P, Q, D, R and B such that AP = PQ = QD = DR = RB.
> Now, through B, draw any line intersecting arm AY at C (see the figure).
> Also, through the point D, draw a line parallel to BC to intersect AC at E. Do you observe from your constructions that AD/DB = 3/2? Measure AE and EC. What about AE/EC? Observe that AE/EC is also equal to 3/2. Thus, you can see that in △ABC, DE ∥ BC and AD/DB = AE/EC. Is it a coincidence? No, it is due to the following theorem (known as the Basic Proportionality Theorem):

[theorem_statement]
> If a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, the other two sides are divided in the same ratio.

[predict] `[authored]`
> Suppose D is placed on AB so that AD : DB = 4 : 1, and the line through D parallel to BC meets AC at E. Before measuring, what do you expect AE : EC to be? Now move D so that AD : DB = 1 : 4. Commit to a guess for AE : EC. The next concept shows why the answer never depends on where D is.

*(Cleanup: the section heading "6.3 Similarity of Triangles" and the label "Activity 2" were removed; "(see Fig. 6.9)" became "(see the figure)". The theorem's book label "Theorem 6.1" is in metadata only.)*

### C15 · Why the basic proportionality theorem holds
`kind: prove` · `objectives: O7`
Media: existing video "Theorem 6.1 (BPT) Proof Animation" (old T5 VID1) [title carries a book number, renamed at build]; existing image "Theorem 6.1 Proof Diagram: Areas of △ADE, △BDE, △DEC (Fig. 6.10)" (old T5 O1.E1) [title carries book numbers, renamed at build]

[textbook_text]
> We are given a triangle ABC in which a line parallel to side BC intersects other two sides AB and AC at D and E respectively (see the figure).
> We need to prove that AD/DB = AE/EC.
> Let us join BE and CD and then draw DM ⊥ AC and EN ⊥ AB.
> Now, area of △ADE (= 1/2 × base × height) = 1/2 × AD × EN.
> Recall from Class IX, that area of △ADE is denoted as ar(ADE).
> So, ar(ADE) = 1/2 × AD × EN
> Similarly, ar(BDE) = 1/2 × DB × EN,
> ar(ADE) = 1/2 × AE × DM and ar(DEC) = 1/2 × EC × DM.
> Therefore, ar(ADE)/ar(BDE) = (AD × EN)/(DB × EN) = AD/DB ... (1)
> and ar(ADE)/ar(DEC) = (AE × DM)/(EC × DM) = AE/EC ... (2)
> Note that △BDE and DEC are on the same base DE and between the same parallels BC and DE.
> So, ar(BDE) = ar(DEC) ... (3)
> Therefore, from (1), (2) and (3), we have :
> AD/DB = AE/EC

### C16 · The converse: try it first
`kind: try` · `objectives: O8`
Media: existing image "Activity 3 (Fig. 6.11) and Theorem 6.2 Contradiction Diagram (Fig. 6.12)" (old T6 O1.E1) [title carries book numbers, renamed at build; the image also shows the proof figure used in C17]
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[textbook_text]
> Is the converse of this theorem also true? To examine this, let us perform the following activity:
>
> Activity : Draw an angle XAY on your notebook and on ray AX, mark points B₁, B₂, B₃, B₄ and B such that AB₁ = B₁B₂ = B₂B₃ = B₃B₄ = B₄B.
> Similarly, on ray AY, mark points C₁, C₂, C₃, C₄ and C such that AC₁ = C₁C₂ = C₂C₃ = C₃C₄ = C₄C. Then join B₁C₁ and BC (see the figure).
> Note that AB₁/B₁B = AC₁/C₁C = 1/4. You can also see that lines B₁C₁ and BC are parallel to each other, i.e., B₁C₁ ∥ BC ... (1)
> Similarly, by joining B₂C₂, B₃C₃ and B₄C₄, you can see that:
> AB₂/B₂B = AC₂/C₂C = 2/3 and B₂C₂ ∥ BC ... (2)
> AB₃/B₃B = AC₃/C₃C = 3/2 and B₃C₃ ∥ BC ... (3)
> AB₄/B₄B = AC₄/C₄C = 4/1 and B₄C₄ ∥ BC ... (4)
> From (1), (2), (3) and (4), it can be observed that if a line divides two sides of a triangle in the same ratio, then the line is parallel to the third side.
> You can repeat this activity by drawing any angle XAY of different measure and taking any number of equal parts on arms AX and AY. Each time, you will arrive at the same result. Thus, we obtain the following theorem, which is the converse of the basic proportionality theorem:

[theorem_statement]
> If a line divides any two sides of a triangle in the same ratio, then the line is parallel to the third side.

[predict] `[authored]`
> In △PQR, a line meets PQ at S and PR at T with PS/SQ = PT/TR = 3/5. Without measuring any angle, do you think ST must be parallel to QR? Commit to yes or no, and say what would have to go wrong if it were not. The next concept checks your reasoning.

*(Cleanup: "(For the meaning of converse, see Appendix 1)" was removed; "the converse of Theorem 6.1" became "the converse of the basic proportionality theorem"; the label "Activity 3" was removed.)*

### C17 · Why the converse holds
`kind: prove` · `objectives: O8`
Media: existing video "Converse BPT (Theorem 6.2) Contradiction Proof Animation" (old T6 VID1) [title carries a book number, renamed at build]

[textbook_text]
> This theorem can be proved by taking a line DE such that AD/DB = AE/EC and assuming that DE is not parallel to BC (see the figure).
> If DE is not parallel to BC, draw a line DE' parallel to BC.
> So, AD/DB = AE'/E'C (Why?)
> Therefore, AE/EC = AE'/E'C (Why?)
> Adding 1 to both sides of above, you can see that E and E' must coincide. (Why?)

### C18 · More to explore: the converse's "Why?" prompts
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Two Points on One Side, One Line" — Triangle ABC with a point D on side AB. A point E on side AC is marked so that AD/DB = AE/EC is written beside the figure. A second point E' on AC is shown with a dashed line from D to E' drawn parallel to BC with the parallel marks. The segments AD, DB, AE, EC, AE' and E'C are labelled.

[enrichment] `[authored answers]`
> **Q.** Why is AD/DB = AE'/E'C?
> **A.** DE' is parallel to BC and meets the sides AB and AC of △ABC at D and E', so the basic proportionality theorem gives AD/DB = AE'/E'C.

[enrichment] `[authored answers]`
> **Q.** Why is AE/EC = AE'/E'C?
> **A.** We are given AD/DB = AE/EC, and we have just found AD/DB = AE'/E'C. Both ratios equal AD/DB, so they equal each other.

[enrichment] `[authored answers]`
> **Q.** Why must E and E' coincide?
> **A.** Adding 1 to both sides gives (AE + EC)/EC = (AE' + E'C)/E'C, that is, AC/EC = AC/E'C. So EC = E'C. Both points lie on AC at the same distance from C, so they are the same point, and DE is the line DE', which is parallel to BC.

---

## T6 · Examples: Basic Proportionality

### C19 · A parallel line cuts both sides in the same fraction
`kind: exercise (worked example)` · `objectives: O9`
Media: existing image "Reference Diagrams for Examples 1, 2, and 3" (old T7 O1.E1) [title carries book numbers, renamed at build]. The image holds the figures of all three examples, so the fit is loose. Please check it in review.

[question]
> If a line intersects sides AB and AC of a △ABC at D and E respectively and is parallel to BC, prove that AD/AB = AE/AC.

[worked solution, from source]
> DE ∥ BC (Given)
> So, AD/DB = AE/EC (Basic proportionality theorem)
> DB/AD = EC/AE
> or, DB/AD + 1 = EC/AE + 1
> or, AB/AD = AC/AE
> So, AD/AB = AE/AC

### C20 · A line parallel to the sides of a trapezium
`kind: exercise (worked example)` · `objectives: O9`
Media: existing video "Example 2 Animated Walkthrough: Trapezium with EF Parallel to AB" (old T7 VID1) [title carries a book number, renamed at build]

[question]
> ABCD is a trapezium with AB ∥ DC. E and F are points on non-parallel sides AD and BC respectively such that EF is parallel to AB (see the figure). Show that AE/ED = BF/FC.

[worked solution, from source]
> Let us join AC to intersect EF at G (see the figure).
> AB ∥ DC and EF ∥ AB (Given)
> So, EF ∥ DC (Lines parallel to the same line are parallel to each other)
> Now, in △ADC,
> EG ∥ DC (As EF ∥ DC)
> So, AE/ED = AG/GC (Basic proportionality theorem) ... (1)
> Similarly, from △CAB,
> CG/GA = CF/FB
> i.e., AG/GC = BF/FC ... (2)
> Therefore, from (1) and (2),
> AE/ED = BF/FC

### C21 · Equal ratios that make a triangle isosceles
`kind: exercise (worked example)` · `objectives: O9`
Media: new image spec "A Triangle with Two Matching Clues" — Triangle PQR with point S on side PQ and point T on side PR, and the segment ST drawn. The ratio PS/SQ = PT/TR is written beside the figure, and the angle at S (angle PST) and the angle at R (angle PRQ) are marked with the same arc to show they are equal. The sides are not labelled with lengths.

[question]
> In the figure, PS/SQ = PT/TR and ∠PST = ∠PRQ. Prove that PQR is an isosceles triangle.

[worked solution, from source]
> It is given that PS/SQ = PT/TR
> So, ST ∥ QR (Converse of the basic proportionality theorem)
> Therefore, ∠PST = ∠PQR (Corresponding angles) ... (1)
> Also, it is given that
> ∠PST = ∠PRQ ... (2)
> So, ∠PRQ = ∠PQR [From (1) and (2)]
> Therefore, PQ = PR (Sides opposite the equal angles)
> i.e., PQR is an isosceles triangle.

*(Cleanup for C19 to C21: the labels "Example 1:" to "Example 3:" and "Solution :" were removed; "(see Fig. 6.13)" was dropped, "(see Fig. 6.14)", "(see Fig. 6.15)" became "(see the figure)", "In Fig. 6.16" became "In the figure"; "(Theorem 6.1)" and "(Theorem 6.2)" became the theorem names. The lead-in "Let us take some examples to illustrate the use of the above theorems." is carried in the topic summary.)*

---

## T7 · Questions: Basic Proportionality

Objectives for this set: O10 (apply) use the basic proportionality theorem and its converse to find unknown lengths and to decide whether a line is parallel to a side; O12 (analyze) pick out, in a figure with several triangles, which triangle and which parallel line to use; O11 (evaluate) write proofs with the theorem for mid-points, trapezia and intersecting diagonals.

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, statement only (or the book's own figure only), no working and no answer. There is no video. Hint, solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for all 13.
The questions are in book order. The two figures of the first question and the three cases of the second are independent tasks, so each is its own concept.

### C22 · Basic Proportionality, Q1 (i)
`objectives: O10` · Media: new image spec (**the book's own figure (i) only**, as it supplies the lengths)
> In the figure, DE ∥ BC.
> (i) Find EC.

### C23 · Basic Proportionality, Q1 (ii)
`objectives: O10` · Media: new image spec (**the book's own figure (ii) only**, as it supplies the lengths)
> In the figure, DE ∥ BC.
> (ii) Find AD.

### C24 · Basic Proportionality, Q2 (i)
`objectives: O10` · Media: new image spec (statement only)
> E and F are points on the sides PQ and PR respectively of a △PQR. For the following case, state whether EF ∥ QR:
> (i) PE = 3.9 cm, EQ = 3 cm, PF = 3.6 cm and FR = 2.4 cm

### C25 · Basic Proportionality, Q2 (ii)
`objectives: O10` · Media: new image spec (statement only)
> E and F are points on the sides PQ and PR respectively of a △PQR. For the following case, state whether EF ∥ QR:
> (ii) PE = 4 cm, QE = 4.5 cm, PF = 8 cm and RF = 9 cm

### C26 · Basic Proportionality, Q2 (iii)
`objectives: O10` · Media: new image spec (statement only)
> E and F are points on the sides PQ and PR respectively of a △PQR. For the following case, state whether EF ∥ QR:
> (iii) PQ = 1.28 cm, PR = 2.56 cm, PE = 0.18 cm and PF = 0.36 cm

### C27 · Basic Proportionality, Q3
`objectives: O12` · Media: new image spec (**the book's own figure only**, as it shows how the points and lines sit)
> In the figure, if LM ∥ CB and LN ∥ CD, prove that AM/AB = AN/AD.

### C28 · Basic Proportionality, Q4
`objectives: O12` · Media: new image spec (**the book's own figure only**, as it shows how the points and lines sit)
> In the figure, DE ∥ AC and DF ∥ AE. Prove that BF/FE = BE/EC.

### C29 · Basic Proportionality, Q5
`objectives: O12` · Media: new image spec (**the book's own figure only**, as it shows how the points and lines sit)
> In the figure, DE ∥ OQ and DF ∥ OR. Show that EF ∥ QR.

### C30 · Basic Proportionality, Q6
`objectives: O12` · Media: new image spec (**the book's own figure only**, as it shows how the points and lines sit)
> In the figure, A, B and C are points on OP, OQ and OR respectively such that AB ∥ PQ and AC ∥ PR. Show that BC ∥ QR.

### C31 · Basic Proportionality, Q7
`objectives: O11` · Media: new image spec (statement only)
> Using the basic proportionality theorem, prove that a line drawn through the mid-point of one side of a triangle parallel to another side bisects the third side. (Recall that you have proved it in Class IX.)

### C32 · Basic Proportionality, Q8
`objectives: O11` · Media: new image spec (statement only)
> Using the converse of the basic proportionality theorem, prove that the line joining the mid-points of any two sides of a triangle is parallel to the third side. (Recall that you have done it in Class IX.)

### C33 · Basic Proportionality, Q9
`objectives: O11` · Media: new image spec (statement only)
> ABCD is a trapezium in which AB ∥ DC and its diagonals intersect each other at the point O. Show that AO/CO = BO/DO.

### C34 · Basic Proportionality, Q10
`objectives: O11` · Media: new image spec (statement only)
> The diagonals of a quadrilateral ABCD intersect each other at the point O such that AO/CO = BO/DO. Show that ABCD is a trapezium.

*(Cleanup for this set: "In Fig. 6.17 to 6.21" became "In the figure"; in the seventh and eighth questions "Using Theorem 6.1" and "Using Theorem 6.2" became the theorem names.)*

---

# M3 · Criteria for similarity of triangles

## T8 · Criteria for Similarity of Triangles

### C35 · Writing a similarity the right way round
`kind: teach` · `objectives: O13`
Media: existing image "Similarity Notation Diagram: Triangle ABC similar to Triangle DEF with Vertex Correspondence" (old T9 O1.E1)

[textbook_text]
> Earlier, we stated that two triangles are similar, if (i) their corresponding angles are equal and (ii) their corresponding sides are in the same ratio (or proportion). That is, in △ABC and △DEF, if
> (i) ∠A = ∠D, ∠B = ∠E, ∠C = ∠F and
> (ii) AB/DE = BC/EF = CA/FD, then the two triangles are similar (see the figure).
>
> Here, you can see that A corresponds to D, B corresponds to E and C corresponds to F. Symbolically, we write the similarity of these two triangles as '△ABC ~ △DEF' and read it as 'triangle ABC is similar to triangle DEF'. The symbol '~' stands for 'is similar to'. Recall that you have used the symbol '≅' for 'is congruent to' in Class IX.
>
> It must be noted that as done in the case of congruency of two triangles, the similarity of two triangles should also be expressed symbolically, using correct correspondence of their vertices. For example, for the triangles ABC and DEF in the figure, we cannot write △ABC ~ △EDF or △ABC ~ △FED. However, we can write △BAC ~ △EDF.
>
> Now a natural question arises : For checking the similarity of two triangles, say ABC and DEF, should we always look for all the equality relations of their corresponding angles (∠A = ∠D, ∠B = ∠E, ∠C = ∠F) and all the equality relations of the ratios of their corresponding sides (AB/DE = BC/EF = CA/FD)? Let us examine. You may recall that in Class IX, you have obtained some criteria for congruency of two triangles involving only three pairs of corresponding parts (or elements) of the two triangles. Here also, let us make an attempt to arrive at certain criteria for similarity of two triangles involving relationship between less number of pairs of corresponding parts of the two triangles, instead of all the six pairs of corresponding parts.

*(Cleanup: the heading "6.4 Criteria for Similarity of Triangles" was removed; "In the previous section" became "Earlier"; "(see Fig. 6.22)" became "(see the figure)" and "of Fig. 6.22" became "in the figure".)*

### C36 · Equal angles: try it first
`kind: try` · `objectives: O14`
Media: existing image "Activity 4: Equiangular Triangles ABC and DEF with Measured Side Ratios" (old T9 O2.E1) [title carries an activity number, renamed at build]
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[textbook_text]
> For this, let us perform the following activity:
>
> Activity : Draw two line segments BC and EF of two different lengths, say 3 cm and 5 cm respectively. Then, at the points B and C respectively, construct angles PBC and QCB of some measures, say, 60° and 40°. Also, at the points E and F, construct angles REF and SFE of 60° and 40° respectively (see the figure).
>
> Let rays BP and CQ intersect each other at A and rays ER and FS intersect each other at D. In the two triangles ABC and DEF, you can see that ∠B = ∠E, ∠C = ∠F and ∠A = ∠D. That is, corresponding angles of these two triangles are equal. Note that BC/EF = 3/5 = 0.6. On measuring AB, DE, CA and FD, you will find that AB/DE and CA/FD are also equal to 0.6 (or nearly equal to 0.6, if there is some error in the measurement). Thus, AB/DE = BC/EF = CA/FD. You can repeat this activity by constructing several pairs of triangles having their corresponding angles equal. Every time, you will find that their corresponding sides are in the same ratio (or proportion). This activity leads us to the following criterion for similarity of two triangles.

[theorem_statement]
> If in two triangles, corresponding angles are equal, then their corresponding sides are in the same ratio (or proportion) and hence the two triangles are similar.
> This criterion is referred to as the AAA (Angle–Angle–Angle) criterion of similarity of two triangles.

[predict] `[authored]`
> Two triangles both have angles 60°, 40° and 80°. One has its shortest side 3 cm, the other 6 cm. Guess the ratio of their longest sides before measuring anything. Then guess: is it enough to know that just two pairs of angles match? The next concept answers both.

### C37 · Why equal angles force equal ratios
`kind: prove` · `objectives: O14`
Media: existing video "Theorem 6.3 Proof Sketch Animation: AAA Criterion" (old T9 VID1) [title carries a book number, renamed at build]

[textbook_text]
> This theorem can be proved by taking two triangles ABC and DEF such that ∠A = ∠D, ∠B = ∠E and ∠C = ∠F (see the figure). Cut DP = AB and DQ = AC and join PQ.
> So, △ABC ≅ △DPQ (Why?)
> This gives ∠B = ∠P = ∠E and PQ ∥ EF (How?)
> Therefore, DP/PE = DQ/QF (Why?)
> i.e., AB/DE = AC/DF (Why?)
> Similarly, AB/DE = BC/EF and so AB/DE = BC/EF = AC/DF.

[remark, from source]
> If two angles of a triangle are respectively equal to two angles of another triangle, then by the angle sum property of a triangle their third angles will also be equal. Therefore, AAA similarity criterion can also be stated as follows:
> If two angles of one triangle are respectively equal to two angles of another triangle, then the two triangles are similar.
> This may be referred to as the AA similarity criterion for two triangles.

*(The book's proof figure for this sketch (Fig. 6.24) has no old image; the video draws it.)*

### C38 · Proportional sides: try it first
`kind: try` · `objectives: O15`
Media: new image spec "Two Triangles with Given Side Lengths" — Two separate triangles drawn side by side with no angle marks. Triangle ABC has AB = 3 cm, BC = 6 cm and CA = 8 cm. Triangle DEF is larger and has DE = 4.5 cm, EF = 9 cm and FD = 12 cm. Each side is labelled with its length and the vertices are named.
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[textbook_text]
> You have seen above that if the three angles of one triangle are respectively equal to the three angles of another triangle, then their corresponding sides are proportional (i.e., in the same ratio). What about the converse of this statement? Is the converse true? In other words, if the sides of a triangle are respectively proportional to the sides of another triangle, is it true that their corresponding angles are equal? Let us examine it through an activity :
>
> Activity : Draw two triangles ABC and DEF such that AB = 3 cm, BC = 6 cm, CA = 8 cm, DE = 4.5 cm, EF = 9 cm and FD = 12 cm (see the figure).
> So, you have : AB/DE = BC/EF = CA/FD = 2/3.
> Now measure ∠A, ∠B, ∠C, ∠D, ∠E and ∠F. You will observe that ∠A = ∠D, ∠B = ∠E and ∠C = ∠F, i.e., the corresponding angles of the two triangles are equal.
> You can repeat this activity by drawing several such triangles (having their sides in the same ratio). Everytime you shall see that their corresponding angles are equal. It is due to the following criterion of similarity of two triangles:

[theorem_statement]
> If in two triangles, sides of one triangle are proportional to (i.e., in the same ratio of) the sides of the other triangle, then their corresponding angles are equal and hence the two triangles are similar.
> This criterion is referred to as the SSS (Side–Side–Side) similarity criterion for two triangles.

[predict] `[authored]`
> A triangle has sides 3 cm, 6 cm and 8 cm. A second triangle has sides 4.5 cm, 9 cm and 12 cm. Before measuring, do you expect the angle opposite the 8 cm side to equal the angle opposite the 12 cm side? Commit to yes or no. The next concept shows why.

### C39 · Why proportional sides force equal angles
`kind: prove` · `objectives: O15`
Media: existing video "Theorem 6.4 (SSS Similarity) Proof Animation" (old T10 VID1) [title carries a book number, renamed at build]; existing image "Theorem 6.4 Proof Diagram: △ABC Inside △DEF with Cut DP = AB" (old T10 O1.E1) [title carries a book number, renamed at build]

[textbook_text]
> This theorem can be proved by taking two triangles ABC and DEF such that AB/DE = BC/EF = CA/FD (< 1) (see the figure):
> Cut DP = AB and DQ = AC and join PQ.
> It can be seen that DP/PE = DQ/QF and PQ ∥ EF (How?)
> So, ∠P = ∠E and ∠Q = ∠F.
> Therefore, DP/DE = DQ/DF = PQ/EF
> So, DP/DE = DQ/DF = BC/EF (Why?)
> So, BC = PQ (Why?)
> Thus, △ABC ≅ △DPQ (Why?)
> So, ∠A = ∠D, ∠B = ∠E and ∠C = ∠F (How?)

[remark, from source]
> You may recall that either of the two conditions namely, (i) corresponding angles are equal and (ii) corresponding sides are in the same ratio is not sufficient for two polygons to be similar. However, on the basis of the AAA and SSS criteria, you can now say that in case of similarity of the two triangles, it is not necessary to check both the conditions as one condition implies the other.

*(Cleanup: "Theorems 6.3 and 6.4" became "the AAA and SSS criteria"; the label "Activity 5" was removed.)*

### C40 · One angle and two sides: try it first
`kind: try` · `objectives: O16`
Media: new image spec "Two Triangles with One Angle Each" — Two separate triangles side by side. Triangle ABC has AB = 2 cm, AC = 4 cm and the angle at A between them marked as 50 degrees. Triangle DEF is larger with DE = 3 cm, DF = 6 cm and the angle at D between them marked as 50 degrees. The other sides and angles are left unlabelled.
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[textbook_text]
> Let us now recall the various criteria for congruency of two triangles learnt in Class IX. You may observe that SSS similarity criterion can be compared with the SSS congruency criterion. This suggests us to look for a similarity criterion comparable to SAS congruency criterion of triangles. For this, let us perform an activity.
>
> Activity : Draw two triangles ABC and DEF such that AB = 2 cm, ∠A = 50°, AC = 4 cm, DE = 3 cm, ∠D = 50° and DF = 6 cm (see the figure).
> Here, you may observe that AB/DE = AC/DF = 2/3 and ∠A (included between the sides AB and AC) = ∠D (included between the sides DE and DF). That is, one angle of a triangle is equal to one angle of another triangle and sides including these angles are in the same ratio (i.e., proportion). Now let us measure ∠B, ∠C, ∠E and ∠F.
> You will find that ∠B = ∠E and ∠C = ∠F. That is, ∠A = ∠D, ∠B = ∠E and ∠C = ∠F. So, by AAA similarity criterion, △ABC ~ △DEF. You may repeat this activity by drawing several pairs of such triangles with one angle of a triangle equal to one angle of another triangle and the sides including these angles are proportional. Everytime, you will find that the triangles are similar. It is due to the following criterion of similarity of triangles:

[theorem_statement]
> If one angle of a triangle is equal to one angle of the other triangle and the sides including these angles are proportional, then the two triangles are similar.
> This criterion is referred to as the SAS (Side–Angle–Side) similarity criterion for two triangles.

[predict] `[authored]`
> Two triangles have a 50° angle each. In one, the sides around it are 2 cm and 4 cm; in the other, 3 cm and 6 cm. Guess whether the triangles are similar. Now suppose the 50° angle were not between the two sides. Would your answer stay the same? Commit, then read on.

### C41 · Why the SAS criterion holds
`kind: prove` · `objectives: O16`
Media: existing video "Theorem 6.5 (SAS Similarity) Proof Animation" (old T11 VID1) [title carries a book number, renamed at build]; existing image "Theorem 6.5 Proof Diagram: SAS Configuration with ∠A = ∠D = 50°" (old T11 O1.E1) [title carries a book number, renamed at build]

[textbook_text]
> As before, this theorem can be proved by taking two triangles ABC and DEF such that AB/DE = AC/DF (< 1) and ∠A = ∠D (see the figure). Cut DP = AB, DQ = AC and join PQ.
> Now, PQ ∥ EF and △ABC ≅ △DPQ (How?)
> So, ∠A = ∠D, ∠B = ∠P and ∠C = ∠Q
> Therefore, △ABC ~ △DEF (Why?)

*(Cleanup: the label "Activity 6" was removed.)*

### C42 · More to explore: the criteria's "Why?" and "How?" prompts
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Cutting a Copy Inside a Bigger Triangle" — A set of three small proof sketches. In each, a large triangle DEF has a point P on DE and a point Q on DF with the segment PQ drawn, and a smaller triangle ABC sits next to it with DP matching AB and DQ matching AC. The first sketch marks equal angles, the second marks the three side ratios, and the third marks one angle with its two enclosing sides.

[enrichment] `[authored answers]`
> **Q.** In the AAA sketch, why is △ABC ≅ △DPQ, and how do we get ∠B = ∠P = ∠E and PQ ∥ EF?
> **A.** DP = AB, DQ = AC and ∠D = ∠A, so the triangles are congruent by SAS. Then ∠B = ∠P as corresponding parts. We are given ∠B = ∠E, so ∠P = ∠E. These are corresponding angles for the lines PQ and EF cut by DE, so PQ ∥ EF.

[enrichment] `[authored answers]`
> **Q.** In the AAA sketch, why is DP/PE = DQ/QF, and why does that give AB/DE = AC/DF?
> **A.** PQ ∥ EF in △DEF, so the basic proportionality theorem gives DP/PE = DQ/QF. Turning both ratios over and adding 1 gives DE/DP = DF/DQ, so DP/DE = DQ/DF. Since DP = AB and DQ = AC, this is AB/DE = AC/DF.

[enrichment] `[authored answers]`
> **Q.** In the SSS sketch, how do we see DP/PE = DQ/QF and PQ ∥ EF?
> **A.** We are given AB/DE = CA/FD, that is DP/DE = DQ/DF. Then DP/(DE − DP) = DQ/(DF − DQ), which is DP/PE = DQ/QF. By the converse of the basic proportionality theorem, PQ ∥ EF.

[enrichment] `[authored answers]`
> **Q.** In the SSS sketch, why is DP/DE = DQ/DF = BC/EF, why is BC = PQ, and why is △ABC ≅ △DPQ?
> **A.** DP/DE = AB/DE, and AB/DE = BC/EF is given. From DP/DE = DQ/DF = PQ/EF we then get PQ/EF = BC/EF, so BC = PQ. Now AB = DP, AC = DQ and BC = PQ, so the triangles are congruent by SSS.

[enrichment] `[authored answers]`
> **Q.** In the SSS sketch, how do we finish with ∠A = ∠D, ∠B = ∠E and ∠C = ∠F?
> **A.** From the congruence, ∠A = ∠D, ∠B = ∠P and ∠C = ∠Q. From the parallel lines, ∠P = ∠E and ∠Q = ∠F. So ∠B = ∠E and ∠C = ∠F.

[enrichment] `[authored answers]`
> **Q.** In the SAS sketch, how do we get PQ ∥ EF and △ABC ≅ △DPQ, and why is △ABC ~ △DEF?
> **A.** AB/DE = AC/DF means DP/DE = DQ/DF, so DP/PE = DQ/QF and, by the converse of the basic proportionality theorem, PQ ∥ EF. DP = AB, DQ = AC and ∠D = ∠A give the congruence by SAS. Then ∠B = ∠P = ∠E and ∠C = ∠Q = ∠F (corresponding angles, as PQ ∥ EF), and ∠A = ∠D, so the triangles are similar by the AAA criterion.

---

## T9 · Examples: Similarity Criteria

### C43 · Parallel lines and a crossing point
`kind: exercise (worked example)` · `objectives: O17`
Media: new image spec "Two Parallel Lines Cut by Crossing Lines" — Two parallel segments PQ (top) and RS (bottom) marked with parallel arrows. Two straight lines cross each other at a point O between them: one joins P to S through O, and the other joins Q to R through O. The points P, Q, R, S and O are labelled, and triangles POQ and SOR are lightly shaded in different colours.

[question]
> In the figure, if PQ ∥ RS, prove that △POQ ~ △SOR.

[worked solution, from source]
> PQ ∥ RS (Given)
> So, ∠P = ∠S (Alternate angles)
> and ∠Q = ∠R
> Also, ∠POQ = ∠SOR (Vertically opposite angles)
> Therefore, △POQ ~ △SOR (AAA similarity criterion)

### C44 · Finding an angle from proportional sides
`kind: exercise (worked example)` · `objectives: O17`
Media: existing image "Reference Diagrams for Examples 4, 5, and 6" (old T12 O1.E1) [title carries book numbers, renamed at build]. The image holds the figures of all three examples. It is placed here because this example cannot be read without its figure. The fit is loose, so please check it in review.

[question]
> Observe the figure and then find ∠P.

[worked solution, from source]
> In △ABC and △PQR,
> AB/RQ = 3.8/7.6 = 1/2, BC/QP = 6/12 = 1/2, CA/PR = 3√3/6√3 = 1/2.
> That is, AB/RQ = BC/QP = CA/PR.
> So, △ABC ~ △RQP (SSS similarity)
> Therefore, ∠C = ∠P (Corresponding angles of similar triangles)
> But ∠C = 180° − ∠A − ∠B (Angle sum property)
> = 180° − 80° − 60° = 40°
> So, ∠P = 40°

### C45 · Equal products give equal angles
`kind: exercise (worked example)` · `objectives: O17`
Media: existing video "Example 6 Animated Walkthrough: OA·OB = OC·OD to SAS Similarity" (old T12 VID1) [title carries a book number, renamed at build]

[question]
> In the figure, OA . OB = OC . OD. Show that ∠A = ∠C and ∠B = ∠D.

[worked solution, from source]
> OA . OB = OC . OD (Given)
> So, OA/OC = OD/OB ... (1)
> Also, we have ∠AOD = ∠COB (Vertically opposite angles) ... (2)
> Therefore, from (1) and (2), △AOD ~ △COB (SAS similarity criterion)
> So, ∠A = ∠C and ∠D = ∠B
> (Corresponding angles of similar triangles)

### C46 · How long is her shadow?
`kind: exercise (worked example)` · `objectives: O18, O19`
Media: existing video "Example 7 Animated Walkthrough: Girl, Lamp-Post, and Shadow" (old T13 VID1) [title carries a book number, renamed at build]; existing image "Lamp-Post Shadow Problem Scenario Diagram (Fig. 6.32)" (old T13 O1.E1) [title carries a book number, renamed at build]

[question]
> A girl of height 90 cm is walking away from the base of a lamp-post at a speed of 1.2 m/s. If the lamp is 3.6 m above the ground, find the length of her shadow after 4 seconds.

[worked solution, from source]
> Let AB denote the lamp-post and CD the girl after walking for 4 seconds away from the lamp-post (see the figure). From the figure, you can see that DE is the shadow of the girl. Let DE be x metres.
> Now, BD = 1.2 m × 4 = 4.8 m.
> Note that in △ABE and △CDE,
> ∠B = ∠D (Each is of 90° because lamp-post as well as the girl are standing vertical to the ground)
> and ∠E = ∠E (Same angle)
> So, △ABE ~ △CDE (AA similarity criterion)
> Therefore, BE/DE = AB/CD
> (4.8 + x)/x = 3.6/0.9 (90 cm = 90/100 m = 0.9 m)
> i.e., 4.8 + x = 4x
> i.e., 3x = 4.8
> i.e., x = 1.6
> So, the shadow of the girl after walking for 4 seconds is 1.6 m long.

### C47 · Medians of similar triangles
`kind: exercise (worked example)` · `objectives: O20`
Media: existing video "Example 8 Part (i) Animated Walkthrough: Medians of Similar Triangles" (old T14 VID1) [title carries a book number, renamed at build]; existing image "Fig. 6.33: Similar Triangles ABC and PQR with Medians CM and RN" (old T14 O1.E1) [title carries a book number, renamed at build]

[question]
> In the figure, CM and RN are respectively the medians of △ABC and △PQR. If △ABC ~ △PQR, prove that :
> (i) △AMC ~ △PNR
> (ii) CM/RN = AB/PQ
> (iii) △CMB ~ △RNQ

[worked solution, from source]
> (i) △ABC ~ △PQR (Given)
> So, AB/PQ = BC/QR = CA/RP ... (1)
> and ∠A = ∠P, ∠B = ∠Q and ∠C = ∠R ... (2)
> But AB = 2 AM and PQ = 2 PN
> (As CM and RN are medians)
> So, from (1), 2AM/2PN = CA/RP
> i.e., AM/PN = CA/RP ... (3)
> Also, ∠MAC = ∠NPR [From (2)] ... (4)
> So, from (3) and (4),
> △AMC ~ △PNR (SAS similarity) ... (5)
> (ii) From (5), CM/RN = CA/RP ... (6)
> But CA/RP = AB/PQ [From (1)] ... (7)
> Therefore, CM/RN = AB/PQ [From (6) and (7)] ... (8)
> (iii) Again, AB/PQ = BC/QR [From (1)]
> Therefore, CM/RN = BC/QR [From (8)] ... (9)
> Also, CM/RN = AB/PQ = 2BM/2QN
> i.e., CM/RN = BM/QN ... (10)
> Therefore, CM/RN = BC/QR = BM/QN [From (9) and (10)]
> Therefore, △CMB ~ △RNQ (SSS similarity)

[remark, from source]
> You can also prove part (iii) by following the same method as used for proving part (i).

*(Cleanup for C43 to C47: the labels "Example 4:" to "Example 8:" and "Solution :" were removed; "In Fig. 6.29 / 6.31 / 6.33" became "In the figure", "Observe Fig. 6.30" became "Observe the figure", "(see Fig. 6.32)" became "(see the figure)". The three parts of the medians example build on each other, so it stays one concept. In its solution the old chunk reads "2AM/CA = 2PN/RP"; the book's step is 2AM/2PN = CA/RP, and that is what is shown. Please check in review.)*

---

## T10 · Questions: Similarity Criteria

Objectives for this set: O21 (apply) pick out similar triangles in a figure, name the criterion and write the similarity with the vertices in the right order; O22 (evaluate) write multi-step proofs with the AA, SSS and SAS criteria; O23 (analyze) solve a shadow problem and a median problem with similar triangles.

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, statement only (or the book's own figure only), no working and no answer. There is no video. Hint, solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for all 19.
The questions are in book order. The four parts of the seventh question are independent tasks, so each is its own concept. The first question's six figure pairs are one task with one figure, so it stays one concept. The ninth question stays one concept because part (ii) is read off the similarity in part (i). The tenth question stays one concept because its parts build on each other: the ratio in part (i) comes from the similarity in part (iii). Please check these two in review.

### C48 · Similarity Criteria, Q1
`objectives: O21` · Media: new image spec (**the book's own figure only**, as it supplies the six pairs of triangles)
> State which pairs of triangles in the figure are similar. Write the similarity criterion used by you for answering the question and also write the pairs of similar triangles in the symbolic form.

### C49 · Similarity Criteria, Q2
`objectives: O21` · Media: new image spec (**the book's own figure only**, as it shows how the triangles sit)
> In the figure, △ODC ~ △OBA, ∠BOC = 125° and ∠CDO = 70°. Find ∠DOC, ∠DCO and ∠OAB.

### C50 · Similarity Criteria, Q3
`objectives: O22` · Media: new image spec (statement only)
> Diagonals AC and BD of a trapezium ABCD with AB ∥ DC intersect each other at the point O. Using a similarity criterion for two triangles, show that OA/OC = OB/OD.

### C51 · Similarity Criteria, Q4
`objectives: O22` · Media: new image spec (**the book's own figure only**, as it marks ∠1 and ∠2)
> In the figure, QR/QS = QT/PR and ∠1 = ∠2. Show that △PQS ~ △TQR.

### C52 · Similarity Criteria, Q5
`objectives: O22` · Media: new image spec (statement only)
> S and T are points on sides PR and QR of △PQR such that ∠P = ∠RTS. Show that △RPQ ~ △RTS.

### C53 · Similarity Criteria, Q6
`objectives: O22` · Media: new image spec (**the book's own figure only**, as it shows how the triangles sit)
> In the figure, if △ABE ≅ △ACD, show that △ADE ~ △ABC.

### C54 · Similarity Criteria, Q7 (i)
`objectives: O22` · Media: new image spec (**the book's own figure only**, as it shows the altitudes and their meeting point)
> In the figure, altitudes AD and CE of △ABC intersect each other at the point P. Show that:
> (i) △AEP ~ △CDP

### C55 · Similarity Criteria, Q7 (ii)
`objectives: O22` · Media: new image spec (**the book's own figure only**, as it shows the altitudes and their meeting point)
> In the figure, altitudes AD and CE of △ABC intersect each other at the point P. Show that:
> (ii) △ABD ~ △CBE

### C56 · Similarity Criteria, Q7 (iii)
`objectives: O22` · Media: new image spec (**the book's own figure only**, as it shows the altitudes and their meeting point)
> In the figure, altitudes AD and CE of △ABC intersect each other at the point P. Show that:
> (iii) △AEP ~ △ADB

### C57 · Similarity Criteria, Q7 (iv)
`objectives: O22` · Media: new image spec (**the book's own figure only**, as it shows the altitudes and their meeting point)
> In the figure, altitudes AD and CE of △ABC intersect each other at the point P. Show that:
> (iv) △PDC ~ △BEC

### C58 · Similarity Criteria, Q8
`objectives: O22` · Media: new image spec (statement only)
> E is a point on the side AD produced of a parallelogram ABCD and BE intersects CD at F. Show that △ABE ~ △CFB.

### C59 · Similarity Criteria, Q9
`objectives: O22` · Media: new image spec (**the book's own figure only**, as it shows how the two right triangles sit)
> In the figure, ABC and AMP are two right triangles, right angled at B and M respectively. Prove that:
> (i) △ABC ~ △AMP
> (ii) CA/PA = BC/MP

### C60 · Similarity Criteria, Q10
`objectives: O22` · Media: new image spec (statement only)
> CD and GH are respectively the bisectors of ∠ACB and ∠EGF such that D and H lie on sides AB and FE of △ABC and △EFG respectively. If △ABC ~ △FEG, show that:
> (i) CD/GH = AC/FG
> (ii) △DCB ~ △HGE
> (iii) △DCA ~ △HGF

### C61 · Similarity Criteria, Q11
`objectives: O22` · Media: new image spec (**the book's own figure only**, as it shows the produced side and the perpendiculars)
> In the figure, E is a point on side CB produced of an isosceles triangle ABC with AB = AC. If AD ⊥ BC and EF ⊥ AC, prove that △ABD ~ △ECF.

### C62 · Similarity Criteria, Q12
`objectives: O22` · Media: new image spec (**the book's own figure only**, as it shows the two triangles and their medians)
> Sides AB and BC and median AD of a triangle ABC are respectively proportional to sides PQ and QR and median PM of △PQR (see the figure). Show that △ABC ~ △PQR.

### C63 · Similarity Criteria, Q13
`objectives: O22` · Media: new image spec (statement only)
> D is a point on the side BC of a triangle ABC such that ∠ADC = ∠BAC. Show that CA² = CB.CD.

### C64 · Similarity Criteria, Q14
`objectives: O22` · Media: new image spec (statement only)
> Sides AB and AC and median AD of a triangle ABC are respectively proportional to sides PQ and PR and median PM of another triangle PQR. Show that △ABC ~ △PQR.

### C65 · Similarity Criteria, Q15
`objectives: O23` · Media: new image spec (statement only)
> A vertical pole of length 6 m casts a shadow 4 m long on the ground and at the same time a tower casts a shadow 28 m long. Find the height of the tower.

### C66 · Similarity Criteria, Q16
`objectives: O23` · Media: new image spec (statement only)
> If AD and PM are medians of triangles ABC and PQR, respectively where △ABC ~ △PQR, prove that AB/PQ = AD/PM.

*(Cleanup for this set: "In Fig. 6.34 to 6.40" became "in the figure" or "In the figure"; "(see Fig. 6.41)" became "(see the figure)".)*

---

# M4 · Wrap-up

## T11 · Chapter Summary

### C67 · Chapter summary
`kind: summary` · `objectives: O24, O25`
Media: existing video "Chapter 6 Recap: All Five Similarity Criteria in 120 Seconds" (old T16 VID1) [title carries a book number, renamed at build]; existing image "Chapter 6 Summary Infographic: Similarity Criteria Reference Card" (old T16 O1.E1) [title carries a book number, renamed at build; its card also prints theorem numbers, please check in review]

[summary_points]
> In this chapter you have studied the following points :
> 1. Two figures having the same shape but not necessarily the same size are called similar figures.
> 2. All the congruent figures are similar but the converse is not true.
> 3. Two polygons of the same number of sides are similar, if (i) their corresponding angles are equal and (ii) their corresponding sides are in the same ratio (i.e., proportion).
> 4. If a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, then the other two sides are divided in the same ratio.
> 5. If a line divides any two sides of a triangle in the same ratio, then the line is parallel to the third side.
> 6. If in two triangles, corresponding angles are equal, then their corresponding sides are in the same ratio and hence the two triangles are similar (AAA similarity criterion).
> 7. If in two triangles, two angles of one triangle are respectively equal to the two angles of the other triangle, then the two triangles are similar (AA similarity criterion).
> 8. If in two triangles, corresponding sides are in the same ratio, then their corresponding angles are equal and hence the triangles are similar (SSS similarity criterion).
> 9. If one angle of a triangle is equal to one angle of another triangle and the sides including these angles are in the same ratio (proportional), then the triangles are similar (SAS similarity criterion).

### C68 · A note on right triangles
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Two Right Triangles and Their Hypotenuses" — Two right triangles side by side. Triangle ABC has its right angle at B, with hypotenuse AC and side AB marked. Triangle PQR has its right angle at Q, with hypotenuse PR and side PQ marked. The hypotenuses are drawn in one colour and the matching sides in another, with the note AC/PR = AB/PQ beside the figure.

[textbook_text · "A note to the reader"]
> If in two right triangles, hypotenuse and one side of one triangle are proportional to the hypotenuse and one side of the other triangle, then the two triangles are similar. This may be referred to as the RHS Similarity Criterion.
> If you use this criterion, some proofs you meet later will become simpler.

*(Cleanup: the heading "6.5 Summary" was removed; "If you use this criterion in Example 2, Chapter 8, the proof will become simpler" became "If you use this criterion, some proofs you meet later will become simpler".)*

---

# Appendix A · Objectives

Format: ID · bloom level · wording · old objective(s) it carries. "(reworded)" means book numbers were taken out of the wording; the meaning is unchanged.

| ID | Bloom | Objective | Old ID |
|---|---|---|---|
| O1 | understand | Distinguish between congruent and similar figures by comparing their respective properties of shape and size. | T1.O1 |
| O2 | apply | Identify examples of similar figures in real-world contexts such as photographs of the same subject printed at different sizes. | T1.O2 |
| O3 | understand | State the two conditions required for two polygons of the same number of sides to be similar. | T2.O1 |
| O4 | evaluate | Verify whether two given polygons are similar by checking equality of corresponding angles and proportionality of corresponding sides. | T2.O2 |
| O5 | apply | Apply the definition of similar figures to classify given shapes and complete fill-in-the-blank and identification tasks. | T3.O1 |
| O6 | understand | Explain the proportional relationship that emerges when a line parallel to one side of a triangle intersects the other two sides, using the observations from the parallel-line construction activity. | T4.O1 (reworded) |
| O7 | evaluate | Prove the Basic Proportionality Theorem using the areas of triangles ADE, BDE, and DEC formed by the parallel transversal line. | T5.O1 (reworded) |
| O8 | evaluate | Prove the converse of the Basic Proportionality Theorem by an indirect argument showing that assuming DE is not parallel to BC leads to E and E' coinciding. | T6.O1 (reworded) |
| O9 | apply | Apply the Basic Proportionality Theorem and its converse to prove proportionality results and identify isosceles triangles in multi-step geometric problems. | T7.O1 (reworded) |
| O10 | apply | Apply BPT and its converse to find unknown lengths and verify whether lines are parallel in numerical problems. | T8.O1 |
| O11 | evaluate | Construct geometric proofs using BPT for problems involving trapezoids, mid-points, and intersecting diagonals. | T8.O2 |
| O12 | analyze | Analyse multi-figure configurations to determine which form of BPT applies to each geometric situation. | T8.O3 |
| O13 | understand | Interpret the similarity notation △ABC ~ △DEF and correctly identify vertex correspondences for a pair of similar triangles. | T9.O1 |
| O14 | apply | Apply the AAA similarity criterion and its AA corollary to determine whether two triangles are similar given angle information. | T9.O2 |
| O15 | evaluate | Prove the SSS similarity criterion by constructing an auxiliary triangle congruent to the smaller triangle and applying BPT to establish angle equality. | T10.O1 (reworded) |
| O16 | evaluate | Prove the SAS similarity criterion and distinguish it from the SAS congruency criterion by identifying the differing condition. | T11.O1 (reworded) |
| O17 | apply | Apply AAA, SSS, and SAS similarity criteria to identify similar triangle pairs and find unknown angles or side ratios in geometric figures. | T12.O1 |
| O18 | apply | Solve real-world indirect measurement problems involving heights and shadows using the AA similarity criterion for triangles. | T13.O1 |
| O19 | analyze | Translate a real-world geometric scenario into a similar triangle relationship and calculate unknown lengths through proportionality. | T13.O2 |
| O20 | apply | Apply SAS similarity to prove △AMC ∼ △PNR using the median-derived proportionality AM/PN = CA/RP and the included angle equality ∠MAC = ∠NPR, then chain the result to prove CM/RN = AB/PQ and to apply SSS similarity to prove △CMB ∼ △RNQ. | T14.O1 (reworded) |
| O21 | apply | Identify similar triangle pairs in a figure of six triangle pairs and state the correct similarity criterion (AA, SSS, or SAS) with the symbolic similarity statement in correct vertex correspondence. | T15.O1 (reworded) |
| O22 | evaluate | Construct multi-step geometric proofs using AAA, SSS, and SAS similarity criteria for configurations involving trapezoids with parallel sides, altitude intersections, isosceles triangles, and proportional medians. | T15.O2 (reworded) |
| O23 | analyze | Solve indirect-measurement problems involving poles and shadows and prove median proportionality in similar triangles using triangle similarity. | T15.O3 (reworded) |
| O24 | understand | Recall the nine key results of the chapter: the definition of similar figures, two polygon similarity conditions, BPT, Converse BPT, AAA similarity criterion, AA corollary, SSS similarity criterion, SAS similarity criterion, and the RHS similarity criterion. | T16.O1 (reworded) |
| O25 | analyze | Distinguish the SAS and SSS similarity criteria from the corresponding SAS and SSS congruency criteria from Class IX by identifying the essential difference: proportional sides in similarity versus equal sides in congruency, with angle conditions preserved in both cases. | T16.O2 (reworded) |

Note: the rewordings remove "Activity 2", "Theorem 6.1" to "Theorem 6.5", "Fig. 6.34", "(Q3–Q14)", "(Q15)", "(Q16)", "Chapter 6" and "Section 6.5". Nothing else changed.

# Appendix B · Held assets (not attached to the new plan; nothing deleted)

**Eight old tools** (no tools in this chapter):
- T1 "Similar vs Congruent Sorter" (T2D1)
- T2 "Polygon Similarity Tester" (T2D1)
- T4 "Basic Proportionality Theorem (Thales) Explorer" (T2D1)
- T8 "Trapezium Diagonal Theorem Visualizer" (T2D1)
- T9 "AAA / AA Similarity Demonstrator" (T2D1)
- T10 "SSS Similarity Verifier" (T2D1)
- T11 "SAS Similarity Tester (included angle)" (T2D1)
- T13 "Indirect Measurement Tool (lamp-post / shadow / Everest)" (T2D1)

**Three old question videos** (no question videos for now):
- "Exercise 6.1 Strategy Walkthrough" (T3 VID1)
- "Q9 Solution: Trapezium Diagonals via Auxiliary Diagonal" (T8 VID1)
- "Q15 Solution: Pole-Shadow Indirect Measurement" (T15 VID1)

**Three old question-set images.** These are the source for the "book's own figure" specs in the question sets. They are held because each question now gets its own hint-free image, and their titles name book figure numbers:
- "Fig. 6.8: Two Quadrilaterals for Q3 Classification" (T3 O1.E1)
- "Reference Diagrams: Figs. 6.17 and 6.18 (Q1 and Q2)" (T8 O1.E1). Its description gives the second question's values for the second figure; the book uses that figure for the first question's part (ii). Please check in review.
- "Fig. 6.34: Six Triangle Pairs for Q1 Classification" (T15 O1.E1)

Totals: 42 old media = 28 attached + 14 held (8 tools, 3 videos, 3 images).

# Appendix C · Carried-over fields

Every old topic's `recall_questions`, `summary`, `key_terms`, `concept_bullets` and `detailed_summary` carry into the new topic that holds its text. They are not shown here, to keep this file reviewable. The nothing-deleted check at build time compares them field by field. The table gives, for each old topic, the new concepts that hold its text; the first concept named decides the new topic.

| Old topic | New concepts |
|---|---|
| T1 Introduction to Similar Figures | C1, C2 |
| T2 Similar Polygons | C3, C4, C5, C6 |
| T3 Exercise 6.1 | C7 to C13 |
| T4 Basic Proportionality Theorem: discovery | C14 |
| T5 Basic Proportionality Theorem: proof | C15 |
| T6 Converse of the Basic Proportionality Theorem | C16, C17, C18 |
| T7 Worked Examples 1 to 3 | C19, C20, C21 |
| T8 Exercise 6.2 | C22 to C34 |
| T9 Similarity notation and the AAA criterion | C35, C36, C37 |
| T10 SSS similarity criterion | C38, C39 |
| T11 SAS similarity criterion | C40, C41, C42 |
| T12 Worked Examples 4 to 6 | C43, C44, C45 |
| T13 Worked Example 7 | C46 |
| T14 Worked Example 8 | C47 |
| T15 Exercise 6.3 | C48 to C66 |
| T16 Summary and Chapter Review | C67, C68 |
