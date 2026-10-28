"""
LeetCode 174 - Dungeon Game

A knight starts at the top-left of an m x n grid and must reach the
bottom-right (princess). Each cell has an integer — positive (health
gain) or negative (damage).

The knight's health must be >= 1 at all times. Return the minimum
initial health needed to reach the bottom-right alive.

Example 1:
    Input:  dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    Output: 7
    Explanation: Path -2 -> -3 -> 3 -> 1 -> -5 needs 7 initial health.

Constraints:
    - 1 <= m, n <= 200

Hint: Work backwards from the bottom-right. dp[i][j] = min health
      needed at cell (i,j) to survive to the end.
"""


def calculate_minimum_hp(dungeon: list[list[int]]) -> int:
    pass


print(calculate_minimum_hp([[-2,-3,3],[-5,-10,1],[10,30,-5]]))  # Expected: 7
