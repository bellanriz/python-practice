"""
LeetCode 912 - Sort an Array

Given an array of integers, sort it in ascending order.
Do NOT use built-in sort — implement Merge Sort or Quick Sort.

Example 1:
    Input:  nums = [5, 2, 3, 1]
    Output: [1, 2, 3, 5]

Example 2:
    Input:  nums = [5, 1, 1, 2, 0, 0]
    Output: [0, 0, 1, 1, 2, 5]

Constraints:
    - 1 <= len(nums) <= 5 * 10^4
    - -5 * 10^4 <= nums[i] <= 5 * 10^4

Hint: Merge Sort is O(n log n) guaranteed. Quick Sort is O(n log n)
      average but O(n^2) worst-case. Use random pivot to avoid it.
"""


def sort_array(nums: list[int]) -> list[int]:
    pass


print(sort_array([5, 2, 3, 1]))          # Expected: [1, 2, 3, 5]
print(sort_array([5, 1, 1, 2, 0, 0]))    # Expected: [0, 0, 1, 1, 2, 5]
