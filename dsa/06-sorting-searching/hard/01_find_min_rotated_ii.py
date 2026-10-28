"""
LeetCode 154 - Find Minimum in Rotated Sorted Array II

A sorted array (with possible duplicates) was rotated at an unknown
pivot. Find the minimum element.

Example 1:
    Input:  nums = [1, 3, 5]
    Output: 1

Example 2:
    Input:  nums = [2, 2, 2, 0, 1]
    Output: 0

Constraints:
    - 1 <= len(nums) <= 5000
    - nums may contain duplicates.

Hint: Binary search. When nums[mid] == nums[high], you can't decide
      which half — shrink high by 1. Worst case O(n).
"""


def find_min(nums: list[int]) -> int:
    pass


print(find_min([1, 3, 5]))          # Expected: 1
print(find_min([2, 2, 2, 0, 1]))   # Expected: 0
