"""
LeetCode 330 - Patching Array

Given a sorted integer array nums and an integer n, add/patch elements
to the array such that any number in the range [1, n] inclusive can be
formed by the sum of some elements in the array.

Return the minimum number of patches required.

Example 1:
    Input:  nums = [1, 3], n = 6
    Output: 1
    Explanation: With [1, 3], we can make: 1, 3, 4 (=1+3).
        We can't make 2, 5, or 6.
        Add 2 -> [1, 2, 3]. Now we can make 1, 2, 3, 4, 5, 6.

Example 2:
    Input:  nums = [1, 5, 10], n = 20
    Output: 2
    Explanation: Add 2 and 4 -> [1, 2, 4, 5, 10].
        Now we can reach all numbers from 1 to 20.

Example 3:
    Input:  nums = [1, 2, 2], n = 5
    Output: 0

Constraints:
    - 1 <= len(nums) <= 1000
    - 1 <= nums[i] <= 10^4
    - nums is sorted in ascending order.
    - 1 <= n <= 2^31 - 1

Hint: Track the smallest number you can't yet reach (call it miss).
      If nums[i] <= miss, you can extend your range. Otherwise, you
      must patch by adding miss itself, which doubles your reachable range.
"""


def min_patches(nums: list[int], n: int) -> int:
    pass


# Test cases
print(min_patches([1, 3], 6))        # Expected: 1
print(min_patches([1, 5, 10], 20))   # Expected: 2
print(min_patches([1, 2, 2], 5))     # Expected: 0
