from manim import *


class MyArray(VGroup):
    def __init__(
        self,
        data=[" "],
        index_from=0,
        index_step=1,
        index_up=True,
        cell_width=1,
        cell_height=0.8,
        fs=22,
        color=BLACK,
        opacity=1,
        stroke=WHITE,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.data = data
        self.len = len(data)
        self.index_up = UP if index_up else DOWN
        self.index_from = index_from
        self.index_step = index_step
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.fs = fs
        self.color = color
        self.opacity = opacity
        self.stroke = stroke

        self.cells = VGroup()
        self.indices = VGroup()
        self.array = VGroup()

        indices = range(index_from, index_from + len(data) * index_step, index_step)

        for item in data:
            rect = Rectangle(
                width=cell_width,
                height=cell_height,
                color=color,
                fill_opacity=opacity,
                stroke_color=stroke,
            )
            label = Text(str(item), font_size=fs, z_index=1).move_to(rect.get_center())
            self.cells.add(VGroup(rect, label))
        self.cells.arrange(RIGHT, buff=0)

        for idx, index in enumerate(indices):
            idx_label = Text(str(index), font_size=fs * 0.7).next_to(
                self.cells[idx], self.index_up, buff=0.2
            )
            self.indices.add(idx_label)

        self.array.add(self.cells, self.indices)
        self.add(self.array)

    def get_cell(self, cell):
        return VGroup(self.cells[cell], self.indices[cell])

    def get_cell_rect(self, cell):
        return self.cells[cell][0]

    def get_cell_label(self, cell):
        return self.cells[cell][1]

    def get_cell_index(self, cell):
        return self.indices[cell]

    def get_cell_range(self, start, end=None):
        end = end or self.len
        return VGroup(self.get_cell(cell) for cell in range(start, end, 1))

    def highlight_cell(
        self,
        scene,
        *cells,
        colors=None,
        fill=ORANGE,
        animate=True,
        sequential=True,
        delay=0.2,
    ):
        if colors is None:
            colors = [fill] * len(cells)
        elif isinstance(colors, list):
            colors += [fill] * (len(cells) - len(colors))
        else:
            colors = [colors] * len(cells)

        animations = []
        for cell, color in zip(cells, colors):
            rect = self.get_cell_rect(cell)
            if animate:
                animations.append(rect.animate.set_fill(color))
            else:
                rect.set_fill(color)

        if animate:
            if sequential:
                for anim in animations:
                    scene.play(anim, run_time=delay)
            else:
                scene.play(*animations, run_time=delay)

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
        for cellid, label in zip(cells, labels):
            cell = self.get_cell(cellid)
            old_label = self.get_cell_label(cellid)
            new_label = Text(str(label), font_size=self.fs, z_index=1).move_to(
                self.get_cell_rect(cellid).get_center()
            )

            cellgroups.append((cellid, new_label))
            if animate:
                animations.append(AnimationGroup(FadeOut(old_label), FadeIn(new_label)))

        if animate:
            if sequential:
                for anim in animations:
                    scene.play(anim, run_time=delay)
            else:
                scene.play(*animations, run_time=delay)

        for cellid, new_label in cellgroups:
            self.cells[cellid].submobjects[1] = new_label

    def insert_cell(self, scene, pos, labels=None):
        labels_input = labels or [" "]

        rects = VGroup(
            *[
                Rectangle(
                    width=self.cell_width,
                    height=self.cell_height,
                    color=self.color,
                    fill_opacity=self.opacity,
                    stroke_color=self.stroke,
                )
                for _ in labels_input
            ]
        )
        rects.arrange(RIGHT, buff=0)

        if pos == 0:
            rects.next_to(self.get_cell_rect(0), LEFT, buff=0)
        elif pos == self.len:
            rects.next_to(self.get_cell_rect(self.len - 1), RIGHT, buff=0)
        else:
            rects.next_to(self.get_cell_rect(pos - 1), RIGHT, buff=0)
            scene.play(
                self.get_cell_range(pos).animate.shift(
                    RIGHT * self.cell_width * len(labels_input)
                )
            )
        scene.play(Write(rects))

        texts = VGroup(
            *[
                Text(str(label), font_size=self.fs, z_index=1).move_to(
                    rect.get_center()
                )
                for rect, label in zip(rects, labels_input)
            ]
        )
        scene.play(Write(texts))

        for idx, (rect, text) in enumerate(zip(rects, texts)):
            self.cells.insert(pos + idx, VGroup(rect, text))

        self.data = self.data[:pos] + labels_input + self.data[pos:]
        self.len += len(labels_input)

        indices = range(
            self.index_from,
            self.index_from + self.len * self.index_step,
            self.index_step,
        )
        index_labels = VGroup(
            *[
                Text(str(index), font_size=self.fs * 0.7).next_to(
                    cell[0], self.index_up, buff=0.2
                )
                for cell, index in zip(self.cells, indices)
            ]
        )
        for mob in self.indices:
            scene.remove(mob)
        self.indices = index_labels
        scene.add(self.indices)
        scene.add(self.indices)

    def append_cell(self, scene, labels=None):
        labels = labels or [" "]
        self.insert_cell(scene, self.len, labels=labels)

    def prepend_cell(self, scene, labels=None):
        labels = labels or [" "]
        self.insert_cell(scene, 0, labels=labels)

    def swap_cell(self, scene, cell1, cell2, delay=1.3):
        arcUp = ArcBetweenPoints(
            start=self.get_cell_rect(cell1).get_center(),
            end=self.get_cell_rect(cell2).get_center(),
            angle=-PI,
        )
        arcDown = ArcBetweenPoints(
            start=self.get_cell_rect(cell2).get_center(),
            end=self.get_cell_rect(cell1).get_center(),
            angle=-PI,
        )

        l1 = (
            self.get_cell_label(cell1)
            .copy()
            .move_to(self.get_cell_rect(cell1).get_center())
        )
        l2 = (
            self.get_cell_label(cell2)
            .copy()
            .move_to(self.get_cell_rect(cell2).get_center())
        )

        self.add(l1, l2)
        self.update_cell(scene, cell1, cell2, animate=False)

        scene.play(
            MoveAlongPath(l1, arcUp),
            MoveAlongPath(l2, arcDown),
            run_time=delay,
        )

        scene.remove(l1, l2)
        self.update_cell(scene, cell1, cell2, labels=[l2.text, l1.text], animate=False)

    def shift_cell(self, scene, start, end, to, sequential=True, delay=0.2):
        end = end - 1 if start > end else end + 1
        step = -1 if start > end else 1

        srccells = list(range(start, end, step))
        dstcells = list(range(to, to + len(srccells) * step, step))
        labels = [self.get_cell_label(cell).text for cell in srccells]

        animations = []
        for srccell, dstcell in zip(srccells, dstcells):
            animations.append(
                self.get_cell_label(srccell).animate.move_to(
                    self.get_cell_rect(dstcell).get_center()
                )
            )
        if sequential:
            for anim in animations:
                scene.play(anim, run_time=delay)
        else:
            scene.play(*animations, run_time=delay)

        self.update_cell(scene, *srccells, animate=False)
        self.update_cell(scene, *dstcells, labels=labels, animate=False)

    def swap_and_shift_cell(self, scene, swapfrom, swapto):
        arc_angle = PI if swapfrom > swapto else -PI

        arcup = ArcBetweenPoints(
            start=self.get_cell_rect(swapfrom).get_center(),
            end=self.get_cell_rect(swapto).get_center(),
            angle=arc_angle,
        )

        swapto = swapto - 1 if swapfrom > swapto else swapto + 1
        step = -1 if swapfrom > swapto else 1

        cells = range(swapfrom, swapto, step)
        srccells = range(swapfrom + step, swapto, step)
        dstcells = range(swapfrom, swapfrom + len(srccells) * step, step)

        animations = []
        for srccell, dstcell in zip(srccells, dstcells):
            animations.append(
                self.get_cell_label(srccell).animate.move_to(
                    self.get_cell_rect(dstcell).get_center()
                )
            )

        scene.play(MoveAlongPath(self.get_cell_label(swapfrom), arcup), *animations)

        labels = [self.get_cell_label(cell).text for cell in srccells]
        labels.append(self.get_cell_label(swapfrom).text)
        self.update_cell(scene, *cells, labels=labels, animate=False)
