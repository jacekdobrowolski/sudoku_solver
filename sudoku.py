import numpy as np


def solve(board, x=0, y=0):
    if x > 8:
        y = y + 1
        x = 0
        if y == 9:
            return True

    if board[y, x] == 0:
        for guess in range(1, 10):
            board[y, x] = guess
            if valid(board, x, y):
                if solve(board, x+1, y):
                    return True
            board[y, x] = 0
        return False
    else:
        if solve(board, x+1, y):
            return True


def valid(board, x, y):
    # row
    if not_unique(board[y, :]):
        return False

    # column
    if not_unique(board[:, x]):
        return False

    # subbox
    subx = x//3
    suby = y//3
    if not_unique(board[suby*3: (suby+1)*3, subx*3: (subx+1)*3]):
        return False

    return True


def not_unique(subboard):
    if np.unique(subboard).sum() != subboard.sum():
        return True
    else:
        return False

if __name__ == '__main__':
    board = np.fromfile("sudoku_board.txt", dtype=np.int32,
                        sep=" ").reshape((9, 9))
    print(solve(board))
    board = np.fromfile("sudoku_board2.txt", dtype=np.int32,
                        sep=" ").reshape((9, 9))
    print(solve(board))
    board = np.fromfile("sudoku_board3.txt", dtype=np.int32,
                        sep=" ").reshape((9, 9))
    print(solve(board))
    board = np.fromfile("sudoku_solved.txt", dtype=np.int32,
                        sep=" ").reshape((9, 9))
    print(solve(board))
