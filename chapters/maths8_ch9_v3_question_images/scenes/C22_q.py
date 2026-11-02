from _style import *


class C22_q(Scene):
    def construct(self):
        self.add(header("Question", r"Chapter Exercises, Q1"))

        question = para(r"Find the diagonal of a square with sidelength 5 cm.", width=5.8, size=40)
        question.move_to([LEFT_EDGE + question.width / 2, 0, 0])
        self.add(question)

        s = 4.0
        A = np.array([1.2, -2.0, 0])
        B, C, D = A + s * RIGHT, A + s * RIGHT + s * UP, A + s * UP
        self.add(Polygon(A, B, C, D, color=INK, stroke_width=4, fill_color=SHAPE_FILL, fill_opacity=0.65))
        self.add(Line(B, D, color=RED, stroke_width=4))
        self.add(MathTex(r"5\text{ cm}", font_size=36, color=INK).next_to(Line(A, B), DOWN, buff=0.14))
        self.add(MathTex(r"5\text{ cm}", font_size=36, color=INK).next_to(Line(A, D), LEFT, buff=0.14))
        self.add(MathTex(r"?", font_size=44, color=RED).move_to((B + D) / 2 + [0.3, 0.3, 0]))
