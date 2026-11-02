from _style import *


class C71_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Chapter Exercises, Q3"))

        unit = 0.07
        O = np.array([-4.1, 0.1, 0])
        E, N, W, S = O + 35 * unit * RIGHT, O + 12 * unit * UP, O + 35 * unit * LEFT, O + 12 * unit * DOWN
        self.add(Polygon(E, N, W, S, color=INK, stroke_width=4, fill_color=SHAPE_FILL, fill_opacity=0.35))
        self.add(Polygon(O, E, N, color=TEAL, stroke_width=4, fill_color=TEAL_BG, fill_opacity=0.9))
        self.add(Line(W, E, color=INK, stroke_width=3), Line(S, N, color=INK, stroke_width=3))
        self.add(right_mark(O, E, N, size=0.2))
        self.add(MathTex(r"35", font_size=30, color=INK).move_to(O + [0.95, 0.17, 0]))
        self.add(MathTex(r"12", font_size=30, color=INK).move_to(O + [-0.3, 0.3, 0]))
        self.add(MathTex(r"37", font_size=34, color=TEAL).move_to((E + N) / 2 + [0.2, 0.34, 0]))

        work = steps([
            r"The diagonals of a rhombus bisect each other at right angles.",
            r"They cut the rhombus into 4 congruent right triangles with sides "
            r"$24 \div 2 = 12$ and $70 \div 2 = 35$.",
            r"Each side of the rhombus is the hypotenuse of one of them.",
            r"By Baudh\={a}yana's Theorem, $c^2 = 12^2 + 35^2 = 144 + 1225 = 1369$.",
            r"$37^2 = 1369$, so the side is 37.",
        ], width=7.5, size=27)
        slip = note("Common mistake", r"using 24 and 70 directly. Halve each diagonal first.", width=7.5)
        ans = answer_box(r"37 units", width=7.5)

        column = VGroup(work, slip, ans).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.4, 0])
        self.add(column)
