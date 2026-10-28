"""
LeetCode 463 - Island Perimeter

Given a row x col grid where grid[i][j] = 1 is land and 0 is water,
determine the perimeter of the island. There is exactly one island.

Example 1:
    Input:  grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    Output: 16

Example 2:
    Input:  grid = [[1]]
    Output: 4

Constraints:
    - 1 <= row, col <= 100

Hint: Each land cell contributes 4 to perimeter, minus 2 for each
      adjacent land cell (shared edge).
"""


def island_perimeter(grid: list[list[int]]) -> int:
    pass


print(island_perimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))  # Expected: 16
print(island_perimeter([[1]]))  # Expected: 4
