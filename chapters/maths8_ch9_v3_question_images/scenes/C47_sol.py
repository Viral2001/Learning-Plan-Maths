from _style import *


class C47_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Missing Sides and New Squares, Q2"))

        R, A, B = [-5.5, -1.5, 0], [-5.5, 0.9, 0], [-2.3, -1.5, 0]
        self.add(triangle(R, A, B), right_mark(R, A, B))
        self.add(side_label(r"a = 8", R, A, [-0.0, 0, 0]).next_to(Line(R, A), LEFT, buff=0.1))
        self.add(side_label(r"c = 17", A, B, [0.75, 0.3, 0]))
        self.add(side_label(r"b = 15", R, B, [0, -0.36, 0], color=TEAL))

        work = steps([
            r"Draw a side of 8 cm, a right angle at one end, and swing an arc of 17 cm from "
            r"the other end. The third side measures about 15 cm.",
            r"By Baudh\={a}yana's Theorem, $a^2 + b^2 = c^2$. The hypotenuse is given, so "
            r"subtract: $b^2 = c^2 - a^2$.",
            r"$b^2 = 17^2 - 8^2 = 289 - 64 = 225$",
            r"$15^2 = 225$, so $b = 15$.",
        ], width=7.6, size=28)
        slip = note("Common mistake", r"adding $17^2 + 8^2$. Subtract when the hypotenuse is given.",
                    width=7.6)
        check = note("Check", r"$8^2 + 15^2 = 64 + 225 = 289 = 17^2$", width=7.6,
                     fill=TEAL_BG, colour=TEAL)
        ans = answer_box(r"the third side is 15 cm.", width=7.6)

        column = VGroup(work, slip, check, ans).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.4, 0])
        self.add(column)
