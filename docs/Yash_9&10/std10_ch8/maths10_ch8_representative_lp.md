# Representative learning plan: Class 10, Introduction to Trigonometry (maths10_ch8)

A review copy of the restructured plan, down to concept level. Content is shown in full. Media are only named and never embedded.

Source: `learning_plan_std10_chap8_version1.json`. Shape follows the Class 9 circles plan and the Class 10 coordinate geometry plan.

## Read this first

**Standing decisions**
- No tools in this chapter. The seven old `2d_tool` items are held (Appendix B).
- No videos for exercise questions. Each question concept gets one hint-free image spec and no video. The three old exercise videos are held (Appendix B).
- Examples keep the existing videos and images that match them. No new example media is planned.
- No grouping inside the question topics. Each textbook question is its own concept, in textbook order, named "<set name>, Q<n>". A question with separate lettered sub-parts is split: each sub-part is its own concept, named "<set name>, Q<n> (<roman>)", and keeps its parent question's objective. No question in this chapter has sub-parts that build on each other, so none is kept whole for that reason.
- The textbook has three exercise sets and no starred or end-of-chapter set. All three are included, each with its own new name.
- The book proves four results: that the ratios do not depend on the size of the triangle, and the three identities. Each becomes a try concept (statement and a prediction) followed by its prove concept. The values for 45°, 30°, 60°, 0° and 90° are worked out in the book as calculations, not stated and proved, so they are teach concepts.

**What a concept entry shows**
- `kind`: try, prove, teach, enrich, hook, exercise or summary.
- `objectives`: objective IDs. Enrichment concepts have none.
- `media`: existing assets re-homed from the old plan, new asset specs, or none. Where the old title carries a book number (Fig., Table or Example), it is shown as found and is cleaned at build.
- `[block_kind]` tags are review labels only. They never reach the student.

**Text cleanup applied to everything below**
- "Fig. 8.x", "see Fig. 8.x" and "as shown in Fig. 8.x" are removed. The figure is carried by the image.
- "Table 8.1" becomes "the table below" or "the table of values".
- "Section 8.1" becomes "earlier", and "From Chapter 6" becomes "From your earlier work on triangles".
- "Theorem 6.4" becomes "the SSS similarity criterion", which is what that theorem states.
- "Example n:" and "Exercise 8.x" labels are removed. The equation numbers "(1)", "(2)" inside a working stay, because they belong to the working.
- Fractions and roots that the book prints in stacked form are written on one line, for example 2√2 k/3k and (1 – tan²A)/(1 + tan²A).
- Book references stay only in metadata (`ncert_refs`), which is not shown here.

**Marked in the text**
- `[authored]` marks text that is not in the old plan or the book. These are predictions, answers to "(Why?)" prompts and the one new objective (O35). Reworded old objectives are marked "reworded" in Appendix A.
- Question solutions (`steps` and `answer`) are not in the old plan. They are marked *to author* and nothing is invented here.

## Plan at a glance

| Module | Topic | Concepts |
|---|---|---|
| M1 Trigonometric ratios | T1 Right Triangles Around Us (hook) | C1–C2 |
|  | T2 The Six Trigonometric Ratios | C3–C6 |
|  | T3 Ratios Depend Only on the Angle | C7–C9 |
|  | T4 From One Ratio to All Six | C10–C11 |
|  | T5 Examples: Ratios From Given Information | C12–C17 |
|  | T6 Questions: Trigonometric Ratios | C18–C35 |
| M2 Ratios of specific angles | T7 Ratios of 45° | C36–C37 |
|  | T8 Ratios of 30° and 60° | C38–C39 |
|  | T9 Ratios of 0° and 90° | C40–C42 |
|  | T10 The Table of Standard Values | C43 |
|  | T11 Examples: Using the Standard Values | C44–C47 |
|  | T12 Questions: Standard Angles | C48–C62 |
| M3 Trigonometric identities | T13 The First Identity | C63–C64 |
|  | T14 Examples: One Ratio in Terms of Another | C65–C66 |
|  | T15 The Second Identity | C67–C69 |
|  | T16 The Third Identity | C70–C71 |
|  | T17 Examples: Proving Identities | C72–C74 |
|  | T18 Questions: Trigonometric Identities | C75–C90 |
| M4 Wrap-up | T19 Chapter Summary | C91 |

Totals: 4 modules, 19 topics, 91 concepts and 35 objectives (34 old, 1 new). 49 question concepts (18 + 15 + 16) need a new image. 0 new videos. 12 worked examples. 4 try/prove pairs (TH1–TH4).

Old media: 48 (18 videos, 23 images, 7 tools). Attached: 37 (15 videos, 22 images). Held: 11 (7 tools, 3 exercise videos, 1 image).

---

# M1 · Trigonometric ratios

## T1 · Right Triangles Around Us (hook)

### C1 · Heights and distances without measuring
`kind: hook` · `is_enrichment: true` · `objectives: none`
Media: existing video "Trigonometry in Everyday Right Triangles" (old T1 VID1)

[textbook_text]
> There is perhaps nothing which so occupies the middle position of mathematics as trigonometry.
> – J.F. Herbart (1890)
>
> You have already studied about triangles, and in particular, right triangles, in your earlier classes. Let us take some examples from our surroundings where right triangles can be imagined to be formed. For instance :
> 1. Suppose the students of a school are visiting Qutub Minar. Now, if a student is looking at the top of the Minar, a right triangle can be imagined to be made. Can the student find out the height of the Minar, without actually measuring it?
> 2. Suppose a girl is sitting on the balcony of her house located on the bank of a river. She is looking down at a flower pot placed on a stair of a temple situated nearby on the other bank of the river. A right triangle is imagined to be made in this situation. If you know the height at which the person is sitting, can you find the width of the river?
> 3. Suppose a hot air balloon is flying in the air. A girl happens to spot the balloon in the sky and runs to her mother to tell her about it. Her mother rushes out of the house to look at the balloon. Now when the girl had spotted the balloon initially it was at point A. When both the mother and daughter came out to see it, it had already travelled to another point B. Can you find the altitude of B from the ground?

