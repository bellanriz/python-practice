"""
LeetCode 1295 - Find Numbers with Even Number of Digits

Given an array nums of integers, return how many of them contain an
even number of digits.

Example 1:
    Input:  nums = [12, 345, 2, 6, 7896]
    Output: 2
    Explanation:
        12   -> 2 digits (even)
        345  -> 3 digits (odd)
        2    -> 1 digit  (odd)
        6    -> 1 digit  (odd)
        7896 -> 4 digits (even)
        Answer = 2

Example 2:
    Input:  nums = [555, 901, 482, 1771]
    Output: 1
    Explanation: Only 1771 has an even number of digits (4).

Constraints:
    - 1 <= len(nums) <= 500
    - 1 <= nums[i] <= 10^5
"""


def find_numbers(nums: list[int]) -> int:
    pass


# Test cases
print(find_numbers([12, 345, 2, 6, 7896]))     # Expected: 2
print(find_numbers([555, 901, 482, 1771]))      # Expected: 1
