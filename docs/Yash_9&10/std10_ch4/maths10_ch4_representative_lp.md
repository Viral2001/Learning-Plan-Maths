# Representative learning plan: Class 10, Quadratic Equations (maths10_ch4)

A review copy of the restructured plan, down to concept level. Content is shown in full. Media are only named and never embedded.

Source: `learning_plan_std10_chap4_version1.json`. Shape follows the Class 9 circles plan and the Class 10 pair-of-linear-equations plan.

## Read this first

**Standing decisions**
- No tools in this chapter. The seven old `2d_tool` items are held (Appendix B). The two "try it first" concepts (the factorisation method and the nature of roots) therefore carry the statement and a prediction only. There is no try-it step.
- No videos for exercise questions. Each question concept gets one hint-free image spec and no video. The six old question videos are held (Appendix B).
- Examples keep the existing videos and images that match them. No new example media is planned.
- No grouping inside the question topics. Each textbook question is its own concept, in textbook order, named "<set name>, Q<n>". A question with separate sub-parts is split: each sub-part is its own concept, named "<set name>, Q<n> (<roman>)", and keeps its parent question's objectives. A question without sub-parts is one concept. No question in this chapter has sub-parts that build on each other, so none is kept whole for that reason.
- The textbook has three exercise sets and no starred or end-of-chapter set. All three are included, each with its own new name. 12 + 10 + 8 = 30 question concepts.
- The book prints no derivation of the quadratic formula in this edition (it states the formula at the start of the nature-of-roots section). It does reason case by case from the formula to the three discriminant cases, so that reasoning is a prove concept (C36) after its try concept (C35), sharing one theorem id. The factorisation method has no derivation, so it is a try concept only (C20), as the methods were in the pair-of-linear-equations plan.

**What a concept entry shows**
- `kind`: try, prove, teach, enrich, hook, exercise or summary.
- `objectives`: objective IDs. Enrichment concepts have none.
- `media`: existing assets re-homed from the old plan, new asset specs, or none. The notation "old T<n> <suffix>" gives the old topic number and the tail of the old media id, e.g. VID1, O1.E1. Where the old title carries a book number (Example, Exercise or Chapter), it is shown as found and marked for renaming at build.
- `[block_kind]` tags are review labels only. They never reach the student.

**Text cleanup applied to everything below**
- "Fig. 4.1", "Fig. 4.2" and "(see Fig. 4.x)" are removed. The figure is carried by the image where one exists.
- "Section 4.1" becomes "at the start of the chapter" or "earlier". "Chapter 2" becomes "earlier". Section headings such as "4.2 Quadratic Equations" are dropped.
- "Example n:", "Exercise 4.x" and the "EXERCISE" heading labels are removed. The one question that points to a book example by number (second set, Q2) is reworded and the example's two problems are written out (see that topic's note).
- Book references stay only in metadata (`ncert_refs`), which is not shown here.

**Marked in the text**
- `[authored]` marks text that is not in the old plan or the book. These are predictions, answers to the two "(Why?)" prompts and new or reworded objective wording.
- Question solutions (`steps` and `answer`) are not in the old plan. They are marked *to author* and nothing is invented here.

**Moved or lightly edited text (all other text is verbatim)**
- The sentence "In this chapter, you will study quadratic equations, ..." is moved ahead of the history paragraph so the hook (C1) ends on what the chapter does. The history paragraph becomes its own enrichment concept (C2).
- The last paragraph of the roots section ("You have learnt in Class IX, how to factorise ...") opens the factorisation try concept (C20) instead of closing the roots concept.
- The factorisation method statement in C20 is the book's own summary point 3, repeated from the chapter summary, because the book has no stepwise statement of the method inside the section.
- The reprint's opening line of the nature-of-roots section reads "The equation ax² + bx + c = 0 are given by"; "roots of" is restored in C35 ("The roots of the equation ...").

## Plan at a glance

| Module | Topic | Concepts |
|---|---|---|
| M1 What a quadratic equation is | T1 A Prayer Hall to Build (hook) | C1–C2 |
|  | T2 Quadratic Equations and Their Standard Form | C3 |
|  | T3 Examples: Forming and Recognising Quadratic Equations | C4–C6 |
|  | T4 Questions: Spotting and Forming Quadratics | C7–C18 |
| M2 Solving by factorisation | T5 Roots and the Factorisation Method | C19–C20 |
|  | T6 Examples: Factorisation | C21–C24 |
|  | T7 Questions: Roots by Factorisation | C25–C34 |
| M3 Nature of roots | T8 The Discriminant and the Nature of Roots | C35–C36 |
|  | T9 Examples: Nature of Roots | C37–C40 |
|  | T10 Questions: The Discriminant at Work | C41–C48 |
| M4 Wrap-up | T11 Chapter Summary | C49 |

Totals: 49 concepts and 24 objectives. 30 question concepts (12 + 10 + 8) need a new image. 0 new videos.

