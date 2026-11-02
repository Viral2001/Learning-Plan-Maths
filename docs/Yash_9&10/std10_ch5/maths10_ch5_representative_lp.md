# Representative learning plan: Class 10, Arithmetic Progressions (maths10_ch5)

A review copy of the restructured plan, down to concept level. Content is shown in full. Media are only named and never embedded.

Source: `learning_plan_std10_chap5_version1.json`. Shape follows the Class 9 circles plan.

## Read this first

**Standing decisions**
- No tools in this chapter. The ten old `2d_tool` items are held (Appendix B).
- No videos for exercise questions. Each question concept gets one hint-free image spec and no video. The four old exercise videos are held.
- Examples keep the existing videos and images that match them. No new example media is planned.
- The question order inside a Questions topic is the textbook order. Independent sub-parts (i), (ii), (iii) are separate concepts.
- The fourth exercise set is marked optional in the book ("not from the examination point of view"). It is kept as its own Questions topic so nothing is lost.

**What a concept entry shows**
- `kind`: try, prove, teach, enrich, hook, exercise or summary.
- `objectives`: objective IDs. Enrichment concepts have none.
- `media`: existing assets re-homed from the old plan, new asset specs, or none.
- `[block_kind]` tags are review labels only. They never reach the student.

**Text cleanup applied to everything below**
- "Fig. 5.x" and "see Fig. 5.x" are removed, or become "as shown in the figure". The figure is carried by the image.
- "Section 5.1" becomes "earlier". "Chapter 1" (Gauss) becomes "earlier".
- Section headings ("5.2 Arithmetic Progressions"), "Example n:" and "Exercise 5.x" labels are removed.
- Book references stay only in metadata (`ncert_refs`), which is not shown here.

**Marked in the text**
- `[authored]` marks text that is not in the old plan or the book. These are predictions and answers to "(Why?)" prompts.
- Question solutions (`steps` and `answer`) are not in the old plan. They are marked *to author* and nothing is invented here.

## Plan at a glance

| Module | Topic | Concepts |
|---|---|---|
| M1 What an arithmetic progression is | T1 Patterns All Around Us (hook) | C1 |
| | T2 What Makes a List an AP | C2–C6 |
| | T3 Examples: Is It an AP? | C7–C8 |
| | T4 Questions: Is It an AP? | C9–C36 |
| M2 The nth term | T5 The nth Term of an AP | C37–C39 |
| | T6 Examples: Using the nth Term | C40–C45 |
| | T7 Examples: The nth Term in Real Situations | C46–C48 |
| | T8 Questions: The nth Term | C49–C78 |
| M3 The sum of the first n terms | T9 The Sum of the First n Terms | C79–C81 |
| | T10 Examples: Using the Sum Formula | C82–C87 |
| | T11 Questions: The Sum of n Terms | C88–C122 |
| | T12 Questions: Challenge Problems | C123–C127 |
| M4 Wrap-up | T13 Chapter Summary | C128–C129 |

Totals: 129 concepts and 24 objectives. 98 question concepts need a new image. 0 new videos. 16 worked examples.

---

# M1 · What an arithmetic progression is

## T1 · Patterns All Around Us (hook)

### C1 · Patterns in nature, and where this chapter goes
`kind: hook` · `is_enrichment: true` · `objectives: none`
Media: existing video "Spotting the Pattern — Introduction to Arithmetic Progressions" (old T1 VID1)

[textbook_text]
> You must have observed that in nature, many things follow a certain pattern, such as the petals of a sunflower, the holes of a honeycomb, the grains on a maize cob, the spirals on a pineapple and on a pine cone, etc.
>
> In this chapter, we shall discuss one of these patterns in which succeeding terms are obtained by adding a fixed number to the preceding terms. We shall also see how to find their nth terms and the sum of n consecutive terms, and use this knowledge in solving some daily life problems.

*(Cleanup: the closing "In this chapter…" paragraph is moved up from the end of the introduction so the hook says where the chapter goes. The six day-to-day examples between them open the next topic. No words dropped.)*

---

## T2 · What Makes a List an AP

### C2 · Lists from daily life
`kind: teach` · `objectives: O1`
Media: existing image "AP vs Non-AP Sequences — Pattern Comparison Chart" (old T1 O1.E1). The book's own figures of the ladder, the squares and the rabbit pairs are source figures; to be confirmed.

[textbook_text]
> We now look for some patterns which occur in our day-to-day life. Some such examples are:
> (i) Reena applied for a job and got selected. She has been offered a job with a starting monthly salary of ₹ 8000, with an annual increment of ₹ 500 in her salary. Her salary (in ₹) for the 1st, 2nd, 3rd, . . . years will be, respectively
> 8000, 8500, 9000, . . . .
> (ii) The lengths of the rungs of a ladder decrease uniformly by 2 cm from bottom to top. The bottom rung is 45 cm in length. The lengths (in cm) of the 1st, 2nd, 3rd, . . ., 8th rung from the bottom to the top are, respectively
> 45, 43, 41, 39, 37, 35, 33, 31
> (iii) In a savings scheme, the amount becomes 5/4 times of itself after every 3 years. The maturity amount (in ₹) of an investment of ₹ 8000 after 3, 6, 9 and 12 years will be, respectively:
> 10000, 12500, 15625, 19531.25
> (iv) The number of unit squares in squares with side 1, 2, 3, . . . units are, respectively
> 1², 2², 3², . . . .
> (v) Shakila puts ₹ 100 into her daughter's money box when she was one year old and increased the amount by ₹ 50 every year. The amounts of money (in ₹) in the box on the 1st, 2nd, 3rd, 4th, . . . birthday were
> 100, 150, 200, 250, . . ., respectively.
> (vi) A pair of rabbits are too young to produce in their first month. In the second, and every subsequent month, they produce a new pair. Each new pair of rabbits produce a new pair in their second month and in every subsequent month. Assuming no rabbit dies, the number of pairs of rabbits at the start of the 1st, 2nd, 3rd, . . ., 6th month, respectively are:
> 1, 1, 2, 3, 5, 8
>
> In the examples above, we observe some patterns. In some, we find that the succeeding terms are obtained by adding a fixed number, in other by multiplying with a fixed number, in another we find that they are squares of consecutive numbers, and so on.

### C3 · Adding a fixed number each time
`kind: teach` · `objectives: O2`
Media: new image spec "Five Lists, One Fixed Step" — Five horizontal strips of number tiles, one per list: 1, 2, 3, 4; 100, 70, 40, 10; -3, -2, -1, 0; 3, 3, 3, 3; and -1.0, -1.5, -2.0, -2.5. Small curved arrows between neighbouring tiles carry the fixed step added each time (+1, -30, +1, +0, -0.5), and each strip ends with three dots to show it continues.

[textbook_text]
> Consider the following lists of numbers:
> (i) 1, 2, 3, 4, . . .
> (ii) 100, 70, 40, 10, . . .
> (iii) – 3, –2, –1, 0, . . .
> (iv) 3, 3, 3, 3, . . .
> (v) –1.0, –1.5, –2.0, –2.5, . . .
>
> Each of the numbers in the list is called a term.
>
> Given a term, can you write the next term in each of the lists above? If so, how will you write it? Perhaps by following a pattern or rule. Let us observe and write the rule.
> In (i), each term is 1 more than the term preceding it.
> In (ii), each term is 30 less than the term preceding it.
> In (iii), each term is obtained by adding 1 to the term preceding it.
> In (iv), all the terms in the list are 3, i.e., each term is obtained by adding (or subtracting) 0 to the term preceding it.
> In (v), each term is obtained by adding – 0.5 to (i.e., subtracting 0.5 from) the term preceding it.
>
> In all the lists above, we see that successive terms are obtained by adding a fixed number to the preceding terms. Such list of numbers is said to form an Arithmetic Progression ( AP ).
>
> So, an arithmetic progression is a list of numbers in which each term is obtained by adding a fixed number to the preceding term except the first term.
>
> This fixed number is called the common difference of the AP. Remember that it can be positive, negative or zero.
>
> Let us denote the first term of an AP by a₁, second term by a₂, . . ., nth term by aₙ and the common difference by d. Then the AP becomes a₁, a₂, a₃, . . ., aₙ.
> So, a₂ – a₁ = a₃ – a₂ = . . . = aₙ – aₙ₋₁ = d.

### C4 · The general form, and finite and infinite APs
`kind: teach` · `objectives: O3`
Media: existing video "Finite vs Infinite APs — Definition and Notation Walkthrough" (old T2 VID1); existing image "General Form of an AP on a Number Line" (old T2 O1.E1)

[textbook_text]
> Some more examples of AP are:
> (a) The heights (in cm) of some students of a school standing in a queue in the morning assembly are 147, 148, 149, . . ., 157.
> (b) The minimum temperatures (in degree celsius) recorded for a week in the month of January in a city, arranged in ascending order are
> – 3.1, – 3.0, – 2.9, – 2.8, – 2.7, – 2.6, – 2.5
> (c) The balance money (in ₹) after paying 5 % of the total loan of ₹ 1000 every month is 950, 900, 850, 800, . . ., 50.
> (d) The cash prizes (in ₹) given by a school to the toppers of Classes I to XII are, respectively, 200, 250, 300, 350, . . ., 750.
> (e) The total savings (in ₹) after every month for 10 months when ₹ 50 are saved each month are 50, 100, 150, 200, 250, 300, 350, 400, 450, 500.
>
> It is left as an exercise for you to explain why each of the lists above is an AP.
>
> You can see that
> a, a + d, a + 2d, a + 3d, . . .
> represents an arithmetic progression where a is the first term and d the common difference. This is called the general form of an AP.
>
> Note that in examples (a) to (e) above, there are only a finite number of terms. Such an AP is called a finite AP. Also note that each of these Arithmetic Progressions (APs) has a last term. The APs in examples (i) to (v) given earlier are not finite APs and so they are called infinite Arithmetic Progressions. Such APs do not have a last term.

*(Cleanup: "in this section" became "given earlier". No words dropped.)*

