from cell import Cell

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win


        def __create_cells(self):
            self.__cells = []

            for i in range(self.__num_cols):
                col = []
                for j in range(self.__num_rows):
                    col.append(Cell(self.__win))

        def __draw_cell(self, i, j):
            pass

        def __animate(self):
            pass
