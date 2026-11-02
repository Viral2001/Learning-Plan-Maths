from _style import *


class C73_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"A Problem from Bh\={a}skar\={a}ch\={a}rya's L\={\i}l\={a}vat\={\i}, Worked Example"))

        self.add(lotus_figure([-4.9, 1.1, 0], unit=0.62, solved=True))

        work = steps([
            r"Let the depth be $x$; the stem has length $x + 1$.",
            r"The upright stem is perpendicular to the water, so there is a right angle at the water surface.",
            r"The bent stem, $x + 1$, is the hypotenuse; the other sides are $x$ and 3.",
            r"By Baudh\={a}yana's Theorem, $3^2 + x^2 = (x + 1)^2$.",
            r"$9 + x^2 = x^2 + 2x + 1$.",
            r"Subtract $x^2$ from both sides: $9 = 2x + 1$.",
            r"$2x = 8$, so $x = 4$.",
        ], width=7.1, size=25, gap=0.12)
        slip = note("Common mistake", r"taking the depth $x$ as the hypotenuse. The bent stem faces the right angle.",
                    width=7.1, size=24)
        ans = answer_box(r"the lake is 4 units deep", width=7.1, size=28)

        column = VGroup(work, slip, ans).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.45, 0])
        self.add(column)
