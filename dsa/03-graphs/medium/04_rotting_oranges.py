"""
LeetCode 994 - Rotting Oranges

In a grid: 0=empty, 1=fresh orange, 2=rotten orange. Every minute,
any fresh orange adjacent (4-directional) to a rotten one becomes rotten.

Return the minimum minutes until no fresh orange remains, or -1 if
impossible.

Example 1:
    Input:  grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4

Example 2:
    Input:  grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1

Constraints:
    - 1 <= m, n <= 10

Hint: Multi-source BFS — start from all rotten oranges simultaneously.
"""

from collections import deque


def oranges_rotting(grid: list[list[int]]) -> int:
    pass


print(oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]))  # Expected: 4
print(oranges_rotting([[2,1,1],[0,1,1],[1,0,1]]))   # Expected: -1
