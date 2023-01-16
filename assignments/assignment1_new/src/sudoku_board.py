from board import Board
from sudoku_reader import Sudoku_reader
from element import Element
from square import Square


class SudokuBoard(Board):
    def __init__(self, nums):
        super().__init__(nums)
        self.squares = []
        for _ in nums:
            square = Square()
            self.squares.append(square)
