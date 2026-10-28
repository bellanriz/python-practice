"""
LeetCode 378 - Kth Smallest Element in a Sorted Matrix

Given an n x n matrix where each row and column is sorted in
ascending order, return the kth smallest element.

Example 1:
    Input:  matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
    Output: 13

Example 2:
    Input:  matrix = [[-5]], k = 1
    Output: -5

Constraints:
    - n == len(matrix) == len(matrix[i])
    - 1 <= n <= 300
    - 1 <= k <= n^2

Hint: Min-heap starting with first element of each row. Or binary
      search on the value range.
"""

import heapq


def kth_smallest(matrix: list[list[int]], k: int) -> int:
    pass


print(kth_smallest([[1,5,9],[10,11,13],[12,13,15]], 8))  # Expected: 13
print(kth_smallest([[-5]], 1))                             # Expected: -5
