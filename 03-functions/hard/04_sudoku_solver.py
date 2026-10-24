"""
LeetCode 37 - Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

Rules:
    - Each row must contain the digits 1-9 without repetition.
    - Each column must contain the digits 1-9 without repetition.
    - Each of the nine 3x3 sub-boxes must contain 1-9 without repetition.
    - '.' indicates an empty cell.

Example 1:
    Input: board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    Output: (the solved board, modified in-place)
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]

Constraints:
    - board.length == 9
    - board[i].length == 9
    - board[i][j] is a digit or '.'
    - It is guaranteed that the input board has only one solution.

Hint: Use backtracking. Find the next empty cell, try digits 1-9,
      check validity, and recurse. If stuck, backtrack.
"""


def solve_sudoku(board: list[list[str]]) -> None:
    pass


# Test case
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
solve_sudoku(board)
for row in board:
    print(row)
