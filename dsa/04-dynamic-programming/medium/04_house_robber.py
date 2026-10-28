"""
LeetCode 198 - House Robber

You are robbing houses along a street. Adjacent houses have connected
alarms — you cannot rob two adjacent houses.

Given an array of money in each house, return the maximum you can rob.

Example 1:
    Input:  nums = [1, 2, 3, 1]
    Output: 4  (rob house 0 and 2: 1+3)

Example 2:
    Input:  nums = [2, 7, 9, 3, 1]
    Output: 12  (rob house 0, 2, 4: 2+9+1)

Constraints:
    - 1 <= len(nums) <= 100

Hint: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
"""


def rob(nums: list[int]) -> int:
    pass


print(rob([1, 2, 3, 1]))       # Expected: 4
print(rob([2, 7, 9, 3, 1]))    # Expected: 12
