from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Solver")
        self.__canvas = Canvas(self.__root, height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)
    

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.pt1 = point1
        self.pt2 = point2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, fill=fill_color, width=2)


