"""
LeetCode 632 - Smallest Range Covering Elements from K Lists

Given k sorted lists of integers, find the smallest range [a, b]
that includes at least one number from each of the k lists.

Example 1:
    Input:  nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
    Output: [20, 24]

Example 2:
    Input:  nums = [[1,2,3],[1,2,3],[1,2,3]]
    Output: [1, 1]

Constraints:
    - 1 <= k <= 3500
    - 1 <= len(nums[i]) <= 50

Hint: Use a min-heap. Start with the first element from each list.
      Track the current max. The range is [heap_min, current_max].
      Pop the min and advance that list's pointer. Update best range.
"""

import heapq


def smallest_range(nums: list[list[int]]) -> list[int]:
    pass


print(smallest_range([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))  # Expected: [20, 24]
print(smallest_range([[1,2,3],[1,2,3],[1,2,3]]))                    # Expected: [1, 1]
