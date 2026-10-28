"""
LeetCode 327 - Count of Range Sum

Given an integer array nums and two integers lower and upper, return
the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i,j) = nums[i] + nums[i+1] + ... + nums[j].

Example 1:
    Input:  nums = [-2, 5, -1], lower = -2, upper = 2
    Output: 3  (ranges: [0,0]=-2, [2,2]=-1, [0,2]=2)

Example 2:
    Input:  nums = [0], lower = 0, upper = 0
    Output: 1

Constraints:
    - 1 <= len(nums) <= 10^5

Hint: Compute prefix sums. Then use modified merge sort to count
      pairs where lower <= prefix[j] - prefix[i] <= upper.
"""


def count_range_sum(nums: list[int], lower: int, upper: int) -> int:
    pass


print(count_range_sum([-2, 5, -1], -2, 2))  # Expected: 3
print(count_range_sum([0], 0, 0))             # Expected: 1
