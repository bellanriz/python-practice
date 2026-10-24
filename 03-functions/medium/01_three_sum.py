"""
LeetCode 15 - 3Sum

Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that:
    - i != j, i != k, and j != k
    - nums[i] + nums[j] + nums[k] == 0

The solution set must not contain duplicate triplets.

Example 1:
    Input:  nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]
    Explanation:
        nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0
        nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0
        nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0
        Distinct triplets are [-1,-1,2] and [-1,0,1].

Example 2:
    Input:  nums = [0, 1, 1]
    Output: []

Example 3:
    Input:  nums = [0, 0, 0]
    Output: [[0, 0, 0]]

Constraints:
    - 3 <= len(nums) <= 3000
    - -10^5 <= nums[i] <= 10^5

Hint: Sort the array first, then use a fixed pointer + two-pointer
      technique. Skip duplicates carefully.
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    pass


# Test cases
print(three_sum([-1, 0, 1, 2, -1, -4]))  # Expected: [[-1, -1, 2], [-1, 0, 1]]
print(three_sum([0, 1, 1]))                # Expected: []
print(three_sum([0, 0, 0]))                # Expected: [[0, 0, 0]]
