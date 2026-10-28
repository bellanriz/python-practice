"""
LeetCode 778 - Swim in Rising Water

An n x n grid where grid[i][j] is the elevation. At time t, the
water depth is t everywhere. You can swim from one cell to an adjacent
cell if both cells have elevation <= t.

Starting at (0,0), return the minimum time to reach (n-1, n-1).

Example 1:
    Input:  grid = [[0,2],[1,3]]
    Output: 3

Example 2:
    Input:  grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],
                    [11,17,18,19,20],[10,9,8,7,6]]
    Output: 16

Constraints:
    - 2 <= n <= 50

Hint: Binary search + BFS, or Dijkstra/min-heap approach where the
      "cost" to reach a cell is the max elevation along the path.
"""

import heapq


def swim_in_water(grid: list[list[int]]) -> int:
    pass


print(swim_in_water([[0,2],[1,3]]))  # Expected: 3
print(swim_in_water([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],
                     [11,17,18,19,20],[10,9,8,7,6]]))  # Expected: 16
