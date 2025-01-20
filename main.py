from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    width = 800
    height = 600
    win = Window(width, height)
    cell_x_size = 30
    cell_y_size = 30

    num_cols = (height - 10)  // cell_y_size
    num_rows = (width - 10) // cell_x_size

    maze = Maze(5, 5, num_rows, num_cols, cell_x_size, cell_y_size, win, 0)
    maze._create_cells()
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()
    maze.solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()