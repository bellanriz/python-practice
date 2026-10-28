"""
LeetCode 1464 - Maximum Product of Two Elements in an Array

Given an array of integers, return the maximum value of
(nums[i]-1) * (nums[j]-1) where i != j.

Example 1:
    Input:  nums = [3, 4, 5, 2]
    Output: 12  ((4-1)*(5-1) = 3*4)

Example 2:
    Input:  nums = [1, 5, 4, 5]
    Output: 16  ((5-1)*(5-1) = 4*4)

Constraints:
    - 2 <= len(nums) <= 500

Hint: Find the two largest elements. A heap makes this straightforward.
"""

import heapq


def max_product(nums: list[int]) -> int:
    pass


print(max_product([3, 4, 5, 2]))  # Expected: 12
print(max_product([1, 5, 4, 5]))  # Expected: 16
