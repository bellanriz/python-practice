"""
LeetCode 51 - N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n
chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution is a list of strings, where 'Q' indicates a queen and
'.' indicates an empty space.

Example 1:
    Input:  n = 4
    Output: [
        [".Q..","...Q","Q...","..Q."],
        ["..Q.","Q...","...Q",".Q.."]
    ]

Example 2:
    Input:  n = 1
    Output: [["Q"]]

Constraints:
    - 1 <= n <= 9

Hint: Use backtracking. Place queens row by row. For each row, try
      each column and check if it's safe (no other queen in the same
      column, or on the same diagonal). Use sets to track occupied
      columns, and both diagonals.
"""


def solve_n_queens(n: int) -> list[list[str]]:
    pass


# Test cases
result = solve_n_queens(4)
for solution in result:
    for row in solution:
        print(row)
    print()
# Expected: 2 solutions for n=4

print(solve_n_queens(1))  # Expected: [["Q"]]
