from _style import *


class C62_sol(Scene):
    def construct(self):
        self.add(header("Solution", r"Triples, Q1"))

        rule = para(r"Use $(n - 1)^2 + (2n - 1) = n^2$. Take the next odd squares after 9 and 25: "
                    r"49, 81, 121, 169 and 225. Write each as $2n - 1$ to find $n$.",
                    width=13.2, size=27)
        rule.move_to([0, 2.72, 0])
        self.add(rule)

        rows = [["Odd square", r"Written as $2n - 1$", "$n$", r"$(n - 1)^2 + (2n - 1) = n^2$", "Triple"]]
        for odd, root, n in ((49, 7, 25), (81, 9, 41), (121, 11, 61), (169, 13, 85), (225, 15, 113)):
            rows.append([r"$%d = %d^2$" % (odd, root), r"$%d = 2 \times %d - 1$" % (odd, n), "$%d$" % n,
                         r"$%d^2 + %d^2 = %d + %d = %d = %d^2$"
                         % (n - 1, root, (n - 1) ** 2, odd, n ** 2, n),
                         "(%d, %d, %d)" % (root, n - 1, n)])
        table = grid_table(rows, [2.0, 3.0, 0.9, 5.0, 2.3], row_h=0.58, size=26, colours={4: TEAL})
        table.move_to([0, 0.5, 0])
        self.add(table)

        slip = note("Common mistake", r"taking any odd number, such as 11. It works only when "
                    r"$2n - 1$ is itself a square number.", width=13.2, size=24)
        ans = answer_box(r"(7, 24, 25), (9, 40, 41), (11, 60, 61), (13, 84, 85), (15, 112, 113)",
                         width=13.2, size=32)
        column = VGroup(slip, ans).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        column.move_to([0, -2.72, 0])
        self.add(column)
