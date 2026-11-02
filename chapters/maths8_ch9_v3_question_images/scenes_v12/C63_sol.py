from _style import *


class C63_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Triples, Q2"))

        table = grid_table([
            [r"Odd square", r"Root", r"$n - 1$", r"$n$"],
            ["9", "3", "4", "5"],
            ["25", "5", "12", "13"],
            ["49", "7", "24", "25"],
            ["81", "9", "40", "41"],
        ], widths=[1.9, 0.9, 1.0, 0.9], row_h=0.62, size=28, colours={2: TEAL, 3: TEAL})
        table.move_to([LEFT_EDGE + table.width / 2, -0.3, 0])
        self.add(table)

        work = steps([
            r"Every triple from the method has the form (the root of the odd square, $n - 1$, $n$).",
            r"Any common factor of $n - 1$ and $n$ also divides their difference, which is 1.",
            r"So $n - 1$ and $n$ share no factor greater than 1, and neither can the whole triple.",
        ], width=7.0, size=28)
        slip = note("Common mistake", r"thinking $(6, 8, 10)$ comes from this method. Its hypotenuse "
                    r"is 2 more than a side, not 1.", width=7.0)
        ans = answer_box(r"No: every triple the method gives is primitive", width=7.0, size=28)

        column = VGroup(work, slip, ans).arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.4, 0])
        self.add(column)
