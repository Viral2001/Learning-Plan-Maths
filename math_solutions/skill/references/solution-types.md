# Types of maths solutions and how to present each

Classify the question first, then use the matching template. Several types can combine in one question (for example a calculation that needs a figure).

| # | Type | Typical wording | Figure? | Core of the write-up |
|---|------|-----------------|---------|----------------------|
| 1 | Numerical / calculation | "Find", "Calculate", "Determine" | Only if the book gives one | Named formula, substitution, simplification, answer with unit |
| 2 | Proof (derivation) | "Prove that", "Show that" | Usually, with construction lines dashed | Given / To prove / Construction / Step-Statement-Reason table |
| 3 | General derivation of a formula | "Derive", "Find a formula for" | Sometimes | Setup, symbols defined, algebra step by step, boxed result |
| 4 | MCQ with justification | Options (A)-(D) | Only if the book gives one | Work out the value, then say which option and why the others fail |
| 5 | Fill in the blank / one-word | "Fill in the blanks" | No | One block per blank, a one-line reason, then the word |
| 6 | Reading data from a figure | "In Fig. ..., find" | The book's figure, redrawn | Explicit setup step: axes, scale, labels; then compute |
| 7 | Construction | "Draw", "Construct" | Yes: the figure is the answer | Numbered steps, finished figure, reasoning that it meets the requirement |
| 8 | Word problem / modelling | A story with numbers | Optional | Translate to symbols first ("Let ... be ..."), solve, interpret in words |
| 9 | Verification / "check whether" | "Is it true that", "Show whether" | No | Compute both sides, compare, state the conclusion |

## 1. Numerical / calculation

```
Question.  (exact wording)
Solution.  1. Identify what is given and what is asked.
           2. State the named formula in general form.
           3. Substitute: show the values put in BEFORE squaring or multiplying,
              then simplify line by line (align the equals signs).
           4. Common mistake note (\slip) where a student is likely to slip.
           5. Verification: put the result back, with the values shown.
           [\ans{value and unit}]   <- highlighted box, closes the main solution; an "Alternative solution" block, if any, follows it
```
There is no separate "Answer." heading: solution and answer are one block. Include a verification when it is cheap (substitute back, or use a second route).

## 2. Proof

```
Solution.
Given:        what the question gives, in symbols.
To prove:     the statement to establish, in symbols.
Construction: only the extra lines drawn (omit if none).
Proof:        Step | Statement | Reason  (table)
(\slip)       the step students most often get wrong, if any
[\ans{the result restated in full. (Proved)}]
```
- Every Reason names the property in words, never just "by theorem".
- Cite earlier steps by number ("From steps 2 and 3").
- Give an alternative proof after the table when a second route exists (RHS vs Pythagoras, direct vs contradiction).
- The figure shows the given configuration plus dashed construction lines. It must not show the conclusion (equal-angle marks, right-angle marks that are the thing to prove).
- If a proof needs an assumption about the figure (a ray lying inside an angle), say so in the reason.

## 3. General derivation

State the setup and define every symbol. Write each algebraic step on its own line and name the rule used when it is not obvious (factorise, cross-multiply, square both sides). Finish with the boxed result and, where possible, a special-case check.

## 4. MCQ with justification

Solve as a numerical or proof question, then close with `\ans{}` giving the letter and the value: "Option (D): $PQ=\sqrt{119}$ cm." Show briefly why each other option fails, using a bound or a quick substitution, and say which wrong calculation leads to the tempting wrong option (for example adding instead of subtracting squares). Do not just match the value.

## 5. Fill in the blank

One sub-block per blank, labelled "Question 2 (i)", "(ii)". Each has a one-line reason (a definition or property), and its `\ans{}` box holds the missing word or number.

## 6. Reading data from a figure

Begin with a setup step tied to the figure, stating the interpretation ("Take columns along the x-axis and rows along the y-axis"). List the data read, for example the points with coordinates. Only then calculate. Flag the interpretation for the teacher to confirm.

## 7. Construction

```
Solution.  This is a construction question; the figure is the answer.
Steps of construction.  1. ... 2. ... (numbered, each one an action)
(finished figure, with the constructed objects labelled)
Reasoning.  Why the constructed objects satisfy the requirement.
[\ans{one line naming what was constructed.}]
```
Use the figure to show the finished construction. Keep the step list short enough that a student can follow it with ruler and compass.

## 8. Word problem

Start with "Let ..." statements that name the unknowns. Form the equation(s), solve, then reject any root that does not fit the situation (negative lengths, non-integer counts) and say why. End with `\ans{}` in words with units.

## 9. Verification

Compute each side separately, compare, and state "Hence ... is true / not true". Do not shortcut by saying the result is "obvious".

## Choosing a method

- If the textbook solution has a method, use it as the main method.
- Add an alternate method when it is genuinely different (similarity vs Pythagoras), not a re-wording.
- Add a verification by substitution or by a second route, and run the numbers in Python before writing them (see `SKILL.md`).
