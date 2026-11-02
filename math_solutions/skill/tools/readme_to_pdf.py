"""Build NCERT_Board_Solutions_Skill_READ_ME.pdf from the Markdown read-me.

Usage (from the skill/ folder):  python tools/readme_to_pdf.py
Needs pdflatex. Handles only the Markdown subset the read-me uses: headings,
pipe tables, fenced code, bullet and numbered lists, **bold**, *italic*,
`code` and $math$. Re-run it whenever the .md changes so the PDF never drifts.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)
SRC = os.path.join(SKILL, 'NCERT_Board_Solutions_Skill_READ_ME.md')
OUT_DIR = os.path.join(SKILL, 'tools', '_build')
JOB = 'NCERT_Board_Solutions_Skill_READ_ME'

UNI_TEXT = {'–': '--', '…': r'\ldots{}', '°': r'\ensuremath{^\circ}',
            '∠': r'\ensuremath{\angle}', '⊥': r'\ensuremath{\perp}',
            'θ': r'\ensuremath{\theta}', '∥': r'\ensuremath{\parallel}',
            '△': r'\ensuremath{\triangle}'}
UNI_PLAIN = {'–': '-', '…': '...', '°': 'deg', '∠': 'angle',
             '⊥': 'perp', 'θ': 'theta', '∥': 'par', '△': 'tri'}
ESC = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '#': r'\#', '_': r'\_',
       '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}',
       '$': r'\$'}

PREAMBLE = r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=2cm]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,array,longtable,xcolor,enumitem}
\usepackage[hidelinks]{hyperref}
\renewcommand{\deg}{^\circ}
\newcommand{\ang}{\angle}
\newcommand{\tri}{\triangle}
\newcommand{\ans}[1]{\fbox{Answer: #1}}
\newcommand{\slip}[1]{\textit{Common mistake. #1}}
\setlength{\parindent}{0pt}\setlength{\parskip}{5pt}
\renewcommand{\arraystretch}{1.25}
\sloppy
\begin{document}
'''


def esc_text(s):
    out = []
    for ch in s:
        if ch in UNI_TEXT:
            out.append(UNI_TEXT[ch])
        else:
            out.append(ESC.get(ch, ch))
    return ''.join(out)


def esc_code(s):
    out = []
    for ch in s:
        ch = UNI_PLAIN.get(ch, ch)
        out.append(ESC.get(ch, ch) if len(ch) == 1 else ch)
    # allow a line break after each backslash so long macro names wrap
    return ''.join(out).replace(r'\textbackslash{}', r'\textbackslash{}\allowbreak{}')


TOKEN = re.compile(r'`([^`]+)`|\$([^$]+)\$|\*\*(.+?)\*\*|\*([^*\s][^*]*?)\*')


def inl(s):
    out, pos = [], 0
    for m in TOKEN.finditer(s):
        out.append(esc_text(s[pos:m.start()]))
        if m.group(1) is not None:
            out.append(r'\texttt{' + esc_code(m.group(1)) + '}')
        elif m.group(2) is not None:
            out.append('$' + ''.join(UNI_PLAIN.get(c, c) if ord(c) > 127 else c
                                      for c in m.group(2)) + '$')
        elif m.group(3) is not None:
            out.append(r'\textbf{' + inl(m.group(3)) + '}')
        else:
            out.append(r'\textit{' + inl(m.group(4)) + '}')
        pos = m.end()
    out.append(esc_text(s[pos:]))
    return ''.join(out)


def table(rows):
    cells = [[c.strip() for c in r.strip().strip('|').split('|')] for r in rows]
    header, body = cells[0], [c for c in cells[2:]]
    n = len(header)
    narrow = header[0] == '#'
    first = 0.05 if narrow else None
    rest = (0.97 - (first or 0)) / (n - (1 if narrow else 0))
    if not narrow:
        first = rest
    cols = []
    for i in range(n):
        w = first if i == 0 else rest
        cols.append(r'>{\raggedright\arraybackslash}p{\dimexpr %.3f\linewidth-2\tabcolsep\relax}' % w)
    lines = [r'\begin{longtable}{' + ''.join(cols) + '}', r'\hline']
    lines.append(' & '.join(r'\textbf{' + inl(h) + '}' for h in header) + r' \\ \hline \endhead')
    for r in body:
        lines.append(' & '.join(inl(c) for c in r) + r' \\ \hline')
    lines.append(r'\end{longtable}')
    return '\n'.join(lines)


def convert(md):
    lines = md.split('\n')
    out, i = [PREAMBLE], 0
    stack = None  # 'itemize' or 'enumerate'

    def close_list():
        nonlocal stack
        if stack:
            out.append(r'\end{%s}' % stack)
            stack = None

    while i < len(lines):
        l = lines[i]
        if l.startswith('```'):
            close_list()
            i += 1
            block = []
            while i < len(lines) and not lines[i].startswith('```'):
                block.append(''.join(UNI_PLAIN.get(c, c) for c in lines[i]))
                i += 1
            out.append('{\\footnotesize\\begin{verbatim}\n' + '\n'.join(block) + '\n\\end{verbatim}}')
        elif l.startswith('|'):
            close_list()
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                rows.append(lines[i])
                i += 1
            out.append(table(rows))
            continue
        elif l.startswith('# '):
            close_list()
            out.append(r'{\Large\bfseries ' + inl(l[2:]) + r'\par}\vspace{4pt}')
        elif l.startswith('## '):
            close_list()
            out.append(r'\subsection*{' + inl(l[3:]) + '}')
        elif l.strip() == '---':
            close_list()
        elif re.match(r'^- ', l) or re.match(r'^\d+\. ', l):
            kind = 'itemize' if l.startswith('- ') else 'enumerate'
            if stack != kind:
                close_list()
                out.append(r'\begin{%s}[leftmargin=1.4em,itemsep=2pt]' % kind)
                stack = kind
            text = re.sub(r'^(- |\d+\. )', '', l)
            while i + 1 < len(lines) and lines[i + 1].startswith('   '):
                i += 1
                text += ' ' + lines[i].strip()
            out.append(r'\item ' + inl(text))
        elif l.strip() == '':
            pass
        else:
            close_list()
            para = [l]
            while (i + 1 < len(lines) and lines[i + 1].strip() and
                   not re.match(r'^(```|\||#|- |\d+\. |---)', lines[i + 1])):
                i += 1
                para.append(lines[i])
            out.append(inl(' '.join(para)) + '\n')
        i += 1
    close_list()
    out.append(r'\end{document}')
    return '\n'.join(out)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tex = os.path.join(OUT_DIR, JOB + '.tex')
    with open(SRC, encoding='utf-8') as f:
        md = f.read()
    with open(tex, 'w', encoding='utf-8') as f:
        f.write(convert(md))
    for _ in range(2):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', JOB + '.tex'],
                           cwd=OUT_DIR, capture_output=True, text=True, encoding='utf-8',
                           errors='replace')
        if r.returncode:
            print(r.stdout[-2500:])
            sys.exit('pdflatex failed')
    pdf = os.path.join(OUT_DIR, JOB + '.pdf')
    dest = os.path.join(SKILL, JOB + '.pdf')
    os.replace(pdf, dest)
    print('wrote', dest)


if __name__ == '__main__':
    main()
