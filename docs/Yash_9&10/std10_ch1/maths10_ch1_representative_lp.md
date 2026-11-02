# Representative learning plan: Class 10, Real Numbers (maths10_ch1)

A review copy of the restructured plan, down to concept level. Content is shown in full. Media are only named and never embedded.

Source: `learning_plan_std10_chap1_version1.json` and the chapter text in `textbook_class10_ch1_jemh101.pdf`. Shape follows the Class 9 circles plan and the Class 10 coordinate geometry plan.

## Read this first

**Standing decisions**
- No tools in this chapter. The five old `2d_tool` items are held (Appendix B).
- No videos for exercise questions. Each question concept gets one hint-free image spec and no video. The two old exercise-recap videos are held (Appendix B).
- Examples keep the existing videos and images that match them. No new example media is planned.
- No grouping inside the exercises. Each textbook question is its own concept, in book order, named "<set name>, Q<n>". A question with separate lettered sub-parts gets one concept per sub-part, named "<set name>, Q<n> (<roman>)". Its quoted text is the stem plus that one sub-part.
- Method cards and an image that prints a question's answer are not attached to any question concept. They are re-homed to the Chapter Summary (C43).

**What a concept entry shows**
- `kind`: try, prove, teach, enrich, hook, exercise or summary.
- `objectives`: objective IDs. Enrichment concepts have none (only C6 and C7 are enrichment).
- `media`: existing assets re-homed from the old plan, new asset specs, or none.
- `[block_kind]` tags are review labels only. They never reach the student.
- Old media titles are quoted exactly as in the old plan. A title that carries a book number (for example "Example 1", "Theorem 1.2", "Exercise 1.1") is renamed at build.

**Text cleanup applied to everything below**
- "Section 1.x" and "Sections 1.2" become a plain phrase ("in this chapter", "Here").
- "Theorem 1.1", "Theorem 1.2" and "Theorem 1.3" are replaced by the theorem's name or statement.
- "Example n" and "Exercise 1.x" labels are removed.
- The pointer "(This technique is discussed in some detail in Appendix 1.)" is removed.
- The pointer "(see Example 8)" in the closing note is removed. This book has no Example 8. The replacement "see the 6, 72, 120 example" is `[authored]`.
- Fig. numbers do not occur in the extracted text. The figures are carried by the images.
- Book references stay only in metadata (`ncert_refs`), which is not shown here.

**Marked in the text**
- `[authored]` marks text that is not in the old plan or the book. These are predictions, answers to book prompts, new objective wording, and the reworded objectives O31 and O32.
- Question solutions (`steps` and `answer`) are not in the old plan. They are marked *to author* and nothing is invented here.

