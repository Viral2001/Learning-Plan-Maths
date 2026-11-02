# Representative learning plan: Class 10, Statistics (maths10_ch13)

A review copy of the restructured plan, down to concept level. Content is shown in full. Media are only named and never embedded.

Source: `learning_plan_std10_chap13_version1.json` and the chapter PDF (reprint 2026-27). Shape follows the Class 9 circles plan and the Class 10 coordinate geometry plan.

## Read this first

**Standing decisions**
- No tools in this chapter. The five old `2d_tool` items are held (Appendix B).
- No videos for exercise questions. Each question concept gets one hint-free image spec and no video. The old plan has no exercise-question videos.
- Examples keep the existing videos and images that match them. No new example media is planned.
- The question order inside a Questions topic is the textbook order. No exercise question in this chapter has lettered sub-parts, so each question is one concept.

**What a concept entry shows**
- `kind`: try, prove, teach, enrich, hook, exercise or summary.
- `objectives`: objective IDs. Enrichment concepts have none.
- `media`: existing assets re-homed from the old plan, new asset specs, or none.
- `[block_kind]` tags are review labels only. They never reach the student.

**Text cleanup applied to everything below**
- Section headings ("13.2 Mean of Grouped Data" and so on) are removed. The topic names carry them.
- "Table 13.x" and "see Table 13.x" become "the table above", "the table below" or a plain description. The book's misprint "Table 14.5" becomes "the table above".
- "Column 1", "Column 3" and "Column 4" become "the first column", "the third column" and "the fourth column".
- "Example n" pointers become plain phrases ("the marks of 30 students", "the family-size survey"). "Example n:" and "Exercise 13.x" labels are removed.
- "Activity n :" labels are removed. The activity text is kept.
- In the female-teachers example, the source line keeps the survey name and drops "conducted by NCERT".
- The PDF shows the rupee sign as a stray character. It is written ₹ here.
- "Class IX" and "Class X" stay. They are not book numbers.
- Book references stay only in metadata (`ncert_refs`), which is not shown here.

**Marked in the text**
- `[authored]` marks text that is not in the old plan or the book. These are predictions and answers to "(Why?)" prompts. No new objective was needed.
- Question solutions (`steps` and `answer`) are not in the old plan. They are marked *to author* and nothing is invented here.

**Content flags for review (not student-facing)**
- The old image "Annotated Table 13.5 — the step-deviation transformation" (old T4 image, on C10) states Σfᵢuᵢ = 24 in its description. The book has 29. Fix before generation.
- The old video "Applying the mode formula — Example 5 and Example 6 walkthrough" (old T7 video, on C28) describes the family-size example with modal class 1–3 and mode ≈ 1.875. The book has modal class 3–5 and mode 3.286. Fix before generation.
- The introduction and the closing note mention ogives (cumulative frequency curves). This reprint has no ogive section and no ogive exercise. The text is kept as it is. The old "Ogive Constructor" tool is held.

## Plan at a glance

| Module | Topic | Concepts |
|---|---|---|
| M1 Mean of grouped data | T1 From Ungrouped to Grouped Data (hook) | C1 |
| | T2 The Mean of Grouped Data | C2–C11 |
| | T3 Examples: Mean of Grouped Data | C12–C14 |
| | T4 Questions: Mean of Grouped Data | C15–C23 |
| M2 Mode of grouped data | T5 The Mode of Grouped Data | C24–C26 |
| | T6 Examples: Mode of Grouped Data | C27–C29 |
| | T7 Questions: Mode of Grouped Data | C30–C35 |
| M3 Median of grouped data | T8 Cumulative Frequency | C36–C39 |
| | T9 The Median of Grouped Data | C40–C41 |
| | T10 Examples: Median of Grouped Data | C42–C43 |
| | T11 Choosing a Measure of Central Tendency | C44–C45 |
| | T12 Questions: Median of Grouped Data | C46–C52 |
| M4 Wrap-up | T13 Chapter Summary | C53–C54 |

Totals: 54 concepts and 24 objectives. 22 question concepts need a new image. 0 new videos. Old media: 21 attached and 7 held, out of 28.

---

# M1 · Mean of grouped data

## T1 · From Ungrouped to Grouped Data (hook)

### C1 · Mean, median and mode, now for grouped data
`kind: hook` · `is_enrichment: true` · `objectives: none`
Media: existing video "Why grouped data needs new methods — a 60-second recap" (old T1 VID1)

[textbook_text]
> In Class IX, you have studied the classification of given data into ungrouped as well as grouped frequency distributions. You have also learnt to represent the data pictorially in the form of various graphs such as bar graphs, histograms (including those of varying widths) and frequency polygons. In fact, you went a step further by studying certain numerical representatives of the ungrouped data, also called measures of central tendency, namely, mean, median and mode. In this chapter, we shall extend the study of these three measures, i.e., mean, median and mode from ungrouped data to that of grouped data. We shall also discuss the concept of cumulative frequency, the cumulative frequency distribution and how to draw cumulative frequency curves, called ogives.

*(Cleanup: the section heading was removed. No words dropped.)*

---

## T2 · The Mean of Grouped Data

### C2 · The mean of data with frequencies
`kind: teach` · `objectives: O1`
Media: existing image "Mind-map: Mean, Median, Mode for ungrouped vs grouped data" (old T1 O1.E1)

[textbook_text]
> The mean (or average) of observations, as we know, is the sum of the values of all the observations divided by the total number of observations. From Class IX, recall that if x₁, x₂, . . ., xₙ are observations with respective frequencies f₁, f₂, . . ., fₙ, then this means observation x₁ occurs f₁ times, x₂ occurs f₂ times, and so on.
>
> Now, the sum of the values of all the observations = f₁x₁ + f₂x₂ + . . . + fₙxₙ, and the number of observations = f₁ + f₂ + . . . + fₙ.
>
> So, the mean x̄ of the data is given by
> x̄ = (f₁x₁ + f₂x₂ + . . . + fₙxₙ) / (f₁ + f₂ + . . . + fₙ)
>
> Recall that we can write this in short form by using the Greek letter Σ (capital sigma) which means summation. That is,
> x̄ = (Σᵢ₌₁ⁿ fᵢxᵢ) / (Σᵢ₌₁ⁿ fᵢ)
> which, more briefly, is written as x̄ = Σfᵢxᵢ / Σfᵢ, if it is understood that i varies from 1 to n.
>
> Let us apply this formula to find the mean in the following example.

### C3 · The mean marks of 30 students
`kind: exercise (worked example)` · `objectives: O1`
Media: new image spec "Marks of 30 Students" — A clean frequency table titled marks out of 100 for 30 students of Class X. The top row lists the marks 10, 20, 36, 40, 50, 56, 60, 70, 72, 80, 88, 92, 95 and the row below gives the number of students for each: 1, 1, 3, 4, 3, 2, 4, 4, 1, 1, 2, 3, 1. Beside it, a small icon of a mathematics answer sheet marked out of 100. No totals or products are shown.

[question]
> The marks obtained by 30 students of Class X of a certain school in a Mathematics paper consisting of 100 marks are presented in the table below. Find the mean of the marks obtained by the students.
> | Marks obtained (xᵢ) | 10 | 20 | 36 | 40 | 50 | 56 | 60 | 70 | 72 | 80 | 88 | 92 | 95 |
> | Number of students (fᵢ) | 1 | 1 | 3 | 4 | 3 | 2 | 4 | 4 | 1 | 1 | 2 | 3 | 1 |

[worked solution, from source]
> Recall that to find the mean marks, we require the product of each xᵢ with the corresponding frequency fᵢ. So, let us put them in a column as shown in the table below.
> | Marks obtained (xᵢ) | Number of students (fᵢ) | fᵢxᵢ |
> | 10 | 1 | 10 |
> | 20 | 1 | 20 |
> | 36 | 3 | 108 |
> | 40 | 4 | 160 |
> | 50 | 3 | 150 |
> | 56 | 2 | 112 |
> | 60 | 4 | 240 |
> | 70 | 4 | 280 |
> | 72 | 1 | 72 |
> | 80 | 1 | 80 |
> | 88 | 2 | 176 |
> | 92 | 3 | 276 |
> | 95 | 1 | 95 |
> | Total | Σfᵢ = 30 | Σfᵢxᵢ = 1779 |
>
> Now, x̄ = Σfᵢxᵢ / Σfᵢ = 1779 / 30 = 59.3
> Therefore, the mean marks obtained is 59.3.

### C4 · Grouping the data and choosing a class mark
`kind: teach` · `objectives: O2, O3`
Media: new image spec "From Raw Marks to Class Intervals" — Two panels joined by an arrow. On the left, the 30 students' marks appear as small dots along a marks line from 10 to 100. On the right, the same line is cut into six equal class intervals of width 15, namely 10-25, 25-40, 40-55, 55-70, 70-85 and 85-100, with the frequencies 2, 3, 7, 6, 6, 6 written above them. A note shows that a mark equal to an upper limit, such as 40, falls in the next class. A midpoint tick sits inside each interval.
No tool, so this concept has the method statement and a prediction only.

