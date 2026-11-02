from _style import *


class C46_q(Scene):
    def construct(self):
        self.add(header("Question", r"Missing Sides and New Squares, Q4"))

        question = para(r"Let $a$, $b$ and $c$ denote the length of the sides of a right triangle, "
                        r"with $c$ being the length of the hypotenuse. Find the missing sidelength "
                        r"in each of the following cases:\\[10pt](i) $a = 5$, $b = 7$\\"
                        r"(ii) $a = 8$, $b = 12$\\(iii) $a = 9$, $c = 15$\\(iv) $a = 7$, $b = 12$\\"
                        r"(v) $a = 1.5$, $b = 3.5$", width=7.2, size=34)
        question.move_to([LEFT_EDGE + question.width / 2, -0.2, 0])
        self.add(question)

        self.add(right_triangle([2.4, -1.6, 0], 2.9, 3.6, left=r"a", bottom=r"b", hyp=r"c", size=40))
