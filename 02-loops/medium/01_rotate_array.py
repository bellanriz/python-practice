"""
LeetCode 189 - Rotate Array

Given an integer array nums, rotate the array to the right by k steps.

You must do this in-place (modify the list directly, do not return a new list).

Example 1:
    Input:  nums = [1, 2, 3, 4, 5, 6, 7], k = 3
    Output: [5, 6, 7, 1, 2, 3, 4]
    Explanation:
        rotate 1 step:  [7, 1, 2, 3, 4, 5, 6]
        rotate 2 steps: [6, 7, 1, 2, 3, 4, 5]
        rotate 3 steps: [5, 6, 7, 1, 2, 3, 4]

Example 2:
    Input:  nums = [-1, -100, 3, 99], k = 2
    Output: [3, 99, -1, -100]
    Explanation:
        rotate 1 step:  [99, -1, -100, 3]
        rotate 2 steps: [3, 99, -1, -100]

Constraints:
    - 1 <= len(nums) <= 10^5
    - -2^31 <= nums[i] <= 2^31 - 1
    - 0 <= k <= 10^5

Hint: Think about what happens when k > len(nums).
"""


def rotate(nums: list[int], k: int) -> None:
    pass


# Test cases
nums1 = [1, 2, 3, 4, 5, 6, 7]
rotate(nums1, 3)
print(nums1)  # Expected: [5, 6, 7, 1, 2, 3, 4]

nums2 = [-1, -100, 3, 99]
rotate(nums2, 2)
print(nums2)  # Expected: [3, 99, -1, -100]
