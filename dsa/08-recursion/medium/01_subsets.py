"""
LeetCode 78 - Subsets

Given an integer array nums of unique elements, return all possible
subsets (the power set). No duplicate subsets allowed.

Example 1:
    Input:  nums = [1, 2, 3]
    Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

Example 2:
    Input:  nums = [0]
    Output: [[], [0]]

Constraints:
    - 1 <= len(nums) <= 10
    - All elements are unique.

Hint: Backtracking — at each index, decide to include or exclude it.
"""


def subsets(nums: list[int]) -> list[list[int]]:
    pass


print(subsets([1, 2, 3]))  # Expected: all 8 subsets
print(subsets([0]))          # Expected: [[], [0]]
