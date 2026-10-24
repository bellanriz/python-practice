"""
LeetCode 75 - Sort Colors

Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red (0), white (1), and blue (2).

You must solve this without using the library sort function.

Example 1:
    Input:  nums = [2, 0, 2, 1, 1, 0]
    Output: [0, 0, 1, 1, 2, 2]

Example 2:
    Input:  nums = [2, 0, 1]
    Output: [0, 1, 2]

Constraints:
    - n == len(nums)
    - 1 <= n <= 300
    - nums[i] is either 0, 1, or 2.

Hint: This is the "Dutch National Flag" problem. Use three pointers:
      low, mid, and high. Process elements at mid and swap to the
      correct position.
"""


def sort_colors(nums: list[int]) -> None:
    pass


# Test cases
nums1 = [2, 0, 2, 1, 1, 0]
sort_colors(nums1)
print(nums1)  # Expected: [0, 0, 1, 1, 2, 2]

nums2 = [2, 0, 1]
sort_colors(nums2)
print(nums2)  # Expected: [0, 1, 2]
