"""
LeetCode 503 - Next Greater Element II

Given a circular integer array nums, return the next greater number
for every element. The next greater number is the first greater number
traversing circularly. If none exists, output -1.

Example 1:
    Input:  nums = [1, 2, 1]
    Output: [2, -1, 2]

Example 2:
    Input:  nums = [1, 2, 3, 4, 3]
    Output: [2, 3, 4, -1, 4]

Constraints:
    - 1 <= len(nums) <= 10^4

Hint: Iterate through the array twice (simulate circular) using a
      monotonic stack.
"""


def next_greater_elements(nums: list[int]) -> list[int]:
    pass


print(next_greater_elements([1, 2, 1]))        # Expected: [2, -1, 2]
print(next_greater_elements([1, 2, 3, 4, 3]))  # Expected: [2, 3, 4, -1, 4]
