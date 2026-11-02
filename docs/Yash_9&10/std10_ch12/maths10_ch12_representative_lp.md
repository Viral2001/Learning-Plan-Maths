# Representative learning plan: Class 10, Surface Areas and Volumes (maths10_ch12)

A review copy of the restructured plan, down to concept level. Content is shown in full. Media are only named and never embedded.

Source: `learning_plan_std10_chap12_version1.json`. Shape follows the Class 9 circles plan and the Class 10 coordinate geometry plan.

## Read this first

**Standing decisions**
- No tools in this chapter. The six old `2d_tool` items are held (Appendix B).
- No videos for exercise questions. Each question concept gets one hint-free image spec and no video. The two old exercise videos are held (Appendix B).
- Examples keep the existing videos and images that match them. No new example media is planned.
- No grouping inside the question topics. Each textbook question is its own concept, in textbook order, named "<set name>, Q<n>". No question in this chapter has lettered sub-parts, so there are 9 + 8 = 17 question concepts.
- The book has no theorem, derivation or proof in this chapter, and the old plan has none either. The two rules of the chapter (surface area counts only the exposed surfaces; volumes of joined solids add) are given in the book as plain explanation, so they are `teach` concepts. There is no try or prove concept and no theorem id.
- The old plan puts the bird-bath example in its second module. Here it stays with the other surface-area examples, where the book has it, so that all surface-area work sits in M1 and all volume work in M2. The topic order is otherwise the old plan's order.

**What a concept entry shows**
- `kind`: teach, hook, exercise or summary.
- `objectives`: objective IDs. Enrichment concepts have none.
- `media`: existing assets re-homed from the old plan, new asset specs, or none. The notation "old T<n> <suffix>" gives the old topic number and the tail of the old media id, e.g. VID1, O1.E1.
- `[block_kind]` tags are review labels only. They never reach the student.

**Text cleanup applied to everything below**
- "Fig. 12.x", "see Fig. 12.x" and "as shown in Fig. 12.x" are removed or turned into "shown here" / "the figure". The figure is carried by the image.
- The section headings "12.1 Introduction", "12.2 ...", "12.3 ..." and "12.4 Summary" are dropped.
- "Example n:" and "EXERCISE 12.x" labels are removed.
- Each exercise set opens in the book with "Unless stated otherwise, take π = 22/7." The answers depend on it, so this line is repeated at the head of every question in both sets, as a stem.
- All example and question text is taken from the old plan's `original_chunk`, which keeps π, primes and fractions that the book's own text layer loses.
- Book references stay only in metadata (`ncert_refs`), which is not shown here.

**Not shown as concept text**
- The old plan's coaching layers (HOOK, RECALL, WHY THIS STEP, STRATEGY, ERROR ALERT, GROUND IT, CHECK, the "translation template" and the "which-template guide" for the two exercise sets) are authored text, not the book's. They are not concept text here. They stay in the old topics' `modified_chunk`, which is carried over whole (Appendix C).

**Marked in the text**
- `[authored]` marks text that is not in the old plan or the book. In this chapter there is none in the concept text: no predictions (no try concepts), and the book has no "(Why?)" prompts.
- Question solutions (`steps` and `answer`) are not in the old plan. They are marked *to author* and nothing is invented here.

## Plan at a glance

| Module | Topic | Concepts |
|---|---|---|
| M1 Surface area of combined solids | T1 Solids Made of Solids (hook) | C1 |
| | T2 Surface Area of a Joined Solid | C2–C3 |
| | T3 Examples: Surface Area of Combined Solids | C4–C7 |
| | T4 Questions: Surface Area of Combined Solids | C8–C16 |
| M2 Volume of combined solids | T5 Volume of a Joined Solid | C17 |
| | T6 Examples: Volume of Combined Solids | C18–C20 |
| | T7 Questions: Volume of Combined Solids | C21–C28 |
| M3 Wrap-up | T8 Chapter Summary | C29 |

Totals: 29 concepts and 17 objectives. 17 question concepts (9 + 8) need a new image. 0 new videos.

---

# M1 · Surface area of combined solids

## T1 · Solids Made of Solids (hook)

### C1 · Everyday objects that are not one basic solid
`kind: hook` · `is_enrichment: true` · `objectives: none`
Media: existing video "A Photo Tour of Combined Solids in Indian Daily Life" (old T1 VID1); existing image "Basic Solids Revisited and Three Everyday Combinations" (old T1 O1.E1)

