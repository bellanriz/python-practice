"""
LeetCode 46 - Permutations

Given an array nums of distinct integers, return all the possible
permutations. You can return the answer in any order.

Example 1:
    Input:  nums = [1, 2, 3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
    Input:  nums = [0, 1]
    Output: [[0, 1], [1, 0]]

Example 3:
    Input:  nums = [1]
    Output: [[1]]

Constraints:
    - 1 <= len(nums) <= 6
    - -10 <= nums[i] <= 10
    - All the integers of nums are unique.

Hint: Use backtracking. At each step, choose an element that hasn't
      been used yet, add it to the current permutation, and recurse.
"""


def permute(nums: list[int]) -> list[list[int]]:
    pass


# Test cases
print(permute([1, 2, 3]))  # Expected: all 6 permutations of [1,2,3]
print(permute([0, 1]))     # Expected: [[0, 1], [1, 0]]
print(permute([1]))         # Expected: [[1]]
