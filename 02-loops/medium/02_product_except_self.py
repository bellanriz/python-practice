"""
LeetCode 238 - Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].

You must solve it WITHOUT using the division operator.
The algorithm should run in O(n) time.

Example 1:
    Input:  nums = [1, 2, 3, 4]
    Output: [24, 12, 8, 6]

Example 2:
    Input:  nums = [-1, 1, 0, -3, 3]
    Output: [0, 0, 9, 0, 0]

Constraints:
    - 2 <= len(nums) <= 10^5
    - -30 <= nums[i] <= 30
    - The product of any prefix or suffix of nums fits in a 32-bit integer.

Hint: Think about prefix and suffix products.
"""


def product_except_self(nums: list[int]) -> list[int]:
    pass


# Test cases
print(product_except_self([1, 2, 3, 4]))          # Expected: [24, 12, 8, 6]
print(product_except_self([-1, 1, 0, -3, 3]))     # Expected: [0, 0, 9, 0, 0]
