from sudoku_reader import SudokuReader
from element import Element
from square import Square


class Board:
    # It is your task to subclass this in order to make it more fit
    # to be a sudoku board

    def __init__(self, nums):
        # Nums parameter is a 2D list, like what the sudoku_reader returns
        self.n_rows = len(nums[0])
        self.n_cols = len(nums)
        self.nums = [[nums[y][x] for x in range(self.n_rows)]
                     for y in range(self.n_cols)]
        self.rows = []
        self.columns = []
        self.boxes = []


    def _set_up_nums(self):

        row = 0
        column = 0
        
        while row < self.n_rows: 
            while column < self.n_cols: 
                new_square = Square(self.nums[row][column], None, None, None)
                self.nums[row][column] = new_square
                column += 1
            column = 0
            row += 1

    def _set_up_elems(self):
        
        for _ in range(9): 
            new_row = Element("row")
            self.rows.append(new_row)
            new_column = Element("column")
            self.columns.append(new_column)
            new_box = Element("box")
            self.boxes.append(new_box)

        row = 0
        column = 0

        while row < self.n_rows: 

            while column < self.n_cols: 

                self.rows[row].add_square(self.nums[row][column])
                self.columns[column].add_square(self.nums[row][column])
                box = int((int(column) / 3)) + 3 * int((int(row) / 3))
                self.boxes[box].add_square(self.nums[row][column])
                
                self.nums[row][column].my_row = self.rows[row]
                self.nums[row][column].my_column = self.columns[column]
                self.nums[row][column].my_box = self.boxes[box]

                column += 1
                
            column = 0
            row += 1
    
    def _reset_elements(self): 

        row = 0
        column = 0
        
        while row < self.n_rows: 
            while column < self.n_cols: 
                self.nums[row][column] = self.nums[row][column].my_number
                column += 1
            column = 0
            row += 1

    def solve(self, row, column):

        if (row == 8 and column == 9): 
            return True 
    
        if column == 9: 
            row += 1
            column = 0

        if self.nums[row][column].my_number > 0: 
            return self.solve(row, column + 1)
        
        for number in range(1, 10, 1): 
            if self.nums[row][column].is_legal(number): 
                self.nums[row][column].set_number(number)
                if self.solve(row, column + 1): 
                    return True
            self.nums[row][column].set_number(0)
        return False

    # Makes it possible to print a board in a sensible format
    def __str__(self):
        r = "Board with " + str(self.n_rows) + \
            " rows and " + str(self.n_cols) + " columns:\n"
        r += "[["
        for num in self.nums:
            for elem in num:
                r += elem.__str__() + ", "
            r = r[:-2] + "]" + "\n ["
        r = r[:-3] + "]"
        return r
