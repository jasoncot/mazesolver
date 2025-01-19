
class Line:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end
    
    def draw(self, canvas, fill_color):
        x1 = self.__start.x
        y1 = self.__start.y

        x2 = self.__end.x
        y2 = self.__end.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)