### C5 · From a and d to the list, and back again
`kind: teach` · `objectives: O2, O3`
Media: new image spec "Building an AP from a and d" — A two-way picture. On the left, three boxes read a = 6, d = 3 and a = 6, d = -3, each with arrows leading to the lists 6, 9, 12, 15 and 6, 3, 0, -3 drawn as rows of tiles with a +3 or -3 arrow between neighbours. On the right, the list 6, 9, 12, 15 is shown with the gaps 9 - 6, 12 - 9 and 15 - 12 marked beside the tiles to show how the first term and the common difference are read back from a list.

[textbook_text]
> Now, to know about an AP, what is the minimum information that you need? Is it enough to know the first term? Or, is it enough to know only the common difference? You will find that you will need to know both – the first term a and the common difference d.
>
> For instance if the first term a is 6 and the common difference d is 3, then the AP is
> 6, 9, 12, 15, . . .
> and if a is 6 and d is – 3, then the AP is
> 6, 3, 0, –3, . . .
>
> Similarly, when
> a = – 7, d = – 2, the AP is – 7, – 9, – 11, – 13, . . .
> a = 1.0, d = 0.1, the AP is 1.0, 1.1, 1.2, 1.3, . . .
> a = 0, d = 1½, the AP is 0, 1½, 3, 4½, 6, . . .
> a = 2, d = 0, the AP is 2, 2, 2, 2, . . .
>
> So, if you know what a and d are, you can list the AP. What about the other way round? That is, if you are given a list of numbers can you say that it is an AP and then find a and d? Since a is the first term, it can easily be written. We know that in an AP, every succeeding term is obtained by adding d to the preceding term. So, d found by subtracting any term from its succeeding term, i.e., the term which immediately follows it should be same for an AP.
>
> For example, for the list of numbers: 6, 9, 12, 15, . . . ,
> We have a₂ – a₁ = 9 – 6 = 3,
> a₃ – a₂ = 12 – 9 = 3,
> a₄ – a₃ = 15 – 12 = 3
> Here the difference of any two consecutive terms in each case is 3. So, the given list is an AP whose first term a is 6 and common difference d is 3.
>
> For the list of numbers: 6, 3, 0, – 3, . . .,
> a₂ – a₁ = 3 – 6 = – 3
> a₃ – a₂ = 0 – 3 = – 3
> a₄ – a₃ = –3 – 0 = –3
> Similarly this is also an AP whose first term is 6 and the common difference is –3.
>
> In general, for an AP a₁, a₂, . . ., aₙ, we have
> d = aₖ₊₁ – aₖ
> where aₖ₊₁ and aₖ are the (k + 1)th and the kth terms respectively.
>
> To obtain d in a given AP, we need not find all of a₂ – a₁, a₃ – a₂, a₄ – a₃, . . . . It is enough to find only one of them.
>
> Consider the list of numbers 1, 1, 2, 3, 5, . . . . By looking at it, you can tell that the difference between any two consecutive terms is not the same. So, this is not an AP.
>
> Note that to find d in the AP: 6, 3, 0, – 3, . . ., we have subtracted 6 from 3 and not 3 from 6, i.e., we should subtract the kth term from the (k + 1) th term even if the (k + 1) th term is smaller. Let us make the concept more clear through some examples.

### C6 · More to explore: why each of these lists is an AP
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Real Lists That Grow by Equal Steps" — A set of five small scenes. A row of students standing in a queue with heights 147, 148, 149 cm; a thermometer strip with readings -3.1, -3.0, -2.9; a loan balance bar shrinking step by step through 950, 900, 850; a row of prize envelopes marked 200, 250, 300; and a money jar with savings 50, 100, 150. Each scene has a small step arrow between neighbouring values.

[enrichment] `[authored answers]`
> **Q.** The heights 147, 148, 149, . . ., 157 form an AP. Why?
> **A.** Each height is 1 cm more than the one before it, so the common difference is d = 1.
>
> **Q.** Why do the temperatures – 3.1, – 3.0, – 2.9, . . ., – 2.5 form an AP?
> **A.** Each temperature is 0.1 degree more than the one before it, so d = 0.1.
>
> **Q.** Why does the loan balance 950, 900, 850, . . ., 50 form an AP?
> **A.** Each month the same ₹ 50 (5 % of ₹ 1000) is paid, so each balance is ₹ 50 less than the one before it, and d = – 50.
>
> **Q.** Why do the cash prizes 200, 250, 300, . . ., 750 and the savings 50, 100, 150, . . ., 500 form APs?
> **A.** In both lists each term is ₹ 50 more than the one before it, so d = 50 in each.

---

## T3 · Examples: Is It an AP?

### C7 · The first term and the common difference of a given AP
`kind: exercise (worked example)` · `objectives: O4`
Media: new image spec "Reading an AP Written with Fractions" — A number line with four evenly spaced marked points at 3/2, 1/2, -1/2 and -3/2, drawn as tiles in a row with dots after the last one to show the list continues. Two curved arrows between neighbouring points are left blank with a question mark for the size of each step, and the first tile is tagged only as the starting point.

[question]
> For the AP : 3/2, 1/2, – 1/2, – 3/2 , . . ., write the first term a and the common difference d.

[worked solution, from source]
> Here, a = 3/2, d = 1/2 – 3/2 = – 1.
> Remember that we can find d using any two consecutive terms, once we know that the numbers are in AP.

### C8 · Which of these lists are APs?
`kind: exercise (worked example)` · `objectives: O4`
Media: existing video "Classifying Sequences — Worked Walkthrough of Examples 1 and 2" (old T3 VID1); existing image "Step Layout — Consecutive Difference Calculations for AP Classification" (old T3 O1.E1)

[question]
> Which of the following list of numbers form an AP? If they form an AP, write the next two terms:
> (i) 4, 10, 16, 22, . . .  (ii) 1, – 1, – 3, – 5, . . .
> (iii) – 2, 2, – 2, 2, – 2, . . .  (iv) 1, 1, 1, 2, 2, 2, 3, 3, 3, . . .

[worked solution, from source]
> (i) We have a₂ – a₁ = 10 – 4 = 6
> a₃ – a₂ = 16 – 10 = 6
> a₄ – a₃ = 22 – 16 = 6
> i.e., aₖ₊₁ – aₖ is the same every time.
> So, the given list of numbers forms an AP with the common difference d = 6.
> The next two terms are: 22 + 6 = 28 and 28 + 6 = 34.
>
> (ii) a₂ – a₁ = – 1 – 1 = – 2
> a₃ – a₂ = – 3 – ( –1 ) = – 3 + 1 = – 2
> a₄ – a₃ = – 5 – ( –3 ) = – 5 + 3 = – 2
> i.e., aₖ₊₁ – aₖ is the same every time.
> So, the given list of numbers forms an AP with the common difference d = – 2.
> The next two terms are: – 5 + (– 2) = – 7 and – 7 + (– 2) = – 9
>
> (iii) a₂ – a₁ = 2 – (– 2) = 2 + 2 = 4
> a₃ – a₂ = – 2 – 2 = – 4
> As a₂ – a₁ ≠ a₃ – a₂, the given list of numbers does not form an AP.
>
> (iv) a₂ – a₁ = 1 – 1 = 0
> a₃ – a₂ = 1 – 1 = 0
> a₄ – a₃ = 2 – 1 = 1
> Here, a₂ – a₁ = a₃ – a₂ ≠ a₄ – a₃.
> So, the given list of numbers does not form an AP.

*(Review: the old video is titled for both examples. It sits on the second, the longer walkthrough. The title is cleaned at build.)*

---

## T4 · Questions: Is It an AP?

Objectives for this set: O5 (apply) classify real-world and numerical lists as APs and write terms when a and d are given; O4 (evaluate) check whether the difference between consecutive terms stays the same.

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, statement only, no working and no answer. There is no video. Hint, solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for all 28.
The questions are in textbook order. Every sub-part of all four questions is an independent task, so each is its own concept.

### C9 · Is It an AP?, Q1 (i)
`objectives: O5` · Media: new image spec (statement only)
> In which of the following situations, does the list of numbers involved make an arithmetic progression, and why?
> (i) The taxi fare after each km when the fare is ₹ 15 for the first km and ₹ 8 for each additional km.

### C10 · Is It an AP?, Q1 (ii)
`objectives: O5` · Media: new image spec (statement only)
> In which of the following situations, does the list of numbers involved make an arithmetic progression, and why?
> (ii) The amount of air present in a cylinder when a vacuum pump removes 1/4 of the air remaining in the cylinder at a time.

### C11 · Is It an AP?, Q1 (iii)
`objectives: O5` · Media: new image spec (statement only)
> In which of the following situations, does the list of numbers involved make an arithmetic progression, and why?
> (iii) The cost of digging a well after every metre of digging, when it costs ₹ 150 for the first metre and rises by ₹ 50 for each subsequent metre.

### C12 · Is It an AP?, Q1 (iv)
`objectives: O5` · Media: new image spec (statement only)
> In which of the following situations, does the list of numbers involved make an arithmetic progression, and why?
> (iv) The amount of money in the account every year, when ₹ 10000 is deposited at compound interest at 8 % per annum.

### C13 · Is It an AP?, Q2 (i)
`objectives: O5` · Media: new image spec (statement only)
> Write first four terms of the AP, when the first term a and the common difference d are given as follows:
> (i) a = 10, d = 10

### C14 · Is It an AP?, Q2 (ii)
`objectives: O5` · Media: new image spec (statement only)
> Write first four terms of the AP, when the first term a and the common difference d are given as follows:
> (ii) a = –2, d = 0

### C15 · Is It an AP?, Q2 (iii)
`objectives: O5` · Media: new image spec (statement only)
> Write first four terms of the AP, when the first term a and the common difference d are given as follows:
> (iii) a = 4, d = – 3

### C16 · Is It an AP?, Q2 (iv)
`objectives: O5` · Media: new image spec (statement only)
> Write first four terms of the AP, when the first term a and the common difference d are given as follows:
> (iv) a = – 1, d = 1/2

### C17 · Is It an AP?, Q2 (v)
`objectives: O5` · Media: new image spec (statement only)
> Write first four terms of the AP, when the first term a and the common difference d are given as follows:
> (v) a = – 1.25, d = – 0.25

### C18 · Is It an AP?, Q3 (i)
`objectives: O5` · Media: new image spec (statement only)
> For the following APs, write the first term and the common difference:
> (i) 3, 1, – 1, – 3, . . .

