from manim import *


class Grid(VGroup):
    def __init__(
        self,
        width=6,
        height=7,
        data=None,
        fs=24,
        color=BLACK,
        opacity=1,
        stroke=WHITE,
        hbuff=0,
        vbuff=0,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.data = data or [[" "]]
        self.rows = len(data)
        self.cols = len(data[0])
        self.cell_width = width / self.cols
        self.cell_height = height / self.rows
        self.fs = fs
        self.color = color
        self.opacity = opacity
        self.stroke = stroke
        self.hbuff = hbuff
        self.vbuff = vbuff

        self.grid = VGroup()

        for data_row in data:
            grid_row = VGroup()
            for cell in data_row:
                rect = Rectangle(
                    width=self.cell_width,
                    height=self.cell_height,
                    color=color,
                    fill_opacity=opacity,
                    stroke_color=stroke,
                )
                label = Text(str(cell), font_size=fs, z_index=1).move_to(
                    rect.get_center()
                )
                grid_row.add(VGroup(rect, label))
            grid_row.arrange(RIGHT, buff=hbuff)
            self.grid.add(grid_row)
        self.grid.arrange(DOWN, buff=vbuff)
        self.add(self.grid)

    def get_cell(self, row, col):
        return self.grid[row][col]

    def get_cell_rect(self, row, col):
        return self.get_cell(row, col)[0]

    def get_cell_label(self, row, col):
        return self.get_cell(row, col)[1]

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
        if colors == None:
            colors = [fill] * len(cells)
        elif isinstance(colors, list):
            colors = colors + [fill] * (len(cells) - len(colors))
        else:
            colors = [colors] * len(cells)

        animations = []
        for color, (row, col) in zip(colors, cells):
            cell = self.get_cell_rect(row, col)
            if animate:
                animations.append(cell.animate.set_fill(color))
            else:
                cell.set_fill(color)

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
        for label, (row, col) in zip(labels, cells):
            cell = self.get_cell(row, col)
            old_val = self.get_cell_label(row, col)
            new_val = Text(str(label), font_size=self.fs, z_index=1).move_to(
                self.get_cell_rect(row, col).get_center()
            )

            cellgroups.append((cell, old_val, new_val))
            if animate:
                animations.append(AnimationGroup(FadeOut(old_val), FadeIn(new_val)))

        if animate:
            if sequential:
                for anim in animations:
                    scene.play(anim, run_time=delay)
            else:
                scene.play(*animations, run_time=delay)

        for cell, old_val, new_val in cellgroups:
            cell.remove(old_val)
            cell.add(new_val)

            scene.remove(old_val)
            scene.add(new_val)
