
class SudokuReader:

    def __init__(self, filename):
        self.file = open(filename, "r")
        self.current_line = 0
        self.total_lines = sum(1 for line in open(filename))

    # Returns a 2D list (9*9) of ints
    def next_board(self):
        try:
            board_txt = self.file.readline()
            board = [[0 for _ in range(9)] for _ in range(9)]
            sym_num = 0
            for i in range(9):
                for j in range(9):
                    board[i][j] = int(board_txt[sym_num])
                    sym_num += 1
            return board
        except:
            print("Reading error")
            quit(-1)


if __name__ == "__main__":
    # Test code to see the format
    s = SudokuReader("sudoku_10.csv")
    print(s.next_board())
