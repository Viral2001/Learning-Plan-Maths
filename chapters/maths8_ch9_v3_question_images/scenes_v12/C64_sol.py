from _style import *


class C64_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Triples, Q3"))

        table = grid_table([
            [r"Triple", r"Gaps from hypotenuse"],
            ["(8, 15, 17)", "9 and 2"],
            ["(20, 21, 29)", "9 and 8"],
            ["(12, 35, 37)", "25 and 2"],
        ], widths=[2.1, 3.4], row_h=0.66, size=26, colours={1: AMBER})
        table.move_to([LEFT_EDGE + table.width / 2, -0.2, 0])
        self.add(table)

        work = steps([
            r"The method gives only triples in which the hypotenuse is 1 more than a side.",
            r"$(8, 15, 17)$: $8^2 + 15^2 = 64 + 225 = 289 = 17^2$, no common factor, and "
            r"$17 - 15 = 2$, $17 - 8 = 9$.",
            r"$(20, 21, 29)$: $20^2 + 21^2 = 400 + 441 = 841 = 29^2$, with gaps 9 and 8.",
            r"$(12, 35, 37)$: $12^2 + 35^2 = 144 + 1225 = 1369 = 37^2$, with gaps 25 and 2.",
            r"In none of them is the hypotenuse 1 more than a side, so the method misses them.",
        ], width=7.4, size=25, gap=0.12)
        ans = answer_box(r"Yes: for example $(8, 15, 17)$, $(20, 21, 29)$ and $(12, 35, 37)$",
                         width=7.4, size=25, pad=0.24)
        slip = note("Common mistake", r"thinking the method gives every primitive triple. "
                    r"$(20, 21, 29)$ is primitive, but its gaps are 9 and 8.", width=7.4, size=25)

        column = VGroup(work, ans, slip).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        column.move_to([RIGHT_EDGE - column.width / 2, -0.4, 0])
        self.add(column)
