from _style import *


class C66_q(Scene):
    def construct(self):
        self.add(header("Question", r"Chapter Exercises, Q6"))

        question = para(r"Give 5 examples of rectangles whose sidelengths and diagonals are all integers.",
                        width=5.8, size=42)
        question.move_to([LEFT_EDGE + question.width / 2, 0, 0])
        self.add(question)

        A, B, C, D = [1.4, -1.7, 0], [5.8, -1.7, 0], [5.8, 1.3, 0], [1.4, 1.3, 0]
        self.add(Polygon(A, B, C, D, color=INK, stroke_width=4, fill_color=SHAPE_FILL, fill_opacity=0.65))
        self.add(Line(A, C, color=INK, stroke_width=4))
        self.add(side_label(r"?", A, B, [0, -0.4, 0], color=RED, size=44))
        self.add(side_label(r"?", B, C, [0.36, 0, 0], color=RED, size=44))
        self.add(side_label(r"?", A, C, [-0.24, 0.34, 0], color=RED, size=44))
