"""
LeetCode 200 - Number of Islands

Given an m x n grid of '1's (land) and '0's (water), count the
number of islands. An island is surrounded by water and formed by
connecting adjacent land cells horizontally or vertically.

Example 1:
    Input:  grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    Output: 1

Example 2:
    Input:  grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    Output: 3

Constraints:
    - 1 <= m, n <= 300

Hint: DFS/BFS from each unvisited '1', marking visited cells.
"""


def num_islands(grid: list[list[str]]) -> int:
    pass


print(num_islands([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]))  # Expected: 1

print(num_islands([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]))  # Expected: 3
