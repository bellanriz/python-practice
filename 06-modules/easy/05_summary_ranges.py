"""
LeetCode 228 - Summary Ranges

Given a sorted unique integer array nums, return the smallest sorted
list of ranges that cover all the numbers exactly.

Each range [a, b] should be output as:
    - "a->b" if a != b
    - "a"    if a == b

Example 1:
    Input:  nums = [0, 1, 2, 4, 5, 7]
    Output: ["0->2", "4->5", "7"]
    Explanation:
        0, 1, 2 form a continuous range -> "0->2"
        4, 5 form a continuous range    -> "4->5"
        7 is alone                      -> "7"

Example 2:
    Input:  nums = [0, 2, 3, 4, 6, 8, 9]
    Output: ["0", "2->4", "6", "8->9"]

Constraints:
    - 0 <= len(nums) <= 20
    - -2^31 <= nums[i] <= 2^31 - 1
    - All values are unique and sorted in ascending order.

Module hint: Consider how itertools.groupby could help group
             consecutive numbers, or solve with a simple loop.
"""

# You may use: from itertools import groupby


def summary_ranges(nums: list[int]) -> list[str]:
    pass


# Test cases
print(summary_ranges([0, 1, 2, 4, 5, 7]))       # Expected: ["0->2", "4->5", "7"]
print(summary_ranges([0, 2, 3, 4, 6, 8, 9]))    # Expected: ["0", "2->4", "6", "8->9"]
