"""
LeetCode 1 - Two Sum

Given an array of integers nums and an integer target, return the
indices of the two numbers that add up to target.

You may assume each input has exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

Example 1:
    Input:  nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: nums[0] + nums[1] = 2 + 7 = 9

Example 2:
    Input:  nums = [3, 2, 4], target = 6
    Output: [1, 2]

Example 3:
    Input:  nums = [3, 3], target = 6
    Output: [0, 1]

Constraints:
    - 2 <= len(nums) <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Only one valid answer exists.

Hint: A brute-force approach is O(n^2). Can you do it in O(n) using
      a dictionary to store seen values?
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    pass


# Test cases
print(two_sum([2, 7, 11, 15], 9))  # Expected: [0, 1]
print(two_sum([3, 2, 4], 6))       # Expected: [1, 2]
print(two_sum([3, 3], 6))          # Expected: [0, 1]
