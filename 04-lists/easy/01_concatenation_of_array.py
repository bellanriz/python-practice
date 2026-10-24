"""
LeetCode 1929 - Concatenation of Array

Given an integer array nums of length n, you want to create an array
ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i]
for 0 <= i < n.

Basically, ans is the array nums concatenated with itself.

Example 1:
    Input:  nums = [1, 2, 1]
    Output: [1, 2, 1, 1, 2, 1]

Example 2:
    Input:  nums = [1, 3, 2, 1]
    Output: [1, 3, 2, 1, 1, 3, 2, 1]

Constraints:
    - n == len(nums)
    - 1 <= n <= 1000
    - 1 <= nums[i] <= 1000
"""


def get_concatenation(nums: list[int]) -> list[int]:
    pass


# Test cases
print(get_concatenation([1, 2, 1]))        # Expected: [1, 2, 1, 1, 2, 1]
print(get_concatenation([1, 3, 2, 1]))     # Expected: [1, 3, 2, 1, 1, 3, 2, 1]
