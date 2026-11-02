from _style import *


class C40_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Missing Sides and New Squares, Q3"))

        a = 1.2
        self.add(word(r"\textbf{Triple}", 28, TEAL).move_to([-5.9, 2.75, 0]))
        self.add(right_triangle([-5.9, 0.75, 0], a, 2 ** 0.5 * a, left=r"a", bottom=r"d",
                                hyp=r"\text{area } a^2 + 2a^2 = 3a^2", size=26, solved="hyp"))
        self.add(word(r"\textbf{Five times}", 28, TEAL).move_to([-5.55, -0.1, 0]))
        self.add(right_triangle([-5.9, -2.3, 0], a, 2 * a, left=r"a", bottom=r"2a",
                                hyp=r"\text{area } a^2 + 4a^2 = 5a^2", size=26, solved="hyp"))

        work = steps([
            r"Let the given square have side $a$ and area $a^2$.",
            r"Its diagonal $d$ is the side of the square with double the area: $d^2 = 2a^2$.",
            r"Make a right triangle with perpendicular sides $a$ and $d$.",
            r"By Baudh\={a}yana's Theorem, the square on its hypotenuse has area "
            r"$a^2 + d^2 = a^2 + 2a^2 = 3a^2$: triple.",
            r"For five times, make a right triangle with perpendicular sides $a$ and $2a$.",
            r"The square on its hypotenuse has area $a^2 + (2a)^2 = a^2 + 4a^2 = 5a^2$.",
        ], width=7.6, size=23, gap=0.08)
        ans = answer_box(r"Triple: the square on the hypotenuse of the right triangle whose sides are "
                         r"a side and a diagonal of the given square. Five times: the square on the "
                         r"hypotenuse of the right triangle with sides $a$ and $2a$",
                         width=7.6, size=23, pad=0.2)
        slip = note("Common mistake", r"taking the diagonal as $2a$. Its square is $2a^2$, not $4a^2$.",
                    width=7.6, size=23)

        column = VGroup(work, ans, slip).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.42, 0])
        self.add(column)