[textbook_text]
> In most of our real life situations, data is usually so large that to make a meaningful study it needs to be condensed as grouped data. So, we need to convert given ungrouped data into grouped data and devise some method to find its mean.
>
> Let us convert the ungrouped data of the 30 students' marks into grouped data by forming class-intervals of width, say 15. Remember that, while allocating frequencies to each class-interval, students falling in any upper class-limit would be considered in the next class, e.g., 4 students who have obtained 40 marks would be considered in the class-interval 40-55 and not in 25-40. With this convention in our mind, let us form a grouped frequency distribution table.
> | Class interval | 10-25 | 25-40 | 40-55 | 55-70 | 70-85 | 85-100 |
> | Number of students | 2 | 3 | 7 | 6 | 6 | 6 |
>
> Now, for each class-interval, we require a point which would serve as the representative of the whole class. It is assumed that the frequency of each class-interval is centred around its mid-point. So the mid-point (or class mark) of each class can be chosen to represent the observations falling in the class. Recall that we find the mid-point of a class (or its class mark) by finding the average of its upper and lower limits. That is,
> Class mark = (Upper class limit + Lower class limit) / 2

[method_statement] *(authored from the chapter summary)*
> The direct method: x̄ = Σfᵢxᵢ / Σfᵢ, where xᵢ is the class mark of the i-th class and fᵢ its frequency, with the assumption that the frequency of a class is centred at its class mark.

[predict] `[authored]`
> The same 30 marks gave an exact mean of 59.3. Once the marks are grouped and each class is replaced by its class mark, will the mean still come out as 59.3, a little more, or a little less? Commit to an answer before you look at the next concept.

### C5 · The direct method
`kind: teach` · `objectives: O3, O4`
Media: existing video "Walkthrough: computing the mean by Direct Method on NCERT Example 1" (old T2 VID1); existing image "Annotated NCERT Table 13.3 with Direct Method columns" (old T2 O1.E1)

[textbook_text]
> For the class 10-25, the class mark is (10 + 25)/2, i.e., 17.5. Similarly, we can find the class marks of the remaining class intervals. We put them in the table below. These class marks serve as our xᵢ's. Now, in general, for the i-th class interval, we have the frequency fᵢ corresponding to the class mark xᵢ. We can now proceed to compute the mean in the same manner as for the ungrouped marks.
> | Class interval | Number of students (fᵢ) | Class mark (xᵢ) | fᵢxᵢ |
> | 10-25 | 2 | 17.5 | 35.0 |
> | 25-40 | 3 | 32.5 | 97.5 |
> | 40-55 | 7 | 47.5 | 332.5 |
> | 55-70 | 6 | 62.5 | 375.0 |
> | 70-85 | 6 | 77.5 | 465.0 |
> | 85-100 | 6 | 92.5 | 555.0 |
> | Total | Σfᵢ = 30 | | Σfᵢxᵢ = 1860.0 |
>
> The sum of the values in the last column gives us Σfᵢxᵢ. So, the mean x̄ of the given data is given by
> x̄ = Σfᵢxᵢ / Σfᵢ = 1860.0 / 30 = 62
>
> This new method of finding the mean is known as the Direct Method.
>
> We observe that the ungrouped table and the grouped table are using the same data and employing the same formula for the calculation of the mean but the results obtained are different. Can you think why this is so, and which one is more accurate? The difference in the two values is because of the mid-point assumption in the grouped table, 59.3 being the exact mean, while 62 an approximate mean.

*(Cleanup: "With reference to Table 13.2" was dropped from the first sentence; "Tables 13.1 and 13.3" became "the ungrouped table and the grouped table". Media titles keep the book labels here; see the flag on clean_title in the report.)*

### C6 · The assumed mean method: try it first
`kind: try` · `objectives: O5`
Media: new image spec "Class Marks on a Number Line" — A number line from 10 to 100 divided into the six class intervals 10-25, 25-40, 40-55, 55-70, 70-85 and 85-100. The class marks 17.5, 32.5, 47.5, 62.5, 77.5 and 92.5 are marked as dots at the middle of each class, with their frequencies 2, 3, 7, 6, 6, 6 under them. The class mark 47.5 is circled and labelled a, the chosen assumed mean. No deviations or means are shown.
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[textbook_text]
> Sometimes when the numerical values of xᵢ and fᵢ are large, finding the product of xᵢ and fᵢ becomes tedious and time consuming. So, for such situations, let us think of a method of reducing these calculations.
>
> We can do nothing with the fᵢ's, but we can change each xᵢ to a smaller number so that our calculations become easy. How do we do this? What about subtracting a fixed number from each of these xᵢ's? Let us try this method.

[theorem_statement] *(authored from the chapter summary)*
> The assumed mean method: x̄ = a + Σfᵢdᵢ / Σfᵢ, where a is the assumed mean and dᵢ = xᵢ – a.

[predict] `[authored]`
> Suppose you subtract 47.5 from every class mark, and then find the mean of what is left. That mean will be far smaller than 62. What must you do to it at the end to get back the real mean? Commit to an answer, then check it in the next concept.

### C7 · Why the assumed mean method works
`kind: prove` · `objectives: O5`
Media: existing video "Why the Assumed Mean Method gives the same answer as the Direct Method" (old T3 VID1); existing image "Deviation-from-assumed-mean visual with NCERT Table 13.4" (old T3 O1.E1)

[textbook_text]
> The first step is to choose one among the xᵢ's as the assumed mean, and denote it by 'a'. Also, to further reduce our calculation work, we may take 'a' to be that xᵢ which lies in the centre of x₁, x₂, . . ., xₙ. So, we can choose a = 47.5 or a = 62.5. Let us choose a = 47.5.
>
> The next step is to find the difference dᵢ between a and each of the xᵢ's, that is, the deviation of 'a' from each of the xᵢ's.
> i.e., dᵢ = xᵢ – a = xᵢ – 47.5
>
> The third step is to find the product of dᵢ with the corresponding fᵢ, and take the sum of all the fᵢdᵢ's. The calculations are shown in the table below.
> | Class interval | Number of students (fᵢ) | Class mark (xᵢ) | dᵢ = xᵢ – 47.5 | fᵢdᵢ |
> | 10-25 | 2 | 17.5 | –30 | –60 |
> | 25-40 | 3 | 32.5 | –15 | –45 |
> | 40-55 | 7 | 47.5 | 0 | 0 |
> | 55-70 | 6 | 62.5 | 15 | 90 |
> | 70-85 | 6 | 77.5 | 30 | 180 |
> | 85-100 | 6 | 92.5 | 45 | 270 |
> | Total | Σfᵢ = 30 | | | Σfᵢdᵢ = 435 |
>
> So, from the table above, the mean of the deviations, d̄ = Σfᵢdᵢ / Σfᵢ.
>
> Now, let us find the relation between d̄ and x̄.
>
> Since in obtaining dᵢ, we subtracted 'a' from each xᵢ, so, in order to get the mean x̄, we need to add 'a' to d̄. This can be explained mathematically as:
> Mean of deviations, d̄ = Σfᵢdᵢ / Σfᵢ
> So, d̄ = Σfᵢ(xᵢ – a) / Σfᵢ = Σfᵢxᵢ / Σfᵢ – (Σfᵢa) / Σfᵢ = x̄ – a (Σfᵢ / Σfᵢ) = x̄ – a
> So, x̄ = a + d̄
> i.e., x̄ = a + Σfᵢdᵢ / Σfᵢ
>
> Substituting the values of a, Σfᵢdᵢ and Σfᵢ from the table above, we get
> x̄ = 47.5 + 435/30 = 47.5 + 14.5 = 62.
> Therefore, the mean of the marks obtained by the students is 62.
>
> The method discussed above is called the Assumed Mean Method.

### C8 · The mean does not depend on the choice of a
`kind: teach` · `objectives: O6`
Media: new image spec "Different Choices of a, One Mean" — The six class marks 17.5, 32.5, 47.5, 62.5, 77.5 and 92.5 drawn as dots on a number line. Three of them, 17.5, 47.5 and 92.5, are each highlighted in turn as a, with three separate arrows labelled choice one, choice two and choice three. All three arrows lead to the same box that reads mean = 62.

[textbook_text]
> From the grouped table of the 30 students' marks, find the mean by taking each of xᵢ (i.e., 17.5, 32.5, and so on) as 'a'. What do you observe? You will find that the mean determined in each case is the same, i.e., 62. (Why?)
>
> So, we can say that the value of the mean obtained does not depend on the choice of 'a'.

*(Cleanup: the "Activity 1 :" label was removed and "From the Table 13.3" became "From the grouped table of the 30 students' marks". The "(Why?)" answer is in C11.)*

### C9 · The step-deviation method: try it first
`kind: try` · `objectives: O7`
Media: new image spec "Class Size and Deviations Together" — A table for the grouped marks with columns for class interval, frequency, class mark and deviation from a = 47.5. The rows are 10-25 with 2, 17.5 and -30; 25-40 with 3, 32.5 and -15; 40-55 with 7, 47.5 and 0; 55-70 with 6, 62.5 and 15; 70-85 with 6, 77.5 and 30; 85-100 with 6, 92.5 and 45. A bracket beside the table marks the class size h = 15.
No tool, so this concept has the statement and a prediction only. There is no try-it step.

[textbook_text]
> Observe that in the table of deviations, the values in the fourth column are all multiples of 15. So, if we divide the values in the entire fourth column by 15, we would get smaller numbers to multiply with fᵢ. (Here, 15 is the class size of each class interval.)
>
> So, let uᵢ = (xᵢ – a)/h, where a is the assumed mean and h is the class size.

