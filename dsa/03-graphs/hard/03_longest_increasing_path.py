"""
LeetCode 329 - Longest Increasing Path in a Matrix

Given an m x n integers matrix, return the length of the longest
increasing path. You can move in 4 directions (up/down/left/right).

Example 1:
    Input:  matrix = [[9,9,4],[6,6,8],[2,1,1]]
    Output: 4  (path: 1->2->6->9)

Example 2:
    Input:  matrix = [[3,4,5],[3,2,6],[2,2,1]]
    Output: 4  (path: 3->4->5->6)

Constraints:
    - 1 <= m, n <= 200

Hint: DFS with memoization. Cache the longest path from each cell.
"""


def longest_increasing_path(matrix: list[list[int]]) -> int:
    pass


print(longest_increasing_path([[9,9,4],[6,6,8],[2,1,1]]))  # Expected: 4
print(longest_increasing_path([[3,4,5],[3,2,6],[2,2,1]]))  # Expected: 4
