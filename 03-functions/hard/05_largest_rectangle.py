"""
LeetCode 84 - Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar
heights (each bar has width 1), return the area of the largest
rectangle in the histogram.

Example 1:
    Input:  heights = [2, 1, 5, 6, 2, 3]
    Output: 10
    Explanation: The largest rectangle has area = 5 * 2 = 10 (using
                 bars of height 5 and 6 at indices 2 and 3).

Example 2:
    Input:  heights = [2, 4]
    Output: 4

Constraints:
    - 1 <= len(heights) <= 10^5
    - 0 <= heights[i] <= 10^4

Hint: A brute-force approach checks all pairs in O(n^2). For O(n),
      use a stack that keeps indices of increasing heights. When you
      encounter a bar shorter than the stack top, pop and calculate
      the area with the popped bar as the shortest bar.
"""


def largest_rectangle_area(heights: list[int]) -> int:
    pass


# Test cases
print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))  # Expected: 10
print(largest_rectangle_area([2, 4]))                # Expected: 4
