"""
LeetCode 47 - Permutations II

Given an array nums that may contain duplicates, return all possible
unique permutations in any order.

Example 1:
    Input:  nums = [1, 1, 2]
    Output: [[1,1,2],[1,2,1],[2,1,1]]

Example 2:
    Input:  nums = [1, 2, 3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
    - 1 <= len(nums) <= 8

Hint: Sort the array first. During backtracking, skip duplicates by
      checking if nums[i] == nums[i-1] and nums[i-1] was not used.
"""


def permute_unique(nums: list[int]) -> list[list[int]]:
    pass


print(permute_unique([1, 1, 2]))  # Expected: [[1,1,2],[1,2,1],[2,1,1]]
print(len(permute_unique([1, 2, 3])))  # Expected: 6
