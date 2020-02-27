import numpy as np


def solve(board, x=0, y=0):
    if x > 8:
        y += 1
        x = 0
        if y == 9:
            return True

    if board[y, x] == 0:
        invalid = find_invalid(board, x, y)
        for guess in range(1, 10):
            board[y, x] = guess
            if guess not in invalid:
                if solve(board, x+1, y):
                    return True
            board[y, x] = 0
        return False
    else:
        if solve(board, x+1, y):
            return True


def find_invalid(board, x, y):
    seen = set()
    # row
    seen = find_unique(board[y, :], seen)
    # column
    seen = find_unique(board[:, x], seen)
    # subbox
    subx = x//3
    suby = y//3
    find_unique(board[suby*3: (suby+1)*3, subx*3: (subx+1)*3].reshape(9), seen)
    return seen


def find_unique(subboard, seen):
    for i in range(0, 9):
        seen.add(subboard[i])
    return seen


def test():
    board = np.fromfile("sudoku_board.txt", dtype=np.int32,
                        sep=" ").reshape((9, 9))
    solve(board)
    print(board)
    board = np.fromfile("sudoku_board2.txt", dtype=np.int32,
                        sep=" ").reshape((9, 9))
    solve(board)
    print(board)
    board = np.fromfile("sudoku_board3.txt", dtype=np.int32,
                        sep=" ").reshape((9, 9))
    solve(board)
    print(board)
    board = np.fromfile("sudoku_solved.txt", dtype=np.int32,
                        sep=" ").reshape((9, 9))
    solve(board)
    print(board)


if __name__ == '__main__':
    import cProfile
    cProfile.run('test()')
