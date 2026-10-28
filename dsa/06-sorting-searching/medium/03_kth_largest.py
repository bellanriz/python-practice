"""
LeetCode 215 - Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element.
Not the kth distinct element.

Example 1:
    Input:  nums = [3,2,1,5,6,4], k = 2
    Output: 5

Example 2:
    Input:  nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4

Constraints:
    - 1 <= k <= len(nums) <= 10^5

Hint: Use a min-heap of size k, or Quickselect for O(n) average time.
"""

import heapq


def find_kth_largest(nums: list[int], k: int) -> int:
    pass


print(find_kth_largest([3,2,1,5,6,4], 2))          # Expected: 5
print(find_kth_largest([3,2,3,1,2,4,5,5,6], 4))    # Expected: 4
