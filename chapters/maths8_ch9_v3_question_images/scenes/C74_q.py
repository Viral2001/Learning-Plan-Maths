from _style import *


class C74_q(Scene):
    def construct(self):
        self.add(header("Question", r"Chapter Exercises, Q3"))

        question = para(r"Find the sidelength of a rhombus whose diagonals are of length 24 units "
                        r"and 70 units.", width=5.2, size=40)
        question.move_to([LEFT_EDGE + question.width / 2, 0, 0])
        self.add(question)

        unit = 0.09
        O = np.array([3.1, -0.1, 0])
        E, N, W, S = O + 35 * unit * RIGHT, O + 12 * unit * UP, O + 35 * unit * LEFT, O + 12 * unit * DOWN
        self.add(Polygon(E, N, W, S, color=INK, stroke_width=4, fill_color=SHAPE_FILL, fill_opacity=0.65))
        self.add(DashedLine(W, E, color=INK, stroke_width=3), DashedLine(S, N, color=INK, stroke_width=3))
        self.add(MathTex(r"70", font_size=36, color=INK).move_to(O + [1.7, -0.25, 0]))
        self.add(MathTex(r"24", font_size=36, color=INK).move_to(O + [0.34, 0.45, 0]))
        self.add(MathTex(r"?", font_size=44, color=RED).move_to((E + N) / 2 + [0.2, 0.36, 0]))
