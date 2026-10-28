"""
LeetCode 733 - Flood Fill

Given an image (m x n grid of integers), a starting pixel (sr, sc),
and a color, perform a flood fill starting from (sr, sc).

Change the color of the starting pixel and all connected pixels with
the same original color to the new color. Connected means up/down/left/right.

Example 1:
    Input:  image = [[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, color=2
    Output: [[2,2,2],[2,2,0],[2,0,1]]

Example 2:
    Input:  image = [[0,0,0],[0,0,0]], sr=0, sc=0, color=0
    Output: [[0,0,0],[0,0,0]]

Constraints:
    - 1 <= m, n <= 50
"""


def flood_fill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    pass


print(flood_fill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
# Expected: [[2,2,2],[2,2,0],[2,0,1]]
