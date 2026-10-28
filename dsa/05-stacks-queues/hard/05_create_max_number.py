"""
LeetCode 321 - Create Maximum Number

Given two integer arrays nums1 and nums2 of lengths m and n, and an
integer k (k <= m + n), create the maximum number of length k from
digits of the two arrays. The relative order of digits from the same
array must be preserved.

Example 1:
    Input:  nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
    Output: [9,8,6,5,3]

Example 2:
    Input:  nums1 = [6,7], nums2 = [6,0,4], k = 5
    Output: [6,7,6,0,4]

Constraints:
    - 1 <= m, n <= 500
    - 0 <= nums1[i], nums2[i] <= 9
    - 1 <= k <= m + n

Hint: For each split (i from nums1, k-i from nums2), find the max
      subsequence of length i from nums1 and length k-i from nums2.
      Then merge them greedily. Take the best across all splits.
"""


def max_number(nums1: list[int], nums2: list[int], k: int) -> list[int]:
    pass


print(max_number([3,4,6,5], [9,1,2,5,8,3], 5))  # Expected: [9,8,6,5,3]
print(max_number([6,7], [6,0,4], 5))              # Expected: [6,7,6,0,4]
