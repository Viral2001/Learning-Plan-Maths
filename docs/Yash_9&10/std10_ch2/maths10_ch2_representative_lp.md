# Representative learning plan: Class 10, Polynomials (maths10_ch2)

A review copy of the restructured plan, down to concept level. Content is shown in full. Media are only named and never embedded.

Source: `learning_plan_std10_chap2_version1.json`. Shape follows the Class 9 circles plan and the Class 10 coordinate geometry plan.

## Read this first

**Standing decisions**
- No tools in this chapter. The eight old `2d_tool` / `simulation` items are held (Appendix B). The two theorem-style "try it first" concepts (the quadratic and the cubic relationships between zeroes and coefficients) therefore carry the statement and a prediction only. There is no try-it step.
- No videos for exercise questions. Each question concept gets one hint-free image spec and no video. The old question videos are held.
- Examples keep the existing videos and images that match them. No new example media is planned.
- No grouping inside the exercise sets. Each book question is its own concept, in book order, named "<set name>, Q<n>". A question with separate sub-parts is split: each sub-part is its own concept, named "<set name>, Q<n> (<roman>)", and keeps the stem verbatim plus that one sub-part. All three questions in this chapter (the graph question and the two quadratic questions) have six independent sub-parts each, so there are 6 + 6 + 6 = 18 question concepts.
- The old plan splits the second exercise set over two topics (Q1 and Q2). In this plan both questions sit in ONE Questions topic.

**What a concept entry shows**
- `kind`: try, prove, teach, enrich, hook, exercise or summary.
- `objectives`: objective IDs. Enrichment concepts have none.
- `media`: existing assets re-homed from the old plan, new asset specs, or none. The notation "old T<n> <suffix>" gives the old topic number and the tail of the old media id, e.g. VID1, E1, O1.E1.
- `[block_kind]` tags are review labels only. They never reach the student.

**Text cleanup applied to everything below**
- "Fig. 2.x" and "see Fig. 2.x" are removed or turned into "shown here" / "the graph". The figure is carried by the image.
- "Table 2.1" and "Table 2.2" become "the table below" / "the table".
- "Section 2.1" becomes "earlier". Section headings such as "2.2 Geometrical Meaning ..." are dropped.
- "Example n:", "Exercise 2.x" and the "EXERCISE" heading labels are removed.
- Book references stay only in metadata (`ncert_refs`), which is not shown here.

**Marked in the text**
- `[authored]` marks text that is not in the old plan or the book. These are predictions, answers to "(Why?)" prompts, theorem statements pulled from the summary and new objective wording.
- Question solutions (`steps` and `answer`) are not in the old plan. They are marked *to author* and nothing is invented here.

**Moved or lightly edited text (all other text is verbatim)**
- The closing paragraph of the old value-and-zero topic ("the zero of a linear polynomial is related to its coefficients ... the division algorithm") is moved to the hook (C1). Its opening "Thus, the zero" became "The zero".
- The book's "In general, it can be proved that ..." statement for cubics is moved from the end of the cubic discussion into the cubic "try" concept (C29). The cubic check (C30) keeps the numbers.
- The footnote about plotting graphs stays with the quadratic table (C8). The Greek-letter footnote stays with the derivation (C25). The "not from the examination point of view" footnote stays with the cubic example (C31).

## Plan at a glance

| Module | Topic | Concepts |
|---|---|---|
| M1 Foundations of polynomials | T1 Where Zeroes and Coefficients Meet (hook) | C1 |
| | T2 Degrees and Types of Polynomials | C2–C3 |
| | T3 Values and Zeroes of a Polynomial | C4–C6 |
| M2 What zeroes look like on a graph | T4 The Line and Its One Zero | C7 |
| | T5 The Parabola and Its Zeroes | C8–C10 |
| | T6 Three Ways a Parabola Meets the Axis | C11 |
| | T7 Cubic Graphs and the At-Most-n Rule | C12–C13 |
| | T8 Examples: Reading Zeroes from Graphs | C14–C15 |
| | T9 Questions: Zeroes on the Graph | C16–C21 |
| M3 Zeroes and coefficients | T10 Spotting the Pattern in Two Quadratics | C22–C23 |
| | T11 Sum and Product of the Zeroes of a Quadratic | C24–C25 |
| | T12 Examples: Quadratic Zeroes and Coefficients | C26–C28 |
| | T13 Zeroes and Coefficients of a Cubic | C29–C30 |
| | T14 Examples: Cubic Zeroes and Coefficients | C31 |
| | T15 Questions: Zeroes and Their Sums and Products | C32–C43 |
| M4 Wrap-up | T16 Chapter Summary | C44 |

Totals: 44 concepts and 27 objectives. 18 question concepts need a new image (6 graph panels, 6 + 6 quadratic sub-parts). 0 new videos.

---

# M1 · Foundations of polynomials

## T1 · Where Zeroes and Coefficients Meet (hook)

### C1 · A question that drives the chapter
`kind: hook` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Zeroes Meet Coefficients" — A split picture. On the left, a straight line y = ax + b crossing the x-axis at one marked point with the label 'zero = -b/a'. On the right, a parabola crossing the x-axis at two marked points with a large question mark between them and the generic form ax^2 + bx + c written below, hinting at the question of whether its zeroes are also tied to the coefficients.

[textbook_text]
> The zero of a linear polynomial is related to its coefficients. Does this happen in the case of other polynomials too? For example, are the zeroes of a quadratic polynomial also related to its coefficients?
>
> In this chapter, we will try to answer these questions. We will also study the division algorithm for polynomials.

*(Moved here from the end of the old value-and-zero topic. The opening "Thus, the" became "The".)*

---

## T2 · Degrees and Types of Polynomials

### C2 · The degree of a polynomial
`kind: teach` · `objectives: O1`
Media: existing video "Classifying polynomials by degree — walkthrough" (old T1 VID1). The video also classifies by degree, which the next concept covers, so the fit is a little wide, please check.

