from sudoku_board import SudokuBoard
from sudoku_reader import SudokuReader

if __name__ == "__main__":

    reader = SudokuReader("sudoku_10.csv")
    solved = 0
    while reader.current_line < reader.total_lines: 
        board = SudokuBoard(reader.next_board())
        print(board)
        board._set_up_nums()
        board._set_up_elems()
        board.solve(0, 0)
        board._reset_elements()
        print(board)
        reader.current_line += 1
        solved += 1
        print("Solved:", solved)