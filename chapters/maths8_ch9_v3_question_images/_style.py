"""Common look for the Ch9 question images. Every scene file imports this, so a change here
changes all of them. Canvas is Manim's default 14.22 x 8 frame, rendered at 1920x1080."""
from manim import *

config.background_color = WHITE

INK = "#1F2937"
MUTED = "#6B7280"
TEAL = "#0F766E"
AMBER = "#B45309"
BLUE = "#1D4ED8"
RED = "#B91C1C"
TEAL_BG = "#D1FAE5"
SLIP_BG = "#FEF3C7"
SHAPE_FILL = "#DBEAFE"

LEFT_EDGE = -6.6
RIGHT_EDGE = 6.6
TOP_EDGE = 3.7

_TEX = TexTemplate()
_TEX.add_to_preamble(r"\usepackage{xcolor}\usepackage{ragged2e}\setlength{\parskip}{0pt}")


def para(text, width=6.0, size=30, color=INK):
    """A wrapped paragraph of LaTeX text, `width` Manim units wide at any font size."""
    # One LaTeX inch comes out as about 0.0723 * size Manim units
    inches = width / (0.0723 * size)
    body = r"\parbox{%.2fin}{\RaggedRight\hyphenpenalty=10000\exhyphenpenalty=10000 %s}" % (inches, text)
    return Tex(body, tex_template=_TEX, font_size=size, color=color)


def word(text, size=28, color=INK):
    """A short label that does not need wrapping."""
    return Tex(text, tex_template=_TEX, font_size=size, color=color)


def header(role, label):
    """Top band: 'Question' or 'Solution' pill on the left, the book reference on the right."""
    colour = BLUE if role == "Question" else TEAL
    word = Tex(r"\textbf{%s}" % role, tex_template=_TEX, font_size=32, color=WHITE)
    pill = RoundedRectangle(corner_radius=0.16, width=word.width + 0.6, height=word.height + 0.3,
                            fill_color=colour, fill_opacity=1, stroke_width=0)
    word.move_to(pill)
    left = VGroup(pill, word)
    left.move_to([LEFT_EDGE + left.width / 2, TOP_EDGE - left.height / 2, 0])
    ref = Tex(label, tex_template=_TEX, font_size=26, color=MUTED)
    ref.move_to([RIGHT_EDGE - ref.width / 2, left.get_y(), 0])
    return VGroup(left, ref)


def steps(items, width=7.2, size=30, gap=0.22):
    """Numbered working, one line of thought per item."""
    rows = VGroup()
    for n, text in enumerate(items, 1):
        num = Tex(r"\textbf{%d.}" % n, tex_template=_TEX, font_size=size, color=TEAL)
        body = para(text, width - 0.5, size)
        body.next_to(num, RIGHT, buff=0.16, aligned_edge=UP)
        rows.add(VGroup(num, body))
    rows.arrange(DOWN, aligned_edge=LEFT, buff=gap)
    return rows


def note(title, text, width=7.2, size=26, fill=SLIP_BG, colour=AMBER):
    """A tinted box: Common mistake, Check."""
    body = para(r"\textbf{%s:} %s" % (title, text), width - 0.6, size)
    box = RoundedRectangle(corner_radius=0.12, width=width, height=body.height + 0.3,
                           fill_color=fill, fill_opacity=1, stroke_color=colour, stroke_width=1.5)
    body.move_to(box)
    return VGroup(box, body)


def answer_box(text, width=7.2, size=34, pad=0.32):
    body = para(r"\textbf{Answer:} %s" % text, width - 0.6, size)
    box = RoundedRectangle(corner_radius=0.12, width=width, height=body.height + pad,
                           fill_color=TEAL_BG, fill_opacity=1, stroke_color=TEAL, stroke_width=3)
    body.move_to(box)
    return VGroup(box, body)


def triangle(a, b, c, fill=SHAPE_FILL):
    return Polygon(a, b, c, color=INK, stroke_width=4, fill_color=fill, fill_opacity=0.65)


