"""
LeetCode 862 - Shortest Subarray with Sum at Least K

Given an integer array nums and an integer k, return the length of
the shortest non-empty subarray with sum >= k. Return -1 if none.

Example 1:
    Input:  nums = [1], k = 1
    Output: 1

Example 2:
    Input:  nums = [1, 2], k = 4
    Output: -1

Example 3:
    Input:  nums = [2, -1, 2], k = 3
    Output: 3

Constraints:
    - 1 <= len(nums) <= 10^5
    - -10^5 <= nums[i] <= 10^5

Hint: Use prefix sums + a deque (monotonic queue). The deque
      maintains indices with increasing prefix sums. For each new
      prefix sum, pop from front while the difference >= k.
"""

from collections import deque


def shortest_subarray(nums: list[int], k: int) -> int:
    pass


print(shortest_subarray([1], 1))        # Expected: 1
print(shortest_subarray([1, 2], 4))     # Expected: -1
print(shortest_subarray([2, -1, 2], 3)) # Expected: 3
