from _style import *


class C65_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Chapter Exercises, Q5"))

        # One worked example of step 3 and step 4
        top = MathTex(r"(6,\ 8,\ 10)", font_size=44, color=INK)
        bottom = MathTex(r"(3,\ 4,\ 5)", font_size=44, color=TEAL)
        top.move_to([-4.2, 1.1, 0])
        bottom.move_to([-4.2, -1.3, 0])
        down = Arrow(top.get_bottom(), bottom.get_top(), color=INK, stroke_width=4, buff=0.15)
        self.add(top, bottom, down)
        self.add(word(r"divide by $f = 2$", 28, MUTED)
                 .next_to(down, RIGHT, buff=0.15))
        self.add(word(r"Example", 28, MUTED)
                 .next_to(top, UP, buff=0.3))
        self.add(word(r"primitive", 28, TEAL)
                 .next_to(bottom, DOWN, buff=0.2))

        work = steps([
            r"Take any triple $(a, b, c)$ and let $f$ be the greatest common factor of $a$, $b$ and $c$.",
            r"If $f = 1$, the triple is primitive.",
            r"If $f$ is more than 1, then $(a/f, b/f, c/f)$ is a triple with no common factor "
            r"greater than 1: a primitive triple.",
            r"And $(a, b, c)$ is $f$ times that primitive triple: a scaled version.",
        ], width=7.6, size=28)
        slip = note("Common mistake", r"dividing by a smaller factor. $(12, 16, 20) \div 2 = (6, 8, 10)$ "
                    r"still has the factor 2. Use the greatest common factor.", width=7.6)
        ans = answer_box(r"True", width=7.6)

        column = VGroup(work, slip, ans).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.4, 0])
        self.add(column)
