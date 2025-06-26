from manim import *
from myarray import MyArray


class ShellSort(Scene):
    def construct(self):
        data = [3, 22, 14, -1, 31, 10, 7, 1]
        n = len(data)
        gap = n // 2

        arr = MyArray(data=data, cell_height=0.6, index_up=False)
        gaplabel = Text("g", font_size=20).next_to(arr.get_cell(gap), UP, buff=0.2)
        ilabel = Text("i", font_size=20).next_to(arr.get_cell(gap), DOWN, buff=0.2)
        jlabel = Text("j", font_size=20).next_to(arr.get_cell(gap), DOWN, buff=0.2)
        self.add(arr.cells, gaplabel, ilabel, jlabel)

        while gap > 0:
            for i in range(gap, n):
                temp = data[i]
                j = i
                while j >= gap and data[j - gap] > temp:
                    data[j] = data[j - gap]
                    j -= gap
                data[j] = temp
            gap //= 2

        print(data)
        self.wait(2)
