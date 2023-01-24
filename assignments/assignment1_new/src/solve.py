from sudoku_board import SudokuBoard
from sudoku_reader import SudokuReader
import time as t
import sys

if __name__ == "__main__":

    try: 
        reader = SudokuReader("sudoku_files/"+sys.argv[1])
    except: 
        print("Error: Provide sudoku file (python3 solve.py 'your_file.csv')")
        sys.exit()
    solved = 0
    start = t.time()
    while reader.current_line < reader.total_lines: 
        board = SudokuBoard(reader.next_board())
        board._set_up_nums()
        board._set_up_elems()
        board.solve(0, 0)
        board._reset_elements()
        reader.current_line += 1
        solved += 1
    end = t.time()
    print("Solved:", solved, "Performance:", "{}s".format(end-start))