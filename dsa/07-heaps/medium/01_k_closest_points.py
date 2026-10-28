"""
LeetCode 973 - K Closest Points to Origin

Given an array of points and an integer k, return the k closest
points to the origin (0, 0). Distance = sqrt(x^2 + y^2).

Example 1:
    Input:  points = [[1,3],[-2,2]], k = 1
    Output: [[-2,2]]

Example 2:
    Input:  points = [[3,3],[5,-1],[-2,4]], k = 2
    Output: [[3,3],[-2,4]]

Constraints:
    - 1 <= k <= len(points) <= 10^4

Hint: Use a max-heap of size k, or use quickselect.
"""

import heapq


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    pass


print(k_closest([[1,3],[-2,2]], 1))            # Expected: [[-2,2]]
print(k_closest([[3,3],[5,-1],[-2,4]], 2))     # Expected: [[3,3],[-2,4]] (order may vary)
