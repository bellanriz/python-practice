"""
LeetCode 417 - Pacific Atlantic Water Flow

Given an m x n grid of heights, water can flow to adjacent cells
(up/down/left/right) if the adjacent cell's height is <= current.

The Pacific ocean touches the left and top edges. The Atlantic ocean
touches the right and bottom edges.

Return a list of cells where water can flow to both oceans.

Example 1:
    Input:  heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Constraints:
    - 1 <= m, n <= 200

Hint: BFS/DFS from ocean edges inward (reverse flow direction).
      Find cells reachable from both oceans.
"""


def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    pass


print(pacific_atlantic([
    [1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]
]))
# Expected: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