[theorem_statement] *(authored from the chapter summary)*
> The step-deviation method: x̄ = a + h × (Σfᵢuᵢ / Σfᵢ), where uᵢ = (xᵢ – a)/h.

[predict] `[authored]`
> Each deviation is now divided by 15 before you multiply by the frequency. So the mean of the uᵢ's is fifteen times too small to stand for a deviation in marks. What two things must you do to it at the end to get back the mean marks? Commit, then check in the next concept.

### C10 · Why the step-deviation method works
`kind: prove` · `objectives: O7`
Media: existing image "Annotated NCERT Table 13.5 — the step-deviation transformation" (old T4 O1.E1)

[textbook_text]
> Now, we calculate uᵢ in this way and continue as before (i.e., find fᵢuᵢ and then Σfᵢuᵢ). Taking h = 15, let us form the table below.
> | Class interval | fᵢ | xᵢ | dᵢ = xᵢ – a | uᵢ = (xᵢ – a)/h | fᵢuᵢ |
> | 10-25 | 2 | 17.5 | –30 | –2 | –4 |
> | 25-40 | 3 | 32.5 | –15 | –1 | –3 |
> | 40-55 | 7 | 47.5 | 0 | 0 | 0 |
> | 55-70 | 6 | 62.5 | 15 | 1 | 6 |
> | 70-85 | 6 | 77.5 | 30 | 2 | 12 |
> | 85-100 | 6 | 92.5 | 45 | 3 | 18 |
> | Total | Σfᵢ = 30 | | | | Σfᵢuᵢ = 29 |
>
> Let ū = Σfᵢuᵢ / Σfᵢ.
>
> Here, again let us find the relation between ū and x̄.
>
> We have, uᵢ = (xᵢ – a)/h
> Therefore, ū = Σfᵢ(xᵢ – a)/h / Σfᵢ = (1/h) × (Σfᵢxᵢ – aΣfᵢ) / Σfᵢ = (1/h) × (Σfᵢxᵢ / Σfᵢ – a Σfᵢ / Σfᵢ) = (1/h) × (x̄ – a)
> So, hū = x̄ – a
> i.e., x̄ = a + hū
> So, x̄ = a + h × (Σfᵢuᵢ / Σfᵢ)
>
> Now, substituting the values of a, h, Σfᵢuᵢ and Σfᵢ from the table above, we get
> x̄ = 47.5 + 15 × (29/30) = 47.5 + 14.5 = 62
> So, the mean marks obtained by a student is 62.
>
> The method discussed above is called the Step-deviation method.
>
> We note that:
> the step-deviation method will be convenient to apply if all the dᵢ's have a common factor.
> The mean obtained by all the three methods is the same.
> The assumed mean method and step-deviation method are just simplified forms of the direct method.
> The formula x̄ = a + hū still holds if a and h are not as given above, but are any non-zero numbers such that uᵢ = (xᵢ – a)/h.
>
> Let us apply these methods in another example.

