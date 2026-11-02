from _style import *


class C20_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Isosceles Right Triangles, Example 1"))

        self.add(right_triangle([-6.1, -1.7, 0], 3.2, 3.2, left=r"12", bottom=r"12",
                                hyp=r"\sqrt{288}", solved="hyp", size=36))

        work = steps([
            r"The equal sides are 12, so $a = 12$.",
            r"For an isosceles right triangle, $c^2 = 2a^2$.",
            r"$c^2 = 2 \times 12^2 = 2 \times 144 = 288$.",
            r"So $c = \sqrt{288}$.",
            r"$16^2 = 256$ and $17^2 = 289$.",
            r"$256 < 288 < 289$, so $16 < \sqrt{288} < 17$.",
        ], width=7.4, size=28, gap=0.17)
        slip = note("Common mistake", r"writing $c = 12 + 12 = 24$. Square, double, then take the root.",
                    width=7.4)
        ans = answer_box(r"$c = \sqrt{288}$ units, between 16 and 17 units", width=7.4, size=30)

        column = VGroup(work, slip, ans).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.4, 0])
        self.add(column)
