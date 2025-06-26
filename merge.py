from manim import *
from myarray import MyArray


class Merge(Scene):
    def construct(self):
        d1 = [1, 3, 5, 7]
        n1 = len(d1)

        d2 = [2, 4, 6, 8, 10]
        n2 = len(d2)

        d3 = [" " for _ in range(n1 + n2)]
        n3 = len(d3)

        arr1 = MyArray(data=d1, cell_height=0.6).shift(UP * 2).shift(LEFT * 2)
        arr2 = MyArray(data=d2, cell_height=0.6).next_to(
            arr1, DOWN, buff=0.5, aligned_edge=LEFT
        )
        arr3 = MyArray(data=d3, cell_height=0.6).next_to(
            arr2, DOWN, buff=0.5, aligned_edge=LEFT
        )

        ilabel = Text("i", font_size=20).next_to(arr1.get_cell_rect(0), UP, buff=0.2)
        jlabel = Text("j", font_size=20).next_to(arr2.get_cell_rect(0), UP, buff=0.2)
        klabel = Text("k", font_size=20).next_to(arr3.get_cell_rect(0), UP, buff=0.2)

        self.add(arr1.cells, arr2.cells, arr3.cells, ilabel, jlabel, klabel)
        self.wait(1)

        i, j, k = 0, 0, 0
        while i < n1 and j < n2:
            arr1.highlight_cell(self, i, fill=RED_D)
            arr2.highlight_cell(self, j, fill=BLUE_D)
            self.wait(0.5)

            if d1[i] < d2[j]:
                arr1.highlight_cell(self, i, fill=GREEN_D)
                arr2.highlight_cell(self, j, fill=BLACK, animate=False)
                self.wait(0.5)
                arr3.update_cell(self, k, fill=d1[i])
                self.wait(0.5)
                arr1.highlight_cell(self, i, fill=BLACK, animate=False)
                self.wait(0.5)

                d3[k] = d1[i]
                i += 1
                k += 1

                if i < n1:
                    self.play(
                        ilabel.animate.next_to(arr1.get_cell_rect(i), UP, buff=0.2),
                        klabel.animate.next_to(arr3.get_cell_rect(k), UP, buff=0.2),
                    )
            else:
                arr2.highlight_cell(self, j, fill=GREEN_D)
                arr1.highlight_cell(self, i, fill=BLACK, animate=False)
                self.wait(0.5)
                arr3.update_cell(self, k, fill=d2[j])
                self.wait(0.5)
                arr2.highlight_cell(self, j, fill=BLACK, animate=False)
                self.wait(0.5)

                d3[k] = d2[j]
                j += 1
                k += 1

                if j < n2:
                    self.play(
                        jlabel.animate.next_to(arr2.get_cell_rect(j), UP, buff=0.2),
                        klabel.animate.next_to(arr3.get_cell_rect(k), UP, buff=0.2),
                    )

        while i < n1:
            arr1.highlight_cell(self, i, fill=GREEN_D)
            self.wait(0.5)
            arr3.update_cell(self, k, fill=d1[i])
            self.wait(0.5)
            arr1.highlight_cell(self, i, fill=BLACK, animate=False)
            self.wait(0.5)

            d3[k] = d1[i]
            i += 1
            k += 1

            if i < n1:
                self.play(
                    ilabel.animate.next_to(arr1.get_cell_rect(i), UP, buff=0.2),
                    klabel.animate.next_to(arr3.get_cell_rect(k), UP, buff=0.2),
                )

        while j < n2:
            arr2.highlight_cell(self, j, fill=GREEN_D)
            self.wait(0.5)
            arr3.update_cell(self, k, fill=d2[j])
            self.wait(0.5)
            arr2.highlight_cell(self, j, fill=BLACK, animate=False)
            self.wait(0.5)

            d3[k] = d2[j]
            j += 1
            k += 1

            if j < n2:
                self.play(
                    jlabel.animate.next_to(arr2.get_cell_rect(j), UP, buff=0.2),
                    klabel.animate.next_to(arr3.get_cell_rect(k), UP, buff=0.2),
                )

        self.wait(2)
