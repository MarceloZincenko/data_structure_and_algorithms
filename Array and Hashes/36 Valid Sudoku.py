#36. Valid Sudoku
import collections

def isValidSudoku(board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                continue
            if board[i][j] in cols[i] or board[i][j] in rows[j] or board[i][j] in squares[(i // 3, j // 3)]:
                return False
            cols[i].add(board[i][j])
            rows[j].add(board[i][j])
            squares[(i // 3,  j // 3)].add(board[i][j])

    return True