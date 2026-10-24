"""
LeetCode 1480 - Running Sum of 1d Array

Given an array nums, return the running sum of the array.
The running sum is defined as runningSum[i] = sum(nums[0]...nums[i]).

Example 1:
    Input:  nums = [1, 2, 3, 4]
    Output: [1, 3, 6, 10]
    Explanation: Running sum is [1, 1+2, 1+2+3, 1+2+3+4]

Example 2:
    Input:  nums = [1, 1, 1, 1, 1]
    Output: [1, 2, 3, 4, 5]

Example 3:
    Input:  nums = [3, 1, 2, 10, 1]
    Output: [3, 4, 6, 16, 17]

Constraints:
    - 1 <= len(nums) <= 1000
    - -10^6 <= nums[i] <= 10^6
"""


def running_sum(nums: list[int]) -> list[int]:
    pass


# Test cases
print(running_sum([1, 2, 3, 4]))        # Expected: [1, 3, 6, 10]
print(running_sum([1, 1, 1, 1, 1]))     # Expected: [1, 2, 3, 4, 5]
print(running_sum([3, 1, 2, 10, 1]))    # Expected: [3, 4, 6, 16, 17]
