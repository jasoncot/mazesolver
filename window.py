from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = "Jason's maze solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.geometry = f"{self.width}x{self.height}"
        # self.__root.minsize(self.width, self.height)
        # self.__root.maxsize(self.width, self.height)
        self.canvas = Canvas(self.__root)
        self.canvas.pack()
        self.is_running = False
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running == True:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

