from _style import *


class C21_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Isosceles Right Triangles, Example 2"))

        self.add(right_triangle([-6.1, -1.7, 0], 3.2, 3.2, left=r"6", bottom=r"6", hyp=r"\sqrt{72}",
                                solved=("left", "bottom"), size=36))

        work = steps([
            r"For an isosceles right triangle, $c^2 = 2a^2$.",
            r"$c = \sqrt{72}$, so $c^2 = (\sqrt{72})^2 = 72$.",
            r"So $2a^2 = 72$.",
            r"$72 \div 2 = 36$, so $a^2 = 36$.",
            r"$\sqrt{36} = 6$, so $a = 6$.",
        ], width=7.4, size=30, gap=0.2)
        slip = note("Common mistake", r"halving the hypotenuse itself. Square it, halve, then take the root.",
                    width=7.4)
        ans = answer_box(r"each of the other two sides has length 6", width=7.4, size=30)

        column = VGroup(work, slip, ans).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.4, 0])
        self.add(column)
