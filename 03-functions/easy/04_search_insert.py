"""
LeetCode 35 - Search Insert Position

Given a sorted array of distinct integers and a target value, return
the index if the target is found. If not, return the index where it
would be inserted to keep the array sorted.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input:  nums = [1, 3, 5, 6], target = 5
    Output: 2

Example 2:
    Input:  nums = [1, 3, 5, 6], target = 2
    Output: 1

Example 3:
    Input:  nums = [1, 3, 5, 6], target = 7
    Output: 4

Constraints:
    - 1 <= len(nums) <= 10^4
    - -10^4 <= nums[i] <= 10^4
    - nums contains distinct values sorted in ascending order.
    - -10^4 <= target <= 10^4

Hint: Binary search is the key. Think about what the left pointer
      represents when the search ends.
"""


def search_insert(nums: list[int], target: int) -> int:
    pass


# Test cases
print(search_insert([1, 3, 5, 6], 5))  # Expected: 2
print(search_insert([1, 3, 5, 6], 2))  # Expected: 1
print(search_insert([1, 3, 5, 6], 7))  # Expected: 4