[textbook_text]
> In Class IX, you have studied polynomials in one variable and their degrees. Recall that if p(x) is a polynomial in x, the highest power of x in p(x) is called the degree of the polynomial p(x). For example, 4x + 2 is a polynomial in the variable x of degree 1, 2y² – 3y + 4 is a polynomial in the variable y of degree 2, 5x³ – 4x² + x – √2 is a polynomial in the variable x of degree 3 and 7u⁶ – (3/2)u⁴ + 4u² + u – 8 is a polynomial in the variable u of degree 6. Expressions like 1/(x – 1), √x + 2, 1/(x² + 2x + 3) etc., are not polynomials.

### C3 · Linear, quadratic and cubic polynomials
`kind: teach` · `objectives: O2, O3`
Media: existing image "Polynomial-degree classification chart" (old T1 O1.E1)

[textbook_text]
> A polynomial of degree 1 is called a linear polynomial. For example, 2x – 3, √3x + 5, y + √2, x – 2/11, 3z + 4, (2/3)u + 1, etc., are all linear polynomials. Polynomials such as 2x + 5 – x², x³ + 1, etc., are not linear polynomials.
>
> A polynomial of degree 2 is called a quadratic polynomial. The name 'quadratic' has been derived from the word 'quadrate', which means 'square'. 2x² + 3x – 2/5, y² – 2, 2 – x² + √3x, u/3 – 2u² + 5, √5v² – (2/3)v, 4z² + 1/7 are some examples of quadratic polynomials (whose coefficients are real numbers). More generally, any quadratic polynomial in x is of the form ax² + bx + c, where a, b, c are real numbers and a ≠ 0. A polynomial of degree 3 is called a cubic polynomial. Some examples of a cubic polynomial are 2 – x³, x³, √2 x³, 3 – x² + x³, 3x³ – 2x² + x – 1. In fact, the most general form of a cubic polynomial is ax³ + bx² + cx + d, where a, b, c, d are real numbers and a ≠ 0.

---

## T3 · Values and Zeroes of a Polynomial

### C4 · Replacing x by a number: the value of a polynomial
`kind: teach` · `objectives: O4`
Media: existing image "Substitution layout for p(x) = x² – 3x – 4" (old T2 O1.E1). The image also shows the zero rows that the next concept introduces, so the fit is loose, please check.

[textbook_text]
> Now consider the polynomial p(x) = x² – 3x – 4. Then, putting x = 2 in the polynomial, we get p(2) = 2² – 3 × 2 – 4 = – 6. The value '– 6', obtained by replacing x by 2 in x² – 3x – 4, is the value of x² – 3x – 4 at x = 2. Similarly, p(0) is the value of p(x) at x = 0, which is – 4.
>
> If p(x) is a polynomial in x, and if k is any real number, then the value obtained by replacing x by k in p(x), is called the value of p(x) at x = k, and is denoted by p(k).

### C5 · When the value is zero: zeroes of a polynomial
`kind: teach` · `objectives: O5`
Media: existing video "From value p(k) to zero of p(x)" (old T2 VID1)

[textbook_text]
> What is the value of p(x) = x² – 3x – 4 at x = –1? We have :
> p(–1) = (–1)² – {3 × (–1)} – 4 = 0
> Also, note that p(4) = 4² – (3 × 4) – 4 = 0.
> As p(–1) = 0 and p(4) = 0, –1 and 4 are called the zeroes of the quadratic polynomial x² – 3x – 4. More generally, a real number k is said to be a zero of a polynomial p(x), if p(k) = 0.

### C6 · The zero of a linear polynomial
`kind: teach` · `objectives: O6`
Media: new image spec "Finding the Zero of ax + b" — A balance-style picture for the linear polynomial 2x + 3: the expression 2k + 3 on one pan and 0 on the other, leading to k = -3/2. Beside it, the general polynomial ax + b with the general equation ak + b = 0 and its solution k = -b/a, with the constant term and the coefficient of x colour-coded in the fraction.

[textbook_text]
> You have already studied in Class IX, how to find the zeroes of a linear polynomial. For example, if k is a zero of p(x) = 2x + 3, then p(k) = 0 gives us 2k + 3 = 0, i.e., k = –3/2.
> In general, if k is a zero of p(x) = ax + b, then p(k) = ak + b = 0, i.e., k = –b/a.
> So, the zero of the linear polynomial ax + b is –b/a = –(Constant term)/(Coefficient of x).

---

# M2 · What zeroes look like on a graph

## T4 · The Line and Its One Zero

### C7 · Where the line y = ax + b meets the x-axis
`kind: teach` · `objectives: O7`
Media: existing video "Graph of y = 2x + 3 and its x-intercept" (old T3 VID1); existing image "Graph of y = 2x + 3 with x-intercept (–3/2, 0)" (old T3 O1.E1)

[textbook_text]
> You know that a real number k is a zero of the polynomial p(x) if p(k) = 0. But why are the zeroes of a polynomial so important? To answer this, first we will see the geometrical representations of linear and quadratic polynomials and the geometrical meaning of their zeroes.
>
> Consider first a linear polynomial ax + b, a ≠ 0. You have studied in Class IX that the graph of y = ax + b is a straight line. For example, the graph of y = 2x + 3 is a straight line passing through the points (–2, –1) and (2, 7).
>
> | x | –2 | 2 |
> |---|---|---|
> | y = 2x + 3 | –1 | 7 |
>
> From the graph, you can see that the graph of y = 2x + 3 intersects the x-axis mid-way between x = –1 and x = –2, that is, at the point (–3/2, 0). You also know that the zero of 2x + 3 is –3/2. Thus, the zero of the polynomial 2x + 3 is the x-coordinate of the point where the graph of y = 2x + 3 intersects the x-axis.
>
> In general, for a linear polynomial ax + b, a ≠ 0, the graph of y = ax + b is a straight line which intersects the x-axis at exactly one point, namely, (–b/a, 0). Therefore, the linear polynomial ax + b, a ≠ 0, has exactly one zero, namely, the x-coordinate of the point where the graph of y = ax + b intersects the x-axis.

---

## T5 · The Parabola and Its Zeroes