*(Cleanup: "Table 14.5" (a misprint in the book for 13.5) became "the table above". Review flag: the re-homed image's description says Σfᵢuᵢ = 24; the book has 29.)*

### C11 · More to explore: why any choice of a gives the same mean
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Subtract a, Then Add It Back" — A number line scene with the class marks 17.5 to 92.5 shown as a row of dots with their frequencies. Below it, a second copy of the same row is slid to the left so that the assumed value a sits at zero, joined to the first row by an arrow labelled subtract a. A return arrow from the shifted row back to the original is labelled add a back, and the mean 62 is marked on the original row.

[enrichment] `[authored answer]`
> **Q.** If you take each class mark in turn (17.5, 32.5, and so on) as 'a', you get the mean 62 every time. Why?
> **A.** For any a, Σfᵢdᵢ / Σfᵢ = Σfᵢ(xᵢ – a) / Σfᵢ = x̄ – a. So a + Σfᵢdᵢ / Σfᵢ = a + (x̄ – a) = x̄. Whatever you subtract at the start, you add back at the end, so a cancels out.

---

## T3 · Examples: Mean of Grouped Data

### C12 · Mean percentage of female teachers, by all three methods
`kind: exercise (worked example)` · `objectives: O7, O8`
Media: existing video "Choosing the right mean method — a decision guide" (old T4 VID1). The fit is loose: the video routes all three opening examples through a method choice, so please check it in review.

[question]
> The table below gives the percentage distribution of female teachers in the primary schools of rural areas of various states and union territories (U.T.) of India. Find the mean percentage of female teachers by all the three methods discussed so far.
> | Percentage of female teachers | 15 - 25 | 25 - 35 | 35 - 45 | 45 - 55 | 55 - 65 | 65 - 75 | 75 - 85 |
> | Number of States/U.T. | 6 | 11 | 7 | 4 | 4 | 2 | 1 |
> Source: Seventh All India School Education Survey

[worked solution, from source]
> Let us find the class marks, xᵢ, of each class, and put them in a column:
> | Percentage of female teachers | Number of States/U.T. (fᵢ) | xᵢ |
> | 15 - 25 | 6 | 20 |
> | 25 - 35 | 11 | 30 |
> | 35 - 45 | 7 | 40 |
> | 45 - 55 | 4 | 50 |
> | 55 - 65 | 4 | 60 |
> | 65 - 75 | 2 | 70 |
> | 75 - 85 | 1 | 80 |
>
> Here we take a = 50, h = 10, then dᵢ = xᵢ – 50 and uᵢ = (xᵢ – 50)/10.
> We now find dᵢ and uᵢ and put them in the table below.
> | Percentage of female teachers | Number of states/U.T. (fᵢ) | xᵢ | dᵢ = xᵢ – 50 | uᵢ = (xᵢ – 50)/10 | fᵢxᵢ | fᵢdᵢ | fᵢuᵢ |
> | 15 - 25 | 6 | 20 | –30 | –3 | 120 | –180 | –18 |
> | 25 - 35 | 11 | 30 | –20 | –2 | 330 | –220 | –22 |
> | 35 - 45 | 7 | 40 | –10 | –1 | 280 | –70 | –7 |
> | 45 - 55 | 4 | 50 | 0 | 0 | 200 | 0 | 0 |
> | 55 - 65 | 4 | 60 | 10 | 1 | 240 | 40 | 4 |
> | 65 - 75 | 2 | 70 | 20 | 2 | 140 | 40 | 4 |
> | 75 - 85 | 1 | 80 | 30 | 3 | 80 | 30 | 3 |
> | Total | 35 | | | | 1390 | –360 | –36 |
>
> From the table above, we obtain Σfᵢ = 35, Σfᵢxᵢ = 1390, Σfᵢdᵢ = –360, Σfᵢuᵢ = –36.
> Using the direct method, x̄ = Σfᵢxᵢ / Σfᵢ = 1390/35 = 39.71
> Using the assumed mean method, x̄ = a + Σfᵢdᵢ / Σfᵢ = 50 + (–360)/35 = 39.71
> Using the step-deviation method, x̄ = a + (Σfᵢuᵢ / Σfᵢ) × h = 50 + (–36/35) × 10 = 39.71
> Therefore, the mean percentage of female teachers in the primary schools of rural areas is 39.71.

[remark, from source]
> The result obtained by all the three methods is the same. So the choice of method to be used depends on the numerical values of xᵢ and fᵢ. If xᵢ and fᵢ are sufficiently small, then the direct method is an appropriate choice. If xᵢ and fᵢ are numerically large numbers, then we can go for the assumed mean method or step-deviation method. If the class sizes are unequal, and xᵢ are large numerically, we can still apply the step-deviation method by taking h to be a suitable divisor of all the dᵢ's.

*(Cleanup: "discussed in this section" became "discussed so far"; the source line drops "conducted by NCERT".)*

### C13 · Mean number of wickets, with unequal classes
`kind: exercise (worked example)` · `objectives: O7, O8`
Media: new image spec "Wickets Taken by One Day Bowlers" — A frequency table titled number of wickets taken by bowlers in one-day cricket matches. The classes are 20-60, 60-100, 100-150, 150-250, 250-350 and 350-450 with 7, 5, 16, 12, 2 and 3 bowlers. The class bars above the table have visibly unequal widths. A small cricket ball and stumps sit beside the table. No class marks or means are shown.

[question]
> The distribution below shows the number of wickets taken by bowlers in one-day cricket matches. Find the mean number of wickets by choosing a suitable method. What does the mean signify?
> | Number of wickets | 20 - 60 | 60 - 100 | 100 - 150 | 150 - 250 | 250 - 350 | 350 - 450 |
> | Number of bowlers | 7 | 5 | 16 | 12 | 2 | 3 |

[worked solution, from source]
> Here, the class size varies, and the xᵢ's are large. Let us still apply the step-deviation method with a = 200 and h = 20. Then, we obtain the data as in the table below.
> | Number of wickets taken | Number of bowlers (fᵢ) | xᵢ | dᵢ = xᵢ – 200 | uᵢ = dᵢ/20 | uᵢfᵢ |
> | 20 - 60 | 7 | 40 | –160 | –8 | –56 |
> | 60 - 100 | 5 | 80 | –120 | –6 | –30 |
> | 100 - 150 | 16 | 125 | –75 | –3.75 | –60 |
> | 150 - 250 | 12 | 200 | 0 | 0 | 0 |
> | 250 - 350 | 2 | 300 | 100 | 5 | 10 |
> | 350 - 450 | 3 | 400 | 200 | 10 | 30 |
> | Total | 45 | | | | –106 |
>
> So, ū = –106/45. Therefore, x̄ = 200 + 20 × (–106/45) = 200 – 47.11 = 152.89.
> This tells us that, on an average, the number of wickets taken by these 45 bowlers in one-day cricket is 152.89.
>
> Now, let us see how well you can apply the concepts discussed so far!

### C14 · Class activity: collect your own data and find its mean
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Three Groups Collect Class Data" — Three illustrated panels, each with a small group of students. The first group holds a sheet of mathematics exam marks, the second reads a thermometer beside a 30 day calendar, the third measures a classmate's height with a tape against a wall. Each panel has an arrow leading to an empty grouped frequency table with columns for class interval and frequency.

[enrichment, from source]
> Divide the students of your class into three groups and ask each group to do one of the following activities.
> (a) Collect the marks obtained by all the students of your class in Mathematics in the latest examination conducted by your school. Form a grouped frequency distribution of the data obtained.
> (b) Collect the daily maximum temperatures recorded for a period of 30 days in your city. Present this data as a grouped frequency table.
> (c) Measure the heights of all the students of your class (in cm) and form a grouped frequency distribution table of this data.
>
> After all the groups have collected the data and formed grouped frequency distribution tables, the groups should find the mean in each case by the method which they find appropriate.

*(Cleanup: the "Activity 2 :" label was removed. The book's items 1 to 3 are lettered (a) to (c), because "table." followed by "3" reads as a table number to the leak check.)*

---

## T4 · Questions: Mean of Grouped Data

Objectives for this set: O9 (apply) find the mean of a grouped distribution, choosing the most efficient of the direct, assumed mean and step-deviation methods; O10 (analyze) find a missing frequency when the mean is given.

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, statement only (with its data table), no working and no answer. There is no video. Hint, solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for all 9.
The questions are in textbook order. None has lettered sub-parts, so each is one concept.

### C15 · Mean of Grouped Data, Q1
`objectives: O9` · Media: new image spec (statement only)
> A survey was conducted by a group of students as a part of their environment awareness programme, in which they collected the following data regarding the number of plants in 20 houses in a locality. Find the mean number of plants per house.
> | Number of plants | 0 - 2 | 2 - 4 | 4 - 6 | 6 - 8 | 8 - 10 | 10 - 12 | 12 - 14 |
> | Number of houses | 1 | 2 | 1 | 5 | 6 | 2 | 3 |
> Which method did you use for finding the mean, and why?

### C16 · Mean of Grouped Data, Q2
`objectives: O9` · Media: new image spec (statement only)
> Consider the following distribution of daily wages of 50 workers of a factory.
> | Daily wages (in ₹) | 500 - 520 | 520 - 540 | 540 - 560 | 560 - 580 | 580 - 600 |
> | Number of workers | 12 | 14 | 8 | 6 | 10 |
> Find the mean daily wages of the workers of the factory by using an appropriate method.

### C17 · Mean of Grouped Data, Q3
`objectives: O10` · Media: new image spec (statement only)
> The following distribution shows the daily pocket allowance of children of a locality. The mean pocket allowance is ₹ 18. Find the missing frequency f.
> | Daily pocket allowance (in ₹) | 11 - 13 | 13 - 15 | 15 - 17 | 17 - 19 | 19 - 21 | 21 - 23 | 23 - 25 |
> | Number of children | 7 | 6 | 9 | 13 | f | 5 | 4 |

### C18 · Mean of Grouped Data, Q4
`objectives: O9` · Media: new image spec (statement only)
> Thirty women were examined in a hospital by a doctor and the number of heartbeats per minute were recorded and summarised as follows. Find the mean heartbeats per minute for these women, choosing a suitable method.
> | Number of heartbeats per minute | 65 - 68 | 68 - 71 | 71 - 74 | 74 - 77 | 77 - 80 | 80 - 83 | 83 - 86 |
> | Number of women | 2 | 4 | 3 | 8 | 7 | 4 | 2 |

### C19 · Mean of Grouped Data, Q5
`objectives: O9` · Media: new image spec (statement only)
> In a retail market, fruit vendors were selling mangoes kept in packing boxes. These boxes contained varying number of mangoes. The following was the distribution of mangoes according to the number of boxes.
> | Number of mangoes | 50 - 52 | 53 - 55 | 56 - 58 | 59 - 61 | 62 - 64 |
> | Number of boxes | 15 | 110 | 135 | 115 | 25 |
> Find the mean number of mangoes kept in a packing box. Which method of finding the mean did you choose?

### C20 · Mean of Grouped Data, Q6
`objectives: O9` · Media: new image spec (statement only)
> The table below shows the daily expenditure on food of 25 households in a locality.
> | Daily expenditure (in ₹) | 100 - 150 | 150 - 200 | 200 - 250 | 250 - 300 | 300 - 350 |
> | Number of households | 4 | 5 | 12 | 2 | 2 |
> Find the mean daily expenditure on food by a suitable method.

### C21 · Mean of Grouped Data, Q7
`objectives: O9` · Media: new image spec (statement only)
> To find out the concentration of SO₂ in the air (in parts per million, i.e., ppm), the data was collected for 30 localities in a certain city and is presented below:
> | Concentration of SO₂ (in ppm) | Frequency |
> | 0.00 - 0.04 | 4 |
> | 0.04 - 0.08 | 9 |
> | 0.08 - 0.12 | 9 |
> | 0.12 - 0.16 | 2 |
> | 0.16 - 0.20 | 4 |
> | 0.20 - 0.24 | 2 |
> Find the mean concentration of SO₂ in the air.

### C22 · Mean of Grouped Data, Q8
`objectives: O9` · Media: new image spec (statement only)
> A class teacher has the following absentee record of 40 students of a class for the whole term. Find the mean number of days a student was absent.
> | Number of days | 0 - 6 | 6 - 10 | 10 - 14 | 14 - 20 | 20 - 28 | 28 - 38 | 38 - 40 |
> | Number of students | 11 | 10 | 7 | 4 | 4 | 3 | 1 |

### C23 · Mean of Grouped Data, Q9
`objectives: O9` · Media: new image spec (statement only)
> The following table gives the literacy rate (in percentage) of 35 cities. Find the mean literacy rate.
> | Literacy rate (in %) | 45 - 55 | 55 - 65 | 65 - 75 | 75 - 85 | 85 - 95 |
> | Number of cities | 3 | 10 | 11 | 8 | 3 |

---

# M2 · Mode of grouped data

## T5 · The Mode of Grouped Data

### C24 · The mode, recalled
`kind: teach` · `objectives: O11`
Media: new image spec "The Value That Occurs Most Often" — A row of bars of different heights, one for each observed value, with the number of times it occurred on the vertical axis. The tallest bar is highlighted in a bold colour and labelled mode, the value with the maximum frequency. A second small panel shows two bars of equal greatest height, labelled multimodal.

[textbook_text]
> Recall from Class IX, a mode is that value among the observations which occurs most often, that is, the value of the observation having the maximum frequency. Further, we discussed finding the mode of ungrouped data. Here, we shall discuss ways of obtaining a mode of grouped data. It is possible that more than one value may have the same maximum frequency. In such situations, the data is said to be multimodal. Though grouped data can also be multimodal, we shall restrict ourselves to problems having a single mode only.
>
> Let us first recall how we found the mode for ungrouped data through the following example.

*(Cleanup: the section heading was removed.)*

### C25 · The mode of a bowler's wickets
`kind: exercise (worked example)` · `objectives: O11`
Media: existing image "Mode of ungrouped data — frequency table from Example 4" (old T6 O1.E1)

[question]
> The wickets taken by a bowler in 10 cricket matches are as follows:
> 2  6  4  5  0  2  1  3  2  3
> Find the mode of the data.

[worked solution, from source]
> Let us form the frequency distribution table of the given data as follows:
> | Number of wickets | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
> | Number of matches | 1 | 1 | 3 | 2 | 1 | 1 | 1 |
>
> Clearly, 2 is the number of wickets taken by the bowler in the maximum number (i.e., 3) of matches. So, the mode of this data is 2.

### C26 · The modal class and the mode formula
`kind: teach` · `objectives: O12, O13`
Media: existing video "Ungrouped mode to modal class — the conceptual leap" (old T6 VID1)
No tool, so this concept has the method statement and a prediction only.

[textbook_text]
> In a grouped frequency distribution, it is not possible to determine the mode by looking at the frequencies. Here, we can only locate a class with the maximum frequency, called the modal class. The mode is a value inside the modal class, and is given by the formula:

[method_statement]
> Mode = l + ((f₁ – f₀) / (2f₁ – f₀ – f₂)) × h
> where l = lower limit of the modal class,
> h = size of the class interval (assuming all class sizes to be equal),
> f₁ = frequency of the modal class,
> f₀ = frequency of the class preceding the modal class,
> f₂ = frequency of the class succeeding the modal class.

[textbook_text]
> Let us consider the following examples to illustrate the use of this formula.

[predict] `[authored]`
> In a survey of family sizes, the modal class is 3 – 5 with frequency 8. The class before it has frequency 7 and the class after it has frequency 2. Is the mode nearer 3 or nearer 5? Commit to an answer, then work the next example to check.

---

## T6 · Examples: Mode of Grouped Data

### C27 · The modal family size
`kind: exercise (worked example)` · `objectives: O12`
Media: new image spec "Family Sizes in 20 Households" — A frequency table for a survey of 20 households with the family sizes 1-3, 3-5, 5-7, 7-9 and 9-11 and the number of families 7, 8, 2, 2 and 1. Beside the table, a small row of house icons with groups of people figures inside. No modal class or mode is marked.

[question]
> A survey conducted on 20 households in a locality by a group of students resulted in the following frequency table for the number of family members in a household:
> | Family size | 1 - 3 | 3 - 5 | 5 - 7 | 7 - 9 | 9 - 11 |
> | Number of families | 7 | 8 | 2 | 2 | 1 |
> Find the mode of this data.

[worked solution, from source]
> Here the maximum class frequency is 8, and the class corresponding to this frequency is 3 – 5. So, the modal class is 3 – 5.
> Now
> modal class = 3 – 5, lower limit (l) of modal class = 3, class size (h) = 2
> frequency (f₁) of the modal class = 8,
> frequency (f₀) of class preceding the modal class = 7,
> frequency (f₂) of class succeeding the modal class = 2.
> Now, let us substitute these values in the formula:
> Mode = l + ((f₁ – f₀) / (2f₁ – f₀ – f₂)) × h = 3 + ((8 – 7) / (2 × 8 – 7 – 2)) × 2 = 3 + 2/7 = 3.286
> Therefore, the mode of the data above is 3.286.

### C28 · The modal marks, compared with the mean
`kind: exercise (worked example)` · `objectives: O12, O13`
Media: existing video "Applying the mode formula — Example 5 and Example 6 walkthrough" (old T7 VID1); existing image "Mode formula dissected — labelled histogram for NCERT Example 6" (old T7 O2.E1). The video's first scene states the wrong data for the family-size example (see the content flags at the top), so it is placed here, on the example it gets right, and it must be fixed before use.

[question]
> The marks distribution of 30 students in a mathematics examination is given in the grouped table of the 30 students' marks used earlier. Find the mode of this data. Also compare and interpret the mode and the mean.

[worked solution, from source]
> Refer to the grouped table of the 30 students' marks. Since the maximum number of students (i.e., 7) have got marks in the interval 40 - 55, the modal class is 40 - 55. Therefore,
> the lower limit (l) of the modal class = 40,
> the class size (h) = 15,
> the frequency (f₁) of modal class = 7,
> the frequency (f₀) of the class preceding the modal class = 3,
> the frequency (f₂) of the class succeeding the modal class = 6.
> Now, using the formula: Mode = l + ((f₁ – f₀) / (2f₁ – f₀ – f₂)) × h,
> we get Mode = 40 + ((7 – 3) / (14 – 6 – 3)) × 15 = 52
> So, the mode marks is 52.
>
> Now, from the earlier calculation, you know that the mean marks is 62.
> So, the maximum number of students obtained 52 marks, while on an average a student obtained 62 marks.

[remark, from source]
> 1. Here, the mode is less than the mean. But for some other problems it may be equal or more than the mean also.
> 2. It depends upon the demand of the situation whether we are interested in finding the average marks obtained by the students or the average of the marks obtained by most of the students. In the first situation, the mean is required and in the second situation, the mode is required.

*(Cleanup: "Table 13.3 of Example 1" became "the grouped table of the 30 students' marks"; "from Example 1" became "from the earlier calculation"; "In Example 6" in Remark 1 became "Here".)*

### C29 · Class activity: the mode of your own data
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Finding the Mode of Class Data" — Three illustrated panels matching the marks, temperature and height groups, each showing a grouped frequency table with its class intervals and frequency bars. In each panel the class with the tallest bar is outlined and tagged modal class. A question mark beside each panel asks for the mode and how it compares with the mean.

[enrichment, from source]
> Continuing with the same groups as formed in the earlier class activity and the situations assigned to the groups, ask each group to find the mode of the data. They should also compare this with the mean, and interpret the meaning of both.

[enrichment, from source remark]
> The mode can also be calculated for grouped data with unequal class sizes. However, we shall not be discussing it.

*(Cleanup: the "Activity 3 :" label was removed and "as formed in Activity 2" became "as formed in the earlier class activity".)*

---

## T7 · Questions: Mode of Grouped Data

Objectives for this set: O14 (apply) find the mode of a grouped distribution by locating the modal class and applying the mode formula; O15 (evaluate) compare the mode and the mean and interpret what each says about the data.

Same rules as the mean questions: `attempt_first`, one new hint-free image spec each, no video, and steps and answer *to author*. The questions are in textbook order. None has lettered sub-parts, so each is one concept.

### C30 · Mode of Grouped Data, Q1
`objectives: O14, O15` · Media: new image spec (statement only)
> The following table shows the ages of the patients admitted in a hospital during a year:
> | Age (in years) | 5 - 15 | 15 - 25 | 25 - 35 | 35 - 45 | 45 - 55 | 55 - 65 |
> | Number of patients | 6 | 11 | 21 | 23 | 14 | 5 |
> Find the mode and the mean of the data given above. Compare and interpret the two measures of central tendency.

### C31 · Mode of Grouped Data, Q2
`objectives: O14` · Media: new image spec (statement only)
> The following data gives the information on the observed lifetimes (in hours) of 225 electrical components:
> | Lifetimes (in hours) | 0 - 20 | 20 - 40 | 40 - 60 | 60 - 80 | 80 - 100 | 100 - 120 |
> | Frequency | 10 | 35 | 52 | 61 | 38 | 29 |
> Determine the modal lifetimes of the components.

### C32 · Mode of Grouped Data, Q3
`objectives: O14` · Media: new image spec (statement only)
> The following data gives the distribution of total monthly household expenditure of 200 families of a village. Find the modal monthly expenditure of the families. Also, find the mean monthly expenditure:
> | Expenditure (in ₹) | Number of families |
> | 1000 - 1500 | 24 |
> | 1500 - 2000 | 40 |
> | 2000 - 2500 | 33 |
> | 2500 - 3000 | 28 |
> | 3000 - 3500 | 30 |
> | 3500 - 4000 | 22 |
> | 4000 - 4500 | 16 |
> | 4500 - 5000 | 7 |

### C33 · Mode of Grouped Data, Q4
`objectives: O14, O15` · Media: new image spec (statement only)
> The following distribution gives the state-wise teacher-student ratio in higher secondary schools of India. Find the mode and mean of this data. Interpret the two measures.
> | Number of students per teacher | Number of states / U.T. |
> | 15 - 20 | 3 |
> | 20 - 25 | 8 |
> | 25 - 30 | 9 |
> | 30 - 35 | 10 |
> | 35 - 40 | 3 |
> | 40 - 45 | 0 |
> | 45 - 50 | 0 |
> | 50 - 55 | 2 |

### C34 · Mode of Grouped Data, Q5
`objectives: O14` · Media: new image spec (statement only)
> The given distribution shows the number of runs scored by some top batsmen of the world in one-day international cricket matches.
> | Runs scored | Number of batsmen |
> | 3000 - 4000 | 4 |
> | 4000 - 5000 | 18 |
> | 5000 - 6000 | 9 |
> | 6000 - 7000 | 7 |
> | 7000 - 8000 | 6 |
> | 8000 - 9000 | 3 |
> | 9000 - 10000 | 1 |
> | 10000 - 11000 | 1 |
> Find the mode of the data.

### C35 · Mode of Grouped Data, Q6
`objectives: O14` · Media: new image spec (statement only)
> A student noted the number of cars passing through a spot on a road for 100 periods each of 3 minutes and summarised it in the table given below. Find the mode of the data:
> | Number of cars | 0 - 10 | 10 - 20 | 20 - 30 | 30 - 40 | 40 - 50 | 50 - 60 | 60 - 70 | 70 - 80 |
> | Frequency | 7 | 14 | 13 | 12 | 20 | 11 | 15 | 8 |

---

# M3 · Median of grouped data

## T8 · Cumulative Frequency

### C36 · The median of ungrouped data, from a running total
`kind: teach` · `objectives: O16`
Media: existing video "Odd-n versus even-n median — two worked examples side by side" (old T9 VID1); existing image "Ungrouped median via cumulative frequency — NCERT Table 13.11" (old T9 O1.E1)

[textbook_text]
> As you have studied in Class IX, the median is a measure of central tendency which gives the value of the middle-most observation in the data. Recall that for finding the median of ungrouped data, we first arrange the data values of the observations in ascending order. Then, if n is odd, the median is the ((n + 1)/2)th observation. And, if n is even, then the median will be the average of the (n/2)th and the ((n/2) + 1)th observations.
>
> Suppose, we have to find the median of the following data, which gives the marks, out of 50, obtained by 100 students in a test:
> | Marks obtained | 20 | 29 | 28 | 33 | 42 | 38 | 43 | 25 |
> | Number of students | 6 | 28 | 24 | 15 | 2 | 4 | 1 | 20 |
>
> First, we arrange the marks in ascending order and prepare a frequency table as follows:
> | Marks obtained | Number of students (Frequency) |
> | 20 | 6 |
> | 25 | 20 |
> | 28 | 24 |
> | 29 | 28 |
> | 33 | 15 |
> | 38 | 4 |
> | 42 | 2 |
> | 43 | 1 |
> | Total | 100 |
>
> Here n = 100, which is even. The median will be the average of the (n/2)th and the ((n/2) + 1)th observations, i.e., the 50th and 51st observations. To find these observations, we proceed as follows:
> | Marks obtained | Number of students |
> | 20 | 6 |
> | upto 25 | 6 + 20 = 26 |
> | upto 28 | 26 + 24 = 50 |
> | upto 29 | 50 + 28 = 78 |
> | upto 33 | 78 + 15 = 93 |
> | upto 38 | 93 + 4 = 97 |
> | upto 42 | 97 + 2 = 99 |
> | upto 43 | 99 + 1 = 100 |
>
> Now we add another column depicting this information to the frequency table above and name it as cumulative frequency column.
> | Marks obtained | Number of students | Cumulative frequency |
> | 20 | 6 | 6 |
> | 25 | 20 | 26 |
> | 28 | 24 | 50 |
> | 29 | 28 | 78 |
> | 33 | 15 | 93 |
> | 38 | 4 | 97 |
> | 42 | 2 | 99 |
> | 43 | 1 | 100 |
>
> From the table above, we see that:
> 50th observation is 28 (Why?)
> 51st observation is 29
> So, Median = (28 + 29)/2 = 28.5

[remark, from source]
> The part of the table above consisting of the first column and the third column is known as Cumulative Frequency Table. The median marks 28.5 conveys the information that about 50% students obtained marks less than 28.5 and another 50% students obtained marks more than 28.5.

*(Cleanup: the section heading was removed; "Table 13.11 consisting Column 1 and Column 3" became "the table above consisting of the first column and the third column". The "(Why?)" answer is in C39.)*

### C37 · Cumulative frequency of the less than type
`kind: teach` · `objectives: O17`
Media: existing video "Building a cumulative frequency column row by row" (old T10 VID1)

[textbook_text]
> Now, let us see how to obtain the median of grouped data, through the following situation.
>
> Consider a grouped frequency distribution of marks obtained, out of 100, by 53 students, in a certain examination, as follows:
> | Marks | Number of students |
> | 0 - 10 | 5 |
> | 10 - 20 | 3 |
> | 20 - 30 | 4 |
> | 30 - 40 | 3 |
> | 40 - 50 | 3 |
> | 50 - 60 | 4 |
> | 60 - 70 | 7 |
> | 70 - 80 | 9 |
> | 80 - 90 | 7 |
> | 90 - 100 | 8 |
>
> From the table above, try to answer the following questions:
> How many students have scored marks less than 10? The answer is clearly 5.
>
> How many students have scored less than 20 marks? Observe that the number of students who have scored less than 20 include the number of students who have scored marks from 0 - 10 as well as the number of students who have scored marks from 10 - 20. So, the total number of students with marks less than 20 is 5 + 3, i.e., 8. We say that the cumulative frequency of the class 10 - 20 is 8.
>
> Similarly, we can compute the cumulative frequencies of the other classes, i.e., the number of students with marks less than 30, less than 40, . . ., less than 100. We give them in the table below:
> | Marks obtained | Number of students (Cumulative frequency) |
> | Less than 10 | 5 |
> | Less than 20 | 5 + 3 = 8 |
> | Less than 30 | 8 + 4 = 12 |
> | Less than 40 | 12 + 3 = 15 |
> | Less than 50 | 15 + 3 = 18 |
> | Less than 60 | 18 + 4 = 22 |
> | Less than 70 | 22 + 7 = 29 |
> | Less than 80 | 29 + 9 = 38 |
> | Less than 90 | 38 + 7 = 45 |
> | Less than 100 | 45 + 8 = 53 |
>
> The distribution given above is called the cumulative frequency distribution of the less than type. Here 10, 20, 30, . . . 100, are the upper limits of the respective class intervals.

### C38 · Cumulative frequency of the more than or equal to type
`kind: teach` · `objectives: O17, O18`
Media: existing image "Less-than vs more-than-or-equal-to cumulative frequency — side by side" (old T10 O2.E1)

[textbook_text]
> We can similarly make the table for the number of students with scores, more than or equal to 0, more than or equal to 10, more than or equal to 20, and so on. From the table of the 53 students' marks, we observe that all 53 students have scored marks more than or equal to 0. Since there are 5 students scoring marks in the interval 0 - 10, this means that there are 53 – 5 = 48 students getting more than or equal to 10 marks. Continuing in the same manner, we get the number of students scoring 20 or above as 48 – 3 = 45, 30 or above as 45 – 4 = 41, and so on, as shown in the table below.
> | Marks obtained | Number of students (Cumulative frequency) |
> | More than or equal to 0 | 53 |
> | More than or equal to 10 | 53 – 5 = 48 |
> | More than or equal to 20 | 48 – 3 = 45 |
> | More than or equal to 30 | 45 – 4 = 41 |
> | More than or equal to 40 | 41 – 3 = 38 |
> | More than or equal to 50 | 38 – 3 = 35 |
> | More than or equal to 60 | 35 – 4 = 31 |
> | More than or equal to 70 | 31 – 7 = 24 |
> | More than or equal to 80 | 24 – 9 = 15 |
> | More than or equal to 90 | 15 – 7 = 8 |
>
> The table above is called a cumulative frequency distribution of the more than type. Here 0, 10, 20, . . ., 90 give the lower limits of the respective class intervals.
>
> Now, to find the median of grouped data, we can make use of any of these cumulative frequency distributions.

### C39 · More to explore: why the 50th observation is 28
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Where the 50th Observation Falls" — A cumulative frequency strip of the marks of 100 students, drawn as consecutive blocks along a line numbered 1 to 100. The blocks are positions 1 to 6 for marks 20, 7 to 26 for marks 25, 27 to 50 for marks 28, 51 to 78 for marks 29, 79 to 93 for marks 33, 94 to 97 for marks 38, 98 to 99 for marks 42 and 100 for marks 43. The 50th and 51st positions are marked with pins.

[enrichment] `[authored answer]`
> **Q.** In the table of 100 students' marks, why is the 50th observation 28, and the 51st observation 29?
> **A.** The cumulative frequency up to 25 is 26, and up to 28 it is 50. So the 27th to the 50th observations are all 28. The cumulative frequency up to 29 is 78, so the 51st to the 78th observations are all 29.

---

## T9 · The Median of Grouped Data

### C40 · The median class and the median formula
`kind: teach` · `objectives: O19`
Media: existing image "Median class identification — annotated NCERT Table 13.15" (old T11 O1.E1)
No tool, so this concept has the method statement and a prediction only.

[textbook_text]
> Let us combine the table of the 53 students' marks and its less than type cumulative frequency table to get the table given below:
> | Marks | Number of students (f) | Cumulative frequency (cf) |
> | 0 - 10 | 5 | 5 |
> | 10 - 20 | 3 | 8 |
> | 20 - 30 | 4 | 12 |
> | 30 - 40 | 3 | 15 |
> | 40 - 50 | 3 | 18 |
> | 50 - 60 | 4 | 22 |
> | 60 - 70 | 7 | 29 |
> | 70 - 80 | 9 | 38 |
> | 80 - 90 | 7 | 45 |
> | 90 - 100 | 8 | 53 |
>
> Now in a grouped data, we may not be able to find the middle observation by looking at the cumulative frequencies as the middle observation will be some value in a class interval. It is, therefore, necessary to find the value inside a class that divides the whole distribution into two halves. But which class should this be?
>
> To find this class, we find the cumulative frequencies of all the classes and n/2. We now locate the class whose cumulative frequency is greater than (and nearest to) n/2. This is called the median class. In the distribution above, n = 53. So, n/2 = 26.5. Now 60 – 70 is the class whose cumulative frequency 29 is greater than (and nearest to) n/2, i.e., 26.5.
>
> Therefore, 60 – 70 is the median class.
>
> After finding the median class, we use the following formula for calculating the median.

[method_statement]
> Median = l + ((n/2 – cf) / f) × h
> where l = lower limit of median class,
> n = number of observations,
> cf = cumulative frequency of class preceding the median class,
> f = frequency of median class,
> h = class size (assuming class size to be equal).

[predict] `[authored]`
> For these 53 students, the median class is 60 – 70. The class before it ends at a cumulative frequency of 22, the median class holds 7 students, and n/2 = 26.5. Is the median nearer 60 or nearer 70? Commit, then check in the next concept.

*(Cleanup: "Let us combine Tables 13.12 and 13.13 to get Table 13.15" became the plain description above.)*

### C41 · Using the median formula
`kind: teach` · `objectives: O19`
Media: new image spec "Reading Values for the Median Formula" — The cumulative frequency table of the 53 students' marks with the class 60-70 highlighted as the median class. Tags point to the lower limit l = 60, the class size h = 10, the frequency of the median class f = 7, and the cumulative frequency of the class just before it, cf = 22, with n = 53 and n/2 = 26.5 written beside the table. The median formula is shown with empty boxes in place of the numbers.

[textbook_text]
> Substituting the values n/2 = 26.5, l = 60, cf = 22, f = 7, h = 10 in the formula above, we get
> Median = 60 + ((26.5 – 22) / 7) × 10 = 60 + 45/7 = 66.4
>
> So, about half the students have scored marks less than 66.4, and the other half have scored marks more than 66.4.

---

## T10 · Examples: Median of Grouped Data

### C42 · The median height of 51 girls
`kind: exercise (worked example)` · `objectives: O19`
Media: new image spec "Heights of 51 Girls of Class X" — A less than type table titled heights in cm of 51 girls. The rows read less than 140 with 4, less than 145 with 11, less than 150 with 29, less than 155 with 40, less than 160 with 46 and less than 165 with 51. Beside the table, a row of girl figures of different heights stands against a measuring scale. No class frequencies or median are shown.

[question]
> A survey regarding the heights (in cm) of 51 girls of Class X of a school was conducted and the following data was obtained:
> | Height (in cm) | Number of girls |
> | Less than 140 | 4 |
> | Less than 145 | 11 |
> | Less than 150 | 29 |
> | Less than 155 | 40 |
> | Less than 160 | 46 |
> | Less than 165 | 51 |
> Find the median height.

[worked solution, from source]
> To calculate the median height, we need to find the class intervals and their corresponding frequencies.
>
> The given distribution being of the less than type, 140, 145, 150, . . ., 165 give the upper limits of the corresponding class intervals. So, the classes should be below 140, 140 - 145, 145 - 150, . . ., 160 - 165. Observe that from the given distribution, we find that there are 4 girls with height less than 140, i.e., the frequency of class interval below 140 is 4. Now, there are 11 girls with heights less than 145 and 4 girls with height less than 140. Therefore, the number of girls with height in the interval 140 - 145 is 11 – 4 = 7. Similarly, the frequency of 145 - 150 is 29 – 11 = 18, for 150 - 155, it is 40 – 29 = 11, and so on. So, our frequency distribution table with the given cumulative frequencies becomes:
> | Class intervals | Frequency | Cumulative frequency |
> | Below 140 | 4 | 4 |
> | 140 - 145 | 7 | 11 |
> | 145 - 150 | 18 | 29 |
> | 150 - 155 | 11 | 40 |
> | 155 - 160 | 6 | 46 |
> | 160 - 165 | 5 | 51 |
>
> Now n = 51. So, n/2 = 51/2 = 25.5. This observation lies in the class 145 - 150. Then,
> l (the lower limit) = 145,
> cf (the cumulative frequency of the class preceding 145 - 150) = 11,
> f (the frequency of the median class 145 - 150) = 18,
> h (the class size) = 5.
> Using the formula, Median = l + ((n/2 – cf) / f) × h, we have
> Median = 145 + ((25.5 – 11) / 18) × 5 = 145 + 72.5/18 = 149.03.
> So, the median height of the girls is 149.03 cm.
>
> This means that the height of about 50% of the girls is less than this height, and 50% are taller than this height.

### C43 · Finding missing frequencies from a given median
`kind: exercise (worked example)` · `objectives: O20`
Media: existing video "Solving NCERT Example 8 — finding missing frequencies with the median formula" (old T11 VID1)

[question]
> The median of the following data is 525. Find the values of x and y, if the total frequency is 100.
> | Class intervals | Frequency |
> | 0 - 100 | 2 |
> | 100 - 200 | 5 |
> | 200 - 300 | x |
> | 300 - 400 | 12 |
> | 400 - 500 | 17 |
> | 500 - 600 | 20 |
> | 600 - 700 | y |
> | 700 - 800 | 9 |
> | 800 - 900 | 7 |
> | 900 - 1000 | 4 |

[worked solution, from source]
> | Class intervals | Frequency | Cumulative frequency |
> | 0 - 100 | 2 | 2 |
> | 100 - 200 | 5 | 7 |
> | 200 - 300 | x | 7 + x |
> | 300 - 400 | 12 | 19 + x |
> | 400 - 500 | 17 | 36 + x |
> | 500 - 600 | 20 | 56 + x |
> | 600 - 700 | y | 56 + x + y |
> | 700 - 800 | 9 | 65 + x + y |
> | 800 - 900 | 7 | 72 + x + y |
> | 900 - 1000 | 4 | 76 + x + y |
>
> It is given that n = 100
> So, 76 + x + y = 100, i.e., x + y = 24  (1)
> The median is 525, which lies in the class 500 – 600
> So, l = 500, f = 20, cf = 36 + x, h = 100
> Using the formula: Median = l + ((n/2 – cf) / f) × h, we get
> 525 = 500 + ((50 – 36 – x) / 20) × 100
> i.e., 525 – 500 = (14 – x) × 5
> i.e., 25 = 70 – 5x
> i.e., 5x = 70 – 25 = 45
> So, x = 9
> Therefore, from (1), we get 9 + y = 24
> i.e., y = 15

---

## T11 · Choosing a Measure of Central Tendency

### C44 · Which measure suits which question?
`kind: teach` · `objectives: O21`
Media: existing image "Decision guide — choosing mean, median, or mode" (old T12 O1.E1)

[textbook_text]
> Now, that you have studied about all the three measures of central tendency, let us discuss which measure would be best suited for a particular requirement.
>
> The mean is the most frequently used measure of central tendency because it takes into account all the observations, and lies between the extremes, i.e., the largest and the smallest observations of the entire data. It also enables us to compare two or more distributions. For example, by comparing the average (mean) results of students of different schools of a particular examination, we can conclude which school has a better performance.
>
> However, extreme values in the data affect the mean. For example, the mean of classes having frequencies more or less the same is a good representative of the data. But, if one class has frequency, say 2, and the five others have frequency 20, 25, 20, 21, 18, then the mean will certainly not reflect the way the data behaves. So, in such cases, the mean is not a good representative of the data.
>
> In problems where individual observations are not important, and we wish to find out a 'typical' observation, the median is more appropriate, e.g., finding the typical productivity rate of workers, average wage in a country, etc. These are situations where extreme values may be there. So, rather than the mean, we take the median as a better measure of central tendency.
>
> In situations which require establishing the most frequent value or most popular item, the mode is the best choice, e.g., to find the most popular T.V. programme being watched, the consumer item in greatest demand, the colour of the vehicle used by most of the people, etc.

### C45 · How the three measures are related
`kind: teach` · `objectives: O22`
Media: existing video "3 Median ≈ Mode + 2 Mean — the empirical relation explained" (old T12 VID1)

[remark, from source]
> 1. There is an empirical relationship between the three measures of central tendency:
> 3 Median = Mode + 2 Mean
> 2. The median of grouped data with unequal class sizes can also be calculated. However, we shall not discuss it here.

*(Cleanup: "a empirical" became "an empirical".)*

---

## T12 · Questions: Median of Grouped Data

Objectives for this set: O23 (apply) find the median of a grouped distribution, including one given as a less than or below type cumulative distribution, and find missing frequencies from a given median; O24 (analyze) find the mean, median and mode of one distribution and compare them.

Same rules as before: `attempt_first`, one new hint-free image spec each, no video, and steps and answer *to author*. The questions are in textbook order. None has lettered sub-parts, so each is one concept. The fourth question has a book hint, which opens only after the attempt and is not on the image.

### C46 · Median of Grouped Data, Q1
`objectives: O24` · Media: new image spec (statement only)
> The following frequency distribution gives the monthly consumption of electricity of 68 consumers of a locality. Find the median, mean and mode of the data and compare them.
> | Monthly consumption (in units) | Number of consumers |
> | 65 - 85 | 4 |
> | 85 - 105 | 5 |
> | 105 - 125 | 13 |
> | 125 - 145 | 20 |
> | 145 - 165 | 14 |
> | 165 - 185 | 8 |
> | 185 - 205 | 4 |

### C47 · Median of Grouped Data, Q2
`objectives: O23` · Media: new image spec (statement only)
> If the median of the distribution given below is 28.5, find the values of x and y.
> | Class interval | Frequency |
> | 0 - 10 | 5 |
> | 10 - 20 | x |
> | 20 - 30 | 20 |
> | 30 - 40 | 15 |
> | 40 - 50 | y |
> | 50 - 60 | 5 |
> | Total | 60 |

### C48 · Median of Grouped Data, Q3
`objectives: O23` · Media: new image spec (statement only)
> A life insurance agent found the following data for distribution of ages of 100 policy holders. Calculate the median age, if policies are given only to persons having age 18 years onwards but less than 60 year.
> | Age (in years) | Number of policy holders |
> | Below 20 | 2 |
> | Below 25 | 6 |
> | Below 30 | 24 |
> | Below 35 | 45 |
> | Below 40 | 78 |
> | Below 45 | 89 |
> | Below 50 | 92 |
> | Below 55 | 98 |
> | Below 60 | 100 |

### C49 · Median of Grouped Data, Q4
`objectives: O23` · Media: new image spec (statement only)
> The lengths of 40 leaves of a plant are measured correct to the nearest millimetre, and the data obtained is represented in the following table:
> | Length (in mm) | Number of leaves |
> | 118 - 126 | 3 |
> | 127 - 135 | 5 |
> | 136 - 144 | 9 |
> | 145 - 153 | 12 |
> | 154 - 162 | 5 |
> | 163 - 171 | 4 |
> | 172 - 180 | 2 |
> Find the median length of the leaves.
> **Hint (shown only after the attempt):** The data needs to be converted to continuous classes for finding the median, since the formula assumes continuous classes. The classes then change to 117.5 - 126.5, 126.5 - 135.5, . . ., 171.5 - 180.5.

### C50 · Median of Grouped Data, Q5
`objectives: O23` · Media: new image spec (statement only)
> The following table gives the distribution of the life time of 400 neon lamps:
> | Life time (in hours) | Number of lamps |
> | 1500 - 2000 | 14 |
> | 2000 - 2500 | 56 |
> | 2500 - 3000 | 60 |
> | 3000 - 3500 | 86 |
> | 3500 - 4000 | 74 |
> | 4000 - 4500 | 62 |
> | 4500 - 5000 | 48 |
> Find the median life time of a lamp.

### C51 · Median of Grouped Data, Q6
`objectives: O24` · Media: new image spec (statement only)
> 100 surnames were randomly picked up from a local telephone directory and the frequency distribution of the number of letters in the English alphabets in the surnames was obtained as follows:
> | Number of letters | 1 - 4 | 4 - 7 | 7 - 10 | 10 - 13 | 13 - 16 | 16 - 19 |
> | Number of surnames | 6 | 30 | 40 | 16 | 4 | 4 |
> Determine the median number of letters in the surnames. Find the mean number of letters in the surnames? Also, find the modal size of the surnames.

### C52 · Median of Grouped Data, Q7
`objectives: O23` · Media: new image spec (statement only)
> The distribution below gives the weights of 30 students of a class. Find the median weight of the students.
> | Weight (in kg) | 40 - 45 | 45 - 50 | 50 - 55 | 55 - 60 | 60 - 65 | 65 - 70 | 70 - 75 |
> | Number of students | 2 | 3 | 8 | 6 | 6 | 3 | 2 |

---

# M4 · Wrap-up

## T13 · Chapter Summary

### C53 · Chapter summary
`kind: summary` · `objectives: none`
Media: existing image "Exercise 13.3 strategy card — mean-median-mode workflow" (old T13 O1.E1). It gives away the method for the median question set, so it is re-homed here, after the questions. It is renamed at build, since its title carries the book's exercise number.

[summary_points]
> In this chapter, you have studied the following points:
> 1. The mean for grouped data can be found by: (i) the direct method: x̄ = Σfᵢxᵢ / Σfᵢ; (ii) the assumed mean method: x̄ = a + Σfᵢdᵢ / Σfᵢ; (iii) the step deviation method: x̄ = a + (Σfᵢuᵢ / Σfᵢ) × h, with the assumption that the frequency of a class is centred at its mid-point, called its class mark.
> 2. The mode for grouped data can be found by using the formula: Mode = l + ((f₁ – f₀) / (2f₁ – f₀ – f₂)) × h, where symbols have their usual meanings.
> 3. The cumulative frequency of a class is the frequency obtained by adding the frequencies of all the classes preceding the given class.
> 4. The median for grouped data is formed by using the formula: Median = l + ((n/2 – cf) / f) × h, where symbols have their usual meanings.

*(Cleanup: the three mean methods, listed (i) to (iii) on separate lines in the book, are folded into point 1 so the builder keeps them as one point.)*

### C54 · A note on continuous classes
`kind: enrich` · `is_enrichment: true` · `objectives: none`
Media: new image spec "Classes Must Join Without Gaps" — Two histograms side by side. The left one has class intervals such as 10-19 and 20-29 with a visible gap between the bars, marked with a cross and labelled not continuous. The right one has intervals 10-20, 20-30 and 30-40 whose bars touch, with the upper limit of each class equal to the lower limit of the next, marked with a tick and labelled continuous.

[textbook_text · "A note to the reader"]
> For calculating mode and median for grouped data, it should be ensured that the class intervals are continuous before applying the formulae. Same condition also apply for construction of an ogive. Further, in case of ogives, the scale may not be the same on both the axes.

---

# Appendix A · Objectives

Format: ID · bloom level · wording · old objective(s) it carries. All 24 old objectives are kept in their old order. None is new.

| ID | Bloom | Objective | Old ID |
|---|---|---|---|
| O1 | remember | Recall the meaning of mean, median, and mode as the three measures of central tendency for ungrouped data. | T1.O1 |
| O2 | understand | Explain why grouped frequency distributions require new methods for computing measures of central tendency. | T1.O2 |
| O3 | apply | Compute the mean of grouped frequency data using class marks and the Direct Method formula x̄ = Σfᵢxᵢ / Σfᵢ. | T2.O1 |
| O4 | understand | Explain why the Direct Method assumes each class frequency is centred at its class mark. | T2.O2 |
| O5 | apply | Compute the mean of grouped data using the Assumed Mean Method x̄ = a + Σfᵢdᵢ / Σfᵢ where dᵢ = xᵢ − a. | T3.O1 |
| O6 | evaluate | Verify that the mean obtained from the Assumed Mean Method equals the Direct Method value, regardless of the choice of a. | T3.O2 |
| O7 | apply | Compute the mean of grouped data using the Step-Deviation Method x̄ = a + h(Σfᵢuᵢ / Σfᵢ) where uᵢ = (xᵢ − a)/h. | T4.O1 |
| O8 | analyze | Determine which of the three methods is most appropriate for a given grouped frequency distribution by analysing the size of xᵢ, fᵢ, and the class widths. | T4.O2 |
| O9 | apply | Solve grouped-data problems asking for the mean by selecting the most efficient among Direct, Assumed Mean, and Step-Deviation methods. | T5.O1 |
| O10 | analyze | Determine missing frequencies when a grouped distribution's mean is given, by setting up and solving an equation. | T5.O2 |
| O11 | apply | Identify the mode of an ungrouped data set as the value with the highest frequency, using a frequency table. | T6.O1 |
| O12 | apply | Compute the mode of a grouped frequency distribution using Mode = l + ((f₁ − f₀)/(2f₁ − f₀ − f₂)) × h, after correctly identifying the modal class. | T7.O1 |
| O13 | understand | Explain the meaning of each symbol (l, h, f₀, f₁, f₂) in the mode formula, and why the formula interpolates within the modal class rather than returning its class mark. | T7.O2 |
| O14 | apply | Solve grouped-data problems asking for the mode by identifying the modal class and applying the mode formula. | T8.O1 |
| O15 | evaluate | Justify comparisons between the computed mode and mean in terms of what each statistic represents about the data. | T8.O2 |
| O16 | apply | Compute the median of an ungrouped data set using the cumulative-frequency column, correctly handling both the odd-n and even-n cases. | T9.O1 |
| O17 | apply | Construct the less-than-type and more-than-or-equal-to-type cumulative frequency distributions from a grouped frequency table. | T10.O1 |
| O18 | analyze | Compare the two cumulative frequency distribution types and explain which class-limit (upper or lower) anchors each row of each table. | T10.O2 |
| O19 | apply | Compute the median of grouped frequency data by locating the median class from the cumulative-frequency column and applying Median = l + ((n/2 − cf)/f) × h. | T11.O1 |
| O20 | analyze | Determine missing class frequencies when the median is given, by combining the total-frequency condition with the median formula. | T11.O2 |
| O21 | analyze | Classify real-world situations by which measure of central tendency — mean, median, or mode — best answers the stated question, and justify the choice. | T12.O1 |
| O22 | evaluate | Verify the empirical relation 3 × Median ≈ Mode + 2 × Mean by applying it to worked-example distributions from this chapter. | T12.O2 |
| O23 | apply | Solve grouped-data problems asking for the median, including those whose input is given as a less-than-type or below-type cumulative distribution. | T13.O1 |
| O24 | analyze | Solve mixed problems that require finding mean, median, and mode for a single grouped distribution, and verify the empirical relation among the three. | T13.O2 |

Note: the old "x-bar" in O3, O5 and O7 is written x̄. No other wording changed.

# Appendix B · Held assets (not attached to the new plan; nothing deleted)

**Five old tools** (no tools in this chapter):
- T4 "Mean Methods Explorer (Direct / Assumed Mean / Step Deviation)" (T2D1)
- T7 "Modal Class Finder & Mode Calculator" (T2D1)
- T10 "Cumulative Frequency Table Builder" (T2D1)
- T10 "Ogive Constructor with Median-from-Graph" (T2D2). This reprint has no ogive section.
- T11 "Median Class Finder & Calculator" (T2D1)

**Old question videos**: none in the old plan.

**Two other old images, held because they give away a question's answer:**
- T5 "Exercise 13.1 Q3 solution — missing frequency f" (O2.E1). It is the full worked solution of the missing-frequency question. It can return as that question's post-attempt solution media.
- T8 "Modal-class identification — bar chart for Exercise 13.2 Q4" (O1.E1). It labels the modal class, f₀ and f₂ of the teacher-student question. It can return as that question's post-attempt hint media.

Identity: 21 attached + 5 tools + 2 images held = 28 old media.

# Appendix C · Old topic to new concepts

The first C-number in each row is the concept that takes the old topic's carried fields (`recall_questions`, `summary`, `key_terms`, `concept_bullets`, `detailed_summary`). Those fields are not shown here, to keep this file reviewable.

| Old topic | New concepts |
|---|---|
| T1 Recap of Measures of Central Tendency | C1, C2 |
| T2 Direct Method for Mean of Grouped Data | C2, C3, C4, C5 |
| T3 Assumed Mean Method | C6, C7, C8, C11 |
| T4 Step-Deviation Method for Mean | C9, C10, C12, C13, C14 |
| T5 Practice: Mean of Grouped Data | C15–C23 |
| T6 Mode of Ungrouped Data — Recap | C24, C25 |
| T7 Mode Formula for Grouped Data | C26, C27, C28, C29 |
| T8 Practice: Mode of Grouped Data | C30–C35 |
| T9 Median of Ungrouped Data — Recap | C36, C39 |
| T10 Cumulative Frequency Distribution | C37, C38 |
| T11 Median Formula for Grouped Data | C40, C41, C42, C43 |
| T12 Choosing Mean, Median, or Mode | C44, C45, C53, C54 |
| T13 Practice: Median of Grouped Data | C46–C52 |
