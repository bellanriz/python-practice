"""
LeetCode 300 - Longest Increasing Subsequence

Given an integer array nums, return the length of the longest
strictly increasing subsequence.

Example 1:
    Input:  nums = [10, 9, 2, 5, 3, 7, 101, 18]
    Output: 4  ([2, 3, 7, 101])

Example 2:
    Input:  nums = [0, 1, 0, 3, 2, 3]
    Output: 4

Constraints:
    - 1 <= len(nums) <= 2500

Hint: O(n^2) DP: dp[i] = longest ending at i.
      O(n log n): maintain a "tails" array with binary search.
"""


def length_of_lis(nums: list[int]) -> int:
    pass


print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))  # Expected: 4
print(length_of_lis([0, 1, 0, 3, 2, 3]))              # Expected: 4
