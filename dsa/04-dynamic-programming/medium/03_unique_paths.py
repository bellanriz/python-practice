"""
LeetCode 62 - Unique Paths

A robot is at the top-left corner of an m x n grid. It can only move
right or down. How many unique paths are there to the bottom-right corner?

Example 1:
    Input:  m = 3, n = 7
    Output: 28

Example 2:
    Input:  m = 3, n = 2
    Output: 3

Constraints:
    - 1 <= m, n <= 100

Hint: dp[i][j] = dp[i-1][j] + dp[i][j-1]. Can optimize to 1D array.
"""


def unique_paths(m: int, n: int) -> int:
    pass


print(unique_paths(3, 7))  # Expected: 28
print(unique_paths(3, 2))  # Expected: 3