**Please check**
- The book's introduction promises Euclid's division algorithm and the decimal expansion of p/q. Neither is taught in this chapter. The text is kept as printed in the hook (C1). The hook carries the new objective O31 because its text states the algorithm; the decimal-expansion promise has no objective.
- The two old objectives that were not carried (Euclid's division algorithm, LCM of three numbers) are now O31 (hook C1) and O32 (C44, now a teach concept). Please confirm the reworded text.
- Text is taken from the PDF. The old plan was used only for the maths symbols the PDF garbles (powers, roots).

## Plan at a glance

| Module | Topic | Concepts |
|---|---|---|
| M1 Primes as building blocks | T1 Building Numbers from Primes (hook) | C1 |
| | T2 The Fundamental Theorem of Arithmetic | C2–C7 |
| | T3 Examples: Primes at Work | C8 |
| M2 HCF and LCM from prime factors | T4 HCF and LCM from Prime Factors | C9–C11 |
| | T5 Examples: HCF and LCM | C12–C13 |
| | T6 Questions: Prime Factors at Work | C14–C28 |
| M3 Irrational numbers | T7 What Makes a Number Irrational? | C29 |
| | T8 A Prime Lemma and the Irrationality of √2 | C30–C33 |
| | T9 Rational and Irrational Numbers Together | C34 |
| | T10 Examples: Proving Irrationality | C35–C37 |
| | T11 Questions: Proving Irrationality | C38–C42 |
| M4 Wrap-up | T12 Chapter Summary | C43–C44 |

Totals: 44 concepts and 32 objectives. 20 question concepts need a new image. 0 new videos.

---

# M1 · Primes as building blocks

## T1 · Building Numbers from Primes (hook)

### C1 · Where this chapter goes
`kind: hook` · `objectives: O31`
Media: existing video "Primes as Building Blocks: Chapter Preview" (old T1 VID1); existing image "Chapter Roadmap: Primes, HCF/LCM, and Irrationality" (old T1 O1.E1)

[textbook_text]
> In Class IX, you began your exploration of the world of real numbers and encountered irrational numbers. We continue our discussion on real numbers in this chapter. We begin with very important properties of positive integers, namely the Euclid's division algorithm and the Fundamental Theorem of Arithmetic.
>
> Euclid's division algorithm, as the name suggests, has to do with divisibility of integers. Stated simply, it says any positive integer a can be divided by another positive integer b in such a way that it leaves a remainder r that is smaller than b. Many of you probably recognise this as the usual long division process. Although this result is quite easy to state and understand, it has many applications related to the divisibility properties of integers. We touch upon a few of them, and use it mainly to compute the HCF of two positive integers.
>
> The Fundamental Theorem of Arithmetic, on the other hand, has to do something with multiplication of positive integers. You already know that every composite number can be expressed as a product of primes in a unique way—this important fact is the Fundamental Theorem of Arithmetic. Again, while it is a result that is easy to state and understand, it has some very deep and significant applications in the field of mathematics.
>
> We use the Fundamental Theorem of Arithmetic for two main applications. First, we use it to prove the irrationality of many of the numbers you studied in Class IX, such as √2, √3 and √5. Second, we apply this theorem to explore when exactly the decimal expansion of a rational number, say p/q (q ≠ 0), is terminating and when it is non-terminating repeating. We do so by looking at the prime factorisation of the denominator q of p/q. You will see that the prime factorisation of q will completely reveal the nature of the decimal expansion of p/q.
>
> So let us begin our exploration.

*(Cleanup: "in Sections 1.2," removed. Euclid's division algorithm is stated in this text and carried by O31. It is not taught further, and neither is the decimal-expansion application; flagged for review.)*

---

## T2 · The Fundamental Theorem of Arithmetic

### C2 · Building numbers up from primes
`kind: teach` · `objectives: O1`
Media: new image spec "Multiplying Primes to Build Numbers" — A building-block style picture: five prime blocks labelled 2, 3, 7, 11 and 23 on the left, with arrows showing different groups of them multiplied together into bigger blocks on the right, labelled 7 x 11 x 23 = 1771, 3 x 7 x 11 x 23 = 5313, 2 x 3 x 7 x 11 x 23 = 10626 and 2^3 x 3 x 7^3 = 8232. A faint row of dots at the end suggests that the collection goes on forever.

[textbook_text]
> In your earlier classes, you have seen that any natural number can be written as a product of its prime factors. For instance, 2 = 2, 4 = 2 × 2, 253 = 11 × 23, and so on. Now, let us try and look at natural numbers from the other direction. That is, can any natural number be obtained by multiplying prime numbers? Let us see.
>
> Take any collection of prime numbers, say 2, 3, 7, 11 and 23. If we multiply some or all of these numbers, allowing them to repeat as many times as we wish, we can produce a large collection of positive integers (In fact, infinitely many). Let us list a few :
> 7 × 11 × 23 = 1771
> 3 × 7 × 11 × 23 = 5313
> 2 × 3 × 7 × 11 × 23 = 10626
> 2³ × 3 × 7³ = 8232
> 2² × 3 × 7 × 11 × 23 = 21252
> and so on.
>
> Now, let us suppose your collection of primes includes all the possible primes. What is your guess about the size of this collection? Does it contain only a finite number of integers, or infinitely many? Infact, there are infinitely many primes. So, if we combine all these primes in all possible ways, we will get an infinite collection of numbers, all the primes and all possible products of primes. The question is – can we produce all the composite numbers this way? What do you think? Do you think that there may be a composite number which is not the product of powers of primes? Before we answer this, let us factorise positive integers, that is, do the opposite of what we have done so far.

### C3 · Factor trees: from a number back to its primes
`kind: teach` · `objectives: O1, O2`
Media: existing image "Factor Tree of 32760" (old T2 O2.E1)
No tool, so the old Factor Tree Builder is held (Appendix B).

[textbook_text]
> We are going to use the factor tree with which you are all familiar. Let us take some large number, say, 32760, and factorise it as shown.

[figure note, review only: the factor tree is carried by the image. Its splits are 32760 = 2 × 16380, 16380 = 2 × 8190, 8190 = 2 × 4095, 4095 = 3 × 1365, 1365 = 3 × 455, 455 = 5 × 91, 91 = 7 × 13.]

[textbook_text]
> So we have factorised 32760 as 2 × 2 × 2 × 3 × 3 × 5 × 7 × 13 as a product of primes, i.e., 32760 = 2³ × 3² × 5 × 7 × 13 as a product of powers of primes. Let us try another number, say, 123456789. This can be written as 3² × 3803 × 3607. Of course, you have to check that 3803 and 3607 are primes! (Try it out for several other natural numbers yourself.) This leads us to a conjecture that every composite number can be written as the product of powers of primes. In fact, this statement is true, and is called the Fundamental Theorem of Arithmetic because of its basic crucial importance to the study of integers. Let us now formally state this theorem.

### C4 · The Fundamental Theorem of Arithmetic: try it first
`kind: try` · `objectives: O3`
Media: new image spec "Splitting 12 Down to Primes" — Two separate factor trees for the number 12 drawn side by side with the leaves left blank. The first tree starts with the split 12 into 2 and 6 and the second starts with the split 12 into 3 and 4. Empty circles at the bottom of each tree wait to be filled with primes.
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[theorem_statement]
> The Fundamental Theorem of Arithmetic: Every composite number can be expressed (factorised) as a product of primes, and this factorisation is unique, apart from the order in which the prime factors occur.

[predict] `[authored]`
> Take the number 12. One person splits it as 2 × 2 × 3. Another starts with 12 = 3 × 4 and keeps splitting until only primes are left. Guess before reading on: will the two always end up with the same primes, or could a composite number be built from two different sets of primes? Commit to an answer. The next concept says exactly what is and is not allowed to differ.

### C5 · What "unique" means
`kind: teach` · `objectives: O4`
Media: new image spec "Same Primes in Any Order" — Four number tiles 2, 3, 5 and 7 arranged in two different orders, 2 x 3 x 5 x 7 and 3 x 5 x 7 x 2, with arrows crossing between the tiles to show they are the same set of tiles. Below, the tiles are lined up in ascending order p1, p2, p3, p4 with the prime-power form of 32760 written as 2^3 x 3^2 x 5 x 7 x 13.

[textbook_text]
> The Fundamental Theorem of Arithmetic says that every composite number can be factorised as a product of primes. Actually it says more. It says that given any composite number it can be factorised as a product of prime numbers in a 'unique' way, except for the order in which the primes occur. That is, given any composite number there is one and only one way to write it as a product of primes, as long as we are not particular about the order in which the primes occur. So, for example, we regard 2 × 3 × 5 × 7 as the same as 3 × 5 × 7 × 2, or any other possible order in which these primes are written. This fact is also stated in the following form:
>
> The prime factorisation of a natural number is unique, except for the order of its factors.
>
> In general, given a composite number x, we factorise it as x = p₁p₂ ... pₙ, where p₁, p₂,..., pₙ are primes and written in ascending order, i.e., p₁ ≤ p₂ ≤ . . . ≤ pₙ. If we combine the same primes, we will get powers of primes. For example, 32760 = 2 × 2 × 2 × 3 × 3 × 5 × 7 × 13 = 2³ × 3² × 5 × 7 × 13
>
> Once we have decided that the order will be ascending, then the way the number is factorised, is unique.
>
> The Fundamental Theorem of Arithmetic has many applications, both within mathematics and in other fields. Let us look at some examples.

### C6 · Gauss and the Fundamental Theorem
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: existing video "Carl Friedrich Gauss and the Fundamental Theorem" (old T2 VID1)

[textbook_text · historical note]
> An equivalent version of this theorem was probably first recorded as Proposition 14 of Book IX in Euclid's Elements, before it came to be known as the Fundamental Theorem of Arithmetic. However, the first correct proof was given by Carl Friedrich Gauss in his Disquisitiones Arithmeticae.
>
> Carl Friedrich Gauss (1777 – 1855) is often referred to as the 'Prince of Mathematicians' and is considered one of the three greatest mathematicians of all time, along with Archimedes and Newton. He has made fundamental contributions to both mathematics and science.

*(Cleanup: the book prints "Theorem 1.2" here, which is a slip for this theorem. The words "this theorem" are `[authored]`.)*

### C7 · More to explore: check it yourself
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Checking a Number Is Prime" — A worked-style checking board for 3803 and 3607: a list of small primes (2, 3, 5, 7, 11, 13 and so on) in a row with a square-root marker line near 61 for 3803 and near 59 for 3607, and a tick-or-cross slot beside each prime left empty. At the right, a box shows 3 squared x 3803 x 3607 with a question mark and 123456789 on the other side.

[enrichment] `[authored answer]`
> **Q.** Check that 3803 and 3607 are primes, and that 3² × 3803 × 3607 really is 123456789.
> **A.** To test a number, divide it by every prime up to its square root: the primes up to 61 for 3803, and up to 59 for 3607. None divides exactly, so both are prime. Then 9 × 3803 × 3607 = 123456789.

[enrichment] *(open-ended prompt from the book; no answer to author)*
> **Q.** Try it out for several other natural numbers yourself: factorise them with a factor tree and write them as a product of powers of primes.

---

## T3 · Examples: Primes at Work

### C8 · Can 4ⁿ end with the digit zero?
`kind: exercise (worked example)` · `objectives: O5`
Media: existing video "Walkthrough of Example 1: Can 4ⁿ End in Zero?" (old T3 VID1); existing image "Example 1 Proof Layout: 4ⁿ Never Ends in Zero" (old T3 O1.E1)
No tool, so the old "Does It End in Zero?" detective is held (Appendix B).

[question]
> Consider the numbers 4ⁿ, where n is a natural number. Check whether there is any value of n for which 4ⁿ ends with the digit zero.

[worked solution, from source]
> If the number 4ⁿ, for any n, were to end with the digit zero, then it would be divisible by 5. That is, the prime factorisation of 4ⁿ would contain the prime 5. This is not possible because 4ⁿ = (2)²ⁿ; so the only prime in the factorisation of 4ⁿ is 2. So, the uniqueness of the Fundamental Theorem of Arithmetic guarantees that there are no other primes in the factorisation of 4ⁿ. So, there is no natural number n for which 4ⁿ ends with the digit zero.

---

# M2 · HCF and LCM from prime factors

## T4 · HCF and LCM from Prime Factors

### C9 · HCF: the smallest power of each common prime
`kind: teach` · `objectives: O6, O7`
Media: existing video "HCF Walkthrough: Examples 2 and 3" (old T4 VID1)

[textbook_text]
> You have already learnt how to find the HCF and LCM of two positive integers using the Fundamental Theorem of Arithmetic in earlier classes, without realising it! This method is also called the prime factorisation method. Let us recall this method through an example.
>
> Find the LCM and HCF of 6 and 20 by the prime factorisation method.
>
> We have : 6 = 2¹ × 3¹ and 20 = 2 × 2 × 5 = 2² × 5¹.
>
> You can find HCF(6, 20) = 2 and LCM(6, 20) = 2 × 2 × 3 × 5 = 60, as done in your earlier classes.
>
> Note that HCF(6, 20) = 2¹ = Product of the smallest power of each common prime factor in the numbers.

### C10 · LCM: the greatest power of each prime involved
`kind: teach` · `objectives: O8, O9`
Media: existing video "LCM Walkthrough: Jogger Meeting Time" (old T5 VID1); existing image "LCM(6, 20) Prime-Power Layout" (old T5 O2.E1). The video's fit is loose, please check: it is tied to a jogger story that is not in the book.

[textbook_text]
> LCM (6, 20) = 2² × 3¹ × 5¹ = Product of the greatest power of each prime factor, involved in the numbers.

### C11 · HCF times LCM: try it first
`kind: try` · `objectives: O10`
Media: existing video "Why HCF × LCM = a × b: Derivation" (old T6 VID1). The fit is loose, please check: the video explains why the identity holds, and the book gives no proof, so it may belong after the prediction.
No tool, so the old verifier is held (Appendix B). This concept has the statement and a prediction only.

[textbook_text]
> From the example above, you might have noticed that HCF(6, 20) × LCM(6, 20) = 6 × 20. In fact, we can verify that for any two positive integers a and b, HCF (a, b) × LCM (a, b) = a × b. We can use this result to find the LCM of two positive integers, if we have already found the HCF of the two positive integers.

[theorem_statement] *(taken from the text above)*
> For any two positive integers a and b, HCF(a, b) × LCM(a, b) = a × b.

[predict] `[authored]`
> Take 8 and 12. Before you work out their HCF and LCM, guess: will HCF × LCM come out equal to 8 × 12 = 96, smaller than 96, or larger than 96? Commit to an answer, then check it once you have found both.

---

## T5 · Examples: HCF and LCM

### C12 · HCF first, then the LCM, for 96 and 404
`kind: exercise (worked example)` · `objectives: O11`
Media: existing images "Prime Factorisation Trees for 96 and 404" (old T4 O2.E1) and "Example 3: HCF × LCM = 96 × 404 Step Layout" (old T6 O2.E1)

[question]
> Find the HCF of 96 and 404 by the prime factorisation method. Hence, find their LCM.

[worked solution, from source]
> The prime factorisation of 96 and 404 gives :
> 96 = 2⁵ × 3, 404 = 2² × 101
> Therefore, the HCF of these two integers is 2² = 4.
> Also,
> LCM (96, 404) = (96 × 404) / HCF(96, 404) = (96 × 404) / 4 = 9696

### C13 · HCF and LCM of three numbers
`kind: exercise (worked example)` · `objectives: O12, O13`
Media: existing video "Three-Number Walkthrough: Why the Product Rule Fails" (old T7 VID1); existing images "Example 4: HCF and LCM of 6, 72, 120 — Summary Layout" (old T7 O2.E1) and "Delhi Bus Depot: LCM(15, 20, 25) Scenario" (old T7 O1.E1). The bus-depot image's fit is loose, please check: its scenario is not in the book.

[question]
> Find the HCF and LCM of 6, 72 and 120, using the prime factorisation method.

[worked solution, from source]
> We have :
> 6 = 2 × 3, 72 = 2³ × 3², 120 = 2³ × 3 × 5
> Here, 2¹ and 3¹ are the smallest powers of the common factors 2 and 3, respectively.
> So,
> HCF (6, 72, 120) = 2¹ × 3¹ = 2 × 3 = 6
> 2³, 3² and 5¹ are the greatest powers of the prime factors 2, 3 and 5 respectively involved in the three numbers.
> So,
> LCM (6, 72, 120) = 2³ × 3² × 5¹ = 360

[remark, from source]
> Notice, 6 × 72 × 120 ≠ HCF (6, 72, 120) × LCM (6, 72, 120). So, the product of three numbers is not equal to the product of their HCF and LCM.

---

## T6 · Questions: Prime Factors at Work

This is the first exercise of the chapter. Q1, Q2 and Q3 have separate lettered sub-parts, so each sub-part is its own concept. Q4 to Q7 have no sub-parts.

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, statement only, no working and no answer. There is no video. Hint, solution and any later media open after the student has attempted the question. The book prints no hint and no figure for these questions.
Steps and answer are *to author* for all 15.

Objectives for this set: **O16** (apply) for Q1 to Q4, **O17** (evaluate) for Q5 and Q6, and **O14** (apply) with **O15** (analyze) for Q7.

### C14 · Prime Factors at Work, Q1 (i)
`objectives: O16` · Media: new image spec (statement only)
> Express each number as a product of its prime factors:
> (i) 140

### C15 · Prime Factors at Work, Q1 (ii)
`objectives: O16` · Media: new image spec (statement only)
> Express each number as a product of its prime factors:
> (ii) 156

### C16 · Prime Factors at Work, Q1 (iii)
`objectives: O16` · Media: new image spec (statement only)
> Express each number as a product of its prime factors:
> (iii) 3825

### C17 · Prime Factors at Work, Q1 (iv)
`objectives: O16` · Media: new image spec (statement only)
> Express each number as a product of its prime factors:
> (iv) 5005

### C18 · Prime Factors at Work, Q1 (v)
`objectives: O16` · Media: new image spec (statement only)
> Express each number as a product of its prime factors:
> (v) 7429

### C19 · Prime Factors at Work, Q2 (i)
`objectives: O16` · Media: new image spec (statement only)
> Find the LCM and HCF of the following pairs of integers and verify that LCM × HCF = product of the two numbers.
> (i) 26 and 91

### C20 · Prime Factors at Work, Q2 (ii)
`objectives: O16` · Media: new image spec (statement only)
> Find the LCM and HCF of the following pairs of integers and verify that LCM × HCF = product of the two numbers.
> (ii) 510 and 92

### C21 · Prime Factors at Work, Q2 (iii)
`objectives: O16` · Media: new image spec (statement only)
> Find the LCM and HCF of the following pairs of integers and verify that LCM × HCF = product of the two numbers.
> (iii) 336 and 54

### C22 · Prime Factors at Work, Q3 (i)
`objectives: O16` · Media: new image spec (statement only)
> Find the LCM and HCF of the following integers by applying the prime factorisation method.
> (i) 12, 15 and 21

### C23 · Prime Factors at Work, Q3 (ii)
`objectives: O16` · Media: new image spec (statement only)
> Find the LCM and HCF of the following integers by applying the prime factorisation method.
> (ii) 17, 23 and 29

### C24 · Prime Factors at Work, Q3 (iii)
`objectives: O16` · Media: new image spec (statement only)
> Find the LCM and HCF of the following integers by applying the prime factorisation method.
> (iii) 8, 9 and 25

### C25 · Prime Factors at Work, Q4
`objectives: O16` · Media: new image spec (statement only)
> Given that HCF (306, 657) = 9, find LCM (306, 657).

### C26 · Prime Factors at Work, Q5
`objectives: O17` · Media: new image spec (statement only)
> Check whether 6ⁿ can end with the digit 0 for any natural number n.

### C27 · Prime Factors at Work, Q6
`objectives: O17` · Media: new image spec (statement only)
> Explain why 7 × 11 × 13 + 13 and 7 × 6 × 5 × 4 × 3 × 2 × 1 + 5 are composite numbers.

### C28 · Prime Factors at Work, Q7
`objectives: O14, O15` · Media: new image spec (statement only)
> There is a circular path around a sports field. Sonia takes 18 minutes to drive one round of the field, while Ravi takes 12 minutes for the same. Suppose they both start at the same point and at the same time, and go in the same direction. After how many minutes will they meet again at the starting point?

---

# M3 · Irrational numbers

## T7 · What Makes a Number Irrational?

### C29 · Irrational numbers: the p/q test
`kind: teach` · `objectives: O18, O19`
Media: existing video "What Makes a Number Irrational" (old T10 VID1); existing image "Irrational Number Examples List" (old T10 O2.E1)
No tool, so the old Rational vs Irrational Sorter is held (Appendix B).

[textbook_text]
> In Class IX, you were introduced to irrational numbers and many of their properties. You studied about their existence and how the rationals and the irrationals together made up the real numbers. You even studied how to locate irrationals on the number line. However, we did not prove that they were irrationals. Here, we will prove that √2, √3, √5 and, in general, √p is irrational, where p is a prime. One of the theorems, we use in our proof, is the Fundamental Theorem of Arithmetic.
>
> Recall, a number 's' is called irrational if it cannot be written in the form p/q, where p and q are integers and q ≠ 0. Some examples of irrational numbers, with which you are already familiar, are :
> √2, √3, √15, π, −√2/√3, 0.10110111011110 …, etc.

*(Cleanup: "In this section, we" became "Here, we", and the heading's section number is dropped. The example list is rendered from the old plan, because the PDF garbles it.)*

---

## T8 · A Prime Lemma and the Irrationality of √2

### C30 · If a prime divides a², it divides a: try it first
`kind: try` · `objectives: O20`
Media: new image spec "Primes Dividing a Perfect Square" — A small table showing the square 36 = 6 x 6 with the numbers a = 6 and a squared = 36 in two boxes, and two prime tiles p = 2 and p = 3 beside it. Each tile has an empty box labelled 'divides a squared?' and another labelled 'divides a?' to be filled in.

[textbook_text]
> Before we prove that √2 is irrational, we need the following theorem, whose proof is based on the Fundamental Theorem of Arithmetic.

[theorem_statement]
> Let p be a prime number. If p divides a², then p divides a, where a is a positive integer.

[predict] `[authored]`
> Guess before reading the proof: if a prime divides a perfect square a², must it also divide a itself? Try a² = 36 with p = 2 and then with p = 3 in your head, and then commit to a guess for every prime and every a.

### C31 · Why a prime that divides a² divides a
`kind: prove` · `objectives: O21`
Media: existing video "Theorem 1.2 Proof Walkthrough" (old T11 VID1); existing image "Theorem 1.2 Proof Layout" (old T11 O1.E1)

[textbook_text · proof]
> Let the prime factorisation of a be as follows :
> a = p₁p₂ . . . pₙ, where p₁, p₂, . . ., pₙ are primes, not necessarily distinct.
>
> Therefore, a² = (p₁p₂ . . . pₙ)(p₁p₂ . . . pₙ) = p₁²p₂² . . . pₙ².
>
> Now, we are given that p divides a². Therefore, from the Fundamental Theorem of Arithmetic, it follows that p is one of the prime factors of a². However, using the uniqueness part of the Fundamental Theorem of Arithmetic, we realise that the only prime factors of a² are p₁, p₂, . . ., pₙ. So p is one of p₁, p₂, . . ., pₙ.
>
> Now, since a = p₁p₂ . . . pₙ, p divides a.

[remark, from source]
> Not from the examination point of view.

### C32 · √2 is irrational: try it first
`kind: try` · `objectives: O22`
Media: new image spec "Writing Root 2 as a Fraction" — A number line with the point marked root 2 between 1 and 2, and beside it a fraction bar a over b with the label 'a and b have no common factor' under it. The equation b times root 2 = a is written under the fraction, with a blank speech bubble above asking which prime might divide both.

[textbook_text]
> We are now ready to give a proof that √2 is irrational. The proof is based on a technique called 'proof by contradiction'.

[theorem_statement]
> √2 is irrational.

[predict] `[authored]`
> Suppose, just for a moment, that √2 could be written as a fraction a/b with no common factor in a and b. Guess which prime will turn out to divide both a and b. Commit to an answer. The next concept shows where the idea goes wrong.

### C33 · Why √2 is irrational
`kind: prove` · `objectives: O23`
Media: existing video "Proof by Contradiction: √2 is Irrational" (old T12 VID1); existing image "√2 Irrationality Proof Layout (Theorem 1.3)" (old T12 O1.E1)

[textbook_text · proof]
> Let us assume, to the contrary, that √2 is rational.
>
> So, we can find integers r and s (≠ 0) such that √2 = r/s.
>
> Suppose r and s have a common factor other than 1. Then, we divide by the common factor to get √2 = a/b, where a and b are coprime.
>
> So, b√2 = a.
>
> Squaring on both sides and rearranging, we get 2b² = a². Therefore, 2 divides a².
>
> Now, by the theorem that if a prime divides a² then it divides a, it follows that 2 divides a.
>
> So, we can write a = 2c for some integer c.
>
> Substituting for a, we get 2b² = 4c², that is, b² = 2c².
>
> This means that 2 divides b², and so 2 divides b (again using that theorem with p = 2).
>
> Therefore, a and b have at least 2 as a common factor.
>
> But this contradicts the fact that a and b have no common factors other than 1.
>
> This contradiction has arisen because of our incorrect assumption that √2 is rational.
>
> So, we conclude that √2 is irrational.

*(Cleanup: "by Theorem 1.2" became the named theorem. The wording is `[authored]`.)*

---

## T9 · Rational and Irrational Numbers Together

### C34 · Rational with irrational: try it first
`kind: try` · `objectives: O24`
Media: new image spec "Mixing Rational and Irrational Numbers" — Two columns of cards. Left column, labelled 'Rational': 1, 4, 5 and 1/2. Right column, labelled 'Irrational': root 2, root 3 and root 5. Between them, two combination cards, 1 + root 2 and 4 x root 3, each with a blank sorting slot marked with a question mark.

[textbook_text]
> In Class IX, we mentioned that :
> - the sum or difference of a rational and an irrational number is irrational and
> - the product and quotient of a non-zero rational and irrational number is irrational.
>
> We prove some particular cases here.

[theorem_statement] *(taken from the text above)*
> The sum or difference of a rational and an irrational number is irrational. The product and quotient of a non-zero rational and an irrational number is irrational.

[predict] `[authored]`
> Guess whether 1 + √2 and 4√3 are rational or irrational. Commit to an answer. The next examples settle two similar cases and show how to argue for any of them.

---

## T10 · Examples: Proving Irrationality

### C35 · Is √3 irrational?
`kind: exercise (worked example)` · `objectives: O25`
Media: existing video "√3 Proof via the √2 Template" (old T13 VID1); existing image "√3 Irrationality Proof Layout (Example 5)" (old T13 O1.E1)

[question]
> Prove that √3 is irrational.

[worked solution, from source]
> Let us assume, to the contrary, that √3 is rational.
>
> That is, we can find integers a and b (≠ 0) such that √3 = a/b.
>
> Suppose a and b have a common factor other than 1, then we can divide by the common factor, and assume that a and b are coprime.
>
> So, b√3 = a.
>
> Squaring on both sides, and rearranging, we get 3b² = a².
>
> Therefore, a² is divisible by 3, and by the theorem that if a prime divides a² then it divides a, it follows that a is also divisible by 3.
>
> So, we can write a = 3c for some integer c.
>
> Substituting for a, we get 3b² = 9c², that is, b² = 3c².
>
> This means that b² is divisible by 3, and so b is also divisible by 3 (using that theorem with p = 3).
>
> Therefore, a and b have at least 3 as a common factor.
>
> But this contradicts the fact that a and b are coprime.
>
> This contradiction has arisen because of our incorrect assumption that √3 is rational.
>
> So, we conclude that √3 is irrational.

### C36 · Is 5 − √3 irrational?
`kind: exercise (worked example)` · `objectives: O26`
Media: existing video "Example 6 Walkthrough: 5 − √3 is Irrational" (old T14 VID1); existing image "Example 6: 5 − √3 Irrational Step Layout" (old T14 O1.E1)

[question]
> Show that 5 – √3 is irrational.

[worked solution, from source]
> Let us assume, to the contrary, that 5 – √3 is rational.
>
> That is, we can find coprime a and b (b ≠ 0) such that 5 – √3 = a/b.
>
> Therefore, 5 – a/b = √3.
>
> Rearranging this equation, we get √3 = 5 – a/b = (5b – a)/b.
>
> Since a and b are integers, we get 5 – a/b is rational, and so √3 is rational.
>
> But this contradicts the fact that √3 is irrational.
>
> This contradiction has arisen because of our incorrect assumption that 5 – √3 is rational.
>
> So, we conclude that 5 – √3 is irrational.

### C37 · Is 3√2 irrational?
`kind: exercise (worked example)` · `objectives: O27`
Media: existing video "Example 7 Walkthrough: 3√2 is Irrational" (old T15 VID1); existing image "Example 7: 3√2 Irrational Step Layout" (old T15 O1.E1)

[question]
> Show that 3√2 is irrational.

[worked solution, from source]
> Let us assume, to the contrary, that 3√2 is rational.
>
> That is, we can find coprime a and b (b ≠ 0) such that 3√2 = a/b.
>
> Rearranging, we get √2 = a/(3b).
>
> Since 3, a and b are integers, a/(3b) is rational, and so √2 is rational.
>
> But this contradicts the fact that √2 is irrational.
>
> So, we conclude that 3√2 is irrational.

---

## T11 · Questions: Proving Irrationality

This is the second exercise. Q3 has three separate sub-parts, so each is its own concept. Q1 and Q2 have no sub-parts. Same rules as the first set: `attempt_first`, one new hint-free image spec each, no video, and steps and answer *to author*. The book prints no hint and no figure for these questions.
Steps and answer are *to author* for all 5.

Objectives for this set: **O28** (apply) for Q1, and **O29** (apply) for Q2 and Q3 (i) to (iii).

### C38 · Proving Irrationality, Q1
`objectives: O28` · Media: new image spec (statement only)
> Prove that √5 is irrational.

### C39 · Proving Irrationality, Q2
`objectives: O29` · Media: new image spec (statement only)
> Prove that 3 + 2√5 is irrational.

### C40 · Proving Irrationality, Q3 (i)
`objectives: O29` · Media: new image spec (statement only)
> Prove that the following are irrationals :
> (i) 1/√2

### C41 · Proving Irrationality, Q3 (ii)
`objectives: O29` · Media: new image spec (statement only)
> Prove that the following are irrationals :
> (ii) 7√5

### C42 · Proving Irrationality, Q3 (iii)
`objectives: O29` · Media: new image spec (statement only)
> Prove that the following are irrationals :
> (iii) 6 + √2

---

# M4 · Wrap-up

## T12 · Chapter Summary

### C43 · Chapter summary
`kind: summary` · `objectives: O30`
Media: existing video "Real Numbers Chapter Recap" (old T17 VID1); existing image "Chapter 1 Summary Infographic" (old T17 O1.E1). Three images that give away a method or an answer are also re-homed here, because they cannot sit on a question concept: "Exercise 1.1 Strategy Reference Chart" (old T9 O3.E1) and "Exercise 1.2 Template and Citation Reference" (old T16 O3.E1), which are method cards, and "Sonia and Ravi on the Circular Sports Field" (old T8 O2.E2), which prints the answer to the last question of the first set (C28). The fit of all three is loose, please check. The first two are renamed at build, since their titles carry the book's exercise numbers.

[summary_points]
> In this chapter, you have studied the following points:
> 1. The Fundamental Theorem of Arithmetic : Every composite number can be expressed (factorised) as a product of primes, and this factorisation is unique, apart from the order in which the prime factors occur.
> 2. If p is a prime and p divides a², then p divides a, where a is a positive integer.
> 3. To prove that √2, √3 are irrationals.

### C44 · A note on three numbers
`kind: teach` · `objectives: O32`
Media: new image spec "HCF and LCM of Three Numbers" — A clean card for three positive integers p, q and r with three overlapping circles labelled p, q, r. The overlap regions are marked HCF(p, q), HCF(q, r), HCF(p, r) and the common centre is marked HCF(p, q, r). Beside it, the numbers 6, 72 and 120 are shown with the products 6 x 72 x 120 on one side and HCF x LCM on the other joined by a not-equal sign.

[textbook_text · "A note to the reader"]
> You have seen that :
> HCF (p, q, r) × LCM (p, q, r) ≠ p × q × r, where p, q, r are positive integers (see the 6, 72, 120 example). However, the following results hold good for three numbers p, q and r :
>
> LCM (p, q, r) = (p · q · r · HCF(p, q, r)) / (HCF(p, q) · HCF(q, r) · HCF(p, r))
>
> HCF (p, q, r) = (p · q · r · LCM(p, q, r)) / (LCM(p, q) · LCM(q, r) · LCM(p, r))

*(Cleanup: "(see Example 8)" became "(see the 6, 72, 120 example)", which is `[authored]`. The book has no Example 8.)*

---

# Appendix A · Objectives

Format: ID · bloom level · wording · old objective(s) it carries.

| ID | Bloom | Objective | Old ID |
|---|---|---|---|
| O1 | understand | Explain why prime numbers act as the building blocks of every natural number by contrasting build-up and factor-tree directions. | T1.O2 |
| O2 | apply | Represent 32,760 as the prime-power product 2³ × 3² × 5 × 7 × 13 using the factor-tree method in ascending order. | T2.O2 |
| O3 | apply | State the Fundamental Theorem of Arithmetic, that every composite number is a product of primes, unique apart from the order in which the prime factors occur, and predict and test it on a composite number such as 12. `[authored]` | T2.O1 |
| O4 | understand | Explain why 2 × 3 × 5 × 7 and 7 × 5 × 3 × 2 describe the same prime factorisation using the uniqueness clause of the Fundamental Theorem of Arithmetic. `[authored]` | T2.O3 |
| O5 | apply | Apply the Fundamental Theorem of Arithmetic to determine whether 4^n can end with the digit zero for any natural number n. | T3.O1 |
| O6 | understand | Explain why the HCF of two positive integers equals the product of the smallest power of each common prime factor. | T4.O1 |
| O7 | apply | Compute the HCF of two positive integers using the prime factorisation method. | T4.O2 |
| O8 | understand | Explain why the LCM of two positive integers equals the product of the greatest power of each prime factor involved in the numbers. | T5.O1 |
| O9 | apply | Compute the LCM of two positive integers using the prime factorisation method. | T5.O2 |
| O10 | apply | State the identity HCF(a,b) × LCM(a,b) = a × b for any two positive integers a and b, and predict and test it on a new pair. `[authored]` | T6.O1 |
| O11 | apply | Compute LCM(a,b) from the identity LCM(a,b) = (a × b) / HCF(a,b), as in the worked case of 96 and 404. `[authored]` | T6.O2 |
| O12 | apply | Compute HCF(6,72,120) and LCM(6,72,120) by prime factorisation, taking the smallest common power and greatest involved power of each prime. | T7.O1 |
| O13 | evaluate | Verify from the worked case of 6, 72 and 120 that 6 × 72 × 120 ≠ HCF(6,72,120) × LCM(6,72,120), showing the two-number product rule fails for three numbers. `[authored]` | T7.O2, T17.O3 |
| O14 | apply | Solve real-world timing and grouping problems by choosing HCF or LCM as the appropriate tool. | T8.O1 |
| O15 | analyze | Determine strategy for selecting HCF or LCM when a word problem describes simultaneous events or regular repetition. | T8.O2 |
| O16 | apply | Express numbers as products of primes, and find HCF and LCM of pairs and triples of integers by prime factorisation, using HCF × LCM = a × b to verify a result or to find an LCM from a given HCF. `[authored]` | T9.O1 |
| O17 | evaluate | Use the Fundamental Theorem of Arithmetic to justify why a power cannot end in zero and why a number such as 7 × 11 × 13 + 13 is composite, and decide whether a timing problem needs HCF or LCM. `[authored]` | T9.O2, T9.O3 |
| O18 | understand | Explain what makes a number irrational by contrasting it with the rational form p/q where q ≠ 0. | T10.O1 |
| O19 | analyze | Classify numbers such as √15, π, and √2/√3 as rational or irrational using the p/q test. | T10.O2 |
| O20 | apply | State the theorem that if a prime p divides a², then p divides a, where a is a positive integer, and predict and test it on a square such as 36. `[authored]` | new |
| O21 | evaluate | Prove that if a prime p divides the square of a positive integer a, then p must also divide a itself. | T11.O1 |
| O22 | apply | State the theorem that √2 is irrational, and predict where an assumption that it is a fraction a/b in lowest terms must break down. `[authored]` | new |
| O23 | evaluate | Prove that √2 is irrational by contradiction, using the theorem on prime factors of squares. | T12.O1 |
| O24 | apply | State that the sum or difference of a rational and an irrational number is irrational, and that the product and quotient of a non-zero rational and an irrational number is irrational, and predict and test them on simple cases. `[authored]` | new |
| O25 | evaluate | Prove that √3 is irrational by adapting the √2 contradiction argument with p = 3. | T13.O1 |
| O26 | apply | Construct a proof by contradiction that 5 − √3 is irrational by assuming it equals a/b with coprime integers. | T14.O1 |
| O27 | apply | Construct a proof by contradiction that 3√2 is irrational, showing √2 would have to be rational. | T15.O1 |
| O28 | apply | Prove by contradiction that √5 is irrational, applying the theorem on a prime dividing a² with p = 5 to 5b² = a². `[authored]` | T16.O1 |
| O29 | apply | Prove that numbers such as 3 + 2√5, 1/√2, 7√5 and 6 + √2 are irrational by isolating the radical and citing the irrationality of √2 or √5, choosing between the squaring and the rearranging method. `[authored]` | T16.O2, T16.O3 |
| O30 | understand | Explain how the Fundamental Theorem of Arithmetic underpins HCF and LCM computation and the irrationality proofs of √2 and √3. `[authored]` | T17.O1 |
| O31 | understand | State Euclid's division algorithm, that any positive integer a can be divided by a positive integer b leaving a remainder r that is smaller than b. `[authored]` | T1.O1 |
| O32 | apply | Compute LCM(p, q, r) for three positive integers using the formula in terms of HCF(p, q, r), HCF(p, q), HCF(q, r) and HCF(p, r). `[authored]` | T17.O2 |

Notes on the table:
- The old "choose the technique" objectives (T9.O3, T16.O3) are folded into the wording of the question-set objectives O17 and O29.
- T17.O3 (why HCF × LCM is not the product for three numbers) is merged into O13. The book gives only the numerical check, so the exponent-accounting argument stays in the carried recall questions (Appendix C).
- Enrichment concepts (C6, C7) carry no objective, and no objective above mentions them.
- O14 and O15 (word problems, HCF or LCM) are now anchored on the Sonia and Ravi question (C28). Their former teach concept was dropped (Appendix B).

**Old objectives now carried as new objectives**
- T1.O1 (Euclid's division algorithm) is carried as O31, reworded without the section number, and anchored on the hook (C1), whose text states the algorithm.
- T17.O2 (LCM of three numbers) is carried as O32, reworded without the note's name, and anchored on C44, which is now a teach concept after the summary (textbook order).
- Every old objective is carried.

# Appendix B · Held assets (not attached to the new plan; nothing deleted)

**Five old tools** (no tools in this chapter):
- T1 "Euclid's Division Lemma Visualizer" (T2D1)
- T2 "Factor Tree Builder (interactive)" (T2D1)
- T3 "\"Does It End in Zero?\" Prime Detective" (T2D1)
- T6 "HCF × LCM = a × b Verifier" (T2D1)
- T10 "Rational vs Irrational Sorter" (T2D1)

**Two old exercise videos** (no question videos for now):
- T9 "Exercise 1.1 Strategy Recap" (VID1)
- T16 "Exercise 1.2 Strategy Recap" (VID1)

**Two old image records with no media entry** (found only under the objectives of the HCF method topic; both are embedded pictures with empty prompts, not usable as they stand):
- T4 "New image" (id M1.S2.T4.M1.S2.T4.O1.E1)
- T4 "HCF " (id M1.S2.T4.M1.S2.T4.O2.E3, caption "HCF of two numbers using prime factorization")

**Three media of a dropped concept** (the teach concept on reading a story as an HCF or an LCM was removed from the plan; reason for all three: concept dropped (authored text, not in the book)):
- T8 "Reading the Story into Maths: HCF or LCM?" (VID1)
- T8 "Anjali and Grandfather at Shivaji Park — Translation Scaffold" (O2.E1)
- T4 "Tiling Scenario: 468 cm × 396 cm Pune Hall" (O2.E2)

# Appendix C · Carried-over fields

Every old topic's `recall_questions`, `summary`, `key_terms`, `concept_bullets`, `brief_summary`, `detailed_summary` and `important_points` carry into the new topic that holds its text. The module-level `summary`, `brief_summary`, `detailed_summary` and `important_points` carry into the three matching modules. They are not shown here, to keep this file reviewable. The nothing-deleted check at build time compares them field by field.

Where each old topic lands:

| Old topic | New home |
|---|---|
| T1 Chapter Introduction | T1 (C1) and the opening of T2 (C2) |
| T2 Statement of the Fundamental Theorem of Arithmetic | T2 (C2–C7) |
| T3 Applying FTA: Can 4^n End in the Digit Zero? | T3 (C8) |
| T4 HCF by Prime Factorisation | T4 (C9), T5 (C12). One image is held (Appendix B) |
| T5 LCM by Prime Factorisation | T4 (C10) |
| T6 The Relationship HCF(a,b) × LCM(a,b) = a × b | T4 (C11), T5 (C12) |
| T7 HCF and LCM of Three Numbers | T5 (C13) |
| T8 Word Problems Using HCF and LCM | T6 (C28, the Sonia and Ravi question), T12 (C43, one image). The story-reading concept was dropped and its video and image are held (Appendix B) |
| T9 Exercise 1.1 — Consolidated Practice | T6 (C14–C27), T12 (C43, one image) |
| T10 Revisiting Irrational Numbers | T7 (C29) |
| T11 Key Lemma: If a Prime Divides a², It Divides a | T8 (C30, C31) |
| T12 Proof That √2 is Irrational | T8 (C32, C33) |
| T13 Proof That √3 is Irrational | T10 (C35) |
| T14 Irrationality of a Rational Plus or Minus an Irrational | T9 (C34), T10 (C36) |
| T15 Irrationality of a Non-Zero Rational Times an Irrational | T10 (C37) |
| T16 Exercise 1.2 — Practice with Irrationality Proofs | T11 (C38–C42), T12 (C43, one image) |
| T17 Chapter Summary and HCF/LCM Formulas for Three Numbers | T12 (C43, C44) |
