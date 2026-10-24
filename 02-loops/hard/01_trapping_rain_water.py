"""
LeetCode 42 - Trapping Rain Water

Given n non-negative integers representing an elevation map where
the width of each bar is 1, compute how much water it can trap
after raining.

Example 1:
    Input:  height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    Output: 6
    Explanation: The elevation map [0,1,0,2,1,0,1,3,2,1,2,1]
                 can trap 6 units of rain water.

Example 2:
    Input:  height = [4, 2, 0, 3, 2, 5]
    Output: 9

Constraints:
    - n == len(height)
    - 1 <= n <= 2 * 10^4
    - 0 <= height[i] <= 10^5

Hint: For each position, the water trapped depends on the minimum of
      the max height to its left and the max height to its right,
      minus its own height. Think about how to compute this efficiently.
"""


def trap(height: list[int]) -> int:
    pass


# Test cases
print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # Expected: 6
print(trap([4, 2, 0, 3, 2, 5]))                       # Expected: 9
