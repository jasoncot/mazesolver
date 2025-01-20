from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(5, 5, 10, 10, 20, 20, win, 0)
    maze._create_cells()
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()
    win.wait_for_close()

if __name__ == "__main__":
    main()