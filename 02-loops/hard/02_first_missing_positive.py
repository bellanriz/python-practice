"""
LeetCode 41 - First Missing Positive

Given an unsorted integer array nums, return the smallest missing
positive integer.

You must implement an algorithm that runs in O(n) time and uses
O(1) auxiliary space.

Example 1:
    Input:  nums = [1, 2, 0]
    Output: 3
    Explanation: The numbers 1 and 2 are present. 3 is the first missing positive.

Example 2:
    Input:  nums = [3, 4, -1, 1]
    Output: 2
    Explanation: 1 is present but 2 is missing.

Example 3:
    Input:  nums = [7, 8, 9, 11, 12]
    Output: 1
    Explanation: The smallest positive integer 1 is missing.

Constraints:
    - 1 <= len(nums) <= 10^5
    - -2^31 <= nums[i] <= 2^31 - 1

Hint: The answer must be in the range [1, n+1] where n = len(nums).
      Think about placing each number in its "correct" index position.
"""


def first_missing_positive(nums: list[int]) -> int:
    pass


# Test cases
print(first_missing_positive([1, 2, 0]))          # Expected: 3
print(first_missing_positive([3, 4, -1, 1]))      # Expected: 2
print(first_missing_positive([7, 8, 9, 11, 12]))  # Expected: 1
