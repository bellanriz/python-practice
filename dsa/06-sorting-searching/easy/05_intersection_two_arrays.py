"""
LeetCode 349 - Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their
intersection. Each element in the result must be unique. Order doesn't matter.

Example 1:
    Input:  nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

Example 2:
    Input:  nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4] (order may vary)

Constraints:
    - 1 <= len(nums1), len(nums2) <= 1000

Hint: Use sets. Or sort both arrays and use two pointers.
"""


def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    pass


print(sorted(intersection([1,2,2,1], [2,2])))         # Expected: [2]
print(sorted(intersection([4,9,5], [9,4,9,8,4])))     # Expected: [4, 9]
