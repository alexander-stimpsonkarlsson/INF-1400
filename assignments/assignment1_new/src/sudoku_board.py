from board import Board
from element import Element
from square import Square

class SudokuBoard(Board):
    def __init__(self, nums):
        super().__init__(nums)
        self.rows = []
        self.columns = []
        self.boxes = []

    def set_up_nums(self):

        row = 0
        column = 0
        
        while row < self.n_rows: 
            while column < self.n_cols: 
                new_square = Square(self.nums[row][column], None, None, None)
                self.nums[row][column] = new_square
                column += 1
            column = 0
            row += 1

    def set_up_elems(self):
        
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
    
    def reset_elements(self): 

        row = 0
        column = 0
        
        while row < self.n_rows: 
            while column < self.n_cols: 
                self.nums[row][column] = self.nums[row][column].my_number
                column += 1
            column = 0
            row += 1

    def solve(self, row, column):

        if (column == self.n_cols): 
            if (row == self.n_rows-1): 
                return True  
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