[textbook_text]
> From Class IX, you are familiar with some of the solids like cuboid, cone, cylinder, and sphere. You have also learnt how to find their surface areas and volumes.
>
> In our day-to-day life, we come across a number of solids made up of combinations of two or more of the basic solids as shown above.
>
> You must have seen a truck with a container fitted on its back, carrying oil or water from one place to another. Is it in the shape of any of the four basic solids mentioned above? You may guess that it is made of a cylinder with two hemispheres as its ends.
>
> Again, you may have seen an object like the one shown here. Can you name it? A test tube, right! You would have used one in your science laboratory. This tube is also a combination of a cylinder and a hemisphere. Similarly, while travelling, you may have seen some big and beautiful buildings or monuments made up of a combination of solids mentioned above.
>
> If for some reason you wanted to find the surface areas, or volumes, or capacities of such objects, how would you do it? We cannot classify these under any of the solids you have already studied. In this chapter, you will see how to find surface areas and volumes of such objects.

*(Cleanup: "(see Fig. 12.1)" and "(see Fig. 12.2)" are dropped, and "the one in Fig. 12.3" becomes "the one shown here". The section heading is dropped. No words dropped otherwise. The old introduction objective (decomposing everyday objects into basic solids) cannot sit on an enrichment hook, so it is anchored on the next concept, where the book breaks the container into its pieces.)*

---

## T2 · Surface Area of a Joined Solid

### C2 · Break it into pieces, then count only what shows
`kind: teach` · `objectives: O1, O2`
Media: existing video "Why the TSA Is Not the Sum of TSAs" (old T2 VID1); existing image "Decomposition of a Cylinder-Plus-Hemispheres Container" (old T2 O1.E1)

[textbook_text]
> Let us consider the container seen earlier. How do we find the surface area of such a solid? Now, whenever we come across a new problem, we first try to see, if we can break it down into smaller problems, we have earlier solved. We can see that this solid is made up of a cylinder with two hemispheres stuck at either end. It would look like what we have in the figure, after we put the pieces all together.
>
> If we consider the surface of the newly formed object, we would be able to see only the curved surfaces of the two hemispheres and the curved surface of the cylinder.
>
> So, the total surface area of the new solid is the sum of the curved surface areas of each of the individual parts. This gives,
> TSA of new solid = CSA of one hemisphere + CSA of cylinder + CSA of other hemisphere
> where TSA, CSA stand for 'Total Surface Area' and 'Curved Surface Area' respectively.

*(Cleanup: "the container seen in Fig. 12.2" becomes "the container seen earlier", and "what we have in Fig. 12.4" becomes "what we have in the figure".)*

### C3 · A round-bottomed toy: a cone on a hemisphere
`kind: teach` · `objectives: O3`
Media: new image spec "Building a Round-Bottomed Toy" — A three-step picture. Step one shows a cone and a hemisphere side by side, both with the same base radius r, with their flat circular faces turned towards each other. Step two shows the flat faces brought together. Step three shows the finished smooth round-bottomed toy, with the curved surface of the cone and the curved surface of the hemisphere shaded in two colours and labelled.

[textbook_text]
> Let us now consider another situation. Suppose we are making a toy by putting together a hemisphere and a cone. Let us see the steps that we would be going through.
>
> First, we would take a cone and a hemisphere and bring their flat faces together. Here, of course, we would take the base radius of the cone equal to the radius of the hemisphere, for the toy is to have a smooth surface. So, the steps would be as shown in the figure.
>
> At the end of our trial, we have got ourselves a nice round-bottomed toy. Now if we want to find how much paint we would require to colour the surface of this toy, what would we need to know? We would need to know the surface area of the toy, which consists of the CSA of the hemisphere and the CSA of the cone.
> So, we can say:
> Total surface area of the toy = CSA of hemisphere + CSA of cone
>
> Now, let us consider some examples.

*(Cleanup: "as shown in Fig. 12.5" becomes "as shown in the figure". The old plan has no image of the toy's assembly steps; the book's own figure of the three steps is a source figure. No new media is planned here; to be confirmed in review.)*

---

## T3 · Examples: Surface Area of Combined Solids

### C4 · Rasheed's top: the area to colour
`kind: exercise (worked example)` · `objectives: O4`
Media: existing video "Colour-Coded Walkthrough of Rasheed's Top" (old T3 VID1); existing image "Rasheed's Top with All Labelled Dimensions" (old T3 O1.E1)

