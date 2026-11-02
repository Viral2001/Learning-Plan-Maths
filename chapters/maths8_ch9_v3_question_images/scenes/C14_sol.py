from _style import *


class C14_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Isosceles Right Triangles, Q1"))

        # Right-angle corners meet at O; the long sides make the outer square
        O = np.array([-4.2, -0.2, 0])
        r = 2.15
        E, N, W, S = O + r * RIGHT, O + r * UP, O + r * LEFT, O + r * DOWN
        for p, q, n, fill in ((E, N, "1", SHAPE_FILL), (N, W, "2", TEAL_BG),
                              (W, S, "3", SHAPE_FILL), (S, E, "4", TEAL_BG)):
            self.add(triangle(O, p, q, fill=fill), right_mark(O, p, q, size=0.26))
            self.add(MathTex(n, font_size=38, color=INK).move_to(O + (p + q - 2 * O) * 0.36))
        self.add(word(r"side of the new square = diagonal", 26, TEAL).move_to(O + 2.75 * DOWN))

        work = steps([
            r"Each square is cut along one diagonal into 2 congruent right triangles: "
            r"4 triangles in all.",
            r"Each triangle has two sides equal to the side of the square, with a right angle "
            r"between them.",
            r"Put the four right angles together at one point: four right angles fill the full "
            r"turn around it with no gap.",
            r"The four long sides, each a diagonal of the square, form the outside: a square "
            r"whose side is the diagonal.",
            r"It is made of the 4 triangles of two squares, so its area is double either square.",
        ], width=7.3, size=25, gap=0.14)
        slip = note("Common mistake", r"joining two triangles along their long sides. That only "
                    r"remakes one of the small squares.", width=7.3, size=24)
        ans = answer_box(r"Yes: put the four right-angle corners together at the centre; the four "
                         r"diagonals make a square with double the area", width=7.3, size=25)

        column = VGroup(work, slip, ans).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.42, 0])
        self.add(column)
