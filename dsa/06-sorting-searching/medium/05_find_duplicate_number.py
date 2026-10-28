"""
LeetCode 287 - Find the Duplicate Number

Given an array of n+1 integers where each integer is in [1, n],
there is exactly one duplicate. Find it.

You must NOT modify the array and use only O(1) extra space.

Example 1:
    Input:  nums = [1, 3, 4, 2, 2]
    Output: 2

Example 2:
    Input:  nums = [3, 1, 3, 4, 2]
    Output: 3

Constraints:
    - 1 <= n <= 10^5
    - len(nums) == n + 1

Hint: Floyd's Cycle Detection. Treat the array as a linked list where
      index i points to nums[i]. The duplicate creates a cycle.
"""


def find_duplicate(nums: list[int]) -> int:
    pass


print(find_duplicate([1, 3, 4, 2, 2]))  # Expected: 2
print(find_duplicate([3, 1, 3, 4, 2]))  # Expected: 3
