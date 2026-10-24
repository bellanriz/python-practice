"""
LeetCode 303 - Range Sum Query - Immutable

Given an integer array nums, handle multiple queries of the following
type: calculate the sum of elements between indices left and right
inclusive, where left <= right.

Implement the NumArray class:
    - NumArray(nums)              -> initializes with the integer array nums.
    - sum_range(left, right)      -> returns the sum of nums[left..right].

Example:
    na = NumArray([-2, 0, 3, -5, 2, -1])
    na.sum_range(0, 2)   # -> 1   (= -2 + 0 + 3)
    na.sum_range(2, 5)   # -> -1  (= 3 + (-5) + 2 + (-1))
    na.sum_range(0, 5)   # -> -3  (= -2 + 0 + 3 + (-5) + 2 + (-1))

Constraints:
    - 1 <= len(nums) <= 10^4
    - -10^5 <= nums[i] <= 10^5
    - 0 <= left <= right < len(nums)
    - At most 10^4 calls will be made to sum_range.

Hint: Precompute a prefix sum array so each query runs in O(1).
"""


class NumArray:

    def __init__(self, nums: list[int]):
        pass

    def sum_range(self, left: int, right: int) -> int:
        pass


# Test cases
na = NumArray([-2, 0, 3, -5, 2, -1])
print(na.sum_range(0, 2))  # Expected: 1
print(na.sum_range(2, 5))  # Expected: -1
print(na.sum_range(0, 5))  # Expected: -3
