import numpy as np
    
def solve(board, x=0, y=0):
    if board[y , x] == 0:
        for guess in range(1, 10):
            board[y, x] = guess
            if valid(board, x, y):
                pass
# TODO

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
    if not_unique(board[ suby*3 : (suby+1)*3, subx*3 : (subx+1)*3 ]):
        return False

    return True

def not_unique(subboard):
    if np.unique(subboard).sum() != subboard.sum():
        return True
    else:
        return False

board = np.fromfile("sudoku_board2.txt", dtype = np.int32, sep = "  ").reshape((9,9))
print(board)
solve(board)
print(board)