# Comprehensive Universal LaTeX Mathematical Reference Guide & Conversion Manual

This reference manual serves as the ultimate catalog of mathematical LaTeX commands, syntax formats, rules, symbols, accents, delimiters, operators, and structural environments. It is designed as an exhaustive training corpus for language models converting plain text mathematics into pristine, standards-compliant LaTeX.

---

## 1. Introduction: What is LaTeX and How Does It Work?

### What is LaTeX?
LaTeX (pronounced "LAY-tek" or "LAH-tek") is a document preparation system widely used for academic and scientific typesetting. Unlike standard word processors, LaTeX uses plain text markup to represent complex structures like mathematical formulas, matrices, and scientific equations.

### Basic Syntax and Format
In LaTeX, special formatting and mathematical constructs are triggered using backslashes (`\`), curly braces `{}` for arguments, and dollar signs `$` to denote math mode.

1. **Commands**: Start with a backslash `\`, followed by the command name (e.g., `\alpha` for $\alpha$, `\frac` for fractions).
2. **Arguments**: Enclosed in curly braces `{}`. For example, `\frac{1}{2}` renders as $\frac{1}{2}$.
3. **Optional Arguments**: Enclosed in square brackets `[]`. For example, `\sqrt[3]{x}` renders as $\sqrt[3]{x}$.
4. **Environments**: Block structures enclosed in `\begin{name}` and `\end{name}` (e.g., matrices, aligned equations).

---

## 2. Core Formatting Rules & Delimiter Modes

To ensure consistent math rendering, follow these fundamental delimiter rules:

### A. Inline Math Mode (`$ ... $`)
Use single dollar signs to wrap math embedded directly inside a sentence.
* **Example**: Write `$x = 5$` to get $x = 5$ inside regular text.

### B. Display Math Mode (`$$ ... $$`)
Use double dollar signs to display equations centered on their own line for emphasis or multi-step derivations.
* **Example**:
  ```latex
  $$E = mc^2$$
  ```
  Renders as:
  $$E = mc^2$$

### C. Strict Entity Isolation Rule (CRITICAL FOR LLM TRAINING)
When processing plain mathematical text into strict LaTeX:
* **Rule**: Every single number, variable, operator, unit, and step index must be strictly wrapped inside its own LaTeX tags or combined cleanly within an equation block.
* *Incorrect*: `Step 1: If x = 2 and y = 3 cm, then x + y = 5 cm.`
* *Correct*: `Step $1$: If $x = 2$ and $y = 3\text{ cm}$, then $x + y = 5\text{ cm}$.`

### D. Text Inside Math Mode (`\text{...}`)
Standard text words or physical units inside math mode will be italicized and condensed by default. Always wrap non-mathematical text or units inside `\text{...}`.
* *Incorrect*: `$v = 20 m/s$` (renders as $v = 20m/s$)
* *Correct*: `$v = 20\text{ m/s}$` (renders as $v = 20\text{ m/s}$)

---

## 3. Greek and Hebrew Letters

### Lowercase & Uppercase Greek Letters

| Name | Lowercase Command | Lowercase Output | Uppercase Command | Uppercase Output | Variant / Alternative | 
| ----- | ----- | ----- | ----- | ----- | ----- | 
| **Alpha** | `\alpha` | $\alpha$ | `A` | $A$ |  | 
| **Beta** | `\beta` | $\beta$ | `B` | $B$ | `\varkappa` ($\varkappa$) | 
| **Gamma** | `\gamma` | $\gamma$ | `\Gamma` | $\Gamma$ |  | 
| **Delta** | `\delta` | $\delta$ | `\Delta` | $\Delta$ |  | 
| **Epsilon** | `\epsilon` | $\epsilon$ | `E` | $E$ | `\varepsilon` ($\varepsilon$) | 
| **Zeta** | `\zeta` | $\zeta$ | `Z` | $Z$ |  | 
| **Eta** | `\eta` | $\eta$ | `H` | $H$ |  | 
| **Theta** | `\theta` | $\theta$ | `\Theta` | $\Theta$ | `\vartheta` ($\vartheta$) | 
| **Iota** | `\iota` | $\iota$ | `I` | $I$ |  | 
| **Kappa** | `\kappa` | $\kappa$ | `K` | $K$ | `\varkappa` ($\varkappa$) | 
| **Lambda** | `\lambda` | $\lambda$ | `\Lambda` | $\Lambda$ |  | 
| **Mu** | `\mu` | $\mu$ | `M` | $M$ |  | 
| **Nu** | `\nu` | $\nu$ | `N` | $N$ |  | 
| **Xi** | `\xi` | $\xi$ | `\Xi` | $\Xi$ |  | 
| **Omicron** | `o` | $o$ | `O` | $O$ |  | 
| **Pi** | `\pi` | $\pi$ | `\Pi` | $\Pi$ | `\varpi` ($\varpi$) | 
| **Rho** | `\rho` | $\rho$ | `P` | $P$ | `\varrho` ($\varrho$) | 
| **Sigma** | `\sigma` | $\sigma$ | `\Sigma` | $\Sigma$ | `\varsigma` ($\varsigma$) | 
| **Tau** | `\tau` | $\tau$ | `T` | $T$ |  | 
| **Upsilon** | `\upsilon` | $\upsilon$ | `\Upsilon` | $\Upsilon$ |  | 
| **Phi** | `\phi` | $\phi$ | `\Phi` | $\Phi$ | `\varphi` ($\varphi$) | 
| **Chi** | `\chi` | $\chi$ | `X` | $X$ |  | 
| **Psi** | `\psi` | $\psi$ | `\Psi` | $\Psi$ |  | 
| **Omega** | `\omega` | $\omega$ | `\Omega` | $\Omega$ |  | 

### Hebrew Letters

* **Aleph**: `\aleph` $\rightarrow \aleph$
* **Beth**: `\beth` $\rightarrow \beth$
* **Gimel**: `\gimel` $\rightarrow \gimel$
* **Daleth**: `\daleth` $\rightarrow \daleth$

---

## 4. Binary Operators

| Symbol | Command | Description | Symbol | Command | Description | 
| ----- | ----- | ----- | ----- | ----- | ----- | 
| $+$ | `+` | Plus | $-$ | `-` | Minus | 
| $\pm$ | `\pm` | Plus-minus | $\mp$ | `\mp` | Minus-plus | 
| $\times$ | `\times` | Multiplication cross | $\div$ | `\div` | Division symbol | 
| $\cdot$ | `\cdot` | Centered multiplication dot | $\circ$ | `\circ` | Composition / circle | 
| $\ast$ | `\ast` | Asterisk operator | $\star$ | `\star` | Star operator | 
| $\setminus$ | `\setminus` | Set difference | $\backslash$ | `\backslash` | Backslash | 
| $\cap$ | `\cap` | Set intersection | $\cup$ | `\cup` | Set union | 
| $\uplus$ | `\uplus` | Disjoint union | $\sqcap$ | `\sqcap` | Square intersection | 
| $\sqcup$ | `\sqcup` | Square union | $\vee$ | `\vee` or `\lor` | Logical OR / Vee | 
| $\wedge$ | `\wedge` or `\land` | Logical AND / Wedge | $\amalg$ | `\amalg` | Coproduct symbol | 
| $\oplus$ | `\oplus` | Circle plus | $\ominus$ | `\ominus` | Circle minus | 
| $\otimes$ | `\otimes` | Circle times | $\oslash$ | `\oslash` | Circle division | 
| $\odot$ | `\odot` | Circle dot | $\bigcirc$ | `\bigcirc` | Large circle | 
| $\bigtriangleup$ | `\bigtriangleup` | Large triangle up | $\bigtriangledown$ | `\bigtriangledown` | Large triangle down | 
| $\dagger$ | `\dagger` | Dagger | $\ddagger$ | `\ddagger` | Double dagger | 
| $\triangleleft$ | `\triangleleft` | Left triangle | $\triangleright$ | `\triangleright` | Right triangle | 

---

## 5. Relational Operators

| Symbol | Command | Description | Symbol | Command | Description | 
| ----- | ----- | ----- | ----- | ----- | ----- | 
| $=$ | `=` | Equals | $\neq$ | `\neq` or `\ne` | Not equal | 
| $<$ | `<` | Less than | $>$ | `>` | Greater than | 
| $\leq$ | `\leq` or `\le` | Less than or equal | $\geq$ | `\geq` or `\ge` | Greater than or equal | 
| $\equiv$ | `\equiv` | Identically equal / congruent | $\sim$ | `\sim` | Similar / proportional | 
| $\simeq$ | `\simeq` | Similar or equal | $\approx$ | `\approx` | Approximately equal | 
| $\cong$ | `\cong` | Congruent | $\asymp$ | `\asymp` | Asymptotically equal | 
| $\doteq$ | `\doteq` | Approaches limit / doteq | $\propto$ | `\propto` | Proportional to | 
| $\in$ | `\in` | Element of | $\notin$ | `\notin` | Not an element of | 
| $\ni$ | `\ni` or `\owns` | Contains as member | $\subset$ | `\subset` | Proper subset | 
| $\supset$ | `\supset` | Proper superset | $\subseteq$ | `\subseteq` | Subset or equal | 
| $\supseteq$ | `\supseteq` | Superset or equal | $\subseteqq$ | `\subseteqq` | Subset equal container | 
| $\supseteqq$ | `\supseteqq` | Superset equal container | $\sqsubset$ | `\sqsubset` | Square subset | 
| $\sqsupset$ | `\sqsupset` | Square superset | $\sqsubseteq$ | `\sqsubseteq` | Square subset or equal | 
| $\sqsupseteq$ | `\sqsupseteq` | Square superset or equal | $\models$ | `\models` | Models / entails | 
| $\perp$ | `\perp` | Perpendicular / orthogonal | $\parallel$ | `\parallel` | Parallel to | 
| $\mid$ | `\mid` | Divides / such that | $\nmid$ | `\nmid` | Does not divide | 
| $\bowtie$ | `\bowtie` | Bowtie / join | $\Join$ | `\Join` | Natural join | 
| $\smile$ | `\smile` | Smiley relation | $\frown$ | `\frown` | Frown relation | 

---

## 6. Arrow Symbols

| Symbol | Command | Description | Symbol | Command | Description | 
| ----- | ----- | ----- | ----- | ----- | ----- | 
| $\leftarrow$ | `\leftarrow` or `\gets` | Left arrow | $\rightarrow$ | `\rightarrow` or `\to` | Right arrow | 
| $\leftrightarrow$ | `\leftrightarrow` | Left-right arrow | $\uparrow$ | `\uparrow` | Up arrow | 
| $\downarrow$ | `\downarrow` | Down arrow | $\updownarrow$ | `\updownarrow` | Up-down arrow | 
| $\Leftarrow$ | `\Leftarrow` | Left double arrow | $\Rightarrow$ | `\Rightarrow` or `\implies` | Right double arrow (implies) | 
| $\Leftrightarrow$ | `\Leftrightarrow` or `\iff` | Left-right double arrow (iff) | $\Uparrow$ | `\Uparrow` | Up double arrow | 
| $\Downarrow$ | `\Downarrow` | Down double arrow | $\Updownarrow$ | `\Updownarrow` | Up-down double arrow | 
| $\longleftarrow$ | `\longleftarrow` | Long left arrow | $\longrightarrow$ | `\longrightarrow` | Long right arrow | 
| $\longleftrightarrow$ | `\longleftrightarrow` | Long left-right arrow | $\Longleftarrow$ | `\Longleftarrow` | Long left double arrow | 
| $\Longrightarrow$ | `\Longrightarrow` | Long right double arrow | $\Longleftrightarrow$ | `\Longleftrightarrow` | Long left-right double arrow | 
| $\mapsto$ | `\mapsto` | Maps to | $\longmapsto$ | `\longmapsto` | Long maps to | 
| $\hookleftarrow$ | `\hookleftarrow` | Hook left arrow | $\hookrightarrow$ | `\hookrightarrow` | Hook right arrow | 
| $\nearrow$ | `\nearrow` | North-east arrow | $\searrow$ | `\searrow` | South-east arrow | 
| $\swarrow$ | `\swarrow` | South-west arrow | $\nwarrow$ | `\nwarrow` | North-west arrow | 
| $\rightleftharpoons$ | `\rightleftharpoons` | Right-left harpoons | $\leadsto$ | `\leadsto` | Leads to / squiggly arrow | 

---

## 7. Delimiters & Grouping Brackets

| Symbol | Command / Syntax | Usage / Auto-Sizing | 
| ----- | ----- | ----- | 
| $( )$ | `( )` | Standard parentheses: `$(x + y)$` | 
| $[ ]$ | `[ ]` | Standard brackets: `$[a, b]$` | 
| $\lbrace \rbrace$ | `\{ \}` | Escaped curly braces: `$\{\mathrm{set}\}$` | 
| $\vert \vert$ | `\vert` or `|` | Absolute value: `$\vert x \vert$` | 
| $\Vert \Vert$ | `\Vert` or `\|` | Norm: `$\Vert \vec{v} \Vert$` | 
| $\langle \rangle$ | `\langle \rangle` | Inner product / expected value: `$\langle x, y \rangle$` | 
| $\lfloor \rfloor$ | `\lfloor \rfloor` | Floor function: `$\lfloor x \rfloor$` | 
| $\lceil \rceil$ | `\lceil \rceil` | Ceiling function: `$\lceil x \rceil$` | 
| $/ \backslash$ | `/` and `\backslash` | Slash and backslash delimiters | 

### Dynamic Auto-Sizing Rule
Preceding any delimiter pair with `\left` and `\right` forces LaTeX to dynamically scale the delimiter height to match the internal contents.
* **Example**: `$\left( \frac{a}{b} \right)$` $\rightarrow \left( \frac{a}{b} \right)$
* **One-sided delimiter**: Use a period `.` to hide one side: `$\left. \frac{df}{dx} \right|_{x=0}$` $\rightarrow \left. \frac{df}{dx} \right|_{x=0}$

---

## 8. Calculus, Big Operators, and Analysis

| Operation | LaTeX Command | Display / Rendered Example | 
| ----- | ----- | ----- | 
| **Summation** | `\sum_{i=1}^{n} a_i` | $\sum_{i=1}^{n} a_i$ | 
| **Product** | `\prod_{k=1}^{N} x_k` | $\prod_{k=1}^{N} x_k$ | 
| **Coproduct** | `\coprod_{i} A_i` | $\coprod_{i} A_i$ | 
| **Integral** | `\int_{a}^{b} f(x) \, dx` | $\int_{a}^{b} f(x) \, dx$ | 
| **Double Integral** | `\iint_{D} f(x,y) \, dx\,dy` | $\iint_{D} f(x,y) \, dx\,dy$ | 
| **Triple Integral** | `\iiint_{V} \rho \, dv` | $\iiint_{V} \rho \, dv$ | 
| **Contour Integral** | `\oint_{C} \mathbf{F} \cdot d\mathbf{r}` | $\oint_{C} \mathbf{F} \cdot d\mathbf{r}$ | 
| **Union / Intersection Operators** | `\bigcap_{i \in I} A_i`, `\bigcup_{i \in I} A_i` | $\bigcap_{i \in I} A_i$, $\bigcup_{i \in I} A_i$ | 
| **Limit** | `\lim_{x \to 0} \frac{\sin x}{x}` | $\lim_{x \to 0} \frac{\sin x}{x}$ | 
| **Supremum / Infimum** | `\sup_{x} f(x)`, `\inf_{x} f(x)` | $\sup_{x} f(x)$, $\inf_{x} f(x)$ | 
| **Derivative / Partial** | `\frac{df}{dx}`, `\frac{\partial f}{\partial x}` | $\frac{df}{dx}$, $\frac{\partial f}{\partial x}$ | 
| **Gradient / Divergence** | `\nabla f`, `\nabla \cdot \mathbf{F}` | $\nabla f$, $\nabla \cdot \mathbf{F}$ | 

---

## 9. Mathematical Accents & Styles

| Accent / Font | Command Example | Rendered Output | Usage Description | 
| ----- | ----- | ----- | ----- | 
| **Hat** | `\hat{x}` or `\widehat{xy}` | $\hat{x}$, $\widehat{xy}$ | Vector / estimator | 
| **Tilde** | `\tilde{x}` or `\widetilde{xy}` | $\tilde{x}$, $\widetilde{xy}$ | Transformation / median | 
| **Bar / Overline** | `\bar{x}` or `\overline{ab}` | $\bar{x}$, $\overline{ab}$ | Sample mean / complex conjugate | 
| **Dot / Ddot** | `\dot{x}`, `\ddot{x}` | $\dot{x}$, $\ddot{x}$ | Time derivatives ($\frac{dx}{dt}, \frac{d^2x}{dt^2}$) | 
| **Vector Arrow** | `\vec{v}` | $\vec{v}$ | Euclidean vector | 
| **Blackboard Bold** | `\mathbb{R}`, `\mathbb{N}`, `\mathbb{Z}` | $\mathbb{R}, \mathbb{N}, \mathbb{Z}$ | Standard number sets (Reals, Naturals, Integers) | 
| **Calligraphic** | `\mathcal{L}`, `\mathcal{F}` | $\mathcal{L}, \mathcal{F}$ | Transforms / Lagrangian / sets | 
| **Fraktur (Gothic)** | `\mathfrak{g}`, `\mathfrak{p}` | $\mathfrak{g}, \mathfrak{p}$ | Lie algebras, algebraic structures | 

---

## 10. Structural Environments & Layouts

### A. Fractions & Roots
* **Standard Fraction**: `$\frac{a}{b}$` $\rightarrow \frac{a}{b}$
* **Nested Fractions**: `$\frac{\frac{a}{b}}{c}$` $\rightarrow \frac{\frac{a}{b}}{c}$
* **Roots**: `$\sqrt{x}$` $\rightarrow \sqrt{x}$ and `$\sqrt[n]{x}$` $\rightarrow \sqrt[n]{x}$

### B. Matrices & Arrays
Use `pmatrix` (parentheses), `bmatrix` (square brackets), or `vmatrix` (determinants):

```latex
$$
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}
$$
```

Rendered Output:
$$
\begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}
$$

### C. Multi-line Aligned Equations (`aligned`)
Use `&` to mark the alignment axis (usually `=`) and `\\` for line breaks:

```latex
$$
\begin{aligned}
(x + y)^2 &= (x + y)(x + y) \\
&= x^2 + xy + yx + y^2 \\
&= x^2 + 2xy + y^2
\end{aligned}
$$
```

Rendered Output:
$$
\begin{aligned}
(x + y)^2 &= (x + y)(x + y) \\
&= x^2 + xy + yx + y^2 \\
&= x^2 + 2xy + y^2
\end{aligned}
$$

### D. Piecewise Functions (`cases`)
```latex
$$
f(x) = \begin{cases}
x^2 & \text{if } x \ge 0 \\
-x & \text{if } x < 0
\end{cases}
$$
```

Rendered Output:
$$
f(x) = \begin{cases} x^2 & \text{if } x \ge 0 \\ -x & \text{if } x < 0 \end{cases}
$$

---

## 11. Step-by-Step Training Guidelines for LLM Conversion

When instructing an LLM to convert standard mathematical text into LaTeX format, enforce the following sequential conversion rules:

1. **Step Identification**: Convert all bullet points or step numbers into inline LaTeX (e.g., `Step 1.` $\rightarrow$ `Step $1$.` or `$1$.`).
2. **Number & Variable Wrapping**: Wrap every independent number, algebraic variable, operator, and equation in dollar signs `$ ... $`.
3. **Fraction Conversion**: Replace forward slash expressions like `a/b` or `22/7` with proper LaTeX fraction commands `\frac{a}{b}` or `\frac{22}{7}`.
4. **Punctuation Isolation**: Keep non-math English punctuation (commas, periods, colons) outside dollar sign delimiters unless they are part of a math formula.
5. **Unit Formatting**: Enclose physical units within `\text{...}` inside math delimiters (e.g., `$7\text{ cm}$`).

---

## 12. Transformation Examples (Plain Text to Standard LaTeX)

### Example 1: Basic Arithmetic & Step Proof

* **Plain Text Input:**
  Worked example: The movements are 1, -2, 3, -4, and so on up to -10. Where does the coin end? 1. Pair the movements: 1 + (-2) = -1. 2. 3 + (-4) = -1. 3. 5 + (-6) = -1. 4. 7 + (-8) = -1. 5. 9 + (-10) = -1. 6. (-1) + (-1) + (-1) + (-1) + (-1) = -5. Answer: At -5.

* **Converted Output:**
  Worked example: The movements are $1$, $-2$, $3$, $-4$, and so on up to $-10$. Where does the coin end?
  
  $1$. Pair the movements: $1 + (-2) = -1$.
  $2$. $3 + (-4) = -1$.
  $3$. $5 + (-6) = -1$.
  $4$. $7 + (-8) = -1$.
  $5$. $9 + (-10) = -1$.
  $6$. $(-1) + (-1) + (-1) + (-1) + (-1) = -5$.
  
  Answer: At $-5$.

### Example 2: Circle Geometry Problem

* **Plain Text Input:**
  1. 2pi r = 44. 2. 2 * 22/7 * r = 44, so 44r/7 = 44. 3. r = 7 cm. Answer: 7 cm.

* **Converted Output:**
  $1$. $2\pi r = 44$.
  $2$. $2 \times \frac{22}{7} \times r = 44$, so $\frac{44r}{7} = 44$.
  $3$. $r = 7\text{ cm}$.
  
  Answer: $7\text{ cm}$.

---

## 13. LLM Math-to-LaTeX Conversion: Master Guardrails & Formatting Guide

This section outlines the core rules, anti-patterns, and system prompt constraints required to train or fine-tune an LLM to convert plain-text math into strictly formatted, mathematically sound LaTeX without the common rendering bugs identified in review of this pipeline's automated converter (`core/solutions/latex_convert.py`).

### A. The Core Rules for Strict LaTeX Conversion

**Rule 1: Never Wrap Full Sentences or Parenthetical Notes in Math Mode**
* **The Issue:** Wrapping entire natural-language sentences or instructions inside `$...$` causes LaTeX to ignore spaces, turning words into a single squished string.
* **Wrong:** `$\text{(Ignore the dotted portions that lie within the circles.)}$` or `$($Ignore the dotted portions...$)$`
* **Right:** `(Ignore the dotted portions that lie within the circles.)` *(Keep plain text outside math mode)*

**Rule 2: Clean Fraction & Coefficient Grouping**
* **The Issue:** Writing coefficients alongside fractions (e.g., $4\pi \frac{r}{3}$) creates poor visual typesetting and clumsy LaTeX markup.
* **Wrong:** `$4\pi \frac{r}{3}$`
* **Right:** `$\frac{4\pi r}{3}$` or `$\frac{4}{3}\pi r$`
* **Caution:** this only ever applies to the content strictly before the slash (the numerator). A coefficient or term written AFTER a already-complete fraction with just a space ("$1/2$ ah", "$1/2$ wh") is a SEPARATE multiplied term, not part of the denominator - $\frac{1}{2}ah$ is correct, $\frac{1}{2ah}$ changes the value and is wrong.

**Rule 3: Consistent Single-Letter Variable Wrapping**
* **The Issue:** Ambiguity with English articles (like the word "a") often leads to inconsistent wrapping, where $b$, $c$, and $d$ are wrapped in `$...$` but $a$ is left bare.
* **Wrong:** `semicircle a`, but `semicircles $b$, $c$, and $d$`
* **Right:** `semicircle $a$`, and `semicircles $b$, $c$, and $d$` *(Every mathematical identifier, including $a'$, must be wrapped consistently)*
* **Caution:** a cue word like "sides"/"radii"/"semicircle" appearing nearby does NOT by itself mean the next "a" is a variable - "the sides of a 10 cm square" and "the arc of a circle" use the same words in ordinary prose, with "a" as the plain article. Only trust the cue word when it sits immediately before "a" ("semicircle a"), or when "a" is also directly followed by a comma continuing an explicit list ("sides are a, b, c").

**Rule 4: Proper Handling of Option Labels and Roman Numerals**
* **The Issue:** Splitting brackets and Roman numerals or option identifiers across math and text modes (e.g., `$($iii$)$` or `$(b$`) leads to font mismatches and broken spacing.
* **Wrong:** `` $($iii$)` The two paths have equal length.``
* **Right:** `(iii) The two paths have equal length.` or `$(iii)$` *(Keep the entire label marker clean)*

**Rule 5: Prevent Symbol Gluing**
* **The Issue:** Greek letters or operators glued directly to adjacent variables without proper spacing result in invalid control sequences (e.g., `\pir` instead of `\pi r`).
* **Wrong:** `$\pir$`
* **Right:** `$\pi r$`

**Rule 6: A Parenthetical List of Short Variables Keeps Its Parens Outside Every Item**
* **The Issue:** "(b, c and d)" merges the opening `(` into the first item and the closing `)` into the last, because both are single-letter tokens with no prose word to force a break: `$(b$, $c$ and $d)$`.
* **Wrong:** `semicircles $(b$, $c$ and $d)$`
* **Right:** `semicircles ($b$, $c$ and $d$)` *(parens as plain text, each item wrapped on its own)*

**Rule 7: Common Abbreviations Stay Whole, Never Split**
* **The Issue:** "i.e." and "e.g." look, letter by letter, like two one-letter variables separated by periods - wrapping each letter on its own scatters the abbreviation into math mode and breaks the surrounding parenthetical note with it.
* **Wrong:** `$(i$.$e$., the curved portion)`
* **Right:** `(i.e., the curved portion)` *(the whole abbreviation stays plain text)*

**Rule 8: A Capitalised "A" Can Be the English Article, Not a Point Label**
* **The Issue:** Point labels (A, B, C, ...) and the English indefinite article "A" look identical when "A" starts a sentence or a part-label ("(vi) A semicircle..."). Wrapping it unconditionally turns ordinary prose into a stray math variable.
* **Wrong:** `$A$ chord of a circle...`, `(vi) $A$ semicircle...`
* **Right:** `A chord of a circle...`, `(vi) A semicircle...` *(a genuine noun right after "A" means article; another letter, a verb, or punctuation means the point label - "centres $A$ and $B$", "$A$ is the centre")*

**Rule 9: A Trailing Prime Mark Is Never English - Wrap It Even Far From the List That Introduced It**
* **The Issue:** Once "a, b, c, d" are introduced as variables, LATER sentences still use the bare, primed form ("a'") without the list nearby to signal it - "a" cannot grammatically take a possessive, so a bare `'` glued right onto it is never prose.
* **Wrong:** `So a' = b' + c' + d'` (while $b'$, $c'$, $d'$ are correctly wrapped next to it)
* **Right:** `So $a' = b' + c' + d'$` *(the apostrophe glued directly on is the signal, regardless of distance from the introducing list)*

**Rule 10: "a" Paired With "by" or "and" in a Dimension or List Phrase Is the Variable**
* **The Issue:** An article is never directly followed by the preposition "by" or the conjunction "and" (it always introduces a noun) - "two a by b rectangles", "legs be a and b" are dimension/list phrases, not prose, even though they read like a plain sentence.
* **Wrong:** `two a by $b$ rectangles`, `the legs be a and $b$`
* **Right:** `two $a$ by $b$ rectangles`, `the legs be $a$ and $b$` *(caution: "divided BY a factor" has "a" preceded by "by" too, but is genuine prose - only trust "a" preceded by "by" when the word before "by" is ALSO a short variable-like token, e.g. "an $a$ by $a$ square", never after a real verb like "divided"/"multiplied"/"bounded")*

### B. Quick Reference: Wrong vs. Right Patterns

| Plain Text Concept | Flawed LLM Output (Common Bugs) | Correct LaTeX Output |
| --- | --- | --- |
| **Units in formulas** | `$r$ units` (bare, not in math mode) | `$r\text{ units}$` *(with explicit `\text{}` for text units)* |
| **Degrees** | `$60^\circ$` | `$60^\circ$` *(Correct, but ensure no space breaks)* |
| **Multi-step equations** | `Step $1$. $AB=AC$` | `$1$. $AB = AC = BC = r$` |
| **Fractions with roots** | `$\sqrt{2} / 3$` | `$\frac{\sqrt{2}}{3}$` |
| **Coefficient + fraction** | `4\pi \frac{r}{3}` | `\frac{4\pi r}{3}` |
| **Parenthetical note** | `$($Ignore the dotted portions...$)$` | `(Ignore the dotted portions...)` |
| **Roman-numeral label** | `$($iii$)$` | `(iii)` |

### C. System Prompt Template for an LLM Converter

```markdown
You are an expert mathematical typesetter specializing in clean, error-free LaTeX conversion. When converting text, follow these strict execution boundaries:

1. Strict Isolation: Enclose ALL numbers, variables, mathematical symbols, operators, and equations in single-dollar LaTeX delimiters ($...$).
2. Never Wrap Plain Text Sentences: Keep all explanatory sentences, instructions, and non-mathematical notes entirely in plain text outside of math mode. Never wrap a full sentence in $...$.
3. Cohesive Fractions: Always merge scalar coefficients and constants into a single numerator (e.g., write \frac{4\pi r}{3}, never 4\pi \frac{r}{3}) - but never let a coefficient or term written AFTER a complete, already-divided fraction merge into the denominator across a space.
4. Uniform Variable Wrapping: Every single-letter mathematical variable or identifier (including "a", "b", "c", "d", "r", "a'") must be wrapped in $...$, even when used in a list or description - but a cue noun ("sides", "radius") appearing nearby does not by itself make a following "a" a variable; English prose ("the sides of a square") must stay unwrapped.
5. Clean Spacing: Ensure proper spaces between symbols (use \pi r, never \pir). Keep option labels like (i), (ii), (iii) cleanly formatted, outside math mode.
```