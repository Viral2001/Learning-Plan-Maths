from _style import *


class C40_q(Scene):
    def construct(self):
        self.add(header("Question", r"Chapter Exercises, Q7"))

        question = para(r"Construct a square whose area is equal to the difference of the areas of "
                        r"squares of sidelengths 5 units and 7 units.", width=5.8, size=38)
        question.move_to([LEFT_EDGE + question.width / 2, 0, 0])
        self.add(question)

        unit = 0.46
        big = Square(7 * unit, color=INK, stroke_width=4, fill_color=SHAPE_FILL, fill_opacity=0.65)
        small = Square(5 * unit, color=INK, stroke_width=4, fill_color=SHAPE_FILL, fill_opacity=0.65)
        big.move_to([big.width / 2 - 0.3, -2.2 + big.height / 2, 0])
        small.next_to(big, RIGHT, buff=0.5, aligned_edge=DOWN)
        self.add(big, small)
        self.add(MathTex(r"7", font_size=36, color=INK).next_to(big, DOWN, buff=0.14))
        self.add(MathTex(r"5", font_size=36, color=INK).next_to(small, DOWN, buff=0.14))
