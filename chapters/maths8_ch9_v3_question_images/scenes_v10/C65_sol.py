from _style import *


class C65_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Chapter Exercises, Q8 (i)"))

        panels = [
            ("(a) area 2", [-6.4, 0.5], [(1, 0), (2, 1), (1, 2), (0, 1)]),
            ("(b) area 3", [-3.7, 0.5], None),
            ("(c) area 4", [-6.4, -2.65], [(1, 1), (3, 1), (3, 3), (1, 3)]),
            ("(d) area 5", [-3.7, -2.65], [(1, 0), (3, 1), (2, 3), (0, 2)]),
        ]
        for label, origin, corners in panels:
            self.add(dot_grid(origin))
            if corners:
                self.add(grid_square(origin, corners))
            else:
                text = word(r"\textbf{not possible}", 26, RED)
                text.move_to([origin[0] + 0.88, origin[1] + 0.88, 0])
                self.add(BackgroundRectangle(text, color=WHITE, fill_opacity=1, buff=0.08), text)
            self.add(word(label, 27, INK)
                     .move_to([origin[0] + 0.88, origin[1] + 2.05, 0]))

        work = steps([
            r"A square with its corners on grid dots has a side that goes $p$ dots across and "
            r"$q$ dots up, so its area is $p^2 + q^2$.",
            r"(a) $p = 1$, $q = 1$: $1^2 + 1^2 = 2$, a tilted square of area 2.",
            r"(c) $p = 2$, $q = 0$: an upright 2 by 2 square, area 4.",
            r"(d) $p = 1$, $q = 2$: $1^2 + 2^2 = 5$, a tilted square of area 5.",
            r"(b) 3 is not a sum of two squares: $0 + 1$, $1 + 1$, $0 + 4$ and $1 + 4$ give "
            r"1, 2, 4 and 5, never 3.",
        ], width=7.4, size=27)
        ans = answer_box(r"Yes for areas 2, 4 and 5; no square of area 3 is possible",
                         width=7.4, size=28)

        column = VGroup(work, ans).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.4, 0])
        self.add(column)
