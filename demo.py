from manim import *
from grid import Grid
from myarray import MyArray


class Demo(Scene):
    def construct(self):
        data = [5, 10, 15, 20, 25]
        arr = MyArray(data=data)
        self.add(arr)
        self.wait(1)

        # s1, m = ("cat", len("cat"))
        # s2, n = ("cut", len("cut"))
        #
        # d = [
        #     [i + j if i == 0 or j == 0 else " " for j in range(n + 1)]
        #     for i in range(m + 1)
        # ]
        #
        # grid = Grid(data=d, height=4)
        #
        # s1labels = VGroup(
        #     *[
        #         Text(char, font_size=28).next_to(
        #             grid.get_cell_rect(i + 1, 0), LEFT, buff=0.4
        #         )
        #         for i, char in enumerate(s1)
        #     ]
        # )
        #
        # s2labels = VGroup(
        #     *[
        #         Text(char, font_size=28).next_to(
        #             grid.get_cell_rect(0, i + 1), UP, buff=0.4
        #         )
        #         for i, char in enumerate(s2)
        #     ]
        # )
        #
        # self.add(grid, s1labels, s2labels)
        #
        # self.wait(2)