*(Cleanup: the section heading and the two "as shown in Fig. 8.x" phrases are dropped. The book's misspelling "intially" is corrected. No words dropped otherwise.)*

### C2 · What trigonometry studies
`kind: teach` · `objectives: O1, O2`
Media: existing image "Qutab Minar Right Triangle Setup" (old T1 O2.E1); existing image "Wheelchair Ramp as a Right Triangle" (old T1 O1.E1). The ramp is not one of the book's situations (the old plan added it), so the fit is loose, please check.

[textbook_text]
> In all the situations given above, the distances or heights can be found by using some mathematical techniques, which come under a branch of mathematics called 'trigonometry'. The word 'trigonometry' is derived from the Greek words 'tri' (meaning three), 'gon' (meaning sides) and 'metron' (meaning measure). In fact, trigonometry is the study of relationships between the sides and angles of a triangle. The earliest known work on trigonometry was recorded in Egypt and Babylon. Early astronomers used it to find out the distances of the stars and planets from the Earth. Even today, most of the technologically advanced methods used in Engineering and Physical Sciences are based on trigonometrical concepts.
>
> In this chapter, we will study some ratios of the sides of a right triangle with respect to its acute angles, called trigonometric ratios of the angle. We will restrict our discussion to acute angles only. However, these ratios can be extended to other angles also. We will also define the trigonometric ratios for angles of measure 0° and 90°. We will calculate trigonometric ratios for some specific angles and establish some identities involving these ratios, called trigonometric identities.

---

## T2 · The Six Trigonometric Ratios

### C3 · Opposite, adjacent and hypotenuse
`kind: teach` · `objectives: O4`
Media: existing image "Angle C Perspective — Swapped Opposite and Adjacent (Fig. 8.5 style)" (old T2 O1.E1) [title carries a book number, cleaned at build]

[textbook_text]
> Earlier, you have seen some right triangles imagined to be formed in different situations.
> Let us take a right triangle ABC.
> Here, ∠ CAB (or, in brief, angle A) is an acute angle. Note the position of the side BC with respect to angle A. It faces ∠ A. We call it the side opposite to angle A. AC is the hypotenuse of the right triangle and the side AB is a part of ∠ A. So, we call it the side adjacent to angle A.
> Note that the position of sides change when you consider angle C in place of A.

*(Cleanup: "In Section 8.1" becomes "Earlier", "as shown in Fig. 8.4" and "(see Fig. 8.5)" are dropped.)*

### C4 · The six ratios of an acute angle
`kind: teach` · `objectives: O3, O4`
Media: existing image "Right Triangle ABC with All Six Ratio Labels (Fig. 8.4 style)" (old T2 O2.E1) [title carries a book number, cleaned at build]

[textbook_text]
> You have studied the concept of 'ratio' in your earlier classes. We now define certain ratios involving the sides of a right triangle, and call them trigonometric ratios.
> The trigonometric ratios of the angle A in right triangle ABC are defined as follows :
> sine of ∠ A = (side opposite to angle A)/(hypotenuse) = BC/AC
> cosine of ∠ A = (side adjacent to angle A)/(hypotenuse) = AB/AC
> tangent of ∠ A = (side opposite to angle A)/(side adjacent to angle A) = BC/AB
> cosecant of ∠ A = 1/(sine of ∠ A) = (hypotenuse)/(side opposite to angle A) = AC/BC
> secant of ∠ A = 1/(cosine of ∠ A) = (hypotenuse)/(side adjacent to angle A) = AC/AB
> cotangent of ∠ A = 1/(tangent of ∠ A) = (side adjacent to angle A)/(side opposite to angle A) = AB/BC
> The ratios defined above are abbreviated as sin A, cos A, tan A, cosec A, sec A and cot A respectively. Note that the ratios cosec A, sec A and cot A are respectively, the reciprocals of the ratios sin A, cos A and tan A.
> Also, observe that tan A = BC/AB = (BC/AC)/(AB/AC) = sin A/cos A and cot A = cos A/sin A.
> So, the trigonometric ratios of an acute angle in a right triangle express the relationship between the angle and the length of its sides.
> Why don't you try to define the trigonometric ratios for angle C in the right triangle?

[remark, from source]
> Note that the symbol sin A is used as an abbreviation for 'the sine of the angle A'. sin A is not the product of 'sin' and A. 'sin' separated from A has no meaning. Similarly, cos A is not the product of 'cos' and A. Similar interpretations follow for other trigonometric ratios also.

*(Cleanup: "(see Fig. 8.4)" and "(See Fig. 8.5)" are dropped. The book prints the remark after the history box on Aryabhata; it is moved up here so that the definitions and the note on the notation stay together, and the history box follows as the next concept. No words dropped.)*

### C5 · Where the word "sine" comes from
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: existing video "Aryabhata and the Origin of the Word Sine" (old T2 VID1)

[textbook_text · history box]
> The first use of the idea of 'sine' in the way we use it today was in the work Aryabhatiyam by Aryabhata, in A.D. 500. Aryabhata used the word ardha-jya for the half-chord, which was shortened to jya or jiva in due course. When the Aryabhatiyam was translated into Arabic, the word jiva was retained as it is. The word jiva was translated into sinus, which means curve, when the Arabic version was translated into Latin. Soon the word sinus, also used as sine, became common in mathematical texts throughout Europe. An English Professor of astronomy Edmund Gunter (1581–1626), first used the abbreviated notation 'sin'.
>
> The origin of the terms 'cosine' and 'tangent' was much later. The cosine function arose from the need to compute the sine of the complementary angle. Aryabhatta called it kotijya. The name cosinus originated with Edmund Gunter. In 1674, the English Mathematician Sir Jonas Moore first used the abbreviated notation 'cos'.

### C6 · More to explore: the ratios for angle C
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Sides seen from angle C" — A right triangle ABC with the right angle at B. Angle C is marked with an arc at vertex C. The side AB is labelled 'side facing angle C', the side BC is labelled 'side touching angle C' and the side AC is labelled 'hypotenuse'.

[enrichment] `[authored answer]`
> **Q.** In the right triangle ABC, right-angled at B, define the six trigonometric ratios for angle C.
> **A.** For angle C, the side opposite is AB, the side adjacent is BC and the hypotenuse is still AC. So sin C = AB/AC, cos C = BC/AC, tan C = AB/BC, cosec C = AC/AB, sec C = AC/BC and cot C = BC/AB.

---

## T3 · Ratios Depend Only on the Angle

### C7 · Does a bigger triangle change the ratios? Try it first
`kind: try` · `objectives: O6`
Media: existing image "Three Similar Triangles on Hypotenuse AC — Fig. 8.6 Style" (old T3 O1.E1) [title carries a book number, cleaned at build]
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[textbook_text]
> Now, if we take a point P on the hypotenuse AC or a point Q on AC extended, of the right triangle ABC and draw PM perpendicular to AB and QN perpendicular to AB extended, how will the trigonometric ratios of ∠ A in △ PAM differ from those of ∠ A in △ CAB or from those of ∠ A in △ QAN?

[theorem_statement] *(the book's own conclusion sentence, from the end of the next concept)*
> The values of the trigonometric ratios of an angle do not vary with the lengths of the sides of the triangle, if the angle remains the same.

[predict] `[authored]`
> △ PAM is smaller than △ CAB, and △ QAN is bigger, but all three have the same angle A. Guess before reading on: is sin A in the small triangle smaller than, equal to or larger than sin A in the big triangle? Commit to an answer. The next concept settles it.

### C8 · Why the ratios stay the same
`kind: prove` · `objectives: O5, O6`
Media: existing video "AA Similarity Proof — Invariance of Trigonometric Ratios" (old T3 VID1)

[textbook_text]
> To answer this, first look at these triangles. Is △ PAM similar to △ CAB? From your earlier work on triangles, recall the AA similarity criterion. Using the criterion, you will see that the triangles PAM and CAB are similar. Therefore, by the property of similar triangles, the corresponding sides of the triangles are proportional.
> So, we have
> AM/AB = AP/AC = MP/BC
> From this, we find
> MP/AP = BC/AC = sin A.
> Similarly,
> AM/AP = AB/AC = cos A, MP/AM = BC/AB = tan A and so on.
> This shows that the trigonometric ratios of angle A in △ PAM not differ from those of angle A in △ CAB.
> In the same way, you should check that the value of sin A (and also of other trigonometric ratios) remains the same in △ QAN also.
> From our observations, it is now clear that the values of the trigonometric ratios of an angle do not vary with the lengths of the sides of the triangle, if the angle remains the same.

[remark, from source]
> For the sake of convenience, we may write sin²A, cos²A, etc., in place of (sin A)², (cos A)², etc., respectively. But cosec A = (sin A)⁻¹ ≠ sin⁻¹ A (it is called sine inverse A). sin⁻¹ A has a different meaning, which will be discussed in higher classes. Similar conventions hold for the other trigonometric ratios as well. Sometimes, the Greek letter θ (theta) is also used to denote an angle.

*(Cleanup: "(see Fig. 8.6)" is dropped from the opening question in the try concept, and "From Chapter 6" becomes "From your earlier work on triangles". The book's "not differ" is kept as printed. The book's "Note :" label becomes the remark tag. The image of the three triangles sits on the try concept, because it shows the set-up the question asks about.)*

### C9 · More to explore: the bigger triangle
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "A bigger triangle on the same angle" — A ray from A along AB extended and a ray along AC extended. Right triangle CAB (right angle at B) sits inside a larger triangle QAN, where Q is a point on AC extended beyond C and N is on AB extended beyond B with QN perpendicular to AB. Both right angles are marked and the shared angle A is shaded in both triangles.

[enrichment] `[authored answer]`
> **Q.** The book asks you to check that sin A stays the same in △ QAN, where Q is on AC extended and QN is perpendicular to AB extended. How?
> **A.** △ QAN and △ CAB share angle A, and ∠ QNA = ∠ CBA = 90°. So by the AA criterion they are similar, and AN/AB = AQ/AC = QN/BC. Therefore QN/AQ = BC/AC = sin A, and in the same way AN/AQ = cos A and QN/AN = tan A.

---

## T4 · From One Ratio to All Six

### C10 · Knowing one ratio gives all six
`kind: teach` · `objectives: O7`
Media: new image spec "A triangle built from sin A = 1/3" — A right triangle ABC with the right angle at B and angle A marked. The side BC is labelled k, the hypotenuse AC is labelled 3k, and the third side AB is labelled 2√2 k. A small caption beside the triangle reads sin A = BC/AC = 1/3.

[textbook_text]
> We have defined six trigonometric ratios of an acute angle. If we know any one of the ratios, can we obtain the other ratios? Let us see.
> If in a right triangle ABC, sin A = 1/3, then this means that BC/AC = 1/3, i.e., the lengths of the sides BC and AC of the triangle ABC are in the ratio 1 : 3. So if BC is equal to k, then AC will be 3k, where k is any positive number. To determine other trigonometric ratios for the angle A, we need to find the length of the third side AB. Do you remember the Pythagoras theorem? Let us use it to determine the required length AB.
> AB² = AC² – BC² = (3k)² – (k)² = 8k² = (2√2 k)²
> Therefore, AB = ± 2√2 k
> So, we get AB = 2√2 k (Why is AB not – 2√2 k ?)
> Now, cos A = AB/AC = 2√2 k/3k = 2√2/3
> Similarly, you can obtain the other trigonometric ratios of the angle A.

[remark, from source]
> Since the hypotenuse is the longest side in a right triangle, the value of sin A or cos A is always less than 1 (or, in particular, equal to 1).
> Let us consider some examples.

*(Cleanup: "(see Fig. 8.7)" is dropped. The old plan repeats this remark in its first-identity topic; it is kept in both places, see the first-identity proof.)*

### C11 · More to explore: finishing the job
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Sides of the 1 : 3 triangle" — A right triangle ABC with the right angle at B and angle A marked. The side BC is labelled k, the hypotenuse AC is labelled 3k and the side AB is labelled 2√2 k. A small side panel shows a ruler with a length measured only on the positive side of zero.

[enrichment] `[authored answers]`
> **Q.** Why is AB not –2√2 k?
> **A.** AB is the length of a side, and a length is never negative. So we keep only the positive square root.

[enrichment] `[authored answers]`
> **Q.** For sin A = 1/3, find the other ratios of angle A.
> **A.** With BC = k, AC = 3k and AB = 2√2 k: tan A = BC/AB = 1/(2√2), cosec A = AC/BC = 3, sec A = AC/AB = 3/(2√2) and cot A = AB/BC = 2√2.

---

## T5 · Examples: Ratios From Given Information

### C12 · All six ratios from tan A
`kind: exercise (worked example)` · `objectives: O7`
Media: existing video "Worked Walkthrough: Six Ratios from a Given tan A" (old T4 VID1); existing image "Right Triangle ABC with tan A = 4/3 — Sides 3k, 4k, 5k" (old T4 O1.E1)

[question]
> Given tan A = 4/3, find the other trigonometric ratios of the angle A.

[worked solution, from source]
> Let us first draw a right △ ABC.
> Now, we know that tan A = BC/AB = 4/3.
> Therefore, if BC = 4k, then AB = 3k, where k is a positive number.
> Now, by using the Pythagoras Theorem, we have
> AC² = AB² + BC² = (4k)² + (3k)² = 25k²
> So, AC = 5k
> Now, we can write all the trigonometric ratios using their definitions.
> sin A = BC/AC = 4k/5k = 4/5
> cos A = AB/AC = 3k/5k = 3/5
> Therefore, cot A = 1/tan A = 3/4, cosec A = 1/sin A = 5/4 and sec A = 1/cos A = 5/3.

### C13 · Equal sines mean equal angles
`kind: exercise (worked example)` · `objectives: O8`
Media: existing image "Equal-Sine Proof Setup — Two Right Triangles ABC and PQR" (old T4 O2.E1)

[question]
> If ∠ B and ∠ Q are acute angles such that sin B = sin Q, then prove that ∠ B = ∠ Q.

[worked solution, from source]
> Let us consider two right triangles ABC and PQR where sin B = sin Q.
> We have sin B = AC/AB and sin Q = PR/PQ
> Then AC/AB = PR/PQ
> Therefore, AC/PR = AB/PQ = k, say    (1)
> Now, using Pythagoras theorem,
> BC = √(AB² – AC²) and QR = √(PQ² – PR²)
> So, BC/QR = √(AB² – AC²)/√(PQ² – PR²) = √(k²PQ² – k²PR²)/√(PQ² – PR²) = k√(PQ² – PR²)/√(PQ² – PR²) = k    (2)
> From (1) and (2), we have
> AC/PR = AB/PQ = BC/QR
> Then, by using the SSS similarity criterion, △ ACB ~ △ PRQ and therefore, ∠ B = ∠ Q.

*(Cleanup: "(see Fig. 8.9)" is dropped, and "Theorem 6.4" becomes "the SSS similarity criterion", which is what that theorem states.)*

### C14 · Squares of sine and cosine in a 20-21-29 triangle
`kind: exercise (worked example)` · `objectives: O7`
Media: new image spec "Right triangle with hypotenuse 29 units" — A right triangle ACB with the right angle at C. The hypotenuse AB is labelled 29 units, the side BC is labelled 21 units, and the angle at B is marked θ. The side AC is drawn with a question mark in place of its length.

[question]
> Consider △ ACB, right-angled at C, in which AB = 29 units, BC = 21 units and ∠ ABC = θ. Determine the values of
> (i) cos²θ + sin²θ,
> (ii) cos²θ – sin²θ.

[worked solution, from source]
> In △ ACB, we have
> AC = √(AB² – BC²) = √((29)² – (21)²) = √((29 – 21)(29 + 21)) = √((8)(50)) = √400 = 20 units
> So, sin θ = AC/AB = 20/29, cos θ = BC/AB = 21/29.
> Now, (i) cos²θ + sin²θ = (20/29)² + (21/29)² = (20² + 21²)/29² = (400 + 441)/841 = 1,
> and (ii) cos²θ – sin²θ = (21/29)² – (20/29)² = (21 + 20)(21 – 20)/29² = 41/841.

*(Cleanup: "(see Fig. 8.10)" is dropped. The two parts share one working in the book, so they stay one concept.)*

### C15 · Checking 2 sin A cos A when tan A = 1
`kind: exercise (worked example)` · `objectives: O7`
Media: new image spec "Right triangle where tan A equals 1" — A right triangle ABC with the right angle at B and angle A marked at vertex A. A caption beside it reads tan A = 1. The sides AB and BC are drawn without any measurements.

[question]
> In a right triangle ABC, right-angled at B, if tan A = 1, then verify that 2 sin A cos A = 1.

[worked solution, from source]
> In △ ABC, tan A = BC/AB = 1
> i.e., BC = AB
> Let AB = BC = k, where k is a positive number.
> Now, AC = √(AB² + BC²) = √((k)² + (k)²) = k√2
> Therefore, sin A = BC/AC = 1/√2 and cos A = AB/AC = 1/√2
> So, 2 sin A cos A = 2(1/√2)(1/√2) = 1, which is the required value.

### C16 · A triangle given one side and a difference
`kind: exercise (worked example)` · `objectives: O7`
Media: new image spec "A right triangle with a 7 cm side" — A right triangle OPQ with the right angle at P. The side OP is labelled 7 cm, and the sides PQ and OQ are drawn with question marks. A note beside the triangle reads OQ – PQ = 1 cm, and a small bracket shows that OQ is the length PQ plus an extra 1 cm.

[question]
> In △ OPQ, right-angled at P, OP = 7 cm and OQ – PQ = 1 cm. Determine the values of sin Q and cos Q.

[worked solution, from source]
> In △ OPQ, we have
> OQ² = OP² + PQ²
> i.e., (1 + PQ)² = OP² + PQ²    (Why?)
> i.e., 1 + PQ² + 2PQ = OP² + PQ²
> i.e., 1 + 2PQ = 7²    (Why?)
> i.e., PQ = 24 cm and OQ = 1 + PQ = 25 cm
> So, sin Q = 7/25 and cos Q = 24/25.

### C17 · More to explore: the "Why?" prompts in these examples
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Reading the working in triangle OPQ" — A right triangle OPQ with the right angle at P and OP = 7 cm. The hypotenuse OQ is drawn as a bar made of two parts, one part equal to PQ and a short extra part labelled 1 cm. Beside it, the sides OP, PQ and OQ are shown as squares on each side of the triangle, labelled OP², PQ² and OQ².

[enrichment] `[authored answers]`
> **Q.** In the triangle OPQ, why can we write (1 + PQ)² in place of OQ²?
> **A.** We are told that OQ – PQ = 1, so OQ = 1 + PQ, and therefore OQ² = (1 + PQ)².

[enrichment] `[authored answers]`
> **Q.** Why does 1 + PQ² + 2PQ = OP² + PQ² become 1 + 2PQ = 7²?
> **A.** PQ² appears on both sides, so it cancels. What is left is 1 + 2PQ = OP², and OP = 7 cm, so OP² = 7².

---

## T6 · Questions: Trigonometric Ratios

Objectives for this set: O9 (apply) compute trigonometric ratios from given side lengths or ratio values (Q1–Q5, Q7–Q10); O8 (evaluate) show that equal values of a ratio for two acute angles mean the angles are equal (Q6); O10 (evaluate) verify or disprove statements about the range of the ratios (Q11 (ii), (v)); O11 (analyze) classify statements about tan A, cos A and cot A as true or false with justification (Q11 (i), (iii), (iv)).

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, statement only (for a split question, the stem and that one sub-part), no working and no answer. Only Q2 comes with its own book figure; its image shows that figure alone. The book prints no hint for any of these questions. There is no video. Solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for all 18.
The questions are in textbook order. The sub-parts of Q1, Q7, Q9 and Q11 are independent tasks, so each is its own concept.

### C18 · Trigonometric Ratios, Q1 (i)
`objectives: O9` · Media: new image spec (statement and this sub-part only)
> In △ ABC, right-angled at B, AB = 24 cm, BC = 7 cm. Determine :
> (i) sin A, cos A

### C19 · Trigonometric Ratios, Q1 (ii)
`objectives: O9` · Media: new image spec (statement and this sub-part only)
> In △ ABC, right-angled at B, AB = 24 cm, BC = 7 cm. Determine :
> (ii) sin C, cos C

### C20 · Trigonometric Ratios, Q2
`objectives: O9` · Media: new image spec (**the book's own figure only**, as it supplies the triangle PQR and its side lengths)
> In the figure, find tan P – cot R.

### C21 · Trigonometric Ratios, Q3
`objectives: O9` · Media: new image spec (statement only)
> If sin A = 3/4, calculate cos A and tan A.

### C22 · Trigonometric Ratios, Q4
`objectives: O9` · Media: new image spec (statement only)
> Given 15 cot A = 8, find sin A and sec A.

### C23 · Trigonometric Ratios, Q5
`objectives: O9` · Media: new image spec (statement only)
> Given sec θ = 13/12, calculate all other trigonometric ratios.

### C24 · Trigonometric Ratios, Q6
`objectives: O8` · Media: new image spec (statement only)
> If ∠ A and ∠ B are acute angles such that cos A = cos B, then show that ∠ A = ∠ B.

### C25 · Trigonometric Ratios, Q7 (i)
`objectives: O9` · Media: new image spec (statement and this sub-part only)
> If cot θ = 7/8, evaluate :
> (i) ((1 + sin θ)(1 – sin θ))/((1 + cos θ)(1 – cos θ))

### C26 · Trigonometric Ratios, Q7 (ii)
`objectives: O9` · Media: new image spec (statement and this sub-part only)
> If cot θ = 7/8, evaluate :
> (ii) cot²θ

### C27 · Trigonometric Ratios, Q8
`objectives: O9` · Media: new image spec (statement only)
> If 3 cot A = 4, check whether (1 – tan²A)/(1 + tan²A) = cos²A – sin²A or not.

### C28 · Trigonometric Ratios, Q9 (i)
`objectives: O9` · Media: new image spec (statement and this sub-part only)
> In triangle ABC, right-angled at B, if tan A = 1/√3, find the value of:
> (i) sin A cos C + cos A sin C

### C29 · Trigonometric Ratios, Q9 (ii)
`objectives: O9` · Media: new image spec (statement and this sub-part only)
> In triangle ABC, right-angled at B, if tan A = 1/√3, find the value of:
> (ii) cos A cos C – sin A sin C

### C30 · Trigonometric Ratios, Q10
`objectives: O9` · Media: new image spec (statement only)
> In △ PQR, right-angled at Q, PR + QR = 25 cm and PQ = 5 cm. Determine the values of sin P, cos P and tan P.

### C31 · Trigonometric Ratios, Q11 (i)
`objectives: O11` · Media: new image spec (statement and this sub-part only)
> State whether the following are true or false. Justify your answer.
> (i) The value of tan A is always less than 1.

### C32 · Trigonometric Ratios, Q11 (ii)
`objectives: O10` · Media: new image spec (statement and this sub-part only)
> State whether the following are true or false. Justify your answer.
> (ii) sec A = 12/5 for some value of angle A.

### C33 · Trigonometric Ratios, Q11 (iii)
`objectives: O11` · Media: new image spec (statement and this sub-part only)
> State whether the following are true or false. Justify your answer.
> (iii) cos A is the abbreviation used for the cosecant of angle A.

### C34 · Trigonometric Ratios, Q11 (iv)
`objectives: O11` · Media: new image spec (statement and this sub-part only)
> State whether the following are true or false. Justify your answer.
> (iv) cot A is the product of cot and A.

### C35 · Trigonometric Ratios, Q11 (v)
`objectives: O10` · Media: new image spec (statement and this sub-part only)
> State whether the following are true or false. Justify your answer.
> (v) sin θ = 4/3 for some angle θ.

---

# M2 · Ratios of specific angles

## T7 · Ratios of 45°

### C36 · Working out the ratios of 45°
`kind: teach` · `objectives: O12, O13`
Media: existing video "Deriving 45° Ratios from the Isosceles Right Triangle" (old T6 VID1); existing image "Isosceles Right Triangle for 45° Ratios — Fig. 8.14 Style" (old T6 O1.E1) [title carries a book number, cleaned at build]

[textbook_text]
> From geometry, you are already familiar with the construction of angles of 30°, 45°, 60° and 90°. Now, we will find the values of the trigonometric ratios for these angles and, of course, for 0°.
>
> In △ ABC, right-angled at B, if one angle is 45°, then the other angle is also 45°, i.e., ∠ A = ∠ C = 45°.
> So, BC = AB (Why?)
> Now, Suppose BC = AB = a.
> Then by Pythagoras Theorem, AC² = AB² + BC² = a² + a² = 2a²,
> and, therefore, AC = a√2.
> Using the definitions of the trigonometric ratios, we have :
> sin 45° = (side opposite to angle 45°)/(hypotenuse) = BC/AC = a/(a√2) = 1/√2
> cos 45° = (side adjacent to angle 45°)/(hypotenuse) = AB/AC = a/(a√2) = 1/√2
> tan 45° = (side opposite to angle 45°)/(side adjacent to angle 45°) = BC/AB = a/a = 1
> Also, cosec 45° = 1/sin 45° = √2, sec 45° = 1/cos 45° = √2, cot 45° = 1/tan 45° = 1.

*(Cleanup: the section heading "8.3", "In this section" (now "Now") and "(see Fig. 8.14)" are dropped or reworded.)*

### C37 · More to explore: why the legs are equal
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Two 45 degree angles in a right triangle" — A right triangle ABC with the right angle at B. Angles A and C are each marked 45° with arcs. An arrow from angle A points to the side BC facing it and an arrow from angle C points to the side AB facing it.

[enrichment] `[authored answer]`
> **Q.** Why is BC = AB when ∠ A = ∠ C = 45°?
> **A.** In a triangle, the sides opposite equal angles are equal. BC is opposite ∠ A and AB is opposite ∠ C, and the two angles are equal, so BC = AB.

---

## T8 · Ratios of 30° and 60°

### C38 · Working out the ratios of 30° and 60°
`kind: teach` · `objectives: O14, O15`
Media: existing video "Equilateral Triangle Construction for 30° and 60° Ratios" (old T7 VID1); existing image "Bisected Equilateral Triangle Producing 30-60-90 — Fig. 8.15 Style" (old T7 O1.E1) [title carries a book number, cleaned at build]

[textbook_text]
> Let us now calculate the trigonometric ratios of 30° and 60°. Consider an equilateral triangle ABC. Since each angle in an equilateral triangle is 60°, therefore, ∠ A = ∠ B = ∠ C = 60°.
> Draw the perpendicular AD from A to the side BC.
> Now △ ABD ≅ △ ACD (Why?)
> Therefore, BD = DC
> and ∠ BAD = ∠ CAD (CPCT)
> Now observe that:
> △ ABD is a right triangle, right-angled at D with ∠ BAD = 30° and ∠ ABD = 60°.
> As you know, for finding the trigonometric ratios, we need to know the lengths of the sides of the triangle. So, let us suppose that AB = 2a.
> Then, BD = (1/2) BC = a
> and AD² = AB² – BD² = (2a)² – (a)² = 3a²,
> Therefore, AD = a√3
> Now, we have :
> sin 30° = BD/AB = a/2a = 1/2, cos 30° = AD/AB = a√3/2a = √3/2
> tan 30° = BD/AD = a/(a√3) = 1/√3.
> Also, cosec 30° = 1/sin 30° = 2, sec 30° = 1/cos 30° = 2/√3
> cot 30° = 1/tan 30° = √3.
> Similarly,
> sin 60° = AD/AB = a√3/2a = √3/2, cos 60° = 1/2, tan 60° = √3,
> cosec 60° = 2/√3, sec 60° = 2 and cot 60° = 1/√3.

*(Cleanup: two "(see Fig. 8.15)" are dropped.)*

### C39 · More to explore: why the two halves match
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "An equilateral triangle split by a height" — An equilateral triangle ABC with each angle marked 60°. A perpendicular AD is drawn from A to the side BC with a right-angle mark at D, splitting the triangle into the two shaded triangles ABD and ACD. The sides AB and AC and the common side AD are highlighted.

[enrichment] `[authored answer]`
> **Q.** Why is △ ABD ≅ △ ACD?
> **A.** AB = AC, since the triangle is equilateral. AD is common to both triangles. ∠ ADB = ∠ ADC = 90°. So the two right triangles are congruent by the RHS rule.

---

## T9 · Ratios of 0° and 90°

### C40 · What happens as the angle shrinks to 0°
`kind: teach` · `objectives: O16, O17`
Media: existing video "0° and 90° Limiting Arguments — Animated Derivation" (old T8 VID1); existing image "Limiting Triangle Sequence — Angle A Shrinking to 0° (Fig. 8.16–8.17 Style)" (old T8 O1.E1) [title carries a book number, cleaned at build, please check the leftover]

[textbook_text]
> Let us see what happens to the trigonometric ratios of angle A, if it is made smaller and smaller in the right triangle ABC, till it becomes zero. As ∠ A gets smaller and smaller, the length of the side BC decreases. The point C gets closer to point B, and finally when ∠ A becomes very close to 0°, AC becomes almost the same as AB.
> When ∠ A is very close to 0°, BC gets very close to 0 and so the value of sin A = BC/AC is very close to 0. Also, when ∠ A is very close to 0°, AC is nearly the same as AB and so the value of cos A = AB/AC is very close to 1.
> This helps us to see how we can define the values of sin A and cos A when A = 0°. We define : sin 0° = 0 and cos 0° = 1.
> Using these, we have :
> tan 0° = sin 0°/cos 0° = 0, cot 0° = 1/tan 0°, which is not defined. (Why?)
> sec 0° = 1/cos 0° = 1 and cosec 0° = 1/sin 0°, which is again not defined. (Why?)

*(Cleanup: "(see Fig. 8.16)" and "(see Fig. 8.17)" are dropped.)*

### C41 · What happens as the angle grows to 90°
`kind: teach` · `objectives: O16, O17`
Media: new image spec "Angle A opening up towards 90 degrees" — Three right triangles ABC drawn one over the other on the same vertical side BC with the right angle at B. In the three drawings angle A is 30°, 60° and 80° and the point A slides closer to B along the base while the line AC swings up towards BC. Angle C is marked in each and gets smaller each time.

[textbook_text]
> Now, let us see what happens to the trigonometric ratios of ∠ A, when it is made larger and larger in △ ABC till it becomes 90°. As ∠ A gets larger and larger, ∠ C gets smaller and smaller. Therefore, as in the case above, the length of the side AB goes on decreasing. The point A gets closer to point B. Finally when ∠ A is very close to 90°, ∠ C becomes very close to 0° and the side AC almost coincides with side BC.
> When ∠ C is very close to 0°, ∠ A is very close to 90°, side AC is nearly the same as side BC, and so sin A is very close to 1. Also when ∠ A is very close to 90°, ∠ C is very close to 0°, and the side AB is nearly zero, so cos A is very close to 0.
> So, we define : sin 90° = 1 and cos 90° = 0.
> Now, why don't you find the other trigonometric ratios of 90°?

*(Cleanup: "(see Fig. 8.18)" is dropped. The old image covers only the shrinking case, so this concept has no media.)*

### C42 · More to explore: the undefined values and the rest of 90°
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Triangles flattened at 0 and 90 degrees" — Two side-by-side flattened right triangles. In the first, angle A is nearly 0°, the side BC is almost a point and AC lies almost along AB. In the second, angle A is nearly 90°, the side AB is almost a point and AC lies almost along BC. The very short side is shown as a tiny segment in each, and the side that would sit in a denominator is circled.

[enrichment] `[authored answers]`
> **Q.** Why are cot 0° and cosec 0° not defined?
> **A.** cot 0° = 1/tan 0° = 1/0 and cosec 0° = 1/sin 0° = 1/0. Division by zero has no value, so neither ratio is defined.

[enrichment] `[authored answers]`
> **Q.** Find the other trigonometric ratios of 90°.
> **A.** With sin 90° = 1 and cos 90° = 0: tan 90° = 1/0, which is not defined; cosec 90° = 1/1 = 1; sec 90° = 1/0, which is not defined; and cot 90° = cos 90°/sin 90° = 0/1 = 0.

---

## T10 · The Table of Standard Values

### C43 · All the standard values in one table
`kind: teach` · `objectives: O18`
Media: existing image "Table 8.1 — Standard Angle Values for Five Angles" (old T9 O1.E1) [title carries a book number, cleaned at build]; existing image "Monotone Behaviour of sin A and cos A from 0° to 90°" (old T10 O2.E1). The second image was a practice image for the second question set; it shows the remark below and gives away two of that set's true-or-false parts, so it is moved here, loose fit, please check.

[textbook_text]
> We shall now give the values of all the trigonometric ratios of 0°, 30°, 45°, 60° and 90° in the table below, for ready reference.
>
> | ∠ A | 0° | 30° | 45° | 60° | 90° |
> |---|---|---|---|---|---|
> | sin A | 0 | 1/2 | 1/√2 | √3/2 | 1 |
> | cos A | 1 | √3/2 | 1/√2 | 1/2 | 0 |
> | tan A | 0 | 1/√3 | 1 | √3 | Not defined |
> | cosec A | Not defined | 2 | √2 | 2/√3 | 1 |
> | sec A | 1 | 2/√3 | √2 | 2 | Not defined |
> | cot A | Not defined | √3 | 1 | 1/√3 | 0 |

[remark, from source]
> From the table above you can observe that as ∠ A increases from 0° to 90°, sin A increases from 0 to 1 and cos A decreases from 1 to 0.
> Let us illustrate the use of the values in the table above through some examples.

*(Cleanup: the lead sentence closes the old 0°/90° text in the book and "in Table 8.1" becomes "in the table below". The table heading "Table 8.1" is dropped.)*

---

## T11 · Examples: Using the Standard Values

### C44 · Two sides from one side and a 30° angle
`kind: exercise (worked example)` · `objectives: O18`
Media: existing video "Example 6 Walkthrough — Finding BC and AC in a 30° Triangle" (old T9 VID1) [title carries a book number, cleaned at build]; existing image "Coconut Tree Shadow at 60° and 30° Elevation" (old T9 O1.E2). The video also walks through the next example. The coconut-tree image is not a book example (the old plan added it), so the fit is loose, please check.

[question]
> In △ ABC, right-angled at B, AB = 5 cm and ∠ ACB = 30°. Determine the lengths of the sides BC and AC.

[worked solution, from source]
> To find the length of the side BC, we will choose the trigonometric ratio involving BC and the given side AB. Since BC is the side adjacent to angle C and AB is the side opposite to angle C, therefore
> AB/BC = tan C
> i.e., 5/BC = tan 30° = 1/√3
> which gives BC = 5√3 cm
> To find the length of the side AC, we consider
> sin 30° = AB/AC    (Why?)
> i.e., 1/2 = 5/AC
> i.e., AC = 10 cm

[remark, from source]
> Note that alternatively we could have used Pythagoras theorem to determine the third side in the example above,
> i.e., AC = √(AB² + BC²) = √(5² + (5√3)²) cm = 10 cm.

*(Cleanup: "(see Fig. 8.19)" is dropped.)*

### C45 · Two angles from two sides
`kind: exercise (worked example)` · `objectives: O18`
Media: new image spec "Right triangle with two known sides" — A right triangle PQR with the right angle at Q. The side PQ is labelled 3 cm and the hypotenuse PR is labelled 6 cm. The angles at P and R are marked with arcs and question marks.

[question]
> In △ PQR, right-angled at Q, PQ = 3 cm and PR = 6 cm. Determine ∠ QPR and ∠ PRQ.

[worked solution, from source]
> Given PQ = 3 cm and PR = 6 cm.
> Therefore, PQ/PR = sin R
> or sin R = 3/6 = 1/2
> So, ∠ PRQ = 30°
> and therefore, ∠ QPR = 60°.    (Why?)

[remark, from source]
> You may note that if one of the sides and any other part (either an acute angle or any side) of a right triangle is known, the remaining sides and angles of the triangle can be determined.

*(Cleanup: "(see Fig. 8.20)" is dropped. The video on the example before also covers this one.)*

### C46 · Two angles from their sum and difference
`kind: exercise (worked example)` · `objectives: O19`
Media: new image spec "Two conditions on angles A and B" — Two small panels. In the first, two rays from a point O make angles A and B with a horizontal base line, A drawn larger than B, and the gap between the rays is shaded and labelled A – B with the condition sin(A – B) = 1/2. In the second, an angle labelled A + B is drawn with its arc staying within a right angle, with the condition cos(A + B) = 1/2 and the note 0° < A + B ≤ 90°.

[question]
> If sin (A – B) = 1/2, cos (A + B) = 1/2, 0° < A + B ≤ 90°, A > B, find A and B.

[worked solution, from source]
> Since, sin (A – B) = 1/2, therefore, A – B = 30°    (Why?)    (1)
> Also, since cos (A + B) = 1/2, therefore, A + B = 60°    (Why?)    (2)
> Solving (1) and (2), we get : A = 45° and B = 15°.

### C47 · More to explore: the "Why?" prompts in these examples
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Three small reasons behind the working" — Three small panels. The first shows a right triangle ABC with the right angle at B, angle C = 30° and the side AB facing it. The second shows a right triangle PQR with the right angle at Q and angle PRQ = 30°, with angle QPR marked by an arc. The third shows a graph of sin rising and cos falling between 0° and 90° with a dotted horizontal line at 1/2.

[enrichment] `[authored answers]`
> **Q.** In the triangle ABC with ∠ ACB = 30°, why is sin 30° = AB/AC?
> **A.** AB is the side opposite angle C and AC is the hypotenuse, and ∠ C = 30°. So sin 30° = sin C = AB/AC.

[enrichment] `[authored answers]`
> **Q.** In the triangle PQR, why is ∠ QPR = 60°?
> **A.** The angles of a triangle add up to 180°. ∠ PQR = 90° and ∠ PRQ = 30°, so ∠ QPR = 180° – 90° – 30° = 60°.

[enrichment] `[authored answers]`
> **Q.** Why does sin (A – B) = 1/2 give A – B = 30°, and cos (A + B) = 1/2 give A + B = 60°?
> **A.** From the table, sin 30° = 1/2 and cos 60° = 1/2. As the angle goes from 0° to 90°, sine keeps increasing and cosine keeps decreasing, so no other angle in that range gives the value 1/2. Since A > B and 0° < A + B ≤ 90°, both A – B and A + B lie in that range.

---

## T12 · Questions: Standard Angles

Objectives for this set: O20 (apply) evaluate expressions in the standard angles (Q1); O21 (analyze) choose the correct value of an expression from given options, with justification (Q2); O19 (analyze) find two angles from equations in their sum and difference (Q3); O35 (evaluate) judge statements about the ratios and how they change with the angle as true or false, with a reason (Q4) `[authored]`.

Same rules as the first question set: `attempt_first`, one new hint-free image spec each (statement and that one sub-part only), no video, and steps and answer *to author* for all 15. The questions are in textbook order. No question has a figure and the book prints no hints. The sub-parts of Q1, Q2 and Q4 are independent tasks, so each is its own concept.

### C48 · Standard Angles, Q1 (i)
`objectives: O20` · Media: new image spec (statement and this sub-part only)
> Evaluate the following :
> (i) sin 60° cos 30° + sin 30° cos 60°

### C49 · Standard Angles, Q1 (ii)
`objectives: O20` · Media: new image spec (statement and this sub-part only)
> Evaluate the following :
> (ii) 2 tan²45° + cos²30° – sin²60°

### C50 · Standard Angles, Q1 (iii)
`objectives: O20` · Media: new image spec (statement and this sub-part only)
> Evaluate the following :
> (iii) cos 45°/(sec 30° + cosec 30°)

### C51 · Standard Angles, Q1 (iv)
`objectives: O20` · Media: new image spec (statement and this sub-part only)
> Evaluate the following :
> (iv) (sin 30° + tan 45° – cosec 60°)/(sec 30° + cos 60° + cot 45°)

### C52 · Standard Angles, Q1 (v)
`objectives: O20` · Media: new image spec (statement and this sub-part only)
> Evaluate the following :
> (v) (5 cos²60° + 4 sec²30° – tan²45°)/(sin²30° + cos²30°)

### C53 · Standard Angles, Q2 (i)
`objectives: O21` · Media: new image spec (statement and this sub-part only)
> Choose the correct option and justify your choice :
> (i) 2 tan 30°/(1 + tan²30°) =
> (A) sin 60°   (B) cos 60°   (C) tan 60°   (D) sin 30°

### C54 · Standard Angles, Q2 (ii)
`objectives: O21` · Media: new image spec (statement and this sub-part only)
> Choose the correct option and justify your choice :
> (ii) (1 – tan²45°)/(1 + tan²45°) =
> (A) tan 90°   (B) 1   (C) sin 45°   (D) 0

### C55 · Standard Angles, Q2 (iii)
`objectives: O21` · Media: new image spec (statement and this sub-part only)
> Choose the correct option and justify your choice :
> (iii) sin 2A = 2 sin A is true when A =
> (A) 0°   (B) 30°   (C) 45°   (D) 60°

### C56 · Standard Angles, Q2 (iv)
`objectives: O21` · Media: new image spec (statement and this sub-part only)
> Choose the correct option and justify your choice :
> (iv) 2 tan 30°/(1 – tan²30°) =
> (A) cos 60°   (B) sin 60°   (C) tan 60°   (D) sin 30°

### C57 · Standard Angles, Q3
`objectives: O19` · Media: new image spec (statement only)
> If tan (A + B) = √3 and tan (A – B) = 1/√3; 0° < A + B ≤ 90°; A > B, find A and B.

### C58 · Standard Angles, Q4 (i)
`objectives: O35` · Media: new image spec (statement and this sub-part only)
> State whether the following are true or false. Justify your answer.
> (i) sin (A + B) = sin A + sin B.

### C59 · Standard Angles, Q4 (ii)
`objectives: O35` · Media: new image spec (statement and this sub-part only)
> State whether the following are true or false. Justify your answer.
> (ii) The value of sin θ increases as θ increases.

### C60 · Standard Angles, Q4 (iii)
`objectives: O35` · Media: new image spec (statement and this sub-part only)
> State whether the following are true or false. Justify your answer.
> (iii) The value of cos θ increases as θ increases.

### C61 · Standard Angles, Q4 (iv)
`objectives: O35` · Media: new image spec (statement and this sub-part only)
> State whether the following are true or false. Justify your answer.
> (iv) sin θ = cos θ for all values of θ.

### C62 · Standard Angles, Q4 (v)
`objectives: O35` · Media: new image spec (statement and this sub-part only)
> State whether the following are true or false. Justify your answer.
> (v) cot A is not defined for A = 0°.

---

# M3 · Trigonometric identities

## T13 · The First Identity

### C63 · An equation true for every angle? Try it first
`kind: try` · `objectives: O22`
Media: existing image "Right Triangle ABC with Pythagorean Equation Annotated — Fig. 8.21 Style" (old T11 O1.E1) [title carries a book number, cleaned at build]
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[textbook_text]
> You may recall that an equation is called an identity when it is true for all values of the variables involved. Similarly, an equation involving trigonometric ratios of an angle is called a trigonometric identity, if it is true for all values of the angle(s) involved.
> Now, we will prove one trigonometric identity, and use it further to prove other useful trigonometric identities.

[theorem_statement]
> cos²A + sin²A = 1, for all A such that 0° ≤ A ≤ 90°.

[predict] `[authored]`
> Check the statement on two angles you already know. From the table, cos 30° = √3/2 and sin 30° = 1/2, and cos 45° = sin 45° = 1/√2. Work out cos²A + sin²A for each. Do you get 1 both times? Before the proof, guess which fact about a right triangle could make this happen for every angle.

*(Cleanup: the section heading "8.4" and "In this section" (now "Now") are dropped or reworded. The statement is the book's own result from the next concept.)*

### C64 · Proving that sin²A + cos²A = 1
`kind: prove` · `objectives: O22, O23`
Media: existing video "Proof of sin²A + cos²A = 1 — Step-by-Step Derivation" (old T11 VID1)

[textbook_text]
> In △ ABC, right-angled at B, we have:
> AB² + BC² = AC²    (1)
> Dividing each term of (1) by AC², we get
> AB²/AC² + BC²/AC² = AC²/AC²
> i.e., (AB/AC)² + (BC/AC)² = (AC/AC)²
> i.e., (cos A)² + (sin A)² = 1
> i.e., cos²A + sin²A = 1    (2)
> This is true for all A such that 0° ≤ A ≤ 90°. So, this is a trigonometric identity.

[remark, from source]
> Since the hypotenuse is the longest side in a right triangle, the value of sin A or cos A is always less than 1 (or, in particular, equal to 1).

*(Cleanup: "(see Fig. 8.21)" is dropped. The old plan prints this remark here as well as after the first ratios; it is kept in both places so that nothing is lost, please check whether one copy should go.)*

---

## T14 · Examples: One Ratio in Terms of Another

### C65 · cos A, tan A and sec A in terms of sin A
`kind: exercise (worked example)` · `objectives: O24`
Media: existing video "Example 9 Walkthrough — cos A, tan A, sec A from sin A" (old T12 VID1) [title carries a book number, cleaned at build]; existing image "Algebraic Chain: From sin A to All Other Ratios" (old T12 O1.E1)

[question]
> Express the ratios cos A, tan A and sec A in terms of sin A.

[worked solution, from source]
> Since cos²A + sin²A = 1, therefore,
> cos²A = 1 – sin²A, i.e., cos A = ± √(1 – sin²A)
> This gives cos A = √(1 – sin²A)    (Why?)
> Hence, tan A = sin A/cos A = sin A/√(1 – sin²A) and sec A = 1/cos A = 1/√(1 – sin²A)

### C66 · More to explore: why the positive root
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Why a ratio of lengths is positive" — A right triangle ABC with the right angle at B and the acute angle A marked. The sides AB and AC are drawn as two lengths along a ruler that starts at zero, both lying on the positive side. A caption reads cos A = AB/AC, a ratio of two lengths.

[enrichment] `[authored answer]`
> **Q.** Why do we take cos A = √(1 – sin²A) and not the negative root?
> **A.** A is an acute angle of a right triangle, so cos A = AB/AC is a ratio of two lengths. Both lengths are positive, so cos A is positive.

---

## T15 · The Second Identity

### C67 · Divide by a different side? Try it first
`kind: try` · `objectives: O25`
Media: existing image "Right Triangle ABC — Deriving 1 + tan²A = sec²A by Dividing by AB²" (old T13 O1.E1)
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[theorem_statement]
> 1 + tan²A = sec²A, for all A such that 0° ≤ A < 90°.

[predict] `[authored]`
> The first identity came from dividing AB² + BC² = AC² by AC². Predict what you get if you divide the same equation by AB² instead. Which two ratios have AB in the denominator? Also guess: at which of 0° and 90° might the result stop making sense?

### C68 · Proving that 1 + tan²A = sec²A
`kind: prove` · `objectives: O25`
Media: existing video "Proof of 1 + tan²A = sec²A — Dividing by AB²" (old T13 VID1)

[textbook_text]
> Let us now divide (1) by AB². We get
> AB²/AB² + BC²/AB² = AC²/AB²
> or, (AB/AB)² + (BC/AB)² = (AC/AB)²
> i.e., 1 + tan²A = sec²A    (3)
> Is this equation true for A = 0°? Yes, it is. What about A = 90°? Well, tan A and sec A are not defined for A = 90°. So, (3) is true for all A such that 0° ≤ A < 90°.

### C69 · All six ratios from tan A, using the identities
`kind: teach` · `objectives: O26`
Media: existing video "tan A = 1/√3 — Full Worked Derivation Using Identities" (old T14 VID1); existing image "Identity-Chain Flowchart: tan A → All Six Ratios" (old T14 O1.E1)

[textbook_text]
> Using these identities, we can express each trigonometric ratio in terms of other trigonometric ratios, i.e., if any one of the ratios is known, we can also determine the values of other trigonometric ratios.
> Let us see how we can do this using these identities. Suppose we know that
> tan A = 1/√3. Then, cot A = √3.
> Since, sec²A = 1 + tan²A = 1 + 1/3 = 4/3, sec A = 2/√3, and cos A = √3/2.
> Again, sin A = √(1 – cos²A) = √(1 – 3/4) = 1/2. Therefore, cosec A = 2.

*(In the book this passage comes after the third identity. The old plan places it here, straight after the second identity, which is the one it uses; that order is kept. It is not a numbered example, so it is a teach concept.)*

---

## T16 · The Third Identity

### C70 · The last side to divide by. Try it first
`kind: try` · `objectives: O27`
Media: existing image "Right Triangle ABC — Deriving cot²A + 1 = cosec²A by Dividing by BC²" (old T15 O1.E1)
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[theorem_statement]
> cot²A + 1 = cosec²A, for all A such that 0° < A ≤ 90°.

[predict] `[authored]`
> One side is left: BC. Predict the identity you get by dividing AB² + BC² = AC² by BC². This time, is it 0° or 90° that has to be left out, and why?

### C71 · Proving that cot²A + 1 = cosec²A
`kind: prove` · `objectives: O27`
Media: existing video "Proof of cot²A + 1 = cosec²A — The Third Pythagorean Identity" (old T15 VID1)

[textbook_text]
> Let us see what we get on dividing (1) by BC². We get
> AB²/BC² + BC²/BC² = AC²/BC²
> i.e., (AB/BC)² + (BC/BC)² = (AC/BC)²
> i.e., cot²A + 1 = cosec²A    (4)
> Note that cosec A and cot A are not defined for A = 0°. Therefore (4) is true for all A such that 0° < A ≤ 90°.

---

## T17 · Examples: Proving Identities

### C72 · Proving sec A (1 – sin A)(sec A + tan A) = 1
`kind: exercise (worked example)` · `objectives: O28, O29`
Media: existing image "Example 10 Proof Layout — Step-by-Step Equation Display" (old T16 O2.E2) [title carries a book number, cleaned at build]

[question]
> Prove that sec A (1 – sin A)(sec A + tan A) = 1.

[worked solution, from source]
> LHS = sec A (1 – sin A)(sec A + tan A) = (1/cos A)(1 – sin A)(1/cos A + sin A/cos A)
> = (1 – sin A)(1 + sin A)/cos²A = (1 – sin²A)/cos²A
> = cos²A/cos²A = 1 = RHS

### C73 · Proving (cot A – cos A)/(cot A + cos A) = (cosec A – 1)/(cosec A + 1)
`kind: exercise (worked example)` · `objectives: O28, O29`
Media: existing video "Identity Proof Walkthrough — Example 11 Full Solution" (old T16 VID1) [title carries a book number, cleaned at build]

[question]
> Prove that (cot A – cos A)/(cot A + cos A) = (cosec A – 1)/(cosec A + 1).

[worked solution, from source]
> LHS = (cot A – cos A)/(cot A + cos A) = (cos A/sin A – cos A)/(cos A/sin A + cos A)
> = cos A(1/sin A – 1)/cos A(1/sin A + 1) = (1/sin A – 1)/(1/sin A + 1) = (cosec A – 1)/(cosec A + 1) = RHS

### C74 · Proving an identity using sec²θ = 1 + tan²θ
`kind: exercise (worked example)` · `objectives: O28, O29`
Media: existing image "Identity Proof Strategy Map — Three Examples and Their Key Identity Steps" (old T16 O2.E1). It covers all three proof examples, so it sits on the last one, loose fit, please check.

[question]
> Prove that (sin θ – cos θ + 1)/(sin θ + cos θ – 1) = 1/(sec θ – tan θ), using the identity sec²θ = 1 + tan²θ.

[worked solution, from source]
> Since we will apply the identity involving sec θ and tan θ, let us first convert the LHS (of the identity we need to prove) in terms of sec θ and tan θ by dividing numerator and denominator by cos θ.
> LHS = (sin θ – cos θ + 1)/(sin θ + cos θ – 1) = (tan θ – 1 + sec θ)/(tan θ + 1 – sec θ)
> = ((tan θ + sec θ) – 1)/((tan θ – sec θ) + 1)
> = {(tan θ + sec θ) – 1}(tan θ – sec θ)/{(tan θ – sec θ) + 1}(tan θ – sec θ)
> = {(tan²θ – sec²θ) – (tan θ – sec θ)}/{tan θ – sec θ + 1}(tan θ – sec θ)
> = (–1 – tan θ + sec θ)/(tan θ – sec θ + 1)(tan θ – sec θ)
> = –1/(tan θ – sec θ) = 1/(sec θ – tan θ),
> which is the RHS of the identity, we are required to prove.

*(The old chunk drops the braces round the numerator on the fifth line; they are restored from the book.)*

---

## T18 · Questions: Trigonometric Identities

Objectives for this set: O30 (apply) express the other ratios in terms of one given ratio (Q1, Q2); O32 (analyze) choose the correct value of an expression from given options using the identities, with justification (Q3); O31 (evaluate) prove given identities by choosing the identity that fits each one (Q4).

Same rules as the first question set: `attempt_first`, one new hint-free image spec each (statement and that one sub-part only), no video, and steps and answer *to author* for all 16. The questions are in textbook order. No question has a figure. The sub-parts of Q3 and Q4 are independent tasks, so each is its own concept; each Q4 sub-part repeats the stem. The book prints a hint for Q4 (iii), (iv) and (ix); each is kept and shown only after the attempt, never on the image.

### C75 · Trigonometric Identities, Q1
`objectives: O30` · Media: new image spec (statement only)
> Express the trigonometric ratios sin A, sec A and tan A in terms of cot A.

### C76 · Trigonometric Identities, Q2
`objectives: O30` · Media: new image spec (statement only)
> Write all the other trigonometric ratios of ∠ A in terms of sec A.

### C77 · Trigonometric Identities, Q3 (i)
`objectives: O32` · Media: new image spec (statement and this sub-part only)
> Choose the correct option. Justify your choice.
> (i) 9 sec²A – 9 tan²A =
> (A) 1   (B) 9   (C) 8   (D) 0

### C78 · Trigonometric Identities, Q3 (ii)
`objectives: O32` · Media: new image spec (statement and this sub-part only)
> Choose the correct option. Justify your choice.
> (ii) (1 + tan θ + sec θ)(1 + cot θ – cosec θ) =
> (A) 0   (B) 1   (C) 2   (D) –1

### C79 · Trigonometric Identities, Q3 (iii)
`objectives: O32` · Media: new image spec (statement and this sub-part only)
> Choose the correct option. Justify your choice.
> (iii) (sec A + tan A)(1 – sin A) =
> (A) sec A   (B) sin A   (C) cosec A   (D) cos A

### C80 · Trigonometric Identities, Q3 (iv)
`objectives: O32` · Media: new image spec (statement and this sub-part only)
> Choose the correct option. Justify your choice.
> (iv) (1 + tan²A)/(1 + cot²A) =
> (A) sec²A   (B) –1   (C) cot²A   (D) tan²A

### C81 · Trigonometric Identities, Q4 (i)
`objectives: O31` · Media: new image spec (statement and this sub-part only)
> Prove the following identities, where the angles involved are acute angles for which the expressions are defined.
> (i) (cosec θ – cot θ)² = (1 – cos θ)/(1 + cos θ)

### C82 · Trigonometric Identities, Q4 (ii)
`objectives: O31` · Media: new image spec (statement and this sub-part only)
> Prove the following identities, where the angles involved are acute angles for which the expressions are defined.
> (ii) cos A/(1 + sin A) + (1 + sin A)/cos A = 2 sec A

### C83 · Trigonometric Identities, Q4 (iii)
`objectives: O31` · Media: new image spec (statement and this sub-part only)
> Prove the following identities, where the angles involved are acute angles for which the expressions are defined.
> (iii) tan θ/(1 – cot θ) + cot θ/(1 – tan θ) = 1 + sec θ cosec θ
> **Hint (shown only after the attempt):** Write the expression in terms of sin θ and cos θ.

### C84 · Trigonometric Identities, Q4 (iv)
`objectives: O31` · Media: new image spec (statement and this sub-part only)
> Prove the following identities, where the angles involved are acute angles for which the expressions are defined.
> (iv) (1 + sec A)/sec A = sin²A/(1 – cos A)
> **Hint (shown only after the attempt):** Simplify LHS and RHS separately.

### C85 · Trigonometric Identities, Q4 (v)
`objectives: O31` · Media: new image spec (statement and this sub-part only)
> Prove the following identities, where the angles involved are acute angles for which the expressions are defined.
> (v) (cos A – sin A + 1)/(cos A + sin A – 1) = cosec A + cot A, using the identity cosec²A = 1 + cot²A.

### C86 · Trigonometric Identities, Q4 (vi)
`objectives: O31` · Media: new image spec (statement and this sub-part only)
> Prove the following identities, where the angles involved are acute angles for which the expressions are defined.
> (vi) √((1 + sin A)/(1 – sin A)) = sec A + tan A

### C87 · Trigonometric Identities, Q4 (vii)
`objectives: O31` · Media: new image spec (statement and this sub-part only)
> Prove the following identities, where the angles involved are acute angles for which the expressions are defined.
> (vii) (sin θ – 2 sin³θ)/(2 cos³θ – cos θ) = tan θ

### C88 · Trigonometric Identities, Q4 (viii)
`objectives: O31` · Media: new image spec (statement and this sub-part only)
> Prove the following identities, where the angles involved are acute angles for which the expressions are defined.
> (viii) (sin A + cosec A)² + (cos A + sec A)² = 7 + tan²A + cot²A

### C89 · Trigonometric Identities, Q4 (ix)
`objectives: O31` · Media: new image spec (statement and this sub-part only)
> Prove the following identities, where the angles involved are acute angles for which the expressions are defined.
> (ix) (cosec A – sin A)(sec A – cos A) = 1/(tan A + cot A)
> **Hint (shown only after the attempt):** Simplify LHS and RHS separately.

### C90 · Trigonometric Identities, Q4 (x)
`objectives: O31` · Media: new image spec (statement and this sub-part only)
> Prove the following identities, where the angles involved are acute angles for which the expressions are defined.
> (x) (1 + tan²A)/(1 + cot²A) = ((1 – tan A)/(1 – cot A))² = tan²A

---

# M4 · Wrap-up

## T19 · Chapter Summary

### C91 · Chapter summary
`kind: summary` · `objectives: O33, O34`
Media: existing video "Chapter Summary Recap — From Right Triangle to Three Identities" (old T18 VID1); existing image "Chapter Summary Infographic — Six Ratios, Three Identities, Standard Angles" (old T18 O1.E1); existing image "Q4 Identity Grouping Chart — Which Identity to Use for Each Sub-Part" (old T17 O2.E1). The grouping chart was a practice image for the last question set; it gives away which identity to use, so it is re-homed here as the Ch3 and Ch7 plans did, please check (the alternative is to hold it).

[summary_points]
> In this chapter, you have studied the following points :
> 1. In a right triangle ABC, right-angled at B, sin A = (side opposite to angle A)/(hypotenuse), cos A = (side adjacent to angle A)/(hypotenuse), tan A = (side opposite to angle A)/(side adjacent to angle A).
> 2. cosec A = 1/sin A; sec A = 1/cos A; tan A = 1/cot A, tan A = sin A/cos A.
> 3. If one of the trigonometric ratios of an acute angle is known, the remaining trigonometric ratios of the angle can be easily determined.
> 4. The values of trigonometric ratios for angles 0°, 30°, 45°, 60° and 90°.
> 5. The value of sin A or cos A never exceeds 1, whereas the value of sec A (0° ≤ A < 90°) or cosec A (0° < A ≤ 90°) is always greater than or equal to 1.
> 6. sin²A + cos²A = 1, sec²A – tan²A = 1 for 0° ≤ A < 90°, cosec²A = 1 + cot²A for 0° < A ≤ 90°.

*(Cleanup: the section heading "8.5 Summary" is dropped. Points 1 and 6 are printed over several lines in the book and are joined here, one point per line.)*

---

# Appendix A · Objectives

Format: ID · bloom level · wording · old objective it carries. O1–O34 carry the 34 old objectives in old order. Wording changed only where the old text cited a book table, an old topic or numbered identities; those rows are marked "reworded". O35 is new.

| ID | Bloom | Objective | Old ID |
|---|---|---|---|
| O1 | understand | Interpret everyday situations (Qutub Minar, river bank, hot-air balloon) as right-triangle problems that trigonometry can solve. | T1.O1 |
| O2 | apply | Represent a real-life scenario as a labelled right triangle identifying the relevant sides and angle. | T1.O2 |
| O3 | evaluate | Justify why cosec A, sec A, and cot A are the reciprocals of sin A, cos A, and tan A respectively. | T2.O1 |
| O4 | understand | Represent sin A, cos A, tan A and their reciprocals as ratios of the sides of right triangle ABC. | T2.O2 |
| O5 | evaluate | Prove that the value of sin A does not depend on the size of the right triangle, using AA similarity of triangles PAM and CAB. | T3.O1 |
| O6 | understand | Explain why trigonometric ratios depend only on the angle and not on the lengths of the triangle's sides. | T3.O2 |
| O7 | apply | Compute all six trigonometric ratios of an angle when one ratio is given, using the Pythagorean theorem to find the missing side. | T4.O1 |
| O8 | evaluate | Verify that equal sine values for two acute angles imply the angles are equal, using the property of similar triangles. | T4.O2 |
| O9 | apply | Solve problems requiring computation of trigonometric ratios from given side lengths or ratio values. | T5.O1 |
| O10 | evaluate | Verify or disprove statements about the range and notation of trigonometric ratios. | T5.O2 |
| O11 | analyze | Classify given statements about tan A, sec A, cos A, and cot A as true or false with justification. | T5.O3 |
| O12 | understand | Derive the values of sin 45°, cos 45°, and tan 45° from an isosceles right triangle with equal legs. | T6.O1 |
| O13 | apply | Compute cosec 45°, sec 45°, and cot 45° as reciprocals of the primary ratios. | T6.O2 |
| O14 | understand | Derive the values of sin 30°, cos 30°, tan 30°, sin 60°, cos 60°, and tan 60° from a bisected equilateral triangle. | T7.O1 |
| O15 | apply | Compute all six trigonometric ratios for 30° and 60° using the derived side ratios of the 30-60-90 triangle. | T7.O2 |
| O16 | understand | Explain why sin 0° = 0 and cos 0° = 1 using the limiting behaviour of angle A approaching 0° in a right triangle. | T8.O1 |
| O17 | apply | Compute tan 0°, cot 0°, sec 0°, cosec 90° and identify which of these are undefined, with reasons. | T8.O2 |
| O18 | apply | Compute side lengths and angles of right triangles using the standard values for 30°, 45°, and 60°. | T9.O1 (reworded) |
| O19 | analyze | Determine unknown angles A and B from equations such as sin(A - B) = 1/2 and cos(A + B) = 1/2 using standard values. | T9.O2 |
| O20 | apply | Evaluate trigonometric expressions involving standard angles using the table of standard values. | T10.O1 (reworded) |
| O21 | analyze | Determine the correct value of a composite expression by selecting from given options with justification. | T10.O2 |
| O22 | evaluate | Prove that sin²A + cos²A = 1 for all acute angles A by dividing the Pythagorean theorem by AC². | T11.O1 |
| O23 | understand | Explain why the value of sin A or cos A never exceeds 1 using the identity sin²A + cos²A = 1. | T11.O2 |
| O24 | apply | Compute cos A, tan A, and sec A as algebraic expressions in sin A using the identity sin²A + cos²A = 1. | T12.O1 |
| O25 | evaluate | Prove that 1 + tan²A = sec²A for all 0° ≤ A < 90° by dividing the Pythagorean equation AB² + BC² = AC² by AB². | T13.O1 |
| O26 | apply | Compute all six trigonometric ratios when tan A = 1/√3 by applying the identity sec²A = 1 + tan²A and then working back through cos A and the identity sin²A + cos²A = 1 to sin A. | T14.O1 (reworded) |
| O27 | evaluate | Prove that cot²A + 1 = cosec²A for all 0° < A ≤ 90° by dividing the Pythagorean equation AB² + BC² = AC² by BC². | T15.O1 |
| O28 | apply | Prove trigonometric identities such as sec A(1 – sin A)(sec A + tan A) = 1 by working from one side only and applying the identities sin²A + cos²A = 1, 1 + tan²A = sec²A or cot²A + 1 = cosec²A. | T16.O1 (reworded) |
| O29 | evaluate | Justify each algebraic step in a trigonometric identity proof by citing which identity or ratio definition was applied. | T16.O2 (reworded) |
| O30 | apply | Express the other trigonometric ratios in terms of one given ratio, such as cot A or sec A, by applying the identities and the reciprocal definitions. | T17.O1 (reworded) |
| O31 | evaluate | Prove given trigonometric identities by selecting and applying the appropriate identity for each one. | T17.O2 (reworded) |
| O32 | analyze | Determine the correct value of composite trigonometric expressions by applying the three identities and justifying each choice. | T17.O3 (reworded) |
| O33 | remember | Recall and state the six trigonometric ratio definitions, three reciprocal relations, and all three Pythagorean identities with their correct domains as a unified summary of the chapter. | T18.O1 |
| O34 | understand | Compare the behaviour of sin A and cos A as A increases from 0° to 90°, and explain why sin A or cos A never exceeds 1 while sec A and cosec A are always at least 1. | T18.O2 |
| O35 | evaluate | Judge statements about the trigonometric ratios and how they change as the angle increases as true or false, with a reason. `[authored]` | new |

Notes:
- Reworded rows. O18 and O20 cited the book's table number. O26 and O28 cited the book's identity numbers (2), (3) and (4). O29 and O30 cited an old topic number. O31 cited the exercise number and question number. O32 cited a question number. O30 also widens "in terms of cot A" to "one given ratio, such as cot A or sec A", so that it covers the second question of the last set.
- O35 is new. No old objective fits the true-or-false part of the second question set, which is about the standard values and how sine and cosine change with the angle.
- O8 (equal sines) also covers the first set's Q6, which is the same task for cosines.

# Appendix B · Held assets (not attached to the new plan; nothing deleted)

**Seven old tools** (no tools in this chapter):
- T1 "Real World Trig Puzzle (Qutub Minar, river width, balloon)" (T2D1)
- T2 "Right Triangle Ratio Builder" (T2D1)
- T3 "PhET Trig Tour Embed" (T2D1)
- T4 "Find All Ratios from One (detective mode)" (T2D1)
- T9 "Standard Angles Table Builder" (T2D1)
- T11 "Pythagorean Identity Proof Visualizer" (T2D1)
- T16 "Identity Simplification Stepper" (T2D1)

**Three old question videos** (no question videos for now):
- "Strategy Walkthrough for Exercise 8.1 Question Groups" (T5 VID1)
- "Model Solution: Exercise 8.2 Q1(v) Using the sin²A + cos²A = 1 Shortcut" (T10 VID1)
- "Model Proof for Q4(i) — (cosec θ − cot θ)² = (1−cos θ)/(1+cos θ)" (T17 VID1)

**One other image**:
- "Right Triangle for Exercise 8.1 Q1 — AB = 24, BC = 7, AC = 25" (T5 O1.E1). It is drawn for the first question of the first set and shows the third side, AC = 25, which is a step of the working. It cannot be the question image, and no teaching concept uses a triangle with these sides, so it is held. It could go to the summary instead, please check.

# Appendix C · Carried-over fields

Every old topic's `recall_questions`, `summary`, `key_terms`, `concept_bullets` and `detailed_summary` carry into the new topic that holds its text. They are not shown here, to keep this file reviewable. The first concept in each row is in the new topic that receives the old topic's fields.

Where each old topic's text and fields land:

| Old topic | New concepts |
|---|---|
| T1 Introduction: right triangles in real-life contexts | C1, C2 |
| T2 Defining the six trigonometric ratios | C3, C4, C5, C6 |
| T3 Invariance of the ratios under scaling | C7, C8, C9 |
| T4 Finding all six ratios given one ratio | C10, C11, then the examples C12–C17 |
| T5 First exercise set | C18–C35 |
| T6 Ratios of 45° | C36, C37 |
| T7 Ratios of 30° and 60° | C38, C39 |
| T8 Ratios of 0° and 90° | C40, C41, C42, and the lead sentence of C43 |
| T9 Table of values and worked examples | C43, then the examples C44–C47 |
| T10 Second exercise set | C48–C62, and its image moves to C43 |
| T11 Proof of sin²A + cos²A = 1 | C63, C64 |
| T12 Ratios in terms of sin A | C65, C66 |
| T13 Proof of 1 + tan²A = sec²A | C67, C68 |
| T14 Ratios from tan A using the identities | C69 |
| T15 Proof of cot²A + 1 = cosec²A | C70, C71 |
| T16 Proving identities | C72, C73, C74 |
| T17 Third exercise set | C75–C90, and its image moves to C91 |
| T18 Chapter summary | C91 |
