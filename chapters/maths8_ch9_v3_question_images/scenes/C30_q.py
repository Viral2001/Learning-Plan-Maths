from _style import *


class C30_q(Scene):
    def construct(self):
        self.add(header("Question", r"Isosceles Right Triangles, Q2"))

        question = para(r"The length of the two equal sides of an isosceles right triangle is given. "
                        r"Find the length of the hypotenuse. Find bounds on the length of the "
                        r"hypotenuse such that they have at least one digit after the decimal point."
                        r"\\[10pt](i) 3 \quad (ii) 4 \quad (iii) 6 \quad (iv) 8 \quad (v) 9",
                        width=7.2, size=34)
        question.move_to([LEFT_EDGE + question.width / 2, 0, 0])
        self.add(question)

        self.add(right_triangle([3.0, -1.9, 0], 3.6, 3.6, left=r"\text{equal side}",
                                bottom=r"\text{equal side}", hyp=r"?", size=32))
