"""
LeetCode 312 - Burst Balloons

Given n balloons, indexed 0..n-1 with values in nums. Bursting
balloon i earns nums[i-1] * nums[i] * nums[i+1] coins (treat out-of-
bounds as 1). Find the maximum coins by bursting all balloons wisely.

Example 1:
    Input:  nums = [3, 1, 5, 8]
    Output: 167
    Explanation: 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 15+120+24+8 = 167

Example 2:
    Input:  nums = [1, 5]
    Output: 10

Constraints:
    - 1 <= n <= 300

Hint: Think about which balloon to burst LAST in a range.
      dp[i][j] = max coins from bursting all balloons in (i, j).
"""


def max_coins(nums: list[int]) -> int:
    pass


print(max_coins([3, 1, 5, 8]))  # Expected: 167
print(max_coins([1, 5]))         # Expected: 10
