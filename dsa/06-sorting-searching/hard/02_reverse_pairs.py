"""
LeetCode 493 - Reverse Pairs

Given an integer array nums, return the number of reverse pairs.
A reverse pair is (i, j) where i < j and nums[i] > 2 * nums[j].

Example 1:
    Input:  nums = [1, 3, 2, 3, 1]
    Output: 2  (pairs: (1,4) and (3,4) => 3>2*1 and 3>2*1)

Example 2:
    Input:  nums = [2, 4, 3, 5, 1]
    Output: 3

Constraints:
    - 1 <= len(nums) <= 5 * 10^4

Hint: Modified merge sort. Count pairs during the merge step.
"""


def reverse_pairs(nums: list[int]) -> int:
    pass


print(reverse_pairs([1, 3, 2, 3, 1]))  # Expected: 2
print(reverse_pairs([2, 4, 3, 5, 1]))  # Expected: 3
