from window import Window, Line, Point

def main():
    win = Window(800, 600)

    line1 = Line(Point(1, 100), Point(100, 200))
    win.draw_line(line1, "red")
    win.wait_for_close()

main()