[question]
> Rasheed got a playing top (lattu) as his birthday present, which surprisingly had no colour on it. He wanted to colour it with his crayons. The top is shaped like a cone surmounted by a hemisphere. The entire top is 5 cm in height and the diameter of the top is 3.5 cm. Find the area he has to colour. (Take π = 22/7)

[worked solution, from source]
> This top is exactly like the object we have discussed earlier. So, we can conveniently use the result we have arrived at there. That is :
> TSA of the toy = CSA of hemisphere + CSA of cone
> Now, the curved surface area of the hemisphere = ½ (4πr²) = 2πr²
> = 2 × (22/7) × (3.5/2) × (3.5/2) cm²
> Also, the height of the cone = height of the top – height (radius) of the hemispherical part
> = (5 – 3.5/2) cm = 3.25 cm
> So, the slant height of the cone (l) = √(r² + h²) = √((3.5/2)² + (3.25)²) cm = 3.7 cm (approx.)
> Therefore, CSA of cone = πrl = (22/7) × (3.5/2) × 3.7 cm²
> This gives the surface area of the top as
> = 2 × (22/7) × (3.5/2) × (3.5/2) cm² + (22/7) × (3.5/2) × 3.7 cm²
> = (22/7) × (3.5/2) × (3.5 + 3.7) cm²
> = (11/2) × (3.5 + 3.7) cm² = 39.6 cm² (approx.)

[remark, from source]
> You may note that 'total surface area of the top' is not the sum of the total surface areas of the cone and hemisphere.

*(Cleanup: "(see Fig 12.6)" is dropped, and "the object we have discussed in Fig. 12.5" becomes "the object we have discussed earlier".)*

### C5 · A cube with a hemisphere on top
`kind: exercise (worked example)` · `objectives: O5`
Media: existing video "Why the Net Change Is + pi*r^2 (Not + 2*pi*r^2)" (old T4 VID1); existing image "Decorative Block with Dimensions and Hidden Circle" (old T4 O1.E1)

[question]
> The decorative block shown here is made of two solids — a cube and a hemisphere. The base of the block is a cube with edge 5 cm, and the hemisphere fixed on the top has a diameter of 4.2 cm. Find the total surface area of the block. (Take π = 22/7)

[worked solution, from source]
> The total surface area of the cube = 6 × (edge)² = 6 × 5 × 5 cm² = 150 cm².
> Note that the part of the cube where the hemisphere is attached is not included in the surface area.
> So, the surface area of the block = TSA of cube – base area of hemisphere + CSA of hemisphere
> = 150 – πr² + 2πr² = (150 + πr²) cm²
> = 150 cm² + (22/7) × (4.2/2) × (4.2/2) cm²
> = (150 + 13.86) cm² = 163.86 cm².

*(Cleanup: "shown in Fig. 12.7" becomes "shown here".)*

### C6 · A toy rocket painted in two colours
`kind: exercise (worked example)` · `objectives: O6`
Media: existing video "Top-View and Side-View Walkthrough of the Rocket" (old T5 VID1); existing image "Wooden Rocket with Orange, Yellow, and Exposed-Ring Regions" (old T5 O1.E1)

[question]
> A wooden toy rocket is in the shape of a cone mounted on a cylinder, as shown in the figure. The height of the entire rocket is 26 cm, while the height of the conical part is 6 cm. The base of the conical portion has a diameter of 5 cm, while the base diameter of the cylindrical portion is 3 cm. If the conical portion is to be painted orange and the cylindrical portion yellow, find the area of the rocket painted with each of these colours. (Take π = 3.14)

[worked solution, from source]
> Denote radius of cone by r, slant height of cone by l, height of cone by h, radius of cylinder by r′ and height of cylinder by h′.
> Then r = 2.5 cm, h = 6 cm, r′ = 1.5 cm, h′ = 26 – 6 = 20 cm
> and l = √(r² + h²) = √(2.5² + 6²) cm = 6.5 cm
> Here, the conical portion has its circular base resting on the base of the cylinder, but the base of the cone is larger than the base of the cylinder. So, a part of the base of the cone (a ring) is to be painted.
> So, the area to be painted orange = CSA of the cone + base area of the cone – base area of the cylinder
> = πrl + πr² – π(r′)²
> = π[(2.5 × 6.5) + (2.5)² – (1.5)²] cm²
> = π[20.25] cm² = 3.14 × 20.25 cm²
> = 63.585 cm²
> Now, the area to be painted yellow = CSA of the cylinder + area of one base of the cylinder
> = 2πr′h′ + π(r′)²
> = πr′(2h′ + r′)
> = (3.14 × 1.5) (2 × 20 + 1.5) cm²
> = 4.71 × 41.5 cm²
> = 195.465 cm²