### C19 · Is It an AP?, Q3 (ii)
`objectives: O5` · Media: new image spec (statement only)
> For the following APs, write the first term and the common difference:
> (ii) – 5, – 1, 3, 7, . . .

### C20 · Is It an AP?, Q3 (iii)
`objectives: O5` · Media: new image spec (statement only)
> For the following APs, write the first term and the common difference:
> (iii) 1/3, 5/3, 9/3, 13/3, . . .

### C21 · Is It an AP?, Q3 (iv)
`objectives: O5` · Media: new image spec (statement only)
> For the following APs, write the first term and the common difference:
> (iv) 0.6, 1.7, 2.8, 3.9, . . .

### C22 · Is It an AP?, Q4 (i)
`objectives: O5, O4` · Media: new image spec (statement only)
> Which of the following are APs ? If they form an AP, find the common difference d and write three more terms.
> (i) 2, 4, 8, 16, . . .

### C23 · Is It an AP?, Q4 (ii)
`objectives: O5, O4` · Media: new image spec (statement only)
> Which of the following are APs ? If they form an AP, find the common difference d and write three more terms.
> (ii) 2, 5/2, 3, 7/2, . . .

### C24 · Is It an AP?, Q4 (iii)
`objectives: O5, O4` · Media: new image spec (statement only)
> Which of the following are APs ? If they form an AP, find the common difference d and write three more terms.
> (iii) – 1.2, – 3.2, – 5.2, – 7.2, . . .

### C25 · Is It an AP?, Q4 (iv)
`objectives: O5, O4` · Media: new image spec (statement only)
> Which of the following are APs ? If they form an AP, find the common difference d and write three more terms.
> (iv) – 10, – 6, – 2, 2, . . .

### C26 · Is It an AP?, Q4 (v)
`objectives: O5, O4` · Media: new image spec (statement only)
> Which of the following are APs ? If they form an AP, find the common difference d and write three more terms.
> (v) 3, 3 + √2, 3 + 2√2, 3 + 3√2, . . .

### C27 · Is It an AP?, Q4 (vi)
`objectives: O5, O4` · Media: new image spec (statement only)
> Which of the following are APs ? If they form an AP, find the common difference d and write three more terms.
> (vi) 0.2, 0.22, 0.222, 0.2222, . . .

### C28 · Is It an AP?, Q4 (vii)
`objectives: O5, O4` · Media: new image spec (statement only)
> Which of the following are APs ? If they form an AP, find the common difference d and write three more terms.
> (vii) 0, – 4, – 8, –12, . . .

### C29 · Is It an AP?, Q4 (viii)
`objectives: O5, O4` · Media: new image spec (statement only)
> Which of the following are APs ? If they form an AP, find the common difference d and write three more terms.
> (viii) – 1/2, – 1/2, – 1/2, – 1/2, . . .

### C30 · Is It an AP?, Q4 (ix)
`objectives: O5, O4` · Media: new image spec (statement only)
> Which of the following are APs ? If they form an AP, find the common difference d and write three more terms.
> (ix) 1, 3, 9, 27, . . .

### C31 · Is It an AP?, Q4 (x)
`objectives: O5, O4` · Media: new image spec (statement only)
> Which of the following are APs ? If they form an AP, find the common difference d and write three more terms.
> (x) a, 2a, 3a, 4a, . . .

### C32 · Is It an AP?, Q4 (xi)
`objectives: O5, O4` · Media: new image spec (statement only)
> Which of the following are APs ? If they form an AP, find the common difference d and write three more terms.
> (xi) a, a², a³, a⁴, . . .

### C33 · Is It an AP?, Q4 (xii)
`objectives: O5, O4` · Media: new image spec (statement only)
> Which of the following are APs ? If they form an AP, find the common difference d and write three more terms.
> (xii) √2, √8, √18, √32, . . .

### C34 · Is It an AP?, Q4 (xiii)
`objectives: O5, O4` · Media: new image spec (statement only)
> Which of the following are APs ? If they form an AP, find the common difference d and write three more terms.
> (xiii) √3, √6, √9, √12, . . .

### C35 · Is It an AP?, Q4 (xiv)
`objectives: O5, O4` · Media: new image spec (statement only)
> Which of the following are APs ? If they form an AP, find the common difference d and write three more terms.
> (xiv) 1², 3², 5², 7², . . .

### C36 · Is It an AP?, Q4 (xv)
`objectives: O5, O4` · Media: new image spec (statement only)
> Which of the following are APs ? If they form an AP, find the common difference d and write three more terms.
> (xv) 1², 5², 7², 73, . . .

*(Review: (xv) is printed in the book as "1², 5², 7², 73"; it is kept exactly as printed.)*

---

# M2 · The nth term

## T5 · The nth Term of an AP

### C37 · The nth term: try it first
`kind: try` · `objectives: O6`
Media: new image spec "Reena's Salary Year by Year" — A job offer letter on the left saying starting monthly salary 8000 rupees with an annual increment of 500 rupees. On the right, a row of small bars for year 1, year 2 and year 3 labelled 8000, 8500 and 9000 with +500 steps between them, then dots, and finally two empty bars labelled year 5 and year 25 with a question mark above each.
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[textbook_text]
> Let us consider the situation again, given earlier, in which Reena applied for a job and got selected. She has been offered the job with a starting monthly salary of ₹ 8000, with an annual increment of ₹ 500. What would be her monthly salary for the fifth year?

[theorem_statement] *(authored from the chapter summary)*
> In an AP with first term a and common difference d, the nth term (or the general term) is given by aₙ = a + (n – 1) d.

[predict] `[authored]`
> Reena's salary starts at ₹ 8000 and goes up by ₹ 500 every year. Without listing every year, guess her monthly salary in the 25th year. Is it nearer ₹ 20000 or nearer ₹ 20500? Commit to an answer. The next concept shows how many times the ₹ 500 is really added.

### C38 · Why the nth term formula works
`kind: prove` · `objectives: O6, O7`
Media: existing video "Deriving the nth Term Formula — From Salary Pattern to aₙ = a + (n−1)d" (old T5 VID1); existing image "Deriving aₙ — Step Layout for nth Term Formula" (old T5 O1.E1)

[textbook_text]
> To answer this, let us first see what her monthly salary for the second year would be.
> It would be ₹ (8000 + 500) = ₹ 8500. In the same way, we can find the monthly salary for the 3rd, 4th and 5th year by adding ₹ 500 to the salary of the previous year.
>
> So, the salary for the 3rd year = ₹ (8500 + 500)
> = ₹ (8000 + 500 + 500)
> = ₹ (8000 + 2 × 500)
> = ₹ [8000 + (3 – 1) × 500]  (for the 3rd year)
> = ₹ 9000
>
> Salary for the 4th year = ₹ (9000 + 500)
> = ₹ (8000 + 500 + 500 + 500)
> = ₹ (8000 + 3 × 500)
> = ₹ [8000 + (4 – 1) × 500]  (for the 4th year)
> = ₹ 9500
>
> Salary for the 5th year = ₹ (9500 + 500)
> = ₹ (8000+500+500+500 + 500)
> = ₹ (8000 + 4 × 500)
> = ₹ [8000 + (5 – 1) × 500]  (for the 5th year)
> = ₹ 10000
>
> Observe that we are getting a list of numbers
> 8000, 8500, 9000, 9500, 10000, . . .
> These numbers are in AP. (Why?)
>
> Now, looking at the pattern formed above, can you find her monthly salary for the 6th year? The 15th year? And, assuming that she will still be working in the job, what about the monthly salary for the 25th year? You would calculate this by adding ₹ 500 each time to the salary of the previous year to give the answer. Can we make this process shorter? Let us see. You may have already got some idea from the way we have obtained the salaries above.
>
> Salary for the 15th year
> = Salary for the 14th year + ₹ 500
> = ₹ [8000 + 14 × 500]
> = ₹ [8000 + (15 – 1) × 500] = ₹ 15000
> i.e., First salary + (15 – 1) × Annual increment.
>
> In the same way, her monthly salary for the 25th year would be
> ₹ [8000 + (25 – 1) × 500] = ₹ 20000
> = First salary + (25 – 1) × Annual increment
>
> This example would have given you some idea about how to write the 15th term, or the 25th term, and more generally, the nth term of the AP.
>
> Let a₁, a₂, a₃, . . . be an AP whose first term a₁ is a and the common difference is d.
> Then,
> the second term a₂ = a + d = a + (2 – 1) d
> the third term a₃ = a₂ + d = (a + d) + d = a + 2d = a + (3 – 1) d
> the fourth term a₄ = a₃ + d = (a + 2d) + d = a + 3d = a + (4 – 1) d
> . . . . . . . .
> Looking at the pattern, we can say that the nth term aₙ = a + (n – 1) d.
>
> So, the nth term aₙ of the AP with first term a and common difference d is given by aₙ = a + (n – 1) d.
>
> aₙ is also called the general term of the AP. If there are m terms in the AP, then aₘ represents the last term which is sometimes also denoted by l.
>
> Let us consider some examples.

### C39 · More to explore: why the salaries are in AP
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Salaries That Rise by the Same Amount" — Five bars side by side for years 1 to 5 with heights labelled 8000, 8500, 9000, 9500 and 10000 rupees. Between each pair of neighbouring bars a bracket marks the same step of 500, and a dashed line at the top of each bar shows the equal rise from year to year.

[enrichment] `[authored answer]`
> **Q.** Why are the salaries 8000, 8500, 9000, 9500, 10000, . . . in AP?
> **A.** Each year's salary is the previous year's salary plus the same ₹ 500. So the difference between any two consecutive terms is always 500, and d = 500.

---

## T6 · Examples: Using the nth Term

### C40 · Finding a given term of an AP
`kind: exercise (worked example)` · `objectives: O8`
Media: existing video "Applying aₙ = a + (n−1)d — Worked Examples 3 to 6" (old T6 VID1). The fit is loose: its description does not match the book's examples, so please check it in review.

[question]
> Find the 10th term of the AP : 2, 7, 12, . . .

[worked solution, from source]
> Here, a = 2, d = 7 – 2 = 5 and n = 10.
> We have aₙ = a + (n – 1) d
> So, a₁₀ = 2 + (10 – 1) × 5 = 2 + 45 = 47
> Therefore, the 10th term of the given AP is 47.

