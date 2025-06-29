from manim import *


class Array(VGroup):
    def __init__(
        self,
        data=None,
        cell_width=0.9,
        cell_height=0.7,
        fs=22,
        dir_right=True,
        index=True,
        index_from=0,
        index_step=1,
        index_up=True,
        color=BLACK,
        opacity=1,
        stroke_color=WHITE,
        stroke_width=1,
        buff=0,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.data = data or [" "]
        self.len = len(self.data)
        self.fs = fs
        self.index_fs = fs * 0.7
        self.buff = buff

        self.cell_width = cell_width
        self.cell_height = cell_height
        self.cell_color = color
        self.cell_opacity = opacity
        self.cell_stroke_color = stroke_color
        self.cell_stroke_width = stroke_width

        self.index = index
        self.index_from = index_from
        self.index_step = index_step

        self.dir_right = RIGHT if dir_right else UP

        if dir_right:
            self.index_up = UP if index_up else DOWN
        else:
            self.index_up = RIGHT if index_up else LEFT

        self.cells = self.create_cells(self.data)
        self.indices = self.create_indices()

        if index:
            self.array = VGroup(self.cells, self.indices)
        else:
            self.array = VGroup(self.cells)

        self.add(self.array)

    def create_cells(self, values):
        cells = VGroup()
        for value in values:
            rect = Rectangle(
                width=self.cell_width,
                height=self.cell_height,
                fill_color=self.cell_color,
                fill_opacity=self.cell_opacity,
                stroke_color=self.cell_stroke_color,
                stroke_width=self.cell_stroke_width,
            )
            label = Text(str(value), font_size=self.fs, z_index=1).move_to(
                rect.get_center()
            )
            cells.add(VGroup(rect, label))
        cells.arrange(self.dir_right, buff=self.buff)
        return cells

    def create_indices(self):
        indexes = range(
            self.index_from,
            self.index_from + self.len * self.index_step,
            self.index_step,
        )

        return VGroup(
            *[
                Text(str(index), font_size=self.index_fs).next_to(
                    self.cells[idx][0], self.index_up, buff=0.2
                )
                for idx, index in enumerate(indexes)
            ]
        )

    def toggleIndices(self, scene):
        self.index = not self.index
        if self.index:
            scene.add(self.indices)
        else:
            scene.remove(self.indices)

    def get_cell_item(self, *cells, item=None):
        if item not in {"group", "cell", "rect", "label", "index"}:
            item = "cell"

        if item == "group" and not self.index:
            item = "cell"

        if item == "group":
            return VGroup(
                *(VGroup(self.cells[cell], self.indices[cell]) for cell in cells)
            )
        elif item == "cell":
            return VGroup(*(self.cells[cell] for cell in cells))
        elif item == "rect":
            return VGroup(*(self.cells[cell][0] for cell in cells))
        elif item == "label":
            return VGroup(*(self.cells[cell][1] for cell in cells))
        elif item == "index" and self.index:
            return VGroup(*(self.indices[cell] for cell in cells))

    def update_cell(
        self,
        scene,
        *cells,
        labels=None,
        fill=" ",
        animate=True,
        sequential=True,
        delay=0.2,
    ):
        labels = labels or []
        labels += [fill] * (len(cells) - len(labels))

        animations = []
        cellgroups = []
        for cell, label in zip(cells, labels):
            oldlabel = self.get_cell_item(cell, item="label")
            newlabel = Text(str(label), font_size=self.fs, z_index=1).move_to(
                self.get_cell_item(cell, item="rect").get_center()
            )

            cellgroups.append((cell, newlabel))
            if animate:
                animations.append(AnimationGroup(FadeOut(oldlabel), FadeIn(newlabel)))

        if animate:
            if sequential:
                for anim in animations:
                    scene.play(anim, run_time=delay)
            else:
                scene.play(*animations, run_time=delay)

        for cell, newlabel in cellgroups:
            self.cells[cell].submobjects[1] = newlabel
