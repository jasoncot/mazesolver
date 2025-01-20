import time
from cell import Cell
from point import Point
import random

UP_DIR = (-1, 0)
DOWN_DIR = (1, 0)
LEFT_DIR = (0, -1)
RIGHT_DIR = (0, 1)

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = None
        if seed != None:
            random.seed(seed)

        self._create_cells()

    def _create_cells(self):
        self._cells = []

        def add_columns_to_row(row):
            cell = Cell()
            cell.set_all_walls()
            cell._win = self.win
            row.append(cell)

        for i in range(self.num_cols):
            self._cells.append([])

            for j in range(self.num_rows):
                add_columns_to_row(self._cells[i])

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        cell = self._cells[i][j]

        upper_left = Point(
            self.x1 + j * self.cell_size_x,
            self.y1 + i * self.cell_size_y
        )

        lower_right = Point(
            self.x1 + (j + 1) * self.cell_size_x,
            self.y1 + (i + 1) * self.cell_size_y
        )

        cell.draw(upper_left, lower_right)
        self._animate()

    def _animate(self):
        if self.win == None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        # entrance is at 0,0
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._animate()

        exit_i = self.num_cols - 1
        exit_j = self.num_rows - 1
        self._cells[exit_i][exit_j].has_bottom_wall = False
        self._draw_cell(exit_i, exit_j)
        self._animate()

    def _break_walls_r(self, i, j):
        cell = self._cells[i][j]
        cell.visited = True

        while True:
            to_visit = []

            # up case
            if i > 0 and self._cells[i - 1][j].visited == False:
                to_visit.append(UP_DIR)
            
            # right case
            if j < (self.num_rows - 1) and self._cells[i][j + 1].visited == False:
                to_visit.append(RIGHT_DIR)

            # down case
            if i < (self.num_cols - 1) and self._cells[i + 1][j].visited == False:
                to_visit.append(DOWN_DIR)

            # left case
            if j > 0 and self._cells[i][j - 1].visited == False:
                to_visit.append(LEFT_DIR)

            if len(to_visit) == 0:
                cell.draw()
                return
            
            value = random.randrange(0, len(to_visit), 1)
            selected = to_visit[value]
            if selected == LEFT_DIR:
                cell.has_left_wall = False
                self._cells[i][j-1].has_right_wall = False
                cell.draw()
                self._break_walls_r(i, j-1)

            if selected == RIGHT_DIR:
                cell.has_right_wall = False
                self._cells[i][j+1].has_left_wall = False
                cell.draw()
                self._break_walls_r(i, j+1)

            if selected == UP_DIR:
                cell.has_top_wall = False
                self._cells[i-1][j].has_bottom_wall = False
                cell.draw()
                self._break_walls_r(i-1, j)

            if selected == DOWN_DIR:
                cell.has_bottom_wall = False
                self._cells[i+1][j].has_top_wall = False
                cell.draw()
                self._break_walls_r(i+1, j)

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False
