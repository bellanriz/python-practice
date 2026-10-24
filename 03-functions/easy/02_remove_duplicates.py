"""
LeetCode 26 - Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove
the duplicates in-place such that each unique element appears only
once. The relative order of the elements should be kept the same.

Return k — the number of unique elements in nums.

The first k elements of nums should hold the unique values in order.
The remaining elements don't matter.

Example 1:
    Input:  nums = [1, 1, 2]
    Output: k = 2, nums = [1, 2, ...]

Example 2:
    Input:  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    Output: k = 5, nums = [0, 1, 2, 3, 4, ...]

Constraints:
    - 1 <= len(nums) <= 3 * 10^4
    - -100 <= nums[i] <= 100
    - nums is sorted in non-decreasing order.

Hint: Use two pointers — a slow pointer to track where to place the
      next unique element, and a fast pointer to scan through the array.
"""


def remove_duplicates(nums: list[int]) -> int:
    pass


# Test cases
nums1 = [1, 1, 2]
k1 = remove_duplicates(nums1)
print(k1, nums1[:k1])  # Expected: 2 [1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = remove_duplicates(nums2)
print(k2, nums2[:k2])  # Expected: 5 [0, 1, 2, 3, 4]
