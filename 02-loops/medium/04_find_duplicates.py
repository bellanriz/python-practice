"""
LeetCode 442 - Find All Duplicates in an Array

Given an integer array nums of length n where all integers are in
the range [1, n] and each integer appears once or twice, return an
array of all the integers that appear twice.

You must solve it in O(n) time and WITHOUT using extra space
(the output array does not count as extra space).

Example 1:
    Input:  nums = [4, 3, 2, 7, 8, 2, 3, 1]
    Output: [2, 3]

Example 2:
    Input:  nums = [1, 1, 2]
    Output: [1]

Example 3:
    Input:  nums = [1]
    Output: []

Constraints:
    - n == len(nums)
    - 1 <= n <= 10^5
    - 1 <= nums[i] <= n
    - Each element appears once or twice.

Hint: Since all numbers are in range [1, n], you can use the array
      indices themselves as a hash. Think about marking visited elements
      by negating values.
"""


def find_duplicates(nums: list[int]) -> list[int]:
    pass


# Test cases
print(find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # Expected: [2, 3]
print(find_duplicates([1, 1, 2]))                    # Expected: [1]
print(find_duplicates([1]))                           # Expected: []
