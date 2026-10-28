"""
LeetCode 34 - Find First and Last Position of Element in Sorted Array

Given a sorted array of integers and a target, find the starting and
ending position. If not found, return [-1, -1]. Must be O(log n).

Example 1:
    Input:  nums = [5,7,7,8,8,10], target = 8
    Output: [3, 4]

Example 2:
    Input:  nums = [5,7,7,8,8,10], target = 6
    Output: [-1, -1]

Constraints:
    - 0 <= len(nums) <= 10^5

Hint: Run binary search twice — once for the leftmost and once for
      the rightmost occurrence.
"""


def search_range(nums: list[int], target: int) -> list[int]:
    pass


print(search_range([5,7,7,8,8,10], 8))  # Expected: [3, 4]
print(search_range([5,7,7,8,8,10], 6))  # Expected: [-1, -1]
print(search_range([], 0))                # Expected: [-1, -1]