### C8 · Building the graph of x² – 3x – 4 from a table
`kind: teach` · `objectives: O8`
Media: existing video "Drawing the parabola y = x² – 3x – 4 point by point" (old T4 VID1); existing image "Parabola of y = x² – 3x – 4 with Table 2.1" (old T4 O1.E1; renamed at build, since the title carries the book's table number)

[textbook_text]
> Now, let us look for the geometrical meaning of a zero of a quadratic polynomial. Consider the quadratic polynomial x² – 3x – 4. Let us see what the graph* of y = x² – 3x – 4 looks like. Let us list a few values of y = x² – 3x – 4 corresponding to a few values for x as given in the table below.
>
> | x | – 2 | –1 | 0 | 1 | 2 | 3 | 4 | 5 |
> |---|---|---|---|---|---|---|---|---|
> | y = x² – 3x – 4 | 6 | 0 | –4 | –6 | –6 | –4 | 0 | 6 |
>
> If we locate the points listed above on a graph paper and draw the graph, it will actually look like the graph shown here.

[textbook_text · footnote]
> * Plotting of graphs of quadratic or cubic polynomials is not meant to be done by the students, nor is to be evaluated.

### C9 · Parabolas open up or down
`kind: teach` · `objectives: O9`
Media: existing image "Parabolic arches and a cricket six's trajectory" (old T4 O2.E1)

[textbook_text]
> In fact, for any quadratic polynomial ax² + bx + c, a ≠ 0, the graph of the corresponding equation y = ax² + bx + c has one of the two shapes either open upwards like ∪ or open downwards like ∩ depending on whether a > 0 or a < 0. (These curves are called parabolas.)

### C10 · The zeroes of a quadratic are where its parabola meets the x-axis
`kind: teach` · `objectives: O10`
Media: new image spec "Zeroes Are Where the Parabola Meets the Axis" — A parabola y = x^2 - 3x - 4 drawn on axes, opening upward, crossing the x-axis at the two marked points (-1, 0) and (4, 0) with dotted vertical lines dropping to the x-axis labelled -1 and 4, and the y-intercept at (0, -4). A small side table shows p(-1) = 0 and p(4) = 0, tying the zeroes to the crossing points.

[textbook_text]
> You can see from the table that –1 and 4 are zeroes of the quadratic polynomial. Also note from the graph that –1 and 4 are the x-coordinates of the points where the graph of y = x² – 3x – 4 intersects the x-axis. Thus, the zeroes of the quadratic polynomial x² – 3x – 4 are x-coordinates of the points where the graph of y = x² – 3x – 4 intersects the x-axis.
>
> This fact is true for any quadratic polynomial, i.e., the zeroes of a quadratic polynomial ax² + bx + c, a ≠ 0, are precisely the x-coordinates of the points where the parabola representing y = ax² + bx + c intersects the x-axis.

---

## T6 · Three Ways a Parabola Meets the Axis

### C11 · Two zeroes, one zero, or none
`kind: teach` · `objectives: O11`
Media: existing video "Three geometric cases for zeroes of a quadratic" (old T5 VID1); existing image "Three cases for zeroes of a quadratic polynomial" (old T5 O1.E1)

[textbook_text]
> From our observation earlier about the shape of the graph of y = ax² + bx + c, the following three cases can happen:
>
> Case (i) : Here, the graph cuts x-axis at two distinct points A and A′.
>
> The x-coordinates of A and A′ are the two zeroes of the quadratic polynomial ax² + bx + c in this case.
>
> Case (ii) : Here, the graph cuts the x-axis at exactly one point, i.e., at two coincident points. So, the two points A and A′ of Case (i) coincide here to become one point A.
>
> The x-coordinate of A is the only zero for the quadratic polynomial ax² + bx + c in this case.
>
> Case (iii) : Here, the graph is either completely above the x-axis or completely below the x-axis. So, it does not cut the x-axis at any point.
>
> So, the quadratic polynomial ax² + bx + c has no zero in this case.
>
> So, you can see geometrically that a quadratic polynomial can have either two distinct zeroes or two equal zeroes (i.e., one zero), or no zero. This also means that a polynomial of degree 2 has atmost two zeroes.

---

## T7 · Cubic Graphs and the At-Most-n Rule

### C12 · The graph of x³ – 4x and its three zeroes
`kind: teach` · `objectives: O12`
Media: existing image "Three cubic graphs and Table 2.2" (old T6 O1.E1; renamed at build). The image shows all three cubics and the table, and this concept uses only the first, so the fit is loose, please check.

[textbook_text]
> Now, what do you expect the geometrical meaning of the zeroes of a cubic polynomial to be? Let us find out. Consider the cubic polynomial x³ – 4x. To see what the graph of y = x³ – 4x looks like, let us list a few values of y corresponding to a few values for x as shown in the table below.
>
> | x | –2 | –1 | 0 | 1 | 2 |
> |---|---|---|---|---|---|
> | y = x³ – 4x | 0 | 3 | 0 | –3 | 0 |
>
> Locating the points of the table on a graph paper and drawing the graph, we see that the graph of y = x³ – 4x actually looks like the graph shown here.
>
> We see from the table above that –2, 0 and 2 are zeroes of the cubic polynomial x³ – 4x. Observe that –2, 0 and 2 are, in fact, the x-coordinates of the only points where the graph of y = x³ – 4x intersects the x-axis. Since the curve meets the x-axis in only these 3 points, their x-coordinates are the only zeroes of the polynomial.

### C13 · More cubics, and a polynomial of degree n has at most n zeroes
`kind: teach` · `objectives: O13`
Media: existing video "Cubic graphs and the at-most-n-zeroes rule" (old T6 VID1)

[textbook_text]
> Let us take a few more examples. Consider the cubic polynomials x³ and x³ – x². We draw the graphs of y = x³ and y = x³ – x² (shown here).
>
> Note that 0 is the only zero of the polynomial x³. Also, from the graph of y = x³, you can see that 0 is the x-coordinate of the only point where the graph of y = x³ intersects the x-axis. Similarly, since x³ – x² = x²(x – 1), 0 and 1 are the only zeroes of the polynomial x³ – x². Also, from the graph of y = x³ – x², these values are the x-coordinates of the only points where the graph of y = x³ – x² intersects the x-axis.
>
> From the examples above, we see that there are at most 3 zeroes for any cubic polynomial. In other words, any polynomial of degree 3 can have at most three zeroes.

[textbook_text · remark]
> Remark : In general, given a polynomial p(x) of degree n, the graph of y = p(x) intersects the x-axis at atmost n points. Therefore, a polynomial p(x) of degree n has at most n zeroes.

---

## T8 · Examples: Reading Zeroes from Graphs

### C14 · How many zeroes does each graph show?
`kind: exercise (worked example)` · `objectives: O14`
Media: existing video "Example 1 walkthrough — count zeroes in six graphs" (old T7 VID1); existing image "Six polynomial graphs with zero counts (Fig. 2.9)" (old T7 O1.E1; renamed at build). The book supplies its own six graphs, and the redrawn panels may not match them exactly, so the fit is loose, please check.

[question]
> Look at the graphs given below. Each is the graph of y = p(x), where p(x) is a polynomial. For each of the graphs, find the number of zeroes of p(x).

[worked solution, from source]
> (i) The number of zeroes is 1 as the graph intersects the x-axis at one point only.
> (ii) The number of zeroes is 2 as the graph intersects the x-axis at two points.
> (iii) The number of zeroes is 3. (Why?)
> (iv) The number of zeroes is 1. (Why?)
> (v) The number of zeroes is 1. (Why?)
> (vi) The number of zeroes is 4. (Why?)

### C15 · More to explore: the book's "Why?" prompts
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Why Does the Graph Cross That Often?" — A row of four small graph panels on axes: a curve crossing the x-axis at three points, a straight sloping line crossing at one point, a curve that just touches the x-axis at one point, and a wavy curve crossing at four points. Each panel is labelled only with a small letter and no counts, so the student can look at where the curve meets the x-axis.

[enrichment] `[authored answers]`
> **Q.** In the third graph, why is the number of zeroes 3?
> **A.** The graph crosses the x-axis at three different points, and each crossing point gives one zero.

[enrichment] `[authored answers]`
> **Q.** In the fourth graph, why is the number of zeroes 1?
> **A.** The graph is a straight line that is not parallel to the x-axis, so it meets the x-axis at exactly one point.

[enrichment] `[authored answers]`
> **Q.** In the fifth graph, why is the number of zeroes 1?
> **A.** The curve just touches the x-axis at a single point. One point of contact gives one zero.

[enrichment] `[authored answers]`
> **Q.** In the sixth graph, why is the number of zeroes 4?
> **A.** The graph meets the x-axis at four different points, and each gives one zero.

---

## T9 · Questions: Zeroes on the Graph

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, statement only, no working and no answer. There is no video. Hint, solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for each question.

Objectives for this set: O15 (apply): count the zeroes of a polynomial from the graph of y = p(x) by counting where the graph meets the x-axis. The six graphs are the six sub-parts (i) to (vi) of the book question, one panel each.

### C16 · Zeroes on the Graph, Q1 (i)
`objectives: O15` · Media: new image spec (**the book's own figure**, panel (i) only, shown alone; no zero counts, no contact dots, no marks, no other panels)
> The graphs of y = p(x) are given below, for some polynomials p(x). Find the number of zeroes of p(x), in each case.
> Graph (i).

### C17 · Zeroes on the Graph, Q1 (ii)
`objectives: O15` · Media: new image spec (**the book's own figure**, panel (ii) only, shown alone; no zero counts, no contact dots, no marks, no other panels)
> The graphs of y = p(x) are given below, for some polynomials p(x). Find the number of zeroes of p(x), in each case.
> Graph (ii).

### C18 · Zeroes on the Graph, Q1 (iii)
`objectives: O15` · Media: new image spec (**the book's own figure**, panel (iii) only, shown alone; no zero counts, no contact dots, no marks, no other panels)
> The graphs of y = p(x) are given below, for some polynomials p(x). Find the number of zeroes of p(x), in each case.
> Graph (iii).

### C19 · Zeroes on the Graph, Q1 (iv)
`objectives: O15` · Media: new image spec (**the book's own figure**, panel (iv) only, shown alone; no zero counts, no contact dots, no marks, no other panels)
> The graphs of y = p(x) are given below, for some polynomials p(x). Find the number of zeroes of p(x), in each case.
> Graph (iv).

### C20 · Zeroes on the Graph, Q1 (v)
`objectives: O15` · Media: new image spec (**the book's own figure**, panel (v) only, shown alone; no zero counts, no contact dots, no marks, no other panels)
> The graphs of y = p(x) are given below, for some polynomials p(x). Find the number of zeroes of p(x), in each case.
> Graph (v).

### C21 · Zeroes on the Graph, Q1 (vi)
`objectives: O15` · Media: new image spec (**the book's own figure**, panel (vi) only, shown alone; no zero counts, no contact dots, no marks, no other panels)
> The graphs of y = p(x) are given below, for some polynomials p(x). Find the number of zeroes of p(x), in each case.
> Graph (vi).

---

# M3 · Zeroes and coefficients

## T10 · Spotting the Pattern in Two Quadratics

### C22 · The zeroes of 2x² – 8x + 6, and a first pattern
`kind: teach` · `objectives: O16`
Media: existing image "Step layout for 2x² – 8x + 6 → zeroes and sum-product check" (old T9 O1.E1)

[textbook_text]
> You have already seen that zero of a linear polynomial ax + b is –b/a. We will now try to answer the question raised earlier regarding the relationship between zeroes and coefficients of a quadratic polynomial. For this, let us take a quadratic polynomial, say p(x) = 2x² – 8x + 6. In Class IX, you have learnt how to factorise quadratic polynomials by splitting the middle term. So, here we need to split the middle term '– 8x' as a sum of two terms, whose product is 6 × 2x² = 12x². So, we write
> 2x² – 8x + 6 = 2x² – 6x – 2x + 6 = 2x(x – 3) – 2(x – 3)
> = (2x – 2)(x – 3) = 2(x – 1)(x – 3)
> So, the value of p(x) = 2x² – 8x + 6 is zero when x – 1 = 0 or x – 3 = 0, i.e., when x = 1 or x = 3. So, the zeroes of 2x² – 8x + 6 are 1 and 3. Observe that :
> Sum of its zeroes = 1 + 3 = 4 = –(–8)/2 = –(Coefficient of x)/(Coefficient of x²)
> Product of its zeroes = 1 × 3 = 3 = 6/2 = Constant term/(Coefficient of x²)

### C23 · A second quadratic shows the same pattern
`kind: teach` · `objectives: O16`
Media: existing video "Two polynomials, same sum-product pattern" (old T9 VID1). The video covers both polynomials, not only this one, so the fit is loose, please check.

[textbook_text]
> Let us take one more quadratic polynomial, say, p(x) = 3x² + 5x – 2. By the method of splitting the middle term,
> 3x² + 5x – 2 = 3x² + 6x – x – 2 = 3x(x + 2) – 1(x + 2)
> = (3x – 1)(x + 2)
> Hence, the value of 3x² + 5x – 2 is zero when either 3x – 1 = 0 or x + 2 = 0, i.e., when x = 1/3 or x = –2. So, the zeroes of 3x² + 5x – 2 are 1/3 and –2. Observe that :
> Sum of its zeroes = 1/3 + (–2) = –5/3 = –(Coefficient of x)/(Coefficient of x²)
> Product of its zeroes = 1/3 × (–2) = –2/3 = Constant term/(Coefficient of x²).

---

## T11 · Sum and Product of the Zeroes of a Quadratic

### C24 · Sum and product of the zeroes: try it first
`kind: try` · `objectives: O17`
Media: new image spec "Sum and Product of Zeroes Setup" — Three polynomial cards in a row. The first shows 2x^2 - 8x + 6 with zeroes 1 and 3, the second shows 3x^2 + 5x - 2 with zeroes 1/3 and -2, and the third shows x^2 - 7x + 12 with its zeroes left as empty boxes. Under each card are two empty slots labelled 'sum of zeroes' and 'product of zeroes', and the coefficients a, b and c of each polynomial are marked.
No tool, so this concept has the statement and a prediction only. There is no try-it step. It has no textbook text of its own, because the motivating text sits in the two concepts before it.

[theorem_statement] *(authored from the chapter summary)*
> If α and β are the zeroes of the quadratic polynomial ax² + bx + c, then α + β = –b/a and αβ = c/a.

[predict] `[authored]`
> Look at the sums and products you found for the last two polynomials. Now take x² – 7x + 12. Before finding its zeroes, guess whether the sum of its two zeroes is 7 or –7, and whether their product is 12 or –12. Commit to your answers. The next concept shows why the rule holds for every quadratic.

### C25 · Why the sum and product rule works
`kind: prove` · `objectives: O18`
Media: existing video "Derivation — α + β = –b/a and αβ = c/a" (old T10 VID1); existing image "Proof layout — α + β = –b/a and αβ = c/a" (old T10 O1.E1)

[textbook_text]
> In general, if α* and β* are the zeroes of the quadratic polynomial p(x) = ax² + bx + c, a ≠ 0, then you know that x – α and x – β are the factors of p(x). Therefore,
> ax² + bx + c = k(x – α)(x – β), where k is a constant
> = k[x² – (α + β)x + αβ]
> = kx² – k(α + β)x + kαβ
> Comparing the coefficients of x², x and constant terms on both the sides, we get
> a = k, b = – k(α + β) and c = kαβ.
> This gives
> α + β = –b/a,
> αβ = c/a
> i.e.,
> sum of zeroes = α + β = –b/a = –(Coefficient of x)/(Coefficient of x²),
> product of zeroes = αβ = c/a = Constant term/(Coefficient of x²).

[textbook_text · footnote]
> * α, β are Greek letters pronounced as 'alpha' and 'beta' respectively. We will use later one more letter 'γ' pronounced as 'gamma'.

---

## T12 · Examples: Quadratic Zeroes and Coefficients

### C26 · Zeroes of x² + 7x + 10, and a check of the rule
`kind: exercise (worked example)` · `objectives: O19`
Media: existing video "Examples 2 and 3 walkthrough" (old T11 VID1). The video covers this example and the next, so the fit is loose, please check.

[question]
> Find the zeroes of the quadratic polynomial x² + 7x + 10, and verify the relationship between the zeroes and the coefficients.

[worked solution, from source]
> We have
> x² + 7x + 10 = (x + 2)(x + 5)
> So, the value of x² + 7x + 10 is zero when x + 2 = 0 or x + 5 = 0, i.e., when x = –2 or x = –5. Therefore, the zeroes of x² + 7x + 10 are –2 and –5. Now,
> sum of zeroes = –2 + (–5) = –(7) = –(7)/1 = –(Coefficient of x)/(Coefficient of x²),
> product of zeroes = (–2) × (–5) = 10 = 10/1 = Constant term/(Coefficient of x²).

### C27 · Zeroes of x² – 3, and a check of the rule
`kind: exercise (worked example)` · `objectives: O19`
Media: existing image "Examples 2 and 3 — side-by-side step layout" (old T11 O1.E1; renamed at build, since the title carries the book's example numbers). The image covers this example and the previous one, so the fit is loose, please check.

[question]
> Find the zeroes of the polynomial x² – 3 and verify the relationship between the zeroes and the coefficients.

[worked solution, from source]
> Recall the identity a² – b² = (a – b)(a + b). Using it, we can write:
> x² – 3 = (x – √3)(x + √3)
> So, the value of x² – 3 is zero when x = √3 or x = –√3.
> Therefore, the zeroes of x² – 3 are √3 and –√3.
> Now,
> sum of zeroes = √3 – √3 = 0 = –(Coefficient of x)/(Coefficient of x²),
> product of zeroes = (√3)(–√3) = –3 = –3/1 = Constant term/(Coefficient of x²).

### C28 · Building a quadratic from a sum and a product
`kind: exercise (worked example)` · `objectives: O20`
Media: existing video "Example 4 — reverse construction and the family form" (old T12 VID1); existing image "Example 4 — construct a quadratic from sum and product" (old T12 O1.E1; renamed at build)

[question]
> Find a quadratic polynomial, the sum and product of whose zeroes are –3 and 2, respectively.

[worked solution, from source]
> Let the quadratic polynomial be ax² + bx + c, and its zeroes be α and β.
> We have
> α + β = –3 = –b/a,
> and αβ = 2 = c/a.
> If a = 1, then b = 3 and c = 2.
> So, one quadratic polynomial which fits the given conditions is x² + 3x + 2.
> You can check that any other quadratic polynomial that fits these conditions will be of the form k(x² + 3x + 2), where k is real.

---

## T13 · Zeroes and Coefficients of a Cubic

### C29 · The cubic relationships: try it first
`kind: try` · `objectives: O21`
Media: new image spec "A Cubic and Its Three Zeroes" — A card for the cubic x^3 - 6x^2 + 11x - 6 with its coefficients a = 1, b = -6, c = 11 and d = -6 marked under the matching terms. Below it, three empty circles labelled alpha, beta and gamma for the zeroes, and three empty boxes labelled 'alpha + beta + gamma', 'alpha beta + beta gamma + gamma alpha' and 'alpha beta gamma'.
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[textbook_text]
> Let us now look at cubic polynomials. Do you think a similar relation holds between the zeroes of a cubic polynomial and its coefficients?

[theorem_statement] *(the book's own statement, moved here from after the check in the next concept)*
> It can be proved that if α, β, γ are the zeroes of the cubic polynomial ax³ + bx² + cx + d, then
> α + β + γ = –b/a,
> αβ + βγ + γα = c/a,
> αβγ = –d/a.

[predict] `[authored]`
> The cubic x³ – 6x² + 11x – 6 has three zeroes. Before finding them, use the statement above to guess the sum of the three zeroes, the sum of their products taken two at a time, and their product. Which of these do you expect to be positive and which negative? Commit to your answers. The next concept checks the statement on a cubic whose zeroes are given.

### C30 · Checking the cubic relationships on 2x³ – 5x² – 14x + 8
`kind: teach` · `objectives: O22`
Media: existing video "Discovering the three cubic relationships" (old T13 VID1); existing image "Three cubic relationships — verified for 2x³ – 5x² – 14x + 8" (old T13 O1.E1)

[textbook_text]
> Let us consider p(x) = 2x³ – 5x² – 14x + 8.
>
> You can check that p(x) = 0 for x = 4, –2, 1/2. Since p(x) can have atmost three zeroes, these are the zeroes of 2x³ – 5x² – 14x + 8. Now,
> sum of the zeroes = 4 + (–2) + 1/2 = 5/2 = –(–5)/2 = –(Coefficient of x²)/(Coefficient of x³),
> product of the zeroes = 4 × (–2) × 1/2 = –4 = –8/2 = –Constant term/(Coefficient of x³).
>
> However, there is one more relationship here. Consider the sum of the products of the zeroes taken two at a time. We have
> {4 × (–2)} + {(–2) × 1/2} + {1/2 × 4}
> = –8 – 1 + 2 = –7 = –14/2 = Coefficient of x/(Coefficient of x³).

---

## T14 · Examples: Cubic Zeroes and Coefficients

### C31 · Are 3, –1 and –1/3 the zeroes of 3x³ – 5x² – 11x – 3?
`kind: exercise (worked example)` · `objectives: O23`
Media: existing video "Example 5 — verify 3, –1, –1/3 are zeroes of 3x³ – 5x² – 11x – 3" (old T14 VID1; renamed at build, since the title carries the book's example number); existing image "Example 5 — verification layout for 3x³ – 5x² – 11x – 3" (old T14 O1.E1; renamed at build)

[question]
> Verify that 3, –1, –1/3 are the zeroes of the cubic polynomial p(x) = 3x³ – 5x² – 11x – 3, and then verify the relationship between the zeroes and the coefficients.

[worked solution, from source]
> Comparing the given polynomial with ax³ + bx² + cx + d, we get
> a = 3, b = –5, c = –11, d = –3. Further
> p(3) = 3 × 3³ – (5 × 3²) – (11 × 3) – 3 = 81 – 45 – 33 – 3 = 0,
> p(–1) = 3 × (–1)³ – 5 × (–1)² – 11 × (–1) – 3 = –3 – 5 + 11 – 3 = 0,
> p(–1/3) = 3 × (–1/3)³ – 5 × (–1/3)² – 11 × (–1/3) – 3,
> = –1/9 – 5/9 + 11/3 – 3 = –2/3 + 2/3 = 0
> Therefore, 3, –1 and –1/3 are the zeroes of 3x³ – 5x² – 11x – 3.
> So, we take α = 3, β = –1 and γ = –1/3.
> Now,
> α + β + γ = 3 + (–1) + (–1/3) = 2 – 1/3 = 5/3 = –(–5)/3 = –b/a,
> αβ + βγ + γα = 3 × (–1) + (–1) × (–1/3) + (–1/3) × 3 = –3 + 1/3 – 1 = –11/3 = c/a,
> αβγ = 3 × (–1) × (–1/3) = 1 = –(–3)/3 = –d/a.

[remark, from source]
> Not from the examination point of view.

---

## T15 · Questions: Zeroes and Their Sums and Products

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, statement only, no working and no answer. There is no video. Hint, solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for every question. There are no group headings, and the questions are in book order (Q1 (i) to (vi), then Q2 (i) to (vi)).

Objectives for this set: O24 (apply, evaluate): find the zeroes of given quadratics by factorising, and verify the sum and product relationships. O25 (apply): build a quadratic polynomial from a given sum and product of zeroes.

### C32 · Zeroes and Their Sums and Products, Q1 (i)
`objectives: O24` · Media: new image spec (statement only)
> Find the zeroes of the following quadratic polynomials and verify the relationship between the zeroes and the coefficients.
> (i) x² – 2x – 8

### C33 · Zeroes and Their Sums and Products, Q1 (ii)
`objectives: O24` · Media: new image spec (statement only)
> Find the zeroes of the following quadratic polynomials and verify the relationship between the zeroes and the coefficients.
> (ii) 4s² – 4s + 1

### C34 · Zeroes and Their Sums and Products, Q1 (iii)
`objectives: O24` · Media: new image spec (statement only)
> Find the zeroes of the following quadratic polynomials and verify the relationship between the zeroes and the coefficients.
> (iii) 6x² – 3 – 7x

### C35 · Zeroes and Their Sums and Products, Q1 (iv)
`objectives: O24` · Media: new image spec (statement only)
> Find the zeroes of the following quadratic polynomials and verify the relationship between the zeroes and the coefficients.
> (iv) 4u² + 8u

### C36 · Zeroes and Their Sums and Products, Q1 (v)
`objectives: O24` · Media: new image spec (statement only)
> Find the zeroes of the following quadratic polynomials and verify the relationship between the zeroes and the coefficients.
> (v) t² – 15

### C37 · Zeroes and Their Sums and Products, Q1 (vi)
`objectives: O24` · Media: new image spec (statement only)
> Find the zeroes of the following quadratic polynomials and verify the relationship between the zeroes and the coefficients.
> (vi) 3x² – x – 4

### C38 · Zeroes and Their Sums and Products, Q2 (i)
`objectives: O25` · Media: new image spec (statement only)
> Find a quadratic polynomial each with the given numbers as the sum and product of its zeroes respectively.
> (i) 1/4, –1

### C39 · Zeroes and Their Sums and Products, Q2 (ii)
`objectives: O25` · Media: new image spec (statement only)
> Find a quadratic polynomial each with the given numbers as the sum and product of its zeroes respectively.
> (ii) √2, 1/3

### C40 · Zeroes and Their Sums and Products, Q2 (iii)
`objectives: O25` · Media: new image spec (statement only)
> Find a quadratic polynomial each with the given numbers as the sum and product of its zeroes respectively.
> (iii) 0, √5

### C41 · Zeroes and Their Sums and Products, Q2 (iv)
`objectives: O25` · Media: new image spec (statement only)
> Find a quadratic polynomial each with the given numbers as the sum and product of its zeroes respectively.
> (iv) 1, 1

### C42 · Zeroes and Their Sums and Products, Q2 (v)
`objectives: O25` · Media: new image spec (statement only)
> Find a quadratic polynomial each with the given numbers as the sum and product of its zeroes respectively.
> (v) –1/4, 1/4

### C43 · Zeroes and Their Sums and Products, Q2 (vi)
`objectives: O25` · Media: new image spec (statement only)
> Find a quadratic polynomial each with the given numbers as the sum and product of its zeroes respectively.
> (vi) 4, 1

---

# M4 · Wrap-up

## T16 · Chapter Summary

### C44 · Chapter summary
`kind: summary` · `objectives: O26, O27`
Media: existing video "Chapter 2 recap — two story-lines in polynomials" (old T17 VID1; renamed at build); existing image "Chapter 2 summary infographic — two story-lines" (old T17 O1.E1; renamed at build). Two images that give away the method are also re-homed here, away from the question concepts: "Exercise 2.2 Q1 — four factoring techniques cheat-sheet" (old T15 O1.E1) and "Exercise 2.2 Q2 — template layout for all six sub-parts" (old T16 O1.E1). Both are renamed at build, since their titles carry the book's exercise numbers.

[summary_points]
> In this chapter, you have studied the following points:
> 1. Polynomials of degrees 1, 2 and 3 are called linear, quadratic and cubic polynomials respectively.
> 2. A quadratic polynomial in x with real coefficients is of the form ax² + bx + c, where a, b, c are real numbers with a ≠ 0.
> 3. The zeroes of a polynomial p(x) are precisely the x-coordinates of the points, where the graph of y = p(x) intersects the x-axis.
> 4. A quadratic polynomial can have at most 2 zeroes and a cubic polynomial can have at most 3 zeroes.
> 5. If α and β are the zeroes of the quadratic polynomial ax² + bx + c, then
> α + β = –b/a, αβ = c/a.
> 6. If α, β, γ are the zeroes of the cubic polynomial ax³ + bx² + cx + d, then
> α + β + γ = –b/a,
> αβ + βγ + γα = c/a,
> and αβγ = –d/a.

---

# Appendix A · Objectives

Format: ID · bloom level · wording · old objective(s) it carries.

| ID | Bloom | Objective | Old ID |
|---|---|---|---|
| O1 | understand | Determine the degree of a polynomial in one variable as the highest power of the variable, and tell polynomials from expressions that are not polynomials. `[authored]` | new |
| O2 | analyze | Classify polynomials as linear, quadratic, or cubic by examining their degree in one variable. | T1.O1 |
| O3 | apply | Construct polynomials of a specified degree using the standard forms ax+b, ax²+bx+c, or ax³+bx²+cx+d. | T1.O2 |
| O4 | apply | Compute the value p(k) of a polynomial p(x) at a given real number k by replacing x by k. `[authored]` | T2.O1 (part) |
| O5 | apply | Verify whether a real number k is a zero of a polynomial p(x) by checking whether p(k) = 0. `[authored]` | T2.O1 (part) |
| O6 | apply | Find the zero of a linear polynomial ax + b as –b/a and relate it to the coefficients. `[authored]` | new |
| O7 | apply | Draw the graph of a linear polynomial y=ax+b and locate its single zero at the x-intercept (-b/a, 0). | T3.O1 |
| O8 | apply | Build the graph of a quadratic polynomial y=ax²+bx+c from a table of values, as a way to see its shape (plotting is not assessed). `[authored]` | T4.O1 |
| O9 | understand | Explain why the graph of a quadratic polynomial is a parabola that opens upward when a>0 and downward when a<0. | T4.O2 |
| O10 | understand | Explain that the zeroes of a quadratic polynomial ax² + bx + c are precisely the x-coordinates of the points where the parabola y = ax² + bx + c meets the x-axis. `[authored]` | new |
| O11 | analyze | Classify the three geometric cases for the zeroes of a quadratic polynomial by whether its parabola intersects the x-axis at two, one, or zero points. | T5.O1 |
| O12 | analyze | Determine strategy for finding the real zeroes of a cubic polynomial by examining where its graph crosses the x-axis. | T6.O1 |
| O13 | create | Generalise that a polynomial of degree n has at most n real zeroes using linear, quadratic, and cubic cases as evidence. | T6.O2 |
| O14 | apply | Compute the number of real zeroes of p(x) from the graph of y=p(x) by counting the x-axis intersections. | T7.O1 |
| O15 | apply | Find the number of zeroes of a polynomial from the graph of y = p(x) by counting the points where the graph meets the x-axis. `[authored]` | T8.O1 |
| O16 | apply | Compute the sum and product of zeroes of specific quadratic polynomials by factorisation and observe that they match -b/a and c/a respectively. | T9.O1 |
| O17 | apply | State the relationship between the zeroes and coefficients of a quadratic polynomial, that for ax² + bx + c with zeroes α and β, α + β = –b/a and αβ = c/a, and predict and test it. `[authored]` | new |
| O18 | evaluate | Justify the general relationships α+β=-b/a and αβ=c/a by comparing the expansion of k(x-α)(x-β) with ax²+bx+c coefficient by coefficient. | T10.O1 |
| O19 | apply | Solve for the zeroes of a quadratic polynomial by factorisation or identity and verify the sum–product relationships with its coefficients. | T11.O1 |
| O20 | apply | Construct a quadratic polynomial given the sum and product of its zeroes using the form k(x²-sx+p). | T12.O1 |
| O21 | apply | State the relationships between the zeroes and coefficients of a cubic polynomial, that for ax³ + bx² + cx + d with zeroes α, β, γ, α + β + γ = –b/a, αβ + βγ + γα = c/a and αβγ = –d/a, and predict and test them. `[authored]` | new |
| O22 | apply | Calculate the sum, the sum of pair products, and the product of zeroes of a cubic polynomial and compare them with -b/a, c/a, and -d/a. | T13.O1 |
| O23 | apply | Compute p(k) for candidate zeroes of a cubic polynomial and confirm the relationships α+β+γ=-b/a, αβ+βγ+γα=c/a, αβγ=-d/a. | T14.O1 |
| O24 | evaluate | Find the zeroes of quadratic polynomials by choosing a suitable factorisation (middle-term split, perfect square, common factor or difference of squares), and verify that the sum of zeroes is –b/a and the product is c/a. `[authored]` | T15.O1 + T15.O2 |
| O25 | apply | Construct a quadratic polynomial from a given sum s and product p of zeroes using the form x² – sx + p or its non-zero multiple k(x² – sx + p). | T16.O1 |
| O26 | understand | Explain the six key points that synthesise polynomial classification, the geometric meaning of zeroes, and the quadratic and cubic sum-product relationships. | T17.O1 |
| O27 | analyze | Compare how zeroes of a polynomial are recovered both geometrically (as x-intercepts of y = p(x)) and algebraically (as ratios of coefficients). | T17.O2 |

Note: the old "Exercise 2.1" objective (T8.O1) is reworded as O15 so that it carries no book number. The two old objectives of the first quadratic exercise (T15.O1 find by technique, T15.O2 verify) are merged into O24, because the sub-parts of that question each carry both tasks (find the zeroes, then verify), so they are one objective. O15 and O24 each stay as one objective shared by the six sub-part concepts of their question, and O25 by the six sub-parts of the last question. The old value-of-a-polynomial objective (T2.O1) is split across O4 and O5, since value and zero are now separate concepts.

# Appendix B · Held assets (not attached to the new plan; nothing deleted)

**Eight old tools and simulations** (no tools in this chapter):
- T3 "Linear Polynomial Zero Visualizer" (T2D1)
- T4 "Quadratic Parabola Explorer (a, b, c sliders)" (T2D1)
- T5 "Parabola morph between the three cases" (SIM1, simulation)
- T5 "Predict-the-Parabola (productive failure)" (T2D1)
- T6 "Cubic Zero Discoverer" (T2D1)
- T11 "Sum & Product of Zeroes Verifier" (T2D1)
- T12 "Build-a-Quadratic-from-Zeroes Tool" (T2D1)
- T15 "Splitting the Middle Term Walkthrough" (T2D1)

**Three old question videos** (no question videos for now):
- T8 "Exercise 2.1 — model walkthrough of sub-part (i)" (VID1)
- T15 "Exercise 2.2 Q1 — model sub-parts (i) and (ii)" (VID1)
- T16 "Exercise 2.2 Q2 — model sub-parts (i) and (ii)" (VID1)

**One old question image** (it marks every x-axis contact with a dot, which would give the count away, and its title carries the book's exercise and figure numbers; replaced by six new image specs, one per sub-part, each showing only the book's own figure panel for that sub-part, alone):
- T8 "Fig. 2.10 — six graphs for Exercise 2.1" (O1.E1)

# Appendix C · Carried-over fields

Every old topic's `recall_questions`, `summary`, `key_terms`, `concept_bullets` and `detailed_summary` carry into the new topic that holds its text. They are not shown here, to keep this file reviewable. The nothing-deleted check at build time compares them field by field.

Where each old topic's text and fields land:

| Old topic | New concepts |
|---|---|
| T1 Degree and classification | C2, C3 |
| T2 Value and zero | C1 (closing paragraph), C4, C5, C6 |
| T3 Graph of a linear polynomial | C7 |
| T4 Parabola | C8, C9, C10 |
| T5 Three cases | C11 |
| T6 Cubic graphs, at most n zeroes | C12, C13 |
| T7 Example 1 | C14, C15 (the "Why?" answers) |
| T8 First exercise set (graphs) | C16–C21 |
| T9 Sum and product patterns | C22, C23 |
| T10 Deriving the quadratic formulas | C24 (statement), C25 |
| T11 Examples 2 and 3 | C26, C27 |
| T12 Example 4 | C28 |
| T13 Three cubic relationships | C29, C30 |
| T14 Example 5 | C31 |
| T15 Second exercise set, Q1 | C32–C37 |
| T16 Second exercise set, Q2 | C38–C43 |
| T17 Summary | C44 |

The old `recall_questions` of the two exercise topics T15 and T16 now belong to the single second Questions topic (T15 in the new plan).