### C41 · Which term is a given number?
`kind: exercise (worked example)` · `objectives: O8`
Media: new image spec "Hunting for a Number in an AP" — A long row of tiles starting 21, 18, 15 with dots continuing to the right, and a step arrow of -3 between neighbours. Below the row, a horizontal line of positions 1, 2, 3 and so on has two target tags, one reading -81 and one reading 0, each joined by a dotted line to an empty position box marked with a question mark.

[question]
> Which term of the AP : 21, 18, 15, . . . is – 81? Also, is any term 0? Give reason for your answer.

[worked solution, from source]
> Here, a = 21, d = 18 – 21 = – 3 and aₙ = – 81, and we have to find n.
> As aₙ = a + ( n – 1) d,
> we have – 81 = 21 + (n – 1)(– 3)
> – 81 = 24 – 3n
> – 105 = – 3n
> So, n = 35
> Therefore, the 35th term of the given AP is – 81.
>
> Next, we want to know if there is any n for which aₙ = 0. If such an n is there, then
> 21 + (n – 1) (–3) = 0,
> i.e., 3(n – 1) = 21
> i.e., n = 8
> So, the eighth term is 0.

### C42 · Finding the AP from two of its terms
`kind: exercise (worked example)` · `objectives: O8`
Media: new image spec "Finding an AP from Two Terms" — A row of seven empty term boxes numbered 1 to 7 from left to right. Only box 3 is filled with the value 5 and only box 7 with the value 9. A curved bracket spans the gap from box 3 to box 7, and the other boxes carry a question mark.

[question]
> Determine the AP whose 3rd term is 5 and the 7th term is 9.

[worked solution, from source]
> We have
> a₃ = a + (3 – 1) d = a + 2d = 5   (1)
> and a₇ = a + (7 – 1) d = a + 6d = 9   (2)
> Solving the pair of linear equations (1) and (2), we get
> a = 3, d = 1
> Hence, the required AP is 3, 4, 5, 6, 7, . . .

### C43 · Is a given number a term of the list?
`kind: exercise (worked example)` · `objectives: O8, O11`
Media: existing image "Example 6 Solution Layout — Membership Check with Integer Test" (old T6 O1.E1)

[question]
> Check whether 301 is a term of the list of numbers 5, 11, 17, 23, . . .

[worked solution, from source]
> We have:
> a₂ – a₁ = 11 – 5 = 6,   a₃ – a₂ = 17 – 11 = 6,   a₄ – a₃ = 23 – 17 = 6
> As aₖ₊₁ – aₖ is the same for k = 1, 2, 3, etc., the given list of numbers is an AP.
> Now, a = 5 and d = 6.
> Let 301 be a term, say, the nth term of this AP.
> We know that
> aₙ = a + (n – 1) d
> So, 301 = 5 + (n – 1) × 6
> i.e., 301 = 6n – 1
> So, n = 302/6 = 151/3
> But n should be a positive integer (Why?). So, 301 is not a term of the given list of numbers.

### C44 · Counting the two-digit numbers divisible by 3
`kind: exercise (worked example)` · `objectives: O9`
Media: existing video "Counting Terms in APs — Worked Walkthrough of Examples 7 and 8" (old T7 VID1)

[question]
> How many two-digit numbers are divisible by 3?

[worked solution, from source]
> The list of two-digit numbers divisible by 3 is:
> 12, 15, 18, . . . , 99
> Is this an AP? Yes it is. Here, a = 12, d = 3, aₙ = 99.
> As aₙ = a + (n – 1) d,
> we have 99 = 12 + (n – 1) × 3
> i.e., 87 = (n – 1) × 3
> i.e., n – 1 = 87/3 = 29
> i.e., n = 29 + 1 = 30
> So, there are 30 two-digit numbers divisible by 3.

### C45 · Counting back from the last term
`kind: exercise (worked example)` · `objectives: O9`
Media: existing image "Reverse-Position Diagram — AP 10 to −62 with Position Mapping" (old T7 O1.E1)

[question]
> Find the 11th term from the last term (towards the first term) of the AP : 10, 7, 4, . . ., – 62.

[worked solution, from source]
> Here, a = 10, d = 7 – 10 = – 3, l = – 62,
> where l = a + (n – 1) d
> To find the 11th term from the last term, we will find the total number of terms in the AP.
> So, – 62 = 10 + (n – 1)(–3)
> i.e., – 72 = (n – 1)(–3)
> i.e., n – 1 = 24
> or n = 25
> So, there are 25 terms in the given AP.
> The 11th term from the last term will be the 15th term. (Note that it will not be the 14th term. Why?)
> So, a₁₅ = 10 + (15 – 1)(–3) = 10 – 42 = – 32
> i.e., the 11th term from the last term is – 32.
>
> **Alternative Solution.** If we write the given AP in the reverse order, then a = – 62 and d = 3 (Why?)
> So, the question now becomes finding the 11th term with these a and d.
> So, a₁₁ = – 62 + (11 – 1) × 3 = – 62 + 30 = – 32
> So, the 11th term, which is now the required term, is – 32.

---

## T7 · Examples: The nth Term in Real Situations

