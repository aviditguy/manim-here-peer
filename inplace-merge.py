from manim import *
from myarray import MyArray


class InplaceMerge(Scene):
    def construct(self):
        data = [4, 5, 10, 13, 1, 3, 8, 9]
        n = len(data)
        p = 3

        arr = MyArray(data=data, cell_height=0.6, index_up=False)
        ilabel = Text("i", font_size=20).next_to(arr.get_cell(0), DOWN, buff=0.2)
        plabel = Text("p", font_size=20).next_to(arr.get_cell_rect(p), UP, buff=0.2)
        p1label = Text("p+1", font_size=20).next_to(
            arr.get_cell_rect(p + 1), UP, buff=0.2
        )
        self.add(arr, ilabel, plabel, p1label)
        self.wait(1)

        for i in range(p + 1):
            arr.highlight_cell(self, i, p + 1, fill=GOLD_E, sequential=False)
            self.wait(0.4)

            if data[i] > data[p + 1]:
                arr.swap_cell(self, i, p + 1)
                arr.highlight_cell(self, i, p + 1, fill=BLACK, animate=False)
                self.wait(0.4)

                data[i], data[p + 1] = data[p + 1], data[i]

                j = p + 2
                while j < n and data[p + 1] > data[j]:
                    j += 1

                arr.highlight_cell(
                    self,
                    *range(p + 1, j),
                    colors=[BLUE_E],
                    fill=RED_D,
                    sequential=False,
                )
                self.wait(0.4)
                arr.swap_and_shift_cell(self, p + 1, j - 1)
                self.wait(0.4)
                arr.highlight_cell(self, *range(p + 1, j), fill=BLACK, animate=False)
                self.wait(0.4)

                data.insert(j - 1, data.pop(p + 1))

            arr.highlight_cell(self, i, p + 1, fill=BLACK, animate=False)

            if i < p:
                self.play(ilabel.animate.next_to(arr.get_cell(i + 1), DOWN, buff=0.2))

        print(data)
        self.wait(2)
