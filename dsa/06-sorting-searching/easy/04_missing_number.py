"""
LeetCode 268 - Missing Number

Given an array nums containing n distinct numbers in range [0, n],
return the only number in the range that is missing.

Example 1:
    Input:  nums = [3, 0, 1]
    Output: 2

Example 2:
    Input:  nums = [0, 1]
    Output: 2

Example 3:
    Input:  nums = [9,6,4,2,3,5,7,0,1]
    Output: 8

Constraints:
    - n == len(nums)
    - All numbers are unique.

Hint: Sum formula: n*(n+1)/2 - sum(nums). Or use XOR.
"""


def missing_number(nums: list[int]) -> int:
    pass


print(missing_number([3, 0, 1]))                  # Expected: 2
print(missing_number([0, 1]))                      # Expected: 2
print(missing_number([9,6,4,2,3,5,7,0,1]))        # Expected: 8