def right_mark(corner, p, q, size=0.3):
    """Square mark at `corner`, between the sides going to p and to q."""
    corner, p, q = np.array(corner), np.array(p), np.array(q)
    u = (p - corner) / np.linalg.norm(p - corner) * size
    v = (q - corner) / np.linalg.norm(q - corner) * size
    return Polygon(corner + u, corner + u + v, corner + v, corner,
                   color=INK, stroke_width=3, fill_opacity=0)


def side_label(text, p, q, shift, size=36, color=INK):
    """Math label at the middle of side pq, pushed by `shift`."""
    mid = (np.array(p) + np.array(q)) / 2
    return MathTex(text, font_size=size, color=color).move_to(mid + np.array(shift))


def grid_table(rows, widths, row_h=0.56, size=28, colours=None):
    """Ruled table, top left at the origin. rows[0] is the header. `colours` maps a column to a colour."""
    colours = colours or {}
    total, height = sum(widths), row_h * len(rows)
    head = Rectangle(width=total, height=row_h, fill_color=SHAPE_FILL, fill_opacity=1, stroke_width=0)
    head.move_to([total / 2, -row_h / 2, 0])
    frame = Rectangle(width=total, height=height, color=INK, stroke_width=2)
    frame.move_to([total / 2, -height / 2, 0])
    out = VGroup(head, frame)
    for r in range(1, len(rows)):
        out.add(Line([0, -r * row_h, 0], [total, -r * row_h, 0], color=MUTED, stroke_width=1.5))
    for r, row in enumerate(rows):
        x = 0
        for c, cell in enumerate(row):
            text = r"\textbf{%s}" % cell if r == 0 else cell
            colour = colours.get(c, INK) if r else INK
            out.add(Tex(text, tex_template=_TEX, font_size=size, color=colour)
                    .move_to([x + widths[c] / 2, -(r + 0.5) * row_h, 0]))
            x += widths[c]
    return out


def dot_grid(origin, n=5, gap=0.44):
    """n x n dot grid as in the book, bottom left dot at `origin`."""
    x0, y0 = origin[0], origin[1]
    out = VGroup()
    for k in range(n):
        out.add(Line([x0 - 0.1, y0 + k * gap, 0], [x0 + (n - 1) * gap + 0.1, y0 + k * gap, 0],
                     color=MUTED, stroke_width=1.5))
        out.add(Line([x0 + k * gap, y0 - 0.1, 0], [x0 + k * gap, y0 + (n - 1) * gap + 0.1, 0],
                     color=MUTED, stroke_width=1.5))
    for i in range(n):
        for j in range(n):
            out.add(Dot([x0 + i * gap, y0 + j * gap, 0], radius=0.045, color=INK))
    return out


def grid_square(origin, corners, gap=0.44, colour=TEAL):
    """Square drawn through grid dots, `corners` as (across, up) dot counts from `origin`."""
    points = [[origin[0] + i * gap, origin[1] + j * gap, 0] for i, j in corners]
    return Polygon(*points, color=colour, stroke_width=4, fill_color=TEAL_BG, fill_opacity=0.7)


def right_triangle(R, up, across, left=None, bottom=None, hyp=None, size=36, solved=None):
    """Upright right triangle with the right angle at R. `solved` names the label to colour teal;
    a label written as ? is red."""
    R = np.array(R, dtype=float)
    P, Q = R + up * UP, R + across * RIGHT
    out = VGroup(triangle(R, P, Q), right_mark(R, P, Q, size=min(0.3, 0.45 * min(up, across))))

    def colour(name, text):
        return RED if "?" in text else TEAL if solved and name in solved else INK

    if left:
        out.add(MathTex(left, font_size=size, color=colour("left", left))
                .next_to(Line(R, P), LEFT, buff=0.14))
    if bottom:
        out.add(MathTex(bottom, font_size=size, color=colour("bottom", bottom))
                .next_to(Line(R, Q), DOWN, buff=0.14))
    if hyp:
        n = np.array([up, across, 0]) / np.hypot(up, across)
        label = MathTex(hyp, font_size=size, color=colour("hyp", hyp))
        offset = n[0] * label.width / 2 + n[1] * label.height / 2 + 0.1
        out.add(label.move_to((P + Q) / 2 + n * offset))
    return out


