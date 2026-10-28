"""
LeetCode 79 - Word Search

Given an m x n grid of characters and a string word, return True if
word exists in the grid. The word can be constructed from sequentially
adjacent cells (horizontal/vertical). Same cell cannot be used twice.

Example 1:
    Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
            word = "ABCCED"
    Output: True

Example 2:
    Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
            word = "SEE"
    Output: True

Example 3:
    Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
            word = "ABCB"
    Output: False

Constraints:
    - 1 <= m, n <= 6
    - 1 <= len(word) <= 15

Hint: DFS/backtracking from each cell. Mark visited cells temporarily.
"""


def exist(board: list[list[str]], word: str) -> bool:
    pass


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
print(exist(board, "ABCCED"))  # Expected: True
print(exist(board, "SEE"))      # Expected: True
print(exist(board, "ABCB"))     # Expected: False
