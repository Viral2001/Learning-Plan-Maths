# Representative learning plan: Class 10, Pair of Linear Equations in Two Variables (maths10_ch3)

A review copy of the restructured plan, down to concept level. Content is shown in full. Media are only named and never embedded.

Source: `learning_plan_std10_chap3_version1.json`. Shape follows the Class 9 circles plan and the Class 10 coordinate geometry plan.

## Read this first

**Standing decisions**
- No tools in this chapter. The ten old `2d_tool` items are held (Appendix B).
- No videos for exercise questions. Each question concept gets one hint-free image spec and no video. The three old exercise videos are held (Appendix B).
- Examples keep the existing videos and images that match them. No new example media is planned.
- No grouping inside the question topics. Each textbook question is its own concept, in textbook order, named "<set name>, Q<n>". A question with separate lettered sub-parts is split: each sub-part is its own concept, named "<set name>, Q<n> (<roman>)", and keeps its parent question's objective. A question without sub-parts is one concept. No question in this chapter has sub-parts that build on each other, so none is kept whole for that reason.
- The textbook has three exercise sets and no starred or end-of-chapter set. All three are included, each with its own new name.
- The book has no derivation for the ratio test, the substitution steps or the elimination steps, so there is no prove concept in this chapter. Each of the three is a try concept (statement and a prediction).

**What a concept entry shows**
- `kind`: try, teach, enrich, hook, exercise or summary.
- `objectives`: objective IDs. Enrichment concepts have none.
- `media`: existing assets re-homed from the old plan, new asset specs, or none. Where the old title carries a book number (Table, Figure, Example, Exercise or Chapter), it is shown as found and marked for renaming at build.
- `[block_kind]` tags are review labels only. They never reach the student.

**Text cleanup applied to everything below**
- "Fig. 3.x", "Table 3.x" and "as shown in Fig. 3.x" are removed or turned into "the table below". The figure is carried by the image.
- "Section 3.x" and "3.3.1" style numbers are removed or turned into a plain phrase.
- "Example n:" and "Exercise 3.x" labels are removed. The step labels inside solutions ("Step 1 :") and the equation numbers ("(1)") stay, because they belong to the working.
- Pairs of equations that the book stacks on two lines are written on one line, separated by " ; ".
- Book references stay only in metadata (`ncert_refs`), which is not shown here.

**Marked in the text**
- `[authored]` marks text that is not in the old plan or the book. These are predictions and new objective wording. The book has no "(Why?)" prompts in this chapter, so there are no authored answers.
- Question solutions (`steps` and `answer`) are not in the old plan. They are marked *to author* and nothing is invented here.

## Plan at a glance

| Module | Topic | Concepts |
|---|---|---|
| M1 Pairs of lines and their graphs | T1 A Puzzle at the Fair (hook) | C1 |
|  | T2 Writing a Pair of Equations | C2 |
|  | T3 Pairs of Lines and Their Solutions | C3–C5 |
|  | T4 Examples: Solving Pairs by Drawing | C6–C8 |
|  | T5 Questions: Lines, Ratios and Solutions | C9–C27 |
| M2 Solving by substitution | T6 Solving by Substitution | C28 |
|  | T7 Examples: Substitution | C29–C32 |
|  | T8 Questions: Replace and Solve | C33–C45 |
| M3 Solving by elimination | T9 Solving by Elimination | C46 |
|  | T10 Examples: Elimination | C47–C50 |
|  | T11 Questions: Eliminate and Compare | C51–C59 |
| M4 Wrap-up | T12 Chapter Summary | C60–C61 |

Totals: 61 concepts and 25 objectives. 41 question concepts (19 + 13 + 9) need a new image. 0 new videos.

---

# M1 · Pairs of lines and their graphs

## T1 · A Puzzle at the Fair (hook)

### C1 · A problem from a village fair
`kind: hook` · `is_enrichment: true` · `objectives: none`
Media: new image spec "A Day at the Village Fair" — A cheerful village fair scene with a tall Giant Wheel with a price board reading Rs 3 per ride, and a Hoopla stall where a girl, Akhila, throws a ring over prizes, with a price board reading Rs 4 per game. A small speech bubble from Akhila says she spent Rs 20 and played Hoopla half as many times as she rode the Giant Wheel. Nothing about equations is shown.

[textbook_text]
> You must have come across situations like the one given below:
> Akhila went to a fair in her village. She wanted to enjoy rides on the Giant Wheel and play Hoopla (a game in which you throw a ring on the items kept in a stall, and if the ring covers any object completely, you get it). The number of times she played Hoopla is half the number of rides she had on the Giant Wheel. If each ride costs ₹ 3, and a game of Hoopla costs ₹ 4, how would you find out the number of rides she had and how many times she played Hoopla, provided she spent ₹ 20.
>
> May be you will try it by considering different cases. If she has one ride, is it possible? Is it possible to have two rides? And so on. Or you may use the knowledge of Class IX, to represent such situations as linear equations in two variables.

*(Cleanup: the section heading is dropped. The video and image for this puzzle sit on the next concept, because they show the two equations that the hook should not give away. No words dropped.)*

---

## T2 · Writing a Pair of Equations

### C2 · Turning a story into two equations
`kind: teach` · `objectives: O1, O2`
Media: existing video "Why One Equation Cannot Fix Two Unknowns" (old T1 VID1); existing image "Akhila at the Fair — Two Conditions, Two Equations" (old T1 O1.E1)

[textbook_text]
> Let us try this approach.
> Denote the number of rides that Akhila had by x, and the number of times she played Hoopla by y. Now the situation can be represented by the two equations:
> y = (1/2) x    (1)
> 3x + 4y = 20    (2)
> Can we find the solutions of this pair of equations? There are several ways of finding these, which we will study in this chapter.

---

## T3 · Pairs of Lines and Their Solutions

### C3 · Three ways two lines can meet
`kind: teach` · `objectives: O3`
Media: existing image "Three Line Behaviours Side by Side" (old T2 O2.E1)

[textbook_text]
> A pair of linear equations which has no solution, is called an inconsistent pair of linear equations. A pair of linear equations in two variables, which has a solution, is called a consistent pair of linear equations. A pair of linear equations which are equivalent has infinitely many distinct common solutions. Such a pair is called a dependent pair of linear equations in two variables. Note that a dependent pair of linear equations is always consistent.
>
> We can now summarise the behaviour of lines representing a pair of linear equations in two variables and the existence of solutions as follows:
> (i) the lines may intersect in a single point. In this case, the pair of equations has a unique solution (consistent pair of equations).
> (ii) the lines may be parallel. In this case, the equations have no solution (inconsistent pair of equations).
> (iii) the lines may be coincident. In this case, the equations have infinitely many solutions [dependent (consistent) pair of equations].

