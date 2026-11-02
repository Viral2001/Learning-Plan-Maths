from _style import *


class C75_q(Scene):
    def construct(self):
        self.add(header("Question", r"Chapter Exercises, Q8"))

        question = para(r"(i) Using the dots of a grid as the vertices, can you create a square that "
                        r"has an area of (a) 2 sq. units, (b) 3 sq. units, (c) 4 sq. units, and "
                        r"(d) 5 sq. units?\\[12pt](ii) Suppose the grid extends indefinitely. What are "
                        r"the possible integer-valued areas of squares you can create in this manner?",
                        width=7.4, size=34)
        question.move_to([LEFT_EDGE + question.width / 2, -0.2, 0])
        self.add(question)

        self.add(dot_grid([2.0, -2.2], n=5, gap=1.0))