### C46 · Simple interest year by year
`kind: exercise (worked example)` · `objectives: O10`
Media: existing video "AP in Real Contexts — Worked Walkthrough of Examples 9 and 10" (old T8 VID1; the fit is loose, as its flower-bed numbers differ from the book's, so please check it in review); existing image "Simple Interest Sequence — Bar Chart Showing the AP Structure" (old T8 O1.E1)

[question]
> A sum of ₹ 1000 is invested at 8% simple interest per year. Calculate the interest at the end of each year. Do these interests form an AP? If so, find the interest at the end of 30 years making use of this fact.

[worked solution, from source]
> We know that the formula to calculate simple interest is given by
> Simple Interest = P×R×T/100
> So, the interest at the end of the 1st year = ₹ (1000 × 8 × 1)/100 = ₹ 80
> The interest at the end of the 2nd year = ₹ (1000 × 8 × 2)/100 = ₹ 160
> The interest at the end of the 3rd year = ₹ (1000 × 8 × 3)/100 = ₹ 240
> Similarly, we can obtain the interest at the end of the 4th year, 5th year, and so on.
> So, the interest (in ₹) at the end of the 1st, 2nd, 3rd, . . . years, respectively are
> 80, 160, 240, . . .
> It is an AP as the difference between the consecutive terms in the list is 80, i.e., d = 80. Also, a = 80.
> So, to find the interest at the end of 30 years, we shall find a₃₀.
> Now, a₃₀ = a + (30 – 1) d = 80 + 29 × 80 = 2400
> So, the interest at the end of 30 years will be ₹ 2400.

### C47 · How many rows in the flower bed?
`kind: exercise (worked example)` · `objectives: O10, O11`
Media: new image spec "Rose Plants in the Flower Bed" — A top view of a flower bed drawn as rows of round rose-plant dots. Row 1 has 23 dots, row 2 has 21 dots and row 3 has 19 dots, each row two dots shorter than the one above, centred so the bed narrows downwards. After a gap marked with dots, the last row has 5 dots. A brace on the left of the bed carries a question mark for the number of rows.

[question]
> In a flower bed, there are 23 rose plants in the first row, 21 in the second, 19 in the third, and so on. There are 5 rose plants in the last row. How many rows are there in the flower bed?

[worked solution, from source]
> The number of rose plants in the 1st, 2nd, 3rd, . . ., rows are:
> 23, 21, 19, . . ., 5
> It forms an AP (Why?). Let the number of rows in the flower bed be n.
> Then a = 23, d = 21 – 23 = – 2, aₙ = 5
> As, aₙ = a + (n – 1) d
> We have, 5 = 23 + (n – 1)(– 2)
> i.e., – 18 = (n – 1)(– 2)
> i.e., n = 10
> So, there are 10 rows in the flower bed.

### C48 · More to explore: the "Why?" prompts in these examples
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Four Small Puzzles About Positions" — Four panels. Panel 1 shows a row of whole-number positions 1, 2, 3, 4, 5 on a line, with a point between two positions crossed out to show a position cannot be a fraction. Panel 2 shows 25 boxes in a row numbered from the left and from the right, with the 11th box from the right end highlighted. Panel 3 shows the list 10, 7, 4 with a step of -3 and the same list written backwards with a step of +3. Panel 4 shows rows of rose plants 23, 21, 19 with a step of -2.

[enrichment] `[authored answers]`
> **Q.** When checking whether 301 is a term of 5, 11, 17, 23, . . ., why must n be a positive integer?
> **A.** n is the position of a term in the list: 1st, 2nd, 3rd, and so on. A position cannot be a fraction or a negative number, so n = 151/3 means 301 is not in the list.
>
> **Q.** In the AP 10, 7, 4, . . ., – 62 with 25 terms, why is the 11th term from the last the 15th term and not the 14th?
> **A.** The last term is the 25th, which is the 1st from the last. Counting back, the kth term from the last is the (25 – k + 1)th term, so the 11th from the last is the (25 – 11 + 1)th = 15th term. The 14th term would be the 12th from the last.
>
> **Q.** Why does the reversed AP – 62, – 59, . . ., 10 have d = 3?
> **A.** Going forwards each term is 3 less than the one before it. Read backwards, each term is 3 more than the one before it, so the common difference changes sign and becomes 3.
>
> **Q.** Why do the rose plants 23, 21, 19, . . ., 5 form an AP?
> **A.** Each row has 2 plants fewer than the row before it, so the difference between consecutive terms is always – 2.

---

## T8 · Questions: The nth Term

Objectives for this set: O12 (apply) fill tables of a, d, n and aₙ, find missing terms, and find a term from partial information; O11 (evaluate) decide whether a value is a term by checking that n is a positive integer.

Same rules as the first set: `attempt_first`, one new hint-free image spec each, no video, and steps and answer *to author* for all 30. The questions are in textbook order. The table rows of the first question, the two choices of the second, the five box sequences of the third and the two lists of the fifth are independent tasks, so each is its own concept.

### C49 · The nth Term, Q1 (i)
`objectives: O12` · Media: new image spec (statement only)
> Fill in the blanks in the following table, given that a is the first term, d the common difference and aₙ the nth term of the AP:
> (i) a = 7, d = 3, n = 8, aₙ = . . .

### C50 · The nth Term, Q1 (ii)
`objectives: O12` · Media: new image spec (statement only)
> Fill in the blanks in the following table, given that a is the first term, d the common difference and aₙ the nth term of the AP:
> (ii) a = – 18, d = . . ., n = 10, aₙ = 0

### C51 · The nth Term, Q1 (iii)
`objectives: O12` · Media: new image spec (statement only)
> Fill in the blanks in the following table, given that a is the first term, d the common difference and aₙ the nth term of the AP:
> (iii) a = . . ., d = – 3, n = 18, aₙ = – 5

### C52 · The nth Term, Q1 (iv)
`objectives: O12` · Media: new image spec (statement only)
> Fill in the blanks in the following table, given that a is the first term, d the common difference and aₙ the nth term of the AP:
> (iv) a = – 18.9, d = 2.5, n = . . ., aₙ = 3.6

### C53 · The nth Term, Q1 (v)
`objectives: O12` · Media: new image spec (statement only)
> Fill in the blanks in the following table, given that a is the first term, d the common difference and aₙ the nth term of the AP:
> (v) a = 3.5, d = 0, n = 105, aₙ = . . .

### C54 · The nth Term, Q2 (i)
`objectives: O12` · Media: new image spec (statement only)
> Choose the correct choice in the following and justify:
> (i) 30th term of the AP: 10, 7, 4, . . . , is
> (A) 97  (B) 77  (C) –77  (D) – 87

### C55 · The nth Term, Q2 (ii)
`objectives: O12` · Media: new image spec (statement only)
> Choose the correct choice in the following and justify:
> (ii) 11th term of the AP: – 3, – 1/2, 2, . . ., is
> (A) 28  (B) 22  (C) –38  (D) – 48½

### C56 · The nth Term, Q3 (i)
`objectives: O12` · Media: new image spec (statement only)
> In the following APs, find the missing terms in the boxes:
> (i) 2, □, 26

### C57 · The nth Term, Q3 (ii)
`objectives: O12` · Media: new image spec (statement only)
> In the following APs, find the missing terms in the boxes:
> (ii) □, 13, □, 3

### C58 · The nth Term, Q3 (iii)
`objectives: O12` · Media: new image spec (statement only)
> In the following APs, find the missing terms in the boxes:
> (iii) 5, □, □, 9½

### C59 · The nth Term, Q3 (iv)
`objectives: O12` · Media: new image spec (statement only)
> In the following APs, find the missing terms in the boxes:
> (iv) – 4, □, □, □, □, 6

### C60 · The nth Term, Q3 (v)
`objectives: O12` · Media: new image spec (statement only)
> In the following APs, find the missing terms in the boxes:
> (v) □, 38, □, □, □, – 22

### C61 · The nth Term, Q4
`objectives: O12` · Media: new image spec (statement only)
> Which term of the AP : 3, 8, 13, 18, . . . ,is 78?

### C62 · The nth Term, Q5 (i)
`objectives: O12` · Media: new image spec (statement only)
> Find the number of terms in each of the following APs:
> (i) 7, 13, 19, . . . , 205

### C63 · The nth Term, Q5 (ii)
`objectives: O12` · Media: new image spec (statement only)
> Find the number of terms in each of the following APs:
> (ii) 18, 15½, 13, . . . , – 47

### C64 · The nth Term, Q6
`objectives: O12, O11` · Media: new image spec (statement only)
> Check whether – 150 is a term of the AP : 11, 8, 5, 2 . . .

### C65 · The nth Term, Q7
`objectives: O12` · Media: new image spec (statement only)
> Find the 31st term of an AP whose 11th term is 38 and the 16th term is 73.

### C66 · The nth Term, Q8
`objectives: O12` · Media: new image spec (statement only)
> An AP consists of 50 terms of which 3rd term is 12 and the last term is 106. Find the 29th term.

### C67 · The nth Term, Q9
`objectives: O12` · Media: new image spec (statement only)
> If the 3rd and the 9th terms of an AP are 4 and – 8 respectively, which term of this AP is zero?

### C68 · The nth Term, Q10
`objectives: O12` · Media: new image spec (statement only)
> The 17th term of an AP exceeds its 10th term by 7. Find the common difference.

### C69 · The nth Term, Q11
`objectives: O12` · Media: new image spec (statement only)
> Which term of the AP : 3, 15, 27, 39, . . . will be 132 more than its 54th term?

### C70 · The nth Term, Q12
`objectives: O12` · Media: new image spec (statement only)
> Two APs have the same common difference. The difference between their 100th terms is 100, what is the difference between their 1000th terms?

### C71 · The nth Term, Q13
`objectives: O12` · Media: new image spec (statement only)
> How many three-digit numbers are divisible by 7?

### C72 · The nth Term, Q14
`objectives: O12` · Media: new image spec (statement only)
> How many multiples of 4 lie between 10 and 250?

### C73 · The nth Term, Q15
`objectives: O12` · Media: new image spec (statement only)
> For what value of n, are the nth terms of two APs: 63, 65, 67, . . . and 3, 10, 17, . . . equal?

### C74 · The nth Term, Q16
`objectives: O12` · Media: new image spec (statement only)
> Determine the AP whose third term is 16 and the 7th term exceeds the 5th term by 12.

### C75 · The nth Term, Q17
`objectives: O12` · Media: new image spec (statement only)
> Find the 20th term from the last term of the AP : 3, 8, 13, . . ., 253.

### C76 · The nth Term, Q18
`objectives: O12` · Media: new image spec (statement only)
> The sum of the 4th and 8th terms of an AP is 24 and the sum of the 6th and 10th terms is 44. Find the first three terms of the AP.

### C77 · The nth Term, Q19
`objectives: O12` · Media: new image spec (statement only)
> Subba Rao started work in 1995 at an annual salary of ₹ 5000 and received an increment of ₹ 200 each year. In which year did his income reach ₹ 7000?

### C78 · The nth Term, Q20
`objectives: O12` · Media: new image spec (statement only)
> Ramkali saved ₹ 5 in the first week of a year and then increased her weekly savings by ₹ 1.75. If in the nth week, her weekly savings become ₹ 20.75, find n.

---

# M3 · The sum of the first n terms

## T9 · The Sum of the First n Terms

### C79 · The sum formula: try it first
`kind: try` · `objectives: O13`
Media: new image spec "Saving in Shakila's Money Box" — A piggy bank money box on the left with a baby girl and a birthday cake. A row of coin stacks for the 1st, 2nd, 3rd and 4th birthdays labelled 100, 150, 200 and 250 rupees, followed by dots and the 21st birthday stack drawn as a question mark. A banner above reads: how much money is in the box by the 21st birthday.
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[textbook_text]
> Let us consider the situation again, given earlier, in which Shakila put ₹ 100 into her daughter's money box when she was one year old, ₹ 150 on her second birthday, ₹ 200 on her third birthday and will continue in the same way. How much money will be collected in the money box by the time her daughter is 21 years old?
>
> Here, the amount of money (in ₹) put in the money box on her first, second, third, fourth . . . birthday were respectively 100, 150, 200, 250, . . . till her 21st birthday. To find the total amount in the money box on her 21st birthday, we will have to write each of the 21 numbers in the list above and then add them up. Don't you think it would be a tedious and time consuming process? Can we make the process shorter? This would be possible if we can find a method for getting this sum. Let us see.

[theorem_statement] *(authored from the chapter summary)*
> The sum of the first n terms of an AP is given by S = n/2 [2a + (n – 1)d].
> If l is the last term of the finite AP, say the nth term, then the sum of all terms of the AP is given by S = n/2 (a + l).

[predict] `[authored]`
> Think about adding 1 + 2 + 3 + . . . + 100. Without adding term by term, guess the total. Is it nearer 5000 or nearer 10000? Commit to an answer. Then look at what happens when you pair the first number with the last.

### C80 · Why the sum formula works
`kind: prove` · `objectives: O13, O14`
Media: existing video "Gauss and the Sum of 1 to 100 — The Pairing Trick That Built a Formula" (old T10 VID1); existing image "Adding S Forward and Backward — The Symmetric Pairing Step Layout" (old T10 O1.E1)

[textbook_text]
> We consider the problem given to Gauss (about whom you read earlier), to solve when he was just 10 years old. He was asked to find the sum of the positive integers from 1 to 100. He immediately replied that the sum is 5050. Can you guess how did he do? He wrote:
> S = 1 + 2 + 3 + . . . + 99 + 100
> And then, reversed the numbers to write
> S = 100 + 99 + . . . + 3 + 2 + 1
> Adding these two, he got
> 2S = (100 + 1) + (99 + 2) + . . . + (3 + 98) + (2 + 99) + (1 + 100)
> = 101 + 101 + . . . + 101 + 101  (100 times)
> So, S = (100 × 101)/2 = 5050, i.e., the sum = 5050.
>
> We will now use the same technique to find the sum of the first n terms of an AP:
> a, a + d, a + 2d, . . .
> The nth term of this AP is a + (n – 1) d. Let S denote the sum of the first n terms of the AP. We have
> S = a + (a + d) + (a + 2d) + . . . + [a + (n – 1) d]   (1)
> Rewriting the terms in reverse order, we have
> S = [a + (n – 1) d] + [a + (n – 2) d] + . . . + (a + d) + a   (2)
> On adding (1) and (2), term-wise. we get
> 2S = [2a + (n – 1)d] + [2a + (n – 1)d] + ... + [2a + (n – 1)d] + [2a + (n – 1)d]  (n times)
> or, 2S = n [2a + (n – 1) d]  (Since, there are n terms)
> or, S = n/2 [2a + (n – 1) d]
>
> So, the sum of the first n terms of an AP is given by
> S = n/2 [2a + (n – 1) d]
>
> We can also write this as S = n/2 [a + a + (n – 1) d]
> i.e., S = n/2 (a + aₙ)   (3)
>
> Now, if there are only n terms in an AP, then aₙ = l, the last term.
> From (3), we see that
> S = n/2 (a + l)   (4)
> This form of the result is useful when the first and the last terms of an AP are given and the common difference is not given.

*(Cleanup: "about whom you read in Chapter 1" became "about whom you read earlier". No words dropped.)*

### C81 · Back to the money box, and the nth term from the sums
`kind: teach` · `objectives: O14`
Media: new image spec "Money Box Total and Each Year's Deposit" — Two panels. Left panel: the money box with the values a = 100, d = 50 and n = 21 written beside it, and the sum formula S = n/2 [2a + (n - 1)d] filled in as 21/2 [2 x 100 + 20 x 50]. Right panel: a long bar for the sum of the first n terms split into a shorter bar for the sum of the first (n - 1) terms and a small end piece labelled as the nth term.

[textbook_text]
> Now we return to the question that was posed to us in the beginning. The amount of money (in Rs) in the money box of Shakila's daughter on 1st, 2nd, 3rd, 4th birthday, . . ., were 100, 150, 200, 250, . . ., respectively.
> This is an AP. We have to find the total money collected on her 21st birthday, i.e., the sum of the first 21 terms of this AP.
> Here, a = 100, d = 50 and n = 21. Using the formula:
> S = n/2 [2a + (n-1) d],
> we have S = 21/2 [2 × 100 + (21 – 1) × 50]
> = 21/2 [200 + 1000]
> = 21/2 × 1200 = 12600
> So, the amount of money collected on her 21st birthday is ₹ 12600.
> Hasn't the use of the formula made it much easier to solve the problem?
>
> We also use Sₙ in place of S to denote the sum of first n terms of the AP. We write S₂₀ to denote the sum of the first 20 terms of an AP. The formula for the sum of the first n terms involves four quantities S, a, d and n. If we know any three of them, we can find the fourth.

[remark, from source]
> The nth term of an AP is the difference of the sum to first n terms and the sum to first (n – 1) terms of it, i.e., aₙ = Sₙ – Sₙ₋₁.

---

## T10 · Examples: Using the Sum Formula

### C82 · Summing a given number of terms
`kind: exercise (worked example)` · `objectives: O15`
Media: existing video "Applying the Sum Formula — Worked Walkthrough of Examples 11, 12, and 13" (old T11 VID1). The fit is loose: its description does not match the book's numbers, so please check it in review.

[question]
> Find the sum of the first 22 terms of the AP : 8, 3, –2, . . .

[worked solution, from source]
> Here, a = 8, d = 3 – 8 = –5, n = 22.
> We know that
> S = n/2 [2a + (n-1) d]
> Therefore, S = 22/2 [16 + 21(–5)] = 11(16 – 105) = 11(–89) = – 979
> So, the sum of the first 22 terms of the AP is – 979.

### C83 · From a known sum to a later term
`kind: exercise (worked example)` · `objectives: O15`
Media: new image spec "From a Known Sum to a Later Term" — A row of twenty small term boxes. Box 1 is filled with 10, and a bracket over boxes 1 to 14 carries the label sum of first 14 terms = 1050. Boxes 15 to 19 are shaded plain, and box 20 is marked with a question mark. The common difference is shown as an unknown d between neighbouring boxes.

[question]
> If the sum of the first 14 terms of an AP is 1050 and its first term is 10, find the 20th term.

[worked solution, from source]
> Here, S₁₄ = 1050, n = 14, a = 10.
> As Sₙ = n/2 [2a + (n-1)d],
> so, 1050 = 14/2 [20 + 13d] = 140 + 91d
> i.e., 910 = 91d
> or, d = 10
> Therefore, a₂₀ = 10 + (20 – 1) × 10 = 200, i.e. 20th term is 200.

### C84 · How many terms give a given sum?
`kind: exercise (worked example)` · `objectives: O16`
Media: new image spec "How Many Terms Add Up to 78?" — A row of term tiles 24, 21, 18 with step arrows of -3, followed by dots and empty tiles. A long bracket under the tiles is labelled sum = 78 and ends with a question mark for the number of tiles included. A small counter with a question mark stands beside the bracket.

[question]
> How many terms of the AP : 24, 21, 18, . . . must be taken so that their sum is 78?

[worked solution, from source]
> Here, a = 24, d = 21 – 24 = –3, Sₙ = 78. We need to find n.
> We know that Sₙ = n/2 [2a + (n-1) d]
> So, 78 = n/2 [48 + (n-1)(–3)] = n/2 [51 – 3n]
> or 3n² – 51n + 156 = 0
> or n² – 17n + 52 = 0
> or (n – 4)(n – 13) = 0
> or n = 4 or 13
> Both values of n are admissible. So, the number of terms is either 4 or 13.

[remark, from source]
> 1. In this case, the sum of the first 4 terms = the sum of the first 13 terms = 78.
> 2. Two answers are possible because the sum of the terms from 5th to 13th will be zero. This is because a is positive and d is negative, so that some terms will be positive and some others negative, and will cancel out each other.

### C85 · The sum of the first n positive integers
`kind: exercise (worked example)` · `objectives: O17`
Media: existing image "Sum of Natural Numbers — From S₁₀₀₀ to Sₙ = n(n+1)/2" (old T12 O1.E1)

[question]
> Find the sum of:
> (i) the first 1000 positive integers  (ii) the first n positive integers

[worked solution, from source]
> (i) Let S = 1 + 2 + 3 + . . . + 1000
> Using the formula Sₙ = n/2 (a + l) for the sum of the first n terms of an AP, we have
> S₁₀₀₀ = 1000/2 (1 + 1000) = 500 × 1001 = 500500
> So, the sum of the first 1000 positive integers is 500500.
>
> (ii) Let Sₙ = 1 + 2 + 3 + . . . + n
> Here a = 1 and the last term l is n.
> Therefore, Sₙ = n/2 (1 + n) or Sₙ = n(n + 1)/2
> So, the sum of first n positive integers is given by
> Sₙ = n(n + 1)/2

*(Review: kept as one concept. Part (ii) is the same steps as part (i) with 1000 replaced by n, so the two parts build on each other.)*

### C86 · Summing a list given by its nth term
`kind: exercise (worked example)` · `objectives: O17`
Media: existing video "Sum Formulas in Context — Worked Walkthrough of Examples 14 and 15" (old T12 VID1)

[question]
> Find the sum of first 24 terms of the list of numbers whose nth term is given by
> aₙ = 3 + 2n

[worked solution, from source]
> As aₙ = 3 + 2n,
> so, a₁ = 3 + 2 = 5
> a₂ = 3 + 2 × 2 = 7
> a₃ = 3 + 2 × 3 = 9
> List of numbers becomes 5, 7, 9, 11, . . .
> Here, 7 – 5 = 9 – 7 = 11 – 9 = 2 and so on.
> So, it forms an AP with common difference d = 2.
> To find S₂₄, we have n = 24, a = 5, d = 2.
> Therefore, S₂₄ = 24/2 [2 × 5 + (24 – 1) × 2] = 12 [10 + 46] = 672
> So, sum of first 24 terms of the list of numbers is 672.

### C87 · TV sets made year by year
`kind: exercise (worked example)` · `objectives: O18, O19`
Media: existing video "Simultaneous Equations from AP Conditions — Worked Walkthrough of Example 16" (old T13 VID1); existing image "TV Production AP — Multi-Year Output Chart with AP Parameters" (old T13 O1.E1)

[question]
> A manufacturer of TV sets produced 600 sets in the third year and 700 sets in the seventh year. Assuming that the production increases uniformly by a fixed number every year, find:
> (i) the production in the 1st year  (ii) the production in the 10th year
> (iii) the total production in first 7 years

[worked solution, from source]
> (i) Since the production increases uniformly by a fixed number every year, the number of TV sets manufactured in 1st, 2nd, 3rd, . . ., years will form an AP.
> Let us denote the number of TV sets manufactured in the nth year by aₙ.
> Then, a₃ = 600 and a₇ = 700
> or, a + 2d = 600
> and a + 6d = 700
> Solving these equations, we get d = 25 and a = 550.
> Therefore, production of TV sets in the first year is 550.
>
> (ii) Now a₁₀ = a + 9d = 550 + 9 × 25 = 775
> So, production of TV sets in the 10th year is 775.
>
> (iii) Also, S₇ = 7/2 [2 × 550 + (7 – 1) × 25]
> = 7/2 [1100 + 150] = 4375
> Thus, the total production of TV sets in first 7 years is 4375.

*(Review: kept as one concept. Parts (ii) and (iii) both use the a and d found in part (i).)*

---

## T11 · Questions: The Sum of n Terms

Objectives for this set: O20 (apply) use both forms of the sum formula, and find the unknown among a, d, n and Sₙ when the others are given; O21 (evaluate) use aₙ = Sₙ – Sₙ₋₁ to find terms when the sum is given as an expression in n.

Same rules as the earlier sets: `attempt_first`, one new hint-free image spec each, no video, and steps and answer *to author* for all 35. The questions are in textbook order. The sub-parts of the first, second, third and tenth questions are independent tasks, so each is its own concept. The tenth question's closing line ("Also find the sum of the first 15 terms in each case") is carried into both of its parts.
The eleventh question stays one concept: each step (S₁, then S₂, then the second term, then later terms) uses the one before it.
Three questions come with a figure in the book (the spiral, the logs and the potato race). Their image spec is the book's own figure only. Two questions carry a book hint, which opens only after the attempt.

### C88 · The Sum of n Terms, Q1 (i)
`objectives: O20` · Media: new image spec (statement only)
> Find the sum of the following APs:
> (i) 2, 7, 12, . . ., to 10 terms.

### C89 · The Sum of n Terms, Q1 (ii)
`objectives: O20` · Media: new image spec (statement only)
> Find the sum of the following APs:
> (ii) –37, –33, –29, . . ., to 12 terms.

### C90 · The Sum of n Terms, Q1 (iii)
`objectives: O20` · Media: new image spec (statement only)
> Find the sum of the following APs:
> (iii) 0.6, 1.7, 2.8, . . ., to 100 terms.

### C91 · The Sum of n Terms, Q1 (iv)
`objectives: O20` · Media: new image spec (statement only)
> Find the sum of the following APs:
> (iv) 1/15, 1/12, 1/10, . . ., to 11 terms.

### C92 · The Sum of n Terms, Q2 (i)
`objectives: O20` · Media: new image spec (statement only)
> Find the sums given below:
> (i) 7 + 10½ + 14 + . . . + 84

### C93 · The Sum of n Terms, Q2 (ii)
`objectives: O20` · Media: new image spec (statement only)
> Find the sums given below:
> (ii) 34 + 32 + 30 + . . . + 10

### C94 · The Sum of n Terms, Q2 (iii)
`objectives: O20` · Media: new image spec (statement only)
> Find the sums given below:
> (iii) –5 + (–8) + (–11) + . . . + (–230)

### C95 · The Sum of n Terms, Q3 (i)
`objectives: O20` · Media: new image spec (statement only)
> In an AP:
> (i) given a = 5, d = 3, aₙ = 50, find n and Sₙ.

### C96 · The Sum of n Terms, Q3 (ii)
`objectives: O20` · Media: new image spec (statement only)
> In an AP:
> (ii) given a = 7, a₁₃ = 35, find d and S₁₃.

### C97 · The Sum of n Terms, Q3 (iii)
`objectives: O20` · Media: new image spec (statement only)
> In an AP:
> (iii) given a₁₂ = 37, d = 3, find a and S₁₂.

### C98 · The Sum of n Terms, Q3 (iv)
`objectives: O20` · Media: new image spec (statement only)
> In an AP:
> (iv) given a₃ = 15, S₁₀ = 125, find d and a₁₀.

### C99 · The Sum of n Terms, Q3 (v)
`objectives: O20` · Media: new image spec (statement only)
> In an AP:
> (v) given d = 5, S₉ = 75, find a and a₉.

### C100 · The Sum of n Terms, Q3 (vi)
`objectives: O20` · Media: new image spec (statement only)
> In an AP:
> (vi) given a = 2, d = 8, Sₙ = 90, find n and aₙ.

### C101 · The Sum of n Terms, Q3 (vii)
`objectives: O20` · Media: new image spec (statement only)
> In an AP:
> (vii) given a = 8, aₙ = 62, Sₙ = 210, find n and d.

### C102 · The Sum of n Terms, Q3 (viii)
`objectives: O20` · Media: new image spec (statement only)
> In an AP:
> (viii) given aₙ = 4, d = 2, Sₙ = –14, find n and a.

### C103 · The Sum of n Terms, Q3 (ix)
`objectives: O20` · Media: new image spec (statement only)
> In an AP:
> (ix) given a = 3, n = 8, S = 192, find d.

### C104 · The Sum of n Terms, Q3 (x)
`objectives: O20` · Media: new image spec (statement only)
> In an AP:
> (x) given l = 28, S = 144, and there are total 9 terms. Find a.

### C105 · The Sum of n Terms, Q4
`objectives: O20` · Media: new image spec (statement only)
> How many terms of the AP : 9, 17, 25, . . . must be taken to give a sum of 636?

### C106 · The Sum of n Terms, Q5
`objectives: O20` · Media: new image spec (statement only)
> The first term of an AP is 5, the last term is 45 and the sum is 400. Find the number of terms and the common difference.

### C107 · The Sum of n Terms, Q6
`objectives: O20` · Media: new image spec (statement only)
> The first and the last terms of an AP are 17 and 350 respectively. If the common difference is 9, how many terms are there and what is their sum?

### C108 · The Sum of n Terms, Q7
`objectives: O20` · Media: new image spec (statement only)
> Find the sum of first 22 terms of an AP in which d = 7 and 22nd term is 149.

### C109 · The Sum of n Terms, Q8
`objectives: O20` · Media: new image spec (statement only)
> Find the sum of first 51 terms of an AP whose second and third terms are 14 and 18 respectively.

### C110 · The Sum of n Terms, Q9
`objectives: O20` · Media: new image spec (statement only)
> If the sum of first 7 terms of an AP is 49 and that of 17 terms is 289, find the sum of first n terms.

### C111 · The Sum of n Terms, Q10 (i)
`objectives: O20` · Media: new image spec (statement only)
> Show that a₁, a₂, . . ., aₙ, . . . form an AP where aₙ is defined as below:
> (i) aₙ = 3 + 4n
> Also find the sum of the first 15 terms.

### C112 · The Sum of n Terms, Q10 (ii)
`objectives: O20` · Media: new image spec (statement only)
> Show that a₁, a₂, . . ., aₙ, . . . form an AP where aₙ is defined as below:
> (ii) aₙ = 9 – 5n
> Also find the sum of the first 15 terms.

### C113 · The Sum of n Terms, Q11
`objectives: O21` · Media: new image spec (statement only)
> If the sum of the first n terms of an AP is 4n – n², what is the first term (that is S₁)? What is the sum of first two terms? What is the second term? Similarly, find the 3rd, the 10th and the nth terms.

### C114 · The Sum of n Terms, Q12
`objectives: O20` · Media: new image spec (statement only)
> Find the sum of the first 40 positive integers divisible by 6.

### C115 · The Sum of n Terms, Q13
`objectives: O20` · Media: new image spec (statement only)
> Find the sum of the first 15 multiples of 8.

### C116 · The Sum of n Terms, Q14
`objectives: O20` · Media: new image spec (statement only)
> Find the sum of the odd numbers between 0 and 50.

### C117 · The Sum of n Terms, Q15
`objectives: O20` · Media: new image spec (statement only)
> A contract on construction job specifies a penalty for delay of completion beyond a certain date as follows: ₹ 200 for the first day, ₹ 250 for the second day, ₹ 300 for the third day, etc., the penalty for each succeeding day being ₹ 50 more than for the preceding day. How much money the contractor has to pay as penalty, if he has delayed the work by 30 days?

### C118 · The Sum of n Terms, Q16
`objectives: O20` · Media: new image spec (statement only)
> A sum of ₹ 700 is to be used to give seven cash prizes to students of a school for their overall academic performance. If each prize is ₹ 20 less than its preceding prize, find the value of each of the prizes.

### C119 · The Sum of n Terms, Q17
`objectives: O20` · Media: new image spec (statement only)
> In a school, students thought of planting trees in and around the school to reduce air pollution. It was decided that the number of trees, that each section of each class will plant, will be the same as the class, in which they are studying, e.g., a section of Class I will plant 1 tree, a section of Class II will plant 2 trees and so on till Class XII. There are three sections of each class. How many trees will be planted by the students?

### C120 · The Sum of n Terms, Q18
`objectives: O20` · Media: new image spec (**the book's own figure only**, as it supplies the spiral of semicircles)
> A spiral is made up of successive semicircles, with centres alternately at A and B, starting with centre at A, of radii 0.5 cm, 1.0 cm, 1.5 cm, 2.0 cm, . . . as shown in the figure. What is the total length of such a spiral made up of thirteen consecutive semicircles? (Take π = 22/7)
> **Hint (shown only after the attempt):** Length of successive semicircles is l₁, l₂, l₃, l₄, . . . with centres at A, B, A, B, . . ., respectively.

### C121 · The Sum of n Terms, Q19
`objectives: O20` · Media: new image spec (**the book's own figure only**, as it supplies the stack of logs)
> 200 logs are stacked in the following manner: 20 logs in the bottom row, 19 in the next row, 18 in the row next to it and so on, as shown in the figure. In how many rows are the 200 logs placed and how many logs are in the top row?

### C122 · The Sum of n Terms, Q20
`objectives: O20` · Media: new image spec (**the book's own figure only**, as it supplies the bucket and potato positions)
> In a potato race, a bucket is placed at the starting point, which is 5 m from the first potato, and the other potatoes are placed 3 m apart in a straight line. There are ten potatoes in the line, as shown in the figure.
> A competitor starts from the bucket, picks up the nearest potato, runs back with it, drops it in the bucket, runs back to pick up the next potato, runs to the bucket to drop it in, and she continues in the same way until all the potatoes are in the bucket. What is the total distance the competitor has to run?
> **Hint (shown only after the attempt):** To pick up the first potato and the second potato, the total distance (in metres) run by a competitor is 2 × 5 + 2 × (5 + 3)

---

## T12 · Questions: Challenge Problems

Objectives for this set: O22 (apply) use aₙ = a + (n – 1)d and the sum formula in multi-step, non-routine problems such as ladder rungs, house numbers and a terrace of steps.

The book marks this set optional ("not from the examination point of view"); that note stays in review prose and metadata only. Same rules as the earlier sets: `attempt_first`, one new hint-free image spec each, no video, and steps and answer *to author* for all 5. The questions are in textbook order and none has sub-parts. Two questions come with a figure in the book (the ladder and the terrace). Four carry a book hint, which opens only after the attempt.

### C123 · Challenge Problems, Q1
`objectives: O22` · Media: new image spec (statement only)
> Which term of the AP : 121, 117, 113, . . ., is its first negative term?
> **Hint (shown only after the attempt):** Find n for aₙ < 0

### C124 · Challenge Problems, Q2
`objectives: O22` · Media: new image spec (statement only)
> The sum of the third and the seventh terms of an AP is 6 and their product is 8. Find the sum of first sixteen terms of the AP.

### C125 · Challenge Problems, Q3
`objectives: O22` · Media: new image spec (**the book's own figure only**, as it supplies the ladder)
> A ladder has rungs 25 cm apart, as shown in the figure. The rungs decrease uniformly in length from 45 cm at the bottom to 25 cm at the top. If the top and the bottom rungs are 2½ m apart, what is the length of the wood required for the rungs?
> **Hint (shown only after the attempt):** Number of rungs = 250/25 + 1

### C126 · Challenge Problems, Q4
`objectives: O22` · Media: new image spec (statement only)
> The houses of a row are numbered consecutively from 1 to 49. Show that there is a value of x such that the sum of the numbers of the houses preceding the house numbered x is equal to the sum of the numbers of the houses following it. Find this value of x.
> **Hint (shown only after the attempt):** Sₓ₋₁ = S₄₉ – Sₓ

### C127 · Challenge Problems, Q5
`objectives: O22` · Media: new image spec (**the book's own figure only**, as it supplies the terrace steps)
> A small terrace at a football ground comprises of 15 steps each of which is 50 m long and built of solid concrete. Each step has a rise of 1/4 m and a tread of 1/2 m, as shown in the figure. Calculate the total volume of concrete required to build the terrace.
> **Hint (shown only after the attempt):** Volume of concrete required to build the first step = 1/4 × 1/2 × 50 m³

---

# M4 · Wrap-up

## T13 · Chapter Summary

### C128 · Chapter summary
`kind: summary` · `objectives: O23, O24`
Media: existing video "Chapter Review — Five Key Results and the AP Decision Tree" (old T16 VID1); existing image "Chapter Summary — Five Key Results at a Glance" (old T16 O1.E1). Three images that give away the method are also re-homed here: "AP Decision Reference Card" (old T4 O1.E1), "AP Parameter Reference Table — Four-Variable Relationship" (old T9 O1.E1) and "Sum Formula Decision Chart — When to Use Which Form" (old T14 O2.E1).

[summary_points]
> In this chapter, you have studied the following points:
> 1. An arithmetic progression (AP) is a list of numbers in which each term is obtained by adding a fixed number d to the preceding term, except the first term. The fixed number d is called the common difference. The general form of an AP is a, a + d, a + 2d, a + 3d, . . .
> 2. A given list of numbers a₁, a₂, a₃, . . . is an AP, if the differences a₂ – a₁, a₃ – a₂, a₄ – a₃, . . ., give the same value, i.e., if aₖ₊₁ – aₖ is the same for different values of k.
> 3. In an AP with first term a and common difference d, the nth term (or the general term) is given by aₙ = a + (n – 1) d.
> 4. The sum of the first n terms of an AP is given by: S = n/2 [2a + (n – 1)d]
> 5. If l is the last term of the finite AP, say the nth term, then the sum of all terms of the AP is given by: S = n/2 (a + l)

### C129 · A note on the arithmetic mean
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "The Middle of Three Terms in AP" — A number line with three points labelled a, b and c in order. The distance from a to b and the distance from b to c are drawn as two equal arcs, both marked as the same step, so that b sits exactly halfway between a and c. Under the line the three labels are shown as consecutive terms of an AP.

[textbook_text · "A note to the reader"]
> If a, b, c are in AP, then b = (a + c)/2 and b is called the arithmetic mean of a and c.

---

# Appendix A · Objectives

Format: ID · bloom level · wording · old objective(s) it carries.

| ID | Bloom | Objective | Old ID |
|---|---|---|---|
| O1 | understand | Interpret real-world sequences — salary increments, ladder rungs, savings deposits — as lists where each term increases by a fixed amount. | T1.O1 |
| O2 | analyze | Explain what an arithmetic progression is and define the common difference d as aₖ₊₁ − aₖ. | T2.O1 |
| O3 | understand | Distinguish between finite and infinite APs and represent a general AP in the form a, a + d, a + 2d, a + 3d, … | T2.O2 |
| O4 | evaluate | Verify whether a given list of numbers forms an AP by checking whether the common difference is constant across all consecutive pairs. | T3.O1 |
| O5 | apply | Solve problems that require classifying real-world and numerical sequences as APs and computing terms when a and d are given. | T4.O1 |
| O6 | understand | Explain how repeated addition of d to the first term generates each subsequent term and leads to the general formula aₙ = a + (n − 1)d. | T5.O1 |
| O7 | apply | Compute any specified term of an AP using aₙ = a + (n − 1)d when the first term a and common difference d are known. | T5.O2 |
| O8 | apply | Apply aₙ = a + (n − 1)d to find a specific term, identify the position of a given value in an AP, and determine the AP when two terms are known. | T6.O1 |
| O9 | apply | Solve multi-step nth term problems including counting terms divisible by a given number, finding a term from the last, and using the reverse-order strategy. | T7.O1 |
| O10 | apply | Translate real-world situations involving uniform change — simple interest, flower-bed rows, salary growth — into APs and compute the required term. | T8.O1 |
| O11 | evaluate | Justify whether a target value is a term of a specific AP by verifying that the computed n is a positive integer. | T8.O2 |
| O12 | apply | Solve a range of nth term problems — filling tables of AP parameters, finding missing terms in box sequences, and determining specific terms from partial information. | T9.O1 |
| O13 | understand | Explain Gauss's symmetric-pairing technique and use it to derive the sum formula Sₙ = n/2 [2a + (n − 1)d]. | T10.O1 |
| O14 | apply | Apply both forms of the sum formula — Sₙ = n/2 [2a + (n − 1)d] and Sₙ = n/2 (a + l) — to calculate the sum of a finite AP. | T10.O2 |
| O15 | apply | Calculate the sum of n terms of an AP using the sum formula, and determine the common difference when Sₙ and a are given. | T11.O1 |
| O16 | analyze | Determine n when Sₙ is given, recognising that a quadratic equation in n may yield two valid admissible answers. | T11.O2 |
| O17 | evaluate | Calculate the sum of sequences expressed via an algebraic nth term formula by identifying the underlying AP and applying the sum formula. | T12.O1 |
| O18 | apply | Model a uniformly-increasing real-world sequence as an AP and compute both a specific term and a running total by applying aₙ = a + (n − 1)d and Sₙ = n/2[2a + (n − 1)d]. | T13.O1 |
| O19 | analyze | Determine the first term and common difference of an AP from two non-adjacent terms by setting up and solving a pair of simultaneous linear equations. | T13.O2 |
| O20 | apply | Apply Sₙ = n/2[2a + (n − 1)d] and Sₙ = n/2(a + l) to compute the sum of APs and to determine unknown AP parameters when three of the four quantities {a, d, n, Sₙ} are given. | T14.O1 |
| O21 | evaluate | Verify the identity aₙ = Sₙ − Sₙ₋₁ by deriving individual terms when Sₙ is expressed as an algebraic function of n, and apply it to solve word problems involving cumulative totals. | T14.O2 |
| O22 | apply | Apply aₙ = a + (n − 1)d and Sₙ = n/2[2a + (n − 1)d] to multi-step non-routine problems involving geometric arrangements such as ladder rungs, house numbering symmetry, and terraced concrete volumes. | T15.O1 |
| O23 | remember | Recall the five key results of the chapter — AP definition, common difference test, nth term formula aₙ = a + (n − 1)d, both sum forms, and the arithmetic mean property — and state the condition under which each formula applies. | T16.O1 |
| O24 | evaluate | Select the appropriate sum formula — Sₙ = n/2[2a + (n − 1)d] versus Sₙ = n/2(a + l) — based on which AP parameters are explicitly given in a problem. | T16.O2 |

Notes:
- All 24 old objectives are carried, in the old order, with their wording unchanged. No new objective was needed: the two try concepts anchor on the old derivation objectives (O6 for the nth term, O13 for the sum).
- Every objective anchors on at least one non-enrichment concept. O1 now sits on the daily-life lists (C2), not on the hook, because the hook is enrichment and carries none.
- O11 (is n a positive integer?) anchors on the membership example (C43), the flower-bed example (C47) and the "is – 150 a term?" question (C64).

# Appendix B · Held assets (not attached to the new plan; nothing deleted)

**Ten old tools** (no tools in this chapter):
- T2 "AP Builder (given a and d)" (T2D1)
- T3 "AP Detective (Is This an AP?)" (T2D1)
- T5 "nth Term Formula Walkthrough" (T2D1)
- T8 "Word Problem Translator (AP Applications)" (T2D1)
- T8 "\"First Negative Term\" Detective" (T2D2)
- T9 "Missing Terms Finder" (T2D1)
- T10 "Sum of n Terms with Gauss Pairing" (T2D1)
- T11 "Find n Given Sum (quadratic twist)" (T2D1)
- T13 "Two-Condition AP Solver (system of equations)" (T2D1)
- T15 "Geometric AP Visualizer (spiral, logs, steps, potato race)" (T2D1)

**Four old exercise videos** (no question videos for now):
- T4 "Taxi Fare Analysis — Is Q1(i) an Arithmetic Progression?" (VID1)
- T9 "Exercise 5.2 Strategy Guide — Question-Type Playbook for nth Term Problems" (VID1)
- T14 "Exercise 5.3 Strategy Guide — Navigating Sum and Combined AP Problems" (VID1)
- T15 "Exercise 5.4 — Strategies for AP Application and Mixed Problems" (VID1)

**Two other held images** (each gives away a question's working or answer):
- T11 "Example 13 — Two Valid Roots for n in a Sum Problem" (O2.E1). Its content is the quadratic 4n² + 5n − 636 = 0, which is the working of the "sum of 636" question (C105), not the worked example. Attaching it anywhere before that attempt would reveal the method and answer.
- T15 "Ladder Rung Diagram — Q3 Geometric Setup" (O1.E1). It shows all eleven rung lengths and the total, which is the answer to the ladder question (C125).

Identity check: 42 old media = 26 attached (12 videos, 14 images) + 16 held (10 tools, 4 exercise videos, 2 images).

# Appendix C · Carried-over fields

Every old topic's `recall_questions`, `summary`, `key_terms`, `concept_bullets`, `brief_summary`, `detailed_summary` and `important_points` carry into the new topic that holds its text. They are not shown here, to keep this file reviewable. The nothing-deleted check at build time compares them field by field.

Where each old topic's text and fields land:

| Old topic | New concepts |
|---|---|
| T1 Real-world patterns and introduction | C1, C2 |
| T2 Defining an AP | C3, C4, C5, C6 (the "left as an exercise" answers) |
| T3 Testing whether a list is an AP | C7, C8 |
| T4 First exercise set | C9–C36; its reference card moves to the summary (C128) |
| T5 Deriving the nth term | C37, C38, C39 (the "Why?" answer) |
| T6 Applying the nth term | C40, C41, C42, C43 |
| T7 Counting terms and reversing the AP | C44, C45 |
| T8 Word problems on the nth term | C46, C47, C48 (the "Why?" answers) |
| T9 Second exercise set | C49–C78; its reference table moves to the summary (C128) |
| T10 Gauss and the sum formula | C79 (setup), C80, C81 |
| T11 Applying the sum formula | C82, C83, C84; one image held (Appendix B) |
| T12 Sums of special lists | C85, C86 |
| T13 Word problems on the sum formula | C87 |
| T14 Third exercise set | C88–C122; its decision chart moves to the summary (C128) |
| T15 Optional fourth exercise set | C123–C127; one image held (Appendix B) |
| T16 Chapter review | C128, C129 |