def part_card(label, lines, answer, width=6.5, height=2.05, size=23, gap=0.07, figure=None):
    """One part of a many-part solution: label, its lines of working, a small answer strip.
    `figure` sits at the left of the card when given."""
    room = width - 0.36 - (figure.width + 0.3 if figure else 0)
    text = VGroup(para(r"\textbf{%s}" % label, room, size, TEAL), *[para(t, room, size) for t in lines])
    text.arrange(DOWN, aligned_edge=LEFT, buff=gap)
    if text.width > room:
        text.scale(room / text.width)
    body = VGroup(text, answer_box(answer, width=room, size=size, pad=0.14))
    body.arrange(DOWN, aligned_edge=LEFT, buff=gap + 0.03)
    box = RoundedRectangle(corner_radius=0.1, width=width, height=max(height, body.height + 0.2),
                           color=MUTED, stroke_width=1.2, fill_opacity=0)
    body.move_to(box.get_right() + (0.18 + body.width / 2) * LEFT)
    out = VGroup(box, body)
    if figure:
        figure.move_to(box.get_left() + (0.15 + figure.width / 2) * RIGHT)
        out.add(figure)
    return out


def lotus_figure(W, unit=0.72, solved=False):
    """The lake in section. W is where the upright stem meets the water; the bed is 4 units below.
    The bent stem touches the water 3 units to the right. `solved` shades the triangle and names x."""
    W = np.array(W, dtype=float)
    B, T, P = W + 4 * unit * DOWN, W + unit * UP, W + 3 * unit * RIGHT
    a, b = W + 1.3 * LEFT, P + 0.9 * RIGHT
    down = 4 * unit * DOWN
    out = VGroup(Polygon(a, b, b + down, a + down, fill_color=SHAPE_FILL, fill_opacity=0.55, stroke_width=0))
    if solved:
        out.add(Polygon(B, W, P, fill_color=TEAL_BG, fill_opacity=0.9, stroke_width=0))
    out.add(Line(a, b, color=BLUE, stroke_width=4), Line(a + down, b + down, color=INK, stroke_width=4))
    out.add(Line(B, T, color=INK, stroke_width=4), Line(B, P, color=TEAL if solved else INK, stroke_width=4))
    if solved:
        out.add(right_mark(W, B, P, size=0.26))
    out.add(Dot(T, radius=0.09, color=RED), Dot(P, radius=0.09, color=RED))

    size = 32
    out.add(MathTex("1", font_size=size, color=INK).next_to(Line(W, T), LEFT, buff=0.14))
    out.add(MathTex("3", font_size=size, color=INK).next_to(Line(W, P), UP, buff=0.12))
    out.add(MathTex("x" if solved else "?", font_size=size, color=TEAL if solved else RED)
            .next_to(Line(B, W), LEFT, buff=0.14))
    if solved:
        out.add(MathTex("x + 1", font_size=size, color=TEAL).move_to((B + P) / 2 + np.array([0.62, -0.3, 0])))
    return out


def card_grid(cards, top, columns=2, gap=0.14):
    """Lay cards row by row from `top`, starting at the left edge."""
    width = cards[0].width
    x = [LEFT_EDGE + width / 2 + i * (width + 0.2) for i in range(columns)]
    y = top
    out = VGroup()
    for start in range(0, len(cards), columns):
        row = cards[start:start + columns]
        h = max(c.height for c in row)
        for i, c in enumerate(row):
            c.move_to([x[i], y - h / 2, 0])
            out.add(c)
        y -= h + gap
    return out
