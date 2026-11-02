from _style import *


class C14_q(Scene):
    def construct(self):
        self.add(header("Question", r"Isosceles Right Triangles, Q1"))

        question = para(r"Earlier, we saw a method to create a square with double the area of a given "
                        r"square paper. There is another method to do this in which two identical "
                        r"square papers are cut in the following way.\\[8pt]Can you arrange these "
                        r"pieces to create a square with double the area of either square?",
                        width=6.6, size=34)
        question.move_to([LEFT_EDGE + question.width / 2, -0.1, 0])
        self.add(question)

        side = 2.5
        for x, low, high in ((0.75, "1", "2"), (3.85, "3", "4")):
            A = np.array([x, -1.25, 0])
            B, C, D = A + side * RIGHT, A + side * RIGHT + side * UP, A + side * UP
            self.add(triangle(A, B, D), triangle(B, C, D))
            self.add(MathTex(low, font_size=40, color=INK).move_to(A + [0.8, 0.8, 0]))
            self.add(MathTex(high, font_size=40, color=INK).move_to(A + [1.7, 1.7, 0]))