### C4 · The ratio test: try it first
`kind: try` · `objectives: O4`
Media: new image spec "Three Pairs of Lines to Compare" — Three side-by-side cards, each holding a pair of equations with its coefficients written under it as a1, b1, c1 and a2, b2, c2: x - 2y = 0 with 3x + 4y - 20 = 0; 2x + 3y - 9 = 0 with 4x + 6y - 18 = 0; and x + 2y - 4 = 0 with 2x + 4y - 12 = 0. Beneath each card is an empty coordinate grid with the axes drawn and no lines on it.
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[textbook_text]
> Consider the following three pairs of equations.
> (i) x – 2y = 0 and 3x + 4y – 20 = 0    (The lines intersect)
> (ii) 2x + 3y – 9 = 0 and 4x + 6y – 18 = 0    (The lines coincide)
> (iii) x + 2y – 4 = 0 and 2x + 4y – 12 = 0    (The lines are parallel)

[theorem_statement] *(the book's own words, from the lines that follow its table; the lead-in "From the table above, you can observe that" is dropped because the table comes in the next concept)*
> If the lines represented by the equation
> a₁x + b₁y + c₁ = 0
> and
> a₂x + b₂y + c₂ = 0
> are
> (i) intersecting, then a₁/a₂ ≠ b₁/b₂.
> (ii) coincident, then a₁/a₂ = b₁/b₂ = c₁/c₂.
> (iii) parallel, then a₁/a₂ = b₁/b₂ ≠ c₁/c₂.

[predict] `[authored]`
> Look at x + 2y – 4 = 0 and 2x + 4y – 12 = 0. The x and y coefficients of the second equation are exactly twice those of the first, but its constant term is three times the first one's. Before you compare any ratios, guess: do the two lines cross, lie on top of each other, or never meet? Commit to an answer. The next concept compares the ratios and shows how they decide it.

### C5 · Checking the ratio test on three pairs
`kind: teach` · `objectives: O5`
Media: existing video "Connecting Ratios to Line Behaviour — a Walkthrough" (old T2 VID1); existing image "Table 3.1 — Three Line Behaviours and their Ratios" (old T2 O1.E1) [title carries a book number, renamed at build]

[textbook_text]
> Let us now write down, and compare, the values of a₁/a₂, b₁/b₂ and c₁/c₂ in all the three examples. Here, a₁, b₁, c₁ and a₂, b₂, c₂ denote the coefficients of equations given in the general form.
>
> | Sl No. | Pair of lines | a₁/a₂ | b₁/b₂ | c₁/c₂ | Compare the ratios | Graphical representation | Algebraic interpretation |
> |---|---|---|---|---|---|---|---|
> | 1. | x – 2y = 0 ; 3x + 4y – 20 = 0 | 1/3 | –2/4 | 0/–20 | a₁/a₂ ≠ b₁/b₂ | Intersecting lines | Exactly one solution (unique) |
> | 2. | 2x + 3y – 9 = 0 ; 4x + 6y – 18 = 0 | 2/4 | 3/6 | –9/–18 | a₁/a₂ = b₁/b₂ = c₁/c₂ | Coincident lines | Infinitely many solutions |
> | 3. | x + 2y – 4 = 0 ; 2x + 4y – 12 = 0 | 1/2 | 2/4 | –4/–12 | a₁/a₂ = b₁/b₂ ≠ c₁/c₂ | Parallel lines | No solution |
>
> In fact, the converse is also true for any pair of lines. You can verify them by considering some more examples by yourself.
> Let us now consider some more examples to illustrate it.

*(Cleanup: "Table 3.1" is dropped, and "in the general form in Section 3.2" is shortened to "in the general form". The book gives a table check, not a derivation, so there is no prove concept here.)*

---

## T4 · Examples: Solving Pairs by Drawing

### C6 · Do the two lines cross, and where?
`kind: exercise (worked example)` · `objectives: O6`
Media: existing video "Graphical Method Walkthrough — Example 1" (old T3 VID1) [title carries a book number, renamed at build]; existing image "Figure 3.1 — Lines AB and PQ Crossing at B(6, 0)" (old T3 O1.E1) [title carries a book number, renamed at build]

[question]
> Check graphically whether the pair of equations
> x + 3y = 6    (1)
> and
> 2x – 3y = 12    (2)
> is consistent. If so, solve them graphically.

[worked solution, from source]
> Let us draw the graphs of the Equations (1) and (2). For this, we find two solutions of each of the equations, which are given in the tables below.
>
> | x | 0 | 6 |
> |---|---|---|
> | y = (6 – x)/3 | 2 | 0 |
>
> | x | 0 | 3 |
> |---|---|---|
> | y = (2x – 12)/3 | –4 | –2 |
>
> Plot the points A(0, 2), B(6, 0), P(0, –4) and Q(3, –2) on graph paper, and join the points to form the lines AB and PQ.
> We observe that there is a point B (6, 0) common to both the lines AB and PQ. So, the solution of the pair of linear equations is x = 6 and y = 0, i.e., the given pair of equations is consistent.

*(Cleanup: "Table 3.2" becomes "the tables below", and "as shown in Fig. 3.1" is dropped because the figure is carried by the image.)*

### C7 · Two equations, one line
`kind: exercise (worked example)` · `objectives: O7`
Media: existing video "Spotting Coincident Pairs in 90 Seconds" (old T4 VID1); existing image "Two Equations Tracing the Same Line" (old T4 O1.E1)

[question]
> Graphically, find whether the following pair of equations has no solution, unique solution or infinitely many solutions:
> 5x – 8y + 1 = 0    (1)
> 3x – (24/5) y + (3/5) = 0    (2)

[worked solution, from source]
> Multiplying Equation (2) by 5/3, we get
> 5x – 8y + 1 = 0
> But, this is the same as Equation (1). Hence the lines represented by Equations (1) and (2) are coincident. Therefore, Equations (1) and (2) have infinitely many solutions.
> Plot few points on the graph and verify it yourself.

### C8 · Champa's sale: words, equations and a graph
`kind: exercise (worked example)` · `objectives: O8, O9`
Media: existing video "Word Problem to Graph — Champa's Full Translation" (old T5 VID1); existing image "Champa's Sale Scenario — Translating Words to Equations" (old T5 O1.E1); existing image "Figure 3.2 — Champa's Two Lines Crossing at (1, 0)" (old T5 O1.E2) [title carries a book number, renamed at build]

[question]
> Champa went to a 'Sale' to purchase some pants and skirts. When her friends asked her how many of each she had bought, she answered, "The number of skirts is two less than twice the number of pants purchased. Also, the number of skirts is four less than four times the number of pants purchased". Help her friends to find how many pants and skirts Champa bought.

[worked solution, from source]
> Let us denote the number of pants by x and the number of skirts by y. Then the equations formed are:
> y = 2x – 2    (1)
> and
> y = 4x – 4    (2)
> Let us draw the graphs of Equations (1) and (2) by finding two solutions for each of the equations. They are given in the tables below.
>
> | x | 2 | 0 |
> |---|---|---|
> | y = 2x – 2 | 2 | –2 |
>
> | x | 0 | 1 |
> |---|---|---|
> | y = 4x – 4 | –4 | 0 |
>
> Plot the points and draw the lines passing through them to represent the equations.
> The two lines intersect at the point (1, 0). So, x = 1, y = 0 is the required solution of the pair of linear equations, i.e., the number of pants she purchased is 1 and she did not buy any skirt.
> Verify the answer by checking whether it satisfies the conditions of the given problem.

*(Cleanup: "Table 3.3" becomes "the tables below", and "as shown in Fig. 3.2" is dropped.)*

---

## T5 · Questions: Lines, Ratios and Solutions

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, showing the statement (for a split question, the stem and that one sub-part only), no working and no answer. None of these questions comes with its own book figure, and the book prints no hint for any of them. There is no video. Solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for all 19.

Objectives for this set:
- **O10** (apply): Solve a pair of linear equations graphically, forming the pair first when it is given in words, and tell from the two lines whether the pair has one, no or infinitely many solutions. `[authored]` Used by Q1 (i)-(ii), Q4 (i)-(iv), Q5, Q7.
- **O11** (apply): Decide whether a pair of linear equations is consistent, and whether its lines intersect, are parallel or coincide, by comparing a₁/a₂, b₁/b₂ and c₁/c₂, and choose between this ratio test and drawing the lines. Used by Q2 (i)-(iii), Q3 (i)-(v), Q6 (i)-(iii).

### C9 · Lines, Ratios and Solutions, Q1 (i)
`objectives: O10` · Media: new image spec (statement and this sub-part only)
> Form the pair of linear equations in the following problems, and find their solutions graphically.
> 10 students of Class X took part in a Mathematics quiz. If the number of girls is 4 more than the number of boys, find the number of boys and girls who took part in the quiz.

### C10 · Lines, Ratios and Solutions, Q1 (ii)
`objectives: O10` · Media: new image spec (statement and this sub-part only)
> Form the pair of linear equations in the following problems, and find their solutions graphically.
> 5 pencils and 7 pens together cost ₹ 50, whereas 7 pencils and 5 pens together cost ₹ 46. Find the cost of one pencil and that of one pen.

### C11 · Lines, Ratios and Solutions, Q2 (i)
`objectives: O11` · Media: new image spec (statement and this sub-part only)
> On comparing the ratios a₁/a₂, b₁/b₂ and c₁/c₂, find out whether the lines representing the following pairs of linear equations intersect at a point, are parallel or coincident:
> 5x – 4y + 8 = 0 ; 7x + 6y – 9 = 0

### C12 · Lines, Ratios and Solutions, Q2 (ii)
`objectives: O11` · Media: new image spec (statement and this sub-part only)
> On comparing the ratios a₁/a₂, b₁/b₂ and c₁/c₂, find out whether the lines representing the following pairs of linear equations intersect at a point, are parallel or coincident:
> 9x + 3y + 12 = 0 ; 18x + 6y + 24 = 0

### C13 · Lines, Ratios and Solutions, Q2 (iii)
`objectives: O11` · Media: new image spec (statement and this sub-part only)
> On comparing the ratios a₁/a₂, b₁/b₂ and c₁/c₂, find out whether the lines representing the following pairs of linear equations intersect at a point, are parallel or coincident:
> 6x – 3y + 10 = 0 ; 2x – y + 9 = 0

### C14 · Lines, Ratios and Solutions, Q3 (i)
`objectives: O11` · Media: new image spec (statement and this sub-part only)
> On comparing the ratios a₁/a₂, b₁/b₂ and c₁/c₂, find out whether the following pair of linear equations are consistent, or inconsistent.
> 3x + 2y = 5 ; 2x – 3y = 7

### C15 · Lines, Ratios and Solutions, Q3 (ii)
`objectives: O11` · Media: new image spec (statement and this sub-part only)
> On comparing the ratios a₁/a₂, b₁/b₂ and c₁/c₂, find out whether the following pair of linear equations are consistent, or inconsistent.
> 2x – 3y = 8 ; 4x – 6y = 9

### C16 · Lines, Ratios and Solutions, Q3 (iii)
`objectives: O11` · Media: new image spec (statement and this sub-part only)
> On comparing the ratios a₁/a₂, b₁/b₂ and c₁/c₂, find out whether the following pair of linear equations are consistent, or inconsistent.
> (3/2) x + (5/3) y = 7 ; 9x – 10y = 14

### C17 · Lines, Ratios and Solutions, Q3 (iv)
`objectives: O11` · Media: new image spec (statement and this sub-part only)
> On comparing the ratios a₁/a₂, b₁/b₂ and c₁/c₂, find out whether the following pair of linear equations are consistent, or inconsistent.
> 5x – 3y = 11 ; –10x + 6y = –22

### C18 · Lines, Ratios and Solutions, Q3 (v)
`objectives: O11` · Media: new image spec (statement and this sub-part only)
> On comparing the ratios a₁/a₂, b₁/b₂ and c₁/c₂, find out whether the following pair of linear equations are consistent, or inconsistent.
> (4/3) x + 2y = 8 ; 2x + 3y = 12

### C19 · Lines, Ratios and Solutions, Q4 (i)
`objectives: O10` · Media: new image spec (statement and this sub-part only)
> Which of the following pairs of linear equations are consistent/inconsistent? If consistent, obtain the solution graphically:
> x + y = 5 ; 2x + 2y = 10

### C20 · Lines, Ratios and Solutions, Q4 (ii)
`objectives: O10` · Media: new image spec (statement and this sub-part only)
> Which of the following pairs of linear equations are consistent/inconsistent? If consistent, obtain the solution graphically:
> x – y = 8 ; 3x – 3y = 16

### C21 · Lines, Ratios and Solutions, Q4 (iii)
`objectives: O10` · Media: new image spec (statement and this sub-part only)
> Which of the following pairs of linear equations are consistent/inconsistent? If consistent, obtain the solution graphically:
> 2x + y – 6 = 0 ; 4x – 2y – 4 = 0

### C22 · Lines, Ratios and Solutions, Q4 (iv)
`objectives: O10` · Media: new image spec (statement and this sub-part only)
> Which of the following pairs of linear equations are consistent/inconsistent? If consistent, obtain the solution graphically:
> 2x – 2y – 2 = 0 ; 4x – 4y – 5 = 0

### C23 · Lines, Ratios and Solutions, Q5
`objectives: O10` · Media: new image spec (statement only)
> Half the perimeter of a rectangular garden, whose length is 4 m more than its width, is 36 m. Find the dimensions of the garden.

### C24 · Lines, Ratios and Solutions, Q6 (i)
`objectives: O11` · Media: new image spec (statement and this sub-part only)
> Given the linear equation 2x + 3y – 8 = 0, write another linear equation in two variables such that the geometrical representation of the pair so formed is:
> intersecting lines

### C25 · Lines, Ratios and Solutions, Q6 (ii)
`objectives: O11` · Media: new image spec (statement and this sub-part only)
> Given the linear equation 2x + 3y – 8 = 0, write another linear equation in two variables such that the geometrical representation of the pair so formed is:
> parallel lines

### C26 · Lines, Ratios and Solutions, Q6 (iii)
`objectives: O11` · Media: new image spec (statement and this sub-part only)
> Given the linear equation 2x + 3y – 8 = 0, write another linear equation in two variables such that the geometrical representation of the pair so formed is:
> coincident lines

### C27 · Lines, Ratios and Solutions, Q7
`objectives: O10` · Media: new image spec (statement only)
> Draw the graphs of the equations x – y + 1 = 0 and 3x + 2y – 12 = 0. Determine the coordinates of the vertices of the triangle formed by these lines and the x-axis, and shade the triangular region.

---

# M2 · Solving by substitution

## T6 · Solving by Substitution

### C28 · The substitution method: try it first
`kind: try` · `objectives: O12`
Media: existing image "Substitution Method — Three-Step Summary Layout" (old T7 O1.E1)
No tool, so this concept has the statement and a prediction only.

[textbook_text]
> In the previous section, we discussed how to solve a pair of linear equations graphically. The graphical method is not convenient in cases when the point representing the solution of the linear equations has non-integral coordinates like (√3, 2√7), (–1.75, 3.3), (4/13, 1/19), etc. There is every possibility of making mistakes while reading such coordinates. Is there any alternative method of finding the solution? There are several algebraic methods, which we shall now discuss.
>
> Substitution Method: We shall explain the method of substitution by taking some examples.

[method_statement] *(the book's own stepwise summary, which it prints after its first worked example)*
> To understand the substitution method more clearly, let us consider it stepwise:
> Step 1 : Find the value of one variable, say y in terms of the other variable, i.e., x from either equation, whichever is convenient.
> Step 2 : Substitute this value of y in the other equation, and reduce it to an equation in one variable, i.e., in terms of x, which can be solved. Sometimes, as in the examples below, you can get statements with no variable. If this statement is true, you can conclude that the pair of linear equations has infinitely many solutions. If the statement is false, then the pair of linear equations is inconsistent.
> Step 3 : Substitute the value of x (or y) obtained in Step 2 in the equation used in Step 1 to obtain the value of the other variable.

[remark, from source]
> We have substituted the value of one variable by expressing it in terms of the other variable to solve the pair of linear equations. That is why the method is known as the substitution method.

[predict] `[authored]`
> Take x + 2y = 3 and 7x – 15y = 2. Which equation would you rewrite first, and which variable would you write in terms of the other, to keep the arithmetic simple? Commit to a choice. The worked solution in the next topic shows how the steps play out.

*(Cleanup: "Examples 9 and 10 below" in Step 2 becomes "the examples below", because the book's numbers point to the wrong examples. The stepwise summary is moved ahead of its worked example, so the try concept can show the statement first. No words dropped.)*

---

## T7 · Examples: Substitution

### C29 · Solving a pair by substitution
`kind: exercise (worked example)` · `objectives: O13`
Media: existing video "Walkthrough of Example 4 — Substitution End-to-End" (old T7 VID1) [title carries a book number, renamed at build]

[question]
> Solve the following pair of equations by substitution method:
> 7x – 15y = 2    (1)
> x + 2y = 3    (2)

[worked solution, from source]
> Step 1 : We pick either of the equations and write one variable in terms of the other. Let us consider the Equation (2):
> x + 2y = 3
> and write it as
> x = 3 – 2y    (3)
> Step 2 : Substitute the value of x in Equation (1). We get
> 7(3 – 2y) – 15y = 2
> i.e.,    21 – 14y – 15y = 2
> i.e.,    – 29y = –19
> Therefore,    y = 19/29
> Step 3 : Substituting this value of y in Equation (3), we get
> x = 3 – 2(19/29) = 49/29
> Therefore, the solution is x = 49/29, y = 19/29.
>
> Verification : Substituting x = 49/29 and y = 19/29, you can verify that both the Equations (1) and (2) are satisfied.

### C30 · Aftab and his daughter: ages
`kind: exercise (worked example)` · `objectives: O14`
Media: existing video "Aftab and Daughter — Translate and Solve Walkthrough" (old T8 VID1); existing image "Aftab and Daughter — Age Timeline" (old T8 O1.E1)

[question]
> Solve the following question—Aftab tells his daughter, "Seven years ago, I was seven times as old as you were then. Also, three years from now, I shall be three times as old as you will be." (Isn't this interesting?) Represent this situation algebraically and graphically by the method of substitution.

[worked solution, from source]
> Let s and t be the ages (in years) of Aftab and his daughter, respectively. Then, the pair of linear equations that represent the situation is
> s – 7 = 7 (t – 7), i.e., s – 7t + 42 = 0    (1)
> and
> s + 3 = 3 (t + 3), i.e., s – 3t = 6    (2)
> Using Equation (2), we get s = 3t + 6.
> Putting this value of s in Equation (1), we get
> (3t + 6) – 7t + 42 = 0,
> i.e.,    4t = 48, which gives t = 12.
> Putting this value of t in Equation (2), we get
> s = 3 (12) + 6 = 42
> So, Aftab and his daughter are 42 and 12 years old, respectively.
> Verify this answer by checking if it satisfies the conditions of the given problems.

### C31 · Pencils and erasers: can we find each price?
`kind: exercise (worked example)` · `objectives: O15`
Media: existing video "Substitution Special Cases — Examples 6 and 7" (old T9 VID1) [title carries a book number, renamed at build]. The video covers both this concept and the next one (the book's two special-case examples), so the fit is loose, please check.

[question]
> In a shop the cost of 2 pencils and 3 erasers is ₹9 and the cost of 4 pencils and 6 erasers is ₹18. Find the cost of each pencil and each eraser.

[worked solution, from source]
> The pair of linear equations formed were:
> 2x + 3y = 9    (1)
> 4x + 6y = 18    (2)
> We first express the value of x in terms of y from the equation 2x + 3y = 9, to get
> x = (9 – 3y)/2    (3)
> Now we substitute this value of x in Equation (2), to get
> 4((9 – 3y)/2) + 6y = 18
> i.e.,    18 – 6y + 6y = 18
> i.e.,    18 = 18
> This statement is true for all values of y. However, we do not get a specific value of y as a solution. Therefore, we cannot obtain a specific value of x. This situation has arisen because both the given equations are the same. Therefore, Equations (1) and (2) have infinitely many solutions. We cannot find a unique cost of a pencil and an eraser, because there are many common solutions, to the given situation.

### C32 · Two rails: will they cross?
`kind: exercise (worked example)` · `objectives: O15`
Media: existing image "Three Substitution Outcomes Side by Side" (old T9 O1.E1). The image compares three outcomes of substitution, so it fits this concept and the one before it. The fit is loose, please check.

[question]
> Two rails are represented by the equations
> x + 2y – 4 = 0 and 2x + 4y – 12 = 0.  Will the rails cross each other?

[worked solution, from source]
> The pair of linear equations formed were:
> x + 2y – 4 = 0    (1)
> 2x + 4y – 12 = 0    (2)
> We express x in terms of y from Equation (1) to get
> x = 4 – 2y
> Now, we substitute this value of x in Equation (2) to get
> 2(4 – 2y) + 4y – 12 = 0
> i.e.,    8 – 12 = 0
> i.e.,    – 4 = 0
> which is a false statement.
> Therefore, the equations do not have a common solution. So, the two rails will not cross each other.

---

## T8 · Questions: Replace and Solve

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, showing the statement (for a split question, the stem and that one sub-part only), no working and no answer. None of these questions comes with its own book figure, and the book prints no hint for any of them. There is no video. Solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for all 13.

Objectives for this set:
- **O16** (apply): Solve a pair of linear equations by substitution, including pairs with fractions, decimals or irrational coefficients, choosing the easier variable to write first. Used by Q1 (i)-(vi), Q2.
- **O17** (apply): Form a pair of linear equations from a word problem and solve it by substitution, checking the answer against the conditions of the problem. Used by Q3 (i)-(vi).

### C33 · Replace and Solve, Q1 (i)
`objectives: O16` · Media: new image spec (statement and this sub-part only)
> Solve the following pair of linear equations by the substitution method.
> x + y = 14 ; x – y = 4

### C34 · Replace and Solve, Q1 (ii)
`objectives: O16` · Media: new image spec (statement and this sub-part only)
> Solve the following pair of linear equations by the substitution method.
> s – t = 3 ; s/3 + t/2 = 6

### C35 · Replace and Solve, Q1 (iii)
`objectives: O16` · Media: new image spec (statement and this sub-part only)
> Solve the following pair of linear equations by the substitution method.
> 3x – y = 3 ; 9x – 3y = 9

### C36 · Replace and Solve, Q1 (iv)
`objectives: O16` · Media: new image spec (statement and this sub-part only)
> Solve the following pair of linear equations by the substitution method.
> 0.2x + 0.3y = 1.3 ; 0.4x + 0.5y = 2.3

### C37 · Replace and Solve, Q1 (v)
`objectives: O16` · Media: new image spec (statement and this sub-part only)
> Solve the following pair of linear equations by the substitution method.
> √2 x + √3 y = 0 ; √3 x – √8 y = 0

### C38 · Replace and Solve, Q1 (vi)
`objectives: O16` · Media: new image spec (statement and this sub-part only)
> Solve the following pair of linear equations by the substitution method.
> 3x/2 – 5y/3 = –2 ; x/3 + y/2 = 13/6

### C39 · Replace and Solve, Q2
`objectives: O16` · Media: new image spec (statement only)
> Solve 2x + 3y = 11 and 2x – 4y = – 24 and hence find the value of 'm' for which y = mx + 3.

### C40 · Replace and Solve, Q3 (i)
`objectives: O17` · Media: new image spec (statement and this sub-part only)
> Form the pair of linear equations for the following problems and find their solution by substitution method.
> The difference between two numbers is 26 and one number is three times the other. Find them.

### C41 · Replace and Solve, Q3 (ii)
`objectives: O17` · Media: new image spec (statement and this sub-part only)
> Form the pair of linear equations for the following problems and find their solution by substitution method.
> The larger of two supplementary angles exceeds the smaller by 18 degrees. Find them.

### C42 · Replace and Solve, Q3 (iii)
`objectives: O17` · Media: new image spec (statement and this sub-part only)
> Form the pair of linear equations for the following problems and find their solution by substitution method.
> The coach of a cricket team buys 7 bats and 6 balls for ₹ 3800. Later, she buys 3 bats and 5 balls for ₹ 1750. Find the cost of each bat and each ball.

### C43 · Replace and Solve, Q3 (iv)
`objectives: O17` · Media: new image spec (statement and this sub-part only)
> Form the pair of linear equations for the following problems and find their solution by substitution method.
> The taxi charges in a city consist of a fixed charge together with the charge for the distance covered. For a distance of 10 km, the charge paid is ₹ 105 and for a journey of 15 km, the charge paid is ₹ 155. What are the fixed charges and the charge per km? How much does a person have to pay for travelling a distance of 25 km?

### C44 · Replace and Solve, Q3 (v)
`objectives: O17` · Media: new image spec (statement and this sub-part only)
> Form the pair of linear equations for the following problems and find their solution by substitution method.
> A fraction becomes 9/11, if 2 is added to both the numerator and the denominator. If, 3 is added to both the numerator and the denominator it becomes 5/6. Find the fraction.

### C45 · Replace and Solve, Q3 (vi)
`objectives: O17` · Media: new image spec (statement and this sub-part only)
> Form the pair of linear equations for the following problems and find their solution by substitution method.
> Five years hence, the age of Jacob will be three times that of his son. Five years ago, Jacob's age was seven times that of his son. What are their present ages?

---

# M3 · Solving by elimination

## T9 · Solving by Elimination

### C46 · The elimination method: try it first
`kind: try` · `objectives: O18`
Media: existing image "Elimination Method — Four-Step Summary Layout" (old T11 O1.E1)
No tool, so this concept has the statement and a prediction only.

[textbook_text]
> Now let us consider another method of eliminating (i.e., removing) one variable. This is sometimes more convenient than the substitution method. Let us see how this method works.

[method_statement] *(the book's own steps, which it prints after its first worked example)*
> Let us now note down these steps in the elimination method:
> Step 1 : First multiply both the equations by some suitable non-zero constants to make the coefficients of one variable (either x or y) numerically equal.
> Step 2 : Then add or subtract one equation from the other so that one variable gets eliminated. If you get an equation in one variable, go to Step 3.
> If in Step 2, we obtain a true statement involving no variable, then the original pair of equations has infinitely many solutions.
> If in Step 2, we obtain a false statement involving no variable, then the original pair of equations has no solution, i.e., it is inconsistent.
> Step 3 : Solve the equation in one variable (x or y) so obtained to get its value.
> Step 4 : Substitute this value of x (or y) in either of the original equations to get the value of the other variable.

[predict] `[authored]`
> Take 9x – 4y = 2000 and 7x – 3y = 2000. By what numbers would you multiply the two equations so that the coefficients of y become equal? Commit to your two multipliers. The worked solution in the next topic shows how the steps play out.

*(Cleanup: the steps are moved ahead of the worked example they follow in the book, so the try concept can show the statement first. The book's closing line "Now to illustrate it, we shall solve few more examples." leads into the next topic and is kept there, on the second worked example. No words dropped.)*

---

## T10 · Examples: Elimination

### C47 · Incomes and savings
`kind: exercise (worked example)` · `objectives: O19`
Media: existing video "Elimination Walkthrough — Income-Expenditure Example" (old T11 VID1)

[question]
> The ratio of incomes of two persons is 9 : 7 and the ratio of their expenditures is 4 : 3. If each of them manages to save ₹ 2000 per month, find their monthly incomes.

[worked solution, from source]
> Let us denote the incomes of the two person by ₹ 9x and ₹ 7x and their expenditures by ₹ 4y and ₹ 3y respectively. Then the equations formed in the situation is given by:
> 9x – 4y = 2000    (1)
> and
> 7x – 3y = 2000    (2)
> Step 1 : Multiply Equation (1) by 3 and Equation (2) by 4 to make the coefficients of y equal. Then we get the equations:
> 27x – 12y = 6000    (3)
> 28x – 12y = 8000    (4)
> Step 2 : Subtract Equation (3) from Equation (4) to eliminate y, because the coefficients of y are the same. So, we get
> (28x – 27x) – (12y – 12y) = 8000 – 6000
> i.e.,    x = 2000
> Step 3 : Substituting this value of x in (1), we get
> 9(2000) – 4y = 2000
> i.e.,    y = 4000
> So, the solution of the equations is x = 2000, y = 4000. Therefore, the monthly incomes of the persons are ₹ 18,000 and ₹ 14,000, respectively.
>
> Verification : 18000 : 14000 = 9 : 7. Also, the ratio of their expenditures = 18000 – 2000 : 14000 – 2000 = 16000 : 12000 = 4 : 3

[remark, from source]
> The method used in solving the example above is called the elimination method, because we eliminate one variable first, to get a linear equation in one variable.

### C48 · More to explore: other routes to the same answer
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Many Routes to the Same Answer" — A map-style picture with a start flag showing the pair 9x - 4y = 2000 and 7x - 3y = 2000 for the incomes problem. Four different paths lead from it, labelled 'eliminate y', 'eliminate x', 'substitution' and 'graph', and all four paths run to a single finish flag with a blank answer box.

[enrichment, from source remarks] *(two prompts from the book's remarks on the income problem; the book gives no answers and none are authored here)*
> In the example above, we eliminated y. We could also have eliminated x. Try doing it that way.
>
> You could also have used the substitution, or graphical method, to solve this problem. Try doing so, and see which method is more convenient.

### C49 · A pair with no solution, by elimination
`kind: exercise (worked example)` · `objectives: O20`
Media: existing video "Diagnosing No-Solution via Elimination — Example 9" (old T12 VID1) [title carries a book number, renamed at build]; existing image "Parallel Lines — Why 0 = 9 Appears" (old T12 O1.E1)

[textbook_text · lead-in]
> Now to illustrate it, we shall solve few more examples.

[question]
> Use elimination method to find all possible solutions of the following pair of linear equations:
> 2x + 3y = 8    (1)
> 4x + 6y = 7    (2)

[worked solution, from source]
> Step 1 : Multiply Equation (1) by 2 and Equation (2) by 1 to make the coefficients of x equal. Then we get the equations as:
> 4x + 6y = 16    (3)
> 4x + 6y = 7    (4)
> Step 2 : Subtracting Equation (4) from Equation (3),
> (4x – 4x) + (6y – 6y) = 16 – 7
> i.e.,    0 = 9, which is a false statement.
> Therefore, the pair of equations has no solution.

### C50 · Two-digit numbers and their reverses
`kind: exercise (worked example)` · `objectives: O21`
Media: existing video "Digit Reversal Problem — Both Sign Cases Walked Through" (old T13 VID1); existing image "Two Numbers 42 and 24 — Place-Value Decomposition" (old T13 O1.E1)

[question]
> The sum of a two-digit number and the number obtained by reversing the digits is 66. If the digits of the number differ by 2, find the number. How many such numbers are there?

[worked solution, from source]
> Let the ten's and the unit's digits in the first number be x and y, respectively. So, the first number may be written as 10x + y in the expanded form (for example, 56 = 10(5) + 6).
> When the digits are reversed, x becomes the unit's digit and y becomes the ten's digit. This number, in the expanded notation is 10y + x (for example, when 56 is reversed, we get 65 = 10(6) + 5).
> According to the given condition.
> (10x + y) + (10y + x) = 66
> i.e.,    11(x + y) = 66
> i.e.,    x + y = 6    (1)
> We are also given that the digits differ by 2, therefore,
> either    x – y = 2    (2)
> or    y – x = 2    (3)
> If x – y = 2, then solving (1) and (2) by elimination, we get x = 4 and y = 2.
> In this case, we get the number 42.
> If y – x = 2, then solving (1) and (3) by elimination, we get x = 2 and y = 4.
> In this case, we get the number 24.
> Thus, there are two such numbers 42 and 24.
>
> Verification : Here 42 + 24 = 66 and 4 – 2 = 2. Also 24 + 42 = 66 and 4 – 2 = 2.

---

## T11 · Questions: Eliminate and Compare

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, showing the statement (for a split question, the stem and that one sub-part only), no working and no answer. None of these questions comes with its own book figure, and the book prints no hint for any of them. There is no video. Solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for all 9.

Objectives for this set:
- **O22** (analyze): Compare the substitution and elimination methods on the same pair of linear equations and choose the more convenient approach. Used by Q1 (i)-(iv).
- **O23** (apply): Form a pair of linear equations from a word problem, solve it by elimination where a solution exists, and verify the answer against every condition of the problem. Used by Q2 (i)-(v).

### C51 · Eliminate and Compare, Q1 (i)
`objectives: O22` · Media: new image spec (statement and this sub-part only)
> Solve the following pair of linear equations by the elimination method and the substitution method:
> x + y = 5 and 2x – 3y = 4

### C52 · Eliminate and Compare, Q1 (ii)
`objectives: O22` · Media: new image spec (statement and this sub-part only)
> Solve the following pair of linear equations by the elimination method and the substitution method:
> 3x + 4y = 10 and 2x – 2y = 2

### C53 · Eliminate and Compare, Q1 (iii)
`objectives: O22` · Media: new image spec (statement and this sub-part only)
> Solve the following pair of linear equations by the elimination method and the substitution method:
> 3x – 5y – 4 = 0 and 9x = 2y + 7

### C54 · Eliminate and Compare, Q1 (iv)
`objectives: O22` · Media: new image spec (statement and this sub-part only)
> Solve the following pair of linear equations by the elimination method and the substitution method:
> x/2 + 2y/3 = –1 and x – y/3 = 3

### C55 · Eliminate and Compare, Q2 (i)
`objectives: O23` · Media: new image spec (statement and this sub-part only)
> Form the pair of linear equations in the following problems, and find their solutions (if they exist) by the elimination method:
> If we add 1 to the numerator and subtract 1 from the denominator, a fraction reduces to 1. It becomes 1/2 if we only add 1 to the denominator. What is the fraction?

### C56 · Eliminate and Compare, Q2 (ii)
`objectives: O23` · Media: new image spec (statement and this sub-part only)
> Form the pair of linear equations in the following problems, and find their solutions (if they exist) by the elimination method:
> Five years ago, Nuri was thrice as old as Sonu. Ten years later, Nuri will be twice as old as Sonu. How old are Nuri and Sonu?

### C57 · Eliminate and Compare, Q2 (iii)
`objectives: O23` · Media: new image spec (statement and this sub-part only)
> Form the pair of linear equations in the following problems, and find their solutions (if they exist) by the elimination method:
> The sum of the digits of a two-digit number is 9. Also, nine times this number is twice the number obtained by reversing the order of the digits. Find the number.

### C58 · Eliminate and Compare, Q2 (iv)
`objectives: O23` · Media: new image spec (statement and this sub-part only)
> Form the pair of linear equations in the following problems, and find their solutions (if they exist) by the elimination method:
> Meena went to a bank to withdraw ₹ 2000. She asked the cashier to give her ₹ 50 and ₹ 100 notes only. Meena got 25 notes in all. Find how many notes of ₹ 50 and ₹ 100 she received.

### C59 · Eliminate and Compare, Q2 (v)
`objectives: O23` · Media: new image spec (statement and this sub-part only)
> Form the pair of linear equations in the following problems, and find their solutions (if they exist) by the elimination method:
> A lending library has a fixed charge for the first three days and an additional charge for each day thereafter. Saritha paid ₹ 27 for a book kept for seven days, while Susy paid ₹ 21 for the book she kept for five days. Find the fixed charge and the charge for each extra day.

---

# M4 · Wrap-up

## T12 · Chapter Summary

### C60 · Chapter summary
`kind: summary` · `objectives: O24, O25`
Media: existing video "Chapter 3 Recap — Three Methods in Three Minutes" (old T15 VID1) [title carries a book number, renamed at build]; existing image "Chapter 3 Master Summary — Methods and Cases" (old T15 O1.E1) [title carries a book number, renamed at build]; existing image "Ratio-Test Quick-Reference Card" (old T6 O2.E1); existing image "Rearrangement Strategy Decision Tree" (old T10 O1.E1); existing image "Method-Choice Flowchart — Substitution vs Elimination" (old T14 O2.E1)
Three images that give away the method are also re-homed here from the old practice topics, so they are not attached to any question concept.

[summary_points]
> In this chapter, you have studied the following points:
> 1. A pair of linear equations in two variables can be represented, and solved, by the:
> (i) graphical method
> (ii) algebraic method
> 2. Graphical Method:
> The graph of a pair of linear equations in two variables is represented by two lines.
> (i) If the lines intersect at a point, then that point gives the unique solution of the two equations. In this case, the pair of equations is consistent.
> (ii) If the lines coincide, then there are infinitely many solutions — each point on the line being a solution. In this case, the pair of equations is dependent (consistent).
> (iii) If the lines are parallel, then the pair of equations has no solution. In this case, the pair of equations is inconsistent.
> 3. Algebraic Methods: We have discussed the following methods for finding the solution(s) of a pair of linear equations:
> (i) Substitution Method
> (ii) Elimination Method
> 4. If a pair of linear equations is given by a₁x + b₁y + c₁ = 0 and a₂x + b₂y + c₂ = 0, then the following situations can arise:
> (i) a₁/a₂ ≠ b₁/b₂ : In this case, the pair of linear equations is consistent.
> (ii) a₁/a₂ = b₁/b₂ ≠ c₁/c₂ : In this case, the pair of linear equations is inconsistent.
> (iii) a₁/a₂ = b₁/b₂ = c₁/c₂ : In this case, the pair of linear equations is dependent and consistent.

### C61 · A note on equations that are not linear at first
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Disguised Linear Equations" — A two-step transformation picture. On the left, a pair of equations of the form a/x + b/y = c and d/x + e/y = f, in a box labelled 'not linear at first'. An arrow labelled 'let p = 1/x and q = 1/y' leads to the right, where the pair becomes ap + bq = c and dp + eq = f in a box labelled 'a pair of linear equations'.

[summary_points · closing point]
> 5. There are several situations which can be mathematically represented by two equations that are not linear to start with. But we alter them so that they are reduced to a pair of linear equations.

---

# Appendix A · Objectives

Format: ID · bloom level · wording · old objective(s) it carries.

| ID | Bloom | Objective | Old ID |
|---|---|---|---|
| O1 | apply | Construct a pair of linear equations in two variables to represent a real-life situation involving two related unknowns. | T1.O1 |
| O2 | understand | Explain why a single linear equation in two variables cannot by itself determine both unknowns. | T1.O2 |
| O3 | understand | Explain how the graphical behaviour (intersecting, coincident, parallel) of two lines corresponds to the number of solutions of the pair. | T2.O2 |
| O4 | apply | State the ratio test, that for a₁x + b₁y + c₁ = 0 and a₂x + b₂y + c₂ = 0 the lines intersect if a₁/a₂ ≠ b₁/b₂, coincide if a₁/a₂ = b₁/b₂ = c₁/c₂ and are parallel if a₁/a₂ = b₁/b₂ ≠ c₁/c₂, and predict and test it on a pair. `[authored]` | new |
| O5 | apply | Compute and compare the ratios a₁/a₂, b₁/b₂ and c₁/c₂ to decide whether a given pair of linear equations is consistent, dependent-consistent or inconsistent. | T2.O1 |
| O6 | apply | Solve a pair of linear equations graphically when the lines intersect, reading the intersection coordinates as the unique solution. | T3.O1 |
| O7 | apply | Solve a pair of coincident linear equations by showing that both equations reduce to the same equation and therefore share infinitely many solutions. | T4.O1 |
| O8 | apply | Construct a pair of linear equations from a word problem and solve it graphically to find the unknown quantities. | T5.O1 |
| O9 | analyze | Classify the graphical solution as valid or invalid by checking each condition stated in the word problem. | T5.O2 |
| O10 | apply | Solve a pair of linear equations graphically, forming the pair first when it is given in words, and tell from the two lines whether the pair has one, no or infinitely many solutions. `[authored]` | new |
| O11 | apply | Decide whether a pair of linear equations is consistent, and whether its lines intersect, are parallel or coincide, by comparing a₁/a₂, b₁/b₂ and c₁/c₂, and choose between this ratio test and drawing the lines. | T6.O1, T6.O2 |
| O12 | apply | State the substitution method (write one variable in terms of the other, substitute it in the other equation, then substitute back), say what a true or a false statement with no variable tells about the pair, and predict which variable to write first. `[authored]` | new |
| O13 | apply | Solve a pair of linear equations by substitution, expressing one variable in terms of the other and reducing the system to a single-variable equation. | T7.O1 |
| O14 | apply | Construct and solve a pair of linear equations for age and cost word problems by the substitution method, verifying solutions against the given conditions. | T8.O1 |
| O15 | apply | Solve a pair of linear equations by substitution, using an identity or a contradiction in the final statement to conclude whether the pair has infinite or no solutions. | T9.O1 |
| O16 | apply | Solve a pair of linear equations by substitution, including pairs with fractions, decimals or irrational coefficients, choosing the easier variable to write first. | T10.O1 (part) |
| O17 | apply | Form a pair of linear equations from a word problem and solve it by substitution, checking the answer against the conditions of the problem. | T10.O1 (part) |
| O18 | apply | State the elimination method (make the coefficients of one variable numerically equal, add or subtract the equations, solve, then substitute back), say what a true or a false statement with no variable tells about the pair, and predict the multipliers for a given pair. `[authored]` | new |
| O19 | apply | Solve a pair of linear equations by the elimination method, equalising the coefficients of one variable by multiplication and adding or subtracting the equations to remove that variable. | T11.O1 |
| O20 | apply | Solve a pair of linear equations by elimination and interpret an identity or contradiction in the final equation as diagnostic of infinite or no solutions respectively. | T12.O1 |
| O21 | apply | Solve two-digit-number and digit-reversal word problems by constructing a pair of linear equations in place-value form 10x + y and applying elimination to each sign-case. | T13.O1 |
| O22 | analyze | Compare the substitution and elimination methods on the same pair of linear equations and choose the more convenient approach. | T14.O2 |
| O23 | apply | Form a pair of linear equations from a word problem, solve it by elimination where a solution exists, and verify the answer against every condition of the problem. | T14.O1, T14.O3 |
| O24 | understand | Explain, using the ratio test on a₁/a₂, b₁/b₂ and c₁/c₂, how the coefficients of a pair of linear equations determine whether it is consistent, dependent or inconsistent. `[authored]` | T15.O1 |
| O25 | analyze | Compare the graphical, substitution, and elimination methods in terms of suitability for different types of equation pairs. | T15.O2 |

Note: the old "choose a strategy" objectives (T6.O2, T10.O1, T14.O2) are folded into the practice-set and comparison objectives. The old summary objective T15.O1 is reworded to name the ratio test, as the criterion it rests on.

# Appendix B · Held assets (not attached to the new plan; nothing deleted)

**10 old tools** (no tools in this chapter):
- T1 "Word Problem → Equation Translator" (T2D1)
- T2 "Ratio Comparator (a₁/a₂, b₁/b₂, c₁/c₂)" (T2D1)
- T2 "Consistent vs Inconsistent vs Dependent Sorter" (T2D2)
- T3 "Two-Line Grapher (live slope/intercept)" (T2D1)
- T5 "Graphical Solution Finder" (T2D1)
- T6 "Triangle from Two Lines Explorer" (T2D1)
- T7 "Substitution Method Walkthrough" (T2D1)
- T8 "Age Problem Solver" (T2D1)
- T11 "Elimination Method Walkthrough" (T2D1)
- T15 "Three Cases Visualizer (side-by-side)" (T2D1)

**3 old question videos** (no question videos for now):
- "Exercise 3.1 Q1(i) — Quiz Word Problem Walkthrough" (T6 VID1)
- "Bats-and-Balls + Taxi-Fare — Q3(iii) and Q3(iv) Walkthrough" (T10 VID1)
- "Library-Charge Word Problem — Exercise 3.3 Q2(v) Walkthrough" (T14 VID1)

# Appendix C · Carried-over fields

Every old topic's `recall_questions`, `summary`, `key_terms`, `concept_bullets` and `detailed_summary` carry into the new topic that holds its text. They are not shown here, to keep this file reviewable. The nothing-deleted check at build time compares them field by field.
