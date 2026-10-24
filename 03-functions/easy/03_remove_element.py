"""
LeetCode 27 - Remove Element

Given an integer array nums and an integer val, remove all occurrences
of val in nums in-place. The order of the elements may be changed.

Return k — the number of elements in nums which are not equal to val.

The first k elements of nums should hold the elements that are not val.

Example 1:
    Input:  nums = [3, 2, 2, 3], val = 3
    Output: k = 2, nums = [2, 2, ...]

Example 2:
    Input:  nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
    Output: k = 5, nums = [0, 1, 3, 0, 4, ...] (any order is fine)

Constraints:
    - 0 <= len(nums) <= 100
    - 0 <= nums[i] <= 50
    - 0 <= val <= 100
"""


def remove_element(nums: list[int], val: int) -> int:
    pass


# Test cases
nums1 = [3, 2, 2, 3]
k1 = remove_element(nums1, 3)
print(k1, sorted(nums1[:k1]))  # Expected: 2 [2, 2]

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
k2 = remove_element(nums2, 2)
print(k2, sorted(nums2[:k2]))  # Expected: 5 [0, 0, 1, 3, 4]
