from manim import *


class Array(VGroup):
    def __init__(
        self,
        data=None,
        dir_right=True,
        cell_width=0.9,
        cell_height=0.7,
        stroke_width=1,
        index=True,
        index_up=True,
        index_from=0,
        index_step=1,
        fs=20,
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
        self.stroke_width = stroke_width

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
                color=BLACK,
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=self.stroke_width,
            )
            label = Text(str(value), font_size=self.fs, z_index=1).move_to(
                rect.get_center()
            )
            cells.add(VGroup(rect, label))
        cells.arrange(self.dir_right, buff=self.buff)
        return cells

    def create_indices(self):
        indices = range(
            self.index_from,
            self.index_from + self.len * self.index_step,
            self.index_step,
        )
        return VGroup(
            *[
                Text(str(index), font_size=self.index_fs).next_to(
                    self.cells[idx][0], self.index_up
                )
                for idx, index in enumerate(indices)
            ]
        )

    def toggle_indices(self, scene):
        self.index = not self.index
        if self.index:
            for mob in self.indices:
                scene.remove(mob)
            self.indices = self.create_indices()
            scene.add(self.indices)
        else:
            for mob in self.indices:
                scene.remove(mob)

    def get_group(self, cell):
        return (
            VGroup(self.cells[cell], self.indices[cell])
            if self.index
            else VGroup(self.cells[cell])
        )

    def get_cell(self, cell):
        return self.get_group(cell)[0]

    def get_rect(self, cell):
        return self.get_group(cell)[0][0]

    def get_label(self, cell):
        return self.get_group(cell)[0][1]

    def get_index(self, cell):
        return self.get_group(cell)[1] if self.index else VGroup()

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
            oldval = self.get_label(cell)
            newval = Text(str(label), font_size=self.fs, z_index=1).move_to(
                self.get_rect(cell).get_center()
            )

            self.data[cell] = label

            cellgroups.append((cell, newval))
            if animate:
                animations.append(AnimationGroup(FadeOut(oldval), FadeIn(newval)))

        if animate:
            if sequential:
                for anim in animations:
                    scene.play(anim, run_time=delay)
            else:
                scene.play(*animations, run_time=delay)

        for cell, newval in cellgroups:
            self.cells[cell].submobjects[1] = newval

        scene.add(self)

    def highlight_cell(
        self,
        scene,
        *cells,
        colors=None,
        fill=GOLD_D,
        animate=True,
        sequential=True,
        delay=0.2,
    ):
        colors = colors or []
        colors += [fill] * (len(cells) - len(colors))

        animations = []
        for cell, color in zip(cells, colors):
            rect = self.get_rect(cell)[0]
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

    def insert_cell(self, scene, pos, values=None, delay=1):
        values = values or [" "]
        cells = self.create_cells(values)

        if pos == 0:
            cells.next_to(self.get_rect(0), LEFT, buff=self.buff)
        elif pos == self.len:
            cells.next_to(self.get_rect(pos - 1), RIGHT, buff=self.buff)
        else:
            cells.next_to(
                self.get_cell_item(pos - 1, item="rect"), RIGHT, buff=self.buff
            )
            cellgrp = VGroup(self.get_group(cell) for cell in range(pos, self.len))
            scene.play(cellgrp.animate.shift(RIGHT * self.cell_width * len(values)))

        scene.play(Write(cells), run_time=delay)

        self.cells[pos:pos] = cells
        self.data[pos:pos] = values
        self.len += len(values)

        if self.index:
            self.toggle_indices(scene)
            self.toggle_indices(scene)

    def append_cell(self, scene, values=None, delay=1):
        self.insert_cell(scene, pos=self.len, values=values, delay=delay)

    def prepend_cell(self, scene, values=None, delay=1):
        self.insert_cell(scene, pos=0, values=values, delay=delay)

    def remove_cell(self, scene, *cells, delay=1):
        cells = sorted(cells, reverse=True)

        for cell in cells:
            item = self.get_group(cell)

            scene.play(FadeOut(item))

            cellitems = VGroup(
                self.get_group(citm) for citm in range(cell + 1, self.len)
            )
            scene.play(cellitems.animate.shift(LEFT * self.cell_width))

            for mob in item:
                scene.remove(mob)

            self.cells.remove(self.cells[cell])
            self.indices.remove(self.indices[cell])
            del self.data[cell]
            self.len -= 1

        if self.index:
            self.toggle_indices(scene)
            self.toggle_indices(scene)

    def swap_cell(self, scene, cell1, cell2, delay=1.5):
        arcup = ArcBetweenPoints(
            start=self.get_rect(cell1).get_center(),
            end=self.get_rect(cell2).get_center(),
            angle=-PI,
        )
        arcdown = ArcBetweenPoints(
            start=self.get_rect(cell2).get_center(),
            end=self.get_rect(cell1).get_center(),
            angle=-PI,
        )

        l1 = self.get_label(cell1)
        l2 = self.get_label(cell2)

        scene.play(MoveAlongPath(l1, arcup), MoveAlongPath(l2, arcdown), run_time=delay)
        self.update_cell(scene, cell1, cell2, labels=[l2.text, l1.text], animate=False)

    def shift_cell(self, scene, start, end, to, sequential=True, delay=0.5):
        end = end - 1 if start > end else end + 1
        step = -1 if start > end else 1

        srccells = range(start, end, step)
        dstcells = range(to, to + len(srccells) * step, step)
        cells = range(to, end, step)
        labels = [self.get_label(cell).text for cell in srccells]

        animations = []
        for srccell, dstcell in zip(srccells, dstcells):
            animations.append(
                self.get_label(srccell).animate.move_to(
                    self.get_rect(dstcell).get_center()
                )
            )

        if sequential:
            for anim in animations:
                scene.play(anim, run_time=delay)
        else:
            scene.play(*animations, run_time=delay)

        self.update_cell(scene, *cells, labels=labels, animate=False)

    def swap_and_shift_cell(self, scene, swapfrom, swapto):
        arc_angle = PI if swapfrom > swapto else -PI

        arcup = ArcBetweenPoints(
            start=self.get_rect(swapfrom).get_center(),
            end=self.get_rect(swapto).get_center(),
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
                self.get_label(srccell).animate.move_to(
                    self.get_rect(dstcell).get_center()
                )
            )

        scene.play(MoveAlongPath(self.get_label(swapfrom), arcup), *animations)

        labels = [self.get_label(cell).text for cell in srccells]
        labels.append(self.get_label(swapfrom).text)
        self.update_cell(scene, *cells, labels=labels, animate=False)



