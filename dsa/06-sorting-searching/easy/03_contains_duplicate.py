"""
LeetCode 217 - Contains Duplicate

Given an integer array nums, return True if any value appears at
least twice, and False if every element is distinct.

Example 1:
    Input:  nums = [1, 2, 3, 1]
    Output: True

Example 2:
    Input:  nums = [1, 2, 3, 4]
    Output: False

Constraints:
    - 1 <= len(nums) <= 10^5

Hint: Use a set to track seen values. O(n) time, O(n) space.
      Or sort first and check adjacent pairs. O(n log n) time, O(1) space.
"""


def contains_duplicate(nums: list[int]) -> bool:
    pass


print(contains_duplicate([1, 2, 3, 1]))  # Expected: True
print(contains_duplicate([1, 2, 3, 4]))  # Expected: False