Media: 37 old media = 23 attached (9 videos, 14 images) + 14 held (7 tools, 6 question videos, 1 image that shows a question's answer).

---

# M1 · What a quadratic equation is

## T1 · A Prayer Hall to Build (hook)

### C1 · A prayer hall and its equation
`kind: hook` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Planning a Prayer Hall" — A top-down plan of a rectangular prayer hall floor with a carpet in the middle. The shorter side is labelled 'breadth x metres' and the longer side 'length (2x + 1) metres'. A banner above reads 'carpet area 300 square metres', and a small sketch of the building with a dome and entrance sits beside the plan.

[textbook_text]
> Earlier, you have studied different types of polynomials. One type was the quadratic polynomial of the form ax² + bx + c, a ≠ 0. When we equate this polynomial to zero, we get a quadratic equation. Quadratic equations come up when we deal with many real-life situations. For instance, suppose a charity trust decides to build a prayer hall having a carpet area of 300 square metres with its length one metre more than twice its breadth. What should be the length and breadth of the hall?
> Suppose the breadth of the hall is x metres. Then, its length should be (2x + 1) metres. We can depict this information pictorially.
> Now,    area of the hall = (2x + 1). x m² = (2x² + x) m²
> So,    2x² + x = 300    (Given)
> Therefore,    2x² + x – 300 = 0
> So, the breadth of the hall should satisfy the equation 2x² + x – 300 = 0 which is a quadratic equation.
>
> In this chapter, you will study quadratic equations, and various ways of finding their roots. You will also see some applications of quadratic equations in daily life situations.

*(Cleanup: "In Chapter 2" became "Earlier", and "as shown in Fig. 4.1" is dropped. The book's hall figure has no matching old image: the only prayer-hall image (old T6 O1.E1) also shows the roots, so it sits on the worked example that solves the hall (C24). The closing sentence is moved up from after the history paragraph. No words dropped.)*

### C2 · More to explore: who first solved quadratic equations?
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: existing video "Origins of Quadratic Equations: Al-Khwarizmi to Modern Standard Form" (old T1 VID1)

[enrichment, from source]
> Many people believe that Babylonians were the first to solve quadratic equations. For instance, they knew how to find two positive numbers with a given positive sum and a given positive product, and this problem is equivalent to solving a quadratic equation of the form x² – px + q = 0. Greek mathematician Euclid developed a geometrical approach for finding out lengths which, in our present day terminology, are solutions of quadratic equations. Solving of quadratic equations, in general form, is often credited to ancient Indian mathematicians. In fact, Brahmagupta (C.E.598–665) gave an explicit formula to solve a quadratic equation of the form ax² + bx = c. Later, Sridharacharya (C.E. 1025) derived a formula, now known as the quadratic formula, (as quoted by Bhaskara II) for solving a quadratic equation by the method of completing the square. An Arab mathematician Al-Khwarizmi (about C.E. 800) also studied quadratic equations of different types. Abraham bar Hiyya Ha-Nasi, in his book 'Liber embadorum' published in Europe in C.E. 1145 gave complete solutions of different quadratic equations.

*(The video's title says it runs "to modern standard form", so it overlaps the next concept a little. The fit is loose, please check.)*

---

## T2 · Quadratic Equations and Their Standard Form

### C3 · What makes an equation quadratic
`kind: teach` · `objectives: O1`
Media: existing image "Standard Form Coefficient Map: Identifying a, b, and c" (old T1 O1.E1)

[textbook_text]
> A quadratic equation in the variable x is an equation of the form ax² + bx + c = 0, where a, b, c are real numbers, a ≠ 0. For example, 2x² + x – 300 = 0 is a quadratic equation. Similarly, 2x² – 3x + 1 = 0, 4x – 3x² + 2 = 0 and 1 – x² + 300 = 0 are also quadratic equations.
> In fact, any equation of the form p(x) = 0, where p(x) is a polynomial of degree 2, is a quadratic equation. But when we write the terms of p(x) in descending order of their degrees, then we get the standard form of the equation. That is, ax² + bx + c = 0, a ≠ 0 is called the standard form of a quadratic equation.
> Quadratic equations arise in several situations in the world around us and in different fields of mathematics. Let us consider a few examples.

*(Cleanup: the heading "4.2 Quadratic Equations" is dropped. No words dropped.)*

---

## T3 · Examples: Forming and Recognising Quadratic Equations

### C4 · Marbles and toys: writing the equation
`kind: exercise (worked example)` · `objectives: O2`
Media: new image spec "Marbles and Toys Situations" — Two side-by-side picture panels. Left panel: two children, John and Jivanti, with a shared pile of marbles labelled 45 in total; each child has a small arrow showing 5 marbles lost, and a speech bubble says the product of the marbles they have now is 124. Right panel: a small workshop with a shelf of toys, a price tag reading 'cost per toy = 55 minus number of toys made in a day', and a bill reading 'total cost Rs 750'. No equations are shown.

[question]
> Represent the following situations mathematically:
> (i) John and Jivanti together have 45 marbles. Both of them lost 5 marbles each, and the product of the number of marbles they now have is 124. We would like to find out how many marbles they had to start with.
> (ii) A cottage industry produces a certain number of toys in a day. The cost of production of each toy (in rupees) was found to be 55 minus the number of toys produced in a day. On a particular day, the total cost of production was ₹ 750. We would like to find out the number of toys produced on that day.

[worked solution, from source]
> (i) Let the number of marbles John had be x.
> Then the number of marbles Jivanti had = 45 – x (Why?).
> The number of marbles left with John, when he lost 5 marbles = x – 5
> The number of marbles left with Jivanti, when she lost 5 marbles = 45 – x – 5 = 40 – x
> Therefore, their product = (x – 5) (40 – x)
> = 40x – x² – 200 + 5x
> = – x² + 45x – 200
> So,    – x² + 45x – 200 = 124    (Given that product = 124)
> i.e.,    – x² + 45x – 324 = 0
> i.e.,    x² – 45x + 324 = 0
> Therefore, the number of marbles John had, satisfies the quadratic equation
> x² – 45x + 324 = 0
> which is the required representation of the problem mathematically.
>
> (ii) Let the number of toys produced on that day be x.
> Therefore, the cost of production (in rupees) of each toy that day = 55 – x
> So, the total cost of production (in rupees) that day = x (55 – x)
> Therefore,    x (55 – x) = 750
> i.e.,    55x – x² = 750
> i.e.,    – x² + 55x – 750 = 0
> i.e.,    x² – 55x + 750 = 0
> Therefore, the number of toys produced that day satisfies the quadratic equation
> x² – 55x + 750 = 0
> which is the required representation of the problem mathematically.

### C5 · More to explore: the book's "Why?" prompt
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Splitting 45 Marbles Between Two" — A single long bar of 45 marble icons split into two parts. The left part is labelled 'John: x marbles' and the right part is labelled 'Jivanti: ?' with a bracket over the whole bar marked 45 together.

[enrichment] `[authored answers]`
> **Q.** In the marbles problem, why does Jivanti have 45 – x marbles?
> **A.** Together they have 45 marbles. If John has x of them, the rest, 45 – x, are Jivanti's.

### C6 · Is it really quadratic? Simplify first
`kind: exercise (worked example)` · `objectives: O3`
Media: existing image "When x² Cancels: Why Equations That Look Quadratic Are Not" (old T2 O1.E1). The image uses its own equations, not the book's, and matches the remark on part (ii). The fit is loose, please check.

[question]
> Check whether the following are quadratic equations:
> (i) (x – 2)² + 1 = 2x – 3
> (ii) x(x + 1) + 8 = (x + 2) (x – 2)
> (iii) x (2x + 3) = x² + 1
> (iv) (x + 2)³ = x³ – 4

[worked solution, from source]
> (i) LHS = (x – 2)² + 1 = x² – 4x + 4 + 1 = x² – 4x + 5
> Therefore, (x – 2)² + 1 = 2x – 3 can be rewritten as
> x² – 4x + 5 = 2x – 3
> i.e.,    x² – 6x + 8 = 0
> It is of the form ax² + bx + c = 0.
> Therefore, the given equation is a quadratic equation.
>
> (ii) Since x(x + 1) + 8 = x² + x + 8 and (x + 2)(x – 2) = x² – 4
> Therefore,    x² + x + 8 = x² – 4
> i.e.,    x + 12 = 0
> It is not of the form ax² + bx + c = 0.
> Therefore, the given equation is not a quadratic equation.
>
> (iii) Here,    LHS = x (2x + 3) = 2x² + 3x
> So, x (2x + 3) = x² + 1 can be rewritten as
> 2x² + 3x = x² + 1
> Therefore, we get    x² + 3x – 1 = 0
> It is of the form ax² + bx + c = 0.
> So, the given equation is a quadratic equation.
>
> (iv) Here,    LHS = (x + 2)³ = x³ + 6x² + 12x + 8
> Therefore, (x + 2)³ = x³ – 4 can be rewritten as
> x³ + 6x² + 12x + 8 = x³ – 4
> i.e.,    6x² + 12x + 12 = 0
> or,    x² + 2x + 2 = 0
> It is of the form ax² + bx + c = 0.
> So, the given equation is a quadratic equation.

[remark, from source]
> Be careful! In (ii) above, the given equation appears to be a quadratic equation, but it is not a quadratic equation.
> In (iv) above, the given equation appears to be a cubic equation (an equation of degree 3) and not a quadratic equation. But it turns out to be a quadratic equation. As you can see, often we need to simplify the given equation before deciding whether it is quadratic or not.

---

## T4 · Questions: Spotting and Forming Quadratics

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, showing the statement (for a split question, the stem and that one sub-part only), no working and no answer. None of these questions comes with its own book figure, and the book prints no hint for any of them. There is no video. Solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for all 12.

Objectives for this set:
- **O4** (apply): Classify an equation as quadratic or not quadratic by expanding all brackets, bringing all terms to one side, simplifying, and checking whether the resulting coefficient of x² is non-zero. `[authored]` (reworded) Used by Q1 (i)-(viii).
- **O2** (apply): Construct a quadratic equation in standard form from a word problem by defining a variable x, expressing all related quantities in terms of x, and writing the given constraint as a degree-2 equation. Used by Q2 (i)-(iv).
- **O5** (evaluate): Verify that the formed equation correctly models the original situation by confirming it simplifies to ax² + bx + c = 0 with a ≠ 0 and checking the logic with a trial substitution where applicable. Used by Q2 (i)-(iv).

### C7 · Spotting and Forming Quadratics, Q1 (i)
`objectives: O4` · Media: new image spec (statement and this sub-part only)
> Check whether the following are quadratic equations:
> (x + 1)² = 2(x – 3)

### C8 · Spotting and Forming Quadratics, Q1 (ii)
`objectives: O4` · Media: new image spec (statement and this sub-part only)
> Check whether the following are quadratic equations:
> x² – 2x = (–2) (3 – x)

### C9 · Spotting and Forming Quadratics, Q1 (iii)
`objectives: O4` · Media: new image spec (statement and this sub-part only)
> Check whether the following are quadratic equations:
> (x – 2)(x + 1) = (x – 1)(x + 3)

### C10 · Spotting and Forming Quadratics, Q1 (iv)
`objectives: O4` · Media: new image spec (statement and this sub-part only)
> Check whether the following are quadratic equations:
> (x – 3)(2x + 1) = x(x + 5)

### C11 · Spotting and Forming Quadratics, Q1 (v)
`objectives: O4` · Media: new image spec (statement and this sub-part only)
> Check whether the following are quadratic equations:
> (2x – 1)(x – 3) = (x + 5)(x – 1)

### C12 · Spotting and Forming Quadratics, Q1 (vi)
`objectives: O4` · Media: new image spec (statement and this sub-part only)
> Check whether the following are quadratic equations:
> x² + 3x + 1 = (x – 2)²

### C13 · Spotting and Forming Quadratics, Q1 (vii)
`objectives: O4` · Media: new image spec (statement and this sub-part only)
> Check whether the following are quadratic equations:
> (x + 2)³ = 2x (x² – 1)

### C14 · Spotting and Forming Quadratics, Q1 (viii)
`objectives: O4` · Media: new image spec (statement and this sub-part only)
> Check whether the following are quadratic equations:
> x³ – 4x² – x + 1 = (x – 2)³

### C15 · Spotting and Forming Quadratics, Q2 (i)
`objectives: O2, O5` · Media: new image spec (statement and this sub-part only)
> Represent the following situations in the form of quadratic equations:
> The area of a rectangular plot is 528 m². The length of the plot (in metres) is one more than twice its breadth. We need to find the length and breadth of the plot.

### C16 · Spotting and Forming Quadratics, Q2 (ii)
`objectives: O2, O5` · Media: new image spec (statement and this sub-part only)
> Represent the following situations in the form of quadratic equations:
> The product of two consecutive positive integers is 306. We need to find the integers.

### C17 · Spotting and Forming Quadratics, Q2 (iii)
`objectives: O2, O5` · Media: new image spec (statement and this sub-part only)
> Represent the following situations in the form of quadratic equations:
> Rohan's mother is 26 years older than him. The product of their ages (in years) 3 years from now will be 360. We would like to find Rohan's present age.

### C18 · Spotting and Forming Quadratics, Q2 (iv)
`objectives: O2, O5` · Media: new image spec (statement and this sub-part only)
> Represent the following situations in the form of quadratic equations:
> A train travels a distance of 480 km at a uniform speed. If the speed had been 8 km/h less, then it would have taken 3 hours more to cover the same distance. We need to find the speed of the train.

*(The old plan taught Q2 as its own topic, with a "five translation steps" video and a rectangular-plot image. Both work Q2 (i) through to its equation, so both are held (Appendix B).)*

---

# M2 · Solving by factorisation

## T5 · Roots and the Factorisation Method

### C19 · What a root is
`kind: teach` · `objectives: O6`
Media: existing video "Roots and Zeroes: Why They Are the Same Values" (old T4 VID1); existing image "The Parabola and Its Roots: Zeroes Verified on the Graph" (old T4 O1.E1)

[textbook_text]
> Consider the quadratic equation 2x² – 3x + 1 = 0. If we replace x by 1 on the LHS of this equation, we get (2 × 1²) – (3 × 1) + 1 = 0 = RHS of the equation. We say that 1 is a root of the quadratic equation 2x² – 3x + 1 = 0. This also means that 1 is a zero of the quadratic polynomial 2x² – 3x + 1.
> In general, a real number α is called a root of the quadratic equation ax² + bx + c = 0, a ≠ 0 if aα² + bα + c = 0. We also say that x = α is a solution of the quadratic equation, or that α satisfies the quadratic equation. Note that the zeroes of the quadratic polynomial ax² + bx + c and the roots of the quadratic equation ax² + bx + c = 0 are the same.
> You have observed earlier that a quadratic polynomial can have at most two zeroes. So, any quadratic equation can have atmost two roots.

*(Cleanup: the heading "4.3 Solution of a Quadratic Equation by Factorisation" is dropped, and "in Chapter 2" became "earlier". The paragraph that follows in the book opens the next concept.)*

### C20 · The factorisation method: try it first
`kind: try` · `objectives: O7`
Media: new image spec "Splitting the Middle Term Setup" — A card showing the equation 2x^2 - 5x + 3 = 0 with a = 2, b = -5 and c = 3 marked under the terms. Below it, a split-the-middle-term board with the goal written as 'two numbers with product 6 and sum -5', and two empty number boxes joined by a plus sign, followed by blank factor brackets ( )( ) = 0 waiting to be filled.
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[textbook_text]
> You have learnt in Class IX, how to factorise quadratic polynomials by splitting their middle terms. We shall use this knowledge for finding the roots of a quadratic equation. Let us see how.

[method_statement] *(the book's own words, from its chapter summary, where it appears again)*
> If we can factorise ax² + bx + c, a ≠ 0, into a product of two linear factors, then the roots of the quadratic equation ax² + bx + c = 0 can be found by equating each factor to zero.

[predict] `[authored]`
> Take 2x² – 5x + 3 = 0. To split the middle term –5x, you need two numbers whose product is 2 × 3 = 6 and whose sum is –5. Guess the pair before reading on, and commit to it. The worked solution in the next topic shows how the split gives the roots.

---

## T6 · Examples: Factorisation

### C21 · Roots of 2x² – 5x + 3 = 0 by factorisation
`kind: exercise (worked example)` · `objectives: O8`
Media: existing video "Splitting Method: Examples 3, 4, and 5 Walkthrough" (old T5 VID1) [title carries a book number, renamed at build]; existing image "Example 3: Five-Step Splitting Method Layout" (old T5 O1.E1) [title carries a book number, renamed at build]. The video covers this concept and the next two (the book's three factorisation examples), so the fit is loose, please check.

[question]
> Find the roots of the equation 2x² – 5x + 3 = 0, by factorisation.

[worked solution, from source]
> Let us first split the middle term – 5x as –2x –3x [because (–2x) × (–3x) = 6x² = (2x²) × 3].
> So,    2x² – 5x + 3 = 2x² – 2x – 3x + 3 = 2x (x – 1) –3(x – 1) = (2x – 3)(x – 1)
> Now, 2x² – 5x + 3 = 0 can be rewritten as (2x – 3)(x – 1) = 0.
> So, the values of x for which 2x² – 5x + 3 = 0 are the same for which (2x – 3)(x – 1) = 0, i.e., either 2x – 3 = 0 or x – 1 = 0.
> Now, 2x – 3 = 0 gives x = 3/2 and x – 1 = 0 gives x = 1.
> So, x = 3/2 and x = 1 are the solutions of the equation.
> In other words, 1 and 3/2 are the roots of the equation 2x² – 5x + 3 = 0.
> Verify that these are the roots of the given equation.

[remark, from source]
> Note that we have found the roots of 2x² – 5x + 3 = 0 by factorising 2x² – 5x + 3 into two linear factors and equating each factor to zero.

### C22 · Roots of 6x² – x – 2 = 0
`kind: exercise (worked example)` · `objectives: O8`
Media: new image spec "A Quadratic Waiting to Be Factorised" — A clean card with the equation 6x^2 - x - 2 = 0, the coefficients a = 6, b = -1 and c = -2 labelled under the terms, and below it two empty bracket pairs ( )( ) = 0 and two empty boxes for the values of x, with nothing filled in.

[question]
> Find the roots of the quadratic equation 6x² – x – 2 = 0.

[worked solution, from source]
> We have
> 6x² – x – 2 = 6x² + 3x – 4x – 2
> = 3x (2x + 1) – 2 (2x + 1)
> = (3x – 2)(2x + 1)
> The roots of 6x² – x – 2 = 0 are the values of x for which (3x – 2)(2x + 1) = 0
> Therefore, 3x – 2 = 0 or 2x + 1 = 0,
> i.e.,    x = 2/3    or    x = –1/2
> Therefore, the roots of 6x² – x – 2 = 0 are 2/3 and –1/2.
> We verify the roots, by checking that 2/3 and –1/2 satisfy 6x² – x – 2 = 0.

### C23 · A repeated root: 3x² – 2√6 x + 2 = 0
`kind: exercise (worked example)` · `objectives: O8`
Media: new image spec "A Quadratic with Root Coefficients" — A clean card with the equation 3x^2 - 2 root 6 x + 2 = 0, with the coefficients a = 3, b = -2 root 6 and c = 2 labelled under the matching terms. Below it are empty bracket pairs ( )( ) = 0 and empty boxes for the roots of x, with nothing filled in.

[question]
> Find the roots of the quadratic equation 3x² – 2√6 x + 2 = 0.

[worked solution, from source]
> 3x² – 2√6 x + 2 = 3x² – √6 x – √6 x + 2
> = √3 x (√3 x – √2) – √2 (√3 x – √2)
> = (√3 x – √2)(√3 x – √2)
> So, the roots of the equation are the values of x for which
> (√3 x – √2)(√3 x – √2) = 0
> Now, √3 x – √2 = 0 for x = √(2/3).
> So, this root is repeated twice, one for each repeated factor √3 x – √2.
> Therefore, the roots of 3x² – 2√6 x + 2 = 0 are √(2/3), √(2/3).

### C24 · The prayer hall, solved
`kind: exercise (worked example)` · `objectives: O9`
Media: existing video "Example 6: Prayer Hall — Full Application Scaffold Solution" (old T6 VID1) [title carries a book number, renamed at build]; existing image "Prayer Hall Floor Plan: Setting Up the Area Equation" (old T6 O1.E1)

[question]
> Find the dimensions of the prayer hall discussed at the start of the chapter.

[worked solution, from source]
> Earlier, we found that if the breadth of the hall is x m, then x satisfies the equation 2x² + x – 300 = 0. Applying the factorisation method, we write this equation as
> 2x² – 24x + 25x – 300 = 0
> 2x (x – 12) + 25 (x – 12) = 0
> i.e.,    (x – 12)(2x + 25) = 0
> So, the roots of the given equation are x = 12 or x = – 12.5. Since x is the breadth of the hall, it cannot be negative.
> Thus, the breadth of the hall is 12 m. Its length = 2x + 1 = 25 m.

*(Cleanup: "discussed in Section 4.1" became "discussed at the start of the chapter", and "In Section 4.1, we found" became "Earlier, we found".)*

---

## T7 · Questions: Roots by Factorisation

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, showing the statement (for a split question, the stem and that one sub-part only), no working and no answer. None of these questions comes with its own book figure, and the book prints no hint for any of them. There is no video. Solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for all 10.
Q2 in the book reads "Solve the problems given in Example 1." It has no sub-parts of its own, so it stays one concept. The book's example number is replaced by a plain pointer, and the example's two problems are written out so the question card stands on its own.

Objectives for this set:
- **O10** (apply): Solve quadratic equations, including those with integer, √2 and fractional coefficients, by factorisation, identifying the split pair (product = a × c, sum = b) and equating each linear factor to zero. `[authored]` (reworded) Used by Q1 (i)-(v).
- **O11** (apply): Translate a word problem into a quadratic equation in standard form, solve it by factorisation, and verify that the accepted root satisfies the physical constraints of the problem. `[authored]` (reworded) Used by Q2, Q3, Q4, Q5, Q6.

### C25 · Roots by Factorisation, Q1 (i)
`objectives: O10` · Media: new image spec (statement and this sub-part only)
> Find the roots of the following quadratic equations by factorisation:
> x² – 3x – 10 = 0

### C26 · Roots by Factorisation, Q1 (ii)
`objectives: O10` · Media: new image spec (statement and this sub-part only)
> Find the roots of the following quadratic equations by factorisation:
> 2x² + x – 6 = 0

### C27 · Roots by Factorisation, Q1 (iii)
`objectives: O10` · Media: new image spec (statement and this sub-part only)
> Find the roots of the following quadratic equations by factorisation:
> √2 x² + 7x + 5√2 = 0

### C28 · Roots by Factorisation, Q1 (iv)
`objectives: O10` · Media: new image spec (statement and this sub-part only)
> Find the roots of the following quadratic equations by factorisation:
> 2x² – x + 1/8 = 0

### C29 · Roots by Factorisation, Q1 (v)
`objectives: O10` · Media: new image spec (statement and this sub-part only)
> Find the roots of the following quadratic equations by factorisation:
> 100x² – 20x + 1 = 0

### C30 · Roots by Factorisation, Q2
`objectives: O11` · Media: new image spec (statement only)
> Solve the problems given in the earlier worked example on marbles and toys:
> (i) John and Jivanti together have 45 marbles. Both of them lost 5 marbles each, and the product of the number of marbles they now have is 124. We would like to find out how many marbles they had to start with.
> (ii) A cottage industry produces a certain number of toys in a day. The cost of production of each toy (in rupees) was found to be 55 minus the number of toys produced in a day. On a particular day, the total cost of production was ₹ 750. We would like to find out the number of toys produced on that day.

### C31 · Roots by Factorisation, Q3
`objectives: O11` · Media: new image spec (statement only)
> Find two numbers whose sum is 27 and product is 182.

### C32 · Roots by Factorisation, Q4
`objectives: O11` · Media: new image spec (statement only)
> Find two consecutive positive integers, sum of whose squares is 365.

### C33 · Roots by Factorisation, Q5
`objectives: O11` · Media: new image spec (statement only)
> The altitude of a right triangle is 7 cm less than its base. If the hypotenuse is 13 cm, find the other two sides.

### C34 · Roots by Factorisation, Q6
`objectives: O11` · Media: new image spec (statement only)
> A cottage industry produces a certain number of pottery articles in a day. It was observed on a particular day that the cost of production of each article (in rupees) was 3 more than twice the number of articles produced on that day. If the total cost of production on that day was ₹ 90, find the number of articles produced and the cost of each article.

---

# M3 · Nature of roots

## T8 · The Discriminant and the Nature of Roots

### C35 · The nature of roots: try it first
`kind: try` · `objectives: O12`
Media: new image spec "What Sits Under the Square Root" — The formula x = (-b plus or minus the square root of (b^2 - 4ac)) / 2a written large, with the part b^2 - 4ac inside the square root highlighted in a box. Below it, a horizontal number line for the value of b^2 - 4ac with three labelled zones: 'positive', 'exactly zero' and 'negative'. Under each zone is an empty box labelled 'how many real roots?'.
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[textbook_text]
> The roots of the equation ax² + bx + c = 0 are given by
> x = (–b ± √(b² – 4ac)) / 2a

[theorem_statement] *(the book's own words, from the end of the section; the lead-in "So," is dropped)*
> A quadratic equation ax² + bx + c = 0 has
> (i) two distinct real roots, if b² – 4ac > 0,
> (ii) two equal real roots, if b² – 4ac = 0,
> (iii) no real roots, if b² – 4ac < 0.

[predict] `[authored]`
> In the formula, b² – 4ac sits under a square root. Before reading on, guess: if b² – 4ac is negative, can the formula give a real value of x? And if b² – 4ac is exactly 0, how many different roots do you get? Commit to both answers. The next concept shows why each case turns out the way it does.

*(Cleanup: the heading "4.4 Nature of Roots" is dropped, and "roots of" is restored in the opening line, which the reprint drops. The three-case statement is moved ahead of the reasoning that leads to it, so the try concept can show the statement first.)*

### C36 · Why the sign of b² – 4ac decides
`kind: prove` · `objectives: O13`
Media: existing video "Deriving the Quadratic Formula: Where Does It Come From?" (old T8 VID1); existing image "Three Discriminant Cases: D > 0, D = 0, D < 0" (old T8 O2.E1). The video derives the formula by completing the square, which this edition of the book does not print, so the fit is loose, please check.

[textbook_text]
> If b² – 4ac > 0, we get two distinct real roots –b/2a + √(b² – 4ac)/2a and –b/2a – √(b² – 4ac)/2a.
> If b² – 4ac = 0, then x = –b/2a ± 0, i.e., x = –b/2a or –b/2a.
> So, the roots of the equation ax² + bx + c = 0 are both –b/2a.
> Therefore, we say that the quadratic equation ax² + bx + c = 0 has two equal real roots in this case.
> If b² – 4ac < 0, then there is no real number whose square is b² – 4ac. Therefore, there are no real roots for the given quadratic equation in this case.
> Since b² – 4ac determines whether the quadratic equation ax² + bx + c = 0 has real roots or not, b² – 4ac is called the discriminant of this quadratic equation.
> Let us consider some examples.

---

## T9 · Examples: Nature of Roots

### C37 · A discriminant below zero
`kind: exercise (worked example)` · `objectives: O14`
Media: existing video "Why D < 0 Means No Real Roots: Number-Line Explanation" (old T9 VID1); existing image "Example 7: Arithmetic Layout with b = −4 Boxed" (old T9 O1.E1) [title carries a book number, renamed at build]

[question]
> Find the discriminant of the quadratic equation 2x² – 4x + 3 = 0, and hence find the nature of its roots.

[worked solution, from source]
> The given equation is of the form ax² + bx + c = 0, where a = 2, b = – 4 and c = 3. Therefore, the discriminant
> b² – 4ac = (– 4)² – (4 × 2 × 3) = 16 – 24 = – 8 < 0
> So, the given equation has no real roots.

### C38 · A pole in a circular park
`kind: exercise (worked example)` · `objectives: O15, O16`
Media: existing video "Example 8: The Circular Park — Full Worked Solution" (old T10 VID1) [title carries a book number, renamed at build]; existing image "Circular Park Geometry: Angle in a Semicircle and Pythagorean Setup" (old T10 O1.E1)

[question]
> A pole has to be erected at a point on the boundary of a circular park of diameter 13 metres in such a way that the differences of its distances from two diametrically opposite fixed gates A and B on the boundary is 7 metres. Is it possible to do so? If yes, at what distances from the two gates should the pole be erected?

[worked solution, from source]
> Let us first draw the diagram.
> Let P be the required location of the pole. Let the distance of the pole from the gate B be x m, i.e., BP = x m. Now the difference of the distances of the pole from the two gates = AP – BP (or, BP – AP) = 7 m. Therefore, AP = (x + 7) m.
> Now, AB = 13m, and since AB is a diameter,
> ∠APB = 90°    (Why?)
> Therefore,    AP² + PB² = AB²    (By Pythagoras theorem)
> i.e.,    (x + 7)² + x² = 13²
> i.e.,    x² + 14x + 49 + x² = 169
> i.e.,    2x² + 14x – 120 = 0
> So, the distance 'x' of the pole from gate B satisfies the equation
> x² + 7x – 60 = 0
> So, it would be possible to place the pole if this equation has real roots. To see if this is so or not, let us consider its discriminant. The discriminant is
> b² – 4ac = 7² – 4 × 1 × (– 60) = 289 > 0.
> So, the given quadratic equation has two real roots, and it is possible to erect the pole on the boundary of the park.
> Solving the quadratic equation x² + 7x – 60 = 0, by the quadratic formula, we get
> x = (–7 ± √289)/2 = (–7 ± 17)/2
> Therefore, x = 5 or – 12.
> Since x is the distance between the pole and the gate B, it must be positive. Therefore, x = – 12 will have to be ignored. So, x = 5.
> Thus, the pole has to be erected on the boundary of the park at a distance of 5m from the gate B and 12m from the gate A.

*(Cleanup: "(see Fig. 4.2)" is dropped. The figure is carried by the image.)*

### C39 · More to explore: the right angle at the pole
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "The Pole on the Park Boundary" — A circle representing the park with a diameter AB marked 13 m and gates A and B at its ends. A point P on the circle is joined to A and B to form a triangle, with BP labelled x m and AP labelled (x + 7) m. A question mark sits at the angle at P.

[enrichment] `[authored answers]`
> **Q.** In the circular park problem, why is ∠APB = 90°?
> **A.** AB is a diameter and P is a point on the circle, so ∠APB is an angle in a semicircle. An angle in a semicircle is a right angle.

### C40 · A discriminant equal to zero
`kind: exercise (worked example)` · `objectives: O17`
Media: existing video "D = 0: Equal Roots, Tangent Parabola, and the Shortcut x = −b/2a" (old T11 VID1); existing image "Example 9: Cancellation Highlighted in Orange" (old T11 O1.E1) [title carries a book number, renamed at build]

[question]
> Find the discriminant of the equation 3x² – 2x + 1/3 = 0 and hence find the nature of its roots. Find them, if they are real.

[worked solution, from source]
> Here a = 3, b = – 2 and c = 1/3.
> Therefore, discriminant b² – 4ac = (– 2)² – 4 × 3 × 1/3 = 4 – 4 = 0.
> Hence, the given quadratic equation has two equal real roots.
> The roots are –b/2a, –b/2a, i.e., 2/6, 2/6, i.e., 1/3, 1/3.

---

## T10 · Questions: The Discriminant at Work

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, showing the statement (for a split question, the stem and that one sub-part only), no working and no answer. None of these questions comes with its own book figure, and the book prints no hint for any of them. There is no video. Solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for all 8.

Objectives for this set:
- **O18** (apply): Calculate D = b² − 4ac for a quadratic equation, classify the nature of its roots using the three discriminant cases, and find the exact roots by the quadratic formula when real roots exist. `[authored]` (reworded) Used by Q1 (i)-(iii).
- **O19** (apply): Calculate the value(s) of k for which a quadratic equation has two equal real roots by setting D = b² − 4ac = 0, solving for k, and rejecting any value of k that makes the leading coefficient zero. `[authored]` (reworded) Used by Q2 (i)-(ii).
- **O20** (evaluate): Verify each accepted value of k by substituting into D = b² − 4ac and confirming D = 0, then state the corresponding repeated root. Used by Q2 (i)-(ii).
- **O21** (apply): Compute the discriminant of the quadratic equation formed from the conditions of a design or age problem to decide whether the described figure or situation can exist. `[authored]` (reworded) Used by Q3, Q4, Q5.
- **O22** (evaluate): Justify, from the sign of the discriminant, whether a described situation is possible, and interpret D = 0 as exactly one possible design, citing the three discriminant cases. `[authored]` (reworded) Used by Q3, Q4, Q5.

### C41 · The Discriminant at Work, Q1 (i)
`objectives: O18` · Media: new image spec (statement and this sub-part only)
> Find the nature of the roots of the following quadratic equations. If the real roots exist, find them:
> 2x² – 3x + 5 = 0

### C42 · The Discriminant at Work, Q1 (ii)
`objectives: O18` · Media: new image spec (statement and this sub-part only)
> Find the nature of the roots of the following quadratic equations. If the real roots exist, find them:
> 3x² – 4√3 x + 4 = 0

### C43 · The Discriminant at Work, Q1 (iii)
`objectives: O18` · Media: new image spec (statement and this sub-part only)
> Find the nature of the roots of the following quadratic equations. If the real roots exist, find them:
> 2x² – 6x + 3 = 0

### C44 · The Discriminant at Work, Q2 (i)
`objectives: O19, O20` · Media: new image spec (statement and this sub-part only)
> Find the values of k for each of the following quadratic equations, so that they have two equal roots.
> 2x² + kx + 3 = 0

### C45 · The Discriminant at Work, Q2 (ii)
`objectives: O19, O20` · Media: new image spec (statement and this sub-part only)
> Find the values of k for each of the following quadratic equations, so that they have two equal roots.
> kx (x – 2) + 6 = 0

### C46 · The Discriminant at Work, Q3
`objectives: O21, O22` · Media: new image spec (statement only)
> Is it possible to design a rectangular mango grove whose length is twice its breadth, and the area is 800 m²? If so, find its length and breadth.

### C47 · The Discriminant at Work, Q4
`objectives: O21, O22` · Media: new image spec (statement only)
> Is the following situation possible? If so, determine their present ages.
> The sum of the ages of two friends is 20 years. Four years ago, the product of their ages in years was 48.

### C48 · The Discriminant at Work, Q5
`objectives: O21, O22` · Media: new image spec (statement only)
> Is it possible to design a rectangular park of perimeter 80 m and area 400 m²? If so, find its length and breadth.

---

# M4 · Wrap-up

## T11 · Chapter Summary

### C49 · Chapter summary
`kind: summary` · `objectives: O23, O24`
Media: existing video "Chapter Review: Connecting All Five Ideas" (old T15 VID1); existing image "Chapter 4 Unified Framework: Five Connected Summary Points" (old T15 O1.E1) [title carries a book number, renamed at build]; existing image "Split Pair Quick Reference: Three Coefficient Types" (old T7 O1.E1); existing image "Nature of Roots: Three-Column Reference Table" (old T12 O1.E1); existing image "Finding k for Equal Roots: General Procedure and Specific Example" (old T13 O1.E1); existing image "Poshan Vatika Garden: Fencing Budget, Area Constraint, and Infeasible Case" (old T14 O1.E1)
Four images that give away a method or an answer are re-homed here from the old practice topics, so they are not attached to any question concept. The split-pair card works three of the second set's Q1 equations, and the nature-of-roots table uses the third set's Q1 equations as its examples.

[summary_points]
> In this chapter, you have studied the following points:
> 1. A quadratic equation in the variable x is of the form ax² + bx + c = 0, where a, b, c are real numbers and a ≠ 0.
> 2. A real number α is said to be a root of the quadratic equation ax² + bx + c = 0, if aα² + bα + c = 0. The zeroes of the quadratic polynomial ax² + bx + c and the roots of the quadratic equation ax² + bx + c = 0 are the same.
> 3. If we can factorise ax² + bx + c, a ≠ 0, into a product of two linear factors, then the roots of the quadratic equation ax² + bx + c = 0 can be found by equating each factor to zero.
> 4. Quadratic formula: The roots of a quadratic equation ax² + bx + c = 0 are given by (–b ± √(b² – 4ac)) / 2a, provided b² – 4ac ≥ 0.
> 5. A quadratic equation ax² + bx + c = 0 has
> (i) two distinct real roots, if b² – 4ac > 0,
> (ii) two equal roots (i.e., coincident roots), if b² – 4ac = 0, and
> (iii) no real roots, if b² – 4ac < 0.

*(Cleanup: the heading "4.5 Summary" is dropped.)*

---

# Appendix A · Objectives

Format: ID · bloom level · wording · old objective(s) it carries.

| ID | Bloom | Objective | Old ID |
|---|---|---|---|
| O1 | remember | State the standard form ax² + bx + c = 0 (a ≠ 0), identify the coefficients a, b, and c for any equation presented in standard form, and rearrange equations not in standard form before identifying the coefficients. | T1.O1 |
| O2 | apply | Construct a quadratic equation in standard form from a word problem by defining a variable x, expressing all related quantities in terms of x, and writing the given constraint as a degree-2 equation. `[authored]` | T3.O1 |
| O3 | apply | Determine whether a given algebraic equation is quadratic by expanding all brackets, collecting like terms on one side, and verifying that the simplified equation has degree 2 with a non-zero coefficient for x². | T1.O2 |
| O4 | apply | Classify an equation as quadratic or not quadratic by expanding all brackets, bringing all terms to one side, simplifying, and checking whether the resulting coefficient of x² is non-zero. `[authored]` | T2.O1 |
| O5 | evaluate | Verify that the formed equation correctly models the original situation by confirming it simplifies to ax² + bx + c = 0 with a ≠ 0 and checking the logic with a trial substitution where applicable. | T3.O2 |
| O6 | understand | Explain the definition of a root α of ax² + bx + c = 0 as a value satisfying aα² + bα + c = 0, state why the zeroes of the quadratic polynomial ax² + bx + c and the roots of the equation are identical values, and state that any quadratic equation has at most two roots. | T4.O1 |
| O7 | apply | State the factorisation method (factorise ax² + bx + c into two linear factors and equate each factor to zero) and predict the pair of numbers that splits the middle term of a given equation. `[authored]` | new |
| O8 | apply | Solve quadratic equations by the middle-term splitting method — finding a pair p, q with p × q = a × c and p + q = b, rewriting bx as px + qx, grouping the four terms in pairs, factorising each pair, and equating each resulting linear factor to zero. `[authored]` | T5.O1 |
| O9 | apply | Construct and solve a quadratic equation arising from a geometric word problem using the factorisation method, and explicitly reject any root that violates the physical constraints of the original problem, such as a negative length. | T6.O1 |
| O10 | apply | Solve quadratic equations, including those with integer, √2 and fractional coefficients, by factorisation, identifying the split pair (product = a × c, sum = b) and equating each linear factor to zero. `[authored]` | T7.O1 |
| O11 | apply | Translate a word problem into a quadratic equation in standard form, solve it by factorisation, and verify that the accepted root satisfies the physical constraints of the problem. `[authored]` | T7.O2 |
| O12 | remember | State the quadratic formula x = (−b ± √(b² − 4ac)) / 2a, define the discriminant D = b² − 4ac, and identify a, b, and c correctly (with signs) from any quadratic equation written in standard form. | T8.O1 |
| O13 | analyze | Predict the nature of the roots from the value of the discriminant D — two distinct real roots when D > 0, two equal real roots when D = 0, and no real roots when D < 0 — without fully solving the equation. | T8.O2 |
| O14 | apply | Compute D = b² − 4ac for 2x² − 4x + 3 = 0, correctly carrying the sign b = −4 throughout the calculation, confirm that D = −8 < 0, and conclude that the equation has no real roots. | T9.O1 |
| O15 | apply | Construct the equation x² + 7x − 60 = 0 from the circular-park problem using the Pythagorean theorem (∠APB = 90° by the angle-in-semicircle property), confirm D > 0, and solve using the quadratic formula, retaining only the positive root x = 5. | T10.O1 |
| O16 | evaluate | Justify the rejection of x = −12 by citing that BP is a physical distance that must be positive, demonstrating how real-world constraints determine which algebraic root is valid. | T10.O2 |
| O17 | apply | Compute D = b² − 4ac for 3x² − 2x + 1/3 = 0 by recognising the cancellation 4 × 3 × (1/3) = 4, confirm D = 0, and calculate the repeated root as −b/2a = 1/3. | T11.O1 |
| O18 | apply | Calculate D = b² − 4ac for a quadratic equation, classify the nature of its roots using the three discriminant cases, and find the exact roots by the quadratic formula when real roots exist. `[authored]` | T12.O1 |
| O19 | apply | Calculate the value(s) of k for which a quadratic equation has two equal real roots by setting D = b² − 4ac = 0, solving for k, and rejecting any value of k that makes the leading coefficient zero. `[authored]` | T13.O1 |
| O20 | evaluate | Verify each accepted value of k by substituting into D = b² − 4ac and confirming D = 0, then state the corresponding repeated root. | T13.O2 |
| O21 | apply | Compute the discriminant of the quadratic equation formed from the conditions of a design or age problem to decide whether the described figure or situation can exist. `[authored]` | T14.O1 |
| O22 | evaluate | Justify, from the sign of the discriminant, whether a described situation is possible, and interpret D = 0 as exactly one possible design, citing the three discriminant cases. `[authored]` | T14.O2 |
| O23 | understand | Explain how the standard form, the meaning of a root, the factorisation method, the quadratic formula and the three discriminant cases connect into one framework for solving and analysing quadratic equations. `[authored]` | T15.O1 |
| O24 | analyze | Distinguish between quadratic equations that are efficiently solved by factorisation — when D is a perfect square — and those requiring the quadratic formula — when D is irrational or factorisation is not obvious — using the discriminant as the decision criterion. | T15.O2 |

Notes:
- Every old objective (23) is carried; one new objective (O7) is added for the factorisation try concept. 24 in all.
- `[authored]` on a carried objective means it is reworded only to drop book numbers: "Exercise 4.1 Q1/Q2", "Exercise 4.2 Q1/Q3–Q6", "Exercise 4.3 Q1/Q2/Q3–Q5", "as demonstrated in Examples 3, 4, and 5", "Section 4.5" and the old topic numbers (T1, T4, T5–T7, T8–T14). O11 also drops "the five-step translation procedure", the scaffold of a held video.
- O22 (old T14.O2) also drops the answers it gave away for two questions: the discriminant value of the ages question and the verdict on the park question.
- O2 (old T3.O1) is anchored on the marbles-and-toys example (C4), which had no objective of its own in the old plan, and is also used by the first set's Q2.
- O12 (old T8.O1, state the formula and define D) is anchored on the try concept (C35); O13 (old T8.O2) on the prove concept (C36).
- Enrichment concepts (C1, C2, C5, C39) carry no objective.

# Appendix B · Held assets (not attached to the new plan; nothing deleted)

**Seven old tools** (no tools in this chapter):
- T4 "Root Verifier (Is x = α a Root?)" (T2D1)
- T5 "Splitting the Middle Term Walkthrough" (T2D1)
- T8 "Quadratic Formula Walkthrough" (T2D1)
- T8 "Discriminant & Nature of Roots Explorer" (T2D2)
- T10 "Geometric Quadratic Visualizer (area / Pythagoras problems)" (T2D1)
- T13 "\"Find k\" Solver (Equal Roots Condition)" (T2D1)
- T15 "Three Methods Comparator" (T2D1)

**Six old question videos** (no question videos for now):
- T2 "Classifying Equations: Worked Screencasts for Exercise 4.1 Q1" (VID1)
- T3 "The Five Translation Steps: From Words to Quadratic Equation" (VID1). It works the first set's Q2 (i) through to its equation.
- T7 "Exercise 4.2 Q3–Q6: Five-Step Word-Problem Translation Walkthrough" (VID1)
- T12 "Exercise 4.3 Q1: Full Worked Solution for All Three Equations" (VID1)
- T13 "Exercise 4.3 Q2: Finding k for Equal Roots — Narrated Worked Example" (VID1)
- T14 "Exercise 4.3 Q4: Why D < 0 Makes the Situation Impossible" (VID1)

**One old image that shows a question's answer**:
- T3 "Rectangular Plot: From Word Problem to Standard Form" (O1.E1). It shows the first set's Q2 (i) with its equation x(2x + 1) = 528 already formed, so it cannot sit on that question card, and it has no other home.

Identity: 23 attached (9 videos, 14 images) + 14 held (7 tools, 6 question videos, 1 image) = 37 old media.

# Appendix C · Carried-over fields

Every old topic's `recall_questions`, `summary`, `key_terms`, `concept_bullets` and `detailed_summary` carry into the new topic that holds its text. They are not shown here, to keep this file reviewable. The nothing-deleted check at build time compares them field by field.

Where each old topic's text and fields land (the first concept listed sets the new home topic):

| Old topic | New concepts |
|---|---|
| T1 Definition and Standard Form | C3 (the standard form), with its opening in C1–C2 and its two examples in C4–C6 |
| T2 First exercise set, Q1 | C7–C14 |
| T3 First exercise set, Q2 (forming equations) | C15–C18 |
| T4 Roots and polynomial zeroes | C19, C20 (its closing paragraph) |
| T5 Splitting the middle term (three examples) | C21–C23, with the method statement in C20 |
| T6 Prayer hall example | C24 |
| T7 Second exercise set | C25–C34 |
| T8 Quadratic formula and discriminant | C35, C36 |
| T9 Example with no real roots | C37 |
| T10 Circular park example | C38, C39 (the "Why?" answer) |
| T11 Example with equal roots | C40 |
| T12 Third exercise set, Q1 | C41–C43 |
| T13 Third exercise set, Q2 (value of k) | C44, C45 |
| T14 Third exercise set, Q3–Q5 (feasibility) | C46–C48 |
| T15 Chapter Summary | C49 |

The old `recall_questions` of the three topics T12, T13 and T14 now belong to the single third Questions topic (T10 in the new plan). The four images re-homed to the summary (from old T7, T12, T13, T14) keep their `old_media_id`.
