"""
LeetCode 239 - Sliding Window Maximum

You are given an array of integers nums and an integer k representing
the size of a sliding window that moves from left to right. Each time
the window moves one position to the right, return the max in that window.

Return a list of the maximum values for each window position.

Example 1:
    Input:  nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    Output: [3, 3, 5, 5, 6, 7]
    Explanation:
        Window position              Max
        -------------------------   -----
        [1  3  -1] -3  5  3  6  7    3
         1 [3  -1  -3] 5  3  6  7    3
         1  3 [-1  -3  5] 3  6  7    5
         1  3  -1 [-3  5  3] 6  7    5
         1  3  -1  -3 [5  3  6] 7    6
         1  3  -1  -3  5 [3  6  7]   7

Example 2:
    Input:  nums = [1], k = 1
    Output: [1]

Constraints:
    - 1 <= len(nums) <= 10^5
    - -10^4 <= nums[i] <= 10^4
    - 1 <= k <= len(nums)

Hint: A brute-force approach checks every window in O(n*k). Can you
      do it in O(n) using a deque (monotonic queue)?
"""

from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    pass


# Test cases
print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Expected: [3, 3, 5, 5, 6, 7]
print(max_sliding_window([1], 1))                            # Expected: [1]