class BitArray(VGroup):
    def __init__(
        self,
        integer,
        bits=None,
        cell_width=0.9,
        cell_height=0.7,
        stroke_width=1,
        index=True,
        index_up=True,
        fs=20,
        buff=0,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.integer = integer
        self.bits = bits or len(format(integer, "b"))
        self.data = list(format(self.integer, f"0{self.bits}b"))
        self.fs = fs
        self.buff = buff

        self.cell_width = cell_width
        self.cell_height = cell_height
        self.stroke_width = stroke_width

        self.index = index
        self.index_up = UP if index_up else DOWN

        self.cells = self.create_bits()
        self.indices = self.create_indices()
        self.bitarray = (
            VGroup(self.cells, self.indices) if self.index else VGroup(self.cells)
        )
        self.add(self.bitarray)

    def create_bits(self):
        bits = VGroup()
        for bitdata in self.data:
            rect = Rectangle(
                width=self.cell_width,
                height=self.cell_height,
                color=BLACK,
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=self.stroke_width,
            )
            label = Text(str(bitdata), font_size=self.fs, z_index=1).move_to(
                rect.get_center()
            )
            bits.add(VGroup(rect, label))
        return bits.arrange(RIGHT, buff=self.buff)

    def create_indices(self):
        indices = VGroup()
        for idx, index in enumerate(range(self.bits - 1, -1, -1)):
            indices.add(
                Text(str(index), font_size=self.fs * 0.7).next_to(
                    self.cells[idx], self.index_up
                )
            )
        return indices

    def toggle_indices(self, scene):
        self.index = not self.index
        for mob in self.indices:
            scene.remove(mob)
        if self.index:
            scene.add(self.indices)

    def get_group(self, bit):
        bit = self.bits - bit - 1
        if self.index:
            return VGroup(self.cells[bit], self.indices[bit])
        else:
            return VGroup(self.cells[bit])

    def get_cell(self, bit):
        return self.get_group(bit)[0]

    def get_rect(self, bit):
        return self.get_group(bit)[0][0]

    def get_label(self, bit):
        return self.get_group(bit)[0][1]

    def get_index(self, bit):
        return self.get_group(bit)[1]

    def highlight_cell(
        self,
        scene,
        *bits,
        colors=None,
        fill=ORANGE,
        animate=True,
        sequential=True,
        delay=0.2,
    ):
        colors = colors or []
        colors += [fill] * (len(bits) - len(colors))

        animations = []
        for bit, color in zip(bits, colors):
            if animate:
                animations.append(self.get_rect(bit).animate.set_fill(color))
            else:
                self.get_rect(bit).set_fill(color)

        if animate and sequential:
            for anim in animations:
                scene.play(anim, run_time=delay)
        elif animate and not sequential:
            scene.play(*animations, run_time=delay)

    def update_cell(
        self,
        scene,
        *bits,
        labels=None,
        fill="0",
        animate=True,
        sequential=True,
        delay=0.2,
    ):
        labels = labels or []
        labels += [fill] * (len(bits) - len(labels))

        animations = []
        bitgroups = []
        for bit, label in zip(bits, labels):
            oldval = self.get_label(bit)
            newval = Text(str(label), font_size=self.fs, z_index=1).move_to(
                self.get_rect(bit).get_center()
            )

            bitgroups.append((bit, newval))
            if animate:
                animations.append(AnimationGroup(FadeOut(oldval), FadeIn(newval)))

        if animate and sequential:
            for anim in animations:
                scene.play(anim, run_time=delay)
        elif animate and not sequential:
            scene.play(*animations, run_time=delay)

        for bit, newval in bitgroups:
            bit = self.bits - bit - 1
            self.cells[bit].submobjects[1] = newval

    def left_shift(self, scene, n=1):
        self.integer <<= n
        self.data = self.data[n:] + [0] * n

        cells = VGroup(*[self.get_label(idx) for idx in range(0, self.bits)])
        scene.play(cells.animate.shift(LEFT * n * self.cell_width))
        labels = [self.get_label(idx).text for idx in range(self.bits - n - 1, -1, -1)]
        self.update_cell(scene, *range(self.bits - 1, -1, -1), labels=labels, fill="0")

    def right_shift(self, scene, n=1):
        self.integer >>= n
        self.data = [0] * n + self.data[: self.bits - n]

        cells = VGroup(*[self.get_label(idx) for idx in range(0, self.bits)])
        scene.play(cells.animate.shift(RIGHT * n * self.cell_width))
        labels = [self.get_label(idx).text for idx in range(n, self.bits)]
        self.update_cell(scene, *range(0, self.bits), labels=labels, fill="0")

    def bitwise_and(self, scene, n, delay=1.8):
        self.integer &= n
        self.data = list(format(self.integer, f"0{self.bits}b"))
        cells = self.create_bits()
        scene.play(Transform(self.cells, cells), run_time=delay)

    def bitwise_or(self, scene, n, delay=1.8):
        self.integer |= n
        self.data = list(format(self.integer, f"0{self.bits}b"))
        cells = self.create_bits()
        scene.play(Transform(self.cells, cells), run_time=delay)

    def bitwise_xor(self, scene, n, delay=1.8):
        self.integer ^= n
        self.data = list(format(self.integer, f"0{self.bits}b"))
        cells = self.create_bits()
        scene.play(Transform(self.cells, cells), run_time=delay)

    def bitwise_not(self, scene, delay=1.8):
        self.integer = ~self.integer & ((1 << self.bits) - 1)
        self.data = list(format(self.integer, f"0{self.bits}b"))
        cells = self.create_bits()
        scene.play(Transform(self.cells, cells), run_time=delay)
