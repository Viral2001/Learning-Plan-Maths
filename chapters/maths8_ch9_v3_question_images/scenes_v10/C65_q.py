from _style import *


class C65_q(Scene):
    def construct(self):
        self.add(header("Question", r"Chapter Exercises, Q8 (i)"))

        question = para(r"Using the dots of a grid as the vertices, can you create a square that "
                        r"has an area of\\[8pt](a) 2 sq. units,\\(b) 3 sq. units,\\(c) 4 sq. units, "
                        r"and\\(d) 5 sq. units?", width=6.4, size=38)
        question.move_to([LEFT_EDGE + question.width / 2, -0.2, 0])
        self.add(question)

        self.add(dot_grid([1.4, -2.3], n=5, gap=1.0))
