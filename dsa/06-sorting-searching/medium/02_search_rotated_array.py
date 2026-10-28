"""
LeetCode 33 - Search in Rotated Sorted Array

A sorted array was rotated at an unknown pivot (e.g. [4,5,6,7,0,1,2]).
Given a target, return its index or -1. Must be O(log n).

Example 1:
    Input:  nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:
    Input:  nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

Constraints:
    - 1 <= len(nums) <= 5000
    - All values are unique.

Hint: Binary search. At each step, one half is sorted. Determine
      which half the target is in.
"""


def search(nums: list[int], target: int) -> int:
    pass


print(search([4,5,6,7,0,1,2], 0))  # Expected: 4
print(search([4,5,6,7,0,1,2], 3))  # Expected: -1
print(search([1], 0))               # Expected: -1
