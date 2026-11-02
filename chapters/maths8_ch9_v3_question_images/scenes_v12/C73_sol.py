from _style import *


class C73_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Chapter Exercises, Q9"))

        side = 4.4
        A = np.array([-6.0, -1.9, 0])
        B = A + side * RIGHT
        C = A + side * np.array([0.5, 3 ** 0.5 / 2, 0])
        M = (A + B) / 2
        self.add(triangle(A, B, C))
        self.add(Line(C, M, color=TEAL, stroke_width=4), right_mark(M, C, B))
        self.add(side_label(r"6", A, C, [-0.32, 0.18, 0]))
        self.add(side_label(r"6", B, C, [0.32, 0.18, 0]))
        self.add(side_label(r"3", A, M, [0, -0.36, 0]))
        self.add(side_label(r"3", M, B, [0, -0.36, 0]))
        self.add(side_label(r"h", C, M, [0.26, 0.3, 0], color=TEAL))

        work = steps([
            r"Drop the altitude from the top vertex to the base; it makes two right triangles.",
            r"They have equal hypotenuses (6), the altitude in common and right angles, so they "
            r"are congruent and the altitude bisects the base into 3 and 3.",
            r"By Baudh\={a}yana's Theorem in one right triangle:\\ $6^2 - 3^2 = 36 - 9 = 27$, so "
            r"$h^2 = 27$ and $h = \sqrt{27}$.",
            r"$5.1^2 = 26.01$ and $5.2^2 = 27.04$, so $5.1 < \sqrt{27} < 5.2$.",
            r"Area $= \frac{1}{2} \times$ base $\times$ height $= \frac{1}{2} \times 6 \times "
            r"\sqrt{27}$, which is $3\sqrt{27}$.",
            r"$3\sqrt{27} = 9\sqrt{3} \approx 15.59$.",
        ], width=7.6, size=26, gap=0.15)
        slip = note("Common mistake", r"using the side 6 as the height.", width=7.6, size=25)
        ans = answer_box(r"$3\sqrt{27} = 9\sqrt{3}$ square units, about 15.59 square units",
                         width=7.6, size=28)

        column = VGroup(work, slip, ans).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.45, 0])
        self.add(column)
