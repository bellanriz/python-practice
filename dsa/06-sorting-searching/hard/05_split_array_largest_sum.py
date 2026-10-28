"""
LeetCode 410 - Split Array Largest Sum

Given an integer array nums and an integer k, split nums into k
non-empty subarrays to minimize the largest sum among them.

Example 1:
    Input:  nums = [7,2,5,10,8], k = 2
    Output: 18
    Explanation: [7,2,5] and [10,8] -> sums 14 and 18 -> max is 18.

Example 2:
    Input:  nums = [1,2,3,4,5], k = 2
    Output: 9

Constraints:
    - 1 <= len(nums) <= 1000
    - 1 <= k <= min(50, len(nums))

Hint: Binary search on the answer. For a given max_sum, greedily
      check if you can split into <= k subarrays.
"""


def split_array(nums: list[int], k: int) -> int:
    pass


print(split_array([7,2,5,10,8], 2))  # Expected: 18
print(split_array([1,2,3,4,5], 2))   # Expected: 9
