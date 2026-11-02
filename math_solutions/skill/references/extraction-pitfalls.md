# Extracting questions from a textbook PDF: pitfalls

NCERT chapter PDFs carry a text layer, but it is unreliable for maths. Use it to locate questions, never to copy them.

1. **Transcribe from rendered page images.** Render with `pdftoppm -r 100 -png chapter.pdf pg` and read the images. The text layer drops or garbles ∠, ⊥, θ, ∥, △, fraction layout, blanks in fill-in questions, and primes (X′Y′).
2. **Square roots and fractions** often come out as plain text ("119" for $\sqrt{119}$, "3 4" for $\frac34$). Check each against the image.
3. **Fill-in blanks** disappear from the text. Look at the image to see where the blank is and write it as `\underline{\hspace{2cm}}`.
4. **Options (A)-(D)** may be reordered or merged onto one line. Copy the order from the image.
5. **Figures.** The question may say "see Fig. 10.11". Redraw the figure in TikZ from the description and the image, label the same points as the book, and caption it "(redrawn)". Where the book has no labels, introduce new labels and say so.
6. **Page headers and margins.** Remove running heads such as "Mathematics" or the chapter title that the text layer inserts mid-question.
7. **"Why?" prompts inside solved examples** are questions to the student. Answer them in the solution.
8. **Theorems, Activities and "Think and Discuss" boxes** are not exercises. Leave them out unless asked, and say so in the report.
9. **Scope check.** Count the questions per exercise from the images and compare with the solution file before finishing. Sub-parts (i), (ii) count as separate items.
10. **Windows shell.** When using a Windows machine, write `.tex` and `.py` files with a file-writing tool, never with heredocs or inline `python -` with backslashes. LaTeX backslashes break shell quoting and give `invalid escape sequence` warnings.
11. **PyMuPDF** (`import pymupdf`, or `import fitz` in older versions) can render a page: `page.get_pixmap(dpi=100).save("pg.png")`, in case `pdftoppm` is not installed.
