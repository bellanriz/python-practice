"""
LeetCode 169 - Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than n/2 times.
You may assume that the majority element always exists in the array.

Example 1:
    Input:  nums = [3, 2, 3]
    Output: 3

Example 2:
    Input:  nums = [2, 2, 1, 1, 1, 2, 2]
    Output: 2

Constraints:
    - n == len(nums)
    - 1 <= n <= 5 * 10^4
    - -10^9 <= nums[i] <= 10^9

Module hint: collections.Counter makes this easy with most_common().

Challenge: Can you solve it in O(1) space using Boyer-Moore Voting?
"""

# You may use: from collections import Counter


def majority_element(nums: list[int]) -> int:
    pass


# Test cases
print(majority_element([3, 2, 3]))                # Expected: 3
print(majority_element([2, 2, 1, 1, 1, 2, 2]))    # Expected: 2
