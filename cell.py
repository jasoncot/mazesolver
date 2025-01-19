from line import Line
from point import Point

class Cell:
    def __init__(
            self,
            has_left_wall=False,
            has_right_wall=False,
            has_top_wall=False,
            has_bottom_wall=False,
            x1=None,
            x2=None,
            y1=None,
            y2=None,
            win=None
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def set_all_walls(self):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, upper_left=None, lower_right=None):
        if upper_left != None and lower_right != None:
            self._x1 = upper_left.x
            self._y1 = upper_left.y
            self._x2 = lower_right.x
            self._y2 = lower_right.y

        if self._x1 == None:
            raise Exception("coordinates are not set")

        lower_left = Point(self._x1, self._y2)
        upper_right = Point(self._x2, self._y1)

        if self.has_left_wall == True:
            self._win.draw_line(Line(upper_left, lower_left), "black")

        if self.has_right_wall == True:
            self._win.draw_line(Line(upper_right, lower_right), "black")

        if self.has_top_wall == True:
            self._win.draw_line(Line(upper_left, upper_right), "black")

        if self.has_bottom_wall == True:
            self._win.draw_line(Line(lower_left, lower_right), "black")
    
    def draw_move(self, to_cell, undo=False):
        x_center = (self._x2 + self._x1) / 2
        y_center = (self._y2 + self._y1) / 2

        to_x_center = (to_cell._x2 + to_cell._x1) / 2
        to_y_center = (to_cell._y2 + to_cell._y1) / 2

        line = Line(Point(x_center, y_center), Point(to_x_center, to_y_center))
        color = "red"
        if undo == True:
            color = "gray"
        
        self._win.draw_line(line, color)