*(Cleanup: "as shown in Fig. 12.8" becomes "as shown in the figure".)*

### C7 · A bird-bath with a hollow at the top
`kind: exercise (worked example)` · `objectives: O7`
Media: existing video "Why the Cylinder Top Vanishes into the Scoop" (old T6 VID1); existing image "Bird-Bath with Depression and the Combined-Formula Label" (old T6 O1.E1)

[question]
> Mayank made a bird-bath for his garden in the shape of a cylinder with a hemispherical depression at one end. The height of the cylinder is 1.45 m and its radius is 30 cm. Find the total surface area of the bird-bath. (Take π = 22/7)

[worked solution, from source]
> Let h be height of the cylinder, and r the common radius of the cylinder and hemisphere. Then,
> the total surface area of the bird-bath = CSA of cylinder + CSA of hemisphere
> = 2πrh + 2πr² = 2πr(h + r)
> = 2 × (22/7) × 30 × (145 + 30) cm²
> = 33000 cm² = 3.3 m²

*(Cleanup: "(see Fig. 12.9)" is dropped.)*

---

## T4 · Questions: Surface Area of Combined Solids

Objectives for this set: O8 (apply) solve surface-area word problems on joined or hollowed combinations of basic solids; O9 (analyze) decide which component surfaces to add or subtract by reading the way the solids are joined, hollowed or left open.

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, statement only (or, for the two questions the book prints with a figure, the book's own figure only), no working and no answer. There is no video. Solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for all 9.
The questions are in textbook order. None has lettered sub-parts. Q4 (the greatest diameter, then the surface area) and Q7 (the canvas area, then its cost) each ask a second thing that builds on the first, so each stays one concept.
O8 is used by Q1, Q3, Q6, Q7. O9 is used by Q2, Q4, Q5, Q8, Q9 (inner surface, the largest dome that fits, a depression, a cavity, two scooped ends).

### C8 · Surface Area of Combined Solids, Q1
`objectives: O8` · Media: new image spec (statement only)
> Unless stated otherwise, take π = 22/7.
> 2 cubes each of volume 64 cm³ are joined end to end. Find the surface area of the resulting cuboid.

### C9 · Surface Area of Combined Solids, Q2
`objectives: O9` · Media: new image spec (statement only)
> Unless stated otherwise, take π = 22/7.
> A vessel is in the form of a hollow hemisphere mounted by a hollow cylinder. The diameter of the hemisphere is 14 cm and the total height of the vessel is 13 cm. Find the inner surface area of the vessel.

### C10 · Surface Area of Combined Solids, Q3
`objectives: O8` · Media: new image spec (statement only)
> Unless stated otherwise, take π = 22/7.
> A toy is in the form of a cone of radius 3.5 cm mounted on a hemisphere of same radius. The total height of the toy is 15.5 cm. Find the total surface area of the toy.

### C11 · Surface Area of Combined Solids, Q4
`objectives: O9` · Media: new image spec (statement only)
> Unless stated otherwise, take π = 22/7.
> A cubical block of side 7 cm is surmounted by a hemisphere. What is the greatest diameter the hemisphere can have? Find the surface area of the solid.

### C12 · Surface Area of Combined Solids, Q5
`objectives: O9` · Media: new image spec (statement only)
> Unless stated otherwise, take π = 22/7.
> A hemispherical depression is cut out from one face of a cubical wooden block such that the diameter l of the hemisphere is equal to the edge of the cube. Determine the surface area of the remaining solid.

### C13 · Surface Area of Combined Solids, Q6
`objectives: O8` · Media: new image spec (the book's own figure of the capsule only)
> Unless stated otherwise, take π = 22/7.
> A medicine capsule is in the shape of a cylinder with two hemispheres stuck to each of its ends. The length of the entire capsule is 14 mm and the diameter of the capsule is 5 mm. Find its surface area.

### C14 · Surface Area of Combined Solids, Q7
`objectives: O8` · Media: new image spec (statement only)
> Unless stated otherwise, take π = 22/7.
> A tent is in the shape of a cylinder surmounted by a conical top. If the height and diameter of the cylindrical part are 2.1 m and 4 m respectively, and the slant height of the top is 2.8 m, find the area of the canvas used for making the tent. Also, find the cost of the canvas of the tent at the rate of ₹ 500 per m². (Note that the base of the tent will not be covered with canvas.)

### C15 · Surface Area of Combined Solids, Q8
`objectives: O9` · Media: new image spec (statement only)
> Unless stated otherwise, take π = 22/7.
> From a solid cylinder whose height is 2.4 cm and diameter 1.4 cm, a conical cavity of the same height and same diameter is hollowed out. Find the total surface area of the remaining solid to the nearest cm².

### C16 · Surface Area of Combined Solids, Q9
`objectives: O9` · Media: new image spec (the book's own figure of the wooden article only)
> Unless stated otherwise, take π = 22/7.
> A wooden article was made by scooping out a hemisphere from each end of a solid cylinder, as shown in the figure. If the height of the cylinder is 10 cm, and its base is of radius 3.5 cm, find the total surface area of the article.

*(Cleanup: Q6 loses "(see Fig. 12.10)", and Q9's "as shown in Fig. 12.11" becomes "as shown in the figure".)*

---

# M2 · Volume of combined solids

## T5 · Volume of a Joined Solid

### C17 · Volumes simply add
`kind: teach` · `objectives: O10`
Media: existing video "The Brass Kalash - Volumes Just Add" (old T8 VID1); existing image "Surface Area vs Volume — Side-by-Side Comparison Chart" (old T8 O1.E1)

[textbook_text]
> In the previous section, we have discussed how to find the surface area of solids made up of a combination of two basic solids. Here, we shall see how to calculate their volumes. It may be noted that in calculating the surface area, we have not added the surface areas of the two constituents, because some part of the surface area disappeared in the process of joining them. However, this will not be the case when we calculate the volume. The volume of the solid formed by joining two basic solids will actually be the sum of the volumes of the constituents, as we see in the examples below.

*(Cleanup: the section heading is dropped. The video uses a brass kalash, which is not the book's object, but it shows exactly this rule. The fit is loose, please check.)*

---

## T6 · Examples: Volume of Combined Solids

### C18 · How much air is in the shed?
`kind: exercise (worked example)` · `objectives: O11`
Media: existing video "Filling the Shed with Air - Then Subtracting Machinery" (old T9 VID1); existing image "Industrial Shed — Cuboid Plus Half-Cylinder" (old T9 O1.E1)

[question]
> Shanta runs an industry in a shed which is in the shape of a cuboid surmounted by a half cylinder. If the base of the shed is of dimension 7 m × 15 m, and the height of the cuboidal portion is 8 m, find the volume of air that the shed can hold. Further, suppose the machinery in the shed occupies a total space of 300 m³, and there are 20 workers, each of whom occupy about 0.08 m³ space on an average. Then, how much air is in the shed? (Take π = 22/7)

[worked solution, from source]
> The volume of air inside the shed (when there are no people or machinery) is given by the volume of air inside the cuboid and inside the half cylinder, taken together.
> Now, the length, breadth and height of the cuboid are 15 m, 7 m and 8 m, respectively. Also, the diameter of the half cylinder is 7 m and its height is 15 m.
> So, the required volume = volume of the cuboid + ½ × volume of the cylinder
> = [15 × 7 × 8 + ½ × (22/7) × (7/2)² × 15] m³ = 1128.75 m³
> Next, the total space occupied by the machinery = 300 m³
> And the total space occupied by the workers = 20 × 0.08 m³ = 1.6 m³
> Therefore, the volume of the air, when there are machinery and workers
> = 1128.75 – (300.00 + 1.60) = 827.15 m³

*(Cleanup: "(see Fig. 12.12)" is dropped.)*

### C19 · A glass that holds less than it seems
`kind: exercise (worked example)` · `objectives: O12, O13`
Media: existing video "Why the Bump Costs You Juice" (old T10 VID1); existing image "Juice Glass with Hemispherical Bump — Apparent vs Actual" (old T10 O1.E1)

[question]
> A juice seller was serving his customers using glasses as shown in the figure. The inner diameter of the cylindrical glass was 5 cm, but the bottom of the glass had a hemispherical raised portion which reduced the capacity of the glass. If the height of a glass was 10 cm, find the apparent capacity of the glass and its actual capacity. (Use π = 3.14.)

[worked solution, from source]
> Since the inner diameter of the glass = 5 cm and height = 10 cm,
> the apparent capacity of the glass = πr²h
> = 3.14 × 2.5 × 2.5 × 10 cm³ = 196.25 cm³
> But the actual capacity of the glass is less by the volume of the hemisphere at the base of the glass.
> i.e., it is less by (2/3)πr³ = (2/3) × 3.14 × 2.5 × 2.5 × 2.5 cm³ = 32.71 cm³
> So, the actual capacity of the glass = apparent capacity of glass – volume of the hemisphere
> = (196.25 – 32.71) cm³
> = 163.54 cm³

*(Cleanup: "as shown in Fig. 12.13" becomes "as shown in the figure".)*

### C20 · A toy inside the cylinder that just holds it
`kind: exercise (worked example)` · `objectives: O14`
Media: existing video "Seeing the Empty Space Inside the Cylinder" (old T11 VID1); existing image "Hemisphere-Plus-Cone Toy Inside a Circumscribing Cylinder" (old T11 O1.E1)

[question]
> A solid toy is in the form of a hemisphere surmounted by a right circular cone. The height of the cone is 2 cm and the diameter of the base is 4 cm. Determine the volume of the toy. If a right circular cylinder circumscribes the toy, find the difference of the volumes of the cylinder and the toy. (Take π = 3.14)

[worked solution, from source]
> Let BPC be the hemisphere and ABC be the cone standing on the base of the hemisphere. The radius BO of the hemisphere (as well as of the cone) = ½ × 4 cm = 2 cm.
> So, volume of the toy = (2/3)πr³ + (1/3)πr²h
> = [(2/3) × 3.14 × (2)³ + (1/3) × 3.14 × (2)² × 2] cm³
> = 25.12 cm³
> Now, let the right circular cylinder EFGH circumscribe the given solid. The radius of the base of the right circular cylinder = HP = BO = 2 cm, and its height is
> EH = AO + OP = (2 + 2) cm = 4 cm
> So, the volume required = volume of the right circular cylinder – volume of the toy
> = (3.14 × 2² × 4 – 25.12) cm³
> = 25.12 cm³
> Hence, the required difference of the two volumes = 25.12 cm³.

*(Cleanup: "(see Fig. 12.14)" is dropped. The labels B, P, C, O, A, E, F, G, H come from the book's figure; the old image of the toy in its cylinder is expected to carry them, please check.)*

---

## T7 · Questions: Volume of Combined Solids

Objectives for this set: O15 (apply) solve volume word problems on combined and hollowed basic solids, first deciding whether each is an add, subtract, displace or verify task; O16 (evaluate) check a claimed volume against the sum of the component volumes.

Every concept below is an `exercise` with `attempt_first: true`. Each has one new image spec: hint-free, statement only (or, for the two questions the book prints with a figure, the book's own figure only), no working and no answer. There is no video. Solution and any later media open after the student has attempted the question.
Steps and answer are *to author* for all 8.
The questions are in textbook order. None has lettered sub-parts, so each is one concept.
O15 is used by Q1 to Q7. O16 is used by Q8.

### C21 · Volume of Combined Solids, Q1
`objectives: O15` · Media: new image spec (statement only)
> Unless stated otherwise, take π = 22/7.
> A solid is in the shape of a cone standing on a hemisphere with both their radii being equal to 1 cm and the height of the cone is equal to its radius. Find the volume of the solid in terms of π.

### C22 · Volume of Combined Solids, Q2
`objectives: O15` · Media: new image spec (statement only)
> Unless stated otherwise, take π = 22/7.
> Rachel, an engineering student, was asked to make a model shaped like a cylinder with two cones attached at its two ends by using a thin aluminium sheet. The diameter of the model is 3 cm and its length is 12 cm. If each cone has a height of 2 cm, find the volume of air contained in the model that Rachel made. (Assume the outer and inner dimensions of the model to be nearly the same.)

### C23 · Volume of Combined Solids, Q3
`objectives: O15` · Media: new image spec (the book's own figure of the gulab jamun only)
> Unless stated otherwise, take π = 22/7.
> A gulab jamun, contains sugar syrup up to about 30% of its volume. Find approximately how much syrup would be found in 45 gulab jamuns, each shaped like a cylinder with two hemispherical ends with length 5 cm and diameter 2.8 cm.

### C24 · Volume of Combined Solids, Q4
`objectives: O15` · Media: new image spec (the book's own figure of the pen stand only)
> Unless stated otherwise, take π = 22/7.
> A pen stand made of wood is in the shape of a cuboid with four conical depressions to hold pens. The dimensions of the cuboid are 15 cm by 10 cm by 3.5 cm. The radius of each of the depressions is 0.5 cm and the depth is 1.4 cm. Find the volume of wood in the entire stand.

### C25 · Volume of Combined Solids, Q5
`objectives: O15` · Media: new image spec (statement only)
> Unless stated otherwise, take π = 22/7.
> A vessel is in the form of an inverted cone. Its height is 8 cm and the radius of its top, which is open, is 5 cm. It is filled with water up to the brim. When lead shots, each of which is a sphere of radius 0.5 cm are dropped into the vessel, one-fourth of the water flows out. Find the number of lead shots dropped in the vessel.

### C26 · Volume of Combined Solids, Q6
`objectives: O15` · Media: new image spec (statement only)
> Unless stated otherwise, take π = 22/7.
> A solid iron pole consists of a cylinder of height 220 cm and base diameter 24 cm, which is surmounted by another cylinder of height 60 cm and radius 8 cm. Find the mass of the pole, given that 1 cm³ of iron has approximately 8g mass. (Use π = 3.14)

### C27 · Volume of Combined Solids, Q7
`objectives: O15` · Media: new image spec (statement only)
> Unless stated otherwise, take π = 22/7.
> A solid consisting of a right circular cone of height 120 cm and radius 60 cm standing on a hemisphere of radius 60 cm is placed upright in a right circular cylinder full of water such that it touches the bottom. Find the volume of water left in the cylinder, if the radius of the cylinder is 60 cm and its height is 180 cm.

### C28 · Volume of Combined Solids, Q8
`objectives: O16` · Media: new image spec (statement only)
> Unless stated otherwise, take π = 22/7.
> A spherical glass vessel has a cylindrical neck 8 cm long, 2 cm in diameter; the diameter of the spherical part is 8.5 cm. By measuring the amount of water it holds, a child finds its volume to be 345 cm³. Check whether she is correct, taking the above as the inside measurements, and π = 3.14.

*(Cleanup: Q3 loses "(see Fig. 12.15)" and Q4 loses "(see Fig. 12.16)".)*

---

# M3 · Wrap-up

## T8 · Chapter Summary

### C29 · Chapter summary
`kind: summary` · `objectives: O17`
Media: existing video "Sixty-Second Recap of the Chapter" (old T13 VID1); existing image "Combined-Solid Strategies — Chapter Summary Chart" (old T13 O1.E1)

[summary_points]
> In this chapter, you have studied the following points:
> 1. To determine the surface area of an object formed by combining any two of the basic solids, namely, cuboid, cone, cylinder, sphere and hemisphere.
> 2. To find the volume of objects formed by combining any two of a cuboid, cone, cylinder, sphere and hemisphere.

*(Cleanup: the heading "12.4 Summary" is dropped.)*

---

# Appendix A · Objectives

Format: ID · bloom level · wording · old objective(s) it carries.

| ID | Bloom | Objective | Old ID |
|---|---|---|---|
| O1 | understand | Explain how everyday objects can be decomposed into combinations of basic solids such as cuboid, cone, cylinder, sphere, and hemisphere. | T1.O1 |
| O2 | understand | Explain why the total surface area of a combined solid is the sum of the exposed curved or flat surfaces of each component. | T2.O1 |
| O3 | analyze | Determine which faces are hidden when two basic solids are joined along a matching circular or flat region. | T2.O2 |
| O4 | apply | Compute the area to be coloured on a cone-plus-hemisphere toy using CSA formulas and the Pythagorean slant-height relation. | T3.O1 |
| O5 | apply | Calculate the surface area of a cube surmounted by a hemisphere by adjusting the cube TSA for the hemisphere base circle. | T4.O1 |
| O6 | apply | Solve for the separately painted areas of a cylinder-mounted cone when the two components have unequal base radii. | T5.O1 |
| O7 | apply | Compute the total surface area of a cylinder with a hemispherical depression using the combined formula 2πr(h + r). | T6.O1 |
| O8 | apply | Solve surface-area word problems on joined or hollowed combinations of basic solids. | T7.O1 |
| O9 | analyze | Determine which component surfaces to add or subtract by interpreting the geometric configuration in each problem. | T7.O2 |
| O10 | understand | Explain why the volume of a combined solid is the simple sum of its component volumes, unlike surface area. | T8.O1 |
| O11 | apply | Calculate the air volume inside a cuboid-plus-half-cylinder shed and account for space occupied by machinery and workers. | T9.O1 |
| O12 | apply | Compute the actual capacity of a cylindrical glass with a hemispherical raised bottom by subtracting the hemisphere volume. | T10.O1 |
| O13 | analyze | Distinguish between the apparent and actual capacity of a hollow solid whose interior is partially displaced. | T10.O2 |
| O14 | apply | Compute the volume of a hemisphere-plus-cone toy and the volume of its circumscribing cylinder, then find their difference using (2/3)πr³, (1/3)πr²h, and πr²H. | T11.O1 |
| O15 | apply | Solve volume word problems on combined and hollowed basic solids by classifying each as an add, subtract, displace, or verify task. | T12.O1 |
| O16 | evaluate | Verify a claimed volume, such as a measured capacity of a vessel, by computing the component-sum and comparing. | T12.O2 |
| O17 | understand | Explain the two governing principles for combined solids: volume is strictly additive, and surface area sums only exposed component surfaces. | T13.O1 |

Note: all 17 old objectives are kept, in the old order, and no new objective is authored. Three old wordings carried book references and are trimmed only to remove them: T7.O1 loses "from Exercise 12.1", T12.O1 loses "from Exercise 12.2", and T12.O2's "(e.g., the 345 cm³ spherical-vessel claim in Q8)" becomes "such as a measured capacity of a vessel". The old T1.O1 is anchored on C2 (the container broken into pieces), because the hook that holds the introduction is enrichment.

# Appendix B · Held assets (not attached to the new plan; nothing deleted)

**Six old tools** (no tools in this chapter):
- T1 "Solid Combination Builder" (T2D1)
- T2 "Surface Area Decomposer" (T2D1)
- T8 "Combined Solids Volume Calculator (ice cream / capsule)" (T2D1)
- T9 "Cuboid ↔ Cube Volume Transformation" (T2D1)
- T11 "Frustum Visualizer" (T2D1). Frustums are not in this edition of the chapter, so this tool would not fit even if tools were allowed.
- T12 "Word-Problem Library (combined solids)" (T2D1)

**Two old question videos** (no question videos for now):
- T7 "The Translation Template Applied to Q1" (VID1)
- T12 "Verifying Q8 - Does the Spherical Vessel Really Hold 345 cm^3?" (VID1)

**Two old question images** (each is drawn for one exercise question and labels the method on the picture, so it would give the method away; a question concept also takes exactly one hint-free image, the new spec):
- T7 "Wedding Shamiana — The Tent of Exercise 12.1 Q7" (O1.E1): labels the wall 2πrh, the roof πrl and the ground "no canvas". Its title also carries the book's exercise number.
- T12 "Wooden Pen Stand with Four Conical Depressions" (O1.E1): labels "– 4 × (1/3)πr²h" and "volume of wood = cuboid – cones".

Media identity: 32 old media = 22 attached (11 videos + 11 images) + 10 held (6 tools + 2 question videos + 2 question images).

# Appendix C · Carried-over fields

Every old topic's `recall_questions`, `summary`, `key_terms`, `concept_bullets`, `detailed_summary` and `modified_chunk` carry into the new topic that holds its text. They are not shown here, to keep this file reviewable. The nothing-deleted check at build time compares them field by field.

Where each old topic's text and fields land:

| Old topic | New concepts |
|---|---|
| T1 Introduction to combinations of basic solids | C1 (and its objective on C2) |
| T2 Strategy: TSA as sum of exposed surfaces | C2, C3 |
| T3 Rasheed's top | C4 |
| T4 Decorative block | C5 |
| T5 Wooden rocket | C6 |
| T6 Bird-bath | C7 |
| T7 First exercise set (surface area) | C8–C16 |
| T8 The volume-additivity principle | C17 |
| T9 Industrial shed | C18 |
| T10 Juice glass | C19 |
| T11 Toy in a circumscribing cylinder | C20 |
| T12 Second exercise set (volume) | C21–C28 |
| T13 Summary | C29 |

The old summary topic T13 lists every earlier topic as a source; its own text and fields land in C29.
